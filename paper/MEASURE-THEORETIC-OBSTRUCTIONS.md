# MEASURE-THEORETIC OBSTRUCTIONS

Substrate-side measure-theoretic typing of the five angles in
[paper/IMPOSSIBILITY-OUTLINE.md](paper/IMPOSSIBILITY-OUTLINE.md) §5.
Each entry: (ID) what the angle is; (Connection to measure theory)
the specific measure-theoretic object the angle invokes; (Measure-
theoretic obstruction) the specific non-availability the structure
carries. Sister to
[paper/LANDFALL-EXPORT.md](paper/LANDFALL-EXPORT.md) (proof-template
repository) and [fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md)
(candidate concrete realization of `δ`).

This file is strictly source-side. Each row is supported by a
citable fact in standard measure theory, Diophantine analysis, or
the program's audited literature. Implications and methodological
readings live elsewhere.

---

## 1. Rotation-orbit Diophantine kinematics (§5.1)

**ID.** The Diophantine spectrum places real `α` according to its
irrationality exponent. Liouville numbers admit unbounded exponent;
algebraic irrationals are constrained to exponent 2 (Roth 1955);
typical irrationals have finite irrationality measure. The
Avila–Jitomirskaya parameter `β(α) = limsup (ln q_{n+1}) / q_n`
satisfies the one-way implication: finite irrationality measure
implies `β(α) = 0`, and `β(α) > 0` implies `α` is Liouville. The
converse fails — some Liouville `α` can still have `β(α) = 0`.
Existing finite irrationality-measure bounds for `π` (e.g., Salikhov
2008 and predecessors) therefore imply `β(π) = 0`; they do not
imply `π` lies on the Roth `μ = 2` boundary, and the `β` parameter
alone does not characterize non-Liouville. The orbit
`{kα mod 1 : k ∈ ℤ}` is the kinematic substrate the algorithm
operates on.

**Connection to measure theory.** Haar measure on `T = ℝ/ℤ`
(equivalently, normalized Lebesgue measure on `[0, 1)`) is the
unique translation-invariant Borel probability measure. Weyl's
equidistribution theorem (Weyl 1916,
`sources/uber-die-gleichverteilung-von-zahlen-mod-eins-2liqw01yl8.pdf`):
for any irrational `α`, the sequence `{kα mod 1}_{k≥1}`
equidistributes against Haar — i.e., for every continuous
`f : T → ℂ`,

```text
(1/N) ∑_{k=1}^{N} f(kα mod 1)  →  ∫_T f dμ_Haar     as N → ∞.
```

By standard approximation, the same convergence extends to
Riemann-integrable `f` and to indicator functions of intervals
whose boundary has Lebesgue measure zero. Convergence rate is
controlled by the irrationality exponent of `α` (Erdős–Turán and
Erdős–Turán–Koksma discrepancy bounds; see
`memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md`).

**Measure-theoretic obstruction.** For continuous and
Riemann-integrable test functions, the asymptotic time-average
along the orbit is fixed by the Haar integral — the orbit cannot
deviate from the Haar mean against this class of statistics.
Distinguishing information at this regularity is consequently
unavailable beyond Haar.

---

## 2. Non-nesting isoperimetric registers (§5.2)

**ID.** Isoperimetric phenomena admit three distinct quantitative
readings on plane curves and their analogues: *rate* — asymptotic
decay of the deficit `L² − 4πA` along a sequence approaching a
circle (the polygon family `Δ_n ~ 4π⁴/(3n²)` is the program's
worked instance); *constant* — pointwise sharp geometric
inequality, owned by the Bonnesen-strengthening `L² − 4πA ≥
π²(R − r)²` per Osserman 1979 §3 / Bonnesen 1921; *almost-every*
— full-measure claims about families parameterized by a stated
measure on `ℝ^k`, in the Khintchine / Beck tradition (Beck 1994
Theorem 1, eq. 2.10, with the Borel–Cantelli
convergence-divergence threshold giving matched upper-and-lower
bounds for almost every parameter; see
`iso/THREE-REGISTER-SYNTHESIS.md` §1.3 and
`iso/BECK-1994-BRIEF.md`). Fuglede 1989's Sobolev / stability
inequalities sit elsewhere in the repo's iso taxonomy
(rate-sharp rather than constant-sharp) and are not invoked here.

**Connection to measure theory.** Each register is a distinct
measure-theoretic operation on a curve family. *Rate* corresponds
to asymptotic-density readings: `lim_n` of normalized deficit.
*Constant* corresponds to pointwise-Lebesgue inequalities — sharp
ratios of Lebesgue-measured area to length-squared. *Almost-every*
corresponds to full-measure claims under a distribution on the
parameter space; equivalently, integrals of indicator functions
against a parameter-space measure.

**Measure-theoretic obstruction.** The three registers do not
nest. Knowing rate does not imply knowing constant: a family
saturating asymptotic decay can have suboptimal sharp constants.
Knowing constant does not imply knowing almost-every: a single
sharp curve does not control the typical curve under a distribution.
Knowing almost-every does not imply knowing rate: a generic curve
in a measure can be far from any asymptotic-saturating sequence.
No measure-theoretic equivalence functor between the three
registers exists; each requires its own argument.

---

## 3. Closed-form polygon arithmetic (§5.3)

**ID.** Closed-form values of regular polygon families that arise
in the program: Hurwitz coefficients on the sparse lattice
`m ≡ 1 mod n` (Hurwitz 1902, computed via geometric-sum / Fourier
coefficient expansion on the polygon's vertex set); the
Archimedean gap `Δ_n ~ 4π⁴/(3n²)` (per
[figures/hurwitz_gap_rate.png](figures/hurwitz_gap_rate.png), build
script [corners/hurwitz_gap.sage](corners/hurwitz_gap.sage)); the
first-band concentration constant
`B_1(n) / Δ_n → 6/π² = 1/ζ(2)` (per
`corners/HURWITZ-FIRST-BAND-CONCENTRATION.md` §1, lines 60–95).

**Connection to measure theory.** The first-band concentration
arises from a `ζ(2)`-tail comparison: paired-band terms `B_j(n)`
(corners memo §1) satisfy `B_j(n) ≤ B_1(n) / j²` for every
`j ≥ 1`, so `Δ_n = ∑_{j ≥ 1} B_j(n) ≤ B_1(n) · ∑_{j ≥ 1} 1/j² =
B_1(n) · ζ(2)`. The first band's share of the total gap is
therefore at least `1/ζ(2) = 6/π²`, with equality in the limit.
The constant is a tail-ratio of the `ζ(2)` series, normalized by
the comparison bound — a counting-type measure-theoretic identity
on the dyadic-shell decomposition of bands. (The numerical
coincidence with the natural density of coprime pairs in `ℕ × ℕ`
is real but is not the route by which `6/π²` appears in the repo
apparatus.)

**Measure-theoretic obstruction.** The closed-form values
`Δ_n ~ 4π⁴/(3n²)` and `B_1(n)/Δ_n → 6/π²` are determined by the
geometric-sum / Fourier-coefficient structure of the polygon
family and by the `ζ(2)`-tail comparison on its band
decomposition. They are not algorithmic targets: an algorithm
operating within the substrate cannot dial these constants below
their fixed values, because the values are fixed by the
substrate's combinatorial-integral structure rather than by
algorithmic choice.

---

## 4. Cyclotomic ladder vs affine flatness (§5.4)

**ID.** For positive integer `n > 2`, the maximal real subfield
of the cyclotomic field `ℚ(ζ_n)` is `K_n^+ = ℚ(ζ_n + ζ_n^{−1})`,
with `[K_n^+ : ℚ] = φ(n)/2`. This degree is unbounded as `n → ∞`.
The affine closure `Aff⁺(ℝ)` (Landfall §2: two-parameter affine
maps `x ↦ ax + b` with `a > 0`) is fixed at parameter-count two;
composition stays within `Aff⁺(ℝ)`.

**Connection to measure theory.** This row is at the boundary of
"measure theory" in the strict (σ-algebra, σ-additive measure)
sense. ℚ-vector-space dimension on finite extensions of ℚ is a
non-negative integer-valued invariant satisfying the
tower-multiplicative formula `[L : K] · [K : F] = [L : F]`; it is
a *counting invariant* on the category of finite extensions, with
measure-theoretic flavor (counting-measure-like on a basis), not a
measure proper. On parametric closure classes, parameter count is
similarly a counting invariant on the parameter space rather than
a Lebesgue/Haar/density measure. The doc preserves this row for
its structural parallel to the strictly measure-theoretic rows
above; it is typed as a counting-invariant obstruction, with
"measure-theoretic" used in the loose / structural sense.

**Counting-invariant obstruction.** No finite composition of
operations within `Aff⁺(ℝ)` produces a sizing-invariant exceeding
two parameters' worth of generative power. The cyclotomic ladder's
sizing invariant grows unbounded with `n`; the affine closure's is
fixed. The algebraic-side closure-mismatch theorem at
[memos/NATIVE-F-MINIMAL-DEFINITION.md](memos/NATIVE-F-MINIMAL-DEFINITION.md)
proves: no functor `F : Aff⁺(ℝ) → {K_n^+}_{n≥3}` preserves
closure-depth at competitive cost.

---

## 5. Admissibility envelope — Lebesgue dichotomy (§5.5)

**ID.** The admissibility envelope is the constraint that the
program's operations remain L-W-safe, staying within
Lindemann–Weierstrass-content (or its content-not-calendar audit
per [memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md)).
Within this constraint, the operative distinction available on
`ℝ` is the dichotomy between algebraic and transcendental real
numbers.

**Connection to measure theory.** Algebraic numbers form a
countable subset of `ℝ`, hence have Lebesgue measure zero on every
interval. Transcendentals form the complement, with full Lebesgue
measure. The L-W boundary (`Lindemann 1882`) divides these classes.

**Measure-theoretic obstruction.** The Lebesgue null/full
dichotomy is the operative measure-theoretic fact within L-W
safety: algebraic numbers are a null set; transcendentals are
full-measure; the boundary between them is the L-W boundary. The
dichotomy itself does not refine the bound at the bounded/unbounded
coefficient boundary — descent past `T(P)` cannot proceed by
appeal to the null-vs-full distinction alone. Whether *every* finer
distinction among transcendentals requires post-1882 transcendence
machinery (Baker on linear forms in logarithms; Gelfond–Schneider;
Thue–Siegel–Roth) is a separate per-instance audit question:
typical finer distinctions of program interest do engage such
machinery (and are therefore subject to content-not-calendar audit
per `memos/OLD-TIME-RELIGION.md`), but the doc does not assert
this universally.
