# AMORTIZATION-AT-THE-BOUNDARY

Follow-on memo from [memos/ALGEBRA-OF-DELTA.md](memos/ALGEBRA-OF-DELTA.md)
§(4) primary attack: the conjecture that `δ` is non-amortizable per-sample
at the bounded/unbounded coefficient boundary, in the strong form that
also closes §(5)'s asymptotic question. Conditional on the cocycle
realization of [fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md).

The deliverable shape was named in advance: *either* a candidate lemma,
*or* a clean statement of where the argument gets stuck and what
cocycle-side structure it needs. The honest verdict is the second:
the most promising route reduces non-amortization to **effective
Hermite-Lindemann at `n = 1`**, which is the program's currently-active
substrate-side interim target. That reduction is itself the finding —
amortization-failure at the boundary is not adjacent to the H-L `n = 1`
work; it depends on it. That changes how the interim target is scoped.

Per [memos/AGENTS.md](memos/AGENTS.md) §"Search memos": this is
provisional and append-only.

---

## The conjecture

**Strong amortization claim (`(4)+(5)`-bundled).** There exists `c > 0`,
independent of `N`, such that for every FFT-style scheme `S` producing
the cocycle family `{Δ_k(m_i)}_{i = 1..N}` at the bounded/unbounded
coefficient boundary, the cost `C_S(N)` satisfies

```text
C_S(N)  ≥  c · N.
```

In particular, per-sample cost has positive infimum `δ_∞ ≥ c > 0` and
amortization across `N` samples does not vanish as `N → ∞`.

The conjecture is single-statement; it bundles `(4)` (per-sample
non-amortization) with `(5)`-strong (constant infimum) per the
ALGEBRA-OF-DELTA cross-cutting position (β). Failure modes split it
back along the `(4)` / `(5)` axis.

---

## Setup

Inputs are `m_1, ..., m_N ∈ [0, 1)` (mantissa coordinates at machine
dyadics). The cocycle realization
([fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md)) gives

```text
ε(m) = log₂(1+m) − m,
Δ_k(m) = e^{2πik · ε(m)}     (analytic specialization).
```

`δ` is the cost of competitively constructing `{Δ_k(m_i)}_{i,k}` inside
`C_FFT`. The PHASE-LIFT-CONSERVATIVITY-AUDIT gives the recovery side
(`{Δ_k} → ε`) as `O(N)` over `N` samples — that's *recovery cost*, which
amortizes cleanly. The amortization question is about *forward
construction cost*, which the audit does not address.

The cost model is the canon's (per IMPOSSIBILITY-OUTLINE §1.2 / §1.3):
multiplicative cost `μ` and additive cost `α` under the canon's standard
accounting, with the regularity guard of PHASE-DEFECT excluding
advice-bearing and growing-state schemes.

---

## Three candidate routes

### Route 1 — Haar averaging on `T = ℝ/ℤ`

**Idea.** The substrate's natural averaging operation is Haar on `T`.
If the per-sample residual `Δ_k(m_i)` could be replaced by its Haar
mean across samples, amortization would succeed. The substrate refuses
this if the Haar mean is structurally inaccessible to FFT-style
composition.

**Where it stalls.** Amortization is not averaging. A scheme that
amortizes does not need to *project onto* the Haar mean; it needs to
*share computational work* across samples. Haar-refusal would obstruct
average-case-statistical compression but not worst-case-algorithmic
compression. Haar shows the wrong axis of refusal for `(4)`.

**Salvage.** Haar refusal still does work for `(5)`-weak: it shows that
no statistical averaging across samples zeros the per-sample residual,
which forecloses one class of asymptotic-slow-growth schemes. That
is `(5)`-adjacent rather than `(4)`-load-bearing. Parked.

### Route 2 — Counting / dimension via cyclotomic-ladder unboundedness

**Idea.** The cocycle family `{Δ_k}_k` is infinite-dimensional in `k`:
as `k` ranges over `ℤ`, the harmonics fill out distinct modes on `T`.
FFT-style closure has bounded depth (per
[memos/NATIVE-F-MINIMAL-DEFINITION.md](memos/NATIVE-F-MINIMAL-DEFINITION.md)
algebraic-side companion: `[K_n^+ : ℚ] = φ(n)/2` grows; affine closure
is flat). Therefore per-sample cost across `K` modes is at least `Ω(K)`.

**Where it stalls.** Counting bounds the *mode-axis* dimension, not the
*sample-axis* amortization. The conjecture is in `N` (samples), not in
`K` (modes). With `K` fixed and `N` varying, the counting argument is
silent.

**Salvage.** The counting argument transports to the orthogonal
question: per-mode cost across samples. If you fix `N` and vary `K`,
counting gives a per-mode positive infimum. That's a different
sub-question than `(4)`/`(5)` (modes are independent of samples in the
cocycle realization), but it's worth recording: counting gives the
mode-axis half of any future `Ω(N · K)` joint bound.

### Route 3 — L-W envelope via per-sample transcendence

**Idea.** By Hermite-Lindemann 1882, `ε(m) = log₂(1+m) − m` is
transcendental at machine dyadics `m ∈ ℚ`. Consequently the cocycle
values `{Δ_k(m_i)}_k` are transcendentally distinct across `m_i`. Any
FFT-style scheme producing all `N` cocycle values must distinguish
them, and the L-W envelope says the cost of distinguishing `N`
transcendentally-distinct values has a positive per-sample lower bound.

This is the most promising route because the per-sample lower bound
lives directly on the sample axis, where the conjecture lives.

**Where it stalls.** Hermite-Lindemann is an *existence* statement
(`ε(m_i)` is transcendental). The amortization claim needs an
*effective* statement: a quantitative per-sample bound on the bits of
work required to distinguish two transcendentally-distinct values at
machine precision. Without effectivity, "transcendentally distinct" is
compatible with arbitrarily-cheap distinguishability in the cost model.

The natural quantitative input is **effective Hermite-Lindemann at
`n = 1`** — the program's currently-active substrate-side interim
target. With effective H-L `n = 1` in hand, each sample's cocycle value
admits a per-sample distinguishability lower bound of the form
`f(precision)` for some explicit `f`, and the total cost is bounded
below by `N · f(precision)`. Choosing precision as a fixed model
parameter makes `f(precision)` the constant `c` in the conjecture.

---

## What this is — the reduction

The cleanest of the three candidate routes (Route 3) reduces

```text
non-amortization of δ at the boundary  (algebra-of-δ sub-question (4))
```

to

```text
effective Hermite-Lindemann at n = 1   (program interim target).
```

That reduction is the memo's contribution. It says: amortization-failure
at the boundary is not a separate piece of work the program owes; it is
a *downstream consequence* of the H-L `n = 1` target landing, modulo
the cocycle realization of PHASE-DEFECT. The reduction sharpens the
load-bearing role of the interim target — H-L `n = 1` is not just
substrate-side cleanup; it is what makes the impossibility *region*
(the difference between the §4.5 statement and the full FIRST-PROOF
theorem) reachable.

This is downstream-to-upstream signal in the sense the briefing
described: working on `(4)` reveals that the program's existing direction
on the substrate side carries algorithm-side payoff at no extra cost.

---

## What this is not — the stuck point

The reduction is not a closed lemma. The argument needs three pieces
of content not currently in hand:

1. **Effective H-L `n = 1`** with a quantitative per-value distinguishability
   bound at machine dyadics. Form spec'd in
   [memos/EFFECTIVE-HL-N1-COST-FORM.md](memos/EFFECTIVE-HL-N1-COST-FORM.md):
   `cost_op ≥ c · p` per sample at precision `p`, for any scheme in
   extended `C_Aff` under the regularity guard. Parked as program
   interim target; not delivered here.
2. ~~PHASE-DEFECT sub-debt 1 (formal-character FFT composition).~~
   **Discharged** in [fft/COCYCLE-COMPOSITION-LAW.md](fft/COCYCLE-COMPOSITION-LAW.md):
   verdict is partial-yes, with the cocycle-product composition law as
   the formal-character skeleton and the cost-norm choice as the
   load-bearing analytic definitional move. Recommendation: operational
   cost-norm. With this, `C_S(N)` is the operational-cost-norm of the
   cocycle product across `S`'s composition path — well-typed.
3. **Phase-lift conservativity** (PHASE-DEFECT sub-debt 3) closed with
   the `C_Aff` definitional move per
   [fft/PHASE-LIFT-CONSERVATIVITY-AUDIT.md](fft/PHASE-LIFT-CONSERVATIVITY-AUDIT.md),
   so the cocycle is the load-bearing object on the FFT side. Audit
   verdict: clean-conditional, refined per
   [fft/LANDFALL-EXTENDED-CAFF-TRANSFER.md](fft/LANDFALL-EXTENDED-CAFF-TRANSFER.md):
   under fixed precision the Landfall §2 transfer fails and the bridge
   delivers no impossibility; under variable precision plus effective
   H-L `n = 1`, the §4 replacement obstruction bites and the bridge
   lands. The conditional is now on (a) variable-precision cost model
   and (b) effective H-L `n = 1` in cost-norm-compatible form. The
   second condition is *the same input* as (1) above — convergence.

The argument's structure is: per-sample distinguishability bound
(needs (1)), against forward construction cost in `C_FFT` (now typed
via (2)'s discharge — `C_S(N)` = operational-cost-norm of the cocycle
product across `S`'s path), with (3) keeping the cocycle load-bearing
on the FFT side. With all three, the bound is `C_S(N) ≥ c · N` and
the conjecture lands. Without (1) or (3), the route stalls at a
precise place.

---

## Cocycle-side structure required

PHASE-DEFECT sub-debt 1 was the most upstream of the three blockers.
[fft/COCYCLE-COMPOSITION-LAW.md](fft/COCYCLE-COMPOSITION-LAW.md)
discharges it: the amortization argument's required precise statement —

> For an FFT-style scheme `S` and cocycle family `{Δ_k(m_i)}_{i,k}`,
> the cost `C_S(N)` is the operational cost-norm on the cocycle
> product `∏ Δ_k^O` across `S`'s composition path under the canon's
> standard composability.

— is now in hand, conditional on the operational cost-norm choice
(the load-bearing analytic definitional move that memo identifies).
Route 3's per-sample lower bound now has a target object.

The remaining cocycle-side work is the form Route 3 needs from
effective H-L `n = 1`: the per-sample distinguishability bound must
contribute to the operational cost-norm in a way that does not cancel
across composition. This sharpens the demand on the substrate-side
work: the H-L bound must be in *cost-norm-compatible* form, not just
in distinguishability-existence form.

This is also a downstream-to-upstream demand on PHASE-DEFECT: the
memo identifies operational compressibility as the load-bearing
choice between PHASE-DEFECT's primary and secondary candidate
definitions. The secondary candidates (low-rank, factorization)
underdetermine the cost model the amortization argument needs.

---

## Failure modes

- **Route 3 fails because effective H-L `n = 1` does not yield a
  per-sample bound of the right form.** Then `(4)` does not reduce to
  H-L `n = 1`; the program owes a separate per-sample lower bound, and
  this memo's reduction-claim retracts. Consequence: H-L `n = 1` keeps
  its substrate-side role but loses its load-bearing role for the
  impossibility region.
- **PHASE-DEFECT sub-debts 1 / 3 do not close.** Then the cocycle
  realization is not the load-bearing object, and `(4)` migrates to
  whatever realization replaces it. The reduction in this memo
  transfers as conjecture-shape (per-sample distinguishability against
  forward construction cost), not as content.
- **Some FFT-style scheme actually amortizes `δ`.** The conjecture is
  false. The §4.5 theorem statement still stands; the impossibility
  *region* retreats. Honest finding; rewrite, don't paper over.
- **Routes 1 and 2 turn out to be load-bearing in some way Route 3
  misses.** Then the parked salvage-claims (Haar for `(5)`-weak,
  counting for the mode-axis half) get reactivated. Track in
  ALGEBRA-OF-DELTA.

---

## What the memo positions for next

Three concrete next moves, in priority order:

1. **Push PHASE-DEFECT sub-debt 1 toward closure.** The amortization
   reduction needs operational compressibility as the cost meaning of
   `δ`. This is the most upstream of the three blockers.
2. **Audit the program's existing effective H-L work** for whether
   the per-sample distinguishability bound it would deliver matches
   the form Route 3 needs. If yes, the reduction is real; if no, the
   program owes a parallel per-sample lower bound.
3. **Re-attack `(3)` additivity** once `(4)`'s composition law is
   provisionally typed via the operational compressibility choice.
   Currently `(3)` is downstream-conditional on `(4)` having a
   composition law; this memo provides one (operational
   compressibility under FFT-style composition).

`(6)` representation-dependence audits remain parallel and continue
as the briefing described.

---

## Adjacent anchors

- [memos/ALGEBRA-OF-DELTA.md](memos/ALGEBRA-OF-DELTA.md) §(4), §(5),
  cross-cutting (β) — the parent memo this follows from.
- [fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md) — cocycle realization;
  sub-debts 1 and 3 are the upstream blockers.
- [fft/PHASE-LIFT-CONSERVATIVITY-AUDIT.md](fft/PHASE-LIFT-CONSERVATIVITY-AUDIT.md)
  — recovery-cost vs forward-construction-cost separation; the audit
  handles recovery; this memo handles forward construction.
- [paper/MEASURE-THEORETIC-OBSTRUCTIONS.md](paper/MEASURE-THEORETIC-OBSTRUCTIONS.md)
  §5.1, §5.4, §5.5 — substrate-side measure-theoretic registers; the
  three candidate routes draw on Haar, counting, and L-W respectively.
- [memos/NATIVE-F-MINIMAL-DEFINITION.md](memos/NATIVE-F-MINIMAL-DEFINITION.md)
  — algebraic-side closure-mismatch companion; load-bearing for
  Route 2's mode-axis dimensionality argument.
- [memos/COASE-FRICTION-AND-SPECIALISTS.md](memos/COASE-FRICTION-AND-SPECIALISTS.md)
  §3 row "Amortization across uses" — methodological precedent;
  Coase's "friction-per-transaction varies with scale" supplies the
  vocabulary, not the content.
- [memos/LINDEMANN-BRIEF.md](memos/LINDEMANN-BRIEF.md) — H-L 1882
  base case; effective version is the program interim target.
- [memos/FORTNOW-KOLMOGOROV-BRIEF.md](memos/FORTNOW-KOLMOGOROV-BRIEF.md)
  — universal dominance / Kolmogorov-style lower-bound machinery
  adjacent to Route 3's per-sample distinguishability formulation.

---

## What this memo is not

- **Not a closed lemma.** The conjecture is stated; the most promising
  route is identified; the stuck point is named. None of that is a
  proof.
- **Not authorization to promote `(4)`/`(5)` in
  [paper/FIRST-PROOF.md](paper/FIRST-PROOF.md).** Promotion requires
  the three blockers above closing, in order.
- **Not a redirection of the program's H-L `n = 1` interim target.**
  The target's substrate-side role is unchanged; this memo identifies
  an *additional* algorithm-side role that target carries if it
  lands. The substrate-side work proceeds on its own merits.
- **Not a verdict on Routes 1 and 2.** Both are parked with salvage
  notes. Either may turn out to do work this memo did not see.

---

## Exit criteria

This memo freezes when:

- The reduction to effective H-L `n = 1` is either confirmed (with
  the per-sample bound delivered in the form Route 3 needs) or
  retracted (with the failure mode that retracts it documented);
- PHASE-DEFECT sub-debt 1 closes (operational compressibility typed)
  or fails (and the cocycle realization migrates);
- The conjecture either lands as a lemma, scope-narrows to a precise
  conditional statement, or fails (with the smarter-FFT amortizing
  scheme exhibited).

Until then, append-only.

---

## Trust boundary

The reduction in this memo is conditional on:

- The cocycle realization of PHASE-DEFECT (parked, exploratory).
- Effective H-L `n = 1` (program interim target, not delivered).
- Phase-lift conservativity (audit clean-conditional).

The Coase precedent supplies vocabulary only (per
COASE-FRICTION-AND-SPECIALISTS trust boundary). Hermite-Lindemann 1882
is L-W safe under content-not-calendar. No new external sources are
introduced; the memo organizes existing program material.

The strong amortization claim is named as conjecture pending earned
content. It should not be cited as an established program position.
