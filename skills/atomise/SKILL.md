---
name: atomise
description: "Break a mathematics lesson, topic or exam question into its teachable atoms — the full chain from initial prompt to final answer, each atom typed as a fact, categorical, transformation or cognitive routine, each marked Assume / Check / Teach, with the misconceptions and hidden decisions surfaced. Use whenever planning what to teach rather than how to present it: 'atomise this', 'break this topic down', 'what do students need to know before', 'why do they keep getting this wrong', 'what am I actually teaching in this lesson', 'is this one lesson or two', or before building any deck, worksheet or teaching sequence. Also use when a lesson keeps failing and the reason isn't obvious. Produces an atomisation table plus a prerequisite map."
---

# Atomising a mathematical idea

The job is to find the joins a fluent teacher can no longer see. Expertise
makes the components of a routine invisible, so the routine gets taught as one
move and a third of the class fails silently at a join nobody knew was there.

Read `standards/atomisation.md` in the teaching folder before starting — it
carries the specification and the worked references, and it overrides anything
below. If it isn't there, work from this file and say which decisions you made
on the teacher's behalf.

## What you are producing

A markdown file at `<unit>/<lesson>/atomisation.md` containing four things: the
chain, the teaching decision on each atom, the misconception analysis, and the
prerequisite map. Then a short verdict in chat about whether this is one lesson.

## A — Establish the target

Find the actual finishing point before decomposing anything. Read the unit
outline, the textbook exercise, and any past assessment questions on this topic
in the folder, and write down **the exam-standard question a student should be
able to answer by the end**, in the form they will meet it.

This matters because atomisations built from a topic name drift to the tidy
version of the topic. The atomisation of "solve simultaneous equations" is a
different shape depending on whether the terminal question says *"Solve"* or
*"Solve the simultaneous equations"* — the first hides a decision the second
gives away.

Read `classes/<class>/profile.md` if a class is named. Which atoms can be
assumed is a fact about this class, not about the topic.

**Quote the terminal questions from the real papers and cite where each came
from.** A terminal question you invented is a guess about the assessment; one
lifted verbatim from last year's Test A is the assessment. Read every past test
in the topic folder, not just the most recent, and note where versions differ —
if Test B has a section Test A doesn't, that is a scope question for the
teacher, not something to resolve yourself.

When the teacher asks for a ceiling **beyond** the test, keep the two separate
and label them. Write the beyond-test terminal question *and* the hardest item
that actually appears on the paper, and mark which is which, so nobody later
mistakes an extension for a requirement.

**Also read the deck that was last taught**, not just the outline. It tells you
the real ceiling the class has met, which is what the first Teach atom has to
build from — and it is often lower than the outline implies. Check it for saved
ink with `ink-progress`; if there is none, say in your report that coverage is
assumed rather than verified.

**Also read the deck for the next lesson in the sequence, if one already
exists.** That's the other end of the ceiling: the deck that was last taught
tells you where the class's floor actually is, but the next lesson tells you
what this one has to reach. A chain that stops short of what the next lesson
already assumes secure is a gap, and looking only backward will never surface
it — you'll atomise a clean, internally consistent lesson that quietly doesn't
connect to the one immediately after it.

## B — Build the chain

Work from the terminal question backwards, or forwards from the prompt —
whichever you find easier — but produce the full chain: every atom between the
question as written and an answer that would earn the mark.

Record it as a table. `#0` is the initial prompt exactly as a student meets it;
each row after is one atom.

| # | Example prompt | Example response | Type | Capability |
|---|---|---|---|---|

Two habits that decide whether the atomisation is any good:

**Write each atom's prompt so it isolates that atom alone.** If you can't write
a question that tests only this, it isn't an atom yet — it's a phase, and it
needs splitting.

**Name the capability, not the topic.** "Identify pairs of equations with a
common coefficient" rather than "common coefficients". A capability can be
checked; a topic can only be covered.

Then look for the atoms that fluency hides. In practice they cluster:

- **The decisions.** Add or subtract these equations? Which side to substitute?
  Is this the adjacent side? Every decision is a categorical atom and they are
  the single most under-taught kind. If your chain contains no categorical
  atoms, you have almost certainly missed some.
- **The final form.** Writing `66 units²` rather than `66`. Exact form vs
  decimal. Three-figure bearings. Students lose marks here and it vanishes from
  nearly every atomisation written by an expert.
- **Recognising the object at all.** Before any method comes "is this the kind
  of thing that method applies to".
- **Notation doing silent work.** Juxtaposition meaning multiply, the fraction
  bar meaning divide, the minus sign as both sign and operation. On a geometry
  or diagram-based topic this is just as often a mark drawn on the figure
  rather than a symbol in the algebra: tick or hash marks for equal sides,
  arrows for parallel sides, arcs for equal angles, a dash for a construction
  line. It's easy to only look for the algebraic kind and miss that the
  diagram itself is carrying an unatomised fact.

Type every atom — Fact, Categorical, Transformation, Cognitive routine — using
the tests in the standard. The type is not filing; it determines which teaching
sequence applies, so a mistyped atom gets taught the wrong way.

Where the chain runs longer than about six atoms, mark **sub-chains**: runs of
two or three consecutive atoms worth practising together before the whole
routine. Prefer sub-chains built from the end backwards, so every student
attempt finishes the problem.

## C — Decide on each atom

Every atom gets exactly one verdict. This is the step that turns analysis into
a lesson.

**Assume** — they can already do it. Record what happens if you're wrong, which
is nearly always "the lesson fails silently for those students and it will look
like they can't do today's topic". Mark it **risky** when the atom is more than
a year old, was taught by someone else, involves negatives, fractions or
notation, or when the class profile gives any reason for doubt. A risky
assumption you're keeping is a legitimate choice; an unexamined one isn't.

**Check** — load-bearing enough that two minutes of verification costs less
than discovering the gap mid-lesson. These become the prior-knowledge check.

**Teach** — new, or previously taught and known to be insecure.

Then count the Teach atoms and say so plainly. **More than two or three is not
one lesson.** Telling the teacher "this is three lessons, and here is where the
boundaries fall" is often the most valuable thing this skill produces, and it
is the finding people most want to be talked out of — so state it early, give
the split, and let them decide.

Give the split as a table with dates against it, taken from the timetable and
the unit outline. Teachers routinely have a lesson they haven't counted, and a
scope problem that looks fatal in the abstract often dissolves once the
available periods are on the page.

### Then break the Teach atoms down by type — this is the headline

Count how many of the Teach atoms are **categorical**. When a teacher says some
version of *"they can do the steps but they can't do the process"*, or *"they're
fine in the exercise and fail the test"*, the answer is almost always that the
categorical atoms — the decisions — were never taught, because expertise makes
decisions invisible in a way it doesn't make procedures invisible. The teacher
demonstrated *how* and assumed *which*.

So don't just report twelve Teach atoms. Report that five of the twelve are
decisions, name them, and say that the class can already execute the other
seven — that is what "they can follow inverse operations but struggle with the
solving process" actually means, and it changes what the lesson should spend
its time on. A count by type is a diagnosis; a count is a number.

### Record what the teacher cuts, and why

The scope verdict usually comes back with atoms removed, merged or moved. Write
the revisions into the file as a table — atom, status, whose call it was — and
keep the original chain intact underneath. Two reasons: `teaching-sequence` and
`deck-build` read this file and will otherwise silently reinstate a cut atom,
and next year the reasoning is worth more than the decision.

When an instruction is ambiguous — an atom kept whose home was just deleted, a
cut that removes the prerequisite for something retained — resolve it as best
you can, put your interpretation in a visible box at the top of the file rather
than a footnote, and say plainly what would change if you read it wrong. Do not
quietly pick one and move on.

## D — Misconception analysis

For each atom marked Teach or Check, write what students actually get wrong,
and be specific enough that it could become a distractor.

The test for whether a misconception is real: **can you write the wrong answer
a reasonable student would produce?** If you can, it belongs in the file and
later in a diagnostic question. If you can only describe a vague confusion, you
have a hypothesis, not a misconception — mark it as such rather than dressing
it up.

Where the topic has a well-known error pattern, name it and say what it
indicates. Where a wrong answer could come from two different errors, say so:
that's a signal the practice needs to separate the atoms.

Look particularly at:

- **Definitional edges** — is a square a rectangle, is x² + 9 factorisable, is
  a bearing always from north. Students build the concept from the examples
  they were shown, so a narrow example set produces a concept that fails at the
  boundary.
- **Reversals** — a student who can do the forward transformation but not the
  inverse has learned a procedure, not a relationship.
- **Degenerate cases** — where a special case teaches a rule that breaks
  generally.

## E — Prerequisite map

A small diagram: prior capabilities feeding in on the left, the target idea in
the centre, what it unlocks on the right. Follow `Purpose-example.pdf`.

Name nodes as capabilities. Prior nodes should be exactly the atoms you marked
Check — if a prior node can't be checked with a quick question, it isn't really
prerequisite and shouldn't be on the diagram. Include future nodes the class
will recognise and care about; that's what makes the map worth showing them.

Record it as a list of edges in the markdown. `lesson-rationale` turns it into
slides.

## Output

Write `<unit>/<lesson>/atomisation.md`:

```markdown
# Atomisation: <lesson>
Class: <class>, Year <N> | Terminal question: <the exam-standard question>

## Chain
| # | Prompt | Response | Type | Capability | Decision |

## Teaching decisions
### Teach (N atoms, of which M are categorical)  — with a note if N > 3
### Check
### Assume — risky ones first, each with what breaks if wrong

## Scope verdict
Is this one lesson? If not, the split, with dates from the timetable.

## Revisions the teacher made
| Atom | Status | Note |

## Misconceptions
| Atom | What students do | Wrong answer it produces | Confidence |

## Prerequisite map
Prior → target → future, as edges

## Sub-chains
```

Then report in chat: how many atoms, how many marked Teach **and how many of
those are categorical**, whether this is one lesson, the two or three riskiest
assumptions, and anything you couldn't resolve. Don't reprint the table — it's
in the file.

Lead with the type breakdown if the categoricals dominate. It is the finding
that changes what gets built, and it is the one a teacher can act on without
reading anything else.

**Report before building.** The scope verdict and any ambiguous instruction go
to the teacher while they are still cheap to act on — not after a deck exists
and the sunk cost argues for keeping it.

## Working from an existing deck or worksheet

When the lesson already exists, atomise **what it actually teaches**, then
compare against the chain the terminal question needs. The gap between the two
is the finding. A deck that teaches five of seven atoms and assumes the other
two — with those two being the decisions rather than the procedures — is the
usual explanation for a lesson that goes well and assesses badly.

## Next steps

- `teaching-sequence` designs how each Teach and Check atom gets taught
- `deck-build` renders that into slides
- `practice-select` chooses the practice for the atoms
- `lesson-rationale` turns the prerequisite map into student-facing slides

