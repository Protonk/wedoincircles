# PHASE-DEFECT-PLAN

Edit map for turning [fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md) from a
parking-lot memo into a usable candidate proof spine. It names where edits
happen, why they happen, and what must be true before the cocycle formulation
can move into
[paper/FIRST-PROOF.md](paper/FIRST-PROOF.md) or
[paper/IMPOSSIBILITY-OUTLINE.md](paper/IMPOSSIBILITY-OUTLINE.md).

## Target Shape

The desired structure is simple:

1. Define the defect object clearly.
2. State what "competitive compression" would mean operationally.
3. Test whether the FFT canon aligns with that object.
4. Audit whether the analytic phase lift is L-W-safe.
5. Only then decide whether the outline and proof skeleton should be
   rewritten around No Free Descent.

The edits below serve that structure.

## Edit 1: Make Competitive Compression Operational

**Where.** [fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md), section
"What this would buy."

**Why.** The memo currently lists several meanings of "competitively
compressible." The operational one should lead, because it is the version a
candidate FFT scheme can actually be tested against:

> the scheme produces a defect-free FFT-style composition law whose
> character products agree across all butterfly refinements and primitive
> modes.

**What changes.** Move that operational definition to the front. Keep the
other candidate definitions as secondary tests:

- low-rank approximation under formal-character decomposition;
- `O(N log N)` evaluation on `N` samples without residual-coordinate cost;
- factorization into simpler cocycle factors closed under canon operations.

**End state.** `{Δ_k}` is not just a suggestive object; it has a first-pass
cost question attached to it.

## Edit 2: Put the Regularity Guard Where Readers Can See It

**Where.** [fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md), immediately after
"Character reflection barrier" or as a short subsection after the existing
"Closure-class regularity guard" paragraph.

**Why.** The theorem will only speak to uniform, non-growing closure classes
over a fixed base field. Advice, oracle constants, and growing state should be
excluded by the hypothesis class, not treated as defeated by the lemma.

**What changes.** Add a short list of excluded patterns:

- Bailey four-step style precomputation when it functions as advice;
- mixed-radix schemes with input-dependent radix selection;
- cache-oblivious or growing-state schemes when the state growth is doing the
  bridge work;
- any scheme whose constants or representation choices grow with the instance
  in a way not charged by the model.

Frame the exclusion as scope control, not as a victory. These schemes become
research targets outside the theorem's present hypothesis class.

**End state.** Bypass-resistance splits cleanly:

- advice / oracle / non-uniform bypass is ruled out by definition;
- amortization and per-instance specialization remain real sub-debts under
  the algebra of `δ`.

## Edit 3: Strengthen Ailon Positioning

**Where.** [fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md), section "External
positioning (Ailon)."

**Why.** Ailon is useful because it warns against claiming a broad Fourier
lower bound. PHASE-DEFECT should say why No Free Descent is not trying to be
that kind of theorem.

**What changes.** Replace the softer "sits beside it" language with this
separation:

> No Free Descent is immune to the broad-model lower-bound open problem Ailon
> flags because transport is structurally different from proving a direct
> Fourier lower bound. The cocycle reframe claims that exporting FFT cheapness
> across the additive/log-binade seam must carry the defect cocycle; it does
> not claim an unrestricted linear-circuit lower bound.

**End state.** Ailon becomes a scope marker and a proof-shape precedent, not a
threat to the cocycle plan.

## Edit 4: Work One Canon Translation

**Where.** New memo:
[fft/SCHOENHAGE-STRASSEN-COCYCLE-TRANSLATION.md](fft/SCHOENHAGE-STRASSEN-COCYCLE-TRANSLATION.md),
then a small update to [fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md), section
"Gating debt 1: coordinate-cut alignment."

**Why.** The alignment claim is too abstract until one canon source is tested.
Schönhage-Strassen is the right first test because its FFT structure is
explicit enough to ask whether the additive/log-binade cut can see the same
work the algorithm is doing.

**What the memo asks.** Re-read the Schönhage-Strassen bound through the
quotient-clock lens:

- What are the native operations?
- Where do additive and multiplicative costs separate?
- Does the algorithm's cyclotomic / negacyclic structure produce a natural
  `{Δ_k}`-compressibility question?
- Does the translation work, work only for a named subclass, or fail?

**Possible verdicts.**

- **Clean translation.** The alignment gate becomes stronger for SS-class
  methods.
- **Conditional translation.** The theorem scope narrows to the subclass where
  the translation is valid.
- **No translation.** SS does not support the cocycle route; PHASE-DEFECT must
  say so and reduce its theorem scope.

**End state.** "Coordinate-cut alignment" is no longer only plausible; it has
one worked test case and a recorded verdict.

## Edit 5: Audit Phase-Lift Conservativity

**Where.** New memo:
[fft/PHASE-LIFT-CONSERVATIVITY-AUDIT.md](fft/PHASE-LIFT-CONSERVATIVITY-AUDIT.md),
then updates to [fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md), sections "Gating
debt 2" and "What gets rewritten if the gates resolve favorably."

**Why.** This is the load-bearing audit. The forced identity is safe, but the
analytic realization `χ_k(t)=e^{2πikt}` may hide arithmetic information. The
paper cannot promote PHASE-DEFECT until it knows whether the phase lift imports
Baker-style machinery.

**Question.** If an FFT-style closure competitively constructs `{Δ_k}`, does
small-branch argument recovery force competitive construction of `ε(m)` in
`C_Aff`?

**Audit route.**

1. Prove or sketch the formal-cocycle transport without analytic exponential
   machinery.
2. Specialize to `χ_k(t)=e^{2πikt}`.
3. Identify every transcendence input used by the specialization.
4. Classify each input under
   [memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md)'s
   content-not-calendar rule.

**Possible verdicts.**

- **Clean.** No post-L-W machinery is needed; outline rewrite can proceed.
- **Clean with footnote.** The bridge uses only pre-1882 or methodologically
  recertified content; rewrite can proceed with the footnote.
- **Baker-essential.** The analytic specialization is post-1882 in substance;
  PHASE-DEFECT stays parked or moves to a separate sequel.

**End state.** The plan has a real go/no-go point for promotion.

## Deferred: Anti-Aggregation / Relocation

**Where eventually.** A later memo on the Layer 3 "relocate the defect" branch.

**Why deferred.** This is the hardest transfer from Landfall §6. It only
matters if Edit 5 returns clean or clean-with-footnote. If phase-lift
conservativity is Baker-essential, this work should not be scheduled now.

**Question when resumed.** If a scheme changes representation so the defect is
renamed or aggregated elsewhere, what is the pullback cocycle in the new
representation, and why can it not disappear by relabeling?

## Promotion Rule

No rewrite of [paper/FIRST-PROOF.md](paper/FIRST-PROOF.md) or
[paper/IMPOSSIBILITY-OUTLINE.md](paper/IMPOSSIBILITY-OUTLINE.md) lands until:

- competitive compression has an operational definition;
- at least one canon translation has a verdict;
- phase-lift conservativity has an L-W audit verdict.

If those three checks pass, PHASE-DEFECT can rewrite the proof around:

- `δ` as the cost of compressing `{Δ_k}`;
- Bridge Theorem as "descent past `T(P)` requires competitive compression of
  `{Δ_k}`";
- Lemma B as "native operations cannot competitively compress `{Δ_k}` at the
  boundary";
- Template transfer as character-pullback transport from `ε ∉ C_Aff` to
  `{Δ_k} ∉ C_FFT`.
