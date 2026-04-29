# FOR-BREAKFAST

![A two-panel figure titled "The reduction collapse: k/n → p/q many-to-one from the integer lattice to reduced rationals." Top panel: scatter plot with horizontal axis x = k/n ∈ [0, 1] and vertical axis "polygon order n" running from 2 at the bottom to 30 at the top. About 435 small dots in two colors — blue for gcd(k, n) = 1 (already reduced) and orange for gcd(k, n) > 1 (collapses on reduction). Dots form curving rows at each n level. Vertical pale-purple bands at x = 1/2, 1/3, 2/3 with a pale-teal band at x = 1/29; annotations at top read "1/2: 15→1", "1/3: 10→1", "2/3: 10→1", and "1/29: 1→1 (lossless)". Center divider: bold italic label "the reduction step k/n → p/q (the operative arithmetic step BIND-Erasure refuses)". Bottom panel: Thomae popcorn at the same Farey horizon N = 30 — vertical stems at every reduced p/q with q ≤ 30, height 1/q, tallest stem at x = 1/2 reaching y = 0.5. Subtitle: "Same Farey horizon N = 30. Integer lattice: 435 distinguishable (k, n) points. Reduced popcorn: 277 stems. Collapse ratio at p/q is ⌊N/q⌋ → 1."](../figures/reduction_collapse.png)

*The frontispiece is the boundary as an operation: the reduction
`k/n → p/q`. Top panel — the integer-sample regime, where each pair
`(k, n)` is its own object. Bottom panel — Stern-Brocot land, where
the same data has been reduced and decorated by `1/q` (Thomae's
popcorn). The middle label names what the program refuses as an
operative arithmetic step. Full tour at §The reduction step.*

The substrate has algebraic-arithmetic rigidity at integer samples.
The program's operative apparatus stays inside that regime by
construction. The instant the samples aren't integer, you are in
Stern-Brocot land, and an unruly fractal construction there eats
measure for breakfast.

This memo is a sensitizer. The fact above is deeply embedded in the
repo — in BIND-Erasure, in the §5 substrate-side typing, in the
bounded-coefficient cost model, in the unreduced `(k, n)` labelings,
in the careful refusal to engage the denominator `q` as an arithmetic
object. It is rarely stated directly, and an agent (human or
otherwise) reading the repo for the first time encounters it only as
a distributed pattern across many files. The purpose of this memo is
to state it once, with operative content, so future workers recognize
the regime boundary when they meet it.

## The two regimes

**Integer-sample regime.** Samples are labeled by integers `(k, n)`.
Vertex `k` of polygon `n`, position `k` of `(ℤ/nℤ)*`, the
integer-iterate orbit `{kα mod 1}`, the `n`-th cyclotomic field, the
`m ≡ 1 mod n` Fourier lattice. Algebraic-arithmetic structure is
*rigid*: cosines lie in named cyclotomic subfields with computable
degrees `φ(n)/2`; integer-matrix determinants are bounded below by
`1` or zero; divisibility tests are exact; coincidences are forbidden
by cyclotomic-rigidity arguments. Measure-theoretic typing applies
cleanly because integer indexing makes counting, Haar on `(ℤ/nℤ)*`,
Lebesgue on integer-iterate orbits, and the L-W null/full dichotomy
all well-defined.

**Stern-Brocot land.** Rationals get reduced to lowest terms `p/q`
and the denominator `q` becomes the operative arithmetic object.
Stern-Brocot organizes rationals by depth; Thomae decorates them by
`f(p/q) = 1/q`; Minkowski's `?(x)` maps the dyadic tree to the Farey
tree; Denjoy re-reads dyadic expansions as continued fractions. The
machinery is fractal — pointwise discontinuous on a dense set,
singular as a measure, generically eating Lebesgue measure of the
sets it lives on. Cyclotomic rigidity fails because the continuum
offers infinitely many close-but-not-equal candidates; pigeonhole
forces multiplicity at any positive resolution.

The regime boundary is *the line where the reduction `k/n → p/q`
becomes the operative arithmetic step*. Above the line, you label
`(k, n)` unreduced and the rigidity holds. Below the line, `q` is
what the argument turns on, and you have crossed.

## Where the rigidity lives in the repo

The portrait, then three witnesses in the program's native vocabulary.

### The picture

![A wide strip plot titled "Strip Linkage | floor grid and special corner contours". Horizontal axis "strip angle u = θ/(2π)" from 0 to 1, with vertical dashed reference lines at 1/4, 1/2, and 3/4. Vertical axis "strip height y = r − 1" from 0 up to about 1. A hatched gray "DH-grid band" runs along the floor with twelve evenly spaced vertical dashes. Six dashed horizontal level lines mark polygon heights y_n = sec(π/n) − 1 for n = 3, 4, …, 8. A scatter of small black dots labeled "corner / tangency point" sits on the floor at positions x = k/n and at the polygon levels at positions x = (2k+1)/(2n). Five colored contour curves rise from the floor to the top of the strip: red curves labeled X = +1 near the right and left edges, orange curves X = +1/2 just inside them, blue curves X = -1/2 mirroring on the other side, two red curves X = -1 around u = 1/2, and dashed black vertical lines labeled X = 0 at u = 1/4 and 3/4. A legend at the upper right enumerates the five contour colors and the marker types.](../figures/counting_strip_observables.png)

Read the figure as a portrait of the integer-sample regime in one
panel. The strip is the unrolled annulus between the unit incircle
(at strip height `y = 0`) and the circumscribed `n = 3`-cir (at the
top). Horizontal axis: strip angle `u = θ/(2π) ∈ [0, 1)`, identified
at the endpoints. Vertical axis: strip height `y = r − 1`. Six
polygons `n = 3, 4, …, 8` are drawn; each contributes `n` floor
tangencies and `n` corner vertices.

Three integer-sample objects sit on the strip.

1. **Floor tangencies at `x = k/n`.** Black dots on the floor for
   each `(k, n)` with `0 ≤ k < n`. Labeled by the unreduced pair
   per ARCHIMEDEAN-CONSTRICTION's discipline; reduction to lowest
   terms is refused at the operative-step level. Each tangency is
   an integer-indexed sample of the circle.

2. **The DH-grid band.** Hatched at the floor with vertical dashes
   at the multiples of `1/DH` (here `DH = 12`). This is the integer
   divisibility lattice of N-GON-WHOLENESS: the test `b_n = 𝟙[n | DH]`
   reads whether *every* tangency of polygon `n` lands on the grid.
   Integer arithmetic; `q` does not appear.

3. **Corner points at `x = (2k+1)/(2n)`, `y = sec(π/n) − 1`.** Black
   dots at the polygon levels. The horizontal coordinate is
   integer-indexed; the vertical coordinate lives in the totally
   real cyclotomic field `K_n = ℚ(cos(2π/n))` of degree `φ(n)/2`.
   Each corner is an algebraic-arithmetic point with an
   integer-indexed signature.

The colored contours are level sets of the planar crystallographic
observable

```text
X(u, y) = (1 + y) · cos(2πu)
```

at the Niven / crystallographic values `X ∈ {+1, +1/2, 0, −1/2, −1}`.
The contour `X = c` traces the locus where a polygon corner could
land on the rational value `c`: it parametrizes
`r = (1 + y) = c / cos(2πu)`, restricted to the strip's vertical
range. The backbone `X ∈ {+1, 0, −1}` is where rigid coincidences
between corners and contours actually occur; `X = ±1/2` is plotted
as a tested but empty comparison family.

Per the wider numerical search recorded at
[n-gons/counting/COUNTING-AND-STRIP.md](n-gons/counting/COUNTING-AND-STRIP.md),
no exact corner-on-`X = ±1/2` hit appears through `n = 400`. The
absence is not coincidence; it is cyclotomic rigidity. The corner's
height `sec(π/n)` is algebraic of degree `φ(2n)/2` over `ℚ`, and
forcing `(1 + y) cos(2πu) = ±1/2` at `(u, y) = ((2k+1)/(2n),
sec(π/n) − 1)` would require an algebraic-arithmetic coincidence the
integer-sample regime forbids generically. The same rigidity
forbids the THICK-SWEEP thin sweep from hitting two corners at once.

Two readouts coexist on the same strip:

- **Floor readout (commensurability).** The DH-grid band tests
  whether tangency `(k, n)` lands on the integer-divisibility
  lattice. Pure integer arithmetic. Floor-side, subpolygon question.
- **Corner readout (incidence).** The contour family tests whether
  corner `(k, n)` lands on the crystallographic backbone. Pure
  cyclotomic algebra. Corner-side, counting question.

Both readouts operate on integer-indexed objects — `(k, n)`
unreduced — and both refuse Stern-Brocot vocabulary at the operative
level. The strip is what BIND-legal apparatus looks like in one
picture: hatched band, tangencies, corners, crystallographic
contours — all integer-sample objects under their respective
measure-theoretic readings.

What is *not* in the figure: no Stern-Brocot tree, no Farey
neighbors, no Thomae height law `f(p/q) = 1/q`, no Minkowski `?(x)`
decoration, no reduction `k/n → p/q` with `q` as the operative
arithmetic object. The discipline shows by absence. The same point
set under a Stern-Brocot reading is preserved separately at
`n-gons/stern_brocot.sage` per N-GON-WHOLENESS §7, but it is not
the operative vocabulary here.

The figure is the integer-sample regime in one panel. The three
witnesses below anatomize it.

### THICK-SWEEP — the boundary

[n-gons/counting/THICK-SWEEP.md](n-gons/counting/THICK-SWEEP.md).
A *thin* sweep through the strip vertex tissue at slope `s = 1/√3`
hits at most one vertex per line,
even as `N → ∞`. The sweep coordinate
`c_{n,k} = sec(π/n) − 1 − s · (2k+1)/(2n)` lives in the totally real
cyclotomic field on the left and `s · rational` on the right; exact
coincidences are forbidden by cyclotomic algebraic rigidity, and
empirically the closest pair through `N = 100` sits at `c`-distance
`≈ 1.4 × 10⁻⁷` but is *never zero*. A *thick* sweep with any positive
bandwidth `δ > 0` eats the rigidity instantly: the sweep coordinates
lie in an interval of length `L = 1 + s` and there are
`N(N+1)/2 − 3` of them; pigeonhole gives
`min gap ≤ 2(1+s)/(N(N+1) − 8)`, falling below any `δ` for `N` large.
Both sides are visible in one note: cyclotomic rigidity above the
line, continuum-pigeonhole collapse the moment you cross.

### ARCHIMEDEAN-CONSTRICTION — the discipline

[BNHA/triad/Eraserhead/ARCHIMEDEAN-CONSTRICTION.md](BNHA/triad/Eraserhead/ARCHIMEDEAN-CONSTRICTION.md).
Operative move: keep the tangency floor at `x = k/n` *labeled by
unreduced `(k, n)`* and refuse every operative step that would
reduce to lowest terms. The
strip-side area functional
`A_below(n) = (n/π) ln(sec(π/n) + tan(π/n)) − 1 = π²/(6n²) + O(n⁻⁴)`
is the BIND-legal substitute for whatever Stern-Brocot/Thomae
machinery would compute the same exhaustion: closed-form,
integer-`n`-indexed, never engaging `q`. Quoted from the note:

> If any of `[Stern-Brocot, Farey, Thomae, Denjoy, reduction k/n →
> p/q when q is operative]` re-enters, the derivation has left BIND
> and restarts.

That is the discipline holding the regime against silent contamination.

### N-GON-WHOLENESS — apparatus on the rigid side

[n-gons/N-GON-WHOLENESS.md](n-gons/N-GON-WHOLENESS.md). Positions
are labeled `(k, n)`; the divisibility test `b_n = 𝟙[n | DH]` is
integer arithmetic; histogram heights at `p/q` are `⌊N/q⌋` (integer);
the binary sequence lives entirely on integer indexing. The
Stern-Brocot reading is preserved separately at
`n-gons/stern_brocot.sage` and explicitly *not* the operative
vocabulary. Same data, two readings; only the integer-rigid one is
operative.

### The depth stratification

The strip portrait shows integer-sample objects geometrically. The
ψ-stratification figure shows their algebraic depth.

![A single-panel scatter plot titled "ψ-stratified x-support of the outside-out corner sweep" with subtitle "Focus: the n = 7 first-cubic row and the tested-empty rational guides at x = ±1/2". Horizontal axis "vertex x-coordinate" running from −2 to +1; vertical axis "polygon order n" running from 3 at the bottom to 40 at the top. One row per polygon order, populated by small colored dots at x_{n,k} = sec(π/n)·cos((2k+1)π/n). A legend at upper left names five ψ(n) classes: red ψ = 2, orange ψ = 4, gold ψ = 6 marked "first cubic, n = 7", teal ψ ∈ {8, 10, 12}, muted slate ψ ≥ 14. A pale gold band highlights the row at n = 7 with an arrow annotation reading "first cubic row" and a left-side row label "n = 7 witness". Four vertical guides cut through the scatter: solid red at x = +1, solid blue at x = −1, dashed black at x = 0, and dashed orange at x = ±1/2 with "empty guide" labels at the top. A footer line records the construction n ∈ [3, 40], the formula x_{n,k} = sec(π/n)·cos((2k+1)π/n), and the verification through n ≤ 400 with closest approaches gap ≈ 1.5 × 10⁻⁵ at n = 399 for +1/2 and gap ≈ 2.3 × 10⁻³ at n = 398 for −1/2.](../figures/counting_psi_stratification.png)

This is the outside-out corner sweep, one row per polygon order
`n ∈ [3, 40]`, with each marker at the vertex x-coordinate
`x_{n,k} = sec(π/n) · cos((2k+1)π/n)`. Markers are colored by the
crystallographic-restriction value `ψ(n)`. The companion memo is
[n-gons/counting/PSI-STRATIFICATION.md](n-gons/counting/PSI-STRATIFICATION.md);
the script is `n-gons/counting/build_psi_stratification.py`.

Five ψ-strata sort the polygon orders by algebraic depth:

- **ψ = 2 (red)** — the Bravais orders `n ∈ {3, 4, 6}`. Entirely
  rational vertex x-coordinates; sit entirely on the backbone
  `x ∈ {−2, −1, 0, +1}`.
- **ψ = 4 (orange)** — `n ∈ {5, 8, 10, 12}`. First quadratic
  trace-field class.
- **ψ = 6 (gold)** — `n ∈ {7, 9, 14, 18}`. First *cubic* trace-field
  class. The highlighted row at `n = 7` is the first polygon whose
  vertex x-coordinates live in a degree-3 totally real cyclotomic
  field — equivalently, the first non-constructible regular polygon
  (Gauss-Wantzel).
- **ψ ∈ {8, 10, 12} (teal)** and **ψ ≥ 14 (slate)** — the
  higher-depth tail.

The vertical guides carry the planar backbone structure: `x = +1`
(every polygon's anchor tangent), `x = −1` (every even polygon's
anti-tangent), `x = 0` (every `n ≡ 2 mod 4`), `x = −2` (only `n = 3`).
The orange dashed guides at `x = ±1/2` carry the **tested-empty**
diagnostic: no polygon vertex through `n ≤ 400` lands on either,
with closest approaches `gap ≈ 1.5 × 10⁻⁵` at `n = 399` for `+1/2`
and `gap ≈ 2.3 × 10⁻³` at `n = 398` for `−1/2`. The picture's
footer records the verification.

The ±1/2 guides are the cyclotomic rigidity in its purest pictorial
form. The points `x = ±1/2` are rational; nothing about the
geometry forbids hitting them; every polygon has rational `(2k+1)`
and rational `2n`. But forcing
`sec(π/n) · cos((2k+1)π/n) = ±1/2` requires an algebraic-arithmetic
coincidence between a sec-factor in `K_n = ℚ(cos(2π/n))` of degree
`φ(n)/2` and a cosine value forced by the integer pair `(2k+1, n)`,
and the cyclotomic ladder forbids it generically. The empty guides
are *the same fact* as THICK-SWEEP's "thin sweep never hits two at
once," shown as a vertical refusal at named rationals rather than a
horizontal refusal of coincidence.

A note on the ψ choice. The outside-out corners' native depth is
`φ(n)/2 = [K_n : ℚ]`, the trace-field degree. That is the
integer-sample regime's own internal arithmetic ladder, and §5.4 of
the substrate-side typing names it as the counting-invariant face
of integer-sample rigidity. ψ is *not* that ladder. ψ is the
additive bridge function PERMEATE uses to compare circle-side depth
(multiplicative on prime-power parts through `φ`) to log-side depth
(additive in `v_p`); the coloring tells the reader the figure is
meant to be legible across the bridge. The trace-field depth is
what the figure structurally reflects when read through ψ.

What this adds to the sensitizer: the integer-sample regime has its
own algebraic stratification, and the strip portrait's
cyclotomic-rigidity content is what populates the strata. The
ψ = 2 backbone is where the rigidity allows rational coincidences;
ψ ≥ 4 is where the rigidity forbids new ones; the empty ±1/2 guides
are the rigidity making itself visible by *not* being hit. The
cyclotomic ladder `[K_n : ℚ] = φ(n)/2` of §5.4 is what this picture
makes pictorial. Inside the integer-sample regime, the depth grows;
the rigidity stratifies; and the rigidity forbids the generic
rational coincidences the Stern-Brocot side would have to fight a
fractal to even pose.

### The §5 typing as five faces of one rigidity

The §5 substrate-side typing at
[measure/SUBSTRATE-OBSTRUCTIONS.md](measure/SUBSTRATE-OBSTRUCTIONS.md)
is then read as five faces of one rigidity: Haar on integer-iterate
orbits; three non-nesting isoperimetric registers sharp on the
regular-`n`-gon family for integer `n`; Hurwitz Fourier on the
integer lattice `m ≡ 1 mod n`; cyclotomic ladder
`[K_n : ℚ] = φ(n)/2` indexed by integer `n`; L-W null/full at the
integer-arithmetic level. The five angles share a domain of validity
— the integer-sample regime — and their squeeze convergence on
`T(P)` is the convergence of five faces of one rigidity, not five
independent witnesses.

## The algorithm-side projection

The bounded/unbounded coefficient boundary in
[paper/IMPOSSIBILITY-OUTLINE.md](paper/IMPOSSIBILITY-OUTLINE.md)
§1.4 is the same regime boundary, read on the algorithm side.
Morgenstern's `Ω(n log n)` additive lower bound holds *under bounded
coefficients* because bounded `|λ|, |μ| ≤ c` keeps determinant volume
integer-bookkept: `det(integer matrix) ∈ ℤ`, modulus ≥ 1, each step's
volume-growth integer-anchored. Unbounded coefficients let the
algebra absorb continuum-structure into linear-combination weights;
the integer-volume floor disappears; the determinant argument
collapses. So bounded coefficients ↔ integer-bookkeeping rigidity ↔
inside the integer-sample regime; unbounded coefficients ↔ continuum
absorption ↔ Stern-Brocot side. `δ` at the bounded/unbounded
boundary is the algorithm-side coordinate for the same regime
boundary the §5 angles read on the substrate side.

The cyclotomic-ladder-vs-affine-closure asymmetry at
[memos/NATIVE-F-MINIMAL-DEFINITION.md](memos/NATIVE-F-MINIMAL-DEFINITION.md)
is the same fact in a third frame: `φ(n)/2` grows because `n` is
integer-indexed (each integer `n` opens a new real cyclotomic field);
`Aff⁺(ℝ)` is two-parameter flat because affine transformations are
continuum-parameterized. Integer-indexed depth on one side,
continuum-flatness on the other. Finite native operations cannot
bridge them, because crossing means leaving the regime where either
side has its rigidity.

## Diagnostics

Five signals that you may be at or across the regime boundary.

1. **You are reducing `k/n` to lowest terms `p/q` and arguing about
   `q`.** Per ARCHIMEDEAN-CONSTRICTION's discipline: if the argument
   depends on `q` as an arithmetic object rather than on `n` as a
   geometric parameter, the derivation has left BIND.

2. **You are summoning Stern-Brocot tree depth, Farey neighbors,
   Thomae heights, Minkowski `?`, Denjoy continued-fraction-from-
   dyadic, or related machinery.** Each is on the explicit BIND
   refusal list. Their appearance signals an argument trying to
   leverage structure that lives only on the Stern-Brocot side.

3. **You are allowing positive bandwidth in a sweep, continuum
   bandwidth in a coefficient, or non-integer `α` where an integer
   index was operative.** Each crosses an aspect of the regime
   boundary. The argument has to either keep that aspect
   non-load-bearing (so the integer-sample apparatus still applies)
   or commit to the Stern-Brocot side (in which case the program's
   measure-theoretic refusals do not transfer and the argument owes
   a different apparatus).

4. **The equation forces an exact coincidence between cyclotomic
   data and a continuum quantity.** Cyclotomic rigidity typically
   forbids the coincidence on the integer-sample side; on the other
   side the impossibility downgrades to pigeonhole approximation.
   THICK-SWEEP is the canonical witness for both behaviors in one
   note.

5. **The argument leans on Lebesgue measure of a set defined by
   continuum-rational decoration (denominator height, fractal depth,
   `?(x)`-derived density).** Ask whether the set is a fractal
   eating measure. Thomae, `?`, Stern-Brocot depth all generically
   have measure-theoretic pathology that the integer-sample
   apparatus avoids by construction.

If any signal fires, pause. Either rewrite the argument to stay on
the integer-sample side, or declare explicitly that the argument is
committing to the Stern-Brocot side and acknowledge that the
program's substrate-side discipline does not transfer there.

## What protects the regime

[BNHA/triad/Eraserhead/BIND-THE-CIRCLE.md](BNHA/triad/Eraserhead/BIND-THE-CIRCLE.md)
is the explicit discipline. Its refusal list — Minkowski `?(x)`,
Stern-Brocot tree, Farey-as-tree, Thomae's function, Denjoy's
construction, the operative reduction `k/n → p/q` — is exactly the
list of primitives that live on the Stern-Brocot side. The list is
not aesthetic. Each primitive is load-bearing on its side; any of
them re-entering an argument means the argument has crossed the
regime boundary.

The OLD-TIME-RELIGION content-not-calendar criterion at
[memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md) is a
sibling discipline on a different axis (post-1882 results don't
smuggle transcendence-theory machinery). Both are substrate-side
disciplines that keep the program in a regime where its
measure-theoretic refusals carry weight.

## The reduction step

The boundary between the regimes is an *operation*: the reduction
`k/n → p/q`. Above the line, you label `(k, n)` unreduced and the
integer-sample regime holds. Below the line, you take the same
rational `k/n`, reduce it to lowest terms `p/q`, and let `q` become
the operative arithmetic object — and you are in Stern-Brocot land.
The figure draws the operation explicitly.

![A two-panel figure titled "The reduction collapse: k/n → p/q many-to-one from the integer lattice to reduced rationals." Top panel: scatter plot with horizontal axis x = k/n ∈ [0, 1] and vertical axis "polygon order n" running from 2 at the bottom to 30 at the top. About 435 small dots in two colors — blue for gcd(k, n) = 1 (already reduced; one-to-one with popcorn stem) and orange for gcd(k, n) > 1 (collapses to a smaller-denominator stem). Dots form curving rows at each n level, fanning outward from the center of the strip. Vertical pale-purple bands cut through the cloud at x = 1/2, 1/3, and 2/3, with a pale-teal vertical band at x = 1/29 near the left edge. Annotations at the top of the panel read "1/2: 15→1" at center, "1/3: 10→1" and "2/3: 10→1" at staggered lower positions, and "1/29: 1→1 (lossless)" near the left edge. A legend at the bottom of the panel names the two colors. Center divider: bold italic label "the reduction step k/n → p/q" with subtitle "(the operative arithmetic step BIND-Erasure refuses)". Bottom panel: Thomae popcorn at the same Farey horizon N = 30 — vertical stems at every reduced p/q with q ≤ 30, height 1/q, tallest stem at x = 1/2 reaching y = 0.5, identical to the popcorn figure earlier in this memo, with the same purple and teal vertical bands aligning to the top panel's columns. Subtitle records: "Same Farey horizon N = 30. Integer lattice: 435 distinguishable (k, n) points. Reduced popcorn: 277 stems. Collapse ratio at p/q is ⌊N/q⌋ → 1."](../figures/reduction_collapse.png)

Two panels at the same Farey horizon `N = 30`.

**Top — integer lattice.** Every integer pair `(k, n)` with
`1 ≤ k < n ≤ 30`, plotted at `(k/n, n)`. 435 distinguishable points.
Color encodes `gcd(k, n)`: blue when the pair is already in lowest
terms (`gcd = 1`, in bijection with a unique popcorn stem below) and
orange when the pair will collapse on reduction (`gcd > 1`, projecting
onto a stem with smaller denominator). The columns at the most lossy
rationals are visible at a glance: `1/2` carries 15 stacked points
(the `n ∈ {2, 4, 6, …, 30}` tower), `1/3` and `2/3` each carry 10,
and the lossless `1/29` row sits as a single isolated dot.

**Bottom — popcorn.** The same 277 stems that appear in the Thomae
figure earlier in this memo. Reduced rationals `p/q` with `q ≤ 30`,
height `1/q`. Identical structure, identical Lebesgue-null support.

**The reduction step** sits between them, labeled across the
divider. It maps the top panel onto the bottom by sending each
`(k, n)` to its reduced representative `(p, q) = (k/g, n/g)` with
`g = gcd(k, n)`. The collapse ratio at each rational is
`⌊N/q⌋ → 1`. Annotated landmarks: `1/2` (15 → 1, the most lossy
rational at `N = 30`), `1/3` and `2/3` (10 → 1 each), and `1/29`
(1 → 1, lossless because nothing else with `n ≤ 30` reduces there).

Three things the figure makes operative.

1. **The two regimes are the same data, two readings.** Top and
   bottom show the same Farey horizon. The popcorn picture
   immediately below in *Why crossing costs measure* is the bottom
   panel of this figure. The strip portrait at the top of the memo
   is the geometric realization of the same `(k, n)` lattice, with
   corner heights and crystallographic contours added. The
   reduction step is what takes you from the integer lattice
   (geometrically rich, individuated) to the Stern-Brocot popcorn
   (denominator-decorated, Lebesgue-null).

2. **The collapse is information loss.** The integer side has 435
   distinguishable points; the popcorn has 277 stems. The 158-point
   difference is what the reduction throws away. The popcorn's tall
   stems are exactly the most-collapsed columns — `1/2` is tall
   (height `1/2`) because every even `n` projects there; `1/29` is
   short (height `1/29`) because only `n = 29` does. The popcorn's
   visual prominence at small denominators is collapse-multiplicity
   read as height.

3. **Diagnostic #1 has a picture.** The diagnostics section above
   asks: *Are you reducing `k/n` to lowest terms `p/q` and arguing
   about `q`?* When you next encounter an argument that wants to,
   this figure is what just happened. The argument has executed the
   projection drawn here. Whether that's legitimate depends on what
   the argument needs from `q` — but the reduction step is the
   boundary-crossing operation, and pretending the argument stayed
   integer-sample-side after invoking it is the failure mode the
   diagnostics are protecting against.

The figure does no work the memo's prose isn't already doing. It
provides a single anchor for the operation the rest of the
sensitizer orbits around. Build script:
[measure/build_reduction_collapse.py](measure/build_reduction_collapse.py).

## Why crossing costs measure

The phrase: *Stern-Brocot land eats measure for breakfast*. The
mechanism: the fractal constructions on that side generically have
measure-theoretic pathology. `?(x)` is continuous and strictly
increasing but has derivative zero almost everywhere — a singular
measure. Thomae is integrable but with all the structure at a
Lebesgue-zero set. Stern-Brocot depth is not uniformly distributed
against Lebesgue measure on `[0, 1]`. Any argument leveraging these
generically has a Lebesgue-zero set masquerading as full coverage,
or full coverage masquerading as a structural distinction.

### The popcorn picture

The Thomae instance shows the mechanism in one panel.

![A horizontal stem plot titled "Comparative denominator-rank stems on F_30: height 1/q at each p/q ∈ (0,1) (normalized shadow of the n-gon tangency-floor multiplicity histogram)". Horizontal axis "angle / 360° = p/q" from 0 to 1; vertical axis "height = 1/q" from 0 to about 0.5. A single tall dark-purple stem at x = 1/2 rises to y = 0.5. Two slightly shorter purple stems at x = 1/3 and x = 2/3 rise to y ≈ 0.333. A pair at x = 1/4 and x = 3/4 reaches y = 0.25; another pair at x = 1/5, 2/5, 3/5, 4/5 reaches y = 0.2; and self-similar combs of progressively shorter stems fill in between, fading into a dense carpet of yellow ticks near the floor. A color bar at the right runs from dark purple at denominator q ≈ 3 to bright yellow at q = 30, and stem colors track that scale — tallest stems are purple, shortest are yellow.](../figures/thomae_popcorn.png)

This is Thomae's popcorn function on the Farey set `F_30`. At every
reduced rational `p/q ∈ (0, 1)` with `q ≤ 30`, draw a stem of height
`1/q`; color encodes `q` from dark (small `q`) to bright (large `q`).
The tallest stem sits at `p/q = 1/2` with height `1/2`. The next
tier at `1/3, 2/3` reaches `1/3`. Then `1/4, 3/4` at `1/4`. Then the
four fifths, the four sevenths, the eight ninths (skipping `1/3`,
`2/3`), and so on, in a self-similar comb fading into the floor.

This is the *same data* as the strip portrait's floor tangencies —
both pictures live over `[0, 1]` with rationals as the organizing
datum. The figure's subtitle says it explicitly: "normalized shadow
of the n-gon tangency-floor multiplicity histogram." The strip reads
each tangency by its unreduced label `(k, n)` and works inside the
integer-sample regime; the popcorn picture reduces `k/n → p/q` and
plots `1/q`. Same arithmetic substrate, two organizing reductions —
the BIND-Erasure-allowed one versus the BIND-Erasure-refused one.
This is what `n-gons/N-GON-WHOLENESS.md` §7's "comparative
denominator-height reconstruction... preserved separately in
`n-gons/stern_brocot.sage`, but it is not the operative vocabulary"
points at: the same histogram, the other reading.

The pathology is in the structure visible in the figure. The set of
points where the stem is *non-trivial* (height above any fixed
threshold `1/Q`) is finite — the rationals with denominator at most
`Q`. Across all `Q`, the support of nonzero stems is the full set of
rationals in `(0, 1)`, which is countable, hence Lebesgue-zero. Most
of `[0, 1]` — almost every point under Lebesgue — is *between* the
stems, where Thomae returns zero. The visually striking
denominator-rank decoration lives entirely on a Lebesgue-null set.

This is the *eats measure for breakfast* mechanism in concrete form.
Any argument that takes Thomae's height law `f(p/q) = 1/q` as an
operative arithmetic step is making a claim that lives on a
measure-zero set. The decoration *looks* dense — every interval
contains rational stems at every height tier — but the
"density" is countable density inside a continuum, not Lebesgue
density. From the integer-sample side, the same arithmetic content
is read differently: every rational `k/n` (unreduced!) is its own
object indexed by `(k, n)`; the strip-side area functional
`A_below(n) = (n/π) ln(sec(π/n) + tan(π/n)) − 1 = π²/(6n²) +
O(n⁻⁴)` reads through a smooth secant tissue where Lebesgue measure
is genuinely informative. Two pictures, same substrate, opposite-side
readings. The strip portrait above is the rigid reading; the popcorn
picture is what's lost on the other side.

This is why BIND-Erasure refuses Thomae's height law as an operative
primitive. The refusal is not aesthetic. Adopting `f(p/q) = 1/q` as
an operative step pulls the argument off the integer-sample regime
onto a Lebesgue-null fractal, and once there, the substrate-side
refusals at [measure/SUBSTRATE-OBSTRUCTIONS.md](measure/SUBSTRATE-OBSTRUCTIONS.md)
no longer apply — the §5 angles are integer-sample-aware, and a
Lebesgue-null fractal does not preserve their measure-theoretic
content.

The point for the sensitizer's purpose is not that Thomae is wrong.
Thomae is a real function with real properties and the canonical
pointwise-discontinuous-but-Riemann-integrable textbook example. The
point is that *using Thomae as an operative arithmetic step* crosses
the regime boundary. `?(x)` and Stern-Brocot depth have analogous
pictures with analogous Lebesgue-null support; the popcorn picture
is the cleanest instance to display because every stem is at a named
rational with a named height. When you next encounter an argument
that wants to use a denominator-rank decoration as a load-bearing
step, this picture is what the substrate-side refusals are
referring to.

### Back to the mechanism

The integer-sample regime avoids this because the apparatus operates
on integers, integer lattices, integer determinants, and Haar /
Lebesgue measure pulled back along integer-indexed maps that
preserve the measure-theoretic structure. The five §5 angles are all
integer-sample-aware in this sense; that is why their joint refusal
is load-bearing.

When an argument crosses into Stern-Brocot land, the measure that
the substrate-side refusals are built on is no longer the operative
measure. The argument may still be correct, but it operates on a
different substrate, and the program's refusals do not transfer.

## What this means for the impossibility theorem

The substrate-side fact the paper is asserting — that
[paper/IMPOSSIBILITY-OUTLINE.md](paper/IMPOSSIBILITY-OUTLINE.md)
§4.5's `T(P)` is structural rather than engineering — has its
content here. `T(P)` is the floor reachable while staying inside the
integer-sample regime. Descent past `T(P)` would require leaving the
regime. Leaving the regime lands you in Stern-Brocot land where the
rigidity is gone but the fractal absorbs Lebesgue measure faster
than any rigorous lower-bound apparatus can recover anything. So the
impossibility is genuinely structural: the apparatus that would
prove the better bound, on the side where the better bound would
need to live, does not exist.

The Coase posture
([measure/COASE-FRICTION-AND-SPECIALISTS.md](measure/COASE-FRICTION-AND-SPECIALISTS.md))
covers the rest: the algebra of `δ` is the cost of trying to cross;
the substrate-side discontinuity *is* the regime boundary; different
reasonable algebras of `δ`
([measure/ALGEBRA-OF-DELTA.md](measure/ALGEBRA-OF-DELTA.md)) read
the same boundary in different shapes; no choice of `δ`-algebra can
erase the boundary because the boundary is upstream of any
coordinate.

## Adjacent anchors

- [n-gons/counting/THICK-SWEEP.md](n-gons/counting/THICK-SWEEP.md) — the boundary in one figure.
- [BNHA/triad/Eraserhead/ARCHIMEDEAN-CONSTRICTION.md](BNHA/triad/Eraserhead/ARCHIMEDEAN-CONSTRICTION.md) — the discipline holding the line.
- [n-gons/N-GON-WHOLENESS.md](n-gons/N-GON-WHOLENESS.md) — operative apparatus on the rigid side.
- [BNHA/triad/Eraserhead/BIND-THE-CIRCLE.md](BNHA/triad/Eraserhead/BIND-THE-CIRCLE.md) — the explicit refusal list.
- [measure/SUBSTRATE-OBSTRUCTIONS.md](measure/SUBSTRATE-OBSTRUCTIONS.md) — the §5 substrate-side typing as five faces of integer-sample rigidity.
- [measure/COASE-FRICTION-AND-SPECIALISTS.md](measure/COASE-FRICTION-AND-SPECIALISTS.md) — substrate vs coordinate posture.
- [measure/ALGEBRA-OF-DELTA.md](measure/ALGEBRA-OF-DELTA.md) — the algorithm-side coordinate's algebra.
- [memos/NATIVE-F-MINIMAL-DEFINITION.md](memos/NATIVE-F-MINIMAL-DEFINITION.md) — cyclotomic-ladder-vs-affine-closure as the integer-vs-continuum asymmetry.
- [memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md) — sibling content-not-calendar discipline.

## Trust boundary

This memo is a sensitizer, not a theorem. It does not prove that
crossing the regime boundary necessarily fails — arguments can be
legitimately committed to the Stern-Brocot side. It does not prove
that the integer-sample regime is the unique substrate where the
program's refusals could work. It does not exhaust the witnesses to
the regime boundary in the repo. It points at a fact that is deeply
embedded in the program's vocabulary and methodology, and gives
operative diagnostics for recognizing the boundary in future work.

The substrate-side fact itself — that algebraic-arithmetic rigidity
at integer samples is what gives the §5 refusals and the
bounded-coefficient lower bounds their load-bearing content — is
upstream of any specific theorem in the repo. The witnesses
[THICK-SWEEP, ARCHIMEDEAN-CONSTRICTION, N-GON-WHOLENESS, the §5
angles, Morgenstern's argument, the cyclotomic ladder] each show
one face of the same rigidity; the rigidity itself is the
substrate-side fact, and any reasonable coordinate (the cocycle
realization at PHASE-DEFECT, the bounded-coefficient determinant
ledger, the Haar-on-orbit reading) charts it without constituting
it.
