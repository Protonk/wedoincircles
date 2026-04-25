"""
Art rendering of the pseudo-Chebyshev node construction.

The geometry is smooth: rays from the origin to the shared tangent line
meet the circle at (cos(pi/n), sin(pi/n)). The arithmetic is not smooth:
the algebraic degree phi(2n)/2 jumps with the factorization of n. This
rendering keeps the construction label-free and lets degree class control
color, opacity, and the small comb below the anchor axis.
"""

import math
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from sage.all import RDF, cos, euler_phi, pi, sin, tan


N_MIN = 3
N_MAX = 64
BG = "#f8f5ef"
INK = "#2f3337"
CIRCLE = "#626568"
AXIS = "#8d918e"


def degree(n):
    return int(euler_phi(2 * n) // 2)


def tier(deg):
    if deg == 1:
        return ("#d1495b", 1.00, 1.85, 46)
    if deg == 2:
        return ("#f4a261", 0.92, 1.55, 38)
    if deg == 3:
        return ("#8e44ad", 0.94, 1.65, 42)
    if deg == 4:
        return ("#2e86ab", 0.86, 1.35, 34)
    if deg <= 6:
        return ("#168e4f", 0.72, 1.10, 27)
    if deg <= 10:
        return ("#1abc9c", 0.55, 0.90, 22)
    if deg <= 16:
        return ("#607a89", 0.24, 0.58, 15)
    return ("#536067", 0.12, 0.42, 10)


def node_data():
    rows = []
    for n in range(N_MIN, N_MAX + 1):
        deg = degree(n)
        x = float(RDF(cos(pi / n)))
        y = float(RDF(sin(pi / n)))
        h = float(RDF(tan(pi / n)))
        rows.append((n, deg, x, y, h))
    return rows


def draw_background(ax):
    theta = [i * math.pi / 2 / 320 for i in range(321)]
    xs = [math.cos(t) for t in theta]
    ys = [math.sin(t) for t in theta]

    ax.fill_between(xs, ys, 0, color="#fffdfa", alpha=0.76, zorder=0)
    ax.plot(xs, ys, color=CIRCLE, lw=2.0, alpha=0.78, zorder=8)
    ax.plot([0.0, 1.055], [0.0, 0.0], color=AXIS, lw=1.15, alpha=0.55, zorder=2)
    ax.plot([1.0, 1.0], [-0.46, 1.78], color=AXIS, lw=1.15, alpha=0.58, zorder=2)
    ax.scatter([0.0], [0.0], s=22, color=INK, alpha=0.82, zorder=30)


def draw_degree_comb(ax, rows):
    max_log = math.log2(max(deg for _, deg, _, _, _ in rows))

    for _, deg, x, _, _ in rows:
        color, alpha, lw, _ = tier(deg)
        height = 0.055 + 0.34 * math.log2(deg) / max_log
        ax.plot(
            [x, x],
            [-0.015, -0.015 - height],
            color=color,
            lw=max(0.55, lw * 1.15),
            alpha=min(0.82, alpha + 0.04),
            solid_capstyle="butt",
            zorder=22,
        )


def draw_construction(ax, rows):
    for _, deg, x, y, h in reversed(rows):
        color, alpha, lw, size = tier(deg)
        ax.plot(
            [0.0, 1.0],
            [0.0, h],
            color=color,
            lw=lw,
            alpha=alpha * 0.54,
            solid_capstyle="round",
            zorder=10,
        )
        ax.plot(
            [x, x],
            [0.0, y],
            color=color,
            lw=max(0.55, lw * 0.58),
            alpha=alpha * 0.30,
            zorder=9,
        )
        ax.plot(
            [0.988, 1.035],
            [h, h],
            color=color,
            lw=max(1.0, lw * 1.25),
            alpha=alpha * 0.70,
            solid_capstyle="round",
            zorder=14,
        )
        ax.scatter(
            [x],
            [y],
            s=size,
            color=color,
            alpha=min(0.96, alpha + 0.04),
            edgecolor=BG,
            linewidth=0.75,
            zorder=24,
        )


def draw_low_degree_pulses(ax, rows):
    low = [(n, deg, x, y, h) for n, deg, x, y, h in rows if deg <= 4]
    for _, deg, x, y, _ in low:
        color, alpha, _, _ = tier(deg)
        ax.scatter(
            [x],
            [-0.44],
            s=58 if deg <= 2 else 46,
            color=color,
            alpha=0.88,
            edgecolor=BG,
            linewidth=0.75,
            zorder=28,
        )
        ax.plot(
            [x, x],
            [-0.405, -0.46],
            color=color,
            lw=1.2,
            alpha=alpha * 0.62,
            zorder=23,
        )


def plot(outpath):
    rows = node_data()

    fig, ax = plt.subplots(figsize=(7.0, 9.0))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)

    draw_background(ax)
    draw_degree_comb(ax, rows)
    draw_construction(ax, rows)
    draw_low_degree_pulses(ax, rows)

    ax.set_xlim(-0.055, 1.075)
    ax.set_ylim(-0.50, 1.82)
    ax.set_aspect("equal")
    ax.axis("off")

    plt.savefig(outpath, dpi=210, bbox_inches="tight", pad_inches=0.01)
    plt.close(fig)


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    figdir = os.path.normpath(os.path.join(here, "..", "figures"))
    os.makedirs(figdir, exist_ok=True)
    out = os.path.join(figdir, "pseudo_chebyshev_nodes.png")
    plot(out)
    print(f"wrote {out}")
