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
