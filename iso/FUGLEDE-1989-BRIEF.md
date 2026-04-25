# FUGLEDE-1989-BRIEF

Source-extraction memo on Bent Fuglede, "Stability in the Isoperimetric
Problem for Convex or Nearly Spherical Domains in `R^n`," *Transactions
of the American Mathematical Society* 314, no. 2 (Aug. 1989),
pp. 619–638
([sources/Fuglede-StabilityIsoperimetricProblem-1989.pdf](sources/Fuglede-StabilityIsoperimetricProblem-1989.pdf)).
JSTOR stable URL 2001401.

**Why this brief exists.** Stability companion to
[iso/OSSERMAN-1979-BRIEF.md](iso/OSSERMAN-1979-BRIEF.md) in the
isoperimetric coordination at
[iso/DIDOS-PREROGATIVE.md](iso/DIDOS-PREROGATIVE.md). Where
Osserman 1979 surveys the Bonnesen-style geometric route (lower bounds
on `Δ` in terms of `R − ρ`, `d`), Fuglede 1989 supplies the *Sobolev*
route — converting `Δ → 0` into uniform and Sobolev 1-norm convergence
of the radial deviation `u` to zero, with explicit constants and rates,
across all dimensions `n ≥ 2`.

**What was read.** All 21 pages: Introduction, §1 (nearly spherical
domains), §2 (convex bodies), §3 (sharpness examples), and the
reference list [1]–[10]. Read with two lenses: *what Fuglede first
proves vs. extends from preceding authors*, and *what Fuglede's
theorems give when specialized to the inscribed regular polygon family
on which [corners/HURWITZ-GAP.md](corners/HURWITZ-GAP.md) computes
`Δ_n ~ 4π⁴/(3n²)`*.

**Confidence level.** High on the paper's mathematical claims —
Theorems 1.2 and 2.3 are explicitly stated with constants, and the
proofs are worked through. High on the per-result attribution from the
Introduction, §1 opener, and Footnote 4 (these explicitly distinguish
new content from Fuglede 1986 [6] and from the Bonnesen 1924 / Osserman
1987 precedents). High on the regular-polygon specialization
computations done in this brief; they are elementary expansions of the
inscribed regular `n`-gon's `R(θ)`. Note: dimension index `n` in
Fuglede vs. polygon vertex count `n` in the program — this brief uses
`n` as Fuglede does (dimension) when stating his theorems, and `n` as
the polygon vertex count in §2 of this brief; the disambiguation is
flagged each time.

**Trust boundary up front.** This brief audits *what the paper says*
about isoperimetric stability. It does not claim Fuglede's tools
specialize to the program's `K_n` ladder or to algebraic-degree
content. It does establish a precise compatibility statement between
Fuglede's H¹ Sobolev result (in `n_dim = 2`) and the program's
existing Hurwitz/strip-H¹ identification.

---

## 1. Main Theorems Precisely

### 1.1 Setup and definitions

Throughout `n ≥ 2` is the *ambient dimension* (Fuglede's notation).
Let `D ⊂ R^n` be a compact starshaped domain with Lipschitz boundary
`∂D`, with volume `V` and surface area `S`, and let `ω_n` be the
volume of the unit ball `Ω` in `R^n`. Define `v` and `s` by
`V = ω_n v^n`, `S = nω_n s^{n-1}`.

**Isoperimetric deficiency** (Fuglede's eq. (1)):

```
Δ = (S / (nω_n)) · (V / ω_n)^{−(n−1)/n} − 1 = (s/v)^{n−1} − 1.
```

This is dimensionless. The classical isoperimetric inequality is
`Δ ≥ 0`, with equality only for the ball. Note `Δ = 0` is equivalent
to `s = v`, i.e. surface-area radius equals volume radius.

**Normalization.** After translating so the barycentre `b = 0` and
homothetically scaling so `v = 1` (i.e. `V = ω_n`), the boundary
admits a polar representation

```
R(ξ) = 1 + u(ξ),   ξ ∈ Σ = unit sphere in R^n.
```

The function `u` is Lipschitz and `u(ξ)` is the radial deviation of
`∂D` from the unit sphere `Σ`. Norms `||·||_p` are taken with
respect to the *normalized* surface measure on `Σ`.

**Nearly-spherical hypothesis** (Definition 1.1):

```
(*)   ||u||_∞ ≤ a := 3/(20n),    ||∇u||_∞ ≤ 1/2.
```

For `n_dim ≥ 3`, the gradient bound follows from the uniform bound
(Lemma 2.2). For `n_dim = 2`, both must be hypothesized.

**Spherical deviation** (Definition 2.1, for convex bodies):

```
d = min{α ≥ 0 : (1−α)_+ Ω ⊂ v^{-1}(D − b) ⊂ (1+α)Ω}.
```

For a normalized convex body, `||u||_∞ = d`. So `d` is the Hausdorff
distance from the normalized body to the unit ball.

### 1.2 Theorem 1.2 — nearly spherical stability

For any nearly spherical domain `D` in `R^n`:

```
(I.a)   (1/10)(||u||_2² + ||∇u||_2²) ≤ Δ ≤ (3/5)||∇u||_2²
```

```
(I.b)   ||u||_∞^{n−1} ≤ {
            A · Δ^{1/2}                              for n_dim = 2,
            A · Δ · log(A' ||∇u||_∞² / Δ)             for n_dim = 3, Δ > 0,
            A · ||∇u||_∞^{n−3}                       for n_dim ≥ 4
        }
```

with constants `A`, `A'` depending only on `n_dim` and explicitly
calculable. **Explicit values per Remark 1.5:**

- `n_dim = 2`: `A = 6.4`. The constants `1/10` and `3/5` in (I.a) can
  be replaced by `0.24` and `0.54`. If one cancels the `||u||_2²`
  term, `1/10` may even be replaced by `0.30`.
- `n_dim = 3`: `A = 18.5`, `A' = 16.5`. The constants `1/10` and
  `3/5` in (I.a) can be replaced by `1/4` and `1/2`. With `||u||_2²`
  cancelled, `1/10` can be replaced by `0.29`.
- `n_dim ≥ 4`: `A = 10 · B · (38/35 · 43/37)^{n−1}`, where
  `B = K · (n−1)/4 · (π(n−1)/(n−3))^{n−2}` and `K = ∫₀^π sin^{n−2}φ dφ`
  (from Lemma 1.4).

The right inequality in (I.a) `Δ ≤ (3/5)||∇u||²` is the easy half;
the left inequality `(1/10)(||u||² + ||∇u||²) ≤ Δ` is the technical
content.

**Hypothesis class.** Compact starshaped Lipschitz-boundary domain
with the nearly-spherical condition (*). *No convexity assumed.*

**Conclusion.** Both an L²-and-H¹ Sobolev bound (I.a) and a uniform
L^∞ bound (I.b) on the radial deviation `u`, in terms of `Δ`. The
L^∞ bound has dimension-dependent rates: `Δ^{1/2}` in `n_dim = 2`,
`(Δ log(...))^{1/(n−1)}` in `n_dim = 3`, and a degenerate
`||∇u||_∞^{(n−3)/(n−1)}` form in `n_dim ≥ 4` that gets replaced by
`Δ^{2/(n+1)}` in Theorem 2.3 once convexity is brought in.

### 1.3 Theorem 2.3 — convex body stability

For a convex body `D ⊂ R^n` (`n ≥ 3`) with isoperimetric deficiency
`Δ < η`:

```
(II)   d = ||u||_∞ ≤ {
            C · (Δ log(1/Δ))^{1/2}    for n_dim = 3,
            C · Δ^{2/(n+1)}            for n_dim ≥ 4
        }
```

Constants `C` and `η > 0` depend only on `n_dim` and are explicitly
calculable. **For n_dim = 3:** `η = 1.04... × 10⁻⁵`, `C = 4.56`.

**The case `n_dim = 2`** is contained in **Bonnesen 1924** [2] and
included by Fuglede only "for comparison" (his footnote 4). Bonnesen's
inequality `(r₂ − r₁)² ≤ L²/(4π) − A` (in plane geometric form, from
Osserman's eq. (33) with constant `4π`) supplies the same stability
statement with `f(Δ) = C√Δ`.

**Hypothesis class.** Convex body in `R^n` (`n_dim ≥ 3`); no
nearly-spherical hypothesis (the hypothesis `Δ < η` automatically
implies (*) via the parallel-body argument and Lemma 2.2).

**Sharpness.** Fuglede asserts (p. 619 abstract; §3) that the
estimate is "sharp as regards the order of magnitude of `f`." Sharp
constructions in §3:
- `n_dim = 3`: §3.1, an explicit one-parameter family `D_α` with
  `Δ ≈ α⁴ log(1/α)`, `||u||_∞ ≈ α² log(1/α)`, giving
  `||u||_∞² ≳ const · Δ log(1/Δ)`. This shows the `(Δ log(1/Δ))^{1/2}`
  rate is best possible up to `C`.
- `n_dim ≥ 4`: §3.2, convex hull of unit ball with two truncated
  cones gives `Δ ≈ α^{n+1}`, `d ≈ α²`, hence `d ≈ Δ^{2/(n+1)}`.

### 1.4 What Fuglede first proves vs. extends or sharpens

**Bonnesen 1924 [2].** Established the n_dim = 2 case of (II): for a
plane convex body, `(r₂ − r₁)² ≤ (L²/(4π)) − A`. Equivalently,
`Δ_F ≥ const · d²`, i.e., `d ≤ const · Δ_F^{1/2}`. This is the
n_dim = 2 case of Theorem 2.3.

**Bernstein 1905 [1].** Equivalent inequality for the plane case as
limit from sphere; constant ≈ 1700, much weaker than Bonnesen's.

**Fuglede 1986 [6].** The n_dim = 3 case of Theorem 1.2 (I.a) — the
Sobolev 1-norm bound for nearly spherical domains in `R³`. Per
Fuglede 1989 §1 opener (p. 621): "*The stated equivalence between the
square root of the isoperimetric deficiency `Δ` of a domain `D`
satisfying (*) and the Sobolev 1-norm of `u`, as expressed in (I.a),
was established in [6] for the case `n = 3` by almost the same method
as in the present paper, and it was shown that some restriction like
(*) above is necessary for stability — whether in uniform norm or in
Sobolev 1-norm as in (I.a).*"

**Osserman 1987 [10]** ("A strong form of the isoperimetric inequality
in `R^n`," Complex Variables 9). Established a related bound on the
ratio `(r − ρ)/ρ` (circumradius minus inradius, divided by inradius)
in terms of `Δ_1`, the inradius-version of the isoperimetric
deficiency. Per Fuglede §2.7 (p. 634): Theorem 2.3 *implies* this
Osserman result, but Osserman's result yielded a "quantitatively much
weaker" stability than Theorem 2.3 (loseness rooted in Osserman's
nontrivial estimate of `δ/ρ` from Bonnesen, [3, p. 135]).

**Fuglede 1989 [present] first proves:**

1. **Theorem 1.2 for all n_dim ≥ 2** with explicit constants. The
   method is "almost the same" as in [6] but extended to all
   dimensions and with explicit `A`, `A'`, `B`.
2. **Theorem 2.3 for n_dim ≥ 3** with the `(Δ log(1/Δ))^{1/2}`
   rate (n_dim = 3) and `Δ^{2/(n+1)}` rate (n_dim ≥ 4). The
   precursor (preliminary version) used Bonnesen [3, p. 135] for
   n_dim = 3 and Osserman [10] for general n_dim ≥ 3, and yielded a
   "much smaller value of `η`" — Fuglede 1989 sharpens to the
   present `η`.
3. **Sharpness of the rate** in §3 via explicit examples — the
   rates `(Δ log(1/Δ))^{1/2}` (n_dim = 3) and `Δ^{2/(n+1)}`
   (n_dim ≥ 4) are best possible up to the constant `C`.
4. **Lemma 2.2** quantifies how convexity yields the gradient bound
   `||∇u||_∞ ≤ 2d^{1/2}(1 + d)/(1 − d)` from the uniform bound `d`
   alone. This is the bridge that lets Theorem 2.3 dispense with the
   gradient half of (*).

### 1.5 Proof technique

The proof of Theorem 1.2 (I.a) uses **spherical harmonics** on `Σ`.
Decompose `u = Σ_{k≥0} a_k Y_k` where `Y_k` are normalized
eigenfunctions of `−∇²_Σ` with eigenvalue `k(k + n − 2)`. Then

```
||u||² = Σ a_k²,    ||∇u||² = Σ k(k + n − 2) a_k².
```

The volume normalization (eq. (10): `∫_Σ v dσ = 0` after substituting
`v = ((1+u)^n − 1)/n`) and barycentre normalization (eq. (8)) force
`a_0` and `a_1` to be small (eq. (19): `a_0, a_1 ≤ α||u||` with
`α = 3/38`).

The technical estimate (eq. (16)):

```
Δ ≥ −(n−1)β||u||² + γ||∇u||²,    β = 43/74,    γ = 714/1805.
```

Combining (16) with the smallness of `a_0, a_1`, and choosing a
positive constant `κ_n < γ`, gives the Sobolev 1-norm lower bound
in (I.a) with `κ_n` in place of `1/10` (the constant `κ_n` is
explicitly computed; for n_dim = 2, `κ_2 = 0.102... > 1/10`; for
n_dim = 3, `κ_3 = 0.171...`).

The proof of (I.b) uses **Lemma 1.4**, a Sobolev-type embedding from
H¹ into L^∞ on the unit sphere `Σ`, with explicit constants depending
on `n_dim`.

The proof of Theorem 2.3 uses the **parallel-body method**. For a
convex body `D` and `λ ≥ 0`, the parallel body `D(λ) = D + λΩ` has
`Δ(λ)` decreasing to 0 (Lemma 2.5, via Minkowski's inequality). For
sufficiently large `λ`, `D(λ)/v(λ)` is squeezed close to the unit ball
in Hausdorff metric (eq. (40), (41)), so `d(λ) → 0`. Combined with
Lemma 2.2 (gradient bound from convexity) and Theorem 1.2, this
forces `d(λ) ≤ f(Δ(λ))`. Continuity of `d(λ)` and `Δ(λ)` in `λ`
(Lemma 2.4) plus a contradiction-by-continuity argument concludes
that `d(0) ≤ f(Δ(0))`.

The technique inventory is therefore **Sobolev / spherical harmonics
+ Minkowski's inequality / parallel bodies + convex-body Lipschitz
continuity in Hausdorff metric**. *Not* Steiner symmetrization, *not*
integral geometry, *not* Bonnesen-style support functions or interior
parallels. The Hurwitz Fourier identity is acknowledged in Footnote 1
(p. 619) as the n_dim = 2 motivation: "*Still another proof — quite
short — can be read off from Hurwitz' Fourier series proof of the
isoperimetric inequality in the plane [8], and that leads in a certain
sense to a stronger inequality, involving a Sobolev 1-norm of the
deviation of `∂D` from a circle, again estimated in terms of
`L² − 4πA`, see [6].*" Reference [8] is Hurwitz 1902. So in n_dim = 2
the spherical-harmonics method *is* Hurwitz Fourier, and Fuglede 1986
[6] is the explicit n_dim = 2 + 3 derivation in that register.

---

## 2. Specialization to Regular n-Gons

For this section the symbol `n` denotes the *polygon vertex count*
(program convention, matching
[corners/HURWITZ-GAP.md](corners/HURWITZ-GAP.md)). Fuglede's
*ambient dimension* is fixed at `2` throughout this section. The
notational clash is unavoidable; the reader should hold both meanings.

### 2.1 Computing Fuglede `Δ` for the inscribed regular n-gon

For the inscribed regular n-gon in the unit circle (program convention,
circumradius = 1), perimeter `L_n = 2n sin(π/n)` and area
`A_n = (n/2) sin(2π/n)`. Hurwitz's `Δ_H = L² − 4πA` (per
[corners/HURWITZ-GAP.md](corners/HURWITZ-GAP.md)) gives

```
Δ_H,n = 4π⁴/(3n²) + O(1/n⁴).
```

Fuglede's `Δ_F` (his eq. (1) in dimension 2) is

```
Δ_F = (s/v)^{n_dim − 1} − 1 = s/v − 1 = L/(2√(πA)) − 1
    = (L − 2√(πA)) / (2√(πA))
    (n_dim = 2).
```

Squaring `Δ_F + 1 = L/(2√(πA))`:

```
(Δ_F + 1)² = L²/(4πA) = 1 + Δ_H/(4πA),
```

so for small `Δ_F`:

```
Δ_H ≈ 8πA · Δ_F.
```

For the inscribed regular n-gon `A_n → π`, so

```
Δ_F,n ≈ Δ_H,n / (8π²) = (4π⁴/(3n²)) / (8π²) = π²/(6n²) + O(1/n⁴).
```

**Rate:** `Δ_F,n = π²/(6n²) + O(1/n⁴) = Θ(1/n²)`.

### 2.2 Computing the radial deviation `u` after Fuglede normalization

To apply Fuglede the polygon must be normalized: scaled so its volume
is `π = ω_2`. The original area is `A_n = (n/2)sin(2π/n) < π`, so
scale by `√(π/A_n) > 1`. The normalized polygon has inradius
`ρ_n = √(π/A_n) · cos(π/n)` and circumradius
`R_n = √(π/A_n)`. The radial function `R(θ) = 1 + u(θ)` after
normalization runs from `R(midpoint of edge) = ρ_n` to
`R(vertex) = R_n`.

Taylor at large `n`:

```
√(π/A_n) = (π / ((n/2) sin(2π/n)))^{1/2}
        = (1 + π²/(3n²) + O(1/n⁴))^{1/2}
        = 1 + π²/(6n²) + O(1/n⁴),

cos(π/n) = 1 − π²/(2n²) + O(1/n⁴).
```

So

```
u_max = √(π/A_n) − 1 = π²/(6n²) + O(1/n⁴),
u_min = √(π/A_n) cos(π/n) − 1
      = (1 + π²/(6n²))(1 − π²/(2n²)) − 1 + O(1/n⁴)
      = −π²/(3n²) + O(1/n⁴),

||u||_∞ = max(|u_max|, |u_min|) = π²/(3n²) + O(1/n⁴).
```

**L^∞ rate:** `||u||_∞ = π²/(3n²) + O(1/n⁴) = Θ(1/n²)`.

### 2.3 Computing the Sobolev seminorms

Within each sector `−π/n ≤ φ ≤ π/n` (where `φ` is the angle from
the inradius midpoint), `R(φ) = √(π/A_n) cos(π/n) / cos(φ)`.
Differentiating,

```
R'(φ) = √(π/A_n) cos(π/n) · sin(φ) / cos²(φ).
```

So `u'(φ) = R'(φ)`. At the sector boundary `φ = ±π/n` the function
has a corner (jump in `u'` across the polygon vertex). Within the
sector, `|u'(φ)| ≤ √(π/A_n) cos(π/n) · tan(π/n)/cos(π/n) ~ π/n` for
the typical sector angle `φ ~ π/n`.

```
||∇u||_∞ ~ π/n + O(1/n³) = Θ(1/n).
```

For `||∇u||_2²`, integrate over `Σ`: each sector contributes
`∫_{-π/n}^{π/n} |u'(φ)|² dφ / (2π) ~ (π/n)² · (2π/n)/(2π) = const/n³`,
times `n` sectors → total `Θ(1/n²)`.

```
||∇u||_2² = Θ(1/n²).
```

For `||u||_2²`: each sector contributes `Θ((1/n²)² · 1/n) = Θ(1/n⁵)`,
times `n` → `Θ(1/n⁴)`.

```
||u||_2² = Θ(1/n⁴).
```

### 2.4 What Fuglede's theorems predict for the inscribed regular n-gon

Substituting into **Theorem 1.2 (I.a)** (n_dim = 2 case):

```
(1/10)(||u||_2² + ||∇u||_2²) ≤ Δ_F ≤ (3/5)||∇u||_2².
(1/10) · (Θ(1/n⁴) + Θ(1/n²)) ≤ Θ(1/n²) ≤ (3/5) · Θ(1/n²).
(1/10) · Θ(1/n²)              ≤ Θ(1/n²) ≤ (3/5) · Θ(1/n²).
```

Both sides scale as `1/n²`. **The bound is two-sided sharp up to
multiplicative constants on the inscribed regular n-gon family.** The
constants `1/10` and `3/5` (or per Remark 1.5, `0.24` and `0.54`)
bracket the actual ratio `Δ_F / (||u||² + ||∇u||²)`.

Substituting into **Theorem 1.2 (I.b)** (n_dim = 2 case)
`||u||_∞ ≤ A · Δ^{1/2}` with `A = 6.4`:

```
||u||_∞ ≤ 6.4 · Θ(1/n²)^{1/2} = 6.4 · Θ(1/n) = Θ(1/n).
```

**Actual** `||u||_∞ = Θ(1/n²)`. **Theorem 1.2 (I.b) is loose by a
factor of `n`** on this family — it predicts `1/n` decay, the actual
decay is `1/n²`.

Substituting into **Theorem 2.3** (n_dim = 2 case, which is Bonnesen
1924): `d ≤ C · Δ^{1/2}`. Same as (I.b) above, same loseness.

### 2.5 Convergence rate and metric

Stating the user's question precisely:

| Metric | Actual rate (computed) | Fuglede bound | Sharpness |
|--------|------------------------|---------------|-----------|
| `Δ_F` | `Θ(1/n²)` | -- | -- |
| `(\|\|u\|\|² + \|\|∇u\|\|²)^{1/2}` (H¹ Sobolev) | `Θ(1/n)` | `(10 Δ_F)^{1/2} = Θ(1/n)` | **Sharp** |
| `\|\|∇u\|\|_2` (H¹ seminorm only) | `Θ(1/n)` | `(5/3)^{1/2} Δ_F^{1/2} = Θ(1/n)` | **Sharp** |
| `\|\|u\|\|_∞` (Hausdorff distance to inscribed disk) | `Θ(1/n²)` | `6.4 · Δ_F^{1/2} = Θ(1/n)` | **Loose by factor `n`** |

So Fuglede's H¹ Sobolev result (I.a) **captures the correct rate**
`Θ(1/n)` for the H¹ Sobolev norm of the radial deviation, with sharp
constants on the inscribed regular n-gon family. Fuglede's L^∞
estimate (Theorem 2.3, Theorem 1.2 (I.b) for n_dim = 2) **predicts
`O(1/n)`, while the true uniform deviation is `Θ(1/n²)`** — loose by
a factor of `n`. The L^∞ loseness is the same loseness Bonnesen 1924
exhibits; this is unsurprising since Theorem 2.3 in n_dim = 2 *is*
Bonnesen 1924 (Fuglede's footnote 4).

### 2.6 Relationship to existing program content

Three program memos already lean on the H¹ Sobolev / Hurwitz Fourier
register:

- [corners/HURWITZ-GAP.md](corners/HURWITZ-GAP.md) computes `Δ_H,n`
  three ways for the inscribed regular n-gon, including via the
  Hurwitz Parseval identity `Δ = 4π² Σ m(m−1)|c_m|²`. Sparse Fourier
  support `c_m = 0` unless `m ≡ 1 (mod n)` gives the leading term
  `4π⁴/(3n²)` from `m = 1 + n`.
- [memos/STRIP-H1-HURWITZ-CLOSURE.md](memos/STRIP-H1-HURWITZ-CLOSURE.md)
  identifies the strip-side `H¹` seminorm with the Hurwitz
  isoperimetric gap, leading-order. The strip-side `H¹` is the
  parametrization-equivalent of Fuglede's `||∇u||_2²` on `Σ`.
- [memos/ARCHIMEDEAN-SIGNATURE.md](memos/ARCHIMEDEAN-SIGNATURE.md) and
  [memos/STRIP-TISSUE-FOURIER.md](memos/STRIP-TISSUE-FOURIER.md) read
  the gap as one face of the Archimedean `1/n²` signature.

**Verdict on the relationship.**

- **Agreement.** Fuglede's Theorem 1.2 (I.a) for n_dim = 2 and the
  program's strip-`H¹` identification are **structurally identical
  content** in a slightly different presentation. Both put `Δ` into a
  Sobolev 1-norm register for the radial / strip-tissue deviation;
  both give the rate `Θ(1/n²)` for the inscribed regular n-gon.
  Fuglede's footnote 1 explicitly traces this to Hurwitz 1902 via
  Fuglede 1986 [6]. The methodological ancestry is the same Hurwitz
  Fourier line.
- **Sharpening (contributed by Fuglede).** Fuglede 1989 supplies
  *explicit constants* `(1/10, 3/5)` in (I.a) — which can be
  improved to `(0.24, 0.54)` per Remark 1.5 — that the program's
  qualitative `Δ ~ ||∇u||²` agreement does not pin down. For the
  K-H-L-A endgame requiring quantitative estimates, these explicit
  constants are real new material.
- **Sharpening (already in the program).** The Hurwitz Parseval
  identity in [corners/HURWITZ-GAP.md](corners/HURWITZ-GAP.md) is an
  *equality*, not a two-sided inequality — refining Fuglede's
  Sobolev bound (I.a) to an exact decomposition into Fourier
  coefficients. In the n_dim = 2 case where Fuglede's spherical
  harmonics on `Σ = S¹` reduce to ordinary Fourier series, the two
  are mathematically identical content; the program has the sharper
  exact form.
- **Divergence (Fuglede's L^∞ stability is qualitatively weaker for
  this family).** Theorem 2.3 / Theorem 1.2 (I.b) predicts `Θ(1/n)`
  L^∞ deviation; the true rate is `Θ(1/n²)`. The program has no
  reason to prefer Fuglede's L^∞ form over the explicit Hurwitz /
  strip-`H¹` rate it already has.
- **Independence (Fuglede's higher-dimensional content).** Theorems
  for n_dim ≥ 3 are entirely outside the program's plane-curve
  scope. They are *not* in conflict with anything in the repo; they
  are simply not used. The program operates in `R²` for the circle
  side; the higher-dimensional Fuglede results are filed as "in
  scope of DIDOS-PREROGATIVE but not specialized."

**Net.** For the program's plane-curve regime, Fuglede 1989 is a
*formal restatement and constant-explicitization* of the
Hurwitz-Sobolev content the program already has, plus higher-
dimensional generalization the program does not currently need.
There is no methodological conflict, no novel rate, and the
sharpest content for the program's purposes (the Parseval exact
form) lives in
[corners/HURWITZ-GAP.md](corners/HURWITZ-GAP.md). What Fuglede
contributes additionally: explicit constants, sharpness examples,
and the convex-body extension (Theorem 2.3) that drops the
nearly-spherical hypothesis.

---

## 3. Trust Boundary

### This brief should be cited for

- The precise statement of **Theorem 1.2** (nearly-spherical stability,
  all `n_dim ≥ 2`): Sobolev (I.a) with constants
  `(1/10, 3/5)` (improvable to `(0.24, 0.54)` for n_dim = 2 per
  Remark 1.5), and uniform (I.b) with explicit `A`, `A'` per
  Remark 1.5.
- The precise statement of **Theorem 2.3** (convex-body stability,
  `n_dim ≥ 3`): `d ≤ C(Δ log(1/Δ))^{1/2}` for n_dim = 3 with
  `C = 4.56`, `η = 1.04 × 10⁻⁵`; `d ≤ C · Δ^{2/(n+1)}` for
  n_dim ≥ 4. The n_dim = 2 case is **Bonnesen 1924** [2], not new
  in this paper.
- The proof technique: **spherical harmonics on `Σ` + Minkowski
  parallel-body argument**; explicitly *not* Steiner symmetrization,
  integral geometry, or interior parallels.
- The acknowledgement (Footnote 1, p. 619) that **Hurwitz 1902 [8]
  Fourier proof yields the same Sobolev 1-norm content** — Fuglede
  1989 is methodologically a higher-dimensional generalization of
  the Hurwitz Fourier line.
- The per-author historiography: Bonnesen 1924 (n_dim = 2 of
  Theorem 2.3); Bernstein 1905 (precursor with weak constant);
  Fuglede 1986 [6] (n_dim = 3 of Theorem 1.2 (I.a));
  Osserman 1987 [10] (related `(r − ρ)/ρ` bound, weaker than
  Theorem 2.3); Fuglede 1989 [present] (all n_dim ≥ 2 with
  explicit constants and sharpness).
- The specialization to the inscribed regular n-gon family: Fuglede's
  H¹ Sobolev bound (I.a) gives the **sharp** rate `Θ(1/n²)` for
  `Δ`; Fuglede's L^∞ bounds (I.b, Theorem 2.3) give a **loose** rate
  `O(1/n)` versus the actual `Θ(1/n²)` for the L^∞ deviation; the
  true L^∞ rate for inscribed regular n-gons is recoverable but not
  via Fuglede.

### This brief should NOT be cited for

- Specialization of Fuglede's tools to `K_n`, `Q(ζ_n)`, or any
  cyclotomic content (not in the paper).
- Algebraic-degree / closure-mismatch material (not in the paper).
- Sharper-than-Sobolev bounds for the inscribed regular n-gon (the
  Hurwitz Parseval identity in
  [corners/HURWITZ-GAP.md](corners/HURWITZ-GAP.md) is sharper, not
  derivable from Fuglede).
- The L^∞ rate `Θ(1/n²)` for inscribed regular n-gons (this is
  computed in §2.2 of *this brief* by elementary expansion of `R(θ)`,
  not by appeal to any Fuglede theorem).
- Anything about asymmetric perturbations of the circle outside the
  nearly-spherical or convex hypotheses.

### Provenance tag for the program

**Methodologically post-1965 stability-theory paper of post-1882
origin.** Fuglede 1989 is purely post-L-W: the spherical-harmonics
method, Sobolev embeddings, Minkowski's mixed-volume inequalities,
parallel-body arguments — all developed in their modern forms during
the 20th century. Pre-L-W substrate available for the n_dim = 2
content (which is Bonnesen 1924 plus Hurwitz 1902 plus the Sobolev
register Fuglede 1986 made explicit): Hurwitz Fourier identity is
1902 (post-L-W by 20 years but contains no transcendence input);
Bonnesen 1924 is post-L-W by 42 years (per
[iso/OSSERMAN-1979-BRIEF.md](iso/OSSERMAN-1979-BRIEF.md), all
quantitative Bonnesen-style strengthenings are post-L-W). For the
K-H-L-A endgame, the n_dim = 2 Sobolev content can be re-routed
through Hurwitz 1902 (no transcendence input) with explicit
constants supplied by Fuglede 1989. The audit is then a check that
the Fuglede 1989 spherical-harmonics derivation can be re-rendered in
n_dim = 2 as a direct Hurwitz Fourier computation — which, per
Fuglede's own footnote 1, it can.

---

## Closing Sentence

This brief contributes the precise statement of Fuglede 1989's two
main stability theorems — Theorem 1.2 (nearly-spherical, Sobolev L²
+ H¹ and uniform L^∞ bounds, all `n_dim ≥ 2`, explicit constants per
Remark 1.5) and Theorem 2.3 (convex-body L^∞ stability, n_dim ≥ 3
with rates `(Δ log(1/Δ))^{1/2}` for n_dim = 3 and `Δ^{2/(n+1)}` for
n_dim ≥ 4, n_dim = 2 contained in Bonnesen 1924). It records the
historiography: Bonnesen 1924 supplied the n_dim = 2 case; Fuglede
1986 [6] supplied the n_dim = 3 H¹ Sobolev case; Osserman 1987 [10]
supplied a related `(r − ρ)/ρ` bound; Fuglede 1989 [present] extends
to all `n_dim ≥ 2` with explicit constants and sharpness examples.
Specialized to the inscribed regular n-gon family, Fuglede's H¹
Sobolev result (Theorem 1.2 (I.a)) **agrees with the program's
existing Hurwitz / strip-H¹ content** and gives the sharp rate
`Θ(1/n²)` for `Δ`, with explicit constants `(1/10, 3/5)`. Fuglede's
L^∞ stability result for n_dim = 2 (which is Bonnesen 1924) gives a
loose `O(1/n)` rate versus the actual `Θ(1/n²)` for `||u||_∞` —
**same loseness Bonnesen exhibits**, by the same identity. This brief
is the stability companion to
[iso/OSSERMAN-1979-BRIEF.md](iso/OSSERMAN-1979-BRIEF.md) for
[iso/DIDOS-PREROGATIVE.md](iso/DIDOS-PREROGATIVE.md): Osserman
covers the geometric Bonnesen route, Fuglede covers the Sobolev /
Hurwitz route, and on the program's regular-polygon test case
Fuglede's H¹ register agrees with the program's existing content
while his L^∞ register reproduces Bonnesen's loseness.

---

## Appendix: Footnote 1 and the `5π` Conversion Overhead

*Follow-up reading; not part of the original lens. Triggered by
Fuglede's footnote 1 statement (p. 619) that the Hurwitz Fourier
proof "*also leads to Bonnesen's inequality with a constant factor
`c (= 5π)` on the right.*"*

### A.1 The exact statement

Fuglede's claim, re-rendered: the Hurwitz Fourier route yields the
plane Bonnesen-style inequality

```
(r₂ − r₁)²  ≤  c · ((L²)/(4π) − A)  =  c · Δ_H / (4π)
```

with `c = 5π` (Hurwitz Fourier proof, attributed to Fuglede 1986 [6]),
where Bonnesen 1924 [2] gives the *sharp* constant `c = 1` (and
Bonnesen further showed in [2] that the inequality fails for any
`c < 1`). So the Fourier route is weaker than the sharp Bonnesen
constant by a factor of `5π ≈ 15.7`.

### A.2 Where the conversion happens

Fuglede 1986 [6] is unread in this brief (the Bull. London Math. Soc.
volume is not in `sources/`), so the exact arithmetic is not
reconstructed here. The structural conversion sequence is identifiable
from Fuglede 1989 §1's spherical-harmonics machinery applied in
`n_dim = 2` and the standard plane Hurwitz route:

**Step (i): Hurwitz Fourier identity.** For a plane curve in
arclength parametrization with rotation index 1, the standard form is

```
L² − 4πA  =  4π² · Σ m(m−1) |c_m|²,
```

with the `m = 0` (translation) and `m = 1` (circle) modes
contributing zero. After volume / barycentre normalization in the
radial parametrization `R(θ) = 1 + u(θ)` and conversion from
arclength to angle parametrization, this leading-order yields a
Sobolev statement of the form

```
Δ_H  ≥  K_H · ||u'||_2²
```

for some constant `K_H` of order `π²` (the conversion is leading-order
in `||u||`).

**Step (ii): Sobolev embedding `H¹ → L^∞` on `S¹`.** For mean-zero
`u` on the unit circle with normalized measure `dσ = dθ/(2π)`,
expanding `u = Σ_{k≠0} c_k e^{ikθ}` and applying Cauchy–Schwarz:

```
||u||_∞  ≤  Σ_{k≠0} |c_k|  ≤  (Σ_{k≠0} 1/k²)^{1/2} (Σ_{k≠0} k² |c_k|²)^{1/2}
        =  (π/√3) · ||u'||_2.
```

The constant `π/√3 ≈ 1.81` is from `Σ_{k≠0} 1/k² = π²/3`.

**Step (iii): geometric translation.** For a normalized convex body
with optimal Bonnesen-annulus center near the barycentre,

```
(r₂ − r₁)²  ≤  (max u − min u)²  ≤  4 · ||u||_∞².
```

The factor `4` is from `max u − min u ≤ 2 ||u||_∞`. (For curves
where the optimal annulus is *not* centered at the barycentre, the
left side is smaller, so the bound is conservative.)

**Composing.** Chaining (ii) and (iii) gives
`(r₂ − r₁)² ≤ 4 · (π²/3) · ||u'||_2² = (4π²/3) ||u'||_2²`. Combining
with (i) `||u'||_2² ≤ Δ_H / K_H`:

```
(r₂ − r₁)²  ≤  (4π² / (3 K_H)) · Δ_H.
```

Comparing to `c · Δ_H/(4π)`: the conversion gives `c = 16π³/(3 K_H)`.
Fuglede's stated `c = 5π` corresponds to `K_H = 16π² / 15`. The
exact value of `K_H` extracted from the Hurwitz identity in the
radial parametrization (with the volume / barycentre constraints
fully accounted) is the technical content of Fuglede 1986 [6]; this
brief notes the conversion structure but does not derive the constant
without that reference.

**Where `5π` enters.** The factor of `5π` is *not* localized to a
single inequality; it is the product of the constants from steps (i),
(ii), (iii). Each step is sharp in its own register (Hurwitz is
exact; Cauchy–Schwarz on `Σ 1/k²` is sharp at the worst-case
coefficient distribution; `max − min ≤ 2 ||u||_∞` is sharp for
symmetric u). The `5π` is the combined Sobolev-to-geometric
*conversion overhead*: each step is sharp for its own extremal
function, but the *same* extremal function does not realize all
three sharpnesses simultaneously, so the chained bound has slack.
Bonnesen's direct proof (parallel curves on a convex body) avoids
the chaining entirely and lands at `c = 1` directly.

### A.3 Position vs. the cross-brief pattern in DIDOS-PREROGATIVE

The `5π` is a different shape of phenomenon from the metric-mismatch
gaps recorded in
[iso/DIDOS-PREROGATIVE.md](iso/DIDOS-PREROGATIVE.md) "Brief
findings" for Osserman 1979 and Fuglede 1989 on the inscribed regular
`n`-gon family. Three distinguishing features:

1. **Curve-family dependence vs. universality.** The metric-mismatch
   gap (`O(1/n²)` Sobolev rate captured sharply, `O(1/n)` L^∞ bound
   loose by factor `n`) is a property of *the inscribed regular
   n-gon family*: the L^∞ deviation has `Θ(1/n²)` decay while the
   bound's right side `Δ^{1/2}` has `Θ(1/n)` decay, mismatching by
   factor `n`. The `5π` is a *uniform constant* in a bound valid
   over *all* planar curves of small Δ_H — independent of family.
2. **Rate vs. constant.** The metric-mismatch gap is a *rate-of-decay*
   gap (different powers of `1/n` on the two sides). The `5π` is a
   *constant-factor* gap in a fixed-rate bound (both sides scale as
   `ε²` for a one-parameter family of small-deviation curves).
3. **Origin: metric choice vs. proof-method choice.** The metric-
   mismatch gap comes from *which metric is being measured* —
   Sobolev `||u'||_2` vs. uniform `||u||_∞`. Both metrics are
   well-defined on the polygon family; one captures the rate, the
   other doesn't. The `5π` comes from *which proof method derives a
   given inequality* — Hurwitz Fourier proof vs. Bonnesen
   parallel-curve proof. Both prove the geometric Bonnesen
   inequality `(r₂ − r₁)² ≤ c · Δ_H/(4π)`; one gets `c = 5π`, the
   other gets `c = 1`.

**Composition on the regular n-gon family.** Both phenomena apply
multiplicatively when the Hurwitz Fourier route is specialized to
the inscribed regular n-gon. In the 1924 annulus-width normalization
`(r₂ − r₁)² ≤ c · Δ_H/(4π)`, Bonnesen's sharp `c = 1` bound predicts
`(R − ρ)² ≤ Δ_H/(4π) ~ π³/(3n²)`, while the actual
`(R − ρ)² ~ π⁴/(4n⁴)`. This is distinct from the 1921 headline
`Δ ≥ π²(R − ρ)²`. So the annulus-width bound, already loose by `n²`,
becomes `5π`-times-looser when derived via Hurwitz Fourier:
`(R − ρ)² ≤ (5/4) Δ_H ~ 5π⁴/(3n²)`, slack ratio `5π · n² /
(constant)` over actual. The `5π` is a *uniform-overhead amplifier*
on top of the family-specific metric mismatch.

**Where the boundary lies.**

- Phenomenon **A** (metric mismatch on n-gons): describes how
  *bounds expressed in different powers of `Δ`* scale on a specific
  parametric family. The right-hand side `Δ^k` for various `k`
  produces different rates of decay on inscribed regular n-gons; the
  metric mismatch is the gap between the "right" `k` (sharp) and the
  "wrong" `k` (loose).
- Phenomenon **B** (the `5π` overhead): describes how *different
  proofs of the same geometric inequality* produce different
  constants. The form `(r₂ − r₁)² ≤ c · Δ_H/(4π)` admits proofs with
  different `c`; Bonnesen's parallel-curve proof gets `c = 1`,
  Hurwitz Fourier route gets `c = 5π`, Bernstein 1905 gets `c ≈ 1700`.

These compose: A determines the *rate* of decay of the inequality's
slack on a family; B determines the *uniform overhead constant* in
the inequality across all families. They do not refine or complicate
each other — they are orthogonal axes of looseness.

### A.4 What this means for the program

For the K-H-L-A endgame's audit of the Bonnesen route:

- **The sharp constant `c = 1`** is Bonnesen 1924, post-1882, derived
  via convex parallel curves. The Fejes-Tóth 1950 elementary
  polygonal proof (per [iso/OSSERMAN-1979-BRIEF.md](iso/OSSERMAN-1979-BRIEF.md))
  is the candidate L-W-safe re-rendering and would preserve `c = 1`.
- **The Fourier route's `c = 5π`** is also post-1882 (Hurwitz 1902)
  but methodologically distinct. The audit question for Hurwitz: does
  the Fourier identity itself depend on post-1882 transcendence
  input? It does not — Parseval on `S¹` and the area-perimeter
  Fourier expansion are pre-1882 in spirit (Fourier 1822, classical
  trigonometric series machinery). So the `5π` route is plausibly
  L-W-safe in its derivation, just non-sharp in its constant.
- **For program purposes**, when the constant matters
  (e.g., contradiction-step audit calculations), the program should
  prefer the Bonnesen direct route (sharp `c = 1`) over the Hurwitz
  Fourier route (`c = 5π`). The Sobolev / `||∇u||²` form remains
  the natural register for *rate* statements (where Hurwitz is
  sharp and Bonnesen is rate-loose by factor `n`); the `(r₂ − r₁)²`
  form remains the natural register for *constant* statements
  (where Bonnesen is sharp and Hurwitz is constant-loose by `5π`).
  The two routes are not interchangeable, and the program inherits
  the bifurcation.
