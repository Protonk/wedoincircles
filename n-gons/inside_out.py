import os
import math

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Inversion z -> 1/z applied to the annulus {1 <= r <= 2}.
# Result: annulus {1/2 <= r <= 1}.
#
# n-gon edge k: original r = sec(theta - 2*pi*k/n)
#   inverted:              r = cos(theta - 2*pi*k/n)
#   same angular span: theta in [(2k-1)*pi/n, (2k+1)*pi/n]
#
# Corners invert to radius cos(pi/n) = node(n).
# n=3 arcs reach the inner boundary (r=1/2) exactly.
# n>=4 arcs float; endpoints sit at r = cos(pi/n) > 1/2.

NS = range(3, 9)
COLORS = {
    3: "#d1495b",
    4: "#2e86ab",
    5: "#168e4f",
    6: "#f4a261",
    7: "#9b59b6",
    8: "#1abc9c",
}


def linspace(start, stop, count):
    if count <= 1:
        return [start]
    step = (stop - start) / (count - 1)
    return [start + i * step for i in range(count)]


def plot(outpath):
    fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(projection="polar"))

    theta_full = linspace(0.0, 2.0 * math.pi, 600)
    ax.plot(theta_full, [1.0] * len(theta_full), color="black", lw=2.0, zorder=5)
    ax.plot(
        theta_full,
        [0.5] * len(theta_full),
        color="#d1495b",
        lw=2.0,
        linestyle="--",
        zorder=5,
    )

    for n in NS:
        color = COLORS[n]
        r_node = math.cos(math.pi / n)
        for k in range(n):
            alpha = 2 * math.pi * k / n
            theta_lo = alpha - math.pi / n
            theta_hi = alpha + math.pi / n
            theta = linspace(theta_lo, theta_hi, 300)
            r = [math.cos(t - alpha) for t in theta]
            ax.plot(theta, r, color=color, lw=1.5, alpha=0.85)
        corner_angles = [(2 * k + 1) * math.pi / n for k in range(n)]
        ax.plot(
            corner_angles,
            [r_node] * n,
            "o",
            color=color,
            ms=4,
            markeredgecolor="black",
            markeredgewidth=0.5,
            zorder=6,
        )

    ax.set_rmin(0)
    ax.set_rmax(1.1)
    ax.set_rticks([0.5, 1.0])
    ax.set_yticklabels(["½  (inverted 3-cir)", "1  (incircle)"], fontsize=8)
    ax.set_title("Inside-out annulus\nn = 3 … 8", fontsize=12, pad=15)
    ax.grid(True, alpha=0.2)

    plt.tight_layout()
    plt.savefig(outpath, dpi=160, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    figdir = os.path.normpath(os.path.join(here, "..", "figures"))
    os.makedirs(figdir, exist_ok=True)
    out = os.path.join(figdir, "archimedean_inside_out.png")
    plot(out)
    print(f"wrote {out}")
