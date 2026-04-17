# BOTHERSOME-EUDOXUS

A note on the gap between *existence of a shape-invariant ratio* and *closed-form value of that ratio*, anchored to the Archimedean strip construction we use elsewhere in this repo.

## The classic statement

Elements XII.2, attributed to Eudoxus:

> Circles are to one another as the squares on their diameters.

That is, for any two circles with diameters $d_1, d_2$ and areas $A_1, A_2$,

$$
A_1 : A_2 \;=\; d_1^{\,2} : d_2^{\,2}.
$$

Not a formula — a proportion. "The square on the diameter" is the literal geometric square of side $d$, and Eudoxus's claim is that two such squares stand in the same ratio as the two circles they enclose. The proof is the method of exhaustion: inscribe regular polygons, show the polygon-to-circle difference is smaller than any given magnitude, and use a double-reductio to rule out any other ratio. No numerical value is computed. The theorem is that the ratio is well-defined and shape-invariant, not what it is.

## Archimedes names the constant

A generation later, Archimedes identified the constant. For any circle,

$$
A \;=\; \tfrac{1}{4}\pi d^{\,2},
$$

equivalently $A = \pi r^2$, with $223/71 < \pi < 22/7$ as his bounding estimate. Archimedes's achievement was to pin down the value that Eudoxus's proposition only asserted existed. From then on "the circle constant" is not just a shape-invariant ratio — it is a specific real number (transcendental, as Lindemann later proved).

## Shapes where the ratio exists but the value is not known

Every deterministic similarity class of planar shapes has a shape-invariant $A/L^2$ ratio for any characteristic length $L$ — this is trivial dimensional analysis. For random shapes or random geometric functionals, the analogous invariant lives at the level of expectation or law after normalization. The bothersome cases are objects defined implicitly, where the shape or functional has a specific area constant but we do not possess a closed form for it.

- **The Mandelbrot set.** A specific bounded subset of the plane with numerically estimated area about $1.5065918\ldots$. No closed form is known, and no theorem rules one out. Equivalently, relative to its own diameter $d_M$, the normalized ratio $A_M/d_M^2$ is fixed but not known in closed form. We do not know if we *can* know the exact value in the sense Archimedes knew $\pi/4$.

- **The optimal moving sofa.** The maximum-area shape that can navigate a unit L-corridor. Gerver's explicit candidate has area $\approx 2.2195$; the best proven upper bound is near $2.37$. The optimizer is an implicit object — defined by a variational problem — and its area is unknown in closed form. Whether Gerver's sofa is optimal is itself open.

- **Expected-area functionals of random shapes.** Some, like the expected area of the convex hull of planar Brownian motion on $[0, T]$, have elegant closed forms ($\pi T / 2$, Spitzer). Others, like higher normalized moments for Poisson–Voronoi cells, do not. Here the invariant is not “every instance has the same $A/d^2$,” but a normalized expectation or law-level quantity.

In each case the normalized constant *exists* in the relevant sense — exact similarity ratio for a deterministic shape, normalized expectation or law-level quantity for a random one — but its numerical value has no Archimedean companion theorem.

## The Archimedean strip

Our n-gon work has a coordinate chart that makes the Archimedean squeeze visually explicit: the **Archimedean strip** (`n-gons/ARCHIMEDEAN-STRIP-FLIP.md`). Unroll the annulus $\{1 \le r \le 2\}$ to a flat rectangle by

$$
x = \theta/(2\pi) \in [0,1], \qquad y = r - 1 \in [0,1].
$$

The incircle $r = 1$ is the strip's bottom edge; the 3-cir $r = 2$ is the top edge. Each circumscribed regular $n$-gon appears as $n$ secant arcs, each arc touching $y = 0$ at its midpoint (tangency with the incircle) and rising to $y_n = \sec(\pi/n) - 1$ at both endpoints (the corners of the $n$-gon). As $n \to \infty$, the arcs flatten onto the strip floor — the picture-level Archimedean exhaustion.

The $n$-cir sibling picture — bend the strip the other way and the corners converge to the pseudo-Chebyshev nodes on the incircle — is in the same note. Here we stay on the un-inverted side.

## Strip-area calculation

The area of the strip *below* the $n$-gon arcs admits a closed form. Each arc is $y = \sec(2\pi(x - k/n)) - 1$ on $x \in [(2k-1)/(2n),\, (2k+1)/(2n)]$. By symmetry it suffices to integrate one arc and multiply by $n$.

$$
\int_{-1/(2n)}^{1/(2n)} \bigl(\sec(2\pi x) - 1\bigr)\,dx
\;=\;
\frac{1}{\pi}\,\ln\bigl(\sec(\pi/n) + \tan(\pi/n)\bigr) - \frac{1}{n}.
$$

The integral of $\sec$ is the Mercator latitude formula; equivalently $\sec u + \tan u = \tan(\pi/4 + u/2)$, so the right-hand side can be written as $\tfrac{1}{\pi}\ln\tan(\pi/4 + \pi/(2n)) - 1/n$.

Multiplying by $n$ (one arc per position) and subtracting from the strip's total area $1$:

$$
\boxed{\,A_{\text{above}}(n) \;=\; 2 \;-\; \frac{n}{\pi}\,\ln\bigl(\sec(\pi/n) + \tan(\pi/n)\bigr).\,}
$$

Equivalently $A_{\text{above}}(n) = 1 - A_{\text{below}}(n)$ with $A_{\text{below}}(n) = (n/\pi)\ln(\sec(\pi/n) + \tan(\pi/n)) - 1$.

**Sample values.**

| $n$ | $A_{\text{below}}(n)$ | $A_{\text{above}}(n)$ |
|---:|---:|---:|
| 3 | $(3/\pi)\ln(2 + \sqrt 3) - 1 \approx 0.258$ | $\approx 0.742$ |
| 6 | $(6/\pi)\ln\sqrt 3 - 1 \approx 0.049$ | $\approx 0.951$ |
| 12 | $\approx 0.011$ | $\approx 0.989$ |

**Asymptotics.** Expand in $u = \pi/n$:

$$
\sec u + \tan u = 1 + u + \tfrac{1}{2}u^2 + \tfrac{1}{3}u^3 + O(u^4),
$$

whence $\ln(\sec u + \tan u) = u + \tfrac{1}{6}u^3 + O(u^5)$, and

$$
A_{\text{below}}(n) \;=\; \frac{n}{\pi}\Bigl(\frac{\pi}{n} + \frac{1}{6}\frac{\pi^3}{n^3} + \cdots\Bigr) - 1 \;=\; \frac{\pi^2}{6\,n^2} + O(n^{-4}).
$$

So $A_{\text{below}}(n) \downarrow 0$ at rate $\pi^2/(6n^2)$, and the strip-area above the arcs fills the strip at the same rate. This is Eudoxus's proposition quantified in the strip chart: the circumscribed $n$-gon's excess over the incircle — in strip coordinates — vanishes like $1/n^2$.

The physical annulus-area twin (area between the $n$-gon and the incircle, measured in the actual plane) is $n\tan(\pi/n) - \pi = \pi^3/(3n^2) + O(n^{-4})$, same rate, different constant. Two charts on the same exhaustion.

## Why the memo is called what it's called

Eudoxus gives a ratio. Archimedes gives the value. Between Eudoxus and Archimedes there is a gap, and the gap is not automatically closable. The Mandelbrot set, the moving sofa, and the shapes that defeat us are reminders that Archimedes's move is a second, independent achievement — a proof of computability of the ratio, not a corollary of its existence. The strip-area calculation above is on the Archimedean side of the gap: we have the closed form because the shape is explicitly a secant arc. Had the shape been implicit, we would be stuck at Eudoxus.

## Addendum — Thomae / Stern–Brocot rhyme

There is a geometric linkage between the Archimedean-strip picture used here and the Thomae / Stern–Brocot histogram used elsewhere in the program. The two constructions are *not* the same — their coordinates, regularity, and underlying spaces differ — but they share an arithmetic substrate, and spotting the shared substrate is part of why Eudoxus remains bothersome even on the Archimedean side.

![Thomae popcorn on F_30](../figures/thomae_popcorn.png)

**Shared base.** Both constructions live over $[0, 1]$ with the *reduced-rational-with-denominator* as the organizing datum. Thomae plots a stem of height $1/q$ at each reduced $p/q$. The strip's floor $y = 0$ deposits a tangency point at every $k/n$ for $0 \le k < n$ and $n = 1, 2, 3, \ldots$; at a reduced rational $p/q$, exactly the $n$-gons with $q \mid n$ put a tangency there, giving multiplicity $\lfloor N/q \rfloor$ over $n \le N$ — which is the Thomae-popcorn height up to the $1/q$ normalization.

**The strip is a thickening of the Thomae plot.** Integrate the strip vertically and the floor-trace of the tangency lattice is the Thomae histogram. The strip adds one thing: the $n$-gon's secant arc, which smoothly connects adjacent tangencies $x = k/n$ and $x = (k+1)/n$ by rising to $y_n = \sec(\pi/n) - 1$ at the corner between them. Where Thomae has a vertical spike, the strip has a cluster of secant arcs passing through that point.

**Modality contrast.**

| | Thomae / Stern–Brocot | Archimedean strip |
|---|---|---|
| Direction | vertical stems | horizontal secant arcs |
| Height datum | $1/q$ (denominator rank) | $\sec(\pi/n) - 1$ (edge width) |
| At $p/q$ | one stem of height $1/q$ | $n$-gon arcs for every $n = q, 2q, 3q, \ldots$ pass through |
| Regularity | pointwise pathological — continuous at irrationals, discontinuous at rationals | smooth almost everywhere, with a countable lattice of vertices on the floor |

**Basel fingerprint on both sides.** The strip-area below one $n$-gon's arcs has leading term $\pi^2/(6 n^2)$, so its large-$n$ contribution is Basel-type. Thomae's natural Dirichlet moments are $\sum_{q \ge 1} \varphi(q)/q^s = \zeta(s-1)/\zeta(s)$ for $s > 2$. Both pictures therefore carry a zeta-function fingerprint, arriving from opposite directions — the strip via a Basel-type $1/n^2$ asymptotic over $n$, Thomae via Euler's product over reduced $p/q$. Same constant family, different derivations.

**What the linkage does and does not do.** It says the arithmetic object both constructions are tracking is *the denominator structure of rationals in $[0, 1]$*, with the multiplicity rule "$n$ hits $p/q$ iff $q \mid n$." Thomae reads that as a pointwise arithmetic function; the strip reads it as a smooth secant-arc tissue whose floor deposits match Thomae's stems. Two geometric expressions of the same combinatorial substrate. It does *not* say that theorems transport from one side to the other. The regularity classes are different, the natural moments are different, and a theorem proved about one side does not automatically cross. Any claim to information transfer between the two pictures has to be made separately and verified — the geometric linkage is a rhyme, not a bridge.

What the linkage does give us: any geometric statement about the strip that depends only on the tangency-point floor pattern is equivalently a statement about the same finite-window denominator-count histogram, and vice versa. The "outside-out" annulus picture, collapsed vertically down to the incircle, produces the same finite-window multiplicity histogram $\lfloor N/q \rfloor$ on reduced rationals that underlies the repo's Thomae-style popcorn picture. The closed-form strip area sits over the same rationals Thomae flags; the two pictures draw different shapes above that shared base.

**Why this is bothersome.** Eudoxus's gap between *a ratio exists* and *here is its value* is not the only gap of its kind. Two geometric constructions that rhyme arithmetically need not admit an information-passing bridge, and the strip / Thomae pair is an example: the same combinatorial substrate, two different analytic expressions, no automatic transport. Archimedes had to name $\pi$ separately from Eudoxus's ratio statement; anyone hoping to use the strip's closed form to constrain Thomae (or vice versa) has to do comparable work. The rhyme invites the question; the question does not come with its answer. That will matter when we return to the strip and the Thomae plot under the program's triad — the rhyme is where a claim of $F$-transport would sit, and the gap is where such a claim would have to be established, not assumed.

## Addendum — Regularity as $n \to \infty$

The two constructions move in opposite directions on regularity, even though they share the same rational-denominator base.

**Thomae: regularity degrades.** The finite-$N$ truncation $f_N(p/q) = 1/q$ for $q \le N$ (and $0$ elsewhere) is discontinuous at a *finite* set of rationals and continuous everywhere else. As $N$ grows, every new rational acquires its stem, and the discontinuity set densifies. In the pointwise limit, Thomae is discontinuous on the full dense set of rationals. The stems themselves never shrink: once the stem at $p/q$ appears (at $N = q$), it persists at height $1/q$ for every subsequent $N$. What accumulates in the limit is the *density* of discontinuities, not their flattening.

**Strip: regularity improves.** Each $n$-gon contributes $n$ secant arcs, $C^\infty$ on the interior with corner joints at the $n$ vertices. As $n$ grows, every arc's maximum height $y_n = \sec(\pi/n) - 1 \sim \pi^2/(2 n^2)$ shrinks, and every arc's derivatives at every interior point shrink too. The arc tissue flattens *uniformly* onto the strip floor. In the pointwise limit, the decoration disappears and only the smooth line segment $y = 0$ remains — literally the incircle.

**Why the asymmetry.** Thomae's height datum is $1/q$ — a function of each rational's *denominator*, fixed in the resolution parameter. The strip's height datum is $\sec(\pi/n) - 1$ — a function of the *polygon order* $n$, vanishing as $n \to \infty$ by Archimedes. Since both constructions share the same tangency-point base on the floor, the two decorations respond to the limit oppositely: Thomae accumulates unflattenable spikes, the strip flattens its arcs to nothing.

**Shared Diophantine envelope.** The rate at which the strip's upper envelope

$$
E_N(x) \;=\; \min_{n \le N,\, k} \bigl(\sec(2\pi(x - k/n)) - 1\bigr)
$$

approaches $0$ at each $x$ is governed by the best rational approximation error

$$
\delta_N(x)=\min_{n \le N,\;k}\left|x-\frac{k}{n}\right|.
$$

Near the strip floor,

$$
\sec(2\pi\delta)-1 = 2\pi^2\delta^2 + O(\delta^4),
$$

so

$$
E_N(x)=2\pi^2\,\delta_N(x)^2 + O\!\bigl(\delta_N(x)^4\bigr).
$$

In particular, badly-approximable $x$ give $E_N(x)$ on the order of $N^{-4}$, while Liouville $x$ can force faster decay along subsequences. The same Diophantine machinery appears on the Thomae side in how small-denominator rationals cluster near $x$ at each window. The rate structure is shared; the limit behavior is not.

**Upshot for the rhyme.** The Thomae picture's limit is pointwise pathological. The strip picture's limit is pointwise smooth — it degenerates to its floor. The two constructions start from the same rational-denominator lattice and end in incompatible regularity classes. This is the concrete reason the rhyme does not automatically transport theorems: a $C^\infty$ statement about the strip's limit and a pointwise-discontinuity statement about Thomae's limit live in different function-space habitats, even though they track the same underlying combinatorics. Any $F$-transport claim between the two has to cross that habitat boundary on purpose, not by default — and this memo does not make such a claim; it flags the boundary where one would have to.
