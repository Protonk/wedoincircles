"""
Toy-angle plot for ROTATION-PERTURBATION.md.

Triangle fixed, square rotated by theta in [0, pi/2]. The figure records
the number of distinct x-positions across all seven vertices.
"""

import math
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


SAMPLES = 100001
TOL = 1e-10
GENERIC_COUNT = 6


def polygon_xs(n, rotation):
    radius = 1 / math.cos(math.pi / n)
    return [
        radius * math.cos((2 * k + 1) * math.pi / n + rotation)
        for k in range(n)
    ]


TRIANGLE_XS = polygon_xs(3, 0.0)


def distinct_count(values, tol=TOL):
    ordered = sorted(values)
    if not ordered:
        return 0

    count = 1
    for left, right in zip(ordered, ordered[1:]):
        if abs(right - left) > tol:
            count += 1
    return count


def sampled_counts():
    thetas = np.linspace(0.0, 0.5 * math.pi, SAMPLES)
    counts = np.empty_like(thetas, dtype=int)

    for idx, theta in enumerate(thetas):
        counts[idx] = distinct_count(TRIANGLE_XS + polygon_xs(4, theta))

    return thetas, counts


def plot(outpath):
    thetas, counts = sampled_counts()
    exceptional = np.where(counts < GENERIC_COUNT)[0]

    expected_thetas = np.array([0.0, 0.25, 0.5])
    observed_thetas = thetas[exceptional] / math.pi
    observed_counts = counts[exceptional]

    if len(exceptional) != 3:
        raise RuntimeError(f"expected 3 exceptional sampled angles, found {len(exceptional)}")
    if not np.allclose(observed_thetas, expected_thetas, atol=1e-12):
        raise RuntimeError(f"unexpected exceptional angles: {observed_thetas!r}")
    if not np.array_equal(observed_counts, np.array([3, 5, 3])):
        raise RuntimeError(f"unexpected exceptional counts: {observed_counts!r}")

    fig, ax = plt.subplots(figsize=(10.2, 4.8))

    ax.hlines(
        GENERIC_COUNT,
        0.0,
        0.5,
        color="#2b6cb0",
        lw=2.4,
    )

    for theta_over_pi in expected_thetas:
        ax.axvline(theta_over_pi, color="0.88", lw=1.0, ls=":")

    ax.scatter(
        observed_thetas,
        observed_counts,
        s=54,
        color="#c53030",
        zorder=4,
    )

    labels = [
        (0.0, 3, r"$\theta=0$, count $3$", (8, 6), "left"),
        (0.25, 5, r"$\theta=\pi/4$, count $5$", (0, 10), "center"),
        (0.5, 3, r"$\theta=\pi/2$, count $3$", (-8, 6), "right"),
    ]
    for x, y, text, offset, align in labels:
        ax.annotate(
            text,
            xy=(x, y),
            xytext=offset,
            textcoords="offset points",
            ha=align,
            va="bottom",
            fontsize=10,
            color="0.22",
        )

    ax.text(
        0.285,
        GENERIC_COUNT + 0.08,
        "generic chamber: 6 distinct x-positions",
        color="#2b6cb0",
        fontsize=10.5,
    )

    ax.set_xlim(-0.01, 0.51)
    ax.set_ylim(2.75, 6.35)
    ax.set_yticks([3, 4, 5, 6])
    ax.set_xticks([0.0, 0.125, 0.25, 0.375, 0.5])
    ax.set_xticklabels(["0", "1/8", "1/4", "3/8", "1/2"])
    ax.set_xlabel(r"$\theta / \pi$")
    ax.set_ylabel("distinct x-positions")
    ax.set_title("Triangle fixed, square rotated: toy chamber count", fontsize=13)
    ax.grid(axis="y", color="0.93", lw=0.7)

    note = (
        "Over 100,001 sampled angles, the count is generically 6 and drops only at "
        r"$\theta = 0, \pi/4, \pi/2$."
    )
    fig.text(0.5, 0.012, note, ha="center", va="bottom", fontsize=10, color="0.28")

    plt.tight_layout(rect=[0, 0.055, 1, 1])
    plt.savefig(outpath, dpi=170, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    figdir = os.path.normpath(os.path.join(here, "..", "..", "figures"))
    os.makedirs(figdir, exist_ok=True)
    out = os.path.join(figdir, "counting_rotation_toy_angles.png")
    plot(out)
    print(f"wrote {out}")
