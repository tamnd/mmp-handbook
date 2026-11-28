---
title: The 2026 preprints
nodes: []
sources: [OAI26, AxiomMMP, Ajit26, BDY26, HLZ25, Mor25]
reads_with: []
requires: ["16.1", "16.2", "16.3"]
level: research
kind: survey
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The 2026 preprints

### Statement

**Definition 16.4.1 (claim record).** A *claim record* is a file `claims/<key>.yaml` of tamnd/mmp for one preprint or one repository. It gives the source and its version, the date of the record, the claim in one sentence, the node of the map that states it, if there is one, and a state. The state is *fresh* when nobody has read the claim for the project, and *withdrawn* when the authors have withdrawn it. The records follow spec 01.3, which gives each claim a number C1 to C17 and a short status.

**Remark 16.4.2 (how the handbook uses the word claimed).** A result is *claimed* when a preprint or a repository asserts it and no referee has accepted it. A claimed result is never a hypothesis of a theorem in the handbook, and never a step in a proof. A Lean formalization of a claimed result does not change the word: by spec 14.7 the state of the literature and the state of the Lean code are shown apart. In Volume 16 every claimed result is stated as a Remark, never as a Theorem.

On 2026-11-28 there are sixteen claim records. Every record except one is fresh, and its notes say: "Nobody has read the claim for the project yet". The record of C16 is withdrawn. The table gives the claims in the order of spec 01.3. A dash in the node column is written "none".

| Claim | Source | What is claimed | Status in spec 01.3 | Node |
|---|---|---|---|---|
| C1 | OpenAI 056 (openai/math, 2026-09-24); AxiomMath/MMP at `1f9ade3670` (2026-11-16) | every MMP for a projective lc 4-fold with rational boundary terminates; about 2.05 million lines of Lean | AI-written paper and code; no human review of the code | S22, claimed |
| C2 | Hashizume, arXiv:2609.33679 v2 | termination of flips for klt pairs with $\Delta$ or $K + \Delta$ big, in all dimensions; finiteness of marked Mori fibre spaces; the strong Sarkisov program | drafts by ChatGPT and Codex, revised by the author | S25, claimed |
| C3 | OpenAI 034 | log abundance in characteristic 0 for rational boundary in all dimensions; canonical non-vanishing; 4-fold non-vanishing; the effective Iitaka fibration; the index conjecture for slc log Calabi-Yau pairs | contested on one tracker, at log Iitaka subadditivity; no Lean | none |
| C4 | J. Liu, arXiv:2610.35913 | non-vanishing for smooth varieties in dimension $d$ implies abundance for lc pairs in dimension at most $d$ | unrefereed | none |
| C5 | Hu and Liu, arXiv:2603.03817 | flips exist for all lc generalized pairs; minimal models exist if and only if programs with scaling terminate | unrefereed | S27, claimed |
| C6 | OpenAI 036 | generalized abundance in the form of Lazić and Peternell | unrefereed, no Lean | none |
| C7 | OpenAI 033 | the Iitaka conjecture $C_{n,m}$ in characteristic 0 | unrefereed, no Lean | none |
| C8 | OpenAI 038; Han, arXiv:2609.01574 | Fujita freeness for $m \ge n + 1$ (OpenAI); a linear bound with $C_0 \approx 1.77629$ (Han) | both unrefereed | none |
| C9 | OpenAI 035; BWX, arXiv:2610.10439 | 3-fold abundance with $\nu = 1$ for $p > 3$ (OpenAI); abundance for lc 3-folds for $p > 42$ (BWX, "very preliminary") | for $5 \le p \le 42$ only the AI manuscript covers the case | none |
| C10 | Hacon and Wang, arXiv:2611.29683 | termination of klt flips with scaling for compact Kähler klt pairs, and good minimal models, with two OpenAI manuscripts as input | unrefereed; its Corollary 1.2 rests on C3 | none |
| C11 | Hacon and Xie, arXiv:2607.24986 v2 | the MMP for big gklt Kähler pairs in all dimensions; Tosatti's transcendental basepoint-free conjecture | unrefereed | none |
| C12 | Bie, Du and Yu, arXiv:2611.12786, with arXiv:2611.18357 and arXiv:2610.10537 | $\mathrm{vol} \ge 1/420$ for smooth 3-folds of general type; the moduli of canonical 3-folds of volume $1/420$; a sharp polynomial volume bound for $\epsilon$-lc Fano varieties | unrefereed; the moduli paper has code | none |
| C13 | BFMT, arXiv:2508.19215 v2; Hu, K. Liu and Shen, arXiv:2611.12744 | the b-semiampleness conjecture of Prokhorov and Shokurov | human papers; the referee status is not checked | S47, claimed |
| C14 | Ajit, arXiv:2610.09270 v2 | counterexamples to the effective non-vanishing conjecture of Ambro and Kawamata in dimension at least 4 | explicit and checkable; read by Totaro | S57, claimed |
| C15 | J. Liu, arXiv:2608.19301 | a K-polystable smooth polarized 5-fold with no cscK metric | unrefereed; the paper says that it was obtained using generative AI | none |
| C16 | Landi, arXiv:2611.30971 | the lower semicontinuity of minimal log discrepancies, and $\mathrm{mld} \le \dim$ | withdrawn on 2026-11-24: "Lemma 3.2 is false" | none |
| C17 | Liu and Wang, arXiv:2608.03258 | a projective klt generalized pair whose generalized lc ring is not finitely generated | unrefereed; the paper says that it is mostly AI-generated and human-verified | none |

The OpenAI families C3, C6, C7 and the OpenAI parts of C8 and C9 share one record, `claims/openai-math.yaml`, because they come from one repository. By spec 01.3, that repository released 722 manuscripts in 372 families on 2026-10-06, and on 2026-10-07 retracted 3 and revised 14; its README says that some of the unformalized results could have issues. Six of the revised manuscripts are on Kähler programs and abundance. The records do not say which.

**Remark 16.4.3 (the withdrawn claim).** The preprint of C16 was withdrawn on 2026-11-24, and the reason given is that its Lemma 3.2 is false. The two statements it claimed, the lower semicontinuity of minimal log discrepancies (S50) and the bound $\mathrm{mld} \le \dim$ (S51), stay open conjectures.

### Proof in words

There is no proof in this section. The section reports claims, and no claim in it is used in a proof elsewhere in the handbook.

Three things decide how a claim is treated, and the records give all three. The first is who wrote it: C1, C3, C6, C7 and the OpenAI parts of C8 and C9 have no human author, C2, C15 and C17 say that AI drafted parts, and the others are human papers. The second is whether the claim has a node, that is, a statement in the map of the project and in Lean: C1, C2, C5, C13 and C14 have one, as S22, S25, S27, S47 and S57. The third is what depends on what. C10 rests on C3 for its Corollary 1.2. C4 turns non-vanishing into abundance, so with the 4-fold non-vanishing of C3 it would give abundance for lc 4-folds, and both are claimed. C1 implies the part of C2 in dimension 4 with a rational boundary, but C2 covers every dimension.

### Examples

**Example 16.4.4 (a claim with a node and a claim without one).** Claim C14 is the negation of a conjecture, and its first counterexample is finite: a quotient of $E^4$, for $E$ the Fermat cubic, with 81 fixed points of type $\frac13(1,1,1,1)$, $D^4 = 72$ and $h^0(mD) = 3(m^4 - 1)$, so $H^0(D) = 0$. These are the numbers of target O-R1-1 in spec 04.2. Its node S57 states the negation in Lean, with the class claimed, and keeps that class until a referee accepts the paper. Claim C12 has no node: its content is a list of inequalities and a moduli count, and the route checks it as a certificate (experiment E1), not as a statement.

**Example 16.4.5 (one claim, two routes).** Claim C1 is checked by route R2, which audits the Lean code, and not by route R1. The Lean code of AxiomMath/MMP is already checked by the Lean kernel; what is unchecked is whether its definitions mean what KM98 and BCHM10 mean. Section 16.4.2 gives the steps.

### Lean

The Lean statements of the claims with a node are listed in Section 16.4.3, with the fidelity checks that each has passed. The table of this section has no Lean of its own. Of the declarations named by the five claim nodes, those of S27 (`MinimalModel.GeneralizedLcFlips`) and S47 (`MinimalModel.BSemiampleness`) are not in mmp-lean at commit 8028303.

### Notes and history

The list of claims is spec 01.3 of tamnd/mmp, and the records are the directory `claims/` at commit b1f85dd. Volume 17 reports the same claims from the side of the open problems: Section 17.1.2 for termination. A claim record changes only when the reader role of the project reads the claim (spec 10.3); the title field of each record stays empty until then, and on 2026-11-28 every title field is empty.

**Questions for a reader.**

- Which of the fresh claims has a part small enough to check by hand in a day? Section 16.4.3 gives the project's choice.
- Which claims would change Volumes 1 to 15 if a referee accepted them? C1 would change the statement of termination in dimension 4; C14 would change the statement of effective non-vanishing.
