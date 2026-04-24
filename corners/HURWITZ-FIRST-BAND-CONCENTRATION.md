# HURWITZ-FIRST-BAND-CONCENTRATION

This note promotes the first-band picture in
[corners/HURWITZ-GAP.md](corners/HURWITZ-GAP.md) from "visible in the
stacked frequency plot" to an explicit theorem. It closes Steps 1–4 of
[memos/HURWITZ-FIRST-BAND-CONCENTRATION-PLAN.md](memos/HURWITZ-FIRST-BAND-CONCENTRATION-PLAN.md):

- derive the paired-band formula,
- prove the monotonic comparison lemma,
- take the zeta corollary.
- derive the dyadic-shell estimate.

The shell estimate is the first honest Kraft-shaped corollary on the
Fourier side: it turns the `1/j^2` band decay into geometric decay on
dyadic shells.

---

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

The closed form matches the direct paired Hurwitz-Parseval sum to machine
precision in a `sage -python` check at

- `n in {3, 5, 7, 10, 40}`,
- `j in {1, 2, 3, 4, 5}`.

The first-band ratio behaves as predicted:

| `n` | `B_1(n) / Delta_n` |
|---:|---:|
| 3 | 0.7297250691 |
| 5 | 0.6555814041 |
| 7 | 0.6328095073 |
| 10 | 0.6202770089 |
| 40 | 0.6087247208 |

while

```text
6 / pi^2 = 0.6079271019...
```

So the theorem constant is correct and the asymptotic sharpness is visible
already by `n = 40`.

The shell estimate is also numerically consistent with the same data:
for fixed `n`, shell masses decrease geometrically and stay well below
the upper bound `2^(-r) B_1(n)`.

---

## Program use

This note closes the first theorem-level ingredient behind the Fourier side
of [memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md](memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md):
the Hurwitz gap is not merely concentrated near the first admissible band
empirically, but uniformly controlled there with an explicit constant, and
the higher bands satisfy a genuine dyadic-shell estimate.

What it does not yet close is the global Aitchison `×` Erdős–Turán–Koksma
constant consolidation. The local Fourier budget is now Kraft-shaped; the
remaining work is to splice that local estimate into the full discrepancy /
density budget without overstating what the shell inequality alone proves.
