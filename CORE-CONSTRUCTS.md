# CORE-CONSTRUCTS

The constructions our program is *about*. Each construct has its full mathematical definition in `core/`. This document is the bestiary — a narrative description of what each construct is, what it does, and what it wants. It is not a precis of the program. The program's threads (the disciplines, the F question, the legs of the triad) live in `triad/`. The reference material we read to inform the program lives in `memos/`. The raw external sources and cross-source syntheses live in `sources/`. The core constructs are the *objects themselves* — the geometric, algebraic, and combinatorial creatures the rest of the work studies.

---

## The Wholeness Apparatus

A fixed circle. Around it, a family of regular n-gons, each tangent to the circle along one shared anchor edge. Position 0 of every n-gon coincides at angle 0° on the circle; position k of the n-gon sits at angle k · 360°/n. The apparatus deposits rationals k/n on the circle as a function of n.

What it does. It asks whether the angles k · 360°/n are *whole* — integer multiples of a chosen grid unit 360°/DH. The all-positions test reduces to n | DH. Iterating the question as n sweeps {2, 3, 4, …} produces the wholeness sequence b_n(DH) = 𝟙[n | DH] and, taken with multiplicity, the running divisor count D(n, DH) and its mean.

What it wants. Two complementary parametrizations of DH. The positional axis (DH ∈ ℤ_{≥1}) is faithful but combinatorial. The logarithmic axis DH = 3.6 · 10^E (E ∈ ℝ) samples the positional axis sparsely at integer E and continues as a real parameter off those points. The logarithmic axis carries a permanent fingerprint — v_3(DH) ≤ 2 always — which the apparatus cannot shed. This is the *Babylonian fossil*: a coordinate artifact from the choice of B = 3.6 that survives every integer value of E.

What it produces in the limit. Union all positions over all n up to N and you get a histogram h_N(p/q) = ⌊N/q⌋ on the rationals of [0, 1) — a finite-window scaling of Thomae's popcorn function. The Stern–Brocot tree governs how high each rational stands in this histogram. The apparatus is, in this sense, the program's geometric face onto the circle's full rational structure.

→ `core/NGON-WHOLENESS.md`

---

## The Pseudo-Chebyshev Nodes

From the same n-gon apparatus, a different question. Don't ask about the full position set; ask about one distinguished point per n. Take the corner of the n-gon directly above the anchor — the point (1, tan(π/n)). Draw the segment from the origin to that corner. It crosses the unit circle at (cos(π/n), sin(π/n)). The x-coordinate of the crossing — node(n) = cos(π/n) — is the *pseudo-Chebyshev node* at n.

What it is. A single scalar per n. The values march monotonically toward 1: node(2) = 0, node(3) = 1/2, node(4) = √2/2, node(5) = (1 + √5)/4, node(6) = √3/2, node(7) ≈ 0.901, and on. Equivalently: node(n) is the k = 1 Chebyshev–Lobatto node at degree n, taken across the polygon family rather than across one fixed degree.

What it wants. To be classified algebraically. The minimal polynomial of node(n) over ℚ has degree φ(2n)/2. So node(n) is rational at n ∈ {2, 3} (where the values are 0 and 1/2), quadratic at n ∈ {4, 5, 6} (the surds √2/2, (1 + √5)/4, √3/2), and first becomes a cubic at n = 7 — also the first non-constructible node by Gauss–Wantzel. The arithmetic depth jumps at exactly the n where the prime support of 2n exits the {2, 3, 5}-smooth regime.

What it tells us about the apparatus. Where NGON-WHOLENESS asks pass/fail (does this n divide DH?), the pseudo-Chebyshev nodes give a real-valued scalar with explicit arithmetic. They are the program's first encounter with the kind of arithmetic depth that the binary divisibility test obscures.

→ `core/PSEUDO-CHEBYSHEV-NODES.md`

---

## The Stern–Brocot Layer (forthcoming)

Inside `core/NGON-WHOLENESS.md` §7, a sub-construct waits to be broken out. The position set P_N = {k · 360°/n : 1 ≤ n ≤ N, 1 ≤ k < n}, after dividing by 360°, lives on [0, 1) as a multiset of rationals. Each rational k/n has a specific depth in the Stern–Brocot tree (its level when the tree is rooted at 1/2 and grown by mediants), and the histogram h_N(p/q) = ⌊N/q⌋ is exactly the Stern–Brocot depth function read over a finite window.

What it will do, once extracted. Make explicit the binary-tree organization of the rationals NGON-WHOLENESS deposits. The apparatus produces the rationals; the layer organizes them by their tree depth and exposes the recursive mediant structure that connects them.

What it will want. To be treated as a combinatorial / order-theoretic object on its own terms — separate from the geometric apparatus that produces its inputs and separate from the rational-approximation theory (continued fractions, Liouville/Diophantine classification) that its convergents share with the spectral-side material in `memos/`.

This entry is a placeholder. The break-out has not happened yet. When it does, the new file will land at `core/STERN-BROCOT-LAYER.md` (or similar), and this entry will be expanded.

→ to be created.

---

## On adding a construct

A construct earns a `core/` entry when it is (a) load-bearing across multiple program threads, and (b) defined by its own mathematical content rather than by being an adaptation of an external object.

Each new entry gets:

- A self-contained definition file in `core/`, full math.
- A bestiary entry here with three movements: *what it is*, *what it does*, *what it wants* (this last one is permitted to be slightly anthropomorphic; the constructs are creatures, after all).

If a construct is an adaptation of an external object — Niven's theorem, the 3DT, the crystallographic restriction — it belongs in `memos/`, not `core/`. If it is a discipline or program move — BIND, CREATI, PERMEATE, the F-question triad — it belongs in `triad/`, not `core/`. The core constructs are the objects themselves, full stop.
