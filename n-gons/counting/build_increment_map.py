import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch
from mpmath import mp

from counting_utils import multiplicity_word


N_MIN = 5   # earliest "previous" N; first transition rendered is 5 → 6
N_MAX = 40

EMPTY = 0
UNCHANGED = 1
GREW = 2
INSERTED = 3

MATCH_TOL = mp.mpf("1e-30")


def classify_step(counts_prev, clusters_prev, counts_curr, clusters_curr, tol):
    labels = []
    i_prev = 0
    for i_curr, cluster in enumerate(clusters_curr):
        x_curr = cluster[0][0]
        while (i_prev < len(clusters_prev)
               and clusters_prev[i_prev][0][0] < x_curr - tol):
            i_prev += 1
        if (i_prev < len(clusters_prev)
                and abs(clusters_prev[i_prev][0][0] - x_curr) < tol):
            if counts_prev[i_prev] == counts_curr[i_curr]:
                labels.append(UNCHANGED)
            else:
                labels.append(GREW)
            i_prev += 1
        else:
            labels.append(INSERTED)
    return labels


def build_rows(n_min, n_max, tol):
    words = {}
    for N in range(n_min, n_max + 1):
        words[N] = multiplicity_word(N)

    max_len = max(len(counts) for (counts, _) in words.values())
    rows = []
    for N in range(n_min + 1, n_max + 1):
        counts_prev, clusters_prev = words[N - 1]
        counts_curr, clusters_curr = words[N]
        labels = classify_step(counts_prev, clusters_prev,
                               counts_curr, clusters_curr, tol)
        row = labels + [EMPTY] * (max_len - len(labels))
        rows.append((N, row))
    return rows, max_len


def plot_increment_map(rows, max_len, outpath):
    n_targets = [r[0] for r in rows]
    image = [r[1] for r in rows]

    cmap = ListedColormap([
        (1.00, 1.00, 1.00),  # EMPTY
        (0.94, 0.94, 0.94),  # UNCHANGED — faint backdrop, keeps the staircase
        (0.90, 0.45, 0.10),  # GREW — deeper orange
        (0.10, 0.60, 0.25),  # INSERTED — deeper green
    ])

    fig, ax = plt.subplots(figsize=(14, 10))
    ax.imshow(image, aspect="auto", interpolation="nearest", origin="upper",
              cmap=cmap, vmin=0, vmax=3)
    ax.set_title(r"Incremental update map $M_{N-1} \to M_N$ (N = 6 … 40)",
                 fontsize=13)
    ax.set_xlabel(r"Position in $M_N$")
    ax.set_ylabel(r"N")

    y_ticks = [i for i, N in enumerate(n_targets) if N % 5 == 0]
    ax.set_yticks(y_ticks)
    ax.set_yticklabels([str(n_targets[y]) for y in y_ticks])

    x_ticks = list(range(0, max_len, 25))
    ax.set_xticks(x_ticks)
    ax.set_xticklabels([str(x + 1) for x in x_ticks])

    legend_patches = [
        Patch(facecolor=(0.94, 0.94, 0.94), label="unchanged"),
        Patch(facecolor=(0.90, 0.45, 0.10), label="grew (higher multiplicity)"),
        Patch(facecolor=(0.10, 0.60, 0.25), label="inserted (new x-column)"),
    ]
    ax.legend(
        handles=legend_patches,
        loc="upper right",
        fontsize=10,
        framealpha=0.95,
        bbox_to_anchor=(0.995, 0.995),
    )

    annotation = (
        "Each row: the transition $M_{N-1} \\to M_N$.\n\n"
        "Orange cells are the three growth events\n"
        "from the closed-form decomposition:\n"
        "  · terminal at $x = +1$ (every row)\n"
        "  · count at $x = -1$ (N even)\n"
        "  · count at $x = 0$ (N $\\equiv$ 2 mod 4)\n\n"
        "Green cells are the $\\sim N$ new x-columns\n"
        "inserted by polygon $N$. They scatter across\n"
        "the row rather than clustering — the update\n"
        "is compressed (few cells change per step)\n"
        "but not local (those cells are distributed\n"
        "across the whole length of $M_N$)."
    )
    ax.text(
        0.985, 0.86,
        annotation,
        transform=ax.transAxes,
        fontsize=13,
        ha="right",
        va="top",
        color="0.15",
    )

    plt.tight_layout()
    plt.savefig(outpath, dpi=170, bbox_inches="tight")
    plt.close(fig)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    figdir = os.path.normpath(os.path.join(here, "..", "..", "figures"))
    os.makedirs(figdir, exist_ok=True)
    rows, max_len = build_rows(N_MIN, N_MAX, MATCH_TOL)
    outpath = os.path.join(figdir, "counting_increment_map.png")
    plot_increment_map(rows, max_len, outpath)
    print(f"wrote {outpath}")


if __name__ == "__main__":
    main()
