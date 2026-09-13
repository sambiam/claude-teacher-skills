---
name: "worksheet-build"
description: "Produce a printable mathematics worksheet and matching answer sheet as DOCX — Mild/Medium/Spicy sections plus an Extra Hot challenge, one section per atom, variation-theory sequencing, working space sized per row, real Word equation objects, and answers placed inside the working boxes. Use when the practice genuinely has to be on paper: 'make a worksheet for', 'print something for', 'they need a handout', 'the questions need diagrams', 'a card sort', 'turn these questions into a worksheet', 'regenerate the answer sheet', or after practice-audit reports insufficient practice. For Years 7-9 check first whether questions in the deck answered in books would do instead; for Years 10-12 prefer senior-homework-build. Also edits an existing worksheet and regenerates its answers."
---

# Building worksheets and answer sheets

A worksheet earns its place by doing something the textbook can't: matching
this lesson's atoms, this class's entry point, and this period's length. It
should read as a professionally designed classroom resource, not a generated
list of questions.

Priorities when they compete: mathematical correctness, atomisation of the
named skills, deliberate sequencing, useful variation, readable page design,
working space sized to the work, correct equation rendering, meaningful
differentiation, and an answer sheet that mirrors the worksheet.

## Check a worksheet is the right answer first

For **Years 7–9** the default is questions in the lesson deck, answered in
exercise books — see `standards/class-defaults.md`. Paper is finite and getting
laptops out to reach a PDF costs five minutes and half the room's attention. A
printed sheet has to earn itself: printed diagrams, a card sort, a layout books
can't carry, or a task students take home.

For **Years 10–12** the default is a textbook or Padlet assignment plus one
weekly consolidation sheet from `senior-homework-build`, not a sheet per
lesson.

If neither applies, say so and offer the alternative rather than building the
worksheet anyway. `practice-select` makes this call; `practice-audit` says
whether anything is needed at all.

## Read first

- `standards/good-worksheet.md`, if it exists — overrides everything here
- `standards/practice-types.md` — question types and design rules
- `<unit>/<lesson>/atomisation.md` — the atoms this consolidates
- `references/question-design.md` — variation theory, section contents,
  enrichment sources. Read before writing any questions.
- `references/docx-production.md` — page setup, the working-space table
  pattern, verified Word equation code, geometry diagram construction, the
  render-and-check loop. Read before building the DOCX.

Where this file and a reference file disagree, this file wins.

## A — Analyse

Work out what the worksheet consolidates before writing anything: the atoms,
the prerequisites, the intended sequence, the misconceptions this topic
reliably produces, and what counts as fluency versus reasoning here. The
atomisation gives you all of this; if there isn't one, run `atomise`.

If source materials exist — the lesson deck, textbook extracts, an earlier
worksheet, screenshots — inspect them closely as evidence of the terminology,
notation, methods, sequencing and difficulty students have already met. Infer
the progression and write new questions consolidating the same atoms; don't
copy the source's questions across.

If a question appears as an image, reproduce its mathematical structure rather
than trusting extracted text. Fractions, indices, brackets, powers and
multiplication signs are exactly what OCR mangles.

## B — One atom at a time

**Count the atoms in the request. Each gets its own practice before any
question combines them.** If the brief says "solving equations *and* the
distributive law", a worksheet where expanding only appears inside an equation
has not tested expanding — a wrong answer to `3(x + 4) = 21` could be a bracket
error or an inverse-operation error, and the teacher can't tell which. That
ambiguity is the failure this step prevents.

- Each atom gets a labelled block in **every** band it belongs in, not just the
  hardest one.
- Sequence bare skill → skill in context. Expand `3(x + 4)`, then solve
  `3(x + 4) = 21`.
- Combine only after each component has been practised alone, and put combined
  questions later in the band.

## C — Design the sections

**Mild / Medium / Spicy**, plus an **Extra Hot** challenge.

- **Mild** — each core atom directly, starting straightforward, adding one
  feature at a time. Not trivial, not ten near-identical questions. The
  sequencing rules in `slop-build` apply here; use them.
- **Medium** — the same mathematics applied securely: negatives, multiple
  variables, indices, more terms, less obvious structure. Difficulty from
  mathematical thinking, not from uglier arithmetic.
- **Spicy** — genuinely richer, not merely longer. In priority order:
  1. **Open Middle** constrained-digit problems. The best Spicy questions
     available — low reading load, no ceiling, every student can start, and
     optimising forces reasoning about structure. Prefer them, and use
     `open-middle-build` so the optimum is found by exhaustive search rather
     than intuition.
  2. Missing-value and reverse problems. "The solution is x = 1; find the
     number in the box."
  3. Comparing expressions; always / sometimes / never, with justification.
  4. Error analysis — useful but *diagnostic* rather than demanding, so it
     belongs in Mild or Medium, not a Spicy slot.
  5. Create-your-own to a target. Low priority: hard to mark, easy to satisfy
     trivially.
- **Extra Hot** — one clearly optional problem, visually separated so nobody
  reads it as a measure of failure. Genuinely higher-level mathematics, not
  uglier arithmetic, connected to the worksheet's theme. For a Year 8 sheet on
  equations and brackets, that's around Year 11 Methods: expanding both sides
  so a quadratic term cancels, solving in terms of a parameter, algebraic
  proof. `non-routine-build` is a good source.

Give each question one clear mathematical purpose. Don't combine unrelated
tasks under a vague heading.

### Say less

Students met the explanation in the lesson. A consolidation worksheet exists to
give them mathematics to do, so every line of prose has to earn its place.

- **Cut descriptive subtitles under section headings.** "Think carefully — these
  are not just longer versions of the questions above" tells the student
  nothing and costs vertical space that should be working room.
- Keep only short functional instructions — `Expand:`, `Expand and simplify:`,
  `Solve for x:` — which double as the atom labels from step B.
- One line of front matter: "Show all working in the box under each question."
- No worked example at the top unless the local standard asks for one. Guided
  notes and scaffolded entry are `differentiation-pack`'s job.

## D — Build

Follow `references/docx-production.md`. The rules most often broken:

- **Working space sits directly under the questions it belongs to.** A row of
  four short questions, then a row of blank boxes beneath them, then the next
  row. Never two rows of questions sharing one large space — students must see
  which space is theirs.
- **Size every box row to the work that row requires.** A per-row decision: a
  one-step and a four-step equation must not get the same box. Group questions
  of similar length into a row so one height fits all four. Starting values in
  DXA for `rule: "atLeast"`:

  | Work required | Worksheet | Answer sheet |
  |---|---|---|
  | Single-line expand, one-step equation | 1200 | 800 |
  | Two-step equation | 1600 | 900 |
  | Expand and simplify, multi-term | 1500 | 1000 |
  | Fraction equation, three steps | 1900 | 1100 |
  | Four steps, brackets plus rearrangement | 2200 | 1200 |
  | Spicy / Extra Hot, full width | 2300–2800 | sized to text |

  Then check the render and aim to fill each page. A page ending half empty
  means the boxes were too small; a section pushed onto a near-empty final page
  usually means a forced break should be removed.
- **Leave the boxes blank.** Don't print "Working" inside them.
- **All mathematics uses Word equation objects (OMML)** — true superscripts,
  true fractions, `×` for multiplication, never `*` or the letter x.
- **Open Middle boxes**: `☐` (U+2610) in a bold `TextRun` at around 34
  half-points with a space either side, mixed inline with `Math` runs for the
  algebraic parts. Don't draw the boxes as equation content.
- **Spicy and Extra Hot get their own layout** — numbered heading, full width,
  equations on separate lines, generous space. Don't force them into the
  four-column fluency grid.
- **A4 portrait**, margins that survive classroom printing, body text 11–12 pt
  minimum, prominent section headings, readable in greyscale. If it doesn't
  fit, cut questions — never shrink the font.

## E — Validate

Work every answer independently rather than trusting the answer generated
alongside the question, and check algebra symbolically with `sympy`: expand,
simplify, factorise, solve, test candidate roots, confirm equivalences.

**Open Middle answers must be found by exhaustive search.** A plausible-looking
arrangement is very often not optimal, and a Spicy answer a student beats
destroys the question.

Then read every question again for whether it is well posed — a computer can
confirm an answer but not that the question makes classroom sense. Look for
impossible conditions, multiple solutions where the wording implies one,
accidental duplicates, ambiguous variables, references to a diagram that isn't
there, and answers needing knowledge not yet taught.

Render and inspect before delivering: page count, equations, line wrapping,
box heights, page breaks, orphaned headings, whether Spicy is cramped, whether
any page ends half empty. Never deliver an unrendered DOCX.

A worksheet with wrong answers is worse than no worksheet — it destroys trust
in everything else the system produces. Flag anything you can't fully verify.

## F — Answer sheet

Generate from the **final** worksheet, not a draft. Mirror it: same section
order, numbering, expressions and positions, with each answer inside the
working box belonging to its question so a teacher can scan down the page
instead of cross-referencing a list. Answer-sheet boxes are sized to their
text.

- Final answer alone for simple fluency questions.
- Concise working wherever reasoning matters, and enough method on Spicy and
  Extra Hot that the teacher can see the intended route.
- For Open Middle, the optimum, the reasoning that finds it, and what a student
  who spots it has understood.
- "One possible answer:" where several are valid — and check the example
  satisfies every stated condition.
- Note accept-also forms and, where useful, the common wrong answer and what it
  indicates.

Use equation objects here too, and render and inspect this file independently.

## Building both files from one script

One script, one shared question data structure — each question carrying its
expression, final answer and intermediate working — and a boolean that swaps
the empty working cell for one containing the answer. Hand-copying question
order between two scripts is where answers drift onto the wrong questions.

## Editing an existing worksheet

The existing document is the source of truth. Preserve the teacher's edits —
reworded questions and rearranged sections are intentional unless they create a
mathematical error — and change only what was asked plus formatting that breaks
as a result. Never silently regenerate from an older version. Regenerate the
answer sheet by reading the current worksheet, not by editing the previous
answer sheet.

## Output

```
<unit>/<lesson>/<topic>_worksheet.docx
<unit>/<lesson>/<topic>_answer_sheet.docx
```

Report briefly: question count, estimated working time, which atoms each
section covers, that both files were rendered and checked, and anything flagged
as unverified. Don't reprint the question set — the teacher is about to open
the file.

