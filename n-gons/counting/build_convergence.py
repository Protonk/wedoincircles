import os
from fractions import Fraction

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mpmath as mp

from counting_utils import (
    c_n_exact,
    f_n_exact,
    golden_convergent,
    multiplicity_word,
)


N_MIN = 5
N_MAX = 50


def log10_of_positive_fraction(f):
    if f <= 0:
        return float("-inf")
    return float(mp.log10(mp.mpf(f.numerator)) - mp.log10(mp.mpf(f.denominator)))


def compute_rows(n_min, n_max):
    phi = (1 + mp.sqrt(5)) / 2
    rows = []
    for N in range(n_min, n_max + 1):
        counts, _ = multiplicity_word(N)
        a = (N - 1) // 2

        c_frac = c_n_exact(counts)
        f_frac = f_n_exact(counts)
        conv_frac = golden_convergent(a - 1) if a >= 1 else Fraction(1)

        d_decimal_frac = abs(c_frac - Fraction(10, 9))
        d_cf_conv_frac = abs(f_frac - conv_frac)

        f_mp = mp.mpf(f_frac.numerator) / mp.mpf(f_frac.denominator)
        d_cf_phi_mp = abs(f_mp - phi)

        rows.append({
            "N": N,
            "a": a,
            "log_d_decimal": log10_of_positive_fraction(d_decimal_frac),
            "log_d_cf_phi": float(mp.log10(d_cf_phi_mp)) if d_cf_phi_mp > 0 else float("-inf"),
            "log_d_cf_conv": log10_of_positive_fraction(d_cf_conv_frac),
        })
    return rows


def plot_dual_convergence(rows, outpath):
    Ns = [r["N"] for r in rows]
    log_d_decimal = [r["log_d_decimal"] for r in rows]
    log_d_cf_phi = [r["log_d_cf_phi"] for r in rows]
    log_d_cf_conv = [r["log_d_cf_conv"] for r in rows]

    log10_phi = float(mp.log10((1 + mp.sqrt(5)) / 2))
    ref_decimal = [-((N - 1) // 2) for N in Ns]
    ref_cf = [-(2 * ((N - 1) // 2) + 1) * log10_phi for N in Ns]

    fig, ax = plt.subplots(figsize=(11, 7))

    ax.plot(Ns, ref_decimal, ":", color="#1f77b4", alpha=0.55,
            label=r"prediction $-a$ (decimal)")
    ax.plot(Ns, ref_cf, ":", color="#d62728", alpha=0.55,
            label=r"prediction $-(2a+1)\log_{10}\varphi$ (CF)")

    ax.plot(Ns, log_d_decimal, "o-", color="#1f77b4",
            label=r"$|C_N - 10/9|$")
    ax.plot(Ns, log_d_cf_phi, "s-", color="#d62728",
            label=r"$|F(M_N) - \varphi|$")
    ax.plot(Ns, log_d_cf_conv, "v-", color="#2ca02c",
            label=r"$|F(M_N) - p_a/q_a|$ (prefix convergent)")

    ax.set_xlabel("N")
    ax.set_ylabel(r"$\log_{10}$ of distance to limit")
    ax.set_title("Decimal vs continued-fraction convergence for $M_N$")
    ax.legend(loc="upper right", fontsize=9)
    ax.grid(True, color="0.92", lw=0.6)

    plt.tight_layout()
    plt.savefig(outpath, dpi=170, bbox_inches="tight")
    plt.close(fig)


def main():
    mp.mp.dps = 100
    here = os.path.dirname(os.path.abspath(__file__))
    figdir = os.path.normpath(os.path.join(here, "..", "..", "figures"))
    os.makedirs(figdir, exist_ok=True)

    rows = compute_rows(N_MIN, N_MAX)
    outpath = os.path.join(figdir, "counting_dual_convergence.png")
    plot_dual_convergence(rows, outpath)
    print(f"wrote {outpath}")


if __name__ == "__main__":
    main()
