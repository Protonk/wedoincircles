# MEASURE-THEORETIC-OBSTRUCTIONS

The `measure/` register supplies the program with substrate-side
measure-theoretic refusal and the first bridge from that refusal to the
algorithm-side closure / drift argument. The detailed five-row catalogue
lives at
[measure/SUBSTRATE-OBSTRUCTIONS.md](measure/SUBSTRATE-OBSTRUCTIONS.md);
the bridge obligation lives at
[measure/THE-FIRST-BRIDGE.md](measure/THE-FIRST-BRIDGE.md).

## What This Memo Carries

The impossibility outline uses five substrate-side angles in
[paper/OUTLINE.md](paper/OUTLINE.md) §5:

1. rotation-orbit Diophantine kinematics, typed by Haar measure on
   `T = R/Z`;
2. non-nesting isoperimetric registers: rate, constant, almost-every;
3. closed-form polygon arithmetic, typed by `ζ(2)`-tail counting on
   Hurwitz bands;
4. cyclotomic-ladder growth against affine flatness, typed as a
   counting-invariant obstruction;
5. the L-W admissibility envelope, typed by the Lebesgue null/full
   dichotomy on algebraics and transcendentals.

This memo does not try to re-prove those facts. It records the paper
role: these five rows are **substrate-side refusals**. They show how
the program's available measures fail to supply the distinguishing
information needed for descent past `T(P)`. They do not by themselves
prove the FFT impossibility theorem.

## Division Of Labor

[measure/SUBSTRATE-OBSTRUCTIONS.md](measure/SUBSTRATE-OBSTRUCTIONS.md)
is the detailed source-side catalogue.

[measure/THE-FIRST-BRIDGE.md](measure/THE-FIRST-BRIDGE.md) states the
first bridge still to earn: `δ = 0` must be shown to be the forbidden
closure boundary, so closure preservation and bounded drift become two
readings of one measurable invariant.

[paper/FIRST-PROOF.md](paper/FIRST-PROOF.md) and
[paper/OUTLINE.md](paper/OUTLINE.md) decide
how this measure package enters the proof. Lemma A remains a parallel
substrate-side reading, not a QED premise, until its exhaustiveness debt
is closed.

## Trust Boundary

Cite this file for the paper-level routing of the measure package. Cite
[measure/SUBSTRATE-OBSTRUCTIONS.md](measure/SUBSTRATE-OBSTRUCTIONS.md)
for the five detailed rows. Cite
[measure/THE-FIRST-BRIDGE.md](measure/THE-FIRST-BRIDGE.md) for the
closure / drift bridge obligation. Do not cite any of these as proving
the bridge, the exhaustiveness of Lemma A, or the final impossibility
claim.
