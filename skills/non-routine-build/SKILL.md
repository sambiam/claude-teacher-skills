---
name: non-routine-build
description: "Find or write non-routine problems for a maths class — problems with no signposted method, reachable with mathematics the class already has, where the work is deciding what to do. Curates from UKMT, the Australian Mathematics Competition, nrich and textbook enrichment before writing anything new, and writes up the route in rather than just the answer. Use when a class needs genuine problem solving rather than more procedure: 'they need something to think about', 'a rich task for', 'problem solving questions on', 'something for a Friday', 'a competition-style problem', 'they can do the procedure but can't apply it', 'reasoning and problem solving'. Also use when an assessment audit finds a unit has no problem-solving opportunities."
---

# Non-routine problems

Problems where the method isn't signposted and the work is in deciding what to
do. The Sierpinski triangle whose perimeter is given and whose total line
length is wanted. The cryptarithm `3y × 4yy = 1y77y`.

Reference: `Practice questions/Non-rotuine-Examples.pdf`,
`standards/practice-types.md`.

## What makes one work

**Reachable with mathematics the class already has.** This is the property
people get wrong. The difficulty must live in the *seeing*, not in a missing
technique — a problem that needs a method the class hasn't met isn't a
challenge, it's a wall, and students correctly conclude they were set up to
fail. Check the required knowledge against the unit outline and the class
profile before offering anything.

**A low floor.** A student should be able to start by trying something: draw
it, try a number, do the first case. If the only way in is the insight, most of
the room gets nothing.

**One real observation at the centre.** The best of these turn on a single
noticing — that the perimeter counts each internal edge twice, that the last
digit of a product constrains y to two values. That observation is what you'll
discuss afterwards, and it's what the student takes away.

**Worth ten to fifteen minutes.** Not five, which isn't enough to get stuck and
unstuck; not a whole lesson unless it's a designated problem-solving lesson.

## Curate before you write

Good non-routine problems have usually been tried on hundreds of students, and
that trialling is exactly what a freshly written problem lacks. A problem that
looks elegant and turns out to have an ambiguity or a much easier route than
intended wastes the lesson.

So look first, in this order:

- The unit folder and the school's resource bank — something already used here
- Textbook enrichment and extension sections
- **UKMT** Junior, Intermediate and Senior Challenges — deep archive, carefully
  calibrated by age, answers and full solutions published
- **Australian Mathematics Competition** past papers
- **nrich** — searchable by topic and stage, with teacher notes
- **Problemo** (problemo.edu.au, Australian Maths Trust) — 400+ problems for
  years 3–10, **classified against the Australian Curriculum**, and each one
  ships with an *enabling prompt* and an *extending prompt*. Best curriculum
  alignment of any source in this list and the differentiation is already done.
  Requires a login; the free tier is 100 problems with solutions.
- **MathPickle** (mathpickle.com) — organised by grade, **Creative Commons**,
  explicitly invites classroom use. Printables and the free *Infinite Pickle*
  book.
- **Don Steward / Median** (donsteward.blogspot.com) — **CC BY-NC-SA 4.0**, so
  unlike almost everything else here it may be reproduced and modified for
  non-commercial classroom use with attribution. 400+ topic labels. The family
  asks for a discretionary donation to education charities in Africa. This is
  the source to reach for when the problem has to go onto a printed sheet.
- **Play With Your Math** (playwithyourmath.com) — 32 numbered one-page
  problems, deliberately unlabelled by year. Strong Friday tasks.
- **Goal-free problems** (goalfreeproblems.blogspot.com) — 200 problems by
  strand, for the students who freeze at multi-step questions.

Search the web for these where you have access. Say clearly which problems you
found and which you wrote, so the teacher knows what has been used before.

**Check the offline bank first.** `sa-task-design` carries 48 fully written,
answer-verified tasks for Years 7–10 plus an offline mirror of the 83-task
three-act catalogue, and it works with no internet. Several of its tasks —
T7-01 *Exactly three*, T7-07 *Five numbers*, T8-01 *Make x as big as you can*,
T10-01 *The coin jar* — are non-routine problems in everything but name.

Write a new one only when the gap is real — a specific topic with nothing
suitable — and then keep it simple, because a complicated new problem has more
places to go wrong.

## Matching to the class

Pick the difficulty from where the class actually is, not from the year level.
A Junior Challenge problem can be right for a strong Year 7 and for a Year 10
class that struggles with reasoning, and the second use is often the more
valuable one.

Check the reading load. A problem whose difficulty is partly comprehension is
testing something you may not have intended, and for an EAL-heavy class it
tests it a lot.

## Writing it up

The answer alone is nearly useless. For each problem:

- **The route in** — the observation that unlocks it. This is what the
  discussion is about and what you'd give as a hint.
- **The full solution**, including the arithmetic, so the teacher can follow it
  cold in front of a class.
- **Two hints of escalating strength**, so a stuck student can be moved without
  being given the answer. The first should point at where to look; the second
  should name the observation.
- **A wrong route students commonly take**, and where it runs out — worth
  knowing in advance because you'll see it.
- **What a student who solves it has demonstrated**, if it's being used
  assessably.
- **Where it came from** — source and year, both for credit and so the teacher
  can find more like it.

## Running it

Note in the write-up how to run it, because non-routine problems fail on
classroom management more often than on mathematics:

- Time to work alone before any discussion, so nobody's thinking gets
  short-circuited
- Whether to pair afterwards
- When to give hint one and hint two
- What to do with the students who finish in three minutes — usually
  "generalise it" or "find a second method"

## Output

- **As a slide** — problem alone, large, no clutter. Solution in the speaker
  notes. Use `scripts/copy_slide.py` and the patterns in
  `templates/slide-patterns.pptx`.
- **On paper** — through `worksheet-build`, with real working space; these need
  room to try things.
- **As Extra Hot** on an existing worksheet, clearly marked optional.

## Verify

Solve every problem yourself, fully, before shipping it. For anything with
enumerable cases, enumerate them in code rather than reasoning to the answer —
cryptarithms and digit problems in particular have a habit of admitting a
second solution nobody noticed.

Then check the problem is well posed: unique answer where the wording implies
one, no missing information, no reliance on a diagram that isn't there, no
required knowledge the class doesn't have.

## Report

Each problem with its source, the mathematics required, estimated time, and the
observation it turns on. Flag anything you wrote yourself rather than curated,
because untried problems deserve a wary first outing.

