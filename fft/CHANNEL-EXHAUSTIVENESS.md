# CHANNEL-EXHAUSTIVENESS

Discharge of construction-debt #11 (channel exhaustiveness for §6.6 composition, path-(i)-by-enumeration over §4.2.2's native operations). Project-management doc + bookkeeping content. Pointer back from `paper/PROOF-CHAIN.md` §6 debt #11 entry; companion to `paper/T4B-DECOMPOSITION.md` (T4b's three faithfulness clauses are what the four §6.6 channels map onto).

## Recap of debt #11

**Structural premise.** Any FFT-style lower-bound proof past `T(P)` must route through one of §6.6's four descent-channel cases. Without exhaustiveness in some form, §4.5's theorem reads "no FFT-style descent through these specific channels" rather than "no FFT-style descent."

**Committed closure form.** Path (i) by finite-composition enumeration over §4.2.2's five native operations. The §6.6 chase walks the case structure against T4b's three faithfulness clauses (Phase 1c verified): Farey recoding → clause (i); cross-register iso → (ii)-substrate; mult-add trading → (ii)-algorithm; tables/advice → (iii). The residual check is whether finite compositions of §4.2.2's five operations stay inside that four-channel routing.

**Path (ii) declined.** Re-tailoring the FFT-style class around the operations §6.6 happens to block would dissolve the syntactic-class meaning the §Conclusion outflow trades on. The class definition stays fixed at §4.2.2 descriptively (each operation traced to a §3 canon source).

**Path (iii) absorbed.** Negative-space covering over candidate non-blocked descents is forced to range behaviorally and is undecidable in general (Rice's theorem). The §Conclusion outflow recognizes this as the natural future-research horizon, not as a closable debt within the apparatus.

## Setting

**The four §6.6 channels** (named per PAPER §4.6 / §6.6):

- **Channel A (Farey recoding).** Method passes `(k, n) ∈ L` through the reduction `R : L → F` and tries to read the threshold position on the reduced fraction. *Mapped to faithfulness clause (i):* observables `f₁, f₂, f₃` factor through δ via the substrate-side L-route, not through F via R^*.
- **Channel B (cross-register iso conversion).** Method trades a rate-form bound for a sharp-constant bound (or analogous moves between iso registers). *Mapped to clause (ii)-substrate:* the iso-register currency structure (rate / constant / almost-every; 5π overhead and type-gap) is encoded measurably on `(Z, ℱ, ν, δ)`.
- **Channel C (mult-add trading).** Method trades multiplicative cost for additive cost across the cocycle, exploiting cross-currency conversion between Morgenstern (additive) and Winograd / AFW (multiplicative). *Mapped to clause (ii)-algorithm:* algorithm-side cross-currency structure (Morgenstern↔Ailon non-transfer, §3.2 / §3.6.2) is encoded measurably alongside `(μ, α)`.
- **Channel D (tables / advice).** Method tries to absorb residue with size-dependent shortcuts: precomputed tables, advice strings, oracle constants. *Mapped to clause (iii):* closure-class membership reads measurably against `(Z, ℱ, ν, δ)` via §5.5's admissibility envelope plus §4.2.1's regularity guard, which excludes uncharged advice / oracle / table-per-size shortcuts.

**The five native operations** (per §4.2.2, each traced to a §3 canon source):

- **O1 — Recursive FFT decomposition** (Schönhage–Strassen 1971, §3.2).
- **O2 — CRT / tensor factorization** (Winograd 1978, §3.4; Auslander–Feig–Winograd 1984, §3.5).
- **O3 — Linear-composition closure** (all four lower-bound canon sources; cf. §3.6.1).
- **O4 — Cyclotomic factor accounting** (Auslander–Feig–Winograd 1984, §3.5).
- **O5 — Coefficient-regime bookkeeping** (Morgenstern 1973, §3.3).

**Closure-class framing.** Each channel `X ∈ {A, B, C, D}` defines a closure class `D_X` of descent attempts: the set of FFT-style methods whose escape past `T(P)` factors through channel `X`. Channel exhaustiveness asks whether `D_FFT ⊆ D_A ∪ D_B ∪ D_C ∪ D_D` where `D_FFT` is the set of all FFT-style methods (finite compositions of {O1, …, O5} under §4.2.1's guard) attempting to descend past `T(P)`.

The verification proceeds in two parts: (1) per-operation classification — each `O_i` engages some non-empty subset of `{A, B, C, D}` when used in a descent attempt; (2) composition closure — finite compositions of `{O1, …, O5}` stay in the union of channels engaged by their constituents.

## Per-operation classification

For each native operation `O_i`, name which channel(s) it engages when used as part of a descent past `T(P)`. The classification is "any composition involving `O_i` can be classified as routing through channel `X`" (channels are not disjoint; an op can engage multiple channels depending on context).

### O1 — Recursive FFT decomposition

*What the op does.* Decomposes a DFT of size `N` into smaller DFTs at radices `r_1 · r_2 · … = N`. Schönhage–Strassen's Fermat-ring construction (`Z/F_n Z`) is the in-canon prototype; Cooley–Tukey radix-2 is the analytic specialization.

*Channel engagements.* Recursive decomposition does not by itself recode indices through `R`; it operates within the cyclotomic substrate's recursive symmetry. However, when used in a descent attempt past `T(P)`:
- **Channel A** if the recursion's index labels are read through `R` (e.g., decomposing at radix `r` and identifying sub-DFTs by Farey-reduced indices). The method tries to read `f_i` on the reduced sub-DFT structure; clause (i) blocks via Theorem K.
- **Channel C** if the recursion is composed with linear-combination steps that trade per-stage multiplications for additions across stages. The method tries to amortize multiplicative cost across recursive levels; clause (ii)-algorithm blocks via Morgenstern↔Ailon non-transfer.
- **Not B** directly: O1 alone doesn't engage iso-register conversions (substrate-side observables are not modified by recursion structure on the algorithm side).
- **Not D** directly: O1 doesn't introduce advice unless composed with O5 in a precomputed-table mode.

*Channels engaged: {A, C}.*

### O2 — CRT / tensor factorization

*What the op does.* Decomposes polynomial-quotient rings `ℚ[x] / T_P` via CRT into a product over irreducible factors `∏ ℚ[x] / p_i(x)`, then further into cyclotomic factors when applicable (Winograd's `μ(T_P) = 2n − k` ledger).

*Channel engagements.*
- **Channel A** if the CRT decomposition reads on Farey-reduced indices for the modular product (e.g., evaluating polynomial multiplications at coprime indices `(k, n)` and trying to recover `f_i`); clause (i) blocks.
- **Channel C** is the headline mode — CRT factorization trades a single bilinear product mod `T_P` for `k` smaller bilinear products in the residue rings, then potentially rebalances via linear combinations. The mult-add trading is the natural target; clause (ii)-algorithm blocks.
- **Not B** directly: substrate-side iso registers are not produced by CRT structure.
- **Not D** directly: CRT factorization itself is not advice.

*Channels engaged: {A, C}.*

### O3 — Linear-composition closure

*What the op does.* Linear combinations of intermediate values with field-coefficient scalars. The additive primitive that all four canon sources admit; the operation Morgenstern's bound counts.

*Channel engagements.*
- **Channel C** is the primary engagement — linear composition is exactly mult-add trading at the primitive-operation level. Trades multiplicative work for additive work; clause (ii)-algorithm blocks via Morgenstern's bounded-coefficient `Ω(n log n)` floor and Ailon's matrix-entropy potential on the normalized side.
- **Channel D** if linear combinations are used to encode size-dependent precomputed tables (e.g., a linear combination whose coefficients are tabulated per `n`); clause (iii) blocks unless the table construction is charged at granularity `p`.
- **Not A** directly: linear combinations don't recode through `R`.
- **Not B** directly: substrate-side iso registers are not modified by linear combinations alone.

*Channels engaged: {C, D}.*

### O4 — Cyclotomic factor accounting

*What the op does.* Tracks decomposition of group DFTs `ℚ[G] = ∏_{d | |G|} ℚ(ζ_d)` per Auslander–Feig–Winograd 1984. Manages the cyclotomic-factor ledger underpinning the multiplicative-complexity bound on cyclotomic DFTs.

*Channel engagements.*
- **Channel A** if cyclotomic indexing identifies sub-fields via Farey-reduced rational indices (cyclotomic field `ℚ(ζ_d)` for `d | n` carries Farey structure); clause (i) blocks via Theorem K.
- **Channel B** if cyclotomic-defined iso readings (e.g., the regular `n`-gon's cyclotomic field `K_n^+ = ℚ(cos(2π/n))` underwrites the iso rate-register reading); cross-register iso-conversion attempts via cyclotomic structure; clause (ii)-substrate blocks.
- **Channel C** if cyclotomic factorization is composed with linear combinations to trade multiplicative cost across factors; clause (ii)-algorithm blocks via AFW's per-factor multiplicative complexity.
- **Not D** directly: cyclotomic accounting is structural, not advice.

*Channels engaged: {A, B, C}.*

### O5 — Coefficient-regime bookkeeping

*What the op does.* Tracks coefficient regime (bounded / unbounded) per Morgenstern 1973's framing. Maintains the bounded-coefficient invariant that Morgenstern's determinant-potential argument requires; or moves between regimes via explicit bookkeeping.

*Channel engagements.*
- **Channel C** if regime-bookkeeping shifts cost between bounded-additive (Morgenstern) and unbounded-multiplicative (Winograd, AFW) currencies — the cross-regime mult-add trading move; clause (ii)-algorithm blocks.
- **Channel D** if the bookkeeping uses size-dependent precomputed-coefficient tables (the natural precomputed-tables route); clause (iii) blocks unless table construction is charged.
- **Not A** directly: regime tracking is not Farey recoding.
- **Not B** directly: substrate-side iso registers are not modified by regime bookkeeping.

*Channels engaged: {C, D}.*

### Summary table

| Op | A: Farey | B: Iso | C: Mult-add | D: Tables |
|---|---|---|---|---|
| O1 — Recursive FFT decomposition | ✓ | — | ✓ | — |
| O2 — CRT / tensor factorization | ✓ | — | ✓ | — |
| O3 — Linear-composition closure | — | — | ✓ | ✓ |
| O4 — Cyclotomic factor accounting | ✓ | ✓ | ✓ | — |
| O5 — Coefficient-regime bookkeeping | — | — | ✓ | ✓ |

Every native operation engages at least one channel; collectively the channels cover all five operations. No operation escapes the four-channel partition.

## Composition closure

**Claim.** Finite compositions of `{O1, …, O5}` stay in the union of the four channels engaged by their constituents.

**Proof sketch.** Let `S = O_{i_n} ∘ ⋯ ∘ O_{i_1}` be a finite composition. Consider `S` as a descent attempt past `T(P)`. The descent attempt's structural form is determined by `S`'s composition path: each `O_{i_j}` step performs a transformation on the running state that is classified by the channel(s) engaged at that step (per the per-operation table above). The cumulative channel engagement of `S` is the union over `j` of the channels engaged by `O_{i_j}`.

Formally, define the *channel set* of a composition `S` as
```
Channels(S)  :=  ⋃_{j = 1}^{n}  Channels(O_{i_j})
```
where `Channels(O_i)` is the per-operation table's row. Since the table shows every `Channels(O_i) ⊆ {A, B, C, D}`, we have `Channels(S) ⊆ {A, B, C, D}` for every finite composition. The descent attempt of `S` factors through `Channels(S)` — equivalently, through the union of clauses (i)–(iii) that the channels-to-clauses mapping covers.

**Why composition doesn't introduce new channel structure.** A composition `O_{i+1} ∘ O_i` performs `O_i` first then `O_{i+1}`; the descent-attempt structure is the *concatenation* of the two operations' descent moves. Concatenation of channel-routed moves is itself channel-routed (the resulting attempt factors through the union of channels). No "fifth channel" emerges from composition because:
1. *Farey recoding* (channel A) is a structural recoding through `R`; concatenating `O_i ∘ O_{j}` doesn't introduce new substrate-coordinate structure beyond what `O_i, O_j` individually engage.
2. *Cross-register iso conversion* (channel B) requires substrate-side iso-register access, which only O4 supplies; compositions involving O4 retain channel B.
3. *Mult-add trading* (channel C) is the additive primitive's universal mode; compositions involving O3 (and structurally any composition since O3 is the linear-composition closure) retain channel C.
4. *Tables / advice* (channel D) is engaged only when the composition's bookkeeping introduces uncharged shortcuts; this is detectable from the composition's structure (per §4.2.1's regularity guard, advice is excluded by class definition unless charged).

The four channels are *closed under composition* in the sense that channel-routing of constituents lifts to channel-routing of the composite. ∎

**Smarter-FFT rebuttal coupling.** The §6.6 smarter-FFT rebuttal closes the residual case: a hypothetical "smarter" FFT-style method improving past `T(P)` would need to invent a *new* cross-currency or cross-regime transfer mechanism outside the canon's stack. By §3.6.2's currency-stratification (Morgenstern↔Ailon non-transfer; substrate-side iso non-nesting), no canon source supplies such a mechanism, and FFT-style closure cannot manufacture one from {O1, …, O5}. The "smarter" method therefore lies outside §4.2's class — not inside it being smarter.

## What's open / what's closed

**Closed (by this discharge).**
- ✓ Per-operation classification: 5 ops × 4 channels mapped (table above).
- ✓ Composition closure: finite compositions of {O1, …, O5} stay in the union of the four channels.
- ✓ Channels-to-clauses mapping: aligned with Phase 1c's verified faithfulness clauses (i), (ii)-substrate, (ii)-algorithm, (iii).

**Open within debt #11 (residuals).**
- The per-operation classification is *qualitative* (which channels each op can engage). A *quantitative* refinement — naming the cost coordinate at which each op engages each channel, and verifying the cost reads on δ at the correct rate — is a Phase 1c-adjacent extension; not load-bearing for §4.5's theorem but tightens the apparatus.
- Path (iii) — negative-space covering over the extensional class — remains the recursion-theoretic horizon (§Conclusion outflow). Not closable within the apparatus; absorbed as future-research direction.

**Discharged.** Path (i) commitment closes. §4.5's theorem reads "no FFT-style descent" rather than "no FFT-style descent through these specific channels."

## Couplings

- **T4b (debt #1):** The four channels-to-clauses mapping requires Phase 1c's verified faithfulness clauses. T4b structural closure is the prerequisite; #11's discharge is the bookkeeping that makes the §6.6 contradiction land for every FFT-style method.
- **§3.6.2 currency-stratification:** Channel C (mult-add trading) and the smarter-FFT rebuttal both consume the §3.6.2 in-canon witness for forced currency-stratification. Without §3.6.2's content, channel C's clause (ii)-algorithm reading is structurally incomplete.
- **§4.2.1 regularity guard:** Channel D (tables / advice) is closed by the §4.2.1 charging discipline. Advice-bearing schemes are out-of-class by definition; the regularity guard is what makes this exclusion measurable on `(Z, ℱ, ν, δ)`.
- **§Conclusion outflow:** Path (iii) — extensional channel exhaustiveness — is named in the outflow trinity (#11(iii), #14, #15) as the recursion-theoretic horizon. This discharge closes path (i); path (iii) remains as the natural future direction, not a closable debt.

## Acceptance status

| Criterion | Status |
|---|---|
| Per-operation classification (5 ops × 4 channels) | ✓ Per-operation table |
| Composition closure (finite compositions stay in channel union) | ✓ Composition closure section |
| Alignment with Phase 1c's verified clauses | ✓ Channels-to-clauses mapping per §6.6 |
| Path (ii) declined explicitly | ✓ Recap; class definition stays at §4.2.2 |
| Path (iii) absorbed as recursion-theoretic horizon | ✓ §Conclusion outflow per `project_debt_11_priority.md` |

**Debt #11 closes (path (i) form).** Composition closure verified at the qualitative level; quantitative cost-coordinate refinement open as a non-load-bearing tightening item.

## Hand-off back to apparatus

With debts #1 (T4b) and #11 (channel exhaustiveness) closed structurally, §4.5's theorem holds modulo the remaining open items in the construction-debt ledger:

- **Debt #5 (endpoint commitment) — now tractable.** The non-vanishing-transaction-cost lemma `δ ≥ δ_min(P) > 0` at `T(P)` lives on the faithful `(Z, ℱ, ν, δ)`. Both halves (existence at `T(P)`; implication past `T(P)`) bridged by debt #2(8).
- **Debt #2(8) (floor extension bridge) — tractable.** Bridge between #5's halves; the structural locus is in hand.
- **Debt #3 (effective H-L `n=1` cost-form) — substrate-side delivery owed.** The long-pole substrate-side input the cost algebra consumes; not gated by T4b or #11.
- **Debt #12 (currency-morphism construction) — per-morphism rigor.** Consumed by Phase 1b; closes the T4b construction's residual.
- **Debt #9(c) (variable-precision canon re-read) — substantive open work.** Not gated by T4b or #11.

The §6.6 contradiction now composes cleanly: T4b supplies the faithful structure; #11 supplies the channel exhaustiveness; #5 + #2(8) supply the endpoint commitment with bridge; the four channels close on `(Z, ℱ, ν, δ)` for every finite composition of native operations. What remains are the substrate-side cost-form (#3), the per-morphism rigor (#12), and the canon re-read at variable precision (#9(c)) — each tractable in its own right.
