# LANDFALL-PROOF-TEMPLATES

Detailed extraction of the Landfall proof templates used by the
FFT-impossibility branch. The source is
[sources/landfall.pdf](sources/landfall.pdf), a proof essay on the
binade residual `epsilon(m) = log_2(1 + m) - m`.

Paper-level routing is at
[paper/LANDFALL-EXPORT.md](paper/LANDFALL-EXPORT.md). The current
cost-level audit is at
[fft/LANDFALL-EXTENDED-CAFF-TRANSFER.md](fft/LANDFALL-EXTENDED-CAFF-TRANSFER.md):
Landfall §2 remains the original closure template, but it is not the
live FFT-side cost obstruction after the extended `C_Aff` audit. The
live source-side obstruction is Landfall §4 plus effective
Hermite-Lindemann at `n = 1`, transported through the phase-defect
machinery.

## Template 1: Affine Closure

Landfall §2 studies the exact binade coordinate
`lambda(m) = log_2(1 + m)`. Native binade operations generate
`Aff^+(R)`: additions translate, multiplications scale, and composition
stays in the two-parameter affine class. Landfall proves that `lambda`
is not in this closure. Since `m` is affine, the residual
`epsilon(m) = lambda(m) - m` is the equivalent non-affine source-side
defect.

Program use: this is the original closure-template shape for
FIRST-PROOF debt #3. It says what a source-side finite-closure refusal
looks like: native operations generate a closure class; the desired
coordinate change lives outside it; finite composition does not produce
the outside object.

Current status: template, not transferred theorem. Under the natural
fixed-precision extension of `C_Aff`, the Landfall §2 obstruction does
not give the FFT-side cost lower bound. The replacement source-side
input is Landfall §4 plus effective H-L at variable precision. The
candidate target transport is the character reflection barrier in
[fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md), with phase-lift
conservativity as the analytic-exponential specialization.

Adjacent decoupling reading: Mitchell's pseudo-log `L(x) = E + m`
fixes magnitude first, then pays the residual `epsilon` as correction.
This is the log-side coarse-first / refine-later pattern used by
[memos/BIDDER-AND-SON.md](memos/BIDDER-AND-SON.md) when it compares
mental logarithm computation with Landfall's hardware substrate.

Algebraic companion: [memos/NATIVE-F-MINIMAL-DEFINITION.md](memos/NATIVE-F-MINIMAL-DEFINITION.md)
uses the same closure-depth pattern in a different class: no functor
preserves closure-depth from `Aff^+(R)` to the cyclotomic ladder
`{K_n}` at competitive cost.

## Template 2: No Invariant Measure For Aggregation

Landfall §6 uses Bowen's no-`PSL(2, R)`-invariant probability measure
on the binary tiling space to block equivariant aggregation of local
data. Local information exists, but no invariant measure packages it
into a global correction. Source extraction for the Bowen input is
[memos/BOWEN-DRILLING-AND-DENSITY.md](memos/BOWEN-DRILLING-AND-DENSITY.md).

Program use: this is the pattern for representation-relocation
rebuttals. A proposed FFT-side escape that moves the defect to another
representation must explain how the pullback cocycle aggregates there.
Landfall supplies the obstruction shape, not the FFT-side theorem. The
FFT-side analogue has to be proved on its own substrate.

Where it lands: [fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md) Layer 3 and
the bypass-resistance / amortization questions under FIRST-PROOF debt
#2. If a candidate geometry is binary-tiling-embeddable, Bowen's
hole-drilling instability is available as a tactical strengthening.

## Template 3: Finite Closure Refused

Landfall §7 reads Gosper's continued-fraction arithmetic machine as a
negative anchor. The machine survives by refusing finite closure: state
grows without bound, periodicity occurs only on quadratic irrationals,
and its Mobius operations do not produce the logarithmic coordinate
change.

Program use: this calibrates scope. The impossibility theorem does not
say computation is impossible; it says `delta` cannot be zeroed by
finite composition of native operations. Gosper sidesteps the claimed
closure by giving up finite composability. The continued-fraction
cross-source role is recorded at
[rotations/CONTINUED-FRACTIONS-CROSSWALK.md](rotations/CONTINUED-FRACTIONS-CROSSWALK.md)
§4.

## Bottom Line

Landfall remains a proof-template source, not an FFT theorem. It proves
facts about `epsilon`, affine closure, binary-tiling aggregation, and
finite closure refusal. It does not prove facts about `delta`,
`{Delta_k}`, or `C_FFT`. The FFT-side burden lives in
[fft/LANDFALL-EXTENDED-CAFF-TRANSFER.md](fft/LANDFALL-EXTENDED-CAFF-TRANSFER.md),
[fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md), and
[measure/THE-FIRST-BRIDGE.md](measure/THE-FIRST-BRIDGE.md).
