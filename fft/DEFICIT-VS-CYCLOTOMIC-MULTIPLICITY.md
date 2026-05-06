# DEFICIT-VS-CYCLOTOMIC-MULTIPLICITY

Joint-trace observation pairing the row-deficit potential `Ψ(A)` with
the cyclotomic-factor isolation profile coming from the AFW 1984 /
Winograd 1978 reading at
[fft/AUSLANDER-FEIG-WINOGRAD-1984-BRIEF.md](fft/AUSLANDER-FEIG-WINOGRAD-1984-BRIEF.md)
and [fft/WINOGRAD-1978-BRIEF.md](fft/WINOGRAD-1978-BRIEF.md). The
two are independent monitors of FFT progress: `Ψ` is a real-valued
row-state monitor, the multiplicity profile is a discrete polynomial-
side monitor. This memo proposes tracking both simultaneously across
butterfly stages of a fixed schedule and records the observed pattern
for radix-2 DIT, with sketches for mixed-radix and AFW-direct.

The memo is **observational**, not theorem-bearing. It does not claim
a relationship between `Ψ`-progress and cyclotomic-factor consumption;
it tabulates what the joint trace looks like for specific schedules.
The row-deficit lower-bound template would require a separate bounded
native-channel capacity theorem; this memo uses only the row-state
monitor, not that bridge.

Per [memos/AGENTS.md](memos/AGENTS.md): exploratory; sharpens
existing program material; no new external sources.

---

## Two monitors

**Row-deficit potential `Ψ`.** For an `N × N` operator state `A`
with row distributions `pᵢ(j) = |Aᵢⱼ|²`,

```text
Ψ(A) = Σᵢ D(pᵢ ‖ uniform)
     = N log₂ N − Σᵢ H(pᵢ).
```

Endpoints: `Ψ(I_N) = N log₂ N`, `Ψ(F_N) = 0` for any unitary target
with row marginals `1/N`. In the radix-2 DIT trajectory below, each
butterfly stage spreads every row over twice as many coordinates, so
`Ψ` decreases by `N` per stage.

**Cyclotomic-factor isolation profile `iso`.** Polynomial-side
bookkeeping. The cyclic DFT of size `N` decomposes as

```text
ℚ[ℤ/Nℤ] ≅ ∏_{d | N} ℚ(ζ_d),    x^N − 1 = ∏_{d | N} Φ_d(x).
```

At stage `j` of a fixed FFT schedule, the algorithm holds the input
polynomial `f` against a list of sub-product moduli `{m_l(x)}` with
`∏_l m_l = x^N − 1` (the moduli partition `x^N − 1`'s factor over
the algebraic closure). Define `Φ_d` to be **isolated** at stage `j`
if every modulus `m_l` whose vanishing locus meets the `d`-th roots
of unity has its locus contained in `μ_d` (the `d`-th roots of unity)
exclusively — equivalently, if `Φ_d` is not lumped with any other
`Φ_{d'}` (`d' ≠ d`) inside any single `m_l`. Define

```text
iso(j) := Σ { φ(d) : Φ_d isolated at stage j }.
```

`iso(0) = 0`; `iso(final) = N`. Define `Δiso(j) := iso(j) − iso(j−1)`.

The bookkeeping admits three states per `Φ_d`:

- **lumped** — `Φ_d` shares a modulus with some other `Φ_{d'}`;
- **isolated, unresolved** — `Φ_d` sits inside one or more moduli that
  partition `μ_d` only (no foreign cyclotomic factors mixed in);
- **fully resolved** — every modulus containing `Φ_d` is linear over
  `ℚ(ζ_d)` (linear-factor stage).

Both *isolated* and *fully resolved* count toward `iso(j)`; *lumped*
does not.

---

## Worked specimen: radix-2 DIT on cyclic DFT, `N = 2^k`

The radix-2 DIT FFT factors `x^N − 1` along the chain

```text
x^{2m} − 1 = (x^m − 1)(x^m + 1),
```

peeling `Φ_{2m}` at each (`x^m + 1`) split. For `N = 2^k` the moduli
at stage `j` are `2^j` blocks, each of degree `N/2^j`, of the form
`x^{N/2^j} − ω` for `ω` ranging over `2^j`-th roots of unity.

The `Ψ`-side trajectory of radix-2 DIT applied to `I_N` is identical
to the Walsh–Hadamard trajectory in row-marginal coordinates: twiddle
factors are unit-modulus and do not affect `|·|²` distributions. So
`ΔΨ(j) = N` for every `j ∈ {1, …, k}`.

The `iso`-side trajectory is non-trivial. For `N = 8`:

| stage `j` | moduli                                | isolated `Φ_d`         | `iso(j)` | `Δiso` | `ΔΨ` | `ΔΨ/Δiso` |
|-----------|---------------------------------------|------------------------|----------|--------|------|-----------|
| 0         | `x⁸ − 1`                              | —                      | 0        | —      | —    | —         |
| 1         | `x⁴ − 1`, `Φ₈ = x⁴ + 1`               | `Φ₈`                   | 4        | 4      | 8    | 2         |
| 2         | `x² − 1`, `Φ₄ = x² + 1`, two sub-`Φ₈` | `Φ₄`, `Φ₈` (split)     | 6        | 2      | 8    | 4         |
| 3         | 8 linear factors                      | `Φ₁`, `Φ₂`, `Φ₄`, `Φ₈` | 8        | 2      | 8    | 4         |

Cumulative checks: `ΣΔΨ = 24 = N log₂ N`; `ΣΔiso = 8 = N`.

For `N = 16`:

| stage `j` | `iso(j)` | `Δiso` | `ΔΨ` | `ΔΨ/Δiso` |
|-----------|----------|--------|------|-----------|
| 0         | 0        | —      | —    | —         |
| 1         | 8        | 8      | 16   | 2         |
| 2         | 12       | 4      | 16   | 4         |
| 3         | 14       | 2      | 16   | 8         |
| 4         | 16       | 2      | 16   | 8         |

Cumulative: `ΣΔΨ = 64 = N log₂ N`; `ΣΔiso = 16 = N`.

For `N = 32` (`k = 5`): per-stage ratios `2, 4, 8, 16, 16`.
For `N = 64` (`k = 6`): per-stage ratios `2, 4, 8, 16, 32, 32`.

**Closed form (radix-2 DIT, `N = 2^k`).** For `j ∈ {1, …, k}`,

```text
ΔΨ(j) = N,
Δiso(j) = φ(2^{k−j+1})  for j ≤ k − 1,    Δiso(k) = φ(1) + φ(2) = 2,
ΔΨ(j) / Δiso(j) = 2^{min(j, k−1)}.
```

The ratio doubles per stage and plateaus at the final stage because
`Φ₁` and `Φ₂` co-emerge from the terminal `(x² − 1)` lump. The
identity `Σⱼ Δiso(j) · 2^{min(j, k−1)} = N log₂ N` is the
stoichiometric signature of the radix-2 DIT schedule; it does not
transport to other schedules.

---

## Sketch: mixed-radix

For composite `N = p q` (`p, q > 1`, `gcd(p, q) = 1`), the
Cooley–Tukey index decomposition yields a two-stage outer split:
`q` size-`p` sub-DFTs followed by twiddles and `p` size-`q` sub-DFTs
(or vice versa). The cyclotomic side runs along

```text
x^{pq} − 1 = ∏_{d | pq} Φ_d(x),
```

and the per-stage `iso`-profile depends on which Cooley–Tukey ordering
is chosen. Targets for tabulation: `N = 6`, `N = 12 = 4 · 3`,
`N = 15 = 3 · 5`. The schedule's `(ΔΨ, Δiso)` shape interpolates
between the radix-2 extreme (uniform `ΔΨ`, doubling-resolution
`Δiso`) and the AFW-direct extreme below.

---

## Sketch: AFW-direct

A scheme that begins with a single CRT decomposition

```text
f ↦ (f mod Φ_d)_{d | N}
```

isolates every `Φ_d` at stage 1: `Δiso(1) = N`. The `Ψ`-side is
not concentrated at stage 1, however — at the matrix-state level,
the CRT projection is one linear transformation per row, and the
row-amplitude distributions only fully spread once the per-factor
sub-evaluations are computed inside each `ℚ(ζ_d)`. The joint trace
exhibits the opposite shape from radix-2: `Δiso` front-loaded,
`ΔΨ` back-loaded.

---

## Observed pattern

![Joint-trace phase plane: four polylines for N = 8, 16, 32, 64 plotted in the unit square with normalized iso(j)/N on the horizontal axis and normalized cleared deficit (N log2 N − Psi(j))/(N log2 N) on the vertical axis. All four polylines start at (0, 0) and end at (1, 1). A faint dotted diagonal y = x marks the uniform-stoichiometry reference. Each polyline descends below the diagonal: the first vertex always lands at x = 0.5 (radix-2 DIT halves the unresolved factor mass at stage 1) with y = 1/k where k = log2 N, the second vertex at x = 0.75, the third at x = 0.875, and so on along x = 1 − 2^{-j}, producing a staircase that hugs the right edge of the square. The N = 64 polyline is annotated with stage labels j = 1 through j = 6 along its vertices.](figures/deficit_vs_iso_phase_plane.png)

Across the three schedule types, the joint trace `(Ψ(j), iso(j))`
sits at a different point in per-stage space at each intermediate
`j`, even though all three schedules reach the same endpoint
`(0, N)` in `(Ψ, iso)` coordinates after their own number of stages.

- **Radix-2 DIT.** Equal `ΔΨ = N` per stage; `Δiso` halves per stage
  (resolution proceeds outermost-Φ first); ratio `ΔΨ/Δiso` doubles
  per stage; stoichiometric identity tied to the schedule.

- **AFW-direct.** `Δiso` concentrated at stage 1; `ΔΨ` distributed
  across the per-factor sub-evaluation phase. Inverse stoichiometric
  shape.

- **Mixed-radix.** Per-stage `Δiso` heterogeneous, reflecting which
  `p`- or `q`-related cyclotomic factors are extracted at the outer
  Cooley–Tukey stage.

For the schedule shapes sketched here, both monitors are individually
monotone across stages. The joint trace records a coupling: the
radix-2 schedule trades large `Δiso` early for small `Δiso` late
while keeping `ΔΨ` flat, AFW-direct does the opposite, and
mixed-radix interpolates. Only the endpoint totals are conserved
across schedules (`ΣΔΨ = N log₂ N` and `ΣΔiso = N`); the area under
any plotted joint path is schedule-dependent. The shape of the
polyline distinguishes schedules.

---

## What the joint trace reveals beyond either monitor alone

`Ψ(A)` is a row-state monitor. It measures how spread the matrix-
coordinate amplitudes have become and is indifferent to which
polynomial factorization the algorithm tracks underneath.

`iso(j)` is a polynomial-state monitor. It measures how thoroughly
the cyclotomic factorization has been realized by the algorithm's
sub-product moduli and is indifferent to how diffuse the matrix
entries are.

Tracking only endpoint `Ψ` does not distinguish schedules that reach
the same Fourier row marginals; tracking only `iso` does not
distinguish a unitary FFT from a non-unitary procedure with the same
factor-isolation bookkeeping. The joint trace separates these.
Across the schedules considered, both monitors are individually
monotone. The empirical question the trace surfaces — whether
schedules with twiddle-table reuse can break monotonicity of `iso`
while `Ψ` continues to descend — is well-defined inside the
bookkeeping above and stays
observational regardless of how it lands.

---

## Caveats

1. The deficit potential `Ψ` is not committed to as the program's
   cost-norm. The program's commitment is **operational
   compressibility** per
   [fft/COCYCLE-COMPOSITION-LAW.md](fft/COCYCLE-COMPOSITION-LAW.md)
   and debt #14 of [paper/PROOF-CHAIN.md](paper/PROOF-CHAIN.md):
   `δ` is the failure-to-agree of cocycle-product factors across
   butterfly refinements, not the row-deficit potential. `Ψ` is an
   auxiliary monitor; its relation to `δ` is open.

   The transferred lower-bound template for `Ψ` is conditional: if
   every admissible native channel removes at most `C` bits of
   row-deficit, then any path from `I_N` to Fourier-uniform row
   marginals needs at least `(N log₂ N) / C` channels. Pairwise
   coordinate-wise conservative channels have `C ≤ 2`; `b`-local
   conservative channels have `C ≤ b log₂ b`. The unproved bridge is
   that the program's admissible native channels satisfy some such
   `C = O(1)` capacity bound.

2. The `iso` profile is a polynomial-side bookkeeping, not the AFW
   per-factor multiplicative-complexity ledger of paper §3.5
   (`μ(T_P) = 2n − k` per Winograd; factor-by-factor multiplicative
   complexity per AFW). Transferring the joint trace to AFW's actual
   cost coordinate requires a separate audit; the present memo only
   tracks isolation status.

3. The row-distribution calculation treats butterflies as row mixers
   in the matrix-state picture. Twiddle factors do not affect `|·|²`
   distributions, so the radix-2 DIT and Walsh–Hadamard produce the
   same `Ψ`-trajectory on `I_N` input. The cyclotomic
   structure differs (Walsh–Hadamard is a `(ℤ/2)^k` DFT, all-`Φ₁`
   trivially; the radix-2 cyclic DFT runs the full `Φ_d` ladder),
   so the joint trace is non-trivial only on the cyclic-DFT side.

4. Observational, not theorem-bearing. No claim is made that the
   ratio doubling, the stoichiometric identity, or the schedule-
   distinguishing trace shape carries cost-algebra content. Whether
   any of these features survive a uniform-charge re-read at variable
   precision (per debt #9(c) of `paper/PROOF-CHAIN.md`) is open.

---

## Trust boundary

`Ψ(A)` and the row-deficit framework: used only as an auxiliary
row-spread monitor with the definition, endpoints, and conditional
capacity caveat stated above. No row-deficit lower-bound content is
imported.
Cyclotomic-factor structure: AFW 1984 and Winograd 1978 per
[fft/FFT-COMPLEXITY-ARTICULATION.md](fft/FFT-COMPLEXITY-ARTICULATION.md),
cited inside their stated trust boundaries per
[fft/PROVENANCE-AND-TRANSFERABILITY.md](fft/PROVENANCE-AND-TRANSFERABILITY.md).
No lower-bound content is imported from AFW/Winograd; the memo's
content is a joint-trace observation defined inside the program.
