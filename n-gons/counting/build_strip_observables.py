"""
Minimal strip bridge figure:

- floor tangencies against a DH-grid,
- corner points against the crystallographic contour family
  X in {+1, +1/2, 0, -1/2, -1}.
"""

import math
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch, Rectangle


NS = range(3, 9)
DH = 12
GRID_COLOR = "#dbdbdb"
LEVEL_COLOR = "#d9d9d9"
TANGENCY_COLOR = "#111111"
CORNER_COLOR = "#111111"
POS_SPECIAL_COLOR = "#c0392b"
NEG_SPECIAL_COLOR = "#2b6cb0"
ZERO_SPECIAL_COLOR = "#111111"
HALF_POS_COLOR = "#d98c2b"
HALF_NEG_COLOR = "#5b8dd1"


def linspace(start, stop, count):
    if count <= 1:
        return [start]
    step = (stop - start) / (count - 1)
    return [start + i * step for i in range(count)]


def draw_strip_points(ax):
    for n in NS:
        y_n = 1.0 / math.cos(math.pi / n) - 1.0
        ax.axhline(y_n, color=LEVEL_COLOR, lw=1.0, linestyle="--", alpha=0.7, zorder=1)

        tangency_xs = [k / n for k in range(n)]
        ax.scatter(
            tangency_xs,
            [0.0] * n,
            s=14,
            color=TANGENCY_COLOR,
            edgecolors="none",
            zorder=4,
        )

        corner_xs = [((2 * k + 1) / (2 * n)) % 1.0 for k in range(n)]
        ax.scatter(
            corner_xs,
            [y_n] * n,
            s=18,
            color=CORNER_COLOR,
            edgecolors="white",
            linewidths=0.4,
            zorder=5,
        )


def draw_x_contour(ax, level):
    if level == 0.0:
        for x0 in (0.25, 0.75):
            ax.axvline(x0, color=ZERO_SPECIAL_COLOR, lw=1.8, ls="--", alpha=0.9, zorder=3)
        return

    if level == 1.0:
        color = POS_SPECIAL_COLOR
        lw = 2.0
        alpha = 0.95
        ls = "-"
    elif level == 0.5:
        color = HALF_POS_COLOR
        lw = 1.4
        alpha = 0.95
        ls = "-"
    elif level == -0.5:
        color = HALF_NEG_COLOR
        lw = 1.4
        alpha = 0.95
        ls = "-"
    else:
        color = NEG_SPECIAL_COLOR
        lw = 2.0
        alpha = 0.95
        ls = "-"
    x_grid = linspace(0.0, 1.0, 2401)
    current_x = []
    current_y = []
    segments = []

    for x in x_grid:
        c = math.cos(2.0 * math.pi * x)
        if abs(c) < 1e-9:
            valid = False
        else:
            r = level / c
            valid = (r > 0.0) and (1.0 <= r <= 2.0)
        if valid:
            current_x.append(x)
            current_y.append(r - 1.0)
        elif current_x:
            segments.append((current_x, current_y))
            current_x = []
            current_y = []

    if current_x:
        segments.append((current_x, current_y))

    for xs, ys in segments:
        ax.plot(xs, ys, color=color, lw=lw, alpha=alpha, ls=ls, zorder=3)


def plot(outpath):
    fig, ax = plt.subplots(figsize=(12.5, 6.2))

    floor_band = Rectangle(
        (0.0, 0.0),
        1.0,
        0.08,
        facecolor="white",
        edgecolor="0.75",
        hatch="////",
        linewidth=0.0,
        zorder=0,
    )
    ax.add_patch(floor_band)
    for m in range(DH + 1):
        x = m / DH
        ax.plot([x, x], [0.0, 0.08], color=GRID_COLOR, lw=1.0, alpha=0.9, zorder=1)

    draw_strip_points(ax)
    for level in (1.0, 0.5, 0.0, -0.5, -1.0):
        draw_x_contour(ax, level)

    ax.axhline(0.0, color="black", lw=2.0, zorder=4)

    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(-0.03, 1.03)
    ax.set_xlabel(r"strip angle $u=\theta/(2\pi)$")
    ax.set_ylabel(r"strip height $y=r-1$")
    ax.set_title("Strip Linkage | floor grid and special corner contours", fontsize=13)
    ax.set_xticks([0.0, 0.25, 0.5, 0.75, 1.0])
    ax.set_xticklabels(["0", "1/4", "1/2", "3/4", "1"])
    ax.grid(True, axis="y", color="0.94", lw=0.6)

    legend_handles = [
        Line2D([0], [0], color=POS_SPECIAL_COLOR, lw=2.0, label="X = +1"),
        Line2D([0], [0], color=HALF_POS_COLOR, lw=1.4, label="X = +1/2"),
        Line2D([0], [0], color=HALF_NEG_COLOR, lw=1.4, label="X = -1/2"),
        Line2D([0], [0], color=NEG_SPECIAL_COLOR, lw=2.0, label="X = -1"),
        Line2D([0], [0], color=ZERO_SPECIAL_COLOR, lw=1.8, ls="--", label="X = 0"),
        Line2D([0], [0], marker="o", color="none", markerfacecolor="black",
               markeredgecolor="white", markeredgewidth=0.4, markersize=6,
               label="corner / tangency point"),
        Patch(facecolor="white", edgecolor="0.55", hatch="////", label="DH-grid band"),
    ]
    ax.legend(
        handles=legend_handles,
        loc="upper right",
        fontsize=8.5,
        framealpha=0.98,
        borderpad=0.35,
        labelspacing=0.35,
        handlelength=2.2,
        handletextpad=0.6,
    )

    plt.tight_layout()
    plt.savefig(outpath, dpi=170, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    figdir = os.path.normpath(os.path.join(here, "..", "..", "figures"))
    os.makedirs(figdir, exist_ok=True)
    out = os.path.join(figdir, "counting_strip_observables.png")
    plot(out)
    print(f"wrote {out}")
