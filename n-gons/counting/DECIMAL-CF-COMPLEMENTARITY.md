# Decimal / CF Complementarity

Two encodings of a finite integer sequence `[a_0; a_1, a_2, …, a_m]`:

- **Decimal concatenation** `D`. Write `a_0` as integer part; concatenate the base-10 digits of `a_1, a_2, …, a_m` in order as mantissa. For `M_N` this is the pseudo-Champernowne number `C_N` (see [PSEUDO-CHAMPERNOWNE.md](PSEUDO-CHAMPERNOWNE.md)).
- **Continued fraction** `F`. Read the entries as partial quotients:

```
F = a_0 + 1/(a_1 + 1/(a_2 + 1/(… + 1/a_m))).
```

Both map an integer sequence to a real. They are not the same, and this memo argues they are *complementary* probes of `M_N`: `D` averages entries against geometric positional weights, so it's dominated by what sits near the decimal point; `F` is magnitude-amplifying and parity-sensitive, so it's dominated by whichever partial quotient is largest and records its depth in the sign. Two toys make the point, each from a different angle.

## Toy 1: single exception at different depths

Perturb a bulk sequence by replacing one `2` with a `20`, at two different depths:

- `P₀ = [1; 2, 2, 2, 2, 2, 2]`    (bulk)
- `P₃ = [1; 2, 2, 20, 2, 2, 2]`   (exception at depth 3)
- `P₄ = [1; 2, 2, 2, 20, 2, 2]`   (exception at depth 4)

Compute both encodings:

| seq | `D` | `F` | `ΔD` | `ΔF` |
|---|---|---|---|---|
| `P₀` | `1.222222`  | `577/408 ≈ 1.414216`  | —              | —              |
| `P₃` | `1.2220222` | `1751/1249 ≈ 1.401922` | `−2.0 × 10⁻⁴` | `−1.2 × 10⁻²` |
| `P₄` | `1.2222022` | `1769/1249 ≈ 1.416333` | `−2.0 × 10⁻⁵` | `+2.1 × 10⁻³` |

Two things to notice.

**Magnitude.** `|ΔD|` shrinks by a factor of `10` as the exception moves one slot later — that's the positional weighting of decimal digits. `|ΔF|` is 60–100× larger than `|ΔD|` at both depths. The reason is that a large partial quotient `a_k` drives `1/(a_k + …)` toward zero, which collapses the CF's tail into a near-trivial remainder. `F` responds to the *shape* of a large entry, not just to its digit count.

**Sign.** `ΔD` is negative at both depths — `D` is monotone in any single entry at any fixed position. `ΔF` *flips sign* between `P₃` and `P₄`. This is the classical parity-of-depth rule for continued fractions: increasing `a_k` raises `F` if `k` is even and lowers it if `k` is odd. So `F` encodes not just *that* the exception exists but *at what depth* it sits.

`D` sees the exception as a small digit-cluster edit whose effect decays 10-to-1 with position. `F` sees it as a truncation event whose sign depends on parity. Same entries, two genuinely different readings.

## Toy 2: same decimal, different CFs

Toy 1 shows `D` and `F` respond differently to the same perturbation. Toy 2 shows something stronger: `D` actually discards information that `F` preserves. Take three sequences whose mantissas concatenate to the *same digit string* `123`:

- `S₁ = [1; 1, 2, 3]`
- `S₂ = [1; 12, 3]`
- `S₃ = [1; 1, 23]`

Then `D(S₁) = D(S₂) = D(S₃) = 1.123`. But the CF values disagree:

| seq | `F` |
|---|---|
| `S₁ = [1; 1, 2, 3]` | `17/10 = 1.7000` |
| `S₂ = [1; 12, 3]`   | `40/37 ≈ 1.0811` |
| `S₃ = [1; 1, 23]`   | `47/24 ≈ 1.9583` |

The three `F` values aren't close — they range over most of the interval `[1, 2]`. `D` has collapsed three distinct integer sequences to one real number; `F` hasn't. As a map from finite integer sequences to reals, `D` is not injective: it conflates any two sequences that concatenate to the same digit string. `F` is essentially injective (one standard tail ambiguity aside, where `[…, a_m]` with `a_m ≥ 2` equals `[…, a_m − 1, 1]`).

This is the underlying reason the two readings of `M_N` can't be reconstructed from each other. `C_N` alone does not uniquely determine `M_N` once any multiplicity reaches two digits — and for `M_N` the counts at `x = ±1`, `x = 0`, and the terminal `2(N − 2)` are generically multi-digit, so the decimal loses their precise values.

## What this says about `M_N`

`M_N` has the six-field structure

```
1×a   [count at x=−1]×1   2×b   [count at x=0]×1   2×c   [count at x=+1]×1
```

from [COUNTING.md](COUNTING.md). Apply the two encodings:

- **Decimal.** `C_N → 10/9` because the `1×a` prefix (with `a ≈ N/2`) dominates the early, high-weight decimal positions; everything else — the three exceptional singletons, the long `2` fields, the terminal `2(N − 2)` — sits at decimal positions of order `a + 1` or later, contributing at most `O(10⁻ᴺ/²)` each. `D` averages the whole sequence against a geometrically-decaying weight and collapses the structural information into a tiny correction away from `10/9`.
- **Continued fraction.** A hypothetical `F(M_N)` reads the same entries as partial quotients. The `1×a` prefix is a stretch of all-`1`s, whose convergents approach the golden ratio `φ`. Then the count at `x = −1` is a large partial quotient at depth `a + 1`; it truncates the tail, pinning `F(M_N)` close to the `a`-th golden-ratio convergent. The count at `x = 0` (when present) adds a sign-alternating correction; the `2×b` and `2×c` fields contribute smaller adjustments; the terminal `2(N − 2)` adds a final small correction.

So `D` sees the bulk of the prefix and averages everything else away to `10/9`, while `F` sees the prefix as a golden-ratio convergent and would render the six-field exceptions as discrete, sign-alternating truncation events. Decimal collapses `M_N`'s interior structure into noise near a base-10 limit; CF preserves it as a legible sequence of events near a base-agnostic limit. Complementary probes, not redundant ones.

## Numerical check

Figure [counting_dual_convergence.png](../../figures/counting_dual_convergence.png) plots `log₁₀` of `|C_N − 10/9|`, `|F(M_N) − φ|`, and `|F(M_N) − p_a/q_a|` (the golden-ratio convergent at depth `a − 1`) for `N = 5 … 50`, against the closed-form predictions `−a` and `−(2a+1) log₁₀ φ`. Both empirical rates match their predictions. The decimal distance decays at roughly 2.4× the CF rate in log-scale — `log₁₀ |C_N − 10/9| ≈ −24` versus `log₁₀ |F(M_N) − φ| ≈ −10` at `N = 50` — and `F(M_N)` sits close to (slightly below) the pure golden-ratio convergent, confirming that the large count-at-`x=−1` at depth `a + 1` does act as a truncation event. Same sequence, two different limits, two different rates, both closed-form.
