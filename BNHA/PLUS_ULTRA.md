# PLUS_ULTRA

A reference doc stating the three disciplines of our program, one per character. Each discipline imposes a productive constraint that keeps the work focused and admissible. Together they partition the kinds of moves we can make on the F question between log-side (Landfall) and circle-side (NGON-WHOLENESS / Inscription).

The character framing is whimsical — very Lewis Carroll if you hold it up to the light. The mathematical content is not. Where a character's quirk maps cleanly to a research discipline, we use the mapping. Where the analogy strains, we drop it and keep the constraint.

Each discipline has its own doc one folder down in `triad/`: `triad/Eraserhead/BIND-THE-CIRCLE.md`, `triad/Creati/CREATI-THE-CIRCLE.md`, `triad/Lemillion/PERMEATE-THE-CIRCLE.md`. This file is the one-page map that says who does what.

## The three disciplines

### Lemillion (PERMEATE) — processual

**Slogan.** *You must know where you are going without looking. Think about the advance of the clock or the crossing of a link.*

**Quirk.** Permeation. Phase through solid matter. The hard part is not the phasing — it is knowing exactly where you will emerge, without being able to see. Mirio trained tens of thousands of hours to make emergence reliable.

**Discipline.** Preparation. No cross-domain move is admitted without the saturation table that would let a reader anticipate it. Anticipation is the research move; the tabulation is the cost. Paid in advance, spent on anticipation, localized on failure.

**Domain — things that advance or cross.** Anything sequential (orbit construction, continued-fraction expansion, saturation across a window, iteration of a rotation, scanning through ε(m) at dyadic m's). Anything cross-domain (matching n on the circle to m on the log by shared arithmetic, phasing an argument from one side to the other, inheriting structure across a boundary). If a claim requires the reader to trust an unbuilt bridge, PERMEATE builds the bridge via saturation first.

**Characteristic tools.** Joint saturation tables; anticipation from saturation; first-witness localization of obstructions; the Euclidean-algorithm / continued-fraction computational substrate; Lefèvre–Muller's 3DT algorithm as a cheap saturation engine.

**Home leg.** Leg 2 of the triad (crystallographic ↔ p-adic matching).

### Momo (CREATI) — constructive

**Slogan.** *You must know the construction you are building. But if you know it, there are no limits.*

**Quirk.** Creation. Materialize any non-living object from her lipid cells — provided she understands the molecular composition down to the atom. Knowledge is the only limit; within knowledge, no limit.

**Discipline.** Form. Every object in scope is given by counting, closed form, or identity (three admissible forms, plus an open-form slot reserved for results whose shape we cannot yet name). Nothing is invoked by existence alone. Nothing is admitted whose composition is partially unknown. The working material is what we can write down.

**Domain — things that can be built.** Explicit closed-form expressions. Exact enumerations. Forced identities between named quantities. Chebyshev polynomials and the monic-ℤ structure they generate. Niven's theorem and its consequences. Perfectly clustering Lyndon words. Specific lattice vectors with algebraic coordinates. ψ and φ and v_p as arithmetic functions with prime-factorization rules. Algebraic-closure arguments (ℤ[x] via Chebyshev, Aff⁺(ℝ) via machine ops). If we can write it, CREATI admits it regardless of how exotic. If we cannot specify it, CREATI refuses it regardless of how tempting.

**Characteristic tools.** Closed-form identities paired by kind (reflection / iteration); counting arguments; identity chains; algebraic-closure theorems; the catalog of named objects and the named operations extending it.

**Home leg.** Leg 1 of the triad (Chebyshev polynomial correspondence).

### Aizawa (BIND) — erasing

**Slogan.** *Focus and bind what cannot be used. Exhibit precision and foresight when dealing with remaining miscreants.*

**Quirk.** Erasure. Look at someone with a quirk and their quirk goes silent for as long as he holds gaze. Erasure is conditional, focused, and temporary — it demands sustained attention to stay in effect.

**Discipline.** Vocabulary. The shared vocabulary between the two sides is erased and kept out: **QMF** (Minkowski's question-mark function ?(x)), Stern–Brocot tree, Farey sequence, Thomae / popcorn function, Denjoy construction, dyadic expansions reinterpreted as continued fractions. These are the objects that make the two sides look alike for the wrong reasons; their absence forces the work back to primitives. The discipline is sustained: the shared vocabulary may not re-enter the working notes even as shorthand. If it does, Erasure is broken and the argument restarts from primitives.

**Domain — erasure and precision on remainder.** Finding the primitive version of every tool. Restating obstructions whose natural statement goes through forbidden vocabulary. Identifying which objects survive Erasure (lattice vectors, SL(2, ℤ) actions, the ψ-function, Γ\SL(2, ℝ), the continuous-E tool, lattice-geometric proofs like Marklof–Strömbergsson's 3DT) and which do not. Foresight about which miscreants will demand attention once the shared vocabulary is gone — Bowen's no-invariant-measure, the Babylonian fossil, the transcendence-at-dyadics theorem, the Aff⁺(ℝ) closure argument.

**Characteristic tools.** Erasure-legal primitives (Euclidean lattice vectors; the ψ-function; Γ\SL(2, ℝ) and its invariant measures; the continuous-E residue τ_c); representational-symmetry duality; lattice-geometric proofs without SB/Farey/QMF routing.

**Home leg.** Leg 3 of the triad (τ_c / ε spectral rhyme).

## What each discipline owns

- **PERMEATE owns the processual.** Advance of the clock. Crossing of a link. Saturation of a table. Anticipation of the next cell. Does not own static structure (CREATI does) or vocabulary hygiene (BIND does).
- **CREATI owns construction.** The closed-form object. The counting result. The identity relation. The algebraic-closure theorem. Does not own the processual cadence of iteration (PERMEATE) or the discipline of what cannot be said (BIND).
- **BIND owns erasure.** The focus on primitives. The precision about what is allowed. The foresight about which obstructions remain. Does not own the processual (PERMEATE) or positive construction (CREATI).

## Boundaries are porous, disciplines stay honest

A leg of the triad may reach into another discipline's domain when the need is sharp. PERMEATE's saturation uses CREATI's closed-form τ and ψ values. CREATI's forced identities are often verified by PERMEATE-style case-checking. BIND's lattice-geometric 3DT uses PERMEATE-style basis-finding and CREATI-style explicit coordinates.

The rule: **if you reach into another discipline, you respect its constraint while you are there.** Borrowing a table from PERMEATE inherits the tabulation requirement. Borrowing an identity from CREATI inherits the written-form requirement. Borrowing a tool from BIND inherits the Erasure prohibition on shared vocabulary.

Violating a constraint is not a failure of the discipline; it is an *exit* from the discipline. If CREATI produces something that cannot be specified, CREATI has not produced a result — it has left CREATI's scope. If BIND reaches for Stern–Brocot in the middle of an argument, BIND has broken Erasure and must restart from primitives.

## Continued-fraction rule

The three disciplines are aligned on one specific boundary:

- **Continued-fraction convergents as outputs of Euclid-style computation are admissible.**
- **Continued fractions as Stern-Brocot navigation or tree vocabulary are not.**

PERMEATE needs convergent computation as part of its saturation substrate. CREATI can admit convergents as explicit arithmetic data. BIND admits the computation but forbids the tree as an organizing frame. So the shared rule is:

> compute the convergents if you need them; do not explain the program by walking the tree.

## When to use which

- "Can we compute / saturate / anticipate across a cross-domain boundary?" → **Lemillion**.
- "Can we build / specify / identify in closed form?" → **Momo**.
- "Can we state this without the shared vocabulary, or find a primitive version?" → **Aizawa**.

If a question spans all three — *can we establish a cross-domain identity in closed form using only primitives?* — all three disciplines participate, each within its own constraint. The F question itself is of this kind.

## The three-constraint / three-domain summary

| Character | Quirk | Constraint | Domain | Home leg |
|---|---|---|---|---|
| Lemillion | Permeation | Preparation | Processual | Leg 2 |
| Momo | Creation | Form | Constructive | Leg 1 |
| Aizawa | Erasure | Vocabulary | Erasive | Leg 3 |

## The Lewis Carroll acknowledgment

The character framing is a mnemonic. It is not the math. The math is three productive constraints (preparation / form / vocabulary) applied to three domains (processual / constructive / erasive), all pointed at one shared goal (understand the F question).

If the character mapping ever gets in the way of the math, drop the character mapping. The constraints and the domains stay.
