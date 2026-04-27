# fft

FFT-complexity literature import for the program's compute-cost branch.
Sibling to `corners/` and `n-gons/` (program-internal constructs); this
directory holds imported reads and the program's syntheses on top of them.

Contents:

- `FFT-CYCLOTOMIC-COMPLEXITY.md` — directed-read coordinator.
- Source-extraction briefs on four FFT-complexity papers:
  - `AUSLANDER-FEIG-WINOGRAD-1984-BRIEF.md`
  - `MORGENSTERN-1973-BRIEF.md`
  - `WINOGRAD-1978-BRIEF.md`
  - `SCHOENHAGE-STRASSEN-1971-BRIEF.md`
- `HEIDEMAN-JOHNSON-BURRUS-1985-BRIEF.md` — historiographical audit (Gauss → Cooley–Tukey chain).
- `GOLDSTINE-1977-INTERPOLATION-BRIEF.md` — technical companion to HJB85: Goldstine's exposition of Gauss 1805 (Theoria interpolationis) and Gauss 1809 (Theoria Motus rounding errors), with two reading lenses (FFT-branch, KHLA-branch).
- `AILON-2013-UNITARY-FFT-LOWER-BOUND-BRIEF.md` — adjacent restricted-model lower-bound brief: matrix entropy gives `Ω(n log n)` for normalized Fourier transform in a layered unitary `2 x 2` gate model.
- `FOUR-FRAMEWORK-SYNTHESIS.md` — cross-source synthesis on the four briefs.
- `PROVENANCE-AND-TRANSFERABILITY.md` — INHERIT-discipline synthesis (provenance backward + transferability forward).
- Program-side FFT syntheses feeding the paper proof plan:
  - `FFT-COMPLEXITY-ARTICULATION.md` — proof-template and trust-boundary articulation for the four FFT frameworks.
  - `FFT-SEARCH-PLAN.md` — adaptive-strategy-family framing for FFT-style methods.
  - `PHASE-DEFECT.md` — candidate cocycle / character-reflection mechanism for realizing the transaction-cost object `δ`.

The four framework briefs feed FOUR-FRAMEWORK-SYNTHESIS; that plus the
historiographical audit feed PROVENANCE-AND-TRANSFERABILITY.

New briefs follow `CONTRIBUTING.md` source-extraction register; L-W-safety
audit per `memos/OLD-TIME-RELIGION.md`; trust boundary explicit per brief.
