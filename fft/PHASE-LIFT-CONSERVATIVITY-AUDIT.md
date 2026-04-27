# PHASE-LIFT-CONSERVATIVITY-AUDIT

L-W audit on the analytic specialization of the character reflection
barrier introduced in [fft/PHASE-DEFECT.md](PHASE-DEFECT.md). The
audit asks: does the bridge claim — that competitive construction of
`{Δ_k}` in `C_FFT` forces competitive construction of `ε(m)` in
`C_Aff` after small-branch arg-unwrapping on `[0, ε_max ≈ 0.0861]` —
import Baker-style or other post-1882 transcendence machinery?

This is the gate-deciding audit per
[fft/PHASE-DEFECT-PLAN.md](PHASE-DEFECT-PLAN.md) Edit 5 / "Promotion
Rule." A verdict here unlocks (or blocks) any rewrite of
[paper/IMPOSSIBILITY-OUTLINE.md](../paper/IMPOSSIBILITY-OUTLINE.md)
or [paper/FIRST-PROOF.md](../paper/FIRST-PROOF.md) around No Free
Descent.

## The claim, precisely

Phase-lift conservativity (analytic specialization, `χ_k(t) = e^{2πikt}`):

> If `C_FFT` competitively constructs the cocycle family
> `{Δ_k(m) := e^{2πikε(m)}}` on machine inputs `m ∈ [0, 1)`, then
> `C_Aff` competitively constructs `ε(m)` on the same inputs.

"Competitive" here means asymptotically equivalent up to constants and
log factors in a fixed cost model.

## Audit route

Per the plan:

1. Sketch the formal-cocycle transport without analytic exponential
   machinery.
2. Specialize to `χ_k(t) = e^{2πikt}`.
3. Identify every transcendence input used by the specialization.
4. Classify each input under
   [memos/OLD-TIME-RELIGION.md](../memos/OLD-TIME-RELIGION.md)'s
   content-not-calendar rule.

### Step 1 — Formal-cocycle transport

At the formal-character layer, the cocycle identity
`χ_k(ψ(m)) = χ_k(m) · χ_k(ε(m))` is just multiplicativity of `χ_k`.
The formal transport — *if `{Δ_k}` admits an FFT-style composition
law, then `ε` admits an additive-side composition law* — is an
algebraic statement about character pullbacks. No transcendence
machinery enters: the argument is a calculation in the formal
character algebra of `A = ℝ/ℤ`. **Step 1 is L-W clean by
construction.** Pre-1882 in content; pre-1882 in calendar.

### Step 2 — Specialization to `χ_k(t) = e^{2πikt}`

Specializing fixes the analytic realization. The bridge becomes a
*recovery* claim: given `Δ_1(m) = e^{2πiε(m)}` computed in `C_FFT`,
recover `ε(m)` in `C_Aff` at competitive cost.

The natural recovery is the small-branch argument:

```text
ε(m) = (1/2π) · Arg Δ_1(m),
```

well-defined on `[0, ε_max]` because `2π · ε_max ≈ 0.541 < π` keeps
the principal branch unambiguous. The recovery is exact pointwise.

The *cost* recovery requires implementing arg-on-branch in `C_Aff` at
`O(1)` per sample. Standard route: Taylor expansion of `Arg(z)`
around `z = 1`, which converges geometrically on the small branch
because `|Δ_1(m) - 1| ≤ 0.541 < 1`. To machine precision (~52 bits),
a degree-`D` truncation with `D = O(log(precision))` ≈ 60 suffices,
giving `O(1)` per sample (`D` is a *constant* in `N`, since the
precision target is fixed).

Total recovery cost: `O(N · D) = O(N)` for `N` samples. If `{Δ_k}` is
in `C_FFT` at `O(N log N)`, then `ε` is in `C_Aff` at `O(N log N) +
O(N) = O(N log N)`. **Competitive.**

### Step 3 — Transcendence inputs

The Step 2 argument uses:

- **Power series of `Arg(z)` around `z = 1`.** This is real-analytic
  geometric-convergence on a small branch — pre-1882 calculus
  (Newton-Mercator-Euler). No transcendence input.
- **Boundedness of `ε`** on `[0, ε_max ≈ 0.0861]`. This is a
  binade-arithmetic fact, not a transcendence fact: it follows from
  the strict concavity of `log₂(1 + m)` on `[0, 1)` and the boundary
  values. Pre-1882.
- **Finite degree `D` suffices.** This is a geometric-decay-rate
  fact about the Taylor remainder, derivable from elementary
  estimates. No transcendence input.

The *transcendence* facts about `ε` — that `ε(m)` is transcendental
at machine dyadics `m ∈ ℚ`, by Hermite-Lindemann 1882 — are used in
**Landfall §2 / §4** to establish `ε ∉ C_Aff` (the *input* to the
bridge), not in the recovery argument itself. The bridge is a
cost-bookkeeping argument; transcendence sits outside its proof.

### Step 4 — Classification under content-not-calendar

Per [memos/OLD-TIME-RELIGION.md](../memos/OLD-TIME-RELIGION.md):
- Pre-1882 calendar: clean.
- Hermite-Lindemann 1882: program's anchor; clean under
  content-not-calendar.
- Baker 1966 / Gelfond-Schneider / Thue-Siegel-Roth: hazardous;
  must be flagged.

The bridge proof uses no Baker, no Gelfond-Schneider, no
Thue-Siegel-Roth. The only transcendence content (H-L) is in the
*input* (Landfall §2 / §4), already cleared under the program's L-W
discipline.

## Verdict

**(i) Clean.** Phase-lift conservativity follows from formal-cocycle
transport (Step 1) plus the small-branch recovery argument (Step 2)
without any post-1882 transcendence input (Step 3). The pre-π promise
of the cocycle reframe survives at the analytic specialization. The
outline rewrite specified in
[fft/PHASE-DEFECT.md](PHASE-DEFECT.md) §"What gets rewritten if the
gates resolve favorably" is **authorized at full strength** by this
audit.

## Caveats and definitional sensitivities

The verdict carries two caveats that the rewrite should price in.

**Caveat 1: `C_Aff` definition.** The competitive-cost argument
(Step 2) requires `C_Aff` to contain bounded-degree polynomial
approximations of fixed-precision real functions. Under the strict
reading `C_Aff = Aff⁺(ℝ)` (literally affine compositions only),
arg-on-branch is *not* in `C_Aff`, and the bridge claim is vacuous
(or trivially false depending on interpretation). The bridge is
*contentful and true* under the natural extended reading: `C_Aff` is
the closure under the machine's primitive arithmetic operations
(`+, −, ×, ÷` on machine numbers), inside which polynomial
approximations of fixed degree live at `O(1)` cost per sample. The
rewrite should make this `C_Aff` definition explicit; the present
audit treats the natural extended reading as the intended one.

**Caveat 2: scheme-side variability.** The audit assumes the
FFT-style scheme produces `{Δ_k}` in a form from which arg-on-branch
recovery applies. Schemes that produce `Δ_k` only in some
quotient-encoding (e.g., truncated phase, modular phase representation)
require an additional unwrap step at the interface. The unwrap is
itself a small-branch operation and adds `O(1)` per sample, so the
asymptotic verdict is unchanged. Pricing the constants is downstream
work for the rewrite, not an audit blocker.

## What this audit does not do

- It does not write the full proof of phase-lift conservativity. The
  audit sketches the proof shape and classifies its inputs; the full
  proof belongs in the sequel.
- It does not check whether *some* alternative proof route to
  phase-lift conservativity might import Baker. The audit verdict is
  about the *natural* proof route via small-branch recovery; a
  proof-by-contradiction using effective Diophantine bounds would be
  a different audit and a different verdict. The natural route
  closes clean; the program is not obligated to investigate
  alternatives that would be Baker-essential.
- It does not validate any specific FFT-style scheme as
  competitively constructing `{Δ_k}`. The bridge is a conditional
  claim; whether any scheme satisfies the antecedent is a separate
  question.

## Updates to PHASE-DEFECT.md

§"Gating debt 2: L-W audit on cocycle non-compressibility" should
record:

- **Verdict (i) Clean.** Phase-lift conservativity does not import
  Baker or other post-1882 transcendence input. The natural recovery
  route (small-branch power series for `Arg`) is pre-1882 calculus.
- The H-L 1882 transcendence-at-dyadics fact remains the *input* to
  the bridge (Landfall §2 / §4), classified under content-not-calendar.
- **Caveat:** the bridge's contentfulness depends on `C_Aff` admitting
  bounded-degree polynomial approximations. The natural extended
  reading (closure under machine primitives) is intended; a strict
  Aff⁺(ℝ) reading makes the bridge vacuous.

§"What gets rewritten if the gates resolve favorably" can land
contingent on Edit 4 (canon-translation gate) closing at (a) or (b)
and Edit 5 (this audit) closing at (i) or (ii). Edit 5 closes at (i).
Whether the rewrite proceeds depends on the user's read of Edit 4's
(b) verdict — which narrows scope but does not block.

## Trust boundary

This is an audit, not a proof. The verdict (i) Clean is
defensible at the level of "no Baker dependency identified in the
natural proof route." A full proof of phase-lift conservativity
would write out the recovery argument carefully, check each step
against the chosen `C_Aff` definition, and verify that no auxiliary
lemma sneaks in transcendence content. The audit identifies the
proof shape and clears it under L-W discipline; the proof itself is
sequel content.
