# BIND-THE-CIRCLE

A research program to either construct or obstruct a functor F between the log-side and circle-side versions of an obstruction that superficially appears to be the same object in both domains. Working hypothesis: F does not exist and the obstruction-to-F is the real result.

## Constraints on method (Aizawa)

The program is conducted with ?(x) erased. No Minkowski question-mark function, no Stern-Brocot tree, no Farey sequence, no Thomae / popcorn function, no Denjoy construction, no dyadic expansions reinterpreted as continued fractions. These are the shared vocabulary whose presence makes the two sides look alike; their absence is what forces us to work with primitives.

Primitives on the log side: floating-point representation, ε(m) = log₂(1+m) − m, rounding modes, carry chains, mantissa arithmetic, IEEE 754 projective vs. affine infinity.

Primitives on the circle side: Euclidean lattice vectors, integer trace constraints on rotation matrices, regular polygon incircle tangencies, divisibility of DH by n, the ψ-function from the crystallographic restriction theorem.

The discipline is sustained: the shared vocabulary may not re-enter the working notes even as shorthand. If it does, the Erasure has broken and the argument must restart from primitives.

## The toe-hold

We have a construction. A circle inscribed by regular n-gons, each anchored at a shared edge so that position 0 of every n-gon coincides at 0°. Position k of the n-gon sits at angle k·360°/n.

Plotting position k as a function of n produces a hyperbola: y = 360k/n. The n=1..20 table of tangency angles, mapped onto the [0,1) interval by division by 360°, is a finite object in which we can identify:

- the positional axis (DH sweeping the integers),
- the logarithmic axis (DH = 3.6·10^E, sampling the positional axis at integer E),
- the coincidence regime (DH ≲ 360) where the two axes probe the same divisor structure,
- the Babylonian fossil (v₃(DH) ≤ 2) that survives the logarithmic parameterization and is the visible face of a coordinate-system artifact.

The circle-side obstruction is that not every n produces tangency angles divisible by the designated grid DH. The log-side obstruction is that not every mantissa value produces an ε that closes under addition. Both obstructions admit a binary test (pass/fail) and a quantitative residue (how close to passing).

This is the toe-hold. The hyperbola y = k·360/n is the geometric face of a rational position k/n. The rational position is the hinge between a circle-side object (polygon vertex) and a number-theoretic object (divisor in a finite lattice). If we keep our hands on the hyperbola without reaching for the shared vocabulary, we can work in primitives on both sides simultaneously.

## What has to happen next

### Step 1. Formalize each obstruction in native primitives.

On the log side: state the obstruction using ε(m), the IEEE representation, and the carry-chain structure. This has been done in earlier work. Import the formalization without modification.

On the circle side: state the obstruction using lattice vectors, rotation matrices, and the trace constraint. The Bamberg-Cairns-Kilminster (2003) formulation via the ψ-function is the right starting point. The obstruction is: ψ(n) > d forces n-fold rotational symmetry to be incompatible with any d-dimensional Euclidean lattice. [PLUS ULTRA]

The two formalizations must be written without reference to each other, and without shared vocabulary. Each must be checkable from inside its own domain by a specialist who does not care about the other side.

### Step 2. Identify the candidate correspondence.

Both sides share the following abstract shape: a generator of group A cannot be expressed exactly in coordinates native to group B, and the failure has a measurable residue. On the log side, A is the additive group of reals and B is the multiplicative (logarithmic) representation. On the circle side, A is the rotation subgroup of order n and B is the additive lattice.

The candidate F would send: log-side obstructions to circle-side obstructions, log-side residues to circle-side residues, log-side composition of obstructions to circle-side composition. [PLUS ULTRA]

The candidate F must be named explicitly and checked against its intended domain and codomain. Ambiguity at this step is fatal — a vaguely specified functor cannot be either constructed or obstructed, and the whole program collapses into analogy.

### Step 3. Compute F on small cases.

Take three to five specific log-side obstructions where ε(m) has known structure. Take three to five specific circle-side obstructions where ψ(n) has known structure. Apply F. Check whether the image is what the circle side produces natively. [PLUS ULTRA]

This step is slow. Each case requires sitting with one specific object on each side until it reveals what it does under F. The Lynch method is correct here — the answer emerges from accumulated close attention to small paired cases, not from categorical bookkeeping. Aizawa cancels ?(x); Lynch stares at what's left.

The outcome of this step is either:
- F works case-by-case, and the question becomes whether it extends to a full functor;
- F fails on a specific case, and the specific case tells us why.

Failures here are the most informative results of the program.

### Step 4. Construct F or construct the obstruction to F.

Two branches.

**F exists branch:** give a natural-transformation-level construction of F, compatible with the small-case computations. State the categories explicitly. Verify functoriality on composition. Identify what F preserves and what it distorts. [PLUS ULTRA]

**F does not exist branch:** construct a specific invariant on the log side and a specific invariant on the circle side, such that any natural map between the two obstruction structures must either respect both invariants or fail functoriality. Show that no map can respect both. The obstruction-to-F is then this specific pair of invariants plus the incompatibility argument. [PLUS ULTRA]

The no-F branch is where the program's discipline pays off. The Babylonian fossil — the v₃ ≤ 2 cap on the log side — is a coordinate artifact of the 3.6·10^E parameterization. The circle-side ψ-constraint is a geometric invariant of any lattice in dimension d. A functor would need to send the coordinate artifact to the geometric invariant. The guess is that this cannot be done naturally, and the obstruction-to-F is an explicit computation of how much the coordinate artifact differs in kind from the geometric invariant.

The computation of this difference is the missing center of the program. [PLUS ULTRA]

### Step 5. Write the result in the voice of the primitives.

No Stern-Brocot pictures. No popcorn function. No grand unification. The paper shows two constraints, one on each side, and either the map between them or the obstruction to the map. The surrounding argument is built from the primitives of each domain, with the shared vocabulary deliberately withheld.

The rhetorical risk: the result will be harder to explain than the corresponding "both are ?(x)" claim would be. That is the point. The harder explanation is the one that has earned its keep.

## What we do not yet know

We do not know the right category on each side. We do not know whether the "natural transformation" language is even the right level of abstraction, or whether a coarser correspondence (a map of invariants, not of full structures) is the honest description. We do not know whether the circle-side literature already contains an object that does what F would do, published under different vocabulary. We do not know whether the Babylonian fossil has a counterpart on the circle side that we are failing to see because we erased the shared vocabulary too eagerly.

Each of these unknowns is a Lynch problem: it resolves through sustained attention to specific objects, not through fast categorical reasoning. [PLUS ULTRA]

## Deliverable shape

A note that contains:

1. The n-gon / hyperbola toe-hold, stated in circle-side primitives.
2. The ε(m) framework, stated in log-side primitives.
3. The candidate F, named and typed.
4. Small-case evidence either for or against F.
5. The main result: construction of F, or explicit obstruction-to-F with computable invariant.
6. A discussion section that does not reach for the shared vocabulary to explain the result.

Length target: short. The Aizawa method produces dry, ugly writeups. That is correct.
