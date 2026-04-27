# FP-MATULA-1970

Source-extraction memo on David W. Matula, "A Formalization of
Floating-Point Numeric Base Conversion," *IEEE Transactions on
Computers* Vol. C-19, No. 8 (August 1970), pp. 681–692
([sources/Formalization of Floating-Point Numeric Base Conversion Matula.pdf](sources/Formalization%20of%20Floating-Point%20Numeric%20Base%20Conversion%20Matula.pdf),
12 PDF pages).

**Why this brief exists.** [fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md)'s
gating-debt 1 work and the option-3 discriminator question surfaced
an underdetermination in the program's "abstract FP" framing: the
cocycle `ε(m) = log_β(1+m) − m` is base-specific, and "binades in
infinite-precision arbitrary FP" are not well-defined without
committing to a base and a precision. Matula 1970 supplies the
formalization the program has been waving at — significance spaces
parametrized by `(β, n)`, gap functions as the structural fingerprint,
commensurability as the primary base-relation dichotomy, and
conversion mappings between significance spaces as the natural
primitives. The program inherits Matula's vocabulary and structural
distinctions to sharpen the option-3 discriminator (what
generalization of "floating-point seam-crossing" captures the FFT
canon's strategy adjustments). Citation form: standard IEEE TC.

**What was read.** The full 12-page paper, including Section II
(floating-point number systems and the significance space), Section
III (conversion mappings, base conversion theorem), Section IV
(compound conversions and invariant points), and Section V
(concluding remarks on hardware/software implications). The
auxiliary references [1]–[4] cited by Matula (his own earlier work
on significance spaces) are not independently audited.

**Confidence level.** High on the brief's direct extractions —
each is a numbered theorem, definition, or formula in the paper.
Medium on the program-side mappings: the connection to the program's
cocycle / regime-boundary-crossing framing is the brief's
inferential contribution, not Matula's framing.

**Trust boundary up front.** Matula 1970 is a 1970 IEEE TC paper on
floating-point base-conversion mathematics, read here for
*vocabulary, formalization, and structural distinctions*, not for
content transferred to the FFT impossibility theorem. The
mathematical content of our paper does not depend on Matula proving
anything about FFTs; it depends on Matula having *formalized* and
*named* the (base, precision, commensurability, conversion)
structure the program needs to express its claims at the right
level of generality.

---

## 1. The significance space `S^β_n` (§II, p. 682)

The abstract floating-point object, defined precisely:

> *"For the integers `β ≥ 2`, called the **base**, and `n ≥ 1`,
> called the **significance** (or **precision**), let the
> significance space `S^β_n` be the following set of real numbers:
> `S^β_n = {b : b = kβ^j for some integers k, j where |k| < β^n}`."*
> (p. 682)

Notation discipline (preserved here): Greek letters `α, β, δ` for
bases; English letters `a, b, c, d` for floating-point numbers;
integers `i, j, k, l, m, n, p, q`; reals `x, y, z`.

**Key features.**

- **Infinite extent.** No bound on the exponent `j`. `S^β_n` is an
  *infinite* set — the abstract model does not carry underflow or
  overflow. This is the feature the program's "abstract FP" wants:
  precision and base are explicit; exponent range is not part of
  the structural description.
- **Non-uniqueness of representation.** A given `b ∈ S^β_n` may
  have multiple `(k, j)` representations (normalized vs
  unnormalized). For the brief's purposes only set membership is
  load-bearing.
- **Density structure.** Within an interval `[β^j, β^{j+1})`,
  there are exactly `(β−1)·β^{n−1}` distinct members. As `n →
  n+1`, the new significance space contains all members of the
  old plus `β−1` new members uniformly spaced between every
  neighboring pair.

**For the program.** This is what *abstract FP* means when made
precise. The program had been operating implicitly with `β = 2`
and an unspecified precision `n`; Matula's formalism makes the
family structure `{S^β_n}_{β, n}` explicit and exposes the cocycle's
base-dependence. Changing `β` changes the cocycle.

## 2. The density formula and the gap function (§II, eqs. 1, 6, 7)

**Density ratio (Theorem 1, p. 683).** For two significance spaces
the limiting ratio of memberships over the whole real line is:

```text
|S^β_n / S^δ_m| = ((β − 1) · β^{n−1}) / ((δ − 1) · δ^{m−1}) · log_β δ.
```

Matula's punchline:

> *"In the folklore on conversion there is an often quoted notion
> that a decimal digit is equivalent to `log_2 10 = 3.32...` bits.
> ... However, ... `|S^{10}_3 / S^2_{10}| = 0.529...`, so that
> there are actually only 53 percent as many real numbers
> representable with three significant decimal digits as there are
> real numbers representable with ten significant bits."* (p. 683)

The folk "1 decimal digit ≈ 3.32 bits" rule overstates the density
of decimal vs binary by ignoring the geometric `β^{n−1}/δ^{m−1}`
factor and the spacing variation Matula's gap function exposes.

**The gap function `F^β_n`.** Matula's structural fingerprint for
an FP system:

> *"The **gap** `F^β_n(x)` in `S^β_n` at `x ≠ 0` is given by
> `F(x) = (min{b : b > x, b ∈ S^β_n} − max{b : b ≤ x, b ∈ S^β_n}) /
> x` for `x > 0`."* (p. 684, eq. 6)

For positive `a ∈ S^β_n` with successor `a'`, this reduces to
`F^β_n(a) = (a' − a)/a` — the relative spacing to the next
representable number. The gap function is *log-periodic* under
`F(βx) = F(x)`, so on a log-log scale it is sawtooth with period
`log β`.

**Bounds (Theorem 2, p. 684).** Over nonzero members of `S^β_n`:

```text
1/(β^n − 1) ≤ F^β_n(b) ≤ 1/(β^{n−1} − 1).
```

Larger bases give larger variation (bigger sawtooth teeth). For
example, four-digit hexadecimal vs four-digit decimal: `|S^4_{16}
/ S^4_{10}| ≈ 5.66` overall, but on the local interval
`[0.0625, 0.1000]` there are *more* four-digit decimal numbers
than four-digit hexadecimal — a fact no "equivalent digits"
formula can show.

Matula's discipline:

> *"the gap function presents a more complete picture of the
> structure of a floating-point number system than any 'equivalent
> digit' notion, and simplified formulas ... must be used with
> extreme caution in any comparison of differently based
> floating-point number systems."* (p. 684)

**For the program.** The gap function is the right structural
object for talking about FP-system "shape." The program's cocycle
`ε_β(m) = log_β(1+m) − m` is the displacement between mantissa
coordinate and log-binade coordinate within a single binade — it
is *one slice* of `F^β_n`'s log-periodic structure, specifically
at the binade-transition locus. The full gap function carries more
(within-binade spacing, base-dependent variation in tooth size);
the cocycle is the slice that fingerprints the binade transition
specifically.

## 3. Commensurability of bases (§III, p. 685)

The primary structural dichotomy:

> *"Let `β ≥ 2` be a **root-free integer**, i.e., has no integral
> `i`th root for any `i`. Then the numbers `β, β^2, β^3, ...` form
> a **commensurable family of bases** termed the `β`-family of
> bases. Two or more bases belonging to the same commensurable
> family of bases are **commensurable bases**. Two bases which do
> not belong to a common commensurable family are termed
> **incommensurable bases**."* (p. 685)

**Equivalent characterizations.**

- *Lemma 1*: `β` and `δ` are commensurable iff `β^i = δ^j` for
  some nonzero integers `i, j`.
- *Corollary 2*: `β` and `δ` are commensurable iff `log_δ β` is
  rational.

**Examples.** 2, 4, 8, 16, 32 belong to the binary family
(root-free integer 2). 3, 9, 27, 81 belong to the ternary family.
6 generates its own family (`6 = 2 · 3` is not a power of any
other integer). Base 10 is incommensurable with any binary-family
member; it generates its own family with 100, 1000, 10000.

**Structural consequence.** Gap functions `F^β_n` and `F^δ_m`
plotted on a log-log scale share a common period when `β, δ` are
commensurable; otherwise the periods are incommensurable and the
two gap structures cannot be aligned. (Matula's Fig. 4 contrasts
hexadecimal/octal — commensurable, period `12` on log-binary
scale — with Fig. 2's binary/decimal — incommensurable, no shared
period.)

**For the program.** This is the structural distinction the
option-3 discriminator wants. Two FP systems with commensurable
bases share *infinite* common structure (they fit together at
every scale); with incommensurable bases, the common structure is
*finite* (Theorem 6 below). Whether an FFT-style algorithm engages
the cocycle non-trivially depends on whether its primitives operate
within the same commensurability class or cross between classes.
The Schönhage–Strassen verdict's "floating-point seam-crossing at
primitive-operation level" generalizes naturally to "engagement
across a commensurability boundary."

## 4. Conversion mappings (§III, eqs. 9–10; Theorem 3)

**Truncation `T^β_n` and rounding `R^β_n`** are the standard
primitives:

```text
T^β_n(x) = max{b : b ≤ x, b ∈ S^β_n}                 (for x > 0)
R^β_n(x) = min{b : (b + b')/2 > x, b ∈ S^β_n}       (for x > 0; b' is the successor of b; midpoint rounds up to b' per Matula's convention)
```

Both are *weakly order-preserving* (`x ≤ y ⟹ M(x) ≤ M(y)`) and
identities on `S^β_n`. *Strongly order-preserving* requires
one-to-oneness, which no conversion into a discrete `S^β_n` can
have on the full reals.

**Base conversion theorem (Theorem 3, p. 686).** For incommensurable
bases `β, δ`, the truncation (or rounding) conversion `T^δ_m`
restricted to `S^β_n → S^δ_m`:

> *"1) is **one-to-one** if and only if `δ^{m−1} > β^n − 1`;
> 2) is **onto** if and only if `β^n − 1 > δ^m − 1`."* (p. 686)

**No FP conversion can be both one-to-one and onto** between
incommensurable systems. To assure one-to-one, sacrifice a digit
in the target; to assure onto, sacrifice a digit in the initial
system. The decimal-binary specialization:

```text
n bits > 3.32m + 1     ⟹   one-to-one (and strongly order-preserving)
n bits < 3.32m − 3.32  ⟹   onto.
```

Conversions between FP systems of nearly equal density are
*neither* one-to-one nor onto (Matula's Fig. 6 lattice diagram).

**For the program.** The conversion-mapping formalism gives precise
vocabulary for the FFT canon's "strategy adjustments." When a canon
paper changes its model — Schönhage–Strassen from `ℝ` to a Fermat
ring; Morgenstern from unbounded to bounded coefficients;
Winograd to rational equivalence; AFW to cyclotomic
decomposition — the analog is a conversion between `S^β_n`-like
structures. The dichotomy *one-to-one vs onto, never both* mirrors
the canon's structural trade-offs at each strategy adjustment:
the algorithm gains some property (cheaper representation, sharper
bound) at the cost of losing another (full coverage, exact
equality).

## 5. Compound conversions and invariant points (§IV)

**Compound conversion `Q`.** A composition of `k` rounding/truncation
conversions through a sequence of significance spaces `S^β1_n1, ...,
S^βk_nk`. Compound truncation conversions are *contractions* (toward
zero); compound rounding conversions need not be.

**Theorem 4 (invariant set of compound truncation, p. 687).**

> *"If `Q` is a `k`-fold compound truncation conversion through
> `S^β1_n1, ..., S^βk_nk`, then `f(Q) = ⋂_i S^βi_ni`."* (p. 687)

The invariant points of a compound truncation conversion are
*exactly* the points common to all significance spaces traversed.
This is a sharp characterization — no looser, no tighter.

**Theorem 6 (intersection of incommensurable significance spaces,
p. 688).**

> *"If `β` and `δ` are incommensurable, then `S^β_n ∩ S^δ_m` has
> no more than `2(β^n − 1)(δ^m − 1) + 1` members."* (p. 688)

The intersection is *finite*. Matula's binary-decimal worked
example: the smallest positive member of `S^2_{24} ∩ S^{10}_7`
is `2^{−10} ≈ 0.0009765625`. Twenty-four-bit binary and
seven-decimal-digit FP, both describing enormous numbers of
representable values, share only finitely many — and the smallest
of these is well above any practical underflow threshold.

**Consequence (compound truncation between incommensurable bases).**
For `Q` a compound truncation through at least two incommensurable
bases, `Q^i ≠ Q^{i−1}` for all `i`, and `lim Q^{(i)}(x) = 0` for
any positive `x` smaller than the minimum positive intersection
member. Iterated truncation conversion of a "constant datum"
between incommensurable bases drifts the value toward zero. This
is the BCD-on-binary-machine pathology Matula warns against.

**Theorem 7 (In-and-Out Conversion Theorem, p. 689).** For
incommensurable `β, δ`:

> *"1) `R^β_n R^δ_m` is the identity on `S^β_n` iff
> `δ^{m−1} > β^n`. 2) `R^β_n T^δ_m` is the identity on `S^β_n`
> iff `δ^{m−1} ≥ 2β^n − 1`."* (paraphrased from p. 689)

With sufficient intermediate precision, round-trip rounding
through an incommensurable intermediate space *regenerates the
initial datum*. The information is recoverable if the intermediate
is fat enough.

**Theorem 8 (Iterated Conversion Theorem, p. 689).** For
`Q = R^δ_m R^β_n` with `m, n ≥ 2`: `QQQ = QQ`. Iterated rounding
stabilizes after at most three applications — a stable pair, not
unbounded drift.

**For the program.** The compound-conversion theory gives precise
tools for *what happens when an FFT-style algorithm passes data
through multiple model layers*. Compound truncation through
incommensurable bases is what would happen if a smarter-FFT method
tried to amortize cost by relocating across multiple
representations; Theorems 4 + 6 say the only stable result is the
finite intersection — no free lunch for representation-relocation
strategies. Theorem 7 (In-and-Out) gives precedent for
"round-trip recovery" arguments under sufficient intermediate
precision; Theorem 8 (Iterated) gives precedent for "stable-pair"
arguments. Both are proof-shape patterns the program may invoke
when the formalization of `δ`'s algebra advances.

---

## What Matula states without our independent check

- The auxiliary references [1]–[4] (Matula's earlier work on
  significance spaces and the `"equivalent digit"` formula) are
  not independently audited; the brief reports them as Matula's
  foundation.
- The PL/I language specification claims about mixed-base
  arithmetic are background context, not load-bearing.
- The 1970-era hardware/software design recommendations in
  Section V (computer-network considerations, BCD tape updating,
  format-standardization advice) are applied content not extracted
  here.
- Urabe [7]'s alternative parity-dependent rounding convention
  for midpoints is mentioned but not adopted; the brief reports
  Matula's choice.

The program's use of Matula 1970 is at the formalization-and-
vocabulary level; none of the unchecked content is load-bearing.

---

## What we infer for the program

The Matula-to-FFT mapping is the brief's contribution; Matula did
not write it.

| Program concept | Matula concept | Status |
|---|---|---|
| Abstract FP | Family `{S^β_n}_{β, n}` of significance spaces | Inherited as formalism |
| Concrete FP system | `S^β_n` for fixed `(β, n)` | Inherited |
| Binade transition | Period of log-periodic structure of `F^β_n`, base-specific | Inherited; the program had been base-implicit |
| Cocycle `ε_β(m) = log_β(1+m) − m` | Slice of `F^β_n` at the mantissa coordinate; base-parametrized | Sharpened: the cocycle is one realization in a family |
| Regime-boundary crossing | Transition between `S^β_n` and `S^δ_m`; commensurability is the natural dichotomy | New: commensurability is the discriminator option-3 wants |
| FFT-style strategy adjustment | Change of `(β, n, conversion mode)` parameters | New: precise vocabulary |
| Round-trip recovery | In-and-Out Conversion Theorem (Theorem 7) | New: proof-shape precedent |
| Stable-pair behavior | Iterated Conversion Theorem (Theorem 8) | New: proof-shape precedent |
| Representation-relocation rebuttal | Compound-truncation invariant set = intersection (Theorem 4); incommensurable intersection finite (Theorem 6) | New: structural rebuttal of "amortize across representations" |
| Folk-rule overclaim | "1 decimal digit ≈ 3.32 bits" (Matula refutes via density formula) | Cautionary precedent: don't paper over structure with simplified formulas |

Matula 1970 transfers to the FFT impossibility theorem at four
levels:

1. **Vocabulary**: "significance space," "gap function,"
   "commensurable / incommensurable bases," "compound conversion,"
   "invariant point" — Matula's. The program adopts this naming
   for talking about what *abstract FP* actually is.
2. **Typing**: FP is a *family* `{S^β_n}` parametrized by
   `(base, precision)`, not a single object. The cocycle is a
   slice of a base-parametrized gap function, not a base-free
   invariant. The program's prior framing was base-implicit;
   Matula's typing makes it base-explicit.
3. **Structural distinctions**: commensurable vs incommensurable
   as the primary FP-relation dichotomy; compound truncation =
   contraction; compound rounding = stable-pair via In-and-Out
   theorem. These are structural facts the program inherits as
   the discriminator question's natural vocabulary.
4. **Methodological discipline**: the gap function carries more
   structure than any "equivalent digit" formula; conversions
   between FP systems can be one-to-one *or* onto but never both.
   Don't paper over structural distinctions with simplified
   formulas.

---

## Trust Boundary

### This brief should be cited for

- the Matula formalization of `S^β_n`, `F^β_n`, `T^β_n`, `R^β_n`
  as defined here;
- the density formula (Theorem 1) and the refutation of the
  "log_β δ digits" folk rule;
- commensurability as the primary base-relation dichotomy
  (Lemma 1 / Corollary 2);
- the base conversion theorem (Theorem 3) and its decimal-binary
  specialization;
- compound-conversion invariant-set characterizations
  (Theorems 4 and 6);
- the In-and-Out (Theorem 7) and Iterated Conversion (Theorem 8)
  theorems as proof-shape precedents;
- the program-side mapping table at §"What we infer for the
  program" above (each row is a defensible analogy or vocabulary
  import, not a transferred theorem).

### This brief should NOT be cited for

- any FFT-impossibility content — Matula contains none;
- any computational-complexity content — Matula is about
  base-conversion mathematics, not complexity;
- the claim that Matula's compound-conversion theorems transfer
  *as theorems* to FFT-style algorithm composition — they
  transfer as *vocabulary, formalization, and proof-shape
  precedents*, not as proof material;
- any specific claim about how a particular FFT-style algorithm
  interacts with `S^β_n` — that is the program's burden to
  construct;
- the 1970-era hardware/software design recommendations in
  Section V — applied content, not extracted here;
- the Urabe alternative rounding convention — flagged but not
  adopted.

### Provenance tag for the program

**Formalization-and-vocabulary anchor for FP-side claims.** Matula
1970 supplies the significance-space formalism, the gap function,
the commensurability dichotomy, and the conversion-mapping
vocabulary. None is a content transfer to the FFT impossibility
theorem; all are language and structural distinction. Cited at
[fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md) (when the prose pass
earns it, sharpening the option-3 discriminator's "regime boundary
crossing" toward "commensurability-class crossing"),
[paper/IMPOSSIBILITY-OUTLINE.md](paper/IMPOSSIBILITY-OUTLINE.md)
§1 and §3 (when the floating-point seam-crossing language is
upgraded to commensurability vocabulary), and (potentially)
[paper/FIRST-PROOF.md](paper/FIRST-PROOF.md) Setup (when the cost /
conversion framework's `(β, n)` parameter dependence is made
explicit).

---

## Closing Sentence

Matula 1970 supplies the formalization the program has been
waving at — abstract FP as the family `{S^β_n}` of significance
spaces, the gap function as the structural fingerprint,
commensurability as the natural base-relation dichotomy, conversion
mappings and their compound behavior — and gives the program
precise vocabulary for the option-3 discriminator question, where
the cocycle becomes one slice of a base-parametrized gap structure
rather than a base-free invariant. The mapping to the FFT canon's
strategy adjustments is the brief's inferential contribution;
Matula did not write it. The brief is formalization-and-vocabulary
import, not proof material.
