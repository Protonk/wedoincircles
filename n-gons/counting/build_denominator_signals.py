"""
Denominator-indexed contribution signals for the counting word M_N.

This figure reorganizes the six-field decomposition of COUNTING.md
as per-polygon contributions on the common denominator axis n.
"""

import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


N_MIN = 3
N_MAX = 30
NS = tuple(range(N_MIN, N_MAX + 1))


def leading_one(n):
    return 1 if n % 2 == 1 else 0


def x_minus_one(n):
    return 2 if n % 2 == 0 else 0


def x_zero(n):
    return 2 if (n >= 6 and n % 4 == 2) else 0


def left_field(n):
    if n % 2 == 1:
        return (n - 1) // 4
    if n % 4 == 0:
        return (n - 4) // 4
    return (n - 6) // 4


def right_field(n):
    if n % 2 == 1:
        return (n - 3) // 4
    if n % 4 == 0:
        return (n - 4) // 4
    return (n - 6) // 4


def x_plus_one(_n):
    return 2


LANES = (
    ("leading 1", leading_one, "1 if n odd else 0", "#2f2f2f"),
    ("x = -1", x_minus_one, "2 if n even else 0", "#2b6cb0"),
    ("L(n)", left_field, "left 2-field growth", "#168e4f"),
    ("x = 0", x_zero, "2 if n ≡ 2 mod 4 else 0", "#8e44ad"),
    ("R(n)", right_field, "right 2-field growth", "#f4a261"),
    ("x = +1", x_plus_one, "2 for every n", "#d1495b"),
)


def draw_lane(ax, label, fn, note, color, is_last):
    values = [fn(n) for n in NS]
    ymax = max(values)
    top = max(2.5, ymax + 0.8)

    for n, value in zip(NS, values):
        if value > 0:
            ax.vlines(n, 0, value, color=color, lw=1.8, zorder=2)
            ax.plot(
                [n],
                [value],
                marker="o",
                ms=4.6,
                color=color,
                markeredgecolor="white",
                markeredgewidth=0.4,
                zorder=3,
            )

    ax.set_xlim(N_MIN - 0.5, N_MAX + 0.5)
    ax.set_ylim(0, top)
    ax.set_ylabel(label, rotation=0, ha="right", va="center", labelpad=28, color=color)
    ax.text(
        0.995,
        0.82,
        note,
        transform=ax.transAxes,
        ha="right",
        va="top",
        fontsize=8.5,
        color=color,
    )

    if ymax <= 2:
        ax.set_yticks([0, 1, 2] if ymax >= 1 else [0])
    else:
        step = 2 if ymax >= 8 else 1
        ax.set_yticks(list(range(0, int(top), step)))

    ax.grid(True, axis="y", color="0.9", lw=0.6)
    ax.axhline(0, color="0.2", lw=0.8)

    if is_last:
        ax.set_xlabel("n")
        ax.set_xticks(range(N_MIN, N_MAX + 1, 2))
    else:
        ax.set_xticks(range(N_MIN, N_MAX + 1, 2))
        ax.set_xticklabels([])


def plot(outpath):
    fig, axes = plt.subplots(len(LANES), 1, figsize=(12.5, 10.5), sharex=True)

    for ax, (label, fn, note, color), is_last in zip(axes, LANES, [False] * (len(LANES) - 1) + [True]):
        draw_lane(ax, label, fn, note, color, is_last)

    fig.suptitle(
        "Counting denominator signals | per-polygon contributions on the n-axis",
        fontsize=14,
        y=0.995,
    )
    fig.text(
        0.5,
        0.972,
        "The six-field decomposition of M_N, read one denominator at a time",
        ha="center",
        va="top",
        fontsize=10,
        color="0.35",
    )

    plt.tight_layout(rect=[0, 0, 1, 0.965])
    plt.savefig(outpath, dpi=170, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    figdir = os.path.normpath(os.path.join(here, "..", "..", "figures"))
    os.makedirs(figdir, exist_ok=True)
    out = os.path.join(figdir, "counting_denominator_signals.png")
    plot(out)
    print(f"wrote {out}")
