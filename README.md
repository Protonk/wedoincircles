# wedoincircles

![A hand-drawn sketch in MS Paint style: a stick figure wearing a hardhat stands beside a small industrial building with a smokestack. On the ground in front of the figure, three red triangles sit alongside one blue circle. Handwritten text floats in the sky reading "i guess we doin circles now".](figures/doincircles.png)

The program tests whether a candidate functor `F` relates the native closure structures of two arithmetic objects: the log-side affine apparatus `Aff⁺(ℝ)` (motivated by the floating-point residue `ε(m) = log₂(1+m) − m` from *Landfall*) and the circle-side cyclotomic apparatus `{K_n = ℚ(cos(2π/n))}` (motivated by the regular `n`-gon wholeness construction). The working expectation is that no such `F` exists, and that the shape of the no is the content worth recording.

## Shape

The shape of the no is a closure-depth mismatch. On the log side, the native closure object `Aff⁺(ℝ)` — affine composition of the machine's primitive operations — is flat: iterating composition never leaves the two-parameter affine form. On the circle side, the trace-field ladder `K_n = ℚ(cos(2π/n))` has `[K_n : ℚ] = φ(n)/2`, which is unbounded as `n` varies. No native functor preserving closure-generator depth can carry a flat object to an unbounded ladder. The no-go holds over any field admitting Chebyshev polynomials and affine maps.

![A rotated label-free pseudo-Chebyshev construction: colored rays fan from a shared anchor into a quarter-circle, with node points and an irregular algebraic-degree comb emphasizing arithmetic jumps along a smooth geometric convergence.](figures/pseudo_chebyshev_nodes.png)

## State

Settled: the closure-depth no-go is proved under named functorial
axioms, and the strip-`H¹` / Hurwitz comparison gives a second
theorem-grade bridge inside the polygon apparatus. The Liouville-style
routes toward `π` have also produced useful negative information: the
obvious Archimedean approximants are too high, and the natural
Euler-identity route crosses into post-L-W transcendence machinery.

Live: the compute-cost branch is the main open construction. Its
current shape is certification-preserving algebraic arithmetic, a
`V_cert`-type ledger, and a still-needed theorem connecting the ledger
to primitive-operation cost. The FFT-side material now names what that
theorem has to earn: the zero-defect endpoint must be a forbidden
closure boundary, not just a small numerical limit.

Parked: the Kraft-Parseval discrepancy route remains available, but it
is not load-bearing unless its Roth / post-L-W audit closes cleanly.
Other branches are treated the same way: useful as substrate and
discipline, not premises, until their own trust boundary is explicit.

Under this state the expected final theorem has two main struts: the
structural closure-depth fault line already in hand, and the open
compute-cost fault line. More struts may return, but none is allowed to
enter by atmosphere.

## Stance

We stand behind the discipline described in [CONTRIBUTING.md](CONTRIBUTING.md). In order to do this our claims must know whether they are load-bearing or exploratory. This means you must know as well.

## Growth

We work under [a set of sharp questions](BNHA/VILLAINS.md) about ourselves; five are answered, one is partly answered (triple named, construction open), one is refused on the grounds that inversion of the premise is enlightenment.

![A label-free geometric art image: translucent red, blue, green, orange, purple, and teal regular polygons overlap around a pale central circle. Thin colored radial lines run from visible polygon corners inward to the center, while a soft gray circle outlines the shared incircle.](figures/archimedean_outside_out.png)
