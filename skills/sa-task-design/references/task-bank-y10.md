# Year 10 task bank

Twelve tasks, fully written, answers verified. Several also work for 10 Methods;
where the senior version differs it is noted.

---

### T10-01 · The coin jar
**Simultaneous equations · Post-teaching · 15 min · `AC9M10A02` · Resilient**

> A jar holds only **20c and 50c coins**. There are **37 coins** and they are
> worth **$12.80**.
> **How many of each?**
> Then: **could a jar of 20c and 50c coins hold 37 coins worth exactly $13.00?
> $12.75? Explain without solving each one.**

*Answers:* 20a + 50b = 1280 and a + b = 37 give **a = 19, b = 18** (19 × 20 +
18 × 50 = 380 + 900 = 1280 ✓).
$13.00 → 20a + 50b = 1300 with a + b = 37 → 30b = 560, b = 18.67 — **impossible**,
not a whole number. $12.75 — **impossible** immediately: every coin is a multiple
of 10c so the total must be too.
*The reasoning payoff is the second part.* Students who solve all three learn
nothing new; students who notice that the total must be a multiple of 10c, and
that 20 × 37 = 740 is the minimum and 50 × 37 = 1850 the maximum, and that the
total changes by 30c per coin swapped, have found the structure.
*Consolidation:* which totals between $7.40 and $18.50 are achievable? (Exactly
those of the form 740 + 30k.)
*Extension:* three coin types. Now what?

---

### T10-02 · Networks: the school tour
**Networks · Deepening · 20 min · `AC9M10SP02` · Resourceful**

> A campus map as a network. Vertices: **Gate, Office, Gym, Library, Canteen,
> Science, Oval**. Edges with walking times in minutes:
> Gate–Office 2 · Gate–Library 5 · Office–Gym 4 · Office–Library 2 ·
> Library–Canteen 3 · Gym–Canteen 2 · Gym–Oval 6 · Canteen–Science 4 ·
> Science–Oval 3 · Library–Science 6
> **a)** Quickest route from **Gate to Oval**?
> **b)** A new student needs to visit **every** building once, starting at the
> Gate. Is it possible? What's the quickest such route?
> **c)** The groundskeeper must walk **every path** at least once and return to
> the Gate. Can it be done without repeating any?

*Answers (all verified).* **a)** **Gate→Office→Gym→Oval = 2 + 4 + 6 = 12
minutes**, the shortest. The tempting near-misses are
Gate→Office→Library→Canteen→Science→Oval = 14 and
Gate→Office→Gym→Canteen→Science→Oval = 15 — both feel shorter because they use
smaller edges, and the single 6-minute Gym–Oval edge looks like the thing to
avoid. It isn't.
**b)** Yes. The quickest route visiting every building once is
**Gate→Office→Library→Canteen→Gym→Oval→Science = 2 + 2 + 3 + 2 + 6 + 3 = 18
minutes**. Note it *ends* at Science, not at the Oval — students who insist on
finishing at the far end of the map do worse.
**c)** Count the degrees: Gate 2, Office 3, Gym 3, Library 4, Canteen 3,
Science 3, Oval 2. **Four vertices have odd degree**, so no closed walk uses every
edge exactly once — an Eulerian circuit needs every vertex to have even degree.
Some paths must be repeated.
*Consolidation:* part (c) is the only one where the *answer is a property of the
network rather than a search*. Ask: "what would have to change to make it
possible?" (Add an edge joining two odd vertices, or remove one.)
*Why this task:* `AC9M10SP02` is new-ish content most textbooks handle badly, and
it is genuinely low-floor — every student can trace a route with a finger.

---

### T10-03 · Half of a half of a half
**Exponential decay modelling · Whole-lesson · 45 min · `AC9M10A04`, `AC9M10A03` · Resourceful**

> A drug leaves the bloodstream so that **half of what is present is gone every
> 4 hours**. A dose puts 100 units in.
> **a)** How much is left after 24 hours?
> **b)** When does it drop below 5 units?
> **c)** A second dose of 100 units is given at 12 hours. Now when does the total
> drop below 5 units?
> **d)** If a dose is given every 12 hours forever, does the amount in the body
> keep growing without limit?

*Answers.* Amount = 100 × (0.5)^(t/4). **a)** t = 24 is 6 half-lives →
100 × 0.5⁶ = **1.5625 units**. **b)** need 0.5^(t/4) < 0.05 → t/4 > log₂20 ≈ 4.32
→ **t ≈ 17.3 hours**. **c)** at t = 12 there are 12.5 units left; adding 100
gives 112.5, decaying from there: 112.5 × 0.5^((t−12)/4) < 5 needs (t−12)/4 >
log₂22.5 ≈ 4.49 → **t ≈ 30 hours**. **d)** **No.** Each 12 hours the previous
amount is multiplied by 0.5³ = 0.125, so the steady state solves
S = 100 + 0.125S, giving **S = 114.3 units** — the body converges to a ceiling.
*Entry:* halve 100 six times. Every student is in.
*Consolidation:* part (d) is the one worth the lesson. A geometric series with
ratio < 1 converges, and here the mathematics is the reason a repeat prescription
is safe. Draw the sawtooth.
*10 Methods version:* do (d) algebraically as a geometric series sum and connect
to the limiting sum formula.
*Related local asset:* Citizen Math *House of Pain* (exponential decay) and
*Pandemic* / *XBOX Xponential* (growth) are in `Citizen math/year 10/`.

---

### T10-04 · Which claim does the data support?
**Bivariate data · Deepening · 20 min · `AC9M10ST03`, `AC9M10ST01` · Reflective**

> Show a scatterplot of ice-cream sales against drowning incidents, month by
> month, with a clear positive association.
> Then three claims:
> **A** "Ice cream causes drowning."
> **B** "There is no relationship — this is a coincidence."
> **C** "Something else explains both."
> **Which does the data support? What extra data would settle it?**

*Answer:* **C**. The data supports *association*, not causation; temperature
drives both. B is also wrong — the association is real, it just isn't causal.
*The extra data:* the same scatterplot with temperature added as a third
variable, or the same two variables within a single month (where temperature
barely varies) — if the association vanishes there, temperature was the driver.
*Consolidation:* students learn "correlation is not causation" as a slogan and
then can't use it. The usable version is the question **"what third thing could
cause both?"** — make them produce a candidate every time.
*Extension — this is the good bit:* ask for a pair of variables in their own
lives with a strong association and no causal link. Shoe size and reading age in
a primary school is the classic.
*Related local asset:* Citizen Math *Pic Me* and *Win at Any Cost* (correlation)
in `Citizen math/year 10/`.

---

### T10-05 · Two machines
**Conditional probability · Post-teaching · 15 min · `AC9M10P01` · Reasoning**

> A factory has two machines. **Machine A** makes **60%** of the items and **2%**
> of its output is faulty. **Machine B** makes the other **40%** and **5%** of
> its output is faulty.
> **a)** What proportion of all items are faulty?
> **b)** A faulty item is pulled off the line. **Which machine most likely made
> it?** What's the probability?
> **c)** Machine B is the newer, faster one. Should it be replaced?

*Answers (verified).* **a)** 0.6 × 0.02 + 0.4 × 0.05 = 0.012 + 0.020 = **0.032**,
i.e. 3.2%. **b)** P(B | faulty) = 0.020 / 0.032 = **0.625** — B most likely, at
62.5%, despite making only 40% of the items. P(A | faulty) = 0.375.
**c)** Genuinely open. B's fault rate is 2.5× A's, but B makes fewer items;
replacing it removes 0.020 of the 0.032, cutting faults by 62.5%.
*The move to teach:* build the table for **1000 items** — 600 from A with 12
faulty, 400 from B with 20 faulty. Every conditional probability is then a
division of two counts, and the reversal (40% of output, 62.5% of faults) is
visible rather than algebraic.
*Consolidation:* "P(faulty given B) is 5%. P(B given faulty) is 62.5%. Why are
they so different?" That question is the whole descriptor.
*Extension:* what fault rate would B need for the two machines to contribute
equally to the faults? (3⅓%.)

---

### T10-06 · What can you work out?
**Goal-free / deductive geometry · Starter · 10 min · `AC9M10SP01` · Resourceful**

> A circle, centre O. Points A, B, C on the circumference. AB is a diameter.
> Angle OAC is marked **32°**.
> **No question. Work out and justify everything you can.**

*Expected:* OA = OC = OB (radii), so triangle OAC is isosceles → angle OCA = 32°
→ angle AOC = 116° → angle BOC = 64° → triangle OBC is isosceles → angles OBC =
OCB = 58° → **angle ACB = 32 + 58 = 90°**, the angle in a semicircle.
*The point:* the class *derives* the angle-in-a-semicircle theorem instead of
being told it, and derives it from the isosceles-triangle fact they already have.
That is inquiry used correctly — deepening an established idea, not delivering a
new one.
*Consolidation:* "would it still be 90° if the angle were 50° instead of 32°?"
Redo it with a letter. The proof falls out.
*Extension:* what if AB is a chord rather than a diameter?

---

### T10-07 · Boxplots that argue
**Data comparison · Starter · 8 min · `AC9M10ST02` · Reflective**

> Two boxplots of the same test, Class P and Class Q, out of 50:
> **P** — min 12, Q1 28, median 34, Q3 39, max 48
> **Q** — min 25, Q1 31, median 33, Q3 36, max 41
> **The head of department says Class P did better. The Year 10 coordinator says
> Class Q did better. Make the strongest case for each.**

*P's case:* higher median (34 vs 33), higher upper quartile (39 vs 36), higher
maximum (48 vs 41), and 25% of P scored above 39 while only 25% of Q scored above
36. P has more high achievers.
*Q's case:* far more consistent — IQR 5 vs 11, range 16 vs 36 — and a much higher
minimum (25 vs 12), so nobody in Q is failing badly. Q has no tail.
*The real answer:* they measure different things, and which matters depends on
what you want from the class.
*Consolidation:* "which single number would you report to a parent, and why?"
Then: "what does the boxplot **not** tell you?" (How many students; whether the
distribution inside each box is even; whether anyone improved.)

---

### T10-08 · Reading the Richter scale
**Logarithmic scales · Post-teaching · 12 min · `AC9M10M02` · Developing understanding**

> The Richter magnitude scale is logarithmic: each whole step is **ten times** the
> ground-motion amplitude, and about **31.6 times** the energy.
> **a)** How much bigger is the shaking in a magnitude 7 than a magnitude 5?
> **b)** How much more energy?
> **c)** A news report says a magnitude 6 quake was "twice as bad" as a magnitude
> 3. **What's wrong with that?**
> **d)** Why use a log scale at all?

*Answers.* **a)** 10² = **100 times** the amplitude. **b)** 31.6² ≈ **1000 times**
the energy. **c)** The reporter has compared the *numbers* 6 and 3, not the
quantities: it is 10³ = **1000 times** the amplitude and roughly **31,600 times**
the energy. **d)** Because the quantities span such an enormous range that a
linear axis is useless — a magnitude 2 tremor and a magnitude 9 quake differ by a
factor of ten million.
*Consolidation:* other log scales they already meet — pH, decibels, the f-stops
on a camera, the way musical octaves work. Ask which of those they'd noticed was
logarithmic.
*Extension:* on a log scale, what does "halfway between 10 and 1000" mean? (100,
not 505 — and that's the whole idea.)

---

### T10-09 · The tank
**Composite solids optimisation · Deepening · 20 min · `AC9M10M01`, `AC9M10M05` · Resilient**

> A water tank is a **cylinder with a hemispherical top and a flat circular
> base**. It must hold **10,000 litres (10 m³)**. The whole outside — base,
> curved side and dome — has to be painted.
> **What radius uses the least paint?** Try r = 1.0, 1.1, 1.2, 1.3, 1.4 m and see.

*Set-up:* volume = πr²h + ⅔πr³ = 10, so h = (10 − ⅔πr³) / πr².
Surface area = 2πrh (side) + 2πr² (dome) + πr² (base).
*Verified values:* r = 1.0 → h = 2.52, SA = 25.24 m² · r = 1.1 → h = 1.90,
SA = 24.52 m² · r = 1.2 → h = 1.41, SA = 24.21 m² · **r = 1.24 → h = 1.24,
SA = 24.18 m²** ← minimum · r = 1.3 → h = 1.02, SA = 24.23 m² · r = 1.4 →
h = 0.69, SA = 24.55 m².
*The result worth finding:* at the minimum, **h = r exactly** — both are
(6/π)^⅓ ≈ 1.2407 m. The class can find this numerically without any calculus, and
the coincidence is the discussion.
*Anticipated:* students expect the tallest or the widest to win and are surprised
by an interior minimum. Someone will notice h shrinks to nothing near r = 1.68 —
worth a minute: past that, the hemisphere alone already holds 10 m³.
*Consolidation:* the curve is flat near the bottom — r = 1.2 and r = 1.3 differ by
0.03 m² of paint. The *practical* answer is "anything around 1.2–1.3 m", and
knowing when precision stops mattering is `AC9M10M04`.
*10 Methods version:* SA simplifies to 20/r + (5/3)πr². Differentiate, set to
zero, get r³ = 6/π exactly.

### T10-10 · Same surface, different deep
**SSDD · Deepening · 15 min · `AC9M10M03`, `A02`, `ST04`, `P01` · Resourceful**

> One picture: a ramp — a right-angled triangle, horizontal run **8 m**, angle of
> elevation **15°** at the bottom.
> **a)** How high is the top of the ramp?
> **b)** The safety code says the ramp must rise no more than 1 m for every 12 m
> of run. Does this ramp pass?
> **c)** Handrails cost $60/m and the sloping surface costs $85/m². The ramp is
> 1.5 m wide with a rail on each side. What's the total cost?
> **d)** Of 80 ramps inspected, 18 failed the gradient test and 25 failed a
> surface test; 9 failed both. What's the probability a randomly chosen ramp
> passed both?
> **Name the topic of each before you solve any.**

*Answers.* **a)** 8 tan 15° = **2.14 m**. **b)** gradient = 2.14/8 = 0.268, i.e.
1 in 3.7 — the code allows 1 in 12 = 0.083, so it **fails badly**. **c)** slope
length = 8 / cos 15° = 8.28 m; two rails = 16.56 m × $60 = $993.80; surface =
8.28 × 1.5 = 12.42 m² × $85 = $1055.90; **total ≈ $2050**. **d)** failed at least
one = 18 + 25 − 9 = 34, so passed both = 46/80 = **0.575**.
*The point:* one picture, four topics — trigonometry, gradient/rates, area and
cost, and a two-way count. Students who read the diagram instead of the question
will reach for tan every time.

---

### T10-11 · Which one doesn't belong: exponentials
**WODB · Starter · 6 min · `AC9M10A03` · Reflective**

> **A** y = 2ˣ · **B** y = 2⁻ˣ · **C** y = 3 × 2ˣ · **D** y = 2ˣ + 3
> **Which one doesn't belong?** A reason for each.

*Reasons:* **B** — the only decreasing one. **D** — the only one whose horizontal
asymptote isn't y = 0, and the only one not of the form k × 2ˣ. **C** — the only
one that doesn't pass through (0, 1) *and* isn't a vertical translation, i.e. the
only pure vertical stretch. **A** — the only one that is *both* a plain power of
2 and increasing; also the only one where y-value equals the "obvious" answer at
every integer x.
*Consolidation:* sketch all four. Which transformations of y = 2ˣ are represented?
(Reflection in the y-axis, vertical stretch, vertical translation.) What's
missing? (Horizontal translation — and y = 2^(x−1) is the same as ½ × 2ˣ, which
is a lovely thirty-second aside.)

---

### T10-12 · Rounding early
**Approximation error · Plenary · 8 min · `AC9M10N01` · Reasoning**

> A calculation: the area of a circle of radius **7.6 cm**, then that area
> multiplied by a height of **12.4 cm** to get a cylinder's volume.
> **Method 1:** round π to 3.14, round the area to the nearest whole cm², then
> multiply.
> **Method 2:** keep everything on the calculator and round only at the end.
> **How different are the answers? Does it matter?**

*Answers (verified):* exact — area = π × 7.6² = 181.458 cm², volume =
**2250.08 cm³**. Method 1 — area = 3.14 × 57.76 = 181.37, rounded to 181; volume =
181 × 12.4 = **2244.4 cm³**. The difference is **5.7 cm³**, about **0.25%**.
*Consolidation:* 0.25% sounds tiny. On a 10,000 L tank it's 25 L. Whether it
matters is a question about the *context*, never about the mathematics — which is
exactly what `AC9M10N01` is asking students to notice.
*Extension:* where did most of the error come from — rounding π, or rounding the
area? (Rounding π to 3.14 loses about 0.05%; rounding 181.458 to 181 loses about
0.25%. The second, by five to one. Students almost always blame π.)
