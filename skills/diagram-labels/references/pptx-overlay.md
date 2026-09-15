# Overlaying editable labels in PPTX

This is the easier of the two formats — `pptxgenjs`'s text box support
(`addText` with `isTextBox: true`) is native, modern, and reliable for this
directly; there is no legacy-format trap here the way there was in DOCX (see
`docx-overlay.md` for that story). Verified end to end with LibreOffice's
renderer and the pptx schema validator.

## Pattern

Given a diagram manifest (see `../SKILL.md` for the schema) and a chosen
on-slide position/size for the image:

```js
const pptxgen = require('pptxgenjs');
const pres = new pptxgen();
pres.layout = 'LAYOUT_WIDE';   // set BEFORE adding slides -- see pptx skill's gotchas
const slide = pres.addSlide();

const imgLeftIn = 3.0, imgTopIn = 1.0, imgWIn = 6.0;
const imgHIn = imgWIn * (manifest.px_height / manifest.px_width);   // preserve the PNG's aspect ratio

// image first, so it sits behind anything added after it
slide.addImage({ path: diagramPngPath, x: imgLeftIn, y: imgTopIn, w: imgWIn, h: imgHIn });

manifest.labels.forEach((lab) => {
  const px = imgLeftIn + lab.fx * imgWIn;
  const py = imgTopIn  + lab.fy * imgHIn;
  const boxW = Math.min(2.2, Math.max(0.8, lab.text.length * 0.075 + 0.2));  // rough width-from-length estimate
  const boxH = 0.3;
  let x = px - boxW / 2, align = 'center';
  if (lab.align === 'left')       { x = px;          align = 'left';  }
  else if (lab.align === 'right') { x = px - boxW;    align = 'right'; }

  slide.addText(lab.text, {
    x, y: py - boxH / 2, w: boxW, h: boxH,
    isTextBox: true,       // required -- without it the shape isn't announced as a text box
    fontSize: 11, bold: true, align,
    fill: { color: 'FFFFFF', transparency: 100 },   // fully transparent -- reads as a label, not a card
    line: { type: 'none' },
    margin: 0,             // kills the built-in text-box padding, so it aligns with `align` exactly
  });
});
```

## Notes

- **Z-order is just add order.** Add the image first and every label after
  it, and labels naturally sit on top — no explicit z-index property needed
  the way DOCX requires one.
- **`isTextBox: true` matters even though it looks cosmetic.** Without it,
  the shape doesn't carry the `txBox="1"` marker, so it may not read to a
  screen reader (or to a teacher's expectations of what's draggable/editable)
  as an actual text box.
- **`margin: 0`** is worth keeping deliberately — pptxgenjs text boxes have
  non-trivial built-in internal padding by default, which throws off the
  `align`-based positioning above (a `left`-aligned box's text won't
  actually start at `x` otherwise).
- Validate with `python /mnt/skills/public/pptx/scripts/office/validate.py
  yourfile.pptx` before considering it done, same as the DOCX path.
