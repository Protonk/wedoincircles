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

The uniform r-shrink is a similarity transformation. `node(n, r) / r = cos(π/n)` is invariant in r; absolute Niven-rationals scale linearly (`node(2, r) = 0`, `node(3, r) = r/2`); the asymptote at x = r tracks the scaling. At r = 0 the construction degenerates to a point.

See `corners/uniform_scaling.sage` and `figures/pseudo_chebyshev_uniform_scaling.png`. The figure is a 3×2 grid showing the geometric construction (left column) and the node-sequence curve (right column) at r = 1, r = 0.5, and r = 0.25. The shape of the right-pane curve is identical across rows; only the horizontal extent changes.

![A 3×2 grid of subplots, titled "Uniform-scaling deformation: pseudo-Chebyshev at r = 1, 0.5, 0.25". Each row shares a layout: the left subplot is a "Geometric construction" with a black quarter-arc and a fan of colored rays piercing the arc at colored disks, with a black arrow pointing toward an anchor; the right subplot is "Node-sequence space" — a black curve rising from low n through colored integer-sample disks toward a vertical asymptote, with horizontal axis labeled "node value = r·cos(π/n)". Across the three rows the asymptote location moves from x=1 (top) to x=0.5 (middle) to x=0.25 (bottom); the curve shapes are identical and only the horizontal extent shrinks.](../figures/pseudo_chebyshev_uniform_scaling.png)

---

## §2. Convex-preserving arc-flattening

Flatten the quarter-circle arc into a vertical line segment without ever bending the arc the wrong way.

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

### Arithmetic collapse

The two rational node values at d = 0 — node(2) = 0 and node(3) = 1/2 — both disappear under the deformation, at d = 0⁺ and d ≈ 0.861 respectively. At d = 1, every surviving sample is at node = 1: one rational value shared by all n ≥ 4. Between the endpoints, the clean cyclotomic formula `cos(π/n)` is gone; the sample values are defined only implicitly by a mixed trigonometric/linear equation, so the explicit algebraic-degree control present at d = 0 has been lost.

At d = 0 the crossing is (cos(π/n), sin(π/n)) — both coordinates encode n. At d = 1 the crossing is (1, tan(π/n)) — only y encodes n; the x-coordinate is frozen at 1. Choosing x as the node picked up the degenerate direction.

For each fixed d < 1, the right-pane curve is smooth on its domain and numerically monotone increasing and convex as a graph of n against x. The whole curve compresses into the strip [d, 1) × [n_min(d), ∞) with

    n_min(d) = π / arctan((1 + d·(π/2 − 1)) / d),   d > 0.

At d = 1 the surviving integer samples are n = 4, 5, 6, …

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

See `corners/translation.sage` and `figures/pseudo_chebyshev_translation.png`. Three rows at c = 0.5, c = 0, c = −0.5. Left column: translated circle with the fixed chords and crossing markers. Right column: node-sequence curve with integer stems, and asymptote √(1 − c²) annotated. The overshoot at c = 0.5 is visible above the dashed asymptote; the monotone behavior at c = −0.5 is visible below it.

![A 3×2 grid of subplots, titled "Translation deformation: pseudo-Chebyshev with circle at (0, c) for c = +0.5, 0, -0.5". Each row pairs a "Geometric construction" on the left with a "Node-sequence space" on the right. The left subplots show a black circle whose center moves from (0, +0.5) at the top down to (0, 0) and (0, -0.5) at the bottom, each crossed by a fan of colored chords emanating from a black star at the origin, with a dashed vertical guide at x=1. The right subplots show a smooth black curve through colored integer-sample disks rising toward a vertical asymptote whose location moves with c — at x = √(1−c²) ≈ 0.866 in the top and bottom rows and x = 1 in the middle row.](../figures/pseudo_chebyshev_translation.png)

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

![A planar geometric plot bounded by axes from -1 to 1 in x and -1 to 1 in y. A solid black unit circle is centered at the origin; a dashed red circle bows from the left through the origin, and a dashed green circle mirrors it on the right. The lower half-plane below y=0 is shaded pale green and labeled "admissible region (target rightmost at y ≤ 0)". Thin gray rays radiate from the origin under the label "chord family (positive-slope rays from origin)". Dotted vertical guides through x=1 mark three points at (1, +0.5), (1, 0.0), and (1, -0.5), with side labels "lead" and small "(c = …)" tags. A small star marks the origin.](../figures/leash_plot_a.png)

### Hierarchy of properties by fragility

Monotonicity is the loosest nontrivial property. Stricter properties require tighter leashes.

1. **Monotonicity.** Leash: the forward-intersection locus stays in the monotone regime above, for example as a decreasing graph ending on the x-axis. Satisfied by uniform scaling, arc-flattening, and translation with c ≤ 0.
2. **Convex right-pane shape.** Leash: stronger than monotonicity. Uniform scaling preserves it exactly. Convex-preserving arc-flattening appears to preserve it as well, but in §2 this is still being treated as numerically supported rather than fully proved. For translation at c < 0, it again appears plausible but is not established here.
3. **Fixed asymptote at x = 1.** Leash: the x-axis endpoint of the forward-intersection locus stays at x = 1 throughout. Preserved by arc-flattening in d ∈ [0, 1); not preserved by uniform scaling (asymptote at r) or translation (asymptote at √(1 − c²)).
4. **Explicit cyclotomic control at integer samples.** Leash: the integer samples remain in the same explicit family `cos(π/n)` up to a fixed scale factor. The undeformed circle has this exactly. Rational uniform scalings preserve the degree pattern over ℚ; arbitrary real scalings preserve it only after normalization by r. Arc-flattening and translation destroy this immediately at nonzero deformation.
5. **The original Niven pair at n = 2, 3.** Leash: the target curve passes through the original sample points (0, 1) and (1/2, √3/2), hence giving node(2) = 0 and node(3) = 1/2 exactly. Only the undeformed unit circle has this. If one weakens the property to "rational at n = 2, 3", then rational uniform scalings preserve it.

