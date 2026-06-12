# ADJACENT-PROBLEM-SCOPE

Theorem-safe definition of "adjacent compute-cost problems" and of `n_P`, for `paper/FFT-CLASS-IMPOSSIBILITY-PAPER.md` §4.3 (and its frontier-first successor). Derived by tracing what the proof actually consumes about `P`; every clause below is load-bearing for a named proof step. Supersedes the current §4.3 two-condition block; the refactor's S2 rewrites §4.3 to match. Binding alongside FLOOR-FORMULA-CONTRACT.md.

## What the proof consumes about `P` (the derivation)

| Proof step | What it needs from `P` |
|---|---|
| Proposition F existence half (`δ ≥ (5π−1)·Δ_{n_P} > 0`) | a well-defined, **instance-determined** `n_P ≥ 3` at which the substrate observables read; `Δ_{n_P} > 0` |
| Theorem statement non-vacuity (`cost_c ≥ T_c(P)`) | at least one canon-mechanism lower bound holding **natively** for `P` |
| Channel A (Farey recoding) meaningfulness | `P`'s instances carry frequency-index structure on the lattice `L = {(k, n)}` |
| The exact-frontier sentence | an **in-class** construction achieving `T_c(P)` |
| Per-currency quantifier | `T(P)` = the set of entries that exist natively for `P` — possibly a strict subset of the three mechanisms |

## Definition (adjacent compute-cost problem)

A problem family `P = {P_i}` of **linear or bilinear computational tasks over ℚ̄** is *adjacent* iff:

**(A1) Cyclotomic instance structure.** Each instance `P_i`'s underlying algebra — its evaluation-point set, coefficient algebra, or semisimple decomposition — is cyclotomic with a well-defined **conductor** `n_P(i) ≥ 3` (see below), and `n_P(i)` is unbounded along the family. The substrate observables `f₁ = φ(n_P)/2`, `f₂ = L_{n_P}`, `f₃ = Δ_{n_P}` are thereby determined by the instance itself.

**(A2) Native threshold cell.** At least one canon mechanism applies to `P` *natively* — its own hypotheses holding for `P` without any cross-regime or cross-currency transfer:
- *Morgenstern-type*: bounded-coefficient additive lower bound via determinant potential (requires the instance's matrix family to carry the determinant growth);
- *Winograd-type*: bilinear multiplicative counting via the modular-product theorem (requires modular-product structure `ℚ[x]/T_P`);
- *AFW-type*: rational-equivalence multiplicative counting via semisimple cyclotomic decomposition (requires group-algebra or equivalent semisimple structure).

`T(P)` is the set of entries so obtained — one, two, or three of the mechanisms, and the theorem quantifies over **the entries that exist**, not over all three.

**(A3) — required for exactness only.** Some FFT-style method (finite composition of the five native operations under the §4.2.1 guard) computes `P` at cost matching `T_c(P)` for the cited entry. With (A3), `T(P)` is the **exact frontier** of FFT-style closure on `P`; without it, only the floor half is claimed.

**Definition (`n_P`).** `n_P(i)` := the **conductor** of instance `P_i`'s cyclotomic algebra — the least `N` such that every cyclotomic field in the instance's decomposition is `ℚ(ζ_d)` with `d | N`. Equivalently: the lcm of the orders of the roots of unity the instance evaluates at; the exponent of the underlying abelian group, for group DFTs; the lcm of the cyclotomic-factor indices of the modulus, for modular products. Canonical, computable from the instance, and **not subject to choice by the method or the prover** — the floor's value depends on `n_P`, so any per-proof or per-method discretion here would corrupt Proposition F.

## Examples (in)

- **n-point DFT**, `n ≥ 3`: conductor `n`; Morgenstern cell (bounded-coefficient regime; `|det| = n^{n/2}`); FFT matches → (A3) holds → exact frontier.
- **Cyclotomic-DFT / DFT over `ℚ(ζ_n)`**: conductor `n`; AFW cell; exact.
- **Finite-abelian-group DFT** with group exponent `≥ 3`: conductor = exponent of `G`; AFW cell; AFW's own constructions match → exact. *(Corrects the current §4.3 call "n_P from the group order": the conductor is the exponent, not `|G|`.)*
- **Polynomial multiplication mod `T_P`** with cyclotomic factorization (e.g., `T_P = x^n − 1`, or `Φ_n`): conductor = lcm of factor orders; Winograd cell `μ(T_P) = 2n − k`; CRT constructions match → exact.

## Nonexamples (out), with the failing clause

- **Integer multiplication** — fails (A2): Schönhage–Strassen supplies an upper bound and model discipline, never a canon lower-bound cell. Also fails (A1) in spirit: the Fermat-ring substrate is the *algorithm's* choice, not the problem's; instances carry no canonical conductor.
- **Walsh–Hadamard transform / `(ℤ/2)^k` DFT** — **fails (A1) while satisfying (A2)**: `|det H_n| = n^{n/2}`, so Morgenstern's mechanism applies natively — but the algebra is `ℚ^{2^k}` with conductor 2 < 3. No cyclotomic ladder, no polygon, no deficit: the substrate observables are blind to it, and the floor genuinely says nothing. This is the demonstrative nonexample — it proves (A1) is independent of (A2) and that the definition has teeth. **The theorem does not reach the WHT, and the paper must not imply otherwise.**
- **General matrix multiplication** — fails (A1) (no canonical conductor per instance) and (A2) (its bilinear lower bounds are rank arguments, not the modular-product theorem; "Winograd-type" means the modular-product mechanism specifically, not bilinear counting at large).
- **The normalized FFT in Ailon's model** — not a `T(P)` cell by construction: the entropy potential is the canon's non-transfer *witness*, deliberately excluded from the mechanism list in (A2). Adjacent prior art, not an adjacent problem.
- **DFT sizes `n ∈ {1, 2}`** — degenerate; excluded by `n_P ≥ 3` (the lattice `L` requires it; `Δ_n` reads nothing below the triangle).

## Allowed theorem phrasings

- "For every adjacent problem family `P` (Definition X), every FFT-style method `M`, every instance `P_i`, and each native threshold entry `T_c(P)`: `M` computes `P_i` at cost at least `T_c(P_i)` in currency `c`."
- "Where `P` additionally satisfies (A3), `T(P)` is the exact cost frontier of FFT-style closure on `P`."
- "Adjacency is checkable per family: exhibit the conductor map `i ↦ n_P(i)` and the native cell."
- (scope honesty) "The class includes the canon's own problems and their modular-product and group-algebra relatives; it excludes problems whose algebra carries no cyclotomic conductor — notably the Walsh–Hadamard transform — and problems with upper bounds but no canon cell, notably integer multiplication."

## Forbidden overclaims

- ✗ The old gloss as definition — "compute-cost problems sharing the cost/conversion structure" is an informal gloss only; (A1)–(A3) govern.
- ✗ Any implication that the WHT, integer multiplication, matrix multiplication, or Ailon's normalized model fall under the theorem.
- ✗ Per-method or per-proof choice of `n_P` — the conductor is instance-determined; no adversarial or convenient re-indexing.
- ✗ Claiming exactness for any `P` without exhibiting (A3)'s matching in-class construction.
- ✗ **Treating adjacency as closed under reductions.** Reductions cross regime and currency boundaries — crossing is exactly what the theorem charges — so "poly-time reducible to DFT" confers nothing. Adjacency is a structural property of the instance algebra, not of the problem's reduction neighborhood. State this; it pre-empts the most common scope inflation a reader will attempt on the paper's behalf.
- ✗ Quantifying over "all three currencies" for a `P` whose `T(P)` has fewer native entries.

## Edits this spec mandates (absorbed into PAPER-REFACTOR-PLAN S2)

1. §4.3 rewritten to (A1)/(A2)/(A3) + the conductor definition, replacing the current two-condition block; gloss demoted to a lead-in sentence.
2. Membership-call corrections: group-DFT `n_P` = exponent (not order), with the exponent ≥ 3 caveat; WHT added as the demonstrative nonexample; the reduction-closure caveat added as a `[NOTX]` block.
3. §4.5's quantifier phrased over "each native threshold entry" (it currently reads "every currency entry of the threshold frontier," which is compatible but should be pinned to (A2)'s entry-set reading).
4. ENDPOINT-COMMITMENT's informal "size parameter" (line 29) may optionally be tightened to "conductor" at the next touch of that file — working-doc hygiene, not paper-blocking.
