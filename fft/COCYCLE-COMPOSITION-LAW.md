# COCYCLE-COMPOSITION-LAW

Structural analysis of [fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md)
sub-debt 1 — *formal-character FFT composition* — addressing the
binary question "does FFT-style composition have a natural formulation
at the formal-character level, or does it require analytic
realization?" with a sharper partial-yes verdict and a worked case in
floating-point Cooley-Tukey radix-2.

This memo is the upstream blocker for
[memos/AMORTIZATION-AT-THE-BOUNDARY.md](memos/AMORTIZATION-AT-THE-BOUNDARY.md):
without a precise cost meaning for "competitive construction of `{Δ_k}`
in `C_FFT`," the amortization conjecture's `C_S(N)` is not yet a typed
object. The deliverable here types it, conditional on the cost-norm
choice the verdict surfaces.

Per [memos/AGENTS.md](memos/AGENTS.md): exploratory; no new external
sources; sharpens existing program material.

---

## The sub-debt

From [fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md) §"Sub-debts":

> **Formal-character FFT composition.** Does FFT-style composition (the
> canon's standard composability) have a natural formulation at the
> formal-character level, or does it require analytic realization? If
> the latter, the cocycle reframe is an abstraction step, not a
> structural one.

The question is binary on its face. The honest answer is **partial**.

---

## Verdict (preview)

**Partial yes — structural skeleton is formal-character; per-operation
residuals are analytic.**

The composition law has a natural formal-character form:

```text
Δ_k((O_2 ∘ O_1) m)  =  Δ_k(m) · Δ_k^{O_1}(m) · Δ_k^{O_2}(O_1 m) · χ_k(c_{O_2, O_1}(m))
```

(Notation. `Δ_k(·)` takes a real input — the mantissa value — per the
setup at §"Setup" below; per-operation factors carry an exponent,
`Δ_k^O(m)`. The verdict's LHS reads "absolute cocycle value at the
composed-input point `(O_2 ∘ O_1) m`," not as a per-composition factor.
There is no separate notation for per-composition factors; the path-
product on the RHS does that work.)

where:

- `Δ_k^O` is the per-operation cocycle factor associated with native
  operation `O` (a formal-character object once `O`'s action on
  binade structure is named);
- `c_{O_2, O_1}(m)` is the composition cross-term measuring how `O_2`
  and `O_1` interact across binade boundaries;
- `χ_k(·)` is the formal character of `A = ℝ/ℤ`.

The composition extends to `n`-fold compositions by the obvious
recursion. The total cocycle of an FFT-style scheme `S` is a product
of per-operation factors and cross-terms along the composition path.

**What is formal-character.** The *structure* of the composition law:
factors and cross-terms multiply through `χ_k`, indices add by
character algebra, the path-product is a 1-cocycle on the compose-monoid
of native operations.

**What is analytic.** The *values* of `Δ_k^O(m)` and `c_{O_2, O_1}(m)`
on specific inputs `m`. To know what each factor *is*, you must
realize the operation analytically (specify how `O` moves the binade
structure of `m`).

**Consequence.** The cocycle reframe is a structural skeleton at the
formal-character level, *not a pure abstraction step* — there is real
character-algebraic content. But the skeleton requires analytic flesh
to deliver a cost quantity. This places sub-debt 1's verdict
parallel to sub-debt 3's (per
[fft/PHASE-LIFT-CONSERVATIVITY-AUDIT.md](fft/PHASE-LIFT-CONSERVATIVITY-AUDIT.md)):
formal-layer clean, analytic-layer conditional on a definitional
move (here, the cost-norm choice).

**What this provides for T4b.** The cocycle-product composition law
is the algebraic structure required for `δ ≡ cost of {Δ_k}
compression` to be a *candidate* δ-faithful coordinate for T4b
([measure/FOR-BREAKFAST.md](measure/FOR-BREAKFAST.md) §K.6 / [measure/THE-FIRST-BRIDGE.md](measure/THE-FIRST-BRIDGE.md)).
Without a composition law, δ-faithfulness cannot be stated — the
bridge needs `δ` to behave coherently under FFT-style composition
before "faithfulness" has a target. The verdict's partial-yes supplies
the formal-character skeleton that makes the candidate well-posed; the
cost-norm choice is what determines whether the resulting candidate
satisfies T4b's faithfulness condition uniformly.

---

## Setup

Following [fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md) §"Pre-π setup":

```text
A := ℝ/ℤ                              additive clock
L := ℝ_{>0}/2^ℤ                       log-binade clock
ψ₀(m) = log₂(1+m) ∈ [0, 1)           lifted log-binade coordinate
ε(m) = ψ₀(m) − m                      defect (displacement)
χ_k : A → 𝕋    (k ∈ ℤ)               formal character of A
Δ_k(m) := χ_k(ε(m))                   defect cocycle
```

Native operations of the FFT canon (per OUTLINE §4.2.1)
act on floating-point values `v = (m, e)` where `m ∈ [0, 1)` is the
mantissa and `e ∈ ℤ` is the binade exponent. An operation `O` takes
input value(s) and produces output `v' = (m', e')`. The cocycle
`Δ_k` is determined by the mantissa coordinate `m`; the binade
exponent `e` records which binade `v` lives in.

Floating-point arithmetic crosses the additive/log-binade seam every
time an operation's output crosses a binade boundary (a *binade
renormalization*). The cocycle `Δ_k` is born at exactly these
crossings.

---

## The cocycle-product composition law (skeleton)

For a single native operation `O`, define its *per-operation cocycle
factor* by:

```text
Δ_k^O(m) := χ_k(ε(O m) − ε(m)),
```

where `O m` denotes `O`'s effect on the mantissa coordinate (with the
binade exponent updated as the operation requires). This is the
*change* in the cocycle's underlying displacement induced by `O`,
lifted through `χ_k`.

By multiplicativity of `χ_k`:

```text
Δ_k(O m)  =  χ_k(ε(O m))
          =  χ_k(ε(m) + (ε(O m) − ε(m)))
          =  Δ_k(m) · Δ_k^O(m).
```

So a single operation acts on the cocycle by *multiplication by the
per-operation factor*. The factor depends on `O`, `k`, and `m` — but
the *form* of the action is character-multiplicative.

For a composition `O_2 ∘ O_1`:

```text
Δ_k((O_2 ∘ O_1) m)  =  Δ_k(O_1 m) · Δ_k^{O_2}(O_1 m)
                    =  Δ_k(m) · Δ_k^{O_1}(m) · Δ_k^{O_2}(O_1 m).
```

This is the *cocycle-product law*: composition multiplies per-operation
factors evaluated along the composition path.

The cross-term `c_{O_2, O_1}(m)` mentioned in the verdict preview
collapses to zero in this clean form because `Δ_k` itself is
multiplicative under `χ_k`. A cross-term arises only when the
arithmetic on `(m, e)` involves *implicit* renormalization that
re-routes the binade structure mid-composition — which is what
happens, e.g., when fused multiply-add or guarded rounding modes
break the (operate)(renormalize) factorization. Under the regularity
guard ([fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md) §"Closure-class
regularity guard": uniform, non-growing, fixed-base-field; no
fused-arithmetic advice) the cross-term vanishes and the composition
law has the clean form above.

**This is the formal-character skeleton.** It is stated entirely in
character algebra: characters multiply, indices add, factors compose
along paths. No analytic content has entered the *form*.

---

## Where the analytic content lives

The *value* of each per-operation factor `Δ_k^O(m)` is analytic. To
compute `Δ_k^O(m)`:

1. Realize `O`'s action on `(m, e)` analytically (specify which binade
   the output lands in, whether renormalization fires, and what `m'`
   results).
2. Compute `ε(O m) = log₂(1 + m') − m'`.
3. Form the difference `ε(O m) − ε(m)`.
4. Apply `χ_k` (analytically, `e^{2πik(ε(O m) − ε(m))}`).

Each step depends on the analytic realization. The character algebra
gives the *form* of the answer (a phase factor in `𝕋`); the analytic
realization gives the *value*.

This is the load-bearing observation. The cocycle reframe extracts
real character-algebraic structure (the composition law, the
multiplicativity, the path-product) without committing to which
specific phase factors arise. The phase factors themselves are the
analytic content the cost framework will quantify over.

---

## Worked case: floating-point Cooley-Tukey radix-2

The canonical in-scope test case per
[fft/SCHOENHAGE-STRASSEN-COCYCLE-TRANSLATION.md](fft/SCHOENHAGE-STRASSEN-COCYCLE-TRANSLATION.md):
"Cooley-Tukey radix-2 FFT applied to floating-point complex numbers
(...mantissa × mantissa crosses the seam every butterfly through
binade renormalization)."

**Scope of this section.** The worked case is *schematic*. Each native
operation is treated as a single binade-renormalizing operation on its
operand's mantissa coordinate; the precise decomposition of FP complex
multiplication into four real multiplications and two real additions
(`(a+bi)(c+di) = (ac−bd) + (ad+bc)i`), the per-component mantissa /
exponent bookkeeping, and the rounding-mode details are not modeled
here. The point is to illustrate the formal-character cocycle-product
structure on a recognizable FFT computation, not to model FP complex
arithmetic faithfully. A faithful FP-arithmetic treatment unpacks each
schematic operation into its constituent real-arithmetic native ops,
each carrying its own per-operation cocycle factor; the path-product
structure then aggregates over the unpacked native ops without change.

Length-`N` Cooley-Tukey radix-2 on input `x[0], ..., x[N-1]`
(each a floating-point complex number, decomposed into mantissa-exponent
pairs per real and imaginary part) computes:

```text
X[k]         =  E[k]  +  ω_N^k · O[k]
X[k + N/2]   =  E[k]  −  ω_N^k · O[k]
```

where `E, O` are sub-FFTs and `ω_N = e^{-2πi/N}` is the twiddle.

Three native operations enter:

### Twiddle multiplication (`v ↦ ω_N^k · v`)

Multiplying a floating-point value `v = (m, e)` by `ω_N^k` produces
output mantissa `m' = m · |ω_N^k|_mantissa` modulo binade
renormalization. Twiddles are unit-modulus, so `|ω_N^k|_mantissa = 1`
exactly only at trivial `k`; for general `k`, `ω_N^k` decomposes into
real and imaginary mantissas with their own binade structure, and the
multiplication renormalizes into a new mantissa.

The per-operation factor `Δ_k^{twiddle}(m)` measures the displacement
change induced by the renormalization. **Form**: pure `χ_k`. **Value**:
depends on which binade the post-multiplication mantissa lands in.

### Butterfly addition (`v_1, v_2 ↦ v_1 + v_2`)

Adding two floating-point values requires aligning their binade
exponents, performing integer mantissa addition, and renormalizing the
result into a canonical binade. The renormalization is the seam
crossing: the result's mantissa coordinate `m'` is determined by
`m_1, m_2, e_1, e_2` and the renormalization rule.

The per-operation factor `Δ_k^{add}(m_1, m_2)` measures the cocycle
displacement change. **Form**: pure `χ_k`. **Value**: depends on
whether the sum's most-significant bit flipped (renormalization fired),
and where in the new binade the result mantissa lands.

### Butterfly subtraction (`v_1, v_2 ↦ v_1 − v_2`)

Same shape as addition but with subtraction. The interesting case is
*catastrophic cancellation*: if `v_1 ≈ v_2`, the subtraction loses
significant bits and renormalizes downward across multiple binades.
The cocycle factor reflects this — large negative displacement in `ε`
when many binades are crossed in one operation.

The per-operation factor `Δ_k^{sub}(m_1, m_2)`. **Form**: pure `χ_k`.
**Value**: highly analytic, especially in the cancellation regime.

### Composition across the FFT

Cooley-Tukey radix-2 on length `N = 2^n` performs `O(N log N)` of these
operations, organized in `n = log_2 N` butterfly stages. The total
cocycle along this composition is:

```text
Δ_k(CT_N input)  =  Δ_k(input)  ·  ∏_{stages s, butterflies b ∈ s}  Δ_k^{b}(state_{s,b})
```

where `state_{s,b}` is the working value at stage `s`, butterfly `b`.
The product runs over the entire FFT computation.

The product *form* is formal-character (a product of `χ_k`-valued
factors). The product *value* requires running the FFT analytically
and recording each factor.

**This is the typed object the amortization conjecture quantifies
over.** `C_S(N)` is a chosen norm on the product — sum of factor
log-magnitudes, count of non-trivial factors, sum of branch
displacements, etc. The choice of norm is the cost-norm definitional
move.

---

## Cost-norm choice (the definitional move)

PHASE-DEFECT's §"What this would buy" lists candidate definitions of
"competitively compressible," any of which translates to a cost-norm
on the cocycle product:

- *Operational definition* (primary): "the scheme produces a
  defect-free FFT-style composition law whose character products agree
  across all butterfly refinements and primitive modes." Cost-norm:
  the *failure-to-agree* across refinements, measured pointwise.
- *Low-rank approximation*. Cost-norm: rank of the joint
  `(input, mode k) → Δ_k` map.
- *`O(N log N)` evaluation without paying the residual-coordinate
  cost*. Cost-norm: the residual-coordinate cost itself.
- *Factorization as a finite product of simpler cocycle factors*.
  Cost-norm: the number/depth of factor decomposition needed.

Under the formal-character skeleton, each of these is a well-typed
cost-norm on the cocycle product. The amortization conjecture in
AMORTIZATION-AT-THE-BOUNDARY is *cost-norm-relative*: it asserts the
existence of some `c > 0` such that `C_S(N) ≥ c · N` *for the chosen
cost-norm*.

The recommendation from this memo, consistent with AMORTIZATION's
pointer that the operational definition is the load-bearing one: adopt
the operational cost-norm. It is testable on candidate schemes,
matches the form of the L-W per-sample lower bound (each sample
contributes a per-character disagreement that cannot be averaged
away), and does not pre-suppose representation machinery.

The other cost-norms are sharper analytic tests if the operational
form needs backing; they remain available as secondary commitments.

---

## Consequences for AMORTIZATION-AT-THE-BOUNDARY

This memo discharges the first of AMORTIZATION's three blockers:

1. ~~PHASE-DEFECT sub-debt 1 (formal-character FFT composition).~~
   **Discharged here** as partial-yes: the cocycle-product composition
   law is the formal-character skeleton; cost-norm is the analytic
   definitional move; operational compressibility is the recommended
   choice.
2. PHASE-DEFECT sub-debt 3 (phase-lift conservativity) + `C_Aff`
   definitional move. *Still open* — see
   [fft/PHASE-LIFT-CONSERVATIVITY-AUDIT.md](fft/PHASE-LIFT-CONSERVATIVITY-AUDIT.md).
3. Effective Hermite-Lindemann at `n = 1`. *Still open* — program
   substrate-side interim target.

With (1) discharged, the amortization conjecture is well-typed:
`C_S(N)` is the operational-cost-norm of the cocycle product across
`S`'s composition path. Route 3 (L-W envelope) now has a target
quantity to bound below.

The reduction surfaced by AMORTIZATION — non-amortization at the
boundary reduces to effective H-L `n = 1` — sharpens correspondingly:
the effective H-L bound must be in the form of a per-sample
disagreement contribution to the operational cost-norm. That is the
content the substrate-side work owes the algorithm-side argument.

---

## Consequences for the other PHASE-DEFECT sub-debts

- **Sub-debt 2 (closure-class transport, general).** This memo gives
  the composition law side; transport across closure classes is a
  different question (whether `{Δ_k} ∈ C_FFT` reflects to `ε ∈ C_Aff`
  at competitive cost). Sub-debt 2 is unaffected at the structural
  level but acquires a sharper target — transport must respect the
  cocycle-product composition law derived here.
- **Sub-debt 3 (phase-lift conservativity).** Unaffected directly, but
  the parallel verdict shape ("formal layer clean; analytic layer
  conditional on a definitional move") is now confirmed across two
  sub-debts. Suggests a methodological pattern: each sub-debt of
  PHASE-DEFECT will likely have a clean formal-character verdict and
  a load-bearing analytic definitional move.
- **Sub-debt 4 (canon-bound translation).** Unaffected. SS verdict is
  the only one in hand; Morgenstern, Winograd, AFW remain.

---

## What this memo does not do

- **Does not prove the cocycle-product law rigorously.** The
  derivation is informal: multiplicativity of `χ_k` plus the
  factorization assumption (no fused-arithmetic advice). A rigorous
  treatment would: (a) specify the floating-point arithmetic model in
  full; (b) verify the factorization assumption against the regularity
  guard; (c) handle edge cases (subnormal numbers, overflow,
  underflow) explicitly. Each is downstream.
- **Does not commit to a cost-norm.** The operational cost-norm is
  recommended; the other candidates remain available. The choice has
  consequences for both the AMORTIZATION reduction and the
  PHASE-DEFECT promotion path; pinning it requires a separate
  decision.
- **Does not verify the regularity guard's exhaustiveness.** The
  cross-term collapse depends on the regularity guard excluding
  fused-arithmetic schemes. Whether the guard's excluded patterns are
  exhaustive is a separate audit (per ALGEBRA-OF-DELTA §(2) and §(6)).
- **Does not promote the cocycle reframe to load-bearing in
  [paper/FIRST-PROOF.md](paper/FIRST-PROOF.md).** Promotion requires
  PHASE-DEFECT's gates to close — including sub-debt 3 and the
  canon-bound translations. This memo discharges one of three
  blockers AMORTIZATION named.

---

## Updates to PHASE-DEFECT.md

§"Sub-debts" should record:

- **Sub-debt 1 verdict.** Partial yes per
  [fft/COCYCLE-COMPOSITION-LAW.md](fft/COCYCLE-COMPOSITION-LAW.md).
  The composition law has a formal-character skeleton (cocycle product
  across path); per-operation residuals require analytic realization.
  Cost-norm choice is the load-bearing definitional move; operational
  compressibility is the recommended choice. Verdict shape parallels
  sub-debt 3's audit: formal layer clean, analytic layer conditional
  on a definitional move.

§"What gets rewritten if the gates resolve favorably" should record:
sub-debt 1 is no longer blocking; the cost meaning of `δ ≡ cost of
{Δ_k} compression` is now well-typed (operational cost-norm on the
cocycle product). PHASE-DEFECT promotion to load-bearing remains
gated on sub-debt 3 (phase-lift conservativity + `C_Aff` definitional
move) and on canon-bound translation (sub-debt 4) for the in-scope
canon frameworks.

---

## Trust boundary

The cocycle-product composition law is sharpened in this memo from
PHASE-DEFECT's §"What this would buy" implicit factorization candidate.
The sharpening uses only multiplicativity of `χ_k` (formal-character
algebra) and the regularity-guard assumption (no fused-arithmetic
advice). No transcendence content enters the structural derivation;
analytic content enters when per-operation residuals are evaluated
on specific values.

The Cooley-Tukey worked case is illustrative, not a proof. The
canonical in-scope status of FP CT-radix-2 is per
[fft/SCHOENHAGE-STRASSEN-COCYCLE-TRANSLATION.md](fft/SCHOENHAGE-STRASSEN-COCYCLE-TRANSLATION.md);
the per-operation analysis (twiddle, butterfly addition, butterfly
subtraction) is sketched at the level needed to ground the
cost-norm discussion.

The cost-norm choice is named as a definitional move; the recommended
choice (operational compressibility) is consistent with PHASE-DEFECT's
primary definition. **As of `paper/OUTLINE.md` §6.4 /
construction-debt #14, the program has committed to operational
compressibility as the cost-norm**, ahead of PHASE-DEFECT's full
promotion. The earlier trust-boundary discipline ("should not be cited
as a program commitment until PHASE-DEFECT's promotion lands") is
superseded for this specific choice; PHASE-DEFECT promotion remains
gated on its own sub-debts (3 and 4) but the cost-norm question is
no longer downstream of that promotion.

This memo does not introduce new external sources. All inputs are
existing program material:
[fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md),
[fft/PHASE-LIFT-CONSERVATIVITY-AUDIT.md](fft/PHASE-LIFT-CONSERVATIVITY-AUDIT.md),
[fft/SCHOENHAGE-STRASSEN-COCYCLE-TRANSLATION.md](fft/SCHOENHAGE-STRASSEN-COCYCLE-TRANSLATION.md),
[memos/AMORTIZATION-AT-THE-BOUNDARY.md](memos/AMORTIZATION-AT-THE-BOUNDARY.md),
[measure/ALGEBRA-OF-DELTA.md](measure/ALGEBRA-OF-DELTA.md),
[paper/OUTLINE.md](paper/OUTLINE.md),
[paper/FIRST-PROOF.md](paper/FIRST-PROOF.md).
