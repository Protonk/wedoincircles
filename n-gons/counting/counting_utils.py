from fractions import Fraction

from mpmath import mp


mp.dps = 120
TOL = mp.mpf("1e-40")


def corner_points_upto(max_n):
    points = []
    for n in range(3, max_n + 1):
        radius = 1 / mp.cos(mp.pi / n)
        for k in range(n):
            theta = (2 * k + 1) * mp.pi / n
            x = radius * mp.cos(theta)
            points.append((x, n, k, theta))
    points.sort(key=lambda t: t[0])
    return points


def multiplicity_word(max_n):
    points = corner_points_upto(max_n)
    counts = []
    clusters = []
    curx = None
    current = []

    for item in points:
        x = item[0]
        if curx is None or abs(x - curx) > TOL:
            if current:
                counts.append(len(current))
                clusters.append(current)
            curx = x
            current = [item]
        else:
            current.append(item)

    if current:
        counts.append(len(current))
        clusters.append(current)

    return counts, clusters


def decimal_encoding(counts):
    if not counts:
        return "0"
    return str(counts[0]) + "." + "".join(str(c) for c in counts[1:])


def non2_entries(max_n):
    counts, _ = multiplicity_word(max_n)
    return [(idx + 1, value) for idx, value in enumerate(counts) if value != 2]


def words_over_range(n_min=5, n_max=40):
    return {n: multiplicity_word(n)[0] for n in range(n_min, n_max + 1)}


def non2_table(n_min=5, n_max=40):
    table = []
    for n in range(n_min, n_max + 1):
        counts = multiplicity_word(n)[0]
        for pos, value in enumerate(counts, start=1):
            if value != 2:
                table.append(
                    {
                        "N": n,
                        "position": pos,
                        "value": value,
                        "word_length": len(counts),
                        "normalized_position": pos / len(counts),
                    }
                )
    return table


def digit_length_of_decimal(counts):
    return sum(len(str(c)) for c in counts[1:])


def c_n_exact(counts):
    """C_N as an exact Fraction: integer part counts[0], mantissa from concatenated digits."""
    if not counts:
        return Fraction(0)
    integer_part = Fraction(counts[0])
    mantissa_digits = "".join(str(c) for c in counts[1:])
    if not mantissa_digits:
        return integer_part
    return integer_part + Fraction(int(mantissa_digits), 10 ** len(mantissa_digits))


def f_n_exact(counts):
    """F(M_N) = [counts[0]; counts[1], ..., counts[-1]] as an exact Fraction."""
    if not counts:
        return Fraction(0)
    result = Fraction(counts[-1])
    for c in reversed(counts[:-1]):
        result = Fraction(c) + Fraction(1) / result
    return result


def golden_convergent(depth):
    """Convergent [1; 1, 1, ..., 1] with `depth` partial quotients after the integer 1."""
    if depth < 0:
        return Fraction(1)
    result = Fraction(1)
    for _ in range(depth):
        result = Fraction(1) + Fraction(1) / result
    return result
