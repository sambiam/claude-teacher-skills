---
name: explanation-script
description: "Write the words a teacher says while working an example at the board for a cognitive routine — the assembly step where the atoms get put together. Produces a numbered narration script built on Engelmann's faultless communication and Barton's I do: a fixed vocabulary with banned synonyms, an explicit reveal order, subgoal labels, repeat-back checks, one true justification sentence, a backward chain, a tick list, and a table of every wrong answer the example can produce. Use whenever the question is what to say rather than what to show — 'write me a script for', 'what do I actually say here', 'script the worked example', 'the narration for the I do', 'economy of language', 'logically faultless', 'make this explanation tighter', 'my explanation always loses them', 'this bit is where they switch off' — and whenever a deck has a worked example with nothing for the teacher to say. Also audits an existing explanation for ambiguity. Runs after atomise and teaching-sequence; feeds deck-build."
---

# Scripting the explanation for a cognitive routine

A cognitive routine is the atom where everything gets put together — the
student meets the whole question and has to run the chain. The individual atoms
below it rarely need a script; they need examples. This one does, because the
teacher is talking while writing while the class is deciding what to attend to,
and every unnecessary word is a competing demand.

The job is not to explain the method. The job is to make the method the only
thing a reasonable student could conclude from what they saw. Engelmann's test:
**a communication is faultless when only one interpretation survives the
examples given.** Most explanations fail not by being wrong but by being
compatible with two or three rules, one of which is the shortcut.

Read `standards/explanation-scripts.md` in the teaching folder first if it
exists — it carries house conventions and overrides anything here. Everything
below works offline; do not go searching the web for pedagogy mid-task.
`references/evidence.md` holds the sources and what each one licenses, for when
you need to justify a design choice to a faculty.

## Input

An atomisation (`<unit>/<lesson>/atomisation.md`) and, ideally, a teaching
sequence. You need three things and should ask for whichever is missing rather
than guessing:

- The **terminal question**, worded as students meet it
- Which atoms are **Assume/Check** (they get pointed at, not taught) and which
  are **Teach**
- The **year level and period length**, because they set the ceiling on
  statement count and tick components

If handed only a topic, atomise first. A script written against a guessed chain
is a script for the wrong lesson.

---

## Step 1 — Interrogate the worked example for degeneracy

Do this before writing a single word, because a degenerate example makes a
faultless script impossible: if the decision doesn't change the answer, no
wording can teach the decision.

`teaching-sequence` already rules out the obvious degenerate first examples
(2/2, a cube, 10%, coefficient 1). This step catches the ones that survive that
filter — where the example looks general but the routine's decisions turn out
to be free.

Run all four checks and write down the result of each:

**1. Symmetry.** Permute the roles of the given quantities and recompute. If any
permutation returns the correct answer, that decision is unassessable in this
example.

> A rectangular prism has three faces that can each serve as the cross-section
> and all three give the correct volume — which is why it is the wrong first
> example for *volume of a prism*. But a **right-angled** triangular prism
> labelled with its two legs and its depth is degenerate in exactly the same
> way: V = ½bhd is a symmetric product, so multiply-all-three-and-halve wins
> without ever identifying a cross-section. Choose a non-right triangle.

**2. Redundancy.** Is every number on the page used in the correct solution? If
so, "use all the numbers" is a winning strategy and the selection decision is
invisible. Add one quantity that is legitimate to show and correctly *not* used
— a sloping side, a diameter beside a radius, a distractor angle.

**3. Collision.** Do any two values coincide — two givens, a given and an
intermediate, an intermediate and the answer? If the cross-section's area is 6
and the depth is 6, `6 × 6` is unreadable on the board and unmarkable in a
book. Change the numbers.

**4. Shortcut.** Is there a method that gets this one right and won't
generalise? Halving instead of the formula, spotting a familiar triple,
counting rather than calculating.

Any failure means new numbers or a new diagram — not a cleverer sentence. Say
in the output which check forced which change; the teacher needs to know why
the obvious numbers were rejected, or they will put them back.

---

## Step 2 — Fix the vocabulary before writing

Engelmann's **wording principle**: identical wording for the identical idea,
every time. Rephrasing is not variety, it is a second thing to work out, and
students generalise on the basis of what stayed the same — including things you
did not intend to teach.

Produce a two-column table: the word you will use, and the synonyms banned for
the rest of the unit.

| Say | Never say |
|---|---|
| cross-section | face, end, base *(of the solid)*, side |
| depth | length, height, long side, the one going back |

Two rules govern the choice:

- **One name per object, and it never changes** — not in the script, not in the
  practice, not in your marking.
- **A word already doing a job cannot be reused.** If *height* means the
  triangle's perpendicular height, then the prism's third dimension is never
  called height. A word with two referents on one diagram cannot be recovered
  by the student, and it is the single most common way a good explanation
  fails.

Pick the term the assessment and textbook use. Where they disagree, pick one,
say so in the flags, and hold it.

---

## Step 3 — Board layout and reveal order

Specify the finished board exactly, then the order the lines appear in. Two
reasons: the order is frequently not left-to-right or top-to-bottom, and a
solution that arrives complete gives students nothing to follow.

Number the reveals `S1, S2, S3 …`, including the non-writing moves — tracing an
edge, marking a right angle, labelling a face.

**Break the formula across lines at the subgoals.** A routine written as one
unbroken expression hides its own structure, invites the
multiply-everything shortcut, and leaves the intermediate unwritten — so there
is nothing to tick and no way to tell which half failed. Two or three short
blocks:

```
A = ½ × b × h          ← subgoal 1: area of the cross-section
A = ½ × 8 × 5
A = 20 cm²

V = A × d              ← subgoal 2: multiply by the depth
V = 20 × 12
V = 240 cm³
```

**Name at most three subgoals, by function.** Subgoal labels — naming a *group*
of steps by what it achieves — improve transfer and show up in students' own
explanations afterwards; a five-step numbered list does not, because it names
actions rather than purposes. "Area of the cross-section" is a subgoal.
"Multiply by the depth" is a subgoal. "Write the units" is a step.

Fix the position of everything on the board and keep it fixed across the
worked example, the You do and the practice. If a line moves between examples,
the eye tracks the movement instead of the mathematics.

---

## Step 4 — Write the script

Numbered statements, not prose. Prose invites reading aloud; numbers force each
sentence to justify itself.

Mark with ▶ the statements the class says back before you continue — this is
what turns explanation from something students hear into something you can
verify they heard. Two or three per script, on the load-bearing ideas.

**Budget: twelve to fifteen statements for a whole worked example.** Barton's
guide is roughly thirty seconds of teacher talk before attention wanes. A
routine that genuinely needs thirty statements is two routines, and saying so
is more useful than writing the thirty.

Four rules do most of the work:

**Every statement is a mathematical move or a decision.** Nothing that is stage
direction. Cut "what we're going to do now is", "let's have a look at", "as you
can see". They cost attention and teach nothing.

**Cut vagueness, mazes and discontinuity.** Vagueness is "kind of", "pretty
much", "sort of". Mazes are "um", "so", "okay", "right", "now then".
Discontinuity is any sentence that leaves the example — a reminiscence, an
aside about the test, a tangent about where this comes up later. Write the
script, then read it aloud and cut again; these words appear in speech, not on
paper, which is exactly why the script has to be written.

**Every step's trigger must be visible.** The student has to be able to see
*what in the diagram* caused the step, or they learn a sequence rather than a
method. Point and name the feature — *"five is the one that meets the base at a
right angle"* — rather than announcing the action — *"we identify the height"*.
If you cannot point at the trigger, the atom underneath is missing and belongs
in the atomisation, not in a sentence.

**Say the distractor out loud, once, negatively.** The redundant quantity from
Step 1 earns its place only if a statement names it as not-the-thing: *"six is
not a height; it does not meet the base at a right angle."* Without that
statement the distractor is just clutter.

### The trust sentence

Exactly one statement in the script says **why the routine works** — the thing
students would otherwise have to take on trust. It costs one sentence and it is
the difference between a rule to be remembered and a relationship that can be
rebuilt.

Three conditions:

- **One sentence.** A paragraph of justification competes with the example. If
  the reason needs a paragraph, it is a separate lesson (`lesson-rationale`).
- **About the objects on the board.** Not an analogy from elsewhere.
- **True.** This is the one that bites. "Twenty square centimetres of
  cross-section, one centimetre thick, is twenty cubic centimetres" is true;
  "twenty cubes" is false for a triangular cross-section, and the class
  contains someone who will check. A convenient falsehood is not a faultless
  communication — it is a misconception you installed deliberately.

If you cannot write a true one-sentence justification, say so explicitly in the
flags. It means the routine is being taught as a rule, and that is a decision
the teacher should make knowingly rather than discover in a year's time.

### Silent teacher variant

Specify it as well as the spoken script, because it is usually the better first
pass: write S1 through Sn in silence with gestures, then *"nobody speak — talk
me through what I did, line one."* Writing and talking while students watch and
listen is a four-way load; splitting it converts your explanation into their
explanation, which is the version you can assess. Then run the numbered
statements as the confirming pass.

Add **one self-explanation prompt** before the You do — *why* a line was done,
not what: *"why is the 6 cm not used anywhere?"* One is enough; two turn a
worked example into a discussion.

---

## Step 5 — Backward chain

Three rungs, each ending in an answer of the terminal type, so every student
attempt finishes a problem rather than stalling in the middle.

| Rung | Given | Asks |
|---|---|---|
| 1 | The intermediate handed over ("the cross-section has area 20 cm², depth 12 cm") | The final answer |
| 2 | The intermediate's inputs, no full diagram | The final answer |
| 3 | The full prompt as students meet it | The final answer |

Rung 1 exists to fix the answer form and units with no diagram competing for
attention — it is where "cm³ not cm²" gets settled cheaply. Order the rungs by
which atom is hardest, not by which comes first in the solution: putting the
hardest atom last means meeting it under time pressure.

---

## Step 6 — You do, and the tick list

**Structurally identical to the worked example.** Same orientation, same
layout, new numbers. Variation belongs in the next item, not this one — a
failure on a problem that changed two things at once tells you nothing about
which one broke.

Run the four checks from Step 1 on it too. A You do that is degenerate lets
students pass without the decision.

**Tick list: four components for Years 7–9, six or seven at most for 10–12.**
Written in the student's words, at the length a Year 8 will actually read while
marking, on the same slide as the problem. Mark the process, not the paperwork
— the components are the things you want to see in their book, and one of them
may be the answer:

- ☐ Wrote the area of the cross-section on its own line
- ☐ Used the height that meets the base at a right angle
- ☐ Multiplied the area by the depth
- ☐ Answer in cm³

Marking components rather than the final answer means a student who slipped a
digit still scores the method, and one pass across the room tells you which
component failed for the whole class.

---

## Step 7 — The wrong-answer table

Compute every plausible error the example can produce. Do this with a solver,
not by eye — a changed number quietly falsifies the row three lines down.

For each: what the student did, the number it produces, and how confident you
are. Then check two things the aggregate hides:

- **Do any two errors produce the same number?** If so the number cannot
  diagnose, and the practice must separate those atoms.
- **Does any error produce the *correct* answer?** This is the one worth
  flagging loudest. Where the routine is a symmetric product, swapping two
  roles gives the right answer every time, for every choice of numbers — it is
  a property of the mathematics, not of the numbers, so no reworking fixes it.
  The consequence is a marking instruction: **working must be marked, not
  answers**, and the tick list is how that gets done.

Build the diagnostic check from this table, not from invented distractors. Each
option is a named misconception with the number it produces; an option that is
merely a plausible-looking number wastes the question. A check on a full
routine runs on mini-whiteboards for a minute or two rather than as a
ten-second finger vote — you need to see the lines, not the number — and that
deviation is worth stating so it does not read as an oversight.

---

## Step 8 — Flags

Report in chat, separately from the script, anything the teacher must rule on
or would not otherwise notice. These are usually the most valuable part of the
output. The ones that recur:

- **Errors on the existing slides**, named by file and slide number — a wrong
  unit on the I do slide is copied into thirty books.
- **Vocabulary conflicts** between deck, textbook and assessment.
- **Answers that aren't whole numbers** when the class has never been told what
  form to give. The teacher's call: teach the convention, or change the numbers.
- **Errors that produce the correct answer** (Step 7).
- **A routine with no true one-sentence justification** (Step 4).
- **Anything you decided on the teacher's behalf** because the atomisation or a
  class profile was missing.

---

## Output

Write `<unit>/<lesson>/explanation-script.md` when a lesson folder exists;
otherwise deliver it in chat. Either way the flags go in chat.

```markdown
# Explanation script: <routine> — <class>, <period length>

**Terminal question:** <as students meet it>
**Atoms assembled:** <list, with Assume/Check/Teach>

## Worked example
<the numbers and diagram, plus which degeneracy check forced which choice>

## Vocabulary
<say / never say table>

## Board layout
<the finished board, exactly>
**Reveal order:** S1 … Sn

## Script
<numbered statements, ▶ marking repeat-backs>
**Trust sentence:** <which number it is, and why it is true>
**Silent teacher:** <what to write silently, and the prompt that follows>
**Self-explanation prompt:** <one question>

## Backward chain
<three rungs>

## You do
<the problem, structurally identical>
<tick list, four components>

## Wrong answers
<table: what they did | number | confidence>
<any collisions or correct-by-accident errors called out>

## Diagnostic
<one question, options, what each distractor diagnoses, response mode>
```

Then report: the routine scripted, the statement count, which degeneracy checks
failed and what you changed, and the flags.

## Next

`deck-build` renders this to slides and speaker notes. `slop-build` writes the
practice that follows. If Step 1 keeps failing on every example you try, the
atom is probably mistyped — go back to `atomise`.
