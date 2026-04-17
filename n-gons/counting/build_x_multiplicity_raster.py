"""
Geometric multiplicity raster for M_N.

Rows are N, horizontal position is the actual vertex x-coordinate in the
outside-out sweep, and marker size/color encode multiplicity at that x.
"""

import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.colors import Normalize

from counting_utils import multiplicity_word


N_MIN = 5
N_MAX = 40


def build_points():
    points = []
    max_mult = 0
    for N in range(N_MIN, N_MAX + 1):
        counts, clusters = multiplicity_word(N)
        for count, cluster in zip(counts, clusters):
            x = float(cluster[0][0])
            points.append((x, N, count))
            max_mult = max(max_mult, count)
    return points, max_mult


def point_color(value, plasma, norm):
    if value == 1:
        return (0.10, 0.10, 0.10, 1.0)
    if value == 2:
        return (0.23, 0.63, 0.86, 1.0)
    return plasma(norm(value))


def point_size(value):
    if value == 1:
        return 14
    if value == 2:
        return 22
    return 18 + 5 * value


def plot(outpath):
    points, max_mult = build_points()
    plasma = plt.get_cmap("plasma")
    norm = Normalize(vmin=3, vmax=max_mult)

    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    cs = [point_color(p[2], plasma, norm) for p in points]
    ss = [point_size(p[2]) for p in points]

    fig, ax = plt.subplots(figsize=(13.5, 8.5))

    for x in (-2, -1, 0, 1):
        ax.axvline(x, color="0.84", ls=":", lw=0.9, zorder=0)
    for x in (-0.5, 0.5):
        ax.axvline(x, color="0.88", ls="--", lw=0.9, zorder=0)

    ax.scatter(xs, ys, s=ss, c=cs, edgecolors="0.2", linewidths=0.25, alpha=0.9)

    ax.set_xlim(-2.2, 1.2)
    ax.set_ylim(N_MIN - 1, N_MAX + 1)
    ax.set_xlabel("x (actual sweep coordinate)")
    ax.set_ylabel("N")
    ax.set_title(r"Multiplicity raster in actual x-space for $M_N$  (N = 5 … 40)", fontsize=13)
    ax.set_yticks(list(range(5, N_MAX + 1, 5)))
    ax.grid(True, axis="y", color="0.94", lw=0.6)

    legend_handles = [
        Line2D([0], [0], marker="o", color="none", markerfacecolor=(0.10, 0.10, 0.10, 1.0),
               markeredgecolor="0.2", markeredgewidth=0.25, markersize=5, label="multiplicity 1"),
        Line2D([0], [0], marker="o", color="none", markerfacecolor=(0.23, 0.63, 0.86, 1.0),
               markeredgecolor="0.2", markeredgewidth=0.25, markersize=6, label="multiplicity 2"),
        Line2D([0], [0], marker="o", color="none", markerfacecolor=plasma(norm(max(3, min(8, max_mult)))),
               markeredgecolor="0.2", markeredgewidth=0.25, markersize=8,
               label="multiplicity ≥ 3  (larger = higher)"),
    ]
    ax.legend(handles=legend_handles, loc="upper left", fontsize=9.5, framealpha=0.95)

    note = (
        r"Guides: $x \in \{-2,-1,0,+1\}$ dotted,  $x=\pm 1/2$ dashed."
        "\n"
        r"This is the geometric counterpart of the barcode: mass by actual x-position, not by word index."
    )
    fig.text(0.5, 0.02, note, ha="center", va="bottom", fontsize=10, color="0.25")

    plt.tight_layout(rect=[0, 0.05, 1, 1])
    plt.savefig(outpath, dpi=170, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    figdir = os.path.normpath(os.path.join(here, "..", "..", "figures"))
    os.makedirs(figdir, exist_ok=True)
    out = os.path.join(figdir, "counting_x_multiplicity_raster.png")
    plot(out)
    print(f"wrote {out}")
