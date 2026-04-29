# TAU-PORTRAIT

![A two-panel scientific plot. Top panel: a lollipop chart of vertical stems rising and falling from a zero baseline across integer values from 3 to 60, with circular markers colored in green, orange, blue, red, purple, gold, and gray bands; green stars sit at the leftmost three positions and arrow callouts label "Niven zeros (crystallographic set)", a "positive bulge", and a "sign flip" near the early integers. Bottom panel: a log-log scatter of colored dots descending along a dashed reference line from upper-left to lower-right, with the same color palette as the top panel.](../figures/tau_portrait.png)

The τ portrait at `figures/tau_portrait.png` (built by `corners/tau_portrait.py`) is a two-panel figure showing the circle-side residue

    τ(n) = 2·cos(2π/n) − round(2·cos(2π/n)),    n ≥ 3,

across n ∈ [3, 60]. τ is bounded in [−1/2, 1/2], defined only on the integers, and is the circle-side analog of Landfall's floating-point residue ε(m) = log₂(1 + m) − m. The portrait is the τ-side counterpart to plotting ε at its dyadic sample points.

The upper panel is a stem plot on linear y-axis: one stem per integer n ∈ [3, 60] running from y = 0 to y = τ(n), tipped with a filled circle, colored categorically by the algebraic degree φ(n)/2 of the value. Seven bins — from "deg 1 / Niven zeros" in green through "deg ≥ 7" in gray, with the cubic class (n ∈ {7, 9, 14, 18}) in orange-red and degree 2 (n ∈ {5, 8, 10, 12}) in navy. At the three n where τ vanishes — n ∈ {3, 4, 6} — the stem collapses to a green star sitting on y = 0 instead. Dashed horizontal guides mark y = 0 and y = ±1/2, the domain's sharp bounds; inline callouts flag the positive bulge at n ∈ {7, 8}, the sign flip at n = 9, and the τ → 0⁻ asymptote on the right tail.

The lower panel is `|τ(n)|` on log–log for all non-Niven n, with the Taylor-tail asymptote `4π²/n²` overlaid as a dashed reference line. Marker colors match the upper panel's degree classes. At small n (5, 7, 8) the markers sit noticeably below the asymptote; by n ≈ 15 they are on it; from there they trace the asymptote cleanly through n = 60.

Three things the figure makes visible without further prose: (i) the zero set of τ is exactly the crystallographic / Bravais rotation orders {1, 2, 3, 4, 6} — Niven's 1956 rational-cosine theorem in residue form; (ii) the only non-Niven n at which τ(n) > 0 are n ∈ {7, 8}, a two-element positive bulge forced by `2·cos(2π/n)` crossing 3/2 between n = 8 and n = 9; (iii) `|τ(n)|` approaches `4π²/n²` from below, sharing its 1/n² Taylor-tail rate with the Hurwitz isoperimetric gap at `corners/hurwitz_gap.sage`. For program context, see `memos/COUNTING-APPARATUS.md §(C)` and `rotations/CONTINUED-FRACTIONS-CROSSWALK.md`.

The visual fact that the small-n markers (n = 5, 7, 8) sit *below* the asymptotic line corresponds to a sharp closed-form pre-asymptotic floor:

    |τ(n)| ≥ 25(3 − √5) / (2 n²)  =  25 / (φ² n²)  ≈  9.5491 / n²,    n ∉ {1, 2, 3, 4, 6},

with equality at n = 5 (where |τ(5)| = 1/φ² is the regular-pentagon golden-ratio identity, since 2cos(2π/5) = 1/φ). The pre-asymptotic constant 25/φ² ≈ 9.55 is `≈ 0.242 · 4π²` — the n = 5 floor sits about a factor of 4 below the asymptotic constant 4π² ≈ 39.48 that the round-2 tail (n ≥ 9) approaches from below. The bound is sharp at n = 5 and not approached again: |τ(n)|·n² climbs from 12.10 at n = 7 to 26.51 at n = 8 to 37.91 at n = 9, then asymptotes to 4π² monotonically. Triad-discipline derivation and inverted-loan-structure commentary at [BNHA/triad/TAU-THREE-WAYS.md](BNHA/triad/TAU-THREE-WAYS.md).
