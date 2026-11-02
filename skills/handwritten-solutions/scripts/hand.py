"""
hand.py - typeset maths in Sam's handwriting as ink strokes.

Units: 1u = digit height. y is DOWN, baseline at y=0, so a digit spans y=-1..0.
A Box holds strokes (lists of [x, y, pressure]) plus width/top/bottom extents.

Markup (a small LaTeX subset):
  \\frac{a}{b}   x^{2}  x^2   \\sqrt{x}  \\sqrt[3]{x}   \\pi \\theta \\times \\div \\deg
  \\therefore  \\gt \\lt  \\,  (thin space)   \\quad   \\tick (mark tick, drawn at line end)
  ( ) are stretched automatically to cover what they enclose. A plain space is a word gap.
"""
import json, math, os, random, re
HERE=os.path.dirname(os.path.abspath(__file__))
RNG=random.Random(7)
NEAT=0.85          # 0 = loose and quick, 1 = careful; scales every random variation and how picky the sample choice is
def seed(s): RNG.seed(s)
def set_neat(v):
    global NEAT, LIB
    NEAT=max(0.0,min(1.0,float(v))); LIB=_load()
def F(): return 1-0.65*NEAT          # multiplier on random variation
def g(mu,sd): return RNG.gauss(mu,sd)
def gv(mu,sd): return RNG.gauss(mu,sd*F())

# ------------------------------------------------------------------ glyph library
def _read_lib():
    """glyphs.b64 = zlib+base64 JSON {char: [{s:[[x0,y0,x1,y1..]..], w, src}]} in 1/250 u"""
    import base64, zlib
    raw=json.loads(zlib.decompress(base64.b64decode(open(os.path.join(HERE,'glyphs.b64')).read().replace('\n',''))))
    lib={}
    for c,vs in raw.items():
        lib[c]=[]
        for v in vs:
            sts=[]
            for st in v['s']:
                pts=[(st[i]/250.0,st[i+1]/250.0) for i in range(0,len(st),2)]
                sts.append(pen_static(neaten(catmull(pts,3))))
            lib[c].append(dict(strokes=sts,w=v['w']/250.0,src=v['src']))
    return lib
def smooth(pts, step=0.015, sigma=2.6, corner_deg=55):
    """Steady a stroke: resample evenly, split at real corners, Gaussian-smooth each piece.
    Removes digitiser jitter / hand shake but keeps the corners of 4, 7, 1 and ticks."""
    if len(pts)<3: return list(pts)
    # resample by arc length
    out=[pts[0]]; carry=0.0
    for a,b in zip(pts,pts[1:]):
        L=math.hypot(b[0]-a[0],b[1]-a[1]); t=step-carry
        while t<=L:
            out.append((a[0]+(b[0]-a[0])*t/L,a[1]+(b[1]-a[1])*t/L)); t+=step
        carry=L-(t-step)
    if math.hypot(out[-1][0]-pts[-1][0],out[-1][1]-pts[-1][1])>1e-6: out.append(pts[-1])
    if len(out)<5: return out
    # corners: direction change over a short window
    w=3; cuts=[0]
    for i in range(w,len(out)-w):
        a=out[i-w]; b=out[i]; c=out[i+w]
        v1=(b[0]-a[0],b[1]-a[1]); v2=(c[0]-b[0],c[1]-b[1])
        n1=math.hypot(*v1); n2=math.hypot(*v2)
        if n1<1e-9 or n2<1e-9: continue
        cosang=(v1[0]*v2[0]+v1[1]*v2[1])/(n1*n2)
        if cosang<math.cos(math.radians(corner_deg)) and i-cuts[-1]>2*w: cuts.append(i)
    cuts.append(len(out)-1)
    R=int(3*sigma); ker=[math.exp(-(k*k)/(2*sigma*sigma)) for k in range(-R,R+1)]
    res=[]
    for s0,s1 in zip(cuts,cuts[1:]):
        seg=out[s0:s1+1]; n=len(seg); sm=[]
        for i in range(n):
            if i==0 or i==n-1: sm.append(seg[i]); continue
            r=min(R,i,n-1-i)          # shrink the window near the ends so endpoints stay put
            ks=ker[R-r:R+r+1]; tot=sum(ks)
            sm.append((sum(ks[j]*seg[i-r+j][0] for j in range(len(ks)))/tot, sum(ks[j]*seg[i-r+j][1] for j in range(len(ks)))/tot))
        res.extend(sm if not res else sm[1:])
    return res
def rdp(pts, eps):
    if len(pts)<3: return list(pts)
    a,b=pts[0],pts[-1]; L=math.hypot(b[0]-a[0],b[1]-a[1]) or 1e-9
    dmax=-1; idx=0
    for i in range(1,len(pts)-1):
        p=pts[i]; d=abs((b[0]-a[0])*(a[1]-p[1])-(a[0]-p[0])*(b[1]-a[1]))/L
        if d>dmax: dmax=d; idx=i
    if dmax>eps: return rdp(pts[:idx+1],eps)[:-1]+rdp(pts[idx:],eps)
    return [a,b]
def neaten(pts, corner_deg=55):
    """Neat-pen stroke: smooth away shake, reduce to the few points that carry the shape,
    then redraw through them with a spline - Sam's letter shapes, drawn with a steady hand."""
    if len(pts)<3: return list(pts)
    xs=[q[0] for q in pts]; ys=[q[1] for q in pts]
    if max(max(xs)-min(xs),max(ys)-min(ys))<0.2: return list(pts)   # dots, primes, tiny marks: leave as drawn
    p=smooth(pts, sigma=4.0, corner_deg=corner_deg)
    p=rdp(p, 0.022)
    return catmull(p, 8)
def pen_static(pts):
    n=len(pts); return [[x,y,int(2500+6000*min(1,(i+1)/3,(n-i)/3))] for i,(x,y) in enumerate(pts)]
def _load():
    lib=_read_lib()
    out={}
    for c,vs in lib.items():
        ws=sorted(v['w'] for v in vs); med=ws[len(ws)//2]
        keep=[]
        for v in vs:
            if not (0.6*med<=v['w']<=1.5*med): continue
            if c=='i' and len(v['strokes'])<2: continue
            if c in '()' and v['w']>0.45: continue
            keep.append(v)
        out[c]=keep or vs
    for c,bad in (('b',['P234']),):
        out[c]=[v for v in out.get(c,[]) if v['src'] not in bad and v['w']<0.8]
    def ext(v):
        ys=[p[1] for st in v['strokes'] for p in st]; xs=[p[0] for st in v['strokes'] for p in st]
        return max(xs)-min(xs), max(ys)-min(ys)
    def straight(v):
        pts=[p for st in v['strokes'] for p in st]; a,b=pts[0],pts[-1]
        L=math.hypot(b[0]-a[0],b[1]-a[1]) or 1
        return max(abs((b[0]-a[0])*(a[1]-p[1])-(a[0]-p[0])*(b[1]-a[1]))/L for p in pts)
    MAXW={'0':0.72,'2':0.85,'3':0.75,'5':0.8,'6':0.7,'8':0.7,'9':0.65,'4':0.8,'7':0.75}
    MAXW.update({'u':0.55,'n':0.6,'e':0.6,'o':0.55,'a':0.6,'s':0.5,'c':0.5})
    for c,mw in MAXW.items(): out[c]=[v for v in out.get(c,[]) if v['w']<=mw] or out.get(c,[])
    out['-']=[v for v in out['-'] if ext(v)[1]<=0.16*ext(v)[0]] or out['-']
    out['1']=[v for v in out['1'] if straight(v)<0.09] or out['1']
    def eq_ok(v):              # two separate, level bars that sit over each other (never a z or a staircase)
        if len(v['strokes'])!=2: return False
        (a,b)=[(min(p[0] for p in st),max(p[0] for p in st),min(p[1] for p in st),max(p[1] for p in st)) for st in v['strokes']]
        ov=min(a[1],b[1])-max(a[0],b[0]); short=min(a[1]-a[0],b[1]-b[0])
        level=all((r[3]-r[2])<0.35*(r[1]-r[0]) for r in (a,b))
        return short>0 and ov>0.7*short and level and min(a[1]-a[0],b[1]-b[0])>0.6*max(a[1]-a[0],b[1]-b[0])
    out['=']=[v for v in out['='] if eq_ok(v)] or out['=']
    def plus_ok(v):            # two strokes crossing near both their middles (not a dagger or an inverted T)
        if len(v['strokes'])!=2: return False
        bb=[(min(p[0] for p in st),max(p[0] for p in st),min(p[1] for p in st),max(p[1] for p in st)) for st in v['strokes']]
        h=[b for b in bb if (b[1]-b[0])>=(b[3]-b[2])]; vt=[b for b in bb if (b[1]-b[0])<(b[3]-b[2])]
        if len(h)!=1 or len(vt)!=1: return False
        h=h[0]; vt=vt[0]; hy=(h[2]+h[3])/2; vx=(vt[0]+vt[1])/2
        fy=(hy-vt[2])/max(vt[3]-vt[2],1e-9); fx=(vx-h[0])/max(h[1]-h[0],1e-9)
        return 0.3<fy<0.7 and 0.3<fx<0.7
    out['+']=[v for v in out['+'] if plus_ok(v)] or out['+']
    for c in ('.','t','-'): out.pop(c,None)       # synthetic versions read better (a clean minus never looks like ~)
    # --- neatness: keep the most typical samples, and pull each one's slant towards Sam's usual lean
    def slant(v):
        pts=[p for st in v['strokes'] for p in st]; n=len(pts)
        mx=sum(p[0] for p in pts)/n; my=sum(p[1] for p in pts)/n
        vy=sum((p[1]-my)**2 for p in pts) or 1e-9
        return sum((p[0]-mx)*(p[1]-my) for p in pts)/vy, my
    def bar_score(v):          # '=', '+', '-', '×': two clean strokes, '=' bars level and parallel
        sc=0 if len(v['strokes'])==(1 if c=='-' else 2) else 1.0
        if c in '=-':
            for st in v['strokes']:
                dx=st[-1][0]-st[0][0] or 1e-9; sc+=abs((st[-1][1]-st[0][1])/dx)
                sc+=ext({'strokes':[st]})[1]/max(ext({'strokes':[st]})[0],1e-9)
        return sc
    letters=set('0123456789abcdefghijklmnopqrstuvwxyzACPVLθ')
    sl_all=[slant(v)[0] for c2 in out if c2 in letters for v in out[c2]]
    sl_all.sort(); usual=sl_all[len(sl_all)//2] if sl_all else 0
    for c,vs in list(out.items()):
        if len(vs)>=4:
            ws=sorted(v['w'] for v in vs); mw=ws[len(ws)//2]
            def score(v):
                sc=abs(math.log(max(v['w'],1e-3)/mw))
                if c in letters: sc+=1.5*abs(slant(v)[0]-usual)
                if c in '=+-×': sc+=bar_score(v)
                return sc
            keep=max(3,int(math.ceil(len(vs)*(1-0.45*NEAT))))
            vs=sorted(vs,key=score)[:keep]
        if c in letters:
            nv=[]
            for v in vs:
                k,my=slant(v); d=(k-usual)*0.7*NEAT
                st=[[[p[0]-d*(p[1]-my),p[1],p[2]] for p in s_] for s_ in v['strokes']]
                x0=min(p[0] for s_ in st for p in s_)
                st=[[[p[0]-x0,p[1],p[2]] for p in s_] for s_ in st]
                nv.append(dict(v,strokes=st,w=max(p[0] for s_ in st for p in s_)))
            vs=nv
        out[c]=vs
    return out

def catmull(pts, n=6):
    if len(pts)<3: 
        out=[]
        for a,b in zip(pts,pts[1:]):
            for k in range(n): t=k/n; out.append((a[0]+(b[0]-a[0])*t,a[1]+(b[1]-a[1])*t))
        out.append(pts[-1]); return out
    P=[pts[0]]+list(pts)+[pts[-1]]; out=[]
    for i in range(1,len(P)-2):
        p0,p1,p2,p3=P[i-1],P[i],P[i+1],P[i+2]
        for k in range(n):
            t=k/n; t2=t*t; t3=t2*t
            out.append(tuple(0.5*((2*p1[j])+(-p0[j]+p2[j])*t+(2*p0[j]-5*p1[j]+4*p2[j]-p3[j])*t2+(-p0[j]+3*p1[j]-3*p2[j]+p3[j])*t3) for j in range(2)))
    out.append(pts[-1]); return out
def pen(pts):
    """polyline -> stroke with a pressure profile like a real pen-down / pen-up"""
    n=len(pts); s=[]
    for i,(x,y) in enumerate(pts):
        f=min(1,(i+1)/3,(n-i)/3)
        s.append([x,y,int(2500+6000*f+RNG.uniform(-400,400))])
    return s
def wobble(pts, amp=0.012):
    """low-frequency hand tremor"""
    ph=RNG.uniform(0,6.3); ph2=RNG.uniform(0,6.3); out=[]
    L=0; prev=pts[0]
    for x,y in pts:
        L+=math.hypot(x-prev[0],y-prev[1]); prev=(x,y)
        out.append((x+amp*math.sin(L*7+ph), y+amp*math.sin(L*6+ph2)))
    return out
# synthetic glyphs for letters with no harvested sample: polylines in glyph units
SYN={
 'V':[[(0,-1),(0.28,0),(0.58,-1.02)]],
 'L':[[(0.02,-1),(0,0),(0.5,0.0)]],
 'A':[[(0,0),(0.3,-1),(0.6,0)],[(0.12,-0.38),(0.48,-0.4)]],
 'R':[[(0,0),(0,-1),(0.38,-0.95),(0.45,-0.72),(0.3,-0.52),(0.02,-0.5)],[(0.12,-0.5),(0.48,0)]],
 'O':[[(0.35,-1),(0.08,-0.85),(0,-0.45),(0.15,-0.05),(0.42,0),(0.62,-0.3),(0.6,-0.8),(0.35,-1),(0.25,-0.95)]],
 'r':[[(0,-0.6),(0.01,0)],[(0.01,-0.35),(0.12,-0.55),(0.3,-0.62),(0.42,-0.55)]],
 'd':[[(0.42,-0.42),(0.25,-0.6),(0.05,-0.5),(0.02,-0.15),(0.2,0),(0.4,-0.15)],[(0.44,-1.0),(0.43,0.0)]],
 'h':[[(0,-1),(0,0)],[(0,-0.35),(0.15,-0.58),(0.35,-0.6),(0.42,-0.35),(0.42,0)]],
 'v':[[(0,-0.6),(0.22,0),(0.44,-0.62)]],
 'w':[[(0,-0.6),(0.15,0),(0.3,-0.45),(0.45,0),(0.6,-0.62)]],
 'k':[[(0,-1),(0,0)],[(0.35,-0.6),(0.02,-0.3),(0.38,0)]],
 'z':[[(0,-0.6),(0.4,-0.6),(0,0),(0.42,0)]],
 'j':[[(0.25,-0.6),(0.25,0.25),(0.12,0.4),(0,0.32)],[(0.25,-0.85),(0.26,-0.82)]],
 "'":[[(0.12,-1.18),(0.0,-0.72)]],
 '/':[[(0.45,-1.05),(0,0.15)]],
 '°':[[(0.12,-1),(0.02,-0.92),(0.05,-0.8),(0.17,-0.79),(0.22,-0.9),(0.12,-1)]],
 '>':[[(0,-0.75),(0.45,-0.45),(0,-0.15)]],
 '<':[[(0.45,-0.75),(0,-0.45),(0.45,-0.15)]],
 '÷':[[(0,-0.45),(0.5,-0.45)],[(0.25,-0.72),(0.26,-0.7)],[(0.25,-0.2),(0.26,-0.18)]],
 '∴':[[(0.0,-0.05),(0.02,-0.04)],[(0.4,-0.05),(0.42,-0.04)],[(0.2,-0.42),(0.22,-0.41)]],
 '≤':[[(0.45,-0.8),(0,-0.55),(0.45,-0.3)],[(0,-0.12),(0.45,-0.12)]],
 '≥':[[(0,-0.8),(0.45,-0.55),(0,-0.3)],[(0,-0.12),(0.45,-0.12)]],
 '±':[[(0,-0.6),(0.5,-0.6)],[(0.25,-0.85),(0.25,-0.35)],[(0,-0.15),(0.5,-0.15)]],
 ':':[[(0.05,-0.5),(0.06,-0.49)],[(0.05,-0.08),(0.06,-0.07)]],
 '%':[[(0.5,-1),(0,0)],[(0.08,-1),(0.0,-0.85),(0.1,-0.72),(0.18,-0.85),(0.08,-1)],[(0.42,-0.28),(0.34,-0.14),(0.44,0),(0.52,-0.14),(0.42,-0.28)]],
}
# simple upright capitals and extra symbols (used only where no real sample exists)
SYN.update({
 'B':[[(0,0),(0,-1),(0.32,-0.98),(0.42,-0.82),(0.3,-0.55),(0.02,-0.52)],[(0.02,-0.52),(0.38,-0.48),(0.48,-0.27),(0.36,-0.04),(0,0)]],
 'D':[[(0,0),(0,-1),(0.3,-0.96),(0.5,-0.7),(0.52,-0.35),(0.34,-0.05),(0,0)]],
 'E':[[(0.46,-1),(0,-1),(0,0),(0.48,0)],[(0,-0.52),(0.36,-0.52)]],
 'F':[[(0.46,-1),(0,-1),(0,0)],[(0,-0.52),(0.36,-0.52)]],
 'G':[[(0.5,-0.85),(0.3,-1),(0.06,-0.85),(0,-0.45),(0.16,-0.05),(0.42,0),(0.55,-0.25),(0.55,-0.45),(0.32,-0.45)]],
 'H':[[(0,-1),(0,0)],[(0.5,-1),(0.5,0)],[(0,-0.5),(0.5,-0.5)]],
 'I':[[(0.1,-1),(0.1,0)],[(0,-1),(0.2,-1)],[(0,0),(0.2,0)]],
 'J':[[(0.42,-1),(0.42,-0.25),(0.3,-0.02),(0.12,0),(0,-0.18)]],
 'K':[[(0,-1),(0,0)],[(0.46,-1),(0.02,-0.45),(0.48,0)]],
 'M':[[(0,0),(0.02,-1),(0.3,-0.4),(0.58,-1),(0.6,0)]],
 'N':[[(0,0),(0,-1),(0.5,0),(0.5,-1)]],
 'Q':[[(0.3,-1),(0.06,-0.85),(0,-0.45),(0.15,-0.05),(0.36,0),(0.56,-0.3),(0.55,-0.8),(0.3,-1)],[(0.34,-0.25),(0.6,0.05)]],
 'S':[[(0.46,-0.9),(0.28,-1),(0.06,-0.9),(0.08,-0.62),(0.4,-0.42),(0.48,-0.18),(0.3,0),(0.04,-0.08)]],
 'T':[[(0,-1),(0.56,-1)],[(0.28,-1),(0.28,0)]],
 'U':[[(0,-1),(0,-0.3),(0.12,-0.04),(0.3,0),(0.46,-0.12),(0.5,-0.4),(0.5,-1)]],
 'W':[[(0,-1),(0.16,0),(0.34,-0.6),(0.52,0),(0.68,-1)]],
 'X':[[(0,-1),(0.5,0)],[(0.5,-1),(0,0)]],
 'Y':[[(0,-1),(0.26,-0.5),(0.52,-1)],[(0.26,-0.5),(0.26,0)]],
 'Z':[[(0,-1),(0.5,-1),(0,0),(0.52,0)]],
 'q':[[(0.38,-0.5),(0.2,-0.6),(0.04,-0.48),(0.04,-0.12),(0.22,-0.02),(0.4,-0.15)],[(0.42,-0.6),(0.42,0.38),(0.52,0.32)]],
 ';':[[(0.1,-0.5),(0.11,-0.49)],[(0.12,-0.08),(0.1,0.1),(0.0,0.22)]],
 '!':[[(0.05,-1),(0.05,-0.3)],[(0.05,-0.05),(0.06,-0.04)]],
 '?':[[(0,-0.82),(0.18,-1),(0.4,-0.92),(0.42,-0.7),(0.22,-0.5),(0.2,-0.3)],[(0.2,-0.05),(0.21,-0.04)]],
 '[':[[(0.2,-1.1),(0,-1.1),(0,0.2),(0.2,0.2)]],
 ']':[[(0,-1.1),(0.2,-1.1),(0.2,0.2),(0,0.2)]],
 '|':[[(0,-1.1),(0,0.2)]],
 '∞':[[(0.4,-0.45),(0.25,-0.62),(0.06,-0.55),(0.04,-0.35),(0.2,-0.28),(0.4,-0.45),(0.6,-0.62),(0.78,-0.55),(0.78,-0.35),(0.6,-0.28),(0.4,-0.45)]],
 '→':[[(0,-0.45),(0.6,-0.45)],[(0.45,-0.58),(0.62,-0.45),(0.45,-0.32)]],
 '$':[[(0.4,-0.85),(0.22,-0.92),(0.04,-0.82),(0.08,-0.58),(0.36,-0.42),(0.42,-0.18),(0.22,-0.06),(0.02,-0.14)],[(0.22,-1.05),(0.22,0.1)]],
 '≈':[[(0,-0.58),(0.12,-0.66),(0.26,-0.58),(0.4,-0.5),(0.52,-0.58)],[(0,-0.36),(0.12,-0.44),(0.26,-0.36),(0.4,-0.28),(0.52,-0.36)]],
 '≠':[[(0,-0.58),(0.5,-0.58)],[(0,-0.32),(0.5,-0.32)],[(0.36,-0.78),(0.14,-0.12)]],
})
LIB=_load()
TICK=[[(0.04,-0.32),(0.17,0.0),(0.62,-0.9)]]
SYN['-']=[[(0.0,-0.44),(0.24,-0.455),(0.46,-0.47)]]
SYN['.']=[[(0.0,-0.04),(0.05,-0.02),(0.03,0.0)]]
SYN['t']=[[(0.17,-0.95),(0.16,-0.3),(0.2,-0.04),(0.3,0),(0.4,-0.06)],[(0.0,-0.6),(0.38,-0.63)]]

class Box:
    def __init__(s,strokes=None,w=0,top=-1,bot=0,kind='ord'):
        s.strokes=strokes or []; s.w=w; s.top=top; s.bot=bot; s.kind=kind; s.marks=[]
    def shifted(s,dx,dy):
        b=Box([[[p[0]+dx,p[1]+dy,p[2]] for p in st] for st in s.strokes],s.w,s.top+dy,s.bot+dy,s.kind)
        b.marks=[(x+dx,y+dy,k) for x,y,k in s.marks]; return b
    def scaled(s,k):
        b=Box([[[p[0]*k,p[1]*k,p[2]] for p in st] for st in s.strokes],s.w*k,s.top*k,s.bot*k,s.kind)
        b.marks=[(x*k,y*k,kk) for x,y,kk in s.marks]; return b

_last={}
def glyph(c, sx=1.0, sy=1.0):
    """one handwritten instance of character c (never the same variant twice running)"""
    if c in LIB and LIB[c]:
        vs=LIB[c]; i=RNG.randrange(len(vs))
        if len(vs)>1 and _last.get(c)==i: i=(i+1)%len(vs)
        _last[c]=i; v=vs[i]
        strokes=[[list(p) for p in st] for st in v['strokes']]; w=v['w']
    elif c in SYN:
        strokes=[pen(neaten(catmull([(x+gv(0,0.008),y+gv(0,0.008)) for x,y in st]))) for st in SYN[c]]
        w=max(p[0] for st in strokes for p in st)-min(p[0] for st in strokes for p in st)
    else:
        raise KeyError('no handwriting glyph for %r - add a sample or a SYN entry'%c)
    # per-instance variation: size, slant, rotation, baseline
    k=gv(1,0.045); kx=k*gv(1,0.03)*sx; ky=k*sy; sh=gv(0.0,0.045); rot=math.radians(gv(0,1.6)); dy=gv(0,0.03)
    ca,sa=math.cos(rot),math.sin(rot)
    out=[]
    for st in strokes:
        ns=[]
        for x,y,p in st:
            x=x*kx-y*ky*sh; y=y*ky
            x,y=x*ca-y*sa, x*sa+y*ca
            ns.append([x,y+dy,p])
        out.append(ns)
    xs=[p[0] for st in out for p in st]; ys=[p[1] for st in out for p in st]
    x0=min(xs)
    out=[[[p[0]-x0,p[1],p[2]] for p in st] for st in out]
    kind='prime' if c=="'" else 'op' if c in '=+-×÷<>≤≥±≈≠→' else ('open' if c=='(' else ('close' if c==')' else ('punct' if c in '.,' else 'ord')))
    return Box(out,max(xs)-x0,min(ys),max(ys),kind)

def tick_box():
    st=[pen(smooth(catmull([(x*0.9+gv(0,0.02),y*0.9+gv(0,0.02)) for x,y in TICK[0]]),corner_deg=40))]
    return Box(st,0.6,-0.8,0.05,'tick')

# ------------------------------------------------------------------ parser
CMDS={'pi':'π','theta':'θ','times':'×','div':'÷','deg':'°','therefore':'∴','gt':'>','lt':'<','le':'≤','ge':'≥','pm':'±','cdot':'.','prime':"'",'infty':'∞','ln':'ln','log':'log','sin':'sin','cos':'cos','tan':'tan','to':'→','approx':'≈','neq':'≠','ne':'≠','dollar':'$'}
def tokenize(s):
    toks=[];i=0
    while i<len(s):
        c=s[i]
        if c=='\\':
            m=re.match(r'\\([A-Za-z]+|.)',s[i:]); toks.append('\\'+m.group(1)); i+=len(m.group(0))
            if s[i:i+1]==' ' and m.group(1).isalpha(): i+=1   # swallow the space that ends a command
        else: toks.append(c); i+=1
    return toks
class P:
    def __init__(s,toks): s.t=toks; s.i=0
    def peek(s): return s.t[s.i] if s.i<len(s.t) else None
    def take(s): s.i+=1; return s.t[s.i-1]
    def row(s,stop=None):
        items=[]
        while s.peek() is not None and s.peek()!=stop:
            a=s.atom()
            if a is None: continue
            while s.peek() in ('^','_'):
                op=s.take(); arg=s.arg()
                a=('sup' if op=='^' else 'sub',a,arg)
            items.append(a)
        if stop: s.take()
        return ('row',items)
    def arg(s):
        if s.peek()=='{': s.take(); return s.row('}')
        return ('row',[s.atom()])
    def atom(s):
        t=s.take()
        if t=='{': return s.row('}')
        if t=='\\frac': a=s.arg(); b=s.arg(); return ('frac',a,b)
        if t=='\\sqrt':
            idx=None
            if s.peek()=='[': s.take(); idx=s.row(']')
            return ('sqrt',s.arg(),idx)
        if t=='\\tick': return ('tick',)
        if t=='\\,': return ('space',0.18)
        if t=='\\quad': return ('space',0.9)
        if t=='\\qquad': return ('space',1.8)
        if t.startswith('\\'):
            if t[1:] in CMDS:
                v=CMDS[t[1:]]
                return ('ch',v) if len(v)==1 else ('row',[('ch',ch) for ch in v])
            raise KeyError('unknown command '+t)
        if t==' ': return ('space',0.42)
        if t=='-' : return ('ch','-')
        if t=='*': return ('ch','×')
        return ('ch',t)

# ------------------------------------------------------------------ layout
def hline(x0,x1,y,slope=None):
    """a hand-drawn bar (fraction line / vinculum): slightly rising, slightly bowed"""
    slope=gv(-0.02*F(),0.012) if slope is None else slope
    n=8; pts=[]; bow=0.025*F()*g(1,0.5)
    for k in range(n+1):
        t=k/n; x=x0+(x1-x0)*t
        pts.append((x, y+slope*(x-x0)+bow*math.sin(math.pi*t)))
    return pen(smooth(pts))
def layout(node, depth=0):
    kind=node[0]
    if kind=='ch': return glyph(node[1])
    if kind=='space': return Box([],node[1]*g(1,0.15),-0.6,0,'space')
    if kind=='tick': return Box([],0,-0.6,0,'tickmark')
    if kind=='row': return layout_row(node[1],depth)
    if kind=='sup':
        b=layout(node[1],depth); e=layout(node[2],depth+1).scaled(0.62)
        base_top=b.top if b.kind!='close' else b.top+0.15
        inner=[n for n in node[2][1] if n!=('ch','-')] if node[2][0]=='row' else []
        if len(inner)==1 and inner[0][0]=='frac':       # fractional index: centre it on the top of the base
            e=e.shifted(b.w+0.08+gv(0,0.02), min(base_top+0.3,-0.45)+gv(0,0.03)-e.bot)
        else:
            yb=min(base_top+0.42,-0.5)+gv(0,0.03)          # baseline of the exponent
            e=e.shifted(b.w+0.07+gv(0,0.02), yb-e.bot)
        out=Box(b.strokes+e.strokes,b.w+0.07+e.w,min(b.top,e.top),b.bot); out.marks=b.marks+e.marks; return out
    if kind=='sub':
        b=layout(node[1],depth); e=layout(node[2],depth+1).scaled(0.6); e=e.shifted(b.w+0.03,0.25-e.bot+0.1)
        return Box(b.strokes+e.strokes,b.w+0.03+e.w,b.top,max(b.bot,e.bot))
    if kind=='frac':
        k=0.82 if depth==0 else 0.9
        gn,gd=(0.2,0.21) if depth==0 else (0.14,0.16)
        n=layout(node[1],depth).scaled(k); d=layout(node[2],depth).scaled(k)
        W=max(n.w,d.w)+0.22; bar=-0.42+gv(0,0.02)
        n=n.shifted((W-n.w)/2+gv(0,0.03), bar-gn-n.bot)
        d=d.shifted((W-d.w)/2+gv(0,0.03), bar+gd-d.top)
        out=Box(n.strokes+[hline(0,W,bar)]+d.strokes,W,n.top,d.bot,'frac'); out.marks=n.marks+d.marks; return out
    if kind=='sqrt':
        c=layout(node[1],depth); T=c.top-0.14; B=max(c.bot,0)
        x_in=0.55; mid=B-0.5*(B-T)
        pts=[(0,mid+0.08),(0.08,mid-0.02),(0.24,B+0.05),(0.44,T),(0.47,T-0.01)]
        pts=[(x+g(0,0.015),y+g(0,0.015)) for x,y in pts]
        st=pen(smooth(catmull(pts,4),corner_deg=40))
        bar=hline(0.47,x_in+c.w+0.12,T,g(-0.01,0.01))
        c2=c.shifted(x_in,0)
        strokes=[st+bar[1:]]+c2.strokes
        top=T-0.05; xo=0
        if node[2] is not None:
            ix=layout(node[2],depth+1).scaled(0.55); ix=ix.shifted(-0.2,mid-0.08-ix.bot)
            strokes=strokes+ix.strokes; top=min(top,ix.top)
        out=Box(strokes,x_in+c.w+0.14,top,B+0.05,'sqrt'); out.marks=c2.marks; return out
    raise ValueError(kind)
def gap(a,b):
    if a.kind in ('space',) or b.kind in ('space',): return 0
    if b.kind=='tickmark' or a.kind=='tickmark': return 0
    if b.kind=='prime': return gv(0.03,0.01)
    if a.kind=='prime': return gv(0.14,0.02)
    if a.kind=='op' or b.kind=='op': return gv(0.2+0.05*NEAT,0.04)
    if a.kind=='open' or b.kind=='close': return gv(0.05+0.02*NEAT,0.02)
    if b.kind=='punct': return gv(0.12,0.02)
    if a.kind=='punct': return gv(0.15,0.03)
    return gv(0.11+0.04*NEAT,0.035)
def layout_row(items,depth=0):
    boxes=[layout(it,depth) for it in items]
    # stretch brackets to cover what they enclose
    stack=[]; pairs=[]
    for i,it in enumerate(items):
        if it==('ch','('): stack.append(i)
        elif it==('ch',')') and stack: pairs.append((stack.pop(),i))
    for a,b in pairs:
        inner=[bx for bx in boxes[a+1:b] if bx.strokes]
        if not inner: continue
        T=min(bx.top for bx in inner)-0.1; B=max(bx.bot for bx in inner)+0.1
        T=min(T,-1.08); B=max(B,0.18)
        for i in (a,b):
            c=items[i][1]; base=glyph(c); h=base.bot-base.top; ky=(B-T)/h
            st=[[[p[0]*min(1.25,ky**0.35),T+(p[1]-base.top)*ky,p[2]] for p in s] for s in base.strokes]
            boxes[i]=Box(st,base.w*min(1.25,ky**0.35),T,B,base.kind)
    x=0; strokes=[]; top=-0.6; bot=0; marks=[]; prev=None; first_eq=None
    for it,bx in zip(items,boxes):
        if bx.kind=='tickmark': marks.append((x,0,'tick')); continue
        if prev is not None: x+=gap(prev,bx)
        if it==('ch','=') and first_eq is None: first_eq=x
        sb=bx.shifted(x,0); strokes+=sb.strokes; marks+=sb.marks
        top=min(top,bx.top); bot=max(bot,bx.bot); x+=bx.w; prev=bx
    out=Box(strokes,x,top,bot,'row'); out.marks=marks; out.eq=first_eq; return out

def line(markup):
    """typeset one line of working; returns Box (+ .ticks = number of \\tick marks, .eq = x of first '=')"""
    toks=tokenize(markup.strip())
    tree=P(toks).row()
    b=layout(tree)
    # gentle drift of the whole line: rising slope + wander
    sl=gv(-0.006*F(),0.006); ph=RNG.uniform(0,6.3); wa=0.0
    b.strokes=[[[p[0],p[1]+sl*p[0]+wa*math.sin(p[0]*0.7+ph),p[2]] for p in st] for st in b.strokes]
    b.ticks=sum(1 for m in b.marks if m[2]=='tick')
    # mark ticks: drawn after the end of the line, one per mark
    b.tick_strokes=[]
    x=b.w+0.45
    for k in range(b.ticks):
        t=tick_box().shifted(x+g(0,0.04),g(-0.05,0.04)); b.tick_strokes.append(t.strokes); x+=0.75
    b.full_w=x if b.ticks else b.w
    return b

def sign_diagram(spec):
    """'+ 15 -'  ->  number line with arrowheads, a tick at each root, signs above"""
    toks=spec.split(); seg=2.1; n_roots=sum(1 for t in toks if t not in '+-'); W=seg*(n_roots+1)
    strokes=[hline(0,W,0,g(-0.01,0.008))]
    for sx in (0,W):
        d=-1 if sx==0 else 1
        strokes.append(pen([(sx-d*0.22,-0.16),(sx,0),(sx-d*0.22,0.15)]))
    x=0; ri=0
    for t in toks:
        if t in '+-':
            gb=glyph(t).shifted(x+seg*0.5-0.25,-0.55); strokes+=gb.strokes
        else:
            ri+=1; x=seg*ri
            strokes.append(pen([(x,-0.25),(x+gv(0,0.02),0.25)]))
            lb=line(t).scaled(0.7); lb=lb.shifted(x-lb.w/2,-0.4); strokes+=lb.strokes
            x=seg*ri
    b=Box(strokes,W,-1.2,0.3,'row'); b.ticks=0; b.tick_strokes=[]; b.full_w=W; b.eq=None
    return b
