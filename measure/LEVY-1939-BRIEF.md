# Lévy 1939 — brief (the modulus/phase split on the circle)

**Paper.** P. Lévy, *L'addition des variables aléatoires définies sur une circonférence*, Bull. Soc. Math. France **67** (1939), 1–41 (NUMDAM, `BSMF_1939__67__1_0`). Source at [sources/LEVY-1939.pdf](sources/LEVY-1939.pdf). The §7 Fourier characterization of distributions on the circle Γ.

**What was read, and confidence.** §7 read directly from the source (journal pp. 23–30). The §7 3°–4° claims below are **verified against the text.** One correction made on verification: the result lives at equations **(30) and (32)**, §7 3°–4°; an earlier transcription cited "eq. 15," which is elsewhere in the paper and is not this result. Only the §7 3°–4° fact is pulled; the rest of Lévy's circle-addition theory (the convergence/quasi-convergence theorem of §7 5°–6°, the limit-type machinery of §4) is out of scope here.

## Payload — the one fact

For laws on the circle Γ given by Fourier coefficients, Lévy's §7 3°–4° establishes:

> **§7 3° (eq. 30, p. 24).** The product law's coefficients multiply, `a_n^(ν) = b_n^(1) b_n^(2) ⋯ b_n^(ν)`; since `|b_n^(ν)| ≤ 1`, `|a_n^(ν)|` decreases monotonically to a limit `|a_n|`, and **every accumulation law `L, L', …` has the same moduli `|a_n|`.** The moduli alone fix the limit-type: uniform (`a_n = 0`, all `n ≠ 0`), periodic of period `1/p` (`a_n = 0` off multiples of `p`), or non-periodic (`|a_n| > 0` on `n` with g.c.d. 1).
>
> **§7 4° (eq. 32, pp. 25–26).** The accumulation laws **differ from one another by addition of a constant** — translation along Γ. With moduli already equal, the phase is what distinguishes them: writing `L'' = L'/L`, `a_n'' = 1` wherever `|a_n| > 0`, so `L'` is a translate of `L`.

Equivalently, in the standard Fourier restatement (faithful to "addition of a constant," though Lévy does not display it as a formula): translating the law by `c` sends `a_n → a_n · e^{-2πinc}`, changing every phase and leaving every modulus fixed. The content downstream work uses: **the modulus is a function of the law's shape alone and is blind to where on Γ the law sits; the phase is the placement coordinate and is blind to shape. A circle-position coordinate is structure-blind** — its 1939 statement.

## Trust boundary

- *Proved in the source (verified here):* §7 3° eq. 30 — coefficient product, monotone modulus convergence, common moduli across accumulation laws, and the modulus characterization of limit-type. §7 4° eq. 32 — accumulation laws differ by addition of a constant (translation).
- *Faithful restatement, not displayed in the source:* the explicit shift identity `a_n → a_n e^{-2πinc}`. It is the standard Fourier form of Lévy's "addition d'une constante" with "même module," used here for legibility.
- *Inferred by this repo:* the reading of `(|a_n|, arg a_n)` as two orthogonal coordinates labelled "shape" and "placement," and the framing of the result as a structure-recovery limit. Lévy proves a classification of limit laws; the coordinate gloss is this program's.

## Role here — antecedent, not an input to Theorem K

This brief gives the *placement-coordinates-are-structure-blind* principle a named, dated home, so Theorem K's universal clause ([measure/FOR-BREAKFAST.md](measure/FOR-BREAKFAST.md) §K — "any function on `F` lifted by `R*` cannot recover `f₁, f₂, f₃`") can be read as a principled instance rather than an enumerated check: `R⁻¹(2^F)` is the placement σ-algebra on the lattice, and the geometric observables are not placement-measurable.

**It is a prototype, not a premise.** Lévy's split is `(|a_n|, arg a_n)` under *translation* of a law on the continuous circle; Theorem K's split is `(reduced fraction, denominator)` under *reduction* on the integer lattice — different group actions on different circles. K is proved on its own fiber-non-constant witnesses (`φ(5)/2 = 2 ≠ 4 = φ(15)/2`, etc.); nothing here is load-bearing for that proof, and the brief must not be cited as though Lévy *implies* K.

This brief is **not currently referenced from [paper/OUTLINE.md](paper/OUTLINE.md) or the §5.6 Theorem-K material.** It is available to be cited *if* the containment reading ("K is the rational-circle instance of a general placement/structure split") is put to work in §5; if that reading is not used, Lévy need not enter the paper at all.

## L–W safety

The date is 1939, the content is classical. The modulus/phase orthogonality and the translation identity are Fourier analysis on the circle — transcendence-free, methodologically pre-L–W, triggering nothing in the hazard repertoire of [memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md). No irrationality measure, Diophantine class, or transcendence statement is used or implied.

## Placement

Sits in `measure/` beside its only potential consumer, Theorem K ([measure/FOR-BREAKFAST.md](measure/FOR-BREAKFAST.md)), and the substrate catalogue ([measure/SUBSTRATE-OBSTRUCTIONS.md](measure/SUBSTRATE-OBSTRUCTIONS.md)). A leaf until the containment reading calls for it.
