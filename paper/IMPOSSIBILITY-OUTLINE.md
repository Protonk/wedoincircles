# Eff Eff Tee

>Meta instruction for humans and agents. Stage direction.

JACM is the venue. ~25 pages with figures is the target. The register is engineering inflected mathematics. Savoir faire is the goal.

## Abstract

We prove that current FFT-style lower-bound methods cannot descend below their existing thresholds on cyclotomic-DFT and adjacent compute-cost problems. The mult/add conversion underlying the FFT framework (Schönhage–Strassen 1971, Morgenstern 1973, Winograd 1978, Auslander–Feig–Winograd 1984) is a map between cost manifolds, coherent on each side but discontinuous across the bounded/unbounded coefficient boundary where the descent gradient is lost. A stronger FFT-style lower bound requires a continuous route through that boundary, and the substrate it would operate on — rotation-orbit Diophantine kinematics, non-nesting isoperimetric registers, closed-form polygon arithmetic, and cyclotomic-ladder unboundedness against affine flatness — supplies no such route. 

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

Context, claim, the operational-side reading paired with the algebraic-side closure-mismatch companion (`memos/NATIVE-F-MINIMAL-DEFINITION.md`). 

## §1. Cost manifolds and the mult/add map

### §1.1. Cost manifolds
Working definition: a cost manifold is a space of cost-bearing primitives equipped with a complexity measure on their compositions. Lower-bound work on a problem inhabits such a manifold; the paper treats this inhabitance explicitly.

### §1.2. The multiplicative cost manifold
The manifold of multiplicative-complexity bounds for cyclotomic-DFT and adjacent computations. Schönhage–Strassen 1971, Winograd 1978, and Auslander–Feig–Winograd 1984 each give it structure (full presentation at §3).

### §1.3. The additive cost manifold
The manifold of additive-complexity bounds. Morgenstern 1973 is the canonical structure-bearing result (full presentation at §3.3).

### §1.4. Coefficient regimes
Bounded vs unbounded coefficients. The regime is a parameter of every cost-bearing measure on either side; many bounds — Morgenstern's notably — depend on which regime is in force.

### §1.5. The mult/add conversion map
A map between §1.2 and §1.3. FFT-style algorithms operate as instances of this conversion. The map's behavior is parameterized by §1.4's regime.

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

## §4. Main theorem

### §4.1. Frame
Preview in plain language: an impossibility theorem on FFT-style descent below existing lower-bound thresholds for cyclotomic-DFT and adjacent compute-cost problems. The formal version is at §4.5.

### §4.2. FFT-style methods
The hypothesis class. The native operations of §1's cost manifold — multiplicative-side primitives from §1.2, additive-side primitives from §1.3, the conversion-map applications of §1.5 — under the standard composability of the four-framework canon (§3.2–§3.5). What the class includes; what it excludes.

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
Values: Hurwitz coefficients, gap `4π⁴/(3n²)`, and the sharp constant `6/π² = 1/ζ(2)` are fixed; descent reaches them only at threshold.

### §5.4. Cyclotomic-ladder unboundedness against affine flatness
Structure: `[K_n : ℚ] = φ(n)/2` grows unbounded with `n`; affine closure is flat; native operations cannot bridge the asymmetry.

### §5.5. The admissibility envelope
Audit: within L-W safety, closed-branch evidence, and the auxiliary-tool repertoire, no admissible method extracts additional descent information.

### §5.6. Information-uniformity at the boundary
Synthesis: §5.1–§5.5 jointly establish that every passage hits the bounded/unbounded coefficient boundary the same way. The result §6 inherits.

## §6. Gradients without information

### §6.1. Gradient descent on the cost manifold
Setup: descent on the cost manifold means trading a higher cost-bearing complexity bound for a lower one by reorganizing the underlying computation. Lower-bound improvement *is* successful descent. Frame the problem in §1's language.

### §6.2. What descent requires
For descent to succeed at the boundary in §1.5's conversion map, the algorithm must extract information distinguishing one passage from another. Without distinguishing information, descent is undirected.

### §6.3. §5.6 inherited
§5.6 establishes information-uniformity at the boundary. The substrate refuses to provide what §6.2 says descent needs.

### §6.4. The affine-closure template (Landfall §2)
The proof template extracted at `paper/LANDFALL-EXPORT.md`, restated for cost manifolds: no finite composition of native operations produces a route outside the operations' closure class. The argument's shape is structural; it does not depend on the specific cost-bearing primitives.

### §6.5. Native operations have closed composition
Apply the template to our setting. The multiplicative-side primitives of §1.2 compose into a closure class bounded by §1.4's regime parameters. The additive-side primitives of §1.3 compose into another. The discontinuity of the conversion map in §1.5 lies outside both classes.

### §6.6. No descent route exists; QED
Compose §6.3 + §6.5: descent has no distinguishing information; native operations don't compose into a route across the discontinuity. No FFT-style descent below current thresholds is reachable on this substrate. QED for §4.

## §7. Back again

Return to the four frameworks of §3, now under the impossibility. Schönhage–Strassen, Morgenstern, Winograd, AFW are at their natural limits — not from defect, but because no further descent is reachable on this substrate by these methods. Pair with the algebraic-side closure-mismatch reading (`memos/NATIVE-F-MINIMAL-DEFINITION.md`): the operational-side and algebraic-side companions complete each other.

## §Conclusion

Coda. What's named, what's left as future work: the cost-manifold map at higher resolution; non-FFT lower-bound methods; the K-H-L-A discrepancy strut as adjacent program.

# References

> Provenance discipline per `BNHA/ONE-FOR-ALL.md`: every load-bearing tool below names the chain it inherits from, and is staged for the next reader to pick up without reconstructing context. Working entries; bibliographic data refined per pass.

## Primary engagement — the four FFT frameworks (§3, §7)

- **Schönhage, A., and Strassen, V., 1971** — operational uniform model; cited at §1 (cost-manifold definition) and §3 (best light + avoidance: not a lower-bound source).
- **Morgenstern, J., 1973** — bounded-coefficient additive lower bound; cited at §1, §3, §6 (the floor that turns out to be unreachable from below).
- **Winograd, S., 1978** — modular-product theorem `μ(T_P) = 2n − k` and CRT-cyclotomic factor ledger; cited at §1, §3.
- **Auslander, L., Feig, E., and Winograd, S., 1984** — cyclotomic decomposition under rational equivalence; cited at §1, §3.
- **`paper/FFT-COMPLEXITY-ARTICULATION.md`** *(in-program extract)* — proof-template and trust-boundary index for the four FFT frameworks.

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
