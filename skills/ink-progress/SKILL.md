---
name: ink-progress
description: "Work out how far a lesson actually got by reading the ink annotations saved in a PowerPoint deck. Use this whenever you need to know where a previous lesson stopped, whether a class finished a deck, how much of a deck was covered, or whether to continue a lesson or move on to the next one. Trigger on any mention of 'where did I get up to', 'did we finish', 'last lesson's slides', 'annotated deck', 'pen marks', or when preparing a follow-up lesson that continues from a previous one. Also use before rebuilding or modifying a deck that has already been taught, so existing annotations aren't destroyed."
---

# Reading lesson progress from ink annotations

Ink written on slides during a lesson is the most honest record of what was
actually covered — it is made in the moment and nobody has to remember to log
it. This skill turns that ink into a progress signal.

## What the ink can and cannot tell you

Be careful here, because it's easy to over-read the evidence.

**Reliable (extract this):**
- Which slides carry ink, and which slide is the *last* one that does
- How many strokes are on each slide
- Where on the slide the ink sits (bounding box)

**Not reliable (do not claim it):**
- What the ink says. Handwriting recognition on maths working is poor, and a
  stroke could be a worked solution, a correction, a student's wrong answer
  being crossed out, or a doodle.
- Whether the class *understood* the annotated slide.
- Whether an unannotated slide was skipped or simply didn't need the pen.
  Plenty of good teaching leaves no marks — a slide that's read aloud,
  discussed, or answered orally looks identical to one never shown.

Treat the ink as an upper bound on progress, and say so when you report it.

## Running the report

```bash
python scripts/ink_report.py "path/to/deck.pptx" --verbose
```

Add `--json` when another step needs to consume the result. The script is
stdlib-only, so it needs no installs. It reads the deck's content types to find
InkML parts, maps them to slides through each slide's relationships, and orders
slides by `<p:sldIdLst>` (real presentation order) rather than by filename,
which matters on any deck whose slides have been reordered.

Output looks like:

```
Slides: 22
Annotated: 3, 4, 5, 8, 9, 11, 12  (94 strokes total)
Last annotated slide: 12
Slides after it: 10
```

## Turning the report into a recommendation

Read the deck's content alongside the ink — `markitdown deck.pptx` gives you
one text block per slide. The ink tells you *where*; the slide content tells
you what that position means. A stop at slide 12 of 22 means something very
different if slide 13 starts a new sub-topic than if slides 13-22 are all
independent practice.

Work through these in order:

1. **Locate the stop.** Last annotated slide, and how many slides follow it.
2. **Classify what follows.** Is the next slide a continuation of the same
   idea, the start of a new concept, worked examples, or practice? Read the
   titles and content.
3. **Check the density of the annotated region.** Slides with many strokes
   generally mean examples were worked live. A long tail of lightly-inked
   slides late in the deck often means the lesson was rushed at the end —
   worth flagging, because rushed content usually needs revisiting.
4. **Look for the gap pattern.** Ink on slides 3-5 and 11-12 but nothing
   between suggests slides 6-10 were skipped, not that they were covered
   silently. Report the gap; don't silently assume either reading.

## Reporting format

Always report evidence and inference separately, so the teacher can overrule
you cheaply. Use this shape:

```
## Where the lesson stopped
Deck: <filename> (<N> slides)
Last ink: slide <X> — "<slide title>"
Remaining: slides <X+1>-<N> — <one line on what they cover>
Coverage gaps: <slides with no ink between inked slides, or "none">

## Reading of it
<2-3 sentences: what the stopping point suggests, including stroke density
and whether the stop lands mid-concept or at a natural boundary>

## Recommendation
<Continue | Move on | Continue briefly then move on>
Because: <one or two sentences>
Confidence: <high | medium | low> — <what would change it>
```

Recommend **continue** when the stop lands mid-concept, when the remaining
slides include worked examples the class hasn't seen, or when the last inked
slides are thinly annotated in a way that suggests rushing.

Recommend **move on** when the stop lands at a topic boundary with only
practice or consolidation remaining, and that practice can be picked up as
homework or a starter.

When the two readings are close, say so rather than manufacturing certainty —
"either is defensible, here's the trade-off" is more useful than a confident
wrong call.

## When no ink is found

This is common and not an error. Report it plainly and fall back to other
evidence rather than guessing: ask which slide the lesson reached, check
whether a different copy of the deck was projected, or look at what students
completed in the questions folder. Never infer full coverage from absence of
ink — an un-annotated deck is uninformative, not evidence of a finished lesson.

## Before modifying an annotated deck

Ink is data the teacher may still want. Never rebuild in place over a deck
that carries ink. Copy it to an archive location first (e.g.
`archive/<date>-<class>-<topic>.pptx`) and work on the copy, so the record of
what was taught survives.
