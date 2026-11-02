---
name: "test-build"
description: "Create a new student assessment and matching worked solutions for a maths class, built from the tests already sitting in that class's topic folder and formatted to the school's assessment template. Use whenever a test, topic test, practice exam, or assessment needs writing or refreshing for a new year — including 'make a practice exam for', 'we need a new version of the trig test', 'write a test on', or 'build an assessment for Year 11'. Also use when checking that a drafted assessment's marks, layout, and solutions are sound. Works from the folder, not from uploads: it finds prior tests itself. For a revision paper students sit *before* the real test, use practice-test-build instead."
---

# Building an assessment from the topic folder

Work as an Australian/SACE-style assessment designer: the tone, layout
conventions, command words, and front-page furniture should all read as though
they came from the same faculty that wrote the prior papers.

Produces two things: a student assessment as a Word document, and worked
solutions **handwritten in Sam's writing as Word ink over that exact
assessment** (via `handwritten-solutions`) — an editable ink `.docx` plus a
print PDF, with the working sitting in the working spaces.

The prior tests in the topic folder are the specification. They encode
difficulty that has been calibrated against real students, topic weighting that
matches what was taught, and layout conventions the faculty has settled on.
Reading them properly is most of this job.

**Building a practice test?** Use `practice-test-build` instead. A practice
paper that mirrors the real one question-for-question with new numbers is a
second form of the test, and students will study it as a rehearsal rather than
using it to find out what they can't yet do.

## Step 1: Find the sources

```bash
python scripts/find_test_sources.py "<class>/units/<topic>/" --templates "templates/"
```

This reports every test, practice test and solutions file in the topic folder,
pairs them, names the template, and lists what's missing. Read the files it
finds — the script classifies by filename, which is a map, not the truth.

**Sort by year and read the most recent paper first.** Faculties revise their
papers, and a format change is invisible from filenames. If this year's paper
drops two question types and adds two others, everything built from last year's
is calibrated to a test that no longer exists. When the newest paper differs
structurally from the one before it, say so explicitly in the report rather
than quietly following one of them.

Read the unit outline in the same folder for what was actually taught. A test
built from last year's paper without checking the outline will assess content
this year's class never saw.

If the folder has no prior assessment at all, say so before going further and
build from the template and unit outline alone — a test with no calibration
behind it needs more scrutiny from the teacher, and they should know that's
what they're getting.

## Step 2: Confirm the brief

Some of this is discoverable, some isn't. Take from the folder what you can,
then ask about the rest in one go rather than proceeding on assumptions:

| Detail | Where to look first |
|---|---|
| Subject and year level | class profile, folder path |
| Assessment type | what's being replaced, or the unit outline |
| Time allowed | prior test's front page |
| Total marks | prior test's front page |
| Topics to include | unit outline for this term |
| Topics to exclude | ask — this is rarely written down |
| Materials and calculator access | prior test's front page; ask if silent |
| Difficulty relative to the prior paper | ask only if there's reason to think it should change |

**Topics to exclude** is the one that most often causes a rebuild, because it
depends on where the class actually got to. Ask it explicitly even when
everything else is discoverable.

**Materials and calculator access** changes what questions are fair. Whether a
CAS or scientific calculator is allowed, whether a formula sheet is provided,
and whether there's a non-calculator section all determine whether a
trigonometry question can carry untidy numbers, or whether a statistics
question can assume summary statistics come off the device rather than being
computed by hand. Get it before drafting, not after.

**Teacher answers outrank inferences from the folder.** If the teacher asks for
something and the folder then appears to contradict it — a topic they want
included isn't on the newest paper, say — that is a discrepancy to raise, not
to resolve unilaterally. They know their class; the folder only knows last
year. Build what they asked for and flag the mismatch in the report. If new
information arrives that would have changed their answer, go back to them.

Unless told otherwise, the output is a student assessment as a **Word document**
and handwritten worked solutions (ink `.docx` + **PDF**).

## Step 3: Analyse before writing

Work through the prior assessments and record, for your own use:

1. Major topics and subtopics assessed, with marks per topic
2. The balance of routine fluency, multi-step procedural, interpretation,
   application/worded, and higher-order questions
3. Recurring question types and the skills each requires
4. Which topics are assessed routinely and which carry the application
   questions
5. Layout conventions: front page, marks table, numbering, subparts, mark
   placement, working grids, diagrams, page breaks

Keep this analysis out of the student document. Summarise it in the report at
the end instead — it's what lets the teacher check the reasoning quickly.

## Step 4: Write the assessment

Read `references/question-design.md` before drafting questions and
`references/layout-and-formatting.md` before building the document. The
short version:

- Match the structure, breadth, and difficulty of the prior assessments.
  **Matching is the default** — go harder only when asked, and then only where
  it stays fair and aligned.
- **Do not reuse the exemplars' questions, contexts, numbers, wording, or
  order.** New numbers on an old question is not a new question — students who
  have seen the old paper get an unearned advantage, which is exactly what a
  new version is meant to prevent.
- Every question must be answerable with skills the unit taught, using the
  materials the students are allowed.
- Marks must match the working the question actually requires.
- Don't group unrelated skills under one question number.

### Build from the real paper, not from a blank document

Open the most recent prior paper with python-docx, strip its body, and write
the new content into it. That inherits the section setup, margins, header with
the school crest and title block, styles, numbering and fonts exactly — none of
which can be reliably reconstructed, and all of which the teacher notices when
it drifts. `docx_math.clear_body(doc)` does the stripping.

Recreating the template's look instead produces a paper that is *almost* right,
which is worse than one that is obviously different, because nobody catches it
until it's printed.

Two things to fix after clearing the body:

- **The header title.** It lives in `word/header*.xml`, usually split across
  several runs (`'Algebra '` + `'T'` + `'est A'`), so match on the pieces
  rather than the whole string.
- **The top of the body.** School headers are often floating frames that
  reserve no vertical space, so the first body paragraph collides with the
  title block. Open the body with an empty spacer paragraph (~16pt) before the
  name line.

Where the new paper's structure closely follows the old one, an even safer
route is to edit the prior paper's XML in place — walk its `<m:oMath>` elements
in document order and replace their contents — which preserves the layout
exactly. Use that for a same-format rebuild; use `clear_body` when the
structure changes.

### Mathematics and working spaces

`scripts/docx_math.py` provides the OMML equation builders and the layout
primitives. Import it rather than rebuilding them each run:

```python
import sys; sys.path.insert(0, '<skill>/scripts')
from docx_math import mr, frac, sup, delim, add_math, eq_run, grid, slot, clear_body
```

Its docstring covers the two rendering traps that are silent and cost the most
time — a math element that starts or ends with `=`, and an unbalanced fragment
inside a delimiter. Both look correct in the source and render as `¿` in the
PDF that actually ships.

Working grids must have **exact** row heights (`grid()` sets this). That is
what lets the handwritten ink be anchored into the grid cells without the
solutions drifting off their questions.

## Step 5: Produce the worked solutions (handwritten)

Solutions are written **in Sam's handwriting as Word ink over the finished
student paper**, using the `handwritten-solutions` skill. Load it and follow
it; in short:

1. Build only from the **final** student `.docx` — the ink is anchored to its
   working-space cells, so any later edit to the paper means re-inking.
2. Work every answer first (Step 6, *Work every answer independently*), and
   check how each method was taught in the topic's lesson decks
   (`handwritten-solutions` Step 1) so the working matches the teaching — e.g.
   tangents as `y = f'(a)(x - a) + f(a)`, derivatives via index form first.
3. `python grids.py student.docx` numbers the working spaces; write `spec.py`
   with one list of lines per part and `\tick` once per mark — method ticks on
   the line where the approach appears, answer ticks on the final answer. The
   content rules in `references/solutions-overlay.md` (step-by-step working,
   units, model responses for interpretation questions, ticks = marks, where
   the marks are) still apply; its typed "derived document" and raster-overlay
   production methods are **superseded** by this.
4. `python inkdoc.py student.docx spec.py "<…> SOLUTIONS (handwritten).docx" --pdf`
   reports ticks against each `[n marks]`, and any box the working ran past or
   was written smaller in.

Two rules carry over from the typed method:

- Every answer needs a **fixed-height space** on the student paper to ink
  into. Answers with nowhere natural to go — a blank in the question line, a
  circled option — still get a `slot()` strip (blank on the student version),
  which `handwritten-solutions` treats as a box.
- Ticks are only ever `\tick` marks, one per mark. Never write a ✓ inside the
  working ("Check: … ✓") — it reads as a mark and inflates the count.

## Step 6: Verify

### Scripted checks

```bash
python scripts/check_marks.py student.docx --expect 80
python scripts/check_layout.py student.docx --solutions "<…> SOLUTIONS (handwritten).docx" --max-pages 4
```

`check_marks.py` reports whether the allocations sum to the declared total.
The tick count is checked by `inkdoc.py` when it builds the handwritten
solutions: it compares the `\tick`s in each working space with the `[n marks]`
printed under it, so put all of a question's ticks in the space that line
belongs to — if the paper says `[4 marks]` once for parts (a)–(d), the four
ticks are spread across those parts' columns of that one grid.

`check_layout.py` renders both documents and reports the true page count, where
content stops on each page, a blank or nearly-blank final page, and whether the
solutions paginate identically to the student paper (the ink floats over the
cells, so they always should). None of that can be judged from the source.

**Install `libreoffice-math` first.** Without it LibreOffice silently drops
every Word equation, and the rendered pages show blank working spaces where the
mathematics should be — it looks like a catastrophic bug in the document and
isn't. `check_layout.py` warns when it's missing.

### Work every answer independently

Do not trust an answer generated alongside its question — check it separately,
and **compute** anything numerical rather than reasoning about it. Use sympy:
solve each equation, expand each expression, and substitute the answer back
into the original. For a "circle the correct option" question, evaluate *every*
option to confirm exactly one is true. An error in a test is discovered
publicly and affects grades; it is the most expensive mistake this workflow can
make. Flag anything that couldn't be fully verified rather than letting it pass
silently.

### Final checklist

Convert both documents to images and work down this list by eye. The scripts
cover arithmetic and pagination; everything here needs looking at.

**Content and correctness**
- [ ] Every question has an independently verified answer
- [ ] No question requires a skill from an excluded topic
- [ ] No question is answerable only with materials the students don't have
- [ ] No impossible data sets, inconsistent conditions, or invalid equations
- [ ] No question gives away the answer to another
- [ ] No hidden assumptions — every value the question needs is stated
- [ ] Diagrams contain every value the question refers to
- [ ] Rounding instructions stated wherever approximation is expected

**Design**
- [ ] Topic balance matches the prior paper, or the change was requested
- [ ] Difficulty matches the prior paper, or the change was requested
- [ ] The first question of the paper, and of each topic, is accessible to the
      weakest student in the class
- [ ] No routine question is an exemplar question with the numbers changed
- [ ] No distinctive worded context is reused from the exemplars
- [ ] Unrelated subparts split into separate questions
- [ ] Question sequence isn't repetitive or obviously patterned

**Layout**
- [ ] Nothing collides with the header
- [ ] Working grids wide enough, with enough rows for the working required
- [ ] Marks sit after the working space, right-aligned
- [ ] No working grid under a question answered directly into a table, graph,
      or single-step response area
- [ ] Fractions, powers, roots and inequalities render properly — no `¿`, no
      plain-text shortcuts anywhere
- [ ] Graphs have square grids and unstretched axes
- [ ] No question split from its working space or its marks line by a page
      break
- [ ] No blank or nearly-blank final page
- [ ] No meta-commentary leaked into the student document

**Solutions (handwritten)**
- [ ] Page count and page positions match the student document exactly
- [ ] Ink sits inside its working spaces; any run-over below a box is small and
      clear of the next question
- [ ] Working follows the method as taught in the lesson decks
- [ ] Question text is readable on every page
- [ ] Strokes smooth and legible at 300 dpi — indices, fractions, decimal points
- [ ] Ticks per question equal its marks (inkdoc reports `ticks n / marks n`)
- [ ] Step-by-step working shown for anything multi-step
- [ ] Model responses given for interpretation questions
- [ ] Built from the final student document, not an earlier draft

## Step 7: Save and report

Write into the topic folder, with the year in the filename, never over a
previous year's paper:

```
<topic>/<Class> <Topic> <Type> <Year>.docx
<topic>/<Class> <Topic> <Type> <Year> SOLUTIONS (handwritten).docx
<topic>/<Class> <Topic> <Type> <Year> SOLUTIONS (handwritten).pdf
<topic>/<Class> <Topic> <Type> <Year> - handwritten spec.py
```

Then report, outside the student document:

- Topic balance, as marks per topic, next to the prior paper's balance
- Difficulty balance across the question types
- Which topics got application questions and why
- What changed from the exemplars, and any format change noticed between the
  faculty's own recent papers
- Assumptions made, and anything unverified
- A plain statement that the paper needs a human read before it goes to
  students

That last line is not a formality. Say it every time, even when the checks all
pass — the checks catch arithmetic and pagination, not judgement. Never
describe the paper as ready to hand out.

## Reference files

- `references/question-design.md` — question design rules and where
  application questions belong
- `references/layout-and-formatting.md` — front page, working grids, mark
  placement, mathematical formatting
- `references/solutions-overlay.md` — what the solutions must contain and
  where the marks go (its production methods are superseded by
  `handwritten-solutions`)
- `handwritten-solutions` skill — produces the solutions as ink in Sam's
  handwriting
- `scripts/docx_math.py` — Word equation objects and layout primitives
- `scripts/check_marks.py` — mark and tick arithmetic
- `scripts/check_layout.py` — page count, blank pages, pagination parity