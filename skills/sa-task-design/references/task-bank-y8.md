# Year 8 task bank

Twelve tasks, fully written, answers verified.

---

### T8-01 · Make x as big as you can
**Open Middle · Post-teaching · 12 min · `AC9M8A02` · Resilient**

> Using the digits **1 to 9, at most once each**, fill the boxes
> `□x + □ = □x + □`
> to make the solution **as large as possible**.

*Entry:* any filling gives an equation to solve — everyone practises the
procedure while searching.
*Answer (verified exhaustively):* the largest possible solution is **x = 8**,
reached by e.g. `2x + 9 = 3x + 1`, `3x + 9 = 4x + 1`, `4x + 9 = 5x + 1` — and
several more. The smallest is **x = −8**.
*The insight:* rearranging gives x = (d − b) ÷ (a − c). To make x big you want the
constants as far apart as possible (9 and 1, difference 8) and the coefficients
as close as possible (difference 1). Students who see this stop guessing.
*Consolidation:* "why can't you do better than 8?" — the constants can differ by
at most 8 and the coefficients by at least 1.
*Extension:* make the solution as close to zero as possible without being zero.
(Answer: **1/8**, e.g. `x + 3 = 9x + 2`.)

---

### T8-02 · Is it right-angled?
**SSDD-adjacent / reasoning · Deepening · 15 min · `AC9M8M06` · Resourceful**

> Five triangles, side lengths only, no diagram to scale:
> **A** 6, 8, 10 · **B** 5, 12, 13 · **C** 7, 8, 11 · **D** 9, 12, 15 · **E** 20, 21, 29
> **Which are right-angled?** Then: **one of the non-right ones — is it
> acute or obtuse? How can you tell without measuring?**

*Answers:* A, B, D and E are right-angled (E: 400 + 441 = 841 = 29²). C is not —
49 + 64 = 113 < 121, so the angle opposite the 11 is **obtuse**.
*Anticipated:* students check A and B from memory of "Pythagorean triples" and
stop thinking. E is unfamiliar and forces the actual test. D is 3-4-5 scaled by 3
— worth surfacing.
*Consolidation:* if a² + b² < c², the angle opposite c is obtuse; if greater,
acute. Most classes have never been told this and can derive it from the
converse in two minutes.
*Extension:* find another triple nobody in the room knows. (Multiples don't
count.)

---

### T8-03 · Two shapes, same area
**Composite area · Deepening · 15 min · `AC9M8M01` · Reasoning**

> An L-shaped block of flats has these outside measurements: it is 12 m across
> the bottom, 10 m up the left side, and a 5 m × 4 m rectangle has been removed
> from the top-right corner.
> **Find the area three different ways.** Then: **is there a rectangle with
> exactly the same area? What are its dimensions?**

*Answer:* area = 12 × 10 − 5 × 4 = **100 m²**. Three routes: subtract the missing
rectangle; split into 7 × 10 + 5 × 6; split into 12 × 6 + 7 × 4. All give 100.
An equal-area rectangle: 10 × 10, or 20 × 5, or 8 × 12.5 — infinitely many.
*Consolidation:* board all three decompositions side by side. "Which was
cleanest, and why?" The subtract-the-hole method wins here and doesn't always —
that's the judgement being built.
*Extension:* what is the L-shape's perimeter, and does the equal-area rectangle
have the same perimeter? (L-shape perimeter = 44 m; the 10 × 10 square is 40 m.
Same area, different perimeter — links straight back to T7-03.)

---

### T8-04 · Which line doesn't belong?
**WODB · Starter · 6 min · `AC9M8A02` · Reflective**

> Four linear relations:
> **A** y = 2x + 3 · **B** y = −2x + 3 · **C** y = 2x − 3 · **D** y = ½x + 3
> **Which one doesn't belong?** A reason for each.

*Reasons:* **A** — the only one with both a positive gradient of 2 *and* a
positive intercept, i.e. the only one that passes through neither the third nor
the fourth quadrant. **B** — the only one with negative gradient. **C** — the
only one that doesn't pass through (0, 3). **D** — the only one whose gradient
isn't ±2, and the only one where x must be even for y to be an integer at
integer-ish points.
*Consolidation:* sketch all four on one set of axes. Which reasons were visible
in the equation and which only in the graph? That is `AC9M8A02`'s "algebraically
*and* graphically".

---

### T8-05 · The exponent Venn
**Maths Venn · Deepening · 15 min · `AC9M8N02` · Resourceful**

> A two-circle Venn.
> **Circle 1:** "the value equals 64"  **Circle 2:** "written using an exponent of 3"
> **Find something for every region — including outside both.
> Is any region impossible?**

*Answers:* both circles — **4³**. Circle 1 only — 2⁶, 8², 64¹, 2⁷ ÷ 2. Circle 2
only — 2³, 5³, 10³. Neither — 3², 2⁵, 100. No region is impossible.
*Now the version with a real fight in it:* change circle 2 to **"written using a
negative exponent"** and circle 1 to **"the value is a whole number greater than
1"**. The intersection needs something like 2⁻³ ... which is ⅛, not a whole
number — but (½)⁻³ = 8 works. Whether that counts is exactly the argument you
want.
*Consolidation:* "how many different ways can we write 64 as a power?" —
`AC9M8N01`'s multiple-forms conceptual understanding, from a puzzle rather than a
statement.

---

### T8-06 · How many fish?
**Modelling · Whole-lesson · 45 min · `AC9M8ST01`, `AC9M8ST04`, `AC9M8M07` · Resourceful**

> A ranger wants to know how many fish are in a lake without draining it.
> She catches **60**, tags them, and puts them back. A week later she catches
> **50** and finds **8** of them are tagged.
> **How many fish are in the lake?** What did you have to assume?

*Entry:* everyone can say "more than 60".
*Answer:* if 8/50 of the second catch is tagged, assume 8/50 of the lake is
tagged. So 60 ÷ n = 8 ÷ 50, giving **n = 375**.
*The assumptions — this is the lesson:* the tagged fish mixed evenly back in;
tagging doesn't change a fish's chance of being caught; no fish were born, died,
or left; a week is long enough to mix but short enough that nothing changed.
*Model it:* a bag of 200 counters, 40 marked. Groups sample 20, estimate, and
compare. The spread of the class's estimates is `AC9M8ST03` — the effect of
sample size — arriving physically.
*Consolidation:* "our estimates ranged from ___ to ___. What would make them
tighter?" (Bigger samples, or repeat and average.)
*Related local asset:* Citizen Math *Seeking Shelter* (line of best fit) in
`Citizen math/year 8/` if you want a second data lesson the same week.

---

### T8-07 · Between which two?
**Number line reasoning · Starter · 6 min · `AC9M8N01` · Reasoning**

> Put these in order on a number line, without a calculator:
> `√2` · `1.5` · `√5` · `π` · `22/7` · `3` · `2.5`
> **Which of them are irrational? For √5, how did you decide where it goes?**

*Answers:* order — √2 (≈1.414), 1.5, 2.5, √5 (≈2.236)… careful: √5 ≈ 2.236 sits
*before* 2.5. Correct order: **√2, 1.5, √5, 2.5, 3, π (≈3.1416), 22/7 (≈3.1429)**.
Irrational: **√2, √5, π**. 22/7 is rational and is *not* π — it is very slightly
larger.
*Anticipated:* nearly every class puts 22/7 and π at the same point. The
difference is about 0.00126, and that is a genuinely surprising fact worth thirty
seconds.
*Consolidation:* how do you locate √5 without a calculator? 2² = 4 and 3² = 9, so
it's between 2 and 3; 2.2² = 4.84 and 2.3² = 5.29, so between 2.2 and 2.3.
Squaring-to-trap is the method.

---

### T8-08 · The pizza question
**Circles / scaling · Post-teaching · 10 min · `AC9M8M03` · Reflective**

> A 12-inch pizza costs $18. An 18-inch pizza costs $34.
> **Which is better value? By how much?**
> Then: **a shop offers "two 12-inch for the price of one 18-inch". Take it?**

*Answers:* areas are π×6² = 113.1 in² and π×9² = 254.5 in². Per square inch:
$0.159 vs **$0.134** — the 18-inch is about 16% better value. Two 12-inch pizzas
give 226.2 in² for $34 vs one 18-inch at 254.5 in² for $34 — **take the 18-inch**,
it's 12.5% more pizza.
*Anticipated:* students compare diameters, not areas — "18 is 1.5 times 12 so it
should cost 1.5 times as much". Doubling the diameter *quadruples* the area, and
that surprise is the task.
*Consolidation:* "if a pizza's diameter goes up by 50%, what happens to the
area?" (×2.25.) Draw the 12-inch inside the 18-inch on the board — the picture
does the work.

---

### T8-09 · Same surface, different deep
**SSDD · Deepening · 12 min · `AC9M8M01`, `M03`, `M06`, `SP01` · Resourceful**

> One diagram on the board: a right-angled triangle with legs 6 cm and 8 cm,
> with a semicircle drawn on the hypotenuse.
> **a)** Find the length of the hypotenuse.
> **b)** Find the area of the triangle.
> **c)** Find the perimeter of the whole shape (triangle plus semicircle arc,
> not counting the hypotenuse).
> **d)** The triangle is enlarged by scale factor 2.5. What is the new area?
> **Before you solve any of them, write down which topic each one is.**

*Answers:* a) 10 cm. b) 24 cm². c) 6 + 8 + ½π(10) = 14 + 5π ≈ **29.7 cm**.
d) area scales by 2.5² = 6.25, so **150 cm²**.
*The point:* the diagram is identical for all four; the mathematics is
Pythagoras, area, circumference and similarity. Part (d) catches almost everyone
— students multiply the area by 2.5.
*Dispatch note:* this school has an `ssdd-build` skill. Use it for a full set;
this one is here so the bank has a worked example of the genre.

---

### T8-10 · Complementary, or not?
**Probability argument · Starter · 8 min · `AC9M8P01`, `AC9M8P02` · Reasoning**

> A spinner has 8 equal sections numbered 1–8.
> Dee says: "P(even) = ½ and P(odd) = ½, and they add to 1, so they're
> complementary."
> Eli says: "P(prime) = 4/8 and P(square) = 3/8 — 2, 3, 5, 7 and 1, 4, 9…
> wait." **Sort Eli out. Then: is 'multiple of 3' complementary to 'not a
> multiple of 3'? Is it complementary to 'multiple of 4'?**

*Answers:* Dee is right. Eli has two errors — 9 isn't on the spinner, so squares
are 1 and 4 only (2/8), and prime/square are not complementary anyway (6 and 8
are neither). "Multiple of 3" (3, 6 → 2/8) and "not a multiple of 3" (6/8) **are**
complementary — mutually exclusive and covering everything. "Multiple of 3" and
"multiple of 4" (4, 8 → 2/8) are mutually exclusive but **do not cover everything**
(1, 2, 5, 7 are left over) — so not complementary.
*Consolidation:* the two conditions are *mutually exclusive* **and** *exhaustive*.
Most students only ever check the second. Build a two-way table to make it visible.

---

### T8-11 · Three time zones
**Modelling · Post-teaching · 12 min · `AC9M8M04` · Resourceful**

> A flight leaves **Adelaide at 6:20 am** and lands in **Perth at 8:05 am**
> local time. Perth is 2½ hours behind Adelaide.
> **How long was the flight?**
> The return leg takes 20 minutes longer. **If it leaves Perth at 4:40 pm, what
> time does it land in Adelaide?**

*Answers:* 8:05 am Perth = 10:35 am Adelaide, so the flight took **4 h 15 min**.
Return: 4 h 35 min from 4:40 pm Perth = 9:15 pm Perth = **11:45 pm Adelaide**.
*Anticipated:* students subtract clock times directly and get 1 h 45 min. The fix
is converting both to one time zone *first* — the habit, not the arithmetic, is
the target.
*Consolidation:* "which zone did you convert to, and why?" There's no right
answer; committing to one before calculating is the strategy.
*Extension:* daylight saving. Perth doesn't observe it; Adelaide does. What
happens to both answers in January?

---

### T8-12 · Which sample would you trust?
**Statistical argument · Plenary · 8 min · `AC9M8ST01`, `AC9M8ST02` · Reflective**

> The school wants to know what proportion of students would use a new bike rack.
> Four proposals:
> **A** ask everyone in Year 8 · **B** ask the first 50 students through the gate
> at 8:30 am · **C** ask 50 students chosen at random from the whole roll ·
> **D** put a poster up asking people to scan a QR code and answer.
> **Rank them. For the worst one, say exactly who gets over-represented.**

*Answer:* **C** is the only representative sample. **A** is a census of one year
level — fine for Year 8, useless for the school. **B** over-samples students who
walk or ride and arrive early — the exact group most likely to say yes, so it
biases *towards* the conclusion the school wants. **D** is self-selected and
over-samples people with strong opinions either way.
*Consolidation:* "B and D both give you 50 answers. Why is C worth more?" That
question is the whole of `AC9M8ST01`.
