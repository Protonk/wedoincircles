# SUBSTRATE-OBSTRUCTIONS

Detailed measure-theoretic typing of the five substrate-side angles in
[paper/OUTLINE.md](paper/OUTLINE.md) §5.
This is the source-side catalogue behind the paper-level pointer
[paper/MEASURE-THEORETIC-OBSTRUCTIONS.md](paper/MEASURE-THEORETIC-OBSTRUCTIONS.md).
Each entry records: the object, the measure-theoretic structure it
uses, and the non-availability it supplies.

This file is strictly source-side. Each row is supported by a citable
fact in standard measure theory, Diophantine analysis, or the program's
audited literature. Implications and methodological readings live in
[measure/THE-FIRST-BRIDGE.md](measure/THE-FIRST-BRIDGE.md),
[paper/FIRST-PROOF.md](paper/FIRST-PROOF.md), and
[paper/OUTLINE.md](paper/OUTLINE.md). The
σ-algebra coarsening reading of these five faces — which faces
transcribe to direct fiber-non-constant L-observables in the
[measure/FOR-BREAKFAST.md](measure/FOR-BREAKFAST.md) §The kernel sense,
and which require separate handling — is recorded at
§Kernel partition below.

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
and the `β` parameter alone does not characterize non-Liouville.
L-W-safety provenance for the chain `finite μ(π) ⟹ β(π) = 0` audited
at [rotations/BETA-PI-LW-AUDIT.md](rotations/BETA-PI-LW-AUDIT.md):
Hermite-Padé auxiliary-function arithmetic in Mahler 1953 / Hata 1993
/ Salikhov 2008 plus classical CF algebra; no Baker / Gelfond-Schneider
/ Thue-Siegel-Roth content. The orbit `{kα mod 1 : k in Z}` is the
kinematic substrate the algorithm operates on.

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

---

## Kernel partition

The five §-faces above transcribe unevenly into
[measure/FOR-BREAKFAST.md](measure/FOR-BREAKFAST.md) §The kernel.
The kernel works on the integer-indexed lattice
`L = {(k, n) : 1 ≤ k < n, n ≥ 3}` with the reduction map `R : L → F`
to the Farey set; its `R^*`-pullback is the fiber-constant L-functions,
and a face is a *direct* K2 instance iff it transcribes to a
fiber-non-constant L-observable. Three of the five faces transcribe
directly. Two do not.

| Substrate angle | K2 status | Notes |
|---|---|---|
| §1 — Haar / `β(α)` on rotation orbit | **not a direct L-observable** | Haar measure lives on `T = ℝ/ℤ`; `β(α)` is a function of irrational `α`. Translating either to `L` requires a separate transport that the kernel does not yet construct. |
| §2 rate — `Δ_n` decay along the regular `n`-gon family | direct L-observable | `f₃(k, n) = Δ_n = L_n²(1 − (π/n)\cot(π/n))` is K2 instance #3. |
| §2 constant — Bonnesen-strengthening sharp constant | direct L-observable | The Bonnesen ratio is a scalar function of `n` on the regular `n`-gon family; e.g., `L_n = 2n\sin(π/n)` plays the role through `f₂` in K2. |
| §2 almost-every — Khintchine / Beck full-measure register | not a scalar L-observable | The almost-every register is a measure operation on a parameterized family of curves, not a scalar function on `L`. To become K2-eligible it requires a stated parameter family and a chosen scalar reduction. |
| §3 — Hurwitz Fourier on lattice `m ≡ 1 mod n`; `B_1(n)/Δ_n → 6/π²` | direct L-observable | `f₂(k, n) = L_n` (equivalently the Hurwitz first Fourier coefficient `c_1^{(n)} = L_n²/(4π²)`) is K2 instance #2. The closed-form `Δ_n`, `B_j(n)` ledger gives the analytic content underwriting this and §2's rate face. |
| §4 — Cyclotomic ladder `[K_n^+ : ℚ] = φ(n)/2`, `n > 2` | direct L-observable | `f₁(k, n) = φ(n)/2` is K2 instance #1, with explicit witness `f₁(1, 5) = 2 ≠ 4 = f₁(3, 15)`. The kernel's `n ≥ 3` restriction lines up with §4's own `n > 2` hypothesis. |
| §5 — L-W null/full Lebesgue dichotomy | **fiber-constant on `L` under literal reading** | Every `cos(2π/n)` for integer `n` is algebraic; the algebraic-vs-transcendental dichotomy assigns the same value to every point of `L`. The finer cyclotomic-depth content is §4's `f₁`, not §5's dichotomy. |

The three direct entries (§2 rate, §3, §4) ground FOR-BREAKFAST K2's
proof of σ-algebra coarsening: each is fiber-non-constant on `L` by
the explicit witnesses recorded in K2's proof. The two non-direct
entries (§1, §5) flag scope:

- **§1 transport.** Promoting the §1 obstruction to a direct K2
  instance requires a measurable map from rotation-orbit Haar /
  β(α) data to an L-observable. The kernel does not supply this;
  it is open work.
- **§5 fiber-constancy.** Promoting §5 to a direct K2 instance
  requires a finer reading than the algebraic-vs-transcendental
  dichotomy. The Niven set `{n : cos(2π/n) ∈ ℚ} = {1, 2, 3, 4, 6}`
  and the cyclotomic-depth profile `[K_n : ℚ]` are finer; both are
  already handled by §4's `f₁`. So §5 contributes no additional
  L-observable beyond what §4 already supplies.

§2's almost-every register sits between: it is not fiber-constant in
a vacuous sense (it does not produce an L-value at all without a
stated parameter family), so it is not a K2 *instance* until the
family is fixed. The rate and constant registers within §2 are
direct K2 instances; the almost-every register is a separate
measure operation.

**Caveat.** The Kernel partition is a reading of the §1-5 typing
through one specific lens (FOR-BREAKFAST's atomic σ-algebra
coarsening). The `σ`-algebra coarsening reading is necessary
infrastructure for the load-bearing measure-theoretic bridge at
[measure/THE-FIRST-BRIDGE.md](measure/THE-FIRST-BRIDGE.md), not the
bridge itself. The §-face content and obstructions above stand on
their own at the source-side typing level.
