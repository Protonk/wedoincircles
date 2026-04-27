# FFT-SEARCH-PLAN

Parking lot for the FFT-as-search insight. Not yet load-bearing in the paper; held here while the framing matures. The integration discipline is at §"Discipline" below — vocabulary may promote into the outline and FIRST-PROOF when a move earns its way; slogans without lemmas stay parked.

## Frame

Gauss 1805 (per `fft/GOLDSTINE-1977-INTERPOLATION-BRIEF.md` §4.12) had a worked divide-and-conquer FFT for orbit interpolation. The Pallas worked example uses both `4×3` and `3×4` factorizations of `12`; Gauss chose them on practical grounds, not asymptotic ones. He did not count operations.

`fft/HEIDEMAN-JOHNSON-BURRUS-1985-BRIEF.md` documents the chain: the asymptotic-complexity register was later formalized by Cooley–Tukey 1965 and downstream (SS 1971, Morgenstern 1973, Winograd 1978, AFW 1984) on a substrate Gauss had already worked.

Reading FFT-style methods as adaptive strategies — not fixed conversions between mult and add — gives the hypothesis class in §4.2 sharper handles. The class is naturally a search-strategy family closed under composition. This is a *program-facing interpretation*, not a historical thesis: Goldstine + HJB support "Gauss had a worked divide-and-conquer FFT, no operation count, practical subdivision choices." Whether they support "FFT was always adaptive search" as a historical claim is not the bet here.

## Discipline

This plan is a parking lot. The integration rules:

1. **Promote vocabulary, not philosophy.** Strategy-family language goes into §1.5 and §4.2; the rest stays here.
2. **Promotion is conditional.** A search-plan item enters FIRST-PROOF only if it reduces a named construction debt.
3. **Slogans don't fire.** "Forbidding search is easier than forbidding technique" is the right rhetoric for this file but is not yet a lemma. The admissible version of the slogan is the typed-strategy-space framing already adopted at §4.2.2.
4. **Guardrail.** The search reading changes the formalization of the hypothesis class; it does not itself supply a lower bound. The Bridge Theorem remains the center of gravity.

## Why this helps the formalization (slogan-level)

Forbidding *search* offers more handles than forbidding *technique*. Search has structure that technique does not:

- **Search space.** Typed; the strategies admissible to FFT-style methods are bounded by the canon's native operations.
- **Search-cost algebra.** Per-strategy execution cost; per-strategy search cost (cost of finding the strategy from problem data); composition cost. *(See model caveat in pencil marks.)*
- **Information-theoretic bounds.** A search must extract distinguishing information from the substrate. Lemma A's exhaustiveness becomes the claim that no admissible information distinguishes strategies at the boundary.
- **Adversarial / decision-tree-style closure.** Oracle reductions might foreclose certain search-space regions. Could give Lemma A's exhaustiveness debt a tractable closure path.

These are reasons to develop the search reading; none of them yet enters the proof. The admissible version of the slogan is the typed-strategy-space framing already adopted at §4.2.2.

## Pre-1882 anchor (worked example, small)

Gauss 1805's `4×3` vs `3×4` for Pallas (Goldstine §4.12, pp. 251–253) is a worked pre-1882 example of divide-and-conquer FFT with adaptive subdivision choice. L-W-safe by lineage (Gauss 1805 + Euler 1748 + Lagrange 1759). The example is *small*: one paragraph max in §3 or §7, no operation count, no lower-bound implication.

The example anchors the program-facing interpretation; it does not validate a historical thesis. Gauss had a divide-and-conquer FFT and chose subdivisions practically; the search-strategy framing is the program's reading.

## Where this lands in the paper

- **§1.5** — the conversion is a family of strategies, not a fixed map. *(Adopted in current outline.)*
- **§4.2** — the hypothesis class is an adaptive strategy family closed under composition. *(Adopted in current outline.)*
- **§3** (or §7) — pre-1882 worked example via Goldstine + Gauss's Pallas computation. One paragraph max. *Pending: placement and length.*
- **§6.5** — closure class = closure of strategies under composition; smarter-FFT = smarter search. *Pending: decide whether prose adopts strategy-composition language explicitly.*
- **§7 ("back again")** — the four canon papers as later asymptotic formalizers of a substrate Gauss had worked. *Pending: short remark if prose earns it.*
- **FIRST-PROOF debt #2** — search-strategy space and topology added to the formalization burden. *(Adopted.)*

## Construction debts the search reading interacts with

Each item below is a candidate; promotion to FIRST-PROOF requires reducing the named debt.

- **Debt #2 expansion.** Search-strategy space and topology need formal specification. Strategy composition algebra. Per-strategy cost decomposition.
- **Debt #5 (Lemma A exhaustiveness) tightening.** The search reading sharpens the exhaustiveness claim: distinguishing information for an adaptive search must come from the search space's structure, which is bounded by canon operations. Possibly admits adversarial / decision-tree-style closure.
- **Debt #6 (A↔B equivalence).** Information route and closure route may converge under the search reading: information that distinguishes search strategies = information that places strategies inside or outside the closure class.

None of these has been promoted to a lemma in FIRST-PROOF. They are candidate moves whose payoff is unverified.

## Slow-promulgation timeline

Don't rewrite. Each step is reversible and conditional on payoff against a named debt.

1. Land the Goldstine + Pallas worked example in §3 (or §7) when the prose pass arrives there. *(Goldstine in References; placement TBD.)*
2. Develop the search-strategy formalization in the prose pass for §1.5 (one paragraph max).
3. Decide whether §6.5's closure-class argument should adopt strategy-composition language explicitly, or stay neutral.
4. If the prose earns it, add a short remark in §7 on the canon as later asymptotic formalizers.
5. If the search reading sharpens Lemma A's exhaustiveness argument enough to reduce debt #5, fold the adversarial / decision-tree closure into the prose at §5.5.

## Pencil marks (parked)

- **Adversarial / decision-tree closure for Lemma A.** *Quarantined.* Decision-tree / oracle language is new proof apparatus, not just vocabulary. Promote only if it produces an actual exhaustiveness lemma for Lemma A; until then, parked.
- **Search-cost vs execution-cost split.** Gauss's adaptive choice (`4×3` vs `3×4`) had near-zero search cost on the Pallas data. Modern FFTs have non-trivial selection overhead. **Caveat:** charging "cost of finding the strategy" requires specifying the model (uniform vs nonuniform; advice-bearing or not; per-instance adaptive or amortized over inputs), since a nonuniform FFT can hardwire strategy and make search cost vanish. Any search-cost/execution-cost split must declare its model.
- **Vocabulary disambiguation.** "Search" in this paper means *adaptive algorithm selection*, not information-theoretic search complexity (decision-tree models, oracle queries) — though the latter may yield bounding tools (see first pencil mark above). Disambiguate in prose at first use.
- **Anchor expansion.** Goldstine §4.12 has more pre-1882 material than Pallas: the two product-to-sum lemmas at p. 245, the discrete Fourier inversion at pp. 246–247, the aliasing identity at p. 248. Each could anchor specific subsections of §3 or §5 if prose earns it.
- **Forbid-search-vs-forbid-technique as candidate §6 spine.** Slogan: forbidding search is easier than forbidding technique because search has structure. Admissible lemma version: "the hypothesis class is a typed strategy space closed under composition" (already adopted at §4.2.2). Whether the slogan promotes to a §6 argument shape depends on whether it reduces a named debt — currently it does not.
- **Connection to NATIVE-F.** *Quarantined.* The closure-mismatch theorem is a forbid-functor argument on the algebraic side. The search-reading forbid-search argument on the operational side may be structurally parallel: both forbid extension of a closure class via finite composition. Worth checking whether NATIVE-F's argument transports as a search-side forbid — but only if the transport produces a usable lemma, not just an analogy.

## Trust boundary

This file is exploratory. Pencil marks here are not yet construction debts in FIRST-PROOF — they're candidate moves whose payoff is unverified. When a pencil mark earns its way into the proof, it migrates to FIRST-PROOF as a debt or a step. Until then, it stays here.

Goldstine's source content (§4.12–13) is L-W-safe per the brief's audit. Gauss 1805 + Euler 1748 + Lagrange 1759 are pre-Lindemann; Goldstine 1977's exposition adds no transcendence content. The pre-1882 anchor is honest as a worked example.
