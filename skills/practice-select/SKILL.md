---
name: practice-select
description: "Choose which kind of practice a maths lesson needs — SLOP fluency, minimally different sequences, Open Middle, SSDD, non-routine problems, a weekly senior homework sheet, or a printed worksheet — then dispatch to the skill that builds it. Use whenever practice is needed but the type isn't specified: 'what practice should I use for', 'the kids need something after this lesson', 'give them something to consolidate', 'what should they do for the rest of the period', 'I need a task for', 'something for the starter', or when a lesson has teaching but nothing for students to do. Also use when the same exercise type has been used repeatedly and the class needs a different kind of thinking. Decides and routes; does not write the questions itself."
---

# Choosing the practice

The question this answers: **given what this class has just been taught and
where they actually are, what kind of thinking should the next twenty minutes
demand?**

Variety is not the goal — matching is. Open Middle is a wonderful task and it
is useless to a student who cannot yet execute the procedure, because they will
spend the lesson stuck at the first step and conclude they are bad at maths.

Read `standards/practice-types.md` — it holds the catalogue, the exemplars, and
the design rules for each type. This skill decides; the generator skills build.

## Work out where the class is

Three things determine the answer, and guessing at any of them produces the
wrong task.

**What was taught, atom by atom.** Read `<unit>/<lesson>/atomisation.md` if it
exists; otherwise read the deck. You need the individual atoms, not the topic,
because practice is per-atom until each is secure.

**Whether execution is fluent yet.** Just taught means not fluent, whatever the
lesson felt like. If there's evidence — exit tickets, the last test, ink
annotations on the deck showing where the class actually got to — use it.
`ink-progress` reads the annotations.

**Year level and time.** From `classes/<class>/profile.md` and
`standards/class-defaults.md`. This decides the *format* before it decides the
type: Years 7–9 answer in books off the slides, Years 10–12 get a textbook or
Padlet assignment plus a weekly homework sheet.

## Route

| Where they are | Type | Skill |
|---|---|---|
| Atom just taught, needs fluency | SLOP | `slop-build` |
| Can execute, should notice the structure | Minimally different sequence | `slop-build` |
| Fluent, ready to reason about structure | Open Middle | `open-middle-build` |
| Can execute but can't tell which method applies | SSDD | `ssdd-build` |
| Everything secure, needs real problem solving | Non-routine | `non-routine-build` |
| Senior class, end of the week | Weekly homework | `senior-homework-build` |
| Needs to be printed — diagrams, card sort, page layout | Mild/Medium/Spicy worksheet | `worksheet-build` |
| Needs to **think**, not practise — a hook, a starter with an argument in it, a deepening task, an SA disposition target | A designed task | `sa-task-design` |

Two rules that override the table:

**Practice is not the only answer.** Sometimes what the next twenty minutes
needs is not more repetitions of anything — it is a task that makes the class
decide something. That is `sa-task-design`, and it is the right call when the
lesson has fluency but no thinking, when a new topic needs a hook before the
explicit teaching, or when the SA Curriculum's **BE** ring — resilient,
resourceful, reflective — is what the lesson is short of. Those dispositions do
not develop from practice of any type, however well chosen, because none of
these practice types has a survivable stuck point in it.

**Fluency before structure.** Earn Open Middle and SSDD with SLOP first.

**One atom at a time before any combination.** A question mixing two untested
atoms yields no usable information — a wrong answer to `3(x + 4) = 21` could be
a bracket error or an inverse-operation error, and you cannot tell which. Give
each named atom its own practice before anything combines them.

## Usually more than one

A period rarely wants a single type. A common and good shape for a junior
lesson:

- Minimally different sequence on mini-whiteboards during teaching, 5 minutes
- SLOP block in books on the taught atom, 15 minutes
- One Open Middle as the Spicy for early finishers
- SSDD set as next lesson's starter, interleaving this with older topics

Say which pieces you're recommending, roughly how long each runs, and where in
the lesson it sits — the sequencing is most of the value.

## Check what already exists first

Practice hides in the deck, in `questions/`, in the textbook exercise named in
the unit outline, and in worksheets from previous years. Run `practice-audit`
before building anything.

**Prefer supplementing over rebuilding.** If a textbook exercise covers two of
three atoms well, six extra questions on the third is a better answer than a
new worksheet: less work, and the class stays on a resource they already know
how to navigate.

## Don't build a worksheet by reflex

For Years 7–9 the default is questions in the deck, answered in books. A
printed worksheet has to earn itself — printed diagrams, a card sort, a layout
books can't carry. Paper is finite, and getting laptops out to reach a PDF
costs five minutes and half the room's attention.

For Years 10–12 the default is an assignment from the teacher's usual source
with the reference on the last teaching slide, plus one weekly homework sheet
across the whole week's skills rather than a sheet per lesson.

## Output

Report before dispatching:

```
## Practice plan: <lesson> (<class>, Year <N>)
Atoms taught: <list, with fluency judgement for each>
Already available: <what exists and what it covers>

Recommended:
1. <type> on <atom> — <N> min, <where in the lesson> — <why this type>
2. ...

Building: <which skills, in order>
Not building: <what you're deliberately leaving to the textbook or the deck>
```

Then invoke the generator skills. If the choice is genuinely finely balanced —
usually between more fluency and moving to structure — say so and ask, rather
than picking silently. That judgement belongs to whoever was in the room.

