# T4B-DECOMPOSITION

Decomposition of construction-debt #1 (T4b — currency-universal limit object with `δ`-faithfulness) into three sequenced phase-debts. Project-management doc; not paper content. Pointer back from `paper/PROOF-CHAIN.md` §6 debt #1 entry; spec at [measure/THE-FIRST-BRIDGE.md](measure/THE-FIRST-BRIDGE.md); candidate `δ` machinery at [fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md).

## Recap

T4b is the currency-universal limit object: a measure space `(Z, ℱ, ν)` together with a `δ`-coordinate `δ : Z → ℝ_{≥0}` (the universal transaction cost), where `Z` is the limit over the three lower-bound currencies (Morgenstern bounded-additive, Winograd modular product, AFW cyclotomic-multiplicative) joined by the three substrate-side iso registers (rate, constant, almost-every) on equal footing. Faithfulness: three clauses — (i) `f₁, f₂, f₃` factor through `δ`; (ii) iso-register currency structure encoded measurably so cross-register conversion costs read on `δ`; (iii) closure-class membership reads measurably against `(Z, ℱ, ν, δ)`.

## Phase 1a — Formalize `δ`

Pin down the candidate cocycle realization as a precisely typed measurable function. The candidate is currently named — `δ` is the failure-to-agree of cocycle-product factors across butterfly refinements and primitive modes, measured pointwise per #14's operational compressibility commitment — but the type signature, domain, and σ-algebra are flagged as candidate machinery at §1.7. Phase 1a converts candidate-state to formal-state.

**Acceptance criteria.**
- (a) Definition: `δ_S(input)` as a finite combination of native-op cocycle factors, with explicit functional form.
- (b) Domain: precisely typed input space (FFT-style scheme `S` × input data `m` × precision `p`, per §1.7 / §6.5).
- (c) Codomain: `ℝ_{≥0}` with Borel σ-algebra.
- (d) Measurability proof against the input-space σ-algebra.
- (e) Compatibility check against §1.7's candidate description and §6.5's committed compressibility.

**Inputs.** Debt #14 (operational compressibility, committed). [fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md). [fft/COCYCLE-COMPOSITION-LAW.md](fft/COCYCLE-COMPOSITION-LAW.md).

**Outputs.** Formalization of `δ` as a measurable function on schemes' input data; pushed to `Z` in Phase 1b via the universal property.

**File target.** [measure/T4B-DELTA-FORMAL.md](measure/T4B-DELTA-FORMAL.md) — fresh file. PHASE-DEFECT.md stays as the exploratory ground; T4B-DELTA-FORMAL supersedes the candidate state with a typed measurable function.

**Status.** **Complete.** All five acceptance criteria met. FP arithmetic model committed to Matula 1970 significance spaces at `(β, n) = (2, p)` per [memos/FP-MATULA-1970.md](memos/FP-MATULA-1970.md); δ measurability proved via piecewise-constancy with finite breakpoint sets, anchored in Matula §II–§IV. Side benefit: Matula's commensurability dichotomy is the natural vocabulary for the option-3 discriminator that Phase 1c clause (iii) may need.

**Self-contained.** Doesn't require `Z` to exist yet.

## Phase 1b — Construct `Z`

Construct `Z` as a measurable-space limit over the diagram supplied by debt #12. The diagram has six nodes: three lower-bound currency-objects (Morgenstern bounded-additive, Winograd modular product, AFW cyclotomic-multiplicative) plus three iso-register objects (rate, constant, almost-every). Structure morphisms (debt #12): Morgenstern↔Winograd as bounded↔unbounded coefficient transfer; Winograd↔AFW as modular product → cyclotomic decomposition; iso-register transitions as the `5π`-overhead Sobolev → geometric chain.

**Acceptance criteria.**
- (a) Diagram explicitly listed: six objects + morphisms (each morphism a measurable map between cost-coordinate objects).
- (b) `Z` constructed as the limit (concrete construction via fiber product / pullback in the category of measurable spaces).
- (c) Universal property verified: for any other measurable space mapping coherently into all six nodes, a unique factoring through `Z`.
- (d) Pushforward measure `ν` on `Z`, induced from any single currency's measure (consistency requires the morphisms to be measure-preserving up to specified rescalings).
- (e) Compatibility with §6.3's prose description of `(Z, ℱ, ν)`.

**Inputs.** Debt #12 (interleaved per ledger — "logically prior; realistically close in tandem"). The six node objects.

**Outputs.** Concrete `(Z, ℱ, ν)` construction; universal-property proof; `ν` definition.

**File target.** [measure/T4B-Z-CONSTRUCTION.md](measure/T4B-Z-CONSTRUCTION.md) — the construction is novel enough to warrant its own file.

**Status.** **Complete (modulo debt #12).** All five acceptance criteria met. `Z` constructed as inverse limit of the 6-node diagram in the category of measurable spaces; `ν` defined as pushforward from any single currency's measure; `δ` committed to `max − min` functional form (spread of currency-specific cost readings). Per-morphism rigorous verification (measurability, rescaling factors, loop-consistency on the algorithm-side `M → W → AFW` triangle) remains open in debt #12; the construction is correct under those assumptions, matching the ledger's "interleaved with #12" closure pattern.

**Long pole.** This is the only phase that's genuinely new construction; Phase 1a and Phase 1c are bookkeeping over already-named or already-proved material.

## Phase 1c — Verify faithfulness clauses

Prove the three faithfulness clauses against Phase 1b's `(Z, ℱ, ν)` and Phase 1a's `δ`. Each clause is a separate proof; the three parallelize cleanly because each consumes a different witness.

**Acceptance criteria.**
- *(i) `f₁, f₂, f₃` factor through `δ`.* Construct measurable maps `π_i : Z → V_i` (where `V_i` is the codomain of `f_i`) such that `f_i = π_i ∘ ι` for `ι` the canonical inclusion of `L` into `Z` (via the substrate-side route). Theorem K (§5.6) supplies the σ-algebra coarsening; the factor-through map is the substrate-side encoding of the `f_i` into the `Z`-coordinate.
- *(ii) Iso-register currency structure encoded measurably.* Construct a measurable encoding of the `5π`-overhead Sobolev → geometric chain into `ν / δ`, so cross-register conversion costs (rate→constant, etc.) are measurable functions on `(Z, ℱ, ν, δ)`. Witness: [iso/THREE-REGISTER-SYNTHESIS.md](iso/THREE-REGISTER-SYNTHESIS.md) Claim 1.
- *(iii) Closure-class membership reads measurably.* Construct the indicator function `1_{C_FFT}` on `Z` and prove it's measurable. Witnesses: §5.5 admissibility envelope plus §4.2.1 regularity guard.

**Inputs.** Phase 1a's `δ`. Phase 1b's `(Z, ℱ, ν)`. Theorem K (proved). T1 (proved). `iso/THREE-REGISTER-SYNTHESIS.md` Claim 1 (proved). §5.5 + §4.2.1 (proved).

**Outputs.** Three measurability proofs.

**File target.** [measure/T4B-FAITHFULNESS.md](measure/T4B-FAITHFULNESS.md) — single file with the three clause proofs; sequential within the file (clause (i)'s substrate-side embedding is reused by clause (ii)).

**Status.** **Complete (modulo debt #12).** All three clauses verified. (i) `f₁, f₂, f₃` factor through `δ` via the substrate-side `L → N_rate → Z` embedding; recover map exploits `Δ_n`-injectivity on `ℕ_{≥3}`; Theorem K is the necessity-side witness ruling out the F-side route. (ii) Cross-register conversion costs and register-state labels constructed as measurable functions on `(Z, ℱ_Z)`; resolved `5π` overhead, categorial type-gap, and unresolved bridge/audit states encoded structurally without needing extended-real-line δ (the type-gap and open bridges are structural rather than pointwise-unbounded). (iii) `C_FFT ⊂ Z` is the countable image of a measurable scheme-set; indicator measurable.

**Parallelizable.** The three clauses parallelize across witnesses (Theorem K / 5π synthesis plus register-state ledger / §5.5 + §4.2.1) and use different portions of `Z`'s structure. Sequential writing was chosen because clause (i)'s substrate-side embedding is reused by clause (ii); single file at ~150 lines.

## Critical path

**Status:** All three phases complete (modulo debt #12).

- ✓ Phase 1a — `δ` formalized; Matula 1970 significance-space FP-model committed; measurability proved via piecewise-constancy with finite breakpoints. ([measure/T4B-DELTA-FORMAL.md](measure/T4B-DELTA-FORMAL.md), 132 lines.)
- ✓ Phase 1b — `Z` constructed as inverse limit of the 6-node diagram; `ν` defined as pushforward; `δ_Z := max_i κ_i − min_i κ_i`. ([measure/T4B-Z-CONSTRUCTION.md](measure/T4B-Z-CONSTRUCTION.md), 155 lines.)
- ✓ Phase 1c — three faithfulness clauses verified. ([measure/T4B-FAITHFULNESS.md](measure/T4B-FAITHFULNESS.md), ~150 lines.)

T4b (debt #1) closes structurally. Residual: debt #12's per-morphism rigorous verification (measurability, rescaling factors, loop consistency on the algorithm-side `M → W → AFW` triangle).

## Couplings

- **#12 (currency-morphism construction)** — consumed by Phase 1b. Closing in tandem per ledger; Phase 1b's diagram-listing step *is* #12's diagram inputs in their final form.
- **#14 (cost-norm operational compressibility)** — consumed by Phase 1a. Already committed; gates the formalization but doesn't block it.
- **#15 (T6 cross-chart invariance)** — absorbed by §Conclusion outflow as recursion-theoretic horizon. T4b commits to the cocycle coordinate; T6 lift is *not* part of T4b.
- **#9(b) (cross-currency `T(P)` reconciliation)** — substantially absorbed by closing T4b. `Z`'s universality *is* the reconciliation; closing #1 closes most of #9(b). Residual: per-entry currency check on the route-3 limit.
- **#5 (endpoint commitment)** — downstream of T4b. Once Phase 1c lands, the existence half of #5 has a faithful `(Z, ℱ, ν, δ)` to live on.
- **#2(8) (floor extension bridge)** — downstream of T4b + #5.
- **#11 (channel exhaustiveness)** — tightly coupled; T4b's three faithfulness clauses are what the four §6.6 channels map onto. Closing T4b stabilizes the clause statements; #11 is then the next priority (per `project_debt_11_priority.md` memory).
- **#3 (effective H-L `n = 1` cost-form)** — substrate-side delivery; doesn't gate T4b directly but feeds #4's coupling chain.

## Risks

- **Phase 1b reveals a needed structure morphism #12 didn't anticipate.** Phase boundary shifts; doc updated; not catastrophic.
- **Candidate cocycle `δ` doesn't naturally support iso-register encoding (clause ii).** The cocycle is FFT-arithmetic; the `5π` overhead is geometric. The link is the substrate-side `δ > 0` instance per §3.6.2 face (iv) — a manifestation of friction, not a coordinate identification. If Phase 1c clause (ii) fails to verify, we'd revisit the candidate. The route-3 commitment accepted this bet at debt #15's recursion-theoretic horizon absorption.
- **Phase 1a measurability proof requires input-space typing that conflicts with §6.5's committed cost-norm.** Unlikely (#14 was committed precisely to make this work) but possible if precision-dependence interacts badly with σ-algebra structure.
- **Phase 1c clause (i) factor-through map has unstated structural requirements.** Theorem K's σ-algebra coarsening has to translate to a `δ`-coordinate factor-through; the translation is the bridge clause (i) carries. If the bridge has hidden requirements, Phase 1c can't complete on K alone — Phase 1b's `Z` construction would need to expose the relevant structure.

## When to update this doc

- Phase boundaries shift (most likely from Phase 1b construction surprises): update the affected phase's acceptance criteria + downstream phase's inputs.
- New work-product files land: update file targets to point to actual files.
- A coupling closes (e.g., #14 was already committed; if #12 closes, update its row to "closed").
- Risks materialize: convert to "shifted phase" rather than risk; record the resolution.
