# COUNTING-APPARATUS

Working notes for the program's most uncertain ambition: binding the counting apparatus at `n-gons/counting/` to the circle-side equivariant surrogate, so that the counting word `M_N` becomes a compute-cost ledger and the whole thing can be stated as a computational-impossibility lower bound paralleling Landfall's log-side result.

This is a **search doc**, not a result doc. It lays out four prerequisites — (A) compute model, (B) task that makes counting the natural ledger, (C) portrait of τ strong enough to carry belief, (D) small-case walkthrough — tracks what's known and unknown for each, and notes which existing repo materials feed in. Progress gets appended here until the pieces are sharp enough to state a conjecture; at that point the result-shaped material promotes to `BNHA/triad/Creati/INSCRIPTION-PAPER-PLAN.md` (Inscription §§1/4 hardening) and possibly its own companion doc.

---

## The target

Landfall's shape, as a template:

- An **equivariant surrogate**: Mitchell's L(x) = E + m, the free-representation estimator of log₂. "The representation is the log table, up to bias."
- A **residue** that survives finite closure: ε(m) = log₂(1+m) − m, continuous but not C¹, Fourier-nontrivial, transcendental at algebraic m.
- A **compute-cost lower bound**: any process beating L to precision ε must perform ≥ f(ε) primitive operations in a fixed compute model. Six walls (§§1–6 of Landfall) each force cost.

Circle-side analog, desired shape:

- **Equivariant surrogate**: `round(2cos(2π/n))`, free in the lattice representation (integer arithmetic on R_n), exact on the crystallographic set {1, 2, 3, 4, 6}.
- **Residue**: τ(n) = 2cos(2π/n) − round(2cos(2π/n)), algebraic of degree φ(n)/2 over ℚ, zeros exactly on the crystallographic set, values in [−1/2, 1/2].
- **Compute-cost lower bound**: any process beating round-trace at n-gon corner resolution N must perform ≥ g(N) primitive operations, where g(N) matches the counting apparatus's `M_N` growth.

Three a-priori facts that make the circle-side ambition plausible, playing the role Gelfond–Schneider / smoothness-break / Padé-closure-failure play on the log side:

1. **Lindemann** (transcendence of π): the classical compute model (ruler-and-compass) literally cannot reach π. Base case.
2. **Unbounded cyclotomic depth**: the algebraic degree of 2cos(2π/n) is φ(n)/2, growing without bound as n sweeps ℤ; no finite cyclotomic extension of ℚ contains all of τ. Closure-failure analog.
3. **Gauss–Wantzel failure at n = 7**: the first non-constructible node in the pseudo-Chebyshev sequence; the first cubic; the first break from ℤ[x]-closure via Chebyshev. Quantitative classical limit.

The facts exist. The work is to assemble them into a belief-forming portrait and wire that portrait to a compute-cost statement.

---

## (A) A compute model

**What it is.** A choice of primitive operations against which "cost" is counted. On the log side, Landfall uses floating-point IEEE operations; the free step is the representation-as-log-table.

**Candidates for the circle side**, in roughly decreasing classical fidelity:

1. **Ruler-and-compass.** Closes outright for non-Fermat-prime n (first at n = 7). Extends to π at the Lindemann limit. Useful as the limiting case — too classical to give quantitative bounds inside the reachable regime.
2. **Ruler-and-compass + integer arithmetic.** Adds a free integer-op budget. Quantitative within the Gauss–Wantzel reachable set, but still closed outside it.
3. **Algebraic-arithmetic over ℚ.** Primitive ops: add, subtract, multiply, divide, adjoin an algebraic number of degree ≤ d. Operations at degree-d cost poly(d). In this model, computing τ(n) to precision ε requires a field extension of degree φ(n)/2, so total cost is poly(φ(n)/2) · log(1/ε). Generalizes ruler-and-compass naturally (which is exactly degree-2ᵏ) and makes Lindemann the E = ∞ boundary.
4. **Algebraic straight-line programs** (ASLP). A cleaner abstract version of (3) measuring depth of field extension plus length of arithmetic circuit. Probably the right formal framework if (3) turns out to be ambiguous.
5. **Gosper-style Möbius transducer.** The log side has Gosper's 8-variable CF machine as an exact-arithmetic compute model. The circle-side analog would be a finite-state transducer on rotation data. Not obviously right; flagged for completeness.

**Decision gate.** Commit before (B) and (D). Current lean: (3) or (4).

**Open:** whether the chosen model is expressive enough to state the bind without circularity, and restrictive enough that the lower bound isn't vacuous.

---

## (B) A task that makes counting the natural ledger

**What it is.** A precise computational task whose primitive-operation cost in the chosen compute model is lower-bounded by `|M_N|` (or some explicit function of M_N). This is the bind itself — the load-bearing piece, and the reason the whole ambition might be vain.

The outside-out counting word `M_N` is already an output of a specific computation — the outside-out corner sweep over regular n-gons n ∈ [3, N] circumscribed around the unit circle, projected to strip coordinates. Each cell of `M_N` records a corner-count at a specific X-value on [−1, 1]. The question is whether this output's length and update complexity are a real cost measure for a task that requires beating the round-trace surrogate.

**Candidate task statements:**

- **T1.** Enumerate corner positions of all n-gons n ∈ [3, N] on [−1, 1] at resolution 10⁻ᵏ. Output: an ordered list of (n, k, X(n, k)) triples with X computed to k decimal places.
- **T2.** Compute `M_N` itself. Output: the integer sequence of length |M_N|.
- **T3.** Distinguish pairs (n, k) whose round-trace agrees but whose actual trace differs at precision ε. Output: a distinguishing witness at each such pair.

T2 is simplest but risks being tautological ("|M_N| is the cost of computing M_N"). T1 and T3 are substantive but need a lower-bound argument that ties them to M_N.

**Target claim:** the cost of T1 (or T3) is Θ(|M_N|) in the chosen compute model. The easy direction (|M_N| as an upper bound, via the outside-out sweep) is constructive. The hard direction (|M_N| as a lower bound) is the real research question.

**Open:** is there a direct reduction from beating-round-trace to corner-enumeration? If yes, T3 is the right task and |M_N| is the right cost. If no, the bind needs a different task — or a different cost measure than |M_N|.

---

## (C) Portrait of τ

**What it is.** A combined structural description of τ(n) that makes the closure-failure visible the way ε's shape did on the log side. Not a proof; a belief-forming picture.

**Atomic facts already in the repo** (scattered across CREATI §§C1/item-9, PSEUDO-CHEBYSHEV-NODES, INSCRIPTION-PAPER-PLAN):

- **Domain**: n ∈ ℤ_{≥1}. Discrete. No natural continuous parameter at this level. (BIND's continuous-E τ_c(n, k, E) is a continuous-parameter analog on a different axis.)
- **Values**: τ(n) ∈ [−1/2, 1/2]. Bounded.
- **Zeros**: exactly {1, 2, 3, 4, 6} (crystallographic set, by Niven).
- **Algebraic structure**: τ(n) is algebraic of degree φ(n)/2 for n ≥ 5 outside {6}; minimal polynomial inherited from 2cos(2π/n) − integer.
- **Galois**: determined by the prime factorization of n through Galois theory of ℚ(ζ_n).
- **Decay**: τ(n) → 0 as n → ∞ (since 2cos(2π/n) → 2 and round picks up 2 once n is large).
- **Cyclotomic closure**: ⋃_n ℚ(τ(n)) has no finite-degree subfield containing all τ(n); any attempt to fit the sequence in a fixed cyclotomic extension breaks at some finite n.
- **No obvious Fourier content**: τ is defined on ℤ, not on a continuous seam. A Dirichlet-style or lattice-Fourier picture may still be worth working out.

**What's missing for the portrait:**

- A single prose statement that collects the above into "here is why no finite algebraic structure reaches τ."
- A decay-rate or average-rate statement (τ(n) = O(1/n²) at large n? something sharper? density at bounded-depth cyclotomic levels?).
- A Stern–Brocot / Farey / counting relation on the same ℤ-domain.
- A spectral or analytic observation analogous to ε's O(1/n²) Fourier tail on the log side.

**Outcome target:** a paragraph that reads, for τ, the way Landfall's §4 reads for ε — compact, load-bearing, a belief pillar.

---

## (D) Small-case walkthrough

Pick **n = 7**. First non-constructible node; first cubic in the pseudo-Chebyshev family; first break from the Chebyshev-reachable regime.

**Three cost measures to compute at n = 7:**

1. **Ruler-and-compass cost**: infinite. node(7) = cos(π/7) is not constructible.
2. **Algebraic-arithmetic cost** (compute model (A3) or (A4)): working in the degree-3 extension ℚ(cos(2π/7)) over ℚ. Computing τ(7) to precision ε requires a field extension of degree 3, arithmetic at that degree, and log(1/ε) digits of precision. Cost: O(poly(3) · log(1/ε)).
3. **Counting-apparatus observable**: `M_7` (the counting word truncated at N = 7). Length, update cost from M_6 → M_7, multiplicity at the new n = 7 corner positions. Already computable via `n-gons/counting/outside_out.py`.

**Target:** the three cost measures track each other (up to constants) across n = 5–11 in a way where the algebraic-degree structure visibly determines the counting-apparatus growth. If it does, that's the belief-forming observation — analogous to plotting ε(m) at a few algebraic m and seeing it doesn't close.

**Candidate artifact:** a script in `n-gons/counting/` producing a figure that shows the three cost measures at n ∈ [5, 11] on one plot with the closure-failure at n = 7 marked.

---

## Adjacent anchors

Existing material this work draws on:

- `memos/LANDFALL-EXPORT.md` — log-side template.
- `corners/PSEUDO-CHEBYSHEV-NODES.md` — algebraic-degree catalog, Gauss–Wantzel constructibility, the n = 7 first-break.
- `BNHA/triad/Creati/CREATI-THE-CIRCLE.md` §§C1, item 9 — τ definition and algebraic-degree.
- `n-gons/counting/COUNTING.md` and the `n-gons/counting/` directory generally — the counting apparatus itself (output `M_N`, update maps, raster figures, Champernowne encoding).
- `BNHA/triad/Creati/INSCRIPTION-PAPER-PLAN.md` §§1/4 — the "softened" walls this work wants to harden.
- `BNHA/SirNighteye/DONT-BELIEVE-ME-JUST-WATCH.md` — the verdict outline, stated in advance in compact-Fourier vocabulary. Its seven rubrics (D1–D4 disanalogies, C5–C7 structural contrasts, plus the coordinative consequence Δ^L = −ε) are each a place this search's quantitative witness has to land. Direct impact here: C6 names item (A)'s compute-model candidate in FFT vocabulary (Cooley–Tukey radix-2 butterfly, native on the unit circle, non-recurring on the log-binade); D1 locates where the Lindemann-dependence of the mismatch enters, feeding the circularity map in `memos/LINDEMANN-BRIEF.md`; and the coordinative-consequence closer reframes "beating the surrogate" as closing an additive-vs-logarithmic (or angular-vs-Euclidean) displacement field — which is the shape the portrait-of-τ in item (C) has been trying to articulate.
- `BNHA/triad/Eraserhead/BIND-THE-CIRCLE.md` — τ_c continuous-E tool; the continuous-parameter analog of τ.
- `memos/CRYSTALLOGRAPHIC-RESTRICTION-BRIEF.md` — the Bamberg–Cairns–Kilminster ψ-function and the higher-dimensional lattice extension.
- `memos/CONTINUED-FRACTIONS-CROSSWALK.md` — the CF axis that cuts across disciplines.
- `memos/LINDEMANN-BRIEF.md` — classical transcendence of π, plus a circularity map for when invoking Lindemann–Weierstrass in the compute-cost argument is safe, programmatically weak, or strictly circular. The base case.

**Anchors yet to be written:**

- Possibly `memos/GAUSS-WANTZEL-BRIEF.md` — ruler-and-compass impossibility for regular 2n-gons at non-Fermat-prime n; the quantitative classical limit. (Alternatively: extend `corners/PSEUDO-CHEBYSHEV-NODES.md` §Constructibility into a richer source-facing anchor.)

---

## What this doc is not

- **Not a proof.** Nothing here is theorem-shaped yet.
- **Not a paper plan.** The paper plan (Inscription) lives at `BNHA/triad/Creati/INSCRIPTION-PAPER-PLAN.md`. This doc is upstream: it supplies the compute-cost content that the paper plan currently disclaims in §"What the paper is for."
- **Not a commitment to achievability.** The ambition may be vain. This doc is for tracking the search while that's still uncertain. Partial success is informative; full failure would be informative too.

---

## Proposed order of work

Ranked from least load-bearing / fastest to complete toward the real research bottleneck:

1. Draft `memos/LINDEMANN-BRIEF.md` (classical anchor).
2. Write (C) — the portrait of τ. A single section; adds directly to this doc or gets its own file once it grows.
3. Decide (A) — the compute model. Short committed statement with a paragraph of rationale.
4. Run (D) — the n = 7 walkthrough. Script + short narrative appended here.
5. Attempt (B) — the task statement. Will likely iterate; interacts with (A) once tried.

Promotion out of this doc: when (C) and (D) together carry belief, and (A) and (B) are sharp enough to state a conjecture, the combined result promotes to an Inscription-§§1/4-hardening section, and `BNHA/triad/Creati/INSCRIPTION-PAPER-PLAN.md` §"What the paper is for" gets its impossibility-disclaim rewritten as an aim.
