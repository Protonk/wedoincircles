# Rotation Perturbation of the Outside-Out Sweep

The tangent-aligned construction described in [COUNTING.md](n-gons/counting/COUNTING.md) — the outside-out corner sweep that produces the counting-exhaustion word `M_N` and its Champernowne decimal `C_N` — is one point in an `(N−1)`-dimensional space of independent polygon rotations. Nothing in the method of exhaustion requires that alignment; this memo records what happens when the polygons are rotated off of it.

## Two-polygon toy

Triangle fixed, square rotated by `θ ∈ [0, π/2]`, sweeping the count of distinct x-positions across all 7 vertices. Over 100,001 sampled angles the generic count is `6`; it drops below generic only at three isolated angles: `θ = 0` (count 3), `θ = π/4` (count 5), `θ = π/2` (count 3). Fraction of sampled angles with any coincidence: `3 × 10⁻⁵`.

![Toy chamber count for a fixed triangle and rotated square](../../figures/counting_rotation_toy_angles.png)

The picture makes the chamber claim concrete: the toy is almost everywhere constant at `6`, and the sampled coincidence set is reduced to three isolated angles.

## Higher-dimensional sampling

Three polygons (triangle, square, pentagon) with two free rotation angles: 50,000 random samples in balls of radius `10⁻¹, 10⁻², 10⁻³, 10⁻⁴` around a generic configuration find zero coincidences at any radius.

## Why coincidences are rare

Each condition "vertex `i` and vertex `j` share an x-coordinate" defines an algebraic hypersurface in rotation space; the full coincidence set is a finite union of such surfaces. That union is closed, has codimension `≥ 1`, and is nowhere dense. Around any generic configuration there is an open ball free of coincidences.

## Chamber picture

Most of parameter space is a chamber on which `M_N` is degenerate — every entry equal to `1`. A thin web of lower-dimensional surfaces separates the chambers. The tangent-aligned construction lives at a high-codimension intersection point on that web, where the many trivial coincidences forced by individual polygon symmetry pile up at once. `C_N` is constant on each open chamber (at the degenerate value) and jumps across coincidence surfaces.
