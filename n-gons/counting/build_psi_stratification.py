"""
ψ-colored support plot for the outside-out corner sweep.

The row at fixed n lives in the trace field ℚ(cos(2π/n)), whose native
circle-side degree is φ(n)/2. This script nevertheless colors by ψ(n), not by
φ(n)/2, because ψ is the additive prime-power invariant used by PERMEATE's
cross-domain matching: it is structurally comparable to the log side's v_p
bookkeeping, whereas φ(n)/2 is the native closure depth of the circle side
alone.
"""

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


def min_distance_to_guide(n_max, guide):
    """Minimum distance from any outside-out vertex x-coordinate to one guide."""
    best_dist = float("inf")
    best_n = None
    for n in range(3, n_max + 1):
        sec_val = 1.0 / np.cos(np.pi / n)
        angles = (2 * np.arange(n) + 1) * np.pi / n
        xs = sec_val * np.cos(angles)
        local_min = float(np.min(np.abs(xs - guide)))
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
    pos_dist, pos_n = min_distance_to_guide(VERIFY_N_MAX, 0.5)
    neg_dist, neg_n = min_distance_to_guide(VERIFY_N_MAX, -0.5)
    print(f"[verify] min |x ± 1/2| over n ≤ {VERIFY_N_MAX}: {verify_dist:.3e} (achieved at n = {verify_n})")
    print(f"[verify] min |x - 1/2| over n ≤ {VERIFY_N_MAX}: {pos_dist:.3e} (achieved at n = {pos_n})")
    print(f"[verify] min |x + 1/2| over n ≤ {VERIFY_N_MAX}: {neg_dist:.3e} (achieved at n = {neg_n})")

    fig, ax = plt.subplots(figsize=(14.2, 9.7))

    # --- theorem-witness row ---------------------------------------------
    ax.axhspan(6.55, 7.45, color=CLASS_COLORS[6], alpha=0.12, zorder=-2)
    ax.text(-2.17, 7.0, r"$n=7$ witness", color="#8a5a08",
            fontsize=9.5, va="center", ha="left", fontweight="bold")

    # --- guide lines -----------------------------------------------------
    backbone_guides = [-2, -1, 0, 1]
    for px in backbone_guides:
        ax.axvline(px, color=BACKBONE_COLORS[px], linestyle=":",
                   linewidth=1.0, alpha=0.55, zorder=0)
    for px in EMPTY_GUIDES:
        ax.axvline(px, color=EMPTY_GUIDE_COLOR, linestyle="--",
                   linewidth=1.0, alpha=0.55, zorder=0)

    # --- scatter (shrunk markers relative to v1 so the tail doesn't crush) --
    for n in ns:
        verts = polygon_vertices(n)
        xs = verts[:, 0]
        color = color_for(n)
        size = 45 if psi_vals[n] == 2 else (32 if psi_vals[n] <= 6 else 24)
        ax.scatter(xs, [n] * len(xs), color=color, s=size,
                   edgecolor="0.15", linewidth=0.3, alpha=alpha_for(n),
                   zorder=5 if psi_vals[n] == 2 else 3)

    # --- axes -------------------------------------------------------------
    ax.set_xlabel(r"vertex $x$-coordinate", fontsize=12)
    ax.set_ylabel(r"polygon order  $n$", fontsize=12)
    ax.set_yticks(list(range(5, N_MAX + 1, 5)))
    ax.set_ylim(N_MIN - 1.0, N_MAX + 1)
    ax.set_xlim(-2.2, 1.2)
    ax.grid(True, color="0.96", lw=0.4, axis="y")

    # colored x-ticks at guide positions carrying guide identity
    tick_spec = [
        (-2.0,  r"$-2$",    BACKBONE_COLORS[-2]),
        (-1.0,  r"$-1$",    BACKBONE_COLORS[-1]),
        (-0.5,  r"$-1/2$",  EMPTY_GUIDE_COLOR),
        ( 0.0,  r"$0$",     BACKBONE_COLORS[0]),
        ( 0.5,  r"$+1/2$",  EMPTY_GUIDE_COLOR),
        ( 1.0,  r"$+1$",    BACKBONE_COLORS[1]),
    ]
    ax.set_xticks([p for p, _, _ in tick_spec])
    ax.set_xticklabels([lbl for _, lbl, _ in tick_spec])
    for tick_label, (_, _, color) in zip(ax.get_xticklabels(), tick_spec):
        tick_label.set_color(color)
        tick_label.set_fontweight("bold")

    # Only label the empty guides above the plot; the backbone guide names
    # are already carried by the colored x-ticks.
    ax.text(0.5, N_MAX + 0.45, r"empty guide", color=EMPTY_GUIDE_COLOR,
            fontsize=9.5, ha="center", va="bottom")
    ax.text(-0.5, N_MAX + 0.45, r"empty guide", color=EMPTY_GUIDE_COLOR,
            fontsize=9.5, ha="center", va="bottom")

    ax.annotate(
        r"first cubic row",
        xy=(-0.90, 7.0),
        xytext=(-1.43, 11.5),
        arrowprops=dict(arrowstyle="->", color="#8a5a08", lw=0.9),
        fontsize=9.5,
        color="#8a5a08",
        ha="left",
    )

    # --- legend (vertical, upper-left negative space) ---------------------
    legend_patches = [
        Patch(facecolor=CLASS_COLORS[2],      label=r"$\psi = 2$"),
        Patch(facecolor=CLASS_COLORS[4],      label=r"$\psi = 4$"),
        Patch(facecolor=CLASS_COLORS[6],      label=r"$\psi = 6$  (first cubic, $n = 7$)"),
        Patch(facecolor=CLASS_COLORS["8-12"], label=r"$\psi \in \{8, 10, 12\}$"),
        Patch(facecolor=CLASS_COLORS[">=14"], label=r"$\psi \geq 14$"),
    ]
    ax.legend(handles=legend_patches,
              loc="upper left", bbox_to_anchor=(0.01, 0.985),
              ncol=1, frameon=True, framealpha=0.92,
              edgecolor="0.8", fontsize=9.7,
              title=r"$\psi(n)$ class", title_fontsize=11)

    # --- suptitle + caption -----------------------------------------------
    fig.suptitle(
        r"$\psi$-stratified $x$-support of the outside-out corner sweep",
        fontsize=14.5, fontweight="bold", y=0.995,
    )
    fig.text(
        0.5, 0.957,
        r"Focus: the $n=7$ first-cubic row and the tested-empty rational guides at $x=\pm1/2$.",
        ha="center", fontsize=10.1, color="0.32",
    )
    fig.text(
        0.5, 0.015,
        r"$n \in [" + str(N_MIN) + r", " + str(N_MAX) + r"]$    "
        r"points: $x_{n,k}=\sec(\pi/n)\cos((2k+1)\pi/n)$;    "
        f"$x=\\pm1/2$ verified empty through $n \\leq {VERIFY_N_MAX}$: "
        f"best $+1/2$ gap ${pos_dist:.1e}$ at $n={pos_n}$, "
        f"best $-1/2$ gap ${neg_dist:.1e}$ at $n={neg_n}$",
        ha="center", fontsize=9.5, color="0.35", style="italic",
    )

    plt.tight_layout(rect=[0.0, 0.04, 1.0, 0.94])
    outpath = os.path.join(figdir, "counting_psi_stratification.png")
    plt.savefig(outpath, dpi=170, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {outpath}")


if __name__ == "__main__":
    main()
