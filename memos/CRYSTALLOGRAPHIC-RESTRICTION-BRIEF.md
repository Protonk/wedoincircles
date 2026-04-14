# CRYSTALLOGRAPHIC-RESTRICTION-BRIEF

Standalone reference on John Bamberg, Grant Cairns, and Devin Kilminster, *The Crystallographic Restriction, Permutations, and Goldbach's Conjecture*, American Mathematical Monthly 110 (2003), 202–209.

Full paper read. Proofs were followed at a reading-not-verifying level. Hiller's cited recursion formula and the Richert/Bertrand ingredient inside Proposition 3 were not independently audited here, so claims below are limited to what the paper states and uses.

## Core Theorem

For each dimension $n$, let

$$
\operatorname{Ord}_n=\{m\ge 1 : \text{some } n\times n \text{ integer matrix has order } m\}.
$$

Equivalently, $\operatorname{Ord}_n$ is the set of rotational symmetry orders realizable by $n$-dimensional Euclidean lattices.

The paper’s central arithmetic invariant is the function $\psi$, defined on prime powers by

- $\psi(1)=0$ and $\psi(2)=0$,
- $\psi(2^r)=2^{r-1}$ for $r\ge 2$,
- $\psi(p^r)=p^r-p^{r-1}=\varphi(p^r)$ for odd prime $p$ and $r\ge 1$,
- and for coprime factors,
  $$
  \psi\!\left(\prod p_i^{r_i}\right)=\sum \psi(p_i^{r_i}).
  $$

The main classification is:

> **Theorem 1.** $\operatorname{Ord}_n=\{m\in\mathbb{N}:\psi(m)\le n\}$.

So an $m$-fold rotation is crystallographic in $n$-dimensional Euclidean space if and only if $\psi(m)\le n$.

The key thing to remember is that $\psi$ is **additive on prime-power parts**, unlike Euler’s $\varphi$, which is multiplicative on coprime factors.

## Immediate Consequences

Basic values:

- $\psi(1)=0$
- $\psi(2)=0$
- $\psi(3)=2$
- $\psi(4)=2$
- $\psi(5)=4$
- $\psi(6)=2$
- $\psi(7)=6$

From these:

- $\operatorname{Ord}_2=\{1,2,3,4,6\}$, the classical planar crystallographic restriction.
- $\operatorname{Ord}_3=\operatorname{Ord}_2$.
- $\operatorname{Ord}_4$ adds $5,8,10,12$.

The parity fact is structural:

> $\psi(m)$ is always even.

Hence

$$
\operatorname{Ord}_{2k+1}=\operatorname{Ord}_{2k}.
$$

Odd dimensions add nothing. New crystallographic orders appear only when the ambient dimension passes to the next even value.

## The Symmetric-Group Analog

The paper defines a second additive arithmetic function:

- $S(1)=1$,
- for $m=\prod p_i^{r_i}>1$,
  $$
  S(m)=\sum p_i^{r_i}.
  $$

Then:

> **Theorem 2.** $S_n$ contains an element of order $m$ if and only if $S(m)\le n$.

This is parallel in shape to Theorem 1, but the function is different. $\psi$ sums prime-power totients; $S$ sums prime powers themselves.

The paper also notes a coupling between the two settings: for products $m=p_1\cdots p_k$ of distinct odd primes, one has a dimension shift relating $\operatorname{Ord}_n$ and $S_{n+k}$. That is not the main theorem, but it is the paper’s clearest bridge between the lattice and permutation sides.

## The Goldbach Theorem In The Paper

The paper’s most striking side result is:

> **Theorem 3.** The following are equivalent:
>
> 1. Strong Goldbach: every even integer $n>4$ is the sum of two distinct odd primes.
> 2. For every even $n\ge 6$, there is an $n\times n$ integer matrix of order $pq$ for distinct odd primes $p,q$, and no smaller integer matrix of that order.
> 3. For every even $n>6$, there is an element of $S_n$ of order $pq$ for distinct odd primes $p,q$, and no such element in $S_{n-1}$.

The arithmetic reason is short:

$$
\psi(pq)=(p-1)+(q-1),
$$

so the condition $\psi(pq)\le n$ is equivalent to $p+q\le n+2$.

This matters for us, but with a clear boundary:

- the paper proves a safe surjectivity statement for $\psi$ onto the even nonnegative integers using **any number** of distinct odd primes;
- the two-prime version is Goldbach-equivalent and should not be used as a program premise.

## Structural Facts Worth Keeping

### $\psi$ is surjective onto the even nonnegative integers

Proposition 3 shows:

> For every even $n\ge 2$ there exist distinct odd primes $p_1,\dots,p_k$ such that
> $$
> \psi(p_1\cdots p_k)=n.
> $$

This is proved by induction using Bertrand’s postulate. It is the safe statement to cite when we need “every even value is hit.” It is not Goldbach.

### $\psi$ and $\varphi$ agree early and diverge later

Examples:

- $\psi(12)=4$ and $\varphi(12)=4$,
- $\psi(15)=6$ while $\varphi(15)=8$,
- $\psi(30)=6$ while $\varphi(30)=8$.

The disagreement is systematic on products of distinct odd primes. This is the arithmetic feature that makes $\psi$ useful here and prevents it from being confused with ordinary totient data.

### The paper gives a computable recursion

Hiller’s formula (quoted as formula (1)) expresses $\operatorname{Ord}_n$ as a disjoint union indexed by the 2-adic valuation of the order. The paper tabulates the resulting sets through $n=24$.

For memo purposes, the important point is not the exact recursion but the consequence:

- Table 1 is already a ready-made saturation table for the crystallographic orders,
- and it can be read equivalently as the layers
  $$
  \psi^{-1}\{n\}=\operatorname{Ord}_n\setminus \operatorname{Ord}_{n-1}.
  $$

### The paper records numerical growth evidence

Figure 2 suggests

$$
\frac{\log\log|\operatorname{Ord}_n|}{\log n}\approx 0.475
$$

for $n$ up to $40{,}000$, so $|\operatorname{Ord}_n|$ grows roughly like $n^c$ with $c$ just under $1/2$.

This is numerical evidence reported by the paper, not an asymptotic rederived here. The rigorous asymptotics live in later references the paper cites.

## Program-Facing Exports

### 1. This is the authoritative source for $\psi$

If we cite

$$
\psi(m)\le n \iff \text{$m$-fold rotational symmetry is crystallographic in dimension $n$},
$$

this is the source.

It is also the source for the exact additive definition of $\psi$ that the triad docs and Inscription-level circle-side notes should use.

### 2. It sharpens the circle-side zero regime

In dimension $2$ one gets exactly

$$
\{1,2,3,4,6\},
$$

which is the same set that appears in Niven’s theorem for integer traces. Higher-dimensional crystallographic allowances then enlarge this set in a controlled arithmetic way, always by even-dimensional jumps.

So the paper supplies the correct “beyond Niven” crystallographic ladder.

### 3. It gives PERMEATE a ready-made saturation table

Table 1 is essentially the first half of PERMEATE Leg 2 already done.

In particular, the first prime outside the log-side `{2,3,5}` support is reflected immediately:

- $\psi(5)=4$,
- $\psi(7)=6$.

That makes the predicted break at `7` arithmetically structural rather than ad hoc.

### 4. It makes the Goldbach boundary explicit

The safe program rule is:

- use Proposition 3’s “any number of odd primes” statement when you need surjectivity of $\psi$ onto even values;
- do not use the two-prime version unless you mean to invoke strong Goldbach.

This paper is where that distinction becomes precise.

### 5. It leaves `S` available as a secondary axis

If the `\psi`-based matching in Leg 2 turns out to be only partial, the symmetric-group function `S` is the obvious backup arithmetic invariant from the same paper. It is not load-bearing now, but it is the natural place to look if a second arithmetic table is needed.

## Scope Note

This memo should be used as the reference for:

- the exact definition of $\psi$,
- the classification $\operatorname{Ord}_n=\{m:\psi(m)\le n\}$,
- the parity consequence $\operatorname{Ord}_{2k+1}=\operatorname{Ord}_{2k}$,
- the safe versus unsafe Goldbach-adjacent uses of the paper,
- and the existence of the pre-built saturation table.

It should not be used as if the recursion formula, the later asymptotic literature, or the Goldbach-equivalent two-prime consequences had been independently reverified here.
