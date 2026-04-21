# VILLAINS

Sharpest-form adversarial questions aimed at the program. Each villain asks exactly one. The program earns its integrity by answering — or by admitting it can't.

## #1 — Lady Nagant

The pseudo-Chebyshev node construction lands $\text{node}(n) = \cos(\pi/n)$ at a specific point in the plane — $(\cos^2(\pi/n),\ \cos(\pi/n)\sin(\pi/n))$, above the anchor edge tangent at $(1, 0)$. That specificity is the hook: *one distinguished point per n, on a coherent curve*. But randomize the anchor independently across $n$ and the scalar $\cos(\pi/n)$ survives while the point scatters onto a ring with no privileged angular coordinate. The strip makes the loss cleaner still: kissing levels unchanged, within-$n$ periods unchanged, only the cross-$n$ angular coregistration breaks.

So the shared anchor is a synchronization convention, not a geometric necessity. The scalar $\cos(\pi/n)$ is the apothem-to-circumradius ratio of a regular $n$-gon — a first-week fact requiring no pseudo-Chebyshev branding. What the construction adds on top is a cross-$n$ angular alignment that exists only because you chose to synchronize.

**Her question.** Is the shared anchor that creates those tenuous pseudo-Chebyshev nodes just a conventional agreement on synchronization? If so, what can we fairly infer from some happenstance of its configuration?

## #2 — Procrustes

The program names its deliverable in advance. The `README` states the expected outcome as "an explicit closure mismatch theorem with computable witnesses" and itemizes those witnesses before the work runs: $\mathbb{Z}[x]$ vs $\text{Aff}^+(\mathbb{R})$, the break at $n = 7$, the $\tau_c / \varepsilon$ spectral rhyme, the crystallographic ↔ $p$-adic matching. The verdict (no functor $F$), the shape of the obstruction (a closure mismatch), and the witnesses that will demonstrate it are all pre-declared.

Each witness is the program's own chosen object. $\varepsilon(m) = \log_2(1+m) - m$ was brought to the table because its structure is suggestive. The Chebyshev apparatus on the circle side was brought because $T_n$ compositional closure generates $\mathbb{Z}[x]$. The $n = 7$ break is a Gauss–Wantzel artifact — constructibility fails at $n = 7$ for every ruler-and-compass framework because $2 \cdot 7 = 14$ is not of Fermat form — repackaged here as a log-versus-circle obstruction. Each witness coheres with the verdict because the same hand that named the verdict chose the witnesses.

**His question.** If every witness was selected after the conclusion was named, where is the prediction that could have killed the program? Name one fact, obtainable from a source that wasn't you, whose appearance in the wild would force the closure-mismatch verdict to retract.

## #3 — Shigaraki

The circle side is saturated with irrationality. By Niven's theorem, across the entire real-$t$ continuation of the pseudo-Chebyshev curve, exactly two values — $\text{node}(2) = 0$ and $\text{node}(3) = 1/2$ — are rational. Every other integer $n$ produces an algebraic irrational of degree $\varphi(2n)/2$; every rational $t = p/q$ produces an algebraic irrational of its own Galois complexity; every irrational $t$ produces, generically, a transcendental. Regularity in the integer index does not propagate to the image. Rational input collapses almost everywhere into the irrationals, and as $n$ grows, the algebraic degree grows without bound — non-monotone but unbounded, a cascade of Galois objects of increasing arithmetic weight.

This is the avalanche. Every computational instantiation of $\text{node}(n)$ — a float, a symbolic expression forced to finite precision, any fixed-width encoding — collapses that irrationality back onto the rationals. What the construction *produces*, computation must destroy in order to *represent*. The log side $\varepsilon(m)$ already lives on the rational side of this divide; it is what the machine's native arithmetic is natively closed on. The circle side lives on the irrational side, and can enter the log side's medium only by decaying into it.

If the real mismatch between the two sides is not a closure mismatch between $\mathbb{Z}[x]$ and $\text{Aff}^+(\mathbb{R})$ but an ontology mismatch — a space whose native elements are algebraic-of-unbounded-degree against a space whose native elements are rational-of-bounded-width — then the no-functor verdict is not a theorem earned at the end of the work, it is an inheritance baked in at the beginning. Every finite witness on the circle side is already a fragment.

**His question.** Regularity in the integer index gives you an avalanche of algebraic irrationality of unbounded degree. Every finite computational witness collapses that irrationality to the rational envelope of its medium. Can computation outrun the degeneracy — can any finite act on the circle side preserve even a shadow of the algebraic structure — or is every witness you'll ever produce already dust the moment you touch it?
