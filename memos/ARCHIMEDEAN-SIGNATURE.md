# ARCHIMEDEAN-SIGNATURE

Reusable reference for the circle side's recurring `1/n^2` quantitative
signature.

The short version:

> Many circle-side observables vanish at rate `constant / n^2` because the
> regular `n`-gon differs from the circle at second order in the half-angle
> `theta = pi / n`. This Taylor / Hessian statement is the universal
> Archimedean frame. A sharper Fourier / Parseval frame is available for
> some observables, especially Hurwitz's isoperimetric gap, while the strip
> area has its own separate Fourier substrate. The Fourier frame is real,
> but not universal and not single-lattice.

This memo consolidates the scattered `1/n^2` appearances in:

- [corners/TAU-PORTRAIT.md](corners/TAU-PORTRAIT.md)
- [corners/HURWITZ-GAP.md](corners/HURWITZ-GAP.md)
- [corners/HURWITZ-FIRST-BAND-CONCENTRATION.md](corners/HURWITZ-FIRST-BAND-CONCENTRATION.md)
- [BNHA/triad/Eraserhead/ARCHIMEDEAN-CONSTRICTION.md](BNHA/triad/Eraserhead/ARCHIMEDEAN-CONSTRICTION.md)
- [n-gons/counting/NEAR-HALF-GAPS.md](n-gons/counting/NEAR-HALF-GAPS.md)
- [memos/ARCHIMEDEAN-DUAL-LANGUAGE-AUDIT.md](memos/ARCHIMEDEAN-DUAL-LANGUAGE-AUDIT.md)
- [memos/STRIP-TISSUE-FOURIER.md](memos/STRIP-TISSUE-FOURIER.md)

It is intentionally narrower than a compute-cost lower bound. If
[memos/COUNTING-APPARATUS.md](memos/COUNTING-APPARATUS.md) never hardens
into a primitive-operation floor, the Archimedean signature remains the
circle side's quantitative companion to the qualitative closure mismatch.

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

| Observable | Function of `theta` | `F''(0)` | Leading term | Home |
|---|---:|---:|---:|---|
| Tail `tau` | `2cos(2theta) - 2` | `-8` | `-4 pi^2 / n^2` | `corners/TAU-PORTRAIT.md` |
| Hurwitz gap `Delta_n` | `4pi^2(sinc^2 theta - sinc(2theta))` | `8pi^2/3` | `4pi^4 / (3n^2)` | `corners/HURWITZ-GAP.md` |
| Strip area `A_below` | `log(sec theta + tan theta)/theta - 1` | `1/3` | `pi^2 / (6n^2)` | `BNHA/triad/Eraserhead/ARCHIMEDEAN-CONSTRICTION.md` |
| Peak height `h_n` | `sec theta - 1` | `1` | `pi^2 / (2n^2)` | `BNHA/triad/Eraserhead/ARCHIMEDEAN-CONSTRICTION.md` |
| Near-half floor `G_half` | `(sec theta - 1)/2` | `1/2` | `pi^2 / (4n^2)` | `n-gons/counting/NEAR-HALF-GAPS.md` |

Here `sinc(theta) = sin(theta) / theta`. The tail `tau` row is the large-`n`
regime where `round(2cos(2pi/n)) = 2`, so

```text
tau(n) = 2cos(2pi/n) - 2
```

for the tail. The near-half row is the `n = 3 mod 6` exact-cosine-alignment
subsequence, not the whole near-half-gap function.

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

The strip tissue has a different BIND-native Fourier substrate. Define

```text
y_n(x) = sec(2 pi (x - k/n)) - 1
         for x in [(2k-1)/(2n), (2k+1)/(2n)] mod 1.
```

Then `y_n` has period `1/n`, so its Fourier series on `[0, 1]` lives on
`n Z`:

```text
y_n(x) = sum_{k in Z} d_k exp(2 pi i k n x),
d_k = n integral_{-1/(2n)}^{1/(2n)}
          (sec(2 pi x) - 1) exp(-2 pi i k n x) dx.
```

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

```text
d_0
= n integral_{-1/(2n)}^{1/(2n)} (sec(2 pi x) - 1) dx
= A_below(n).
```

For `k != 0`, the constant term integrates to zero and symmetry gives

```text
d_k = (n / pi) integral_0^(pi/n) sec(t) cos(k n t) dt.
```

After the constant term vanishes, `sec(t) - 1 = t^2/2 + O(t^4)` yields

```text
d_k = (-1)^k / (k^2 n^2) + O(n^-4).
```

So `A_below` has an honest Fourier reading, but it is a linear DC-mode
reading on the strip lattice `n Z`, not a quadratic Parseval reading on the
arc-length lattice `1 + n Z`.

### Pointwise / Arithmetic Selection

The remaining two observables are Taylor-native:

- `h_n` is a pointwise maximum of a strip arc.
- `G_half(n)` is a distance to a rational guide line on an arithmetic
  subsequence.

Each has a valid `1/n^2` Taylor constant. Neither is currently a natural
Fourier functional. A point-evaluation operator could be written against the
strip tissue, but that would be a different, less stable object than either
a DC coefficient or a Parseval norm.

## Classification Table

| Observable | Taylor status | Fourier status | Boundary statement |
|---|---|---|---|
| Tail `tau` | Clean second jet | Clean on-support energy | Exact Parseval identity, but not first-band departure |
| `Delta_n` | Clean second jet | Clean off-support Parseval | The genuine first-band Fourier observable |
| `A_below` | Clean second jet | Clean linear strip mode | Exact DC coefficient of strip tissue on `n Z` |
| `h_n` | Clean second jet | Pointwise / not Fourier | Pointwise strip maximum |
| `G_half` | Clean second jet plus congruence | Arithmetic selection / not Fourier | Rational-guide distance selected by arithmetic subsequence |

## Program Use

This memo gives the circle side a stable quantitative sentence:

> Across several independent observables, regular `n`-gon exhaustion of the
> circle first appears at order `1/n^2`; this is the Archimedean signature.

For the closure-mismatch program, this is a companion metric, not the
load-bearing no-go mechanism. The no-go mechanism is still closure depth:
circle-side `phi(n)/2` grows through Chebyshev/cyclotomic closure, while the
log side's native `Aff^+(R)` closure is flat.

For the Kraft/Hermite-Lindemann side, the Hurwitz row is the important one:
the Fourier support condition and first-band concentration are theorem-level
inputs to [memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md](memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md).

For BIND, the `A_below` row now supplies a real strip-Fourier substrate:
linear modes `d_k` on `n Z`, with the area as `d_0`. The same substrate also
gives `||y_n||_L2^2 ~ pi^4/(20n^4)` and
`||y_n'||_L2^2 ~ 4pi^4/(3n^2)`; see
[memos/STRIP-TISSUE-FOURIER.md](memos/STRIP-TISSUE-FOURIER.md). For the
counting side, the near-half row remains diagnostic: it shows the same
second-order Archimedean rate after an arithmetic subsequence is selected,
without pretending to be Fourier-Parseval.

## What This Does Not Claim

- It does not claim every `1/n^2` observable is a first-band Fourier
  observable.
- It does not claim every Fourier reading uses the same coefficient lattice.
- It does not claim the counting word `M_N` is a compute-cost lower-bound
  ledger.
- It does not claim `A_below`, peak height, or near-half gaps are the right
  final observables for the F theorem.
- It does not replace the need to define the category-theoretic meaning of
  "native F."

The useful claim is narrower and defensible: Taylor is the universal
language of the Archimedean signature; Fourier is stronger where the
observable has a native coefficient system, but the coefficient system and
functional type must be named each time.
