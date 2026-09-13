# Sourcing protocol — find the real task before writing one

**Binding.** This file governs step 2 of the design sequence in `SKILL.md`.

The failure this file exists to prevent: Claude reads the source catalogue,
recognises the *genre* ("this wants an estimation task"), and then writes its own
estimation task from the genre recipe — without ever opening estimation180.com.
The result looks plausible and is worse than the original in every way that
matters: no photo, no reveal, wrong register, a level that drifts, and formatting
that does not match what the class has seen before.

**A source catalogue is a retrieval instruction, not a bibliography.** Naming
`openmiddle.com` in the output while having authored the problem yourself is the
specific thing that must stop.

---

## The search ladder

Work down it. Stop at the first rung that yields two or more usable candidates.
Do not skip a rung because you can imagine what it would contain.

### Rung 1 — the school's own drive
If class/topic folders are connected, `ls` and `grep` them before anything else.
Citizen Math handouts and teacher guides, downloaded 3-act media, and previously
built task slides live here. A held local copy beats an equivalent web task every
time: it is complete, it has a teacher guide with expected responses, and the
formatting already matches what this department uses.

Also read any `local-assets.md` alongside this file.

### Rung 2 — the live source sites
**When there is internet, this rung is mandatory for every media-dependent genre
and expected for every other genre.** Use `WebFetch` / `WebSearch` against the
specific sites in `source-catalogue.md` — go to the topic index, not the
homepage. Landing pages are thin; the tasks are on the inner pages.

| Genre | Where to actually go | What to bring back |
|---|---|---|
| Estimation | `estimation180.com/days` — days grouped in 20s | The **photo URL**, the day number, the question stem, the **answer/reveal** |
| WODB | `wodb.ca/shapes.html`, `/numbers.html`, `/graphs.html`, `/incomplete.html` | The **image of the 2×2 grid**, plus your own four reasons written out |
| Open Middle | `openmiddle.com` → topic → problem page | The **exact wording of the constraint**, the skeleton, the source link. Verify the optimum yourself (step 7) |
| Same But Different | `samebutdifferentmath.com` → domain | The **image pair** |
| Maths Venns | `mathsvenns.com` (note the *s*) → strand | The **Venn image**, the two/three criteria verbatim, the empty-region answer |
| Slow reveal graphs | `slowrevealgraphs.com` → graph type or theme | The **full reveal sequence of images, in order**, and the source of the data |
| Visual patterns | `visualpatterns.org` → numbered pattern | The **step 1–3 image** and the stated count at step 43 |
| Goal-free | `goalfreeproblems.blogspot.com` → strand | The **diagram**, with the question already removed |
| Error analysis | `mathmistakes.org` | The **photo of real student work** — an authentic error beats an invented one |
| 3-act | `three-act-catalogue.md` for the task, then `101qs.com` / `gfletchy.com` / `tapintoteenminds.com` / the author's post for the media | Act 1 video or image, Act 2 information, Act 3 reveal, the sequel |
| Non-routine | `playwithyourmath.com`, `nrich.maths.org`, `mathpickle.com`, `problemo.edu.au` | The problem as published, plus teacher notes/solution where offered |
| Whole-lesson modelling | Citizen Math (rung 1 first), `citizenmath.com/lessons` | Lesson name, the split point from the teacher guide |

### Rung 3 — the offline bank
`task-bank-y7.md` … `-y10.md`. **These 48 tasks are themselves authored
equivalents, not sourced originals.** They exist so the skill still works with no
internet, and they are fine to use — but when the connection is up and the genre
is media-dependent, a real Estimation 180 day beats a bank task that describes a
photo nobody can see.

### Rung 4 — author it yourself
Only when rungs 1–3 have been genuinely worked and produced nothing that fits the
year level, topic, slot and time. See SKILL.md step 6 — this rung carries an
obligation to say what was searched, and to match a real exemplar's format.

---

## Media-dependent genres — never fabricate these

These genres **are** their media. A described photo is not a photo; a student
cannot estimate from a paragraph telling them there is a jar.

> Estimation · Slow reveal graphs · Visual patterns · Three-act modelling ·
> WODB where the four items are images · Same But Different · Error analysis
> using real student work · Citizen Math

For these, the permitted outcomes are, in order:

1. **Embed the actual media.** Fetch the image and put it on the slide with
   `replace_picture` (see `slide-patterns.md`). Attribute it on the slide.
2. **Link it, in full, on the slide and in the speaker notes** — the exact page
   URL, not the site homepage — so the teacher opens it live in the room. Say in
   the output that the media was not embedded and why.
3. **Only if 1 and 2 both fail:** substitute a *different* genre that does not
   need media, and say plainly that you did.

Authoring a fake one is never on this list. If you cannot get the photo, you do
not have an estimation task.

---

## Copying: what may be lifted, and how

`source-catalogue.md` carries the per-source licence verdicts. In practice:

**On a slide, shown in class:** any of these sources may be shown with the site
named on the slide. Classroom display is what they are for. Reproduce the prompt
wording as published — rewording a published task into your own words is how the
level and register drift.

**On a printed handout that leaves the room:** only Don Steward (CC BY-NC-SA),
CC-BY 3-act tasks, and MathPickle may be reproduced outright, with attribution.
For everything else, put the task on a slide, or print with attribution for
in-class use only, or — as a last resort — author an equivalent, in which case
step 6 of the design sequence applies in full and the output must say the task is
an original inspired by *X*, not that it came from *X*.

**Never** present an authored task as though it were sourced. The `**Source**`
line in the output template is not decorative.

---

## When a fetch fails

Sites go down, Padlet never renders, Hungry Teacher blocks robots, and 101qs is
ageing. When retrieval fails:

- Try one alternative route (the topic index instead of the homepage; a web
  search for the task name plus the site).
- Then fall to rung 3, and say in the output which link could not be read.
- Do **not** silently substitute an authored task for a failed fetch. That is the
  exact drift this file prevents, wearing a good excuse.
