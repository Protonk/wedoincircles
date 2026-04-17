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

## Working tree is dirty

Multiple agents and humans work in concert here, where concert <-> cacophany. Don't chase working tree diffs.
