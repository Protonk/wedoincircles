# FFT-COMPLEXITY-ARTICULATION

This file extracts proof templates from the four FFT-complexity frameworks the paper engages with directly: Schönhage–Strassen 1971, Morgenstern 1973, Winograd 1978, Auslander–Feig–Winograd 1984. Each template is paired with the witness it composes with from the chain and tagged by paper-direction — *inherits*, *extends*, or *specifies against*. Same shape as `paper/LANDFALL-EXPORT.md`. Trust boundaries follow `fft/PROVENANCE-AND-TRANSFERABILITY.md` §3.2.

## Template 1: Operational uniform model (Schönhage–Strassen 1971)

Schönhage–Strassen 1971 supplies the operational uniform model: bit/gate primitives, FFT over a representation where root multiplication is cheap by construction. Proof template: *operational specification* — uniform ring-of-cost-bearing-operations construction that fixes the cost ledger before any algorithmic content. The paper *specifies against* this template, using it to fix what "FFT-style cost manifold" means as a concrete cost object with mult and add submanifolds named explicitly. Composes with `paper/IMPOSSIBILITY-CHARTER.md`'s mult/add cost-manifold map. Trust boundary: SS supplies the model, not a lower bound; not cited for any descent argument.

## Template 2: Bounded-coefficient additive lower bound (Morgenstern 1973)

Morgenstern 1973 proves that bounded-coefficient `n × n` determinant computation requires `Ω(n log n)` additive operations. Proof template: *bounded-coefficient additive lower bound* — combinatorial argument that holds precisely when coefficient size is constrained, and collapses under unbounded coefficients. The paper *inherits*: this is the bounded-side anchor of the mult/add boundary, the floor any further descent would have to cross. Composes with `paper/IMPOSSIBILITY-CHARTER.md`'s bounded↔unbounded coefficient regime change. Trust boundary: Morgenstern is bounded-coefficient only; not cited for unbounded regimes or algebraic-height accounting.

## Template 3: CRT-cyclotomic factor ledger (Winograd 1978)

Winograd 1978's modular-product theorem `μ(T_P) = 2n − k` factors multiplicative complexity across the CRT decomposition of a polynomial-quotient ring with `k` distinct irreducible factors. Proof template: *CRT-cyclotomic factor ledger* — μ-cost bookkept across cyclotomic factors via the chinese remainder structure. The paper *extends*: from rational-equivalence cost (Winograd's setting) to certification cost on the same factor structure. Composes with `paper/VERTEXIOUS-ALGEBRA.md`'s compute-cost-on-vertex-algebra reading. Trust boundary: μ-bounds are under rational equivalence; not cited for paid adjunctions or certification cost without explicit extension.

## Template 4: Cyclotomic decomposition (AFW 1984)

Auslander–Feig–Winograd 1984 supply the semisimple cyclotomic decomposition of finite-abelian DFTs with multiplicative complexity computed under rational equivalence. Proof template: *cyclotomic decomposition* — separate the DFT into cyclotomic-factor-localized pieces, bookkeep μ-cost factor-by-factor. The paper *inherits*: this is the algebraic structure on which the multiplicative side of the cost manifold is measured. Composes with `paper/POLYGONAL-LEDGER.md`'s algebraic-depth catalogue and `paper/VERTEXIOUS-ALGEBRA.md`'s vertex-algebra reading. Trust boundary: rational-equivalence complexity only; not cited for certification cost, paid constants, or the real-subfield `K_n` result (that is HJB §5, below).

## HJB-1985 §5 aside

`fft/HEIDEMAN-JOHNSON-BURRUS-1985-BRIEF.md` §5 is also in `fft/` but is algebraic-side — the eigenspace decomposition forcing `K_n` as the unique multiplicatively-closed half of `Q(ζ_n)` under `σ_{−1}`. Already cross-pointed from `POLYGONAL-LEDGER` and `ROTATIONAL-SUBSTRATE`; not a fifth FFT-complexity template.
