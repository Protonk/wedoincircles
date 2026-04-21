import os
import math
import random

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Randomized-anchor variant of inside_out.py.
#
# Same construction: each n-gon edge, after inversion z -> 1/z, becomes an
# arc r = cos(theta - alpha) of a diameter-1 Apollonius circle tangent to
# the unit circle at angle alpha, drawn over theta in [alpha - pi/n, alpha + pi/n].
# Corners at radius cos(pi/n), angles alpha + (2k+1)*pi/n - 2*pi*k/n wait,
# equivalently: for each edge index k, alpha_k = 2*pi*k/n + phi_n and the
# corner above that edge sits at angle alpha_k + pi/n.
#
# Difference from inside_out.py: each n gets an independent random rotation
# phi_n ~ Uniform[0, 2*pi). The shared tangent anchor at (1, 0) and all the
# accidental arc overlaps go away.

NS = range(3, 9)
COLORS = {
    3: "#d1495b",
    4: "#2e86ab",
    5: "#168e4f",
    6: "#f4a261",
    7: "#9b59b6",
    8: "#1abc9c",
}

SEED = 20260420


def linspace(start, stop, count):
    if count <= 1:
        return [start]
    step = (stop - start) / (count - 1)
    return [start + i * step for i in range(count)]


def plot(outpath, seed=SEED):
    rng = random.Random(seed)
    phis = {n: rng.uniform(0.0, 2.0 * math.pi) for n in NS}

    fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(projection="polar"))

    theta_full = linspace(0.0, 2.0 * math.pi, 600)
    ax.plot(theta_full, [1.0] * len(theta_full), color="black", lw=2.0, zorder=5)

    for n in NS:
        color = COLORS[n]
        r_node = math.cos(math.pi / n)
        phi = phis[n]
        ax.plot(
            theta_full,
            [r_node] * len(theta_full),
            color=color,
            lw=1.0,
            linestyle=":",
            alpha=0.7,
            zorder=2,
        )
        for k in range(n):
            alpha = 2 * math.pi * k / n + phi
            theta_lo = alpha - math.pi / n
            theta_hi = alpha + math.pi / n
            theta = linspace(theta_lo, theta_hi, 300)
            r = [math.cos(t - alpha) for t in theta]
            ax.plot(theta, r, color=color, lw=1.5, alpha=0.85)
        corner_angles = [(2 * k + 1) * math.pi / n + phi for k in range(n)]
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
    ax.set_rticks([])
    ax.set_yticklabels([])
    ax.set_title("Inside-out annulus, randomized anchors\nn = 3 … 8", fontsize=12, pad=15)
    ax.grid(True, alpha=0.2)

    plt.tight_layout()
    plt.savefig(outpath, dpi=160, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    figdir = os.path.normpath(os.path.join(here, "..", "figures"))
    os.makedirs(figdir, exist_ok=True)
    out = os.path.join(figdir, "archimedean_inside_out_randomized.png")
    plot(out)
    print(f"wrote {out}")
