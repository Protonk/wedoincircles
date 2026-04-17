import os
import math

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


NS = [3, 7]
COLORS = {3: "#d1495b", 7: "#9b59b6"}
NAMES = {3: "triangle", 7: "heptagon"}

CUT_COLOR = "#555555"
CUT_LW = 1.6


def linspace(start, stop, count):
    if count <= 1:
        return [start]
    step = (stop - start) / (count - 1)
    return [start + i * step for i in range(count)]


def _draw_polar(ax, r_func, r_node_func, rmax, title):
    theta_full = linspace(0.0, 2 * math.pi, 600)
    ax.plot(theta_full, [1.0] * len(theta_full), color="black", lw=2.0, zorder=5)

    for n in NS:
        color = COLORS[n]
        r_node = r_node_func(n)
        ax.plot(theta_full, [r_node] * len(theta_full),
                color=color, lw=0.8, linestyle=":", alpha=0.6, zorder=2)
        for k in range(n):
            alpha_k = 2 * math.pi * k / n
            theta_lo = alpha_k - math.pi / n
            theta_hi = alpha_k + math.pi / n
            theta = linspace(theta_lo, theta_hi, 300)
            r = [r_func(t - alpha_k) for t in theta]
            ax.plot(theta, r, color=color, lw=2.0, alpha=0.9)

        corner_angles = [(2 * k + 1) * math.pi / n for k in range(n)]
        ax.plot(corner_angles, [r_node] * n, "o", color=color, ms=5,
                markeredgecolor="black", markeredgewidth=0.5, zorder=6)

    # Cut line at 0° (right side → strip left edge)
    ax.plot([0, 0], [0, rmax * 0.97], color=CUT_COLOR, lw=CUT_LW,
            ls="--", zorder=7, alpha=0.7)

    ax.set_rmin(0)
    ax.set_rmax(rmax)
    ax.set_rticks([])
    ax.set_yticklabels([])
    ax.set_thetagrids([0, 90, 180, 270], ["0°", "90°", "180°", "270°"],
                      fontsize=9, color="0.5")
    ax.set_title(title, fontsize=13, pad=14)
    ax.grid(True, alpha=0.15)


def draw_inside_out(ax):
    _draw_polar(
        ax,
        r_func=lambda dt: math.cos(dt),
        r_node_func=lambda n: math.cos(math.pi / n),
        rmax=1.1,
        title="(a)  Inside-out",
    )


def draw_outside_out(ax):
    _draw_polar(
        ax,
        r_func=lambda dt: 1.0 / math.cos(dt),
        r_node_func=lambda n: 1.0 / math.cos(math.pi / n),
        rmax=2.1,
        title="(b)  Outside-out",
    )


def draw_strip(ax):
    for n in NS:
        color = COLORS[n]
        y_n = 1.0 / math.cos(math.pi / n) - 1.0
        for k in range(n):
            alpha_k = 2 * math.pi * k / n
            theta_lo = alpha_k - math.pi / n
            theta_hi = alpha_k + math.pi / n
            theta = linspace(theta_lo, theta_hi, 300)
            x = [((t / (2 * math.pi)) % 1.0) for t in theta]
            y = [(1.0 / math.cos(t - alpha_k)) - 1.0 for t in theta]

            start = 0
            for i in range(len(x) - 1):
                if abs(x[i + 1] - x[i]) > 0.5:
                    if i + 1 - start > 1:
                        ax.plot(x[start:i + 1], y[start:i + 1],
                                color=color, lw=2.0, alpha=0.9)
                    start = i + 1
            if len(x) - start > 1:
                ax.plot(x[start:], y[start:], color=color, lw=2.0, alpha=0.9)

        ax.axhline(y_n, color=color, lw=0.8, linestyle=":", zorder=4, alpha=0.5)

        corner_x = [(2 * k + 1) / (2 * n) for k in range(n)]
        ax.plot(corner_x, [y_n] * n, "o", color=color, ms=5,
                markeredgecolor="black", markeredgewidth=0.5, zorder=6)

    ax.axhline(0, color="black", lw=2.0, zorder=5)

    # Cut lines at both edges (identified)
    for xcut in [0, 1]:
        ax.axvline(xcut, color=CUT_COLOR, lw=CUT_LW, ls="--", alpha=0.7, zorder=7)

    ax.set_xlim(0, 1)
    ax.set_ylim(-0.04, 1.08)
    ax.set_xlabel(r"angle  $\theta / 2\pi$", fontsize=11)
    ax.set_ylabel(r"height  $\sec(\pi/n) - 1$", fontsize=11)
    ax.set_title("(c)  Strip (cut at 0° and unrolled)", fontsize=13)
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.set_xticklabels(["0", "¼", "½", "¾", "1"])
    ax.grid(True, alpha=0.12)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    figdir = os.path.normpath(os.path.join(here, "..", "figures"))
    os.makedirs(figdir, exist_ok=True)

    fig = plt.figure(figsize=(13, 12))
    gs = GridSpec(2, 2, figure=fig, height_ratios=[2.5, 1],
                  hspace=0.08, wspace=0.08)

    ax_inside = fig.add_subplot(gs[0, 0], projection="polar")
    ax_outside = fig.add_subplot(gs[0, 1], projection="polar")
    ax_strip = fig.add_subplot(gs[1, :])

    draw_inside_out(ax_inside)
    draw_outside_out(ax_outside)
    draw_strip(ax_strip)

    # Inversion annotation between the two polars
    fig.text(0.50, 0.68, r"$z \;\leftrightarrow\; 1/z$",
             ha="center", va="center", fontsize=16, color="0.3",
             bbox=dict(boxstyle="round,pad=0.4", facecolor="white",
                       edgecolor="0.75", alpha=0.9))

    fig.suptitle("Three views of the Archimedean strip",
                 fontsize=15, y=0.98)

    # Polygon key at bottom
    x_start = 0.34
    for i, n in enumerate(NS):
        fig.text(x_start + i * 0.18, 0.005, "■",
                 ha="center", va="bottom", fontsize=15, color=COLORS[n])
        fig.text(x_start + i * 0.18 + 0.015, 0.005,
                 f" n = {n}  ({NAMES[n]})",
                 ha="left", va="bottom", fontsize=12, color="0.25")

    outpath = os.path.join(figdir, "archimedean_triptych.png")
    plt.savefig(outpath, dpi=170, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {outpath}")


if __name__ == "__main__":
    main()
