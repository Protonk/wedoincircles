"""
Joint-trace phase-plane figure for fft/DEFICIT-VS-CYCLOTOMIC-MULTIPLICITY.md.

Plots the per-stage trajectory of (iso(j), N log2 N - Psi(j)) for the
radix-2 DIT FFT applied to the cyclic DFT of size N at four sizes
N in {8, 16, 32, 64}.

  - Psi(A) := N log2 N - sum_i H(p_i)  with p_i(j) = |A_ij|^2
    is the row-deficit potential used in the memo. Computed directly
    by simulating radix-2 butterflies on I_N (twiddle phases do not
    affect |.|^2 distributions, so the Psi trajectory matches the
    Walsh-Hadamard trajectory in row-marginal coordinates).

  - iso(j) is the cyclotomic-factor isolation profile defined in
    the memo: cumulative sum of phi(d) over Phi_d that are isolated
    or fully resolved at stage j of the schedule. For radix-2 DIT
    on N = 2^k, the closed-form is
        iso(j) = N (1 - 2^{-j})  for 1 <= j <= k - 1,
        iso(k) = N
    (Phi_1 and Phi_2 co-emerge from the terminal (x^2 - 1) lump).

The figure uses normalized coordinates (iso/N, cleared-Psi/(N log2 N))
so that all four trajectories share the unit-square endpoint (1, 1)
and the doubling-ratio shape of the radix-2 DIT schedule is visible
across N.

Produces:
    figures/deficit_vs_iso_phase_plane.png
"""

import os
from math import log2, sqrt

import numpy as np
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt


def row_entropy(distribution, tolerance=1e-12):
    nonzero = distribution[distribution > tolerance]
    if nonzero.size == 0:
        return 0.0
    return float(-np.sum(nonzero * np.log2(nonzero)))


def total_row_entropy(matrix):
    return sum(
        row_entropy(np.abs(matrix[i]) ** 2) for i in range(matrix.shape[0])
    )


def apply_hadamard_block(matrix, block_start, stride):
    inv_sqrt2 = 1.0 / sqrt(2.0)
    for offset in range(stride):
        upper = matrix[block_start + offset].copy()
        lower = matrix[block_start + offset + stride].copy()
        matrix[block_start + offset] = (upper + lower) * inv_sqrt2
        matrix[block_start + offset + stride] = (upper - lower) * inv_sqrt2


def apply_hadamard_stage(matrix, stage_index):
    n = matrix.shape[0]
    stride = 2 ** stage_index
    block_size = stride * 2
    for block_start in range(0, n, block_size):
        apply_hadamard_block(matrix, block_start, stride)


def psi_trajectory(n):
    """Per-stage Psi(A_j) trajectory across log2(n) butterfly stages on I_n."""
    matrix = np.eye(n, dtype=np.complex128)
    canon = n * log2(n)
    psi_values = [canon - total_row_entropy(matrix)]
    for j in range(int(log2(n))):
        apply_hadamard_stage(matrix, j)
        psi_values.append(canon - total_row_entropy(matrix))
    return psi_values


def iso_trajectory(n):
    """Per-stage iso(j) for radix-2 DIT on cyclic DFT of size N = 2^k."""
    k = int(log2(n))
    iso = [0]
    cumulative = 0
    for j in range(1, k):
        cumulative += n // (2 ** j)
        iso.append(cumulative)
    iso.append(n)
    return iso


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    figdir = os.path.normpath(os.path.join(here, "..", "figures"))
    os.makedirs(figdir, exist_ok=True)

    sizes = [8, 16, 32, 64]
    colors = ["#1f77b4", "#d62728", "#2ca02c", "#9467bd"]
    markers = ["o", "s", "D", "^"]

    fig, ax = plt.subplots(figsize=(7.5, 6.0))

    # uniform-stoichiometry diagonal (y = x)
    ax.plot(
        [0, 1],
        [0, 1],
        linestyle=":",
        linewidth=1.0,
        color="0.55",
        label=r"uniform $y=x$",
        zorder=1,
    )

    for n, color, marker in zip(sizes, colors, markers):
        psi = psi_trajectory(n)
        iso = iso_trajectory(n)
        canon = n * log2(n)

        cleared = [canon - p for p in psi]
        x = [v / n for v in iso]
        y = [c / canon for c in cleared]

        ax.plot(
            x,
            y,
            linewidth=1.8,
            marker=marker,
            markersize=6.5,
            color=color,
            label=f"$N={n}$ ($k={int(log2(n))}$)",
            zorder=3,
        )

        # stage labels for the largest N only
        if n == 64:
            for j, (xi, yi) in enumerate(zip(x, y)):
                if j == 0:
                    continue
                ax.annotate(
                    f"$j={j}$",
                    xy=(xi, yi),
                    xytext=(8, -10),
                    textcoords="offset points",
                    fontsize=8.5,
                    color=color,
                )

    # consistency print: closed-form Psi vs simulated for N=32
    n_check = 32
    psi_sim = psi_trajectory(n_check)
    canon_check = n_check * log2(n_check)
    cleared_sim = [canon_check - p for p in psi_sim]
    print(f"N={n_check}: cleared-Psi per stage = {[round(c, 6) for c in cleared_sim]}")
    print(f"N={n_check}: iso per stage         = {iso_trajectory(n_check)}")

    ax.set_xlim(-0.02, 1.04)
    ax.set_ylim(-0.02, 1.04)
    ax.set_xlabel(r"$\mathrm{iso}(j) / N$  (cyclotomic-factor degree isolated)")
    ax.set_ylabel(
        r"$(N \log_2 N - \Psi(j)) / (N \log_2 N)$  (deficit cleared)"
    )
    ax.set_title(
        "Joint trace: row-deficit cleared vs cyclotomic-factor isolation\n"
        "radix-2 DIT, cyclic DFT, normalized"
    )
    ax.grid(alpha=0.3)
    ax.legend(loc="lower right", framealpha=0.95)
    ax.set_aspect("equal")

    out_path = os.path.join(figdir, "deficit_vs_iso_phase_plane.png")
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
