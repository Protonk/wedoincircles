# AGENTS

This is a math-research writing repo. Most work is reading papers, promoting notes into reusable internal references, tightening theorem statements, and keeping the document graph coherent.

## Sage has tools

>use sage to invoke python

Use sage for `numpy`, `scipy`, and `matplotlib`. Do not attempt to install these or use the system version.

As an example, run a script from the repo root:

```
sage corners/pseudo_chebyshev_continuity.sage
```

Scripts resolve their output path relative to their own location and write PNGs to `figures/` at the repo root; each prints the path it wrote. No cwd matters. Other entry points follow the same pattern — e.g. `sage n-gons/anchor_345.sage`, `sage n-gons/strip.py` (plain Python scripts in `n-gons/` run with `python3` or `sage` interchangeably).

The `.sage.py` file that appears next to each `.sage` after a run is the Sage preprocessor artifact; ignore it (and leave it untracked).

## Pathing

>prefer repo-relative paths in docs

When a document links to another file in the repo, write the link target as a repo-root-relative path — not as a relative path with `..` segments and not as an absolute filesystem path.

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

## Image alt-text

>alt-text is mandatory

Use literally descriptive alt-text (`< 1000` characters) for embeds of all figures. alt-text is not captioning of figures in text, it is replacement for the visual mapping of the figure itself.

## Old-time religion

When the program leans on machinery post-Lindemann 1882 (Fortnow, Aitchison, Erdős-Turán, Baker, Gelfond-Schneider, Thue-Siegel-Roth), that machinery must either be methodologically re-certified as pre-L-W in its use or be replaced by a pre-1882 anchor. Do not smuggle in number-theoretic ease, as this carries with it pi transcendental.

Circularity enters most easily through silent upgrade — invoking a modern sharpening of a classical tool without checking whether the sharpening itself already uses what the program is trying to prove. See [memos/LINDEMANN-BRIEF.md](memos/LINDEMANN-BRIEF.md) for the circularity map and the safe/weak/circular tagging; live audits of which tools anchor where and which rebuilds are worth pursuing live in [memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md). 

## Working tree is dirty

Multiple agents and humans work in concert here, where concert <-> cacophany. Don't chase working tree diffs.
