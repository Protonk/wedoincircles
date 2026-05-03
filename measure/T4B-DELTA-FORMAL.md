# T4B-DELTA-FORMAL

Phase 1a of the T4b decomposition (`paper/T4B-DECOMPOSITION.md`): formalize `δ` as a measurable function. Pin down the candidate cocycle realization at [fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md) to a precisely typed function on a precisely typed domain, with measurability proven.

## Recap of the candidate

Per [fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md) and [fft/COCYCLE-COMPOSITION-LAW.md](fft/COCYCLE-COMPOSITION-LAW.md):

- *Quotient-clock displacement.* For `m ∈ [0, 1)`, `ε(m) := log₂(1 + m) − m` is the displacement between additive and log-binade coordinates.
- *Defect cocycle.* For each character index `k ∈ ℤ`, `Δ_k(m) := χ_k(ε(m))` where `χ_k` is the formal character of `A = ℝ/ℤ`.
- *Composition law.* For an FFT-style scheme `S = O_n ∘ ⋯ ∘ O_1`, the cocycle path-product is `Π_k(S, m) = ∏_{(s, b)} Δ_k^{(b)}(state_{s, b})` over all (stage, butterfly) pairs in `S`'s computation, with cross-terms `χ_k(c_{O_{i+1}, O_i}(m))` collapsing under the §1.2 / §4.2.1 regularity guard.
- *Operational compressibility cost-norm* (debt #14, committed): "the failure-to-agree of cocycle-product factors across butterfly refinements and primitive modes, measured pointwise."

Phase 1a converts these candidate descriptions into a measurable function.

## FP arithmetic model: Matula 1970 significance spaces

Phase 1a inherits the FP arithmetic formalism of [memos/FP-MATULA-1970.md](memos/FP-MATULA-1970.md) (David W. Matula, "A Formalization of Floating-Point Numeric Base Conversion," IEEE TC C-19 №8, August 1970).

**Significance space.** For base `β ≥ 2` and precision `n ≥ 1`,
```
S^β_n  :=  { b : b = k · β^j  for integers k, j  with |k| < β^n }
```
is the (infinite-extent, no underflow / no overflow) abstract FP space at `(β, n)` (Matula §II, p. 682). Within each binade `[β^j, β^{j+1})`, `S^β_n` carries exactly `(β − 1) · β^{n−1}` distinct values (Matula §II, p. 683).

**Conversion primitives.** Truncation `T^β_n : ℝ → S^β_n` and rounding `R^β_n : ℝ → S^β_n` (Matula §III, eqs. 9–10; midpoints round up per Matula's convention; Urabe's parity-dependent alternative flagged but not adopted). Both are step functions with breakpoints at `S^β_n` elements within each binade.

**Base commitment.** Phase 1a fixes `β = 2`. Justification: (i) the candidate cocycle at `fft/PHASE-DEFECT.md` is `ε(m) = log₂(1 + m) − m`; (ii) `fft/COCYCLE-COMPOSITION-LAW.md`'s worked example is radix-2 Cooley–Tukey; (iii) §3 canon's bit-counting and binary-FP framing throughout. The Matula formalism is base-parametrized; Phase 1a's commitment is operational. Per Matula's commensurability dichotomy (Lemma 1 / Corollary 2 — `β, δ` commensurable iff `β^i = δ^j` for some nonzero `i, j` iff `log_δ β ∈ ℚ`), changes of base inside the binary commensurability family `{2, 4, 8, 16, …}` preserve structural alignment; cross-family changes (e.g., `β = 10`) are out of Phase 1a's scope and become a Phase 1c discriminator question if needed.

**Native operations at `(β, n) = (2, p)`.** Each operation in §4.2.2's list (recursive FFT decomposition, CRT / tensor factorization, linear-composition closure, cyclotomic factor accounting, coefficient-regime bookkeeping) decomposes into elementary FP primitives operating on `S^2_p` via finite arithmetic with `T^2_p` / `R^2_p` rounding. Phase 1a does not enumerate this decomposition; it inherits §4.2.1's regularity guard ("operation cost / stored precision / coefficient size paid at same granularity") as the commitment that the decomposition exists at the FP-primitive level.

## Setting

**Schemes.** `S` = the countable set of FFT-style schemes. Each `S ∈ S` is a finite composition of native operations from §4.2.2 (recursive FFT decomposition; CRT / tensor factorization; linear-composition closure; cyclotomic factor accounting; coefficient-regime bookkeeping). The native list is finite; finite compositions are enumerable. σ-algebra on `S`: discrete (`𝒫(S)`).

**Input space.** `M = [0, 1)` with the standard Borel σ-algebra `ℬ([0, 1))`. Inputs `m ∈ M` are realized in `S^2_p` at precision `p` via the standard mantissa-coordinate identification `m ↦ T^2_p(1 + m) − 1` (truncation path) or `m ↦ R^2_p(1 + m) − 1` (rounding path). Machine-dyadic inputs `m = j / 2^p` are exactly the precision-`p` representable subset.

**Precision.** `P = ℕ_{>0}` with discrete σ-algebra `𝒫(ℕ_{>0})`. Identified with Matula's precision parameter `n`; we use `p` throughout to match paper convention.

**Joint domain.** `D := S × M × P` with the product σ-algebra `ℬ_D := 𝒫(S) ⊗ ℬ([0, 1)) ⊗ 𝒫(ℕ_{>0})`. `D` is a standard Borel space (countable factor × Borel factor × countable factor).

**Codomain.** `(ℝ_{≥0}, ℬ(ℝ_{≥0}))`.

## Definition

For `(S, m, p) ∈ D`:

**(a) Per-refinement cocycle value.** Let `R(S, p)` be the finite set of admissible butterfly refinements of `S` at precision `p` — distinct butterfly tree decompositions, mixed-radix factorizations, and stage groupings consistent with `S`'s native-operation skeleton. For each `r ∈ R(S, p)` and character index `k ∈ ℤ`:
```
Π_k^{(r)}(S, m, p)  :=  ∏_{(s, b) ∈ r}  Δ_k^{(b)}(state_{s, b}^{(r, m, p)})
```
where the product runs over all (stage `s`, butterfly `b`) pairs in refinement `r`, and `state_{s, b}^{(r, m, p)} ∈ S^2_p` is the working value at `(s, b)` when `S` applies to `m` at precision `p` under refinement `r` — values in Matula's significance space `S^2_p`. The per-butterfly factor `Δ_k^{(b)}(·)` evaluates the formal character `χ_k` at the state's mantissa-coordinate residual (per [fft/COCYCLE-COMPOSITION-LAW.md](fft/COCYCLE-COMPOSITION-LAW.md) §"Worked example").

**(b) Character index set at precision p.** `K(p) := { k ∈ ℤ : |k| < 2^p }` (matching Matula's strict bound `|k| < β^n` on `S^β_n`). Finite at each `p`; characters with `|k| > 2^p` are aliased at precision `p` and don't supply distinct mode behaviors.

**(c) δ as pointwise failure-to-agree.**
```
δ(S, m, p)  :=  max_{k ∈ K(p)}  max_{r, r' ∈ R(S, p)}  d_𝕋(Π_k^{(r)}(S, m, p),  Π_k^{(r')}(S, m, p))
```
where `d_𝕋(z₁, z₂) := |z₁ − z₂|_{ℝ/ℤ}` is the standard quotient distance on `𝕋 = ℝ/ℤ` (or, under the analytic specialization `χ_k(t) = e^{2πikt}`, the chordal distance on the unit circle scaled to `[0, 1]`).

The double max runs over finite sets `K(p) × R(S, p) × R(S, p)` at each `(S, p)`. When `|R(S, p)| = 1` (no refinement freedom — e.g., a primitive operation), `δ(S, m, p) = 0` trivially. The interesting regime is `|R(S, p)| > 1`: distinct refinements produce distinct cocycle products iff `S` is operationally non-compressible at `(m, p)`.

## Measurability

**Claim.** `δ : (D, ℬ_D) → (ℝ_{≥0}, ℬ(ℝ_{≥0}))` is measurable.

**Proof.** Fix `S ∈ S` and `p ∈ P`. Show `δ(S, ·, p) : M → ℝ_{≥0}` is Borel measurable; joint measurability on `D` then follows from the product-σ-algebra criterion (countable factors with discrete σ-algebra times Borel factor with section-measurable functions).

The proof proceeds via Matula's significance-space structure: native operations are piecewise-constant in `m` with **finite** breakpoint sets (not just continuous-up-to-measure-zero), and finite compositions preserve this property.

**Step 1 — Conversion-primitive piecewise-constancy.** The conversion primitives `T^2_p` and `R^2_p` (Matula §III, eqs. 9–10) are step functions on `[0, 1)` with breakpoints at the `S^2_p` lattice within each binade. By Matula's density count `(β − 1) · β^{n−1}` at `(β, n) = (2, p)`, each binade carries `2^{p−1}` representable values; restricted to the unit-interval-image binade `[1, 2)` (under `m ↦ 1 + m`), `T^2_p` and `R^2_p` are piecewise-constant with `2^{p−1}` finite breakpoints. Piecewise-constant functions with finite breakpoint sets are Borel measurable (each constant piece is the indicator of a half-open interval).

**Step 2 — Per-native-op piecewise-constancy.** Each native operation `O ∈` §4.2.2 list, applied at fixed precision `p`, decomposes into a finite composition of elementary FP arithmetic (addition, multiplication, twiddle-constant multiplication, division by 2, etc.) interleaved with conversion primitives `T^2_p` / `R^2_p`. By §4.2.1's regularity guard, each primitive is charged at granularity `p`; advice strings, oracle constants, and growing hidden state are out of class. Compositions of step functions with finite breakpoint sets remain step functions with finite breakpoint sets — for `g ∘ f`, the breakpoint set is `(breakpoints of f) ∪ f^{-1}(breakpoints of g)`, both finite when `f, g` are piecewise-constant with finite breakpoints (the pre-image of a finite set under a piecewise-constant function is finite). Therefore `O : M → S^2_p` is piecewise-constant with finite breakpoint set `N_O ⊂ M`, with cardinality bounded by the operation count of `O` times Matula's per-binade density `2^{p−1}`.

**Step 3 — State values are piecewise-constant.** By induction on operation depth, `state_{s, b}^{(r, m, p)} : M → S^2_p` is piecewise-constant in `m` for fixed `(S, r, p)` with finite breakpoint set. Base case: the input realization `m ↦ T^2_p(1 + m) − 1` (Step 1). Inductive step: composition with one further native operation (Step 2) preserves piecewise-constancy with finite breakpoints.

**Step 4 — Cocycle factors are piecewise-constant.** `Δ_k^{(b)}(·) : S^2_p → 𝕋` is a function from the discrete value set `S^2_p` to the formal character torus. Composed with the piecewise-constant `state_{s, b}(m)`, the composition `Δ_k^{(b)}(state_{s, b}(m))` inherits piecewise-constancy in `m` with the breakpoint set of `state_{s, b}`.

**Step 5 — Cocycle products are piecewise-constant.** `Π_k^{(r)}(S, m, p) = ∏_{(s, b) ∈ r} Δ_k^{(b)}(state_{s, b}^{(r, m, p)})` is a finite product of piecewise-constant functions, hence piecewise-constant in `m` with breakpoint set the union of constituent breakpoints (still finite).

**Step 6 — δ is piecewise-constant.** `δ(S, m, p) = max_{k ∈ K(p)} max_{r, r' ∈ R(S, p)} d_𝕋(Π_k^{(r)}, Π_k^{(r')})` is a finite max over `K(p) × R(S, p) × R(S, p)` of piecewise-constant functions with finite breakpoints. Finite max of piecewise-constant functions is piecewise-constant. The combined breakpoint set is
```
N_{S, p}  :=  ⋃_{(k, r, r') ∈ K(p) × R(S, p)²}  N(Π_k^{(r)}) ∪ N(Π_k^{(r')})
```
finite by Steps 1–5. Cardinality bound:
```
|N_{S, p}|  ≤  |K(p)| · |R(S, p)|² · op-depth(S) · 2^{p−1}
≤  2^p · |R(S, p)|² · op-depth(S) · 2^{p−1}.
```

**Step 7 — Borel measurability on `M`.** Piecewise-constant functions on `[0, 1)` with finite breakpoint sets are finite linear combinations of indicators of half-open intervals, hence Borel measurable. So `δ(S, ·, p) : M → ℝ_{≥0}` is Borel measurable. Codomain non-negativity follows from `d_𝕋 ≥ 0` and `max ≥ 0`.

**Step 8 — Joint measurability on `D`.** For each `(S, p) ∈ S × P` (a countable set with discrete σ-algebra `𝒫(S) ⊗ 𝒫(P)`), the section `δ(S, ·, p) : M → ℝ_{≥0}` is Borel measurable. By the product-σ-algebra criterion for measurable functions on `D = S × M × P` with discrete factors `S × P` and Borel factor `M`, the joint function `δ : D → ℝ_{≥0}` is measurable. ∎

**Compound-conversion structural anchor.** Matula §IV (compound truncation: invariant set = intersection of significance spaces, Theorem 4; iterated rounding stabilizes after at most three applications, Theorem 8) provides the structural reason composition closure remains well-behaved beyond the proof above: chaining conversion primitives across multiple precisions (or, hypothetically, multiple bases) would otherwise be a candidate route for breakpoint-set blowup, but Matula's compound-conversion theorems bound the iterated behavior. Phase 1a stays at fixed `(β, n) = (2, p)`, so the compound theorems are not directly invoked; they supply structural confidence that the formalism scales if Phase 1c needs cross-precision reasoning (e.g., for clause (iii)'s closure-class indicator on schemes that vary precision adversarially).

## Compatibility checks

**§1.7 candidate description.** §1.7 reads "δ is the cost of `{Δ_k}` cocycle compression — the failure-to-agree of cocycle-product factors across butterfly refinements and primitive modes, measured pointwise." Definition (c) implements this exactly: *pointwise* (per `m`), *across butterfly refinements* (max over `r, r' ∈ R(S, p)`), *across primitive modes* (max over `k ∈ K(p)`).

**§6.5 operational compressibility commitment.** §6.5 commits to operational compressibility as the cost-norm (debt #14). Definition (c) implements operational compressibility: it returns 0 iff cocycle products agree across all refinement and mode pairs, and a positive failure-magnitude otherwise. This is the testable form recommended at [fft/COCYCLE-COMPOSITION-LAW.md](fft/COCYCLE-COMPOSITION-LAW.md) §"Cost-norm choice."

**Debt #14 status.** Committed; secondary cost-norms (low-rank, factorization, residual-coordinate) remain available as sharper analytic tests but are not committed and do not enter Phase 1a.

## What Phase 1a does not do

- **Pushforward to Z.** Phase 1a defines `δ` on `D = S × M × P`. Phase 1b's universal-property step pushes `δ` to `Z` via the structure morphisms of debt #12.
- **Faithfulness clauses (i), (ii), (iii).** Phase 1c proves these against `(Z, ℱ, ν, δ)` once Phase 1b lands `Z`. Phase 1a delivers measurability, not faithfulness.
- **Rigorous composition-law proof.** Debt #2's residual: full FP arithmetic model + regularity-guard exhaustiveness + edge cases (subnormals, overflow). Phase 1a uses the composition-law skeleton; the rigorous version is downstream.
- **Non-triviality of `δ`.** Whether `δ > 0` on the relevant FFT-style class at the bounded/unbounded boundary is the existence half of debt #5 (endpoint commitment), not Phase 1a's scope.

## Open inside Phase 1a

- **Character index set boundary `K(p)`.** The choice `K(p) = { k : |k| < 2^p }` matches Matula's strict-inequality bound on `S^β_n`. A sharper choice could restrict to *primitive* characters at precision `p` (`k` coprime to `2^p`), reducing the index set without changing measurability. Affects the constant in any resulting inequality, not the qualitative formalization.
- **Refinement set `R(S, p)` cardinality.** Finite but combinatorially large. Whether `δ(S, m, p)` is computationally achievable (vs. just well-defined) is a separate question; Phase 1a requires only well-definedness and measurability.
- **Native-operation FP-primitive decomposition.** Phase 1a inherits §4.2.1's regularity guard as the commitment that each operation decomposes into elementary FP primitives at granularity `p`. Phase 1a does not enumerate this decomposition explicitly; if Phase 1c clause (iii)'s closure-class indicator needs explicit per-op breakpoint counts, that's a Phase 1c residual.
- **Base parametrization.** `β = 2` committed for Phase 1a's operational scope; the Matula formalism is base-parametrized via `S^β_n` and the cocycle `ε_β(m) = log_β(1 + m) − m`. If Phase 1c clause (iii) needs commensurability-class crossing structure (the option-3 discriminator question of `fft/PHASE-DEFECT.md` per Matula's commensurability dichotomy), the base parametrization can be made explicit there without disturbing Phase 1a.

## Acceptance status

| Criterion | Status |
|---|---|
| (a) Definition with explicit functional form | ✓ Definition (c) |
| (b) Domain: precisely typed input space | ✓ `D = S × M × P` with product σ-algebra |
| (c) Codomain: `ℝ_{≥0}` with Borel σ-algebra | ✓ |
| (d) Measurability proof | ✓ Steps 1–8, anchored in Matula §II–§IV |
| (e) Compatibility with §1.7, §6.5, #14 | ✓ See "Compatibility checks" |

**Phase 1a complete.** All five acceptance criteria met. FP arithmetic model committed to Matula 1970 significance spaces at `(β, n) = (2, p)`; `δ` typed as a measurable function on `D = S × M × P`; measurability proved via piecewise-constancy with finite breakpoint sets, rigorously anchored in Matula's significance-space density and conversion-primitive structure.

**Phase 1a hand-off to Phase 1b.** Phase 1b's universal-property step takes `(D, ℬ_D, δ)` as input and constructs `(Z, ℱ, ν)` with `δ` pushed forward as the universal transaction-cost coordinate. The pushforward will require Phase 1b's diagram + structure morphisms (debt #12); Phase 1a's `δ` lives natively on `D` until Phase 1b assembles the limit object. Matula's significance-space formalism remains available to Phase 1b/1c as the inherited FP vocabulary; the commensurability dichotomy (Matula Lemma 1 / Corollary 2) is the natural option-3 discriminator for Phase 1c clause (iii) closure-class indicator structure.
