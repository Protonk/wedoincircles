# GOLDSTINE-1977-INTERPOLATION-BRIEF

Source-extraction memo on Herman H. Goldstine, *A History of Numerical
Analysis from the 16th Through the 19th Century* (Springer-Verlag, 1977),
§4.12 "Gauss on Interpolation" (pp. 233-258) and the opening of §4.13
"Gauss on Rounding Errors" (pp. 258ff)
([sources/gauss-interpolation.pdf](sources/gauss-interpolation.pdf)).

**Relationship to the existing FFT briefs.** The
[fft/HEIDEMAN-JOHNSON-BURRUS-1985-BRIEF.md](fft/HEIDEMAN-JOHNSON-BURRUS-1985-BRIEF.md)
covers HJB's 1985 historiographical paper, which cites Goldstine 1977
as its reference [9] for the English exposition of Gauss's manuscript
*Theoria interpolationis methodo nova tractata* (Werke III, pp. 265-327).
This brief reads Goldstine §4.12-13 *directly*. Where HJB85 selectively
quotes Articles 19-20 and 25-28 of Gauss's manuscript through the lens
of "is this Cooley-Tukey?", Goldstine walks Sections 1-41 of Gauss's
paper through, expanding the algebraic interior. The two briefs do not
duplicate: HJB85 is the chain-of-custody record; this is the technical
exposition the program inherits at the 1805 endpoint.

**Why this brief exists.** Two reading lenses, requested by the program:

- **L1 — FFT memo branch.** What computational primitives did Gauss
  explicitly identify in 1805? Goldstine reproduces Gauss's algorithmic
  decomposition with a worked numerical example (Pallas data,
  pp. 251-253) and three pre-1882 product-to-sum identities (the two
  lemmas at p. 245 plus the aliasing identity at p. 248) that the
  modern complexity briefs do not name.

- **L2 — KHLA branch.** Does Goldstine's exposition give us pre-1882
  weapons usable for
  [memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md](memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md)?
  Relevant content is the trigonometric-Lagrange interpolation formula
  (Goldstine eq. 4.61), the aliasing identity (p. 248), and the two
  product-to-sum lemmas (p. 245), all strictly pre-1882 in lineage.
  Whether they translate to KHLA's (B) → (C) handoff is an inferred
  question, flagged as such.

**What was read.** All 26 pages of the PDF, covering Goldstine §4.12 in
full plus the opening pages of §4.13. Identities are checked from
Goldstine's formulas; Gauss's original (Werke III, pp. 265-327) is not
in the repo and is not independently consulted.

**Confidence level.** High on the structural content of Gauss 1805 as
Goldstine presents it (interpolation formula, two product-to-sum
lemmas, aliasing identity, divide-and-conquer subdivision, Pallas
worked example, rounding-error stance in *Theoria Motus*). Medium on
program import: the L2 lens reads possibilities into the source that
Goldstine does not name as such.

**Trust boundary up front.** Goldstine is exposing Gauss; the brief is
exposing Goldstine. Two layers of indirection between us and the 1805
manuscript. Where Goldstine attributes a step to Gauss ("Gauss now
examined ...", "Gauss next forms ..."), the brief preserves the
attribution. Goldstine's own commentary — the framing of §4.13 as
"numerical stability," the equation numbering 4.58-4.68, the
parenthetical "(This is the Lagrange formula.)" at p. 237 — is flagged
as Goldstine's, not Gauss's.

---

## 1. The Substrate: Lagrange Interpolation Reframed (Goldstine pp. 233-237)

Gauss's "first problem" (Goldstine p. 233): given `m` quantities
`a, b, c, d, ...`, compute the sum
`S^n = α a^n + β b^n + γ c^n + δ d^n + ...`,
where `α, β, γ, δ` are the partial-fraction weights

```
α = 1 / [(a-b)(a-c)(a-d)···],   β = 1 / [(b-a)(b-c)(b-d)···],   etc.
```

Form `P = α/(1-ax) + β/(1-bx) + γ/(1-cx) + ...` and `Q = (1-ax)(1-bx)···`.
Gauss's identity (Goldstine p. 233): `PQ = x^{m-1}`. Series-expanding
gives `S^0 = S^1 = ··· = S^{m-2} = 0`, `S^{m-1} = 1`, `S^m = A` where
`A = a + b + c + ···`, and recurrences for higher `S^{m+k}`.

Goldstine's footnote 80 (p. 233): "The problem just mentioned was first
treated by Euler in his *Inst. Calc. Integr.*, *Opera*, Vol. II, p. 432.
He showed there that `S^0 = S^1 = ··· = S^{m-2} = 0`."

Gauss next *substitutes* the abscissae with complex unit phasors
(Goldstine p. 234): replace `a, b, c, ...` by `E^{ia}, E^{ib}, E^{ic}, ...`
and `E^{-ia}, E^{-ib}, ...`, where `E` is the base of the natural
logarithms and `i = √-1`. Forms two `S^n`-style sums (one for each sign);
calls them `S^n` and `T^n`. Then

```
½(S^n + T^n) = 0       for n = 0, 1, ..., m-2,
             = 1       for n = m-1,
             = cos a + cos b + cos c + ···   for n = m;
(S^n - T^n)/(2i) = 0   for n = 0, 1, ..., m-1,
                = sin a + sin b + sin c + ···   for n = m.
```

The trigonometric form (Goldstine pp. 235-236) introduces auxiliary
functions `U^λ, V^λ` indexed by `λ = n + 1 - m/2`. The case analysis
splits on parity of `m`. The output is the **trigonometric Lagrange
formula** (Goldstine eq. 4.59 first, then eq. 4.61 in trig form):

```
                       sin ½(t-b) sin ½(t-c) sin ½(t-d)···
T = Σ_a A_a · ─────────────────────────────────────────────────
                       sin ½(a-b) sin ½(a-c) sin ½(a-d)···
```

Goldstine's parenthetical (p. 237): "(This is the Lagrange formula.)" —
he is identifying the algebraic version with Lagrange interpolation. The
trigonometric version is Gauss's own (Goldstine eq. 4.61).

**For the program.** Lagrange's interpolation formula is 1759-1762; the
trigonometric version is Gauss 1805. Both are pre-Liouville (1844),
pre-Hermite (1873), pre-Lindemann (1882). The mechanism by which Gauss
reaches the trigonometric form — substitution of `a → E^{ia}` into a
Lagrange identity over `Q` — is a *circle-arithmetic* derivation that
uses no transcendence input. It is methodologically pre-1882 even where
the names that survive (`E`, `i`) read modern.

---

## 2. The Two Pre-1882 Product-to-Sum Lemmas (Goldstine p. 245)

Goldstine reproduces, with Gauss-attribution, two identities that the
modern FFT-complexity briefs do not name. Both are stated for
`a, b, c, d, ...` being `μ` arcs in arithmetic progression with common
difference `360°/μ`, i.e., the angular vertices of a regular `μ`-gon.

**Lemma 1.** `P = sin ½(t-a) sin ½(t-b) sin ½(t-c) ···` (a product over
the `μ` vertices) satisfies

```
P = ∓ sin ½μ(t-a) / 2^{μ-1},
```

with the upper sign for `μ` even and the lower for `μ` odd. Goldstine's
attribution (p. 245): "Gauss remarks that this follows from a related
result of Euler (*Introd. in Anal. Inf.*, I, Section 240, *Opera Omnia*,
Vol. VIII) which says that

```
sin nz = 2^{n-1} sin z · sin(π/n - z) · sin(π/n + z) · sin(2π/n - z) · ···
```

**Lemma 2.** Under the same hypothesis on `a, b, c, d, ...`,

```
(cos t - cos a)(cos t - cos b)(cos t - cos c)··· = (cos μt - cos μa) / 2^{μ-1}.
```

Goldstine's proof sketch (p. 245-246): write
`cos t - cos a = 2 sin ½(t-a) sin ½(-t-a)` etc., apply Lemma 1 to the two
half-angle products, multiply.

**For the program.** These are the closed-form factorizations of
*products of polygon-vertex differences* in two natural bases (`sin`
half-angle and `cos`). Both reduce a length-`μ` product to a single
trigonometric term over `2^{μ-1}`. They are pre-1882 in lineage (the
attribution Goldstine gives is to *Introductio in Analysin Infinitorum*,
Euler 1748, Section 240). They are circle-arithmetic primitives whose
existence the program does not currently use anywhere on the circle
side. The KHLA reading in §8 below names a candidate use; this section
records only the identities and their lineage.

The endpoint/product specialization of Lemma 1 gives

```
sin(π/μ) · sin(2π/μ) · ··· · sin((μ-1)π/μ) = μ / 2^{μ-1},
```

which is the sine-product specialization of the Euler/Gauss identity
(consistent with Lemma 1 under the limit; Goldstine's exposition reaches
it via the Euler reference, not as a direct corollary). This identity says
that the product of all `μ-1` non-trivial vertex separations on the unit circle,
measured as half-chord lengths, is *rational*, equal to `μ/2^{μ-1}` —
even though each factor is algebraic of degree `~ φ(2μ)`.

---

## 3. The Discrete Fourier Inversion Formula (Goldstine pp. 246-247)

Setting `μ = 2m + 1` and applying Lemma 1 to the trigonometric Lagrange
formula (Goldstine eq. 4.61), Gauss derives the explicit Fourier
inversion (Goldstine pp. 246-247):

```
T = (1/μ)(A + B + C + D + ···)
  + (2/μ)(A cos a + B cos b + C cos c + D cos d + ···) cos t
  + (2/μ)(A sin a + B sin b + C sin c + D sin d + ···) sin t
  + (2/μ)(A cos 2a + B cos 2b + ···) cos 2t
  + (2/μ)(A sin 2a + B sin 2b + ···) sin 2t
  + ···
  + (2/μ)(A cos ma + B cos mb + ···) cos mt
  + (2/μ)(A sin ma + B sin mb + ···) sin mt.
```

This is the **discrete Fourier inversion formula** in modern terms, with
all `2m+1` coefficients written down explicitly. Goldstine: "This gives
the values of `α, α', β', β''` etc. in their well-known form" (p. 247),
i.e., the standard DFT formula.

In one direction (continuous → samples): `X(x) = α + α' cos x + α'' cos 2x
+ ··· + β' sin x + ···` evaluated at `x = a, b, c, ...` gives
`A, B, C, ...`. In the other direction (samples → continuous), the
formula above recovers all `2m+1` coefficients exactly from the `2m+1`
sample values.

**For the program.** This is the *exact* discrete-sampling theorem on
the circle, due to Gauss 1805, on a `μ = 2m + 1` equally-spaced grid.
It is the bridge between continuous arc-length Fourier coefficients
(the natural register for [corners/HURWITZ-FIRST-BAND-CONCENTRATION.md](corners/HURWITZ-FIRST-BAND-CONCENTRATION.md))
and discrete polygon-vertex evaluations (the natural register for the
KHLA Kraft budget). Pre-1882 lineage: the formula reduces to applications
of Lemma 1 (Euler 1748) to the trigonometric Lagrange identity
(Lagrange 1759-1762, Gauss 1805 in trig form).

---

## 4. The Aliasing Identity (Goldstine pp. 247-249)

Goldstine then turns to the case `μ ≠ 2m + 1`, i.e., samples fewer than
twice the highest frequency present. Suppose `X` extends to higher
modes:

```
X = α + α' cos x + ··· + α^m cos mx + α^{m+1} cos(m+1)x + α^{m+2} cos(m+2)x + ···
  + β' sin x + ··· + β^m sin mx + β^{m+1} sin(m+1)x + β^{m+2} sin(m+2)x + ···
```

Run the discrete Fourier inversion against `μ` samples at the regular
grid `a, b, c, ...`. Goldstine's eq. (after p. 247): the recovered
coefficients `γ, γ', γ'', δ', δ''` are *aliased sums*:

```
γ   = α + α^μ cos μa + α^{2μ} cos 2μa + α^{3μ} cos 3μa + ···
            + β^μ sin μa + β^{2μ} sin 2μa + β^{3μ} sin 3μa + ···,
γ'  = α' + (α^{μ-1} + α^{μ+1}) cos μa + (α^{2μ-1} + α^{2μ+1}) cos 2μa + ···
            + (β^{μ-1} - β^{μ+1}) sin μa + ···,
δ'  = β' - (β^{μ-1} - β^{μ+1}) cos μa - (β^{2μ-1} - β^{2μ+1}) cos 2μa - ···
            - (α^{μ-1} - α^{μ+1}) sin μa - ···,
···
```

(Goldstine p. 248, formulas before eq. 4.64.)

**For the program.** This is the **discrete-aliasing identity**: under
length-`μ` sampling, real-basis modes with frequencies congruent to
`±m (mod μ)` collapse onto the recovered coefficient at frequency `m`,
with the sine terms carrying the sign data shown above. It is a pre-1882
statement (Gauss 1805) of what would today be called the Poisson
summation / sampling theorem on the circle.

The aliasing structure is the **dual** of the polygon's frequency-support
condition derived in [corners/hurwitz_gap.sage](corners/hurwitz_gap.sage)
and recorded at
[corners/HURWITZ-FIRST-BAND-CONCENTRATION.md](corners/HURWITZ-FIRST-BAND-CONCENTRATION.md):
the regular `n`-gon's continuous arc-length parametrization has
`c_m^{(n)} ≠ 0` only for `m ≡ 1 (mod n)`. Both sides of the duality are
"frequency-support is congruence-class-determined under polygon-rotation
symmetry"; on the discrete-sample side it is aliasing onto a single
recovered coefficient, on the continuous-parametrization side it is
the surviving lattice in the original Fourier expansion.

---

## 5. Divide-and-Conquer with `π = μν` (Goldstine pp. 249-251)

The substrate of the FFT begins on Goldstine p. 249, with footnote 83:

> "This fascinating work of Gauss was neglected and was rediscovered by
> Cooley and Tukey in an important paper in 1965. Cf. Cooley, *CTA*,
> pp. 297-301."

(For the *historical* import of this footnote, see
[fft/HEIDEMAN-JOHNSON-BURRUS-1985-BRIEF.md](fft/HEIDEMAN-JOHNSON-BURRUS-1985-BRIEF.md)
§1 and §4. The present brief reads the *technical* content.)

**Setup (Goldstine p. 249).** Let `π = μν`. The total set of `π` sample
abscissae splits into `ν` groups of `μ` terms each, each group itself an
arithmetic progression with common difference `360°/μ`:

```
group 1:  a,  b,  c,  d, ...      (μ terms, step 360°/μ, anchor a)
group 2:  a', b', c', d', ...     (anchor a' = a + 360°/π)
group 3:  a'', b'', c'', d'', ... (anchor a'' = a + 2·360°/π)
···
group ν                           (anchor a^{(ν-1)} = a + (ν-1)·360°/π)
```

**Inner pass (length-`μ` Fourier per group).** Each group is treated as
an independent length-`μ` discrete Fourier expansion via the formula in
§3 above. This produces, for each group `g ∈ {1, ..., ν}`, a vector of
Fourier coefficients `γ_g, γ'_g, γ''_g, ..., δ'_g, δ''_g, ...`.

**Combine pass (length-`ν` Fourier across groups).** The inner-pass
coefficients `γ, γ', δ', ...` themselves vary with the group's anchor,
i.e., are functions of `y = μa^{(g-1)}`. Each is treated as a periodic
function of `y` and Fourier-expanded *again* at length `ν`. Goldstine's
narration (p. 250):

> "Gauss imagines that the coefficients `γ, γ', δ',` etc. in
> `X' = γ + γ' cos x + γ'' cos 2x + ··· + δ' sin x + δ'' sin 2x + ···`
> are themselves variable, as we shall see."

He sets up new variables `y = μa, y = μa', y = μa''`, etc. — `ν` values
of `y` arising from the `ν` group anchors — and Fourier-expands the
coefficient-functions at this length.

**Algebraic verification of the two factorizations.** Goldstine pp. 250-251
walks the case analysis on parities of `μ` and `ν`. The output is that
the two-stage decomposition exactly reproduces the direct length-`π`
Fourier expansion, with consistency guaranteed by the case-by-case
matching of "last terms" and modular arithmetic in the indices.

**The Pallas worked example (Goldstine pp. 251-253).** Gauss applied
the algorithm to `π = 12` equally spaced declination measurements of the
asteroid Pallas, taken from Baron von Zach's tables. Two factorizations
worked side-by-side:

- Case (II) of Goldstine's catalog: `μ = 4, ν = 3`. Twelve samples
  partitioned into 3 groups of 4 (anchors at 0°, 30°, 60°). Each group
  yields a length-4 Fourier expansion (pp. 251-252, three rows of
  numerical coefficients `γ, γ', δ', γ'', δ''`). Gauss then expands each
  coefficient as a periodic function of `y = 4x` (length-3 outer DFT),
  combining to a length-12 Fourier series.
- Case (III) of Goldstine's catalog: `μ = 3, ν = 4`. Same 12 samples,
  partitioned into 4 groups of 3 (Goldstine p. 252 bottom — p. 253).
  Same length-12 Fourier series recovered, modulo the "harmless"
  reflections `cos(7x) ≡ cos(5x)`, `sin(7x) ≡ -sin(5x)` on the
  12-point grid (p. 253).
  Goldstine: "the form above becomes identical to the previous one for
  all 12 values of `x` given in von Zach's table" (p. 253).

The second-form Pallas expansion (Goldstine p. 253), before reducing the
`7x` aliases to the previous form, is:

```
X = 780.6 - 411.0 cos x - 720.2 sin x + 43.4 cos 2x - 2.2 sin 2x
        - 4.3 cos 3x + 5.5 sin 3x - 1.1 cos 4x - 1.0 sin 4x
        + 0.15 cos 5x - 0.15 sin 5x + 0.1 cos 6x + 0.15 cos 7x + 0.15 sin 7x.
```

(Goldstine reports a sign correction at `α' = 411.0` per the original
Werke III p. 310; footnote 84.)

**For the program.** This is the FFT divide-and-conquer at length 12,
fully worked, in 1805. It is the upstream technical content the four
modern complexity briefs in `fft/` sit downstream of. Pre-1882 lineage
is clean: the construction uses Lemma 1 (Euler 1748) and the discrete
Fourier inversion (§3 above, also pre-1882). Goldstine reports no
operation count, and Gauss did not give one — this is consistent with
HJB85's verdict that "He did not, however, go on to quantify the
computational requirements of his method to obtain the now familiar
`N · Σ N_i` or `N log N` expressions" (HJB85 p. 271, quoted at
[fft/HEIDEMAN-JOHNSON-BURRUS-1985-BRIEF.md](fft/HEIDEMAN-JOHNSON-BURRUS-1985-BRIEF.md)
§1).

---

## 6. Gauss on Rounding Errors (Goldstine pp. 258-end of segment read)

Goldstine §4.13 opens (p. 258):

> "Gauss in the *Theoria Motus* discusses the problem of rounding errors
> as they affect the accuracy of a numerical calculation. As far as I
> can tell from the works of authors I have examined, he appears to have
> been the first to do this systematically: he also seems to have noted
> the phenomenon we now call numerical stability."

The illustration Goldstine reproduces from Gauss is the eccentric/true
anomaly relation (Goldstine eq. 4.68):

```
tan ½E = tan ½v · tan(45° - ½φ),   where cos φ = √(1 - ee).
```

`E` is the eccentric anomaly, `v` the true anomaly, `e` the orbital
eccentricity. Gauss supposes `φ` and `E` exact and analyzes how table
errors in `log tan E/2` and `log tan(45° - φ/2)` propagate.

(Footnote 86 in Goldstine: source is Gauss, *Theoria* (Eng. trans.),
p. 31. Here *Theoria* is *Theoria Motus Corporum Coelestium* (1809), a
separate work from the interpolation manuscript.)

**For the program.** This is the pre-1882 ancestor of the program's
log-side floating-point analysis in
[paper/LANDFALL-EXPORT.md](paper/LANDFALL-EXPORT.md): Gauss 1809 doing
forward error analysis under fixed-precision tables, on a transcendental
relation (the eccentric-anomaly equation). Whether the analogy carries
content beyond methodology — i.e., whether Gauss's table-error
propagation is *structurally* the same as Landfall's residue
`ε(m) = log_2(1+m) - m`, or only superficially adjacent — is an open
question for the program; the brief records only that the methodology
is in place by 1809 and is pre-1882.

---

## 7. Inferred for the Program — L1 Lens (FFT Branch)

What §4.12-13 contributes that the existing four FFT-complexity briefs
do not:

1. **Three pre-1882 product-to-sum identities** (the two lemmas at
   p. 245 and the aliasing identity at p. 248). All three are
   methodologically certified pre-1882: they trace to Euler 1748
   (Lemma 1 directly cited; Lemma 2 derived from Lemma 1) and Gauss
   1805 (aliasing identity). They are the algebraic interior the
   modern complexity briefs (Morgenstern, Winograd, Schönhage-Strassen,
   AFW) take as ambient and do not name.

2. **A worked numerical FFT at `N = 12`** with both factorizations
   (`4 × 3` and `3 × 4`) carried out and verified to give the same
   length-12 Fourier expansion (Goldstine pp. 251-253). This is the
   length-12 instance of what the modern briefs prove asymptotically.
   The program now has, at a single `N`, an end-to-end worked example
   in pre-1882 algebraic primitives, audit-ready against any modern
   FFT implementation.

3. **Gauss's algorithmic restraint.** Gauss does not count operations.
   He chooses subdivisions for *practical* (orbit-computation) reasons,
   not asymptotic ones. This is consistent with HJB85's non-citation
   chain: the absence of an asymptotic-complexity register before ~1965
   is *visible inside* Gauss 1805 as a methodological gap, not just a
   notational one. The L1 lens reads the gap as evidence that the
   modern operation-counting machinery (Morgenstern's bounded-coefficient
   linear circuits, Winograd's multiplicative complexity) is genuinely
   downstream content, not retro-fitted vocabulary on a complete 1805
   theory.

4. **A pre-1882 forward-error analysis** (§4.13, Theoria Motus 1809).
   Gauss's eccentric-anomaly equation (4.68) under table errors is the
   methodological ancestor of the program's
   [paper/LANDFALL-EXPORT.md](paper/LANDFALL-EXPORT.md) residue
   analysis. The L1 lens reads this as a clean methodological precedent
   for floating-point-style residue analysis with pre-1882 lineage.

What §4.12-13 does *not* contribute to the FFT branch:

- No operation count, asymptotic or finite. The compute-cost branch's
  questions about T1/T3, `V_cert`, certification-preserving regimes
  ([memos/LEDGER-PIVOT-SEARCH.md](memos/LEDGER-PIVOT-SEARCH.md),
  [fft/FOUR-FRAMEWORK-SYNTHESIS.md](fft/FOUR-FRAMEWORK-SYNTHESIS.md))
  are not asked or answered here.
- No lower-bound material. Gauss demonstrates an upper-bound algorithm
  by example.
- No cyclotomic-depth content. Gauss treats `K_n = Q(cos 2π/n)` only
  implicitly, through the regular grid choice.

---

## 8. Inferred for the Program — L2 Lens (KHLA Branch)

[memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md](memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md)
names two live branches: (i) finding a replacement small algebraic
quantity to substitute for `α_n = n tan(π/n)` (which died on exponential
cyclotomic height per
[memos/LIOUVILLE-SCALE-TEST.md](memos/LIOUVILLE-SCALE-TEST.md)), and
(ii) auditing the discrepancy/Aitchison endgame, with the
empirical-to-density proxy in
[memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md](memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md)
§5 as the bottleneck. Goldstine §4.12 offers candidate inputs to both
branches.

**Branch (i) lead — the Euler/Gauss sine-product identity.** From Lemma 1
(§2 above), by the standard endpoint specialization:

```
sin(π/n) · sin(2π/n) · ··· · sin((n-1)π/n) = n / 2^{n-1}.
```

Each factor `sin(π k/n)` is algebraic over `Q` of cyclotomic degree
`~ φ(2n)`; the product is *rational*. The log of the identity is

```
Σ_{k=1}^{n-1} log sin(π k/n) = log n - (n-1) log 2.
```

This is a length-`(n-1)` Riemann sum approximation to
`∫_0^π log sin θ dθ = -π log 2`: compared with the `(n-1)`-point
integral scale `-(n-1) log 2`, the exact discrepancy is `log n`
(compared with the `n`-point scale `-n log 2`, it is `log(2n)`).
**Lead:** the identity says the Euler/Gauss product
`Π sin(π k/n)` collapses an exponentially-many-factor product of
algebraic numbers into a *single rational*, with all the cyclotomic
height carried by individual factors *cancelling*. If a small algebraic
quantity built from this product structure can be made to approximate
`π` Archimedeanly at rate `1/n^c` while keeping cyclotomic height
polynomial in `n` (because the height-bearing factors cancel in the
product), the Liouville scale test failure of `α_n = n tan(π/n)` would
not transfer.

**Caveat — circularity check needed.** The integral
`∫_0^π log sin θ dθ = -π log 2` is itself *the* relation that connects
the sine product to `π`. Whether the pre-1882 derivability of this
integral is genuine or covertly invokes Lindemann–Weierstrass machinery
or later transcendence facts about `π` and `log 2` is the audit step that
has to come *first*. The integral is Euler-derivable (1768,
*Institutiones calculi integralis*, evaluated by series), so its
existence as an identity is pre-1882. Whether *using the identity* to
turn product-height cancellation into an arithmetic statement about `π`
is pre-1882-safe is the open question. Flag at hazard 4 of KHLA's hazard
list ("Fourier-support condition isn't Kraft-compatible") with a more
specific reading: "the sine-product specialization introduces the
`π log 2` integral constant, whose role must be audited before use in a
transcendence argument."

**Branch (i) lead — the cosine-product specialization.** Lemma 2 gives
the non-trivial vertex specialization:

```
(1 - cos(2π/n))(1 - cos(4π/n)) ··· (1 - cos(2(n-1)π/n)) = n² / 2^{n-1}.
```

This is the squared sine-product value times `2^{n-1}`, consistent with
`1 - cos 2θ = 2 sin² θ`. Same height-cancellation phenomenon. Same
caveat.

**Branch (ii) lead — Gauss's discrete Fourier inversion as
empirical-to-density bridge.** The KHLA budget's open issue at
[memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md](memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md)
§5 is the empirical-to-density proxy: the budget is stated for an
*assumed* density-side `C_X(2π h)` that bounds the empirical Weyl sums,
without a generic mechanism to read the proxy off the polygon-vertex
data. Gauss's discrete Fourier inversion (§3 above) supplies an *exact*
density-side reading from `2m+1` polygon-vertex samples — i.e., for the
specific case where the "empirical sequence" is the regular polygon
itself, the inversion formula is exact, not a bound. This collapses the
proxy into an identity at the polygon level. Whether the identity then
extends to the discrepancy register (where the relevant sequences are
not regular polygons but `(nπ) mod 1`) is the next step, and is *not*
supplied by Goldstine.

**Branch (ii) lead — Aliasing as Kraft-coded support condition.**
KHLA §(B) records that the polygon's continuous Fourier expansion has
support `{m : m ≡ 1 (mod n)}`. Gauss's aliasing identity (§4 above)
is the dual statement: under length-`μ` sampling, real-basis modes in the
two residue classes `±r mod μ` collapse onto a single coefficient. The
duality reads: continuous-side polygon support and discrete-side
aliased recovery are two sides of the same congruence-class structure
on the dual lattice `Z`. **Lead:** if the Kraft-budget (A) is rewritten
to use Gauss-aliasing for the polygon-vertex Fourier reading, the
"Fourier-support condition is Kraft-encodable" question (KHLA hazard 4)
admits a discrete formulation: encode the aliasing pattern on a
length-`μ` grid as the prefix-free description of the polygon's
continuous Fourier support. The encoding length is `O(log μ)` per
vertex, total `O(μ log μ)` for the whole polygon — comparable to the
polygon's algebraic depth `φ(2μ)/2 ~ μ/log log μ`. Whether this gives
a Kraft-bounded encoding without smuggling transcendence is the
audit step.

What §4.12-13 does *not* contribute to the KHLA branch:

- It does *not* close the Liouville scale test. The sine-product
  height-cancellation is a *lead*, not a closure; the relevant
  Archimedean rate of approximation to `π` has to be checked, and the
  `π log 2` circularity audit has to come first.
- It does *not* supply the empirical-to-density proxy in general.
  The discrete Fourier inversion is exact for regular-polygon vertex
  sequences; for `(nπ) mod 1` orbits, it is not the relevant register.
- It does *not* refute KHLA hazard 1 ("Dido route is Hermite in
  disguise"). Whether sine-product or Gauss-aliasing identities
  collapse to Hermite's auxiliary under Poisson summation is a
  separate check, not done here.

---

## 9. Pre-1882 Lineage Summary (Old-Time-Religion Audit)

Per [memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md), each item
in §1-6 above tagged for L-W-safety:

| Item | Source | Tag |
|---|---|---|
| Lagrange interpolation formula | Lagrange ~1759-1762; Gauss 1805 in trig form | Pre-1882 |
| Lemma 1 (sine half-angle product) | Euler 1748, *Introd. in Anal. Inf.* §240; Gauss 1805 | Pre-1882 |
| Lemma 2 (cosine product) | Gauss 1805, derived from Lemma 1 | Pre-1882 |
| Discrete Fourier inversion (length `2m+1`) | Gauss 1805 | Pre-1882 |
| Aliasing identity (length `μ ≠ 2m+1`) | Gauss 1805 | Pre-1882 |
| Divide-and-conquer subdivision `π = μν` | Gauss 1805 | Pre-1882 |
| Pallas worked example, `N = 12` | Gauss 1805 (data: von Zach) | Pre-1882 |
| Eccentric-anomaly forward-error analysis | Gauss 1809, *Theoria Motus* | Pre-1882 |
| Goldstine's exposition / numbering | Goldstine 1977 | Post-1882, methodologically transparent |
| Cooley-Tukey rediscovery footnote | Goldstine 1977 referencing 1965 | Post-1882, historiographic, not load-bearing |

Goldstine's exposition adds no transcendence content. His commentary
("This is the Lagrange formula", "This fascinating work of Gauss was
neglected and was rediscovered by Cooley and Tukey") is post-1882
historiography; the underlying mathematics is pre-1882.

The **`π log 2` circularity audit** flagged in §8 branch (i) is the one
identified hazard: any program use of the sine-product specialization
that connects the rational product `Π sin(π k/n) = n/2^{n-1}` to `π`
*as a transcendental* needs an explicit pre-1882 derivation of
`∫_0^π log sin θ dθ = -π log 2`. Euler 1768 supplies the integral as an
identity; whether using it inside a transcendence argument re-imports
L-W content is open.

---

## 10. Trust Boundary

### This brief should be cited for

- the existence and structure of Gauss's *Theoria interpolationis
  methodo nova tractata* (Werke III pp. 265-327) as exposed in
  Goldstine §4.12, with explicit Section-by-Section Goldstine
  references;
- the two product-to-sum lemmas at Goldstine p. 245, attributed to
  Gauss with an Euler 1748 anchor for Lemma 1;
- the aliasing identity at Goldstine p. 248, attributed to Gauss 1805;
- the discrete Fourier inversion formula at Goldstine pp. 246-247;
- the divide-and-conquer subdivision `π = μν` at Goldstine pp. 249-251;
- the Pallas worked example at Goldstine pp. 251-253, including the
  numerical Fourier expansion;
- the Cooley-Tukey rediscovery footnote at Goldstine p. 249 footnote 83;
- the dating of Gauss's manuscript to October 1805 per Goldstine
  p. 253 footnote 85 ("an improved version of an investigation begun
  by Gauss in October, 1805");
- the existence and structure of Gauss's forward-error analysis of the
  eccentric-anomaly equation in *Theoria Motus* (1809), per Goldstine
  §4.13 opening (pp. 258ff).

### This brief should NOT be cited for

- any modern complexity result (Goldstine reports no operation count;
  asymptotic content is not in the source);
- any direct claim about Gauss's manuscript without Goldstine
  intermediation (Werke III pp. 265-327 is not in the repo and not
  read directly);
- any L1-lens upper or lower bound — the FFT-complexity content
  remains Morgenstern, Winograd, Schönhage-Strassen, AFW;
- any L2-lens closure of the KHLA branches — §8 contains *leads*, not
  closures, and each lead carries a flagged audit step (Liouville
  height check, `π log 2` circularity check, Aitchison-extension
  check, Hermite-disguise check);
- the resolution of KHLA hazard 4 (Fourier-support Kraft-encodability)
  — §8 names a candidate encoding via Gauss-aliasing but does not
  audit its transcendence-content;
- any claim about the original Gauss text beyond what Goldstine
  reports (e.g., Goldstine's equation numbers 4.58-4.68 are
  Goldstine's, not Gauss's).

### Provenance tag for the program

**Methodologically pre-1882 mathematics, Goldstine 1977 exposition.**
The mathematical content is Gauss 1805 (interpolation manuscript) and
Gauss 1809 (*Theoria Motus*), with the Lemma 1 anchor at Euler 1748.
All three sources are within the L-W-safety window per
[memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md). Goldstine
1977's editorial framing is post-1882 but adds no transcendence
content. The brief functions as the technical companion to
[fft/HEIDEMAN-JOHNSON-BURRUS-1985-BRIEF.md](fft/HEIDEMAN-JOHNSON-BURRUS-1985-BRIEF.md):
HJB85 is the chain-of-custody record, this is the algebraic interior.

---

## Closing Sentence

This brief contributes the technical exposition of Gauss 1805 to the
program's audit of the FFT chain (L1) and a candidate set of pre-1882
weapons for the KHLA route (L2). On L1, the load-bearing additions are
the two product-to-sum lemmas at Goldstine p. 245, the aliasing
identity at p. 248, and the Pallas worked example at pp. 251-253 —
none of which the four modern complexity briefs name, and all of which
are pre-1882 in lineage. On L2, the load-bearing leads are
Euler/Gauss sine-product height-cancellation (a candidate substitute for
the dead `α_n = n tan(π/n)`, conditional on a `π log 2` circularity audit) and
Gauss-aliasing as a Kraft-coded discrete dual to the polygon's
continuous Fourier-support condition (a candidate response to KHLA
hazard 4, conditional on a Kraft-encoding audit). Neither lead closes
a KHLA branch; both are recorded with their audit steps named. The
brief does not enter the modern complexity register and does not
supersede the existing four FFT briefs on any operation-count
question.
