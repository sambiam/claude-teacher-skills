---
name: "final-grading"
description: "Grade a class set of final assignments against a rubric's performance standards: calibrate on graded exemplars, comment each document in Word, give A+ to E- (or I) per standard, run AI-use and plagiarism checks, and produce a grading document. Use for 'mark the final assignments', 'grade these submissions'."
---

# Final grading

Use this skill to mark a class set of final submissions. It produces four outputs:

- **A commented copy of every student document.** Comments carry the teacher's name and are tagged with the standard they address. Spelling and grammar errors are highlighted in yellow.
- **A grading document.** It gives each student a grade for every performance standard, a final grade and a short assessment comment.
- **Teacher-only marking notes.** These cover calibration, the comparative ranking and borderline calls.
- **A teacher-only integrity check.** It covers AI use, copying between students and copying from exemplars.

The commenting mechanics are the same as in the `draft-feedback` skill (reading the documents, anchoring comments, equations, highlighting). Load that skill and reuse its `flat.lua`, `dump.py` and `annot.py`.

## Step 1: Gather inputs

Ask for these in a single AskUserQuestion call, skipping anything the teacher has already given.

1. **Rubric (required).** Ask specifically for the task sheet or rubric that contains the performance standards. Grade against its specific features, such as CT1 to CT4 and RC1 to RC5 for SACE Stage 1 Mathematics.
2. **Exemplars across grade bands (required).** Ask specifically for graded exemplars, ideally at least a high (A), a middle (B or C) and a low band, with the grade in the file name or stated. Explain that they are used to calibrate the grades. If there are none, say the grades are uncalibrated and flag this in the notes.
3. **Submissions.** A folder or a zip of the student files.
4. **Commenter name.** Use the format `Lastname, Firstname (School)`. The initials are the first letter of the first name followed by the first letter of the last name.
5. **Output location.** Ask whether they will give access to a folder for the outputs. If not, everything goes in a zip attached in the chat.
6. **Optional inputs.**
   - Students' earlier drafts, so finals can be compared with drafts.
   - The school's rule on AI use for this task.
   - Anything to ignore or emphasise, such as template wording or rounding.

## Step 2: Extract the standards

For each specific feature, record its code, its descriptor and its A to E descriptors. Every student gets a grade for every feature.

Grade scale:

```
I = 0 (incomplete or not attempted)
E- = 1, E = 2, E+ = 3
D- = 4, D = 5, D+ = 6
C- = 7, C = 8, C+ = 9
B- = 10, B = 11, B+ = 12
A- = 13, A = 14, A+ = 15
```

Use **I** for a feature only when there is no evidence for it at all.

## Step 3: Calibrate on the exemplars first

1. Mark each exemplar fully, as if it were a student, and grade every feature.
2. Write a calibration table: exemplar, given grade, your grade, and the features that decide the band.
3. If your grade differs from the given grade, adjust how you read the descriptors until they agree. These become the thresholds for the class.

## Step 4: Read every submission properly

Follow Step 2 of `draft-feedback`: run pandoc with the table-flattening filter, then check the parts it misses.

- **Text boxes and their OMML.** Extract `w:txbxContent` separately.
- **Ink and shape diagrams.** Render or view them.
- **Working split across table columns.** It can read out of order, so check the sequence.

Recompute every number in Python. Each wrong value gets a comment.

As you read, note each error with its paragraph index, the student's strengths, and the evidence for each feature.

## Step 5: Integrity check (AI use and plagiarism)

Run this on every class set, before grading. Save the scripts in a separate folder from the submissions. Compare finals, exemplars and, if provided, drafts.

**A. Copying between students**

- Normalise each document's text, keeping equation text: lower-case it and strip punctuation and LaTeX commands.
- Build 6-word and 8-word shingles.
- **Rare shingles.** Count shingles shared by exactly two documents.
  - Phrases found in four or more documents are class-taught or template wording. Ignore them. (In the 2026 calculus set, "re-arranging the formula for volume to get h in terms of v and r" appeared in 15 files.)
  - Strip template text from the task sheet.
- **Long matching passages.** For the top-scoring pairs, use `difflib.SequenceMatcher(autojunk=False)` on the word lists and list blocks of 10 or more words.
- **Shared fingerprints.** These are much stronger evidence than common phrasing:
  - identical unrounded decimals (four or more decimal places) shared by only two or three students, after checking whether the value is simply correct;
  - the same wrong value or the same wrong method in the same place;
  - the same odd wording or typo, for example "local or maximum of minimum".

**B. Copying from the exemplars.** Run the same shingle comparison of each submission against each exemplar, because exemplars circulate between year groups.

**C. AI and pasted-text markers**

No single marker is meaningful, so look for clusters, and compare each student's text with their own writing elsewhere in the report. Check only the non-equation text: drop `m:oMath` before reading `w:t`.

- American spellings (minimize, optimization, analyze, utilize) mixed with Australian ones in the same piece.
- Typed Unicode maths in sentences (πr²h, ≈, √, ×) when the rest of the class uses the equation editor. ChatGPT output pastes this way.
- Markdown or LaTeX leftovers: `**`, `###`, `\frac`, `$`.
- Em-dash asides, and stock AI phrasing: "is essential for", "plays a crucial role", "real-world applications", "delve", "it is important to note", "this demonstrates", "ensuring", "key insight".
  - Words like "optimal" and "therefore" are normal in maths reports. Don't count them.
- A sudden jump in register: a polished introduction or conclusion next to plain working.
- Font changes on pasted blocks. Count runs per `w:ascii` font. A font that appears only on some paragraphs (such as Segoe UI or Aptos inside a Times or Calibri document) means the text was pasted from a browser, a translator or another student's file. Read what those runs say.
- An acknowledged AI tool in the text or the bibliography.

**D. File metadata** (`docProps/core.xml`, `docProps/app.xml`, `word/settings.xml`)

- Created and modified dates. A file created just after a classmate's, with very similar content, is one to look at.
- Revision count and `TotalTime`. A long report with 2 to 4 revisions or a few minutes of editing was pasted into a new file. This is weak on its own, because "Save a copy" does the same.
- Shared rare `w:rsid` values between two students' files mean one file was derived from the other.
- If drafts were provided, an unchanged draft resubmitted as the final.
- Leftover comments from earlier rounds, especially another student's.

**E. Report**

Write a landscape `.docx` titled "Integrity check – teacher only" with a table of Level (High / Medium / Low / Known / Clear), student(s), concern, specific evidence (quoted phrases, shared values, metadata) and suggested follow-up.

- State at the top that these are indicators for a conversation, not proof, and that AI-text detection is unreliable.
- List what was checked, and that the exemplars were checked.
- Include a "Clear" row for everyone else.

Never mention integrity concerns in student comments, in the grading document or in the assessment comments. Grade the work as submitted unless the teacher decides otherwise.

## Step 6: Write the comments

- **How many.** 10 to 20 comments per student is a guide, not a hard floor or ceiling; being thorough matters more.
  - Every mathematical error gets a comment.
  - Every feature gets at least one comment.
  - A student who did little may warrant only a few comments. Give each large missing section one comment.
- **Length.** One sentence or a quick statement is ideal. Use two sentences when a next step is needed. Three sentences should be rare.
  - "Excellent use of the second derivative to confirm a minimum – RC2"
  - "Units should be cm³ – RC3"
  - "This substitution uses 15000 instead of 12500 – CT2"
- **Tag.** End every comment with its feature code, e.g. " – CT2".
- **Tone.** Name errors plainly and include brief positives where they are earned. Don't do the work for the student.
- **Equations.** Put any equation in a comment on its own line as a real Word equation (OMML).
- **Spelling and grammar.**
  - Highlight in yellow; don't comment on them.
  - Run `merge_runs.py` from the docx skill first.
  - List in the notes any errors that couldn't be highlighted.
- **Template wording.** Never comment on it; note template problems in the teacher notes.
- **Anchoring.**
  - Anchor each comment on the exact paragraph, never inside a text box or `mc:Fallback`.
  - For a repeated error, comment on the first instance and say that it repeats.
- **Existing comments.** Strip them before annotating: `commentRangeStart`/`commentRangeEnd`/`commentReference`, the comments*.xml parts, and their rels and content-type entries.

## Step 7: Grade, then apply comparative judgement

1. **Grade each feature from the evidence.** Typical evidence includes:
   - justification of results (for example, a minimum test);
   - accuracy;
   - complete, non-circular general cases;
   - use of technology;
   - interpretation in context;
   - reasonableness and limitations;
   - notation;
   - communication;
   - the conjecture.
2. **Raw mean.** Average the values and round to a grade. A mean below 0.5 is I.
3. **Comparative judgement.**
   - Rank the class and place each student against the exemplar ladder and their neighbours in the ranking.
   - Where the mean grade doesn't match where the work sits, adjust it.
   - **Report every adjustment explicitly**: raw mean → adjusted final grade, with the reason.
   - Note any borderline result within about 0.3 of a grade boundary.

## Step 8: Build the outputs

1. **Commented copies.** For each file: strip old comments, run `merge_runs.py`, then `annot.py` (set `AUTHOR`, `INIT` and `DATE`), then `validate.py --original`. Keep the original file names.
2. **Grading document** (landscape .docx):
   - a method paragraph covering the scale, the mean and comparative adjustment;
   - a grades table: Student | each feature | raw mean | adjustment | final grade, colour-coded by band;
   - an assessment comments table: Student | final grade | comment. Each comment is at most 2 sentences, followed by: "Please read the rubric and the comments in your attached final feedback document for full feedback."
3. **Teacher-only marking notes**:
   - the calibration table;
   - the ranking, with a placement note for each student;
   - every adjustment and its reason;
   - borderline calls;
   - template issues;
   - spelling and grammar errors that couldn't be highlighted;
   - a summary of the integrity flags that points to the integrity report.
4. **Integrity check**, from Step 5.
5. **Delivery.**
   - **If the teacher gave folder access:** write every output (commented copies, grading document, marking notes and integrity check) into that one folder with `device_commit_files`.
   - **Otherwise:** zip them into `<task> – marked.zip` in /mnt/user-data/outputs and send it with SendUserFile.
   - **If a path can't be granted or the folder disconnects:** say so, attach the files in the chat, and ask the teacher to reconnect the folder with the desktop app's Add folder button.
   - Remind the teacher to open one file in Word to check the equation comments.

## Step 9: Report in chat

Keep the report short:

- the grades, marking those adjusted by comparative judgement;
- the adjustments and borderline calls;
- the integrity flags, by level, with one line of evidence each;
- where the files are.

## Gotchas

- Students copy template headings, so never comment on template wording.
- A draft may be resubmitted unchanged as the final.
- Copying shows up as identical unusual phrases, the same wrong method, identical long decimals, matching pasted fonts, or another student's comments left in the file. Correct values to many decimal places can be shared innocently, so check the value first.
- In an international school, pasted text in an unusual font with translated-sounding wording is often a translation tool rather than AI. Flag it as Low and ask about it.
- A missing minimum or maximum test, a circular general proof, or a model that switches problem partway through is a conceptual (CT) issue, not a notation one.
- Write the per-student specs (grades, summary, comments, highlights) to a file as you go, so the grading document and the comparative pass come from one source.