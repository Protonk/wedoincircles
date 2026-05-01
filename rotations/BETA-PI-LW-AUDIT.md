# BETA-PI-LW-AUDIT

L-W-safety audit on the load-bearing step `finite irrationality measure
for π ⟹ β(π) = 0` invoked at
[paper/OUTLINE.md](paper/OUTLINE.md) §5.1
and flagged at [paper/FIRST-PROOF.md](paper/FIRST-PROOF.md) Lemma A
bullet 1 / debt #8 (the "if load-bearing here, β(π) = 0 needs L-W-safety
provenance per OLD-TIME-RELIGION" caveat).

This is an anchor-mode audit per
[memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md) §"Audit
criterion: content, not calendar." It does not produce a new
irrationality-measure bound; it traces the existing literature chain
the program leans on and tags each link.

Lemma A is parallel-reading and not in the QED ([paper/FIRST-PROOF.md](paper/FIRST-PROOF.md)
§"Strategy", §"Lemma A"). Closing this audit favorably therefore
discharges debt #8 in the parallel-reading sense — it does not move
QED-bearing content. Cosmetically it removes the "do not treat as
L-W-safe until audited" caveat from outline §5.1 and FIRST-PROOF
Lemma A bullet 1.

## Audit target

Outline §5.1 verbatim:

> Arena: finite irrationality measure for π implies the
> Avila–Jitomirskaya parameter β(π) = 0, placing the orbit
> {kπ mod 1} in Weyl's equidistribution regime against Haar measure
> on T = ℝ/ℤ.

Source-side typing per [measure/SUBSTRATE-OBSTRUCTIONS.md](measure/SUBSTRATE-OBSTRUCTIONS.md)
§1:

> The Avila-Jitomirskaya parameter `β(α) = limsup (ln q_{n+1}) / q_n`
> satisfies the one-way implication: finite irrationality measure
> implies `β(α) = 0` … Existing finite irrationality-measure bounds
> for π therefore imply `β(π) = 0`.

The audit splits into two layers per the brief:

1. **The implication itself.** "Finite irrationality measure for π
   ⟹ β(π) = 0." Continued-fraction algebra.
2. **The input.** "Finite irrationality measure for π" as an
   already-established fact in the literature. Where the proof comes
   from, what tools the proof uses.

## Layer 1 — the implication "finite μ ⟹ β = 0"

The K-H-L-A parent memo
([memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md](memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md)
§"Diophantine classification of π") records the elementary derivation:

> Any finite irrationality measure `|α − p/q| ≥ c q^{−C}` forces
> β(α) = 0: applying the lower bound to convergents gives
> `q_{n+1} ≤ c^{−1} q_n^{C−1}`, hence `ln q_{n+1}/q_n → 0`.

The step uses the standard continued-fraction convergent inequality
`|α − p_n/q_n| < 1/(q_n q_{n+1})` together with the irrationality-
measure hypothesis. Combining,

```text
1/(q_n q_{n+1}) > |α − p_n/q_n| ≥ c q_n^{−C}
  ⟹ q_{n+1} < c^{−1} q_n^{C−1}
  ⟹ (ln q_{n+1})/q_n < ((C−1) ln q_n + |ln c|)/q_n → 0,
```

since `q_n → ∞` for any irrational α.

**Tools used.**

- The CF convergent inequality `|α − p_n/q_n| < 1/(q_n q_{n+1})`. This
  is classical in continued-fraction arithmetic: established
  rigorously by Lagrange, present in Euler's CF expositions, and
  standard in any 19th-century treatment by 1820. Pre-1882 in
  calendar **and** content.
- Elementary asymptotic algebra (`ln q_n / q_n → 0` for `q_n → ∞`).
  Trivial.
- The hypothesis `|α − p/q| ≥ c q^{−C}` for some finite `C`. Not
  audited at this layer — that's Layer 2.

**Verdict on Layer 1.** Clean. The implication is pre-1882 in
content and calendar, terminates at standard CF arithmetic, and
introduces no transcendence content beyond what its input carries.
The β parameter is named for Avila–Jitomirskaya (post-2008), but the
*value* β(π) = 0 derived from finite μ(π) does not inherit
post-2008 transcendence content from the parameter's later use in
spectral theory.

## Layer 2 — the input "finite irrationality measure for π"

The literature chain the program references is given at K-H-L-A §"Effective rate":

> Compare against Salikhov's 7.6 (current best) and Mahler's 42 (1953).

and §"Adjacent literature" lists the transcendence-theory landscape:

> Liouville 1844, Hermite 1873, Lindemann 1882, Weierstrass 1885,
> **Mahler 1953**, Baker 1966, Feldman, Waldschmidt, Nesterenko,
> **Salikhov 2008**.

The relevant spine of the irrationality-measure literature on π:

1. **Mahler 1953**, "On the approximation of π," *Indagationes Math.*
   15 / *Proc. Akad. Wet. Amsterdam* A, 56. First effective bound
   `μ(π) < 42` (some expositions report 30 after later refinement).
   Method: explicit Padé-type rational approximations to `π` built
   from arithmetic-bearing hypergeometric integrals; estimates of
   numerator/denominator factorial growth and integral asymptotics.
2. **Mignotte 1974**, refinement.
3. **Chudnovsky 1979/82**, hypergeometric refinement.
4. **Hata 1993**, "Rational approximations to π and some other
   numbers," *Acta Arithmetica* 63: `μ(π) < 8.0161`. Method:
   Padé-style approximations from explicit rational-function
   integrals of the form `∫₀¹ x^a (1−x)^b R(x) dx` with `R` chosen
   for arithmetic structure; arithmetic growth control on
   denominators via *p*-adic valuations.
5. **Rhin–Viola 1996/2003**, group-theoretic / arithmetic-method
   refinements (target: μ(π²) ≤ 5.441).
6. **Salikhov 2008**, "On the irrationality measure of π," *Russ.
   Math. Surveys* 63(3): `μ(π) ≤ 7.6063`. Refines Hata's method
   with delicate symmetry arguments.

**Audit on the methodology layer.** Each of (1)–(6) is a Hermite/Padé-
tradition argument: build explicit rational-coefficient integrals,
estimate denominators, derive a Diophantine inequality from the
`p_n/q_n` thus constructed. None of the standard proofs invokes:

- **Baker 1966** (linear forms in logs of algebraic numbers): would
  be circular for any result *about π* whose method ultimately bounds
  approximation by a single transcendental, since Baker's machinery
  generalizes the Lindemann–Weierstrass theorem the program is
  trying to stay upstream of.
- **Gelfond–Schneider 1934** (transcendence of α^β): orthogonal in
  content; not invoked.
- **Thue–Siegel–Roth 1955** / Schmidt subspace theorem: applies to
  algebraic numbers, not to π. Not invoked in the irrationality-
  measure literature on π.

The Hermite-Padé tradition is L-W-safe in content under
[memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md)'s content-not-
calendar criterion: post-1882 in calendar (Mahler 1953 and later) but
the proof technology is auxiliary-function arithmetic, *p*-adic
valuation control, and integral asymptotics — content present in
Hermite 1873's transcendence-of-`e` proof, with the irrationality-
measure literature carefully extracting only the irrationality-measure
content rather than the full transcendence statement.

**Cross-check at K-H-L-A.** K-H-L-A's own audit hazards
([memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md](memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md)
§"Hazards") include "Liouville-height step routes through L–W"
(§"Hazards" 2) — but that hazard is about the *program's* attempt to
*derive* an effective rate from a Liouville step on the joint
cyclotomic × ℚ(π) field. It does *not* apply to citing finite μ(π) as
established input from the existing irrationality-measure literature.
K-H-L-A line 207 explicitly classifies Padé-approximant methods (e.g.,
Feldman 1960's effective Liouville) as **pre-Baker** in content,
which is the same content-criterion classification this audit lands
on for Mahler/Hata/Salikhov.

**Verdict on Layer 2.** Clean. The literature chain establishing
finite μ(π) is L-W-safe in content. The cheapest L-W-safe witness is
**Mahler 1953**; **Hata 1993** and **Salikhov 2008** are sharper
witnesses in the same content class.

## Hermite-disguise hazard does not apply here

K-H-L-A's "Hazards" §1 names a hazard the program's own attempts
must watch out for — the *Dido route reducing to classical
Hermite–Lindemann in disguise*. That hazard applies at K-H-L-A
level, where the program tries to *replace* Hermite's auxiliary by a
Kraft-Parseval construction; if the Kraft-Parseval auxiliary turns out
to be Poisson-dual to Hermite's, the program has produced a
pedagogical reframing rather than a structurally new tool.

That hazard does **not** apply at the level of this audit. Outline
§5.1 does not attempt a new transcendence proof or a new effective
rate; it cites finite μ(π) as established input, then runs the
Layer-1 implication to obtain β(π) = 0 as an input to Lemma A's
first substrate-side bullet. The program is consuming an
already-established Diophantine fact, not re-deriving one. Hermite-
disguise is a hazard for *new derivations*; for *consumption of
established facts*, the only audit question is whether the
established fact's proof violates the content criterion. It does
not.

## Verdict

**(a) Clean.** β(π) = 0 lifts to outline §5.1 as L-W-safe in content
under
[memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md)'s content-not-
calendar discipline. The chain is:

```text
Lambert 1761 (π irrational; pre-1882, L-W-free)
+ Mahler 1953 / Hata 1993 / Salikhov 2008 (finite μ(π) via
  Hermite–Padé auxiliary-function arithmetic; post-1882 in calendar,
  L-W-safe in content per OLD-TIME-RELIGION)
+ classical CF convergent inequality (pre-1882, L-W-free)
+ elementary CF algebra (pre-1882, L-W-free)
⟹ β(π) = 0.
```

The audit-sensitive link is Mahler/Hata/Salikhov. Each is in the
Hermite-Padé tradition; none invokes Baker, Gelfond–Schneider, or
Thue–Siegel–Roth content. The cheapest L-W-safe witness is Mahler
1953.

The Lemma A first-bullet usage in [paper/FIRST-PROOF.md](paper/FIRST-PROOF.md)
and §5.1 of [paper/OUTLINE.md](paper/OUTLINE.md)
therefore stands without an L-W-circularity hazard.

**Methodological note.** The audit consumes an existing literature
chain; the verdict does not constitute a new irrationality-measure
proof and does not bear on K-H-L-A's open question of whether a
Kraft-Parseval construction can re-derive an effective μ(π)
auxiliary-free. That work remains parked at K-H-L-A under its own
hazards.

## What changes downstream

- [paper/FIRST-PROOF.md](paper/FIRST-PROOF.md) §"Lemma A" bullet 1:
  the audit-debt parenthetical "**[Audit debt:** if load-bearing
  here, `β(π) = 0` needs L-W-safety provenance per
  `memos/OLD-TIME-RELIGION.md`.**]**" can be replaced by a citation
  pointer to this memo.
- [paper/FIRST-PROOF.md](paper/FIRST-PROOF.md) Construction-debt
  table, debt #8: status promotes from **open conditional** to
  **discharged (parallel-reading)**, with the "do not re-claim"
  guidance (do not treat β(π) = 0 as L-W-safe until provenance is
  audited) lifted in favor of a citation pointer.
- [paper/OUTLINE.md](paper/OUTLINE.md)
  §6.7 debt #8 row: same status promotion.
- [measure/SUBSTRATE-OBSTRUCTIONS.md](measure/SUBSTRATE-OBSTRUCTIONS.md)
  §1: backreference to this audit, retaining the careful "finite
  irrationality measure ⟹ β = 0" framing the file already uses.

Lemma A's role in the QED is unchanged: parallel-reading, not in the
QED. The audit closes a flag, not an obligation.

## Trust boundary

This memo presupposes:

- The substantive content of the irrationality-measure literature on
  π (Mahler 1953, Hata 1993, Salikhov 2008) at the level of method
  classification, *not* at the level of independently re-checking
  the bound. The audit verdict is conditional on the published
  proofs being what their reception says they are: Hermite-Padé
  auxiliary-function arithmetic without smuggled Baker / Gelfond–
  Schneider / Thue–Siegel–Roth content. Local PDFs of these papers
  are not in `sources/`; the audit does not perform paragraph-level
  re-reads.
- The CF convergent inequality and elementary CF algebra from any
  standard reference (Hardy–Wright; Khinchin's *Continued Fractions*;
  Khintchine's Russian original).
- [memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md)'s
  content-not-calendar criterion as the operative L-W-safety
  discipline.
- [rotations/10-MARTINIS-BRIEF.md](rotations/10-MARTINIS-BRIEF.md)
  for the β parameter definition.

This memo does **not**:

- Prove a new bound on μ(π).
- Adjudicate the K-H-L-A program's open question of whether a
  Kraft-Parseval construction can produce a new L-W-safe effective
  rate (parked at K-H-L-A).
- Discharge any QED-bearing debt: Lemma A is parallel-reading, and
  this audit closes the parallel-reading flag only.
- Audit the *use* of β(π) = 0 in spectral or substrate contexts
  beyond outline §5.1; downstream consumers should rerun the audit
  if they invoke β(π) = 0 in load-bearing form.

Per [fft/PROVENANCE-AND-TRANSFERABILITY.md](fft/PROVENANCE-AND-TRANSFERABILITY.md)'s
discipline, this audit cites the named irrationality-measure sources
for what their methods establish (Hermite-Padé auxiliary-function
arithmetic; finite μ(π)), not for content beyond that.
