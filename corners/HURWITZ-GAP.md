# HURWITZ-GAP

![A log-log plot whose three series — a black dashed line, a column of blue dots, and a column of red plus markers — overlap so closely that they trace a single straight diagonal descending from the upper left to the lower right across roughly seven decades on the horizontal axis and six decades on the vertical. A narrower inset panel sits below sharing the horizontal axis: a magenta curve rises on linear-y from near zero to a flat asymptote, with a small annotation pointing at the plateau.](../figures/hurwitz_gap_rate.png)

The Hurwitz-gap rate figure at `figures/hurwitz_gap_rate.png` (built by `corners/hurwitz_gap.sage`) plots the isoperimetric gap

    Δ_n  =  L_n² − 4π A_n

of the inscribed regular n-gon over `n ∈ [3, 100]`, computed three ways and compared on log–log. Navy circles are the elementary evaluation `L_n² − 4π A_n` from the closed forms `L_n = 2n sin(π/n)` and `A_n = (n/2) sin(2π/n)`. Red crosses are the Parseval truncation `4π² Σ m(m−1)|c_m^{(n)}|²` with `|j| ≤ 400`. The gray dashed line is the Archimedean leading term `4π⁴/(3n²)`. All three curves collapse onto each other visually from `n = 3` onward; the lower residual panel shows the elementary-vs-Parseval relative difference sitting on a `~1.55 × 10⁻³` floor that is the `|j| > 400` truncation tail, not a model mismatch.

The Fourier setup is the Hurwitz 1902 identity. For any simple closed curve `γ : [0, L] → ℂ` parametrized by arc length, writing `γ(s) = Σ c_m e^{2πi m s / L}` gives

    L² − 4π A  =  4π² Σ_{m ∈ ℤ}  m(m−1) |c_m|²,

with equality (the circle) iff `c_m = 0` for every `m ∉ {0, 1}`. For the inscribed regular n-gon a geometric-sum computation from `γ'(s) = T_k = ω^k i e^{iπ/n}` on edge k gives a sparse coefficient lattice:

    c_m  =  0                     unless  m ≡ 1 (mod n),
    c_m  =  L_n² / (4π² m²)       for  m = 1 + j·n,  j ∈ ℤ.

The closed form `Δ_n = L_n² · [1 − (π/n) cot(π/n)]` exposes the Archimedean asymptote `Δ_n = 4π⁴/(3n²) + O(1/n⁴)` by Taylor-expanding `cot` at the origin. The Parseval sum hits this rate from the lowest-admissible off-{0,1} mode at `m = 1 + n`.

This is the Dido hinge. The Fourier-side Hurwitz identity reads `π` into the extremum condition of a Parseval quadratic form — the circle maximizes the enclosed area per unit perimeter precisely by being the curve whose Fourier support is `{0, 1}`. The isoperimetric gap `Δ_n` measures, in Fourier-Parseval norm, how far the regular n-gon sits from that extremum. For the program at `memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md`, the figure closes steps 1–2: the identity is not assumed, it is enacted numerically — elementary agrees with Parseval, both hit the Archimedean leading term, the coefficients are explicit.

Three things the figure makes visible without further prose: (i) the `4π⁴/(3n²)` Archimedean rate is hit cleanly from `n = 3` upward — the convergence to the circle is *polynomial*, not exponential, which is the quantitative complexion that makes the approach-to-π a Kraft-budget question rather than a ruler-and-compass question; (ii) the elementary and Parseval computations agree to the `|j| = 400` truncation floor (`~1.55 × 10⁻³` relative), which is a numerical stand-in for the Hurwitz identity itself — the figure is a Parseval closure check, not a curve fit; (iii) the `1/n²` rate is the *same* Archimedean rate visible in `figures/tau_portrait.png` (the `−4π²/n²` large-n asymptote of τ), and at `figures/counting_near_half_gaps.png` (the `π²/(4n²)` floor on the exact-cos-aligned subsequence) — three different circle-side observables agreeing on `1/n²` is the signature that they all read a common Archimedean leading term. For the theorem-level first-band statement and its dyadic-shell corollary behind the frequency plot, see [corners/HURWITZ-FIRST-BAND-CONCENTRATION.md](corners/HURWITZ-FIRST-BAND-CONCENTRATION.md). For the coefficient-side and frequency-band companions, see `figures/hurwitz_gap_coefficients.png` and `figures/hurwitz_gap_frequency_decomposition.png`; for program context, see `memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md` §"Proposed order of work" and [corners/TAU-PORTRAIT.md](corners/TAU-PORTRAIT.md).

For a rotations-side lattice/spectral comparison, see
`rotations/3DT-BRIEF.md` §"Marklof–Strömbergsson: The Geometric Lens."

## Circumscribed counterpart and the Archimedean squeeze

![A two-panel log-log figure spanning polygon order n=3 to n=100. The top panel shows four series collapsing onto a single descending diagonal across roughly six decades vertically: a gray dashed line for the Archimedean leading term 4π⁴/(3n²), navy circles for the inscribed isoperimetric gap, red triangles for the circumscribed gap, and purple plus markers for the Parseval-truncated circumscribed sum. The red triangles sit slightly above the blue circles at small n (visible at n=3, 4, 5) and merge with them at larger n; all four converge to the gray dashed line. The bottom panel shows a magenta curve fluctuating around 10⁻¹³ to 10⁻¹⁵ across the same n range, labeling the relative error between Δ^circ/Δ^insc and sec²(π/n) at floating-point precision.](../figures/hurwitz_gap_archimedean_squeeze.png)

The circumscribed counterpart at `figures/hurwitz_gap_archimedean_squeeze.png` (built by `corners/hurwitz_gap_circumscribed.sage`) closes the optional follow-on of `memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md` step 7. The circumscribed regular `n`-gon (incircle = unit circle) has perimeter `L_n^circ = 2n tan(π/n)` and area `A_n^circ = n tan(π/n)`; the same `1 − (π/n) cot(π/n)` bracket factor that describes the inscribed gap describes the circumscribed gap, with the squared perimeter prefactor adjusted accordingly:

    Δ_n^circ  =  (L_n^circ)² · [1 − (π/n) cot(π/n)].

The ratio of the two gaps is `Δ_n^circ / Δ_n^insc = sec²(π/n) → 1`. Both sides therefore converge to the common Archimedean leading term `4π⁴/(3n²)` at the *same* polynomial rate; the regular `n`-gon sits between an inscribed lower envelope and a circumscribed upper envelope that pinch the circle from both sides — Archimedes' construction, written as a Fourier-Parseval squeeze.

For the Hurwitz Fourier coefficients, the support pattern `m ≡ 1 (mod n)` is identical between inscribed and circumscribed (regular `n`-gons share their rotation-orbit support); the magnitudes scale by

    |c_m^circ|  =  L_n^insc · L_n^circ / (4π² m²)  =  sec(π/n) · |c_m^insc|

so the Parseval norm target lifts from `(L_n^insc/(2π))²` to `(L_n^circ/(2π))²` correctly, and the paired-band terms `B_j(n)` and the first-band concentration constants of [corners/HURWITZ-FIRST-BAND-CONCENTRATION.md](corners/HURWITZ-FIRST-BAND-CONCENTRATION.md) transfer verbatim — every paired-band `B_j` scales by the same `sec²(π/n)` factor as `Δ_n` itself, so `B_1(n)/Δ_n → 6/π²` and the dyadic-shell estimate `Σ_{2^r ≤ j < 2^{r+1}} B_j(n) ≤ 2^{−r} B_1(n)` hold on the circumscribed side without modification.

What this buys for the program. The Archimedean squeeze is now numerically enacted (not just asserted): inscribed and circumscribed gaps agree on rate and sit either side of the leading term, and the `sec²(π/n) → 1` ratio is verified to floating-point. The E-T-K × Aitchison Kraft budget of `memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md` (B) wants the inscribed + circumscribed sum, and that sum is now numerically available. The first-band concentration story is unchanged across the squeeze — the program loses no `6/π²` content by passing from one side to the other or by combining them.
