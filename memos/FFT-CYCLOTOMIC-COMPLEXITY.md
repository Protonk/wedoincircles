# FFT-CYCLOTOMIC-COMPLEXITY

A search memo on whether five papers from the FFT complexity literature —
Schönhage–Strassen 1971, Winograd 1978, Heideman–Burrus 1986,
Auslander–Feig–Winograd 1984, and Morgenstern 1973 — supply the missing
piece of the compute-cost branch announced in the README and worked at
[memos/COUNTING-APPARATUS.md](memos/COUNTING-APPARATUS.md) and
[memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md](memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md).
This memo opens because the program has been computing in the same fields
as the FFT-complexity literature for sixty years from opposite directions
and has not yet wired the two together.

This is a **search memo**, not a result memo, and is provisional in the
sense of [CONTRIBUTING.md](CONTRIBUTING.md). Sources are gitignored under
`sources/`; the five papers are in hand and ready to be promoted to
`-BRIEF` extractions per [memos/AGENTS.md](memos/AGENTS.md) when each
directed read closes.

---

## Why this memo exists

The program already works in the cyclotomic ladder

```text
K_n = Q(cos(2 pi / n)),    [K_n : Q] = phi(n) / 2,
```

as the load-bearing closure-generator family on the circle side
([memos/NATIVE-F-MINIMAL-DEFINITION.md](memos/NATIVE-F-MINIMAL-DEFINITION.md)).
The closure-depth no-go is stated in those terms.

The DFT of length `N` is the algebraic isomorphism

```text
C[x] / (x^N - 1)  ->  prod_{d | N} C[x] / Phi_d(x),
```

evaluation at the `N`-th roots of unity, induced by the cyclotomic
factorization

```text
x^N - 1  =  prod_{d | N} Phi_d(x).
```

The trace fields `K_n` are the maximal real subfields of these cyclotomic
factors. Multiplicative complexity of DFT is — across sixty years of
algorithm-design literature — a count of the algebraic operations needed to
realize that isomorphism. Winograd's `2N - d(N)` bound is exactly a degree
sum across the cyclotomic factorization. Heideman–Burrus is the same count
for `N = 2^n`, where the cyclotomic tower aligns one-to-one with the
program's binade structure on the log side.

So:

- The objects the program calls "the K_n ladder" are the objects FFT
  complexity calls "cyclotomic factors of `x^N - 1`."
- Winograd's `2N - d(N)` is a sum over divisors of N where each divisor
  contributes work proportional to `phi(d)`. That is the same `phi(d)`
  the closure-depth no-go uses.
- Heideman–Burrus is the powers-of-two case where the cyclotomic tower
  aligns with the binade tower from Landfall §0.
- Morgenstern is the closest existing **lower bound**: bounded-coefficient
  Ω(N log N), in a hypothesis class that is naturally compatible with
  `Aff^+(R)`-style native operations.

The sentence the program needs from this literature is not a new theorem.
It is the existing theorems, transported.

## Target

> Identify which of Winograd 1978, Heideman–Burrus 1986, Auslander–Feig–
> Winograd 1984, Schönhage–Strassen 1971, and Morgenstern 1973 supply load-
> bearing inputs to (i) the open compute-cost branch announced in the
> README, (ii) the bounded-coefficient lower-bound hypothesis the
> Kraft-Parseval budget at
> [memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md](memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md)
> wants for its empirical-to-density proxy, and (iii) item (A)'s compute
> model in [memos/COUNTING-APPARATUS.md](memos/COUNTING-APPARATUS.md);
> identify the inputs by paper and stated theorem, and tag each by
> L-W-safety per [memos/LINDEMANN-BRIEF.md](memos/LINDEMANN-BRIEF.md).

The deliverable from this memo, when it closes, is a short list of
specific theorem statements with citations, ready for promotion into the
parent memos as load-bearing inputs.

## Items under search

### (A) Winograd 1978 — multiplicative complexity of DFT

**S. Winograd, "On computing the discrete Fourier transform," Math. Comp.
32 (1978), 175–199.** ([sources/Winograd-ComputingDiscreteFourier-1978.pdf](sources/Winograd-ComputingDiscreteFourier-1978.pdf))

The decisive paper for the program's purposes. Winograd proves that the
multiplicative complexity of the DFT of length `N` over a field containing
the appropriate roots of unity is

```text
M(DFT_N)  =  2N  -  (number of divisors of N),
```

via a decomposition of the DFT into independent computations on the
cyclotomic factors `Phi_d(x)` of `x^N - 1`. For each `d | N`, the work on
the `Phi_d`-factor is paid in operations proportional to `phi(d)`.

- **Known.** The closed-form bound, the matching algorithm, and the
  cyclotomic-factorization decomposition are all in the paper. Tightness
  for many `N` is established there.
- **Unknown for the program.** Whether the field-extension hypothesis
  matches the bounded-coefficient setting the Kraft-Parseval budget needs.
  Winograd works over arbitrary fields containing roots of unity;
  Morgenstern's bounded-coefficient lower bound (item E) is a strictly
  tighter hypothesis class. The two need to be checked against each other.
- **Closing condition.** A short paragraph stating the theorem with
  notation aligned to NATIVE-F-MINIMAL-DEFINITION (`phi(n)`, not "number
  of divisors"), and an explicit identification of the cyclotomic factors
  with the trace-field ladder used elsewhere in the program.

### (B) Heideman–Burrus 1986 — DFT at `N = 2^n`

**M. T. Heideman and C. S. Burrus, "On the number of multiplications
necessary to compute a length-2^n DFT," IEEE Trans. ASSP 34 (1986),
91–95.** ([sources/On_the_number_of_multiplications_necessary_to_compute_a_length-2nDFT.pdf](sources/On_the_number_of_multiplications_necessary_to_compute_a_length-2nDFT.pdf))

The powers-of-two case of Winograd's program, with exact (not asymptotic)
multiplication counts. The cyclotomic factorization is

```text
x^(2^n) - 1  =  prod_{k=0}^{n} Phi_(2^k)(x),
```

a tower indexed by binade depth.

- **Known.** Exact multiplication counts at every `n`. The factorization
  structure aligns level-by-level with the binary tower.
- **Unknown for the program.** Whether the per-level complexity in
  Heideman–Burrus is the same combinatorial object as the per-binade
  Kraft accounting in Landfall §5. The strong reading is yes — both count
  cyclotomic-factor work paid per level of the binary tower — but the
  identification has not been written out.
- **Closing condition.** A side-by-side comparison of the Heideman–Burrus
  per-level count and the Landfall §5 Kraft cylinder count at depth `p`,
  with the matching identified or the discrepancy named.

### (C) Auslander–Feig–Winograd 1984 — tensor framework

**L. Auslander, E. Feig, and S. Winograd, "New algorithms for the multi-
dimensional discrete Fourier transform," IEEE Trans. ASSP 31 (1983),
388–403; and "The multiplicative complexity of the discrete Fourier
transform," Adv. in Appl. Math. 5 (1984), 31–55.** ([sources/multiplicative-complexity.pdf](sources/multiplicative-complexity.pdf) — the 1984 paper; the 1983 ASSP paper is not in the local sources directory)

The framework paper. Auslander–Feig–Winograd formalize FFT algorithms as
tensor decompositions of the DFT matrix, where the tensor structure tracks
the cyclotomic factorization. This is the bridge paper for translating
Winograd's bounds into a form usable by the program: it makes the
decomposition explicit enough to count operations against a Kraft budget
rather than just a multiplication count.

- **Known.** The tensor formalism, the connection between
  CRT-on-`x^N - 1` and tensor decomposition, and the per-factor work
  accounting.
- **Unknown for the program.** Whether the tensor-decomposition accounting
  can be re-expressed as a self-delimiting code in the sense of Landfall
  §5. The hope is that the tensor structure at each cyclotomic factor
  becomes the prefix-free description of the work paid at that factor, so
  that Kraft's inequality applies to the global decomposition. This is
  the central bridge claim and is not in the existing literature; this
  memo's main creative move is to attempt it.
- **Closing condition.** Either a stated identification of tensor-
  decomposition tokens with Kraft cylinders, or a documented obstruction
  to that identification.

### (D) Schönhage–Strassen 1971 — bit/cyclotomic translation

**A. Schönhage and V. Strassen, "Schnelle Multiplikation großer Zahlen,"
Computing 7 (1971), 281–292.** ([sources/Fast Multiplication of Large Integers.pdf](<sources/Fast Multiplication of Large Integers.pdf>) — English translation in sources)

Integer multiplication via DFT over `Z[x] / (x^N + 1)`. The relevance to
the program is dual: the existing direction in the literature converts
*cheap multiplicative work* over a cyclotomic ring into *cheap bit work*
on integers; the program needs the reverse direction, which would convert
*irreducible bit work* on circle-side observables into *irreducible
multiplicative work* in the cyclotomic ladder.

- **Known.** The forward translation is the load-bearing piece of the
  paper; the conversion is constructive and explicit.
- **Unknown for the program.** Whether the reverse direction goes through
  in the program's compute model. Probably not as a literal inversion;
  more likely as a structural template for how a cyclotomic-complexity
  statement gets paid in self-delimiting bits.
- **Closing condition.** A statement of which direction of the Schönhage–
  Strassen translation the program can use, and which it cannot, with the
  obstruction named in the second case.

### (E) Morgenstern 1973 — bounded-coefficient lower bound

**J. Morgenstern, "Note on a lower bound of the linear complexity of the
fast Fourier transform," J. ACM 20 (1973), 305–306.** ([sources/FFT-lower-bound.pdf](sources/FFT-lower-bound.pdf))

The closest existing lower bound to what the program wants. Morgenstern
proves that any FFT algorithm using only constants of bounded magnitude
requires Ω(N log N) operations. The bounded-coefficient hypothesis is
natural for the program: native operations on the log side live in
`Aff^+(R)` with bounded constants, and the closure-depth no-go restricts
to that class.

- **Known.** The Ω(N log N) lower bound under bounded coefficients.
- **Unknown for the program.** Whether Morgenstern's bound technique can
  be re-expressed in Kraft units. The bound itself is not enough; the
  program needs the bound paid in the same currency as Landfall §5 so
  that the log-side and circle-side compute-cost statements are
  commensurable. This is where the Kraft-Parseval bridge actually
  becomes a bridge rather than a pun.
- **Closing condition.** Either a Morgenstern-style argument expressed in
  prefix-free / Kraft accounting, or a documented obstruction (most
  likely: Morgenstern's bound is in arithmetic-circuit depth, and the
  prefix-free reading would require a different unit).

## What this memo would buy if it closes

The current state of the program's compute-cost branch (per the README's
"Open search" status):

> The program's central open bet sits in the compute-cost branch: marry
> Kraft arithmetic to cyclotomic complexity without circular dependence
> on the circle.

If the five papers above import cleanly, the marriage is no longer a
hope. Winograd supplies the cyclotomic side; Morgenstern supplies the
lower-bound technique; Auslander–Feig–Winograd supplies the framework
that lets the two be paid in compatible units; Heideman–Burrus aligns the
binary case with the program's binade structure; Schönhage–Strassen
supplies the existing example of cyclotomic-to-bit translation as a
template.

If the bridge holds, the program is in a position to state a Landfall-
parallel theorem on the circle side, with explicit constants, in a
provenance class compatible with the L-W-safety discipline of
[memos/LINDEMANN-BRIEF.md](memos/LINDEMANN-BRIEF.md). That is the
deliverable announced in the README's compute-cost branch.

If the bridge does not hold, the failure mode is informative on its own
terms: it locates exactly which of the five papers the program cannot
use, and why.

## Adjacent anchors

Existing material this memo draws on:

- [memos/NATIVE-F-MINIMAL-DEFINITION.md](memos/NATIVE-F-MINIMAL-DEFINITION.md) —
  the closure-depth no-go, in `K_n` vocabulary. The cyclotomic ladder is
  the same object the FFT-complexity literature factorizes.
- [memos/LANDFALL-EXPORT.md](memos/LANDFALL-EXPORT.md) — the log-side
  Kraft accounting (§5) that the bridge wants to import to.
- [memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md](memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md)
  and [memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md](memos/KRAFT-BUDGET-ONE-DIMENSIONAL.md) —
  the Kraft-Parseval budget that wants Morgenstern as a load-bearing input.
- [memos/COUNTING-APPARATUS.md](memos/COUNTING-APPARATUS.md) — items (A)
  compute model and (C) τ portrait. Winograd settles (A)'s compute-model
  candidate (3) or (4) by showing that the algebraic-arithmetic-over-Q
  framework already has a quantitative complexity theory attached.
- [memos/LOWER-BOUND-COUNTRY.md](memos/LOWER-BOUND-COUNTRY.md) — the
  algebraic-complexity reading queue this memo's papers slot into. Several
  of the entries there (Strassen 1973, Bürgisser–Clausen–Shokrollahi 1997)
  are direct upstream of the five papers here.
- [memos/CONTINUED-FRACTIONS-CROSSWALK.md](memos/CONTINUED-FRACTIONS-CROSSWALK.md) —
  recurring arithmetic substrate. The cyclotomic ladder is the algebraic
  cousin of the CF crosswalk; both index the same underlying Galois-
  theoretic structure on `Q(zeta_n)`.
- [memos/LINDEMANN-BRIEF.md](memos/LINDEMANN-BRIEF.md) — the L-W-safety
  audit. None of the five papers here use Lindemann–Weierstrass, so the
  provenance tagging is straightforward; it should still be done explicitly.

Anchors that would be written if the memo closes:

- `memos/WINOGRAD-1978-BRIEF.md` — source-extraction brief on the
  cyclotomic-factorization complexity argument.
- `memos/MORGENSTERN-1973-BRIEF.md` — source-extraction brief on the
  bounded-coefficient lower-bound technique.
- The other three papers may not need full briefs if their use is
  contained.

## What this memo is not

- **Not an FFT tutorial.** The five papers are technical and assume
  familiarity with cyclotomic factorization, tensor decomposition, and
  arithmetic-circuit lower-bound technique. Agents who need orientation
  before reading them should consult Shpilka–Yehudayoff 2010 (survey) or
  Bürgisser–Clausen–Shokrollahi 1997 (textbook), both already cited at
  [memos/LOWER-BOUND-COUNTRY.md](memos/LOWER-BOUND-COUNTRY.md).
- **Not a claim that FFT-as-procedure is in the program.** It is not.
  The program works the obstruction face. The construction face of the
  FFT literature is the upper-bound side; the program imports it as
  benchmark and as cyclotomic-structure source, not as method.
- **Not load-bearing for the closure-depth no-go.** That theorem stands
  on the K_n ladder alone, no compute-cost machinery required. This memo
  is for the compute-cost branch, which is open and downstream.
- **Not a commitment to all five papers being load-bearing.** The likely
  outcome is that two or three are decisive (Winograd, Morgenstern, and
  probably Auslander–Feig–Winograd), and the others enter as background.
  The memo is honest about which is which only after directed reads.

## Hazards

Three failure modes worth naming so a directed read can detect them:

1. **The construction-face / obstruction-face inversion is not free.**
   The literature proves *upper bounds* on FFT complexity. The program
   wants *lower bounds*. Importing a paper's bound as if the direction
   were preserved is a category error. Each directed read should explicitly
   tag which direction the cited bound runs in, and how the bridge to
   the program's lower-bound ambition is supposed to work.

2. **Field-of-coefficients drift.** Winograd works over arbitrary fields
   containing the roots of unity. Morgenstern works under bounded
   coefficients. The program's `Aff^+(R)` is bounded-coefficient-natural
   but not closed under root-of-unity adjunction. If a directed read
   cannot show that the bound's hypothesis class is compatible with
   `Aff^+(R)` after honest accounting, the import does not go through.

3. **Tensor decomposition is a Kraft cousin, not a Kraft identity.** The
   central bridge claim — that Auslander–Feig–Winograd's tensor
   accounting can be re-expressed as Kraft accounting — is the place
   where the most wishful thinking can hide. A specific check: does the
   tensor-decomposition accounting satisfy Kraft's inequality with a
   provable constant, or does it require additional structure
   (semicomputability, prefix-freeness, universal dominance) the program
   would have to import separately? Fortnow's universal-dominance step
   ([memos/FORTNOW-KOLMOGOROV-BRIEF.md](memos/FORTNOW-KOLMOGOROV-BRIEF.md)
   §6) may be needed; if so, that has to be called out and audited per
   [memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md) §(A5)'s
   shell-calculus / universality split.

A directed read that does not address (1), (2), and (3) explicitly is
incomplete for the program's purposes.

## Order of work

Ranked from least load-bearing first, ending at the central bridge claim:

1. **Winograd 1978** — the cleanest cyclotomic-ladder result. Read first
   to establish that the K_n ladder appears explicitly in the FFT
   literature with the same `phi` accounting the program already uses.
   Promote to `memos/WINOGRAD-1978-BRIEF.md` on close.
2. **Heideman–Burrus 1986** — the binary case, aligning with the binade
   tower. Read second to establish that the Landfall-side binary tower
   has a direct analog on the circle side. Short paper; brief if needed
   may be appended to the Winograd brief rather than standalone.
3. **Auslander–Feig–Winograd 1984** — the tensor framework. Read third
   to establish whether the bridge to Kraft accounting goes through.
   This is where the hazard items (2) and (3) get worked out. Decisive
   for the program; promote to its own brief on close.
4. **Schönhage–Strassen 1971** — the bit/cyclotomic translation
   template. Read fourth as a template for what the bridge looks like
   in an existing case. Note where the program runs the template
   forwards vs. backwards.
5. **Morgenstern 1973** — the bounded-coefficient lower bound. Read
   fifth, after the framework is in place, because the value of the bound
   depends on whether it can be expressed in Kraft units. If the bridge
   from item (3) goes through, Morgenstern is the lower-bound input the
   compute-cost branch announces it is looking for. Promote to
   `memos/MORGENSTERN-1973-BRIEF.md` on close.

Each directed read closes with a sentence of form:

> *"This contributes [theorem statement] to the K_n-Kraft transport, with
> hypothesis class [X], provenance tag [pre-1882 / methodologically
> pre-L-W / post-L-W methodologically essential], and slots into [item of
> COUNTING-APPARATUS or KRAFT-BUDGET-ONE-DIMENSIONAL]."*

If a directed read cannot produce such a sentence, the read did not serve
the bridge, and the paper either drops out of the load-bearing list or
gets re-read with a different question.

## Exit criteria

The memo freezes and promotes when any one of the following triggers:

1. **Bridge closes.** Items (A), (C), and (E) are all promoted to briefs
   and the central bridge claim — that tensor-decomposition complexity
   on the cyclotomic side is equivalent (up to a stated constant) to
   prefix-free Kraft accounting — is stated and either proven or
   documented as a load-bearing hypothesis. The compute-cost branch in
   the README transitions from "Open search" to "Theorem-shaped." Promote
   the bridge statement into a Landfall-parallel circle-side memo and
   retire FFT-CYCLOTOMIC-COMPLEXITY.

2. **Bridge fails on a specific item.** A directed read on (A), (C), or
   (E) produces a documented obstruction to the bridge — most likely a
   coefficient-class mismatch (hazard 2) or a tensor-vs-prefix-free
   accounting incompatibility (hazard 3). Promote the negative finding
   into [memos/COUNTING-APPARATUS.md](memos/COUNTING-APPARATUS.md) §(A) as
   a constraint on compute-model choice, and retire this memo.

3. **Two directed reads close without a tagged sentence.** Same discipline
   as the parent search memos: if two of the five reads come back without
   a sentence of the form named in §"Order of work," demote this memo to
   low-priority and note the failure mode.

## Status

Open search memo. All five papers in hand, sources directory landing
imminent. No directed reads completed. The reading queue above is the
active queue; Winograd 1978 is first in line because it is the cleanest
single-paper instance of the K_n ladder appearing in the FFT-complexity
literature, and reading it first establishes the surprise the rest of the
program is about to absorb: the FFT-complexity literature has been
factorizing the program's load-bearing closure-generator family for sixty
years, in a vocabulary that did not advertise the connection.
