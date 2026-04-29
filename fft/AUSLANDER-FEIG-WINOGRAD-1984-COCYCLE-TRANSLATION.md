# AUSLANDER-FEIG-WINOGRAD-1984-COCYCLE-TRANSLATION

A translation of Auslander–Feig–Winograd 1984 through the cocycle lens
of [fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md) §"Gating debt 1." The
purpose is not to re-derive the rational-equivalence cyclotomic
decomposition; it is to record a verdict on whether AFW's
multiplicative-complexity ledger becomes a `{Δ_k}`-compressibility
claim under the additive/log-binade quotient-clock lens, and what that
verdict implies for the No Free Descent theorem's scope.

The substantive content of AFW 1984 is summarized in
[fft/AUSLANDER-FEIG-WINOGRAD-1984-BRIEF.md](fft/AUSLANDER-FEIG-WINOGRAD-1984-BRIEF.md);
this memo presupposes that brief and works through its lens. The
verdict format follows
[fft/SCHOENHAGE-STRASSEN-COCYCLE-TRANSLATION.md](fft/SCHOENHAGE-STRASSEN-COCYCLE-TRANSLATION.md).

## AFW's hypothesis class

Per [fft/AUSLANDER-FEIG-WINOGRAD-1984-BRIEF.md](fft/AUSLANDER-FEIG-WINOGRAD-1984-BRIEF.md)
§§1–2:

- Semilinear algebraic-computation model over `ℂ` with rational
  equivalence: a finite base set inside `ℂ` plus input indeterminates,
  with elements of `ℂ(x_1, …, x_n)` formed by field operations.
- Cost `p(M)` counts essential nonrational multiplication / division
  steps in evaluating a linear system `MX`. Addition / subtraction is
  free; rational scalar multiplication / division is free; only
  nonrational m/d is charged.
- Rational pre/post transformations (rational equivalence) preserve
  `p(M)`. Tensor / Kronecker products of DFT matrices and CRT splittings
  of cyclotomic-quotient algebras assemble the finite-abelian-group
  case from `p`-primary blocks.
- The structure theorem reduces `F(G)` for finite abelian `G` to a
  semisimple cyclotomic algebra system; under the dimension hypothesis,
  `p(S) = Σ_j t_j (2 n_j − 1)` follows from the Auslander–Winograd 1980
  semilinear-system theorem.

The model is **algebraic / arithmetic-circuit over `ℂ` under rational
equivalence**, with rational scalars and additive operations free. As
with Winograd 1978, there is no representation layer at primitive-
operation level.

## The cocycle lens

Per [fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md), the defect cocycle
`Δ_k(m) = χ_k(ε(m))` is born at the floating-point binade seam. The
in-scope criterion established by SS is: in-scope iff the algorithm
crosses the floating-point binade seam at its primitive-operation level.

## AFW under the lens

AFW's primitive operations live in `ℂ` under rational equivalence:
field operations, free additions, free rational scalar m/d, and counted
essential nonrational m/d on indeterminate-bearing forms. Complex
algebraic constants (DFT matrix entries `e^{2πij/m}` for `j, m ∈ ℤ`)
enter the base set at no cost; rational pre/post transformations are
free. Cyclotomic field elements `ζ_m` are algebraic objects; the
arithmetic in `ℚ(ζ_m)` is exact algebraic arithmetic, not floating-point.

The dimension hypothesis the brief calls the "hidden no-collapse
condition" — `[ℚ(ζ_m) : ℚ] = φ(m)` and the matching tensor-product
identities — is verified algebraically over `ℚ`, not under any
floating-point representation. Vandermonde blocks `V(p^j)`, the
semisimple blocks `K(p^k)` for odd `p`, and the two `p = 2` blocks
`K(2^k; 1)`, `K(2^k; 2)` are all algebraic objects.

The mantissa-vs-binade displacement `ε` therefore does not appear at
the primitive-operation level of AFW's hypothesis class. The cocycle
family `{Δ_k}` has no native presence in the model.

This is the closest structural relative of Winograd 1978's cocycle
verdict, with one extra layer: AFW's rational-equivalence quotient is
*coarser* than Winograd's bilinear-complexity bookkeeping. Per the
brief's reflection addendum ("Rational Equivalence Quotients Away Data
the Program May Need"), nonsingular rational pre/post transformations
preserve `p(M)` while scrambling positional / cell-incidence structure.
A floating-point seam-crossing scheme reduced under rational
equivalence to a semisimple algebra system loses the per-mantissa
information the cocycle parameterizes; the equivalence relation
*forgets* exactly the structure the cocycle lives on.

## What this means for the cocycle compressibility question

The compressibility question — "does the scheme produce a defect-free
FFT-style composition law whose character products agree across all
butterfly refinements and primitive modes?" — *cannot be evaluated* on
AFW's hypothesis class. There is no defect cocycle to compress: no
`ε`, no binade, no mantissa coordinate. The cyclotomic characters AFW
uses (roots of unity in `ℚ(ζ_m)` Vandermonde blocks) are *algebraic*
finite-order characters; the cocycle's analytic-realization characters
`χ_k(t) = e^{2πikt}` on `A = ℝ/ℤ` parameterize the additive/log-binade
defect, not the cyclotomic factorization.

AFW's `p(F(G))` ledger stands as a real multiplicative-complexity
statement on semilinear DFT systems under rational equivalence. The
bound's mechanism is rational equivalence + p-primary decomposition +
tensor products + CRT cyclotomic decomposition + the Auslander–Winograd
1980 semilinear-system theorem; this mechanism is independent of the
cocycle question.

The bound therefore enters the program's threshold side `T(P)` as the
**multiplicative-side floor under rational equivalence** any in-scope
FFT-style method must respect (when assembled from semilinear primitives
and reduced under rational equivalence), not as a cocycle-
compressibility statement.

A finer note: rational equivalence's coarseness is *strictly stronger*
than Winograd 1978's field-extension move at quotienting away
representation structure. Where Winograd lowers `μ(T_P)` by enlarging
the scalar field, AFW lowers `p(M)` by allowing arbitrary nonsingular
rational pre/post transformations. Both moves leave the floating-point
seam untouched because neither model has such a seam to cross. The
program's cocycle obstruction therefore sits *outside* what AFW's
equivalence relation can quotient — which is the cocycle's defense, not
its weakness, against import collapse.

## The verdict

**(b) Conditional translation, out-of-scope.** AFW does not natively
translate to a `{Δ_k}`-compressibility question; the obstruction is the
absence of the floating-point binade seam at the primitive-operation
level, structurally parallel to SS Method 2 and Winograd 1978, with
the rational-equivalence quotient as an extra layer of distance from
mantissa-level structure.

The theorem scope therefore narrows in the same principled way: **No
Free Descent speaks to FFT-style methods that cross the floating-point
additive/log-binade seam at their primitive-operation level, not to
semilinear cyclotomic FFTs reduced under rational equivalence.**

Floating-point seam-crossing FFTs that *also* fall under AFW's
semilinear hypothesis (and survive the rational-equivalence reduction
without losing mantissa-level cost structure) still face AFW's
multiplicative-complexity floor; the floor is imported into the
program's `T(P)` from outside the cocycle question, not derived from
cocycle compressibility.

The rational-equivalence layer adds a methodological note: the program
must take care not to quotient floating-point seam-crossing schemes
through a rational equivalence that erases the mantissa-level cost the
cocycle measures. AFW's invariant is correct for DFT multiplicative
complexity but, per the brief's addendum, can be too coarse for
positional / mantissa-level ledgers. The cocycle obstruction's
representation-dependence (per
[measure/ALGEBRA-OF-DELTA.md](measure/ALGEBRA-OF-DELTA.md) §6) is
specifically the answer to that hazard: `δ` is born at the seam, and
seam-orthogonal equivalences cannot zero it.

## What changes in PHASE-DEFECT.md

Update §"Gating debt 1: coordinate-cut alignment" to record:

- AFW 1984 sits **out-of-scope of the cocycle compressibility question**
  at primitive-operation level: semilinear `ℂ` model under rational
  equivalence has no floating-point binade and no `ε`. The structural
  path is parallel to SS Method 2 and Winograd 1978, with rational
  equivalence as an extra coarsening layer.
- The bound enters the program as a `T(P)`-side floor on multiplicative
  cost under rational equivalence for in-scope methods that assemble
  through semilinear cyclotomic primitives, not as a
  cocycle-compressibility claim.
- Methodological note: rational equivalence preserves `p(M)` while
  scrambling mantissa-level structure. The cocycle obstruction is
  defended *because* `δ` is born at the seam, outside the rational-
  equivalence quotient.
- This is *seam-orthogonal* scope-narrowing on the source side,
  reinforcing the SS pattern; the rational-equivalence note is a
  positive consequence for the cocycle's representation-independence
  story under
  [measure/ALGEBRA-OF-DELTA.md](measure/ALGEBRA-OF-DELTA.md) §6.

## Trust boundary

This memo presupposes the substantive content of
[fft/AUSLANDER-FEIG-WINOGRAD-1984-BRIEF.md](fft/AUSLANDER-FEIG-WINOGRAD-1984-BRIEF.md);
it does not re-derive AFW's structure theorem (which the brief notes
imports the semilinear-system complexity theorem from Auslander–
Winograd 1980), does not check independently whether the rational-
equivalence quotient interacts with floating-point representation
beyond what the brief's reflection addendum already records, and does
not run a literature audit on whether AFW's semilinear hypothesis
class exhausts the rational-equivalence-side hypothesis classes the
canon supplies.

The verdict here is **(b) Conditional**: AFW is one fully-worked
out-of-scope verdict via the rational-equivalence / cyclotomic-
decomposition path, landing at the same boundary SS Method 2 and
Winograd 1978 establish (no floating-point binade structure at
primitive-operation level). The conditional shape — theorem scope
narrows to floating-point seam-crossing — matches the SS verdict and
reinforces it; the rational-equivalence layer adds a methodological
note in the program's favor on representation-dependence.

The trust-boundary discipline of
[fft/PROVENANCE-AND-TRANSFERABILITY.md](fft/PROVENANCE-AND-TRANSFERABILITY.md)
governs how AFW is cited downstream: AFW supplies the rational-
equivalence cyclotomic-decomposition multiplicative-complexity ledger,
not a cocycle-compressibility theorem; the `T(P)`-floor role and the
cocycle role are separate imports.
