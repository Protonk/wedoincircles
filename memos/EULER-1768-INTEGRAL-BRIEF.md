# EULER-1768-INTEGRAL-BRIEF

Source-extraction memo on Leonhard Euler, *Institutionum calculi
integralis volumen primum* (Petropoli, Impensis Academiae Imperialis
Scientiarum, 1768; Eneström E342), 593 pp. Latin
([sources/euler-1768-institutiones-calculi-integralis-vol1.pdf](sources/euler-1768-institutiones-calculi-integralis-vol1.pdf)).

**Why this brief exists.** [memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md](memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md)
§"Proposed order of work" 6b and §"Hazards" flag a `π log 2` circularity
audit on the identity `∫_0^π log sin θ dθ = -π log 2`, attributed to
"Euler 1768, *Institutiones calculi integralis*." [fft/GOLDSTINE-1977-INTERPOLATION-BRIEF.md](fft/GOLDSTINE-1977-INTERPOLATION-BRIEF.md)
§8 branch (i) and §9 carry the same attribution. The brief reads Vol 1
directly to settle (a) whether the identity is there, (b) what other
π-emergence routes Vol 1 supplies, and (c) which of those is the
right audit target for the KHLA route's sine-product cancellation
candidate.

**What was read.** Front matter (title page, *Index Capitum*,
*Praenotanda* §§1-5). All of Cap. IV (*De integratione formularum
logarithmicarum et exponentialium*, body pp. 122-145), Cap. V (*De
integratione formularum angulos sinusve angulorum implicantium*,
body pp. 146-173), the opening of Cap. VI (*De evolutione integralium
per series secundum sinus cosinusque angulorum multiplorum
progredientes*, body pp. 174-186), Cap. VIII (*De valoribus integralium
quos certis tantum casibus recipiunt*, body pp. 230-254), and the
opening of Cap. IX (*De evolutione integralium per producta infinita*,
body pp. 255-261). Caps. I-III, VII, and the bulk of Sectio II
(differential equations) were *not* read — they are integration of
rational/irrational forms, series methods at the indefinite level,
general approximation, and ODE theory, none directly relevant to the
KHLA audit lens.

**Confidence level.** High on the negative finding (the specific
`∫_0^π log sin θ dθ` evaluation is absent from the chapters read,
which are the chapters where it would naturally appear). High on the
positive findings (Wallis even/odd split at §330-331, Beta-reflection
at §352, Wallis product at §357 — all directly visible on the page).
Medium on the KHLA inference: the identification of Beta-reflection
as the program-relevant audit target rather than `∫ log sin` is a
brief-level inference, not Euler's framing.

**Trust boundary up front.** Latin source; Goldstine 1977's English
exposition is not used here — only Vol 1's primary text, read with
attention to the mathematical content of the *Problemata*,
*Solutiones*, *Corollaria*, and *Scholia*. Section numbers cited as
"§N" refer to Euler's running paragraph numbers, which are continuous
across chapters. Body page numbers cited as "p. N" are the printed
page numbers, not PDF indices.

---

## 1. Verdict on the KHLA Audit Lens

The KHLA audit flag, in the form attributed to Vol 1, is **misscoped**.

The identity `∫_0^π log sin θ dθ = -π log 2` is not present in Vol 1
of *Institutiones calculi integralis*. Cap. IV handles logarithmic
integrals as series in `(log x)^n` with rational integrand, not
log-trig composites. Cap. V handles trigonometric integrals as
products of powers `sin^μ φ cos^n φ`, not log-trig composites. Cap. VI
opens with `dφ/(1+n cos φ)^ν` and its series expansion, again with no
log appearance. Cap. VIII evaluates definite integrals at the Wallis /
Beta-reflection level, with π appearing as a coefficient. Cap. IX
gives infinite-product representations including the Wallis product.
None of the five contains the log-sin integral.

What Vol 1 *does* supply is a different and arguably more useful
ingredient for the KHLA route: three pre-1882-safe π-emergence routes,
each derived by elementary content (substitution, integration by
parts, Wallis-style reduction). The audit target for KHLA's
sine-product cancellation candidate (branch (i) of [fft/GOLDSTINE-1977-INTERPOLATION-BRIEF.md](fft/GOLDSTINE-1977-INTERPOLATION-BRIEF.md)
§8) is **not** the log-sin integral; it is the **Beta-function
reflection formula at rational arguments** (Cap. VIII §352).

Whether the original `π log 2` audit can still be run depends on
locating Euler's actual derivation in a different source. Candidates
include Vol 4 (*Supplementum*, posthumous 1794), Eneström E156 (*De
inventione integralium si post integrationem variabili quantitati
determinatus valor tribuatur*, written c. 1750), or related 1750s
papers. None is in the repo at present.

---

## 2. Cap. IV — Logarithmic and Exponential Integrals (pp. 122-145)

Euler's logarithmic integration is presented as integration tables for
`x^n (log x)^m` and similar forms. The relevant content for the audit:

**§192-194 Coroll. 1-2.** Reduction of `∫ x^a (log x)^n dx` to lower
powers of `log x`, recursively, via integration by parts. Standard.

**§213 Coroll. 2.** The clean evaluation

```
∫_0^1 x^{m-1} (log(1/x))^n dx · (m^{n+1}) = 1 · 2 · 3 · ··· · n,
```

i.e., `∫_0^1 x^{m-1} (log(1/x))^n dx = n! / m^{n+1}`. This is the
analytic continuation of `Γ(n+1)/m^{n+1}` and is the source of the
familiar `∫_0^∞ e^{-t} t^n dt = n!` after `t = -m log x`.

**§219 Scholion.** Euler observes that `∫ dx / log x` (the logarithmic
integral) is not algebraically expressible, not expressible through
logarithms alone, and not expressible through trigonometric ("per
angulos") functions. This is an *informal* recognition of `Li(x)` as a
genuinely new transcendental, well before formal transcendence theory.
For the audit: Euler's recognition uses no transcendence-theoretic
machinery; it is a structural observation that the integral resists
elementary reduction.

**§220-227 Problemata 21-22.** Integration of `a^x · X(x)` for `X`
polynomial. Standard.

**§228 Scholion 1.** Euler labels `∫ a^x dx / x^n` a "transcendent
quantity" expressible by a series in powers of `dx`. Again, this is
classification by elementary methods, not transcendence theory.

**For the KHLA audit.** Cap. IV gives no log-trig integrals. Its
*recognition* of new transcendentals (`∫ dx/log x`, `∫ a^x dx/x^n`) is
classification, not arithmetic content. No L-W-style machinery is
present; no L-W-style machinery is required.

---

## 3. Cap. V — Trigonometric Integrals (pp. 146-173)

Cap. V handles trigonometric integrals in three families.

**§234-241 — `∫ X dx · arcsin x` and friends.** Polynomial-times-arcsin
integrals, by integration by parts:

```
∫ X(x) dx · arcsin x = P(x) · arcsin x − ∫ P(x) dx / √(1-x²).
```

with `P(x) = ∫ X(x) dx`. Worked examples §235-237 cover `∫dx · arcsin x`,
`∫x dx · arcsin x / √(1-x²)`, and `∫ dx · arcsin x / (1-x²)`.

**§242-247 — `∫ sin^μ φ cos^n φ dφ`.** Reduction formulas via product-
to-sum. The Werner identities

```
sin α cos β = ½[sin(α+β) + sin(α-β)]
cos α cos β = ½[cos(α-β) + cos(α+β)]
sin α sin β = ½[cos(α-β) − cos(α+β)]
```

are stated explicitly (§241 Scholion mentions "elementa de angulorum
compositione"). All reductions are pre-1882-safe.

**§248-260 — `∫ dφ / (sin^μ φ cos^n φ)`.** Reciprocal forms. §253
Scholion gives the standard `∫ dφ/cos^μ φ = (sin φ)/((m-1)cos^{m-1} φ)
+ (m-2)/(m-1) ∫ dφ/cos^{m-2} φ` reduction (with appropriate
sign conventions for tan vs. sec). §256 Coroll. tabulates the small
cases: `∫ dφ/cos² φ = tan φ`, `∫ dφ/sin² φ = -cot φ`, etc.

**For the KHLA audit.** No log-trig integrals; no `∫ log sin x dx`.
The chapter is integration tables for trig polynomials and rational
trig integrands. Its content is the substrate of every later chapter
that uses trig identities at the analytic level.

---

## 4. Cap. VI — Series in `cos(kφ)` (pp. 174 onward)

Cap. VI opens with **Problema 32** (§272): expand `∫ dφ/(1 + n cos φ)`
as a series in `cos(kφ)`. The structure of the chapter is

```
1/(1 + n cos φ) = a_0 + a_1 cos φ + a_2 cos 2φ + a_3 cos 3φ + ···,
```

with explicit recursion for the coefficients `a_k`. §273-277
(Coroll. 1-5) derive the recursion and apply it to special cases
(geometric, etc.).

**Problema 33** (§278+) is the same expansion for higher powers
`(1 + n cos φ)^{-ν}`.

**For the KHLA audit.** Cap. VI is the *Fourier-series-in-disguise*
chapter, but the series treated are expansions of *rational* functions
of cos φ, not of `log sin φ` or `log(2 sin(φ/2))`. The series
`log(2 sin(φ/2)) = -∑_{k≥1} cos(kφ)/k` does not appear in this
chapter. The methodology is undetermined-coefficient matching plus
recursion, all elementary. Pre-1882-safe.

What this *suggests*: a derivation of the log-sin Fourier series at
the level of Vol 1 would proceed by setting `f(φ) = log(2 sin(φ/2))`
and matching coefficients term-by-term in cos kφ, exactly as in
Cap. VI for rational integrands. The methodology is in place by 1768;
whether Euler ever wrote out the log-sin case in this register, in any
of his works, is the question the original `π log 2` audit really
needs to settle, and the answer is not in Vol 1.

---

## 5. Cap. VIII — Definite-Integral Values (pp. 230-254)

This is the chapter that supplies Vol 1's first π-emergence and the
KHLA-relevant audit target.

### 5.1 Wallis even/odd split (§330-331)

**Problema 38** (§330): evaluate `∫_0^1 x^{2m} dx / √(1-x²)`. By
reduction (using §119 already-proven recursion),

```
∫_0^1 dx/√(1-x²)        = π/2
∫_0^1 x² dx/√(1-x²)     = (1/2) · (π/2)
∫_0^1 x⁴ dx/√(1-x²)     = (1·3)/(2·4) · (π/2)
∫_0^1 x⁶ dx/√(1-x²)     = (1·3·5)/(2·4·6) · (π/2)
···
∫_0^1 x^{2n} dx/√(1-x²) = (1·3·5···(2n-1))/(2·4·6···(2n)) · (π/2),
```

and for odd powers,

```
∫_0^1 x dx/√(1-x²)        = 1
∫_0^1 x³ dx/√(1-x²)       = 2/3
∫_0^1 x⁵ dx/√(1-x²)       = (2·4)/(3·5)
···
∫_0^1 x^{2n+1} dx/√(1-x²) = (2·4·6···(2n))/(3·5·7···(2n+1)).
```

§331 Coroll. 1 states this verbatim. **§331 Coroll. 2** (verbatim
translation): "The integral `∫ x^m dx / √(1-x²)` is algebraically
expressible in cases where `m` is odd, but for `m` an even integer,
it always involves the periphery of the circle."

This is the **even/odd parity at the level of π-content** that the
KHLA program already invokes structurally on the polygon side. Euler
1768 supplies it explicitly for the Wallis-family integrals.

### 5.2 Wallis-pair product (§332-334)

**§332 Coroll. 2.** Two consecutive integrals multiply to π:

```
∫_0^1 x^m dx/√(1-x²) · ∫_0^1 x^{m+1} dx/√(1-x²) = π / (2(m+1)).
```

**§333 Coroll. 3.** Special cases:

```
∫_0^1 dx/√(1-x²) · ∫_0^1 x dx/√(1-x²)     = π/2,
∫_0^1 x dx/√(1-x²) · ∫_0^1 x² dx/√(1-x²)  = π/4,
···
```

**§334 Scholion 1** (verbatim): "Such a product of two integrals
yields a non-algebraic equality, even when the formulas themselves are
neither algebraically nor through quadrature of the circle expressible."
Euler observes that the *product* of two non-algebraic integrals can be
rationally tied to π even when neither integrand individually has a
closed form involving π.

**For the KHLA audit.** §332-334 is the cleanest pre-1882 instance of
"multiplicative cancellation across integrals brings π out as a
coefficient." Structurally this is the analytic ancestor of the KHLA
sine-product cancellation candidate (Goldstine-brief §8 branch (i)),
where multiplication across `n-1` algebraic-of-degree-`~φ(2n)` factors
collapses to a rational `n/2^{n-1}`. The Euler 1768 instance is *over
integrals*, not over algebraic numbers, but the cancellation
phenomenon is the same shape. **This is the program-relevant audit
target for the cancellation lead.**

### 5.3 Beta-reflection at rational arguments (§352)

**Problema 41** (§351-352): evaluate `∫_0^∞ x^{m-1} dx / (1 + x^n)`.

By reduction (Euler chains through §349's earlier result), the answer
is

```
∫_0^∞ x^{m-1} dx / (1 + x^n) = π / (n · sin(mπ/n))         [§352].
```

This is the **Beta-function reflection formula** at rational
arguments (`a = m/n` in modern notation, `Γ(a)Γ(1-a) = π/sin(aπ)` in
later packaging). The derivation in Cap. VIII routes through repeated
reduction and the recognition that `∫_0^∞ dx/(1+x^n)` at integer `n`
is `π/(n sin(π/n))`.

§353 Coroll. 2 tabulates small cases:

```
∫_0^∞ dx/(1+x²)        = π/2,
∫_0^∞ dx/√(1-x²)       = π/2,
∫_0^∞ dx/(1+x⁴)        = π/(4 sin(π/4))  =  π/(2√2),
∫_0^∞ x dx/(1+x⁴)      = π/(4 sin(2π/4)) =  π/4,
∫_0^∞ dx/(1+x³)        = π/(3 sin(π/3))  =  2π/(3√3),
···
```

**For the KHLA audit.** This is the load-bearing identity for the
program-relevant KHLA lead. Each individual `sin(πk/n)` value is given
an **explicit elementary integral representation** at §352. The
sine-product `Π_{k=1}^{n-1} sin(πk/n) = n/2^{n-1}` therefore admits a
representation as a product of `n-1` Euler integrals — each of the
form `∫_0^∞ x^{k-1} dx / (1 + x^n)` for `k = 1, ..., n-1`.

Whether that product representation gives a usable cancellation
mechanism for the KHLA branch (i) sine-product candidate is open
research, not a brief deliverable. What the brief contributes: the
audit target for the cancellation lead is **Beta-reflection at
rational arguments (Euler 1768 Cap. VIII §352)**, not the log-sin
integral.

### 5.4 §354 onward

§354 Coroll. 3 derives integral identities for closely-related forms,
including `∫_0^∞ x^{m-1} dx / (1 + x^n)^k` reductions. §355 Scholion
flags that these definite values are accessible by Euler's reduction
methodology even when the indefinite forms are not.

---

## 6. Cap. IX — Infinite-Product Representations (pp. 255-261+)

**Problema 43** (§356): evaluate `∫_0^1 dx/√(1-x²)` (= π/2) as an
infinite product. Euler chains the Wallis-family reductions and
arrives at

```
π/2 = (2·2·4·4·6·6·8·8····) / (1·3·3·5·5·7·7·9····)             [§357]
```

— **the Wallis product** (Wallis 1655; Euler reproof here). §358
Coroll. 2 notes that the order of factors does not matter (absolute
convergence is implicit in Euler's wording: "Nihil interest, quonam
ordine singuli factores in hoc producto disponantur").

**For the KHLA audit.** The Wallis product is the canonical pre-1882
example of "π as an infinite product of rationals." It is one of the
clearest cases where a transcendental constant is exhibited as a
limit of explicit rational arithmetic, with no transcendence input.
For the KHLA route specifically: it is the *L*-statement complement to
Cap. VIII's *finite-integral* statement. The brief flags it for
completeness; it is not the audit target for the cancellation lead.

---

## 7. Inferred for the KHLA Program

### 7.1 The audit-target migration

The KHLA `π log 2` audit, as currently flagged in [memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md](memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md)
§"Proposed order of work" 6b and §9 of [fft/GOLDSTINE-1977-INTERPOLATION-BRIEF.md](fft/GOLDSTINE-1977-INTERPOLATION-BRIEF.md),
should be split into two:

- **`π log 2` audit (deferred).** Original target: `∫_0^π log sin θ dθ
  = -π log 2`. Vol 1 of *Calculi Integralis* does not contain this
  identity; the audit target is a different Euler source not yet in
  the repo. Keep the audit flag open in KHLA but disconnect it from
  the Vol-1 attribution.
- **Beta-reflection audit (live, with Vol-1 anchor).** New target:
  `∫_0^∞ x^{m-1} dx / (1 + x^n) = π / (n sin(mπ/n))`, Cap. VIII §352.
  This is the upstream of the KHLA sine-product cancellation
  candidate, and is the right audit object for KHLA branch (i).

The migration matters because Beta-reflection has a cleaner pre-1882
lineage than the log-sin integral. Beta-reflection is in Wallis 1655
(`m=n=2` case), Euler 1738 (E20, general form), and Euler 1768 §352
(present source). The log-sin integral's earliest pre-1882 source has
to be located; until it is, the audit attribution is a placeholder.

### 7.2 Wallis even/odd parity as a direct KHLA tool

Cap. VIII §330-331 supplies a clean structural fact: among the Wallis
family `∫_0^1 x^m dx/√(1-x²)`, the integrals at *even* `m` are
proportional to π, and at *odd* `m` are rational. This parity is
elementary in content and predates 1882 cleanly (Wallis 1655 explicit;
Euler 1768 packaged).

For the program: this is a candidate **anchor for an even/odd parity
argument on the polygon-vs-circle gap**. The polygon side
([corners/HURWITZ-FIRST-BAND-CONCENTRATION.md](corners/HURWITZ-FIRST-BAND-CONCENTRATION.md))
already exhibits a frequency-support condition `m ≡ 1 (mod n)`; the
Wallis family supplies a different parity (`m` even vs. odd) at the
level of integrals. Whether the two parities can be coupled — e.g.,
via a discrete-to-integral lift through Gauss interpolation
([fft/GOLDSTINE-1977-INTERPOLATION-BRIEF.md](fft/GOLDSTINE-1977-INTERPOLATION-BRIEF.md))
— is open. Flagged here, not pursued.

### 7.3 The §332-334 cancellation pattern as ancestor

The Wallis-pair cancellation `∫_0^1 x^m dx/√(1-x²) · ∫_0^1 x^{m+1}
dx/√(1-x²) = π/(2(m+1))` (§332) is the cleanest pre-1882 instance of
the cancellation phenomenon the KHLA route is searching for: a product
of two non-algebraic objects collapses to a rationally-π expression.
Structurally this is the *integral-side* analog of the program's
*algebraic-side* sine-product cancellation. The brief notes the
pattern; whether the integral-side instance can be lifted to an
algebraic-side construction via Beta-reflection (§352) is the question
that links them.

### 7.4 What this brief does *not* settle

- The original `π log 2` audit (target identity not in Vol 1).
- Whether sine-product cancellation produces a polynomial-cyclotomic-
  height small algebraic quantity Archimedean-close to π.
- Whether the Hermite-disguise hazard ([memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md](memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md)
  §"Hazards" 1) propagates to the Beta-reflection audit target.
- Whether the discrete Fourier inversion (Goldstine-brief §3) and the
  Wallis-family integrals (this brief §5.1-5.3) are dual under any
  natural transformation.

These are research moves, not source-extraction moves. Each gets its
own register if and when the audit closes.

---

## 8. Pre-1882 Lineage Summary (Old-Time-Religion Audit)

Per [memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md), each
identity in §§2-6 above tagged for L-W-safety:

| Identity | Source | L-W-safety tag |
|---|---|---|
| Logarithmic integration tables (Cap. IV) | Euler 1768 §§192-227 | Pre-1882, methodologically transparent |
| `Li(x)` recognition as new transcendental (§219 Scholion) | Euler 1768 | Pre-1882, classification-only |
| Trig integration tables (Cap. V) | Euler 1768 §§234-260; Werner identities pre-1600 | Pre-1882 |
| Cosine-series expansion of rational trig integrands (Cap. VI) | Euler 1768 §§272+ | Pre-1882 |
| Wallis even/odd integral parity (§330-331) | Wallis 1655; Euler 1768 reproof | Pre-1882 |
| Wallis-pair cancellation (§332-334) | Euler 1768; Wallis precedent | Pre-1882 |
| Beta-reflection at rational arguments (§352) | Wallis 1655 (`m=n=2`), Euler 1738 (general), Euler 1768 (present) | Pre-1882 |
| Wallis product (§357) | Wallis 1655; Euler 1768 reproof | Pre-1882 |

All identities derived in Vol 1 by elementary methods (substitution,
integration by parts, recursive reduction, undetermined coefficients).
No transcendence-theoretic input. The whole chapter is admissible
under §"Audit criterion: content, not calendar" of OLD-TIME-RELIGION
in its strongest form: it is *both* pre-1882 in calendar *and*
transcendence-free in content.

The migrated KHLA audit target — Beta-reflection at rational arguments
— inherits the same lineage. Its **use** inside a transcendence
argument requires a separate audit (does the use smuggle L-W content?),
which is research, not extraction.

---

## 9. Trust Boundary

### This brief should be cited for

- the absence of `∫_0^π log sin θ dθ = -π log 2` from Vol 1 of
  *Institutiones calculi integralis* in the chapters covering
  logarithmic, trigonometric, series, and definite-integral material
  (Caps. IV-IX);
- the **Wallis even/odd integral parity** at §330-331 (`∫_0^1 x^m dx/
  √(1-x²)` is rational for `m` odd, π-times-rational for `m` even);
- the **Wallis-pair cancellation** at §332-334 (`∫_0^1 x^m dx/√(1-x²)
  · ∫_0^1 x^{m+1} dx/√(1-x²) = π/(2(m+1))`);
- the **Beta-reflection formula at rational arguments** at §352
  (`∫_0^∞ x^{m-1} dx / (1+x^n) = π/(n sin(mπ/n))`);
- the **Wallis product** at §357 (`π/2 = Π even²/odd²`);
- the §219 Scholion *informal* recognition of `∫ dx / log x` as a new
  transcendental, by classification rather than by transcendence
  theory;
- the methodological observation that all π-bearing definite integrals
  in Vol 1 are derived from elementary content (substitution,
  reduction, recursion), without transcendence-theoretic input.

### This brief should NOT be cited for

- the identity `∫_0^π log sin θ dθ = -π log 2` *as a Vol-1 result*
  (it is not in Vol 1);
- any post-1768 packaging — Γ-function reflection (Gauss/Weierstrass),
  Beta-Gamma identification (Legendre), dilogarithm theory (Euler
  1768 elsewhere or post-1768) — the brief does not enter these
  registers;
- any modern transcendence content — Vol 1 has none, and the brief
  does not import any;
- a *closure* of the KHLA branch (i) cancellation lead (the brief
  identifies the audit target, not the audit's outcome);
- a *closure* of the KHLA `π log 2` audit (the target identity is
  not in this source);
- chapters of Vol 1 not read here (Caps. I, II, III, VII, and most of
  Sectio II / III), nor Vols 2-4 of the same work.

### Provenance tag for the program

**Pre-1882 in calendar (1768) and transcendence-free in content.**
Vol 1 is a complete elementary-integration treatise; every result the
brief extracts is derivable by substitution, integration by parts,
recursion, or undetermined-coefficient matching. It is admissible
without methodological caveat under [memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md)
§"Audit criterion: content, not calendar." The brief functions as the
classical-analysis companion to the modern complexity briefs in
[fft/](fft/), and as a direct upstream for the KHLA route's branch
(i) audit (sine-product cancellation candidate).

---

## Closing Sentence

This brief settles three questions about Euler 1768 Vol 1 with bearing
on the KHLA route. (1) The identity `∫_0^π log sin θ dθ = -π log 2` is
not in Vol 1; the original KHLA audit attribution should migrate. (2)
The right audit target for the KHLA branch (i) sine-product
cancellation candidate is **Beta-reflection at rational arguments**,
Cap. VIII §352, not the log-sin integral. Beta-reflection has a
cleaner pre-1882 lineage (Wallis 1655 + Euler 1738/1768) than the
log-sin identity, and is the upstream of every individual `sin(πk/n)`
that enters the cancellation candidate. (3) Vol 1 supplies, as
collateral, two further pre-1882 anchors of independent program
interest: the **Wallis even/odd integral parity** (§330-331) as a
candidate parity argument on the polygon-vs-circle gap, and the
**Wallis-pair cancellation** (§332-334) as the integral-side ancestor
of the algebraic-side cancellation pattern KHLA is searching for.
None of these closes the KHLA route; each redirects an open audit to
a pre-1882-safe object with verified provenance.
