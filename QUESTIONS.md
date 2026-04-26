## 1

In `memos/COUNTING-APPARATUS.md` the program's most uncertain ambition is that `|M_N|` — the length of the outside-out corner-sweep word — is the compute-cost ledger for a circle-side lower bound paralleling Landfall's log-side result. The `(D)` n=7 walkthrough records an honest negative finding: length-of-`M_N` does **not** localize the Gauss–Wantzel algebraic-depth break at n=7. Step increments Δ`|M_n|` across n=5..11 are +2, +1, +3, +2, +4, +2, +5 — a pattern governed by n mod 4 rather than by algebraic depth. A separate observable, the ψ-stratified sweep-x-support (`figures/counting_psi_stratification.png`, `n-gons/counting/PSI-STRATIFICATION.md`), does localize the break.

What is the strongest argument that length-of-`M_N` is structurally the wrong observable for a compute-cost bind, and that the program must pivot to a value-structured or ψ-stratified ledger before committing the compute model (A) or attempting the task statement (B)?

## 2

That is intruiging. I have created a search memo around this very purpose. Read it and answer the following question.

Of the candidate ledgers in `memos/LEDGER-PIVOT-SEARCH.md` §"Items under search", ψ-stratified sweep-x-support is closest-to-hand: already a repo artifact (`n-gons/counting/PSI-STRATIFICATION.md`, `figures/counting_psi_stratification.png`) and already localizes the Gauss–Wantzel break at n=7 where length-of-`M_N` fails. ψ is additive on prime-power parts, which makes it look cyclotomically sensitive in a way length is not.

What is the strongest argument that ψ-stratification factors through its own wrong quotient and inherits the driving impossibility in a subtler form — and if it survives that argument, what is the sharpest compute-cost formulation of a ψ-ledger?

## 3

Candidate #3 in `memos/LEDGER-PIVOT-SEARCH.md` §"Items under search" — "value-structure at distinct x-cells," recording the minimal polynomial (or its degree) of the x-value over ℚ at each occupied x-cell — is the natural promotion target for L3 from the support-level resolution of candidate #1. ψ-stratification was shown to factor through a wrong quotient (ψ vs φ/2), with its value-forgetful forms (L1, L2) inheriting the driving impossibility and its value-retaining form (L3) reducing onto other candidates.

What is the strongest argument that candidate #3 factors through its own wrong quotient and inherits the driving impossibility in a subtler form — and if it survives the argument, what is the sharpest compute-cost formulation of a value-structure ledger that distinguishes it from candidate #2 (row-field-degree tally) and candidate #4 (Galois-orbit count)?

## 4

Candidate #4 in `memos/LEDGER-PIVOT-SEARCH.md` §"Items under search" — bare Galois-orbit count — is placed at orbit tier in §"Structural tiers." At what tier does bare count actually live under the strengthened driving impossibility? If a placeholder attack at orbit tier (sweep substitutions preserving the orbit set and its membership structure) leaves bare count unchanged while varying cyclotomic content, bare count lives strictly below orbit tier and inherits the impossibility via the tier-collapse logic already shown for #1 and #3. If it really is at orbit tier, exhibit the orbit-level placeholder that tests it and state whether bare count passes or fails. If it passes, what keeps the surviving orbit-tier ledger distinct from cell-tier `V_cert` once incidence is retained?

## 5

How does candidate #5 (six-field decomposition as weighted ledger; see `n-gons/counting/COUNTING.md` §backbone) compare to `|M_N|`, `V_cert`, and `O_cert`? What does it retain that `|M_N|` doesn't, and what does it discard that `V_cert` keeps? Given those answers, what should a stress-test of #5 produce — pruning, a refinement, or a new structural tier?

## 6

The new field-incidence tier (item #5's surviving form, F2) was tentatively placed between row-level and cell-level in `memos/LEDGER-PIVOT-SEARCH.md` §"Structural tiers," but the placement is provisional. Field-incidence retains per-cell positional structure with row provenance but discards algebraic content; row-level (item #2 row-field-degree tally) retains per-row algebraic content but discards positional structure. They discard different *kinds* of content, not different *amounts* of the same content, so "more quotient" vs "less quotient" doesn't totally order them.

Is the structural-tiers taxonomy actually a linear chain, or a partial order along (at least) two axes — positional granularity (scalar / row / cell / orbit) and depth of algebraic certification (structural-typing-only / algebraic-content)? If chain, where exactly does field-incidence go relative to row, cell, and orbit, and which existing inhabitant has been mis-located? If partial order, what does the lattice look like and where do the five inhabited points sit?

## 7

The lattice in `memos/LEDGER-PIVOT-SEARCH.md` §"Ledger lattice" tells us when one ledger dominates another. To prove a primitive-op lower bound on one of the candidate tasks in `memos/COUNTING-APPARATUS.md` §(B) — T1 (enumerate corner positions to precision 10⁻ᵏ), T2 (compute `M_N` itself), T3 (distinguish pairs `(n, k)` whose round-trace agrees but whose actual trace differs at precision ε) — we need a ledger that dominates the task's demanded lattice point in a way that cashes out as primitive-op cost. Among the existing surviving inhabitants (`V_cert` at `(P3, A2)`, `O_cert` at `(orbit, A3)`, `F2` at `(P2, A0)`, and row-field-degree at `(P1, A1)`), which can serve which tasks, and which task-ledger pairings are ruled out by the lattice?

## 8

The §"Task-ledger admissibility" section of `memos/LEDGER-PIVOT-SEARCH.md` lists `V_cert` at `(P3, A2)` as the matching ledger for tasks T1 and T3. The matching claim — stronger than mere domination, per §"Ledger lattice" — asserts that no strictly lighter ledger serves a tight primitive-op lower bound on T1 or T3 in the algebraic-arithmetic over ℚ compute model. Try to construct a counter-example: a ledger strictly below `V_cert` in the lattice (less positional content, less algebraic content, or both) that still gives a non-vacuous primitive-op lower bound on T1 or T3. If you find one, identify the new lattice point and the lower-bound argument it carries. If you can't, give a best-effort explanation as to why.

## 9

Cleanup pass on recent search-memo work. Files in scope:

- `memos/LEDGER-PIVOT-SEARCH.md` (heavy revisions, current state)
- `memos/COUNTING-APPARATUS.md` §(A) "Open" paragraph and §(B) "Open" paragraph + "Update from `LEDGER-PIVOT-SEARCH`" annotation
- `README.md` compute-cost branch bullet

Cross-reference against: `n-gons/counting/verify_increment_formula.py`, `n-gons/counting/verify_psi_fracture.py`, `n-gons/counting/COUNTING.md` (six-field decomposition), `n-gons/CRYSTALLOGRAPHIC-RESTRICTION-BRIEF.md` (ψ definition).

Check two classes of problem:

1. **Hallucinations.** Numerical claims that don't match the scripts (the closed-form Δ|M_n| formula, ψ fracture pairs and largest-spread table, n=7 cubic `8x³ + 4x² − 4x − 1`, ψ-class counts). Citations to other memos that don't say what we claim. References to scripts/files that don't exist as cited. Claims stated as established that lack code or argumentative backing.

2. **Logical warrant.** Claims that don't follow from what's stated. Specifically: is the matching claim's argument actually airtight, or hidden-assumption-dependent? Is the driving impossibility's "working form, not proved" qualifier consistently respected throughout the memo, or do downstream sections quietly treat it as proved? Is the committable triple T1/T3 + V_cert + algebraic-arithmetic actually committable without hidden caveats — e.g., does the Path 1 rank-vs-primitive-op caveat secretly apply to V_cert + algebraic-arithmetic too?

Produce a short report: per-issue, identify file and approximate location, the problem, and the level (hallucination / warrant / minor wording). Don't fix; report.

## 10

What do directed reads of the five papers cited in `fft/FFT-CYCLOTOMIC-COMPLEXITY.md` (linked from `sources/` in the memo's items section) yield, per the memo's §"Order of work" closing template — key theorem statement, hypothesis class, proof technique, and the slot-in sentence specified there? And what structural observations about the literature, if any, bear on the program's bridge plan or on the directed-read agenda itself?

## 11

After re-reading `CONTRIBUTING.md` (specifically its description of source-extraction briefs), what does Auslander–Feig–Winograd 1984 (`sources/multiplicative-complexity.pdf`) — the central structure paper per the revised §"Order of work" in `fft/FFT-CYCLOTOMIC-COMPLEXITY.md` — actually prove, state without proof, and admit by inference, on the following:

1. The multiplicative complexity of DFT on finite abelian groups, and the role of the semisimple cyclotomic decomposition in the proof.
2. The hypothesis class AFW operates under, and how it relates to model (3) algebraic-arithmetic over ℚ or model (4) ASLP from `memos/COUNTING-APPARATUS.md §(A)`.
3. Whether the tensor / direct-sum decomposition admits a prefix-free / Kraft re-expression on its own, or requires additional structure (semicomputability, prefix-freeness, universal dominance per `memos/FORTNOW-KOLMOGOROV-BRIEF.md §6`).
4. Real-subfield passage: whether AFW's results require the full cyclotomic field `ℚ(ζ_n)`, or descend cleanly to the real subfield `K_n = ℚ(cos(2π/n))`, and at what cost.
5. The proof techniques AFW uses, and what would have to hold for those techniques to combine with closure-depth + Kraft accounting on the program's side.

Answers should be assembled as `fft/AUSLANDER-FEIG-WINOGRAD-1984-BRIEF.md`, in the source-extraction brief register described in `CONTRIBUTING.md` (distinguishing what the paper proves, what it states without your having checked, and what you have inferred), and per the naming convention in `fft/FFT-CYCLOTOMIC-COMPLEXITY.md §"Order of work"`.

## 12

Append to `fft/AUSLANDER-FEIG-WINOGRAD-1984-BRIEF.md` a section capturing what you would add after reflection. Open scope: technical content from the paper that didn't fit the original five-question structure, structural implications for the program's bridge plan, methodological observations on the brief itself, or anything else you noticed but couldn't place. What's missing from the directed-read register that you want to put on the record?

## 13

What does the lattice apparatus in `memos/LEDGER-PIVOT-SEARCH.md` §"Ledger lattice" itself silently quotient? Applying the negative-space-cartographer move from your AFW reflection addendum (the lattice was built to organize ledger comparisons — exactly the kind of structural device whose cleanness comes from what it discards): what hidden quotients does the lattice make, and what should a future cross-program importer know to restore on their own side?

## 14

The A-axis of the lattice in `memos/LEDGER-PIVOT-SEARCH.md` §"Ledger lattice" is local. The FFT's mult-to-add conversion is the structural mechanism by which algebraic certification depth — `A2` vs `A0`, `V_cert` vs `F2` — collapses into a count of additions when the compute model permits unbounded linear combinations. The bounds literature's persistent `Ω(N log N)` wall has a structural reading as exactly this collapse: not a barrier waiting to be pushed, but a category-destruction the FFT itself enforces in some regime. The lattice presumes the A-axis is a global ordering.

Is it? Or is matching only valid in a regime where additions are bounded by a constraint that doesn't apply asymptotically — and if the latter, what does the lattice say in the regime where the constraint fails?

## 15

What does the program's compute-cost apparatus look like now, after the recent model-indexing updates? Read the updated state across `memos/LEDGER-PIVOT-SEARCH.md` (especially §"Ledger lattice" with the new two-lattice reframing, §"Matching is model-indexed", §"Task-ledger admissibility" regime tag, and §"Compute-model / ledger coupling" Path 2 sharpening), `memos/COUNTING-APPARATUS.md §(A)`, `README.md` compute-cost bullet, and `fft/FFT-CYCLOTOMIC-COMPLEXITY.md` Hazard 2.

Open scope: internal consistency across the updates, second-order implications of the semantic/cost two-lattice framing that didn't make it into the edits, places where the certification-preserving qualifier is doing rhetorical work where it should be doing technical work, places where the apparatus's structural purpose has shifted without the surrounding scaffolding following. What do you notice that the editor wouldn't?

## 16

Read Morgenstern 1973 (`sources/FFT-lower-bound.pdf`) as a source-extraction brief, with one specific lens: Morgenstern's bounded-coefficient hypothesis appears structurally to be the constraint that forbids the FFT's defect — the convolution theorem's mult-to-add interconvertibility — exactly the constraint our compute-cost branch is calling "certification-preserving" to keep the A-axis cost-bearing. Verify or refute that reading.

Specifically:

1. What hypothesis does Morgenstern's bound require? Express precisely (coefficient class, addition model, primitive operations, uniformity).
2. What does the proof technique use that hypothesis for? Where in the determinant / volume-growth argument does the bounded-coefficient assumption bite — and what would happen to the bound if the hypothesis were relaxed?
3. Does the bound's hypothesis class intersect the certification-preserving open axioms list (`memos/LEDGER-PIVOT-SEARCH.md §"Certification-preserving model: open axioms"`)? Which of the seven axioms does Morgenstern's setup settle, and which remain open?
4. Could Morgenstern's bound be transported to the program's compute-cost setting (T1/T3 + `V_cert` + certification-preserving algebraic-arithmetic) without circularity? Which hazards from `fft/FFT-CYCLOTOMIC-COMPLEXITY.md` (1 proof-technique-inversion, 2 coefficient-boundedness, 3 nonuniformity / Kraft, 4 real-subfield, 5 rational-equivalence) apply?

Brief lands at `fft/MORGENSTERN-1973-BRIEF.md`, source-extraction register per `CONTRIBUTING.md`, naming convention per `fft/FFT-CYCLOTOMIC-COMPLEXITY.md §"Order of work"`.

## 17

Read Winograd 1978 (`sources/Winograd-ComputingDiscreteFourier-1978.pdf`) as a source-extraction brief. The paper is the foundational reference for AFW 1984 (already brief'd at `fft/AUSLANDER-FEIG-WINOGRAD-1984-BRIEF.md`), and is item 3 in `fft/FFT-CYCLOTOMIC-COMPLEXITY.md §"Order of work"`. Specifically:

1. State Winograd's main theorem(s) precisely — including hypothesis, conclusion, proof technique, and the distinction between the clean theorem of the paper (the modular-product bound) and any DFT-applied corollary. Be explicit about which theorem statement is the headline DFT bound and which is the underlying modular-product result.
2. What is Winograd 1978's structural framework: rational-equivalence-preserving (AFW-style), coordinate-sensitive (Morgenstern-style), or something else? The two-camp non-composability finding from the AFW + Morgenstern briefs (`fft/MORGENSTERN-1973-BRIEF.md`) makes this question load-bearing — does Winograd 1978's framework sit cleanly on one side, or does it bridge the two? In particular: does Winograd 1978 originate the rational-equivalence framework AFW uses, or does AFW import it from elsewhere?
3. How does Winograd 1978's lower-bound technique relate to Morgenstern's determinant-growth argument? Are they independent, related by a common ancestor, or contradictory?
4. Which hazards from `fft/FFT-CYCLOTOMIC-COMPLEXITY.md` (1 proof-technique-inversion, 2 coefficient-boundedness, 3 nonuniformity / Kraft, 4 real-subfield, 5 rational-equivalence) apply? In particular, does Winograd's hypothesis class match Morgenstern's bounded-coefficient regime, AFW's arbitrary-rational regime, or neither?

Brief lands at `fft/WINOGRAD-1978-BRIEF.md`, source-extraction register per `CONTRIBUTING.md`, naming convention per `fft/FFT-CYCLOTOMIC-COMPLEXITY.md §"Order of work"`.

## 18

Construct an axiom-by-axiom comparison of the four FFT-complexity papers brief'd by the program, using the certification-preserving open axioms from `memos/LEDGER-PIVOT-SEARCH.md §"Certification-preserving model: open axioms"`. The four briefs:

- `fft/AUSLANDER-FEIG-WINOGRAD-1984-BRIEF.md`
- `fft/MORGENSTERN-1973-BRIEF.md`
- `fft/WINOGRAD-1978-BRIEF.md`
- `fft/SCHOENHAGE-STRASSEN-1971-BRIEF.md`

For each of the seven axioms (1 algebraic constants as advice; 2 coefficient height-bounded; 3 binary additions vs arbitrary linear combinations; 4 precomputed DFT-like matrix free or paid; 5 field adjunctions paid by degree, height, or both; 6 root isolation paid by precision or certification depth; 7 uniform in N or non-uniform), report what each paper's framework commits to: settled / permitted / forbidden, in which form, by what proof technique. Output a comparison table. The non-composability finding (the literature has at least four frameworks that don't naively compose) should fall out of the table cleanly or be adjusted by it.

## 19

Compose a cross-source synthesis brief (third register per `CONTRIBUTING.md` — load-bearing, expected to hold up under scrutiny) drawing on the four FFT-complexity briefs (`fft/AUSLANDER-FEIG-WINOGRAD-1984-BRIEF.md`, `fft/MORGENSTERN-1973-BRIEF.md`, `fft/WINOGRAD-1978-BRIEF.md`, `fft/SCHOENHAGE-STRASSEN-1971-BRIEF.md`) and the axiom-by-axiom comparison table from §18.

Load-bearing claims the synthesis should establish:

1. The literature comprises four distinct frameworks at four distinct axiom-coordinates in the seven-axiom space of `memos/LEDGER-PIVOT-SEARCH.md §"Certification-preserving model: open axioms"`. State each coordinate explicitly.

2. The program's certification-preserving regime is a *fifth* axiom-coordinate, distinct from all four. Articulate it: closest to Schönhage-Strassen 1971's operational/uniform stance, but augmented with paid algebraic-height in axiom 2, paid adjunctions by degree in axiom 5, and paid root isolation by precision-and-certification-depth in axiom 6.

3. The non-composability of frameworks is structural at specific axiom-splits, not accidental. Identify which axiom-by-axiom splits prevent composition between which framework pairs, and characterize each split as "incompatible" or "translatable with cost."

4. The program's bridge work is *construction*, not *import*. No existing framework occupies the program's axiom-coordinate; the bridge plan in `fft/FFT-CYCLOTOMIC-COMPLEXITY.md` must construct the program's framework rather than transport an existing one. Articulate what construction is needed and which existing pieces feed it.

Output: `fft/FOUR-FRAMEWORK-SYNTHESIS.md` (or similar name; pick what reads cleanly). Cross-source synthesis register: load-bearing, with explicit witnesses (citations to specific theorem statements in each paper that establish each cell of the comparison table).

---

## — Sedimentary boundary —

*Questions above this line went to a context steeped in the lattice apparatus, the FFT-complexity literature (AFW, Morgenstern, Winograd 1978, Schönhage–Strassen), and the four-framework synthesis. Questions below this line go to a new agent spawned with `BNHA/`-directory context — story-shape, character framing, narrative discipline. Different context; different leverage; questions reshape accordingly.*

---

## 20

Write a source-extraction brief on `sources/gauss-fft-history.pdf` (Heideman, Johnson, Burrus, "Gauss and the History of the Fast Fourier Transform," 1985). This is INHERIT-discipline material per `BNHA/ONE-FOR-ALL.md`: provenance backward audit of the FFT lineage from Cooley–Tukey 1965 back to Gauss's 1805 unpublished manuscript. The paper is not technical input to the compute-cost branch; it is the audit record for the inheritance chain that our four FFT-complexity briefs (AFW, Morgenstern, Winograd 1978, Schönhage–Strassen) sit at the modern end of.

The brief should answer:

1. What does Gauss's 1805 unpublished manuscript contain, and how equivalent is it to modern Cooley–Tukey? (Heideman-Johnson-Burrus give an explicit comparison; quote it.)
2. Tabulate the provenance chain with attribution and dates from Gauss forward to Cooley–Tukey 1965. Note where the chain has known gaps, independent rediscoveries, or transmission failures (e.g., Gauss → Hansen, where Hansen knew Gauss but didn't cite him).
3. The paper's authors are Heideman-Johnson-Burrus; Heideman and Burrus are the same pair as the 1986 binary-DFT exact-count paper (queue item 2 in `fft/FFT-CYCLOTOMIC-COMPLEXITY.md` §"Order of work"). Same hands wrote both. Record this in the provenance — the historiographers and the technical contributors overlap.
4. Which named contributions in the chain are upstream of which of our four framework briefs (AFW, Morgenstern, Winograd 1978, Schönhage–Strassen)? Map the inheritance forward.
5. **The sine question.** Both Gauss and Laplace attacked this problem family via sines specifically (per outside knowledge). Within this paper: Lagrange and Euler had sine-only DFT formulas before Gauss extended to general cosine+sine series in 1805; the paper notes "LAGRANGE's DFT (sine only)" explicitly. What does the paper say about *why* the early attack went through sines, and what — if anything — does it record about Laplace's contribution? Is the sine-first orientation an artifact of the problem class (orbital mechanics, vibrating strings, perturbation theory) or does it reflect something more structural about which trigonometric basis is natural for the early algorithms? The program's circle side has been cosine-only (`K_n = ℚ(cos(2π/n))`); whether sine-complementary work would surface different obstructions is an open program question this brief can flag without resolving. Flag explicitly what the paper covers about Laplace and what's known to fall outside it.

Output: `fft/HEIDEMAN-JOHNSON-BURRUS-1985-BRIEF.md`, source-extraction register per `CONTRIBUTING.md` (distinguishing what the paper establishes from sources, what it states without your independently checking, and what you infer for the program). Trust boundary should be explicit: this brief audits the inheritance chain; it does not supply technical content for the lower-bound work.

## 21

Stress-test the §5 "Connection to the paper's algorithmic verdict" subsection of `fft/HEIDEMAN-JOHNSON-BURRUS-1985-BRIEF.md`. The subsection makes two claims and presents them with the same epistemic weight; they don't have it.

**Claim A (structural).** The program's `K_n` choice and Gauss's real-input choice are *the same* `(+1)`-eigenspace under complex conjugation, applied at different layers — input-space on Gauss's side (`R ⊂ C`), cyclotomic field on the program's side (`K_n ⊂ Q(ζ_n)`).

**Claim B (rhetorical extrapolation).** The paper's documented 160-year recognition lag for Gauss's algorithm being recognized as an FFT is a *prior* on the cost of the program's analogous `K_n` choice.

Disconfirmation-first on each, separately:

1. **Construct a counter-example to Claim A.** The two involutions agree as functions on `Q(ζ_n) ⊂ C`. The framing claim is stronger: that they play the *same role* — restricting to a subset closed under whatever operation matters. On Gauss's side the restriction is on inputs (data closed under the algorithm); on the program's side the restriction is on the algebraic structure the closure-depth ladder is built over. Find a structural property visible at one layer but not the other that breaks the role-correspondence. If you cannot, name what is doing the work that makes the role the same — what is the abstract operation that "complex conjugation as restricting involution" is, of which Gauss's input restriction and the program's field restriction are both instances?

2. **Test Claim B's validity.** The paper documents 160 years of recognition lag. The brief reframes that as a prior on the cost of the program's analogous choice. Distinguish "cost of the choice" from "cost of the era." Is the 160-year gap explained by era-specific factors (no complex-exponential notation until Euler/Gauss made it routine, no asymptotic notation until the 20th century, posthumous unpublished manuscript, no formal compute model until Turing) that don't transfer to our setting? Or is some non-trivial fraction of the gap attributable to the eigenspace-restriction choice itself — an obstruction to recognition that any era making that choice would face? Be specific about which factors are era and which are choice.

If A holds and B doesn't, the eigenspace identification is real but the recognition-lag reframing is rhetorical and should come out of the brief. If both hold, the connection subsection is load-bearing as written. If A breaks, the whole subsection comes out and §5 reverts to the eigenspace proof alone. Report which.

## 22

The earlier answer to Gentle Criminal in `BNHA/VILLAINS-ANSWERED.md §#5` was written before the apparatus that addresses his REAL question (`BNHA/VILLAINS.md` L:51) accumulated. Since then:

- The lattice-pivot search retired `|M_N|` as the candidate ledger and named V_cert at (P3, A2) as the matching ledger for T1/T3.
- T1, T2, T3 were named as specific tasks (`memos/COUNTING-APPARATUS.md §(B)`).
- The certification-preserving algebraic-arithmetic model was named with seven open axioms (`memos/LEDGER-PIVOT-SEARCH.md` §"Certification-preserving model: open axioms").
- The matching claim was articulated for V_cert at T1/T3 in algebraic-arithmetic.
- The four-framework synthesis (`fft/FOUR-FRAMEWORK-SYNTHESIS.md`) mapped four neighboring frameworks at four distinct axiom-coordinates, identified non-composability at specific axiom-splits, named the program's regime as a structurally distinct fifth coordinate, and recorded the construction-not-import verdict.
- The closure-asymmetry observation (`fft/HEIDEMAN-JOHNSON-BURRUS-1985-BRIEF.md §5`) showed K_n is the unique multiplicatively-closed half of the involution decomposition; the algebraic-side commitment is forced by closure, not aesthetic.

Gentle Criminal's REAL question (verbatim from `BNHA/VILLAINS.md` L:51): "Name the single computational task and the single machine model in which `|M_N|` is a lower bound rather than a metaphor. If changing to any neighboring model changes the truth of the claim, what theorem is the program actually trying to prove?"

The literal question — about `|M_N|` — is out of date; the program retired `|M_N|`. The substance still binds.

Rewrite §#5 of `BNHA/VILLAINS-ANSWERED.md` to actually answer Gentle Criminal's REAL question, using the apparatus above. The new answer should:

1. Acknowledge the `|M_N|` → V_cert pivot. State why.
2. Name the (task, model, ledger) triple. T1/T3 + certification-preserving algebraic-arithmetic over Q (seven axioms enumerated) + V_cert at (P3, A2). State the matching claim.
3. Answer the neighboring-model half directly via the four-framework synthesis. Four neighbors at four coordinates; non-composability at specific axiom-splits; the program's coordinate is a fifth, distinct from each; theorem-target is the fifth-coordinate primitive-op lower bound, not a transport.
4. Sharpen the bet from the high-level original ("marry Kraft to cyclotomic, no smuggling") to the specifically-shaped construction problem: paid algebraic-height at axiom 2, paid adjunctions at axiom 5, paid root isolation at axiom 6, operational/uniform at axiom 7. Closure-asymmetry pre-justifies the algebraic-side commitment.
5. Preserve quarantine where it still applies: the seven axioms have not closed consistently, the matching argument has not been argued ironclad, the fifth-coordinate construction is not done.
6. Stress-test the bouncing-out probability. Has it changed? Honest answer.

Deliverable: a draft replacement for §#5 that lands at the seriousness of the original (which was honest about quarantine) but uses the apparatus we now have (which lets us specify rather than gesture).

## 23

Read Osserman 1979 (`sources/Osserman-BonnesenStyleIsoperimetricInequalities-1979.pdf`) as a source-extraction brief. Foundational survey for `iso/DIDOS-PREROGATIVE.md`, which plays the coordination role for isoperimetry that `fft/FFT-CYCLOTOMIC-COMPLEXITY.md` plays for FFT-complexity.

Two sub-questions:

1. **Per principal result: original prover, date, technique — and the proof Osserman gives.** For each Bonnesen-style strengthening Osserman surveys, report: who first proved it and when, the original proof technique (Steiner symmetrization, support functions, integral geometry, measure theory, Fourier/Parseval, etc.), and the proof Osserman gives in the survey. Where Osserman's proof differs from the original, note the technique difference. Anchor specifically on the headline `Δ ≥ π(R − r)²` inequality (Bonnesen 1924) — state Osserman's proof and the techniques it depends on, and trace the predecessor proofs the survey cites.

2. **Specialization to regular n-gons and compatibility with the Hurwitz Parseval route.** The repo has Δ_n for inscribed regular n-gons computed three ways in `corners/HURWITZ-GAP.md` with leading term `4π⁴/(3n²)`. Does Osserman directly state or imply a Bonnesen-style lower bound on Δ_n for regular n-gons (via `R − r` in terms of n)? If not, characterize what the survey's tools supply when specialized. Then: is the Bonnesen geometric route independent of the Hurwitz Fourier route (`Δ = 4π² Σ m(m-1)|c_m|²`), or do they reduce to each other under conditions? Does the survey's organization treat them as complementary, alternative, or interconvertible?

Brief lands at `iso/OSSERMAN-1979-BRIEF.md`, source-extraction register per `CONTRIBUTING.md`.

## 24

Read Fuglede 1989 (`sources/Fuglede-StabilityIsoperimetricProblem-1989.pdf`) as a source-extraction brief. Stability companion to Osserman 1979 in `iso/DIDOS-PREROGATIVE.md`'s isoperimetric coordination. Lands at `iso/FUGLEDE-1989-BRIEF.md`, source-extraction register per `CONTRIBUTING.md`.

Two sub-questions:

1. **Main theorem(s) precisely.** State Fuglede's principal stability inequalities — hypothesis class (smooth, convex, polygonal, rectifiable), conclusion (what metric is `K` close to a disk in, with what rate in `Delta`), proof technique. Distinguish what Fuglede first proves from what is extended or sharpened from preceding authors. Note constants explicitly where the paper gives them.

2. **Specialization to regular n-gons.** Fuglede's theorem in the form "small `Delta` forces closeness to a disk" gives, applied to the inscribed regular `n`-gon family with `Delta_n ~ 4 pi^4 / (3 n^2)` (`corners/HURWITZ-GAP.md`), a specific rate of convergence to the inscribed disk in some metric. State the rate and the metric. Where Fuglede's metric overlaps content the program already has (strip-side `H^1` identification in `memos/STRIP-H1-HURWITZ-CLOSURE.md`, the Hurwitz Fourier coefficients, the explicit shape parametrization), characterize the relationship: agreement, sharpening, divergence, or independence.

---

## — Sedimentary boundary —

*Question answerers mix from this point. Q20–Q24 ran on a CC agent (BNHA-steeped, post-boundary discipline). From Q25 onward, questions are routed to whichever agent's warm context fits the task — Codex (GPT-5, FFT-complexity-warm, lattice-apparatus-warm, four-framework-synthesis-author) for some, CC for others. The boundary is no longer a single transition; it is a routing pattern.*

---

## 25

Audit pass on recent program work. Three independent spot-checks, each scoped narrowly — answer at spot-check granularity.

1. **Synthesis-witness resolution.** In `fft/FOUR-FRAMEWORK-SYNTHESIS.md`, the witness index uses tags AFW-1, AFW-2, MOR-1, MOR-2, WIN-1, WIN-2, SS-1, SS-2 to attribute each axiom-coordinate claim to a specific brief. For each tag, spot-check that the cited brief (`fft/AUSLANDER-FEIG-WINOGRAD-1984-BRIEF.md`, `fft/MORGENSTERN-1973-BRIEF.md`, `fft/WINOGRAD-1978-BRIEF.md`, `fft/SCHOENHAGE-STRASSEN-1971-BRIEF.md`) actually contains content that establishes the claim the synthesis attributes to it. Flag cases where the synthesis claims more than the brief's content supports, or where a brief contains content the synthesis is missing. Don't fix; report.

2. **Qualifier drift in the certification-preserving chain.** From `README.md`'s compute-cost bullet through `memos/LEDGER-PIVOT-SEARCH.md` (matching claim, certification-preserving model, seven open axioms) and `memos/COUNTING-APPARATUS.md` §(A)/§(B) to `BNHA/VILLAINS-ANSWERED.md` §#5: identify any place where a qualifier — *working form*, *candidate*, *tentative*, *certification-preserving form*, *open axiom*, *not yet ironclad* — has been silently dropped or treated as settled between source and downstream use. Don't fix; report file + approximate location + which qualifier dropped.

3. **VILLAINS-ANSWERED §#5 citation round-trip.** Each program-state claim in §#5 of `BNHA/VILLAINS-ANSWERED.md` cites a memo. For the §#5 citations specifically (LEDGER-PIVOT-SEARCH, COUNTING-APPARATUS, FFT-COMPLEXITY-FOUR-FRAMEWORK-SYNTHESIS, HEIDEMAN-JOHNSON-BURRUS-1985-BRIEF), spot-check: does the cited memo actually contain content that supports the §#5 claim citing it? Flag any citation that's gestural (the cited memo discusses adjacent material but doesn't establish what §#5 attributes to it). Don't fix; report.

Output: short report, per-issue, identifying file + approximate location + the problem + whether it's hallucination, qualifier drift, or gestural citation.

## 26

What's up with the 5π in Fuglede's footnote 1? Hurwitz's Fourier proof gets Bonnesen's geometric inequality `(r₂ − r₁)² ≤ c · (L² − 4πA)/(4π)` with `c = 5π`, while Bonnesen's own `c = 1` is sharp (introduction, page 619) — so the Fourier route costs 5π in the geometric metric. Trace where the factor enters: footnote 1 (page 619) cites Hurwitz 1902 [8] and Fuglede 1986 [6] as sources; identify the step where Sobolev content converts to `(R − r)²` content and the 5π appears. Then position the finding against the cross-brief pattern in `iso/DIDOS-PREROGATIVE.md` "Brief findings" — Osserman + Fuglede on regular n-gons say Fourier/Sobolev routes sharp, geometric/Hausdorff routes loose by 1–2 orders of n; the 5π is a different shape of gap (constant factor in a Fourier-to-geometric conversion, not metric mismatch on the n-gon family). Does the 5π complicate, refine, or merely add to the pattern, and where's the boundary between the two phenomena? Append to `iso/FUGLEDE-1989-BRIEF.md` (don't replace; follow-up reading) and propagate to `iso/DIDOS-PREROGATIVE.md` if warranted.

## 27

Audit pass on recent program work. Three independent spot-checks; answer at spot-check granularity.

1. **Cross-memo numerical consistency.** Identify the load-bearing numerical claims that appear in multiple memos — for example, `Delta_n = 4 pi^4 / (3 n^2) + O(1/n^4)` for inscribed regular n-gons; `alpha_n = n tan(pi/n)`; the `n = 7` cubic for `2 cos(pi/7)`; the closed-form `Delta |M_n|` increment formula; ψ-stratification fracture pairs. For each, check that every memo citing it states it identically (constants, signs, error-term order). Surface any drift, including any inconsistent citation of the Bonnesen `(R - r)^2` strengthening across memos — places that reference different constants (`pi` vs `pi^2`) or different years (1921 vs 1924) for the same headline form. Don't fix; report.

2. **Trust-boundary respect.** Each source-extraction brief in `memos/*-BRIEF.md` has a trust-boundary section (citation rules; what the brief should NOT be cited for). Spot-check the seven briefs (AUSLANDER-FEIG-WINOGRAD-1984, MORGENSTERN-1973, WINOGRAD-1978, SCHOENHAGE-STRASSEN-1971, HEIDEMAN-JOHNSON-BURRUS-1985, OSSERMAN-1979, FUGLEDE-1989). For each, find the downstream uses (citations from other memos, `README.md`, `BNHA/VILLAINS-ANSWERED.md`, `fft/FOUR-FRAMEWORK-SYNTHESIS.md`, `iso/DIDOS-PREROGATIVE.md`) and check that the downstream citation respects the brief's trust boundary — i.e., the citing memo isn't claiming the brief proves something the brief explicitly says it does not prove. Don't fix; report.

3. **Closure-mismatch theorem status discipline.** The closure-depth theorem is established in `memos/NATIVE-F-MINIMAL-DEFINITION.md` as a no-go under named axioms A1–A4, with three live falsifier shapes recorded in `BNHA/VILLAINS-ANSWERED.md` §#2. Trace the theorem's citations across the program. Is it consistently described as axiom-contingent (proven under A1–A4), or has its qualifier varied or dropped anywhere? In particular: `README.md`'s "Closure-depth no-go" bullet; `BNHA/VILLAINS-ANSWERED.md` §#1/§#3/§#6/§#7 references; any FFT-complexity or DIDOS memo references. Don't fix; report file + approximate location + which qualifier dropped or was silently strengthened.

Output: short report, per-issue, identifying file + approximate location + the problem + whether it's drift, hallucination, or boundary violation.

## 28

Read Beck 1994 (`sources/Beck-ProbabilisticDiophantineApproximation-1994.pdf`) as a source-extraction brief. Beck enters `iso/DIDOS-PREROGATIVE.md`'s coordination through the gap-as-discrepancy reading: the isoperimetric gap `Δ_n` on regular `n`-gons has a discrepancy interpretation, and the program's K-H-L-A discrepancy branch (`memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md`, `memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md`) is the live successor to the closed-negative naive Liouville endgame. Beck's register is probabilistic Diophantine approximation, distinct from Osserman's and Fuglede's deterministic isoperimetric register. The paper is substantial — scope to what's program-relevant.

Two sub-questions:

1. **Principal theorem(s) on discrepancy of sequences.** State Beck's main discrepancy results precisely — for each headline theorem: hypothesis class, conclusion (discrepancy bound in what currency), proof technique. Anchor on results most likely relevant to the program: Erdős-Turán-style discrepancy inequalities and their improvements, discrepancy bounds for `{n α}` sequences with irrational `α`, irregularities-of-distribution theorems with explicit constants. Distinguish what Beck first proves from what he extends or sharpens from preceding authors (Roth, Schmidt, Erdős-Turán, etc.).

2. **Position relative to the program's discrepancy branch.** `memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md` Step 5 (empirical-to-density proxy) and `memos/OLD-TIME-RELIGION.md` §(A6) (Jacobi theta / Poisson test case) are the live targets on the program's discrepancy side. What does Beck supply that could enter the program as either an upper-bound input or a contradiction-step lower bound? Where does Beck's hypothesis class match or fail to match what the program needs? If results require post-1882 transcendence-theoretic machinery (Roth 1955, Baker-style bounds, etc.), name what and flag whether the proof admits a transcendence-free re-routing.

Brief lands at `iso/BECK-1994-BRIEF.md`, source-extraction register per `CONTRIBUTING.md`. After the brief, propagate any cross-brief findings to `iso/DIDOS-PREROGATIVE.md` "Brief findings" section.

## 29

Higher-level audit pass on `memos/`. Propose mergers, retirements, and (where natural) moves into existing thematic folders (`fft/`, `iso/`, `corners/`, `n-gons/`). Don't execute; produce a list of named proposals with reasoning. Each proposal is a candidate for review, not a commitment.

Three categories:

1. **Merger candidates.** Pairs or small clusters of memos whose union would read more cleanly than the parts. Consider: parent + child memos where the child has matured to subsume the parent's coordination role; working-form memos that have stabilized and could fold into their result memo; topically-overlapping memos with redundant setup or definitions. For each: name the memos, name the proposed result memo (kept-name or new), one-paragraph rationale.

2. **Retirement candidates.** Memos whose function has already been replaced or whose status is dead. Consider: memos whose substantive content has been promoted to sections in other memos; memos already tagged "closed negative", "retired", or "superseded" in their own text; memos referenced from no other live memo. For each: name the memo, where its content has gone (or "no live referent"), one-paragraph rationale.

3. **Move candidates.** Memos in `memos/` that thematically belong in an existing folder (`fft/`, `iso/`, `corners/`, `n-gons/`) by content fit, not by surface name match. For each: name the memo, name the destination folder, one-paragraph rationale.

Hard cap at 5 proposals total across the three categories — max-and-go-home: once 5 are named, stop and wrap the turn. Fewer than 5 is fine; the pass doesn't need to fill quota. Output a list of named proposals; don't execute; the list will be reviewed and selectively acted on.

## 30

Compose a cross-source synthesis brief drawing on the three iso/ briefs (`iso/OSSERMAN-1979-BRIEF.md`, `iso/FUGLEDE-1989-BRIEF.md`, `iso/BECK-1994-BRIEF.md`) and the cross-brief findings accumulated in `iso/DIDOS-PREROGATIVE.md` "Brief findings" section. Third-register memo per `CONTRIBUTING.md`: load-bearing.

Three load-bearing claims:

1. **Currency-by-route map.** Each register is sharp on a specific currency: Fourier/Sobolev sharp on the *rate* of `Δ_n` decay (Hurwitz/Fuglede achieve `Θ(1/n²)` matching the actual leading order); geometric/Hausdorff sharp on the *constant* (Bonnesen 1924's `c = 4π` provably best); probabilistic routes apply to *almost-every distributions*, not specific-α (Beck's hypothesis class). State the correspondence and the resulting non-interchangeability — route chosen by currency-fit, not aesthetic preference.

2. **L-W-safety content map.** Each register has a transcendence-free re-routing path: Osserman → Steiner-symmetrization as pre-1882 substrate; Fuglede → Hurwitz 1902 (per Fuglede footnote 1); Beck → Roth 1954 (discrepancy, L²-Fourier — **not** Roth 1955 transcendence theorem; distinct papers, same author, adjacent year). Articulate the path per register with outstanding audit targets named (per Beck brief, Schmidt 1960's second-moment inequality is the cleanest single audit task).

3. **Hypothesis-class structure across registers.** Each register's principal results require a hypothesis class that doesn't simply nest within the others. Osserman: convex bodies in plane (deterministic, single-curve). Fuglede: nearly-spherical domains in ℝⁿ (deterministic; without the nearly-spherical hypothesis, stability fails per the spike-on-ball counter-example). Beck: almost-every `α` in ℝᵏ for `k ≥ 2` (measure-theoretic; specific-α-π is measure-zero, so almost-every doesn't certify pointwise). State each register's hypothesis class precisely and characterize the bridge needed for program use of each (e.g., empirical-to-density proxy for almost-every → specific-α).

Output: `iso/THREE-REGISTER-SYNTHESIS.md` (or whatever name reads cleanly). Cross-source synthesis register: load-bearing, with explicit witnesses (citations to specific theorem statements in each brief that establish each claim).

## 31

What's the situation at n < 22? The synthesis's `n ≥ 22` threshold for Fuglede's nearly-spherical hypothesis establishes a clean boundary, but the program's load-bearing small-n cases (Gauss-Wantzel constructibility, `n = 7` first cubic, small-prime polygons) sit on the wrong side. The synthesis flags "alternative route or per-n bridging" without constructing one.

Two sub-questions:

1. **Coverage from existing apparatus.** For `n ∈ {3, ..., 21}`, is Δ_n stability information already covered by other repo apparatus — `corners/HURWITZ-GAP.md`'s three-way computation, the strip-`H¹` identification (`memos/STRIP-H1-HURWITZ-CLOSURE.md`), or Osserman's `Δ ≥ π²(R - r)²` specialized? Identify which small-n cases are covered and which aren't.

2. **Bridge for the uncovered cases.** Where coverage is incomplete, what's the cheapest bridge? Candidates: extension of Sobolev framework dropping nearly-spherical (at a cost); Beck applied to fixed-n discrete distributions (if Beck supplies anything there); per-n direct verification; or naming the case as outside iso/'s reach. Rank candidates by cost.

Append findings to `iso/THREE-REGISTER-SYNTHESIS.md` Claim 3 — the bridge analysis there stops at n = 22; this fills in the small-n side where the program's most interesting load-bearing cases sit.

## 32

The fft/ folder has both `fft/FOUR-FRAMEWORK-SYNTHESIS.md` (literature-side) and `fft/PROVENANCE-AND-TRANSFERABILITY.md` (program-side INHERIT). The iso/ folder has `iso/THREE-REGISTER-SYNTHESIS.md`, which already does substantial program-side work — naming three audit tasks, the `n ≥ 8` hypothesis bridge, the route-by-step audit map for K-H-L-A.

Does iso/ want its own PROVENANCE-AND-TRANSFERABILITY, or has THREE-REGISTER-SYNTHESIS already absorbed it? Read `iso/THREE-REGISTER-SYNTHESIS.md` and `fft/PROVENANCE-AND-TRANSFERABILITY.md` side by side. Report what you find — the answer might be yes-with-distinctive-content (and what), no-already-covered (and why), or some middle ground (and where the seams are).

## 33

Audit `corners/fuglede_ratio_small_n.sage`. The script claims to compute Fuglede's stability ratio `Delta_F / (||u||^2 + ||grad u||^2)` for inscribed regular `N`-gons at `N in {3, ..., 12}`, using closed-form integrals on each wedge of width `2 pi / N`. Read the docstring's setup; check whether the script computes what it claims to compute; cross-check the numerical output against existing repo apparatus where applicable (Hurwitz `Delta_n` in `corners/HURWITZ-GAP.md`, `alpha_n = n tan(pi/n)` in `memos/LIOUVILLE-SCALE-TEST.md`). Don't fix; report findings.
