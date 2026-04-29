# MORGENSTERN-1973-COCYCLE-TRANSLATION

A translation of Morgenstern 1973 through the cocycle lens of
[fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md) §"Gating debt 1." The purpose
is not to re-derive Morgenstern's bound; it is to record a verdict on
whether his bounded-coefficient additive lower bound becomes a
`{Δ_k}`-compressibility claim under the additive/log-binade
quotient-clock lens, and what that verdict implies for the No Free
Descent theorem's scope.

The substantive content of Morgenstern 1973 is summarized in
[fft/MORGENSTERN-1973-BRIEF.md](fft/MORGENSTERN-1973-BRIEF.md); this
memo presupposes that brief and works through its lens. The verdict
format follows
[fft/SCHOENHAGE-STRASSEN-COCYCLE-TRANSLATION.md](fft/SCHOENHAGE-STRASSEN-COCYCLE-TRANSLATION.md).

## Morgenstern's hypothesis class

Per [fft/MORGENSTERN-1973-BRIEF.md](fft/MORGENSTERN-1973-BRIEF.md) §1:

- Linear algorithms over `ℂ`: a finite sequence of available linear
  affine functions, starting from constants and coordinate projections.
- Each counted step adjoins one new function `h = λ f + μ g`, where
  `f` and `g` are already available and `λ, μ ∈ ℂ` with
  `|λ|, |μ| ≤ c` for a fixed constant `c > 1/2`.
- The cost is the number of counted additions `m+`. Multiplication by
  a fixed scalar of bounded modulus is bundled into the bounded-
  coefficient binary linear combination, not separately counted.
- The lower-bound theorem is a determinant / volume-growth argument:
  `m+ > log A(F) / log(2c)`, with `A(F)` the maximum modulus of any
  square subdeterminant of the target coefficient matrix. For the
  `n × n` DFT with rows of common length `√n`, this yields
  `m+ > (n/2) log₂ n` at `c = 1`.

The model is **exact arithmetic over `ℂ`** with bounded-modulus complex
coefficients. There is no representation layer, no per-number scaling,
and no normalization step.

## The cocycle lens

Per [fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md), the two quotient clocks
are `A = ℝ/ℤ` (additive mantissa coordinate) and `L = ℝ_{>0}/2^ℤ`
(log-binade clock); the defect `ε(m) = log₂(1+m) − m` is the
displacement between them on the floating-point binade `[1, 2)`. The
defect cocycle `Δ_k(m) = χ_k(ε(m))` is born specifically at the
floating-point binade seam — the seam floating-point hardware crosses
when normalizing mantissas across binade boundaries.

The in-scope criterion established by SS is: in-scope iff the algorithm
crosses the floating-point binade seam at its primitive-operation level.

## Morgenstern under the lens

Morgenstern's primitive operation is the binary linear combination
`h = λ f + μ g` over exact `ℂ`. Complex coefficients of bounded modulus
are simply available; they are not floating-point objects, do not carry
mantissa coordinates, and do not undergo normalization. The model has no
binade structure: a complex number `z ∈ ℂ` is a single field element,
not a (sign, exponent, mantissa) triple, and adding two such elements
does not invoke binade renormalization.

The mantissa-vs-binade displacement `ε` therefore does not appear at
the primitive-operation level of Morgenstern's hypothesis class. The
cocycle family `{Δ_k}` has no native presence in the model.

This matches the structural pattern of SS Method 1 (fixed-point `ℂ`):
both models route around the floating-point seam by working in an
exact-arithmetic representation on the complex side, with the cost
structure (determinant growth for Morgenstern; precomputed quantization
for SS Method 1) independent of mantissa coordinates.

## What this means for the cocycle compressibility question

The compressibility question PHASE-DEFECT poses — "does the scheme
produce a defect-free FFT-style composition law whose character
products agree across all butterfly refinements and primitive modes?"
— *cannot be evaluated* on Morgenstern's hypothesis class. There is no
defect cocycle to compress: no `ε`, no binade, no mantissa coordinate.

Morgenstern's `Ω(n log n)` lower bound stands as a real bound on
bounded-coefficient linear `ℂ`-circuits computing the DFT. The bound's
mechanism is determinant / volume growth under bounded binary linear
combinations; this mechanism is independent of the cocycle question.
The bound therefore enters the program's threshold side `T(P)` as the
**additive-side floor** any in-scope FFT-style method must respect, not
as a cocycle-compressibility statement.

The distinction is sharp: a floating-point Cooley-Tukey FFT that
satisfies Morgenstern's bounded-coefficient hypothesis still pays
`Ω(n log n)` additions because its target matrix has the same
determinant scale, regardless of whether its primitive operations
cross the floating-point binade seam. The Morgenstern bound and the
cocycle obstruction are independent cost statements, both binding on
the in-scope class.

## The verdict

**(b) Conditional translation, out-of-scope.** Morgenstern does not
natively translate to a `{Δ_k}`-compressibility question; the
obstruction is the absence of the floating-point binade seam at the
primitive-operation level, exactly as in SS Method 1.

The structural reason aligns with the SS Method 1 path: exact `ℂ`
arithmetic with bounded-modulus complex coefficients has no per-number
binade and no mantissa coordinate, so the cocycle is not born inside
the model. Morgenstern is reached by determinant growth; SS Method 1
is reached by fixed-point quantization; both terminate at the same
boundary (no floating-point binade structure at primitive-operation
level).

The theorem scope therefore narrows in the same principled way SS
established: **No Free Descent speaks to FFT-style methods that cross
the floating-point additive/log-binade seam at their primitive-operation
level, not to bounded-coefficient linear `ℂ`-circuit FFTs that work in
exact complex arithmetic.**

Floating-point seam-crossing FFTs that *also* fall under Morgenstern's
bounded-coefficient hypothesis still face Morgenstern's `Ω(n log n)`
floor; the floor is imported into the program's `T(P)` from outside
the cocycle question, not derived from cocycle compressibility.

## What changes in PHASE-DEFECT.md

Update §"Gating debt 1: coordinate-cut alignment" to record:

- Morgenstern 1973 sits **out-of-scope of the cocycle compressibility
  question** at primitive-operation level: bounded-coefficient linear
  `ℂ`-circuit model has no floating-point binade and no `ε`. The
  structural path is parallel to SS Method 1.
- The bound enters the program as a `T(P)`-side floor on additive cost
  for in-scope methods that satisfy the bounded-coefficient hypothesis,
  not as a cocycle-compressibility claim.
- This is *seam-orthogonal* scope-narrowing on the source side,
  matching the SS pattern; it does not expand or contract the in-scope
  class beyond what SS already established.

## Trust boundary

This memo presupposes the substantive content of
[fft/MORGENSTERN-1973-BRIEF.md](fft/MORGENSTERN-1973-BRIEF.md); it does
not re-derive Morgenstern's bound, does not run a literature audit on
whether bounded-coefficient linear `ℂ`-circuits exhaust the
relevant additive-side hypothesis classes, and does not check whether
Morgenstern-style determinant arguments transport to floating-point
representations independently. Those are downstream questions this memo
does not answer.

The verdict here is **(b) Conditional**: Morgenstern is one fully-worked
out-of-scope verdict via the determinant-growth path, landing at the
same boundary SS Method 1 establishes (no floating-point binade
structure at primitive-operation level). The conditional shape — theorem
scope narrows to floating-point seam-crossing — matches the SS verdict
and reinforces it.

The trust-boundary discipline of
[fft/PROVENANCE-AND-TRANSFERABILITY.md](fft/PROVENANCE-AND-TRANSFERABILITY.md)
governs how Morgenstern is cited downstream: Morgenstern supplies the
bounded-coefficient additive lower bound, not a cocycle-compressibility
theorem; the `T(P)`-floor role and the cocycle role are separate
imports.
