# AILON-2013-UNITARY-FFT-LOWER-BOUND-BRIEF

Source-extraction memo on Nir Ailon, "A Lower Bound for Fourier Transform
Computation in a Linear Model Over 2x2 Unitary Gates Using Matrix Entropy,"
arXiv:1305.4745v1 [cs.CC], 21 May 2013; local PDF compiled April 26, 2021
([sources/Ailon-LB-1305.4745v1.pdf](sources/Ailon-LB-1305.4745v1.pdf)).

**What was read.** The local four-page PDF was read in full. Lens:
extract the author's survey of the Fourier-transform lower-bound field,
state the spare unitary layered model, and record why the result belongs
beside the four FFT-complexity briefs even though it is not one of the
four canon papers used by the main outline.

**Confidence level.** High on the theorem statement, model definition,
and proof sketch: the paper is short and self-contained. Medium on
program import: using Ailon as adjacent prior art for the program's
transaction-cost / phase-defect direction is repo-side positioning, not
the paper's claim.

---

## 1. Survey Payload

Ailon opens by framing nontrivial lower bounds for Fourier-transform
computation in broad linear-circuit models as a longstanding open problem.
The paper's useful survey facts:

- A broad linear algorithm model computes a sequence of affine functions:
  start from coordinate projections and constants; each step adjoins
  `lambda_i f + mu_i g` from previously available functions.
- A super-linear lower bound is trivial, but no nontrivial lower bound is
  known in the unrestricted broad model.
- Known lower bounds impose strong restrictions on the computational
  model.
- Morgenstern 1973 gives `Ω(n log n)` for the unnormalized Fourier
  transform when coefficients are bounded.
- Morgenstern's determinant potential sees the unnormalized Fourier
  determinant `n^(n/2)` and controls determinant growth per step.
- The determinant method does not explain a lower bound for the normalized
  Fourier transform, whose determinant has modulus `1`.

Ailon's stated moral is that a useful potential for the normalized Fourier
transform should not be determinant-based; the paper proposes matrix
entropy as the replacement potential in a restricted unitary model.

### Program Use

This is the cleanest adjacent citation for "direct broad Fourier lower
bounds are hard, and the known successful results depend on restrictions."
It complements
[fft/MORGENSTERN-1973-BRIEF.md](fft/MORGENSTERN-1973-BRIEF.md):
Morgenstern is bounded-coefficient / determinant / unnormalized; Ailon is
unitary-layered / entropy / normalized.

For `paper/FIRST-PROOF.md` and `fft/PHASE-DEFECT.md`, Ailon supports a
trust-boundary posture: the program should not casually claim a broad FFT
lower bound. If the program lands, it lands as a structural no-escape
statement about the mult/add seam and its defect object, not as a direct
solution to the unrestricted linear-circuit lower-bound problem.

---

## 2. The Unitary Layered Circuit Model

Ailon's model has layers

```text
L_0, L_1, ..., L_m,       L_i in C^n.
```

`L_0` is the input vector and `L_m` is the output vector. At each step
`i >= 1`, choose two coordinates

```text
k_i, ell_i in [n],        k_i < ell_i,
```

and a complex unitary `2 x 2` matrix

```text
A_i = [ a_i(1,1)  a_i(1,2) ]
      [ a_i(2,1)  a_i(2,2) ].
```

All coordinates outside `{k_i, ell_i}` stay fixed. The two selected
coordinates are updated by applying `A_i`:

```text
[ L_i(k_i)   ]       [ L_{i-1}(k_i)   ]
[ L_i(ell_i) ] = A_i [ L_{i-1}(ell_i) ].
```

So one counted gate is exactly one unitary mixing of two coordinates.
The model is layered and has only `n` live complex numbers at any moment.
It cannot reuse an older layer directly.

### Relation to Morgenstern

Ailon explicitly says this model is strictly weaker than Morgenstern's
linear-algorithm model:

- it is not stronger because every matrix entry in a unitary `2 x 2`
  gate has modulus at most `1`;
- it is strictly weaker because gates must be unitary;
- it is also weaker because the layered model has bounded memory: later
  layers cannot directly access coordinates from earlier layers.

The normalized FFT still fits: Ailon states that the normalized FFT is
implemented as a unitary layered circuit with `m = O(n log n)`.

### Program Use

This model is spare enough to sit beside the other FFT source briefs as a
clean hypothesis class. It is not the program's model, but it gives a
useful comparison point for FIRST-PROOF's "native operations compose into
closure classes" language: here the native operation is a `2 x 2` unitary
coordinate mixing, and the closure is products of those sparse unitary
updates.

---

## 3. The Lower Bound

Theorem 2.1:

```text
If a unitary layered circuit computes the normalized Fourier transform,
then m >= (1/2) n log_2 n.
```

Let `M_i = Atilde_i Atilde_{i-1} ... Atilde_1`, where `Atilde_i` is the
`n x n` identity except for the selected `2 x 2` unitary block. Then
`M_0 = Id` and `M_m = F`, the normalized Fourier matrix.

Ailon defines the potential

```text
Phi(M) = - sum_{p,q} |M(p,q)|^2 log_2 |M(p,q)|^2.
```

For a unitary matrix, this is the sum of the Shannon entropies of the
row-wise probability vectors `(|M(p,q)|^2)_q`.

The endpoints are:

```text
Phi(Id) = 0,
Phi(F)  = n log_2 n,
```

because every entry of the normalized Fourier matrix has modulus
`1/sqrt(n)`.

The proof's key step is:

```text
Phi(M_i) - Phi(M_{i-1}) <= 2.
```

Only two rows change at each gate. Their squared moduli are redistributed
while the coordinate-wise sums

```text
|x'(j)|^2 + |y'(j)|^2 = |x(j)|^2 + |y(j)|^2
```

are preserved by unitarity. The entropy of the two changed rows can
increase by at most `2`. Therefore at least `(n log_2 n)/2` gates are
needed to reach the normalized Fourier matrix from the identity.

### What This Result Explains

Morgenstern's determinant potential sees volume growth, so it naturally
fits the unnormalized Fourier matrix. Ailon's entropy potential sees
mixing / delocalization of row mass, so it sees the normalized Fourier
matrix even though determinant magnitude is `1`.

This is program-relevant because it separates two lower-bound currencies:

- determinant / volume growth under bounded coefficients;
- entropy / row-spread growth under unitary two-coordinate mixing.

Both reach `Ω(n log n)`, but by different restricted mechanisms.

---

## 4. Trust Boundary

### This Brief Should Be Cited For

- Ailon's survey claim that nontrivial Fourier-transform lower bounds in
  broad linear-circuit models are longstanding open and that known results
  require strong model restrictions.
- The unitary layered circuit model: `n` live coordinates, each step a
  `2 x 2` unitary gate on two coordinates.
- The comparison to Morgenstern: Ailon's model is strictly weaker than the
  bounded-coefficient linear-algorithm model, and determinant potential
  does not handle the normalized Fourier transform.
- The `Ω(n log n)` lower bound for normalized Fourier transform in the
  unitary layered model.
- Matrix entropy as the potential function replacing determinant growth in
  this restricted setting.

### This Brief Should NOT Be Cited For

- Any lower bound in unrestricted linear-circuit models.
- Any lower bound for arbitrary FFT-style algorithms.
- Any lower bound for the program's transaction-cost object `δ`.
- Any proof of the character reflection barrier, phase-lift
  conservativity, or PHASE-DEFECT's cocycle non-compressibility.
- Any certification-cost, field-adjunction, root-isolation, or `V_cert`
  claim.
- Any claim about rational-equivalence multiplicative complexity.

### Program Position

Ailon is adjacent prior art, not one of the four canon sources in
`paper/IMPOSSIBILITY-OUTLINE.md`. Its role is to keep the paper honest
about the landscape: the FFT lower-bound literature has real `Ω(n log n)`
results, but each successful lower bound is attached to a restriction
that makes a potential function monotone. The program's proposed
No-Free-Descent direction should be framed as a structural obstruction
around the mult/add seam, not as a broad-model FFT lower-bound theorem.

## Closing Sentence

Ailon supplies a spare restricted model and an entropy potential reaching
the same `Ω(n log n)` scale as Morgenstern, while explicitly preserving
the field's warning label: broad Fourier-transform lower bounds remain
open, and model restrictions do the work.
