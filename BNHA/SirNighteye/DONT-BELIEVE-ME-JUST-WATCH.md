# DONT-BELIEVE-ME-JUST-WATCH

A comparative examination of the unit circle (DFT) and the
log-binade circle (mantissa problem). Seven structural points,
then the thing they point at.


## Disanalogies

### D1. Algebraic vs. transcendental characters

The N-th roots of unity solve z^N = 1. They are algebraic. Every
operation the FFT performs on them is exact in exact arithmetic.
Rounding errors are perturbations of an exact process.

On the log-binade circle, the coordinate change involves ln 2,
which is transcendental. There is no exact process being
perturbed. The inexactness is constitutive. The DFT has an ideal
form that rounding errors corrupt. The mantissa problem has no
ideal form.


### D2. Exact vs. approximate coefficient action

The FFT butterfly acts on the Fourier coefficient at frequency r
with no coupling to other frequencies. No error term.

Addition acts on the mantissa distribution's coefficient h_n(r)
via Schatte's Lemma 1:

    |h_n(r) − (|a|n)^{2πir}| ≤ A_1 r²σ² / (a²n).

The error couples frequency r to the global statistics of the
distribution. It decays but does not vanish at any finite step.
Mode-by-mode tracking on the binade circle means accepting
inter-mode leakage at every step.


### D3. Invertibility

The DFT maps N time-domain samples to N frequency-domain
coefficients and back, losslessly.

Mantissa extraction maps a number to its position on [0,1) and
discards the binade index. Many-to-one. The original number is
not recoverable. Fourier analysis on the binade circle analyzes a
quotient of the original space. Information has been destroyed by
construction. The analysis is one-directional.


### D4. Finite vs. infinite character group

The DFT lives on ℤ/Nℤ: N characters, finite group, finite
transform, finite computation.

The log-binade circle is ℝ/ℤ: characters indexed by all of ℤ.
The derivative jump at the seam forces infinite Fourier content.
The O(1/n²) decay of the coefficients of ε is the quantitative
expression of this: continuous but not C¹ at the glue point
implies infinite spectral support. No finite truncation is exact.


## Structural contrasts

### C5. Compactness survives

Both circles are compact. Distributions on both are fully
characterised by their Fourier coefficients. If every nonzero
mode decays, convergence is proved. The distribution need not be
tracked directly — only its spectral content. This is the
strongest structural parallel and the reason the comparison is
non-vacuous.


### C6. Radix-2 analog

Cooley–Tukey factors a size-N DFT into size-N/2 DFTs via
N = 2 × N/2. On the log-binade circle, binary subdivision at
depth d produces 2^d cells. Refining from depth d to d+1 doubles
the count: a radix-2 step. The Stern–Brocot level-by-level
construction performs exactly this refinement.

The butterfly analog is the update rule for the mantissa
distribution's Fourier coefficients between depths d and d+1.
On the unit circle, the inter-stage corrections (twiddle factors)
are roots of unity and recur exactly. On the binade circle, they
involve ln 2 and do not recur. Same architecture, different
constants, different closure.

This is the Padé wall (Landfall §4) in FFT language.


### C7. Partial survival of convolution

On the unit circle, pointwise multiplication in the frequency
domain is convolution in the time domain.

On the log-binade circle, multiplication of positive reals is
addition of their logarithms, which is translation on the circle.
Translation acts diagonally on Fourier coefficients — clean,
exact, no coupling.

Addition of positive reals does not correspond to any group
operation on the log-binade circle. Its action on the Fourier
coefficients is approximately diagonal with decaying but
nonvanishing cross-terms.

Multiplication respects the circle's group structure. Addition
does not. This is Schatte's fundamental asymmetry expressed in
the FFT's language.


## The coordinative consequence

On the unit circle, all roots of unity have the same modulus:
they are equally spaced on the circle with |z| = 1 everywhere.

On the log-binade circle, the machine numbers m = k/2^d are
equally spaced in the additive coordinate but not in the
logarithmic coordinate. Their images under ψ(m) = log₂(1+m) are
non-uniformly spaced on [0,1). The non-uniformity is the
displacement field Δ^L = −ε.

This is not a disanalogy. It is not a structural contrast. It is
a coordinative consequence of the seam: the two grids — additive
and logarithmic — are incommensurable because the glue involves a
transcendental constant.

The displacement field and its characteristics — concave, zero at
the binade boundaries, maximal near m* ≈ 0.4427, transcendental
at every interior machine number, with Fourier coefficients that
decay as O(1/n²) but never terminate — will eventually force the
abandonment of attempts to find a functor F relating e and π
through the two circles. The unit circle and the log-binade circle
are not two views of the same object connected by a natural
transformation. They are two objects whose structural agreement
makes their coordinative disagreement irreducible.

The seam is not a defect in the log-binade circle. It is what
makes the log-binade circle a different circle.
