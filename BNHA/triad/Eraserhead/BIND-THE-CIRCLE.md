# BIND-THE-CIRCLE

A research program pursuing the τ_c / ε spectral-rhyme candidate for a functor F between the log-side (Landfall) and circle-side (NGON-WHOLENESS) obstructions, under the Erasure discipline.

---

**Pointer.** BIND pursues one leg of a three-candidate approach. The abstract triad pattern — identity / polynomial closure (CREATI), arithmetic matching (PERMEATE), and residue / spectral rhyme (this doc) — is in `BNHA/triad/TRIAD-ABSTRACT-PATTERN.md`. BIND is the home of Leg 3 only; the other legs are not pursued here.

**Complementarity note.** BIND, CREATI, and PERMEATE are complementary disciplines by design, not by convergence. Each imposes a different productive constraint: BIND's is **vocabulary** (Erasure: no ?(x), Farey, SB, Thomae, Denjoy), CREATI's is **form** (every object a count, closed form, or identity), PERMEATE's is **preparation** (no cross-domain move without the saturation table behind it). Future lemmas will need to state what each reaches that the others cannot. This doc tolerates those gaps rather than papering them over.

**Working hypothesis (Leg 3 local).** Spectral rhyme fails because τ_c's spectrum is dominated by features the log rep A = 3.6·10^E chose (Babylonian fossil), not by features intrinsic to the circle. Any F matching spectra is matching representational artifacts. The goal is to name this failure mode with a computable invariant. The global "does F exist?" question sits at the triad level, not here.

---

## Constraints on method (Aizawa)

The program is conducted with ?(x) erased. No Minkowski question-mark function, no Stern-Brocot tree, no Farey sequence, no Thomae / popcorn function, no Denjoy construction, no dyadic expansions reinterpreted as continued fractions. These are the shared vocabulary that makes the two sides look alike; their absence forces us to work with primitives from each side in its own voice.

The discipline is sustained: the shared vocabulary may not re-enter the working notes even as shorthand. If it does, the Erasure has broken and the argument restarts from primitives.

What Erasure is actually enforcing is a symmetry that is easy to violate: both sides have *representations* (the log representation on the Landfall side, lattice and grid representations on the circle side), and legal tools should treat representation as something both sides have. Tools that live on one side only and are imported onto the other are in bounds. Tools that live in the shared vocabulary — mostly ?(x)-family objects — are not.

Primitives on the log side: floating-point representation, ε(m) = log₂(1+m) − m, rounding modes, carry chains, mantissa arithmetic, and the extended-real infinity structure at the abstract level (projective vs. affine closure of ℝ), independent of which closure any given IEEE 754 revision standardizes.

Primitives on the circle side: Euclidean lattice vectors, integer trace constraints on rotation matrices, regular polygon incircle tangencies, divisibility n | DH, the ψ-function from the crystallographic restriction theorem (Bamberg–Cairns–Kilminster 2003: ψ(n) > d forces n-fold rotational symmetry to be incompatible with any d-dimensional Euclidean lattice), and the space of 2D Euclidean lattices Γ\SL(2, ℝ) with Γ = SL(2, ℤ) — including lattice-geometric theorems proved on it, such as the Three Distance Theorem via Marklof–Strömbergsson 2017 (see below).

## The toe-hold

A fixed circle, circumscribed by each of a family of regular n-gons (the circle is the shared incircle; each n-gon is tangent to the circle along one anchor edge, with position 0 of every n-gon coinciding at 0° on the circle). Position k of the n-gon sits at angle k·360°/n.

Plotting position k as a function of n — one curve per fixed k = 1, 2, 3, … — gives a family of hyperbolas y = 360k/n. The n=1..20 table of tangency angles, mapped onto [0, 1) by division by 360°, is an (n, k)-indexed finite object. It is not where DH structure lives. DH structure is an **overlay** applied to that table: fix DH, ask which entries land on the grid of integer multiples of 1/DH. Under that overlay we read off:

- the positional axis (DH sweeping ℤ_{≥1}),
- the logarithmic axis (DH = 3.6·10^E, E ∈ ℝ), which agrees with the positional axis at integer E (DH ∈ {36, 360, 3600}) and carries a continuous parameter off those points,
- the coincidence regime (DH ≲ 360) where the two axes probe the same divisor structure,
- the Babylonian fossil v₃(DH) ≤ 2 that survives the logarithmic parameterization — a visible coordinate-system artifact of the 3.6 choice, not a fact about the circle.

The circle-side obstruction: not every n divides a given DH (the all-positions test is n | DH). The log-side obstruction: not every mantissa value produces an ε that closes under addition. Both obstructions admit a binary test (pass/fail) and a quantitative residue (how close to passing).

The hyperbola y = k·360/n is the geometric face of a rational position k/n, and k/n is the hinge between a circle-side object (polygon tangency) and a number-theoretic object (divisor in a finite lattice). If we keep our hands on the hyperbola without reaching for the shared vocabulary, we can work in primitives on both sides at once.

## The representational symmetry

Each side has two natural operations and a representation that is clean for one and breaks the other:

- **Log side.** The reals carry + and ·. The log representation is a group isomorphism (ℝ_{>0}, ·) ≅ (ℝ, +); it makes · native in log coordinates (becomes +) but breaks +-of-original-reals (x + y is not linear in log x and log y, and the nonlinear correction is ε).
- **Circle side.** ℝ² carries additive lattice structure (ℤ^d, +) and rotational structure (SO(d), ·). The lattice representation makes + native (integer vectors) but breaks a rotation R_n generically: the trace is 2cos(2π/n), non-integer for n ∉ {1, 2, 3, 4, 6}, and the nonlinear correction is τ(n) = 2cos(2π/n) − round(2cos(2π/n)).

The two sides are **dual**: the log representation is native to · and breaks +; the lattice representation is native to + and breaks ·. Any candidate F sends one kind of brokenness to the other and has to respect this flip. That duality is the shape of the abstract correspondence. It also tells us what the earlier A/B framing was trying to say and kept getting wrong — F is not parallel across sides; it is anti-parallel, and the "native operation" role swaps. A covariant functor rhyming operation-to-operation does not exist; what might exist is a functor rhyming residue-to-residue.

## The continuous-E tool

The log DH parametrization — DH = A·10^E with E ∈ ℝ and A fixed (A = 3.6 in the current construction) — is a **representational primitive imported from the log side** onto the circle side. Under Erasure it is legal: it does not route through ?(x), Stern-Brocot, Farey, or Thomae. It is the first tool in this program that treats representation as something both sides have rather than something only one side has while the other has "geometry."

It lets us replace the binary divisibility test with a continuous residue

τ_c(n, k, E) = frac(k · A · 10^E / n),

smooth in E for each fixed (n, k). τ_c has Fourier structure, derivatives, near-zeros, critical points — the analytic machinery the binary test forecloses. It is the circle-side analog of admitting ε(m) for m ∈ (0, 1) instead of only at m = 0 and m → 1.

At integer E, τ_c collapses to the positional test: the positional and logarithmic axes agree on their intersection. Off integer E, the log axis carries a continuous family of DH values the positional axis cannot name. The useful content of this tool lives in the continuation off the intersection, not in the interchange at it.

Caveat. A = 3.6 is not canonical; it locks in v₃(DH) ≤ 2 (the Babylonian fossil). Either embrace the 3.6 fingerprint as part of what is being measured (specific-construction tool) or generalize to DH = A·10^E with A variable and study the A-family (moduli-space tool). The two readings ask different questions.

## The lattice-geometric 3DT (Marklof–Strömbergsson)

The Three Distance Theorem — that any α-rotation orbit of length N on ℝ/ℤ partitions the circle into gaps of at most three distinct lengths, with the longest equal to the sum of the other two when three appear — is usually proved combinatorially (via interval exchanges and word encodings) or algorithmically (via the Euclidean / continued-fraction expansion). Both of those routes are Erasure-adjacent to varying degrees: the combinatorial version is clean, but the algorithmic one (Lefèvre–Muller) is explicitly a continued-fraction computation, and continued fractions are Stern–Brocot-adjacent.

Marklof–Strömbergsson 2017 give a **third proof from lattice geometry alone**. For each (α, N) they construct the lattice ℤ²A_N with A_N ∈ SL(2, ℝ), define the function F on Γ\SL(2, ℝ) × (0, 1] via shortest-second-coordinate of a lattice vector in a strip, and show by a parallelogram argument (their Figure 3) that F takes at most three values r_2, s_2, r_2 + s_2 where (r, s) is a specific lattice basis. No Stern–Brocot. No Farey. No ?(x). No word encodings. No interval-exchange combinatorics. Just lattice vectors, shortest-vector minimization, and a parallelogram-containment lemma.

This means **the 3DT is Erasure-legal under BIND when taken via Marklof–Strömbergsson**. BIND did not previously have a proof of the 3DT it could cite without dropping discipline; now it does. Consequences:

- **The reflection identity d_b = d_a + d_c becomes an Erasure-legal circle-side identity.** Previously this pair lived on the CREATI side (via B–R's combinatorial proof). It now lives on the BIND side too, via r + s. BIND can pair it with the log-side ε(m) + ε(1−m) without Erasure friction.
- **Γ\SL(2, ℝ) is a first-class Erasure primitive.** The modular surface and its SL(2, ℝ)-extension are homogeneous spaces whose invariant measures descend from Haar. These are lattice-geometric objects, exactly the kind BIND's primitives list already admits. Any theorem proved on Γ\SL(2, ℝ) by finding short vectors, computing shortest-basis parallelograms, or taking SL(2, ℤ)-invariant functions is Erasure-legal.
- **The 3DT sits on the "invariant-measure-technique-works" side of the homogeneous-dynamics divide.** Contrast with Landfall §6 (Bowen 2002): the binary tiling space has no PSL(2, ℝ)-invariant probability measure. Γ\SL(2, ℝ) does. BIND inherits both cases as concrete examples of when invariant-measure aggregation succeeds and when it fails, which sharpens the INSCRIPTION-level §6 mechanism question into a question about *which specific homogeneous space* the obstruction lives on. See `BNHA/triad/Creati/INSCRIPTION-PAPER-PLAN.md` for the paper-side framing.

The upshot for Leg 3 specifically: τ_c and ε can be studied alongside the 3DT's finite-valued function F on Γ\SL(2, ℝ), all under the same Erasure-legal vocabulary. If τ_c's spectrum admits a lattice-geometric reading on Γ\SL(2, ℝ) — whether directly or through some related homogeneous space — that's a spectral-rhyme candidate BIND can pursue without importing shared vocabulary. The continuous-E tool stays, the lattice-geometric 3DT joins it, and the cross-check between them becomes a concrete Leg 3 task.

Pointer for the ring-theoretic / geometric details: `memos/3DT-BRIEF.md` §"The third angle: 3DT from the space of lattices (Marklof–Strömbergsson 2017)".

## What has to happen next

### Step 1. Formalize each obstruction in native primitives.

On the log side: state the obstruction using ε(m), the IEEE-level representation, and the carry-chain structure. Import from Landfall without modification.

On the circle side: state using lattice vectors, rotation matrices, the trace constraint, and Bamberg–Cairns–Kilminster ψ. [PLUS ULTRA]

The two formalizations must be written without reference to each other and without shared vocabulary. Each must be checkable from inside its own domain by a specialist who does not care about the other side.

### Step 2. Name and type Leg 3's candidate.

Leg 3's F sends log-side residues (broken-+ in the log rep) to circle-side residues (broken-× in the lattice rep) via **spectral invariants** — Fourier moduli, decay rates, symmetry classes — rather than pointwise values. The duality in §The representational symmetry is the shape F must respect: log and lattice reps are dual in which operation they preserve, and F transports across the flip. [PLUS ULTRA]

F must be named explicitly and typed. Ambiguity at this step is fatal: a vaguely specified candidate cannot be either constructed or obstructed, and the Leg 3 attack collapses into analogy. The other candidate F's (Leg 1 Chebyshev, Leg 2 crystallographic ↔ p-adic) are not pursued here.

### Step 3. Compute F on small cases.

Pick three to five specific log-side residues at known m and three to five circle-side residues — either τ(n) at specific n, or τ_c(n, k, E) along a slice in E. Apply F. Check whether the image is what the native side produces. [PLUS ULTRA]

Concrete first pass: plot τ_c(n, 1, E) for n ∈ {5, 7, 8, 9} on E ∈ [0, 4]; plot ε(m) on m ∈ (0, 1); look for qualitative features that rhyme (period lengths, decay rates, near-zero density, symmetries). This is cheap evidence no ?(x)-based attempt can produce.

Second concrete first pass (lattice-geometric): for the same n values, take α = 1/n and N = n, construct the lattice ℤ²A_N per Marklof–Strömbergsson, find the two basis vectors (r, s) that minimize the relevant second-coordinate, read off the three 3DT distances as r_2, s_2, r_2 + s_2. Compare against ε(m) at matched m values. This route uses only lattice vectors, shortest-vector arguments, and SL(2, ℤ)-invariance — fully Erasure-legal — and provides a second channel into the spectral-rhyme question that runs independent of the continuous-E tool. If the two channels agree, Leg 3 has internal coherence; if they disagree, the disagreement is the finding.

The Lynch method is correct here — the answer emerges from accumulated close attention to small paired cases, not from categorical bookkeeping. Aizawa cancels ?(x); Lynch stares at what's left.

Outcomes:
- F works case-by-case, and the question becomes whether it extends.
- F fails on a specific case, and the specific case tells us why.

Failures are the most informative results.

### Step 4. Construct Leg 3 or name its obstruction.

**If Leg 3 succeeds.** Give a closed-form spectral invariant pairing: a decay exponent, a symmetry under an involution, or a Fourier relation that τ_c and ε share, checkable on a finite window. State the categorical setting. Verify that the invariant respects composition. Identify what the pairing preserves and what it distorts. [PLUS ULTRA]

**If Leg 3 fails.** Construct a specific invariant on each side such that any spectral map between the two obstruction structures must either respect both invariants or fail. The Babylonian fossil — v₃ ≤ 2 on the log-DH axis — is a coordinate artifact of 3.6·10^E. The circle-side ψ-constraint is a geometric invariant of any lattice in dimension d. A spectral F would need to send the coordinate artifact to the geometric invariant; the guess is that this cannot be done naturally, and Leg 3's obstruction is an explicit computation of how much the coordinate artifact differs in kind from the geometric invariant. [PLUS ULTRA]

The computation of this difference is the missing center of Leg 3. The other legs' obstructions, if they share this mechanism, triangulate to the triad-level result in `BNHA/triad/TRIAD-ABSTRACT-PATTERN.md`. [PLUS ULTRA]

### Step 5. Write the result in the voice of the primitives.

No Stern-Brocot pictures. No popcorn function. No grand unification. The paper shows two constraints, one on each side, and either the map between them or the obstruction to the map. The surrounding argument is built from primitives of each domain, with the shared vocabulary deliberately withheld.

The rhetorical risk: the result will be harder to explain than the corresponding "both are ?(x)" claim would be. That is the point. The harder explanation is the one that has earned its keep.

## What we do not yet know

The right category on each side. Whether "natural transformation" is the right level of abstraction, or whether a coarser correspondence (a map of invariants, not of full structures) is the honest description. Whether the circle-side literature already contains an object that does what F would do, published under different vocabulary. Whether the Babylonian fossil has a counterpart on the circle side we are failing to see because we erased the shared vocabulary too eagerly. Whether τ_c's continuous-E structure admits a closed-form Fourier or spectral invariant that matches ε's.

Each of these is a Lynch problem: it resolves through sustained attention to specific objects, not through fast categorical reasoning. [PLUS ULTRA]

## Deliverable shape

A note, scoped to Leg 3, that contains:

1. The n-gon / hyperbola toe-hold, stated in circle-side primitives.
2. The ε(m) framework, stated in log-side primitives.
3. The representational-symmetry framing (duality, residues, anti-parallel F).
4. The continuous-E residue τ_c as the cross-side representational tool.
5. Leg 3's candidate F, named and typed.
6. Small-case spectral evidence, for or against.
7. The main result: Leg 3 construction, or Leg 3 obstruction with computable invariant.
8. A discussion that does not reach for the shared vocabulary to explain the result, with a pointer to `BNHA/triad/TRIAD-ABSTRACT-PATTERN.md` for the triad-level synthesis.

Length target: short. The Aizawa method produces dry, ugly writeups. That is correct.
