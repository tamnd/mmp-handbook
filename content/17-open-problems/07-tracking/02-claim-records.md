---
title: The claim records
nodes: [MMBTDMD2XP, MM2NY6352R, MMQMD68H79, MMRXDSNJQ7, MMRG60YPYS, MMY38TT73M]
sources: [OAI26, AxiomMMP, HLZ25, Ajit26]
reads_with: []
requires: ["0"]
level: research
kind: survey
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The claim records

### Statement

**Remark 17.7.3 (The rule for claims).** A fresh claim is never a hypothesis of another node (spec 06.6). It enters as a hypothesis only after experts accept its paper, and the paper record has `expert_status: accepted` (spec 07.13). Before that, the project says only "a Lean check of section X of the preprint found Y", and it writes to the authors before any page goes public.

**Remark 17.7.4 (The claims of 2025 and 2026).** Spec 01.3 lists 17 claims, C1 to C17. The project keeps them in 16 files in `claims/`. One file, `claims/openai-math.yaml`, holds the OpenAI families of C3, C6, C7, C8 and C9. This table gives each claim with its record and its status on 2026-11-26.

| Claim | Authors | What it claims | Record | Node | Status | Section |
|---|---|---|---|---|---|---|
| C1 | OpenAI 056; Axiom | every program for a projective lc 4-fold with rational boundary terminates | `AxiomMath-MMP.yaml`, `openai-math.yaml` | S22 | fresh | 1.2 |
| C2 | Hashizume | termination for klt pairs with $\Delta$ or $K + \Delta$ big, all dimensions; the strong Sarkisov program | `arXiv-2609-33679.yaml` | S25 | fresh | 1.2, 1.3 |
| C3 | OpenAI 034 | log abundance for rational boundary, all dimensions; 4-fold non-vanishing; the index conjecture for slc log CY pairs | `openai-math.yaml` | none | fresh; "contested" on one tracker [S] | 2.1, 2.2 |
| C4 | J. Liu | non-vanishing for smooth varieties implies abundance for lc pairs | `arXiv-2610-35913.yaml` | none | fresh | 2.2 |
| C5 | Hu, Liu | flips for all lc generalized pairs | `arXiv-2603-03817.yaml` | S27 | fresh | 1.2 |
| C6 | OpenAI 036 | generalized abundance | `openai-math.yaml` | none | fresh | 2.3 |
| C7 | OpenAI 033 | the Iitaka conjecture $C_{n,m}$ | `openai-math.yaml` | none | fresh | 2.3 |
| C8 | OpenAI 038; Han | Fujita freeness; a linear bound | `openai-math.yaml`, `arXiv-2609-01574.yaml` | none | fresh | 4.2 |
| C9 | OpenAI 035; BWX | 3-fold abundance in characteristic $p$ | `openai-math.yaml`, `arXiv-2610-10439.yaml` | none | fresh | 5.1 |
| C10 | Hacon, Wang | termination with scaling for Kähler klt pairs | `arXiv-2611-29683.yaml` | none | fresh | 6.2 |
| C11 | Hacon, Xie | the program for big gklt Kähler pairs | `arXiv-2607-24986.yaml` | none | fresh | 6.2 |
| C12 | Bie, Du, Yu | $\mathrm{vol} \ge 1/420$ for 3-folds of general type; a Fano volume bound | `arXiv-2611-12786.yaml` | none | fresh | 4.1 |
| C13 | BFMT; Hu, K. Liu, Shen | b-semiampleness | `arXiv-2508-19215.yaml`, `arXiv-2611-12744.yaml` | S47 | fresh | 2.3 |
| C14 | Ajit | counterexamples to effective non-vanishing, dimension $\ge 4$ | `arXiv-2610-09270.yaml` | S57 | fresh | 4.2 |
| C15 | J. Liu | a K-polystable 5-fold with no cscK metric | `arXiv-2608-19301.yaml` | none | fresh | 4.3 |
| C16 | Landi | the full LSC for mlds, and $\mathrm{mld} \le \dim$ | `arXiv-2611-30971.yaml` | none | withdrawn | 3.2 |
| C17 | Liu, Wang | a klt generalized pair with a generalized lc ring that is not finitely generated | `arXiv-2608-03258.yaml` | none | fresh | 2.3 |

Each file name has the prefix `claims/`. Of the 17 claims, 16 are fresh and one, C16, is withdrawn. No claim is read, checked, accepted or refuted in the records.

### Proof in words

**What a claim record holds.** Each record has a key, the authors, the source with its arXiv number or its address and its version, the date of the record, the date of the post where the records know it, a status, a route, the text of the claim, a node, a list `parts` and a list `letters`. On 2026-11-26 every record has the date 2026-11-26, the route R1, an empty `parts` list and an empty `letters` list. Every `title` field is empty. Each record says: "Nobody has read the claim for the project yet, and the title field stays empty until the reader role copies it from the source."

**How a claim moves.** The roles of the project move a claim in this order (spec 08.3 and spec 07.13).

1. The command `mmp claim add` writes the record with the status fresh.
2. The reader role reads the source and copies its title.
3. The reader and stater roles pick a self-contained part of the claim. It goes into the list `parts`.
4. The prover and refuter roles work on the part in Lean.
5. The project writes to the authors before any page goes public (spec 14.4). The letter goes into the list `letters`.
6. The claim becomes a hypothesis only after experts accept its paper.

A claim that the authors take back keeps its record with the status withdrawn. C16 is the only such claim on 2026-11-26.

**Claims with a node and claims without.** Five claims have a node in the map. C1 has S22, C2 has S25, C5 has S27, C13 has S47 and C14 has S57. The record of C13 by Hu, K. Liu and Shen has no node, while the record by BFMT has S47. S24 has the class claimed, but it has no claim record. Its source is the paper record HLZ25 (Section 1.2), and spec 01.3 does not give it a C number. The other twelve claims have no node. Some of them concern a statement of the map: C3 concerns S40 and S41, C6 concerns S45, C7 concerns S46 and C8 concerns S56. The records do not say why these claims have no node.

**Claims on claims.** Some claims use others. C10 rests on C3 through its Corollary 1.2 (Section 6.2). C1 has two parts, the paper of OpenAI 056 and the Lean code of Axiom, and the audit of Section 7.3 treats the second. Target O-R1-11, the same as O-R9-1, is the citation audit of C10.

### Examples

The first claim that route R1 checks is C14, the counterexamples of Ajit (milestone S1). Its first node is the arithmetic of the example: the intersection numbers, the values of $h^0$ and the singularities. Lab experiment E3 computes them. Section 4.2 gives the example. The records rate C14 "explicit and checkable; read by Totaro [R]". Spec 15 asks for the letter to the author at milestone S1.

A claim that is hard to check is C3, the log abundance of OpenAI 034. Target O-R1-6 asks for its dependency map, with the disputed step (log Iitaka subadditivity) as a named `Prop`.

### Lean

The Lean library states three claimed nodes: S22 (`MinimalModel.TerminationLc4Rational`), S24 (`MinimalModel.TerminationBigLe5`) and S25 (`MinimalModel.TerminationBig`). Each of the three is in `MinimalModel/Statements/Termination.lean`. S27, S47 and S57 have no Lean statement. No Lean proof of any part of a claim exists in the library on 2026-11-26.

Node: MMBTDMD2XP · Lean: `MinimalModel.TerminationLc4Rational`

### Notes and history

**Disputed earlier claims.** Spec 07.13 keeps one claim that is older than 2025 on its watch list: Chan (arXiv:2411.07129) on Fujita freeness in all dimensions, with the status disputed. Helmke found a gap (Section 4.2). The project has no file in `claims/` for it.

**Routes.** Route R1 (weight 0.20) is the formal check of fresh claims. It has the largest weight of all routes. Lab experiment E10 computes the explicit identities and numbers of each new claim of route R1.

**References.** OAI26 and AxiomMMP for C1; HLZ25 for S24; Ajit26 for C14. The arXiv numbers of the other claims are in the table and in the sections that it names.

**Questions for a reader.**

- Must the claims C3, C4, C6, C7, C8, C9, C10, C11, C12, C15 and C17 have nodes in the map?
- Must S24 have a claim record and a C number?
- Must the record of Hu, K. Liu and Shen point to S47, as the record of BFMT does?
- Must Chan's claim have a record with the status disputed?
