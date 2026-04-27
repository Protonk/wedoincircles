# FIRST-PROOF
## Sketch of the descent impossibility, with construction debts visible

Working draft. Sections §4–§6 of the paper sketched in proof form. Load-bearing claims currently *asserted* rather than *earned* are flagged inline as **[Construction debt: …]**. The proof's central open object is the **Bridge Theorem**, named below and listed as debt #1 in the summary at the end.

This is the destination map the paper points toward; closing each debt is the paper's work.

## Theorem (working statement)

For every FFT-style method `M` and every problem `P` in the cyclotomic-DFT class (and adjacent compute-cost problems), `M` does not prove a lower bound on `P` improving past the existing threshold `T(P)`.

**[Construction debt.** Formal definitions of `M`, `P`, `T(P)`, and "FFT-style method" are deferred to §1 + §4. The quantifiers above are placeholders until the cost / conversion framework is formally specified.**]**

## Setup (working language)

From §1, in working form. None of the items below is a finished formal definition; each names an object the paper has to specify.

- **Multiplicative cost `μ` and additive cost.** Two complexity measures on FFT-style algorithms (per §1.2 and §1.3). **[Construction debt:** precise specification of each measure under the canon's standard accounting. Currently working language only.**]**
- **The mult/add conversion.** An adaptive strategy family that FFT-style algorithms search through (per §1.5 and `paper/FFT-SEARCH-PLAN.md`); each strategy is a finite composition of native operations under the canon's standard composability, and methods select a strategy adaptively from problem data. The same computation may admit multiple strategies under different decompositions or representations. **[Construction debt:** the conversion as a precisely-typed object — an adaptive strategy family closed under composition rather than a single partial function. Domain, codomain, regime-dependent behavior, route-multiplicity, search-strategy space, and search-space topology all need formal specification.**]**
- **Transaction cost `δ`.** A non-zero quantity associated with each instance of the conversion, reflecting irreducible cost. Vocabulary and typing follow Coase 1937 (`memos/COASE-FRICTION-AND-SPECIALISTS.md`): the existence of friction (`δ > 0`) is one claim; the algebra of friction is another. Lemma B is the existence-side claim about `δ`; the algebra of `δ` — and with it the full impossibility region — is debt #2. **[Construction debt:** the *algebra* of `δ` is not yet specified. Open questions: is it additive across compositions? amortizable over many uses? asymptotic? per-size? per-precision? representation-dependent? bypass-resistant under advice? Each is a distinct sub-debt — Lemma B as stated only blocks the simplest zeroing route; bypass / amortization / advice / multi-route effects require their own arguments under whatever algebra the paper specifies.**]**
- **Native operations and closure classes.** Operations the canon admits, and the closure classes they generate. **[Construction debt:** operational definitions of the four-framework canon's native operations, and the closure classes they generate. Per `fft/PROVENANCE-AND-TRANSFERABILITY.md`, *bridge work is construction, not import*.**]**
- **Coefficient regimes.** Bounded vs unbounded (§1.4). The regime parameterizes both the cost measures and `δ`.
- **Threshold `T(P)`.** Current best lower bound on `P` from the canon. **[Construction debt:** per-problem threshold specification; canon bounds are stated in different currencies (multiplicative complexity, additive complexity, modular product) and the threshold's role requires cross-currency reconciliation.**]**
- **FFT-style method `M`.** Finite composition of native operations under standard composability (per §4.2). **[Construction debt:** specification depends on §1's framework formalization and §3.6's "common conversion" defense.**]**

## Strategy

The proof composes the Bridge Theorem and Lemma B via a template inherited from Landfall §2. None of the three is yet earned; the strategy below identifies what each piece would contribute and what construction it requires. Lemma A is named as parallel reading; its equivalence with the Bridge + B + Template route is its own debt and Lemma A does not enter the QED.

- **Bridge Theorem (open; central construction).** Any FFT-style method that proves a lower bound on `P` improving past `T(P)` requires `δ` at the bounded/unbounded coefficient boundary to drop to zero.
  - This is the equivalence between "any threshold-improving descent" and "frictionless conversion at the boundary." Without it, Lemma B can block the frictionless-conversion route but not other routes. **[Construction debt:** the paper's central new theorem. Currently asserted, not derived. Substantive claim about the structure of descent paths under the cost / conversion framework.**]**
- **Lemma B (Closed composition).** Native operations compose into closure classes; reducing `δ` at the boundary to zero is outside the closure classes' reach.
- **Template (Landfall §2, restated for the cost / conversion framework).** No finite composition of native operations produces an effect outside the operations' closure class.

Bridge Theorem + Lemma B + Template close the impossibility.

**Lemma A (Information-uniformity at the boundary; parallel reading).** No FFT-algorithm passage extracts information distinguishing one trade from another at the boundary. Lemma A is the information-side reading of the same impossibility; whether it is rigorously equivalent to the Bridge-plus-B-plus-Template route is itself **[Construction debt]**. *Lemma A is not assumed by the QED below.*

## Lemma A — Information-uniformity at the boundary

**Claim.** At the boundary between bounded- and unbounded-coefficient regimes, no admissible FFT-algorithm passage extracts information distinguishing one trade from another.

**Sketch (substrate-side angles, five).**

1. *Rotation-orbit Diophantine kinematics.* `β(π) = 0` places the substrate on the Diophantine side. **[Audit debt:** if load-bearing here, `β(π) = 0` needs L-W-safety provenance per `memos/OLD-TIME-RELIGION.md`.**]**
2. *Non-nesting isoperimetric registers.* The three currencies (rate, constant, almost-every) do not nest.
3. *Closed-form polygon arithmetic.* Hurwitz coefficients, gap, sharp constants are fixed.
4. *Cyclotomic-ladder unboundedness against affine flatness.* `[K_n : ℚ] = φ(n)/2` grows; affine closure is flat.
5. *Admissibility envelope.* Auxiliary tools (Fortnow, strip-Fourier, Landfall log-side reference) supply no additional information within L-W safety.

**[Construction debt: exhaustiveness.** The five bullets cover specific substrate-side classes of distinguishing information. The universal claim "no admissible distinguishing information" requires an **exhaustiveness argument**: that the five angles cover *every* admissible source available to FFT-style methods. Not implied by the bullets; a separate covering argument is owed.

The argument closes by negative space. Any distinguishing-information source not covered by the five witnesses must violate one of the program's named constraints — L-W safety (`memos/OLD-TIME-RELIGION.md`), trust boundaries on the FFT canon (`fft/PROVENANCE-AND-TRANSFERABILITY.md`), the closure-mismatch theorem (`memos/NATIVE-F-MINIMAL-DEFINITION.md`), or BIND vocabulary erasure (`BNHA/triad/Eraserhead/BIND-THE-CIRCLE.md`). The five witnesses live inside the constraint envelope; the constraints close the rest.

Closure-class typing supplies the technical backbone: information of types incompatible with the closure class cannot enter the proof, since extracting it would require an operation outside the closure class — which by the Template does not exist. NATIVE-F's universal no-functor statement covers functorial-route information sources directly: distinguishing information that requires a functor between sides is foreclosed by the algebraic-side companion.**]**

## Lemma B — Closed composition of native operations

**Claim (existence-side).** Native operations compose into closure classes; no finite composition reduces `δ` at the bounded/unbounded boundary to zero.

**Sketch.**

- *Mult-side closure.* Composition of multiplicative-side primitives stays inside a closure class; `δ` contributions stay nonzero across the regime boundary.
- *Add-side closure.* Composition of additive-side primitives stays inside another closure class; same boundary behavior.
- *No reduction.* The boundary's irreducible `δ` is outside the reach of finite composition on either side.

*Existence vs algebra* (per `memos/COASE-FRICTION-AND-SPECIALISTS.md`). Lemma B is the existence-side claim: `δ > 0` at the boundary, and finite composition does not zero it. The algebra of `δ` — its scaling with problem, regime, and strategy — is debt #2's open structure. Lemma B suffices to compose with the Bridge Theorem and the Template to close the §4.5 theorem statement; the full impossibility *region* (which thresholds `T(P)` sit unreachable across the problem class) closes when debt #2 closes.

**[Construction debt:** each sub-claim requires explicit calculation in the cost / conversion formalism. Mult-side and add-side closure classes need definition; the boundary's `δ` behavior needs precise characterization; non-reduction is a calculation, not an inspection. The construction depends on the algebra of `δ` (see Setup); under amortization or advice-augmented regimes the no-reduction claim may need refinement or separate sub-arguments.**]**

**[Trust-boundary debt.** Per `fft/PROVENANCE-AND-TRANSFERABILITY.md` §3.2: SS supplies the operational model, not a lower bound; Morgenstern's bound is bounded-coefficient only; Winograd's μ-bounds are under rational equivalence; AFW is rational-equivalence cyclotomic decomposition, not certification cost. Lemma B's closure-class statement must respect each "should be cited for / should NOT be cited for" boundary.**]**

## Template (Landfall §2, restated)

**Statement (Landfall's instance, in hand).** Native binade operations generate `Aff⁺(ℝ)`; `λ(m) = log₂(1+m)` is not in the closure; therefore no finite composition of native binade operations produces `λ`.

**[Construction debt: template transfer.** The cost / conversion generalization is the paper's work; per `paper/LANDFALL-EXPORT.md` Template 1: "*the paper has to earn this generalization at the cost-manifold level.*" (LANDFALL-EXPORT was written under the manifold framing; the transfer task in the cost / conversion framework is parallel and inherits the same debt.) The concrete burden: **identify the specific operation or effect that, like `λ`, lies outside the closure class — i.e., the operation that would, if achievable by finite composition of native operations, zero `δ` at the boundary.** Until that specific operation is named with the same precision as `λ(m) = log₂(1+m)`, the template transfer is a structural analogy rather than a transferred proof.**]**

## Proof of the theorem (conditional on debts)

*Assuming* the Bridge Theorem, Lemma B, and the cost / conversion-generalized Template:

Suppose `M` is an FFT-style method proving a lower bound on `P` strictly improving past `T(P)`. Then `M` is a finite composition of native operations producing such a descent. By the Bridge Theorem, the descent requires `δ` at the bounded/unbounded boundary to drop to zero. By Lemma B, no finite composition of native operations reduces `δ` at the boundary to zero. By the Template, no finite composition produces an effect outside the operations' closure class. Contradiction. ∎

**Information-side reading via Lemma A** (parallel; not assumed by the QED above; conditional on the equivalence debt). At the boundary, choosing a frictionless trade requires information distinguishing one trade from another; Lemma A says no such information exists; therefore the trade cannot be directed even if the cost could be paid. The reading is informational; whether it is rigorously equivalent to the closure-class route is itself a **[Construction debt]**.

**Smarter-FFT rebuttal** (conditional on the above closing). A smarter FFT-style method does not answer the obstruction — same cost measures, same native operations, same closure classes, same `δ` at the boundary. Per Coase 1937 (`memos/COASE-FRICTION-AND-SPECIALISTS.md`): the cost may be reduced by smarter strategies (Coasean specialists) but it will not be eliminated. `δ` is on the substrate, not on the algorithm.

## Scope

- The theorem constrains FFT-style methods. Non-FFT methods are unconstrained.
- The non-FFT-operation question — whether some operation outside the canon's native operations reduces `δ` at the boundary — is well-posed and pointed to `memos/NATIVE-F-MINIMAL-DEFINITION.md` as the algebraic-side companion.
- Higher-resolution structure of the conversion (its precise typing, regime-dependent calculation, route-multiplicity, `δ` algebra) is deferred.

## Construction-debt summary

The proof depends on the following debts, ordered by how load-bearing each is for the QED:

1. **Bridge Theorem.** Any threshold-improving FFT-style descent requires `δ` at the boundary to drop to zero. Central new theorem.
2. **Cost / conversion formalization.** `μ`, additive cost, the conversion (as an adaptive strategy family closed under composition rather than a partial function; see `paper/FFT-SEARCH-PLAN.md`), `δ` with explicit algebra (additivity, amortizability, asymptotics, representation-dependence, bypass-resistance, sign-vs-shape — see `memos/COASE-FRICTION-AND-SPECIALISTS.md` for methodological precedent), search-strategy space and topology, regime parameter, threshold `T(P)` made formal per §1's framework. The algebra of `δ` closes the impossibility *region*; Lemma B's existence-side claim alone closes only the §4.5 theorem statement.
3. **Template transfer.** Landfall §2's affine-closure argument generalized to the cost / conversion framework. Concrete burden: name the specific operation or effect — analog of `λ(m) = log₂(1+m)` — that lies outside the closure class. Paper-internal construction per `paper/LANDFALL-EXPORT.md`.
4. **Lemma B's closure-class calculation.** Mult-side closure, add-side closure, non-reduction of `δ` at the boundary — three calculations, not inspections, dependent on the algebra of `δ`.
5. **Lemma A's exhaustiveness.** The five substrate-side angles do not yet constitute a covering theorem.
6. **A↔B equivalence.** Information route (Lemma A) and closure route (Bridge + B + Template) need an equivalence if Lemma A is to enter the proof rather than serve as parallel reading.
7. **Trust-boundary discipline.** Each citation of the FFT canon respects `fft/PROVENANCE-AND-TRANSFERABILITY.md`'s "should be cited for / should NOT be cited for" boundaries.
8. **β(π) = 0 L-W audit.** If load-bearing in Lemma A's first bullet, the reference must be audited under `memos/OLD-TIME-RELIGION.md`.

The eight debts are the paper's writing agenda. The sketch above is the destination; closing each debt is the work.
