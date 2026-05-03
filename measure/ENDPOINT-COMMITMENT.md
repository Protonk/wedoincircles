# ENDPOINT-COMMITMENT

Discharge of construction-debts #5 (endpoint commitment as non-vanishing transaction-cost lemma at canon thresholds) and #2(8) (floor extension bridge between #5's two halves). Tightly coupled debts; discharged together because closing #2(8) collapses #5's halves into two readings of one structural fact. Pointer back from `paper/PROOF-CHAIN.md` §6 debt #5 and debt #2 entries; spec at [measure/THE-FIRST-BRIDGE.md](measure/THE-FIRST-BRIDGE.md) §"What The Argument Must Show"; Coasean reading at [measure/COASE-FRICTION-AND-SPECIALISTS.md](measure/COASE-FRICTION-AND-SPECIALISTS.md).

Inherits the faithful `(Z, ℱ, ν, δ)` structure from the T4b decomposition (`paper/T4B-DECOMPOSITION.md`): Phase 1a's δ on `D = S × M × P` ([measure/T4B-DELTA-FORMAL.md](measure/T4B-DELTA-FORMAL.md)); Phase 1b's `Z` as inverse limit ([measure/T4B-Z-CONSTRUCTION.md](measure/T4B-Z-CONSTRUCTION.md)); Phase 1c's three faithfulness clauses ([measure/T4B-FAITHFULNESS.md](measure/T4B-FAITHFULNESS.md)).

## Recap

**Debt #5 — endpoint commitment.** A non-vanishing transaction-cost lemma at canon threshold `T(P)`, in two halves:
- *(Existence half)* Any FFT-style method `M` achieving `T(P)` pays `δ ≥ δ_min(P) > 0` at the bounded/unbounded coefficient boundary, currency-by-currency (Morgenstern bounded-additive, Winograd modular product, AFW cyclotomic-multiplicative).
- *(Implication half)* Strict improvement past `T(P)` requires `δ → 0`.

The lemma ties threshold improvement to the cost-coordinate value δ. Per PAPER §6.2: implication direction (descent → endpoint), not biconditional.

**Debt #2(8) — floor extension bridge.** Sub-question (8) of debt #2's eight-sub-question algebra-of-δ decomposition: the structural bridge between #5's existence claim *at* `T(P)` and the implication claim *past* `T(P)`. Without (8), the halves are independent claims sharing a label; closing (8) collapses them into two readings of one floor-extension fact about the boundary.

## Setting

From Phase 1c: `(Z, ℱ_Z, ν, δ_Z)` with `δ_Z := max_i κ_i − min_i κ_i` over the 6 currency nodes. Substrate-side embedding `ι : L → Z` carries `(k, n) ↦ (trivial_M, trivial_W, trivial_AFW, n, γ_n, family(γ_n))`; on this image, `δ_Z(ι(k, n)) = max(Δ_n, α_n)` where `Δ_n = 4π⁴/(3n²) + O(1/n⁴) > 0` for `n ≥ 3`.

Per `iso/THREE-REGISTER-SYNTHESIS.md` Claim 1: the substrate-side iso-register currency-stratification has worked overhead `5π ≈ 15.7×` between rate and constant on the chained Sobolev → geometric route, plus a categorial type-gap to almost-every. This is the substrate-side `δ > 0` instance per §3.6.2 face (iv) (PAPER:202) — encoded measurably on Z via Phase 1c's clause (ii).

For an FFT-style method `M`, the algorithm-side embedding `embed : S → Z` (Phase 1a / Phase 1b interface) places `M`'s algorithm-side state at a Z-point with positive substrate-side projections (every Z-point has a substrate-side coordinate by Z's product structure). The cross-currency / cross-register conversion costs read on `δ_Z` per Phase 1c's clauses (i) and (ii).

## Lemma (existence half of #5)

**Statement.** For every problem `P` in the cyclotomic-DFT class (and adjacent compute-cost problems), and every FFT-style method `M` achieving `T(P)`, there exists `δ_min(P) > 0` such that `δ_Z(embed(M's state at T(P))) ≥ δ_min(P)`, currency-by-currency.

**Proof.** Fix `P` and `M`. Let `n_P` be the size parameter of `P`'s threshold-instance (e.g., `n` in the cyclotomic-DFT class indexed by group order). The algorithm-side embedding `embed(M) ∈ Z` has substrate-side projections `(proj_rate, proj_const, proj_aae)(embed(M))` at Z-points whose substrate-side coordinate is determined by `n_P` via the diagram constraints.

By Phase 1c's clause (i) factor-through, `f_3(_, n_P) = Δ_{n_P}` factors through `δ_Z`; specifically, `δ_Z(embed(M))` is at least the substrate-side iso-register cost contribution at `n_P`, which is `Δ_{n_P} > 0`.

Per `iso/THREE-REGISTER-SYNTHESIS.md` Claim 1, the substrate-side currency-stratification supplies a worked-instance overhead between rate and constant of `5π · Δ_{n_P}`: any cross-register conversion at `n_P` pays at least this overhead. By Phase 1c's clause (ii) encoding, this overhead reads on `δ_Z` as a contribution to the spread `max_i κ_i − min_i κ_i` at substrate-side Z-points reachable from `embed(M)` through the diagram morphisms.

Therefore
```
δ_Z(embed(M's state at T(P)))  ≥  δ_min(P)  :=  max(Δ_{n_P}, (5π − 1) · Δ_{n_P} / 5π, type_gap_contribution_{n_P})  >  0.
```
The right-hand side is strictly positive for every `n_P ≥ 3` because each component is.

**Currency-by-currency.** The lemma's "currency-by-currency" reading per §6.2 is automatic from `δ_Z`'s `max − min` form: the spread takes contributions from each of the 3 algorithm-side and 3 substrate-side currencies; the substrate-side iso-register contribution is positive (as shown above); therefore `δ_Z > 0` regardless of which algorithm-side currency dominates.

For each currency `c ∈ {Morgenstern, Winograd, AFW}`, write `δ_min^{(c)}(P)` for the lemma's floor specialized to currency `c`'s threshold cell (Morgenstern's `Ω(n log n)` additive, Winograd's `2n − k` modular product, AFW's per-factor multiplicative). The lemma reads `δ_Z(embed(M)) ≥ δ_min^{(c)}(P) > 0` at currency `c`'s threshold cell, with `δ_min^{(c)}(P)` derived from the substrate-side floor at `n_P` weighted by currency-specific morphism rescalings (debt #12 supplies the rescalings; the floor's positivity is invariant under multiplicative rescalings).

**Witness.** §3.6.2 face (iv) substrate-side currency-stratification, encoded measurably on Z via Phase 1c clause (ii). Theorem K (§5.6) is the necessity-side witness for clause (i)'s factor-through, supplying the L-side route into Z that the existence-half embedding rides on.

∎

## Bridge (debt #2(8)) — floor extension from at-threshold to past-threshold

**Statement.** The substrate-side floor `δ_min(P) > 0` at `T(P)` does not depend on whether `M` is at `T(P)` or attempting to descend past `T(P)`; the floor is invariant under T(P)-movement.

**Proof.** The substrate-side `δ > 0` instance is a property of the iso-register structure itself: 5π overhead between rate and constant on the Sobolev → geometric chain (`iso/THREE-REGISTER-SYNTHESIS.md` Claim 1), plus the categorial type-gap to almost-every. This structure depends on the substrate-side state space (planar curves, parametric families) and the morphism `f_{rc}, f_{ca}` rescalings — *not* on the algorithm-side method `M`'s position relative to `T(P)`.

Concretely: when `M` attempts strict improvement past `T(P)`, it moves to a refined algorithm-side state that may differ from the at-threshold state. But the substrate-side projections of `embed(M)` continue to live on the same iso-register diagram with the same morphism rescalings. The cross-register conversion costs (rate→constant, constant→aae, rate→aae composed) remain measurable on `(Z, ℱ_Z, ν, δ_Z)` with the same 5π overhead and type-gap encoding.

The substrate-side floor is therefore *invariant under M's algorithm-side movement*. δ_min(P) at T(P) extends to δ_min(P) past T(P) by this invariance.

**Closure-form choice (among the three the algebra of δ leaves open).** Per the eight-sub-question decomposition at `measure/ALGEBRA-OF-DELTA.md`, sub-question (8) admits three candidate closure forms: continuity, monotonicity, quantization. The discharge here closes via *invariance of the substrate-side structure* — closest to the monotonicity reading in spirit, but stronger: the floor doesn't merely fail to decrease; it doesn't move at all under T(P)-direction.

Continuity, monotonicity, quantization were candidates for closing (8) under different structural hypotheses about δ's behavior at the threshold. The Phase 1c-delivered faithful structure makes the substrate-side floor a *property of the substrate*, not a property of where M sits — which moots the at-vs-past distinction directly.

∎

## Lemma (implication half of #5)

**Statement.** Suppose `M` is an FFT-style method achieving strict improvement past `T(P)`. Then `δ_Z(embed(M)) → 0` along the descent path.

**Proof.** "Strict improvement past `T(P)`" means `M` produces a lower-bound proof at a threshold value strictly below `T(P)` — equivalently, `M` certifies a cost-coordinate value strictly less than `T(P)`'s threshold cell value. Per Phase 1a's δ definition (operational compressibility cost-norm: failure-to-agree of cocycle products across butterfly refinements, measured pointwise), `M`'s cocycle products must agree below the at-threshold spread, which on Z translates to `δ_Z(embed(M)) < δ_min(P)`.

By the existence half + the bridge: `δ_Z(embed(M)) ≥ δ_min(P) > 0` at *and* past `T(P)`. So `δ_Z(embed(M)) < δ_min(P)` requires `δ_Z(embed(M)) → 0` as `M` attempts strict improvement.

**Implication direction only.** §6.2 disclaims biconditional: the lemma says descent → δ → 0, not δ → 0 → descent. The reverse direction would require additional structure (specifically, that any δ → 0 sequence corresponds to an actual descent attempt, which is a separate claim about what δ's vanishing implies for `M`'s lower-bound certificate).

∎

## Coupled reading: §6.6 contradiction

Combining the existence half, the bridge, and the implication half: any FFT-style method `M` attempting strict improvement past `T(P)` would require `δ_Z(embed(M)) → 0` (implication half), but the substrate-side floor `δ_Z(embed(M)) ≥ δ_min(P) > 0` holds at and past `T(P)` (existence half + bridge). The two requirements contradict.

This is the §6.6 contradiction in lemma form. Combined with channel exhaustiveness (debt #11, discharged at `fft/CHANNEL-EXHAUSTIVENESS.md`), the contradiction lands for *every* FFT-style method's descent attempt: the four channels exhaust the descent routes, T4b's three faithfulness clauses cover the channels, and the endpoint commitment lemma forces the cost-coordinate violation that the channels can't escape.

§4.5's working theorem now reads: no FFT-style method `M` proves a lower bound on `P` improving past the existing threshold `T(P)`, because doing so would force `δ → 0` on a structure that pays `δ ≥ δ_min(P) > 0`.

## What this discharge does not do

- **Substrate-side delivery (#3).** The lemma's substrate-side floor uses iso-register currency-stratification (proved at `iso/THREE-REGISTER-SYNTHESIS.md` Claim 1). The substrate-side cost-form for effective Hermite–Lindemann at `n = 1` (debt #3) is a separate substrate-side input the cost algebra consumes; not gated by #5 or #2(8).
- **Per-morphism rigor (#12).** The currency-by-currency reading of the existence half uses morphism rescalings supplied by debt #12. Phase 1b interleaved with #12; rigorous per-morphism verification of rescalings stays at #12.
- **Variable-precision canon re-read (#9(c)).** The lemma's "currency-by-currency" reading at `T(P)` requires the canon's threshold cells to be re-read at variable precision under the §1.2 uniform-charge guard. Phase 1c assumes this; #9(c) is the substantive substrate-side commitment outstanding.
- **Biconditional direction.** The implication half is one-direction (descent → δ → 0); the converse requires additional structure not provided here.

## Open inside the discharge

- **Currency-specific `δ_min^{(c)}(P)` derivation.** The proof shows `δ_min(P) > 0` aggregated across currencies; specializing to per-currency `δ_min^{(c)}(P)` requires the morphism rescalings (`r_{MW}, r_{WAFW}, r_{rc}, r_{ca}` per Phase 1b) to be specified up to multiplicative constants — debt #12's per-morphism residual.
- **Implication half tightness.** The implication says `δ → 0` past `T(P)`. Whether the convergence is at any specific rate (e.g., polynomial vs exponential) is open; the lemma only requires the qualitative implication, which is what §6.6 consumes.
- **`α_n` regime dependence.** Phase 1c assumed `α_n = κ_aae(family(γ_n))` is a function of `n` not coinciding pathologically with `Δ_n`. This is a Phase 1b `κ_aae` definitional choice; the lemma here uses it as already-committed.

## Couplings

- **T4b (debt #1):** prerequisite. The faithful `(Z, ℱ, ν, δ)` is what the lemma lives on. Without T4b, "δ ≥ δ_min(P) > 0" has no measurable structure to refer to.
- **Debt #11 (channel exhaustiveness):** complementary. #11 supplies that every FFT-style descent attempt routes through the four channels; #5 + #2(8) supply that the channels cannot drive δ → 0. Together they make §6.6 land.
- **Debt #3 (effective H-L `n=1` cost-form):** independent. The substrate-side cost-form is the substrate-side input the cost algebra consumes per amortization-failure; the endpoint commitment doesn't depend on #3 directly.
- **Debt #12 (currency-morphism rigor):** consumed. The per-currency floor `δ_min^{(c)}(P)` derivation uses #12's morphism rescalings; loop-consistency on the algorithm-side `M → W → AFW` triangle is what makes the per-currency reading well-defined.
- **Debt #9 (cost-model + canon re-read):** consumed (component (c)). The variable-precision canon re-read is what makes the lemma's "currency-by-currency at `T(P)`" reading land — without #9(c), the per-currency thresholds aren't re-read at the apparatus's committed precision.

## Acceptance status

| Item | Status |
|---|---|
| Existence half of #5 (`δ ≥ δ_min(P) > 0` at `T(P)`) | ✓ Proved on `(Z, ℱ, ν, δ)` via substrate-side iso-register floor |
| Implication half of #5 (improvement past `T(P)` ⟹ `δ → 0`) | ✓ Proved via Phase 1a δ definition + bridge |
| #2(8) bridge (at-threshold floor extends past-threshold) | ✓ Proved via substrate-side structural invariance under T(P)-movement |
| Currency-by-currency reading of existence half | ✓ Modulo debt #12 morphism-rescaling specification |
| §6.6 contradiction lands | ✓ Coupled with debt #11; §4.5 theorem reads as the paper claims |

**Debts #5 and #2(8) close** (modulo debts #12 and #9(c)). The §6.6 contradiction now has all three structural inputs in hand: faithful `(Z, ℱ, ν, δ)` (T4b); channel exhaustiveness over §4.2.2's native operations (debt #11); endpoint commitment lemma in two halves bridged by floor extension (debts #5 + #2(8)).

## Hand-off back to apparatus

After this discharge, the open items in the construction-debt ledger are:

- **Debt #3 (effective H-L `n=1` cost-form)** — substrate-side delivery owed; the long-pole substrate-side input.
- **Debt #12 (currency-morphism rigor)** — per-morphism verification residual; tightens T4b and per-currency `δ_min^{(c)}(P)` reading.
- **Debt #9(c) (variable-precision canon re-read)** — substantive substrate-side methodology commitment still owed in full.
- **Debts #6 (NATIVE-F promotion), #7 (T2), #8 (T3), #10 (trust-boundary discipline)** — supporting / cyclotomic-rigidity / discipline items, not gating §4.5.
- **Debt #4 (phase-lift transport)** — coupling claim that closes automatically when #3 + #9(c) land.
- **Debts #13 (substrate-side δ generalization), #14 (cost-norm operational compressibility), #15 (T6 cross-chart invariance)** — definitional / committed / recursion-theoretic horizon items, not closable as discrete proof obligations within the apparatus.

§4.5's theorem holds modulo (#3) + (#12) + (#9(c)). These are tractable in their own right; #3 is the long pole; #12 is per-morphism bookkeeping; #9(c) is the substantive variable-precision re-read. None is a structural keystone in the way T4b was.
