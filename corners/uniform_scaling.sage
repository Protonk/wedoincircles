"""
Uniform-scaling deformation for the pseudo-Chebyshev construction.

Companion to `corners/DEFORMATION.md` (Deformation 2) and to the
arc-flattening script `corners/pseudo_chebyshev_continuity.sage`
(the r = 1, d = 0 baseline).

This script plots the diagnostic foil: uniform scaling of the circle
to radius r. Because this is a similarity transformation, the
right-pane curve stays the same shape and only compresses horizontally.
Contrast with the arc-flattening deformation, which changes the shape
of the construction itself.

Three rows × two columns:
  rows:    r = 1, r = 0.5, r = 0.25
  columns: geometric construction / node-sequence space

The demonstration: the shape in the right-pane is identical across
rows. Only the asymptote moves (x = r), and the integer stems
compress toward 0 linearly in r.
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
R_VALUES = (1.0, 0.5, 0.25)


def node(t, r):
    """Pseudo-Chebyshev node at real t >= 2 on a circle of radius r."""
    return r * math.cos(math.pi / t)


def crossing(t, r):
    """The crossing of the origin-to-corner segment with the circle of radius r."""
    return (r * math.cos(math.pi / t), r * math.sin(math.pi / t))


def corner_y(t, r):
    """y-coordinate of the n-gon corner directly above the anchor (at x = r)."""
    return r * math.tan(math.pi / t)


def left_panel(ax, r, integer_ns=INTEGER_NS_LEFT):
    """Geometric construction pane at radius r."""
    # circle of radius r
    ax.add_patch(MplCircle((0, 0), r, fill=False, ec="black", lw=1.8, zorder=3))

    # vertical anchor line at x = r
    ax.axvline(r, color="0.55", ls="--", lw=1.0, zorder=2)

    # continuous trajectory of the crossing point: upper-right quarter of the circle
    ts = np.linspace(2.005, 80.0, 400)
    xs = [r * math.cos(math.pi / t) for t in ts]
    ys = [r * math.sin(math.pi / t) for t in ts]
    ax.plot(xs, ys, color="#2e4a7d", lw=2.6, alpha=0.35, zorder=2)

    # integer-n segments and crossings
    cmap = plt.get_cmap("viridis")
    denom = max(len(integer_ns) - 1, 1)
    for i, n in enumerate(integer_ns):
        color = cmap(i / denom)
        cx, cy = crossing(n, r)
        yc = corner_y(n, r)
        # segment from origin to corner (clipped at frame)
        ax.plot([0, r], [0, yc], color=color, lw=1.2, zorder=4, alpha=0.9)
        # crossing point on the circle
        ax.plot([cx], [cy], marker="o", color=color, ms=6,
                markeredgecolor="black", markeredgewidth=0.4, zorder=5)

    # anchor point
    ax.plot([r], [0], marker="*", color="black", ms=10, zorder=7)

    # consistent axes across rows so the circle visibly shrinks
    ax.set_xlim(-0.08, 1.22)
    ax.set_ylim(-0.12, 1.52)
    ax.set_aspect("equal")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True, color="0.92", lw=0.5)
    ax.set_title(f"Geometric construction    (r = {float(r):.2f})", fontsize=11)


def right_panel(ax, r, integer_ns=INTEGER_NS_RIGHT):
    """Node-sequence pane at radius r."""
    # smooth curve x = r * cos(pi/t)
    ts = np.linspace(2.0, 60.0, 800)
    xs = [r * math.cos(math.pi / t) for t in ts]
    ax.plot(xs, ts, color="black", lw=1.8, zorder=3,
            label=f"x = {r:.2f}·cos(π/n)")

    # integer-n stems
    cmap = plt.get_cmap("viridis")
    denom = max(len(integer_ns) - 1, 1)
    for i, n in enumerate(integer_ns):
        nv = node(n, r)
        color = cmap(i / denom)
        ax.vlines(nv, 0, n, color=color, lw=1.2, alpha=0.6, zorder=4)
        ax.plot([nv], [n], marker="o", color=color, ms=7,
                markeredgecolor="black", markeredgewidth=0.4, zorder=5)

    # asymptote at x = r
    ax.axvline(r, color="0.55", ls="--", lw=1.0, zorder=2,
               label=f"asymptote x = {r:.2f}")

    # consistent axes across rows
    ax.set_xlim(-0.03, 1.08)
    ax.set_ylim(1.3, 32)
    ax.set_xlabel("node value = r · cos(π/n)")
    ax.set_ylabel("n")
    ax.set_title(f"Node-sequence space    (r = {float(r):.2f})", fontsize=11)
    ax.grid(True, color="0.92", lw=0.5)
    ax.legend(loc="upper left", fontsize=8, framealpha=0.95)


def plot(outpath):
    fig, axes = plt.subplots(
        3, 2, figsize=(13, 15),
        gridspec_kw={"width_ratios": [1.0, 1.1]},
    )
    for i, r in enumerate(R_VALUES):
        left_panel(axes[i, 0], r)
        right_panel(axes[i, 1], r)

    fig.suptitle(
        "Uniform-scaling deformation: pseudo-Chebyshev at r = 1, 0.5, 0.25",
        fontsize=14, y=0.997,
    )
    plt.tight_layout()
    plt.savefig(outpath, dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    figdir = os.path.normpath(os.path.join(here, "..", "figures"))
    os.makedirs(figdir, exist_ok=True)
    out = os.path.join(figdir, "pseudo_chebyshev_uniform_scaling.png")
    plot(out)
    print(f"wrote {out}")
