# PAPER-REFACTOR-PLAN

Frontier-first reorganization of `paper/FFT-CLASS-IMPOSSIBILITY-PAPER.md` around care / interest / use, with the **geometric bet committed**: the paper's public face is the identification `δ_min(P) = (5π − 1) · Δ_{n_P}` — the cost of trading the circle's algebra against the polygon's geometry is the isoperimetric deficit of the discretization. Epistemic order and rhetorical order coincide (earned material is also the striking material); the structure is built on that alignment.

Three stages: **recon** (build the maps, move nothing), **staging** (new prose, then carpentry), **cleanup** (verification, concordance v2, memory, commits). Each stage has acceptance criteria. Items marked **DECISION** are yours; strike or annotate in place and reply.

Ground rules carried over from the founding:

- The new paper's section numbers are free — nothing in the repo points at them. SCAFFOLD keeps the old map; working docs aim at SCAFFOLD. Renumbering costs nothing externally.
- Gestation names must not re-enter (zero-grep enforced at cleanup).
- Tag set unchanged. Door/room conceit budget: exactly two sites (chase setup; proof payoff), both `[RHETOR]`.
- Semantic theorem names now; mechanical numbering at prose freeze.

## Target architecture

| New § | Title (working) | Content | Source | Trio |
|---|---|---|---|---|
| Front | Abstract | rebuilt on the trio; floor formula stated; conditionality sentence retained | rewrite | all |
| §1 | The seam question | four tight cells, silent off-cell; seams as algorithmic resources; **Frontier Theorem, informal, with the floor formula, by page 2**; earned/committed/owed; working vocabulary (half page, informal: currency, regime, conversion, `δ`, `T(P)`) | new prose + harvest of current §Intro + best of current §2 | care |
| §2 | The circle against the polygon | substrate led by the Coarsening Theorem; registers; polygon arithmetic; ladder; envelope; compress-vs-steer reading stated here | current §5 wholesale; current §2's circle imagery as opening tissue | interest (earned half) |
| §3 | The canon and its seams | four sources + stratification + Ailon; each cell subsection now ends at its seam ("the boundary this bound does not cross") | current §3, reframed closings only | care, sustained |
| §4 | The class and the theorem | class, adjacency criterion, thresholds, formal Frontier Theorem, the chase | current §4 intact | — |
| §5 | The cost of conversion | full cost apparatus; (H1)/(H2) declarations; Proposition F; the boundary object | current §1 + current §6.1–§6.3, just-in-time | interest (mechanism half) |
| §6 | The four channels and the proof | Propositions A–D, E, ten-block proof, smarter-FFT rebuttal | current §6.4 + §6.6, moved as a sealed unit | — |
| §7 | What this buys | channels as audit instrument; measurement non-transport (where new bounds must look); boundary-object template as reusable machinery; Rice horizon | current §6.7 + §Conclusion outflow + new framing prose | use |
| §8 | The circle | canon reread; multi-measure; closure-mismatch companion; ring closes on the geometric identification | current §7, slimmed | echo |

Lucky breaks: current §3 and §4 keep their numbers (large reduction in internal-reference churn). The proposition architecture moves as one sealed unit.

**DECISION D1 — current §2 dissolves.** Its overture material splits: circle imagery → new §2 opening tissue; conversion framing → new §1. This resolves the parked §2/§7 genre question in favor of the ring (new §1 plants the circle; new §8 returns to it). Strike if you want §2 preserved as a standalone overture instead.

**DECISION D2 — §Conclusion dissolves.** Outflow (intensional/extensional, Rice) → new §7; coda fragments and the non-FFT question → new §8. Strike if you want a separate Conclusion section retained.

**DECISION D3 — staging gate.** Stage 2a writes the only genuinely new prose (new §1, new §7 framing, transitions) to `paper/REFACTOR-STAGING.md` for your sign-off before any block moves. Strike this line to skip the gate and let staging run end-to-end.

**DECISION D4 — abstract carries the formula.** The rebuilt abstract states `δ_min(P) = (5π − 1) · Δ_{n_P}` explicitly (with its conditionality). This is the geometric bet made visible at the first opportunity. Strike to keep the formula at §1 only.

## Stage 1 — Recon (build maps; move nothing)

- [ ] **R1. Renumber map.** Full old→new subsection map (e.g., old §1.2 → new §5.x; old §6.2 → new §5.y; old §5.x → new §2.x). Output: table appended to this file under *Recon results*.
- [ ] **R2. Internal-reference inventory.** Every `§x.y` occurrence in the paper, bucketed by target; confirm §3/§4 self-references survive unchanged; list every reference that crosses the move boundaries (notably the heavy `§1.2 uniform-charge` and `§6.3 boundary object` families, and `(H1)/(H2) declared at §6.1` → new §5 home with §1 forward pointer).
- [ ] **R3. Dependency audit for the working vocabulary.** Enumerate exactly which terms current §3/§4 blocks consume from current §1 (candidate list: currency `μ`/`α`, coefficient regime, conversion, `δ` informal, `T(P)`, uniform-charge guard, regularity guard). The new-§1 vocabulary block must cover precisely this list — no more.
- [ ] **R4. Figure re-homing map.** cost_conversion_schematic (old §1.8 → new §5); native_f_closure_mismatch (Intro + old §7 → new §1 + new §8); §5.3 trio → new §2; delta_phase_plot (old §6.5 → new §5); counting_psi (Conclusion → new §7 or §8). Update the Figures table's section column accordingly.
- [ ] **R5. Harvest list.** Blocks of current §Intro/§2/§Conclusion worth carrying into new §1/§7/§8 verbatim vs paraphrase vs drop, with reason classes (same discipline as the founding).
- [ ] **R6. Door-budget check under the new order.** Chase door-line lands in §4; room-line lands in §6; current §2's "slams into a substrate-side door" line dies with D1. Confirm budget = 2 post-move.

*Acceptance: all six outputs appended to this file; zero edits to the paper.*

## Stage 2 — Staging (write, then move)

- [ ] **S1. New prose** (the authorship; everything else is carpentry):
  - New §1: the seam question — four tight cells / uncharged seams / informal Frontier Theorem with floor formula / earned-committed-owed (compressed, not diluted) / working vocabulary. Target ≤ 35 blocks. Harvests the care argument already drafted in session notes.
  - New §7: use framing — audit-instrument reading of the channels; non-transport corollary as "where to look"; template claim (inverse-limit construction as reusable machinery, stated once, modestly); Rice horizon absorbed from Conclusion.
  - Transition tissue: §1→§2 (from the question to the substrate), §4→§5 (from the theorem to the machinery that prices it), §6→§7 (from proof to instrument).
  - Rebuilt abstract per D4.
  - Per D3: all of the above lands in `paper/REFACTOR-STAGING.md` for sign-off first.
- [ ] **S2. Carpentry.** Execute the architecture table: move blocks per R5, retitle sections, apply R1 renumber map to every internal reference, re-home figures per R4, dissolve current §2 and §Conclusion per D1/D2. Propositions and proof move untouched.
- [ ] **S3. Seam-closings for §3.** Add the one-block "the boundary this bound does not cross" closer to §3.2–§3.5 (four blocks, new).

*Acceptance: paper assembled in the new order; staging file (if D3 stands) consumed; no content lost except R5's reasoned drops.*

## Stage 3 — Cleanup (verify, record, commit)

- [ ] **C1. Mechanical verification.** Integrity detector (parens/bold per block); `check_input` accepts; block reconciliation old→new with every delta assigned a reason class; internal `§x.y` audit — every reference resolves under the new map; zero-grep for gestation names (`T4b`, `Theorem K`, `debt #`, `route-3`, `NATIVE-F` outside file paths, …).
- [ ] **C2. Budget checks.** Door/room conceit at exactly two sites, `[RHETOR]`-tagged; "Lower bounds are not numbers" appears once verbatim plus explicit callbacks only; floor formula appears in abstract (per D4), §1, §5, §8 — and nowhere else.
- [ ] **C3. Concordance v2.** SCAFFOLD's concordance gains the section map (old paper § → frontier-first §) so the bridge stays bilingual through the renumbering.
- [ ] **C4. Memory + commits.** Update session memory (architecture note → frontier-first map). Commits: one for recon results (this file), one for staging, one for cleanup — or collapse staging+cleanup if D3 is struck.

*Acceptance: all checks green; SCAFFOLD bilingual against the new map; three (or two) reviewable commits.*

## Risks (acknowledged, accepted, or mitigated)

1. **The bet itself.** Frontier-first makes the geometric identification the paper's face; if (H1)/(H2) force retreat on the floor's value, the headline takes the hit. *Accepted by decision (this plan).*
2. **Informal-first discipline.** §1's informal Frontier statement must not overclaim: it carries the conditionality sentence adjacent, and the formal statement remains the only citable one (§4). Mitigation: tag the informal statement's blocks and check at C2.
3. **Vocabulary sufficiency.** If R3 finds §3/§4 consuming more of the cost apparatus than a half page can carry, fallback: promote current §1.1–§1.4 (stack, model, currencies, regimes) into new §1 as a compact formal subsection and defer only §1.5–§1.8 + boundary object to new §5. Decide at end of recon, not before.
4. **Transcription drift.** Same mitigation as the founding: block-by-block movement with reconciliation, no silent rewrites during carpentry — rewriting is S1's job only.

## Out of scope

Prose pass (sentence-level rewriting beyond S1's new sections); terminology already settled at the founding; SCAFFOLD/working-doc edits beyond C3; the title (provisional title stands until prose freeze); ledger vocabulary; figure regeneration (build-script text only if captions change).

---

## Resolutions (pre-recon)

**Primary promise of new §1 (Q3, resolved): the method, instantiated by the frontier, with the geometry as fenced emblem.** By the end of §1 the non-specialist mathematically-serious reader should care that *algorithmic limits can be located by pricing conversions between incommensurable cost measures* — and should believe it because the FFT frontier is the worked arena and the polygon–circle deficit is what the method finds there. Order of emphasis in §1: seams → method → instance → emblem. Rationale: the method is the one promise the paper keeps unconditionally (construction + composition + audit instrument survive even if (H1)/(H2) stall); the frontier alone is the most specialist framing and triggers the vacuity reflex at first contact; the geometry alone would make §1 promise what the paper only conditionally delivers (see FLOOR-FORMULA-CONTRACT.md links 3–4). The geometric bet stays committed as the paper's *face* — abstract formula (D4), §8 ring, the memorable sentence — but face and §1-promise are different obligations: the face is what a reader remembers; the promise is what the paper must be audited against. This resolution does not weaken the bet; it makes the bet survivable.

**Staging is governed by two contract documents:** the floor formula's phrasing at all four sites obeys [paper/FLOOR-FORMULA-CONTRACT.md](FLOOR-FORMULA-CONTRACT.md) (conditional theorem in a committed coordinate; the Deficit Identification named with status clause; value vs positivity discipline). The boundary object's presentation absorbs the four changes mandated by [paper/REFEREE-BOUNDARY-OBJECT-AUDIT.md](REFEREE-BOUNDARY-OBJECT-AUDIT.md) (composition-device reading in the paper's own voice; the two-fact division of non-vacuous measure theory; value/positivity block near Proposition F; falsifiability point in §7). Both are S1/S2 inputs; C2 verifies compliance.

*Recon results appended below when Stage 1 runs.*
