# HURWITZ-FIRST-BAND-CONCENTRATION

## Setup

For the inscribed regular `n`-gon in the unit circle, write

```text
L_n = 2 n sin(pi / n),
A_n = (n / 2) sin(2 pi / n),
Delta_n = L_n^2 - 4 pi A_n.
```

The arc-length Fourier coefficients from
[corners/hurwitz_gap.sage](corners/hurwitz_gap.sage) are

```text
c_m^(n) = 0                                unless m = 1 + j n,
c_(1 + j n)^(n) = L_n^2 / (4 pi^2 (1 + j n)^2),   j in Z.
```

Hurwitz's identity therefore reads

```text
Delta_n = 4 pi^2 sum_{j in Z, j != 0} m(m-1) |c_m^(n)|^2,
          m = 1 + j n.
```

The `j = 0` term drops because then `m = 1` and `m(m-1) = 0`.

For each `j >= 1`, pair the frequencies `m = 1 +- j n` and define

```text
B_j(n) = 4 pi^2 [
  (1 + j n)(j n)          |c_(1 + j n)^(n)|^2
  +
  (1 - j n)(-j n)         |c_(1 - j n)^(n)|^2
].
```

Both bracket terms are strictly positive for `n >= 3`, `j >= 1`:
`(1 + j n)(j n) > 0`, and

```text
(1 - j n)(-j n) = j n (j n - 1) > 0
```

because `j n >= 3`. Hence

```text
Delta_n = sum_{j >= 1} B_j(n)
```

as a sum of positive paired-band contributions.

---

## Theorem

For every `n >= 3`:

1. The paired-band terms have the closed form

   ```text
   B_j(n) = (L_n^4 / (2 pi^2)) *
            [j^2 n^2 (j^2 n^2 + 3)] / (j^2 n^2 - 1)^3,
            j >= 1.
   ```

2. They satisfy the comparison bound

   ```text
   B_j(n) <= B_1(n) / j^2
   ```

   for every `j >= 1`.

3. Consequently the first band carries a uniform proportion of the whole
   Hurwitz gap:

   ```text
   B_1(n) >= (6 / pi^2) Delta_n.
   ```

4. More generally, for every `r >= 0`, one has the dyadic-shell estimate

   ```text
   sum_{2^r <= j < 2^(r+1)} B_j(n) <= 2^(-r) B_1(n).
   ```

The constant `6 / pi^2` is sharp:

```text
B_1(n) / Delta_n -> 6 / pi^2
```

as `n -> infty`.

---

## Proof

### Step 1. Closed form for `B_j(n)`

Substitute

```text
|c_(1 +- j n)^(n)|^2 = L_n^4 / (16 pi^4 (1 +- j n)^4)
```

into the definition of `B_j(n)`. This gives

```text
B_j(n)
= (L_n^4 / (4 pi^2)) [
    j n / (1 + j n)^3
    -
    j n / (1 - j n)^3
  ].
```

Now simplify:

```text
j n / (1 + j n)^3  -  j n / (1 - j n)^3
  =  j n * [(1 - j n)^3 - (1 + j n)^3] / (1 - j^2 n^2)^3
  =  j n * [-2 j n (3 + j^2 n^2)]      / (1 - j^2 n^2)^3
  =  2 j^2 n^2 (j^2 n^2 + 3)           / (j^2 n^2 - 1)^3,
```

using `(1 - j^2 n^2)^3 = -(j^2 n^2 - 1)^3`. Therefore

```text
B_j(n) = (L_n^4 / (2 pi^2)) *
         [j^2 n^2 (j^2 n^2 + 3)] / (j^2 n^2 - 1)^3.
```

That proves the formula.

### Step 2. Comparison with the first band

Write

```text
B_j(n) = (L_n^4 / (2 pi^2)) G(j n),
```

where

```text
G(x) = x^2 (x^2 + 3) / (x^2 - 1)^3.
```

For fixed `n`, the prefactor depends on `n` but not on `j`, so

```text
B_j(n) / B_1(n) = G(j n) / G(n).
```

Define

```text
H(x) = x^2 G(x) = x^4 (x^2 + 3) / (x^2 - 1)^3.
```

Writing `t = x^2`,

```text
H(x) = t^2 (t + 3) / (t - 1)^3,
d/dt H = -6 t (t + 1) / (t - 1)^4 < 0
```

for `t > 1`. Since `t(x) = x^2` is strictly increasing on `x > 0`,
`H` is strictly decreasing on `(1, infty)`. Thus for `n >= 3` and
`j >= 1`,

```text
H(j n) <= H(n).
```

Unpacking `H(x) = x^2 G(x)` gives

```text
(j n)^2 G(j n) <= n^2 G(n)
=> j^2 G(j n)  <= G(n)
=> G(j n)      <= G(n) / j^2
=> B_j(n)      <= B_1(n) / j^2.
```

This is the required comparison bound.

### Step 3. Zeta corollary

Because `Delta_n = sum_{j >= 1} B_j(n)` and `B_j(n) <= B_1(n) / j^2`,

```text
Delta_n
<= B_1(n) sum_{j >= 1} 1 / j^2
= zeta(2) B_1(n)
= (pi^2 / 6) B_1(n).
```

So

```text
B_1(n) / Delta_n >= 1 / zeta(2) = 6 / pi^2.
```

This proves the theorem.

To see sharpness, fix `j` and let `n -> infty`. Since `L_n -> 2 pi`,

```text
B_j(n) ~ 8 pi^2 / (j^2 n^2).
```

Summing over `j >= 1`,

```text
Delta_n ~ (8 pi^2 / n^2) sum_{j >= 1} 1 / j^2
        = 8 pi^2 zeta(2) / n^2
        = 4 pi^4 / (3 n^2).
```

Hence

```text
B_1(n) / Delta_n -> 1 / zeta(2) = 6 / pi^2
```

from above.

### Step 4. Dyadic-shell estimate

Fix `r >= 0`. For every `j` in the shell `2^r <= j < 2^(r+1)`, Step 2
gives

```text
B_j(n) <= B_1(n) / j^2 <= B_1(n) * 2^(-2r).
```

There are exactly `2^r` integers `j` in that shell, so

```text
sum_{2^r <= j < 2^(r+1)} B_j(n)
<= 2^r * B_1(n) * 2^(-2r)
= 2^(-r) B_1(n).
```

This is the claimed shell estimate.

---

## Numerical check

Computed by
[`corners/hurwitz_shell_masses.sage`](corners/hurwitz_shell_masses.sage)
at 200-bit precision. The closed form matches the direct paired
Hurwitz-Parseval sum to machine precision in a `sage -python` check at

- `n in {3, 5, 7, 10, 40}`,
- `j in {1, 2, 3, 4, 5}`.

### First-band ratio

Exact closed-form values of `B_1(n) / Delta_n`:

| `n` | `B_1(n) / Delta_n` |
|---:|---:|
| 3 | 0.7297110451 |
| 5 | 0.6555644296 |
| 7 | 0.6327917727 |
| 10 | 0.6202588877 |
| 40 | 0.6087062638 |

Asymptotic limit `6 / pi^2 = 0.6079271019...`; already visible by
`n = 40`.

### Dyadic-shell masses at `n = 10`

| `r` | shell range | `S_r(n)` | `2^(-r) B_1(n)` | `S_r / bound` | `S_r / S_(r-1)` |
|---:|---:|---:|---:|---:|---:|
| 0 | `[1, 1]` | 7.846e-1 | 7.846e-1 | 1.0000 | — |
| 1 | `[2, 3]` | 2.702e-1 | 3.923e-1 | 0.6889 | 0.3444 |
| 2 | `[4, 7]` | 1.117e-1 | 1.962e-1 | 0.5693 | 0.4132 |
| 3 | `[8, 15]` | 5.077e-2 | 9.808e-2 | 0.5176 | 0.4546 |
| 4 | `[16, 31]` | 2.421e-2 | 4.904e-2 | 0.4937 | 0.4769 |
| 5 | `[32, 63]` | 1.182e-2 | 2.452e-2 | 0.4822 | 0.4884 |

The bound `S_r(n) <= 2^(-r) B_1(n)` holds row by row. Cumulative
through `r = 5`: `99.08%` of `Delta_10`.

### Asymptotic of `S_r / bound` is `n`-dependent

Closed-form gives, for fixed `n`,

```text
lim_{r -> infty} S_r(n) / (2^(-r) B_1(n))
  = (n^2 - 1)^3 / (2 n^4 (n^2 + 3)).
```

Sample values:

| `n` | limit |
|---:|---:|
| 3 | 0.2634 |
| 5 | 0.3950 |
| 7 | 0.4429 |
| 10 | 0.4710 |
| 40 | 0.4981 |

The "factor-of-two slack" reading of the dyadic-shell bound is
asymptotic in `n` as well as in `r`; for small `n`, the bound is
meaningfully tighter at large `r` than `(1/2) B_1(n)` would suggest.
The decay ratio `S_r / S_(r-1) -> 1/2` is the universal-in-`n`
asymptotic; the bound-comparison ratio is not.

---

## Asymptotic expansion of `B_1(n) / Delta_n`

The first-band concentration ratio admits a closed-form asymptotic
expansion in `1/n^2`, with rational-in-`pi^2` coefficients to all
orders. Through `O(1/n^6)`:

```text
B_1(n) / Delta_n = 6/pi^2
                 + 12 (15 - pi^2) / (5 pi^2 n^2)
                 + 2 (34 pi^4 - 1260 pi^2 + 7875) / (175 pi^2 n^4)
                 - 4 (22 pi^6 - 1530 pi^4 + 23625 pi^2 - 110250) /
                   (2625 pi^2 n^6)
                 + O(1/n^8).
```

Numerical leading-correction constant: `12(15 - pi^2)/(5 pi^2) ≈
1.24756`. The sign of the leading correction is **positive**, so the
excess `B_1(n)/Delta_n - 6/pi^2` approaches zero from above as
`n -> infty` — matching the table above (`0.7297, 0.6556, 0.6328,
0.6203, 0.6087 -> 0.6079271 ...`), where the inequality `B_1(n) >=
(6/pi^2) Delta_n` from §"Theorem" is approached, not realized, at
each finite `n`.

### Derivation

Set `u = pi/n` and substitute the closed forms `B_1(n) = (L_n^4 /
(2 pi^2)) * n^2 (n^2 + 3) / (n^2 - 1)^3` and `Delta_n = L_n^2 *
[1 - (pi/n) cot(pi/n)]`. The ratio becomes

```text
B_1(n)/Delta_n = 2 pi^2 sin^2(u) (pi^2 + 3 u^2) /
                 [(pi^2 - u^2)^3 * (1 - u cot u)],
```

a rational expression in `sin u`, `cos u`, and polynomials in `u` and
`pi`. Taylor expansion around `u = 0` gives the coefficients above.

### Numerical agreement

Computed at 200-bit precision by
[corners/hurwitz_first_band_excess.sage](corners/hurwitz_first_band_excess.sage):

| `n` | exact `B_1/Delta` | leading + `c_1/n^2` | through `c_3/n^6` |
|---:|---:|---:|---:|
| 3 | 0.7297110451 | 0.7465451698 | 0.7297444674 |
| 5 | 0.6555644296 | 0.6578296063 | 0.6555650004 |
| 7 | 0.6327917727 | 0.6333875633 | 0.6327918115 |
| 10 | 0.6202588877 | 0.6204027280 | 0.6202588900 |
| 40 | 0.6087062638 | 0.6087068285 | 0.6087062638 |
| 100 | 0.6080518437 | 0.6080518581 | 0.6080518437 |
| 10000 | 0.6079271143 | 0.6079271143 | 0.6079271143 |

By `n = 10000`, the truncation through `O(1/n^6)` matches the exact
value to floating-point precision; for `n >= 10`, the leading
`c_1/n^2` correction is good to better than 1 part in 4000.

### Inheritance across the Archimedean squeeze

The expansion is *invariant* across the inscribed/circumscribed
squeeze of [corners/hurwitz_gap_circumscribed.sage](corners/hurwitz_gap_circumscribed.sage).
Both `B_j(n)` and `Delta_n` scale by the same `sec^2(pi/n)` factor
between inscribed and circumscribed regular `n`-gons, so the ratio
`B_1(n)/Delta_n` is identical on the two sides; the leading
correction `~ 1.24756/n^2` and all higher-order coefficients above
transfer verbatim. The first-band concentration story — `6/pi^2`
asymptote, with this explicit pre-asymptotic correction — therefore
holds uniformly across the squeeze without modification.

### What this closes

The open question at [paper/POLYGONAL-LEDGER.md](paper/POLYGONAL-LEDGER.md)
§"Open" — "whether the sharpness constant `6/pi^2` has tractable
higher-order corrections (the `B_1(n)/Delta_n` excess decays as
`O(1/n^2)`)" — is closed: yes, fully tractable, with explicit
rational-in-`pi^2` coefficients. The leading rate is `O(1/n^2)` as
predicted, with the explicit constant `12(15 - pi^2)/(5 pi^2)`.
