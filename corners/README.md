# corners

The vertex side of the regular-anchored-n-gon material. Sibling to `n-gons/`
(the tangency side); together they cover the two fixed-and-inverted faces of
the same anchored n-gon.

Contents:

- `PSEUDO-CHEBYSHEV-NODES.md` — `node(n) = cos(π/n)`, one scalar per n.
- `CIRCLE-TRANSFORMATIONS.md` — deformations of pseudo-Chebyshev + leash framework.
- `HURWITZ-GAP.md` — isoperimetric gap of the inscribed regular n-gon.
- `HURWITZ-FIRST-BAND-CONCENTRATION.md` — companion theorem on first-band Parseval mass.
- `TAU-PORTRAIT.md` — τ(n) portrait construction.
- Scripts (`*.py`, `*.sage`) — figure builders for the constructs above.

A construct earns an entry when load-bearing across multiple program threads
and defined by its own mathematical content; the rule matches `n-gons/`'s.
