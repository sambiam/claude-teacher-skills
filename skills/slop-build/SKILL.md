---
name: "slop-build"
description: "Write fluency practice for a maths skill as a sequenced set of questions — either a long SLOP run banded by structural feature, or a short minimally different sequence where consecutive questions change exactly one thing so students can predict before they calculate, run with Reflect-Expect-Check-Explain. Use when a skill has just been taught and students need repetitions that build rather than repeat: 'they need more practice on', 'write me a set of questions for', 'make a SLOP for', 'I want a sequence where only one thing changes', 'something for mini-whiteboards', 'intelligent practice', 'variation questions', or when an exercise is too short or jumps difficulty too fast. Outputs question slides for the deck (Years 7-9) or a printable set, always with answers."
---

# Building sequenced fluency practice

Two closely related formats. Both put deliberate structure into a list of
questions so that the *order* teaches something a shuffled list wouldn't.

Read `standards/practice-types.md` for the specification and the exemplars
(`SLOP-examples-for-training-1.pdf`, `Minimally-different-Examples.pdf`).

## Which format

**SLOP** — a long run, 20–60 questions, banded by structural feature. Use when
the class needs volume: the skill is new and repetitions are the point, or the
fastest students keep running out. Lives in books or on a handout.

**Minimally different sequence** — a short numbered run, 9–21 questions, where
consecutive questions differ in exactly one respect. Use when the class can
execute and now needs to *notice*. Lives on the board or on mini-whiteboards,
one at a time, with prediction between questions.

Same design principle, different length and different use in the room. If
you're unsure, the tell is whether you want the student to predict before
calculating — if yes, it's a minimally different sequence.

## Start from the atom, not the topic

Read `<unit>/<lesson>/atomisation.md`. Write practice for **one atom at a time**
before anything combines them, because a question mixing two untested atoms
produces no usable diagnostic information — a wrong answer to `3(x + 4) = 21`
could be a bracket error or an inverse-operation error and nobody can tell
which.

If the brief names two skills, each gets its own block, and the combined
questions come after both have been practised alone.

## Designing the sequence

The work is choosing **what varies and in what order**.

List the features that can change for this skill — sign, magnitude, a
coefficient of 1, number of terms, position of the unknown, integer vs
fraction, the order the information is given. Then order them so each step
changes exactly one, easiest-to-see first, hardest last.

From the decimals exemplar:

```
1.2 × 4    3.2 × 3    5.3 × 2       one decimal place, single digit
1.26 × 2   2.63 × 3   5.14 × 3      two decimal places
1.24 × 13  2.51 × 17  12.5 × 23     two-digit multiplier
```

Each band holds one feature constant while another varies, so a student who
fails band three has told you precisely which feature broke them. That
diagnostic value is what separates this from an exercise.

For a minimally different sequence the steps are tighter:

```
1. 10% of 40      4. 30% of 40      7. 30% of 8
2. 5% of 40       5. 30% of 80      8. 300% of 8
3. 15% of 40      6. 3% of 80       9. 8% of 300
```

Two design details worth the effort:

**Make the answers a pattern worth noticing.** Question 2 halving question 1,
question 3 being their sum. That's what gives students something to predict.

**Break the pattern deliberately at least once.** In the factorising exemplar,
`x² + 9` sits among factorisable expressions precisely to catch the
generalisation the student has just formed. The question they get wrong is
doing more work than the eight they got right.

## Running a minimally different sequence

The prediction is where the thinking is. Write the routine into the resource so
it survives being picked up by someone else:

**Reflect** — what changed from the last question?
**Expect** — what do you expect that to do to the answer?
**Check** — now work it out.
**Explain** — why did it do that?

A student who works each question cold gets the fluency and misses the point,
so the prompts need to be visible, not just intended.

## Rules that keep the practice honest

- **Numbers never obscure the target skill.** If the atom is expanding
  brackets, the arithmetic stays easy. Difficulty comes from the structure
  being practised, not from harder multiplication.
- **Start where every student can begin unaided** — directly parallel to the
  worked example they just saw.
- **Supply more than you think.** Running out is the common failure and it
  costs the end of the lesson. For a SLOP run, aim past the fastest student.
- **Answers always.** Practice students can't self-check quietly loses the
  feedback that makes practice work.

## Output format

**Years 7–9** — question slides for the deck, answered in books. Four to eight
per slide, band boundaries visible, answers on the following slide. Build with
`scripts/copy_slide.py` using the patterns in `templates/slide-patterns.pptx`;
`standards/good-deck.md` has the mechanics. No worksheet unless the questions
genuinely need print.

**Years 10–12** — as a slide sequence if it's being taught from, or folded into
the weekly homework by `senior-homework-build`.

**When it must be printed** — hand the question set to `worksheet-build`, which
owns page layout, working space and Word equation objects.

A minimally different sequence intended for mini-whiteboards goes one question
per slide, in the same position each time so nothing moves between slides.

## Verify

Work every answer independently rather than trusting the answer you had in mind
when writing the question, and check algebra symbolically with `sympy`.

Then read the set again for whether the questions are well posed: accidental
duplicates, ambiguous notation, a question whose answer needs something not yet
taught, a "pattern break" that's actually an error. A set with wrong answers is
worse than no set — it destroys trust in everything else the system produces.

## Report

Which atom each band practises, the feature that varies within it, roughly how
long the set takes, and where the deliberate pattern break sits — that last one
matters because the teacher needs to be ready for the question everyone gets
wrong.

