# Cost-model methodology, reread on the circle: the §7 table

Source-of-truth markdown table for the cost-model methodology pair (Schönhage–Strassen 1971, Ailon 2013) read through §7's frame. Designed for two audiences: a slide-deck reader (e.g., an FFT-history seminar that wants the structural-significance reading rather than the canonical-result reading), and a `paper/PAPER.md` §7 prose reader who has already seen §3.2's standard presentation and is now reading the impossibility-relocates-what-the-canon-was-seeing reframing.

The table is dense — paragraph-sized cells — by design. The first three columns of `paper/tables/FFT-CANON-TABLE.md` (Setting / Result + mechanism / Where the mechanism unbinds) carry survey-style content; this table carries exegesis-style content. Both forms are tables in the sense of presenting parallel rows; only the first is a table in the sense of inviting cell-by-cell scanning. This one is "two big paragraphs in a table frame."

## Optional caption

> **Table 2: The cost-model methodology, reread on the circle.** After §6's impossibility, what looked like an upper-bound construction and a restricted-model lower bound are two sides of the same circle reading — the canon's own apparatus for measuring what the circle was doing.

Lift the caption with the table for slide-deck use. The §6 reference and the "circle reading" framing are §7-specific; can be edited for non-paper contexts.

## Table

| Source | Reread on the circle |
|---|---|
| **Schönhage–Strassen 1971** | Schönhage–Strassen 1971 measures integer multiplication through the cyclotomic substrate. The construction works in `Z/F_n Z` for Fermat number `F_n = 2^{2^n} + 1`, where `2` is a primitive `2^{n+1}`-th root of unity — the circle's roots of unity made arithmetically cheap. Root multiplication reduces to cyclic shift; the recursive composability of the FFT decomposition is the cyclic group's structure showing up in the operational cost ledger. The `O(N log N log log N)` upper bound is what integer multiplication costs when counted through this cyclotomic lens — the circle's recursive symmetry together with the bit-counting overhead of finite-precision arithmetic. Integer multiplication, counted operationally on this substrate, takes the shape the substrate gives it; the cost-model makes the cheap shifts visible because the substrate makes them cheap. |
| **Ailon 2013** | Ailon 2013 measures the normalized Fourier transform through unitary entropy. The model is layered `2 × 2` unitary gates, each mixing two of `n` live coordinates — the circle's symmetry group acting infinitesimally on the data vector. The matrix-entropy potential `Φ(M) = −∑ \|M(p,q)\|² log_2 \|M(p,q)\|²` measures the information-theoretic spread of `M`'s amplitudes; `Φ(Id) = 0`, `Φ(F) = n log_2 n` for the normalized Fourier matrix, and one native gate raises `Φ` by at most `2`. The `(1/2) n log_2 n` lower bound is what the circle costs when the cost-model is unitary entropy. The normalized FFT is unitary by construction (`\|det\| = 1`); information spread is what unitary structure has to give, and the entropy potential registers it. Ailon witnesses, on the canon's own ground, that each cost-model picks up a different aspect of the circle's geometry — the cost-model and the potential are entangled with what the circle has to show. |

## Design rationale

**Two papers, paragraph-sized cells.** The two cost-model methodology papers (per §3's 3+2 typing) read through §7's frame. The cells are paragraph-sized because the §7 reading is interpretive — re-presenting each paper's content under the impossibility-relocates-what-the-canon-was-seeing frame. Survey-style cells would defeat the purpose: §3.2 already gives the standard presentation, and the §7 table's job is the bold reframing the standard presentation does not give.

**Two columns, no recap.** *Source* identifies the paper. *Reread on the circle* carries the §7 reading. No "what it appears to do" recap column — the reader has absorbed §3.2 by the time they reach §7, and a recap column would be redundant.

**Honest plus bold.** Each cell preserves the actual technical content of the paper (Fermat-ring construction, root-of-unity cyclic shifts; matrix-entropy potential, unitarity giving `|det| = 1`) and adds the §7 reading explicitly. Cells state the §7 reading positively rather than via contrast with the canonical reading — students read each cell and learn what the paper does on the circle without being asked to entertain what the paper isn't. Both cells preserve the canon's standalone integrity by elevating the papers' structural significance, not by reducing them to instruments of the program's argument.

**Structural arc per cell.** Both cells follow the same arc: *what the paper measures* → *the technical apparatus* → *what the bound is in the §7 reading* → *the §7-licensed structural significance*. The parallel structure across the two cells lets the reader see the §7 reading as a consistent move, not a one-off rhetorical maneuver.

**Why §7, not §3.2.** §3.2 presents Schönhage–Strassen and Ailon as cost-model methodology in canon-survey voice. §7's "the canon's heterogeneity is the circle showing through" frame earns a richer reading that §3.2's voice does not permit. Putting the bold reading at §3.2 would be premature — the reader has not yet seen §6's impossibility theorem. At §7, the reading is licensed by what the impossibility theorem has earned.

## Out of scope

- Not a re-presentation of the three lower bounds. Morgenstern, Winograd, Auslander–Feig–Winograd are presented at §3.3–§3.5 in §3 voice; §7's multi-measure framing reads them as heterogeneous measures of `T(P)`. They are not in this table because their §7 reading lives in the multi-measure block, not in the cost-model-methodology block.
- Not a replacement for §3.2. §3.2 stands as the standard presentation; §7's table is the bold rereading. Both are needed; the bold reading depends on the standard reading having been seen first.
- Not a literature-survey of FFT cost-model papers. Just the two the program engages.

## To update

When cell content changes, propagate to:

- `paper/PAPER.md` §7 (the new "**The cost-model methodology, reread on the circle.**" block) — the table is inline-copied from this file; updates here should sync there.
- `paper/PAPER.md` §7 multi-measure block — the cross-reference "(per Table 2 above)" should stay accurate; if Table 2 moves or restructures, the reference may need updating.
