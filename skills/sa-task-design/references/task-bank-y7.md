# Year 7 task bank

Twelve tasks, written out in full. Every answer has been verified. Nothing here
needs the internet.

Header key — **Slot**: starter / post-teaching / deepening / whole-lesson /
plenary. **Disposition**: the one it develops *strongly*.

---

### T7-01 · Exactly three
**Open Middle-ish · Deepening · 12 min · `AC9M7N02` (prime factorisation), `AC9M7N01` · Reasoning · Resourceful**

> Most numbers have an even number of factors. Some have an odd number.
> **Find every number below 200 that has exactly three factors.**
> How do you know you have found them all?

*Entry:* everyone can start by listing factors of small numbers.
*Answer:* **4, 9, 25, 49, 121, 169** — the squares of the primes 2, 3, 5, 7, 11, 13.
*Anticipated:* students find 4 and 9 and guess "square numbers" — then 16 has
five factors and the conjecture breaks. That break is the lesson.
*Consolidation:* why must a number with exactly three factors be p²? (Its factors
are 1, itself, and exactly one other, which must be prime and must square to it.)
*Extension:* exactly four factors? (p³ or p×q.)

---

### T7-02 · Closest to 500
**Open Middle · Post-teaching · 8 min · `AC9M7N06`, `AC9M7N05` (estimation) · Resilient**

> Using the digits 1 to 9, **at most once each**, fill the boxes
> `□□ × □` to make the answer **as close to 500 as possible**.

*Entry:* any filling gives an answer; everyone is in within a minute.
*Answer (verified by exhaustive search):* the best is **83 × 6 = 498**, off by 2.
Next best are 62 × 8 = 496 and three ways to make 504 (56×9, 63×8, 84×6), all off
by 4.
*Anticipated:* students go straight for large tens digits. The insight is to
estimate first — 500 ÷ 6 ≈ 83, 500 ÷ 8 ≈ 62 — then check the one product.
*Consolidation:* "how could you have known where to look without trying them all?"
*Extension:* closest to 1000 with `□□ × □□`.

---

### T7-03 · Same area, different perimeter
**Optimisation · Deepening · 15 min · `AC9M7M01` · Resourceful**

> A rectangle has an area of 40 cm².
> **What is the smallest perimeter it can have? What is the largest?**

*Entry:* draw any rectangle with area 40.
*Answer:* with **whole-number** sides, smallest perimeter is **26 cm** (5 × 8);
largest is **82 cm** (1 × 40). If sides need not be whole numbers, the smallest
is the square √40 × √40 ≈ 6.32 × 6.32, perimeter ≈ **25.3 cm**, and there is **no
largest** — 0.1 × 400 has perimeter 800.2, and it keeps going.
*Anticipated:* almost every class assumes whole-number sides without being told.
Do not correct this early; let someone find 6.32 and let the class argue.
*Consolidation:* "why does the most square-ish rectangle have the smallest
perimeter?"
*This is the worked example of a low-ceiling question repaired.* The original —
"area 40, one side 8, find the other" — takes a capable student ten seconds.

---

### T7-04 · Which one doesn't belong: quadrilaterals
**WODB · Starter · 6 min · `AC9M7SP02` · Reflective**

> Four shapes on the board:
> **A** a square (4 cm sides) · **B** a rhombus with 4 cm sides and 60°/120° angles ·
> **C** a rectangle 8 cm × 2 cm · **D** a parallelogram 8 cm × 4 cm with 60°/120° angles.
> **Which one doesn't belong?** Find a reason for each of the four.

*Reasons (have all four ready):* **A** is the only one with all sides equal *and*
all angles equal. **B** is the only one with all sides equal but not all angles
equal — and the only one whose area is not a whole number of cm². **C** is the
only one with all right angles but not all sides equal. **D** is the only one
with no line of symmetry.
*Consolidation:* build the class definition list — which properties did we
actually need to name?

---

### T7-05 · What can you work out?
**Goal-free · Starter · 8 min · `AC9M7M04`, `AC9M7M05` · Resourceful**

> Two parallel lines crossed by a transversal. One angle is marked **68°**.
> A triangle sits on the lower parallel line with another angle marked **45°**.
> **No question. Work out everything you can, and label it.**

*Entry:* every student can mark the vertically opposite angle.
*Expected:* the vertically opposite 68°, co-interior 112°, corresponding and
alternate 68°, the third angle of the triangle 180 − 68 − 45 = 67°, exterior
angles, and the straight-line pairs.
*Consolidation:* compare lists. "Who found something nobody else did? What did
you use to get it?" Then — and only then — show a past-paper question on the same
diagram and ask which of their deductions was actually needed.
*Why this genre:* removes means-end analysis; the students who freeze on
multi-step angle chasing are usually the ones who cannot choose a starting point.

---

### T7-06 · Two discounts
**Argument · Starter · 6 min · `AC9M7N09` · Reasoning**

> A shop offers **20% off, then a further 10% off at the till**.
> A rival offers a flat **30% off**.
> Ali says they're the same. Bo says the first is better. Cam says the second is
> better. **Who is right, and how would you convince the other two?**

*Answer:* Cam. 0.8 × 0.9 = **0.72**, so the first shop charges 72% — a 28%
discount, not 30%. The flat 30% (0.70) is cheaper.
*Anticipated:* "20 + 10 = 30, same" is the dominant answer and is exactly the
misconception worth surfacing. Ask for a $100 item; the argument ends quickly.
*Consolidation:* does the order matter? (No — 0.9 × 0.8 = 0.8 × 0.9.) When *would*
successive discounts equal the sum? (Never, for non-zero discounts.)

---

### T7-07 · Five numbers
**Constrained search · Deepening · 15 min · `AC9M7ST01` · Resilient**

> Five whole numbers have **mean 6, median 5 and range 8**.
> **Find a set that works. Then find them all. How do you know you have them all?**

*Entry:* try five numbers and check.
*Answer (verified exhaustively):* there are exactly **seven** sets —
(2,3,5,10,10), (2,4,5,9,10), (2,5,5,8,10), (3,3,5,8,11), (3,4,5,7,11),
(3,5,5,6,11), (4,4,5,5,12).
*The structure:* mean 6 fixes the total at 30; median 5 fixes the middle value;
range 8 means max = min + 8. Only min = 2, 3 or 4 leaves a workable middle pair.
*Consolidation:* "which constraint was doing the most work?" Most classes find
the total-of-30 move last and it is the most powerful one.
*Extension:* change the mean to 7. How many now?

---

### T7-08 · Visually growing pattern
**Visual pattern · Post-teaching · 10 min · `AC9M7A05`, `AC9M7A02` · Developing understanding**

> Draw an L-shaped arrangement of squares: step 1 is 1 across and 1 up (3
> squares in a corner), step 2 is 2 across and 2 up (5 squares), step 3 is 3
> and 3 (7 squares).
> **How many squares at step 10? At step 43? Write a rule. Then show us where
> your rule is in the picture.**

*Answer:* step *n* has **2n + 1** squares; step 10 → 21, step 43 → 87.
*Anticipated — and this is the point:* different students see it differently.
"n up, n across, plus the corner" gives 2n + 1. "Two arms of n+1, sharing the
corner" gives 2(n+1) − 1. "One row of n+1 plus a column of n" gives
(n+1) + n. All three are correct and all three are the same expression.
*Consolidation:* put the three expressions side by side and ask whether they are
different rules or the same rule written differently. That is `AC9M7A02` — the
"infinitely many equivalent forms" conceptual understanding — arriving from a
picture rather than from a worksheet.

---

### T7-09 · Is it a fair game?
**Probability argument · Deepening · 15 min · `AC9M7P01`, `AC9M7P02` · Reasoning**

> Two dice are rolled and the numbers **added**.
> Player A scores a point if the total is **even**. Player B scores if it is **odd**.
> **Is this fair?** Now change it: A scores if the total is a **prime number**,
> B otherwise. **Now is it fair? If not, how would you fix it?**

*Answers:* even/odd is **fair** — 18 of 36 outcomes each. Prime totals (2, 3, 5,
7, 11) occur **15 of 36** times, so B wins 21/36 — not fair.
*Anticipated:* students argue about whether "even is more likely because there
are more even numbers on a die" — the sample space grid settles it.
*Consolidation:* run it 40 times as a class and compare the experimental relative
frequency with 15/36 ≈ 0.42. That comparison *is* `AC9M7P02`.
*Fix it:* give B a point only on 4, 6, 8, 9, 10 (also 15/36 — verify with the class).

---

### T7-10 · The bigger half
**Estimation / integers · Starter · 6 min · `AC9M7N07` · Reflective**

> On a number line, **a** is somewhere between −8 and −2, and **b** is somewhere
> between 1 and 6. You are not told exactly where.
> **Which of these can you be certain about?**
> `a + b > 0` · `a − b < 0` · `a × b < 0` · `b − a > 0` · `a ÷ b < −1`

*Answers:* certain — `a − b < 0`, `a × b < 0`, `b − a > 0`. Not certain —
`a + b > 0` (e.g. −8 + 1 = −7) and `a ÷ b < −1` (e.g. −2 ÷ 6 ≈ −0.33).
*Anticipated:* students test one pair of values and declare victory. Push: "you
showed it works once — show me it always works, or find one where it fails."
*Consolidation:* a single counterexample kills a claim; no number of examples
proves one. This is the reasoning move the whole year depends on.

---

### T7-11 · Which is the better deal?
**Modelling · Whole-lesson · 45 min · `AC9M7N08`, `AC9M7N09`, `AC9M7M06` · Resourceful**

> Three phone plans:
> **P1** $25/month, 10 GB included, $8 per extra GB.
> **P2** $40/month, 30 GB included, $4 per extra GB.
> **P3** $15/month, no data included, $6 per GB.
> **Which plan should you be on?** You need to tell us what you assumed.

*Entry:* work out the cost of each for one chosen amount of data.
*Answers (verified across 0–40 GB):* **P3 is cheapest below ≈ 1.7 GB** —
P3 = 15 + 6d meets P1's flat $25 at d = 10/6 ≈ 1.67. **P1 is cheapest from ≈ 1.7
GB to ≈ 11.9 GB** — beyond 10 GB it costs 25 + 8(d − 10), which reaches $40 at
d = 11.875. **P2 is cheapest above ≈ 11.9 GB.** Accept any answer with correct
working and a stated assumption about usage.
*Consolidation:* the answer is a *range*, not a number, and the honest answer is
"it depends how much data you use". Getting a class to say that out loud is the
lesson. `AC9M7N09` asks them to *review the appropriateness of the model* — ask
what the model ignores (contract length, coverage, phone included).
*If you want the polished version:* Citizen Math *Text Me Later* (ratios
and proportion) and *To Have and to Hold* both cover this ground, if your
school holds the Citizen Math library.

---

### T7-12 · Find the mistake
**Error analysis · Plenary · 6 min · `AC9M7A03` · Reflective**

> A student's work, on the board exactly as written:
> `3x + 7 = 22`
> `3x = 29`
> `x = 9.67`
> **Is this right? What did they do? What one sentence would you say to them?**

*Answer:* they added 7 instead of subtracting. The check settles it —
3(9.67) + 7 = 36, not 22.
*Anticipated:* students spot the arithmetic but say "they did it wrong". Push for
the *rule* they were following: "do the opposite" got applied as "move the
number", losing the sign.
*Consolidation:* substitute the answer back. Make substitution the class's
default self-check; `AC9M7A03` says *verify the solution by substitution* in so
many words.
*To build more of these:* take the misconception already named in the lesson's
atomisation and write the solution a student holding it would actually produce.
