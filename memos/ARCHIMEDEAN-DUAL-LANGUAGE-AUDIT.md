# ARCHIMEDEAN-DUAL-LANGUAGE-AUDIT

Audit note for the proposed `ARCHIMEDEAN-SIGNATURE.md` synthesis.

Question: which circle-side `1/n^2` observables admit both a Taylor
second-jet derivation and a clean Fourier / Parseval derivation from the
regular polygon coefficients, and which only have the Taylor derivation?

Conclusion up front:

- The Taylor / Hessian view covers all five observables below.
- The Fourier / Parseval view is clean for Hurwitz's isoperimetric gap.
- `tau` has a clean Parseval-energy reading, but it is on-support and uses
  an external `1/n^2` factor; it is not a first-off-support departure
  statement.
- `A_below` has an honest strip-Fourier reading, but as the zeroth mode of a
  separate strip-tissue lattice, not as a Parseval band-sum on the polygon
  coefficient lattice.
- Peak-height and near-half-gap observables are still Taylor-native:
  pointwise maxima and distances to rational guide lines are not natural
  Parseval functionals of the polygon coefficient lattice.

This note is deliberately narrow. It covers five observables and records the
boundary honestly, so a later synthesis does not overstate the Fourier side.

---

## Common setup

Let

```text
theta = pi / n.
```

The Taylor test is:

```text
F(theta) = F(0) + F'(0) theta + (1/2) F''(0) theta^2 + O(theta^4).
```

For all five observables here, `F(0) = F'(0) = 0`, so

```text
F(pi / n) = c_F / n^2 + O(n^-4),
where c_F = (1/2) F''(0) pi^2.
```

The Fourier object used for comparison is the arc-length coefficient lattice
from [corners/HURWITZ-FIRST-BAND-CONCENTRATION.md](corners/HURWITZ-FIRST-BAND-CONCENTRATION.md):

```text
c_m^(n) = 0                                              unless m = 1 + j n,
c_(1 + j n)^(n) = L_n^2 / (4 pi^2 (1 + j n)^2),          j in Z,
L_n = 2 n sin(pi / n).
```

Four Fourier outcomes are distinguished:

- **Clean off-support Parseval:** the observable is literally a Parseval-type
  sum over the off-circle bands `m = 1 +- j n`, with nonzero weight at
  `j = 1`.
- **Clean on-support energy:** the observable is expressible through the
  Parseval energy of the whole polygon, dominated by the `m = 1` mode, with
  the `1/n^2` scaling supplied externally.
- **Clean linear strip mode:** the observable is a Fourier coefficient of a
  different, BIND-native strip function. The reading is linear, not
  Parseval-quadratic, and it lives on a different lattice.
- **Stretched / fake:** there is no natural Parseval functional of
  `c_m^(n)` currently on the page. One could Fourier-expand some local
  kernel, but that would change the object being audited.

---

## 1. Tail-normalized tau

For the large-`n` tail, where `round(2cos(2pi/n)) = 2`, use

```text
tau_tail(n) = 2 cos(2pi/n) - 2.
```

### Taylor derivation

Set

```text
F(theta) = 2 cos(2 theta) - 2.
```

Then

```text
F'(theta)  = -4 sin(2 theta),
F''(theta) = -8 cos(2 theta),
F''(0)     = -8.
```

So

```text
tau_tail(n) = -4 pi^2 / n^2 + O(n^-4).
```

### Fourier attempt

This has a clean Parseval-energy reading, but not an off-support one.

Since

```text
L_n = 2 n sin(theta),
tau_tail(n) = -4 sin^2(theta) = -L_n^2 / n^2,
```

and the arc-length Parseval energy gives

```text
sum_m m^2 |c_m^(n)|^2 = L_n^2 / (4 pi^2),
```

we get the exact identity

```text
tau_tail(n)
= -(4 pi^2 / n^2) sum_m m^2 |c_m^(n)|^2.
```

The leading term comes from the fact that the energy tends to `1`, with the
`m = 1` mode dominant. The off-support bands only correct this energy at
lower order.

### Boundary statement

`tau` is clean in Fourier language only as an on-support energy identity.
It should not be advertised as a first-band departure from circle support.

---

## 2. Hurwitz isoperimetric gap

For the inscribed regular `n`-gon,

```text
Delta_n = L_n^2 - 4 pi A_n,
L_n = 2 n sin(pi/n),
A_n = (n/2) sin(2pi/n).
```

### Taylor derivation

With `theta = pi/n`,

```text
F(theta)
= 4 pi^2 [ (sin(theta) / theta)^2 - sin(2theta) / (2theta) ].
```

Using

```text
(sin(theta) / theta)^2 = 1 - theta^2/3 + O(theta^4),
sin(2theta) / (2theta) = 1 - 2 theta^2/3 + O(theta^4),
```

we get

```text
F(theta) = (4 pi^2 / 3) theta^2 + O(theta^4),
F''(0)   = 8 pi^2 / 3.
```

So

```text
Delta_n = 4 pi^4 / (3 n^2) + O(n^-4).
```

### Fourier attempt

This is the clean off-support Parseval case.

Hurwitz's identity gives

```text
Delta_n
= 4 pi^2 sum_{j in Z, j != 0} m(m-1) |c_m^(n)|^2,
  m = 1 + j n.
```

Pairing `m = 1 +- j n`, [corners/HURWITZ-FIRST-BAND-CONCENTRATION.md](corners/HURWITZ-FIRST-BAND-CONCENTRATION.md)
defines positive band masses `B_j(n)` with

```text
Delta_n = sum_{j >= 1} B_j(n),
B_j(n) = (L_n^4 / (2 pi^2))
         [j^2 n^2 (j^2 n^2 + 3)] / (j^2 n^2 - 1)^3.
```

As `n -> infinity`,

```text
B_j(n) ~ 8 pi^2 / (j^2 n^2).
```

Summing over `j >= 1` gives

```text
Delta_n ~ (8 pi^2 / n^2) zeta(2)
        = 4 pi^4 / (3 n^2).
```

The first band carries a sharp uniform proportion:

```text
B_1(n) >= (6 / pi^2) Delta_n,
B_1(n) / Delta_n -> 6 / pi^2.
```

### Boundary statement

`Delta_n` is the genuine first/off-support Fourier observable in this list.
Its Taylor constant and Fourier constant are the same statement in two
languages.

---

## 3. Strip area below the circumscribed arcs

The BIND strip area is

```text
A_below(n)
= (n / pi) log(sec(pi/n) + tan(pi/n)) - 1.
```

### Taylor derivation

Set

```text
F(theta) = log(sec(theta) + tan(theta)) / theta - 1.
```

Since

```text
log(sec(theta) + tan(theta)) = integral_0^theta sec(t) dt
                             = theta + theta^3/6 + O(theta^5),
```

we have

```text
F(theta) = theta^2 / 6 + O(theta^4),
F''(0)   = 1/3.
```

So

```text
A_below(n) = pi^2 / (6 n^2) + O(n^-4).
```

### Fourier attempt

This is a clean linear Fourier reading on a different substrate.

Define the strip tissue `y_n : [0, 1] -> R` by piecing together the
circumscribed secant arcs:

```text
y_n(x) = sec(2 pi (x - k/n)) - 1
         for x in [(2k-1)/(2n), (2k+1)/(2n)] mod 1.
```

This function has period `1/n`, so its Fourier series on `[0, 1]` lives on
the frequency lattice `n Z`:

```text
y_n(x) = sum_{k in Z} d_k exp(2 pi i k n x).
```

With one-period normalization,

```text
d_k = n integral_{-1/(2n)}^{1/(2n)}
          (sec(2 pi x) - 1) exp(-2 pi i k n x) dx.
```

The zeroth coefficient is exactly the strip area:

```text
d_0 = n integral_{-1/(2n)}^{1/(2n)} (sec(2 pi x) - 1) dx
    = A_below(n).
```

For `k != 0`, the constant `-1` term integrates to zero and symmetry gives

```text
d_k = (n / pi) integral_0^(pi/n) sec(t) cos(k n t) dt.
```

Equivalently, using `sec(t) - 1 = t^2/2 + O(t^4)` after the constant term
vanishes,

```text
d_k = (-1)^k / (k^2 n^2) + O(n^-4).
```

So the strip tissue has real nonzero-mode band structure on `n Z`, with
`1/n^2` leading modes. `A_below` itself reads only the DC component.

This is not the Hurwitz coefficient lattice `c_m^(n)`, and it is not a
quadratic Parseval reading. It is an honest BIND-native Fourier object with
a linear `d_0` observable.

### Boundary statement

`A_below` is Taylor-native and also Fourier-native as a strip-tissue DC
mode. Its Fourier substrate is separate from Hurwitz's arc-length
coefficient lattice.

---

## 4. Peak height

The peak height of a circumscribed strip arc is

```text
h_n = sec(pi/n) - 1.
```

### Taylor derivation

Set

```text
F(theta) = sec(theta) - 1.
```

Since

```text
sec(theta) = 1 + theta^2/2 + O(theta^4),
```

we get

```text
F''(0) = 1,
h_n    = pi^2 / (2 n^2) + O(n^-4).
```

### Fourier attempt

This is stretched.

Peak height is a pointwise maximum of the strip arc. Point evaluation is not
a stable Parseval norm, and the observable is attached to the circumscribed
strip geometry rather than to the inscribed polygon's arc-length coefficient
lattice. A Fourier series of the local arc could encode the point value, but
that would be an evaluation functional on a different object, not the
first-band Parseval mechanism.

### Boundary statement

Peak height is Taylor-native and pointwise. Do not treat it as a Fourier
observable unless a new, explicit Fourier object for the strip arcs is
introduced.

---

## 5. Near-half-gap floor on `n = 3 mod 6`

On the arithmetic subsequence `n = 3 mod 6`, the `+1/2` guide has exact
cosine alignment. The gap floor is

```text
G_half(n) = (sec(pi/n) - 1) / 2.
```

This is not the whole near-half-gap function; it is the special-subsequence
floor visible in [n-gons/counting/NEAR-HALF-GAPS.md](n-gons/counting/NEAR-HALF-GAPS.md).

### Taylor derivation

Set

```text
F(theta) = (sec(theta) - 1) / 2.
```

Then

```text
F(theta) = theta^2 / 4 + O(theta^4),
F''(0)   = 1/2.
```

So on `n = 3 mod 6`,

```text
G_half(n) = pi^2 / (4 n^2) + O(n^-4).
```

### Fourier attempt

This is stretched.

The observable is a distance to a rational guide line, and the `1/n^2`
floor appears only after an arithmetic congruence selects the exact-cosine
alignment subsequence. That is a pointwise arithmetic event, not a global
Parseval functional of the polygon coefficient lattice.

### Boundary statement

The near-half floor is Taylor plus arithmetic selection. Its Fourier reading
would currently be fake.

---

## Summary table

| Observable | `F(theta)` | `F''(0)` | Leading term | Fourier outcome | Honest Fourier reading |
|---|---:|---:|---:|---|---|
| `tau_tail` | `2cos(2theta)-2` | `-8` | `-4 pi^2/n^2` | Clean on-support energy | Exact `-(4pi^2/n^2) sum m^2 abs(c_m)^2`; rate from external `n^-2` and `m=1` energy |
| `Delta_n` | `4pi^2(sinc^2 theta - sinc(2theta))` | `8pi^2/3` | `4pi^4/(3n^2)` | Clean off-support Parseval | Exact Hurwitz sum over `m=1+jn`; first band carries sharp `6/pi^2` proportion |
| `A_below` | `log(sec theta + tan theta)/theta - 1` | `1/3` | `pi^2/(6n^2)` | Clean linear strip mode | Exact DC coefficient `d_0` of strip tissue on frequency lattice `n Z`; nonzero modes satisfy `d_k = (-1)^k/(k^2 n^2) + O(n^-4)` |
| `h_n` | `sec theta - 1` | `1` | `pi^2/(2n^2)` | Stretched / fake | Pointwise maximum of strip arc |
| `G_half` | `(sec theta - 1)/2` | `1/2` | `pi^2/(4n^2)` | Stretched / fake | Rational-guide distance on `n = 3 mod 6` subsequence |

Here `sinc(theta) = sin(theta) / theta`.

---

## Numerical sanity check at `n = 10`

These values compare each observable with its Taylor leading term. For the
near-half entry, `n = 10` is not in the `n = 3 mod 6` subsequence; the row
therefore checks only the analytic floor expression `(sec(pi/n)-1)/2`, not
an actual best-approach event.

| Observable | Actual at `n=10` | Leading term | Actual / leading | Fourier check |
|---|---:|---:|---:|---|
| `tau_tail` | `-0.381966011250` | `-0.394784176044` | `0.967531209` | Exact energy identity gives `-0.381966011250` |
| `Delta_n` | `1.264964515201` | `1.298787880453` | `0.973957745` | `B_1/Delta = 0.620258888`; limit `6/pi^2 = 0.607927102` |
| `A_below` | `0.016867222158` | `0.016449340668` | `1.025404148` | Exact strip DC coefficient `d_0` |
| `h_n` | `0.051462224238` | `0.049348022005` | `1.042842695` | No clean Fourier check |
| `G_half` expression | `0.025731112119` | `0.024674011003` | `1.042842695` | No clean Fourier check |

The agreement is at the expected `O(n^-4)` level for `n = 10`; the signs of
the errors differ because the fourth-order Taylor coefficients differ.

---

## Honest claim for `ARCHIMEDEAN-SIGNATURE.md`

The safe synthesis is:

> The `1/n^2` Archimedean signature is universally visible as a second-jet
> phenomenon in `theta = pi/n`. For Parseval-type observables, especially
> Hurwitz's isoperimetric gap, the same signature has a stronger Fourier
> reading through the polygon's coefficient lattice and the first
> off-support bands. `tau` has a related but weaker on-support energy
> reading. `A_below` has a separate linear Fourier reading as the DC mode of
> the strip tissue. Peak-height and near-half-gap observables remain
> pointwise / arithmetic-selection observables rather than Fourier
> functionals.

That is enough for the program-level claim that `1/n^2` is the circle side's
quantitative fingerprint. It is not enough to say every `1/n^2` observable
is a first-band Fourier observable, or even that every Fourier reading lives
on the same coefficient lattice.
