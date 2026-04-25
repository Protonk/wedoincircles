## 1

In `memos/COUNTING-APPARATUS.md` the program's most uncertain ambition is that `|M_N|` — the length of the outside-out corner-sweep word — is the compute-cost ledger for a circle-side lower bound paralleling Landfall's log-side result. The `(D)` n=7 walkthrough records an honest negative finding: length-of-`M_N` does **not** localize the Gauss–Wantzel algebraic-depth break at n=7. Step increments Δ`|M_n|` across n=5..11 are +2, +1, +3, +2, +4, +2, +5 — a pattern governed by n mod 4 rather than by algebraic depth. A separate observable, the ψ-stratified sweep-x-support (`figures/counting_psi_stratification.png`, `n-gons/counting/PSI-STRATIFICATION.md`), does localize the break.

What is the strongest argument that length-of-`M_N` is structurally the wrong observable for a compute-cost bind, and that the program must pivot to a value-structured or ψ-stratified ledger before committing the compute model (A) or attempting the task statement (B)?

## 2

That is intruiging. I have created a search memo around this very purpose. Read it and answer the following question.

Of the candidate ledgers in `memos/LEDGER-PIVOT-SEARCH.md` §"Items under search", ψ-stratified sweep-x-support is closest-to-hand: already a repo artifact (`n-gons/counting/PSI-STRATIFICATION.md`, `figures/counting_psi_stratification.png`) and already localizes the Gauss–Wantzel break at n=7 where length-of-`M_N` fails. ψ is additive on prime-power parts, which makes it look cyclotomically sensitive in a way length is not.

What is the strongest argument that ψ-stratification factors through its own wrong quotient and inherits the driving impossibility in a subtler form — and if it survives that argument, what is the sharpest compute-cost formulation of a ψ-ledger?

## 3

Candidate #3 in `memos/LEDGER-PIVOT-SEARCH.md` §"Items under search" — "value-structure at distinct x-cells," recording the minimal polynomial (or its degree) of the x-value over ℚ at each occupied x-cell — is the natural promotion target for L3 from the support-level resolution of candidate #1. ψ-stratification was shown to factor through a wrong quotient (ψ vs φ/2), with its value-forgetful forms (L1, L2) inheriting the driving impossibility and its value-retaining form (L3) reducing onto other candidates.

What is the strongest argument that candidate #3 factors through its own wrong quotient and inherits the driving impossibility in a subtler form — and if it survives the argument, what is the sharpest compute-cost formulation of a value-structure ledger that distinguishes it from candidate #2 (row-field-degree tally) and candidate #4 (Galois-orbit count)?

## 4

Candidate #4 in `memos/LEDGER-PIVOT-SEARCH.md` §"Items under search" — bare Galois-orbit count — is placed at orbit tier in §"Structural tiers." At what tier does bare count actually live under the strengthened driving impossibility? If a placeholder attack at orbit tier (sweep substitutions preserving the orbit set and its membership structure) leaves bare count unchanged while varying cyclotomic content, bare count lives strictly below orbit tier and inherits the impossibility via the tier-collapse logic already shown for #1 and #3. If it really is at orbit tier, exhibit the orbit-level placeholder that tests it and state whether bare count passes or fails. If it passes, what keeps the surviving orbit-tier ledger distinct from cell-tier `V_cert` once incidence is retained?

## 5

How does candidate #5 (six-field decomposition as weighted ledger; see `n-gons/counting/COUNTING.md` §backbone) compare to `|M_N|`, `V_cert`, and `O_cert`? What does it retain that `|M_N|` doesn't, and what does it discard that `V_cert` keeps? Given those answers, what should a stress-test of #5 produce — pruning, a refinement, or a new structural tier?

## 6

The new field-incidence tier (item #5's surviving form, F2) was tentatively placed between row-level and cell-level in `memos/LEDGER-PIVOT-SEARCH.md` §"Structural tiers," but the placement is provisional. Field-incidence retains per-cell positional structure with row provenance but discards algebraic content; row-level (item #2 row-field-degree tally) retains per-row algebraic content but discards positional structure. They discard different *kinds* of content, not different *amounts* of the same content, so "more quotient" vs "less quotient" doesn't totally order them.

Is the structural-tiers taxonomy actually a linear chain, or a partial order along (at least) two axes — positional granularity (scalar / row / cell / orbit) and depth of algebraic certification (structural-typing-only / algebraic-content)? If chain, where exactly does field-incidence go relative to row, cell, and orbit, and which existing inhabitant has been mis-located? If partial order, what does the lattice look like and where do the five inhabited points sit?

## 7

The lattice in `memos/LEDGER-PIVOT-SEARCH.md` §"Ledger lattice" tells us when one ledger dominates another. To prove a primitive-op lower bound on one of the candidate tasks in `memos/COUNTING-APPARATUS.md` §(B) — T1 (enumerate corner positions to precision 10⁻ᵏ), T2 (compute `M_N` itself), T3 (distinguish pairs `(n, k)` whose round-trace agrees but whose actual trace differs at precision ε) — we need a ledger that dominates the task's demanded lattice point in a way that cashes out as primitive-op cost. Among the existing surviving inhabitants (`V_cert` at `(P3, A2)`, `O_cert` at `(orbit, A3)`, `F2` at `(P2, A0)`, and row-field-degree at `(P1, A1)`), which can serve which tasks, and which task-ledger pairings are ruled out by the lattice?

## 8

The §"Task-ledger admissibility" section of `memos/LEDGER-PIVOT-SEARCH.md` lists `V_cert` at `(P3, A2)` as the matching ledger for tasks T1 and T3. The matching claim — stronger than mere domination, per §"Ledger lattice" — asserts that no strictly lighter ledger serves a tight primitive-op lower bound on T1 or T3 in the algebraic-arithmetic over ℚ compute model. Try to construct a counter-example: a ledger strictly below `V_cert` in the lattice (less positional content, less algebraic content, or both) that still gives a non-vacuous primitive-op lower bound on T1 or T3. If you find one, identify the new lattice point and the lower-bound argument it carries. If you can't, give a best-effort explanation as to why.

## 9

Cleanup pass on recent search-memo work. Files in scope:

- `memos/LEDGER-PIVOT-SEARCH.md` (heavy revisions, current state)
- `memos/COUNTING-APPARATUS.md` §(A) "Open" paragraph and §(B) "Open" paragraph + "Update from `LEDGER-PIVOT-SEARCH`" annotation
- `README.md` compute-cost branch bullet

Cross-reference against: `n-gons/counting/verify_increment_formula.py`, `n-gons/counting/verify_psi_fracture.py`, `n-gons/counting/COUNTING.md` (six-field decomposition), `memos/CRYSTALLOGRAPHIC-RESTRICTION-BRIEF.md` (ψ definition).

Check two classes of problem:

1. **Hallucinations.** Numerical claims that don't match the scripts (the closed-form Δ|M_n| formula, ψ fracture pairs and largest-spread table, n=7 cubic `8x³ + 4x² − 4x − 1`, ψ-class counts). Citations to other memos that don't say what we claim. References to scripts/files that don't exist as cited. Claims stated as established that lack code or argumentative backing.

2. **Logical warrant.** Claims that don't follow from what's stated. Specifically: is the matching claim's argument actually airtight, or hidden-assumption-dependent? Is the driving impossibility's "working form, not proved" qualifier consistently respected throughout the memo, or do downstream sections quietly treat it as proved? Is the committable triple T1/T3 + V_cert + algebraic-arithmetic actually committable without hidden caveats — e.g., does the Path 1 rank-vs-primitive-op caveat secretly apply to V_cert + algebraic-arithmetic too?

Produce a short report: per-issue, identify file and approximate location, the problem, and the level (hallucination / warrant / minor wording). Don't fix; report.

## 10

What do directed reads of the five papers cited in `memos/FFT-CYCLOTOMIC-COMPLEXITY.md` (linked from `sources/` in the memo's items section) yield, per the memo's §"Order of work" closing template — key theorem statement, hypothesis class, proof technique, and the slot-in sentence specified there? And what structural observations about the literature, if any, bear on the program's bridge plan or on the directed-read agenda itself?

...
