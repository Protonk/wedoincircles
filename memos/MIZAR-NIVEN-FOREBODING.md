# MIZAR-NIVEN-FOREBODING

A future-facing memo on Korniłowicz & Naumowicz, *Niven's Theorem*, Formalized Mathematics 24(4), 2016, pp. 301–308.

This is not here because the program needs Mizar today. It is here because this is the sort of paper future-us may suddenly care about: a formally verified version of exactly the Chebyshev / monic-ℤ / rational-root chain that keeps showing up around Niven, the crystallographic set, and the circle-side closure story. Accompanying memo: `triad/NIVEN-THREE-WAYS.md`.

## Why keep this around

If we ever need one of the following, this paper will probably re-enter:

- a formal citation for “Chebyshev gives a monic integer polynomial”;
- a formal version of the rational-root / integer-root step;
- a map from the human Niven proof to something machine-verifiable;
- or a sanity check on what it would cost to formalize our own circle-side algebra later.

So this file is a re-entry map, not a source brief in the same sense as the other math-paper memos.

## What the paper is like

Mizar papers are written for the verifier, not for a human reader trying to learn the proof.

- Most of the 70 propositions are plumbing.
- The prose is thin.
- The interesting content is scattered among many tiny lemmas.
- Reading it straight through is a bad use of attention.

If you want the human proof first, ProofWiki is the right warm-up:
https://proofwiki.org/wiki/Niven's_Theorem

Then come back to the Mizar paper only when you need a precise proposition number.

## The propositions likely to matter later

### First tier

These are the ones most likely to matter if the future gets formal.

**(50) Rational Root Theorem.** For a $\mathbb{Z}$-valued polynomial, a rational root $k/l$ in lowest terms forces divisibility conditions on $k$ and $l$.

**(51) Integer Root Theorem.** A rational root of a monic $\mathbb{Z}$-valued polynomial is an integer.

**(52) Chebyshev existence theorem.** For $e=2\cos t$ and $n\ge 1$, there exists a monic $\mathbb{Z}$-valued polynomial $p$ of degree $n$ with

$$
p(e)=2\cos(nt).
$$

This is the one with the strongest future smell. If we ever need to say, in a formal or citation-heavy way, that the circle side carries monic-ℤ closure through Chebyshev, this is the proposition number to grab.

### Second tier

These are less central, but plausible future touchpoints.

**(49) Factor-theorem variant.** If $p(a)=b$, then $p-b$ has root $a$.

**(61) Niven for cosine.** If $r/\pi$ is rational and $\cos r$ is rational, then

$$
\cos r\in\{0,\pm 1/2,\pm 1\}.
$$

**(70) Niven for sine.** Same statement for $\sin r$.

**(53)–(60), (62)–(69).** The interval-by-interval casework that actually assembles the final Niven statements.

**(45), (46), (39)–(48).** Leading-coefficient and monic-behavior lemmas. Not glamorous, but these are the pieces you would touch if you were rebuilding the Chebyshev induction inside a proof assistant.

### Third tier

The rest is mostly there to make Mizar comfortable:

- arithmetic housekeeping,
- polynomial-as-finite-sequence conventions,
- explicit evaluation lemmas,
- degree and coefficient bookkeeping.

Ignore all of this unless you are actually formalizing.

## The likely reasons to come back

Future-us is likely to reopen this note under one of these headings:

**“I need a formal citation for monic-ℤ Chebyshev.”**
Use proposition (52).

**“I need the rational-root step in a formal setting.”**
Use (50) and (51).

**“I need the final formal Niven statement, not the machinery.”**
Use (61) or (70).

**“I need to see how Mizar encodes integer-coefficient polynomials over the reals.”**
Start in the coefficient / degree / leading-coefficient cluster around (39)–(48), with (20), (38) nearby.

**“I need the human source instead of the formal one.”**
Go to Niven’s *Irrational Numbers* first. The Mizar paper is for proof objects, not exposition.

## References worth remembering

If this thread gets pulled, these are the references most likely to matter:

- **[8] J. D. King, _Integer roots of polynomials_.** Short informal source for the root theorem.
- **[9] Serge Lang, _Algebra_.** Standard background if the polynomial-ring side needs refreshing.
- **[11] Robert Milewski, formalized FTA.**
- **[12] Ivan Niven, _Irrational Numbers_.** The canonical non-Mizar source.
- **[13] Piotr Rudnicki, formalized factor theorem.**

The likely future chain is:

our argument -> Niven / Chebyshev step -> this Mizar paper -> whichever supporting Mizar lemma it imports.

## Foreboding

This memo is speculative on purpose. It is not claiming that we are about to formalize anything. It is recording a suspicion about what kinds of future pressure could make this paper suddenly relevant.

Some plausible futures:

- we decide that the circle-side closure story needs formal backing rather than just persuasive algebra;
- we want a sharper citation than “Chebyshev does this”;
- a reviewer or collaborator asks whether the Niven-side argument is merely standard or also formalizable;
- we decide to port part of the program into a proof assistant and need a nearby precedent.

If none of that happens, this note can sit quietly. If any of it does happen, the one thing to remember is simple:

> proposition (52) is the likely doorway back in.

That is the whole omen.
