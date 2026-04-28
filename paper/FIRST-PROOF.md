# FIRST-PROOF
## Sketch of the descent impossibility, with construction debts visible

Working draft. Sections §4–§6 of the paper sketched in proof form. Load-bearing claims currently *asserted* rather than *earned* are flagged inline as **[Construction debt: …]**. The proof's central open object is the **Bridge Theorem**, named below and listed as debt #1 in the summary at the end.

This is the destination map the paper points toward; closing each debt is the paper's work.

## Theorem (working statement)

For every FFT-style method `M` and every problem `P` in the cyclotomic-DFT class (and adjacent compute-cost problems), `M` does not prove a lower bound on `P` improving past the existing threshold `T(P)`.

**[Construction debt.** Formal definitions of `M`, `P`, `T(P)`, and "FFT-style method" are deferred to §1 + §4. The quantifiers above are placeholders until the cost / conversion framework is formally specified.**]**

## Setup (working language)

From §1, in working form. None of the items below is a finished formal definition; each names an object the paper has to specify.

**Methodological frame (two anchors).** Coase 1937 ([memos/COASE-FRICTION-AND-SPECIALISTS.md](memos/COASE-FRICTION-AND-SPECIALISTS.md)) supplies vocabulary and discipline for treating `δ` as irreducible friction with algebra: sign is one question, shape is another. Cook–Reckhow 1973 and Slot–van Emde Boas 1984 / van Emde Boas 1988/1990 ([memos/COST-MODEL-UNIFORMITY-BRIEF.md](memos/COST-MODEL-UNIFORMITY-BRIEF.md)) supply the charging/model-invariance discipline: the algebra of `δ` has to live inside a stated, reasonable cost model. Both anchors transfer as method, not theorem content. The proof is conditional on this cost-framework choice until debt #9 finishes the canon re-read.

- **Multiplicative cost `μ` and additive cost.** Two complexity measures on FFT-style algorithms (per §1.2 and §1.3). **[Construction debt:** precise specification of each measure under the canon's standard accounting. Currently working language only.**]**
- **The mult/add conversion.** An adaptive strategy family that FFT-style algorithms search through (per §1.5 and `fft/FFT-SEARCH-PLAN.md`); each strategy is a finite composition of native operations under the canon's standard composability, and methods select a strategy adaptively from problem data. The same computation may admit multiple strategies under different decompositions or representations. **[Construction debt:** the conversion as a precisely-typed object — an adaptive strategy family closed under composition rather than a single partial function. Domain, codomain, regime-dependent behavior, route-multiplicity, search-strategy space, and search-space topology all need formal specification.**]**
- **Transaction cost `δ`.** A non-zero quantity associated with each instance of the conversion, reflecting irreducible cost. Vocabulary and typing follow Coase 1937 (`memos/COASE-FRICTION-AND-SPECIALISTS.md`): the existence of friction (`δ > 0`) is one claim; the algebra of friction is another. Lemma B is the existence-side claim about `δ`; the algebra of `δ` — and with it the full impossibility region — is debt #2. **[Construction debt:** the *algebra* of `δ` is not yet specified. Open questions: is it additive across compositions? amortizable over many uses or per-instance specializations? asymptotic? per-size? per-precision? representation-dependent? Lemma B as stated only blocks the simplest zeroing route; amortization / per-instance specialization / multi-route effects require their own arguments under whatever algebra the paper specifies. Advice and non-uniformity are handled separately by the uniform-charge regularity guard in debt #9.**]**
- **Native operations and closure classes.** Operations the canon admits, and the closure classes they generate. **[Construction debt:** operational definitions of the four-framework canon's native operations, and the closure classes they generate. Per `fft/PROVENANCE-AND-TRANSFERABILITY.md`, *bridge work is construction, not import*.**]**
- **Coefficient regimes.** Bounded vs unbounded (§1.4). The regime parameterizes both the cost measures and `δ`.
- **Threshold `T(P)`.** Current best lower bound on `P` from the canon. **[Construction debt:** per-problem threshold specification; canon bounds are stated in different currencies (multiplicative complexity, additive complexity, modular product) and the threshold's role requires cross-currency reconciliation.**]**
- **FFT-style method `M`.** Finite composition of native operations under standard composability (per §4.2). **[Construction debt:** specification depends on §1's framework formalization and §3.6's "common conversion" defense.**]**

## Strategy

The proof has a potential-style skeleton with three separated claims — Bridge, Separation, Native drift — that combine into the impossibility. None is yet earned; the strategy below identifies what each piece contributes and what construction it requires. Lemma A is named as a parallel information-side reading; its squeeze relation with the three-claim closure route is debt #6, and Lemma A does not enter the QED.

- **Bridge claim (Bridge Theorem; open; central construction).** Any FFT-style method that proves a lower bound on `P` improving past `T(P)` requires crossing a named defect gap: `δ` at the bounded/unbounded coefficient boundary moves from `δ > 0` to `δ = 0`.
  - Endpoint-side claim. Without it, Native drift can block per-operation crossings but not the equivalence between threshold improvement and gap-crossing in the first place. **[Construction debt:** the paper's central new theorem. Currently asserted, not derived. Substantive claim about the structure of descent paths under the cost / conversion framework.**]**
- **Separation claim (Template; current source-side obstruction transported).** `δ = 0` lies outside the native closure class `C_FFT`.
  - Target-side claim. The endpoint of the bridge is not in the closure of native operations. The current route is Landfall §4 plus effective Hermite-Lindemann at `n = 1`, transported by the character reflection barrier / phase-lift conservativity candidate of `fft/PHASE-DEFECT.md`.
- **Native drift claim (Lemma B; per-operation).** Each native operation has bounded (or non-crossing) effect on the defect potential `δ` at the boundary; no single native operation crosses the gap.
  - Step-side claim. Per-operation drift bound, the analog of Ailon's per-gate `Φ(M_i) − Φ(M_{i-1}) ≤ 2`.

**Interface (potential-style skeleton).** The three claims combine: the gap must be crossed (Bridge), the target lies outside the closure (Separation), and no single native operation crosses the gap (Native drift); therefore no finite composition of native operations crosses the gap. Proof-shape precedent: `fft/AILON-2013-UNITARY-FFT-LOWER-BOUND-BRIEF.md` — endpoint values `Φ(Id) = 0`, `Φ(F) = n log₂ n`; per-gate drift `Φ(M_i) − Φ(M_{i-1}) ≤ 2`; therefore `m ≥ (n log₂ n)/2`. Ailon enters as **shape, not content**: the program's potential is `δ`, not matrix entropy; the model is the canon's FFT-style methods, not unitary `2 × 2` layered circuits. The trust-boundary posture in `fft/AILON-2013-UNITARY-FFT-LOWER-BOUND-BRIEF.md` §4 governs the citation.

**Lemma A (Information-uniformity at the boundary; parallel reading).** No FFT-algorithm passage extracts information distinguishing one trade from another at the boundary. Lemma A is the information-side reading of the same obstruction; debt #6 asks how this substrate-side refusal and the Bridge-plus-Separation-plus-Native-drift closure route converge as a squeeze on `T(P)`. *Lemma A is not assumed by the QED below.*

## Lemma B — Native drift on the defect potential

**Claim (native drift; per-operation).** Each native operation `o` has bounded (or non-crossing) effect on the defect potential `δ` at the bounded/unbounded coefficient boundary: the per-step change `δ(o(x)) − δ(x)` is either zero, or bounded above by a constant that depends only on the operation's class — not on the running state. No single native operation crosses the gap from `δ > 0` to `δ = 0`.

**Sketch.**

- *Mult-side drift.* Composition of multiplicative-side primitives stays inside a closure class; the per-operation effect on `δ` at the boundary is bounded.
- *Add-side drift.* Composition of additive-side primitives stays inside another closure class; the per-operation effect on `δ` is bounded.
- *No single-op crossing.* Neither class contains an operation whose single application drops `δ` from positive to zero at the boundary.

The shape is potential-style: `δ` is the potential, the boundary is the gap locus, and the claim is that each native operation moves `δ` only by a bounded amount. The Template (Separation) places `δ = 0` outside the closure of native operations; Native drift places per-operation effect inside the closure. Combined with the Bridge claim that threshold improvement requires crossing the gap, finitely many bounded steps cannot cross to a target outside the closure.

*Existence vs algebra* (per `memos/COASE-FRICTION-AND-SPECIALISTS.md`). Native drift is the existence-side claim: `δ > 0` at the boundary, and each native operation has bounded effect on `δ` there. The algebra of `δ` — its scaling with problem, regime, and strategy — is debt #2's open structure. Native drift, composed with the Bridge claim and the Separation claim, closes the core no-crossing contradiction at the boundary; the §4.5 statement's full quantification over `P`, `T(P)`, and the canon's distinct currencies (multiplicative complexity, additive complexity, modular product) still depends on debt #2's algebra of `δ`. The full impossibility *region* (which thresholds `T(P)` sit unreachable across the problem class) closes when debt #2 closes.

**[Construction debt:** each sub-claim requires explicit calculation in the cost / conversion formalism. Mult-side and add-side closure classes need definition; the boundary's `δ` behavior needs precise characterization; non-reduction is a calculation, not an inspection. The construction depends on the algebra of `δ` (see Setup); under amortization, per-instance specialization, or uncharged-growth regimes the no-reduction claim may need refinement or separate sub-arguments.**]**

**[Trust-boundary debt.** Per `fft/PROVENANCE-AND-TRANSFERABILITY.md` §3.2: SS supplies the operational model, not a lower bound; Morgenstern's bound is bounded-coefficient only; Winograd's μ-bounds are under rational equivalence; AFW is rational-equivalence cyclotomic decomposition, not certification cost. Lemma B's closure-class statement must respect each "should be cited for / should NOT be cited for" boundary.**]**

## Template — Separation: `δ = 0` outside the closure

**Statement (separation).** `δ = 0` lies outside the native closure class `C_FFT`. The Bridge claim's target endpoint is therefore not in the closure of native operations.

**Source-side instance (current).** Landfall §2 supplies the original affine-closure template: native binade operations generate `Aff⁺(ℝ)`, while `λ(m) = log₂(1+m)` and `ε = λ − m` are non-affine. That template no longer transfers at cost level under extended `C_Aff`, because polynomial Taylor approximation can put `ε` competitively in the class. The current source-side obstruction is therefore Landfall §4 plus effective Hermite-Lindemann at `n = 1`: under a uniform-charge variable-precision model, `ε` should carry a per-sample lower bound `Ω(p)` at precision `p` (per [memos/EFFECTIVE-HL-N1-COST-FORM.md](memos/EFFECTIVE-HL-N1-COST-FORM.md)).

**[Construction debt: template transfer.** The target-side burden is now to prove a transport lemma carrying the source-side cost obstruction on `ε` to `δ = 0 ∉ C_FFT`. Candidate transport: the **character reflection barrier** of `fft/PHASE-DEFECT.md`, with **phase-lift conservativity** as its analytic-exponential specialization. The transport mechanism is unchanged; the source-side obstruction has shifted from Landfall §2 non-affineness to Landfall §4 + effective H-L per-sample cost. Both the source-side lower bound and the character-reflection transport are still open.**]**

## Proof of the theorem (conditional on debts)

*Assuming* Bridge, Separation, and Native drift:

Suppose `M` is an FFT-style method proving a lower bound on `P` strictly improving past `T(P)`. Then `M` is a finite composition of native operations producing such a descent. By the **Bridge** claim, the descent corresponds to crossing the defect gap from `δ > 0` to `δ = 0` at the boundary. By the **Separation** claim, the target endpoint `δ = 0` lies outside the native closure class `C_FFT`. By the **Native drift** claim, each native operation has bounded (or non-crossing) effect on `δ` at the boundary; in particular, no single native operation crosses the gap. A finite composition of bounded-drift operations whose target lies outside the closure cannot reach that target — finitely many bounded steps inside the closure stay inside the closure. Contradiction. ∎

The argument is potential-style: endpoint gap (Bridge) + per-step drift bound (Native drift) + target-outside-closure (Separation). The shape is on the shelf in `fft/AILON-2013-UNITARY-FFT-LOWER-BOUND-BRIEF.md` (`Φ(Id) = 0`, `Φ(F) = n log₂ n`, `ΔΦ ≤ 2` per gate, hence `m ≥ (n log₂ n)/2`). The program's specific instantiation — `δ` as the potential, the bounded/unbounded coefficient boundary as the gap locus, the FFT canon's native operations as the steps — is the program's content; Ailon's matrix-entropy machinery does not enter, only the shape does.

**Information-side reading via Lemma A** (parallel; not assumed by the QED above; conditional on debt #6's squeeze articulation). At the boundary, choosing a frictionless trade requires information distinguishing one trade from another; Lemma A says no such information exists; therefore the trade cannot be directed even if the cost could be paid. This is an informational companion to the closure-class route, not a premise of the proof.

**Smarter-FFT rebuttal** (conditional on the above closing). A smarter FFT-style method does not answer the obstruction — same cost measures, same native operations, same closure classes, same `δ` at the boundary. The mathematical non-elimination claim is Lemma B's: smarter strategies redistribute or amortize cost but cannot zero `δ` at the boundary by finite composition. Coase 1937 (`memos/COASE-FRICTION-AND-SPECIALISTS.md`) supplies the vocabulary and methodological precedent — *reduce yes, eliminate no*, "Coasean specialists" — for naming what the lemma rules out. `δ` is on the substrate, not on the algorithm.

## Lemma A — Information-uniformity at the boundary (parallel reading)

*Not used in the QED above. Presented here as the information-side reading of the same obstruction. Debt #6 no longer asks for a logical equivalence with the closure-class route; it asks for the squeeze articulation that explains how both readings converge on `T(P)`.*

**Claim.** At the boundary between bounded- and unbounded-coefficient regimes, no admissible FFT-algorithm passage extracts information distinguishing one trade from another.

**Sketch (substrate-side angles, five).**

1. *Rotation-orbit Diophantine kinematics.* `β(π) = 0` places the substrate on the Diophantine side. **[Audit debt:** if load-bearing here, `β(π) = 0` needs L-W-safety provenance per `memos/OLD-TIME-RELIGION.md`.**]**
2. *Non-nesting isoperimetric registers.* The three currencies (rate, constant, almost-every) do not nest.
3. *Closed-form polygon arithmetic.* Hurwitz coefficients, gap, sharp constants are fixed.
4. *Cyclotomic-ladder unboundedness against affine flatness.* `[K_n : ℚ] = φ(n)/2` grows; affine closure is flat.
5. *Admissibility envelope.* Auxiliary tools (Fortnow, strip-Fourier, Landfall log-side reference) supply no additional information within L-W safety.

**[Construction debt: exhaustiveness.** The five bullets cover specific substrate-side classes of distinguishing information. The universal claim "no admissible distinguishing information" requires an **exhaustiveness argument**: that the five angles cover *every* admissible source available to FFT-style methods. Not implied by the bullets; a separate covering argument is owed.

The candidate closure route is by negative space. Any distinguishing-information source not covered by the five witnesses would have to violate one of the program's named constraints — L-W safety (`memos/OLD-TIME-RELIGION.md`), trust boundaries on the FFT canon (`fft/PROVENANCE-AND-TRANSFERABILITY.md`), the closure-mismatch theorem (`memos/NATIVE-F-MINIMAL-DEFINITION.md`), or BIND vocabulary erasure (`BNHA/triad/Eraserhead/BIND-THE-CIRCLE.md`). The five witnesses live inside the constraint envelope; whether the constraints close the rest is itself the exhaustiveness debt, not yet discharged.

Closure-class typing is the candidate technical backbone: information of types incompatible with the closure class would not be available to the proof if extracting it required an operation outside the closure class — which the Template would forbid (subject to the Template's own transfer debt #3). NATIVE-F's universal no-functor statement is the candidate cover for functorial-route information sources: distinguishing information that requires a functor between sides would be foreclosed by the algebraic-side companion. Each step is a candidate route, not a closed argument.**]**

## Scope

- The theorem constrains FFT-style methods. Non-FFT methods are unconstrained.
- The non-FFT-operation question — whether some operation outside the canon's native operations reduces `δ` at the boundary — is well-posed and pointed to `memos/NATIVE-F-MINIMAL-DEFINITION.md` as the algebraic-side companion.
- Higher-resolution structure of the conversion (its precise typing, regime-dependent calculation, route-multiplicity, `δ` algebra) is deferred.

## Construction-debt summary

The table is a status register, not a second proof. Debts #1, #3, #4 are the QED interface; #2 and #9 are foundations; #5, #6, #8 govern Lemma A's parallel-reading status; #7 is citation discipline. The "Do not re-claim" column is part of the summary.

| # | Debt | Proof role | Current status | Depends on | Do not re-claim |
|---|---|---|---|---|---|
| 1 | Bridge Theorem | Endpoint-side QED claim: threshold improvement requires crossing `δ > 0` to `δ = 0`. | Open; central new theorem. | #2, #9. | Do not treat gap-crossing as proved by the drift or separation arguments. |
| 2 | Cost / conversion formalization | Foundation for `μ`, additive cost, adaptive conversion strategies, `δ` algebra, regimes, and `T(P)`. | Partly advanced: cocycle composition is typed in [fft/COCYCLE-COMPOSITION-LAW.md](fft/COCYCLE-COMPOSITION-LAW.md); amortization and asymptotics point to [memos/EFFECTIVE-HL-N1-COST-FORM.md](memos/EFFECTIVE-HL-N1-COST-FORM.md). Advice / non-uniformity is delegated to #9. | `memos/COASE-FRICTION-AND-SPECIALISTS.md`, `fft/PHASE-DEFECT.md`, `memos/ALGEBRA-OF-DELTA.md`, `memos/AMORTIZATION-AT-THE-BOUNDARY.md`, #9. | Do not say Lemma B closes the full impossibility region; it closes only the existence-side core. Do not treat advice as an algebra-of-`δ` sub-claim. |
| 3 | Template transfer / Separation | Target-side QED claim: `δ = 0` lies outside `C_FFT`. | Open. Landfall §2 is the original affine-closure template, but it does not transfer at cost level under extended `C_Aff`; current source-side obstruction is Landfall §4 plus effective H-L at `n = 1`, still needing source-side lower bound and character-reflection transport. | #2, #9, [fft/LANDFALL-EXTENDED-CAFF-TRANSFER.md](fft/LANDFALL-EXTENDED-CAFF-TRANSFER.md), [fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md), [memos/EFFECTIVE-HL-N1-COST-FORM.md](memos/EFFECTIVE-HL-N1-COST-FORM.md). | Do not re-use `ε ∉ Aff⁺(ℝ)` / Landfall §2 non-affineness as the live cost-level obstruction. |
| 4 | Lemma B drift calculation | Step-side QED claim: no native operation crosses the defect gap. | Open calculations: mult-side drift, add-side drift, and no-single-op crossing. PHASE-DEFECT may narrow the FFT-side check to reflection of `ε`'s per-sample cost obstruction. | #2, #3, #9, `fft/PROVENANCE-AND-TRANSFERABILITY.md`, [fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md). | Do not import a lower bound from SS, Morgenstern, Winograd, AFW, or Ailon; each supplies only what its trust boundary allows. |
| 5 | Lemma A exhaustiveness | Substrate-side support for the parallel information reading. | Open covering argument; the five measure-theoretic angles are witnesses, not an exhaustion theorem. | [measure/SUBSTRATE-OBSTRUCTIONS.md](measure/SUBSTRATE-OBSTRUCTIONS.md), `memos/OLD-TIME-RELIGION.md`, `fft/PROVENANCE-AND-TRANSFERABILITY.md`, `memos/NATIVE-F-MINIMAL-DEFINITION.md`, `BNHA/triad/Eraserhead/BIND-THE-CIRCLE.md`. | Do not use Lemma A as a QED premise or treat the five bullets as universal coverage. |
| 6 | Lemma A / closure-route squeeze | Meta-claim relating the information reading to the Bridge + Separation + Native-drift route. | Open but lighter than the old equivalence demand: articulate convergence on `T(P)`; optional information-side Bridge only if Lemma A is promoted. | #1, #3, #4, #5, `BNHA/hakamada/MEASURE-TWICE.md`. | Do not re-claim `A ⟺ B` or logical equivalence between Lemma A and the closure route. |
| 7 | Trust-boundary discipline | Per-citation guardrail. | Ongoing. Each imported source needs its own "cited for / not cited for" boundary. | `fft/PROVENANCE-AND-TRANSFERABILITY.md`, `fft/AILON-2013-UNITARY-FFT-LOWER-BOUND-BRIEF.md`, `memos/BOWEN-DRILLING-AND-DENSITY.md`, `memos/COASE-FRICTION-AND-SPECIALISTS.md`. | Do not transfer theorem content from vocabulary or methodological precedents. |
| 8 | `β(π) = 0` L-W audit | Conditional support for Lemma A's first substrate-side bullet. | Open only if load-bearing; audit needed under old-time-religion discipline. | `memos/OLD-TIME-RELIGION.md`, [measure/SUBSTRATE-OBSTRUCTIONS.md](measure/SUBSTRATE-OBSTRUCTIONS.md). | Do not treat `β(π) = 0` as L-W-safe until the provenance audit is done. |
| 9 | Uniform-charge cost model and canon re-read | Foundation for the cost model in which #2's algebra and #3's source-side obstruction live. | Layer (a) methodological commitment is set at Setup. Layers (b) canon re-read and (c) substrate-side form-spec consumption remain open. | `memos/COST-MODEL-UNIFORMITY-BRIEF.md`, [fft/LANDFALL-EXTENDED-CAFF-TRANSFER.md](fft/LANDFALL-EXTENDED-CAFF-TRANSFER.md), [memos/EFFECTIVE-HL-N1-COST-FORM.md](memos/EFFECTIVE-HL-N1-COST-FORM.md), canon rereads of Morgenstern, AFW, Winograd, Ailon. | Do not say canon compatibility or effective H-L cost form is discharged. Do not conflate program "uniform-charge" with Cook-Reckhow constant `l(n)=1` / van Emde Boas uniform measure. |

The nine debts are the paper's writing agenda. The sketch above is the destination; closing each debt is the work.
