"""
Cyclotomic isolation barcode for fft/DEFICIT-VS-CYCLOTOMIC-MULTIPLICITY.md.

Plots the radix-2 DIT isolation state of each cyclotomic factor Phi_d
for the cyclic DFT of size N = 64. Row heights are weighted by phi(d),
so the visible area changing from lumped to isolated at each stage is
the stage contribution Delta iso(j).

States:
  - lumped: Phi_d still shares a modulus with another Phi_{d'}
  - isolated, unresolved: all current sub-product moduli meeting Phi_d
    contain only roots from mu_d, but are not yet linear factors
  - fully resolved: final linear-factor stage

Produces:
    figures/cyclotomic_isolation_barcode_n64.png
"""

import os
from math import log2

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import Patch, Rectangle


LUMPED = "lumped"
ISOLATED = "isolated, unresolved"
RESOLVED = "fully resolved"

STATE_COLORS = {
    LUMPED: "#d9d9d9",
    ISOLATED: "#4c78a8",
    RESOLVED: "#12385b",
}


def phi_power_two(d):
    if d == 1:
        return 1
    return d // 2


def cyclotomic_factors(n):
    k = int(log2(n))
    return [1] + [2 ** e for e in range(1, k + 1)]


def state_for_factor(d, stage, n):
    """Radix-2 DIT isolation state after stage j for N = 2^k."""
    k = int(log2(n))
    if stage == 0:
        return LUMPED
    if stage == k:
        return RESOLVED

    # For N = 2^k, stage j peels Phi_{2^(k-j+1)}; prior peeled
    # factors remain isolated until the final linear-factor stage.
    if d >= 2 ** (k - stage + 1):
        return ISOLATED
    return LUMPED


def iso_trajectory(n):
    k = int(log2(n))
    values = [0]
    cumulative = 0
    for stage in range(1, k):
        cumulative += n // (2 ** stage)
        values.append(cumulative)
    values.append(n)
    return values


def plot_barcode(n, outpath):
    k = int(log2(n))
    factors = cyclotomic_factors(n)
    heights = {d: phi_power_two(d) for d in factors}
    iso = iso_trajectory(n)
    delta_iso = [None] + [iso[j] - iso[j - 1] for j in range(1, k + 1)]

    fig = plt.figure(figsize=(10.2, 7.2))
    grid = fig.add_gridspec(nrows=2, ncols=1, height_ratios=[1.0, 5.2], hspace=0.08)
    ax_top = fig.add_subplot(grid[0])
    ax = fig.add_subplot(grid[1], sharex=ax_top)

    # Top strip: row-deficit clearing is flat, Delta Psi(j) = N.
    stages = list(range(1, k + 1))
    ax_top.bar(
        stages,
        [1.0] * k,
        width=0.72,
        color="#f28e2b",
        edgecolor="white",
        linewidth=1.2,
        zorder=2,
    )
    for stage in stages:
        ax_top.text(
            stage,
            0.52,
            r"$\Delta\Psi/N=1$",
            ha="center",
            va="center",
            fontsize=8.5,
            color="white",
            rotation=90,
        )
        ax_top.text(
            stage,
            1.08,
            rf"$\Delta iso={delta_iso[stage]}$",
            ha="center",
            va="bottom",
            fontsize=8.5,
            color="0.2",
        )
    ax_top.set_ylim(0, 1.32)
    ax_top.set_yticks([])
    ax_top.set_ylabel(r"$\Delta\Psi$", rotation=0, labelpad=28, va="center")
    ax_top.spines["left"].set_visible(False)
    ax_top.spines["right"].set_visible(False)
    ax_top.spines["top"].set_visible(False)
    ax_top.tick_params(axis="x", labelbottom=False, bottom=False)

    # Weighted barcode: stage columns show state after stage j.
    y_bottoms = {}
    y = 0
    for d in factors:
        y_bottoms[d] = y
        y += heights[d]

    for stage in range(0, k + 1):
        for d in factors:
            state = state_for_factor(d, stage, n)
            rect = Rectangle(
                (stage - 0.5, y_bottoms[d]),
                1.0,
                heights[d],
                facecolor=STATE_COLORS[state],
                edgecolor="white",
                linewidth=1.15,
            )
            ax.add_patch(rect)

    for stage, value in enumerate(iso):
        ax.text(
            stage,
            n + 1.4,
            rf"$iso={value}$",
            ha="center",
            va="bottom",
            fontsize=8.5,
            color="0.25",
        )

    ax.annotate(
        r"$\Phi_1,\Phi_2$ co-emerge",
        xy=(k, 1.0),
        xytext=(k - 2.45, 9.0),
        arrowprops=dict(arrowstyle="->", lw=0.9, color="0.25"),
        fontsize=9,
        color="0.25",
    )

    y_centers = [1.0] + [y_bottoms[d] + heights[d] / 2.0 for d in factors[2:]]
    y_labels = [r"$\Phi_1,\Phi_2$  $\varphi=1$ each"] + [
        rf"$\Phi_{{{d}}}$  $\varphi={heights[d]}$" for d in factors[2:]
    ]
    ax.set_yticks(y_centers)
    ax.set_yticklabels(y_labels)
    ax.set_ylim(0, n + 6.0)
    ax.set_xlim(-0.5, k + 0.5)
    ax.set_xticks(range(0, k + 1))
    ax.set_xlabel("stage j (state after stage)")
    ax.set_ylabel("cyclotomic factor, weighted by degree")
    ax.grid(axis="x", color="0.85", linewidth=0.8)
    fig.suptitle(
        "Cyclotomic isolation barcode: radix-2 DIT, cyclic DFT, N = 64",
        y=0.965,
        fontsize=14,
    )

    legend = [
        Patch(facecolor=STATE_COLORS[LUMPED], edgecolor="white", label="lumped"),
        Patch(
            facecolor=STATE_COLORS[ISOLATED],
            edgecolor="white",
            label="isolated, unresolved",
        ),
        Patch(facecolor=STATE_COLORS[RESOLVED], edgecolor="white", label="fully resolved"),
        Patch(facecolor="#f28e2b", edgecolor="white", label=r"$\Delta\Psi/N=1$"),
    ]
    fig.legend(
        handles=legend,
        loc="lower center",
        ncol=4,
        framealpha=0.95,
        bbox_to_anchor=(0.5, 0.02),
    )

    fig.subplots_adjust(top=0.86, bottom=0.16, left=0.17, right=0.98, hspace=0.12)
    fig.savefig(outpath, dpi=170, bbox_inches="tight")
    plt.close(fig)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    figdir = os.path.normpath(os.path.join(here, "..", "figures"))
    os.makedirs(figdir, exist_ok=True)
    out = os.path.join(figdir, "cyclotomic_isolation_barcode_n64.png")
    plot_barcode(64, out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
