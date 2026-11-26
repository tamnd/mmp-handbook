---
title: Boundedness after BAB
nodes: [MMB93N0PQZ, MM3A7BTV1N, MM1B2V5Q7P]
sources: [BDY26]
reads_with: []
requires: ["12"]
level: research
kind: survey
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Boundedness after BAB

### Statement

**Theorem 17.4.1 (BAB).** Fix $n$ and $\epsilon > 0$. The $\epsilon$-lc Fano varieties of dimension $n$ form a bounded family.

Node: MMB93N0PQZ · Lean: `MinimalModel.BAB`

This is statement S53, a theorem of Birkar (arXiv:1603.05765 and 1609.05543, Ann. of Math.).

**Conjecture 17.4.2 (The index conjecture).** Let $(X, \Delta)$ be a klt log Calabi-Yau pair of dimension $n$ with the coefficients of $\Delta$ in a fixed finite set. Then the index of $K_X + \Delta$ is bounded by a number that depends only on $n$ and the set.

Node: MM3A7BTV1N · Lean: `MinimalModel.IndexConj`

This is statement S54. It is open in dimension at least 4.

**Conjecture 17.4.3 (The cone conjecture).** Let $(X, \Delta)$ be a klt Calabi-Yau pair. Then $\operatorname{Aut}(X)$ acts on the effective nef cone with a rational polyhedral fundamental domain. The same holds for the movable cone and the birational automorphisms.

Node: MM1B2V5Q7P · Lean: `MinimalModel.ConeConj`

This is statement S55, due to Kawamata and Morrison. It is open.

**Remark 17.4.4 (Claim C12: the volume bound 1/420).** A smooth projective 3-fold of general type has $\operatorname{vol}(K_X) \ge 1/420$.

This is claimed by Bie, Du and Yu (arXiv:2611.12786). The map has no node for it.

### Proof in words

**BAB and complements.** Birkar proves BAB and the boundedness of complements (arXiv:1603.05765; spec 01.7). His Fields Medal of 2018 cites BAB [S]. The ACC for log canonical thresholds (S48, Section 3.1) is a theorem, and volumes satisfy the DCC, not the ACC (spec 01.7). OpenAI family 066 claims bounded klt complements for Fano contractions and the Cartier conjecture of Birkar and Shokurov. The records hold this claim only in the catalogue of spec 01.7 [P, catalogue]. It has no claim record and no C number.

**The index conjecture, by dimension.** Spec 01.7 says that the conjecture is open in dimension at least 4 [S]. The records do not say which proof covers dimension 3 or less. OpenAI family 034 (claim C3) claims the index conjecture for slc log Calabi-Yau pairs, as one of its five claims (Section 2.2). Nakamura and Shibata show that the index conjecture fails outside the klt case (arXiv:2608.28038; Section 3.2).

**The cone conjecture, by dimension.**

- Dimension 2: the generalized cone conjecture is complete (Lazić, Stenger and Xie, arXiv:2608.26079, 2608.27001 and 2610.10115) [P].
- Dimension 3 and higher: Lutz (arXiv:2410.05949) calls the conjecture "wide open" for Calabi-Yau varieties of dimension more than 2 [S]. Spec 07 lists the known cases of Kawamata, Morrison and Totaro in row T10-11, rated [U], with no detail.

**Calabi-Yau varieties.** The boundedness of Calabi-Yau 3-folds is open. Elliptic Calabi-Yau 3-folds are bounded (Filipazzi, Hacon and Svaldi, JEMS 27 (2025), arXiv:2112.01352), and so are many elliptic Calabi-Yau 4-folds (Filipazzi and Xu, arXiv:2607.27048) [P]. Spec 04.7 calls Calabi-Yau 3-folds "the hard core of classification".

**Volumes.** J. A. Chen and M. Chen prove $\operatorname{vol}(K_X) \ge 1/1680$ for a smooth projective 3-fold of general type (arXiv:1302.0374, Compositio 151 (2014)). Claim C12 raises the bound to $1/420$. The records give the method in spec 03, Example 3.20: the proofs reduce to a finite search over baskets of terminal singularities and Riemann-Roch.

### Examples

**Claim C12 in detail.** The record `claims/arXiv-2611-12786.yaml` covers four preprints of Bie, Du and Yu: arXiv:2611.12786, 2611.18357 and 2610.10537 (spec 01.3), and arXiv:2611.14402 (row T10-08 of spec 07). The claims are:

- $\operatorname{vol} \ge 1/420$ for smooth projective 3-folds of general type;
- the moduli of canonical 3-folds of volume $1/420$ has one component of dimension 33 and two rigid points, which the authors call Vega and Altair;
- a sharp polynomial volume bound for $\epsilon$-lc Fano varieties, $\operatorname{Vol}(-K_X) \le C_n \epsilon^{-(2^n - n - 1)}$ (arXiv:2610.10537).

The record has the status fresh: unrefereed, and the moduli paper has code. It says: "Nobody has read the claim for the project yet." Spec 13.4 calls experiment E1 "the cheapest test of a 118-page claim".

**First test cases.**

- The index conjecture: klt log Calabi-Yau pairs of dimension 4 (O-R6-6, difficulty 3).
- The cone conjecture: one deformation class of Calabi-Yau 3-folds, with the invariance of Lutz and a Vinberg search (O-R6-7, difficulty 2 to 3; lab experiment E6, 100 to 1,000 core hours per class [U]). The full conjecture for Calabi-Yau 3-folds is O-R6-8 (difficulty 5).
- Boundedness of Calabi-Yau 3-folds: O-R6-9 (difficulty 5). The records name no smaller case.
- Claim C12: the basket search and the inequalities as a certificate (O-R1-2, difficulty 1, formal check 2). The sharp Fano volume bound in Lean for a fixed small dimension (O-R6-10, difficulty 2).

A known instance is the bound $1/1680$. Experiment E1 asks the lab to reproduce it with its extremal basket, before it checks the search of Bie, Du and Yu for $1/420$ with their code read as data. Experiment E5 checks $(-K)^3 \ge 1/330$ for terminal weak $\mathbb{Q}$-Fano 3-folds (J. A. Chen and M. Chen, arXiv:0712.4356; Jiang, arXiv:2109.03453) on the data of the Graded Ring Database. On 2026-11-26 the lab has no run of E1, E5 or E6.

### Lean

On 2026-11-26, `MinimalModel.BAB` (S53), `MinimalModel.IndexConj` (S54) and `MinimalModel.ConeConj` (S55) are not in `records/lean.json`. The nodes plan them in `MinimalModel/Statements/Boundedness.lean`, S54 for milestone S2 and S53 and S55 for milestone S3. The vocabulary of S54 is ready. S53 needs bounded families, and S55 needs automorphism groups. Spec 04.7 names the obstruction for the formalization: Calabi-Yau geometry needs Hodge theory for most statements, so the project states them on named hypotheses.

For C12, the certificate of a basket search (spec 13.5) states Reid's plurigenus formula and the Chen-Chen inequalities as named hypotheses. Lean checks the arithmetic with `norm_num` and `decide`. The result is `proved-mod` the named hypotheses.

### Notes and history

**Claims of 2025 and 2026.**

| Claim | What it claims | Record | Status |
|---|---|---|---|
| C12, Bie-Du-Yu | $\operatorname{vol} \ge 1/420$; the moduli at $1/420$; the sharp Fano volume bound | `claims/arXiv-2611-12786.yaml`, `papers/BDY26.yaml` | fresh; unrefereed |
| C3, OpenAI 034 | among five claims, the index conjecture for slc log Calabi-Yau pairs | `claims/openai-math.yaml` | fresh; no Lean |
| OpenAI 066 | bounded klt complements for Fano contractions; the Cartier conjecture of Birkar and Shokurov | none; spec 01.7 only | catalogue |

**Routes.** Route R6 (weight 0.10) has O-R6-6 to O-R6-10. Its first nodes are `index-conj-statement`, `cone-conj-statement` and `bab-statement`. Route R1 has O-R1-2. The lab has E1, E5 and E6.

**References.** BDY26; arXiv:1603.05765 and 1609.05543 (Birkar); arXiv:1208.4150 (Hacon, McKernan and Xu); arXiv:2410.05949 (Lutz); arXiv:2608.26079, 2608.27001 and 2610.10115 (Lazić, Stenger and Xie); arXiv:2112.01352 (Filipazzi, Hacon and Svaldi); arXiv:2607.27048 (Filipazzi and Xu); arXiv:1302.0374 and 0712.4356 (J. A. Chen and M. Chen); arXiv:2109.03453 (Jiang). Volume 12 treats boundedness and complements.

**Questions for a reader.**

- In which dimensions below 4 do the records hold the index conjecture as a theorem, and by which proof?
- Which known cases of the cone conjecture does row T10-11 of spec 07 mean?
- Does the search of E1 for $1/420$ use the same inequalities as the search for $1/1680$, or new ones?
