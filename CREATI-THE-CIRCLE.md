# CREATI-THE-CIRCLE

A research program conducted by the principle of construction. Every object in scope must be given by an explicit specification: a counting formula, a closed-form expression, or an identity relation between named quantities. Objects that can only be invoked by existence proofs are out of scope. Objects whose composition is partially unknown are out of scope. The working material is what we can write down.

## Three modes of construction

**Counting.** Quantities that admit exact enumeration at finite resolution. Divisor counts, polygon position counts, lattice points inside a region, bit-length of a binary sequence, multiplicity at a rational in a Farey-structured histogram, cardinality of a {2,3,5}-smooth slice.

**Closed form.** Quantities expressible in named elementary or special functions with no limiting process hidden inside. τ(DH). ε(m) = log₂(1+m) − m. 2cos(2π/n). ψ(n) via Euler's totient. The hyperbola y = k·360/n.

**Identity relations.** Forced equalities between constructed objects. The divisor involution d ↔ DH/d. The symmetry of ε under m ↔ 1−m at second order. The trace constraint trace(R) ∈ ℤ. The HCN ladder's exact ratios. The coincidence DH = 360·10^(E−1) ↔ integer E on the logarithmic axis.

The discipline: every argument is written as a counting argument, a closed-form manipulation, or an identity chain. Inequalities are admitted only when both sides are constructible and the comparison is exact.

## Catalog of what the construction already gives us

The n-gon apparatus, the ε-framework, and the divisibility test together produce the following explicit objects. These are the raw materials. Nothing in what follows will be used unless it can be built from this list or extended from it by a named operation.

1. **Divisor-indicator sequence.** b_n(DH) = 𝟙[n | DH]. Finite binary string at each DH. Countable. Closed form via remainder test.

2. **Running divisor count.** D(n, DH) = #{d : d | DH, d ≤ n}. Integer-valued. Closed-form bounded by τ(DH). Exact at every n.

3. **Running mean.** m(n, DH) = D(n, DH)/n. Closed form. For n ≥ DH, exactly τ(DH)/n. For n ≤ DH, the exact step function.

4. **Position set.** P_N = {k · 360°/n : 1 ≤ n ≤ N, 1 ≤ k < n}. Finite. Every element is a rational with denominator ≤ N. Enumerable.

5. **Histogram multiplicity.** For p/q in lowest terms with q ≤ N: h_N(p/q) = ⌊N/q⌋. Closed form. Identity: Σ_{q≤N} φ(q) ⌊N/q⌋ counts P_N with multiplicity.

6. **ε(m).** Real-valued, closed-form, defined on (0,1). Transcendence at algebraic m by Gelfond-Schneider. Fourier decay O(1/n²). Explicit.

7. **Trace of rotation.** For the n-fold rotation R_n: trace(R_n) = 2cos(2π/n). Closed form. Algebraic of degree ψ(n)/2 for n > 2. Integer iff n ∈ {1,2,3,4,6}.

8. **ψ(n).** Arithmetic function built from Euler's totient via ψ(p^k) = φ(p^k) for odd p and k≥1, ψ(2^k) = φ(2^k) for k>1, ψ(2) = ψ(1) = 0, extended additively on prime powers. Closed form on prime factorization. Integer-valued.

9. **Algebraic degree of cos(2π/n).** Equal to ψ(n)/2 for n > 2. Closed form. Identity connecting ψ to the minimal polynomial of 2cos(2π/n).

## New constructions to build

Each of these is an object we do not yet have but which can be constructed from the catalog by operations already named.

### C1. The circle-side ε.

Define ε_c(n) = 2cos(2π/n) − round(2cos(2π/n)). Closed form. Real-valued. Zero exactly on n ∈ {1,2,3,4,6}, nonzero elsewhere. This is the circle-side analog of the log-side ε(m): an explicit residue function measuring how far the relevant representation object (the trace of the rotation) is from being an integer.

ε_c is constructible, countable at every integer n, and has its own closed-form properties: periodicity in n under no integer period (it is quasi-periodic), boundedness in [−1/2, 1/2], and a known transcendence structure because 2cos(2π/n) is algebraic.

### C2. The paired complexity table.

For each n in a finite window, build the row (n, ε_c(n), ψ(n), deg(2cos(2π/n))). For each m in a finite grid on (0,1), build the row (m, ε(m), algebraic degree of m where defined, rounding-mode dependence of ε under each IEEE mode). Tabulate both. The table is fully constructive and lets us compare the two ε's at matched complexity without invoking any shared-vocabulary object.

### C3. The forced-identity pairs.

A forced identity on the log side: ε(m) + ε(1−m) has a known closed form. A forced identity on the circle side: trace(R_n) + trace(R_{n}^{-1}) = 2·trace(R_n) by R_n = R_n^{-T} (orthogonal), giving an immediate involution. Build the exhaustive list of such identities on each side, in a common notation. Closed form throughout. The pairing between log-side and circle-side identities is the first place to check whether a structural correspondence exists, because the identities are the most rigid constructible objects on each side.

### C4. The constructible HCN / SHCN ladder meets the smooth-prime ladder.

The highly composite numbers with prime support in {2,3,5} form an explicit list: 1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, ... Countable. Closed-form generation rule (multiply by next available smooth prime power subject to the HCN property). The full HCN list — including numbers whose support extends beyond {2,3,5} — begins agreeing with the smooth list until exactly the entry where 7 joins (M = 2520). The first disagreement is a constructible witness to the end of the coincidence regime, and it is a single explicit integer.

### C5. The explicit functor candidate.

Define F on the level of objects: F(ε-curve at m) = ε_c-evaluation at a rational related to m by a fixed correspondence. The correspondence itself is to be constructed, not hypothesized. Candidate: send m to the n such that k/n approximates m best among Farey fractions of bounded height, and take ε_c(n). This is a closed-form map on a finite domain, extensible by continuity if it turns out to behave continuously.

F as a map on identities: the forced log-side identity ε(m) + ε(1−m) must, under F, map to a forced circle-side identity. Check on a finite window whether it does.

F as a map on counts: the log-side count of mantissa values for which ε is below a threshold must, under F, map to a circle-side count of n values for which ε_c is below a threshold. Check on a finite window.

Each of these checks is a construction, not a hypothesis. The checks either succeed numerically on a finite window, which lets us extend, or they fail on a specific case, which lets us name the obstruction.

### C6. The obstruction invariant.

If F fails on a specific case, build the invariant that witnesses the failure. The invariant must be constructible on both sides: a closed-form quantity computable from the log-side data and a closed-form quantity computable from the circle-side data, with a specific comparison. The failure is a numerical inequality between two explicit numbers.

If F succeeds on every case checked, build the closed-form extension argument. The extension must either be a formula or an algorithm; no nonconstructive continuation is admitted.

## Construction order

C1 is immediate. Build ε_c as a Python function, tabulate on n = 1..100.

C2 depends on C1 and on the existing log-side tabulation. One table, two columns of residues, compared row by row.

C3 is a literature-and-derivation task. The log-side identities are collected from earlier work; the circle-side identities are derived from orthogonality of rotation matrices and from the Chebyshev identities for cos(nθ). Tabulate both lists.

C4 is immediate. List the smooth HCN ladder and the full HCN ladder. Identify the first disagreement. That integer (likely 2520) is a named constant in the program.

C5 depends on C1 through C4. The candidate F is constructed on the finite domain where all four priors are tabulated, and its behavior on identities and counts is checked.

C6 depends on C5 and on the outcome of the C5 checks.

## What a Creati result looks like

Three forms are admissible:

**A counting result.** "The number of n ≤ N for which ε_c(n) is below threshold τ equals the number of m in grid G for which ε(m) is below threshold τ', under the correspondence F, for all N in a specified range, with closed-form expressions on both sides."

**A closed-form result.** "For every n in a specified family, F sends ε_c(n) to a function of ε on the log side, and the function is given by [explicit formula]."

**An identity result.** "The log-side identity ε(m) + ε(1−m) = φ(m) and the circle-side identity ε_c(n) + ε_c(n') = ψ(n,n') are related by F: [explicit relation]. Therefore the identity structure on each side corresponds under F."

A result that cannot be stated in one of these three forms is out of scope for this program. It does not mean the result is wrong, only that it requires a different working discipline to establish.

## What is not built here

Nothing that requires an ambient category structure prior to the objects being enumerated. No claims about natural transformations between functors whose source and target categories are not themselves constructed here. No appeal to the Farey structure as an organizing frame — the Farey fractions appear as explicit rationals k/n, nothing more, and their properties are used only where the property is a closed-form fact about the specific rational.

The discipline is that every claim in the writeup is downstream of a constructed object listed in the catalog or built by C1 through C6. If a claim requires something off this list, that thing goes on the list and is built, or the claim is removed.

## Deliverable shape

A note whose body is a list of constructions with their closed forms, counting formulas, or identities beside them. A results section that states, for each comparison point between the log-side and circle-side, the exact numerical or algebraic match or mismatch. A discussion section that sits within the mode of construction — every claim referencing a specific built object.

Length target: the length required to tabulate the constructions. No less, no more.
