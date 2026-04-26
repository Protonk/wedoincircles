# THREE-REGISTER-SYNTHESIS

Cross-source synthesis of the three iso/ briefs:
[iso/OSSERMAN-1979-BRIEF.md](iso/OSSERMAN-1979-BRIEF.md) (geometric
Bonnesen route),
[iso/FUGLEDE-1989-BRIEF.md](iso/FUGLEDE-1989-BRIEF.md) (Sobolev
stability route),
[iso/BECK-1994-BRIEF.md](iso/BECK-1994-BRIEF.md) (probabilistic
Diophantine route), with cross-brief findings consolidated in
[iso/DIDOS-PREROGATIVE.md](iso/DIDOS-PREROGATIVE.md) §"Brief findings."

**Register.** Third register per
[CONTRIBUTING.md](CONTRIBUTING.md) — *cross-source synthesis,
load-bearing, expected to hold up under scrutiny*. Each load-bearing
claim below is grounded in explicit witnesses (specific theorem
statements in the three briefs).

**Frame.** The three iso/ briefs survey three independent attacks on
the same inequality `Δ = L² − 4πA ≥ 0` (planar isoperimetric gap)
plus its higher-dimensional and Diophantine relatives. The naive
expectation is that they are alternative methods for one question,
ranked by which gives the sharpest bound. **They are not.** They are
sharp on three distinct *currencies* (rate of decay, geometric
constant, almost-every measure), with three distinct hypothesis
classes that do not nest, and three distinct L-W-safety paths to
transcendence-free re-routing. The non-interchangeability is
structural: each register is the sharp tool for its own
sub-question and a loose proxy for the others. This synthesis
articulates the structural pattern and its operational consequence
for the program.

---

## Claim 1 — Currency-by-Route Map

**Statement.** Each register is sharp on a specific currency. The
sharpness is *currency-specific*, not absolute, and the
non-interchangeability of routes is the structural consequence.

| Register | Sharp on | Loose on |
|---|---|---|
| Fourier / Sobolev (Hurwitz, Fuglede) | **rate** of `Δ_n` decay (`Θ(1/n²)` on inscribed regular `n`-gons) | constant in geometric Bonnesen form (incurs `5π` overhead) |
| Geometric / Hausdorff (Bonnesen 1924, Osserman) | **constant** (`c = 4π` provably best in `Δ ≥ 4π · d²`; equivalently `c = 1` in `(r₂ − r₁)² ≤ Δ_H/(4π)`) | rate on `n`-gon family (loose by 1–2 orders of `n`) |
| Probabilistic Diophantine (Beck, Khintchine) | **almost-every distribution** on `α`-space (Borel-Cantelli convergence-divergence threshold is sharp) | pointwise bound for *specific* `α` (specific points are measure zero) |

### 1.1 Witnesses for the Sobolev rate-sharpness

[iso/FUGLEDE-1989-BRIEF.md](iso/FUGLEDE-1989-BRIEF.md) §2.5,
specialization to inscribed regular `n`-gon:

- Actual `Δ_F = π²/(6n²) + O(1/n⁴) = Θ(1/n²)`
  (Fuglede brief eq., from Hurwitz `Δ_H,n = 4π⁴/(3n²) + O(1/n⁴)` per
  [corners/HURWITZ-GAP.md](corners/HURWITZ-GAP.md)).
- Theorem 1.2 (I.a) bound: `(1/10)(||u||² + ||∇u||²) ≤ Δ ≤ (3/5)||∇u||²`,
  with `||∇u||²₂ = Θ(1/n²)`. Both sides scale as `1/n²` —
  *bound is two-sided sharp up to constants on the regular-`n`-gon family*.
- Constants `(1/10, 3/5)` improvable to `(0.24, 0.54)` per Fuglede
  Remark 1.5 (Fuglede brief §1.2).
- Fuglede footnote 1 traces the `n_dim = 2` ancestry to Hurwitz 1902
  Fourier proof; Hurwitz Parseval identity
  `Δ_H = 4π² Σ m(m−1)|c_m|²` is exact, sharper than the Sobolev
  two-sided bound.

### 1.2 Witnesses for the geometric constant-sharpness

[iso/OSSERMAN-1979-BRIEF.md](iso/OSSERMAN-1979-BRIEF.md) §1.3
(per-inequality table) and §1.1:

- Bonnesen 1924's annulus-width form, Osserman eq. (33):
  `Δ ≥ 4π · d²`, where `d` is the minimum width of a circular
  annulus containing `C`. **Constant `4π` provably best possible**
  (Osserman p. 14: "in 1924, he obtained the constant `4π`, which he
  showed by an example was the best possible").
- Equivalently, `(r₂ − r₁)² ≤ Δ_H/(4π)` — sharp `c = 1` on the right
  side per Bonnesen [2] (Fuglede brief p. 619: "Bonnesen showed that
  the inequality ceases to hold in general if the right-hand member
  is multiplied by a constant `c < 1`").
- The geometric route's *rate* on inscribed regular `n`-gons:
  `(R − ρ)² = (1 − cos(π/n))² ~ π⁴/(4n⁴) = Θ(1/n⁴)` while
  `Δ_H ~ 4π⁴/(3n²) = Θ(1/n²)`. Bonnesen's `Δ ≥ π²(R − ρ)²` (Osserman
  eq. (21), Bonnesen 1921 [19]) gives a lower bound of `O(1/n⁴)` on
  `Δ_n` while the actual is `Θ(1/n²)` — **rate-loose by `n²`**, even
  though the constant `π²` in front is sharp.

### 1.3 Witnesses for the probabilistic almost-every-sharpness

[iso/BECK-1994-BRIEF.md](iso/BECK-1994-BRIEF.md) §1.2 (Theorem 1):

- For almost every `α ∈ R^k` with `k ≥ 2`,
  `Δ(α; N) ≪ (log N)^k · φ(log log N) ⟺ Σ 1/φ(n) < ∞` (Beck
  eq. 2.10). The `⟺` is the Borel-Cantelli convergence-divergence
  threshold; the bound is *exact* up to the `φ` choice — the
  divergence side gives matching lower bounds for infinitely many
  `N`.
- 1-dim case is Khintchine 1923/1924 (Beck eq. 1.17):
  `Δ(α; N) ≪ log N · φ(log log N) ⟺ Σ 1/φ(n) < ∞` for almost every
  `α ∈ R`. Same Borel-Cantelli sharpness.
- **Specific-`α` failure mode.** Beck p. 458: "What is missing here
  is a good lower bound for *every* `α ∈ R^k`." The almost-every
  result tells you nothing about a specific `α` outside the
  measure-1 set. For the program's target `α = π`, specific-α
  pointwise bounds require either external transcendence input or
  the empirical-to-density proxy.

### 1.4 Non-interchangeability — the operational consequence

The three sharpnesses are on *non-comparable* currencies:

- **Sobolev currency** is `||∇u||²` or `Σ |c_m|²` weighted by
  `m(m−1)` — measures the L²-mass of derivative information.
- **Geometric currency** is `(R − ρ)`, `d`, `||u||_∞` — measures the
  Hausdorff distance to a reference disk.
- **Probabilistic currency** is the Lebesgue measure on `α`-space —
  measures how typical a Diophantine property is.

Conversion between currencies is possible but lossy. The
[iso/FUGLEDE-1989-BRIEF.md](iso/FUGLEDE-1989-BRIEF.md) appendix on
the `5π` overhead documents the Sobolev-to-geometric conversion
cost explicitly: chained Sobolev embedding + Cauchy-Schwarz on
`Σ 1/k²` + `(r₂ − r₁) ≤ 2 ||u||_∞` together yield `c = 5π` in
`(r₂ − r₁)² ≤ c · Δ_H/(4π)`, *15.7× weaker* than Bonnesen's direct
`c = 1`. *Each step is sharp in its own register; the chained bound
has slack because no single extremal function realizes all three
sharpnesses simultaneously.*

**Operational consequence.** The choice of route is *currency-fit*,
not aesthetic preference. For program audit calculations:

- Need a tight constant in a Bonnesen-style geometric inequality?
  → Use Bonnesen direct (1924, sharp `c = 4π`).
- Need a tight rate of decay on inscribed regular `n`-gons?
  → Use Hurwitz / strip-`H¹` (`Θ(1/n²)`, sharp).
- Need a typical-α discrepancy estimate?
  → Use Beck / Khintchine (almost-every, with sharp Borel-Cantelli
  threshold).

The three routes are not interchangeable; the program's audit
choices respect the currency-by-route map.

---

## Claim 2 — L-W-Safety Content Map

**Statement.** Each register's *post-1882 calendar timestamp*
(Osserman 1979, Fuglede 1989, Beck 1994) admits a transcendence-free
re-routing path. The substrate that carries the content L-W-safely
is identifiable per register, with outstanding audit targets named.
The audit criterion is *content* not *calendar*, per
[memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md).

| Register | Calendar-late paper | Transcendence-free substrate | Outstanding audit target |
|---|---|---|---|
| Geometric (Osserman 1979) | survey of post-1882 Bonnesen-style | Steiner symmetrization (~1830s, pre-1882) for *qualitative* isoperimetric statement; Fejes-Tóth 1950 polygonal proof for *quantitative* `(R − ρ)²` form | Fejes-Tóth 1950 polygonal proof certification for L-W-safety |
| Sobolev (Fuglede 1989) | post-1882 spherical harmonics + Minkowski parallel bodies | Hurwitz 1902 Fourier proof (per Fuglede footnote 1, p. 619) — calendar-post-1882 but *transcendence-free in content* | Hurwitz 1902 Parseval-form derivation in transcendence-free language (program already has the structural fact in [corners/HURWITZ-GAP.md](corners/HURWITZ-GAP.md); explicit certification not yet written) |
| Probabilistic (Beck 1994) | post-1965 measure-theoretic Diophantine | Roth 1954 (discrepancy, L²-Fourier) + Cauchy-Schwarz + classical Fourier + Borel-Cantelli; **NOT** Roth 1955 (transcendence) | Schmidt 1960's second-moment inequality (Beck Lemma 9.71 input); cleanest single audit task |

### 2.1 Witnesses for the geometric content-path

[iso/OSSERMAN-1979-BRIEF.md](iso/OSSERMAN-1979-BRIEF.md) §"Provenance
tag for the program":

- "All quantitative Bonnesen-style strengthenings in this paper are
  post-1882" (Osserman brief §6, line ~390). Bernstein 1905 [15],
  Bonnesen 1921 [19] / 1924 [20], Hadwiger 1941 [42], Fiala 1941
  [40] — all post-L-W.
- Pre-1882 substrate: **Steiner symmetrization (~1830s)** for the
  *qualitative* isoperimetric inequality `L² ≥ 4πA`. This is the
  pre-L-W proof of the classical inequality; it does *not* recover
  the quantitative `Δ ≥ π²(R − ρ)²` strengthening, which requires
  Bonnesen-style methods.
- Quantitative substrate: **Fejes-Tóth 1950's polygonal exterior-
  parallel-curve proof** (Osserman §1.4 — the technique Osserman
  himself uses in §I.A). Fejes-Tóth's proof "drops the machinery of
  integral geometry and gives direct elementary proofs of the
  formulas needed to prove Bonnesen's inequalities" (Osserman p. 14).
  *Candidate for L-W-safety certification — but the certification is
  not in Osserman.* This is the cleanest audit task on the geometric
  side.

### 2.2 Witnesses for the Sobolev content-path

[iso/FUGLEDE-1989-BRIEF.md](iso/FUGLEDE-1989-BRIEF.md) §1.5
(technique) and §1.4 (precedents):

- Fuglede 1989's spherical-harmonics method on `Σ` is post-1882
  machinery; the Minkowski parallel-body argument is post-1882
  (Minkowski's mixed-volume inequalities, 1903).
- Fuglede footnote 1 (p. 619, quoted in Fuglede brief §1.5):
  "Still another proof — quite short — can be read off from
  Hurwitz' Fourier series proof of the isoperimetric inequality in
  the plane [8], and that leads in a certain sense to a stronger
  inequality, involving a Sobolev 1-norm of the deviation of `∂D`
  from a circle, again estimated in terms of `L² − 4πA`, see [6]."
  Reference [8] is Hurwitz 1902.
- Hurwitz 1902 itself is calendar-post-1882 by 20 years but uses no
  transcendence input. The Parseval identity
  `Δ_H = 4π² Σ m(m−1) |c_m|²` is a Hilbert-space identity on
  `L²(S¹)`, deriving only from Fourier expansion (Fourier 1822) and
  area-perimeter formulas — both pre-1882.
- The program already has the Hurwitz Parseval identity in
  [corners/HURWITZ-GAP.md](corners/HURWITZ-GAP.md), computed three
  ways for the inscribed regular `n`-gon. **The structural content
  is in the program; explicit L-W-safety certification of the
  derivation is not yet written.** This is the audit task on the
  Sobolev side.

### 2.3 Witnesses for the probabilistic content-path

[iso/BECK-1994-BRIEF.md](iso/BECK-1994-BRIEF.md) §2.4 (pre-L-W
audit):

- Beck 1994's main proof uses Poisson summation (Poisson 1827, pre-
  1882), Fejér kernel smoothing (Fejér 1900, classical Fourier),
  second-moment + Cauchy-Schwarz, combinatorial box decomposition,
  and Borel-Cantelli. **None require transcendence input.**
- Critical clarification: Beck's Roth input is **Roth 1954 [17]
  "On irregularities of distribution"** (Mathematika 1, 73–79) —
  the L²-Fourier *discrepancy* lower bound. This is
  *methodologically distinct* from Roth 1955's *transcendence*
  theorem on rational approximations to algebraic numbers
  (Mathematika 2, 1–20). Same author, adjacent year, distinct
  papers. Beck cites only the 1954 paper; the 1955 transcendence
  theorem is not used.
- Schmidt 1960's second-moment inequality (Beck Lemma 9.71, citing
  ref [18]): this is the cleanest single audit point. Beck uses it
  off-the-shelf; certifying it L-W-safely would close the audit on
  Beck's content path. Schmidt 1960 is methodologically L²-Fourier
  metric Diophantine approximation — not transcendence theory — so
  the certification task is plausibly tractable, though not yet
  written.

### 2.4 Synthesis of the L-W-safety map

All three registers admit transcendence-free re-routing in
*content*, despite calendar-post-1882 publication. The audit work
is therefore *certification of specific proofs*, not search for
new substrate. Three concrete audit tasks:

1. **Fejes-Tóth 1950 polygonal proof** (geometric register) — verify
   the exterior-parallel-curve argument uses only pre-1882 elementary
   geometry and induction.
2. **Hurwitz 1902 Parseval derivation** (Sobolev register) — verify
   the Fourier-Parseval identity for `Δ_H` uses only Fourier 1822
   and elementary plane geometry.
3. **Schmidt 1960 second-moment inequality** (probabilistic register)
   — verify the Diophantine metric input uses only L²-Fourier and
   measure theory, no transcendence.

Each task is a candidate -BRIEF; the audit closes the L-W-safety
side of DIDOS-PREROGATIVE for the corresponding register.

---

## Claim 3 — Hypothesis-Class Structure Across Registers

**Statement.** Each register's principal results require a
hypothesis class that does *not* nest within the others. The classes
are not ordered by inclusion; they intersect on specific test cases
(notably the inscribed regular `n`-gon, which is convex,
nearly-spherical for large `n`, and *not* in Beck's measure-1 class)
but each register has theorems that fail outside its own class. The
program needs all three classes to be available, with a *bridge* per
class for program use.

| Register | Hypothesis class | Why class is necessary | Bridge for program use |
|---|---|---|---|
| Osserman / geometric | rectifiable Jordan curves bounding plane domains; quantitative results require *convex* (or extension to non-convex via Schmidt 1939, Fiala 1941) | Bonnesen-style requires `R, ρ` well-defined; in plane only | Direct: inscribed regular `n`-gon is convex Jordan curve |
| Fuglede / Sobolev | nearly-spherical: `‖u‖_∞ ≤ 3/(20n)`, `‖∇u‖_∞ ≤ 1/2` (n_dim ≥ 3 has gradient bound implied by uniform via Lemma 2.2) | Without the hypothesis, stability fails — *spike-on-ball counter-example* (Fuglede §1, p. 621) | Verify hypothesis: for inscribed regular `n`-gon, `‖u‖_∞ = π²/(3n²)` so `n ≥ ?` puts within nearly-spherical class |
| Beck / probabilistic | almost-every `α ∈ R^k` for `k ≥ 2` (1-dim is Khintchine, similar class); Lemmas 4.1–4.4 specify the measure-1 set | Specific `α` is measure zero; the Borel-Cantelli machinery is intrinsically about a measure-1 conclusion | Empirical-to-density proxy ([memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md](memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md) Step 5) bridges almost-every to specific α via averaged-over-range |

### 3.1 Witnesses for hypothesis precision

**Osserman / geometric** — [iso/OSSERMAN-1979-BRIEF.md](iso/OSSERMAN-1979-BRIEF.md):

- Theorem 1 hypothesis: "Let `D` be a plane domain bounded by a
  rectifiable Jordan curve of length `L`. `A`, `ρ`, `R` denote the
  area, inradius, and circumradius of `D`" (Osserman p. 3).
- All quantitative inequalities (11)–(23) in Theorems 2–4 require
  rectifiability; convexity is assumed for the simplest proofs and
  extended to non-convex via Schmidt 1939 [68] / Fiala 1941 [40] /
  Hadwiger 1941 [41].
- **Plane-only.** Higher-dimensional Bonnesen analogs in Osserman §I.B
  require additional hypotheses (Gauss curvature bounded above by
  `M`); these are different theorems, not direct generalizations.

**Fuglede / Sobolev** —
[iso/FUGLEDE-1989-BRIEF.md](iso/FUGLEDE-1989-BRIEF.md) §1.1:

- "Nearly-spherical hypothesis" (Definition 1.1): `‖u‖_∞ ≤ a := 3/(20n)`,
  `‖∇u‖_∞ ≤ 1/2`. For `n_dim ≥ 3` the gradient bound follows from the
  uniform bound (Lemma 2.2). For `n_dim = 2` both must be hypothesized.
- **Necessity of the hypothesis.** Fuglede §1 opener (p. 621), in
  Fuglede brief §1.4: "*it was shown that some restriction like (\*)
  above is necessary for stability — whether in uniform norm or in
  Sobolev 1-norm as in (I.a). (An example is obtained e.g. by adding
  a thin 'spike' to a ball.)*" The spike-on-ball construction has
  small `Δ` but large `‖u‖_∞` — defeating any L^∞ stability without
  a nearly-spherical pre-hypothesis. The Sobolev stability fails for
  the same reason.
- For inscribed regular `n`-gon (Fuglede brief §2.2):
  `‖u‖_∞ = π²/(3n²) + O(1/n⁴)`. The hypothesis `‖u‖_∞ ≤ 3/(20n)`
  becomes `π²/(3n²) ≤ 3/(20n)`, i.e., `n ≥ 20π²/9 ≈ 21.9` — so for
  `n ≥ 22` the inscribed regular `n`-gon is nearly-spherical and
  Fuglede's theorems apply pointwise. (For smaller `n`, Theorem 2.3
  applies if `n_dim ≥ 3`; for `n_dim = 2` and small `n`, Bonnesen
  1924 covers via Theorem 2.3's `n = 2` clause.)

**Beck / probabilistic** —
[iso/BECK-1994-BRIEF.md](iso/BECK-1994-BRIEF.md) §1.2:

- Theorem 1 hypothesis: "for almost every `α ∈ R^k`" with `k ≥ 2`.
- Lemmas 4.1–4.4 (Beck §4) specify the measure-1 set explicitly:
  Lemma 4.1 controls a sum of large terms in the Fourier expansion,
  Lemma 4.2 supplies a Khintchine-style local criterion, Lemma 4.3
  is a divergence Borel-Cantelli for `nα`, Lemma 4.4 gives a series
  convergence on a weighted lattice sum. The intersection of the
  Lemma 4.1–4.4 hypotheses defines Theorem 1's measure-1 class.
- **Specific-α failure mode.** Per Beck brief §2.3: "Beck's headline
  theorems are measure-theoretic; the program targets a specific α
  (= π). Specific points are measure zero; the theorem says nothing
  about specific α." This is the intrinsic limit of the
  probabilistic class.

### 3.2 Why the classes do not nest

Three pairwise non-inclusions:

- **Osserman ⊄ Fuglede.** Osserman's class includes far-from-spherical
  convex curves (e.g., a thin ellipse with eccentricity → 1) which
  fail Fuglede's `‖u‖_∞ ≤ 3/(20n)` hypothesis. Fuglede stability
  fails on such curves; Bonnesen `Δ ≥ π²(R − ρ)²` still holds.
- **Fuglede ⊄ Osserman.** Fuglede's class includes non-convex
  nearly-spherical domains (small spike included, since spike-on-
  ball with small enough spike still satisfies a relaxed
  nearly-spherical condition). Osserman's quantitative theorems
  require convexity directly (extension to non-convex via Schmidt
  1939 et al. is a separate theorem).
- **Beck ⊄ {Osserman ∪ Fuglede}.** Beck's measure-1 class lives in
  `α`-parameter space, not curve-shape space. There is no embedding
  of Beck's hypothesis class into the geometric or Sobolev classes;
  they are about different objects (sequences vs. curves).

The classes intersect on specific test cases. The **inscribed regular
`n`-gon** is in:

- Osserman's class (convex Jordan curve in plane), for all `n ≥ 3`.
- Fuglede's class (nearly-spherical), for `n ≥ 22` per §3.1.
- *Not* directly in Beck's class — the polygon-vertex sequence
  `(k/n) mod 1` for `k = 0, …, n−1` is rational with discrepancy
  exactly `1/n`, not an irrational Kronecker sequence. Beck enters
  the program via the *adjacent* sequence `(n π) mod 1`, which is
  the K-H-L-A target, not the polygon vertex sequence.

So even on the program's central test case, the three registers
attach to *different objects*: Osserman/Fuglede attach to the
polygon as a curve; Beck attaches to a Diophantine sequence
elsewhere in the K-H-L-A apparatus.

### 3.3 Bridges per register

For each register, a bridge is needed to apply the register's
results to specific program targets:

- **Osserman → program**: direct, no bridge needed. Inscribed regular
  `n`-gon is a convex Jordan curve; Bonnesen-style inequalities apply
  pointwise. Loseness on rate is the price; the bound *holds*, just
  loosely.
- **Fuglede → program**: hypothesis verification. For `n ≥ 22` the
  inscribed regular `n`-gon is nearly-spherical and Theorems 1.2 / 2.3
  apply pointwise; the bound is rate-sharp. For `n < 22` the
  uniform-norm hypothesis fails and only `n_dim ≥ 3`'s gradient-from-
  uniform inference is unavailable (we are in `n_dim = 2`); fall
  back to Bonnesen 1924 via Theorem 2.3's `n_dim = 2` clause.
  *Bridge: explicit threshold `n ≥ 22` for hypothesis admission*.
- **Beck → program**: empirical-to-density proxy
  ([memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md](memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md)
  Step 5). Beck's almost-every statements do not certify pointwise
  for `α = π`; the proxy replaces pointwise discrepancy with
  averaged-over-range discrepancy, which is a different quantity for
  which almost-every-style results admit honest interpretation. The
  proxy is the program's bridge from Beck's measure-theoretic
  register to specific-α program targets. *Bridge: empirical-to-
  density proxy, currently a hypothesis at KRAFT-BUDGET-ONE-DIMENSIONAL
  Step 5*.

---

## Synthesis: Three Registers, Three Sub-Questions

The three registers are sharp on three different currencies because
they are answering three different *questions*:

- **Geometric register asks:** *"How close is this fixed convex curve
  to a disk in Hausdorff metric?"* Answer: bounded by `(Δ_H/(4π))^{1/2}`
  with sharp constant `1` (Bonnesen 1924). Sharp on the
  curve-to-disk Hausdorff distance.
- **Sobolev register asks:** *"How concentrated is the Fourier mass
  of this nearly-spherical domain on the m=1 mode?"* Answer:
  `Δ_F = (κ_n + O(small)) (‖u‖² + ‖∇u‖²)` with explicit constants
  `κ_n` (Fuglede 1989). Sharp on the H¹ Sobolev mass.
- **Probabilistic register asks:** *"For a typical irrational `α`,
  how uniformly distributed is `(nα) mod 1`?"* Answer:
  `Δ(α; N) ≪ (log N)^k φ(log log N) ⟺ Σ 1/φ(n) < ∞` (Beck 1994).
  Sharp on the typical-α discrepancy threshold.

These are *distinct questions*. None is a special case of another.
The *non-interchangeability of routes* is therefore not a defect of
the registers but a reflection of the question-multiplicity. The
program's audit choices respect the question-by-currency map: which
route to use depends on which sub-question is being asked.

The K-H-L-A endgame
([memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md](memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md))
is a multi-step argument that touches all three sub-questions:

- The *isoperimetric gap* on inscribed regular `n`-gons is in the
  geometric / Sobolev class. The Hurwitz/strip-`H¹` route is sharp
  on the rate `Θ(1/n²)` (program already has this).
- The *constant* in the discrepancy-to-gap conversion is in the
  geometric class. Bonnesen 1924's sharp `c = 1` is the operational
  reference.
- The *discrepancy of `(n π) mod 1`* is in the probabilistic class
  (or its specific-α specialization via the empirical-to-density
  proxy). Beck's machinery is the methodological exemplar.

The synthesis is therefore not a unification — it is a *map* that
tells the program which register to use for which step. Different
currencies, different L-W-safety paths, different hypothesis classes,
different bridges. The audit is currency-fit, route-by-step.

---

## Closing — Operational Implications for the Program

This synthesis establishes three load-bearing facts the program now
inherits:

1. **Currency-by-route map.** The choice of route for a specific
   audit step is determined by which currency must be sharp.
   Geometric for constants; Sobolev for rates; probabilistic for
   typical-α distributions. Mixing routes incurs conversion overhead
   (the `5π` overhead being the documented case) and should be
   justified case-by-case.
2. **L-W-safety content map.** All three registers admit
   transcendence-free re-routing; the audit work is certification of
   specific proofs, not new mathematics. Three audit tasks named:
   Fejes-Tóth 1950 (geometric), Hurwitz 1902 Parseval (Sobolev),
   Schmidt 1960 second-moment (probabilistic). Each is a candidate
   future -BRIEF.
3. **Hypothesis-class structure.** No nesting; bridges per register.
   Inscribed regular `n`-gon is in Osserman/Fuglede classes
   (pointwise) but not Beck's (which targets `(nα) mod 1`, not the
   polygon vertices). Program use of Beck requires the empirical-to-
   density proxy; Fuglede's threshold for nearly-spherical
   admission is `n ≥ 22` for inscribed regular `n`-gons.

The program does not need to choose one register; it needs to use
each at its sharp currency, with the bridges and audit tasks
acknowledged. This synthesis is the operational map.

---

## Trust Boundary

This memo should be cited for:

- The currency-by-route map (Claim 1) and its operational consequence
  for audit step selection.
- The L-W-safety content map (Claim 2) and the three named outstanding
  audit tasks.
- The hypothesis-class structure (Claim 3) and the per-register
  bridges, including the explicit `n ≥ 22` threshold for Fuglede on
  inscribed regular `n`-gons and the empirical-to-density proxy as
  the Beck bridge.
- The synthesis claim that the three registers answer three distinct
  sub-questions, hence the non-interchangeability is structural not
  defective.

This memo should NOT be cited for:

- Any new isoperimetric or discrepancy theorem; the synthesis
  contains no new mathematics, only a reading of the three iso/
  briefs.
- Closure of any of the three audit tasks (Fejes-Tóth, Hurwitz,
  Schmidt 1960); these are flagged as outstanding.
- Direct K-H-L-A audit conclusions; the synthesis informs the
  K-H-L-A audit but does not perform it.

Per
[memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md), this
memo's L-W-safety status: methodologically post-1965 synthesis of
three post-1882 papers. Content reduces to facts about the briefs,
which themselves trace to pre-1882 substrate per the audit map in
Claim 2. *The synthesis is L-W-safe in content; the underlying
briefs are post-1882 but transcendence-free in their re-routing
paths.*
