---
name: lesson-rationale
description: "Build the slides that answer 'why are we learning this' for a mathematical idea — a prior/present/future knowledge flow diagram, hinterland knowledge (the stories and history behind the procedure), genuine real-world contexts, and a headache task that makes students feel the need for the idea before it is taught. Use whenever a lesson needs purpose, motivation, or a hook — including 'why do students need this', 'how do I introduce', 'the kids will ask when they'll ever use this', 'add some context to this lesson', 'where does this fit in the sequence', 'give me a headache for', or 'this deck goes straight into the procedure'. Also use when a new topic starts and its first lesson has no motivation slides."
---

# Building the rationale slides for a mathematical idea

Students who cannot see why an idea exists learn it as an arbitrary ritual.
This skill produces four things that fix that, and inserts them into the
lesson deck as slides — not as a document the teacher reads and forgets.

The four are deliberately different in kind. **Connection** places the idea in
the student's own learning history. **Hinterland** gives it a human origin.
**Real-world context** shows where it lives now. **The headache** makes the
student want it before it arrives. A lesson that has only one of these still
feels arbitrary.

## Read the folder first

Work from the lesson and unit folder, not from what you already know about
the topic:

- the **unit outline** and any scope-and-sequence — this is where the prior
  and future nodes of the flow diagram must come from
- `classes/<class>/profile.md` — year level, period length, cohort
- `standards/explicit-instruction.md` — slide conventions
- `templates/` — the branded template
- the existing lesson deck, if there is one

The prior/future ideas have to be things *this* cohort has actually met or
will actually meet, in this curriculum, in roughly this order. A diagram built
from general mathematical knowledge rather than the school's sequence will
name topics the class has never seen, and students will read it as evidence
that they have missed something.

**If the deck carries ink annotations, work on a copy** — see the
ink-progress skill. If no deck exists yet, say so and build the rationale
slides as a standalone deck for deck-build to absorb, rather than guessing at
the lesson structure.

## 1. The prior / present / future flow diagram

One slide, built from shapes on the template — three columns, left to right:
what feeds in, the new idea, what it feeds.

- **Name nodes as capabilities, not topic headings.** "Find the area of a
  rectangle" rather than "Area". A student can check themselves against a
  capability.
- **Three to five nodes per column.** More than that and the slide becomes a
  curriculum map, which is a teacher artefact, not a student one.
- **Centre node visually dominant** — larger, template accent fill, the other
  two columns in a muted fill.
- **Arrows carry the dependency**, left to right, and only where the
  dependency is real. If a prior node isn't genuinely used in the new idea,
  cut it. Crossing arrows are fine and often honest; a diagram where every
  node connects to every other is not.
- **Prior nodes must be recoverable.** Each one should be something you could
  put a quick question on in the prior-knowledge check. If it can't be
  checked, it isn't really prerequisite.
- **Future nodes should be recognisable and desirable** — ideally at least one
  the class knows is coming and cares about (a senior topic, something in an
  exam, something with obvious power).

Keep it one slide. Where an idea has an unusually rich downstream, add a
second future column rather than a second slide, so the whole story stays in
one eyeful.

## 2. Hinterland knowledge

The stories, people and problems behind the procedure — how it was first
found, what it was for, how it changed, what it cost someone.

What makes hinterland work:

- **A problem someone actually had.** Hinterland lands when it starts with a
  person stuck on something, not with a date and a name.
- **Tension or surprise.** A result that was resisted, a wrong answer held for
  centuries, a rival claim, a method that came from somewhere unrelated.
- **Connection back to the procedure on the board.** If the story doesn't
  change how a student reads the notation or the method, it's decoration.
- **Two or three minutes.** Written as speaker notes for the teacher to tell,
  with the slide carrying only an image, a name, or a single question.

Mathematical history is thick with apocrypha — Gauss and the schoolroom sum,
Pythagoras and the drowned student, Newton's apple, Archimedes in the bath.
These are often worth telling, and telling them as fact quietly teaches
students that history is a set of anecdotes. Mark each item as
**established**, **disputed**, or **legend**, and where something is legend,
give the teacher the one-line truth alongside it. Non-European origins are
routinely dropped from the standard telling — where the idea has a history in
Indian, Chinese, Islamic or other mathematics that predates the name it now
carries, say so, because the standard version is not neutral.

Prefer specificity over sweep: one well-sourced episode beats a survey from
Babylon to Euler.

## 3. Real-life contexts

Only genuine ones. The test: would someone in that field, doing that job,
actually perform this calculation? If the honest answer is that a machine does
it, or nobody does it, don't offer it — students detect invented relevance
immediately and it makes every future claim of usefulness suspect.

Good contexts are usually one of:

- **A job where it is done, named specifically** — not "engineers use
  trigonometry" but the particular calculation a surveyor makes and why.
- **A thing the student uses that would not work without it** — where the idea
  is inside something familiar, and you can show what breaks without it.
- **A decision the student themselves will make** — money, time, risk,
  measurement in their own life. Be honest about scale; not every idea has one
  of these and pretending otherwise is worse than skipping it.

Some ideas have no compelling everyday application, and the honest answer is
that they exist because they make later mathematics possible, or because they
are interesting. Say that plainly rather than manufacturing a context. Where
the real answer is "this is a stepping stone", the flow diagram is doing the
work, not this section.

## 4. The headache

Before the aspirin, the headache. Students spend a few minutes doing something
the hard way so that the new idea arrives as relief rather than as another
thing to memorise.

The pattern to follow:

- Repeated addition of 693, eight times over, before long multiplication
- Copying the mass of the Earth out in full before standard form
- Winning repeatedly at a rigged game before probability

What each of those has in common, and what a new headache needs:

- **Every student can do it.** The task uses only what they already have. A
  headache that requires the new idea is just a hard question, and produces
  helplessness rather than appetite.
- **It genuinely hurts.** Long, or fiddly, or error-prone, or humiliating in a
  low-stakes way. If the class breezes through, there is no need to relieve.
- **The pain is specific to what the idea fixes.** The tedium should be
  exactly what the method removes, so the reveal is a direct answer to what
  they just felt.
- **Two to four minutes, then cut it off.** Past that it stops being a hook
  and becomes the lesson.
- **The reveal is written and immediate.** Give the teacher the exact line
  that connects it: what they just did, how long it took, and what the new
  idea does to it.

Where the idea is about precision rather than effort, the headache can be
disagreement instead of tedium — get the class to produce four different
answers to the same question, then show that the new idea is what settles it.

## Slide placement

Default order in the deck, and the reasoning — deviate where the lesson
demands it, but say that you did:

1. **Headache** immediately after the retrieval starter, before the learning
   intention. It must land before students know what is coming, or the relief
   is spoiled.
2. **Flow diagram** after the learning intention, replacing or feeding the
   prior-knowledge check — the prior column *is* the prior-knowledge check.
3. **Hinterland** after the first worked example, once the notation means
   something. A story told before students know what it is about is a story
   about nothing.
4. **Real-world context** near the end, or attached to the practice as the
   setting for a question, so it points forwards rather than filling time.

Only the first lesson of a topic needs all four. For a lesson mid-sequence,
the flow diagram and one short hinterland or context item is usually right —
say which you left out and why, rather than padding.

## Building the slides

Follow the pptx skill for the mechanics: unpack, duplicate template layout
slides with `add_slide.py`, edit slide XML, repack, then
`validate.py out.pptx --original deck.pptx`.

- Build every slide from the branded template's layouts, never from a blank.
- Teacher-facing material goes in speaker notes — the hinterland script, the
  timing, the reveal line, the answers to the headache task. The slide itself
  carries almost no text.
- The flow diagram is shapes and connectors on the slide, not an image, so the
  teacher can edit a node when the sequence changes.
- Save alongside the original rather than over it.

## Report back

- Which of the four you built and where each slide sits
- The prior and future nodes, with the unit outline sections they came from
- Each hinterland item marked established / disputed / legend
- Any context you rejected as not genuine, and why — this is the part the
  teacher most needs to see, because it is where the temptation to invent is
  strongest
- What you left out for a mid-sequence lesson, and the reasoning
