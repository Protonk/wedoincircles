"""
Close-up of the shared-anchor 3-4-5 n-gon construction (NGON-WHOLENESS §1).

Circle of radius 1 (incircle). Each regular n-gon has apothem 1, so the circle
is inscribed in all of them. All n-gons share one edge tangent at the anchor
(1, 0), so they coincide along a vertical strip x = 1 near y = 0; they diverge
as their first corner above/below the anchor arrives at height a_n = tan(pi/n).

The figure zooms in tight on the upper-right region so the "bumps" — the
slivers between the circle arc and each polygon edge — are visible.
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as MplPolygon, Circle as MplCircle
from matplotlib.collections import PatchCollection

from sage.all import cos, sin, tan, sec, pi, RDF, vector


def ngon_vertices(n):
    """Corners of the regular n-gon with unit incircle, anchor edge on x=1.

    Edge k is tangent at angle 2*pi*k/n. Corner between edge k and edge k+1
    sits at angle (2k+1)*pi/n, distance sec(pi/n).
    """
    R = RDF(sec(pi / n))
    return [
        (R * RDF(cos((2 * k + 1) * pi / n)),
         R * RDF(sin((2 * k + 1) * pi / n)))
        for k in range(n)
    ]


def tangency_points(n):
    """Position k of the n-gon — tangency of edge k with the incircle."""
    return [
        (RDF(cos(2 * pi * k / n)), RDF(sin(2 * pi * k / n)))
        for k in range(n)
    ]


def plot_anchor_345(outpath):
    fig, ax = plt.subplots(figsize=(9, 10))

    # unit circle
    circle = MplCircle((0, 0), 1.0, fill=False, ec="black", lw=2.2, zorder=5)
    ax.add_patch(circle)

    # outermost first so the inner polygons' outlines sit on top where
    # edges coincide on the anchor strip x = 1.
    specs = [
        (3, "#d1495b", 5.5, "triangle (n=3)"),
        (4, "#2e86ab", 3.3, "square (n=4)"),
        (5, "#168e4f", 1.6, "pentagon (n=5)"),
    ]

    for n, color, lw, label in specs:
        verts = ngon_vertices(n)
        outline = MplPolygon(verts, closed=True, fill=False,
                             edgecolor=color, lw=lw, zorder=3,
                             joinstyle="miter", label=label)
        ax.add_patch(outline)

    # radii from center to the first corner above the anchor
    # (length = sec(pi/n), meeting edge at (1, tan(pi/n)))
    for n, color, lw, _ in specs:
        h = float(RDF(tan(pi / n)))
        R = float(RDF(sec(pi / n)))
        ax.plot([0.0, 1.0], [0.0, h],
                linestyle=(0, (6, 3)), color=color, lw=max(1.2, lw * 0.55),
                zorder=2, alpha=0.9)
        ax.annotate(
            f"|sec(π/{n})| = {R:.3f}",
            xy=(0.5, h / 2.0), xytext=(-10, 6), textcoords="offset points",
            fontsize=8, color=color,
        )

    # tangency markers (positions 0 and 1 of each n-gon in view)
    for n, color, _, _ in specs:
        for k in (0, 1):
            tx, ty = tangency_points(n)[k]
            ax.plot([tx], [ty], "o", color=color, ms=8,
                    markeredgecolor="black", markeredgewidth=0.6, zorder=7)
            ax.annotate(
                f"n={n}, k={k}",
                xy=(tx, ty), xytext=(7, 7), textcoords="offset points",
                fontsize=8, color=color, zorder=8,
            )

    # anchor callout
    ax.plot([1], [0], marker="*", color="black", ms=16, zorder=9)
    ax.annotate("anchor (1, 0)", xy=(1, 0), xytext=(-95, -20),
                textcoords="offset points", fontsize=10, zorder=9,
                arrowprops=dict(arrowstyle="->", lw=0.8))

    # corner-height labels at each polygon's first corner above the anchor
    for n, color, _, _ in specs:
        h = float(RDF(tan(pi / n)))
        ax.annotate(
            f"  corner: (1, tan(π/{n})) = (1, {h:.3f})",
            xy=(1.0, h), xytext=(10, 0), textcoords="offset points",
            fontsize=8.5, color=color, va="center", zorder=9,
        )
        ax.plot([1.0], [h], marker="s", color=color, ms=6,
                markeredgecolor="black", markeredgewidth=0.5, zorder=8)

    # highlight the bump regions (polygon minus disk) visible in frame.
    # Pentagon's unique bump is the thin sliver between its edge 1 and the
    # arc from (1,0.727) to tangency at (cos72, sin72).
    ax.annotate("pentagon bump", xy=(0.78, 0.82),
                xytext=(0.38, 0.55), fontsize=9, color="#168e4f",
                arrowprops=dict(arrowstyle="->", color="#168e4f", lw=0.8))
    ax.annotate("square bump", xy=(0.62, 1.0),
                xytext=(0.18, 1.22), fontsize=9, color="#2e86ab",
                arrowprops=dict(arrowstyle="->", color="#2e86ab", lw=0.8))
    ax.annotate("triangle bump (edge turns at y≈1.732)",
                xy=(1.0, 1.55), xytext=(0.18, 1.65),
                fontsize=9, color="#d1495b",
                arrowprops=dict(arrowstyle="->", color="#d1495b", lw=0.8))

    ax.set_xlim(-0.05, 1.35)
    ax.set_ylim(-0.12, 1.85)
    ax.set_aspect("equal")
    ax.set_title(
        "Shared-anchor close-up: 3-gon, 4-gon, 5-gon inscribing one circle\n"
        "(apothem = 1, anchor at (1, 0); bumps = polygon ∖ disk)"
    )
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend(loc="lower left", framealpha=0.95)
    ax.grid(True, color="0.9", lw=0.5)

    plt.tight_layout()
    plt.savefig(outpath, dpi=180)
    plt.close(fig)


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    figdir = os.path.normpath(os.path.join(here, "..", "figures"))
    os.makedirs(figdir, exist_ok=True)
    out = os.path.join(figdir, "anchor_345.png")
    plot_anchor_345(out)
    print(f"wrote {out}")
