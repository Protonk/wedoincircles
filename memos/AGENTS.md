# AGENTS

## Recurring gotchas

- If you need a monic integer Chebyshev polynomial, use the scaled form
  $$
  P_n(x)=2T_n(x/2),
  $$
  not raw `T_n`.
- For the Ten Martini memo, the arithmetic parameter is
  $$
  \beta(\alpha)=\limsup \frac{\ln q_{n+1}}{q_n},
  $$
  not $\limsup \ln q_{n+1}/\ln q_n$.
- The crystallographic function `\psi` is additive on prime-power parts. It is not `\varphi/2`.
- In the lattice 3DT formulation, `r_2`, `s_2`, and `r_2+s_2` are unscaled lattice-function values. The actual circle-gap lengths are those quantities divided by `N`.
