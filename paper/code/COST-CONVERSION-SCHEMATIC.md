# COST-CONVERSION-SCHEMATIC

Companion to `figures/cost_conversion_schematic.png`, the
mult/add conversion economy schematic for [paper/IMPOSSIBILITY-OUTLINE.md](paper/IMPOSSIBILITY-OUTLINE.md) §1.5.

![A 2D schematic, "The mult/add conversion economy". X-axis multiplicative cost μ; y-axis additive cost α. Top: italic grey ribbon "← bounded coefficients · unbounded coefficients →". Upper-left tan region: "ACHIEVABLE". A solid black concave curve — the actual frontier — runs upper-left to lower-right with three blue canon dots: Morgenstern (upper-left), AFW (middle-left), Winograd (lower-right); "T(P) thresholds (canon)" labels them collectively. A dashed red curve below dips near the middle: "counterfactual δ=0 frontier (unreachable)". Between them a hatched red gap is widest at the middle and tapers toward both ends. A red double-headed vertical arrow at the middle spans the gap, marked δ, annotated "Bridge claim (§6.2): descent past T(P) ⟺ δ=0 at boundary". Mustard bidirectional arrows tangent to the frontier near Morgenstern: "conversion strategies (trade α↔μ)". Below the actual frontier: light grey region, italic "FFT-style methods do not reach below the frontier".](../../figures/cost_conversion_schematic.png)

The figure is built by
[paper/code/build_cost_conversion_schematic.py](paper/code/build_cost_conversion_schematic.py).

## Intent

The figure orients the reader to the mult/add conversion economy
*before* §3 lays out the four canon frameworks and §6 runs the
impossibility argument. It is a setup picture, not a proof picture.

Two axes, both abstract cost measures:

- `μ` — multiplicative cost (number of multiplications under bilinear /
  rational-equivalence accounting; §1.2).
- `α` — additive cost (number of additions, sensitive to coefficient
  regime; §1.3).

Three structural features:

1. **The actual frontier (solid black).** The lower-left boundary of
   the achievable region. FFT-style methods sit on or above it;
   conversion strategies (§1.5) move along it, trading `μ` for `α` or
   vice versa.
2. **The counterfactual `δ = 0` frontier (dashed red).** Where methods
   *would* sit if the irreducible transaction cost were zero. Coincides
   with the actual frontier far from the regime boundary; dips below
   near it.
3. **The δ-gap (hatched red).** The region between actual and
   counterfactual. Its height at any point is `δ` — the irreducible
   transaction cost at that location in the conversion economy. The
   gap's structure — widest at the regime boundary, tapering toward
   both corners — visualizes that `δ` is regime-localized rather
   than uniform across the plane.

Three claims read off the picture:

- **Canon thresholds sit on the actual frontier near the boundary.**
  Morgenstern, AFW, Winograd are marked with named dots — not as the
  boundary itself, but as the canon points the program engages with.
- **The Bridge equivalence (§6.2)** is shown as a double-headed
  vertical arrow at the boundary spanning the δ-gap, with `⟺`
  language: descent past `T(P)` ⟺ zeroing `δ` at the boundary. The
  arrow's two heads encode both directions of the equivalence.
- **The impossibility rule-out** is visualized as the greyed
  below-frontier region: FFT-style methods do not reach below the
  frontier, and the counterfactual frontier is labeled "unreachable"
  to make the impossibility-theorem verdict explicit on the figure.

## Honesty notes

- **Schematic register.** No numeric tick labels; the axes carry
  qualitative meaning (`μ` more multiplications → right; `α` more
  additions → up). The frontier shape, the δ-gap height, and the
  canon-point placements are illustrative — they convey the structure
  the §6.2 Bridge claim names, not specific numerical bounds. The
  actual frontier shape for any concrete cost model is part of §3,
  not §1.5.
- **Bridge-side only.** The figure visualizes the §6.2 Bridge claim
  (the equivalence between threshold improvement and gap-crossing).
  It does not visualize the §6.4 Separation claim (`δ = 0` outside
  the native closure class) or the §6.5 Native drift claim (bounded
  per-operation effect on `δ`). Those are at
  [figures/delta_phase_plot.png](figures/delta_phase_plot.png) /
  [paper/code/COASE-PHASE.md](paper/code/COASE-PHASE.md).
- **Regime is a parameter, not a region of the plane.** §1.4's
  bounded/unbounded coefficient distinction is a parameter of the
  cost model, not a coordinate. The figure does not partition the
  `(μ, α)` plane into regime regions. The "← bounded · unbounded →"
  ribbon at the top of the plot indicates the boundary axis between
  regimes without claiming one side of the plane "is" one regime.
- **Canon points are not the boundary.** Morgenstern, AFW, and
  Winograd are placed on the frontier as canon thresholds; none of
  them is identified as "the regime boundary." The boundary is where
  the δ-gap is widest, marked by the Bridge arrow's location, not
  by any one canon paper.
- **Counterfactual ≠ tighter bound.** The dashed red curve labeled
  "counterfactual δ=0 frontier (unreachable)" represents what the
  Bridge claim says is unreachable, not a tighter bound someone
  could try to prove. The figure visualizes the impossibility
  theorem's verdict at the schematic level.

## Where it sits

- Figure file: [figures/cost_conversion_schematic.png](figures/cost_conversion_schematic.png)
- Build script: [paper/code/build_cost_conversion_schematic.py](paper/code/build_cost_conversion_schematic.py)
- Companion outline section: [paper/IMPOSSIBILITY-OUTLINE.md](paper/IMPOSSIBILITY-OUTLINE.md) §1.5 (with re-references at §3, §4, §6.2)
- Companion closure-class figure: [paper/code/COASE-PHASE.md](paper/code/COASE-PHASE.md) (the §6.5 phase plot, where Separation and Native drift live)
- Methodological precedent for transaction-cost vocabulary: [memos/COASE-FRICTION-AND-SPECIALISTS.md](memos/COASE-FRICTION-AND-SPECIALISTS.md)
