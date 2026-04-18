# TRIAD-ABSTRACT-PATTERN

The abstract companion to `BNHA/triad/NIVEN-THREE-WAYS.md`. Niven is the concrete test case: one solved theorem, three routes, one visible handoff. This note states the pattern that test is probing.

The core claim is modest. We are not assuming a single functor `F` already exists between the log-side and circle-side obstructions. We are testing three distinct *attack shapes* for such an `F`, each with its own primitives, its own discipline of best fit, and its own characteristic way of failing.

## Why there are three legs

A single candidate correspondence can fail, but its failure is hard to interpret. A triad gives failure geometry.

- If all three legs fail for the same reason, that repeated reason is likely the real obstruction.
- If the legs fail differently, the problem has more internal structure than any one viewpoint captures.
- If one leg succeeds while the others fail, the successful leg says what `F` is, and the failed legs say what `F` is not.

This is the only load-bearing claim at the triad level. Everything else is leg-specific work.

## The three disciplines

Each leg lives where its natural primitives already exist. The split is at the level of **elementary posture toward mathematics**: each discipline names a distinct kind of mathematical work, and the characters are load-bearing nicknames for the postures.

- **CREATI** supplies **form**; the posture is **constructive**. Every object must be a count, a closed form, or an identity. This is the right home when the question is whether one side's rigid identities or algebraic closure have a counterpart on the other.
- **PERMEATE** supplies **preparation**; the posture is **translational**. No cross-domain move is admitted without the small-case table that would let a reader anticipate it. This is the right home when the question is whether arithmetic matching survives saturation.
- **BIND** supplies **vocabulary hygiene**; the posture is **constrictive**. The shared vocabulary is erased so each side has to speak in its own primitives. This is the right home when the question is whether residue-level or spectral structure survives after the easy analogies are removed.

The postures are complementary, not competing — and complete: build, translate, constrict are the three natural things one can elementarily do to attack an unknown functor F, and the triad has exactly one canonical home for each. A leg may borrow from another, but when it does, the borrowing should be explicit.

## The three legs

### Leg 1: identity / polynomial closure

Question: does the circle side's native closed-form identity structure have a genuine log-side cousin, or is the mismatch itself the obstruction?

This is the CREATI leg. The exact formulas belong in `BNHA/triad/Creati/CREATI-THE-CIRCLE.md`. At the abstract level, Leg 1 tests whether circle-side algebraic closure transports at all. If it fails, the interesting result is not merely "no formula was found"; it is "the two sides support different kinds of rigid identity."

### Leg 2: arithmetic matching

Question: can arithmetic invariants on the circle side and log side be matched naturally enough to support a cross-domain rule, at least on a visible finite regime?

This is the PERMEATE leg. The exact arithmetic objects belong in `BNHA/triad/Lemillion/PERMEATE-THE-CIRCLE.md` and the crystallographic source brief. At the abstract level, Leg 2 tests whether a matching rule survives saturation, where the decisive datum is often the first witness at which the pattern breaks.

### Leg 3: residue / spectral rhyme

Question: if pointwise transport is too strict, do the two sides at least share invariant-level structure such as decay, symmetry, or other residue behavior?

This is the BIND leg. The actual objects and obstructions belong in `BNHA/triad/Eraserhead/BIND-THE-CIRCLE.md`. At the abstract level, Leg 3 tests whether any correspondence remains once the shared vocabulary is withheld and only native primitives are allowed.

## A shared arithmetic axis

When a problem in the program depends on an irrational slope or frequency $\alpha$, the continued-fraction convergents $p_n/q_n$ and the Liouville/Diophantine split are not local curiosities. They cut across the legs.

- In the spectral memo, they appear through $\beta(\alpha)$.
- In the 3DT memo, they appear as convergent depth and Euclidean-style update data.
- In PERMEATE, they are part of the computational substrate that makes saturation cheap enough to scale.

So arithmetic type is a cross-cutting axis of the program, not a special-purpose tool belonging to one paper.

## How to read outcomes

The Niven memo already shows the smallest clean instance of mixed behavior: two legs close as proofs, while the third gives a productive attack that still needs a loaned lemma. That pattern is not a defect in the triad. It is one of the things the triad is for.

So the outcome taxonomy is:

- **Shared obstruction.** Different legs keep running into the same mismatch. That repeated mismatch becomes the result.
- **Structured disagreement.** Different legs fail differently. Then the non-existence of a single neat `F` may be less interesting than the partition of what transports and what does not.
- **Complementary closure.** One discipline gets the conjectural picture cheaply, another supplies the closing lemma, and a third clarifies the primitive setting. This is still evidence of a real architecture, not a breakdown.
- **Leg success.** A genuine correspondence appears in one invariant type. Then the other legs become boundary tests on its scope.

## How this pairs with Niven

`BNHA/triad/NIVEN-THREE-WAYS.md` is the concrete base case.

- It shows what a triad run looks like on a theorem whose answer is already known.
- It shows that the disciplines are not just stylistic labels; they sort real proof behavior.
- It shows a first explicit handoff: PERMEATE can narrow the tail but not close it alone, and CREATI supplies the closing arithmetic lemma.

This note supplies the abstract reading frame for that example. Read together, the pair says:

- Niven: here is the triad at work.
- This note: here is what that work is evidence *for*.

## Doc map

The triad-level companion sits above the leg docs, not in competition with them.

| Role | Doc |
|---|---|
| Concrete worked test | `BNHA/triad/NIVEN-THREE-WAYS.md` |
| Abstract pattern / reading frame | `BNHA/triad/TRIAD-ABSTRACT-PATTERN.md` |
| Leg 1 home | `BNHA/triad/Creati/CREATI-THE-CIRCLE.md` |
| Leg 2 home | `BNHA/triad/Lemillion/PERMEATE-THE-CIRCLE.md` |
| Leg 3 home | `BNHA/triad/Eraserhead/BIND-THE-CIRCLE.md` |

## Scope note

This file is intentionally not the authoritative place for leg mathematics. It should be used for:

- explaining why the program has three legs,
- explaining how to interpret success and failure across legs,
- pairing with Niven as the abstract half of the example,
- and orienting a reader toward the live leg-specific docs.

It should not be used as the place where the exact formulas or leg-level claims are settled. Those now live in the leg docs and source briefs.
