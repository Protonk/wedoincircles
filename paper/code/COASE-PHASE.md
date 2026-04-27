# COASE-PHASE

Companion to `figures/delta_phase_plot.png`, the
δ-algebra phase plot for [paper/IMPOSSIBILITY-OUTLINE.md](../IMPOSSIBILITY-OUTLINE.md) §6.

![A 2D phase plot, "The δ-algebra phase plot". X-axis amortization rate α (0–3.2); y-axis asymptotic floor δ_∞ (0–1.0). Above floor ≈ 0.12: light-pink IMPOSSIBILITY region, sub-label "program's claim, universal over the upper half-plane". A solid blue horizontal at floor ≈ 0.12 reads "program's working floor δ_min (Lemma B + Bridge consequence)". A mustard cross-hatched band straddles the blue line, labeled at right "debt #2: where does δ_min actually sit? open under amortization, bypass, additivity". Below the band: a hatched light-blue foreclosed strip. Along floor = 0 a thin green strip spans the full width, with a green star at its right end. An upper-center green label reads "FFT canon's claimed territory: the entire bottom edge (floor = 0); ★ marks the α → ∞ limit". A vertical dashed grey arrow descends from y ≈ 0.55 at α ≈ 0.85 down to the green strip, with italic grey label "Lemma B blocks this descent route: no finite composition zeros the floor".](../../figures/delta_phase_plot.png)

The figure is built by
[paper/code/build_delta_phase_plot.py](build_delta_phase_plot.py).

## Intent

The figure projects δ-algebra to 2D and stages three distinct claims about the projection. Two axes:

- `α` — amortization rate. `δ_k ~ k^(-α)` under composition. Larger
  `α` means faster per-composition decay.
- `δ_∞` — asymptotic floor. The irreducible part of `δ` that survives
  composition and specialization.

The three claims:

1. **FFT canon's claim.** Free descent succeeds at `floor = 0` — and
   `floor = 0` is *the entire bottom edge*, not a corner. The canon
   isn't asking for a single (α, floor) point; it's claiming the whole
   `floor → 0` axis is reachable.
2. **The program's claim (Lemma B + Bridge consequence).** No finite
   composition zeros the floor. The bottom edge is foreclosed; the
   working floor `δ_min > 0` sits above it. The label says "Lemma B +
   Bridge consequence" because the *uniform* lower bound is something
   the proof needs to establish, not something Coase hands us.
3. **Debt #2.** Where `δ_min` sits exactly is open under amortization,
   bypass-resistance, additivity, representation-dependence. The
   horizontal mustard band at the working-floor line is the
   floor-location uncertainty.

Above the band: a single IMPOSSIBILITY region. One mechanism (Lemma B
+ Bridge + Template), one shaded region — not two side-by-side
mechanisms.

The dashed Lemma B arrow is the descent route the proof rules out: a
direct vertical descent from the impossibility region down through the
foreclosed strip to the canon's edge. The arrow's geometry encodes the
content of Lemma B; the label states it.

## Honesty notes

- The (α, `δ_∞`) parametrization is a *projection* of higher-
  dimensional `δ`-algebra space (additivity across compositions,
  bypass-resistance under intermediation, representation-dependence,
  amortization across reuse). The full debt #2 list is not 2D.
- `δ_min` is *not* a Coase output. Coase 1937 establishes existence
  (`δ > 0`) and supplies the methodological precedent for separating
  existence from algebra. The uniform bound is a program-side claim
  that Lemma B + Bridge must establish.
- The band's vertical extent is heuristic for legibility; its precise
  shape and amplitude are part of debt #2's content.
- The IMPOSSIBILITY region is *one* region, not two. The figure does
  not promise a two-pronged proof; FIRST-PROOF has one mechanism.

## Where it sits

- Figure file: [figures/delta_phase_plot.png](../../figures/delta_phase_plot.png)
- Build script: [paper/code/build_delta_phase_plot.py](build_delta_phase_plot.py)
- Companion outline section: [paper/IMPOSSIBILITY-OUTLINE.md](../IMPOSSIBILITY-OUTLINE.md) §6
- Methodological precedent: [memos/COASE-FRICTION-AND-SPECIALISTS.md](../../memos/COASE-FRICTION-AND-SPECIALISTS.md)
