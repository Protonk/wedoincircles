# KRAFT-HERMITE-LINDEMANN-AITCHISON

A search memo on whether effective Hermite–Lindemann at $n=1$ — transcendence of $\pi$ with an effective irrationality measure — can be reproduced as a pure Kraft argument on the circle. The ambition is to replace Hermite's 1873 integral-auxiliary construction with a Kraft–Parseval budget assembled from three pieces already on the program's desk: (i) Aitchison's 1959 density-side Fourier expansion on $\mathbb{T}$ via Poisson summation (`sources/A Statistical Theory of Remnants.pdf`), (ii) the Erdős–Turán–Koksma discrepancy-sum inequality in its multi-dimensional harmonic-weighted form (`sources/K-N-Chapter2.pdf`, §2 and p. 116), and (iii) the Kraft-arithmetic machinery already in use on the log side in `sources/landfall.pdf` §5.

The non-obvious hook — the part the memo proposes but does not yet prove — is that **Dido**'s isoperimetric extremum, expressed in Hurwitz's 1902 Fourier-analytic form, gives $\pi$ a variational certificate whose Fourier-support condition is native to the Kraft–Parseval budget. That removes the need to route through the exp-map the way classical Hermite–Lindemann does, and pairs the transcendence statement to the geometry of approximating the circle by polygons rather than to algebraic relations among $e^\alpha$ for algebraic $\alpha$. This is what the program's opening commitment to "approximating the circle" reaches for. If the memo closes, the deliverable is not a new theorem but a new **proof structure** with an explicit effective constant extractable from the budget — and, if the lineage check passes, a strictly pre-L–W provenance.

This is a **search doc**, not a result doc. It lays out four prerequisites — (A) the Kraft–Parseval budget itself, (B) the Hurwitz–Dido extremum as $\pi$'s native variational certificate, (C) the auxiliary-free Hermite replacement, (D) the effective rate and L–W-safety audit — tracks what's known and unknown for each, and notes which existing repo material feeds in. Progress gets appended here until the pieces are sharp enough to state a theorem; at that point the result-shaped material promotes out.

---

## The target

Single sentence, honest about uncertainty:

> Reprove transcendence of $\pi$ (Hermite–Lindemann at $n=1$) as the saturation of a Kraft–Parseval budget (Aitchison $\times$ Erdős–Turán–Koksma) against the Hurwitz–Dido isoperimetric extremum, with an effective $|q\pi - p| \gg q^{-C}$ constant extractable from the same argument and strictly pre-L–W provenance verified.

Landfall template, compressed. The source paper `sources/landfall.pdf` §5 reads prefix-free halting domains through Kraft's inequality and concludes "composition redistributes the available Kraft budget; it does not create the missing correction." On the log side, the uncorrected-by-finite-composition object is $\varepsilon(m) = \log_2(1+m) - m$; the pointwise transcendence statement (Landfall §4) is $\varepsilon(k/2^p)$ transcendental at every interior machine dyadic, via Gelfond–Schneider. On the circle side, the uncorrected-by-finite-composition object is $\pi$ itself, and the pointwise transcendence statement the program would like is H–L at $n=1$. The two statements sit at the same altitude on their respective sides — they're the clean arithmetic-depth fact each program leg wants to land.

Desired shape, paralleling `memos/COUNTING-APPARATUS.md`'s "equivariant surrogate / residue / compute-cost" triptych:

- **Equivariant surrogate**: inscribed (or circumscribed) regular $n$-gon. Free in cyclotomic arithmetic: vertex coordinates are $(\cos(2\pi k/n), \sin(2\pi k/n))$, algebraic of degree $\varphi(2n)/2$. See the catalog at `corners/PSEUDO-CHEBYSHEV-NODES.md`.
- **Residue**: the isoperimetric deficit $L^2 - 4\pi A$, Hurwitz form $4\pi^2 \sum_{|n|\ne 1} n(n-1)\,|c_n|^2$. Zero iff the curve is a circle. Archimedean rate: $(L_n^{\text{insc}})^2 - 4\pi A_n^{\text{insc}} = \Theta(1/n^2)$ for regular $n$-gons.
- **Kraft–Parseval budget**: Erdős–Turán–Koksma, $D_N \lesssim 1/m + \sum_{0 < \|\mathbf{h}\|_\infty \le m} r(\mathbf{h})^{-1}\, |S_N(\mathbf{h})|$ with $r(\mathbf{h}) = \prod_j \max(|h_j|, 1)$ (K-N p. 116), paired with Aitchison's density-side $d(g, u) \le \sum_{r \ne 0} |C_X(2\pi r)|$ (Aitchison 2.3, with $k$-dim twin at 6.8). The pairing is: E-T-K supplies the *a priori* dual-lattice weight, Aitchison supplies the *a posteriori* per-frequency density mass.
- **Effective rate**: $|q\pi - p| \ge c\, q^{-C}$ with $C$ extractable from (Archimedean exponent) $\times$ (cyclotomic height growth) $\times$ (Kraft–Parseval harmonic constant). Compare against Salikhov's 7.6 (current best) and Mahler's 42 (1953).

---

## Methodological precedent

Fortnow 2000 §2 reproves the **infinitude of primes** via Kolmogorov incompressibility: take Kolmogorov-random $m$ of length $n$, suppose the prime list $p_1, \ldots, p_k$ is finite, write $m = p_1^{e_1} \cdots p_k^{e_k}$, note that $|\langle e_1, \ldots, e_k\rangle| \le 2k \log\log m$, conclude $C(m) \le 2k \log(n+1) + c$, contradicting $C(m) \ge n$ for large $n$. The same technique yields the effective $p_i \le i (\log i)^2$ bound — close to the Prime Number Theorem, derived from the complexity side. Fortnow §3 extends the same **cut-and-paste** template to runs in random strings: if $x$ contains a run of zeros longer than a specific length, then $x$ admits a short description, contradicting randomness.

These are the direct structural precedent for this memo's ambition: a classical theorem reproved through a Kraft-accounted incompressibility argument, with an effective rate extractable as a side effect of the argument. Euclid → incompressibility (Fortnow §2) is the miniature of effective H–L at $n = 1$ → Kraft budget (this memo). The memo should keep that template in view when writing §(C) below. See `memos/FORTNOW-KOLMOGOROV-BRIEF.md` §§2–3.

---

## (A) The Kraft–Parseval budget

**What it is.** A joint Fourier-side accounting of how discrepancy of the sequence $(n\pi) \bmod 1$ (or multi-dim generalizations on $\mathbb{T}^k$) decays with $N$, with a weight structure that is literally Kraft-shaped on the dual lattice.

**What the two sources contribute.**

Erdős–Turán (K-N Thm 2.5):

$$D_N \le \frac{6}{m+1} + \frac{4}{\pi}\sum_{h=1}^m \left(\frac{1}{h} - \frac{1}{m+1}\right)\left|\frac{1}{N}\sum_{n=1}^N e^{2\pi i h x_n}\right|.$$

Multi-dim Erdős–Turán–Koksma (K-N p. 116):

$$D_N \le C_k\!\left(\frac{1}{m} + \sum_{0 < \|\mathbf{h}\|_\infty \le m} \frac{1}{r(\mathbf{h})}\,\bigl|S_N(\mathbf{h})\bigr|\right),\qquad r(\mathbf{h}) = \prod_{j=1}^k \max(|h_j|, 1).$$

The sum $\sum_{\|\mathbf{h}\|_\infty \le m} 1/r(\mathbf{h}) \asymp (\log m)^k$: one log-factor per independent frequency band. That is a proper Kraft budget on the dual lattice — harmonic-Kraft, one dyadic band's worth of description mass per dimension.

Aitchison 1959, density-side twin. For $X$ a random variable with density $f$ on $\mathbb{R}$, the fractional-part density $g(y) = \sum_r f(y+r)$ equals $1 + \sum_{r \ne 0} C_X(2\pi r) e^{-i2\pi r y}$ (his 2.2), and

$$d(g, u) := \sup_y |g(y) - 1| \le \sum_{r \ne 0} |C_X(2\pi r)|$$

(his 2.3). The $k$-dim analog (his 6.3, 6.8) uses the multi-dim Poisson summation with the same Parseval-flavored weighting through the joint characteristic function $C_{\mathbf{X}}(2\pi \mathbf{r})$. For Gaussian $\mathbf{X}$, the decay is exponential in $|\mathbf{r}|^2$; for sharper densities, power-law.

**How they pair.** Aitchison gives the *density-side a posteriori* weight through $C_X(2\pi r)$; E-T-K gives the *empirical-side a priori* weight through $1/r(\mathbf{h})$. If the empirical sequence $(x_n)$ is drawn from a density with characteristic function $C_X$, the expected Weyl sum $|S_N(\mathbf{h})|$ is bounded by $|C_X(2\pi \mathbf{h})|$ plus sampling noise of order $N^{-1/2}$, and the joint budget becomes

$$D_N \lesssim \frac{1}{m} + \sum_{\|\mathbf{h}\|_\infty \le m} \frac{1}{r(\mathbf{h})}\bigl(|C_X(2\pi \mathbf{h})| + N^{-1/2}\bigr).$$

This is the single Kraft–Parseval budget the memo is proposing to run. It interpolates between the "smooth density" and "empirical orbit" regimes, each of which has a classical Fourier bound; their pairing is the content.

For the one-dimensional bookkeeping at the dyadic cutoff `m = 2^R - 1`, the shellized version of Erdős–Turán, the exact per-shell harmonic cost, the direct linear shell candidate, the Step 3.5 interface theorem, the Step 4 Fortnow pullback, and the final Step 5 bookkeeping lemma are now written out at [memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md](memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md). The outcome is that the honest Aitchison-facing object is the paired shell `L_r^(pair)(n)`, obtained exactly from a phase-adjusted polygon density on support `s = +- j n`, Fortnow dominates the exact paired-shell semimeasure rather than a surrogate, and the final one-dimensional discrepancy bound is on the page with every constant sourced and the empirical-to-density proxy stated explicitly.

**What's partially closed (Fortnow §6).**

- The universal semicomputable measure $\mu(x) = 2^{-K(x)}$ together with **Fortnow's Fact 6.2** (universal dominance: any semicomputable $\tau$ with $\sum_x \tau(x) \le 1$ satisfies $\tau(x) \le c\, \mu(x)$) supplies the canonical prefactor this memo was asking for. It is Chaitin's $c$ in Fact 6.2 — the right model-facing constant to sit in front of the budget. In the one-dimensional note, the exact paired-shell semimeasure has now been written down explicitly, Fortnow has been pulled back to the local inequality `L_r^(pair)(n) <= (3 c L_n^2 / (2 pi^2 n^2)) 2^n mu(code(n, r))`, and that inequality has already been folded into the final one-dimensional bookkeeping lemma. What remains is no longer constant consolidation but the next research step beyond it.
- **Fortnow's Theorem 6.3** (`T_worst(n) = O(T_average(n))` under $\mu$) is a candidate *second line of argument*: any worst-case rate lower bound on approximating $\pi$ by rationals at denominator $q$ converts, under $\mu$, to an average-case statement over universally-weighted rationals near $\pi$, with matching-order worst-case falling out of universal dominance. Flag as exploratory; feeds step 2a of §"Proposed order of work" if the memo reaches that step.

**What remains open.**

- Thue–Siegel–Roth (K-N Example 3.1) says algebraic irrationals are of type 1, hence $ND_N = O(N^\varepsilon)$. This is an **input** to the budget for algebraic sequences; it does not fall out of the budget. So the budget discriminates algebraic from transcendental $\alpha$ only *through* the type, which is an exogenous input. This asymmetry has to be lived with: the budget does not prove transcendence by itself; it provides the comparison quantity against which transcendence is detected.
- **Polygon corner is now exact.** Gauss's discrete Fourier inversion (Gauss 1805 via Lagrange 1759-62 + Euler 1748 §240; see [fft/GOLDSTINE-1977-INTERPOLATION-BRIEF.md](fft/GOLDSTINE-1977-INTERPOLATION-BRIEF.md) §3, §8) collapses the empirical-to-density proxy of [memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md](memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md) Step 5 to an identity on regular-polygon vertex input. The proxy now has to cover only polygon → orbit drift, not the polygon part itself. Pending L-W-safety audit on whether the inversion's *use* inside the budget routes through Aitchison/E-T-K essentially or stays inside Lagrange-Euler-Gauss; tracked at (A9) of [memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md).

---

## (B) The Hurwitz–Dido extremum

**What it is.** Dido's classical problem: given a fixed perimeter $L$, maximize the enclosed area $A$. Answer: circle, with $L^2 = 4\pi A$. Hurwitz 1902's Fourier-analytic proof: for a smooth simple closed curve parametrized by arc-length, expand the parametrization in Fourier series; Parseval gives $\sum n^2 |c_n|^2 = (L/2\pi)^2$ and a matching Parseval identity for the area integral, yielding the sharp inequality

$$L^2 - 4\pi A = 4\pi^2 \sum_{n \ne 0} n(n-1)\,|c_n|^2 \ge 0,$$

with equality iff $c_n = 0$ for every $|n| \ne 1$. The extremum is a **Fourier-support condition**: circles are the unique curves whose arc-length parametrization has Fourier mass on frequencies $\pm 1$ only.

**Why this is the right certificate for $\pi$.** $\pi$ appears as the coefficient of $A$ in the Parseval quadratic form, in a way that is immediately sensitive to Fourier support. There is no exp-map in sight. Historically, the Parseval constant $\pi$ is pre-L–W (Fourier 1822, Parseval 1799), pre-Hermite (1873), and well pre-Lindemann (1882). Hurwitz's 1902 proof is chronologically post-Lindemann but uses no transcendence input — it is a direct Fourier/Parseval identity on an arc-length parametrization.

The Fourier-support condition ($c_n = 0$ for $|n| \ne 1$) is **combinatorially** encodable in principle: two nonzero modes, everything else vanishing. That is the part the memo bets can be fed into the Kraft budget as a prefix-free certificate.

**What's closed (via `corners/hurwitz_gap.sage`).**

- *Explicit Fourier coefficients.* A short geometric-sum calculation on the tangent field $T_k = \omega^k \cdot i e^{\pi i/n}$ (edge $k$, $\omega = e^{2\pi i/n}$) gives the closed form
  $$c_m^{(n)} = \begin{cases} L_n^2 / (4\pi^2 m^2) & \text{if } m \equiv 1 \pmod{n}, \\ 0 & \text{otherwise,} \end{cases}$$
  with $L_n = 2n \sin(\pi/n)$. The admissible lattice is $1 + n\mathbb{Z}$, not $\pm 1 \pmod n$ as first guessed — the polygon's rotation-by-$2\pi/n$ symmetry kills every frequency except those congruent to $+1$ mod $n$.
- *Hurwitz identity closure.* The closed-form Parseval identity reads
  $$\Delta_n = L_n^2 - 4\pi A_n = L_n^2 \left[1 - \tfrac{\pi}{n}\cot\tfrac{\pi}{n}\right],$$
  with asymptote $\Delta_n = 4\pi^4/(3n^2) + O(1/n^4)$. Elementary geometry and the closed-form Parseval sum agree to machine precision across $n = 3, 5, 7, 10, 30, 100$; the Parseval sum truncated at $|j| \le 400$ agrees to a relative $1.5 \times 10^{-3}$ uniformly in $n$ (the tail is $\sim 6/(\pi^2 j_{\max})$, independent of $n$). Rate-comparison figure: `figures/hurwitz_gap_rate.png`.

  ![A log-log plot whose three series — a black dashed line, a column of blue dots, and a column of red plus markers — overlap so closely that they trace a single straight diagonal descending from the upper left to the lower right across roughly seven decades on the horizontal axis and six decades on the vertical. A narrower inset panel sits below sharing the horizontal axis: a magenta curve rises on linear-y from near zero to a flat asymptote, with a small annotation pointing at the plateau.](../figures/hurwitz_gap_rate.png)

- *First-band concentration theorem and dyadic-shell corollary.* The companion note [corners/HURWITZ-FIRST-BAND-CONCENTRATION.md](corners/HURWITZ-FIRST-BAND-CONCENTRATION.md) promotes the frequency plot to a theorem: if $B_j(n)$ is the paired contribution of $m = 1 \pm j n$ to $\Delta_n$, then $B_j(n) \le B_1(n)/j^2$ for every $j \ge 1$, hence $B_1(n) \ge (6/\pi^2)\Delta_n$ uniformly in $n$, and more generally $\sum_{2^r \le j < 2^{r+1}} B_j(n) \le 2^{-r} B_1(n)$. The constant is sharp: $B_1(n)/\Delta_n \to 6/\pi^2$ from above. What remains for the Kraft reading is global Aitchison $\times$ E-T-K constant consolidation, not the local shell estimate.

  ![A stacked-area chart titled "Hurwitz gap by frequency band: contribution of m ∈ {1 ± jn} to Δn, stacked over |j| = 1, …, 6". Horizontal axis n from about 1 to 100; vertical axis "fraction of Δn carried by band" from 0 to 1. A dominant dark-purple band (|j| = 1) fills from the baseline up to roughly 0.6 across the whole range, with a slight droop near the left edge. Above it a wider blue-purple band (|j| = 2) carries the next ~0.15. Thinner teal (|j| = 3), green (|j| = 4), light-green (|j| = 5), and a second purple (|j| = 6) bands stack tightly above, each contributing a few percent. A pale gray "tail" band labeled |j| > 6 caps the figure at 1.0. A right-side legend names the bands with their frequency indices and `m = 1 ± jn` formulas.](../figures/hurwitz_gap_frequency_decomposition.png)

**What remains open.**

- Whether the support condition $\{m \equiv 1 \pmod n\}$ is Kraft-encodable without secretly already using the transcendence of $\pi$. The condition is linear on an infinite-dimensional space; the encoding question is whether it can be written as a finite prefix-free description. A natural target: code the polygon-vs-circle *gap* as a prefix-free string whose length is bounded by the polygon's algebraic-depth $\varphi(2n)/2$. Whether this works is the first concrete check (B) still asks to run.
- **Gauss-aliasing as candidate discrete dual.** Gauss 1805 ([fft/GOLDSTINE-1977-INTERPOLATION-BRIEF.md](fft/GOLDSTINE-1977-INTERPOLATION-BRIEF.md) §4, §8) gives a discrete analog of the support condition: under length-$n$ sampling, real-basis modes in residue classes $\pm m \pmod n$ collapse onto a single recovered coefficient, $O(\log n)$-bit encodable per residue class. Encoding length is well below polygon algebraic depth $\varphi(2n)/2 \sim n/\log\log n$, so Kraft-compatibility of the support condition admits a structural existence path through the discrete dual. Audit step: confirm the encoding does not smuggle transcendence content. Tracked at (A9) of [memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md).

---

## (C) The auxiliary-free Hermite replacement

**What classical Hermite–Lindemann does.** Construct an auxiliary polynomial $f$ of bounded degree, define the integral

$$I(t) = \int_0^t e^{-x} f(x)\,dx,$$

derive two inequalities on $I(1)$: one bounding it above (small, because $f$ is small and the integral is short) and one bounding it below (nonzero algebraic integer if $e$ or $\pi$ were algebraic, hence $\ge 1$ in absolute value over its Galois orbit). Contradiction. The $e^{-x}$ is what forces the exp-map detour.

**Dido route proposal.** Replace the exp-kernel integral with a Fourier–Parseval integral of the polygon-versus-circle gap. The "auxiliary" becomes the polygon's own parametrization, whose Fourier coefficients are already algebraic in cyclotomic data. The Hurwitz gap $(L_n^{\text{insc}})^2 - 4\pi A_n^{\text{insc}}$, evaluated at the $n$-gon, is an elementary expression in $\cos(2\pi/n), \sin(2\pi/n)$, and $\pi$. That is the candidate "small quantity."

**Speculative proof-shape — cut-and-paste (Fortnow §3).** *We speculate here on a possible proof shape, with this as a candidate and nothing more — the translation it requires has not been done in this repo and is not yet known to go through.* The polygon-vs-circle gap at level $n$ is a form of *run* in the approximation of $\pi$: a region where the polygon's algebraic data agree with $\pi$ to Archimedean accuracy $\Theta(1/n^2)$. Fortnow §3's cut-and-paste template says that runs longer than a threshold (there: $2 \log n$ zeros in a random string) force a description shorter than the complexity floor, contradicting randomness. The candidate transposition: an agreement between the $n$-gon algebraic approximant and $\pi$ past a specific Archimedean-rate threshold would, under the algebraic-$\pi$ hypothesis, force $K(\pi)$ below the cyclotomic height at that level, contradicting the hypothesis. Needs the `K`-to-algebraic-height translation made rigorous before the argument carries weight; flagged here so §(C) has a candidate shape in view when directed attempts start. See `memos/FORTNOW-KOLMOGOROV-BRIEF.md` §3 for Fortnow's template in its native string-complexity register.

**The hoped-for load-bearing inequality.** If $\pi$ were algebraic of
degree $d$, the original plan was to treat the gap as an algebraic element
of a joint cyclotomic $\times \mathbb{Q}(\pi)$ field, control its height,
and compare the Liouville lower bound with the Archimedean
`Theta(1/n^2)` upper bound. The classical "nonzero algebraic integer is
`>=` one-over-denominator" lower bound (Liouville 1844) would force a
contradiction only if the relevant height grew slowly enough.

**Status after scale test.** The natural version of this inequality is now
closed negative. [memos/LIOUVILLE-SCALE-TEST.md](memos/LIOUVILLE-SCALE-TEST.md)
shows that the inscribed gap, the circumscribed/radial-lift gap, and the
strip `H^1` seminorm all reduce to geometric weights on
`alpha_n - pi`, where `alpha_n = n tan(pi/n)`. Along odd primes,
`alpha_n` has degree `phi(2n)` and Mahler measure
`log M(alpha_n) ~ phi(2n) log n`, so Liouville gives a lower bound far
below the Archimedean `1/n^2` upper bound. The naive Liouville endgame on
the polygon-gap approximant is dead on scale. A Liouville route would now
need a different small algebraic quantity, not a reweighting of these
gaps.

**What's open.**

- Finding a different small algebraic quantity with polynomial cyclotomic
  height, if the Liouville branch is to survive at all.
- Auditing the discrepancy / averaging route over a range of `n`, which
  does not go through `alpha_n` pointwise. The empirical-to-density proxy
  in [memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md](memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md)
  Step 5 is the remaining live bottleneck for that branch.
- Verifying any replacement Diophantine step stays elementary. The natural
  sharpenings — Thue, Siegel, Roth, Baker — are post-L-W and are not
  acceptable for the pre-L-W provenance claim.

---

## (D) Effective rate and L–W-safety

**What would fall out if a replacement (A), (B), (C) close.** A bound of form $|q\pi - p| \ge c\, q^{-C}$ with $C$ extractable from three ingredients:

- **Archimedean exponent**: 2, from $\Theta(1/n^2)$ polygon-vs-circle gap. Pre-L–W (Archimedes).
- **Cyclotomic degree growth**: $\varphi(2n)/2$, averaging $\sim n/\log\log n$ per Erdős–Kac. Pre-L–W (Gauss).
- **Kraft–Parseval harmonic constant**: $O(\log m)$ or $O(\log^2 m)$ from the E-T-K weight, possibly with an $m$-dependence that tightens after matching to Aitchison's density-side decay. Pre-L–W methodologically.

Expected ballpark, now conditional on finding a replacement small
quantity or discrepancy endgame: $C$ in the range 2 to about 10, under
Archimedean-squeeze + cyclotomic-height matching. Compare Salikhov 7.6
(2008, current best), Mahler 42 (1953). A $C$ in that range would be
competitive with the transcendence-theoretic literature; a $C$ in the 20s
would be historically interesting only as a pre-L–W argument.

**Diophantine classification of $\pi$.** The continued-fraction control
parameter to use here is

$$
\beta(\alpha)=\limsup_{n\to\infty}\frac{\ln q_{n+1}(\alpha)}{q_n(\alpha)},
$$

not $\limsup \ln q_{n+1}/\ln q_n$. See
[rotations/10-MARTINIS-BRIEF.md](rotations/10-MARTINIS-BRIEF.md)
§"The Arithmetic Parameter" for the source-extraction note. Any finite
irrationality measure $|\alpha-p/q|\ge c q^{-C}$ forces
$\beta(\alpha)=0$: applying the lower bound to convergents gives
$q_{n+1}\le c^{-1}q_n^{C-1}$, hence
$\ln q_{n+1}/q_n\to 0$. Existing irrationality-measure results for $\pi$
therefore place $\pi$ on the $\beta=0$ / Diophantine side in this
classification. This does not close the memo's target; it only fixes the
arithmetic side on which any K-H-L-A effective constant must live.

**L–W-safety tags** (per `memos/LINDEMANN-BRIEF.md` §"Exit criteria"):

| Ingredient | Source | Tag |
|---|---|---|
| Archimedean squeeze | Archimedes, ~250 BCE | Pre-L–W |
| Cyclotomic degree $\varphi(2n)/2$ | Gauss, cyclotomic theory | Pre-L–W |
| Hurwitz Fourier-isoperimetric identity | Hurwitz 1902 | Pre-L–W methodologically (no transcendence input) |
| Liouville lower bound on algebraic-integer heights | Liouville 1844 | Pre-L–W (predates Hermite 1873 by 29 years) |
| Aitchison Poisson-summation density bound | Aitchison 1959 | Post-L–W chronologically, pure Fourier/Parseval methodologically |
| Erdős–Turán / Koksma discrepancy-sum | E-T 1948, Koksma 1950s | Post-L–W chronologically, pure Fourier/Weyl methodologically |

**If** every step stays inside these tools, the argument is strictly pre-L–W in lineage. That is the novelty claim, not any numerical tightness. A pre-L–W proof of transcendence of $\pi$ with any effective rate would be a rewriting result; if the rate is competitive with Salikhov, it is also a transcendence-theory result.

**What's open.**

- Whether the Liouville-height step generalizes to the joint cyclotomic $\times \mathbb{Q}(\pi)$ field without silent upgrade to Baker / Gelfond–Schneider. This is the place to audit carefully.
- Whether a tight **heightwise** version of Liouville exists at the joint field — or whether the honest next step is Feldman's 1960 effective Liouville (which uses Padé approximants; see Landfall §4's "Padé Ghost" for a related flavor) or something similar pre-Baker.
- Whether the full rate is vacuous ($C = \infty$) because the Archimedean gap $1/n^2$ and the cyclotomic height $\exp(O(n))$ misalign. If so, the memo ends in (3) below: a circularity-free negative result, which is still informative as a lineage check.

---

## Adjacent anchors

- [sources/landfall.pdf](sources/landfall.pdf) — §5 Kraft machinery is the log-side template this memo transposes; §4 is the log-side pointwise transcendence statement ($\varepsilon(k/2^p)$ transcendental, via Gelfond–Schneider — noting the asymmetry: the log side uses post-L–W machinery for its pointwise statement, while this memo hopes to avoid it on the circle side). See [fft/LANDFALL-PROOF-TEMPLATES.md](fft/LANDFALL-PROOF-TEMPLATES.md) for the slim proof-template extract.
- [memos/LINDEMANN-BRIEF.md](memos/LINDEMANN-BRIEF.md) — the circularity map. Every step of this memo's argument has to be tagged per that brief's §"Exit criteria" classification (pre-L–W / background / essential / circular).
- [rotations/3DT-BRIEF.md](rotations/3DT-BRIEF.md) — Lefèvre–Muller 1998 use 3DT for table-maker's-dilemma worst-case filtering; that is the log-side precedent for "Kraft + Diophantine arguments on a rotation orbit." Structurally parallel to what this memo wants on the circle side.
- [rotations/CONTINUED-FRACTIONS-CROSSWALK.md](rotations/CONTINUED-FRACTIONS-CROSSWALK.md) — the continued-fraction convergents of $\pi$ are the arithmetic substrate under the Archimedean polygon approximation; the crosswalk now supplies six indexed perspectives on this substrate and logs this K-H-L-A branch as the effective-transcendence perspective.
- [memos/LOWER-BOUND-COUNTRY.md](memos/LOWER-BOUND-COUNTRY.md) — the symmetric partner to `memos/RAMANUJANS-COMPLIMENT.md`; the complexity-theoretic reading queue. If this memo's argument lands as a compute-cost lower bound rather than a transcendence measure, promotion target is there.
- [corners/PSEUDO-CHEBYSHEV-NODES.md](corners/PSEUDO-CHEBYSHEV-NODES.md) — circle-side algebraic-depth catalog: $\cos(\pi/n)$ of degree $\varphi(2n)/2$, first non-constructible at $n=7$. These are the polygon vertices in (C).
- [corners/CIRCLE-TRANSFORMATIONS.md](corners/CIRCLE-TRANSFORMATIONS.md) §4 Leash framework — the tightness–informativeness tradeoff is the framework for what Hurwitz's extremum condition is buying: the Fourier-support condition is the tightest possible leash on a planar simple closed curve.
- [BNHA/SirNighteye/DONT-BELIEVE-ME-JUST-WATCH.md](BNHA/SirNighteye/DONT-BELIEVE-ME-JUST-WATCH.md) — disanalogies D1 (algebraic vs transcendental characters) and D4 (finite vs infinite character group) are what distinguish the unit-circle Fourier side (where Hurwitz's identity is exact) from the log-binade-circle Fourier side (where the Fourier tail at $O(1/n^2)$ never terminates). This memo lives entirely on the unit-circle side, and the disanalogies are what make the circle side available to the argument while the log side is not.
- [fft/GOLDSTINE-1977-INTERPOLATION-BRIEF.md](fft/GOLDSTINE-1977-INTERPOLATION-BRIEF.md) — Goldstine §4.12 exposition of Gauss 1805 (*Theoria interpolationis*): pre-1882 trigonometric Lagrange interpolation, two product-to-sum lemmas (Euler 1748 §240 anchor, Gauss 1805), discrete Fourier inversion, aliasing identity, divide-and-conquer subdivision. §8 names three KHLA leads now folded back into this memo: discrete inversion as exact polygon-corner empirical-to-density bridge (§(A) above); Gauss-aliasing as discrete dual to the Fourier-support condition (§(B) hazard 4); sine-product cancellation as candidate replacement small algebraic quantity (§"Proposed order of work" 6b). (A9) of [memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md) is the audit row.
- [memos/EULER-1768-INTEGRAL-BRIEF.md](memos/EULER-1768-INTEGRAL-BRIEF.md) — direct read of Euler 1768 *Institutiones calculi integralis* Vol 1 (E342, [sources/euler-1768-institutiones-calculi-integralis-vol1.pdf](sources/euler-1768-institutiones-calculi-integralis-vol1.pdf)). Settles the §"Proposed order of work" 6b audit-target migration: the sine-product cancellation candidate's Vol 1 anchor is **Beta-reflection at rational arguments** (Cap. VIII §352), not the log-sin integral. Wallis even/odd integral parity (§330-331) and Wallis-pair cancellation (§332-334) flagged as collateral pre-1882 anchors. The original `π log 2` audit attribution is reported misscoped (the log-sin identity is not in Vol 1).
- [memos/EULER-1794-SUPPLEMENT-BRIEF.md](memos/EULER-1794-SUPPLEMENT-BRIEF.md) — direct read of Euler Vol IV *Supplementum* (originally 1794, *editio tertia* 1845, [sources/euler-1794-institutiones-calculi-integralis-vol4-supplementum.pdf](sources/euler-1794-institutiones-calculi-integralis-vol4-supplementum.pdf)). Re-attaches the `π log 2` audit thread to its proper Vol IV source: Supplementum V §51 contains the Fourier series $\sum_{k\ge 1}\cos(ku)/k = -\log(2\sin(u/2))$ (originally Novi Commentarii XIX, ~1774), from which $\int_0^\pi \log\sin u\,du = -\pi\log 2$ follows in one elementary step. Constant-determination method attributed by Euler to **Daniel Bernoulli**. The two Euler briefs together pin both KHLA branch (i) audit anchors (Beta-reflection and log-sin) to verified pre-1882 sources.
- `sources/A Statistical Theory of Remnants.pdf` — Aitchison 1959, JRSS B 21(1). Equations (2.2), (2.3), and the $k$-dim (6.3), (6.8) are the density-side Fourier bounds.
- `sources/K-N-Chapter2.pdf` — Kuipers–Niederreiter 1974, *Uniform Distribution of Sequences*, Ch. 2. Theorems 2.5 (Erdős–Turán), 3.2 / 3.4 (type-based bounds on $(n\alpha) \bmod 1$), Example 3.1 (Thue–Siegel–Roth as type 1 for algebraic irrationals), and the multi-dim Erdős–Turán–Koksma on p. 116.
- `sources/the table maker's dilemma.pdf` — Lefèvre–Muller–Tisserand 1998. §2.2.1 is the 3DT-based filter already extracted into `rotations/3DT-BRIEF.md`; the implicit Kraft accounting on worst-case bits is the log-side template.

**Anchors yet to be written:**

- Possibly `memos/HURWITZ-ISOPERIMETRIC-BRIEF.md` — a focused source extraction of Hurwitz 1902, "Sur le problème des isopérimètres" (*Comptes Rendus*) and/or the later expository version in Hurwitz–Courant, for the Fourier-support-condition-at-extremum statement. For now, the necessary content lives inside this memo's §(B).
- Possibly `memos/LIOUVILLE-1844-BRIEF.md` — Liouville's original transcendence-from-height theorem. Would be the canonical pre-Hermite reference and clarify exactly which statements about algebraic-integer heights are available without invoking post-L–W machinery.

---

## Pairing

Five neighboring literatures converge here, and none is the center:

- **Classical transcendence theory** (Liouville 1844, Hermite 1873, Lindemann 1882, Weierstrass 1885, Mahler 1953, Baker 1966, Feldman, Waldschmidt, Nesterenko, Salikhov 2008). Landscape this memo is trying to re-derive a single piece of, pre-L–W.
- **Uniform distribution / discrepancy theory** (Weyl 1916, van der Corput, Koksma, Erdős–Turán 1948, Kuipers–Niederreiter 1974). The Fourier-budget side.
- **Information theory / Kraft accounting** (Kraft 1949, Shannon 1948, Chaitin 1966–75). The Kraft vocabulary; already in use in Landfall §5 (`sources/landfall.pdf`).
- **Fourier-analytic isoperimetry** (Hurwitz 1902, Polya–Szegő 1951, Osserman 1978). The Dido extremum in Parseval form.
- **Table-maker's dilemma** (Muller 1997, Lefèvre–Muller 1998, Brent–Zimmermann 2010). The log-side Kraft-+-Diophantine template; see `rotations/3DT-BRIEF.md`.

The memo's discipline: the argument must be constructible from pieces in at least three of these five, with the fourth and fifth entering as background at most. If the argument ends up living entirely inside classical transcendence theory, the program has not done anything new. If it ends up living entirely inside Fourier analysis, the effective rate is probably vacuous. The sweet spot is what the memo is betting on.

---

## Hazards

Four failure modes worth naming in advance so a directed attempt can detect them:

1. **Dido route is classical Hermite–Lindemann in disguise.** Hermite's auxiliary $f(x) e^{-x}$ is a specific Schwartz test function on the line; the polygon-vs-circle gap is a specific Schwartz-adjacent test "function" on the torus (really a Parseval identity). Both are "smooth approximators to a delta at the algebraic point of interest." If the Hurwitz-extremum auxiliary reduces to Hermite's after a Poisson-summation change of variable, the memo has produced a pedagogical reframing — still useful but not the program's target. Check: is the polygon's Fourier tail at $\{k \equiv \pm 1 \pmod n\}$ the Poisson dual of Hermite's $f(x) e^{-x}$ for some choice of $f$? If yes, promote to a different kind of memo. The same hazard inherits to the sine-product and Gauss-aliasing reformulations of [fft/GOLDSTINE-1977-INTERPOLATION-BRIEF.md](fft/GOLDSTINE-1977-INTERPOLATION-BRIEF.md) §8: whether the discrete identities collapse to Hermite's auxiliary under Poisson summation is the same check, restated in the discrete register.

2. **Liouville-height step routes through L–W.** When extending Liouville's 1844 bound to the joint cyclotomic $\times \mathbb{Q}(\pi)$ field, the natural sharpening invokes Baker 1966 (linear forms in logs) or Gelfond–Schneider 1934. Any such invocation is a **circularity signal** (see `memos/LINDEMANN-BRIEF.md` §"When invoking L–W is strictly circular"); if the argument needs it essentially, the memo documents a negative lineage result and closes.

3. **Effective rate is vacuous.** If the Kraft–Parseval budget yields $|q\pi - p| \ge c\, q^{-C}$ with $C = \infty$ or $c = 0$, the argument has produced a qualitative statement, not an effective one. Salikhov 7.6 is the benchmark; any finite $C$ with explicit $c$ is a valid effective statement; but a pre-L–W argument with $C = \infty$ is just transcendence of $\pi$ reproved in new language, and may or may not be interesting depending on how short the proof is.

4. **Fourier-support condition isn't Kraft-compatible.** The Hurwitz extremum $c_n = 0$ for $|n| \ne 1$ is a linear condition on an infinite-dimensional space. Encoding it as a prefix-free Kraft description may not be possible without already knowing something strong about $\pi$ (implicit circularity). Watch for this at the (B) → (C) handoff: the prefix-free encoding of the support condition must not smuggle in a transcendence input.

A directed attempt on any of (A)–(D) should close with a sentence of form

> *"Under assumption X, the Kraft–Parseval budget yields $C \le Y$, with L–W-safety tag Z."*

All three named. Analog of the Ramanujan-memo and lower-bound-country memo discipline.

---

## What this is not

- **Not a proof.** The Kraft–Parseval budget is known; the Hurwitz extremum is known; Aitchison and E-T-K are known. The memo scopes whether they combine into a pre-L–W transcendence proof — the combination is the open question.
- **Not a commitment to outperforming classical Hermite–Lindemann.** A pre-L–W Kraft-accounted proof with effective rate weaker than Salikhov is still a useful deliverable if the lineage is clean. The rewrite value is in the proof structure, not the numeric.
- **Not a replacement for the full Lindemann–Weierstrass at $n \ge 2$.** `memos/LINDEMANN-BRIEF.md` and the user's framing in the KRAFT discussion both flag that the subspace theorem is the genuine gate for $n \ge 2$. This memo handles only the $n=1$ case; the $n \ge 2$ case is a separate search.
- **Not a compute-cost lower bound in the sense of `memos/COUNTING-APPARATUS.md`.** The bind there is about primitive-op floors in a fixed compute model. This memo is about Diophantine rates with effective constants. The two overlap in vocabulary (Kraft, Parseval, dual lattice) but not in target. If the argument here lands, it feeds (A) and (C) of that search rather than subsuming them.
- **Not a treatment of transcendence of $e$.** The $n=1$ case of H–L covers both $e$ and $\pi$, but the Dido hook is specific to $\pi$ (it's a statement about the circle). The analogous hook for $e$ would probably want a different extremum characterization — perhaps $e$ as the unique $a$ for which $\frac{d}{dx} a^x = a^x$, i.e., a differential-equation extremum rather than an isoperimetric one. Out of scope here.

---

## Proposed order of work

Ranked from least load-bearing / fastest to check toward the real research bottleneck, following the pattern of `memos/COUNTING-APPARATUS.md` §"Proposed order of work":

1. **~~(B), explicit Fourier coefficients of the regular $n$-gon.~~** ✅ **Closed.** `corners/hurwitz_gap.sage` derives $c_m^{(n)} = L_n^2/(4\pi^2 m^2) \cdot \mathbb{1}[m \equiv 1 \pmod n]$ from the tangent-field geometric sum.
2. **~~(B), Hurwitz identity closure check.~~** ✅ **Closed.** The same script verifies $\Delta_n = L_n^2 - 4\pi A_n = L_n^2(1 - (\pi/n)\cot(\pi/n))$ against the Parseval sum, matching to machine precision for the closed-form identity and to $1.5 \times 10^{-3}$ relative for the $|j| \le 400$ truncation (uniformly in $n$). Archimedean asymptote $\Delta_n = 4\pi^4/(3n^2)$ verified (`figures/hurwitz_gap_rate.png`); frequency-band concentration visible (`figures/hurwitz_gap_frequency_decomposition.png`).
3. **~~(A/B), first-band concentration theorem.~~** ✅ **Closed.** [corners/HURWITZ-FIRST-BAND-CONCENTRATION.md](corners/HURWITZ-FIRST-BAND-CONCENTRATION.md) derives the paired-band closed form $B_j(n)$, proves $B_j(n) \le B_1(n)/j^2$, concludes the sharp uniform bound $B_1(n) \ge (6/\pi^2)\Delta_n$, and adds the dyadic-shell estimate $\sum_{2^r \le j < 2^{r+1}} B_j(n) \le 2^{-r} B_1(n)$.
4. **~~(A), Kraft-constant consolidation.~~** ✅ **Closed.** [memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md](memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md) now contains the exact weighted one-dimensional lemma, its dyadic-shell corollary, and the Fortnow-consolidated corollary at cutoff `m = 2^R - 1`, all under the explicitly stated empirical-to-density proxy. The honest Aitchison-facing shell is the paired shell `L_r^(pair)(n)`, and every front constant is sourced.
5. **(D), L–W-safety audit on a drafted argument — now the only live transcendence path.** With Step 6b closed negative-pending-counterexample (Baker-circularity, see below), the discrepancy/Aitchison branch is the only remaining transcendence route, and Step 5 — previously deferred — is now urgent. Specifically: take the one-dimensional bookkeeping in [memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md](memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md) and tag every step that uses a type-1 / Roth 1955 input. The KHLA budget already discriminates algebraic from transcendental $\alpha$ only *through* the type (per §(A) "What remains open"), and that input is post-L-W as flagged in [AGENTS.md](AGENTS.md) "Old-time religion." The audit asks: can the empirical-to-density proxy + the Erdős-Turán-Koksma budget run on **Liouville-1844-only inputs** (giving weaker type-$d$ bounds on degree-$d$ algebraic irrationals, possibly still adequate to detect $(n\pi) \bmod 1$ as discrepancy-anomalous), or does the budget need Roth essentially? If Liouville-only suffices, the discrepancy branch survives and produces a pre-L-W deliverable. If Roth is essential, the discrepancy branch closes negative on provenance — same shape as the Liouville endgame failure at Step 6b — and the whole memo freezes per Exit criterion 3. Run with the Goldstine §3 polygon-corner-exact reduction in hand: the proxy now has to cover only polygon → orbit drift, which narrows the audit's surface area.
6. **~~(C), naive Liouville auxiliary-free replacement on the polygon gap.~~** ❌ **Closed negative.** [memos/LIOUVILLE-SCALE-TEST.md](memos/LIOUVILLE-SCALE-TEST.md) reduces the inscribed gap, circumscribed/radial-lift gap, and strip `H^1` seminorm to `alpha_n - pi` with `alpha_n = n tan(pi/n)`, then shows `alpha_n` has exponential cyclotomic height. Liouville cannot collide with the `1/n^2` Archimedean upper bound.
6b. **~~(C/D), replacement endgame via Euler-identity-mediated Liouville.~~** ❌ **Closed negative-pending-counterexample (Baker-circularity).** The two pre-1882 anchors located by [memos/EULER-1768-INTEGRAL-BRIEF.md](memos/EULER-1768-INTEGRAL-BRIEF.md) and [memos/EULER-1794-SUPPLEMENT-BRIEF.md](memos/EULER-1794-SUPPLEMENT-BRIEF.md) — Beta-reflection at rational arguments and the log-sin Fourier series — are derivation-clean (Mercator + Bernoulli-Euler trigonometry, no transcendence input), but their *use* in a Liouville-style argument routes the effective Diophantine extraction through linear forms in logarithms. Sketch: any natural construction that brings $\pi$ in Archimedeanly via these identities produces approximants in a multi-transcendental field (`Q(π, log 2)` for the log-sin route, `Q(log α_i, arctan α_j)` for the Beta-reflection truncation route). Liouville 1844 is a one-transcendental tool. The compression from multi- back to one-transcendental is exactly what Baker 1966-67 does on linear forms in logarithms, and Baker uses Gelfond-Schneider essentially (post-L-W). So the natural use of these anchors invites Baker-circularity — using L-W-machinery to reprove an L-W statement. The closure is **not** unconditional: it stands "until a one-transcendental construction is found" (sine-product cancellation gestures at this — purely algebraic, no $\log 2$ exposure — but the Liouville scale test on $\alpha_n = n\tan(\pi/n)$ already showed the obvious cyclotomic-only candidates die on height; nothing is currently on the page that survives). Sine-product cancellation as a candidate is preserved at (A8) of [memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md) for any future cyclotomic-only construction; promotion to attempt requires demonstrating it does not reintroduce $\log 2$ via Riemann sums or asymptotic expansions.
7. **(D), effective-rate extraction.** Read off $c, C$; compare against Salikhov 7.6.

Optional follow-on to steps 1–2: **circumscribed counterpart**. `corners/hurwitz_gap_circumscribed.sage` would do the same for the circumscribed regular $n$-gon ($L_n^{\text{circ}} = 2n \tan(\pi/n)$, $A_n^{\text{circ}} = n \tan(\pi/n)$). The Archimedean squeeze uses both sides, and the E-T-K $\times$ Aitchison Kraft budget wants the inscribed $+$ circumscribed sum. Not yet built.

Promotion out of this doc: when (A), (B), (C), (D) combine to produce an effective statement with a clean L–W-safety tagging, the combined result promotes to a standalone writeup. Alternatively, if step 3 or 5 fails, the memo freezes as a lineage-check record and the finding migrates into `memos/LINDEMANN-BRIEF.md` §"Post-Lindemann tools."

---

## Exit criteria

The memo freezes and promotes when any one of the following triggers:

1. **Effective rate derived with L–W-safety tag.** Item (D) produces $|q\pi - p| \ge c\, q^{-C}$ with explicit $c, C$ and all steps tagged per `memos/LINDEMANN-BRIEF.md` §"Exit criteria." Promote the argument to a standalone writeup.

2. **Dido route collapses to Hermite's auxiliary.** Item (C) shows the polygon-vs-circle gap is Hermite's $\int_0^t e^{-x} f(x) dx$ under Poisson-summation change of variable. The memo becomes a pedagogical note; promote to `memos/HERMITE-AS-DIDO-BRIEF.md` and close the search.

3. **Liouville-height step fails on scale or provenance.** The natural
   polygon-gap version has already failed on scale at
   [memos/LIOUVILLE-SCALE-TEST.md](memos/LIOUVILLE-SCALE-TEST.md). If every
   replacement endgame either repeats that scale failure or requires
   Baker / Gelfond-Schneider essentially, the memo becomes a negative
   lineage record and closes.

4. **Two directed attempts at steps 1–6 of §"Proposed order of work" close without a tagged sentence.** Same discipline as `memos/RAMANUJANS-COMPLIMENT.md` §"When to leave" and `memos/LOWER-BOUND-COUNTRY.md` §"Exit criteria." Demote to low-priority; note findings.

---

## Status

**Speculative off-branch of the program, not a load-bearing strut.** Open search memo with **two** negative branches now recorded.

The one-dimensional program through Step 4 is on the page: the regular $n$-gon's arc-length Fourier coefficients have the clean closed form $c_m^{(n)} = L_n^2/(4\pi^2 m^2) \cdot \mathbb{1}[m \equiv 1 \pmod n]$, Hurwitz's identity matches elementary geometry, the first admissible band carries a sharp uniform proportion $6/\pi^2$ of the whole gap, the honest Aitchison-facing shell has been identified exactly, Fortnow has been pulled back to the exact paired-shell semimeasure, and the final one-dimensional bookkeeping lemma is written down under the empirical-to-density proxy.

**Two negative closures on the transcendence side:**
1. The naive Liouville endgame on the polygon gap is closed negative by [memos/LIOUVILLE-SCALE-TEST.md](memos/LIOUVILLE-SCALE-TEST.md) (exponential cyclotomic height of $\alpha_n = n\tan(\pi/n)$ misses $1/n^2$ Archimedean rate).
2. The Euler-identity-mediated Liouville endgame (Step 6b) is closed negative-pending-counterexample (Baker-circularity: the natural use of Vol 1 §352 Beta-reflection or Vol IV Supp V §51 log-sin Fourier series routes through linear forms in logarithms, which is Baker 1966-67 and uses L-W essentially).

**One live transcendence branch remaining:** the discrepancy/Aitchison endgame via the empirical-to-density proxy. Step 5 has been promoted to live target: the audit asks whether the Erdős-Turán-Koksma budget on $(n\pi)\bmod 1$ can run on Liouville-1844-only inputs (pre-1882-safe) or needs Roth 1955 essentially (post-L-W, same circularity shape as Step 6b). The polygon corner of the proxy is now exact (Goldstine §3 discrete Fourier inversion), so the audit surface is narrowed to polygon → orbit drift.

**Program-level posture.** With both Liouville-style endgames closed negative, KHLA is no longer a candidate load-bearing strut for the program's triadic lower-bound theorem. It is now treated as a speculative off-branch: the structural results in §(B) Hurwitz–Dido and §(A) Kraft-Parseval budget remain valuable as methodology, the [fft/GOLDSTINE-1977-INTERPOLATION-BRIEF.md](fft/GOLDSTINE-1977-INTERPOLATION-BRIEF.md), [memos/EULER-1768-INTEGRAL-BRIEF.md](memos/EULER-1768-INTEGRAL-BRIEF.md), and [memos/EULER-1794-SUPPLEMENT-BRIEF.md](memos/EULER-1794-SUPPLEMENT-BRIEF.md) anchors remain valid pre-1882 sources for whatever future cyclotomic-only construction may emerge, and Step 5 if it closes positive could revive the branch. But the program's center of gravity has shifted to the closure-depth no-go (in hand) and the compute-cost lower bound ([memos/LEDGER-PIVOT-SEARCH.md](memos/LEDGER-PIVOT-SEARCH.md), [fft/FOUR-FRAMEWORK-SYNTHESIS.md](fft/FOUR-FRAMEWORK-SYNTHESIS.md)) as the load-bearing struts.

Hurwitz 1902 has still not been sourced into the repo; `memos/HURWITZ-ISOPERIMETRIC-BRIEF.md` remains a candidate anchor-to-be-written if the structural results promote independently.
