# KRAFT-CONSTANT-CONSOLIDATION-PLAN

Advance plan for the next live step in
[memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md](memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md):
consolidate the already-closed local Fourier shell theorem with the
one-dimensional Erdős–Turán discrepancy bound, Aitchison's density-side
Fourier estimate, and Fortnow's universal-dominance constant into one
correctly normalized budget.

This is deliberately narrower than the full KRAFT memo. No transcendence
claim, no irrationality-measure claim, no `k > 1` generality, and no
program-level synthesis beyond what is needed to produce a single explicit
constant lemma.

The point of the plan is brutal locality: one dimension, one shell
decomposition, one bridge quantity, one final bookkeeping inequality.

---

## What this plan is for

The local Fourier side is now closed at
[corners/HURWITZ-FIRST-BAND-CONCENTRATION.md](corners/HURWITZ-FIRST-BAND-CONCENTRATION.md):

- explicit coefficient lattice,
- paired-band closed form,
- first-band concentration,
- dyadic-shell estimate.

What remains is not more local harmonic analysis. What remains is to align
three different normalizations:

- Hurwitz gives a **quadratic** Fourier budget on the polygon side,
- Erdős–Turán gives a **linear harmonic** discrepancy budget on the orbit side,
- Aitchison gives a **linear absolute-value** density budget on the
  characteristic-function side.

This plan exists to align those three without hidden losses or hidden
hypotheses.

---

## Target deliverable

A single theorem-shaped lemma, specialized to `k = 1`, of the form

```text
D_N <= K_0 [ 2^(-R) + shell_Fourier_term(R) + R * N^(-1/2) ]
```

or an equivalent one-dimensional variant with the same ingredients:

- one truncation term from Erdős–Turán (size `~ 1/m = 2^(-R) / (1 - 2^(-R))`),
- one shell-summed Fourier term (sum over `r = 0, ..., R-1` of a
  per-shell linear Fourier quantity),
- one sampling-noise term (harmonic sum `~ R ln 2` times the per-term
  sampling error `N^(-1/2)`),
- one explicit front constant `K_0`.

The exact shape may move slightly during derivation, but the deliverable
must satisfy three constraints:

1. Every constant is explicitly sourced.
2. The shell term is stated in the same shell language as
   [corners/HURWITZ-FIRST-BAND-CONCENTRATION.md](corners/HURWITZ-FIRST-BAND-CONCENTRATION.md).
3. No step appeals to transcendence or Diophantine type.

This plan succeeds if it closes that one lemma cleanly.

---

## Scope restrictions

Keep the proof inside the following fence:

- `k = 1` only.
- Dyadic cutoff `m = 2^R - 1` only (chosen just below a power of two so
  shells tile exactly; see Input 1).
- Shell index `r` (running `0, ..., R-1`) only.
- One-dimensional Erdős–Turán only, unless the `k = 1` proof literally
  forces the Koksma form.
- No irrationality measure.
- No algebraic-vs-transcendental discrimination claim.
- No attempt to move from the budget lemma to the auxiliary-free
  contradiction.

Anything outside this fence belongs to the parent KRAFT memo, not to this
plan.

---

## Exact local inputs

### Input 1. One-dimensional Erdős–Turán

Use the `k = 1` form already quoted in
[memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md](memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md):

```text
D_N <= 6/(m+1) + (4/pi) sum_{h=1}^m (1/h - 1/(m+1)) |S_N(h)|.
```

Fix the dyadic cutoff `m = 2^R - 1` (choosing `m` just below a power of
two so the shells tile cleanly). Then

```text
sum_{h=1}^{2^R - 1} (1/h) |S_N(h)|
= sum_{r=0}^{R-1} sum_{2^r <= h < 2^(r+1)} (1/h) |S_N(h)|,
```

and the `R` shells partition `{1, 2, ..., 2^R - 1}` exactly (shell `r`
has `2^r` elements). Per-shell harmonic cost:

```text
sum_{2^r <= h < 2^(r+1)} 1/h  =  ln 2 + O(2^(-r))  in (ln 2, 1],
```

i.e. `O(1)` per shell with limiting value `ln 2 ~= 0.693`, not
logarithmic inside each shell. The total harmonic sum is therefore
`~ R * ln 2 = log_2(m+1) * ln 2`.

### Input 2. Aitchison

Use only the one-dimensional density estimate:

```text
d(g, u) <= sum_{s != 0} |C_X(2 pi s)|.
```

(Here `s` is Aitchison's Fourier index, renamed from the source's `r`
to avoid collision with the shell index `r` used throughout this plan.
The sum runs over nonzero integers `s`; `C_X` is the characteristic
function of the sampling density `X`.)

Do not generalize. The task is to identify exactly how the shellized
Erdős–Turán terms are supposed to pair with this absolute-value Fourier
budget. The natural pairing interprets `|S_N(h)|` as a sampled proxy
for `|C_X(2 pi h)|`, incurring a `N^(-1/2)` sampling cost per
evaluation.

### Input 3. Local Hurwitz shell theorem

Use the already-closed shell estimate from
[corners/HURWITZ-FIRST-BAND-CONCENTRATION.md](corners/HURWITZ-FIRST-BAND-CONCENTRATION.md):

```text
sum_{2^r <= j < 2^(r+1)} B_j(n) <= 2^(-r) B_1(n).
```

This is the local Kraft-shaped input. The consolidation problem is to
decide how this shell budget should be translated into the linear shell
budget needed by Erdős–Turán and Aitchison.

### Input 4. Fortnow universal dominance

Use only Fact 6.2 as quoted in
[memos/FORTNOW-KOLMOGOROV-BRIEF.md](memos/FORTNOW-KOLMOGOROV-BRIEF.md):
if `tau` is semicomputable with total mass at most `1`, then

```text
tau(x) <= c mu(x).
```

In this plan, Fortnow enters only after a precise shell-weight object
`tau_r` has been defined. Do not invoke the universal constant before the
subprobability is actually on the page.

---

## Main choice to resolve

The decisive technical choice is the bridge quantity.

Hurwitz gives quadratic mass `B_j(n)`. Erdős–Turán and Aitchison want
linear absolute values. There are two possible routes:

1. **Direct route.**
   Go back to the explicit coefficient formula

   ```text
   c_(1 + j n)^(n) = L_n^2 / (4 pi^2 (1 + j n)^2)
   ```

   and derive a shell estimate directly for

   ```text
   sum |c_(1 + j n)^(n)|
   ```

   or whichever linear shell quantity is actually needed.

2. **Cauchy–Schwarz route.**
   Pass from `B_j(n)` to a linear shell estimate by inequality.

Preferred route: direct. The coefficients are explicit, and the direct
route avoids an unnecessary square-root loss.

The plan should be considered stalled if it slides into the second route
without first ruling out the direct one.

---

## Proof sequence

### Step 1. Shellize Erdős–Turán cleanly

Fix `m = 2^R - 1` and rewrite the one-dimensional Erdős–Turán sum as a
sum over shells `2^r <= h < 2^(r+1)` for `r = 0, ..., R-1`.

Deliverable:

- one displayed shellized E–T inequality,
- one sentence stating exactly what the cost of one shell is,
- no asymptotic shorthand beyond what is justified in-line.

The point of this step is to make the outer bookkeeping object visible
before any Fourier substitution happens.

### Step 2. Identify the linear shell quantity

Using the explicit coefficient formula, write down the shell quantity that
naturally interfaces with the shellized E–T sum and Aitchison's absolute
characteristic-function bound.

The target is something of the form

```text
L_r(n) = sum_{2^r <= j < 2^(r+1)} linear_Fourier_mass(j,n).
```

This step must answer:

- what exactly `linear_Fourier_mass` is,
- why it is the right quantity for both E–T and Aitchison,
- how it is related to the already-closed `B_j(n)` shell theorem.

Deliverable:

- one definition of `L_r(n)`,
- one direct shell estimate on `L_r(n)`,
- one note explaining whether `B_j(n)` is being used directly or only as
  corroboration.

### Step 3. Normalize a shell subprobability

Define a shell-weight object `tau_r` whose total mass is at most `1`.
This is the point where the phrase "Kraft-shaped" stops being metaphorical
and becomes a literal summable budget.

The shell weights should be chosen so that:

- the total mass is explicit,
- semicomputability is visible,
- the front constant needed for Fortnow can be read off honestly.

Deliverable:

- one explicit definition of `tau_r`,
- one proof that `sum_r tau_r <= 1` or another fixed explicit constant,
- one sentence stating whether `tau_r` is already normalized or must be
  rescaled before Fortnow applies.

### Step 4. Insert Fortnow only after normalization

Apply Fact 6.2 only once the shell budget is genuinely a semicomputable
subprobability.

Deliverable:

- one line of the form `tau_r <= c mu(r)` or its exact local variant,
- one sentence naming the constant source and what object it dominates.

If the shell weights are not semicomputable in the needed sense, stop and
record that failure explicitly. Do not smooth over it.

### Step 5. Produce the final bookkeeping lemma

Assemble:

- the shellized E–T truncation term,
- the linear shell Fourier term,
- the sampling-noise term,
- the Fortnow dominance constant.

The goal is a single inequality with one front constant `K_0`.

Deliverable:

- one explicit final lemma,
- one list of the constants entering `K_0`,
- one sentence saying exactly what the lemma does and does not prove.

That sentence matters. The lemma is a budget consolidation, not yet a
transcendence argument.

---

## Failure modes to watch

1. **Quadratic-linear mismatch.**
   If the argument only works by taking square roots of shell masses and
   destroys the shell geometry, the direct route failed and the loss has to
   be named.

2. **Density-orbit slippage.**
   Erdős–Turán is empirical-orbit language; Aitchison is density language.
   The interface has to be stated, not implied.

3. **Premature Fortnow invocation.**
   Universal dominance is not a magic front constant. It only applies after
   an actual semicomputable subprobability has been defined.

4. **Silent return of `k > 1`.**
   If a derivation starts importing the multi-dimensional form merely
   because it looks more elegant, the plan has drifted off scope.

5. **Transcendence creep.**
   Any appeal to irrationality type, Liouville, Baker, Roth, or a
   contradiction with algebraicity belongs later, not here.

---

## What not to do

- Do not mention `pi`-irrationality measures in the proof itself.
- Do not treat the shell estimate as if it already yields a coding theorem.
- Do not hide constants under `O(1)` if the whole point is to consolidate
  constants.
- Do not promote the resulting lemma into a contradiction argument in the
  same note.

This plan is successful if it closes a one-dimensional constant lemma and
nothing more.

---

## Promotion target

If the lemma closes cleanly, it should promote in two places:

- back into
  [memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md](memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md)
  as the closed version of item 4 in §"Proposed order of work", and
- outward into a short companion memo, likely
  `memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md`, if the bookkeeping statement
  becomes stable enough to cite independently.

If the direct route fails but the failure is precise, that is still a real
finding. In that case the plan promotes a negative note: the local Hurwitz
shell theorem does not linearize into the needed E–T/Aitchison budget
without loss, and the next attempt has to name the loss explicitly.
