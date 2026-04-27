# COASE-PHASE

Companion to `figures/delta_phase_plot.png`, the
δ-algebra phase plot for [paper/IMPOSSIBILITY-OUTLINE.md](../IMPOSSIBILITY-OUTLINE.md) §6.

![A 2D phase plot, "The δ-algebra phase plot". X-axis amortization rate α (0 to 3.2); y-axis asymptotic floor δ_∞ (0 to 1.0). The whole plot is light-pink IMPOSSIBILITY, labeled "(slow-α mechanism)" upper-left and "(floor-dominated)" upper-right. A solid blue horizontal at floor ≈ 0.10 reads "Coase axiom: floor ≥ δ_min > 0"; below it a hatched blue strip is the Coase exclusion zone. Along floor = 0 from α ≈ 1.85 to 3.2 runs a thin green free-descent strip; a green star at its right end is labeled "FFT canon: free descent (α → ∞, floor = 0)". A vertical mustard hatched band at α ≈ 1.4 above the blue line holds a large mustard "?" annotated "debt #2: where exactly does the mechanism boundary sit? (additivity, amortization, bypass)". A red dot at (1.85, 0.60) is labeled "program working hypothesis". A dashed grey curved arrow sweeps from the red dot down-right to the green star, labeled "Lemma B: no finite composition zeros the floor — this descent route is blocked".](../../figures/delta_phase_plot.png)

The figure is built by
[paper/code/build_delta_phase_plot.py](build_delta_phase_plot.py).

## Intent

The figure visualizes the *algebra-vs-existence* distinction Coase 1937
names methodologically and FIRST-PROOF debt #2 carries forward. Two
axes of `δ`'s algebra are taken as a 2D projection:

- `α` — amortization rate. `δ_k ~ k^(-α)` under composition. Larger `α`
  means faster per-composition decay.
- `δ_∞` — asymptotic floor. The irreducible part of `δ` that survives
  composition and specialization.

The plot reads:

- The FFT canon (★) lives at `(α → ∞, floor = 0)` — the unreachable
  corner where descent would be free.
- The Coase axiom (solid blue line) puts the program above
  `floor = δ_min > 0` (Coase 1937, p. 390: specialists reduce, do not
  eliminate).
- Above the line: impossibility everywhere, but two distinct
  *mechanisms*. Left of the band, slow amortization makes cumulative
  cost run away. Right of the band, the positive floor still forces
  total cost to grow even with fast amortization.
- The mustard hatched band is debt #2 in the open: the mechanism
  boundary's exact location is what the algebra-of-`δ` sub-questions
  (additivity, amortization, bypass-resistance) must close.
- Lemma B in its current form is the existence claim that no finite
  composition zeros the floor — the dashed arrow is the descent route
  the program rules out.

## Honesty notes

- The two axes are a *projection* of higher-dimensional `δ`-algebra
  space (additivity across compositions, bypass-resistance under
  intermediation, representation-dependence). The full debt #2 list is
  not 2D.
- The Coase line height `δ_min` is the program's working hypothesis,
  not a proven number. Its stability under composition,
  specialization, and amortization is itself part of debt #2.
- The mechanism-boundary band is drawn at heuristic location and width
  for legibility; its precise functional form is debt #2's content.
- The Lemma B arrow encodes the existence claim already in hand. The
  band encodes what the algebra has not yet ruled out.

## Where it sits

- Figure file: [figures/delta_phase_plot.png](../../figures/delta_phase_plot.png)
- Build script: [paper/code/build_delta_phase_plot.py](build_delta_phase_plot.py)
- Companion outline section: [paper/IMPOSSIBILITY-OUTLINE.md](../IMPOSSIBILITY-OUTLINE.md) §6
- Methodological precedent: [memos/COASE-FRICTION-AND-SPECIALISTS.md](../../memos/COASE-FRICTION-AND-SPECIALISTS.md)
