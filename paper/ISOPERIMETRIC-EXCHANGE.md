# ISOPERIMETRIC-EXCHANGE

The `iso/` register supplies the program with three-register decomposition machinery on the isoperimetric gap and BIND-compatible Fourier-discrepancy methodology. Three sources — Osserman 1979, Fuglede 1989, Beck 1994 — index three currencies (rate, constant, almost-every) on one quantity.

## Operational supply

Beck 1994's Fourier + Poisson + Fejér + second-moment + Borel–Cantelli machinery is the higher-dimensional substitute for continued-fraction Diophantine control on Kronecker sequences. It pairs with Lefèvre–Muller–Tisserand's 1-dim compressed-orbit pseudocode at `memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md` Step 5 as adjacent-register precedent for the K-H-L-A empirical-to-density proxy.

Fuglede 1989 Theorem 1.2 gives the stability bound on nearly-spherical domains: `(1/10)(‖u‖² + ‖∇u‖²) ≤ Δ ≤ (3/5)‖∇u‖²`. The strip H¹ ↔ circumscribed Hurwitz gap identification at `memos/STRIP-H1-HURWITZ-CLOSURE.md` is the adjacent Sobolev/Hurwitz bridge for that stability currency.

Osserman 1979's Bonnesen-strengthening inequality `L² − 4πA ≥ π²(R − r)²` is the geometric-rate sharp instance among the three.

## Direct technical input

Pairwise hypothesis-class non-nesting: convex-Bonnesen, nearly-spherical-Fuglede, and almost-every-Beck do not contain one another. Witnesses at `corners/pairwise_non_inclusion_witnesses.sage` — thin ellipse `a = 2, b = 1/2` (convex but outside Fuglede); small-spike non-convex `k = 5, ε = 0.0575` (Fuglede but outside Bonnesen); categorial Beck argument (almost-every but neither pointwise convex nor nearly-spherical). Each register is sharp on its own currency; no register is uniformly stronger. The same non-nesting structure appears at `fft/FOUR-FRAMEWORK-SYNTHESIS.md`: AFW / Morgenstern / Winograd / Schönhage–Strassen occupy distinct axiom-coordinates in the seven-axiom space, with no source subsuming another. Register-non-interchangeability is a recurring pattern across cross-source synthesis registers, not an iso/-specific fact.

Fuglede stability at small `n`: the bound holds at every `n ≥ 3` for the inscribed regular `n`-gon despite the hypothesis class formally requiring `n ≥ 8`. Numerical verification at `corners/fuglede_ratio_small_n.sage` records 174% margin at `n = 3`; the polygon stability survives the hypothesis-class formal failure as a separate fact.

Citation-precision audit catalogue with four dimensions on file at `iso/THREE-REGISTER-SYNTHESIS.md`: same-author-different-paper (Roth 1954 discrepancy vs Roth 1955 transcendence), same-result-different-constants (Bonnesen 1921 with `π²(R − r)²` vs the 1924 `4πd²` form), same-letter-different-meaning (Fuglede's ambient-dimension `n` vs the program's polygon-vertex-count `n`), same-paper-different-hypothesis-classes (Bonnesen-vs-Osserman scope inside Osserman 1979). The same precision discipline generalizes beyond iso/: `fft/PROVENANCE-AND-TRANSFERABILITY.md` records explicit "should be cited for / should NOT be cited for" boundaries on each FFT-complexity import.

## Enabled and open

Enabled. Register-non-interchangeability is on the page. The discrepancy register has a BIND-audit precedent paired with `rotations/3DT-BRIEF.md`. The currency-by-route map is explicit. The Beck path is audited as content-not-calendar pre-L-W-safe.

Open. Whether the verified inscribed computations and the circumscribed Hurwitz bridge promote to theorem-grade regular-polygon stability statements with effective constants at every `n ≥ 3`. Whether Beck's `(log N)^k φ(log log N)` Borel–Cantelli threshold promotes to pointwise control on `π`. Whether the three currencies admit a unified register at higher resolution, or whether the non-nesting result is structural and unification is precluded.
