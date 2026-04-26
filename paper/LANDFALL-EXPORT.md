# LANDFALL-EXPORT

This file extracts three proof templates from Landfall (Adam, 9-page proof-essay on the residual `ε(m) = log₂(1 + m) − m` of the affine pseudo-logarithm). Under the program's FFT-impossibility direction, Landfall is read as a proof-template repository rather than as a sibling paper for cross-side reference. Three obstructions are inherited as templates: §2's affine closure, §6's no-invariant-measure aggregation, §7's finite-closure refusal. Other Landfall content — polynomial wall, local corona failure, transcendence-at-dyadics — is on the page in the source paper and not extracted here.

## Template 1: Affine closure (Landfall §2)

Native binade operations generate `Aff⁺(ℝ)`: additions translate, multiplications scale, composition stays in the two-parameter affine class. Landfall §2 proves that `lambda(m) = log₂(1 + m)` is not in this closure; therefore no finite composition of native binade operations produces `lambda`.

This is the proof template the paper inherits for the mult/add gradient destruction. The argument generalizes: native FFT operations (multiplications under FFT-style reduction; bounded-coefficient additions) generate a closed cost-map class; the descent past current FFT lower bounds is a cost-map outside that class; therefore no finite composition of native FFT operations yields the descent. The paper has to earn this generalization at the cost-manifold level — item (ii) on `paper/IMPOSSIBILITY-CHARTER.md`'s to-be-earned list.

The algebraic-side twin is `memos/NATIVE-F-MINIMAL-DEFINITION.md`: no functor `F` preserves closure-depth from `Aff⁺(ℝ)` to `{K_n}`. Same template-structure, different closure class.

## Template 2: No invariant measure for aggregation (Landfall §6)

Bowen 2002: the binary tiling space carries no `PSL(2, ℝ)`-invariant probability measure. Landfall §6 uses this to block equivariant aggregation of local information across the binary tiling — local data exists; no invariant measure aggregates it consistently into a global correction.

Under the FFT-impossibility framing this is the structural antecedent for the mult/add gradient destruction's anti-aggregation mechanism. The pattern: local information exists (cost values on the multiplicative submanifold; cost values on the additive submanifold) but no invariant measure on the cost manifold restricts consistently to both submanifolds. The prior instance is binary tilings via Bowen; the FFT cost manifold is a candidate second instance.

## Template 3: Finite closure refused (Landfall §7 — Gosper)

Landfall §7 observes that Gosper's continued-fraction arithmetic machine survives by refusing finite closure: state grows without bound, periodicity only on quadratic irrationals, Möbius operations cannot produce the logarithmic clock-change.

Under the FFT-impossibility framing Gosper is the negative anchor. The impossibility asserts that no FFT-style cost manifold has both finite closure and continuous descent across the mult/add boundary. Gosper is what survives if you give up finite closure: exact computation in unbounded state. The impossibility does not say computation is impossible; it says FFT-style closure-with-descent is.

## Bottom line

Landfall closes finite structural routes for `ε` at the residual level; the paper closes finite-closure-with-descent routes for FFT-style lower bounds at the cost-manifold level. The "imperfect mult/add conversion" mechanism is a refinement of Template 1's argument.
