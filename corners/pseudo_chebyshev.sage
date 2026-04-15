"""
Two-pane visualization of the pseudo-Chebyshev node construction
(see `corners/PSEUDO-CHEBYSHEV-NODES.md`), shown for n = 3, 4, 5, 6, 7, 8.

Left pane — geometric construction:
  Unit circle (apothem-1 incircle). Shared anchor edge tangent at (1, 0),
  drawn as the vertical line x = 1. For each n, the first corner above the
  anchor is (1, tan(π/n)). The segment from the origin to that corner
  crosses the unit circle at (cos(π/n), sin(π/n)); the x-coordinate of
  that crossing is node(n).

Right pane — the node sequence:
  The six node values cos(π/n) as colored stems on the interval [0, 1],
  with n labels and the limit 1 marked.
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle as MplCircle

from sage.all import cos, sin, tan, pi, RDF


NS = [3, 4, 5, 6, 7, 8]

COLORS = {
    3: "#d1495b",  # red     — rational 1/2
    4: "#e07a00",  # orange  — √2/2
    5: "#b8860b",  # gold    — (1+√5)/4
    6: "#168e4f",  # green   — √3/2
    7: "#2e86ab",  # blue    — cubic
    8: "#6a4c93",  # purple  — quartic
}

# algebraic-degree label, for the legend
DEGREE = {3: 1, 4: 2, 5: 2, 6: 2, 7: 3, 8: 4}


def left_panel(ax):
    # unit circle
    ax.add_patch(MplCircle((0, 0), 1.0, fill=False, ec="black",
                           lw=1.8, zorder=4))

    # shared tangent line x = 1 (anchor edge strip)
    ax.axvline(1.0, color="0.55", lw=1.0, ls="--", zorder=2)
    ax.plot([1], [0], marker="*", color="black", ms=14, zorder=6)
    ax.annotate("anchor (1, 0)", xy=(1, 0), xytext=(-95, -18),
                textcoords="offset points", fontsize=9,
                arrowprops=dict(arrowstyle="->", lw=0.7))

    for n in NS:
        h = float(RDF(tan(pi / n)))           # corner height
        cx = float(RDF(cos(pi / n)))          # node(n)
        cy = float(RDF(sin(pi / n)))          # y of circle crossing
        color = COLORS[n]

        # segment origin -> corner
        ax.plot([0.0, 1.0], [0.0, h], color=color, lw=1.8,
                zorder=3, alpha=0.95)

        # corner marker (square) on the tangent line
        ax.plot([1.0], [h], marker="s", color=color, ms=7,
                markeredgecolor="black", markeredgewidth=0.5, zorder=5)
        ax.annotate(f"n={n}", xy=(1.0, h), xytext=(8, 0),
                    textcoords="offset points", fontsize=9,
                    color=color, va="center", zorder=6)

        # circle-crossing marker (dot) — this is (cos π/n, sin π/n)
        ax.plot([cx], [cy], marker="o", color=color, ms=8,
                markeredgecolor="black", markeredgewidth=0.5, zorder=6)

        # projection of the crossing down to the x-axis (the node value)
        ax.plot([cx, cx], [0.0, cy], color=color, lw=0.9,
                ls=":", zorder=2)
        ax.plot([cx], [0.0], marker="v", color=color, ms=7,
                markeredgecolor="black", markeredgewidth=0.4, zorder=6)

    # x-axis line for visual anchoring
    ax.axhline(0.0, color="0.75", lw=0.6, zorder=1)

    ax.set_xlim(-0.08, 1.22)
    ax.set_ylim(-0.22, 1.85)
    ax.set_aspect("equal")
    ax.set_title("Geometric construction:\n"
                 "segment from 0 to (1, tan(π/n)) crosses unit circle "
                 "at (cos(π/n), sin(π/n))")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True, color="0.92", lw=0.5)


def right_panel(ax):
    # [0, 1] number line with one stem per n at x = cos(π/n), height = n
    # so vertical position encodes the index and we can label cleanly.
    ax.axhline(0, color="0.75", lw=0.6, zorder=1)

    for n in NS:
        v = float(RDF(cos(pi / n)))
        color = COLORS[n]
        ax.vlines(v, 0, n, color=color, lw=2.2, zorder=3)
        ax.plot([v], [n], marker="o", color=color, ms=10,
                markeredgecolor="black", markeredgewidth=0.5, zorder=4)
        # label with exact/decimal and algebraic degree
        ax.annotate(
            f"n={n}   cos(π/{n}) ≈ {v:.4f}\n"
            f"deg φ(2·{n})/2 = {DEGREE[n]}",
            xy=(v, n), xytext=(8, -4), textcoords="offset points",
            fontsize=9, color=color, va="top", zorder=5,
        )

    # the limit
    ax.axvline(1.0, color="0.55", lw=1.0, ls="--", zorder=2)
    ax.annotate("limit cos(π/n) → 1", xy=(1.0, 8.7),
                xytext=(-135, 0), textcoords="offset points",
                fontsize=9, color="0.35", va="center",
                arrowprops=dict(arrowstyle="->", color="0.55", lw=0.7))

    ax.set_xlim(-0.02, 1.08)
    ax.set_ylim(0, 9.5)
    ax.set_xlabel("node value = cos(π/n)")
    ax.set_ylabel("n")
    ax.set_yticks(NS)
    ax.set_title("Node sequence (pseudo-Chebyshev):\n"
                 "one distinguished value per n, monotone increasing")
    ax.grid(True, axis="x", color="0.92", lw=0.5)


def plot(outpath):
    fig, (axL, axR) = plt.subplots(
        1, 2, figsize=(16, 8),
        gridspec_kw={"width_ratios": [1.0, 1.15]},
    )
    left_panel(axL)
    right_panel(axR)
    fig.suptitle(
        "Pseudo-Chebyshev nodes from the shared-anchor n-gon construction",
        fontsize=13, y=0.995,
    )
    plt.tight_layout()
    plt.savefig(outpath, dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    figdir = os.path.normpath(os.path.join(here, "..", "figures"))
    os.makedirs(figdir, exist_ok=True)
    out = os.path.join(figdir, "pseudo_chebyshev_nodes.png")
    plot(out)
    print(f"wrote {out}")
