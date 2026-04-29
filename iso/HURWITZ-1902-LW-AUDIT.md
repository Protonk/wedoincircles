# HURWITZ-1902-LW-AUDIT

L-W-safety audit on the Hurwitz 1902 Parseval derivation of the
isoperimetric gap

```text
Δ = L² − 4π A = 4π² Σ_{m ∈ ℤ} m(m − 1) |c_m|²,
```

invoked across the program at
[corners/HURWITZ-GAP.md](corners/HURWITZ-GAP.md),
[corners/HURWITZ-FIRST-BAND-CONCENTRATION.md](corners/HURWITZ-FIRST-BAND-CONCENTRATION.md),
[memos/STRIP-H1-HURWITZ-CLOSURE.md](memos/STRIP-H1-HURWITZ-CLOSURE.md),
[memos/ARCHIMEDEAN-SIGNATURE.md](memos/ARCHIMEDEAN-SIGNATURE.md),
and named at
[iso/THREE-REGISTER-SYNTHESIS.md](iso/THREE-REGISTER-SYNTHESIS.md)
§2.4 as the outstanding L-W-safety audit task for the **Sobolev
register**.

This is an anchor-mode audit per
[memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md) §"Audit
criterion: content, not calendar." It does not produce a new
isoperimetric theorem; it certifies that Hurwitz's 1902 derivation of
the Parseval-form gap identity uses only transcendence-free (pre-1882
in content) tools. The audit format follows
[rotations/BETA-PI-LW-AUDIT.md](rotations/BETA-PI-LW-AUDIT.md)
(today's β(π) = 0 audit on the rotation-orbit Diophantine register).

Hurwitz 1902 is calendar-post-1882 by 20 years (Hurwitz, A., "Sur
quelques applications géométriques des séries de Fourier," *Annales
scientifiques de l'École Normale Supérieure* 19 (1902), pp. 357–408),
so the audit sits in the content-not-calendar regime: the question is
whether the *proof* uses transcendence-theoretic input, not whether
the *paper* postdates Lindemann 1882.

The Sobolev register's certification is the audit's deliverable.
[iso/THREE-REGISTER-SYNTHESIS.md](iso/THREE-REGISTER-SYNTHESIS.md)
§2.4 lists three outstanding audit targets across the three iso/
registers (Fejes-Tóth 1950 / Hurwitz 1902 / Schmidt 1960); this audit
closes the Hurwitz item. The other two remain open and are tracked
separately.

## Audit target

The identity Hurwitz 1902 derives, in modern statement: for a smooth
closed plane curve `γ : [0, L] → ℂ` parametrized by arc length, with
complex Fourier expansion

```text
γ(s) = Σ_{m ∈ ℤ} c_m e^{2π i m s / L},   s ∈ [0, L],
```

the isoperimetric gap admits the closed Parseval form

```text
Δ = L² − 4π A = 4π² Σ_{m ∈ ℤ} m(m − 1) |c_m|²,
```

with `Δ ≥ 0` because every term in the sum has `m(m − 1) ≥ 0`, and
equality `Δ = 0` iff `c_m = 0` for every `m ∉ {0, 1}` — equivalently,
the curve is a circle.

This is the identity used at
[corners/HURWITZ-GAP.md](corners/HURWITZ-GAP.md) (closure check on
inscribed regular `n`-gons),
[corners/HURWITZ-FIRST-BAND-CONCENTRATION.md](corners/HURWITZ-FIRST-BAND-CONCENTRATION.md)
(first-band concentration `B_1(n) ≥ (6/π²) Δ_n`), today's Archimedean
squeeze and first-band excess work, and the Sobolev-register column
of [iso/THREE-REGISTER-SYNTHESIS.md](iso/THREE-REGISTER-SYNTHESIS.md)
§"Currency-by-route map".

The audit asks: does the proof above depend on Lindemann-Weierstrass,
Baker, Gelfond-Schneider, Thue-Siegel-Roth, or any transcendence-
theoretic content?

## Reconstruction with provenance tags

The proof is short. Each step terminates at a pre-1882 primitive,
which we tag inline.

**Step 1. Fourier expansion of `γ`.** Smooth periodic functions on
`[0, L]` admit `L²`-convergent Fourier expansions in the basis
`{e^{2π i m s / L}}_{m ∈ ℤ}`. The expansion is

```text
γ(s) = Σ_{m ∈ ℤ} c_m e^{2π i m s / L},
c_m = (1/L) ∫₀^L γ(s) e^{−2π i m s / L} ds.
```

*Provenance:* **Fourier 1822** (*Théorie analytique de la chaleur*).
The orthogonality of the trigonometric system on `[0, L]` is the
identity

```text
(1/L) ∫₀^L e^{2π i (m − n) s / L} ds = δ_{m, n},
```

a direct integral evaluation. Pre-1882 in calendar and content; no
transcendence input.

**Step 2. Term-by-term differentiation.** For sufficiently smooth `γ`
(C¹ suffices for the formal manipulation; classical regularity is
implicit in Hurwitz's setting), differentiation commutes with the
Fourier sum:

```text
γ'(s) = Σ_{m ∈ ℤ} (2π i m / L) c_m e^{2π i m s / L}.
```

*Provenance:* classical Fourier-series differentiation; the validity
follows from convergence of `Σ |m c_m|` (Weierstrass M-test) for
smooth curves. **Weierstrass 1872** for the M-test in published form;
the underlying technique (uniform-convergence argument) is in
**Cauchy 1821** (*Cours d'analyse*). Pre-1882 in content, no
transcendence input.

**Step 3. Perimeter via Parseval.** Arc-length parametrization gives
`|γ'(s)| = 1` at every `s`, so

```text
L = ∫₀^L 1 · ds = ∫₀^L |γ'(s)|² ds.
```

Expand `|γ'(s)|² = γ'(s) · γ'(s)*` using Step 2 and integrate term by
term:

```text
∫₀^L |γ'|² ds = Σ_{m, n} (2π i m / L)(−2π i n / L) c_m c_n* ∫₀^L e^{2π i (m − n) s / L} ds
              = Σ_{m, n} (4π² m n / L²) c_m c_n* · L · δ_{m, n}
              = (4π² / L) Σ_{m ∈ ℤ} m² |c_m|².
```

Setting this equal to `L`:

```text
L² = 4π² Σ_{m ∈ ℤ} m² |c_m|².                                  (★)
```

*Provenance:* **Parseval 1799** in original trigonometric-series form;
the modern statement follows from Step 1's orthogonality and the
elementary integral computation above. Pre-1882 in content; no
transcendence input. The constant π appears *symbolically* in the
identity — as the ratio of circumference to diameter, an elementary
Euclidean datum — not as an analytic transcendence claim.

**Step 4. Area via Green's theorem.** For a positively-oriented
simple closed plane curve `γ`, the enclosed area is

```text
A = (1/2) ∫₀^L Im(γ(s)* γ'(s)) ds = (1/2) ∮ (x dy − y dx).
```

*Provenance:* **Green 1828** (*An Essay on the Application of
Mathematical Analysis to the Theories of Electricity and Magnetism*);
the planar form is also implicit in **Cauchy 1825** (Cauchy integral
theorem and its real specialization). Pre-1882 in content; no
transcendence input. (For non-simple curves the Parseval form
generalizes to signed area; Hurwitz's original argument and modern
expositions both treat the simple-curve case.)

**Step 5. Area via Parseval.** Substituting the Fourier expansions of
`γ` and `γ'` and using orthogonality:

```text
γ(s)* γ'(s) = Σ_{m, n} c_m* c_n (2π i n / L) e^{2π i (n − m) s / L},
∫₀^L γ* γ' ds = Σ_{m, n} c_m* c_n (2π i n / L) · L · δ_{m, n}
              = 2π i Σ_{m ∈ ℤ} m |c_m|².
```

Taking the imaginary part: since `Σ m |c_m|²` is real,
`Im(2π i · real) = 2π · real`, so

```text
A = (1/2) · 2π · Σ_{m ∈ ℤ} m |c_m|² = π Σ_{m ∈ ℤ} m |c_m|².      (★★)
```

*Provenance:* combination of Steps 1, 2, 4. Algebraic manipulation of
complex numbers (Cauchy / Argand 1806 / Gauss; pre-1882 in content);
no transcendence input.

**Step 6. The Hurwitz identity.** Multiply `(★★)` by `4π` and subtract
from `(★)`:

```text
L² − 4π A = 4π² Σ_{m ∈ ℤ} m² |c_m|² − 4π · π Σ_{m ∈ ℤ} m |c_m|²
          = 4π² Σ_{m ∈ ℤ} (m² − m) |c_m|²
          = 4π² Σ_{m ∈ ℤ} m(m − 1) |c_m|².
```

*Provenance:* algebra. Pre-1882 in content; no transcendence input.

**Step 7. The inequality and the equality case.** For every integer
`m`, `m(m − 1) ≥ 0` (trivially: the polynomial `t(t − 1)` is
non-negative on integers, since one of `m`, `m − 1` is non-negative
and the other non-positive only when `m ∈ {0, 1}`, where the product
is zero). The terms `m = 0` and `m = 1` contribute zero; every other
term is non-negative. Hence

```text
Δ = L² − 4π A ≥ 0,
```

with equality iff `c_m = 0` for every `m ∉ {0, 1}`. The remaining
two-term Fourier expansion `γ(s) = c_0 + c_1 e^{2π i s / L}`
parametrizes a circle of radius `|c_1| = L/(2π)` centered at `c_0`.

*Provenance:* integer arithmetic and direct verification on the
two-term case. Pre-1882 in content (and in calendar); no
transcendence input.

## L-W-safety analysis

The full proof chain is:

```text
Fourier 1822 (series expansion)
+ Parseval 1799 (orthogonality / norm identity)
+ Cauchy 1821 / Weierstrass 1872 (uniform-convergence machinery)
+ Green 1828 (planar area as boundary integral)
+ Cauchy / Argand 1806 / Gauss (complex-number algebra)
+ elementary integer arithmetic (`m(m − 1) ≥ 0`)
⟹ Δ = 4π² Σ m(m − 1) |c_m|², with `Δ ≥ 0`, equality iff circle.
```

What is **not** used:

- **Lindemann 1882 / Weierstrass 1885** (transcendence of `π` and of
  `e^α` for algebraic `α ≠ 0`). The constant `π` enters the identity
  symbolically as the ratio of circumference to diameter. The
  identity makes no claim about `π`'s algebraic-versus-transcendental
  status; it is a Hilbert-space norm equality on `L²([0, L])`.
- **Baker 1966** (linear forms in logarithms of algebraic numbers).
  No logarithmic content beyond the symbolic `π`.
- **Gelfond-Schneider 1934** (transcendence of `α^β` for algebraic
  `α ∉ {0, 1}` and irrational algebraic `β`). No exponential content
  beyond the symbolic `e^{2π i m s / L}` Fourier basis.
- **Thue-Siegel-Roth 1955** (rational approximations to algebraic
  numbers). No Diophantine content; the identity is non-arithmetic.
- **Schmidt subspace theorem, Nesterenko algebraic-independence
  results, Mahler's transcendence machinery.** None applies; the
  proof is finite-dimensional Hilbert-space arithmetic plus elementary
  plane geometry.

The constant `π` appears in `(★)`, `(★★)`, and the final identity
purely as an Archimedean datum — the ratio of a circle's
circumference to its diameter. This is a pre-1882 Euclidean fact
(implicit in Archimedes, *Measurement of a Circle*, c. 250 BCE; made
explicit as the universal ratio by **Lambert 1761** for irrationality
and **Euler / Newton** for the analytic series). The identity does
*not* claim `π` is transcendental; it claims a relationship among the
geometric quantities `L²`, `A`, and the Fourier coefficients of `γ`
in which `π` appears as a normalization constant from Green's
theorem.

The crucial discipline distinction (per
[memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md) §"Audit
criterion: content, not calendar"): Hurwitz 1902 is calendar-post-1882
by 20 years, but every step in the proof terminates at a pre-1882
primitive whose content is transcendence-free. Calendar dating is not
the audit criterion; content dating is. By the content criterion,
Hurwitz 1902's Parseval derivation is L-W-safe.

## Cross-reference: Fuglede 1989's footnote 1

[iso/FUGLEDE-1989-BRIEF.md](iso/FUGLEDE-1989-BRIEF.md) §1.5 records
that **Fuglede's footnote 1** (page 619) explicitly traces the
`n_dim = 2` Sobolev stability result back to Hurwitz 1902:

> "Still another proof — quite short — can be read off from Hurwitz'
> Fourier series proof of the isoperimetric inequality in the plane
> [8]"

(Fuglede ref [8] = Hurwitz 1902.) This is the program-side
methodological lineage: Fuglede 1989 → Fuglede 1986 → Hurwitz 1902,
with the planar Sobolev stability content present already in
Hurwitz's Parseval form. The audit above certifies that the Hurwitz
content used by this lineage is L-W-safe.

For the program's strip-`H¹` / circumscribed-Hurwitz cross-row
theorem at
[memos/STRIP-H1-HURWITZ-CLOSURE.md](memos/STRIP-H1-HURWITZ-CLOSURE.md)
and
[memos/ARCHIMEDEAN-SIGNATURE.md](memos/ARCHIMEDEAN-SIGNATURE.md)
§"Cross-Row Theorem" — both of which use the Hurwitz Parseval
identity as their underlying content — the L-W-safety provenance now
inherits via this audit.

## Verdict

**(a) Clean.** Hurwitz 1902's Parseval derivation of the
isoperimetric-gap identity `Δ = 4π² Σ m(m − 1) |c_m|²` is L-W-safe
in content under
[memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md)'s
content-not-calendar discipline. The proof terminates at:

- **Fourier 1822** (series expansion);
- **Parseval 1799** (orthogonality / norm identity);
- **Green 1828** (planar area via boundary integral);
- **Cauchy 1821 / Weierstrass 1872** (convergence machinery);
- **Cauchy / Argand 1806 / Gauss** (complex-number algebra);
- **Archimedes / Euclid** (`π` as the Archimedean diameter-to-
  circumference ratio);
- elementary integer arithmetic.

All pre-1882 in content; no transcendence-theoretic input. The
constant `π` enters the identity only as a Euclidean normalization
constant from the area integral, not as an algebraic-versus-
transcendental claim.

The Sobolev register's L-W-safety status promotes from "outstanding
audit target" (per
[iso/THREE-REGISTER-SYNTHESIS.md](iso/THREE-REGISTER-SYNTHESIS.md)
§2.4) to **discharged**. The Hurwitz Parseval content used at
[corners/HURWITZ-GAP.md](corners/HURWITZ-GAP.md),
[corners/HURWITZ-FIRST-BAND-CONCENTRATION.md](corners/HURWITZ-FIRST-BAND-CONCENTRATION.md),
[memos/STRIP-H1-HURWITZ-CLOSURE.md](memos/STRIP-H1-HURWITZ-CLOSURE.md),
[memos/ARCHIMEDEAN-SIGNATURE.md](memos/ARCHIMEDEAN-SIGNATURE.md),
and today's circumscribed Hurwitz / first-band excess work inherits
L-W-safe provenance through this audit.

The two remaining audit targets in
[iso/THREE-REGISTER-SYNTHESIS.md](iso/THREE-REGISTER-SYNTHESIS.md)
§2.4 — Fejes-Tóth 1950 (geometric register) and Schmidt 1960
(probabilistic register) — remain open and are tracked separately.

## What changes downstream

- [iso/THREE-REGISTER-SYNTHESIS.md](iso/THREE-REGISTER-SYNTHESIS.md)
  §2.4 — promote the Hurwitz 1902 audit task from "outstanding" to
  "discharged"; add citation pointer to this memo.
- [iso/THREE-REGISTER-SYNTHESIS.md](iso/THREE-REGISTER-SYNTHESIS.md)
  §2.2 (Sobolev content-path witnesses) — add a closing line stating
  the certification is now in hand.
- [iso/DIDOS-PREROGATIVE.md](iso/DIDOS-PREROGATIVE.md) §"Brief
  findings" — append a line registering the audit closure as a
  Hurwitz-derivative finding.
- (Bundled hygiene fix:)
  [iso/THREE-REGISTER-SYNTHESIS.md](iso/THREE-REGISTER-SYNTHESIS.md)
  §"Trust Boundary" — fix the stale `n ≥ 22` Fuglede threshold to
  `n ≥ 8` per the §3.4.1 correction (an internal inconsistency
  identified in today's iso/ surf).

The Sobolev register is the program's load-bearing route for
*rate-sharp* statements about `Δ_n` decay on the inscribed regular
`n`-gon family (per
[iso/THREE-REGISTER-SYNTHESIS.md](iso/THREE-REGISTER-SYNTHESIS.md)
§"Currency-by-Route Map"). The audit's closure means that the
program's principal Hurwitz-rooted content — `Δ_n = 4π⁴/(3n²) +
O(1/n⁴)` and the Parseval-form gap — sits on certified L-W-safe
substrate, not just on the structural fact that "Hurwitz 1902 didn't
need transcendence theory."

## Trust boundary

This memo presupposes:

- The standard textbook statement of Hurwitz 1902's argument as
  represented in **Hurwitz, A. (1902)**, *Annales scientifiques de
  l'École Normale Supérieure*, vol. 19, pp. 357–408, "Sur quelques
  applications géométriques des séries de Fourier." A local PDF of
  Hurwitz 1902 is **not** in `sources/`; the audit verdict is
  conditional on the published proof being what its reception
  describes — Fourier-Parseval arithmetic with no transcendence
  content. The reception is unanimous on this point (see Fuglede
  1989's footnote 1; standard isoperimetric expositions, e.g. Pólya–
  Szegő 1951, Osserman 1978; the Wikipedia article on Hurwitz's
  isoperimetric inequality reproduces the derivation in the form
  above). The audit does not perform a paragraph-level re-read of
  Hurwitz 1902.
- The pre-1882 primitives cited (Fourier 1822, Parseval 1799,
  Green 1828, Cauchy 1821) are themselves transcendence-free in
  content; this is not separately re-audited here, since these
  primitives are universally treated as classical analysis.
- [memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md)'s
  content-not-calendar criterion as the operative L-W-safety
  discipline; per that memo,
  [iso/FUGLEDE-1989-BRIEF.md](iso/FUGLEDE-1989-BRIEF.md) was the
  first crisp example of a post-1882 paper certified L-W-safe via
  Hurwitz 1902 ancestry. This audit certifies the ancestor.

This memo does **not**:

- Prove a new isoperimetric identity or stability bound. The Hurwitz
  identity is established; the audit is a provenance certification.
- Discharge the other two iso/ register audit targets (Fejes-Tóth
  1950, Schmidt 1960). Those remain open and need their own briefs.
- Audit the use of the Hurwitz identity downstream (e.g., the
  first-band concentration argument at
  [corners/HURWITZ-FIRST-BAND-CONCENTRATION.md](corners/HURWITZ-FIRST-BAND-CONCENTRATION.md)).
  The downstream uses are pure algebraic manipulation of the Hurwitz
  identity and are L-W-safe by inheritance, but each new derived
  result inherits this audit's verdict only for the Hurwitz-Parseval
  step itself.
- Comment on Hurwitz 1902's derivations of *other* isoperimetric
  results in the same paper (e.g., Hurwitz also proved
  three-dimensional analogs and considered convexity sharpenings).
  Only the planar Parseval-form gap identity is audited here.

Per
[fft/PROVENANCE-AND-TRANSFERABILITY.md](fft/PROVENANCE-AND-TRANSFERABILITY.md)'s
discipline, this audit cites the named pre-1882 primitives for what
their methods establish (Fourier expansion / Parseval orthogonality /
Green's theorem / complex algebra / Archimedean ratio), not for
content beyond that. Hurwitz 1902 is cited for the planar Parseval-
form gap identity only; not for higher-dimensional generalizations,
not for stability theorems, and not for transcendence content (which
the paper does not contain).
