"""
grids.py - find every working space in a homework / test / worksheet .docx.

    python grids.py STUDENT.docx

Three layouts are recognised (all made by Sam's skills):
  grid   a squared working grid (table with >= 10 grid columns): exam-revision-homework,
         test-build, practice-test-build. Its part columns (a | b | c) come from a label row
         inside the grid's first row, or from a borderless label table straight above it.
  box    an empty working cell in a row of answer boxes under a row of questions
         (worksheet-build, senior-homework-build); each empty cell is its own region.
  slot   an empty fixed-height single-cell strip (test-build slot()) - also a box.
Each region gets an index; the solutions spec is keyed by that index.
"""
import re, sys, zipfile
from lxml import etree
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'
NS={'w':W,'m':'http://schemas.openxmlformats.org/officeDocument/2006/math'}
def q(t): return '{%s}%s'%(W,t)
def text_of(el):
    return ''.join(t.text for t in el.iter() if t.tag in (q('t'),'{%s}t'%NS['m']) and t.text)
def has_content(el):
    return bool(text_of(el).strip()) or el.find('.//'+q('drawing')) is not None or el.find('.//{%s}oMath'%NS['m']) is not None
def row_height(tr):
    h=tr.find('w:trPr/w:trHeight',NS)
    return (int(h.get(q('val'))),h.get(q('hRule')) or 'atLeast') if h is not None else (None,None)
def span(tc):
    s=tc.find('w:tcPr/w:gridSpan',NS); return int(s.get(q('val'))) if s is not None else 1
def cell_margin(tbl):
    m=tbl.find('w:tblPr/w:tblCellMar/w:left',NS)
    return int(m.get(q('w'))) if m is not None else 108
MARKS=re.compile(r'[\[(](\d+)\s*marks?[\])]',re.I)
def marks_after(kids,i):
    for e in kids[i+1:i+3]:
        m=MARKS.search(text_of(e))
        if m: return int(m.group(1))
    return None
def inventory(doc_root):
    body=doc_root.find('w:body',NS); kids=list(body); regions=[]
    for i,tbl in enumerate(kids):
        if tbl.tag!=q('tbl'): continue
        cols=[int(c.get(q('w'))) for c in tbl.findall('w:tblGrid/w:gridCol',NS)]
        rows=tbl.findall('w:tr',NS); mar=cell_margin(tbl)
        if len(cols)>=10:                                     # ---- squared grid
            work=[r for r in rows if row_height(r)[0] and not has_content(r)]
            if not work: continue
            label=[r for r in rows if r not in work and has_content(r)]
            splits=None; ctx=[]
            if label:                                         # labels inside the grid's first row
                tcs=label[0].findall('w:tc',NS)
                splits=[sum(cols[sum(span(t) for t in tcs[:k]):sum(span(t) for t in tcs[:k+1])]) for k in range(len(tcs))]
                ctx.append(' | '.join(text_of(t) for t in tcs))
            j=i-1
            while j>=0 and len(ctx)<3:
                e=kids[j]
                if e.tag==q('tbl') and len(e.findall('w:tblGrid/w:gridCol',NS))>=10: break
                if e.tag==q('tbl') and splits is None and j==i-1:
                    tcs=e.findall('w:tr/w:tc',NS)
                    if len(tcs)>=2:
                        splits=[int(tc.find('w:tcPr/w:tcW',NS).get(q('w'))) for tc in tcs]
                        ctx.insert(0,' | '.join(text_of(tc) for tc in tcs)); j-=1; continue
                t=text_of(e).strip()
                if t: ctx.insert(0,t)
                j-=1
            if splits and len(splits)==1: splits=None
            regions.append(dict(kind='grid',tbl=tbl,rows=work,heights=[row_height(r)[0] for r in work],cols=cols,x0=0,
                                parts=splits or [sum(cols)],margin=mar,marks=marks_after(kids,i),context=' / '.join(ctx)[-160:]))
        else:                                                 # ---- answer boxes / slots
            for ri,tr in enumerate(rows):
                h,rule=row_height(tr)
                if not h or h<500: continue
                x=0
                for tc in tr.findall('w:tc',NS):
                    w=sum(cols[x:x+span(tc)]) if cols else int(tc.find('w:tcPr/w:tcW',NS).get(q('w')))
                    if not has_content(tc):
                        # context: the question cell above this one
                        ctx=''
                        if ri>0:
                            xx=0
                            for up in rows[ri-1].findall('w:tc',NS):
                                if xx==x: ctx=text_of(up)
                                xx+=span(up)
                        if not ctx:
                            j=i-1
                            while j>=0 and not text_of(kids[j]).strip(): j-=1
                            ctx=text_of(kids[j]) if j>=0 else ''
                        regions.append(dict(kind='box',tbl=tbl,rows=[tr],heights=[h],cols=cols,x0=sum(cols[:x]) if cols else 0,
                                            parts=[w],margin=mar,marks=marks_after(kids,i) if len(rows)==1 else None,
                                            context=ctx.strip()[:160],rule=rule))
                    x+=span(tc)
    for k,r in enumerate(regions): r['index']=k
    return regions
if __name__=='__main__':
    root=etree.fromstring(zipfile.ZipFile(sys.argv[1]).read('word/document.xml'))
    for g in inventory(root):
        print('%s %d: %d rows (%.2f cm), parts=%d widths(cm)=%s, marks=%s :: %s'%(g['kind'],g['index'],len(g['heights']),sum(g['heights'])/567.0,
              len(g['parts']),[round(s/567,2) for s in g['parts']],g['marks'],g['context']))
