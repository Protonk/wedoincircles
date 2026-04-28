# SUBSTRATE-OBSTRUCTIONS

Detailed measure-theoretic typing of the five substrate-side angles in
[paper/IMPOSSIBILITY-OUTLINE.md](paper/IMPOSSIBILITY-OUTLINE.md) §5.
This is the source-side catalogue behind the paper-level pointer
[paper/MEASURE-THEORETIC-OBSTRUCTIONS.md](paper/MEASURE-THEORETIC-OBSTRUCTIONS.md).
Each entry records: the object, the measure-theoretic structure it
uses, and the non-availability it supplies.

This file is strictly source-side. Each row is supported by a citable
fact in standard measure theory, Diophantine analysis, or the program's
audited literature. Implications and methodological readings live in
[measure/THE-FIRST-BRIDGE.md](measure/THE-FIRST-BRIDGE.md),
[paper/FIRST-PROOF.md](paper/FIRST-PROOF.md), and
[paper/IMPOSSIBILITY-OUTLINE.md](paper/IMPOSSIBILITY-OUTLINE.md).

---

## 1. Rotation-Orbit Diophantine Kinematics

**ID.** The Diophantine spectrum places real `α` according to its
irrationality exponent. Liouville numbers admit unbounded exponent;
algebraic irrationals are constrained to exponent 2 (Roth 1955);
typical irrationals have finite irrationality measure. The
Avila-Jitomirskaya parameter `β(α) = limsup (ln q_{n+1}) / q_n`
satisfies the one-way implication: finite irrationality measure
implies `β(α) = 0`, and `β(α) > 0` implies `α` is Liouville. The
converse fails: some Liouville `α` can still have `β(α) = 0`.
Existing finite irrationality-measure bounds for `π` therefore imply
`β(π) = 0`; they do not imply `π` lies on the Roth `μ = 2` boundary,
and the `β` parameter alone does not characterize non-Liouville. The
orbit `{kα mod 1 : k in Z}` is the kinematic substrate the algorithm
operates on.

**Connection to measure theory.** Haar measure on `T = R/Z`
(equivalently, normalized Lebesgue measure on `[0, 1)`) is the unique
translation-invariant Borel probability measure. Weyl's
equidistribution theorem (Weyl 1916,
`sources/uber-die-gleichverteilung-von-zahlen-mod-eins-2liqw01yl8.pdf`)
says that for any irrational `α`, the sequence `{kα mod 1}_{k>=1}`
equidistributes against Haar: for every continuous `f : T -> C`,

```text
(1/N) sum_{k=1}^N f(kα mod 1) -> integral_T f dμ_Haar.
```

By standard approximation, the same convergence extends to
Riemann-integrable `f` and to indicator functions of intervals whose
boundary has Lebesgue measure zero. Convergence rate is controlled by
the irrationality exponent of `α` through discrepancy bounds; see
`memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md`.

**Obstruction.** For continuous and Riemann-integrable test functions,
the asymptotic time-average along the orbit is fixed by the Haar
integral. The orbit cannot deviate from the Haar mean against this
class of statistics, so distinguishing information at this regularity
is unavailable beyond Haar.

## 2. Non-Nesting Isoperimetric Registers

**ID.** Isoperimetric phenomena admit three distinct quantitative
readings on plane curves and their analogues: rate, constant, and
almost-every. Rate records asymptotic decay of the deficit
`L^2 - 4πA` along a sequence approaching a circle. Constant records a
pointwise sharp geometric inequality, with Bonnesen's strengthening
`L^2 - 4πA >= π^2(R - r)^2` per Osserman 1979 / Bonnesen 1921.
Almost-every records full-measure claims about families parameterized
by a stated measure, as in the Khintchine / Beck 1994 tradition.
Fuglede 1989's Sobolev stability inequalities sit elsewhere in the
repo taxonomy and are not invoked here as a constant-sharp result.

**Connection to measure theory.** Each register is a distinct
measure-theoretic operation on a curve family. Rate corresponds to
asymptotic-density readings. Constant corresponds to pointwise
Lebesgue inequalities: sharp ratios of Lebesgue-measured area to
length-squared. Almost-every corresponds to full-measure claims under a
distribution on parameter space.

**Obstruction.** The three registers do not nest. Knowing rate does
not imply knowing the sharp constant. Knowing the sharp constant does
not control the typical curve under a distribution. Knowing an
almost-every statement does not identify an asymptotic-saturating
sequence. No measure-theoretic equivalence functor between the three
registers is available; each requires its own argument.

## 3. Closed-Form Polygon Arithmetic

**ID.** The regular-polygon family carries closed-form values: Hurwitz
coefficients on the sparse lattice `m = 1 mod n`; the Archimedean gap
`Δ_n ~ 4π^4/(3n^2)`; and the first-band concentration constant
`B_1(n) / Δ_n -> 6/π^2 = 1/ζ(2)`. The detailed ledger is
[paper/POLYGONAL-LEDGER.md](paper/POLYGONAL-LEDGER.md), with source
calculation at `corners/HURWITZ-FIRST-BAND-CONCENTRATION.md`.

**Connection to measure theory.** The first-band concentration arises
from a `ζ(2)`-tail comparison. Paired-band terms `B_j(n)` satisfy
`B_j(n) <= B_1(n) / j^2` for every `j >= 1`, so

```text
Δ_n = sum_{j >= 1} B_j(n) <= B_1(n) sum_{j >= 1} 1/j^2
    = B_1(n) ζ(2).
```

The first band's share of the total gap is therefore at least
`1/ζ(2) = 6/π^2`, with equality in the limit. The constant is a
tail-ratio of the `ζ(2)` series, normalized by the comparison bound.
The numerical coincidence with the natural density of coprime pairs is
real but is not the route by which `6/π^2` appears in the repo
apparatus.

**Obstruction.** The values `Δ_n ~ 4π^4/(3n^2)` and
`B_1(n)/Δ_n -> 6/π^2` are fixed by the geometric-sum /
Fourier-coefficient structure of the polygon family and the `ζ(2)`-tail
comparison. They are not algorithmic knobs. An algorithm operating
within the substrate cannot dial these constants below their fixed
values.

## 4. Cyclotomic Ladder Vs Affine Flatness

**ID.** For `n > 2`, the maximal real subfield of `Q(ζ_n)` is
`K_n^+ = Q(ζ_n + ζ_n^{-1})`, with `[K_n^+ : Q] = φ(n)/2`. This degree
is unbounded as `n -> infinity`. The affine closure `Aff^+(R)` is a
two-parameter class; composition stays within it.

**Connection to measure theory.** This row is at the boundary of
"measure theory" in the strict sigma-additive sense. `Q`-vector-space
dimension on finite extensions is a non-negative integer-valued
counting invariant satisfying the tower formula. On parametric closure
classes, parameter count is likewise a counting invariant rather than
a Lebesgue/Haar/density measure.

**Counting-invariant obstruction.** No finite composition inside
`Aff^+(R)` produces a sizing invariant exceeding two parameters' worth
of generative power. The cyclotomic ladder grows unbounded with `n`;
the affine closure stays fixed. The algebraic-side closure-mismatch
theorem at [memos/NATIVE-F-MINIMAL-DEFINITION.md](memos/NATIVE-F-MINIMAL-DEFINITION.md)
proves that no functor `F : Aff^+(R) -> {K_n^+}_{n>=3}` preserves
closure-depth at competitive cost.

## 5. Admissibility Envelope: Lebesgue Dichotomy

**ID.** The admissibility envelope is the constraint that the program's
operations remain L-W-safe, staying within Lindemann-Weierstrass
content or its content-not-calendar audit per
[memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md). Within this
constraint, the operative distinction available on `R` is the
dichotomy between algebraic and transcendental real numbers.

**Connection to measure theory.** Algebraic numbers form a countable
subset of `R`, hence have Lebesgue measure zero on every interval.
Transcendentals form the complement, with full Lebesgue measure. The
L-W boundary divides these classes.

**Obstruction.** The Lebesgue null/full dichotomy is the operative
measure-theoretic fact within L-W safety. It does not refine the bound
at the bounded/unbounded coefficient boundary, so descent past `T(P)`
cannot proceed by appeal to the null-vs-full distinction alone. Finer
distinctions among transcendentals are per-instance audit questions;
typical distinctions of program interest engage post-1882 machinery
and must pass `memos/OLD-TIME-RELIGION.md`.
