# Bidder and Son: Two Approaches to Mental Logarithms

A method note : a 19th-century mental-arithmetic record of two distinct procedures for computing log₁₀(n) for arbitrary integers, including large primes. Useful here as a historical hint about the lattice ↔ multiplicative-structure interface and where each side of that interface stops being convenient.

Source: W. Pole, F.R.S., "Mental Calculation. A Reminiscence of
the late Mr. G. P. Bidder, Past-President." Paper No. 2486,
Institution of Civil Engineers. Published posthumously from a
memorandum prepared during Bidder's lifetime with his approval.

Contextual supplement: George Parker Bidder's earlier 1856
address, "On Mental Calculation." That address does not present
the later seven- or eight-place logarithm procedures in the same
form, but it does give Bidder's own account of what makes
mental calculation hard and what a labour-saving method is
supposed to achieve.


## The problem

Compute log₁₀(n) to seven or eight decimal places, mentally,
for any positive integer n — including large primes where no
factorization shortcut is available.


## Earlier frame from Bidder's own address (1856)

The 1856 address adds one important piece of context to Pole's
later reminiscence: Bidder already described the limiting factor
in mental calculation as **registration** — the ability to hold a
string of exact intermediate results in mind without loss or
misplacement.

His formulation is worth keeping in view:

- reasoning and execution are not the main bottleneck;
- registration is;
- and if his powers of registration matched his powers of
  reasoning, he says he could compile a large table of logarithms
  in very short time.

That matters here because the father/son contrast in the
logarithm memo turns out not to be only a contrast of tricks. It
is also a contrast of how the burden of registration is managed.

The 1856 address goes further. The registration constraint is not
just a diagnosis; Bidder shows it dictating the structural shape of
mental algorithms. Three specific consequences:

**Mental multiplication runs left-to-right, not right-to-left.**
Bidder writes:

> On paper when you multiply any number of figures, you begin
> with the units' places and proceed successively to the left, and
> then you add them up. That process is impracticable in the
> mind … in mental arithmetic you begin at the left hand
> extremity, and you conclude at the unit, allowing only one fact
> to be impressed on the mind at a time.

The running total carries continuous magnitude meaning at every
step — one quantity to register, refined downward as more digits
enter. Right-to-left would force registration of partial column-sums
whose meaning isn't fixed until the final addition. So left-to-right is
registration-driven, not stylistic. Structurally this is the coarse-first /
refine-later split (see `memos/LANDFALL-EXPORT.md` on Day's
decoupling): fix the magnitude first, refine downward. Bidder
arrived at this discipline a century before Mitchell's pseudo-log
observation made the same shape a hardware concern.

**Deliberate catalog enrichment.** Bidder memorized 68
multiplication facts (sufficient for 3-figure × 3-figure work) versus
the standard 72-fact 12-table — a deliberate trade chosen because
more memorized facts mean fewer operations to register. Beyond
multiplication, the address records pre-computed unit-conversion
catalogs (seconds in a year, barleycorns in a mile, etc.) that turn
long compound conversions into single multiplications. The prime-
logs catalog the father later used for log computation is one
instance of the same enrichment strategy applied across many
domains.

**Honest scope bound.** "The limits within which [mental
arithmetic] may be usefully and properly applied, should be
restricted to multiplying 3 figures by 3 figures." Past that, even
Bidder's own technique struggles.


## The substrate, in computational terms

Translating Bidder's self-description into the vocabulary of later
computing: the substrate is a **strictly sequential,
memory-bounded machine** on which reasoning is abundant and
working-memory capacity is scarce. Peak working memory is the
binding constraint, not total operation count. Memorized facts —
prime logs, multiplication tables, unit-conversion constants —
serve as long-term storage: effectively free at run-time but
pre-paid in advance.

On such a substrate, the optimal algorithm is the one that
minimizes peak memory, not the one that minimizes operations.
Bidder states this explicitly as a design rule: his procedures
"might appear prolix, complicated, and inexpeditious" because
the extra operations buy memory relief. The same multiplication
algorithm run on paper (no memory pressure) runs right-to-left;
run mentally, it runs left-to-right. Algorithmic shape is
substrate-relative.

What Bidder articulates, without the vocabulary, is the
first-principles design rule for space-bounded sequential
computation: on a memory-bounded substrate, trade operations
for memory relief. The same rule underlies register-pressure-
aware compilation, streaming algorithms over data too large to
fit in memory, and complexity classes like LOGSPACE. Bidder set
it down in 1856 in a mental-arithmetic register; it generalizes
across substrates.


## The father: G. P. Bidder (1806–1878)

### Stored constants

The logarithms of nearly all primes under 100, and a few above,
apparently all computed mentally and, by his own account, not
written down or looked up in tables for many years.
Additionally, the following correction table:

    log(1.01)    = 0.0043214
    log(1.001)   = 0.00043407
    log(1.0001)  = 0.0000434
    log(1.00001) = 0.0000043

### Method for composite numbers

Factor the target into known primes and sum their logarithms.
The factorization is performed by direct perception — Bidder
could see instantly that 17,861 = 337 × 53, or that
1,659 = 79 × 7 × 3. He described this as natural instinct.

### Method for primes and difficult numbers

Find a nearby composite that factors into known primes,
differing from the target by a small residual. Correct for the
residual using the stored correction table and simple proportion.

The residual should be less than 1/1000 of the number. If no
nearby composite is close enough, multiply the target by a small
known factor to produce one.

### Worked example: log(877)

877 is prime and does not have a convenient neighbor. Bidder
multiplies by 13:

    877 × 13 = 11401 = (600 × 19) + 1

Now the problem decomposes:

    log(600)     = 2.7781512    (known factorization)
    log(19)      = 1.2787536    (memorized)
    correction   = 0.0000381    (for the +1, via proportion)
    ─────────────────────────
    log(11401)   = 4.0569429

    subtract log(13) = 1.1139433

    log(877)     = 2.9429996

The correction for +1 is computed as 0.00043428 / 11.4,
using the log(1.001) entry scaled by proportion.

### Worked example: log(369353)

    369353 = (9 × 41000) + 369 − 16

Bidder first adds a correction for 369/369000 (approximately
1/1000), then subtracts a correction for 16. The composition of
two corrections demonstrates flexibility in choosing the
approach path.

### Character of the method

Each problem is a fresh navigation. The solver looks at the
target, perceives a nearby landmark — a factorable composite —
and walks to it. The art is in choosing which landmark gives
the cleanest path: which helper multiplier, which nearby
composite, which way to split the residual.

The method is powerful when good landmarks exist. It rewards
deep familiarity with the multiplicative structure of the integers
and an intuitive sense for which numbers factor cleanly.


## The son: G. P. Bidder Jr. (1836–1896)

### Stored constants

The logarithms of four primes — 2, 3, 7, and 11 — and the
modulus 0.4343 (= log₁₀ e). Additionally, the logarithms of the
multi-scale correction factors:

    log(1.1)     (known)
    log(1.01)    (known)
    log(1.001)   (known)
    log(1.0001)  (known)
    log(1.00001) (known)

### Method for small numbers

Find m + n where m is a multiple of {2, 3, 7, 11} and n is
small. Then:

    log₁₀(m + n) = log₁₀(m) + log₁₀(1 + n/m)

    log₁₀(1 + n/m) = 0.4343 × [n/m − ½(n/m)² + ⅓(n/m)³ − ...]

A few terms of the series suffice when n/m is small.

### Method for large numbers

Decompose the target as a multi-scale product:

    n = (small factorable core) × (1.001)^a × (1.0001)^b × (1.00001)^c

Each factor accounts for one decimal scale of precision. The
exponent at each scale is determined by how much of the target
remains unexplained by the coarser scales.

The logarithm is then a weighted sum:

    log(n) = log(core) + a·log(1.001) + b·log(1.0001) + c·log(1.00001)

All terms are products of a small integer (the exponent) and a
memorized constant.

### Worked example: log(724871)

    724871 = 72 × (1.001)⁶ × (1.0001)⁷ × (1.00001)^4.5

The logarithm is the sum:

    log(72) + 6·log(1.001) + 7·log(1.0001) + 4.5·log(1.00001)

Result: 5.860261 (six places).

### Character of the method

The son's note gives two procedures: one for numbers not very
large, using a series expansion around a nearby multiple of
2, 3, 7, and 11, and another for very large numbers, using a
multi-scale product decomposition into powers of 1.001, 1.0001,
and 1.00001. In both cases the answer is assembled from a small
stock of memorized constants rather than from opportunistic
factor spotting.

This is reinforced by the son's own framing in Pole's paper:
the desideratum is to relieve the mind, as far as possible, from
the burden of performing and registering long calculations.


## Comparison

Both methods decompose a multiplicative problem into additive
steps via the logarithm identity log(a × b) = log(a) + log(b).
Both rely on memorized constants. Both navigate from known
territory to an unknown target.

They differ in how they navigate.

### What is decomposed

The father decomposes the *target* into factors. The factors
are classical primes, or products of classical primes, specific
to the number at hand.

The son decomposes the *space* into scales. The scales are
fixed — they do not depend on the target. The target is
located within the pre-existing grid.

### The role of the residual

For the father, the residual is a local correction applied once,
at the end. It bridges the gap between the nearest factorable
composite and the target. The entire method is organized to
make this residual as small as possible.

For the son, the residual is distributed across all scales. There
is no single correction step. Each scale absorbs its portion of
the discrepancy, and the sum of all contributions constitutes
the answer.

### Dependence on the target's structure

The father's method is sensitive to the target. A number near
a highly factorable composite is easy. A number in a sparse
region of the multiplicative landscape is hard and may require
an indirect approach (the helper multiplier trick).

The son's note is less dependent on spotting a nearby highly
factorable landmark. Its two procedures are organized around
stored constants and controlled expansions instead.

### What must be memorized

The father memorizes many logarithms — nearly all primes
under 100. The method draws on a large library of known
landmarks.

The son memorizes few logarithms — four primes and a handful
of correction constants. The method draws on a small set of
universal reference points.

### Where the difficulty lies

For the father, the difficulty is perception: seeing the factors,
choosing the path, selecting the helper multiplier. The
computation at each step is straightforward (addition of known
values, simple proportion). The challenge is strategic.

For the son, the difficulty is registration: holding a running
total across several scales while computing each contribution.
There is no strategic choice — the procedure is fixed. The
challenge is bookkeeping. This is not just our gloss; it matches
the son's explicit account of what the method is for.

## Algebraic continuity: the binomial-expansion genealogy

The 1856 address records the father working out the binomial
expansion from scratch in service of mental compound-interest
computation. He set up the picking-up-stones puzzle to derive
∑(1..n) = n(n+1)/2, then iterated to derive successive sums of
sums, eventually arriving at

    P(1+r)^n = P {1 + n·r
                  + n(n−1)/2! · r²
                  + n(n−1)(n−2)/3! · r³
                  + …}

and explicitly noted that this "is the expansion, by the binomial
theorem, of (1+r)^n, which is the form in which the problem is
presented for solution by logarithms."

The series-expansion machinery the son later uses for log₁₀(1+x)
— the small-argument expansion 0.4343 × [x − ½x² + ⅓x³ − …] —
is in the same family. The son's multi-scale log technique is not
a categorical departure from the father's natural-algebra path; it
is a specialization of the same series-expansion technology
applied to log corrections at multiple scales.

So the framing of two methods "devised independently" is true at
the level of procedure but understates the algebraic continuity.
The father supplied the algebraic substrate, and named it
explicitly: "I have, in fact, worked out this algebraic formula" —
where the formula is the distributive expansion
(a+b+c)(d+e+f) = ad + ae + af + bd + be + bf + cd + ce + cf,
which Bidder calls the "natural algebra" of mental multiplication.
The son specialized that substrate to log corrections. The
continuity is genealogical, not merely typological.

## Coda

Both methods were devised independently for the same
problem. The father developed his approach first and used it
to compute eight-place logarithms of arbitrary primes in under
four minutes, mentally. The son learned the general principles
from his father, arrived at his own details independently, and
found them practical for six-place results.

The father considered the power of perceiving factors to be
innate and unteachable. The son considered his own method —
the multi-scale decomposition — to be learnable.

Neither claimed superiority over the other.

## Program-Facing Notes

The two methods are historical instances of two of this program's three disciplines applied to the log-side problem. A third (BIND) is implicit but not enacted by either Bidder.

**Father's method as historical CREATI.** A memorized catalog of prime logarithms plus perception of factor structure to decompose any target into catalog elements. The catalog is the primary asset; the work is constructive composition from that catalog. This is structurally CREATI: every result is downstream of a catalog item, the discipline rewards rich enumeration, and the difficulty (per the source's own framing) is strategic perception of how to traverse the catalog. The father's prime-log catalog is the human-arithmetic analogue of CREATI's catalog of named circle-side objects.

**Son's method as historical PERMEATE.** A small fixed set of universal scale constants — log(1.001), log(1.0001), log(1.00001), the modulus, and four prime logs — used by registering each target's contribution at every scale. The catalog is small, the procedure is fixed, the difficulty is bookkeeping rather than strategic choice. This is structurally PERMEATE: the saturation table is the scale catalog, the work is registration of where the target sits in pre-existing structure, and the discipline rewards preparation over perception.

**The implicit BIND question.** Neither Bidder asks: what reals are *exactly* reachable as ℤ-linear combinations of the son's nine memorized log-constants? The set is dense in ℝ but measure-zero; the structure of the reachable subset is a closure question with depth (touching Baker's theorem on linear forms in logarithms of algebraic numbers). The son's method computes approximations, not exact values; the closure question is where a BIND-flavored discipline would enter, and is not pursued by either historical actor here.

**Day-decoupling, by hand.** The son's "small factorable core × (1.001)^a × (1.0001)^b × (1.00001)^c" decomposition is mental-arithmetic Day-decoupling: a coarse stage (log of the core) plus a multi-scale correction stage where each scale contributes one decimal of resolution. The correction constants log(1+m) for m ∈ {0.001, 0.0001, 0.00001} are evaluated values of log₁₀(1+m) — Landfall's ε territory at small m. The son arrived at this structurally decoupled mental algorithm two generations before floating-point hardware made the same decoupling a hardware concern. See `memos/LANDFALL-EXPORT.md` for the program's reading of Day's decoupling theorem.

**Lattice ↔ multiplicative interface, with a visible seam.** The father lives in the multiplicative structure (factor catalog, navigation by prime decomposition). The son lives in a lattice structure (the multi-scale grid is a ℤ-lattice in log space). Both methods compute the same log values when the target permits; they differ in which structure they prefer. Where one method becomes hard — father: targets in sparse multiplicative regions, requiring helper-multiplier tricks; son: targets that don't decompose cleanly across scales — the other often remains easy. The two methods together delineate the seam between the two structures, which is exactly the seam this program is tracking.

## Open question (not pursued here)

A precise statement of which reals are exactly reachable from the son's nine-element constant set, and how this set's reachable-real structure compares to the multiplicative ℚ-span of {log p : p prime}, is the BIND-shaped closure question this memo flags but does not answer. See Baker, *Linear forms in the logarithms of algebraic numbers*, Mathematika 13 (1966), for the relevant transcendence-theory backdrop.
