---
name: "open-middle-build"
description: "Write Open Middle constrained-digit problems for a maths skill — a skeleton with empty boxes and a rule such as 'using the digits 1 to 9 at most once each, fill the boxes to make x as large as possible' — with the true optimum found by exhaustive search and the insight that finds it written up for the teacher. Use whenever a challenge, extension or Spicy question is needed that has no ceiling and every student can start: 'I need something for the fast finishers', 'give me a Spicy question for', 'make an open middle for', 'something challenging on', 'an extension task that isn't just harder numbers', 'a low floor high ceiling task'. Prefer this over harder arithmetic for extension. Verifies answers by enumeration, never by intuition."
---

# Building Open Middle problems

A skeleton with empty boxes and a constraint:

> Using the digits 1 to 9, at most one time each, fill in the boxes to make the
> value of x as large as possible.
>
> `☐☐ + x = ☐☐`

These are the best challenge questions available for a maths classroom, for
four reasons worth keeping in mind while designing: **low reading load** (a
student who struggles with text can still start), **every student can start**
(any arrangement is an attempt), **no ceiling** (there is always a better
arrangement to hunt for), and — the important one — **optimising forces
reasoning about structure rather than execution of a procedure**. The student
has to understand what makes x large, which is a different and deeper thing
than being able to solve for x.

Read `standards/practice-types.md` and the exemplars in
`Practice questions/Open-Middle-examples-for-training.pdf`.

## Prerequisite: fluency first

An Open Middle problem is useless to a student who cannot yet execute the
underlying procedure — they will spend the whole task stuck at the first step
and conclude they're bad at maths. Check the class can do the skill before
reaching for this. `slop-build` earns it.

## Designing

**Start from the skeleton, not the question.** Take the standard form of the
skill and blank out the numbers:

```
☐☐ + x = ☐☐              solving one-step equations
☐(x + ☐) = ☐☐            solving with brackets
☐x + ☐ = ☐x + ☐          unknowns on both sides
x² + ☐x + ☐              factorisable quadratics
☐☐/☐☐                    fractions closest to one
```

**Choose the objective so the optimum rewards an insight.** This is the whole
design. "Make x as large as possible" in `☐☐ + x = ☐☐` requires seeing that you
want the largest possible right side and the smallest possible left — which
means understanding the equation as a relationship rather than a thing to
solve. Objectives that work:

- as large / as small as possible
- as close as possible to a target (zero, one, an integer)
- make the result an integer, or a whole number of a given kind
- make the expression factorisable, or not

An objective where the optimum is obvious teaches nothing. If a competent
student can write down the answer without exploring, redesign it.

**Choose the constraint to control the search space.** "Digits 1–9 at most once
each" is standard and keeps the space small enough to reason about and large
enough to be non-trivial. "Digits may repeat" makes many problems trivial;
"integers from −9 to 9" opens sign reasoning, which is often where you want the
thinking to go.

**A second constraint gives you a second level for free.** "Now do it without
using 1 outside the brackets." "Now find the second-best arrangement." One
question becomes a task that occupies a fast finisher for the rest of the
period.

## Finding the answer

**Enumerate. Never reason your way to the optimum and trust it.** A plausible
arrangement is very often not the best one, and a challenge question a student
beats is worse than no challenge question — it costs the teacher's credibility
in the moment and there's no recovering the lesson.

```python
from itertools import permutations
from fractions import Fraction

best = max(
    ((r1 * 10 + r2) - (l1 * 10 + l2), (l1, l2, r1, r2))
    for l1, l2, r1, r2 in permutations(range(1, 10), 4)
)
print(best)
```

Use `Fraction` rather than floats wherever the objective is "closest to" —
float comparison will silently pick the wrong arrangement on ties.

Also record **how many arrangements achieve the optimum**. If there are several,
the teacher needs to know, because a student with a different arrangement and
the same value is right.

## Writing it up

The answer alone is close to useless to the teacher. For each problem record:

- **The optimum**, and every arrangement that reaches it
- **The insight that finds it** — the reasoning a student who solves it
  properly has used. This is what the discussion afterwards is about.
- **What a student who spots it has understood.** Being explicit about this is
  what makes the task assessable rather than just fun.
- **A common near-miss** and why it falls short — the teacher will see it and
  should be ready.

## Output

Usually **one problem**, not a set. An Open Middle problem is a Spicy question,
an extension for early finishers, or ten minutes of whole-class exploration —
not an exercise.

- **As a Spicy panel** in a lesson deck: the skeleton and the rule in the red
  box, answer in the speaker notes. Use `scripts/copy_slide.py` and the
  patterns in `templates/slide-patterns.pptx`.
- **As a full slide** for whole-class work: skeleton large and centred, rule
  above it, nothing else.
- **On a worksheet**: hand it to `worksheet-build`, which renders the boxes as
  `☐` (U+2610) in a bold run at around 34 half-points with a space either side,
  mixed inline with equation runs for the algebraic parts. Don't try to draw
  the boxes as equation content.

## Report

The skeleton, the rule, the optimum, the insight, and how long it should
occupy. If the search space turned out to be trivially small or the optimum
turned out to be obvious, say so and offer a redesign rather than shipping a
question that won't hold anyone's attention.

