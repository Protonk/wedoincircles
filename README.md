# wedoincircles

![A hand-drawn sketch in MS Paint style: a stick figure wearing a hardhat stands beside a small industrial building with a smokestack. On the ground in front of the figure, three red triangles sit alongside one blue circle. Handwritten text floats in the sky reading "i guess we doin circles now".](figures/doincircles.png)

A research program testing whether a structural correspondence — a candidate functor `F` — exists between two arithmetic objects: on the log side, the floating-point residue `ε(m) = log₂(1+m) − m` studied in *Landfall*; on the circle side, the regular `n`-gon wholeness construction and the arithmetic objects it generates. Most of the repository develops that circle side, then asks whether its structure can be matched, translated, or obstructed against the log side.

The working hypothesis is that no such `F` exists, and that the interesting result is the shape of the obstruction. Three independent legs probe this — Chebyshev polynomial structure (CREATI), crystallographic ↔ p-adic matching (PERMEATE), and `τ_c / ε` spectral rhyme (BIND) — each conducted under its own productive constraint (form / preparation / vocabulary). The expected outcome is not just a no-go verdict but an explicit closure mismatch with computable witnesses: the circle side carries `ℤ[x]` as its operational closure via Chebyshev, the log side appears capped at `Aff⁺(ℝ)` via the machine's native operations, and arithmetic witnesses such as the break at `n = 7` localize the mismatch. Where any leg succeeds locally, that success is informative too. The deliverable shape is a closure-mismatch theorem articulated cooperatively across the three disciplines.

## Project Layout

This section records only the top-level roles, so it stays useful even as the deeper file tree shifts.

- `corners/`, `n-gons/`: the circle-side constructions, variants, and bridge notes.
- `BNHA/`: the program architecture — the three working disciplines (BIND / CREATI / PERMEATE) under `BNHA/triad/`, plus satellite characters as peers (e.g. `BNHA/sir_nighteye/`).
- `memos/`: promoted internal references, crosswalks, and speculative future-facing notes.
- `sources/`: source-facing reads, PDFs, and extraction material.
- `figures/`, `sage/`: generated figures and the scripts that produce or support them.
- `README.md`, `AGENTS.md`: top-level orientation and repo-local working rules.
