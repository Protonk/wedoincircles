"""
Comparative denominator-rank stems for the rational-support histogram behind
`n-gons/N-GON-WHOLENESS.md` §7.

The designated-wholeness apparatus is stated in denominator-rank language:
every n-gon deposits tangency positions at k/n on the unit circle, and reducing
k/n to lowest terms p/q yields a height profile indexed by q.

This script preserves only the denominator-height comparison plot. The old
tree-centered companion was removed because the operative invariant here is
divisibility/multiplicity, not generation order.
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize

from sage.all import Rational, gcd


# --------------------------------------------------------------------------
# Reduced rational support with denominator-height data.
# --------------------------------------------------------------------------

def denominator_heights(N):
    """Return dict {Rational(p/q) in (0,1) : 1/q} for q in [2, N]."""
    heights = {}
    for q in range(2, N + 1):
        for p in range(1, q):
            if gcd(p, q) == 1:
                heights[Rational((p, q))] = Rational((1, q))
    return heights


# --------------------------------------------------------------------------
# Plot denominator-rank stems over F_N.
# --------------------------------------------------------------------------

def plot_thomae(N, outpath):
    heights = denominator_heights(N)

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
        f"(normalized shadow of the n-gon tangency-floor multiplicity histogram)"
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

    thomae_path = os.path.join(figdir, "thomae_popcorn.png")

    plot_thomae(N=30, outpath=thomae_path)

    print(f"wrote {thomae_path}")
