import csv
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from counting_utils import non2_table


N_MIN = 5
N_MAX = 40


def plot_non2_entries(table, outpath):
    fig, ax = plt.subplots(figsize=(14, 8))

    xs = [row["position"] for row in table]
    ys = [row["N"] for row in table]
    cs = [row["value"] for row in table]
    ss = [18 + 5 * row["value"] for row in table]

    sc = ax.scatter(xs, ys, c=cs, s=ss, cmap="plasma", edgecolors="black", linewidths=0.35)
    cbar = plt.colorbar(sc, ax=ax)
    cbar.set_label("Multiplicity value")

    ax.set_title("Non-2 entries in M_N (positions and values, N = 5 … 40)", fontsize=13)
    ax.set_xlabel("Position in M_N")
    ax.set_ylabel("N")
    ax.set_xlim(0, max(xs) + 10)
    ax.set_ylim(N_MIN - 1, N_MAX + 1)
    ax.grid(True, color="0.92", lw=0.6)

    plt.tight_layout()
    plt.savefig(outpath, dpi=170, bbox_inches="tight")
    plt.close(fig)


def write_non2_table(table, outpath):
    with open(outpath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["N", "position", "value", "word_length", "normalized_position"],
            delimiter="\t",
        )
        writer.writeheader()
        for row in table:
            writer.writerow(row)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    figdir = os.path.normpath(os.path.join(here, "..", "..", "figures"))
    os.makedirs(figdir, exist_ok=True)

    table = non2_table(N_MIN, N_MAX)

    plot_non2_entries(table, os.path.join(figdir, "counting_non2_entries.png"))
    write_non2_table(table, os.path.join(here, "non2_entries.tsv"))

    print(f"wrote {os.path.join(figdir, 'counting_non2_entries.png')}")
    print(f"wrote {os.path.join(here, 'non2_entries.tsv')}")


if __name__ == "__main__":
    main()
