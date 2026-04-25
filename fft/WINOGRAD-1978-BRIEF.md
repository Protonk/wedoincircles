# WINOGRAD-1978-BRIEF

Source-extraction memo on S. Winograd, "On computing the discrete Fourier
transform," Mathematics of Computation 32.141 (1978), 175-199
([sources/Winograd-ComputingDiscreteFourier-1978.pdf](sources/Winograd-ComputingDiscreteFourier-1978.pdf)).

**What was read.** The local Math. Comp. PDF was read as item 3 in
[fft/FFT-CYCLOTOMIC-COMPLEXITY.md](fft/FFT-CYCLOTOMIC-COMPLEXITY.md)
§"Order of work": the cyclic-convolution / CRT engine underneath the later
FFT multiplicative-complexity literature.

**Confidence level.** High on what this paper itself says: it is an
algorithm-construction paper using previously proved bilinear-complexity
theorems for polynomial multiplication modulo a polynomial. Medium on the
exact provenance of the imported lower bounds: the paper cites earlier
Winograd, Fiduccia-Zalcstein, and Toom results; this brief has not checked
those sources independently.

**Source identity caution.** AFW 1984 cites earlier Winograd work on the
multiplicative complexity of the DFT and Auslander-Winograd work on
semilinear systems. The local PDF briefed here is the Math. Comp. 1978 paper
"On computing the discrete Fourier transform." It is foundational for the
cyclic-convolution / CRT algorithmic engine, but it is not the source of
AFW's rational-equivalence theorem.

---

## Main Payload

Winograd 1978 supplies an algorithmic bridge:

```text
polynomial multiplication mod P
  -> cyclic convolution
  -> Rader / Good / CRT decompositions of DFT
  -> low-multiplication DFT algorithms
```

The clean algebraic result used by the paper is the modular-product
multiplicative-complexity theorem:

```text
mu(T_P) = 2n - k
```

for multiplication of two degree `< n` polynomials modulo a degree-`n`
polynomial `P`, where `k` is the number of distinct irreducible factors of
`P` over the coefficient field. In this Math. Comp. paper, that theorem is
stated as prior theory, not proved from scratch.

The paper's DFT payload is constructive: it shows how to use that modular
product machinery, plus cyclic-convolution reductions and CRT index
decompositions, to obtain DFT algorithms with far fewer multiplications than
Cooley-Tukey FFT at the sizes studied.

---

## 1. Main Theorem Statements

### What the Paper States or Imports

Let

```text
R_l(u) = sum_{i=0}^l x_i u^i,
S_m(u) = sum_{i=0}^m y_i u^i,
```

and let `P(u)` be a monic degree-`n` polynomial over a field `G`. Let `T` be
the coefficient system of the ordinary product `R_l S_m`, and let `T_P` be
the coefficient system of `R_l S_m mod P`. Multiplication by a fixed element
of `G` is not counted.

The paper states these background results:

1. Computing the ordinary product coefficient system `T` requires at least
   `l + m + 1` counted multiplications, and algorithms attain this.
2. When `l = m = n - 1`, computing `T_P` requires

```text
2n - k
```

   counted multiplications, where `k` is the number of distinct irreducible
   factors of `P`.
3. Every algorithm attaining `2n - k` for `T_P` uses the CRT decomposition
   when `P` has relatively prime factors.

The key CRT identity is: if `P = P_1 P_2` with `(P_1, P_2) = 1`, then
multiplication modulo `P` is assembled from multiplication modulo `P_1` and
modulo `P_2`, followed by fixed linear recombination using polynomials
`Q_1, Q_2` satisfying

```text
Q_1 P_1 + Q_2 P_2 = 1 mod P.
```

For cyclic convolution of length `N`, the relevant polynomial is

```text
P(u) = u^N - 1.
```

Over `Q`, the distinct irreducible factors are the cyclotomic polynomials
`Phi_d(u)` for `d | N`, so `k = d(N)`, the number of positive divisors of
`N`. The modular-product theorem therefore gives the cyclic-convolution
count

```text
mu(T_{u^N - 1}) = 2N - d(N)
```

over `Q`, in the paper's multiplication-counting convention.

### What the Paper Itself Constructs

The paper constructs DFT algorithms from the modular-product / convolution
machinery:

- cyclic convolution is represented as polynomial multiplication modulo
  `u^N - 1`;
- prime-length DFT is reduced, by Rader's rearrangement, to cyclic
  convolution on the multiplicative group of nonzero residues;
- prime-power lengths are treated by analogous permutations of the DFT
  matrix into repeated residue-class blocks;
- coprime composite lengths `N = N_1 N_2` are handled by CRT on the index
  set, giving a direct/Kronecker product of the two smaller DFT matrices
  after suitable permutations and root substitutions;
- multidimensional DFTs are direct products of one-dimensional DFT matrices;
- extension fields can reduce multiplication counts by splitting more
  factors of the relevant polynomial.

This is the paper's headline DFT payload: constructive DFT algorithms with
low multiplication count, not a single universal exact formula for the
multiplicative complexity of `DFT_N` in the later AFW sense.

### Clean Theorem Versus DFT Corollary

For this local source, the safe distinction is:

- **Underlying clean theorem:** the modular-product bound `mu(T_P) = 2n-k`
  for `l = m = n - 1`, imported from prior complexity theory and used
  throughout.
- **Cyclic-convolution corollary:** applying that theorem to `P = u^N - 1`
  gives `2N - d(N)` over `Q`.
- **DFT-applied result:** Rader / Good / CRT constructions turn cyclic
  convolution algorithms into DFT algorithms for primes, prime powers,
  coprime composites, and multidimensional transforms. The paper tabulates
  explicit counts and algorithms, but does not present the later AFW-style
  exact multiplicative-complexity theorem for every finite abelian DFT.

So the memo-level phrase "`2N - d(N)` DFT bound" should be used carefully:
in this paper it is cleanest as a cyclic-convolution / modular-product count
that feeds DFT algorithms, not as the final AFW theorem.

---

## 2. Structural Framework

### What the Paper Uses

Winograd's framework is **bilinear multiplicative complexity plus explicit
algorithmic change-of-form**.

It uses:

- polynomial products modulo `P`;
- CRT decompositions of quotient rings;
- cyclic convolution matrices;
- transposition / duality of bilinear algorithms;
- permutations of input/output coordinates;
- direct-product decompositions for coprime dimensions;
- extension of the coefficient field to split more factors and reduce
  multiplication count;
- precomputation of constants when one side of a bilinear product is known.

Multiplication by fixed field elements is often free in the theoretical
background. In DFT tables and examples, the paper separately tracks certain
constant multiplications and real additions, but the lower-bound engine is
not a bounded-coefficient additive model.

### Relation to AFW's Rational-Equivalence Framework

This paper anticipates some of AFW's structural moves: CRT decomposition,
permuting rows/columns, replacing DFT matrices by block/direct-product
forms, and exploiting cyclotomic splitting. But it does not formulate the
AFW rational-equivalence theorem for semilinear systems.

AFW imports rational-equivalence invariance from Auslander-Winograd 1980 and
related AFW work, not from this Math. Comp. paper. Winograd 1978 is therefore
best classified as the **algorithmic CRT / cyclic-convolution ancestor**, not
as the formal rational-equivalence source.

### Relation to Morgenstern's Coordinate-Sensitive Framework

Winograd is not in Morgenstern's coordinate-sensitive determinant-growth
framework. It does count operations in concrete algorithms and gives explicit
coordinate formulas, but its lower-bound statements are bilinear /
multiplicative-complexity statements for polynomial-product systems, not
determinant lower bounds for bounded-coefficient linear circuits.

Winograd also permits exactly the kind of coefficient-field maneuvering that
Morgenstern controls: changing the field of constants can reduce the
multiplication count. This is not a contradiction; it is a different cost
currency.

### Classification

Winograd 1978 sits between the later camps only historically, not
technically:

```text
Morgenstern: coordinate-sensitive bounded-linear additions.
Winograd 1978: bilinear multiplicative complexity and explicit CRT algorithms.
AFW 1984: rational-equivalence-stable semilinear / semisimple algebra.
```

It helps explain why AFW exists, but it does not bridge Morgenstern and AFW.

---

## 3. Relation to Morgenstern's Determinant-Growth Argument

### What the Paper Proves

Winograd's lower-bound input is the multiplicative complexity of bilinear
maps such as polynomial multiplication and multiplication modulo `P`. The
paper states the lower bounds as prior results and then builds algorithms
that attain or exploit them.

Morgenstern's lower bound is about linear algorithms, additions, and
bounded complex coefficients. It uses determinant / volume growth.

### Repo Inference

The two techniques are independent for the program's purposes.

They are not contradictory because they charge different primitives:

- Winograd optimizes multiplications in bilinear convolution/DFT
  constructions, often allowing additions and fixed-field scalars cheaply.
- Morgenstern lower-bounds additions in bounded-coefficient linear
  algorithms.

They also protect different invariants:

- Winograd's modular-product theorem is sensitive to factorization of `P`
  over the chosen field; enlarging the field can reduce counted
  multiplications.
- Morgenstern's determinant theorem is sensitive to coefficient magnitude;
  unbounded coefficients destroy the lower bound.

There may be broad common background in algebraic complexity of bilinear
forms, but this local paper does not derive one from the other.

---

## 4. Hazard Audit

### Hazard 1: Proof-Technique Inversion

Applies. This paper is mainly constructive. It imports a lower bound for
modular polynomial products, but its DFT contribution is algorithmic:
constructing low-multiplication transforms from convolution algorithms.

The program cannot cite the DFT algorithms themselves as lower bounds for
T1/T3. At most, it can cite the modular-product lower-bound theorem as part
of an algebraic-complexity toolkit, with the caveat that the theorem is
imported from earlier work.

### Hazard 2: Coefficient-Boundedness

Applies strongly. Winograd's hypothesis class does not match Morgenstern's
bounded-coefficient regime.

The Section II theory works over a field `G`; multiplication by fixed
elements of `G` is not counted. Later sections deliberately enlarge the field
of constants, e.g. to `Q(i)` or other algebraic extensions, to split
polynomials further and reduce multiplication counts. There is no height,
modulus, or bounded-coefficient condition analogous to Morgenstern's.

For the program, this means Winograd is not certification-preserving by
itself. It is closer to an algebraic multiplicative-complexity model with
field constants treated as cheap or free.

### Hazard 3: Nonuniformity / Kraft

Applies. The paper gives explicit algorithms for fixed transform sizes and
discusses program-length tradeoffs. It even notes that one construction saves
multiplications at the expense of writing a longer specialized algorithm.

There is no uniform self-delimiting compiler, no prefix-free accounting, no
semicomputable measure, and no universal-dominance step. The paper supplies
finite algorithms and counts, not Kraft bookkeeping over a family.

### Hazard 4: Real-Subfield Passage

Applies. The DFT is written with roots of unity `w = exp(2 pi i/n)`, so the
natural field is the full cyclotomic field. The paper observes that in some
prime-power algorithms the root-dependent multipliers are purely real or
purely imaginary, involving expressions like `w^i + w^{-i}` and
`w^i - w^{-i}`. That is useful evidence that real trace-field structure is
nearby.

But the paper does not prove a real-subfield `K_n = Q(cos(2 pi/n))`
multiplicative-complexity theorem. A real-subfield descent remains a separate
program step.

### Hazard 5: Rational-Equivalence / Positional Data

Applies. Winograd uses permutations, CRT recombinations, transposition, and
block/direct-product transformations. These are exactly the kinds of
structure-changing operations that can preserve an algebraic operation count
while scrambling the per-cell positional data required by `V_cert`.

This paper does not track the positional semantics needed by T1/T3. Any
import into a cell-tier ledger must prove that the reduction preserves the
relevant ordered real cells and incidence data, or else accept the result as
a coarser companion bound.

---

## Program Import

Winograd 1978 can be used safely for three things:

1. **Cyclic-convolution engine.** It cleanly links polynomial multiplication
   modulo `u^N - 1` to cyclic convolution and hence to DFT algorithms.
2. **Cyclotomic-factor receipt.** Applying the modular-product theorem to
   `u^N - 1 = product_{d|N} Phi_d(u)` makes the `phi(d)` cyclotomic
   degree-sum visibly operational.
3. **Field-of-constants warning.** It explicitly shows that changing the
   scalar field changes multiplicative complexity, which supports the
   program's insistence that compute-model choice and coefficient-boundedness
   are load-bearing.

It should not be cited as:

- the source of AFW's rational-equivalence theorem;
- a Morgenstern-style bounded-coefficient lower bound;
- a Kraft / prefix-free accounting theorem;
- a real-subfield `K_n` theorem;
- a lower bound for T1/T3 + `V_cert`.

---

## Closing Sentence for FFT-CYCLOTOMIC-COMPLEXITY

This contributes the modular-product theorem `mu(T_P) = 2n-k` for
degree-`n` polynomial multiplication modulo `P` with `k` distinct
irreducible factors, and its cyclic-convolution / DFT algorithmic
deployment, to the K_n-Kraft transport, with hypothesis class bilinear
multiplicative complexity over a chosen field with fixed field scalars
cheap or free, proof technique CRT decomposition plus cyclic-convolution
and Rader/Good index transformations, provenance tag methodologically
pre-L-W, and slots into [memos/COUNTING-APPARATUS.md](memos/COUNTING-APPARATUS.md)
item (A) as an algebraic-complexity structure source rather than as a direct
bounded-coefficient or primitive-op lower bound.

---

## Trust Boundary

This brief should be cited for:

- the modular-product `2n-k` theorem as stated/imported in the paper;
- the application to `u^N - 1` and cyclic convolution;
- the constructive DFT reductions through Rader / Good / CRT;
- the fact that field extension can reduce multiplication count.

It should not be cited as independently proving:

- the imported bilinear-complexity lower bounds from Winograd's earlier
  paper or Fiduccia-Zalcstein;
- a universal exact DFT multiplicative-complexity formula in AFW's later
  sense;
- bounded-coefficient additive lower bounds;
- real-subfield or `V_cert` lower bounds.
