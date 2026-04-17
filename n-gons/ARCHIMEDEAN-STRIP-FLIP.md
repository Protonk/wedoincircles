# ARCHIMEDEAN-STRIP-FLIP

The strip and flip constructions for the anchored-n-gon family, followed by the two organizational splits they make visible: the tangency-side subpolygon link on the strip floor, and the corner-side pseudo-Chebyshev / counting observable under inversion.

## 1. Setup

Fix a circle of radius 1 — the **incircle**. Circumscribe a sequence of regular n-gons around it (apothem = 1), each with an anchor side supported by the common tangent line `x = 1` and tangent to the circle at `(1, 0)`. Each n-gon has circumradius

$$R_n = \sec(\pi/n).$$

The circumscribed circle of the n-gon — the **n-cir** — has radius $R_n$. The 3-cir has radius $R_3 = \sec(\pi/3) = 2$.

The construction uses only the range $n = 3, 4, 5, \ldots$. The incircle is the limiting inner boundary ($n \to \infty$, $R_n \to 1$). The 3-cir is the fixed outer boundary.

---

## 2. The strip

Map the annular region $\{1 \leq r \leq 2\}$ to a flat strip by:

$$x = \frac{\theta}{2\pi} \in [0, 1], \qquad y = \frac{r - 1}{R_3 - 1} = r - 1 \in [0, 1].$$

The angular coordinate $\theta$ wraps: $x = 0$ and $x = 1$ are identified. The incircle maps to $y = 0$; the 3-cir maps to $y = 1$.

Each n-cir maps to the horizontal line

$$y_n = R_n - 1 = \sec(\pi/n) - 1.$$

Each edge of the n-gon maps to a secant arc in the strip. Edge $k$ (tangent to the incircle at angle $2\pi k/n$) satisfies $r = \sec(\theta - 2\pi k/n)$ in polar coordinates, and spans $\theta \in \bigl[(2k-1)\pi/n,\,(2k+1)\pi/n\bigr]$. In the strip this is the curve

$$y(x) = \sec\!\left(2\pi\!\left(x - \tfrac{k}{n}\right)\right) - 1$$

over $x \in \bigl[(2k-1)/(2n),\,(2k+1)/(2n)\bigr]$ modulo `1`.

Each arc touches $y = 0$ at its midpoint (tangency with the incircle) and rises to $y_n$ at both endpoints (the corners of the n-gon). The strip is produced by `n-gons/strip.py`, which writes `figures/archimedean_strip.png`.

---

## 3. The flip

Apply unit-circle inversion to the original annulus $\{1 \leq r \leq 2\}$: in Euclidean coordinates this is $x \mapsto x/|x|^2$, and in complex notation it is $z \mapsto 1/\overline z$. In polar coordinates it is exactly $r \mapsto 1/r$ at fixed $\theta$. This maps the annulus to

$$\left\{\tfrac{1}{2} \leq r \leq 1\right\}.$$

Under the inversion:

- The incircle ($r = 1$) is fixed and becomes the **outer** boundary.
- The 3-cir ($r = 2$) maps to $r = 1/2$ and becomes the **inner** boundary.
- Each straight edge of the n-gon (a line at distance 1 from the origin) maps to a circular arc satisfying $r = \cos(\theta - 2\pi k/n)$, spanning the same angular range as before.

The full inverted circle `r = \cos(\theta - 2\pi k/n)` meets the inner boundary `r = 1/2` at angles `2\pi k/n \pm \pi/3`, but the actual inverted edge arc is restricted to `\theta \in [(2k-1)\pi/n,(2k+1)\pi/n]`. So only the `n = 3` arc reaches the inner boundary. For `n \geq 4` the arc ends earlier, at radius `\cos(\pi/n) > 1/2`, and floats in the interior of the annulus.

The n-gon corners, originally at radius $\sec(\pi/n)$, invert to radius

$$\cos(\pi/n) = \mathrm{node}(n),$$

the pseudo-Chebyshev node sequence from `corners/PSEUDO-CHEBYSHEV-NODES.md`. The nodes now appear as radii rather than x-coordinates. The flipped annulus is produced by `n-gons/inside_out.py`, which writes `figures/archimedean_inside_out.png`.

---

## 4. Tangency side: the subpolygon link

The strip floor `y = 0` carries the n-gon tangency points at `x = k/n`. Fix integer `DH ≥ 1` and draw a `DH`-grid on the strip: vertical lines at `x = m / DH`, for `m = 0, …, DH − 1`. A tangency point at `x_k = k / n` lies on a `DH`-gridline iff

$$
\frac{k}{n} = \frac{m}{DH}
\iff n \mid k \cdot DH,
$$

which is exactly the whole-position test from `n-gons/SUBPOLYGON.md`. So the subpolygon construction is, on the strip floor, the **lattice intersection**

$$
\tfrac{1}{n}\mathbb Z / \mathbb Z \;\cap\; \tfrac{1}{DH}\mathbb Z / \mathbb Z
\;=\;
\tfrac{1}{\gcd(n, DH)}\mathbb Z / \mathbb Z.
$$

The whole positions are the common points of the two rational lattices on `ℝ / ℤ`, and the gcd theorem for subpolygons is the standard lattice-intersection identity on `S¹`. The "regular anchored `g`-gon on the shared incircle" is literally the image of that intersection back on the circle.

---

## 5. Corner side: pseudo-Chebyshev nodes and counting

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

There is also a second corner-side observable besides the pseudo-Chebyshev node sequence. In the strip's `(x, y)` coordinates, the Euclidean horizontal coordinate is

$$
X = (1+y)\cos(2\pi x),
$$

so the outside-out counting word `M_N` from `n-gons/counting/COUNTING.md` can be read as a corner-incidence count for equal-`X` contours on the same strip. Subpolygon asks which floor points lie on a `DH`-grid; counting asks which corner points lie on the same `X`-contour. See `n-gons/counting/COUNTING-AND-STRIP.md`.

---

## 6. What this changes

Nothing mathematically new — the gcd theorem in `n-gons/SUBPOLYGON.md` is unchanged, and the pseudo-Chebyshev node formula is unchanged. What changes is the organizational picture:

- Subpolygons and pseudo-Chebyshev nodes are not two unrelated constructions on the n-gon; they are the two natural things one can do with a regular anchored n-gon on a fixed incircle, split by which part of the n-gon (edge midpoints vs. corners) you look at.
- Counting extends the corner side further: not just one distinguished corner value per `n`, but the full incidence pattern of all corners against the strip observable `X=(1+y)\cos(2\pi x)`.
- The strip-flip is the visualization that makes this split visible at a glance.
- The `DH`-grid on the strip floor is the right visualization for the subpolygon construction. A `DH`-grid plus the n-gon tangency lattice is the entire content of the whole-position test.

---

## 7. Files

| File | Produces |
|---|---|
| `n-gons/strip.py` | `figures/archimedean_strip.png` |
| `n-gons/inside_out.py` | `figures/archimedean_inside_out.png` |

---

## 8. Pointers

- `n-gons/SUBPOLYGON.md` — the subpolygon construction and gcd theorem.
- `corners/PSEUDO-CHEBYSHEV-NODES.md` — the corner side of the same n-gon.
- `n-gons/counting/COUNTING-AND-STRIP.md` — the counting construction as the corner-incidence observable on the same strip.
- `n-gons/N-GON-WHOLENESS.md` — the binary whole-position test that the subpolygon construction refines.
