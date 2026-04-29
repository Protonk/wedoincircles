# LANDFALL-EXTENDED-CAFF-TRANSFER

Re-derivation audit on the deferred question from
[fft/PHASE-LIFT-CONSERVATIVITY-AUDIT.md](fft/PHASE-LIFT-CONSERVATIVITY-AUDIT.md):
does the Landfall §2 obstruction (`λ ∉ Aff⁺(ℝ)`-closure; equivalently
`ε ∉ Aff⁺(ℝ)`) transfer to the extended `C_Aff` the audit's bridge
contentfulness requires (`C_Aff` = closure under machine arithmetic
primitives `+, −, ×, ÷` with bounded-degree polynomial approximations
of fixed-precision real functions at `O(1)` per sample)?

**Verdict (preview): the §2 statement does not transfer at the
cost-level under fixed precision.** Polynomial Taylor approximation of
`log₂(1+m)` at fixed precision lives in extended `C_Aff` at `O(1)`
per sample, so `ε ∈ extended C_Aff` competitively. This vacates the
source-side hardness the bridge's contrapositive needs. The bridge
under extended `C_Aff` at fixed precision delivers no FFT-side
impossibility.

**Replacement (positive):** Landfall §4's transcendence-at-dyadics
fact, combined with **effective Hermite-Lindemann at `n = 1`** (program
substrate-side interim target) and a **variable-precision** cost
model, supplies a *replacement* source-side obstruction: `ε` is
`Ω(N log N)` in extended `C_Aff` at precision `∝ log N`, by per-sample
distinguishability summed across `N` samples. Under this reading the
bridge contrapositive bites and the impossibility lands.

The §2 statement falls; the §4 + effective-H-L route preserves the
spirit. Both threads (this memo and
[memos/AMORTIZATION-AT-THE-BOUNDARY.md](memos/AMORTIZATION-AT-THE-BOUNDARY.md))
converge on effective H-L `n = 1` as the load-bearing substrate-side
input.

Per [memos/AGENTS.md](memos/AGENTS.md): exploratory; no new external
sources; sharpens the audit's deferred question.

---

## The deferred question

[fft/PHASE-LIFT-CONSERVATIVITY-AUDIT.md](fft/PHASE-LIFT-CONSERVATIVITY-AUDIT.md)
§"Definitional condition" recorded the deferral verbatim:

> The Landfall §2 obstruction is stated against `Aff⁺(ℝ)`; transferring
> it to the natural extended `C_Aff` requires re-deriving the
> obstruction in the new closure class — or arguing that the
> obstruction transfers automatically. Neither is checked by this
> audit.
>
> The rewrite must make the `C_Aff` definition explicit and
> re-establish the Landfall transfer in that definition.

This memo does that re-derivation. The verdict resolves the audit's
**(ii) Clean-conditional** promotion verdict in the negative direction
under fixed precision, with the positive direction surviving via a
replacement obstruction at variable precision.

---

## Landfall §2's argument, restated

Verbatim from the source ([sources/landfall.pdf](sources/landfall.pdf),
p. 4):

> The machine's operations on the mantissa are affine within a binade:
> additions translate by a constant, multiplications scale by a
> constant. ... These generate the group `Aff⁺(ℝ)` of maps
> `x ↦ ax + b` with `a > 0`. The coordinate change `ψ(m) = log₂(1 + m)`
> is not affine — it is logarithmic. The composition of affine maps is
> affine: `Aff⁺(ℝ)` is a group. No finite composition of the machine's
> operations produces `ψ`.

Three lines:

1. *Generators:* additive (translate), multiplicative (scale).
2. *Closure:* `Aff⁺(ℝ) = {x ↦ ax + b : a > 0}`, a group under
   composition.
3. *Target:* `λ(m) = log₂(1+m)` is not of the form `am + b` for any
   `a, b`. Therefore `λ ∉ Aff⁺(ℝ)`. Equivalently `ε = λ − m ∉ Aff⁺(ℝ)`
   since `m` is affine.

The argument is structurally trivial: closure under affine composition
stays affine; log isn't affine.

The argument's *strength* is its weakness for the audit's purposes:
it's a *closure-class* argument at a very narrow class. As soon as the
class is enriched — even mildly — the argument no longer applies and
must be re-run from scratch.

---

## Two readings of "ε in C_Aff"

The audit's extended `C_Aff` is the closure of `+, −, ×, ÷` on machine
numbers, with bounded-degree polynomial approximations of fixed-precision
real functions at `O(1)` cost per sample. Under this definition,
"membership of `ε`" splits into two readings:

### Reading (E) — Exact membership

A scheme `S ∈ C_Aff` produces `S(m) = ε(m)` exactly for each `m` in
the domain.

Under either strict `Aff⁺(ℝ)` or extended `C_Aff`, exact membership
fails: at machine dyadics `m = k/2^p`, `ε(m)` is transcendental
(Landfall §4, via Hermite-Lindemann + Gelfond-Schneider). Polynomial
or rational expressions in `+, −, ×, ÷` at machine-number inputs
produce algebraic values; transcendentals cannot equal algebraics.
**Transfer holds trivially under (E).**

But (E) is not the audit's reading. The audit explicitly works at
machine precision, with polynomial approximations, not exact equality.
The (E) verdict is a sanity check, not the answer the audit needed.

### Reading (P) — Membership at machine precision

A scheme `S ∈ C_Aff` produces `S(m)` such that `|S(m) − ε(m)| ≤ 2^{-p}`
for some fixed precision `p`. Equivalently, `S(m)` is the machine-
precision approximation of `ε(m)`.

This is the audit's reading. Under it, polynomial Taylor approximation
of `log₂(1+m)` around `m = 0` gives:

```text
ε(m) ≈ m(1/ln 2 − 1) − m²/(2 ln 2) + m³/(3 ln 2) − ...
```

A degree-`D` truncation with `D = O(p)` (geometric convergence on
`m ∈ [0, 1)`) approximates `ε(m)` to precision `2^{-p}`. The
truncated polynomial — with machine-precision-approximated coefficients
`1/ln 2`, etc. — is in extended `C_Aff`: it uses only `+, ×` on
machine numbers and a finite set of precomputed constants.

**Per-sample evaluation cost: `O(D) = O(p)`.** At fixed precision `p`
(machine precision), this is `O(1)` in `N`. Total cost for `N`
samples: `O(N)`.

**Therefore `ε ∈ extended C_Aff` competitively at fixed precision.**
The Landfall §2 transfer FAILS under reading (P) at fixed precision.

*Cost-model uniformity, not table-permissive vs strict.* An earlier
draft of this footnote drew a permissive-vs-strict line on
range-reduction tables (allow them or forbid them?). That axis is
wrong: in big-O, "tables yes / no" collapses under any cost model
that charges for stored bits and native operations at the same
precision granularity. A scheme that uses a table pays for the
table; a scheme that recomputes pays for the recomputation; the
asymptotic accounting is the same. "Preloading arithmetic into
microcode doesn't put TSP in a different complexity class" — same
argument applies here.

The substantive question is whether the cost model is **uniform**.
Under non-uniform charging — storage free, or charged at a
different precision granularity than operations — Bailey-style
tables can purchase savings the cost model fails to record. Under
uniform charging they cannot. PHASE-DEFECT's regularity guard
expresses this directly: "any scheme whose constants or
representation choices grow with the instance in a way *not charged
by the model*." Emphasis on the charging.

Under uniform charging the verdict is clean: `ε ∈ extended C_Aff`
at fixed precision `p` costs `O(p)` per sample by total cost (Taylor
evaluation, or any equivalent) — verdict "§2 transfer fails" stands
unconditionally on the cost-model side; problems sneak in only if
the cost model itself is non-uniform.

Debt #9 therefore reads: **adopt a uniform-charge cost model, and
re-read the canon's `Ω(n log n)` cluster (Morgenstern, AFW, Ailon)
under it**. Most canon thresholds were proved under one specific
allocation between storage and operations; the variable-precision
re-read needs to verify each threshold survives uniform charging.

The information-theoretic basis (per
[memos/EFFECTIVE-HL-N1-COST-FORM.md](memos/EFFECTIVE-HL-N1-COST-FORM.md)
§"Information-theoretic basis"): bits of `ε(m)` carry no
compressible structure for a transcendental target — knowledge at
precision `P` is asymptotically zero-information about the bit at
`P + 1`; conditional probability of any further bit is `1/2`. Under
uniform charging, this forces each new bit to cost `Ω(1)`
regardless of scheme architecture; the `Ω(p)` per-sample bound
aggregates to `Ω(N log N)` at variable precision, and the bridge
contrapositive bites.

---

## What this means for the bridge

The bridge as stated in
[fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md) §"Character reflection
barrier":

> If the FFT-style composition closure `C_FFT` contains the cocycle
> family `{Δ_k(m) := χ_k(ε(m))}`, then the underlying additive defect
> `ε(m)` lies in the affine closure `C_Aff`.

Specialized to costs by the audit ("competitively constructs"):

> If `C_FFT` competitively constructs `{Δ_k}`, then `C_Aff`
> competitively constructs `ε`.

The contrapositive is what the impossibility theorem uses:

```text
(¬ε ∈_competitive C_Aff)  ⟹  (¬{Δ_k} ∈_competitive C_FFT).
```

For the impossibility to bite, we need `ε` to be *hard* in `C_Aff` —
specifically, harder than the FFT threshold `T(P)`.

Under the (E) reading: hardness is infinite (no exact construction
possible). Contrapositive bites trivially: `{Δ_k}` not exactly in
`C_FFT`. But `{Δ_k}` are themselves transcendental values; no exact
scheme produces them. Trivially-true conclusion, no useful FFT-side
information.

Under the (P) reading at fixed precision: `ε` is `O(N)` in extended
`C_Aff`. The contrapositive *does not bite*. The bridge under
extended `C_Aff` at fixed precision delivers no FFT-side impossibility.

This is the substantive negative finding. The audit's
**Clean-conditional** verdict was conservative; resolving the
conditional in the natural direction (extended `C_Aff` at fixed
precision) renders the bridge impotent for the impossibility's
intended use.

---

## The replacement: §4 + effective H-L at variable precision

The §2 statement falls. The proof template's *spirit* — that `ε`
carries an irreducible substrate-level obstruction — survives via a
different argument.

**Source content.** Landfall §4 establishes that `ε(m)` is
transcendental at every interior machine dyadic `m = k/2^p`. The
proof uses Hermite-Lindemann 1882 + Gelfond-Schneider; it does not
go through closure-class reasoning. This is a *distinguishability*
fact about `ε` at machine-dyadic inputs, not a *closure-class* fact.

**Cost transport via effective H-L.** Given an effective H-L `n = 1`
bound in the form specified at
[memos/EFFECTIVE-HL-N1-COST-FORM.md](memos/EFFECTIVE-HL-N1-COST-FORM.md)
(`cost_op ≥ c · p` per sample at precision `p`, for any scheme in
extended `C_Aff` under the regularity guard) — *the program's
currently-active substrate-side interim target* — the transcendence-
at-dyadics fact upgrades to a per-sample lower bound that aggregates
correctly under variable precision.

**Aggregation across `N` samples.** Under variable precision
`p ∝ log N`, the per-sample cost is `Ω(log N)` operations (per the
spec's `cost_op ≥ c · p` form). Over `N` samples, total cost is
`Ω(N log N)` operations. Any scheme in extended `C_Aff` producing
`ε` on `N` samples at precision `log N` must therefore spend at
least `Ω(N log N)` operations.

**Result.** Under variable precision `∝ log N`, `ε` is `Ω(N log N)`
in extended `C_Aff`. This is the *cost-level source-side obstruction*
the bridge needs.

**The bridge contrapositive then bites:**

```text
ε ∈_competitive C_Aff  requires  Ω(N log N)
   ⟹  {Δ_k} ∈_competitive C_FFT  requires  Ω(N log N)
   ⟹  no FFT-style descent below T(P) = Ω(N log N).
```

The impossibility lands.

---

## What survives, what falls

| Object | Strict `Aff⁺(ℝ)` | Extended `C_Aff`, fixed precision | Extended `C_Aff`, variable precision + effective H-L |
|---|---|---|---|
| `ε ∈ C_Aff` (E, exact) | No (transcendental) | No (transcendental) | No (transcendental) |
| `ε ∈ C_Aff` (P, at precision) | No (not affine) | **Yes, `O(N)` cheap** | No (`Ω(N log N)` by H-L) |
| Bridge contentful? | Vacuous (recovery impossible in `Aff⁺(ℝ)`) | Yes (recovery via Taylor) | Yes (recovery via Taylor) |
| Contrapositive bites? | Trivially (everything fails exactly) | **No** | Yes (`ε` hard) |
| Useful impossibility delivered? | Trivial | **No** | **Yes** |

The middle column is the audit's resolution and is non-deliverable.
The right column is the replacement — and it depends on effective H-L
`n = 1` plus a variable-precision cost model.

---

## Why §2 fails to transfer (structural reading)

Landfall §2's argument is *closure-class non-membership at exact level*.
It works because `Aff⁺(ℝ)` is small enough that an exact non-affineness
fact (log isn't affine) suffices.

Extended `C_Aff` is large enough to contain bounded-degree polynomial
approximations of any fixed-precision real-analytic function, including
`log`. The non-affineness of `log` is no longer a non-membership
witness in this larger class — it is just a property of the exact
function that the *approximations* don't share.

The deeper Landfall content does survive but at a different level:
- **§1** (polynomial wall): `ε` is not exactly a polynomial of any
  finite degree. Survives in any `C_Aff` that requires exactness;
  doesn't survive at fixed-precision approximation.
- **§4** (transcendence-at-dyadics): `ε(m)` is transcendental at
  machine dyadics. Survives in any `C_Aff` (algebraic ≠ transcendental).
  Cost-quantitative version requires effective H-L.
- **§6** (no invariant measure for aggregation): substrate-side, not
  closure-class. Doesn't go through `C_Aff` at all; aggregates against
  the binary tiling. Different proof route.

The §2 closure-class route is fragile; the §4 transcendence route is
robust but needs effective H-L for cost content; the §6 no-invariant-
measure route is robust but operates on different substrate.

---

## Convergence with AMORTIZATION-AT-THE-BOUNDARY

[memos/AMORTIZATION-AT-THE-BOUNDARY.md](memos/AMORTIZATION-AT-THE-BOUNDARY.md)
identified Route 3 (L-W envelope via per-sample transcendence) as the
most promising attack on `(4)`/`(5)`-strong, reducing non-amortization
at the boundary to effective H-L `n = 1`. This memo's positive verdict
(replacement obstruction via §4 + effective H-L at variable precision)
arrives at the same upstream dependency from a different direction —
bridge contrapositive in cost form rather than direct per-sample work
bound.

The convergence sharpens the program's substrate-side priorities:

- Effective H-L `n = 1` is now load-bearing for **two distinct
  algorithm-side reductions**:
  1. AMORTIZATION's `(4)`/`(5)`-strong via per-sample distinguishability.
  2. THIS memo's bridge transport via cost-level source-side hardness
     under variable precision.
- The form effective H-L must take is shared between them: a
  per-sample, precision-dependent distinguishability lower bound
  on `ε` at machine dyadics. Both reductions consume this in
  cost-norm-compatible form.
- This is no longer adjacent program work. It is the program's
  **central upstream dependency** for the impossibility region (the
  difference between the §4.5 statement and the full FIRST-PROOF
  theorem).

---

## Updates to PHASE-LIFT-CONSERVATIVITY-AUDIT.md

§"Definitional condition" should record:

- **The deferred re-derivation has been attempted.**
  [fft/LANDFALL-EXTENDED-CAFF-TRANSFER.md](fft/LANDFALL-EXTENDED-CAFF-TRANSFER.md)
  finds that under the (P) reading at fixed precision — the audit's
  natural reading — the §2 transfer fails: `ε` is `O(N)` in extended
  `C_Aff` via Taylor approximation. The bridge contrapositive does
  not bite under this resolution.
- **A replacement obstruction is identified.** Under variable
  precision and effective H-L `n = 1`, Landfall §4's transcendence-at-
  dyadics upgrades to a per-sample distinguishability lower bound,
  giving `ε ∈ Ω(N log N)` in extended `C_Aff` at precision `∝ log N`.
  The bridge contrapositive then bites and the impossibility lands.
- The audit's promotion verdict **(ii) Clean-conditional** therefore
  resolves to: **clean only under the variable-precision + effective-
  H-L replacement**. Under fixed precision with the §2 obstruction as
  source-side, the bridge does not deliver the impossibility.

§"Trust boundary" should record: the bridge's contentfulness depends
not just on the `C_Aff` definitional move but also on (i) the cost
model (fixed vs variable precision), and (ii) the source-side
obstruction (Landfall §2 statement vs §4 + effective H-L). The
program's commitment must name both choices explicitly before the
rewrite of [paper/FIRST-PROOF.md](paper/FIRST-PROOF.md) or
[paper/IMPOSSIBILITY-OUTLINE.md](paper/IMPOSSIBILITY-OUTLINE.md)
proceeds.

---

## Updates to PHASE-DEFECT.md

§"Sub-debts" sub-debt 3 (phase-lift conservativity) should record:

- The sub-debt's bridge contentfulness verdict from
  [fft/PHASE-LIFT-CONSERVATIVITY-AUDIT.md](fft/PHASE-LIFT-CONSERVATIVITY-AUDIT.md)
  refines via [fft/LANDFALL-EXTENDED-CAFF-TRANSFER.md](fft/LANDFALL-EXTENDED-CAFF-TRANSFER.md):
  the bridge is contentful and impossibility-delivering only under
  **variable precision** plus **§4 + effective H-L `n = 1`** as the
  source-side obstruction. Under the audit's natural fixed-precision
  reading with §2 as source, the bridge gives no impossibility.
- Sub-debt 3 therefore promotes from "Clean-conditional" on the
  `C_Aff` definitional move to "Clean-conditional on (i) variable-
  precision cost model and (ii) effective H-L `n = 1` delivering the
  per-sample distinguishability bound in cost-norm-compatible form."
- The two conditionals are inherited by **debt #3** (Template
  transfer) of FIRST-PROOF and by **debt #2** (algebra of `δ`) via
  AMORTIZATION-AT-THE-BOUNDARY's parallel reduction.

---

## Updates to FIRST-PROOF debt #3

The Template transfer debt should record:

- Source-side instance was named as `λ`/`ε` per Landfall §2; transport
  candidate was the character reflection barrier of PHASE-DEFECT.
- This memo finds the §2 instance does not transport at the cost
  level under extended `C_Aff` at fixed precision. The replacement
  source-side instance is **`ε` at variable precision under effective
  H-L `n = 1`**.
- Debt #3 is therefore re-typed: instead of "transfer Landfall §2,"
  the debt is now "transfer Landfall §4 + effective H-L to a cost-
  level source-side obstruction in extended `C_Aff` at variable
  precision."
- The transport mechanism (character reflection barrier / phase-lift
  conservativity) is unchanged; the source content it transports is
  upgraded.

---

## What this memo does not do

- **Does not prove effective H-L `n = 1`.** The replacement
  obstruction depends on the program's substrate-side interim target
  delivering a per-sample distinguishability bound in
  cost-norm-compatible form. That work is parked.
- **Does not prove the variable-precision cost model is the right
  one.** The replacement assumes precision `∝ log N`; other scalings
  (precision `= constant`, precision `= polynomial in N`) give
  different verdicts. The choice of precision-scaling is a model
  commitment the program owes.
- **Does not authorize promotion.** The Landfall §2 fall and §4
  replacement are structural findings; they require effective H-L `n
  = 1` to land before any rewrite of FIRST-PROOF or IMPOSSIBILITY-
  OUTLINE proceeds.
- **Does not survey the canon for variable-precision cost-model
  compatibility.** Under variable precision the canon's `Ω(n log n)`
  cluster (Morgenstern, AFW, Ailon) needs re-examination — each was
  proved at its own precision assumption, and the bridge's
  applicability depends on alignment.

---

## Trust boundary

The (P)-reading verdict (`ε` is `O(N)` in extended `C_Aff` at fixed
precision via Taylor) uses standard floating-point cost analysis with
free precomputed constants. Under charged-constants models, the
verdict shifts: per-sample cost stays `O(1)`, but a one-time
precomputation cost of `O(precision)` is added. The `O(N)` total is
unchanged at fixed precision; at variable precision the
precomputation cost grows but does not change the per-sample
asymptotics.

The (E)-reading verdict uses Landfall §4's transcendence-at-dyadics
fact, which is L-W safe under content-not-calendar (Hermite-Lindemann
1882 is the program's anchor).

The replacement-obstruction verdict assumes effective H-L `n = 1` in
a form that delivers per-sample distinguishability at cost
`Ω(precision)`. The form-claim is plausible from program goals but
not delivered by this memo. The substrate-side work owes the
algorithm-side a precise effective-H-L statement that this memo and
AMORTIZATION-AT-THE-BOUNDARY both consume.

The variable-precision cost model is not standard in the FFT
literature (which typically fixes machine precision). Adopting it
requires either (i) reading the canon's `Ω(n log n)` bounds as
implicitly variable-precision or (ii) re-proving them in the
variable-precision regime. Neither is checked here.

This memo introduces no new external sources; all inputs are from
existing program material:
[sources/landfall.pdf](sources/landfall.pdf) (re-read for §2 and §4),
[fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md),
[fft/PHASE-LIFT-CONSERVATIVITY-AUDIT.md](fft/PHASE-LIFT-CONSERVATIVITY-AUDIT.md),
[fft/COCYCLE-COMPOSITION-LAW.md](fft/COCYCLE-COMPOSITION-LAW.md),
[memos/AMORTIZATION-AT-THE-BOUNDARY.md](memos/AMORTIZATION-AT-THE-BOUNDARY.md),
[measure/ALGEBRA-OF-DELTA.md](measure/ALGEBRA-OF-DELTA.md),
[fft/LANDFALL-PROOF-TEMPLATES.md](fft/LANDFALL-PROOF-TEMPLATES.md),
[paper/FIRST-PROOF.md](paper/FIRST-PROOF.md).
