# Pseudo-Champernowne Encoding of `M_N`

The decimal encoding `C_N` of the counting-exhaustion word `M_N` (defined in [COUNTING.md](COUNTING.md)), and its behavior as `N` grows.

## Decimal Encoding

Concatenating the entries of `M_N` as decimal digits gives `C_N`: the first entry is the integer part, the rest the mantissa. For `N = 8`, `C_8 = 1.11622222212`. `C_N` is terminating and therefore rational — Champernowne-like in method, but not irrational. Reading the entries instead as partial quotients of a continued fraction is a natural alternative encoding; see [DECIMAL-CF-COMPLEMENTARITY.md](DECIMAL-CF-COMPLEMENTARITY.md) for how the two encodings compare.

## Initial values

The first few `C_N` as decimal strings:

- `C_5  = 1.1226`
- `C_6  = 1.14228`
- `C_7  = 1.114222210`
- `C_8  = 1.11622222212`
- `C_9  = 1.111622222222214`
- `C_10 = 1.11182222224222216`

Exact values at a few larger `N`:

- `C_12 = 1.111110222222222242222222220`
- `C_16 = 1.11111114222222222222222222222622222222222222222228`
- `C_20 = 1.111111111822222222222222222222222222222222222282222222222222222222222222222222236`
- `C_25 = 1.1111111111122222222222222222222222222222222222222222222222222222222222222210222222222222222222222222222222222222222222222222222222246`

## Word length

Number of entries in `M_N` for `N = 3, …, 50`:

```
2, 3, 5, 6, 9, 11, 15, 17, 22, 26, 32, 36, 43, 49, 57, 63, 72, 80,
90, 98, 109, 119, 131, 141, 154, 166, 180, 192, 207, 221, 237, 251,
268, 284, 302, 318, 337, 355, 375, 393, 414, 434, 456, 476, 499, 521,
545, 567.
```

Asymptotic length is `≈ N²/4`. The ratio `length / (N²/4)` climbs from `0.68` at `N = 10` to `0.99` at `N = 400`.

## Decimal length

The digit count of `C_N` after the decimal point, `d_N`, differs from the word length because multi-digit multiplicities like `10`, `12`, `14`, … are concatenated as written. For `N ≤ 6` every multiplicity is single digit and `d_N = length − 1`; from `N = 7` the terminal `2(N−2)` is multi-digit; from `N = 12` the count at `x = −1` is multi-digit too, and `d_N` begins to exceed the word length.

| `N` | `d_N` |
|---:|---:|
| 5  | 4   |
| 6  | 5   |
| 7  | 9   |
| 8  | 11  |
| 9  | 15  |
| 10 | 17  |
| 11 | 22  |
| 12 | 27  |
| 13 | 33  |
| 14 | 37  |
| 15 | 44  |
| 16 | 50  |
| 17 | 58  |
| 18 | 64  |
| 19 | 73  |
| 20 | 81  |
| 21 | 91  |
| 22 | 100 |
| 23 | 111 |
| 24 | 121 |
| 25 | 133 |

## Magnitude of `C_N`

`C_N` converges to `10/9`. Distances to `10/9` computed to 200-digit precision:

- `N = 8`:   `5.1 × 10⁻³`
- `N = 16`:  `3.1 × 10⁻⁸`
- `N = 32`:  `1.9 × 10⁻¹⁵`
- `N = 64`:  `5.1 × 10⁻³¹`
- `N = 128`: `1.5 × 10⁻⁶⁴`

The rate is consistent with the trailing large entry sitting at decimal position `≈ N²/4`. Dropping the final entry gives the same limit.
