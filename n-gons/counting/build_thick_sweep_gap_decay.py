"""
Gap-decay plot for the tilted thin sweep in THICK-SWEEP.md.

At slope s = 1/sqrt(3), compare the empirical minimum consecutive gap
between sweep coordinates c_{n,k} against the pigeonhole bound
2(1+s)/(N(N+1)-8).
"""

import math
import os
from bisect import bisect_left

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpmath import mp


mp.dps = 80

N_MIN = 5
N_MAX = 120
SLOPE = 1 / mp.sqrt(3)
HIGHLIGHTS = (20, 50, 100)


def polygon_c_values(n):
    y = 1 / mp.cos(mp.pi / n) - 1
    return [y - SLOPE * mp.mpf(2 * k + 1) / (2 * n) for k in range(n)]


def build_gap_data():
    coords = []
    min_gap = None

    ns = []
    empirical = []
    bounds = []

    for n in range(3, N_MAX + 1):
        for c in polygon_c_values(n):
            idx = bisect_left(coords, c)
            if idx > 0:
                gap = c - coords[idx - 1]
                min_gap = gap if min_gap is None else min(min_gap, gap)
            if idx < len(coords):
                gap = coords[idx] - c
                min_gap = gap if min_gap is None else min(min_gap, gap)
            coords.insert(idx, c)

        if n >= N_MIN:
            ns.append(n)
            empirical.append(float(min_gap))
            bounds.append(float(2 * (1 + SLOPE) / (n * (n + 1) - 8)))

    return ns, empirical, bounds


def plot(outpath):
    ns, empirical, bounds = build_gap_data()

    fig, ax = plt.subplots(figsize=(12.5, 7))

    ax.semilogy(ns, bounds, color="#b56576", lw=2.0, label="pigeonhole bound")
    ax.semilogy(ns, empirical, color="#2b6cb0", lw=2.0, label="empirical min consecutive gap")

    for n in HIGHLIGHTS:
        idx = ns.index(n)
        ax.scatter([n], [bounds[idx]], color="#b56576", s=34, zorder=4)
        ax.scatter([n], [empirical[idx]], color="#2b6cb0", s=34, zorder=4)

        ax.annotate(
            fr"$N={n}$",
            xy=(n, empirical[idx]),
            xytext=(5, 8),
            textcoords="offset points",
            fontsize=9,
            color="0.3",
        )

    ax.set_xlim(N_MIN, N_MAX)
    ax.set_xlabel("N")
    ax.set_ylabel("gap size")
    ax.set_title(r"Thin-sweep gap decay at slope $s = 1/\sqrt{3}$", fontsize=13)
    ax.grid(True, which="both", color="0.93", lw=0.6)
    ax.legend(loc="upper right", fontsize=10, framealpha=0.95)

    note = (
        r"The empirical minimum gap drops far below the averaging bound."
        "\n"
        r"For $N=20,50,100$ the empirical values are approximately "
        r"$2.9\times 10^{-5}, 1.4\times 10^{-7}, 4.5\times 10^{-8}$."
    )
    fig.text(0.5, 0.015, note, ha="center", va="bottom", fontsize=10, color="0.25")

    plt.tight_layout(rect=[0, 0.05, 1, 1])
    plt.savefig(outpath, dpi=170, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    figdir = os.path.normpath(os.path.join(here, "..", "..", "figures"))
    os.makedirs(figdir, exist_ok=True)
    out = os.path.join(figdir, "counting_thick_sweep_gap_decay.png")
    plot(out)
    print(f"wrote {out}")
