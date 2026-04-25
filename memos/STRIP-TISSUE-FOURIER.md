# STRIP-TISSUE-FOURIER

The BIND strip has its own Fourier substrate. It is not the Hurwitz
arc-length coefficient lattice, and it should not be folded into that
object. The strip tissue lives on the frequency lattice `n Z`, has
`1/n^2` nonzero modes, and produces theorem-level observables of its own.

This note promotes the strip-Fourier part of
[memos/ARCHIMEDEAN-SIGNATURE.md](memos/ARCHIMEDEAN-SIGNATURE.md) from
"`A_below` is a DC coefficient" to a small toolkit:

- `A_below(n)` is the zeroth mode of the strip tissue.
- The nonzero modes satisfy `d_k = (-1)^k/(k^2 n^2) + O(n^-4)`.
- The nonzero-mode `L^2` energy is a `1/n^4` observable with first-pair
  concentration ratio `90/pi^4`.
- The strip `H^1` seminorm is a `1/n^2` observable with leading constant
  `4pi^4/3`, matching the Hurwitz gap of the radial-graph lift at leading
  order up to an explicit `O(n^-4)` correction.

No Stern-Brocot / Farey / Thomae primitive enters. This is BIND-native strip
geometry: secant arcs, integration, and Fourier modes on `[0, 1]`.

![Three panels under the title "Strip-tissue Fourier object: DC area, signed modes, and first-pair concentration". Top panel (a) "strip tissue y_10(x): area is the DC mode" runs across the full width on a horizontal axis from 0 to 1, showing repeating gray cusped arcs that dip down and back up many times, a dashed orange horizontal reference at the DC level, and a single blue-shaded "one strip period" patch near x=1/2. Bottom-left panel (b) "signed nonzero modes" is a stem chart over integer mode index k from -12 to +12 with three overlaid series (orange dots, green dots, red x-markers) alternating in sign. Bottom-right panel (c) "nonzero L² energy: first pair carries almost all mass" is a green bar chart over mode-pair k from 1 to about 13, descending steeply, with a red limit curve and a callout "90/π⁴ ≈ 0.924".](../figures/strip_tissue_fourier.png)

The figure is built by
[n-gons/build_strip_tissue_fourier.py](n-gons/build_strip_tissue_fourier.py).
It shows the `n = 10` strip tissue, the signed scaled coefficients
`10^2 d_k`, and the first-pair concentration of nonzero `L^2` energy.

---

## Strip Tissue

For each `n >= 3`, define the strip tissue `y_n : [0, 1] -> R` by piecing
together the circumscribed secant arcs:

```text
y_n(x) = sec(2 pi (x - k/n)) - 1
```

on the interval

```text
[(2k - 1)/(2n), (2k + 1)/(2n)] mod 1.
```

The function has period `1/n`, so its Fourier series on `[0, 1]` has
support on `n Z`:

```text
y_n(x) = sum_{k in Z} d_k(n) exp(2 pi i k n x).
```

The coefficients are

```text
d_k(n) = n integral_{-1/(2n)}^{1/(2n)}
             (sec(2 pi x) - 1) exp(-2 pi i k n x) dx.
```

By construction,

```text
d_0(n)
= n integral_{-1/(2n)}^{1/(2n)} (sec(2 pi x) - 1) dx
= (n/pi) log(sec(pi/n) + tan(pi/n)) - 1
= A_below(n).
```

So the BIND area functional is the DC component of the strip tissue.

## Nonzero Modes

For `k != 0`, the constant `-1` term integrates to zero, and with
`t = 2 pi x` symmetry gives

```text
d_k(n) = (n/pi) integral_0^(pi/n) sec(t) cos(k n t) dt.
```

Expanding `sec(t) = 1 + t^2/2 + O(t^4)`, the constant term vanishes because

```text
integral_0^(pi/n) cos(k n t) dt = sin(k pi) / (k n) = 0.
```

The `t^2/2` term contributes `(-1)^k / (k^2 n^2)` (via
`integral_0^(pi/n) t^2 cos(k n t) dt = 2 (pi/n) (-1)^k / (k n)^2`, with the
sine boundary terms vanishing), and higher terms contribute `O(n^-4)` for
fixed `k`, so

```text
d_k(n) = (-1)^k / (k^2 n^2) + O(n^-4)
```

for fixed nonzero `k`.

## Strip `L^2` Energy

Parseval on `[0, 1]` gives

```text
||y_n||_L2^2 = sum_k |d_k(n)|^2.
```

The total `L^2` norm has an exact integral form:

```text
||y_n||_L2^2
= n integral_{-1/(2n)}^{1/(2n)} (sec(2 pi x) - 1)^2 dx
= (n/pi) [tan(pi/n) - 2 log(sec(pi/n) + tan(pi/n)) + pi/n].
```

Hence

```text
||y_n||_L2^2 = pi^4 / (20 n^4) + O(n^-6).
```

The DC energy alone is

```text
|d_0(n)|^2 = A_below(n)^2
           = pi^4 / (36 n^4) + O(n^-6).
```

Therefore the nonzero-mode energy is

```text
sum_{k != 0} |d_k(n)|^2
= pi^4 / (45 n^4) + O(n^-6).
```

The same value follows from the coefficient asymptotic:

```text
sum_{k != 0} |d_k(n)|^2
~ 2 n^-4 sum_{k >= 1} 1/k^4
= 2 zeta(4) / n^4
= pi^4 / (45 n^4).
```

### First-Pair Concentration

The first nonzero pair contributes

```text
|d_1(n)|^2 + |d_-1(n)|^2
= 2 / n^4 + O(n^-6).
```

Thus the asymptotic first-pair concentration is

```text
(|d_1|^2 + |d_-1|^2) / sum_{k != 0} |d_k|^2
-> 1 / zeta(4)
= 90 / pi^4
= 0.9239...
```

This is much tighter than Hurwitz's first-band proportion `6/pi^2`. The
reason is simple: strip nonzero modes decay like `1/k^2`, so their squared
energy decays like `1/k^4`.

### Dyadic Shells

At leading order, the shell `2^r <= k < 2^(r+1)` has mass bounded by

```text
2 * sum_{2^r <= k < 2^(r+1)} 1/(k^4 n^4)
<= 2 * 2^r / (2^(4r) n^4)
= 2 * 2^(-3r) / n^4.
```

So the strip `L^2` shell hierarchy has geometric ratio `1/8` per dyadic
step at leading order. This is the strip analog of the Hurwitz dyadic-shell
estimate, but one level deeper in rate: `1/n^4` rather than `1/n^2`.

Finite-`n` sharp inequalities are not claimed here. The theorem-level
payload is the asymptotic concentration and the exact integral formulas
above.

## Strip `H^1` Seminorm

The derivative is

```text
y_n'(x) = 2 pi sec(2 pi (x - k/n)) tan(2 pi (x - k/n))
```

on each arc. Therefore

```text
||y_n'||_L2^2
= n integral_{-1/(2n)}^{1/(2n)}
      (2 pi)^2 sec^2(2 pi x) tan^2(2 pi x) dx.
```

With `u = 2 pi x`,

```text
||y_n'||_L2^2
= 2 pi n integral_{-pi/n}^{pi/n} sec^2(u) tan^2(u) du
= (4 pi n / 3) tan^3(pi/n).
```

Taylor expansion gives

```text
tan^3(pi/n) = pi^3/n^3 + pi^5/n^5 + (11/15) pi^7/n^7 + O(n^-9),
```

(obtained from `tan(theta) = theta + theta^3/3 + 2 theta^5/15 + O(theta^7)`
cubed), so

```text
||y_n'||_L2^2
= (4 pi n / 3) tan^3(pi/n)
= 4 pi^4 / (3 n^2) + 4 pi^6 / (3 n^4) + O(n^-6).
```

Fourier-side Parseval gives the same object as

```text
||y_n'||_L2^2 = 4 pi^2 n^2 sum_k k^2 |d_k(n)|^2.
```

Using `d_k(n) ~ (-1)^k/(k^2 n^2)`,

```text
4 pi^2 n^2 sum_{k != 0} k^2 |d_k(n)|^2
~ 4 pi^2 n^2 * 2 n^-4 sum_{k >= 1} 1/k^2
= 4 pi^4 / (3 n^2).
```

This leading constant matches Hurwitz's isoperimetric gap:

```text
Delta_n = 4 pi^4 / (3 n^2) + O(n^-4).
```

The observables are not equal. The next terms already differ:

```text
||y_n'||_L2^2 = 4 pi^4/(3n^2) + 4 pi^6/(3n^4) + O(n^-6),
Delta_n       = 4 pi^4/(3n^2) - 16 pi^6/(45n^4) + O(n^-6).
```

The next-order difference is

```text
||y_n'||_L2^2 - Delta_n
= (4/3 + 16/45) pi^6 / n^4 + O(n^-6)
= 76 pi^6 / (45 n^4) + O(n^-6).
```

So the shared constant is a genuine Archimedean match, not an identity in
disguise.

The stronger comparison is now closed in
[memos/STRIP-H1-HURWITZ-CLOSURE.md](memos/STRIP-H1-HURWITZ-CLOSURE.md).
Let

```text
gamma_tilde_n(theta) = (1 + y_n(theta/(2 pi))) e^(i theta).
```

Geometrically, `gamma_tilde_n` is exactly the circumscribed regular
`n`-gon. Its Hurwitz gap satisfies

```text
||y_n'||_L2([0,1])^2 = Delta(gamma_tilde_n) + R_n,
R_n = (16/45) pi^6 / n^4 + (128/315) pi^8 / n^6 + O(n^-8),
R_n > 0.
```

Thus the bridge object is not the inscribed `Delta_n` directly, but the
circumscribed Hurwitz gap of the radial lift. The remaining order-`n^-4`
difference decomposes into the classical circumscribed-vs-inscribed
squeeze plus the explicit residual `R_n`.

![A three-panel figure titled "Hurwitz gap and strip H1 seminorm: same Archimedean jet, different observables". Top panel (a) "same leading rate, different substrates" is a log-log plot with three nearly coincident series — a dashed gray "shared guide", blue dots "Hurwitz gap Δn", and green dots "strip seminorm |y_n'|²" — descending across the plot from n=10 to n=100. Bottom-left panel (b) "second-order match" is a linear plot with two curves converging to a shared horizontal level near 1.0: a blue "Hurwitz approaches from below" and a green "strip H1 approaches from above". Bottom-right panel (c) "not an identity: next term separates them" plots a single red curve flattening into a horizontal limit annotated "76π⁶/45 ≈ 1623.68".](../figures/hurwitz_strip_h1_match.png)

The figure is built by
[memos/build_hurwitz_strip_h1_match.py](memos/build_hurwitz_strip_h1_match.py).
It plots `Delta_n` and `||y_n'||_L2^2` against their shared leading term,
then shows that the next term separates them:
`n^4 (||y_n'||_L2^2 - Delta_n) -> 76 pi^6 / 45`.

## Rate Hierarchy

The strip tissue supports a small Sobolev hierarchy:

```text
sum_k k^(2s) |d_k(n)|^2.
```

Using `d_k ~ 1/(k^2 n^2)`:

- `s = 0`: `L^2` energy, rate `1/n^4`.
- `s = 1`: `H^1` seminorm, rate `1/n^2`.
- `s = 2`: borderline/high-frequency-sensitive; the leading `k^0` tail is
  not summable without using the full finite-`n` coefficients rather than
  the fixed-`k` asymptotic.

A separate non-Sobolev scalar is total variation:

```text
TV(y_n) = 2n (sec(pi/n) - 1) = pi^2/n + O(n^-3).
```

This is a `1/n` observable, not part of the `1/n^2` Archimedean signature,
but it may be useful as a BIND-local roughness measure.

## Program Use

The strip tissue gives BIND a Fourier toolkit independent of Hurwitz:

| Substrate | Function | Frequency lattice | Natural observables |
|---|---|---|---|
| Arc-length polygon | complex curve `gamma_n(s)` | `1 + n Z` | Hurwitz gap `Delta_n ~ 1/n^2` |
| Strip tissue | real function `y_n(x)` | `n Z` | `A_below = d_0`, `||y_n||_L2^2 ~ 1/n^4`, `||y_n'||_L2^2 ~ 1/n^2` |

The key point is not that BIND recreates the inscribed Hurwitz gap. It does
not. The strip has its own native Fourier object on `n Z`; its `H^1`
seminorm reaches the Hurwitz register only after the radial-graph lift
`gamma_tilde_n`, which is the circumscribed regular `n`-gon. The closure
memo
[memos/STRIP-H1-HURWITZ-CLOSURE.md](memos/STRIP-H1-HURWITZ-CLOSURE.md)
settles the former open question affirmatively in this two-step form:

```text
||y_n'||_L2([0,1])^2 = Delta(gamma_tilde_n) + R_n,
R_n = (16/45) pi^6 / n^4 + O(n^-6).
```

So `||y_n'||_L2^2` and the circumscribed Hurwitz gap share the same
isoperimetric Hessian at leading order, with an explicit lower-order
geometric correction. The direct comparison to the inscribed `Delta_n`
remains a secondary Archimedean squeeze, not the primary bilinear-form
identification.
