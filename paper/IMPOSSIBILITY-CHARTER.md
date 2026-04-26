# IMPOSSIBILITY-CHARTER

The paper proves that current FFT-style lower bounds cannot improve on this substrate because the multiplication-to-addition conversion has a structural imperfection that destroys the descent gradient. The five substrate memos in `paper/` (ROTATIONAL-SUBSTRATE, ISOPERIMETRIC-EXCHANGE, POLYGONAL-LEDGER, VERTEXIOUS-ALGEBRA, INTERIOR-RESIDUUM) supply the witnesses. This charter records the load-bearing claim, the witness composition, and the discipline of what is *earned* versus what is *to be earned*.

## Working statement

In working form (the propositional theorem statement is deferred): the mult/add conversion in FFT-style cost models is a map between cost manifolds — a multiplicative-complexity manifold (where Schönhage–Strassen / Karatsuba / AFW reductions live) into an additive-complexity manifold (where Morgenstern bounded-coefficient determinants live). The map is imperfect: it is continuous on each manifold but discontinuous across them on this substrate. The discontinuity is the bounded↔unbounded coefficient regime change. Any further descent on FFT lower bounds would have to traverse this regime continuously. The substrate provides no continuous path; further descent is therefore not reachable by FFT-style methods.

## Witness composition

The five substrate memos compose as follows. **ROTATIONAL-SUBSTRATE** is the kinematic substrate where the gradient is supposed to flow — rotation orbits, CF convergents, Lyndon-word avatars. **ISOPERIMETRIC-EXCHANGE** is the register-barrier witness — three currencies that do not nest, of the same shape as mult/add separation at higher scale. **POLYGONAL-LEDGER** is the value witness — the closed-form constants `6/π² = 1/ζ(2)`, `4π⁴/(3n²)`, `φ(n)/2` the descent would need to reach. **VERTEXIOUS-ALGEBRA** is the unbounded-asymmetry witness — cyclotomic-ladder unboundedness against affine flatness. **INTERIOR-RESIDUUM** is the admissibility envelope — L-W safety, closed branches, auxiliary tools. The conjunction is the witness chain the paper assembles into its impossibility claim.

## Earned and to-be-earned

Earned by the substrate memos: each witness carries citation-backed content with named live items in the program. Earned elsewhere: `memos/NATIVE-F-MINIMAL-DEFINITION.md` (the algebraic-side twin — no functor `F` preserves closure-depth from `Aff⁺(ℝ)` to `{K_n}`); `fft/HEIDEMAN-JOHNSON-BURRUS-1985-BRIEF.md` §5 (closure-asymmetry forced by the involution decomposition `Q(ζ_n) = K_n ⊕ K_n · 2i sin(2π/n)`); the K-H-L-A discrepancy branch (empirical-to-density proxy under `β(π) = 0`).

To be earned in the paper proper: (i) the formal propositional statement of the impossibility theorem; (ii) the mult/add conversion as a precise map between cost manifolds with the discontinuity localized; (iii) the conversion from "five witnesses suggest the impossibility" to "five witnesses prove the impossibility."

## Relation to program structure

The paper sits in the program's three-strut frame (per the root README) as the operational-side complement to NATIVE-F. NATIVE-F is the algebraic-closure strut, already proven. The Kraft–Parseval discrepancy strut is downstream of K-H-L-A, not the paper's target. The compute-cost-lower-bound strut is what the paper addresses — but as an *impossibility* result on FFT-style descent, not as a positive lower-bound proof. The paper's contribution is to convert the open compute-cost question from "find a stronger lower bound" to "prove no stronger lower bound is reachable on this substrate by these methods."
