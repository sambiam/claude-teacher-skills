---
name: sa-task-design
description: "Design a mathematics task that develops the SA Curriculum dispositions — resilient, resourceful, reflective — and render it as slides, a standalone deck or a worksheet. Anything from a five-minute starter to a whole-lesson modelling task: Which One Doesn't Belong, estimation, same-but-different, Open Middle, SSDD, maths Venns, slow-reveal graphs, goal-free problems, error analysis, visual patterns, three-act modelling, Citizen Math. Sources the real published task first and authors an original only when nothing suitable exists. Use when a lesson needs thinking rather than more procedure — 'give me a task for', 'something to start the lesson with', 'a rich task on', 'a hook for this topic', 'something for the last ten minutes', 'they can do it but don't understand it', 'a Friday task', 'something that builds resilience', 'which one doesn't belong for', 'a task that hits the SA dispositions', 'an inquiry for'. Prompts for year level, topic, time, lesson slot and output format when not given."
---

# SA Curriculum task designer

Tasks that make students think, mapped to the SA Curriculum's UNDERSTAND / DO /
BE frame, and delivered as something teachable tomorrow.

⚠ **Departmental circulation only.** `references/sa-curriculum.md` contains an
extract of the SA Curriculum prototype, which is marked *for authorised use
only*. Do not pass this skill outside the Department for Education. Outside SA,
delete that file and substitute your own curriculum framework — everything else
in the skill is framework-agnostic.

## The two failures this skill exists to prevent

**Failure one — the invented task.** The catalogue in `source-catalogue.md` gets
read as a bibliography rather than as a retrieval instruction. Claude recognises
the genre, reaches for the genre recipe, and writes its own estimation task, its
own WODB, its own Open Middle — without ever opening the site. What comes out
looks plausible and is worse than the original in every way the teacher notices:
no photo, no reveal, the wrong register, a level that drifts, and formatting that
matches nothing the class has seen. **Finding beats writing. Every time.** See
`references/sourcing-protocol.md`, which is binding.

**Failure two — the flat task.** A "rich task" only the top three can start; an
"investigation" a capable student finishes in ninety seconds; or a task that is
technically correct against the quality bar and still forgettable — thin
engagement, a context nobody cares about, a disposition claimed on paper but not
felt in the room. All are checked before anything is produced.

These two pull against each other, so the order matters: **engagement is a
criterion for choosing between found tasks, never a licence to invent one.** A
sourced task that reads slightly flat is a reason to go back to the sites and find
a better one, not a reason to start writing.

## Read first, in this order

1. `references/task-quality.md` — what counts as a task here. **Binding.**
2. `references/sourcing-protocol.md` — where to look and what to bring back.
   **Binding.**
3. `references/sa-curriculum.md` — the dispositions, capabilities and the
   Year 7–10 content, offline.
4. `references/task-genres.md` — the run protocol for each genre.
5. The class's `profile.md` and the unit outline, where the folder structure has
   them — for where the lesson sits. Skip if there is no such folder; ask
   instead.
6. The lesson's `atomisation.md` if one exists — it tells you what the class can
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

### 2. Find the task before you invent one
**This is the step that gets skipped, and skipping it is the single biggest cause
of poor output from this skill.** Read `references/sourcing-protocol.md` and work
its search ladder in order:

1. **The school's own drive** — connected class/topic folders, `local-assets.md`,
   downloaded Citizen Math lessons with their teacher guides, 3-act media already
   held. A local copy beats an equivalent web task every time.
2. **The live source sites** — when there is internet, actually fetch them.
   `WebFetch` / `WebSearch` against the specific pages in `source-catalogue.md`,
   going to the topic index rather than the homepage. Bring back the **image or
   video**, the **prompt wording as published**, the **reveal or answer**, and
   the **exact page URL**.
3. **The offline bank** — `task-bank-y7.md` … `-y10.md`. Note what these are: 48
   *authored equivalents*, written so the skill works with no internet. They are
   good tasks and fine to use, but for a media-dependent genre with a live
   connection, the real Estimation 180 day beats a bank task describing a photo
   nobody can see.
4. **Author it** — step 6, and only after 1–3 have genuinely been worked.

**Media-dependent genres may never be fabricated.** Estimation, slow-reveal
graphs, visual patterns, three-act, image-based WODB, Same But Different, error
analysis from real student work, Citizen Math. Embed the actual media, or put the
exact page URL on the slide and in the notes for the teacher to open live, or
switch to a genre that needs no media and say so. Inventing a photo is not one of
the options — if you cannot get the picture, you do not have an estimation task.

Record what you searched as you go. Step 6 and the output template both require it.

### 3. Build when you're confident; ask only when you aren't
**Default: pick the best candidate and build it.** Do not stop to offer a menu
just because step 2 turned up more than one task. A shortlist presented for no
reason is friction, and most of the time the fit is obvious once year level,
topic, slot, time and disposition are laid against the candidates.

**Build without asking when** any of these hold — and they usually do:
- one candidate clearly fits the five knowns better than the others;
- the teacher named the task, the genre, or the source;
- the candidates are near-equivalent, so the choice doesn't much matter — pick
  the one with the stronger stake, context or reveal (step 4) and move;
- the session is unattended.

**Stop and offer two to four options only when the choice turns on something you
genuinely cannot know**, specifically:
- **class history** — the candidates are equally good and the tiebreak is whether
  this class has already seen one of them, which is invisible from here;
- **different lessons** — the candidates would run the lesson differently (a
  10-minute WODB against a whole-lesson three-act), and the brief didn't settle
  which shape was wanted;
- **an unverifiable catch** — a candidate needs media you couldn't fetch, a login
  the school may not hold, or carries a US context or unit that may not land;
- **borderline level** — the strongest candidate sits a year above or below and
  you cannot tell from here whether this class would take it.

When you do ask, keep it to one short block and then wait:

```
Two that fit, and the choice depends on your class:

1. **<name>** · <source> · <genre>, <n> min — <one line: what students do>
2. **<name>** · <source> · <genre>, <n> min — <one line>

<One sentence: which you'd pick and why, and what would change your mind.>
```

**Either way, always list the runners-up** in the output under *Also considered*,
one line each with their source — so swapping is a sentence from the teacher, not
a re-run of the skill.

### 4. Engagement — the test applied to the candidates
A task can satisfy every disqualifier in `task-quality.md` — low floor, no
ceiling, no signposted method, reachable, an answer to defend — and still be
flat: no stakes, no reason to care which of three equivalent methods you used,
nothing a student would tell a friend about afterwards. Before locking the choice
in, ask honestly: **would a student who finishes early want to show someone else
what they found?**

If the honest answer is "they'd shrug", the fix is, in this order:

1. **Go back to step 2 and find a better one.** Most of the time the flat
   candidate simply means the search stopped too early — a different Estimation
   180 day, a different visual pattern, a Citizen Math lesson instead. This is
   the correct response and it is the one that gets skipped.
2. **Sharpen the sourced task** — same task, add the stake: run it as
   *too low / too high* first, board the best-so-far, add "can you beat it?",
   ask which method was better rather than accepting any answer.
3. **Only then**, consider authoring (step 6).

What a strong task has that a flat one doesn't:

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
not be the only task handed over for a disposition-focused request.

### 5. Decide who is holding the scaffolding
A task you run yourself can lean on you: the launch, the hint dropped at eight
minutes, the pull-together when half the room stalls. A task printed on a
worksheet has none of that. Whatever a student cannot get past, they sit in
front of until the bell — and the students who most needed the thinking are
exactly the ones who end up with an empty box.

So when the output is paper (question 5), the bar is higher than "low floor". It
is: **every student finishes it, alone, from the page.** That is not a lowering
of ambition. It moves the depth from *whether* a student can enter the task to
*how far* they take it, which is where the depth should have been anyway.

- Work the first case fully on the page, numbers filled in, as a model — not as
  an instruction to "start by trying a value".
- Make the next step the same move with different numbers. A table with the
  first row already completed is the standard device and it is hard to beat.
- Put the open part third, where a student arrives already holding the method
  and one success.
- Keep the ceiling in *how far*, never in *whether*. "Find the biggest you can,
  then see if you can beat it" has no ceiling and no entry cost; "find the
  optimum" has both.
- Anything you would otherwise have explained aloud belongs in Extra Hot, marked
  optional — not in the part every student is expected to reach.

Then read the page back as the least confident student in the class. If they
cannot produce a correct line of work with no adult in the room, what you have
is a lesson task, not a worksheet task: either build the scaffolding in, or
choose a different task.

A sourced task usually needs scaffolding *added* to survive the trip to paper.
Adding it is fine and does not make the task yours — keep the original wording of
the prompt, and say in the output what you added.

### 6. Author one only as a last resort — and match a real exemplar
Reached only when the ladder in step 2 came up empty. Two obligations attach.

**First, say what you searched.** The output must name the local folders checked,
the sites fetched, and in one line why nothing fit — wrong year level, wrong
topic, media unreachable, nothing at this length. "The bank had nothing" is not
an account of a search. If that sentence would be embarrassing to write, the
search was not finished; go back to step 2.

**Second, open a real one and copy its shape.** Before writing, fetch two or three
published examples of that genre — actual Open Middle problems, actual WODB grids,
actual Estimation 180 days — and match them on:

- **Prompt wording and length.** Published tasks are terse. An authored one runs
  long and over-explains, which is the clearest tell.
- **How much is given.** Count what the exemplar hands the student and give the
  same.
- **Layout on the page or slide.** Number of items, where the constraint sits,
  what the reveal looks like.
- **Level.** Check the exemplar's stated year band against the class's.

Then use the genre recipes in `task-genres.md` and apply the low-ceiling repair
moves from `task-quality.md` — reverse it, optimise it, constrain the digits, ask
how many, remove the goal, ask which and why. Reaching for bigger numbers instead
of one of those six moves is the failure mode.

Optimisation-under-a-constraint ("you have a fixed budget/length/amount, what's
the best outcome") is usually the single strongest lever for real Resilience — a
genuine, survivable stuck point — and is worth reaching for before a
reverse/reframe of a flatter question.

**Calibrate the optimisation by writing out one trial by hand.** Before setting
it, do exactly what a student does to test a single candidate, and count the
steps. "Fixed 24 m of fencing, best rectangle" is one step per trial — halve,
subtract, multiply — so a Year 8 can run twenty trials in ten minutes and the
pattern falls out of the table. The same question about a composite shape, a
rectangle with a semicircle on top, reads like a small step up and is not: the
student has to derive the height from the perimeter through a relationship
involving π before they can compute anything at all, so one trial is four steps
with a decimal in the middle, and most of the class never runs enough trials to
see a pattern. If a single trial is more than about three steps, either scaffold
the trial itself — give the relationship as a stated formula and the first row of
the table worked — or step back to the simpler shape and put the composite
version in Extra Hot. **The number of trials a student can actually run is what
makes an optimisation task work**; the shape it is about is secondary. Where the
task is going on paper, step 5 applies with full force here.

An authored task is labelled as authored. Never write a source line naming a site
for a task you wrote yourself; "an original in the style of *X*" is the honest
form, and the output template enforces it.

### 7. Verify the answer in code. Every time.
Open Middle optima, "find them all" counts, best-value comparisons, optimisation
minima — **enumerate them, never reason them**. Three of the tasks in this bank
were wrong on the first pass and were caught only by running the search. If the
answer cannot be verified computationally, verify it two independent ways and say
in the output that you did.

This applies to sourced tasks as well as authored ones. A published answer is
evidence, not proof — check it, and if it disagrees with your enumeration, say so
in the output rather than quietly picking one.

### 8. Check it against the disqualifiers
Read the four disqualifiers in `task-quality.md`, plus the engagement check in
step 4, the sourcing check in step 2 and — for anything going on paper — the
finish-it-alone check in step 5, against your task, in words, in the output. If it
fails one, fix it or say so — don't quietly ship it.

### 9. Build the output
`references/slide-patterns.md` for slides — into an existing deck or a standalone
one, per the format chosen at question 5. Dispatch to `worksheet-build` for a
printed page. Four slides where slides are wanted: task, optional hint, reveal,
consolidation. Launch script and anticipated responses go in the speaker notes.
Use `deck-build`'s `copy_slide.py` and `omml.py`; never hand-build a layout and
never render mathematics as text. `slide-patterns.md` carries three build traps
— canvas size, `find_pattern` matching notes rather than titles, and label-sized
pattern frames — read them before writing PowerPoint code, not after.

**Put the media on the slide.** Where step 2 retrieved an image, embed it with
`replace_picture` rather than describing it. Where it could not be embedded, the
slide carries the exact page URL and the speaker notes repeat it, so the teacher
opens it live. Attribute the source on the slide itself — the site name is
enough.

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

**Source** — one of:
  · Found at <site / lesson name> — <exact page URL>. Prompt reproduced as
    published. Media: <embedded / linked on the slide / unavailable, because …>
  · Held locally at <path>
  · From the offline bank, <T8-04>
  · **Authored for this lesson.** Searched: <local folders>, <sites fetched>.
    Nothing fit because <reason>. Written in the style of <exemplar + URL>.

**The prompt** (exactly as it goes on the slide/page)

**Every student can start by** …

**Every student can finish by** … — for a printed task, what the least
confident student in the room walks out having actually done

**Answer** — verified by <enumeration / two independent routes>

**Anticipated responses** — including the wrong one worth having

**The consolidation question**

**Extension**

**Against the disqualifiers**: entry bar ✓ · not inquiry-for-core-knowledge ✓ ·
has a ceiling ✓ · doesn't eat the lesson ✓ · genuinely engaging (real stake,
context or reveal) ✓ · sourced rather than invented, or authoring justified ✓ ·
finishable unaided, if it's going on paper ✓

**Also considered**: <every other candidate step 2 found, one line each with
its source — always included, whether or not you stopped to ask>

**Output built**: <n> slides/pages, into <deck / standalone file / worksheet>
**Judgement calls**: …
```

The **source** line is not optional and it must be true. Naming a site for a task
you wrote is the failure this skill was rewritten to stop.

The **judgement calls** section is not padding. It is what makes an unattended run
reviewable in two minutes instead of re-checkable in twenty.

## Internet, or no internet

**With internet — fetch.** Rung 2 of the search ladder is mandatory for
media-dependent genres and expected for everything else. Having a source
catalogue and not opening it is the failure mode; the catalogue is a list of
places to go, not a list of places to cite.

**Without internet — do not fail, and do not wait.** Everything needed is already
in `references/`: build from the bank, from any local Citizen Math library, and
from the genre recipes. Say in the output which links could not be checked, and
where a media-dependent genre was wanted, put the page URL on the slide for the
teacher to open in the room rather than substituting an invented equivalent.

If a 3-act lesson is planned more than a day out, **download the media now**. That
is the one thing that cannot be reconstructed from this skill offline.
