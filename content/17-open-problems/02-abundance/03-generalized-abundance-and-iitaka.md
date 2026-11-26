---
title: Generalized abundance, the Iitaka conjecture and b-semiampleness
nodes: [MMSH2N59E3, MMY51YYYJX, MMRXDSNJQ7, MM193HWD2S]
sources: [BCHM10]
reads_with: []
requires: ["10", "16"]
level: research
kind: survey
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Generalized abundance, the Iitaka conjecture and b-semiampleness

### Statement

**Conjecture 17.2.9 (Generalized abundance).** Let $(X, \Delta)$ be a klt pair with $K_X + \Delta$ pseudo-effective, and let $L$ be a nef divisor with $K_X + \Delta + L$ nef. Then $K_X + \Delta + L$ is numerically equivalent to a semiample divisor.

Node: MMSH2N59E3 · Lean: `MinimalModel.GeneralizedAbundance`

This is statement S45, due to Lazić and Peternell. It is open.

**Conjecture 17.2.10 (The Iitaka conjecture $C_{n,m}$).** Let $f \colon X \to Y$ be an algebraic fibre space of smooth projective varieties with $\dim X = n$, $\dim Y = m$ and general fibre $F$. Then $\kappa(X) \ge \kappa(F) + \kappa(Y)$.

Node: MMY51YYYJX · Lean: `MinimalModel.IitakaConj`

This is statement S46. It is open in general.

**Remark 17.2.11 (Claim C13: b-semiampleness of the moduli part).** The moduli part of an lc trivial fibration is b-semiample.

Node: MMRXDSNJQ7 · Lean: `MinimalModel.BSemiampleness`

This is statement S47, the conjecture of Prokhorov and Shokurov. It is claimed by Bakker, Filipazzi, Mauri and Tsimerman (BFMT, arXiv:2508.19215; spec 07.13 gives the names) and by Hu, K. Liu and Shen (arXiv:2611.12744). The records keep it in the class claimed.

For contrast, finite generation holds for the canonical ring.

**Theorem 17.2.12 (Finite generation of the canonical ring).** Let $X$ be a smooth projective variety. Then the canonical ring $R(X, K_X) = \bigoplus_{m \ge 0} H^0(X, mK_X)$ is finitely generated.

Node: MM193HWD2S · Lean: `MinimalModel.FiniteGenerationCanonical`

### Proof in words

**Generalized abundance.** The conjecture adds a nef divisor $L$ to the setting of abundance. For $L = 0$ it is abundance for klt pairs up to numerical equivalence. Spec 03.11 gives one consequence: generalized abundance implies the log Iitaka conjecture (Fujino, arXiv:1406.2759, rated [S]). The records give no dimension in which the full conjecture is known. Target O-R5-5 names generalized abundance in dimension 3 with $\nu = 0$ as a small open case. The records do not say more about the known cases.

**The Iitaka conjecture.** Spec 03.11 gives the arrow "a good minimal model of $F$ gives $C_{n,m}$" (Kawamata, rated [U]). Ammar (arXiv:2510.06412) proves the case $\alpha(Y) \ge m - 2$. Item 7 of spec 01.16 asks whether Ammar's result needs a non-uniruled Iitaka variety. The records list the cases of Kawamata, Viehweg and Birkar-Chen (spec 07, row T9-09) with the tag [U], and give no detail.

**b-semiampleness.** Prokhorov and Shokurov prove the conjecture in relative dimension one (spec 07, row T9-10, rated [U]). BFMT and Hu-K. Liu-Shen claim it in general. Spec 03.11 gives the arrow "b-semiampleness gives adjunction to all lc centres and Shokurov's GLC" (BFMT). The effective form of b-semiampleness is open in relative dimension at least 3 (spec 01.9).

**Finite generation.** BCHM prove the finite generation of the canonical ring (BCHM10, Corollary 1.1.2). Cascini-Lazić (arXiv:1009.3188) and Corti-Lazić (arXiv:1005.0614) prove it without the program. For generalized pairs, Liu and Wang (arXiv:2608.03258) claim an example of a projective klt generalized pair whose generalized lc ring is not finitely generated. The table of spec 01.1 lists this in its row "Disproved". The claim record (C17) has the status fresh and says that the preprint is not refereed and is "mostly AI-generated, human-verified". So this report treats the example as a claimed counterexample.

### Examples

- The first test case of generalized abundance is dimension 3 with $\nu = 0$ (target O-R5-5, difficulty 2).
- The first test case of $C_{n,m}$ is the case of Ammar with one more unit: $\alpha(Y) \ge m - 3$, or the removal of the non-uniruled hypothesis (target O-R5-6, difficulty 2 for the small step and 4 for the full conjecture).
- The first test case of effective b-semiampleness is relative dimension 3 with bounded $b_2$ (target O-R5-7, difficulty 3).
- The first test case of C17 is its explicit example: the computation of the generalized lc ring (target O-R1-7, difficulty 2, formal check 3).

### Lean

`MinimalModel.FiniteGenerationCanonical` (S32) is stated in `MinimalModel/Statements/Models.lean`, with no proof. On 2026-11-26, `GeneralizedAbundance` (S45), `IitakaConj` (S46) and `BSemiampleness` (S47) are not in `records/lean.json`. The notes of S47 say that the vocabulary of b-divisors is missing, and plan the statement for milestone S4. Target O-R5-9 is the finite generation of Cascini-Lazić in Lean, as an alternative to the proof of BCHM (S31).

### Notes and history

**Claims of 2025 and 2026.**

| Claim | What it claims | Record | Status |
|---|---|---|---|
| C6, OpenAI 036 | generalized abundance (Lazić-Peternell) | `claims/openai-math.yaml` | fresh; no Lean |
| C7, OpenAI 033 | the Iitaka conjecture $C_{n,m}$ in characteristic 0 | `claims/openai-math.yaml` | fresh; no Lean |
| C13, BFMT; Hu-K. Liu-Shen | b-semiampleness | `claims/arXiv-2508-19215.yaml`, `claims/arXiv-2611-12744.yaml` | fresh; spec 01.3 says "strong human papers; referee status not checked" |
| C17, Liu-Wang | finite generation fails for generalized pairs | `claims/arXiv-2608-03258.yaml` | fresh; unrefereed |

Each record says: "Nobody has read the claim for the project yet."

**Routes.** Route R5 has O-R5-4 (generalized abundance, difficulty 4), O-R5-5, O-R5-6, O-R5-7 and O-R5-9. Route R1 has O-R1-7 for Liu-Wang. Route R9 has O-R9-3, b-semiampleness for Kähler morphisms of relative dimension 1.

**References.** BCHM10; arXiv:1406.2759 (Fujino); arXiv:2510.06412 (Ammar); arXiv:2508.19215 (BFMT); arXiv:2611.12744 (Hu, K. Liu and Shen); arXiv:2608.03258 (Liu and Wang); arXiv:1009.3188 (Cascini-Lazić); arXiv:1005.0614 (Corti-Lazić). Volume 10 treats the Iitaka conjecture and Volume 16 treats generalized pairs.

**Questions for a reader.**

- In which dimensions is generalized abundance known? The records do not say.
- Does Ammar's proof need the Iitaka variety of $Y$ to be non-uniruled (item 7 of spec 01.16)?
- Does the example of Liu-Wang use a nef part that is not NQC, and does it contradict any stated node of the map?
