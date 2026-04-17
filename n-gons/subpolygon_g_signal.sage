"""
Signal plot for the subpolygon order g_n(DH) = gcd(n, DH).

Companion to `n-gons/SUBPOLYGON.md`.

Three stacked panels for DH = 36, 360, 3600, showing the integer-valued
function n -> g_n(DH) on 1 <= n <= 30. Green means full survival (g = n),
red means anchor-only survival (g = 1), and blue means partial survival.
"""

import os
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


DHS = (36, 360, 3600)
NS = tuple(range(1, 31))
FULL_COLOR = "#2a9d59"
PARTIAL_COLOR = "#2b6cb0"
ANCHOR_COLOR = "#d1495b"


def g_value(n, dh):
    return math.gcd(n, dh)


def classify_color(n, g):
    if g == n:
        return FULL_COLOR
    if g == 1:
        return ANCHOR_COLOR
    return PARTIAL_COLOR


def panel(ax, dh):
    gs = [g_value(n, dh) for n in NS]
    colors = [classify_color(n, g) for n, g in zip(NS, gs)]

    for n, g, color in zip(NS, gs, colors):
        ax.vlines(n, 0, g, color=color, lw=2.0, alpha=0.9, zorder=2)
        ax.plot([n], [g], marker="o", ms=5.8, color=color,
                markeredgecolor="black", markeredgewidth=0.4, zorder=3)

    ax.set_xlim(0.5, 30.5)
    ax.set_ylim(0, 31)
    ax.set_xticks(range(1, 31, 2))
    ax.set_ylabel("g_n(DH)")
    ax.set_title(f"DH = {dh}", fontsize=11)
    ax.grid(True, axis="y", color="0.9", lw=0.6)


def plot(outpath):
    fig, axes = plt.subplots(3, 1, figsize=(12, 10), sharex=True)
    for ax, dh in zip(axes, DHS):
        panel(ax, dh)

    axes[-1].set_xlabel("n")
    legend_handles = [
        Line2D([0], [0], color=FULL_COLOR, lw=2.0, marker="o",
               markeredgecolor="black", markeredgewidth=0.4,
               label="full survival (g = n)"),
        Line2D([0], [0], color=PARTIAL_COLOR, lw=2.0, marker="o",
               markeredgecolor="black", markeredgewidth=0.4,
               label="partial survival (1 < g < n)"),
        Line2D([0], [0], color=ANCHOR_COLOR, lw=2.0, marker="o",
               markeredgecolor="black", markeredgewidth=0.4,
               label="anchor only (g = 1)"),
    ]
    axes[0].legend(handles=legend_handles, loc="upper right", fontsize=8, framealpha=0.95)

    fig.suptitle("Subpolygon order signal n -> g_n(DH) = gcd(n, DH)", fontsize=14, y=0.995)
    plt.tight_layout()
    plt.savefig(outpath, dpi=160)
    plt.close(fig)


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    figdir = os.path.normpath(os.path.join(here, "..", "figures"))
    os.makedirs(figdir, exist_ok=True)
    out = os.path.join(figdir, "subpolygon_g_signal.png")
    plot(out)
    print(f"wrote {out}")
