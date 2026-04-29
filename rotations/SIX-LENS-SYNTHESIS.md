# ROTATIONS-SIX-LENS-SYNTHESIS

Cross-source synthesis of the rotations/ briefs:
[rotations/10-MARTINIS-BRIEF.md](rotations/10-MARTINIS-BRIEF.md) (Avila–Jitomirskaya
spectral) and
[rotations/3DT-BRIEF.md](rotations/3DT-BRIEF.md) (three-distance
combinatorial / algorithmic / geometric), plus adjacent material:
[iso/BECK-1994-BRIEF.md](iso/BECK-1994-BRIEF.md) (probabilistic
Diophantine substitute),
[fft/LANDFALL-PROOF-TEMPLATES.md](fft/LANDFALL-PROOF-TEMPLATES.md)
Template 3 (Gosper computational refusal-of-closure), and the
program-side L-W audit
[rotations/BETA-PI-LW-AUDIT.md](rotations/BETA-PI-LW-AUDIT.md). The
pre-work is at
[rotations/CONTINUED-FRACTIONS-CROSSWALK.md](rotations/CONTINUED-FRACTIONS-CROSSWALK.md).

**Register.** Third register per
[CONTRIBUTING.md](CONTRIBUTING.md) — *cross-source synthesis,
load-bearing, expected to hold up under scrutiny*. Each load-bearing
claim below is grounded in explicit witnesses (specific theorem
statements in the briefs).

**Frame.** The rotations briefs and adjacent material supply six lenses
on one mathematical primitive — the continued-fraction convergents
$p_n/q_n$ of an irrational $\alpha$ and the rotation orbit
$\{k\alpha \bmod 1\}$ they organize. The naive expectation is that the
lenses are alternative methods for one question. **They are not.** Each
lens is sharp on a different operative aspect of the substrate:
arithmetic-type classification, gap-identity export, compressed-orbit
algorithmics, lattice-vector reformulation, Fourier-substitute
discrepancy, and program-consumption interface. The lenses neither nest
nor compete. They substitute on different problem axes. This synthesis
articulates the structural pattern and its operational consequence for
the program's K-H-L-A interim target.

**Lineage closure.**
[iso/THREE-REGISTER-SYNTHESIS.md](iso/THREE-REGISTER-SYNTHESIS.md)
§"Methodological lineage" names 3DT-BRIEF as the program's first
multi-lens synthesis instance and CROSSWALK as the
substrate-index extension; the iso synthesis takes the move to higher
resolution. The present memo closes the loop by promoting the rotations
register to the same load-bearing standing as the iso synthesis.
CROSSWALK remains the index; this memo is the synthesis.

---

## Verdict

Six lenses on the continued-fraction convergent substrate. Five are
external (Avila–Jitomirskaya, Berthé–Reutenauer, Lefèvre–Muller,
Marklof–Strömbergsson, Beck), each sharp on a distinct currency. The
sixth is internal: the program's K-H-L-A consumption interface, which
calls the convergent substrate twice — as classification input
($\beta(\pi) = 0$) and as operational template (the
$(\gamma, \delta, d, u, v)$ compressed-orbit loop).

The sixth lens is not a co-equal external source. It is a consumer.
The CROSSWALK's listing of K-H-L-A alongside the five external lenses
is a category mixing that this synthesis disciplines: external lenses
are read; the program's own use is the reader. Treating the K-H-L-A
interface as program-consumption rather than as a co-source clarifies
the substitution structure below.

The "missing synthesis" the rotations/README.md flags as a structural
gap is the present memo.

## The Unifying Object

Fix an irrational $\alpha \in \mathbb{R}$. The continued-fraction
convergents $p_n/q_n$ are produced by the Euclidean expansion of
$\alpha$. The rotation orbit $\{k\alpha \bmod 1\}$ is the iterate of
$\alpha$ under translation on $\mathbb{T} = \mathbb{R}/\mathbb{Z}$.

Three structural facts pin the substrate:

- **Convergent inequality.**
  $|\alpha - p_n/q_n| < 1/(q_n q_{n+1})$. Pre-1882 in calendar and
  content (Lagrange; Euler).
- **Three-distance.** For every $(\alpha, N)$, the gaps of
  $\{0, \alpha, 2\alpha, \dots, (N-1)\alpha\}$ take at most three
  distinct values; if exactly three, the largest is the sum of the
  other two. Sós–Surányi–Świerczkowski 1958–59.
- **Arithmetic-type cut.**
  $\beta(\alpha) = \limsup \ln(q_{n+1})/q_n$ classifies $\alpha$:
  $\beta = 0$ (Diophantine), $0 < \beta < \infty$ (finite Liouville),
  $\beta = \infty$ (very Liouville). Avila–Jitomirskaya 2009.

Every lens below reads one of these structural facts under a different
rhetorical framing.

## Coordinate Notation

For compactness, each lens is recorded as

```text
(C1, C2, C3, C4, C5, C6)
```

where the six axes are:

1. **C1 — Substrate object handled.** orbit, gap word, lattice
   vectors, $\beta$-cut, semimeasure, transducer state, density-shaped
   bookkeeping.
2. **C2 — Type-handling.** classifies $\alpha$ via $\beta$-cut, assumes
   irrational without classifying, free of $\alpha$-type, restricted to
   rational + limit, etc.
3. **C3 — Identity exported.** $\beta$-cut on the spectrum of the
   almost-Mathieu cocycle, three-distance gap-sum, Euclidean-loop
   invariant, basis-vector $r + s$ reading, Borel–Cantelli almost-every
   threshold, effective Diophantine inequality.
4. **C4 — Native venue.** spectral / continuous, finite-word
   combinatorial / discrete, log-side floating-point,
   lattice-geometric, Fourier / Diophantine, K-H-L-A bookkeeping shell.
5. **C5 — L-W-safety in content** per
   [memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md). pre-1882 /
   post-1882 with content pre-Baker / post-1882 content-untyped.
6. **C6 — Program role.** classification input, identity export,
   candidate machinery, operational precedent, BIND/Erasure-
   compatibility witness, consumption interface.

These coordinates are semantic/role coordinates, not moral rankings. A
lens can be powerful precisely because it discards data another lens
keeps.

## Witness Index

The synthesis below relies on the following source-level witnesses,
each recorded in the corresponding source-extraction brief.

| Tag | Witness | Brief location |
|---|---|---|
| AJ-1 | $\beta(\alpha) = \limsup \ln(q_{n+1})/q_n$ is the operative arithmetic-type parameter for the almost-Mathieu cocycle. | 10-martinis brief §"The Arithmetic Parameter". |
| AJ-2 | $\beta = 0 \Leftrightarrow$ $\alpha$ Diophantine; $0 < \beta < \infty$ finite Liouville; $\beta = \infty$ very Liouville. Threshold $\beta \le |\ln \lambda| \le 2\beta$ is the proof's critical region. | 10-martinis brief §"Strategy In One Sentence". |
| BR-1 | Three-distance words are encodings of circular symmetric discrete 3-interval exchanges; the leftmost interval is not the longest one. | 3DT brief §"Theorem 1". |
| BR-2 | Three-distance words are perfectly clustering Lyndon words (Ferenczi–Zamboni cited). | 3DT brief §"Burrows–Wheeler and perfectly clustering Lyndon words". |
| LMT-1 | Compressed-orbit loop: state $(\gamma, \delta, d, u, v)$ + Euclidean updates + termination by $u + v \ge N$, working without enumerating orbit points. | 3DT brief §"Lefèvre–Muller–Tisserand: The Algorithmic Lens". |
| LMT-2 | The filter is reported $\sim 150\times$ faster than its enumeration counterpart on the table-maker's exponential-function search. | 3DT brief §"Practical outcome reported in the paper". |
| MS-1 | The three gap values are $r_2$, $s_2$, $r_2 + s_2$ for basis vectors $r, s$ of the unimodular lattice $\mathbb{Z}^2 M$; the third is *literally* the second coordinate of $r + s$. | 3DT brief §"Marklof–Strömbergsson: The Geometric Lens". |
| MS-2 | $F(M, t)$ is well-defined on $\Gamma \backslash \mathrm{SL}(2, \mathbb{R}) \times (0, 1]$, $\Gamma = \mathrm{SL}(2, \mathbb{Z})$, with no auxiliary continued-fraction machinery. | 3DT brief §"Proposition 1". |
| BECK | $k$-dimensional Diophantine discrepancy via Fourier + Poisson + Fejér + second moment + Borel–Cantelli; sharp threshold at $(\log N)^k \varphi(\log \log N)$ under $\sum 1/\varphi(n) < \infty$. | iso/BECK-1994-BRIEF brief. |
| GOSPER | 8-variable Möbius-transducer arithmetic; reaches periodicity only for quadratic irrationals; cannot produce log-scale $\psi(m) = \log_2(1 + m)$. The "refusal of finite closure" is the negative content. | fft/LANDFALL-PROOF-TEMPLATES.md Template 3. |
| BPi-1 | Finite irrationality measure $\Rightarrow \beta(\alpha) = 0$. Pre-1882 in content. | rotations/BETA-PI-LW-AUDIT Layer 1. |
| BPi-2 | Mahler 1953 / Hata 1993 / Salikhov 2008 establish finite $\mu(\pi)$ by Hermite–Padé auxiliary-function arithmetic, no Baker / Gelfond–Schneider / Thue–Siegel–Roth content. L-W-safe in content. | rotations/BETA-PI-LW-AUDIT Layer 2. |
| KHL-A | $\beta(\pi) = 0$ places $\pi$ Diophantine; the K-H-L-A Step 5 empirical-to-density proxy uses LMT-1 as one-dimensional operational template. | KRAFT-BUDGET-ONE-DIMENSIONAL §"Operational precedents". |

## The Six Lenses

| Lens | C1 | C2 | C3 | C4 | C5 | C6 |
|---|---|---|---|---|---|---|
| Avila–Jitomirskaya | $\beta$-cut on convergent growth | classifies $\alpha$ | $\beta$-cut governs spectrum-of-cocycle (Cantor) and the three-region threshold $\beta \le \|\ln \lambda\| \le 2\beta$ | spectral / continuous | post-1882; β-parameter content-untyped, β = 0 derived from finite μ inherits no post-Baker content (per BPi-2) | classification input |
| Berthé–Reutenauer | gap word + permutation | irrational by limit | three-distance gap-sum $d_b = d_a + d_c$; Lyndon / BWT avatar | finite-word combinatorial | post-1882; combinatorial; BIND-safe | identity export + BIND-compatibility witness |
| Lefèvre–Muller | $(\gamma, \delta, d, u, v)$ state | irrational | Euclidean-loop invariant; orbit handled without enumeration | log-side floating-point | post-1882; Euclidean / classical CF content; pre-Baker | operational precedent (K-H-L-A Step 5) |
| Marklof–Strömbergsson | basis vectors $r, s$ of $\mathbb{Z}^2 M$ | irrational | $F(M, t) \in \{r_2, s_2, r_2 + s_2\}$ — third value *literally* second coord. of $r + s$ | lattice-geometric | post-1882; lattice / homogeneous-space; BIND-safe | identity export (basis-vector reading) |
| Beck 1994 | semimeasure / Fourier substitute | $k$-dim general $\alpha$ | $(\log N)^k \varphi(\log \log N)$ threshold under $\sum 1/\varphi < \infty$ | Fourier / Diophantine | post-1882; audited at iso/THREE-REGISTER-SYNTHESIS Claim 2 §2.3; L-W-safe | candidate machinery (higher-dim Fourier substitute) |
| K-H-L-A Step 5 | $\pi$-CF + density bookkeeping | reads $\beta(\pi) = 0$ as input | effective $C$ in $\|q\pi - p\| \gg q^{-C}$ (target, not theorem) | K-H-L-A bookkeeping shell | program-internal; consumes audited externals | consumption interface |

The first five rows are external readings of the substrate. The sixth
is the program's consumption interface, which calls rows 1
(classification), 3 (operational precedent), and indirectly 5
(Fourier-substitute methodology) to deliver an effective constant whose
existence remains open.

The Gosper transducer is read here as a **substrate boundary marker**
rather than a sixth external lens: it certifies that finite-closure
arithmetic on $p_n/q_n$ does not extend to log-scale
$\psi(m) = \log_2(1 + m)$. Its content is negative and is recorded
under L-W-safety §2.3 below rather than as its own row.

---

## Claim 1 — Six Lenses, One Substrate, No Hierarchy

**Statement.** The six lenses do not nest. They substitute on different
problem axes, and no lens is a strengthening of another.

| Lens | Sharp on | Loose on |
|---|---|---|
| Avila–Jitomirskaya | $\beta$-cut classification ($\beta(\alpha)$ determines the spectrum-side regime exactly) | identity export from a particular $\alpha$ (no closed-form gap data) |
| Berthé–Reutenauer | $d_b = d_a + d_c$ identity and its Lyndon avatar | arithmetic-type classification (uses irrationality but not $\beta$) |
| Lefèvre–Muller | compressed-orbit algorithmics (the Euclidean loop achieves filtering without enumerating points) | analytic / spectral content |
| Marklof–Strömbergsson | basis-vector identity (third gap is *literally* $r_2 + s_2$, not numerically equal) | algorithmic content (lattice description is not constructive in LMT's sense) |
| Beck 1994 | almost-every Diophantine discrepancy in dimension $k \ge 2$ | pointwise bound for specific $\alpha$ |
| K-H-L-A Step 5 | bookkeeping interface (Kraft + Aitchison + Erdős–Turán–Koksma assembly) | the empirical-to-density proxy itself remains open |

### 1.1 — How the lenses substitute

External lenses substitute on different axes, not in a substitution
chain. Witness pairs:

- **AJ ↔ BR / MS.** AJ reads $p_n/q_n$ through $\beta$; BR/MS read the
  same convergents through gap-words and lattice vectors. Translation:
  $\beta$ controls *how fast* the convergents grow; the gap-word and
  lattice descriptions encode *what shape* a finite truncation
  produces. The two readings are orthogonal — knowing $\beta(\alpha)$
  does not give the gap-word; knowing the gap-word for fixed $N$ does
  not give $\beta$.
- **BR ↔ MS.** Berthé–Reutenauer's word encoding and
  Marklof–Strömbergsson's lattice $F$-function describe the same three
  values, but BR's combinatorial structure does not preserve which
  lattice basis underlies the example, while MS's basis-vector reading
  does not preserve the Burrows–Wheeler / Lyndon structure that BR
  exposes. The two readings preserve different invariants of the same
  partition.
- **LMT ↔ MS.** Both can compute the gap structure for given
  $(\alpha, N)$. LMT compresses by Euclidean updates; MS computes via
  lattice point search. The cost models differ — LMT is genuinely fast
  (LMT-2 reports a $\sim 150\times$ speedup over enumeration), MS gives
  no algorithmic content but generalizes to higher-dimensional
  invariants.
- **AJ ↔ Beck.** Both are arithmetic-type sensitive; AJ classifies
  $\alpha$ via $\beta$, Beck delivers an almost-every threshold over
  $\alpha$-space. AJ is sharp pointwise but only on specific $\alpha$
  for which $\beta$ is known; Beck is sharp on the measure side but
  blurry pointwise. Complementary, not competing.
- **CF / Beck.** Beck explicitly *substitutes* Fourier + Borel–Cantelli
  for one-dimensional CF control in dimension $k \ge 2$. The
  substitution preserves the Diophantine-discrepancy content that CFs
  carry in $k = 1$.

### 1.2 — Operational consequence

The program cannot pick "the best lens" and discard the others.
K-H-L-A Step 5 invokes AJ for classification and LMT for operational
template; the iso/THREE-REGISTER-SYNTHESIS Claim 2 §2.3 audit invokes
BR for BIND/Erasure-compatibility comparison;
fft/HEIDEMAN-JOHNSON-BURRUS-1985 §5 invokes MS for basis-vector
precedent. Each interface uses the lens that is *sharp on the axis the
program needs*. A naive single-lens import would lose currency on every
axis except one.

This is the same pattern iso/THREE-REGISTER-SYNTHESIS articulates for
the isoperimetric gap, transposed to the rotation-orbit substrate. The
substrate differs (gap vs. orbit), but the non-interchangeability is
structural in both cases.

---

## Claim 2 — L-W-Safety Content Map

**Statement.** Five of the six lenses are L-W-safe in content under
[memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md)'s
content-not-calendar criterion. The sixth (K-H-L-A) is the consumer,
not a source, so its L-W-safety is inherited from the externals it
calls and from the audit of [paper/IMPOSSIBILITY-OUTLINE.md](paper/IMPOSSIBILITY-OUTLINE.md)
itself.

### 2.1 — Per-lens audit

| Lens | Calendar | Content | Verdict |
|---|---|---|---|
| Avila–Jitomirskaya | post-1882 (2009) | spectral content; $\beta$ parameter itself is content-untyped; the *value* $\beta(\pi) = 0$ derived from finite $\mu(\pi)$ does not inherit post-Baker content (see §2.2) | The $\beta$-cut definition is consumed, not the cocycle / Cantor content. Definition is content-untyped. |
| Berthé–Reutenauer | post-1882 (2023) | combinatorial: orbit-words, permutations, Lyndon, Burrows–Wheeler. No Stern–Brocot, no Thomae, no Minkowski $?$. | BIND-safe in content (worked precedent under OLD-TIME-RELIGION). |
| Lefèvre–Muller | post-1882 (1998) | Euclidean-style subtractions on slope; classical CF arithmetic content. | L-W-safe; pre-Baker content. |
| Marklof–Strömbergsson | post-1882 (2017) | basis vectors of a unimodular lattice; $\Gamma \backslash \mathrm{SL}(2, \mathbb{R})$ homogeneous space; no transcendence-theory content. | BIND-safe in content. |
| Beck 1994 | post-1882 (1994) | Fourier + Poisson + Fejér + second moment + Borel–Cantelli. Audited at [iso/THREE-REGISTER-SYNTHESIS](iso/THREE-REGISTER-SYNTHESIS.md) Claim 2 §2.3. | L-W-safe. |
| Gosper transducer | content pre-1882 (CF arithmetic) | 8-variable Möbius transducer; reaches periodicity only for quadratic irrationals; *cannot* produce $\psi(m) = \log_2(1 + m)$ on the log side. | L-W-safe; the content is *negative* (refusal of finite closure on $\psi$). |

### 2.2 — $\beta(\pi) = 0$ audit closure

[rotations/BETA-PI-LW-AUDIT.md](rotations/BETA-PI-LW-AUDIT.md)
certifies the chain
`Lambert 1761 + Mahler 1953 / Hata 1993 / Salikhov 2008 + classical CF
algebra ⟹ β(π) = 0` as L-W-safe in content. Layer 1 (the implication
"finite $\mu \Rightarrow \beta = 0$") is pre-1882. Layer 2 (the input
"finite $\mu(\pi)$") cites Hermite–Padé auxiliary-function
arithmetic — pre-Baker content under the audit criterion. Cheapest
L-W-safe witness: Mahler 1953.

The audit closes a parallel-reading flag at FIRST-PROOF Lemma A
bullet 1; it does not derive a new $\mu(\pi)$ bound, and does not
adjudicate K-H-L-A's open question of whether a Kraft–Parseval
auxiliary can re-derive an effective $\mu(\pi)$ without Hermite–Padé
content.

### 2.3 — Trust gap on the Layer 2 sources

Mahler 1953, Hata 1993, Salikhov 2008 are not in `sources/`. The audit
explicitly does not paragraph-level re-read; it relies on
reception-level method classification. Compare with
[iso/HURWITZ-1902-LW-AUDIT.md](iso/HURWITZ-1902-LW-AUDIT.md), which
*did* paragraph-level re-read because its source PDF was local. The
$\beta(\pi)$ Layer-2 audit is structurally weaker by accident of source
availability. Acquiring at minimum Mahler 1953 (cheapest L-W-safe
witness) would symmetrize the audit with the iso/HURWITZ-1902 audit.
Open slot **C** below.

### 2.4 — The Gosper boundary and why it counts as positive content

GOSPER's verdict is "refuses finite closure on $\psi(m) = \log_2(1+m)$."
This is L-W-safe because its content is the *boundary* of
finite-closure CF arithmetic, not a smuggled transcendence statement.
It records where the substrate stops carrying its own weight, which is
a bookkeeping fact about the substrate, not a transcendence theorem
about $\pi$.

The boundary marker matters for the K-H-L-A bookkeeping shell: it
disciplines the program against expecting CF arithmetic to deliver
$\psi$-side content under finite closure. Whatever the
empirical-to-density proxy at K-H-L-A Step 5 ends up being, it cannot
be a CF algorithm in the Gosper sense.

---

## Claim 3 — Disambiguating CREATI C3

**Statement.** The 3DT brief's claim that the $d_b = d_a + d_c$
identity "fills the open reflection-style slot" in CREATI C3 is
methodologically suggestive but operationally loose. CREATI C3's open
slot is about *trace* identities under involutions on circle rotations;
the 3DT identity is a *gap-length sum*. These are different objects.

### 3.1 — The CREATI C3 open slot, restated

[BNHA/triad/Creati/CREATI-THE-CIRCLE.md](BNHA/triad/Creati/CREATI-THE-CIRCLE.md)
C3 frames the question as:

> Reflection → circle side (open slot). Does trace on the circle admit
> a non-trivial reflection identity (some involution $\sigma$ with
> $\mathrm{trace}(R_n) + \mathrm{trace}(R_{\sigma(n)}) =$ closed form)?
> The transpose-trivial candidates fail; whether a richer reflection
> exists is an open enumeration question.

This is an identity on $\mathrm{trace}(R_n) = 2 \cos(2\pi/n)$ under an
involution on $n$. It is a circle-side question about the iteration
substrate, not a question about gap lengths.

### 3.2 — What 3DT actually delivers

The Berthé–Reutenauer / Marklof–Strömbergsson identity is

```text
d_b(α, N) = d_a(α, N) + d_c(α, N)
```

whenever three distinct gap lengths occur. The MS lattice reading
sharpens this to *literally* "third gap = second coordinate of $r + s$"
for basis vectors $r, s$ of the lattice $\mathbb{Z}^2 M$. This is
non-iterative and exact. But it lives on the *gap-length* substrate of
a finite rotation orbit, not on the *trace-of-rotation-matrix*
substrate.

### 3.3 — Methodological cousin, not slot-filler

The 3DT identity is what the program's BIND/Erasure-compatible
vocabulary *can deliver* on the circle side. CREATI C3's open slot is
what the program *would like* on the trace-iteration side. They are
sibling open questions, not the same question.

The downgrade: the 3DT brief's Program-Facing Consequence #1 should be
read as "3DT supplies a non-iterative gap-sum identity on circle
rotations, sibling-open to CREATI C3's trace-reflection slot," not as
"fills" the slot. Implementation note: pending small clarifying edit at
[rotations/3DT-BRIEF.md](rotations/3DT-BRIEF.md) §"Program-Facing
Consequences" #1; this synthesis records the disambiguation. The
trace-reflection open slot remains open. Whether it is *answerable* is
the right next question for CREATI C3 — Open Slot **F** below.

---

## Claim 4 — Continued-Fraction Convergents Are BIND-Compatible

**Statement.** All five external lenses use continued-fraction
convergents (or directly equivalent arithmetic) without invoking the
disallowed circle-side machinery. This is a worked precedent for
[memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md)'s
content-not-calendar criterion at the rotations register, and it is the
load-bearing assumption that lets K-H-L-A Step 5 consume the LMT loop.

### 4.1 — The forbidden list

[BNHA/triad/PLUS_ULTRA.md](BNHA/triad/PLUS_ULTRA.md) records the
discipline rule that admits CF computation while forbidding
disallowed circle-side organizing frames:

- Stern–Brocot tree as a global organizing frame.
- Farey-as-tree organization.
- Thomae's function.
- Minkowski's question-mark function $?(x)$.

### 4.2 — What the lenses use

| Lens | Uses | Notably does not use |
|---|---|---|
| Avila–Jitomirskaya | $\beta = \limsup \ln(q_{n+1})/q_n$ directly on convergents | no Stern–Brocot tree |
| Berthé–Reutenauer | finite words, permutations on $[\![n]\!]$, Burrows–Wheeler, Lyndon | no Stern–Brocot, no Thomae, no Minkowski $?$ |
| Lefèvre–Muller | Euclidean-style subtraction on slope $a$ | no global tree organization |
| Marklof–Strömbergsson | basis vectors of unimodular lattice; $\Gamma \backslash \mathrm{SL}(2, \mathbb{R})$ | no Farey-as-tree |
| Beck 1994 | Fourier + Poisson + Fejér + Borel–Cantelli | no continued fractions at all in $k \ge 2$; one-dimensional CF data is *substituted* by Fourier-side machinery |

CFs appear as local arithmetic data, not as a global organizing tree.
This is the BIND/Erasure-compatibility distinction the program's
discipline requires.

### 4.3 — Why this matters for K-H-L-A Step 5

K-H-L-A consumes the LMT loop as operational precedent. The Step 5
interface is therefore inheriting the BIND-compatibility witness from
LMT — running CF-style updates without recruiting a global tree
organization is exactly what the K-H-L-A bookkeeping shell needs. The
L-W-safety audit at iso/THREE-REGISTER-SYNTHESIS Claim 2 §2.3 (Beck)
and the BIND-compatibility witness here jointly clear the rotations
side of the K-H-L-A pipeline. The substrate is admissible. What
remains open is the empirical-to-density proxy itself, which is a
K-H-L-A-internal construction question, not a rotations-register
audit question.

---

## Synthesis: Six Lenses, Four Operational Roles

The six lenses partition into four operational roles relative to the
program:

1. **Classification.** Avila–Jitomirskaya provides the $\beta$-cut.
   The program reads $\beta(\pi) = 0$ via the BPi audit and proceeds.
2. **Identity export.** Berthé–Reutenauer + Marklof–Strömbergsson
   deliver the three-distance gap-sum and its lattice basis-vector
   reading. Cited at
   [n-gons/counting/COUNTING-AND-3DT.md](n-gons/counting/COUNTING-AND-3DT.md)
   (methodological-only; the outside-out construction adjoins rational
   levels rather than appending one orbit point) and
   [fft/HEIDEMAN-JOHNSON-BURRUS-1985-BRIEF.md](fft/HEIDEMAN-JOHNSON-BURRUS-1985-BRIEF.md)
   §5 (methodological-only; cyclotomic decomposition has the same
   basis-vector shape but the cyclotomic-depth lift is open). The
   CREATI C3 fit is sibling-open, not slot-filler (Claim 3).
3. **Operational template.** Lefèvre–Muller delivers the
   $(\gamma, \delta, d, u, v)$ compressed-orbit loop. Cited as K-H-L-A
   Step 5 operational precedent. Currently rhetorical-not-executable
   (Open Slot **A**); a Sage instantiation would close that gap.
4. **Substitute / refusal.** Beck substitutes Fourier for CF in
   dimension $k \ge 2$. Gosper refuses finite closure on $\psi$ at the
   one-dimensional log side. Both are methodological substitutes that
   mark where the CF substrate stops carrying its own weight.

The CROSSWALK's six-perspective listing is the index of these roles.
This memo is the structural reading.

---

## Open Slots Inventory

The synthesis exposes six concrete gaps in operational uptake. Listed
in approximate ascending order of cost.

### A. LMT loop instantiation — *discharged*

The $(\gamma, \delta, d, u, v)$ loop is in 3DT-BRIEF as pseudocode and
is cited at KRAFT-BUDGET-ONE-DIMENSIONAL §"Operational precedents" as
the K-H-L-A Step 5 template. **Implementation:**
[corners/lefevre_muller_pi.sage](corners/lefevre_muller_pi.sage). The
script runs the loop on $\pi$ for $N$ up to $10^7$ and verifies four
properties:

1. *Termination.* The loop terminates on $\alpha = \pi$ for every tested
   $(b, N)$.
2. *Compression.* Total operations scale sublinearly with $N$: 8 ops at
   $N = 10$, 330 ops at $N = 10^7$ — a $\sim 30{,}000\times$ savings
   over brute-force orbit enumeration. Op-count jumps coincide with
   traversal of $\pi$'s large CF partial quotients (notably the 292
   between $q_3$ and $q_4$).
3. *Lower-bound semantics.* $d_{\text{LMT}} \le d_{\text{brute}}(\text{first } N)$
   holds in all cases. Tight at small $N$; $\sim 10^{-6}$ relative
   floating-point drift at $N \sim 10^5$ from accumulated subtractions.
4. *CF correspondence.* $(u + v)$ at outer-iteration checkpoints
   lands *exactly* on $\pi$'s CF convergent denominators
   $q_n = 1, 7, 106, 113, 33102, 33215, 66317, 99532, 265381, \dots$.
   The loop terminates at the first $q_n \ge N$.

The K-H-L-A Step 5 operational-precedent citation is now demonstrated
rather than rhetorical. The "memory cost: 5 floats independent of $N$;
update cost: $\sim 330$ ops at $N = 10^7$" empirical witness is the
density-shaped bookkeeping the K-H-L-A pipeline assumed without
exhibiting.

### B. $\beta$-classification beyond $\pi$

The 10-martinis cut $\beta = 0$ / $0 < \beta < \infty$ /
$\beta = \infty$ is precise; only $\pi$ is placed in the program. Other
substrate-relevant $\alpha$ — $\log 2$, $\log 3$, $\zeta(3)$,
Euler–Mascheroni $\gamma$, $e$ — are not classified in any rotations/
memo. A short audit with citations would expose which substrate-
adjacent $\alpha$ the program can also place Diophantine-side without
taking a fresh transcendence-theory dependency.

### C. Mahler / Hata / Salikhov source acquisition

Local PDFs of the three irrationality-measure papers are not in
`sources/`. The $\beta(\pi) = 0$ audit Layer 2 explicitly does not
paragraph-level re-read. Acquiring Mahler 1953 (cheapest L-W-safe
witness) would symmetrize the audit with the iso/HURWITZ-1902 audit,
which did paragraph-level re-read.

### D. CREATI C3 trace-reflection enumeration — *discharged (negatively)*

The slot remains open after the disambiguation in Claim 3. The right
next question is whether a non-trivial trace-reflection identity exists
*at all*, or whether the obstruction is structural. **Implementation:**
[corners/creati_c3_reflection.sage](corners/creati_c3_reflection.sage)
enumerates the natural involution families (additive `σ(n) = c − n`,
the unique `1/n + 1/σ(n) = 1/2` Möbius involution `σ(n) = 2n/(n − 2)`,
multiplicative `σ(n) = c/n`) and tests `f_σ(n) = trace(R_n) +
trace(R_σ(n))` for closed-form structure on integer-valued domains in
`n ∈ [3, 60]`.

Verdict: **no non-trivial `σ`-involution on the `n`-parameter
produces a closed-form reflection identity over an infinite domain.**
The unique informative witness is `f_σ ≡ 0` on `{3, 4, 6}` for
`σ(n) = 2n/(n − 2)`, which is the equilateral-triangle / regular-
hexagon coincidence and has finite domain. By Niven, no involution
extending beyond the Niven set can give a rational closed form across
multiple `n`, since `cos(2π/n)` for `n ∉ {1, 2, 3, 4, 6}` lies in a
non-trivial cyclotomic subfield with no algebraic relation forcing
the sum into `ℚ`.

Memo: [BNHA/triad/Creati/CREATI-C3-REFLECTION-ENUMERATION.md](BNHA/triad/Creati/CREATI-C3-REFLECTION-ENUMERATION.md).
The kind-mismatch (log side reflection-rigid, circle side
iteration-rigid) is now a **structural obstruction**, not an open
question. CREATI C3's open slot is upgraded to a closed obstruction.

### E. Marklof–Strömbergsson basis-vector reading vs. cyclotomic $K_n$

[fft/HEIDEMAN-JOHNSON-BURRUS-1985-BRIEF.md](fft/HEIDEMAN-JOHNSON-BURRUS-1985-BRIEF.md)
§5 cites MS as "rotations-layer precedent" for the closure-side
decomposition $\mathbb{Q}(\zeta_n) = K_n \oplus K_n \cdot 2i \sin(2\pi/n)$.
The cross-reference is methodological-only. MS-1's "third value =
literally $r_2 + s_2$" identity has the same basis-vector shape;
whether the closure-depth statement on cyclotomic factor decompositions
is genuinely strengthened by the MS reading is open.

### F. Lyndon / BWT prefix-free ledger pivot

Cited as candidate machinery at four memos:
[BNHA/VILLAINS-ANSWERED.md](BNHA/VILLAINS-ANSWERED.md) §#5,
[memos/LEDGER-PIVOT-SEARCH.md](memos/LEDGER-PIVOT-SEARCH.md),
[fft/FOUR-FRAMEWORK-SYNTHESIS.md](fft/FOUR-FRAMEWORK-SYNTHESIS.md),
[fft/PROVENANCE-AND-TRANSFERABILITY.md](fft/PROVENANCE-AND-TRANSFERABILITY.md)
§3.1. The 3DT brief poses the open task: "test whether the Lyndon/BWT
avatar can be promoted to a prefix-free ledger coupled to `V_cert`'s
certification costs." Never attempted. Higher cost than (A)–(E);
riskier; bigger payoff if it works.

---

## Trust Boundary

This memo may be cited for:

- the six-lens coordinate organization of the rotations register;
- the substitution structure (Claim 1) and the L-W-safety map (Claim 2);
- the disambiguation of the 3DT identity vs. CREATI C3 (Claim 3);
- the BIND-compatibility witness from the rotations register (Claim 4);
- the four operational-roles partition;
- the open-slot inventory.

It should not be cited as proving:

- a new $\mu(\pi)$ bound;
- an effective constant $C$ in $|q\pi - p| \gg q^{-C}$ (target, not theorem; remains open at K-H-L-A Step 5);
- a CREATI C3 trace-reflection identity (the slot remains open; Open Slot **D**);
- a Lyndon/BWT prefix-free ledger (open task; Open Slot **F**);
- a cyclotomic-depth lift of MS's basis-vector reading (open task; Open Slot **E**);
- an extension of $\beta$-classification beyond $\pi$ (open task; Open Slot **B**).

The audit verdicts in §2 inherit their conditional dependencies from
the underlying briefs and from
[memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md). The
$\beta(\pi) = 0$ Layer-2 audit is conditional on
reception-level method classification of Mahler 1953 / Hata 1993 /
Salikhov 2008 (Open Slot **C**). Per
[fft/PROVENANCE-AND-TRANSFERABILITY.md](fft/PROVENANCE-AND-TRANSFERABILITY.md)'s
discipline, the cited sources are referenced for what their methods
establish, not for content beyond that.
