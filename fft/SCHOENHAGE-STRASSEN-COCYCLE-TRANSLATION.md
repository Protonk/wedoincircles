# SCHOENHAGE-STRASSEN-COCYCLE-TRANSLATION

A worked first translation of one canon source through the cocycle
lens of [fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md) §"Gating debt 1."
The purpose is not to re-derive Schönhage-Strassen; it is to record a
verdict on whether SS's bounds become `{Δ_k}`-compressibility claims
under the additive/log-binade quotient-clock lens, and what that
verdict implies for the No Free Descent theorem's scope.

The substantive content of SS 1971 is summarized in
[fft/SCHOENHAGE-STRASSEN-1971-BRIEF.md](fft/SCHOENHAGE-STRASSEN-1971-BRIEF.md);
this memo presupposes that brief and works through its lens.

## SS 1971 has two methods

Per [fft/SCHOENHAGE-STRASSEN-1971-BRIEF.md](fft/SCHOENHAGE-STRASSEN-1971-BRIEF.md)
§"The Two Algorithms":

- **Method 1 (over ℂ).** FFT with `w_n = e^{2πi · 2^{-n}}`, performed
  in **fixed-point arithmetic** with `s` digits after the decimal
  point. Three nesting levels give bounds `O(N(log N)²)`, `O(N log N
  (log log N)²)`, `O(N log N log log N · (log log log N)²)`.
- **Method 2 (over `ℤ_{F_n}`).** FFT in the Fermat ring `ℤ/(2^{2^n}+1)`
  where `2` is a primitive `2^{n+1}`-th root of unity, twiddle
  multiplications as cyclic shifts. Final bound `O(N log N log log N)`.

The two methods have structurally different primitive-operation
layers. The cocycle lens must be applied to each separately.

## The cocycle lens

PHASE-DEFECT's two quotient clocks are:

- `A = ℝ/ℤ` — additive mantissa coordinate.
- `L = ℝ_{>0}/2^ℤ` — log-binade clock.

The defect `ε(m) = log₂(1+m) − m` is the *displacement* between these
two coordinates **on the floating-point binade `[1, 2)`**. The defect
cocycle `Δ_k(m) = χ_k(ε(m))` is the residual phase factor any
character pullback through `ψ = m + ε` must carry, and it is *born at
the floating-point binade structure* — the additive/log-binade seam is
specifically the seam floating-point hardware crosses when normalizing
mantissas across binade boundaries.

This is the load-bearing observation for the SS translation: the seam
is a floating-point-specific phenomenon, not a general
integer-arithmetic or modular-arithmetic phenomenon.

## Method 1 under the lens

Method 1 uses **fixed-point arithmetic**, not floating-point. Fixed-
point numbers have an implicit shared scaling factor across all
operands; multiplications are integer multiplications followed by a
fixed-rescaling shift. There is no per-number binade and no
renormalization across binade boundaries. The mantissa-vs-binade
displacement `ε` does not appear at the primitive-operation level
because there are no binades.

The complex roots of unity `w_n = e^{2πi · 2^{-n}}` *appear in
fixed-point quantization*, not as live floating-point objects: they
are precomputed once at the chosen precision `s` and stored as
fixed-point complex pairs. The runtime arithmetic does not invoke
log/exp at any butterfly.

Method 1 therefore does not cross the additive/log-binade seam in its
primitive operations. The `{Δ_k}` cocycle has no native presence in
the algorithm.

## Method 2 under the lens

Method 2 operates entirely in `ℤ_{F_n}`. Twiddle multiplications by
`2^κ` are cyclic shifts of the bit representation — by the
[fft/SCHOENHAGE-STRASSEN-1971-BRIEF.md](fft/SCHOENHAGE-STRASSEN-1971-BRIEF.md)
§"Repo Inference — The Cyclic-Shift Trick" structural observation —
not arithmetic operations at all in the Turing-machine cost model.

There is no log-binade clock anywhere in Method 2: `ℤ_{F_n}` is a
finite ring, characters of its additive group are finite, and the
algorithm never traffics in mantissa coordinates. The cocycle
construction `χ_k(ε(m))` requires `ε(m)` to exist; in Method 2 it
does not.

## What this means for the cocycle compressibility question

The compressibility question PHASE-DEFECT poses — "does the scheme
produce a defect-free FFT-style composition law whose character
products agree across all butterfly refinements and primitive modes?"
— *cannot be evaluated* on either SS method as a self-contained
algorithm. There is no defect cocycle to compress in either method:

- **Method 1**: no binade structure (fixed-point), no `ε`.
- **Method 2**: no mantissa coordinate (modular ring), no `ε`.

The seam where the cocycle is born is the floating-point binade
seam; SS uses non-floating-point arithmetic throughout in both
methods.

## The verdict

**(b) Conditional translation.** SS does not natively translate to a
`{Δ_k}`-compressibility question in either method; the obstruction
is the same in both cases (no floating-point binade), but reached
by different means (fixed-point in Method 1, modular in Method 2).

The theorem scope therefore narrows in a principled way: **No Free
Descent speaks to FFT-style methods that cross the floating-point
additive/log-binade seam at their primitive-operation level, not to
FFT-style methods that work in fixed-point or modular arithmetic.**

The natural in-scope test cases are:

- Cooley-Tukey radix-2 FFT applied to floating-point complex numbers
  (the textbook FFT in numerical libraries; mantissa × mantissa
  crosses the seam every butterfly through binade renormalization);
- Bluestein's algorithm and other floating-point convolution
  methods;
- log-domain FFTs that explicitly factor through `log` to convert
  multiplications to additions (cross the seam by construction);
- any FFT-style scheme whose primitive operations include a
  floating-point multiplication with binade renormalization.

The natural out-of-scope cases (in addition to both SS methods):

- pure modular FFTs over `ℤ/p` or `ℤ/(2^k+1)`;
- number-theoretic transforms over finite fields;
- Fürer-style algorithms working in finite rings without a
  floating-point seam;
- fixed-point FFTs (no binade structure, no `ε`).

## What changes in PHASE-DEFECT.md

Update §"Gating debt 1: coordinate-cut alignment" to record:

- SS sits outside theorem scope **in both Method 1 (fixed-point ℂ)
  and Method 2 (Fermat ring)**. Its bounds do not become
  `{Δ_k}`-compressibility claims in either method, because neither
  method crosses the floating-point binade seam at primitive-operation
  level.
- The theorem scope is principled: in-scope iff the algorithm crosses
  the *floating-point* additive/log-binade seam at its
  primitive-operation level. Fixed-point and modular FFTs are
  out-of-scope structurally, not by regularity-guard exclusion.
- This is *seam-orthogonal* scope-narrowing, distinct from the
  regularity-guard exclusion of advice-bearing / non-uniform /
  growing-state schemes.

## Trust boundary

This memo presupposes the substantive content of
[fft/SCHOENHAGE-STRASSEN-1971-BRIEF.md](fft/SCHOENHAGE-STRASSEN-1971-BRIEF.md);
it does not re-derive SS, does not run a full literature audit on
whether the floating-point/non-floating-point partition is exhaustive,
and does not check whether other canon sources (Cooley-Tukey,
Bluestein, Bailey, AFW, Winograd) actually translate cleanly when the
in-scope criterion is applied to them. Those are downstream test
cases, each warranting its own translation memo.

The verdict here is **(b) Conditional**: SS is one fully-worked
out-of-scope verdict via two structurally different paths, both
landing at the same boundary (no floating-point binade structure).
The conditional shape — theorem scope narrows to floating-point
seam-crossing — is recorded; whether downstream canon sources (the
ones actually expected to be in-scope) translate cleanly is a
separate question this memo does not answer.
