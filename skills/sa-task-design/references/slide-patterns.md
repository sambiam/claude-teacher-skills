# Rendering a task — slides, standalone deck, or worksheet

A task is not finished until it is in the form the lesson needs. This file covers
the slide route; for a printed page, dispatch to `worksheet-build` and stop here.

This skill has **no PowerPoint machinery of its own and must not grow one** — it
uses `deck-build`'s. Read `deck-build/SKILL.md` before writing any PowerPoint
code.

## What deck-build provides

```
templates/lesson-template.potx      theme + layouts, no slides
templates/slide-patterns.pptx       one worked example of each recurring pattern
scripts/copy_slide.py               open_template, find_pattern, copy_slide,
                                    clone_slide, set_text, replace_text,
                                    render_math, replace_picture, audit_slide,
                                    drop_named
scripts/omml.py                     equation(), equation_lines() — real equation
                                    objects
scripts/anim.py                     click-to-reveal entrance animations
```

Filenames vary between departments — check the actual template folder rather than
assuming these exact names.

Three of `deck-build`'s rules bind this skill absolutely:

1. **Every piece of mathematics is a real equation object** via `omml.equation`,
   never text with superscript formatting and never a picture.
2. **The slide gets inked over in the lesson.** Leave genuinely empty space. A
   task slide that is full at build time has nowhere for the class to work.
3. **No completed working on a teaching slide.** The answer lives on a separate
   reveal slide.

## Pattern inventory

The patterns below are the ones this skill draws on. Numbers are positions in the
reference pattern deck as it stood on 1 Sep 2026 — **verify them against your own
copy before relying on them**, because a pattern deck that has been edited will
have shifted.

| # | Title on the slide | Use it for |
|---|---|---|
| 2 | *3. Explain a connection* | retrieval starter with mixed response modes |
| 4 | *Lesson goal* | bridging prior knowledge to today |
| 7 | *CATEGORICAL — example vs non-example* | definition + example + close non-example |
| 8 | *Is it an example?* | quick yes/no category check |
| 9 | *Which category does each case belong to?* | three cases, choose a category |
| 13 | *Decision checks* | the full cognitive routine — cues, decisions, actions |
| 17 | *Worked example* | teacher model plus matched student task |
| 18 | *Which response best answers the question?* | four-option diagnostic |
| 19 | *Check in — decide for each case* | five varied cases, one short result each |
| 20 | *Spot the error — does it work?* | misconception or partially correct method |
| 21 | *Evidence for your choice* | matching, sorting, classifying with justification |
| 22 | *Extending prompt* | bounded extension changing one structural condition |
| 23 | *Independent practice* | bookwork |
| 24 | *Exit check — apply, justify, connect* | end-of-lesson application |

## Three build traps, all of them caught the hard way

**`find_pattern()` matches speaker notes, not titles.** Pattern decks usually
carry generic notes ("Pattern use: Use for a bounded extension…") rather than a
restatement of the title, so a title-keyword lookup raises `KeyError`. **Index by
position instead** — `pat.slides[n]`, with `n` from the table above, checked
against your own deck.

**`open_template()` can give you a 4:3 canvas.** Lesson templates often default to
10 × 7.5 in while the pattern deck and every real lesson deck are 13.333 × 7.5 in
(16:9). Set `prs.slide_width` / `prs.slide_height` to 13.333 in / 7.5 in
immediately after opening the template and **before copying any pattern slide in**
— otherwise every copied shape's absolute coordinates run off the right edge.

**Pattern frames can be label-sized, not content-sized.** In the *Worked example*
pattern, `worked-example-frame` / `your-turn-frame` are about 0.5 in tall.
Anchor multi-line content (e.g. `equation_lines`) **below** the frame's bottom
edge — `frame.top + frame.height + ~0.5 in`, not the frame's own top — or the
content overflows with no visible container. Also drop that pattern's decorative
circular icon before writing a second title near it: it collides with a title
that wraps to two lines.

## Genre → pattern mapping

| Task genre | Slides to build |
|---|---|
| **WODB** | `Evidence for your choice` (21) for the grid — four items, the prompt "which one doesn't belong?", and space for reasons. Then a reveal slide with all four reasons. |
| **Estimation** | A picture slide from `Worked example` (17) with the photo full-width and three stems: *too low / too high / my estimate because…*. Reveal slide with the actual value. |
| **Same but different** | `CATEGORICAL — example vs non-example` (7), retitled *"Same but different"*, the two objects side by side. |
| **Open Middle** | `Extending prompt` (22) — the skeleton as an equation object with `\square` boxes, the digit rule below it, and half the slide empty. A second slide, *"best so far"*, stays blank for the teacher to ink the running record. Reveal slide carries the verified optimum. |
| **SSDD** | `Check in — decide for each case` (19): one diagram, four questions, one line of space each. Dispatch to `ssdd-build` for the set itself. |
| **Maths Venn** | `Evidence for your choice` (21) with the two circles as a picture; every region empty. Reveal slide with one example per region and which regions are impossible. |
| **Slow reveal graph** | One slide per reveal stage, same position, same size, using `anim.py` for click-to-reveal — or simply duplicate the slide with more of the graph each time. Prompt stem identical on every stage: *what do you notice / what's your story now*. |
| **Goal-free** | `Worked example` (17) with the diagram and the words *"Work out everything you can."* No question box. Reveal slide lists everything deducible. |
| **Error analysis** | `Spot the error — does it work?` (20). This pattern already exists for exactly this. |
| **3-act / modelling** | Act 1: a full-bleed image or video-link slide with one line — the question. Act 2: `Decision checks` (13) with the stem *"What do you need to know?"*, blank. Act 3: reveal. Sequel: `Extending prompt` (22). |
| **Visual pattern** | `Worked example` (17) with steps 1–3 drawn, then three stems: *step 10 / step n / where is your rule in the picture?* |
| **Non-routine problem** | `Extending prompt` (22) with the problem, and the whole lower half empty. Dispatch to `non-routine-build`. |

## The slide set every task produces

Whatever the genre, build this sequence. It is short on purpose.

1. **The task slide.** The prompt, exactly as it will be read aloud, and nothing
   else. Half the slide empty.
2. **A thinking slide** *(optional, for tasks over 10 minutes)* — the same prompt
   with the entry hint added, revealed only if the room stalls. Keep the hint to
   one sentence and make it a *starting move*, never a method.
3. **The reveal / answer slide.** Full working where the task has one answer;
   the verified optimum and the insight where it is an optimisation; all four
   reasons where it is a WODB.
4. **The consolidation slide.** The single question that names what was learned.
   This is the slide that is most often skipped and it is the one that turns the
   task into teaching.

Put the launch script, the anticipated responses and the timing in the **speaker
notes**, never on the slide.

## Where the slides go

**Into an existing lesson deck**, at the position the task's slot implies:

- **starter** → after the retrieval starter, before *Lesson goal*
- **post-teaching / deepening** → after the I do / We do / You do run, before
  *Independent practice*
- **plenary** → immediately before or in place of *Exit check*

**As a standalone deck** — for a whole-lesson task, or whenever no existing
lesson deck was supplied. Name it for the task and save it beside the unit's
numbered lesson decks, following that folder's naming convention.

**Never overwrite an existing deck.** Save alongside.
