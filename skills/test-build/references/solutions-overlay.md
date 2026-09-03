# Producing the worked solutions

The goal: a PDF where the solutions sit inside the working spaces of the
actual assessment pages, with ticks marking where each mark is earned.

## Primary method — raster overlay

```
student.docx → PDF → flatten pages → place working + ticks → solutions.pdf
```

1. Export the finished student document to PDF.
2. Rasterise the pages so the layout is fixed and cannot reflow.
3. Render the working — LaTeX or equation-editor quality, not plain text — and
   place it at measured coordinates inside each working space.
4. Place tick glyphs beside each marking point.
5. Record every tick in the manifest as you place it (see below).
6. Export as PDF.
7. Visually inspect **every page** before finalising.

### What this method demands in return

Placement is by coordinate, not by layout engine, so nothing enforces that the
working actually landed where it should. Misalignment is per-page and silent —
it looks correct on the pages you checked and wrong on the ones you didn't.
Three rules follow from that, and they are not optional:

- **Check every page, not a sample.** A spot check on a 12-page paper is a
  75% chance of shipping a broken page.
- **Rebuild from scratch after any change** to the student document. Every
  coordinate is measured against a specific rendering; edit a question on page 3
  and the coordinates on pages 3 onward are all stale. Never patch an overlay.
- **Build only from the final student document.** If the paper isn't finished,
  the overlay isn't ready to start.

### Tick manifest

Ticks drawn onto raster pages are graphics. Nothing downstream can count them,
so `check_marks.py` cannot verify them the way it verifies mark totals. Record
them as you place them, in `solutions_ticks.json` next to the output:

```json
{
  "1a": 2,
  "1b": 3,
  "2": 1,
  "3a": 4
}
```

Keys are question labels as they appear on the paper; values are the number of
ticks placed. Step 6 checks the total against the paper's mark allocations.
Write this while placing ticks, not from memory afterwards — a manifest
reconstructed at the end just records what you believed, which is the thing the
check exists to test.

## Alternative — derived document

If a raster overlay can't be produced with the tools available, or the run needs
to be reliable without a page-by-page human check, build the solutions from a
**copy of the finished student document**, typing the working into the same
grids, then export that to PDF.

```
student.docx → copy → fill grids with solutions → PDF
```

The trade-off runs the other way: the solutions land in the working spaces
because the same layout engine placed them, so nothing drifts when the paper is
regenerated, and the resulting PDF keeps selectable text and prints crisply. The
cost is that it needs the student document's working grids to have **fixed row
heights** set with an exact height rule — otherwise typing solutions into a grid
grows the row and the two documents paginate differently.

If using this method, keep the question text untouched in the copy, and verify
with `check_marks.py --solutions solutions.docx`, which counts the ticks
directly and needs no manifest.

## Content requirements

Both methods:

1. Solutions sit inside the correct working space, table, diagram, graph, or
   answer area, and never obscure the question text.
2. Clean mathematical typesetting, matching the quality of the student paper.
3. Step-by-step working for anything multi-step — a bare final answer can't be
   used to mark partial credit.
4. Final answers clearly identified.
5. Units and contextual interpretation where the question asks for them.
6. Model responses for interpretation questions, showing what a full-mark
   answer contains.
7. **Tick marks at each marking point**, using a real tick glyph (✓ or ✔), not
   a triangle, bullet, or placeholder.
8. **The number of ticks per question must equal its mark allocation exactly.**
9. If ticks can't be placed neatly beside every marking point, adjust the
   layout rather than dropping ticks — the mark allocation has to stay legible.

## Where the marks are

A tick says a mark was earned; it doesn't say what earned it. Where a question
carries more than one mark, place the ticks so the split is legible to whoever
marks the paper:

- A **method mark** sits against the line where the correct approach appears —
  the substitution, the rearrangement, the rule chosen. It's earned even if the
  arithmetic that follows is wrong.
- An **answer mark** sits against the final answer, including its units and any
  required rounding.

The practical test: a colleague marking a student who set the problem up
correctly and then slipped in the arithmetic should be able to see from the
solutions which marks that student still gets. If the ticks don't answer that,
the split isn't clear enough yet.

## Verification

```bash
python scripts/check_marks.py student.docx --tick-manifest solutions_ticks.json
```

Then render both documents to images and compare page by page:

- Page count matches between the two documents
- Each page's questions appear in the same position in both
- Solutions sit inside their working spaces, not spilling past them
- Ticks render as ticks, not as boxes, triangles, or missing glyphs
- Equations render fully — no broken fractions or dropped radicals
- Question text is still readable everywhere
- No page is shifted, stretched, or rotated relative to the student paper

## Be transparent about limitations

If a true aligned solutions PDF can't be produced with the tools available, say
so plainly and hand over the closest alternative — a separate solutions document
with correct mathematical formatting and clear question references. Do not
quietly produce a separate sheet and present it as an overlay. The teacher needs
to know which they're getting, because it changes how they mark.
