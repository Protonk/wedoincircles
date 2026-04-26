# POLYGONAL-LEDGER

The `corners/` register supplies the program with explicit closed-form arithmetic for the polygon-circle gap and an algebraic-depth catalogue for cyclotomic data on regular n-gons. Sharp inequalities and asymptotic constants are extracted to symbolic precision; numerical agreement is verified at 200-bit precision.

## Closed-form supply

The Hurwitz Fourier coefficients of the inscribed regular `n`-gon's arc-length parametrization are

```text
c_m^(n) = L_n^2 / (4 pi^2 m^2)   for m ≡ 1 (mod n),
c_m^(n) = 0                      otherwise,
```

with `L_n = 2 n sin(π/n)`. The closed-form Hurwitz gap is `Δ_n = L_n²(1 − (π/n) cot(π/n))` with Archimedean asymptote `4π⁴/(3n²)`. The pseudo-Chebyshev nodes `node(n) = cos(π/n)` are algebraic of degree `φ(2n)/2`. The `τ`-residue `τ(n) = 2cos(2π/n) − round(2cos(2π/n))` is catalogued at `corners/TAU-PORTRAIT.md`. The circumscribed area scale `alpha_n = n tan(π/n)` is the companion outer datum used by `memos/LIOUVILLE-SCALE-TEST.md` and the strip/circumscribed Hurwitz bridge. Numerical agreement with elementary geometry is verified to machine precision in `corners/hurwitz_gap.sage`.

## Sharp concentration

The Hurwitz first-band concentration theorem at `corners/HURWITZ-FIRST-BAND-CONCENTRATION.md` gives the closed paired-band mass

```text
B_j(n) = (L_n^4 / (2 π²)) · j² n² (j² n² + 3) / (j² n² − 1)³,
```

with comparison `B_j(n) ≤ B_1(n)/j²` for every `j ≥ 1`, hence `B_1(n) ≥ (6/π²) Δ_n` uniformly in `n`. The constant `6/π² = 1/ζ(2)` is sharp as `n → ∞`. The dyadic-shell estimate `Σ_{2^r ≤ j < 2^(r+1)} B_j(n) ≤ 2^(-r) B_1(n)` is verified numerically at `corners/hurwitz_shell_masses.sage`. The shell-asymptotic ratio limit is `n`-dependent:

```text
S_r(n) / (2^(-r) B_1(n)) → (n² − 1)³ / (2 n⁴ (n² + 3))
```

as `r → ∞`, approaching `1/2` only in the further limit `n → ∞`.

## Algebraic depth

`cos(π/n)` has degree `φ(2n)/2`; first non-constructible at `n = 7` (Gauss–Wantzel). `τ(n) ∈ ℚ(cos(2π/n))` with Niven zero set exactly `{1, 2, 3, 4, 6}` (the crystallographic restriction); positive bulge at `{7, 8}`; decay `|τ(n)| ~ 4π²/n²` from below. The cyclotomic ladder `K_n = ℚ(cos(2π/n))` with `[K_n : ℚ] = φ(n)/2` is unbounded as `n` varies — the unbounded-ladder side of the closure-mismatch theorem at `memos/NATIVE-F-MINIMAL-DEFINITION.md`. The `K_n` choice is forced by closure rather than aesthetic: `fft/HEIDEMAN-JOHNSON-BURRUS-1985-BRIEF.md` §5 proves the involution decomposition `Q(ζ_n) = K_n ⊕ K_n · 2i sin(2π/n)` under `σ_{−1}`, with `K_n` the unique multiplicatively-closed half. The cyclotomic-ladder fact also carries multiplicative-complexity content via `fft/AUSLANDER-FEIG-WINOGRAD-1984-BRIEF.md` and `fft/WINOGRAD-1978-BRIEF.md`: `μ`-bounds on cyclotomic factors are functions of `φ(n)`. The algebraic-depth catalogue is a complexity-cost catalogue in adjacent currency.

## Enabled and open

Enabled. Hurwitz weight bookkeeping closes uniformly via the dyadic-shell bound. The algebraic-depth catalogue makes the `n = 7` anchor explicit. Numerical verification stops being ad hoc — every closed form has a 200-bit Sage script.

Open. Whether the sharpness constant `6/π²` has tractable higher-order corrections (the `B_1(n)/Δ_n` excess decays as `O(1/n²)`). Whether subpolygon residues extend the catalogue along divisor lattices. Whether the `τ`-residue admits a Fourier reading despite living on `ℤ` rather than on a continuous seam.
