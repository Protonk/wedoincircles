# DONT-BELIEVE-ME-JUST-WATCH

## Disanalogies

### D1. Algebraic vs. transcendental characters
The N-th roots of unity solve z^N = 1. They are algebraic. Every operation the FFT performs on them is exact in exact arithmetic.

The log-binade circle's coordinate change involves ln 2, which is transcendental. The inexactness is constitutive, not a perturbation of an exact process. The DFT has an ideal form that rounding errors corrupt. The log-binade circle has no ideal form.

### D2. Exact vs. approximate coefficient action
The FFT butterfly acts on the Fourier coefficient at frequency r with no coupling to other frequencies.

Addition on the log-binade circle couples frequency r to the global statistics of the distribution, with an error that decays as the distribution concentrates but does not vanish at any finite step. Mode-by-mode tracking means accepting inter-mode leakage at every step.

### D3. Invertibility
The DFT maps N time-domain samples to N frequency-domain coefficients and back, losslessly.

The log-binade circle is a quotient: the binade index is discarded, the map is many-to-one, the original number is not recoverable. Fourier analysis here analyzes a projection, not the underlying space. The analysis is one-directional.

### D4. Finite vs. infinite character group
The DFT lives on ℤ/Nℤ: N characters, finite group, finite computation.

The log-binade circle is ℝ/ℤ: characters indexed by all of ℤ. The seam's derivative jump forces infinite Fourier content — continuous but not C¹ at the glue point implies infinite spectral support, with coefficients decaying as O(1/n²) but never terminating. No finite truncation is exact.

## Structural contrasts

### C5. Compactness survives
Both circles are compact. Distributions on both are fully characterised by their Fourier coefficients, and vanishing non-trivial modes imply convergence to uniform. The distribution need not be tracked directly — only its spectral content. This is the strongest structural parallel and the reason the comparison is non-vacuous.

### C6. Radix-2 analog
Cooley–Tukey factors a size-N DFT into size-N/2 DFTs. Binary subdivision of the log-binade circle at depth d produces 2^d cells; refining to d+1 doubles the count — a radix-2 step.

The butterfly analog is the update rule for Fourier coefficients between depths. On the unit circle, the inter-stage corrections are roots of unity and recur exactly. On the log-binade circle, they involve ln 2 and do not recur. Same architecture, different constants, different closure.

### C7. Partial survival of convolution
On the unit circle, pointwise multiplication in the frequency domain is convolution in the time domain.

On the log-binade circle, multiplication of positive reals is addition of their logarithms, which is translation on the circle. Translation acts diagonally on Fourier coefficients — clean, exact, no coupling.

Addition of positive reals does not correspond to any group operation on the log-binade circle. Its action on the coefficients is approximately diagonal with decaying but nonvanishing cross-terms. Multiplication respects the circle's group structure; addition does not.

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
