---
name: sa-task-design
description: "Design a mathematics task that develops the SA Curriculum dispositions — resilient, resourceful, reflective — and render it as slides, a standalone deck or a worksheet. Anything from a five-minute starter to a whole-lesson modelling task: Which One Doesn't Belong, estimation, same-but-different, Open Middle, SSDD, maths Venns, slow-reveal graphs, goal-free problems, error analysis, visual patterns, three-act modelling, Citizen Math. Use when a lesson needs thinking rather than more procedure — 'give me a task for', 'something to start the lesson with', 'a rich task on', 'a hook for this topic', 'something for the last ten minutes', 'they can do it but don't understand it', 'a Friday task', 'something that builds resilience', 'which one doesn't belong for', 'a task that hits the SA dispositions', 'an inquiry for'. Prompts for year level, topic, time, lesson slot and output format when not given. Draws on a verified offline Years 7-10 task bank, so it works with no internet."
---

# SA Curriculum task designer

Tasks that make students think, mapped to the SA Curriculum's UNDERSTAND / DO /
BE frame, and delivered as something teachable tomorrow.

⚠ **Departmental circulation only.** `references/sa-curriculum.md` contains an
extract of the SA Curriculum prototype, which is marked *for authorised use
only*. Do not pass this skill outside the Department for Education. Outside SA,
delete that file and substitute your own curriculum framework — everything else
in the skill is framework-agnostic.

The thing this skill exists to prevent is three standard failures: a "rich task"
that only the top three students can start; an "investigation" a capable student
finishes in ninety seconds; and a task that is technically correct against the
quality bar but forgettable — thin engagement, a context nobody cares about, a
disposition claimed on paper but not actually felt in the room. All three are
checked before anything is produced. The third is easy to miss, because a task
can pass every disqualifier in `task-quality.md` and still be flat — see
"Engagement is not optional" below. It was added after a task (find a composite
shape's area three ways) that was correctly-formed but dull: no stakes, no
context, no reason to care which way you found the answer.

## Read first, in this order

1. `references/task-quality.md` — what counts as a task here. **Binding.**
2. `references/sa-curriculum.md` — the dispositions, capabilities and the
   Year 7–10 content, offline.
3. `references/task-genres.md` — the run protocol for each genre.
4. The class's `profile.md` and the unit outline, where the folder structure has
   them — for where the lesson sits. Skip if there is no such folder; ask
   instead.
5. The lesson's `atomisation.md` if one exists — it tells you what the class can
   already do, which decides hook versus deepening.

Then, only when you know what the task is:
`references/slide-patterns.md` for how to render it.

## Five things you must know before designing

Ask for anything missing. Do not guess — a task built for the wrong slot is
worse than no task, because it eats the lesson.

| | Question | Why it changes the task |
|---|---|---|
| **1** | **Year level and class** | Decides the content ceiling, and whether SSO or support staff are in the room. |
| **2** | **Topic, or the content descriptor** | Anchors the task to `AC9M…` rather than to a vibe. |
| **3** | **How long — and where in the lesson?** | 6-minute starter, 15-minute deepening and 45-minute whole-lesson are three different genres, not one genre at three lengths. |
| **4** | **Have they been taught it yet?** | **This is the one that gets skipped.** Before → hook, short, creates the need. After → deepening, uses the fluency. Inquiry must never be the delivery mechanism for the core procedure. |
| **5** | **Output format** | Into an existing lesson deck, a standalone deck, a worksheet, or more than one — these are genuinely different deliverables, not a rendering detail. |

If you are given several of the five, ask for the rest in **one** question with
options — don't interrogate. Always ask #5 explicitly rather than assuming; don't
infer it from the fact that a deck happens to be available. If no existing lesson
deck has been provided or found, default to a **standalone deck** without asking,
but still ask whether a worksheet is also wanted.

If the session is unattended, take: the class from the schedule for the next
lesson if one is readable, the topic from the unit outline, 10 minutes as the
duration, *after teaching* as the slot, and standalone deck as the format — then
say plainly at the top of the output that those were assumptions.

Optional but worth asking when the answer isn't obvious: **which disposition are
you trying to build?** A class that has stopped trying needs a Resilient task; a
class that can only do the thing the exercise names needs a Resourceful one.

## The design sequence

### 1. Locate it in the curriculum
Name the content descriptor, the **capability** and the **disposition**. One
disposition claimed strongly, not three claimed weakly. If you cannot name the
disposition, the task is an exercise.

### 2. Engagement is not optional
A task can satisfy every disqualifier in `task-quality.md` — low floor, no
ceiling, no signposted method, reachable, an answer to defend — and still be
flat: no stakes, no reason to care which of three equivalent methods you used,
nothing a student would tell a friend about afterwards. Before locking in a task,
ask honestly: **would a student who finishes early want to show someone else what
they found?** If the honest answer is "they'd shrug", the task needs one of
these, not bigger numbers or a longer prompt:

- **A real stake or constraint**, not just a shape to compute — "you have a fixed
  24 m of fencing, what's the *best* paddock" beats "find this shape's area three
  ways", because now there's a right answer to fight for.
- **A concrete, physical or social context** the student can picture (a farm, a
  competition, a real object, a disagreement to settle) rather than an abstract
  shape or a bare number.
- **A genuine surprise or reveal** — the answer does something the student didn't
  expect (a pattern that always holds, a counterintuitive winner).

A "find it three ways" or "which of these matches" task is a perfectly good
**secondary** offering — quick to build, still develops something — but should
not be the only task handed over for a disposition-focused request. When time
allows, build the stronger, more engaging task as the main option and mention
that a lighter alternative exists, rather than the reverse.

### 3. Look in the bank before writing anything
- `references/task-bank-y7.md` … `-y10.md` — 48 tasks, fully written, every
  answer verified. Nothing here needs the internet.
- `references/source-catalogue.md` — **check "Your own local library" second,
  always.** A downloaded Citizen Math lesson with its teacher guide, or 3-act
  media already on the school drive, beats an equivalent web task every time.
- `references/three-act-catalogue.md` — 83 modelling tasks with their questions.
- `references/btc-index.md` and the rest of `source-catalogue.md` — for
  everything else, with the liveness and licence verdicts attached.

When picking between two bank tasks that both fit, prefer the one with the real
context or constraint (step 2) over the one that is just "the same computation
done a different way".

### 4. Write one only if the bank has nothing suitable and engaging
Use the genre recipes in `task-genres.md`. Then apply the low-ceiling repair
moves from `task-quality.md` — reverse it, optimise it, constrain the digits, ask
how many, remove the goal, ask which and why. Reaching for bigger numbers instead
of one of those six moves is the failure mode.
Optimisation-under-a-constraint ("you have a fixed budget/length/amount, what's
the best outcome") is usually the single strongest lever for real Resilience — a
genuine, survivable stuck point — and is worth reaching for before a
reverse/reframe of a flatter question.

### 5. Verify the answer in code. Every time.
Open Middle optima, "find them all" counts, best-value comparisons, optimisation
minima — **enumerate them, never reason them**. Three of the tasks in this bank
were wrong on the first pass and were caught only by running the search. If the
answer cannot be verified computationally, verify it two independent ways and say
in the output that you did.

### 6. Check it against the disqualifiers
Read the four disqualifiers in `task-quality.md`, plus the engagement check in
step 2, against your task, in words, in the output. If it fails one, fix it or say
so — don't quietly ship it.

### 7. Build the output
`references/slide-patterns.md` for slides — into an existing deck or a standalone
one, per the format chosen at question 5. Dispatch to `worksheet-build` for a
printed page. Four slides where slides are wanted: task, optional hint, reveal,
consolidation. Launch script and anticipated responses go in the speaker notes.
Use `deck-build`'s `copy_slide.py` and `omml.py`; never hand-build a layout and
never render mathematics as text. `slide-patterns.md` carries three build traps
— canvas size, `find_pattern` matching notes rather than titles, and label-sized
pattern frames — read them before writing PowerPoint code, not after.

## Dispatch, don't duplicate

This skill sits alongside others in this pack that already do part of the job.
Hand over rather than reimplementing:

| If the answer is… | Use |
|---|---|
| an SSDD set | `ssdd-build` |
| an Open Middle problem as the Spicy question | `open-middle-build` |
| a competition-style problem | `non-routine-build` |
| fluency, or a minimally different / thin-sliced sequence | `slop-build` |
| a printed handout | `worksheet-build` |
| "why are we learning this", a headache, a hinterland story | `lesson-rationale` |
| unclear what kind of practice is needed at all | `practice-select` |
| the slides themselves | `deck-build` |

Come here when the need is **a task that makes them think**, and specifically when
the dispositions are the point.

## What the output looks like

```
## Task: <name>
Year <n> · <topic> · `AC9M…` · <slot>, <n> minutes · <deck / standalone / worksheet>
Develops: <disposition> · <capability>

**The prompt** (exactly as it goes on the slide/page)

**Every student can start by** …

**Answer** — verified by <enumeration / two independent routes>

**Anticipated responses** — including the wrong one worth having

**The consolidation question**

**Extension**

**Against the disqualifiers**: entry bar ✓ · not inquiry-for-core-knowledge ✓ ·
has a ceiling ✓ · doesn't eat the lesson ✓ · genuinely engaging (real stake,
context or reveal) ✓

**Output built**: <n> slides/pages, into <deck / standalone file / worksheet>
**Judgement calls**: …
```

The **judgement calls** section is not optional and it is not padding. It is what
makes an unattended run reviewable in two minutes instead of re-checkable in
twenty.

## When there is no internet

Everything needed is already in `references/`. Do not fail, and do not wait —
build from the bank, from any local Citizen Math library, and from the genre
recipes, and note in the output which links could not be checked.

If a 3-act lesson is planned more than a day out, **download the media now**. That
is the one thing that cannot be reconstructed from this skill offline.
