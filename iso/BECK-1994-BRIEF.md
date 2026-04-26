# BECK-1994-BRIEF

Source-extraction memo on József Beck, "Probabilistic Diophantine
Approximation, I. Kronecker Sequences," *Annals of Mathematics* 140,
no. 2 (Sep. 1994), pp. 451–502
([sources/Beck-ProbabilisticDiophantineApproximation-1994.pdf](sources/Beck-ProbabilisticDiophantineApproximation-1994.pdf)).
JSTOR stable URL 2118607. (The PDF in `sources/` includes a one-page
prefatory note from Beck explaining that this is a reprint due to "a
great number of errors in the production" of the original July 1994
issue (Vol. 140, no. 1).)

**Why this brief exists.** Beck enters
[iso/DIDOS-PREROGATIVE.md](iso/DIDOS-PREROGATIVE.md)'s coordination
through the *gap-as-discrepancy* reading: the isoperimetric gap `Δ_n`
on inscribed regular `n`-gons admits a discrepancy interpretation
(the polygon's vertex sequence on `S¹` is `(k/n) mod 1` for
`k = 0, …, n−1`, a *finite-N* uniform-distribution problem; the
program's K-H-L-A discrepancy branch handles the related sequence
`(n α) mod 1`). Beck's register is *probabilistic Diophantine
approximation* — distinct from Osserman's and Fuglede's deterministic
isoperimetric register, but anchored on the same Fourier/Parseval
machinery that Hurwitz-side
[corners/HURWITZ-GAP.md](corners/HURWITZ-GAP.md) and the K-H-L-A
discrepancy branch
([memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md](memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md),
[memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md](memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md))
both already use.

**What was read.** Pages 1–14 (Introduction, §1 "Uniform distribution
in the unit interval," §2 "Uniform distribution in the unit torus,"
§3 "Poisson's summation formula," §4 "Local lemmas," §5 "Estimating
the tail," start of §6 "Cancellation of the main terms"); pages
49–54 (end of §9, references). The middle technical sections (§§5–9
on the second-moment method and box decomposition) were skimmed but
not read in detail — per the user's scoping instruction "scope to
what's program-relevant," the proof internals are out of scope. The
references list and explicit citations were read in full.

**Confidence level.** High on the precise statement and proof outline
of **Theorem 1** (the headline multidimensional Khintchine analog),
**Theorem 2** (sum of fractional-part products), and the continuous
version of Theorem 1. High on the per-author historical attributions
in §1 and §2, which are explicit in Beck's text. Medium on the
detailed step-by-step structure of the §3–§9 proof of Theorem 1 (not
re-derived here). High on the K-H-L-A program-side cross-reference,
since the program's existing memos cite the same Erdős-Turán /
Schmidt / Khintchine framework.

**Trust boundary up front.** This brief audits *what the paper says*
about discrepancy of multidimensional Kronecker sequences. It does
not claim Beck's tools transport directly to the program's specific
discrepancy target (the sequence `(n π) mod 1` at dyadic cutoffs);
where the hypothesis class fails to match, this is flagged.

---

## 1. Headline Theorems on Discrepancy of Kronecker Sequences

### 1.1 Setup

For `α = (α_1, …, α_k) ∈ R^k`, the **multidimensional discrepancy
function** is (Beck eq. 2.5)

```
Δ(α; N) = max_{1 ≤ m ≤ N}  |D(α, x; m)|
        = max  | Σ_{n=1..m} 1_{box}(n α mod 1) − m · vol(box) |.
```

Here `n α = (n α_1, …, n α_k) mod 1` and the box ranges over
`B = ∏_j [0, x_j] ⊂ [0,1]^k`. The 1-dim case `k = 1` reduces to the
classical `Δ(α; N) = max_{1 ≤ m ≤ N, 0 ≤ x ≤ 1} |Σ_{n=1..m} (1_{[0,x]}(nα) − x)|`.

A real `α` is **badly approximable** if its continued-fraction partial
quotients `a_n(α)` are uniformly bounded; equivalently, `||q α|| > c(α)/q`
for all `q ≥ 1` (eq. 1.14). For badly approximable α, `Δ(α; N) ≪ log N`
(the minimum possible discrepancy of any irrational `α`).

### 1.2 Theorem 1 — Multidimensional Borel-Cantelli for Discrepancy

**Statement** (Beck p. 458, eq. 2.10). For arbitrary positive
increasing function `φ(n)` of `n`, and for `k ≥ 2`,

```
Δ(α; N) ≪ (log N)^k · φ(log log N)   ⟺   Σ_{n=1}^∞ 1/φ(n) < ∞
```

for *almost every* `α ∈ R^k`.

**Hypothesis class.** Almost-every `α ∈ R^k`, `k ≥ 2`. Excludes
measure-zero sets (which include all specific algebraic and many
specific transcendental numbers individually — the theorem says
nothing about a *specific* `α`, only about the measure-1 generic
class).

**Conclusion.** A precise Borel-Cantelli convergence-divergence
criterion: the discrepancy growth rate is *exactly* `(log N)^k ·
log log N` up to log-log-of-log-log refinements. Specific examples
(eq. 2.11):

```
Δ(α; N) ≪ (log N)^k · (log_2 N) · (log_3 N) · ⋯ · (log_s N) · (log_{s+1} N)^{1+ε}
```

for almost every `α`, where `log_r` denotes iterated logarithm. The
last factor cannot be replaced by `log_{s+1} N` (without `ε`) — the
divergence side of Borel-Cantelli kicks in.

**This is the multidimensional analog of Khintchine 1923.** The 1-dim
case (Khintchine, eq. 1.17) gave

```
Δ(α; N) ≪ log N · φ(log log N)   ⟺   Σ 1/φ(n) < ∞
```

for almost every `α ∈ R`. Khintchine's proof used *continued
fractions* — the partial quotients `a_n(α)` characterize the discrepancy
in 1-dim (eq. 1.11 — Hardy-Littlewood, Ostrowski, Behnke, Hecke, Sós).
**No multi-dim continued-fraction analog is known**, which is why
Theorem 1 was a long-standing open problem.

### 1.3 Theorem 2 — Sum of Fractional-Part Products

**Statement** (Beck p. 460). For almost every `α = (α_1, …, α_k) ∈ R^k`,
the sum of products of fractional parts satisfies

```
| Σ_{N=1}^N { n α_1 } · { n α_2 } ⋯ { n α_k } − N · 2^{−k} |  ≪  (log N)^k · (log log N)^{1+ε}.
```

Each term has expected value `2^{−k}` (uniform distribution of `nα`
implies uniform distribution of products), and the sum is precisely
sandwiched between the corresponding Borel-Cantelli bounds.

**Hypothesis and proof technique.** Same as Theorem 1; Theorem 2 is
derived from Theorem 1 via the Koksma-Hlawka inequality applied to
`f(x_1, …, x_k) = x_1 ⋯ x_k`, which has bounded variation in the
sense of Hardy and Krause.

### 1.4 Continuous Version of Theorem 1

**Statement** (Beck p. 460, eq. 2.18). The `(k+1)`-dimensional line
`(α_1 t, α_2 t, …, α_k t)` for `0 ≤ t ≤ T`, `T → ∞`, is *very
uniformly distributed* in the `(k+1)`-dimensional unit torus: every
box `B` contains line segments of total length

```
T · vol(B) ± (log T)^k · (log log T)^{1+ε}.
```

This is the geodesic flow analog of Theorem 1 — replace the discrete
sequence `(n α)` by a continuous orbit.

### 1.5 Auxiliary precedents Beck cites and uses

**Khintchine 1923** [9] (eq. 1.13): for almost every `α ∈ R`,
`Δ(α; N) ≪ log N · (log log N)^{1+ε}`. Precise version (Khintchine
1924 [10], eq. 1.17): `Δ(α; N) ≪ log N · φ(log log N) ⟺ Σ 1/φ(n) < ∞`.
Proof via continued fractions.

**Schmidt 1964** [19] (eq. 2.8): for almost every `α ∈ R^k`,

```
Δ(α; N) ≪ (log N)^{k+1+ε}.
```

Proved via the Erdős-Turán-Koksma inequality. Schmidt notes this is
"the best possible result via the Erdős-Turán inequality" — the
extra `log N` factor is the inherent defect of the E-T-K inequality.
Beck's Theorem 1 *removes that defect* by using Poisson summation +
second-moment + Borel-Cantelli instead of E-T-K.

**Roth 1954** [17] (eq. 2.17): for *every* `α ∈ R^k` (not almost
every),

```
Δ(α; N) ≫ (log N)^{k/2}.
```

This is the universal lower bound on discrepancy of arbitrary
k-dimensional sequences (not just `nα` sequences). Beck note: "(2.17)
is exactly the square-root of the conjecture" `Δ(α; N) ≫ (log N)^k`.
**Important distinction:** this is Roth 1954 *Mathematika 1, 73–79
"On irregularities of distribution"* — the L²-Fourier discrepancy
lower bound, methodologically different from Roth 1955's transcendence
theorem on rational approximations to algebraic numbers.

**Erdős-Turán 1948** [6]: the original E-T inequality
`Δ(α; N) ≤ (1/(M+1)) + (3/N) Σ_{m=1}^M (1/m) |Σ_{n=1}^N e^{2πi m n α}|`,
giving the standard tool for converting Fourier/Weyl-sum bounds to
discrepancy bounds. K-N Theorem 2.5 (the program's reference at
[memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md](memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md))
is the standard textbook form. **Multi-dim Erdős-Turán-Koksma**:
K-N p. 116, also cited by the program.

### 1.6 What Beck first proves vs. extends

**Beck 1994 [present] first proves:**

- **Theorem 1** in `k ≥ 2`. The 1-dim case (k = 1) was Khintchine
  1923/1924. The multidim case was open since Khintchine: Schmidt
  1964 had `(log N)^{k+1+ε}` (one log too many); Beck removes the
  extra log.
- **Theorem 2** as a consequence of Theorem 1 + Koksma-Hlawka.
- **Continuous version of Theorem 1** (eq. 2.18) for the geodesic
  line on `T^{k+1}`.

**Methodological innovation.** "It is rather surprising that our
tools: Fourier analysis, the 'second moment method' and combinatorics,
are powerful enough to substitute the continued fractions in higher
dimensions" (p. 452). The continued-fraction tool is fundamentally
1-dimensional; Beck's substitution opens multi-dim discrepancy to
the same Fourier-theoretic methods the K-H-L-A program uses for
1-dim.

**Extends/sharpens from preceding authors:**

- Sharpens **Schmidt 1964** by `log N` (the precise gain attributable
  to using Poisson summation and second-moment instead of E-T-K).
- Extends **Khintchine 1923/1924** from `k = 1` to `k ≥ 2`.
- Strengthens **Sprindžuk** [21] on almost-pairwise independence in
  Borel-Cantelli (Beck cites Sprindžuk's *Metric Theory of Diophantine
  Approximations*, English transl. 1979).

### 1.7 Proof technique

The proof structure is mapped out in Beck §3–§9:

- **§3 Poisson summation:** rewrite the discrepancy `D(α, x; N)` as a
  Fourier sum (eq. 3.1) via the lattice `L(α)` generated by
  `(α_1, …, α_k, 1)` and its integer-shift companions.
- **§3 smoothing:** replace the discontinuous box-characteristic
  function by a "roof-like average" (eq. 3.10) using the Fejér
  kernel, yielding the absolutely-convergent series (eq. 3.12).
- **§4 Local lemmas:** four "almost-always" properties of `α ∈ R^k`
  (Lemmas 4.1–4.4) that hold for almost every `α` and serve as the
  Borel-Cantelli inputs.
- **§5 Tail estimate:** decompose the Fourier sum into "small terms"
  and "large terms"; the small-term tail is bounded using Lemma 4.4,
  the large-term contribution is estimated via Lemma 4.1 + Cauchy
  cancellation.
- **§6–§7 Main-term cancellation:** the "Key Lemma" of §7 supplies
  the second-moment cancellation that beats Schmidt's E-T-K bound by
  one logarithm.
- **§8 Smoothing parameter** `N²` can be replaced by `N^{1+ε}`.
- **§9 Proofs of the local lemmas** Lemmas 4.1–4.4. These use
  Khintchine's local criterion (eq. 4.7) and Schmidt's second-moment
  inequality (Beck eq. 9.71 = Schmidt 1960 [18] Theorem 2). The
  Schmidt 1960 input is itself a second-moment computation, *not* a
  transcendence-theoretic input.

**Inventory.** Fourier + Poisson summation + Fejér smoothing +
second-moment method + combinatorial box decomposition + Borel-Cantelli.
*Not* continued fractions, *not* Roth-Schmidt transcendence theory,
*not* integral geometry, *not* Lindemann-Weierstrass machinery.

---

## 2. Position Relative to the Program's Discrepancy Branch

### 2.1 What the program needs

From [memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md](memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md)
Step 5 and
[memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md) §(A6), the
program's live discrepancy targets are:

1. **The 1-dimensional sequence `(n π) mod 1`** (or equivalently `n α`
   for some specific algebraic number tied to the polygon side) at
   dyadic cutoffs `m = 2^R − 1`, with the empirical-to-density proxy
   bridging pointwise `n` discrepancy to averaged-over-range
   discrepancy.
2. **The Jacobi theta / Poisson test case** at OLD-TIME-RELIGION §(A6)
   — using Jacobi's theta-function transformation as a transcendence-
   free way to extract Poisson summation's content.
3. **An effective constant `C`** in the expected approximation
   `|q π − p| ≫ q^{−C}`, sourced through the Aitchison ×
   Erdős-Turán-Koksma × Kraft pairing.

The program is currently 1-dimensional (k = 1) and targets a *specific*
α (= π or polygon-related), not "almost every α."

### 2.2 What Beck supplies for this target

**Direct entry as upper bound: limited.** Theorem 1 is an
*almost-every* statement. The set of `α` for which the theorem fails
has measure zero; π is a single point of measure zero. Theorem 1
does not, by itself, certify that `Δ(π; N) ≪ log N · (log log N)^{1+ε}`
for the specific `α = π`. The program's K-H-L-A endgame requires
either:

- An external argument that π satisfies the type-1 hypothesis (so
  Khintchine-class bounds apply pointwise; this is what is *expected*
  but not *known* unconditionally — Roth 1955's transcendence
  theorem gives type 1 for *algebraic* numbers, but π is
  transcendental, and effective irrationality measure for π is
  exactly the unknown the program is trying to prove); or
- An averaged/empirical reading where the "almost every" statement
  applies to a generic perturbation around π — this is the
  empirical-to-density proxy in
  [memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md](memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md)
  Step 5.

**Direct entry as lower bound: also limited, but a candidate.** Roth
1954 [17] (eq. 2.17) gives `Δ(α; N) ≫ (log N)^{k/2}` for *every*
`α ∈ R^k`. In the 1-dim case (k = 1) this becomes
`Δ(α; N) ≫ √(log N)` — but this is **weaker** than the trivial
1-dim lower bound `Δ(α; N) ≫ log N` already implied by
Hardy-Littlewood (eq. 1.11) for any irrational α with bounded partial
quotients, and by Khintchine for almost-every α. So Roth 1954 in
k = 1 gives nothing the program doesn't already have. **Roth 1954
becomes useful only at `k ≥ 2`**, where the trivial lower bound is
absent.

**Methodological entry: substantial.** Beck's proof technique —
Poisson summation + Fejér smoothing + second-moment method + local
Borel-Cantelli lemmas — is methodologically *exactly* what the
K-H-L-A program does in 1-dim with Aitchison + Erdős-Turán-Koksma +
Kraft. Beck's paper is a worked example of the same recipe at higher
dimension. Three specific ingredients the program could borrow:

- **Smoothing via Fejér kernel** (Beck eq. 3.10–3.12): converts
  discontinuous box-counting functions to absolutely convergent
  Fourier sums. The K-H-L-A shellized E-T-K
  ([memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md](memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md))
  uses a similar discrete-shell decomposition; Beck's continuous
  Fejér smoothing is a refinement that may sharpen constants.
- **Second-moment / Borel-Cantelli substitution for continued
  fractions** (Beck p. 458): explicit demonstration that the
  *measure-theoretic* discrepancy bound can be obtained without
  continued-fraction input. The program is already 1-dim and uses
  continued fractions only auxiliarily; Beck's substitution affirms
  that a fully Fourier-side proof is achievable.
- **Local lemmas 4.1–4.4** as a template for "almost-every"
  preconditions on the irrational α. The program's empirical-to-
  density proxy needs an analogous lemma class — Beck's structure
  (statement of `(* )`-type hypotheses, then verification for
  almost every α) is a usable template.

Cross-register pairing: [rotations/3DT-BRIEF.md](rotations/3DT-BRIEF.md)
§"Lefèvre–Muller–Tisserand: The Algorithmic Lens" now supplies the
one-dimensional compressed-orbit precedent for the same K-H-L-A
empirical-to-density proxy. Beck remains the higher-dimensional
Fourier-substitute exemplar: useful as methodology, not as a pointwise
bound for `pi`. The central index for this role is
[rotations/CONTINUED-FRACTIONS-CROSSWALK.md](rotations/CONTINUED-FRACTIONS-CROSSWALK.md),
which logs Beck as the fifth perspective: a Fourier-side substitute
that preserves the Diophantine content continued fractions carry in
dimension one.

### 2.3 Where Beck's hypothesis class fails to match

Three mismatches:

1. **Almost-every vs. specific α.** Beck's headline theorems are
   measure-theoretic; the program targets a specific α (= π). The
   gap is bridged in K-H-L-A only by the empirical-to-density proxy
   or by an external transcendence input (which the program is
   trying to avoid).
2. **`k ≥ 2` vs. `k = 1`.** Theorem 1's novelty is the multidim case;
   in 1-dim the result was already Khintchine 1923. The program is
   currently 1-dim; Beck's main theorem is overkill for the 1-dim
   target, and the 1-dim version was already in the program's
   bibliography (K-N Ch. 2, Khintchine).
3. **Discrepancy of `(nα) mod 1` vs. polygon-vertex discrepancy.**
   The polygon-vertex sequence on `S¹` is `(k/n) mod 1` for
   `k = 0, …, n−1` — a rational sequence with discrepancy `≤ 1/n`
   exactly (the polygon vertices are equispaced; their discrepancy
   is *minimal*, not "of size log N"). This is the wrong target for
   Beck's bounds. The relevant K-H-L-A target is the *irrational*
   sequence `(n π) mod 1` (or analogous).

### 2.4 Pre-L-W audit

**Calendar:** Beck 1994 is post-1882 by 112 years. All cited
predecessors with substantive content (Khintchine 1923, Erdős-Turán
1948, Roth 1954, Schmidt 1960/64, Sprindžuk, Hardy-Littlewood 1922)
are also post-1882. Bernstein 1909 (probabilities, the
Borel-Cantelli prehistory) is post-1882 by 27 years.

**Content:** The audit criterion per
[memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md) is *content*,
not *calendar*. Beck's main proof uses:

- **Poisson summation formula** — Poisson 1827, well pre-1882.
- **Fejér kernel smoothing** — Fejér 1900, post-1882 by 18 years
  but methodologically classical Fourier (no transcendence input;
  the kernel is `(sin x / x)²`-type, elementary).
- **Second-moment method** — Borel-Cantelli + Cauchy-Schwarz; both
  pre-1882-content (Cauchy 1821, Borel/Cantelli around 1909 but
  re-derivable from elementary measure theory which itself is
  pre-/around-1882).
- **Combinatorial box decomposition** — pure combinatorics,
  no transcendence content.
- **Schmidt 1960** [18] (Beck's Lemma 4.2 input): a metrical theorem
  in Diophantine approximation, methodologically L²-Fourier.
- **Roth 1954** [17] (Beck eq. 2.17 lower bound): "On irregularities
  of distribution" — this is the *discrepancy* Roth, methodologically
  L²-Fourier and combinatorial. **Distinct from Roth 1955's
  transcendence theorem on rational approximations to algebraic
  numbers**, which uses Roth-Schmidt machinery and is the
  problematic post-L-W input. Roth 1954 has no transcendence
  content.

**Verdict.** Beck 1994's content is *plausibly L-W-safe* even though
calendar-late: the Fourier + second-moment + Borel-Cantelli machinery
admits transcendence-free re-derivation, and the only "Roth" input
is the 1954 discrepancy paper, not the 1955 transcendence theorem.
The program's audit criterion (content over calendar) admits Beck's
theorems as L-W-safe candidates *modulo* re-rendering each step in
explicitly transcendence-free language. The Schmidt 1960 second-
moment lemma is the one piece that should be checked carefully —
Beck cites it as an off-the-shelf input (eq. 9.71), and certifying
it L-W-safely would require its own brief.

### 2.5 What Beck does *not* supply

For the program's 1-dim K-H-L-A endgame:

- A pointwise discrepancy bound for `(n π) mod 1` (Beck is
  almost-every, not pointwise).
- An effective constant `C` in `|q π − p| ≫ q^{−C}` (Beck's almost-
  every bounds give no effective constant for any specific α).
- A transcendence proof or transcendence-measure refinement (Beck
  is metrical / probabilistic, not transcendence-theoretic).
- Direct connection to the Hurwitz isoperimetric gap or polygon
  vertex sequence (Beck targets `(nα) mod 1`, not `(k/n) mod 1`).

---

## 3. Trust Boundary

### This brief should be cited for

- The precise statement of **Theorem 1** (Beck p. 458, eq. 2.10):
  multidimensional Khintchine analog,
  `Δ(α; N) ≪ (log N)^k · φ(log log N) ⟺ Σ 1/φ(n) < ∞`, almost every
  `α ∈ R^k`, `k ≥ 2`.
- The precise statement of **Theorem 2** (p. 460): sum of fractional-
  part products with bound `(log N)^k · (log log N)^{1+ε}`.
- The continuous version of Theorem 1 (eq. 2.18, geodesic flow on
  `T^{k+1}`).
- The methodological inventory: Fourier + Poisson + Fejér smoothing
  + second-moment + Borel-Cantelli + combinatorial box decomposition.
- The historical chain: Khintchine 1923 (1-dim), Schmidt 1964
  ((log N)^{k+1+ε} via E-T-K), Beck 1994 (sharpens by one log via
  second-moment).
- The distinction between **Roth 1954 [17] "On irregularities of
  distribution"** (used by Beck, methodologically L²-Fourier
  discrepancy lower bound) and Roth 1955's transcendence theorem
  (NOT used by Beck; problematic for L-W-safety).
- The methodological substitution claim (p. 452): Fourier + second-
  moment + Borel-Cantelli "substitute the continued fractions" in
  multi-dim discrepancy proofs.
- The list of input theorems Beck relies on as off-the-shelf:
  Khintchine local criterion (eq. 4.7), Schmidt 1960 [18] second-
  moment inequality (eq. 9.71), Borel-Bernstein theorem (eq. 1.18).

### This brief should NOT be cited for

- A pointwise discrepancy bound on `Δ(π; N)` (Beck is almost-every,
  not pointwise).
- An effective constant for `|q π − p|` (Beck's almost-every bounds
  give no effective specific-α constant).
- A transcendence proof of π (Beck is metrical, not transcendence-
  theoretic).
- Direct upper or lower bounds on the polygon-vertex discrepancy
  `(k/n) mod 1` (rational sequence; not Beck's target).
- The full proof of Theorem 1 (only the proof outline is in this
  brief; the technical core in §§5–9 was skimmed, not extracted).
- Schmidt 1960's second-moment inequality details (Beck cites this
  as an input; it requires its own brief if program use is intended).
- Anything about K-H-L-A's empirical-to-density proxy beyond the
  observation that Beck's local-lemma structure is a methodological
  template; the proxy itself is program-internal.

### Provenance tag for the program

**Methodologically post-1965 measure-theoretic Diophantine
approximation paper of post-1882 origin.** Beck 1994 is calendar-
post-1882; its main proof technique (Poisson summation, Fejér
smoothing, second-moment method, Borel-Cantelli) is *plausibly L-W-
safe in content* — re-rendering each step in transcendence-free
language is a candidate audit task per
[memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md). The Roth
input is Roth 1954 (discrepancy), not Roth 1955 (transcendence) —
this distinction matters for L-W-safety. The Schmidt 1960
second-moment input (Beck Lemma 9.71) is the cleanest single point
that would need its own L-W-safety brief if program use of Beck's
machinery becomes load-bearing.

---

## Closing Sentence

This brief contributes the precise statement of Beck 1994's
multidimensional Khintchine analog (Theorem 1: `Δ(α; N) ≪ (log N)^k
· φ(log log N) ⟺ Σ 1/φ(n) < ∞`, almost every `α ∈ R^k`, `k ≥ 2`),
plus Theorem 2 and the continuous version. It records the
methodological substitution Beck demonstrates — Fourier + Poisson +
second-moment + Borel-Cantelli replacing continued fractions in
higher-dimensional discrepancy proofs — and flags the L-W-safety
audit status: calendar-post-1882, content-plausibly-safe, with the
key clarification that Beck's Roth input is the 1954 discrepancy
paper, not the 1955 transcendence theorem. For the program's K-H-L-A
discrepancy branch
([memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md](memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md),
[memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md](memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md))
the contribution is **methodological exemplar, not direct
upper/lower bound**: Beck's almost-every statements do not certify
pointwise discrepancy of `(n π) mod 1`, and his multi-dim setting
overshoots the program's current 1-dim target. The program's
empirical-to-density proxy and Beck's local-lemma structure are
analogous bridges from "almost-every" to "specific α" in their
respective registers; cross-pollination is plausible but requires
program-internal re-derivation. This brief is the discrepancy-side
companion to
[iso/OSSERMAN-1979-BRIEF.md](iso/OSSERMAN-1979-BRIEF.md) (Bonnesen
geometric route) and
[iso/FUGLEDE-1989-BRIEF.md](iso/FUGLEDE-1989-BRIEF.md) (Sobolev
stability route) for
[iso/DIDOS-PREROGATIVE.md](iso/DIDOS-PREROGATIVE.md): Osserman covers
the geometric stability of the isoperimetric extremum, Fuglede covers
its Sobolev stability, and Beck covers the Diophantine *probabilistic*
register that the program's K-H-L-A discrepancy branch shares.
