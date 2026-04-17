# CONTINUED-FRACTIONS-CROSSWALK

A cross-source synthesis note on one arithmetic object that keeps recurring: the continued-fraction convergents $p_n/q_n$ of $\alpha$. This is not a fifth source; it is the crosswalk among four existing memos.

The useful content that remains here is the read-across itself: four different literatures, four different rhetorics, one recurring arithmetic substrate.

## The four perspectives

### 1. Spectral (Avila–Jitomirskaya, 10-martinis)

Continued fractions measure α's arithmetic type. Let p_n/q_n be the convergents of α ∈ ℝ \ ℚ. Define

$$\beta(\alpha) = \limsup_{n \to \infty} \frac{\ln q_{n+1}}{q_n}.$$

- β = 0: α is Diophantine.
- β > 0: α is Liouville.

The Ten Martini proof splits the parameter space by β. The critical region β ≤ |ln λ| ≤ 2β (where λ is the almost-Mathieu coupling) is inaccessible from either direct method; it is where their analytic-continuation machinery does its hardest work. **Continued-fraction convergents are what define the cut.**

### 2. Combinatorial (Berthé–Reutenauer, 3DT)

For an $(\alpha, N)$ pair, the 3DT partition is controlled by convergent depth: which denominator $q_n$ first passes the orbit length, and how the Euclidean data at that depth resolve into the two or three gap sizes. Berthé–Reutenauer do not make continued fractions the foreground vocabulary of their proof, but the arithmetic structure sits behind the distances.

The word encoding is the finite combinatorial compression of that partition. **Continued-fraction convergents are part of what determines which finite pattern appears.**

### 3. Algorithmic (Lefèvre–Muller, Table Maker's Dilemma §2.2.1)

The pseudocode on p. 10 of their paper — the $(\gamma,\delta,d,u,v)$ subtractive loop — is a Euclidean-style computation on the slope $a$. $\gamma$ and $\delta$ carry the current two shorter distances, and the loop compresses the orbit structure into the same arithmetic data that continued-fraction convergents encode.

The algorithm stops when the compressed arithmetic data are deep enough to cover orbit length $N$. **Continued-fraction convergents are the arithmetic substrate behind that compression.**

### 4. Computational (Landfall §7, Gosper's CF machine)

Gosper (1972) describes a transducer that represents continued-fraction arithmetic by eight integer state variables updated by Möbius transformations. Landfall notes:

- Gosper's machine reaches periodicity only for quadratic irrationals — this is §2's recurrence obstruction.
- Its operations are Möbius transformations that cannot produce the logarithmic coordinate change ψ = log₂(1 + m) — this is §2's affine obstruction.
- It "survives by refusing finite closure."

**Continued-fraction convergents are what Gosper's machine handles exactly, term by term, on the log side.**

## The unified object

All four perspectives converge on the continued-fraction convergents $p_n/q_n$ of $\alpha$. The different usages:

| Source | Uses CF for | Key quantity |
|---|---|---|
| 10-martinis | Arithmetic-type classification of $\alpha$ | $\beta(\alpha)=\limsup \ln(q_{n+1})/q_n$ |
| Berthé–Reutenauer | 3DT pattern formation | orbit structure organized by convergent depth |
| Lefèvre–Muller | Fast minimum-distance computation | Euclidean-style loop on the same arithmetic data |
| Landfall (Gosper) | Continued-fraction arithmetic-in-hardware | 8-variable Möbius transducer |

The underlying arithmetic is the same. The differences are rhetorical: spectral theorists write β; combinatorists write word encodings; algorithmists write Euclid's-algorithm subtractions; computer arithmeticians write Möbius transformations on 8 integer variables. All four describe the convergents.

For our program this means: **we have four independent reasons to treat the continued-fraction convergents of α as a primitive object.** Each source validates the status of the object from a different angle.

## What Was Dispersed

The earlier version of this note also carried discipline policy and program-planning material. That content now lives in the docs that actually own it:

- The discipline rule “admit CF computation, forbid the Stern-Brocot tree as organizing frame” now lives in `BNHA/PLUS_ULTRA.md`.
- The saturation-side use of convergents now lives in `BNHA/triad/Lemillion/PERMEATE-THE-CIRCLE.md`.
- The log-side computational role of Gosper’s machine now lives in `memos/LANDFALL-EXPORT.md`.
- The cross-leg Liouville/Diophantine axis now lives in `BNHA/triad/TRIAD-ABSTRACT-PATTERN.md`.

## Pointers

- For the spectral perspective on CF: `memos/10-MARTINIS-BRIEF.md`.
- For the combinatorial and algorithmic 3DT perspectives: `memos/3DT-BRIEF.md`.
- For the Gosper / computational perspective: `memos/LANDFALL-EXPORT.md`, especially §7 and Program-Facing Export 5.
- For the program-level triad absorption: `memos/NIVEN-THREE-WAYS.md`, `BNHA/triad/TRIAD-ABSTRACT-PATTERN.md`, and `BNHA/PLUS_ULTRA.md`.
