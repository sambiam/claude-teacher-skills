# Overlaying editable labels in DOCX

Use the `docx` (npm) library already used by the `docx` skill. Everything
here was verified against LibreOffice's renderer and the official OOXML
schema validator (`/mnt/skills/public/docx/scripts/office/validate.py`) —
run that validator on anything you build this way before calling it done,
not just a visual render. A visual check in one renderer does not prove
another viewer (real Word, Word Online, Google Docs, mobile Office) will
render it the same way, and this exact mechanism has already burned that
lesson once — see "Why not frames or VML" below.

## The two floating pieces

1. **The diagram image** — a floating `ImageRun`, anchored to the page,
   placed `behindDocument: true` so it never covers nearby text if your
   reserved gap is slightly off.
2. **One shape per label** — a floating `WpsShapeRun` (a modern DrawingML
   text box, the same kind Word's own Insert → Text Box produces), anchored
   to the page, left in front of text (the default) so it's always visible
   on top of the diagram.

Both use the *same* `floating` option shape, so position math is
consistent between them:

```js
const {
  Document, Packer, Paragraph, ImageRun, TextRun, WpsShapeRun,
  AlignmentType, HorizontalPositionRelativeFrom, VerticalPositionRelativeFrom,
} = require('docx');

const DXA_PER_IN = 1440, EMU_PER_IN = 914400;
const dxa = (inches) => Math.round(inches * DXA_PER_IN);
const emu = (inches) => Math.round(inches * EMU_PER_IN);

// --- the image ---
function diagramImagePara(pngBuffer, leftIn, topIn, wIn, hIn) {
  return new Paragraph({
    spacing: { line: 40, lineRule: 'exact', before: 0, after: 0 },  // negligible flow height
    children: [ new ImageRun({
      type: 'png',
      data: pngBuffer,
      transformation: { width: wIn * 96, height: hIn * 96 },   // 96 = px-per-inch docx.js expects here
      floating: {
        horizontalPosition: { relative: HorizontalPositionRelativeFrom.PAGE, offset: emu(leftIn) },
        verticalPosition:   { relative: VerticalPositionRelativeFrom.PAGE,   offset: emu(topIn) },
        wrap: { type: 'none' },
        zIndex: 1,
        behindDocument: true,   // <-- keeps it from covering text if the gap below is imprecise
        allowOverlap: true,
      },
    })],
  });
}

// --- one label ---
function labelPara(text, leftIn, topIn, wIn, hIn, align) {
  return new Paragraph({
    children: [ new WpsShapeRun({
      type: 'wps',
      transformation: { width: Math.round(wIn * 96), height: Math.round(hIn * 96) },
      outline: { type: 'noFill' },        // borderless -- reads as a label, not a boxed shape
      floating: {
        horizontalPosition: { relative: HorizontalPositionRelativeFrom.PAGE, offset: emu(leftIn) },
        verticalPosition:   { relative: VerticalPositionRelativeFrom.PAGE,   offset: emu(topIn) },
        wrap: { type: 'none' },
        zIndex: 10,
        allowOverlap: true,
        // no behindDocument -- labels stay in front of both the image AND body text
      },
      children: [ new Paragraph({
        alignment: align,   // AlignmentType.LEFT / RIGHT / CENTER -- see positioning below
        children: [ new TextRun({ text, bold: true, size: 19 }) ],
      })],
    })],
  });
}
```

## Turning a label manifest into positions

Given a diagram placed at `(imgLeftIn, imgTopIn)` displayed at
`(dispWIn, dispHIn)`, and a label `{text, fx, fy, align}` from the
manifest (see `../SKILL.md` for the schema):

```js
function placeLabel(lab, imgLeftIn, imgTopIn, dispWIn, dispHIn) {
  const pointX = imgLeftIn + lab.fx * dispWIn;
  const pointY = imgTopIn  + lab.fy * dispHIn;
  const wIn = Math.min(2.6, Math.max(0.95, lab.text.length * 0.086 + 0.25));  // rough width-from-length estimate
  const hIn = 0.30;
  let leftIn, align;
  if (lab.align === 'left')       { leftIn = pointX;          align = AlignmentType.LEFT;   }
  else if (lab.align === 'right') { leftIn = pointX - wIn;     align = AlignmentType.RIGHT;  }
  else                             { leftIn = pointX - wIn / 2; align = AlignmentType.CENTER; }
  const topIn = pointY - hIn / 2;
  return labelPara(lab.text, leftIn, topIn, wIn, hIn, align);
}
```

## Why not paragraph frames (`w:framePr`) or legacy VML text boxes

Both were tried first and both have real problems:

- **`w:framePr`** (the old Word 95-era "paragraph frame") positions
  reliably in LibreOffice, but the labels came out **missing entirely**
  in another real-world viewer — this is what sent this project back to
  the drawing board once already. Assume it is not safe outside Word's own
  desktop renderer.
- **Legacy VML text boxes** (`docx`'s built-in `Textbox` class) never
  rendered their absolute position correctly in LibreOffice at all in
  testing here, regardless of table nesting.

`WpsShapeRun` is the only one of the three that is genuinely modern
DrawingML — the same family the image anchoring already uses, and the
actual format Word itself writes for a real text box. Use it.

## Gotchas, all found the hard way

- **Never anchor page-positioned floating content inside a table cell.**
  Absolute `page`-relative positioning (this applied to `w:framePr`
  specifically, but treat it as a general rule) silently breaks when the
  anchor paragraph is inside a table. Keep the image and label paragraphs
  as plain body paragraphs.
- **Floating content does not reserve flow height.** A floating image or
  label paragraph is invisible to normal document flow — whatever comes
  next in your document will render as if the diagram weren't there unless
  you explicitly reserve the vertical gap yourself (see below). This is
  also why `behindDocument: true` on the image is worth keeping even once
  your gap math is right: it's a free safety net for the case where it's
  slightly off.
- **Reserve that gap with plain paragraphs, not one custom-spaced one.**
  A paragraph carrying `spacing.before` (or a large `lineRule: exact`)
  immediately after the label shapes rendered with a visible
  double-struck/ghosted glitch in testing — a LibreOffice quirk, cause
  unconfirmed. The fix that worked cleanly: skip the gap with a handful of
  genuinely plain `new Paragraph({ text: '' })` lines (estimate how many
  from the reserved height ÷ a normal single-line height, then add a
  couple extra for safety) rather than one paragraph with custom spacing.
  Nothing after the diagram on the same page needs pixel-exact positioning
  anyway, so the approximation costs nothing.
- **`border` on a `Paragraph` can emit invalid OOXML.** `docx`'s paragraph
  border (`w:pBdr`) serializes its four sides in a fixed `top, bottom,
  left, right` order regardless of the order you pass them in the options
  object — the true schema order is `top, left, bottom, right`, so this
  fails validation. If you need a bordered empty box (e.g. a working-space
  area), put it in a one-cell table instead and border the *cell*
  (`w:tcBorders`) — that path serializes correctly.
- **Run the schema validator.** `python
  /mnt/skills/public/docx/scripts/office/validate.py yourfile.docx` — it
  catches exactly the class of defect above, which a visual render will
  never show you.
- **Units**: `ImageRun.transformation` width/height are in *pixels at
  96dpi* (so `inches * 96`, regardless of the PNG's actual pixel
  resolution — render the PNG at whatever DPI looks crisp, display size is
  independent). Floating `offset` values are in EMU (`inches * 914400`).
  `WpsShapeRun.transformation` uses the same pixels-at-96dpi convention as
  `ImageRun`.
