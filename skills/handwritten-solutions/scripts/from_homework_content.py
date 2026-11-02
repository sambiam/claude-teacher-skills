"""
from_homework_content.py - draft a handwritten-solutions spec from an exam-revision-homework content.py

    python from_homework_content.py content.py WEEK > spec.py

Every ('w', ...) working block becomes one grid region, in order, and each T(text, ticks)
solution line becomes one handwritten line with `ticks` x \\tick. Text outside $...$ is kept as
words; LaTeX inside is simplified to the handwriting markup. ALWAYS read and edit the draft:
match Sam's taught methods and notation (handwritten-solutions Step 1-2), drop typed-solution
habits ("Check:", long prose), and split or merge lines the way he would write them.
"""
import re, sys
def conv_math(m):
    m=re.sub(r'\\(?:left|right|big|Big|bigg)\s*([()\[\]|.])',lambda k:'' if k.group(1)=='.' else k.group(1),m)
    m=re.sub(r'\\(?:mathrm|text|textrm|operatorname|mathit)\{([^{}]*)\}',r'\1',m)
    m=re.sub(r"\^\{\\prime\}|\^\\prime","'",m)
    m=m.replace(r'\dfrac',r'\frac').replace(r'\tfrac',r'\frac').replace(r'\cdot',r'\times').replace(r'\ ',' ')
    m=m.replace(r'\circ',r'\deg').replace('^{\\deg}',r'\deg').replace(r'\leq',r'\le').replace(r'\geq',r'\ge')
    m=m.replace('~',' ').replace(r'\!','').replace(r'\;',' ').replace(r'\:',' ')
    m=re.sub(r'\\(?:displaystyle|quad\s*)',lambda k:r'\quad ' if 'quad' in k.group(0) else '',m)
    return m
def conv(s):
    s=s.replace(r'\$','$DOLLAR$')
    out=[]
    for i,part in enumerate(re.split(r'(?<!\\)\$',s)):
        if part=='DOLLAR': out.append('$'); continue
        out.append(conv_math(part) if i%2 else part.replace('✓',''))
    t=' '.join(''.join(out).split())
    return t
def main(path, week):
    ns={}; exec(open(path,encoding='utf-8').read(), ns)
    wk=ns['WEEKS'][int(week)]
    print('# Draft handwritten spec from %s, week %s - edit before building.'%(path,week))
    print('SOL = {')
    k=0
    for b in wk['blocks']:
        if b[0]!='w': continue
        d=b[1]
        cols=[[conv(txt)+(' \\tick'*n) for txt,n in col] for col in d['sol']]
        print(' %d: [  # marks=%s'%(k,d.get('marks')))
        for col in cols:
            print('   [' + ',\n    '.join('r"%s"'%l.replace('"','\\"') for l in col) + '],')
        print(' ],')
        k+=1
    print('}')
if __name__=='__main__': main(sys.argv[1], sys.argv[2])
