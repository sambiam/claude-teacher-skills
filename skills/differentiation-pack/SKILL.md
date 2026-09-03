---
name: differentiation-pack
description: "Assemble the support and extension materials that let every student in a class access a lesson — guided notes for students working with an SSO, scaffolded entry tasks, and genuine extension for students who finish early. Use whenever preparing materials for a mixed class, when an SSO or support staff member needs something to work from, when a lesson needs an access point for struggling students, or when fast finishers need something better than 'do the next exercise'. Trigger on 'differentiation', 'extension', 'guided notes', 'SSO', 'support materials', 'students who finish early', or 'how do I make this accessible'."
---

# Building the differentiation pack

Two failure modes to avoid. One is extension that's just more of the same
questions — that reads as a punishment for working quickly. The other is
support that removes the mathematics — a scaffold so heavy the student
succeeds at filling gaps without ever doing the thinking.

Read `classes/<class>/profile.md` for the cohort before building anything.

## Guided notes

These go to students who need the structure, and to whoever is supporting
them. They mirror the lesson deck exactly so a supported student is working on
the same mathematics as the room, at the same moment, rather than on a
parallel track.

Build them by taking the deck and removing selectively:

- **Keep the structure.** Every heading, definition, and worked example from
  the deck appears in the same order. A student should be able to follow the
  board and their notes simultaneously.
- **Gap the notes, don't blank them.** Definitions appear with key terms
  missing. Worked examples appear with the first steps complete and later
  steps blank. The student writes the mathematically load-bearing parts, not
  the connecting words.
- **Fade across the sheet.** The first worked example is mostly complete; the
  last has only the first line given.
- **Leave real working space.** Ruled lines sized to the actual work.
- **Never gap something the student can't recover.** If a term is missing and
  it isn't on the board when the student needs it, the sheet fails. Gaps must
  be fillable from what's being said or shown.

Write a short SSO-facing note at the top or on a cover page — this is the part
that most often gets skipped and most determines whether the support works:

- What the student should be able to do by the end
- The prerequisite skills the lesson assumes, so the SSO knows what to shore
  up if the student is stuck at a lower level
- The specific misconception to watch for on this topic
- What to prompt with rather than what to tell — two or three questions the
  SSO can ask that move a stuck student forward without giving the answer
- Which questions are the priority if time runs short

Keep this practical and brief. SSOs are supporting in real time, not reading a
document.

## Scaffolded entry

For students who can't start the core practice, provide a route in rather than
a different task:

- A worked example directly parallel to the first core question
- The first two or three questions broken into their steps as separate parts
- A reference strip — the formula, the method summary, the notation — on the
  same page, so the student isn't hunting through a book
- Where the barrier is arithmetic rather than the concept being taught, use
  friendly numbers so the target skill is what's being practised

The aim is that they do the same mathematics with more support, then rejoin
the class set.

## Extension

Extension should change the *kind* of thinking, not the quantity, and it
should read as a task worth doing — not a worksheet with a rationale attached.

### Say less

The student opens this after finishing the core work, not after a briefing.
Cut anything that explains the task rather than posing it:

- No subtitle or standfirst explaining why the task exists ("For students who
  finish early", "Today's lesson was about deciding what to do, not just
  executing the steps..."). If the framing would help, it belongs in what you
  say to the student when you hand it out, not on the page — write it in your
  own report back, not into the document.
- No sentence that tells the student the task is hard, rich, or different
  from what they've been doing. Let the task demonstrate that.
- Keep only what a student needs to attempt the question: the skeleton or
  equation, the rule or constraint, and — only where the task is genuinely
  unfamiliar in form (e.g. Open Middle, a literal equation) — one short line
  naming the form. "Using the digits 1–9, at most once each, fill in the
  boxes" earns its place; "this task will push you into territory you won't
  meet until senior maths" doesn't.
- A short line of context is earned when it changes how the student reads the
  question (e.g. the two data points needed to set up the Temperature task
  below) — never when it's commentary on the task itself.

### Ramp the difficulty inside the pack, not just across it

A pack with one very open task and nothing else asks a student to go from
"just finished the class exercise" to "cope with total ambiguity" in one
step, which reads as too open too fast. A pack that's just larger numbers on
the same procedure reads as punishment. Sequence two or three tasks so the
*mathematics* stays close to what was just taught while the *demand* escalates:

1. **Familiar procedure, hidden path.** The mechanics are exactly what the
   student just practised — nothing new to learn — but the route to the
   answer isn't signposted. This is what **Open Middle** problems are for:
   take the lesson's equation skeleton and blank out the numbers (see
   `open-middle-build`). A student who can solve `☐x + ☐ = ☐x + ☐` for any
   digits can attempt "make x as large as possible" immediately; finding the
   arrangement that does it requires understanding the equation as a
   relationship, which is a genuinely different demand from executing the
   method. Prefer this as the *first* extension task, not a "if they finish
   everything else" bonus — it has no ceiling and every student can start.
2. **New context, same decisions.** A problem that requires the same
   decisions taught in the lesson (which side to collect to, what sign to
   divide by, how to read a fraction bar) but applied inside an unfamiliar
   setup — a real-world model, a literal equation, a problem the student has
   to translate into an equation themselves rather than one handed to them
   ready-formed. This is harder than task 1 because the student must first
   decide *what equation to solve*, not just how to solve it.
3. **Extra Hot, optional.** Label it exactly that — `worksheet-build` uses the
   same name for the same idea, so keep the convention consistent across
   documents. Only include one if there's a natural next step: genuinely
   higher-level mathematics the lesson's method reaches cleanly, typically a
   year or two ahead.

   **A higher-level equation handed over to "solve for x" is not extension for
   an advanced student, however far ahead the content is** — if the method is
   just "expand, then use the routine already taught," it's fluency practice
   wearing older content as a costume, and an advanced student will clock that
   immediately. The tier-1 principle still has to hold at the higher level:
   familiar-once-you-see-it mechanics, but the *path* to the answer is not
   signposted. Concretely, that usually means turning the higher-level idea
   into an existence, construction or proof question rather than a "solve
   this" question — "find an arrangement where this has no solution", "show
   this can never be true for every x", "for what values of the parameter
   does this have two solutions, one, or none" — over "solve this specific
   equation once you've expanded it." Open Middle again works well for this:
   take the higher-level skeleton (e.g. `(x + ☐)(x + ☐) = (x + ☐)(x + ☐)`) and
   set an existence/impossibility objective rather than a maximise/minimise
   one, verified the same way — by exhaustive search, not by constructing one
   example and assuming it generalises.

   Visually separate it from the rest of the pack and keep it to one problem
   with at most a short second part, rather than a full second exercise — the
   point is one genuinely higher-ceiling question, not more content.

An extension pack does not need all three tiers every time — two or three
well-chosen, well-sequenced tasks beat a longer set where the difficulty jump
between them is uneven or where the last one is just there to fill the page.

### Good sources of extension, by tier

- **Tier 1 (hidden path, familiar mechanics):** Open Middle constrained-digit
  problems — hand this to `open-middle-build`, which finds the true optimum
  by exhaustive search and writes up the insight. This is close to always the
  right first extension task for a procedural topic.
- **Tier 2 (new context, same decisions):**
  - **Reverse the question.** Give the answer, ask for the problem. "The
    solution is x = 4. Write three different equations with that solution,
    each requiring a different one of today's decisions."
  - **Generalise.** "You've done four of these. What happens in general? Will
    it always work?"
  - **Connect.** A problem that requires setting up, not just solving, an
    equation — linking this topic to a real context or one taught earlier or
    later in the year. `non-routine-build` is built for exactly this and is
    usually a better first move than writing one from scratch.
- **Tier 3 (genuinely new mathematics):** the next year or two of the same
  idea — a literal equation, a parameter, a case the method extends to but
  the class hasn't met. `non-routine-build` again, or curated from an
  external source (below).

**Avoid manufactured error-finding as extension.** "Spot the mistake" is a
legitimate *diagnostic* task for consolidating a lesson's known misconceptions
(it belongs with the core practice or `practice-audit`'s coverage, not here),
but a fabricated error that just restates "remember to do it to both sides"
is not extension — it's the same demand as the lesson, dressed up. Only use
find-and-fix as an extension task when the error itself is genuinely subtle
or reveals something non-obvious (e.g. why multiplying both sides by an
expression containing the unknown can introduce a false solution) — not when
it's a slip a student in the core group would also make.

### Curate before you write

Search for a task that already exists and has been trialled before writing a
new one — this is the highest-value step in building extension, not an
afterthought. Check, in order:

1. **The unit folder** — an existing extension resource, a prior year's
   enrichment sheet, textbook enrichment sections. If found, verify it's
   actually complete and correct before reusing it (render it; broken or
   half-finished resources do turn up — check equations are actually present,
   not blank boxes left by an earlier incomplete attempt).
2. **The school's other topic folders** — a rich task built for a related
   topic may adapt directly.
3. **External sources**, searched and fetched with `WebSearch` / `WebFetch`:
   - **nrich** (nrich.maths.org) — search `site:nrich.maths.org <topic>`, or
     browse the topic's tag page (e.g. `nrich.maths.org/tags/<topic>`). Its
     "Getting Started" and challenge-level ratings make it easy to match to a
     year group. Read the actual problem page, not just the search snippet —
     some content is image-only and needs a direct fetch or a judgement call
     to skip.
   - **Don Steward's median blog** (median-don-steward.blogspot.com, older
     posts at donsteward.blogspot.com) — search
     `site:median-don-steward.blogspot.com <topic>`. Excellent for genuinely
     non-routine numerical/algebraic puzzles; content is often images, so
     confirm you can actually read the task before citing it.
   - **UKMT** past Junior/Intermediate Mathematical Challenge questions — good
     for short, sharp reasoning problems at the right reading level.
   - **Open Middle** (openmiddle.com) — pre-built constrained-digit problems;
     check the stated answer against `open-middle-build`'s exhaustive-search
     standard before trusting it, some published answers are wrong.
   When adapting a found task, keep its structure and change only what's
   needed to fit the lesson's numbers or context — don't rewrite it into
   something unrecognisable, and always verify the adapted version's answer
   independently (see Verify, below) rather than trusting the source.

Say clearly, in your report back, which items were found (and where) and
which were written from scratch — the teacher needs to know what has already
been trialled with students versus what's new.

## Formatting the documents

Build DOCX extension and scaffold materials the same way `worksheet-build`
does — read its `references/docx-production.md` before writing the build
script. In particular:

- **All mathematics is a real Word equation object (OMML)**, using the `docx`
  library's `Math`/`MathRun`/`MathFraction`/`MathSuperScript` classes — never
  plain text approximations (`3/5`, `x^2`, `*`). A blank box where an
  equation should be is worse than no document; always render the file to
  PDF and read it back before delivering (`pandoc -t markdown file.docx` to
  check the equations translated correctly, then convert to PDF and view the
  pages) — see `docx-production.md`'s render-and-check loop.
- **Open Middle boxes** render as `☐` (U+2610) in a bold `TextRun` around 34
  half-points with a space either side — not inside the equation's math zone,
  and not drawn as a table or shape.
- **Working space** sits directly under each question, sized to the work that
  question actually requires (a one-line check needs far less room than a
  multi-step derivation) — see the working-box sizing table in
  `worksheet-build`'s SKILL.md.
- Verify every answer independently (symbolically with `sympy` where
  possible; by exhaustive search, never intuition, for any Open Middle
  optimum) before it goes in an answer sheet. Do this even for algebra you're
  confident in — a sign slip in `x = (d−b)/(a−c)` vs `x = (d−b)/(c−a)` is easy
  to make by hand and easy to miss on a read-through; `sympy.solve` catches it
  in one line and costs nothing.

### Answer sheets

An answer sheet built as a wall of prose ("collect the x terms, then divide
by the coefficient, giving...") is much harder to mark against than the
student's own working, which defeats the point of providing one. Mirror
`worksheet-build`'s answer-sheet standard exactly:

- **Every step of working is its own real equation object**, stacked
  vertically in its own paragraph — never an arrow-chain run into one line of
  text (`C − 1.8C = 32 → −0.8C = 32 → C = −40`). A teacher scanning down the
  page should see the same shape of working they'd expect from a student:
  one line per step, not a sentence that happens to contain some algebra.
- **The final answer gets its own bolded line** (`x = 8`, or the correct
  variable name — don't default to `x` when the question is solving for a
  different letter, check which one it actually is), followed by a **Check**
  line that substitutes back in and ends in a tick (`✓`), the same visual
  marker used for verification throughout this school's materials.
- **The filled-in working sits inside a bordered box in the same position and
  width as the empty box on the student page** — same visual object, filled
  rather than blank — so the answer sheet reads as the student sheet
  completed, not a separate document with its own layout.
- Reasoning that isn't itself a step of algebra (the Open Middle insight, the
  near-miss, why a cancellation always happens) goes as ordinary text
  *outside* the box, immediately below it — the box is for working, prose is
  for explanation.
- Render and read back every answer page before delivering, the same as the
  student page — `pandoc -t markdown` to confirm each equation reads as
  intended, then the rendered PDF to check nothing overflows its box and nothing
  reads as a plain-text approximation.

## Output

Write into the lesson folder:

```
<unit>/<lesson>/guided-notes-<topic>.docx
<unit>/<lesson>/guided-notes-<topic>-SSO-BRIEF.docx   (or as a cover page)
<unit>/<lesson>/extension-<topic>.docx
```

Report which lesson atoms the guided notes cover, what each extension task
asks for and which tier it sits at, and where anything was sourced from
(unit folder, other topic folder, nrich, Don Steward, UKMT, Open Middle)
rather than written from scratch.
