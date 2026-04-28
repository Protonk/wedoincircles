# ALGEBRA-OF-DELTA

Search memo on FIRST-PROOF debt #2's algebra-of-`δ` open questions.
Companion to [memos/COASE-FRICTION-AND-SPECIALISTS.md](memos/COASE-FRICTION-AND-SPECIALISTS.md)
(methodological precedent and the seven-sub-question decomposition) and
[fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md) (candidate concrete realization
of `δ` as cost of `{Δ_k}` cocycle compression). Coase supplies vocabulary
and shape discipline, not mathematical content.

Per [memos/AGENTS.md](memos/AGENTS.md) §"Search memos": this is
provisional. Items below are working positions, not theorem material.
Promotion to FIRST-PROOF is conditional on a sub-question reducing a
named construction debt under [fft/FFT-SEARCH-PLAN.md](fft/FFT-SEARCH-PLAN.md)'s
"vocabulary may promote when it earns its way" rule.

---

## Target

Specify the *algebra* of `δ` — additivity across compositions,
amortization across uses, scale-behavior, representation-dependence,
bypass-resistance under advice and amortization, and the sign-vs-shape
methodological discipline — sharply enough that the §4.5 theorem
statement and the full impossibility *region* of FIRST-PROOF have
precise objects to quantify over.

The seven sub-questions inherit Coase 1937's mapping table
([memos/COASE-FRICTION-AND-SPECIALISTS.md](memos/COASE-FRICTION-AND-SPECIALISTS.md) §3).
Lemma B's existence claim (`δ > 0` at the boundary, bounded per-operation
effect) is enough for the narrow §4.5 theorem statement. The algebra of
`δ` is what would locate the larger impossibility *region*: which
problems, currencies, and representations sit unreachable across the
canon's `Ω(n log n)` cluster.

---

## (1) Existence of `δ` — the sign-side claim

**Working position.** `δ > 0` at the bounded/unbounded coefficient
boundary. This is Lemma B's existence-side claim
([paper/FIRST-PROOF.md](paper/FIRST-PROOF.md) Setup, §"Lemma B").
Coase precedent: p. 390, "there is a cost of using the price mechanism."

**Scaffolding.** FIRST-PROOF names `δ` and Lemma B asserts existence at
the boundary. PHASE-DEFECT offers the candidate realization
`δ ≡ cost of {Δ_k}` cocycle compression, with `{Δ_k}` forced by
`ε(m) = log₂(1+m) − m` and the formal identity
`χ_k(ψ(m)) = χ_k(m) · χ_k(ε(m))`. That formal layer is pre-analytic and
pre-1882. What is not closed is *cost*: competitive uncompressibility in
`C_FFT`, i.e. phase-lift conservativity plus the `C_Aff` definitional
move identified in [fft/PHASE-LIFT-CONSERVATIVITY-AUDIT.md](fft/PHASE-LIFT-CONSERVATIVITY-AUDIT.md).

**Status.** Closed in spirit at the formal layer; conditional at the
cost layer. Existence is not the bottleneck of this memo.

---

## (2) Bypass-resistance under advice (the regularity-guard reading)

**Working position.** Bypass-resistance against advice / oracle
constants / non-uniformity / growing-state schemes is closed *by
definition*, not by argument. The closure classes `C_FFT` and `C_Aff`
are uniform, non-growing, fixed-base-field; advice-bearing primitives
and growing-state schemes are excluded by the closure-class definition,
not refuted by separate sub-claim.

**Scaffolding.** PHASE-DEFECT names the closure-class regularity guard:
uniform, non-growing schemes only. FIRST-PROOF debt #2 separates this
advice-side guard from the substantive amortization question in (4).
Coase's "specialists" point supplies the vocabulary: reduce yes,
eliminate no. Here the programmatic analog is scope control.

**Excluded by definition.** Bailey four-step style precomputation when
functioning as advice; mixed-radix schemes with input-dependent radix
selection; cache-oblivious or growing-state schemes when the state
growth is doing the bridge work; any scheme whose constants or
representation choices grow with the instance in a way not charged by
the model. These become outside-theorem research targets, not
counterexamples.

**What closes it.** The guard must be explicit in the §1 framework, and
the canon audit in (6) must say which frameworks stay in scope. Excluded
advice-bearing schemes then become outside-theorem research targets, not
counterexamples.

**Status.** Closed by definition. Trust-boundary discipline (debt #7)
governs how the guard is cited as new sources enter; the substance is
not open here.

---

## (3) Additivity across compositions

**Working position.** *Open.* The candidate working hypothesis under
the cocycle realization is **sub-additive in the interior, super-
additive at the boundary**: composing two FFT-style schemes whose work
stays inside one regime can amortize residual structure between them
(`δ(M₂ ∘ M₁) ≤ δ(M₁) + δ(M₂)`), but composing across the bounded /
unbounded coefficient boundary cannot share residuals because each
crossing carries its own forced cocycle contribution
(`δ(M₂ ∘ M₁) ≥ δ(M₁) + δ(M₂)`). The position is speculative; nothing
yet earns it.

**Coase hook.** Long-term contracts bundle transaction costs; cocycles
need their own composition law. The analogy suggests the question, not
the answer.

**Scaffolding.** Lemma B gives a per-step drift bound, not a composition
law. PHASE-DEFECT's "factorization as a finite product of simpler
cocycle factors" would turn additivity into a concrete question about
how `{Δ_k}` factors under FFT-style composition.

**What closes it.** A precise composition law on the cocycle
realization — does composing two FFT-style schemes that each compute
some `{Δ_k}`-segment combine into a single cocycle whose compression
cost is no worse than the sum, equal to the sum, or strictly worse at
the boundary? The question is well-posed once `{Δ_k}` is the
load-bearing object. Until then it is an analogy.

**Status.** Open. Ranking: depends on the cocycle realization landing.
If PHASE-DEFECT's gates close, this becomes a tractable cocycle
calculation; otherwise it remains Coasean analogy.

---

## (4) Amortization across uses (the substantive bypass-resistance sub-claim)

**Working position.** *Open and substantive.* The candidate working
hypothesis is **non-amortizable per-sample at the boundary**: each
sample's cocycle contribution is independent in a measure-theoretic
sense (informally, `{Δ_k(m)}` carries a per-`m` residual character that
cannot be replaced by a fixed amortized constant across `m`-batches);
amortization across `N` samples reduces *recovery* cost (per
PHASE-LIFT-CONSERVATIVITY-AUDIT step 2, total recovery is `O(N)` for
`N` samples), but does not zero `δ` itself.

Separate two ledgers:

- **Recovery cost.** The cost of unwrapping `{Δ_k}` back to `ε(m)` in
  `C_Aff` after the FFT-style composition has produced it. The audit
  shows this is `O(N)` over `N` samples (Taylor expansion of `Arg(z)`
  on the small branch, degree `D = O(log precision)`, geometric
  convergence). Recovery amortizes cleanly.
- **Defect cost `δ` itself.** The cost of competitively compressing
  `{Δ_k}` inside `C_FFT`. The working position says this does *not*
  amortize across samples — each sample carries its own residual
  contribution that batching cannot eliminate.

Coase makes this plausible as vocabulary only: friction can vary with
scale without vanishing under specialization.

**Existing scaffolding.** FIRST-PROOF debt #2 and PHASE-DEFECT both
separate this from the advice-side regularity guard. The proposed proof
material is [measure/SUBSTRATE-OBSTRUCTIONS.md](measure/SUBSTRATE-OBSTRUCTIONS.md):
amortization across samples would need a substrate-compatible averaging
operation that the five substrate obstructions are meant to refuse.

**What closes it.** A per-sample lower bound on `δ` that is independent
of `N` — i.e., `δ(N samples) ≥ N · c` for some `c > 0`. The candidate
proof shape is measure-theoretic: pair the `{Δ_k}` realization with
the substrate's Haar / counting / dimension / Shannon registers and
show that no measure-preserving averaging across samples zeros the
per-sample residual. The argument is parallel to Lemma A's substrate-
side measure-theoretic refusal but at the algorithm-side amortization
question rather than at the information-distinguishing question.

**Status.** Open and substantive. First attack made in
[memos/AMORTIZATION-AT-THE-BOUNDARY.md](memos/AMORTIZATION-AT-THE-BOUNDARY.md):
Routes 1 (Haar) and 2 (counting/dimension) park as adjacent salvage;
Route 3 (L-W envelope via per-sample transcendence) is the most
promising and reduces non-amortization at the boundary to **effective
Hermite-Lindemann at `n = 1`**, the program's currently-active
substrate-side interim target. The reduction is conditional on
PHASE-DEFECT sub-debts 1 (formal-character FFT composition) and 3
(phase-lift conservativity) closing. Stuck at three named upstream
blockers; not yet a lemma.

---

## (5) Scale-behavior / asymptotics (the marginal-condition analog)

**Working position.** *Open.* The candidate working hypothesis is
**positive infimum at the boundary, independent of `N`**: there exists
`δ_∞ > 0` such that for every FFT-style scheme on inputs of size `N`,
`δ(scheme, N) ≥ δ_∞` at the bounded/unbounded coefficient boundary.
This is the strong form. A weaker form would be `δ(N) ≥ f(N)` for some
positive `f(N) → 0` slow enough that the gap to `T(P)` cannot close —
sufficient for the impossibility region but less clean.

**Coase hook.** The marginal condition asks how friction changes with
scale. Here the variables are problem size `N`, mode index `k`, and
precision.

**Scaffolding.** IMPOSSIBILITY-OUTLINE §6.2 requires zeroing `δ` at the
boundary; the asymptotic question is whether `δ` has positive infimum or
merely positive value at each finite `N`. PHASE-DEFECT §"What this would
buy" lists two candidate compressibility definitions that translate the
question into cocycle asymptotics — *low-rank approximation under
formal-character decomposition* and *`O(N log N)` evaluation on `N`
samples without paying the residual-coordinate cost*. The threshold side
is set by the canon's `Ω(n log n)` cluster (Morgenstern's bounded-
coefficient additive bound, AFW's multiplicative complexity under
rational equivalence, Ailon's restricted-model entropy potential); the
asymptotic structure of `δ` must be such that no finite-step composition
closes the gap to that scale.

**What closes it.** A scale law for `δ`. Two candidate forms:

1. **Constant infimum.** `δ ≥ δ_∞ > 0` independent of `N`. Strong;
   would close (4) automatically. Plausible under the cocycle
   realization if each mode `k` carries an independent positive
   contribution.
2. **Slow-growth lower bound.** `δ(N) ≥ f(N)` with `f(N)` slow but
   positive. Weak; sufficient if `f(N)` does not close the gap to
   `T(P)`'s scale. May be more honest if amortization (4) admits some
   sub-linear sample-sharing.

**Status.** Open. Tightly coupled to (4) — amortization and asymptotics
are two views of the same scale question. A constant-infimum result
would close both; a slow-growth result closes asymptotics but leaves
amortization with finer structure.

---

## (6) Representation-dependence (partially answered by seam-narrowing)

**Working position.** **`δ` is born at the floating-point additive /
log-binade seam.** Representations that do not cross that seam at
primitive-operation level do not carry `δ`, and FFT-style methods
operating in such representations are *out-of-scope* of the impossibility
theorem rather than counterexamples to it. The theorem's scope is
seam-orthogonally narrowed.

**Existing scaffolding.**

- [fft/SCHOENHAGE-STRASSEN-COCYCLE-TRANSLATION.md](fft/SCHOENHAGE-STRASSEN-COCYCLE-TRANSLATION.md)
  is the first canon test case: SS 1971 has two methods, both
  out-of-scope but for different reasons (Method 1 uses precomputed
  fixed-point quantizations, no per-number binade structure; Method 2
  uses Fermat-ring modular arithmetic, no mantissa coordinate). Verdict:
  **(b) Conditional translation** — in-scope iff the algorithm crosses
  the floating-point binade seam at its primitive-operation level.
- [fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md) §"Gating debt 1" frames
  the alignment claim at the group-theoretic level: additive vs
  log-binade quotient cut, mult/add complexity cut, and character
  structure may align even where a particular analytic realization fails.
- [memos/COASE-FRICTION-AND-SPECIALISTS.md](memos/COASE-FRICTION-AND-SPECIALISTS.md)
  §3 row "Representation-dependence": Coasean answer is "friction
  varies across transaction types," which the seam-narrowing reading
  inherits.

**What closes it.** A literature-audit verdict on each canon framework
(Morgenstern, Winograd, AFW; SS already done) under the cocycle lens:
does the framework cross the floating-point seam at primitive-operation
level? Each verdict either keeps the framework in scope (and the
theorem applies) or narrows the scope away from it (and the framework
becomes a research target rather than a counterexample). The audit is
mechanical once the lens is fixed.

**Status.** Partially answered. SS done; three canon frameworks owed.
The closing move is verdict-by-verdict, not a single lemma.

---

## (7) Sign vs shape (the methodological wedge; programmatic)

**Working position.** Programmatic, closed in spirit. Lemma B's
sign-side claim (`δ > 0`, per-operation bounded effect) closes the
§4.5 theorem statement. The shape-side claims (Bridge, Separation
transport, Native drift bound) close the impossibility *region*. The
algebra of `δ` feeds shape; the existence of `δ` feeds sign.

The layering is named in [paper/FIRST-PROOF.md](paper/FIRST-PROOF.md)
debt #2: Lemma B's existence-side claim alone closes only the §4.5
theorem statement; the algebra of `δ` closes the impossibility region.
This memo is the algebra-side bookkeeping that wedge implies.

**Coase hook.** The p. 390 sign claim and p. 396 shape question are the
methodological wedge; no content transfers.

**What closes it.** Already closed at the methodological layer. This
memo only checks that (1)–(6) respect the wedge: (1) is sign; (2) is a
scope guard; (3)–(6) are shape.

**Status.** Closed at the methodological layer. The wedge governs the
memo, not the other way around.

---

## Cross-cutting positions

Two structural observations that fall out of the above:

**(α) The cocycle realization is the load-bearing handle.** Five of the
seven sub-questions ((1) cost layer, (3), (4), (5), and partially (6))
acquire concrete content under the candidate `δ ≡ cost of {Δ_k}`
realization. Without it, the algebra of `δ` is largely Coasean analogy.
With it (and PHASE-DEFECT's gates closing), the algebra acquires a
mathematical object to operate on. The memo's productivity is therefore
gated on PHASE-DEFECT's promotion path.

**(β) The substantive open work clusters around amortization and
asymptotics ((4) and (5)).** Existence is closed in spirit; bypass under
advice and sign-vs-shape are programmatic; representation-dependence
narrows by audit; additivity is open but tractable once the cocycle
lands. Amortization and asymptotics carry the algebraic-structure
weight — they are what determines the impossibility region's *boundary*,
which is the difference between the §4.5 theorem and the full theorem
the program promises.

First attack on (4) made in
[memos/AMORTIZATION-AT-THE-BOUNDARY.md](memos/AMORTIZATION-AT-THE-BOUNDARY.md).
Verdict: not a lemma yet, but a clean reduction of `(4)` (and `(5)`-strong
when bundled) to effective Hermite-Lindemann at `n = 1` — the program's
substrate-side interim target — via per-sample transcendence in the
L-W envelope. The reduction is conditional on PHASE-DEFECT sub-debts 1
and 3 closing. The downstream-to-upstream signal: H-L `n = 1`, if it
lands, carries algorithm-side payoff (closes `(4)`) at no extra cost
beyond what the substrate-side work already buys.

The natural next move follows from the AMORTIZATION verdict: push
PHASE-DEFECT sub-debt 1 (operational compressibility) toward closure,
since it is the most upstream of the three blockers; in parallel, audit
whether the program's existing effective H-L work delivers a per-sample
distinguishability bound of the form Route 3 needs.

---

## Adjacent anchors

- [memos/COASE-FRICTION-AND-SPECIALISTS.md](memos/COASE-FRICTION-AND-SPECIALISTS.md):
  seven-question map and method precedent.
- [fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md) and
  [fft/PHASE-LIFT-CONSERVATIVITY-AUDIT.md](fft/PHASE-LIFT-CONSERVATIVITY-AUDIT.md):
  candidate cocycle realization, gates, and audit boundary.
- [fft/SCHOENHAGE-STRASSEN-COCYCLE-TRANSLATION.md](fft/SCHOENHAGE-STRASSEN-COCYCLE-TRANSLATION.md):
  first representation-dependence test case.
- [fft/FFT-SEARCH-PLAN.md](fft/FFT-SEARCH-PLAN.md):
  strategy-family and search/execution-cost framing.
- [paper/FIRST-PROOF.md](paper/FIRST-PROOF.md),
  [measure/SUBSTRATE-OBSTRUCTIONS.md](measure/SUBSTRATE-OBSTRUCTIONS.md),
  [memos/NATIVE-F-MINIMAL-DEFINITION.md](memos/NATIVE-F-MINIMAL-DEFINITION.md):
  debt #2, substrate-side refusal, and algebraic closure companion.

---

## What this memo is not

- **Not a proof.** None of the seven sub-questions is closed at the
  theorem level here.
- **Not authorization to rewrite [paper/FIRST-PROOF.md](paper/FIRST-PROOF.md)
  or [paper/IMPOSSIBILITY-OUTLINE.md](paper/IMPOSSIBILITY-OUTLINE.md).**
  Promotion requires a named sub-question to earn its way.
- **Not a commitment to the cocycle realization.** PHASE-DEFECT is
  parked; this memo notes that the cocycle realization gives the
  algebra of `δ` concrete handles where it has them, without committing
  to that realization being the right one.
- **Not a closure of the impossibility region.** The region closes when
  (4) and (5) close, conditional on the others. The memo states
  working positions on (4) and (5); it does not earn them.

---

## Exit criteria

The memo freezes when (1) promotes from formal-cocycle existence to cost,
(2) migrates into the §1 regularity guard, (3)–(5) become lemmas, scope
narrowings, or precise conjectures, (6) has a verdict for each canon
framework, and (7) still checks out. Closed parts can then promote to
FIRST-PROOF Setup definitions; unresolved parts become sharper debt #2
sub-debts.

---

## Trust boundary

The seven-sub-question decomposition and the Coase mapping are
inherited from [memos/COASE-FRICTION-AND-SPECIALISTS.md](memos/COASE-FRICTION-AND-SPECIALISTS.md);
trust-boundary discipline applies. The cocycle realization is inherited
from [fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md), whose gates are not yet
closed. This memo adds no external citations; it organizes existing
program material under FIRST-PROOF debt #2.

The working positions in (3), (4), and (5) are the memo's
contributions; each is named as speculative pending earned mathematical
content. None should be cited as an established program position.
