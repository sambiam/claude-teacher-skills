---
name: "practice-audit"
description: "Judge whether the practice attached to a lesson is enough — mapping every existing question against the lesson's atoms, estimating whether the set fills the available time, checking the difficulty gradient has a real entry point, and verifying answers exist. Use before building any new practice material and whenever the sufficiency is in doubt: 'is there enough practice', 'do we have questions for this', 'check the exercises', 'will this fill the lesson', 'does the textbook exercise cover this', 'can every student start this'. Reports a per-atom coverage map, a verdict, and whether to supplement or rebuild; hand the gaps to practice-select to choose the type and to the generator skills to write them."
---

# Auditing the practice attached to a lesson

The question this answers: **if this class walks in tomorrow, do they have
enough of the right practice, and can every student in the room get started?**

Both halves matter. A resource that covers the content perfectly and opens at
the difficulty the lesson finished at leaves the students who most need
practice unable to begin.

## Gather what exists

Practice hides in several places. Check all of them before concluding anything
is missing:

- The lesson deck — question slides, "your turn" problems, Spicy panels
- `questions/` or equivalent for the unit
- The textbook exercise or Padlet named in the unit outline
- Any worksheet in the lesson or unit folder, including previous years'
- Activities, card sorts and tasks stored separately

For **Years 7–9** the practice is usually *in the deck*, answered in books —
so a lesson with no worksheet is not a lesson with no practice. Check the
slides before reporting a gap. For **Years 10–12** look for the textbook
reference on the last teaching slide, in the form `8B (page 208) Q2a-c, 3-10`.

Read the unit outline for what this lesson is *supposed* to practise. A pile of
questions on the wrong sub-skill is not practice for this lesson.

## The four tests

A resource has to pass all four.

### 1. Coverage, atom by atom

Read `<unit>/<lesson>/atomisation.md` — or the lesson deck if there isn't one —
and list the atoms the lesson teaches. Then map each existing question to an
atom, and **report the map, not just the verdict**, because the gap is the
actionable part.

The common failure: the lesson teaches three atoms, the exercise drills the
first twenty times and never touches the other two.

The subtler failure worth naming when you see it: **every question exercises
the atoms in combination and none in isolation**. A wrong answer to
`3(x + 4) = 21` might be a bracket error or an inverse-operation error, so a
set of only combined questions produces no usable diagnostic information even
when the coverage table looks complete.

### 2. Quantity against time

Available practice time is the lesson length minus the teaching phase minus
transitions — usually 15–25 minutes of independent work in a standard period.

Starting figures for time per question, to be calibrated against real classes:

| Question type | Rough time |
|---|---|
| Single-step fluency (mental or one line) | 20–40 sec |
| Multi-step procedure | 1–2 min |
| Worded or contextual problem | 2–4 min |
| Multi-part problem-solving task | 5–10 min |

Aim for enough that the fastest student is still working at the bell, without
the slowest facing an obviously impossible list. In practice: the core set fits
the median student in the available time, with extension beyond it.

Running out is the more damaging error of the two, because the cost lands in
the last ten minutes of the lesson.

### 3. Difficulty gradient

The set should start where every student can begin unaided. Check that:

- The first two or three questions are directly parallel to a worked example
- Difficulty rises gradually, not in one jump
- The hardest core questions are reachable for the median student, with the
  real stretch in extension rather than buried at the end where slower students
  never see it
- There is something for early finishers that isn't just more of the same —
  a Spicy question, an Open Middle, an extension task

Flag a set that opens at the level the lesson finished at.

### 4. Answers

Check answers exist and are correct. Practice without answers can't be
self-checked, which quietly removes the feedback that makes practice work. If
answers exist but you can't verify them, say so rather than assuming — and
spot-check a few of the harder ones with `sympy`.

## Verdict

```
## Practice audit: <lesson> (<class>, Year <N>)
Available practice time: ~<M> minutes
Found: <each resource and where it lives>

### Coverage
| Lesson atom | Questions | Isolated or combined | Verdict |

### Quantity
Estimated working time for the core set: <X> min against <M> min available

### Gradient
<entry point, progression, ceiling, provision for early finishers>

### Answers
<present / partial / missing / unverified>

## Verdict
<Sufficient | Sufficient with gaps | Insufficient>
Gaps: <specific — "no questions on the third atom; nothing below textbook Q4
as an entry point">
Recommended action: <use as is | supplement with N questions on X | build new>
```

**Prefer supplementing over rebuilding.** If a textbook exercise covers two of
three atoms well, six extra questions on the third is a better answer than a
whole new worksheet — less work, and the class stays on a resource they already
know how to navigate.

Be willing to return "sufficient". An audit that always finds a gap stops being
useful, and the teacher's time is the scarcest resource in this system.

## Handing off

This skill diagnoses; it doesn't write questions.

- `practice-select` chooses what type the gap needs
- `slop-build`, `open-middle-build`, `ssdd-build`, `non-routine-build` write it
- `worksheet-build` produces it as a printable handout, if paper is warranted
- `differentiation-pack` handles the entry-point problem when the issue is
  access rather than quantity

## Judging an existing worksheet

Audit against `standards/good-worksheet.md` if it exists. If it doesn't,
`worksheet-build` carries the default specification — use that, and note that
the local standard should be written down properly, because the definition of a
good worksheet is a pedagogical decision that belongs to the teacher rather
than to a skill.

