---
name: teaching-sequence
description: "Design the instructional sequence for each atom in a maths lesson — NPPPN example sequences for categoricals, continuous-conversion minimal-difference runs for transformations, initial instruction plus repeat-back for facts, backward-chained step-by-step then start-to-finish with the tick trick for routines — plus the choice of first example, the explanation script, and diagnostic questions whose distractors each name a misconception. Use whenever deciding how to teach something rather than what to teach: 'how should I teach this', 'design the sequence for', 'what examples should I use', 'I need non-examples for', 'write me some diagnostic questions', 'what should my first example be', 'how do I check they've got it'. Runs after atomise and feeds deck-build. Also use when students can do every step but still fail the whole question."
---

# Designing the teaching sequence for each atom

Atomisation says what to teach. This says how, and the two are not
interchangeable — a correctly identified categorical atom taught as a
definition plus three positive examples will still fail, because the concept it
builds has no boundary.

Read `standards/teaching-sequences.md` in the teaching folder first. It carries
the specification, the worked references and the house conventions, and it
overrides anything here.

## Input

An atomisation — `<unit>/<lesson>/atomisation.md`, or run `atomise` first. You
need each atom's **type** and its **decision**, because the type picks the
sequence and the decision picks the depth. Atoms marked *Assume* get nothing;
*Check* gets a diagnostic question; *Teach* gets a full sequence.

If you're handed a topic with no atomisation, atomise it first rather than
guessing at the atom types. A transformation taught as a categorical is a
wasted lesson and the mistake is invisible until you're in the room.

## The first decision: which example comes first

Make this before designing anything, for every atom, because it does more
damage than any other choice when it goes wrong. The first example a student
meets becomes their prototype of the whole idea, so a special case produces a
permanently special concept.

**Do not start with a degenerate case.** 2/3 not 2/2. (2x + 5)(10x + 3) not
(x + 5)(x + 1). 25% not 10%. A cuboid not a cube. y = 5x³ not y = x².

Check your chosen first example against the three failure modes:

1. Could a student get this right by a shortcut that won't generalise?
2. Does anything about the method become invisible because a coefficient is 1
   or a value is special?
3. Will I need a different method for the harder cases?

Any yes means pick a different first example. Special cases come later, in
expansion, where they teach the edge rather than define the centre.

## Categorical atoms → NPPPN

Sequence: Negative, Positive, Positive, Positive, Negative. Four to eight
items, five is a good default, each on its own slide, students respond to every
one.

Design it by deciding what the concept **turns on**, then:

- **Item 1 → 2 differ in exactly that one feature** (difference principle). The
  student sees the boundary before they see the category.
- **Items 2, 3, 4 are all positive and differ as much as possible** (sameness
  principle) — different orientations, magnitudes, representations, contexts —
  so the label doesn't attach to an irrelevant feature.
- **Item 4 → 5 differ minimally again**, back across the boundary in a
  different respect from item 1 → 2.
- **Same wording throughout** (wording principle). "Is this a bearing?" five
  times. Rephrasing adds a second thing to work out.

**Selecting the negatives is the whole job.** A good negative is one a
reasonable student would call positive — take them from the misconceptions in
the atomisation. A negative that's obviously not the thing teaches nothing.

Write, for each item: the item, positive or negative, and **which principle it
serves and why**. That last part goes in the speaker notes; it's what lets the
teacher (or the next person to edit the deck) keep the sequence intact.

Then design the **test**: four to six fresh, untaught items in random order,
positives and negatives mixed, same wording. Students who pass the taught five
and fail these memorised a sequence rather than learning a concept, and you
want to find that out now.

**The five-item default is not invariant — it's sized to how hard the
distinction is to hold onto, not to how hard it was to notice.** Those are
different properties. An atom can be genuinely invisible at expert fluency —
which is exactly why atomise flagged it as categorical in the first place —
and still be easy for the class to apply correctly once it's been pointed out
once. Boundary-vs-internal-line, an obvious visual contrast, anything with a
one-line decision rule: these are hard to *see* unprompted but not hard to
*retain*, and running the full five-item NPPPN plus a separate test on one of
these spends slides the harder atoms further down the chain actually need. If
the class profile or the misconception evidence says this is that kind of
atom, cut the taught sequence to two or three items — still N then P, still
the difference principle on the first pair — and put the freed slides toward
the atom's harder downstream steps instead. Either way, write the reasoning in
the notes: a short sequence that looks like an oversight is worse than a short
sequence that says why it's short.

On slides: item alone and large, decision rule visible for the first two or
three then removed, thumbs up/down or finger vote. Pattern `NPPPN CATEGORICAL`
in `templates/slide-patterns.pptx`.

## Transformation atoms → continuous conversion

A run of near-identical presentations where each turns into the next and only
one thing changes.

Design it by listing the features that can vary — sign, coefficient of 1,
number of terms, position of the unknown, fraction vs integer — then ordering
them so each step changes exactly one, hardest-to-see change last:

```
(3x + 2)(4x − 5) ≡ 3x(4x − 5) + 2(4x − 5)
(3x − 2)(4x − 5) ≡ 3x(4x − 5) − 2(4x − 5)      sign
(3x − 1)(4x − 5) ≡ 3x(4x − 5) − (4x − 5)       coefficient 1 disappears
```

The third line is where students break and it is one character from the second.
That's the design working.

**Keep everything else still.** Same position on the slide, same size, same
layout. If the expression shifts between slides the eye tracks the movement
instead of the mathematics. Build these by cloning one slide and editing only
the changed characters.

**Specify near-silence.** Write the narration as: make the change, wait two
seconds, then point and say the result — *"because 2x plus 5x is 7x"*.
Explanation delivered before students have seen the change competes with it.

## Fact atoms

Three short moves:

- **State it once**, plainly, in the notation the textbook and the assessment
  use.
- **Repeat back** — the class says it, then an individual, then in a form that
  needs the fact rather than the words: "Simultaneous means…?" and "What word
  means together?"
- **Expansion** — for a generalisable fact, cases where it applies and cases
  where it doesn't. For a specific fact, put it in the next three starters
  rather than drilling it now.

Then specify where it lives for the rest of the lesson: a **reference panel**
down the side of the slide. A fact still being consolidated shouldn't also be a
memory task while students learn the routine that uses it.

## Cognitive routine atoms → step by step, then start to finish

**Step by step (I do).** One worked example revealed in the order it's written.
Specify the reveal order explicitly — S1, S2, S3 … — because it is often not
left to right, and a solution that arrives complete gives students nothing to
follow. Beside it, list the atoms this example used with their types, marking
the assumed ones.

**Start to finish (You do).** A structurally identical problem, students alone,
whole thing. This comes before any second worked example — two worked examples
back to back with no attempt between them tell you nothing about who is
following.

**Tick trick.** Specify the components to be ticked. Marking components rather
than the final answer means a student who slipped one digit still scores full
marks for the method, and one pass across the room tells you which component
failed for the whole class.

**Four components for Years 7–9. Six or seven is the ceiling for Years 10–12.**
Ten is Year 11 exam-marking granularity, and on a junior lesson it starts
awarding marks for bookkeeping.

**Mark the process, not the paperwork.** The components should be the things
you actually want to see in a student's book:

- Showed the inverse operation used, every line
- Did it to BOTH sides, every line
- One step per line, working downwards
- Answer written as `x = …`

Not "wrote out the backward chain", "underlined the answer", or anything else
that is a scaffold for the method rather than the method. A scaffold earns its
place by being useful, not by being marked.

The tick list is rendered as a small bordered box with blank checkboxes on the
**same slide** as the You do, not buried in the speaker notes — students tick
their own before you collect anything.

**Backward chaining** for long routines — teach the last link first, then the
last two, and so on, so the student always finishes the problem and every
attempt ends in a completed answer.

**Narration** once assembled: the chain said aloud in order — *"common
coefficient? no. multiply. expand. add or subtract? subtract. solve.
substitute."* — by you, then by them. The order of the chain is itself
something to be remembered.

## Explanation script

Where the atom needs words, write them in one of the two forms from
`Explanation-training.pdf`, both laid out as model left, words right:

- **Written explanation** — two or three sentences saying *why*, referring to
  what is on the board.
- **Check for listening** — the explanation as numbered statements you'll say,
  with a mark against the ones students will be asked to repeat back. This
  turns explanation from something students hear into something you can verify
  they heard.

Keep it short. The examples are doing the teaching; every sentence competes.

## Checks for understanding

For each atom marked *Check*, and at the testing stage of each taught atom,
write a diagnostic question:

- Answerable in **under ten seconds** — one atom, not a routine
- **One** unambiguously correct answer
- Three or four options where **each distractor is a specific named
  misconception** taken from the atomisation, with what it diagnoses recorded
  alongside
- Minimum reading

The distractors are the entire value. "£4 and 97p" as an answer to
"£3 and 64p + £1 and 3p" tells you the student read 3p as 30p; a distractor
that's just a plausible number tells you nothing and wastes the question.

Then choose the **response mode** by what you need to see: mini-whiteboards for
anything with working (Write it → Hover it → Chin it → Wipe it → Park it),
finger vote for a small option set, thumbs up/down for categorical yes/no,
repeat back for facts, turn and talk with a specific question when you want
reasoning. A finger vote on a question needing working tells you nothing.

**Size a check at one standard question plus one Spicy, and specify two
backups.** Not a set of five. Five questions means the fastest student is done
in forty seconds and the slowest in four minutes, and you spend the difference
losing the room; one question puts everyone on the same beat. The backups exist
for the case where the class gets the first one wrong — `deck-build` hides them
behind click animations so they cost nothing when they aren't needed. Give the
backups no letters: a lettered list reads as a set to be completed, which is
the opposite of a check.

This applies to checks inside the teaching sequence. The opening retrieval
starter and the practice sets are different animals and should be full.

## Fading

Specify how support comes away across the lesson: full worked example →
partially completed with the load-bearing steps blank → problem with a prompt →
bare problem. Say which slide each transition happens on.

**Write the completion problem out in full. Do not just name the stage.** A
fading schedule in a table is not a fading schedule — it is an intention, and
the deck ends up jumping from a complete worked example straight to a bare
problem with nothing in between. Produce the actual middle rung:

```
(2x + 6)/4 - 1 = 3
(2x + 6)/4 = ____        add 1 to both sides
2x + 6 = ____            _____________________
____ = 10                take 6 from both sides
x = ____                 _____________________
```

Blank the **load-bearing** lines — the both-sides steps — and leave the
arithmetic visible. Alternate which column is blank down the page so students
have to supply both the operation and the result, not one mechanically.

The decision rule beside the NPPPN items is gone by the fourth. The reference
panel stays longer, because it holds a fact rather than a method.

## Vary the method, not just the questions

A sequence built only from *show an example, ask a question* teaches one way of
thinking however good the examples are. Choose deliberately from the list
below and record which you used, so a unit doesn't run six lessons of identical
shape. These are additions to the sequences above, not replacements.

**Reflect–Expect–Check–Explain, on every minimal-difference run.** This is the
protocol the runs exist for, and a run without it is just five questions.
Before students calculate item *n*, they say what changed and predict what it
does: *"we changed +20 to −20 — will the answer be bigger or smaller than 8?"*
Reflect on the change, expect the effect, check by solving, explain the gap.
The students who predict wrongly and then see why are the ones who learn the
relationship; the ones who just solve have done arithmetic. Write the predict
prompt into the narration for each item — it costs no slides.

**Self-explanation prompts on worked examples.** Before the You do, ask *why*
a specific line was done, not what it was: *"why did we multiply the whole
right-hand side and not just the top?"* Students who explain a worked example
to themselves transfer better than students who study one. One prompt per
worked example is enough.

**Peer instruction on diagnostic MCQs.** Vote silently → *"turn to the person
next to you and convince them"* → revote. Use it when the first vote splits.
The second vote is substantially better, and more usefully for you, the
argument you overhear is the misconception in the students' own words — which
is what you need to reteach it.

**Silent teacher.** Work an example on the board without speaking. Then:
*"nobody speak — now talk me through what I did, line one."* It forces
attention onto the writing rather than the voice, and it converts your
explanation into their explanation, which is the version you can actually
assess.

**Goal-free start.** Put a hard question up and ask *"write down everything you
can work out about this"* before naming any method. Strips the means–ends load
off a problem that would otherwise be attacked by flailing at a remembered
procedure. Good for the first slide of a routine.

**Say it again, better.** Take a student's rough verbal rule and have them
restate it more precisely, twice. The fastest way to find out whether a rule
has landed as a rule or as a noise they repeat.

**Compare two correct methods.** Show the same question solved two legitimate
ways and ask which is better and why. Distinct from spot-the-error: the work is
evaluating, not detecting.

**Deliberate error / spot the mistake.** Show wrong working and have them find
and name the error. Strongest when the error is one you have just seen in their
books — and strongest of all when the wrong answer *looks* confirmed.

## Output

Write `<unit>/<lesson>/teaching-sequence.md`, one section per atom:

```markdown
## Atom N: <capability>  [Type] [Teach|Check]

First example: <the example> — chosen because <reason>
Sequence: <the items, in order, each with its role and principle>
Narration: <what to say, and where to stay silent>
Check: <diagnostic question, options, what each distractor diagnoses>
Response mode: <MWB | finger vote | thumbs | repeat back | turn and talk>
Test items: <fresh untaught items for the testing stage>
Completion problem: <the faded middle rung, written out in full>
Slide pattern: <name from slide-patterns.pptx — must match the atom type>
Extra technique: <REC-E prompt / self-explanation / peer instruction / silent
                  teacher / goal-free / compare methods / deliberate error>
Misconception targeted: <from the atomisation>
```

**Every answer in the file must be verified with a solver, not by eye,** before
it reaches a slide. Sequences get edited — a coefficient changes and the answer
three lines down quietly stops being true. Write the whole set out as
assertions and run them.

Then report in chat: the atoms covered, roughly how long the teaching phase
runs, which extra techniques you used and why, and any atom you couldn't design
a sequence for — which usually means it was mistyped, and saying so is more
useful than inventing a sequence.

Flag anything the teacher has to rule on rather than deciding it silently. The
one that recurs: an answer that isn't a whole number when the class has never
been told what form to give. Either the sequence teaches the convention or the
numbers change — but it is the teacher's call, not yours.

## Next

`deck-build` renders this to slides. `practice-select` chooses what students do
afterwards. `differentiation-pack` builds the guided notes that shadow it.

