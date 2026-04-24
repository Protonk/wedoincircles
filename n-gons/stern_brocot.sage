"""
Comparative Stern-Brocot / Thomae reconstruction for the denominator-rank
histogram behind `n-gons/N-GON-WHOLENESS.md` §7.

The designated-wholeness apparatus is stated in denominator-rank language.
This script preserves the classical mediant / popcorn reconstruction of the
same histogram as comparative material: every n-gon deposits tangency positions
at k/n on the unit circle, and reducing k/n to lowest terms p/q yields a
height profile indexed by q.

This script:
  1. Builds the mediant tree on (0,1) by recursion to depth D.
  2. Plots that tree in the classical dyadic layout.
  3. Plots the corresponding denominator-rank stems for F_N.
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize

from sage.all import Rational, gcd, QQ, Integer

# --------------------------------------------------------------------------
# Stern-Brocot tree by mediant recursion.
#   Each node carries (p/q, depth). Root is the mediant of 0/1 and 1/1 = 1/2.
# --------------------------------------------------------------------------

def stern_brocot(max_depth):
    """Return list of (fraction, depth, parent_index) walking SB tree in (0,1)."""
    nodes = []

    def rec(lo_p, lo_q, hi_p, hi_q, depth, parent):
        if depth > max_depth:
            return
        p, q = lo_p + hi_p, lo_q + hi_q
        idx = len(nodes)
        nodes.append((Rational((p, q)), depth, parent))
        rec(lo_p, lo_q, p, q, depth + 1, idx)
        rec(p, q, hi_p, hi_q, depth + 1, idx)

    rec(0, 1, 1, 1, 1, -1)
    return nodes


# --------------------------------------------------------------------------
# Farey set with multiplicity for the popcorn/Thomae plot.
# --------------------------------------------------------------------------

def farey_heights(N):
    """Return dict {Rational(p/q) in (0,1) : 1/q} for q in [2, N]."""
    heights = {}
    for q in range(2, N + 1):
        for p in range(1, q):
            if gcd(p, q) == 1:
                heights[Rational((p, q))] = Rational((1, q))
    return heights


# --------------------------------------------------------------------------
# Plot 1: the Stern-Brocot tree as a binary layout.
# --------------------------------------------------------------------------

def plot_tree(max_depth, outpath):
    nodes = stern_brocot(max_depth)

    # Binary layout: at depth d, place the 2^(d-1) nodes at evenly spaced x
    # positions in (0,1). y = -depth so root is on top.
    by_depth = {}
    for i, (frac, d, parent) in enumerate(nodes):
        by_depth.setdefault(d, []).append(i)

    pos = {}
    for d, idxs in by_depth.items():
        m = len(idxs)
        for j, i in enumerate(idxs):
            pos[i] = ((j + 0.5) / m, -d)

    fig, ax = plt.subplots(figsize=(14, 8))

    cmap = cm.viridis
    norm = Normalize(vmin=1, vmax=max_depth)

    # edges
    for i, (frac, d, parent) in enumerate(nodes):
        if parent >= 0:
            x0, y0 = pos[parent]
            x1, y1 = pos[i]
            ax.plot([x0, x1], [y0, y1], color="0.7", lw=0.8, zorder=1)

    # nodes + labels
    for i, (frac, d, parent) in enumerate(nodes):
        x, y = pos[i]
        ax.scatter([x], [y], s=60, color=cmap(norm(d)), zorder=2,
                   edgecolor="black", linewidth=0.4)
        ax.text(x, y - 0.25, f"{frac.numerator()}/{frac.denominator()}",
                ha="center", va="top", fontsize=8)

    ax.set_title(f"Comparative mediant tree in (0,1), depth ≤ {max_depth}")
    ax.set_xlim(-0.02, 1.02)
    ax.set_ylim(-max_depth - 1, 0)
    ax.set_xlabel("tree position (dyadic layout)")
    ax.set_ylabel("−depth")
    ax.set_yticks(range(-max_depth, 0))
    ax.set_yticklabels([str(d) for d in range(max_depth, 0, -1)])
    ax.grid(False)

    plt.tight_layout()
    plt.savefig(outpath, dpi=160)
    plt.close(fig)


# --------------------------------------------------------------------------
# Plot 2: Thomae popcorn stems over F_N.
# --------------------------------------------------------------------------

def plot_thomae(N, outpath):
    heights = farey_heights(N)

    xs = [float(f) for f in heights]
    ys = [float(h) for h in heights.values()]
    qs = [int(f.denominator()) for f in heights]

    fig, ax = plt.subplots(figsize=(14, 5))

    cmap = cm.viridis
    norm = Normalize(vmin=2, vmax=N)

    for x, y, q in zip(xs, ys, qs):
        ax.vlines(x, 0, y, color=cmap(norm(q)), lw=0.8)
        ax.plot([x], [y], marker="o", ms=3, color=cmap(norm(q)))

    ax.set_title(
        f"Comparative denominator-rank stems on F_{N}: height 1/q at each p/q ∈ (0,1)\n"
        f"(same histogram as the n-gon tangency plot, in classical popcorn language)"
    )
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 0.55)
    ax.set_xlabel("angle / 360°  =  p/q")
    ax.set_ylabel("height  =  1/q")

    sm = cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=ax, pad=0.01)
    cbar.set_label("denominator q")

    plt.tight_layout()
    plt.savefig(outpath, dpi=160)
    plt.close(fig)


# --------------------------------------------------------------------------
# Entry point.
# --------------------------------------------------------------------------

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    figdir = os.path.normpath(os.path.join(here, "..", "figures"))
    os.makedirs(figdir, exist_ok=True)

    tree_path = os.path.join(figdir, "stern_brocot_tree.png")
    thomae_path = os.path.join(figdir, "thomae_popcorn.png")

    plot_tree(max_depth=6, outpath=tree_path)
    plot_thomae(N=30, outpath=thomae_path)

    print(f"wrote {tree_path}")
    print(f"wrote {thomae_path}")
