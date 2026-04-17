# BIDDER-THE-NAVIGATOR

A bridge doc connecting the 19th-century mental-arithmetic of George Parker Bidder with the 21st-century floating-point argument of *Landfall*. Not a memo on Bidder — see `memos/BIDDER-AND-SON.md` for that. Not a discipline charter — see `../BNHA/triad` for those. A standalone observation whose one claim is:

> Landfall is a crystallization of an arithmetic fact that Bidder already knew and exploited. The hardware substrate changed. The structural fact didn't.

## The shared constraint

Mental arithmetic in 1856 and floating-point hardware today face the same underlying constraint: the logarithm comes free in *some* representation, but the residue

ε(m) = log₂(1 + m) − m

survives every finite correction strategy. Mental arithmetic pays for this in registration burden — the mind holds only so many intermediate results at a time. Floating-point hardware pays for it in finite precision — the register file holds only so many bits, and ε does not vanish at any finite precision.

Bidder's 1856 address identifies *registration* as the binding constraint on mental calculation. Landfall's §0 identifies *finite operational closure* as the binding constraint on floating-point. These are the same constraint seen through two different substrates.

Bidder's substrate, described in computational terms: a strictly sequential, memory-bounded machine where reasoning is abundant, working memory is scarce, and peak register pressure is the binding constraint on how far any computation can go. Memorized facts serve as pre-paid long-term storage. The design rule is to trade operations for memory relief — a procedure that looks "prolix" on paper can be the right mental algorithm because the extra operations keep peak register load low. Bidder articulates this rule explicitly in the 1856 address and organizes his procedures around it.

Landfall's substrate is the same shape in different hardware: a sequential machine with bounded precision, where the register file is finite and ε is what escapes that finite state. Bidder's "if registration matched reasoning" and Landfall's "if the register file were unbounded" are the same counterfactual. The residue that survives both — ε(m) = log₂(1+m) − m — is a substrate-invariant, not an artifact of either particular substrate.

## Four direct correspondences

**1. Registration ↔ register file.** Bidder: "if my powers of registration matched my powers of reasoning, I could compile a large table of logarithms in very short time." Landfall §0: the floating-point register file is itself a coarse log table via Mitchell's pseudo-log L(x) = E + m. Same constraint — limited state through which the computation must be funnelled. The technology is what differs.

**2. Left-to-right mental multiplication ↔ coarse-first / refine-later.** Bidder begins mental multiplication at the most significant digit, preserving a continuously-meaningful running total. Landfall and Day observe that the floating-point coarse stage L(x) fixes magnitude first, and every later correction is a refinement downward. Same structural order. Bidder's constraint was memory; Landfall's is the endpoint-exactness of the affine surrogate L.

**3. Multi-scale log(1+ε) corrections ↔ Landfall's ε(m) machinery.** Bidder's son uses log(1.001), log(1.0001), log(1.00001) as universal scale constants — each captures one decimal of precision. Landfall's ε(m) is the binade-uniform residual every floating-point correction must account for, with its small-m behavior controlled by log₂(1+m). The son's scale constants are *evaluations* of log₁₀(1+m) at the canonical small-m grid points. The son had worked out, in a mental substrate, what a multi-scale ε-correction layer looks like.

**4. Prime-logs catalog ↔ "the representation is the table."** Bidder's father memorized logs of all primes under 100, turning any factorable target into an additive sum of catalog entries. Landfall §0 quotes Mitchell: "the representation contains its own log table" — the bit pattern of x in floating point is already L(x) up to bias. Same fact about what "table lookup" means. The 19th-century solution: memorize. The 21st-century solution: let the hardware encode it.

## What Bidder shares with Landfall's closing stance

Landfall's §7 Coda draws Gosper's continued-fraction machine as a model that "survives by refusing finite closure." Its state grows without bound on non-Hurwitz inputs; it reaches periodicity only on quadratic irrationals; its Möbius operations do not produce the logarithmic coordinate change. The machine works by continuing, not by closing.

Bidder is the same shape. He computed eight-place logarithms of arbitrary primes in under four minutes, mentally. He did not reduce the problem to a closed table; he developed methods that worked at *any* precision needed, stopping when the remaining terms could no longer change the answer. The son's compound-interest derivation in the 1856 address is explicit about this: "the remaining terms could not possibly amount to one farthing, the process was stopped and the result stated." Bidder's stance is Landfall's stance: no finite structure flattens ε, and no practical technique needs one to. The work is in disciplined navigation around the residue.

## What this doc is and is not

This doc is a bridge observation. It does not re-derive Bidder's math (see `memos/BIDDER-AND-SON.md`). It does not re-derive Landfall (see `memos/LANDFALL-EXPORT.md`). It does not propose new program work. Its value is in stating a continuity that has been implicit in the program since the Bidder memo went in.

## Why "the Navigator"

Landfall borrows its title from Paintapu, the Gilbert Islands navigator of the 1780s whose methods were "real, traditional, and entirely alien to her companions." She guided one canoe safely to Abemama by reading the heavens; the rest of the flotilla was lost because her chief would not let her practice her craft.

Bidder is the same kind of navigator, for mental arithmetic. His elementary instruction ended at "count to 100, and there he stopped" — everything after was self-invented. Prime-logs; multi-scale corrections; distributive "natural algebra"; left-to-right multiplication. His results were practical and reliable, but the method was alien to his colleagues in the Institute of Civil Engineers. Stephenson's 1856 introduction says as much: "none of those gifted persons, even after enjoying the benefits of education, have been enabled to render intelligible the source of the power, or to describe clearly the processes employed."

Paintapu navigated by sky. Bidder navigated by number. Both worked because the navigator knew the territory and refused to reduce it to a finite table. The framing gives Landfall's open §7 question — bounded sequential computation exactly flattening ε — a concrete existence proof on the historical side: a navigator can do this, and has.
