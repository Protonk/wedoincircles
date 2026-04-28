# Eff Eff Tee

>Meta instruction for humans and agents. Stage direction.

JACM is the venue. ~25 pages with figures is the target. The register is engineering inflected mathematics. Savoir faire is the goal.

## Abstract

We prove that current FFT-style lower-bound methods cannot improve past their existing thresholds on cyclotomic-DFT and adjacent compute-cost problems. The mult/add conversion underlying the FFT framework (Schönhage–Strassen 1971, Morgenstern 1973, Winograd 1978, Auslander–Feig–Winograd 1984) carries a transaction cost — the irreducible cost of trading multiplicative cost for additive cost or vice versa — that is bounded away from zero at the bounded/unbounded coefficient boundary, with each canon framework reaching its bound through its own measure-theoretic potential (Lebesgue / counting / ℚ-vector-space dimension / Shannon entropy across the canon and adjacent restricted-model lower bounds). A stronger FFT-style lower bound would require a frictionless conversion across that boundary, and the substrate it would operate on — rotation-orbit Diophantine kinematics under Haar measure, non-nesting isoperimetric registers across three measure-theoretic currencies, closed-form polygon arithmetic via `ζ(2)`-tail counting on Hurwitz-band decompositions, cyclotomic-ladder unboundedness against affine flatness as a counting-invariant asymmetry, and a Lebesgue null/full dichotomy under the L-W admissibility envelope — supplies no such conversion under any of these measures.

### CCS

**Primary.**
- Theory of computation → Computational complexity and cryptography → **Algebraic complexity theory**
- Theory of computation → Computational complexity and cryptography → **Circuit complexity**

**Secondary.**
- Theory of computation → Computational complexity and cryptography → **Problems, reductions and completeness**

**Optional context.**
- Mathematics of computing → Discrete mathematics → **Combinatorics**
- Mathematics of computing → Mathematical analysis → **Numerical analysis**


## §Intro

Context, claim, the operational-side reading paired with the algebraic-side closure-mismatch companion (`memos/NATIVE-F-MINIMAL-DEFINITION.md`). Frame figure: [figures/native_f_closure_mismatch.png](figures/native_f_closure_mismatch.png) — flat affine closure (left) against the unbounded `φ(n)/2` cyclotomic ladder (right), the closure-depth contrast in one panel. Re-referenced at §7. 

## §1. Mult/add cost and conversion

### §1.1. Setup
Two cost measures track FFT-style algorithm cost: multiplicative cost (§1.2) and additive cost (§1.3). The mult/add conversion (§1.5) is the family of strategies FFT-style algorithms use to trade cost between the two. The conversion has a *transaction cost* `δ`: a non-zero quantity reflecting the irreducible cost of executing a strategy. Vocabulary and typing follow Coase 1937 (`memos/COASE-FRICTION-AND-SPECIALISTS.md`); the existence of `δ` is one claim, its algebra another. `δ` depends on the coefficient regime (§1.4); the paper makes the conversion and `δ` explicit objects.

### §1.2. Multiplicative cost
The cost-bearing primitives are multiplications; the complexity measure `μ` counts them under bilinear / rational-equivalence accounting. Schönhage–Strassen 1971, Winograd 1978, and Auslander–Feig–Winograd 1984 each give `μ` structure on cyclotomic-DFT and adjacent computations (full presentation at §3).

### §1.3. Additive cost
The cost-bearing primitives are additions; the complexity measure counts them, sensitive to the coefficient regime. Morgenstern 1973's `Ω(n log n)` bounded-coefficient additive lower bound is the canonical structure-bearing result (full presentation at §3.3). Ailon 2013 is the adjacent normalized-FFT comparison: in a layered `2 × 2` unitary-gate model, matrix entropy gives the same `Ω(n log n)` scale without determinant growth.

### §1.4. Coefficient regimes
Bounded vs unbounded coefficients. The regime is a parameter of every cost measure on either side; many bounds — Morgenstern's notably — depend on which regime is in force. `δ` (§1.5) also depends on regime.

### §1.5. The mult/add conversion
The family of strategies FFT-style algorithms use to trade multiplicative cost for additive cost (or vice versa); methods select a strategy adaptively (Gauss 1805's `4×3` vs `3×4` for Pallas is the pre-1882 worked example, per `fft/GOLDSTINE-1977-INTERPOLATION-BRIEF.md`; deeper framing parked at `fft/FFT-SEARCH-PLAN.md`). The transaction cost `δ` — the irreducible cost of executing a strategy — depends on §1.4's regime parameter; `δ`'s behavior at the bounded/unbounded coefficient boundary is the object §4's main theorem speaks about. A candidate concrete realization of `δ` — `δ ≡ cost of {Δ_k} cocycle compression` — is parked at `fft/PHASE-DEFECT.md`, conditional on that file's gating debts and four sub-debts (formal-character composition, closure-class transport, phase-lift conservativity, canon-bound translation).

Figure: [figures/cost_conversion_schematic.png](figures/cost_conversion_schematic.png) — the cost-pair `(μ, α)` plane with the actual frontier (canon thresholds Morgenstern, AFW, Winograd marked), the counterfactual `δ = 0` frontier (unreachable per §4), the hatched `δ`-gap between them, and the Bridge equivalence `descent past T(P) ⟺ δ = 0 at boundary` (§6.2) shown as a double-headed vertical arrow at the bounded/unbounded coefficient boundary (§1.4). Bridge-side picture only; the closure-class story lives at §6.5. Companion at [paper/code/COST-CONVERSION-SCHEMATIC.md](paper/code/COST-CONVERSION-SCHEMATIC.md).

## §2. The tour

Promissory. After §1 establishes language, §2 promises the route: cards on the table at §3, theorem at §4, the maze at §5, gradients at §6, back to the canon at §7. Names the substrate-side corpus (rotation-orbit Diophantine kinematics, non-nesting isoperimetric registers, closed-form polygon arithmetic, cyclotomic-ladder unboundedness against affine flatness, admissibility envelope) as the proof material §5 will deploy.

## §3. Cards on the table

### §3.1. The canon together
Frame: four sources, 1971–1984, define the FFT lower-bound apparatus the paper engages with.

### §3.2. Schönhage–Strassen 1971
Operational uniform model: bit/gate primitives, FFT over a representation where root multiplication is cheap by construction.

### §3.3. Morgenstern 1973
Bounded-coefficient additive lower bound: `Ω(n log n)` additions for `n × n` determinant.

### §3.4. Winograd 1978
Modular-product theorem `μ(T_P) = 2n − k`; multiplicative complexity factors along the CRT decomposition.

### §3.5. Auslander–Feig–Winograd 1984
Semisimple cyclotomic decomposition of finite-abelian DFTs with multiplicative complexity under rational equivalence.

### §3.6. Common cost / conversion structure
What do the four attacks share in §1's cost / conversion framework?

#### §3.6.1. Translation
Each of §3.2–§3.5 re-read in §1's cost / conversion language. SS's operational uniform model as a multiplicative-side structure; Morgenstern's bound as the additive-side floor; Winograd's modular product as a CRT-factored ledger on the multiplicative side; AFW's cyclotomic decomposition as a factor-by-factor reading on the multiplicative side.

#### §3.6.2. What's structurally shared
The four cost / conversion readings converge on common structure: shared cost-bearing primitives, compatible composability, shared regime parameter, one mult/add conversion connecting the same two cost classes. Per-framework projection onto §1's axes:

| Framework | Cost side | Composability | Regime | Output |
|---|---|---|---|---|
| Schönhage–Strassen 1971 (§3.2) | mult | recursive Fermat-ring FFT in uniform bit/gate model | n/a (constructive) | upper: `O(N log N log log N)` for integer multiplication |
| Morgenstern 1973 (§3.3) | add | linear-composition closure | bounded coefficients | lower: `Ω(n log n)` additions for `n × n` DFT-related determinant |
| Winograd 1978 (§3.4) | mult | CRT-factored ledger via modular-product theorem | unbounded (rational equivalence) | exact: `μ(T_P) = 2n − k` for modular product |
| Auslander–Feig–Winograd 1984 (§3.5) | mult | semisimple cyclotomic decomposition | unbounded (rational equivalence) | per-factor `μ`-bound on cyclotomic DFTs |

Three of four sit on the multiplicative side; Morgenstern is the lone additive-side framework, and the only one that *requires* the bounded-coefficient regime (§1.4) to bind. SS's bound is upper, not lower, and its role in the paper is the operational uniform model rather than the bound itself. Together the four span the cost/conversion axes §6 deploys: mult-side / add-side, bounded / unbounded, constructive / lower-bound. None of them gives a bound transferable to another's regime — every transfer has to pay δ at §1.4's boundary.

### §3.7. Adjacent restricted-model lower bound: Ailon 2013
Ailon records the warning the paper must keep visible: nontrivial Fourier-transform lower bounds in broad linear-circuit models remain open, and known successes come with strong restrictions. His model keeps only `n` live coordinates; each gate applies a `2 × 2` unitary mixing to two coordinates. The normalized FFT fits this model in `O(n log n)` gates, and Ailon proves any such circuit needs at least `(1/2)n log_2 n` gates.

The proof mechanism is the useful import. For a unitary matrix `M`, define `Phi(M) = -∑_{p,q} |M(p,q)|² log_2 |M(p,q)|²`. Then `Phi(Id)=0`, `Phi(F)=n log_2 n` for the normalized Fourier matrix, and one native `2 × 2` unitary gate can raise `Phi` by at most `2`. Program use: Ailon supplies an entropy-potential precedent at the same scale as Morgenstern's determinant-potential lower bound, but in a different restricted model. It is not a broad FFT lower bound and not a proof of the program's `δ`; it is evidence that native-operation restrictions can make a monotone potential carry the lower-bound load.

## §4. Main theorem

### §4.1. Frame
Preview in plain language: an impossibility theorem on FFT-style descent below existing lower-bound thresholds for cyclotomic-DFT and adjacent compute-cost problems. The formal version is at §4.5.

### §4.2. FFT-style methods
The hypothesis class.

#### §4.2.1. Standard composability of the canon
The composability rules used by Schönhage–Strassen, Morgenstern, Winograd, and AFW (§3.2–§3.5). The class is closed under these.

#### §4.2.2. The class defined
Formally: an FFT-style method is a finite composition of native operations under the standard composability of the canon — equivalently, an adaptive strategy family closed under composition (per §1.5's reading; see `fft/FFT-SEARCH-PLAN.md` for the Gauss 1805 anchor and the deeper search-theoretic framing). This is the formal object §4.5 quantifies over.

### §4.3. Cyclotomic-DFT and adjacent
The problem class. Cyclotomic-DFT specifically — the discrete Fourier transform over cyclotomic fields. "Adjacent" pinned down: compute-cost problems sharing §1's cost / conversion structure, differing in inputs but not in the cost / conversion framework the bounds inhabit.

### §4.4. Existing thresholds
The current best lower bounds the theorem asserts are unreachable from below. AFW's multiplicative-complexity threshold for cyclotomic DFTs under rational equivalence; Morgenstern's `Ω(n log n)` bounded-coefficient additive threshold; Winograd's modular-product threshold. Named precisely; cited to §3.

### §4.5. The theorem
Formal propositional statement. For every FFT-style method `M` (§4.2) and every problem `P` (§4.3), `M` does not prove a lower bound on `P` below the existing threshold `T(P)` of §4.4. Equivalently: no FFT-style descent below the current thresholds is reachable on this substrate.

### §4.6. Proof outline
Three load-bearing claims combine into a potential-style argument (per `paper/FIRST-PROOF.md`). **Bridge** (§6.2): threshold improvement requires crossing the defect gap from `δ > 0` to `δ = 0` at the boundary. **Separation** (§6.4): `δ = 0` lies outside the native closure class, via the affine-closure template inherited from Landfall §2 (`paper/LANDFALL-EXPORT.md`). **Native drift** (§6.5): each native operation has bounded effect on `δ` at the boundary; no single native operation crosses the gap. Combined at §6.6: finitely many bounded steps inside the closure cannot reach a target outside it. Lemma A (§5.6 / §6.3) is the information-side parallel reading; not assumed by the QED. Proof-shape precedent: Ailon's matrix-entropy potential (§3.7), imported as shape, not content.

## §5. A maze of twisting passages, all alike

### §5.1. Rotation-orbit Diophantine kinematics
Arena: finite irrationality measure for `π` implies the Avila–Jitomirskaya parameter `β(π) = 0`, placing the orbit `{kπ mod 1}` in Weyl's equidistribution regime against Haar measure on `T = ℝ/ℤ`. No FFT-algorithm passage extracts a kinematic feature distinguishing one trade from another beyond the Haar mean for continuous and Riemann-integrable test functions. Source-side typing per `paper/MEASURE-THEORETIC-OBSTRUCTIONS.md` §1.

### §5.2. Non-nesting isoperimetric registers
Currencies: the three (rate, constant, almost-every) do not nest; no passage gets a free conversion between them. Constant register: Bonnesen-strengthening per Osserman 1979 / Bonnesen 1921. Almost-every register: Khintchine / Beck 1994 tradition. Source-side typing per `paper/MEASURE-THEORETIC-OBSTRUCTIONS.md` §2.

### §5.3. Closed-form polygon arithmetic
Values: Hurwitz coefficients (Fourier expansion on the sparse lattice `m ≡ 1 mod n`), gap `4π⁴/(3n²)`, and the first-band concentration constant `6/π² = 1/ζ(2)` (from the `ζ(2)`-tail comparison `B_j(n) ≤ B_1(n)/j²` per `corners/HURWITZ-FIRST-BAND-CONCENTRATION.md` §1) are fixed; descent reaches them only at threshold. Source-side typing per `paper/MEASURE-THEORETIC-OBSTRUCTIONS.md` §3. Figures: [figures/archimedean_triptych.png](figures/archimedean_triptych.png) sets up the inside-out / outside-out / strip substrate; [figures/hurwitz_gap_rate.png](figures/hurwitz_gap_rate.png) closes the Hurwitz identity at the `4π⁴/(3n²)` Archimedean rate (three series collapse to one line over seven decades); [figures/hurwitz_gap_frequency_decomposition.png](figures/hurwitz_gap_frequency_decomposition.png) shows the first-band concentration `B_1(n) ≥ (6/π²) Δ_n` directly as a stacked-area chart over `n`.

### §5.4. Cyclotomic-ladder unboundedness against affine flatness
Structure: the maximal real subfield `K_n^+ = ℚ(ζ_n + ζ_n^{−1})` has `[K_n^+ : ℚ] = φ(n)/2`, which grows unbounded with `n`; affine closure is flat; native operations cannot bridge the asymmetry. Source-side typing per `paper/MEASURE-THEORETIC-OBSTRUCTIONS.md` §4 (counting-invariant obstruction). Figure: [figures/pseudo_chebyshev_arithmetic_ladder.png](figures/pseudo_chebyshev_arithmetic_ladder.png) — degrees of `cos(π/n)` over ℚ as a stem chart, constructible nodes filled and non-constructible open, with `n = 7` highlighted as the first cubic and first non-constructible node.

### §5.5. The admissibility envelope
Audit: within L-W safety, closed-branch evidence, and the auxiliary-tool repertoire, no admissible method extracts additional descent information. The operative measure-theoretic fact within the envelope is the Lebesgue null/full dichotomy on `ℝ` (algebraics null; transcendentals full); finer distinctions among transcendentals trigger per-instance content-not-calendar audits per `memos/OLD-TIME-RELIGION.md`. Source-side typing per `paper/MEASURE-THEORETIC-OBSTRUCTIONS.md` §5.

### §5.6. Information-uniformity at the boundary
Synthesis: §5.1–§5.5 jointly establish that every passage hits the bounded/unbounded coefficient boundary the same way. The result §6 inherits.

## §6. Gradients without information

### §6.1. Descent in the cost / conversion framework
Setup: descent in §1's framework means trading a higher cost-bearing complexity bound for a lower one by reorganizing the underlying computation. Lower-bound improvement *is* successful descent. The proof asks whether such descent is reachable by FFT-style methods past `T(P)`.

### §6.2. Bridge claim: threshold improvement requires crossing the defect gap
For descent past `T(P)` to succeed, the algorithm must drive `δ` at the bounded/unbounded coefficient boundary from positive to zero — equivalently, cross the defect gap. The Bridge claim asserts this equivalence: threshold improvement *is* gap-crossing. Endpoint-side claim of the potential-style interface (`paper/FIRST-PROOF.md`). Central new theorem of the program. **[Construction debt #1.]**

### §6.3. Lemma A inherited (parallel reading)
§5.6 establishes information-uniformity at the boundary: no FFT-algorithm passage extracts information distinguishing one trade from another. Under `BNHA/hakamada/MEASURE-TWICE.md`'s discipline this is the **substrate-side measure-theoretic refusal** — the substrate's five measures (per `paper/MEASURE-THEORETIC-OBSTRUCTIONS.md`) jointly refuse the distinguishing information descent would need. The closure route of §6.4–§6.5 is the complementary **algorithm-side measure-theoretic refusal**; together they form a measure-theoretic squeeze on `T(P)` (per `paper/FIRST-PROOF.md` debt #6, re-framed as squeeze convergence rather than logical equivalence). *Lemma A is not used in the QED*; the QED closes via the closure route alone, with the Bridge claim's equivalence between threshold improvement and gap-crossing supplying sufficiency. Lemma A's exhaustiveness debt (#5) governs the substrate-side half independently.

### §6.4. Separation claim: `δ = 0` outside the native closure class
The proof template extracted at `paper/LANDFALL-EXPORT.md` Template 1, restated for the cost / conversion framework as the Separation claim: `δ = 0` lies outside the closure of native operations. Source-side instance: Landfall §2's affine-closure result that `λ(m) = log₂(1+m)` is not in the closure generated by binade operations; equivalently `ε = λ − m` is non-affine since `m` is affine. Target-side: prove a transport lemma carrying `ε ∉ C_Aff` to `δ = 0 ∉ C_FFT`. Candidate transport: the **character reflection barrier** of `fft/PHASE-DEFECT.md`, with **phase-lift conservativity** as its analytic-exponential specialization. Target-side claim of the potential-style interface. **[Construction debt #3.]**

### §6.5. Native drift claim: bounded per-operation effect on `δ`
Each native operation has bounded (or non-crossing) effect on the defect potential `δ` at the boundary. Mult-side primitives of §1.2 compose into a closure class; per-operation drift on `δ` is bounded. Add-side primitives of §1.3 compose into another closure class; same drift bound. No single native operation crosses the gap from `δ > 0` to `δ = 0`. Step-side claim of the potential-style interface. **[Construction debt #4.]**

Figure: [figures/delta_phase_plot.png](figures/delta_phase_plot.png) — the closure-class picture in algebraic-phase space (amortization rate, asymptotic floor). Above the working-floor line `δ_min`: the IMPOSSIBILITY region (native closure of mult/add primitives). Below the foreclosed strip: the FFT canon's claimed territory at `floor = 0`, unreachable by finite composition. The horizontal mustard band straddling the working floor is debt #2 in the open: where `δ_min` actually sits depends on the algebra of `δ`. Companion at [paper/code/COASE-PHASE.md](paper/code/COASE-PHASE.md).

Proof-shape precedent: Ailon 2013 (§3.7) demonstrates the potential-style argument in a restricted unitary model — endpoint values `Φ(Id) = 0`, `Φ(F) = n log₂ n`, per-gate drift `ΔΦ ≤ 2`, conclusion `m ≥ (n log₂ n)/2`. The program imports the *shape*, not the content: `δ` is the potential, the bounded/unbounded coefficient boundary is the gap locus, the FFT canon's native operations are the steps. Ailon's matrix-entropy machinery does not enter; only the three-claim skeleton does. Trust-boundary discipline per `fft/AILON-2013-UNITARY-FFT-LOWER-BOUND-BRIEF.md` §4.

### §6.6. Compose the three claims; QED
Compose Bridge + Separation + Native drift. Descent past `T(P)` requires crossing the defect gap (Bridge), but the target `δ = 0` lies outside the native closure class (Separation), and each native operation has bounded effect on `δ` at the boundary (Native drift). A finite composition of bounded-drift operations whose target lies outside the closure cannot reach that target; finitely many bounded steps inside the closure stay inside the closure. No FFT-style descent below current thresholds is reachable on this substrate. A smarter FFT-style method does not answer the impossibility — same cost measures, same native operations, same closure classes, same `δ` at the boundary. The mathematical non-elimination claim is Native drift's — the existence-side claim of the §1.1 typing, with the algebra-side held open at debt #2. Coase 1937 (`memos/COASE-FRICTION-AND-SPECIALISTS.md`) supplies the vocabulary (*reduce yes, eliminate no*) for naming what the lemma rules out. The obstruction is structural, not in algorithmic cleverness. QED for §4.

*Meta-claim (FIRST-PROOF debt #6, re-framed as squeeze convergence).* Originally, debt #6 sought a logical equivalence between substrate-side refusal (Lemma A, §6.3) and algorithm-side refusal (Bridge + Separation + Native drift, §6.2 / §6.4 / §6.5). The outline re-frames the relationship as **squeeze convergence**: the bound `T(P)` is structurally real because every algorithm-side framework reaches it via a measure-theoretic argument (the canon's `Ω(n log n)` cluster, each in its own measure: Lebesgue / counting / dimension / Shannon entropy / bit-counting) and every substrate-side angle refuses descent under a different measure-theoretic argument (the five §5 obstructions: Haar / three isoperimetric registers / `ζ(2)`-tail counting / counting-invariant on extensions / Lebesgue null-full). The two sides converge on `T(P)` from different cost-currencies; the convergence is the structural fact, not an artifact of any one framework, and not the logical equivalence the original debt sought. Substrate-side typing per `paper/MEASURE-THEORETIC-OBSTRUCTIONS.md`; methodological character per `BNHA/hakamada/MEASURE-TWICE.md`.

### §6.7. Construction-debt accounting

The eight debts of `paper/FIRST-PROOF.md` mapped to outline location and current status. Status taxonomy: **load-bearing for QED** (the three-claim interface), **foundational** (gates the others), **parallel-reading** (Lemma A's status; not used in QED), **methodological** (per-citation discipline).

| # | Name | Outline location | Status | Note |
|---|---|---|---|---|
| 1 | Bridge Theorem | §6.2 `[Construction debt #1]` | Load-bearing (QED) | Equivalence between threshold improvement and gap-crossing; central new theorem |
| 2 | Cost / conversion formalization (algebra of `δ`) | §1.1 (typing), §1.5, §6.6 | Foundational; gates #1, #3, #4 | `μ`, additive cost, strategy-family conversion, `δ` algebra; closes the impossibility *region*, vs Lemma B alone closing the §4.5 *statement* |
| 3 | Template transfer (Separation) | §6.4 `[Construction debt #3]` | Load-bearing (QED) | Carries `ε ∉ C_Aff` (Landfall §2) to `δ = 0 ∉ C_FFT`; candidate transport via character reflection barrier (`fft/PHASE-DEFECT.md`) |
| 4 | Lemma B per-operation drift (Native drift) | §6.5 `[Construction debt #4]` | Load-bearing (QED) | Mult-side, add-side, no-single-op-crossing — three calculations, not inspections |
| 5 | Lemma A's exhaustiveness | §6.3 (parenthetical) | Parallel-reading (not QED) | Five substrate-side angles must cover every admissible distinguishing-information source |
| 6 | A and B as squeeze halves | §6.3, §6.6 (meta-claim) | Parallel-reading; meta-claim | Articulates squeeze convergence on `T(P)`; rigorous `A ⟺ B` no longer required |
| 7 | Trust-boundary discipline | §3, §6, References (per-source) | Methodological | Each canon citation respects `fft/PROVENANCE-AND-TRANSFERABILITY.md`'s "should be cited for / should NOT be cited for" boundaries |
| 8 | `β(π) = 0` L-W audit | §5.1 | Parallel-reading; conditional | If load-bearing in Lemma A's first bullet, audit under `memos/OLD-TIME-RELIGION.md` |

Pay-down status as of this revision: #1, #3, #4 sharpened (named and located) but not earned; #2's `δ` algebra parked per Coase precedent; #6 re-framed from logical-equivalence to squeeze convergence; #7 and #8 are ongoing per-source / per-citation discipline.

## §7. Back again

Return to the four frameworks of §3, now under the impossibility. Schönhage–Strassen, Morgenstern, Winograd, AFW are at their natural limits — not from defect, but because no further descent is reachable on this substrate by these methods. Pair with the algebraic-side closure-mismatch reading (`memos/NATIVE-F-MINIMAL-DEFINITION.md`): the operational-side and algebraic-side companions complete each other. Figure re-reference: [figures/native_f_closure_mismatch.png](figures/native_f_closure_mismatch.png) — the §Intro panel re-read after the impossibility theorem closes; the closure-depth contrast is the structural payoff, not the setup.

## §Conclusion

Coda. What's named, what's left as future work: the cost-manifold map at higher resolution; non-FFT lower-bound methods; the K-H-L-A discrepancy strut as adjacent program. Operational-observable companion figure: [figures/counting_psi_stratification.png](figures/counting_psi_stratification.png) — the ψ(n)-stratified outside-out sweep-x-support over `n ∈ [3, 40]`, localizing the algebraic-depth discontinuity at `n = 7` through ψ classes (Bravais ψ = 2 backbone vs first cubic ψ = 6). The algebraic-side `n = 7` first-cubic anchor of [figures/native_f_closure_mismatch.png](figures/native_f_closure_mismatch.png) shows up here in the operational-observable register. The compute-cost branch (`memos/LEDGER-PIVOT-SEARCH.md`, `fft/FOUR-FRAMEWORK-SYNTHESIS.md`) searches for the cost-theorem that converts this stratification into a primitive-op floor.

*Pencil mark for prose pass.* The non-FFT vector-field question is well-posed and sharpened by the manifold framing — *is there a non-FFT vector field that crosses the discontinuity?* Point to `memos/NATIVE-F-MINIMAL-DEFINITION.md` as the place where a different vector field is considered (the algebraic-side companion is the natural home for that question). Clean handoff, not vague future work.

# Figures

Eight figures, theorem-paired, each with an alt-text-ready companion document. All figures live at `figures/`; build scripts and companion documents per the table below.

| Figure | Build script | Companion document | Section |
|---|---|---|---|
| [figures/native_f_closure_mismatch.png](figures/native_f_closure_mismatch.png) | [memos/build_native_f_closure_mismatch.py](memos/build_native_f_closure_mismatch.py) | [memos/NATIVE-F-MINIMAL-DEFINITION.md](memos/NATIVE-F-MINIMAL-DEFINITION.md) | §Intro, §7 |
| [figures/cost_conversion_schematic.png](figures/cost_conversion_schematic.png) | [paper/code/build_cost_conversion_schematic.py](paper/code/build_cost_conversion_schematic.py) | [paper/code/COST-CONVERSION-SCHEMATIC.md](paper/code/COST-CONVERSION-SCHEMATIC.md) | §1.5 |
| [figures/archimedean_triptych.png](figures/archimedean_triptych.png) | [n-gons/build_archimedean_triptych.py](n-gons/build_archimedean_triptych.py) | [n-gons/ARCHIMEDEAN-STRIP-FLIP.md](n-gons/ARCHIMEDEAN-STRIP-FLIP.md) | §5.3 |
| [figures/hurwitz_gap_rate.png](figures/hurwitz_gap_rate.png) | [corners/hurwitz_gap.sage](corners/hurwitz_gap.sage) | [corners/HURWITZ-GAP.md](corners/HURWITZ-GAP.md) | §5.3 |
| [figures/hurwitz_gap_frequency_decomposition.png](figures/hurwitz_gap_frequency_decomposition.png) | [corners/hurwitz_gap.sage](corners/hurwitz_gap.sage) | [corners/HURWITZ-FIRST-BAND-CONCENTRATION.md](corners/HURWITZ-FIRST-BAND-CONCENTRATION.md) | §5.3 |
| [figures/pseudo_chebyshev_arithmetic_ladder.png](figures/pseudo_chebyshev_arithmetic_ladder.png) | [corners/pseudo_chebyshev_arithmetic_ladder.sage](corners/pseudo_chebyshev_arithmetic_ladder.sage) | [corners/PSEUDO-CHEBYSHEV-NODES.md](corners/PSEUDO-CHEBYSHEV-NODES.md) | §5.4 |
| [figures/delta_phase_plot.png](figures/delta_phase_plot.png) | [paper/code/build_delta_phase_plot.py](paper/code/build_delta_phase_plot.py) | [paper/code/COASE-PHASE.md](paper/code/COASE-PHASE.md) | §6.5 |
| [figures/counting_psi_stratification.png](figures/counting_psi_stratification.png) | [n-gons/counting/build_psi_stratification.py](n-gons/counting/build_psi_stratification.py) | [n-gons/counting/PSI-STRATIFICATION.md](n-gons/counting/PSI-STRATIFICATION.md) | §Conclusion |

All previously named figure-and-table gaps are now in place; further gaps will be identified during the prose pass.

---

# References

> Provenance discipline per `BNHA/ONE-FOR-ALL.md`: every load-bearing tool below names the chain it inherits from, and is staged for the next reader to pick up without reconstructing context. Working entries; bibliographic data refined per pass.

## Primary engagement — the four FFT frameworks (§3, §7)

- **Schönhage, A., and Strassen, V., 1971** — operational uniform model; cited at §1 (cost-manifold definition) and §3 (best light + avoidance: not a lower-bound source).
- **Morgenstern, J., 1973** — bounded-coefficient additive lower bound; cited at §1, §3, §6 (the floor that turns out to be unreachable from below).
- **Winograd, S., 1978** — modular-product theorem `μ(T_P) = 2n − k` and CRT-cyclotomic factor ledger; cited at §1, §3.
- **Auslander, L., Feig, E., and Winograd, S., 1984** — cyclotomic decomposition under rational equivalence; cited at §1, §3.
- **`fft/FFT-COMPLEXITY-ARTICULATION.md`** *(in-program extract)* — proof-template and trust-boundary index for the four FFT frameworks.
- **Goldstine, H. H., 1977** — *A History of Numerical Analysis from the 16th Through the 19th Century*, §4.12–13. Pre-1882 anchor for the FFT-as-adaptive-search reading: Gauss 1805's divide-and-conquer interpolation engine, with the Pallas worked example (`4×3` vs `3×4`) chosen on practical grounds rather than asymptotic ones. Source-extraction at `fft/GOLDSTINE-1977-INTERPOLATION-BRIEF.md`; deeper framing parked at `fft/FFT-SEARCH-PLAN.md`. Cited at §1.5, §4.2, and (potentially) §3 / §7.

## Adjacent FFT lower-bound prior art (§3.7)

- **Ailon, N., 2013** — `Ω(n log n)` lower bound for the normalized Fourier transform in a layered `2 × 2` unitary-gate model, proved by a matrix-entropy potential; cited for the survey warning that broad linear-circuit Fourier lower bounds remain open and for the restricted-model entropy-potential precedent. Source-extraction at `fft/AILON-2013-UNITARY-FFT-LOWER-BOUND-BRIEF.md`.

## Cost / conversion framework anchor (§1)

- **Coase, R. H., 1937** — "The Nature of the Firm," *Economica* New Series Vol. 4 No. 16 (Nov. 1937), pp. 386–405. PDF at [sources/Coase-1937.pdf](sources/Coase-1937.pdf). Source for the transaction-cost framework adopted at §1.5 and §6: trade through any coordination mechanism carries a non-zero, irreducible fee, and the *algebra* of that fee — additivity across compositions, amortization across repeated uses, scale-behavior, representation-dependence, bypass-resistance under specialist intermediation, and heterogeneity across transaction types — determines what the framework lets one prove. Coase's distinction between the existence of friction (p. 390: "there is a cost of using the price mechanism") and its algebra (p. 395 marginal condition; p. 396 the firm-size determination "(a) the less the costs of organising and the slower these costs rise with an increase in the transactions organised") is the methodological precedent for FIRST-PROOF debt #2 (algebra of `δ` left open with named open sub-questions). Cited at §1.1 (transaction-cost vocabulary), §1.5 (irreducible-fee framing), §6.5 (Lemma B as the simplest zeroing-route block, with full algebra of `δ` deferred per debt #2), and (potentially) §Conclusion as the methodological-framework reference.

## Algebraic-side material

- **Heideman, M. T., Johnson, D. H., and Burrus, C. S., 1985, §5** — eigenspace decomposition `Q(ζ_n) = K_n ⊕ K_n · 2i sin(2π/n)` under `σ_{−1}`, forcing `K_n` as the multiplicatively-closed half; cited at §1, §6.
- **`memos/NATIVE-F-MINIMAL-DEFINITION.md`** *(in-program companion)* — closure-mismatch theorem (no functor `F` preserves closure-depth from `Aff⁺(ℝ)` to `{K_n}`); cited at §Intro and §7 as the algebraic-side companion.

## Substrate-side sources (§5)

- **`paper/MEASURE-THEORETIC-OBSTRUCTIONS.md`** *(in-program companion)* — substrate-side measure-theoretic typing of the five §5 angles: Haar measure on `T = ℝ/ℤ` for §5.1; non-nesting of three measure-theoretic registers (rate / constant / almost-every) for §5.2; `ζ(2)`-tail comparison and Hurwitz Fourier expansion for §5.3; ℚ-vector-space dimension as counting-invariant obstruction for §5.4; Lebesgue null/full dichotomy under L-W safety for §5.5. Sister to `paper/LANDFALL-EXPORT.md` and `fft/PHASE-DEFECT.md`. Cited at §5.1–§5.5 as the source-side typing layer.

### Rotation-orbit Diophantine kinematics

- **Avila, A., and Jitomirskaya, S., "The Ten Martini Problem,"** *Annals of Mathematics* 2009 — exponential-rate Diophantine parameter `β(α) = limsup (ln q_{n+1}) / q_n`; places `π` on the Diophantine side.
- **Berthé, V., and Reutenauer, C.** — three-distance theorem combinatorial reading via three-interval exchanges.
- **Ferenczi, S., and Zamboni, L.** — perfectly clustering Lyndon-word characterization used through Berthé–Reutenauer's citation and statement, not as a separately audited source.
- **Lefèvre, V., Muller, J.-M., and Tisserand, A., 1998** — compressed-orbit pseudocode for the table-maker's-dilemma filter.
- **Marklof, J., and Strömbergsson, A.** — lattice formulation of the three-distance theorem on `Γ\SL(2, ℝ)`.

### Non-nesting isoperimetric registers

- **Osserman, R., 1979** — Bonnesen-strengthening inequality `L² − 4πA ≥ π²(R − r)²`.
- **Fuglede, B., 1989, Theorem 1.2** — stability bound for nearly-spherical domains.
- **Beck, J., 1994** — higher-dimensional Fourier + second-moment + Borel–Cantelli machinery as Diophantine substitute.
- **Bonnesen, T., 1921; 1924** — both forms; audit-catalogue same-result-different-constants instance.
- **Hurwitz, A., 1902** — Fourier-isoperimetric identity.

### Closed-form polygon arithmetic

- Hurwitz 1902 (above) — Fourier coefficients on the lattice `1 + nℤ`.
- **Gauss, C. F., *Disquisitiones Arithmeticae*, 1801** — cyclotomic ladder and constructible polygon sufficiency; the algebraic-depth substrate.
- **Wantzel, P.-L., 1837** — necessity side of the Gauss–Wantzel constructibility criterion; supports the `n = 7` first non-constructible anchor.
- **Niven, I., 1956** — rational-cosine theorem; `τ(n)` zero set `{1, 2, 3, 4, 6}`.

### Cyclotomic-ladder unboundedness against affine flatness

- HJB 1985 §5 (above).
- **Bamberg, J., Cairns, G., and Kilminster, D., 2003** — crystallographic restriction `ψ` function; rotation orders compatible with Bravais lattices = `{1, 2, 3, 4, 6}`.

### Admissibility envelope

- **Lindemann, F., 1882** — the L–W boundary; transcendence of `π`.
- **Roth, K. F., 1954** — discrepancy lower bound (transcendence-free in content).
- **Roth, K. F., 1955** — rational approximations to algebraic numbers (distinct paper, same author, adjacent year; transcendence-class theorem).
- **Fortnow, L., 2000** — Kolmogorov complexity tools; universal semicomputable measure `μ(x) = 2^{−K(x)}` and Fact 6.2 universal dominance.
- **Aitchison, J., 1959** — density-side Fourier/Poisson expansion; adjacent K-H-L-A discrepancy-strut material.
- **Kuipers, L., and Niederreiter, H., 1974** — source for the Erdős–Turán / Erdős–Turán–Koksma discrepancy-sum apparatus used by the adjacent K-H-L-A branch.

## Proof-template precedent (§6)

- **`paper/LANDFALL-EXPORT.md`** *(in-program extract from Adam, Landfall)* — affine-closure template (Landfall §2), no-invariant-measure aggregation (Landfall §6, deploying the source content documented in `memos/BOWEN-DRILLING-AND-DENSITY.md`), finite-closure refusal (Landfall §7 via Gosper). Cited at §6 as the template the impossibility argument inherits.
- **Bowen, L. P.** *Density in Hyperbolic Spaces.* Ph.D. dissertation, University of Texas at Austin, 2002. — §2.3.1 no-`PSL(2, ℝ)`-invariant probability measure on the binary tiling space; §2.3.1 hole-drilling instability of density under arbitrarily small perturbations; §2.3.2 alternative no-invariant-measure construction via free-group action on a noncompact `H²`-covered surface. See `memos/BOWEN-DRILLING-AND-DENSITY.md` for the source-extraction brief; citation form lifted from Landfall.
- **Gosper, R. W., 1972** — continued-fraction arithmetic machine; cited as the negative anchor (exact computation in unbounded state, finite closure refused).
