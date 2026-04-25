# COUNTING

Two first exploratory probes of the counting-exhaustion word `M_N`, using the outside-out corner sweep from [n-gons/outside_out.py](n-gons/outside_out.py). For background on the underlying annulus construction, see [n-gons/ARCHIMEDEAN-STRIP-FLIP.md](n-gons/ARCHIMEDEAN-STRIP-FLIP.md).

Files in this directory:

- [counting_utils.py](n-gons/counting/counting_utils.py): computation of `M_N`, decimal encodings, and the non-2 table.
- [build_counting.py](n-gons/counting/build_counting.py): generates the two exploratory figures and the extracted non-2 data.
- [build_x_multiplicity_raster.py](n-gons/counting/build_x_multiplicity_raster.py): renders a cumulative vertex-density heatmap on `x`, log color; reveals the arc manifold on which the integer-polygon vertices sit. Companion memo [X-DENSITY-RASTER.md](n-gons/counting/X-DENSITY-RASTER.md).
- [build_near_half_gaps.py](n-gons/counting/build_near_half_gaps.py): tracks nearest approach to the tested-empty guides `x = \pm 1/2`.
- [build_strip_observables.py](n-gons/counting/build_strip_observables.py): renders the strip bridge figure for counting vs subpolygon.
- [build_psi_table.py](n-gons/counting/build_psi_table.py): writes the `\psi`-aligned counting saturation table.
- [build_psi_stratification.py](n-gons/counting/build_psi_stratification.py): plots the outside-out vertex x-coordinates stratified by `ψ(n)`, with backbone and tested-empty guides as colored ticks. Companion memo [PSI-STRATIFICATION.md](n-gons/counting/PSI-STRATIFICATION.md).
- [case_seven.py](n-gons/counting/case_seven.py): three-panel small-case walkthrough at `n = 7`, comparing ruler-and-compass cost, algebraic degree `φ(2n)/2`, and counting word length `|M_n|` across `n ∈ [5, 11]`. Produces `figures/case_seven_three_costs.png` and writes `case_seven_table.tsv`. Closes the (D) "Candidate artifact" line of `memos/COUNTING-APPARATUS.md`; see that memo for the read-off.
- [non2_entries.tsv](n-gons/counting/non2_entries.tsv): tabular output of the second probe.
- [psi_counting_table.tsv](n-gons/counting/psi_counting_table.tsv): `n`, `\psi(n)`, six-field increments, and exact contour hits on `X \in \{\pm1,\pm1/2,0\}`.
- [case_seven_table.tsv](n-gons/counting/case_seven_table.tsv): per-`n` row for the three cost measures, written by `case_seven.py`.

Generated figures:

- [counting_non2_entries.png](figures/counting_non2_entries.png)
- [counting_x_multiplicity_raster.png](figures/counting_x_multiplicity_raster.png) — cumulative vertex-density heatmap on `x`, log color, arc-manifold visible (see [X-DENSITY-RASTER.md](n-gons/counting/X-DENSITY-RASTER.md)).
- [counting_near_half_gaps.png](figures/counting_near_half_gaps.png) — nearest approach to `x = \pm 1/2` through `n = 400`.
- [counting_strip_observables.png](figures/counting_strip_observables.png) — same strip, floor-grid vs corner-contour readout (see [n-gons/counting/COUNTING-AND-STRIP.md](n-gons/counting/COUNTING-AND-STRIP.md)).
- [counting_dual_convergence.png](figures/counting_dual_convergence.png) — decimal vs CF convergence rates (see [DECIMAL-CF-COMPLEMENTARITY.md](n-gons/counting/DECIMAL-CF-COMPLEMENTARITY.md)).
- [counting_increment_map.png](figures/counting_increment_map.png) — the `M_{N−1} → M_N` update, per-cell (see [COUNTING-AND-3DT.md](n-gons/counting/COUNTING-AND-3DT.md)).
- [counting_psi_stratification.png](figures/counting_psi_stratification.png) — outside-out x-support colored by `ψ(n)` class, with backbone and tested-empty guides (see [PSI-STRATIFICATION.md](n-gons/counting/PSI-STRATIFICATION.md)).

## Construction

The outside-out corner sweep runs over regular polygons `n = 3, 4, …, N`, each circumscribed around the unit circle with circumradius `sec(π/n)` and vertices at angles `(2k+1)π/n`. The x-coordinate of vertex `k` of polygon `n` is therefore:

```
x_{n,k} = sec(π/n) · cos((2k+1)π/n),   k = 0, 1, …, n − 1.
```

This anchoring puts two vertices of every polygon at `x = +1`, and for even `n` two more vertices at `x = −1`.

A vertical line sweeping left to right lands on one or more vertices at each x-coordinate that hosts any. `M_N` is the list of those counts, in sweep order. Initial examples:

- `M_5  = [1, 1, 2, 2, 6]`
- `M_6  = [1, 1, 4, 2, 2, 8]`
- `M_7  = [1, 1, 1, 4, 2, 2, 2, 2, 10]`
- `M_8  = [1, 1, 1, 6, 2, 2, 2, 2, 2, 2, 12]`
- `M_9  = [1, 1, 1, 1, 6, 2, 2, 2, 2, 2, 2, 2, 2, 14]`
- `M_10 = [1, 1, 1, 1, 8, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 16]`

The sweep is operationally simple — ticking each vertex as the line reaches it disambiguates stacked vertices — which is why it works as a ruler-and-pencil exercise.

For the comparison with the Three Distance Theorem, and for the claim that the useful analogy here is a compressed `N -> N+1` update law rather than a fixed-rotation orbit, see [n-gons/counting/COUNTING-AND-3DT.md](n-gons/counting/COUNTING-AND-3DT.md).

For the strip-side bridge to the subpolygon construction, and for the claim that counting is the corner-incidence observable on the same strip where subpolygon is the floor-lattice observable, see [n-gons/counting/COUNTING-AND-STRIP.md](n-gons/counting/COUNTING-AND-STRIP.md).

## 1. Word Barcode, `N = 5 .. 40`

The first probe is a row-by-row barcode of the multiplicity word `M_N`. Each row is one `N`; each column is a position in the word. The palette is:

- white: no entry yet,
- black: multiplicity `1`,
- blue: multiplicity `2`,
- warm colors: multiplicity `>= 3`.

What the barcode makes visible immediately:

- a long interior sea of `2`s,
- a left-hand staircase of `1`s that lengthens with `N`,
- a sparse set of warm exceptional columns,
- and a persistent heavy right edge where the final collision multiplicity grows with `N`.

This is already enough to show that `M_N` is not a noisy encoding. Most positions are rigidly generic (`2`), while a very small number of positions carry the interesting combinatorics.

## 2. Non-2 Extraction

The second probe throws away the sea of `2`s and records only the entries where `M_N` is not `2`. The scatter plot uses:

- x-axis: position in `M_N`,
- y-axis: `N`,
- color and marker size: multiplicity value.

This isolates the exceptional structure. Up through `N = 40`, the non-2 entries organize into the same exceptional families predicted by the six-field decomposition below:

- an initial block of `1`s on the left,
- a large exceptional column appearing relatively early in the word,
- an intermittent interior column of even multiplicity,
- and the terminal right-edge pileup.

The point of the extraction is that the six-field shape already appears to be the whole story: the live theorem target is not to discover additional interior families, but to prove that no cross-row non-backbone collisions exist beyond these fields.

## Structural Decomposition

For `N ≥ 4`, `M_N` factors into a six-field shape:

```
1×a   [count at x=−1]×1   2×b   [count at x=0]×1   2×c   [count at x=+1]×1
```

The `x = 0` field is present only when some `n ∈ [6, N]` satisfies `n ≡ 2 (mod 4)`; otherwise it collapses out.

Closed forms for each field:

- `a = ⌊(N−1)/2⌋`
- count at `x = −1`: `2⌊N/2⌋ − 2`
- `b = Σ L(n)` for `n = 3..N`
- count at `x = 0`: `2·|{n ∈ [6, N] : n ≡ 2 (mod 4)}|`
- `c = Σ R(n)` for `n = 3..N`
- count at `x = +1`: `2(N − 2)`

With per-polygon contributions:

- `L(n) = ⌊(n−1)/4⌋` for odd `n`, `(n−4)/4` for `n ≡ 0 (mod 4)`, `(n−6)/4` for `n ≡ 2 (mod 4)`
- `R(n) = ⌊(n−3)/4⌋` for odd `n`, `(n−4)/4` for `n ≡ 0 (mod 4)`, `(n−6)/4` for `n ≡ 2 (mod 4)`

Predicted `M_N` matches the directly-computed sequence for all `N = 4..25`.

Current conjectural stance: this six-field shape is complete for all `N`. Proving completeness is equivalent to classifying collisions `x_{n_1, k_1} = x_{n_2, k_2}` and showing that, away from the backbone values `{-2, -1, 0, +1}` and the within-polygon symmetry `k ↔ n - 1 - k`, the outside-out x-values are injective across the whole sweep.

This six-field shape is what the two probes are picking up. In the barcode, the left-hand staircase of `1`s is the `1×a` field, the interior sea of `2`s is the `2×b` and `2×c` fields, and the heavy right edge is the terminal `2(N−2)` entry. In the non-2 extraction, the three exceptional columns — the initial block of `1`s, the large early column, and the intermittent interior column of even multiplicity — are the `1×a` field and the two interior singletons at `x = −1` and `x = 0`. The right-edge pileup is the third singleton at `x = +1`.

![A 2D heatmap titled "Cumulative vertex-density raster of the outside-out sweep (semantic: density, not cluster multiplicity)". Horizontal axis "vertex x-coordinate" from -2 to about +1.2 with labeled ticks at -2, -1, -1/2, 0, +1/2, +1; vertical axis "polygon order N (cumulative through n ≤ N)" from 3 at the bottom to 40 at the top. The colormap is inferno on a log scale (deep purple at low density rising through magenta and orange to bright yellow at high density), with a vertical color bar on the right. Bright yellow vertical bands sit at the backbone positions x ∈ {-2, -1, 0, +1}, while two darker vertical stripes mark x = ±1/2 — the tested-empty guides. Dotted reference guides cut through these positions.](../../figures/counting_x_multiplicity_raster.png)

Cumulative vertex-density raster on `x`, log color: the backbone `x ∈ {-2,-1,0,+1}` reads as bright vertical bands with a `76 : 38 : 18 : 1` hierarchy, the interior arcs are the fixed-k vertex loci `x_k(N) = sec(π/N)·cos((2k+1)π/N)`, and the `x = ±1/2` stripes are visible as absence of light. See [X-DENSITY-RASTER.md](n-gons/counting/X-DENSITY-RASTER.md) for the full guide.

Binary run-length encoding of `M_N` does not compress: `2` in binary is `10`, so every run of `2`s becomes an alternating `1010…` pattern with no internal runs. The runs/bits ratio rises toward `1` as `N` grows.

## Running The Exploration

The figures and TSV were generated by:

```bash
sage -python n-gons/counting/build_counting.py
sage -python n-gons/counting/build_x_multiplicity_raster.py
sage -python n-gons/counting/build_near_half_gaps.py
sage -python n-gons/counting/build_convergence.py
sage -python n-gons/counting/build_increment_map.py
sage -python n-gons/counting/build_strip_observables.py
sage -python n-gons/counting/build_psi_table.py
sage -python n-gons/counting/build_psi_stratification.py
```

The scripts write their figures to `figures/`; `n-gons/counting/build_counting.py` also writes its tabular extraction to this directory.
