# CREATI-C3-REFLECTION-ENUMERATION

Closes the open enumeration question at
[BNHA/triad/Creati/CREATI-THE-CIRCLE.md](BNHA/triad/Creati/CREATI-THE-CIRCLE.md)
C3's "Reflection → circle side (open slot)":

> Does trace on the circle admit a non-trivial reflection identity
> (some involution `σ` with `trace(R_n) + trace(R_σ(n)) =` closed
> form)? The transpose-trivial candidates fail; whether a richer
> reflection exists is an open enumeration question.

This memo discharges Open Slot D of
[rotations/SIX-LENS-SYNTHESIS.md](rotations/SIX-LENS-SYNTHESIS.md).
The script implementing the enumeration is
[corners/creati_c3_reflection.sage](corners/creati_c3_reflection.sage).

## Scope

A "reflection identity" in CREATI's sense is an involution
`σ: ℤ_{≥3} → ℤ_{≥3}` (i.e., a map satisfying `σ(σ(n)) = n`) such that

```text
f_σ(n) := trace(R_n) + trace(R_σ(n)) = 2 cos(2π/n) + 2 cos(2π/σ(n))
```

admits a closed-form expression in `n` over an infinite domain. The
phrase "transpose-trivial" excludes:

- `σ = id`, giving `f_σ(n) = 4 cos(2π/n)`, which is closed but trivial;
- `σ` that pointwise fixes the trace (e.g., `σ(n) = -n` extended to
  the negation symmetry on the index), giving `f_σ(n) = 2 trace(R_n)`,
  trivial.

The closed-form criterion in the program's BIND/Erasure-compatible
sense (per
[memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md)) admits
rational expressions, polynomial-in-`1/n` expressions, and identities
within cyclotomic subfields. It does not admit transcendental closure
(arbitrary log-trig combinations beyond what each `2 cos(2π/n)` already
contributes).

## Candidate families enumerated

The script enumerates three structurally natural involution families
and tests `f_σ` on the integer-valued domain in `n ∈ [3, 60]`:

1. **Additive reflection.** `σ(n) = c − n` for `c ∈ {7, 8, 9, 10, 11, 12, 15, 20}`. Involution: `σ(σ(n)) = c − (c − n) = n`. Integer-valued domain: pairs `(n, c − n)` with both ≥ 3.
2. **The `1/n + 1/σ(n) = 1/2` involution.** `σ(n) = 2n/(n − 2)`. Integer-valued only at `n ∈ {3, 4, 6}` (giving the pair `(3, 6)` and the fixed point `n = 4`).
3. **Multiplicative reflection.** `σ(n) = c/n` for `c ∈ {12, 24, 36, 48, 60, 120}`. Involution: `σ(σ(n)) = c / (c/n) = n`. Integer-valued domain: divisor pairs of `c`.

The script also notes — but does not enumerate as `σ`-involutions on
`n` — two adjacent identity-types that are sometimes confused with the
present question:

- **Chebyshev / iteration.** `trace(R_n^m) = 2 cos(2πm/n)` is parameterized by `(n, m)`, not by an involution on `n` alone. Sum-to-product gives closed-form sums for fixed `n` over varying `m`. Lives on the iteration substrate, not the reflection substrate.
- **Galois twist within fixed `n`.** For `n` with multiple prime factors, `(ℤ/nℤ)*` contains involutions `k ↦ k'` (with `kk' ≡ 1 mod n`, `k ≠ ±1`); these give identities like `2 cos(2π/8) + 2 cos(6π/8) = 0` at `n = 8`. They act on indices inside a fixed `n`, not on `n` itself. Different identity-type from `σ`-on-`n`.

## Verdict

**The enumeration closes negatively.** No non-trivial involution
`σ` on `ℤ_{≥3}` produces a closed-form `f_σ` over an infinite domain.
Findings:

| Family | Domain on `n ∈ [3, 60]` | `f_σ` constant? |
|---|---|---|
| `σ(n) = c − n` for `c ∈ [7, 20]` | finite pairs around `c/2` | non-constant for every `c ≥ 8` (each pair sits in a different cyclotomic subfield) |
| `σ(n) = 2n/(n − 2)` | `{3, 4, 6}` (one pair + one fixed point) | **constant: `f_σ ≡ 0`** |
| `σ(n) = c/n` for `c ∈ [12, 120]` | divisor pairs of `c` | non-constant; degenerate `c = 12` gives one pair `(3, 4)` |

The unique informative finding is the `σ(n) = 2n/(n − 2)` involution
on `{3, 4, 6}`:

```text
2 cos(2π/3) + 2 cos(2π/6) = (−1) + (+1) = 0
2 · trace(R_4)            = 2 · 0       = 0
```

This is the equilateral-triangle / regular-hexagon coincidence (the
Niven-set fact that `cos(2π/3) = −1/2` and `cos(2π/6) = +1/2`,
together with the right-angle vanishing `cos(2π/4) = 0`). Its
domain is finite (three integers), so it does not constitute a
structural identity in the program's sense. It is a single
3-element witness, not a reflection law.

All other constant-`f_σ` candidates in the enumeration are
**degenerate**: their integer-valued domain consists of a single
pair `(n_1, n_2)`, so "constant on the domain" reduces to "one value
at one pair." Any single-pair involution is trivially constant; this
is not what CREATI C3 is asking for.

## Why no `σ`-involution can do better, structurally

The non-existence has a clean structural reason. For any involution
`σ` other than the trivially-trace-fixing ones,

- the value `2 cos(2π/n) + 2 cos(2π/σ(n))` lies in the compositum
  `K_n · K_σ(n) ⊂ ℚ(cos(2π/n), cos(2π/σ(n)))`;
- by Niven's theorem, `cos(2π/n) ∈ ℚ` only for `n ∈ {1, 2, 3, 4, 6}`;
- for `n ∉ {1, 2, 3, 4, 6}`, `cos(2π/n)` is an algebraic irrational
  with degree `φ(n)/2` over `ℚ`;
- different choices of `n` typically place `cos(2π/n)` in
  *different* cyclotomic subfields with no algebraic relation
  forcing the sum into `ℚ`.

The only way to force `f_σ(n)` rational across multiple `n` is to
restrict to the Niven set. The richest involution there is
`σ(n) = 2n/(n − 2)` on `{3, 4, 6}`, which gives the 3-element witness
above. Any extension of this involution to a larger domain must
accept that `f_σ` then takes irrational, cyclotomic-subfield-valued
quantities at non-Niven `n` — non-constant by the algebraic-
independence content of the Niven theorem.

The `1/n + 1/σ(n) = 1/2` involution is also the *unique* hyperbolic
Möbius involution `σ(n) = an/(bn + c)` on the upper half-line that
satisfies the angle-supplementarity condition `2π/n + 2π/σ(n) = π`,
under which the cosines sum to zero. Any other Möbius involution
either violates the supplementarity condition (giving non-vanishing
cosine sums in different cyclotomic subfields) or reduces to
`σ = id`. So the Möbius family contributes no further candidate.

## Relation to the kind-mismatch finding

CREATI C3 names the **kind-mismatch** as a pre-result:

> the log side's rigid identities are reflections, the circle side's
> are iterations, and any F on identities must transport across that
> mismatch or declare it an obstruction.

The negative outcome of this enumeration *strengthens* the kind-
mismatch into a **structural finding** rather than an absence-of-
discovery. The circle side does not merely "not yet have" a
reflection identity; it cannot have one in the relevant
infinite-domain sense, by Niven. The enumeration is the negative
evidence that converts the open slot into a closed obstruction.

This is the C3 analog of the closure-mismatch theorem at
[memos/NATIVE-F-MINIMAL-DEFINITION.md](memos/NATIVE-F-MINIMAL-DEFINITION.md):
both are obstruction theorems established by enumerating the
candidate-families on the circle side and showing that the relevant
algebraic-content closure forbids the desired identity.

## Adjacent positive results (for completeness)

The following identities **do** exist on the circle side, in
identity-types that are *not* `σ`-involutions on `n`:

1. **Chebyshev iteration identity.** For fixed `n` and `m ∈ ℤ`,
   `trace(R_n^m) = 2 T_m(cos(2π/n)) = 2 cos(2πm/n)`. Closed form in
   `(n, m)`. Sums of traces of powers within a fixed `n` admit
   product-to-sum formulas:
   ```text
   trace(R_n^a) + trace(R_n^b) = 4 cos(π(a+b)/n) cos(π(a−b)/n).
   ```
   This is what CREATI C3 names as the iteration substrate.

2. **Galois-twist identity at fixed `n`.** For `n` with multiple
   prime factors, the elements `k ∈ (ℤ/nℤ)*` with `k^2 ≡ 1 mod n`
   and `k ≠ ±1` produce involutions on cyclotomic indices. At
   `n = 8`, `k = 3`: `2 cos(2π/8) + 2 cos(6π/8) = √2 + (−√2) = 0`.
   At `n = 12`, `k = 5`: `2 cos(2π/12) + 2 cos(10π/12) = √3 + (−√3)
   = 0`. These hold within the fixed cyclotomic field
   `ℚ(ζ_n)`, not as identities in `n`.

Both are well-defined and worth keeping in the program's catalog, but
neither answers CREATI C3's reflection-on-`n` question. They are
sibling identity-types.

## Trust boundary

This memo may be cited for:

- the negative enumeration verdict for `σ`-involutions on `n`;
- the unique-3-element-witness finding for `σ(n) = 2n/(n − 2)`;
- the upgrade of CREATI C3's open slot to a structural obstruction;
- the catalog of adjacent positive identity-types (iteration,
  Galois-twist) that are *not* `σ`-involutions on `n`.

It should not be cited as proving:

- non-existence of *any* circle-side reflection identity in any
  identity-type (the enumeration is restricted to `σ`-on-`n`);
- a closed-form bridge from CREATI C3 to the log-side
  `ε(m) + ε(1 − m) = log_2((1+m)(2−m)) − 1` reflection (the
  kind-mismatch is now structural rather than open, but no positive
  bridge is constructed);
- a strengthening of the closure-mismatch theorem at
  [memos/NATIVE-F-MINIMAL-DEFINITION.md](memos/NATIVE-F-MINIMAL-DEFINITION.md).
