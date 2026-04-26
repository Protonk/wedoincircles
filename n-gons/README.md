# n-gons

The edge-midpoint / tangency side of the regular-anchored-n-gon material.
Sibling to `corners/` (the vertex side); together they cover the two
fixed-and-inverted faces of the same anchored n-gon.

Contents:

- `N-GON-WHOLENESS.md` — wholeness apparatus (rationals k/n on the circle).
- `SUBPOLYGON.md` — gcd refinement of wholeness (`g_n(DH) = gcd(n, DH)`).
- `ARCHIMEDEAN-STRIP-FLIP.md` — strip + inversion bridge connecting tangency data to corner data.
- `CRYSTALLOGRAPHIC-RESTRICTION-BRIEF.md` — Bamberg–Cairns–Kilminster ψ-function; lattice-symmetry orders and the crystallographic restriction used throughout the n-gon material.
- `counting/` — counting apparatus subdirectory (compute-cost ledger candidates).
- Scripts (`*.py`, `*.sage`) — figure builders and counting utilities.

A construct earns an entry when load-bearing across multiple program threads
and defined by its own mathematical content. Domain-owned source briefs may
live here when the extracted result has become local infrastructure;
disciplines and program-moves stay in `BNHA/triad/`.
