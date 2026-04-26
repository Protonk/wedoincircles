# OLD-TIME-RELIGION

A search memo on pre-1882 mathematical tools as candidate toolchains for the
circle-side program, with the L-W-safety audit in view.

The parent [memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md](memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md)
now closes its one-dimensional bookkeeping at
[memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md](memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md)
and announces the L-W-safety audit as the next live step. That audit is the
decisive gate. Every load-bearing step in the current construction leans on
machinery from after 1882 (Fortnow 2000, Aitchison 1959, Erdős-Turán 1948,
Kuipers-Niederreiter 1974). Each must either re-certify as methodologically
pre-L-W or be replaced by something that is provably pre-1882. This memo
tracks the practice of the replacement work.

Two modes are available, and the distinction is load-bearing:

- **Anchor mode.** Take a pre-1882 theorem as a fixed lower bound and
  arrange the modern construction to collide with it. The *setup* may use
  modern tools; the *contradiction step* uses only pre-1882 machinery. The
  argument is safe as long as the modern setup is itself methodologically
  pre-L-W.
- **Rebuild mode.** Take a pre-1882 primitive and use it to reconstruct a
  modern structure from scratch. The reconstructed structure then has
  pre-1882 provenance by construction. High cost, high risk of reinventing
  a weaker version of a mature tool, and the reconstruction may silently
  import modern ideas through the back door.

Current verdict (per the search-memo register):
**anchor mode is still the live practice**, but the naive Liouville
endgame on the polygon-gap approximant is now closed negative. The first
directed attempt — (A2) paired with (A3), carried by (A8) — was run in
[memos/LIOUVILLE-SCALE-TEST.md](memos/LIOUVILLE-SCALE-TEST.md). Stage 1
reduces the inscribed gap, the circumscribed/radial-lift gap, and the
strip `H^1` seminorm to geometric weights on the single approximant
`alpha_n - pi`, where `alpha_n = n tan(pi/n)`. Stage 2 shows
`alpha_n` has exponential cyclotomic height (`log M(alpha_n) ~
phi(2n) log n` along primes), so Liouville cannot collide with the
Archimedean `1/n^2` upper bound. That branch is dead on scale, not on
provenance. The next live anchor attempts must either build a different
small algebraic quantity or move to the discrepancy/Aitchison side.
Rebuild mode remains a last resort, triggered only when a specific audit
step fails and no pre-1882 anchor can be found. The specific rebuild the
program has gestured at — Boole-to-Kraft — is almost certainly a bad
trade; §(B1) explains why.

---

## Audit criterion: content, not calendar

The audit asks whether a step's *proof* depends on transcendence-
theoretic results, not whether the *paper* was published before 1882.
"Pre-1882" is calendar shorthand for the actual criterion, which is
**transcendence-free in content**.

Most pre-1882 papers are obviously safe (they couldn't depend on a
theorem that hadn't been proved yet). Some post-1882 papers are also
safe: a result whose proof uses no Lindemann-Weierstrass-or-later
machinery is L-W-safe in content even when its publication date sits
on the wrong side of the calendar cutoff.

The first crisp example surfaced in
[iso/FUGLEDE-1989-BRIEF.md](iso/FUGLEDE-1989-BRIEF.md): Fuglede
1989's explicit constants in the `n = 2` Sobolev stability bound are
post-L-W in publication, but per Fuglede's own footnote 1 the `n = 2`
content is re-routable through Hurwitz 1902 — itself post-1882 in
calendar but transcendence-free in content. Fuglede 1989's `n = 2`
constants are therefore a candidate L-W-safe certification of explicit
constants in the strip-`H^1` register.

(A4) Dirichlet kernel / Jordan bounded variation already operates
under this criterion implicitly: Hurwitz 1902 is post-1882 by 20
years, but the Fourier/Parseval primitives the row terminates at are
all pre-1882 (Fourier 1822, Parseval 1799, Dirichlet 1829). The
content-criterion clarification makes that practice explicit, and
extends it: the audit may admit any post-1882 result whose proof is
provably transcendence-free, not only those that terminate at
classical Fourier primitives.

Consequence for the (A) and (B) catalogues. A candidate anchor's
first-proof date is not the end of the audit. If the proof technique
routes through transcendence theory (Baker, Gelfond-Schneider, or
descendants), the anchor fails the audit even if the paper is ancient.
Conversely, a post-1882 result whose proof is provably
transcendence-free can serve as a contradiction-step anchor.

---

## Target

Single sentence, honest about uncertainty:

> Identify pre-1882 theorems that either (a) supply a provably-pre-L-W lower
> bound against which the current Kraft-Parseval budget can be made to
> contradict, or (b) plausibly reconstruct a modern primitive (Kraft's
> inequality, Fortnow's universal dominance, Aitchison's characteristic-
> function bound) without importing post-1882 content, then track which
> mode applies to each load-bearing step of the drafted argument.

Priority ordering. Anchor mode is audited item-by-item first. Rebuild mode
opens only when anchor mode fails on a specific item and no alternative
anchor exists. Sentiment-driven rebuilds are not in scope.

---

## (A) Anchor-mode candidates

Each row is a pre-1882 theorem that could serve as the contradiction step
for some part of the drafted argument. Rows are live audit targets, not
committed dependencies. (A1) Liouville and (A7) Dido state the classical
pre-1882 anchors; (A2)-(A6) and (A8) are the working forms that actually
carry calculation. Pre-1882 tools considered but not currently attached
to a load-bearing step live in the Reserve list at the end of §(A), to
be recalled if one of the live rows fails.

### (A1) Liouville 1844

Liouville's bound: for algebraic `alpha` of degree `d >= 2`, there exists
`c(alpha) > 0` with

```text
|alpha - p/q| > c / q^d
```

for every rational `p/q`. Proof is elementary polynomial evaluation plus the
mean value theorem. No exp-map, no transcendence input. Predates Hermite 1873
by 29 years.

- **Known.** Liouville is the canonical pre-1882 lower bound on algebraic
  heights. Parent memo §(C) already plans to end at a Liouville-type
  inequality against the Archimedean `Theta(1/n^2)` upper bound.
- **Unknown / scale risk.** Whether the relevant Liouville inequality on
  the joint cyclotomic `times Q(pi)` field, under the hypothesis that `pi`
  is algebraic of degree `d`, gives an exponent tight enough to collide
  with `1/n^2`. This is the decisive danger. A generic norm over
  `K_n Q(pi)` is likely to produce a lower bound of order
  `exp(-O(phi(n) log n))` or worse, which will not meet an `O(1/n^2)`
  upper bound at any `n`. The only way this row helps is if the special
  linear-in-`pi` shape or the paired inscribed/circumscribed squeeze
  removes most of the apparent height. The working form of that question
  lives in (A2); the matching upper-bound form lives in (A3).
- **Closing condition.** A height-bound calculation on
  `(L_n^insc)^2 - 4 pi A_n^insc` in the joint field, with the Archimedean
  rate `1/n^2` written out against the Liouville `1/q^d` bound, yielding a
  specific `C` or a specific failure mode.
- **Status.** Closed negative for the natural polygon-gap approximant by
  [memos/LIOUVILLE-SCALE-TEST.md](memos/LIOUVILLE-SCALE-TEST.md). All three
  geometric gaps route through `alpha_n - pi` with
  `alpha_n = n tan(pi/n)`, and `alpha_n` has exponential cyclotomic
  height. Liouville's lower bound is exponentially too weak to meet the
  `1/n^2` Archimedean upper bound. This does not rule out Liouville on a
  different small algebraic quantity; none is currently on the page.

### (A2) Resultants, norms, and Cauchy root bounds

Use the pre-L-W algebra of resultants and field norms as the working form
of the Liouville step. If `pi` is assumed algebraic with primitive
polynomial `P_pi(x)` and the polygon data live in a cyclotomic field `K_n`,
then the gap

```text
G_n = (L_n^insc)^2 - 4 pi A_n^insc
```

is a linear expression in `pi` with coefficients in `K_n`. Clearing
denominators and taking the norm over `K_n Q(pi)` gives a nonzero integer.
Resultants express that integer without invoking transcendence theory;
Cauchy root bounds give explicit control of the conjugate factors.

- **Known.** This is exactly the low-background algebra underneath
  Liouville: primitive polynomials, symmetric functions of conjugates,
  resultants, and root bounds. It does not need Baker, Gelfond-Schneider,
  or any exp-map input.
- **Unknown.** Whether the resulting lower bound is remotely strong enough.
  A generic norm estimate over `K_n Q(pi)` will likely be
  `exp(-O(phi(n) log n))` or worse, while the geometric upper bound is only
  `O(1/n^2)`. That is not a contradiction. The only way this row helps is
  if the special linear-in-`pi` shape or the paired inscribed/circumscribed
  squeeze removes most of the apparent height.
- **Closing condition.** Write `G_n = a_n - pi b_n` with
  `a_n, b_n in K_n`, compute the primitive resultant/norm after clearing
  denominators, and record the explicit lower bound. If it is exponential
  in `n`, the naive Liouville endgame is not cogent and the memo must say
  so before opening more anchors.
- **Status.** Closed negative for `G_n` and its circumscribed/strip
  siblings. The scale test rewrites them through
  `alpha_n - pi`; the resultant/norm calculation is therefore governed by
  the height of `alpha_n`, not by a hidden lower-height Hurwitz quantity.
  The computed Mahler-measure growth is exponential in `phi(2n) log n`
  along primes, so this row cannot rescue the naive Liouville branch.

### (A3) Euler-Maclaurin / Taylor with signed remainders

Archimedes' method of exhaustion (~250 BCE) supplies the upper bound on
the polygon gap in principle; this row formalizes it with explicit
remainders. Taylor expansion with remainder, Euler-Maclaurin, and the
Bernoulli-number expansions of `sin`, `tan`, and `cot` are all pre-1882
and are enough for the regular polygon formulas. The Archimedean side
should be upgraded from `Theta(1/n^2)` to explicit two-sided inequalities
with named classical provenance.

- **Known.** The relevant expressions are elementary:

  ```text
  L_n^insc = 2 n sin(pi/n),
  A_n^insc = (n/2) sin(2 pi/n),
  Delta_n = L_n^2 - 4 pi A_n
          = L_n^2 (1 - (pi/n) cot(pi/n)).
  ```

  The leading constant `4 pi^4 / (3 n^2)` is already collected in
  [memos/ARCHIMEDEAN-SIGNATURE.md](memos/ARCHIMEDEAN-SIGNATURE.md);
  this row asks for a paper-proof inequality with explicit remainder.
- **Unknown.** Whether the circumscribed counterpart gives a cleaner
  squeeze for the algebraic lower-bound calculation than the inscribed
  gap alone.
- **Closing condition.** Produce constants `c_1, c_2, N_0` such that

  ```text
  c_1 / n^2 <= Delta_n <= c_2 / n^2
  ```

  for `n >= N_0`, and do the same for the circumscribed gap if that is the
  expression fed to the norm/resultant calculation.
- **Status.** The Archimedean side is not the failure. The scale test
  confirms the exact normal form
  `Delta_n = 4 A_n^insc (alpha_n - pi)` and
  `Delta(gamma_tilde_n) = 4 A_n^circ (alpha_n - pi)`. The upper bound is
  the expected `1/n^2`; the failure is that Liouville's lower bound for
  `alpha_n - pi` is far smaller.

### (A4) Dirichlet kernel / Jordan bounded variation

The Fourier / Parseval machinery underneath Erdős-Turán — Fourier 1822,
Parseval 1799, Dirichlet 1829 — is all pre-1882. Hurwitz's 1902
isoperimetric identity and the `Delta_n` first-band concentration of
[corners/HURWITZ-FIRST-BAND-CONCENTRATION.md](corners/HURWITZ-FIRST-BAND-CONCENTRATION.md)
terminate at these primitives modulo the Hurwitz packaging, so that side
of the audit is effectively free. The strip-Hurwitz closure at
[memos/STRIP-H1-HURWITZ-CLOSURE.md](memos/STRIP-H1-HURWITZ-CLOSURE.md)
also lands here: the radial-graph lift is the circumscribed regular
`n`-gon, so its Hurwitz gap is Fourier/Parseval applied to a classical
Archimedean object, not a new modern primitive. The active question for
this row is narrower: the post-1882 Erdős-Turán inequality should be
audited against its old Fourier core — expand interval indicators,
truncate the Fourier series, pay `1/h` for the coefficients. Dirichlet's
Fourier machinery and Jordan's bounded-variation criterion are the natural
low-background ancestors.

- **Known.** The harmonic weight in Erdős-Turán is not mysterious. It is
  the Fourier coefficient size of an interval indicator. This matches the
  shell bookkeeping already written in
  [memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md](memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md).
- **Unknown.** The boundary term is the whole issue. Raw Dirichlet partial
  sums have Gibbs overshoot; modern discrepancy proofs hide this inside
  clean majorant/minorant trigonometric polynomials. If the old Fourier
  package only gives convergence away from endpoints, it does not replace
  Erdős-Turán for star discrepancy.
- **Closing condition.** Reprove the one-dimensional Erdős-Turán inequality
  used in KRAFT-BUDGET-ONE-DIMENSIONAL from Dirichlet/Jordan-level
  primitives, with constants allowed to worsen. If the proof needs
  Fejer/Selberg/Vaaler-style positive kernels, record the provenance
  downgrade explicitly.

### (A5) Cauchy condensation as pre-Kraft shell calculus

Separate the old dyadic-shell arithmetic from the modern prefix-free
semimeasure layer. The estimate

```text
sum_{2^r <= h < 2^(r+1)} 1/h <= 1
```

is just Cauchy condensation / integral comparison. It gives one bounded
unit of harmonic mass per dyadic shell before any Kolmogorov vocabulary is
introduced.

- **Known.** This is enough to justify the "Kraft-shaped" shell budget on
  the Fourier side as old calculus. It also clarifies what Fortnow adds:
  not the shell mass itself, but the universal semicomputable domination
  used to pull a model-facing constant across encodings.
- **Unknown.** Whether the argument actually needs Fortnow's universal
  dominance, or whether the direct shell budget plus explicit coding of
  `(n, r)` is sufficient for the claimed lower-bound interface.
- **Closing condition.** In every occurrence of "Kraft-Parseval", tag the
  local shell estimate as Cauchy-condensation old calculus and tag any
  universal dominance claim as modern computability. If the final theorem
  needs the latter essentially, the theorem is not strictly pre-1882 even
  if the Fourier estimates are.

### (A6) Jacobi theta / Poisson test case

Before trying to replace Aitchison in full generality, test the density
side on the classical Gaussian case. Poisson summation and Jacobi's theta
transformation give the fractional-part Fourier coefficients explicitly:
Gaussian smoothing has coefficients with quadratic exponential decay.

- **Known.** This gives a pre-1882 sanity check for the Aitchison-facing
  statement `d(g, u) <= sum |C_X(2 pi r)|` in the most favorable case.
  It is also the cleanest place to see whether the Aitchison layer is doing
  more than Poisson summation plus absolute convergence.
- **Unknown.** The polygon density `g_n` is sparse and algebraic, not
  Gaussian. A Gaussian test case may certify provenance without proving the
  polygon interface.
- **Closing condition.** Derive Aitchison 2.3 for a periodized Gaussian
  from Poisson/Jacobi primitives, then state exactly which step fails or
  changes when `g_n` replaces the Gaussian.

### (A7) Dido / Zenodorus isoperimetric theorem

The classical isoperimetric problem — given a closed curve of fixed
perimeter `L`, maximize the enclosed area `A` — has the circle as its
extremum, with `L^2 = 4 pi A` iff the curve is a circle. Zenodorus
(~200 BCE) gives the earliest recorded mathematical formulation; Steiner's
1838 symmetrization gave the first elementary proof for convex curves.
The rigorous Jordan-curve formulation is 1887 and later, but the program
does not need that formulation: for polygons and smooth convex curves the
pre-1882 statement suffices, and the defect `L^2 - 4 pi A >= 0` is the
load-bearing object.

- **Known.** The isoperimetric defect `Delta_n = L_n^2 - 4 pi A_n` is
  exactly the object the parent memo §(B) calls the "Hurwitz-Dido
  extremum." Dido supplies the pre-1882 statement that the defect is
  positive for every non-circular polygon; Hurwitz 1902 (see (A4)) supplies
  a Fourier-analytic proof, but the statement and the defect predate him.
  Steiner 1838 handles the convex-curve case without modern curve theory.
- **Unknown.** Whether a Steiner-symmetrization-level derivation gives a
  quantitative defect tight enough to pair with (A1)/(A2). Steiner's
  argument shows the defect is positive; the `Theta(1/n^2)` rate for
  regular polygons currently comes from (A4) Fourier or (A3) Taylor.
- **Closing condition.** Either a Steiner-style pre-1882 derivation of the
  `1/n^2` rate for regular polygons, or an explicit tag that the rate
  provenance is Fourier/Taylor and Dido supplies only positivity of the
  defect.

### (A8) Cyclotomic units and sine-product identities

Kummer's cyclotomic-unit arithmetic — closed-form norms of `1 - zeta_n`,
the classical sine-product identity
`prod_{k=1}^{n-1} 2 sin(k pi / n) = n`, and the unit group of `Z[zeta_n]`
— gives exact height control on the polygon data that enters (A2). Because
`sin(pi/n)` and `cot(pi/n)` are built from roots of unity, their minimal
polynomials and norms are cyclotomic-unit expressions with integer values,
not generic Mahler-measure estimates. The trace field `K_n = Q(cos 2pi/n)`
is also the Chebyshev register (`T_n(cos theta) = cos(n theta)`, Chebyshev
1854), so cyclotomic-unit arithmetic here doubles as the Chebyshev-form
height calculation the Liouville step ultimately needs.

- **Known.** The polygon data `L_n^insc = 2 n sin(pi/n)` and
  `A_n^insc = (n/2) sin(2 pi/n)` live in `K_n = Q(cos(2 pi/n))`; their
  heights are computed exactly by cyclotomic-unit norms. Kummer's
  cyclotomic-integer arithmetic (1840s-1850s) and the sine-product
  identity are both well pre-1882.
- **Why this mattered.** This row was the best pre-1882 lever on the
  scale risk in (A1)/(A2). A generic norm estimate over `K_n Q(pi)`
  produces `exp(-O(phi(n) log n))` because it treats `L_n, A_n` as
  arbitrary algebraic numbers; a cyclotomic-unit calculation was the
  plausible way to detect cancellation among conjugates on the unit
  circle. The scale test confirms that, for `alpha_n`, the hoped-for
  cancellation does not occur.
- **Closing condition.** Express the gap
  `G_n = (L_n^insc)^2 - 4 pi A_n^insc = a_n - pi b_n` with
  `a_n, b_n in K_n`, reduce `a_n` and `b_n` to cyclotomic-unit form, and
  compute `N_{K_n/Q}(a_n)` and `N_{K_n/Q}(b_n)` by sine-product
  identities. Record the actual height growth in `n`. This computation is
  now done for the `alpha_n` normal form; repeat it only for a genuinely
  different small algebraic quantity.
- **Status.** Closed negative for `alpha_n = n tan(pi/n)`. Cyclotomic-unit
  cancellation does not collapse its height; the worst conjugates near
  `n/2` survive and force `log M(alpha_n) ~ phi(2n) log n` along primes.
  Keep this row only as a possible tool for a genuinely different small
  algebraic quantity.

### Reserve (not promoted)

Pre-1882 tools identified as potentially useful but not yet attached to a
specific load-bearing step. Listed only so future audits do not
re-discover them; do not open full (A) rows unless a specific audit
failure names one.

- **Dirichlet simultaneous approximation 1842.** The pigeonhole bound
  `|alpha - p/q| < 1/(q N)` for every irrational `alpha` and every
  `N >= 1`. Not currently attached to any step: the program's upper bound
  on the polygon gap comes from Archimedes, not from rational
  approximation to `pi`. Recall if a step ever needs "every irrational
  has good rational approximants" beyond the Liouville / cyclotomic-height
  register.
- **Euler / Lagrange / Legendre continued fractions (1730s-1808).**
  CF-convergents of `pi` as a pre-1882 accounting scheme alternative to
  the dyadic shells of Kraft-Parseval. Speculative restatement, not
  directed work; recall if a CF-specific audit target ever opens. The
  crosswalk memo [rotations/CONTINUED-FRACTIONS-CROSSWALK.md](rotations/CONTINUED-FRACTIONS-CROSSWALK.md)
  identifies CF convergents as a primitive shared across four memos, but
  none of those contact points currently sit on a load-bearing audit
  step.
- **Bezout / Sylvester resultants plus Sturm 1829.** Concrete working
  toolkit underneath (A2): Sylvester determinant resultants for the
  "nonzero algebraic integer" step, Sturm's theorem for explicit real-root
  separation.
- **Dedekind algebraic integers and discriminants (1871-1877).** Pre-1882
  by a narrow margin. Would organize denominator clearing and ring-of-
  integers arithmetic in `K_n Q(pi)` if the compositum gets messy; less
  elementary than (A8) cyclotomic units, so reach for it only if (A8)
  is not enough.
- **Kronecker's root-of-unity rigidity (1857).** Algebraic integers whose
  conjugates all lie on the unit circle are roots of unity. Guardrail
  against claims that accidentally characterize cyclotomic-only data.
- **Lambert 1761.** Irrationality of `pi`. Lower-background than
  Liouville. Use Lambert, not Liouville, whenever a step only needs `pi`
  irrational and not algebraic-of-bounded-degree.
- **Abel summation / summation by parts (Abel 1826).** Standard
  Fourier-tail technique. Useful on the (A4) Dirichlet-kernel side for
  converting coefficient estimates into discrepancy-style bounds without
  invoking newer kernel packages.
- **Cauchy-Bunyakovsky-Schwarz inequality (Cauchy 1821 / Bunyakovsky
  1859).** Low-background substitute for later norm-inequality packaging
  when moving between Fourier coefficient sums, Parseval norms, and
  absolute bounds.

---

## (B) Rebuild-mode candidates

Each row is a reconstruction target: a modern primitive the program uses,
and the pre-1882 tool that might in principle rebuild it. Rows here are
much slower to act on than (A) rows. Do not open (B) work without first
showing that the corresponding (A) row fails.

### (B1) Boole 1854 -> Kraft 1949 (do not pursue speculatively)

*An Investigation of the Laws of Thought* (1854) gives an algebra of logic
and a calculus of probability. The question posed to this memo is whether
Boole can be made to rebuild Kraft arithmetic from scratch.

- **Known.** Boolean algebra is finitary and truth-functional; Kraft's
  inequality is about prefix-free codes and self-delimiting length
  functions over countable alphabets, with an infinite-series statement
  (`sum 2^(-l_i) <= 1`). The structural content Boole does not speak to is
  exactly the content Kraft needs: a code tree, a length function, and a
  convergent series over code lengths.
- **Why pursuit is likely wasteful.** Kraft's own 1949 proof is trivial
  (the series is a sum over disjoint leaves of a binary tree with measure
  `2^(-l_i)`). The hard part of the current argument is not Kraft's
  inequality; it is the Fortnow universal-dominance step that sits on top
  of it. Rebuilding the easy part from Boole while still needing Fortnow
  buys no provenance, and any rebuild that tries to reach Fortnow-style
  semimeasures from Boolean primitives alone is reinventing Turing
  machines without Turing.
- **Closing condition.** Retire this row unless a specific audit failure
  isolates Kraft's inequality itself as the offending step. The current
  search has no reason to open it.

### (B2) Gauss 1809 least squares / 1801 cyclotomy -> Aitchison 1959

Gauss's least-squares and cyclotomy already speak Fourier and
orthogonality. Aitchison 1959 packages a Poisson-summation density-side
bound with explicit characteristic-function decay.

- **Known.** The cyclotomic half of the parent memo is natively Gaussian
  and needs no rebuild. The Poisson-summation half has a pre-1882 ancestor
  in Poisson 1827.
- **Unknown.** Whether Aitchison's specific characteristic-function
  inequality (2.3) can be recovered from Poisson 1827 plus classical
  Fourier in a form tight enough for the parent memo's Step 3.5.
- **Closing condition.** A pre-1882 derivation of Aitchison 2.3 for the
  polygon density `g_n` of KRAFT-BUDGET-ONE-DIMENSIONAL §3.5, or a
  documented failure. (A6) is the natural prerequisite — a Gaussian test
  case before the algebraic one.

### (B3) Catalog of likely non-starters

Rows here are kept only to prevent re-opening by a later agent:

- **Boole -> Fortnow.** Fortnow's Fact 6.2 needs a universal semicomputable
  measure. That needs a universal Turing machine. Boolean algebra does not
  get you there.
- **Abel / Galois -> transcendence.** Algebraic irresolvability is
  orthogonal to transcendence. Do not attempt to use the 1820s-1830s work
  on solvability of polynomial equations as a transcendence input.
- **Cauchy residues -> effective Liouville.** Residue calculus is pre-1882
  (Cauchy 1825), but turning it into an effective Diophantine bound is
  precisely what Baker 1966 does, and Baker is post-L-W. The calculus is
  safe; the Diophantine use is not.

---

## (C) Practice

This memo is a workbook for the audit, not a theorem. The practice it
records:

1. **First directed attempt: (A2) paired with (A3), carried by (A8) —
   closed negative.** [memos/LIOUVILLE-SCALE-TEST.md](memos/LIOUVILLE-SCALE-TEST.md)
   shows the polygon-gap branch reduces to `alpha_n - pi` and dies on
   height scale. Do not continue trying to make Liouville collide with
   `Delta_n`, `Delta(gamma_tilde_n)`, or `||y_n'||^2`; they are all
   weighted versions of the same approximant.
2. **Next directed attempts.** Either invent a different small algebraic
   quantity with polynomial cyclotomic height, or shift to the
   discrepancy/Aitchison mechanism over a range of `n`. The empirical-to-
   density proxy of KRAFT-BUDGET-ONE-DIMENSIONAL Step 5 is now the natural
   live target on the discrepancy side; (A6) is the cleanest
   self-contained density-ancestry test.
3. **Run anchor mode item-by-item on the rest.** For each load-bearing
   step in KRAFT-HERMITE-LINDEMANN-AITCHISON and
   KRAFT-BUDGET-ONE-DIMENSIONAL, identify a candidate (A) row and try to
   close it. The Liouville/polygon-gap row is now closed; do not let it
   obscure the still-open discrepancy branch.
4. **Tag the shell-calculus / universality split explicitly.** Per (A5),
   the dyadic shell mass in every "Kraft-Parseval" step is
   Cauchy-condensation old calculus, but the universal-dominance claim on
   top of it is modern computability. Fortnow is provenance-expensive and
   does not inherit classicality from the harmonic arithmetic beneath it.
   If the final theorem needs Fortnow essentially, the theorem is not
   strictly pre-1882 even when every Fourier estimate is.
5. **Escalate to rebuild mode only on specific failure.** If an (A) attempt
   fails and no alternative (A) anchor exists, open a (B) row. Never open
   a (B) row because the rebuild "would be interesting."
6. **Record failures as findings.** A step that cannot be anchored at
   pre-1882 machinery is a finding. It means the pre-L-W provenance claim
   is retired for that step and the program either lives with the
   methodologically-safe tag or retreats to a weaker deliverable.
7. **Keep the log-side asymmetry visible.** Landfall's pointwise
   transcendence statement uses Gelfond-Schneider (post-L-W). The circle
   side is attempting the analogous statement without that crutch. If the
   circle side's audit fully closes at pre-1882 anchors, the asymmetry is
   the novelty. If it does not, the program degrades to a second
   transcendence proof rather than a structurally new one.

Append new anchor attempts here as they run. Do not retroactively edit old
entries; note outcomes below.

---

## Adjacent anchors

- [memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md](memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md)
  §(D) — the parent memo's L-W-safety tags. Every (A) row here should map
  to a row there.
- [memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md](memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md)
  Step 5 — the empirical-to-density proxy, currently a hypothesis. With
  the (A2)+(A3) Liouville branch closed negative, this is the natural live
  target on the discrepancy side.
- [memos/LINDEMANN-BRIEF.md](memos/LINDEMANN-BRIEF.md) — the circularity
  map. Tags in this memo defer to that brief's exit criteria.
- [memos/FORTNOW-KOLMOGOROV-BRIEF.md](memos/FORTNOW-KOLMOGOROV-BRIEF.md) —
  the modern computability layer. This memo does not replace it; it
  identifies which of its uses can terminate at a pre-1882 anchor.
- [memos/RAMANUJANS-COMPLIMENT.md](memos/RAMANUJANS-COMPLIMENT.md) —
  adjacent memo on when to stay inside Ramanujan's pre-theoretical orbit
  and when to leave for lower-bound literature. Practice overlap on
  discipline, not content.

---

## What this is not

- Not a proposal to discard modern tools on principle. Modern tools stay
  unless an audit identifies a specific failure.
- Not a proof that no pre-1882 endgame exists. It does record that the
  natural Liouville endgame on `alpha_n - pi` is dead on scale.
- Not a commitment to rebuild Kraft from Boole. It is in fact a
  documented recommendation against doing so.
- Not a historical catalog. Rows are live audit candidates. A pre-1882
  theorem with no current audit relevance does not belong here.
- Not a replacement for LINDEMANN-BRIEF. This memo is the practice side;
  the brief is the circularity side.

---

## Exit criteria

This memo freezes, and its content promotes, when any one of the following
triggers:

1. Every load-bearing step in KRAFT-HERMITE-LINDEMANN-AITCHISON and
   KRAFT-BUDGET-ONE-DIMENSIONAL is tagged with a pre-1882 anchor (or a
   methodologically-safe modern packaging of a pre-1882 anchor), and the
   Liouville-style endgame survives through a small algebraic quantity
   *other than* `alpha_n - pi`, or the discrepancy branch supplies a
   replacement endgame with an effective constant extractable. Promote the
   consolidated anchor list into the parent memo's §(D) and retire
   OLD-TIME-RELIGION.
2. A specific load-bearing step is proven to require post-1882 content
   with no pre-1882 anchor available. Promote the negative finding into
   LINDEMANN-BRIEF's exit-criteria table, retire the pre-L-W provenance
   claim on that step, and retire OLD-TIME-RELIGION after noting the
   failure mode. The scale-failure form of this trigger has already fired
   for the `alpha_n` / polygon-gap Liouville branch; remaining work must
   not recycle that same approximant under new vocabulary.
3. Two directed attempts on a single (A) row fail to make progress and no
   alternative (A) row for the same load-bearing step is visible. Park the
   step, note the failure, and reconsider after adjacent audits land.

If the memo starts growing more rows without closing any, that is itself a
finding: it means the audit is too diffuse and the next action is to pick
one load-bearing step and exhaust its (A) candidates before adding more.
