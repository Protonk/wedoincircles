# DEFORMATION

Worked examples showing how the pseudo-Chebyshev continuation (`corners/CONTINUITY.md`) behaves under continuous deformations of the underlying arc. Two deformations in this file, paired deliberately: a convex-preserving arc-flattening (non-similar, interesting) and a uniform scaling of the circle (similar, mostly diagnostic). The contrast is the point. Similarity transformations preserve the normalized geometry and normalized node data; non-similar deformations are the ones that can change the construction in a substantive way.

The first deformation — arc-flattening — is the main example. The second — uniform scaling — is included as the diagnostic foil: a deformation that looks dramatic geometrically but, after normalization, changes very little.

## Deformation 1: convex-preserving arc-flattening

This deformation flattens the quarter-circle arc into a vertical line segment without ever bending the arc the wrong way. The point is to watch what happens to the right-pane curve when the left-pane geometry is pulled continuously through a family of convex arcs.

The short version: the curve remains smooth on its shrinking domain, compresses rightward, loses small-n samples one at a time, and in the limit collapses onto the vertical line x = 1. The construction's explicit cyclotomic arithmetic does not survive the deformation.

## The deformation family

Pin the endpoint (1, 0). Start with the quarter-circle arc from (1, 0) to (0, 1). End with the vertical segment from (1, 0) to (1, π/2). Both have arc length π/2.

One simple family that interpolates uses the shared quarter-turn parameter s ∈ [0, π/2] and a deformation parameter d ∈ [0, 1],

P(s, d) = (1 − d)·(cos s, sin s) + d·(1, s).

Check:
- P(s, 0) = (cos s, sin s) — the quarter-circle.
- P(s, 1) = (1, s) — the vertical segment.
- P(0, d) = (1, 0) — pinned endpoint. ✓
- P(π/2, d) = (d, 1 − d + d·π/2) = (d, 1 + d·(π/2 − 1)) — moving endpoint.

At d = 0 and d = 1, the parameter s is arc length; for intermediate d it is just a common interpolation parameter. Convexity still holds for all d ∈ [0, 1]. The signed-curvature numerator is

    x'(s,d) y''(s,d) - y'(s,d) x''(s,d) = (1−d)² + (1−d)d·cos(s),

which is non-negative on s ∈ [0, π/2]; strictly positive for d < 1 and zero at d = 1 (straight line). Since the speed is positive, this is enough to show that the family never goes concave. Also x'(s,d) = −(1−d) sin(s) ≤ 0 and y'(s,d) = (1−d) cos(s) + d > 0, so the arc never bends backward.

## The pseudo-Chebyshev construction under deformation

For each d, the pseudo-Chebyshev construction still makes sense on the part of the t-range whose origin-to-corner segment actually meets the deformed arc. The n-gon's corner above the anchor sits at (1, tan(π/n)) regardless of d. The segment from the origin to that corner crosses the deformed arc at some parameter s = s(n, d) satisfying

(1 − d)·sin(s) + d·s = tan(π/n)·[(1 − d)·cos(s) + d].

Rearranged:

(1 − d)·[sin(s) − tan(π/n)·cos(s)] + d·[s − tan(π/n)] = 0.

At d = 0 this reduces to tan(s) = tan(π/n), giving s = π/n (the unchanged circle crossing). At d = 1 it reduces to s = tan(π/n) (the crossing on the vertical segment). For intermediate d, s moves between these endpoints whenever a crossing exists, and the node is read from the crossing's x-coordinate:

node(n, d) = (1 − d)·cos(s(n, d)) + d.

## Worked example: nodes at d = 0, d = 1/2, d = 1

Compute node(n, d) for n ∈ {3, 4, 5, 6, 8, 10} at three values of d.

| n  | d = 0 (quarter-circle) | d = 1/2 (halfway) | d = 1 (straight segment) |
|----|------------------------|-------------------|--------------------------|
| 3  | 0.500                  | 0.645             | — (segment exits top)    |
| 4  | 0.707                  | 0.821             | 1.000                    |
| 5  | 0.809                  | 0.891             | 1.000                    |
| 6  | 0.866                  | 0.927             | 1.000                    |
| 8  | 0.924                  | 0.960             | 1.000                    |
| 10 | 0.951                  | 0.975             | 1.000                    |

Three readings, one construction. Column 1 is the unmodified pseudo-Chebyshev (see `corners/PSEUDO-CHEBYSHEV-NODES.md`); column 3 is the fully flattened limit; column 2 is the worked middle.

**Sample computation for n = 4, d = 1/2.** The crossing equation is sin(s) − cos(s) + s − 1 = 0. Newton iteration from s ≈ π/4 converges to s ≈ 0.875. Then node(4, 1/2) = 0.5·cos(0.875) + 0.5 ≈ 0.5·0.641 + 0.5 ≈ 0.821.

**Sample computation for n = 10, d = 1/2.** The crossing equation is sin(s) − 0.325·cos(s) + s − 0.325 = 0, with solution s ≈ 0.319 and node ≈ 0.5·cos(0.319) + 0.5 ≈ 0.975. For large n, s ≈ π/n throughout the deformation, and node(n, d) ≈ (1 − d)·cos(π/n) + d ≈ 1 − (1 − d)·(π/n)²/2. The d = 1/2 entry is approximately the midpoint of the d = 0 and d = 1 entries for large n.

**Sample computation for n = 3, d = 1/2.** The crossing equation is sin(s) − √3·cos(s) + s − √3 = 0, with solution s ≈ 1.278 (still within [0, π/2] ≈ 1.571). Then node(3, 1/2) = 0.5·cos(1.278) + 0.5 ≈ 0.5·0.290 + 0.5 ≈ 0.645. The segment is not yet exiting the top of the arc at d = 1/2; see below.

## Domain contraction

The segment from origin to (1, tan(π/n)) exits the top of the deformed arc (parameter s = π/2) at the critical value

d*_n = 1 / (1 + tan(π/n) − π/2),

when the right-hand side lies in (0, 1). Beyond d*_n, the construction has no crossing for this n, and the sample is lost.

Evaluating:
- n = 2: tan(π/2) = ∞, so d*_2 = 0⁺. The t = 2 sample is lost the instant d leaves 0.
- n = 3: tan(π/3) = √3 ≈ 1.732, so d*_3 = 1 / (1 + √3 − π/2) ≈ 1/1.161 ≈ 0.861. The n = 3 sample is valid throughout d ∈ [0, 0.861] and lost for d > 0.861.
- n ≥ 4: tan(π/n) ≤ 1 < π/2, so d*_n > 1 or the formal expression is negative. Either way, the sample persists for every d ∈ [0, 1].

So under this deformation only n = 2 and n = 3 drop out; every integer sample n ≥ 4 survives all the way to d = 1 and lands at node = 1.

## Discussion

Four observations about what the right-pane curve does.

**1. The right-pane curve stays well-behaved in this family.** For each fixed d < 1, the curve is smooth on its domain and numerically remains monotone increasing and convex as a graph of n against x. The preserved convexity of the underlying arc points the same way, but this file is using that as guidance rather than a full proof of convexity for every d.

**2. Rightward compression.** For every integer n ≥ 4, the sample value moves from cos(π/n) at d = 0 toward 1 at d = 1. The whole curve compresses into the strip [d, 1) × [n_min(d), ∞), where

    n_min(d) = π / arctan((1 + d·(π/2 − 1)) / d),   d > 0,

is the smallest real t for which the origin-to-corner segment still hits the arc. At d = 0, n_min = 2 and the curve occupies the full domain [0, 1) × [2, ∞). At d = 1, the continuous curve has collapsed to the vertical line x = 1 with t > π / arctan(π/2) ≈ 3.129, so the surviving integer samples are n = 4, 5, 6, …

**3. Arithmetic collapse.** The two rational node values at d = 0 — node(2) = 0 and node(3) = 1/2 — both disappear under the deformation, at d = 0⁺ and d ≈ 0.861 respectively. At d = 1, every surviving sample is at node = 1: one rational value shared by all n ≥ 4. Between the endpoints, the clean cyclotomic formula `cos(π/n)` is gone. The sample values are now defined only implicitly by a mixed trigonometric/linear equation, so the explicit algebraic-degree control present at d = 0 has been lost. Some middle values may be algebraic, others transcendental; this file does not classify them.

**4. Information migrates from x to y.** At d = 0, the crossing is (cos(π/n), sin(π/n)) — both coordinates encode n. At d = 1, the crossing is (1, tan(π/n)) — only y encodes n; the x-coordinate is frozen at 1. If we had defined the "node" as the crossing's y-coordinate rather than its x-coordinate, the deformation would morph the sin(π/n) sequence into the tan(π/n) sequence — a non-degenerate transformation between two related sequences. Choosing x picked up the degenerate direction.

## What the program takes from this

A concrete existence proof of smooth-vs-arithmetic decoupling, on a small scale. Three specific things:

- **The smooth structure of the right-pane curve is relatively deformation-robust in this family.** The curve stays smooth on its domain, keeps its monotone rightward drift, and numerically retains the same convex shape.
- **The arithmetic structure of the integer samples is deformation-fragile.** The Niven-rationals are lost; the explicit cyclotomic algebraicity at integer samples is lost; in the limit every surviving sample has the same value.
- **Preserving convexity of the underlying arc is what keeps the geometry tame here.** This family was chosen to preserve convexity, and the right-pane behavior stays correspondingly orderly. A family that allowed the arc itself to go non-convex would be free to produce more complicated right-pane behavior as well.

This is the continuity frame at its cleanest: the same object (the pseudo-Chebyshev construction) read two ways (smooth / arithmetic), watched as it is pulled continuously toward a degenerate endpoint. Continuity preserves one reading and destroys the other. The decoupling is not hypothetical — this one-parameter family exhibits it explicitly.

## Deformation 2: uniform circle scaling (the diagnostic foil)

The d-deformation above is non-similar — it changes the shape of the arc. For contrast, consider the simplest possible alternative: uniformly scaling the circle from radius 1 down to radius r ∈ (0, 1]. The geometry responds by simple rescaling.

The n-gon circumscribing a circle of radius r has apothem r, anchor at (r, 0), and corner above the anchor at (r, r·tan(π/n)). The segment from origin to that corner still has slope tan(π/n), independent of r. Its crossing with the circle x² + y² = r² sits at

(r·cos(π/n), r·sin(π/n)),

so

node(n, r) = r · cos(π/n).

Linear in r. The right-pane curve is

n(x, r) = π / arccos(x / r),  x ∈ [0, r),

which is the r = 1 curve horizontally rescaled by factor r. Shape identical; only the asymptote moves from x = 1 at r = 1 down to x = r at general r and to x = 0 at r = 0. Every integer stem compresses toward 0 linearly in r.

**What differs from the arc-flattening deformation.**

- **Similarity vs non-similarity.** The r-shrink is a similarity transformation: every angle and geometric ratio in the construction is preserved. The normalized node values `node(n, r) / r = cos(π/n)` are unchanged. The d-deformation, by contrast, changes the arc's shape and changes the construction itself.
- **Arithmetic is preserved in ratios.** node(n, r) / r = cos(π/n) is invariant in r. The pseudo-Chebyshev data lives entirely in that ratio; normalize by r and the structure is r-invariant.
- **Absolute values collapse uniformly.** Every node → 0 as r → 0. The Niven-rationals node(2) = 0 and node(3) = r/2 remain rational when r is rational and compress toward 0. At r = 0 all integer stems pile at x = 0 — the mirror image, at the left end of the node axis, of the d → 1 collapse at x = 1.
- **No new arithmetic after normalization.** As absolute numbers, the values `node(n, r) = r·cos(π/n)` inherit whatever arithmetic is already present in `r`: for rational or algebraic r they stay algebraic, while for transcendental r they are transcendental as soon as `n > 2`. But after dividing by r, the pseudo-Chebyshev data is exactly the original `cos(π/n)` sequence. So unlike the d-deformation, the r-shrink does not introduce a new parameter-dependent arithmetic regime.

**Diagnostic rule.** If the object of interest is scale-free, similarity transformations are mostly diagnostic: they do not alter the underlying shape or the normalized node sequence. The d-deformation is interesting because it changes shape, not just size. At r = 0 the construction degenerates because it has been scaled to a point, not because a new phenomenon appeared along the way.

**Demonstration.** See `corners/uniform_scaling.sage` and `figures/pseudo_chebyshev_uniform_scaling.png`. The figure is a 3×2 grid showing the geometric construction (left column) and the node-sequence curve (right column) at r = 1, r = 0.5, and r = 0.25. The shape of the right-pane curve is identical across rows; only the horizontal extent changes.

## Pointer

Two concrete deformations so far. The first (arc-flattening) is non-similar and substantively interesting. The second (uniform scaling) is similar and mostly diagnostic — present as a foil. Future entries can introduce other deformations (non-convex-preserving, deformations that change which n values are critical, deformations that act on only part of the arc) and compare against these two baselines.
