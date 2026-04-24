# STRIP-H1-HURWITZ-CLOSURE

Result memo closing the open question at the end of
[memos/STRIP-TISSUE-FOURIER.md](memos/STRIP-TISSUE-FOURIER.md): whether
`||y_n'||_L2^2` and `Delta_n` share more than a second-order Archimedean
jet. The honest pairing goes through the radial-graph lift `gamma_tilde_n`,
and the answer is positive closure with an explicit `O(n^-4)` remainder.

---

## Verdict up front

**Positive closure.** With

```text
gamma_tilde_n(theta) = (1 + y_n(theta/(2 pi))) e^{i theta},
Delta(gamma_tilde_n) = L(gamma_tilde_n)^2 - 4 pi A(gamma_tilde_n),
R_n                  = ||y_n'||_L2([0,1])^2 - Delta(gamma_tilde_n),
```

the remainder `R_n` starts at `1/n^4`, not at `1/n^2`:

```text
R_n = (16 / 45) pi^6 / n^4  +  (128 / 315) pi^8 / n^6  +  O(n^-8),
R_n > 0 for every n >= 3.
```

The shared leading constant `4 pi^4 / (3 n^2)` is therefore a genuine
Hurwitz-form identification — the strip `H^1` seminorm is the Hurwitz gap
of the lift up to an explicit lower-order correction — not a
second-order Archimedean-jet coincidence. `ARCHIMEDEAN-SIGNATURE.md`
gets a cross-row theorem.

The computation is done symbolically in Sage and verified numerically at
200-bit precision; script at
[memos/strip_h1_hurwitz_closure.sage](memos/strip_h1_hurwitz_closure.sage).

---

## Normalization

Work on a single period. All `L^2` norms below use the measure stated.

- `y_n : [0, 1] -> R` with period `1/n`, as in
  [memos/STRIP-TISSUE-FOURIER.md](memos/STRIP-TISSUE-FOURIER.md). On the
  `k`-th arc, `y_n(x) = sec(2 pi (x - k/n)) - 1` for
  `x in [(2k-1)/(2n), (2k+1)/(2n)]`.
- `gamma_tilde_n : [0, 2 pi] -> R^2`, the radial-graph lift,
  `gamma_tilde_n(theta) = (1 + y_n(theta/(2 pi))) e^{i theta}`. Parametrized
  by angle `theta = 2 pi x`, not by arclength.
- `||y_n'||_L2([0,1])^2 = int_0^1 (dy_n/dx)^2 dx`. Measure `dx`, interval
  `[0, 1]`.
- `L(gamma_tilde_n) = int_0^{2 pi} sqrt(r^2 + (dr/dtheta)^2) dtheta` and
  `A(gamma_tilde_n) = (1/2) int_0^{2 pi} r(theta)^2 dtheta` with
  `r(theta) = 1 + y_n(theta/(2 pi))`. Measure `dtheta`, interval
  `[0, 2 pi]`. Area formula is polar, valid because `r > 0` and the curve
  is a simple radial graph.

---

## Geometric identification of `gamma_tilde_n`

On arc `k` of the strip tissue, in angular coordinate `phi = theta - 2 pi k / n`:

```text
r(theta) = 1 + y_n(theta/(2 pi)) = 1 + (sec(phi) - 1) = sec(phi).
```

The tangent line to the unit circle at the point `(cos(2 pi k / n), sin(2 pi k / n))`
has polar equation `r cos(theta - 2 pi k / n) = 1`, i.e.
`r = sec(theta - 2 pi k / n)` on the arc where this is positive. So on the
interval `phi in [-pi/n, pi/n]`, `gamma_tilde_n` traces the tangent line at
angle `2 pi k / n`. Corners occur at the seams `phi = +- pi/n`, where two
tangent lines meet.

> **`gamma_tilde_n` is the circumscribed regular `n`-gon.**

This is the key geometric fact. The radial-graph lift of the strip tissue
is not a new curve; it is the circumscribed polygon in polar form. That
makes `Delta(gamma_tilde_n)` a Hurwitz gap of a classically-named object,
not an ad hoc invariant.

---

## Exact closed forms

On each arc, `r^2 + (dr/dtheta)^2 = sec^2(phi) + sec^2(phi) tan^2(phi) = sec^4(phi)`,
so the arclength element is `ds = sec^2(phi) dphi`. Integrating over `n`
arcs:

```text
L(gamma_tilde_n) = n int_{-pi/n}^{pi/n} sec^2(phi) dphi = 2 n tan(pi/n).
```

For the area, `int_{-pi/n}^{pi/n} sec^2(phi) dphi = 2 tan(pi/n)`, so

```text
A(gamma_tilde_n) = (1/2) * n * 2 tan(pi/n) = n tan(pi/n).
```

(Both match the classical circumscribed-regular-`n`-gon formulas.) Hence

```text
Delta(gamma_tilde_n) = (2 n tan(pi/n))^2 - 4 pi (n tan(pi/n))
                    = 4 n^2 tan^2(pi/n) - 4 pi n tan(pi/n)
                    = 4 n tan(pi/n) * (n tan(pi/n) - pi).
```

From [memos/STRIP-TISSUE-FOURIER.md](memos/STRIP-TISSUE-FOURIER.md):

```text
||y_n'||_L2([0,1])^2 = (4 pi n / 3) tan^3(pi/n).
```

Therefore, as a closed form,

```text
R_n = ||y_n'||_L2^2 - Delta(gamma_tilde_n)
    = (4 pi n / 3) tan^3(pi/n) - 4 n^2 tan^2(pi/n) + 4 pi n tan(pi/n)
    = 4 n tan(pi/n) * [ (pi / 3) tan^2(pi/n) - n tan(pi/n) + pi ].
```

Setting `u = pi / n` and using `n = pi / u`:

```text
R_n = (4 pi^2 / u) * tan(u) * [ (1/3) tan^2(u) - tan(u) / u + 1 ].
```

---

## Taylor expansion (symbolic, Sage)

Using `tan(u) = u + u^3/3 + 2 u^5/15 + 17 u^7/315 + O(u^9)`:

```text
(1/3) tan^2(u) - tan(u)/u + 1 = (4 / 45) u^4 + (68 / 945) u^6 + O(u^8),
(4 pi^2 / u) tan(u)            = 4 pi^2 (1 + u^2/3 + 2 u^4/15 + 17 u^6/315 + ...).
```

Multiplying and collecting at order `u^4` and `u^6`:

```text
R_n = (16 / 45) pi^2 u^4 + (128 / 315) pi^2 u^6 + O(u^8).
```

Substituting `u = pi / n`:

```text
R_n = (16 / 45) pi^6 / n^4  +  (128 / 315) pi^8 / n^6  +  O(n^-8).
```

Sage verifies both coefficients exactly (Part A of the script).

For reference, the series of the two observables individually:

```text
||y_n'||_L2^2      = 4 pi^4 / (3 n^2)  +  (60/45) pi^6 / n^4  +  (44/45) pi^8 / n^6  +  O(n^-8),
Delta(gamma_tilde_n) = 4 pi^4 / (3 n^2)  +  (44/45) pi^6 / n^4  +  ( 4/ 7) pi^8 / n^6  +  O(n^-8).
```

(`60/45 = 4/3`; writing in `/45` makes the 1/n^4 budget transparent.)

The inscribed gap, recalled for comparison:

```text
Delta_n = 4 pi^4 / (3 n^2)  -  (16/45) pi^6 / n^4  +  O(n^-6).
```

---

## Three-way `1/n^4` budget

At order `1/n^4`, three pairwise differences combine cleanly:

```text
||y_n'||^2 - Delta_n           (total gap)             =  76 pi^6 / (45 n^4) + O(n^-6),
Delta(gamma_tilde_n) - Delta_n (circumscribed - insc.) =  60 pi^6 / (45 n^4) + O(n^-6),
||y_n'||^2 - Delta(gamma_tilde_n) (strip - circ.)      =  16 pi^6 / (45 n^4) + O(n^-6).
```

The total gap decomposes exactly as `60 + 16 = 76`: the circumscribed lift
accounts for `60/76` of the `1/n^4` gap, leaving the residual `16/76`
that is the true bilinear-form correction `R_n`. The numerical table from
Part B of the script, at `n = 100000`:

```text
n^4 * (||y_n'||^2 - Delta_n)          = 1.62368e+3   vs. 76 pi^6 / 45 = 1.62368e+3
n^4 * (Delta(gamma_tilde_n) - Delta_n) = 1.28185e+3  vs. 60 pi^6 / 45 = 1.28185e+3
n^4 * (||y_n'||^2 - Delta(gamma_tilde_n)) = 3.41827e+2 vs. 16 pi^6 / 45 = 3.41827e+2
```

Sum `60 + 16 = 76` verified to 25+ digits.

---

## Numerical verification

Run `sage memos/strip_h1_hurwitz_closure.sage` to reproduce. Extract:

```text
n        n^4 * R_n                        deviation from 16 pi^6 / 45
 10      3.8357e+2                        4.17e+1
100      3.4221e+2                        3.86e-1
1000     3.4183e+2                        3.86e-3
10000    3.4183e+2                        3.86e-5
100000   3.4183e+2                        3.86e-7
```

The deviation shrinks as `1/n^2` (the next-order `128 pi^8 / 315` term),
as predicted.

Extracting `n^6 * (R_n - 16 pi^6 / (45 n^4))` gives `128 pi^8 / 315` to
15 digits by `n = 100000`, confirming the `1/n^6` coefficient.

`R_n > 0` is confirmed at `n = 3, 4, 5, 6, 7, 10, 100` directly from the
closed-form value.

---

## Geometric attribution of `R_n`

Quadratic expansion of the isoperimetric functional at the circle. For
`r(theta) = 1 + phi(theta)` with `phi` small:

```text
L(r)^2 - 4 pi A(r) = (int phi dtheta)^2  +  2 pi int (phi')^2 dtheta  -  2 pi int phi^2 dtheta
                   +  (cubic and higher in phi).
```

For `phi(theta) = y_n(theta / (2 pi))`:

```text
int phi dtheta          = 2 pi A_below(n)    (A_below = pi^2/(6 n^2) + O(n^-4)),
2 pi int phi^2 dtheta   = 4 pi^2 ||y_n||_L2([0,1])^2   ~  pi^6 / (5 n^4),
2 pi int (phi')^2 dtheta = ||y_n'||_L2([0,1])^2.
```

So the pure Hessian approximation to `Delta(gamma_tilde_n)` is

```text
H[y_n] = 4 pi^2 A_below(n)^2  +  ||y_n'||_L2^2  -  4 pi^2 ||y_n||_L2^2,
```

and rearranging,

```text
||y_n'||_L2^2 - H[y_n] = 4 pi^2 ||y_n||_L2^2 - 4 pi^2 A_below(n)^2
                      = pi^6 / (5 n^4) - pi^6 / (9 n^4) + O(n^-6)
                      = (4 / 45) pi^6 / n^4 + O(n^-6).
```

So the Hessian part of `R_n` is `4/45`, leaving

```text
R_n - (||y_n'||^2 - H[y_n]) = (16/45 - 4/45) pi^6 / n^4 + O(n^-6)
                            = (12 / 45) pi^6 / n^4 + O(n^-6)
```

attributable to the cubic-and-higher geometric terms in the expansion of
`L^2 - 4 pi A` around `r = 1`. Said differently:

```text
R_n decomposes at 1/n^4 as:
  (4/45) pi^6 / n^4     [mean-nonzero + L^2-mass correction to the Hessian]
+ (12/45) pi^6 / n^4    [cubic curvature of the isoperimetric functional]
= (16/45) pi^6 / n^4.
```

`R_n` is a geometric remainder, not an artifact of the lift, and each
piece has a clean interpretation.

---

## Consequence for `ARCHIMEDEAN-SIGNATURE.md`

Per the promotion path discussed in recent notes, the one conditional
gate that would let `ARCHIMEDEAN-SIGNATURE.md` host a cross-row theorem
was precisely this bilinear-form question. The gate opens affirmatively,
and the theorem statement is:

> **Cross-row theorem (strip-H¹ / circumscribed-Hurwitz identification).**
> Let `y_n` be the strip tissue and `gamma_tilde_n = (1 + y_n(theta/(2 pi))) e^{i theta}`
> its radial-graph lift, which coincides with the circumscribed regular
> `n`-gon. Then
>
> ```text
> ||y_n'||_L2([0,1])^2 = Delta(gamma_tilde_n) + R_n,
> R_n = (16/45) pi^6 / n^4 + (128/315) pi^8 / n^6 + O(n^-8),   R_n > 0.
> ```
>
> The shared leading constant `4 pi^4 / (3 n^2)` is a common evaluation of
> the isoperimetric-functional Hessian at the circle; `R_n` is the
> explicit geometric correction from mean-nonzero `L^2` mass and the
> cubic curvature of `L^2 - 4 pi A`.

The inscribed-vs-circumscribed comparison (the second step in the two-step
architecture of the earlier discussion) is the classical Archimedean
squeeze: `Delta(gamma_tilde_n) - Delta_n = (4/3) pi^6 / n^4 + O(n^-6)`,
pre-1882 in provenance.

---

## Follow-up edits this memo recommends

1. **`memos/STRIP-TISSUE-FOURIER.md`**, end of file. Replace the open
   question ("Are `Delta_n` and `||y_n'||_L2^2` evaluations of one bilinear
   form...") with the closure statement and a pointer here. The pairing
   goes through `gamma_tilde_n` (circumscribed), not `Delta_n` (inscribed),
   and the closure is affirmative with the explicit `R_n`.
2. **`memos/ARCHIMEDEAN-SIGNATURE.md`**, §"Program Use" or a new theorem
   section. Promote SIGNATURE from "companion vocabulary" to "companion
   vocabulary hosting one cross-row theorem," and state the identification
   above. The "intended promotion path" note in recent discussion can be
   retired: the gate is closed affirmatively.
3. **`memos/OLD-TIME-RELIGION.md`**, §(A5) Fourier/Parseval framing inside
   (A4). The Hurwitz gap of `gamma_tilde_n` is exactly the circumscribed
   `n`-gon's Hurwitz gap, so the `1/n^2` match is pre-1882 Fourier applied
   to a classical Archimedean object. Worth a one-line note.

These edits are outside the scope of this computation memo; flagged here
for a follow-up pass.

---

## What this does not claim

- Not a claim that `||y_n'||_L2^2 = Delta(gamma_tilde_n)` exactly. `R_n`
  is nonzero and explicit.
- Not a claim that the strip-tissue Fourier lattice `n Z` and the
  circumscribed-polygon arclength Fourier lattice `1 + n Z` are the same
  substrate. They are not; the identification is through a geometric
  lift, not a Fourier-coefficient isomorphism.
- Not a claim that `Delta_n` itself (inscribed) is the `H^1` seminorm of
  anything. The inscribed and circumscribed Hurwitz gaps differ at order
  `1/n^4` by `(4/3) pi^6 / n^4`; only the circumscribed lift is the
  right bridge to `||y_n'||^2`.
- Not a claim that the closure resolves anything in the closure-depth /
  F-obstruction program. That program is independent (per
  [memos/NATIVE-F-MINIMAL-DEFINITION.md](memos/NATIVE-F-MINIMAL-DEFINITION.md)).
  SIGNATURE becomes a companion with one theorem; the primary
  architecture is untouched.
