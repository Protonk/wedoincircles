# The n-gon designated-wholeness construction

## 1. Geometric base

Fix a circle. Inscribe a sequence of regular polygons — triangle, square, pentagon, ... — each tangent to the same circle along one shared edge. That shared edge fixes a common reference point on the circle: the **anchor**, declared to be position 0 at angle 0°.

For each regular n-gon (n ≥ 3), the incircle's tangency points with the polygon's edges are labeled position 0 through position n−1, walking around the circle. Position k of the n-gon sits at angle

$$\theta_{n,k} = (k) \cdot \frac{360°}{n}, \qquad k = 0, 1, \ldots, n-1,$$

with position 0 coinciding with the anchor for every n.

## 2. Designated wholeness

Pick a positive integer **DH** — the *designated wholeness*. The angular unit is 360°/DH. An angle θ is "whole" iff it is an integer multiple of this unit, equivalently iff θ · DH / 360° ∈ ℤ.

The default convention is DH = 360, so the unit is 1°.

## 3. The divisibility test

Position k of the n-gon is whole iff

$$\theta_{n,k} \cdot \frac{\mathrm{DH}}{360°} = \frac{k \cdot \mathrm{DH}}{n} \in \mathbb{Z}.$$

For the **all-positions** test — does every position of the n-gon land on a whole angle? — this reduces to

$$n \mid \mathrm{DH}.$$

Define

$$b_n = \mathbb{1}[\,n \mid \mathrm{DH}\,].$$

## 4. Binary sequence

Sweeping n = 2, 3, 4, ..., n_max produces a binary sequence

$$B(\mathrm{DH}, n_{\max}) = (b_2, b_3, b_4, \ldots, b_{n_{\max}}).$$

This is the **designated-wholeness sequence** at resolution DH over window [2, n_max].

A natural scalar summary is the mean

$$\bar b(\mathrm{DH}, n_{\max}) = \frac{1}{n_{\max} - 1} \sum_{n=2}^{n_{\max}} b_n.$$

## 5. Two ways to address DH

**Positional:** DH ranges over the integers. DH = 36, 37, 38, ..., 360, 361, ..., 3600. Every integer is a valid resolution. The sequence B and the scalar b̄ are defined at every step.

**Logarithmic:** DH = B · 10^E with B = 3.6 and 1 ≤ E ≤ 3. Integer E gives DH ∈ {360, 3600, 36000}, which are lattice points of the positional axis. The factor 3.6 is chosen so that DH retains a factor of 3² (since 3.6 = 2² · 3² / 10), which the 10^E term cannot supply.

The logarithmic axis is a sparse sample of the positional axis, sharing exact values only at integer E.

## Parameters of the construction

- **Anchor convention:** position 0 of every n-gon at 0°.
- **DH:** positive integer (positional) or B · 10^E (logarithmic), B = 3.6.
- **n-range:** [2, n_max] for the binary sequence.
- **Test:** all-positions, reducing to n | DH.

## 6. Degenerate extensions: C and L

The construction naturally extends to n = 1 and n = 2 by the same formula θ_{n,k} = k·360°/n:

- **n = 1 (C, compactification to a point):** the single position is at 0°. The polygon collapses to the anchor.
- **n = 2 (L, line/digon):** two positions at 0° and 180°, antipodal. Not a polygon in the usual sense (zero enclosed area) but the tangency positions are well-defined.

Under the divisibility test, b_1 = 1 trivially for every DH, and b_2 = 1 iff DH is even — which holds for all DH = 360·10^(E−1).

## 7. Position distribution and the Stern-Brocot structure

Collect all positions from all n-gons up to some cap N:

$$P_N = \{\,k \cdot 360° / n : 1 \le n \le N,\ 1 \le k < n\,\}.$$

Mapping angles to [0,1] by dividing by 360°, every element of P_N is a rational k/n ∈ (0,1). Binning this set at a fine angular resolution (e.g., 0.1°) and counting multiplicity produces a histogram whose height at p/q in lowest terms is

$$h_N(p/q) = \lfloor N / q \rfloor,$$

the number of multiples of q in [1, N]. This is the Farey sequence F_N with multiplicity, equivalently a finite-window scaling of **Thomae's (popcorn) function**, which assigns height 1/q at each rational p/q.

The height hierarchy is the Stern-Brocot tree depth function: the deepest spine is at 1/2 (q=2), next tier at 1/3 and 2/3 (q=3), then 1/4 and 3/4 (q=4), and so on. The rational k/n at position k of the n-gon is literally the Farey fraction; sweeping n from 1 upward walks the Stern-Brocot tree level by level.

### Connection to ?(x)

Minkowski's question-mark function ?(x) maps rationals p/q (ranked by Stern-Brocot depth) to dyadic rationals (ranked by binary expansion length). Because the n-gon construction deposits rationals on the circle in exactly the Stern-Brocot order, the position-distribution histogram above is a finite-window discretization of the object ?(x) linearizes.

The divisibility test of §3 picks out which rationals k/n fit the fixed grid of size DH — equivalently, which rationals appear in the dyadic-like lattice defined by the prime support of DH. Under DH = 3.6·10^E, the addressable prime support is {2, 3, 5} with the 3-content permanently capped at exponent 2.

## 8. Relationship between the two axes

The integer-E samples f_E(E) = b̄(3.6·10^E, n_max) are a sparse subset of the positional samples f_M(M) = b̄(M, n_max). The sampling is geometric on the M-axis: successive integer E values sample M at ratio 10.

The two axes coincide as divisor-structure probes only in the regime DH ≲ 360, where the highly composite numbers governing the upper envelope of f_M are {2,3,5}-smooth. Once M grows past 360, the HCN ladder begins picking up primes outside {2,3,5} (7 enters at M=2520, 11 at 27720, 13 at 360360), and the logarithmic axis becomes constitutionally blind to those events — no E produces a DH divisible by 7, 11, or 13.

## Open directions

Left deliberately unresolved:

- Whether the construction's natural scalar invariant should be b̄ over all n (dominated by non-divisors), b̄ over {2,3,5}-smooth n (bounded away from 1), or some divisor-density per [2,N] (erratic but with HCN envelope).
- Non-integer E: no canonical extension. Three candidate readings (strict divisibility, floor, soft distance) disagree categorically.
- Running-mean behavior: for fixed DH, m(n) = D(n)/n where D(n) counts divisors of DH up to n. Universal shape is τ(DH)/log(DH) · log(n)/n for n ≤ DH, crossing over to τ(DH)/n for n ≥ DH.
