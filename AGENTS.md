# AGENTS

## Sage has tools

Use sage for `numpy`, `scipy`, and `matplotlib`. Do not attempt to install these or use the system version.

As an example, run a script from the repo root:

```
sage corners/pseudo_chebyshev_continuity.sage
```

Scripts resolve their output path relative to their own location and write PNGs to `figures/` at the repo root; each prints the path it wrote. No cwd matters. Other entry points follow the same pattern — e.g. `sage n-gons/subpolygon_gallery.sage`, `sage n-gons/strip.py` (plain Python scripts in `n-gons/` run with `python3` or `sage` interchangeably).

The `.sage.py` file that appears next to each `.sage` after a run is the Sage preprocessor artifact; ignore it (and leave it untracked).

## Pathing

When a document links to another file in the repo, write the link target as a repo-root-relative path — not as a relative path with `..` segments and not as an absolute filesystem path. Repo-root-relative targets stay correct when the linking document moves inside the tree.

Prefer:

```
[n-gons/SUBPOLYGON.md](n-gons/SUBPOLYGON.md)
```

Avoid:

```
[n-gons/SUBPOLYGON.md](../n-gons/SUBPOLYGON.md)
[n-gons/SUBPOLYGON.md](/Users/.../wemakincircles/n-gons/SUBPOLYGON.md)
```

### Images

Image embeds stay as they are (`![…](figures/foo.png)` or the equivalent `..`-relative form when a sage script needs it) — those are loaded by viewers/renderers that resolve paths from the document's own directory, not by the repo-root convention above.

## Repo character

This is a math-research writing repo. Most work is reading papers, promoting notes into reusable internal references, tightening theorem statements, and keeping the document graph coherent.

## Transcendence-tool provenance

Drafts aimed at the program's compute-cost reformulation of transcendence prefer **pre-Lindemann–Weierstrass** tools (Liouville 1844, Gauss–Wantzel, Hurwitz Fourier-isoperimetric, Lambert/Euler irrationality, classical cyclotomic theory) over **post-L–W** machinery (Baker 1966, Gelfond–Schneider 1934, Nesterenko 1996) when the latter would be load-bearing. Drafts that only *use* transcendence as background or as a weaker lemma are free to cite post-L–W results — Landfall's §4 pointwise-transcendence-at-dyadics statement uses Gelfond–Schneider and is fine. The rule bites only when a draft is aiming at the program's own target (compute-cost reformulation of L–W or one of its pieces), where invoking post-L–W machinery risks circularity.

See `memos/LINDEMANN-BRIEF.md` for the full circularity map (safe / background / essential / circular classification).

## Shared-vocabulary hygiene

The program tests a structural distinction between the log side (`ε(m) = log₂(1+m) − m`) and the circle side (`τ(n) = 2cos(2π/n) − round(2cos(2π/n))`). Vocabulary that glosses that distinction — Minkowski's question-mark function `?(x)`, Stern–Brocot tree, Farey sequence, Thomae / popcorn function, Denjoy construction, dyadic expansions reinterpreted as continued fractions — is excluded from working notes, even as shorthand. Continued-fraction convergents as computational outputs are admitted (PERMEATE needs them; CREATI admits them as explicit arithmetic data); the tree as organizing frame is not.

See `BNHA/PLUS_ULTRA.md §Aizawa (BIND)` for the list and the triad-level articulation, and `BNHA/PLUS_ULTRA.md §"Continued-fraction rule"` for the CF boundary.

## Lower-bound target, upper-bound companions

The program's target is a compute-cost lower bound (or impossibility theorem) — `memos/COUNTING-APPARATUS.md` is the parent search; `memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md` is one active specialization. Upper-bound results — explicit constructions (Chudnovsky, Ramanujan, Borwein), fast algorithms (Bresenham-midpoint, AGM, binary splitting), convergence rates — are admitted as allusive companions and sanity checks; they are not load-bearing. Nevertheless, time spent in upper-bound territory may teach us things about the problem, provided we don't get lost in beautiful analyticity. 

See `memos/LOWER-BOUND-COUNTRY.md` (the complexity-theoretic reading queue) and `memos/RAMANUJANS-COMPLIMENT.md §"When to leave"` (the discipline against staying in upper-bound territory) for the detailed articulation.

## Working tree is dirty

Multiple agents and humans work in concert here, where concert <-> cacophany. Don't chase working tree diffs.
