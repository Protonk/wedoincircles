# PHASE-DEFECT

Parking lot for the phase-defect cocycle `Δ_k(m) = χ_k(ε(m))` (and its analytic realization `D_k(m) = e^{2πikε(m)}`) as a candidate concrete realization of `δ`. Not yet load-bearing in the paper; held here until the gating debts (coordinate-cut alignment; L-W audit) resolve, "competitive compression" is given a precise cost meaning, and the sub-debts (formal-character composition, closure-class transport, phase-lift conservativity, canon-bound translation) close. If those checks succeed, this formulation could reduce debts #1, #3, and #4 of FIRST-PROOF at once and give the proof concrete pre-π content. Companion to `fft/FFT-SEARCH-PLAN.md`: search-plan parks the strategy-family interpretation; phase-defect parks the candidate object the strategies operate on.

Candidate theorem name: **No Free Descent** — any FFT-competitive descent past `T(P)` must carry the defect cocycle, and the cocycle is forced by the quotient-clock displacement, not by representation choice.

## Pre-π setup: two quotient clocks

The two coordinate systems are quotient groups, defined without `π`:

```text
Additive clock:    A := ℝ/ℤ.
Log-binade clock:  L := ℝ_{>0}/2^ℤ  (equivalently, log₂ phase mod 1).
```

The mantissa-to-log coordinate has a canonical lift

```text
ψ₀(m) = log₂(1 + m) ∈ [0, 1),   m ∈ [0, 1),
```

whose class modulo `1` is the log-binade clock coordinate `ψ(m)`. The
defect is the lifted displacement

```text
ε(m) = ψ₀(m) − m.
```

This is the displacement between the additive mantissa coordinate and the multiplicative/log-binade coordinate. No `π`. No complex exponential. No chosen analytic unit-circle realization. The obstruction is born at the quotient-clock level — the same object Landfall §2 already studies as the gap between the affine pseudo-log and the true logarithmic coordinate. `π` may return later as one analytic realization of the formal characters introduced below; it is not load-bearing in the obstruction itself.

## The forced identity (cocycle form)

Characters of `A = ℝ/ℤ` are indexed by `ℤ`. Treat the codomain `𝕋` here as the formal character torus, not yet as a chosen complex-exponential realization: a character `χ_k : A → 𝕋` satisfies

```text
χ_k(t + s) = χ_k(t) · χ_k(s).
```

Pulling characters through the lifted coordinate `ψ₀` and then reducing modulo `1`:

```text
χ_k(ψ₀(m)) = χ_k(m + ε(m)) = χ_k(m) · χ_k(ε(m)).
```

The residual factor

```text
Δ_k(m) := χ_k(ε(m))
```

is the **defect cocycle**: the multiplicative residual any character pullback through `ψ` must carry. The family `{Δ_k}_{k ∈ ℤ}` parametrizes the defect mode-by-mode. In any model that really identifies the coordinate change `m ↦ ψ(m)` with the paper's mult/add conversion, `{Δ_k}` is the residual cocycle the conversion must carry; it is not metaphor.

The exponential `D_k(m) = e^{2πikε(m)}` is the analytic specialization of `Δ_k` under `χ_k(t) = e^{2πikt}`. It is one realization. The obstruction lives at the cocycle level, before that analytic realization — which is the move that decouples the proof from `π` while keeping the analytic specialization available when needed.

## Three-layer proof architecture

If the gates and sub-debts resolve, the proof acquires a three-layer spine:

**Layer 1 — Quotient-clock obstruction.** Define `A`, `L`, `ψ`, `ε` as above. The obstruction is the displacement between additive and log-binade coordinates. Pre-`π`; pre-analytic. (Maps to outline §1.)

**Layer 2 — Character-pullback cocycle.** Introduce formal characters `χ_k`. Derive `Δ_k(m) = χ_k(ε(m))` as the residual cocycle of any character pullback through `ψ`. (Maps to outline §3 / §4.)

**Layer 3 — No-free-escape theorem.** Any FFT-competitive method that descends past `T(P)` must either compress the cocycle family `{Δ_k}` competitively under FFT-style composition (forbidden if the character reflection barrier is proved), flatten `ε` directly (forbidden by Landfall §2 on the binade side), or relocate the defect to a new representation (in which case it must explain what happens to the pullback cocycle in that representation; Landfall §6 supplies the template for an anti-aggregation/relocation obstruction, not an already-transported FFT theorem). (Maps to outline §5 / §6.)

## What this would buy

`δ` becomes a concrete object: *the cost of compressing `{Δ_k}` under FFT-style composition*. The Bridge Theorem becomes:

> Any FFT-style method that descends past `T(P)` requires the defect cocycle family `{Δ_k}` to be competitively compressible under the canon's standard composability.

"Competitively compressible" needs precise definition before this can touch FIRST-PROOF. The leading candidate is **operational**:

> The scheme produces a defect-free FFT-style composition law whose character products agree across all butterfly refinements and primitive modes.

The operational form is testable on a candidate scheme, does not pre-suppose representational machinery on either side, and avoids the begging-the-question risk in vaguer "competitively compressible" formulations. With this definition in place, `{Δ_k}` is no longer a suggestive object; it carries a first-pass cost question: *does a given FFT-style scheme produce a defect-free composition law whose character products agree across butterflies?*

Three secondary candidate definitions remain available as sharper analytic tests, each importing additional structure the operational form does not require:

- low-rank approximation under formal-character decomposition;
- `O(N log N)` evaluation on `N` samples without paying the residual-coordinate cost;
- factorization as a finite product of simpler cocycle factors closed under the canon's operations.

The right *full* form is an internal sub-debt. The operational form is what the proof can run on first; the secondary forms are sharpening targets if the operational version turns out to need analytic backing.

## Debts this would close (favorably)

**Debt #1 (Bridge Theorem).** Becomes: descent past `T(P)` ↔ `{Δ_k}` competitive compressibility at the boundary. The forced identity identifies the residual cocycle a bridge would have to compress; it does not by itself prove the bridge equivalence. That equivalence remains the central theorem, now with a concrete cocycle target.

**Debt #3 (Template transfer).** Landfall §2 establishes `λ(m) = log₂(1+m) ∉ Aff⁺(ℝ)`-closure; since `m` is affine, `ε = λ − m` is the equivalent non-affine defect on the binade side. The transfer to FFT-style composability would assert `{Δ_k} ∉` FFT-style-composability closure. The concrete operation outside the source closure is `λ`/`ε`; the extra work is the **character-pullback transport** — proving the formal-character lift preserves the relevant non-membership in the FFT-side closure. Until that lift is proved, the template is sharpened but not yet transferred.

**Debt #4 (Lemma B closure-class calculation).** Becomes Fourier-analytic at the cocycle level: which `{Δ_k}` families are reachable by FFT-style composition? Landfall §2 answers the binade-side question for `λ`/`ε`; the FFT-side question narrows to whether `{Δ_k}` inherits that non-membership through the character-pullback lift. A targeted transport calculation, not a blank closure-class search.

## Character reflection barrier (named transport lemma)

The transport from Landfall §2's `λ ∉ Aff⁺(ℝ)` obstruction — equivalently the non-affine residual `ε = λ - m`, since `m` is affine — to `{Δ_k} ∉ C_FFT` requires a bridge lemma: call it the **character reflection barrier**.

> If the FFT-style composition closure `C_FFT` contains the cocycle family `{Δ_k(m) := χ_k(ε(m))}`, then the underlying additive defect `ε(m)` lies in the affine closure `C_Aff`.

The contrapositive composes with the Landfall §2 obstruction after that `λ`/`ε` equivalence: `ε ∉ C_Aff` ⟹ `{Δ_k} ∉ C_FFT`. This is the transport we need.

The lemma's hypothesis decomposes into three parts:

1. **Faithfulness on the defect range.** The map `t ↦ (χ_k(t))_k` separates points on `ε(m) ∈ [0, ε_max ≈ 0.0861]`. For `χ_1(t) = e^{2πit}`, faithfulness holds: the small-branch argument `ε(m) = (1/2π) Arg Δ_1(m)` is well-defined and gives pointwise recovery.
2. **Log-liftability on the defect image.** If FFT-style composition produces `{χ_k(f(m))}_k`, the lifted function `f(m)` must be recoverable as an additive-coordinate object. Pointwise recovery is easy on a small branch; competitive-cost recovery is not. The strong form says phase facts cannot be cheaper than coordinate facts.
3. **Closure compatibility (load-bearing).** The lifting operation must send FFT-style compositions back into `C_Aff` at competitive cost — the "no cheaper-than-affine logarithmic lift" condition. Without it, the character system can encode `ε` injectively while making it cheap in the multiplicative representation.

Faithfulness is mild. Log-liftability is cost-sensitive. Closure compatibility is the substantive hypothesis. For the analytic exponential `χ_k(t) = e^{2πikt}`, closure compatibility specializes to **phase-lift conservativity**: any FFT-style composition closure containing `{Δ_k}` must, after branch-unwrapping on `[0, ε_max]`, contain `ε(m)` in `C_Aff` at competitive cost.

**Pointwise recovery is not closure-reflection.** `ε(m) = (1/2π) Arg Δ_1(m)` recovers `ε` pointwise via the small-branch argument; the obstruction is whether the arg-lift stays within the allowed computational closure at competitive cost. Pointwise recovery is automatic on the small defect interval; closure-class recovery is the bridge theorem the FFT sequel must earn.

**Phase-lift conservativity is not derivable from Landfall alone.** §2 gives source non-affineness for `ψ`; §4 gives transcendence-at-dyadics for `ε`, blocking exact algebraic repair routes. Neither implies that constructing `{Δ_k}` competitively forces constructing `ε` competitively — exponentiation can hide arithmetic information at the closure level. Phase-lift conservativity is the new content the sequel produces.

**Closure-class regularity guard.** All three parts of the decomposition presuppose that `C_FFT` and `C_Aff` are *uniform, non-growing* closure classes over a fixed base field, with oracle constants, advice-bearing primitives, and growing-state schemes excluded *by definition* rather than refuted by separate argument. Without this guard, the "cheaper-than-affine logarithmic lift" can be smuggled in through advice or non-uniformity — defeating the lemma at the closure-class definition rather than at its hypothesis. The guard reads on the closure-class definition: "the scheme is uniform and non-growing." Bypass-resistance against advice and oracle constants is therefore not a separate sub-claim of the lemma; it is a *guard on the closure-class definition* the lemma applies to. Bypass-resistance against amortization and per-instance specialization remains a substantive sub-claim and lives in FIRST-PROOF debt #2's algebra.

**Excluded patterns under the regularity guard.** The schemes the guard excludes by hypothesis-class definition include:

- Bailey four-step style precomputation when it functions as advice;
- mixed-radix schemes with input-dependent radix selection;
- cache-oblivious or growing-state schemes when the state growth is doing the bridge work;
- any scheme whose constants or representation choices grow with the instance in a way not charged by the model.

This is *scope control*, not victory. The excluded schemes become research targets outside the theorem's present hypothesis class — not counterexamples to it.

## Gating debt 1: coordinate-cut alignment

**The question.** Does the additive-vs-log-binade quotient-clock cut align with the FFT canon's mult/add complexity cut?

**Strengthened argument under the cocycle reframe.** The quotient-clock cut (`A` vs `L`) is **group-theoretic**, not Fourier-register-specific. The mult/add complexity cut is also structural (multiplicative complexity `μ` on circuit operations vs additive complexity `α`). The two cuts may align at the structural group level: cyclotomic DFTs are Fourier transforms on finite abelian groups, with roots of unity as multiplicative character values; their arithmetic-circuit complexity decomposes by how mult and add operations interact with that character structure. This alignment claim is cleaner than "Fourier-character cut matches arithmetic-circuit complexity cut" because it lives at the group/character level, not at the analytic-realization level.

**Counter-considerations.** Morgenstern's bounded-coefficient additive bound doesn't fit cyclotomic factor structure cleanly; arithmetic-circuit complexity is coarser than Fourier-character structure. Need to verify each canon source's bound translates to a cocycle-side claim, or accept that the theorem scope narrows to those that do.

**Resolution path.** Read each canon source under the additive/log-binade quotient-clock lens; check whether each bound becomes a `{Δ_k}`-side compressibility claim or a boundary condition around such a claim. No majority vote: any source that refuses the lens narrows the theorem scope or gets a different role.

**Canon verdicts (all four).** All four canon sources audited under the lens land at **(b) Conditional translation, out-of-scope**, by structurally distinct paths terminating at the same boundary (no floating-point binade structure at primitive-operation level).

- **Schönhage-Strassen 1971** ([fft/SCHOENHAGE-STRASSEN-COCYCLE-TRANSLATION.md](fft/SCHOENHAGE-STRASSEN-COCYCLE-TRANSLATION.md)). Method 1 (over ℂ) uses fixed-point arithmetic with precomputed `e^{2πi · 2^{-n}}` quantizations — no per-number binade, no `ε`. Method 2 (over `ℤ_{F_n}`) uses the Fermat ring with cyclic-shift twiddles — pure modular arithmetic, no mantissa coordinate.
- **Morgenstern 1973** ([fft/MORGENSTERN-1973-COCYCLE-TRANSLATION.md](fft/MORGENSTERN-1973-COCYCLE-TRANSLATION.md)). Bounded-coefficient linear `ℂ`-circuit model; primitive operation is the binary linear combination `h = λf + μg` over exact `ℂ`; no per-number binade, no `ε`. Structurally parallel to SS Method 1; reached by determinant-growth control rather than fixed-point quantization.
- **Winograd 1978** ([fft/WINOGRAD-1978-COCYCLE-TRANSLATION.md](fft/WINOGRAD-1978-COCYCLE-TRANSLATION.md)). Bilinear / CRT-decomposition model over a chosen field with fixed-field scalars free; algebraic / arithmetic-circuit primitives, no mantissa coordinate. Structurally parallel to SS Method 2; reached by CRT factorization plus the modular-product theorem.
- **Auslander-Feig-Winograd 1984** ([fft/AUSLANDER-FEIG-WINOGRAD-1984-COCYCLE-TRANSLATION.md](fft/AUSLANDER-FEIG-WINOGRAD-1984-COCYCLE-TRANSLATION.md)). Semilinear `ℂ` model under rational equivalence; rational-equivalence quotient is an extra coarsening layer beyond Winograd's field-extension move. Same boundary; the coarseness is methodologically informative for the cocycle's representation-independence story (per [measure/ALGEBRA-OF-DELTA.md](measure/ALGEBRA-OF-DELTA.md) §6).

The theorem scope narrows in a principled way: **in-scope iff the algorithm crosses the floating-point binade seam at its primitive-operation level**. This is *seam-orthogonal* scope-narrowing, distinct from the regularity-guard exclusion of advice-bearing / non-uniform / growing-state schemes.

The four canon bounds (SS upper, Morgenstern's `Ω(n log n)` additive floor, Winograd's `μ(T_P) = 2n − k` modular-product, AFW's `p(F(G))` rational-equivalence ledger) enter the program as `T(P)`-side imports, not as cocycle-compressibility claims; the cocycle obstruction is *additional* content the program supplies at the seam the canon does not cross.

## Gating debt 2: L-W audit on cocycle non-compressibility

The pre-`π` setup means the obstruction itself is born before transcendence machinery enters: quotient-clock displacement and formal characters are pre-Lindemann. The audit narrows — but does not vanish.

**The question.** Does the *translation step* — from formal-cocycle non-compressibility to the canon's concrete (analytic-realization) bounds — import transcendence essentially, *and* does the closure-reflection step (the character reflection barrier above) import any post-1882 content beyond what Landfall already supplies?

**Why neither §2 nor §4 alone resolves it.** §2 gives source non-affineness for `ψ` and equivalent non-affineness for `ε` on the binade side; this is the obstruction the cocycle inherits at the formal-character level. §4 gives transcendence-at-dyadics for `ε`, blocking exact algebraic repair routes. Neither implies that constructing the cocycle family `{Δ_k}` competitively forces constructing `ε` competitively in `C_Aff`. Exponentiation can in principle hide arithmetic information at the closure level — the very content the **phase-lift conservativity** specialization of the character reflection barrier asserts is unavailable. That non-hiding claim is the new content the sequel must produce; it is not a corollary of Landfall §2 ∪ §4.

**Plausible argument for clean audit at the formal-cocycle layer.** The formal-cocycle obstruction inherits Landfall §2's affine-closure obstruction (pre-1882 methodologically) given character-pullback transport. At this layer the audit is clean.

**Counter-considerations at the analytic layer.** At machine dyadics `m`, `1+m` are algebraic, but `ε(m)` is generally not; `e^{2πikε(m)}` introduces an additional exponential layer. If forbidding analytic compression of `e^{2πikε(m)}` requires transcendence input beyond Landfall §2 (linear forms in logarithms / Baker-style), the analytic realization is post-1882 even though the formal cocycle is pre-1882. Phase-lift conservativity may itself import such content, since it is precisely the claim that the analytic exponential cannot be cheaper than the affine coordinate. Manageable under `memos/OLD-TIME-RELIGION.md`'s content-not-calendar criterion; not free.

**Resolution path.** Sketch the formal-cocycle non-compressibility argument using only Landfall §2-content. Then state phase-lift conservativity as the bridge theorem the analytic-realization step requires; audit *that* theorem under content-not-calendar (Baker-style input is the natural suspect). The audit therefore has two stages: clean at the formal-cocycle layer, conditionally clean at the analytic layer once phase-lift conservativity's transcendence cost is named.

**Audit verdict.** Recorded in [fft/PHASE-LIFT-CONSERVATIVITY-AUDIT.md](fft/PHASE-LIFT-CONSERVATIVITY-AUDIT.md). **L-W content: (i) Clean** — phase-lift conservativity does not import Baker, Gelfond-Schneider, or Thue-Siegel-Roth content; the natural recovery route via small-branch power series for `Arg(z)` is pre-1882 calculus, per-sample cost `O(1)` at fixed precision. **Promotion: (ii) Clean-conditional** — the bridge's contentfulness is conditional on a non-transcendence definitional move: `C_Aff` must admit bounded-degree polynomial approximations of fixed-precision real functions. Under strict `Aff⁺(ℝ)` (the closure named in §"Character reflection barrier" above) the bridge is vacuous; under the natural extended reading (closure under machine arithmetic primitives) the bridge is true at competitive cost. **The definitional move has consequences for the Landfall §2 transfer** that the rewrite must price in: the §2 obstruction is stated against `Aff⁺(ℝ)` and must be re-derived in (or argued to transfer automatically to) the chosen extended `C_Aff`. The H-L 1882 transcendence-at-dyadics fact remains the *input* to the bridge (Landfall §2 / §4), classified clean under content-not-calendar.

## Sub-debts (under debt #2's expansion)

The cocycle reframe introduces four sub-debts:

- **Formal-character FFT composition.** Does FFT-style composition (the canon's standard composability) have a natural formulation at the formal-character level, or does it require analytic realization? If the latter, the cocycle reframe is an abstraction step, not a structural one. **Verdict** recorded in [fft/COCYCLE-COMPOSITION-LAW.md](fft/COCYCLE-COMPOSITION-LAW.md): **partial yes**. The cocycle-product composition law `Δ_k(O_2 ∘ O_1)(m) = Δ_k(m) · Δ_k^{O_1}(m) · Δ_k^{O_2}(O_1 m)` is the formal-character skeleton; per-operation residuals `Δ_k^O` require analytic realization on specific values. Cost-norm choice is the load-bearing analytic definitional move; operational cost-norm (per §"What this would buy") is recommended. Verdict shape parallels sub-debt 3's: formal layer clean, analytic layer conditional on a definitional move.
- **Closure-class transport (general).** Does the character reflection barrier hold for the chosen character system at the formal level — i.e., does `{Δ_k} ∈ C_FFT` reflect to `ε ∈ C_Aff` at competitive cost? Faithfulness is mild; log-liftability is mild only pointwise and cost-sensitive in the theorem-facing form; closure compatibility is the load-bearing component.
- **Phase-lift conservativity (analytic-exponential specialization).** For `χ_k(t) = e^{2πikt}`, does FFT-style competitive construction of `{Δ_k}` force competitive construction of `ε` in `C_Aff` after small-branch arg-unwrapping on `[0, ε_max]`? This is the substantive analytic specialization of closure compatibility and is *not* derivable from Landfall §2 ∪ §4 alone — it is the new content the sequel must earn. Pointwise recovery via `Arg` is automatic on the small defect interval; closure-class recovery is the bridge. **Verdict refinement** per [fft/LANDFALL-EXTENDED-CAFF-TRANSFER.md](fft/LANDFALL-EXTENDED-CAFF-TRANSFER.md): under the audit's natural fixed-precision (P)-reading, the Landfall §2 transfer to extended `C_Aff` fails (`ε` is `O(N)` cheap via Taylor); the bridge delivers no impossibility. The replacement source-side obstruction is **§4 + effective H-L `n = 1` at variable precision**, which gives `ε ∈ Ω(N log N)` and lets the bridge contrapositive bite. Sub-debt 3 promotes from "Clean-conditional on `C_Aff` definitional move" to "Clean-conditional on (a) variable-precision cost model and (b) effective H-L `n = 1` in cost-norm-compatible form."
- **Canon-bound translation.** Do the canon's concrete bounds (Morgenstern's `Ω(n log n)`, AFW's `μ`-bounds, Winograd's modular-product theorem) translate cleanly to cocycle-side compressibility claims? Each canon source gets a translation check.

Each is tractable; none is automatic. Phase-lift conservativity is the named, load-bearing analytic sub-debt. Cumulatively they sit under debt #2's expansion.

## What gets rewritten if the gates resolve favorably

**Gate status as of this revision: partially advanced.** Competitive compression has its operational definition (§"What this would buy"). Coordinate-cut alignment has its first canon test case at [fft/SCHOENHAGE-STRASSEN-COCYCLE-TRANSLATION.md](fft/SCHOENHAGE-STRASSEN-COCYCLE-TRANSLATION.md), grounded in [fft/SCHOENHAGE-STRASSEN-1971-BRIEF.md](fft/SCHOENHAGE-STRASSEN-1971-BRIEF.md): verdict **(b) Conditional** — both SS methods out-of-scope, theorem scope narrows to FFT-style methods that cross the *floating-point* additive/log-binade seam at their primitive-operation level. L-W audit on phase-lift conservativity at [fft/PHASE-LIFT-CONSERVATIVITY-AUDIT.md](fft/PHASE-LIFT-CONSERVATIVITY-AUDIT.md): **L-W content (i) Clean**, **promotion (ii) Clean-conditional** on a `C_Aff` definitional move with named consequences for the Landfall §2 transfer. Sub-debt 1 (formal-character FFT composition) discharged at [fft/COCYCLE-COMPOSITION-LAW.md](fft/COCYCLE-COMPOSITION-LAW.md): **partial yes**, cocycle-product law as formal-character skeleton with cost-norm choice as the analytic definitional move; recommendation is operational cost-norm. With sub-debt 1 typed, the cost meaning of `δ ≡ cost of {Δ_k} compression` is well-typed (operational cost-norm on the cocycle product), discharging the first of the three blockers identified in [memos/AMORTIZATION-AT-THE-BOUNDARY.md](memos/AMORTIZATION-AT-THE-BOUNDARY.md).

Per the project's promotion discipline (`fft/FFT-SEARCH-PLAN.md` Discipline section: vocabulary may promote when it earns its way; promotion is conditional on reducing a named construction debt), the rewrite is **not yet authorized**: the canon-translation verdict is conditional, the audit's promotion verdict is conditional on a definitional move that itself requires re-establishing the Landfall §2 transfer in the chosen extended `C_Aff`, and the literature audit on whether the floating-point/non-floating-point partition is exhaustive across the canon has not been run. The rewrite below is a *target shape*, not a green light.

If the conditional canon-translation verdict is accepted as scope-narrowing (in-scope iff floating-point seam-crossing), the `C_Aff` extension is made explicit and the Landfall §2 transfer re-established in it, and the four sub-debts close:

- **Outline §1.** Adopt the pre-`π` quotient-clock setup (Layer 1). `A`, `L`, `ψ`, `ε` defined as quotient-group objects before any character or analytic content.
- **Outline §1.5 / §3 / §4.** Introduce formal characters and the defect cocycle `Δ_k` (Layer 2). The exponential realization `D_k` becomes a derived analytic specialization.
- **Outline §4.5 (theorem statement).** "M does not improve past `T(P)`" → **No Free Descent**: "any FFT-competitive descent past `T(P)` requires `{Δ_k}` competitive compressibility under canon composability; the cocycle is forced by the quotient-clock displacement and cannot be bypassed by representation choice."
- **FIRST-PROOF Setup.** Transaction cost `δ` becomes "`δ ≡ cost of {Δ_k} cocycle compression`."
- **FIRST-PROOF Lemma B.** "No finite composition reduces `δ` to zero" becomes "No finite composition of native operations competitively compresses `{Δ_k}` at the boundary." Inherits Landfall §2 only after the character-pullback transport has been proved.
- **FIRST-PROOF Bridge Theorem.** Becomes: "Any descent past `T(P)` requires `{Δ_k}` competitive compressibility at the boundary." Concrete; testable.
- **FIRST-PROOF debt #3.** Narrows to the character-pullback transport theorem, with `λ`/`ε` named as the source-side obstruction.
- **`figures/delta_phase_plot.png`.** Re-projection: axes shift to "compression rate" and "asymptotic compression floor"; the Coase axiom band becomes a Landfall-anchored working floor (not a theorem until the lift is proved); cocycle non-compressibility region becomes the impossibility region.

## External positioning (Ailon)

Ailon, "A Lower Bound for Fourier Transform Computation in a Linear Model Over 2x2 Unitary Gates Using Matrix Entropy" (arXiv 1305.4745v1; local source `sources/Ailon-LB-1305.4745v1.pdf`) explicitly frames nontrivial Fourier lower bounds in broad linear-circuit models as a longstanding open problem. The paper gives an `Ω(n log n)` lower bound for the normalized Fourier transform in a layered linear model restricted to unitary `2×2` gates, and contrasts this with Morgenstern's bounded-coefficient determinant method for the unnormalized transform. The normalized FFT itself works in Ailon's restricted model.

The No Free Descent theorem would not be "another FFT lower bound" in the same direct sense. It would be a **structural no-escape result**: any export of FFT cheapness across the additive/log-binade seam must carry the defect cocycle. It therefore does not compete directly with Ailon's open-problem framing; it sits beside it as a structural obstruction rather than a direct broad-model lower bound. Add Ailon to References as adjacent FFT-side prior art when promotion lands.

## Relationship to FFT-SEARCH-PLAN

`FFT-SEARCH-PLAN` parks the *interpretive* sharpening: FFT-style methods are an adaptive strategy family. Vocabulary and discipline.

`PHASE-DEFECT` parks the *concrete-object* sharpening: if the gates resolve, the strategies operate on the cocycle family `{Δ_k}`, the residual phase factor forced by `ψ = m + ε`. Mathematical content; what the strategies are searching over.

The two are compatible: under search, the strategy family searches over `{Δ_k}` compressibility schemes. If neither gate in PHASE-DEFECT closes, FFT-SEARCH-PLAN stands without the cocycle formulation. If both close and competitive compression becomes a real cost notion, FFT-SEARCH-PLAN's strategy family acquires `{Δ_k}` as its target object.

## Trust boundary

This file is exploratory. The cocycle formulation is a *candidate* sharpening, not yet a proof object. The gating debts (coordinate-cut alignment, L-W audit), the competitive-compression definition, and the four sub-debts (formal-character composition, closure-class transport, phase-lift conservativity, canon-bound translation) must resolve before any of the proposed rewrites land. Phase-lift conservativity is the named bridge theorem the analytic sequel must earn — it is not a corollary of Landfall §2 ∪ §4. If gates fail, the cocycle stays parked or migrates to a separate paper.

The forced identity `χ_k(ψ(m)) = χ_k(m) · χ_k(ε(m))` is right and L-W-safe as algebra: it uses formal-character multiplicativity, no transcendence theorem. The implications for the FFT-impossibility argument are *conditional* on the gating debts and the sub-debts.

The promotion discipline of `fft/FFT-SEARCH-PLAN.md` applies here too: vocabulary may promote when it earns its way; philosophy stays parked; promotion is conditional on reducing a named construction debt. The cocycle formulation could reduce three primary debts at once — but only if the gates and sub-debts resolve favorably.
