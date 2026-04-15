"""
Translation deformation for the pseudo-Chebyshev construction.

Companion to `corners/TRANSLATION.md`. Also complements
`corners/pseudo_chebyshev_continuity.sage` (the c = 0 baseline) and
`corners/uniform_scaling.sage` (the similarity-transformation foil).

Move the circle vertically: instead of centered at the origin with
radius 1, center it at (0, c) with radius 1. Keep the chords fixed
(still from (0, 0) to (1, tan(π/n)) for n >= 3, with the limiting
vertical chord at n = 2). The chord–circle intersections change, and
the x-coordinate of the forward-direction intersection is the new
node:

    node(n, c) = cos(π/n) · (c·sin(π/n) + √(1 − c²·cos²(π/n))).

The plotted regime is |c| <= 1, where every n >= 3 chord still meets
the translated circle.

Three rows × two columns:
  rows:    c = 0.5 (raised), c = 0 (normal), c = −0.5 (lowered)
  columns: geometric construction / node-sequence space

Findings the figure makes visible:
- At c > 0, the right-pane curve is non-monotone: it overshoots
  the asymptote x = √(1 − c²) for moderate n, peaks near a specific
  integer, and then decreases back to the asymptote.
- At c < 0, the curve is monotone increasing to the same asymptote.
- The asymptote √(1 − c²) is symmetric in c, but the path to it is
  not.
"""

import os
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle as MplCircle


INTEGER_NS_LEFT = (3, 4, 5, 6, 7, 8)
INTEGER_NS_RIGHT = (2, 3, 4, 5, 6, 7, 8, 10, 12, 16, 20, 30)
C_VALUES = (0.5, 0.0, -0.5)  # top → bottom: raised, normal, lowered


def node(t, c):
    """Pseudo-Chebyshev node at real t ≥ 2 with circle centered at (0, c)."""
    u = math.pi / t
    cu = math.cos(u)
    R = 1.0 - c * c * cu * cu
    if R < -1e-12:
        return None  # chord misses the translated circle
    if R < 0.0:
        R = 0.0
    return cu * (c * math.sin(u) + math.sqrt(R))


def crossing(t, c):
    """Crossing of origin-to-corner segment with the translated circle."""
    x = node(t, c)
    if x is None:
        return None
    y = x * math.tan(math.pi / t)
    return (x, y)


def corner_y(t):
    """y-coordinate of the n-gon corner above the anchor (x = 1). Independent of c."""
    return math.tan(math.pi / t)


def _label(c):
    if c > 0:
        return "raised"
    if c < 0:
        return "lowered"
    return "normal"


def left_panel(ax, c, integer_ns=INTEGER_NS_LEFT):
    """Geometric construction pane with circle translated to (0, c)."""
    # the translated circle
    ax.add_patch(MplCircle((0, c), 1.0, fill=False, ec="black", lw=1.8, zorder=3))

    # original anchor line at x = 1 (unchanged by the deformation)
    ax.axvline(1.0, color="0.55", ls="--", lw=1.0, zorder=2)

    # continuous trajectory of forward-direction crossings as t sweeps
    ts = np.linspace(2.005, 80.0, 400)
    xys = [crossing(float(t), c) for t in ts]
    xs = [p[0] for p in xys if p is not None]
    ys = [p[1] for p in xys if p is not None]
    if xs:
        ax.plot(xs, ys, color="#2e4a7d", lw=2.6, alpha=0.35, zorder=2)

    # integer-n chords and crossings
    cmap = plt.get_cmap("viridis")
    denom = max(len(integer_ns) - 1, 1)
    for i, n in enumerate(integer_ns):
        color = cmap(i / denom)
        # chord from origin to corner (1, tan(π/n)); unchanged by c
        ax.plot([0, 1], [0, corner_y(n)], color=color, lw=1.2, zorder=4, alpha=0.9)
        # forward-direction crossing with the translated circle
        cr = crossing(n, c)
        if cr is not None:
            ax.plot([cr[0]], [cr[1]], marker="o", color=color, ms=6,
                    markeredgecolor="black", markeredgewidth=0.4, zorder=5)

    # origin marker
    ax.plot([0], [0], marker="*", color="black", ms=10, zorder=7)

    # consistent axes across rows so the circle visibly translates
    ax.set_xlim(-1.25, 1.25)
    ax.set_ylim(-1.65, 2.00)
    ax.set_aspect("equal")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True, color="0.92", lw=0.5)
    ax.set_title(f"Geometric construction    (c = {c:+.1f}, {_label(c)})",
                 fontsize=11)


def right_panel(ax, c, integer_ns=INTEGER_NS_RIGHT):
    """Node-sequence pane at translation c."""
    # smooth curve: sweep t, plot (node(t, c), t)
    ts = np.linspace(2.0, 60.0, 1200)
    pairs = [(float(t), node(float(t), c)) for t in ts]
    pairs = [(t, v) for t, v in pairs if v is not None]
    xs = [v for (_, v) in pairs]
    ys = [t for (t, _) in pairs]
    if xs:
        ax.plot(xs, ys, color="black", lw=1.8, zorder=3,
                label=f"smooth curve, c = {c:+.1f}")

    # asymptote x = √(1 − c²) (defined for |c| ≤ 1)
    if abs(c) <= 1:
        asymptote = math.sqrt(1.0 - c * c)
        ax.axvline(asymptote, color="0.55", ls="--", lw=1.0, zorder=2,
                   label=f"asymptote x = √(1−c²) ≈ {asymptote:.3f}")

    # integer-n stems
    cmap = plt.get_cmap("viridis")
    denom = max(len(integer_ns) - 1, 1)
    for i, n in enumerate(integer_ns):
        nv = node(n, c)
        if nv is None:
            continue
        color = cmap(i / denom)
        ax.vlines(nv, 0, n, color=color, lw=1.2, alpha=0.6, zorder=4)
        ax.plot([nv], [n], marker="o", color=color, ms=7,
                markeredgecolor="black", markeredgewidth=0.4, zorder=5)

    # consistent axes across rows
    ax.set_xlim(-0.05, 1.12)
    ax.set_ylim(1.3, 32)
    ax.set_xlabel("node value")
    ax.set_ylabel("n")
    ax.set_title(f"Node-sequence space    (c = {c:+.1f})", fontsize=11)
    ax.grid(True, color="0.92", lw=0.5)
    ax.legend(loc="upper left", fontsize=8, framealpha=0.95)


def plot(outpath):
    fig, axes = plt.subplots(
        3, 2, figsize=(13, 15),
        gridspec_kw={"width_ratios": [1.0, 1.1]},
    )
    for i, c in enumerate(C_VALUES):
        left_panel(axes[i, 0], float(c))
        right_panel(axes[i, 1], float(c))

    fig.suptitle(
        "Translation deformation: pseudo-Chebyshev with circle at (0, c) "
        "for c = +0.5, 0, −0.5",
        fontsize=14, y=0.997,
    )
    plt.tight_layout()
    plt.savefig(outpath, dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    figdir = os.path.normpath(os.path.join(here, "..", "figures"))
    os.makedirs(figdir, exist_ok=True)
    out = os.path.join(figdir, "pseudo_chebyshev_translation.png")
    plot(out)
    print(f"wrote {out}")
