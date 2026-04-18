# RAMANUJANS-COMPLIMENT

A search memo on what Ramanujan's work contributes to the compute-cost bind ambition laid out in `memos/COUNTING-APPARATUS.md`, and — the harder-to-write half — when to stop reading him and leave for lower-bound territory.

The "compliment" in the title reads two ways, both useful: what Ramanujan's work says in appreciation of the circle (he believed the circle was algebraically navigable long before justification caught up), and what it completes for the program (filling the belief-gap the counting-apparatus search currently has). The memo is organized so neither reading becomes a trap.

---

## Why Ramanujan, precisely

`memos/BIDDER-AND-SON.md` gave Landfall three things, underneath the biographical color:

1. **Pre-theoretical faith** that the residue could be navigated on a bounded substrate.
2. **Method-sibling validation** — father/son methods instantiate CREATI (catalog) and PERMEATE (saturation) on the log side.
3. **An implicit BIND question** — what reals are exactly reachable from the son's constant set.

Ramanujan gives the same three, plus a fourth Bidder's log side didn't have:

4. **Upper-bound benchmarks.** Rapid-convergence series for π (Ramanujan 1914, Chudnovsky 1988, Borwein–Bailey descendants) give numerical rates against which any claimed compute-cost lower bound is evaluated. A lower bound embarrassingly looser than Chudnovsky's ~14 digits per term would be uninformative; a lower bound comparable-to-or-tighter would be load-bearing.

Where Bidder had to be translated into the modern compute-in-a-bounded-register register, Ramanujan's corpus is already in the algebraic-cyclotomic-modular register the circle-side catalog uses. The vocabulary matches.

5. Ramanujan and Hardy are linked and I like Hardy.

---

## Specific questions we bring

Not "read Ramanujan." That is a rabbit hole and the memo later argues explicitly against it. Targeted questions only, each tied to a specific item in `memos/COUNTING-APPARATUS.md`:

### On upper-bound benchmarks (feeds item D)

- What is Chudnovsky's compute cost per digit of π in algebraic-arithmetic-over-ℚ primitive ops? What compute model does their rate implicitly assume?
- What is the upper-bound compute rate for cos(π/n) to precision ε via Ramanujan-Sato–style CM-point constructions, as a function of n and ε?
- Do the Borwein–Bailey–Plouffe (BBP) formulas give a different compute-model answer than Chudnovsky?

### On the algebraic-depth portrait (feeds item C)

- Singular moduli at CM points τ = i√d produce algebraic numbers whose degree is controlled by the class number of ℚ(√−d). Does this illuminate the algebraic-depth growth of τ(n) = 2cos(2π/n) − round(2cos(2π/n))?
- Ramanujan's class invariants (G_n, g_n) are specific algebraic numbers of controlled degree. Do they give a quantitative companion to the φ(2n)/2 algebraic-degree growth already in `corners/PSEUDO-CHEBYSHEV-NODES.md`?
- The Hardy–Ramanujan asymptotic for the partition function bridges analytic (modular-form coefficient) and combinatorial regimes. Can that bridge be lifted to the counting-apparatus setting, where analytic rates of series approximation meet combinatorial word-length growth? (*This is the fun-but-dangerous direction — see §"When to leave" below.*)

### On the implicit BIND question

- What real numbers are exactly reachable from singular moduli at CM points + the modular-form machinery evaluated there? This is the Heegner-number closure question.
- How does the Heegner closure relate to the Baker-linear-forms-in-logs closure question that `memos/BIDDER-AND-SON.md` flags on the log side? Same shape, different shape, or structurally dual?

### On possible traps

- Do any of Ramanujan's "rogue" nested-radical identities from the notebooks produce 2cos(2π/n) for specific n in a form that would look like a counter-example to a naive compute-cost lower bound? If so, the lower bound will have to explain them.

---

## What specifically to read

In rough priority for this search:

1. **Borwein & Borwein 1987**, *Pi and the AGM* (Wiley). The big-picture reference connecting Ramanujan, Gauss's AGM, and modern π algorithms. Probably the single best book to pair with `memos/COUNTING-APPARATUS.md`.
2. **Chudnovsky & Chudnovsky 1988**, "Approximations and complex multiplication according to Ramanujan" (in *Ramanujan Revisited*, Andrews et al. eds.). The 14-digits-per-term series and its CM-theoretic origin.
3. **Ramanujan 1914**, "Modular equations and approximations to π," Quarterly J. Math. 45. The original singular-moduli idea.
4. **Hardy & Ramanujan 1918**, "Asymptotic formulae in combinatory analysis" — for the partition-function / analytic-combinatorial bridge if that direction pays off.
5. **Berndt**, *Ramanujan's Notebooks* (Springer, 5 vols.). Targeted lookups only; not a systematic pass.
6. **Heegner 1952 / Stark 1967** — on class-number-one imaginary quadratic fields; background for the implicit BIND question on closure.

If any of the above turns up nothing load-bearing, stop reading. Move to the exit.

---

## Pairing

Ramanujan alone doesn't carry item (A) of `memos/COUNTING-APPARATUS.md` — the compute-model choice. Two pairings:

- **Gauss.** Gauss–Wantzel gives the classical ruler-and-compass compute model; the AGM gives another rapid-π upper-bound family; cyclotomic theory is the ambient framework the circle-side catalog already inhabits. A companion `memos/GAUSS-WANTZEL-BRIEF.md` (already flagged in `memos/COUNTING-APPARATUS.md` as a candidate anchor) is the natural compute-model-theorist home.
- **Archimedes.** Already with the program via `n-gons/ARCHIMEDEAN-STRIP-FLIP.md` and `BNHA/triad/Eraserhead/ARCHIMEDEAN-CONSTRICTION.md`. The method of exhaustion is the original squeeze.

Archimedes–Gauss–Ramanujan as a classical triad cleanly covers the terrain: squeeze, compute-model, navigation-within-algebraic-depth.

---

## When to leave

This section has a specific job: to argue, with enough force to hold up against the in-moment appeal of the analytic-bridge material, that the program should exit Ramanujan's territory the moment its shape is clear.

**Why leaving is the hard part.** Ramanujan's realm is analytically seductive in ways Bidder's wasn't. Modular forms, q-series, theta functions, nested radicals, the Hardy–Ramanujan partition asymptotic, CM theory — each is a genuinely deep and beautiful territory, and each could absorb months or years without ever producing a compute-cost lower bound. The author of this memo has already flagged the concern: the analytic-bridge work is *fun*, the lower-bound work is *less fun*, and the latter is what the program actually needs to deliver. Ramanujan makes it easy to stay. Read this section as the discipline against staying.

**What Ramanujan supplies, and does not.** He supplies (i) the target (upper-bound rates), (ii) the inspiration (pre-theoretical faith), and (iii) the terrain (the algebraic-cyclotomic-modular landscape τ inhabits). He does not supply compute-cost *lower bounds*. Lower bounds live in a different literature entirely, written by different people in a different register. No amount of further Ramanujan reading will produce a lower bound — only confirm that upper bounds are what they are, and make the landscape look even richer.

**Exit criteria, as specific as the memo can make them.** Stop reading Ramanujan the moment *any one* of the following triggers:

1. **τ portrait carries belief.** Item (C) of `memos/COUNTING-APPARATUS.md` is complete enough that "here is why no finite algebraic structure reaches τ" reads as a load-bearing paragraph, not a scattered list. Ramanujan's contribution: sharpening the algebraic-depth picture via singular moduli. When that contribution is in, stop.
2. **Compute model chosen.** Item (A) is committed — probably algebraic-arithmetic over ℚ or an ASLP model. Ramanujan-Chudnovsky benchmarks fix the upper-bound lane. When the model is committed, stop.
3. **Small-case walkthrough runs.** Item (D) at n = 7 shows the three cost measures tracking. Ramanujan's contribution: specific upper-bound rates for cos(π/7) and similar. When the walkthrough is up, stop.
4. **A hypothesized lower bound has a shape.** Even conjecturally. This is the real exit. The moment a compute-cost lower bound has enough shape to state as a conjecture, stop reading Ramanujan outright.

**One practical heuristic.** Each Ramanujan-direction read should close with a sentence starting *"This bounds the compute cost of τ at …"* or *"This constrains a lower bound by ruling out …"*. If the read cannot produce such a sentence, the read did not serve the program, regardless of how intrinsically interesting the material was. Flag it, note it in this doc, move on.

**What to read instead, when exit triggers.** Ranked by estimated relevance to the circle-side compute-cost lower bound:

- **Blum, Shub, Smale 1998**, *Complexity and Real Computation*. The compute model closest to ruler-and-compass + integer arithmetic. Almost certainly load-bearing for item (A).
- **Bürgisser, Clausen, Shokrollahi 1997**, *Algebraic Complexity Theory* (Springer). The textbook. Algebraic straight-line program depth lower bounds live here.
- **Brent & Zimmermann 2010**, *Modern Computer Arithmetic*. The modern π-computation authority; the bridge where Ramanujan's upper bounds meet lower-bound discussion.
- **Heintz, von zur Gathen, Schnorr, Kaltofen** — algebraic-complexity classics from the 1980s–90s on straight-line-program and algebraic-circuit depth lower bounds.
- **Mulmuley's GCT program** — only if the lower bound turns out to require deep algebraic-geometry machinery. Probably premature; note but don't read first.

These are technical and unglamorous compared to Ramanujan's corpus. That is the point. Beauty of the terrain is not evidence that the terrain contains the theorem. A compute-cost lower bound is not a modular-forms question; it is a complexity-theoretic question that *uses* modular-forms evidence as benchmarks and counter-examples.

**Final framing.** The compliment Ramanujan pays the circle is real and already paid in full by the moment we open his notebooks. Stay long enough to collect the benchmarks and the portrait. Leave before the scenery becomes a substitute for the work.

---

## Status

Open search memo. Specific reads listed above, none started. No findings yet. This doc gets appended to as Ramanujan-directed reads happen. When any of the four exit criteria triggers, the doc freezes and the active work moves to lower-bound territory — with the exit list immediately above as the new reading queue.
