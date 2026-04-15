# STRIP-AND-SUBPOLYGON

The link between the Archimedean strip-flip picture (`n-gons/ARCHIMEDEAN-STRIP-FLIP.md`) and the subpolygon construction (`tangencies/SUBPOLYGON.md`). One short file whose only job is to say that the two are the same object seen from two angles.

## Setup recap

Regular n-gon circumscribed around the unit incircle, anchored so that one tangency sits at `(1, 0)`. Tangency point `k` is at angle `2π k / n`, for `k = 0, …, n − 1`.

Unroll the annulus `{1 ≤ r ≤ 2}` to the strip

$$
x = \theta / (2\pi) \in [0, 1], \qquad y = r - 1 \in [0, 1].
$$

The incircle `r = 1` is the bottom edge `y = 0`. The n-gon tangency points sit on the strip floor at

$$
x_k = k / n, \qquad y = 0.
$$

## The link

Fix integer `DH ≥ 1` and draw a `DH`-grid on the strip: vertical lines at `x = m / DH`, for `m = 0, …, DH − 1`. A tangency point at `x_k = k / n` lies on a `DH`-gridline iff

$$
\frac{k}{n} = \frac{m}{DH}
\iff n \mid k \cdot DH,
$$

which is exactly the whole-position test from `SUBPOLYGON.md`. So the subpolygon construction is, on the strip floor, the **lattice intersection**

$$
\tfrac{1}{n}\mathbb Z / \mathbb Z \;\cap\; \tfrac{1}{DH}\mathbb Z / \mathbb Z
\;=\;
\tfrac{1}{\gcd(n, DH)}\mathbb Z / \mathbb Z.
$$

The whole positions are the common points of the two rational lattices on `ℝ / ℤ`, and the gcd theorem for subpolygons is the standard lattice-intersection identity on `S¹`. The "regular anchored `g`-gon on the shared incircle" is literally the image of that intersection back on the circle.

This makes the subpolygon construction feel less strange. It is commensurability between two rational subdivisions of `S¹`, dressed up as a polygon question.

## The flip side

Unit-circle inversion `r ↦ 1/r` fixes the incircle `r = 1` setwise (and pointwise). The subpolygon lives entirely on the incircle — on the inversion-invariant locus. So the flip does nothing to subpolygon data.

What the flip *does* do is act on the corners. The n-gon corners sit at radius `sec(π/n)` in the original annulus and invert to radius

$$
\cos(\pi / n) = \text{node}(n),
$$

the pseudo-Chebyshev node sequence of `corners/PSEUDO-CHEBYSHEV-NODES.md`. The tangency points — where the subpolygon lives — and the corners — where the pseudo-Chebyshev nodes live — are the two fixed-and-inverted faces of the same n-gon.

| Object | Location on n-gon | Radius | Role under inversion |
|---|---|---|---|
| Tangency point `k` | edge midpoint | `1` | fixed |
| Corner `k` | vertex | `sec(π/n)` | sent to `cos(π/n)` |

Subpolygon-theoretic content lives on the first row; pseudo-Chebyshev content lives on the second. Both are derived from the same anchored regular n-gon on the same incircle; the inversion is what exchanges their radial locations.

## What this changes

Nothing mathematically new — the gcd theorem in `SUBPOLYGON.md` is unchanged, and the pseudo-Chebyshev node formula is unchanged. What changes is the organizational picture:

- Subpolygons and pseudo-Chebyshev nodes are not two unrelated constructions on the n-gon; they are the two natural things one can do with a regular anchored n-gon on a fixed incircle, split by which part of the n-gon (edge midpoints vs. corners) you look at.
- The strip-flip is the visualization that makes this split visible at a glance.
- The `DH`-grid on the strip floor is the right visualization for the subpolygon construction. A `DH`-grid plus the n-gon tangency lattice is the entire content of the whole-position test.

## Pointers

- `tangencies/SUBPOLYGON.md` — the subpolygon construction and gcd theorem.
- `n-gons/ARCHIMEDEAN-STRIP-FLIP.md` — the strip and flip constructions.
- `corners/PSEUDO-CHEBYSHEV-NODES.md` — the corner side of the same n-gon.
- `tangencies/WHOLENESS.md` — the binary whole-position test that the subpolygon construction refines.
