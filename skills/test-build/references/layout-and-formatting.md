# Layout and mathematical formatting

Australian/SACE-style assessment layout. The template in the templates folder
takes precedence over anything here — these are the conventions to apply where
the template is silent.

## Front page

- Assessment title
- Student name line
- Time allowed
- Materials allowed — state them specifically (calculator type, formula sheet,
  notes), not just "materials permitted". Students check this line, and it has
  to agree with what the questions assume.
- Instructions
- Total marks
- Marks table, if the template or prior papers use one

## Question layout

- Numbered questions with subparts, following the template's numbering scheme
- **Mark allocations go after the working space, right-aligned** — not beside
  the question number. A student reading the question shouldn't have the mark
  value competing for attention with the task.
- Clear working space after each question that requires working
- Page breaks placed so a question and its working space never split across
  pages
- Consistent font, spacing, and margins throughout
- **No student-facing meta-commentary.** Nothing like "only formula
  rearranging is required", "this question is routine", or "this is harder
  than the original". These are design notes; they belong in the report.

## Working spaces

1. Use table/grid working spaces, never ruled lines.
2. The grid spans most of the usable page width — add columns so it fills the
   width rather than leaving a narrow strip.
3. Enough rows for the working the question actually needs.
4. **No working grid** under questions answered directly into a table, graph,
   diagram, or a single-step response area. A grid there just confuses the
   student about where to write.
5. For two-way tables, frequency tables, summary tables and similar completion
   questions, provide the table only, unless substantial written working is
   genuinely required.
6. Leave a small visual gap between a provided table or diagram and any
   working space that follows it.
7. For box plot questions, don't pre-label the groups or the scale unless the
   prior papers do and the task requires it. Constructing the scale is often
   part of what's being assessed.

### How much room

Teachers notice cramped boxes immediately — a student who runs out of room
either writes smaller and illegibly or works on the desk and transcribes the
answer, which loses them method marks. As a starting point, in points of
height:

| Question type | Working space |
|---|---|
| One-line recall or a single value | 25–40 |
| Single-step solve or expand | 45–70 |
| Two-step solve, shown line by line | 100–150 |
| Error analysis, explain-and-correct | 75–95 |
| A 4-mark multi-step problem | 200–250 |

Multi-column grids are more economical than a stack of full-width boxes and
match how faculties usually lay out a run of similar questions — put the
question label and expression inside each cell rather than above the grid.

## Page discipline

These are the faults that get reported back, and none of them are visible in
the source document:

- **Nothing may collide with the header.** School headers are often floating
  frames that reserve no vertical space, so the first body paragraph lands on
  top of the title block. Open the body with an empty spacer paragraph.
- **No question separated from its working box or its marks line by a page
  break.** Set `cantSplit` on grid rows and `keep_with_next` on the paragraphs
  inside working cells. That handles most cases; where a renderer still
  orphans a marks line, adjust the box heights above it until each page ends on
  a complete question.
- **No blank or nearly-blank final page.** A stray trailing marks line makes
  one, and so does a page holding a single short question. Rebalance the
  working-space heights until the last page is genuinely used, or pull its
  content back onto the previous page.
- **Respect any stated page limit.** Check the rendered page count, not the
  source. A paper that runs to five pages when four were asked for costs the
  teacher a reprint.

## Mathematical formatting

All mathematics, in both documents, must be equation-editor quality.

- Fractions render vertically with a horizontal bar
- Exponents raised correctly
- Roots with proper radical notation
- Brackets, subscripts, function notation, inequalities and equations clear
  and correct
- **No plain-text shortcuts** — not `x^2`, not `sqrt(x)`, not `a/b` for
  anything but a trivial fraction
- Watch for `¿` in the rendered PDF. It means an equation object was malformed
  — almost always one that starts or ends with `=`, or an unbalanced fragment
  inside a bracket. It renders correctly in Word and breaks everywhere else,
  so it only shows up if the PDF is actually inspected.
- Exact values where required; rounding instructions stated explicitly

## Diagrams and graphs

- Correct proportions; axes not stretched
- Graph grids square, clear, and labelled only where the labelling isn't part
  of the task
- Every value the question refers to appears on the diagram
- Diagrams sized so they're readable after photocopying

## Building the document

Use the docx skill for the mechanics. Points that bite on assessment papers
specifically:

- Tables need `columnWidths` on the table and `width` on every cell, both in
  DXA — percentage widths break the grid alignment.
- Set explicit row heights on working grids so adding solution text later
  doesn't reflow the page and break alignment between the two documents.
- Use a paragraph bottom border for horizontal rules, not a one-row table.
- Build from the template rather than recreating its look — copy its styles,
  header, and front page rather than approximating them.
