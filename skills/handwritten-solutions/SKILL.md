---
name: "handwritten-solutions"
description: "Write worked solutions in Sam's own handwriting as real Word ink over the working spaces of a homework, practice test, test or worksheet .docx, using the methods taught in his lessons. Used by every skill that makes solutions or answer sheets."
---

# Handwritten worked solutions (ink over the paper)

Produces worked solutions that look like Sam wrote them with his pen on the student paper:

| Output | What it is |
|---|---|
| `<paper name> - SOLUTIONS (handwritten).docx` | The student paper with every working grid filled with **Word ink objects** (one per line of working, one per tick). In Word they are real ink: Draw tab → Eraser / Lasso Select to fix a line, recolour, or delete a tick. The *Name:* field reads **WORKED SOLUTIONS (teacher copy)** in red. |
| `<paper name> - SOLUTIONS (handwritten).pdf` | Print copy, rendered through each ink object's picture fallback. |

It is **the solutions step for every skill that produces worked solutions or an answer sheet**: `test-build`, `practice-test-build`, `exam-revision-homework`, `senior-homework-build` and `worksheet-build` all build the student paper and then hand over to this skill. Their content rules still hold: solutions sit in the working space of the actual paper, step-by-step working for multi-step questions, final answers with units, and **one tick per mark** (method ticks on the method line, answer ticks on the answer line).

The handwriting comes from a glyph library harvested from Sam's own ink (Year 10 Methods solution booklets in Word and the Year 11 Methods lesson decks). Every character is drawn from one of several real samples of that character, never the same sample twice running, with small random changes to size, slant and baseline, so no two lines look stamped.

## Step 1 — Find the paper and confirm the method

1. Get the **finished student paper** (`... - printable.docx` for homework sheets; the student version of a test). Build only from the final paper: the ink is anchored to its grid cells.
2. If typed solutions already exist (`... - SOLUTIONS.docx`), read them for mark allocation and answers, then **verify every answer yourself** before inking it.
3. **Check how each method was taught.** Find the lesson decks for each topic in the class folder (e.g. `11 Methods/05 Differential Calculus Ch 14 15/`), read slide text and Sam's ink on the worked-example slides (the `ink-progress` skill reads deck ink; or render `ppt/ink/*.xml` traces over the slide). Use the taught method, written the taught way, even when a shorter route exists. Known conventions:

| Topic | How Sam teaches it — reproduce this |
|---|---|
| Tangent | `y = f'(a)(x - a) + f(a)`: find f(a), find f'(x), evaluate f'(a), substitute, simplify. Never y − y₁ = m(x − x₁) or y = mx + c. |
| Normal | `y = -\frac{1}{f'(a)}(x - a) + f(a)` |
| Differentiating | Rewrite every term in index form first (√x = x^½, 6/x² = 6x⁻²), then `n × coefficient x^{n-1}` term by term, then simplify back to positive indices / surds. |
| Average rate of change | List a, b, f(a), f(b), then `ROC = \frac{f(b) - f(a)}{b - a}` |
| Instantaneous rate | f'(x), then substitute. |
| Stationary points / max / min | f'(x) = 0 → solve (factorise) → sign diagram → substitute into f → state `max = (x, y)` / `min = (x, y)` |
| Degrees ↔ radians | `× \frac{\pi}{180}` and `× \frac{180}{\pi}` |
| Arc / sector (radians) | `l = \theta r`, `A = \frac{1}{2}\theta r^2`; perimeter = 2r + l. Degrees versions `\frac{\theta}{360} × 2\pi r`, `\frac{\theta}{360} × \pi r^2`. Keep unrounded values until the final answer. |
| Surds | Split out the square factor (`\sqrt{25 × 3}`); rationalise by multiplying top and bottom by the conjugate written in brackets. |
| Exponential factorising | Write terms with prime bases, find the HCF (`2^n × 2^3 + 2^n = 2^n(2^3 + 1)`), or spot a perfect square / DOTS (`(2^x)^2 - 3^2`). |
| Expanding a square | Write it out as two brackets first: `(a + b)(a + b)`. |

If a topic is not in the table, look it up in the decks before writing anything — and add the convention to this table when Sam confirms it.

## Step 2 — Sam's notation and layout (follow it)

- Red ink (#E71224), fine pen (0.042 cm). Upright and **neat but still handwritten** (Sam, Nov 2026: the first draft was "a little bit too messy"). `NEAT = 0.85` keeps only the most typical samples of each character, straightens each sample's slant towards his usual lean, steadies size, baseline and spacing, levels fraction bars, and spreads lines evenly into spare box height. Raise it towards 1 for tidier; never below about 0.5.
- **Smooth, steady strokes — no shake** (Sam, Nov 2026, twice: "there shouldn't be as much shaking in the writing", then "still too messy and shaky … similar to my writing but neat"). Every stroke is `neaten()`ed: smoothed, reduced to the few points that carry its shape, and redrawn through them as a spline — his letter shapes, written with a steady hand (corners of 4, 7, 1 and ticks kept). The PDF picture fallback is drawn 4× oversize with round joins and downsampled, so edges are clean rather than jagged. There is no tremor or wander added, the minus is a clean single stroke, and only two-bar `=` and `+` samples with level, aligned bars are used. Don't reintroduce wobble to make it look "more handwritten" — the variety comes from choosing between real samples.
- **One step per line**; continuation lines start with `=` and sit under the first line's `=` (the engine does this automatically for any line that starts with `=`).
- Pronumeral x is his curly x (written "ɔc"); multiplication is a cross ×. Fractions are stacked with a short rising bar. Indices written small and high; fractional indices as small stacked fractions.
- Minimal words: `max`, `min`, `so`, `ROC`, units (`cm`, `L/min`, `°`). No sentences unless the question asks for an explanation.
- No boxes round answers. Ticks go at the end of the line that earns the mark.
- **When space is short, do not squash the writing.** Run steps across the box (`… = … = …`) as Sam does on the board, or let the last line run a little below the box (up to about one grid row) as a person would. Only as a last resort is the writing made slightly smaller (never below 80 %). `inkdoc.py` makes these choices in that order and reports what it did.

## Step 3 — Write the solutions spec

Run the inventory to number the working spaces:

```bash
python grids.py "STUDENT.docx"
```
```
grid 0: 4 rows (1.80 cm), parts=3 widths(cm)=[6.0, 6.0, 6.0], marks=3 :: 1. Write in the form ... a) | b) | c)
grid 6: 7 rows (3.15 cm), parts=1 widths(cm)=[17.99], marks=3 :: 7. Find f'(x) ...
box 0: 1 rows (1.94 cm), parts=1 widths(cm)=[6.06], marks=None :: 1)  Find the volume.
```

It recognises every working space Sam's skills make:

| Kind | Made by | What a region is |
|---|---|---|
| `grid` | exam-revision-homework (dashed 0.45 cm squares), test-build / practice-test-build (`grid()`) | one squared grid; its part columns come from an a) b) c) label row inside the grid's first row or a borderless label table straight above it |
| `box` | worksheet-build, senior-homework-build (a row of empty answer boxes under a row of questions); test-build `slot()` strips | each empty working cell is its own region |

If side-by-side parts are only labelled inline in the question text (so the grid shows `parts=1`), split it with `SPLIT = {region: n}`. Then write `spec.py`, keyed by region index:

```python
SOL = {
 0: [ [r"\sqrt[3]{7} = 7^{\frac{1}{3}} \tick"],                 # part a)
      [r"\sqrt{125} = \sqrt{5^3}", r"= 5^{\frac{3}{2}} \tick"],   # part b)
      [...] ],                                                   # part c)
 6: [ [r"f(x) = 4x^3 - 6x^{-2} + 5x^{\frac{1}{2}} \tick",
       r"f'(x) = 3 \times 4x^{3-1} - 2 \times -6x^{-2-1} + \frac{1}{2} \times 5x^{\frac{1}{2}-1}",
       r"= 12x^2 + 12x^{-3} + \frac{5}{2}x^{-\frac{1}{2}} \tick",
       r"= 12x^2 + \frac{12}{x^3} + \frac{5}{2\sqrt{x}} \tick"] ],
}
# a box region may be given as just its list of lines:  3: [r"V = 6 \times 4 \times 3", r"= 72 cm^3"],
# optional: U_CM = 0.38 (digit height)  PEN_CM = 0.042  COLOR = '#E71224'  TICKS = True  SEED = 11
#           SPLIT = {0: 3}   HEADER = 'WORKED SOLUTIONS (teacher copy)'  (None to leave the name line alone)
#           NEAT = 0.85  (0 = quick and loose, 1 = careful; see Step 2)
```

Markup (a LaTeX subset — use raw strings):

| Write | Get |
|---|---|
| `x^2`, `x^{-3}`, `x^{\frac{1}{2}}` | indices (fractional indices drawn small and high) |
| `\frac{a}{b}` | stacked fraction |
| `\sqrt{x}`, `\sqrt[3]{27}` | radicals |
| `( … )` | brackets, stretched to what they enclose |
| `\pi \theta \times \div \deg \therefore \gt \lt \le \ge \pm \approx \ne \infty \to` | π θ × ÷ ° ∴ > < ≤ ≥ ± ≈ ≠ ∞ → |
| `\sin \cos \tan \ln \log`, `f^{\prime}` or `f'` | written as words / a prime |
| capitals, lowercase, digits, `. , ; : ! ? [ ] | / % $` | all available (capitals other than C and P, and some lowercase, are drawn from stroke recipes) |
| a space / `\quad` / `\,` | word gap / wide gap / thin gap |
| `\tick` | one mark tick, drawn after the end of that line |
| a line `@sign + 15 -` | sign diagram: arrowed line, root ticks, signs and roots above |

Keep each line to what Sam would write: a substitution line, a simplification line, the answer with units.

**Ticks follow the paper.** Assessments and homework with `[n marks]` get one `\tick` per mark (inkdoc checks the count against the paper). Worksheet answer sheets and other unmarked sheets set `TICKS = False` — answers and working only.

**From an exam-revision-homework `content.py`:** `python from_homework_content.py content.py WEEK > spec.py` drafts the spec from the week's `T(text, ticks)` solution lines (one region per working block, in order). Always edit the draft into Sam's methods and notation before building — it is typed-solution wording, not his handwriting. A full worked example (the 11 Methods Week 3 homework) is in the bundle as `example_spec_week3.py` — copy its shape, not its content.

## Step 4 — Build

```bash
python inkdoc.py "STUDENT.docx" spec.py "OUT - SOLUTIONS (handwritten).docx" --pdf
```

It prints, per part, the height used against the box, any run-over below the box, any reduced size, and **ticks vs the `[n marks]` printed under each grid**. Fix every `!!` line and any tick/mark mismatch before going on.

`python preview.py lines.txt` draws a few lines of markup to `preview.png` for a quick look while drafting.

## Step 5 — Check every page by eye

Render the PDF at ~110 dpi and look at **every page**, then zoom to ~300 dpi on a couple of dense boxes to check the strokes are smooth and steady:

- every line of ink sits in its own box, starts clear of the left border and the box above;
- nothing collides with the question text, the part labels, or `[n marks]`;
- run-overs below a box are small (≤ about one grid row) and don't reach the next question;
- indices, fractions, radicals, primes and decimal points read clearly;
- the number of ticks per question equals its marks.

Fix by editing the spec (shorten a line, split a long line into two, put two short steps on one line with `=`) and rebuild. Never hand-move ink coordinates; the whole document is regenerated from the spec. Change `SEED` for a different random draw of the handwriting.

## Step 6 — Save and report

Save beside the student paper (e.g. `.../homework/exam revision/`):
`<paper name> - SOLUTIONS (handwritten).docx` and `.pdf`, plus the spec as `<paper name> - handwritten spec.py` so a later fix is a rebuild, not a redo.

Report in two or three lines: where the files are, any box where the working ran below the grid or was written smaller, and anything Sam should check. Then ask for feedback and note whether each point is **standing** (fold into this skill: conventions table, notation rules, engine defaults) or **situational** (this paper only: change the spec).

## How it works (for maintenance)

- `hand.py` — glyph library (`glyphs.b64`: zlib+base64 JSON of Sam's strokes, normalised so a digit is 1 unit tall), the `NEAT` control (sample curation, slant straightening, how much random variation), `neaten()` (smooth → simplify → spline redraw of every stroke; dots and primes left as drawn), the markup parser and maths layout (indices, fractions, radicals, stretched brackets, primes), ticks, sign diagrams. Characters with no harvested sample are drawn from short stroke recipes in `SYN` (most capitals, d h j k q r t v w z, minus, decimal point, prime, and symbols). An unknown character raises an error naming it — add a `SYN` recipe (polyline points, digit height = 1, baseline y = 0, y down) or harvest a sample.
- `inkdoc.py` — block layout per part (one step per line → chain sideways → run slightly below → shrink; spare height spread between lines), then writes each line as an InkML part (`word/ink/inkhN.xml`, Word's own encoding: X/Y in 1/1000 cm, pressure channel, first-difference traces) anchored in the grid cell under its top-left corner (`wp:anchor`, `layoutInCell`, column/paragraph relative, `wrapNone`), inside `mc:AlternateContent` with an anti-aliased VML picture fallback (`word/media/inkhN.png`, 300 dpi). Word draws the ink; LibreOffice and older readers draw the picture.
- `grids.py` — finds the working spaces: squared grids (tables with ≥10 grid columns: exact-height working rows, part splits from a label row inside or a label table above, the `[n marks]` line below) and answer boxes (empty cells ≥ 0.9 cm tall in any other table, including `slot()` strips). Ink is anchored in whichever cell lies under each line's top-left corner, so it stays put if Word reflows the page.
- `from_homework_content.py` — drafts a spec from an exam-revision-homework `content.py` week.
- Improving the handwriting: more samples of letters that are currently synthetic (V, L, A, r, t, d…) make the biggest difference. The harvesting workflow: decode `word/ink/*.xml` (or `ppt/ink/*.xml`) traces, group strokes into characters by x-overlap, render numbered contact sheets, label them by eye, normalise per character (digit height = 1; operators by width) and re-pack `glyphs.b64`.

## Getting the scripts and the glyph library

Everything is bundled with this skill in its `scripts/` folder: `hand.py`, `inkdoc.py`, `grids.py`, `preview.py`, `from_homework_content.py`, the worked Week 3 example spec (`example_spec_week3.py`) and the glyph library (`glyphs.b64`, Sam's handwriting). Copy them into a working folder before Step 3 (the scripts find `glyphs.b64` next to themselves):

```bash
mkdir -p hw_ink && cp "<path to this skill>/scripts/"* hw_ink/ && cd hw_ink
pip install lxml pillow --break-system-packages -q 2>/dev/null
```

Seven files should be present. LibreOffice (`soffice`) is needed for `--pdf`; install `libreoffice-math` too or Word equations in the question text render as blanks. If `scripts/` or `glyphs.b64` is missing, stop and say so — don't rebuild the glyph library from memory.
