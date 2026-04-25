# HEIDEMAN-JOHNSON-BURRUS-1985-BRIEF

Source-extraction memo on M. T. Heideman, D. H. Johnson, & C. S. Burrus,
"Gauss and the History of the Fast Fourier Transform," *Archive for History
of Exact Sciences* 34 (1985), pp. 265–277, communicated by C. Truesdell,
received Feb. 28, 1985 ([sources/gauss-fft-history.pdf](sources/gauss-fft-history.pdf)).

**Why this brief exists.** The L-W-safety audit
([memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md)) applied
backward through the FFT lineage. Gauss's *Theoria Interpolationis*
was written in 1805 — 77 years before Lindemann–Weierstrass — so its
content is **certifiably pre-1882** and the FFT chain has a clean
upstream endpoint inside the L-W-safety window. The audit traces that
endpoint forward through documented gaps (Hansen's 1835 non-citation,
Burkhardt's 1904 unnoticed-noticing, the 1866–1965 quiet century) to
the four modern complexity briefs
([fft/AUSLANDER-FEIG-WINOGRAD-1984-BRIEF.md](fft/AUSLANDER-FEIG-WINOGRAD-1984-BRIEF.md),
[fft/MORGENSTERN-1973-BRIEF.md](fft/MORGENSTERN-1973-BRIEF.md),
[fft/WINOGRAD-1978-BRIEF.md](fft/WINOGRAD-1978-BRIEF.md),
[fft/SCHOENHAGE-STRASSEN-1971-BRIEF.md](fft/SCHOENHAGE-STRASSEN-1971-BRIEF.md))
the program inherits at the modern end.

**What was read.** The full 13-page PDF, including the dating-of-the-work
appendix and reference list. Read with the lens: *trace the inheritance
chain that the four modern briefs sit at the modern end of, identify gaps
and transmission failures, and record the author overlap between the
historiographers and the technical contributors.*

**Confidence level.** High on the paper's internal mathematical claim
(Gauss 1805 ≡ decimation-in-frequency Cooley–Tukey for real data) — the
algebraic comparison is in the paper. High on the chronology. Medium on
the historiographical claims (library records, diary entries, who knew
whom, who cited whom) — these are sourced to Dunnington, Merzbach,
Burkhardt, etc., not independently checked here. The brief reports them
as *paper-states-without-check* where appropriate.

**Trust boundary up front.** This brief audits the inheritance chain. It
does **not** supply technical content for the lower-bound work. The
program must not cite "Heideman–Johnson–Burrus 1985" for any complexity
or cyclotomic-depth claim. The technical Heideman–Burrus paper is the
1986 binary-DFT exact-count work (queue item 2 in
[fft/FFT-CYCLOTOMIC-COMPLEXITY.md](fft/FFT-CYCLOTOMIC-COMPLEXITY.md)
§"Order of work"), separate from this historiographical paper, by an
overlapping author set.

---

## 1. The 1805 Manuscript and Its Equivalence to Cooley–Tukey

### What the paper establishes from sources

Gauss's treatise *Theoria Interpolationis Methodo Nova Tractata* was
written most likely in October–November 1805, was never published in his
lifetime, and appeared posthumously only in *Carl Friedrich Gauss Werke*
Vol. III (Göttingen, 1866), pp. 265–330 (the paper's reference [10]).
Goldstine's *History of Numerical Analysis from the 16th Through the 19th
Century* (1977, ref. [9]) gives an English translation of parts related
to trigonometric interpolation (Articles 25–28).

The paper's content (paper, p. 269): Gauss extends trigonometric
interpolation to general periodic functions of the form

```
         m                        m
f(x) =  sum a_k cos(2 pi k x)  +  sum b_k sin(2 pi k x),
        k=0                      k=1
```

with `m = (N − 1)/2` for odd `N` and `m = N/2` for even `N`. Articles
19–20 of the treatise give "the now well-known formulas for the DFT" of
the sample values `f(x_n)`, `x_n = n/N`. The paper records this as "the
earliest explicit formula for the general DFT that we have found"
(p. 269).

### What the paper proves about equivalence

The paper carries out the explicit algebraic comparison (pp. 269–271).
Gauss's procedure: take `N = N_1 N_2`, sample over `N_2` interleaved
sub-grids of `N_1` equally spaced points, compute a length-`N_1` finite
Fourier series for each sub-grid, then combine via a length-`N_2`
correction. In modern index-mapping terms (paper's eq. 4):

```
                    N_2-1  N_1-1
C(k_1 + N_1 k_2) =   sum    sum   X(N_2 n_1 + n_2) W_N1^{n_1 k_1}  W_N^{n_2 k_1}  W_N2^{n_2 k_2}
                    n_2=0  n_1=0
```

The paper's verbatim verdict (p. 270):

> "This is exactly the exponential form of GAUSS' algorithm where the
> `W_N` term accounts for the shifts from the origin of the `N_2`
> length-`N_1` sequences. This is also exactly the FFT algorithm derived
> by COOLEY & TUKEY in 1965 [1] where `W_N` is called a *twiddle factor*
> [2], a factor to correct the DFT of the inner sum for the shifted
> samples of `X(n)`. The equivalence of GAUSS' algorithm and the
> COOLEY–TUKEY FFT is not obvious due to the notation and trigonometric
> formulation of GAUSS."

And on p. 271:

> "Thus, GAUSS' algorithm is as general and powerful as the COOLEY–TUKEY
> algorithm and is, in fact, equivalent to an algorithm called
> decimation-in-frequency adapted to a real data sequence."

The paper translates Article 27 of the treatise into English (p. 270,
quoted in full there): Gauss states explicitly that the algorithm
generalizes from `N = mu nu` to arbitrary composite `N`. He gives worked
examples for `N = 12` (orbit of asteroid Pallas, Article 28) and `N = 36`
with `N_1 = N_2 = 6` (Article 41, special case of odd symmetry).

### What the paper notes Gauss did *not* do

Gauss did not quantify the algorithm's complexity. Quoting the paper
(p. 271): "He did not, however, go on to quantify the computational
requirements of his method to obtain the now familiar `N · sum N_i` or
`N log N` expressions for its computational complexity." Gauss's
motivation, per the paper, was purely practical: faster orbit
computation for a "select, but interesting, set of sequence lengths."

### Inferred for the program

The 1805 manuscript is the genuine origin point of the FFT algorithm in
the program's INHERIT sense: it predates Cooley–Tukey by 160 years, it
contains the algorithmic content (general composite `N`, decimation, the
twiddle correction), and it is *equivalent* — not merely "similar" — to
the modern algorithm. The chain therefore has a well-defined upstream
endpoint at 1805 with provenance certified through *Werke* Vol. III
(1866).

What it does *not* give the program: any cyclotomic-depth content, any
lower-bound machinery, any mention of multiplicative complexity. Gauss
counted neither operations nor field extensions. The compute-cost
branch's questions are not answered by the 1805 manuscript; they are
not even asked there.

---

## 2. Provenance Chain with Dates, Attribution, and Gaps

### The principal table

Reproduced from the paper, p. 272 ("Principal Discoveries of Efficient
Methods of Computing the DFT"):

| Date | Researcher | Lengths | DFT values | Application |
|------|-----------|---------|------------|-------------|
| 1805 | C. F. Gauss [10] | any composite integer | All | orbits of celestial bodies |
| 1828 | F. Carlini [28] | 12 | 7 | barometric pressure |
| 1846 | A. Smith [25] | 4, 8, 16, 32 | 5 or 9 | ship's compass deviations |
| 1860 | J. D. Everett [23] | 12 | 5 | underground temperatures |
| 1903 | C. Runge [7] | `2^n K` | All | harmonic analysis |
| 1939 | K. Stumpff [16] | `2^n K`, `3^n K` | All | harmonic analysis |
| 1942 | Danielson & Lanczos [5] | `2^n` | All | X-ray crystallography |
| 1948 | L. H. Thomas [13] | coprime factors | All | harmonic analysis |
| 1958 | I. J. Good [3] | coprime factors | All | harmonic analysis |
| 1965 | Cooley & Tukey [1] | any composite | All | harmonic analysis |
| 1976 | S. Winograd [14] | coprime factors | All | complexity theory |

### Pre-Gauss substrate (paper §"The Background of Gauss' Work")

- **L. Euler** (1707–1783, refs [31]–[35]): introduced trigonometric
  series in analysis. In ref. [34] Euler "uses a trigonometric series to
  describe the motions of a discrete approximation to sound propagation
  in an elastic medium. By example, he derives a formula for the
  coefficients of a series of sines given samples of the function, which
  can be interpreted as the DFT for a series consisting only of sines"
  (p. 268). This is Euler's sine-only DFT.

- **A.-C. Clairaut** (1713–1765, ref. [37]): published in 1754 "what we
  currently believe to be the earliest explicit formula for the DFT (the
  computation for series coefficients from equally spaced samples of the
  function), but it was restricted to a cosine FOURIER series" (p. 268).

- **D. Bernoulli** (1700–1782, ref. [38]): in 1753 "expressed the form
  of a vibrating string as a series of sine and cosine terms with
  arguments of both time and distance" (p. 268).

- **J. L. Lagrange** (1736–1813, refs [39]–[40]): in 1759 and 1762,
  "extending the work of Euler, he published a DFT-like formula for
  finite Fourier series containing only sines" (p. 268). Carlini's 1828
  paper cites Lagrange. Lagrange's papers were published in *Miscellanea
  Taurinensia*, the proceedings of the Turin Academy.

The paper records (p. 268, footnote 2) that Dunnington, by searching
University of Göttingen library records (ref. [42]), compiled a list of
books borrowed by Gauss, and that Gauss borrowed the volumes containing
Lagrange's papers [39] and [40] while a student between 1795 and 1798.
This is the documented direct upstream link from Lagrange to Gauss.

### Known gaps and transmission failures

The paper documents several:

1. **Gauss → Hansen (1835).** Most explicit transmission failure in the
   paper. Quote (p. 267): "The only other method found by BURKHARDT
   which predates ARCHIBALD SMITH is that of PETER ANDREAS HANSEN
   (1795–1874) in 1835 [29] for `n = 64`. These works have no apparent
   influence on the work by the British. HANSEN was heavily influenced
   by GAUSS in his astronomical work, but does not mention GAUSS in the
   development of his algorithms for harmonic analysis for reasons which
   shall be made clear later." *The paper records the non-citation; it
   does not fully explain it.*

2. **Gauss → Burkhardt (1904).** Burkhardt wrote the *Encyklopädie der
   Mathematischen Wissenschaften* article (ref. [11], 1899–1916) that is
   the second known reference to Gauss's algorithm. Quote (p. 266):
   "BURKHARDT comments that GAUSS' method was general, but seemingly
   not known by practitioners. It is interesting to note that
   GOLDSTINE'S and BURKHARDT's works went almost as unnoticed as
   GAUSS' work itself."

3. **Continental → British 19th c.** Quote (p. 267): "These works have
   no apparent influence on the work by the British." The British chain
   (Smith 1846 → Everett 1860 → Kelvin → Darwin/Strachey 1883/1884)
   developed independently of the Gauss/Carlini/Hansen line.

4. **Cooley–Tukey citation chain.** Quote (p. 265): "In their original
   paper COOLEY & TUKEY referred only to the work of I. J. GOOD [3]
   published in 1958 as influencing their development. However, it was
   soon discovered there were major differences between the
   COOLEY–TUKEY FFT and the algorithm described by GOOD, which is now
   commonly referred to as the prime factor algorithm (PFA). Soon after
   the appearance of the COOLEY–TUKEY paper, RUDNICK [4] demonstrated a
   similar algorithm based on the work of DANIELSON & LANCZOS [5] which
   had appeared in 1942." Cooley–Lewis–Welch [6] subsequently traced
   back to Runge (1903/1905), but as the paper notes (p. 265): "While
   not influencing their work directly, the algorithm developed by
   COOLEY & TUKEY clearly had roots in the early twentieth century."

5. **Gauss → Goldstine (1977).** Quote (p. 272): "BURKHARDT pointed out
   this algorithm in 1904 and GOLDSTINE suggested the connection between
   GAUSS and the FFT in 1977, but both of these went largely unnoticed,
   presumably because they were published in books dealing primarily
   with history."

The paper's closing summary (p. 272): "Almost one hundred years passed
between the publication of GAUSS' algorithm [in *Werke* III, 1866] and
the modern rediscovery of this approach by COOLEY & TUKEY." T. S. Huang
remarked in 1971 (paper ref. [50]) that "the FFT was GAUSS' 1001st
algorithm" — the paper records this as accurate.

---

## 3. Author Overlap with Technical Contributions

The paper's author triple is **M. T. Heideman, D. H. Johnson, C. S.
Burrus** (Rice University, Department of Electrical & Computer
Engineering). The technical Heideman–Burrus paper on the exact
multiplicative complexity of the length-`2^n` DFT is queue item 2 in
[fft/FFT-CYCLOTOMIC-COMPLEXITY.md](fft/FFT-CYCLOTOMIC-COMPLEXITY.md)
§"Order of work":

> Heideman, M. T. & Burrus, C. S. "On the number of multiplications
> necessary to compute a length-`2^n` DFT," *IEEE Trans. ASSP* (1986).

That is one year after the present historiographical paper, by an
overlapping author pair (Heideman + Burrus, minus Johnson; the queue
file is locally `sources/On_the_number_of_multiplications_necessary_to_compute_a_length-2nDFT.pdf`).

Internal corroboration in the present paper: ref. [12] is "Heideman &
Burrus, *A Bibliography of Fast Transform and Convolution Algorithms
II*, Technical Report Number 8402, Electrical Engineering Dept., Rice
University, Houston, TX 77251-1892, Feb. 1984" — an earlier
bibliographical artifact by the same pair, which the paper relies on
("This has resulted in a bibliography of over 2000 entries [12]",
p. 266 footnote 1).

**Inheritance note for the program.** The historiographers and the
technical contributors are the same hands. When the program draws on
Heideman–Burrus 1986 for binary-DFT exact counts, it is drawing on a
tool whose authors also did the provenance audit on the chain that
produced the tool. The 1985 paper is a same-author historiographical
record for the 1986 technical paper. This does not eliminate the need
for the program to do its own audit; it does strengthen the chain of
custody between Gauss 1805 and Heideman–Burrus 1986.

---

## 4. Inheritance Forward to the Four Framework Briefs

The four FFT-complexity briefs already in the repo all sit downstream
of Cooley–Tukey 1965. The paper places them on the chain as follows
(some of the mapping is the paper's, some is inferred for the program;
inference noted explicitly).

### Schönhage–Strassen 1971

Outside the paper's coverage. The FFT-kernel inheritance from
Cooley–Tukey is internal to
[fft/SCHOENHAGE-STRASSEN-1971-BRIEF.md](fft/SCHOENHAGE-STRASSEN-1971-BRIEF.md).
*That step is not audited here.*

### Morgenstern 1973

Outside the paper's coverage. Morgenstern's lower bound takes the
Cooley–Tukey FFT as its upper-bound target; the inheritance step is
internal to [fft/MORGENSTERN-1973-BRIEF.md](fft/MORGENSTERN-1973-BRIEF.md).
*That step is not audited here.*

### Good 1958 → Cooley–Tukey 1965 → Winograd 1976/78

*From the paper.* Good 1958 is in the principal table at p. 272, and
Winograd 1976 is the table's last entry. The paper notes (p. 266) that
Cooley–Tukey originally referred only to Good. Winograd's prime-factor
algorithm work generalizes Good's, and the paper records Winograd's
contribution as "Use of complexity theory for harmonic analysis" — the
inflection where the chain becomes complexity-theoretic. The brief
[fft/WINOGRAD-1978-BRIEF.md](fft/WINOGRAD-1978-BRIEF.md) thus sits
on the Good → Winograd substrand; through Cooley–Tukey it also touches
the Gauss substrand at the 1965 confluence.

### Winograd 1978 → Auslander–Feig–Winograd 1984

*Outside the paper's coverage.* AFW (1984) postdates the bibliography
[12] of Feb. 1984 marginally, and is published the same year as the
present paper's submission (received Feb. 28, 1985). The paper does
not include AFW in the table or text. Inheritance from Winograd's
prime-factor framework to AFW's tensor-product framework is internal
to the modern algebraic-complexity literature; see
[fft/AUSLANDER-FEIG-WINOGRAD-1984-BRIEF.md](fft/AUSLANDER-FEIG-WINOGRAD-1984-BRIEF.md)
for the technical content. *That step is not audited by this paper.*

### Summary diagram

```
             pre-1805 substrate
           (Euler, Clairaut, Bernoulli)
                     |
                  Lagrange
                  1759/62
              (sine-only DFT,
               read by Gauss
               at Göttingen)
                     |
                     v
                  Gauss 1805         [Theoria Interpolationis,
              (general composite N,    posthumous Werke III 1866]
            cos+sin, twiddle factor)
                     |
            +--------+--------+
            |                 |
       Hansen 1835       Carlini 1828
       (no citation)
            |
            v
         |  Burkhardt 1904  |
         | Encyklopädie     |  -- transmission gap, 19th-c.
         |  notes Gauss     |     British line independent
         | (largely unnoticed)
            |
            v
       Runge 1903/1905
       Stumpff 1939
       Danielson-Lanczos 1942
            |
            +------ Good 1958 (PFA, coprime factors,
            |                   independent line via Thomas 1948)
            |                |
            v                v
       Cooley–Tukey 1965 (cited Good only;
            |              Runge link found later by C-L-W 1967)
            |
            +------------+--------------+----------------+
            |            |              |                |
            v            v              v                v
      Schönhage-      Morgenstern   Winograd 1976/78   [via Winograd]
      Strassen        1973          (PFA + complexity      |
      1971            (lower bound   theory)               v
      [Brief]         on C-T target) [Brief]            AFW 1984
                      [Brief]                           [Brief]
                                              (outside paper coverage)
```

The chain has a long quiet century (1866 *Werke* publication →
1904 Burkhardt → 1942 Danielson–Lanczos), several independent
rediscoveries, and one explicit non-citation (Hansen 1835).

---

## 5. The Sine Question

### What the paper directly states

The paper records, factually, that the early DFT-class formulas were
basis-restricted:

- **Clairaut 1754**: cosine-only series.
- **Euler [34], pre-1750**: derives sine-only series coefficients from
  samples for sound propagation in an elastic medium.
- **Lagrange 1759/1762**: sine-only ("LAGRANGE's DFT (sine only)" is the
  paper's verbatim labeling in the dating appendix on p. 273, in the
  September 1795 entry on Gauss's library borrowing).
- **Bernoulli 1753**: vibrating string — sine and cosine, with
  arguments of both time and distance.
- **Gauss 1805**: first general cosine + sine series for arbitrary
  periodic functions (paper, p. 269 eq. 2).

### What the paper says about *why* sines came first

The paper gives a problem-class answer, not a structural one
(p. 268):

> "CLAIRAUT and LAGRANGE were concerned with orbital mechanics and the
> problem of determining from a finite set of observations the details
> of an orbit. Consequently, their data was periodic and they used an
> interpolation approach to orbit determination."

Note the conflation: Clairaut's 1754 work was orbital-mechanics-driven,
but Lagrange's references [39] *Recherches sur la Nature et la
Propagation du Son* and [40] *Solution de Différents Problèmes de
Calcul Intégral* (paper refs) are sound-propagation and pure
integral-calculus. The paper aggregates these problem domains under a
single periodicity rationale. Euler's sine-only work (paper ref. [34],
*De Propagatione Pulsuum per Medium Elasticum*) is sound-propagation,
not orbital. So:

- **Cosine substrate** → orbital mechanics (Clairaut), where the
  natural data is even/symmetric about an angular origin.
- **Sine substrate** → sound propagation in elastic media (Euler,
  Lagrange's [39]) and vibrating strings with fixed endpoints
  (Bernoulli), where the natural boundary conditions force the
  function to vanish at the ends and the natural basis is sines.

The paper does **not** make a structural argument that one basis is
algorithmically more natural than the other. The split appears in the
paper as a problem-class accident: each early author worked in the
basis their physical problem demanded, and the union to general
cos+sin is Gauss's 1805 unification. *The paper records the
trigonometric-formulation difficulty as an obstacle to recognizing
Gauss's algorithm as an FFT* (p. 270: "The equivalence of GAUSS'
algorithm and the COOLEY–TUKEY FFT is not obvious due to the notation
and trigonometric formulation of GAUSS"; p. 271: "GAUSS' method was
also derived using real trigonometric functions rather than complex
exponentials, making it more difficult to relate his method to current
FFT techniques"). So the trigonometric vs. exponential split is a
*notation* obstacle in the paper's account, distinct from the
sine-vs-cosine basis question.

### Note on the Gauss–Euler pair

The structurally relevant pair attacking via sines is **Gauss and
Euler**, both covered in the paper. Euler's sine-only DFT for sound
propagation in an elastic medium ([34], pre-1750) is the early
sine-substrate move; Gauss 1805 is the unification to general
`cos + sin`. Laplace is absent from this paper (text, reference list
[1]–[50], principal table p. 272, and dating appendix pp. 273–274);
his harmonic-analysis work is not part of the inheritance chain this
paper documents. The sine-question is fully readable from Gauss and
Euler alone.

### Inferred for the program

The program's circle side is currently cosine-only:

```
K_n = Q(cos(2 pi / n)),    [K_n : Q] = phi(n) / 2.
```

This is the load-bearing closure-generator family in
[memos/NATIVE-F-MINIMAL-DEFINITION.md](memos/NATIVE-F-MINIMAL-DEFINITION.md).
The cosine choice tracks the *real subfield* of `Q(zeta_n)`. The full
cyclotomic field `Q(zeta_n)` has degree `phi(n)` — twice the degree
of `K_n`.

Working in `K_n` is not just "avoiding `C`"; it is the unique
multiplicatively-closed half of the `Q(zeta_n)` decomposition under the
geometric reflection `theta -> -theta`. Both halves are eigenspaces of
the Galois involution `sigma_{-1}: zeta_n -> zeta_n^{-1}` on
`Q(zeta_n)`, but only the `(+1)`-eigenspace `K_n` is a subfield; the
`(-1)`-eigenspace `E_{-1} = K_n · 2 i sin(2 pi / n)` is a 1-dimensional
`K_n`-module that is not closed under multiplication
(`(2 i sin(2 pi / n))^2 = -4 sin^2(2 pi / n) in K_n`, outside
`E_{-1}`). The choice to work in `K_n` is therefore *forced by
closure*, not selected from parallel options. The next subsection
proves the eigenspace identification.

Whether anything analogous to closure-depth lives on the
`(-1)`-eigenspace — viewed as a `K_n`-module rather than a subfield —
is an **open program question** the brief does not resolve. The full
cyclotomic field `Q(zeta_n)` is the natural larger setting; whether
running closure-depth analysis there surfaces obstructions invisible
from `K_n` is also open and would require an internal computation in
the program.

### Proof: `K_n` is the `(+1)`-eigenspace of the reflection involution

**Setup.** Fix `n >= 3`. Let `zeta_n = e^(2 pi i / n)`, a primitive
`n`-th root of unity. The cyclotomic field `Q(zeta_n)` has degree
`phi(n)` over `Q`. Let `K_n = Q(cos(2 pi / n))`.

**Step 1: The involution `theta -> -theta` is the Galois automorphism
`sigma_{-1}` of `Q(zeta_n)`.**

The Galois group `G = Gal(Q(zeta_n) / Q)` is canonically `(Z / nZ)*`,
acting on the generator by `sigma_a(zeta_n) = zeta_n^a` for
`a in (Z / nZ)*`. Complex conjugation on `C` restricts to `Q(zeta_n)`
as the automorphism `sigma_{-1}: zeta_n -> zeta_n^{-1}`.
Geometrically, viewing `zeta_n` as the point on the unit circle at
angle `2 pi / n`, this is reflection `theta -> -theta`.

**Step 2: `K_n = Fix(sigma_{-1})`.**

The element `zeta_n + zeta_n^{-1} = 2 cos(2 pi / n)` is fixed by
`sigma_{-1}` (since `sigma_{-1}(zeta_n + zeta_n^{-1}) = zeta_n^{-1} +
zeta_n`). So `K_n ⊆ Fix(sigma_{-1})`. For the reverse: `sigma_{-1}`
has order 2 in `G` (assuming `n > 2`, since then `zeta_n != zeta_n^{-1}`),
so by Galois correspondence
`[Q(zeta_n) : Fix(sigma_{-1})] = 2`. The minimal polynomial of
`zeta_n` over `K_n` is `x^2 - 2 cos(2 pi / n) x + 1`, of degree 2,
so `[Q(zeta_n) : K_n] = 2`. Together with
`K_n ⊆ Fix(sigma_{-1}) ⊆ Q(zeta_n)`, this forces
`K_n = Fix(sigma_{-1})`.

**Step 3: Eigenspace decomposition under `sigma_{-1}`.**

`Q(zeta_n)` is a 2-dimensional `K_n`-vector space. The automorphism
`sigma_{-1}` is `K_n`-linear (since `K_n` is fixed pointwise) and has
order 2, so its minimal polynomial divides `x^2 - 1 = (x - 1)(x + 1)`.
Hence `Q(zeta_n)` decomposes as a direct sum of `K_n`-eigenspaces:

```
Q(zeta_n) = E_{+1} ⊕ E_{-1}
```

The `(+1)`-eigenspace is `Fix(sigma_{-1}) = K_n` by Step 2. For the
`(-1)`-eigenspace: the element `zeta_n - zeta_n^{-1} = 2 i sin(2 pi / n)`
satisfies

```
sigma_{-1}(zeta_n - zeta_n^{-1}) = zeta_n^{-1} - zeta_n = -(zeta_n - zeta_n^{-1}),
```

so it lies in `E_{-1}`. Since `E_{-1}` is 1-dimensional over `K_n`
(the eigenspaces of an order-2 automorphism on a 2-dimensional space,
when both eigenvalues appear, are each 1-dimensional) and
`zeta_n - zeta_n^{-1} != 0`, we have

```
E_{-1} = K_n · (zeta_n - zeta_n^{-1}) = K_n · 2 i sin(2 pi / n).
```

**Step 4: The eigenspace decomposition matches even/odd symmetry under
`theta -> -theta`.**

The involution `theta -> -theta` acts on real-valued functions of
`theta` by `f(theta) -> f(-theta)`. The classical eigenfunctions are:

- `cos(2 pi k / n)`: `cos(-2 pi k / n) = cos(2 pi k / n)` —
  `(+1)`-eigenfunction.
- `sin(2 pi k / n)`: `sin(-2 pi k / n) = -sin(2 pi k / n)` —
  `(-1)`-eigenfunction.

So in the function-space sense, the `(+1)`-eigenspace under
`theta -> -theta` is spanned by cosines and the `(-1)`-eigenspace is
spanned by sines.

Matching this to the algebraic decomposition: `K_n` is generated over
`Q` by `cos(2 pi / n)`, the lowest-frequency `(+1)`-eigenfunction.
The `(-1)`-eigenspace `K_n · 2 i sin(2 pi / n)` is generated over
`K_n` by `sin(2 pi / n)` with an `i` factor. The `i` carries the
odd-eigenvalue through the algebraic embedding: the Galois action
`sigma_{-1}` acts on the algebraic representation
`(zeta_n - zeta_n^{-1}) / (2 i)` rather than on the real-number
value `sin(2 pi / n)` directly.

**Conclusion.** Working in `K_n = Q(cos(2 pi / n))` is choosing the
`(+1)`-eigenspace of the Galois involution `sigma_{-1}`, which
corresponds geometrically to reflection `theta -> -theta` on the unit
circle and analytically to the even-symmetric function-space
component. The full structure `Q(zeta_n)` decomposes as
`K_n ⊕ K_n · 2 i sin(2 pi / n)` under this involution; restricting
to `K_n` lives in the `(+1)`-eigenspace and ignores the
`(-1)`-component. The identification "even-symmetric eigenspace under
`theta -> -theta`" is exact. ∎

### Connection to the paper's algorithmic verdict

The paper's equivalence statement on p. 271 (quoted in §1) ends with
the phrase "decimation-in-frequency adapted to a *real data sequence*."
The qualifier *real data sequence* means the input `X(n)` is in `R`,
the fixed field of complex conjugation on `C`. The proof above
identifies `K_n` as the fixed field of the same involution restricted
to `Q(zeta_n)`. Gauss's algorithmic choice (real input) and the
program's algebraic choice (`K_n` rather than `Q(zeta_n)`) are
*categorically parallel*: both are `(+1)`-eigenspaces under
complex-conjugation-extending involutions of order 2. They are not the
*same* choice, however — they play structurally different roles in
their respective contexts.

**Asymmetry on the program's side that has no parallel on Gauss's side.**
On Gauss's side, the `(+1)`- and `(-1)`-eigenspaces of complex
conjugation on `C^N` (real and purely-imaginary input data) are equal-
status `R`-vector-space restrictions: same dimension, same closure
properties, the DFT operates on either identically. The choice of
real input is an *input convention*, not a structural commitment — the
algorithm doesn't care whether the symmetry is `X = conj(X)` or
`X = -conj(X)`. On the program's side, the two eigenspaces are
structurally non-corresponding: `K_n` is a subfield, `E_{-1}` is a
non-multiplicatively-closed `K_n`-module. The `(+1)`-eigenspace is
privileged because it is the only multiplicatively-closed half. The
program's choice to work in `K_n` is *forced by closure*; Gauss's
choice to work with real input is not.

So what carries across is the categorical observation: both choices
are fixed-loci of order-2 involutions that, on the shared substructure
`Q(zeta_n) ⊂ C`, agree with complex conjugation. The strong reading
that they are "the same eigenspace choice" overreaches — what is an
arbitrary input convention on Gauss's side is a structural commitment
to the unique multiplicatively-closed half on the program's side.

**The paper's recognition-lag attestation.** The paper attests
qualitatively (p. 270, 271) that the trigonometric formulation hid the
algorithm's index-mapping structure and made it unrecognizable as an
FFT. This is *qualitative* friction; the paper does not quantify it.
The 160-year gap between *Werke* III (1866) and Cooley–Tukey (1965)
is a sum of era factors and choice-specific factors that the
historical record does not separate: posthumous publication delay
(61 years before publication at all), absence of asymptotic-complexity
language until ~1965, absence of a formal compute model until Turing
1936, domain isolation across celestial mechanics / British empirical
physics / signal processing, and pre-database citation conventions.
Era factors absorb the bulk of the headline window. The choice-
specific friction the paper attests is bounded above by something on
the order of "a paper of notational translation" once era factors are
stripped — small in magnitude, and present only in qualitative form
in the paper.

The brief therefore should not lean on "160 years" as a magnitude
prior on the program's `K_n` choice. The honest version: the paper
attests qualitatively that real-trig presentation is recognition-
restricting; magnitude unknown; era factors confound the historical
estimate. The structural identification (§5 proof) does not depend on
this attestation, and the attestation by itself is too weak to carry
program-level decisions about how visible the program's lower-bound
work will be in its own era.

---

## 6. Trust Boundary

### This brief should be cited for

- the date and content of Gauss's 1805 manuscript;
- the explicit claim that Gauss 1805 ≡ Cooley–Tukey decimation-in-frequency
  for real data, with the algebraic comparison verified internally to
  the paper (eq. 4, pp. 269–271);
- the verbatim quote on equivalence (p. 270);
- the principal-discoveries table reproduced from p. 272;
- the documented transmission failures: Hansen 1835 (knew Gauss, didn't
  cite), Burkhardt 1904 (noticed but unnoticed), British 19th-century
  line independent of Gauss;
- the author overlap between this paper and the 1986 Heideman–Burrus
  exact-count paper;
- the chain-of-custody framing for the four FFT-complexity briefs as
  modern descendants of a 1805 origin point;
- the identification of `K_n = Q(cos(2 pi / n))` as the
  `(+1)`-eigenspace of the Galois involution `sigma_{-1}` on
  `Q(zeta_n)` (proven internally to the brief, §5);
- the categorical parallel between the program's `K_n` choice and
  Gauss's 1805 real-input algorithmic choice — both are
  `(+1)`-eigenspaces under complex-conjugation-extending order-2
  involutions, with structurally different roles in their respective
  contexts (§5 connection subsection, anchored on the paper's "real
  data sequence" phrase, p. 271). The brief does **not** support the
  stronger reading that the two are "the same eigenspace choice";
  closure-asymmetry on the program's side breaks that reading.

- the qualitative attestation (paper p. 270, 271) that real-trig
  formulation is recognition-restricting. The brief does **not**
  support a quantitative recognition-lag prior derived from the
  160-year *Werke*-III-to-Cooley–Tukey gap; era factors confound the
  historical magnitude.

### This brief should NOT be cited for

- any complexity result (the paper is historiography; it states `N log N`
  in the introduction but proves nothing about it);
- any cyclotomic or algebraic-degree content (the paper does not enter
  this register);
- any lower-bound material;
- a final answer to the sine vs. cosine question. The eigenspace proof
  in §5 plus the closure-asymmetry observation give a partial answer:
  `K_n` is the unique multiplicatively-closed half, so the program's
  choice is forced rather than selected, and a closure-depth ladder
  does not natively run on `E_{-1}` (which is a `K_n`-module, not a
  field). What remains open: whether anything analogous to closure-
  depth lives on `E_{-1}` as a `K_n`-module structure, and whether
  running the program's analysis on the full `Q(zeta_n)` surfaces
  obstructions invisible from `K_n`. Both require internal program
  computation, not historiography.
- a claim that the inheritance chain is *complete* (the paper itself
  notes "almost one hundred years passed" with the chain partially
  broken; the brief inherits that limitation);
- the inheritance step Winograd 1978 → AFW 1984 (postdates the paper's
  scope; not audited here);
- substantive resolution of why Hansen did not cite Gauss (the paper
  gestures at "reasons which shall be made clear later" but does not
  fully explain them).

### Provenance tag for the program

**Methodologically post-1965 historiography about pre-1882 origin
work.** The paper is a 1985 review. Its substantive *historical claims*
are about pre-1882 mathematics (Gauss 1805, Lagrange 1759, Euler, etc.)
and are accordingly within the L-W-safety window
([memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md)). The
paper's *modern algebraic comparison* (eq. 3–4, the Cooley–Tukey
equivalence proof) uses post-1882 notation but adds no post-1882
content beyond rewriting Gauss in modern indices. The paper functions
for the program as an audit document, not as a load-bearing tool.

---

## Closing Sentence

This brief contributes the inheritance-chain audit from Cooley–Tukey
1965 back to Gauss 1805, with documented transmission failures (Hansen
1835, the British 19th-century line, the 1866–1965 quiet century) and
documented direct continuities (Lagrange → Gauss via Göttingen library
borrowing 1795–1798; Heideman–Burrus historiography overlapping with
Heideman–Burrus technical contribution). It supplies the pre-1965
context the four FFT-complexity briefs sit at the modern end of and
confirms a clean upstream endpoint at 1805 with provenance certified
through *Werke* Vol. III. It does not supply technical content for the
compute-cost branch. The sine vs. cosine question receives a partial
structural answer in §5: the `(+1)`-eigenspace `K_n` is the unique
multiplicatively-closed half of the involution decomposition, so the
program's `K_n` choice is forced by closure rather than selected from
parallel options, and a closure-depth ladder does not natively run on
the `(-1)`-eigenspace as a field. The categorical parallel to Gauss's
real-input choice is structurally weaker than the brief originally
claimed — both are `(+1)`-eigenspaces of order-2
complex-conjugation-extending involutions, but they play different
roles (input convention vs. forced subfield choice). Per
[BNHA/ONE-FOR-ALL.md](BNHA/ONE-FOR-ALL.md), this brief is the
program's provenance-backward audit record for the inheritance the
four modern briefs depend on.
