# Maths Teaching Skills Pack

22 skills for planning, building, and auditing maths lessons — atomising
content, designing teaching sequences and explanation scripts, building slide
decks, worksheets, tests, practice, labelled diagrams, and relief lessons, giving feedback on student drafts,
and auditing existing resources.

This is a **plugin bundle**: all 22 skills below install in one step,
instead of teachers having to zip and upload each skill individually.

## How to install

This repository is a Claude Code plugin **marketplace** — add it once, then
install the plugin from it:

```
/plugin marketplace add sambiam/claude-teacher-skills
/plugin install maths-teaching-skills@claude-teacher-skills
```

All 22 skills are added in one go. To update later, run
`/plugin marketplace update claude-teacher-skills` followed by
`/plugin update maths-teaching-skills`.

To validate the structure locally before sharing further changes:

```
claude plugin validate .
```

## Setup this pack assumes

Several skills (`test-build`, `practice-test-build`, `assessment-audit`,
`ink-progress`, `deck-build`, `practice-audit`, `senior-homework-build`,
`explanation-script`, `relief-setter`, `draft-feedback`) work by reading files from an existing
class/topic folder structure rather than from uploads — e.g. prior tests, unit
outlines, lesson decks, atomisations. For these to work, you'll need an
equivalent folder layout connected to Claude (matching class → topic →
resource files), not just the skills themselves.

Skills that don't depend on a folder (`atomise`, `teaching-sequence`,
`open-middle-build`, `slop-build`, `ssdd-build`, `lesson-rationale`,
`differentiation-pack`, `non-routine-build`, `practice-select`) will work
standalone. `sa-task-design` designs and verifies tasks standalone from its
own offline bank, but needs `deck-build`'s template and scripts to render
them as slides. `diagram-labels` is a supporting skill other skills call
into when a diagram needs to go on the page — it isn't invoked directly.

## What's included

| Skill | What it does |
|---|---|
| atomise | Breaks a lesson/topic/exam question into its teachable atoms, misconceptions, and prerequisite map |
| teaching-sequence | Designs the instructional sequence, examples, and diagnostic questions for an atom |
| explanation-script | Writes the faultless-communication narration script for a worked example |
| deck-build | Builds (or repairs) a lesson PowerPoint from proven slide patterns |
| worksheet-build | Produces a printable worksheet + answer sheet (Mild/Medium/Spicy + Extra Hot) |
| test-build | Builds a new student assessment + worked solutions from prior tests in a topic folder |
| practice-test-build | Builds the revision paper students sit before the real test |
| assessment-audit | Audits a unit's tests/assessments for completeness and quality |
| draft-feedback | Marks a class set of student drafts against a task sheet — Word comments, yellow-highlighted spelling/grammar, on-track summary table |
| practice-audit | Judges whether existing practice is sufficient for a lesson |
| practice-select | Decides which kind of practice a lesson needs and routes to the right skill |
| slop-build | Writes sequenced fluency practice (SLOP / minimally different questions) |
| ssdd-build | Builds Same-Surface-Different-Deep interleaving question sets |
| open-middle-build | Writes low-floor/high-ceiling constrained-digit extension problems |
| non-routine-build | Finds or writes genuine problem-solving tasks (curated before written) |
| differentiation-pack | Builds support/extension materials for mixed classes, incl. SSO guided notes |
| lesson-rationale | Builds the "why are we learning this" slides — prior/future knowledge, hinterland, headache task |
| senior-homework-build | Builds the weekly Y10-12 homework sheet + solutions from the week's decks |
| ink-progress | Reads ink annotations on a taught deck to work out how far a lesson got |
| sa-task-design | Designs a task that develops the SA dispositions, from a verified offline bank of 48 tasks |
| relief-setter | Builds a cover note and self-contained resources for a lesson you won't be there to teach |
| diagram-labels | Renders a diagram as a static image with movable, editable text-box labels overlaid for DOCX/PPTX |

## One note on sharing

`sa-task-design` includes an offline extract of the **SA Curriculum:
Mathematics R-10 prototype**, which is marked *for authorised use only —
internal departmental use*. Keep this pack inside the Department for
Education. If you want to pass the pack further afield, delete
`skills/sa-task-design/references/sa-curriculum.md` first and substitute
your own curriculum framework — nothing else in the skill depends on it.

The other skills carry no restricted material.
