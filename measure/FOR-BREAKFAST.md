# FOR-BREAKFAST

![A two-panel figure titled "The reduction collapse: k/n → p/q many-to-one from the integer lattice to reduced rationals." Top panel: scatter plot with horizontal axis x = k/n ∈ [0, 1] and vertical axis "polygon order n" running from 2 at the bottom to 30 at the top. About 435 small dots in two colors — blue for gcd(k, n) = 1 (already reduced) and orange for gcd(k, n) > 1 (collapses on reduction). Dots form curving rows at each n level. Vertical pale-purple bands at x = 1/2, 1/3, 2/3 with a pale-teal band at x = 1/29; annotations at top read "1/2: 15→1", "1/3: 10→1", "2/3: 10→1", and "1/29: 1→1 (lossless)". Center divider: bold italic label "the reduction step k/n → p/q (the operative arithmetic step BIND-Erasure refuses)". Bottom panel: Thomae popcorn at the same Farey horizon N = 30 — vertical stems at every reduced p/q with q ≤ 30, height 1/q, tallest stem at x = 1/2 reaching y = 0.5. Subtitle: "Same Farey horizon N = 30. Integer lattice: 435 distinguishable (k, n) points. Reduced popcorn: 277 stems. At p/q, ⌊N/q⌋ lattice points collapse to one stem."](../figures/reduction_collapse.png)

*The frontispiece is the boundary as an operation: the reduction
`k/n → p/q`. Top panel — the integer-indexed regime, where each pair
`(k, n)` is its own object. Bottom panel — Stern-Brocot land, where
the same data has been reduced and decorated by `1/q` (Thomae's
popcorn). The middle label names what the program refuses as an
operative arithmetic step. Full tour at §The reduction step.*

The central thesis (formalized as Theorem K below) is: the substrate
has algebraic-arithmetic rigidity at integer-indexed samples. (What's
integer is the *label* — `(k, n)`, `n`, finite orbit index,
cyclotomic order — not the sample value, which can sit in any
continuum.) The program's operative apparatus stays inside that
regime by construction. The instant the integer indexing isn't
operative — when `q` in lowest terms takes over from `(k, n)`, or
fractal-rational decoration replaces the integer label — you are in
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

**Proof-debt convention.** `[GREENEGGS]` marks a claim that points at
proof material the sensitizer keeps as the argument's intended
direction. The central kernel claim — Theorem K below — is **proved
for the named L-observables `f₁, f₂, f₃`** (cyclotomic-ladder degree,
polygon perimeter, Hurwitz isoperimetric gap rate). Other §5 faces
are either out of scope as direct K2 instances (the Haar / β(α)
face on `T = ℝ/ℤ`; the L-W null/full face, fiber-constant on L
under the literal source-side reading) or flagged for separate
transport. Lemma T1 is also proved here. The remaining
`[GREENEGGS]` tags route to specific named lemmas (T2, T3, T4b, T6)
in §The kernel, or flag analogies that are still suggestive rather
than formal.

## The two regimes

**Integer-indexed regime.** Samples are labeled by integers `(k, n)`.
Vertex `k` of polygon `n`, position `k` of `(ℤ/nℤ)*`, the
integer-iterate orbit `{kα mod 1}`, the `n`-th cyclotomic field, the
`m ≡ 1 mod n` Fourier lattice. Algebraic-arithmetic structure is
*rigid*: cosines lie in named cyclotomic subfields with computable
degrees `φ(n)/2`; determinant-growth arguments have a protected
scale when their coefficient hypotheses keep volume growth bounded;
divisibility tests are exact; the off-backbone empty-contour
claim is **Lemma T1** (proved in §The kernel by trace/Ramanujan);
the thin-sweep all-`N` claim is open **Lemma T2**. Measure-theoretic
typing applies cleanly to several integer-indexed observables
(cyclotomic-ladder degree, polygon perimeter, Hurwitz isoperimetric
gap; per K2 of §The kernel). The Haar / β(α) face uses Haar measure
on `T = ℝ/ℤ` for irrational rotation orbits with continued-fraction
parameter `β(α)`, not Haar on `(ℤ/nℤ)*`; whether it transports to a
direct L-observable is open. The §5-faces-on-a-shared-state-space
upgrade is the open boundary-object piece T4b.

**Stern-Brocot land.** Rationals get reduced to lowest terms `p/q`
and the denominator `q` becomes the operative arithmetic object.
Stern-Brocot organizes rationals by depth; Thomae decorates them by
`f(p/q) = 1/q`; Minkowski's `?(x)` maps the dyadic tree to the Farey
tree; Denjoy re-reads dyadic expansions as continued fractions. The
machinery is fractal: Thomae is discontinuous at every rational and
continuous at every irrational; `?(x)` induces a singular measure;
Stern-Brocot depth is not Lebesgue-uniform. Exact algebraic rigidity
does not literally disappear, but it stops being the *operative*
protection once the argument is carried by denominator decoration or
positive-resolution approximation. The measure-theoretic content of
this stops-being-operative claim is Theorem K below: F-side
distinctions are fiber-constant on `R`-fibers and cannot reconstruct
the named fiber-varying L-observables extracted from §5
(`f₁ = φ(n)/2`, `f₂ = L_n`, `f₃ = Δ_n`).

The regime boundary is *the line where the reduction `k/n → p/q`
becomes the operative arithmetic step*. Above the line, you label
`(k, n)` unreduced and the rigidity holds. Below the line, `q` is
what the argument turns on, and you have crossed.

## Where the rigidity lives in the repo

The portrait, then three witnesses in the program's native vocabulary.

### The picture

![A wide strip plot titled "Strip Linkage | floor grid and special corner contours". Horizontal axis "strip angle u = θ/(2π)" from 0 to 1, with vertical dashed reference lines at 1/4, 1/2, and 3/4. Vertical axis "strip height y = r − 1" from 0 up to about 1. A hatched gray "DH-grid band" runs along the floor with twelve evenly spaced vertical dashes. Six dashed horizontal level lines mark polygon heights y_n = sec(π/n) − 1 for n = 3, 4, …, 8. A scatter of small black dots labeled "corner / tangency point" sits on the floor at positions x = k/n and at the polygon levels at positions x = (2k+1)/(2n). Five colored contour curves rise from the floor to the top of the strip: red curves labeled X = +1 near the right and left edges, orange curves X = +1/2 just inside them, blue curves X = -1/2 mirroring on the other side, two red curves X = -1 around u = 1/2, and dashed black vertical lines labeled X = 0 at u = 1/4 and 3/4. A legend at the upper right enumerates the five contour colors and the marker types.](../figures/counting_strip_observables.png)

Read the figure as a portrait of the integer-indexed regime in one
panel. The strip is the unrolled annulus between the unit incircle
(at strip height `y = 0`) and the circumscribed `n = 3`-cir (at the
top). Horizontal axis: strip angle `u = θ/(2π) ∈ [0, 1)`, identified
at the endpoints. Vertical axis: strip height `y = r − 1`. Six
polygons `n = 3, 4, …, 8` are drawn; each contributes `n` floor
tangencies and `n` corner vertices.

Three integer-indexed objects sit on the strip.

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
   real field `K_{2n} = ℚ(cos(π/n))`, of degree `φ(2n)/2` for
   `n > 1`. The trace-field ladder `K_n = ℚ(cos(2π/n))` remains the
   program's circle-side depth observable, but the actual corner
   coordinate may sit one half-angle field higher. Each corner is an
   algebraic-arithmetic point with an integer-indexed signature.

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
all-`n` absence is **Lemma T1** of §The kernel, **proved** there
by squaring + trace identity + Ramanujan-sum reduction
`4 c_n(2k+1) = μ(n) − 3 φ(n)` + `φ(h)` enumeration. (Niven's
classical theorem does *not* directly imply T1: T1 concerns the
rational ratio of two cyclotomic cosines, not the rationality of
one.) The corner's height `sec(π/n)` is algebraic of degree
`φ(2n)/2` over `ℚ`, and forcing `(1 + y) cos(2πu) = ±1/2` at
`(u, y) = ((2k+1)/(2n), sec(π/n) − 1)` is the equation T1 rules
out. The connection to THICK-SWEEP's thin-sweep non-coincidence is
**open Lemma T2** — *not* parallel to T1 (the slope `1/√3` adjoins
`√3 ∈ ℚ(ζ_{12})`, which sits inside relevant cyclotomic composita
and breaks the Ramanujan-sum reduction).

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
contours — all integer-indexed objects under their respective
measure-theoretic readings.

What is *not* in the figure: no Stern-Brocot tree, no Farey
neighbors, no Thomae height law `f(p/q) = 1/q`, no Minkowski `?(x)`
decoration, no reduction `k/n → p/q` with `q` as the operative
arithmetic object. The discipline shows by absence. The same point
set under a Stern-Brocot reading is preserved separately at
`n-gons/stern_brocot.sage` per N-GON-WHOLENESS §7, but it is not
the operative vocabulary here.

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

For this memo, the thin-sweep half is imported as a theorem target:
the pigeonhole thick-sweep bound is elementary, but the global
all-`N` non-coincidence at slope `1/√3` is **Lemma T2** of §The
kernel.

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

The strip portrait shows integer-indexed objects geometrically. The
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
coincidence inside the half-angle field `K_{2n} = ℚ(cos(π/n))`,
with trace-field shadows in `K_n = ℚ(cos(2π/n))`; the integer pair
`(2k+1, n)` fixes the cosine value. The cyclotomic ladder forbids
that coincidence generically per **Lemma T1**. The empty guides are
the same *kind* of rigidity as THICK-SWEEP's "thin sweep never hits
two at once" (**Lemma T2**), shown as a vertical refusal at named
rationals rather than a horizontal refusal of coincidence.

A note on the ψ choice. The outside-out coordinates themselves can
live in the half-angle field `K_{2n}`. The program's native
circle-side depth observable in §5.4, however, is the trace-field
degree `φ(n)/2 = [K_n : ℚ]` for
`K_n = ℚ(cos(2π/n))`. That is the integer-indexed regime's internal
arithmetic ladder. ψ is *not* that ladder. ψ is the additive bridge
function PERMEATE uses to compare circle-side depth (multiplicative
on prime-power parts through `φ`) to log-side depth (additive in
`v_p`); the coloring tells the reader the figure is meant to be
legible across the bridge. The trace-field depth is what the figure
structurally reflects when read through ψ, while the plotted
coordinates may carry half-angle field data. Treating these as one
stratification needs **Lemma T3** of §The kernel.

Inside the integer-indexed regime, depth grows and the rigidity
stratifies: ψ = 2 backbone where rational coincidences land, higher
ψ where new ones are forbidden (**Lemma T1**), ±1/2 guides made
visible by *not* being hit. The picture makes the cyclotomic ladder
pictorial.

### The §5 typing as faces of one rigidity

The §5 substrate-side typing at
[measure/SUBSTRATE-OBSTRUCTIONS.md](measure/SUBSTRATE-OBSTRUCTIONS.md)
records five angles: Haar on irrational rotation orbits with
`β(α)` from continued fractions; three non-nesting isoperimetric
registers sharp on the regular-`n`-gon family; Hurwitz Fourier on
the integer lattice `m ≡ 1 mod n`; cyclotomic ladder
`[K_n : ℚ] = φ(n)/2` indexed by integer `n`; L-W null/full at the
algebraic-vs-transcendental level.

**What Theorem K proves about these.** Not all five faces transcribe
to direct L-observables. K's σ-algebra coarsening is established for
three concrete L-observables (cyclotomic-ladder degree, polygon
perimeter, Hurwitz isoperimetric gap rate) — these are
fiber-non-constant and hence not in `R^*(M(F))`. The Haar / `β(α)`
face lives on `T = ℝ/ℤ` and requires a separate transport to L; the
L-W null/full face is fiber-constant on L under the literal
algebraic-vs-transcendental reading. So the "five faces of one
rigidity" framing is *partially* supported by K (three faces, with
explicit L-observables) and *not* yet supported as a uniform
single-state-space theorem; the boundary-object-with-`δ`-faithfulness
piece T4b of [measure/THE-FIRST-BRIDGE.md](measure/THE-FIRST-BRIDGE.md)
is the open upgrade.

## The algorithm-side projection

The bounded/unbounded coefficient boundary in
[paper/OUTLINE.md](paper/OUTLINE.md)
§1.4 is a candidate algorithm-side parallel to the same regime
boundary. Morgenstern's `Ω(n log n)` additive lower bound holds
*under bounded coefficients* because a step
`h = λf + μg`, with `|λ|, |μ| ≤ c`, can increase the maximum
subdeterminant by at most `2c`; the DFT target has determinant scale
`n^(n/2)`. This is a determinant-growth floor, not literally an
integer-determinant floor: Morgenstern allows arbitrary complex
coefficients subject to the modulus bound. Unbounded coefficients let
the algebra absorb volume growth into linear-combination weights; the
determinant argument then gives no nontrivial asymptotic lower bound.
The structural parallel: bounded-coefficient bookkeeping behaves
rigidly the way integer-indexed labels behave rigidly; unbounded
coefficients soften the cost model the way the reduction step softens
`(k, n)` labels into denominator decoration. Whether the parallel
lifts to a formal map between coefficient unboundedness and
reduction-collapse / denominator depth is **open** — the analogy is
suggestive, not proved.

The cyclotomic-ladder-vs-affine-closure asymmetry at
[memos/NATIVE-F-MINIMAL-DEFINITION.md](memos/NATIVE-F-MINIMAL-DEFINITION.md)
is a **sibling** structural fact, not downstream of Theorem K:
NATIVE-F's no-go is a closure-depth mismatch (unbounded `{K_n}`
versus flat affine composition) that does *not* use the reduction
map `R`, Stern-Brocot fibers, or denominator collapse. `φ(n)/2`
grows because `n` is integer-indexed; `Aff⁺(ℝ)` is two-parameter
flat because affine transformations are continuum-parameterized.
Integer-indexed depth on one side, continuum-flatness on the other.
The two facts (Theorem K's σ-algebra coarsening and NATIVE-F's
closure-depth mismatch) share an integer-vs-continuum motif but
proceed by separate proof routes; neither is a corollary of the
other.

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

3. **Positive bandwidth replaces what was thin / zero-width.**
   Bandwidth softening is its own crossing mode, distinct from the
   reduction-collapse mode in (1) and (2). Cyclotomic rigidity holds
   at zero bandwidth (THICK-SWEEP thin-sweep); pigeonhole takes over
   at any positive bandwidth. Irrational `α` itself is *not* a
   crossing — `BIND-THE-CIRCLE` allows continuous parameters and the
   rotations register works with irrational `α` routinely. The
   crossing is when the bandwidth or `q`-decoration becomes the
   load-bearing object, not when continuum parameters appear at all.

4. **The equation forces an exact coincidence between cyclotomic
   data and a continuum quantity.** Cyclotomic rigidity typically
   forbids the coincidence on the integer-indexed side; on the other
   side the impossibility downgrades to pigeonhole approximation.
   THICK-SWEEP is the canonical witness for both behaviors in one
   note.

5. **The argument leans on Lebesgue measure of a set defined by
   continuum-rational decoration (denominator height, fractal depth,
   `?(x)`-derived density).** Ask whether the set is a fractal
   eating measure. Thomae, `?`, Stern-Brocot depth all generically
   have measure-theoretic pathology that the integer-indexed
   apparatus avoids by construction.

If any signal fires, pause. Either rewrite the argument to stay on
the integer-indexed side, or declare explicitly that the argument is
committing to the Stern-Brocot side and acknowledge that the
program's substrate-side discipline does not transfer there.

## What protects the regime

[BNHA/triad/Eraserhead/BIND-THE-CIRCLE.md](BNHA/triad/Eraserhead/BIND-THE-CIRCLE.md)
is the explicit discipline. Its refusal list (named at §The two
regimes; flagged in Diagnostic #2) is exactly the list of
primitives that live on the Stern-Brocot side. The list is not
aesthetic. Each primitive is load-bearing on its side; any of them
re-entering an argument means the argument has crossed the regime
boundary.

The OLD-TIME-RELIGION content-not-calendar criterion at
[memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md) is a
sibling discipline on a different axis (post-1882 results don't
smuggle transcendence-theory machinery). Both are substrate-side
disciplines that keep the program in a regime where its
measure-theoretic refusals carry weight.

## The reduction step

The frontispiece, with the full tour.

![A two-panel figure titled "The reduction collapse: k/n → p/q many-to-one from the integer lattice to reduced rationals." Top panel: scatter plot with horizontal axis x = k/n ∈ [0, 1] and vertical axis "polygon order n" running from 2 at the bottom to 30 at the top. About 435 small dots in two colors — blue for gcd(k, n) = 1 (already reduced; one-to-one with popcorn stem) and orange for gcd(k, n) > 1 (collapses to a smaller-denominator stem). Dots form curving rows at each n level, fanning outward from the center of the strip. Vertical pale-purple bands cut through the cloud at x = 1/2, 1/3, and 2/3, with a pale-teal vertical band at x = 1/29 near the left edge. Annotations at the top of the panel read "1/2: 15→1" at center, "1/3: 10→1" and "2/3: 10→1" at staggered lower positions, and "1/29: 1→1 (lossless)" near the left edge. A legend at the bottom of the panel names the two colors. Center divider: bold italic label "the reduction step k/n → p/q" with subtitle "(the operative arithmetic step BIND-Erasure refuses)". Bottom panel: Thomae popcorn at the same Farey horizon N = 30 — vertical stems at every reduced p/q with q ≤ 30, height 1/q, tallest stem at x = 1/2 reaching y = 0.5, identical to the popcorn figure earlier in this memo, with the same purple and teal vertical bands aligning to the top panel's columns. Subtitle records: "Same Farey horizon N = 30. Integer lattice: 435 distinguishable (k, n) points. Reduced popcorn: 277 stems. At p/q, ⌊N/q⌋ lattice points collapse to one stem."](../figures/reduction_collapse.png)

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
`g = gcd(k, n)`. For fixed reduced `p/q` at horizon `N`, exactly
`⌊N/q⌋` lattice points collapse to one reduced stem. Annotated
landmarks: `1/2` (15 → 1, the most lossy rational at `N = 30`),
`1/3` and `2/3` (10 → 1 each), and `1/29` (1 → 1, lossless because
nothing else with `n ≤ 30` reduces there).

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
   integer-indexed-side after invoking it is the failure mode the
   diagnostics are protecting against.

The figure is the single anchor for the operation the rest of the
sensitizer orbits around. Build script:
[measure/build_reduction_collapse.py](measure/build_reduction_collapse.py).

## Why crossing costs measure

The phrase: *Stern-Brocot land eats measure for breakfast*. The
mechanism: the fractal constructions on that side generically have
measure-theoretic pathology. `?(x)` is continuous and strictly
increasing but has derivative zero almost everywhere — a singular
measure. Thomae is integrable but with all the structure at a
Lebesgue-zero set. Stern-Brocot depth is not uniformly distributed
against Lebesgue measure on `[0, 1]`. Any argument leveraging these is liable to confuse a Lebesgue-zero
set with full coverage, or full coverage with a structural
distinction.

The skeptical caveat is important: Lebesgue-nullness alone is not the
obstruction. The integer-indexed data are also countable when embedded
naively in `[0, 1]`. The difference is the operative measure space:
the integer-indexed side uses counting / Haar / algebraic-degree
bookkeeping on labels, while the Stern-Brocot side asks a
denominator-decorated subset of the continuum to carry distinctions
back into that apparatus. The claim that this transport fails is
**Theorem K** of §The kernel: F-side data lifted through `R^*` is
fiber-constant, but the named L-observables (cyclotomic-ladder
degree `f₁ = φ(n)/2`, polygon perimeter `f₂ = L_n`, isoperimetric
gap `f₃ = Δ_n`) vary on R-fibers, so they are not in the image of
`R^*`.

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

The figure is the bottom panel of the reduction-step figure at
§The reduction step, in isolation. Its subtitle records the
substrate identity directly: "normalized shadow of the n-gon
tangency-floor multiplicity histogram."

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
density. From the integer-indexed side, the same arithmetic content
is read differently: every rational `k/n` (unreduced!) is its own
object indexed by `(k, n)`; the strip-side area functional
`A_below(n) = (n/π) ln(sec(π/n) + tan(π/n)) − 1 = π²/(6n²) +
O(n⁻⁴)` reads through a smooth secant tissue where Lebesgue measure
is genuinely informative. Two pictures, same substrate, opposite-side
readings. The strip portrait above is the rigid reading; the popcorn
picture is what's lost on the other side.

This is why BIND-Erasure refuses Thomae's height law as an operative
primitive. The refusal is not aesthetic. Adopting `f(p/q) = 1/q` as
an operative step pulls the argument off the integer-indexed regime
onto a Lebesgue-null fractal, and once there, the substrate-side
refusals at [measure/SUBSTRATE-OBSTRUCTIONS.md](measure/SUBSTRATE-OBSTRUCTIONS.md)
no longer apply to the named L-observables (`f₁, f₂, f₃` of K2):
they vary on `R`-fibers, so by **Theorem K** they are not in
`R^*(M(F))` and an apparatus reading only F-side decoration cannot
reconstruct them.

The point for the sensitizer's purpose is not that Thomae is wrong.
Thomae is a real function with real properties and the canonical
pointwise-discontinuous-but-Riemann-integrable textbook example. The
point is that *using Thomae as an operative arithmetic step* crosses
the regime boundary. `?(x)` and Stern-Brocot depth carry analogous
F-side decorations whose distinctions are subject to the same
Theorem K obstruction; the popcorn picture is the cleanest instance
to display
because every stem is at a named rational with a named height. When
you next encounter an argument
that wants to use a denominator-rank decoration as a load-bearing
step, this picture is what the substrate-side refusals are
referring to.

## What this means for the impossibility theorem

The substrate-side fact the paper is asserting — that
[paper/OUTLINE.md](paper/OUTLINE.md)
§4.5's `T(P)` is structural rather than engineering — has its
content here. `T(P)` is the floor reachable while the apparatus
stays inside the integer-indexed regime. Descent past `T(P)` would
require leaving it. Leaving lands you in Stern-Brocot land where the
distinguishing structure is supported on null or singular measure
sets — Thomae on the rationals, `?(x)`-derivative concentrated on a
Lebesgue-null set, Stern-Brocot depth not uniformly distributed
against Lebesgue. The present admissible apparatus has no
measure-stable way to recover the needed distinction after crossing
— this is **Theorem K** of §The kernel.

The Coase posture
([measure/COASE-FRICTION-AND-SPECIALISTS.md](measure/COASE-FRICTION-AND-SPECIALISTS.md))
covers the rest: the algebra of `δ` is the cost of trying to cross;
the substrate-side discontinuity *is* the regime boundary; different
reasonable algebras of `δ`
([measure/ALGEBRA-OF-DELTA.md](measure/ALGEBRA-OF-DELTA.md)) read
the same boundary in different shapes; no choice of `δ`-algebra can
erase the boundary because the boundary is upstream of any
coordinate (formalized as **open T6** in §The kernel).

## The kernel of the measure-theoretic proof

This section consolidates the [GREENEGGS] obligations into named
lemmas with measure-theoretic content. The central claim — *Theorem
K* below — is a **σ-algebra coarsening theorem**: the reduction
step `R: (k, n) → p/q` induces the quotient-visible sub-σ-algebra
`R⁻¹(2^F)` on `L`, and any F-side apparatus only sees functions
measurable for that coarsening, i.e. fiber-constant functions.
Several concrete `n`-observables on `L` (cyclotomic-ladder degree,
Hurwitz Fourier perimeter, isoperimetric gap rate) are shown to be
**not** fiber-constant; hence those observables cannot be recovered
from F-side data.

**Scope honesty.** Theorem K as proved here is a model instance of
information loss under reduction. It is not yet the load-bearing
measure-theoretic proof the program needs. The full impossibility
bridge — a faithful boundary object with a `δ` coordinate tying
closure, drift, and source-side obstruction together — is the open
THE-FIRST-BRIDGE statement; T1–T3 are supporting cyclotomic-rigidity
claims (T1 proved here, T2/T3 open); T4 splits into a trivial
shared-indexing piece and an open boundary-object piece; T6 is
softened to upstream-ness only. The kernel is the σ-algebra side of
what the bridge will eventually need to deliver.

### K.0 The two measurable structures

Let

```text
L = { (k, n) ∈ ℤ² : 1 ≤ k < n, n ≥ 3 }
```

be the **integer-indexed lattice**, equipped with counting measure
`c_L` (or the corresponding atomic σ-algebra `2^L`). The
degenerate cases `n ∈ {1, 2}` are excluded from the kernel
argument: at `n = 2` the trace-field formula
`[K_n : ℚ] = φ(n)/2` fails (`K_2 = ℚ`, degree 1, but `φ(2)/2 = 1/2`),
and the polygon apparatus collapses to a digon. The §5 substrate-
side content lives at `n ≥ 3`.

Let

```text
F = { (p, q) ∈ ℤ² : 1 ≤ p < q, gcd(p, q) = 1 }
```

be the **Farey set**, equipped with the denominator-decoration
measure `μ_F` carrying Thomae's stem assignment `(p, q) ↦ 1/q` (or
any σ-finite refinement of the Farey arrangement; the kernel
argument is independent of which decoration `μ_F` carries).

The **reduction map** is

```text
R : L → F,    R(k, n) = (k / g, n / g),   g = gcd(k, n).
```

`R` is measurable in any reasonable σ-algebra on `L` and `F`
(both are countable, atomic σ-algebras, so all functions are
measurable). For each `(p, q) ∈ F`, the fiber inside `L` is

```text
R⁻¹(p, q) ∩ L = { (m p, m q) : m ≥ m₀(q) }
```

where `m₀(q) = ⌈3/q⌉` is the least integer with `m₀(q) · q ≥ 3`
(so `m₀(q) = 1` for `q ≥ 3` and `m₀(2) = 2`). The fiber is a
countably infinite arithmetic progression. At horizon `N`, the
truncated fiber has cardinality `⌊N/q⌋ − (m₀(q) − 1)`. Define a
**fiber basepoint section** `s : F → L` by
`s(p, q) := (m₀(q) p, m₀(q) q)`; for `q ≥ 3` this is the inclusion
`(p, q) ↪ L`, and for `q = 2` (the unique reduced rational with
`q = 2` is `1/2`) it is `s(1, 2) = (2, 4)`.

### K.1 The pullback functor

Fix a measurable codomain `(V, 𝒱)` with point-separating σ-algebra
(singletons are `𝒱`-measurable; `V = ℝ` with the Borel σ-algebra
suffices for all K2 instances). The pullback
`R^* : M(F → V) → M(L → V)` sends `g : F → V` to `g ∘ R : L → V`.
Its image is exactly the **fiber-constant** L-functions.

> **Lemma K1 (fiber-constant characterization).** Under the above
> typing, `f ∈ R^*(M(F → V))` iff `f` is constant on every L-fiber
> of `R`: for every `(p, q) ∈ F` and every pair
> `(m p, m q), (m' p, m' q) ∈ R⁻¹(p, q) ∩ L`,
> `f(m p, m q) = f(m' p, m' q)`.

*Proof.* If `f = g ∘ R`, every point in `R⁻¹(p, q) ∩ L` maps to
`(p, q)` under `R`, so `f` takes the value `g(p, q)` on the whole
L-side fiber. Conversely, if `f` is fiber-constant, use the
basepoint section `s : F → L` of K.0 and define
`g(p, q) := f(s(p, q))`. Then for any `(m p, m q) ∈ R⁻¹(p, q) ∩ L`,
fiber-constancy gives `f(m p, m q) = f(s(p, q)) = g(p, q)`, so
`f = g ∘ R`. Since `F` carries an atomic σ-algebra (every singleton
measurable), `g` is automatically `(F, 2^F) → (V, 𝒱)`-measurable. ⊣

### K.2 Concrete `n`-observables on `L` that fail to be fiber-constant

K2 names specific functions on `L`, drawn from §5 substrate-side
content, that are not fiber-constant. Three are clean instances; two
§5 faces are flagged as not directly K2-eligible without further
apparatus.

> **Lemma K2.** The following functions on `L` are not fiber-constant
> — there exist `(p, q) ∈ F` and `m ≥ 2` with
> `f(m p, m q) ≠ f(p, q)`:
>
> 1. *Cyclotomic-ladder degree:* `f₁(k, n) = φ(n)/2 = [K_n : ℚ]`.
> 2. *Polygon perimeter:* `f₂(k, n) = L_n = 2 n sin(π/n)`, equivalently
>    the Hurwitz first Fourier coefficient
>    `c_1^{(n)} = L_n² / (4 π²)`.
> 3. *Hurwitz isoperimetric gap (rate face):*
>    `f₃(k, n) = Δ_n = L_n² · (1 − (π/n) cot(π/n))`.

*Proof.* K2 only requires one fiber witness per observable; we
give explicit ones.

- **f₁.** Take `(p, q) = (1, 5)`, `m = 3`: `f₁(1, 5) = φ(5)/2 = 2`,
  `f₁(3, 15) = φ(15)/2 = 4`. Distinct. ✓
- **f₂.** Take `(p, q) = (1, 3)`, `m = 2`:
  `f₂(1, 3) = L_3 = 6 \sin(π/3) = 3\sqrt{3} ≈ 5.196`,
  `f₂(2, 6) = L_6 = 12 \sin(π/6) = 6`. Distinct. ✓
- **f₃.** Take `(p, q) = (1, 3)`, `m = 2`:
  `f₃(1, 3) = Δ_3 = L_3² · (1 − (π/3) \cot(π/3))
  = 27 · (1 − π/(3\sqrt{3})) ≈ 10.68`;
  `f₃(2, 6) = Δ_6 = L_6² · (1 − (π/6) \cot(π/6))
  = 36 · (1 − \sqrt{3}\,π/6) ≈ 3.35`. Distinct. ✓

⊣

(Closed-form data per
[corners/HURWITZ-FIRST-BAND-CONCENTRATION.md](corners/HURWITZ-FIRST-BAND-CONCENTRATION.md);
no monotonicity claim is needed beyond a single fiber pair.)

**§5 faces that are not directly K2 instances.** Two of the §5 faces
in [measure/SUBSTRATE-OBSTRUCTIONS.md](measure/SUBSTRATE-OBSTRUCTIONS.md)
do not transcribe to L-functions without further apparatus:

- The **Haar / `β(α)` face** (§1 of SUBSTRATE-OBSTRUCTIONS) uses
  Haar measure on `T = ℝ/ℤ` for irrational rotation orbits and the
  continued-fraction parameter `β(α)` (per
  [rotations/10-MARTINIS-BRIEF.md](rotations/10-MARTINIS-BRIEF.md)).
  This is *not* "Haar on `(ℤ/nℤ)*`" and is not naturally a function
  on the integer-indexed lattice `L`. To make it a K2 instance,
  the kernel would need a transport from rotation-orbit content
  to L-observables. Open.
- The **L-W null/full face** (§5 of SUBSTRATE-OBSTRUCTIONS) operates
  through the algebraic-vs-transcendental dichotomy. Every
  `cos(2π/n)` for integer `n` is algebraic, so under the literal
  source-side reading the face is fiber-*constant* on `L` — it does
  not give a K2 instance. Replacing it with a finer cyclotomic-depth
  reading (Niven rationality, `[K_n : ℚ]`) does give fiber-non-
  constancy, but that content is f₁ above, not the L-W dichotomy.

**Almost-every isoperimetric register.** §2 of SUBSTRATE-OBSTRUCTIONS
includes a probabilistic "almost-every" register (Beck / Khintchine).
This is a measure operation on a parameterized family, not a scalar
observable on `L`. Rate and constant registers do give scalar
L-observables (f₂, f₃ above); the almost-every register requires
naming the parameter family before becoming a K2 instance. Restricted
to the f₂, f₃ instances, the isoperimetric face is fiber-non-constant.

The three K2 instances above are sufficient for Theorem K. The
non-instances flag scope: K is a proof for the named L-observables,
not yet a proof that all §5 substrate-side content fails to transport.

### K.3 Theorem K: σ-algebra coarsening and transport failure

> **Theorem K (σ-algebra coarsening + transport failure).** The
> reduction map `R: L → F` induces the sub-σ-algebra
> `R⁻¹(2^F) ⊂ 2^L`. A function `f: L → V` factors through `R` (lies
> in `R^*(M(F))`) iff it is `R⁻¹(2^F)`-measurable, iff it is
> fiber-constant. The L-observables `f₁, f₂, f₃` of K2 are not
> fiber-constant, hence not in `R^*(M(F))`. An apparatus that reads
> only on `R⁻¹(2^F)` cannot recover any of `f₁, f₂, f₃`.

*Proof.* The σ-algebra equality `R⁻¹(2^F) =` (fiber-constant sets)
is routine: any `R⁻¹(S)` is a union of fibers; any union of fibers
is `R⁻¹` of its image. Combined with K1 (functions measurable for a
σ-algebra of fiber-constant sets are themselves fiber-constant) and
K2 (f₁, f₂, f₃ are not fiber-constant), the conclusion follows. ∎

### K.4 Operative consequence

A hypothetical apparatus that lower-bounds `T(P)` by reading only
F-side decoration (denominator-rank, Thomae height, Stern-Brocot
depth, `?`-derivative) is restricted to the sub-σ-algebra
`R⁻¹(2^F)`. Theorem K says cyclotomic-ladder depth, polygon
perimeter, and isoperimetric gap rate are not in that sub-σ-algebra.
So the apparatus cannot reconstruct those L-observables from F-side
data. That is genuine information loss under reduction.

This is the measure-theoretic content of *Stern-Brocot land eats
measure for breakfast*: not the Lebesgue-nullness of the rationals
(which is true but not by itself the obstruction), but the
σ-algebra coarsening that fiber-collapses L-observables.

**Caveat on what this is not.** Theorem K is a model instance of
information loss under a single operational reduction `R`. The full
impossibility-theorem bridge requires more: a faithful boundary
object with `δ`-coordinate per
[measure/THE-FIRST-BRIDGE.md](measure/THE-FIRST-BRIDGE.md), tying
closure, drift, and source-side obstruction together. K does not
yet construct that bridge. K demonstrates that *one specific
crossing* (the Stern-Brocot side) genuinely loses L-observable
content; whether other apparatus can recover the same content
through other channels is a separate question. The σ-algebra
coarsening is a useful piece of the load-bearing measure-theoretic
proof, not yet the proof itself.

### K.5 Supporting cyclotomic-rigidity obligations

Theorem K does not depend on the cyclotomic-rigidity claims tagged
elsewhere in the memo. T1 is proved here; T2 and T3 remain open.

> **Lemma T1 (off-backbone empty contour) — proved.** For all
> integers `n ≥ 3` and `0 ≤ k < n`,
> `sec(π/n) · cos((2k+1) π / n) ≠ ±1/2`.

*Proof.* Suppose to the contrary
`sec(π/n) cos((2k+1) π/n) = ε/2` for some `ε ∈ {+1, −1}`,
i.e. `2 cos((2k+1) π/n) = ε cos(π/n)`. Square and use the
double-angle identities `2 cos²(θ) = 1 + cos(2θ)`:

```text
4 cos²((2k+1) π/n) = cos²(π/n)
2 (1 + cos((2k+1) · 2π/n)) = (1 + cos(2π/n))/2
4 cos((2k+1) · 2π/n) − cos(2π/n) = −3.        (†)
```

Both `cos((2k+1) · 2π/n)` and `cos(2π/n)` lie in
`K_n = ℚ(cos(2π/n))`. The Galois group `Gal(K_n/ℚ) = (ℤ/nℤ)*/{±1}`
acts on each. If (†) holds in `K_n`, then summing the LHS over
Galois conjugates (the trace from `K_n` to `ℚ`) gives a rational
equation; using
`Trace_{K_n/ℚ}(cos(2π m/n)) = (1/2) c_n(m)` where `c_n` is the
Ramanujan sum, this is

```text
2 c_n(2k+1) − (1/2) c_n(1) = (φ(n)/2) · (−3)
4 c_n(2k+1) = μ(n) − 3 φ(n).                (‡)
```

Apply Ramanujan's closed form
`c_n(r) = μ(h) φ(n) / φ(h)` with `h = n / gcd(n, r)`. Substituting
into (‡) and dividing by `φ(n)`,

```text
4 μ(h) / φ(h) = μ(n)/φ(n) − 3.              (§)
```

For `n ≥ 3`, `φ(n) ≥ 2` and `|μ(n)| ≤ 1`, so `|μ(n)/φ(n)| ≤ 1/2`,
and the RHS of (§) lies in `[−7/2, −5/2]`. The RHS is therefore
strictly negative, forcing `μ(h) = −1` (so `h` is squarefree with
an odd number of prime factors). Then (§) becomes
`4/φ(h) = 3 − μ(n)/φ(n) ∈ [5/2, 7/2]`. Enumerate `h` with
`μ(h) = −1`:

- `h = 2`: `φ(h) = 1`, `4/φ(h) = 4`. Outside `[5/2, 7/2]`. ✗
- `h = 3`: `φ(h) = 2`, `4/φ(h) = 2`. Outside. ✗
- `h = 5`: `φ(h) = 4`, `4/φ(h) = 1`. Outside. ✗
- `h = 7, 11, 13, …` (single prime, μ = −1): `φ(h) = h − 1 ≥ 6`,
  `4/φ(h) ≤ 2/3`. Outside. ✗
- `h = 30, 42, 66, …` (three distinct primes, μ = −1): `φ(h) ≥ 8`,
  `4/φ(h) ≤ 1/2`. Outside. ✗

No squarefree `h` with `μ(h) = −1` makes `4/φ(h)` land in
`[5/2, 7/2]`. Equation (§) has no solution. ∎

*Note on the path.* Niven's theorem (rational `cos(rπ)` ⟹
`cos(rπ) ∈ {0, ±1/2, ±1}`) does not directly imply T1: T1 is a
rational ratio of two cyclotomic cosines, not the rationality of
one. The trace/Ramanujan reduction above is the clean route; the
divisibility-by-4 test alone does not suffice (some `n` pass it),
but the φ(h)-bound argument above is uniform.

> **Lemma T2 (thin-sweep all-N) — open, proof target.** For slope
> `s = 1/√3` and the sweep coordinate
> `c_{n,k} = sec(π/n) − 1 − s · (2k+1)/(2 n)`, distinct
> `(n, k), (n', k')` give `c_{n,k} ≠ c_{n', k'}`.

*Status.* Empirical floor `≈ 1.4 × 10⁻⁷` through `n ≤ 100` (per
[n-gons/counting/THICK-SWEEP.md](n-gons/counting/THICK-SWEEP.md)),
no exact coincidence observed. The all-`N` claim is **not**
parallel to T1: adjoining `s = 1/√3` introduces `√3 ∈ ℚ(ζ_{12})`,
which can already live inside relevant cyclotomic composita with
cyclotomic cosines. The Galois-sum reduction does not close cleanly;
the obstruction is a real-quadratic-field intersection problem
inside cyclotomic composita, not a Ramanujan-sum / divisibility
contradiction. Treat as proof target only.

> **Lemma T3 (`x`-support / trace-field ψ compatibility) — open.**
> For the ψ-stratification at
> [n-gons/counting/PSI-STRATIFICATION.md](n-gons/counting/PSI-STRATIFICATION.md),
> the plotted `x`-support `x_{n,k} = sec(π/n) cos((2k+1)π/n)` is
> compatible with the trace-field-degree reading through ψ.

*Status.* `K_{2n} = ℚ(cos(π/n))` can be a quadratic extension of
`K_n = ℚ(cos(2π/n))`. The full strip-height `sec(π/n) − 1` lives in
`K_{2n}`; the *plotted* `x`-support is the odd-Chebyshev quotient
`cos((2k+1)π/n) / cos(π/n)`, which lies in `K_n` by the following
**odd-Chebyshev factorization**: the odd Chebyshev polynomial
`T_{2k+1}(X)` has zero constant term, so `T_{2k+1}(X) / X ∈ ℚ[X²]`,
and substituting `X = cos(π/n)` gives
`cos((2k+1)π/n) / cos(π/n) = (T_{2k+1}(X)/X)|_{X = cos(π/n)}`,
a polynomial in `cos²(π/n) = (1 + cos(2π/n)) / 2 ∈ K_n`. So the
figure's `x`-support is trace-field-readable, even though
`cos(π/n)` itself can sit one level higher in `K_{2n}`. The ψ
stratification is a coloring of `n` by the additive bridge function
`ψ(n)`, distinct from `[K_n : ℚ]` per
[BNHA/triad/Creati/CREATI-THE-CIRCLE.md](BNHA/triad/Creati/CREATI-THE-CIRCLE.md).
The compatibility lemma is the precise statement that the ψ-coloring
and trace-field-degree reading agree on the qualitative content
they share. Verified case-by-case at low `n`; uniform statement is
open. T3 is **not** the claim "`K_n` and `K_{2n}` agree" (they don't
in general); it is the claim "the plotted `x`-support is
trace-field-readable via odd-Chebyshev factorization, and ψ is a
bridge function on top of that reading."

### K.6 Open: shared state space, boundary object, coordinate posture

The agent review noted that the previous T4 conflated two distinct
tasks. Split into T4a (achieved trivially) and T4b (the genuine open
problem); T6 is correspondingly softened.

> **T4a (common indexing domain) — trivial / achieved.** The
> integer-indexed lattice `L` is a shared state space for the K2
> observables `f₁, f₂, f₃`.

Trivial because each is already defined on `L`. T4a is *not* the
"common boundary object" of THE-FIRST-BRIDGE; it is just the
indexing domain on which the kernel's three concrete observables
live.

> **Open T4b (common boundary object with `δ`-faithfulness).**
> Construct a measure space `(Z, ℱ, μ)` together with a `δ`
> coordinate satisfying THE-FIRST-BRIDGE's faithful-measurable-
> coordinate condition, such that the §5 substrate-side observables
> factor through `δ` and the program's closure-class membership
> reads measurably against `(Z, ℱ, μ, δ)`.

Per [measure/THE-FIRST-BRIDGE.md](measure/THE-FIRST-BRIDGE.md),
this is the genuinely load-bearing measure-theoretic statement the
program needs: a boundary object on which closure preservation,
drift, and source-side obstruction can be jointly typed. The
present kernel does not construct it. T4a (the indexing domain) is
necessary but not sufficient for T4b.

> **Open T6 (boundary upstream of any `δ`-coordinate).** The
> substrate-side discontinuity is upstream of any specific
> `δ`-algebra: a different reasonable coordinate would chart the
> same boundary in different shape, but the boundary-as-set is
> coordinate-independent.

Per
[measure/COASE-FRICTION-AND-SPECIALISTS.md](measure/COASE-FRICTION-AND-SPECIALISTS.md)
and
[measure/ALGEBRA-OF-DELTA.md](measure/ALGEBRA-OF-DELTA.md), the
Coase posture supports this upstream-ness as a *posture*, not a
theorem. T6 is the upstream-ness statement only. The stronger claim
"all reasonable `δ`-algebras yield the same impossibility region at
`T(P)`" is a separate invariance theorem **not** entailed by the
Coase posture, and would need to be earned by direct argument
against each candidate algebra. The kernel keeps T6 in the weaker
form.

**Tracked as construction-debt #15** in `paper/OUTLINE.md` and
`paper/PROOF-CHAIN.md`; committed via **route 3** (recursion-theoretic
horizon absorption per the §Conclusion / §7 outflow): the extensional
question "do all reasonable δ-algebras agree?" is Rice-flavored
("reasonable" is not syntactically decidable), so T6 sits at the same
horizon as channel exhaustiveness #11(iii) and cost-norm uniformity
#14. The `paper/OUTLINE.md` §4.5 / `paper/PROOF-CHAIN.md` working
theorem holds on the syntactic δ-algebra (cocycle realization at
`fft/PHASE-DEFECT.md`); lifting to the extensional class meets the
recursion-theoretic horizon. Route 3 does not foreclose later upgrades
to direct invariance per candidate algebra or finite-list verification
if a stronger claim becomes available.

### Summary of the kernel

| Object | Role | Status |
|---|---|---|
| `R: L → F` | the reduction step as measurable map | defined |
| `R^*` pullback functor | F-side data lifted to `L` | defined |
| `R⁻¹(2^F)` sub-σ-algebra on `L` | the coarsening induced by `R` | defined |
| K1 (fiber-constant characterization) | algebraic core of the kernel | proved |
| K2 instances f₁, f₂, f₃ | concrete L-observables, fiber-non-constant | proved |
| **Theorem K (σ-algebra coarsening + transport failure)** | **central kernel theorem** | proved for f₁, f₂, f₃ |
| Haar/β face as K2 instance | not directly an L-observable | open transport |
| L-W null/full as K2 instance | fiber-constant on `L` under literal source reading | not directly K2-eligible |
| T1 (off-backbone empty) | supporting cyclotomic rigidity | **proved** (trace/Ramanujan + φ(h) bound) |
| T2 (thin-sweep all-N) | parallel rigidity claim, *not* parallel to T1 | open; quadratic-irrationality intersection problem |
| T3 (`x`-support / ψ compatibility) | depth-stratification compatibility | open |
| T4a (common indexing domain `L`) | indexing-side prerequisite | trivial / achieved |
| T4b (boundary object with `δ`-faithfulness) | promotes K to THE-FIRST-BRIDGE form | **open; load-bearing** |
| T6 (boundary upstream of `δ`) | weaker upstream-ness only; stronger cross-chart invariance tracked as `paper/OUTLINE.md` debt #15 (route 3) | open posture-statement; debt #15 absorbs the stronger form into the §Conclusion outflow as a Rice-flavored sub-question |

Theorem K is a σ-algebra coarsening result: it shows information
loss under one specific operational reduction `R`. T1 is now a
cleanly-proved cyclotomic-rigidity lemma. T2 and T3 remain open;
T2's path is genuinely harder than T1's. T4b is the load-bearing
piece toward THE-FIRST-BRIDGE — the kernel's main theorem here is
necessary infrastructure, not a substitute for the bridge. T4a is
trivially achieved and should not be confused with T4b. T6 is the
weakened upstream-of-coordinate posture, not the stronger
impossibility-region invariance.

## Adjacent anchors

- [n-gons/counting/THICK-SWEEP.md](n-gons/counting/THICK-SWEEP.md) — the boundary in one figure.
- [BNHA/triad/Eraserhead/ARCHIMEDEAN-CONSTRICTION.md](BNHA/triad/Eraserhead/ARCHIMEDEAN-CONSTRICTION.md) — the discipline holding the line.
- [n-gons/N-GON-WHOLENESS.md](n-gons/N-GON-WHOLENESS.md) — operative apparatus on the rigid side.
- [BNHA/triad/Eraserhead/BIND-THE-CIRCLE.md](BNHA/triad/Eraserhead/BIND-THE-CIRCLE.md) — the explicit refusal list.
- [measure/SUBSTRATE-OBSTRUCTIONS.md](measure/SUBSTRATE-OBSTRUCTIONS.md) — the §5 substrate-side typing as five faces of integer-indexed rigidity.
- [measure/COASE-FRICTION-AND-SPECIALISTS.md](measure/COASE-FRICTION-AND-SPECIALISTS.md) — substrate vs coordinate posture.
- [measure/ALGEBRA-OF-DELTA.md](measure/ALGEBRA-OF-DELTA.md) — the algorithm-side coordinate's algebra.
- [memos/NATIVE-F-MINIMAL-DEFINITION.md](memos/NATIVE-F-MINIMAL-DEFINITION.md) — cyclotomic-ladder-vs-affine-closure as the integer-vs-continuum asymmetry.
- [memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md) — sibling content-not-calendar discipline.

## Trust boundary

This memo is a sensitizer, not a theorem. It does not prove that
crossing the regime boundary necessarily fails — arguments can be
legitimately committed to the Stern-Brocot side. It does not prove
that the integer-indexed regime is the unique substrate where the
program's refusals could work. It does not exhaust the witnesses to
the regime boundary in the repo. It points at a fact that is deeply
embedded in the program's vocabulary and methodology, and gives
operative diagnostics for recognizing the boundary in future work.

The substrate-side fact itself — that algebraic-arithmetic rigidity
at integer-indexed labels is what gives the §5 refusals and the
bounded-coefficient lower bounds their load-bearing content — is
upstream of any specific theorem in the repo. **Theorem K** is the
measure-theoretic content of that upstream-ness on the §5 face; the
upstream-of-coordinate framing is **open T6**. The witnesses
[THICK-SWEEP, ARCHIMEDEAN-CONSTRICTION, N-GON-WHOLENESS, the §5
angles, Morgenstern's argument, the cyclotomic ladder] each show
one face of the same rigidity; the rigidity itself is the
substrate-side fact, and any reasonable coordinate (the cocycle
realization at PHASE-DEFECT, the bounded-coefficient determinant
ledger, the Haar-on-orbit reading) charts it without constituting
it (T6).
