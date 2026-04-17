# CREATI-THE-CIRCLE

A research program conducted by the principle of construction. Every object in scope must be given by an explicit specification: a counting formula, a closed-form expression, or an identity relation between named quantities. Objects that can only be invoked by existence proofs are out of scope. Objects whose composition is partially unknown are out of scope. The working material is what we can write down.

---

**Pointer.** CREATI pursues one leg of a three-candidate approach to the functor F. The abstract triad pattern — identity / polynomial closure (this doc), arithmetic matching (PERMEATE), and residue / spectral rhyme (BIND) — is described in `../TRIAD-ABSTRACT-PATTERN.md`. CREATI is the home of Leg 1 only; the other legs are not pursued from inside this discipline.

**Complementarity note.** CREATI, BIND, and PERMEATE are complementary disciplines by design, not by convergence. Each imposes a different productive constraint: CREATI's is **form** (every object a count, closed form, or identity), BIND's is **vocabulary** (Erasure: no ?(x), Farey, SB, Thomae, Denjoy), PERMEATE's is **preparation** (no cross-domain move without the saturation table behind it). Future lemmas will need to state what each reaches that the others cannot. This doc tolerates those gaps rather than papering them over.

**Working hypothesis (Leg 1 local).** F-via-Chebyshev probably does not exist: log₂(1+m) is not polynomial in m, and the strict polynomial form fails at the first probe. Leg 1's payoff is therefore dual: (1) a named obstruction, and (2) the pseudo-Chebyshev node and n-gon-mediant machinery as a vocabulary for stating that obstruction in circle-side primitives without invoking ?(x). The F question gets a negative answer with computable content; the vocabulary carries forward into the triad-level synthesis. Discipline note: mediants are used here as finite arithmetic operations (add numerators, add denominators, one pair at a time), never as steps in a canonical Stern-Brocot descent — the latter would collapse the Erasure-compatibility that makes the vocabulary portable.

---

## Three modes of construction

**Counting.** Quantities that admit exact enumeration at finite resolution. Divisor counts, polygon position counts, lattice points inside a region, bit-length of a binary sequence, multiplicity at a rational in a Farey-structured histogram, cardinality of a {2,3,5}-smooth slice.

**Closed form.** Quantities expressible in named elementary or special functions with no limiting process hidden inside. d(DH) (the divisor-count function; here d(·) to free τ for the residue). ε(m) = log₂(1+m) − m. 2cos(2π/n). ψ(n) via Euler's totient. The hyperbola y = k·360/n.

**Identity relations.** Forced equalities between constructed objects. The divisor involution d ↔ DH/d. The symmetry of ε under m ↔ 1−m at second order. The trace constraint trace(R) ∈ ℤ. The HCN ladder's exact ratios. The coincidence DH = 360·10^(E−1) ↔ integer E on the logarithmic axis. The Chebyshev relation trace(R_n^m) = 2·T_m(cos(2π/n)).

The discipline: every argument is written as a counting argument, a closed-form manipulation, or an identity chain. Inequalities are admitted only when both sides are constructible and the comparison is exact.

## Catalog of what the construction already gives us

The n-gon apparatus, the ε-framework, and the divisibility test together produce the following explicit objects. These are the raw materials. Nothing in what follows will be used unless it can be built from this list or extended from it by a named operation.

1. **Divisor-indicator sequence.** b_n(DH) = 𝟙[n | DH]. Finite binary string at each DH. Countable. Closed form via remainder test.

2. **Running divisor count.** D(n, DH) = #{d : d | DH, d ≤ n}. Integer-valued. Closed-form bounded by d(DH) (the total number of divisors of DH). Exact at every n.

3. **Running mean.** m(n, DH) = D(n, DH)/n. Closed form. For n ≥ DH, exactly d(DH)/n. For n ≤ DH, the exact step function.

4. **Position set.** P_N = {k · 360°/n : 1 ≤ n ≤ N, 1 ≤ k < n}. Finite. Every element is a rational with denominator ≤ N. Enumerable.

5. **Histogram multiplicity.** For p/q in lowest terms with q ≤ N: h_N(p/q) = ⌊N/q⌋. Closed form. Identity: Σ_{q≤N} φ(q) ⌊N/q⌋ counts P_N with multiplicity.

6. **ε(m).** Real-valued, closed-form, defined on (0,1). Transcendence at algebraic m by Gelfond-Schneider. Fourier decay O(1/n²). Explicit.

7. **Trace of rotation.** For the n-fold rotation R_n: trace(R_n) = 2cos(2π/n). Closed form. Algebraic of degree φ(n)/2 for n ≥ 3, where φ is Euler's totient. Integer iff n ∈ {1,2,3,4,6}.

8. **ψ(n), the crystallographic function (Bamberg–Cairns–Kilminster).** Arithmetic function built additively from Euler's totient on prime-power parts: ψ(p^k) = φ(p^k) for odd p and k ≥ 1, ψ(2^k) = φ(2^k) for k ≥ 2, ψ(2) = ψ(1) = 0, and ψ(mn) = ψ(m) + ψ(n) for gcd(m, n) = 1. Integer-valued, closed form on prime factorization. ψ(n) is the minimum ambient dimension in which an n-fold rotation is crystallographic (ψ(n) ≤ d ⟺ n-fold rotation preserves some d-dimensional Euclidean lattice). Distinct from φ(n)/2 — e.g., ψ(12) = 4 while φ(12)/2 = 2.

9. **Algebraic degree of 2cos(2π/n).** Equal to φ(n)/2 for n ≥ 3. Closed form via the minimal polynomial of ζ_n + ζ_n^{-1} over ℚ; determined by the prime factorization of n through the Galois theory of ℚ(ζ_n). Not the same object as ψ(n); the two functions disagree whenever n has more than one distinct prime factor in its squarefree part beyond {2}.

## New constructions to build

Each of these is an object we do not yet have but which can be constructed from the catalog by operations already named.

### C1. The circle-side residue τ.

Define τ(n) = 2cos(2π/n) − round(2cos(2π/n)). Closed form. Real-valued. Zero exactly on n ∈ {1, 2, 3, 4, 6}, nonzero elsewhere. This is the circle-side analog of the log-side ε(m): an explicit residue function measuring how far the relevant representation object (the trace of the rotation) is from being an integer. BIND extends τ to a continuous-E version τ_c(n, k, E) = frac(k · A · 10^E / n); here we work with the integer-indexed τ. The two objects agree on the intersection where continuous-E lands on integer E.

τ is constructible, countable at every integer n, and has closed-form properties: not periodic in n (a sequence on ℤ_{≥1} with τ(n) → 0 as n → ∞, since 2cos(2π/n) → 2 and round picks up 2 once n is large enough), boundedness in [−1/2, 1/2], and algebraic structure — τ(n) is algebraic of degree φ(n)/2 for n ≥ 5 outside {6}, inherited from 2cos(2π/n) minus an integer.

The zero set {1, 2, 3, 4, 6} is the 2D crystallographic restriction (cf. item 8 on ψ): a 2D rotation matrix R_n in a lattice basis has integer trace exactly for n in this set. The rounding step that defines τ is free — lattice arithmetic — and τ is exactly what that rounding leaves behind. Higher-dimensional lattices enlarge the zero set via ψ; the sibling-paper draft `INSCRIPTION-PAPER-PLAN.md` works 2D throughout.

### C2. The paired complexity table.

For each n in a finite window, build the row (n, τ(n), ψ(n), deg(2cos(2π/n))). For each m in a finite grid on (0, 1), build the row (m, ε(m), algebraic degree of m where defined, rounding-mode dependence of ε under each IEEE mode). Tabulate both. The table is fully constructive and lets us compare τ and ε at matched complexity without invoking any shared-vocabulary object.

### C3. The forced-identity pairs.

Each side has a natural family of identities, but the families are different in kind. Matching them requires being honest about that.

**Log-side (reflection).** ε(m) + ε(1−m) = log₂((1+m)(2−m)) − 1 — a symmetry under m ↔ 1−m. No known iteration identity: ε does not satisfy a closed-form relation expressing ε(k·m) in terms of ε(m) for k ≥ 2.

**Circle-side (iteration).** Chebyshev: trace(R_n^m) = 2·T_m(cos(2π/n)) = 2cos(2πm/n), an iteration identity tying trace(R_n^m) to trace(R_n) via a polynomial. Consequences: double-angle trace(R_n)² = trace(R_n²) + 2; sum-to-product relations between traces at different n. No known reflection identity of comparable depth — obvious candidates like trace(R_n) = trace(R_n^{−1}) collapse by transpose-invariance and are trivial.

The kind-mismatch is itself a pre-result: the log side's rigid identities are reflections, the circle side's are iterations, and any F on identities must transport across that mismatch or declare it an obstruction. Two directions follow, both worth tabulating:

- **Iteration → log side** (pursued in C5). Does ε admit a closed-form relation ε(k·m) = Q(m, k)·ε(m) + …? If yes, that is the log-side Chebyshev cousin; if no, the derivation's failure point is Leg 1's obstruction.
- **Reflection → circle side** (open slot). Does trace on the circle admit a non-trivial reflection identity (some involution σ with trace(R_n) + trace(R_σ(n)) = closed form)? The transpose-trivial candidates fail; whether a richer reflection exists is an open enumeration question.

Build the exhaustive list on each side, classified by kind (reflection, iteration, other). Closed form throughout. The pairing test — does any identity on one side have a closed-form cousin of the same kind on the other — is the rigidity check for F on identities.

### C4. The constructible HCN / SHCN ladder meets the smooth-prime ladder.

The highly composite numbers with prime support in {2, 3, 5} form an explicit list: 1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, ... Countable. Closed-form generation rule (multiply by next available smooth prime power subject to the HCN property). The full HCN list — including numbers whose support extends beyond {2, 3, 5} — begins agreeing with the smooth list until exactly the entry where 7 joins (M = 2520). The first disagreement is a constructible witness to the end of the coincidence regime, and it is a single explicit integer.

### C5. The Chebyshev functor candidate (Leg 1 of the triad).

CREATI pursues the Chebyshev-polynomial leg of F. The other two legs (crystallographic ↔ p-adic, τ_c / ε spectral rhyme) are not pursued from inside this discipline; see `../TRIAD-ABSTRACT-PATTERN.md`.

Define F on identities: the circle-side identity trace(R_n^m) = 2·T_m(cos(2π/n)) is a closed-form polynomial identity tying rotations at different n's. F, if it exists, must send this to a log-side closed-form identity tying ε at different m's. The question is whether such a log-side identity exists.

Concrete first pass. For small integer k ≥ 2, compute ε(k · m) in terms of ε(m) and whatever other arithmetic falls out. Check whether the answer admits a polynomial form in ε(m) with integer (or at least closed-form) coefficients. If yes, name the polynomial family — that is the log-side Chebyshev analog. If no, state the obstruction explicitly: which step of the derivation forces a non-closed-form term.

*Domain note.* ε is defined on m ∈ [0, 1). For m ≥ 1/k the product km leaves the domain, so ε(km) is read through the binade-periodic continuation ε(x) := ε(x − ⌊x⌋) with the binade shift accounted separately (consistent with Landfall's treatment of ε on the binade circle). Any candidate identity ε(km) = Q(m, k)·ε(m) + … is stated after normalizing km back into [0, 1).

Secondary pass. Check the circle-side double-angle identity trace(R_n)² = trace(R_n²) + 2 under F. The log-side image would relate ε(m)² to ε at some function of m. If the log-side image is not closed-form, that is a specific case where F fails.

Each check is a construction, not a hypothesis. They either succeed on the tested identities, which lets us extend to a closed-form F on identities, or they fail on a specific case, which lets us name the obstruction explicitly.

### C6. The obstruction invariant.

If C5 fails on a specific Chebyshev-style identity, build the invariant that witnesses the failure. The invariant must be constructible on both sides: a closed-form quantity computable from the log-side data and a closed-form quantity computable from the circle-side data, with a specific comparison. The failure is a numerical inequality between two explicit numbers, or a structural statement like "the log-side expansion of ε(2m) in terms of ε(m) contains a transcendence that the circle-side Chebyshev polynomial does not."

If C5 succeeds on every tested identity, build the closed-form extension argument. The extension must either be a formula or an algorithm; no nonconstructive continuation is admitted.

## Construction order

C1 is immediate. Build τ as a Python function, tabulate on n = 1..100.

C2 depends on C1 and on the existing log-side tabulation. One table, two columns of residues, compared row by row.

C3 is a literature-and-derivation task. The log-side identities are collected from earlier work; the circle-side identities are derived from Chebyshev polynomial relations for cos(nθ). Tabulate both lists.

C4 is immediate. List the smooth HCN ladder and the full HCN ladder. Identify the first disagreement. That integer (likely 2520) is a named constant in the program.

C5 depends on C1 through C4. The Chebyshev candidate F is tested on the identity pairs from C3.

C6 depends on C5 and on the outcome of the C5 checks.

## What a CREATI result looks like

Four forms are admissible — three with known shape, one reserved for shape we cannot yet name:

**A counting result.** "The number of n ≤ N for which τ(n) is below threshold τ₀ equals the number of m in grid G for which ε(m) is below threshold ε₀, under the Chebyshev F, for all N in a specified range, with closed-form expressions on both sides."

**A closed-form result.** "For every n in a specified family, F sends τ(n) to a function of ε on the log side, and the function is given by [explicit formula in Chebyshev polynomials]."

**An identity result.** "The log-side identity ε(m) + ε(1−m) = f(m) and the circle-side Chebyshev identity [explicit relation among trace iterates] are related by F: [explicit relation]. Therefore the identity structure on each side corresponds under F." (Placeholder letters f, g for closed forms; not to be confused with Euler's φ or the crystallographic ψ used in the catalog.)

**An open-form result (reserved slot).** The Chebyshev leg may produce a result whose shape cannot be stated in advance — a structural claim that is neither a count nor a closed form nor a pre-existing identity, but instead names a new constructible object whose own closed form is the deliverable. This is the one place CREATI allows itself to be loose: loose about result-shape for a result we cannot yet name, tight about everything feeding into it. If the work produces an open-form result, that result retroactively extends the admissible catalog.

**Historical instance.** The father's method in `../../../memos/BIDDER-AND-SON.md` is a 19th-century mental-arithmetic enactment of CREATI applied to log₁₀ computation: a memorized catalog of prime logarithms, plus perception of factor structure to decompose any target into catalog elements. Every result is downstream of the catalog; the difficulty is strategic catalog-traversal. Useful as a worked example of what a CREATI result looks like in a problem domain other than the n-gon construction.

## What is not built here

Nothing that requires an ambient category structure prior to the objects being enumerated. No claims about natural transformations between functors whose source and target categories are not themselves constructed here. Farey structure appears as finite enumeration of rationals k/n with closed-form multiplicity (catalog item 5) — Farey-as-enumeration-primitive is in scope; Farey-as-organizing-frame (Stern-Brocot descent, ?(x) alignment, Thomae-popcorn scaffolding) is not. BIND's Erasure goes further and forbids Farey in any form; CREATI does not. That divergence is deliberate and is the load-bearing distinction between the two disciplines.

The discipline is that every claim in the writeup is downstream of a constructed object listed in the catalog or built by C1 through C6. If a claim requires something off this list, that thing goes on the list and is built, or the claim is removed — with the one exception named under the open-form result slot.

## Deliverable shape

A note whose body is a list of constructions with their closed forms, counting formulas, or identities beside them. A results section that states, for each comparison point between log-side ε and circle-side τ (via the Chebyshev F), the exact numerical or algebraic match or mismatch. A discussion section that sits within the mode of construction — every claim referencing a specific built object — with any open-form result flagged explicitly as such.

Length target: the length required to tabulate the constructions. No less, no more.
