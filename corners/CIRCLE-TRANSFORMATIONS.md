# CIRCLE-TRANSFORMATIONS

Three continuous deformations of the pseudo-Chebyshev construction (`corners/PSEUDO-CHEBYSHEV-NODES.md`), plus the leash framework that organizes them. The construction fixes a circle and reads a node off each n-gon chord; here we vary the circle and watch the integer samples and right-pane curve respond.

Contents: (§1) uniform scaling — similarity transformation, diagnostic foil. (§2) convex-preserving arc-flattening — non-similar, destroys cyclotomic arithmetic. (§3) vertical translation — non-similar and sign-sensitive, with an interior-maximum fold at c > 0. (§4) the leash framework — cross-deformation analysis, property hierarchy, stratification, tightness–informativeness tradeoff.

---

## §1. Uniform scaling (diagnostic foil)

The simplest possible deformation: uniformly scale the circle from radius 1 down to radius r ∈ (0, 1]. The geometry responds by simple rescaling.

The n-gon circumscribing a circle of radius r has apothem r, anchor at (r, 0), and corner above the anchor at (r, r·tan(π/n)). The segment from origin to that corner still has slope tan(π/n), independent of r. Its crossing with the circle x² + y² = r² sits at

(r·cos(π/n), r·sin(π/n)),

so

node(n, r) = r · cos(π/n).

Linear in r. The right-pane curve is

n(x, r) = π / arccos(x / r),  x ∈ [0, r),

which is the r = 1 curve horizontally rescaled by factor r. Shape identical; only the asymptote moves from x = 1 at r = 1 down to x = r at general r and to x = 0 at r = 0. Every integer stem compresses toward 0 linearly in r.

**What makes this a foil.** The uniform r-shrink is a similarity transformation: every angle and geometric ratio in the construction is preserved. The normalized node values `node(n, r) / r = cos(π/n)` are unchanged. Non-similar deformations (§§2 and 3) can change the construction itself; this one cannot.

Specific consequences of the scaling being similar:

- **Arithmetic preserved in ratios.** `node(n, r) / r = cos(π/n)` is invariant in r. The pseudo-Chebyshev data lives entirely in that ratio; normalize by r and the structure is r-invariant.
- **Absolute values collapse uniformly.** Every node → 0 as r → 0. The Niven-rationals `node(2) = 0` and `node(3) = r/2` remain rational when r is rational and compress toward 0. At r = 0 all integer stems pile at x = 0 — the mirror image, at the left end of the node axis, of the d → 1 collapse that §2 shows at x = 1.
- **No new arithmetic after normalization.** As absolute numbers, the values `node(n, r) = r·cos(π/n)` inherit whatever arithmetic is already present in r: for rational or algebraic r they stay algebraic, while for transcendental r they are transcendental as soon as n > 2. But after dividing by r, the pseudo-Chebyshev data is exactly the original `cos(π/n)` sequence. So the r-shrink does not introduce a new parameter-dependent arithmetic regime.

**Diagnostic rule.** If the object of interest is scale-free, similarity transformations are mostly diagnostic: they do not alter the underlying shape or the normalized node sequence. At r = 0 the construction degenerates because it has been scaled to a point, not because a new phenomenon appeared along the way.

**Demonstration.** See `corners/uniform_scaling.sage` and `figures/pseudo_chebyshev_uniform_scaling.png`. The figure is a 3×2 grid showing the geometric construction (left column) and the node-sequence curve (right column) at r = 1, r = 0.5, and r = 0.25. The shape of the right-pane curve is identical across rows; only the horizontal extent changes.

---

## §2. Convex-preserving arc-flattening

The interesting counterpart to §1's similarity foil: a deformation that changes shape. Flatten the quarter-circle arc into a vertical line segment without ever bending the arc the wrong way. The point is to watch what happens to the right-pane curve when the left-pane geometry is pulled continuously through a family of convex arcs.

The short version: the curve remains smooth on its shrinking domain, compresses rightward, loses small-n samples one at a time, and in the limit collapses onto the vertical line x = 1. The construction's explicit cyclotomic arithmetic does not survive the deformation.

### The deformation family

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

### The pseudo-Chebyshev construction under deformation

For each d, the pseudo-Chebyshev construction still makes sense on the part of the t-range whose origin-to-corner segment actually meets the deformed arc. The n-gon's corner above the anchor sits at (1, tan(π/n)) regardless of d. The segment from the origin to that corner crosses the deformed arc at some parameter s = s(n, d) satisfying

(1 − d)·sin(s) + d·s = tan(π/n)·[(1 − d)·cos(s) + d].

Rearranged:

(1 − d)·[sin(s) − tan(π/n)·cos(s)] + d·[s − tan(π/n)] = 0.

At d = 0 this reduces to tan(s) = tan(π/n), giving s = π/n (the unchanged circle crossing). At d = 1 it reduces to s = tan(π/n) (the crossing on the vertical segment). For intermediate d, s moves between these endpoints whenever a crossing exists, and the node is read from the crossing's x-coordinate:

node(n, d) = (1 − d)·cos(s(n, d)) + d.

### Worked example: nodes at d = 0, d = 1/2, d = 1

Compute node(n, d) for n ∈ {3, 4, 5, 6, 8, 10} at three values of d.

| n  | d = 0 (quarter-circle) | d = 1/2 (halfway) | d = 1 (straight segment) |
|----|------------------------|-------------------|--------------------------|
| 3  | 0.500                  | 0.645             | — (segment exits top)    |
| 4  | 0.707                  | 0.821             | 1.000                    |
| 5  | 0.809                  | 0.891             | 1.000                    |
| 6  | 0.866                  | 0.927             | 1.000                    |
| 8  | 0.924                  | 0.960             | 1.000                    |
| 10 | 0.951                  | 0.975             | 1.000                    |

Three readings, one construction. Column 1 is the unmodified pseudo-Chebyshev; column 3 is the fully flattened limit; column 2 is the worked middle.

**Sample computation for n = 4, d = 1/2.** The crossing equation is sin(s) − cos(s) + s − 1 = 0. Newton iteration from s ≈ π/4 converges to s ≈ 0.875. Then node(4, 1/2) = 0.5·cos(0.875) + 0.5 ≈ 0.5·0.641 + 0.5 ≈ 0.821.

**Sample computation for n = 10, d = 1/2.** The crossing equation is sin(s) − 0.325·cos(s) + s − 0.325 = 0, with solution s ≈ 0.319 and node ≈ 0.5·cos(0.319) + 0.5 ≈ 0.975. For large n, s ≈ π/n throughout the deformation, and node(n, d) ≈ (1 − d)·cos(π/n) + d ≈ 1 − (1 − d)·(π/n)²/2. The d = 1/2 entry is approximately the midpoint of the d = 0 and d = 1 entries for large n.

**Sample computation for n = 3, d = 1/2.** The crossing equation is sin(s) − √3·cos(s) + s − √3 = 0, with solution s ≈ 1.278 (still within [0, π/2] ≈ 1.571). Then node(3, 1/2) = 0.5·cos(1.278) + 0.5 ≈ 0.5·0.290 + 0.5 ≈ 0.645. The segment is not yet exiting the top of the arc at d = 1/2; see below.

### Domain contraction

The segment from origin to (1, tan(π/n)) exits the top of the deformed arc (parameter s = π/2) at the critical value

d*_n = 1 / (1 + tan(π/n) − π/2),

when the right-hand side lies in (0, 1). Beyond d*_n, the construction has no crossing for this n, and the sample is lost.

Evaluating:
- n = 2: tan(π/2) = ∞, so d*_2 = 0⁺. The t = 2 sample is lost the instant d leaves 0.
- n = 3: tan(π/3) = √3 ≈ 1.732, so d*_3 = 1 / (1 + √3 − π/2) ≈ 1/1.161 ≈ 0.861. The n = 3 sample is valid throughout d ∈ [0, 0.861] and lost for d > 0.861.
- n ≥ 4: tan(π/n) ≤ 1 < π/2, so d*_n > 1 or the formal expression is negative. Either way, the sample persists for every d ∈ [0, 1].

So under this deformation only n = 2 and n = 3 drop out; every integer sample n ≥ 4 survives all the way to d = 1 and lands at node = 1.

### Discussion

Four observations about what the right-pane curve does.

**1. The right-pane curve stays well-behaved in this family.** For each fixed d < 1, the curve is smooth on its domain and numerically remains monotone increasing and convex as a graph of n against x. The preserved convexity of the underlying arc points the same way, but this section is using that as guidance rather than a full proof of convexity for every d.

**2. Rightward compression.** For every integer n ≥ 4, the sample value moves from cos(π/n) at d = 0 toward 1 at d = 1. The whole curve compresses into the strip [d, 1) × [n_min(d), ∞), where

    n_min(d) = π / arctan((1 + d·(π/2 − 1)) / d),   d > 0,

is the smallest real t for which the origin-to-corner segment still hits the arc. At d = 0, n_min = 2 and the curve occupies the full domain [0, 1) × [2, ∞). At d = 1, the continuous curve has collapsed to the vertical line x = 1 with t > π / arctan(π/2) ≈ 3.129, so the surviving integer samples are n = 4, 5, 6, …

**3. Arithmetic collapse.** The two rational node values at d = 0 — node(2) = 0 and node(3) = 1/2 — both disappear under the deformation, at d = 0⁺ and d ≈ 0.861 respectively. At d = 1, every surviving sample is at node = 1: one rational value shared by all n ≥ 4. Between the endpoints, the clean cyclotomic formula `cos(π/n)` is gone. The sample values are now defined only implicitly by a mixed trigonometric/linear equation, so the explicit algebraic-degree control present at d = 0 has been lost. Some middle values may be algebraic, others transcendental; this section does not classify them.

**4. Information migrates from x to y.** At d = 0, the crossing is (cos(π/n), sin(π/n)) — both coordinates encode n. At d = 1, the crossing is (1, tan(π/n)) — only y encodes n; the x-coordinate is frozen at 1. If we had defined the "node" as the crossing's y-coordinate rather than its x-coordinate, the deformation would morph the sin(π/n) sequence into the tan(π/n) sequence — a non-degenerate transformation between two related sequences. Choosing x picked up the degenerate direction.

### What the program takes from this

A concrete existence proof of smooth-vs-arithmetic decoupling, on a small scale. Three specific things:

- **The smooth structure of the right-pane curve is relatively deformation-robust in this family.** The curve stays smooth on its domain, keeps its monotone rightward drift, and numerically retains the same convex shape.
- **The arithmetic structure of the integer samples is deformation-fragile.** The Niven-rationals are lost; the explicit cyclotomic algebraicity at integer samples is lost; in the limit every surviving sample has the same value.
- **Preserving convexity of the underlying arc is what keeps the geometry tame here.** This family was chosen to preserve convexity, and the right-pane behavior stays correspondingly orderly. A family that allowed the arc itself to go non-convex would be free to produce more complicated right-pane behavior as well.

This is the continuity frame at its cleanest: the same object (the pseudo-Chebyshev construction) read two ways (smooth / arithmetic), watched as it is pulled continuously toward a degenerate endpoint. Continuity preserves one reading and destroys the other. The decoupling is not hypothetical — this one-parameter family exhibits it explicitly.

---

## §3. Vertical translation

A third deformation: translate the circle vertically while keeping the chords fixed. Non-similar like §2, but with a new feature: it is sign-sensitive — raising the circle produces structurally different behavior from lowering it by the same amount.

### The construction under translation

Keep the chords as in the original pseudo-Chebyshev setup: for each n ≥ 3, the chord is the line from the origin to (1, tan(π/n)). For n = 2, use the limiting chord: the positive y-axis. These chords do not move with the deformation.

Translate the circle: instead of being centered at the origin with radius 1, it is centered at (0, c) with radius 1, for a translation parameter c. The circle–chord intersections change, and the x-coordinate of the forward-direction intersection is the new node.

Substituting y = x·tan(π/n) into x² + (y − c)² = 1 and simplifying:

x² − c·sin(2π/n)·x + (c² − 1)·cos²(π/n) = 0.

Two roots. For c ∈ (−1, 1), the origin is inside the translated circle (distance from origin to (0, c) is |c| < 1 = radius), so one root is negative and one positive. Take the positive root:

**node(n, c) = cos(π/n) · (c · sin(π/n) + √(1 − c²·cos²(π/n))).**

At c = 0 this reduces to node = cos(π/n), recovering the original construction.

**When does the chord cross the translated circle?** The perpendicular distance from (0, c) to the chord equals |c|·cos(π/n). The line meets the translated circle iff that distance is ≤ 1, i.e., **|c| ≤ sec(π/n)**. In the regime emphasized here, `|c| ≤ 1`, every chord with `n ≥ 3` meets the circle, and the forward-direction root above is the relevant one. Outside that regime some chords miss entirely, and once the origin lies outside the circle one must also distinguish first and second forward intersections; this section does not pursue that case.

### Worked example

node(n, c) for n ∈ {3, 4, 5, 6, 10} at c ∈ {0.5, 0, −0.5}:

| n  | c = 0.5 (raised) | c = 0 (normal) | c = −0.5 (lowered) |
|----|------------------|----------------|--------------------|
| 3  | 0.701            | 0.500          | 0.268              |
| 4  | 0.911            | 0.707          | 0.411              |
| 5  | 0.977            | 0.809          | 0.501              |
| 6  | 0.997            | 0.866          | 0.564              |
| 10 | 0.984            | 0.951          | 0.689              |

**Sample computation for n = 3, c = 0.5.** node(3, 0.5) = (1/2)·(0.5·(√3/2) + √(1 − 0.25·0.25)) = (1/2)·(√3/4 + √(15/16)) = (√3 + √15) / 8 ≈ 0.701. Irrational; the Niven-rational node(3, 0) = 1/2 has been destroyed by the translation.

Across the displayed window `c ∈ {-0.5, 0, 0.5}`, each row increases with `c`. That is not a global monotonicity statement in `c`: for fixed `n` and larger positive `c`, the node can turn back down. For example, `node(10, 0.5) ≈ 0.984` but `node(10, 0.9) ≈ 0.756`.

### The asymptote: √(1 − c²)

As t → ∞, cos(π/t) → 1 and sin(π/t) → 0, so

node(t, c) → 1·(0 + √(1 − c²)) = √(1 − c²).

Symmetric in c: the asymptotes at c = 0.5 and c = −0.5 agree at √0.75 ≈ 0.866. Geometrically, as t → ∞ the chord approaches the x-axis, and the translated circle intersects the x-axis at x = ±√(1 − c²).

### The overshoot: c > 0 curve is non-monotone

At c = 0, the right-pane curve is monotone increasing from (0, 2) to the asymptote x = 1.

At c = 0.5, the curve rises above the asymptote `0.866`, peaks near `n ≈ 7` at node `≈ 1`, then decreases toward `0.866` from above. The curve is non-monotone.

Spot-check at c = 0.5:

| n        | node    |
|----------|---------|
| 6        | 0.997   |
| 7        | 1.000   |
| 8        | 0.996   |
| 10       | 0.984   |
| 30       | 0.915   |
| → ∞      | 0.866   |

The curve overshoots the asymptote by about 15% at the peak.

More sharply, for every `c > 0` with `c ≤ 1`, the translated circle contains the point `(1, c)`, and the fixed chord family contains exactly one positive-slope chord through that point: the chord with

    tan(π/t*) = c,   i.e.   t* = π / arctan(c).

At that real parameter, the forward intersection has `x = 1`, so the curve reaches node `= 1` exactly. Since the asymptote is `√(1 − c²) < 1`, every positive-`c` curve overshoots its asymptote. For `c = 0.5`, this gives `t* = π / arctan(0.5) ≈ 6.775`, which is why the integer samples peak near `n = 7`.

At `c = −0.5`, there is no analogous event: the point `(1, c)` lies below the x-axis, outside the positive-slope chord family. The curve is monotone increasing from `(0, 2)` to the same asymptote `0.866`.

**Geometric interpretation.** The positive-`c` overshoot is not just qualitative. Raising the circle puts `(1, c)` on the circle above the x-axis, and one member of the fixed chord family passes exactly through that point, forcing the right-pane curve up to node `= 1` before it relaxes back to the asymptote `√(1 − c²)`. Lowering the circle moves `(1, c)` below the x-axis, so this mechanism disappears.

### Symmetry-breaking

Unlike arc-flattening (§2), translation is not symmetric in its parameter:

- **c > 0:** non-monotone; reaches node `= 1` at `t* = π / arctan(c)` and so overshoots the asymptote.
- **c = 0:** monotone; reaches asymptote = 1.
- **c < 0:** monotone increasing; approaches the same asymptote `√(1 − c²)` from below.

One clean way to see the sign effect is to parameterize the translated circle by its own angle: write the forward intersection as

    (x, y) = (cos θ, c + sin θ).

The chord condition `y/x = tan(π/t)` becomes

    sin(π/t − θ) = c cos(π/t),

so for `|c| ≤ 1`,

    θ(t, c) = π/t − arcsin(c cos(π/t)),
    node(t, c) = cos θ(t, c).

If `u = π/t`, then

    dθ/du = 1 + c sin(u) / √(1 − c² cos²(u)),

which is nonnegative for `|c| ≤ 1` because `√(1 − c² cos²(u)) ≥ |c| sin(u)` on `[0, π/2]`; since `u` decreases as `t` increases, `θ(t, c)` decreases with `t`. When `c > 0`, `θ` starts positive and ends negative, so it crosses `0` once; that crossing is exactly the peak `node = 1`. When `c < 0`, `θ` stays nonnegative, so `node = cos θ` increases monotonically. Translation in the `+y` and `−y` directions therefore produce genuinely different right-pane behavior even though the circles themselves are mirror images in the left pane.

### Special cases at |c| = 1

**c = 1 (circle tangent to origin from above).** The formula collapses:

node(t, 1) = cos(π/t) · (sin(π/t) + √(sin²(π/t))) = cos(π/t) · 2·sin(π/t) = sin(2π/t).

A clean closed form. The pseudo-Chebyshev construction at c = 1 produces the sequence **sin(2π/n)**. Peak at n = 4 where sin(π/2) = 1. Asymptote 0 as n → ∞. The angle-doubling identity sin(2x) = 2 sin(x) cos(x) is what connects the original cos(π/n) sequence (at c = 0) to the sin(2π/n) sequence (at c = 1).

**c = −1 (circle tangent to origin from below).** The formula also collapses, but to something degenerate:

node(t, −1) = cos(π/t) · (−sin(π/t) + sin(π/t)) = 0 for every t.

Every chord is tangent to the circle at the origin, with no other forward-direction intersection. The construction degenerates to the constant 0.

So c = 1 is a nondegenerate limit (produces the sin(2π/n) sequence, related to the original by angle-doubling), while c = −1 is a degenerate collapse (every node becomes 0). Another instance of translation's asymmetry.

### What this reveals

- **Translation is a non-similar, symmetry-breaking deformation.** Unlike uniform scaling (§1), it changes shape. Unlike arc-flattening (§2), it is sign-sensitive.
- **Asymptote-symmetry without path-symmetry.** √(1 − c²) depends only on |c|, but the path each curve takes to its asymptote depends strongly on the sign of c.
- **The special rational value disappears immediately.** For example, `node(3, 1/2) = (√3 + √15) / 8`, so the rational value `node(3, 0) = 1/2` is destroyed as soon as the circle is translated.
- **c = 1 is a clean secondary construction.** sin(2π/n) is a classical sequence, and it emerges from the pseudo-Chebyshev setup simply by sliding the circle up until it kisses the origin. The operation is entirely geometric; the identity is what's revealing.

**Demonstration.** See `corners/translation.sage` and `figures/pseudo_chebyshev_translation.png`. Three rows at c = 0.5, c = 0, c = −0.5. Left column: translated circle with the fixed chords and crossing markers. Right column: node-sequence curve with integer stems, and asymptote √(1 − c²) annotated. The overshoot at c = 0.5 is visible above the dashed asymptote; the monotone behavior at c = −0.5 is visible below it.

---

## §4. The leash framework

Constraints on the three deformations above that preserve specified properties of the right-pane node-sequence curve. The name is literal: each property of the right-pane curve that we want to preserve implies a leash on the deformation family — a boundary it cannot cross without breaking that property.

The starting example, visible in §3: what leashes the deformation so the right-pane curve does not bend backward?

### The fold mechanism (why the curve bends)

As t grows from 2 to ∞, the chord y = x·tan(π/t) rotates clockwise: its slope decreases monotonically from +∞ toward 0. The forward-direction crossing with the target curve (circle, deformed arc, whatever shape the deformation produces) traces a path in the plane. "Bending backward" means the x-coordinate of that crossing is not monotone in t — somewhere along the way the crossing's x-value reverses direction.

The canonical instance: translation at c > 0 (§3). The chord passes through the point (1, c) on the translated circle at the specific slope tan(π/t*) = c. At that instant, the crossing is at x = 1, the maximum x-value any forward intersection can achieve. Before t*, the crossing is in the upper arc at x < 1; after t*, in the lower arc, again at x < 1. The right-pane curve rises to x = 1, then retreats toward the asymptote √(1 − c²). The fold.

The exact way to package this is polar. Write θ = π/t, so θ decreases from π/2 to 0 as t increases. If each positive-slope chord from the origin meets the target in a unique forward point, write that point as

    γ(θ) = r(θ) (cos θ, sin θ).

Then the right-pane node is

    x(θ) = r(θ) cos θ.

The right-pane bends backward exactly when x(θ) has an interior extremum, i.e. when

    d/dθ [r(θ) cos θ] = 0

somewhere in 0 < θ < π/2. In the translated-circle example with c > 0, that interior extremum occurs at the visible point (1, c).

### The monotonicity leash

**Exact criterion.** In the star-shaped setting above, the right-pane curve is monotone increasing in t iff

    d/dθ [r(θ) cos θ] ≤ 0

throughout 0 < θ < π/2.

**Convenient sufficient condition.** A simple geometric way to guarantee that is: the forward-intersection locus itself is a graph y = f(x) on some interval [x_min, x_max], with f(x) ≥ 0, f strictly decreasing, and f(x_max) = 0. Then each positive slope m corresponds to a unique solution of f(x) = mx, and x increases as m decreases.

**Geometric restatement in that graph setting.** The reachable branch should run monotonically down to the x-axis, with its rightmost reachable point lying on the x-axis. If the forward-intersection locus instead extends to a reachable point with y > 0, then the chord family can hit an interior x-maximum before relaxing back toward the asymptote, which is exactly the fold mechanism seen in translation for c > 0.

### Leashes for the three deformation families

| Deformation | Parameter range | Monotonicity leash condition | Monotone? |
|---|---|---|---|
| Uniform scaling (r) | r > 0 | always satisfied (target is the circle of radius r; rightmost at (r, 0) on x-axis) | yes |
| Arc-flattening (d, convex-preserving) | d ∈ [0, 1] | always satisfied (the reachable branch is a decreasing graph ending at (1, 0)) | yes |
| Translation (c) | \|c\| ≤ 1 (studied regime) | c ≤ 0 (reachable branch ends on the x-axis iff c ≤ 0) | yes iff c ≤ 0 |

For translation, the threshold is c = 0. Any c > 0 makes the point (1, c) reachable by a positive-slope chord, and that chord forces the interior maximum x = 1.

### Hierarchy of properties by fragility

Monotonicity is the loosest nontrivial property. Stricter properties require tighter leashes.

1. **Monotonicity.** Leash: the forward-intersection locus stays in the monotone regime above, for example as a decreasing graph ending on the x-axis. Satisfied by uniform scaling, arc-flattening, and translation with c ≤ 0.
2. **Convex right-pane shape.** Leash: stronger than monotonicity. Uniform scaling preserves it exactly. Convex-preserving arc-flattening appears to preserve it as well, but in §2 this is still being treated as numerically supported rather than fully proved. For translation at c < 0, it again appears plausible but is not established here.
3. **Fixed asymptote at x = 1.** Leash: the x-axis endpoint of the forward-intersection locus stays at x = 1 throughout. Preserved by arc-flattening in d ∈ [0, 1); not preserved by uniform scaling (asymptote at r) or translation (asymptote at √(1 − c²)).
4. **Explicit cyclotomic control at integer samples.** Leash: the integer samples remain in the same explicit family `cos(π/n)` up to a fixed scale factor. The undeformed circle has this exactly. Rational uniform scalings preserve the degree pattern over ℚ; arbitrary real scalings preserve it only after normalization by r. Arc-flattening and translation destroy this immediately at nonzero deformation.
5. **The original Niven pair at n = 2, 3.** Leash: the target curve passes through the original sample points (0, 1) and (1/2, √3/2), hence giving node(2) = 0 and node(3) = 1/2 exactly. Only the undeformed unit circle has this. If one weakens the property to "rational at n = 2, 3", then rational uniform scalings preserve it.

### Stratification of the deformation space

The deformation space can be stratified by which properties are preserved:

- **Unit-circle point**: all five properties are present.
- **Uniform-scaling ray**: monotonicity and right-pane shape survive exactly; the asymptote rescales to x = r; normalized cyclotomic structure survives; absolute arithmetic over ℚ survives only for rational r.
- **Convex-target region** (convex-preserving arc-flattening): monotonicity survives; convex right-pane behavior is numerically robust; the asymptote stays at x = 1 for d < 1; explicit cyclotomic control is lost.
- **Monotone-target region** (includes downward translation c ≤ 0): monotonicity survives; stronger shape properties need separate checking; the asymptote moves; explicit cyclotomic control is lost.
- **General deformation** (upward translation c > 0, non-convex deformations): no monotonicity guarantee. Folds can appear.

The translation family straddles the monotone-target and general regions, with the dividing line at c = 0.

### The tightness–informativeness tradeoff

The leash framework makes an explicit tradeoff visible. A tighter leash preserves more properties but admits a narrower family of deformations and therefore reveals less. A looser leash admits a broader family and reveals more about what can break.

- The undeformed unit circle: tightest leash, preserves everything, reveals nothing.
- Uniform scaling: still a very tight leash; it preserves the normalized geometry and normalized sample structure, but not every absolute arithmetic feature.
- Convex arc-flattening: medium leash, preserves monotonicity and appears to preserve the same convex right-pane shape, while revealing the smooth/arithmetic decoupling.
- Translation at c > 0: loose leash, breaks monotonicity, reveals how folds form and how asymmetric deformations work.

The program's use of deformation is not to find the tightest leash (that would just confirm similarity invariances) but to choose the leash appropriate to the question being asked. If the question is "how does arithmetic structure respond to geometric deformation?", convex arc-flattening is the right leash — tight enough to preserve smooth regularity, loose enough to destroy cyclotomic depth.

### Open questions

- What is the cleanest geometric hypothesis weaker than "decreasing graph to the x-axis" but strong enough to imply the exact polar inequality d/dθ [r(θ) cos θ] ≤ 0?
- Is there a deformation that preserves algebraic depth but breaks monotonicity? Plausibly not among natural deformations, since algebraic depth is tied to the pseudo-Chebyshev's cyclotomic origin.
- What does the leash for a "combined" deformation (e.g., translation composed with scaling) look like? Presumably the intersection of the individual leashes, but with a subtler form when the deformations interact nonlinearly.
- Can the leash framework be lifted to other n-gon constructs (`n-gons/N-GON-WHOLENESS.md`)? What counts as "bending backward" in the wholeness b_n(DH) sequence, say?
