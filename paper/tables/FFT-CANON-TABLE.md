# FFT canon table: the three lower bounds

Source-of-truth ASCII table for the FFT lower-bound canon (Morgenstern 1973, Winograd 1978, Auslander–Feig–Winograd 1984). Designed to serve two audiences: a slide-deck reader teaching FFT lower bounds, and a `paper/PAPER.md` §3 prose reader who has just read §3.3–§3.5 in detail. The first wants self-contained cells; the second wants pattern visible at a glance. Column 4 is what serves the second audience; the first three columns serve both.

## Optional caption

> **Table 1: The three FFT lower bounds.** Each row presents one bound's setting, result and mechanism, and the regions where the mechanism unbinds. Reading down column 4 makes the cross-row pattern of forced silences visible — the heterogeneity §3.6.2 develops as content.

Lift the caption with the table for slide-deck use; drop it if the surrounding prose carries the framing.

## Table

```
+------------------------------+----------------------------------------+------------------------------------------------------------+---------------------------------------------+
| Source                       | Setting                                | Result + mechanism                                         | Where the mechanism unbinds                 |
+------------------------------+----------------------------------------+------------------------------------------------------------+---------------------------------------------+
| Morgenstern 1973             | bounded coefficients (|c_i| ≤ c for    | Ω(n log n) additive cost via determinant potential: the    | unbounded coefficients (potential unbinds   |
|                              | some constant c); linear-circuit /     | DFT matrix has determinant |det| = n^(n/2), and a bounded  | when gate growth is no longer constant);    |
|                              | additive accounting                    | gate grows the running determinant by at most a constant   | multiplicative cost (potential measures     |
|                              |                                        | factor                                                     | volume, not bilinear multiplications); the  |
|                              |                                        |                                                            | normalized FFT (determinant has modulus 1)  |
+------------------------------+----------------------------------------+------------------------------------------------------------+---------------------------------------------+
| Winograd 1978                | unbounded rational-equivalence;        | exact bilinear multiplicative complexity μ(T_P) = 2n − k   | additive cost (bilinear ledger blind to     |
|                              | bilinear multiplicative accounting on  | for degree-n polynomial with k irreducible factors over    | additions); bounded coefficients (rational  |
|                              | polynomial-quotient rings              | the base field, via CRT decomposition: polynomial          | equivalence permits unbounded scalar        |
|                              |                                        | multiplication mod T_P reduces factor-by-factor over       | substitutions); content outside             |
|                              |                                        | residue rings, with the bound from counting essential      | polynomial-quotient ring structure          |
|                              |                                        | bilinear multiplications per factor                        |                                             |
+------------------------------+----------------------------------------+------------------------------------------------------------+---------------------------------------------+
| Auslander–Feig–Winograd 1984 | unbounded rational-equivalence;        | factor-by-factor multiplicative complexity via cyclotomic  | additive cost; bounded coefficients;        |
|                              | bilinear multiplicative accounting on  | decomposition ℚ[G] = ∏_(d | |G|) ℚ(ζ_d) (one cyclotomic    | content outside the rational-equivalence    |
|                              | finite-abelian-group DFTs              | factor per divisor d of |G|), with μ computed per factor   | equivalence relation (linear-rational       |
|                              |                                        | under rational equivalence                                 | substitutions are free)                     |
+------------------------------+----------------------------------------+------------------------------------------------------------+---------------------------------------------+
```

## Design rationale

**Three rows, not five.** Schönhage–Strassen 1971 and Ailon 2013 are excluded — they are cost-model methodology, not lower-bound theorems the program reads as `T(P)` (per §4.4). Schönhage–Strassen is upper-bound only; Ailon's `(1/2) n log_2 n` lives in a restricted unitary-gate model the program does not assert impossibility against. Both are presented at §3.2 as the cost-model methodology pair. The three rows here are the bounds the impossibility theorem is stated against: Morgenstern (additive, bounded coefficients), Winograd (multiplicative on polynomial-quotient rings), Auslander–Feig–Winograd (multiplicative on cyclotomic-decomposed group DFTs).

**Four columns.** *Source* identifies the paper. *Setting* names the model the result lives in (regime plus accounting). *Result + mechanism* carries the bound and a one-clause mechanism gloss in one cell — merged so the mechanism gloss stays on the page without widening the table. *Where the mechanism unbinds* is the structural-pattern column: each cell lists the regions where the mechanism's reach ends, and the silences are forced by what each potential or accounting can see.

**Why column 4 is load-bearing.** Without it, the table is a survey of three results side by side. With it, the cross-row pattern is visible: every mechanism unbinds in three of four (regime × currency × structural-limit) cells; two rows (Winograd, Auslander–Feig–Winograd) share shape — additive cost / bounded coefficients / outside their structural assumption — and Morgenstern is the inverse. That repetition is the §3.6.2 content claim about forced heterogeneity made data. Slide-deck use: column 4 is a "what to not over-claim" panel for each row. Prose-reader use: it gives structural visibility prose-in-sequence cannot deliver.

**Cell density.** Result + mechanism cells run two clauses each (result, then mechanism after a colon or "via"). For slide projection this is on the heavy side, but tighter cells lose the mechanism gloss, and the gloss is what makes the table teaching-load-bearing rather than just a result list. A teacher can either let students read each cell slowly or paraphrase aloud while pointing.

**Full author names, no subsection links.** Auslander–Feig–Winograd 1984 spelled out — first-encounter slide-deck readers need the attribution; abbreviation "AFW" loses it. No `(§3.X)` subsection references in the source column — they are noise on slides and the surrounding §3 prose handles in-paper navigation.

**Slide-deck independence.** The table travels: caption + table + nothing else needed. Cell content is self-contained; mechanism glosses stand on their own. A teacher leaving the table up for two minutes can let students read each row without footnote-chasing.

**Prose collaboration.** §3.1 hooks the table with a parenthetical reference; §3.3–§3.5 develop each row in prose at length; §3.6.2 reads the column-4 pattern as the content claim about forcing. The prose adds mechanism explanation and structural commentary at depth; the table adds cross-row pattern at a glance. Reading both gives more than reading either alone.

## Out of scope

- Not a literature survey of FFT lower bounds. Cooley–Tukey 1965, Pan 1986, Heun 2003, post-2013 successors — out of scope. This is the program's engaged canon, not a literature review.
- Not an upper-bound / lower-bound comparison. Schönhage–Strassen's `O(N log N log log N)` upper bound is at §3.2 with the cost-model methodology, not in this table.
- Not a `T(P)` reconciliation. Cross-currency reconciliation across the three rows is the substantive open work at §6.5 (the route-3 currency-universal limit `Z`); the table presents the three currencies separately, not their integration.

## To update

When cell content changes, propagate to:

- `paper/PAPER.md` §3.1 (parenthetical hook in the closing paragraph + table block before §3.2) — *landed 2026-05-02*.
- `paper/PAPER.md` §3.6.2 (column-4-pattern reading is the content claim — keep the reference accurate).
- `paper/code/` if a typeset / figure-rendered version is built later (none currently).
