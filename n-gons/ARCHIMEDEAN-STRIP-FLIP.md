# ARCHIMEDEAN-STRIP-FLIP

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

Each arc touches $y = 0$ at its midpoint (tangency with the incircle) and rises to $y_n$ at both endpoints (the corners of the n-gon). The strip is produced by `strip.py`, which writes `figures/archimedean_strip.png`.

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

the pseudo-Chebyshev node sequence from `corners/PSEUDO-CHEBYSHEV-NODES.md`. The nodes now appear as radii rather than x-coordinates. The flipped annulus is produced by `inside_out.py`, which writes `figures/archimedean_inside_out.png`.

---

## 4. Files

| File | Produces |
|---|---|
| `strip.py` | `figures/archimedean_strip.png` |
| `inside_out.py` | `figures/archimedean_inside_out.png` |

---

## 5. Link to the subpolygon construction

The strip floor `y = 0` carries the n-gon tangency points at `x = k/n`. A `DH`-grid of vertical lines at `x = m/DH` intersects the tangency lattice in a cyclic subgroup of order `gcd(n, DH)`, reproducing the subpolygon construction of `tangencies/SUBPOLYGON.md`. The flip exchanges corners at `sec(π/n)` with pseudo-Chebyshev nodes at `cos(π/n)` while fixing the incircle, so subpolygons and pseudo-Chebyshev nodes are the two fixed-and-inverted faces of the same n-gon. See `n-gons/STRIP-AND-SUBPOLYGON.md`.
