# 3DT-BRIEF

Standalone reference on the Three Distance Theorem from three linked papers:

1. **Combinatorial** — Valérie Berthé and Christophe Reutenauer, *On the Three Distance Theorem* (2023, 11 pp., full paper read).
2. **Algorithmic** — Vincent Lefèvre, Jean-Michel Muller, and Arnaud Tisserand, *The Table Maker's Dilemma* (1998 research report, §2.2.1 plus setup/results read in context).
3. **Geometric** — Jens Marklof and Andreas Strömbergsson, *The Three Gap Theorem and the Space of Lattices* (2017, 6 pp., full paper read).

Proofs were followed at a reading-not-verifying level. Berthé–Reutenauer's cited Ferenczi–Zamboni theorem and Lefèvre–Muller–Tisserand's cited detailed derivation of the fast algorithm were not separately consulted, so those parts are reported as used or stated in the papers at hand.

## Core Statement

Fix a real number $\alpha$ and an integer $n \ge 1$. Form the points

$$
0,\ \{\alpha\},\ \{2\alpha\},\ \ldots,\ \{(n-1)\alpha\}
$$

on $[0,1)$, sort them as

$$
0=x_0 < x_1 < \cdots < x_{n-1} < 1,\qquad x_n=1,
$$

and let

$$
d_i = x_{i+1}-x_i \qquad (0 \le i \le n-1)
$$

be the successive gap lengths. Then:

1. At most three distinct values occur among the $d_i$.
2. If exactly three distinct values occur, the largest equals the sum of the other two.

This is the Three Distance Theorem, also called the Three Gap Theorem or Steinhaus conjecture. Historically it was proved in 1958–59 by Sós, Surányi, and Świerczkowski, with later proofs by Slater and Halton.

If $\alpha$ is rational, the usual non-repetition hypothesis is that $n$ be smaller than the least positive denominator of $\alpha$.

## Worked Example

Take $\alpha=5/22$ and $n=7$. The multiples $5i \bmod 22$ for $i=0,\dots,6$ are

$$
0,5,10,15,20,3,8.
$$

After sorting:

$$
0,3,5,8,10,15,20.
$$

So the successive gaps on $[0,22]$ are

$$
3,2,3,2,5,5,2.
$$

The distinct distances are $\{2,3,5\}$, with $5=2+3$.

Berthé–Reutenauer encode these distances by letters as follows:

- `a` = the leftmost distance
- `b` = the longest distance
- `c` = the remaining distance

This yields the word `acacbbc`.

Later sections show that this same example can be read in three ways:

- as a word encoding of a discrete interval exchange,
- as an instance of a Euclidean/continued-fraction algorithm on gap lengths,
- as the values of a lattice function on $\Gamma\backslash SL(2,\mathbb{R})$.

## Shared Dictionary Across The Three Papers

- **Orbit points.** The basic orbit is the rotation sequence $\{k\alpha\}$ modulo $1$.
- **Gaps / distances.** These are the successive interval lengths after sorting the orbit points.
- **Distance word.** Reading the gaps from left to right gives a finite word over two or three letters.
- **Return times.** In Berthé–Reutenauer’s rational model, the distances are return times for a cyclic permutation.
- **Euclidean data.** In Lefèvre–Muller, the two shorter gap lengths are updated by a Euclidean-style subtractive loop.
- **Lattice data.** In Marklof–Strömbergsson, the corresponding $F$-values are $r_2$, $s_2$, and $r_2+s_2$ for two distinguished lattice vectors $r,s$; the actual circle gaps are these quantities divided by $N$.

So the same theorem is simultaneously:

- a statement about finite words,
- a statement about a continued-fraction-style algorithm,
- a statement about a function on the space of unimodular lattices.

## Berthé–Reutenauer: The Combinatorial Lens

### Discrete interval exchanges

For a composition $(c_1,c_2,c_3)$ of $n$, split

$$
[[n]]=\{0,1,\dots,n-1\}
$$

into consecutive intervals $I_1,I_2,I_3$ of lengths $c_1,c_2,c_3$, and also into intervals $J_1,J_2,J_3$ of lengths $c_3,c_2,c_1$. The associated **symmetric discrete interval exchange** is the permutation $\sigma$ sending each $I_j$ increasingly onto the opposite block $J_{4-j}$. For three intervals this is

$$
\sigma(i)=
\begin{cases}
i+c_2+c_3 & i\in I_1,\\
i+c_3-c_1 & i\in I_2,\\
i-c_1-c_2 & i\in I_3.
\end{cases}
$$

The permutation is **circular** if it has one cycle. If

$$
\sigma=(0,k_1,\dots,k_{n-1})
$$

in cycle form, its **word encoding** is obtained by replacing each $k_j$ by the letter attached to the interval block containing it.

For the example $(c_1,c_2,c_3)=(2,2,3)$ one gets

$$
\sigma=(0,5,1,6,2,3,4),
$$

and its word encoding over $\{a<b<c\}$ is `acacbbc`.

### Theorem 1: 3DT words come from circular 3-interval exchanges

Berthé–Reutenauer prove:

> If the partition from $(\alpha,n)$ has three distinct distances, then the leftmost interval is not the longest one, and the distance-encoding word is the word encoding of a circular symmetric discrete exchange of three intervals.

Their proof is fully combinatorial.

### Rational case: induce a 2-interval exchange

Write $\alpha=r/N$ in lowest terms and assume $n<N$. Let $q$ be the inverse of $r$ modulo $N$. Then addition by $q$ modulo $N$ gives a circular permutation

$$
\omega(i)=i+q \pmod N
$$

on $[[N]]$. This $\omega$ is itself a circular symmetric exchange of two intervals, with composition $(N-q,q)$.

Now restrict $\omega$ cyclically to $[[n]]$ by deleting all entries $\ge n$ from its cycle. The resulting permutation $\sigma$ is a first-return map on $[[n]]$.

Two key facts drive the proof:

1. **Lemma 2.** The cyclic restriction of a circular 2-interval exchange is a circular 2- or 3-interval exchange.
2. The actual geometric gap lengths are the return times
   $$
   s(i)=\min\{s>0:\omega^s(i)\in [[n]]\}.
   $$

Because $\sigma$ acts by translations on interval blocks $I_1,I_2,I_3$, the return time $s(i)$ is constant on each block. If the three block-values are $s_1,s_2,s_3$, then:

- there are at most three gap lengths,
- and in the three-distance case
  $$
  s_2=s_1+s_3.
  $$

This is the theorem’s “longest equals sum of the other two” identity in purely combinatorial form.

The same argument also shows that the leftmost interval cannot be the longest one: the leftmost interval comes from the first block $I_1$, while the maximal return time is the middle block value $s_2$.

### Irrational case: stabilize the order type

For irrational $\alpha$, choose rationals $\alpha_k\to\alpha$ with denominators larger than $n$. For fixed $n$, the relative order of the points

$$
0,\{\alpha_k\},\dots,\{(n-1)\alpha_k\}
$$

eventually matches the relative order for $\alpha$. Since there are only finitely many possible distance-encoding words of length $n$, one may pass to a subsequence with constant encoding. The rational case then passes to the limit:

- no new gap values appear,
- the encoding stabilizes,
- and the identity “largest = sum of the other two” survives the limit.

So the irrational case is obtained by a compactness / finite-pigeonhole argument, not by invoking an external Diophantine theorem.

### Burrows–Wheeler and perfectly clustering Lyndon words

The paper’s final section records the word-theoretic identification.

- The **Burrows–Wheeler transform** `BW(v)` is the last column of the lexicographically sorted cyclic-rotation matrix of a word $v$.
- A word is **perfectly clustering** if `BW(v)` is decreasing, i.e. made of same-letter runs in reverse alphabet order.
- A word is **Lyndon** if it is strictly smaller than all its proper cyclic rotations.

For the running example, the cyclic rotations of `acacbbc` sort so that

$$
BW(\texttt{acacbbc})=\texttt{cccbbaa}.
$$

So `acacbbc` is perfectly clustering.

The cited Ferenczi–Zamboni theorem states:

> A Lyndon word is perfectly clustering if and only if it is the word encoding of a circular symmetric discrete interval exchange.

Combining this with Theorem 1:

> Every three-distance encoding word is a perfectly clustering Lyndon word.

That is the paper’s clean finite-word avatar of the theorem.

## Lefèvre–Muller–Tisserand: The Algorithmic Lens

### Why the theorem appears in Table Maker’s Dilemma

The Table Maker’s Dilemma asks how hard it is to guarantee correct rounding for elementary functions. In §2.2.1, the authors use the Three Distance Theorem to build a much faster filter for possible worst cases.

The reduction in the paper is:

1. Split the input range into small subdomains where $f$ is well approximated by a line
   $$
   y=ax-b.
   $$
2. Scale the problem so relevant floating-point inputs and outputs become integer grid points.
3. Ask whether some integer grid point lies within a small tolerance $\varepsilon$ of that line.
4. After translating the line, reduce this to the modular question
   $$
   \{b-ax\}<2\varepsilon
   $$
   for some integer $x$ in a bounded range.
5. Read real numbers modulo $1$ as points on a circle. Then the orbit
   $$
   b,\ b-a,\ b-2a,\dots \pmod 1
   $$
   is exactly a rotation orbit with step $-a$ in $\mathbb{R}/\mathbb{Z}$, or equivalently with angle $-2\pi a$ on the geometric circle.

So the fast-filtering question becomes: how small can the gaps in a finite rotation orbit get?

### The stated fast algorithm

The paper then states an algorithm, described as an extension of Euclid’s algorithm and tied to continued-fraction expansion of the slope. Rewritten with readable variable names, it is:

```text
Initialization:
    gamma = {a}
    delta = 1 - {a}
    d = {b}
    u = v = 1

Loop:
    if d < gamma:
        while gamma < delta:
            if u + v >= N: stop
            delta = delta - gamma
            u = u + v
        if u + v >= N: stop
        gamma = gamma - delta
        v = v + u
    else:
        d = d - gamma
        while delta < gamma:
            if u + v >= N: stop
            gamma = gamma - delta
            v = v + u
        if u + v >= N: stop
        delta = delta - gamma
        u = u + v

Return d
```

The paper’s explanation of the state variables is short but clear:

- `gamma` and `delta` are the current lengths appearing in the three-distance picture,
- `u` and `v` are the numbers of arcs of those lengths,
- `u+v` is the current number of intervals / points,
- `d` is the running lower bound for the distance from the line to grid points.

The key point is that the filter works **without explicitly constructing the orbit points**. The orbit structure is compressed into a Euclidean-style update on the two shorter distances.

### What this contributes mathematically

This section of the report is not a proof-heavy treatment of 3DT. It is a use-case:

- 3DT supplies the right finite-state description of a rotation orbit,
- continued fractions enter through the same slope parameter $a$,
- and the theorem becomes a practical algorithm for eliminating most non-worst-case inputs.

The report explicitly says more details of the algorithm are given elsewhere. What is contained here is the reduction, the loop, the interpretation of its variables, and its empirical value.

### Practical outcome reported in the paper

The authors say the second filtering strategy, based on §2.2.1, reproduced the same exponential-function results as their earlier filter while being approximately **150 times faster** in their January 1997 run.

For this brief, the important point is structural rather than historical:

> In this paper, the Three Distance Theorem is not a side remark. It is the engine of a real floating-point filtering algorithm.

That makes 3DT log-side-native in this repository’s terms, not merely a circle-side theorem later imported into log-side questions.

## Marklof–Strömbergsson: The Geometric Lens

### Gap lengths as a lattice function

Marklof–Strömbergsson reformulate the theorem as a statement about unimodular lattices.

Let $\xi_k=\{k\alpha\}$ and let $s_{k,N}$ be the gap from $\xi_k$ to its next neighbor on $\mathbb{R}/\mathbb{Z}$. They rewrite

$$
s_{k,N}
=
\min\{m\alpha+n>0:(m,n)\in\mathbb{Z}^2,\ -k<m\le N-k\}.
$$

Then define

$$
A_N=
\begin{pmatrix}
1 & \alpha\\
0 & 1
\end{pmatrix}
\begin{pmatrix}
N^{-1} & 0\\
0 & N
\end{pmatrix}
\in SL(2,\mathbb{R})
$$

and

$$
F(M,t)=\min\{y>0:(x,y)\in\mathbb{Z}^2M,\ -t<x\le 1-t\}.
$$

Their equation is

$$
s_{k,N}=\frac{1}{N}F(A_N,k/N).
$$

So the three-gap problem becomes the question: for fixed lattice $M$, how many values can the function $t\mapsto F(M,t)$ take on $(0,1]$?

### Proposition 1

They first show $F$ is well defined on

$$
\Gamma\backslash G \times (0,1],\qquad
\Gamma=SL(2,\mathbb{Z}),\ G=SL(2,\mathbb{R}),
$$

because:

- the defining set is nonempty for every $M\in G$ and $t\in(0,1]$,
- and $F(\gamma M,t)=F(M,t)$ for every $\gamma\in\Gamma$.

So $F$ is genuinely a function on the space of unimodular lattices.

### Proposition 2

Their main statement is:

> For every fixed $M\in G$, the function $t\mapsto F(M,t)$ is piecewise constant and takes at most three distinct values. If there are three values, the third is the sum of the first and second.

This is the theorem in lattice language.

### Why exactly three values appear

Let

$$
A=(-1,1)\times \mathbb{R}_{>0}.
$$

Choose:

- $r=(r_1,r_2)\in \mathbb{Z}^2M\cap A$ with minimal positive second coordinate,
- $s=(s_1,s_2)\in (\mathbb{Z}^2M\cap A)\setminus \mathbb{Z}r$ with minimal second coordinate.

Then:

1. The parallelogram with vertices $0,r,s,r+s$ contains no other lattice points.
2. Therefore $r$ and $s$ form a basis of the lattice.
3. Their first coordinates must have opposite signs, so the intervals
   $$
   J_r=(0,1]\cap(-r_1,1-r_1],\qquad
   J_s=(0,1]\cap(-s_1,1-s_1]
   $$
   cover $(0,1]$ in a two-endpieces-plus-middle pattern.

From this they obtain:

$$
F(M,t)=
\begin{cases}
r_2 & t\in J_r,\\
s_2 & t\in J_s\setminus J_r,\\
r_2+s_2 & t\in (0,1]\setminus(J_r\cup J_s).
\end{cases}
$$

So the third value is not merely numerically equal to the sum of the first two. It is literally the value contributed by the lattice vector $r+s$.

In the equal-height special case $s_2=r_2$, the function takes only two values: $r_2$ and $2r_2$.

### What this contributes mathematically

The proof converts the theorem’s familiar identity

$$
d_{\max}=d_1+d_2
$$

into a basis-vector statement in a unimodular lattice.

That is the paper’s contribution:

- it packages 3DT as a function on $\Gamma\backslash SL(2,\mathbb{R})$,
- proves the three-valuedness geometrically,
- and shows that the “sum of the other two” clause is really a lattice-addition fact.

## Three-Way Correspondence

The three papers are talking about the same structure in different languages.

- **Rotation orbit:** $\{k\alpha\}$ modulo $1$.
- **Combinatorial avatar:** a distance word, equivalently a circular symmetric discrete interval exchange.
- **Algorithmic avatar:** a Euclidean / continued-fraction loop on the two shorter current gap lengths.
- **Geometric avatar:** a lattice function $F(M,t)$ whose values are $r_2$, $s_2$, and $r_2+s_2$, so the actual gap lengths are $r_2/N$, $s_2/N$, and $(r_2+s_2)/N$.

The strongest common invariant across the three is:

$$
\text{longest gap} = \text{short gap}_1 + \text{short gap}_2.
$$

In the three papers this appears respectively as:

- a relation among return-time values $s_1,s_2,s_3$,
- the structure maintained by the Euclidean-style update on `gamma` and `delta`,
- the identity $r_2+s_2$ coming from the basis vectors $r,s$.

This is the cleanest synthesis the three-source read supports.

For a nearby but nonidentical procedural problem on the outside-out annulus, see [n-gons/counting/COUNTING-AND-3DT.md](n-gons/counting/COUNTING-AND-3DT.md): the counting word `M_N` also wants a compressed update rule, but it is built from a growing union of rational levels rather than from a fixed rotation orbit.

## Program-Facing Consequences

### 1. CREATI C3 gets a real circle-side reflection identity

The theorem supplies an exact, non-iterative circle-side identity:

$$
d_b(\alpha,n)=d_a(\alpha,n)+d_c(\alpha,n)
$$

whenever three distinct distances occur.

That fills the open reflection-style slot more seriously than trace/inverse trivialities do. Marklof–Strömbergsson strengthens this by showing the identity is not only combinatorial but lattice-geometric:

$$
d_b = \frac{r_2+s_2}{N}.
$$

### 2. The vocabulary is unusually Erasure-compatible

The main objects used here are:

- finite words,
- permutations on $[[n]]$,
- Burrows–Wheeler transforms,
- continued-fraction / Euclidean updates,
- unimodular lattices and $SL(2,\mathbb{Z})$.

None of the three papers requires the repo’s disallowed circle-side machinery such as the Stern–Brocot tree, Farey-as-tree organization, Thomae’s function, or Minkowski’s question-mark function. Continued fractions do appear, but as local arithmetic data, not as a global organizing tree.

### 3. 3DT is both circle-side and log-side

Berthé–Reutenauer and Marklof–Strömbergsson treat the theorem as a rotation/lattice phenomenon. Lefèvre–Muller–Tisserand use the same structure inside a floating-point worst-case search for elementary functions. So in repository terms, 3DT is not just circle-side material that can be exported; it already has a native log-side occurrence.

### 4. The lattice paper gives a positive homogeneous-space example

Here the relevant homogeneous space is $\Gamma\backslash SL(2,\mathbb{R})$, and the theorem works because the lattice function $F$ is well defined there. That gives the repo a concrete positive example of invariant-geometry machinery succeeding on a specific space, in contrast with the no-invariant-measure obstructions that appear elsewhere in the notes.

## Bottom Line

Taken together, the three papers show that the Three Distance Theorem is simultaneously:

- a theorem about finite orbit partitions on the circle,
- a theorem about discrete interval-exchange words,
- a theorem about Euclidean / continued-fraction evolution of gap lengths,
- and a theorem about a three-valued function on the space of unimodular lattices.

For this repository, the most important stable payload is:

1. the exact identity “longest gap = sum of the other two,”
2. the finite-word encoding of that identity,
3. the fact that the same structure also drives a practical floating-point filter,
4. and the lattice reformulation that makes the identity algebraic rather than merely pictorial.
