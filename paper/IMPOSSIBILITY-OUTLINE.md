# Charter

>Meta instruction for humans and agents. Stage direction.

JACM is the venue. ~25 pages with figures is the target. The register is engineering inflected mathematics. Savoir faire is the goal.

# Paper

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

Context, claim, the operational-side reading paired with the algebraic-side closure-mismatch companion (`memos/NATIVE-F-MINIMAL-DEFINITION.md`). Methodological signature: substrate-side lemmas + boundary discontinuity composed under an affine-closure proof template inherited from prior work on the affine-pseudo-logarithm residue.

## §1. Cost manifolds and the mult/add map

Define the multiplicative cost manifold (Schönhage–Strassen 1971's operational uniform model; Winograd 1978's modular-product / CRT-cyclotomic ledger; Auslander–Feig–Winograd 1984's cyclotomic decomposition under rational equivalence) and the additive cost manifold (Morgenstern 1973's bounded-coefficient additive lower bound). Specify the mult/add conversion as a map between them. Notation hands the reader the paper's working language; the four frameworks enter as definitional apparatus, not yet as objects of engagement.

## §2. The tour

Promissory. After §1 establishes language, §2 promises the route: cards on the table at §3, theorem at §4, the maze at §5, gradients at §6, back to the canon at §7. Names the substrate-side corpus (rotation-orbit Diophantine kinematics, non-nesting isoperimetric registers, closed-form polygon arithmetic, cyclotomic-ladder unboundedness against affine flatness, admissibility envelope) as the proof material §5 will deploy.

## §3. Cards on the table

The four FFT frameworks (Schönhage–Strassen 1971, Morgenstern 1973, Winograd 1978, Auslander–Feig–Winograd 1984) presented in their best light. Then what each avoids individually and as a set: AFW under rational equivalence avoids certification cost; Morgenstern's bound avoids unbounded-coefficient regimes; Winograd's μ-bounds avoid paid adjunctions; Schönhage–Strassen's operational model is not a lower-bound source. The avoidances foreshadow §5/§6 without yet naming the impossibility.

## §4. Main theorem

Formal propositional statement of the FFT-impossibility on cyclotomic-DFT and adjacent compute-cost problems. Precise hypothesis specifying what counts as "FFT-style" lower-bound methods (the four-framework canon plus its standard composability), conclusion stating no descent below the existing thresholds is reachable, proof outline naming §5 + §6 + the Landfall §2 affine-closure template as the load-bearing pieces.

## §5. A maze of twisting passages, all alike

The problem of information passage through the FFT. Five substrate-side lemmas, one per witness from `paper/`: rotation-orbit Diophantine kinematics; non-nesting isoperimetric registers; closed-form polygon arithmetic; cyclotomic-ladder unboundedness against affine flatness; admissibility envelope. Each lemma establishes that every FFT-algorithm passage hits the bounded/unbounded coefficient boundary in the same way — no passage distinguishes itself, no information is available to choose a descent direction. The maze is uniform.

## §6. Gradients without information

Gradient descent on the cost manifold robbed of information at the boundary. The affine-closure proof template inherited from Landfall §2 (extracted at `paper/LANDFALL-EXPORT.md`): no finite composition of native operations produces a route through the discontinuity. The substrate-side lemmas of §5 supply the information-uniformity that makes the template fire. QED for the §4 main theorem.

## §7. Back again

Return to the four frameworks of §3, now under the impossibility. Schönhage–Strassen, Morgenstern, Winograd, AFW are at their natural limits — not from defect, but because no further descent is reachable on this substrate by these methods. Pair with the algebraic-side closure-mismatch reading (`memos/NATIVE-F-MINIMAL-DEFINITION.md`): the operational-side and algebraic-side companions complete each other. The canon is intact; what the paper has shown is where descent stalls.

## §Conclusion

Coda. What's named, what's left as future work: the cost-manifold map at higher resolution; non-FFT lower-bound methods; the K-H-L-A discrepancy strut as adjacent program.
