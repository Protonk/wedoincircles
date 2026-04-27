# LANDFALL-EXPORT

This file extracts three proof templates from Landfall (`sources/landfall.pdf`, Adam, 9-page proof-essay on the residual `ε(m) = log₂(1 + m) − m` of the affine pseudo-logarithm). Under the program's FFT-impossibility direction, Landfall is read as a proof-template *repository* rather than as a sibling paper for cross-side reference. Three obstructions are inherited as templates: §2's affine closure, §6's no-invariant-measure aggregation, §7's finite-closure refusal. Other Landfall content — polynomial wall, local corona failure, transcendence-at-dyadics — is on the page in the source paper and not extracted here.

**Division of labor with sister docs.** This file is the *source-side* inheritance map: what each Landfall template asserts and where it lands in FIRST-PROOF's debt list. The candidate concrete object that would realize Template 1's transport — the cocycle `{Δ_k}`, the **character reflection barrier**, **phase-lift conservativity** — lives in `fft/PHASE-DEFECT.md`; this file references it without duplicating its content. The full proof scaffold, debt numbering, and theorem-statement-conditional-on-debts structure live in `paper/FIRST-PROOF.md`; this file refers to debts by number without restating them. The methodological vocabulary (existence-vs-algebra of friction, `δ` as the irreducible-fee object, Coasean specialists) lives in `memos/COASE-FRICTION-AND-SPECIALISTS.md`; this file inherits it.

## Template 1: Affine closure (Landfall §2)

Native binade operations generate `Aff⁺(ℝ)`: additions translate, multiplications scale, composition stays in the two-parameter affine class. Landfall §2 proves that `λ(m) = log₂(1 + m)` is not in this closure; therefore no finite composition of native binade operations produces `λ`. Equivalently — since `m` is affine — the displacement `ε(m) = λ(m) − m` is not in `Aff⁺(ℝ)`-closure either.

This is the proof template the paper inherits for the conversion-cost obstruction. Generalization: native FFT operations (multiplications under FFT-style reduction, bounded-coefficient additions) generate a closure class `C_FFT`; descent past the canon's bounds requires moving outside `C_FFT`; no finite composition of native operations produces an outside-`C_FFT` cost map. This is the substrate of **FIRST-PROOF debt #3 (Template transfer)**: the concrete operation outside the FFT-side closure must be named, and the transport from `Aff⁺(ℝ)`-non-membership to `C_FFT`-non-membership must be earned.

The transport mechanism — and a candidate concrete object that carries it — is parked in `fft/PHASE-DEFECT.md`: the **character reflection barrier** asserts that `{Δ_k} ∈ C_FFT ⟹ ε ∈ C_Aff` at competitive cost, with **phase-lift conservativity** as its analytic-exponential specialization (the load-bearing sub-debt under FIRST-PROOF #2). Until that lemma is proved, Template 1 is sharpened (we know what `λ`/`ε` is on the source side and what `C_FFT` is on the target side) but not yet transferred. The transport is the FFT sequel's content, not Landfall's.

The algebraic-side companion is `memos/NATIVE-F-MINIMAL-DEFINITION.md`: no functor `F` preserves closure-depth from `Aff⁺(ℝ)` to `{K_n}`. Same template-structure, different closure class. The operational-side analog (a candidate forbid-search/forbid-cocycle argument as third structural sibling) is parked in `fft/FFT-SEARCH-PLAN.md`'s pencil marks.

Existence-vs-algebra reading per `memos/COASE-FRICTION-AND-SPECIALISTS.md`: Template 1 is the *existence* side of `δ` — friction > 0, finite composition does not zero it — which closes FIRST-PROOF Lemma B's existence claim once the transport lands. The *algebra* of `δ` (additivity, amortization, scale-behavior, representation-dependence, bypass-resistance) is debt #2 and is not in Landfall's scope.

## Template 2: No invariant measure for aggregation (Landfall §6)

Landfall §6 deploys the no-`PSL(2, ℝ)`-invariant-measure result on the binary tiling space — Bowen's source content is documented in `memos/BOWEN-DRILLING-AND-DENSITY.md` §1, with the citation form lifted from Landfall — to block equivariant aggregation of local information across the binary tiling. Local data exists; no invariant measure aggregates it consistently into a global correction.

For the program this is the structural antecedent for *representation-relocation* rebuttals: the candidate FFT-side strategy that says "move the defect to a new representation and amortize it cheaply there" must explain what consistent invariant aggregation across representations would look like. The pattern Landfall §6 supplies on the binary tiling is the pattern the FFT side has to reproduce on its own substrate (PHASE-DEFECT's additive-clock-vs-log-binade-clock seam, `A` vs `L`); the no-invariant-measure result is not transported by inheritance — it is the *shape* of the obstruction the FFT-side relocation argument has to assemble.

Where this lands: PHASE-DEFECT Layer 3's relocation-route obstruction, and the bypass-resistance sub-question under **FIRST-PROOF debt #2** (Coasean specialists: "reduce yes, eliminate no"). Template 2 asserts that representation-shopping is not a free escape; it does not by itself prove the FFT-side analogue. When a candidate aggregation attack presents in a binary-tiling-embeddable geometry, the **hole-drilling instability** strengthening (per `memos/BOWEN-DRILLING-AND-DENSITY.md` §2) is available as a tactical reach: not only is there no invariant measure on the would-be tiling, density on it is structurally unstable under arbitrarily small perturbations.

## Template 3: Finite closure refused (Landfall §7 — Gosper)

Landfall §7 observes that Gosper's continued-fraction arithmetic machine survives by refusing finite closure: state grows without bound, periodicity only on quadratic irrationals, Möbius operations cannot produce the logarithmic clock-change.

For the program Gosper is the negative anchor that calibrates the impossibility's scope. The impossibility does not say computation is impossible. It says: `δ` cannot be zeroed by finite composition of native operations. Gosper exists by giving up the finite composability the canon depends on — unbounded state is the price of zero `δ`. This calibrates **FIRST-PROOF Lemma B**'s reading: the no-finite-composition-zeros-`δ` claim is exactly what Gosper sidesteps by going non-finite, and the canon's claim of `O(N \log N)`-style FFT performance lives squarely on the finite-composition side of that line.

## Bottom line

Landfall closes finite structural routes for `ε` at the residual level on the binade side; the program closes finite-composition routes for `δ` at the conversion-cost level on the FFT side. The three templates supply the inheritance shape — affine closure (Template 1) for the headline non-membership, no-invariant-measure (Template 2) for the relocation rebuttal, finite-closure-refused (Template 3) for the scope calibration. The transport from `ε` to `δ` is the program's burden, not Landfall's; it lives in FIRST-PROOF debts #1, #3, #4, with PHASE-DEFECT carrying the candidate transport mechanism.

## Trust boundary

Templates are inherited *as templates*: arguments-of-shape, not arguments-of-content. Landfall proves things about `ε`; it does not prove things about `δ`, `{Δ_k}`, or `C_FFT`. None of the three templates above is an already-transported FFT theorem — each names a structural pattern the FFT-side argument must reproduce on its own substrate. The non-extracted Landfall content (polynomial wall, local corona failure, transcendence-at-dyadics) may become load-bearing in a later sequel; here it stays in the source paper. The export brief is repository plus inheritance map, nothing more.
