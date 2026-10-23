---
name: "exam-revision-homework"
description: "Build weekly revision homework sets leading up to an exam or test for any maths class — asks for the teaching schedule and which weeks, then makes printable, questions-only and ticked solutions versions in the school layout and logo."
---

# Weekly revision homework before an exam

Builds one homework set per chosen week for the run-up to an exam or topic test, for any class or course. Each set only uses content the class has already been taught by that week. Each week gets four files:

| File | What it is |
|---|---|
| `<PREFIX> Week N - printable.docx` | One double-sided A4 sheet: school logo title block, exam-style dashed square working grids, `[n marks]` right-aligned under each grid |
| `<PREFIX> Week N - questions only.docx` | The same questions on **one page**, with no grids — for uploading so students work in their books |
| `<PREFIX> Week N - SOLUTIONS.pdf` (+ `.docx`) | The printable sheet with each grid replaced by a box of red worked solutions and **one ✓ per mark**. It paginates identically to the printable sheet |

All three versions come from **one shared question structure** (`content.py`) and one generator (`homework_gen.py`, embedded below), so answers can never drift away from their questions.

Use this skill rather than `senior-homework-build` when the teacher wants a *series* of sheets building towards an assessment, or wants the printable / questions-only / solutions trio. The answer-sheet conventions (solutions inside the working spaces, method/answer ticks, tick count = marks, a human read before release) follow `test-build`.

## Step 1 — Intake: ask before building

A wrong schedule means every sheet tests the wrong content, and the whole set has to be rebuilt. So settle these first.

**Look before you ask.** If a class folder is linked, search it for the exam or test paper, the unit outline / BOWS / term planner, and the topic decks. Only ask for what you can't find. Then ask everything that's still missing **in one go**, using AskUserQuestion for the choice questions where it's available, or in plain text otherwise:

1. **The class and the assessment.** Year level and course (for example Year 11 Stage 1 Mathematical Methods, or Year 10 Maths). Which exam or test the homework prepares for, its date, the topics it covers, and its calculator / notes conditions. Ask them to upload or point to a past paper if one isn't in the folder; it sets the style.
2. **The teaching schedule.** Ask the teacher to **upload a schedule** (term planner, BOWS / unit outline, scope and sequence, a spreadsheet, or a photo of a planner) **or type it in** as one line per week: topics or textbook sections taught. Include topics finished earlier in the course that the assessment also covers.
3. **Which weeks need homework.** For example "Weeks 3–6 of Term 4". Also ask the due day; the default is the first lesson or Monday of the following week.
4. **The pacing rule.** Does a week's homework cover only content taught *before* that week (the default, because homework is set at the start of the week), or can it include that week's own content?
5. **Anything to change from the defaults:**
   - about 25–30 marks and 40 minutes per sheet
   - printable sheet ≤ 2 pages, questions-only sheet 1 page
   - an optional challenge question
   - calculator permitted

Then **echo back a content map** and get a yes before writing any questions:

| Homework | Due | New-topic content allowed (taught before this week) | Retrieval topics (finished) |
|---|---|---|---|
| Week 3 | Mon 2 Nov | 12A–12E surds, indices | Trig, calculus |
| … | | | |

If the schedule leaves a week blank, ask what it covers. Until you have an answer, use nothing specific to that week. If the teacher is not around to answer (an unattended run), take the most reasonable reading, put the content map at the top of the report, and flag every assumption. Never infer pacing from file dates: decks are often from a previous year.

## Step 2 — Read the assessment for style

Read the past paper and any practice tests (`pandoc file.docx -t plain`). Note:

- question types and command words
- typical mark sizes (1–6), and multi-part contextual questions
- calculator use
- how the topics are mixed

The homework should *feel* like that paper.

## Step 3 — Design each sheet

Fill each week from the content map. The proportions are a guide; adapt the section names to the course:

- **Section A — the topic in progress (about half).** Only the sections allowed for that week. Open with a question every student can start. Put short routine parts side by side (a, b, c).
- **Section B — Keep it fresh (about a quarter).** Retrieval from finished topics on the assessment. Rotate the skills across the weeks so each one comes back more than once.
- **Section C — Exam-style questions (about a quarter).** Two or three multi-part contextual questions with marks on every part, in the assessment's language.
- **Challenge (optional, unmarked).** It must still use allowed content.

The final week can be mixed exam practice across everything allowed by then.

Rules:

- **The pacing rule is absolute, including for challenges.** Watch for methods that sneak in. For example, before logs are taught, solve exponential models "using the graph or table on your calculator", never "algebraically".
- **No reused exam questions or contexts.** Make it similar in style, but with new numbers, contexts and structures.
- Marks match the working. Every part has a mark. Give rounding instructions wherever approximation is expected.
- Respect the calculator conditions. If there is no calculator, numbers must work out cleanly.
- **Page budget:** if a sheet overflows, cut a whole question rather than shrinking anything, and report what you cut.

## Step 4 — Verify every answer

Compute every answer independently with sympy (solve, expand, limits, derivatives, numeric values), and substitute back where possible. Check rounding. Re-read each question for whether it is well posed.

## Step 5 — Build

```bash
pip install --break-system-packages python-docx lxml sympy pillow
apt-get install -y libreoffice-math pandoc   # libreoffice-math or equations vanish when rendering
```

1. Write `homework_gen.py` and `content_template.py` from the blocks below. Save the logo block as `logo.b64` and decode it:
   `python3 -c "import base64;open('logo.png','wb').write(base64.b64decode(open('logo.b64').read()))"`
2. Write `content.py` in the shape of the template, with the content map in its header comment. Set:
   - `COURSE`, `TITLE`, `PREFIX`
   - optionally `CALC_NOTE` and `WEEK_LABEL`
   - one `WEEKS[n]` per chosen week, with `due`, `time`, `focus` and `blocks`
3. Run:
   `python3 homework_gen.py content.py out --logo logo.png --pdf`
   - It refuses to build if any block's ticks ≠ marks.
   - `--pdf` renders everything and reports page counts and printable/solutions page parity per week.
   - `--template some_school_paper.docx` optionally inherits styles from a school document.

### content.py essentials

- `$...$` becomes a real Word equation (LaTeX via pandoc → OMML); `\$` is a literal dollar sign.
- Each solution line is `T('text $math$', ticks)`. Put method ticks on the method line and answer ticks on the answer line.
- Working space is automatic: grids are sized to fit their solution, and `rows` is a minimum. Use `extra=n` for more room; the solutions box grows identically.

### Rendering traps (LibreOffice shows `¿`)

- A math fragment that starts or ends with `=`: write `= $2x^{7}$`, not `$=2x^{7}$`.
- A math fragment that is just an operator (`$+$`): use words.
- Units: write them as text with Unicode (`30 cm²`, `m/s²`), not `\mathrm{}`.
- `%` straight after an equation can float; put it in a following text phrase.

## Step 6 — Check by eye

Render the solutions PDF at about 80 dpi and look at **every page**:

- no clipped last line in any box (fix with `extra`, or merge two short solution lines into one)
- ticks render
- fractions and limits render
- nothing orphaned

Glance at the printable and questions-only pages too. The generator's parity check catches page drift, but not clipping.

## Step 7 — Save and report

Save to the class's topic or assessment folder, under `homework/<name of the run>/`. Include the four files per week, plus `generator/` (`content.py`, `homework_gen.py`, `logo.png`) so a question can be changed and everything regenerated. If a file is locked because it's open in Word, save it as `... (v2).docx` and say so.

Report:

- the content map actually used
- marks per week
- anything cut to fit the page budget
- every assumption made
- a plain statement that the sheets need a teacher's read before release

## Layout specification (fixed — the generator implements it)

- A4; margins 1.0 cm top/bottom and 1.5 cm left/right; Calibri 10.5 pt; equations in Cambria Math.
- **Title block:** borderless table. Left: the Banksia Park International High School logo, 3.85 cm wide. Right:
  - `COURSE — TITLE, Week N` in 12 pt bold
  - the focus line in 9.5 pt italic
  - `Name: ____` | `Due: …` | `Total: n marks` in 10.5 pt bold. On the solutions copy, the Name field reads **WORKED SOLUTIONS (teacher copy)** in red.
- Under the title block, an instruction line (9 pt italic) with a grey bottom rule: `CALC_NOTE`, show appropriate steps of logic, the marks tell you how much working is expected, and the suggested time.
- **Section headings:** 11 pt bold on E7E6E6 shading. The challenge heading uses F2F2F2 shading.
- **Questions:** bold number with a hanging indent. Sub-parts a), b) are indented. Side-by-side parts sit in borderless columns that line up with the solution columns.
- **Working grid:** 40 × 0.45 cm squares; dashSmallGap borders in A6A6A6; exact 12.75 pt rows; rows can't split and the grid stays with its question. `[n marks]` (9.5 pt) is right-aligned after the grid.
- **Solutions:** the same grid with the squares merged into one box per part (dotted dividers between parts). Red C00000 text at 9 pt, with ✓ ticks in Segoe UI Symbol, one per mark.
- **Questions-only:** no grids. Marks sit in a right-hand column or at the end of the line. Must fit one page.

## Embedded file: homework_gen.py

```python
#!/usr/bin/env python3
"""Generate weekly revision homework sheets (any course, any weeks) in the school layout.

Usage:
  python3 homework_gen.py content.py OUTDIR --logo logo.png [--template exam.docx] [--pdf]

One shared question structure (content.py) -> three outputs per week:
  print      : student sheet with dashed square working grids (exam style)
  questions  : questions only, for students to complete in their books
  solutions  : the print sheet with the grids replaced by same-height boxes
               holding the worked solutions and one tick per mark
"""
import copy, os, re, subprocess, sys, tempfile
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, Cm, RGBColor, Emu
from lxml import etree

import argparse, importlib.util, glob, zipfile

WEEKS = {}
CFG = {}          # COURSE, TITLE, PREFIX, CALC_NOTE, WEEK_LABEL from content.py
TEMPLATE = None   # optional: a prior exam .docx to inherit styles from
CREST = None      # school logo PNG
M = 'http://schemas.openxmlformats.org/officeDocument/2006/math'
W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'

FONT = 'Calibri'
BASE = 10.5          # question text size
SOL = 9            # solution text size
RED = 'C00000'
CELL_DXA = 255       # 0.45 cm squares, as on the 2024 exam
NCOLS = 40
USABLE = CELL_DXA * NCOLS
ROW_PT = 12.75
INDENT = Cm(0.65)

# ------------------------------------------------------------------ LaTeX -> OMML
_cache = {}

def build_math_cache():
    texs = []
    pat = re.compile(r'(?<!\\)\$(.+?)(?<!\\)\$')
    def collect(s):
        for m in pat.finditer(s or ''):
            texs.append(m.group(1))
    for wk in WEEKS.values():
        for b in wk['blocks']:
            if b[0] in ('q',):
                collect(b[2])
            elif b[0] == 'ch':
                collect(b[1])
            elif b[0] == 'w':
                d = b[1]
                collect(d.get('text'))
                for _, pt in d.get('parts') or []:
                    collect(pt)
                for col in d['sol']:
                    for s, _ in col:
                        collect(s)
    uniq = list(dict.fromkeys(texs))
    with tempfile.TemporaryDirectory() as td:
        md = os.path.join(td, 'm.md')
        with open(md, 'w') as f:
            f.write('\n\n'.join('$%s$' % t for t in uniq))
        out = os.path.join(td, 'm.docx')
        subprocess.run(['pandoc', md, '-o', out], check=True)
        import zipfile
        root = etree.fromstring(zipfile.ZipFile(out).read('word/document.xml'))
    paras = root.findall('.//{%s}body/{%s}p' % (W, W))
    assert len(paras) == len(uniq), (len(paras), len(uniq))
    for t, p in zip(uniq, paras):
        oms = p.findall('{%s}oMath' % M)
        assert len(oms) == 1, t
        _cache[t] = clean_omml(oms[0])


def _m(tag):
    return etree.Element('{%s}%s' % (M, tag))


def clean_omml(o):
    """Make pandoc's OMML render in LibreOffice as well as Word."""
    # plain delimiters: drop the empty separator / grow flags that LibreOffice mis-draws
    for dpr in o.iter('{%s}dPr' % M):
        for tag in ('sepChr', 'grow'):
            for e in dpr.findall('{%s}%s' % (M, tag)):
                dpr.remove(e)
    # \lim_{..} arrives as sSub(lim) followed by its argument: rebuild as Word does,
    # func( fName=limLow(lim, h->0), e=argument )
    for ss in list(o.iter('{%s}sSub' % M)):
        base = ''.join(ss.find('{%s}e' % M).itertext())
        if base != 'lim':
            continue
        parent = ss.getparent()
        arg = ss.getnext()
        func = _m('func'); fname = etree.SubElement(func, '{%s}fName' % M)
        ll = etree.SubElement(fname, '{%s}limLow' % M)
        e = etree.SubElement(ll, '{%s}e' % M)
        for k in ss.find('{%s}e' % M): e.append(k)
        lim = etree.SubElement(ll, '{%s}lim' % M)
        for k in ss.find('{%s}sub' % M): lim.append(k)
        fe = etree.SubElement(func, '{%s}e' % M)
        if arg is not None:
            fe.append(arg)
        parent.replace(ss, func)
    return o


def styled_math(tex, size, color=None):
    o = copy.deepcopy(_cache[tex])
    for r in o.iter('{%s}r' % M):
        rpr = etree.Element('{%s}rPr' % W)
        f = etree.SubElement(rpr, '{%s}rFonts' % W)
        f.set('{%s}ascii' % W, 'Cambria Math'); f.set('{%s}hAnsi' % W, 'Cambria Math')
        if color:
            etree.SubElement(rpr, '{%s}color' % W).set('{%s}val' % W, color)
        etree.SubElement(rpr, '{%s}sz' % W).set('{%s}val' % W, str(int(size * 2)))
        etree.SubElement(rpr, '{%s}szCs' % W).set('{%s}val' % W, str(int(size * 2)))
        mrpr = r.find('{%s}rPr' % M)
        if mrpr is not None:
            mrpr.addnext(rpr)
        else:
            r.insert(0, rpr)
    return o


def run(p, text, size=BASE, bold=False, italic=False, color=None, font=FONT):
    r = p.add_run(text)
    r.font.name = font
    r._element.rPr.rFonts.set(qn('w:hAnsi'), font)
    r.font.size = Pt(size)
    r.bold = bold
    r.italic = italic
    if color:
        r.font.color.rgb = RGBColor.from_string(color)
    return r


def rich(p, s, size=BASE, color=None, bold=False):
    parts = re.split(r'(?<!\\)\$(.+?)(?<!\\)\$', s)
    for i, seg in enumerate(parts):
        if i % 2:
            p._p.append(styled_math(seg, size, color))
        elif seg:
            run(p, seg.replace('\\$', '$'), size, color=color, bold=bold)


def ticks(p, n):
    if n:
        run(p, ' ' + '✓' * n, SOL + 1, bold=True, color=RED, font='Segoe UI Symbol')


def fmt(p, before=0, after=0, left=None, hanging=None, keep=True, align=None, line=None):
    pf = p.paragraph_format
    pf.space_before = Pt(before); pf.space_after = Pt(after)
    if left is not None: pf.left_indent = left
    if hanging is not None: pf.first_line_indent = -hanging
    pf.keep_with_next = keep
    if align: p.alignment = align
    if line: pf.line_spacing = line
    return p

# ------------------------------------------------------------------ table helpers

def tbl_props(tbl, widths, borders=None, indent=0):
    t = tbl._tbl
    tp = t.tblPr
    for tag in ('w:tblW', 'w:tblLayout', 'w:tblBorders', 'w:tblInd', 'w:tblCellMar', 'w:tblStyle'):
        for e in tp.findall(qn(tag)):
            tp.remove(e)
    w = OxmlElement('w:tblW'); w.set(qn('w:w'), str(sum(widths))); w.set(qn('w:type'), 'dxa'); tp.append(w)
    ind = OxmlElement('w:tblInd'); ind.set(qn('w:w'), str(indent)); ind.set(qn('w:type'), 'dxa'); tp.append(ind)
    b = OxmlElement('w:tblBorders')
    for side in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        e = OxmlElement('w:' + side)
        spec = (borders or {}).get(side)
        if spec:
            e.set(qn('w:val'), spec[0]); e.set(qn('w:sz'), str(spec[1])); e.set(qn('w:space'), '0'); e.set(qn('w:color'), spec[2])
        else:
            e.set(qn('w:val'), 'nil')
        b.append(e)
    tp.append(b)
    lay = OxmlElement('w:tblLayout'); lay.set(qn('w:type'), 'fixed'); tp.append(lay)
    mar = OxmlElement('w:tblCellMar')
    for side, v in (('left', 40), ('right', 40), ('top', 0), ('bottom', 0)):
        e = OxmlElement('w:' + side); e.set(qn('w:w'), str(v)); e.set(qn('w:type'), 'dxa'); mar.append(e)
    tp.append(mar)
    grid = t.tblGrid
    for gc, wd in zip(grid.findall(qn('w:gridCol')), widths):
        gc.set(qn('w:w'), str(wd))
    for row in tbl.rows:
        for c, wd in zip(row.cells, widths):
            tcpr = c._tc.get_or_add_tcPr()
            tw = tcpr.find(qn('w:tcW'))
            if tw is None:
                tw = OxmlElement('w:tcW'); tcpr.append(tw)
            tw.set(qn('w:w'), str(wd)); tw.set(qn('w:type'), 'dxa')


def row_height(row, pt, rule='exact'):
    trpr = row._tr.get_or_add_trPr()
    h = OxmlElement('w:trHeight'); h.set(qn('w:val'), str(int(round(pt * 20)))); h.set(qn('w:hRule'), rule)
    trpr.append(h)
    cs = OxmlElement('w:cantSplit'); trpr.append(cs)


def tiny(p):
    """Collapse an empty cell paragraph so it can't push an exact-height row."""
    fmt(p, 0, 0, keep=True)
    p.paragraph_format.line_spacing = Pt(1)
    run(p, '', 1)

GRID = ('dashSmallGap', 4, 'A6A6A6')


def working_grid(doc, rows):
    tbl = doc.add_table(rows=rows, cols=NCOLS)
    tbl_props(tbl, [CELL_DXA] * NCOLS, {k: GRID for k in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV')})
    for r in tbl.rows:
        row_height(r, ROW_PT)
        for c in r.cells:
            tiny(c.paragraphs[0])
    return tbl


def solution_box(doc, rows, cols):
    """Same 0.45 cm grid as the student sheet (so heights match exactly), with the
    squares merged into one box per part to hold the worked solution."""
    k = len(cols)
    tbl = doc.add_table(rows=rows, cols=NCOLS)
    b = {s: GRID for s in ('top', 'left', 'bottom', 'right')}
    b['insideV'] = ('dotted', 4, 'BFBFBF')
    tbl_props(tbl, [CELL_DXA] * NCOLS, b)
    for r in tbl.rows:
        row_height(r, ROW_PT)
        for c in r.cells:
            tiny(c.paragraphs[0])
    per = NCOLS // k
    for j, lines in enumerate(cols):
        c0 = j * per
        c1 = NCOLS - 1 if j == k - 1 else c0 + per - 1
        cell = tbl.cell(0, c0).merge(tbl.cell(rows - 1, c1))
        for p in list(cell.paragraphs)[1:]:
            p._p.getparent().remove(p._p)
        first = True
        for s, n in lines:
            p = cell.paragraphs[0] if first else cell.add_paragraph()
            if first:
                for r in list(p.runs):
                    r._r.getparent().remove(r._r)
                p.paragraph_format.line_spacing = None
            first = False
            fmt(p, 0.5, 0, keep=True)
            rich(p, s, SOL, RED)
            ticks(p, n)
    # keep the merged box on one page, exactly as the student grid is kept
    for pel in tbl._tbl.iter(qn('w:p')):
        pPr = pel.get_or_add_pPr()
        if pPr.find(qn('w:keepNext')) is None:
            pPr.insert(0, OxmlElement('w:keepNext'))
    return tbl


def parts_table(doc, parts, marks=None):
    k = len(parts)
    avail = USABLE - (950 if marks else 0)
    widths = [avail // k] * k
    widths[-1] += avail - sum(widths)
    if marks:
        widths.append(950)
    tbl = doc.add_table(rows=1, cols=len(widths))
    tbl_props(tbl, widths)
    for i, (c, (lab, txt)) in enumerate(zip(tbl.rows[0].cells, parts)):
        p = c.paragraphs[0]
        fmt(p, 1, 2, left=Cm(0.55), hanging=Cm(0.55), keep=True)
        run(p, lab + '\t')
        rich(p, txt)
        p.paragraph_format.tab_stops.add_tab_stop(Cm(0.55))
    if marks:
        p = tbl.rows[0].cells[-1].paragraphs[0]
        fmt(p, 1, 2, keep=True, align=WD_ALIGN_PARAGRAPH.RIGHT)
        run(p, '[%d mark%s]' % (marks, '' if marks == 1 else 's'), 9.5)
    row = tbl.rows[0]._tr.get_or_add_trPr()
    row.append(OxmlElement('w:cantSplit'))
    return tbl

# ------------------------------------------------------------------ document

def new_doc():
    doc = Document(TEMPLATE) if TEMPLATE else Document()
    body = doc.element.body
    for el in list(body):
        if el.tag != qn('w:sectPr'):
            body.remove(el)
    s = doc.sections[0]
    s.page_width = Cm(21.0); s.page_height = Cm(29.7)   # A4
    s.top_margin = Cm(1.0); s.bottom_margin = Cm(1.0)
    s.left_margin = Cm(1.5); s.right_margin = Cm(1.5)
    s.header_distance = Cm(0.4); s.footer_distance = Cm(0.4)
    # empty the header so nothing floats over the title block
    for hdr in (s.header, s.first_page_header):
        for p in hdr.paragraphs:
            for r in p.runs:
                r.text = ''
    return doc


def title_block(doc, wk, n, mode, total):
    tbl = doc.add_table(rows=1, cols=2)
    tbl_props(tbl, [2350, USABLE - 2350])
    c0, c1 = tbl.rows[0].cells
    p = c0.paragraphs[0]; fmt(p, 0, 0)
    p.add_run().add_picture(CREST, width=Cm(3.85))
    p = c1.paragraphs[0]; fmt(p, 2, 0)
    run(p, '%s — %s, %s %s' % (CFG['COURSE'], CFG['TITLE'], CFG['WEEK_LABEL'], n), 12, bold=True)
    p = c1.add_paragraph(); fmt(p, 1, 0)
    run(p, wk['focus'], 9.5, italic=True)
    p = c1.add_paragraph(); fmt(p, 3, 0)
    p.paragraph_format.tab_stops.add_tab_stop(Cm(6.4))
    p.paragraph_format.tab_stops.add_tab_stop(Cm(13.7), WD_TAB_ALIGNMENT.RIGHT)
    if mode == 'solutions':
        run(p, 'WORKED SOLUTIONS (teacher copy)', 10.5, bold=True, color=RED)
    else:
        run(p, 'Name: ________________', 10.5, bold=True)
    run(p, '\tDue: %s' % wk['due'], 10.5, bold=True)
    run(p, '\tTotal: %d marks' % total, 10.5, bold=True)
    p = doc.add_paragraph(); fmt(p, 4, 2, keep=False)
    p.paragraph_format.bottom_border = True
    if mode == 'questions':
        msg = ('Complete in your exercise book. %s Show appropriate steps of logic — '
               'the marks tell you how much working is expected. Suggested time: %s.' % (CFG['CALC_NOTE'], wk['time']))
    else:
        msg = ('%s Work in the spaces provided and show appropriate steps of logic — '
               'the marks tell you how much working is expected. Suggested time: %s.' % (CFG['CALC_NOTE'], wk['time']))
    run(p, msg, 9, italic=True)
    pPr = p._p.get_or_add_pPr()
    bdr = OxmlElement('w:pBdr'); bt = OxmlElement('w:bottom')
    for k, v in (('val', 'single'), ('sz', '6'), ('space', '1'), ('color', '808080')):
        bt.set(qn('w:' + k), v)
    bdr.append(bt); pPr.append(bdr)


def marks_line(doc, m):
    p = doc.add_paragraph(); fmt(p, 1, 3, keep=False, align=WD_ALIGN_PARAGRAPH.RIGHT)
    run(p, '[%d mark%s]' % (m, '' if m == 1 else 's'), 9.5)
    return p


def _line_h(s, k):
    h = 15.5
    if re.search(r'(?<![\^_]\{)(?<!\^\{-)\\frac|\\lim', s):
        h = 29.0
    elif '^{\\frac' in s or '^{-\\frac' in s:
        h = 19.0
    plain = re.sub(r'\\[a-z]+|[{}^_$]', '', s)
    if len(plain) > 100 / k:
        h *= 2
    return h


def need_rows(d):
    k = len(d['sol'])
    need = max(sum(_line_h(s, k) for s, _ in col) for col in d['sol']) + 4
    return max(d['rows'], int(-(-need // ROW_PT))) + d.get('extra', 0)


def build(n, mode, out):
    wk = WEEKS[n]
    total = sum(b[1]['marks'] for b in wk['blocks'] if b[0] == 'w' and b[1]['marks'])
    doc = new_doc()
    title_block(doc, wk, n, mode, total)
    last = None
    qnum = 0
    for b in wk['blocks']:
        kind = b[0]
        if kind == 'sec':
            p = doc.add_paragraph(); fmt(p, 4, 2)
            run(p, b[1], 11, bold=True)
            shd = OxmlElement('w:shd'); shd.set(qn('w:val'), 'clear'); shd.set(qn('w:color'), 'auto'); shd.set(qn('w:fill'), 'E7E6E6')
            p._p.get_or_add_pPr().append(shd)
        elif kind in ('q', 'ch'):
            if kind == 'ch':
                p = doc.add_paragraph(); fmt(p, 6, 1)
                run(p, 'Challenge (optional)  ', 11, bold=True)
                rich(p, b[1])
                shd = OxmlElement('w:shd'); shd.set(qn('w:val'), 'clear'); shd.set(qn('w:color'), 'auto'); shd.set(qn('w:fill'), 'F2F2F2')
                p._p.get_or_add_pPr().append(shd)
                last = p
                continue
            qnum += 1
            num, stem = qnum, b[2]
            p = doc.add_paragraph(); fmt(p, 3, 1, left=INDENT, hanging=INDENT)
            p.paragraph_format.tab_stops.add_tab_stop(INDENT)
            run(p, '%d.\t' % num, bold=True)
            rich(p, stem)
            last = p
        elif kind == 'w':
            d = b[1]
            if d.get('label'):
                p = doc.add_paragraph(); fmt(p, 2, 1, left=INDENT + Cm(0.6), hanging=Cm(0.6))
                p.paragraph_format.tab_stops.add_tab_stop(INDENT + Cm(0.6))
                run(p, d['label'] + '\t')
                rich(p, d['text'])
                last = p
            if d.get('parts'):
                if mode == 'questions' and d['marks']:
                    parts_table(doc, d['parts'], d['marks'])
                    continue
                t = parts_table(doc, d['parts'])
                last = t.rows[0].cells[-1].paragraphs[-1]
            if mode == 'print':
                working_grid(doc, need_rows(d))
            elif mode == 'solutions':
                solution_box(doc, need_rows(d), d['sol'])
            if d['marks']:
                if mode == 'questions':
                    # marks sit at the right-hand end of the question's last line
                    last.paragraph_format.tab_stops.add_tab_stop(Cm(18), WD_TAB_ALIGNMENT.RIGHT)
                    run(last, '\t[%d mark%s]' % (d['marks'], '' if d['marks'] == 1 else 's'), 9.5)
                else:
                    marks_line(doc, d['marks'])
            elif mode != 'questions':
                p = doc.add_paragraph(); fmt(p, 0, 0, keep=False)
                run(p, '', 4)
    doc.save(out)
    return total


def check_ticks():
    bad = []
    for n, wk in WEEKS.items():
        for b in wk['blocks']:
            if b[0] == 'w' and b[1]['marks']:
                t = sum(k for col in b[1]['sol'] for _, k in col)
                if t != b[1]['marks']:
                    bad.append((n, b[1].get('label'), t, b[1]['marks']))
    return bad


def pdf_report(outdir):
    """Render every docx, report page counts and printable/solutions page parity."""
    files = sorted(glob.glob(os.path.join(outdir, '*.docx')))
    subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', '--outdir', outdir] + files,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
    def pages(pdf):
        out = subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout
        return int(re.search(r'Pages:\s+(\d+)', out).group(1))
    def page_starts(pdf):
        txt = subprocess.run(['pdftotext', '-layout', pdf, '-'], capture_output=True, text=True).stdout
        return [next((l.strip() for l in pg.splitlines() if l.strip()), '') for pg in txt.split('\f')[:-1]]
    ok = True
    for n in WEEKS:
        base = os.path.join(outdir, '%s %s %s - ' % (CFG['PREFIX'], CFG['WEEK_LABEL'], n))
        pp, qq, ss = (base + s + '.pdf' for s in ('printable', 'questions only', 'SOLUTIONS'))
        np_, nq, ns = pages(pp), pages(qq), pages(ss)
        parity = page_starts(pp) == page_starts(ss)
        flag = '' if (np_ <= 2 and nq == 1 and np_ == ns and parity) else '   <-- CHECK'
        ok &= not flag
        print('%s %s: printable %d pp, questions %d pp, solutions %d pp, page parity %s%s'
              % (CFG['WEEK_LABEL'], n, np_, nq, ns, 'OK' if parity else 'MISMATCH', flag))
    return ok


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('content'); ap.add_argument('outdir')
    ap.add_argument('--logo', required=True)
    ap.add_argument('--template')
    ap.add_argument('--pdf', action='store_true', help='also render PDFs and check pages/parity')
    a = ap.parse_args()
    spec = importlib.util.spec_from_file_location('content', a.content)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    WEEKS.update(mod.WEEKS)
    missing = [k for k in ('COURSE', 'TITLE', 'PREFIX') if not hasattr(mod, k)]
    if missing:
        sys.exit('content.py must define %s' % ', '.join(missing))
    CFG.update(COURSE=mod.COURSE, TITLE=mod.TITLE, PREFIX=mod.PREFIX,
               CALC_NOTE=getattr(mod, 'CALC_NOTE', 'Calculator permitted.'),
               WEEK_LABEL=getattr(mod, 'WEEK_LABEL', 'Week'))
    TEMPLATE, CREST = a.template, a.logo
    bad = check_ticks()
    if bad:
        sys.exit('Tick count != marks: %r' % bad)
    build_math_cache()
    os.makedirs(a.outdir, exist_ok=True)
    for n in WEEKS:
        for mode, suffix in (('print', 'printable'), ('questions', 'questions only'), ('solutions', 'SOLUTIONS')):
            tot = build(n, mode, os.path.join(a.outdir, '%s %s %s - %s.docx' % (CFG['PREFIX'], CFG['WEEK_LABEL'], n, suffix)))
        print('%s %s: %d marks' % (CFG['WEEK_LABEL'], n, tot))
    if a.pdf:
        pdf_report(a.outdir)
```

## Embedded file: content_template.py (an example week; copy its shape, not its content)

```python
# content.py — EXAMPLE (a Year 11 Stage 1 Methods week). Copy the shape, not the content.
#
# Pacing for this run (fill in from the teacher's schedule):
#   Taught Weeks 1-2: 12A-12E  surds, index laws, rational indices
#   Taught Week 3   : 12F-12I  exponential equations, functions, growth
#   Taught Week 4   : 12J-12K
#   Homework Week 5 may use: everything taught before Week 5 (12A-12K) + finished topics (trig, calculus)
#
# Block types
#   ('sec', title)          section heading
#   ('q', n, stem)          numbered question stem (numbers are reassigned in order by the generator)
#   ('w', dict)             a working block:
#        label  : 'a)' etc. or None
#        text   : sub-question text or None
#        parts  : list of inline parts shown side by side (label, rich text) or None
#        rows   : minimum grid rows (the generator raises this to fit the solution)
#        extra  : extra rows of working space on top of that
#        marks  : int (None for challenge)
#        sol    : list of columns (one per part); each column is a list of T(rich text, ticks)
#   ('ch', stem)            challenge heading + stem (followed by one unmarked 'w' block)
#
# Rich text: $...$ is a Word equation (LaTeX); \$ is a literal dollar sign.

T = lambda s, n=0: (s, n)

COURSE = 'Stage 1 Mathematical Methods'          # title line, before the em dash
TITLE  = 'Exam Revision Homework'                 # title line, after the em dash
PREFIX = '11 Methods Exam Revision Homework'      # file names: '<PREFIX> Week N - printable.docx'
CALC_NOTE  = 'Calculator permitted.'              # or 'No calculator.' / 'Section A: no calculator.'
WEEK_LABEL = 'Week'                               # optional; e.g. 'Term 4 Week'

WEEKS = {}

# ---------------------------------------------------------------------------- WEEK 5  (12A-12I)
WEEKS[5] = dict(
    due='Monday 16 November',
    time='40 minutes',
    focus='Growth & decay 12A–12I (indices, exponential equations, models) + trig and calculus',
    blocks=[
        ('sec', 'Section A — Growth and decay: indices, exponential equations and models'),
        ('q', 1, r'Simplify $\frac{2^{n+2}-2^{n}}{3\times 2^{n}}$.'),
        ('w', dict(rows=3, marks=2,
                   sol=[[T(r'$\frac{2^{n}\left(2^{2}-1\right)}{3\times 2^{n}}$', 1), T(r'= $\frac{3}{3}=1$', 1)]])),
        ('q', 2, r'Solve for $x$ without a calculator:'),
        ('w', dict(parts=[('a)', r'$25^{x}=\frac{1}{125}$'), ('b)', r'$8^{x+1}=4^{2x}$')],
                   rows=3, marks=4,
                   sol=[[T(r'$5^{2x}=5^{-3}$', 1), T(r'$x=-\frac{3}{2}$', 1)],
                        [T(r'$2^{3x+3}=2^{4x}$', 1), T(r'$x=3$', 1)]])),
        ('q', 3, r'The graph of $y=a\times b^{x}$, where $b>0$, passes through the points $(0,\ 5)$ and $(2,\ 45)$. Find $a$ and $b$.'),
        ('w', dict(rows=3, marks=3,
                   sol=[[T(r'$(0,\ 5)$: $5=a\times b^{0}$, so $a=5$', 1),
                         T(r'$(2,\ 45)$: $45=5b^{2}$, so $b^{2}=9$', 1),
                         T(r'$b=3$ (since $b>0$)', 1)]])),
        ('q', 4, r'Solve $9^{x}-10\times 3^{x}+9=0$.'),
        ('w', dict(rows=3, marks=3,
                   sol=[[T(r'Let $u=3^{x}$: $u^{2}-10u+9=0$', 1),
                         T(r'$(u-1)(u-9)=0$, so $3^{x}=1$ or $3^{x}=9$', 1),
                         T(r'$x=0$ or $x=2$', 1)]])),

        ('sec', 'Section B — Keep it fresh: trigonometry and calculus'),
        ('q', 5, r'Solve $2\sin\theta=-\sqrt{2}$ for $0\le\theta\le 2\pi$, giving exact answers.'),
        ('w', dict(rows=4, marks=3,
                   sol=[[T(r'$\sin\theta=-\frac{\sqrt{2}}{2}$, reference angle $\frac{\pi}{4}$', 1),
                         T(r'Sine is negative in quadrants 3 and 4', 1),
                         T(r'$\theta=\frac{5\pi}{4}$, $\frac{7\pi}{4}$', 1)]])),
        ('q', 6, r'Find the coordinates of the stationary points of $y=x^{3}-3x^{2}-9x+2$ and determine their nature.'),
        ('w', dict(rows=6, marks=4,
                   sol=[[T(r'$\frac{dy}{dx}=3x^{2}-6x-9=3(x-3)(x+1)$', 1),
                         T(r'Stationary when $x=-1$ or $x=3$: points $(-1,\ 7)$ and $(3,\ -25)$', 1),
                         T(r'Sign diagram of $\frac{dy}{dx}$: positive, negative, positive'),
                         T(r'$(-1,\ 7)$ is a local maximum;  $(3,\ -25)$ is a local minimum', 2)]])),

        ('sec', 'Section C — Exam-style questions'),
        ('q', 7, r'The mass, $M$ grams, of a radioactive substance after $t$ years is given by $M(t)=80\times(0.95)^{t}$.'),
        ('w', dict(label='a)', text='Find the initial mass.', extra=1, rows=2, marks=1,
                   sol=[[T(r'$M(0)=80$ g', 1)]])),
        ('w', dict(label='b)', text='Find the mass after 20 years, correct to 2 decimal places.', extra=1, rows=2, marks=1,
                   sol=[[T(r'$M(20)=80\times 0.95^{20}\approx 28.68$ g', 1)]])),
        ('w', dict(label='c)', text='Use the graph or table on your calculator to find the half-life of the substance, correct to 1 decimal place.', extra=1, rows=3, marks=2,
                   sol=[[T(r'Solve $80\times 0.95^{t}=40$ (intersect $y=80\times 0.95^{x}$ with $y=40$)', 1),
                         T(r'$t\approx 13.5$ years', 1)]])),
        ('w', dict(label='d)', text='Show that after 30 years less than a quarter of the original mass remains.', extra=1, rows=3, marks=2,
                   sol=[[T(r'$M(30)=80\times 0.95^{30}\approx 17.17$ g', 1),
                         T(r'A quarter of 80 g is 20 g, and $17.17<20$', 1)]])),
        ('q', 8, r'For $y=3\sin(2x)+1$, state:'),
        ('w', dict(parts=[('a)', 'the amplitude'), ('b)', 'the period'), ('c)', 'the maximum and minimum values')],
                   extra=2, rows=2, marks=3,
                   sol=[[T(r'$3$', 1)],
                        [T(r'$\frac{2\pi}{2}=\pi$', 1)],
                        [T(r'max $4$, min $-2$', 1)]])),
        ('ch', r'An investment doubles in value after 9 years of compound growth at $r$% per year. Find $r$, correct to 1 decimal place.'),
        ('w', dict(extra=2, rows=3, marks=None,
                   sol=[[T(r'$P\left(1+\frac{r}{100}\right)^{9}=2P$, so $1+\frac{r}{100}=2^{\frac{1}{9}}$'),
                         T(r'$r=100\left(2^{\frac{1}{9}}-1\right)$'), T(r'$r\approx 8.0$, so the growth rate is 8.0% per year')]])),
    ])

```

## Embedded file: logo.b64 (Banksia Park International High School logo, PNG, 338×141)

```
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
```