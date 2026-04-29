"""
The reduction collapse: (k, n) integer lattice vs. reduced p/q.

Companion figure for measure/FOR-BREAKFAST.md. Shows the operative
arithmetic step BIND-Erasure refuses — the many-to-one projection
from integer pairs (k, n) to reduced rationals p/q — explicitly.

Top panel: every integer pair (k, n) with 1 <= k < n and 2 <= n <= N.
Each lattice point individuated; color encodes whether (k, n) is
already reduced (gcd = 1) or collapses on reduction (gcd > 1).

Bottom panel: Thomae popcorn at every reduced p/q with q <= N,
height 1/q. Identical structure to figures/thomae_popcorn.png at
the same N.

Between them: vertical projection bands at the most lossy rationals
(1/2, 1/3, 1/4, 1/5) and one lossless landmark (1/29), with the
collapse ratio floor(N/q) annotated. The label across the divider
names the operation: "the reduction step k/n -> p/q".

Output: figures/reduction_collapse.png
"""

import math
import os
from math import gcd

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


N = 30

COLOR_REDUCED = "#2b6cb0"        # blue: gcd(k,n) = 1
COLOR_NONREDUCED = "#d97706"     # orange: gcd(k,n) > 1
COLOR_STEM = "#1a202c"           # near-black for popcorn stems
COLOR_PROJECTION = "#7c3aed"     # purple for projection bands
COLOR_LOSSLESS = "#0f766e"       # teal for lossless landmark
COLOR_GRID = "#e5e7eb"


def integer_lattice_points(N):
    """All (k, n) with 1 <= k < n, 2 <= n <= N. Returns list of (x, n, gcd)."""
    points = []
    for n in range(2, N + 1):
        for k in range(1, n):
            g = gcd(k, n)
            x = k / n
            points.append((x, n, g))
    return points


def reduced_rationals(N):
    """All reduced p/q with 0 < p < q, 2 <= q <= N. Returns list of (x, q)."""
    rats = []
    for q in range(2, N + 1):
        for p in range(1, q):
            if gcd(p, q) == 1:
                rats.append((p / q, q))
    return rats


def plot(outpath):
    fig = plt.figure(figsize=(14.0, 10.5))
    gs = fig.add_gridspec(
        2, 1, height_ratios=[2.4, 1.0], hspace=0.55,
        top=0.88, bottom=0.07, left=0.07, right=0.97,
    )
    ax_top = fig.add_subplot(gs[0])
    ax_bot = fig.add_subplot(gs[1], sharex=ax_top)

    points = integer_lattice_points(N)
    n_total = len(points)
    rats = reduced_rationals(N)
    q_total = len(rats)

    # --- PROJECTION BANDS (drawn first, behind data) -------------------
    # Annotated landmarks: pruned to {1/2, 1/3, 2/3, 1/29} for legibility.
    # Highest-collapse (1/2 = 15-fold), the third-fraction pair (10-fold),
    # plus one lossless landmark (1-fold) for contrast.
    lossy_landmarks = [(1, 2), (1, 3), (2, 3)]
    lossless_landmark = (1, 29)

    for p, q in lossy_landmarks:
        x = p / q
        ax_top.axvline(x, color=COLOR_PROJECTION, lw=1.0, alpha=0.28, zorder=1)
        ax_bot.axvline(x, color=COLOR_PROJECTION, lw=1.0, alpha=0.28, zorder=1)

    x_lossless = lossless_landmark[0] / lossless_landmark[1]
    ax_top.axvline(x_lossless, color=COLOR_LOSSLESS, lw=1.0, alpha=0.45, zorder=1)
    ax_bot.axvline(x_lossless, color=COLOR_LOSSLESS, lw=1.0, alpha=0.45, zorder=1)

    # --- TOP: integer lattice -------------------------------------------
    xs_red = [p[0] for p in points if p[2] == 1]
    ys_red = [p[1] for p in points if p[2] == 1]
    xs_non = [p[0] for p in points if p[2] > 1]
    ys_non = [p[1] for p in points if p[2] > 1]

    ax_top.scatter(
        xs_red, ys_red, s=20, color=COLOR_REDUCED,
        edgecolors="white", linewidths=0.4, zorder=4,
        label=r"gcd($k$, $n$) = 1   (already reduced; one-to-one with popcorn stem)",
    )
    ax_top.scatter(
        xs_non, ys_non, s=20, color=COLOR_NONREDUCED,
        edgecolors="white", linewidths=0.4, zorder=4,
        label=r"gcd($k$, $n$) > 1   (collapses to a smaller-denominator stem)",
    )

    # Extend ylim to fit annotation band above data
    ax_top.set_ylim(1.5, N + 4.5)
    ax_top.set_yticks([2, 5, 10, 15, 20, 25, 30])
    ax_top.set_ylabel(r"polygon order $n$", fontsize=11)
    ax_top.set_title(
        f"Top: integer lattice $(k, n)$, $1 \\leq k < n \\leq {N}$"
        f"   —   {n_total} distinguishable points",
        fontsize=11.5, loc="left", pad=8,
    )
    ax_top.grid(True, axis="y", color=COLOR_GRID, lw=0.5, zorder=0)
    ax_top.legend(
        loc="lower center", bbox_to_anchor=(0.5, -0.02),
        fontsize=9.0, framealpha=0.96, borderpad=0.45,
        handletextpad=0.5, ncol=2,
    )

    # --- ANNOTATIONS inside the top panel above the data --------------
    # Stagger: 1/2 (largest collapse) on a higher row than the
    # third-pair, with the lossless landmark on the same row as 1/2.
    annotations = [
        (1, 2, r"$\frac{1}{2}$:  15$\to$1", "#4c1d95", N + 3.2),
        (1, 3, r"$\frac{1}{3}$:  10$\to$1", "#4c1d95", N + 1.5),
        (2, 3, r"$\frac{2}{3}$:  10$\to$1", "#4c1d95", N + 1.5),
        (1, 29, r"$\frac{1}{29}$:  1$\to$1   (lossless)", COLOR_LOSSLESS, N + 3.2),
    ]
    for p, q, label, color, ay in annotations:
        x = p / q
        ax_top.plot(
            [x, x], [N + 0.6, ay - 0.3],
            color=color, lw=0.7, alpha=0.55, zorder=2,
        )
        ax_top.text(
            x, ay, label,
            ha="center", va="bottom", fontsize=9.5, color=color,
            zorder=5,
        )

    # --- BOTTOM: popcorn ------------------------------------------------
    for x, q in rats:
        ax_bot.vlines(x, 0, 1.0 / q, color=COLOR_STEM, lw=0.9,
                      zorder=3, alpha=0.85)
        ax_bot.scatter(
            [x], [1.0 / q], s=11, color=COLOR_STEM,
            edgecolors="none", zorder=4,
        )

    ax_bot.set_ylim(0, 0.55)
    ax_bot.set_xlim(0, 1)
    ax_bot.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
    ax_bot.set_xticklabels(["0", "1/4", "1/2", "3/4", "1"])
    ax_bot.set_ylabel(r"height $= 1/q$", fontsize=11)
    ax_bot.set_xlabel(r"$x = p/q$  (reduced)", fontsize=11)
    ax_bot.set_title(
        f"Bottom: reduced rationals $p/q$, $q \\leq {N}$"
        f"   —   {q_total} stems",
        fontsize=11.5, loc="left", pad=8,
    )
    ax_bot.grid(True, axis="y", color=COLOR_GRID, lw=0.5, zorder=0)

    # --- DIVIDER LABEL --------------------------------------------------
    # Place midway between top and bottom panel (gridspec hspace=0.55,
    # top=0.88, bottom=0.07; the gap sits around y ≈ 0.34–0.36).
    fig.text(
        0.5, 0.350,
        r"the reduction step   $k/n \to p/q$",
        ha="center", fontsize=12, color="#4c1d95", style="italic",
        fontweight="bold",
    )
    fig.text(
        0.5, 0.328,
        r"(the operative arithmetic step BIND-Erasure refuses)",
        ha="center", fontsize=9.5, color="#4c1d95", style="italic",
    )

    # --- TITLE ----------------------------------------------------------
    fig.suptitle(
        r"The reduction collapse:  $k/n \to p/q$  many-to-one from "
        r"the integer lattice to reduced rationals",
        fontsize=13.5, fontweight="bold", y=0.97,
    )
    fig.text(
        0.5, 0.925,
        f"Same Farey horizon $N = {N}$.   "
        f"Integer lattice: {n_total} distinguishable $(k, n)$ points.   "
        f"Reduced popcorn: {q_total} stems.   "
        f"Collapse ratio at $p/q$ is $\\lfloor N/q \\rfloor \\to 1$.",
        ha="center", fontsize=10, color="0.3", style="italic",
    )

    plt.savefig(outpath, dpi=170, bbox_inches="tight")
    plt.close(fig)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    figdir = os.path.normpath(os.path.join(here, "..", "figures"))
    os.makedirs(figdir, exist_ok=True)
    out = os.path.join(figdir, "reduction_collapse.png")

    points = integer_lattice_points(N)
    rats = reduced_rationals(N)

    print(f"N = {N}")
    print(f"  integer lattice points (k, n) with 1 <= k < n: {len(points)}")
    print(f"  reduced rationals p/q in (0, 1) with q <= N : {len(rats)}")
    print(f"  collapse landmarks (lossy):")
    for q in (2, 3, 4, 5, 6, 7):
        print(f"    1/{q}: {N // q} -> 1")
    print(f"  collapse landmark (lossless):")
    print(f"    1/29: {N // 29} -> 1")

    plot(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
