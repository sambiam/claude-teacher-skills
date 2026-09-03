# Year 9 task bank

Twelve tasks, fully written, answers verified.

---

### T9-01 · The paddock
**Optimisation / quadratic modelling · Whole-lesson · 45 min · `AC9M9A05`, `AC9M9A04` · Resilient**

> You have **24 m of fencing** and a long straight wall. You want to fence a
> rectangular paddock using the wall as one side.
> **What is the largest area you can enclose?**
> Then: **what if there is no wall?** And: **what if you have 24 m and want to
> fence two identical paddocks side by side against the wall?**

*Entry:* pick a width, work out the area. Everyone has a data point in a minute.
*Answers (verified):* with the wall, width w and length 24 − 2w gives
A = w(24 − 2w), maximised at **w = 6 m, area 72 m²** (6 × 12). With no wall,
2w + 2l = 24, so it's a **6 × 6 square, 36 m²**. Two paddocks against the wall
needs three widths: A = w(24 − 3w), maximised at **w = 4, area 48 m²**.
*Anticipated:* students assume the square is always best. The wall breaks that,
and the surprise is the point.
*Consolidation:* tabulate w against A and plot it. It's a parabola; the maximum is
the vertex. This is `AC9M9A04`'s "identify and graph quadratic functions" arriving
because something needed it, not because the exercise said to.
*Extension:* the wall version is always half the fence one way and half the other
— is that a coincidence? (No. Reflect the paddock in the wall and you have the
no-wall problem with 48 m.)

---

### T9-02 · Roll an A4 sheet
**Volume / surface area · Deepening · 20 min · `AC9M9M01` · Reasoning**

> Take a sheet of A4 (21.0 cm × 29.7 cm). Roll it into a cylinder — you can roll
> it **the tall way** or **the wide way**. No lid, no base, no overlap.
> **Do the two cylinders hold the same amount? If not, which holds more, and by
> how much?**

*Entry:* everyone can roll two sheets and look.
*Answer (verified):* tall cylinder — circumference 21, so r = 21/2π ≈ 3.34, height
29.7, volume ≈ **1042 cm³**. Wide cylinder — circumference 29.7, r ≈ 4.73, height
21, volume ≈ **1474 cm³**. The short fat one holds about **41% more**.
*Anticipated:* "same paper, same volume" is the near-universal first answer. Roll
both and pour rice from one into the other — the demonstration is worth doing.
*Consolidation:* why? Volume goes as r²h, and halving the height while
multiplying the radius by ~1.41 multiplies r² by 2 — so the fat one wins.
*Extension:* if you could use any rectangle of paper with area 623.7 cm², what
shape gives the biggest cylinder?

---

### T9-03 · Which triangle is the odd one out?
**WODB / trigonometry · Starter · 8 min · `AC9M9SP01`, `AC9M9M03` · Reflective**

> Four right-angled triangles, all with the right angle at the bottom right:
> **A** legs 3 and 4 · **B** legs 6 and 8 · **C** legs 4 and 3 · **D** legs 5 and 12
> **Which one doesn't belong?**

*Reasons:* **D** — the only one not similar to the others (its ratios are 5:12:13,
not 3:4:5). **B** — the only one whose sides aren't in lowest terms / the only one
with even perimeter 24 rather than 12. **C** — the same triangle as A but the
other way round, so the only one where the *angle at the top* is the smaller one;
tan of the marked angle is 3/4 for A and 4/3 for C. **A** — the only one that is
both in lowest terms and "the usual way round".
*Consolidation:* A, B and C all give the same tan, sin and cos values for
corresponding angles — that constancy under enlargement **is** `AC9M9SP01`, and
it is why trigonometry works at all. Ask: "if I gave you a triangle with legs 30
and 40, what's the angle?" They already know it.

---

### T9-04 · The ladder rule
**Trigonometry modelling · Post-teaching · 15 min · `AC9M9M03` · Resourceful**

> Safety guidance says a ladder should be set at an angle of **75°** to the
> ground, and should extend **1 m above** the edge it rests against.
> A gutter is **4.2 m** above the ground.
> **What length ladder do you need, and how far from the wall should the foot go?**
> Then: **a tradie's rule of thumb is "one out for every four up". Is that the
> same as 75°?**

*Answers:* the ladder must reach 4.2 + 1 = 5.2 m up. Length = 5.2 ÷ sin 75° ≈
**5.38 m**. Foot distance = 5.2 ÷ tan 75° ≈ **1.39 m**.
The 1-in-4 rule gives tan θ = 4, so θ ≈ **75.96°** — close to 75° but not equal.
Over 5.2 m of height that's a foot distance of 1.30 m instead of 1.39 m, a
difference of about 9 cm.
*Consolidation:* is a 9 cm difference worth worrying about? The class has to
decide what precision the context deserves — which is `AC9M9M04`, error and
accuracy, without a worksheet on error.
*Extension:* at what height does the 1-in-4 rule put the foot a whole 20 cm out
from the 75° position?

---

### T9-05 · Order of magnitude
**Estimation / scientific notation · Starter · 8 min · `AC9M9M02` · Resourceful**

> Put these in order, smallest to largest, and write each in scientific notation:
> the thickness of a sheet of paper · the diameter of a human hair · the length
> of this classroom · the distance to Melbourne · the diameter of the Earth ·
> the distance to the Sun
> **You are not allowed to look anything up. Justify each estimate.**

*Reference answers:* paper ≈ 1 × 10⁻⁴ m · hair ≈ 7 × 10⁻⁵ m (**thinner than
paper** — this is the surprise) · classroom ≈ 8 m = 8 × 10⁰ · Adelaide–Melbourne
≈ 7.3 × 10⁵ m · Earth's diameter ≈ 1.27 × 10⁷ m · Earth–Sun ≈ 1.5 × 10¹¹ m.
*Anticipated:* students reach for digits rather than powers. Redirect: "don't tell
me the number, tell me the power of ten."
*Consolidation:* a ream of 500 sheets is about 5 cm thick — that's where 10⁻⁴
comes from, and it is a reasoning move (divide a measurable thing by a count)
they can reuse.
*Extension:* how many hairs side by side to cross the classroom? (≈10⁵.)

---

### T9-06 · How wrong can it be?
**Measurement error · Deepening · 15 min · `AC9M9M04` · Reasoning**

> A rectangular slab is measured as **3.4 m by 2.7 m**, each to the nearest 0.1 m.
> **What is the smallest the area could be? The largest?**
> A concreter quotes on the measured area at $95/m². **How much could the quote
> be out by?**

*Answers:* the true lengths lie in [3.35, 3.45) and [2.65, 2.75). Minimum area =
3.35 × 2.65 = **8.8775 m²**; maximum = 3.45 × 2.75 = **9.4875 m²**. Measured area
= 9.18 m². So the true area could be up to 0.3075 m² above or 0.3025 m² below —
a relative error of about **±3.3%**, or **±$29** on a quote of $872.10.
*Anticipated:* students halve the 0.1 correctly for each length but then think the
area error is ±0.05. It roughly doubles, because both dimensions are uncertain.
*Consolidation:* percentage errors of about 1.5% each combine to about 3% in the
area. That's the rule worth carrying: for a product, relative errors add.
*Extension:* the concreter measures to the nearest cm instead. Now what?

---

### T9-07 · Expand and factorise Venn
**Maths Venn · Post-teaching · 12 min · `AC9M9A02` · Resourceful**

> Two circles.
> **Circle 1:** "expands to give an x² term with coefficient 1"
> **Circle 2:** "expands to give a constant term of −12"
> Find a product of two brackets for **every region**, including outside both.
> **Is any region impossible?**

*Answers:* both — (x + 2)(x − 6), or (x − 3)(x + 4), or (x + 12)(x − 1). Circle 1
only — (x + 2)(x + 3). Circle 2 only — (2x + 3)(x − 4), which gives 2x². Neither
— (2x + 1)(x + 5). No region is impossible.
*Consolidation:* "how many products give a constant of −12 *and* a monic
quadratic?" Every factor pair of −12: (1, −12), (2, −6), (3, −4), (4, −3),
(6, −2), (12, −1) — six, and they are exactly the pairs students search when
factorising. The Venn makes the search visible before it becomes a procedure.
*Extension:* add a third circle, "the quadratic has a repeated root". Which
regions empty out?

---

### T9-08 · Read the claim
**Statistical argument · Starter · 10 min · `AC9M9ST01`, `AC9M9ST02` · Reflective**

> A headline: **"Teen screen time up 40% — students spending 9 hours a day on
> phones."** The article says the figure comes from an online survey of 1,200
> teenagers, run through a gaming website, in which participants self-reported
> their daily usage.
> **List every reason to be careful with this number. Then: what would a survey
> you'd believe look like?**

*Expected:* self-selected sample from a gaming site (over-samples heavy users);
self-reported rather than measured; "up 40%" — from what, over what period, and
was the earlier figure measured the same way; "9 hours a day" is a mean, and one
outlier at 20 hours drags a mean hard — what's the median; does "screen time"
include school work.
*Consolidation:* which of those objections could be fixed by a bigger sample?
(None of the important ones.) Sample size is the thing students reach for, and
it's the wrong lever here.
*Extension:* rewrite the headline so it is defensible from the same data.

---

### T9-09 · With or without replacement
**Probability · Deepening · 15 min · `AC9M9P01`, `AC9M9P02` · Reasoning**

> A bag has **5 red and 3 blue** counters. Two are taken out.
> **a)** P(both red) if the first is put back.
> **b)** P(both red) if it is not.
> **c)** P(one of each) without replacement.
> **d)** Someone claims that as the bag gets bigger — 50 red and 30 blue, same
> ratio — the two answers to (a) and (b) get closer together. **Are they right?**

*Answers:* a) 5/8 × 5/8 = **25/64 ≈ 0.391**. b) 5/8 × 4/7 = **20/56 = 5/14 ≈
0.357**. c) 2 × (5/8 × 3/7) = **30/56 = 15/28 ≈ 0.536**. d) **Yes** — with 50 and
30, without replacement gives 50/80 × 49/79 ≈ 0.3877 against 0.3906 with
replacement. The gap shrinks from 0.034 to 0.003.
*Anticipated:* students forget the factor of 2 in (c). Ask them to list the
orders.
*Consolidation:* why does (d) work? Removing one counter from 8 changes the
proportion a lot; removing one from 80 barely moves it. That is precisely why
sampling from a large population is treated as *with* replacement — and it links
straight back to Year 8's sampling work.

---

### T9-10 · What stays the same?
**Enlargement · Post-teaching · 12 min · `AC9M9SP02` · Developing understanding**

> A triangle with vertices A(1, 1), B(5, 1), C(1, 4) is enlarged by scale factor
> **3** from the origin.
> **Write down everything that changes and everything that stays the same.**
> Be precise — give numbers.

*Answers.* Changes: coordinates (3, 3), (15, 3), (3, 12); side lengths ×3
(4→12, 3→9, 5→15); perimeter 12→36; **area ×9** (6 → 54).
Stays the same: all three angles; the shape; the *ratios* of the sides (3:4:5);
the gradient of every side; the fact that it's right-angled; the point (0, 0),
which is the only fixed point.
*Anticipated:* area is the one everyone gets wrong, and gradient is the one
nobody thinks to mention. Prompt: "what about the steepness of AC?"
*Consolidation:* which of the "stays the same" list would still hold if the
enlargement were from (2, 2) instead? (All of them except which point is fixed.)
*Extension:* scale factor −2. Now what changes?

---

### T9-11 · Which graph tells the truth?
**Data representation · Plenary · 8 min · `AC9M9ST04`, `AC9M9ST02` · Reflective**

> The same six monthly sales figures — 102, 105, 103, 108, 106, 110 — drawn three
> ways on the board:
> **A** a bar chart with the vertical axis from 0 to 120
> **B** the same bar chart with the axis from 100 to 112
> **C** a line graph with the axis from 100 to 112
> **Which would a salesperson use? Which would a critic use? Which is honest?**

*Answer:* B makes an 8% rise look like a fivefold jump — the salesperson's
choice. A is honest about magnitude but makes the trend nearly invisible — the
critic's choice. C is usually the fairest because a line graph doesn't carry the
implicit "bars start at zero" contract that a bar chart does.
*Consolidation:* the rule is *bars must start at zero; lines need not*. Ask why:
a bar's **length** encodes the value, so truncating the axis lies about the value.
A line encodes **change**, so a truncated axis is legitimate.
*Curriculum:* this is `AC9M9ST02` — how the choice of representation can be used
to support a particular point of view — as a six-minute argument.

---

### T9-12 · Where's the mistake?
**Error analysis · Plenary · 6 min · `AC9M9A01` · Reflective**

> On the board:
> `(3x²)³ = 3x⁶` · `x⁵ ÷ x⁵ = 0` · `2⁻³ = −8` · `(x + y)² = x² + y²`
> **All four are wrong. For each: what rule were they using, and what is the
> correct answer?**

*Answers:* `(3x²)³ = 27x⁶` — the 3 gets cubed too. `x⁵ ÷ x⁵ = x⁰ = 1` — subtracting
exponents gives 0 *as an exponent*, not as an answer. `2⁻³ = 1/8` — a negative
exponent means reciprocal, not negative. `(x + y)² = x² + 2xy + y²` — the
"freshman's dream", and the one that survives into Year 12.
*Run it as:* each error is a *rule half-remembered*, not carelessness. Naming the
half-rule out loud is what stops it coming back.
*Consolidation:* for `(x + y)²`, substitute x = 3, y = 4: 49 versus 25. One
counterexample, thirty seconds, permanent.
