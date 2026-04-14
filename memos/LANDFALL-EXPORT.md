# LANDFALL-EXPORT

Standalone reference on **Landfall** (Adam, 9-page Annals-style proof-essay on the residual $\varepsilon(m)=\log_2(1+m)-m$ of the affine pseudo-logarithm). Full paper read at a reading-not-verifying level. The paper is less traditional than the other source briefs: it mixes standard real-valued arguments with “Surreal §n” companion remarks and with a literary frame. The mathematical spine is still clear. The primary load-bearing material is in the real-valued sections §0–§6; the Surreal sidebars are auxiliary unless explicitly invoked.

## Thesis

Write a positive floating-point number in base 2 as

$$
x = 2^E(1+m), \qquad m\in[0,1).
$$

If one reads the bit pattern as an integer, up to bias and scaling the result is

$$
L(x)=E+m.
$$

This is the “poor man's logarithm”: an affine surrogate for $\log_2 x$ that the representation provides for free. The true logarithm differs from it by the binade-local residual

$$
\varepsilon(m)=\log_2(1+m)-m.
$$

Landfall asks whether $\varepsilon$ can be eliminated exactly by any **finite structural correction**. Its answer is no, and it argues this through a sequence of closures:

1. finite-degree polynomial correction fails;
2. finite affine composition cannot produce the clock-change $\psi(m)=\log_2(1+m)$;
3. finite local corona data on the binary tiling cannot determine $\varepsilon$ exactly;
4. finite-dimensional closure of the Stern–Brocot-to-dyadic scaffold would force Minkowski’s question-mark function into an absolutely continuous space, contradiction;
5. pointwise, $\varepsilon$ is transcendental at every interior machine dyadic;
6. computational aggregation on the binary tiling fails because the relevant tiling space has no invariant probability measure.

The paper’s abstract compresses this as:

> No composition flattens $\varepsilon$.

## Core Definitions And Facts

### The affine pseudo-logarithm

Within a fixed binade $[2^E,2^{E+1})$, the floating-point representation stores:

- an integer exponent $E$,
- a mantissa $m\in[0,1)$,
- with $x=2^E(1+m)$.

Mitchell’s observation is that the stored representation already gives the coarse logarithm

$$
L(x)=E+m.
$$

Day’s cited theorem says this is not just a convenient heuristic: on each binade, $L$ is the unique affine function agreeing with $\log_2(x)$ at the endpoints, and it is the endpoint-exact affine minimax surrogate on that interval.

### The residual

The correction term is

$$
\varepsilon(m)=\log_2(1+m)-m.
$$

Landfall records the basic geometry of $\varepsilon$:

- $\varepsilon(0)=0$,
- $\varepsilon(m)\to 0$ as $m\to 1^{-}$,
- $\varepsilon(m)>0$ on $(0,1)$,
- $\varepsilon$ is strictly concave on $(0,1)$,
- it has a unique maximum at
  $$
  m^*=\frac{1}{\ln 2}-1\approx 0.4427,
  $$
  where
  $$
  \varepsilon(m^*)\approx 0.0861.
  $$

The key structural fact is that the same $\varepsilon$ appears on every binade. The coarse part changes with $E$; the residual does not.

### Day’s decoupling theorem

Landfall treats Day’s decoupling theorem as foundational:

- the **coarse stage** is computing $L(x)$;
- the **correction stage** is approximating the residual.

These are independent problems. Once $L$ is fixed, every refinement architecture inherits the same correction problem.

## Section-By-Section Reference

### §0. The Poor Man’s Logarithm

This section defines the object of the paper.

The key claims are:

1. The floating-point encoding itself contains an affine pseudo-logarithm $L(x)=E+m$.
2. Kahan’s “magic” square-root constant is interpreted as a log-table trick executed directly on the representation: reinterpret bits as a logarithm, halve in log-space by shifting, reinterpret back, then refine.
3. The only genuinely nontrivial part is the residual $\varepsilon$.
4. The binade geometry is uniform: each mantissa cell has the same hyperbolic shape, so the same residual profile repeats.

This section also states Day’s decoupling theorem and notes that Day’s extremal classification for reciprocal-power correction lives in $\varepsilon$-coordinates, with Farey / Stern–Brocot sampling and binary mantissa subdivision treated as different metrics on the same interval.

The program-level consequence is simple: **$\varepsilon$ is the object**. Everything else is infrastructure.

### §1. Polynomial Packing On A Tile

This is the first impossibility argument.

Landfall grants the machine an unbounded real-valued accumulator, so finite-state aliasing is not the issue. Even then, after the coarse stage is computed exactly, the correction must approximate a function of the form

$$
z^{-1/b}
$$

on a nondegenerate interval $[z_{\min},z_{\max}]$.

If one restricts to polynomial correctors $p(z)$ of degree at most $n$, the minimax relative error is

$$
\varepsilon_n^*(\rho)
=
\min_{\deg p\le n}\ \max_{z\in[z_{\min},z_{\max}]}
\frac{|z^{-1/b}-p(z)|}{z^{-1/b}},
\qquad
\rho=\frac{z_{\max}}{z_{\min}}.
$$

The point is immediate: on any interval of positive length, $z^{-1/b}$ is not a polynomial, so for every finite degree

$$
\varepsilon_n^*(\rho)>0.
$$

This is the **polynomial wall**. Unbounded accumulation does not remove it.

### §2. Affine Recurrence

This is the second impossibility argument and one of the paper’s main exports.

The section starts from Schatte’s asymptotic distribution theory for mantissas of sums. Under repeated multiplication, mantissa distributions converge exponentially to the logarithmic law. Under repeated addition, they do not: the phase keeps rotating because

$$
\log(n+1)-\log n \approx \frac{1}{n}.
$$

Landfall contrasts:

- **Cesàro means**, which weight terms uniformly in additive time and do not converge to the needed correction;
- **Riesz logarithmic means**, which weight the $j$-th term by $1/j$ and do converge.

The paper’s interpretation is that the weight $1/j$ is the Jacobian for the coordinate change from additive time to multiplicative time. That coordinate change is

$$
\psi(m)=\log_2(1+m),
$$

and its deviation from the identity clock is exactly $\varepsilon$.

The decisive closure argument is then stated explicitly:

- within a single binade, machine operations on mantissas are affine;
- additions translate and multiplications scale;
- these generate the group $\operatorname{Aff}^+(\mathbb{R})$ of maps $x\mapsto ax+b$ with $a>0$;
- composition of affine maps stays affine;
- but $\psi(m)=\log_2(1+m)$ is not affine.

Therefore:

> No finite composition of the machine’s native operations produces the logarithmic clock-change $\psi$.

This is the paper’s clean log-side obstruction to any iteration-style “just compose the machine’s own moves until the correction emerges” strategy.

### §3. Corona Crawl

This is the local-combinatorial obstruction.

The background is the binary tiling in the Poincaré half-plane, read through Bowen’s stripe model and Dolbilin–Frettlöh’s corona classification. Each depth-$d$ dyadic cell is identified with its left endpoint $k/2^d$ as canonical mantissa.

Landfall defines a **$k$-local corona-invariant corrector** to be a map on cells whose value depends only on the $k$-corona congruence class. This is weaker than a streaming machine, since it only sees finite local tiling type rather than the full dyadic address.

The section proves:

> No $k$-local corona-invariant corrector is exact on all depth-$d$ cells once $d\ge k+1$.

The proof uses three ingredients:

1. Dolbilin–Frettlöh: the binary tiling has
   $$
   N_k=2^{k-1}
   $$
   congruence classes of $k$-coronae.
2. Orientation-reversing pairing of tails forces many cells into the same local class.
3. Strict concavity of $\varepsilon$ means one horizontal value cannot hit three distinct interior mantissas.

For $k=1$, the contradiction is already visible from $\varepsilon(0)=0$ and

$$
\varepsilon(1/2)=\log_2(3/2)-1/2\approx 0.085.
$$

So finite local tiling information cannot pin down the exact correction.

### §4. The Padé Ghost

This is the rational-approximation / finite-dimensional closure obstruction and the section that contains the paper’s pointwise transcendence theorem.

The setup is Minkowski’s question-mark function $?(x)$, viewed as the bijection between the Stern–Brocot subdivision and the dyadic subdivision. Finite levels of its construction are absolutely continuous; the limit is singular continuous.

Landfall builds level-$k$ floors $C_k$: absolutely continuous piecewise-affine interpolants matching $?(x)$ at Farey endpoints. It then asks what would happen if the level-to-level update closed inside a fixed finite-dimensional linear system:

$$
v_{k+1}=Mv_k,\qquad C_k=\Phi(M^k v_0)
$$

for fixed $M$ and $\Phi$.

If that happened, then:

1. the span
   $$
   W=\operatorname{span}\{C_k:k\ge 0\}
   $$
   would be finite-dimensional;
2. finite-dimensional subspaces of $C[0,1]$ are closed;
3. $C_k\to ?(x)$ uniformly;
4. hence $?(x)\in W$;
5. but every $C_k$ is absolutely continuous, so $W\subset AC[0,1]$;
6. contradiction, since $?(x)$ is singular continuous.

This is exactly the §2 closure-under-composition argument lifted from affine maps to a finite-dimensional matrix algebra.

The section then returns from $?(x)$ to $\varepsilon$ itself.

### Fourier consequence

The periodic extension of $\varepsilon$ to the binade circle is continuous but not $C^1$ at the seam:

$$
\varepsilon'(0^+)=\frac{1}{\ln 2}-1,\qquad
\varepsilon'(1^-)=\frac{1}{2\ln 2}-1.
$$

Therefore its Fourier coefficients decay like

$$
O(1/n^2)
$$

and do not terminate. So no finite trigonometric packet equals $\varepsilon$.

### Pointwise transcendence at dyadics

This is one of the paper’s strongest concrete facts:

> For every interior machine dyadic
> $$
> m=\frac{k}{2^p},\qquad 0<k<2^p,
> $$
> the value
> $$
> \varepsilon(m)=\log_2(1+m)-m
> $$
> is transcendental.

The proof is short:

1. Let $\beta=\log_2(1+m)$.
2. If $\beta$ were algebraic irrational, then $2^\beta=1+m$ would be transcendental by Gelfond–Schneider, contradiction.
3. If $\beta=a/b$ were rational, then
   $$
   (1+m)^b=2^a,
   $$
   so
   $$
   (2^p+k)^b=2^{a+pb},
   $$
   forcing $2^p+k$ to be a power of $2$, impossible because
   $$
   2^p<2^p+k<2^{p+1}.
   $$
4. Hence $\beta$ is transcendental, and subtracting the algebraic number $m$ leaves $\varepsilon(m)$ transcendental.

This is the paper’s sharpest arithmetic-depth statement.

### §5. So You Want To Compute

This section translates the previous obstructions into a computational class.

The admissible class is:

> one-pass binary-digit-reading correctors with signaled completion.

That means:

- the machine reads significand bits from left to right;
- it chooses for itself when it is done;
- halting inputs must therefore form a prefix-free domain.

Landfall interprets this through Chaitin / Kraft arithmetic:

- a halt at depth $p$ claims one dyadic cylinder of width $2^{-p}$;
- prefix-free halting domains satisfy Kraft’s inequality;
- composition, splicing, partition refinement, and machine simulation all remain inside the same self-delimiting budget.

The section’s conclusion is not a new external theorem but an architectural claim:

> composition redistributes the available Kraft budget; it does not create the missing correction.

So the paper argues that prefix-free one-pass computation does not furnish a hidden exact route around the earlier obstructions.

### §6. The Fire

This is the aggregation obstruction, and it is where Bowen’s no-invariant-measure result becomes central.

The section imagines a “Shannon demon” that:

1. produces a smooth surrogate $\tilde\varepsilon$ cheaply;
2. lets an external process interact with the true $\varepsilon$;
3. reads a small amount of partial output from that interaction.

Landfall frames such a demon as needing two things:

- **information asymmetry**, meaning there is real information to extract from the gap between smooth and singular behavior;
- **aggregation**, meaning local observations can be combined equivariantly into a global correction.

Landfall treats the first condition as available: because $\varepsilon$ is transcendental at every interior dyadic, the pointwise gap never collapses into an algebraic triviality.

The second condition fails. Bowen’s result says the binary tiling space carries **no** $PSL(2,\mathbb{R})$-invariant probability measure. An equivariant way of aggregating local observations across tilings would amount to precisely such an invariant measure. Since none exists, the global aggregation step is blocked.

This yields the paper’s global obstruction:

> the residual lives on a tiling space where equivariant averaging has nowhere to land.

That is the structural content behind the paper’s repeated claim that the logarithm is “free” in the representation but the residual is not.

### §7. Coda

The coda does two things.

First, it reinterprets Gosper’s continued-fraction arithmetic machine as a model that survives by **refusing finite closure**:

- its state can grow without bound,
- it reaches periodicity only in special quadratic-irrational cases,
- and its Möbius operations do not produce the logarithmic coordinate change.

Second, it states the main open problem left by the paper:

> fixed-width branching-program exact correction is not ruled out here.

The local corona model fails at depth $k+1$, but a width-$q$ branching program can read the dyadic address sequentially and use information the corona model discards. Landfall cites known lower bounds for read-once branching programs and separator/treewidth facts for planar hyperbolic graphs, but explicitly says it does **not** prove that $\varepsilon$ falls under those techniques.

So the paper ends with an open bounded-computation question, not with a universal computational impossibility theorem.

## What The Paper Proves Versus What It Argues

The most solid internal payload, as presented in the paper, is:

1. the definition and geometry of $\varepsilon$ as the binade-uniform residual of the affine pseudo-log;
2. the finite-degree polynomial obstruction;
3. the affine closure obstruction for producing $\psi(m)=\log_2(1+m)$ from native binade operations;
4. the local corona obstruction;
5. the finite-dimensional closure contradiction for the Minkowski scaffold;
6. Fourier nontermination at $O(1/n^2)$;
7. transcendence of $\varepsilon(k/2^p)$ at every interior dyadic.

Sections §5–§6 are more architectural than theorem-theorem in flavor. Their role is to synthesize the earlier obstructions into a statement about admissible computation and failed aggregation, rather than to introduce a wholly new elementary proof.

## Program-Facing Exports

### 1. The Affine-Closure Obstruction

This is the strongest log-side obstruction for CREATI-style “iterate the native operations until the log-side correction appears” thinking.

It says:

- native binade operations generate $\operatorname{Aff}^+(\mathbb{R})$,
- $\psi(m)=\log_2(1+m)$ is not affine,
- so no finite composition of those operations yields the needed clock-change.

This turns “Chebyshev-style iteration probably fails on the log side” into a structural obstruction, not just a failed guess.

### 2. Transcendence At Every Interior Dyadic

This is the clean arithmetic-depth statement exported by the current memo and it remains the main single-line theorem worth carrying around:

$$
\varepsilon(k/2^p)\ \text{is transcendental for every}\ 0<k<2^p.
$$

It means the residual never simplifies algebraically even on the log representation’s own native dyadic grid.

### 3. Bowen’s No-Invariant-Measure Result As Anti-Aggregation

Landfall’s use of Bowen is precise:

- local information may exist,
- but there is no invariant-measure-based way to aggregate it equivariantly across the binary tiling space.

This is the source-level reason INSCRIPTION’s measure-based obstruction exists.

### 4. The Local-Corona Failure

The corona argument gives a concrete finite-window impossibility result:

- finite local tiling type is too coarse,
- strict concavity of $\varepsilon$ forces aliasing,
- so exact correction cannot be local in that sense.

This is the paper’s most explicit bounded-local-information obstruction.

### 5. Gosper As The Continued-Fraction Primitive

The coda makes one additional program-facing point:

- exact continued-fraction arithmetic on the log side exists,
- but it lives in Gosper’s unbounded Möbius-state machine,
- not inside the affine closure of the machine’s native binade operations.

So continued-fraction computation is real log-side infrastructure, but it survives by refusing the finite closure Landfall is testing.

## Bottom Line

Landfall’s central claim is not merely that $\log_2(1+m)$ is awkward to compute. It is that the residual

$$
\varepsilon(m)=\log_2(1+m)-m
$$

is the irreducible price of using an additive representation to index a multiplicative world.

The paper supports that claim by ruling out one finite structural route after another:

- finite-degree polynomial correction,
- finite affine composition,
- finite local corona data,
- finite-dimensional Padé-style closure,
- algebraic exactness at dyadics,
- and invariant-measure-based global aggregation.

What remains open is not whether these easy routes fail, but how much bounded sequential computation can still do inside the admissible class.
