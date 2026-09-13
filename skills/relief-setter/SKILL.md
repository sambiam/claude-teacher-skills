---
name: relief-setter
description: "Build everything needed for a lesson you won't be there to teach — a short cover note ready to paste into Daymap, plus the resources a relief/casual teacher can run without you. Use whenever a teacher says they'll be absent, away, on leave, at PD, sick, or otherwise not taking a class, or asks for 'relief work', 'sub plans', 'cover work', 'a relief note', 'something for the CRT/casual', or 'set work for when I'm away'. Also use proactively when planning ahead reveals an upcoming absence against the schedule. Defaults to consolidation, not new teaching — asks about the buddy classroom and confirms the period length before building anything."
---

# Setting a relief lesson

A relief lesson has one job: keep the class doing real mathematics with nobody
in the room who can answer a question about why a step works. Everything here
follows from that constraint.

The two deliverables are different in kind and both matter:

1. **The Daymap note** — what the relief teacher reads in the first thirty
   seconds. Short, so it can't be missed inside a Daymap page's real estate.
2. **The resources** — what the students actually spend the period doing.
   Ready to print or upload with no further work from you or the relief
   teacher.

## Why relief lessons default to consolidation, not new teaching

A relief teacher cannot field "why does this work", cannot spot the
misconception forming three minutes in, and cannot adjust the explanation on
the fly — the exact things new instruction depends on. Practice and
elaboration of what's already been taught don't have that dependency: the
thinking work was already done in the room, and a worksheet or task doesn't
care who's supervising it. That's the whole rationale for the structure
below, not a rule to route around.

New content is the exception, not a design option to reach for because it's
more efficient timetabling. Treat it as something to justify, once (Step 4).

## Step 1 — Establish what this lesson is

Ask for whatever isn't already obvious from context: **which class**, **which
date/period**, and **why they're covering it** (irrelevant to the resources,
but worth a line in the note if it's a planned absence like PD or leave —
never write a reason the teacher hasn't given you).

Then work out the two things everything downstream depends on:

**Where the class actually is.** Find the most recently taught lesson in that
class's unit folder. If ink annotations exist on the deck, run `ink-progress`
to see where the lesson actually stopped — not where the plan said it would.
Read the unit outline to confirm what that means was covered. This is the
ceiling for the relief lesson: nothing on the page should require anything
past this point.

**How long the period actually is.** Read `schedule.md` (or ask) for the
period's start and end time, and check whether this is a single period or a
double (two consecutive periods with the same class, common when a relief day
absorbs an adjoining prep period). Don't assume a standard length — schools
vary, and a wrong guess here is why Step 5 exists.

## Step 2 — Decide: consolidation, or does new content have to happen?

Default to consolidation. Only route to Step 4 (new content) if the teacher
tells you the timetable genuinely leaves no other choice — the next lesson
in sequence cannot simply move to next time. If you're not sure which
applies, ask; don't infer it from the unit outline looking like it's "due"
for the next lesson. A relief day is a legitimate reason to slow the unit
down by one lesson, and that's almost always the better trade.

## Step 3 — Build the consolidation lesson

Two parts, both drawing only on content already covered:

**Part A — the core task.** This is practice on what's been taught, not a
new worksheet built from nothing. Run `practice-audit` first — a lot of the
time the questions already exist in the deck, in `questions/`, or in a
previous worksheet, and the job is packaging what's there rather than writing
new material. Where something genuinely needs building, use `practice-select`
to choose the type (for a relief lesson specifically, prefer something
self-checking and low-ambiguity — SLOP or a worksheet over anything that
depends on classroom discussion to make sense) and dispatch to
`worksheet-build` so the page is complete and self-contained: instructions a
relief teacher can read aloud verbatim, an answer sheet the relief teacher can
use to check work without knowing the maths themselves.

**Part B — the extension/interest task.** This is what makes the lesson feel
like more than busywork, and what fills the room for early finishers or runs
as a second activity in a double. In priority order:

1. An existing interactive classroom activity for this unit — check
   `02. Powerpoints/Activities/` and similar folders for anything already
   built (an Amplify activity, an estimation task, a game) that fits what's
   been covered. Reusing something proven beats writing something new that a
   relief teacher has to run cold.
2. `sa-task-design` for a genuine deepening or hook task if the format needed
   is slides — ask it for the standalone-deck format so it isn't wired into a
   teaching deck that assumes you're presenting it.
3. `non-routine-build` or `open-middle-build` for a challenge task with a low
   floor and no ceiling — these work unsupervised because every student can
   start and there's no single "right way in" a teacher would normally
   unblock.

Don't pick the extension task by reflex. A relief lesson is a bad place for
anything that depends on a facilitator reading the room, however good the
task is in your own hands.

## Step 4 — When new content is genuinely unavoidable

This is the exception path — flag it as one in the output rather than
blending it in as if it were routine.

The relief teacher can supervise new learning but can't deliver the
explanation live, so the explanation has to travel with the resources:

- **Prefer an existing video** that teaches the specific atom, pitched at the
  right level — search for one rather than assuming your usual explanation
  script survives without you saying it. Link it directly and tell the relief
  teacher when in the period to play it.
- **If no suitable video exists**, build short explanation slides via
  `teaching-sequence` and `deck-build` — worked examples with the reasoning
  written out on the slide itself (not just in speaker notes, which the
  relief teacher won't read to the class), because nobody is there to narrate
  the parts you'd normally say out loud.
- **Follow immediately with practice on exactly that atom** — one atom, SLOP
  first (`slop-build`), never straight to anything requiring judgement. A
  relief teacher watching a class attempt reasoning on content they just met
  from a video has no way to catch it going wrong.

## Step 5 — Check there's enough for the actual time

Work out an honest time estimate for what you've built: worksheet questions
at a rough per-question rate for the year level, the extension task's own
estimate if `sa-task-design` gave one, video length if there is one. Compare
against the period length from Step 1.

- **Single period**: core task should comfortably fill it with the extension
  as a genuine second activity or early-finisher option, not padding.
- **Double period**: needs noticeably more than a single, not exactly double
  — a relief double loses more time to settling, instructions, and the
  novelty of a different adult in the room. Build a second core block (a
  different atom's worth of practice, not more of the same one) rather than
  just a longer version of one worksheet, and treat the extension task as
  something a meaningful fraction of the class will actually reach.

If the estimate comes up short, add more before finishing — an relief lesson
that runs out at the twenty-minute mark is worse than one slightly over-full,
because there's nobody who can improvise a genuine extension on the spot.
Say the time estimate in the output so this is checkable, not asserted.

## Step 6 — The buddy classroom

Every relief note needs a plan for a student who needs to leave the room —
and that plan is a specific, named classroom, not a generic "send them to
their buddy class". This is genuinely lesson-specific, so don't guess or
carry over a default from memory without checking.

Read `classes/<class>/profile.md` first. If it has a `buddy_class:` line,
use it and don't ask again. If it doesn't, ask which classroom is buddied
with this class for this lesson, then offer to save it to the profile so
future relief notes for this class don't need to ask — but confirm before
writing, since a buddy arrangement can be a one-off for the day rather than
the class's standing arrangement.

## Step 7 — Write the Daymap note

This is the artefact that actually gets read, so it earns its length by
being short. A relief teacher scans it once before the bell and glances at
it again mid-lesson — it is not the place for anything they could instead
find by opening the resource file.

Keep to roughly this shape, and cut anything that isn't decision-relevant to
someone standing in the room:

```
<Class> — <date>, Period <n> (<start>–<end>)
<One line: what today's lesson is, in a phrase a non-specialist can say aloud>

Materials: <exactly what to hand out / open, and where it is — filename and
folder, or "on the desk">

Plan:
- <n> min: <what happens first>
- <n> min: <core task>
- <n> min: <extension task, and who it's for>

If a student needs to leave the room: send to <buddy class, room>.
Behaviour: <only what's non-obvious for this specific class — a seating
plan quirk, a student needing a specific accommodation already in place,
anything the regular teacher would say in the corridor on the way out.
Don't restate generic school behaviour policy.>

Answers: <where the answer sheet is, so the relief teacher can check work
without needing to know the maths>
```

Don't editorialise about the maths in this note — that's what the resource
files are for. This note is a set of instructions, not a lesson plan.

## Step 8 — Save and hand over

Save resources inside the lesson's own folder, in a `relief/` subfolder
alongside the deck and worksheets it draws on:

```
<unit>/<lesson>/relief/
  <topic>_relief_worksheet.docx
  <topic>_relief_worksheet_ANSWERS.docx
  <topic>_relief_extension.pptx        (or .docx, whichever the task built)
  relief_note_<date>.md                (the Daymap text, ready to paste)
```

If new content was unavoidable (Step 4), also include the explanation
slides or the video link in this folder, named so their purpose is obvious
without opening them.

## Output

```
## Relief lesson: <class>, <date> Period <n> (<single/double>, <length> min)
Covering: <what's already been taught, ceiling for this lesson>
Structure: consolidation | new content (exception — <why>)

Built:
- Core: <what, from what atoms, est. <n> min>
- Extension: <what, source (existing / sa-task-design / non-routine-build /
  open-middle-build), est. <n> min>
- [If new content] Explanation: <video link, or slides built>

Time check: <sum> min against a <length> min <single/double> period — <verdict>
Buddy class: <room, and whether it was asked this time or read from profile.md>

Files: <paths under relief/>

Daymap note (copy below into Daymap):
---
<the note>
---

Judgement calls: <anything inferred rather than confirmed — the unit
boundary used for "already taught", a time estimate, a task substituted
because nothing existing fit>
```

The judgement calls section matters here more than in most of these skills —
this output may be read and acted on by someone who wasn't in the room for
any of the decisions behind it, sometimes on a morning when nobody has time
to double-check.

## Dispatch, don't duplicate

| Need | Use |
|---|---|
| What's been covered, where the last lesson stopped | `ink-progress` |
| Whether existing practice is enough before building more | `practice-audit` |
| Choosing the practice type for the core task | `practice-select` |
| The core worksheet + answers | `worksheet-build` |
| A deepening/hook task, or nothing existing fits the extension slot | `sa-task-design` |
| A genuine problem-solving challenge task | `non-routine-build` |
| A constrained, no-ceiling challenge task | `open-middle-build` |
| Fluency practice for one atom (new-content exception path) | `slop-build` |
| The instructional sequence and worked examples (new-content exception path) | `teaching-sequence` |
| Building the explanation slides (new-content exception path) | `deck-build` |
| Confirming what atoms this lesson actually contains | `atomise` |

This skill decides what the lesson needs and assembles it; it doesn't write
questions or slides itself.
