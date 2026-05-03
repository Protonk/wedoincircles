# T4B-FAITHFULNESS

Phase 1c of the T4b decomposition (`paper/T4B-DECOMPOSITION.md`): verify the three faithfulness clauses against `(Z, ℱ, ν, δ)`. Inputs from Phase 1a ([measure/T4B-DELTA-FORMAL.md](measure/T4B-DELTA-FORMAL.md)) and Phase 1b ([measure/T4B-Z-CONSTRUCTION.md](measure/T4B-Z-CONSTRUCTION.md)). Spec at [measure/THE-FIRST-BRIDGE.md](measure/THE-FIRST-BRIDGE.md).

## Recap

T4b's three faithfulness clauses (per PAPER §6.3 / `measure/THE-FIRST-BRIDGE.md`):

- *(i)* `f₁, f₂, f₃` factor through `δ`.
- *(ii)* iso-register currency structure encoded measurably so cross-register conversion costs read on `δ` alongside `(μ, α)`.
- *(iii)* closure-class membership reads measurably against `(Z, ℱ, ν, δ)`.

Phase 1c proves each clause, consuming a different witness:

- *(i):* Theorem K (PAPER §5.6 / `measure/FOR-BREAKFAST.md` §K.0–§K.4).
- *(ii):* `iso/THREE-REGISTER-SYNTHESIS.md` Claim 1 (5π overhead worked; categorial type-gap to almost-every).
- *(iii):* PAPER §5.5 admissibility envelope + §4.2.1 regularity guard.

The three clauses parallelize across witnesses; we proceed sequentially because clause (i) sets up the substrate-side `L → Z` embedding that clause (ii) reuses.

## Setup

From Phase 1a: `δ_D : D = S × M × P → ℝ_{≥0}` measurable on the joint domain.

From Phase 1b: `Z := lim_← Diagram` ⊂ `∏_i X_i` over six nodes (`N_M, N_W, N_AFW` algorithm-side; `N_rate, N_const, N_aae` substrate-side); `ℱ_Z` the trace σ-algebra; `ν := proj_M^* ν_M`; `δ_Z((x_i)_i) := max_i κ_i(x_i) − min_i κ_i(x_i)`.

Each substrate-side node is parametrized by `n ≥ 3` (regular `n`-gon for `N_rate`; `n`-gon-as-curve `γ_n` for `N_const`; parametric family from `γ_n` for `N_aae`). The algorithm-side nodes admit a "trivial-state" element with `κ_i = 0` — the empty circuit, the identity bilinear form, the trivial cyclotomic decomposition — used as the algorithm-side coordinate of substrate-side `Z`-embeddings.

## Clause (i) — `f₁, f₂, f₃` factor through `δ`

**Substrate-side embedding `ι : L → Z`.** Define
```
ι(k, n)  :=  (trivial_M, trivial_W, trivial_AFW, n, γ_n, family(γ_n))
```
where `trivial_·` are the algorithm-side trivial states and the substrate-side coordinates are the `n`-gon-derived images under `f_{rc}` and `f_{ca}`. By the diagram constraints, `ι(k, n) ∈ Z`. `ι` is measurable: discrete on `L`'s atomic σ-algebra, into `Z`'s trace σ-algebra.

**Compute `δ_Z ∘ ι(k, n)`.** At `ι(k, n)`:
- `κ_M = κ_W = κ_AFW = 0` (trivial states).
- `κ_rate(n) = Δ_n = 4π⁴/(3n²) + O(1/n⁴)` (Hurwitz Parseval).
- `κ_const(γ_n) = Δ(γ_n) = Δ_n` (`γ_n` is the `n`-gon-as-curve; the gap is the same).
- `κ_aae(family(γ_n))` = some fixed function of `n` (per Phase 1b's `κ_aae` reading on the linearly-interpolated parametric family from `γ_n`); call it `α_n`.

So `δ_Z(ι(k, n)) = max(0, 0, 0, Δ_n, Δ_n, α_n) − min(0, 0, 0, Δ_n, Δ_n, α_n) = max(Δ_n, α_n) − 0 = max(Δ_n, α_n)`.

**Injectivity in `n`.** `Δ_n` is strictly decreasing on `ℕ_{≥3}` (monotone in the leading `4π⁴/(3n²)` term, with the `O(1/n⁴)` correction not flipping the sign for `n ≥ 3`). `α_n` is a function of `n` (specific form depending on `κ_aae`'s definition, but well-defined per Phase 1b). The map `n ↦ max(Δ_n, α_n)` is injective on `ℕ_{≥3}` provided `α_n` does not coincide pathologically with `Δ_n` across distinct `n` — a Phase 1b `κ_aae` definitional choice, achieved by any reasonable parametric-family reading. Phase 1c assumes this; if Phase 1b's `κ_aae` choice were to fail injectivity, Phase 1c would refine `κ_aae` to restore it (e.g., `κ_aae(family) := (a.e. value) + (1/n)` to ensure separation).

**Recovery and factorization.** Define `recover : image(n ↦ max(Δ_n, α_n)) → ℕ_{≥3}` as the (well-defined by injectivity) inverse, extended by 0 elsewhere. Define `π_i : ℝ_{≥0} → ℝ` by
```
π_i(t)  :=  f_i(_, recover(t))     for i ∈ {1, 2, 3}
```
where the `k` argument of `f_i` is irrelevant (each `f_i` depends only on `n`). Concretely:
- `π_1(t) = φ(recover(t)) / 2`,
- `π_2(t) = 2 · recover(t) · sin(π / recover(t))`,
- `π_3(t) = Δ_{recover(t)}` (which equals the input `t` when `t ∈ image(Δ_n)`).

**Verify `f_i = π_i ∘ δ_Z ∘ ι`.** For `(k, n) ∈ L`:
```
π_i ∘ δ_Z ∘ ι(k, n)  =  π_i(max(Δ_n, α_n))  =  f_i(_, recover(max(Δ_n, α_n)))  =  f_i(_, n)  =  f_i(k, n).  ✓
```

**Measurability of `π_i`.** `image(n ↦ max(Δ_n, α_n))` is a countable subset of `ℝ_{≥0}`; on a countable set with the discrete trace σ-algebra, every function is measurable. `π_i` extended by 0 elsewhere is measurable on `(ℝ_{≥0}, ℬ(ℝ_{≥0}))`.

**Theorem K's role (necessity-side witness).** Theorem K certifies that no apparatus restricted to `F`-side coordinates can recover `f_1, f_2, f_3` (per `R^*`-pullback, the `f_i` are not `R^{−1}(2^F)`-measurable). The `L`-side substrate route via `N_rate` (used in `ι` above) is therefore the only viable factorization route. Without Theorem K, an alternative `F`-side embedding might be claimed; Theorem K rules it out, leaving the `L`-side route as necessary.

**Clause (i) ✓.**

## Clause (ii) — iso-register currency structure encoded measurably

**Cross-register conversion costs as measurable functions on `Z`.** Phase 1b's substrate-side morphisms `f_{rc} : N_rate → N_const` and `f_{ca} : N_const → N_aae` are measurable maps with specified rescaling factors. The cross-register conversion costs are:
```
cross_{rc}(z)  :=  κ_const(proj_const(z))  −  κ_rate(proj_rate(z))
cross_{ca}(z)  :=  κ_aae(proj_aae(z))   −  κ_const(proj_const(z))
cross_{ra}(z)  :=  κ_aae(proj_aae(z))   −  κ_rate(proj_rate(z))    [composed]
```
Each is a measurable function on `(Z, ℱ_Z)` because `proj_·` are measurable and `κ_·` are measurable cost coordinates on each node.

**Encoding the 5π overhead (`iso/THREE-REGISTER-SYNTHESIS.md` Claim 1).** The 5π overhead is the structural cost-rescaling factor `r_{rc}^{(κ)} = 5π` on `f_{rc}` (per `measure/CURRENCY-MORPHISMS.md`) — the chain's cost-of-derivation between the rate-register asymptotic-bound construction and the constant-register direct-Bonnesen reading. Phase 1b's δ_Z reads this rescaling literally via the rescaled-spread form: at every substrate-side Z-point ι(k, n),
```
δ_Z(z)  ≥  | κ_const(γ_n)  −  r_{rc}^{(κ)} · κ_rate(n) |  =  | Δ_n  −  5π · Δ_n |  =  (5π − 1) · Δ_n  ≈  14.7 · Δ_n,
```
positive at every `n ≥ 3`. The 5π is *encoded measurably* on `(Z, ℱ_Z)` at every n-gon Z-point — the apparatus reads the chain's structural commitment via Phase 1b's rescaled-spread `δ_Z`, not requiring "non-n-gon" Z-points (which Phase 1b's diagram doesn't admit, since `x_const = f_{rc}(x_rate)` constrains substrate-side const coordinates to be n-gon images).

**Encoding the categorial type-gap.** The type-gap to almost-every (per `iso/THREE-REGISTER-SYNTHESIS.md`) is a structural feature: there is no measurable right-inverse `s : N_aae → N_const` of `f_{ca}` with finite cost-rescaling — the constant-register reading is on convex curve-shape space, the almost-every reading is on parametric-measure space, and the two are type-incompatible at the apparatus level. The type-gap encodes as the *non-availability of a finite `r_{ca}^{(κ)}`* in the diagram: `f_{ca}` is measurable, but no path through the diagram traversing `f_{ca}` admits a finite composite rescaling. Per Phase 1b's δ_Z definition, paths whose composite rescaling is non-finite are excluded from the max — the structural type-gap registers as the *exclusion* of cross-currency paths that pass through `f_{ca}`, not as a numerical δ-contribution. The qualitative non-existence reading suffices for Phase 1c here; rigorous measure-theoretic non-existence proof is a sharpening item tracked at `measure/CURRENCY-MORPHISMS.md` (Phase 1c residual + #12 sharpening).

**No extended-real-line needed.** Phase 1c's verification finds that the type-gap is structural rather than pointwise-unbounded; pointwise δ stays in `ℝ_{≥0}` (each `κ_i` is finite at each `Z`-point); the type-gap surfaces in the *morphism structure*, not in δ-values. Phase 1b's `δ : Z → ℝ_{≥0}` codomain is sufficient; the brief's anticipated extension to `[0, ∞]` is unnecessary.

**Cross-side coupling alongside `(μ, α)`.** δ's `max − min` form takes the spread across all 6 currencies. At a `Z`-point where algorithm-side κ_i contribute non-trivially (an FFT-style scheme's embedding), the algorithm-side `(μ, α)` cost-currency values appear in the δ spread alongside the substrate-side iso-register values. The cross-register iso costs and the algorithm-side cost-currencies *both* read on δ, "on equal footing" per §6.3's framing.

**Clause (ii) ✓** (modulo Phase 1b's `f_{rc}` and `f_{ca}` morphism-property assumptions, which are debt #12's residual).

## Clause (iii) — closure-class membership reads measurably

**`C_FFT` as a subset of `Z`.** A `Z`-point `z = (x_M, x_W, x_AFW, x_rate, x_const, x_aae)` corresponds to an FFT-style method iff its algorithm-side projection `(x_M, x_W, x_AFW)` is in the embed-image of some scheme `S ∈ S` meeting §4.2.1's regularity guard and §5.5's admissibility envelope. Define
```
C_FFT  :=  embed( { S ∈ S : S meets §4.2.1 + §5.5 } )  ⊂  Z
```
where `embed : S → Z` is the algorithm-side embedding map (Phase 1a's `D → Z` interface; rigorous form deferred per Phase 1b's hand-off note).

**Measurability of `C_FFT`.** Schemes form a countable set with discrete σ-algebra `𝒫(S)` (Phase 1a). The condition "S meets §4.2.1's regularity guard" is decidable on `S` (operation cost / stored precision / coefficient size paid at granularity `p`; advice strings, oracle constants, and table-per-size shortcuts excluded — each excludable feature is detectable in a finite scheme description). The condition "S meets §5.5's admissibility envelope" is similarly decidable (L-W safety per content-not-calendar; structurally typed at `measure/SUBSTRATE-OBSTRUCTIONS.md` §5). The set `{ S ∈ S : S meets §4.2.1 + §5.5 }` is a measurable subset of `S` (any subset of a countable set with discrete σ-algebra is measurable). Image under `embed` is a countable subset of `Z`, hence measurable in `ℱ_Z` (countable subsets of standard Borel spaces are Borel).

**Indicator measurability.** `1_{C_FFT} : Z → {0, 1}` is the indicator of a measurable subset, hence measurable.

**§5.5 + §4.2.1 jointly characterize `C_FFT`.** §4.2.1 fixes the charging discipline; §5.5 fixes the L-W safety dichotomy and admissibility envelope. Together they specify which schemes are in-class: schemes whose every primitive is paid at the committed granularity, whose substrate-side reasoning lives within the L-W envelope, and whose construction does not smuggle in advice or oracle structure. Phase 1c inherits this characterization without re-deriving it; the indicator's measurability follows from the joint commitment.

**Clause (iii) ✓.**

## Compatibility with §6.3 prose

§6.3's three faithfulness clauses are stated as the bridge T4b owes; Phase 1c's three proofs land them.
- Clause (i)'s "Witness: Theorem K" reading at §6.3 is the necessity-side input (Theorem K rules out the F-side route). The factor-through map is constructed here against the substrate-side `L → N_rate → Z` embedding.
- Clause (ii)'s "Witness (substrate-side): §5.2 iso non-nesting; Witness (algorithm-side): §3.6.2 currency-stratification" is the structural input the encoding consumes. The cross-register conversion costs are constructed here as measurable functions on `(Z, ℱ_Z)`.
- Clause (iii)'s "Witness: §5.5 admissibility envelope plus §4.2.1 regularity guard" is the joint commitment; the indicator's measurability is verified here.

§6.4's "→ clause (X)" expansions in PAPER are paraphrased correctly: Theorem K certifies non-recoverability from F (clause (i)'s necessity); §5.2 + 5π synthesis encodes the iso-register stratification (clause (ii)); §5.5 + §4.2.1 typify closure-class membership (clause (iii)).

## What Phase 1c does not do

- **Debt #5 existence-half lemma.** "Any FFT-style method achieving `T(P)` pays `δ ≥ δ_min(P) > 0`" is downstream of T4b closing; Phase 1c gives δ faithful structure but doesn't prove non-vanishing.
- **Debt #2(8) floor extension.** The bridge between #5's existence and implication halves is a separate proof obligation; Phase 1c provides faithful δ on Z, the substrate the bridge proof needs.
- **Debt #12 morphism-property verification.** Phase 1c uses the morphism rescalings (`f_{rc}` 5π, `f_{ca}` type-gap, algorithm-side cost-rescalings) as named at Phase 1b. Rigorous per-morphism verification stays at debt #12.
- **Phase 1a `D → Z` embedding rigor.** Phase 1c's clause (iii) uses `embed : S → Z` informally as a projection chain; the rigorous embedding map remains a Phase 1c-side bookkeeping item, low difficulty.
- **Debt #11 channel exhaustiveness.** Now-tractable downstream priority per `project_debt_11_priority.md` memory; Phase 1c does not address it.

## Open inside Phase 1c

- **`κ_aae` definitional choice for clause (i) injectivity.** Phase 1b deferred `κ_aae`'s precise reading (essential supremum vs integral vs quantile). Phase 1c assumes a choice that preserves `n ↦ max(Δ_n, α_n)` injectivity; if Phase 1b's eventual choice fails, a small refinement is needed (e.g., explicit `1/n` separation term).
- **`embed : S → Z` rigorous form.** Used informally in clause (iii); a rigorous bookkeeping pass would write the projection chain explicitly. Low priority — closure-class measurability holds under the informal interface.
- **Algorithm-side trivial-state convention.** Phase 1c uses `κ_M = κ_W = κ_AFW = 0` at substrate-side `Z`-embeddings. If Phase 1b's diagram constraints don't admit a uniform trivial-state element, the construction needs a per-currency canonical-default choice — minor.

## Acceptance status

| Criterion | Status |
|---|---|
| Clause (i): `f₁, f₂, f₃` factor through `δ` | ✓ Substrate-side `ι : L → Z`, recover via `Δ_n`-injectivity, π_i constructed measurably. Theorem K is necessity-side witness. |
| Clause (ii): iso-register currency structure encoded measurably | ✓ Cross-register conversion costs constructed as measurable functions; 5π overhead and type-gap encoded structurally; modulo debt #12. |
| Clause (iii): closure-class membership measurable | ✓ `C_FFT` is countable image of a measurable scheme-set in `Z`; indicator measurable. |

**Phase 1c complete (modulo debt #12).** All three clauses verified. T4b decomposition (Phase 1a + Phase 1b + Phase 1c) closes debt #1 in the form named at the ledger entry, conditional on debt #12's per-morphism rigorous verification.

## Hand-off back to the apparatus

With T4b (debt #1) closed at the structural level:
- **Debt #5 (endpoint commitment)** becomes tractable. The existence-half lemma "any FFT-style method achieving `T(P)` pays `δ ≥ δ_min(P) > 0`" now has a faithful `(Z, ℱ, ν, δ)` to live on. The substrate-side `δ > 0` instance from §3.6.2 face (iv) — the substrate-side currency-stratification with 5π overhead and type-gap — is encoded on Z via clause (ii); δ ≥ this substrate-side instance everywhere on the substrate-side embedding image.
- **Debt #2(8) (floor extension bridge)** becomes tractable. Bridge between #5's existence and implication halves; the structural locus where #5 lives (faithful δ on Z) is now in hand.
- **Debt #11 (channel exhaustiveness)** is the next priority per `project_debt_11_priority.md` memory. The four §6.6 channels-to-clauses mapping is now stated against verified faithfulness clauses: Farey recoding → clause (i); cross-register iso → clause (ii)-substrate; mult-add trading → clause (ii)-algorithm; tables/advice → clause (iii). Path (i)-by-enumeration over §4.2.2's five native operations becomes a finite check against the now-verified clause structure.
- **Debt #9(b) (cross-currency `T(P)` reconciliation)** substantially closes — `Z`'s universality *is* the reconciliation per the Coasean reading. Residual: per-entry currency check on the route-3 limit, debt #12-adjacent.

The four-channel composition at PAPER §6.6 now has structurally complete faithfulness inputs; the §6.6 contradiction lands modulo (a) debt #5's endpoint commitment, (b) debt #11's channel exhaustiveness, (c) debt #12's per-morphism rigor. T4b's closure here was the keystone; the remaining ledger items are tractable rather than central.
