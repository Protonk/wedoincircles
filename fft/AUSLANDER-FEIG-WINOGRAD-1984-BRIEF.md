# AUSLANDER-FEIG-WINOGRAD-1984-BRIEF

Source-extraction memo on L. Auslander, E. Feig, and S. Winograd,
"The multiplicative complexity of the discrete Fourier transform,"
Advances in Applied Mathematics 5 (1984), 87-109
([sources/multiplicative-complexity.pdf](sources/multiplicative-complexity.pdf)).

**What was read.** The local PDF was read as the first directed-read item
from [fft/FFT-CYCLOTOMIC-COMPLEXITY.md](fft/FFT-CYCLOTOMIC-COMPLEXITY.md)
because that search memo now treats AFW 1984 as the central structure
paper for the cyclotomic-complexity bridge.

**Confidence level.** Medium-high on the theorem architecture of this
paper: the definitions, rational-equivalence reductions, p-primary cases,
and final finite-abelian-group induction are explicit in the text. Medium
on the exact inherited complexity theorem, because the paper imports the
semilinear-system complexity theorem from Auslander-Winograd 1980 and
imports earlier DFT equivalence results from the authors' prior papers; this
brief has not independently checked those sources.

---

## Main Payload

**Theorem-shape payload.** For every finite abelian group `G`, the DFT
matrix `F(G)` is rationally equivalent to a semisimple linear system built
from cyclotomic fields and finite-dimensional semisimple abelian `Q`-algebras.
That semisimple system satisfies the dimension hypothesis of the
Auslander-Winograd semilinear-system theorem, so the multiplicative
complexity of `F(G)` is computable and minimal algorithms are constructible.

More concretely:

- The computational task is evaluating `F(G)X`, where `X` is a full vector
  of indeterminates.
- The cost `p(M)` of a semilinear system `MX` is the minimum number of
  essential nonrational multiplication/division steps needed to evaluate it.
- Rational row/column changes of variables preserve `p(M)`.
- The finite abelian DFT is reduced, by p-primary decomposition and tensor
  products, to cyclotomic Vandermonde blocks.
- Those blocks are then reduced to semisimple linear systems by CRT and
  cyclotomic-field bookkeeping.

This is a structural computability theorem for multiplicative complexity,
not a Kraft theorem and not a bit-complexity theorem.

---

## 1. DFT Complexity and Semisimple Cyclotomic Decomposition

### What the Paper Proves

AFW proves that the DFT on a finite abelian group reduces to semisimple
cyclotomic algebra.

For `G = Z/p^k Z`, the paper uses a prior result identifying `F(G)` up to
rational equivalence with a direct sum of Vandermonde matrices `V(p^j)`.
For a p-primary group, tensor-product identities reduce `F(G)` to a direct
sum of tensor products of those `V(p^j)` blocks. This gives a computable
direct-sum form

```text
F(G) ~ product_j d_j V(p^j)
```

in the paper's block notation.

The paper then performs the "dirty work" for the p-primary case:

- for odd `p`, it shows that `V(p^k)` can be rationally transformed into
  a block containing `V(p^(k-1))` and a semisimple block `K(p^k)`;
- for `p = 2`, it handles the noncyclic unit group separately and obtains
  two semisimple blocks `K(2^k; 1)` and `K(2^k; 2)`;
- in both cases, a dimension count using cyclotomic degrees verifies the
  hypothesis needed to invoke the semisimple-system complexity theorem;
- the final section inducts over the distinct p-primary components of a
  finite abelian group, using that tensor products of semisimple algebras
  remain semisimple and that `phi` is multiplicative on coprime inputs.

The proof therefore supplies the exact structural role of the cyclotomic
decomposition: cyclotomic fields are not decorative notation; they are the
field summands whose dimensions and tensor products make the multiplicative
complexity computable.

### What the Paper States or Imports Without Reproving Here

AFW imports several load-bearing ingredients from earlier papers:

- The rational-equivalence invariance theorem for semilinear systems is an
  immediate corollary of results in Auslander-Winograd 1980.
- The reduction of `F(Z/p^k Z)` to a direct sum of Vandermonde matrices is
  stated as proved in the authors' prior work on abelian semisimple algebras
  and DFT algorithms.
- The formula for semisimple systems,

```text
p(S) = sum_j t_j (2 n_j - 1),
```

  under the stated dimension hypothesis, is a special case of the main
  theorem from Auslander-Winograd 1980.
- The paper states that minimal algorithms are constructible once the
  semisimple reduction is in hand; this brief has not checked the earlier
  construction theorem independently.

### Repo Inference

AFW is the right structure paper for the FFT-cyclotomic bridge because it
does not merely exhibit an FFT algorithm. It identifies the DFT's
multiplicative-complexity ledger with a direct-sum/tensor-product ledger of
cyclotomic semisimple algebra factors.

But the result is still a multiplicative-complexity result. It does not by
itself provide a lower bound for the program's corner tasks T1/T3, nor does
it identify the program's `K_n = Q(cos(2 pi/n))` ladder as the exact ledger.
Those are extra bridge steps.

---

## 2. Hypothesis Class and Relation to COUNTING-APPARATUS Models (3) and (4)

### What the Paper Proves

AFW's hypothesis class is a semilinear algebraic-computation model.

An algorithm has a finite base set inside `C` together with the input
indeterminates, and then forms elements of `C(x_1, ..., x_n)` by field
operations. The complexity `p(M)` counts essential multiplication/division
steps: addition/subtraction is free, rational scalar multiplication/division
is free, and only nonrational multiplication/division steps are charged.

The target systems are linear systems `MX` with complex matrix `M` and full
indeterminate input vector `X`.

### What the Paper Does Not Claim

AFW does not count:

- additions;
- rational linear preprocessing or postprocessing;
- bit complexity;
- numerical precision;
- height of algebraic constants;
- the cost of constructing cyclotomic constants;
- a primitive "adjoin an algebraic number of degree <= d" operation.

It also does not address nonlinear algorithms for non-DFT tasks. Its model is
tailored to semilinear systems and essential multiplication/division steps.

### Repo Inference

AFW is closest to an ASLP-style version of
[memos/COUNTING-APPARATUS.md](memos/COUNTING-APPARATUS.md) model (4), but
only after specializing ASLP to linear systems and counting essential
nonrational multiplication/division steps. It is compatible with model (3)
"algebraic-arithmetic over Q" only after a conversion theorem is supplied.

That conversion theorem would have to say how AFW's essential m/d count
translates into model-(3) primitive-operation cost, where operations at
degree `d` cost `poly(d)` and algebraic adjunctions are explicitly paid.
Without that conversion, AFW supplies a structural algebraic ledger, not the
program's primitive-op lower bound.

The main caution is coefficient-class drift. AFW allows complex algebraic
DFT constants as matrix entries and treats rational transformations as free.
The program must decide whether roots of unity and their real subfield
generators are free constants, paid adjunctions, or forbidden until
constructed.

---

## 3. Tensor / Direct-Sum Decomposition Versus Kraft Accounting

### What the Paper Proves

AFW proves algebraic decompositions:

- DFT matrices decompose under finite-abelian-group tensor products.
- p-primary blocks reduce to cyclotomic Vandermonde blocks.
- CRT and rational equivalence convert those blocks into semisimple direct
  sums.
- Tensor products of semisimple algebras remain semisimple, so the general
  case is closed by induction.

The accounting is additive over algebraic direct summands once the
semisimple-system theorem applies.

### What the Paper Does Not Prove

AFW does not define a prefix-free code, a semicomputable sub-probability
measure, Kraft cylinders, a universal prefix-free machine, or universal
dominance. Nothing in the paper asserts an inequality of the form

```text
sum_summands 2^(-length(summand)) <= 1.
```

The tensor/direct-sum decomposition is therefore not a Kraft decomposition
on its own.

### Repo Inference

AFW can supply the finite algebraic parse tree that a later Kraft
construction might encode: prime decomposition of `G`, cyclotomic block
labels, tensor products, CRT factors, and field-summand counts. But the
prefix-free layer is additional structure.

To turn AFW accounting into Kraft accounting, the program would need at
least:

- a self-delimiting description language for the AFW decomposition tokens;
- a proof that the induced weights form a semicomputable sub-probability
  measure;
- a Kraft inequality for those descriptions;
- if using the Fortnow route, a universal-dominance step of the kind
  summarized in
  [memos/FORTNOW-KOLMOGOROV-BRIEF.md](memos/FORTNOW-KOLMOGOROV-BRIEF.md)
  Section 6.

Thus the strongest honest conclusion is negative-for-now: AFW is a Kraft
cousin, not a Kraft identity.

---

## 4. Real-Subfield Passage

### What the Paper Proves

AFW works with the full cyclotomic field

```text
Q(zeta_m) = Q(exp(2 pi i / m)).
```

The paper defines cyclotomic fields using primitive roots of unity, uses the
minimal polynomial of `zeta_m`, and repeatedly verifies dimension hypotheses
with

```text
[Q(zeta_m) : Q] = phi(m).
```

The DFT matrices themselves have entries in the full cyclotomic field.

### What the Paper Does Not Prove

AFW does not prove a descent from full DFT complexity over `Q(zeta_n)` to the
maximal real subfield

```text
K_n = Q(cos(2 pi / n)).
```

It also does not state a separate multiplicative-complexity theorem for
cosine transforms, trace-field-only systems, or conjugation-invariant
subsystems.

### Repo Inference

The real-subfield passage is available algebraically but not free as an AFW
theorem. For `n >= 3`, `K_n` is the fixed field of complex conjugation and

```text
[K_n : Q] = phi(n)/2,
```

while `Q(zeta_n)` is generally a quadratic extension of `K_n`. The full DFT
uses both cosine and sine information, so it naturally lives in the full
cyclotomic field. A trace/corner ledger that uses only real parts may live in
`K_n`, but that requires a separate conjugation-invariant reduction.

Cost possibilities:

- computing the full DFT and then taking real/cosine combinations pays the
  full cyclotomic-field cost and only then descends;
- carrying the full field as a quadratic extension of `K_n` costs, at
  minimum, an extra degree-2 layer over the real subfield;
- restricting the task to real trace-field data may recover the `phi(n)/2`
  degree, but AFW does not prove that the restricted task has the same
  multiplicative-complexity lower bound.

For the program, this means AFW supports the slogan "the same cyclotomic
ladder is present" but does not by itself license replacing `Q(zeta_n)` by
`K_n` in a lower-bound statement.

---

## 5. Proof Techniques and Compatibility Conditions for the Program

### What the Paper Uses

AFW's proof techniques are:

- rational equivalence of semilinear systems;
- finite abelian group decomposition into p-primary factors;
- tensor/Kronecker product identities for DFT matrices;
- cyclotomic field theory and unit-group structure;
- Vandermonde matrices generated by primitive roots of unity;
- CRT splitting of polynomial quotient algebras;
- companion-matrix representations of quotient algebras;
- separate odd-prime and `p = 2` analyses;
- dimension counts using cyclotomic degrees and multiplicativity of `phi`;
- semisimple algebra closure under tensor product.

No use of Lindemann-Weierstrass or transcendence machinery is visible. The
provenance tag for the algebraic content is methodologically pre-L-W: it is
modern packaging of cyclotomic/Galois/linear-algebra material, not a
post-L-W transcendence input.

### What Must Hold for Combination with Closure-Depth + Kraft Accounting

To combine AFW with the program's closure-depth and Kraft accounting, the
following extra claims would have to be proved outside AFW:

1. **Model alignment.** Essential nonrational m/d steps must be converted to
   the primitive operations of model (3) or to a precisely defined ASLP model
   (4). In particular, algebraic constants and field adjunctions cannot remain
   silently free if the program wants degree-cost lower bounds.

2. **Task alignment.** The program's T1/T3 corner tasks must be reduced to,
   or shown to contain, an AFW-style semilinear cyclotomic subsystem in the
   lower-bound direction. AFW proves DFT complexity, not corner-enumeration
   or value-certificate complexity.

3. **Real-subfield descent.** The full-cyclotomic AFW system must either be
   kept as the paid object or replaced by a proved trace-field subsystem over
   `K_n`.

4. **Kraft structure.** The AFW tensor/direct-sum parse tree must be encoded
   by prefix-free descriptions with a proven Kraft inequality, or dominated
   by a universal semicomputable measure in the Fortnow sense.

5. **Lower-bound transfer.** Additive accounting over AFW direct summands
   must become a primitive-op lower bound for the selected task ledger
   (`V_cert`, `O_cert`, or another survivor), not merely an exact count for a
   different linear transform.

If these conditions fail, AFW remains valuable as a structural comparison
theorem but does not close the compute-cost branch.

---

## Closing Sentence for FFT-CYCLOTOMIC-COMPLEXITY

This contributes the rational-equivalence reduction of finite-abelian-group
DFTs to semisimple cyclotomic algebra systems, with computable
multiplicative complexity and constructible minimal algorithms, to the
K_n-Kraft transport, with hypothesis class semilinear algebraic computation
over `Q` counting essential nonrational multiplication/division steps, proof
technique rational equivalence plus CRT/tensor decomposition of cyclotomic
semisimple algebras, provenance tag methodologically pre-L-W, and slots into
[memos/COUNTING-APPARATUS.md](memos/COUNTING-APPARATUS.md) item (A) as a
structure theorem for model (4) and a candidate input to model (3) only after
a separate cost-conversion theorem.

---

## Trust Boundary

This brief should be cited for:

- AFW's structural decomposition of DFT complexity into semisimple
  cyclotomic algebra;
- the distinction between AFW's multiplicative-complexity currency and the
  program's desired Kraft/primitive-op currency;
- the fact that real-subfield descent is not supplied by AFW itself.

It should not be cited as proving:

- a prefix-free/Kraft version of FFT complexity;
- a primitive-op lower bound for the program's T1/T3 tasks;
- a real-subfield `K_n` multiplicative-complexity theorem;
- a closed-form formula for every finite abelian DFT without doing the
  field-summand count required by the paper's Remark 3.

---

## Reflection Addendum: What the Directed Read Did Not Quite Capture

The five-question directed read caught the main bridge hazards, but a few
technical and methodological points deserve to be on record.

### AFW's "Tensor Framework" Is Not Modern Tensor-Rank Language

The search memo calls AFW the tensor-framework paper. That is fair if
"tensor" means Kronecker products of DFT matrices and tensor products of
semisimple algebras. It is potentially misleading if read as modern tensor
rank / border-rank complexity. AFW's invariant is the number of essential
nonrational multiplication/division steps in semilinear systems, preserved
under rational equivalence. The tensor products are structural devices for
assembling finite abelian groups from p-primary pieces, not a standalone
tensor-rank lower-bound method.

For the program, this matters because a tensor-rank bridge to Kraft would
be a different project. The AFW bridge candidate is instead:

```text
finite abelian DFT
  -> rational equivalence
  -> cyclotomic semisimple algebra factors
  -> essential m/d count
```

Any Kraft transport has to start from that chain, not from a generic
tensor-complexity slogan.

### Nonuniformity Is a Real Gap

AFW treats each finite system `F(G)X` as a fixed semilinear system. The
paper proves computability of the multiplicative complexity and
constructibility of minimal algorithms for the fixed system after the
cyclotomic decomposition is performed. It does not maintain a uniform
machine that, given a code for `G`, emits the decomposition with code-length
cost charged.

This is a major mismatch with prefix-free/Kraft accounting. Kraft wants a
description language over a family of objects. AFW gives exact algebraic
complexity after the object is fixed and after rational equivalence and
field decompositions are admitted as structural transformations. The
program cannot get a Kraft ledger merely by pointing at the finite direct
sum; it needs a uniform, self-delimiting compiler for those direct-sum
tokens.

### Rational Equivalence Quotients Away Data the Program May Need

AFW's central equivalence relation is intentionally coarse: nonsingular
rational pre- and post-transformations preserve multiplicative complexity.
This is exactly what makes the theorem work, but it is also dangerous for
the counting-program ledgers.

The recent ledger work cares about positional/cell incidence and value
certificates. A rational change of basis can preserve multiplicative
complexity while destroying the visible cell-level structure a task such as
T1 or T3 asks for. Thus AFW may factor through a quotient that is correct
for DFT multiplicative complexity but too coarse for `V_cert`-style task
admissibility.

This does not make AFW unusable. It means any reduction from a corner task
to an AFW system has to specify which structure survives rational
equivalence and which structure is allowed to be forgotten.

### "Computable Complexity" Is Not Yet a Closed Formula

AFW deliberately changes the conclusion of the semisimple-system theorem
from an explicit sum to "computable" complexity, because the number of
direct summands is not tracked in the exposition. Remark 3 says that to
actually compute the complexity one must know the number of direct summands
or fields in tensor products of cyclotomic fields, i.e. the number of
maximal ideals in those tensor products.

So the paper is stronger than an existence proof but weaker than a ready
closed-form ledger for arbitrary `G`. The field-summand count is itself a
computational subtask. If the program wants constants, AFW points to a
number-theoretic counting problem that still has to be executed or imported
from the later exact-count literature.

### The p = 2 Case Is Structurally Special

The p-primary proof splits odd primes and `p = 2` because the unit group of
`Z/2^k Z` is not cyclic for `k >= 3`. The `p = 2` case produces two
semisimple blocks `K(2^k; 1)` and `K(2^k; 2)`, rather than the single-block
recursion pattern for odd primes.

This should temper any too-smooth "binade tower" language. The binary tower
does align with the program's log-side binades, but AFW's algebra says the
power-of-two side has its own structural wrinkle. Heideman-Burrus is still
the better source for exact binary constants; AFW supplies the structural
reason the binary case is not merely the odd-prime case with `p = 2`
substituted.

### The Dimension Hypothesis Is the Hidden No-Collapse Condition

The semisimple complexity theorem applies when the rational vector-space
dimension of the coefficient span matches the sum of the dimensions of the
associated fields or semisimple algebras. AFW verifies this with cyclotomic
degree counts such as `[Q(zeta_m):Q] = phi(m)`.

For the program, this is the algebraic-complexity analog of a no-collapse
condition. It says the relevant cyclotomic content has not accidentally
fallen into a smaller rational span. Any value-certificate ledger that tries
to inherit AFW's lower-bound force will need its own no-collapse statement,
not just a list of field labels.

### Semisimplicity Is Doing Real Work

AFW's clean additivity is tied to semisimple abelian `Q`-algebras. This is
safe for cyclotomic factors in characteristic zero because the relevant
polynomial splittings are squarefree and CRT decomposes into field products.
If the program later moves to degenerate quotient rings, repeated factors,
or approximate/numerical objects that do not retain semisimplicity, AFW's
direct-sum additivity should not be assumed to survive.

### Additions and Heights Are Invisible

AFW's theorem is purpose-built for essential m/d complexity. Additions,
rational transformations, coefficient heights, conditioning, and numerical
precision are outside the cost. That is not a defect of the paper, but it is
a defect if imported unmodified into a primitive-op lower bound.

This is especially relevant because the program's compute model (3) pays
for arithmetic at degree `d` and precision `epsilon`, while AFW neither pays
for precision nor for the size of rational matrices used in equivalence
transformations. A model-conversion theorem has to decide whether those
costs remain free, are bounded by a harmless polynomial, or dominate the
desired ledger.

### The Best Use of AFW May Be Negative

AFW may ultimately be most valuable not because it closes the bridge, but
because it identifies exactly what the bridge must not silently quotient:

- uniform code cost;
- prefix-freeness;
- real-subfield descent;
- positional/cell incidence;
- coefficient height and numerical precision;
- task-specific output semantics.

That is a useful negative result for the directed-read agenda. If the
program later states a circle-side compute lower bound, it should be able to
say which of those AFW-quotiented structures was restored, and where.
