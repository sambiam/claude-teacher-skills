---
name: deck-build
description: "Build a lesson PowerPoint by lifting proven slide patterns out of the branded pattern deck and filling them with a lesson's atoms and teaching sequences — retrieval starter, lesson goal, prior knowledge check, NPPPN and minimal-difference runs, I do / You do, diagnostic MCQs, Spicy panels, persistent reference panel, and either in-book questions (Years 7-9) or a textbook reference (Years 10-12). Also reviews or repairs an existing deck against that specification. Use whenever slides are needed or need fixing — 'make the slides for', 'build tomorrow's lesson', 'fix this deck', 'the slides need more worked examples', 'add a check for understanding to this', 'does this lesson follow the spec' — or when a unit outline names a lesson with no deck. Not for tests or assessments; use test-build or assessment-audit."
---

# Building lesson decks

A deck someone can walk into a room and teach from, where the cognitive load
lands on the mathematics rather than on decoding the slide.

The distinctive thing about these decks, and the thing most easily lost: they
are **near-empty and repetitive on purpose**. A typical teaching slide is a
title, one mathematical object, and nothing else, and five consecutive slides
may differ by one character. That is variation theory doing the teaching. Slide
count is free; working memory is not.

## The deck gets written on

These decks are taught from a screen the teacher inks over — that is why
`ink-progress` can read a taught deck and tell you where the class got to — and
it changes what belongs on a slide more than any other single fact about them.

**A teaching slide carries the question, the diagram and the answer frame —
never the completed working.** The frame is the stems the answer will be built
on, written out and then left empty:

```
bottom gap =
side gap   =
P =
P =
```

not

```
top gap  = 14 − 6 = 8cm        overall width minus notch width
side gap = 9 − 4  = 5cm        overall height minus notch height
P = 14+9+8+6+4+5               walk the boundary once, in order
P = 46cm
```

The second version is the same slide with the lesson already taught on it.
There is nothing for the teacher to do in front of the class except read it
out, nothing for the class to predict, and no room left to write. Every I do,
every You do, every check: stems and space.

Three consequences worth stating separately, because each one gets missed:

- **Leave the space.** Half the slide below the diagram, or the column beside
  it, stays genuinely empty. A slide that is full at build time has nowhere for
  the lesson to happen. If a layout has no room to write, cut something.
- **Printed blanks are a worksheet device, not a slide device.** `missing = 12
  − 5 = ___cm` and `P = 12 + 7 + __ + 5 + 3 + 4` belong on paper. On a slide
  the completion problem is the stem plus the space — the fading comes from
  how much of the stem you give, not from underscores.
- **Completed working lives on answer slides.** A separate reveal slide, or
  the final rung of a fading run, carries the full vertical solution with its
  right-hand annotation column. That is where `equation_lines` belongs.

The same rule governs the right-hand annotation column generally: *"π button,
final answer to 1 dp"*, *"diameter given directly"*, *"walk the boundary once,
in order"* are things the teacher says. On an answer slide they name the step
for each line and earn their place. On the slide the teacher is about to model
from, they pre-empt the only thing the teacher was going to contribute. Put
them in the speaker notes.

## Read first

- `standards/good-deck.md` — the visual and structural specification. Overrides
  everything here.
- `standards/teaching-sequences.md` — how each atom type is taught.
- `standards/class-defaults.md` and `classes/<class>/profile.md` — year level,
  period length, textbook, cohort.
- The unit outline, for where this lesson sits.

## Get the lesson design before opening PowerPoint

The deck is a rendering of a lesson design, not the design itself. You need:

- `<unit>/<lesson>/atomisation.md` — the atoms, typed, with Assume/Check/Teach
- `<unit>/<lesson>/teaching-sequence.md` — how each is taught

If either is missing, run `atomise` and `teaching-sequence` first. Building
slides from a topic name produces a deck that covers the topic and teaches the
procedure while assuming the decisions, which is the standard failure and it
doesn't show up until the test.

If the teacher wants something quick and doesn't want the analysis, at minimum
name the atoms and their types before building, and say in your report that the
atomisation was inferred rather than done.

## The assets

```
templates/lesson-template.potx    theme + layouts, no slides
templates/slide-patterns.pptx     one worked example of each recurring pattern
scripts/copy_slide.py             slide copying, leftover audit
scripts/omml.py                   LaTeX -> real PowerPoint equation objects
scripts/anim.py                   click-to-reveal entrance animations
scripts/triangle_geometry.py      vertices, labels and tick marks for a custom triangle diagram
```

**Copy the pattern; don't rebuild it.** These positions have been used in front
of classes. Reconstructing a layout from coordinates gets you something that
looks almost right and reads as slightly wrong all lesson.

```python
import sys; sys.path.insert(0, "scripts")
from copy_slide import (open_template, find_pattern, copy_slide, clone_slide,
                        set_text, replace_text, render_math, replace_picture,
                        audit_slide)
from pptx import Presentation

prs = open_template("templates/lesson-template.potx")   # python-pptx can't open .potx
pat = Presentation("templates/slide-patterns.pptx")

s = copy_slide(find_pattern(pat, "NPPPN CATEGORICAL"), prs)
for _ in range(4):
    clone_slide(prs, s)      # then change only the mathematics on each
```

`find_pattern` matches the label in each pattern slide's speaker notes, so ask
for a pattern by name rather than by slide number.

### Every equation is an equation object. No exceptions.

**Maths is never plain text with superscript formatting, and never a bare
picture.** It is a real PowerPoint equation object, so variables italicise, the
fraction bar is a bar rather than a slash, exponents sit properly, and the
teacher can click in and edit. Getting this wrong is the single most visible
defect in a generated deck, and Year 7–9 notation — fractions, indices,
negative coefficients — is exactly where it shows.

Use `scripts/omml.py`:

```python
from omml import equation, equation_lines, NAVY, RED

equation(slide, r"\frac{3x + 7.5}{5} - 2 = 2", 6.66, 3.7, sz=4000, anchor="cc")
```

`sz` is hundredths of a point, as everywhere in OOXML: `sz=4000` is 40pt.
`anchor` is two characters, horizontal then vertical, from `l|c|r` and
`t|c|b` — `"cc"` centres on the point given, `"lc"` left-aligns at it.
Pass `max_w` (inches) and it shrinks the point size to fit rather than
overflowing.

Supported LaTeX subset: digits, letters, operators, `\frac{}{}`, `^{}`,
`\text{}` for upright words inside maths, `\div \times \cdot \pm \le \ge \ne`,
arrows, and spacing. It is **not** full LaTeX — no environments, no packages.

**Why it is written the way it is.** Each call emits the same structure
PowerPoint itself writes: an `mc:AlternateContent` holding the real
`<a14:m><m:oMath>` in `mc:Choice`, and a matched picture in `mc:Fallback`.
Both branches carry the same shape id, so an animation targeting that id works
whichever one renders. This matters for a reason you will otherwise waste an
hour on: **LibreOffice ignores the `a14` namespace entirely**, so a plain
`<a14:m>` paragraph renders as nothing at all when you convert to PDF to proof
the deck. With the fallback in place the PDF shows the equation at the correct
size and position, and what you are proofing is the real layout.

Where the maths sits *on top of* another image — the mini-whiteboard graphic, a
printed triangle — don't swap that image. Place the equation over the centre of
the board.

For a vertical worked solution, see **Answers and worked solutions** below;
`equation_lines` handles the stack.

### Audit every copied slide before saving

```python
texts, pictures = audit_slide(slide)
```

Then check nothing from the source lesson survived. A cheap end-of-build sweep
catches what per-slide editing misses:

```python
for i, s in enumerate(Presentation(out).slides, 1):
    for sh in s.shapes:
        if sh.has_text_frame:
            for bad in ("permutation", "m&m", "2x + 7", "sine rule"):
                assert bad.lower() not in sh.text_frame.text.lower(), (i, bad)
```

**Text is the easy half. Check the images too.** The exemplar decks carry
lesson-specific pictures that a text sweep will never catch — a padlock from
the combinations lesson, a Drake meme, a triangle from the sine rule. They look
like branding and they are not. Extract every picture on every copied pattern
and *look at it* the first time you use that pattern, then hard-code the
drop list:

```python
drop_named(s, "Picture 7", "Picture 4")   # Drake meme, padlock
```

Keep only images that do instructional work — the mini-whiteboard graphic, the
thumbs up/down pair, the MWB routine poster — and drop everything that belonged
to the source lesson's content.

**Edit text with `set_text` and `replace_text`, never by assigning to
`text_frame.text`.** Direct assignment throws away the run formatting that made
the pattern worth copying, and you get 18pt Calibri where a 40pt navy title
should be. Delete the pattern label from the notes once a slide is filled.

## Source before you generate

The pattern deck is not the only prior art. Before drawing a diagram or
inventing an example, look in the unit's own `02. Powerpoints` folder — the
neighbouring lessons, the `Atomised` and `Activities` subfolders — and lift
what already exists. A slide the teacher has taught from before is worth more
than a better one they have never seen, and the two lessons then feel
continuous instead of like two different courses.

Match the neighbouring decks' conventions when you do build something new, and
look at them to find out what those are rather than assuming:

- **Fill shapes with a light tint** rather than leaving them as bare outlines.
  A filled figure reads as an object; an outline reads as a drawing of lines,
  which is precisely the wrong prompt on a lesson about which lines count.
- Copy the unit's labelling house style — boxed variable labels, mid-side
  notch marks, right-angle squares, arrows for parallel sides — from the
  deck that already uses it.
- Keep diagrams at a fixed on-slide size regardless of their stated
  measurements, the way a textbook page does, and say "not to scale" once.

External tasks count as prior art too. Where the lesson runs a published task —
a Make Math Moments 3-act, an Esti-Mystery, an nrich problem — build the slides
it needs (the notice-and-wonder, the reveal, the follow-up question) and add a
small **Lesson resources** slide holding the links, so the teacher can find the
video from inside the deck on the day.

## Geometry diagram construction

For a **custom** diagram — one drawn in code because no template pattern
covers it, most often a labelled triangle for a trig lesson — don't re-derive
the coordinate geometry inline. `scripts/triangle_geometry.py` builds the
vertices, a mirrored second triangle, label-anchor points for each vertex and
side midpoint, tick-mark endpoints for a side, and an angle-bisector point for
a badge:

```python
import sys; sys.path.insert(0, "scripts")
from triangle_geometry import (triangle_sas, triangle_sss, mirror,
                                label_anchors, tick_marks,
                                angle_badge_point, interior_angles)

tri = triangle_sas(p=7, theta_deg=52, q=9)   # two sides + included angle
anchors = label_anchors(tri, vertex_offset=0.3, side_offset=0.3)
ticks = tick_marks(tri, "AB", count=1)
```

`triangle_sas`/`triangle_sss` return vertices `'A'`/`'B'`/`'C'` plus a `sides`
dict on the standard convention (side `a` = BC opposite A, and so on), so a
diagram's labels line up with whatever the worked solution calls each side.

**Gotchas specific to drawing this in a slide library:**

- **A `line` shape (pptxgenjs) only draws within its own bounding box.** An
  arbitrary diagonal from `(x1,y1)` to `(x2,y2)` needs
  `x=min(x1,x2), y=min(y1,y2), w=|x2-x1|, h=|y2-y1|, flipH=(x2<x1), flipV=(y2<y1)`,
  or a diagonal drawn "backwards" fails to appear or renders reflected into
  the wrong quadrant of its box. python-pptx's `add_connector` takes the two
  endpoints directly and doesn't have this problem.
- **There's no usable small-arc primitive for an angle mark**, in either
  library. Don't try to draw one — use coloured, matched text instead, per the
  labelling convention below.

**Diagram-labelling convention**, so custom diagrams match the house style
referenced above rather than inventing a new one per lesson:

- Variables and unknowns are italic — bold italic inside the diagram (needs
  to be spotted fast), plain italic inline in question text. An italic
  serif/maths face — Cambria Math, or italic Cambria or Times as a fallback.
  Never bold upright sans-serif.
- Never put a filled circle or badge behind a value purely to show it
  corresponds to another value — a tick mark (sides) or a consistent accent
  colour (angles) already carries that, and a background shape is decorative
  content competing with instructional content.
- Default 3-colour convention: `#262626` (near-black) for given values and
  outlines, `#1F4E79` (navy) for correspondence marks (matching ticks,
  matching-coloured angle text), `#C00000` (red, matching the colour already
  used for worked-solution values elsewhere in this plugin) for the unknown.

**Geometry QA check**, alongside the label-spacing check already covered under
**Before handing over**: after rendering, confirm the drawn proportions
plausibly match the stated numbers — the longest labelled side should look
longest, a given obtuse angle shouldn't render as visibly acute.
`interior_angles()` on the built triangle gives the actual numbers to compare
against the question; a mismatch is a sign or offset error in the coordinate
math, which a text-only slide audit won't catch.

## Structure

1. **Retrieval starter** — 3–4 numbered questions in quadrants, one from last
   lesson, one from further back, plus a Spicy. Answers on the next slide.
2. **Hook / headache** — one slide, immediately after the starter and *before*
   the goal slide, where the class does the thing the lesson is about to make
   easier, using only what they already have. It has to land before students
   know what is coming or the relief is spoiled. `lesson-rationale` builds it
   and carries the full specification; deck-build's job is to leave the slot
   and to place it here rather than next to the content it motivates. A
   concrete task beats a described one — measure these two shapes with a
   ruler, estimate from this photograph, produce four different answers to one
   question.
3. **Today's focus / lesson goal** — capabilities in student language. **One
   goal slide, not two.** Either the plain capability list or the "You can
   already do this / You can't do this — yet" contrast, whichever suits the
   lesson; building both means the class reads the objectives twice and the
   second one is where attention is already gone. Every capability listed must
   trace directly to a Teach atom (or a Teach-worthy Check atom) in the
   atomisation — this slide is not a summary of the topic, it is the Teach-atom
   list in student language. An Assume atom's content may appear here only as
   the contrast case (the "already secure" half), never as an objective in its
   own right; if the goal slide reads like the lesson is about the Assume atom,
   the pacing that follows will teach it that way too.
4. **Prior knowledge check** — the atoms marked *Check*. **Immediately after
   the goal slide, before the first teaching sequence** — its whole purpose is
   to decide whether the teaching that follows can go ahead, so anything taught
   before it is taught on an untested foundation. Under two minutes,
   whole-class response. Put in the notes what to do if they fail it; a check
   you'd ignore is theatre. **One standard question and one Spicy per slide —
   see below.**
5. **Teaching** — each *Teach* atom gets its sequence rendered slide by slide.
6. **Practice** — see below.
7. **Exit check** — 2–3 questions separating those who have it from those who
   don't.

**Where a deck spans more than one period, it splits at a section-break slide
and only the final period carries an exit check.** Don't append a second
practice tier, a second extension slide and a second exit check to the end of
phase one just because the phase ended — that is four slides the teacher
deletes on the day. One practice block per phase; the extension is the Spicy
panel, not extra slides.

## Check-for-understanding slides: one question, backups behind a click

A check inside the teaching sequence carries **one standard question and one
Spicy, and nothing else on screen.** Extra questions go on the same slide,
hidden, each revealed by its own click, and used only if the class gets the
first one wrong.

Do not label them (a), (b), (c). A lettered list reads as a set to be completed
and that is the opposite of what a check is for.

The reason is timing, not clutter. Five questions on a check slide means the
fastest student finishes in forty seconds and the slowest in four minutes, so
you either cut the check short or lose the room. One question puts the whole
class on the same beat, and the backups mean you are never stuck improvising a
second example on the board.

```python
from anim import click_reveal
click_reveal(slide, [backup1_id], [backup2_id])   # one click each
```

`scripts/anim.py` writes the `<p:timing>` tree by hand — python-pptx has no
animation support. Entrance effects hide the shape until its click arrives, so
nothing else is needed to keep the backups off screen. `equation()` returns the
shape id as the fifth element of its tuple; that is what you pass in.

**You cannot proof an animation by converting to PDF** — the export flattens
everything and shows every backup at once. Say so in your report and tell the
teacher to check it once in slideshow view.

This rule is about checks. It does **not** apply to the opening retrieval
starter, or to book practice, where several labelled questions are correct.

**The NPPPN test stage is not an exception, and it is where this rule is most
often broken.** A slide reading *"Check-in: for each shape, is the red line
part of the perimeter? (yes / no)"* with three shapes strung across it is the
lettered-set failure wearing a different hat: the class works at three
different speeds, the answers arrive as a chorus, and you learn nothing per
item. Render the test items the way the taught items were rendered — one item
per slide, same wording, same position — or drop the separate test stage and
let a single fresh check carry it. If the run was short because the
distinction is easy to retain (see `teaching-sequence`), a separate test stage
is usually the thing to cut.

## Rendering each atom type

**Match the pattern to the atom type. This is a hard rule.** The image on a
slide tells students what response is wanted, so a thumbs up/down graphic on a
question that needs working is a promise the slide doesn't keep, and students
answer the wrong way. Before building, walk the atomisation and write the
pattern against each atom:

| Atom type | Pattern | Response |
|---|---|---|
| Categorical | `NPPPN CATEGORICAL` (thumbs) | thumbs up/down, finger vote |
| Transformation | `MINI-WHITEBOARD QUESTION` | mini-whiteboards |
| Fact | `DEFINITION` → reference panel | repeat back |
| Cognitive routine | `WORKED EXAMPLE \| YOUR TURN`, `I DO` | written attempt |

The failure this prevents is subtle and easy to ship: a sequence *about* a
decision is not automatically a categorical atom. "What do we divide both sides
by?" sounds like a classification and is actually a transformation — the
student has to carry out a division, not sort an object into a bin. It belongs
on the whiteboard slide. Conversely "is the whole top of this fraction
grouped?" is a genuine categorical and belongs on the thumbs slide, one
instance per slide.

**Categorical → NPPPN.** Five consecutive slides, one item each, same title
wording every time, thumbs up/down. Build the first properly, then clone and
change only the item. Notes on each: positive or negative, and which principle
it serves.

The **decision rule box** goes on the first two or three items and is deleted
from the rest — but only if the rule is worth reading. *"If it's on the outer
edge of the shape: perimeter. If it's a line inside the shape: not
perimeter"* under the title *"Is this line part of the perimeter?"* is the
title restated, and it is the second object on a slide that is supposed to
hold one. Keep the box where the rule genuinely resolves something the item
alone doesn't — *"If it's a line drawn only to show a measurement: not
perimeter"* earns its place, because a radius line looks like an edge. Drop it
where the rule is a paraphrase of the question.

**Transformation → continuous conversion.** A run of near-identical slides
where one thing changes. **Nothing else may move** — same position, size and
layout, so the eye tracks the mathematics rather than a shape shifting two
millimetres. Cloning guarantees this; rebuilding doesn't. Render each
expression at the same fontsize and centre it identically.

**Fact.** State it on one slide, *Repeat back* cue in the corner, then move it
into the persistent reference panel for the rest of the lesson.

State it as the object itself, not as a sentence about the object. A labelled
diagram beside a real equation object, and an instruction that makes the class
produce the fact — *"write one formula on each side of your whiteboard"*,
*"choral response"* — does the work that *"Circumference is always π times the
diameter, and since the diameter is twice the radius that's the same as 2 × π
× radius"* only describes. Prose on a fact slide is the explanation the teacher
was going to give.

**Where a fact has two equivalent forms — `C = πd` and `C = 2πr`, area of a
trapezium either way round — put both on the slide, each beside its own
labelled diagram, and then treat *choosing between them* as a categorical atom
with its own short run.** *"Which formula should you use?"* over one circle
with a radius marked, one with a diameter marked, one measurement running
edge-to-edge but not through the centre, one given by a bounding box. Knowing
both forms and knowing which one this diagram hands you are different
capabilities, and the second is the one the test asks for. If the atomisation
missed it, say so and add it.

**Cognitive routine.** I do → You do, paired, always in that order. Build the
worked example so it appears in steps — successive slides or animation — with
the reveal order from the teaching sequence. Never two worked examples with no
attempt between them.

**One slide, one step — and the You do pairs to that step, not to the whole
routine.** A title reading *"I do: find both missing sides, then add the
boundary"* is two steps, and the You do that follows it is the whole routine
with nothing modelled in between. Split it: *I do: find both missing sides* →
*You do: find the missing side* → *I do: add the boundary* → *You do: find the
perimeter*. The pairing is per step, and the step names itself in the title.

**For anything built on a formula, separate forming the expression from
evaluating it.** Ask *"what would give the circumference?"* and stop at the
substitution — `C = π × d`, then `C = π × (10)` — before any slide asks for a
number. Students who go straight to the calculator have made the substitution
invisibly and you cannot see which of them chose the wrong form, doubled the
radius, or neither. Run the *what would give* pass across the whole set, then
evaluate.

Between the I do and the You do, build the **completion problem** the teaching
sequence specifies. On a slide this is the answer frame with the load-bearing
lines left as bare stems and the rest of the space empty — not underscores, not
a partially printed calculation; see **The deck gets written on**. A deck that
jumps from a complete worked example straight to a bare problem has no rung in
the middle, and it is always the students who copied your example correctly who
fall off it.

**Every slide that wants a written response gets the mini-whiteboard graphic
with the answer stems already on it** — `x =`, `y =`, `P =`, `missing =` — and
nothing else. The stems are what stop half the class writing a bare number and
the other half writing a sentence, and they are the same stems the answer slide
will fill in. This applies to a question slide lifted from another deck as much
as to one you built: drop the whiteboard underneath it and write the stems on.

**The tick box goes on the slide, not in the notes** — a small bordered box
beside the You do, with blank checkboxes the student marks themselves. Four
marks for Years 7–9.

Write them in the student's words, short enough to self-mark in five seconds:

```
☐ Calculated missing side
☐ Wrote out all the numbers which need to be added
☐ Correct answer
☐ Answer given as a length (cm)
```

not *"Found each missing side from the correct known segments"* or *"Included
every boundary side exactly once — none skipped, none doubled"*, which are
accurate, are about process, and are a paragraph a Year 8 will not read while
also marking their work. Keep them mostly about process; one item may be the
answer itself. Ten components is Year 11 granularity and it starts awarding
marks for bookkeeping rather than mathematics.

## Answers and worked solutions

**Answers are laid out vertically, line by line, the way a teacher writes them
on the board.** Never a horizontal arrow chain — `9k = 63 → ÷9 → k = 7` is a
description of a procedure, not a piece of working, and it is not the thing you
want students to copy.

```python
equation_lines(slide, [
    (r"12 - 5x = 2",  None),
    (r"-5x = -10",    "take 12 from both sides"),
    (r"x = 2",        "divide both sides by -5"),
], x=1.0, y=2.4, sz=2600, gap=0.7, note_x=5.2)
```

The right-hand note names the inverse operation for that line. Read the note
column down the page and it is the back-tracking chain — say that to the class.

**An answer is the substituted expression and then the number, not the number
alone.** `C = π × 6 = 18.8cm` and `P = (π × 16 ÷ 2) + 16 = 41.1cm`, so a
student checking their book can see which line they went wrong on rather than
only that they did. On a set of final answers this costs one extra term per
line and is what makes the slide usable for self-marking.

A slide of final answers is fine for a six-question book exercise, but pick the
one or two questions most likely to go wrong and give each a full vertical
solution of its own. Two blocks side by side is the maximum; three columns of
working is unreadable at the back of a room.

## Space

Crowded text is a defect, not a detail. Set `space_after` on every multi-line
box, keep body text clear of the title box (titles wrap to two lines more often
than you expect — check the rendered image, not the character count), and keep
annotation columns from colliding with the next column of working. If a title
wraps and something sits under it, shorten the title rather than moving the
box.

## Verify every answer with a solver before you save

Not by eye. Write the whole question set out as assertions and run them:

```python
from sympy import symbols, Eq, solve, nsimplify
x = symbols('x')
assert solve(Eq((3*x + 4)/2 - 4, 7)) == [6]
```

This is not belt-and-braces. On a 60-slide deck it reliably finds two or three
real errors — an answer that drifted when a coefficient changed, a "your turn"
whose answer isn't a whole number when it was supposed to be. Every one of them
would otherwise be found by a student, in the lesson, at the worst moment.

## Practice, by year level

**Years 7–9: questions go in the deck, answered in exercise books.** Build a
section of question slides — four to eight per slide, answers on the following
slide — sequenced by the variation rules in `standards/practice-types.md`. No
worksheet, no laptops. Paper is finite and getting devices out costs five
minutes and half the room.

Size it so the fastest student is still working at the bell. Ask
`practice-audit` if you're unsure whether there's enough.

**Years 10–12: assign from the teacher's usual source.** A small boxed
reference in the corner of the last teaching slide, in the house form:
`8B (page 208) Q2a-c, 3-10`. If the unit outline doesn't name the source, ask —
a wrong page reference costs the teacher more than a missing one.

Build a junior worksheet only when books genuinely can't carry it: printed
diagrams, card sorts, layouts that need the page. `practice-audit` decides,
`worksheet-build` produces.

## Spicy panel

A red-bordered box, top or bottom right, persisting across a run so nobody
waits on the teacher. Not the same question with worse numbers — construct an
example with a given property, do it in the fewest steps, generalise, work
backwards. Sources in `standards/practice-types.md`; `open-middle-build` writes
good ones.

**Where it goes: retrieval, checks and practice. Not on an I do or a You do.**
Those slides are modelling one step to the whole room at one pace, and a second
question in the corner is exactly the split attention the one-question rule
exists to prevent. The first slide students work independently on is the first
slide that needs a Spicy.

**Put the Spicy's answer on the slide** — small, under the box or beside it, or
on the matching answer slide if there is one. It is the question most likely to
be attempted by the students the teacher is least likely to reach, and an
answer they can check against is the whole point of the panel being there.

## Persistent reference panel

A boxed panel down the right holding the fact, formula or criteria list the
current work depends on. It removes a memory task competing with the thing
being taught. Keep it up for the whole phase that needs it; take it down when
the fact should be secure. Facts still being learned belong here — a method the
lesson is trying to automate does not.

## Speaker notes

Everything teacher-facing goes here, nothing on the slide: what each distractor
diagnoses and what to do about it, the misconception targeted, timing, what to
cut if the class is slow, who to call on, and for NPPPN slides why this example
is positive or negative.

## Improving an existing deck

Diagnose before rewriting. Read it with `markitdown deck.pptx`, atomise what it
actually teaches, and list specific defects first:

- Slides carrying more than one idea
- Worked examples with no matched problem
- Missing retrieval starter, prior knowledge check or exit check
- Atoms taught as procedure where the atomisation says categorical — usually
  showing up as a definition and three positive examples with no non-examples
- Scaffolding that fails to fade, or fades in one jump
- Dense text slides with no worked example
- Decorative content competing with instructional content
- Teaching slides with the working already printed on them, leaving the
  teacher nothing to model and nowhere to write
- An I do whose title names two steps, or which has no matched You do before
  the next step starts
- Two goal slides, a check placed after the teaching it was meant to gate, or
  a hook placed next to the content it was meant to motivate
- A second practice tier, extension and exit check appended to a phase that
  isn't the end of the deck

Then make the smallest set of changes that fixes them. A deck the teacher
already knows how to teach has real value and wholesale rewriting throws it
away. Preserve slide order and sound worked examples, and say what changed.

**If the deck carries ink annotations, work on a copy** — see `ink-progress`.
The annotations record what was actually taught and where the class got to.

## Before handing over

Render to images and look at them — this catches what code inspection can't,
and on these decks it is where you discover an equation from the source lesson
still sitting on slide 6.

```bash
soffice --headless --convert-to pdf deck.pptx && pdftoppm -png -r 60 deck.pdf s
```

Tile them into contact sheets and actually look, rather than reading the code
back to yourself:

```python
ims = [Image.open(f) for f in sorted(glob.glob("s-*.png"))[:12]]
w, h = ims[0].size
sheet = Image.new("RGB", (w * 3, h * 4), "white")
for i, im in enumerate(ims):
    sheet.paste(im, ((i % 3) * w, (i // 3) * h))
```

Check every worked example has its matched problem, every question has an
answer somewhere, nothing overflows its container, titles aren't clipped when
they wrap to two lines, and the near-identical runs really are near-identical.

Then look again for the things this deck fails at specifically:

- **Is there room to write on it?** Any I do, You do or check slide whose
  working is already printed on it, or which is full to the edges, is a slide
  the teacher cannot teach from. Stems and space — see **The deck gets written
  on**.
- **Does every I do have a You do for the same step, immediately after?**
  Read the titles down the deck as a list; a title naming two steps, or an I do
  followed by anything other than its matched attempt, shows up instantly this
  way.
- **Is there a second object competing on any single-item slide?** A decision
  rule that restates the title, an annotation column, a Spicy on a modelling
  slide, three test items strung across one check-in.
- **Are the diagrams the unit's diagrams?** Same fill, same labelling
  convention, same notation as the deck either side of this one.

**For any custom diagram — one drawn in code rather than copied from a
template pattern — check that every side label sits the same visual distance
from its edge**, regardless of whether that edge is horizontal, vertical or
slanted, and regardless of which side of the shape it's on. There's no
template prior art to inherit correctly from on a custom diagram, so this
class of bug has to be caught by looking rather than by copying a pattern that
already got it right. A flat vertical offset applied uniformly to every label
is a common cause of inconsistent spacing on anything but a horizontal top
edge — check a bottom edge and a slanted edge specifically, not just whichever
one happened to render first. `label_anchors()` in
`scripts/triangle_geometry.py` (see **Geometry diagram construction**) avoids
this by construction — it offsets each label along its own direction from the
centroid rather than by a flat vertical shift — so prefer it over hand-placed
coordinates for a triangle diagram.

Two things the PDF will not tell you, so say them in your report rather than
implying they were checked: **click animations don't survive the export** (the
teacher needs to run slideshow view once), and the PDF shows the equation
*fallbacks*, which are pixel-accurate for layout but are not proof that
PowerPoint parsed the OMML.

Save alongside the original rather than over it. Then report: what was built or
changed slide by slide, which atoms each phase covers, decisions you made where
the standards were silent, and anything the teacher needs to resolve.

