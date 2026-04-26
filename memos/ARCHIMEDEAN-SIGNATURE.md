# ARCHIMEDEAN-SIGNATURE

> Many circle-side observables vanish at rate `constant / n^2` because the
> regular `n`-gon differs from the circle at second order in the half-angle
> `theta = pi / n`. This Taylor / Hessian statement is the universal
> Archimedean frame. A sharper Fourier / Parseval frame is available for
> some observables, especially Hurwitz's isoperimetric gap, while the strip
> area has its own separate Fourier substrate. The Fourier frame is real,
> but not universal and not single-lattice. One cross-row theorem is now
> known: the strip `H^1` seminorm matches the Hurwitz gap of its
> radial-graph lift up to an explicit `O(n^-4)` correction.

Reusable reference for the circle side's recurring `1/n^2` quantitative
signature.

---

## The Universal Taylor Frame

Set

```text
theta = pi / n.
```

For the observables collected here, the circle limit has the form

```text
F(0) = 0,
F'(0) = 0,
F(theta) = (1/2) F''(0) theta^2 + O(theta^4).
```

Substituting `theta = pi / n` gives

```text
F(pi / n) = c_F / n^2 + O(n^-4),
c_F = (1/2) F''(0) pi^2.
```

This is the universal part: tangency/exhaustion kills the zeroth and first
orders, so the first visible term is quadratic in the half-angle.

## Five Observables

| Observable | `F(theta)` | `F''(0)` | Leading term | Fourier status | Home |
|---|---:|---:|---:|---|---|
| Tail `tau` | `2cos(2theta) - 2` | `-8` | `-4 pi^2 / n^2` | On-support energy | `corners/TAU-PORTRAIT.md` |
| Hurwitz gap `Delta_n` | `4pi^2(sinc^2 theta - sinc(2theta))` | `8pi^2/3` | `4pi^4 / (3n^2)` | Off-support Parseval (first band) | `corners/HURWITZ-GAP.md` |
| Strip area `A_below` | `log(sec theta + tan theta)/theta - 1` | `1/3` | `pi^2 / (6n^2)` | Linear strip mode (DC) | `BNHA/triad/Eraserhead/ARCHIMEDEAN-CONSTRICTION.md` |
| Peak height `h_n` | `sec theta - 1` | `1` | `pi^2 / (2n^2)` | Pointwise / not Fourier | `BNHA/triad/Eraserhead/ARCHIMEDEAN-CONSTRICTION.md` |
| Near-half floor `G_half` | `(sec theta - 1)/2` | `1/2` | `pi^2 / (4n^2)` | Arithmetic selection / not Fourier | `n-gons/counting/NEAR-HALF-GAPS.md` |

Here `sinc(theta) = sin(theta) / theta`. The "Fourier status" column is
explained in [§"Fourier Taxonomy"](#fourier-taxonomy) below. The tail `tau`
row is the large-`n`
regime where `round(2cos(2pi/n)) = 2`, so

```text
tau(n) = 2cos(2pi/n) - 2
```

for the tail. The near-half row is the `n = 3 mod 6` exact-cosine-alignment
subsequence, not the whole near-half-gap function.

![A two-panel scientific plot. Top panel: a lollipop chart of vertical stems rising and falling from a zero baseline across integer values from 3 to 60, with circular markers colored in green, orange, blue, red, purple, gold, and gray bands; green stars sit at the leftmost three positions and arrow callouts label "Niven zeros (crystallographic set)", a "positive bulge", and a "sign flip" near the early integers. Bottom panel: a log-log scatter of colored dots descending along a dashed reference line from upper-left to lower-right, with the same color palette as the top panel.](../figures/tau_portrait.png)

## Derivation Sketches

The constants above come from elementary expansions:

```text
2cos(2theta) - 2 = -4 theta^2 + O(theta^4).
```

```text
4pi^2[(sin(theta)/theta)^2 - sin(2theta)/(2theta)]
= (4pi^2/3) theta^2 + O(theta^4).
```

```text
log(sec theta + tan theta)
= integral_0^theta sec(t) dt
= theta + theta^3/6 + O(theta^5).
```

```text
sec theta - 1 = theta^2/2 + O(theta^4).
```

The near-half floor is half of the peak-height expansion, after the
congruence `n = 3 mod 6` supplies the exact `cos = 1/2` alignment.

## Fourier Taxonomy

The Fourier story is real, but narrower than the Taylor story. It also has
more than one substrate.

The arc-length polygon coefficient lattice from
[corners/HURWITZ-FIRST-BAND-CONCENTRATION.md](corners/HURWITZ-FIRST-BAND-CONCENTRATION.md)
is:

```text
c_m^(n) = 0                                             unless m = 1 + j n,
c_(1 + j n)^(n) = L_n^2 / (4 pi^2 (1 + j n)^2),         j in Z,
L_n = 2 n sin(pi / n).
```

The strip tissue `y_n(x) = sec(2 pi (x - k/n)) - 1` has a different
BIND-native Fourier substrate, living on the lattice `n Z`; the
construction and all `d_k` identities are in
[memos/STRIP-TISSUE-FOURIER.md](memos/STRIP-TISSUE-FOURIER.md).

These two coefficient systems support four distinct outcomes.

### Clean Off-Support Parseval

Hurwitz's isoperimetric gap is the clean case:

```text
Delta_n
= 4 pi^2 sum_{j in Z, j != 0} m(m-1) |c_m^(n)|^2,
  m = 1 + j n.
```

The gap is exactly the off-circle Fourier support. Pairing `m = 1 +- jn`
gives positive band masses `B_j(n)` with

```text
Delta_n = sum_{j >= 1} B_j(n),
B_j(n) <= B_1(n) / j^2,
B_1(n) >= (6 / pi^2) Delta_n.
```

This is the strong Fourier statement: the `1/n^2` rate is read from the
first off-support bands and their `1/j^2` tail.

![A log-log plot whose three series — a black dashed line, a column of blue dots, and a column of red plus markers — overlap so closely that they trace a single straight diagonal descending from the upper left to the lower right across roughly seven decades on the horizontal axis and six decades on the vertical. A narrower inset panel sits below sharing the horizontal axis: a magenta curve rises on linear-y from near zero to a flat asymptote, with a small annotation pointing at the plateau.](../figures/hurwitz_gap_rate.png)

### Clean On-Support Energy

The tail of `tau` has a clean Parseval-energy identity, but it is not an
off-support statement:

```text
tau_tail(n) = 2cos(2pi/n) - 2 = -L_n^2 / n^2.
```

Parseval for the arc-length parametrization gives

```text
sum_m m^2 |c_m^(n)|^2 = L_n^2 / (4 pi^2),
```

so

```text
tau_tail(n)
= -(4 pi^2 / n^2) sum_m m^2 |c_m^(n)|^2.
```

This identity is exact. Its `1/n^2` comes from the external factor
`1/n^2`, while the energy is dominated by the on-support `m = 1` mode.
So `tau` belongs in the Fourier discussion, but not in the same way as the
Hurwitz gap.

### Clean Linear Strip Mode

The strip area is the zeroth Fourier coefficient of the strip tissue:
`d_0 = A_below(n)`, with nonzero modes
`d_k = (-1)^k / (k^2 n^2) + O(n^-4)`. This is a linear DC-mode reading on
the strip lattice `n Z`, not a quadratic Parseval reading on the
arc-length lattice `1 + n Z`. Full derivation in
[memos/STRIP-TISSUE-FOURIER.md](memos/STRIP-TISSUE-FOURIER.md).

![Three panels under the title "Strip-tissue Fourier object: DC area, signed modes, and first-pair concentration". Top panel (a) "strip tissue y_10(x): area is the DC mode" runs across the full width on a horizontal axis from 0 to 1, showing repeating gray cusped arcs that dip down and back up many times, a dashed orange horizontal reference at the DC level, and a single blue-shaded "one strip period" patch near x=1/2. Bottom-left panel (b) "signed nonzero modes" is a stem chart over integer mode index k from -12 to +12 with three overlaid series (orange dots, green dots, red x-markers) alternating in sign. Bottom-right panel (c) "nonzero L² energy: first pair carries almost all mass" is a green bar chart over mode-pair k from 1 to about 13, descending steeply, with a red limit curve and a callout "90/π⁴ ≈ 0.924".](../figures/strip_tissue_fourier.png)

### Pointwise / Arithmetic Selection

The remaining two observables are Taylor-native:

- `h_n` is a pointwise maximum of a strip arc.
- `G_half(n)` is a distance to a rational guide line on an arithmetic
  subsequence.

Each has a valid `1/n^2` Taylor constant. Neither is currently a natural
Fourier functional. A point-evaluation operator could be written against the
strip tissue, but that would be a different, less stable object than either
a DC coefficient or a Parseval norm.

## Cross-Row Theorem

The strip-Hurwitz bridge. Let `y_n` be the strip tissue and define its
radial-graph lift

```text
gamma_tilde_n(theta) = (1 + y_n(theta/(2 pi))) e^(i theta).
```

Then `gamma_tilde_n` is exactly the circumscribed regular `n`-gon, and
[memos/STRIP-H1-HURWITZ-CLOSURE.md](memos/STRIP-H1-HURWITZ-CLOSURE.md)
proves

```text
||y_n'||_L2([0,1])^2 = Delta(gamma_tilde_n) + R_n,
R_n = (16/45) pi^6 / n^4 + (128/315) pi^8 / n^6 + O(n^-8),
R_n > 0.
```

The shared leading constant `4 pi^4 / (3 n^2)` is therefore not merely a
numerical rhyme between rows. It is the common second-variation content of
the isoperimetric functional at the circle, applied through the
circumscribed radial lift. The order-`n^-4` residual is explicit and
geometric; the direct comparison to the inscribed `Delta_n` remains a
secondary Archimedean squeeze.

![A three-panel figure titled "Hurwitz gap and strip H1 seminorm: same Archimedean jet, different observables". Top panel (a) "same leading rate, different substrates" is a log-log plot with three nearly coincident series — a dashed gray "shared guide", blue dots "Hurwitz gap Δn", and green dots "strip seminorm |y_n'|²" — descending across the plot from n=10 to n=100. Bottom-left panel (b) "second-order match" is a linear plot with two curves converging to a shared horizontal level near 1.0: a blue "Hurwitz approaches from below" and a green "strip H1 approaches from above". Bottom-right panel (c) "not an identity: next term separates them" plots a single red curve flattening into a horizontal limit annotated "76π⁶/45 ≈ 1623.68".](../figures/hurwitz_strip_h1_match.png)

## Scope

- Not every `1/n^2` observable is a first-band Fourier observable.
- Not every Fourier reading uses the same coefficient lattice.
- The strip lattice `n Z` and the Hurwitz arclength lattice `1 + n Z`
  are not the same; the cross-row theorem passes through a geometric
  radial lift.
