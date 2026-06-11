## RRU Close Reading Report

**Document:** paper/PAPER.md (untitled — the document has no title line; first heading is `## Abstract`)
**Date:** 2026-06-11
**Token budget:** ~90k base / ~104k with remediation reserve (parser scaffold corrected by hand: H2 units treated as main sections)
**Sections flagged for remediation:** none (all eleven main sections carry anchored observations)
**Adaptation:** Adaptation 2 (outline-stage), nonstandard variant — near-complete prose split one sentence per block, tagged with `NOTX`/`RHETOR`/`INTERNAL`/`SIGNPOST`/`HEDGE`. "Sections" below are H2 units; "paragraphs" are H3 sentence-runs. Stub analysis replaced by debt-ledger reconciliation, since the document carries its own promise ledger (the Construction-debt ledger, designated "not paper content").

### Promise Ledger (from orientation)

| # | Promise | Section |
|---|---------|---------|
| P1 | "We prove this heterogeneity is structural" / FFT-style methods "cannot improve past those thresholds" | Abstract, §Intro.1 |
| P2 | Theorem K "certifies that the cyclotomic-ladder degree, polygon perimeter, and isoperimetric gap rate are unrecoverable from Farey coordinates" | Abstract, §5.6 |
| P3 | "Non-nesting ... blocks free conversion across measure-theoretic registers" | Abstract, §5.2/§6.6 |
| P4 | "forecloses the F-side coordinate channel and the cross-register channel" | Abstract, §6.6 |
| P5 | "Extension to behaviorally-equivalent algorithms meets Rice's theorem, and we locate that horizon precisely" | Abstract, §Conclusion |
| P6 | "The proof carries three objects at three evidentiary standards" (earned/committed/owed) | §Intro.3 |
| P7 | "§3.6.2 demonstrates currency-stratification on both sides" | §Intro.2, §3.6.2 |
| P8 | "M does not prove a lower bound on P improving past the existing threshold T(P)" | §4.5 |

Reconciliation: P2 delivered (proof in companion form; witnesses verified arithmetically). P6 delivered structurally — the device works. P7 delivered for one worked pair (Morgenstern↔Ailon), generalized by definition. P3/P4 delivered conditionally on T4b (debt #1). P5 delivered modulo a likely-wrong recursion-theoretic classification. P1/P8 not deliverable as phrased — see Promise Issues.

### Section Classifications

| Section | Classification | Notes |
|---------|----------------|-------|
| Abstract | promise-bearing | claims the theorem unconditionally |
| §Intro | promise-bearing | carries the earned/committed/owed contract |
| §1 | promise-bearing | incurs debts #2, #9, #13 definitionally |
| §2 | promise-bearing | rhetorical overture; 17/23 blocks `RHETOR`; informationally redundant |
| §3 | promise-bearing | survey + the load-bearing §3.6.2 structural claim |
| §4 | promise-bearing | theorem, class, chase |
| §5 | supporting | substrate facts; pays P2 |
| §6 | promise-bearing | incurs the largest debts (T4b, endpoint) while composing |
| §7 | supporting | self-declared "sibling reading, not load-bearing" |
| §Conclusion | promise-bearing | Rice horizon claim |
| Figures / References | paratext | annotated references consulted, not close-read |
| Construction-debt ledger | designated working paratext | "Outline-only — not paper content"; used for reconciliation |

### Issues

#### Warrant Issues
- **The method/proof equivocation — the paper's deepest gap.** The theorem is stated in proof-method language ("M does not prove a lower bound on P improving past T(P)", §4.5) but the class M ranges over is defined as computations ("finite compositions of the native operations", §4.2.3), and §6 argues in algorithm language ("the algorithm must drive δ ... toward zero", §6.2). The bridge is one unsupported sentence: "Lower-bound improvement *is* successful descent" (§6.1, line 763). Two different theorems are in superposition: (A) the canon thresholds extend as cost lower bounds to the whole FFT-style class (algorithms can't compute below them, even with cross-currency trades), and (B) a barrier theorem (FFT-style proof techniques can't establish stronger bounds). §4.5's "Equivalently:" yokes them together inside the theorem statement itself. — Anchors: §4.5 lines 517–519; §6.1 line 763; §6.2 line 779.
- **Aims→validity slide at the canon reading's root.** "None of the four targets another's regime or currency, and that non-transfer is what §3.6 unpacks" (§3.1) — "targets" (intent) becomes "non-transfer" (impossibility) with one worked witness pair (Morgenstern↔Ailon), then full generality by definition ("Every such transfer is exactly what §1.6 calls δ", line 371). Defensible as framework; currently silent. — Anchors: §3.1 line 276; §3.6.2 line 371.
- **Definitional-escape adjacency in the smarter-FFT rebuttal.** "'Smarter FFT' therefore collapses to 'FFT-style method plus machinery outside the canon's stack'" (§6.6 line 1035) — whatever beats the class is defined out of the class; ledger #11 concedes the missing exhaustiveness while body line 1013 claims the rebuttal "upgrades from posture to content." The ledger is more honest than the body here. — Anchors: §6.6 lines 1013, 1035; ledger row 11.
- **Recursion-theoretic classification likely mis-stated.** "(Σ⁰₁ set whose Π⁰₁ complement is the halting set up to a recursion-theoretic translation)" — behavioral equivalence to a class member is ∃M∀x-shaped (Σ⁰₂-flavored), not Σ⁰₁; P5's "precisely" rests on this parenthetical. — Anchor: §Conclusion line 1143.
- **Audit-as-fact.** "no admissible method extracts additional descent information" (§5.5 line 691) asserts an off-paper audit's conclusion with undefined scope ("auxiliary-tool repertoire"). — Anchor: §5.5 line 691.
- **"Adjacent" not actually pinned.** "'Adjacent' pinned down: compute-cost problems sharing §1's cost / conversion structure" — a gesture, not a definition; §4.5 quantifies over P, so theorem scope inherits the vagueness. — Anchor: §4.3 line 491.

#### Purpose Issues
- **§2 is a second introduction.** All informational content restated elsewhere; function purely rhythmic. Keep as essayistic overture or merge its three best kernels into §Intro — currently the paper pays for both §Intro and §2. — Anchors: §2 lines 216–262.
- **§4.7 duplicates §6's architecture block-for-block** (575–617 vs 859–1005) — the third full pass over the door/clause/witness mapping. — Anchors: §4.7, §6.4.
- **§5.1 feeds nothing downstream.** By §5.6's own kernel partition it is non-direct ("lives on T = ℝ/ℤ, not on L"); it closes no door and witnesses no clause. Candidate for demotion to a remark in §5.6. — Anchors: §5.1 lines 625–633; §5.6 line 739.
- **§7 ends on bookkeeping** ("[Construction debt #6 ...]") — a resonance section closing on a ledger bracket. — Anchor: §7 lines 1115–1117.
- **§5.3 breaks §5's discipline** — "Descent reaches them only at threshold" is a §6-grade conclusion inside a typing section; §5.2 explicitly forbids itself the same move ("§5.2 delivers substrate-side typing only"). — Anchors: §5.3 line 665; §5.2 line 659.

#### Promise Issues
- **The abstract claims a theorem; the body delivers a conditional composition plus a research program.** "We prove this heterogeneity is structural" / "cannot improve past those thresholds" vs "QED for §4 once (b)–(c) are earned and (9) reconciles" (§6.6 line 1043) and a fifteen-row debt ledger with #1, #3, #5, #9(c), #11, #12 open. The word "conditional" does not appear in the abstract. The abstract even reproduces the gap internally: sentence 3 claims the full impossibility, sentence 8 honestly claims only two channels foreclosed. — Anchors: Abstract lines 5–7, 17; §6.6 lines 1011, 1043; ledger.
- **Conditionality trails the proof-walk.** §6.6 narrates the composition (985–1009) as if (a)–(c) were available and states the conditions at line 1011, after the QED-shaped sequence. — Anchor: §6.6.
- **Stale internal promise:** §3.6.2 promises "§6.6's (a)–(d) composition" (line 375); §6.6 composes (a)–(c) (977–981). — Anchors: §3.6.2 line 375; §6.6 lines 977–981.
- **Vagrant promise:** "sharpened by the manifold framing" (§Conclusion line 1161) — no manifold framing exists in the paper (sole occurrence of "manifold").
- **Evidence delivered and used well (positive):** Theorem K's witnesses check out arithmetically (f₁(1,5)=2≠4=f₁(3,15); L₃=3√3≠6=L₆); the canon summaries §3.2–§3.5 are accurate (det n^{n/2}, μ(T_P)=2n−k, Φ(F)=n log n).

#### Repetition Issues
- **The door/clause/witness mapping is narrated in full at least five times** (§4.6, §4.7, §6.3, §6.4, §6.6, plus the §5 section openers). Counts: "door" ×14, "currency-stratification" ×13, "(Z, ℱ, μ" ×13, "Morgenstern↔Ailon" ×8, "per §3.6.2" ×5. In ledger format this is auditability; in prose it will be monotony. One door→clause→witness→section table (modeled on §3.6.1's existing table) should carry the mapping once, with every other site reduced to a reference. — Anchors: §4.6 543–557; §6.4 859–901; §6.6 993–1005.
- **Verbatim self-repetition unmarked as callback:** "Lower bounds are not numbers. / They are measurements made in particular coordinate systems" at §Intro.2 (60–62) and §3.6.2 (405–407).
- **Ailon 2013 introduced at full length three times** (§1.3.2, §3.7, §7).
- **Template rigidity in §5** ("Source-side typing per measure/SUBSTRATE-OBSTRUCTIONS.md §N" ×5) and §6.4 ("X → clause (Y)" ×4): the §6.4 instance should become a table; the §5 instance needs prose variation.

#### Terminology Issues
- **Symbol collision, referee-visible:** μ = multiplicative cost (§1.3, line 108) and μ = the measure in (Z, ℱ, μ) (§6.3, line 815). Both load-bearing.
- **Undefined in-paper:** "K2" (733, 867); "L-W" never expanded (691); "route-3" in body prose (1011); "Landfall" (955); "K-H-L-A" (1127); "A1–A4" named never stated (1089); "auxiliary-tool repertoire" (691).
- **T4b without T4a:** T4b used from §Intro.3; T4a appears only in the ledger's earned-list (1320). Readers will hunt for the sibling.
- **Program-internal idiom in paper prose:** "iso/ registers" (directory slash as adjective); "ALGEBRA-OF-DELTA sub-question (8)" (783) cites a memo's internal numbering.
- **Format-induced fracture:** sentence-splitting breaks real syntactic units — parentheticals split across blocks at 146–148, 377–381, 433–435, 537–539, 561–563, 577–579, 619–621, 693–695, 725–729, 783–785, 795–797, 815–819; a bold span opens at 176 and closes at 182 across four blocks (renders as literal asterisks). The unit the tags govern is violated in ~15+ places.

### Patterns That Serve
- **The earned/committed/owed device (§Intro.3) is the paper's best structural innovation** — three evidentiary standards declared up front, then tracked. It should be promoted (into the abstract's frame), not diluted.
- **The chase (§4.6).** Staking the theorem with a worked specimen adversary before earning it is genuinely engaging and reviewer-friendly; "The adversary is artificial" (559) is the right honesty at the right moment.
- **§3.6.1's five-coordinate table** is the model the rest of the apparatus should imitate.
- **Trust-boundary discipline around Ailon (§3.7)** — "It is not a broad FFT lower bound and not a proof of the program's δ" — is exactly how to cite adjacent prior art.
- **Kernel sentences the format has already surfaced:** "Without (8) the two halves are independent claims sharing a label" (787); "The heterogeneity was the circle showing through" (1061); "The FFT is the conversion of multiplication and addition on the circle" (218).
- The `RHETOR` tag is functioning as a cuttable-mass detector: §2 (17/23) and §6 (×37) light up exactly where prose-pass compression is needed.

### Completion Diagnostic Summary
First diagnostic run flagged three coverage gaps against the script's own (mis-parsed) three-section scaffold: "Abstract" (= entire body), "Figures", "Construction-debt ledger". Mandatory remediation re-reads performed on all three targets despite artifact status; they produced three new anchored findings now in the log: (1) §3.6.1's closing blocks concede every §4.4 threshold awaits re-verification under the paper's own cost model (debt #9(c)) and §4.4 doesn't say so locally; (2) "theorem-paired" in the Figures framing sentence overclaims (the table pairs figures to sections); (3) the ledger's status vocabulary is uncontrolled (~7 informal statuses vs the declared three-way "proven, resolved, or absorbed"). Residual coverage flags after re-read are parse artifacts, reported as-is.

Parser scaffold required manual correction (body uses H2/H3 with H1 only in back matter, so the script rolled §Intro–§Conclusion under "Abstract"); coverage was therefore reconciled by hand against the corrected section list: all eleven main sections carry ≥1 anchored observation; no remediation re-reads required. Promise ledger reconciled above (P1–P8 each dispositioned). Promise-bearing sections received the double forward exposure; §5/§7 single. Repetition observations span §1–§7 (not clustered). Stub-section category (Adaptation 2): the genuinely stub-like units are the missing title, §4.4's "Named precisely. / Cited to §3.", and §Conclusion's "Coda." fragments — everything else owed is owed by declared debt, not by omission, and is tracked in the document's own ledger.
