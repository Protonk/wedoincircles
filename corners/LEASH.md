# LEASH

Constraints on deformations of the pseudo-Chebyshev construction that preserve specified properties of the right-pane node-sequence curve. Companion to `corners/CONTINUITY.md`, `corners/DEFORMATION.md`, `corners/TRANSLATION.md`. The name is literal: each property of the right-pane curve that we want to preserve implies a leash on the deformation family — a boundary it cannot cross without breaking that property.

The starting example, visible in `TRANSLATION.md`: what leashes the deformation so the right-pane curve does not bend backward?

## The fold mechanism (why the curve bends)

As t grows from 2 to ∞, the chord y = x·tan(π/t) rotates clockwise: its slope decreases monotonically from +∞ toward 0. The forward-direction crossing with the target curve (circle, deformed arc, whatever shape the deformation produces) traces a path in the plane. "Bending backward" means the x-coordinate of that crossing is not monotone in t — somewhere along the way the crossing's x-value reverses direction.

The canonical instance: translation at c > 0. The chord passes through the point (1, c) on the translated circle at the specific slope tan(π/t*) = c. At that instant, the crossing is at x = 1, the maximum x-value any forward intersection can achieve. Before t*, the crossing is in the upper arc at x < 1; after t*, in the lower arc, again at x < 1. The right-pane curve rises to x = 1, then retreats toward the asymptote √(1 − c²). The fold.

The exact way to package this is polar. Write θ = π/t, so θ decreases from π/2 to 0 as t increases. If each positive-slope chord from the origin meets the target in a unique forward point, write that point as

    γ(θ) = r(θ) (cos θ, sin θ).

Then the right-pane node is

    x(θ) = r(θ) cos θ.

The right-pane bends backward exactly when x(θ) has an interior extremum, i.e. when

    d/dθ [r(θ) cos θ] = 0

somewhere in 0 < θ < π/2. In the translated-circle example with c > 0, that interior extremum occurs at the visible point (1, c).

## The monotonicity leash

**Exact criterion.** In the star-shaped setting above, the right-pane curve is monotone increasing in t iff

    d/dθ [r(θ) cos θ] ≤ 0

throughout 0 < θ < π/2.

**Convenient sufficient condition.** A simple geometric way to guarantee that is: the forward-intersection locus itself is a graph y = f(x) on some interval [x_min, x_max], with f(x) ≥ 0, f strictly decreasing, and f(x_max) = 0. Then each positive slope m corresponds to a unique solution of f(x) = mx, and x increases as m decreases.

**Geometric restatement in that graph setting.** The reachable branch should run monotonically down to the x-axis, with its rightmost reachable point lying on the x-axis. If the forward-intersection locus instead extends to a reachable point with y > 0, then the chord family can hit an interior x-maximum before relaxing back toward the asymptote, which is exactly the fold mechanism seen in translation for c > 0.

## Leashes for the three deformation families

| Deformation | Parameter range | Monotonicity leash condition | Monotone? |
|---|---|---|---|
| Uniform scaling (r) | r > 0 | always satisfied (target is the circle of radius r; rightmost at (r, 0) on x-axis) | yes |
| Arc-flattening (d, convex-preserving) | d ∈ [0, 1] | always satisfied (the reachable branch is a decreasing graph ending at (1, 0)) | yes |
| Translation (c) | \|c\| ≤ 1 (studied regime) | c ≤ 0 (reachable branch ends on the x-axis iff c ≤ 0) | yes iff c ≤ 0 |

For translation, the threshold is c = 0. Any c > 0 makes the point (1, c) reachable by a positive-slope chord, and that chord forces the interior maximum x = 1.

## Hierarchy of properties by fragility

Monotonicity is the loosest nontrivial property. Stricter properties require tighter leashes.

1. **Monotonicity.** Leash: the forward-intersection locus stays in the monotone regime above, for example as a decreasing graph ending on the x-axis. Satisfied by uniform scaling, arc-flattening, and translation with c ≤ 0.
2. **Convex right-pane shape.** Leash: stronger than monotonicity. Uniform scaling preserves it exactly. Convex-preserving arc-flattening appears to preserve it as well, but in `DEFORMATION.md` this is still being treated as numerically supported rather than fully proved. For translation at c < 0, it again appears plausible but is not established here.
3. **Fixed asymptote at x = 1.** Leash: the x-axis endpoint of the forward-intersection locus stays at x = 1 throughout. Preserved by arc-flattening in d ∈ [0, 1); not preserved by uniform scaling (asymptote at r) or translation (asymptote at √(1 − c²)).
4. **Explicit cyclotomic control at integer samples.** Leash: the integer samples remain in the same explicit family `cos(π/n)` up to a fixed scale factor. The undeformed circle has this exactly. Rational uniform scalings preserve the degree pattern over ℚ; arbitrary real scalings preserve it only after normalization by r. Arc-flattening and translation destroy this immediately at nonzero deformation.
5. **The original Niven pair at n = 2, 3.** Leash: the target curve passes through the original sample points (0, 1) and (1/2, √3/2), hence giving node(2) = 0 and node(3) = 1/2 exactly. Only the undeformed unit circle has this. If one weakens the property to "rational at n = 2, 3", then rational uniform scalings preserve it.

## Stratification of the deformation space

The deformation space can be stratified by which properties are preserved:

- **Unit-circle point**: all five properties are present.
- **Uniform-scaling ray**: monotonicity and right-pane shape survive exactly; the asymptote rescales to x = r; normalized cyclotomic structure survives; absolute arithmetic over ℚ survives only for rational r.
- **Convex-target region** (convex-preserving arc-flattening): monotonicity survives; convex right-pane behavior is numerically robust; the asymptote stays at x = 1 for d < 1; explicit cyclotomic control is lost.
- **Monotone-target region** (includes downward translation c ≤ 0): monotonicity survives; stronger shape properties need separate checking; the asymptote moves; explicit cyclotomic control is lost.
- **General deformation** (upward translation c > 0, non-convex deformations): no monotonicity guarantee. Folds can appear.

The translation family straddles the monotone-target and general regions, with the dividing line at c = 0.

## The tightness–informativeness tradeoff

The leash framework makes an explicit tradeoff visible. A tighter leash preserves more properties but admits a narrower family of deformations and therefore reveals less. A looser leash admits a broader family and reveals more about what can break.

- The undeformed unit circle: tightest leash, preserves everything, reveals nothing.
- Uniform scaling: still a very tight leash; it preserves the normalized geometry and normalized sample structure, but not every absolute arithmetic feature.
- Convex arc-flattening: medium leash, preserves monotonicity and appears to preserve the same convex right-pane shape, while revealing the smooth/arithmetic decoupling.
- Translation at c > 0: loose leash, breaks monotonicity, reveals how folds form and how asymmetric deformations work.

The program's use of deformation is not to find the tightest leash (that would just confirm similarity invariances) but to choose the leash appropriate to the question being asked. If the question is "how does arithmetic structure respond to geometric deformation?", convex arc-flattening is the right leash — tight enough to preserve smooth regularity, loose enough to destroy cyclotomic depth.

## Open questions

- What is the cleanest geometric hypothesis weaker than "decreasing graph to the x-axis" but strong enough to imply the exact polar inequality d/dθ [r(θ) cos θ] ≤ 0?
- Is there a deformation that preserves algebraic depth but breaks monotonicity? Plausibly not among natural deformations, since algebraic depth is tied to the pseudo-Chebyshev's cyclotomic origin.
- What does the leash for a "combined" deformation (e.g., translation composed with scaling) look like? Presumably the intersection of the individual leashes, but with a subtler form when the deformations interact nonlinearly.
- Can the leash framework be lifted to other n-gon constructs (`tangencies/WHOLENESS.md`)? What counts as "bending backward" in the wholeness b_n(DH) sequence, say?

