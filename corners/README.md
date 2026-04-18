# corners

The vertex side of the regular-anchored-n-gon material. Sibling to `n-gons/` (which holds the edge-midpoint / tangency side and the bridge constructions). This directory holds the pseudo-Chebyshev node construction, the family of circle-transformations of that construction, and the leash framework that organizes them.

Each construct below is a narrative bestiary entry with three movements: *what it is*, *what it does*, *what it wants*. Full mathematical content lives in the linked file.

---

## The Pseudo-Chebyshev Nodes

For each integer n ≥ 2, inscribe a regular n-gon around the unit circle with apothem 1, anchored so that one edge is tangent at (1, 0). Draw the segment from the origin to the n-gon corner above the anchor — the point (1, tan(π/n)). The segment crosses the unit circle at (cos(π/n), sin(π/n)). The x-coordinate is the pseudo-Chebyshev node: node(n) = cos(π/n). One distinguished scalar per n.

What it does. Produces a monotone-increasing sequence toward 1 — node(2) = 0, node(3) = 1/2, node(4) = √2/2, and so on. Algebraic degree over ℚ equals φ(2n)/2, and ruler-and-compass constructibility holds iff 2n is in the Gauss–Wantzel set. The first non-constructible node and the first cubic both appear at n = 7. The construction extends to a real-valued continuation on t ∈ [2, ∞); by Niven's theorem the only rational values on that continuation are at t = 2 and t = 3.

What it wants. To be a CREATI-program candidate object: explicit, closed-form, integer-indexed, with algebraic degree tied to the crystallographic ψ-function. A constructible circle-side analog of one mantissa value per representation resolution — a scalar at each n where the log-side has a scalar at each m.

→ `corners/PSEUDO-CHEBYSHEV-NODES.md`

---

## The Circle Transformations and the Leash Framework

Three continuous deformations of the pseudo-Chebyshev construction — uniform scaling (diagnostic foil, similarity), convex-preserving arc-flattening (non-similar, interesting), vertical translation (non-similar, sign-sensitive) — plus the leash framework that organizes them by which property each deformation preserves.

What it does. Watches the integer samples and the right-pane node-sequence curve respond when the underlying circle is transformed. Cyclotomic arithmetic is fragile under non-similar deformations; monotonicity survives unless translation goes positive; uniform scaling preserves the normalized sample structure exactly. The leash framework makes the tightness–informativeness tradeoff explicit: tighter leashes preserve more but reveal less, and the program's use of deformation is to choose the leash appropriate to the question.

What it wants. To make the smooth-vs-arithmetic decoupling concrete. A family of deformations where one reading (the smooth curve) stays well-behaved and another (the cyclotomic depth of integer samples) collapses — the continuity-frame squeeze, enacted on the circle side.

→ `corners/CIRCLE-TRANSFORMATIONS.md`

---

## Scripts

Each script produces a figure under `figures/` at the repo root:

- `corners/pseudo_chebyshev.sage` — static two-pane visualization of the pseudo-Chebyshev construction for n = 3, 4, 5, 6, 7, 8.
- `corners/pseudo_chebyshev_continuity.sage` — the real-t continuation of the node curve with integer samples overlaid, in both the unit-circle geometric pane and the node-sequence pane.
- `corners/uniform_scaling.sage` — the diagnostic-foil deformation: uniform r-scaling at r ∈ {1, 0.5, 0.25}.
- `corners/translation.sage` — the vertical-translation deformation at c ∈ {−0.5, 0, 0.5}, including the overshoot at c > 0.
- `corners/leash_plot_a.sage` — the monotonicity leash condition in a single panel, Marklof–Strömbergsson Figure 3 style.

---

## On adding a construct

A construct earns an entry here when it is (a) load-bearing across multiple program threads, and (b) defined by its own mathematical content rather than by being an adaptation of an external object. See `n-gons/README.md` §"On adding a construct" for the full criterion — this directory uses the same rule.
