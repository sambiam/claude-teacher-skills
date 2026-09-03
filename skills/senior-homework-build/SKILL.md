---
name: "senior-homework-build"
description: "Build the weekly homework sheet for a Year 10, 11 or 12 maths class — one page consolidating the core skills taught that week, with spaced retrieval of earlier topics, exam-style questions in the course's format, and a separate worked-solutions sheet. Use for senior homework rather than per-lesson worksheets: 'homework for my Year 11s', 'weekly consolidation sheet', 'what should the Methods class do this week', 'they need something to practise over the weekend', 'a revision sheet for the senior class', 'exam practice on this week's work'. Reads the week's lesson decks and atomisations to work out what was actually covered rather than what was planned. Produces two DOCX files."
---

# Weekly homework for senior classes

One page a week, per senior class, consolidating what the week actually taught
and quietly keeping earlier topics alive.

Senior classes get this instead of a worksheet per lesson. In-lesson practice
comes from the textbook or Padlet with the reference on the last teaching slide
— see `standards/class-defaults.md`. A weekly sheet is better for these classes
because it can space and interleave in a way a per-lesson sheet structurally
cannot, and because a single predictable weekly artefact is one students
actually do.

## Find out what the week actually covered

Planned and taught are different, and building homework on the plan sets
questions on material the class never reached, which is worse than setting no
homework at all.

- Read this week's lesson decks and `<unit>/<lesson>/atomisation.md` files
- **Check the ink annotations** on the taught decks — `ink-progress` reads them
  and tells you where each lesson actually stopped
- Read the unit outline for where the week sits
- Read `classes/<class>/profile.md` for the course and any known weak atoms

If the week ended mid-topic, say so and cover what was reached. A question on
the atom they didn't get to belongs in next week's sheet.

## Shape

One page, A4 portrait, four sections. The proportions matter more than the
exact counts:

**1. This week's core skills — about half the sheet.** The atoms actually
taught, each getting its own questions before anything combines them. Start
where every student in the class can begin: homework attempted alone, at home,
with nobody to ask, needs a genuinely accessible entry point or it doesn't get
done at all.

**2. Spaced retrieval — about a quarter.** Four to six questions on material
from earlier in the term and earlier in the year. Choose deliberately: topics
that decay (anything with negatives, index laws, exact values), topics the last
test exposed, and topics this week's work will need soon. This is the section
students skip if it looks like filler, so keep it short and make it count.

**3. Exam-style questions — about a quarter.** Two or three in the format,
language and mark allocation of the actual course assessment. Include the mark
allocation, because for senior students learning to read `[3 marks]` as an
instruction about how much working to show is part of the course.

Take the style from past papers and the school's own assessments in the unit
folder rather than inventing it — `test-build` and `assessment-audit` know
where those live.

**4. One challenge.** Clearly optional and visually separated. An Open Middle
problem (`open-middle-build`) or a non-routine problem
(`non-routine-build`) connected to the week's work.

## Length

Aim for the homework time the course actually expects — usually 30–45 minutes
for a Year 11 or 12 class, less for Year 10. Ask if it isn't recorded in
`standards/class-defaults.md`.

Overlong sheets get half done or copied, and either way the feedback you get is
about stamina rather than understanding. If it doesn't fit, cut questions —
never shrink the font.

## Building it

Follow the `docx` skill for the mechanics and `worksheet-build` for the page
conventions:

- **Real Word equation objects (OMML)** throughout — true fractions,
  superscript indices, `×` for multiplication. Plain-text approximations look
  amateur next to a textbook and are ambiguous in places that matter.
- Working space sized to the work each question needs, decided per row.
- Section headings clear, minimal prose. Students met the explanation in class;
  every line of instruction costs working room.
- Readable in greyscale, and printable without losing an edge.
- Header carrying class, week, and due date.

Senior students often work digitally as well as on paper, so keep the layout
robust when printed at 90%.

## Solutions

A separate document, not an answer key appended to the sheet — these get handed
back or displayed, and a solutions section on the student sheet defeats it.

- Full working for the exam-style questions, laid out as a marker would want to
  see it, with the marks indicated at each stage. This is the part senior
  students learn most from.
- Final answers alone are fine for routine fluency questions.
- For the challenge, the route in rather than only the answer.
- Note accept-also forms — equivalent surds, factorised vs expanded — because
  senior work generates these constantly.

Generate both files from **one script with one shared question structure**, and
a flag that swaps the empty working space for the solution. Maintaining two
scripts is how answers end up attached to the wrong questions.

## Verify

Work every answer independently and check the algebra symbolically with
`sympy`: expand, factorise, solve, confirm claimed equivalences, test candidate
roots. Enumerate exhaustively for anything with a finite search space.

Then read every question again for whether it's well posed — a homework
question a student can't do because it's broken costs you their trust and their
weekend.

Render both files and look at them before delivering: page count, equations,
line wrapping, working space, nothing orphaned or overflowing.

## Output

```
<unit>/homework/<class>-week-<N>.docx
<unit>/homework/<class>-week-<N>-solutions.docx
```

Report: which atoms the core section covers, which older topics the retrieval
section revisits and why those, estimated time, and anything from the week you
deliberately left out because the class didn't get there.

