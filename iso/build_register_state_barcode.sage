"""
Register-state barcode for iso/THREE-REGISTER-SYNTHESIS.md.

The figure separates "currency isolated" from "program target resolved"
for the three iso/ registers. It mirrors the three-state bookkeeping
used in fft/DEFICIT-VS-CYCLOTOMIC-MULTIPLICITY.md, but the states are
register-level rather than cyclotomic-factor-level.

Produces:
    figures/iso_register_state_barcode.png
"""

import os

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import Patch, Rectangle


UNRESOLVED = "isolated, unresolved"
RESOLVED = "resolved"

STATE_COLORS = {
    UNRESOLVED: "#4c78a8",
    RESOLVED: "#12385b",
}


ROWS = [
    (
        "Geometric /\nBonnesen",
        [
            (RESOLVED, "sharp\nconstant"),
            (UNRESOLVED, "Fejes-Toth\nopen"),
            (RESOLVED, "convex\nn-gons"),
            (UNRESOLVED, "usable;\naudit open"),
        ],
    ),
    (
        "Sobolev /\nHurwitz-Fuglede",
        [
            (RESOLVED, "sharp\nrate"),
            (RESOLVED, "Hurwitz\naudit closed"),
            (RESOLVED, "n >= 8 +\nsmall-n direct"),
            (RESOLVED, "rate target\nresolved"),
        ],
    ),
    (
        "Probabilistic /\nBeck",
        [
            (RESOLVED, "almost-every\nthreshold"),
            (UNRESOLVED, "Schmidt 1960\nopen"),
            (UNRESOLVED, "specific-pi\nbridge open"),
            (UNRESOLVED, "method\nexemplar"),
        ],
    ),
]

COLUMNS = [
    "currency\nisolated",
    "L-W\naudit",
    "bridge /\nhypothesis",
    "program\ntarget",
]


def plot_barcode(outpath):
    fig, ax = plt.subplots(figsize=(10.8, 4.8))

    for y, (row_label, cells) in enumerate(reversed(ROWS)):
        for x, (state, label) in enumerate(cells):
            rect = Rectangle(
                (x, y),
                1.0,
                1.0,
                facecolor=STATE_COLORS[state],
                edgecolor="white",
                linewidth=2.0,
            )
            ax.add_patch(rect)
            ax.text(
                x + 0.5,
                y + 0.5,
                label,
                ha="center",
                va="center",
                fontsize=10,
                color="white",
            )
        ax.text(
            -0.13,
            y + 0.5,
            row_label,
            ha="right",
            va="center",
            fontsize=11,
            color="0.15",
        )

    for x, column in enumerate(COLUMNS):
        ax.text(
            x + 0.5,
            len(ROWS) + 0.14,
            column,
            ha="center",
            va="bottom",
            fontsize=11,
            color="0.15",
        )

    ax.text(
        1.5,
        -0.3,
        "5pi conversion is overhead between isolated registers, not a failure of Sobolev isolation.",
        ha="center",
        va="top",
        fontsize=9.5,
        color="0.25",
    )

    legend = [
        Patch(facecolor=STATE_COLORS[UNRESOLVED], edgecolor="white", label=UNRESOLVED),
        Patch(facecolor=STATE_COLORS[RESOLVED], edgecolor="white", label=RESOLVED),
    ]
    ax.legend(
        handles=legend,
        loc="lower center",
        bbox_to_anchor=(0.5, -0.38),
        ncol=2,
        framealpha=0.95,
    )

    ax.set_xlim(-1.45, len(COLUMNS))
    ax.set_ylim(-0.42, len(ROWS) + 0.55)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("iso register-state barcode: isolated currency vs resolved program use")
    for spine in ax.spines.values():
        spine.set_visible(False)

    fig.subplots_adjust(left=0.2, right=0.98, top=0.86, bottom=0.26)
    fig.savefig(outpath, dpi=170, bbox_inches="tight")
    plt.close(fig)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    figdir = os.path.normpath(os.path.join(here, "..", "figures"))
    os.makedirs(figdir, exist_ok=True)
    out = os.path.join(figdir, "iso_register_state_barcode.png")
    plot_barcode(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
