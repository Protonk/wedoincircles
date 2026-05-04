# Scaffold teardown — the smell

A finished paper is one where the author has left the room. The math is on the page; the reader is alone with it. Scaffolding is what is left when the author is still in the room — narrating, reassuring, counting, restating, defending. Every variety of it is the same gesture under different masks: a protective hand on the work, performed for an audience the paper no longer needs to address — us, the writers.

The smell is *protectiveness*. Watch for the moment a sentence stops doing the math and starts taking care of the doing: explaining its own structure, anticipating an objection no one raised, hedging a precise statement with a blunter restatement, counting items so the reader knows none are missing, pointing forward or backward at itself, naming the discipline that produced it. None of these are claims. They are postures.

Scaffolding helped build the work. Trust boundaries, the ledger, debt-channel exhaustiveness, the program discipline — all load-bearing during construction, all invisible on the finished surface of a paper that trusts itself. A reader of a building does not need the scaffolding; a reader who *can see* the scaffolding assumes the building is unfinished. So every retained methodological gesture, every "we are careful to," every paired precise-then-blunt clause, every numbered self-promise, signals — far from reassuring the reader — that the writer does not yet trust the work to stand on its own.

The same diagnosis explains why repetition fails. Legal-style say-it-thrice is protective ritual: each repeat is insurance against the previous one having missed. The reader given one clean statement gets it. Saying it again broadcasts the writer's anxiety, not the idea's weight.

A working test, applied at the clause level: *who is this sentence for?* If it is for the reader needing this fact, in this place, to follow the argument — keep it. If it is for the writer — assuring themselves the structure is sound, the discipline was kept, the objection is parried, the count is right, the idea was understood — cut it. The math is finished. The discipline is in the proofs. The trust boundary did its job and is no longer needed in the air. Leave the reader alone with the work.

# Plan: surveying the scaffolding

The survey produces two reports. Their synthesis into an edit plan is a later session; that plan's shape is deliberately unspecified here.

1. **Vibes pass.** A single light forward read of the paper. The sensitizer above is the gauge instrument; the clause-level test is the working tool. Anything that smells off is recorded as a short location-tagged comment, in order of encounter, into `## Vibe Report` below. No editing, no rewriting, no decisions during the read. The pass ends when the read ends.

2. **Backwards pass.** Reversal is at the *sub-section* level: walk a section's sub-sections in reverse order; if a section has no sub-sections, read it in forward order. (Paragraph-level reversal is slower and is reserved for when the paper is tighter.) Reversal strips the prose of its forward momentum — which is what hides scaffolding, since a sub-section that "earns" its scaffolding by leading into the next one is exposed as soon as it has to stand alone. The view will differ from the vibe report by agent, context, and direction — not by read intensity. Same recording discipline as pass 1; comments land in `## Backwards Report`.

3. **Condensation.** From the two raw lists, produce a single condensed brief: which sections show concentrated scaffolding, which gestures recur, which surfaces deserve targeted scrutiny. The output is a directed-search prompt — specific enough that a fresh agent, given only the brief and the sensitizer, can run a targeted pass without re-reading the raw notes. Lands in `## Condensation Brief`.

4. **Targeted ID.** A fresh agent, dispatched with the brief plus the sensitizer onto the chosen sections, returns a structured report identifying scaffold elements at clause/sentence resolution. Lands in `## Targeted ID Report`.

The condensation and the targeted ID report are the survey's outputs. They feed the edit plan, in a later session.

# Reports

## Vibe Report

- `paper/PAPER.md:L2-L18` Opening "Notes to be collected" are explicit construction room: self-warnings, project summary, anti-scaffold diagnosis, and process instructions before the paper begins.
- `paper/PAPER.md:L45-L60` §Intro.3 inventories evidentiary statuses and debts before the theorem breathes; reads like ledger protection rather than reader-needed setup.
- `paper/PAPER.md:L60` `[CONNECT]` note breaks the paper surface and says the internal-doc concern directly.
- `paper/PAPER.md:L64-L70` §1 opens with a forward-reference management note and self-location map; the section explains where its own parts will land.
- `paper/PAPER.md:L68-L69` Accounting-stack paragraph names four objects, then immediately guards what `δ` is not and where §1.6 will name its algebra; protective typing posture.
- `paper/PAPER.md:L74-L76` Cost-model paragraph ends by naming "methodological commitment" and remaining work; reads like audit status folded into theorem setup.
- `paper/PAPER.md:L80` Cost-currencies paragraph repeats "not conversion strategies" and points ahead to §1.5/§1.6; useful typing is mixed with anti-confusion scaffolding.
- `paper/PAPER.md:L98` Adaptivity paragraph anticipates an evasion and answers it before the evasion is formally in play.
- `paper/PAPER.md:L102-L104` Transaction-cost section over-explains Coase existence/algebra as "precedent the program inherits" and then itemizes open-work statuses; authorial apparatus visible.
- `paper/PAPER.md:L106-L108` Substrate-side `δ` generalization leans on repo memo content and is followed by a `[CONNECT]` admission that it is not yet paper content.
- `paper/PAPER.md:L112-L114` Candidate cocycle realization is a deep forward reference and the note itself calls out the awkwardness.
- `paper/PAPER.md:L118-L122` Threshold interface packs endpoint commitment, candidate coordinate, biconditional guard, figure-routing, and a `[CONNECT]`; high concentration of self-protection.
- `paper/PAPER.md:L126-L152` §2 repeatedly restates the conversion/failure frame in bolded pieces; the final sentence re-synthesizes four failed routes as one structural fact before the machinery arrives.
- `paper/PAPER.md:L158-L164` §3.1 tells the reader how the five sources should be grouped, then repeats what §3.2-§3.6 will do; strong table-of-contents narration.
- `paper/PAPER.md:L190` Table caption says what "reading down column 4" should make visible; interpretive stage direction.
- `paper/PAPER.md:L196-L198` Ailon/Morgenstern contrast repeats the currency-stratification moral several times in increasingly blunt language.
- `paper/PAPER.md:L214-L222` §3.6 question plus coordinate list plus "point is..." sentence are scaffolded, and the inline note already identifies the stage direction.
- `paper/PAPER.md:L232-L244` Four labeled "structural faces" read like protective enumeration; the parenthetical distinguishes numbering systems for the writer's bookkeeping.
- `paper/PAPER.md:L250-L258` §4.1-§4.2 are placeholder phrases ("Preview in plain language," "Formal version," "The hypothesis class") rather than paper prose.
- `paper/PAPER.md:L270-L277` FFT-style class definition guards against stipulation, future §6.6 narrowing, and ledger movement; defensive scope management dominates.
- `paper/PAPER.md:L297-L301` The theorem is stated, then immediately restated as "Equivalently"; the blunt restatement may be anxiety rather than new content.
- `paper/PAPER.md:L305-L333` §4.6 labels its own adversary as specimen, toy, controlled display, artificial, and narrative scaffolding; this is the densest author-in-room passage so far.
- `paper/PAPER.md:L321-L329` "Three variants" plus "four-attempt span" count-management exposes the construction routing.
- `paper/PAPER.md:L337-L359` Proof outline says "three parts plus a load-bearing transport," contrasts dramatic vs structural versions, and lists debts; roadmap scaffolding is heavy.
- `paper/PAPER.md:L361` §5 heading "A maze of twisting passages, all alike" is rhetorically cute and foregrounds the author's framing hand.
- `paper/PAPER.md:L367-L375` §5.1-§5.2 repeatedly says how §5.6 and §6.4 will read the material; facts are mixed with future-use labels.
- `paper/PAPER.md:L381-L383` §5.3 figure list narrates what each figure "sets up" or "closes"; figure routing instead of a clean embed/caption surface.
- `paper/PAPER.md:L389-L391` §5.4 ties the face to NATIVE-F and then routes to a figure; sibling-structural language feels like internal graph maintenance.
- `paper/PAPER.md:L395-L399` Admissibility envelope names the audit regime and §6 role more than it states a result; "content not calendar" is methodological posture.
- `paper/PAPER.md:L403-L411` Theorem K section surrounds the theorem with door-closing, apparatus-restriction, kernel partition, and open support inventory; proof surface buried in use-context.
- `paper/PAPER.md:L417-L419` §6.1 repeats the descent definition and then narrows quantifiers; protective distinction between algorithm-side and substrate-side currencies.
- `paper/PAPER.md:L423-L429` Endpoint commitment restates existence/implication/bridge, discharge location, biconditional guard, and contradiction use; precise statement plus multiple safety rails.
- `paper/PAPER.md:L433-L445` T4b section announces "single sovereign claim," explains notation collision, states witnesses vs proofs, and gives phase status; much of it is apparatus status.
- `paper/PAPER.md:L449-L457` §6.4 repeatedly says each fact "closes" a door; the proof choreography remains visible clause by clause.
- `paper/PAPER.md:L461-L469` §6.5 labels every item as input/not-parallel/open/conditional; useful ledger, but paper voice has not left the room.
- `paper/PAPER.md:L475-L493` Conditional impossibility composition is followed by exhaustive-case reassurance, floor-extension reassurance, residual list, smarter-FFT rebuttal, field-survey alignment, and QED qualifier; repeated defenses cluster after the argument.
- `paper/PAPER.md:L497-L532` §7 "circle reread" is conceptually polished but repeats "reading/reread" as interpretive instruction; NATIVE-F status and companion role keep construction state visible.
- `paper/PAPER.md:L538` Construction debt flag inside §7 is explicitly not finished-paper prose.
- `paper/PAPER.md:L542-L554` Conclusion outflow repeatedly names horizons, hidden dependencies, handoff cleanliness, and future direction; defensive anti-hand-wave posture.
- `paper/PAPER.md:L556-L571` Figures section is an internal tracking table with "alt-text-ready" and gap status; construction inventory, not reader-facing paper content.
- `paper/PAPER.md:L577-L598` References open with provenance discipline and trust-boundary staging; bibliography entries carry citation-contract prose.
- `paper/PAPER.md:L606-L607` Substrate-side reference entries state trust boundaries and source-side typing roles; references are doing internal graph control.
- `paper/PAPER.md:L659-L683` Construction-debt ledger is overt scaffold and says it will not survive; the final line is a compressed global status report rather than paper content.

## Backwards Report

Backwards pass at sub-section granularity (sub-sections within each section reversed; sections themselves in document order; sectionless sections read forward). Observations below split into single-passage flags and cross-section pattern flags that only surface under reversal.

**Single-passage flags.**

- `paper/PAPER.md:L43` §Intro.2's slogan "Lower bounds are not numbers; they are measurements made in particular coordinate systems" reappears nearly verbatim at L244 inside §3.6.2; same line, two sections, two protective restatements.
- `paper/PAPER.md:L46-L54` §Intro.3 read as the *first* paragraph of §Intro (reversed entry) is striking: the opening of the introduction is a triple-status inventory of paper-local / structurally-discharged / committed / residual content. A reader's first impression of the paper is its construction ledger.
- `paper/PAPER.md:L116-L122` §1.8 read alone: after one declarative sentence, the rest is forward references to §6.2 plus a "biconditional is not claimed" disclaimer plus a figure caption that routes seven internal locations.
- `paper/PAPER.md:L100-L108` §1.6 italic status labels "*Reduced to substrate-side input* / *Closed in spirit* / *Skeleton in hand* / *Separate from the algebra*" are work-progress markers carrying technical content; cut the labels and the technical content survives.
- `paper/PAPER.md:L74` §1.2 "*Uniform* in this paper does not mean Cook–Reckhow constant `l(n) = 1` or van Emde Boas uniform measure" — the negative-definition clause occupies more of the paragraph than the positive definition.
- `paper/PAPER.md:L86-L88` §1.3.2 closes "§3.6.2 develops this as the content claim that currency-stratification is forced." A subsection should not need to tell the reader what its successor will *develop as content*.
- `paper/PAPER.md:L156-L164` §3.1 read last in §3 (reversed exit) exposes its full TOC redundancy: §3.2-§3.6 have just been read, and §3.1's "§3.2 presents..., §3.3, §3.4, §3.5 present..., §3.6 reads..." pre-narrates everything just witnessed.
- `paper/PAPER.md:L198` §3.2 closes "The Morgenstern↔Ailon pair is the field-internal demonstration that the §3.6.2 non-transfer is forced rather than incidental." — meta-claim about the pair's demonstrative role *for the paper*, not the math.
- `paper/PAPER.md:L228-L246` §3.6.2 read as §3's opener (reversed entry) reads as §3's conclusion lifted out: "the shared structure is the stack" lands as a thesis before the lower bounds it summarizes have been seen. The "(i)–(iv) here to keep them distinct from §6.6's (a)–(d)" parenthetical is bookkeeping of the writer's labeling choices, exposed.
- `paper/PAPER.md:L335-L359` §4.7 read as §4's opener (reversed entry) reads as a TOC for §5 and §6 with bolded item labels; the proof outline announces three parts plus a transport before the theorem of §4.5 has been encountered.
- `paper/PAPER.md:L301` §4.5 "Equivalently:" line — the only subsection in the paper containing a formal theorem statement, and the very next sentence is a blunt restatement.
- `paper/PAPER.md:L294` §4.4 closes with a debt-pointer to §6.3's currency-universal limit; closure of §4.4 ought to be definitional, not promissory.
- `paper/PAPER.md:L281-L286` §4.3 reads as three slide-bullets ("The problem class." / "Cyclotomic-DFT specifically..." / "'Adjacent' pinned down: ...") rather than connected prose. Same shape as §4.1-§4.2 already flagged.
- `paper/PAPER.md:L401-L411` §5.6 read as §5's opener (reversed entry): the theorem statement is clean; the "**Kernel partition.**" block then re-categorizes every prior §5 subsection in §5.6's vocabulary. T1, T2, T3 supports carry "open" status labels in the body.
- `paper/PAPER.md:L399` §5.5's closing clause "size-dependent shortcuts are out-of-class unless paid at the same granularity" lands the section's operational content in §6.5 and §4.2.1 vocabulary borrowed from elsewhere.
- `paper/PAPER.md:L387` §5.4's "Native operations cannot bridge the asymmetry: they live in a closure system whose depth is constant against a substrate whose depth is unbounded." — a §6 conclusion stated inside a §5 substrate-fact subsection.
- `paper/PAPER.md:L473-L483` §6.6 opens with an (a)/(b)/(c) inventory of §6.4/§6.3+§6.5/§6.2 contents, and the next paragraph re-deploys each by clause label; two consecutive paragraphs each name the cast list.
- `paper/PAPER.md:L487-L491` §6.6 closes with the "smarter-FFT rebuttal" italic label, "Coase 1937 supplies the *reduce yes, eliminate no* vocabulary" slogan, and "The obstruction is structural, not in algorithmic cleverness" thesis-restatement; three protective gestures stacked at the section's exit.
- `paper/PAPER.md:L493` §6.6's "QED for §4 once the three named residuals close" — the QED line carries debt status. The QED is conditional on its own ledger being closed.
- `paper/PAPER.md:L425-L427` §6.2's bridge is named three different ways in two paragraphs ("the load-bearing move," "the at-threshold-to-past-threshold step," "the bridge to T4b"). Anxiety-shaped repetition.
- `paper/PAPER.md:L419` §6.1's second sentence is a preemptive scope clarification: "The currency-by-currency quantifier here is over *algorithm-side* cost currencies (`μ`, `α`). Substrate-side iso/ currencies ... feed in as facts ... not as additional axes §6 quantifies over."
- `paper/PAPER.md:L536` §7 "The companion role is what NATIVE-F's own memo claims for itself ('structural rhyme, not theorem dependency', per `memos/NATIVE-F-MINIMAL-DEFINITION.md` §Methodological note); the present outline aligns with that scope." — the paper cites a memo's claim about the paper's relationship with the memo.
- `paper/PAPER.md:L548` §Conclusion has paired threes: "the FFT-style class fixed at §4.2, the operational cost-norm committed at §6.5, the δ-algebra realized at the §1.7 cocycle coordinate" mapped to "debt #3, debt #9(c), and the qualitative-rigor sharpening of `f_{ca}`'s type-gap (Phase 1c residual)" — counted commitments against counted residuals in one paragraph.
- `paper/PAPER.md:L554` §Conclusion's final line "Clean handoff, not vague future work." — single-sentence defensive closer asserting what the conclusion is NOT.

**Cross-section pattern flags** (visible only under reversal — a sub-section that "earns" a gesture by handing forward gets exposed as soon as it has to stand alone next to its peers).

- The **T4b clause↔witness↔door triple** is encoded four times: §4.7's proof-outline bullets (L341-L355), §6.3's faithfulness clauses with inline witness-and-door tags (L441-L443), §6.4's bolded paragraph headings (L451-L457), and §6.6's case enumeration (L479). Four sites for one mapping.
- The **§5 face-classification doubling**: every §5 subsection (L367, L375, L381, L389, L399) closes with "§5.6's kernel partition reads §5.X as ...", and §5.6 (L409) re-enumerates the same classification. The categorization happens twice — once in each face's voice, once as §5.6's table.
- The **Coasean frame** is named in §Intro.2, §1.6, §3.6.2, §6.2, §6.3, §6.6, §7 — every body section past §1 carries Coase-vocabulary as recurring chrome.
- **Debt enumerations** in body prose: §4.6 (L329, L333), §4.7 (L359), §6.3 (L445), §6.5 (L463, L465, L467, L469), §6.6 (L481, L483, L485), §7 (L538), §Conclusion (L544, L548). Debts read as paper content rather than ledger content across nearly every late section.
- **Internal-doc routing in body prose** is frequent past §4: `paper/T4B-DECOMPOSITION.md`, `measure/THE-FIRST-BRIDGE.md`, `measure/CURRENCY-MORPHISMS.md`, `measure/ENDPOINT-COMMITMENT.md`, `fft/COCYCLE-COMPOSITION-LAW.md`, `fft/PHASE-DEFECT.md`, `fft/PHASE-LIFT-CONSERVATIVITY-AUDIT.md`, `fft/LANDFALL-EXTENDED-CAFF-TRANSFER.md`, `memos/AMORTIZATION-AT-THE-BOUNDARY.md`, `memos/EFFECTIVE-HL-N1-COST-FORM.md` — repo paths are quoted into the prose surface where a paper would normally cite a published reference or a labelled appendix.
- **Bolded TOC labels in prose-only sections**: §2 (three), §4.6 (two), §4.7 (four), §6.6 (none, but italic labels), §7 (five), §Conclusion (three). Prose paragraphs are organized by sub-section labels in sections that have no formal sub-sections.
- **"Sibling structural reading" / NATIVE-F not-load-bearing disclaimer** appears in §Intro.3 (L56), §3.6.2 (L246), §4.7 (L357), §6.6 (L475), §7 (L530), §Conclusion (via §552's algebraic-side reference). Six restatements that NATIVE-F is companion-not-load-bearing — a single fact maintained by recurring disclaimer.
- **"Per §X.Y" mid-clause forward/back-references** are denser per paragraph in §6 than in §1-§5. §6.3-§6.6 paragraphs frequently carry three or more inter-section pointers each, turning prose into an index.

## Condensation Brief

The forward and reverse reads converge: the paper has a small, well-defined catalog of scaffolding gestures, distributed unevenly. A few sections are saturated; many sections carry one or two recurring tics; a few surfaces (figures, references, the debt ledger, the pre-paper notes block) are construction-room artifacts that the targeted pass can flag wholesale rather than clause by clause. The work below is organized so a fresh agent can run a directed sweep without reading the raw notes.

### A. Sections where scaffolding concentrates (rank-ordered for the targeted pass)

**Top tier — saturated; assume scaffolding until proven otherwise.**

1. `paper/PAPER.md:L1-L20` — the "Notes to be collected" block. Pre-paper, entirely construction-room: self-warnings (`[NOTE 1]`–`[NOTE 5]`, `[N.B. 4]`), explicit anti-scaffold diagnosis, project-summary paragraph at L6, "this paper" → "we" memo at L18. Not paper content.
2. `paper/PAPER.md:L303-L333` — §4.6 "The chase: a worked adversary." Densest author-in-room passage in the body. Self-labels its own adversary as *specimen*, *toy*, *controlled display*, *artificial*, *narrative scaffolding*; counts "three variants" and a "four-attempt span"; closes with a debt-enumeration paragraph (#11, #13, #2(8)) explaining what `M_FR`'s failure does *not* prove. Two `[NOTE §4.6]` insertions (L311, L319) are explicit construction-state.
3. `paper/PAPER.md:L335-L359` — §4.7 "Proof outline." Roadmap scaffolding, by definition. Announces "three parts plus a load-bearing transport"; bolded TOC labels (Substrate-side witness package / T4b / Substrate-side facts / Inputs T4b consumes / Conditional impossibility); closes with the NATIVE-F not-load-bearing disclaimer and a "working ledger at end of document (outline-only; not paper content)" line.
4. `paper/PAPER.md:L473-L493` — §6.6 "Conditional impossibility." Opens with an (a)/(b)/(c) inventory of what §6.4/§6.5/§6.3 supplied, then re-deploys each by clause label in the next paragraph; closes with three protective stacked gestures — smarter-FFT rebuttal, Coasean *reduce yes, eliminate no* slogan, "obstruction is structural, not in algorithmic cleverness" thesis-restatement — followed by a QED line whose own clause carries debt status (L493).
5. `paper/PAPER.md:L45-L60` — §Intro.3 "What's earned, what's committed, what's owed." Triple-status evidentiary ledger (paper-local / structurally discharged / committed / residual) as the third paragraph of the introduction. Italic labels carry technical content but read as project bookkeeping. Closes with a `[CONNECT]` (L60) saying the internal-doc concern out loud.
6. `paper/PAPER.md:L116-L122` — §1.8 threshold interface. After one declarative sentence the rest is forward references (§6.2), a biconditional-not-claimed disclaimer, a figure caption that routes seven internal locations, and a `[CONNECT]`. High packing density of self-protection.
7. `paper/PAPER.md:L156-L164` — §3.1. Pre-narrates §3.2-§3.6 content; the agent should read this *after* §3.6.2 to feel the redundancy.
8. `paper/PAPER.md:L401-L411` — §5.6 "Kernel partition" block. Re-enumerates every §5 sub-section in §5.6's vocabulary after the section has already done it once.

**Construction-room surfaces — flag wholesale, do not chase clauses.**

9. `paper/PAPER.md:L250-L286` — §4.1, §4.2, §4.3 are placeholder phrases ("Preview in plain language," "Formal version," "The hypothesis class"); §4.3 reads as three slide-bullets, not connected prose. Drafty surface, not retained scaffolding.
10. `paper/PAPER.md:L556-L571` — Figures section: internal tracking table with "alt-text-ready" and gap status.
11. `paper/PAPER.md:L577-L607` — References open with provenance-discipline / trust-boundary / source-side-typing prose.
12. `paper/PAPER.md:L659-L683` — Construction-debt ledger; explicitly flagged as not surviving.

**Mid tier — one or two saturating gestures inside otherwise-working prose.**

13. §1.1-§1.6 (`L66-L108`): forward-reference management (L64, L70, L76), negative-definition clauses (L74 "Uniform … does not mean …" longer than the positive definition), italic status labels (L100-L108: *Reduced to substrate-side input* / *Closed in spirit* / *Skeleton in hand* / *Separate from the algebra*), `δ`-is-not guards (L68).
14. §3.6.2 (`L228-L246`): "(i)–(iv) here to keep them distinct from §6.6's (a)–(d)" parenthetical = writer's labeling-system bookkeeping; "Lower bounds are not numbers; they are measurements made in particular coordinate systems" repeats verbatim from L43.
15. §4.4-§4.5 (`L294-L301`): debt-pointer at §4.4's close (currency-universal limit forward-reference); the "Equivalently:" blunt restatement after the formal theorem at L301 — the *only* formal theorem statement in the body, immediately reglossed.
16. §5.1-§5.5 (`L367, L375, L381, L387, L389, L399`): every sub-section closes (or contains) a "§5.6's kernel partition reads §5.X as …" tag. Same classification stated twice — once in each face's voice, once as §5.6's table. L387 lifts a §6 conclusion ("Native operations cannot bridge the asymmetry…") into a §5 substrate-fact subsection.
17. §6.1-§6.5 (`L417-L469`): preemptive scope clarification at L419 (algorithm-side vs substrate-side quantifier); bridge-named-three-ways at L425-L427 ("the load-bearing move," "the at-threshold-to-past-threshold step," "the bridge to T4b"); T4b paragraph announces "single sovereign claim" and explains notation collision (L433-L445); §6.4 paragraph headings each say "closes" a door (L449-L457); §6.5 input/not-parallel/open/conditional ledger labels (L461-L469).
18. §7 (`L497-L538`): "circle reread" interpretive instruction repeats; bolded TOC labels in a prose-only section (five of them); paper cites NATIVE-F memo's claim about the paper's relationship to the memo (L536); explicit construction-debt flag in body prose (L538).
19. §Conclusion (`L542-L554`): paired threes — three syntactic commitments mapped to three residuals (L548); single-sentence defensive closer "Clean handoff, not vague future work." (L554) asserting what the conclusion is *not*.

### B. Recurring gestures — a taxonomy the agent should grep for

The agent should treat each gesture as a *family* and report instances by family rather than by location, so the edit plan can decide policy per family.

1. **Internal-doc piercings (`[CONNECT]`, `[NOTE §X]`, `[NOTE N]`, `[N.B.]`, `[Construction debt #N: …]`).** Direct rupture of paper surface. Locations: L4, L8, L10, L12, L14, L60, L64, L70, L76, L311, L319, L538 (+ the entire L1-L20 block). Cut wholly; no clause work.
2. **NATIVE-F "sibling structural reading / not load-bearing" disclaimer.** Six restatements of one fact — L56, L246, L357, L475, L530, L552. A single fact maintained by recurring disclaimer.
3. **Coasean frame name-drops.** Coase appears in §Intro.2, §1.6, §3.6.2, §6.2, §6.3, §6.6, §7. Several are operative; many are chrome (e.g. L491 "Coase 1937 supplies the *reduce yes, eliminate no* vocabulary"). The pass should distinguish working uses from slogan uses.
4. **Debt-number enumerations in body prose (#3, #9(c), #11, #13, #14, #2(8), Phase 1c residual).** L329, L333, L359, L445, L463-L469, L481-L485, L538, L544, L548. Debts read as paper content rather than ledger content.
5. **Repo-path citations in prose.** `paper/T4B-DECOMPOSITION.md`, `measure/THE-FIRST-BRIDGE.md`, `measure/CURRENCY-MORPHISMS.md`, `measure/ENDPOINT-COMMITMENT.md`, `fft/COCYCLE-COMPOSITION-LAW.md`, `fft/PHASE-DEFECT.md`, `fft/PHASE-LIFT-CONSERVATIVITY-AUDIT.md`, `fft/LANDFALL-EXTENDED-CAFF-TRANSFER.md`, `memos/AMORTIZATION-AT-THE-BOUNDARY.md`, `memos/EFFECTIVE-HL-N1-COST-FORM.md`, `memos/OLD-TIME-RELIGION.md`, `memos/NATIVE-F-MINIMAL-DEFINITION.md`, `paper/code/COASE-PHASE.md`. Densest in §6.3-§6.6 and §7. The repo path is occupying the slot a published reference would.
6. **Per-§X.Y forward/back-references mid-clause.** Densest in §6.3-§6.6 (three or more pointers per paragraph), turning prose into an index.
7. **TOC narration in prose-only sections.** §2 (three bolded labels), §3.1 (TOC of §3.2-§3.6), §4.6 (two bold labels), §4.7 (four bold labels), §5.6 kernel partition, §6.6 a/b/c inventory, §7 (five bold labels), §Conclusion (three bold labels). Paragraphs organized by sub-section labels in sections without sub-sections.
8. **Counted enumerations as reassurance.** "Three variants" (L321), "four-attempt span" (L329), "three parts plus a load-bearing transport" (L337), "Three direct K2 instances / Two non-direct faces / One measure operation" (L409), "paired threes" (L548), "five sources" (Intro.2 / §3.1 / §7).
9. **Precise-then-blunt restatement (legal-style say-it-twice).** L301 "Equivalently:" after the theorem; L425-L427 bridge named three ways in two paragraphs; L43 ↔ L244 verbatim slogan repeat; §3.2 closing meta-claim about the Morgenstern↔Ailon pair's "demonstrative role."
10. **Negative definition / preemptive scope clarification.** L68 "`δ` is not a synonym for the mult/add conversion"; L74 "*Uniform* in this paper does not mean Cook–Reckhow constant `l(n) = 1` or van Emde Boas uniform measure"; L80 "not conversion strategies"; L419 preemptive algorithm-side / substrate-side quantifier guard; L122 "biconditional is not claimed"; L554 "Clean handoff, not vague future work."
11. **Italic status labels carrying content.** *Paper-local facts* / *Structurally discharged apparatus* / *Committed* / *Residual conditions* (§Intro.3); *Reduced to substrate-side input* / *Closed in spirit* / *Skeleton in hand* / *Separate from the algebra* (§1.6); "*proved here in companion form*" parentheticals throughout. Test: cut the label, does the technical content survive? Almost always yes.
12. **Stage-direction captions.** L190 "reading down column 4" tells the reader what to see; figure captions throughout route to internal locations rather than describing what is in the figure.
13. **T4b clause↔witness↔door triple, restated four times.** §4.7 proof-outline bullets (L341-L355), §6.3 faithfulness clauses with inline witness-and-door tags (L441-L443), §6.4 bolded paragraph headings (L451-L457), §6.6 case enumeration (L479). Four sites, one mapping.
14. **§5 face-classification doubling.** Each §5 sub-section closes "§5.6's kernel partition reads §5.X as …"; §5.6 then re-enumerates the same partition. The categorization happens twice, once in each direction.

### C. Clause-level scrutiny — surfaces where the targeted agent should work line-by-line

These are the surfaces where wholesale flagging is wrong: the technical content is real and load-bearing, but each clause needs the *who-is-this-for* test applied. Listed in document order.

- `L43` ↔ `L244` — slogan duplication. Decide a single home; cut the other.
- `L46-L54` — §Intro.3's three italic-labeled buckets. Each bucket carries technical claims, but the bucketization is project-internal.
- `L68-L70` — §1.1 closing sentence. The negative-typing posture ("`δ` is not a synonym for the mult/add conversion. It is a typed object that ranges across both …; §1.6 names how it ranges and what its algebra owes.") mixes definition with promise.
- `L74` — §1.2's negative-definition clause; the methodological-commitment phrase at the end.
- `L98` — §1.5 adaptivity paragraph anticipates an evasion not formally in play.
- `L100-L108` — §1.6 italic status labels (four of them), each preceding a real fact.
- `L118-L122` — §1.8 entire sub-section.
- `L196-L198` — §3.2 currency-stratification moral, restated in three increasingly blunt versions.
- `L214-L222` — §3.6 question-list-then-"point is" structure (the inline note already names the stage direction).
- `L232-L244` — §3.6.2 four labeled "structural faces" (i)-(iv); the parenthetical at L246 distinguishing numbering systems.
- `L270-L277` — §4.2 FFT-style class definition; defensive scope-management dominates.
- `L297-L301` — §4.5 theorem + "Equivalently:" line. The blunt restatement is the cleanest test case in the paper for the precise-then-blunt diagnosis.
- `L305-L333` — §4.6 entire sub-section. Specimen/toy/controlled-display/artificial/narrative-scaffolding self-labels; the "**Three variants foreshadowed for §5 to dispatch**" header; the closing paragraph that enumerates which debts `M_FR`'s failure does *not* close.
- `L337-L359` — §4.7 entire sub-section; especially the bolded TOC labels and the closing NATIVE-F disclaimer + debt-ledger pointer.
- `L367, L375, L381, L389, L399` — closing or near-closing tags in each §5 sub-section pointing to §5.6's kernel partition. Decide whether the partition lives in §5.X or in §5.6, not both.
- `L387` — §5.4 sentence "Native operations cannot bridge the asymmetry: they live in a closure system whose depth is constant against a substrate whose depth is unbounded." A §6 conclusion stated inside a §5 substrate-fact sub-section.
- `L395-L399` — §5.5 admissibility-envelope paragraph names "audit regime" and "§6 role" more than it states a result. "Content not calendar" is methodological posture.
- `L403-L411` — §5.6 surrounding prose around Theorem K (the theorem statement itself is clean): door-closing language at L403, the kernel-partition re-enumeration at L409.
- `L417-L419` — §6.1's second sentence (preemptive quantifier-scope clarification).
- `L423-L429` — §6.2 endpoint-commitment paragraph. Existence/implication/bridge / discharge-location / biconditional-guard / contradiction-use stacked.
- `L433-L445` — §6.3 T4b paragraphs. "Single sovereign claim" announcement, notation-collision explanation, witnesses-vs-proofs distinction, phase-status sentence.
- `L449-L457` — §6.4 each-fact-closes-a-door choreography in bolded paragraph headings.
- `L461-L469` — §6.5 paragraphs each opening with a label (Operational cost-norm / Amortization conjecture / Substrate-side input / Candidate transport) and each tagging the item as input/not-parallel/open/conditional.
- `L475-L491` — §6.6 (a)/(b)/(c) inventory + smarter-FFT rebuttal paragraph + Coase-vocabulary / "obstruction is structural" closing thesis-restatement.
- `L493` — QED line carrying debt-conditional status.
- `L497-L536` — §7 "reading/reread" interpretive instruction repeats; the L536 sentence citing NATIVE-F's memo's self-claim about the memo's relation to the paper.
- `L542-L554` — §Conclusion. The L548 paired-threes paragraph (counted commitments vs counted residuals); L554 "Clean handoff, not vague future work."

### D. Sensitizer reminders for the targeted pass

Three calibration points the agent should keep in working memory:

- **The `[CONNECT]` / `[NOTE §X]` / italic status label / "Construction debt #N" markup is the cheapest tell.** When in doubt about whether a passage is scaffolding, check whether construction-state markup is nearby; it usually is.
- **The "*who is this sentence for?*" test bites hardest on closing/transition sentences.** Many sub-sections end with a sentence that points forward, points back, names what the section "does," names what closes a door, or asserts what the section is *not*. These are scaffolding by default.
- **Repetition is the second-cheapest tell.** Anything stated twice (slogan, mapping, classification, disclaimer, count) is a candidate for one-instance retention. The T4b clause-witness-door triple, the NATIVE-F disclaimer, the §5.6 partition, and the L43/L244 slogan are the four loudest cases.

## Targeted ID Report

*Empty; gated on completion of the condensation brief.*

# Teardown plan

Three phases on the survey, each gated on the prior; one verification read at the end.

1. **Bulk removals.** Excise the wholesale-flagged surfaces. Mechanical: cut, stitch the seam, move on.
2. **Single-home collapses.** For each repeated gesture, pick its one home and cut the others. Must precede phase 3 — otherwise polished prose gets cut.
3. **Clause-level edits.** Apply the *who-is-this-sentence-for?* test on what survives, sub-section by sub-section.

Verification: a sober forward read. Done when the sensitizer would catch nothing.
