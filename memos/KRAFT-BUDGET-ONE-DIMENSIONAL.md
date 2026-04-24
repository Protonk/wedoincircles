# KRAFT-BUDGET-ONE-DIMENSIONAL

Working note for the one-dimensional constant consolidation behind
[memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md](memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md).
At present this note closes only Step 1 of
[memos/KRAFT-CONSTANT-CONSOLIDATION-PLAN.md](memos/KRAFT-CONSTANT-CONSOLIDATION-PLAN.md):
the shellized Erdős–Turán inequality at the dyadic cutoff

```text
m = 2^R - 1.
```

No attempt is made here to identify the correct linear Fourier shell
quantity. That is Step 2.

---

## Setup

For a sequence `x_1, ..., x_N` in `[0, 1)`, write

```text
S_N(h) = | (1/N) sum_{n=1}^N exp(2 pi i h x_n) |.
```

Erdős–Turán in the one-dimensional form quoted in
[memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md](memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md)
states that for every positive integer `m`,

```text
D_N <= 6/(m+1) + (4/pi) sum_{h=1}^m (1/h - 1/(m+1)) S_N(h).
```

Fix

```text
m = 2^R - 1,
```

so that `m + 1 = 2^R`.

---

## Shellized Erdős–Turán

At this cutoff, the frequency range `1 <= h <= m` is partitioned exactly by
the dyadic shells

```text
2^r <= h < 2^(r+1),   r = 0, ..., R-1.
```

Indeed,

```text
{1, ..., 2^R - 1}
= disjoint union over r = 0, ..., R-1 of
  {2^r, ..., 2^(r+1) - 1},
```

and shell `r` contains exactly `2^r` integers.

Therefore Erdős–Turán rewrites exactly as

```text
D_N
<= 6 * 2^(-R)
 + (4/pi) sum_{r=0}^{R-1}
     sum_{2^r <= h < 2^(r+1)}
       (1/h - 2^(-R)) S_N(h).
```

This is the shellized one-dimensional budget.

Define the shell weight

```text
w_{R,r}(h) = 1/h - 2^(-R),
```

for `2^r <= h < 2^(r+1)`, and the total shell cost

```text
A_{R,r}
= sum_{2^r <= h < 2^(r+1)} w_{R,r}(h)
= sum_{2^r <= h < 2^(r+1)} (1/h - 2^(-R)).
```

Then

```text
A_{R,r}
= (H_{2^(r+1)-1} - H_{2^r-1}) - 2^(r-R),
```

where `H_n = sum_{k=1}^n 1/k` is the `n`-th harmonic number.

Since `2^r <= h < 2^(r+1) <= 2^R`, every shell weight is strictly
positive:

```text
1/h - 2^(-R) > 0.
```

So each shell contributes a genuine positive budget, not a signed
correction.

---

## Per-shell harmonic cost

The unsubtracted harmonic shell satisfies

```text
sum_{2^r <= h < 2^(r+1)} 1/h = ln 2 + O(2^(-r)),
```

and in particular lies in `(ln 2, 1]`.

Hence

```text
A_{R,r}
= ln 2 - 2^(r-R) + O(2^(-r)).
```

Two consequences matter:

1. The cost of one shell is `O(1)`, uniformly in `r`.
2. The asymptotic shell cost is controlled by `ln 2`, not by a
   logarithm inside the shell.

This is the bookkeeping fact the consolidation plan wanted on the page.

---

## Total harmonic cost through shell R-1

Summing `A_{R,r}` over `r = 0, ..., R-1` gives

```text
A_R
= sum_{r=0}^{R-1} A_{R,r}
= sum_{h=1}^{2^R-1} (1/h - 2^(-R))
= H_{2^R-1} - (2^R - 1) 2^(-R)
= H_{2^R-1} - 1 + 2^(-R).
```

Using `H_n = log n + gamma + o(1)`,

```text
A_R
= R ln 2 + (gamma - 1) + o(1).
```

So the total shell cost is asymptotically `R ln 2`. This is exactly where
the eventual sampling-noise term

```text
R * N^(-1/2)
```

in [memos/KRAFT-CONSTANT-CONSOLIDATION-PLAN.md](memos/KRAFT-CONSTANT-CONSOLIDATION-PLAN.md)
comes from: one `N^(-1/2)` sampling error per Fourier evaluation, weighted
by a shell sum whose total cost is `R ln 2 + O(1)`.

---

## Immediate corollary for the next step

If one can produce a nonnegative shell quantity `L_r` such that on shell
`r`,

```text
S_N(h) <= linear_Fourier_mass(h) + N^(-1/2),
```

and

```text
sum_{2^r <= h < 2^(r+1)} linear_Fourier_mass(h) <= L_r,
```

then the shellized Erdős–Turán inequality becomes

```text
D_N
<= 6 * 2^(-R)
 + (4/pi) sum_{r=0}^{R-1} L_r
 + (4/pi) A_R N^(-1/2).
```

Since `A_R = R ln 2 + O(1)`, this has the target bookkeeping shape

```text
D_N <= K_0 [ 2^(-R) + shell_Fourier_term(R) + R * N^(-1/2) ].
```

The entire remaining issue is therefore Step 2 of the consolidation plan:
identify the right linear shell quantity and show that it interfaces
honestly with both Erdős–Turán and Aitchison.

---

## Status

Step 1 of
[memos/KRAFT-CONSTANT-CONSOLIDATION-PLAN.md](memos/KRAFT-CONSTANT-CONSOLIDATION-PLAN.md)
is now closed:

- exact dyadic partition at `m = 2^R - 1`,
- exact shellized Erdős–Turán inequality,
- exact shell cost `A_{R,r}`,
- total harmonic cost `A_R = R ln 2 + O(1)`.

What remains open is not shell bookkeeping but the bridge quantity.
