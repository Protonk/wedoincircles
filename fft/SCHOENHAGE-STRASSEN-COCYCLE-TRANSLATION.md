# SCHOENHAGE-STRASSEN-COCYCLE-TRANSLATION

A worked first translation of one canon source through the cocycle
lens of [fft/PHASE-DEFECT.md](PHASE-DEFECT.md) §"Gating debt 1." The
purpose is not to re-derive Schönhage-Strassen; it is to record a
verdict on whether SS's `O(n log n log log n)` integer-multiplication
bound becomes a `{Δ_k}`-compressibility claim under the
additive/log-binade quotient-clock lens, and what that verdict implies
for the No Free Descent theorem's scope.

Reference: A. Schönhage and V. Strassen, "Schnelle Multiplikation
großer Zahlen," *Computing* 7 (1971), 281–292. Local source not
retrieved for this stub; the algorithm is reconstructed from canonical
secondary sources (Knuth Vol. 2, Crandall-Pomerance), and the
translation is sensitive to that level of detail.

## What SS does, in two lines

Given two `n`-bit integers, split each into chunks of size ~√`n`,
treat as polynomials of degree √`n` with integer coefficients, and
multiply the polynomials via FFT in the Fermat ring `R_k = ℤ/(2^k+1)`
where `2` is a `2(k+1)`-th root of unity. The convolution recurses:
coefficient products in `R_k` are themselves SS multiplications at
smaller scale. Total cost: `O(n log n log log n)`.

## Applying the cocycle lens

PHASE-DEFECT's two quotient clocks are:

- `A = ℝ/ℤ` — additive mantissa coordinate.
- `L = ℝ_{>0}/2^ℤ` — log-binade clock.

The defect `ε(m) = log₂(1+m) − m` is the *displacement* between these
two coordinates on the floating-point binade `[1, 2)`. The defect
cocycle `Δ_k(m) = χ_k(ε(m))` is the residual phase factor any
character pullback through `ψ = m + ε` must carry.

**SS does not work on this seam.** SS operates entirely on integer
coordinates: input is `n`-bit integers, intermediate values are
polynomial coefficients in `R_k`, output is integer. The
log-binade clock `L` does not appear; mantissa-vs-binade coordinate
displacement is not a quantity in the algorithm. There is no `ε`
at the algorithm's primitive-operation level.

The roots of unity SS uses (powers of `2` in `R_k`) are *finite-ring*
roots, not `e^{2πi/N}`. The character system of the additive group
`ℤ_{2^k+1}` is also finite, indexed by `ℤ_{2^k+1}` itself. A
finite-character cocycle analog could be written formally, but it
would have *no `ε` to carry* — there is no log-binade displacement in
the integer setting.

## What this means for the cocycle compressibility question

The compressibility question PHASE-DEFECT poses — "does the scheme
produce a defect-free FFT-style composition law whose character
products agree across all butterfly refinements and primitive modes?"
— *cannot be evaluated on SS as a self-contained integer algorithm*.
There is no defect cocycle to compress; the algorithm never crosses
the seam where the cocycle would be born.

This is not a failure of SS or of the cocycle lens. It is a scope
fact: the cocycle obstruction lives at the additive/log-binade seam.
Algorithms that work entirely on one side of the seam — pure integer
arithmetic, pure modular arithmetic, pure log-domain — are not subject
to the compressibility obstruction in their native domain.

## The verdict

**(b) Conditional translation.** SS does not natively translate to a
`{Δ_k}`-compressibility question. The translation succeeds at the
*interface* level — when SS is used as a building block in
floating-point computation (e.g., as part of high-precision multiplier
in a numerical library), the seam returns at the interface and the
cocycle compressibility question applies to the interface logic, not
to the SS internals.

The theorem scope therefore narrows, but the narrowing is principled:
**No Free Descent speaks to FFT-style methods at points where they
cross the additive/log-binade seam, not to FFT-style methods that work
entirely within an integer or modular ring.**

The natural in-scope test cases are:

- Cooley-Tukey radix-2 FFT applied to floating-point complex numbers
  (the textbook FFT in numerical libraries; mantissa × mantissa
  crosses the seam every butterfly);
- Bluestein's algorithm and other floating-point convolution methods;
- log-domain FFTs that explicitly factor through `log` to convert
  multiplications to additions (cross the seam by construction);
- any FFT-style scheme whose primitive operations include a
  floating-point multiplication.

The natural out-of-scope test cases (in addition to SS):

- pure modular FFTs over `ℤ/p` or `ℤ/(2^k+1)`;
- number-theoretic transforms over finite fields;
- Furer-style algorithms working in finite rings without a
  floating-point seam.

## What changes in PHASE-DEFECT.md

Update §"Gating debt 1: coordinate-cut alignment" to record:

- SS sits *outside* theorem scope as a self-contained integer
  algorithm. Its `O(n log n log log n)` bound does not become a
  `{Δ_k}`-compressibility claim under the cocycle lens.
- The theorem scope is principled: in-scope iff the algorithm crosses
  the additive/log-binade seam at its primitive-operation level.
- Reference back to PHASE-DEFECT.md's "Excluded patterns under the
  regularity guard" — the SS exclusion is *seam-orthogonal* exclusion,
  not regularity-guard exclusion. They are two distinct ways an
  FFT-style algorithm can fall outside theorem scope.

## Trust boundary

This stub does not re-derive SS; it does not run a literature audit
on whether the in-scope/out-of-scope partition is exhaustive; and it
does not check whether the conditional translation at the *interface*
level is itself clean (that interface-level question may import
content the audit at PHASE-DEFECT-PLAN's Edit 5 must resolve). The
stub is sized to record one verdict on one canon source, no more.

The verdict is **(b) Conditional** in the plan's three-verdict scheme:
SS-class methods are out-of-scope as native integer algorithms;
in-scope only at floating-point interfaces, where the cocycle question
re-applies to the interface logic. Theorem scope narrows; the
narrowing is principled and structural, not ad-hoc.
