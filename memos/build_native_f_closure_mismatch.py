"""
Build the native-F closure mismatch figure.

The figure is the visual companion to memos/NATIVE-F-MINIMAL-DEFINITION.md.
It shows the load-bearing obstruction:

    log side:    Affine composition remains two-parameter and flat.
    circle side: K_n = Q(cos(2 pi / n)) has degree phi(n)/2, unbounded.

The broken middle arrow records that a native F would have to preserve
closure-generator depth and account for the unbounded circle ladder.
"""

import math
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import FancyBboxPatch


N_MAX = 60
K_MAX = 20

INK = "#17202a"
LOG_BLUE = "#255c7e"
CIRCLE_GREEN = "#2e7d55"
PRIME_GOLD = "#d99b2b"
WITNESS_RED = "#b03a2e"
GRID = "0.90"


def euler_phi(m):
    result = m
    temp = m
    p = 2
    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            result -= result // p
        p += 1
    if temp > 1:
        result -= result // temp
    return result


def trace_degree(n):
    # Degree of Q(cos(2 pi/n)) over Q. For n = 3, 4, 6 this gives 1.
    return max(1, euler_phi(n) // 2)


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True


def draw_log_side(ax):
    ks = np.arange(1, K_MAX + 1)
    depth = np.full_like(ks, 2, dtype=float)

    ax.plot(ks, depth, color=LOG_BLUE, lw=3.0, zorder=3)
    ax.scatter(ks, depth, s=42, color=LOG_BLUE, edgecolor="white",
               linewidth=0.7, zorder=4)

    ax.text(
        10.5,
        2.55,
        r"$(x\mapsto ax+b)\circ(x\mapsto cx+d)$"
        "\n"
        r"$=x\mapsto (ac)x+(ad+b)$",
        ha="center",
        va="bottom",
        fontsize=12,
        color=INK,
        bbox=dict(boxstyle="round,pad=0.42", facecolor="white",
                  edgecolor="0.78", alpha=0.96),
    )
    ax.text(
        10.5,
        1.42,
        "finite affine composition never leaves\n"
        "the same two-parameter family",
        ha="center",
        va="top",
        fontsize=10.5,
        color=LOG_BLUE,
    )

    ax.set_xlim(0.4, K_MAX + 0.6)
    ax.set_ylim(0.0, 6.5)
    ax.set_title("log side: affine closure is flat", fontsize=13, loc="left")
    ax.set_xlabel("composition depth k")
    ax.set_ylabel("closure rank / depth")
    ax.set_xticks([1, 5, 10, 15, 20])
    ax.set_yticks([0, 1, 2, 3, 4, 5, 6])
    ax.grid(True, color=GRID, lw=0.55)


def draw_circle_side(ax):
    ns = np.arange(3, N_MAX + 1)
    degrees = np.array([trace_degree(int(n)) for n in ns])
    primes = np.array([is_prime(int(n)) for n in ns])

    composite_mask = ~primes
    ax.vlines(ns[composite_mask], 0, degrees[composite_mask],
              color=CIRCLE_GREEN, lw=1.6, alpha=0.74, zorder=2)
    ax.scatter(ns[composite_mask], degrees[composite_mask], s=28,
               color=CIRCLE_GREEN, edgecolor="white", linewidth=0.45,
               zorder=3)

    ax.vlines(ns[primes], 0, degrees[primes], color=PRIME_GOLD, lw=2.0,
              alpha=0.88, zorder=4)
    ax.scatter(ns[primes], degrees[primes], s=42, color=PRIME_GOLD,
               edgecolor=INK, linewidth=0.45, zorder=5)

    witness_n = 7
    witness_d = trace_degree(witness_n)
    ax.vlines([witness_n], 0, [witness_d], color=WITNESS_RED, lw=3.0,
              zorder=7)
    ax.scatter([witness_n], [witness_d], s=95, color=WITNESS_RED,
               edgecolor=INK, linewidth=0.75, zorder=8)
    ax.annotate(
        r"$n=7$: first cubic"
        "\n"
        r"$[K_7:\mathbb{Q}]=3$",
        xy=(witness_n, witness_d),
        xytext=(13, 7.8),
        arrowprops=dict(arrowstyle="->", color=WITNESS_RED, lw=1.0),
        fontsize=10.5,
        color=WITNESS_RED,
    )

    ax.annotate(
        r"prime rows: $(p-1)/2$"
        "\n"
        "make the unbounded ladder visible",
        xy=(47, trace_degree(47)),
        xytext=(31, 25.5),
        arrowprops=dict(arrowstyle="->", color=PRIME_GOLD, lw=1.0),
        fontsize=10.5,
        color="#8a5a08",
    )

    ax.set_xlim(2.2, N_MAX + 0.8)
    ax.set_ylim(0.0, max(degrees) + 3.0)
    ax.set_title(r"circle side: $K_n=\mathbb{Q}(\cos(2\pi/n))$ climbs",
                 fontsize=13, loc="left")
    ax.set_xlabel("polygon order n")
    ax.set_ylabel(r"closure depth  $[K_n:\mathbb{Q}]=\varphi(n)/2$")
    ax.yaxis.set_label_position("right")
    ax.set_xticks([3, 7, 10, 20, 30, 40, 50, 60])
    ax.grid(True, color=GRID, lw=0.55)

    handles = [
        Line2D([0], [0], marker="o", color=CIRCLE_GREEN, lw=0,
               markerfacecolor=CIRCLE_GREEN, markeredgecolor="white",
               label="composite n"),
        Line2D([0], [0], marker="o", color=PRIME_GOLD, lw=0,
               markerfacecolor=PRIME_GOLD, markeredgecolor=INK,
               label="prime n"),
        Line2D([0], [0], marker="o", color=WITNESS_RED, lw=0,
               markerfacecolor=WITNESS_RED, markeredgecolor=INK,
               label="n = 7 witness"),
    ]
    ax.legend(handles=handles, loc="upper left", fontsize=9,
              framealpha=0.94)


def draw_middle_obstruction(ax):
    ax.set_axis_off()
    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(0.0, 1.0)

    box = FancyBboxPatch(
        (0.12, 0.34),
        0.76,
        0.32,
        transform=ax.transAxes,
        boxstyle="round,pad=0.04,rounding_size=0.035",
        facecolor="white",
        edgecolor="0.70",
        linewidth=1.0,
        alpha=0.98,
        zorder=5,
    )
    ax.add_patch(box)

    ax.text(
        0.50,
        0.58,
        "native F?",
        ha="center",
        va="center",
        fontsize=13,
        fontweight="bold",
        color=INK,
        zorder=6,
    )
    ax.text(
        0.50,
        0.50,
        "A2 + A4 require\n"
        "an unbounded\n"
        "closure ladder",
        ha="center",
        va="center",
        fontsize=9.2,
        color="0.25",
        zorder=6,
    )
    ax.text(
        0.50,
        0.40,
        "but Aff is flat",
        ha="center",
        va="center",
        fontsize=11,
        color=WITNESS_RED,
        fontweight="bold",
        zorder=6,
    )

    ax.annotate(
        "",
        xy=(0.12, 0.50),
        xytext=(0.00, 0.50),
        arrowprops=dict(
            arrowstyle="->",
            color="0.35",
            lw=1.2,
            linestyle="--",
        ),
    )
    ax.annotate(
        "",
        xy=(1.00, 0.50),
        xytext=(0.88, 0.50),
        arrowprops=dict(
            arrowstyle="->",
            color="0.35",
            lw=1.2,
            linestyle="--",
        ),
    )
    ax.text(
        0.50,
        0.25,
        "closure-generator\npreservation breaks here",
        ha="center",
        va="center",
        fontsize=10,
        color=WITNESS_RED,
        style="italic",
    )
    ax.text(
        0.50,
        0.74,
        "broken arrow",
        ha="center",
        va="center",
        fontsize=9.5,
        color="0.40",
        style="italic",
    )


def plot(outpath):
    fig = plt.figure(figsize=(16.2, 7.2))
    gs = fig.add_gridspec(
        1,
        3,
        width_ratios=[1.0, 0.36, 1.0],
        wspace=0.12,
    )
    ax_left = fig.add_subplot(gs[0, 0])
    ax_mid = fig.add_subplot(gs[0, 1])
    ax_right = fig.add_subplot(gs[0, 2])

    draw_log_side(ax_left)
    draw_circle_side(ax_right)
    draw_middle_obstruction(ax_mid)

    fig.suptitle(
        "Native-F closure mismatch: flat affine closure vs unbounded trace fields",
        fontsize=15,
        fontweight="bold",
        y=0.975,
    )
    fig.text(
        0.5,
        0.925,
        r"No native functor can preserve closure-generator depth from "
        r"$Aff^+(\mathbb{R})$ to the ladder "
        r"$K_n=\mathbb{Q}(\cos(2\pi/n))$.",
        ha="center",
        va="center",
        fontsize=10.5,
        color="0.30",
    )
    fig.text(
        0.5,
        0.025,
        "Figure target: memos/NATIVE-F-MINIMAL-DEFINITION.md. "
        "The diagnostic rates and asymmetries are useful, but the theorem obstruction is this closure-depth mismatch.",
        ha="center",
        fontsize=9.5,
        color="0.35",
        style="italic",
    )

    plt.savefig(outpath, dpi=170, bbox_inches="tight")
    plt.close(fig)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    figdir = os.path.normpath(os.path.join(here, "..", "figures"))
    os.makedirs(figdir, exist_ok=True)
    outpath = os.path.join(figdir, "native_f_closure_mismatch.png")

    degrees = [trace_degree(n) for n in range(3, N_MAX + 1)]
    print(f"circle degree range for n=3..{N_MAX}: {min(degrees)}..{max(degrees)}")
    print(f"n=7 witness degree: {trace_degree(7)}")
    print(f"prime n=59 degree: {trace_degree(59)}")

    plot(outpath)
    print(f"wrote {outpath}")


if __name__ == "__main__":
    main()
