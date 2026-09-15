---
name: "diagram-labels"
description: "Generate a diagram as a static geometry image with movable, editable text-box labels overlaid on top, for insertion into a DOCX or PPTX file. Use this whenever another skill's workflow needs to add a diagram, figure, or illustrated shape carrying dimension labels, values, names, or callouts — worksheet-build, deck-build, ssdd-build, test-build, lesson-rationale, or any other skill about to insert a labelled diagram into a Word or PowerPoint output. Trigger on 'a diagram', 'a labelled shape', 'dimension labels', 'add a figure', or a diagram-drawing step inside another skill's plan, even if 'editable labels' isn't said explicitly — a diagram whose labels are baked into the picture as pixels is the thing this skill exists to avoid. Not for diagrams that stay purely decorative with no labels a teacher would ever want to move or correct."
---

# Diagrams with movable, editable labels

A diagram built the ordinary way — one raster image, labels baked into the
pixels — can't be fixed after the fact. A label that overlaps a line, a
value that needs correcting for a different class, a relabelling for
differentiation: all of it means regenerating the whole image. This skill
keeps the diagram itself a static picture (that part genuinely doesn't need
to change) but makes every label a real, separate, movable, editable text
box in the final document, positioned precisely over the picture.

**This is a supporting skill.** It doesn't produce a finished worksheet or
slide deck by itself — whatever skill is building that document (worksheet
figures out the question, the values, which shape) hands off to this skill
at the point where a diagram needs to go on the page, and gets back a PNG
plus the code pattern to place it with editable labels.

## The approach

1. **Draw the geometry only — no text.** Use `scripts/diagram_scene.py`
   (`Scene`, `extrude`, `draw_cylinder`, `bbox_for_prism`, and friends) to
   render the shape as a plain PNG. Every dimension line, arrow, or tick
   mark that's part of the picture goes in the image; every piece of text
   that names a value does not.
2. **Record where each label belongs, as a manifest.** Call
   `sc.add_label(text, point, direction)` for every label before saving —
   this doesn't draw anything, it records the label's position as a
   *fraction* (0–1) of the image's own width/height. `sc.save(path)` writes
   the PNG and a same-named `.json` manifest:

   ```json
   {
     "image": "diagrams/triangular_prism.png",
     "px_width": 900, "px_height": 814,
     "labels": [
       {"text": "6 cm", "fx": 0.3412, "fy": 0.9272, "align": "center"},
       {"text": "Area = 18 cm\u00b2", "fx": 0.3061, "fy": 0.7217, "align": "left"}
     ]
   }
   ```

   Fractional coordinates are the reason this works cleanly: the overlay
   step places the image at whatever size and position the target document
   needs, then computes each label's absolute position as
   `image_position + fraction × image_size` — no dependency on the image's
   pixel resolution, no re-deriving positions if the display size changes
   later. `align` (`left` / `right` / `center`) says which edge of the
   label should sit at that exact point, so text reads outward from the
   shape rather than centering awkwardly over it.
3. **Check it before it ever touches a document.** Run
   `scripts/label_debug_overlay.py diagrams/yourfile.png` and look at the
   result — every label should sit in clear space, not on top of a line or
   another label. Read `references/label-placement.md` for the specific
   collision patterns seen doing this (an outward push heading straight into
   the extruded back face, an edge whose slope happens to match the
   extrusion angle, two labels landing close on a small shape) and how each
   was fixed. Iterating here is one Python call; iterating inside a built
   docx or pptx is a full render-and-inspect cycle.
4. **Overlay the real labels in the target format.** Read
   `references/docx-overlay.md` for Word or `references/pptx-overlay.md`
   for PowerPoint — each has the exact, verified code pattern for turning
   the manifest into a floating image plus one real editable text box per
   label. Read the one you need; you don't need both.
5. **Validate and render-and-inspect before delivering**, exactly as the
   `docx` and `pptx` skills already require for any generated file — run
   the schema validator, convert to PDF, and look at the actual pages. A
   diagram that looks right in one renderer is not proof it's correct OOXML;
   see the validator note in `references/docx-overlay.md`, which caught a
   real defect that a visual check alone missed.

## Scope: which labels should be editable

Usually not *everything* drawn on the diagram — tick marks, arrowheads,
right-angle marks, and similar diagram furniture stay baked into the image.
Make editable text boxes out of the labels a teacher would plausibly want to
move or correct: dimensions, values, variable names, and callouts. That's
the distinction `add_label` is for — call it for those, and let the rest
stay as plain geometry drawn with `Scene.line` / `Scene.polygon`.

## What "movable and editable" actually buys

Once built this way, in the final document each label is a normal text box:
click it, drag it, double-click to retype the text — the same as if a
teacher had drawn it themselves with Word's or PowerPoint's own text box
tool. Nothing about the diagram picture needs to change for any of that.

## Reference files

- `references/docx-overlay.md` — the DOCX code pattern (modern DrawingML
  text boxes via `WpsShapeRun`), plus the gotchas that cost real debugging
  time: why not paragraph frames or VML, floating content not reserving
  flow height, a `docx`-library border-ordering bug, and unit conventions.
- `references/pptx-overlay.md` — the PPTX code pattern (`pptxgenjs`
  `addText` with `isTextBox: true`), considerably simpler since there's no
  legacy-format trap on this side.
- `references/label-placement.md` — collision patterns and fixes for
  positioning labels well on a new diagram.
- `scripts/diagram_scene.py` — the drawing library: `Scene`, `extrude`
  (prisms from any 2D cross-section, convex or concave), `draw_cylinder`,
  `bbox_for_prism`, `polygon_centroid`, `outward_normal_for_edge`.
- `scripts/label_debug_overlay.py` — the QA tool from step 3 above.
