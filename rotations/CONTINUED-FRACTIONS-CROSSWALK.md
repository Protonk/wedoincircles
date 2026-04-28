# CONTINUED-FRACTIONS-CROSSWALK

A cross-source synthesis note on one arithmetic object that keeps recurring: the continued-fraction convergents $p_n/q_n$ of $\alpha$. This is not a source brief; it is the crosswalk among six indexed perspectives across `rotations/`, `iso/`, and `memos/`.

The useful content that remains here is the read-across itself: six different literatures, six different rhetorics, one recurring arithmetic substrate.

## The six perspectives

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

### 5. Probabilistic / Diophantine (Beck 1994)

Beck's multidimensional discrepancy theorem replaces the one-dimensional continued-fraction route with Fourier analysis, second moments, and Borel-Cantelli. In dimension one, Khintchine's continued-fraction machinery already controls the same Diophantine-discrepancy interface; in higher dimensions, Beck shows what has to substitute for it.

So Beck is not another continued-fraction algorithm. It is the probabilistic perspective that reveals the content carried by continued fractions in one dimension: a sharp almost-every discrepancy threshold, expressed in Beck's setting as $(\log N)^k \varphi(\log\log N)$ with the Borel-Cantelli condition $\sum 1/\varphi(n) < \infty$.

**Continued-fraction convergents are the one-dimensional substrate whose Diophantine content Beck's Fourier-side machinery preserves by substitution.**

### 6. Effective transcendence (K-H-L-A)

The K-H-L-A discrepancy branch uses continued fractions of $\pi$ as the arithmetic substrate under the Aitchison $\times$ Erdős-Turán-Koksma $\times$ Kraft pairing. The parent memo now fixes the operative classification through the exponential-rate parameter $\beta(\pi)=0$; the one-dimensional bookkeeping note isolates the empirical-to-density proxy where that classification has to feed the discrepancy budget.

The target quantity is an effective irrationality measure

$$
|q\pi-p| \gg q^{-C},
$$

with $C$ extracted from the same Fourier/Kraft budget rather than imported as a black-box transcendence-theory constant.

**Continued-fraction convergents of $\pi$ are the arithmetic scaffold on which the program tries to read an effective constant.**

## The unified object

All six perspectives converge on the continued-fraction convergents $p_n/q_n$ of $\alpha$. The different usages:

| Source | Uses CF for | Key quantity |
|---|---|---|
| 10-martinis | Arithmetic-type classification of $\alpha$ | $\beta(\alpha)=\limsup \ln(q_{n+1})/q_n$ |
| Berthé–Reutenauer | 3DT pattern formation | orbit structure organized by convergent depth |
| Lefèvre–Muller | Fast minimum-distance computation | Euclidean-style loop on the same arithmetic data |
| Landfall (Gosper) | Continued-fraction arithmetic-in-hardware | 8-variable Möbius transducer |
| Beck 1994 | Higher-dimensional Fourier substitute for one-dimensional CF control | $(\log N)^k\varphi(\log\log N)$ Borel-Cantelli threshold |
| K-H-L-A | Effective transcendence / discrepancy substrate for $\pi$ | effective $C$ in $|q\pi-p|\gg q^{-C}$ |

The underlying arithmetic is the same. The differences are rhetorical: spectral theorists write β; combinatorists write word encodings; algorithmists write Euclid's-algorithm subtractions; computer arithmeticians write Möbius transformations on 8 integer variables; probabilists write Fourier substitutes and Borel-Cantelli thresholds; the K-H-L-A branch writes effective constants against $\pi$. All six describe, replace, or budget the convergents.

For our program this means: **we have six independent reasons to treat the continued-fraction convergents of α as a primitive object.** Each source validates the status of the object from a different angle.

Pattern note: this crosswalk is the bridge between
[rotations/3DT-BRIEF.md](rotations/3DT-BRIEF.md), where three lenses
converge on one theorem, and
[iso/THREE-REGISTER-SYNTHESIS.md](iso/THREE-REGISTER-SYNTHESIS.md),
where three registers illuminate the same isoperimetric gap but with
different sharp currencies. Here the object is neither one theorem nor
one gap; it is the primitive substrate of continued-fraction convergents
viewed through six source families.

## Pointers

- For the spectral perspective on CF: `rotations/10-MARTINIS-BRIEF.md`.
- For the combinatorial and algorithmic 3DT perspectives: `rotations/3DT-BRIEF.md`.
- For the Gosper / computational perspective: §4 above and `fft/LANDFALL-PROOF-TEMPLATES.md` Template 3.
- For the probabilistic / Diophantine Fourier-substitute perspective: `iso/BECK-1994-BRIEF.md`.
- For the K-H-L-A effective-transcendence branch and its Step 5 bookkeeping interface: `memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md`, `memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md`.
- For the discipline rule on admitting CF computation while forbidding the Stern-Brocot tree as organizing frame: `BNHA/triad/PLUS_ULTRA.md`.
- For the saturation-side use of convergents: `BNHA/triad/Lemillion/PERMEATE-THE-CIRCLE.md`.
- For the program-level triad absorption and the cross-leg Liouville/Diophantine axis: `BNHA/triad/NIVEN-THREE-WAYS.md`, `BNHA/triad/TRIAD-ABSTRACT-PATTERN.md`.
