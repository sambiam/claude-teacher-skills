---
name: assessment-audit
description: "Audit a unit's tests and assessments for completeness and quality — whether a practice test, answers, and the actual test all exist, whether an assessment has a clear task sheet, exemplars, and marking guidance, and whether the unit as a whole gives students enough opportunity to problem-solve and reason. Also generates a new version of an existing test. Use when reviewing unit resources, checking assessment readiness, preparing a test for a new year, or auditing whether a unit is properly resourced. Trigger on 'check the assessments', 'do we have a practice test', 'new version of the test', 'task sheet', 'exemplars', or a weekly or termly resource review."
---

# Auditing tests, assessments, and unit scope

Two jobs here: checking that assessment materials are complete and sound, and
checking that the unit around them gives students something worth assessing.

Read `standards/assessment-requirements.md` from the teaching folder first —
it defines what a task must contain here, and overrides the defaults below.

## Part 1: Test units

For any unit assessed by a test, the minimum set is:

| Artefact | Present? | Notes |
|---|---|---|
| The test itself | | current year's version |
| Full marked solutions | | working shown, marks allocated |
| Practice test | | parallel structure, different numbers |
| Practice test solutions | | |

Audit each against the unit outline, not just for existence:

- **Alignment.** Every topic in the unit outline should appear on the test,
  weighted roughly as it was taught. Flag topics taught but not assessed, and
  anything assessed but never taught — the second is the one that damages
  students.
- **Difficulty spread.** There should be marks available for every student in
  the room. A test where the first question defeats a third of the class
  measures nothing useful about them.
- **Mark allocation.** Marks should reflect the work required. Check the total
  and the per-question sum agree.
- **Time.** Estimate working time and compare with the period length. Tests
  that don't fit measure speed.

### Generating a new version

When making a new version of an existing test:

- Keep the structure, topic order, mark allocation, and difficulty of the
  original. It has been calibrated against real students; that calibration is
  the valuable part.
- Change the numbers, contexts, and specific instances — not the question
  types.
- Where the original question has a particular pedagogical point (a specific
  misconception it probes, a deliberate edge case), preserve that point in the
  new numbers rather than accidentally sanding it off.
- Check that changed numbers don't produce ugly answers where the original was
  clean, or accidentally make a question trivial or impossible.
- Produce full solutions alongside, and **verify them computationally**. An
  error in a test is far more costly than an error anywhere else in this
  workflow — it affects grades and it is discovered publicly. Work each
  question independently rather than trusting the answer generated with it,
  and flag anything you can't fully verify.
- Save as a new file with the year in the name; never overwrite a previous
  year's test. Note in your report that the new version needs a human read
  before it goes near students — this is not optional, and you should say so
  plainly rather than implying the file is ready to print.

Store test versions and solutions where students can't reach them. If the
folder structure doesn't clearly separate student-facing from teacher-facing
material, flag that as a finding.

## Part 2: Assessment tasks

For units assessed by a task rather than a test, check for:

- **A task sheet** written for students, stating what to produce, the
  conditions, the length or scope, and the due date
- **Explicit criteria** — what distinguishes each achievement level, in
  language a student can act on. "Sophisticated application" tells a student
  nothing; describe what it looks like.
- **At least one exemplar**, ideally two at different levels, annotated to
  show why each earned what it earned
- **A marking guide or rubric** the teacher can apply consistently
- **Scaffolding for access** — how a student who needs support gets started
  without the task being done for them

Then check the task itself:

- Does it assess what the unit taught, or does it assess writing ability,
  presentation skill, or home resources?
- Can it be completed without the mathematics? If so, it doesn't assess the
  mathematics.
- Is it doable in the time and conditions given?

Where something is missing, decide between flagging and building. Build task
sheets, exemplars, and marking guides where the task itself is clear. Flag —
don't invent — anything requiring a judgement about standards, moderation
agreements, or faculty-level decisions.

## Part 3: Unit scope

The broader question: does the unit give students genuine opportunity to
problem-solve and reason, structured so they can succeed?

Look for:

- **Problem-solving that follows instruction, not replaces it.** Students
  should meet non-routine problems after they have the tools, not be expected
  to derive the tools from the problem. A unit whose problem-solving happens
  before the explicit teaching is set up for failure and should be flagged.
- **Reasoning tasks with an entry point.** "Explain why" and "will this always
  work" questions need a worked model of what a good explanation looks like,
  or most students write nothing.
- **Engagement through the mathematics.** Prefer tasks that are interesting
  because the mathematics is interesting over tasks decorated with a theme.
- **Spread across the unit**, not one problem-solving lesson bolted on at the
  end after the test.
- **A success route for every student.** For each rich task, ask what the
  weakest student in the room does for the first ten minutes. If the answer is
  "nothing", the task needs a scaffolded entry, not removal.

## Output

Report per class or per unit, in this shape:

```
# Assessment audit: <unit> (<class>, Year <N>)

## Test/assessment materials
<the table above, with findings>

## Alignment and quality
<what the audit found>

## Unit scope
<problem-solving and reasoning opportunities, with gaps>

## Actions taken
<files created, with paths>

## Needs your decision
<anything flagged rather than built, and why>
```

Keep "needs your decision" honest and short. A long list of auto-generated
material with no flags usually means judgement calls were made silently.
