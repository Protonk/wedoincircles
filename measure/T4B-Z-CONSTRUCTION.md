# T4B-Z-CONSTRUCTION

Phase 1b of the T4b decomposition (`paper/T4B-DECOMPOSITION.md`): construct `Z`, the currency-universal limit object, as a measurable-space limit over the 6-node diagram of cost-coordinate currencies. Companion to Phase 1a ([measure/T4B-DELTA-FORMAL.md](measure/T4B-DELTA-FORMAL.md)) and Phase 1c (clauses (i)–(iii) faithfulness, deferred). Spec at [measure/THE-FIRST-BRIDGE.md](measure/THE-FIRST-BRIDGE.md).

## Recap

T4b owes a currency-universal limit object: a measure space `(Z, ℱ, ν)` together with a `δ`-coordinate `δ : Z → ℝ_{≥0}` (the universal transaction cost), where `Z` is the limit over the three lower-bound currencies (Morgenstern bounded-additive, Winograd modular product, AFW cyclotomic-multiplicative) joined by the three substrate-side iso registers (rate, constant, almost-every) on equal footing. Structure morphisms between currency-specific cost coordinates supply the diagram `Z` is the limit over.

Phase 1b's task: list the diagram explicitly, construct `Z` as the limit, verify the universal property, define `ν`, and specify how Phase 1a's `δ` on `D = S × M × P` pushes to `Z`.

The construction is *categorical* — limit in the category of measurable spaces. Per-morphism rigorous verification is **debt #12**'s residual; Phase 1b lists the morphisms and assumes their properties (measurability, measure-preservation up to specified rescalings), with the limit construction completed under those assumptions. This is the "interleaved with #12" closure pattern named in the ledger.

## The diagram

Six nodes, each a measurable space `(X_i, ℱ_i)` with a cost coordinate `κ_i : X_i → ℝ_{≥0}`, plus structure morphisms (debt #12 inputs).

### Algorithm-side currency nodes

**`N_M` (Morgenstern bounded-additive).** `X_M` = bounded-coefficient linear circuits computing the DFT, equipped with a coefficient bound `c`. `ℱ_M`: discrete on circuit topology × Borel on `c`. `κ_M(circuit, c)` = number of additive gates, weighted by Morgenstern's determinant-potential argument (PAPER §3.3 / Table 1). Threshold `T_M = Ω(n log n)` on the bounded-coefficient regime.

**`N_W` (Winograd modular product).** `X_W` = bilinear circuits on polynomial-quotient rings `ℚ[x]/T_P`, indexed by the modulus polynomial `T_P`. `ℱ_W`: discrete on circuit / polynomial structure. `κ_W(circuit, T_P)` = number of essential bilinear multiplications. Threshold `T_W = 2n − k` where `k` = number of irreducible factors of `T_P` over the base field (PAPER §3.4 / Table 1).

**`N_AFW` (AFW cyclotomic-multiplicative).** `X_AFW` = rational-equivalence classes of cyclotomic decompositions of group DFTs `ℚ[G] = ∏_{d | |G|} ℚ(ζ_d)`, indexed by the abelian group `G`. `ℱ_AFW`: discrete on decomposition + group structure. `κ_AFW` = sum over cyclotomic factors of multiplicative complexity per factor. Threshold `T_AFW` per AFW 1984 (PAPER §3.5 / Table 1).

### Substrate-side iso register nodes

**`N_rate` (Iso rate register).** `X_rate` = inscribed regular `n`-gon family, indexed by `n ≥ 3`. `ℱ_rate`: discrete on `n`. `κ_rate(n) = Δ_n = 4π⁴/(3n²) + O(1/n⁴)` per Hurwitz Parseval expansion ([corners/HURWITZ-FIRST-BAND-CONCENTRATION.md](corners/HURWITZ-FIRST-BAND-CONCENTRATION.md)).

**`N_const` (Iso constant register).** `X_const` = **convex** simple closed planar curves with isoperimetric data `(L, A, Δ = L² − 4πA)`. The convex restriction is load-bearing: convex bodies have well-defined area without invoking the Jordan curve theorem (post-1882), keeping N_const's content pre-1882 in the L-W-envelope sense (`memos/OLD-TIME-RELIGION.md` content-not-calendar discipline). Bonnesen 1921 / 1924 strengthenings are convex-curve facts; the 5π chain inflation in `iso/THREE-REGISTER-SYNTHESIS.md` Claim 1 holds in the convex setting; nothing load-bearing is lost by restriction. `ℱ_const`: Borel on convex-curve-shape space (Hausdorff metric on convex bodies). `κ_const(γ) = Δ(γ)`, with Bonnesen-strengthening `Δ(γ) ≥ 4π · d(γ)²` (annulus-width form, Bonnesen 1924; [iso/THREE-REGISTER-SYNTHESIS.md](iso/THREE-REGISTER-SYNTHESIS.md) Claim 1).

**`N_aae` (Iso almost-every register).** `X_aae` = parametric measure spaces (parametric family of convex curves + probability measure on parameter space; Khintchine / Beck 1994 framework). `ℱ_aae`: Borel on parametric measure space. `κ_aae(family, μ)` = a.e. value of `Δ` under `μ`. Convex-family restriction inherited from N_const's convex restriction.

### Structure morphisms (debt #12)

Algorithm-side (3):

- **`f_{MW} : N_M → N_W`.** Bounded-coefficient → unbounded-rational-equivalence transfer. Bounded-additive circuits embed into bilinear circuits via the bounded-coefficient → polynomial-quotient identification. Cost-rescaling: bounded-side additions become bilinear multiplications under the embedding; the rescaling factor is per Morgenstern → Winograd cost-currency conversion (debt #9(b) component).
- **`f_{WAFW} : N_W → N_AFW`.** Modular product → cyclotomic decomposition. The polynomial-quotient `ℚ[x]/T_P` decomposes via CRT into `∏ ℚ[x]/p_i` over irreducible factors `p_i`; further cyclotomic identification when factors are cyclotomic. Cost-preserving up to factor-multiplication accounting per Winograd → AFW conversion.
- **`f_{MAFW} : N_M → N_AFW`.** Composed: `f_{WAFW} ∘ f_{MW}`. Could be defined directly or as the composition; debt #12 chooses the canonical form. Phase 1b assumes the composition route.

Substrate-side (2):

- **`f_{rc} : N_rate → N_const`.** `5π` Sobolev → geometric chain. Inscribed regular `n`-gon family produces curves with `Δ_n`; the morphism associates each `n`-gon to its constant-register reading via the Sobolev → geometric chain. Cost-rescaling: the chain has worked overhead `5π ≈ 15.7×` weaker than Bonnesen direct ([iso/THREE-REGISTER-SYNTHESIS.md](iso/THREE-REGISTER-SYNTHESIS.md) Claim 1).
- **`f_{ca} : N_const → N_aae`.** Curve → parametric family embedding. Each constant-register curve admits a parametric family (e.g., the linear interpolation family between the curve and the disk); the morphism associates the curve's pointwise sharp inequality with the family's a.e. reading. *Type-gap*: discrete pointwise reading → continuous a.e. reading (categorial type-gap per [iso/THREE-REGISTER-SYNTHESIS.md](iso/THREE-REGISTER-SYNTHESIS.md)). The morphism exists at the level of the construction; whether it is cost-preserving up to a *finite* rescaling or admits only an asymptotic rescaling is debt #12's residual.

Cross-side (algorithm-side ↔ substrate-side):

Phase 1b commits to **cross-side connectivity via `δ`**, not via direct cross-side morphisms. The two halves of the diagram (algorithm-side and substrate-side) are joined "on equal footing" per §6.3's framing — each contributes nodes to the diagram but they are not connected by a structure morphism. Cross-side coupling emerges through `Z`'s universal property and the `δ`-coordinate, which encodes both algorithm-side `(μ, α)` and substrate-side iso-register costs. Phase 1c's clause (ii) carries the cross-register channel argument, which uses `δ`'s joint encoding.

**Debt #12 status.** Morphism-properties (measurability, cost-rescaling factors, loop-consistency) are listed and assumed; rigorous per-morphism verification remains open inside #12. Phase 1b's construction is correct under those assumptions.

## The limit construction

In the category of measurable spaces, the inverse limit of the diagram exists as a measurable subspace of the product:

```
Z  :=  lim_← Diagram
    =  { (x_M, x_W, x_AFW, x_rate, x_const, x_aae) ∈ ∏_i X_i :
         f_{MW}(x_M) = x_W,
         f_{WAFW}(x_W) = x_AFW,
         f_{MAFW}(x_M) = x_AFW,
         f_{rc}(x_rate) = x_const,
         f_{ca}(x_const) = x_aae }.
```

Equipped with the trace σ-algebra `ℱ_Z := ℱ_∏ ∩ Z`, where `ℱ_∏ := ⊗_i ℱ_i` is the product σ-algebra on the cartesian product `∏_i X_i`.

**Existence.** Each constraint `f_{ij}(x_i) = x_j` is the equalizer of two measurable maps `(proj_i, f_{ij} ∘ proj_i)` and `(proj_j)` from `∏ X_i` to `X_j`, hence a measurable subset of `∏ X_i`. Finite intersection of measurable sets is measurable, so `Z ∈ ℱ_∏` and `(Z, ℱ_Z)` is a well-defined measurable subspace.

**Standard Borel.** If each `(X_i, ℱ_i)` is a standard Borel space and each morphism `f_{ij}` is a measurable map between standard Borel spaces, then `(Z, ℱ_Z)` is a standard Borel space (the category of standard Borel spaces is closed under finite products and measurable subspaces). All algorithm-side nodes are countable-discrete or discrete×Borel, hence standard Borel; substrate-side nodes are Borel on metric spaces (curve shape, parametric measure space), hence standard Borel under the standard separability assumptions.

## Universal property

**Claim.** For any measurable space `(X, 𝒢)` equipped with measurable maps `π_i : X → X_i` (one per node) such that `f_{ij} ∘ π_i = π_j` for every morphism `f_{ij}` in the diagram, there is a unique measurable map `u : X → Z` with `π_i = (proj_i) ∘ u` for each `i`, where `proj_i : Z → X_i` is the projection onto the `i`-th coordinate.

**Construction of `u`.** Define `u(x) := (π_M(x), π_W(x), π_AFW(x), π_rate(x), π_const(x), π_aae(x)) ∈ ∏ X_i`. By the compatibility hypotheses `f_{ij} ∘ π_i = π_j`, the tuple `(π_i(x))_i` satisfies all the morphism-equality constraints defining `Z`, hence lies in `Z`. `u` is measurable as a tuple of measurable maps into a product space, restricted to a measurable subspace.

**Uniqueness.** The tuple-form is forced by the projection equations `π_i = proj_i ∘ u`: if `u'` is any map satisfying these, then `proj_i ∘ u' = π_i = proj_i ∘ u` for each `i`, so `u' = u` on each coordinate, hence `u' = u`. ∎

This is the standard universal property of inverse limits in categories of structured sets.

## Pushforward measure `ν`

Each currency node `N_i` carries (or is assumed to carry, per debt #12) a measure `ν_i` on `(X_i, ℱ_i)` — for the algorithm-side currencies, `ν_i` may be a counting measure on the discrete circuit / decomposition space; for the substrate-side iso registers, `ν_rate` is counting on `n`, `ν_const` is a Borel reference measure on curve-shape space, `ν_aae` is the meta-distribution on parametric measure spaces. The morphisms `f_{ij} : N_i → N_j` are assumed measure-preserving up to specified rescaling factors `r_{ij}`:
```
f_{ij,*}  ν_i  =  r_{ij}  ·  ν_j.
```

**Definition of `ν` on `Z`.** Pull back any single currency's measure to `Z` via the projection:
```
ν  :=  proj_M^*  ν_M.
```
Under the morphism-rescaling assumption, the choice of currency is canonical up to an overall rescaling factor: `proj_M^* ν_M = (∏_path r_{ij}) · proj_j^* ν_j` for any `j` reachable from `M` via a directed path in the diagram.

**Consistency check.** For any pair of currencies `(i, j)` connected by a directed path in the diagram, the relation `proj_i^* ν_i = (path-product of rescalings) · proj_j^* ν_j` holds on `Z` by induction on the morphism chain.

**Loop-consistency.** Whether the morphism-rescaling factors compose consistently around closed loops in the diagram (i.e., whether `∏_loop r_{ij} = 1` for every closed directed loop) is part of debt #12's verification. The diagram has potentially one closed loop on the algorithm-side: `M → W → AFW` and `M → AFW` directly. Phase 1b assumes the diagram is loop-consistent; if loops don't close (`∏_loop r_{ij} ≠ 1`), the diagram needs an explicit normalization choice, which becomes a debt #12 sub-residual.

The substrate-side has no closed loops in the current 5-morphism diagram (`rate → const → aae` is a chain), so no substrate-side loop-consistency check is needed at Phase 1b.

## The `δ`-coordinate on `Z`

`δ : Z → ℝ_{≥0}` is the universal transaction cost. Phase 1b commits to the **rescaled-spread functional form** (refined per debt #12's per-morphism rigor at [measure/CURRENCY-MORPHISMS.md](measure/CURRENCY-MORPHISMS.md)):
```
δ((x_i)_i)  :=  max  over  directed-path (i → j) in the diagram  of  | κ_j(x_j)  −  r_{ij}^{(κ)} · κ_i(x_i) |,
```
where `r_{ij}^{(κ)}` is the composite cost-coordinate rescaling along the directed path from node `i` to node `j` (product of named per-morphism rescalings along the path; well-defined by composition closure of the diagram). Paths whose rescaling is non-finite (e.g., paths traversing the categorial type-gap of `f_{ca}`) are excluded from the max; the structural type-gap is encoded separately via Phase 1c clause (ii)'s non-existence of measurable inverse with finite rescaling.

**Justification.** On `Z`, each `x_i` is the morphism-image of a source coordinate; the per-point κ values may agree (e.g., `κ_rate(n) = κ_const(γ_n) = Δ_n` at n-gons), but the morphism *carries* its rescaling factor as a structural commitment — the chain's cost-of-derivation between currencies. `δ` reads this structural commitment by comparing each pair's κ values *after* applying the morphism rescaling. The Coasean transaction-cost reading lands literally: `δ((x_i)) = 0` iff every directed-path rescaling is exactly identity (no chain inflation between any pair); `δ((x_i)) > 0` captures the rescaling discrepancy as transaction cost.

For example, on a substrate-side `Z`-point at the `n`-gon with `f_{rc}` carrying `r_{rc}^{(κ)} = 5π` (per `measure/CURRENCY-MORPHISMS.md`):
```
| κ_const(γ_n)  −  r_{rc}^{(κ)} · κ_rate(n) |  =  | Δ_n  −  5π · Δ_n |  =  (5π − 1) · Δ_n  ≈  14.7 · Δ_n,
```
positive at every `n ≥ 3`. The 5π chain inflation is encoded in `δ` at every substrate-side Z-point.

**Measurability.** Each `κ_i ∘ proj_i : Z → ℝ_{≥0}` is measurable; each finite `r_{ij}^{(κ)}` (constant or measurable function of input) preserves measurability under multiplication; `max` over a finite set of measurable functions preserves measurability. Hence `δ` is measurable on `(Z, ℱ_Z)`.

**Phase 1a / Phase 1b interface.** Phase 1a's `δ` on `D = S × M × P` is the algorithm-side cocycle-product failure-to-agree. The map `D → Z` embeds `D` into the algorithm-side portion of `Z`. Phase 1a's `δ_D(S, m, p)` and Phase 1b's `δ_Z(z)` are related by `δ_D = δ_Z ∘ (D → Z)` on the algorithm-side image, with `δ_Z`'s rescaled-spread form picking up algorithm-side cost-rescalings (`r_{MW}^{(κ)}`, `r_{WAFW}^{(κ)}`) where they bind.

**Why rescaled spread, not raw spread.** The earlier (provisional) form `δ = max κ_i − min κ_i` reads the per-point spread but doesn't pick up morphism rescalings when per-point κ values agree (as they do at `n`-gons under `f_{rc}`). The rescaled-spread form is the necessary refinement — the morphism's rescaling factor is what reads on `δ`, not just the per-point κ comparison. Phase 1c clause (ii)'s claim that "δ encodes the 5π overhead" becomes literal under this form: every substrate-side Z-point traversing `f_{rc}` contributes at least `(5π − 1) · κ_rate` to `δ`.

## Compatibility with §6.3 prose

§6.3's prose: "a measure space `(Z, ℱ, ν)` ... together with a `δ`-coordinate `δ : Z → ℝ_{≥0}` (the universal transaction cost), where `Z` is the limit over the three LB currencies — Morgenstern bounded-additive, Winograd modular product, AFW cyclotomic-multiplicative — joined by substrate-side iso registers (rate, constant, almost-every; §5.2) on equal footing. Structure morphisms between currency-specific cost coordinates supply the diagram `Z` is the limit over."

Phase 1b's construction implements this exactly: `Z` as the inverse limit of the 6-node diagram; `ν` as pushforward from any single currency's measure; `δ` as the universal-transaction-cost coordinate (committed to `max − min` form); 3 algorithm-side + 3 substrate-side nodes "on equal footing" (parallel halves with no direct cross-side morphisms — cross-side coupling via `δ`); 5 structure morphisms named with debt #12 as the residual verification.

## What Phase 1b does not do

- **Faithfulness clauses (i), (ii), (iii).** Phase 1c's job. Phase 1b delivers `(Z, ℱ, ν, δ)`; Phase 1c proves the three faithfulness conditions against this object using Theorem K (clause i), the 5π synthesis (clause ii), and §5.5 + §4.2.1 (clause iii).
- **Per-morphism rigorous verification.** Debt #12's residual. Phase 1b lists the morphisms and assumes their properties; debt #12 verifies measurability, measure-preservation rescalings, and loop-consistency.
- **The full `D → Z` embedding.** Phase 1b sketches the Phase 1a / Phase 1b interface (D embeds via algorithm-side currencies); the rigorous embedding map is a Phase 1c interface task.
- **Direct cross-side morphisms.** Phase 1b commits to cross-side coupling via `δ` rather than via direct algorithm-side ↔ substrate-side morphisms. If Phase 1c clause (ii) (cross-register channel) requires a direct morphism, the diagram extends; Phase 1b's commitment is provisional in that sense.

## Open inside Phase 1b

- **Cross-side connectivity commitment.** Phase 1b commits to cross-side via `δ`. Phase 1c's clause (ii) tests this; if it fails, Phase 1b adds direct cross-side morphisms (e.g., `N_AFW ↔ N_rate` via the cyclotomic-`n` parameter shared with the regular-`n`-gon family).
- **Diagram loop-consistency.** Algorithm-side loop `M → W → AFW` vs `M → AFW` direct: rescaling factors must satisfy `r_{MW} · r_{WAFW} = r_{MAFW}` for `ν` to be well-defined. Debt #12 verifies; Phase 1b assumes.
- **`δ` functional form.** Committed to `max − min`. Phase 1c may push back if alternative forms (sup-inf, weighted) are needed for faithfulness.
- **`κ_aae` precise definition.** The "a.e. value of `Δ` under `μ`" reading of the almost-every register requires a specific reading — the `essential supremum`, the integral, or a quantile. Phase 1b leaves this as a debt #12 sub-residual; Phase 1c clause (ii) likely requires a specific choice.
- **`X_const` topology / σ-algebra.** Hausdorff metric on simple closed curves is the natural choice; alternatives (Sobolev metrics on parametrizations, Fréchet metrics) exist. Phase 1b commits to Hausdorff for concreteness.

## Acceptance status

| Criterion | Status |
|---|---|
| (a) Diagram explicitly listed (6 nodes + morphisms) | ✓ "The diagram" section |
| (b) `Z` constructed as the limit | ✓ "The limit construction" section |
| (c) Universal property verified | ✓ "Universal property" section |
| (d) Pushforward measure `ν` | ✓ "Pushforward measure ν" section (modulo debt #12 morphism-properties) |
| (e) Compatibility with §6.3 | ✓ See "Compatibility with §6.3 prose" |

**Phase 1b complete (modulo debt #12).** All five acceptance criteria met. `Z` constructed as inverse limit of the 6-node diagram; `ν` defined as pushforward from the algorithm-side `M` currency; `δ` committed to `max − min` functional form on `Z`. Per-morphism rigorous verification (measurability, rescaling factors, loop consistency) remains open in debt #12; Phase 1b's construction is correct under those assumptions, which the ledger names as "interleaved with #12" closure pattern.

**Phase 1b hand-off to Phase 1c.** Phase 1c receives `(Z, ℱ, ν, δ)` plus Phase 1a's `δ` on `D` and proves the three faithfulness clauses:
- (i) `f₁, f₂, f₃` factor through `δ` via Theorem K's L-side encoding (substrate-side route into `Z`'s `N_const` / `N_rate` projections);
- (ii) iso-register currency structure encodes measurably so cross-register conversion costs read on `δ` (the 5π Sobolev → geometric chain encoded via `f_{rc}` and the type-gap via `f_{ca}`);
- (iii) closure-class membership reads measurably against `(Z, ℱ, ν, δ)` (§5.5 admissibility envelope plus §4.2.1 regularity guard giving the `C_FFT` indicator on `Z`).

The three clauses parallelize cleanly across the three witnesses; each consumes a specific portion of `Z`'s structure. Phase 1b's `Z` and `δ` definitions are the inputs; Phase 1c's faithfulness verification is the output.
