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

Define the multiplicative cost manifold (Schönhage–Strassen 1971's operational uniform model; Winograd 1978's modular-product / CRT-cyclotomic ledger; Auslander–Feig–Winograd 1984's cyclotomic decomposition under rational equivalence) and the additive cost manifold (Morgenstern 1973's bounded-coefficient additive lower bound). Specify the mult/add conversion as a map between them.

## §2. The tour

Promissory. After §1 establishes language, §2 promises the route: cards on the table at §3, theorem at §4, the maze at §5, gradients at §6, back to the canon at §7. Names the substrate-side corpus (rotation-orbit Diophantine kinematics, non-nesting isoperimetric registers, closed-form polygon arithmetic, cyclotomic-ladder unboundedness against affine flatness, admissibility envelope) as the proof material §5 will deploy.

## §3. Cards on the table

The four FFT frameworks (Schönhage–Strassen 1971, Morgenstern 1973, Winograd 1978, Auslander–Feig–Winograd 1984) presented in their best light. Then what each avoids individually and as a set: AFW under rational equivalence avoids certification cost; Morgenstern's bound avoids unbounded-coefficient regimes; Winograd's μ-bounds avoid paid adjunctions; Schönhage–Strassen's operational model is not a lower-bound source. The avoidances foreshadow §5/§6 without yet naming the impossibility.

## §4. Main theorem

Formal propositional statement of the FFT-impossibility on cyclotomic-DFT and adjacent compute-cost problems. Precise hypothesis specifying what counts as "FFT-style" lower-bound methods (the four-framework canon plus its standard composability), conclusion stating no descent below the existing thresholds is reachable, proof outline naming §5 + §6 + the Landfall §2 affine-closure template as the load-bearing pieces.

## §5. A maze of twisting passages, all alike

The problem of information passage through the FFT. Five substrate-side lemmas, one per witness from `paper/`: rotation-orbit Diophantine kinematics; non-nesting isoperimetric registers; closed-form polygon arithmetic; cyclotomic-ladder unboundedness against affine flatness; admissibility envelope. Each lemma establishes that every FFT-algorithm passage hits the bounded/unbounded coefficient boundary in the same way — no passage distinguishes itself, no information is available to choose a descent direction.

## §6. Gradients without information

Gradient descent on the cost manifold robbed of information at the boundary. The affine-closure proof template inherited from Landfall §2 (extracted at `paper/LANDFALL-EXPORT.md`): no finite composition of native operations produces a route through the discontinuity. The substrate-side lemmas of §5 supply the information-uniformity that makes the template fire. QED for the §4 main theorem.

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
