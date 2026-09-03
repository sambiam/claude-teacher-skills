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
  starter pattern already has the quadrant structure and dividers.
- **On paper** — A4 portrait, stem centred, four questions around it, working
  space in each quadrant. Hand to `worksheet-build` for the layout mechanics.

Answers go in the speaker notes or on a separate teacher sheet, never on the
student-facing page.

## Verify

Work all four independently and check symbolically with `sympy` where the
algebra is non-trivial. Then check the property the set depends on: **read the
four questions as a student would and confirm the surface really is identical**
— same numbers, same units, same diagram, no extra information smuggled into
one of them. That's the failure mode a solution check won't catch.

## Report

The surface, the four deep structures, which topics they reach back to, and the
misconception the set is designed to expose. If you couldn't find four genuine
deep structures for the surface, say so and offer three plus a suggestion —
a padded fourth question defeats the whole design.

