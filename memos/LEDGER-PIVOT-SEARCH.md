# LEDGER-PIVOT-SEARCH

Search memo. Target: a replacement ledger for the counting-apparatus
compute-cost ambition that is sensitive to cyclotomic depth rather than
residue-class parity. Opened because [memos/COUNTING-APPARATUS.md](memos/COUNTING-APPARATUS.md) §(D)
records that length-of-`M_N`, the current candidate ledger, factors through
an invariant that does not track `φ(n)/2`. This memo sits downstream of
`COUNTING-APPARATUS`: if a candidate passes here, it hands off to §(A)/(B);
if no candidate passes, the branch closes negative with an explicit
impossibility.

Register: search memo, append-only during active life, provisional.

---

## Driving impossibility (working form, not proved)

The compression `(n, k, x_{n,k}) → M_N → |M_N|` is a two-stage quotient. The
first stage keeps collision multiplicities at equal x-values, discarding the
x-values themselves. The second keeps only the length (count of occupied
x-cells), discarding the multiplicity sequence. The load-bearing step is the
first: any two sweep inputs with the same collision pattern yield identical
`M_N`, hence identical `|M_N|`.

The working impossibility: a hypothetical "generic rational placeholder"
sweep — x-values chosen to be arbitrary rationals matching the real sweep's
collision pattern exactly — has no cyclotomic depth but the same `|M_N|`.
Therefore any cost measure that factors through `|M_N|` cannot lower-bound
tasks whose difficulty is cyclotomic-depth-controlled.

The placeholder construction is not yet shown to exist for every collision
pattern. Some real-sweep collisions may be forced by algebraic coincidence
in a way that resists rational stand-ins. Working assumption: the
impossibility holds modulo that construction question, and the live search
is what ledger avoids the quotient.

**Strengthened form (algebraic placeholders).** A generalization, surfaced
during candidate #3's stress-test: instead of rational stand-ins, use
algebraic-of-same-degree stand-ins. For each occupied x-cell of degree
`d`, replace its x-value by a fresh algebraic number of degree `d` that
is not a Galois conjugate of the original. The collision pattern, the
degree multiset, and even per-cell algebraicity are preserved; cyclotomic
provenance, real embedding, and incidence structure are not. Any ledger
that factors through `(collision pattern, degree multiset)` therefore
inherits the impossibility — including degree-only forms of value-
structure (item #3 in its naive form) and degree-blind Galois-orbit
counts (item #4 if not refined). The placeholder attack is parameterized
by lattice coordinate; see §"Ledger lattice" below for the
domination-and-defeat conditions.

**Scalar-summary failure pattern.** `|M_N|` itself was the program's
first encounter with a more general failure pattern, surfaced during
candidate #4's stress-test: any ledger that takes scalar count of
equivalence classes after a structural quotient inherits the driving
impossibility by construction, regardless of which parent quotient
produced the count. Bare Galois-orbit count (item #4 in its naive form)
sits at the same `(P0, A0)` lattice coordinate as `|M_N|`, just from a
different parent quotient. The pattern is predictive: future candidates
that factor through "count of X-equivalence classes" are flagged a
priori. See §"Ledger lattice" for inhabitants by coordinate and what
structural content has to survive each placeholder attack.

## First exhibit: closed-form Δ|M_n|

Verified empirically at [n-gons/counting/verify_increment_formula.py](n-gons/counting/verify_increment_formula.py),
n = 3 through 40. The script reports two MISS rows at n = 4 and n = 6,
which are the non-trivial Niven zeros (`τ(4) = τ(6) = 0`,
crystallographic restriction); the closed form below holds for all
other tested n:

    odd n:         Δ|M_n| = (n - 1)/2
    n ≡ 0 mod 4:   Δ|M_n| = (n - 4)/2      [n = 4 boundary: actual +1]
    n ≡ 2 mod 4:   Δ|M_n| = (n - 6)/2      [n = 6 boundary: actual +1]

The recurrence is clean from n = 7 onward in all three residue classes.

The formula is governed by `n mod 4` alone — not by `φ(n)/2`. The two agree
numerically on odd primes, since `(p-1)/2 = φ(p)/2`; the fracture is visible
on composites and prime powers:

| `n`  | class      | `φ(n)/2` | `Δ|M_n|` | fracture |
|-----:|:-----------|---------:|---------:|---------:|
|    5 | prime      | 2        | 2        | 0        |
|    7 | prime      | 3        | 3        | 0        |
|    9 | prime²     | 3        | 4        | +1       |
|   11 | prime      | 5        | 5        | 0        |
|   15 | composite  | 4        | 7        | +3       |
|   21 | composite  | 6        | 10       | +4       |
|   25 | prime²     | 10       | 12       | +2       |
|   27 | prime³     | 9        | 13       | +4       |
|   33 | composite  | 10       | 16       | +6       |

Length-of-`M_N` grows linearly in `n` within each residue class; `φ(n)/2`
grows with irregular factor structure. The agreement on odd primes is the
reason the naive "length tracks algebraic depth" reading looked plausible
longer than it should have. The fracture column is the receipt.

## Second exhibit: ψ fracture

Verified at [n-gons/counting/verify_psi_fracture.py](n-gons/counting/verify_psi_fracture.py),
default range `n = 3` through `60`.

The ψ-pivot repairs the `n = 7` miss because ψ is sensitive to prime-power
content. But ψ is additive on prime-power parts, while the trace-field degree
`φ(n)/2` inherits φ's multiplicative cross-prime coupling. Equal-ψ classes can
therefore hide different trace degrees.

Named equal-ψ / different-degree pairs:

| rows | ψ | trace degrees `φ(n)/2` | spread |
|---:|---:|---:|---:|
| `7`, `15` | 6 | `3`, `4` | 1 |
| `11`, `35` | 10 | `5`, `12` | 7 |
| `16`, `40` | 8 | `4`, `8` | 4 |

Largest nonzero spreads through `n = 60`:

| ψ | rows as `n:φ(n)/2` | spread |
|---:|:---|---:|
| 20 | `25:10`, `50:10`, `57:18` | 8 |
| 14 | `39:12`, `52:12`, `55:20` | 8 |
| 18 | `19:9`, `27:9`, `38:9`, `51:16`, `54:9` | 7 |
| 10 | `11:5`, `22:5`, `35:12`, `45:12`, `48:8`, `56:12` | 7 |
| 12 | `13:6`, `26:6`, `33:10`, `44:10` | 4 |

So the row ψ ledger localizes the first planar crystallographic break, but it
does not preserve the trace-field degree. It quotients the problem through
"minimum crystallographic ambient rank" rather than through "native 2D trace
field."

## Support-level resolution of candidate #1

The phrase "ψ-stratified sweep-x-support" hides three different ledgers:

- **L1: row ψ ledger.** The sequence `(ψ(n))_{3 <= n <= N}`. This is a
  function of the row label alone. It sees no x-values.
- **L2: ψ-stratum support counts.** The number of support points `(n, k)` in
  each ψ stratum. This keeps row weights but not the actual x-values.
- **L3: exact support with ψ grading.** The full set `{(x_{n,k}, ψ(n))}`.
  This keeps the values themselves.

The verification script runs a rational-placeholder relabeling at `N = 15`:
each occupied x-cell is assigned a fresh rational placeholder while preserving
the collision partition. Output:

```text
occupied x-cells: 43
total support points (n,k): 117
collision signature preserved: True
L2 psi support counts unchanged: True
L3 exact support with psi grading changed: True
L2 counts by psi: 2:13, 4:35, 6:45, 10:11, 12:13
```

This is the support-level version of the driving impossibility. L1 is omitted
from the output because it ignores x-values by definition — it is trivially
invariant under any relabeling, including the placeholder. L2 is the
non-trivial invariance: rational placeholder values preserve the `(n, k)`
membership of each ψ stratum, so the stratum counts are unchanged even
though the cyclotomic content is gone. L3 escapes only because it retains
the x-values. But then ψ is a grading on a value-structured ledger; the
load-bearing invariant is the minimal-polynomial / Galois-orbit content of
the x-values, which points to candidates (3) and (4), not to ψ alone.

## Sensitivity criterion (intake filter)

A candidate ledger `L_N` passes the filter iff there exist two relabelings
of the sweep x-values — both preserving the collision pattern — that `L_N`
distinguishes. Length fails this trivially. More ambitiously, `L_N` should
be non-invariant under any relabeling that preserves `n mod 4` but changes
prime factorization.

## Items under search

Candidate replacement ledgers, ordered from closest-to-hand to
furthest-afield:

1. **ψ-stratified sweep-x-support.** ψ-classes of corner x-positions; ψ is
   additive on prime-power parts, so a ψ-stratified count retains the
   prime-factorization content that length discards. Already localizes the
   n=7 break in the existing repo figure.
   Anchor: [n-gons/counting/PSI-STRATIFICATION.md](n-gons/counting/PSI-STRATIFICATION.md).
   Update: this candidate resolves into L1 (row ψ) and L2 (ψ-stratum
   support counts), which inherit the driving impossibility by the ψ-fracture
   and placeholder tests above, and L3 (exact support with ψ grading), which
   survives sensitivity only by reducing to value-structure / Galois-orbit
   ledgers. ψ remains load-bearing only under the crystallographic-realization
   path in §"Compute-model / ledger coupling."

2. **Row-field-degree tally.** For each row n, the degree
   `[ℚ(cos(2π/n)) : ℚ] = φ(n)/2`. Sum, max, or weighted aggregate over
   `n ∈ [3, N]`. Directly arithmetic; may be too coarse (no position
   content).
   Update: located at `(P1, A1)` in the lattice. Gives a coarse,
   non-vacuous primitive-op lower bound on T1 and T3 via the
   row-entry argument — producing any row-n value forces entering
   `ℚ(cos(2π/n))`, so total work is at least `max_{n ≤ N} φ(n)/2` (the
   additive `Σ φ(n)/2` form is conservative; composita and field
   reuse make the sum hard to warrant without independence
   assumptions). Not matching/tight (no per-cell precision or
   root-isolation cost), but valid as a below-matching companion to
   `V_cert`.

3. **Value-structure at distinct x-cells.** For each occupied x-cell,
   record the minimal polynomial of the x-value over `ℚ`, an isolating
   interval / real-embedding index distinguishing Galois conjugates, the
   collision-cell incidence, and contributing `(n, k)` provenance.
   Update: degree-only and min-poly-only variants collapse — the
   algebraic-placeholder attack at matching degree multiset preserves
   the former, and distinct elements of the same trace field can share
   a parent min-poly while occupying distinct sweep positions (the
   structural pattern: `cos(π/7)`, `cos(3π/7)`, `cos(5π/7)` are
   Galois conjugates over `ℚ` with shared minimal polynomial
   `8x³ − 4x² − 4x + 1`, illustrating the form of conjugate-collapse
   the min-poly-only ledger inherits; sweep x-cells exhibit related
   collapses with their own min-polys, verified per-cell by Sage).
   Surviving form is `V_cert(N) = Σ_{cells C} (deg(P_C) + height(P_C)
   + root-isolation cost)` at lattice coordinate `(P3, A2)`, dominating
   `F2` and incomparable with `O_cert` — see §"Ledger lattice" below.

4. **Galois-orbit count.** Total count of Galois orbits of sweep x-values
   up to `n = N`. Invariant of the Galois action on the sweep, independent
   of cell-occupation combinatorics.
   Update: bare count sits at lattice coordinate `(P0, A0)` — same
   point as `|M_N|`, just from a different parent quotient (see
   §"Ledger lattice") — and inherits the strengthened impossibility by
   construction. The orbit-level placeholder replaces each Galois orbit
   `O_i` with a fresh algebraic conjugacy class of matching size from a
   different totally real field, preserving orbit count, sizes, and
   membership while changing field/conductor, min-polys, and heights.
   Surviving form is `O_cert(N) = Σ_orbits (field/conductor + P_O /
   height(P_O) + stabilizer + incidence-map costs)` at lattice
   coordinate `(orbit, A3)`. Incomparable with `V_cert` in the lattice
   (orbit-positional and cell-positional are different quotients,
   neither dominating the other); the comparison resolves only by task
   choice — orbit-level tasks pick `O_cert`, ordered-real-sweep tasks
   pick `V_cert` (per-cell root-isolation forces cell-positional
   granularity).

5. **Six-field decomposition as weighted ledger.** [n-gons/counting/COUNTING.md](n-gons/counting/COUNTING.md)
   §backbone identifies six fields governing word shape. A ledger
   weighted by field content (rather than flat word length) may recover
   cyclotomic sensitivity within the existing apparatus.
   Update: candidate splits into four variants under stress-test. F0
   (six-field counts only) and F1 (counts weighted by `φ(n)/2` or
   `ψ(n)`) are multidimensional scalar-summary variants — both inherit
   the working impossibility (per §"Driving impossibility") for
   cyclotomic-content tasks. F3 (full value-certified ledger per
   field) collapses onto `V_cert` at `(P3, A2)`, decorated with
   redundant field labels. F2 (six-field incidence ledger
   `(field, n, k → cell)`) is the genuine survivor at lattice
   coordinate `(P2, A0)` (see §"Ledger lattice"), incomparable with
   row-field-degree along the product order. F2's survival is
   task-coupled: dominates the typed-incidence-production task point
   `(P2, A0)` and serves as a cost ledger there; for any task
   demanding `A2` or higher, F2 fails and must promote to `V_cert`.
   Caveat: per [n-gons/counting/COUNTING.md](n-gons/counting/COUNTING.md), the six-field
   decomposition is verified through `N = 25` and conjectural beyond;
   F2's general applicability inherits this verification status.

6. **Champernowne-encoding height.** [n-gons/counting/PSEUDO-CHAMPERNOWNE.md](n-gons/counting/PSEUDO-CHAMPERNOWNE.md)
   connects `M_N` to a Champernowne-style encoding. Height of the encoded
   number may be a finer invariant than length.

## Ledger lattice

The items above do not order on a single chain. They occupy points in a
partial order along two axes — positional / incidence granularity and
depth of algebraic certification — with domination given by the product
order: ledger A dominates ledger B iff A retains at least as much
positional content as B *and* at least as much algebraic certification
as B. Where one has more on one axis and less on the other, the two
are incomparable; an earlier "structural tiers" chain framing forced
arbitrary tiebreaks that the lattice dissolves.

**P-axis (positional / incidence granularity).**

- `P0` — scalar summary. Count of equivalence classes after a quotient.
- `P1` — row-indexed. One value per row `n`, no per-corner content.
- `P2` — typed field-incidence. Per-cell with structural typing and
  row provenance `(n, k → cell)`.
- `P3` — exact cell / ordered embedding. Per-cell with full positional
  identity on the real line.

A separate orbit-positional dimension groups cells by Galois orbit.
Orbits are not a refinement of cells — they are a different quotient on
cells — so orbit-positional sits orthogonal to the `P0`–`P3` chain.

**A-axis (algebraic certification depth).**

- `A0` — none / structural typing only.
- `A1` — row-field degree, the abstract `[ℚ(cos(2π/n)) : ℚ] = φ(n)/2`.
- `A2` — value certificate per cell: minimal polynomial + height +
  isolating interval.
- `A3` — orbit certificate: field/conductor + Galois action /
  stabilizer + incidence map into the orbit.

**Inhabitants by coordinate.**

- `|M_N|` at `(P0, A0)`. Scalar count, no algebraic content. Bottom of
  every chain through the lattice.
- Item #4 in its naive form (bare orbit count) at `(P0, A0)` — same
  coordinate as `|M_N|`, just a different parent quotient.
- Item #2 (row-field-degree tally) at `(P1, A1)`. Per-row algebraic
  depth, no positional incidence.
- Item #5 surviving form (`F2`) at `(P2, A0)`. Typed positional
  incidence with row provenance, no algebraic certification.
- Item #3 surviving form (`V_cert`) at `(P3, A2)`. Exact ordered cell
  values with embedding certificates.
- Item #4 surviving form (`O_cert`) at `(orbit, A3)`. Orbit-positional
  granularity with full orbit certificate.

**Domination tests.**

- `V_cert` dominates `F2` (`P3 > P2`, `A2 > A0`).
- `V_cert` dominates row-field-degree (`P3 > P1`, `A2 > A1`).
- `F2` and row-field-degree are incomparable: `F2` has more `P`, less
  `A`; row-field-degree has more `A`, less `P`. Each can be
  placeholder-attacked along the axis it does not see.
- `V_cert` and `O_cert` are incomparable on the positional axis
  (cell-positional vs orbit-positional are different quotients,
  neither refining the other). The comparison resolves only when a
  task fixes the positional axis it requires.
- `|M_N|` is dominated by every other inhabitant.

**Predictive principle (generalized).** A task demands a lattice
coordinate `(P_t, A_t)`. Passing ledgers are those that dominate
`(P_t, A_t)` in the product order. Any ledger not dominating the
demanded point fails: the placeholder attack at the missing axis
defeats it. The earlier "scalar-summary tier inherits impossibility a
priori" is the special case where any non-trivial cyclotomic-content
task demands strictly more than `(P0, A0)`, so any `(P0, A0)` ledger
fails by construction. The lattice gives the full version:
non-domination on either axis is sufficient for failure.

**Lower bounds, domination, and matching.** A ledger gives a
non-vacuous lower bound on a task when its accounting reflects
unavoidable work for any process completing the task. There are three
regimes relative to the task's matching coordinate `(P_t, A_t)`:

- **At matching.** The ledger's accounting tightly reflects the task's
  unavoidable work; the lower bound is matching / tight. Search
  target.
- **Below matching.** The ledger captures *some* unavoidable work but
  not all of it; the lower bound is non-vacuous but loose. Example:
  row-field-degree at `(P1, A1)` gives at least `max_{n ≤ N} φ(n)/2`
  as a coarse lower bound on T1 — any process producing a row-n value
  must enter `ℚ(cos(2π/n))`, so the work is at least the maximum
  row-field degree across rows touched. (The additive `Σ φ(n)/2` form
  is conservative under independence assumptions, but composita and
  field reuse make the sum harder to warrant without an additional
  argument.) Real bound, but doesn't reflect per-cell precision or
  root-isolation cost.
- **Above matching.** The ledger captures work the task doesn't
  strictly require; the bound it produces is a lower bound on a
  *stronger* task (one that needs the ledger's full content), not on
  the original task. Example: `V_cert` dominates T2's matching
  coordinate in the lattice but cannot lower-bound T2 — T2's
  combinatorial output does not require V_cert's algebraic content;
  T2's matching ledger is `F2`.

Matching ledgers are the search target. Below-matching ledgers exist
as fallback / coarse companion bounds. Above-matching ledgers are
pointing at a different (stronger) task, not at T itself.

**Matching is a structural prediction, not yet a proven matching.**
The lattice apparatus organizes domination structurally; the
"matching" judgement at any specific `(P_t, A_t)` rests on two further
claims that are not themselves established here: (a) the strengthened
driving impossibility (currently *working form, not proved*), which
the placeholder attack at the missing axis depends on, and (b) a
primitive-op cost theorem connecting the ledger's components (e.g.,
min-poly degree, height, root-isolation cost in `V_cert`) to actual
primitive-operation count in the chosen compute model. The memo's
matching language presumes both; neither is yet in hand. "Matching"
should be read as best-current-candidate-for-matching pending those
two pieces.

**Coupling to compute-model / task choice.** The Path 1 / Path 2 split
becomes a choice of demanded lattice coordinate. Path 1
(crystallographic-realization) demands orbit-positional with an `A3`
certificate (`O_cert`-shaped). Path 2 (trace-computation) demands
`(P3, A2)` (`V_cert`-shaped). `F2` sits on a Path-1-flavored task
track of its own — typed-incidence-production demands `(P2, A0)`,
which `F2` dominates. The same ledger can pass under one task and
fail under another depending on which lattice point the task demands.

**Item #6 (Champernowne height) location.** Not yet placed; a strong
candidate for `(P0, A0)`, in which case it inherits the impossibility
a priori. Worth stress-testing under that hypothesis.

## Compute-model / ledger coupling

Ledger choice is not independent of compute-model choice. There are now two
different paths, and they should not be collapsed. **Path 1** is a
crystallographic-realization task: ψ is the ledger, and the machine model is a
rank/lattice model that charges crystallographic realization. **Path 2** is a
trace-computation task: the ledger is value-structure, row-field degree, or
Galois orbit data, and the machine model is algebraic arithmetic over `Q` or an
algebraic straight-line program. Both are legitimate Landfall-parallel
ambitions; they would prove different theorems.

Under Path 1 the explicit ψ-ledgers are:

```text
Ψ_max(N) = max_{3 <= n <= N} ψ(n)
Ψ_sum(N) = sum_{3 <= n <= N} ψ(n)
Ψ_wit(N) = sum over charged witnesses (n,k) of ψ(n).
```

`Ψ_max` is the ambient lattice rank needed for one shared realization machine
handling every row through `N`; `Ψ_sum` is row-wise certificate capacity;
`Ψ_wit` is a witness-weighted aggregate for a distinguishing task.

These are capacity / certificate-size lower bounds before they are primitive-op
lower bounds. A Path 1 compute model must explicitly charge rank allocation,
integer-matrix construction, or certificate production as primitive operations
before a ψ-ledger becomes a Landfall-style compute-cost theorem. Under Path 2
the rank-allocation form of the caveat disappears (algebraic arithmetic
charges field adjunctions and ring operations natively), but a separate cost
theorem connecting `V_cert` components — minimum polynomial degree, height,
root-isolation cost — to primitive-operation count is still required. The
natural Path 2 ledgers are trace degree, minimum-polynomial degree, and
Galois-orbit structure, but their primitive-op tightness depends on that
pending theorem.

**`O_cert` is a sibling track, not a Path 1 sub-case.** Path 1 was originally
named for the crystallographic-realization task with ψ-ledger and rank/lattice
machine model. The `O_cert` ledger surfaced during candidate #4's stress-test
defines a *separate* non-trace-computation track — orbit-realization with
per-orbit field/poly/action/incidence certificates — with its own compute
model. Both Path 1 (ψ-rank) and the `O_cert` track are sibling alternatives
to Path 2 (V_cert + algebraic-arithmetic), but they are not the same ledger.
Earlier text that tagged `O_cert` as "Path 1" should be read as "Path-1-
flavored sibling track."

## Task-ledger admissibility

With the lattice in hand, each candidate task statement in
`memos/COUNTING-APPARATUS.md` §(B) admits a comparison against the
inhabited ledger points. Result of that comparison:

| Task | `V_cert` `(P3, A2)` | `O_cert` `(orbit, A3)` | `F2` `(P2, A0)` | row-deg `(P1, A1)` |
|------|:-------------------:|:----------------------:|:---------------:|:------------------:|
| T1 (enumerate corner positions to `10⁻ᵏ`) | matching | no¹ | no values | coarse⁴ |
| T2 (compute `M_N`) | overkill² | no | matching³ | no word structure |
| T3 (distinguish round-trace pairs at `ε`) | matching | no¹ | no values | coarse⁴ |

¹ Only under reformulation to an orbit-level task; for real-line
distinction, `O_cert` must add per-cell embedding and collapses to
`V_cert`.

² `V_cert` dominates T2's matching coordinate but cannot lower-bound
T2 non-vacuously: T2's combinatorial output doesn't require V_cert's
algebraic content, so the ledger is "above" the task. See §"Ledger
lattice" — lower bounds, domination, and matching.

³ `F2` serves a strengthened "produce typed incidence / six-field
derivation of `M_N`" task, not the literal "output `M_N`" task.

⁴ Coarse but non-vacuous: producing any row-n value forces entering
`ℚ(cos(2π/n))`, so total work is at least `max_{n ≤ N} φ(n)/2` (the
additive `Σ φ(n)/2` form is conservative but depends on independence
assumptions that composita and field reuse make model-dependent).
Below-matching, doesn't reflect per-cell precision or root-isolation
cost, but valid as a fallback / sanity-check bound alongside
`V_cert`.

**Viable task-ledger pairings.**

- **T1 + `V_cert` + algebraic-arithmetic over ℚ.** Per-corner ordered
  enumeration with algebraic precision cost. Matching. Landfall-
  parallel.
- **T3 + `V_cert` + algebraic-arithmetic over ℚ.** Real-valued
  distinction at precision. Matching. Landfall-parallel.
- **T2 + `F2` + word-structure compute model.** Honest combinatorial
  theorem, not the original cyclotomic-depth ambition.
- **T_orbit (reformulated) + `O_cert` + lattice/rank model.** Path 1.
- **T_capacity + row-field-degree + algebraic-arithmetic.** Row-level
  capacity theorem; coarse / loose.
- **(Coarse companion.) Row-field-degree on T1 / T3.** Below-matching
  fallback giving at least `max_{n ≤ N} φ(n)/2` (or sum, modulo
  composita / field-reuse independence) as a non-vacuous primitive-op
  lower bound on T1 and T3 directly. Useful as a sanity-check or
  coarse-bound companion to `V_cert`, surfaced during Q8's calibration
  attempt.

**First exit-(a) candidate for the search.** T1 or T3 (or both,
sharing `V_cert` and the same compute model) is the cleanest
committable triple if the program holds to the original
Landfall-parallel ambition. The compute-model / ledger pair is a
single commitment: algebraic-arithmetic over ℚ (or ASLP) charging
field adjunctions and ring operations, with `V_cert` as the cost
ledger.

T2 + `F2` is the alternative theorem available without further
search, at the cost of moving the program's stated ambition from
"primitive-op lower bound on cyclotomic-depth content" to "primitive-
op lower bound on typed-incidence production." Different theorem,
legitimate, but not the original target.

## Adjacent anchors

- [memos/COUNTING-APPARATUS.md](memos/COUNTING-APPARATUS.md) — parent
  search doc; §(A) compute model, §(B) task statement, §(C) portrait of τ,
  §(D) n=7 walkthrough (the finding that opens this memo).
- [n-gons/counting/PSI-STRATIFICATION.md](n-gons/counting/PSI-STRATIFICATION.md) — candidate #1 anchor.
- [n-gons/counting/COUNTING.md](n-gons/counting/COUNTING.md) — the counting
  apparatus; six-field decomposition.
- [n-gons/counting/PSEUDO-CHAMPERNOWNE.md](n-gons/counting/PSEUDO-CHAMPERNOWNE.md) — candidate #6 anchor.
- [n-gons/counting/verify_increment_formula.py](n-gons/counting/verify_increment_formula.py) — verifies the
  closed-form Δ|M_n| recurrence through n = 40.
- [n-gons/counting/verify_psi_fracture.py](n-gons/counting/verify_psi_fracture.py) —
  verifies the ψ-fracture exhibit and the support-level placeholder test.
- [memos/FORTNOW-KOLMOGOROV-BRIEF.md](memos/FORTNOW-KOLMOGOROV-BRIEF.md) —
  generate-vs-distinguish framing, relevant once a passing candidate meets
  §(B).

## What this memo is not

- **Not a proof of the driving impossibility.** The generic-rational
  placeholder construction needs explicit formalization before it becomes
  a lemma.
- **Not a compute-cost lower-bound proof.** Task + machine-model pairings
  are now proposed at §"Task-ledger admissibility" as the search's first
  exit-(a) candidate, but the proofs that those pairings deliver
  primitive-op lower bounds — the placeholder construction promoted from
  working form to theorem, plus a cost theorem connecting ledger
  components to primitive ops — remain to be done.
- **Not a commitment that a replacement ledger exists.** Exit criterion
  (b) contemplates the branch closing negative.

## Exit criteria

- **(a) Pass.** One candidate ledger passes the sensitivity criterion,
  admits a compute-model formulation, and hands off to `COUNTING-APPARATUS
  §(A)`. The memo closes; content promotes or cross-links.
- **(b) Fail.** All candidates under search fail the sensitivity criterion
  (or their apparent passes resolve to length-equivalents under closer
  reading). The compute-cost branch in `COUNTING-APPARATUS` closes negative
  with the driving impossibility promoted to a lemma statement.

Append below as items get worked through.
