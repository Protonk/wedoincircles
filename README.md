# wedoincircles

![A hand-drawn sketch in MS Paint style: a stick figure wearing a hardhat stands beside a small industrial building with a smokestack. On the ground in front of the figure, three red triangles sit alongside one blue circle. Handwritten text floats in the sky reading "i guess we doin circles now".](figures/doincircles.png)

The program tests whether a candidate functor `F` relates two arithmetic objects: on the log side, the floating-point residue `ε(m) = log₂(1+m) − m` from *Landfall*; on the circle side, the regular `n`-gon wholeness construction and the Chebyshev / cyclotomic apparatus it generates. The working expectation is that no such `F` exists, and that the shape of the no is the content worth recording.

The shape of the no is a closure-depth mismatch. On the log side, the native closure object `Aff⁺(ℝ)` — affine composition of the machine's primitive operations — is flat: iterating composition never leaves the two-parameter affine form. On the circle side, the trace-field ladder `K_n = ℚ(cos(2π/n))` has `[K_n : ℚ] = φ(n)/2`, which is unbounded as `n` varies. No native functor preserving closure-generator depth can carry a flat object to an unbounded ladder. The no-go is self-contained algebra: it names no transcendental constants, and it holds over any field admitting Chebyshev polynomials and affine maps.

Current state, per branch:

- **Closure-depth no-go.** Proven under named functorial axioms. Self-contained algebra; names no transcendental constants.
- **Strip-H¹ / circumscribed-Hurwitz identification.** Proven: the strip-tissue `H¹` seminorm equals the circumscribed regular `n`-gon's Hurwitz gap up to `R_n = 16π⁶/(45n⁴) + 128π⁸/(315n⁶) + O(n⁻⁸)`. The radial-graph lift *is* the circumscribed polygon.
- **Naive Liouville endgame for transcendence of `π`.** Closed negative. All circle-side Archimedean observables factor through a single approximant `α_n = n tan(π/n)`, whose cyclotomic height is exponential in `φ(n) log n`. The Liouville lower bound fails to meet the `1/n²` Archimedean upper bound for every `n ≥ 3`.
- **Kraft–Parseval discrepancy route for effective transcendence of `π`.** Open search. The empirical-to-density bridge is the one remaining hypothesis.
- **Compute-cost lower bound on counting primitives.** Open search. No committed task-plus-machine-model pair yet makes `|M_N|` a bound rather than a companion metric.

The closure-depth theorem does not depend on any of the other branches; the strip-H¹ identification does not use Liouville; the negative closure of the Liouville endgame is a disciplined output in its own right, recording plainly that the circle side's Archimedean observables factor through an approximant whose height rules out the contradiction the endgame wanted. Two buildings, shared wall. The program's central open bet sits in the compute-cost branch: marry Kraft arithmetic to cyclotomic complexity without circular dependence on the circle. Until that lands, `|M_N|` is companion metric and the program's headline result is the closure-depth theorem alone.

The program also keeps itself under [a set of sharp questions](VILLAINS.md) about its own design; five are answered, one is quarantined as open search, one is refused on the grounds that the question's premise would corrupt the primary theorem if admitted.
