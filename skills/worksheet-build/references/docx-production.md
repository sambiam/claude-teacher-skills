# DOCX production

How to build the worksheet and answer sheet so the mathematics is real Word
equation content and the layout survives printing. Use the `docx` skill for
general file mechanics; this file covers what that skill doesn't: equations,
working boxes, and checking that what you built is what you meant.

## Contents

- Page setup
- The working-space pattern
- Equations (OMML) — verified code
- Geometry diagrams
- Building the answer sheet from the same source
- Rendering and checking
- Editing an existing worksheet

## Page setup

- A4 portrait, roughly two pages. Cut questions before shrinking type.
- Margins around 1000–1440 DXA (0.7–1.0") so nothing is lost to the
  photocopier's edge.
- Body text 11–12 pt minimum; section headings clearly larger and bold.
- Section colour is optional and must survive greyscale printing — never carry
  meaning in colour alone.
- Whitespace between question groups so sections are visually distinct. No
  decorative borders or clip art.

`docx` (npm) is preinstalled — `require('docx')` directly. Tables need
`columnWidths` on the table *and* `width` on every cell, both in
`WidthType.DXA`; column widths must sum to the table width.

## The working-space pattern

Working space goes directly beneath the questions it belongs to: a row of
questions, then a row of blank boxes under it, then the next row of questions.
Never two rows of questions above one large shared space — a student must be
able to see which box is theirs at a glance.

Leave the boxes empty. Don't print the word "Working" inside them.

Set the box row height with `rule: "atLeast"` and size it to the work
required: a one-step simplification needs far less than a three-step
rearrangement. Spicy questions leave the grid entirely — full width, numbered
heading, equations on separate lines, generous space beneath.

Verified pattern (4 columns across a 9360 DXA text width):

```js
const {Table, TableRow, TableCell, WidthType, BorderStyle,
       Paragraph, TextRun, Math, MathRun, MathSuperScript} = require('docx');

const COL  = 2340;                                          // 4 × 2340 = 9360
const none = {style: BorderStyle.NONE,   size: 0, color: "FFFFFF"};
const box  = {style: BorderStyle.SINGLE, size: 4, color: "BFBFBF"};

const questionCell = (label, mathChildren) => new TableCell({
  width: {size: COL, type: WidthType.DXA},
  borders: {top: none, bottom: none, left: none, right: none},
  children: [new Paragraph({children: [
    new TextRun({text: label + ")  ", bold: true}),
    new Math({children: mathChildren}),               // label and equation
  ]})],                                               // share one paragraph
});

const workingCell = () => new TableCell({
  width: {size: COL, type: WidthType.DXA},
  borders: {top: box, bottom: box, left: box, right: box},
  children: [new Paragraph("")],
});

const row = new Table({
  columnWidths: [COL, COL, COL, COL],
  width: {size: 9360, type: WidthType.DXA},
  rows: [
    new TableRow({children: [/* four questionCell(...) */]}),
    new TableRow({height: {value: 1400, rule: "atLeast"},
                  children: [workingCell(), workingCell(),
                             workingCell(), workingCell()]}),
  ],
});
```

## Equations (OMML) — verified code

Use the `docx` library's `Math*` classes. They emit `<m:oMath>` — genuine Word
equation objects that Word opens and edits as equations. Never fake notation
with plain text (`x^3`, `3/5`, `*`).

```js
const {Math, MathRun, MathFraction, MathSuperScript, MathRadical} = require('docx');

const sup  = (base, power) => new MathSuperScript({
  children:   [new MathRun(base)],
  superScript:[new MathRun(power)],
});

// 3x² × 4x³
new Math({children: [
  new MathRun("3"), sup("x", "2"),
  new MathRun("×4"), sup("x", "3"),
]});

// (6x⁴)/(10x²)
new MathFraction({
  numerator:  [new MathRun("6"), sup("x", "4")],
  denominator:[new MathRun("10"), sup("x", "2")],
});

// x^(2/3) — a fraction inside the superscript
new MathSuperScript({
  children:   [new MathRun("x")],
  superScript:[new MathFraction({numerator:  [new MathRun("2")],
                                 denominator:[new MathRun("3")]})],
});
```

Multiplication is `×` (U+00D7) inside a `MathRun` — not `*`, not a centred
dot, not the letter x. Indices must be true superscripts, fractions true
fractions, and fractional indices must render as a fraction in the exponent.

A `Math` object can sit in a paragraph alongside `TextRun`s, so question
labels and equations share one line without a text-mode approximation.

## Geometry diagrams

`docx-js` has no vector-drawing API worth using for a labelled triangle.
Build the diagram as an image and embed it with `ImageRun` the same as any
other picture — don't try to construct shapes out of borders and tables.

Don't work out the vertices, mirrored second triangle, label positions, tick
marks or angle-bisector point by hand for each question — that coordinate
geometry is identical every time and is worked out once in
`scripts/triangle_geometry.py` (Python; run it as a separate step before the
`docx-js` build, then render its output to an image and pass the image path
into the build script):

```python
import sys; sys.path.insert(0, "scripts")
from triangle_geometry import triangle_sas, triangle_sss, label_anchors, tick_marks

tri = triangle_sas(p=7, theta_deg=52, q=9)      # two sides + included angle
anchors = label_anchors(tri, vertex_offset=0.3, side_offset=0.3)
ticks = tick_marks(tri, "AB", count=1)
# then render tri/anchors/ticks with matplotlib or Pillow at print
# resolution (≈300 dpi for the printed page) and save as PNG/SVG
```

`triangle_sas`/`triangle_sss` return vertices `'A'`/`'B'`/`'C'` plus a `sides`
dict on the standard convention (side `a` = BC opposite A, and so on), so the
diagram's labels line up with whatever the answer sheet's working calls each
side. `interior_angles()` and `side_lengths()` read the angles and lengths
back off the built triangle — use them as a QA check after rendering: the
longest labelled side should look longest and a given obtuse angle shouldn't
render as visibly acute, or there's a sign/offset error in the coordinates
that a text-only proof-read won't catch.

Match the same labelling convention `deck-build` and `ssdd-build` use, so a
diagram doesn't look different depending on which skill produced it:
variables and unknowns in italic (an italic serif/maths face — Cambria Math,
or italic Cambria/Times as a fallback — never bold upright sans-serif); no
filled circle or badge behind a value purely to show correspondence, since a
tick mark or a consistent accent colour already carries that meaning; and the
plugin's default 3-colour convention — `#262626` (near-black) for given
values and outlines, `#1F4E79` (navy) for correspondence marks, `#C00000`
(red) for the unknown. Colour still has to survive greyscale printing per
**Page setup** above, so also distinguish the unknown by the italic "x" label
itself, not by colour alone.

`line`-type bounding-box quirks from pptxgenjs/python-pptx don't apply
here — `matplotlib`/Pillow both draw an arbitrary line from two endpoints
directly — but there's still no small-arc primitive worth using for an angle
mark in either; use coloured, matched text instead.

## Building the answer sheet from the same source

Generate both documents from one script with a single question data
structure, and produce the answer sheet by swapping the empty working cell for
a cell containing the answer. That is what guarantees the two files stay
aligned — hand-copying question order between two scripts is where answers
drift onto the wrong questions.

Regenerate the answer sheet after any change to the worksheet, and always from
the final worksheet content.

## Rendering and checking

Two checks, and they catch different failures.

**1. Read the equations back.** `pandoc` converts OMML to LaTeX, which makes
every exponent, numerator, denominator, bracket, sign and multiplication
symbol readable at a glance:

```bash
pandoc -t markdown worksheet.docx
```

Compare that output against the questions you intended. Syntactically valid
XML proves nothing about whether the exponent landed on the right base.

**2. Render and look at the pages.**

```bash
python /mnt/skills/public/docx/scripts/office/soffice.py --headless --convert-to pdf worksheet.docx
pdftoppm -jpeg -r 100 worksheet.pdf page
ls page-*.jpg     # then read the images
```

**LibreOffice renders equations as blank space unless `libreoffice-math` is
installed.** The document is fine; the renderer isn't. If equations are
missing from the PDF, install it once and re-render — otherwise the layout
check is meaningless, because the space equations occupy won't be represented:

```bash
apt-get update && apt-get install -y libreoffice-math   # no sudo in this container
```

Inspect every page for: intended page count, equation rendering, line
wrapping, table dimensions, working-box height, sensible page breaks, headings
not orphaned at the foot of a page, a Spicy section that isn't cramped, and —
on the answer sheet — every answer sitting under its own question. Revise and
re-render until it's right. Never deliver an unrendered file.

For symbolic verification of the answers themselves, `sympy` is available:
expand, simplify, factor, solve, and check claimed equivalences with
`simplify(a - b) == 0`.

## Editing an existing worksheet

`docx-js` cannot open an existing file. To change a worksheet the teacher has
already edited, unzip it, edit `word/document.xml`, and rezip — see the `docx`
skill. Preserve their wording and ordering; regenerating from scratch throws
away deliberate changes.

If the existing worksheet was produced from a build script that still exists,
editing the script and rebuilding is cleaner — but only when nothing has been
changed in Word since, or those changes are lost.
