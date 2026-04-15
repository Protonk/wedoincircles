# TRANSLATION

A third deformation of the pseudo-Chebyshev construction: translate the circle vertically while keeping the chords fixed. Complements `corners/DEFORMATION.md` (the arc-flattening and uniform-scaling examples). Where arc-flattening was non-similar and interesting, and uniform-scaling was similar and mostly diagnostic, translation is non-similar and symmetry-breaking: raising the circle produces structurally different behavior from lowering it by the same amount.

## The construction under translation

Keep the chords as in the original pseudo-Chebyshev setup: for each n ≥ 3, the chord is the line from the origin to (1, tan(π/n)). For n = 2, use the limiting chord: the positive y-axis. These chords do not move with the deformation.

Translate the circle: instead of being centered at the origin with radius 1, it is centered at (0, c) with radius 1, for a translation parameter c. The circle–chord intersections change, and the x-coordinate of the forward-direction intersection is the new node.

Substituting y = x·tan(π/n) into x² + (y − c)² = 1 and simplifying:

x² − c·sin(2π/n)·x + (c² − 1)·cos²(π/n) = 0.

Two roots. For c ∈ (−1, 1), the origin is inside the translated circle (distance from origin to (0, c) is |c| < 1 = radius), so one root is negative and one positive. Take the positive root:

**node(n, c) = cos(π/n) · (c · sin(π/n) + √(1 − c²·cos²(π/n))).**

At c = 0 this reduces to node = cos(π/n), recovering the original construction.

**When does the chord cross the translated circle?** The perpendicular distance from (0, c) to the chord equals |c|·cos(π/n). The line meets the translated circle iff that distance is ≤ 1, i.e., **|c| ≤ sec(π/n)**. In the regime emphasized here, `|c| ≤ 1`, every chord with `n ≥ 3` meets the circle, and the forward-direction root above is the relevant one. Outside that regime some chords miss entirely, and once the origin lies outside the circle one must also distinguish first and second forward intersections; this note does not pursue that case.

## Worked example

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

## The asymptote: √(1 − c²)

As t → ∞, cos(π/t) → 1 and sin(π/t) → 0, so

node(t, c) → 1·(0 + √(1 − c²)) = √(1 − c²).

Symmetric in c: the asymptotes at c = 0.5 and c = −0.5 agree at √0.75 ≈ 0.866. Geometrically, as t → ∞ the chord approaches the x-axis, and the translated circle intersects the x-axis at x = ±√(1 − c²).

## The overshoot: c > 0 curve is non-monotone

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

## Symmetry-breaking

Unlike arc-flattening (DEFORMATION.md's Deformation 1), translation is not symmetric in its parameter:

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

## Special cases at |c| = 1

**c = 1 (circle tangent to origin from above).** The formula collapses:

node(t, 1) = cos(π/t) · (sin(π/t) + √(sin²(π/t))) = cos(π/t) · 2·sin(π/t) = sin(2π/t).

A clean closed form. The pseudo-Chebyshev construction at c = 1 produces the sequence **sin(2π/n)**. Peak at n = 4 where sin(π/2) = 1. Asymptote 0 as n → ∞. The angle-doubling identity sin(2x) = 2 sin(x) cos(x) is what connects the original cos(π/n) sequence (at c = 0) to the sin(2π/n) sequence (at c = 1).

**c = −1 (circle tangent to origin from below).** The formula also collapses, but to something degenerate:

node(t, −1) = cos(π/t) · (−sin(π/t) + sin(π/t)) = 0 for every t.

Every chord is tangent to the circle at the origin, with no other forward-direction intersection. The construction degenerates to the constant 0.

So c = 1 is a nondegenerate limit (produces the sin(2π/n) sequence, related to the original by angle-doubling), while c = −1 is a degenerate collapse (every node becomes 0). Another instance of translation's asymmetry.

## What this reveals

- **Translation is a non-similar, symmetry-breaking deformation.** Unlike uniform scaling, it changes shape. Unlike arc-flattening, it is sign-sensitive.
- **Asymptote-symmetry without path-symmetry.** √(1 − c²) depends only on |c|, but the path each curve takes to its asymptote depends strongly on the sign of c.
- **The special rational value disappears immediately.** For example, `node(3, 1/2) = (√3 + √15) / 8`, so the rational value `node(3, 0) = 1/2` is destroyed as soon as the circle is translated.
- **c = 1 is a clean secondary construction.** sin(2π/n) is a classical sequence, and it emerges from the pseudo-Chebyshev setup simply by sliding the circle up until it kisses the origin. The operation is entirely geometric; the identity is what's revealing.

## Demonstration

See `corners/translation.sage` and `figures/pseudo_chebyshev_translation.png`. Three rows at c = 0.5, c = 0, c = −0.5. Left column: translated circle with the fixed chords and crossing markers. Right column: node-sequence curve with integer stems, and asymptote √(1 − c²) annotated. The overshoot at c = 0.5 is visible above the dashed asymptote; the monotone behavior at c = −0.5 is visible below it.
