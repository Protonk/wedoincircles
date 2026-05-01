# GPT Audit

Top-line: **ready with named caveats**; the proof shape is coherent enough for prose expansion, but a short cleanup pass should fix the companion coverage gap, stale cross-references, and threshold-orientation wording first.

## Severity-Ranked Findings

1. **Missing companion gloss for the phase-lift audit**  
   Where: `paper/COMPANION.md:5`, `paper/PROOF-CHAIN.md:34`, `paper/PROOF-CHAIN.md:101`, `paper/OUTLINE.md:199`, `paper/OUTLINE.md:349`.  
   Issue: `COMPANION` says a memo gets an entry iff its basename appears in `OUTLINE` or `PROOF-CHAIN`, but `fft/PHASE-LIFT-CONSERVATIVITY-AUDIT.md` is cited repeatedly and has no companion entry.  
   Why it matters: debt #4's "clean-conditional / no independent open work" status depends on that audit's refined condition: variable precision + effective H-L `n=1` in cost-norm-compatible form. Without a gloss, a cold reader sees a load-bearing cited audit omitted from the primer.  
   Severity: **shape-risk**.

2. **Theorem orientation is locally ambiguous**  
   Where: `paper/OUTLINE.md:116`, `paper/OUTLINE.md:134`, `paper/OUTLINE.md:137`, compared with `paper/PROOF-CHAIN.md:8` and `paper/OUTLINE.md:181`, `paper/OUTLINE.md:215`.  
   Issue: `OUTLINE` says "descent below existing lower-bound thresholds" and "does not prove a lower bound ... below `T(P)`", while the rest of the apparatus says "strictly improving past `T(P)`." In ordinary lower-bound language, a lower bound below the current threshold sounds weaker, not stronger.  
   Why it matters: prose expansion of §4.5 will force a choice of orientation. The apparatus itself is calibrated around "improving past / stronger than the canon threshold"; the theorem sentence should not invite the opposite reading.  
   Severity: **shape-risk**.

3. **Two stale cross-references remain**  
   Where: `paper/OUTLINE.md:173` and `paper/OUTLINE.md:342`.  
   Issue: §5.6 points to "§6.7 debts #7, #8", but no §6.7 exists; the debts are in the construction ledger. The ledger preamble says "The ten debts" although the table has 15 entries and the closing paragraph correctly says 15.  
   Why it matters: these do not affect the proof shape, but they break reader trust in the ledger map during expansion.  
   Severity: **minor**.

4. **COMPANION slightly blurs the `f2` / `f3` split**  
   Where: `paper/COMPANION.md:95`, `paper/COMPANION.md:97`, `paper/COMPANION.md:103`; compare `paper/OUTLINE.md:169`, `paper/PROOF-CHAIN.md:72`, and `measure/SUBSTRATE-OBSTRUCTIONS.md:187-190`.  
   Issue: the individual glosses correctly assign rate / gap to `f3 = Delta_n` and first Fourier / perimeter to `f2 = L_n`, but the interlocks sentence says both Hurwitz memos "ride together on `f2 = L_n`."  
   Why it matters: the main outline and proof-chain are correct, so this is not a structural break. It is a companion-level ambiguity that could cause prose to conflate two K2 observables.  
   Severity: **minor**.

## Cross-Reference Validation

All Markdown file links in the three target files resolve locally. Debt numbers #1-#15 are present in both ledgers and substantively agree across names, statuses, couplings, and anchors. The only unresolved / stale references I found are the non-existent `§6.7` pointer in `OUTLINE` and the "ten debts" ledger preamble. The `PHASE-LIFT-CONSERVATIVITY-AUDIT.md` omission is not a dangling file link; it is an inclusion-rule miss in `COMPANION`.

## Trinity Coherence

The outflow trinity holds up structurally: #11(iii) covers paths, #14 covers cost-norms / measures, and #15 covers coordinates. The adjacent questions in #12 and #13 are defensibly absorbed by analogy rather than suppressed, because both are explicitly named as coupling notes and neither is silently needed as a fourth horizon. Prose should keep those notes visible: #12 is "all reasonable morphisms in the chosen diagram," and #13 is "all reasonable iso-register readings," both meeting the same extensional-completeness horizon as #15 if lifted beyond the syntactic apparatus.

## Before Prose

Priority items before paragraph expansion:

1. Add or otherwise account for the missing `PHASE-LIFT-CONSERVATIVITY-AUDIT.md` companion gloss.
2. Normalize §4.5 theorem orientation to "improving past / stronger than `T(P)`" versus "descent below" so the formal statement cannot read as forbidding weaker lower bounds.
3. Fix the stale `§6.7` and "ten debts" references.
4. Clean the `f2` / `f3` companion interlock sentence.

No new first-class construction debt surfaced. The major hidden premises I would expect a careful reader to catch are already named: #11 channel exhaustiveness, #12 morphism construction, #13 substrate-side `delta` generalization, #14 cost-norm commitment, and #15 cross-chart invariance.
