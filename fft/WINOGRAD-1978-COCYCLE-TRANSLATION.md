# WINOGRAD-1978-COCYCLE-TRANSLATION

A translation of Winograd 1978 through the cocycle lens of
[fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md) §"Gating debt 1." The purpose
is not to re-derive the modular-product theorem; it is to record a
verdict on whether Winograd's bilinear / multiplicative-complexity
ledger becomes a `{Δ_k}`-compressibility claim under the additive/log-
binade quotient-clock lens, and what that verdict implies for the No
Free Descent theorem's scope.

The substantive content of Winograd 1978 is summarized in
[fft/WINOGRAD-1978-BRIEF.md](fft/WINOGRAD-1978-BRIEF.md); this memo
presupposes that brief and works through its lens. The verdict format
follows
[fft/SCHOENHAGE-STRASSEN-COCYCLE-TRANSLATION.md](fft/SCHOENHAGE-STRASSEN-COCYCLE-TRANSLATION.md).

## Winograd's hypothesis class

Per [fft/WINOGRAD-1978-BRIEF.md](fft/WINOGRAD-1978-BRIEF.md) §1–§2:

- Bilinear algorithms over a chosen field `G`: polynomial products,
  modular polynomial products `T_P` for `P` a degree-`n` monic
  polynomial over `G`, cyclic convolutions, and DFT matrices assembled
  from these by Rader / Good / CRT index decompositions.
- The cost `μ(T_P)` counts essential nonrational multiplications under
  bilinear / rational-equivalence accounting. Multiplication by fixed
  elements of `G` is **not counted**. Additions, permutations,
  transpositions, and direct-product decompositions are free.
- The lower-bound input is the modular-product theorem
  `μ(T_P) = 2n − k`, with `k` the number of distinct irreducible
  factors of `P` over `G`. Applied to `P = u^N − 1` over `ℚ`, this
  gives the cyclic-convolution count `2N − d(N)`.
- Field extension can reduce `μ(T_P)` by splitting more factors of `P`.

The model is **algebraic / arithmetic-circuit over a field**, with
fixed-field scalars cheap and the cost currency on essential
multiplications. There is no representation layer at primitive-operation
level: a field element of `G` is a single algebraic object, not a
(sign, exponent, mantissa) triple.

## The cocycle lens

Per [fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md), the defect cocycle
`Δ_k(m) = χ_k(ε(m))` is born at the floating-point binade seam where
the additive mantissa coordinate `m` and the log-binade coordinate
`log₂(1+m)` displace. The in-scope criterion established by SS is:
in-scope iff the algorithm crosses the floating-point binade seam at
its primitive-operation level.

## Winograd under the lens

Winograd's primitive operations live in the field `G`: addition,
subtraction, multiplication by a fixed `g ∈ G` (free), and essential
nonrational multiplication of two indeterminate-bearing forms (counted).
Field elements of `G` carry no mantissa coordinate, no per-number
binade, and no normalization step. Polynomial residues modulo `P` are
algebraic objects in the quotient ring `G[u]/(P)`; CRT decompositions
recombine via `Q_1 P_1 + Q_2 P_2 = 1 mod P`, an algebraic identity, not
a floating-point operation.

When `G = ℚ` or `G = ℚ(i)` or any algebraic extension Winograd uses to
split factors, the field elements are exact algebraic numbers. The
constructions work in the exact arithmetic of those fields. Roots of
unity enter as algebraic objects (finite-order elements of an algebraic
extension), not as floating-point quantizations of `e^{2πi/N}`.

The mantissa-vs-binade displacement `ε` therefore does not appear at
the primitive-operation level of Winograd's hypothesis class. The
cocycle family `{Δ_k}` has no native presence in the model.

This matches the structural pattern of SS Method 2 (Fermat ring): both
models route around the floating-point seam by working in exact
algebraic / modular arithmetic on a finite or finitely-generated
algebraic structure, with the cost currency (essential multiplications
for Winograd; cyclic shifts for SS Method 2) independent of mantissa
coordinates.

## What this means for the cocycle compressibility question

The compressibility question — "does the scheme produce a defect-free
FFT-style composition law whose character products agree across all
butterfly refinements and primitive modes?" — *cannot be evaluated* on
Winograd's hypothesis class. There is no defect cocycle to compress:
no `ε`, no binade, no mantissa coordinate. The character structure
Winograd uses (roots of unity in cyclotomic factors of `u^N − 1`) is
*algebraic* character structure; the cocycle's analytic-realization
characters `χ_k(t) = e^{2πikt}` on `A = ℝ/ℤ` are pre-Fourier in a
different sense — they parameterize the additive/log-binade defect, not
the cyclotomic factorization.

Winograd's modular-product `μ(T_P) = 2n − k` and its
cyclic-convolution corollary `2N − d(N)` stand as real bounds on
bilinear algorithms in the chosen field. The bound's mechanism is CRT
decomposition plus the bilinear-complexity theorem; this mechanism is
independent of the cocycle question.

The bound therefore enters the program's threshold side `T(P)` as the
**multiplicative-side floor** any in-scope FFT-style method must
respect (when assembled from polynomial-product / convolution
primitives), not as a cocycle-compressibility statement. As with
Morgenstern, this is a separate import: a floating-point seam-crossing
FFT that is also assembled from cyclic-convolution / CRT primitives
still pays Winograd's multiplicative-complexity floor on its bilinear
part, regardless of whether its mantissa-level operations cross the
binade seam.

## The verdict

**(b) Conditional translation, out-of-scope.** Winograd does not
natively translate to a `{Δ_k}`-compressibility question; the
obstruction is the absence of the floating-point binade seam at the
primitive-operation level, exactly as in SS Method 2.

The structural reason aligns with the SS Method 2 path: bilinear
arithmetic over a field with fixed-field scalars free has no per-number
binade and no mantissa coordinate, so the cocycle is not born inside
the model. Winograd is reached by CRT factorization plus bilinear
complexity; SS Method 2 is reached by Fermat-ring modular arithmetic;
both terminate at the same boundary (no floating-point binade structure
at primitive-operation level).

The theorem scope therefore narrows in the same principled way: **No
Free Descent speaks to FFT-style methods that cross the floating-point
additive/log-binade seam at their primitive-operation level, not to
bilinear / CRT-decomposition FFTs that work in exact field arithmetic.**

Floating-point seam-crossing FFTs that *also* fall under Winograd's
bilinear hypothesis still face Winograd's modular-product floor; the
floor is imported into the program's `T(P)` from outside the cocycle
question, not derived from cocycle compressibility.

A separate Coasean note: Winograd's field-extension move (enlarging
the scalar field to split more factors of `P` and lower `μ(T_P)`) is
*not* a counterexample to the cocycle obstruction. It is a within-model
optimization at the bilinear-complexity layer; it leaves the
floating-point seam untouched because the model has no such seam to
cross. The two cost currencies (essential multiplications under field
extension; cocycle-compression cost at the seam) are independent.

## What changes in PHASE-DEFECT.md

Update §"Gating debt 1: coordinate-cut alignment" to record:

- Winograd 1978 sits **out-of-scope of the cocycle compressibility
  question** at primitive-operation level: bilinear / CRT-decomposition
  model over a chosen field has no floating-point binade and no `ε`.
  The structural path is parallel to SS Method 2.
- The bound enters the program as a `T(P)`-side floor on multiplicative
  cost for in-scope methods that assemble through polynomial-product /
  cyclic-convolution primitives, not as a cocycle-compressibility
  claim.
- The field-extension move that lowers `μ(T_P)` is within-model at the
  bilinear layer; it does not interact with the cocycle obstruction at
  the floating-point seam.
- This is *seam-orthogonal* scope-narrowing on the source side,
  reinforcing the SS pattern.

## Trust boundary

This memo presupposes the substantive content of
[fft/WINOGRAD-1978-BRIEF.md](fft/WINOGRAD-1978-BRIEF.md); it does not
re-derive the modular-product theorem (which the brief notes is itself
imported from earlier work), does not run a literature audit on whether
Winograd-style bilinear algorithms exhaust the multiplicative-side
hypothesis classes the canon supplies, and does not check whether the
modular-product theorem has independent transport to floating-point
representations. Those are downstream questions this memo does not
answer.

The verdict here is **(b) Conditional**: Winograd is one fully-worked
out-of-scope verdict via the bilinear-complexity / CRT path, landing at
the same boundary SS Method 2 establishes (no floating-point binade
structure at primitive-operation level). The conditional shape — theorem
scope narrows to floating-point seam-crossing — matches the SS verdict
and reinforces it.

The trust-boundary discipline of
[fft/PROVENANCE-AND-TRANSFERABILITY.md](fft/PROVENANCE-AND-TRANSFERABILITY.md)
governs how Winograd is cited downstream: Winograd supplies the
modular-product / cyclic-convolution multiplicative-complexity ledger,
not a cocycle-compressibility theorem; the `T(P)`-floor role and the
cocycle role are separate imports.
