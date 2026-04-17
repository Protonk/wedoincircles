# CONTINUITY

A working directory for real-valued continuations of integer constructions. The program's n-gon constructs (see `n-gons/README.md`) are indexed by integers. Many admit a natural continuous reading: replace n ∈ ℤ with a real t and see what changes, what stays, and how the integer samples relate to the continuous object they live on. Some do not; that resistance is part of what this directory is for.

## The idea

Most n-gon constructs (`tangencies/`, `corners/`) are integer-indexed. When a geometric construction admits a natural continuous reading, replace n with real t and keep the construction well-defined. Then:

- The integer samples become discrete points on a smooth curve (or surface).
- The resulting curve is often analytically well-behaved: smooth, monotone, with identifiable asymptotics.
- The integer samples have arithmetic content the curve itself does not carry.
- The relationship between the smooth curve and its integer samples is a relationship between smooth analysis and arithmetic depth.

The continuations are often obvious geometrically and much less obvious arithmetically. In favorable cases, integer t gives algebraic output with depth controlled by the factorization of t or some related discrete invariant, while rational t gives a denser algebraic sampling of the same curve. Other constructions behave differently, and some have no canonical real continuation at all.

## First case: pseudo-Chebyshev continuation

The pseudo-Chebyshev construction (`corners/PSEUDO-CHEBYSHEV-NODES.md`) produces one node per integer n ≥ 2 via the segment from the origin to the n-gon corner (1, tan(π/n)). The segment crosses the unit circle at (cos(π/n), sin(π/n)); the node is the x-coordinate, node(n) = cos(π/n).

Continuation: replace n with real t ∈ [2, ∞). The corner (1, tan(π/t)) sweeps continuously down the vertical line x = 1 as t grows. The crossing point (cos(π/t), sin(π/t)) sweeps along the upper-right quarter of the unit circle, from (0, 1) at t = 2 to (1, 0) in the limit t → ∞.

In node-sequence coordinates (horizontal = node value x, vertical = n):

    n(x) = π / arccos(x)    equivalently    x(n) = cos(π/n),  n ∈ [2, ∞)

Shape. Starts at (0, 2). Passes through (1/2, 3), (√2/2, 4), ((1+√5)/4, 5), (√3/2, 6), (cos(π/7), 7), … As a graph of n(x), it is monotone increasing and convex, with vertical asymptote x = 1 as n → ∞. Near x = 1 it rises like n ~ π/√(2(1−x)).

Arithmetic density along the curve. Integer t = n gives an algebraic node of degree φ(2n)/2 (see `corners/PSEUDO-CHEBYSHEV-NODES.md`). More generally, rational t = p/q ≥ 2 in lowest terms gives

    node(t) = cos(πq/p),

an algebraic value whose degree is φ(m)/2, where m = 2p / gcd(q, 2) is the order of e^{iπq/p}. So rational parameters give a dense countable set of algebraic node values.

On the other hand, x = cos(π/t) is strictly increasing on t ∈ [2, ∞), so each node value x ∈ [0, 1) comes from exactly one parameter t = π / arccos(x). Since the algebraic numbers form a countable set, only countably many parameters can produce algebraic node values at all. Every other parameter produces a transcendental node value. By Niven's theorem, the *only* rational node values on t ∈ [2, ∞) are node(2) = 0 and node(3) = 1/2.

So the pseudo-Chebyshev continuation is a smooth analytic curve carrying a dense countable set of algebraic node values, a dense co-countable set of transcendental node values, and exactly two rational node values.

## Why the pattern matters

Integer-indexed constructions carry two kinds of content simultaneously: a smooth reading (the curve they live on, viewed as a function of real t) and an arithmetic reading (the algebraic depth of integer samples, determined by factorization). Continuations hold both in view at once.

When a program move crosses from smooth analysis into arithmetic claims — or vice versa — the continuation is where the crossing happens. Observations about the curve's smooth properties (derivatives, asymptotics, Fourier structure) sometimes transfer to observations about integer samples, and sometimes don't. The transfer pattern is itself the kind of thing the F question cares about. The pseudo-Chebyshev continuation is the first concrete object where we can watch the pattern on a small scale.

## Candidate continuations to draft next

- **The n-gon construction itself** (`tangencies/WHOLENESS.md`). A "real-t-gon" is geometrically meaningful at rational t = p/q in lowest terms as a {p/q} star polygon: the rotation closes after p steps. At irrational t there is no closed polygon, only an infinite rotation orbit. The 3DT lens (`memos/3DT-BRIEF.md`) is the natural frame for finite orbit prefixes: their gap structure is exactly what 3DT describes.
- **The residue τ(n) = 2cos(2π/n) − round(2cos(2π/n)).** Real-t version: τ(t) is piecewise-smooth, with the `round` kink producing a sawtooth-like set of discontinuities whose locations are arithmetic data in their own right.
- **Constructs that resist continuation.** The divisor-indicator b_n(DH) = 𝟙[n | DH] does not admit an obvious or canonical smooth real continuation — divisibility is purely discrete. The crystallographic function ψ(n), defined via prime factorization, has no obvious real-valued analogue of the same kind. Resistance is itself a finding; entries explaining why belong here.

Each case lands as its own file, with a sage demonstration where geometry permits one.

## This is a reading frame, not a discipline

The triad (BIND / CREATI / PERMEATE) lives in `../BNHA/triad/`. Continuity is a reading frame — it says what kind of object we are looking at when we hold integer-indexed and real-continuous readings side by side. Discipline-appropriate treatment of a continuation depends on which discipline is asking. CREATI wants closed forms for curve and samples. BIND wants Erasure-legal tools for the integer/real crossing. PERMEATE wants saturation tables covering integer samples plus nearby rational continuations to anticipate curve behavior.

## Demonstration

The real-continuation of the pseudo-Chebyshev construction is plotted by `corners/pseudo_chebyshev_continuity.sage`; output lands at `figures/pseudo_chebyshev_continuity.png`. The figure shows the smooth curve with integer samples overlaid, in both the unit-circle geometric pane and the node-sequence pane.
