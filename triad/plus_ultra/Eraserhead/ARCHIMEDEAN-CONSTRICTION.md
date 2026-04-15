# ARCHIMEDEAN-CONSTRICTION

A BIND move. The Archimedean strip is used as a geometric substitute that binds around the Stern–Brocot / Thomae object without engaging it. The obstruction is not handled; it is constricted. Erasure holds throughout: no primitive from the S–B / Thomae family enters the operative vocabulary.

Companion to `triad/plus_ultra/Eraserhead/BIND-THE-CIRCLE.md`. The linkage that motivates the move is articulated in `memos/BOTHERSOME-EUDOXUS.md` (the rhyme and its regularity opposition); the geometric objects used are in `n-gons/ARCHIMEDEAN-STRIP-FLIP.md` and `n-gons/STRIP-AND-SUBPOLYGON.md`.

---

## What is refused

Per `BIND-THE-CIRCLE.md`'s Erasure list:

- Minkowski `?(x)`.
- The Stern–Brocot tree, Farey sequences, Farey neighbors, mediant geometry.
- The Thomae / popcorn function. In particular: the height law `f(p/q) = 1/q` at reduced rationals, and its pointwise regularity profile (continuous at irrationals, discontinuous at rationals).
- Denjoy's construction; dyadic expansions reinterpreted as continued fractions.
- Reduction of a rational `k/n` to lowest terms `p/q` when that reduction is the operative step — i.e., when the argument depends on the denominator `q` as an arithmetic object rather than on `n` as a geometric parameter.

These primitives are not merely absent from the statement; they are absent from every step of the derivation. If any of them re-enters, the derivation has left BIND and restarts.

## What is used

Circle-side geometric primitives, from `BIND-THE-CIRCLE.md`'s allowed list:

- Regular polygons circumscribed around a fixed unit incircle; the shared anchor edge; the tangency at $(1, 0)$.
- Position $k$ of the $n$-gon at angle $2\pi k / n$, labeled by the *unreduced* pair $(k, n)$.
- The incircle as the fixed inner boundary; the 3-cir (the $n = 3$ circumscribed circle) as the fixed outer boundary.
- Angular widths $\pi/n$; secant half-edges; the polar equation $r = \sec(\theta - 2\pi k/n)$ of a straight edge tangent to the incircle.
- The unroll $x = \theta/(2\pi)$, $y = r - 1$ that maps the annulus $\{1 \le r \le 2\}$ to the flat strip $[0, 1]^2$.
- The integral $\int \sec = \ln|\sec + \tan|$.

No arithmetic function of the denominator appears. No depth function on a binary tree appears. No limiting process that invokes reduction-to-lowest-terms appears.

## The operative substitution

The S–B / Thomae pair uses a **height law indexed by the denominator**:

$$
h_{\text{Thomae}}(p/q) = 1/q, \qquad p/q \text{ reduced.}
$$

The strip uses a **height datum indexed by the polygon order**:

$$
h_{\text{strip}}(n) = \sec(\pi/n) - 1.
$$

Both attach a height to points on $[0, 1]$. Thomae's attachment is to each reduced rational individually, indexed by that rational's arithmetic (denominator). The strip's attachment is to each $n$-gon's secant arc, indexed by the polygon order — a geometric parameter native to the circle side.

The two height laws agree on nothing. They share only a floor: the tangency positions $k/n$ where the strip's secant arcs touch $y = 0$ are the same set of points, taken over all $n$, that Thomae decorates with $1/q$ stems. BIND inherits the floor as *positional data* ($k/n$ unreduced, one label per $(k, n)$ deposit) and refuses the height law.

## What this achieves, at BIND-legal precision

Computing in the strip, using only the primitives above, one obtains

$$
\int_{-1/(2n)}^{1/(2n)} \bigl(\sec(2\pi x) - 1\bigr)\,dx = \frac{1}{\pi}\ln\bigl(\sec(\pi/n) + \tan(\pi/n)\bigr) - \frac{1}{n},
$$

and summing over the $n$ arcs gives

$$
A_{\text{below}}(n) = \frac{n}{\pi}\ln\bigl(\sec(\pi/n) + \tan(\pi/n)\bigr) - 1
= \frac{\pi^2}{6\,n^2} + O(n^{-4}).
$$

This is the Archimedean exhaustion in closed form, produced without invoking Thomae's height, the denominator $q$, or any reduction step. The only arithmetic in view is integer arithmetic on $n$ and $k$; no arithmetic function of $q$ has been summoned.

The corresponding flattening statement — arc maxima $y_n = \sec(\pi/n) - 1 \sim \pi^2/(2n^2) \to 0$ — is a geometric fact about secant expansion, not a regularity statement about a function on $[0, 1]$. BIND obtains it without asserting anything about the regularity of any function living on the rationals.

## The constriction

The S–B / Thomae object has an obstruction: its height law is resolution-blind, and under any resolution-indexed averaging (Cesàro-uniform in the resolution parameter), the stems do not flatten. See the regularity addendum of `memos/BOTHERSOME-EUDOXUS.md`.

The strip object, built on the same floor with a different height law, has no such obstruction. Its arcs flatten at rate $\pi^2/(6 n^2)$, and the computation producing that rate is BIND-legal throughout.

The BIND move is therefore precise:

1. **Inherit** the tangency floor as positional data.
2. **Refuse** the Thomae height law and every derivation that depends on it.
3. **Substitute** the strip's geometric height law $\sec(\pi/n) - 1$.
4. **Compute** the closed-form area and its Archimedean limit using only geometric primitives.

The S–B / Thomae obstruction is not solved. It is not asked about. The primitive that would summon it — the reduced denominator $q$ — is not written down. Everything in view is indexed by $n$, which is a polygon count, and $k$, which is a position label. Neither is an arithmetic function of any reduced form.

This is constriction: the obstruction sits beneath the strip, on the same floor, but the strip's operative vocabulary does not reach it, and the results produced by the strip do not require it. BIND erases the S–B / Thomae object from the working vocabulary and builds the geometric object that occupies the same floor without inheriting its height law.

## Why "Archimedean"

Archimedes' method of exhaustion constricts the circle between inscribed and circumscribed polygons, identifying the circle's area by squeezing from both sides without ever writing down a non-geometric primitive. BIND's move here is the same shape of operation, one level up: constrict the rational-lattice decoration on the circle between the strip's secant arcs above and the incircle below, identifying the limit (a flat floor) by squeezing geometrically, without ever writing down a non-geometric primitive about rationals.

The classical Archimedean constriction dodges irrationality (of $\pi$) by staying in polygon-area arithmetic. The present Archimedean constriction dodges the S–B / Thomae obstruction by staying in secant-arc geometry. Same shape.

## What this does not claim

- This memo does not claim that the S–B / Thomae object is dispensable in general. Other work (outside BIND) may engage it. BIND only claims it can be bound around in this specific computation.
- This memo does not claim the strip flattens Thomae. The strip and Thomae have different limit behavior (opposite regularity directions; see the addendum in `BOTHERSOME-EUDOXUS.md`). Flattening is not the BIND objective; vocabulary hygiene is.
- This memo does not claim to prove a π-side computational-impossibility statement of the Landfall shape. BIND clears the vocabulary in which such a statement could be posed on the strip. Whether the statement actually holds — whether there is a named circle-side closure and a Bowen-analog no-aggregation theorem — is a separate question, not undertaken here.

## What this unlocks for the program

The open question at the end of the speculative discussion in `BOTHERSOME-EUDOXUS.md` is: does the circle side admit a computational-closure-and-aggregation impossibility consonant with Landfall's log-side one? The strip, not Thomae, is the natural circle-side object to ask this of, because the strip is BIND-legal end to end and the question about it can be posed without importing any piece of the erased vocabulary.

This does not answer the question. It moves the question to a surface where the question is pose-able. That is the only thing BIND is meant to do: clear the vocabulary, leave the work to be done on allowed primitives, mark precisely what has been refused and what has been kept. The refusal is the discipline; the constriction is the result of keeping the discipline.
