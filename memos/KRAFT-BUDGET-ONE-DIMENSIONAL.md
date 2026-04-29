# KRAFT-BUDGET-ONE-DIMENSIONAL

Working note for the one-dimensional constant consolidation behind
[memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md](memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md).
At present this note closes Step 1, records a direct Step 2 attempt,
pushes Step 3 through conditionally on that Step 2 candidate, closes Step
3.5 by identifying the exact Aitchison-facing object from the
phase-adjusted polygon signal, closes Step 4 by applying Fortnow's
universal dominance to the honest paired-shell semimeasure, and closes
Step 5 by assembling the final one-dimensional bookkeeping lemma for
[memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md](memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md):
the shellized Erdős–Turán inequality at the dyadic cutoff

```text
m = 2^R - 1.
```

The one-dimensional bookkeeping is now complete. What remains in the
parent KRAFT memo is no longer constant consolidation but the next
program-level step: the L-W-safety audit on a drafted argument.

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

## Step 2 attempt: direct linear shell mass

The explicit coefficient formula from
[corners/HURWITZ-FIRST-BAND-CONCENTRATION.md](corners/HURWITZ-FIRST-BAND-CONCENTRATION.md)
suggests the direct linear quantity immediately.

For `j >= 1`, define the paired linear mass

```text
lambda_j(n)
= |c_(1 + j n)^(n)| + |c_(1 - j n)^(n)|.
```

Using

```text
c_(1 + j n)^(n) = L_n^2 / (4 pi^2 (1 + j n)^2),
c_(1 - j n)^(n) = L_n^2 / (4 pi^2 (1 - j n)^2),
```

one gets

```text
lambda_j(n)
= (L_n^2 / (4 pi^2)) [ 1/(1 + j n)^2 + 1/(1 - j n)^2 ]
= (L_n^2 / (2 pi^2)) * (1 + j^2 n^2) / (j^2 n^2 - 1)^2.
```

Now define the direct shell quantity

```text
L_r^(pair)(n)
= sum_{2^r <= j < 2^(r+1)} lambda_j(n).
```

This is the natural linear analog of the quadratic shell quantity from the
Hurwitz gap theorem.

### Direct shell bound

Let `x = j n`. For `x >= 3`,

```text
2 (1 + x^2) / (x^2 - 1)^2 <= 3 / x^2.
```

Indeed this is equivalent to

```text
0 <= x^4 - 8 x^2 + 3,
```

which holds for `x >= 3` since the derivative `4x(x^2 - 4)` is positive
there and the value at `x = 3` is already positive.

Therefore

```text
lambda_j(n) <= (3 L_n^2 / (4 pi^2 j^2 n^2)).
```

Summing over shell `r`,

```text
L_r^(pair)(n)
<= (3 L_n^2 / (4 pi^2 n^2)) sum_{2^r <= j < 2^(r+1)} 1/j^2
<= (3 L_n^2 / (4 pi^2 n^2)) 2^(-r).
```

Since `L_n <= 2 pi`, one also has the crude universal bound

```text
L_r^(pair)(n) <= 3 * 2^(-r) / n^2.
```

So the direct linear shell quantity has the same geometric shell shape as
the already-closed quadratic shell theorem.

### Positive-frequency version

For the one-sided positive frequencies used by Erdős–Turán, define

```text
L_r^(+)(n)
= sum_{2^r <= j < 2^(r+1)} |c_(1 + j n)^(n)|.
```

Then trivially

```text
L_r^(+)(n) <= L_r^(pair)(n),
```

so the same shell bound holds for the positive-frequency quantity as well.

### Shell-index alignment

The remaining bookkeeping issue is not decay but indexing.

Erdős–Turán shells frequencies by `h`, whereas the natural sparse Hurwitz
quantity shells admissible modes by `j` with

```text
h = 1 + j n.
```

For fixed `n` and `r`, the `j`-shell `2^r <= j < 2^(r+1)` maps into the
frequency interval

```text
1 + n 2^r <= h < 1 + n 2^(r+1),
```

whose ratio of endpoints is strictly less than `2`. Hence the image of one
`j`-shell lies inside at most two adjacent dyadic `h`-shells.

So the shell mismatch is mild: it is a constant-factor alignment issue, not
a logarithmic tax.

### What this does and does not settle

This direct route closes the local analytic part of Step 2:

- there is a natural direct linear shell quantity,
- it has the correct `2^(-r)` decay,
- and its shell index aligns with the `h`-shells up to a constant factor.

What it does **not** yet settle is the interpretive part:
why this coefficient shell is the right honest interface to Aitchison's
characteristic-function coefficients rather than merely a local surrogate
with the same decay profile.

---

## Step 3 attempt: shell subprobability

Condition on the Step 2 candidate `L_r^(+)(n)`. The direct shell bound
gives

```text
L_r^(+)(n) <= C_n 2^(-r),
```

where

```text
C_n = 3 L_n^2 / (4 pi^2 n^2) = 3 sin^2(pi/n) / pi^2.
```

Since

```text
sum_{r >= 0} 2^(-r) = 2,
```

the normalized local shell weights

```text
tau_n(r) = L_r^(+)(n) / (2 C_n),   r >= 0,
```

satisfy

```text
sum_{r >= 0} tau_n(r)
<= sum_{r >= 0} 2^(-(r+1))
= 1.
```

So for each fixed `n >= 3`, `tau_n` is a genuine subprobability on shell
index `r`.

### Local status

The normalization is explicit and computable:

- `L_r^(+)(n)` is a finite sum of explicit closed-form coefficients,
- `C_n` is an explicit elementary function of `n`,
- therefore `tau_n(r)` is computable uniformly in `(n, r)`.

In particular, `tau_n` is semicomputable as required for a Fortnow-style
dominance statement.

Sample partial sums through `r = 19`:

| `n` | `sum_{r=0}^{19} tau_n(r)` |
|---:|---:|
| 3 | 0.1826 |
| 5 | 0.2112 |
| 7 | 0.2262 |
| 10 | 0.2389 |
| 40 | 0.2645 |

So the local normalization is comfortably non-vacuous.

### Global Fortnow-ready object

To package the local shell budgets into one object for universal
dominance, fix any standard computable self-delimiting encoding

```text
code(n, r)
```

of integer pairs. Define

```text
tau_hat(code(n, r)) = 2^(-n) tau_n(r),   n >= 3, r >= 0,
```

and `tau_hat(x) = 0` for strings `x` not of that form.

Then

```text
sum_x tau_hat(x)
= sum_{n >= 3} sum_{r >= 0} 2^(-n) tau_n(r)
<= sum_{n >= 3} 2^(-n)
< 1.
```

So `tau_hat` is a computable semimeasure on encoded pairs. This is the
correct object to which Fortnow Fact 6.2 can be applied if the direct shell
candidate from Step 2 is accepted as the right bridge quantity.

### What this settles

The normalization problem itself is now closed, conditional on Step 2:

- local shell subprobability `tau_n` exists,
- global computable semimeasure `tau_hat` exists,
- Fortnow can be inserted without further normalization work.

That interpretive issue is resolved in Step 3.5 below.

---

## Step 3.5: the honest interface

The interface question can be settled starting from the polygon's own
complex position signal.

Let

```text
Gamma_n(y) = gamma_n(2 pi y)
           = sum_{m in Z} c_m^(n) e^(2 pi i m y),
           y in [0, 1),
```

where `gamma_n` is the unit-speed inscribed regular `n`-gon and the
coefficients `c_m^(n)` are the Hurwitz coefficients already in use above.

### Step 3.5a. Use the `j`-indexed convention and peel off the `h = 1` term

The support issue is resolved by starting from `Gamma_n` and removing the
circle mode explicitly. Define the phase-adjusted signal

```text
Q_n(y) = e^(-2 pi i y) Gamma_n(y)
       = sum_{j in Z} c_(1 + j n)^(n) e^(2 pi i j n y).
```

This converts the sparse support from `1 + n Z` to `n Z`. The `h = 1`
term becomes the constant mode

```text
c_1^(n) = L_n^2 / (4 pi^2),
```

which is exactly the non-decaying main term that had to be treated
separately.

So the right indexing convention for the interface test is:

- shell `r` means `2^r <= j < 2^(r+1)`,
- the corresponding Aitchison frequencies are `s = +- j n`,
- and the `h = 1` contribution has already been peeled off into the
  constant term `c_1^(n)`.

### Step 3.5b. Build a real density from the phase-adjusted signal

Take the centered real part

```text
R_n(y) = Re(Q_n(y) - c_1^(n))
       = sum_{j >= 1} lambda_j(n) cos(2 pi j n y),
```

where

```text
lambda_j(n) = c_(1 + j n)^(n) + c_(1 - j n)^(n)
            = (L_n^2 / (2 pi^2)) * (1 + j^2 n^2) / (j^2 n^2 - 1)^2.
```

Now define

```text
g_n(y) = 1 + R_n(y).
```

This is a genuine probability density on `[0, 1)`. Indeed:

1. `R_n` has mean zero, so `int_0^1 g_n(y) dy = 1`.
2. Since `|R_n(y)| <= sum_{j >= 1} lambda_j(n)`, the direct bound from
   Step 2 gives

   ```text
   sum_{j >= 1} lambda_j(n)
   <= (3 L_n^2 / (4 pi^2 n^2)) sum_{j >= 1} 1 / j^2
   <= 3 zeta(2) / n^2
   <= pi^2 / 18
   < 1.
   ```

   Therefore

   ```text
   g_n(y) >= 1 - pi^2 / 18 > 0
   ```

   for every `y` and every `n >= 3`.

Let `X_n` be the random variable on `[0, 1)` with density `g_n`.

### Step 3.5c. Exact coefficient identity

Because

```text
g_n(y) = 1 + sum_{j >= 1} [lambda_j(n) / 2]
               [e^(2 pi i j n y) + e^(-2 pi i j n y)],
```

its Fourier coefficients satisfy

```text
C_(X_n)(2 pi s) = 0                 unless s = +- j n,
C_(X_n)(+- 2 pi j n) = lambda_j(n) / 2,   j >= 1.
```

So the honest Aitchison shell is exactly the paired shell from Step 2:

```text
sum_{2^r <= j < 2^(r+1)}
  [ |C_(X_n)(2 pi j n)| + |C_(X_n)(-2 pi j n)| ]
= sum_{2^r <= j < 2^(r+1)} lambda_j(n)
= L_r^(pair)(n).
```

This is Outcome 1 from the plan: exact identification, on the nose.

### Step 3.5d. Comparison back to the positive-frequency direct shell

The exact Aitchison interface is paired, but it stays uniformly comparable
to the positive-frequency direct quantity from Step 2.

For `j >= 1`,

```text
lambda_j(n) / (2 c_(1 + j n)^(n))
= (1/2) [1 + ((j n + 1) / (j n - 1))^2].
```

Since `j n >= 3`, this ratio lies in `[1, 5/2]`. Therefore

```text
c_(1 + j n)^(n)
<= |C_(X_n)(2 pi j n)|
<= (5/2) c_(1 + j n)^(n),
```

and after summing over a shell,

```text
L_r^(+)(n)
<= sum_{2^r <= j < 2^(r+1)} |C_(X_n)(2 pi j n)|
<= (5/2) L_r^(+)(n).
```

So the positive-frequency shell from Step 2 was not a wrong object; it was
an asymmetric surrogate for an exact paired interface.

### Step 3.5e. Numerical sanity check

The analytic positivity bound is uniform:

```text
g_n(y) >= 1 - pi^2 / 18 ~= 0.4517.
```

Direct sample checks using the explicit cosine series give:

| `n` | `sum_{j >= 1} lambda_j(n)` | sampled `min_y g_n(y)` |
|---:|---:|---:|
| 3 | 0.3160 | 0.8161 |
| 5 | 0.1248 | 0.9339 |
| 7 | 0.0653 | 0.9663 |
| 10 | 0.0325 | 0.9835 |
| 40 | 0.0021 | 0.9990 |

At the pointwise comparison level, the worst-case value of

```text
lambda_j(n) / c_(1 + j n)^(n)
```

occurs at `(n, j) = (3, 1)` and equals `5`, so the `5/2` one-sided
constant above is sharp.

### What this settles

Step 3.5 is now closed:

- the exact candidate `X_n` is on the page,
- the `h = 1` main term has been treated explicitly,
- the shell index is fixed as the `j`-index on support `s = +- j n`,
- the Aitchison coefficients are identified exactly,
- and the direct Step 2 shell is uniformly comparable to the positive
  Aitchison shell.

The honest Aitchison-facing shell quantity is `L_r^(pair)(n)`, not
`L_r^(+)(n)`.

The same normalization from Step 3 now applies to the honest shell:

```text
tau_n^(Ait)(r) = L_r^(pair)(n) / (2 C_n),
```

with

```text
sum_{r >= 0} tau_n^(Ait)(r) <= 1.
```

So Step 4 is now licensed: the semimeasure normalization exists for the
exact Aitchison interface, not just for a local surrogate.

---

## Step 4: Fortnow on the honest paired shell

The honest shell from Step 3.5 is

```text
L_r^(pair)(n)
= sum_{2^r <= j < 2^(r+1)}
  [ |C_(X_n)(2 pi j n)| + |C_(X_n)(-2 pi j n)| ].
```

Define the exact local shell weights

```text
tau_n^(Ait)(r) = L_r^(pair)(n) / (2 C_n),
```

with

```text
C_n = 3 L_n^2 / (4 pi^2 n^2).
```

Because Step 2 gave

```text
L_r^(pair)(n) <= C_n 2^(-r),
```

one has

```text
sum_{r >= 0} tau_n^(Ait)(r)
<= sum_{r >= 0} 2^(-(r+1))
= 1.
```

So `tau_n^(Ait)` is a genuine subprobability on shell index `r` for each
fixed `n >= 3`.

### Global semimeasure

Fix a standard computable self-delimiting encoding

```text
code(n, r)
```

of integer pairs and define

```text
tau_hat^(Ait)(code(n, r)) = 2^(-n) tau_n^(Ait)(r),   n >= 3, r >= 0,
```

with `tau_hat^(Ait)(x) = 0` otherwise. Then

```text
sum_x tau_hat^(Ait)(x)
= sum_{n >= 3} sum_{r >= 0} 2^(-n) tau_n^(Ait)(r)
<= sum_{n >= 3} 2^(-n)
< 1.
```

Since `L_r^(pair)(n)` is an explicit finite sum of closed-form
coefficients, `tau_hat^(Ait)` is computable and hence semicomputable.

### Fortnow pullback

Fortnow Fact 6.2 applies to `tau_hat^(Ait)`, so there is a universal
constant `c > 0` such that

```text
tau_hat^(Ait)(x) <= c mu(x),
```

for every string `x`, where

```text
mu(x) = 2^(-K(x))
```

is the universal semicomputable measure.

Evaluating at `x = code(n, r)` gives

```text
2^(-n) tau_n^(Ait)(r) <= c mu(code(n, r)),
```

hence

```text
tau_n^(Ait)(r) <= c 2^n mu(code(n, r)).
```

Substituting back the definition of `tau_n^(Ait)` yields the local shell
bound

```text
L_r^(pair)(n)
<= 2 C_n c 2^n mu(code(n, r))
= (3 c L_n^2 / (2 pi^2 n^2)) 2^n mu(code(n, r)).
```

Using `L_n <= 2 pi`, one also gets the crude uniform form

```text
L_r^(pair)(n) <= (6 c / n^2) 2^n mu(code(n, r)).
```

This is the exact local variant required by Step 4 of the plan: Fortnow's
universal constant dominates the honest Aitchison-facing shell, not the
earlier positive-frequency surrogate.

### What this settles

Step 4 is now closed:

- the honest paired shell `tau_n^(Ait)` is on the page,
- the global encoded-pair semimeasure `tau_hat^(Ait)` is explicit,
- Fortnow Fact 6.2 applies directly to that semimeasure,
- and the pullback inequality for `L_r^(pair)(n)` is explicit.

What remains is Step 5: insert this exact shell bound back into the
shellized Erdős–Turán inequality and consolidate the constants into one
final bookkeeping lemma.

---

## Step 5: final one-dimensional bookkeeping lemma

The only new ingredient in this step is the empirical-to-density proxy.
Everything else is now explicit.

### Hypothesis

Fix `n >= 3`, `R >= 1`, and an empirical sequence `x_1, ..., x_N` in
`[0, 1)`. Let `X_n` be the exact density from Step 3.5. Assume that for
every frequency `1 <= h <= 2^R - 1`,

```text
S_N(h) <= |C_(X_n)(2 pi h)| + N^(-1/2),
```

where

```text
S_N(h) = | (1/N) sum_{m=1}^N e^(2 pi i h x_m) |.
```

This is the density-orbit interface hypothesis already implicit in the
parent memo. Step 5 treats it as a hypothesis, not as a theorem proved in
this note.

### Operational precedents

The parent memo now fixes the relevant arithmetic classification before
this interface is used: for the continued-fraction parameter
`beta(alpha) = limsup log(q_{n+1}) / q_n` extracted in
[rotations/10-MARTINIS-BRIEF.md](rotations/10-MARTINIS-BRIEF.md)
§"The Arithmetic Parameter", existing finite irrationality-measure
results put `pi` on the `beta(pi) = 0` / Diophantine side. Thus Step 5's
open point is the empirical-to-density proxy itself, not a choice between
Liouville and Diophantine regimes.

The one-dimensional operational template is Lefèvre–Muller–Tisserand's
Three Distance Theorem filter for the table-maker's dilemma, extracted in
[rotations/3DT-BRIEF.md](rotations/3DT-BRIEF.md) §"Lefèvre–Muller–
Tisserand: The Algorithmic Lens." Their loop keeps the rotation orbit
compressed in the variables `gamma, delta, d, u, v`: `gamma` and
`delta` are the current two shorter gap lengths, `u` and `v` count arcs
of those lengths, and `d` is the running lower bound to grid points. The
updates are Euclidean-style subtractions on `gamma` and `delta`, with
matching updates to `u` and `v`; the filter works without enumerating
the orbit points. This is not a proof of the proxy, but it is a worked
one-dimensional algorithmic precedent for replacing explicit orbit
enumeration by density-shaped bookkeeping.

The loop is instantiated for $\alpha = \pi$ at
[corners/lefevre_muller_pi.sage](corners/lefevre_muller_pi.sage). The
script verifies termination, sublinear compression
(8 ops at $N = 10$ scaling to 330 ops at $N = 10^7$), the lower-bound
semantics $d_{\text{LMT}} \le d_{\text{brute}}$, and the
$(u + v) = q_n$ correspondence with $\pi$'s CF convergent
denominators. The instance discharges Open Slot A of
[rotations/SIX-LENS-SYNTHESIS.md](rotations/SIX-LENS-SYNTHESIS.md) and
upgrades this Step 5 citation from rhetorical to demonstrated.

The complementary higher-dimensional precedent is Beck 1994, briefed at
[iso/BECK-1994-BRIEF.md](iso/BECK-1994-BRIEF.md): Fourier + Poisson +
Fejér smoothing + second-moment / Borel-Cantelli machinery substitutes
for continued fractions in `k >= 2` discrepancy. Beck does not give a
pointwise bound for `pi`, but it supplies the higher-dimensional
Fourier-substitute methodology adjacent to Lefèvre–Muller–Tisserand's
one-dimensional compressed-orbit algorithm.

The consolidated index is
[rotations/CONTINUED-FRACTIONS-CROSSWALK.md](rotations/CONTINUED-FRACTIONS-CROSSWALK.md):
it records this Step 5 interface as part of the K-H-L-A sixth
perspective, where continued-fraction convergents of `pi` are the
arithmetic scaffold for reading an effective constant rather than a
finished proof of that constant.

### Exact weighted lemma

Let

```text
J_max(n, R) = floor((2^R - 1) / n).
```

Then the shellized Erdős–Turán inequality from Step 1 and the exact
support statement from Step 3.5 give

```text
D_N
<= 6 * 2^(-R)
 + (2/pi) sum_{j=1}^{J_max(n, R)}
     (1/(j n) - 2^(-R)) lambda_j(n)
 + (4/pi) A_R N^(-1/2),
```

where

```text
A_R = H_{2^R - 1} - 1 + 2^(-R) = R ln 2 + O(1).
```

Indeed, under the hypothesis,

```text
D_N
<= 6 * 2^(-R)
 + (4/pi) sum_{h=1}^{2^R - 1} (1/h - 2^(-R)) |C_(X_n)(2 pi h)|
 + (4/pi) A_R N^(-1/2).
```

By Step 3.5, `C_(X_n)(2 pi h) = 0` unless `h = j n` for some `j >= 1`,
and at `h = j n`

```text
|C_(X_n)(2 pi j n)| = lambda_j(n) / 2.
```

Substituting this gives the displayed formula above. This is the exact
weighted bookkeeping identity.

### Dyadic-shell corollary

Since `1/(j n) - 2^(-R) <= 1/(j n)`, and on shell `2^r <= j < 2^(r+1)`
one has `1/j <= 2^(-r)`, the weighted term is bounded by

```text
(1/n) sum_{2^r <= j < 2^(r+1)} lambda_j(n) / j
<= (2^(-r) / n) L_r^(pair)(n).
```

Therefore

```text
D_N
<= 6 * 2^(-R)
 + (2/(pi n)) sum_{2^r <= J_max(n, R)} 2^(-r) L_r^(pair)(n)
 + (4/pi) A_R N^(-1/2).
```

This is the dyadic-shell form of the same lemma. It is weaker than the
exact weighted identity, but it is the version that interfaces directly
with the shell normalization from Steps 3–4.

### Fortnow-consolidated corollary

Substitute the Step 4 pullback inequality

```text
L_r^(pair)(n)
<= (3 c L_n^2 / (2 pi^2 n^2)) 2^n mu(code(n, r))
```

into the dyadic-shell form. One gets

```text
D_N
<= 6 * 2^(-R)
 + (3 c L_n^2 / (pi^3 n^3))
   sum_{2^r <= J_max(n, R)} 2^(n-r) mu(code(n, r))
 + (4/pi) A_R N^(-1/2).
```

Using `L_n <= 2 pi`, this implies the crude uniform bound

```text
D_N
<= 6 * 2^(-R)
 + (12 c / (pi n^3))
   sum_{2^r <= J_max(n, R)} 2^(n-r) mu(code(n, r))
 + (4/pi) A_R N^(-1/2).
```

### Constant sources

The constants now have an explicit provenance:

- `6` from the one-dimensional Erdős–Turán truncation term,
- `4/pi` from the harmonic side of Erdős–Turán,
- `A_R = H_{2^R-1} - 1 + 2^(-R) = R ln 2 + O(1)` from the shellized
  harmonic cost,
- `3/(2 pi^2)` from the direct paired-shell bound in Step 2,
- `c` from Fortnow Fact 6.2,
- the factor `1/2` converting `lambda_j(n)` into
  `|C_(X_n)(2 pi j n)| = lambda_j(n) / 2` from Step 3.5.

### What this does and does not prove

This closes Step 5 of the plan: the one-dimensional bookkeeping lemma is
now fully explicit.

What it proves:

- an exact weighted one-dimensional discrepancy bound under the
  empirical-to-density proxy,
- a dyadic-shell version aligned with the honest Aitchison shell,
- and a Fortnow-consolidated corollary with every constant sourced.

What it does **not** prove:

- any transcendence statement,
- any irrationality measure,
- or the empirical-to-density proxy itself.

Those belong to the parent KRAFT memo, not to this bookkeeping note.

---

## Status

The one-dimensional consolidation sequence is now closed:

- Step 1: exact dyadic partition at `m = 2^R - 1`, exact shellized
  Erdős–Turán inequality, exact shell cost `A_{R,r}`, and total harmonic
  cost `A_R = R ln 2 + O(1)`,
- Step 2: direct linear shell quantity `L_r^(pair)(n)` identified, with
  exact closed form for `lambda_j(n)` and direct shell bound
  `L_r^(pair)(n) <= (3 L_n^2 / (4 pi^2 n^2)) 2^(-r)`,
- Step 3: shell subprobability and encoded-pair semimeasure written down,
- Step 3.5: exact Aitchison-facing density `g_n` identified, with
  coefficients `C_(X_n)(+- 2 pi j n) = lambda_j(n) / 2` and honest shell
  `L_r^(pair)(n)`,
- Step 4: Fortnow applied to the exact paired-shell semimeasure, giving
  the pullback inequality
  `L_r^(pair)(n) <= (3 c L_n^2 / (2 pi^2 n^2)) 2^n mu(code(n, r))`,
- Step 5: exact weighted lemma, dyadic-shell corollary, and
  Fortnow-consolidated corollary all on the page under the stated
  empirical-to-density proxy.

The next live step is no longer one-dimensional bookkeeping. It is the
parent memo's next item: the L-W-safety audit on a drafted argument.
