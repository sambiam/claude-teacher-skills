"""
inkdoc.py - write handwritten worked solutions as real Word ink over the working grids
of a homework / test .docx.

    python inkdoc.py STUDENT.docx SOLUTIONS_SPEC.py OUT.docx [--pdf] [--seed N]

SOLUTIONS_SPEC.py defines
    SOL = {region_index: [part_lines, part_lines, ...], ...}   # one list per part column
          (a box region can be given as just its list of lines)
    part_lines = ['line markup', '= next line \\tick', ...]   (see hand.py for the markup)
    optional: U_CM (digit height, default 0.30), PEN_CM (0.05), COLOR ('#E71224'),
              HEADER ('WORKED SOLUTIONS (teacher copy)'), TICKS (True),
              NEAT (0.85: 0 = quick and loose, 1 = careful),
              SPLIT ({region: n} - split a full-width region into n equal side-by-side parts)
Run  python grids.py STUDENT.docx  first to see which grid index is which question.
"""
import copy, io, math, os, re, shutil, subprocess, sys, tempfile, zipfile, random
from lxml import etree
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hand
from grids import inventory, NS, q, W
from PIL import Image, ImageDraw

DXA_CM=2.54/1440
EMU_CM=360000

# ---------------------------------------------------------------- block layout
def place_block(lines, Wcm, Hcm, u, overflow_cm=0.45, pad_x=0.25, pad_top=0.14, gap_u=0.22, gap_max_u=0.55):
    """Typeset a part's lines inside a Wcm x Hcm box. Prefers one step per line with '='
    aligned; when the box is too short it chains steps across the line (as a person would),
    then lets the last line run a little below the box, and only then writes smaller."""
    def build(scale):
        items=[]
        ref_eq=None
        for L in lines:
            if L.strip().startswith('@sign'):
                b=hand.sign_diagram(L.strip()[5:]); cont=False
            else:
                b=hand.line(L); cont=L.strip().startswith('=')
            if cont and ref_eq is not None: indent=ref_eq+hand.gv(0,0.08)
            elif cont: indent=0.5
            else: indent=0
            if not cont and getattr(b,'eq',None) is not None: ref_eq=b.eq
            items.append(dict(box=b,cont=cont,indent=max(indent,0)))
        return items
    for scale in (1.0, 1.0, 0.92, 0.85, 0.8):
        us=u*scale
        items=build(scale)
        rows=[[it] for it in items]
        def row_w(r):
            w=0
            for k,it in enumerate(r):
                w+= (it['indent'] if k==0 else (0.5 if it['cont'] else 1.1)) + it['box'].full_w
            return w*us
        def row_h(r): return (max(it['box'].bot for it in r)-min(it['box'].top for it in r))*us
        def total(rs): return pad_top+sum(row_h(r) for r in rs)+gap_u*us*(len(rs)-1)
        # one step per line if it fits (a small run-over below the box is fine);
        # otherwise chain steps sideways until the block fits
        small_over=min(0.15,overflow_cm)
        while total(rows)>Hcm+small_over and len(rows)>1:
            best=None
            for i in range(len(rows)-1):
                cand=rows[i]+rows[i+1]
                if row_w(cand)<=Wcm-pad_x:
                    key=(0 if rows[i+1][0]['cont'] else 1, row_w(cand))
                    if best is None or key<best[0]: best=(key,i)
            if best is None: break
            i=best[1]; rows[i:i+2]=[rows[i]+rows[i+1]]
        if total(rows)<=Hcm+overflow_cm and all(row_w(r)<=Wcm+0.3 for r in rows): break
    # spread lines out evenly into any spare height (neater than packing them at the top)
    spare=Hcm-total(rows)
    if spare>0 and len(rows)>1:
        gap_u=min(gap_max_u, gap_u+spare/(us*(len(rows)-1))*0.6)
    # place
    placed=[]; y=pad_top
    for r in rows:
        top=min(it['box'].top for it in r); bot=max(it['box'].bot for it in r)
        base=y-top*us; x=pad_x
        for k,it in enumerate(r):
            b=it['box']
            x+= (it['indent'] if k==0 else (0.5 if it['cont'] else 1.1))*us
            placed.append(dict(strokes=b.strokes, x=x, base=base, us=us, kind='line'))
            for ts in b.tick_strokes:
                placed.append(dict(strokes=ts, x=x, base=base, us=us, kind='tick'))
            x+=b.full_w*us
        y=base+bot*us+gap_u*us
    used=y-gap_u*us
    return placed, used, us

def to_cm(item, ox, oy):
    return [[(ox+item['x']+p[0]*item['us'], oy+item['base']+p[1]*item['us'], p[2]) for p in st] for st in item['strokes']]

# ---------------------------------------------------------------- ink XML
INK_HEAD=('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<inkml:ink xmlns:inkml="http://www.w3.org/2003/InkML">'
 '<inkml:definitions><inkml:context xml:id="ctx0"><inkml:inkSource xml:id="inkSrc0"><inkml:traceFormat>'
 '<inkml:channel name="X" type="integer" min="-2.14748E9" max="2.14748E9" units="cm"/>'
 '<inkml:channel name="Y" type="integer" min="-2.14748E9" max="2.14748E9" units="cm"/>'
 '<inkml:channel name="F" type="integer" max="32767" units="dev"/></inkml:traceFormat>'
 '<inkml:channelProperties><inkml:channelProperty channel="X" name="resolution" value="1000" units="1/cm"/>'
 '<inkml:channelProperty channel="Y" name="resolution" value="1000" units="1/cm"/>'
 '<inkml:channelProperty channel="F" name="resolution" value="0" units="1/dev"/></inkml:channelProperties>'
 '</inkml:inkSource><inkml:timestamp xml:id="ts0" timeString="{ts}"/></inkml:context>'
 '<inkml:brush xml:id="br0"><inkml:brushProperty name="width" value="{pw}" units="cm"/>'
 '<inkml:brushProperty name="height" value="{pw}" units="cm"/><inkml:brushProperty name="color" value="{col}"/></inkml:brush>'
 '</inkml:definitions>')
def ink_xml(strokes_cm, pw, col, ts):
    x0=min(p[0] for s in strokes_cm for p in s); y0=min(p[1] for s in strokes_cm for p in s)
    out=[INK_HEAD.replace('{pw}',str(pw)).replace('{col}',col).replace('{ts}',ts)]
    t=0.0
    for s in strokes_cm:
        P=[]; last=None
        for x,y,f in s:
            q_=(int(round((x-x0)*1000)),int(round((y-y0)*1000)),max(0,min(32767,int(f))))
            if q_[:2]==last: continue
            last=q_[:2]; P.append(q_)
        if len(P)==1: P.append((P[0][0]+1,P[0][1],3000))
        # Word's own encoding: first point explicit, then first differences ("'" sets the mode)
        pts=['%d %d %d'%P[0]]
        for k in range(1,len(P)):
            d=[P[k][j]-P[k-1][j] for j in range(3)]
            pts.append(("'%d'%d'%d" if k==1 else '%d %d %d')%tuple(d))
        out.append('<inkml:trace contextRef="#ctx0" brushRef="#br0"%s>%s</inkml:trace>'%('' if t==0 else ' timeOffset="%d"'%t, ','.join(pts)))
        t+=180+random.random()*250
    out.append('</inkml:ink>')
    return ''.join(out)

def fallback_png(strokes_cm, pw, col, dpi=300):
    pad=pw/2
    x0=min(p[0] for s in strokes_cm for p in s)-pad; y0=min(p[1] for s in strokes_cm for p in s)-pad
    x1=max(p[0] for s in strokes_cm for p in s)+pad; y1=max(p[1] for s in strokes_cm for p in s)+pad
    SS=4                                   # draw 4x larger then downsample = smooth, anti-aliased edges
    k=dpi/2.54*SS
    W_,H_=max(2,int((x1-x0)*k)+1),max(2,int((y1-y0)*k)+1)
    mask=Image.new('L',(W_,H_),0); d=ImageDraw.Draw(mask)
    wpx=max(1,pw*k); r=wpx/2
    for s in strokes_cm:
        P=[((x-x0)*k,(y-y0)*k) for x,y,f in s]
        if len(P)==1: P=P*2
        d.line(P,fill=255,width=int(round(wpx)))
        for x,y in P:                      # round joins and caps at every vertex
            d.ellipse((x-r,y-r,x+r,y+r),fill=255)
    mask=mask.resize((max(1,W_//SS),max(1,H_//SS)),Image.LANCZOS)
    rgb=tuple(int(col[i:i+2],16) for i in (1,3,5))
    im=Image.new('RGBA',mask.size,rgb+(0,)); im.putalpha(mask)
    b=io.BytesIO(); im.save(b,'PNG'); return b.getvalue()

SHAPETYPE='''<v:shapetype id="_x0000_t75" coordsize="21600,21600" o:spt="75" o:preferrelative="t" path="m@4@5l@4@11@9@11@9@5xe" filled="f" stroked="f"><v:stroke joinstyle="miter"/><v:formulas><v:f eqn="if lineDrawn pixelLineWidth 0"/><v:f eqn="sum @0 1 0"/><v:f eqn="sum 0 0 @1"/><v:f eqn="prod @2 1 2"/><v:f eqn="prod @3 21600 pixelWidth"/><v:f eqn="prod @3 21600 pixelHeight"/><v:f eqn="sum @0 0 1"/><v:f eqn="prod @6 1 2"/><v:f eqn="prod @7 21600 pixelWidth"/><v:f eqn="sum @8 21600 0"/><v:f eqn="prod @7 21600 pixelHeight"/><v:f eqn="sum @10 21600 0"/></v:formulas><v:path o:extrusionok="f" gradientshapeok="t" o:connecttype="rect"/><o:lock v:ext="edit" aspectratio="t"/></v:shapetype>'''
NSDECL=('xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
 'xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" '
 'xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" '
 'xmlns:wp14="http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing" '
 'xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml" '
 'xmlns:wpi="http://schemas.microsoft.com/office/word/2010/wordprocessingInk" '
 'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
 'xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" '
 'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"')
def run_xml(docpr_id, rid_ink, rid_png, offx_cm, offy_cm, w_cm, h_cm, pw, z, with_shapetype):
    E=lambda cm:int(round(cm*EMU_CM))
    pad=E(pw)  # effect extent ~ pen
    cx,cy=max(E(w_cm),1),max(E(h_cm),1)
    pt=lambda cm: cm/2.54*72
    vml_style=('position:absolute;margin-left:%.2fpt;margin-top:%.2fpt;width:%.2fpt;height:%.2fpt;z-index:%d;visibility:visible;'
        'mso-wrap-style:square;mso-wrap-distance-left:9pt;mso-wrap-distance-top:0;mso-wrap-distance-right:9pt;mso-wrap-distance-bottom:0;'
        'mso-position-horizontal:absolute;mso-position-horizontal-relative:text;mso-position-vertical:absolute;mso-position-vertical-relative:text')%(
        pt(offx_cm-pw/2),pt(offy_cm-pw/2),pt(w_cm+pw),pt(h_cm+pw),z)
    return ('<w:r %s><w:rPr><w:noProof/></w:rPr><mc:AlternateContent><mc:Choice Requires="wpi"><w:drawing>'
     '<wp:anchor distT="0" distB="0" distL="114300" distR="114300" simplePos="0" relativeHeight="%d" behindDoc="0" locked="0" layoutInCell="1" allowOverlap="1">'
     '<wp:simplePos x="0" y="0"/><wp:positionH relativeFrom="column"><wp:posOffset>%d</wp:posOffset></wp:positionH>'
     '<wp:positionV relativeFrom="paragraph"><wp:posOffset>%d</wp:posOffset></wp:positionV>'
     '<wp:extent cx="%d" cy="%d"/><wp:effectExtent l="%d" t="%d" r="%d" b="%d"/><wp:wrapNone/>'
     '<wp:docPr id="%d" name="Ink %d"/><wp:cNvGraphicFramePr/>'
     '<a:graphic><a:graphicData uri="http://schemas.microsoft.com/office/word/2010/wordprocessingInk">'
     '<w14:contentPart bwMode="auto" r:id="%s"><w14:nvContentPartPr><w14:cNvContentPartPr/></w14:nvContentPartPr>'
     '<w14:xfrm><a:off x="0" y="0"/><a:ext cx="%d" cy="%d"/></w14:xfrm></w14:contentPart></a:graphicData></a:graphic>'
     '</wp:anchor></w:drawing></mc:Choice><mc:Fallback><w:pict>%s<v:shape id="Ink %d" o:spid="_x0000_s%d" type="#_x0000_t75" style="%s">'
     '<v:imagedata r:id="%s" o:title=""/></v:shape></w:pict></mc:Fallback></mc:AlternateContent></w:r>')%(
     NSDECL, z, E(offx_cm), E(offy_cm), cx, cy, pad, pad, pad, pad, docpr_id, docpr_id, rid_ink, cx, cy,
     SHAPETYPE if with_shapetype else '', docpr_id, 4000+docpr_id, vml_style, rid_png)

# ---------------------------------------------------------------- main
def build(student, spec_path, out, make_pdf=False, seed=None):
    spec={}; exec(open(spec_path,encoding='utf-8').read(), spec)
    SOL=spec['SOL']; U=spec.get('U_CM',0.38); PW=spec.get('PEN_CM',0.042); COL=spec.get('COLOR','#E71224')
    TICKS=spec.get('TICKS',True); SPLIT=spec.get('SPLIT',{}); HEADER=spec.get('HEADER','WORKED SOLUTIONS (teacher copy)')
    hand.set_neat(spec.get('NEAT',0.85)); hand.seed(seed if seed is not None else spec.get('SEED',11)); random.seed(3)
    tmp=tempfile.mkdtemp(); zin=zipfile.ZipFile(student)
    files={n:zin.read(n) for n in zin.namelist()}
    root=etree.fromstring(files['word/document.xml'])
    rels=etree.fromstring(files['word/_rels/document.xml.rels'])
    ct=etree.fromstring(files['[Content_Types].xml'])
    rid_n=max([int(m) for m in re.findall(r'rId(\d+)',files['word/_rels/document.xml.rels'].decode())]+[0])+1
    ids=[int(x) for x in root.xpath('//wp:docPr/@id',namespaces={'wp':'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing'})]
    docpr=max(ids+[0])+1; z=251700000
    grids=inventory(root); report=[]
    ink_n=0; first=True
    import datetime; ts=datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.000')
    tick_total=0; mark_total=0
    for gi,parts in SOL.items():
        nt=sum(l.count('\\tick') for part in ([parts] if parts and isinstance(parts[0],str) else parts) for l in part)
        exp=grids[gi]['marks']; tick_total+=nt; mark_total+=exp or 0
        if exp is not None and nt!=exp: report.append('!! region %d: %d ticks but the paper says [%d marks]'%(gi,nt,exp))
    for gi,parts in SOL.items():
        gd=grids[gi]; DX=DXA_CM
        rowh=[h*DX for h in gd['heights']]; H=sum(rowh); cols=gd['cols']; parts_w=gd['parts']
        if gi in SPLIT: parts_w=[sum(parts_w)/SPLIT[gi]]*SPLIT[gi]       # side-by-side parts the paper doesn't mark out
        x_start=gd['x0']*DX
        if isinstance(parts,list) and parts and isinstance(parts[0],str): parts=[parts]   # a box may be given as a plain list of lines
        for pj,lines in enumerate(parts):
            Wcm=parts_w[pj]*DX if pj<len(parts_w) else (sum(cols)*DX-x_start)
            ox=x_start; x_start+=Wcm
            if not lines: continue
            lines=[l if TICKS else l.replace('\\tick','') for l in lines]
            placed,used,us=place_block(lines,Wcm,H,U)
            report.append('%s %d part %d: %.2f of %.2f cm used%s%s'%(gd['kind'],gi,pj,used,H,' (runs %.2f cm below box)'%(used-H) if used>H else '',' at %.0f%% size'%(us/U*100) if us<U*0.99 else ''))
            for item in placed:
                st=to_cm(item,ox,0)
                xs=[p[0] for s in st for p in s]; ys=[p[1] for s in st for p in s]
                bx0,by0,bx1,by1=min(xs),min(ys),max(xs),max(ys)
                # anchor in the working-space cell under the ink's top-left corner
                r=0; acc=0
                while r<len(rowh)-1 and acc+rowh[r]<=by0: acc+=rowh[r]; r+=1
                tc=None; cx=0; tc_x=0
                for t in gd['rows'][r].findall('w:tc',NS):            # last cell starting left of the ink
                    sp=t.find('w:tcPr/w:gridSpan',NS); sp=int(sp.get(q('val'))) if sp is not None else 1
                    left=sum(cols[:cx])*DX
                    if tc is None or left<=bx0+1e-6: tc=t; tc_x=left
                    cx+=sp
                p=tc.find('w:p',NS)
                if p is None: p=etree.SubElement(tc,q('p'))
                offx=bx0-tc_x-gd['margin']*DX; offy=by0-acc
                ink_n+=1; name='inkh%d.xml'%ink_n
                files['word/ink/'+name]=ink_xml(st,PW,COL,ts).encode('utf-8')
                files['word/media/inkh%d.png'%ink_n]=fallback_png(st,PW,COL)
                rid_i='rId%d'%rid_n; rid_p='rId%d'%(rid_n+1); rid_n+=2
                etree.SubElement(rels,'{http://schemas.openxmlformats.org/package/2006/relationships}Relationship',Id=rid_i,
                    Type='http://schemas.openxmlformats.org/officeDocument/2006/relationships/customXml',Target='ink/'+name)
                etree.SubElement(rels,'{http://schemas.openxmlformats.org/package/2006/relationships}Relationship',Id=rid_p,
                    Type='http://schemas.openxmlformats.org/officeDocument/2006/relationships/image',Target='media/inkh%d.png'%ink_n)
                etree.SubElement(ct,'{http://schemas.openxmlformats.org/package/2006/content-types}Override',PartName='/word/ink/'+name,ContentType='application/inkml+xml')
                runel=etree.fromstring(run_xml(docpr,rid_i,rid_p,offx,offy,bx1-bx0,by1-by0,PW,z,first)); first=False
                p.append(runel); docpr+=1; z+=1
    if not any(e.get('Extension')=='png' for e in ct):
        etree.SubElement(ct,'{http://schemas.openxmlformats.org/package/2006/content-types}Default',Extension='png',ContentType='image/png')
    # header: Name field -> WORKED SOLUTIONS
    if HEADER:
        for t in root.iter(q('t')):
            if t.text and t.text.strip().startswith('Name:'):
                t.text=HEADER
                rpr=t.getparent().find('w:rPr',NS)
                if rpr is None: rpr=etree.SubElement(t.getparent(),q('rPr')); t.getparent().insert(0,rpr)
                c=rpr.find('w:color',NS)
                if c is None: c=etree.SubElement(rpr,q('color'))
                c.set(q('val'),COL[1:]); break
    files['word/document.xml']=etree.tostring(root,xml_declaration=True,encoding='UTF-8',standalone=True)
    files['word/_rels/document.xml.rels']=etree.tostring(rels,xml_declaration=True,encoding='UTF-8',standalone=True)
    files['[Content_Types].xml']=etree.tostring(ct,xml_declaration=True,encoding='UTF-8',standalone=True)
    with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as zo:
        order=['[Content_Types].xml']+[n for n in files if n!='[Content_Types].xml']
        for n in order: zo.writestr(n,files[n])
    report.append('ticks %d / marks %d%s'%(tick_total,mark_total,'' if tick_total==mark_total else '   <-- CHECK'))
    print('\n'.join(report)); print('%d ink objects written -> %s'%(ink_n,out))
    if make_pdf:
        od=os.path.dirname(os.path.abspath(out))
        subprocess.run(['soffice','--headless','--convert-to','pdf','--outdir',od,out],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,timeout=240)
        print('pdf ->',os.path.splitext(out)[0]+'.pdf')
if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser(); ap.add_argument('student'); ap.add_argument('spec'); ap.add_argument('out')
    ap.add_argument('--pdf',action='store_true'); ap.add_argument('--seed',type=int)
    a=ap.parse_args(); build(a.student,a.spec,a.out,a.pdf,a.seed)
