# EULER-1794-SUPPLEMENT-BRIEF

Source-extraction memo on Leonhard Euler, *Institutionum calculi
integralis volumen quartum, continens supplementa partim inedita partim
iam in operibus academiae imperialis scientiarum Petropolitanae impressa*
(originally Petropoli, Imp. Acad. Sci., 1794; *editio tertia* 1845;
Eneström E660 + collected reprints), 632 pp. Latin
([sources/euler-1794-institutiones-calculi-integralis-vol4-supplementum.pdf](sources/euler-1794-institutiones-calculi-integralis-vol4-supplementum.pdf)).

**Why this brief exists.** [memos/EULER-1768-INTEGRAL-BRIEF.md](memos/EULER-1768-INTEGRAL-BRIEF.md)
§1 reported the negative finding that `∫_0^π log sin θ dθ = -π log 2`
is **not** in Vol 1 of *Institutiones calculi integralis*, and flagged
the audit-target attribution for [memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md](memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md)
§"Proposed order of work" 6b as needing a different Euler source. Vol IV
*Supplementum* — originally posthumous 1794, here read in the 1845
*editio tertia* reprint — is the natural next candidate: it collects
Euler's later integration papers, organized as Supplementa each tied to
a Caput of Vols I-III. This brief reads Vol IV directly with that
specific search target.

**What was read.** Title page (1845 *editio tertia*, "Continens
supplementa partim inedita partim iam in operibus academiae imperialis
scientiarum Petropolitanae impressa"), the opening of Supplementum I
(Ad Tom. I Cap. II, irrational forms, body pp. 3-30), part of
Supplementum III (Ad Tom. I Cap. IV, log/exp integrals, body
pp. 91-103), the body of Supplementum IV (Ad Tom. I Cap. V, trig
integrals, body pp. 191-225), and **Supplementum V in detail (Ad Tom.
I Cap. VIII, definite-integral values, body pp. 260-294)** including
its explicit source attribution. The volume's tail (Supplementum XI,
Ad finem Tom. III, calculus of variations, ending body p. 620) was
sampled to confirm the supplement structure but not read substantively.

**Confidence level.** High on the positive finding: Vol IV Supp V §51
contains the Fourier series for `log(2 sin(u/2))`, from which
`∫_0^π log sin u du = -π log 2` follows by one elementary additional
step (term-by-term integration plus orthogonality of `cos(ku)` on
`[0, π]`). High on the source attribution: Supp V Section 1 explicitly
cites *Nova Methodus quantitates integrales determinandi*, *Novi
Commentarii Academiae Scient. Petropolitanae* Tom. XIX, pp. 66-102 —
the original paper that became this Supplementum. High on the Daniel
Bernoulli attribution at p. 285. Medium on whether Euler *also*
explicitly states the integral value in some other section of Vol IV
not read here; the chapters most likely to contain it have been read.

**Trust boundary up front.** The 1845 reprint of an originally 1794
posthumous publication. The mathematical content is Euler's; the
typesetting, equation numbering, and 1845 third-edition packaging are
later editorial. Section numbers cited as "§N" are Euler's running
paragraph numbers (continuous within each Supplementum). Latin OCR is
unavailable on this scan; identities are read directly from the page
images. Daniel Bernoulli's role is reported on Euler's attribution, not
independently checked against Bernoulli's own writings.

---

## 1. Verdict on the KHLA Audit Lens

**The `π log 2` audit identity is now located.** Vol IV Supplementum V,
Section 1 (originally *Nova Methodus quantitates integrales
determinandi*, Novi Commentarii XIX), §51, contains the Fourier series

```
cos(u)/1 + cos(2u)/2 + cos(3u)/3 + cos(4u)/4 + ··· = -log(2 sin(u/2))
```

derived for `0 < u < 2π`. From this, `∫_0^π log sin u du = -π log 2`
follows by **one additional elementary step**: integrate both sides on
`[0, π]`, use `∫_0^π cos(ku) du = sin(kπ)/k = 0` for every integer
`k ≥ 1`, conclude `∫_0^π log(2 sin(u/2)) du = 0`, substitute `v = u/2`
and rearrange.

The derivation Euler gives uses three pre-1882 methodological
ingredients:
1. The geometric/cotangent series `Q = sin u + sin 2u + sin 3u + ··· =
   (1/2) cot(u/2)`, formally justified as the imaginary part of the
   geometric series `∑ z^k e^{iku}` in the limit `z → 1`.
2. Term-by-term integration to produce the convergent series for
   `P' = -log(2 sin(u/2))`.
3. Determination of the constant of integration via the **alternating
   harmonic series at `u = π`**: `-1 + 1/2 - 1/3 + 1/4 - ··· = -log 2`
   (Mercator/Newton 1668, log series for `log(1+x)` at `x = 1`).

Euler explicitly attributes this constant-determination method to
**Daniel Bernoulli** (p. 285): *"Hoc modo constantem determinandi
Illustr. Daniel Bernoulli primus est usus, qui praeterea multa praeclara
circa indolem harum serierum annotavit"* — "Daniel Bernoulli was the
first to use this method of determining the constant, who also noted
many fine things about the nature of these series." Daniel Bernoulli
died in 1782, predating Lindemann–Weierstrass by a century. The
attribution chain is therefore Bernoulli → Euler → 1774 publication →
1794 collection → 1845 reprint, all pre-1882 in mathematical content,
and pre-Hermite (1873) at the publication of the original paper.

**Audit closes positive on the identity itself.** The `π log 2` audit
flagged in [memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md](memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md)
§"Proposed order of work" 6b can now be re-attached to Vol IV Supp V
§51. The transcendence-content audit on whether *using* the identity
inside a Liouville-style argument smuggles L-W content remains a
separate, independent audit and is not closed by this brief.

---

## 2. Vol IV Structural Map

The volume is organized as eleven Supplementa, each tied to one or more
chapters of the earlier volumes. The supplementa are reprints (some
with editorial reorganization) of papers Euler presented to the
Petersburg Academy. Source attributions appear at the head of each
section.

| Supp. | Tied to | Body pp. | Read here |
|---|---|---|---|
| I | Tom. I Cap. II (irrationalium) | 3-89 | Opening §§1-35 |
| II | Tom. I Cap. III (per series) | (probable) | Not read |
| III | Tom. I Cap. IV (log/exp) | 90-110+ | §§22-37 |
| IV | Tom. I Cap. V (trig integrals) | 187-252 | §§17-55 |
| V | **Tom. I Cap. VIII (definite values)** | **260-318+** | **§§1-55 in full** |
| VI through X | Tom. II / Tom. III | 319-619 | Not read |
| XI | Ad finem Tom. III (variations) | 612-620 | Sampled |

The supplementa relevant to KHLA are **Supp V** (Tom. I Cap. VIII,
where definite-integral values like `∫_0^π log sin` would naturally
live) and **Supp IV** (Tom. I Cap. V, the Poisson-kernel definite
integrals from `Φ = 0` to `Φ = π`).

---

## 3. Supplementum IV Highlights — Poisson-Kernel Definite Integrals

Supp IV contains three distinct papers, with explicit source
attribution at the head of each section.

**Supp IV Section 2 (p. 192).** *Theorema maxime memorabile circa
formulam integralem `∫ ∂Φ cos(λΦ)/(1 + a² - 2a cos Φ)^{n+1}`*. M. S.
Academiae exhib. die 13. Augusti 1778. Euler proves: for integer `λ ≥ 0`
and integer `n ≥ 0`,

```
∫_0^π ∂Φ cos(λΦ)/(1 + a² - 2a cos Φ)^{n+1} = (π a^λ / (1 - a²)^{2n+1}) · V,
```

where `V` is a polynomial in `a²` with binomial-coefficient factors.
At `λ = n`, `V = (2n choose n)`. Tabulated for `n = 0, 1, ..., 6` at
p. 209 with explicit numerators (1, 2, 6, 20, 70, 252, 924 — central
binomial coefficients).

**For the program.** This is the Poisson-kernel orthogonality identity
in finite-Fourier-series form — exactly the apparatus that *underwrites*
the polygon Fourier expansion in
[corners/HURWITZ-FIRST-BAND-CONCENTRATION.md](corners/HURWITZ-FIRST-BAND-CONCENTRATION.md).
The polygon's frequency-support condition `c_m^(n) ≠ 0 ⇔ m ≡ 1 (mod n)`
is the same congruence-class structure Euler tabulates here under
length-`mu` sampling, viewed from the analytic side. Pre-1882 (1778
academy presentation), method-pure (rational-function partial fractions
and trig identities, no transcendence input).

**Supp IV Section 3 (p. 217).** *Disquisitio conjecturalis super formula
integrali `∫ ∂Φ cos(iΦ)/(α + β cos Φ)^n`*. M. S. Academiae exhib. die
31. Augusti 1778. Establishes via the Weierstrass substitution `t = tan(½Φ)`:

```
∫_0^π ∂Φ/(α + β cos Φ) = π/√(α² - β²)        [§42],
```

then iterates to higher `n` via reduction. Continues with case analysis
for `i = 0, 1, 2, 3, ...` and recursion. Supplies the `1/sin(rational·π)`
normalization the Beta-reflection family of Vol 1 §352 sits inside.

**For the program.** Pre-1882 derivation of the canonical
`∫_0^π dφ/(1 - 2a cos φ + a²) = π/(1 - a²)` definite integral, and its
generalizations — the integral-side counterpart of the Beta-reflection
identity flagged at [memos/EULER-1768-INTEGRAL-BRIEF.md](memos/EULER-1768-INTEGRAL-BRIEF.md)
§5.3.

---

## 4. Supplementum V Section 1 — Source for `π log 2`

Supplementum V opens at p. 260 with header:

> **SUPPLEMENTUM V. AD TOM. I. CAP. VIII. DE VALORIBUS INTEGRALIUM
> QUOS CERTIS TANTUM CASIBUS RECIPIUNT.**
>
> 1) **Nova Methodus quantitates integrales determinandi.** *Novi
> Commentarii Academiae Scient. Petropolitanae* Tom. XIX. Pag. 66 - 102.

This is Euler's original paper on the "new method" for determining
integral values. Published in *Novi Commentarii* XIX, which corresponds
to academic year 1774-1775 (publication ~1775). Pre-Hermite (1873) by
about a century, pre-Lindemann (1882) by 107 years.

### 4.1 §3-6 — The integral identity `∫_0^1 (z-1) dz / log z = log 2`

**§2-3 (p. 261-262).** Euler considers the integral
`∫_0^1 (z-1) dz / log z`. By substituting `z = e^{-1/i}` for large `i`,
he reduces it to the Riemann-sum form `∑_{k=i}^{2i-1} 1/k` (a partial
harmonic sum).

**§4-5 (p. 262-263).** Identifying

```
∑_{k=i}^{2i-1} 1/k = A - B   where A = 1 + 1/2 + ... + 1/(2i-1)  
                                 B = 1 + 1/2 + ... + 1/(i-1),
```

and rearranging into the alternating harmonic series

```
A - B = 1 - 1/2 + 1/3 - 1/4 + 1/5 - ··· = log 2
```

(in the limit `i → ∞`), Euler concludes

```
∫_0^1 (z - 1) dz / log z = log 2 = 0.6931471805     [§5].
```

**§6 (p. 263-264).** Generalizes to

```
∫_0^1 (z^m - z^n) dz / log z = log((m + 1)/(n + 1))   [Frullani-type].
```

**For the program.** This is a *separate* `log 2` definite-integral
identity, not the `π log 2` one, but it lives in the same Supp V §1
paper and uses the same alternating-harmonic-series device that fixes
the constant in §51 below. The methodology is `Mercator 1668 + Riemann
sum reorganization`, both pre-1882. No π appears here; the connection to
π is via §32-43 and §51 below.

### 4.2 §32-43 — Series in `cos(ku)/k^p` and `sin(ku)/k^p`

**§32 (p. 279).** Euler defines

```
P = z·cos u + z²·cos 2u + z³·cos 3u + ··· = (z·cos u - z²)/(1 - 2z cos u + z²),
Q = z·sin u + z²·sin 2u + z³·sin 3u + ··· =  z·sin u    /(1 - 2z cos u + z²).
```

These are real and imaginary parts of the geometric series `∑ z^k
e^{iku}`. Identities are exact for `|z| < 1`.

**§40 (p. 284).** At `z = 1`, the formal series

```
cos u + cos 2u + cos 3u + cos 4u + ··· = -1/2
```

is established by Euler in the analytic-continuation sense (`P` evaluated
at `z = 1`).

**§40 continued (p. 285).** Multiplying by `∂u` and integrating:

```
Q' := sin u/1 + sin 2u/2 + sin 3u/3 + sin 4u/4 + ··· = A - u/2.
```

The constant `A` is determined by a clever limit at `u = π + ω` with
`ω → 0`: the series at `u = π` becomes alternating-zero (zero in the
Cesàro sense), forcing `A - π/2 = 0`, i.e., `A = π/2`. Hence

```
sin u/1 + sin 2u/2 + sin 3u/3 + ··· = (π - u)/2
```

— **the Fourier series of the sawtooth wave on `(0, 2π)`**. Euler
attributes the constant-determination method here explicitly to **Daniel
Bernoulli** (p. 285): *"Hoc modo constantem determinandi Illustr. Daniel
Bernoulli primus est usus."*

**§41 (p. 285-286).** Iterating once more:

```
P'' := cos u/1² + cos 2u/2² + cos 3u/3² + ··· = π²/6 - πu/2 + u²/4.
```

Constant fixed by `u = 0`: gives `B = ζ(2) = π²/6` (Euler's Basel
problem solution, 1735).

**§42-43 (p. 286).** Continuing iteration produces

```
Q''' = sin u/1³ + sin 2u/2³ + ··· = π²u/6 - πu²/4 + u³/12,
P^IV = cos u/1⁴ + cos 2u/2⁴ + ··· = π⁴/90 - π²u²/12 + πu³/12 + u⁴/48,
```

with constants `B = ζ(2) = π²/6`, `D = ζ(4) = π⁴/90` from Euler's
earlier results. These are the **classical Fourier series of Bernoulli
polynomials**, derived here by Euler's method.

**For the program.** This branch supplies Fourier series for
`B_k(u/(2π))`-type periodic functions, not the log-sin integral
directly. Listed for completeness; the log-sin route is §51 below.

### 4.3 §51 — The Fourier series for `-log(2 sin(u/2))`

**§51 (p. 291).** Euler now starts from the dual series

```
Q = sin u + sin 2u + sin 3u + sin 4u + ··· = (1/2) cot(u/2),
```

(this is the same `Q` of §32 evaluated at `z = 1`, equivalent to `Q`
above by `cot(u/2) = (1 - cos u)/sin u`). Multiplying by `-∂u` and
integrating:

```
P' := cos u/1 + cos 2u/2 + cos 3u/3 + cos 4u/4 + ··· = -(1/2) log sin(u/2) + A.
```

To determine `A`, Euler evaluates at `u = π` where `sin(u/2) = 1`,
`log sin(u/2) = 0`, and the series becomes the alternating harmonic
series

```
-1 + 1/2 - 1/3 + 1/4 - 1/5 + ··· = -log 2.
```

So `A = -log 2`, and Euler combines into the closed-form

```
P' = cos u + (cos 2u)/2 + (cos 3u)/3 + (cos 4u)/4 + ··· = -log(2 sin(u/2))     [§51].
```

This is **the Fourier series for `-log(2 sin(u/2))`** on `(0, 2π)`.

### 4.4 Derivation of `∫_0^π log sin u du = -π log 2`

Euler does not in §51 explicitly state the integral evaluation
`∫_0^π log sin u du = -π log 2`, but it is **one elementary step away**
from §51:

```
∫_0^π P'(u) du = -∫_0^π log(2 sin(u/2)) du.

LHS:  ∑_{k≥1} (1/k) ∫_0^π cos(ku) du
   =  ∑_{k≥1} (1/k) · [sin(kπ)/k]
   =  0       (since sin(kπ) = 0 for every integer k).

Hence:  ∫_0^π log(2 sin(u/2)) du = 0,
i.e.:   π·log 2 + ∫_0^π log sin(u/2) du = 0,
i.e.:   ∫_0^π log sin(u/2) du = -π·log 2.

Substitute v = u/2 (dv = du/2, v: 0 → π/2):
        ∫_0^{π/2} log sin v · 2 dv = -π·log 2,
i.e.:   ∫_0^{π/2} log sin v dv = -(π/2)·log 2,
equivalently:
        ∫_0^π log sin v dv = -π·log 2.
```

The single additional ingredient is the elementary `∫_0^π cos(ku) du = 0`
for integer `k ≥ 1`, which is in Vol 1 of *Institutiones calculi
integralis* Cap. V at the level of indefinite integration. **All
content is pre-1882-safe.**

### 4.5 §52-55 — Iterations to higher polylog-like series

Continuing from §51:

```
Q'' := sin u/1² + sin 2u/2² + ··· = ∫ ∂u Δ:u                          [§52],
P''' := cos u/1³ + cos 2u/2³ + ··· = -∫ ∂u Δ':u                       [§53],
Q^IV, P^V, ···  by further iteration                                  [§54-55].
```

These are the **Clausen function `Cl_2`** and the polylogarithm-like
generalizations, derived by Euler via the same elementary integration
plus constant-determination machinery.

**For the program.** Not directly relevant to the KHLA `π log 2` audit;
listed as collateral evidence that Euler's methodology in Supp V scales
to higher-order log-trig integrals systematically and in pre-1882 register.

---

## 5. Inferred for the KHLA Program — Audit-Target Re-Attachment

### 5.1 Migration of the `π log 2` audit attribution

[memos/EULER-1768-INTEGRAL-BRIEF.md](memos/EULER-1768-INTEGRAL-BRIEF.md)
§7.1 reported that the original KHLA audit attribution to Euler 1768
(Vol 1) for `∫_0^π log sin θ dθ = -π log 2` was misscoped (the identity
is not in Vol 1) and migrated the audit's *active* target to
**Beta-reflection at rational arguments** (Vol 1 Cap. VIII §352) for the
sine-product cancellation candidate. That migration stands.

This brief now supplies the Vol IV anchor for the **original** `π log 2`
audit thread:

| KHLA audit branch | Pre-1882 anchor | Source |
|---|---|---|
| Sine-product cancellation candidate (§6b) | Beta-reflection `∫_0^∞ x^{m-1} dx/(1+x^n) = π/(n sin(mπ/n))` | Vol 1 §352 + Wallis 1655 + Euler 1738 |
| `π log 2` audit (original flag) | Fourier series `∑ cos(ku)/k = -log(2 sin(u/2))` + integration on `[0, π]` + alternating harmonic series at `u = π` | Vol IV Supp V §51, originally Novi Comm XIX (1774) |
| Daniel Bernoulli's constant-determination method | Used by Euler at §40 sawtooth and §51 log-sin | Bernoulli ante 1782, attributed by Euler at p. 285 |

The KHLA audit target structure is therefore now anchored in **two
distinct pre-1882 sources**, neither of which routes through Lindemann–
Weierstrass machinery.

### 5.2 Methodology audit — what Euler's derivation requires

The §51 derivation chain:

1. `Q = sin u + sin 2u + ··· = (1/2) cot(u/2)`
   *Pre-1882.* Geometric/cotangent series; provable by `cot(u/2) =
   (cos(u/2))/(sin(u/2)) = i(e^{iu/2} + e^{-iu/2})/(e^{iu/2} - e^{-iu/2})`
   manipulation, which is method-pure trigonometric algebra.

2. Term-by-term integration to get `P' = ∑ cos(ku)/k = -log(2 sin(u/2)) + A`.
   *Pre-1882.* Justified for `u ∈ (0, 2π)` by Abel-summation arguments
   that are in Cauchy 1821 *Cours d'analyse*. Pre-1882 in calendar (1821)
   and method-pure.

3. Alternating harmonic series `-1 + 1/2 - 1/3 + ··· = -log 2` at `u = π`.
   *Pre-1882.* Mercator 1668 series for `log(1 + x)` at `x = 1`,
   conditionally convergent. Pre-Liouville (1844) by 176 years.

4. Hence `A = -log 2`, giving `P' = -log(2 sin(u/2))`.
   *Pre-1882.* Algebra.

5. Integrate `P'` term-by-term over `[0, π]`, use `∫_0^π cos(ku) du = 0`
   for integer `k ≥ 1`. Conclude `∫_0^π log sin u du = -π log 2`.
   *Pre-1882.* Vol 1 Cap. V level integration.

**Every step pre-1882-safe in calendar and methodology.** The
transcendence-content audit on whether using `∫_0^π log sin u du = -π log 2`
inside a Liouville-style argument smuggles L-W content is independent of
this and is not closed by this brief. (The audit would ask whether the
relation `π log 2` between two transcendentals — even though derivable
elementarily as a real-number equality — secretes algebraic-independence
input when used as a constraint in a transcendence-detection argument.
That is a transcendence-theoretic question, not an Euler-source
question.)

### 5.3 Daniel Bernoulli as upstream attribution

Euler's explicit attribution (p. 285) of the constant-determination
method to **Daniel Bernoulli** pushes the lineage of the `π log 2`
identity back further than Euler's own publication. Daniel Bernoulli
(1700-1782) was active in St. Petersburg with Euler in the 1730s.
The Bernoulli precedent supplies an additional pre-1773 (pre-Hermite,
pre-Lindemann, pre-Liouville-1844) anchor.

For [memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md): the
§"Audit criterion: content, not calendar" stance treats this as
transcendence-free in content and pre-1882 in both calendar and method.

---

## 6. Pre-1882 Lineage Summary (Old-Time-Religion Audit)

| Identity / methodology | Source | L-W-safety tag |
|---|---|---|
| Mercator series `log(1 + x) = x - x²/2 + x³/3 - ···` at `x = 1` | Mercator 1668 | Pre-1882 (foundational) |
| Basel problem `∑ 1/k² = π²/6` | Euler 1735 | Pre-1882 |
| Daniel Bernoulli's constant-determination method for trig series | Bernoulli ante 1782 | Pre-1882 |
| Geometric/cotangent series `Q = (1/2) cot(u/2)` | Pre-Euler trigonometry; Vol 1 Cap. V level | Pre-1882 |
| Term-by-term integration (Abel summation context) | Cauchy 1821; methodology established by 1821 | Pre-1882 |
| Sawtooth Fourier series `∑ sin(ku)/k = (π - u)/2` | Vol IV Supp V §40, originally Novi Comm XIX (1774) | Pre-1882 |
| **Log-sin Fourier series `∑ cos(ku)/k = -log(2 sin(u/2))`** | **Vol IV Supp V §51, originally Novi Comm XIX (1774)** | **Pre-1882** |
| Bernoulli-polynomial Fourier series (`P''`, `P^IV`, etc.) | Vol IV Supp V §41-43, originally Novi Comm XIX | Pre-1882 |
| `∫_0^1 (z - 1) dz / log z = log 2` | Vol IV Supp V §3-5, originally Novi Comm XIX | Pre-1882 |
| Frullani `∫_0^1 (z^m - z^n) dz / log z = log((m+1)/(n+1))` | Vol IV Supp V §6, originally Novi Comm XIX | Pre-1882 |
| Poisson-kernel orthogonality `∫_0^π cos(λΦ) dΦ/(1 - 2a cos Φ + a²)^{n+1} = π a^λ V/(1-a²)^{2n+1}` | Vol IV Supp IV §21+, originally academy presentation 1778 | Pre-1882 |
| **Integral identity `∫_0^π log sin u du = -π log 2`** | **Derivable in one elementary step from Vol IV Supp V §51** | **Pre-1882 (derivable, not stated)** |
| 1845 *editio tertia* typesetting / numbering | Editorial 1845 | Post-1882 in calendar, transcendence-free |

The entire chain is pre-1882 in calendar and transcendence-free in
methodology, admissible under [memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md)
§"Audit criterion: content, not calendar" without caveat.

---

## 7. Trust Boundary

### This brief should be cited for

- the location of the Fourier series `∑ cos(ku)/k = -log(2 sin(u/2))` at
  Vol IV Supplementum V §51, originally *Nova Methodus quantitates
  integrales determinandi*, *Novi Commentarii Academiae Scient.
  Petropolitanae* Tom. XIX, pp. 66-102 (~1774);
- the methodology of constant-determination via the alternating harmonic
  series at `u = π`, attributed by Euler at p. 285 to **Daniel
  Bernoulli**;
- the **derivation** (one elementary step from §51) of
  `∫_0^π log sin u du = -π log 2`, with all steps pre-1882-safe in
  content;
- the integral identity `∫_0^1 (z-1) dz / log z = log 2` at Supp V §5
  (Frullani-type companion identity);
- the Fourier series of the sawtooth wave at Supp V §40, attributed to
  the same Bernoulli-Euler methodology;
- the Bernoulli-polynomial Fourier series `∑ cos(ku)/k², ∑ sin(ku)/k³,
  ∑ cos(ku)/k⁴, ...` at Supp V §41-43, with closed forms involving
  `ζ(2) = π²/6`, `ζ(4) = π⁴/90`;
- the Poisson-kernel orthogonality identities at Supp IV §21+,
  originally presented to the Academy 13 August 1778;
- the source attribution of Supp IV §17+ to academy presentation 31
  August 1778;
- the structural fact that Vol IV is organized as eleven Supplementa,
  each tied to a Caput of Vols I-III (Supp I-X) or to Vol III's end
  (Supp XI on calculus of variations).

### This brief should NOT be cited for

- the *closure* of the KHLA `π log 2` transcendence-content audit (this
  brief locates the Vol IV anchor for the identity itself; whether using
  the identity inside a Liouville-style argument smuggles L-W content
  remains a separate audit);
- the explicit statement of `∫_0^π log sin u du = -π log 2` as Euler's
  own assertion in Vol IV (the Fourier series is in §51; the integral
  evaluation is one step away but the brief does not certify Euler
  states the integral form *as such* in the chapters read);
- chapters of Vol IV not read here (Supplementa II, VI-X, and most of
  Supp I and III). These cover Tom. I Cap. III, Tom. II's chapters, and
  most of Tom. III; they may contain additional definite-integral
  evaluations not surveyed here;
- modern transcendence content (Vol IV has none, and this brief does
  not import any);
- a full English-translation review of the Latin text (the brief reads
  the Latin directly with attention to mathematical content, not as a
  translation deliverable).

### Provenance tag for the program

**Pre-1882 in calendar (Novi Commentarii XIX, 1774; collected 1794;
*editio tertia* reprint 1845) and transcendence-free in content.** The
brief provides the second pre-1882 anchor for the KHLA route's
log-bearing audits, complementing
[memos/EULER-1768-INTEGRAL-BRIEF.md](memos/EULER-1768-INTEGRAL-BRIEF.md)
which provided the Vol 1 Beta-reflection anchor for the sine-product
cancellation candidate. The two briefs together pin the KHLA branch (i)
audit targets to verified pre-1882 sources. Methodology audit on use is
separate.

---

## Closing Sentence

This brief locates `∫_0^π log sin u du = -π log 2` to its proper Vol IV
source: Supplementum V §51, derived from the Fourier series
`∑ cos(ku)/k = -log(2 sin(u/2))` (originally *Novi Commentarii* XIX,
~1774) by one additional step of elementary `cos(ku)`-orthogonality on
`[0, π]`. The methodology — constant-determination via alternating
harmonic series at `u = π`, giving `-log 2` — is explicitly attributed
by Euler to **Daniel Bernoulli** (p. 285), pushing the lineage further
pre-1882. The KHLA `π log 2` audit thread, previously held open after
[memos/EULER-1768-INTEGRAL-BRIEF.md](memos/EULER-1768-INTEGRAL-BRIEF.md)
reported the Vol 1 misscoping, can now be re-attached to a verified
pre-1882 Vol IV source. The transcendence-content audit on **using**
the identity inside a Liouville-style argument is independent of this
sourcing audit and remains open.
