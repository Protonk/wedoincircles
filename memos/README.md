# memos

Promoted internal references for the program. Source-extraction briefs, cross-source syntheses, program-level notes, concrete worked tests, and active search memos all live here. Conventions for the three written patterns used in this directory — `-BRIEF` source extractions, search memos, general cross-source syntheses — are in `memos/AGENTS.md`.

Each entry below is a short bestiary with its role. Full content is in the linked file.

---

## Program-level references

### LANDFALL-EXPORT

The log-side program reference. Foundational write-up of the floating-point residue ε(m) = log₂(1+m) − m, the six-wall structure that forces a compute-cost lower bound, Mitchell's pseudo-log L = E + m as the equivariant surrogate, and the program-facing exports (β arithmetic type, Gosper's CF machine, the Padé wall at §4) that other memos build on.

→ `memos/LANDFALL-EXPORT.md`

### BIDDER-AND-SON

Two notes in one. Part I records the mental-arithmetic procedures by which G. P. Bidder (1806–1878) and his son G. P. Bidder Jr. computed log₁₀(n) to seven or eight decimal places mentally. Part II is the bridge to *Landfall*: the father's method is structurally CREATI (catalog), the son's is structurally PERMEATE (saturation), and the residue ε both have to navigate around is the same one IEEE rounding has to live with. Closes with the BIND-shaped open question about exact reachability from the son's nine-constant set.

→ `memos/BIDDER-AND-SON.md`

### CONTINUED-FRACTIONS-CROSSWALK

A cross-source synthesis on continued-fraction convergents as a recurring primitive across four independent memos — spectral (10-MARTINIS), combinatorial (3DT), algorithmic (Lefèvre–Muller via 3DT), and computational (LANDFALL-EXPORT via Gosper). Not a source brief; a read-across.

→ `memos/CONTINUED-FRACTIONS-CROSSWALK.md`

### MIZAR-NIVEN-FOREBODING

A future-facing anchor on Korniłowicz & Naumowicz's 2016 formalization of Niven's theorem in Mizar. Not active program material; parked for the moment a formally-verified Chebyshev / monic-ℤ / rational-root chain becomes necessary.

→ `memos/MIZAR-NIVEN-FOREBODING.md`

---

## Source-extraction briefs

Each brief is the repo's extracted reading of a specific paper stashed under `sources/` (gitignored). The writing standard is in `memos/AGENTS.md` §"Source extraction memos".

### 10-MARTINIS-BRIEF

Avila–Jitomirskaya's *Ten Martini Problem* result. Spectral analysis of the almost-Mathieu operator. The arithmetic parameter β(α) = limsup (ln q_{n+1}) / q_n classifies α as Diophantine vs. Liouville; the proof splits parameter space by β.

→ `memos/10-MARTINIS-BRIEF.md`

### 3DT-BRIEF

The Three-Distance Theorem: the gap structure of an α-rotation orbit on ℝ/ℤ partitions the circle into at most three distinct gap lengths. Three proofs are present: Berthé–Reutenauer's combinatorial, Lefèvre–Muller's algorithmic (Table Maker's Dilemma §2.2.1), Marklof–Strömbergsson's lattice-geometric on `Γ\SL(2, ℝ)`.

→ `memos/3DT-BRIEF.md`

### LINDEMANN-BRIEF

Classical transcendence of π (Lindemann 1882) and its Weierstrass-1885 generalization (Lindemann–Weierstrass). Plus a circularity map for when invoking Lindemann–Weierstrass in the compute-cost argument is safe, programmatically weak, or strictly circular. The program's target would uphold Lindemann–Weierstrass for e and π, so using it as a tool needs explicit care.

→ `memos/LINDEMANN-BRIEF.md`

### FORTNOW-KOLMOGOROV-BRIEF

Lance Fortnow's 14-page Kaikoura tutorial on Kolmogorov complexity. Plain `C` and prefix-free `K`; pairing bounds and symmetry of information; Kraft's inequality and the universal semicomputable measure `μ(x) = 2^{-K(x)}` with its dominance fact and worst-case-equals-average-case theorem; time-bounded `C^t` and the distinguishing variant `CD^t` (with the unique-SAT / P-vs-NP-flavored equivalence); size-of-set bounds via hashing including Sipser's theorem and Valiant–Vazirani.

→ `memos/FORTNOW-KOLMOGOROV-BRIEF.md`

---

## Active search memos

Scaffolding for uncertain program ambitions that aren't yet theorem-shaped. Each tracks a specific search with exit criteria; content promotes outward when exit triggers. Convention documented in `memos/AGENTS.md` §"Search memos".

### COUNTING-APPARATUS

The program's most uncertain ambition: binding the counting apparatus (`n-gons/counting/`) to the circle-side equivariant surrogate. If that bind closes, `M_N` becomes a compute-cost ledger paralleling *Landfall*'s log-side result; if it does not, the branch remains a descriptive counting portrait of circle-side structure. Four prerequisites laid out: (A) compute model, (B) task that makes counting the natural ledger, (C) portrait of τ, (D) small-case walkthrough at n = 7.

→ `memos/COUNTING-APPARATUS.md`

### RAMANUJANS-COMPLIMENT

What Ramanujan's corpus contributes to the compute-cost search — pre-theoretical faith, method-sibling validation, upper-bound benchmarks (Ramanujan–Chudnovsky–Borwein), algebraic-depth terrain — and, the harder half, when to leave his realm for the lower-bound literature. Paired with Gauss (compute-model theorist) and Archimedes (the squeeze).

→ `memos/RAMANUJANS-COMPLIMENT.md`

### KRAFT-HERMITE-LINDEMANN-AITCHISON

A search on whether effective Hermite–Lindemann at `n = 1` — transcendence of π with an effective irrationality measure — can be reproduced as a pure Kraft argument on the circle, using Aitchison 1959's density-side Fourier bound and the Erdős–Turán–Koksma discrepancy-sum inequality as a joint Kraft–Parseval budget, and Hurwitz 1902's Fourier-analytic isoperimetric identity as Dido's native variational certificate for π. Target deliverable is a pre-L–W proof structure with an effective `|qπ − p| ≫ q^{-C}` constant extractable from the budget. Four items under search (A Kraft–Parseval budget / B Hurwitz–Dido extremum / C auxiliary-free Hermite replacement / D effective rate + L–W-safety audit), with explicit hazards around circularity and pedagogical-collapse cases.

→ `memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md`

---

## On adding a memo

- **Source-facing extraction of a specific paper:** use the `-BRIEF` suffix and follow `memos/AGENTS.md` §"Source extraction memos".
- **Cross-source synthesis or program-level reference:** no suffix convention; lead with scope and audience.
- **Search memo for an open ambition:** follow the pattern in `memos/AGENTS.md` §"Search memos" — target, items under search, adjacent anchors, what-this-is-not, exit criteria.
- **Note that outgrows source-facing extraction into reusable internal reference:** drop the `-BRIEF` suffix or promote out of `memos/` into the home that actually owns it (`BNHA/triad/...`).
