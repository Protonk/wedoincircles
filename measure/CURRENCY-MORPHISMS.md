# CURRENCY-MORPHISMS

Discharge of construction-debt #12 (currency-morphism construction for the T4b limit). Per-morphism rigorous specification of the five structure morphisms in the inverse-limit diagram of `paper/T4B-DECOMPOSITION.md` / [measure/T4B-Z-CONSTRUCTION.md](measure/T4B-Z-CONSTRUCTION.md). Companion to Phase 1b (which interleaved with #12) and to [measure/ENDPOINT-COMMITMENT.md](measure/ENDPOINT-COMMITMENT.md) (whose currency-by-currency reading consumes the rescalings specified here).

Pointer back from `paper/PROOF-CHAIN.md` §6 debt #12 entry. Sources: PAPER §3.2 (in-canon Morgenstern↔Ailon); `iso/THREE-REGISTER-SYNTHESIS.md` Claim 1 (5π overhead); cocycle-translation memos in `fft/` (`MORGENSTERN-1973-COCYCLE-TRANSLATION.md`, `WINOGRAD-1978-COCYCLE-TRANSLATION.md`, `AUSLANDER-FEIG-WINOGRAD-1984-COCYCLE-TRANSLATION.md`).

## Recap

Phase 1b assumed five structure morphisms in the diagram, with measurability + measure-preservation up to rescaling factors + loop-consistency on the algorithm-side `M → W → AFW` triangle. #12's job: specify each morphism rigorously enough that Phase 1b's pushforward `ν`, Phase 1c's clauses (i)/(ii), and ENDPOINT-COMMITMENT.md's currency-by-currency reading all land.

The five morphisms:
- *Algorithm-side:* `f_{MW} : N_M → N_W`, `f_{WAFW} : N_W → N_AFW`, `f_{MAFW} : N_M → N_AFW` (composed).
- *Substrate-side:* `f_{rc} : N_rate → N_const`, `f_{ca} : N_const → N_aae`.

## Setting

Each morphism `f_{ij} : N_i → N_j` carries two kinds of rescaling, which Phase 1b conflated into a single "rescaling factor" — #12 disentangles:

- *Measure rescaling* `r_{ij}^{(ν)}` such that `f_{ij,*} ν_i = r_{ij}^{(ν)} · ν_j` on `f_{ij}(N_i) ⊆ N_j`. Governs the pushforward measure on `Z`.
- *Cost-coordinate translation* `r_{ij}^{(κ)}` relating `κ_j(f_{ij}(x))` to `κ_i(x)`. Governs how cost readings transfer between currencies; what δ on Z reads.

For algorithm-side morphisms with discrete-counting reference measures, `r_{ij}^{(ν)} = 1` in the simplest setting (the maps are state-space identifications). For substrate-side morphisms with continuous reference measures, `r_{ij}^{(ν)}` reflects the Jacobian of the embedding; the program does not need its specific value beyond measurability.

The cost-coordinate translation `r_{ij}^{(κ)}` is the load-bearing piece — it's what the §6.6 contradiction reads on δ.

## Algorithm-side morphisms

### `f_{MW} : N_M → N_W` (Morgenstern → Winograd)

**Domain.** `N_M` = bounded-coefficient linear circuits computing the DFT, with coefficient bound `c`; discrete-on-circuit-topology × Borel-on-`c` σ-algebra.

**Codomain.** `N_W` = bilinear circuits on polynomial-quotient rings `ℚ[x] / T_P`, indexed by the modulus polynomial `T_P`; discrete-on-circuit-topology × discrete-on-`T_P` σ-algebra.

**Map.** A bounded-coefficient linear circuit `C` computing the n-point DFT can be re-expressed as a bilinear circuit on `ℚ[x] / (x^n − 1)` via the standard identification: `x^n − 1 = ∏_{d | n} Φ_d(x)` (cyclotomic factorization), and the DFT corresponds to evaluation at `n`-th roots of unity in the residue rings. Each bounded-coefficient linear combination in `C` re-expresses as a step in the bilinear circuit on the residue rings. Define:
```
f_{MW}( (C, c) )  :=  (B, T_P)
```
where `B` is the bilinear circuit obtained from `C`'s polynomial-quotient re-expression, and `T_P = x^n − 1` for the n-point DFT.

**Measurability.** Both spaces have discrete-on-finite-circuit factors; the map is well-defined per the standard identification (one circuit topology in `N_M` maps to one in `N_W`). Discrete maps are measurable.

**Measure rescaling.** With counting measure on both sides, `r_{MW}^{(ν)} = 1`.

**Cost-coordinate translation.** `κ_M(C, c)` = number of additive gates in `C`; `κ_W(B, T_P)` = number of essential bilinear multiplications in `B`. The Morgenstern bound is `Ω(n log n)` additions on bounded coefficients; the Winograd bound is `μ(T_P) = 2n − k` essential bilinear multiplications, where `k` is the number of irreducible factors of `T_P` over the base field. The cost-coordinate translation factor:
```
r_{MW}^{(κ)}(C, c)  =  κ_W(f_{MW}(C, c))  /  κ_M(C, c)
```
is a function of the input (specifically of `n` and the factor count `k`), not a global constant. For the n-point DFT specifically, `r_{MW}^{(κ)} ≈ (2n − k) / (n log n)` at threshold-instances. Background per `fft/MORGENSTERN-1973-COCYCLE-TRANSLATION.md` and `fft/WINOGRAD-1978-COCYCLE-TRANSLATION.md` (verdict (b) Conditional translation, out-of-scope at the canon's primitive-operation level; the morphism here is at the cost-coordinate level, distinct from the canon-internal translation).

### `f_{WAFW} : N_W → N_AFW` (Winograd → Auslander–Feig–Winograd)

**Domain.** `N_W`-cyclotomic ⊆ `N_W` — bilinear circuits restricted to cyclotomic moduli `T_P = x^n − 1` (the cases the morphism maps natively). For non-cyclotomic `T_P`, the morphism is undefined; this is a domain restriction, not a totality failure of the diagram, since the algorithm-side currency states the apparatus tracks are exactly those reachable from `N_M`'s embedding via `f_{MW}`, all of which have cyclotomic `T_P`.

**Codomain.** `N_AFW` = rational-equivalence classes of cyclotomic decompositions of group DFTs `ℚ[G] = ∏_{d | |G|} ℚ(ζ_d)`, indexed by the abelian group `G`; discrete σ-algebra.

**Map.** Winograd's modular product on `ℚ[x] / T_P` decomposes via CRT into `∏_{i} ℚ[x] / p_i(x)` over irreducible factors. When `T_P = x^n − 1`, the irreducible factors over `ℚ` are exactly the cyclotomic polynomials `Φ_d(x)` for `d | n`, and the residue rings are `ℚ(ζ_d)`. The bilinear circuit on `ℚ[x] / (x^n − 1)` decomposes factor-by-factor into bilinear circuits on the cyclotomic field extensions. Define:
```
f_{WAFW}( (B, T_P) )  :=  (D, G)
```
where `D` is the cyclotomic-decomposed multiplicative-complexity object derived from `B`'s factor-by-factor structure, and `G = ℤ/nℤ` for `T_P = x^n − 1`.

**Measurability.** Discrete-to-discrete; measurable.

**Measure rescaling.** `r_{WAFW}^{(ν)} = 1` with counting measure.

**Cost-coordinate translation.** `κ_W(B, T_P) = 2n − k` (Winograd's bound); `κ_AFW(D, G) = ∑_{d | |G|} μ_AFW(d)` (AFW's per-cyclotomic-factor multiplicative complexity sum). The translation:
```
r_{WAFW}^{(κ)}(B, T_P)  =  κ_AFW(f_{WAFW}(B, T_P))  /  κ_W(B, T_P)
```
is again a function of the input. AFW 1984's content is exactly the per-factor accounting that makes this translation precise; the morphism inherits AFW's bound. Background per `fft/AUSLANDER-FEIG-WINOGRAD-1984-COCYCLE-TRANSLATION.md`.

### `f_{MAFW} : N_M → N_AFW` (composition)

**Definition.** `f_{MAFW} := f_{WAFW} ∘ f_{MW}`. Phase 1b commits to the composition route over a direct definition.

**Loop consistency.** The algorithm-side triangle `M → W → AFW` commutes by construction (`f_{MAFW}` is *defined* as the composition). Measure rescalings compose: `r_{MAFW}^{(ν)} = r_{WAFW}^{(ν)} · r_{MW}^{(ν)} = 1 · 1 = 1`. Cost-coordinate translations compose pointwise: `r_{MAFW}^{(κ)}(C, c) = r_{WAFW}^{(κ)}(f_{MW}(C, c)) · r_{MW}^{(κ)}(C, c)`. No separate verification needed.

## Substrate-side morphisms

### `f_{rc} : N_rate → N_const` (rate-register → constant-register)

**Domain.** `N_rate` = inscribed regular `n`-gon family, indexed by `n ≥ 3`; discrete σ-algebra.

**Codomain.** `N_const` = simple closed planar curves with isoperimetric data `(L, A, Δ)`; Borel σ-algebra (Hausdorff metric on simple closed curves).

**Map.** Each regular `n`-gon `P_n` is a simple closed curve `γ_n` with isoperimetric data `(L_n, A_n, Δ_n)`. Define:
```
f_{rc}( n )  :=  γ_n
```
the n-gon-as-curve embedding.

**Measurability.** `f_{rc}` is a discrete-to-Borel map; the image `{γ_n : n ≥ 3}` is a countable subset of `N_const`. Any map from a discrete space to a Borel space is measurable.

**Measure rescaling.** `r_{rc}^{(ν)}`: depends on the reference measure choice on `N_const` (Borel reference measure with weights, or counting on the n-gon-family subset). For Phase 1b's pushforward, the natural choice is to take the n-gon-family subset's induced measure, in which case `r_{rc}^{(ν)} = 1`.

**Cost-coordinate translation.** `κ_rate(n) = Δ_n = 4π⁴/(3n²) + O(1/n⁴)` (Hurwitz Parseval). `κ_const(γ_n) = Δ(γ_n) = Δ_n` directly (the same gap, evaluated at the n-gon).

**Rescaling: `r_{rc}^{(κ)} = 5π` (committed).** `f_{rc}` carries the chain's cost-of-derivation as its structural rescaling factor. The 5π is the resolved worked overhead between the rate-register asymptotic-bound construction and the constant-register direct-Bonnesen reading on the chained Sobolev → geometric route (`iso/THREE-REGISTER-SYNTHESIS.md` Claim 1, proved). The morphism *commits* to this overhead even when per-point `κ` values agree (e.g., at `n`-gons, both κ_rate(n) = Δ_n and κ_const(γ_n) = Δ_n give the same numerical value, but the chain's cost-of-derivation from rate to const is 5π regardless). The rescaling reads on `δ_Z` per Phase 1b's rescaled-spread form: `|κ_const(γ_n) − 5π · κ_rate(n)| = (5π − 1) · Δ_n > 0` at every n-gon `Z`-point.

**Why the rescaling is structural, not pointwise-equational.** The 5π factor is a property of the *bound technique* (Sobolev-derived rate-bound is 5π weaker than direct Bonnesen-strengthening), not of the per-point `Δ` value. On any specific curve, both registers read the curve's actual `Δ`; the 5π gap is the chain's bound-tightness loss. Phase 1b's rescaled-spread `δ_Z` reads this commitment by comparing rescaled κ values rather than raw κ values — the morphism's rescaling enters δ regardless of pointwise equality.

**Witness.** `iso/THREE-REGISTER-SYNTHESIS.md` Claim 1 (proved): resolved `5π` overhead on chained Sobolev → geometric route, with no single extremal function realizing all three sharpnesses simultaneously. The register-state ledger keeps Fejes-Tóth certification and Beck → specific-`π` as unresolved bridge/audit states rather than finite morphism costs. Convex restriction inherited from N_const (avoids Jordan; preserves Bonnesen content).

### `f_{ca} : N_const → N_aae` (constant-register → almost-every-register)

**Domain.** `N_const` as above.

**Codomain.** `N_aae` = parametric measure spaces (parametric family + probability measure on parameter space; Khintchine / Beck 1994 framework); Borel σ-algebra.

**Map.** Each convex constant-register curve `γ` (with the convex restriction inherited from `N_const`) admits a canonical parametric family via convex combination with the unit disk `D`: the linear-interpolation family
```
{ (1 − t) · D  +  t · γ  :  t ∈ [0, 1] }
```
where `+` is Minkowski sum after centering both bodies at their centroids and `·` is scalar dilation. Convex combinations of convex bodies are convex (and hence simple closed), so the family stays inside `N_const`-convex throughout. Define:
```
f_{ca}( γ )  :=  (linear-interpolation family from γ,  Lebesgue measure on [0, 1]).
```

**Measurability.** `f_{ca}` is a Borel-to-Borel map; the convex-combination construction is continuous in the Hausdorff metric on convex bodies (a standard fact in convex geometry, pre-1882 in content), so the embedding gives a continuous parametric family on `N_aae`.

**Measure rescaling.** `r_{ca}^{(ν)}`: again depends on reference measure choice. The natural choice gives `r_{ca}^{(ν)} = 1`.

**Cost-coordinate translation.** `κ_const(γ) = Δ(γ)`; `κ_aae(family from γ, Lebesgue) = ∫_0^1 Δ((1 − t) · disk + t · γ) dt` (or the a.e.-value of `Δ` under the parameter measure, per Phase 1b's `κ_aae` reading). The translation `r_{ca}^{(κ)}(γ)` is a finite real-valued function of `γ`.

**Categorial type-gap.** Per `iso/THREE-REGISTER-SYNTHESIS.md`: the constant-register reading is on curve-shape space (a single curve gives a pointwise sharp inequality); the almost-every reading is on parametric-measure space (a family + measure gives an a.e. value). The two are type-incompatible at the apparatus level — there's no measurable cross-section `s : N_aae → N_const` with `κ_const = κ_aae ∘ s` globally, because `κ_aae` averages over the family and loses the curve-shape information `κ_const` reads.

**Non-existence of measurable right-inverse with finite rescaling — qualitative argument.** Suppose for contradiction a measurable section `s : N_aae → N_const` exists with `κ_const(s(family, μ)) = α · κ_aae(family, μ)` for some constant `α`, and `f_{ca} ∘ s = id` on `f_{ca}(N_const)`. Then for every parametric family `(F, μ)` in the image, `s` selects a representative curve whose `Δ` is `α` times the family's a.e. `Δ`. The parametric family generated by `γ` via convex interpolation has `Δ`-distribution depending on `γ`'s entire convex shape — curvature distribution, asymmetries, eccentricity. Different starting curves can produce parametric families with the same a.e. `Δ` value (worked example: radial perturbations of the disk at modes `m = 2` with amplitude `a = 0.15` and `m = 5` with `a ≈ 0.0530938465` both give averaged deficit ≈ 0.4441; endpoint curves differ by radial sup ≈ 0.203). Information-loss arguments suggest `s` cannot consistently invert `f_{ca}` while preserving cost-coordinate proportionality, but the rigorous form requires sharpening: a measurable function from a many-to-one value space *can* select canonical representatives, so non-injectivity of `κ_aae` alone does not obstruct measurable selection. The type-gap is qualitatively visible at the apparatus level (curve-shape vs parametric-family type-incompatibility per `iso/THREE-REGISTER-SYNTHESIS.md`); the measure-theoretic non-existence proof remains a sharpening item.

**Status: qualitative; sharpening tracked.** The categorial type-gap is structurally evident from the type-mismatch between `N_const` (curve-shape space) and `N_aae` (parametric measure space) — `f_{ca}` is measurable, `f_{ca}` is not surjective, and `f_{ca}` has no obvious measurable right-inverse preserving cost. A rigorous non-existence proof requires more than information loss — it would need to argue that any candidate `s` violates either measurability or the cost-preservation condition uniformly. Sharpening is a Phase 1c residual; the qualitative reading suffices for Phase 1c clause (ii)'s structural-encoding argument because Phase 1c reads the type-gap as the apparatus's *non-availability of a finite cost-rescaling* `r_{ca}^{(κ)}`, not as a fully-rigorous non-existence theorem.

**Witness.** `iso/THREE-REGISTER-SYNTHESIS.md` Claim 1 plus its categorial-type-gap discussion.

## Loop-consistency verification

**Algorithm-side `M → W → AFW` triangle.** Loop consistency is automatic: `f_{MAFW} := f_{WAFW} ∘ f_{MW}` by definition. Measure rescalings compose multiplicatively (`r_{MAFW}^{(ν)} = r_{WAFW}^{(ν)} · r_{MW}^{(ν)} = 1`); cost-coordinate translations compose pointwise. No separate equality to verify.

**Substrate-side chain `rate → const → aae`.** No closed loops; the chain is acyclic. No loop-consistency check needed.

**Cross-side.** Per Phase 1b's commitment, no direct cross-side morphism; the algorithm-side and substrate-side halves of the diagram are connected only through Z's universal property and the δ-coordinate. No cross-side loops to check.

## Couplings

- **Consumed by:** Phase 1b's pushforward `ν` definition (the `r_{ij}^{(ν)}` rescalings are inputs); Phase 1c's clause (ii) cross-register encoding (the cost-coordinate translations `r_{ij}^{(κ)}` are what δ reads); ENDPOINT-COMMITMENT.md's currency-by-currency reading of debt #5 (the per-currency `δ_min^{(c)}(P)` derivation uses `r_{ij}^{(κ)}` to translate the substrate-side floor across currencies).
- **Depends on:** debt #9 (variable-precision canon re-read) — needed for the algorithm-side cost-coordinate translations to land at the apparatus's committed precision granularity. Without #9(c), the per-canon translations are at fixed precision only.
- **Adjacent extensional question:** "are the named morphisms all the reasonable morphisms?" — absorbed into §Conclusion outflow as the recursion-theoretic horizon (parallel to #11(iii) and #15). #12 verifies the *named* morphisms; the extensional-class question is not closable here.

## Open inside #12

- **Cost-coordinate translations as functions of input.** `r_{MW}^{(κ)}, r_{WAFW}^{(κ)}, r_{ca}^{(κ)}` are functions of the input rather than constants. The currency-by-currency reading of debt #5 uses these functions; specifying their analytic form (e.g., `r_{MW}^{(κ)}(n) = (2n − k(n)) / (n log n)` with `k(n)` the irreducible-factor count) is concrete bookkeeping. Closed at the qualitative level here; quantitative closure tracks debt #9(c).
- **Reference measure choice on substrate-side nodes.** `ν_const` on Borel curve-shape space and `ν_aae` on parametric-measure space have multiple natural choices (Hausdorff measure variants, weighted Borel, etc.). #12 commits to "natural choice" without specifying which; if Phase 1c's clause (ii) needs a specific weighting, the choice is refined there.
- **Non-existence proof for `f_{ca}^{-1}` rigor.** The information-loss argument for the type-gap is qualitatively right but could be sharpened with explicit families of curves having the same a.e.-Δ but different shapes. Not gating any downstream debt.

## Acceptance status

| Item | Status |
|---|---|
| `f_{MW}` specification + measurability + rescalings | ✓ Discrete-to-discrete; `r_{MW}^{(ν)} = 1`; `r_{MW}^{(κ)}` per Morgenstern↔Winograd cost-translation, threshold-formula form |
| `f_{WAFW}` specification + measurability + rescalings | ✓ Discrete-to-discrete on `N_W`-cyclotomic; `r_{WAFW}^{(ν)} = 1`; `r_{WAFW}^{(κ)}` per AFW per-factor accounting |
| `f_{MAFW}` (composition) | ✓ Defined as `f_{WAFW} ∘ f_{MW}`; loop consistency automatic |
| `f_{rc}` specification + measurability + rescalings | ✓ Discrete-to-Borel into convex `N_const`; **`r_{rc}^{(κ)} = 5π` committed as the chain's resolved finite cost commitment** (read on δ_Z via Phase 1b's rescaled-spread form); `r_{rc}^{(ν)}` deferred to natural choice |
| `f_{ca}` specification + measurability | ✓ Borel-to-Borel via convex-combination interpolation (well-defined on convex N_const, measurable in Hausdorff metric); `r_{ca}^{(ν)}` deferred to natural choice |
| `f_{ca}` type-gap rigor | **Qualitative; sharpening tracked.** The categorial type-gap is structurally evident; rigorous non-existence proof for measurable cost-preserving right-inverse remains a Phase 1c residual. Phase 1c clause (ii) consumes the qualitative reading. |
| Loop consistency (algorithm-side triangle) | ✓ Automatic by composition definition |
| Convex restriction of `N_const`, `N_aae` | ✓ Inherited from Phase 1b's restriction; avoids Jordan, preserves Bonnesen content, makes f_ca map well-defined |

**Debt #12 closes (modulo: debt #9(c) for quantitative analytic forms of cost-coordinate translations; Phase 1c residual for `f_{ca}` type-gap rigor sharpening).** Five morphisms specified at a level sufficient for Phase 1b's pushforward, Phase 1c's clauses (i)/(ii)/(iii), and ENDPOINT-COMMITMENT.md's currency-by-currency reading. The Jordan-curve L-W audit question (raised at the apparatus-refinement stage) is sidestepped by the convex restriction on `N_const`; substrate-side content stays pre-1882.

## Hand-off back to apparatus

After this discharge, the apparatus's open structural items are:
- **Debt #3 (effective H–L `n=1` cost-form)** — substrate-side delivery owed; the long pole.
- **Debt #9(c) (variable-precision canon re-read)** — substantive substrate-side methodology commitment; quantitative closure of `r_{ij}^{(κ)}` translations tracks here.
- **Debts #6, #7, #8, #10** — supporting / cyclotomic-rigidity / discipline; not gating §4.5.
- **Debts #13, #14, #15** — definitional / committed / recursion-theoretic horizon; not closable as discrete proof obligations within the apparatus.

§4.5's theorem now holds modulo (#3) + (#9(c)). Both are tractable in their own right; #3 is the substrate-side long pole; #9(c) is the methodological commitment for re-reading canon at variable precision. The structural argument is otherwise complete.
