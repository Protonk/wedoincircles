# n-gons

The bridge directory for the regular-anchored-n-gon material. Two sibling directories hold the sides; this one holds the constructions that join them.

- `tangencies/` — what the n-gon does at its edge midpoints on the incircle. Home of the wholeness apparatus and its gcd refinement.
- `corners/` — what the n-gon does at its vertices. Home of the pseudo-Chebyshev nodes and the continuity / deformation / leash material that reads the node sequence as a smooth curve.
- `n-gons/` (this directory) — the bridge: the strip and flip constructions, and the explicit statement that tangency data and corner data are two fixed-and-inverted faces of the same anchored n-gon.

Each construct below is a narrative bestiary entry with three movements: *what it is*, *what it does*, *what it wants*. Full mathematical content lives in the linked file.

---

## The Wholeness Apparatus

A fixed circle. Around it, a family of regular n-gons, each tangent to the circle along one shared anchor edge. Position 0 of every n-gon coincides at angle 0° on the circle; position k of the n-gon sits at angle k · 360°/n. The apparatus deposits rationals k/n on the circle as a function of n.

What it does. It asks whether the angles k · 360°/n are *whole* — integer multiples of a chosen grid unit 360°/DH. The all-positions test reduces to n | DH. Iterating the question as n sweeps {2, 3, 4, …} produces the wholeness sequence b_n(DH) = 𝟙[n | DH] and, taken with multiplicity, the running divisor count D(n, DH) and its mean.

What it wants. Two complementary parametrizations of DH. The positional axis (DH ∈ ℤ_{≥1}) is faithful but combinatorial. The logarithmic axis DH = 3.6 · 10^E (E ∈ ℝ) samples the positional axis sparsely at integer E and continues as a real parameter off those points. The logarithmic axis carries a permanent fingerprint — v_3(DH) ≤ 2 always — which the apparatus cannot shed. This is the *Babylonian fossil*: a coordinate artifact from the choice of B = 3.6 that survives every integer value of E.

What it produces in the limit. Union all positions over all n up to N and you get a histogram h_N(p/q) = ⌊N/q⌋ on the rationals of [0, 1) — a finite-window scaling of Thomae's popcorn function. The Stern–Brocot tree governs how high each rational stands in this histogram.

→ `tangencies/WHOLENESS.md`

---

## The Subpolygon Refinement

The binary test b_n(DH) = 𝟙[n | DH] only detects full survival. The primary observable is the finer gcd

$$g_n(\mathrm{DH}) = \gcd(n, \mathrm{DH}),$$

which records how many of the n-gon's tangency points land on the DH-grid around the incircle. The whole-position set is a cyclic subgroup of ℤ/n of order `g_n(DH)`, and on the incircle it is the tangency-point set of a regular anchored `g_n(DH)`-gon.

What it wants. A graded reading of survival in place of pass/fail, a prime-valuation form `g_n(DH) = ∏_p p^{min(v_p(n), v_p(DH))}`, and explicit worked examples along the `3.6 · 10^E` axis that make the Babylonian `v_3 ≤ 2` cap visible as a capped subpolygon-order exponent at prime 3.

→ `tangencies/SUBPOLYGON.md`

---

## The Pseudo-Chebyshev Nodes

From the same n-gon apparatus, a different question. Don't ask about the full position set; ask about one distinguished point per n. Take the corner of the n-gon directly above the anchor — the point (1, tan(π/n)). Draw the segment from the origin to that corner. It crosses the unit circle at (cos(π/n), sin(π/n)). The x-coordinate of the crossing — node(n) = cos(π/n) — is the *pseudo-Chebyshev node* at n.

What it is. A single scalar per n. The values march monotonically toward 1: node(2) = 0, node(3) = 1/2, node(4) = √2/2, node(5) = (1 + √5)/4, node(6) = √3/2, node(7) ≈ 0.901, and on. Equivalently: node(n) is the k = 1 Chebyshev–Lobatto node at degree n, taken across the polygon family rather than across one fixed degree.

What it wants. To be classified algebraically. The minimal polynomial of node(n) over ℚ has degree φ(2n)/2. So node(n) is rational at n ∈ {2, 3} (where the values are 0 and 1/2), quadratic at n ∈ {4, 5, 6} (the surds √2/2, (1 + √5)/4, √3/2), and first becomes a cubic at n = 7 — also the first non-constructible node by Gauss–Wantzel. The arithmetic depth jumps at exactly the n where the prime support of 2n exits the {2, 3, 5}-smooth regime.

What it tells us about the apparatus. Where the wholeness test asks pass/fail, the pseudo-Chebyshev nodes give a real-valued scalar with explicit arithmetic. They are the program's first encounter with the kind of arithmetic depth that the binary divisibility test obscures.

→ `corners/PSEUDO-CHEBYSHEV-NODES.md`

---

## The Strip and the Flip

Map the annulus `{1 ≤ r ≤ R_3 = sec(π/3) = 2}` to a flat strip by `x = θ/(2π)`, `y = r − 1`. The incircle becomes the strip's bottom edge; each n-gon edge becomes a secant arc that touches the floor at its midpoint (tangency) and rises to `y = sec(π/n) − 1` at the corners. Apply unit-circle inversion `r ↦ 1/r` and the annulus flips to `{1/2 ≤ r ≤ 1}`, with the incircle now the outer boundary and the n-gon corners inverting from radius `sec(π/n)` to radius `cos(π/n)` — the pseudo-Chebyshev node sequence.

What it does. It puts tangencies and corners on the same picture. The strip lays out what every n-gon does simultaneously; the flip exchanges the two radial endpoints of the construction.

What it wants. To be read as the picture in which subpolygon data and pseudo-Chebyshev data are visibly the same object. That reading is carried out in the next entry.

→ `n-gons/ARCHIMEDEAN-STRIP-FLIP.md`

---

## The Strip-and-Subpolygon Link

The strip floor carries the n-gon tangency points at `x = k/n`. Drawing a DH-grid at `x = m/DH` and asking "which tangency points sit on the grid?" is exactly the subpolygon whole-position test, and the answer — a cyclic subgroup of order `gcd(n, DH)` — is the standard lattice-intersection identity on `S¹`. The flip, which fixes the incircle, sends the corners to the pseudo-Chebyshev nodes. So tangency data (subpolygon) and corner data (pseudo-Chebyshev) are the two fixed-and-inverted faces of the same anchored n-gon.

What it does. It removes the sense that subpolygons and pseudo-Chebyshev nodes are two unrelated constructions on the n-gon; they are the two natural things one can do with the n-gon, split by which radial location one reads.

→ `n-gons/STRIP-AND-SUBPOLYGON.md`

---

## The Continuity Frame

Integer-indexed n-gon constructions admit real-valued continuations: replace `n ∈ ℤ` with real `t` and see what changes, what stays, and how the integer samples relate to the continuous object. The pseudo-Chebyshev nodes extend to the curve `x = cos(π/t)` on `t ∈ [2, ∞)`; deformations of the underlying arc (convex-preserving flattening, uniform scaling, translation) give a small family of continuations whose shape-preservation / shape-breaking pattern stratifies by a "leash" — a constraint on which properties survive which deformation.

What it wants. To be treated as the reading frame that holds smooth and arithmetic content side by side. CREATI closed-forms, PERMEATE saturation tables, and BIND domain-internal restatements each see a different slice.

→ `corners/CONTINUITY.md`, `corners/DEFORMATION.md`, `corners/TRANSLATION.md`, `corners/LEASH.md`

---

## The Stern–Brocot Layer (forthcoming)

Inside `tangencies/WHOLENESS.md` §7, a sub-construct waits to be broken out. The position set `P_N = {k · 360°/n : 1 ≤ n ≤ N, 1 ≤ k < n}`, after dividing by 360°, lives on `[0, 1)` as a multiset of rationals. Each rational `k/n` has a specific depth in the Stern–Brocot tree (its level when the tree is rooted at `1/2` and grown by mediants), and the histogram `h_N(p/q) = ⌊N/q⌋` is exactly the Stern–Brocot depth function read over a finite window.

What it will do, once extracted. Make explicit the binary-tree organization of the rationals the wholeness apparatus deposits.

→ to be created.

---

## On adding a construct

A construct earns an entry here when it is (a) load-bearing across multiple program threads, and (b) defined by its own mathematical content rather than by being an adaptation of an external object.

Each new entry gets:

- A self-contained definition file in `tangencies/`, `corners/`, or `n-gons/` (depending on which side of the apparatus it lives on).
- A bestiary entry here with three movements: *what it is*, *what it does*, *what it wants* (this last one is permitted to be slightly anthropomorphic; the constructs are creatures, after all).

If a construct is an adaptation of an external object — Niven's theorem, the 3DT, the crystallographic restriction — it belongs in `memos/`. If it is a discipline or program move — BIND, CREATI, PERMEATE, the F-question triad — it belongs in `triad/`. The n-gon constructs are the objects themselves, full stop.
