---
name: "ssdd-build"
description: "Build SSDD sets — Same Surface, Different Deep structure — four questions sharing one diagram, context or set of numbers that each need completely different mathematics. Use for interleaving and for the specific failure where students pick a method from surface features without reading: 'they just see a right angle and reach for Pythagoras', 'make an SSDD for', 'I need a starter that mixes topics', 'something to interleave', 'they can do it in the exercise but not in the test', 'four questions on the same diagram', or when revising several topics at once. Best after the individual methods are secure; works as a starter, plenary or revision task. Produces one four-question slide or handout with full solutions."
---

# Building SSDD sets

Four questions arranged around a shared surface — the same diagram, the same
context, the same numbers — that each require completely different mathematics.

```
        3/5 of the class are girls.        3/5 of a number is 60.
        Write the ratio of boys to girls.  What is the number?
                              3
                              ─
                              5
        3/5 said blue is their             A square has side 3/5 cm.
        favourite. What angle on           What is the perimeter?
        a pie chart?
```

Craig Barton's format. Reference: `Practice questions/SSDD-Examples.pdf` and
`standards/practice-types.md`.

## What it's actually for

Students select methods from surface features. They see a triangle with a right
angle and reach for Pythagoras without reading which quantity is missing; they
see two fractions and reach for a common denominator regardless of the
operation. In an exercise this is invisible, because every question in the
exercise needs the same method and guessing from the surface *works*. In a test
it stops working, which is why "they can do it in class but not in the exam" is
so often a method-selection problem rather than a knowledge problem.

An SSDD set makes the surface useless as a cue. Four questions look identical
and go four different ways, so the student has to read.

It is therefore **diagnostic as much as it is practice**. Which of the four a
student gets wrong tells you which method they have wrongly attached to that
surface, and that is usually more useful than the marks.

## When to use it

**After the individual methods are secure.** A student who can't do any of the
four learns nothing from discovering that four different things were needed.
Fluency first — `slop-build` earns this.

Best as a starter or plenary, or as revision across a unit. One set is five to
ten minutes, not a lesson. Two sets in a row is usually one too many.

## Designing

**Pick the surface first.** Something visually or verbally distinctive that
naturally supports several topics: a labelled triangle, a can of drink with
dimensions, a ratio, a number in standard form, a set of three values.

**Then find four questions that genuinely share it.** This is the hard part and
where sets fail. Every question must use the *same* given information — if one
needs an extra measurement or a different context sentence, the surface has
changed and the effect is gone. The student should be able to look at all four
and see one picture.

**For a shared *diagram* specifically, "same" doesn't mean identical printed
numbers on every panel.** It means the same shape, the same tick-mark and arc
skeleton, and the same general appearance. Forcing four different trig methods
off one triangle requires deliberately varying which quantities are given,
hidden, or replaced with the unknown — see **Geometry diagram construction**
below for the resolution pattern.

**Spread the deep structures deliberately**, and include topics from weeks ago.
That interleaving is the point: a set where all four questions come from the
current unit still lets students guess from context.

For the can of drink: volume of a cylinder, surface area, scale factor with
volume, and a partly-filled cylinder on its side. Same object, same two
measurements, four unrelated pieces of mathematics.

**Vary the difficulty across the four** so there's an entry point and a
stretch. Students should be able to start somewhere.

**Watch for a question that gives another away.** If working out the first
answer hands you a value the third needs, the set is a chain rather than four
independent questions.

## Geometry diagram construction

Trig SSDD sets nearly always share one labelled triangle, and the same
handful of things eat the build time on every one of them: where the vertices
actually go, where a second triangle's mirror sits, where a label clears the
triangle's own lines, where the tick marks for "these sides are equal" go, and
where to put a coloured angle badge. None of it is task-specific.
`scripts/triangle_geometry.py` does all of it — import it rather than
re-deriving the coordinate trigonometry inline:

```python
import sys; sys.path.insert(0, "scripts")
from triangle_geometry import (triangle_sas, triangle_sss, mirror,
                                label_anchors, tick_marks,
                                angle_badge_point, interior_angles,
                                side_lengths)

tri = triangle_sas(p=7, theta_deg=52, q=9)          # two sides + included angle
second = mirror(tri, axis="vertical", translate=(4.5, 0))
anchors = label_anchors(tri, vertex_offset=0.3, side_offset=0.3)
ticks = tick_marks(tri, "AB", count=1)
badge = angle_badge_point(tri, "A", distance=0.35)
```

`triangle_sas` and `triangle_sss` return vertices keyed `'A'`, `'B'`, `'C'`
plus a `sides` dict using the standard convention — side `a` = BC is opposite
vertex A, side `b` = AC is opposite vertex B, side `c` = AB is opposite vertex
C — the same convention the table below assumes, so the diagram's labels and
the worked solution use the same letters. `interior_angles` and
`side_lengths` read the angles and lengths straight back off a built or
mirrored triangle, which is what the QA check below uses.

### Gotchas

- **pptxgenjs's `line` shape only draws within its own bounding box.** An
  arbitrary diagonal from `(x1, y1)` to `(x2, y2)` needs:
  ```
  x = min(x1, x2),  y = min(y1, y2)
  w = abs(x2 - x1), h = abs(y2 - y1)
  flipH = x2 < x1,  flipV = y2 < y1
  ```
  Skip this and a diagonal drawn "backwards" — right-to-left or
  bottom-to-top — either fails to appear or appears reflected into the wrong
  quadrant of its own bounding box. (python-pptx's `add_connector` doesn't
  have this problem — it takes the two endpoints directly — but check it if
  porting a diagram between the two.)
- **Neither pptxgenjs nor python-pptx has a usable small-arc primitive for an
  angle mark.** Don't try to draw one. Use coloured, matched text instead —
  see the labelling convention below.

### Given values → forced method

Work out which rule a question is actually forcing *before* choosing numbers,
or the four panels end up needing the same method under different surface
dressing.

| Given | Asked for | Forced method | Note |
|---|---|---|---|
| Two sides + the included angle (SAS) | the third side | Cosine rule | To block a congruence shortcut (matching the two triangles by side length rather than reasoning), leave the corresponding side in the second triangle unlabelled. |
| Two sides + a non-included angle that is a known side's own opposite angle (SSA) | the other unknown angle | Sine rule | **Ambiguous case.** Don't assume the calculator's first answer is the only one — check explicitly whether the supplementary angle (180° minus that answer) is ruled out by the angle sum before treating the question as having one solution. |
| Two angles + one side (ASA / AAS) | another side | Sine rule | The third angle comes free from the angle sum; that's what makes the third side reachable. |

**Structural limit:** in an SAS-only triangle (two sides and the included
angle, nothing else), no angle can be found without finding the third side
first — a "find the side" question and a "find an angle" question drawn from
the same SAS data will always chain, whatever the panel design tries to do
about it. Either accept the chain as a deliberate difficulty progression and
say so in the report, or give the extra side as a stated given specifically to
decouple the two questions.

### Diagram-labelling convention

- **Variables and unknowns render in italics.** Bold italic inside the
  diagram, where it needs to be spotted fast; plain italic inline in question
  text. Use an italic serif/maths face — Cambria Math, or italic Cambria or
  Times as a fallback. Never bold upright sans-serif; it reads as a label, not
  as a value to be found.
- **Never put a filled circle or badge behind a value purely to show it
  corresponds to another value.** A tick mark (sides) or a consistent accent
  colour (angles) already carries that meaning — a background shape adds
  visual weight with no new information. Treat this the same as the general
  rule against decorative content competing with instructional content.
- **Default 3-colour convention**, so every diagram this plugin draws reads
  as one system:
  - `#262626` (near-black) — given values and the triangle's own outline.
  - `#1F4E79` (navy) — correspondence marks: matching tick marks, and
    matching-coloured text for angles that correspond across two triangles.
  - `#C00000` (red) — the unknown, i.e. whichever value the question is
    actually asking for. This reuses the red already used elsewhere in the
    plugin for worked-solution values, so red keeps meaning "the thing being
    found" across decks, worksheets and diagrams alike.

### Same surface for diagram-based sets

For a shared-*diagram* set, "same surface" means the same triangle shape, the
same tick-mark and arc skeleton, and the same general appearance — not
literally identical numeric labels on every panel. Forcing four different
trig methods off one triangle requires deliberately varying which quantities
carry a printed number, which are hidden entirely, and which is replaced with
*x*.

The resolution pattern: **keep the triangle's shape and every tick mark or arc
constant across all four panels — build it once and reuse the same vertices
for every panel — and vary only which quantities carry a printed number
versus which one is "x".** A student comparing the four panels should see one
triangle with the labels moved around, not four different triangles.

### Geometry QA check

Alongside the usual overflow/overlap pass, after rendering **confirm the
drawn proportions plausibly match the stated numbers**: the longest labelled
side should look longest, a given obtuse angle shouldn't render as visibly
acute, a right angle should look like one. Read the numbers back with
`interior_angles()` and `side_lengths()` on the built (or mirrored) triangle
and compare them to what the question states — a mismatch means a sign or
offset error in the coordinate math. This is the class of bug a text-only QA
pass, which only checks labels and layout rather than the shape they're
attached to, will never catch.

## Writing it up

Full solutions for all four, plus the part that makes the set worth running:

- **What each question actually requires**, named as the method.
- **Which wrong method each question invites**, and what a student choosing it
  would produce. That's the diagnosis, and it's what you'll talk about
  afterwards.
- **The discussion question** — usually "what did you have to notice to tell
  these apart?" This is where the learning consolidates, and without it the set
  is just four questions.

## Output

- **As a slide** — the stem large in the centre, four questions in the
  quadrants around it, matching the exemplar layout. Use
  `scripts/copy_slide.py` with `templates/slide-patterns.pptx`; the retrieval
  starter pattern already has the quadrant structure and dividers. Where the
  shared stem is a labelled triangle, build it with `scripts/triangle_geometry.py`
  (see **Geometry diagram construction** above) rather than placing shapes by
  eye.
- **On paper** — A4 portrait, stem centred, four questions around it, working
  space in each quadrant. Hand to `worksheet-build` for the layout mechanics.

Answers go in the speaker notes or on a separate teacher sheet, never on the
student-facing page.

## Verify

Work all four independently and check symbolically with `sympy` where the
algebra is non-trivial. Then check the property the set depends on: **read the
four questions as a student would and confirm the surface really is
identical** — same shape, same units, same diagram, no extra information
smuggled into one of them. (For a diagram set, "identical" is about the shape
and its tick marks, not the printed numbers — see **Same surface for
diagram-based sets** above.) That's the failure mode a solution check won't
catch.

For a diagram-based set, also run the **Geometry QA check** above — a solver
that gets the algebra right will not notice a triangle whose drawn angles
don't match the numbers it was built from.

## Report

The surface, the four deep structures, which topics they reach back to, and the
misconception the set is designed to expose. If you couldn't find four genuine
deep structures for the surface, say so and offer three plus a suggestion —
a padded fourth question defeats the whole design.

