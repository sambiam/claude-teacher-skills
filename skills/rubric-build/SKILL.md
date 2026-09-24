---
name: "rubric-build"
description: "Build an assessment rubric from a task sheet or assessment — a standard table rubric or a Daymap .rbc file. Always asks which format first. Use for 'build a rubric', 'marking guide', 'Daymap rubric', 'convert this rubric'."
---

# Rubric Build

Builds a marking rubric from an assessment/task sheet, in one of two output formats. **Always confirm the format before doing any other work** — teachers frequently just want a standard table rubric, not a Daymap import file, and building the wrong one wastes a full generation cycle.

## Step 0 — Ask the format (always, every time)

Before reading the assessment in depth, ask:

> Do you want this as a **standard table rubric** (a Word table — A/B/C/D/E or however many bands, dropped into or alongside the task sheet), or a **Daymap .rbc file** (the full A+ to E−/I plus-minus import file)?

Don't assume from context (e.g. an uploaded "Daymap guide" doc doesn't mean this particular request wants the .rbc — ask anyway). If the user's request already unambiguously states the format ("make me a Daymap rubric", "just a normal rubric table"), this step can be a one-line confirmation rather than a full question, but never skip it silently.

## Step 1 — Analyse the assessment (both paths)

- Read the task sheet / assessment carefully.
- Identify the main content skills, reasoning/communication demands, and evidence students are expected to produce.
- Note the year level and likely Australian Curriculum (or SACE) achievement standard — ask the teacher if it isn't obvious from context.
- **Check for an existing rubric already in the document** (a success-criteria table, grade-boundary notes, etc.). If one exists, ask the teacher whether to:
  - convert/adapt the existing rubric (keep its criteria and wording as the base), or
  - design a fresh rubric from the assessment.
  Do not proceed past this until it's resolved.

## Step 2 — Design rules (both paths)

- 3–5 broad, substantial criteria — never many narrow ones.
- Each criterion needs evidence from a substantial part of the task, not just a small slice.
- No effort, behaviour, neatness, or completion-only criteria. (A "how many parts did you finish" criterion is a smell — flag it to the teacher rather than silently dropping or silently keeping it, since teachers sometimes want it anyway.)
- Observable, evidence-based language — avoid "understands", "tries hard", "shows effort" unless tied to something visible in the work.
- Clear, meaningful progression between bands — avoid descriptors that differ only by "excellent/good/sound/basic".
- Weight criteria by importance (more marks/prominence to the skills that matter most in the task), not evenly by default.
- Anchor top and bottom bands concretely: top band = exceptional, accurate, independent; bottom (non-zero) band = extremely limited but still observable evidence.

## Step 3 — Confirm the plan before building (both paths)

Present, and get explicit confirmation on:
- The rubric title.
- Curriculum/achievement-standard alignment being used (confirm year level if unstated).
- The proposed criteria and what each is worth (marks or weighting).
- A one-line rationale for why these criteria were chosen.
- A short summary of what top / middle / bottom band performance broadly looks like.
- For the Daymap path only: confirm the file will use full plus/minus ratings (A+, A, A−, B+, B, B−, C+, C, C−, D+, D, D−, E+, E, E−, I).

Do not generate the output file until the teacher confirms or has given specific changes to make first.

## Step 4A — Standard table rubric

Build a table: one row per criterion, one column per band (default A/B/C/D/E unless the school's existing convention or the teacher says otherwise — match whatever band scheme the uploaded task sheet already uses if one is present). Put it in a Word document (use the docx skill) — either as a new file or inserted into the existing task sheet, per the teacher's preference. No JSON, no Daymap structure needed for this path.

## Step 4B — Daymap .rbc file

### Descriptor text: default to one shared text per letter band

Unless the teacher says otherwise, write **one descriptor text per letter (A, B, C, D, E, I)** and reuse it across that letter's three sub-ratings (+, base, −). The marks still step down across the three sub-ratings (see below) so selecting + or − in Daymap still changes the score even though the wording is identical — this is what most teachers actually want and matches how they use the +/− picker in practice.

**Exception:** if the source rubric or grade-boundary notes draw a genuine, substantive line *within* a letter band (e.g. "reaches the target ⇒ A+, doesn't reach it ⇒ A"), give that specific sub-rating its own distinct text instead of sharing it, and call this out explicitly in the Step 3 confirmation so the teacher can veto it.

### Mark generation

For each criterion with `MaxMark = M`:
- Generate 15 whole-number marks (RatingIndex 1–15, A+ through E−), non-increasing, starting at `M` (A+) and ending at `1` (E−).
- Use linear interpolation and round to whole numbers; when `M < 15` some adjacent marks will legitimately repeat — that's fine and expected (per Daymap rubric conventions), just keep RatingIndex and DescriptorID distinct.
- RatingIndex 16 (I) always has Mark `"0"` and text `"Not attempted or insufficient assessable evidence provided."` (or task-specific non-completion wording) — never effort/behaviour wording.
- `MaxMark` for the criterion must equal the A+ mark.

Reference implementation:
```python
def gen_marks(maxmark):
    vals = []
    for i in range(15):
        v = round(maxmark - i * (maxmark - 1) / 14)
        vals.append(int(v))
    for i in range(1, 15):
        if vals[i] > vals[i - 1]:
            vals[i] = vals[i - 1]
    vals[-1] = max(vals[-1], 1)
    return vals  # 15 marks, A+ -> E-; append 0 for I
```

### RBC JSON structure (exact)

```json
{
  "Criteria": [
    {
      "Descriptors": [
        {"DescriptorID": 110001, "CriteriaID": 200001, "RatingIndex": 1, "Text": "...", "Mark": "20"},
        ... 16 total per criterion, RatingIndex 1-16 ...
      ],
      "CriteriaID": 200001,
      "Criteria": "1. Criterion name here\n",
      "MaxMark": 20,
      "CriteriaIndex": 1
    }
    // one object per criterion (3-5 total)
  ],
  "Ratings": [
    {"RatingIndex": 1, "Rating": "A+"}, {"RatingIndex": 2, "Rating": "A"}, {"RatingIndex": 3, "Rating": "A-"},
    {"RatingIndex": 4, "Rating": "B+"}, {"RatingIndex": 5, "Rating": "B"}, {"RatingIndex": 6, "Rating": "B-"},
    {"RatingIndex": 7, "Rating": "C+"}, {"RatingIndex": 8, "Rating": "C"}, {"RatingIndex": 9, "Rating": "C-"},
    {"RatingIndex": 10, "Rating": "D+"}, {"RatingIndex": 11, "Rating": "D"}, {"RatingIndex": 12, "Rating": "D-"},
    {"RatingIndex": 13, "Rating": "E+"}, {"RatingIndex": 14, "Rating": "E"}, {"RatingIndex": 15, "Rating": "E-"},
    {"RatingIndex": 16, "Rating": "I"}
  ],
  "HasMarks": true,
  "RubricID": 305824,
  "OwnerID": 719,
  "RubricType": 0,
  "Title": "Rubric title here",
  "Description": "Briefly describe the assessment and the key skills assessed.",
  "Created": "0001-01-01T00:00:00.0000000",
  "Modified": "2026-09-24T00:00:00.0000000",
  "ModifiedBy": 0,
  "Archived": false,
  "HasLinkedRubric": false,
  "GroupCriteria": false,
  "PlusMinus": true
}
```

Rules:
- `DescriptorID` and `CriteriaID` values unique across the whole file (e.g. block per criterion: 110001–110016, 120001–120016, ...).
- `RubricID` is a new number each time — never reused from a prior rubric.
- `OwnerID` stays `719` (this school's Daymap import owner) unless the teacher gives a different one.
- Marks are strings (`"15"`, not `15`).
- UTF-8 JSON, valid, `.rbc` extension.

### Build and validate with a script

Write a small Python script that assembles the structure above and writes the file, then re-reads and asserts before delivering:
- `PlusMinus` is `true`.
- Exactly 16 `Ratings`.
- Every criterion has exactly 16 `Descriptors`.
- All `DescriptorID` values unique; all `CriteriaID` values unique.
- Marks are non-increasing across RatingIndex 1→16 within each criterion, end at `0` (I).
- `MaxMark` equals the criterion's A+ mark.

Deliver the file with `SendUserFile` after validation passes — don't paste the JSON into chat unless asked.

## Final response (both paths)

Keep it short: one line confirming what was built, the file, and — for the Daymap path — a one-line note of any criterion-specific text exceptions made in Step 4B. Don't re-explain the whole rubric back to the teacher; they can open the file.