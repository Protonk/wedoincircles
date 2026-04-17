# ARCHIMEDEAN-CONSTRICTION

A BIND move. The Archimedean strip is used as a geometric substitute that binds around the Stern–Brocot / Thomae object without engaging it. The obstruction is not handled; it is constricted. Erasure holds throughout: no primitive from the S–B / Thomae family enters the operative vocabulary.

Companion to `BNHA/triad/Eraserhead/BIND-THE-CIRCLE.md`. The linkage that motivates the move is articulated in `BNHA/triad/Lemillion/BOTHERSOME-EUDOXUS.md` (the rhyme and its regularity opposition); the geometric objects used are in `n-gons/ARCHIMEDEAN-STRIP-FLIP.md`.

---

## What is refused

Per `BNHA/triad/Eraserhead/BIND-THE-CIRCLE.md`'s Erasure list:

- Minkowski `?(x)`.
- The Stern–Brocot tree, Farey sequences, Farey neighbors, mediant geometry.
- The Thomae / popcorn function. In particular: the height law `f(p/q) = 1/q` at reduced rationals, and its pointwise regularity profile.
- Denjoy's construction; dyadic expansions reinterpreted as continued fractions.
- Reduction of a rational `k/n` to lowest terms `p/q` when that reduction is the operative step, i.e. when the argument depends on the denominator `q` as an arithmetic object rather than on `n` as a geometric parameter.

These primitives are not merely absent from the statement; they are absent from every operative step. If any of them re-enters, the derivation has left BIND and restarts.

## What is used

Circle-side geometric primitives, from `BNHA/triad/Eraserhead/BIND-THE-CIRCLE.md`'s allowed list:

- Regular polygons circumscribed around a fixed unit incircle; the shared anchor edge; the tangency at `(1, 0)`.
- Position `k` of the `n`-gon at angle `2πk/n`, labeled by the unreduced pair `(k, n)`.
- The incircle as the fixed inner boundary; the 3-cir (the `n = 3` circumscribed circle) as the fixed outer boundary.
- Angular widths `π/n`; secant half-edges; the polar equation `r = sec(θ - 2πk/n)` of a straight edge tangent to the incircle.
- The unroll `x = θ/(2π)`, `y = r - 1` that maps the annulus `{1 <= r <= 2}` to the flat strip `[0, 1]^2`.
- The integral `∫ sec = ln|sec + tan|`.

No arithmetic function of the denominator appears. No depth function on a binary tree appears. No limiting process that invokes reduction to lowest terms appears.

## Three Strip-Side Objects

The strip naturally offers three different geometric objects. They are not interchangeable.

### 1. The arc family

For each `n >= 3` and each edge label `k = 0, ..., n-1`, define the edge interval

$$
I_{n,k}=\left[\frac{2k-1}{2n},\,\frac{2k+1}{2n}\right] \pmod 1
$$

and the corresponding strip arc

$$
y_{n,k}(x)=\sec\!\left(2\pi\!\left(x-\frac{k}{n}\right)\right)-1,
\qquad x \in I_{n,k}.
$$

Taken together, these arcs are the full `n`-gon tissue on the strip.

### 2. The peak-height sequence

Each arc reaches its maximum at the endpoints of its interval, namely

$$
h_n=\sec(\pi/n)-1.
$$

This is the clean scalar that measures geometric flattening of the `n`-gon in the strip.

### 3. The area functional

The total strip area below the `n` arcs is

$$
A_{\mathrm{below}}(n)=
\sum_{k=0}^{n-1}\int_{I_{n,k}} y_{n,k}(x)\,dx.
$$

By symmetry this is one arc integral times `n`.

## Choice Of Operative Object

We proceed to examine the area functional as our operative BIND object, reaching for peak height where appropriate. We do not fully understand the scope and richness of the arc family well enough to use it to bind.

This choice is deliberate.

- The arc family is too rich: it is a genuine geometric tissue over `[0,1]`, and at present BIND does not have a controlled way to say exactly which of its properties are load-bearing and which are incidental.
- The peak height is useful, but too thin by itself: it records flattening, not the whole geometric computation.
- The area functional is the BIND-sweet spot for the present note: it is geometric, closed-form, and computable from strip primitives alone.

## The Operative Substitution

The erased S–B / Thomae object uses a denominator-indexed decoration on a rational floor. BIND does not reproduce that decoration. It inherits only the floor as positional data: the tangency deposits at `x = k/n`, labeled by unreduced `(k, n)`.

The substitute is therefore not a pointwise height law. It is the strip-side area functional

$$
A_{\mathrm{below}}(n),
$$

with the peak-height sequence

$$
h_n=\sec(\pi/n)-1
$$

as supporting geometric evidence of flattening.

That is the constriction: keep the same floor, refuse the erased height law, and move to a BIND-legal geometric functional that lives entirely on the strip side.

This does **not** establish that `A_{\mathrm{below}}(n)` is the right circle-side object for the larger program. It establishes something narrower: `A_{\mathrm{below}}(n)` is a circle-side object that is BIND-legal, geometrically native, and computable in closed form. Showing that it is the right object, or even a sufficient one, is future work.

## What This Achieves, At BIND-Legal Precision

Computing in the strip, using only the primitives above, one obtains

$$
\int_{-1/(2n)}^{1/(2n)} \bigl(\sec(2\pi x)-1\bigr)\,dx
=
\frac{1}{\pi}\ln\bigl(\sec(\pi/n)+\tan(\pi/n)\bigr)-\frac{1}{n},
$$

and multiplying by `n` gives

$$
A_{\mathrm{below}}(n)
=
\frac{n}{\pi}\ln\bigl(\sec(\pi/n)+\tan(\pi/n)\bigr)-1.
$$

Expanding at large `n`,

$$
A_{\mathrm{below}}(n)=\frac{\pi^2}{6n^2}+O(n^{-4}).
$$

This is the Archimedean exhaustion in closed form, produced without invoking Thomae's height, the denominator `q`, or any reduction step. The only arithmetic in view is integer arithmetic on `n` and `k`; no arithmetic function of `q` has been summoned.

The supporting peak-height statement is

$$
h_n=\sec(\pi/n)-1=\frac{\pi^2}{2n^2}+O(n^{-4}),
$$

so the secant tissue itself flattens geometrically. We use this only as support. The operative BIND object remains `A_{\mathrm{below}}(n)`.

## The Constriction

The erased side is left erased. This note does not analyze it; it declines to summon the primitives that would make that analysis possible.

The strip object chosen here has a clean BIND-legal profile at the level of the operative object:

- `A_{\mathrm{below}}(n)` is defined without reduced denominators.
- `A_{\mathrm{below}}(n)` has a closed-form expression.
- `A_{\mathrm{below}}(n) \to 0` at the explicit Archimedean rate `\pi^2/(6n^2)`.

The BIND move is therefore:

1. **Inherit** the tangency floor as positional data.
2. **Refuse** the erased height law and every derivation that depends on it.
3. **Substitute** the strip-side area functional `A_{\mathrm{below}}(n)` as the operative geometric object.
4. **Use** the peak height `h_n` only as supporting flattening evidence.
5. **Decline** to use the full arc family as the binding object, because its scope is not yet sufficiently understood.

This is constriction: the shared floor is retained, the erased vocabulary is not reintroduced, and a computable geometric object is produced without crossing back into the refused language.

## Why "Archimedean"

Archimedes' method of exhaustion constricts the circle between inscribed and circumscribed polygons, identifying the circle's area by squeezing from both sides without ever writing down a non-geometric primitive. BIND's move here is the same shape of operation, one level up: constrict the rational-lattice decoration on the circle between the strip's geometric functionals above and the incircle below, identifying a vanishing quantity by squeezing geometrically, without ever writing down a non-geometric primitive about rationals.

The classical Archimedean constriction dodges irrationality (of `π`) by staying in polygon-area arithmetic. The present Archimedean constriction dodges the erased denominator obstruction by staying in strip geometry. Same shape.

## What This Does Not Claim

- This memo does not claim that the erased S–B / Thomae object is dispensable in general. Other work, outside BIND, may engage it. BIND only claims it can be bound around in this specific computation.
- This memo does not claim the strip flattens Thomae. The strip and Thomae have different limit behavior; that was the point of `BNHA/triad/Lemillion/BOTHERSOME-EUDOXUS.md`.
- This memo does not claim the full arc family is now understood. On the contrary: the note explicitly declines to use it as the operative binding object.
- This memo does not claim that `A_{\mathrm{below}}(n)` has already been shown to be the right circle-side object for the whole program. What is shown here is narrower: it is BIND-legal and computable. Whether it is the right object is a separate achievement still to be obtained.
- This memo does not claim to prove a `π`-side computational-impossibility statement of the Landfall shape. BIND clears the vocabulary in which such a statement could later be posed on the strip. Whether the statement actually holds is a separate question.

## What This Unlocks For The Program

The question at the end of the speculative discussion in `BNHA/triad/Lemillion/BOTHERSOME-EUDOXUS.md` is whether the circle side admits a computational-closure-and-aggregation impossibility consonant with Landfall's log-side one. This note does not settle which circle-side object should carry that question. It shows only that the strip, and more specifically the area functional `A_{\mathrm{below}}(n)`, is an available BIND-legal candidate.

This does not answer the question. It does not even prove that the candidate chosen here is the right one. What it does is narrower and still useful: it produces a poseable candidate surface using allowed primitives. That is the only thing BIND is meant to do at this stage: clear the vocabulary, leave the further selection and proof work to be done on allowed objects, and mark precisely what has been refused and what has been kept. The refusal is the discipline; the constriction is the result of keeping the discipline.

## Addendum — The 3DT reading

Strip the `n`-cir sizes away from the construction — the radii `sec(π/n)` and the circumscribed-polygon areas — and what remains is a point (the anchor), a circle, and a family of rotations by `2π/n`. Each `n`-gon's tangency set is exactly the orbit set of the anchor under rotation by `2π/n`: in normalized coordinates it is

$$
\left\{0,\frac1n,\frac2n,\dots,\frac{n-1}{n}\right\}\subset \mathbb R/\mathbb Z.
$$

That is verbatim the Three-Distance Theorem setup — point, rotation, iteration on `S¹` — with one specific choice: the rotation angle is the rational `1/n`.

The 3DT states that the orbit of a rotation after `N` iterations partitions the circle into at most three distinct gap lengths. For the rational rotation `1/n`, the distinct orbit set consists of `n` equally spaced points, hence `n` equal gaps of length `1/n`. The three possible gap sizes collapse to one. So the anchored `n`-gon is the degenerate rational slice of 3DT: equal spacing is exactly the 3DT output at that instance.

Sweeping `n` therefore produces the equally spaced orbit sets coming from the rational rotations `1/n`, and more generally every reduced rational rotation `p/n` has the same underlying `n`-point set, though with a different cyclic visitation order. In that sense the anchored `n`-gons capture the rational equal-gap slice of the rotation picture, but not the full order data of every rational orbit.

The irrational case is different. For irrational `α`, the first `N` points of the orbit of rotation by `α` produce the non-degenerate 3DT instance, with up to three distinct gap lengths. Continued-fraction convergents `p_k/q_k` are relevant there as analysis tools: they control and organize the gap structure of the irrational orbit. But the closed rational orbit of `p_k/q_k` is still an equally spaced `q_k`-point set, not the non-degenerate irrational 3DT object itself. So the relation is:

- rational anchored `n`-gons give the degenerate equal-gap slice;
- irrational 3DT gives the non-degenerate gap picture;
- convergents link the two analytically, without identifying one with the other.

### BIND-legality

The lattice-geometric proof of 3DT via Marklof–Strömbergsson 2017, operating in `Γ\SL(2, ℝ)` with `Γ = SL(2, ℤ)`, is on the allowed-primitives list of `BNHA/triad/Eraserhead/BIND-THE-CIRCLE.md`. Reading the anchored `n`-gon construction through 3DT is therefore a BIND-native frame: the family of anchored rational-rotation orbits at all resolutions can be discussed without importing Minkowski `?(x)`, Stern–Brocot, Farey, Thomae, or Denjoy.

### Two BIND-legal frames on the same object

The anchored `n`-gon construction now carries two native BIND readings:

1. **Archimedean frame.** The `n`-gon circumscribes the incircle; its sec-indexed circumscription shrinks geometrically; the area functional `A_below(n)` closes in `∫ sec` and vanishes at rate `π²/(6n²)`. This is the frame the main body of this note develops.

2. **3DT frame.** The `n`-gon is the equally spaced orbit set of a rational rotation; the family sweeps the rational equal-gap slice of the rotation picture; the full irrational 3DT is the non-degenerate companion problem analyzed on the same circle side. Lattice-geometric in `Γ\SL(2, ℝ)` via Marklof–Strömbergsson.

Both frames describe the same construction, and neither imports any erased primitive. They do not collapse into each other: the Archimedean frame is about area and exhaustion; the 3DT frame is about orbits and gaps. Their independence inside BIND is itself informative. Two distinct primitive-sets can speak about the anchored `n`-gon without reaching for shared vocabulary.

### What this does not add

- Neither frame proves the `π`-side computational-impossibility statement this program eventually wants.
- Neither frame by itself shows the anchored `n`-gon is the "right" circle-side object for the larger question. Both are BIND-legal candidate surfaces.
- The relationship between the two frames — whether they should be treated as one object from two angles, or as two readings that happen to coincide on this construction — is not settled here. It is a question that could go to Creati if and when either frame's catalog-level content is written down.

What the addendum adds is narrower and useful: the construction has a second BIND-legal reading independent of the first. Independence of readings inside BIND is a guard against the single-frame math-error failure mode. The same construction reached twice through disjoint primitive-sets is harder to be wrong about than the same construction reached once.

## Footer: Where This Probably Goes Next

Three ambiguities remain visible here:

- whether the "same floor" relation can be made sharp enough to carry real geometric weight without silently reimporting erased vocabulary;
- whether the arc family has stable, saturated structure worth naming beyond the area functional and peak height;
- whether `A_{\mathrm{below}}(n)` is merely a BIND-legal candidate or can be shown to be the right circle-side object for later closure / obstruction work.

These are probably not Aizawa's jobs alone.

- For the richer strip geometry and the arc family as a watched object, look toward Lemillion in `BNHA/triad/Lemillion/PERMEATE-THE-CIRCLE.md`.
- For the moment when any part of that geometry becomes exact enough to enter the catalog as a count, closed form, identity, or named obstruction, look toward Creati in `BNHA/triad/Creati/CREATI-THE-CIRCLE.md`.

This footer is only a handoff marker. It does not assign future results in advance; it marks where to look when this note's preparatory work has to be taken further by a different discipline.
