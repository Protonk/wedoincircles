# Irrational-rotation non-closure — the irrational half of the substrate obstruction

Scope: a substrate-side result for §5 of [paper/OUTLINE.md](paper/OUTLINE.md), companion to Theorem K. Audience: a reader who has the §5.6 σ-algebra coarsening (Farey/rational reduction strips the substrate observables) and wants the matching statement on the irrational side of the rotation. This memo states a result inherited from the summability literature and records its substrate role; it is not a source-extraction of either cited paper and does not re-derive them.

## Result

Work on the log circle `ℝ/ℤ` with the rotation that multiplication induces (multiplication is translation in the log coordinate). Take the rotation angle irrational, so the orbit is non-periodic. The accumulated phase does not close under affine averaging, and the obstruction is a change of basis, not of degree.

Concretely, in the i.i.d.-sum mantissa setting where the statement is proved: let `X_i` be i.i.d. with `E X_1 = a ≠ 0` and `σ² = E(X_1 − a)² < ∞`, `Z_n = Σ_{i=1}^n X_i`, and let `h_n(r) = E(|Z_n|^{2πir})` be the mode-`r` Fourier coefficient of the mantissa distribution of `Z_n`.

1. **No convergence.** The leading coefficient is `(|a|n)^{2πir}`: unit modulus, argument `2πr · log(|a|n)`. The argument increases without bound, so `h_n(r)` does not converge.

2. **Cesàro damps modulus, not phase.** `k`-fold Cesàro/Hölder averaging gives leading term `(|a|n)^{2πir} / (2πir + 1)^k`: the modulus contracts to `|2πir + 1|^{−k}` (independent of `n`), but the phase only acquires a constant shift and continues to wind. The averaged sequence is **not Cauchy at any finite `k`** — separation `≥ c · |2πi+1|^{−k}` for an absolute `c > 0`, with per-order floor factor `|2πi+1| = √(1 + 4π²) ≈ 6.362`. Geometric per-order improvement coexists with non-convergence.

3. **Riesz closes; the closing coordinate is non-affine.** Riesz logarithmic means (the `1/j`-weighted averages) converge with no residual. The passage from Cesàro to Riesz is a change of basis, not an increase of degree, and the basis that closes is the non-affine coordinate `ψ(m) = log₂(1 + m)`.

## Trust boundary

Items 1–3 are proof-grade in **Schatte 1986** (Math. Nachr. 127, 7–20; Lemma 1, Lemma 6, Theorem 5) assembled with **Tsao 1974** (Comm. ACM 17(5), 269–271; the leading-digit / cumulative-averages side). The two are not held in this repo's `sources/` and are inherited as stated, not independently re-derived here. What this repo contributes is the substrate-role reading below; that reading is an inference, not part of the cited theorems.

## Substrate role — the irrational complement to Theorem K

Theorem K ([measure/FOR-BREAKFAST.md](measure/FOR-BREAKFAST.md) §K) and this result are two specializations of one obstruction: **affine flatness cannot reach what the rotation generates**, with the target's type set by the arithmetic of the rotation angle.

- **Rational angle `2π/n`.** The rotation lands in the cyclotomic ladder `K_n = ℚ(cos 2π/n)`, degree `φ(n)/2` — finite at each `n`, unbounded over the family. Affine closure is flat and cannot carry the family ([paper/OUTLINE.md](paper/OUTLINE.md) §5.4). Theorem K is the σ-algebra form: the substrate observables `f₁ = φ(n)/2`, `f₂ = L_n`, `f₃ = Δ_n` do not factor through the Farey reduction `R`. **This is the rational half.**
- **Irrational angle.** The orbit is non-periodic; its averaged Fourier content does not close under affine (Cesàro) iteration, and closure requires the non-affine `ψ`. **This is the irrational half — the present result.**

The two halves are disjoint in the kind of obstruction they record. §5.6's coarsening is a measurability fact about a rational reduction map; §5.1 ([measure/SUBSTRATE-OBSTRUCTIONS.md](measure/SUBSTRATE-OBSTRUCTIONS.md) §1) is a kinematic equidistribution fact (Weyl, Haar mean) and §5.5 a measure-class fact (Lebesgue null/full). This is a third kind — a **non-closure** fact about affine averaging on the irrational orbit — and it occupies the corner §5 otherwise leaves open: the actual coefficient coordinate is the transcendental log coordinate, not a rational reduction of it, and the irrational regime needs its own obstruction.

The non-affineness of `ψ` is the load-bearing link to affine flatness: affine maps compose to affine maps, so no finite composition of native operations produces `ψ`. The deviation of `ψ` from the identity, `ψ(m) − m = log₂(1+m) − m`, is the program's residue `ε`; this is a coordinate identity, recorded for locating the object, and carries no weight beyond it.

## L–W safety

The result is transcendence-free in content. Items 1–2 require only that the accumulated logarithmic phase `2πr · log(|a|n)` be unbounded and non-periodic — i.e. that the rotation be irrational. They do **not** invoke an irrationality measure, a Diophantine class, or any transcendence statement about the rotation angle; the non-closure follows from unboundedness of the logarithm and Cesàro/Riesz summability, both pre-1882. The posture matches [rotations/BETA-PI-LW-AUDIT.md](rotations/BETA-PI-LW-AUDIT.md): the available Diophantine strength is not needed here, and the weaker input (mere irrationality) is what the obstruction rests on. No item triggers the hazard repertoire of [memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md).

## Provenance and placement

Inheritance chain: Tsao 1974 (cumulative-averages logarithmic law, via Flehinger 1966) and Schatte 1986 (Fourier-coefficient machinery for i.i.d.-sum mantissa distributions) → the assembled Cesàro-non-closure / Riesz-convergence statement above. Placement: §5 substrate menagerie, sibling to Theorem K ([measure/FOR-BREAKFAST.md](measure/FOR-BREAKFAST.md) §K) and to the angle catalogue at [measure/SUBSTRATE-OBSTRUCTIONS.md](measure/SUBSTRATE-OBSTRUCTIONS.md). Not load-bearing for the §6 cost argument; it completes the substrate-side picture and is consumed there as the irrational-angle entry alongside K's rational-angle entry.
