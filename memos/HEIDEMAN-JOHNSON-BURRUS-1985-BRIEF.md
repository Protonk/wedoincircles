# HEIDEMAN-JOHNSON-BURRUS-1985-BRIEF

Source-extraction memo on M. T. Heideman, D. H. Johnson, & C. S. Burrus,
"Gauss and the History of the Fast Fourier Transform," *Archive for History
of Exact Sciences* 34 (1985), pp. 265–277, communicated by C. Truesdell,
received Feb. 28, 1985 ([sources/gauss-fft-history.pdf](sources/gauss-fft-history.pdf)).

**Why this brief exists.** This is INHERIT-discipline material per
[BNHA/ONE-FOR-ALL.md](BNHA/ONE-FOR-ALL.md): a provenance-backward audit of
the FFT lineage from Cooley–Tukey 1965 back to Gauss's 1805 unpublished
manuscript. The four FFT-complexity briefs already in the repo
([memos/AUSLANDER-FEIG-WINOGRAD-1984-BRIEF.md](memos/AUSLANDER-FEIG-WINOGRAD-1984-BRIEF.md),
[memos/MORGENSTERN-1973-BRIEF.md](memos/MORGENSTERN-1973-BRIEF.md),
[memos/WINOGRAD-1978-BRIEF.md](memos/WINOGRAD-1978-BRIEF.md),
[memos/SCHOENHAGE-STRASSEN-1971-BRIEF.md](memos/SCHOENHAGE-STRASSEN-1971-BRIEF.md))
sit at the modern end of a chain whose origin point this paper documents.

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
[memos/FFT-CYCLOTOMIC-COMPLEXITY.md](memos/FFT-CYCLOTOMIC-COMPLEXITY.md)
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
   shall be made clear later." The "reasons later" are not made entirely
   explicit in the paper but tie to the fact that Gauss's manuscript
   was unpublished at the time of Hansen's 1835 work — so Hansen could
   only have known of the technique through personal communication or
   through Gauss's diary, neither of which would constitute a citable
   source under 19th-century conventions. *The paper records the
   non-citation; it does not fully explain it.*

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
[memos/FFT-CYCLOTOMIC-COMPLEXITY.md](memos/FFT-CYCLOTOMIC-COMPLEXITY.md)
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

### Cooley–Tukey 1965 → Schönhage–Strassen 1971

*Inferred for the program.* The paper does not discuss
Schönhage–Strassen. The standard structural fact (verifiable from the
Schönhage–Strassen brief itself,
[memos/SCHOENHAGE-STRASSEN-1971-BRIEF.md](memos/SCHOENHAGE-STRASSEN-1971-BRIEF.md)):
the Schönhage–Strassen integer-multiplication algorithm uses the FFT
over a finite ring as its inner kernel. The provenance chain therefore
runs Gauss 1805 → ... → Cooley–Tukey 1965 → Schönhage–Strassen 1971,
with the Cooley–Tukey link being the algorithmic ancestor of the FFT
kernel inside Schönhage–Strassen.

### Cooley–Tukey 1965 → Morgenstern 1973

*Inferred for the program.* The paper does not discuss Morgenstern.
Structural fact (verifiable from
[memos/MORGENSTERN-1973-BRIEF.md](memos/MORGENSTERN-1973-BRIEF.md)):
Morgenstern's `Ω((n/2) log_2 n` lower bound for the bounded-coefficient
linear DFT explicitly takes the Cooley–Tukey FFT as the upper-bound
target it almost meets. So Morgenstern's lower bound is downstream of
the existence of Cooley–Tukey as an artifact to be lower-bounded.

### Good 1958 → Cooley–Tukey 1965 → Winograd 1976/78

*From the paper.* Good 1958 is in the principal table at p. 272, and
Winograd 1976 is the table's last entry. The paper notes (p. 266) that
Cooley–Tukey originally referred only to Good. Winograd's prime-factor
algorithm work generalizes Good's, and the paper records Winograd's
contribution as "Use of complexity theory for harmonic analysis" — the
inflection where the chain becomes complexity-theoretic. The brief
[memos/WINOGRAD-1978-BRIEF.md](memos/WINOGRAD-1978-BRIEF.md) thus sits
on the Good → Winograd substrand; through Cooley–Tukey it also touches
the Gauss substrand at the 1965 confluence.

### Winograd 1978 → Auslander–Feig–Winograd 1984

*Outside the paper's coverage.* AFW (1984) postdates the bibliography
[12] of Feb. 1984 marginally, and is published the same year as the
present paper's submission (received Feb. 28, 1985). The paper does
not include AFW in the table or text. Inheritance from Winograd's
prime-factor framework to AFW's tensor-product framework is internal
to the modern algebraic-complexity literature; see
[memos/AUSLANDER-FEIG-WINOGRAD-1984-BRIEF.md](memos/AUSLANDER-FEIG-WINOGRAD-1984-BRIEF.md)
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

### What the paper says about Laplace

**Nothing.** Laplace is not in the paper's text and not in its
reference list [1]–[50]. He is absent from the principal table on
p. 272. He is absent from the dating appendix on pp. 273–274.

Per the user's outside-knowledge cue — that both Gauss and Laplace
attacked this problem family via sines — the paper's silence on
Laplace is a notable omission. Possible reasons (none stated in the
paper):

- The paper deliberately scopes itself to *efficient* (i.e., fewer
  than `O(N^2)` operation) DFT-class algorithms, and Laplace's
  contributions, whatever their substantive content on harmonic
  analysis or perturbation theory, may not include a `O(N log N)`-style
  decomposition.
- Laplace's relevant work may be embedded in larger treatises (e.g.,
  *Mécanique céleste*, *Théorie analytique des probabilités*) where
  the trigonometric-coefficient computation is incidental rather than
  the named result, and so does not surface in the algorithmic-DFT
  bibliography the paper draws on.
- The paper's PFA branch (Thomas, Good, Winograd) is explicitly
  scoped out (p. 266: "Another class of efficient DFT algorithms,
  called prime factor algorithms... is not included in this
  investigation"), and a similar editorial decision may apply to
  Laplace's contributions.

**This brief flags Laplace as a known omission. Its resolution is
outside the paper's scope and outside this brief's audit.**

### Inferred for the program (open question, not resolved)

The program's circle side is currently cosine-only:

```
K_n = Q(cos(2 pi / n)),    [K_n : Q] = phi(n) / 2.
```

This is the load-bearing closure-generator family in
[memos/NATIVE-F-MINIMAL-DEFINITION.md](memos/NATIVE-F-MINIMAL-DEFINITION.md).
The cosine choice tracks the *real subfield* of `Q(zeta_n)`. A
sine-complementary construction would route through `Q(sin(2 pi / n))`
or through `Q(zeta_n)` directly (the full cyclotomic field, not its
real subfield), with degree `phi(n)` rather than `phi(n)/2`.

Whether sine-side or full-cyclotomic-side machinery would surface
*different obstructions* than the program's current cosine-only
analysis is an **open program question**. The Heideman–Johnson–Burrus
historiography does not answer it: the early sine-only DFTs are
basis-restricted by physical problem class, not by algebraic
selection, and the unification at Gauss 1805 is to general cos+sin
(equivalently, the full complex DFT). So the inheritance chain does
not pre-suggest a structural reason to expect cosine-only and
sine-only to differ in algebraic obstruction. *That is not the same as
showing they don't differ.* The program may still find that a
sine-complementary or full-cyclotomic recasting changes which
F-theorem axioms bite.

This is flagged here per the user's cue. It is not pursued. A
resolution would require either (a) a separate Laplace source
extraction from a paper that does cover his harmonic work, or (b) an
internal computation in the program comparing closure-depth
obstructions over `Q(cos)` versus `Q(sin)` versus `Q(zeta)`. Neither
is in scope for this brief.

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
- the absence of Laplace from the paper's text and reference list.

### This brief should NOT be cited for

- any complexity result (the paper is historiography; it states `N log N`
  in the introduction but proves nothing about it);
- any cyclotomic or algebraic-degree content (the paper does not enter
  this register);
- any lower-bound material;
- a final answer to the sine vs. cosine question (the paper does not
  give one, and Laplace is absent from its scope);
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
compute-cost branch and does not resolve the sine vs. cosine question
(Laplace's absence flagged but not investigated). Per
[BNHA/ONE-FOR-ALL.md](BNHA/ONE-FOR-ALL.md), this brief is the
program's provenance-backward audit record for the inheritance the
four modern briefs depend on.
