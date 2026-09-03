---
name: practice-test-build
description: "Build the revision paper a maths class sits before the real topic test, plus its worked answer sheet — same skills and mark weighting as the real test, but the questions asked in enough different ways that students can't rehearse it. Use whenever a practice test, revision test, practice paper, mock, pre-test or 'something to see if they're ready' is needed, including 'make a practice test for the equations topic', 'the kids need revision before Friday's test', 'build a practice paper that matches the 2026 test', or 'is there a practice test for this unit'. Also use to fix a practice paper that is too close to the real one, too hard, or short on fluency practice. Works from the topic folder: it finds the real test itself. For the graded test students actually sit, use test-build."
---

# Building a practice test

A practice test has one job: tell a student what they can't yet do, while
there's still time to fix it. Everything here follows from that.

Two ways to fail it, and the second is less obvious than the first:

**Too close to the real paper.** Mirroring it question-for-question with new
numbers produces a second form of the test. Students then revise the practice
paper as a rehearsal, arrive knowing the shape of every question, and someone
who has memorised the sequence scores well without being ready. The practice
paper stops measuring anything.

**Too far from it.** Replacing every question with error analysis, explain-your-
reasoning and worded problems makes a harder, different paper. It starves
students of the repetitions they actually need the week before a test, and the
score misinforms them in the other direction — they come away believing they're
further behind than they are.

The target sits between. Same skills, same weighting, same arithmetic
difficulty; roughly **60% of the marks routine fluency and 40% complex**, with
each core skill getting a real run of straightforward repetitions before
anything clever appears.

## Step 1: Find the real test

```bash
python scripts/find_test_sources.py "<class>/units/<topic>/" --templates "templates/"
```

Read the actual papers, most recent first. Filenames lie about years and
contents; the newest paper is the specification, and an older one may describe
a format the faculty has since abandoned. If the newest test differs
structurally from the one before it, the practice paper follows the newest, and
the report says so.

Also read any existing practice test in the folder. If it was built against an
older format, work out exactly which marks it now mis-trains — that comparison
is often the most useful thing to hand back.

Record from the real test before designing anything:

- Total marks, and marks per skill
- Which question types appear, and which have been dropped
- Layout conventions: header, numbering, working grids, mark placement
- The page count

## Step 2: Confirm the brief

Take what the folder gives and ask about the rest in one go:

| Detail | Where to look |
|---|---|
| Which real test to match | folder, newest first — confirm if ambiguous |
| Topics taught but not on the test | unit outline; ask |
| Topics on the test the class hasn't reached | ask — the common rebuild trigger |
| Page limit | ask if not stated; four pages is a sensible default |
| Total marks | match the real test unless the content changes |

**Teacher instructions outrank the folder.** If they ask for a topic the real
paper doesn't assess, include it and flag the mismatch — they know what their
class has covered and may be adding it to the test. Don't silently drop
something they asked for on the grounds that the real paper lacks it. If they
later reverse the decision, that's information rather than a contradiction.

## Step 3: Design the paper

### Hold constant

Skills assessed, marks per skill (proportionally — an exact copy of the mark
scheme isn't needed), total marks, arithmetic difficulty, and the faculty's
layout conventions. A student should be able to read their practice score as an
estimate of their real one.

### Vary how questions are asked

Rotate formats *across* the paper rather than reinventing every question.
Useful ones, all testing the same underlying skill:

| Format | What it exposes |
|---|---|
| Direct "solve / expand / simplify" | fluency — the bulk of the paper |
| Matching or table completion | recall, without a page of writing |
| Fill in the missing number or step | whether they can run the procedure backwards |
| Spot the error in a student's working | whether they know *why* each step is legal |
| Substitute to check a claimed answer | whether they can verify their own work |
| "Circle the equation with solution x = …" | recognition rather than production |
| "Write your own question whose answer is …" | flexible command of the idea |
| Short worded problem | translating English into algebra |
| Multi-step problem combining two skills | whether the pieces connect |

Anchor every varied item in a skill the real test assesses. A format that needs
a skill the test doesn't cover is a different paper, not a practice one.

Prefer formats the faculty already uses. Prior papers are worth mining for
this: if last year's test asked students to circle an error in a worked
solution, that format is familiar and fair, and reusing the *format* is not the
same as reusing the question.

### Give fluency enough volume

This is the part most often got wrong. Variety in *format* is not a substitute
for *repetitions*. Every core skill needs roughly **four or more straightforward
parts** before its complex variants appear — a student who can't yet solve
`3y + 5 = 20` reliably needs four of those, not one of those and three clever
ones. Put the routine run first and the complex items at the end of each
section, so every section still has an entry point for the weakest student.

### End with one genuine stretch question

Around 4 marks, at the end, drawn from the same topic rather than a different
one. The best kind combines two skills the paper has already practised
separately and has a real decision at the start — for solving equations,
something like `5(2x − 3) + 4 = 39`, which needs expanding before the two-step
method applies. Keep the answer clean and split the marks one per step.

### Check the split before building

Count the marks:

- **Routine** — direct solve/expand/simplify, table completion, recall.
  Multi-step procedural counts here too; more steps is not a different kind of
  thinking.
- **Complex** — error analysis, worded problems, explain-why, write-your-own,
  fill-in-the-missing-step, recognition questions needing justification.

Aim for 60/40. At 75/25 the paper is a rehearsal; at 50/50 it's a reasoning
test. Report the actual figure, and say which side of the line any judgement
call sits on — "is a 4-mark multi-step solve routine or complex" is genuinely
arguable, and the teacher may see it differently.

### Tell the student what this is

One line under the name field, in the student's own interest:

> This practice test covers the same skills as the topic test. Some questions
> are asked in a different way, so read each one carefully. Show all working.

Without it, a student meeting an unfamiliar format assumes they've been taught
the wrong things. This line is for the student — keep design notes about the
paper out of the student document entirely.

## Step 4: Build the documents

Read `references/layout-and-formatting.md` before building.

Build from the **real test file**: open it with python-docx, strip the body
with `docx_math.clear_body(doc)`, and write the new content in. That inherits
the section setup, margins, header with the school crest, styles and fonts
exactly. Recreating the look produces a paper that is almost right, which both
students and teachers notice.

Change the header title so it reads as practice — the title usually lives in
`word/header*.xml` split across several runs (`'Algebra '` + `'T'` + `'est A'`),
so match on the pieces rather than the whole string.

Use `scripts/docx_math.py` for the equation objects and working grids:

```python
import sys; sys.path.insert(0, '<skill>/scripts')
from docx_math import mr, frac, sup, delim, add_math, eq_run, grid, slot, clear_body
```

Read its docstring first. Two silent traps cost the most time: an equation
element that starts or ends with `=`, and an unbalanced fragment inside a
bracket. Both look right in the source and render as `¿` in the PDF.

### Answer sheet

Build it from the finished student file — copy it, type the working into the
same grids, export to PDF. Three things make it hold:

- Insert solutions **immediately after the question paragraph** in each cell,
  not appended at the end, or they sink to the bottom of a tall box far from
  the question.
- Every answer goes inside a **fixed-height container**. Answers with nowhere
  natural to sit — a blank in the question line, a circled option — need
  reserved space too; `slot()` gives an invisible fixed-height strip that is
  blank on the student version. Without it the two documents paginate
  differently and stop lining up.
- One real tick glyph per mark, method marks against the line where the
  approach appears. Never put a literal `✓` inside solution prose — a
  "Check: … ✓" line reads as a mark tick and inflates the count.

## Step 5: Verify

```bash
python scripts/check_marks.py practice.docx --expect 40 --tick-manifest ticks.json
python scripts/check_layout.py practice.docx --solutions answers.docx --max-pages 4
```

Give the tick manifest the **same granularity as the printed mark
allocations** — if the paper says `[4 marks]` once for parts (a)–(d), the
manifest needs one key worth 4, not four keys worth 1, or the check reports a
mismatch that isn't there.

`check_layout.py` catches what the source can't show: the real page count, a
blank or nearly-empty final page, and whether the answer sheet paginates
identically to the student paper.

**Install `libreoffice-math` first** — without it LibreOffice silently drops
every equation and the rendered pages show blank working spaces where the
mathematics should be. The script warns if it's missing.

**Work every answer independently with sympy.** Solve each equation, expand
each expression, substitute the answer back into the original. For a "circle
the correct option" question, evaluate every option to confirm exactly one is
true. An answer generated alongside its question has not been checked.

Then look at the rendered pages:

- [ ] Every skill on the real test appears, with proportional weight
- [ ] No skill the real test doesn't assess, unless the teacher asked for it
- [ ] Each core skill has four or more straightforward parts before its
      complex ones
- [ ] The first question of each section is accessible to the weakest student
- [ ] No question is a real-test question with the numbers changed
- [ ] Routine/complex split counted, reported, and near 60/40
- [ ] One stretch question, from the same topic, at the end
- [ ] Nothing collides with the header
- [ ] Working boxes roomy enough for the working each question needs
- [ ] No question split from its box or its marks line by a page break
- [ ] No blank or nearly-blank final page; within the page limit
- [ ] No `¿` and no plain-text mathematics anywhere
- [ ] Answer sheet matches the student paper page for page
- [ ] Ticks per question equal its marks

## Step 6: Save and report

Into the topic folder's revision area, with the year, never over an existing
paper:

```
<topic>/Revision/<Year> <Topic> Practice Test.docx
<topic>/Revision/<Year> <Topic> Practice Test SOLUTIONS.pdf
```

The report is where the teacher checks the judgement calls. Give them:

- Marks per skill, next to the real test's marks per skill
- The routine/complex split as a number, and any item whose classification is
  arguable
- What each varied format is testing, so it reads as deliberate rather than
  decorative
- If an older practice test existed: which of its marks the format change made
  obsolete
- Anything included or excluded against what the real paper does, and why
- A plain statement that the paper needs a human read before it goes to
  students

Say that last line every time. The scripts catch arithmetic and pagination, not
judgement — whether a question is fair for *this* class is the teacher's call,
and the paper is never "ready to hand out" on this skill's say-so.

## Reference files

- `references/question-design.md` — question design rules, difficulty balance
- `references/layout-and-formatting.md` — working spaces, page discipline,
  mathematical formatting
- `references/solutions-overlay.md` — answer sheets, ticks, mark placement
- `scripts/docx_math.py` — Word equation objects and layout primitives
- `scripts/check_marks.py` — mark and tick arithmetic
- `scripts/check_layout.py` — page count, blank pages, pagination parity
