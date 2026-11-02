"""preview.py LINES.txt [seed] -> preview.png : quick look at handwriting for a few lines of markup"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
from hand import line, seed
def draw(lines, out, U=60, pw=0.05):
    boxes=[line(l) for l in lines]
    W=int(max(b.full_w for b in boxes)*U)+80; H=int(sum(b.bot-b.top+0.5 for b in boxes)*U)+40
    im=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(im); y=20
    for b in boxes:
        y+=-b.top*U
        for st in b.strokes+[s for t in b.tick_strokes for s in t]:
            P=[(40+p[0]*U,y+p[1]*U) for p in st]
            if len(P)==1: P=P*2
            d.line(P,fill=(231,18,36),width=max(1,int(pw/0.38*U)),joint='curve')
        y+=(b.bot+0.5)*U
    im.save(out)
if __name__=='__main__':
    seed(int(sys.argv[2]) if len(sys.argv)>2 else 1)
    draw([l for l in open(sys.argv[1],encoding='utf-8').read().split('\n') if l.strip()],'preview.png')
    print('preview.png')
