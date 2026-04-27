# Eff Eff Tee

>Meta instruction for humans and agents. Stage direction.

JACM is the venue. ~25 pages with figures is the target. The register is engineering inflected mathematics. Savoir faire is the goal.

## Abstract

We prove that current FFT-style lower-bound methods cannot improve past their existing thresholds on cyclotomic-DFT and adjacent compute-cost problems. The mult/add conversion underlying the FFT framework (Schönhage–Strassen 1971, Morgenstern 1973, Winograd 1978, Auslander–Feig–Winograd 1984) carries a transaction cost — the irreducible cost of trading multiplicative cost for additive cost or vice versa — that is bounded away from zero at the bounded/unbounded coefficient boundary. A stronger FFT-style lower bound would require a frictionless conversion across that boundary, and the substrate it would operate on — rotation-orbit Diophantine kinematics, non-nesting isoperimetric registers, closed-form polygon arithmetic, and cyclotomic-ladder unboundedness against affine flatness — supplies no such conversion.

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
The cost-bearing primitives are additions; the complexity measure counts them, sensitive to the coefficient regime. Morgenstern 1973's `Ω(n log n)` bounded-coefficient additive lower bound is the canonical structure-bearing result (full presentation at §3.3).

### §1.4. Coefficient regimes
Bounded vs unbounded coefficients. The regime is a parameter of every cost measure on either side; many bounds — Morgenstern's notably — depend on which regime is in force. `δ` (§1.5) also depends on regime.

### §1.5. The mult/add conversion
The family of strategies FFT-style algorithms use to trade multiplicative cost for additive cost (or vice versa); methods select a strategy adaptively (Gauss 1805's `4×3` vs `3×4` for Pallas is the pre-1882 worked example, per `fft/GOLDSTINE-1977-INTERPOLATION-BRIEF.md`; deeper framing parked at `paper/FFT-SEARCH-PLAN.md`). The transaction cost `δ` — the irreducible cost of executing a strategy — depends on §1.4's regime parameter; `δ`'s behavior at the bounded/unbounded coefficient boundary is the object §4's main theorem speaks about.

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

### §3.6. Common manifolds
What do the four attacks share in the language of cost manifolds we just introduced?

#### §3.6.1. Translation
Each of §3.2–§3.5 re-read in cost-manifold language. SS's operational uniform model as a structure on the multiplicative manifold; Morgenstern's bound as the additive-manifold floor; Winograd's modular product as a CRT-factored ledger on the multiplicative side; AFW's cyclotomic decomposition as a factor-by-factor reading on the multiplicative side.

#### §3.6.2. What's structurally shared
The four manifold-language readings converge on common structure: shared cost-bearing primitives, compatible composability, shared regime parameter, one mult/add conversion map between the same two manifolds.

## §4. Main theorem

### §4.1. Frame
Preview in plain language: an impossibility theorem on FFT-style descent below existing lower-bound thresholds for cyclotomic-DFT and adjacent compute-cost problems. The formal version is at §4.5.

### §4.2. FFT-style methods
The hypothesis class.

#### §4.2.1. Standard composability of the canon
The composability rules used by Schönhage–Strassen, Morgenstern, Winograd, and AFW (§3.2–§3.5). The class is closed under these.

#### §4.2.2. The class defined
Formally: an FFT-style method is a finite composition of native operations under the standard composability of the canon — equivalently, an adaptive strategy family closed under composition (per §1.5's reading; see `paper/FFT-SEARCH-PLAN.md` for the Gauss 1805 anchor and the deeper search-theoretic framing). This is the formal object §4.5 quantifies over.

### §4.3. Cyclotomic-DFT and adjacent
The problem class. Cyclotomic-DFT specifically — the discrete Fourier transform over cyclotomic fields. "Adjacent" pinned down: compute-cost problems sharing the cost-manifold structure of §1, differing in inputs but not in the manifold the bounds inhabit.

### §4.4. Existing thresholds
The current best lower bounds the theorem asserts are unreachable from below. AFW's multiplicative-complexity threshold for cyclotomic DFTs under rational equivalence; Morgenstern's `Ω(n log n)` bounded-coefficient additive threshold; Winograd's modular-product threshold. Named precisely; cited to §3.

### §4.5. The theorem
Formal propositional statement. For every FFT-style method `M` (§4.2) and every problem `P` (§4.3), `M` does not prove a lower bound on `P` below the existing threshold `T(P)` of §4.4. Equivalently: no FFT-style descent below the current thresholds is reachable on this substrate.

### §4.6. Proof outline
Two load-bearing ingredients. §5.6: information-uniformity at the boundary. §6.5: native operations have closed composition. Composed via the affine-closure template inherited from Landfall §2 (extracted at `paper/LANDFALL-EXPORT.md`). §5 and §6 carry the load; §4.6 names the route.

## §5. A maze of twisting passages, all alike

### §5.1. Rotation-orbit Diophantine kinematics
Arena: orbit data carries `β(π) = 0`; no FFT-algorithm passage finds a kinematic feature distinguishing itself from another.

### §5.2. Non-nesting isoperimetric registers
Currencies: the three (rate, constant, almost-every) do not nest; no passage gets a free conversion between them.

### §5.3. Closed-form polygon arithmetic
Values: Hurwitz coefficients, gap `4π⁴/(3n²)`, and the sharp constant `6/π² = 1/ζ(2)` are fixed; descent reaches them only at threshold. Figures: [figures/archimedean_triptych.png](figures/archimedean_triptych.png) sets up the inside-out / outside-out / strip substrate; [figures/hurwitz_gap_rate.png](figures/hurwitz_gap_rate.png) closes the Hurwitz identity at the `4π⁴/(3n²)` Archimedean rate (three series collapse to one line over seven decades); [figures/hurwitz_gap_frequency_decomposition.png](figures/hurwitz_gap_frequency_decomposition.png) shows the first-band concentration `B_1(n) ≥ (6/π²) Δ_n` directly as a stacked-area chart over `n`.

### §5.4. Cyclotomic-ladder unboundedness against affine flatness
Structure: `[K_n : ℚ] = φ(n)/2` grows unbounded with `n`; affine closure is flat; native operations cannot bridge the asymmetry. Figure: [figures/pseudo_chebyshev_arithmetic_ladder.png](figures/pseudo_chebyshev_arithmetic_ladder.png) — degrees of `cos(π/n)` over ℚ as a stem chart, constructible nodes filled and non-constructible open, with `n = 7` highlighted as the first cubic and first non-constructible node.

### §5.5. The admissibility envelope
Audit: within L-W safety, closed-branch evidence, and the auxiliary-tool repertoire, no admissible method extracts additional descent information.

### §5.6. Information-uniformity at the boundary
Synthesis: §5.1–§5.5 jointly establish that every passage hits the bounded/unbounded coefficient boundary the same way. The result §6 inherits.

## §6. Gradients without information

### §6.1. Gradient descent on the cost manifold
Setup: descent on the cost manifold means trading a higher cost-bearing complexity bound for a lower one by reorganizing the underlying computation. Lower-bound improvement *is* successful descent. Frame the problem in §1's language.

### §6.2. What descent requires
For descent to succeed at the boundary in §1.5's conversion, the algorithm must extract information distinguishing one strategy from another. Without distinguishing information, descent is undirected.

### §6.3. §5.6 inherited
§5.6 establishes information-uniformity at the boundary. The substrate refuses to provide what §6.2 says descent needs.

### §6.4. The affine-closure template (Landfall §2)
The proof template extracted at `paper/LANDFALL-EXPORT.md`, restated for the cost / conversion framework: no finite composition of native operations produces an effect outside the operations' closure class. The argument's shape is structural; it does not depend on the specific cost-bearing primitives.

### §6.5. Native operations have closed composition
Apply the template to our setting.

#### §6.5.1. Multiplicative-side and additive-side closure
The multiplicative-side primitives of §1.2 compose into a closure class bounded by §1.4's regime parameters. Composition stays inside. The additive-side primitives of §1.3 compose into another closure class. Composition stays inside.

#### §6.5.2. Discontinuity outside both classes
At the bounded/unbounded coefficient boundary, `δ` (§1.5) is non-zero — outside both closure classes' reach. No finite composition of native operations reduces it to zero. This is the closure-class observation §6.6 composes with §6.3.

### §6.6. No descent route exists; QED
Compose §6.3 + §6.5: descent has no distinguishing information; native operations don't compose into a route across the discontinuity. No FFT-style descent below current thresholds is reachable on this substrate. A smarter FFT-style method does not answer the impossibility — it lives in the same tangent space, which is what lacks a descent direction. The obstruction is in the geometry, not in algorithmic cleverness. QED for §4.

## §7. Back again

Return to the four frameworks of §3, now under the impossibility. Schönhage–Strassen, Morgenstern, Winograd, AFW are at their natural limits — not from defect, but because no further descent is reachable on this substrate by these methods. Pair with the algebraic-side closure-mismatch reading (`memos/NATIVE-F-MINIMAL-DEFINITION.md`): the operational-side and algebraic-side companions complete each other. Figure re-reference: [figures/native_f_closure_mismatch.png](figures/native_f_closure_mismatch.png) — the §Intro panel re-read after the impossibility theorem closes; the closure-depth contrast is the structural payoff, not the setup.

## §Conclusion

Coda. What's named, what's left as future work: the cost-manifold map at higher resolution; non-FFT lower-bound methods; the K-H-L-A discrepancy strut as adjacent program. Operational-observable companion figure: [figures/counting_psi_stratification.png](figures/counting_psi_stratification.png) — the ψ(n)-stratified outside-out sweep-x-support over `n ∈ [3, 40]`, localizing the algebraic-depth discontinuity at `n = 7` through ψ classes (Bravais ψ = 2 backbone vs first cubic ψ = 6). The algebraic-side `n = 7` first-cubic anchor of [figures/native_f_closure_mismatch.png](figures/native_f_closure_mismatch.png) shows up here in the operational-observable register. The compute-cost branch (`memos/LEDGER-PIVOT-SEARCH.md`, `fft/FOUR-FRAMEWORK-SYNTHESIS.md`) searches for the cost-theorem that converts this stratification into a primitive-op floor.

*Pencil mark for prose pass.* The non-FFT vector-field question is well-posed and sharpened by the manifold framing — *is there a non-FFT vector field that crosses the discontinuity?* Point to `memos/NATIVE-F-MINIMAL-DEFINITION.md` as the place where a different vector field is considered (the algebraic-side companion is the natural home for that question). Clean handoff, not vague future work.

# Figures

Six figures, theorem-paired, each with an alt-text-ready companion document. All figures live at `figures/`; build scripts and companion documents per the table below.

| Figure | Build script | Companion document | Section |
|---|---|---|---|
| [figures/native_f_closure_mismatch.png](figures/native_f_closure_mismatch.png) | [memos/build_native_f_closure_mismatch.py](memos/build_native_f_closure_mismatch.py) | [memos/NATIVE-F-MINIMAL-DEFINITION.md](memos/NATIVE-F-MINIMAL-DEFINITION.md) | §Intro, §7 |
| [figures/archimedean_triptych.png](figures/archimedean_triptych.png) | [n-gons/build_archimedean_triptych.py](n-gons/build_archimedean_triptych.py) | [n-gons/ARCHIMEDEAN-STRIP-FLIP.md](n-gons/ARCHIMEDEAN-STRIP-FLIP.md) | §5.3 |
| [figures/hurwitz_gap_rate.png](figures/hurwitz_gap_rate.png) | [corners/hurwitz_gap.sage](corners/hurwitz_gap.sage) | [corners/HURWITZ-GAP.md](corners/HURWITZ-GAP.md) | §5.3 |
| [figures/hurwitz_gap_frequency_decomposition.png](figures/hurwitz_gap_frequency_decomposition.png) | [corners/hurwitz_gap.sage](corners/hurwitz_gap.sage) | [corners/HURWITZ-FIRST-BAND-CONCENTRATION.md](corners/HURWITZ-FIRST-BAND-CONCENTRATION.md) | §5.3 |
| [figures/pseudo_chebyshev_arithmetic_ladder.png](figures/pseudo_chebyshev_arithmetic_ladder.png) | [corners/pseudo_chebyshev_arithmetic_ladder.sage](corners/pseudo_chebyshev_arithmetic_ladder.sage) | [corners/PSEUDO-CHEBYSHEV-NODES.md](corners/PSEUDO-CHEBYSHEV-NODES.md) | §5.4 |
| [figures/counting_psi_stratification.png](figures/counting_psi_stratification.png) | [n-gons/counting/build_psi_stratification.py](n-gons/counting/build_psi_stratification.py) | [n-gons/counting/PSI-STRATIFICATION.md](n-gons/counting/PSI-STRATIFICATION.md) | §Conclusion |

Gaps the prose pass will identify a need for but the repo does not yet have: §1.5 cost-manifold conversion schematic (bounded↔unbounded coefficient boundary as discontinuity); §3 four-frameworks comparison (probably better as a table); §6.5 closure-class / tangent-bundle picture (discontinuity outside both closure classes). Each is a schematic to be drawn during the prose pass, not extracted from existing repo material.

---

# References

> Provenance discipline per `BNHA/ONE-FOR-ALL.md`: every load-bearing tool below names the chain it inherits from, and is staged for the next reader to pick up without reconstructing context. Working entries; bibliographic data refined per pass.

## Primary engagement — the four FFT frameworks (§3, §7)

- **Schönhage, A., and Strassen, V., 1971** — operational uniform model; cited at §1 (cost-manifold definition) and §3 (best light + avoidance: not a lower-bound source).
- **Morgenstern, J., 1973** — bounded-coefficient additive lower bound; cited at §1, §3, §6 (the floor that turns out to be unreachable from below).
- **Winograd, S., 1978** — modular-product theorem `μ(T_P) = 2n − k` and CRT-cyclotomic factor ledger; cited at §1, §3.
- **Auslander, L., Feig, E., and Winograd, S., 1984** — cyclotomic decomposition under rational equivalence; cited at §1, §3.
- **`paper/FFT-COMPLEXITY-ARTICULATION.md`** *(in-program extract)* — proof-template and trust-boundary index for the four FFT frameworks.
- **Goldstine, H. H., 1977** — *A History of Numerical Analysis from the 16th Through the 19th Century*, §4.12–13. Pre-1882 anchor for the FFT-as-adaptive-search reading: Gauss 1805's divide-and-conquer interpolation engine, with the Pallas worked example (`4×3` vs `3×4`) chosen on practical grounds rather than asymptotic ones. Source-extraction at `fft/GOLDSTINE-1977-INTERPOLATION-BRIEF.md`; deeper framing parked at `paper/FFT-SEARCH-PLAN.md`. Cited at §1.5, §4.2, and (potentially) §3 / §7.

## Cost / conversion framework anchor (§1)

- **Coase, R. H., 1937** — "The Nature of the Firm," *Economica* New Series Vol. 4 No. 16 (Nov. 1937), pp. 386–405. PDF at [sources/Coase-1937.pdf](sources/Coase-1937.pdf). Source for the transaction-cost framework adopted at §1.5 and §6: trade through any coordination mechanism carries a non-zero, irreducible fee, and the *algebra* of that fee — additivity across compositions, amortization across repeated uses, scale-behavior, representation-dependence, bypass-resistance under specialist intermediation, and heterogeneity across transaction types — determines what the framework lets one prove. Coase's distinction between the existence of friction (p. 390: "there is a cost of using the price mechanism") and its algebra (p. 395 marginal condition; p. 396 the firm-size determination "(a) the less the costs of organising and the slower these costs rise with an increase in the transactions organised") is the methodological precedent for FIRST-PROOF debt #2 (algebra of `δ` left open with named open sub-questions). Cited at §1.1 (transaction-cost vocabulary), §1.5 (irreducible-fee framing), §6.5 (Lemma B as the simplest zeroing-route block, with full algebra of `δ` deferred per debt #2), and (potentially) §Conclusion as the methodological-framework reference.

## Algebraic-side material

- **Heideman, M. T., Johnson, D. H., and Burrus, C. S., 1985, §5** — eigenspace decomposition `Q(ζ_n) = K_n ⊕ K_n · 2i sin(2π/n)` under `σ_{−1}`, forcing `K_n` as the multiplicatively-closed half; cited at §1, §6.
- **`memos/NATIVE-F-MINIMAL-DEFINITION.md`** *(in-program companion)* — closure-mismatch theorem (no functor `F` preserves closure-depth from `Aff⁺(ℝ)` to `{K_n}`); cited at §Intro and §7 as the algebraic-side companion.

## Substrate-side sources (§5)

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

- **`paper/LANDFALL-EXPORT.md`** *(in-program extract from Adam, Landfall)* — affine-closure template (Landfall §2), no-invariant-measure aggregation (Landfall §6 via Bowen 2002), finite-closure refusal (Landfall §7 via Gosper). Cited at §6 as the template the impossibility argument inherits.
- **Bowen, L., 2002** — no `PSL(2, ℝ)`-invariant probability measure on the binary tiling space.
- **Gosper, R. W., 1972** — continued-fraction arithmetic machine; cited as the negative anchor (exact computation in unbounded state, finite closure refused).
