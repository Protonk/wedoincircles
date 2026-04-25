# SCHOENHAGE-STRASSEN-1971-BRIEF

Source-extraction memo on A. Schönhage and V. Strassen, "Schnelle
Multiplikation großer Zahlen," *Computing* 7 (1971), 281–292 (English
translation by Ryan Landay, May 2023:
[sources/Fast Multiplication of Large Integers.pdf](<sources/Fast Multiplication of Large Integers.pdf>)).

**Author identity.** V. Strassen is the same Volker Strassen of Strassen's
matrix-multiplication algorithm (1969) and substantial foundational work
in algebraic complexity theory. A. Schönhage (Konstanz) continued in
fast-arithmetic work through the 1970s–80s. The paper is the
Schönhage–Strassen integer-multiplication algorithm, a foundational
result in the bit-complexity / algebraic-complexity boundary literature.

**What was read.** The local PDF was read with one specific lens: how
does a Turing machine fit into the program's compute-cost branch? The
program's beating heart is likely a structured operational compute model
in the Landfall tradition (Mitchell's L-table representation + IEEE
floats), and Schönhage–Strassen 1971 is the FFT-complexity literature's
instance of an FFT-style upper bound stated in *bit-complexity* terms on
explicit operational compute models.

**Confidence level.** Medium-high on the paper's two algorithm
constructions and complexity counts; the constructions are explicit and
the complexity arithmetic is straightforward. Medium on the structural
reading for the program: bridging Schönhage–Strassen's compute model to
Landfall's operational model or to circle-side T1/T3 is repo-side
inference, not in the paper.

**Provenance.** Methodologically pre-L-W: Fermat numbers, FFT over
residue rings, primitive roots of unity in finite rings, classical
ring-theoretic algebra, Cooley–Tukey recursion. No transcendence
machinery, no analytic number theory. L-W-safe.

---

## Main Payload

The paper proves an *upper bound* on integer multiplication: two N-digit
binary numbers can be multiplied in `O(N log N log log N)` operations on
a multitape Turing machine, with the same bound for Boolean (logical)
networks. The construction is recursive nesting of FFT with carefully
chosen base rings — `ℂ` (with rounded fixed-point) in the first method,
the Fermat residue ring `ℤ_{F_n}` (with `F_n = 2^{2^n} + 1`) in the
second.

**The structural move that matters for our program.** The paper
explicitly works in *two* operational compute models in parallel —
multitape Turing machine (effort = max head movements over input pairs
of length N) and Boolean network (effort = number of two-input gates) —
and gets matching complexity in both. The compute model is concrete and
operational; "primitive" is a head movement or a gate.

**The key engineering trick.** In `ℤ_{F_n}`, the value `2` is a primitive
`2^{n+1}`-th root of unity. Multiplication by this root in the FFT
becomes *cyclic shift* by one position in the binary representation —
which is essentially free on a multitape Turing machine (the head moves)
and free in a Boolean network (the wiring permutes). The FFT's twiddle
multiplications, expensive over `ℂ`, become operationally cheap over
`ℤ_{F_n}`. The compute model is engineered so that the natural algebraic
operation is operationally cheap by construction.

This is the same shape of move Landfall makes on the log side: choose a
representation where the natural algebraic operation is cheap by
construction (Mitchell's L-table makes log-lookup free; Fermat-residue
representation makes root-of-unity multiplication free).

---

## 1. The Compute Models

### What the Paper Defines

**Multitape Turing machine.** "For a Turing machine that performs
multiplication of numbers of arbitrary length, the effort of multiplying
N-digit numbers is defined as the maximum number of head movements over
all input pairs of length N." Cost is operational; the primitive is a
single tape-head step.

**Boolean (logical) network.** "We define the effort of a network as
the number of its elements." Two-input logic gates as primitives.

The paper notes both models give the same complexity for its algorithms.

### What the Paper States Without Independent Verification Here

The reduction between the two models is treated as background: a
Boolean network can simulate a multitape Turing machine with at most
polylogarithmic overhead, and vice versa, with both reductions inside
the same complexity class. The paper does not prove this; it relies on
prior work (Cook 1966, Knuth Vol. 2 Ch. 4 are cited as references).

### Repo Inference

Both compute models in Schönhage–Strassen are *operational*: each
specifies a concrete primitive cost and counts it. This is the same
shape as Landfall's compute model (IEEE floats on Mitchell's L-table,
counting floating-point operations). The program's circle-side
compute-cost branch, if it lands as a Landfall-parallel theorem, will
need an operational compute model of this shape — *not* the abstract
bilinear / rational-equivalence frameworks of Winograd 1978 or AFW 1984.

The framework `[sources/Fast Multiplication of Large Integers.pdf]` lives
in is the closest to what the program's compute-cost branch wants
operationally, even though the paper proves an upper bound rather than a
lower bound.

---

## 2. The Two Algorithms

### What the Paper Proves

**Method 1 (over ℂ).** Decompose each N-digit factor into `2^n`
sections of length `l`. Use FFT over `ℂ` with `w_n = e^{2πi · 2^{-n}}`,
performed in fixed-point arithmetic with `s` digits after the decimal
point. The complex multiplications inside the FFT are themselves
recursively reduced to N-digit binary multiplications, calling the
algorithm at smaller scale. Three nesting levels give

```text
M_1(N) = O(N (log N)²)
M_2(N) = O(N log N (log log N)²)
M_3(N) = O(N log N log log N · (log log log N)²)
```

with deeper nesting giving `O(N log N (log log N)^{1+ε})`.

**Method 2 (over `ℤ_{F_n}`).** The Fermat residue ring `ℤ_{F_n}` has
`F_n = 2^{2^n} + 1`. The value `2` is a primitive `2^{n+1}`-th root of
unity in `ℤ_{F_n}` (because `2^{2^n} ≡ -1 (mod F_n)`). FFT over
`ℤ_{F_n}` therefore has its twiddle-multiplications realized as cyclic
shifts of the bit representation, requiring `O(2^n)` operations rather
than `O(s)` arithmetic operations.

The paper reduces multiplication in `ℤ_{F_m}` to multiplications in
`ℤ_{F_n}` for `m = 2n−1` or `m = 2n−2`, recursively. The recursion
depth is roughly `log log N`. The closed-form bound is

```text
M(n) = O(2^n · n · log n)
```

for multiplication of `2^{n+1}`-digit numbers in `ℤ_{F_n}`. Applied to
N-digit binary numbers (taking `n = ⌈log(2N)⌉`), this gives

```text
O(N log N log log N).
```

### What the Paper Imports

- Cooley–Tukey FFT (cited as ref. [3]).
- Cook 1966 for upper-bound techniques on Turing-machine computations
  (refs. [1, 2]).
- Karatsuba and Toom for prior fast-multiplication work (refs. [4, 7]).
- Schönhage 1966 for the previous best `O(N · 2^{√(2 log N)} · (log N)^{3/2})`
  (ref. [6]).

### Repo Inference — The Cyclic-Shift Trick

The structural move worth highlighting: in `ℤ_{F_n}`, the canonical
root-of-unity multiplication `x ↦ 2^κ · x` is *not arithmetic at all*
in the Turing-machine cost model. It is a cyclic shift by `κ` positions
of the bit representation. On a Turing machine, this is `O(2^n)` head
movements (the bit string is `2^{n+1}` long); on a Boolean network, it
is wiring (zero gates if the wiring is fixed). Either way, the cost is
*not the FFT's twiddle cost in arithmetic terms* but the head-movement
/ wiring cost of moving bits.

This is the program's natural template if the compute-cost branch lands
on a Turing-machine-native compute model: choose a representation where
the natural circle-side operation is structurally cheap. Cyclotomic
integer arithmetic in `ℤ[ζ_n]` could plausibly have multiplication-by-
`ζ_n` as a coordinate permutation (cheap on a tape); the engineering
trick generalizes.

---

## 3. The Lower-Bound Question (What the Paper Doesn't Prove)

### What the Paper States

> "We do not believe that the order of magnitude `N log N log log N` for
> the effort is optimal, but we suspect that the order of magnitude
> `N log N` is optimal (cf. the deeper result of [2])."

Reference [2] is Cook–Aanderaa, *On the Minimum Computation Time of
Functions* (Trans. AMS 142, 291–314, 1969). The paper conjectures the
matching lower bound but explicitly acknowledges it as unproved.

### Repo Inference

For the program's compute-cost lower-bound branch, this is critical.
Schönhage–Strassen gives a *target* (a matching lower bound on a related
task must reach `Ω(N log N)` or better) but not a *technique*. The paper
is in the construction face of the literature's upper-bound /
lower-bound divide.

The matching `Ω(N log N)` lower bound on multitape Turing-machine
multiplication, conjectured here in 1971, remained open for decades and
— to my knowledge — is still not proved unconditionally in the broadest
model. Cook–Aanderaa-style results give partial lower bounds in
restricted models. This is one of the long-standing open problems in
algorithmic complexity, and the program's compute-cost branch is in the
same neighborhood.

---

## 4. How a Turing Machine Fits the Program

This is the lens the brief was written under. Four bridges to the
program, each speculative but available:

### Bridge to V_cert

`V_cert` as defined in `memos/LEDGER-PIVOT-SEARCH.md` is at the
algebraic level (per-cell min-poly + height + isolating interval). To
translate `V_cert` into a Turing-machine-native ledger, each component
would have to be charged operationally:

- **Min-poly evaluation:** counted as polynomial-arithmetic head
  movements on tape.
- **Height bookkeeping:** counted as bit-manipulation of the height
  witness.
- **Root isolation at precision ε:** counted as interval-arithmetic
  head movements at log(1/ε) bit precision.

Cost would then be a function of degree, height, and precision — the
same parameters `V_cert` has, but charged operationally rather than
algebraically. Schönhage–Strassen demonstrates the translation is in
principle feasible: the paper's algorithm has both an algebraic
specification (FFT over Fermat residue rings) and an operational cost
(Turing-machine head movements), and the two are tightly coupled by the
ring choice. The same dual specification could exist for `V_cert`.

### Bridge to Closure-Depth

The closure-depth no-go is purely algebraic: `[K_n : ℚ] = φ(n)/2` is
unbounded as `n` varies. To place this in a Turing-machine framework,
one would need a translation: the K_n ladder's `φ(n)/2` degree forces a
corresponding `φ(n)/2` operational depth on any Turing machine that
produces values in K_n.

Schönhage–Strassen provides indirect support: the algorithm's recursion
depth is roughly `log log N`, and the depth at each level is tied to
the cyclotomic structure of the Fermat residue ring (the `ℤ_{F_n}` ring
contains primitive `2^{n+1}`-th roots of unity exactly because of its
algebraic structure). A program-side analog would tie K_n's degree to
operational depth in a similar way — but the analog is not in the
paper.

### Bridge to Kraft–Parseval

Schönhage–Strassen's algorithm is *uniform in N* (a single algorithm
description handles all input sizes; the recursion is parameterized).
Kraft accounting wants a uniform self-delimiting compiler. The paper
doesn't supply Kraft-style accounting, but its uniformity is the right
kind: a single description encodes the algorithm's behavior across all
input sizes.

This is a structural advantage Schönhage–Strassen has over the other
three FFT-complexity papers we've brief'd. AFW, Morgenstern, and
Winograd 1978 are all per-fixed-N (axiom 7 of `memos/LEDGER-PIVOT-SEARCH.md`
§"Certification-preserving model: open axioms" remains "nonuniform" in
each). Schönhage–Strassen is uniform. Translating its uniform recursion
into prefix-free / Kraft-compatible accounting is not in the paper but
is structurally available.

### Bridge to the Triadic Structure

The triadic structure in `README.md` has three struts: closure-depth
(structural), compute-cost (per-instance algebraic), Kraft–Parseval
(cross-input encoding). Schönhage–Strassen is the FFT-complexity
literature's example of a paper that touches all three structurally:

- It uses cyclotomic structure operationally (the Fermat-ring
  primitive-root trick) — adjacent to closure-depth.
- It charges per-instance bit-complexity — adjacent to compute-cost.
- It is uniform across input sizes — adjacent to Kraft–Parseval.

It does not weld these into a single bound, but it is the literature's
nearest example of all three flavors appearing in one paper.

---

## 5. Hazard Audit

### Hazard 1: Proof-Technique Inversion

Applies. The paper is constructive — it builds an algorithm and counts
its cost. The DFT/multiplication payload is an upper bound. The paper
does not supply a lower-bound technique; it explicitly conjectures the
matching `Ω(N log N)` but cites Cook–Aanderaa as the partial state of
that art.

The program cannot cite Schönhage–Strassen as a primitive-op lower
bound on T1/T3. It can cite the paper as a structural template for how
to engineer a compute model where cyclotomic structure is operationally
cheap, and as evidence that uniform algorithms over the size family do
exist (a thing AFW, Morgenstern, and Winograd 1978 don't have).

### Hazard 2: Coefficient-Boundedness

Applies in modified form. Schönhage–Strassen does not have a
Morgenstern-style separately-bounded-coefficient hypothesis: elements
of `ℤ_{F_n}` are bounded by ring size, and operations on them are
charged in bits. The "boundedness" is built into the bit count rather
than imposed as a separate hypothesis on linear-combination scalars.

For the program: this is closer to the certification-preserving regime
than Morgenstern's framework, because the cost of an operation scales
with the bit-size of the operand. But it's not literally the same —
Morgenstern bounds *coefficients*, while Schönhage–Strassen bounds
*element bit-lengths via the ring*. The program needs to choose which
form of boundedness the compute model imposes.

### Hazard 3: Nonuniformity / Kraft

**Applies in a useful direction.** Schönhage–Strassen's algorithm IS
uniform in N (the same description handles all input sizes). The paper
does not cast this uniformity as a Kraft / prefix-free statement, but
the uniform-in-N property is structurally compatible with Kraft
accounting in a way the per-fixed-N theorems of AFW, Morgenstern, and
Winograd 1978 are not.

This is the single most program-aligned property of the paper.
Schönhage–Strassen is the FFT-complexity literature's example of a
*uniform compiler over the family of input sizes*. If Kraft accounting
wants a uniform self-delimiting description, this paper's algorithm is
closer to that than any of the other three brief'd papers.

### Hazard 4: Real-Subfield Passage

Applies. The paper works over `ℂ` (Method 1) or `ℤ_{F_n}` (Method 2).
Neither descends to `K_n = ℚ(cos(2π/n))`. A real-subfield analog would
have to be constructed; the paper's machinery is built on full
cyclotomic structure (or finite-ring analog).

### Hazard 5: Rational-Equivalence / Positional Data

Applies. Schönhage–Strassen's algorithm is *coordinate-sensitive* — the
specific bit positions in the Fermat-ring representation matter for the
cyclic-shift trick. Rational changes of basis would scramble exactly
what makes the trick work. So Schönhage–Strassen sits closer to
Morgenstern's coordinate-sensitivity than to AFW's
rational-equivalence-stability, and inherits a related non-composability
hazard with AFW.

This makes Schönhage–Strassen non-composable with AFW directly, but
*potentially composable in spirit* with Morgenstern (both protect
coordinate-frame structure). The cost currencies differ — bit-complexity
vs bounded-coefficient linear additions — but the protected invariants
are compatible.

---

## Frameworks Comparison: Where Schönhage–Strassen Sits

The literature now has four frameworks identified across our briefs:

```text
Morgenstern 1973:        coordinate-sensitive bounded-coefficient linear additions
Winograd 1978:           bilinear multiplicative complexity, field constants cheap/free
AFW 1984:                rational-equivalence-stable semisimple algebra (via AW 1980)
Schönhage–Strassen 1971: bit-complexity Turing-machine / Boolean-circuit, coordinate-sensitive,
                         uniform in N
```

Composability with the others:

- **SS71 with Morgenstern:** structurally compatible (both
  coordinate-sensitive, both operational), different cost currencies
  (bit-complexity vs bounded-linear additions). A bridge would need a
  translation between bit-ops and bounded-linear-ops.
- **SS71 with Winograd 1978:** SS71 explicitly uses Winograd-style FFT
  decomposition internally, and the `ℤ_{F_n}` choice is a finite-ring
  instance of Winograd's "enlarge the field of constants" technique. So
  SS71 is partially in Winograd 1978's framework, with bit-complexity
  costs added.
- **SS71 with AFW:** non-composable. AFW's rational equivalence
  scrambles bit positions and breaks the cyclic-shift trick.

So the four-framework picture is: AFW stands alone; SS71, Winograd
1978, and Morgenstern are closer to each other (all operational, all
coordinate-sensitive in some sense, all working with explicit cost
counts), but each charges a different primitive — bit-ops, multiplications,
bounded-linear adds. The literature's fragmentation is real, and SS71
is the most program-relevant single paper for the operational-compute-
model framing, particularly because it is *uniform in N*.

---

## Closing Sentence for FFT-CYCLOTOMIC-COMPLEXITY

This contributes Schönhage–Strassen's `O(N log N log log N)`
bit-complexity upper bound on N-digit integer multiplication via FFT
over Fermat residue rings — where multiplication by primitive roots of
unity is realized as cyclic shift on the bit representation — to the
K_n-Kraft transport, with hypothesis class multitape Turing machines
and Boolean networks charging head movements / gate counts uniformly in
input size, proof technique recursive nesting of FFT with carefully
engineered base ring (`ℂ` with rounded fixed-point in Method 1;
`ℤ_{F_n}` with Fermat-residue arithmetic and cyclic-shift roots-of-unity
in Method 2), provenance tag methodologically pre-L-W, and slots into
[memos/COUNTING-APPARATUS.md](memos/COUNTING-APPARATUS.md) item (A) as
the FFT-complexity literature's instance of a Turing-machine-native
compute model uniform in N — supplying the structural template for an
operational compute model on the circle side, but not by itself a
primitive-op lower bound for T1/T3.

---

## Trust Boundary

This brief should be cited for:

- Schönhage–Strassen's `O(N log N log log N)` upper bound on integer
  multiplication, in both the multitape Turing machine and Boolean
  network compute models;
- the cyclic-shift trick in Fermat residue rings (multiplication by
  `2^κ` realized as cyclic shift by `κ`);
- the operational shape of the compute model (multitape Turing machine,
  Boolean network, with primitives = head movements / gates);
- the uniform-in-N property of the algorithm and its structural
  compatibility with Kraft / prefix-free accounting;
- the structural template for engineering a compute model where natural
  algebraic operations are operationally cheap.

It should not be cited as proving:

- a matching lower bound (the paper is upper-bound only; the paper
  itself acknowledges this);
- a bound on T1/T3 + V_cert (a translation from algebraic certificates
  to bit operations is needed; not in the paper);
- a Kraft / prefix-free accounting theorem (the paper is uniform but
  not formally prefix-free);
- a real-subfield K_n result (the paper works over `ℂ` or `ℤ_{F_n}`,
  not K_n);
- a framework that composes with AFW (rational equivalence breaks the
  cyclic-shift trick).
