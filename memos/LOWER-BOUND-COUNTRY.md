# LOWER-BOUND-COUNTRY

A search memo on the complexity-theoretic literature that `memos/RAMANUJANS-COMPLIMENT.md` §"When to leave" pre-announces as the next reading queue — the literature where compute-cost *lower* bounds actually live — and on what a lower-bound-with-shape for the circle-side program in `memos/COUNTING-APPARATUS.md` would have to look like. This is the symmetric partner to the Ramanujan memo: where that one scouts upper-bound benchmarks and pre-theoretical faith, this one scouts the machinery that turns a conjectured lower bound into a statement and the traps that keep it from being one.

The country here is **algebraic complexity theory** (Strassen, Baur–Strassen, degree bound, arithmetic circuits / straight-line programs) and **real computation** (Blum–Shub–Smale machine, algebraic computation trees). It is technical, it is less glamorous than Ramanujan's territory, and it is where the program's actual load-bearing question lives.

---

## Why this country, precisely

What upper-bound sources (Chudnovsky 1988 on π, Bresenham-midpoint on lattice-resolution circles, Bidder/Mitchell on log-side) cannot supply:

1. **A primitive-op floor.** Upper bounds prove something *can* be done. Lower bounds prove nothing *better* can be done. `memos/COUNTING-APPARATUS.md` wants the second kind of statement. No upper-bound literature, however rich, produces one.
2. **A compute-model commitment with teeth.** Item (A) of `memos/COUNTING-APPARATUS.md` currently lists candidates (ruler-and-compass, algebraic-arithmetic over ℚ, algebraic straight-line programs, Gosper-style Möbius transducer). The lower-bound literature is where those names stop being candidates and start being objects with proof technology attached.
3. **A vocabulary for "the bound is vacuous."** Much of the work in algebraic complexity is proving that a seemingly-natural lower bound fails in a specific sense (restricted-depth, multilinear-only, non-uniform, natural-proofs-barrier-limited). The program needs to know, before committing, whether the bind it wants belongs to a regime where lower bounds are reachable or to one where known techniques are known not to reach.

Ramanujan supplies the upper-bound benchmark and the belief that the circle is navigable. Bresenham-midpoint supplies an existence-proof integer-arithmetic procedure. Neither supplies the floor. This memo scouts where the floor could come from.

---

## Specific questions we bring

Each tied to a named item in `memos/COUNTING-APPARATUS.md`.

### On item (A) — which compute model admits a floor

- Which of {BSS real-computation machine, algebraic straight-line program over ℤ, algebraic straight-line program over ℚ, algebraic computation tree} admits a proof technique whose target shape is "`Ω(g(N))` primitive ops to approximate the circle at lattice resolution `N`"? The candidate techniques — **Strassen's degree bound** (multiplicative complexity via geometric degree of the associated rational map), **Baur–Strassen** (derivatives are free), **Ben-Or's topological method** (log of connected components / Betti numbers of a semialgebraic set bounds algebraic-computation-tree height) — each live in a specific model. The question is which model carries the bound the program wants to state.
- Does the BSS model (Blum, Cucker, Shub, Smale 1998, *Complexity and Real Computation*, Springer) have a chapter whose machinery directly attaches to circle approximation? The textbook has a "Deterministic Lower Bounds" chapter using connected-components counts — Ben-Or-style — on semialgebraic decision problems. Circle approximation is not, at first read, a decision problem on a semialgebraic set, but there may be a decision-problem reformulation (e.g., "is this pixel on the Bresenham trace?") that fits.

### On item (B) — whether the task statement can be cost-lower-bounded

- `memos/COUNTING-APPARATUS.md` T1/T3 (enumerate corner positions at resolution `10^{-k}`; produce a distinguishing witness at every mismatched pair). T3 is a decision problem and therefore fits the Ben-Or / BSS semialgebraic-decision framework *if* the decision surface has enough topological complexity (high `b_0` or high Betti numbers) to force `Ω(log b_m(Σ)/(m+1))` tree depth. Does it? This is the first concrete question to attempt.
- The degree bound (Strassen) produces `Ω(log deg)` lower bounds on multiplicative complexity. The "degree" of the computation required to emit `M_N` is, loosely, the product of cyclotomic-extension degrees `∏φ(n)/2` for `n ∈ [3, N]`. Does this plug in? Probably not directly — the degree bound counts multiplications in a single rational function, not arithmetic to emit a sequence — but the moral analog is visible.

### On item (C) — algebraic-depth statement with a proof technology attached

- The τ-portrait wants to say: "no finite algebraic structure reaches τ." Algebraic-complexity-theoretic analog: the lower-envelope of the algebraic-circuit complexity of the sequence of minimal polynomials of 2cos(2π/n) grows with `n`. Is there a published result of that shape, or is it a gap?
- **Kaltofen's straight-line-program factorization** (Kaltofen 1989, "Factorization of polynomials given by straight-line programs," in *Randomness and Computation*) is a closure result for arithmetic-circuit representations. Its dual — a lower bound on the SLP-size of cyclotomic polynomials — is presumably available or known-open.

### On item (D) — can a small-case walkthrough at `n = 7` illustrate an asymptotic bound

- Asymptotic lower bounds do not specialize to single points. A small-case walkthrough at `n = 7` is illustrative only; the memo should not expect it to produce a numerical `Ω`-bound. What it *can* produce: an instance where the three cost measures (ruler-and-compass ∞, algebraic-arithmetic poly(3)·log(1/ε), Bresenham-midpoint `O(N)` ints) separate cleanly, visible in a plot. Is there a known lower-bound technique that explains the separation, at `n = 7` specifically, via cubic-extension degree?

---

## What specifically to read

In rough priority for this search. Each entry is a full citation so the reader can search independently.

### Core texts

1. **Blum, Cucker, Shub, Smale 1998.** *Complexity and Real Computation*, Springer. The BSS-machine book, foreword by Richard Karp. Has a dedicated "Deterministic Lower Bounds" chapter. First read.
2. **Bürgisser, Clausen, Shokrollahi 1997** (with Thomas Lickteig). *Algebraic Complexity Theory*, Grundlehren der mathematischen Wissenschaften **315**, Springer. The textbook. ~600 pages, ~500-paper bibliography. Chapters 7–9 (multiplicative complexity, additive complexity, degree bound) are the core for this program. Read targeted, not cover-to-cover.
3. **Shpilka & Yehudayoff 2010.** "Arithmetic Circuits: A Survey of Recent Results and Open Questions," *Foundations and Trends in Theoretical Computer Science* **5**(3–4), 207–388. The modern survey. If the program's bound shape is arithmetic-circuit-flavored, this is the entry point.
4. **Brent & Zimmermann 2010.** *Modern Computer Arithmetic*, Cambridge Monographs on Applied and Computational Mathematics **18**, Cambridge University Press. Already flagged in `memos/RAMANUJANS-COMPLIMENT.md` — the bridge between upper-bound rates and the lower-bound register. Chapter 4 (function evaluation via AGM, binary splitting, Newton's method) is the specific section where upper-bound rates meet any existing lower-bound discussion.

### Foundational papers

5. **Strassen 1973.** "Die Berechnungskomplexität von elementarsymmetrischen Funktionen und von Interpolationskoeffizienten," *Numerische Mathematik* **20**(3), 238–251. The original degree bound.
6. **Baur & Strassen 1983.** "The complexity of partial derivatives," *Theoretical Computer Science* **22**(3), 317–330. The `Ω(n log n)` lower bound for algebraic branching programs evaluating polynomials with all partial derivatives simultaneously. Model result for how to extract a non-trivial arithmetic-circuit lower bound.
7. **Ben-Or 1983.** "Lower bounds for algebraic computation trees," *Proceedings of the 15th Annual ACM Symposium on Theory of Computing* (STOC '83), 80–86. The topological method: `c_1 log b_0(Σ) − c_2 n` lower bound on tree height, where `b_0(Σ)` is the number of connected components of the semialgebraic set `Σ`. Later extended by Yao (1992) and others to higher Betti numbers.
8. **Kaltofen 1989.** "Factorization of polynomials given by straight-line programs," in Micali (ed.), *Randomness and Computation*, Advances in Computing Research **5**, JAI Press, 375–412. The closure-under-factorization result; entry point to Kaltofen's sequence of straight-line-program complexity papers.

### Barrier literature (so the program knows where not to push)

9. **Razborov & Rudich 1997.** "Natural proofs," *Journal of Computer and System Sciences* **55**(1), 24–35. The natural-proofs barrier. Boolean-circuit-flavored but has algebraic analogs. Relevant if the program's bound shape starts to look "natural" and "large" in the Razborov–Rudich sense.
10. **Mulmuley's GCT program**, surveyed in Mulmuley 2012, "The GCT program toward the P vs. NP problem," *Communications of the ACM* **55**(6), 98–107. The 100-year program. Probably not load-bearing for the circle-side bind — and Mulmuley's own timeline estimate is a realism check — but should be known-of before expecting a fast lower-bound proof in the general algebraic setting.

### Survey / orientation

11. **von zur Gathen 1988.** "Algebraic complexity theory," *Annual Review of Computer Science* **3**, 317–348. Older than Bürgisser–Clausen–Shokrollahi but more compact; useful first-orientation read.
12. **Lokam 2009.** "Complexity Lower Bounds using Linear Algebra," *Foundations and Trends in Theoretical Computer Science* **4**(1–2). Linear-algebraic techniques for lower bounds. Complementary to the algebraic-geometric techniques.

**Not yet read, flagged for completeness:**

- **von zur Gathen 1988** on arithmetic networks (Springer *AAECC* 1991) for a compute-model closer to ruler-and-compass-plus-integer-arithmetic.
- Mulmuley's **"GCT V"** and subsequent papers if and only if the bind somehow touches VP vs VNP. Not expected.

If any of the above turns up nothing load-bearing in a directed read, note it in this memo and move on. The exit discipline matters here too.

---

## Pairing

Three neighboring literatures that supplement the algebraic-complexity core without being the core:

- **Real algebraic geometry / semialgebraic topology.** Basu, Pollack, Roy 2006, *Algorithms in Real Algebraic Geometry*, Springer. The topology tools (Betti numbers, connected components) that Ben-Or and its descendants use are from here. If the lower-bound argument ends up running through `b_m(Σ)` counts, this is where the counts come from.
- **Information-based complexity (IBC).** Traub, Wasilkowski, Woźniakowski 1988, *Information-Based Complexity*, Academic Press. IBC proves lower bounds for continuous problems (approximating a real-valued functional given partial information) in a compute model where the primitive op is a query to an oracle. The circle-approximation problem has an IBC flavor when recast as "given query access to 2cos(2π/n), produce a rational approximation." Probably not load-bearing, but known-of.
- **Transcendence theory, as a lower-bound source.** `memos/LINDEMANN-BRIEF.md` already flags the circularity map for using Lindemann–Weierstrass inside a compute-cost argument. Baker's theorem on linear forms in logarithms of algebraic numbers (Baker 1966, *Mathematika* **13**) sits adjacent: it produces effective lower bounds on `|α_1 log β_1 + … + α_n log β_n|` for algebraic `α_i, β_i`, which is exactly the shape of "how well can you approximate a transcendental circle point by an algebraic-depth-`d` surrogate" when recast as a diophantine-approximation question. Noting this here without pursuing: `memos/BIDDER-AND-SON.md` §"Open question" already flags Baker as the transcendence-theory backdrop for the son's nine-element closure question, and the circle-side analog may be available.

---

## Hazards (why this country has traps of its own)

Three failure modes worth naming in advance, so a directed read can detect them:

1. **The bound lands in a restricted circuit class.** Most published arithmetic-circuit lower bounds are for restricted models (constant-depth, multilinear, non-commutative, monotone). A lower bound in a restricted class does not imply a lower bound in the unrestricted class the program actually wants. If a candidate result comes up, the first question is: which restriction?
2. **The bound is tight only up to a polynomial factor.** The lower-bound literature frequently produces bounds of the form `Ω(n log n)` vs. a known upper bound of `O(n² log n)`. A poly-separating bound is informative if the task genuinely requires super-polynomial work, but for the circle-side bind — where `|M_N|` appears linearly-ish in `N` — a log-factor separation may be all that's available, and may not be the shape the program wants.
3. **The bound requires a conjecture.** Many modern arithmetic-circuit lower bounds are conditional on conjectures in algebraic complexity (e.g., the permanent is hard; VP ≠ VNP). Conditional bounds are still useful — they locate the bind in a known-hard region — but the program should not accept one as final without naming the conditioning assumption.

A directed read should close with a sentence of the form *"This produces a bound of shape X in model Y under assumption Z,"* with all three named. The analog of the Ramanujan-memo discipline ("this bounds the compute cost of τ at …"), on the other side.

---

## Adjacent anchors

- `memos/RAMANUJANS-COMPLIMENT.md` — the upper-bound partner. This memo's reading list is the explicit continuation of that memo's §"What to read instead, when exit triggers."
- `memos/COUNTING-APPARATUS.md` — the parent search; all four items (A)–(D) are where any lower-bound result has to land to be load-bearing.
- `memos/BRESENHAM-MIDPOINT.md` — the integer-arithmetic upper-bound witness. Any lower bound this memo finds has to be at least as strong as Bresenham-midpoint's `O(R)` integer-op rate, or the bind gets pinned.
- `memos/LINDEMANN-BRIEF.md` — transcendence-theoretic circularity map. Baker's theorem sits adjacent to this memo and is the one transcendence-theoretic tool that doubles as a diophantine lower-bound source.
- `memos/BIDDER-AND-SON.md` §"Open question" — the log-side Baker-closure question this memo might end up dual-using on the circle side.

---

## What this memo is not

- **Not a complexity-theory textbook.** The citations are entry points, not pedagogy. A reader who needs the field from scratch starts with Shpilka–Yehudayoff 2010 (survey) or Bürgisser–Clausen–Shokrollahi 1997 (textbook), not this memo.
- **Not a claim that a lower bound is near.** The most honest prior on the circle-side compute-cost bind is that no existing technique proves it, and it will have to be constructed rather than found. This memo scopes the territory; it does not promise a theorem.
- **Not a detour into P vs NP.** The circle-side program has nothing to do with P vs NP and should not try to acquire a relationship with it. Mulmuley's GCT program is cited for context and realism, not as a model for the work.
- **Not a replacement for upper-bound work.** Upper bounds (Ramanujan, Bresenham-midpoint) stay load-bearing. A lower bound without a matched upper bound is half a statement.

---

## Exit criteria

The memo freezes and its content migrates when *any one* of the following triggers:

1. **Compute model committed with bound-technology attached.** Item (A) of `memos/COUNTING-APPARATUS.md` commits to a specific compute model (probably BSS or ASLP) *and* to a specific proof technique from this memo's reading list that plausibly produces a matching bound. When the commit happens, this memo freezes as historical record.
2. **Task statement admits a known technique.** Item (B)'s T1 or T3 gets reformulated in a way that plugs into Ben-Or / Strassen / Baur–Strassen directly, with a concrete bound (even a weak one) derived. Promote the derivation to `memos/COUNTING-APPARATUS.md` §(B).
3. **"Known techniques do not reach this" with citation.** A directed read establishes that the bind the program wants lies outside the reach of existing lower-bound technology (for example, the Razborov–Rudich barrier applies, or all known bounds are restricted-depth-only and the bind requires unrestricted depth). This is itself a finding; note it in `memos/COUNTING-APPARATUS.md` §(A) and consider weakening the compute model to one where bounds exist.
4. **Two directed reads without a load-bearing take-away.** Same discipline as `memos/RAMANUJANS-COMPLIMENT.md`: if two reads from the list above close without a sentence of the form "this bounds the compute cost of τ at …" or "this constrains the compute cost by ruling out …," note both in this memo and demote it to low-priority.

---

## Status

Open search memo. No directed reads completed. The reading queue above is the active queue; BSS 1998 (Blum–Cucker–Shub–Smale) and Shpilka–Yehudayoff 2010 are the two first-cuts — the first for compute-model grounding, the second for modern technique orientation. Ben-Or 1983 is the first short paper, and cheap to read; the question there is whether a circle-approximation task can be cast as a semialgebraic decision problem with enough topology to bite.
