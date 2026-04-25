# MORGENSTERN-1973-BRIEF

Source-extraction memo on Jacques Morgenstern, "Note on a lower bound of
the linear complexity of the fast Fourier transform," Journal of the ACM
20.2 (1973), 305-306
([sources/FFT-lower-bound.pdf](sources/FFT-lower-bound.pdf)).

**What was read.** The local two-page PDF was read with the specific lens
from [fft/FFT-CYCLOTOMIC-COMPLEXITY.md](fft/FFT-CYCLOTOMIC-COMPLEXITY.md):
does Morgenstern's bounded-coefficient hypothesis supply the structural
constraint that keeps the A-axis of
[memos/LEDGER-PIVOT-SEARCH.md](memos/LEDGER-PIVOT-SEARCH.md) cost-bearing,
by preventing algebraic / linear content from being hidden in unbounded
coefficients?

**Confidence level.** High on the statement and proof of the paper's two
propositions; the argument is short and self-contained modulo Morgenstern's
earlier linear-algorithm setup. Medium on program import: the bridge from
bounded-coefficient linear DFT circuits to T1/T3 plus `V_cert` is not in the
paper and remains a repo inference / open task.

---

## Verdict on the Lens

The reading is **verified in the bounded-linear-circuit regime** and **not
yet transported to the program's certification-cost regime**.

Morgenstern's coefficient bound is exactly the condition that prevents the
determinant / volume growth of a Fourier matrix from being hidden in large
linear-combination coefficients. In that sense it is structurally aligned
with the program's "certification-preserving" demand: do not let the model
erase cost-bearing algebraic content by making huge constants, arbitrary
linear maps, or uncharged advice free.

But Morgenstern proves a lower bound for bounded-coefficient **linear
algorithms** computing linear forms. He does not prove a lower bound for
algebraic certificate production, field adjunctions, root isolation, `V_cert`,
or the corner tasks T1/T3. The paper is evidence for why boundedness matters;
it is not the missing cost theorem for the compute-cost branch.

---

## 1. Hypothesis Class

### What the Paper Proves

Morgenstern works with a linear algorithm over `C`.

For a family `f` of linear forms in `r` variables, with coefficient matrix
`F`, an algorithm is a finite sequence of available linear affine functions.
The initial family contains constants and coordinate projections. Each counted
step adjoins one new function of the form

```text
h = lambda f + mu g,
```

where `f` and `g` were already available and `lambda, mu in C`.

The coefficient hypothesis is:

```text
|lambda| <= c,  |mu| <= c,  c > 1/2,
```

at every counted step. The number of counted steps is the number of additions
`m+`.

Let `A(F)` be the maximum modulus of the determinant of any square submatrix
of `F`. Morgenstern proves:

```text
m+ > log A(F) / log(2c).
```

For the `n x n` DFT matrix, the rows are orthogonal with common length
`sqrt(n)`, so the determinant has modulus `n^(n/2)`. Therefore

```text
m+ > ((n/2) log n) / (log c + log 2).
```

For coefficients of modulus at most `1`, this gives

```text
m+ > (n/2) log_2 n.
```

### What the Paper Does Not Require

The paper does not require:

- algebraic coefficients;
- rational coefficients;
- a uniform algorithm over all `n`;
- bit complexity;
- precision accounting;
- field-adjunction accounting;
- root isolation;
- prefix-free descriptions.

The coefficients may be arbitrary complex numbers, provided their moduli are
bounded by `c`. The theorem is nonuniform in the usual circuit sense: it
applies to each fixed matrix `F`, and the DFT conclusion is obtained by
applying the determinant estimate to the fixed `n x n` Fourier matrix.

### Source Caution

Morgenstern notes that whether nonlinear algorithms can reduce the number of
additions for linear functions was, to his knowledge, open in this setting.
This brief therefore cites the theorem only for bounded-coefficient linear
algorithms, not for arbitrary algebraic algorithms.

---

## 2. Where Boundedness Bites in the Proof

### What the Paper Proves

The proof is a determinant-growth argument.

At any stage, take a square subdeterminant of maximum modulus among the
currently available forms. If the next added form

```text
h = lambda f + mu g
```

does not occur in the determinant being considered, the maximum determinant
does not increase. If it does occur, multilinearity of the determinant gives
the new determinant as

```text
lambda D' + mu D'',
```

where `D'` and `D''` are determinants from the previous stage. Since their
moduli are bounded by the previous maximum and since
`|lambda|, |mu| <= c`, one step can increase the maximum determinant by at
most a factor of `2c`.

Starting from coordinate projections, where the determinant maximum is `1`,
after `m+` additions the maximum determinant is at most `(2c)^(m+)`. To
produce a matrix with determinant scale `A(F)`, one must have

```text
(2c)^(m+) >= A(F).
```

This is the whole lower bound.

### What Happens if the Hypothesis Is Relaxed

If `c` is larger, the lower bound weakens by the denominator `log(2c)`.
If `c = c(n)` grows with the problem size, the DFT lower bound becomes

```text
Omega(n log n / log c(n)).
```

If no coefficient bound is imposed, the determinant argument gives no
nontrivial asymptotic lower bound: a single step may increase determinant
scale by an arbitrarily large factor. Volume growth can be hidden in the
coefficients.

This is the precise sense in which bounded coefficients are structurally
protective. They are not a cosmetic numerical restriction; they are the
mechanism that prevents unbounded linear combinations from destroying the
cost meaning of algebraic or spectral structure.

### Repo Inference

This supports the program's model-indexing update. Under bounded linear
combinations, the A-axis can remain cost-bearing. Under unbounded linear
combinations, the A-axis can collapse as a cost axis because the complexity
is transferred into uncharged coefficients.

The proof does not mention the convolution theorem or the FFT's
multiplication-to-addition trade directly. The connection is structural:
Morgenstern isolates the condition under which linear/additive computation
cannot absorb the hard content into coefficient magnitude.

---

## 3. Intersection with the Certification-Preserving Open Axioms

The open axioms are from
[memos/LEDGER-PIVOT-SEARCH.md](memos/LEDGER-PIVOT-SEARCH.md) §"Certification-preserving model:
open axioms."

### Axiom-by-Axiom Comparison

1. **Arbitrary algebraic constants as advice?**

   Morgenstern permits arbitrary complex coefficients of bounded modulus as
   free scalars in the linear combinations. It does not require construction
   by paid adjunction. This settles the question in the opposite direction
   from the program's likely default: bounded advice is allowed.

2. **Coefficient height-bounded?**

   Partially. Morgenstern bounds complex modulus, not algebraic height,
   description length, denominator size, or field degree. This is enough for
   determinant growth, but not enough for `V_cert` height accounting.

3. **Binary additions or arbitrary linear combinations?**

   Settled for Morgenstern: each counted step combines two previous forms.
   It is a binary fan-in linear operation with two bounded scalar
   coefficients, not an arbitrary fan-in linear transform.

4. **Precomputed DFT-like matrix free or paid?**

   Not settled in the program's sense. The target matrix `F` is fixed and
   known for the theorem, and the circuit may be chosen nonuniformly for that
   `F`. Morgenstern does not allow a full matrix-vector transform as one
   primitive step, but he also does not charge a uniform description of the
   matrix or of the circuit family.

5. **Field adjunctions paid by degree, height, or both?**

   Not settled. There is no field-adjunction operation. Complex coefficients
   are simply available if they obey the modulus bound.

6. **Root isolation paid by precision or certification depth?**

   Not settled. Morgenstern is exact linear algebra over `C`; there is no
   root-isolation or numerical-precision cost.

7. **Uniform in `N` or nonuniform advice?**

   Nonuniform. The theorem applies to a fixed `F`, and the DFT corollary
   applies it separately to each size `n`. There is no single machine whose
   code handles all `n`, and no prefix-free / Kraft charge for the family.

### Summary

Morgenstern strongly supports axiom 2's *modulus-bounded* version and axiom
3's *binary-operation* version. It leaves axioms 4-7 open for the program and
answers axiom 1 in a way that is too permissive for paid-adjunction
certification unless the program separates bounded coefficient advice from
algebraic certificate construction.

---

## 4. Transport to T1/T3 + V_cert

### What the Paper Gives

Morgenstern gives a genuine lower bound, not an upper-bound algorithm:

```text
bounded-coefficient linear algorithms for DFT_n require Omega(n log n)
additions.
```

The proof is methodologically pre-L-W. It uses determinant algebra,
orthogonality of the finite Fourier matrix, and bounded complex coefficients.
No Lindemann-Weierstrass or transcendence theorem is involved. Roots of unity
can be treated algebraically as finite-order elements; no transcendence of
`pi` is needed for the finite DFT statement.

### What Would Be Needed for Transport

To transport Morgenstern to the compute-cost branch, the program would need a
reduction of the following form:

1. Any algorithm solving T1/T3 in the chosen certification-preserving
   algebraic-arithmetic model induces a bounded-coefficient linear algorithm,
   or a determinant-growth object of the same kind.
2. The induced matrix has determinant / volume growth comparable to the
   Fourier matrix or to another explicitly computed witness.
3. The reduction preserves the `V_cert`-relevant cell / value structure.
4. The constants introduced by the reduction remain bounded in Morgenstern's
   sense, or their growth is explicitly charged in the program's model.
5. The construction is uniform or is separately paid for in Kraft / code
   length if the branch needs a prefix-free accounting.

None of these steps is in Morgenstern.

### Hazard Audit from FFT-CYCLOTOMIC-COMPLEXITY

1. **Proof-technique inversion.** Applies. Morgenstern is a lower bound, so
   it is the right direction, but it is a lower bound for bounded linear DFT
   algorithms. T1/T3 and `V_cert` are not DFT matrix-vector multiplication.
   A reduction is required.

2. **Coefficient-boundedness.** Applies positively. This is the paper's
   load-bearing hypothesis and the reason it is relevant to the
   certification-preserving regime. The match is only modulus-boundedness,
   not height-bounded algebraic certification.

3. **Nonuniformity / Kraft.** Applies. The theorem is per fixed matrix and
   has no prefix-free compiler, semicomputable measure, or universal
   dominance step. It cannot by itself close a Kraft accounting bridge.

4. **Real-subfield passage.** Applies. The DFT matrix is full complex
   cyclotomic data. The paper does not descend to the real trace field
   `K_n = Q(cos(2 pi/n))`, nor to corner x-values. A real-subfield analogue
   would have to be proved or imported.

5. **Rational-equivalence / positional data.** Applies in a modified form.
   Morgenstern's determinant lower bound is coordinate-sensitive: arbitrary
   rational or complex pre/post transformations can change determinants and
   coefficient bounds. Therefore it does not automatically survive the
   rational-equivalence quotients that AFW uses, and it does not preserve
   `V_cert`'s per-cell positional semantics without an explicit
   structure-preservation argument.

### Transport Verdict

Morgenstern can be cited as evidence that coefficient boundedness is the
right kind of structural protection for an additive / linear lower bound.
It cannot yet be cited as a primitive-op lower bound for T1/T3 + `V_cert`.

No circularity obstruction is visible at the finite cyclotomic level. The
obstructions are model conversion, task reduction, real-subfield descent,
uniformity/Kraft accounting, and preservation of positional certificate
content.

---

## Closing Sentence for FFT-CYCLOTOMIC-COMPLEXITY

This contributes Morgenstern's determinant-growth lower bound
`m+ > log A(F)/log(2c)`, yielding `m+ > (n/2) log_2 n` for the `n`-point
DFT under coefficients of modulus at most `1`, to the K_n-Kraft transport,
with hypothesis class nonuniform bounded-coefficient linear algorithms over
`C`, proof technique determinant / volume-growth control under binary
bounded linear combinations, provenance tag methodologically pre-L-W, and
slots into [memos/COUNTING-APPARATUS.md](memos/COUNTING-APPARATUS.md) item
(A) only as a bounded-linear lower-bound model that motivates the
certification-preserving constraint, not as a direct cost theorem for T1/T3
or `V_cert`.

---

## Trust Boundary

This brief should be cited for:

- the precise bounded-coefficient linear lower bound;
- why boundedness is load-bearing in the determinant argument;
- the fact that unbounded coefficients collapse the determinant-growth
  lower bound;
- the partial overlap between Morgenstern's model and the program's
  certification-preserving axioms.

It should not be cited as proving:

- a lower bound for nonlinear algebraic algorithms;
- a lower bound for T1/T3;
- a lower bound for `V_cert` certificate production;
- a real-subfield `K_n` result;
- a Kraft or prefix-free accounting theorem;
- a uniform lower bound over a family with advice/code length charged.
