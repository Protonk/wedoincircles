# PERMEATE-THE-CIRCLE

A research program conducted under the discipline of small-case saturation. The productive constraint is practice: no cross-domain claim is admitted without the tabulation that would let a reader anticipate it. The epistemological move is anticipation grounded in saturation, rather than derivation from first principles (BIND) or explicit construction from primitives (CREATI).

---

**Pointer.** PERMEATE is the third character-led discipline alongside BIND (Aizawa, Erasure) and CREATI (Momo, Construction). The abstract triad pattern is in `triad/TRIAD-ABSTRACT-PATTERN.md`. PERMEATE's leg of best fit is Leg 2 (crystallographic ↔ p-adic matching), because Leg 2's central move — pairing an n on the circle side with an m on the log side by shared arithmetic — is exactly the cross-domain phasing that requires saturation to do reliably. The stance is more general than the leg, though: PERMEATE applies wherever tabulation produces predictive intuition, and we expect to find it useful on Legs 1 and 3 at the right grain of attention.

**Complementarity note.** PERMEATE, BIND, and CREATI are complementary disciplines by design, not by convergence. Each imposes a different productive constraint:

- BIND's constraint is **vocabulary**: erase ?(x) / SB / Farey / Thomae / Denjoy; work in primitives on each side separately.
- CREATI's constraint is **form**: every object is a count, a closed form, or an identity; nothing exists that cannot be written down.
- PERMEATE's constraint is **preparation**: no cross-domain move without the small-case data to anticipate where it lands.

Future lemmas will need to state what each discipline reaches that the others cannot. This doc tolerates the gap rather than papering it over.

**Working hypothesis (triad-aware, Leg 2 local).** At the triad level, F probably does not exist. PERMEATE expects to find the obstruction by saturating the matched-pair tables until predictions become possible, then identifying the first pair at which prediction breaks. For Leg 2 specifically: partial-F probably exists on the {2, 3, 5}-smooth n, and breaks at n = 7, with 7 as the first prime outside the log rep's support and therefore the first index where ψ(n) has no natural v_p cousin. The break is predicted from saturation before it is derived; the derivation confirms what the tabulation already made visible.

---

## Constraints on method (Mirio)

PERMEATE is the discipline of *practice*. The central constraint: **no cross-domain claim is admitted without the small-case tabulation behind it.** Cross-domain moves — taking a log-side object and asserting a circle-side counterpart, or vice versa — are expensive in this discipline. The expense is paid in advance, as tabulation. The research move itself, once paid for, is cheap: after enough reps, you know where the argument will emerge without doing the full derivation.

This is not "we believe X because it feels right." It is a procedural move: the tabulation is the ground, the anticipation is the figure. If the ground is missing, the figure is not admitted.

Three implications, each a positive rule:

- **Saturation is the entry point.** Before any claim relating (say) ψ(n) to v_p(m), tabulate both over a window large enough that the pattern — or its absence — is visible without further work. The tabulation is not a supplement to the argument; it is where the argument starts.
- **Anticipation is admitted as a research move.** PERMEATE allows "I expect X to hold at this n before computing" provided the expectation is grounded in the saturation. BIND would require derivation; CREATI would require a constructed witness; PERMEATE accepts an informed prediction and judges it by whether it holds.
- **Failure is localized cheaply.** When a predicted move breaks, the saturation tells you exactly which pair broke and why. Obstruction-identification does not require a separate invariant-construction step; the data was already in hand.

## Primitives and admissible moves

**The primitive is the joint table.** Rows are matched pairs (n, m) — one circle-side index, one log-side index — with their invariants laid out: (n, τ(n), ψ(n), deg(2cos(2π/n))) on the circle side; (m, ε(m), v_2(denom(m)), algebraic degree) on the log side; and the matching rule that produced the pair. BIND's primitives live on each side separately. CREATI's primitives are catalog entries within each domain. PERMEATE's primitives live at the matching.

**Admissible move: anticipation from saturation.** Having tabulated over a declared window, predict the next pair's behavior before computing it. A correct prediction is evidence that the matching rule is catching structure. A failed prediction names the first discrepancy — and the discrepancy is the finding.

**Admissible move: cross-domain phasing.** Take an argument on one side, phase it through to the other, emerge with the claim stated in the destination's language. The cost is the matched-pair table covering the phasing domain. Uncontrolled phasing — phasing without the tabulation behind it — is inadmissible, and its outputs are not results.

**Admissible move: first-witness localization.** When a phasing fails, name the smallest matched pair at which it fails. That pair is the discipline's obstruction witness, read directly from the table rather than constructed by a side argument.

**Admissible move: convergent compression.** When an orbit-by-orbit table would be too expensive, replace the raw orbit construction by an equivalent Euclid / continued-fraction computation. Lefèvre–Muller’s 3DT filter is the model: the convergents are admitted as outputs of a finite computation, not as Stern-Brocot paths.

## What the stance buys

BIND trusts the walls between domains and never crosses them without importing a representational primitive. CREATI trusts the catalog within each domain and never admits objects without closed-form specification. Neither discipline has native rules for cross-domain *matching* — pairing an n with an m on the basis of shared arithmetic, shared spectral, or shared index structure.

PERMEATE trusts the tabulation. Saturation produces a shared substrate in which cross-domain moves are legible and on which predictive claims are checkable pair-by-pair. The method produces a different kind of confidence — not "derived from axioms" or "built from primitives," but "I have seen enough cases that this is what I expect, and here is the first case where the expectation would break." Obstruction-naming is a consequence of the method, not a separate deliverable.

When a problem depends on a slope or frequency $\alpha$, the continued-fraction convergents $p_n/q_n$ become part of that substrate. They tell PERMEATE how deep a saturation window has to go before a pattern is visible, and they make large-window tabulation computationally cheap enough to be useful instead of ceremonial.

## Steps

### Step 1. Build the joint saturation table.

Compute ψ(n), τ(n), deg(2cos(2π/n)) for n = 1..30. Compute ε(m) and v_2(denom(m)) for a grid of dyadic m. Pair them by a declared matching rule — the first-pass rule is: match n with the smallest DH such that n | DH, then read log-side valuations at that DH against circle-side invariants at n.

### Step 2. Predict.

Before computing n = 7: state that ψ(7) = 6 while v_7 of any DH built from primes in {2, 3, 5} is zero, so the matching must break at 7. Record the prediction in writing. Then compute and confirm.

### Step 3. Name the post-break obstruction.

On the {2, 3, 5}-smooth subset, tabulate whether a natural i : ℕ → ℕ exists such that ψ(n) = v_p(i(n)) for a fixed p. Trivial answers (i(n) = p^ψ(n)) are noted and excluded; natural candidates are those derivable from Landfall's primitives (binade depth, ε(m)'s denominator, DH itself). If a natural i exists on the smooth subset and breaks at 7, Leg 2's result is partial-F-with-witness.

### Step 4. Apply the method outside Leg 2.

Where else does saturation admit a cross-domain anticipation? For Leg 1: tabulate ε(k·m) and trace(R_n^m) jointly over a window and see whether the polynomial form predicted by Chebyshev on the circle side admits an anticipation-level log-side cousin. For Leg 3: tabulate τ_c(n, k, E) and ε(m) jointly over a parameter grid and see whether spectral invariants (decay rate, symmetry class) are anticipatable from one side to the other. The stance travels even when the matching rule changes.

## Deliverable shape

A note, method-first, containing:

1. The joint saturation table, exhaustively tabulated over a declared window.
2. The matching rule(s) that produced the matched pairs, stated explicitly.
3. The predictions, stated before computation, and verified (or falsified) after.
4. The first-witness localization of each obstruction, read from the table.
5. A discussion of what saturation made visible that first-principles derivation would have missed.

Length target: short. PERMEATE produces tabular, specific writeups. The table is the argument; the prose explains which cell broke first and why the break was anticipated.
