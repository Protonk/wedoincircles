# OSSERMAN-1979-BRIEF

Source-extraction memo on Robert Osserman, "Bonnesen-Style Isoperimetric
Inequalities," *American Mathematical Monthly* 86, no. 1 (Jan. 1979),
pp. 1–29
([sources/Osserman-BonnesenStyleIsoperimetricInequalities-1979.pdf](sources/Osserman-BonnesenStyleIsoperimetricInequalities-1979.pdf)).
JSTOR stable URL 2320297.

**Why this brief exists.** Foundational survey for
[iso/DIDOS-PREROGATIVE.md](iso/DIDOS-PREROGATIVE.md), which plays
the coordination role for isoperimetry that
[fft/FFT-CYCLOTOMIC-COMPLEXITY.md](fft/FFT-CYCLOTOMIC-COMPLEXITY.md)
plays for FFT-complexity. The paper's value to the program is two-fold:
(i) Part II is an explicit per-result historiography of Bonnesen-style
strengthenings, suitable for an INHERIT-discipline audit; (ii) Part I
is a proof-tour of the geometric route to `L² − 4πA ≥ π²(R − ρ)²` and
its eight cousins, against which the Hurwitz/Parseval route used in
[corners/HURWITZ-GAP.md](corners/HURWITZ-GAP.md) can be compared.

**What was read.** All 30 pages: §I (plane domains and surface domains),
§II (history), §III (amplifications, eigenvalue applications, higher
dimensions), and the reference list [1]–[77]. Read with two lenses:
*per-inequality original prover and technique*, and *what the paper's
tools say (or do not say) about the inscribed regular n-gon's
isoperimetric gap.*

**Confidence level.** High on the paper's internal mathematical content
— the inequalities and their proofs are stated and worked through.
High on the historical attributions for plane convex curves
(Bonnesen 1921 [19], Bonnesen 1924 [20], Bernstein 1905 [15], Liebmann
1919 [54], Hadwiger 1941 [41]/[42], Fiala 1941 [40], Fejes-Tóth 1950
[39]). Medium on the surface-domain history (Carleman 1921, Schmidt
1939/1940, Bol 1941, Aleksandroff/Stre'l'tsov, Burago/Zalgaller, Ionin
1969); the surface chain is more fragmented and Osserman flags the
"strange history" himself (p. 13).

**Trust boundary up front.** This brief audits *what the paper says*
about Bonnesen-style isoperimetric inequalities. It does not attempt
to specialize Osserman's tools to the program's `K_n` ladder or to the
`x_{n,k}` corner-incidence material; those steps live elsewhere. The
brief flags one corrigendum on a date the user supplied — see §1.

---

## 1. Per-Inequality Historiography

### 1.1 The headline inequality is from 1921, not 1924

The user's prompt named "the headline `Δ ≥ π(R − r)²` inequality
(Bonnesen 1924)." The paper's actual statements (with `Δ = L² − 4πA`,
`R` circumradius, `ρ` inradius — Osserman uses `ρ` for the inradius,
not `r`):

- **Eq. (21):** `Δ ≥ π² (R − ρ)²`. Constant is `π²`, not `π`. Proved
  by **Bonnesen 1921** in [19] *Über eine Verschärfung der
  isoperimetrischen Ungleichheit des Kreises in der Ebene und auf der
  Kugeloberfläche*, Math. Ann. 84 (1921) 216–227. Derived from
  inequalities (14) and (19), both also in the same 1921 paper.
- **Eq. (33):** `Δ ≥ 4π · d²`, where `d` is the minimum width of a
  circular annulus containing `C`. Constant is `4π`. Proved by
  **Bonnesen 1924** in [20] *Über das isoperimetrische Defizit ebener
  Figuren*, Math. Ann. 91 (1924) 252–268. Osserman notes (p. 14):
  "still later, in 1924, he obtained the constant `4π`, which he
  showed by an example was the best possible."

So the headline `(R − ρ)²` form with constant `π²` is **Bonnesen
1921**, and the headline `d²` form with constant `4π` (best possible)
is **Bonnesen 1924**. These are distinct inequalities by the same
author three years apart.

### 1.2 The very first Bonnesen-style inequality — Bernstein 1905

Osserman's verdict on the chronology (p. 13, opening of Part II):

> "It is peculiarly appropriate to the strange history of the circle
> of ideas discussed here, that the first Bonnesen-style inequality
> should have been proved not by Bonnesen, but by F. Bernstein in
> 1905, and that, furthermore, Bernstein started by considering curves
> on the sphere, and then obtained a 'Bonnesen inequality' for plane
> curves as a limiting case."

**F. Bernstein 1905** [15], *Über die isoperimetrische Eigenschaft des
Kreises auf der Kugeloberfläche und in der Ebene*, Math. Ann. 60
(1905) 117–136. Inequality of the form (66): `L² − 4πA + MA² ≥ B`,
where `M = α² = 1/t²` is the constant curvature of a sphere of radius
`t`, and `B = (2t · g(t))²(2π + g(t)²)` with `g(t) = sin(d/(4(1+2πt)))`,
`d` = width of narrowest spherical annulus containing the curve.
Letting `t → ∞` gives the plane consequence (68):
`L² − 4πA ≥ (π / (2(1 + 2π)²)) · d²` — strictly weaker constant than
Bonnesen's later `4π`. Bernstein's technique: analytic, on the sphere,
limiting argument to plane.

### 1.3 Per-inequality table

The paper lists nine Bonnesen-type plane inequalities in Theorems 2–4,
plus the original (33) of Bonnesen 1924. Original prover and technique
per Osserman's Part II:

| Ineq | Form | Original prover (Osserman's attribution) | Technique |
|------|------|------------------------------------------|-----------|
| (11) | `Δ ≥ (L − 2πρ)²` | **Bonnesen 1926** [21] (first explicit "Bonnesen form"); Fiala 1941 [40] for non-convex | Convex parallel-curve; Fiala interior parallels for non-convex |
| (12) | `Δ ≥ (A − πρ²)² / ρ²` | **Hadwiger 1941** [42] for convex | Integral geometry |
| (13) | `Δ ≥ (L − 2A/ρ)²` | **Hadwiger 1941** [42] for convex | Integral geometry |
| (14) | `ρL ≥ A + πρ²` | **Liebmann 1919** [54] for convex; equivalent in Chisini [36]; also Bonnesen 1921 [19]. **Used by Bonnesen with (19) to derive (21).** Non-convex: Fiala 1941 [40] (analytic Jordan); Besicovitch 1949 [16] (arbitrary Jordan, equality characterization); Fejes-Tóth 1950 [39] (polygonal direct, no integral geometry needed) | Liebmann: convex geometry |
| (16) | `Δ ≥ (2πR − L)²` | **Liebmann 1919** [54] for convex; also Bonnesen 1921 [19] | Convex geometry |
| (17) | `Δ ≥ (πR² − A)² / R²` | **Hadwiger 1941** [42] for convex | Integral geometry |
| (18) | `Δ ≥ (L − 2A/R)²` | **Hadwiger 1941** [42] for convex | Integral geometry |
| (19) | `RL ≥ A + πR²` | **Bonnesen 1921** [19], paired with (14) to yield (21) | Convex parallel-curve |
| (21) | `Δ ≥ π²(R − ρ)²` | **Bonnesen 1921** [19]; the geometric headline | Derived from (14) + (19) |
| (22) | `Δ ≥ (A²/(R²ρ²))(R − ρ)²` | **Hadwiger 1941** [42] | Integral geometry |
| (23) | `Δ ≥ (L²/(R + ρ)²)(R − ρ)²` | **Hadwiger 1941** [42] | Integral geometry |
| (33) | `Δ ≥ 4π · d²`, `d` = min annulus width, constant 4π best possible | **Bonnesen 1924** [20] | Convex parallel-curve, sharpened |

**Non-convex extension** (Osserman p. 14): "All of these results were
for convex curves only, and the extension to non-convex curves
required essentially new methods." Three independent routes:

- **Erhard Schmidt 1939** [68]: analytic methods for non-convex
  rectifiable Jordan curves. Does not obtain Theorems 1 and 2.
- **Fiala 1941** [40]: interior parallels method. Analytic Jordan
  curves; first to give (11) and (14) explicitly for non-convex.
- **Hadwiger 1941** [41]: integral geometry; gets results "essentially
  equivalent to inequalities (15) and (20) for arbitrary rectifiable
  Jordan curves." Notices Bonnesen connection only in later [42].

**Polygonal direct route** (Fejes-Tóth 1950 [39]): "we owe the
observation that by working with polygons one can drop the machinery
of integral geometry and give direct elementary proofs of the formulas
needed to prove Bonnesen's inequalities."

### 1.4 Osserman's own proof of the headline (21)

Osserman's Part I §I.A proof structure (pp. 4–6):

1. **Theorem 4 from Theorems 2 and 3 (purely algebraic).** Subtract
   (15) from (20) to get (21). From (13) and (18):
   `√Δ ≥ (2/ρ)A − L`, `√Δ ≥ L − (2/R)A`. Adding gives (22). Multiply
   the first by `ρ`, the second by `R`, add — yields (23). So (21)–(23)
   are *immediate consequences* of Theorems 2 and 3.

2. **Theorems 2 and 3 via Fejes-Tóth's polygonal method.** For a
   convex polygon `C`, the *exterior parallel curve* `C_t` at distance
   `t` has length `L(t) = L + 2πt` (eq. 25) and the parallel domain
   `D_t` has area `A(t) = A + Lt + πt²` (eq. 26). Critical observation:
   for `t ∈ (ρ, R)`, every circle of radius `t` whose center lies in
   `D_t` must intersect `C` — by the definitions of `ρ` and `R` such
   a circle cannot lie inside `D` nor surround it, and by the
   definition of `D_t` cannot lie totally outside `C`.

3. **Polygonal length-area identity** (eq. 27): for an arbitrary
   polygon `P`, `Σ k · A_k = 4tL` where `A_k` is the area of the set
   of points whose distance-`t` circles intersect `P` in exactly `k`
   points. Proved by induction on the number of sides; base case is a
   single segment of length `s`, giving a region consisting of an
   `s × 2t` rectangle plus two semicircular caps. For *closed*
   polygons every circle intersects in an even number of points, so
   `2A ≤ 4tL` (eq. 28).

4. **Combining (26) with (28)** gives `2tL ≥ A(t) = A + Lt + πt²` for
   `ρ < t < R` (eq. 29). Letting `t → ρ` and `t → R` recovers (14) and
   (19).

5. **Convex hull argument** extends (19) from arbitrary to convex
   polygon. **Approximation argument** (Lemma 3) extends to rectifiable
   Jordan curves: any such curve admits a sequence of Jordan polygons
   `P_n` with `L_n → L`, `A_n → A`, `R_n → R`.

6. **For (14) on non-convex polygons** Osserman uses an alternative
   method (his Lemma 4): for `0 < r < ρ`, let `D_r = {p ∈ D :
   d(p, C) > r}` and `C_r = ∂D_r`. Then `L(r) ≤ L − 2πr` (eq. 31) and
   `A = ∫₀^ρ L(r) dr` (eq. 32), and (31) inserted into (32) yields
   (14) for Jordan polygons. The proof of (31) requires elaboration
   for non-convex curves (Osserman defers to Part II §A's discussion
   of Bol 1941, Sz.-Nagy, Hartman 1964).

**Summary technique.** Fejes-Tóth's polygonal exterior-parallel-curve
argument plus convex hull plus rectifiable approximation. *Not*
Steiner symmetrization, *not* support functions, *not* Fourier
coefficients, *not* integral geometry (in Osserman's main text, though
integral geometry is the technique of Hadwiger and Santaló in the
historical chain). The non-convex case in Lemma 4 borrows interior
parallels from Fiala 1941, sharpened via Sz.-Nagy and Hartman.

### 1.5 Where Osserman's proof differs from the originals

- **Bonnesen 1921's original derivation** of (21): Bonnesen used (14)
  and (19) directly, both proved for convex curves. Osserman's chain
  is the same algebraically but routes (14) and (19) through
  Fejes-Tóth's polygonal lemma (eq. 27) rather than Bonnesen's own
  convex parallel-curve argument. *Algebraic conclusion identical;
  geometric substrate different.*
- **Hadwiger 1941's** proofs of (12), (13), (17), (18), (22), (23) use
  *integral geometry* (Crofton-style formulas, Blaschke's framework).
  Osserman derives these as algebraic corollaries of (14), (19), (15),
  (20), avoiding integral geometry entirely. The Hadwiger-via-Osserman
  proofs are strictly elementary in a way Hadwiger's originals are
  not.
- **Bonnesen 1924's (33)** with optimal `4π` constant: Osserman states
  it (eq. 33) but defers detailed proof to Part II, where he
  attributes the technique to convex parallel curves with sharpening.
  Osserman does not reproduce the optimality argument (Bonnesen's
  example showing `4π` is best possible).

---

## 2. Specialization to Regular n-Gons and the Hurwitz Fourier Route

### 2.1 Does Osserman directly state a regular-n-gon bound?

**No.** The paper does not specialize any of (11)–(23), (33) to
regular polygons; it does not mention `n`-gons except as approximating
sequences in Lemma 3. The inequalities all hold for the inscribed
regular `n`-gon (which is a rectifiable Jordan curve, in fact a
convex one), but Osserman does not write the specialization.

### 2.2 What the survey's tools supply when specialized

For the inscribed regular `n`-gon (program convention,
[corners/HURWITZ-GAP.md](corners/HURWITZ-GAP.md)): circumradius `R = 1`,
inradius `ρ = cos(π/n)`, side length `s = 2 sin(π/n)`, perimeter
`L_n = 2n sin(π/n)`, area `A_n = (n/2) sin(2π/n)`.

The geometric gap `R − ρ = 1 − cos(π/n) = 2 sin²(π/(2n))`. Taylor
expanding at large `n`:

```
R − ρ = 2 sin²(π/(2n)) = 2 · (π/(2n))² + O(1/n⁴) = π²/(2n²) + O(1/n⁴).
```

Substituting into (21) `Δ ≥ π²(R − ρ)²`:

```
Δ_n ≥ π² · (π²/(2n²) + O(1/n⁴))² = π² · π⁴/(4n⁴) + O(1/n⁶) = π⁶/(4n⁴) + O(1/n⁶).
```

So Osserman's inequality (21), specialized to the inscribed regular
`n`-gon, gives **`Δ_n ≥ π⁶/(4n⁴) + O(1/n⁶)` — an `O(1/n⁴)` lower
bound.**

The actual leading term, computed three ways in
[corners/HURWITZ-GAP.md](corners/HURWITZ-GAP.md) and confirmed
numerically against the elementary closed form, is

```
Δ_n = 4π⁴/(3n²) + O(1/n⁴).
```

That is **`O(1/n²)` — a strictly faster vanishing rate than what
Bonnesen's R-ρ inequality detects.** Bonnesen's lower bound is two
orders of magnitude in `n` weaker than the actual rate.

The same conclusion holds for (33) `Δ ≥ 4π · d²` with `d` the minimum
annulus width: for the inscribed regular `n`-gon `d = R − ρ = O(1/n²)`,
so `4π·d² = O(1/n⁴)` — same `n⁴` floor.

For (11) `Δ ≥ (L − 2πρ)²`: `L_n − 2πρ_n = 2n sin(π/n) − 2π cos(π/n)`.
Taylor-expanding,
`= 2n(π/n − π³/(6n³) + ...) − 2π(1 − π²/(2n²) + ...)`
`= 2π − π³/(3n²) − 2π + π³/n² + O(1/n⁴)`
`= 2π³/(3n²) + O(1/n⁴)`.
So `(L − 2πρ)² = 4π⁶/(9n⁴) + O(1/n⁶)`, again `O(1/n⁴)`.

**All Bonnesen-style inequalities in the survey are `O(1/n⁴)` when
specialized to the inscribed regular `n`-gon.** None recovers the
Hurwitz/Parseval `O(1/n²)` leading rate.

This is a real finding for the program. The geometric Bonnesen route
*qualitatively underestimates* the isoperimetric gap for nearly-circular
inscribed regular polygons. It says the gap is at least `O(1/n⁴)` when
in fact it is `Θ(1/n²)`.

### 2.3 Independence from the Hurwitz Parseval route

**Hurwitz** is **not in Osserman's reference list** [1]–[77]. The
Hurwitz 1902 identity
`Δ = 4π² Σ m(m − 1) |c_m|²`
(with `c_m` the Fourier coefficients of an arclength-parametrized
curve) does not appear in this paper, and no Fourier or Parseval
methods are used at any point in §I, §II, or §III. The closest the
paper comes to spectral content is §III.B (eigenvalue applications,
Cheeger's inequality `λ₁(D) ≥ h²/4`), and that is *downstream* of
Bonnesen-style inequalities, not parallel to them.

So the two routes are **methodologically independent**: Osserman's
geometric/parallel-curve/integral-geometric route on one side, the
Hurwitz/Parseval/Fourier-coefficient route on the other. Neither
reduces to the other in the paper.

The structural relationship between them, inferred for the program
(not in Osserman):

- **Hurwitz route gives an *equality*.** `Δ = 4π² Σ m(m − 1) |c_m|²`
  is a Parseval identity, exact, valid for any rectifiable closed
  curve in arclength parametrization. Lower bounds come from selecting
  individual coefficients to lower-bound the sum.
- **Bonnesen route gives *inequalities*** in terms of geometric
  invariants `R`, `ρ`, `d`, `A`, `L`. The inequalities are sharp only
  at the disk; for any non-circular curve they are strict but the slack
  is not generally sharp.
- **They produce different rates on the regular-n-gon test case.**
  Hurwitz gets `O(1/n²)` exactly via the Fourier-support computation
  in [corners/HURWITZ-GAP.md](corners/HURWITZ-GAP.md) (`c_m = 0` unless
  `m ≡ 1 (mod n)`, with `|c_m|² = L_n² /(4π²m²)` for `m = 1 + jn`).
  Bonnesen, specialized via `R − ρ`, gets `O(1/n⁴)` — correct but loose
  by two orders of `n`.
- **The routes are not interconvertible.** Bonnesen's inequalities
  cannot recover the Fourier-support sparsity that drives the
  Hurwitz `O(1/n²)` rate: the `R − ρ` quantity is a single geometric
  scalar, while the Hurwitz rate emerges from the *shape* of the
  Fourier support `m ≡ 1 (mod n)`. Conversely, the Hurwitz Parseval
  identity does not encode any direct dependence on `R` or `ρ`; one
  can write a curve's Fourier coefficients without ever computing
  these radii. The two routes are reading different invariants of the
  same curve.

### 2.4 Survey's organization — complementary, alternative, or interconvertible?

Osserman's survey organization treats Bonnesen-style as a *single
geometric program*: nine inequalities in §I.A, all derivable from
parallel-curve/polygonal arguments, with integral-geometric and
analytic alternatives in Part II. The Hurwitz/Parseval route is *not
a member* of this program in Osserman's organization — it is absent
from the references and the text. So at the level of *Osserman's
framing*, the Bonnesen and Hurwitz routes are not in the same
conversation.

For the program, the operational reading: **complementary, not
alternative or interconvertible.** Bonnesen for general convex/Jordan
curves where Fourier coefficients are not easily available; Hurwitz
for arclength-parametrized curves where Fourier is the natural
register. The regular `n`-gon is in *both* domains — it is a
rectifiable convex Jordan curve (Bonnesen domain) and admits a clean
arclength-Fourier expansion (Hurwitz domain) — and on this overlap the
two routes give different rates with the Fourier route winning. That
asymmetry is a real fact about the geometric route's coarseness on
nearly-circular polygons.

---

## 3. Trust Boundary

### This brief should be cited for

- The headline geometric Bonnesen inequality `Δ ≥ π²(R − ρ)²` is
  Osserman's eq. (21), proved by **Bonnesen 1921** [19], constant
  `π²` (not `π`).
- The minimum-annulus-width form `Δ ≥ 4π · d²` is Osserman's eq. (33),
  proved by **Bonnesen 1924** [20], constant `4π` provably best
  possible.
- The very first Bonnesen-style inequality is **Bernstein 1905** [15],
  obtained on the sphere with a plane consequence of strictly weaker
  constant.
- The per-inequality attribution table in §1.3 above.
- Osserman's own proof technique: Fejes-Tóth polygonal exterior
  parallel curves + convex hull + rectifiable approximation, with
  Lemma 4's interior-parallels variant for non-convex polygons. *Not*
  Steiner symmetrization, support functions, or Fourier methods.
- The non-convex extension chain: Schmidt 1939 (analytic), Fiala 1941
  (interior parallels), Hadwiger 1941 (integral geometry), Besicovitch
  1949, Fejes-Tóth 1950 (polygonal direct).
- The fact that all Bonnesen-style inequalities in the survey,
  specialized to the inscribed regular `n`-gon, give `O(1/n⁴)` lower
  bounds — strictly weaker than the Hurwitz/Parseval `O(1/n²)`
  leading rate.
- Hurwitz 1902 is **not in the paper's reference list [1]–[77]**;
  Fourier/Parseval methods are not used.

### This brief should NOT be cited for

- Specialization of Osserman's tools to `K_n`, `Q(ζ_n)`, or any
  cyclotomic content (not in the paper).
- Algebraic-degree / closure-mismatch material (not in the paper).
- Sharper-than-`O((R − ρ)²)` Bonnesen-type bounds on `Δ_n` (the
  paper's geometric route bottoms out at this scale).
- The Hurwitz 1902 identity or its Parseval form (absent from the
  paper).
- Any claim of inter-derivability between Bonnesen and Hurwitz routes
  (the paper does not address this).
- Surface-domain history beyond the chronological skeleton; Osserman
  himself flags this part of the literature as fragmented.

### Provenance tag for the program

**Methodologically post-1965 historiography of post-1882 origin
work.** The substantive results in the paper are *not* pre-Lindemann–
Weierstrass: the earliest Bonnesen-style inequality the paper
attributes is **Bernstein 1905**, twenty-three years after L–W; the
headline (21) is **Bonnesen 1921**, thirty-nine years after L–W. The
classical isoperimetric inequality `L² ≥ 4πA` itself has pre-L-W
proofs (Steiner symmetrization, ~1830s), but **all quantitative
Bonnesen-style strengthenings in this paper are post-1882.** This is
a clarification to
[iso/DIDOS-PREROGATIVE.md](iso/DIDOS-PREROGATIVE.md), which
provisionally read "Bonnesen-1924-and-earlier" as clean substrate; the
"and-earlier" qualifier should now be read as referring to the
*qualitative* statement only (Zenodorus, Steiner), not to the
quantitative `(R − ρ)²` strengthening, which is post-L-W by four
decades. For the K-H-L-A endgame
([memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md](memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md)),
each Bonnesen technique used in a contradiction step requires its own
L-W-safety audit per
[memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md): does the
proof depend on post-1882 transcendence input, or is it methodologically
reconstructible pre-L-W? The Fejes-Tóth 1950 polygonal proof in
Osserman's main text appears to use only elementary geometry of
parallel curves and induction — a candidate for L-W-safety
certification — but the certification itself is not in this paper.

---

## Closing Sentence

This brief contributes the per-result historiography of Bonnesen-style
isoperimetric inequalities — Bernstein 1905 (first, on sphere with
plane consequence), Liebmann 1919 (precursor (14), (16)), Bonnesen
1921 (headline `Δ ≥ π²(R − ρ)²`), Bonnesen 1924 (`Δ ≥ 4π · d²` with
`4π` best possible), Hadwiger 1941 (integral-geometric corollaries),
Schmidt 1939 / Fiala 1941 / Hadwiger 1941 (non-convex extensions),
Fejes-Tóth 1950 (polygonal direct method) — together with the
technique inventory (parallel curves, integral geometry, analytic
methods, polygonal direct) and Osserman's own elementary-Fejes-Tóth
proof of the headline. It records the structural finding that all
Bonnesen-style inequalities in the survey, specialized to the
inscribed regular `n`-gon, give `O(1/n⁴)` lower bounds on `Δ_n` —
*qualitatively weaker* than the Hurwitz/Parseval `O(1/n²)` leading
rate computed in [corners/HURWITZ-GAP.md](corners/HURWITZ-GAP.md). The
two routes are methodologically independent (Hurwitz absent from
Osserman's references), and the paper's organization treats Bonnesen
as a self-contained geometric program rather than as an alternative
to Fourier methods. The program's working stance: complementary, not
interconvertible. This brief is the foundational survey extraction
for [iso/DIDOS-PREROGATIVE.md](iso/DIDOS-PREROGATIVE.md).
