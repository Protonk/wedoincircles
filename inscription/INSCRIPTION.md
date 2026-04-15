# INSCRIPTION

A sibling to *Landfall* on the circle side, pursued as a research problem in its own right. The audience is assumed to have read *Landfall* and to know its six walls; this note states what differs and where the original work has to happen.

---

**Status.** This is program material, not a source digest. It was promoted out of `memos/` once the structural parallel to *Landfall* became sharp enough to attack directly. The triad layer (`triad/TRIAD-ABSTRACT-PATTERN.md`, `triad/plus_ultra/`) still governs whether a functor F transports *Landfall* into this sibling; the working expectation is that F does not exist and the interesting result is the shape of the obstruction — which reads back into Inscription as "siblings with shared parent structure, not translations." Inscription's existence as a target structure does not depend on F existing.

---

## The residue

$$\tau(n) = 2\cos(2\pi/n) - \mathrm{round}(2\cos(2\pi/n)),\quad n \in \mathbb{Z}_{\ge 1}.$$

Zero at n ∈ {1, 2, 3, 4, 6} (the crystallographic set, by Niven's theorem). Algebraic of degree exactly φ(n)/2 elsewhere (for n ≥ 5 outside {6}), where φ is Euler's totient. Bounded in [−1/2, 1/2]. Determined by the prime factorization of n via Galois theory of ℚ(ζ_n).

The "free" coarse stage: a 2D rotation matrix R_n in a lattice basis has integer trace iff n ∈ {1, 2, 3, 4, 6} (the 2D crystallographic restriction; higher-dimensional lattices enlarge this set). The rounding to crystallographic is free (lattice arithmetic). The residue τ is what rounding leaves behind. This brief operates in 2D throughout.

## Three walls port, three walls soften

Ports directly: §2 closure (R_n ∉ integer-preserving extension of lattice group), §3 local aliasing (Penrose local isomorphism replaces corona classes), §5 Kraft (domain-independent).

Softens:

- **§1 / §4**: Landfall has *transcendence* of ε. Inscription has *unbounded algebraic degree* of τ. Every τ(n) is in ℚ̄; the sequence of τ(n) does not fit in any finite-dimensional extension of ℚ. Weaker absolutely, sharper structurally. The wall still closes — no fixed-degree algebraic corrector can match τ(n) for all n — but by degree growth rather than by irrationality in an absolute sense.

- **§6**: compared under the full symmetry group of each geometry, both settings fail — but by different mechanisms. Landfall closes by Bowen's result that the binary tiling's hull has *no* PSL(2, ℝ)-invariant probability measure. The Penrose analog closes against E(2) on the LI-class closure Ω (defined below), not against translation alone — under ℝ²-translation, a single Penrose hull is uniquely ergodic. So the papers agree under the respective translation subgroups and diverge under the full symmetry group.

## The §6 mechanism

The binary tiling carries a phase: Bowen's equivariant protrusion direction toward the ideal boundary. Aggregation under PSL(2, ℝ) would require averaging over this direction, and the directional distribution is the thing that has no invariance.

The Penrose setting carries a phase too: the cut-and-project offset in the internal ℝ³ (de Bruijn's ℝ⁵ → ℝ² projection, with internal space the orthogonal ℝ³; the Baake–Grimm ℝ⁴ → ℝ² convention with internal ℝ² is equivalent for the phase-as-gauge reading, but the ℝ⁵/ℝ³ presentation makes the 5-fold symmetry manifest and is used here).

Two tiling-space objects matter and are not the same:

- **X** = the translation hull of a single Penrose tiling T: closure of {T + v : v ∈ ℝ²} in the local topology. ℝ²-invariant, uniquely ergodic. A non-crystallographic rotation does not act on X — it carries X to a distinct X' in the same local-isomorphism class.
- **Ω** = the LI-class closure, the union of all such X over Penrose tilings in one LI class. Ω is E(2)-invariant, and E(2) acts on Ω.

The obstruction lives on Ω. An E(2)-invariant probability measure on Ω cannot concentrate on any single X: it must superpose over the rotation fiber of LI-class representatives, and that superposition averages out the cut-and-project offset that the per-X ergodic measure distinguishes. No E(2)-invariant measure on Ω restricts to a per-X ergodic measure on any X.

A structural parallel — stated here as prose observation, not theorem:

- Binary tiling: translation and scale generate the non-abelian Aff⁺(ℝ); the commutator picks out the protrusion direction, and the per-subgroup measure sees a direction the full group would have to quotient away.
- Penrose Ω: translation and rotation generate the non-abelian E(2); the commutator picks out the cut-and-project offset, and the per-X measure sees an offset the full group would have to quotient away.

In both cases the per-subgroup invariant measure distinguishes something a full-group-invariant measure would be forced to wash out. Whether this rhyme lifts to a theorem is open (see §6 residue in "Where the original work sits").

## Where the original work sits

§1 and §4 require redoing the closure arguments against algebraic targets of unbounded degree rather than against transcendental targets. The Galois-theoretic version of the finite-dimensional M-invariant subspace argument — if Padé closes, the level-k approximations fit in a fixed cyclotomic extension, but the limit lives outside every cyclotomic extension — is the replacement. Cleaner than Landfall's transcendence argument in some ways, murkier in others.

§6 is two specific obstructions with a structural parallel pointed out in prose, not one theorem. Bowen's non-existence of a PSL(2, ℝ)-invariant measure on the binary tiling's hull, and the non-existence of an E(2)-invariant measure on Ω compatible with the per-X ergodic measure, each require their own proof. Both are citation-plus-adaptation; neither is being claimed as new.

**§6 residue — open question.** Is there a general statement along the lines of: for (Y, G) with closed subgroup H ⊂ G, if the H-ergodic measure on Y has support not setwise fixed by the G/H-action, no G-invariant measure on Y restricts to it? An earlier draft of this brief asserted a clean corollary-producing theorem ("G/H non-trivial ⇒ no G-invariant measure unless G/H acts trivially on the H-measure"); that statement is false as written — compact G/H acting trivially lets the measure extend by fiber integration, which is the opposite of what the clause claimed. A correct version has to pin down how G/H moves the H-measure's support. Not proved here; not even carefully stated. This is the honest shape of the unresolved question behind the §6 parallel.

§2, §3, §5 are citation-level work.

## What Inscription is for

Not to port Landfall. To document that when the target is algebraic-of-unbounded-degree rather than transcendental, and when the ambient tiling has a phase rather than a direction, the obstruction has the same overall shape but closes by a structurally distinct mechanism.

The payoff: placing the two obstructions side by side exposes a shared shape — non-abelian symmetry group, per-subgroup invariant measure, full-group measure blocked by a phase the subgroup measure distinguishes. Whether this rises to a unification or remains a rhyme is the open question at the end of §6, not a claim the brief delivers.

Inscription earns its parallelism by being different in mechanism at §1, §4, §6 — specifically at the places where "port" would have been the easy move. The papers are siblings because they have the same parent structure, not because one is a translation of the other.
