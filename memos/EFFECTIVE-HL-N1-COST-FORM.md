# EFFECTIVE-HL-N1-COST-FORM

Spec for the form effective Hermite-Lindemann at `n = 1` must take to
discharge two algorithm-side reductions:
[memos/AMORTIZATION-AT-THE-BOUNDARY.md](memos/AMORTIZATION-AT-THE-BOUNDARY.md)
Route 3 and
[fft/LANDFALL-EXTENDED-CAFF-TRANSFER.md](fft/LANDFALL-EXTENDED-CAFF-TRANSFER.md)
replacement obstruction. Algorithm-side memo; substrate-side delivery
is parked program work.

This is the substrate-side input THE-FIRST-BRIDGE consumes — the
"lower-bound shape the bridge needs to consume" of
[measure/THE-FIRST-BRIDGE.md](measure/THE-FIRST-BRIDGE.md). The bridge
whose construction it consumes is T4b in
[measure/FOR-BREAKFAST.md](measure/FOR-BREAKFAST.md) §K.6 (boundary
object with `δ`-faithfulness). The form spec'd here is what T4b's open
load-bearing task needs to acquire its quantitative content; without
delivery in this form, the bridge's contrapositive does not bite.

---

## The spec

For every scheme `S` in extended `C_Aff` (closure under `+, −, ×, ÷`
on machine numbers, with bounded-degree polynomial approximations of
fixed-precision real functions, regularity guard per
[fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md)) that produces `ε(m)` to
precision `2^{-p}` on machine-dyadic input `m = k/2^p`,

```text
cost_total(S, m, p)  ≥  c · p
```

for some constant `c > 0` independent of `m`, `S`, and `p`, where
`cost_total` is **total cost in a uniform-charge model**: native
operations performed *and* stored bits used (constants, tables,
precomputed state), all charged at the same precision granularity.
The operational cost-norm of
[fft/COCYCLE-COMPOSITION-LAW.md](fft/COCYCLE-COMPOSITION-LAW.md) is
the operations-side component; storage bits enter at the same charge
per bit as a single operation. Tables and microcode and any other
form of precomputation are charged for what they store and how they
are used; nothing is uncharged.

The constant `c` need not be sharp. Existence at this form suffices.

---

## Why this form

Three properties the algorithm side consumes.

1. **Per-sample.** The bound is on a single sample, indexed by `(m, p)`.
   Aggregation across `N` samples is the algorithm side's job (linearity
   of the operational cost-norm under scheme composition; Route 3 of
   AMORTIZATION).
2. **Precision-dependent.** The bound scales as `Ω(p)` in precision
   `p`, not as a constant. Under variable precision `p ∝ log N`, this
   aggregates to `Ω(N log N)` total cost — matching the canon
   threshold `T(P)`.
3. **Stated against a uniform-charge cost model.** Total cost
   charges all stored bits and all native operations at the same
   precision granularity, so tables, microcode, and other forms of
   precomputation cannot purchase savings the cost model fails to
   record. The bound holds against any scheme regardless of how it
   allocates work between storage and computation. "Tables yes / no"
   is not a meaningful axis: under uniform charging, both pay the
   same total, and the `Ω(p)` lower bound fires either way.

---

## Information-theoretic basis

The `Ω(p)` bound is robust under cost-model uniformity because
`ε(m)` is incompressible at the bit level. For a transcendental
target, knowledge of bits up to position `P` does not better-than-
chance predict the bit at position `P + 1`: the conditional
probability of any further bit is asymptotically `1/2`, equivalently
zero conditional mutual information. Each new bit *is* `Ω(1)` in
information content; precision `p` requires `Ω(p)` such bits;
`cost_total` follows.

This is the property effective Hermite-Lindemann at `n = 1` is
delivering as the program's quantitative substitute. The lower
bound is therefore *not* a count of arithmetic operations in any
specific architecture. It is a statement about how much information
any scheme — regardless of tables, precomputation, or microcode —
must encode and ship to deliver `ε(m)` at precision `p`.

---

## What it is not

- **Not a bound on a specific algorithm.** The bound must hold for
  *every* `S` satisfying the regularity guard. Lower-bound shape, not
  upper-bound shape.
- **Not a sharp constant.** Any `c > 0` independent of `p` and `m`
  suffices for the asymptotic transport.
- **Not a bound on bit-precision input/output handling.** Charges
  apply to the *internal* work of producing `ε(m)`, not to reading
  `m` or writing the output.
- **Not a fixed-precision bound.** The `Ω(p)` form must survive as
  `p` grows. Fixed-precision bounds (`p = 52` machine bits) collapse
  to `Ω(1)` and don't aggregate.

---

## Audit task (parallel quick-win)

Check the program's existing effective-H-L material for proximity to
this spec. Most likely candidates:

- [memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md](memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md)
  — the title is the closest match; check whether it delivers a
  per-sample bound at the precision-scaling required.
- [memos/LINDEMANN-BRIEF.md](memos/LINDEMANN-BRIEF.md) — base case
  (existence-only); confirms what is *not* enough.
- [memos/LIOUVILLE-SCALE-TEST.md](memos/LIOUVILLE-SCALE-TEST.md) —
  Liouville machinery may give effective-bound shape on adjacent
  objects; useful as analogy or as direct material if it transports.
- [memos/RAMANUJANS-COMPLIMENT.md](memos/RAMANUJANS-COMPLIMENT.md) —
  search memo; may have parked H-L material.

If existing material delivers a bound of the right form for `ε(m)`
at machine dyadics, the spec discharges immediately. If existing
material gives a weaker form (`Ω(log p)`, or `Ω(p)` only at fixed
constants), the gap to this spec is the substrate-side work owed.

---

## Debt #9 reminder (do not add to FIRST-PROOF yet)

The bridge transport from `ε`-cost to `{Δ_k}`-cost via the
contrapositive of phase-lift conservativity also requires a
**variable-precision cost model**. Effective H-L at the form above
gives `Ω(p)` per-sample; aggregation to `Ω(N log N)` requires
precision `p ∝ log N`. The canon's `Ω(n log n)` cluster (Morgenstern,
AFW, Ailon) was largely proved at fixed precision; whether those
bounds re-read cleanly at variable precision is a sibling dependency
that this spec does not discharge.

When the rewrite of [paper/FIRST-PROOF.md](paper/FIRST-PROOF.md) is
authorized, this dependency enters as **debt #9** (working name:
*variable-precision cost model and canon re-read*). Not added to the
debt list yet; the eight-debt count holds until the rewrite. The
reminder lives here.

---

## Adjacent anchors

- [memos/AMORTIZATION-AT-THE-BOUNDARY.md](memos/AMORTIZATION-AT-THE-BOUNDARY.md)
  — Route 3 consumer of this spec.
- [fft/LANDFALL-EXTENDED-CAFF-TRANSFER.md](fft/LANDFALL-EXTENDED-CAFF-TRANSFER.md)
  — replacement-obstruction consumer of this spec.
- [fft/COCYCLE-COMPOSITION-LAW.md](fft/COCYCLE-COMPOSITION-LAW.md) —
  operational cost-norm definition.
- [fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md) — regularity guard
  definition; sub-debt 3 status.
- [fft/PHASE-LIFT-CONSERVATIVITY-AUDIT.md](fft/PHASE-LIFT-CONSERVATIVITY-AUDIT.md)
  — audit verdict refinement consuming this spec.
- [measure/ALGEBRA-OF-DELTA.md](measure/ALGEBRA-OF-DELTA.md) §(4), §(5)
  — algebra-of-`δ` sub-questions whose discharge this spec specifies
  (substrate-side delivery actually discharges).

---

## Trust boundary

This memo is algorithm-side. It states what the substrate-side work
must deliver; it does not deliver it. The spec is L-W safe under
content-not-calendar (effective H-L is post-1882 in calendar but
classified by its contentful use; per
[memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md)
substrate-side work governs that classification, not this memo).

The form claim — `cost_op ≥ c · p` for some `c > 0` independent of
`m`, `S`, `p` — is necessary for the algorithm-side reductions to
fire as stated. It is not claimed sufficient for any specific
substrate-side proof route; weaker effective-H-L forms may suffice
for narrower algorithm-side claims, but the bridge transport in
LANDFALL-EXTENDED-CAFF-TRANSFER needs this form.
