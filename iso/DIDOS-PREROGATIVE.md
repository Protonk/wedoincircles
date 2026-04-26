# DIDOS-PREROGATIVE

*Search memo. Coordination point for isoperimetric source-extraction
briefs in the program; provisional, append-only during active life.*

**The matter, in its older form.** Among plane figures of fixed
perimeter `L`, the one of greatest area `A` is the circle, with
`4 pi A <= L^2`, equality only for the circle. Stated this way the
inequality predates Jordan curves, predates rectifiability, predates
measure theory — it lives in the Greek geometric register of
Zenodorus (c. 200 BCE), with Virgil giving the named case: Queen
Dido's oxhide cut into thin strips and laid out against the Carthaginian
coast to enclose the maximum land. The polygonal sub-statement is
equally pre-modern: among `n`-gons of fixed perimeter the regular
`n`-gon has the greatest area, and the regular `n`-gon's gap to the
optimal disk closes as `n -> infinity`. Both statements live entirely
inside elementary geometry; no analytic completion is required to ask
them or to verify them on examples. *Dido's prerogative* is the right
to that maximum — and the program inherits the question in exactly her
form, not in the Jordan-curve completion that came eighteen centuries
later.

**Sensitizing concepts.** The quantity that carries the question into
computation is the **isoperimetric gap** `Delta = L^2 - 4 pi A`, zero
exactly at the circle. Five concepts orient briefs in this area: (i)
**Bonnesen-style strengthening** — `Delta >= pi^2 (R - r)^2`
(Bonnesen 1921) with `R, r` the circumscribed and inscribed radii, a
geometric lower bound on the gap; the separate `Delta >= 4 pi d^2`
form (Bonnesen 1924, with `d` the minimum annulus width) is a
companion strengthening; (ii) **Hurwitz's 1902 identity** — for a
curve in arclength parametrization, `Delta = 4 pi^2 Sigma m(m-1) |c_m|^2`
over Fourier coefficients, putting the gap into Parseval form;
(iii) **stability** — Fuglede 1989 and successors quantify how
`Delta -> 0` forces the figure toward the disk in stronger metrics
than just gap-vanishing; (iv) **Steiner symmetrization** as the
canonical proof technique, well-defined on polygons without analytic
machinery; (v) **regular-polygon sequences** — `Delta_n` for the
inscribed regular `n`-gon goes to zero like `1/n^2`, with Archimedean
leading term `4 pi^4 / (3 n^2)`. Each is computable on a polygon by
hand, which keeps the topic squarely inside the program's pre-1882
audit window.

**Where the repo already cares.** Multiple anchor points lean on
isoperimetry already.
[corners/HURWITZ-GAP.md](corners/HURWITZ-GAP.md) computes `Delta_n`
three ways for the inscribed regular `n`-gon and uses the Parseval
rendering as the load-bearing closure check;
[memos/STRIP-H1-HURWITZ-CLOSURE.md](memos/STRIP-H1-HURWITZ-CLOSURE.md)
routes the gap through the strip-side `H^1` seminorm;
[memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md](memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md)
and
[memos/COUNTING-APPARATUS.md](memos/COUNTING-APPARATUS.md) treat the
gap as one of several small-quantity candidates for the L-W-safety
endgame;
[memos/ARCHIMEDEAN-SIGNATURE.md](memos/ARCHIMEDEAN-SIGNATURE.md) and
[memos/STRIP-TISSUE-FOURIER.md](memos/STRIP-TISSUE-FOURIER.md) read
the gap as one face of the larger Archimedean signature on `1/n^2`.
Source PDFs in scope:
[sources/Osserman-BonnesenStyleIsoperimetricInequalities-1979.pdf](sources/Osserman-BonnesenStyleIsoperimetricInequalities-1979.pdf)
(Bonnesen-style strengthenings, modern survey — briefed at
[iso/OSSERMAN-1979-BRIEF.md](iso/OSSERMAN-1979-BRIEF.md));
[sources/Fuglede-StabilityIsoperimetricProblem-1989.pdf](sources/Fuglede-StabilityIsoperimetricProblem-1989.pdf)
(quantitative stability — not yet briefed); and
[sources/Beck-ProbabilisticDiophantineApproximation-1994.pdf](sources/Beck-ProbabilisticDiophantineApproximation-1994.pdf)
(probabilistic Diophantine approximation — briefed at
[iso/BECK-1994-BRIEF.md](iso/BECK-1994-BRIEF.md); enters DIDOS through
the K-H-L-A empirical-to-density discrepancy proxy, not as a direct
isoperimetric theorem).
Each requires an INHERIT-discipline extraction brief with the
L-W-safety audit
([memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md)) declaring
which steps sit on pre-1882 substrate (Zenodorus's polygonal extremal
cases, Steiner symmetrization in Steiner's hand — qualitative
isoperimetric statements only) versus on post-L-W machinery (Bernstein
1905 onward; the quantitative Bonnesen-style strengthenings are all
post-1882 and require their own audit, may be admissible only as
setup). This memo is the coordination point for those briefs.

## Three-thread chain (skeleton for a future historiographical brief)

The literature DIDOS coordinates does not converge to a single origin
the way the FFT chain converges to Gauss 1805. Three threads run
through it, with different origin dates and different convergence
patterns. A future historiographical brief — the iso/ analog of
[fft/HEIDEMAN-JOHNSON-BURRUS-1985-BRIEF.md](fft/HEIDEMAN-JOHNSON-BURRUS-1985-BRIEF.md)
— would unfold these threads as historiography. This section is the
skeleton.

**Thread 1 — Geometric / Bonnesen-style.**
- Pre-1882 substrate: Zenodorus c. 200 BCE (qualitative isoperimetric
  inequality, polygonal extremal cases); Steiner ~1830s
  (symmetrization technique, qualitative). Both pre-L-W.
- First quantitative Bonnesen-style: Bernstein 1905 (sphere → plane
  limit; constant `≈ 1700`, weak).
- Sharp constants: Bonnesen 1921 (`(R − ρ)²` form, constant `π²`);
  Bonnesen 1924 (annulus-width form `Δ ≥ 4π · d²`, constant `4π`
  provably best).
- Convex-only → non-convex extensions: Schmidt 1939 (analytic),
  Fiala 1941 (interior parallels), Hadwiger 1941 (integral
  geometry); Fejes-Tóth 1950 (polygonal direct, drops integral
  geometry).
- Modern survey: Osserman 1979
  ([iso/OSSERMAN-1979-BRIEF.md](iso/OSSERMAN-1979-BRIEF.md)).
- Convergence point: Bonnesen 1924 sharp `Δ ≥ 4π · d²`.

**Thread 2 — Sobolev / Hurwitz-Fourier.**
- Pre-1882 substrate: Fourier 1822 (trigonometric series machinery).
- First quantitative Sobolev: Hurwitz 1902 (Parseval identity
  `Δ_H = 4π² Σ m(m−1)|c_m|²` for arclength-parametrized curves).
  Calendar-post-1882 by 20 years; transcendence-free in content.
- L² + H¹ stability for nearly-spherical: Fuglede 1986
  (n_dim = 3 case of Theorem 1.2 (I.a)).
- All-dimensions with explicit constants: Fuglede 1989
  ([iso/FUGLEDE-1989-BRIEF.md](iso/FUGLEDE-1989-BRIEF.md), Theorem
  1.2 for all `n_dim ≥ 2`).
- Convergence point: Sobolev L² + H¹ stability of nearly-spherical
  domains; for inscribed regular n-gon, sharp rate `Θ(1/n²)`.

**Thread 3 — Probabilistic / Diophantine.**
- Pre-1882 substrate: Poisson 1827 (summation formula); classical
  Fourier from thread 2.
- First quantitative metric: Khintchine 1923/1924 (1-dim Borel-Cantelli
  for `Δ((nα) mod 1; N)`); proof via continued fractions.
- Multi-dim via Erdős-Turán-Koksma: Schmidt 1964 (`(log N)^{k+1+ε}`,
  one log over conjecture).
- Universal lower bound: **Roth 1954** "On irregularities of
  distribution," `Δ(α; N) ≫ (log N)^{k/2}` for *every* `α ∈ R^k`.
  Methodologically L²-Fourier discrepancy — *not* Roth 1955's
  transcendence theorem on rational approximations to algebraic
  numbers.
- Multi-dim Khintchine analog: Beck 1994
  ([iso/BECK-1994-BRIEF.md](iso/BECK-1994-BRIEF.md), Theorem 1);
  Fourier + Poisson + second-moment + Borel-Cantelli substituting
  for continued fractions.
- Convergence point: `(log N)^k · φ(log log N)` Borel-Cantelli
  threshold for almost every `α`.

**Documented gaps and continuities.**
- *Continuity, thread 2:* Hurwitz 1902 → Fuglede 1986 explicit, via
  Fuglede 1989 footnote 1 ("Still another proof — quite short — can
  be read off from Hurwitz' Fourier series proof"). Same Hilbert
  space, same Parseval identity, four decades apart.
- *Disambiguation, thread 3:* Roth 1954 [Mathematika 1, 73–79,
  "On irregularities of distribution"] vs. Roth 1955 [Mathematika 2,
  1–20, "Rational approximations to algebraic numbers"]. Same author,
  adjacent year, distinct papers, distinct registers. The 1954
  paper is the discrepancy lower bound used by Beck; the 1955 paper
  is the transcendence theorem the program audits as
  post-Lindemann-Weierstrass.
- *Pre-1882 substrate sufficiency:* qualitative isoperimetric
  inequality (thread 1, Zenodorus + Steiner) is fully pre-L-W.
  *Quantitative* content in all three threads is post-1882: even
  Hurwitz 1902 and Bonnesen 1921 sit on the post-L-W side of the
  audit calendar. Content audit (per
  [memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md)) finds
  all three threads transcendence-free in content despite
  calendar-post-1882 dating.
- *Cross-thread convergence:* threads 1 and 2 both target the
  inscribed regular n-gon and converge on the same Δ_n via
  Hurwitz Parseval (sharp on rate) vs. Bonnesen `(R − ρ)²` (sharp
  on constant). Thread 3 targets the *adjacent* sequence
  `(n π) mod 1`, not the polygon vertices `(k/n) mod 1` (which are
  rational, discrepancy `1/n` exactly). The three threads do not
  share a single test object.

A historiographical brief unfolding these threads would document the
chain at the level of detail HJB-1985 documents the Gauss → Cooley-
Tukey chain — primary-source quotes, transmission events,
attribution corrections, calendar vs. content audit. The skeleton
above is what such a brief would be expanding on.

## Brief findings (append-only)

### From [iso/OSSERMAN-1979-BRIEF.md](iso/OSSERMAN-1979-BRIEF.md)

- **Date and constant correction.** The headline `(R - r)^2`
  strengthening is Bonnesen **1921** with constant **`pi^2`**, not
  Bonnesen 1924 with constant `pi` (as DIDOS-PREROGATIVE originally
  cited; corrected above). Bonnesen 1924 supplies the separate
  `Delta >= 4 pi d^2` form (`d` = minimum annulus width; `4 pi`
  provably best possible). Both appear in Osserman.

- **Earliest Bonnesen-style attribution.** The first Bonnesen-style
  inequality is **Bernstein 1905** (Osserman ref [15]), proven on
  the sphere with the plane case as a limit; constant strictly
  weaker than Bonnesen's.

- **Audit window.** All quantitative Bonnesen-style strengthenings
  Osserman covers are post-1882. Pre-1882 substrate (Zenodorus,
  Steiner-in-Steiner's-hand) carries only qualitative isoperimetric
  and symmetrization statements, not the quantitative `Delta`-floor
  strengthenings. Osserman's main-text proof uses Fejes-Tóth 1950
  polygonal exterior-parallel-curve method + convex hull +
  rectifiable approximation; that proof is a candidate for L-W-safety
  certification but is not certified by Osserman.

- **Specialization to regular `n`-gons.** Osserman does not specialize
  to regular `n`-gons, but the inequalities apply. Specializing
  `Delta >= pi^2 (R - r)^2` to inscribed regular `n`-gons:
  `R - r = 1 - cos(pi/n) = pi^2 / (2 n^2) + O(1/n^4)`, giving
  `Delta_n >= pi^6 / (4 n^4) + O(1/n^6)` — an **`O(1/n^4)`** floor.
  The actual leading term per
  [corners/HURWITZ-GAP.md](corners/HURWITZ-GAP.md) is
  `Delta_n = 4 pi^4 / (3 n^2) + O(1/n^4)` — **`O(1/n^2)`**. The
  Bonnesen-style geometric route is **two orders of `n` weaker**
  than the Hurwitz Fourier route on the regular-`n`-gon test case.
  None of the Bonnesen forms in Osserman recovers the actual rate.

- **Methodological independence.** Hurwitz 1902 is not in Osserman's
  references [1]–[77]; Fourier/Parseval methods are absent from the
  survey. The Bonnesen geometric route and the Hurwitz Fourier route
  are **methodologically independent** — complementary, not
  interconvertible.

### From [iso/FUGLEDE-1989-BRIEF.md](iso/FUGLEDE-1989-BRIEF.md)

- **Main theorems.** Theorem 1.2 (nearly-spherical, all `n >= 2`):
  two-sided Sobolev bound on `Delta` with explicit constants —
  `(1/10)(||u||^2 + ||grad u||^2) <= Delta <= (3/5) ||grad u||^2`,
  improvable to `(0.24, 0.54)` for `n = 2`. Theorem 2.3 (convex body,
  `n >= 3`): Hausdorff `d <= C (Delta log(1/Delta))^(1/2)` for `n = 3`
  with `C = 4.56`, `d <= C Delta^(2/(n+1))` for `n >= 4`. The `n = 2`
  case of Theorem 2.3 is Bonnesen 1924, included for comparison
  (Fuglede footnote 4).

- **Per-author attribution.** Bonnesen 1924 (n=2 of Theorem 2.3);
  Bernstein 1905 (precursor, weaker constant); Fuglede 1986 (n=3 of
  Theorem 1.2 (I.a)); Osserman 1987 (related `(r - rho) / rho` bound,
  quantitatively weaker per Fuglede §2.7); Fuglede 1989 [present] is
  the all-`n >= 2` extension with explicit constants and sharpness
  examples.

- **Hurwitz 1902 ancestry confirmed.** Fuglede's footnote 1 explicitly
  traces the `n = 2` ancestry of Theorem 1.2 (I.a) to Hurwitz 1902
  via Fuglede 1986. The strip-`H^1` identification in
  [memos/STRIP-H1-HURWITZ-CLOSURE.md](memos/STRIP-H1-HURWITZ-CLOSURE.md)
  is structurally identical content. The program's strip-`H^1`
  closure check now has explicit literature provenance.

- **Specialization to regular n-gons.** Conversion: `Delta_F,n =
  Delta_H,n / (8 pi^2) = pi^2 / (6 n^2)`. H¹ Sobolev bound: `||u||^2 +
  ||grad u||^2 <= 10 Delta = Theta(1/n^2)` — **sharp** with explicit
  constants. L^∞ Hausdorff bound: `||u||_inf <= 6.4 Delta^(1/2) =
  Theta(1/n)` — **loose by one order of `n`** on the regular n-gon
  family. Radial deviation after Fuglede normalization:
  `||u||_inf = pi^2 / (3 n^2) + O(1/n^4)`.

- **Pattern across briefs.** Combining Osserman and Fuglede on the
  regular-n-gon family:
  Fourier/Sobolev routes (Hurwitz 1902, Fuglede H¹) match the actual
  `Theta(1/n^2)` rate. Geometric/Hausdorff routes (Bonnesen 1921 in
  Osserman; Fuglede L^∞ Theorem 2.3) fall short by **one to two orders
  of `n`** — Bonnesen's `pi^2 (R - r)^2` floor is `O(1/n^4)` (two
  orders weaker); Fuglede's L^∞ bound is `O(1/n)` (one order weaker).
  The methodological independence Osserman flagged (no Hurwitz citation
  in his [1]–[77]) extends: the load-bearing route for the program's
  regular-n-gon decay-rate question is the Fourier/Sobolev branch, not
  the geometric branch. This is the empirical record of the gap, not
  aesthetic preference.

- **L-W-safety status.** Fuglede 1989 itself is post-1882 (post-L-W).
  Per Fuglede footnote 1, the `n = 2` Sobolev content is re-routable
  through Hurwitz 1902, which is post-1882 in calendar but
  transcendence-free in content (no Lindemann-Weierstrass input). The
  audit criterion is *content*, not *calendar*. Fuglede 1989's
  explicit constants — `(1/10, 3/5)` for general `n = 2`, improvable
  to `(0.24, 0.54)` — are a candidate for L-W-safe certification of
  explicit constants in the strip-`H^1` register, since the framework
  underlying them is transcendence-free.

- **The `5 pi` conversion overhead (Fuglede footnote 1).** Hurwitz
  Fourier proof of Bonnesen's geometric inequality
  `(r_2 - r_1)^2 <= c · (L^2/(4 pi) - A)` lands at `c = 5 pi ≈ 15.7`,
  while Bonnesen's own direct parallel-curve proof lands at the sharp
  `c = 1` (per Bonnesen 1924, who showed the inequality fails for any
  `c < 1`). The `5 pi` is a **uniform constant-factor overhead** —
  curve-family-independent, paid once in the Sobolev-to-geometric
  conversion (Hurwitz Sobolev → Cauchy-Schwarz `H^1 -> L^infty`
  embedding on `S^1` → `(r_2 - r_1)^2 <= 4 ||u||_infty^2`). Each step
  is sharp in its own register; the chained bound has slack because no
  single extremal function realizes all three sharpnesses
  simultaneously.

- **Two distinct shapes of looseness.** The cross-brief pattern on
  inscribed regular `n`-gons (Osserman + Fuglede: Fourier/Sobolev
  sharp, geometric/Hausdorff loose by 1–2 orders of `n`) and the
  `5 pi` overhead are **orthogonal phenomena**, not refinements of one
  another:
  - *Metric mismatch* (the cross-brief pattern): different metrics
    have different decay rates on the regular n-gon family. L^∞
    deviation is `Theta(1/n^2)`, but bounds expressed as `Delta^{1/2}`
    only predict `O(1/n)`. Family-specific; rate-of-decay gap.
  - *Conversion overhead* (the `5 pi`): different proofs of the same
    geometric inequality produce different uniform constants. Bonnesen
    parallel-curve proof: `c = 1`. Hurwitz Fourier proof: `c = 5 pi`.
    Bernstein 1905: `c ≈ 1700`. Family-independent; constant-factor
    gap in a fixed-rate bound.
  These compose multiplicatively on the regular n-gon: the Bonnesen
  annulus-width normalization with sharp `c = 1`,
  `(R - rho)^2 <= Delta_H/(4 pi)`, is already loose by `n^2` on this
  family. This is the 1924 `4 pi d^2` form, not the 1921
  `pi^2(R-r)^2` headline. The Hurwitz-Fourier route via `c = 5 pi`
  is `5 pi` times looser than the annulus-width form. The `5 pi` does
  not refine or complicate the cross-brief pattern; it adds a
  curve-independent overhead axis that the cross-brief pattern does not
  capture.

- **Program-side bifurcation.** Two natural registers, each sharp at
  one thing and loose at the other:
  - *Sobolev `||grad u||^2`*: sharp on the rate (Hurwitz exact,
    Fuglede explicit constants), but does not directly bound geometric
    `(r_2 - r_1)^2`.
  - *Geometric `(r_2 - r_1)^2`*: sharp constant `c = 1` only via
    Bonnesen's direct parallel-curve route; the Fourier route incurs
    the `5 pi` overhead.
  For program audit calculations where the constant matters
  (contradiction-step Δ-floors), prefer Bonnesen direct (sharp `c`).
  For rate statements on regular n-gons, prefer Hurwitz / strip-`H^1`
  (sharp rate). The two routes are not interchangeable; the program
  inherits the bifurcation rather than resolving it.

### From [iso/BECK-1994-BRIEF.md](iso/BECK-1994-BRIEF.md)

- **Headline theorem.** Beck Theorem 1: for almost every
  `alpha in R^k` with `k >= 2`,
  `Delta(alpha; N) << (log N)^k · phi(log log N) <=>
  sum 1/phi(n) < infty`. Multidimensional Borel-Cantelli analog of
  Khintchine 1923 (1-dim, via continued fractions). Sharpens
  Schmidt 1964's `(log N)^{k+1+eps}` by one logarithm. Theorem 2
  (sum of fractional-part products, almost every `alpha`) and the
  continuous version (geodesic line on `T^{k+1}`) are derived from
  Theorem 1.

- **Methodological substitution.** Beck's tools — Fourier analysis,
  Poisson summation, Fejér smoothing, second-moment method, local
  Borel-Cantelli lemmas, combinatorial box decomposition —
  *substitute for continued fractions* in higher-dimensional
  discrepancy proofs (Beck p. 452). This is methodologically the
  same recipe the program's K-H-L-A discrepancy branch uses
  (Aitchison + Erdős-Turán-Koksma + Kraft) at 1-dim; Beck is a
  worked example at higher dimension.

- **Roth-1954 vs. Roth-1955 distinction.** Beck's lower bound
  `Delta(alpha; N) >> (log N)^{k/2}` for *every* `alpha in R^k`
  (eq. 2.17) cites **Roth 1954** "On irregularities of distribution"
  (Mathematika 1, 73-79) — the L²-Fourier *discrepancy* lower bound.
  This is methodologically distinct from Roth 1955's *transcendence*
  theorem on rational approximations to algebraic numbers. The 1954
  paper is transcendence-free in content; the 1955 paper is the
  problematic post-L-W input. *For program audit purposes:
  Beck's content does not depend on Roth-1955 transcendence
  machinery.*

- **Almost-every vs. specific-`alpha` mismatch.** Beck's headline
  theorems are measure-theoretic ("for almost every `alpha`"). The
  program targets specific `alpha = pi` (or polygon-related
  algebraic number). Beck's bounds do not directly apply to a
  specific point of measure zero. The empirical-to-density proxy at
  [memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md](memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md)
  Step 5 is the program's bridge from "almost every" to "this
  specific `alpha`"; Beck's local-lemma structure (Lemmas 4.1-4.4)
  is a usable methodological template but not a direct input.

- **L-W-safety audit verdict.** Beck 1994 is calendar-post-1882
  (1994 - 1882 = 112 years), but methodologically *plausibly
  L-W-safe in content*. The proof techniques (Poisson summation,
  Fejér smoothing, Cauchy-Schwarz, Borel-Cantelli, Schmidt 1960
  second-moment inequality) are transcendence-free; the only
  potentially-problematic input is **Schmidt 1960** [18], which
  would require its own L-W-safety brief if program use becomes
  load-bearing. The Roth input is Roth 1954 (discrepancy), not Roth
  1955 (transcendence) — a distinction that matters for the audit.

- **Cross-brief pattern, third axis.** Osserman + Fuglede + Beck
  cover three distinct registers attaching to `Delta`:
  - *Geometric* (Osserman): `Delta >= pi^2 (R - rho)^2` etc.;
    family-specific, loose by `n^2` on regular n-gons.
  - *Sobolev / Stability* (Fuglede): `Delta >= const ||grad u||^2`;
    sharp rate on regular n-gons; explicit constants `(0.24, 0.54)`.
  - *Probabilistic / Diophantine* (Beck): discrepancy of `(n alpha)
    mod 1` sequences; almost-every register, no specific-alpha
    bound. **Distinct hypothesis class** from the regular-polygon
    family — Beck's `(n alpha) mod 1` is irrational sequence;
    polygon vertices `(k/n) mod 1` are rational with discrepancy
    `1/n` exactly. So Beck does not enter the regular-polygon test
    case directly; the entry is via the K-H-L-A discrepancy branch
    on `(n pi) mod 1`, a *different* sequence than the polygon
    vertices.

- **Program-side methodological alignment.** The K-H-L-A discrepancy
  branch already uses Aitchison + Erdős-Turán-Koksma + Kraft; Beck
  uses Poisson + Fejér + second-moment + Borel-Cantelli on the
  multidim version of the same target. The two are
  methodologically convergent: both replace continued-fraction
  arguments with Fourier-side machinery for non-1-dim or
  averaged-over-range targets. Beck's 1994 paper provides a fully
  worked example that the Fourier substitution suffices, which
  affirms the K-H-L-A program's strategic choice.
