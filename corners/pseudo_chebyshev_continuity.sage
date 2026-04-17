"""
Continuity demonstration for the pseudo-Chebyshev construction.

The pseudo-Chebyshev nodes (see `corners/PSEUDO-CHEBYSHEV-NODES.md`) are
generated at integer n by the construction documented in
`n-gons/N-GON-WHOLENESS.md`: a regular n-gon circumscribing the unit
circle with one edge tangent at the anchor (1, 0); the corner of
that edge above the anchor sits at (1, tan(π/n)); the segment from
the origin to that corner crosses the unit circle at
(cos(π/n), sin(π/n)); the node is the x-coordinate cos(π/n).

The construction admits a real-valued continuation: replace n ∈ ℤ_{≥2}
with t ∈ [2, ∞). The corner (1, tan(π/t)) sweeps continuously down
the vertical anchor line x = 1 as t grows; the crossing point
(cos(π/t), sin(π/t)) sweeps along the upper-right quarter of the
unit circle; in node-sequence coordinates, the sweep traces the
curve x = cos(π/n) for n ∈ [2, ∞), equivalently n = π/arccos(x).

This script plots both panes together. The left pane shows the
geometric construction with integer-n segments overlaid on the
continuous circle arc. The right pane shows the node-sequence curve
with integer-n samples as stems.

See `corners/PSEUDO-CHEBYSHEV-NODES.md` §§"Real-t continuation" and "Arithmetic density along the curve" for the accompanying note.
"""

import os
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle as MplCircle


# --- pseudo-Chebyshev primitives ---

def node(t):
    """cos(π/t): pseudo-Chebyshev node at real t ≥ 2."""
    return math.cos(math.pi / t)


def corner_y(t):
    """tan(π/t): y-coordinate of the n-gon corner directly above the anchor."""
    return math.tan(math.pi / t)


def crossing(t):
    """(cos(π/t), sin(π/t)): where the origin-to-corner segment meets the unit circle."""
    return (math.cos(math.pi / t), math.sin(math.pi / t))


# --- plotting helpers ---

INTEGER_NS_LEFT = (3, 4, 5, 6, 7, 8, 10, 12)
INTEGER_NS_RIGHT = (2, 3, 4, 5, 6, 7, 8, 10, 12, 16, 20, 30)


def left_panel(ax):
    """Geometric construction: unit circle + continuous arc of crossings
    + segments-to-corner for a selection of integer n."""
    # unit circle
    ax.add_patch(MplCircle((0, 0), 1.0, fill=False, ec="black", lw=1.8, zorder=3))

    # vertical anchor line x = 1
    ax.axvline(1.0, color="0.55", ls="--", lw=1.0, zorder=2)

    # continuous trajectory of the crossing point along the upper-right circle arc,
    # drawn slightly thicker to make the continuity explicit
    ts = np.linspace(2.005, 80.0, 400)
    xs = [math.cos(math.pi / t) for t in ts]
    ys = [math.sin(math.pi / t) for t in ts]
    ax.plot(xs, ys, color="#2e4a7d", lw=2.6, alpha=0.35, zorder=2,
            label="crossing point as t sweeps continuously")

    # integer-n segments and crossing points
    cmap = plt.get_cmap("viridis")
    denom = max(len(INTEGER_NS_LEFT) - 1, 1)
    for i, n in enumerate(INTEGER_NS_LEFT):
        color = cmap(i / denom)
        cx, cy = crossing(n)
        yc = corner_y(n)
        # segment from origin to (1, tan(π/n)), extending only within the frame
        ax.plot([0, 1], [0, yc], color=color, lw=1.4, zorder=4, alpha=0.9)
        # crossing point on the unit circle
        ax.plot([cx], [cy], marker="o", color=color, ms=8,
                markeredgecolor="black", markeredgewidth=0.5, zorder=5)
        ax.annotate(f"n={n}", xy=(cx, cy), xytext=(6, 6),
                    textcoords="offset points", fontsize=8, color=color,
                    zorder=6)

    # anchor
    ax.plot([1], [0], marker="*", color="black", ms=13, zorder=7)
    ax.annotate("anchor (1, 0)", xy=(1, 0), xytext=(-80, -18),
                textcoords="offset points", fontsize=9, zorder=7,
                arrowprops=dict(arrowstyle="->", lw=0.7))

    ax.set_xlim(-0.08, 1.25)
    ax.set_ylim(-0.18, 1.20)
    ax.set_aspect("equal")
    ax.set_title("Geometric construction\n"
                 "(integer samples on a continuous arc)")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True, color="0.92", lw=0.5)
    ax.legend(loc="lower left", fontsize=8, framealpha=0.95)


def right_panel(ax):
    """Node-sequence pane: smooth curve n = π/arccos(x) with integer stems."""
    # smooth curve: sweep t continuously, plot (cos(π/t), t)
    ts = np.linspace(2.0, 60.0, 800)
    xs = [math.cos(math.pi / t) for t in ts]
    ax.plot(xs, ts, color="black", lw=1.8, zorder=3,
            label="x = cos(π/n),  n ∈ [2, ∞)  (smooth curve)")

    # integer-n samples
    cmap = plt.get_cmap("viridis")
    denom = max(len(INTEGER_NS_RIGHT) - 1, 1)
    for i, n in enumerate(INTEGER_NS_RIGHT):
        nv = node(n)
        color = cmap(i / denom)
        # stem from y = 0 up to the curve at (nv, n)
        ax.vlines(nv, 0, n, color=color, lw=1.5, alpha=0.7, zorder=4)
        # dot at the integer sample
        ax.plot([nv], [n], marker="o", color=color, ms=10,
                markeredgecolor="black", markeredgewidth=0.5, zorder=5)
        # label
        ax.annotate(f"n={n}", xy=(nv, n), xytext=(6, -3),
                    textcoords="offset points", fontsize=8, color=color,
                    zorder=6)

    # asymptote at x = 1
    ax.axvline(1.0, color="0.55", ls="--", lw=1.0, zorder=2)
    ax.annotate("x = 1  (asymptote, n → ∞)",
                xy=(1, 25), xytext=(-135, 6), textcoords="offset points",
                fontsize=9, color="0.35",
                arrowprops=dict(arrowstyle="->", color="0.55", lw=0.7))

    # Niven note: only rational node values at t = 2 (node = 0) and t = 3 (node = 1/2)
    ax.annotate("only rational\nnode values:\nnode(2)=0, node(3)=1/2",
                xy=(0.25, 4.5), fontsize=8, color="0.25",
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="0.7", lw=0.5),
                zorder=7)

    ax.set_xlim(-0.03, 1.09)
    ax.set_ylim(1.3, 35)
    ax.set_xlabel("node value = cos(π/n)")
    ax.set_ylabel("n")
    ax.set_title("Node-sequence space:\n"
                 "smooth analytic curve with integer samples")
    ax.grid(True, color="0.92", lw=0.5)
    ax.legend(loc="upper left", fontsize=8, framealpha=0.95)


def plot(outpath):
    fig, (axL, axR) = plt.subplots(
        1, 2, figsize=(15, 7.5),
        gridspec_kw={"width_ratios": [1.0, 1.18]},
    )
    left_panel(axL)
    right_panel(axR)
    fig.suptitle(
        "Continuity: pseudo-Chebyshev nodes as integer samples on a smooth curve",
        fontsize=13, y=0.995,
    )
    plt.tight_layout()
    plt.savefig(outpath, dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    figdir = os.path.normpath(os.path.join(here, "..", "figures"))
    os.makedirs(figdir, exist_ok=True)
    out = os.path.join(figdir, "pseudo_chebyshev_continuity.png")
    plot(out)
    print(f"wrote {out}")
