import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np
from mpmath import mp


mp.dps = 60

N_MIN = 3
N_MAX = 40
VERIFY_N_MAX = 400
EMPTY_GUIDES = (-0.5, 0.5)


def psi(n):
    """Crystallographic restriction function.
    Additive on prime-power parts: ψ(2)=0, ψ(2^r)=2^(r-1) for r≥2, ψ(p^r)=p^r−p^(r-1) for odd p."""
    def psi_pp(p, r):
        if p == 2:
            return 0 if r == 1 else 2 ** (r - 1)
        return p ** r - p ** (r - 1)
    if n <= 1:
        return 0
    total = 0
    temp = n
    p = 2
    while p * p <= temp:
        if temp % p == 0:
            r = 0
            while temp % p == 0:
                temp //= p
                r += 1
            total += psi_pp(p, r)
        p += 1
    if temp > 1:
        total += psi_pp(temp, 1)
    return total


def polygon_vertices(n):
    sec_val = 1 / mp.cos(mp.pi / n)
    verts = []
    for k in range(n):
        theta = (2 * k + 1) * mp.pi / n
        verts.append((float(sec_val * mp.cos(theta)), float(sec_val * mp.sin(theta))))
    return np.array(verts)


def min_distance_to_halves(n_max):
    """Minimum distance from any outside-out vertex x-coord to ±1/2, over polygons n ∈ [3, n_max]."""
    best_dist = float("inf")
    best_n = None
    for n in range(3, n_max + 1):
        sec_val = 1.0 / np.cos(np.pi / n)
        angles = (2 * np.arange(n) + 1) * np.pi / n
        xs = sec_val * np.cos(angles)
        dists = np.minimum(np.abs(xs - 0.5), np.abs(xs + 0.5))
        local_min = float(np.min(dists))
        if local_min < best_dist:
            best_dist = local_min
            best_n = n
    return best_dist, best_n


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    figdir = os.path.normpath(os.path.join(here, "..", "..", "figures"))
    os.makedirs(figdir, exist_ok=True)

    ns = list(range(N_MIN, N_MAX + 1))
    psi_vals = {n: psi(n) for n in ns}

    CLASS_COLORS = {
        2: "#d62728",      # crimson
        4: "#ff8c1a",      # orange
        6: "#d4a017",      # gold
        "8-12": "#2a9d8f", # teal (combines ψ ∈ {8, 10, 12})
        ">=14": "#6b7a90", # muted slate
    }

    def psi_class(n):
        p = psi_vals[n]
        if p in {2, 4, 6}:
            return p
        if p in {8, 10, 12}:
            return "8-12"
        return ">=14"

    def color_for(n):
        return CLASS_COLORS[psi_class(n)]

    def alpha_for(n):
        cls = psi_class(n)
        if cls == 2:
            return 1.0
        if cls in {4, 6, "8-12"}:
            return 0.88
        return 0.62

    BACKBONE_COLORS = {
        1: "#c0392b",   # red — tangent (forced for every polygon)
        -1: "#2c5d8f",  # blue — anti-tangent (forced for every even polygon)
        0: "#2c5d8f",   # blue — forced for every n ≡ 2 (mod 4)
        -2: "#888888",  # gray — triangle-only (hapax)
    }
    EMPTY_GUIDE_COLOR = "#e87722"  # orange — Niven-rational, empty

    verify_dist, verify_n = min_distance_to_halves(VERIFY_N_MAX)
    print(f"[verify] min |x ± 1/2| over n ≤ {VERIFY_N_MAX}: {verify_dist:.3e} (achieved at n = {verify_n})")

    fig, ax = plt.subplots(figsize=(13, 10))

    backbone_guides = [-2, -1, 0, 1]
    for px in backbone_guides:
        ax.axvline(px, color=BACKBONE_COLORS[px], linestyle=":",
                   linewidth=1.0, alpha=0.6, zorder=0)
    for px in EMPTY_GUIDES:
        ax.axvline(px, color=EMPTY_GUIDE_COLOR, linestyle="--",
                   linewidth=1.0, alpha=0.6, zorder=0)

    for px in backbone_guides:
        label = f"x = {px:+d}" if px != 0 else "x = 0"
        ax.text(px, N_MIN - 1.6, label, ha="center", va="top",
                fontsize=11, color=BACKBONE_COLORS[px])
    for px in EMPTY_GUIDES:
        label = f"x = {px:+.1f}\nempty"
        ax.text(px, N_MIN - 1.6, label, ha="center", va="top",
                fontsize=9.5, color=EMPTY_GUIDE_COLOR)

    for n in ns:
        verts = polygon_vertices(n)
        xs = verts[:, 0]
        color = color_for(n)
        size = 60 if psi_vals[n] == 2 else (40 if psi_vals[n] <= 6 else 28)
        ax.scatter(xs, [n] * len(xs), color=color, s=size,
                   edgecolor="0.15", linewidth=0.3, alpha=alpha_for(n),
                   zorder=5 if psi_vals[n] == 2 else 3)

    ax.set_xlabel("x (vertex x-coordinate)", fontsize=12)
    ax.set_ylabel("polygon $n$", fontsize=12)
    ax.set_title(
        r"$\psi$-stratified x-support of the outside-out corner sweep,"
        f"  $n = {N_MIN}..{N_MAX}$",
        fontsize=14,
    )
    ax.set_yticks(list(range(5, N_MAX + 1, 5)))
    ax.set_ylim(N_MIN - 2.7, N_MAX + 1)
    ax.set_xlim(-2.2, 1.2)
    ax.grid(True, color="0.96", lw=0.4, axis="y")

    legend_patches = [
        Patch(facecolor=CLASS_COLORS[2],      label=r"$\psi = 2$:  $n \in \{3, 4, 6\}$"),
        Patch(facecolor=CLASS_COLORS[4],      label=r"$\psi = 4$:  $n \in \{5, 8, 10, 12\}$"),
        Patch(facecolor=CLASS_COLORS[6],      label=r"$\psi = 6$:  $n \in \{7, 9, 14, 15, 18, 20, 24, 30\}$"),
        Patch(facecolor=CLASS_COLORS["8-12"], label=r"$\psi \in \{8, 10, 12\}$:  $n \in \{11, 13, 16, 21, 22, 26, 28, 33, 35, 36, 40\}$"),
        Patch(facecolor=CLASS_COLORS[">=14"], label=r"$\psi \geq 14$:  remaining rows"),
    ]
    ax.legend(handles=legend_patches, loc="upper left", fontsize=10,
              framealpha=0.95, title=r"$\psi(n)$ class", title_fontsize=11)

    caption = (
        r"Companion view of $\mathtt{counting\_strip\_observables.png}$ (polygon-indexed rather than strip-indexed)."
        "\n"
        r"This is a support plot, not a multiplicity plot: each dot marks a vertex x-position, colored by $\psi(n)$."
        "\n"
        r"The persistent exceptional columns of $M_N$ lie on the planar backbone $x \in \{-1, 0, +1\}$ (red/blue); "
        r"the point at $x=-2$ is triangle-only."
        "\n"
        r"The comparison guides $x = \pm 1/2$ (orange, dashed) are exact-empty over the tested range: "
        f"minimum $|x \\pm 1/2|$ for $n \\leq {VERIFY_N_MAX}$ is ${verify_dist:.2e}$ (at $n = {verify_n}$), "
        r"and $\to 0$ as $n \to \infty$ at rate $O(1/n^2)$ along odd multiples of $3$."
    )
    fig.text(0.5, 0.015, caption, ha="center", va="bottom", fontsize=10,
             color="0.2")

    plt.tight_layout(rect=[0, 0.09, 1, 1])
    outpath = os.path.join(figdir, "counting_psi_stratification.png")
    plt.savefig(outpath, dpi=170, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {outpath}")


if __name__ == "__main__":
    main()
