# LIOUVILLE-SCALE-TEST

Two-stage test of whether the K-H-L-A endgame survives reduction to a
single Archimedean approximant

```text
alpha_n := n tan(pi/n).
```

**Result.** Stage 1 is confirmed exactly. Stage 2 is negative. The naive
Liouville strategy of
[memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md](memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md)
§(C) dies on scale when reduced to `alpha_n`. No cyclotomic-unit
cancellation rescues it.

Computation in Sage at
[memos/liouville_scale_test.sage](memos/liouville_scale_test.sage).

---

## Stage 1 (positive): the single-approximant normal form

Symbolic verification (Sage `full_simplify` after substituting
`tan = sin/cos`) confirms the three factorizations exactly:

```text
Delta_n              = 4 A_n^{insc} * (alpha_n - pi)
Delta(gamma_tilde_n) = 4 A_n^{circ} * (alpha_n - pi)
||y_n'||_L2^2        = 4 A_n^{circ} * (alpha_n - pi)  +  R_n,
```

with

```text
A_n^{insc} = n sin(pi/n) cos(pi/n),
A_n^{circ} = n tan(pi/n) = alpha_n,
R_n        = 4 A_n^{circ} * [ (pi/3) tan^2(pi/n)  -  (alpha_n - pi) ].
```

Each residual cancellation is exact; Sage reports `0` for all three
differences.

The inner bracket of `R_n`,

```text
(pi/3) tan^2(pi/n) - (alpha_n - pi)  =  (4/45) pi u^4 + O(u^6),  u = pi/n,
```

cancels at `1/n^2` and leaves order `1/n^4`, which is why
`R_n = 16 pi^6/(45 n^4) + O(n^-6)` — consistent with
[memos/STRIP-H1-HURWITZ-CLOSURE.md](memos/STRIP-H1-HURWITZ-CLOSURE.md).

### Interpretation

The Fourier / Hurwitz / strip apparatus is **not producing a new small
algebraic quantity**. It is producing three different *geometric weights*
on the same underlying approximation data `alpha_n - pi`:

- `Delta_n` weights by `A_n^{insc}` (inscribed area),
- `Delta(gamma_tilde_n)` weights by `A_n^{circ}` (circumscribed area),
- `||y_n'||^2` weights by `A_n^{circ}` and adds a higher-order term whose
  inner factor also cancels to `alpha_n - pi` data.

Any endgame that contradicts an upper bound on one of these three
against a lower bound on its algebraic content is ultimately contradicting
the same numerical quantity: `|alpha_n - pi|`. That reduces the height
analysis to a single object.

---

## Stage 2 (negative): the height of `alpha_n` kills Liouville

### Degree and field

`alpha_n = n tan(pi/n) = n sin(pi/n) / cos(pi/n)`. Over `Q`:

- `cos(pi/n)` generates the real subfield of `Q(zeta_{2n})`, degree
  `phi(2n)/2`.
- `tan(pi/n)` requires a further square-root (`tan^2 = sec^2 - 1 in
  Q(cos(pi/n))`), so generically `deg(tan(pi/n)) = phi(2n)`, twice the
  real-subfield degree.
- Hence `deg_Q(alpha_n) = phi(2n)` generically. (For small `n` with
  accidental rationalities — e.g. `n = 4, 6, 8, 12` where `tan(pi/n)` is
  itself quadratic — the degree collapses; computed below.)

### Conjugates and height

The conjugates of `alpha_n` are `n tan(pi k / n)` for `k` in a Galois
orbit of size `deg(alpha_n)`. For `k` close to `n/2`,
`n tan(pi k / n) = n cot(pi (n-2k)/(2n)) ~ 2 n^2 / (pi (n - 2k))`. The
worst conjugate is at the `k` with `|n - 2k|` minimal, producing
`max |sigma(alpha_n)| ~ 2 n^2 / pi`.

Sage table (prime `n` selected):

```text
   n   deg(alpha_n)   max |conj|   log M(alpha_n)   log M / deg   log M / (deg * log n)
   3         2             5.20        3.296           1.648           1.500
   5         4            15.39        8.047           2.012           1.250
   7         6            30.67       13.621           2.270           1.167
  11        10            76.51       26.377           2.638           1.100
  13        12           107.07       33.344           2.779           1.083
  17        16           183.46       48.165           3.010           1.063
  19        18           229.30       55.944           3.108           1.056
  23        22           336.25       72.116           3.278           1.045
```

The ratio `log M(alpha_n) / (deg * log n)` converges to `~1` (approach
from above), so

```text
log M(alpha_n)  =  deg(alpha_n) * log n + O(deg)
             ~   phi(2n) * log n     for prime n.
```

The Mahler measure grows **exponentially** in `phi(2n) log n`. There is no
cyclotomic-unit cancellation that collapses this: the worst conjugate
(from `k` near `n/2`) is as large as the analysis predicts and is itself
an algebraic number of unbounded height.

### Liouville vs Archimedes

Suppose `pi` algebraic of degree `d >= 2` over `Q`. Then
`beta_n := alpha_n - pi` is algebraic of degree
`D_n <= d * deg(alpha_n) = d * phi(2n)` (generically).

Weak Liouville: for algebraic `beta != 0` of degree `D`,

```text
|beta| >= 1 / ( max_sigma |sigma(beta)| )^{D-1}.
```

For `beta_n`, `max_sigma |sigma(beta_n)| <= max |sigma(alpha_n)| +
max |sigma(pi)| ~ 2 n^2 / pi` (`sigma(pi)` contributes a bounded factor
`H(pi)`). So

```text
log |alpha_n - pi|  >=  -(D_n - 1) * log (2 n^2 / pi)
                    ~  -(d * phi(2n) - 1) * 2 log n.
```

Geometric upper bound (Archimedes, explicit Taylor):

```text
alpha_n - pi = pi^3 / (3 n^2) + 2 pi^5 / (15 n^4) + O(n^-6),
log |alpha_n - pi|  ~  -2 log n + log(pi^3/3) + O(1/n^2).
```

Collision (Liouville LB `>=` Archimedes UB) requires

```text
(d * phi(2n) - 1) * 2 log n  <=  2 log n + O(1)
-> d * phi(2n) - 1 <= 1 + O(1/log n)
-> d * phi(2n) <= 2 + O(1/log n).
```

For `d >= 2` and `phi(2n) >= 2` (true for every `n >= 3`), the product
`d * phi(2n) >= 4`, so the condition fails by a factor of at least 2 in
the exponent for **every** `n >= 3`.

Numerical confirmation (at `d = 2`, the loosest nontrivial hypothesis):

```text
   n   deg(alpha_n)  log M_n   Liouville LB @ d=2    Archimedes UB    Liouville wins?
   3          2       1.648           -4.94                0.14         no
   5          4       2.734          -19.14               -0.88         no
   7          6       3.423          -37.66               -1.56         no
  11         10       4.337          -82.41               -2.46         no
  13         12       4.673         -107.49               -2.79         no
  17         16       5.212         -161.57               -3.33         no
  19         18       5.435         -190.23               -3.55         no
  23         22       5.818         -250.17               -3.94         no
```

At `n = 23`, Archimedes is `exp(246)` larger than Liouville. The gap
widens with `n`.

### Cancellation check

If cyclotomic-unit identities collapsed `alpha_n`'s height, the ratio
`log M(alpha_n) / deg(alpha_n)` would be bounded as `n` grows. The table
in the Sage output shows this ratio is `~ log n` for primes — unbounded.
No cancellation. The worst conjugate `n cot(pi/(2n))` contributes `O(n^2)`
to the product, and that contribution survives all cyclotomic
simplifications.

---

## Verdict

- **Stage 1:** the reduction to `alpha_n` is the right normal form. The
  Fourier / Hurwitz / strip machinery is a choice of geometric weight, not
  a new small algebraic quantity.
- **Stage 2:** `alpha_n`'s algebraic height is exponential in `phi(n)
  log n`. Liouville under the hypothesis that `pi` is algebraic of degree
  `d >= 2` gives a lower bound on `|alpha_n - pi|` that is weaker than the
  Archimedean upper bound by a factor of `n^{2(d phi(n) - 1)}` for every
  `n >= 3`.
- **Consequence:** the Liouville endgame in its naive form — as sketched
  in KRAFT-HERMITE-LINDEMANN-AITCHISON §(C) — is not cogent.

## What this kills and what it leaves open

**Killed:** using the inscribed-Hurwitz gap (or any of its geometrically
weighted siblings) against a Liouville-style lower bound on the joint
cyclotomic × `Q(pi)` field to derive transcendence of `pi` at effective
rate. That collision does not occur; the scale is against us by
`n^{2 phi(n)}`.

**Not killed (by this memo):**

1. **Alternative small algebraic quantities.** If the program can build a
   small quantity with polynomial cyclotomic height — not `alpha_n - pi`,
   which has exponential height — Liouville may still apply. No such
   quantity is on the page; it would be a new invention.
2. **Non-Liouville Diophantine bounds.** Thue 1909, Siegel 1921, Roth
   1955 improve Liouville's exponent from `D` to `2 + epsilon`. These are
   post-L-W (Lindemann 1882 is pre-Thue), so using them in a pre-L-W
   argument is circular. Under current provenance discipline this path
   is closed; relaxing the discipline re-opens it at a cost.
3. **Discrepancy / averaging arguments over a range of `n`.** This is
   exactly what the Kraft-Parseval budget of
   [memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md](memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md)
   attempts. The budget does not go through `alpha_n` pointwise; it goes
   through discrepancy of `(n pi) mod 1`. That is a separate mechanism
   and is not scale-killed by this memo. It has its own open audit —
   see the empirical-to-density proxy (`KRAFT-BUDGET-ONE-DIMENSIONAL`
   Step 5).
4. **Closure-depth primary architecture.** The no-go of
   [memos/NATIVE-F-MINIMAL-DEFINITION.md](memos/NATIVE-F-MINIMAL-DEFINITION.md)
   is unaffected. It operates on qualitative algebraic closure, not on
   numerical heights.

## Consequence for `OLD-TIME-RELIGION`

The (A2) + (A3) directed attempt — "compute the norm/resultant lower bound
with explicit Archimedean squeeze" — has now been run. Result: the
cyclotomic-height growth of `alpha_n` is sharp, not an artifact of a
loose bound. (A2) closes **with a negative result** at the naive-Liouville
level.

The Reserve row *"cyclotomic units and sine-product identities"* (formerly
(A8) in the reserve list, now the key intended refinement) is still
available — it could in principle attack a different small algebraic
quantity — but it cannot rescue `alpha_n` specifically. That's confirmed.

Suggested update to `OLD-TIME-RELIGION.md`:

- Mark (A2) + (A3) closed with negative verdict, pointing here.
- Note that the "first directed attempt" in §(C) has resolved, and the
  next live directed attempt should target a *different* small algebraic
  quantity (per item 1 of "Not killed" above) or shift to discrepancy
  (item 3), rather than continuing with `alpha_n - pi`.

## What this memo does not claim

- Not a proof that `pi` is transcendental. It assumes `pi` algebraic and
  shows that Liouville-on-`alpha_n` fails to derive a contradiction; this
  is a failure of a proof strategy, not of the underlying fact.
- Not a claim that no pre-1882 endgame for `pi`-transcendence exists.
  It closes one specific endgame.
- Not a claim against the strip-H¹/Hurwitz cross-row theorem
  ([memos/STRIP-H1-HURWITZ-CLOSURE.md](memos/STRIP-H1-HURWITZ-CLOSURE.md)).
  That theorem stands; it does not use Liouville.
- Not a claim that `alpha_n` is uninteresting. It is the natural
  irrationality-measure candidate for `pi`, with `|alpha_n - pi| ~ 1/n^2`;
  this just isn't the right register for the height.
