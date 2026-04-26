# VERTEXIOUS-ALGEBRA

The `n-gons/` register records the constitutive structure of the regular `n`-gon as the program's load-bearing approximation object. Three frames are recorded: vertex algebra and dual parametrizations; symmetry and divisor structure; counting register.

## Vertex algebra and parametrizations

The regular `n`-gon inscribed in the unit circle has vertex coordinates `(cos(2πk/n), sin(2πk/n))` algebraic of degree `φ(2n)/2`. These degrees carry multiplicative-complexity content via `fft/AUSLANDER-FEIG-WINOGRAD-1984-BRIEF.md` and `fft/WINOGRAD-1978-BRIEF.md`: the polygon's vertex algebra is a compute-cost object as well as an algebraic object. Two complementary parametrizations carry the program's calculations.

The arc-length parametrization underwrites Hurwitz Fourier coefficients on the lattice `1 + nℤ` (the closed forms are recorded in `paper/POLYGONAL-LEDGER.md`). The strip parametrization at `n-gons/ARCHIMEDEAN-STRIP-FLIP.md` flips this to coordinates `k/n` on a tangency axis and `sec(π/n) − 1` on a peak axis, with the position set `P_N = {k · 360°/n}` as the natively-Erasure-legal substrate. The first non-constructible `n = 7` is the program's lowest cubic anchor; it appears across closure-mismatch, crystallographic restriction, and counting.

## Symmetry and divisor structure

The crystallographic restriction at `n-gons/CRYSTALLOGRAPHIC-RESTRICTION-BRIEF.md` records the Bamberg–Cairns–Kilminster `ψ` function: rotation orders compatible with a Bravais lattice are exactly `{1, 2, 3, 4, 6}`. This is the symmetry-data complement of the algebraic-depth catalogue.

The prime-valuation form at `n-gons/SUBPOLYGON.md` extends `ψ` along the divisor lattice:

```text
v_p(g_n(DH)) = min(v_p(n), v_p(DH)).
```

This enacts the `ψ`-budget as a divisor-side fact, not a free combinatorial parameter. Subpolygon orders inherit a structured prime-budget rather than a free divisor lattice.

## Counting register

The outside-out counting word `M_N` at `n-gons/counting/COUNTING.md` is the program's primitive ledger for the polygon-circle gap. Three correspondences make it cross-register: with 3DT at `n-gons/counting/COUNTING-AND-3DT.md` (orbit-incidence ↔ counting-word equivalence); with the strip at `n-gons/counting/COUNTING-AND-STRIP.md` (strip-flip ↔ counting equivalence); and with Bresenham-midpoint at `n-gons/counting/BRESENHAM-MIDPOINT.md` (the `O(R)` integer-arithmetic upper bound in matched currency).

Adjacent counting-side investigations — `NEAR-HALF-GAPS`, `PSI-STRATIFICATION`, `ROTATION-PERTURBATION`, `THICK-SWEEP`, `X-DENSITY-RASTER`, `DECIMAL-CF-COMPLEMENTARITY`, `PSEUDO-CHAMPERNOWNE` — refine the ledger at named structural features.

`M_N` is the program's first candidate ledger; the second is `V_cert` at `(P3, A2)` developed at `fft/FOUR-FRAMEWORK-SYNTHESIS.md` and `memos/LEDGER-PIVOT-SEARCH.md`. Together they are the program's two compute-cost surfaces.

## Enabled and open

Enabled. The program's central object is constituted with explicit vertex algebra, two equivalent parametrizations, structured prime-budget, and a primitive counting ledger with three cross-register correspondences. The `n = 7` cubic anchor is load-bearing across closure-mismatch, crystallographic restriction, and counting.

Open. Whether `M_N` lifts to a primitive-op-count lower bound under a fixed compute model (the open ledger pivot at `memos/LEDGER-PIVOT-SEARCH.md`). Whether the `ψ`-budget admits an effective form across all subpolygon orders. Whether the strip and arc-length parametrizations agree across the Hurwitz gap to resolution beyond `R_n = 16π⁶/(45n⁴) + O(n⁻⁶)` recorded at `memos/STRIP-H1-HURWITZ-CLOSURE.md`.
