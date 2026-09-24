---
name: "draft-feedback"
description: "Mark a class set of student drafts (maths investigations, reports, assignments) against a task sheet or template: add teacher-named Word comments, highlight spelling/grammar in yellow, and give an on-track summary table. Use for 'give feedback on these drafts', 'comment on the progress check', 'mark these drafts' or when handed a folder of student work."
---

# Draft feedback

Turn a folder of student drafts into commented copies a teacher can hand straight back. Each copy is identical to the original apart from Word comments (attributed to the teacher) and yellow highlighting on spelling and grammar errors. You also produce a one-page summary that places every student against the teacher's benchmarks.

## Inputs to expect

- **The task sheet and/or the student template.** Read these first. They tell you what each part of the task needs, and which text is the template's own. Never comment on template wording, even when it's wrong (for example a heading that says "maximum" when the task is about a minimum). Mention template problems to the teacher in your summary instead.
- **An exemplar**, if one is given. Use it only to calibrate. It may belong to a different variant of the task.
- **The drafts**, usually a folder on the teacher's computer (.docx, sometimes .odt). If the teacher points at a File Explorer window, confirm you have the exact folder they mean before you start. Folders with similar names are common, for example "...investigation" and "...investigation (1)". If you get it wrong, the teacher has to redirect you.

## Step 1: Ask three questions before marking

Ask all three in one AskUserQuestion call. Skip any the teacher has already answered in their prompt.

1. **Who are the comments from?** The author name must follow the format `Lastname, Firstname (School name)`, e.g. `Bowler, Sam (Banksia Park International HS)`. Initials for the comment are the first letter of the first name followed by the first letter of the last name, e.g. "SB". If the teacher gives a name in another shape, reformat it and confirm.
2. **What should the feedback focus on?** Just maths / just writing / writing and maths.
   - *Maths* means accuracy of calculations and algebra, correct and complete working, valid reasoning, correct notation, and whether conclusions or conjectures follow from the evidence.
   - *Writing* means clarity, structure, explanation and use of the required terminology.
   - The focus decides which errors get comments. Spelling and grammar are always highlighted, never commented on.
3. **What are the benchmarks for on track / needs improvement / not on track?** For example: "on track = parts A–C done and part D started; needs improvement = A–C done but D not started; not on track = A or B incomplete." Offer the previous benchmarks as an option if you know them.

Also ask, or respect if already stated, anything to ignore. For example: "don't comment on students not using the suggested values" or "only pick up rounding if it damages the result".

## Step 2: Read every draft properly

- **Stage the drafts into the container.** Maths content lives in equation objects that tools like LibreOffice often fail to render. The reliable way to read it is pandoc to markdown, with a Lua filter that flattens tables so each cell's content appears in order (the script below includes the filter). For .odt files, read the formula objects' MathML from `Object N/content.xml`.
- **Watch for images and ink.** Check `word/media` and any drawing shapes, because sign diagrams, handwritten working and chosen-shape diagrams often live there. Render the page or view the media when it matters to your judgement.
- **Check for duplicates.** Compare checksums across files so you don't mark the same draft twice. If a student has two versions, mark the latest and tell the teacher.
- **Recompute every number.** Check every numerical result with Python, never by eye. Each wrong value becomes a comment unless it's a trivial rounding slip that the teacher said to ignore.

Work in multi-column tables can read in an odd order. Use the rendered page, or the row and column structure, to confirm which working belongs to which part.

## Step 3: Decide the comments for each student

Apply these rules so the feedback is consistent across the class:

- **Length.** Each comment is at most 2–3 sentences: name the error, and only suggest a next step when the student wouldn't otherwise know what to do. Don't do the work for them.
- **Count.** No more than 10 comments per student. Go over only if the student has more than 10 critical errors, because no mathematical error may be missed. When cutting, drop clarity and notation comments before any error in the mathematics.
- **Priority.** Wrong results and faulty reasoning first (for example, calling a minimum a maximum, or a conjecture with the wrong condition). Then missing required steps, such as no test for a minimum or no ratio calculated. Then working that is unclear or false as written, such as chaining `A = ... = A' = ...` or giving a cube root a ±. Minor rounding comes last, and only if it damages the conclusion.
- **Missing sections.** Give one short comment per missing required section, e.g. "Part B hasn't been started yet."
- **Positive feedback.** One short positive comment at the end of each part that is well done or well worked (for example the specific cases, the general case, the conjecture). Keep it brief, e.g. "Excellent working out." Never more than one per part.
- **No inline maths.** If a comment needs an equation, put it on its own line as a real Word equation (OMML), not typed into the sentence. Word the prose so it doesn't need symbols, e.g. "the radius needs to be squared in this denominator:" followed by the equation.
- **Anchor comments on the exact paragraph** where the error is. If an error repeats across trials, comment on the first instance and say "this applies to all three trials".
- **Spelling and grammar.** Collect the misspellings and misused words (e.g. "conjected", "tringle", "eachother", "hailed" for "yielded"). These get yellow highlighting only.

## Step 4: Build the commented copies

Write a spec per student (paragraph index, then comment segments), then run the annotation script below. It:

- adds `comments.xml` and the relationship and content-type entries,
- anchors each comment on its paragraph,
- converts LaTeX to OMML with pandoc for equation lines, and puts the equation elements in schema order,
- splits runs to add yellow highlighting,
- leaves everything else byte-for-byte unchanged.

Find paragraph indices with `dump.py`. Run the docx skill's `validate.py --original` on every output, and check that the paragraph count is unchanged.

For .odt drafts, insert `office:annotation` (with `dc:creator` and `dc:date`) at the start of the paragraph and `office:annotation-end` at its end. Keep the file as .odt. Write the comments so they need no equations.

Save the copies under the original filenames in a `Feedback` subfolder beside the drafts, using `device_commit_files`. Never overwrite the students' originals.

## Step 5: Summary

Create `Progress check summary.docx` in the same Feedback folder: a table with Student / Judgement (colour-coded green, amber or red) / a one-line note. Apply the teacher's benchmarks literally. When a student falls between categories (e.g. has started the shape but is missing the general case), apply the rule and flag it as borderline in the note.

In your chat reply, show the judgement table, list the borderline calls, give the two or three most common class-wide issues, and mention any template problems or duplicate drafts. Keep it short. The detail belongs in the documents.

## Scripts

Write these into the working directory at the start of the task.

`flat.lua` (pandoc filter that flattens tables):

```lua
function Table(t)
  local out = {}
  local function addrows(rows)
    for _, r in ipairs(rows) do for _, c in ipairs(r.cells) do
      table.insert(out, pandoc.Para{pandoc.Str("--- [cell] ---")})
      for _, b in ipairs(c.contents) do table.insert(out, b) end
    end end
  end
  addrows(t.head.rows)
  for _, b in ipairs(t.bodies) do addrows(b.head); addrows(b.body) end
  return out
end
```

Usage: `pandoc -t markdown --wrap=none --lua-filter flat.lua draft.docx`

`dump.py` (paragraph indices for anchoring):

```python
import sys, zipfile
from lxml import etree
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'
M='http://schemas.openxmlformats.org/officeDocument/2006/math'
root=etree.fromstring(zipfile.ZipFile(sys.argv[1]).read('word/document.xml'))
for i,p in enumerate(root.iter('{%s}p'%W)):
    t=''.join(x.text or '' for x in p.iter('{%s}t'%W,'{%s}t'%M)).strip()
    if p.find('.//{%s}drawing'%W) is not None and not t: t='[DRAWING]'
    if t: print(i, t[:110])
```

`annot.py` (comments with equations, plus highlighting):

```python
import zipfile, subprocess, tempfile, copy, sys
from lxml import etree
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'
M='http://schemas.openxmlformats.org/officeDocument/2006/math'
R='http://schemas.openxmlformats.org/officeDocument/2006/relationships'
def w(t): return '{%s}%s'%(W,t)
AUTHOR=None; INIT=None; DATE='2026-01-01T09:00:00Z'  # set these per run

def latex_to_omml(latexes):
    if not latexes: return []
    d=tempfile.mkdtemp()
    open(d+'/e.md','w').write('\n\n'.join('$$%s$$'%l for l in latexes))
    subprocess.run(['pandoc',d+'/e.md','-o',d+'/e.docx'],check=True)
    x=etree.fromstring(zipfile.ZipFile(d+'/e.docx').read('word/document.xml'))
    order=['begChr','sepChr','endChr','grow','shp','ctrlPr']
    for dpr in x.iter('{%s}dPr'%M):
        kids=sorted(dpr, key=lambda c: order.index(etree.QName(c).localname) if etree.QName(c).localname in order else 99)
        for c in kids: dpr.remove(c)
        for c in kids: dpr.append(c)
    paras=x.findall('.//{%s}oMathPara'%M); assert len(paras)==len(latexes)
    return paras

def run(text,rpr=None):
    r=etree.Element(w('r'))
    if rpr is not None: r.append(copy.deepcopy(rpr))
    t=etree.SubElement(r,w('t')); t.text=text
    t.set('{http://www.w3.org/XML/1998/namespace}space','preserve'); return r

def highlight(root, word, occurrence=None, para_idx=None):
    paras=list(root.iter(w('p'))); targets=[paras[para_idx]] if para_idx is not None else paras
    count=done=0
    for p in targets:
        for t in list(p.iter(w('t'))):
            r=t.getparent()
            if r.tag!=w('r'): continue
            txt=t.text or ''; i=txt.find(word)
            while i>=0:
                count+=1
                if occurrence is None or count==occurrence:
                    rpr=r.find(w('rPr')); parts=[]
                    if txt[:i]: parts.append(run(txt[:i],rpr))
                    hr=run(word,rpr); hp=hr.find(w('rPr'))
                    if hp is None: hp=etree.Element(w('rPr')); hr.insert(0,hp)
                    for o in hp.findall(w('highlight')): hp.remove(o)
                    hl=etree.Element(w('highlight')); hl.set(w('val'),'yellow')
                    later=['u','effect','bdr','shd','fitText','vertAlign','rtl','cs','em','lang','eastAsianLayout','specVanish','oMath']
                    pos=next((k for k,c in enumerate(hp) if etree.QName(c).localname in later),len(hp)); hp.insert(pos,hl)
                    parts.append(hr)
                    if txt[i+len(word):]: parts.append(run(txt[i+len(word):],rpr))
                    par=r.getparent(); idx=par.index(r); par.remove(r)
                    for k,n in enumerate(parts): par.insert(idx+k,n)
                    done+=1; break
                i=txt.find(word,i+1)
    return done

def annotate(src, dst, comments, highlights):
    """comments: [(para_idx, [str | ('eq', latex), ...])]; highlights: [(word, occurrence|None, para_idx|None)]"""
    z=zipfile.ZipFile(src); files={n:z.read(n) for n in z.namelist()}
    root=etree.fromstring(files['word/document.xml']); paras=list(root.iter(w('p')))
    omml=iter(latex_to_omml([s[1] for _,segs in comments for s in segs if isinstance(s,tuple)]))
    croot=etree.Element(w('comments'),nsmap={'w':W,'m':M,'r':R})
    for cid,(pi,segs) in enumerate(comments):
        p=paras[pi]
        s=etree.Element(w('commentRangeStart')); s.set(w('id'),str(cid))
        p.insert(1 if p.find(w('pPr')) is not None else 0, s)
        e=etree.SubElement(p,w('commentRangeEnd')); e.set(w('id'),str(cid))
        r=etree.SubElement(p,w('r')); rs=etree.SubElement(etree.SubElement(r,w('rPr')),w('rStyle')); rs.set(w('val'),'CommentReference')
        etree.SubElement(r,w('commentReference')).set(w('id'),str(cid))
        c=etree.SubElement(croot,w('comment'))
        for k,v in (('id',str(cid)),('author',AUTHOR),('date',DATE),('initials',INIT)): c.set(w(k),v)
        for n,seg in enumerate(segs):
            cp=etree.SubElement(c,w('p')); etree.SubElement(etree.SubElement(cp,w('pPr')),w('pStyle')).set(w('val'),'CommentText')
            if n==0:
                ar=etree.SubElement(cp,w('r')); etree.SubElement(etree.SubElement(ar,w('rPr')),w('rStyle')).set(w('val'),'CommentReference')
                etree.SubElement(ar,w('annotationRef'))
            cp.append(next(omml) if isinstance(seg,tuple) else run(seg))
    for word,occ,pi in highlights:
        if not highlight(root,word,occ,pi): print('highlight not found (split run?):',word,file=sys.stderr)
    files['word/document.xml']=etree.tostring(root,xml_declaration=True,encoding='UTF-8',standalone=True)
    assert 'word/comments.xml' not in files, 'draft already has comments - merge instead'
    files['word/comments.xml']=etree.tostring(croot,xml_declaration=True,encoding='UTF-8',standalone=True)
    rels=files['word/_rels/document.xml.rels'].decode()
    files['word/_rels/document.xml.rels']=rels.replace('</Relationships>','<Relationship Id="rIdCmt1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/comments" Target="comments.xml"/></Relationships>').encode()
    ct=files['[Content_Types].xml'].decode()
    files['[Content_Types].xml']=ct.replace('</Types>','<Override PartName="/word/comments.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.comments+xml"/></Types>').encode()
    st=files['word/styles.xml'].decode(); add=''
    if 'w:styleId="CommentText"' not in st: add+='<w:style w:type="paragraph" w:styleId="CommentText"><w:name w:val="annotation text"/><w:basedOn w:val="Normal"/><w:rPr><w:sz w:val="20"/></w:rPr></w:style>'
    if 'w:styleId="CommentReference"' not in st: add+='<w:style w:type="character" w:styleId="CommentReference"><w:name w:val="annotation reference"/><w:rPr><w:sz w:val="16"/></w:rPr></w:style>'
    if add: files['word/styles.xml']=st.replace('</w:styles>',add+'</w:styles>').encode()
    with zipfile.ZipFile(dst,'w',zipfile.ZIP_DEFLATED) as o:
        for n in ['[Content_Types].xml']+[n for n in files if n!='[Content_Types].xml']: o.writestr(n,files[n])
```

Some caveats:

- **Split words.** Highlighting only works on a word that sits inside one text run. If a word is split across runs, merge the runs first with the docx skill's `merge_runs.py`, or skip the word and mention it.
- **Existing comments.** If a draft already has `comments.xml`, merge into it rather than overwriting it.
- **Headless preview.** LibreOffice's headless PDF export shows comments in the margin, which is handy for a spot check, but it won't draw equations. Tell the teacher to open one file in Word to confirm the equation comments look right.