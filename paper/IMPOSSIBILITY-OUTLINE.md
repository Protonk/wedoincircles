# Eff Eff Tee

>Meta instruction for humans and agents. Stage direction.

JACM is the venue. ~25 pages with figures is the target. The register is engineering inflected mathematics. Savoir faire is the goal.

## Abstract

We formulate the target theorem: current FFT-style lower-bound methods cannot improve past their existing thresholds on cyclotomic-DFT and adjacent compute-cost problems. We isolate the mult/add conversion underlying the FFT framework (Schönhage–Strassen 1971, Morgenstern 1973, Winograd 1978, Auslander–Feig–Winograd 1984) and assign it a transaction cost — the irreducible cost of trading multiplicative cost for additive cost or vice versa. The central bridge to earn is measure-theoretic: `δ = 0` must be shown to be the forbidden closure boundary, so native closure preservation and bounded drift are two readings of the same obstruction. With that bridge in place, a stronger FFT-style lower bound would require a frictionless conversion across the bounded/unbounded coefficient boundary, and the substrate it would operate on — rotation-orbit Diophantine kinematics under Haar measure, non-nesting isoperimetric registers across three measure-theoretic currencies, closed-form polygon arithmetic via `ζ(2)`-tail counting on Hurwitz-band decompositions, cyclotomic-ladder unboundedness against affine flatness as a counting-invariant asymmetry, and a Lebesgue null/full dichotomy under the L-W admissibility envelope — is organized to show that no such conversion is available under the admissible measures.

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

## §1. Cost, conversion, and defect

### §1.1. The accounting stack
Orientation: we use four nested objects — cost model, cost currencies, conversion strategies, and transaction cost `δ`. The cost model governs what is charged; the currencies say what is being counted; the conversion is the adaptive family of strategies trading one currency for another; `δ` is the cost object attached to that conversion. This section prevents `δ` from being treated as a synonym for the mult/add conversion.

### §1.2. Cost model: uniform-charge accounting
We work in a uniform-charge / logarithmic-measure cost model in the Cook-Reckhow / van Emde Boas sense, per `memos/COST-MODEL-UNIFORMITY-BRIEF.md`: bit growth is charged, advice / non-uniformity is handled by the regularity guard, and bare "uniform" is not allowed to mean Cook-Reckhow constant `l(n) = 1` / van Emde Boas uniform measure. Canon compatibility under variable precision remains construction debt #9.

### §1.3. Cost currencies
The two cost currencies are multiplicative cost `μ` and additive cost `α`. They are currencies inside the cost model of §1.2, not yet conversion strategies.

#### §1.3.1. Multiplicative cost
The cost-bearing primitives are multiplications; the complexity measure `μ` counts them under bilinear / rational-equivalence accounting. Schönhage–Strassen 1971, Winograd 1978, and Auslander–Feig–Winograd 1984 each give `μ` structure on cyclotomic-DFT and adjacent computations (full presentation at §3).

#### §1.3.2. Additive cost
The cost-bearing primitives are additions; the complexity measure `α` counts them, sensitive to the coefficient regime. Morgenstern 1973's `Ω(n log n)` bounded-coefficient additive lower bound is the canonical structure-bearing result (full presentation at §3.3). Ailon 2013 is the adjacent normalized-FFT comparison: in a layered `2 × 2` unitary-gate model, matrix entropy gives the same `Ω(n log n)` scale without determinant growth.

### §1.4. Coefficient regimes and the boundary
Bounded vs unbounded coefficients. The regime is a parameter of every cost measure on either side; many bounds — Morgenstern's notably — depend on which regime is in force. The bounded/unbounded coefficient boundary is the later measure-theoretic state space where `δ` is evaluated.

### §1.5. Conversion as adaptive strategy family
The mult/add conversion is the family of strategies FFT-style algorithms use to trade multiplicative cost for additive cost (or vice versa); methods select a strategy adaptively (Gauss 1805's `4×3` vs `3×4` for Pallas is the pre-1882 worked example, per `fft/GOLDSTINE-1977-INTERPOLATION-BRIEF.md`; deeper framing parked at `fft/FFT-SEARCH-PLAN.md`). The conversion is an adaptive strategy family closed under composition, not a single partial function.

### §1.6. Transaction cost `δ`: existence vs algebra
The conversion has a transaction cost `δ`: a non-zero quantity reflecting the irreducible cost of executing a strategy. Vocabulary and typing follow Coase 1937 (`measure/COASE-FRICTION-AND-SPECIALISTS.md`): the existence of friction (`δ > 0`) is one claim; the algebra of friction is another. Debt #2 lives here: additivity, amortization, asymptotics, per-size / per-precision behavior, representation dependence, and multi-route effects.

### §1.7. Candidate realization: phase-defect cocycle
A candidate concrete realization of `δ` is parked at `fft/PHASE-DEFECT.md`: `δ ≡ cost of {Δ_k} cocycle compression`. The formal composition law is at `fft/COCYCLE-COMPOSITION-LAW.md`; the closure/drift relation the candidate must satisfy is named at `measure/THE-FIRST-BRIDGE.md`. This is candidate machinery, not yet the definition of `δ`.

### §1.8. Threshold interface `T(P)`
For a problem `P`, the current threshold `T(P)` is the lower-bound frontier supplied by the canon (§4.4). Descent past `T(P)` means trading a higher cost-bearing bound for a lower one by reorganizing the computation. The Bridge claim (§6.2) asserts that descent past `T(P)` requires the boundary endpoint `δ = 0`.

Figure: [figures/cost_conversion_schematic.png](figures/cost_conversion_schematic.png) — the cost-pair `(μ, α)` plane with the actual frontier (canon thresholds Morgenstern, AFW, Winograd marked), the counterfactual `δ = 0` frontier (the endpoint §4 aims to rule out), the hatched `δ`-gap between them, and the Bridge equivalence `descent past T(P) ⟺ δ = 0 at boundary` (§6.2) shown as a double-headed vertical arrow at the bounded/unbounded coefficient boundary (§1.4). Bridge-side picture only; the closure-class story lives at §6.4–§6.5. Companion at [paper/code/COST-CONVERSION-SCHEMATIC.md](paper/code/COST-CONVERSION-SCHEMATIC.md).

## §2. The tour

Promissory. After §1 establishes language, §2 promises the route: cards on the table at §3, theorem at §4, the maze at §5, gradients at §6, back to the canon at §7. Names the substrate-side corpus (rotation-orbit Diophantine kinematics, non-nesting isoperimetric registers, closed-form polygon arithmetic, cyclotomic-ladder unboundedness against affine flatness, admissibility envelope) as the proof material §5 will deploy.

## §3. Cards on the table

### §3.1. The canon together
Frame: four sources, 1971–1984, define the FFT lower-bound apparatus we engage with.

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

#### §3.6.1. Translation into the §1 stack
We re-read §3.2–§3.5 through five coordinates: cost model / guard, cost currency, coefficient regime, conversion role, and `δ` status. This keeps theorem content separate from model vocabulary.

| Framework | Cost model / guard | Currency | Regime / boundary role | Conversion role | `δ` status |
|---|---|---|---|---|---|
| Schönhage–Strassen 1971 (§3.2) | Operational bit/gate discipline; used for model and composability, not as a lower-bound theorem | constructive FFT cost, adjacent to the multiplicative side | representation makes root multiplication cheap; not a bounded-coefficient lower-bound regime | shows a native recursive strategy family | no transaction-cost lower bound |
| Morgenstern 1973 (§3.3) | bounded-coefficient linear-composition setting | additive cost `α` | bounded side of §1.4; determinant potential binds only there | supplies the additive floor against which conversion is measured | no transfer to unbounded coefficients |
| Winograd 1978 (§3.4) | bilinear / rational-equivalence accounting | multiplicative cost `μ` | unbounded rational-equivalence side | CRT modular product gives the multiplicative ledger | no additive-floor transfer |
| Auslander–Feig–Winograd 1984 (§3.5) | rational-equivalence cyclotomic decomposition | multiplicative cost `μ` | unbounded cyclotomic side | factor-by-factor multiplicative accounting | no additive-floor transfer |

The §1.2 uniform-charge / logarithmic-measure guard is a program-side requirement placed over this canon re-read. Where a source does not itself formulate variable-precision charging, debt #9 is to check that the cited threshold survives the guard.

#### §3.6.2. What's structurally shared
The shared object is not a single theorem and not a free mult/add conversion. The shared structure is the stack: charged operations, cost currencies, a coefficient-regime boundary, strategy-family composition, and an unpaid transaction cost at the boundary.

Three of four sources sit on the multiplicative side; Morgenstern is the additive-side floor, and the only source here whose lower bound requires bounded coefficients. Schönhage–Strassen contributes operational model discipline and recursive FFT composability, but its headline result is an upper bound, not the threshold §4 tries to protect. Winograd and AFW give multiplicative ledgers on the unbounded / rational-equivalence side. None of the four source theorems transfers a bound across another source's coefficient regime or cost currency. Every such transfer is exactly what §1.6 calls `δ`, and §6 must prove that native FFT-style methods cannot make that payment vanish.

### §3.7. Adjacent restricted-model lower bound: Ailon 2013
Ailon records the warning we must keep visible: nontrivial Fourier-transform lower bounds in broad linear-circuit models remain open, and known successes come with strong restrictions. His model keeps only `n` live coordinates; each gate applies a `2 × 2` unitary mixing to two coordinates. The normalized FFT fits this model in `O(n log n)` gates, and Ailon proves any such circuit needs at least `(1/2)n log_2 n` gates.

The proof mechanism is the useful import. For a unitary matrix `M`, define `Phi(M) = -∑_{p,q} |M(p,q)|² log_2 |M(p,q)|²`. Then `Phi(Id)=0`, `Phi(F)=n log_2 n` for the normalized Fourier matrix, and one native `2 × 2` unitary gate can raise `Phi` by at most `2`. Program use: Ailon supplies an entropy-potential precedent at the same scale as Morgenstern's determinant-potential lower bound, but in a different restricted model. It is not a broad FFT lower bound and not a proof of the program's `δ`; it is evidence that native-operation restrictions can make a monotone potential carry the lower-bound load.

## §4. Main theorem

### §4.1. Frame
Preview in plain language: an impossibility theorem on FFT-style descent below existing lower-bound thresholds for cyclotomic-DFT and adjacent compute-cost problems. The formal version is at §4.5.

### §4.2. FFT-style methods
The hypothesis class. It is intentionally narrower than "all lower-bound methods": only methods built from the FFT canon's native operations, under the cost model and guard of §1.2, are in scope.

#### §4.2.1. Model and regularity guard
An in-scope method is charged in the uniform-charge / logarithmic-measure sense of §1.2. Operation cost, stored precision, coefficient size, precomputed tables, and size-dependent constants must be paid for at the same granularity. Advice strings, oracle constants, table-per-size shortcuts, and growing hidden state are outside the class unless their construction and storage costs are explicitly charged inside the method.

#### §4.2.2. Standard composability of the canon
The native operations and composition rules are those used by Schönhage–Strassen, Morgenstern, Winograd, and AFW (§3.2–§3.5): recursive FFT decomposition, CRT / tensor factorization, linear-composition closure, cyclotomic factor accounting, and coefficient-regime bookkeeping. The class is closed under these operations when the §4.2.1 guard is respected.

#### §4.2.3. The class defined
Formally: an FFT-style method is a uniformly described strategy family whose per-size methods are finite compositions of the native operations of §4.2.2, possibly with adaptive choices, charged under §4.2.1, and closed under composition (per §1.5's reading; see `fft/FFT-SEARCH-PLAN.md` for the Gauss 1805 anchor and the deeper search-theoretic framing). This is the formal object §4.5 quantifies over.

### §4.3. Cyclotomic-DFT and adjacent
The problem class. Cyclotomic-DFT specifically — the discrete Fourier transform over cyclotomic fields. "Adjacent" pinned down: compute-cost problems sharing §1's cost / conversion structure, differing in inputs but not in the cost / conversion framework the bounds inhabit.

### §4.4. Existing thresholds
The current best lower bounds the theorem asserts are unreachable from below. AFW's multiplicative-complexity threshold for cyclotomic DFTs under rational equivalence; Morgenstern's `Ω(n log n)` bounded-coefficient additive threshold; Winograd's modular-product threshold. Named precisely; cited to §3.

### §4.5. The theorem
Formal propositional statement. For every FFT-style method `M` (§4.2) and every problem `P` (§4.3), `M` does not prove a lower bound on `P` below the existing threshold `T(P)` of §4.4. Equivalently: no FFT-style descent below the current thresholds is reachable on this substrate.

### §4.6. Proof outline
Three load-bearing claims combine into a potential-style argument (per `paper/FIRST-PROOF.md`). **Bridge** (§6.2): threshold improvement requires crossing the defect gap from `δ > 0` to `δ = 0` at the boundary. **Separation** (§6.4): `δ = 0` lies outside the native closure class; the original Landfall §2 affine-closure template no longer transfers at cost level under extended `C_Aff`, so the live source-side obstruction is Landfall §4 plus effective Hermite-Lindemann at `n = 1`. **Native closure / drift** (§6.5): native operations preserve the admissible side and have bounded or non-crossing effect on `δ`. The relation between closure preservation and drift is the first measure-theoretic bridge named at `measure/THE-FIRST-BRIDGE.md`; §6.6 is conditional on earning it. Lemma A (§5.6 / §6.3) is the information-side parallel reading; not assumed by the QED. Proof-shape precedent: Ailon's matrix-entropy potential (§3.7), imported as shape, not content.

## §5. A maze of twisting passages, all alike

### §5.1. Rotation-orbit Diophantine kinematics
Arena: finite irrationality measure for `π` implies the Avila–Jitomirskaya parameter `β(π) = 0`, placing the orbit `{kπ mod 1}` in Weyl's equidistribution regime against Haar measure on `T = ℝ/ℤ`. No FFT-algorithm passage extracts a kinematic feature distinguishing one trade from another beyond the Haar mean for continuous and Riemann-integrable test functions. Source-side typing per `measure/SUBSTRATE-OBSTRUCTIONS.md` §1.

### §5.2. Non-nesting isoperimetric registers
Currencies: the three (rate, constant, almost-every) do not nest; no passage gets a free conversion between them. Constant register: Bonnesen-strengthening per Osserman 1979 / Bonnesen 1921. Almost-every register: Khintchine / Beck 1994 tradition. Source-side typing per `measure/SUBSTRATE-OBSTRUCTIONS.md` §2.

### §5.3. Closed-form polygon arithmetic
Values: Hurwitz coefficients (Fourier expansion on the sparse lattice `m ≡ 1 mod n`), gap `4π⁴/(3n²)`, and the first-band concentration constant `6/π² = 1/ζ(2)` (from the `ζ(2)`-tail comparison `B_j(n) ≤ B_1(n)/j²` per `corners/HURWITZ-FIRST-BAND-CONCENTRATION.md` §1) are fixed; descent reaches them only at threshold. Source-side typing per `measure/SUBSTRATE-OBSTRUCTIONS.md` §3. Figures: [figures/archimedean_triptych.png](figures/archimedean_triptych.png) sets up the inside-out / outside-out / strip substrate; [figures/hurwitz_gap_rate.png](figures/hurwitz_gap_rate.png) closes the Hurwitz identity at the `4π⁴/(3n²)` Archimedean rate (three series collapse to one line over seven decades); [figures/hurwitz_gap_frequency_decomposition.png](figures/hurwitz_gap_frequency_decomposition.png) shows the first-band concentration `B_1(n) ≥ (6/π²) Δ_n` directly as a stacked-area chart over `n`.

### §5.4. Cyclotomic-ladder unboundedness against affine flatness
Structure: the maximal real subfield `K_n^+ = ℚ(ζ_n + ζ_n^{−1})` has `[K_n^+ : ℚ] = φ(n)/2`, which grows unbounded with `n`; affine closure is flat; native operations cannot bridge the asymmetry. Source-side typing per `measure/SUBSTRATE-OBSTRUCTIONS.md` §4 (counting-invariant obstruction). Figure: [figures/pseudo_chebyshev_arithmetic_ladder.png](figures/pseudo_chebyshev_arithmetic_ladder.png) — degrees of `cos(π/n)` over ℚ as a stem chart, constructible nodes filled and non-constructible open, with `n = 7` highlighted as the first cubic and first non-constructible node.

### §5.5. The admissibility envelope
Audit: within L-W safety, closed-branch evidence, and the auxiliary-tool repertoire, no admissible method extracts additional descent information. The operative measure-theoretic fact within the envelope is the Lebesgue null/full dichotomy on `ℝ` (algebraics null; transcendentals full); finer distinctions among transcendentals trigger per-instance content-not-calendar audits per `memos/OLD-TIME-RELIGION.md`. Source-side typing per `measure/SUBSTRATE-OBSTRUCTIONS.md` §5.

### §5.6. Information-uniformity at the boundary
Synthesis target: once Lemma A's exhaustiveness debt closes, §5.1–§5.5 jointly establish that every admissible passage hits the bounded/unbounded coefficient boundary the same way. The result §6 would inherit.

## §6. Gradients without information

### §6.1. Descent in the cost / conversion framework
Setup: descent in §1's framework means trading a higher cost-bearing complexity bound for a lower one by reorganizing the underlying computation. Lower-bound improvement *is* successful descent. The proof asks whether such descent is reachable by FFT-style methods past `T(P)`.

### §6.2. Bridge claim: threshold improvement requires crossing the defect gap
For descent past `T(P)` to succeed, the algorithm must drive `δ` at the bounded/unbounded coefficient boundary from positive to zero — equivalently, cross the defect gap. The Bridge claim asserts this equivalence: threshold improvement *is* gap-crossing. Endpoint-side claim of the potential-style interface (`paper/FIRST-PROOF.md`). The companion bridge at `measure/THE-FIRST-BRIDGE.md` relates the defect coordinate to the closure boundary: `δ = 0` must be shown to be the forbidden closure endpoint, not merely a small potential value. Central new theorem of the program. **[Construction debt #1.]**

### §6.3. Lemma A inherited (parallel reading)
Conditional on §5.6's exhaustiveness argument, no FFT-algorithm passage extracts information distinguishing one trade from another at the boundary. Under `BNHA/hakamada/MEASURE-TWICE.md`'s discipline this is the **substrate-side measure-theoretic refusal** — the substrate's five measures (per `measure/SUBSTRATE-OBSTRUCTIONS.md`) jointly refuse the distinguishing information descent would need. The closure route of §6.4–§6.5 is the complementary **algorithm-side measure-theoretic refusal**; together they form a measure-theoretic squeeze on `T(P)` (per `paper/FIRST-PROOF.md` debt #6, re-framed as squeeze convergence rather than logical equivalence). *Lemma A is not used in the QED*; the QED closes via the closure route alone, with the Bridge claim's equivalence between threshold improvement and gap-crossing supplying sufficiency. Lemma A's exhaustiveness debt (#5) governs the substrate-side half independently.

### §6.4. Separation claim: `δ = 0` outside the native closure class
The Separation claim restates the proof template for the cost / conversion framework: `δ = 0` lies outside the closure of native operations. Landfall §2 supplies the original affine-closure template, but it does not transfer at cost level under extended `C_Aff` (per `fft/LANDFALL-EXTENDED-CAFF-TRANSFER.md`). The live source-side obstruction is Landfall §4 plus effective Hermite-Lindemann at `n = 1`: `ε` must carry a per-sample lower bound at variable precision under the uniform-charge model. Target-side: prove a transport lemma carrying that source-side cost obstruction to `δ = 0 ∉ C_FFT`. Candidate transport: the **character reflection barrier** of `fft/PHASE-DEFECT.md`, with **phase-lift conservativity** as its analytic-exponential specialization. Target-side claim of the potential-style interface. **[Construction debt #3.]**

### §6.5. Native closure / drift claim
Each native operation preserves the admissible closure side and has bounded (or non-crossing) effect on the defect potential `δ` at the boundary. Mult-side primitives of §1.3.1 compose into a closure class; add-side primitives of §1.3.2 compose into another closure class; no single native operation realizes the zero-defect endpoint. The proof must not silently identify closure preservation with bounded drift. `measure/THE-FIRST-BRIDGE.md` names the missing relation: `δ` must be a faithful measurable coordinate for membership/non-membership in `C_FFT`, so the closure statement and drift statement become two readings of the same invariant. Step-side claim of the potential-style interface. **[Construction debt #4, tied to #1 and #3.]**

Figure: [figures/delta_phase_plot.png](figures/delta_phase_plot.png) — the closure-class picture in algebraic-phase space (amortization rate, asymptotic floor). Above the working-floor line `δ_min`: the IMPOSSIBILITY region (native closure of mult/add primitives). Below the foreclosed strip: the FFT canon's claimed territory at `floor = 0`, targeted as unreachable by finite composition once the bridge closes. The horizontal mustard band straddling the working floor is debt #2 in the open: where `δ_min` actually sits depends on the algebra of `δ`. Companion at [paper/code/COASE-PHASE.md](paper/code/COASE-PHASE.md).

Proof-shape precedent: Ailon 2013 (§3.7) demonstrates the potential-style argument in a restricted unitary model — endpoint values `Φ(Id) = 0`, `Φ(F) = n log₂ n`, per-gate drift `ΔΦ ≤ 2`, conclusion `m ≥ (n log₂ n)/2`. The program imports the *shape*, not the content: `δ` is the potential, the bounded/unbounded coefficient boundary is the gap locus, the FFT canon's native operations are the steps. Ailon's matrix-entropy machinery does not enter; only the three-claim skeleton does. Trust-boundary discipline per `fft/AILON-2013-UNITARY-FFT-LOWER-BOUND-BRIEF.md` §4.

### §6.6. Compose the three claims; QED
Compose Bridge + Separation + Native closure / drift, conditional on the first bridge of `measure/THE-FIRST-BRIDGE.md`. Descent past `T(P)` requires crossing the defect gap (Bridge). The target `δ = 0` lies outside the native closure class once the source-side cost obstruction is transported (Separation). Native operations preserve the admissible side and do not realize the zero-defect endpoint (Native closure / drift). Therefore no finite FFT-style composition reaches the endpoint while staying inside the admissible closure class. No FFT-style descent below current thresholds is reachable on this substrate. A smarter FFT-style method does not answer the impossibility — same cost measures, same native operations, same closure classes, same `δ` at the boundary. The mathematical non-elimination claim is the bridged closure / drift invariant — the existence-side claim of §1.6, with the algebra-side held open at debt #2. Coase 1937 (`measure/COASE-FRICTION-AND-SPECIALISTS.md`) supplies the vocabulary (*reduce yes, eliminate no*) for naming what the lemma rules out. The obstruction is structural, not in algorithmic cleverness. QED for §4 once the three-claim interface and bridge are earned.

*Meta-claim (FIRST-PROOF debt #6, re-framed as squeeze convergence).* Originally, debt #6 sought a logical equivalence between substrate-side refusal (Lemma A, §6.3) and algorithm-side refusal (Bridge + Separation + Native closure / drift, §6.2 / §6.4 / §6.5). We re-frame the relationship as **squeeze convergence**: the bound `T(P)` is structurally real because every algorithm-side framework reaches it via a measure-theoretic argument (the canon's `Ω(n log n)` cluster, each in its own measure: Lebesgue / counting / dimension / Shannon entropy / bit-counting) and every substrate-side angle refuses descent under a different measure-theoretic argument (the five §5 obstructions: Haar / three isoperimetric registers / `ζ(2)`-tail counting / counting-invariant on extensions / Lebesgue null-full). The two sides converge on `T(P)` from different cost-currencies; the convergence is the structural fact, not an artifact of any one framework, and not the logical equivalence the original debt sought. Substrate-side typing per `measure/SUBSTRATE-OBSTRUCTIONS.md`; methodological character per `BNHA/hakamada/MEASURE-TWICE.md`.

### §6.7. Construction-debt accounting

The nine debts of `paper/FIRST-PROOF.md` mapped to outline location and current status. Status taxonomy: **load-bearing for QED** (the three-claim interface), **foundational** (gates the others), **parallel-reading** (Lemma A's status; not used in QED), **methodological** (per-citation discipline). The "Do not re-claim" column is part of the accounting.

| # | Name | Outline location | Status | Note | Do not re-claim |
|---|---|---|---|---|---|
| 1 | Bridge Theorem | §6.2 `[Construction debt #1]` | Load-bearing (QED) | Equivalence between threshold improvement and gap-crossing; central new theorem | Gap-crossing is not proved by drift or separation alone. |
| 2 | Cost / conversion formalization (algebra of `δ`) | §1.1, §1.3–§1.8, §6.6 | Foundational; gates #1, #3, #4 | `μ`, additive cost, strategy-family conversion, `δ` algebra; closes the impossibility *region*, vs Lemma B alone closing the §4.5 *statement* | Advice / non-uniformity belongs under #9's regularity guard, not the algebra of `δ`. |
| 3 | Template transfer (Separation) | §6.4 `[Construction debt #3]` | Load-bearing (QED) | Current source-side obstruction is Landfall §4 + effective H-L at `n = 1`, transported to `δ = 0 ∉ C_FFT` via character reflection / phase-lift conservativity | Do not use Landfall §2 non-affineness (`ε ∉ Aff⁺(ℝ)`) as the live cost-level obstruction. |
| 4 | Lemma B native closure / drift | §6.5 `[Construction debt #4]` | Load-bearing (QED) | Mult-side, add-side, no-zero-endpoint; closure preservation and drift are bridged by `measure/THE-FIRST-BRIDGE.md` | Do not say bounded drift alone proves non-reachability. |
| 5 | Lemma A's exhaustiveness | §6.3 (parenthetical) | Parallel-reading (not QED) | Five substrate-side angles must cover every admissible distinguishing-information source | The five witnesses are not yet a universal covering theorem. |
| 6 | A and B as squeeze halves | §6.3, §6.6 (meta-claim) | Parallel-reading; meta-claim | Articulates squeeze convergence on `T(P)`; rigorous `A ⟺ B` no longer required | Do not re-claim logical equivalence between Lemma A and the closure route. |
| 7 | Trust-boundary discipline | §3, §6, References (per-source) | Methodological | Each canon citation respects `fft/PROVENANCE-AND-TRANSFERABILITY.md`'s "should be cited for / should NOT be cited for" boundaries | Do not transfer theorem content from vocabulary or methodological precedents. |
| 8 | `β(π) = 0` L-W audit | §5.1 | Parallel-reading; **discharged** | Audited at [rotations/BETA-PI-LW-AUDIT.md](rotations/BETA-PI-LW-AUDIT.md): chain `finite μ(π) ⟹ β(π) = 0` is L-W-safe in content (Mahler 1953 / Hata 1993 / Salikhov 2008 are Hermite-Padé; CF implication is pre-1882) | Do not re-import `β(π) = 0` into a QED-bearing slot — Lemma A is parallel-reading. |
| 9 | Uniform-charge cost model and canon re-read | §1.2, §6.4, §6.6 | Foundational | Methodological commitment set; canon re-read and effective H-L cost-form consumption remain open | Do not say canon compatibility or the effective H-L cost form is discharged; do not conflate uniform-charge with constant-cost uniform measure. |

Pay-down status as of this revision: #1, #3, #4 are named and located but not earned; #2's `δ` algebra is parked per Coase precedent; #3 now uses Landfall §4 + effective H-L rather than Landfall §2 at cost level; #4 is bridged to closure via `measure/THE-FIRST-BRIDGE.md`; #6 is re-framed from logical-equivalence to squeeze convergence; #9 is added as the cost-model / canon-reread foundation.

## §7. Back again

Return to the four frameworks of §3 after the theorem closes. Schönhage–Strassen, Morgenstern, Winograd, AFW are then read as sitting at their natural limits — not from defect, but because no further descent is reachable on this substrate by these methods. Pair with the algebraic-side closure-mismatch reading (`memos/NATIVE-F-MINIMAL-DEFINITION.md`): the operational-side and algebraic-side companions complete each other. Figure re-reference: [figures/native_f_closure_mismatch.png](figures/native_f_closure_mismatch.png) — the §Intro panel re-read after the impossibility theorem closes; the closure-depth contrast is the structural payoff, not the setup.

## §Conclusion

Coda. What's named, what's left as future work: the cost / conversion map at higher resolution; non-FFT lower-bound methods; the K-H-L-A discrepancy strut as adjacent program. Operational-observable companion figure: [figures/counting_psi_stratification.png](figures/counting_psi_stratification.png) — the ψ(n)-stratified outside-out sweep-x-support over `n ∈ [3, 40]`, localizing the algebraic-depth discontinuity at `n = 7` through ψ classes (Bravais ψ = 2 backbone vs first cubic ψ = 6). The algebraic-side `n = 7` first-cubic anchor of [figures/native_f_closure_mismatch.png](figures/native_f_closure_mismatch.png) shows up here in the operational-observable register. The compute-cost branch (`memos/LEDGER-PIVOT-SEARCH.md`, `fft/FOUR-FRAMEWORK-SYNTHESIS.md`) searches for the cost-theorem that converts this stratification into a primitive-op floor.

*Pencil mark for prose pass.* The non-FFT vector-field question is well-posed and sharpened by the manifold framing — *is there a non-FFT vector field that crosses the discontinuity?* Point to `memos/NATIVE-F-MINIMAL-DEFINITION.md` as the place where a different vector field is considered (the algebraic-side companion is the natural home for that question). Clean handoff, not vague future work.

# Figures

Eight figures, theorem-paired, each with an alt-text-ready companion document. All figures live at `figures/`; build scripts and companion documents per the table below.

| Figure | Build script | Companion document | Section |
|---|---|---|---|
| [figures/native_f_closure_mismatch.png](figures/native_f_closure_mismatch.png) | [memos/build_native_f_closure_mismatch.py](memos/build_native_f_closure_mismatch.py) | [memos/NATIVE-F-MINIMAL-DEFINITION.md](memos/NATIVE-F-MINIMAL-DEFINITION.md) | §Intro, §7 |
| [figures/cost_conversion_schematic.png](figures/cost_conversion_schematic.png) | [paper/code/build_cost_conversion_schematic.py](paper/code/build_cost_conversion_schematic.py) | [paper/code/COST-CONVERSION-SCHEMATIC.md](paper/code/COST-CONVERSION-SCHEMATIC.md) | §1.8 |
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

- **Schönhage, A., and Strassen, V., 1971** — operational uniform model; cited at §1 (cost-model / cost-currency setup) and §3 (best light + avoidance: not a lower-bound source).
- **Morgenstern, J., 1973** — bounded-coefficient additive lower bound; cited at §1, §3, §6 (the floor that turns out to be unreachable from below).
- **Winograd, S., 1978** — modular-product theorem `μ(T_P) = 2n − k` and CRT-cyclotomic factor ledger; cited at §1, §3.
- **Auslander, L., Feig, E., and Winograd, S., 1984** — cyclotomic decomposition under rational equivalence; cited at §1, §3.
- **`fft/FFT-COMPLEXITY-ARTICULATION.md`** *(in-program extract)* — proof-template and trust-boundary index for the four FFT frameworks.
- **Goldstine, H. H., 1977** — *A History of Numerical Analysis from the 16th Through the 19th Century*, §4.12–13. Pre-1882 anchor for the FFT-as-adaptive-search reading: Gauss 1805's divide-and-conquer interpolation engine, with the Pallas worked example (`4×3` vs `3×4`) chosen on practical grounds rather than asymptotic ones. Source-extraction at `fft/GOLDSTINE-1977-INTERPOLATION-BRIEF.md`; deeper framing parked at `fft/FFT-SEARCH-PLAN.md`. Cited at §1.5, §4.2, and (potentially) §3 / §7.

## Adjacent FFT lower-bound prior art (§3.7)

- **Ailon, N., 2013** — `Ω(n log n)` lower bound for the normalized Fourier transform in a layered `2 × 2` unitary-gate model, proved by a matrix-entropy potential; cited for the survey warning that broad linear-circuit Fourier lower bounds remain open and for the restricted-model entropy-potential precedent. Source-extraction at `fft/AILON-2013-UNITARY-FFT-LOWER-BOUND-BRIEF.md`.

## Cost / conversion framework anchor (§1)

- **Coase, R. H., 1937** — "The Nature of the Firm," *Economica* New Series Vol. 4 No. 16 (Nov. 1937), pp. 386–405. PDF at [sources/Coase-1937.pdf](sources/Coase-1937.pdf). Source for the transaction-cost framework adopted at §1.6 and §6: trade through any coordination mechanism carries a non-zero, irreducible fee, and the *algebra* of that fee — additivity across compositions, amortization across repeated uses, scale-behavior, representation-dependence, bypass-resistance under specialist intermediation, and heterogeneity across transaction types — determines what the framework lets one prove. Coase's distinction between the existence of friction (p. 390: "there is a cost of using the price mechanism") and its algebra (p. 395 marginal condition; p. 396 the firm-size determination "(a) the less the costs of organising and the slower these costs rise with an increase in the transactions organised") is the methodological precedent for FIRST-PROOF debt #2 (algebra of `δ` left open with named open sub-questions). Cited at §1.6 (transaction-cost vocabulary and irreducible-fee framing), §6.5 (closure / drift invariant, with full algebra of `δ` deferred per debt #2), and (potentially) §Conclusion as the methodological-framework reference.
- **Cook, S. A., and Reckhow, R. A., 1973** — RAM charging-granularity vocabulary via the `l(n)` function; cited for logarithmic charging, not for FFT lower-bound content.
- **Slot, C., and van Emde Boas, P., 1984; van Emde Boas, P., 1988/1990** — Invariance Thesis / First Machine Class methodological precedent for model-independent reasonable charging; cited as thesis-level discipline, not theorem transfer.
- **`memos/COST-MODEL-UNIFORMITY-BRIEF.md`** *(in-program extract)* — paired brief on Cook-Reckhow and van Emde Boas; cited for the terminology guard that the program's "uniform-charge" is logarithmic-measure charging, not Cook-Reckhow constant `l(n) = 1` / van Emde Boas uniform measure.

## Algebraic-side material

- **Heideman, M. T., Johnson, D. H., and Burrus, C. S., 1985, §5** — eigenspace decomposition `Q(ζ_n) = K_n ⊕ K_n · 2i sin(2π/n)` under `σ_{−1}`, forcing `K_n` as the multiplicatively-closed half; cited at §1, §6.
- **`memos/NATIVE-F-MINIMAL-DEFINITION.md`** *(in-program companion)* — closure-mismatch theorem (no functor `F` preserves closure-depth from `Aff⁺(ℝ)` to `{K_n}`); cited at §Intro and §7 as the algebraic-side companion.

## Substrate-side sources (§5)

- **`paper/MEASURE-THEORETIC-OBSTRUCTIONS.md`** *(paper-level pointer)* — routes the paper reader to the measure package and states the trust boundary: substrate-side refusals are support for Lemma A, not proof of the bridge or final impossibility.
- **`measure/SUBSTRATE-OBSTRUCTIONS.md`** *(detailed measure catalogue)* — substrate-side measure-theoretic typing of the five §5 angles: Haar measure on `T = ℝ/ℤ` for §5.1; non-nesting of three measure-theoretic registers (rate / constant / almost-every) for §5.2; `ζ(2)`-tail comparison and Hurwitz Fourier expansion for §5.3; ℚ-vector-space dimension as counting-invariant obstruction for §5.4; Lebesgue null/full dichotomy under L-W safety for §5.5. Cited at §5.1–§5.5 as the source-side typing layer.

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

- **`measure/THE-FIRST-BRIDGE.md`** *(in-program bridge memo)* — names the relation we must prove between closure preservation and drift: `δ = 0` must be a faithful measurable coordinate for the forbidden closure boundary.
- **`paper/LANDFALL-EXPORT.md`** *(paper-level pointer)* — routes the paper reader to the Landfall inheritance map and states the trust boundary.
- **`fft/LANDFALL-PROOF-TEMPLATES.md`** *(detailed template map)* — original affine-closure template (Landfall §2), no-invariant-measure aggregation (Landfall §6, deploying the source content documented in `memos/BOWEN-DRILLING-AND-DENSITY.md`), finite-closure refusal (Landfall §7 via Gosper). Cited at §6 as the historical template, not as the live cost-level obstruction.
- **`fft/LANDFALL-EXTENDED-CAFF-TRANSFER.md`** *(in-program audit)* — explains why Landfall §2 does not transfer at cost level under extended `C_Aff` and why the source-side obstruction shifts to Landfall §4 plus effective H-L at `n = 1`.
- **`memos/EFFECTIVE-HL-N1-COST-FORM.md`** *(in-program target form)* — states the per-sample lower-bound shape the live source-side obstruction must supply at variable precision.
- **`fft/PHASE-DEFECT.md`** *(in-program candidate machinery)* — phase-defect cocycle `{Δ_k}`, character reflection barrier, and phase-lift conservativity as the candidate transport from source-side `ε` cost obstruction to FFT-side `δ`.
- **Bowen, L. P.** *Density in Hyperbolic Spaces.* Ph.D. dissertation, University of Texas at Austin, 2002. — §2.3.1 no-`PSL(2, ℝ)`-invariant probability measure on the binary tiling space; §2.3.1 hole-drilling instability of density under arbitrarily small perturbations; §2.3.2 alternative no-invariant-measure construction via free-group action on a noncompact `H²`-covered surface. See `memos/BOWEN-DRILLING-AND-DENSITY.md` for the source-extraction brief; citation form lifted from Landfall.
- **Gosper, R. W., 1972** — continued-fraction arithmetic machine; cited as the negative anchor (exact computation in unbounded state, finite closure refused).
