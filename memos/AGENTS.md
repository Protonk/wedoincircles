# AGENTS

## Source extraction memos

Source-facing extraction memos live in this directory (`memos/`) with the `-BRIEF` suffix, e.g. `memos/10-MARTINIS-BRIEF.md`, `memos/3DT-BRIEF.md`. The parent `sources/` directory holds the raw PDFs and is gitignored.

Writing standard for a brief:

- Lead with the paper identity, what was read, and the confidence level of the read.
- State the main theorem or main payload early.
- Distinguish clearly between:
  - what the paper proves,
  - what the paper states but this repo has not independently checked,
  - and what this repo is inferring from the paper.
- Prefer theorem-first summaries over reading-diary narration.
- Keep scope notes and trust boundaries explicit.
- Use section-by-section or theorem-by-theorem structure when that helps re-entry.
- Avoid burying repo-wide doctrine or triad-law inside a brief. If a note outgrows its source-facing role and becomes reusable internal reference, drop the `-BRIEF` suffix or promote it out of `memos/` into the discipline home that actually owns it (e.g. `BNHA/triad/...`).

## Search memos

Open-ended search memos live in this directory without a suffix convention, as scaffolding for uncertain program ambitions that are not yet theorem-shaped. Examples in use: `memos/COUNTING-APPARATUS.md`, `memos/RAMANUJANS-COMPLIMENT.md`.

Anatomy of a search memo:

- **Target.** A single-sentence statement of the ambition. Honest about whether achievability is uncertain.
- **Prerequisites or items under search.** Labeled (A / B / C / D, or whatever the search decomposition suggests). Each item has its own section with what's known, what's unknown, and what would close it.
- **Adjacent anchors.** Existing material the search draws on — leg docs, briefs, prior memos. Kept current.
- **What this is not.** Explicit scope note: not a proof, not a paper plan, not a commitment to achievability. The absence of these disclaimers is how search memos silently drift into commitments they did not earn.
- **Exit criteria.** Specific conditions under which the memo freezes and its content promotes into a committed location — paper plan, discipline home, or source brief. Writing these in advance disciplines the search.

A search memo is append-only during its active life. When exit triggers, the memo either freezes (becomes a historical record) or its content migrates out. Do not edit a search memo as though it were a committed statement; its register is provisional.

If a search memo is growing faster than it is converging, that is a finding. Note it explicitly in the memo rather than letting the memo drift into a sprawl.

## Recurring gotchas

- If you need a monic integer Chebyshev polynomial, use the scaled form
  $$
  P_n(x)=2T_n(x/2),
  $$
  not raw `T_n`.
- For the Ten Martini memo, the arithmetic parameter is
  $$
  \beta(\alpha)=\limsup \frac{\ln q_{n+1}}{q_n},
  $$
  not $\limsup \ln q_{n+1}/\ln q_n$.
- The crystallographic function `\psi` is additive on prime-power parts. It is not `\varphi/2`.
- In the lattice 3DT formulation, `r_2`, `s_2`, and `r_2+s_2` are unscaled lattice-function values. The actual circle-gap lengths are those quantities divided by `N`.
