# TAU-THREE-WAYS

The second concrete test of the triad discipline (BIND, CREATI, PERMEATE) on a circle-side question whose answer is closed-form computable. NIVEN-THREE-WAYS (`BNHA/triad/NIVEN-THREE-WAYS.md`) handled the *zero* question — for which `n` is `τ(n) = 0` — and established a "loan structure" prediction: PERMEATE saturates, CREATI supplies the closed-form tail bound, BIND supplies the domain-internal argument that the tail bound is sharp. This memo runs the same test on the *magnitude* question — what is the sharp lower bound on `|τ(n)|` for `n` outside the Niven zero set — and finds the loan structure **inverted**: PERMEATE is self-contained on this problem, while CREATI's named primitives are exponentially weaker than the actual rate.

The point of the exercise is to test whether the triad's productive separation (catalog of primitives, domain-internal arguments, saturation-first attacks) is robust across question shapes, not whether the answer is hard. The answer is closed-form. What changes between Niven and τ-bounds is *which leg can finish on its own primitives*.

---

## Why τ-bounds is the right second test

NIVEN-THREE-WAYS established that `τ(n) = 0` exactly on the crystallographic set `{1, 2, 3, 4, 6}`, with two complete proofs (CREATI and BIND) and a productive PERMEATE attack that needs a CREATI lemma to close the tail. The complementary question is the magnitude question:

> For `n ∉ {1, 2, 3, 4, 6}`, give a sharp lower bound on `|τ(n)|`.

The answer is closed-form:

> **C\*-bound.** For every `n ∈ ℤ_{≥1} \ {1, 2, 3, 4, 6}`,
>
> ```text
> |τ(n)| ≥ C* / n²,        C* = 25(3 - √5)/2 = 25/φ² ≈ 9.5491,
> ```
>
> with equality at `n = 5` and strict inequality elsewhere. Equivalently, `|τ(n)| ≥ |τ(5)| · (5/n)²`, where `|τ(5)| = 1/φ²` and `φ = (1 + √5)/2` is the golden ratio.

The bound is a real-valued statement about an infinite family — exactly the question type NIVEN-THREE-WAYS flagged as a potential discriminator: "τ(n) = 0 is a yes/no question; τ(n) for n outside the zero set is a real-valued question with infinite complexity, and the triad might behave differently when asked to produce bounds."

This memo runs the test and reports back what changes.

---

## Setup

For `n ≥ 3`, the circle-side residue is

```text
τ(n) = 2cos(2π/n) − round(2cos(2π/n)).
```

Per the τ portrait (`figures/tau_portrait.png`, exposition at `corners/TAU-PORTRAIT.md`), `n ∈ {1, 2, 3, 4, 6}` are the Niven zeros; the values of `2cos(2π/n)` for `n ∉ {1,2,3,4,6}` partition cleanly:

- **Round-1 region** `{5, 7, 8}`: `2cos(2π/n) ∈ (1/2, 3/2)`, so `round = 1`. The "positive bulge" at `n = 7, 8` lives here; `n = 5` sits below `1` so `τ(5) < 0`.
- **Round-2 tail** `{n ≥ 9}`: `2cos(2π/n) ∈ (3/2, 2)`, so `round = 2` and `τ(n) = 2cos(2π/n) − 2 < 0`.

The asymptotic in the round-2 tail is `τ(n) = -4π²/n² + O(n⁻⁴)`, so `|τ(n)| → 4π²/n²` from below.

---

## The three routes, assigned

### CREATI route: minimal polynomial + algebraic-integer norm

**Primitives used.** `2cos(2π/n)` is an algebraic integer of degree `φ(n)/2` over `ℚ` for `n ≥ 3` (catalog item 9 of `BNHA/triad/Creati/CREATI-THE-CIRCLE.md`). Its conjugates under `Gal(ℚ(ζ_n)/ℚ)` are `2cos(2πk/n)` for `k` coprime to `n` modulo `±1`. Translation by an integer preserves the algebraic-integer property and the minimal-polynomial degree. The product of the absolute values of an algebraic integer's conjugates equals the absolute value of its `ℚ`-norm, which is a non-zero integer (i.e., `≥ 1`) for non-zero algebraic integers.

**Bound.** Fix `n ∉ {1,2,3,4,6}`. Set `θ_n = 2cos(2π/n)`, `k_n = round(θ_n) ∈ {-2, -1, 0, 1, 2}`, `τ(n) = θ_n − k_n`. Then `τ(n)` is a non-zero algebraic integer of degree `d := φ(n)/2` in `K_n^+ = ℚ(cos(2π/n))`. Its conjugates are `2cos(2πk/n) − k_n` for `k` running over `(ℤ/nℤ)*/{±1}`. Each conjugate is bounded by `|2cos(·) − k_n| ≤ 2 + |k_n| ≤ 4`. Therefore

```text
|N_{K_n^+/ℚ}(τ(n))| = |τ(n)| · ∏_{σ ≠ id} |σ(τ(n))| ≥ 1,
|τ(n)| ≥ 1 / ∏_{σ ≠ id} |σ(τ(n))| ≥ 4^{-(d − 1)} = 4 · 4^{-d}.
```

So `|τ(n)| ≥ 4 · 4^{-φ(n)/2}` — exponentially weak in `φ(n)`.

**Why this is CREATI-native.** Every primitive lives in the catalog: minimal-polynomial degree `φ(n)/2` (item 9), monic-`ℤ` Chebyshev closure carrying the conjugate set (item 7–8), the algebraic-integer norm bound is the standard "divisibility ⇒ ≥ 1" step. Closed-form throughout; no limiting process; no asymptotic content.

**Did it reach across?** No. The bound is honest CREATI; it just isn't quantitatively sharp.

**Quantitative bottom line.** `|τ(n)| ≥ 4 · 4^{-φ(n)/2}`. For `n = 5` this gives `4 · 4^{-2} = 1/4 = 0.25`, which is *below* the actual `|τ(5)| ≈ 0.382` — sharp on direction but loose on constant. For `n = 7` it gives `4 · 4^{-3} = 1/16 = 0.0625`, against actual `|τ(7)| ≈ 0.247`. For larger `n` the gap widens exponentially: at `n = 30` (`φ(30)/2 = 4`), CREATI gives `4 · 4^{-4} = 1/64 ≈ 0.0156`, against actual `|τ(30)| ≈ 0.0438`. CREATI's bound is exponentially weaker than the truth as `n` grows.

### BIND route: Galois-orbit qualitative argument

**Primitives used.** The Galois group `Gal(ℚ(ζ_n)/ℚ)` acts on `ζ_n + ζ_n^{-1} = 2cos(2π/n)` with orbit size `φ(n)/2` for `n ≥ 3`. Galois conjugates of a rational number are equal to it; therefore a rational `2cos(2π/n)` has Galois orbit of size 1, forcing `φ(n) = 2`, hence `n ∈ {1, 2, 3, 4, 6}`. Translation by an integer preserves the Galois action and the orbit size.

**Bound.** For `n ∉ {1, 2, 3, 4, 6}`, the Galois orbit of `τ(n) = 2cos(2π/n) − k_n` has size `φ(n)/2 ≥ 2`, so `τ(n)` is irrational, hence non-zero. The orbit consists of distinct algebraic numbers `{2cos(2πk/n) − k_n : k ∈ (ℤ/nℤ)*/{±1}}`; their pairwise distances are non-zero, but BIND has no native machinery for converting the *qualitative* non-collapse of the orbit into a *quantitative* lower bound on `|τ(n)|` itself.

**Why this is BIND-native.** Galois theory of cyclotomic fields, internal to `K_n^+`. No trigonometry, no Taylor expansion, no analytic content. The argument operates at the field-extension level throughout.

**Did it reach across?** Almost no, exactly parallel to NIVEN-THREE-WAYS' BIND analysis. Complex conjugation enters as the involution on `ℚ(ζ_n)` fixing the real subfield, treated field-theoretically.

**Quantitative bottom line.** No rate. BIND closes existence and qualitative structure (`τ(n) ≠ 0`, `τ(n)` irrational, orbit non-singleton) but does not produce a numerical lower bound. Quantitative content has to be borrowed.

### PERMEATE route: tabulation + Taylor-with-remainder + explicit threshold

**Primitives used.** Saturation of `|τ(n)|·n²` over the small-`n` range. Taylor expansion with explicit remainder for the round-2 tail, giving `|τ(n)|·n² = 4n²sin²(π/n)` monotonically increasing toward `4π²` for `n ≥ 9`. Combine the two to identify the global minimum.

**Proof.** Compute `|τ(n)|·n²` for `n` outside the Niven set:

| `n` | regime | `2cos(2π/n)` | `|τ(n)|` | `|τ(n)|·n²` |
|---:|:---:|---:|---:|---:|
| 5  | round-1 | `(√5 − 1)/2` | `(3 − √5)/2 = 1/φ²` | `25(3 − √5)/2 ≈ 9.549` |
| 7  | round-1 | `2cos(2π/7) ≈ 1.247` | `≈ 0.247` | `≈ 12.099` |
| 8  | round-1 | `√2 ≈ 1.414` | `√2 − 1 ≈ 0.414` | `64(√2 − 1) ≈ 26.510` |
| 9  | round-2 | `≈ 1.532` | `≈ 0.468` | `≈ 37.908` |
| 10 | round-2 | `(1+√5)/2 = φ` | `2 − φ = 1/φ² ≈ 0.382` | `100(2 − φ) ≈ 38.197` |
| 12 | round-2 | `√3 ≈ 1.732` | `2 − √3 ≈ 0.268` | `144(2 − √3) ≈ 38.585` |
| ⋮ | round-2 | ⋮ | ⋮ | ⋮ |
| `n → ∞` | round-2 | `→ 2⁻` | `≈ 4π²/n²` | `→ 4π² ≈ 39.478` |

The round-2 tail values satisfy `|τ(n)|·n² = 4n²sin²(π/n) = 4(π · sin(π/n)/(π/n))²`. Setting `u = π/n`, this equals `4(sin(u)/u · π)² · (n/n) = 4π²(sin(u)/u)²`. Since `sin(u)/u` is strictly decreasing on `(0, π]` and `→ 1` as `u → 0⁺`, the function `4π²(sin(u)/u)² = |τ(n)|·n²` is strictly increasing in `n` on `n ≥ 2`, hence on `n ≥ 9`. Its infimum on `n ≥ 9` is the value at `n = 9`:

```text
4 · 81 · sin²(π/9) = 324 · sin²(20°) ≈ 37.908.
```

The round-1 region is exhausted by the three-element table above. Minimum across both regimes:

```text
min{ |τ(n)|·n² : n ∉ {1,2,3,4,6} }
  = min{ 9.549,  12.099,  26.510,  37.908,  38.197, … , 4π² }
  = 25(3 − √5)/2,   attained at n = 5.
```

Therefore `|τ(n)| ≥ 25(3 − √5)/(2n²)` for every `n ∉ {1, 2, 3, 4, 6}`, with equality at `n = 5`.

The Taylor identity `|τ(5)| = (3 − √5)/2 = 1/φ²` is closed-form trigonometry: `2cos(2π/5) = (√5 − 1)/2 = 1/φ` is the half-side of a regular pentagon, classical pre-1882 (`memos/EULER-1768-INTEGRAL-BRIEF.md` lineage). The asymptotic is Taylor-with-remainder on `cos`, also pre-1882. The monotonicity of `(sin u)/u` on `(0, π]` is elementary calculus.

**Why this is PERMEATE-native.** Tabulation across a finite range, asymptotic shape with explicit remainder, monotonicity check, threshold argument. Every primitive is in the catalog of `BNHA/triad/Lemillion/PERMEATE-THE-CIRCLE.md`. No reach-across to algebraic-integer arguments, Galois orbits, or minimal polynomials.

**Did it reach across?** No. The closed-form value `2cos(2π/5) = (√5−1)/2` is trigonometry, present in any school text; PERMEATE consumes it as a numerical fact, not as an algebraic-integer fact. The argument never invokes `2cos(2π/5)`'s minimal polynomial or algebraic conjugates.

**Quantitative bottom line.** Sharp. `|τ(n)| ≥ 25(3 − √5)/(2n²)` with equality at `n = 5`. The constant `25(3 − √5)/2 = 25/φ²` is closed-form.

---

## What the test shows

PERMEATE finishes `τ`-bounds on its own primitives, with a sharp closed-form constant. CREATI's algebraic-integer norm bound is exponentially weak. BIND has no native quantitative content for this question.

This **inverts the loan structure** NIVEN-THREE-WAYS predicted. For Niven, PERMEATE could saturate the table and identify the conjectural zero set, but it could not rule out rational-noninteger values in the tail without borrowing CREATI's "rational ⇒ integer" lemma. For τ-bounds, PERMEATE can saturate the table, identify the global minimum at `n = 5`, and use Taylor-with-remainder to close the tail — entirely on its own primitives, with a sharp constant.

The structural reason. NIVEN asks a *discrete* question: is `2cos(2π/n)` exactly an integer? PERMEATE's metric-style tabulation cannot distinguish "exactly integer" from "very close to integer" without an arithmetic lemma. τ-bounds asks a *metric* question: how far from the nearest integer is `2cos(2π/n)`? PERMEATE's metric-style tabulation answers this directly, and the asymptotic gives the rate. The discrete-vs-metric distinction is the discriminator, not the substrate.

This is the second triad finding. NIVEN-THREE-WAYS established that BIND, CREATI, and PERMEATE partition the proof space natively for the τ = 0 question. TAU-THREE-WAYS establishes that *which leg finishes the job* depends on the question's shape: discrete questions route through CREATI (or BIND), metric questions route through PERMEATE. Both are valid uses of the disciplines; the loan structure is question-shape-sensitive.

---

## Sharpness commentary

The bound `|τ(n)| ≥ 25(3 − √5)/(2n²)` is sharp at `n = 5` and not approached again. The next-smallest value of `|τ(n)|·n²` is `12.099` at `n = 7` (a `26.7%` margin above `C*`), and `|τ(n)|·n²` then climbs through `26.510` at `n = 8` and `37.908` at `n = 9`, asymptoting to `4π² ≈ 39.478` from below.

The asymptotic constant `4π²` is the natural Taylor reference for the round-2 tail; the actual minimum sits at `25/φ² ≈ 9.549 ≈ 0.242 · 4π²`, almost exactly four times smaller. The factor-of-four shortfall is the cost of `n = 5`'s round-1 placement: at `n = 5`, `2cos(2π/5)` sits closer to the *lower* round boundary `1/2` than to `1`, so `τ(5)` is `(√5 − 1)/2 − 1 = (√5 − 3)/2`, larger in magnitude than the corresponding tail value would be.

The golden-ratio appearance `|τ(5)| = 1/φ²` is incidental, not load-bearing — it follows from `2cos(2π/5) = 1/φ`, which is the standard regular-pentagon identity (the diagonal-to-side ratio). For the program, the noteworthy structural fact is that the sharp constant is determined by the *smallest n outside the zero set*, not by the asymptotic regime.

---

## Consequences for the program

Three small consequences for the doc set.

**`corners/TAU-PORTRAIT.md`.** The log-log lower panel of `figures/tau_portrait.png` shows `|τ(n)|` descending toward the dashed `4π²/n²` line, with the small-`n` markers (`n = 5, 7, 8`) sitting noticeably below. The `C*-bound = 25(3 − √5)/(2n²)` is the sharp pre-asymptotic floor visible in that panel, with `n = 5` realizing equality. Worth adding to the figure's exposition as the explicit bound that the visual-below-asymptote behavior actually realizes.

**`paper/POLYGONAL-LEDGER.md` §"Open".** That memo lists "Whether the τ-residue admits a Fourier reading despite living on `ℤ` rather than on a continuous seam" as open. The C*-bound is a *Taylor* reading, not a Fourier reading — it answers a different question. This memo doesn't close the Fourier line; it does establish that the Taylor line gives a sharp closed-form answer for the magnitude question, useful as a benchmark when the Fourier reading lands.

**`BNHA/triad/`** discipline files (`Creati/`, `Eraserhead/`, `Lemillion/`). The discipline catalogs gain a worked example each:
- *CREATI*: the algebraic-integer norm bound is a CREATI-native argument that produces an honest but quantitatively weak answer. Worth flagging as the "exponentially-weak warning" — CREATI primitives can finish a question and still be far from sharp.
- *BIND*: the Galois-orbit argument closes the *qualitative* part of τ-bounds (`τ(n) ≠ 0` for non-Niven `n`) and is reminded of its limitation: domain-internal arguments don't natively quantify metric questions.
- *PERMEATE*: the C*-bound is a worked example of PERMEATE finishing on its own primitives, with the loan structure inverted relative to Niven. Worth adding to the PERMEATE catalog as the "metric-question template."

---

## What this previews about F

The C*-bound has a sharp closed form because the circle side carries a native metric on `ℤ` — the residue `τ(n)` measures distance to the nearest integer at the rotation angle `2π/n`, and this distance is a real number that PERMEATE can saturate finitely and asymptotically. The log-side analog is `ε(m) = log₂(1 + m) − m`, the floating-point residue at machine numbers (`Landfall §2`); it admits a similar Taylor-with-remainder bound in the binade-tail regime, and a similar saturation across machine-precision values.

So PERMEATE's productive separation between metric and discrete questions is not unique to the circle side. The asymmetry between the two sides — the structural closure-mismatch of `memos/NATIVE-F-MINIMAL-DEFINITION.md` — sits elsewhere: on the circle side, the algebraic-integer ladder `[K_n^+ : ℚ] = φ(n)/2` provides BIND/CREATI with a discrete invariant (orbit size, minimal-polynomial degree) that grows unbounded with `n`; on the log side, the affine closure `Aff⁺(ℝ)` is flat, and the analogous discrete invariant is missing.

NIVEN-THREE-WAYS' "loan structure" prediction was that PERMEATE saturates and CREATI tail-closes. TAU-THREE-WAYS shows the prediction *generalizes correctly* to discrete questions and *inverts* on metric questions, with PERMEATE self-contained. For the log side, the same partition would hold: discrete-rationality questions on `ε(m)` (e.g., is `ε(m) = 0` for any `m`) need a CREATI lemma, while metric-magnitude questions on `|ε(m)|` are closed by PERMEATE saturation plus Taylor-with-remainder.

The closure-mismatch the program targets is therefore not visible at the *τ-bounds* / *|ε(m)|-bounds* level — both sides admit clean PERMEATE answers there. It is visible at the *discrete-rationality* level, where the circle side can finish via CREATI's `[K_n^+ : ℚ] = φ(n)/2` ladder and the log side cannot, because `Aff⁺(ℝ)` has no analogous discrete invariant.

This is preview, not result. What this memo establishes is the second discipline-level data point on the triad's behavior across question shapes; the closure-mismatch reading sits over the data point, not inside it.

---

## What this test does not establish

- Whether the C*-bound generalizes to higher-resolution `τ`-statements: e.g., effective lower bounds on `|τ(n) − r/q|` for rational `r/q` (a Diophantine question on `τ` itself), or `τ`-bounds in the joint cyclotomic × `ℚ(π)` field. Both are open and may need CREATI lemmas (the joint-field question is exactly the Liouville-scale test of `memos/LIOUVILLE-SCALE-TEST.md`, closed negative).
- Whether the loan-structure inversion is generic across metric questions or specific to the round-distance shape of `τ`. The companion question on the strip residue `R_n = 16π⁶/(45n⁴) + ...` (`memos/STRIP-H1-HURWITZ-CLOSURE.md`) is metric-shaped and admits a clean PERMEATE answer; that's one further data point, not a generalization theorem.
- Whether PERMEATE's self-containment scales to questions where the asymptotic is itself open. For `τ`, the asymptotic `|τ(n)| → 4π²/n²` is closed-form; for questions where the asymptotic requires non-trivial transcendence content (e.g., Diophantine `τ`-on-`π` questions), PERMEATE will have to borrow.

---

## Trust boundary

This memo is a discipline test, not a new theorem. The C*-bound is closed-form, derivable in any sitting from the primitives in the three discipline catalogs; what's new is the verdict on which leg finishes which question, not the bound itself.

The argument uses only pre-1882 primitives in content (CF / Taylor / elementary trigonometry / monotonicity); per `memos/OLD-TIME-RELIGION.md` content-not-calendar, the C*-bound is L-W-safe in content. The closed form `|τ(5)| = 1/φ²` is regular-pentagon trigonometry (Euclid; pre-1882 in calendar by millennia).

The trust-boundary discipline of `BNHA/ONE-FOR-ALL.md` applies: the discipline catalogs (`Creati/`, `Eraserhead/`, `Lemillion/`) supply primitives, this memo consumes them, and any cross-citation of the C*-bound downstream should respect the catalog provenance.
