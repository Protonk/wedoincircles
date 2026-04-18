# BRESENHAM-MIDPOINT

A search memo on Bresenham's midpoint circle algorithm and whether it belongs in the compute-cost program laid out in `memos/COUNTING-APPARATUS.md` — as an upper-bound benchmark for item (A)'s compute model, as a combinatorial cousin of the counting word `M_N`, or as neither (noted and set aside).

The algorithm is, by 1977, the canonical integer-arithmetic procedure for rasterizing a circle of radius `R` on the square lattice `ℤ²`. The question here is not whether it works — it plainly does, and has for half a century of graphics hardware — but what it *is*, viewed from this program's angle: an exact integer-arithmetic compute model for the circle, whose output is a deterministic word on an alphabet of pixel steps, with a half-pixel error bound and eightfold symmetry. Each of those four nouns has a search direction attached.

---

## The algorithm, named precisely

The object referred to as **"Bresenham's midpoint circle algorithm"** in graphics textbooks and Wikipedia is a specific decision-variable-driven procedure that steps through one octant of a circle of integer radius `R` centered at the origin, emitting a pixel per unit x-step, choosing at each step between "E" (east, keep `y`) and "SE" (southeast, decrement `y`) according to the sign of a decision variable derived from evaluating the implicit circle equation `F(x, y) = x² + y² − R²` at the midpoint between the two candidate pixels.

Standard textbook initialization: `d₀ = 1 − R` for the unscaled midpoint variant, or `d₀ = 5 − 4R` for the scaled integer variant (Hearn–Baker). Update rules: `d ← d + 2x + 3` on "E" and `d ← d + 2(x − y) + 5` on "SE". Primitive ops per step: constant (five, in the Zingl 2014 "beauty" formulation), all integer additions/shifts.

**Citation chain** (each paper searchable independently by author, year, and venue):

- **Bresenham 1965.** J. E. Bresenham, *"Algorithm for computer control of a digital plotter,"* IBM Systems Journal **4**(1), 25–30. The line algorithm. Presented earlier at the 1963 ACM National Conference, Denver.
- **Horn 1976.** B. K. P. Horn, *"Circle generators for display devices,"* Computer Graphics and Image Processing **5**(2), 280–288. An addition-and-shift-only circle generator; one of the predecessors to the midpoint variant.
- **Bresenham 1977.** J. E. Bresenham, *"A linear algorithm for incremental digital display of circular arcs,"* Communications of the ACM **20**(2), 100–106. The direct extension of the 1965 line algorithm to circular arcs.
- **Pitteway 1967.** M. L. V. Pitteway, *"Algorithm for drawing ellipses or hyperbolae with a digital plotter,"* Computer Journal **10**(3), 282–289. The conic-section generalization. Wikipedia credits "the midpoint variant" to joint Pitteway–Van Aken influence.
- **Van Aken 1984.** J. R. Van Aken, *"An efficient ellipse-drawing algorithm,"* IEEE Computer Graphics and Applications **4**(9), 24–35.
- **Van Aken & Novak 1985.** J. R. Van Aken and M. Novak, *"Curve-drawing algorithms for raster displays,"* ACM Transactions on Graphics **4**(2), 147–169. The consolidated treatment that names the midpoint-selection criterion and proves its half-pixel error bound for conics.
- **Zingl 2014.** A. Zingl, *"The beauty of Bresenham's algorithm"* (web monograph, `zingl.github.io`). The minimal five-op-per-step formulation widely quoted in modern implementations.
- **Klette & Rosenfeld 2004.** R. Klette and A. Rosenfeld, *Digital Geometry: Geometric Methods for Digital Picture Analysis*, Morgan Kaufmann. The textbook treatment in the digital-geometry tradition; ties rasterization to word-theoretic and number-theoretic structure.

The naming is slightly contested: the same object is written in the literature as "Bresenham's circle algorithm," "midpoint circle algorithm," "Bresenham midpoint circle algorithm," and — in German-language sources — attributed substantially to Horn. This memo uses "Bresenham-midpoint" as a compound referring to the canonical 1977 / Pitteway–Van Aken object, without taking a side on priority.

---

## Why this is plausibly in the program

Four separate entry points into the work already in the repo:

1. **Compute-model candidate for `memos/COUNTING-APPARATUS.md` item (A).** The Bresenham-midpoint procedure is an existence proof: a circle of radius `R` can be rasterized with `O(R)` integer additions/comparisons and a bounded half-pixel error. That is a concrete *upper bound* on the cost of beating any less precise circle surrogate at lattice resolution. The COUNTING-APPARATUS search currently names three candidate compute models (ruler-and-compass, algebraic-arithmetic over ℚ, algebraic straight-line programs); Bresenham-midpoint lives natively in the ASLP register, but with all arithmetic over `ℤ` rather than `ℚ`, and with *no* field extensions — it is strictly weaker than algebraic-arithmetic-over-ℚ, and that restriction is what makes it interesting as a benchmark floor.
2. **Upper-bound benchmark analogous to Chudnovsky on the π side.** `memos/RAMANUJANS-COMPLIMENT.md` notes that the circle-side program needs upper-bound rates to evaluate any lower-bound claim against. Chudnovsky 1988 supplies the rate for π at full precision. Bresenham-midpoint supplies the rate for the *whole circle at lattice resolution* — a different regime (coarse precision, every point on the curve) where the Chudnovsky-class CM-point series is overkill. The two upper-bound sources are complementary, not competing.
3. **Combinatorial cousin of the counting word `M_N`.** The sequence of "E" / "SE" decisions emitted by the algorithm over one octant of a radius-`R` circle is a deterministic binary word of length approximately `R/√2`, with structure controlled by the slope of the circle at each step. On the *line* side, this is the Bresenham / mechanical / Sturmian / Christoffel-word correspondence, well-documented in combinatorics-on-words (Lothaire, Berstel, Pirillo). On the *circle* side, the word is no longer Sturmian — the slope is non-constant — but its local structure is governed by the Stern–Brocot convergents of the local tangent slope. This is a direct invitation to compare against `n-gons/counting/` where `M_N` already records a similar kind of lattice-incidence word over a related sweep.
4. **Octant symmetry vs. crystallographic restriction.** Bresenham-midpoint's eight-fold symmetry (the octant mirror group) is the natural symmetry of the *square lattice ℤ²*, not of the circle. Niven's crystallographic restriction (see `BNHA/triad/NIVEN-THREE-WAYS.md`, `memos/CRYSTALLOGRAPHIC-RESTRICTION-BRIEF.md`) fixes the compatible rotational orders at `{1, 2, 3, 4, 6}` — the four-fold nests inside the eight-fold by factor of two, but the six-fold and three-fold do not. A Bresenham-midpoint procedure on a triangular / hexagonal lattice would have sixfold symmetry and would look structurally different; such a variant either exists in the digital-geometry literature or is a gap, and that is itself a search item.

None of these four is a decided link to the main argument. They are the reasons to hold the memo open.

---

## (A) Compute-cost accounting in the integer-arithmetic model

**What it is.** A formal statement of the cost, in Bresenham-midpoint's own primitive ops (integer add, integer compare, shift), of rasterizing a radius-`R` circle.

**What's known** (from the cited literature):

- Per-pixel cost: constant (Zingl's five-op formulation is the tightest published).
- Pixels per octant: `⌈R/√2⌉` (the second octant spans x ∈ [0, R/√2], one pixel per unit x-step).
- Pixels per full circle: `8 · ⌈R/√2⌉ ≈ 4√2 · R`. Standard graphics-textbook figure.
- Error bound: at most half a pixel from the true circle, at every emitted pixel (Van Aken–Novak 1985 is the canonical proof reference).
- Register width: `O(log R)` bits, so each primitive op is `O(log R)` bit ops under a uniform-cost model or `O(M(log R))` under a bit-cost model with Karatsuba-class multiplication. For the compute-cost bind, uniform-cost is probably the honest register.

**What's unknown** for this program's purposes:

- Whether "rasterize a circle at lattice resolution" is the right task to feed into `memos/COUNTING-APPARATUS.md` item (B). Rasterizing a single circle is not the same task as the outside-out corner sweep over `n ∈ [3, N]`. The cost of doing Bresenham-midpoint *once per `n`*, summed, is `O(N²)` integer ops, which gives a candidate upper-bound rate — but the cost measure `|M_N|` in the counting apparatus may not line up with this.
- Whether a matching *lower* bound exists in the literature. The folklore claim "Bresenham is optimal" (see the 2022 *Possibly Wrong* blog analysis) is a closeness-of-pixel-choice statement, not a primitive-op lower bound. An actual `Ω(R)` lower bound in an appropriate compute model would be very useful and may not exist in a usable form.

**Search moves:**

- Check Blum–Shub–Smale 1998 (*Complexity and Real Computation*) and Bürgisser–Clausen–Shokrollahi 1997 (*Algebraic Complexity Theory*) for any circle-specific or convex-curve-specific lower bound results.
- Check if the Brent–Zimmermann 2010 (*Modern Computer Arithmetic*) treatment of "constant-precision arithmetic on implicit curves" pulls Bresenham in as a reference point.

---

## (B) Combinatorial structure of the pixel word

**What it is.** A description of the "E" / "SE" output sequence of one octant of a Bresenham-midpoint run, as a word over `{E, SE}`, with enough structure stated to compare against the counting apparatus output.

**What's known**:

- On the *line* side (Bresenham 1965), the digital-line word of slope `p/q` is a Christoffel word of slope `p/q`, and its structure is given by the continued-fraction expansion of `p/q` via the Stern–Brocot tree. See the survey "Digital lines, Sturmian words, and continued fractions" (available via DiVA, Uppsala, and Berstel's 2008 chapter "Combinatorics on Words: Christoffel Words and Repetitions").
- On the *circle* side, the slope varies continuously along the arc, so the output word is not Sturmian. It is, at best, a concatenation of Christoffel-like segments where the local slope is approximately rational of small denominator. The digital-geometry literature (Bhowmick–Bhattacharya, Klette–Rosenfeld) treats "digital circles" as combinatorial objects but — as of this writing, unchecked — tends not to state the output as a word in the combinatorics-on-words register.

**What's unknown**:

- Whether anyone has explicitly factored a Bresenham-midpoint circle word into Christoffel segments keyed to rational tangent slopes along the octant.
- Whether such a factorization, if it exists, aligns with the Stern–Brocot structure the repo already uses in `n-gons/stern_brocot.sage` and `memos/CONTINUED-FRACTIONS-CROSSWALK.md`.
- Whether the word's length, as a function of `R`, admits a *combinatorial* cost measure (e.g., sum of continued-fraction partial quotients of some associated real) that differs meaningfully from the raw pixel count.

**Search moves:**

- Look at Brlek–Labelle–Lacasse's work on digital-curve word factorizations (e.g. "Incremental algorithms based on discrete Green theorem," Berstel–Brlek et al.), which treats boundary words of digital regions. "Digital circle" as a boundary word is the relevant keyword.
- Check the IWCIA (International Workshop on Combinatorial Image Analysis) proceedings for Bhowmick / Bhattacharya / Das on digital circularity.

---

## (C) Octant symmetry vs. crystallographic restriction

**What it is.** The observation that Bresenham-midpoint's symmetry group (dihedral `D_4`, order 8, the symmetries of `ℤ²`) is the ambient lattice's symmetry, not the circle's, and that this forces an asymmetry between "how the algorithm sees the four-fold rotational center" and "how the algorithm sees the six-fold rotational center" — because on `ℤ²`, the six-fold does not exist.

**Implication for the program.** The counting apparatus in `n-gons/counting/` is set on `ℤ²` as well (raster / strip coordinates), and so it inherits the same asymmetry. The Niven crystallographic set `{1, 2, 3, 4, 6}` is `ℤ²`-friendly at orders 1, 2, 4 and `triangular-lattice-friendly` at orders 1, 2, 3, 6. The shared-friendly orders are `{1, 2}`. Everything else gets handled asymmetrically. Bresenham-midpoint is a concrete witness to how this asymmetry shows up in a concrete circle-approximation procedure, which is exactly the kind of witness the τ-portrait in `memos/COUNTING-APPARATUS.md` item (C) has been trying to articulate.

**What's unknown**:

- Whether a "hexagonal Bresenham" for the triangular lattice `A_2` exists and has been published. The keyword to search is "hexagonal raster," "A2 lattice," "triangular grid circle rasterization." Amidror's *Mastering the Discrete Fourier Transform in One, Two or Several Dimensions* discusses hexagonal sampling; its circle-drawing treatment (if any) would be the starting point.
- Whether the natural two-lattice object (square + triangular, each with its own Bresenham-midpoint) reproduces the crystallographic restriction as an *output* property rather than an input assumption.

---

## (D) Relation to the counting apparatus `M_N`

**What it is.** A direct comparison of the Bresenham-midpoint octant word for a circle of radius `R = N` against the counting word `M_N` produced by `n-gons/counting/outside_out.py`.

**What's known**:

- `M_N` is a raster / word-like output over a corner-count multiplicity raster, keyed to X-values on `[−1, 1]` at the unit-circle scale. See `n-gons/counting/COUNTING.md`, `n-gons/counting/build_x_multiplicity_raster.py`.
- Bresenham-midpoint-on-radius-`N` is a raster / word-like output over a pixel-presence raster, keyed to lattice X-values on `[0, N]` at the radius-`N` scale.
- Both are integer-arithmetic-exact.
- Both have length `Θ(N)`.

**What's unknown**:

- Whether they are the same kind of object up to coordinate change (promising but not obvious), or structurally different because one records *inscribed-polygon-corner-incidence* and the other records *circle-tangent-direction*.
- Whether running Bresenham-midpoint on the exact circle associated with the counting apparatus (the unit circle, rescaled to integer resolution `N`) and comparing against `M_N` produces a matched pair of words with a legible correspondence, or two words that drift apart in a way that itself is interesting.

**Search moves:**

- Run Bresenham-midpoint at `R = N` for `N ∈ [8, 64]`, alongside the existing `M_N` pipeline, and diff the outputs. This is a small script, and could live at `n-gons/counting/compare_bresenham.py` or similar. If the words match up to reflection, that closes one of COUNTING-APPARATUS item (D)'s open questions. If they don't, the shape of the mismatch is the finding.

---

## Adjacent anchors

Existing material this memo draws on:

- `memos/COUNTING-APPARATUS.md` — the parent search, specifically items (A) compute model, (B) task statement, (C) τ portrait, (D) small-case walkthrough.
- `memos/RAMANUJANS-COMPLIMENT.md` — the sister memo on upper-bound benchmarks; Bresenham-midpoint is the lattice-resolution counterpart to Chudnovsky's full-precision rate.
- `corners/PSEUDO-CHEBYSHEV-NODES.md` — algebraic-degree catalog; the `round(2cos(2π/n))` surrogate. Bresenham-midpoint is a compute-model instance of exactly the same round-to-integer operation, applied to the whole circle rather than a single node.
- `memos/CRYSTALLOGRAPHIC-RESTRICTION-BRIEF.md`, `BNHA/triad/NIVEN-THREE-WAYS.md`, `memos/MIZAR-NIVEN-FOREBODING.md` — the crystallographic-restriction side; relevant to item (C).
- `memos/CONTINUED-FRACTIONS-CROSSWALK.md`, `n-gons/stern_brocot.sage` — the CF / Stern–Brocot machinery that the Christoffel-word angle in item (B) plugs into.
- `n-gons/counting/COUNTING.md` and the full `n-gons/counting/` directory — the comparison target for item (D).
- `n-gons/ARCHIMEDEAN-STRIP-FLIP.md`, `BNHA/triad/Eraserhead/ARCHIMEDEAN-CONSTRICTION.md` — the exhaustion tradition; Bresenham-midpoint is an integer-lattice descendant of Archimedean exhaustion.
- `memos/LANDFALL-EXPORT.md` — the log-side template; Bresenham-midpoint is the circle-side answer to "what plays the role of Mitchell's `L(x) = E + m`?" for lattice resolution rather than mantissa precision.
- `memos/LINDEMANN-BRIEF.md` — the transcendence boundary; Bresenham-midpoint gets arbitrarily close to π at `R → ∞` with integer-arithmetic only, which is a quantitative sharpening of "Lindemann is the `E = ∞` corner."

Anchors yet to be written:

- Possibly `memos/DIGITAL-GEOMETRY-BRIEF.md` — a source-facing brief on Klette–Rosenfeld 2004 and the digital-geometry tradition, if item (B) turns out to need it. Deferred until a specific result from that literature becomes load-bearing.

---

## What this memo is not

- **Not a graphics tutorial.** The algorithm is well-documented elsewhere (Wikipedia, any intro computer-graphics textbook). This memo names citations and connections, not pedagogy.
- **Not a commitment to inclusion.** It is an open question whether Bresenham-midpoint belongs in the compute-cost program. The memo is the place that question gets worked out.
- **Not a proof, not a paper plan.** Paper-plan work lives at `BNHA/triad/Creati/INSCRIPTION-PAPER-PLAN.md`; the parent search lives at `memos/COUNTING-APPARATUS.md`. This memo is upstream of both.
- **Not a scan-conversion engineering review.** Engineering details (antialiasing, subpixel accuracy, hardware implementation, FPGA variants) are noted only where they touch the compute-model question. The 2021 *ResearchGate* FPGA paper and the 2023 *Springer* "enhancements" paper are not load-bearing for this program and should not be read unless a specific item pulls them in.

---

## Exit criteria

The memo freezes and its content migrates when *any one* of the following triggers:

1. **Item (A) resolved.** Bresenham-midpoint is committed as the compute-model upper-bound benchmark for `memos/COUNTING-APPARATUS.md` item (A) (and promoted there), or explicitly ruled out (and noted there as "considered and rejected because …").
2. **Item (D) resolved.** The comparison script in `n-gons/counting/` either shows Bresenham-midpoint's octant word matches `M_N` under a legible coordinate change (promote finding to `n-gons/counting/COUNTING.md`), or shows they are structurally different in a specific way (promote the mismatch-shape to the same file as a finding).
3. **Item (B) resolved or stalled.** Either the Christoffel-segment factorization of the circle-word is established from existing literature (promote a short writeup to `memos/CONTINUED-FRACTIONS-CROSSWALK.md`), or two directed reads turn up nothing load-bearing (note it here, move on).
4. **Bresenham-midpoint loses relevance.** If the main argument takes a turn that makes integer-arithmetic-on-`ℤ²` irrelevant — e.g., the compute model commits to algebraic-arithmetic-over-ℚ and never revisits the integer-only register — the memo freezes as historical record.

---

## Status

Open search memo. No directed reads completed. No comparison script written. The four items above are the active queue; item (D) is the cheapest to attempt and the most likely to produce an immediate finding, so it is first in line whenever work resumes on this memo.
