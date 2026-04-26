# ROTATIONS-UPLIFT-PLAN

Plan for integrating the rotations/ register's supply across the
program. The cross-folder brief identified four "direct supply"
targets, three "methodological precedent" targets, and two "candidate
machinery" targets — nine integrations in total — that take the
rotations/ register from "newly-organized folder" to "actively wired
into fft/, iso/, memos/, and BNHA/."

This file contains two artifacts:

1. **Target uplift list** (§1) — populated copy of the cross-folder
   brief that triggered this plan. Stable; treat as the table of
   contents for what the plan operates on.
2. **Plan skeleton** (§2) — scaffolding only. Per-target work plans,
   sequencing, cross-folder consistency check, final synthesis memo,
   status tracker. To be filled in turns.

Register: search-memo / planning artifact during the active build-up
phase. When all targets close, the file freezes as a historical record
of how the rotations/ supply was wired in, with the final synthesis
memo as the load-bearing artifact downstream.

---

## 1. Target uplift list

Three categories. Each target names a live item elsewhere in the
program plus the rotations/ supply that addresses it.

### Direct supply (rotations/ does the work the live item needs)

**A1. K-H-L-A empirical-to-density proxy ← Lefèvre–Muller compressed
orbit.** `memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md` Step 5 names the
proxy as a hypothesis: bridge from pointwise per-`n` discrepancy to
averaged-over-range. `rotations/3DT-BRIEF.md` §"Lefèvre–Muller–
Tisserand: The Algorithmic Lens" supplies a worked pseudocode (`gamma, delta, d,
u, v` with Euclidean updates) that compresses the rotation orbit
without enumerating its points — exactly the move the proxy
proposes, in 1-dim algorithmic form. Beck 1994 (in iso/) is the
higher-dim Fourier-substitute version. The proxy has a 1-dim worked
precedent and a higher-dim methodological template.

**A2. BIND-audit safety for the discrepancy register ← 3DT
BIND-compatibility flag.** `memos/OLD-TIME-RELIGION.md`'s
content-not-calendar audit and `iso/THREE-REGISTER-SYNTHESIS.md`
Claim 2's Beck-via-Roth-1954 audit both want BIND-safe
Fourier-discrepancy machinery. `rotations/3DT-BRIEF.md` §"Program-
Facing Consequences 2" already explicitly flags: "None of the three
papers requires the repo's disallowed circle-side machinery such as
the Stern–Brocot tree, Farey-as-tree, Thomae, or Minkowski's
question-mark function." This BIND-clearance was logged before the
audit discipline was formally named.

**A3. β(π) as the right control parameter for K-H-L-A's effective-C
← 10-martinis.** `memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md` wants
effective `C` in `|qπ − p| ≫ q^{−C}`.
`rotations/10-MARTINIS-BRIEF.md` §"The Arithmetic Parameter"
establishes `β(α) = limsup (ln q_{n+1})/q_n` as the *exponential-
rate* control parameter (correcting the early memo's wrong
`limsup ln q_{n+1}/ln q_n`). β(π) = 0 places π in the Diophantine
class; the K-H-L-A endgame's effective-C lives downstream of this
classification.

**A4. CF-as-primitive ← CF-CROSSWALK extension.** When
`rotations/CONTINUED-FRACTIONS-CROSSWALK.md` was written, four
perspectives converged on the convergents. Two more have since
landed: Beck 1994 (iso/) substitutes Fourier+second-moment for CFs
in higher-dim discrepancy; the K-H-L-A discrepancy branch
(`memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md` +
`memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md`) uses CFs of π as the
substrate for the Aitchison × E-T-K × Kraft pairing. Six
perspectives now, not four.

### Methodological precedent (rotations/ supplied the proof template or organizational pattern that already-completed work later instantiated)

**B1. F-theorem proof shape ← 10-martinis "absence-of-X implies
impossible regularity."** `memos/NATIVE-F-MINIMAL-DEFINITION.md`'s
closure-mismatch theorem proves no functor `F` by: assume `F` exists
→ derive cyclotomic-ladder unboundedness incompatible with affine
flatness → contradict. `rotations/10-MARTINIS-BRIEF.md` §"Program-
Facing Exports 1" explicitly names this template (assume non-Cantor
→ derive fictitious analytic regularity → contradict via polar-set
obstruction) as a "reusable export." The program's primary theorem
inhabits a template the rotations/ register articulated before
NATIVE-F was written.

**B2. iso/THREE-REGISTER pattern ← 3DT's three-lens predecessor.**
`iso/THREE-REGISTER-SYNTHESIS.md` reads geometric / Sobolev /
probabilistic as three independent registers on the isoperimetric
gap. `rotations/3DT-BRIEF.md` reads Berthé–Reutenauer
(combinatorial), Lefèvre–Muller (algorithmic), Marklof–Strömbergsson
(geometric/lattice) on rotation-orbit gaps. *Same structural pattern
at smaller scale — three independent registers converging on one
arithmetic object.* iso/ is independent confirmation; 3DT was the
first instance and is the methodological model.

**B3. HJB-1985 §5 eigenspace decomposition ← Marklof–Strömbergsson
basis vectors.** The closure-side proof in
`fft/HEIDEMAN-JOHNSON-BURRUS-1985-BRIEF.md` §5 reads
`Q(ζ_n) = K_n ⊕ K_n · 2i sin(2π/n)` from basis elements `1` and
`(ζ_n − ζ_n^{−1})`. Marklof–Strömbergsson read 3DT gap lengths as
`r₂/N, s₂/N, (r₂+s₂)/N` from basis vectors `r, s` of a unimodular
lattice with `r + s` accounting for the third value. *Same
"decompose 2-dim structure, read identity off basis" pattern at two
layers* — algebraic (closure-mismatch) and geometric
(rotation-orbit gaps).

### Candidate machinery (rotations/ offers concrete machinery for explicitly-open program bets)

**C1. Gentle Criminal's Kraft-cyclotomic bet ← 3DT BWT/Lyndon
finite-word machinery.** `BNHA/VILLAINS-ANSWERED.md` §#5 names the
bet: "marry Kraft arithmetic to cyclotomic complexity… prefix-free-
encoding floor on objects of cyclotomic depth, denominated in bits,
in a model whose primitives don't smuggle the circle in as a free
constant." `rotations/3DT-BRIEF.md` §"Burrows–Wheeler and perfectly
clustering Lyndon words" supplies the Ferenczi–Zamboni
identification: every 3DT-encoding word is a perfectly-clustering
Lyndon word — *finite-state* characterization of rotation-orbit
structure, separable from the circle, with prefix-free encoding
properties. One concrete candidate path from rotation-orbit data to
Kraft-shaped bookkeeping.

**C2. Two-sided log/circle objects ← Lefèvre–Muller "log-side
native" 3DT use.** The program seeks objects that natively live on
both sides (log: Landfall ε(m); circle: K_n, polygon vertices).
`rotations/3DT-BRIEF.md` §"Lefèvre–Muller–Tisserand: The Algorithmic Lens"
flags 3DT's table-maker's-dilemma deployment as "log-side native,
not merely a circle-side theorem later imported." 3DT is the
program's *first* explicit two-sided object; K_n (post HJB-1985) is
the second.

### Concrete small audit-discipline citations (subset of A1, A4, B1, B3)

The brief's closing also named four small citation-discipline edits
that visible the rotations/ supply at the live items without writing
new substantive content. These are the cheapest sub-pieces of the
larger targets; they may be done independently or as part of the
parent target.

- (i) Update `rotations/CONTINUED-FRACTIONS-CROSSWALK.md` to six
  perspectives — sub-piece of A4.
- (ii) Cite `rotations/10-MARTINIS-BRIEF.md` §"Program-Facing Exports
  1" methodologically in `memos/NATIVE-F-MINIMAL-DEFINITION.md`'s
  proof-shape note — sub-piece of B1.
- (iii) Cite Marklof–Strömbergsson's basis-vector reading in
  `fft/HEIDEMAN-JOHNSON-BURRUS-1985-BRIEF.md` §5's "Conclusion"
  subsection as the rotations-layer precedent for the eigenspace
  decomposition — sub-piece of B3.
- (iv) Cite Lefèvre–Muller's compressed-orbit pseudocode in
  `memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md` Step 5 as the operational
  template for the empirical-to-density proxy — sub-piece of A1.

---

## 2. Plan skeleton

The remainder of this file is scaffolding. To be filled in turns.

### 2.1 Per-target work plans

One sub-subsection per target. Each populated by:

- **Live item.** File + section that treats this as live elsewhere.
- **rotations/ supply.** File + section in rotations/ that addresses
  it.
- **Type.** direct supply / methodological precedent / candidate
  machinery.
- **Specific edits.** Files to touch and the substance of each edit.
- **Audit step.** Verification after edits land.
- **Dependencies.** Other targets this depends on.
- **Status.** not-started / in-progress / complete.

#### A1 — K-H-L-A empirical-to-density proxy ← Lefèvre–Muller

- **Live item.** `memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md` Step 5 — the
  empirical-to-density proxy is named there as a hypothesis: bridge
  from pointwise per-`n` discrepancy to averaged-over-range. Also
  relevant: `memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md` (parent
  transcendence-program memo whose discrepancy branch this proxy
  serves); `iso/BECK-1994-BRIEF.md` (higher-dim Fourier-substitute
  methodological alignment, already on file as the K-H-L-A
  branch's structural validation).
- **rotations/ supply.** `rotations/3DT-BRIEF.md` §"Lefèvre–Muller–
  Tisserand: The Algorithmic Lens" — worked pseudocode (`gamma, delta, d, u, v`
  with Euclidean updates) that compresses the rotation orbit
  without enumerating its points. This is the 1-dim algorithmic
  shape of exactly what the proxy proposes. Beck 1994 supplies the
  higher-dim Fourier-substitute version of the same shape; Lefèvre–
  Muller and Beck pair as 1-dim algorithmic + higher-dim probabilistic
  precedents for the proxy.
- **Type.** Direct supply.
- **Specific edits.**
  - `memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md` Step 5: cite the
    Lefèvre–Muller compressed-orbit pseudocode as the **1-dim
    operational template** for the empirical-to-density proxy, with
    the variables `gamma, delta, d, u, v` named explicitly. This is
    sub-citation (iv) from the plan's closing list and is the
    load-bearing edit for A1. Also note the complementary higher-
    dim Fourier-substitute methodological alignment via Beck 1994
    (per `iso/BECK-1994-BRIEF.md`); the proxy now has two
    precedents in adjacent registers.
  - `rotations/3DT-BRIEF.md` §"Lefèvre–Muller–Tisserand: The
    Algorithmic Lens": back-pointer to the K-H-L-A Step 5 use site.
  - `iso/BECK-1994-BRIEF.md` (optional cross-link): note that
    Beck's higher-dim Fourier-substitute is paired with Lefèvre–
    Muller's 1-dim algorithmic precedent for the K-H-L-A empirical-
    to-density proxy. Optional because Beck stays in `iso/` per the
    rotations/README; this would be a cross-reference, not
    relocation. Recommend including for symmetry but tag as
    optional.
- **Audit step (verification pass).**
  - (a) Verify the Lefèvre–Muller pseudocode is correctly summarized
    at the K-H-L-A use site — variables (`gamma, delta, d, u, v`),
    Euclidean updates, the orbit-compression invariant. The Step 5
    reference must accurately reflect what the algorithm does and
    how it relates to the proxy.
  - (b) Verify the relationship to Beck 1994 is correctly stated.
    Lefèvre–Muller is 1-dim algorithmic; Beck is `k ≥ 2` dim
    probabilistic. The proxy's 1-dim case is what the program needs
    (π lives in `ℝ^1`). The two sources supply 1-dim precedent and
    higher-dim methodological alignment respectively — neither
    alone suffices; the combination is the operational pairing.
  - (c) Cross-reference symmetry between `KRAFT-BUDGET-ONE-
    DIMENSIONAL` Step 5 and `3DT-BRIEF`.
  - (d) Trust-boundary respect: `3DT-BRIEF`'s source-extraction
    framing and "Bottom Line" name the brief's payload; verify the
    K-H-L-A citation respects those limits. Specifically:
    `3DT-BRIEF` is a source-extraction brief on three rotation
    papers, not a proof of the empirical-to-density proxy. The
    citation should be for "operational template" or "1-dim
    algorithmic precedent," not for proof of the proxy itself.
  - (e) BIND-discipline check: the Lefèvre–Muller pseudocode uses
    CFs of `α` implicitly (via Euclidean updates); the K-H-L-A
    discrepancy branch uses CFs of π. The crosswalk memo
    (`rotations/CONTINUED-FRACTIONS-CROSSWALK.md`) records CFs as
    a primitive shared across multiple memos. The A1 integration
    should be consistent with the CF-as-primitive framing — not
    introducing a new CF use, but making the existing one
    explicit.
- **Dependencies.** Lands after A3 (A3 establishes `β(π) = 0`
  Diophantine classification; A1's proxy uses Diophantine
  classification implicitly — though the link is not load-bearing,
  sequencing avoids forward references). Independent of B1 and C1.
  Sub-citation (iv) is the load-bearing edit.
- **Status.** complete; landed and verified.
- **Change in program capacity.**
  - *Before.* K-H-L-A's discrepancy branch has a Step-5 hypothesis
    (empirical-to-density proxy) with methodological alignment from
    Beck 1994 (higher-dim Fourier-substitute) but no 1-dim
    operational template. The proxy is shaped but not anchored to a
    specific algorithm.
  - *After.* The 1-dim case has a worked algorithmic precedent
    (Lefèvre–Muller's compressed-orbit pseudocode). The proxy now
    has 1-dim algorithmic precedent + higher-dim methodological
    alignment from two different rotations/iso sources, in two
    complementary registers.
  - *Newly do.* K-H-L-A's discrepancy branch can reference a
    specific algorithmic template for the empirical-to-density
    proxy. The construction question becomes: does the Lefèvre–
    Muller compressed-orbit machinery compose with the K-H-L-A
    budget machinery without smuggling in CF-of-π content beyond
    what the crosswalk already records? That is a specific
    construction with named ingredients, not a placeholder for
    unknown machinery.

#### A2 — BIND-audit safety for discrepancy ← 3DT BIND-compatibility

- **Live item.** `memos/OLD-TIME-RELIGION.md`'s content-not-calendar
  audit, plus `iso/THREE-REGISTER-SYNTHESIS.md` Claim 2's L-W-safety
  content map (specifically the Beck → Roth 1954 sub-thread, §2.3 of
  the synthesis). Both want BIND-safe Fourier-discrepancy machinery
  with worked precedent.
- **rotations/ supply.** `rotations/3DT-BRIEF.md` §"Program-Facing
  Consequences 2: The vocabulary is unusually Erasure-compatible" —
  explicitly flags: "None of the three papers requires the repo's
  disallowed circle-side machinery such as the Stern–Brocot tree,
  Farey-as-tree, Thomae, or Minkowski's question-mark function.
  Continued fractions do appear, but as local arithmetic data, not as
  a global organizing tree." This BIND-clearance was logged before
  the audit discipline was formally named in OLD-TIME-RELIGION.
- **Type.** Direct supply.
- **Specific edits.**
  - `memos/OLD-TIME-RELIGION.md`: in the audit-criterion section
    naming BIND-compatibility as a content criterion, add a worked-
    precedent paragraph noting that 3DT-BRIEF logged BIND-compatibility
    for rotation-orbit machinery (finite words, Burrows–Wheeler,
    lattice F on Γ\SL(2,R), Euclidean updates) before the audit
    discipline was formally named. Cite `rotations/3DT-BRIEF.md`
    §"Program-Facing Consequences", subsection 2.
  - `iso/THREE-REGISTER-SYNTHESIS.md` Claim 2 §2.3 (Beck content-
    path subsection): add a forward-pointer noting that the BIND-
    compatibility claim for Beck's Fourier-discrepancy machinery
    (Poisson + Fejér + second-moment + Borel-Cantelli) has a worked
    precedent in 3DT-BRIEF. Beck's machinery and 3DT's machinery
    share BIND-compatibility status; the precedent strengthens the
    audit verdict from "isolated audit on Beck" to "audit-with-
    precedent."
  - `rotations/3DT-BRIEF.md` §"Program-Facing Consequences",
    subsection 2: back-pointer to the OLD-TIME-RELIGION audit-
    criterion section and the iso/THREE-REGISTER-SYNTHESIS Claim 2
    use site.
- **Audit step (verification pass).**
  - (a) Verify the BIND-compatibility claim is structurally accurate.
    The 3DT brief lists (Stern–Brocot tree, Farey-as-tree, Thomae,
    Minkowski ?(x)) as forbidden circle-side machinery; spot-check
    that none appears in Berthé–Reutenauer, Lefèvre–Muller, or
    Marklof–Strömbergsson.
  - (b) Verify the same BIND-compatibility holds for Beck 1994's
    machinery (Poisson + Fejér + second-moment + Borel-Cantelli) and
    Aitchison's density expansion (Poisson summation + Fourier
    coefficients). If any forbidden vocabulary appears in those
    sources, the worked-precedent claim weakens and the uplift's
    framing must be adjusted.
  - (c) Cross-reference symmetry: forward-pointers from
    OLD-TIME-RELIGION and iso/THREE-REGISTER-SYNTHESIS to 3DT-BRIEF,
    plus matching back-pointer from 3DT-BRIEF.
  - (d) Trust-boundary respect: 3DT-BRIEF flags BIND-compatibility as
    a "Program-Facing Consequence" — a derived observation about the
    brief's content, not a result the brief proves. Cite as such; do
    not promote to a "BIND-safety theorem." The 3DT brief is a
    source-extraction brief; the audit is the program's discipline
    applied to it, not the brief's own claim.
- **Dependencies.** Independent of A1, A3, A4, B1, B2, B3, C1, C2.
  Lower-leverage than A1 (audit-discipline consolidation rather than
  new operational template); sequenced after the populated batch as
  part of the second pass.
- **Status.** complete; landed and verified.
- **Change in program capacity.**
  - *Before.* The L-W-safety audit at OLD-TIME-RELIGION names BIND-
    compatibility as a content criterion. Beck 1994's machinery is
    being audited under this criterion (per iso/THREE-REGISTER-
    SYNTHESIS Claim 2). The audit verdict is "plausibly L-W-safe"
    but isolated — no in-program precedent for "Fourier-discrepancy
    machinery audited as BIND-compatible."
  - *After.* The audit verdict has a worked precedent. 3DT-BRIEF
    logged BIND-compatibility for the same kind of machinery before
    the audit discipline was formally named. The OLD-TIME-RELIGION
    criterion has a confirming instance; the iso/THREE-REGISTER-
    SYNTHESIS Beck audit is no longer an isolated case.
  - *Newly do.* The discrepancy register's BIND-audit status moves
    from "isolated audit on Beck" to "audit-with-precedent." Future
    Fourier-discrepancy literature imports inherit a worked example:
    flag BIND-compatibility at brief-time, not retroactively. Small
    style-of-discipline export beyond the specific Beck audit.

#### A3 — β(π) as K-H-L-A effective-C control parameter ← 10-martinis

- **Live item.** `memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md` (the
  effective-C ambition `|q π − p| ≫ q^(−C)`); also
  `memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md` (the K-H-L-A budget side
  whose Step-5 empirical-to-density proxy uses Diophantine
  classification of π implicitly).
- **rotations/ supply.** `rotations/10-MARTINIS-BRIEF.md`
  §"The Arithmetic Parameter": `β(α) = limsup_n (ln q_{n+1}(α)) /
  q_n(α)` is the operative *exponential-rate* Diophantine parameter,
  with `β(π) = 0` placing π in the Diophantine class
  (non-Liouville, non-near-Liouville).
- **Type.** Direct supply.
- **Specific edits.**
  - `memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md`: add a §"Diophantine
    classification of π" subsection (or fold into the existing
    effective-C discussion). State the parameter formula, `β(π) = 0`,
    and the implication that K-H-L-A's effective-C lives downstream
    of the Diophantine-class classification. Cite
    `rotations/10-MARTINIS-BRIEF.md` §"The Arithmetic Parameter".
  - `memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md`: cross-link to the
    Diophantine classification at Step 5 if the empirical-to-density
    proxy uses it; if A1's operational-template paragraph has already
    landed, attach this as a one-line cross-link inside that paragraph.
  - `rotations/10-MARTINIS-BRIEF.md` §"The Arithmetic Parameter":
    add back-pointer to the K-H-L-A use site.
- **Audit step (verification pass).**
  - (a) Verify the `β(π) = 0` citation chain. The 10-martinis-brief
    should already trace this to the Diophantine-approximation
    literature; spot-check the chain.
  - (b) Sweep K-H-L-A and adjacent memos for any use of `β` written
    in the wrong logarithmic form `(ln q_{n+1} / ln q_n)`. The
    cross-folder brief notes that `10-MARTINIS-BRIEF` itself was
    corrected from this form to the exponential form. If any
    miswritten references survive in K-H-L-A material, log location
    and replace.
  - (c) Verify the implication `β(α) = 0 ⟹ Diophantine class` is
    standard and correctly stated.
  - (d) Cross-reference symmetry: forward-pointer from K-H-L-A to
    `10-MARTINIS-BRIEF` and back-pointer the other way are both in
    place.
- **Dependencies.** Independent of B1 and C1; sequenced first as the
  cleanest of the three (settled-by-citation; possibly surfaces a
  correction).
- **Status.** complete; landed and verified.
- **Change in program capacity.**
  - *Before.* K-H-L-A's effective-C ambition has no fixed Diophantine
    classification of π in operative form. The parameter `β` is
    either implicit or, per the cross-folder brief's correction
    note, possibly miswritten in older material.
  - *After.* K-H-L-A has `β(π) = 0` as a load-bearing operative
    classification with citation to the modern almost-Mathieu
    literature. Any miswritten `β` references are corrected.
  - *Newly do.* K-H-L-A's effective-C analysis proceeds downstream
    of a fixed Diophantine classification. The "is π in the
    Diophantine class?" question is settled-by-citation rather than
    implicit, and the program inherits the correct exponential-rate
    parameter form for any further effective-C work.

#### A4 — CF-as-primitive ← CF-CROSSWALK extension

- **Live item.** `rotations/CONTINUED-FRACTIONS-CROSSWALK.md` itself
  — currently lists four perspectives on CF convergents (spectral /
  combinatorial / algorithmic / computational). Two perspectives
  have landed since the crosswalk was written: Beck 1994 (in iso/)
  and the K-H-L-A discrepancy branch
  (`memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md` +
  `memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md`). Sub-citation (i)
  from the plan's closing list is the load-bearing edit.
- **rotations/ supply.** `rotations/CONTINUED-FRACTIONS-CROSSWALK.md`
  is both supply and destination. The brief's §"The unified object"
  claims "we have four independent reasons to treat the continued-
  fraction convergents of α as a primitive object." After A4, the
  claim becomes "six independent reasons" — a substantive
  strengthening of the primitive-status claim.
- **Type.** Direct supply.
- **Specific edits.**
  - `rotations/CONTINUED-FRACTIONS-CROSSWALK.md` §"The four
    perspectives": add fifth and sixth perspective sub-sections.
    Fifth (Probabilistic / Diophantine, via Beck 1994): Beck
    substitutes Fourier + second-moment + Borel-Cantelli for
    continued fractions in higher-dim discrepancy of Kronecker
    sequences; the substitution preserves the Diophantine content
    the CF substrate carries in 1-dim. Sixth (Effective transcendence
    / K-H-L-A): the Aitchison × E-T-K × Kraft pairing in the K-H-L-A
    discrepancy branch uses CFs of π as the substrate for the
    empirical-to-density proxy (per A1). Rename §"The four
    perspectives" to §"The six perspectives" or analogous. This is
    sub-citation (i) from the plan's closing list and is the
    load-bearing edit for A4.
  - Same memo §"The unified object" (the table): extend table from
    four rows to six. New rows for Beck 1994 and K-H-L-A; key
    quantities documented (Beck's `(log N)^k φ(log log N)` Borel-
    Cantelli threshold; K-H-L-A's effective `C` from
    `|qπ − p| ≫ q^{−C}`).
  - Same memo §"Pointers" (bottom): extend pointer list to include
    `iso/BECK-1994-BRIEF.md`, `memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md`,
    and `memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md`.
  - Same memo §"For our program this means": update the closing
    line. From "we have four independent reasons" to "we have six
    independent reasons" — strengthening the primitive-status
    claim.
  - `iso/BECK-1994-BRIEF.md` (back-pointer): in the "adjacent
    material kept elsewhere" section or analogous, add a pointer to
    CF-CROSSWALK with the framing that Beck's Fourier-substitution
    is logged as the fifth perspective on the CF substrate.
  - `memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md` §"Adjacent anchors":
    verify back-pointer to CF-CROSSWALK is already present (line
    197 was updated in the rotations/ folder move) and that its
    framing reflects the sixth-perspective addition.
  - `memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md`: forward-pointer to
    CF-CROSSWALK in the section discussing CF substrate use (Step
    5 area); if A1's operational-template paragraph has already
    landed, add this as that Step-5 region's closing line.
- **Audit step (verification pass).**
  - (a) Verify Beck and K-H-L-A genuinely converge on the CF
    substrate. Beck explicitly substitutes Fourier-machinery *for*
    continued fractions in higher dimensions — does that count as
    "another perspective on CF" or as "a substitute for CF"? The
    1-dim case still uses CFs (Khintchine 1923) so Beck's framework
    has CF in its 1-dim ancestry. Decide framing: "Beck demonstrates
    the CF substrate's primacy by showing what's needed to substitute
    for it" or "Beck supplies a Fourier-substitute that preserves CF
    content." The latter is more honest; document accordingly.
  - (b) Verify the K-H-L-A use of CF-of-π is genuine, not metaphorical.
    The Aitchison × E-T-K × Kraft pairing must use CFs of π as
    substrate, not just discuss them. Spot-check
    `memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md` Step 5 for explicit CF-
    of-π content.
  - (c) Cross-reference symmetry: each of the new pointers (in the
    crosswalk and in the destination memos) has a matching back-
    pointer.
  - (d) Trust-boundary respect: CF-CROSSWALK is a meta-document, not
    a source-extraction brief; it has no formal "should NOT be cited
    for" section. Still, the meta-document's claim ("CF as primitive
    object") is a recurring-substrate observation, not a theorem
    about CF. Verify the new entries don't promote the observation
    to a theorem.
- **Dependencies.** Lands after A1 (A1 makes the K-H-L-A use of
  CF-of-π explicit; the crosswalk's sixth perspective references
  that). Independent of A2, A3, B1, B2, B3, C1, C2.
- **Status.** complete; A4a core CF-CROSSWALK update and A4b downstream back-pointers/audit landed and verified.
- **Change in program capacity.**
  - *Before.* CF-CROSSWALK names four independent perspectives on
    CF convergents as a primitive object: spectral, combinatorial,
    algorithmic, computational. The K-H-L-A discrepancy branch and
    Beck 1994 use the same substrate but aren't indexed at the
    crosswalk.
  - *After.* CF-CROSSWALK names six perspectives. The K-H-L-A and
    Beck uses are visible at the central index, not buried in their
    respective memos. The "CF as primitive" claim is materially
    stronger — six independent threads, not four.
  - *Newly do.* The program can cite CF-CROSSWALK as the consolidated
    primitive-status reference for CF convergents across all six
    registers (spectral / combinatorial / algorithmic / computational
    / probabilistic / effective-transcendence). Future CF uses
    inherit the index. The crosswalk becomes a substantive cross-
    folder hub, not just a 4-source rotations-internal note.

#### B1 — F-theorem proof shape ← 10-martinis template

- **Live item.** `memos/NATIVE-F-MINIMAL-DEFINITION.md` §"No-Go
  Theorem" — the closure-mismatch theorem's proof structure: assume
  `F` exists → derive cyclotomic-ladder unboundedness → contradicts
  affine flatness. Also relevant: `BNHA/VILLAINS-ANSWERED.md` §#2
  (Procrustes — three live falsifier shapes).
- **rotations/ supply.** `rotations/10-MARTINIS-BRIEF.md`
  §"Program-Facing Exports 1": "The proof pattern is 'absence of X
  implies impossible regularity'" — explicitly named as a reusable
  export. The 10-martinis instance: assume non-Cantor → derive
  fictitious analytic regularity → contradict via polar-set
  obstruction. The closure-mismatch instance fits the same
  template, with cyclotomic-ladder unboundedness in the role of the
  obstruction and affine flatness in the role of the contradicted
  regularity.
- **Type.** Methodological precedent.
- **Specific edits.**
  - `memos/NATIVE-F-MINIMAL-DEFINITION.md`: append a "Methodological
    note" after §"No-Go Theorem" recording that this proof inhabits
    the named template, with citation to
    `rotations/10-MARTINIS-BRIEF.md` §"Program-Facing Exports 1".
    This is sub-citation (ii) from the plan's closing list and is
    the load-bearing edit for B1.
  - `BNHA/VILLAINS-ANSWERED.md` §#2 (Procrustes): conditional on
    audit step (b) below — if a polar-set obstruction analog exists
    in the closure-depth context, add as a fourth Procrustes
    falsifier shape. If no clean analog, document why the
    obstruction is instance-specific and don't extend.
  - `rotations/10-MARTINIS-BRIEF.md` §"Program-Facing Exports 1":
    back-pointer noting the NATIVE-F instantiation of the template.
- **Audit step (verification pass).**
  - (a) Verify the template-match is structurally sound, not just
    rhetorically appealing. Both proofs are "absence-of-X implies
    impossible regularity" but the *kind* of regularity differs
    (continuity over a parameter space vs. flatness vs. depth).
    Check: are these the same template, or just rhyming?
  - (b) Investigate whether the 10-martinis polar-set obstruction
    has a closure-depth analog. The 10-martinis polar set is a
    specific spectral-theory object; the closure-depth analog (if
    any) might be a measure-theoretic constraint on field-extension
    degrees, or a topological constraint on a closure-generator
    moduli space. If a clean analog exists, it's a fourth
    Procrustes falsifier shape; if not, document the gap and the
    reason.
  - (c) Cross-reference symmetry: NATIVE-F → `10-MARTINIS-BRIEF`
    forward-pointer and back-pointer are both in place.
  - (d) Trust-boundary respect: `10-MARTINIS-BRIEF`'s "What The Paper
    Actually Establishes," "What The Paper Leaves Open," and
    "Program-Facing Exports" sections define the brief's payload and
    limits; verify the methodological note in NATIVE-F respects them.
    In particular: do not cite `10-MARTINIS-BRIEF` for any
    quantitative closure-depth claim — the brief is a methodological
    precedent only.
- **Dependencies.** Independent of A3 and C1. Sub-citation (ii) is
  the load-bearing edit; the conditional fourth-falsifier-shape
  extension is gated on audit step (b).
- **Status.** complete; B1a methodological note and 10-martinis back-pointer landed, B1b polar-set analog audit documented no fourth falsifier.
- **Change in program capacity.**
  - *Before.* The closure-mismatch theorem reads as a sui-generis
    program-internal proof, with no acknowledged methodological
    lineage in the modern literature.
  - *After.* The theorem inhabits a recognized template ("absence
    of X implies impossible regularity") with a precedent in the
    almost-Mathieu spectral literature. The program inherits any
    generalizations that template has been given elsewhere, and the
    F-theorem stops being orphaned: it's a member of a family.
  - *Newly do.* The program articulates its primary theorem's
    methodological lineage explicitly. Procrustes' falsifier-shape
    catalogue may gain a fourth shape if a polar-set analog exists
    in the closure-depth setting (audit pending). Independent of
    that audit's outcome, future readers of NATIVE-F can follow the
    template back to its precedent and forward to other instances
    once they accumulate.

#### B2 — iso/THREE-REGISTER pattern ← 3DT three-lens predecessor

- **Live item.** `iso/THREE-REGISTER-SYNTHESIS.md` reads "three
  independent lenses on one object" as the structural pattern of
  the iso/ work. The synthesis treats this as a discovery from the
  iso/ briefs themselves. Also relevant:
  `rotations/CONTINUED-FRACTIONS-CROSSWALK.md`, which extends the
  same pattern to four (post-A4: six) perspectives on CF
  convergents and predates iso/THREE-REGISTER-SYNTHESIS.
- **rotations/ supply.** `rotations/3DT-BRIEF.md` reads three papers
  on the same theorem — Berthé–Reutenauer (combinatorial), Lefèvre–
  Muller (algorithmic), Marklof–Strömbergsson (geometric/lattice).
  This IS the three-lens pattern, articulated before iso/ was
  conceived. Together with CF-CROSSWALK's lens-multiplication on
  CF convergents, rotations/ is the program's *first home* for the
  pattern.
- **Type.** Methodological precedent.
- **Specific edits.**
  - `iso/THREE-REGISTER-SYNTHESIS.md` Frame paragraph or Claim 1's
    witness section: add a short paragraph noting that the "three
    independent lenses on one object" pattern is the second instance
    in the program — first instance was 3DT-BRIEF (three proofs of
    one theorem); CF-CROSSWALK extends to lens-multiplication on a
    primitive substrate; iso/THREE-REGISTER-SYNTHESIS is the third
    instance and the highest-resolution version (registers with
    distinct sharpness on distinct currencies). Cite
    `rotations/3DT-BRIEF.md` and `rotations/CONTINUED-FRACTIONS-CROSSWALK.md`.
  - `rotations/3DT-BRIEF.md` §"Program-Facing Consequences" (or
    appended subsection): note that 3DT's three-lens structure was
    the program's first articulation of the pattern, and that
    iso/THREE-REGISTER-SYNTHESIS instantiated the same pattern at
    higher resolution on the isoperimetric gap. Back-pointer to
    iso/THREE-REGISTER-SYNTHESIS.
  - `rotations/CONTINUED-FRACTIONS-CROSSWALK.md`: cross-link as the
    bridge between 3DT (three lenses on a theorem) and
    iso/THREE-REGISTER-SYNTHESIS (three lenses on a gap with
    distinct sharpness). Likely folded into A4's edits since they
    touch the same memo; coordinate sequencing.
- **Audit step (verification pass).**
  - (a) Verify the structural-pattern claim is genuinely the same,
    not just rhetorically similar. 3DT's three lenses are three
    *proofs* of the same theorem; iso/'s three lenses are three
    *registers* with different sharpness on different currencies
    (rate / constant / probabilistic). Are these the same pattern,
    or different patterns sharing the "three lenses" surface? The
    honest reading: 3DT's lenses converge on the same theorem;
    iso/'s lenses each illuminate different currencies of the same
    gap. Both are "lens multiplication" but the second is more
    refined. Document the gradient explicitly.
  - (b) Cross-reference symmetry: forward-pointer from
    iso/THREE-REGISTER-SYNTHESIS to 3DT-BRIEF; back-pointer from
    3DT-BRIEF to iso/THREE-REGISTER-SYNTHESIS.
  - (c) Trust-boundary respect: 3DT-BRIEF is a source-extraction
    brief on three rotation papers. The methodological-precedent
    claim should not promote the brief beyond its source-extraction
    role. The pattern is observed *across* the brief's three sources;
    the brief itself is not a synthesis of the pattern (no claim
    that 3DT-BRIEF "established" the lens-multiplication discipline).
  - (d) CF-CROSSWALK as bridge: verify CF-CROSSWALK (with its lens-
    multiplication on CF convergents) is correctly positioned as
    the link between 3DT (three lenses on a theorem) and
    iso/THREE-REGISTER-SYNTHESIS (three lenses on a gap with
    distinct sharpness). If A4 is already populated, the link is in
    place; if not, sequence A4 before B2.
- **Dependencies.** Lands after A4 (A4 extends CF-CROSSWALK to six
  lenses, strengthening the lens-multiplication-pattern argument) and
  after B1 and B3 (which establish the methodological-precedent
  register's framing discipline that B2 inherits). Independent of A1,
  A2, A3, C1, C2.
- **Status.** complete; lens-multiplication lineage links landed and verified.
- **Change in program capacity.**
  - *Before.* iso/THREE-REGISTER-SYNTHESIS treats the "three
    independent lenses on one object" structure as a discovery from
    the iso/ briefs. The pattern feels load-bearing but isn't
    methodologically grounded — no precedent in the program for
    lens multiplication.
  - *After.* The pattern has explicit precedent: 3DT-BRIEF was the
    first instance (three proofs of one theorem); CF-CROSSWALK
    extends it (multi-lens perspectives on a primitive substrate);
    iso/THREE-REGISTER-SYNTHESIS is the third and most refined
    instance (registers with distinct sharpness). The pattern is
    visible as a *recurring* methodological move rather than a
    singular discovery.
  - *Newly do.* The program can articulate "lens multiplication" as
    a methodological pattern with multiple instances. Future cross-
    source synthesis work inherits the pattern as an established
    move. The pattern itself becomes a candidate for inclusion in
    the eventual rotations/ synthesis memo as a generalizable
    structural observation.

#### B3 — HJB-1985 §5 eigenspace ← Marklof–Strömbergsson basis vectors

- **Live item.** `fft/HEIDEMAN-JOHNSON-BURRUS-1985-BRIEF.md` §5 —
  the eigenspace identification: `K_n = Q(cos(2π/n))` is the
  `(+1)`-eigenspace of `σ_{−1}` on `Q(ζ_n)`, with decomposition
  `Q(ζ_n) = K_n ⊕ K_n · 2i sin(2π/n)`. The §5 "Conclusion" subsection
  is the natural location for the methodological back-pointer.
- **rotations/ supply.** `rotations/3DT-BRIEF.md` §"Marklof–
  Strömbergsson: The Geometric Lens" — proves 3DT in lattice form
  by basis-vector reading. Gap lengths are `r₂/N, s₂/N, (r₂+s₂)/N`
  from basis vectors `r, s` of a unimodular lattice with `r + s`
  accounting for the third value. Same "decompose 2-dim structure,
  read identity off basis" pattern as the eigenspace decomposition.
- **Type.** Methodological precedent.
- **Specific edits.**
  - `fft/HEIDEMAN-JOHNSON-BURRUS-1985-BRIEF.md` §5 Conclusion: append
    a "Methodological note" recording that the eigenspace
    decomposition's basis-vector reading has a rotations-layer
    precedent in `rotations/3DT-BRIEF.md` §"Marklof–Strömbergsson:
    The Geometric Lens." Both decompose a 2-dimensional structure
    into basis vectors and read the geometric/algebraic identity
    off the basis: the third value in 3DT (`r + s`) is the lattice-
    addition fact; the eigenspace decomposition (`K_n + K_n · 2i sin`)
    is the Galois-action fact. Cite `rotations/3DT-BRIEF.md`. Sub-
    citation (iii) from the plan's closing list; load-bearing edit
    for B3.
  - `rotations/3DT-BRIEF.md` §"Marklof–Strömbergsson: The Geometric
    Lens": back-pointer to HJB-1985 §5 noting the closure-side
    instance of the same basis-vector decomposition pattern.
  - `memos/NATIVE-F-MINIMAL-DEFINITION.md` (optional): if the memo
    references HJB-1985 §5's eigenspace identification directly, add
    a parallel note pointing to the rotations-layer precedent. Tag
    as optional — defer if NATIVE-F's existing pointer is sufficient.
- **Audit step (verification pass).**
  - (a) Verify the basis-vector pattern-match is structurally sound.
    3DT version: lattice in `R²` has basis `r, s`; gap lengths read
    off as `r₂, s₂, r₂+s₂`. Eigenspace version: `Q(ζ_n)` is 2-dim
    `K_n`-space with basis `1` and `(ζ_n − ζ_n^{−1})`; the
    decomposition `K_n + K_n · (ζ_n − ζ_n^{−1})` reads off as
    `(+1)`-eigenspace + `(−1)`-eigenspace under `σ_{−1}`. Structural
    parallel: both are 2-dim decompositions where the "third element"
    (`r + s` on one side; the `(−1)`-eigenspace generator on the
    other) is the geometric/algebraic identity-bearing object.
    Confirm or document the gap.
  - (b) Investigate whether the basis-vector pattern has further
    instances in the program. Is this a 2-instance pattern (3DT +
    HJB-1985 §5), or are there others? If only two, the
    methodological note is "first precedent" rather than "established
    pattern." Honest scoping; document accordingly.
  - (c) Cross-reference symmetry: forward-pointer from HJB-1985 §5
    to 3DT-BRIEF; back-pointer from 3DT-BRIEF to HJB-1985 §5. If
    NATIVE-F is also touched, pointers there too.
  - (d) Trust-boundary respect: `3DT-BRIEF`'s source-extraction
    framing and "Bottom Line" name the brief's payload; verify the
    methodological note in HJB-1985 §5 respects those limits.
    Do not cite 3DT-BRIEF for any quantitative closure-depth claim;
    it's a methodological precedent only. Also: do not cite the
    brief as the *source* of the basis-vector pattern (which goes
    back to ergodic theory on lattice spaces); cite as the *first
    program-internal instance*.
- **Dependencies.** Independent of A1, A2, A3, A4, B1, B2, C1, C2.
  Sub-citation (iii) is the load-bearing edit. The optional NATIVE-F
  extension can be deferred without affecting the load-bearing
  content.
- **Status.** complete; HJB §5 methodological note and 3DT back-pointer landed and verified.
- **Change in program capacity.**
  - *Before.* HJB-1985 §5's eigenspace decomposition reads as a
    sui-generis algebraic fact: Galois action on `Q(ζ_n)` decomposes
    the field into eigenspaces, the `(+1)`-side is `K_n`, basis-
    vector reading gives the closure structure. No acknowledged
    in-program precedent for the "basis-vector reading of a 2-dim
    decomposition" move.
  - *After.* The eigenspace decomposition has a rotations-layer
    precedent in Marklof–Strömbergsson's lattice formulation of 3DT.
    Both proofs use basis-vector decomposition to read identities
    off a 2-dim object. The HJB-1985 §5 result is no longer
    methodologically orphaned; it inhabits a recognized pattern (so
    far with two instances).
  - *Newly do.* Future readers of HJB-1985 §5 can follow the basis-
    vector pattern back to its rotations-layer precedent and forward
    to other instances if any accumulate. The closure-side eigenspace
    decomposition is visible as an instance of the same pattern that
    lattice geometry uses to prove 3DT — a small but real
    strengthening of the program's structural cohesion.

#### C1 — Gentle Criminal Kraft-cyclotomic bet ← 3DT BWT/Lyndon

- **Live item.** `BNHA/VILLAINS-ANSWERED.md` §#5 ("Gentle Criminal —
  partly answered: triple named, fifth coordinate identified, axioms
  still open"). The bet inside the quarantine: "marry Kraft
  arithmetic to cyclotomic complexity ... prefix-free-encoding floor
  on objects of cyclotomic depth, denominated in bits, in a model
  whose primitives don't smuggle the circle in as a free constant."
  Also relevant: `fft/FOUR-FRAMEWORK-SYNTHESIS.md` §"Construction
  Required" (the bridge construction agenda); `memos/LEDGER-PIVOT-
  SEARCH.md` §"Two paths and one sibling" (Path 2 / `V_cert`
  apparatus); `fft/PROVENANCE-AND-TRANSFERABILITY.md` §3.1
  (transferability forward — articulated bridge-construction agenda
  for successors).
- **rotations/ supply.** `rotations/3DT-BRIEF.md` §"Burrows–Wheeler
  and perfectly clustering Lyndon words" — the Ferenczi–Zamboni
  identification: every 3DT-encoding word is a perfectly-clustering
  Lyndon word. This is a finite-state characterization of
  rotation-orbit structure, with native prefix-free properties,
  separable from the circle.
- **Type.** Candidate machinery.
- **Specific edits.**
  - `BNHA/VILLAINS-ANSWERED.md` §#5, in "The bet, sharpened" or
    "What stays open": add a candidate-path bullet citing the
    Ferenczi–Zamboni Lyndon-word characterization as a specific
    construction candidate from rotation-orbit data to Kraft-shaped
    bookkeeping. Frame strictly as candidate, not result.
  - `memos/LEDGER-PIVOT-SEARCH.md` §"Two paths and one sibling":
    add a sub-paragraph noting that Path 2's bridge construction
    has a candidate machinery via 3DT BWT/Lyndon — separable from
    the circle, with native prefix-free properties. Cross-link
    `rotations/3DT-BRIEF.md`. Watch the recently-restructured
    section's flow; the addition should sit cleanly inside
    "Two paths and one sibling" without reintroducing a bolted-on
    feel.
  - `fft/FOUR-FRAMEWORK-SYNTHESIS.md` §"Source Inputs To The
    Construction" (or analogous section for new candidate inputs):
    list 3DT/Lyndon as a candidate source for the Kraft side of
    the fifth-coordinate construction, alongside the four briefed
    frameworks.
  - `fft/PROVENANCE-AND-TRANSFERABILITY.md` §3.1 (articulated
    bridge-construction agenda): note 3DT BWT/Lyndon as a
    candidate machinery for the Kraft side; flag explicitly that
    closure of the candidate is itself an open construction
    question that successors inherit as work, not as supply.
  - `rotations/3DT-BRIEF.md` §"Burrows–Wheeler and perfectly
    clustering Lyndon words" (or an adjacent program-facing note):
    back-pointer to §#5 of VILLAINS-ANSWERED and the
    bridge-construction agenda. Frame as: the BWT/Lyndon
    characterization is a candidate machinery for the Kraft-
    cyclotomic bridge; the bridge is not yet constructed.
- **Audit step (verification pass).**
  - (a) Cross-reference symmetry: each forward-pointer from program
    memos to `rotations/3DT-BRIEF` has a matching back-pointer.
    Four forward-pointers expected (one each in VILLAINS-ANSWERED,
    LEDGER-PIVOT-SEARCH, FOUR-FRAMEWORK-SYNTHESIS, and PROVENANCE-AND-
    TRANSFERABILITY), plus matching back-pointer(s) in 3DT-BRIEF.
  - (b) Candidate-not-result framing check. Spot every uplift edit
    for verb tense and modal language. The phrase "candidate path"
    or "candidate machinery" should appear; phrases that imply
    closure ("constructs", "completes", "supplies the bridge")
    should not.
  - (c) Trust-boundary respect: `3DT-BRIEF`'s source-extraction
    framing and "Bottom Line" name the brief's payload; verify
    uplifts respect those limits. Specifically:
    `3DT-BRIEF` is a source-extraction brief on three rotation
    papers, not a proof of any cyclotomic-Kraft bridge. Uplifts
    must not cite the brief for the bridge itself, only for the
    Ferenczi–Zamboni Lyndon-word characterization that the brief
    extracts.
  - (d) Successor-readability check: a successor reader should be
    able to follow VILLAINS-ANSWERED §#5 → `rotations/3DT-BRIEF`
    §"Burrows–Wheeler and perfectly clustering Lyndon words" and
    understand (i) what closing the bridge would entail and (ii)
    why 3DT supplies a candidate path rather than a closed
    construction.
- **Dependencies.** Lands after A3 (settled-by-citation; cleanest
  first) and B1 (methodological note; independent technique).
  C1 is the highest-leverage and the most candidate-shaped, so
  most care is required to avoid overclaiming. Sequencing
  detailed in §2.2.
- **Status.** complete; C1a forward candidate edits and C1b framework/provenance edits plus 3DT back-pointer landed and verified.
- **Change in program capacity.**
  - *Before.* The compute-cost branch has a named bet (Kraft
    arithmetic ↔ cyclotomic complexity, no smuggling) but no
    machinery. The bet is a placeholder for whatever construction
    would close it. `VILLAINS-ANSWERED` §#5 names the bet's
    shape; no candidate machinery has been on file.
  - *After.* The bet has a specific candidate machinery (Lyndon-
    word prefix-free encoding, Ferenczi–Zamboni) drawn from 3DT
    structure. The candidate is finite-state, prefix-free, and
    separable from the circle — i.e., it is shaped exactly as
    Gentle Criminal's bet asked for. The fifth-coordinate
    construction agenda in `FOUR-FRAMEWORK-SYNTHESIS` and
    `PROVENANCE-AND-TRANSFERABILITY` gains a named candidate
    input on the Kraft side.
  - *Newly do.* The program states the bet's bridge construction
    with at least one concrete candidate path. The construction
    question becomes: does Ferenczi–Zamboni's prefix-free Lyndon
    characterization compose with cyclotomic-depth accounting in
    a model whose primitives don't smuggle the circle? That is
    now a specific construction problem with named ingredients,
    not a placeholder for unknown machinery. Successor work has a
    specific target to attempt or refute, rather than an
    unstructured "find a bridge."

#### C2 — Two-sided log/circle objects ← Lefèvre–Muller log-side native

- **Live item.** The program seeks objects that natively live on
  both log and circle sides. Currently relevant locations:
  `memos/LANDFALL-EXPORT.md` (log side: `ε(m) = log_2(1+m) − m`),
  `memos/NATIVE-F-MINIMAL-DEFINITION.md` (circle side via `K_n`),
  `memos/STRIP-H1-HURWITZ-CLOSURE.md` (strip-side bridge),
  `BNHA/triad/PLUS_ULTRA.md` (the program's two-sided framing in the
  triad disciplines), and the triad memos in `BNHA/triad/`. The two-sided
  pattern is the program's core architecture but has no central
  catalog of named instances.
- **rotations/ supply.** `rotations/3DT-BRIEF.md` §"Lefèvre–Muller–
  Tisserand: The Algorithmic Lens" — flags 3DT's table-maker's-dilemma
  deployment as "log-side native, not merely a circle-side theorem
  later imported into log-side questions." Lefèvre–Muller use 3DT
  inside a real floating-point filtering algorithm; the orbit
  structure is on `R/Z` but the substrate is log-side machine
  arithmetic. Same brief §"Three-Way Correspondence" enumerates the
  four avatars (rotation orbit, combinatorial word, algorithmic
  loop, lattice function) — the algorithmic avatar IS the log-side
  native instance.
- **Type.** Candidate machinery (i.e., 3DT is offered as a worked
  example of two-sided objects, but the synthesis "two-sided objects
  as a class" is open).
- **Specific edits.**
  - `BNHA/triad/PLUS_ULTRA.md` (or the triad's two-sided framing
    location; if a more specific two-sided memo exists, prefer it):
    note that the program's two-sided pattern has an articulated
    worked example in 3DT, with explicit log-side native deployment
    via Lefèvre–Muller. Cite `rotations/3DT-BRIEF.md`
    §"Lefèvre–Muller–Tisserand: The Algorithmic Lens" and §"Three-Way
    Correspondence." Frame strictly as candidate or worked example,
    not as result.
  - `memos/STRIP-H1-HURWITZ-CLOSURE.md` (strip-side bridge memo):
    cross-reference 3DT as an older worked example of two-sided
    structure on rotation orbits. Frame as adjacent worked example
    in the program's catalog of two-sided primitives.
  - `memos/NATIVE-F-MINIMAL-DEFINITION.md` (closure-mismatch theorem):
    note near §"Why `K_n` (forced by closure)" or in a distinct
    methodology note that `K_n`'s
    two-sidedness (algebraic on one side, geometric on the other)
    joins 3DT (orbit on circle, machine arithmetic on log) as a
    pair of two-sided primitives in the program. Frame as pattern
    observation, not theorem.
  - `rotations/3DT-BRIEF.md` §"Program-Facing Consequences",
    subsection "3. 3DT is both circle-side and log-side" (or an
    appended adjacent subsection): back-pointer noting 3DT's role as
    the program's first explicit two-sided primitive. Cross-link to
    NATIVE-F-MINIMAL-DEFINITION (`K_n` as second), STRIP-H1-HURWITZ-
    CLOSURE (strip-bridge), `BNHA/triad/PLUS_ULTRA.md` (triad
    framing).
  - Deferred to synthesis memo: a sub-section in the eventual
    rotations/ synthesis memo on "two-sided primitives as a class,"
    with 3DT and `K_n` as instances. Not part of C2 itself; flagged
    for the synthesis-memo scope (§2.4).
- **Audit step (verification pass).**
  - (a) Verify 3DT is genuinely two-sided in the same sense `K_n`
    is. `K_n`'s two-sidedness: algebraic on one side (Galois action
    on `Q(ζ_n)`), geometric on the other (real subfield of
    `cos(2π/n)`). 3DT's two-sidedness: rotation orbit on the
    geometric circle (`R/Z`), Lefèvre–Muller deployment on machine
    arithmetic (log side). The "sides" differ in each case — for
    3DT it's circle-vs-machine-arithmetic; for `K_n` it's algebraic-
    vs-geometric. Are these the same kind of two-sidedness? Honest
    answer: probably not exactly the same, but both are "natively-
    on-two-sides primitives" in the program's broader sense.
    Document the distinction.
  - (b) Verify 3DT's log-side native status holds up in the brief's
    framing. The brief says "3DT is not just circle-side material
    that can be exported; it already has a native log-side
    occurrence." Check: does Lefèvre–Muller use 3DT *intrinsically*
    (the algorithm requires 3DT structure) or *incidentally* (3DT
    happens to be a useful tool)? The brief reads it as intrinsic;
    verify against the source.
  - (c) Cross-reference symmetry: each forward-pointer from program
    memos to 3DT-BRIEF has a back-pointer.
  - (d) Candidate-not-result framing check (same discipline as C1).
    Phrases "two-sided primitives," "worked example," "candidate
    class" should appear; phrases that imply closure ("establishes
    the two-sided class," "supplies the unification," "completes
    the pattern") should not. Same verb-tense and modal-language
    scrutiny as C1's audit step (b).
  - (e) Trust-boundary respect: 3DT-BRIEF is a source-extraction
    brief on three rotation papers. The two-sided-class observation
    is a program-internal observation derived from the brief, not a
    result the brief proves. Frame the citation accordingly.
- **Dependencies.** Lands after A1 (A1 establishes Lefèvre–Muller as
  the operational template for the K-H-L-A proxy; C2 leverages the
  same Lefèvre–Muller for the broader two-sided-class observation),
  B1 (B1's methodological-note discipline is the template for C2's
  pattern observation), and ideally C1 (C1 establishes the
  candidate-machinery framing discipline that C2 inherits). Most
  candidate-shaped of the remaining five; needs the most care.
  Sequenced last in the second batch.
- **Status.** complete; C2a program-side two-sided catalog edits and C2b
  3DT back-pointer landed and verified, with two-sidedness/candidate-
  language audit complete.
- **Change in program capacity.**
  - *Before.* The program's two-sided pattern (log + circle, or
    algebraic + geometric, or strip + curve) is articulated across
    multiple memos but not catalogued as a class with named
    instances. `K_n` is implicitly two-sided (closure-mismatch
    theorem). The strip is implicitly two-sided (STRIP-H1-HURWITZ-
    CLOSURE). 3DT is implicitly two-sided (Lefèvre–Muller). No
    single memo catalogs the class.
  - *After.* The two-sided pattern has at least two named instances
    (3DT, `K_n`) with worked examples each, and a candidate third
    (strip bridge). The pattern is visible as a recurring program
    architecture rather than a triad-discipline assumption. The
    eventual rotations/ synthesis memo can pull the catalog into a
    single section.
  - *Newly do.* The program names its two-sided architecture
    explicitly, with examples. Future two-sided-primitive candidates
    (whether they emerge from rotations/, fft/, iso/, or elsewhere)
    can be checked against the candidate class as articulated.
    Successor work has a starting catalog: 3DT (rotation/log-
    arithmetic), `K_n` (algebraic/geometric); the strip bridge as
    candidate third; future work may add a fourth.

### 2.2 Sequencing

With all nine targets populated, the recommended order is

**A3 → A1 → A4 → A2 → B1 → B3 → B2 → C1 → C2**

by ascending closure risk (direct supply → methodological precedent →
candidate machinery), with within-tier dependencies respected. Each
target's audit step runs after its own edits land; the full cross-
folder consistency check (§2.3) runs once after all nine targets
close.

This reorders the previously-recorded four-target prefix
(A3 → A1 → B1 → C1). Two structural reasons force the change once
the second batch's plans are in: A4 must precede B2 (B2's three-lens
pattern observation cites CF-CROSSWALK's lens-multiplication, which
A4 extends from four to six perspectives), and C2 must follow C1,
A1, and B1. Risk-tier ordering — direct supply settled first,
methodological precedents next, candidate machinery last — also
produces a cleaner narrative for the eventual synthesis memo:
substrate-then-pattern-then-candidate.

Per-target sequencing rationale:

- **A3 first.** Settled-by-citation; lowest closure risk; potentially
  surfaces a `β`-form correction in K-H-L-A material (A3 audit step
  b). Pure technical input. Lands as warmup.
- **A1 second.** Direct supply for the K-H-L-A discrepancy branch's
  Step-5 proxy. Sequenced after A3 because A3's `β(π) = 0`
  Diophantine classification is the substrate the proxy's analysis
  rests on; this ordering avoids forward references. Sub-citation
  (iv) is the load-bearing edit.
- **A4 third.** Extends CF-CROSSWALK from four to six perspectives,
  citing K-H-L-A's CF-of-π use (made explicit by A1) and Beck 1994's
  Fourier-substitute. Sub-citation (i) is the load-bearing edit.
  Sequenced after A1 because the K-H-L-A use must be explicit before
  it can be cross-referenced from the crosswalk.
- **A2 fourth.** BIND-audit safety direct supply; independent of all
  other targets. Placed inside the direct-supply tier so the
  discrepancy-register cluster (A1, A4, A2 — all touching K-H-L-A /
  Beck / discrepancy-audit material) is contiguous. Audit-discipline
  consolidation rather than a new operational template; lower-leverage
  than A1, A3, A4.
- **B1 fifth.** Methodological-note edit in NATIVE-F (sub-citation
  (ii)) plus a conditional fourth-falsifier-shape extension to
  VILLAINS-ANSWERED §#2 gated on a structural audit (B1 audit step
  b). Independent of other B-tier targets; sequenced first within
  the methodological-precedent tier as the anchor for the proof-shape
  pattern that later B's borrow from in tone.
- **B3 sixth.** HJB-1985 §5 methodological note (sub-citation (iii)).
  Independent of other targets. Lands here so the basis-vector
  pattern observation is recorded before B2's three-lens pattern
  (which is the more refined sibling).
- **B2 seventh.** Three-lens pattern observation, with iso/THREE-
  REGISTER-SYNTHESIS as the high-resolution instance. Sequenced
  after A4 (CF-CROSSWALK's lens-multiplication is the bridge between
  3DT and iso/) and after B1, B3 (which establish the methodological-
  precedent register's framing discipline that B2 inherits).
- **C1 eighth.** Highest leverage, most candidate-shaped. Sequenced
  after A3 and B1 (its named dependencies) and after the rest of
  the direct-supply and methodological-precedent tiers so the
  framing-discipline observations land into a stable substrate. The
  candidate-not-result framing requires the most care; landing C1
  with all foundations in place reduces the risk of accidental
  claim escalation.
- **C2 ninth.** Two-sided primitives as candidate class. Sequenced
  last because it depends on A1 (Lefèvre–Muller as operational
  template), B1 (methodological-note discipline), and ideally C1
  (candidate-machinery framing discipline). C2 is the most
  candidate-shaped of the candidate-machinery tier and inherits the
  most framing discipline from earlier targets.

Cross-target conflicts to coordinate during execution:

- **3DT-BRIEF as cross-target hub.** Six targets (A1, A2, B2, B3,
  C1, C2) add back-pointers to `rotations/3DT-BRIEF.md`. Each
  target's back-pointer attaches to the appropriate source-section
  ("Lefèvre–Muller–Tisserand: The Algorithmic Lens" for A1; "Program-Facing
  Consequences" subsection 2 for A2 and subsection 3 for C2;
  "Marklof–Strömbergsson: The Geometric Lens" for B3;
  "Burrows–Wheeler and perfectly clustering Lyndon words" for C1;
  "Program-Facing Consequences" for B2). Each
  landing must respect the others' attachment points; running each
  target's 3DT-BRIEF back-pointer pass last in that target's own
  edits avoids stepping on prior additions.
- **KRAFT-BUDGET-ONE-DIMENSIONAL Step 5 as triple-touchpoint.** A1
  (sub-citation (iv)), A3 (Diophantine cross-link), and A4 (forward-
  pointer to CF-CROSSWALK) all converge on Step 5. The edits should
  compose into a single coherent Step-5 "operational precedents"
  region rather than stacking three sibling paragraphs. Recommend:
  A1 lands the operational-template paragraph; A3 attaches a one-
  line Diophantine cross-link inside it; A4 adds the forward-pointer
  to CF-CROSSWALK as the closing line.
- **CF-CROSSWALK ordering.** A4 (extension to six perspectives)
  lands before B2 (cross-link as bridge between 3DT and iso/THREE-
  REGISTER-SYNTHESIS). The sequencing places A4 at position 3, B2
  at position 7 — A4 closes well before B2 needs the six-perspectives
  version.
- **NATIVE-F-MINIMAL-DEFINITION as triple-touchpoint.** B1 appends
  a methodological note (sub-citation (ii), load-bearing); B3
  optionally adds a parallel note pointing to the rotations-layer
  basis-vector precedent (deferrable); C2 may add a pattern
  observation about K_n's two-sidedness near the `K_n` discussion or
  in a distinct methodology note. Recommend: B1 lands the
  load-bearing note; B3's
  optional addition skipped unless its audit specifically calls for
  it; C2's two-sidedness observation goes into a distinct note near
  the `K_n` discussion.
- **VILLAINS-ANSWERED.** B1 (§#2 conditional fourth falsifier
  shape); C1 (§#5 candidate-path bullet). Different sections; low
  conflict risk.
- **iso/THREE-REGISTER-SYNTHESIS.** A2 (Beck-audit forward-pointer
  in §2.3 sub-thread); B2 (frame paragraph or Claim 1 witness).
  Different sections; low conflict risk.
- **LEDGER-PIVOT-SEARCH.** C1 adds a sub-paragraph in §"Two paths
  and one sibling." The memo was recently restructured; the C1
  addition must respect the restructured flow rather than
  reintroducing a bolted-on feel that the structural-repair pass
  removed.

### 2.3 Cross-folder consistency check

The full nine-target plan crosses five folder boundaries:

- **rotations/ ↔ memos/.** A1 (KRAFT-BUDGET-ONE-DIMENSIONAL, 3DT-
  BRIEF). A2 (OLD-TIME-RELIGION, 3DT-BRIEF). A3 (KRAFT-HERMITE-
  LINDEMANN-AITCHISON, KRAFT-BUDGET-ONE-DIMENSIONAL, 10-MARTINIS-
  BRIEF). A4 (CF-CROSSWALK as primary edit, with sibling pointers
  in KRAFT-HERMITE-LINDEMANN-AITCHISON and KRAFT-BUDGET-ONE-
  DIMENSIONAL). B1 (NATIVE-F-MINIMAL-DEFINITION, 10-MARTINIS-BRIEF).
  C1 (LEDGER-PIVOT-SEARCH, 3DT-BRIEF). C2 (NATIVE-F-MINIMAL-
  DEFINITION, STRIP-H1-HURWITZ-CLOSURE, 3DT-BRIEF).
- **rotations/ ↔ BNHA/.** B1 (VILLAINS-ANSWERED §#2, conditional on
  audit). C1 (VILLAINS-ANSWERED §#5). C2
  (`BNHA/triad/PLUS_ULTRA.md` or analogous two-sided framing location
  in the triad).
- **rotations/ ↔ fft/.** B3 (HEIDEMAN-JOHNSON-BURRUS-1985-BRIEF §5).
  C1 (FOUR-FRAMEWORK-SYNTHESIS, PROVENANCE-AND-TRANSFERABILITY).
- **rotations/ ↔ iso/.** A1 (BECK-1994-BRIEF, optional cross-link).
  A2 (THREE-REGISTER-SYNTHESIS Claim 2 §2.3). A4 (BECK-1994-BRIEF,
  back-pointer to crosswalk). B2 (THREE-REGISTER-SYNTHESIS Frame
  paragraph or Claim 1 witness section).
- **rotations/ ↔ rotations/.** A4 extends CF-CROSSWALK; B2 then
  references the extended crosswalk. Internal-to-rotations boundary;
  ordering already enforced by §2.2 sequencing.

After all nine targets land, a single consistency pass verifies:

- (a) **Forward-pointer / back-pointer symmetry** across each
  cross-folder boundary. Every program-memo → rotations/ pointer
  has a matching rotations/ → program-memo back-pointer. Special
  attention to 3DT-BRIEF, where six targets contribute back-
  pointers to coordinated source-sections/subsections (per §2.2 hub
  note).
- (b) **Trust-boundary respect.** Every uplift cite respects the
  source brief's stated payload and limits. `10-MARTINIS-BRIEF`
  records these through "What The Paper Actually Establishes," "What
  The Paper Leaves Open," and "Program-Facing Exports"; `3DT-BRIEF`
  records them through "Program-Facing Consequences" and "Bottom
  Line." Per-target audit steps name the specific limits to check.
- (c) **No accidental claim escalation.** Each integration's
  framing remains type-appropriate (direct supply / methodological
  precedent / candidate machinery), not silently promoted across
  the boundary. Specific high-risk targets: C1 and C2 (candidate
  machinery, where closure-implying language is easiest to slip
  into); B1's conditional fourth-falsifier extension (gated on
  B1 audit step b); A4's "six perspectives" claim (whether Beck
  counts as "another perspective on CF" or as "a substitute for
  CF"; A4 audit step a settles the framing).
- (d) **No regression in restructured memos.** The C1 sub-paragraph
  in `LEDGER-PIVOT-SEARCH.md` §"Two paths and one sibling" should
  sit cleanly inside the recently-restructured section. The
  `FOUR-FRAMEWORK-SYNTHESIS.md` and `PROVENANCE-AND-TRANSFERABILITY.md`
  additions should respect the existing structure rather than
  attaching mini-sections.
- (e) **Cross-target conflict resolution.** Where multiple targets
  touch the same memo (3DT-BRIEF for six targets; KRAFT-BUDGET
  Step 5 for three; NATIVE-F for three; CF-CROSSWALK for two),
  verify the edits compose into coherent sections rather than
  stacking sibling paragraphs. The §2.2 cross-target conflicts
  list names the specific recommendations.
- (f) **Sub-citation completeness.** All four sub-citation pieces
  ((i)–(iv)) have landed as part of their parent targets (A4, B1,
  B3, A1 respectively), with no orphaned references.

**Status.** complete; post-nine-target consistency pass run after C2.
Small fixes landed for stale 3DT section-title references and guardrail
phrasing in two-sided/candidate notes. Pointer symmetry, trust-boundary
language, claim-escalation checks, shared-memo composition, and
sub-citation completeness verified.

### 2.4 Final synthesis memo

With all nine targets populated and sequenced, the synthesis memo's
load-bearing claim — **the rotations/ register sits underneath the
program's three named registers (algebraic-closure / Sobolev /
discrepancy) as a substrate of methodological patterns and
operational machinery, not as a peer fourth register** — has its
full evidence set assembled. The synthesis memo itself remains
**deferred until all nine targets close** and the §2.3 consistency
pass confirms trust-boundary discipline holds.

The full evidence set, organized by substrate role:

**Operational supply (program bets gain templates and candidate paths).**
The bucket label is a substrate-role descriptor and is distinct from
the per-target Type field "candidate machinery": A1 is direct supply
of a worked operational template; C1 and C2 are candidate machinery
proposed for the same supply role.

- **C1** supplies a candidate path (Kraft-cyclotomic via Ferenczi–
  Zamboni Lyndon words) for the program's central open bet
  (Gentle Criminal §#5).
- **A1** supplies the 1-dim algorithmic operational template
  (Lefèvre–Muller compressed-orbit pseudocode) for the K-H-L-A
  empirical-to-density proxy.
- **C2** names the program's two-sided primitives as a candidate
  class with worked examples (3DT, K_n) and a candidate third
  (strip bridge).

**Methodological pattern lineage (program patterns gain in-house
precedents).**

- **B1** records the F-theorem proof shape ("absence-of-X implies
  impossible regularity") as a 10-martinis-articulated template
  predating NATIVE-F.
- **B2** records the three-lens pattern as a recurring move with
  three instances of increasing resolution: 3DT (three proofs of
  one theorem), CF-CROSSWALK (lens multiplication on a primitive
  substrate), iso/THREE-REGISTER-SYNTHESIS (three registers with
  distinct sharpness on distinct currencies).
- **B3** records the basis-vector decomposition pattern ("decompose
  2-dim structure, read identity off basis") as a two-instance
  pattern across HJB-1985 §5 (algebraic) and Marklof–Strömbergsson
  (geometric).

**Direct technical input (program work gains specific quantities).**

- **A3** supplies the Diophantine classification of π via β(π) = 0,
  the operative exponential-rate parameter for K-H-L-A's effective-
  C ambition.
- **A4** strengthens the "CF as primitive" claim from four to six
  independent perspectives (spectral / combinatorial / algorithmic /
  computational / probabilistic / effective-transcendence).
- **A2** supplies a worked precedent for BIND-audit safety on
  Fourier-discrepancy machinery, moving the discrepancy register's
  audit verdict from "isolated audit on Beck" to "audit-with-
  precedent."

The synthesis memo will record these nine pieces as primary
evidence and articulate the substrate-vs-peer-register reading of
the rotations/ folder. The three-bucket structure (operational
machinery / methodological pattern lineage / direct technical
input) is the natural skeleton for the memo's argument. No
commitment yet on the synthesis memo's title or filename; that
decision waits until all nine targets close.

### 2.5 Status tracker

| Target | Tier | Sequence | Status |
|---|---|---:|---|
| A3 | direct supply | 1 | complete; landed and verified |
| A1 | direct supply | 2 | complete; landed and verified |
| A4 | direct supply | 3 | complete; landed and verified |
| A2 | direct supply | 4 | complete; landed and verified |
| B1 | methodological precedent | 5 | complete; landed and verified |
| B3 | methodological precedent | 6 | complete; landed and verified |
| B2 | methodological precedent | 7 | complete; landed and verified |
| C1 | candidate machinery | 8 | complete; landed and verified |
| C2 | candidate machinery | 9 | complete; landed and verified |

| Sub-citation | Parent target | Sequence | Status |
|---|---|---:|---|
| (iv) Lefèvre–Muller cite in KRAFT-BUDGET Step 5 | A1 | 2 | complete; landed as part of A1 |
| (i) CF-CROSSWALK → 6 perspectives | A4 | 3 | complete; six-perspectives core plus reciprocal pointers landed |
| (ii) 10-martinis cite in NATIVE-F | B1 | 5 | complete; landed in B1a |
| (iii) Marklof–Strömbergsson cite in HJB-1985 §5 | B3 | 6 | complete; landed as part of B3 |

### 2.6 Implementation chunking

The full work decomposes into fourteen turns: thirteen for the nine
targets plus the §2.3 consistency pass, with a fourteenth for the
post-plan relaxation review (§2.7). Splits inside L targets respect
target-boundary effort; sequencing (§2.2) and total workset are
unchanged.

#### Per-target effort

| Target | S/M/L | Turns | Basis |
|---|:---:|:---:|---|
| A3 | M | 1.0 | 3 files; one technical subsection plus two pointers; β-form sweep is real verification. |
| A1 | M | 1.0 | 2 required files + optional Beck link; one load-bearing Step 5 paragraph; careful pseudocode/Beck audit. |
| A4 | L | 1.5–2.0 | 4 files; CF-CROSSWALK rewrite/table/pointers plus satellites; Beck-vs-CF framing audit is nontrivial. |
| A2 | M | 1.0 | 3 files; two forward paragraphs + 3DT backpointer; BIND spot-check across 3DT/Beck/Aitchison. |
| B1 | L | 1.5–2.0 | 3 possible files; NATIVE-F note plus 10M backpointer; polar-set analog audit may drive conditional BNHA edit. |
| B3 | S | 0.5 | 2 required files, optional NATIVE-F; compact methodology note/backpointer; audit is grep/structural spot-check. |
| B2 | M | 1.0 | 3 files; one pattern paragraph, 3DT backpointer, CF-CROSSWALK bridge; conceptual-pattern audit. |
| C1 | L | 1.5–2.0 | 5 files; four forward candidate edits + 3DT backpointer; candidate-language and LEDGER-flow audits are heavy. |
| C2 | L | 1.5–2.0 | 4 files + deferred synthesis note; three catalog edits + 3DT backpointer; two-sidedness audit is concept-heavy. |

#### Proposed chunking

1. **Turn 1 — A3.** Land K-H-L-A β classification, Step 5 cross-link,
   10-MARTINIS-BRIEF back-pointer; run β-form sweep. (~1 turn.)
2. **Turn 2 — A1.** Land Step 5 operational-template paragraph, 3DT
   back-pointer, optional Beck cross-link; verify pseudocode and
   Beck pairing. (~1 turn.)
3. **Turn 3 — A4a.** Update CF-CROSSWALK core: rename four → six
   perspectives, add Beck and K-H-L-A perspectives, extend unified
   table and internal closing line. (~1 turn.)
4. **Turn 4 — A4b.** Add satellite pointers/back-pointers in
   BECK-1994-BRIEF, KRAFT-HERMITE-LINDEMANN-AITCHISON, KRAFT-
   BUDGET-ONE-DIMENSIONAL; complete A4 framing audit.
   (~0.75–1 turn.)
5. **Turn 5 — A2.** OLD-TIME-RELIGION paragraph,
   iso/THREE-REGISTER-SYNTHESIS Claim 2 §2.3 forward-pointer, 3DT
   back-pointer; BIND spot-check. (~1 turn.)
6. **Turn 6 — B1a.** NATIVE-F-MINIMAL-DEFINITION methodological
   note and 10-MARTINIS-BRIEF back-pointer only.
   (~0.75–1 turn.)
7. **Turn 7 — B1b.** Polar-set analog audit; either add conditional
   VILLAINS-ANSWERED §#2 fourth falsifier or document non-extension.
   (~0.75–1 turn.)
8. **Turn 8 — B3 + B2.** First B3's HJB-1985 §5 methodological note
   and 3DT back-pointer; then B2's iso/THREE-REGISTER-SYNTHESIS,
   3DT, and CF-CROSSWALK pattern links. (~1.25 turns.)
9. **Turn 9 — C1a.** VILLAINS-ANSWERED §#5 and LEDGER-PIVOT-SEARCH
   §"Two paths and one sibling" candidate-path edits. (~1 turn.)
10. **Turn 10 — C1b.** FOUR-FRAMEWORK-SYNTHESIS, PROVENANCE-AND-
    TRANSFERABILITY, then 3DT back-pointer last; full candidate-
    not-result audit. (~1 turn.)
11. **Turn 11 — C2a.** BNHA/triad/PLUS_ULTRA, STRIP-H1-HURWITZ-
    CLOSURE, NATIVE-F-MINIMAL-DEFINITION two-sided catalog edits.
    (~1 turn.)
12. **Turn 12 — C2b.** 3DT back-pointer and two-sidedness/
    candidate-language audit. (~0.75–1 turn.)
13. **Turn 13 — §2.3 consistency pass.** Pointer symmetry,
    trust-boundary discipline, claim-escalation check, shared-memo
    composition, sub-citation completeness. (~1 turn.)
14. **Turn 14 — Post-plan relaxation review.** Sweep semi-related
    docs (everything not plan-touched) for small consolidation /
    extension / fill-in edits made possible by the just-landed
    integrations. See §2.7 for the full punch list across five
    categories plus paper-readiness verdict. (~1–1.5 turns;
    effectively two sub-turns: small Category 1–3 edits land
    quickly, while the Category 4–5 paper-prep work — synthesis
    memo writing, top-level theorem statement scaffolding — is
    flagged for follow-up turns and is post-plan in scope.)

#### Fragility flags

- **A4 split (Turns 3–4).** After Turn 3, CF-CROSSWALK is
  internally coherent but satellite memos do not yet point back.
  No claims should imply the downstream back-pointers already
  exist.
- **B1 split (Turns 6–7).** After Turn 6, NATIVE-F has the
  load-bearing methodological note; VILLAINS-ANSWERED §#2 stays
  intentionally untouched until the polar-set analog audit
  determines whether the fourth-falsifier extension lands.
- **C1 split (Turns 9–10).** After Turn 9, forward candidate edits
  exist without the 3DT back-pointer. Turn 10 must run the 3DT
  back-pointer pass last, per §2.2.
- **C2 split (Turns 11–12).** After Turn 11, program-side catalog
  edits exist without the 3DT reciprocal pointer. Turn 12 finishes
  pointer symmetry and the candidate-framing audit.
- **Final pass standalone.** Turn 13 (§2.3 consistency pass) must
  remain its own turn; it is the only place that sees cross-target
  composition across 3DT-BRIEF, KRAFT-BUDGET Step 5,
  NATIVE-F-MINIMAL-DEFINITION, and CF-CROSSWALK simultaneously.
- **Turn 14 reconnaissance, not landing.** Turn 14's paper-prep
  surfacings (synthesis-memo scope, top-level theorem statement)
  are inventoried but not scheduled inside the plan; they land in
  follow-up turns after the file freezes.

### 2.7 Turn 14 — Post-plan relaxation review

Sweep semi-related docs (everything not plan-touched) for small
edits made possible by the just-landed integrations. Punch list
across five categories, plus a paper-readiness verdict.

**Frame.** The plan integrations have landed (Turns 1–13). This is
reconnaissance for what the post-landing state enables in docs the
plan did not directly touch. Most items are pointer-only or
one-line; a few flag larger paper-prep work that the plan inventories
but does not own.

#### Category 1 — Stale framing

- **`memos/AGENTS.md`** "Recurring gotchas" — missing β(π) = 0
  entry (Diophantine class settlement) and Ferenczi–Zamboni Lyndon-
  word entry (candidate Kraft-cyclotomic machinery). *paragraph.*
- **`BNHA/triad/Creati/CREATI-THE-CIRCLE.md`** §C5 — "The other two
  legs … are not pursued here" reads stale once `rotations/` briefs
  supply the machinery for the crystallographic-↔-p-adic and
  spectral-rhyme legs. *one-line revise.*
- **`n-gons/N-GON-WHOLENESS.md`** §"Open directions" — Ferenczi–
  Zamboni opens a *candidate path* (not closure) for running-mean
  envelope work; entry should say "candidate path now articulated;
  see rotations/3DT-BRIEF and the C1 candidate-machinery line."
  *paragraph, with strict candidate framing.*

#### Category 2 — Orphan claims now resolvable

- **`memos/COUNTING-APPARATUS.md`** §(D) walkthrough — Gauss–Wantzel
  constructibility check feeds compute-model primitives; A3's
  Diophantine classification of π and C1's candidate Kraft-
  cyclotomic machinery now sit downstream. *one-line ×2.*
- **`memos/LIOUVILLE-SCALE-TEST.md`** ~line 248 — "cyclotomic units
  and sine-product identities" reserve mention; CF-CROSSWALK 6-
  perspectives placement is now where those identities sit.
  *one-line.*
- **`memos/RAMANUJANS-COMPLIMENT.md`** — Ramanujan upper bounds
  now have rotations/-side comparison via 3DT and CF machinery.
  *one-line.*

#### Category 3 — Missing back-references

- **`BNHA/VILLAINS-ANSWERED.md` §#6 (Daedalus).** "Name the
  staircase" answer should reference C1's candidate Kraft-
  cyclotomic machinery and A1's empirical-to-density proxy as
  candidate staircase pieces. (NOT plan-touched: §#2 and §#5 only.)
  *paragraph; highest-leverage edit in the punch list.*
- **`BNHA/triad/Eraserhead/BIND-THE-CIRCLE.md`** Step 4 — Leg 3
  obstruction-construction PLUS ULTRA slots lack pointers to
  `rotations/3DT-BRIEF.md` (lattice machinery) and
  `rotations/CONTINUED-FRACTIONS-CROSSWALK.md` (CF machinery).
  *pointer-only ×2.*
- **`BNHA/triad/Eraserhead/ARCHIMEDEAN-CONSTRICTION.md`** §"The
  3DT reading" — should point to `rotations/3DT-BRIEF.md` §"The
  third angle" for the specific lattice reading. *pointer-only.*
- **`BNHA/triad/NIVEN-THREE-WAYS.md`** §"What this previews about
  F" — Bamberg–Cairns–Kilminster ψ cited without source; add
  pointer to `n-gons/CRYSTALLOGRAPHIC-RESTRICTION-BRIEF.md`.
  *pointer-only.*
- **`memos/COUNTING-APPARATUS.md`** adjacent anchors — add pointer
  to `rotations/CONTINUED-FRACTIONS-CROSSWALK.md`. *pointer-only.*
- **`memos/STRIP-TISSUE-FOURIER.md`** Hurwitz cross-check — flag
  that BIND-THE-CIRCLE supplies modular-surface context.
  *one-line.*
- **`memos/ARCHIMEDEAN-SIGNATURE.md`** §"Fourier Taxonomy" — note
  that the arc-length-vs-strip lattice split is also visible in
  `rotations/3DT-BRIEF.md`. *one-line.*
- **`memos/LOWER-BOUND-COUNTRY.md`** §(E) Kolmogorov-complexity
  thread — add `rotations/CONTINUED-FRACTIONS-CROSSWALK.md` pointer
  for CF-as-description-length sit. *pointer-only.*
- **`memos/LANDFALL-EXPORT.md`** §2 Affine Recurrence — circle-
  side-closure dual could pointer-link
  `BNHA/triad/Creati/CREATI-THE-CIRCLE.md` C9 or CF-CROSSWALK.
  *pointer-only.*
- **`corners/HURWITZ-GAP.md`** ~line 24 — add `rotations/3DT-
  BRIEF.md` pointer for lattice-spectral reading. *pointer-only.*
- **`corners/TAU-PORTRAIT.md`** ~line 15 — add
  `rotations/CONTINUED-FRACTIONS-CROSSWALK.md` pointer.
  *pointer-only.*
- **`n-gons/ARCHIMEDEAN-STRIP-FLIP.md`** ~line 113 — add
  `iso/BECK-1994-BRIEF.md` and `iso/DIDOS-PREROGATIVE.md` pointers
  for grid-incidence-as-discrepancy reading. *pointer-only.*
- **`n-gons/CRYSTALLOGRAPHIC-RESTRICTION-BRIEF.md`** §3 close —
  explicit cross-reference to SUBPOLYGON.md prime-valuation form.
  *one-line.*
- **`iso/DIDOS-PREROGATIVE.md`** lines 64–66 — sharpen "Beck
  enters DIDOS via K-H-L-A discrepancy proxy" language.
  *one-line.*
- **`AGENTS.md`** root "Old-time religion" — add Roth-1954-vs-
  1955 note and Beck 1994 sit (transcendence-free vs transcendence-
  theorem distinction). *one-line.*

#### Category 4 — Endgame consolidation candidates

- **`README.md`** root — does not currently mention `rotations/`
  folder. Once integrations land, the §State or §Shape paragraph
  should acknowledge rotations/ as substrate (substrate-vs-peer-
  register reading from the deferred synthesis memo). *paragraph;
  flag for after integrations land.*
- **`memos/COUNTING-APPARATUS.md`** ~line 152 — possible outdated
  parenthetical "an earlier revision … said φ(2n)/2"; verify
  against current repo state, then strike if confirmed stale.
  *one-line delete pending verification.*

#### Category 5 — Paper-scaffolding gaps

- **`BNHA/triad/Creati/INSCRIPTION-PAPER-PLAN.md`** — paper plan
  references closure arguments at §1/§4 needing redoing against
  algebraic-of-unbounded-degree targets. With integrations landed,
  the paper plan should record: (i) NATIVE-F's closure-mismatch
  theorem as the §2 closure source; (ii) B1's "absence-of-X
  implies impossible regularity" template as the proof-shape
  lineage for §1/§4; (iii) C1's BWT/Lyndon candidate machinery as
  the §5 Kraft-domain-independence candidate. *paragraph each;
  three small fill-in adds.*
- **Synthesis memo (deferred per §2.4).** Once written, this is
  the paper's "integration narrative across three named registers"
  source. Currently a gap. Recommended turn after Turn 14.
  *needs-design-pass.*
- **VILLAINS-ANSWERED §#6 Daedalus answer sharpening.**
  Integrations supply candidate staircase pieces; same edit listed
  in Category 3 above. *paragraph; cross-listed.*
- **Top-level statement of the main theorem.** Root README's §State
  paragraph names three struts (closure-depth / compute-cost /
  Kraft–Parseval discrepancy) with closure status. The paper plan
  articulates parallelism (three walls port, three soften, six
  villains answered). What's missing is a single doc — call it
  `MAIN-THEOREM-STATEMENT.md` or fold into the synthesis memo —
  that says: "Given hypotheses H₁, H₂, H₃, the program asserts T.
  Proof outline: …" with explicit reference to where each strut
  closes. *needs-design-pass; largest paper-scaffolding gap.*

#### Paper-readiness verdict

**Not yet ready to start drafting.** Two structural gaps stand
between the post-plan state and a paper draft.

The first is the synthesis memo (§2.4, deferred). It is the
natural "integration narrative across three named registers" the
paper would draw on for its substrate framing.

The second is the absence of a top-level propositional statement
of the main theorem. The root README articulates the *shape*
(truss-bridge: three independent struts) and the *state* (closure-
depth proven; compute-cost open; Kraft–Parseval open). The paper
plan articulates *parallelism*. What's missing is a single doc
stating "given hypotheses H₁, H₂, H₃, the program asserts T;
proof outline: …" with explicit reference to where each strut
closes.

**Natural first chapter to draft (when ready).** §2 closure of
INSCRIPTION-PAPER-PLAN — the one wall that ports directly, has
NATIVE-F as its proof, and only needs B1's methodological lineage
cite to be paper-grade. Drafting it would also surface what's
still missing for §1/§4 (the unbounded-algebraic-degree argument),
where the real original work sits.

**Recommended sequencing after Turn 14.** Synthesis memo →
`MAIN-THEOREM-STATEMENT.md` → start the paper at §2. The 14th
turn the user described is genuinely two sub-turns: small
Category 1–3 edits (lands as Turn 14a) and Category 4–5 paper-
prep flagging (Turn 14b). The synthesis memo and theorem-
statement work surfaced by Category 5 are post-plan in scope and
do not belong inside this plan file.

**Status.** complete; Category 1–3 pointer/framing edits landed, the
verified stale `COUNTING-APPARATUS` parenthetical was removed, and the
Category 4–5 paper-prep items remain flagged rather than implemented.
Post-plan paper blockers remain: deferred synthesis memo and top-level
main-theorem statement.

---

*Plan populated and sequenced. Per-target audit steps run after
each landing; the full cross-folder consistency check (§2.3) runs
once after all nine targets close. When all targets close, this
file freezes as a historical record of how the rotations/ supply
was wired in, with the synthesis memo (§2.4) as the load-bearing
artifact downstream.*
