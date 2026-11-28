---
title: The claim checks of route R1
nodes: [MMY38TT73M, MM2NY6352R, MMRG60YPYS]
sources: [Ajit26, BDY26, HLZ25, OAI26, Laz04]
reads_with: []
requires: ["16.1", "16.3"]
level: research
kind: survey
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The claim checks of route R1

### Statement

Route R1 of tamnd/mmp checks fresh claims formally. It does not try to formalize a whole paper. A formal check of one part that is new, self-contained and checkable is evidence that no referee can give, and it is cheap compared with a full proof. Its weight in the plan of the project is 0.20, the highest of the routes.

**Definition 16.4.9 (the four steps of a claim check).** For each claim, route R1 does four things (spec 04.2):

1. it writes a claim record, with the date and the status;
2. it states the main theorem in Lean as a `def` of type `Prop`, with the class claimed;
3. it maps the dependencies of the claim, and marks those that are themselves unrefereed;
4. it picks the smallest part that is new, self-contained and checkable: a finite computation, a combinatorial lemma, a numerical inequality, or an implication between named hypotheses.

**Remark 16.4.10 (a check of a part is not a check of the claim).** A Lean proof of one part of a preprint says that this part is right. It says nothing about the other parts. So the record of a check names exactly the part checked (spec 14.3), the claim keeps the class claimed, and the credit line has the form "a Lean check of section X of [preprint] by the project" (spec 14.2).

On 2026-11-28 step 1 is done for every claim, and step 2 for the claims with a node. Steps 3 and 4 are not done for any claim. The Lean statements of step 2 are these.

**Remark 16.4.11 (claim of Han, Liu and Zhuang: termination for a big boundary in dimension at most 5).** Let $(X, \Delta)$ be a projective klt pair of dimension $n \le 5$ with $\Delta$ big or $K_X + \Delta$ big. Then each $(K_X + \Delta)$-program terminates.

Node: MMY38TT73M · Lean: `MinimalModel.TerminationBigLe5`

This is statement S24, claimed by HLZ25. It has no claim record of 2026, since the preprint is of 2025.

**Remark 16.4.12 (claim C2: termination for a big boundary in all dimensions).** Let $(X, \Delta)$ be a projective klt pair with $\Delta$ big or $K_X + \Delta$ big. Then each $(K_X + \Delta)$-program terminates.

Node: MM2NY6352R · Lean: `MinimalModel.TerminationBig`

This is statement S25, claimed by Hashizume, arXiv:2609.33679.

**Remark 16.4.13 (claim C14: effective non-vanishing fails in dimension 4).** There is a projective klt pair $(X, \Delta)$ of dimension 4 and a nef Cartier divisor $D$ with $D - (K_X + \Delta)$ nef and big and $H^0(X, D) = 0$.

Node: MMRG60YPYS · Lean: `MinimalModel.NotEffectiveNonVanishing4`

This is statement S57, the negation of the effective non-vanishing conjecture of Ambro and Kawamata in dimension 4. It is claimed by Ajit26 and keeps the class claimed until a referee accepts the paper. The statements S22 of claim C1 (Section 16.4.2), S27 of C5 (Section 16.1.2) and S47 of C13 (Section 16.1.1) complete the list.

### Proof in words

There is no proof in this section. What follows is the list of targets of route R1 in spec 04.2, with the part that each would check.

| Id | Claim | The part to check |
|---|---|---|
| O-R1-1 | C14, Ajit | the first example in full: the action on $E^4$ for the Fermat cubic $E$, the 81 fixed points of type $\frac13(1,1,1,1)$, $3K_X \sim 0$, $D^4 = 72$, $h^0(mD) = 3(m^4 - 1)$, so $H^0(D) = 0$ |
| O-R1-2 | C12, Bie, Du and Yu | the basket search and the inequalities behind $\mathrm{vol} \ge 1/420$, as a certificate (experiment E1) |
| O-R1-3 | C8, Han | the real analysis and the multiplicity inequality behind $C_0 \approx 1.77629$ |
| O-R1-4 | C4, J. Liu | the reduction as an implication between named statements, with each cited input a hypothesis |
| O-R1-5 | C2, Hashizume | the combinatorial core: the finiteness of the set of models met by a program, with the index bound and the finiteness of models of BCHM10 as hypotheses |
| O-R1-6 | C3, OpenAI 034 | the dependency map, with the step of log Iitaka subadditivity isolated as a named statement, and a search for a counterexample to it in toric and abelian cases |
| O-R1-7 | C17, Liu and Wang | the explicit example and its generalized lc ring |
| O-R1-8 | C5, Hu and Liu | the statement, and the equivalence of minimal models and termination with scaling as a reduction |
| O-R1-9 | C9, OpenAI 035 and BWX | a human audit of OpenAI 035 against Z. Xu, arXiv:2307.03938 |
| O-R1-10 | HLZ25 | the step bounds for 4-folds of general type as a computable function, with a certificate on examples |
| O-R1-11 | C10, Hacon and Wang | a citation audit: which results of which AI manuscripts it uses, and whether each is a theorem or a claim |
| O-R1-12 | C16, Landi | a Lean refutation of the false Lemma 3.2, if the counterexample is finite |

The first target is O-R1-1, because it is a disproof that is finite, new and certain if it is right: a group action on a product of four copies of one elliptic curve, a fixed point count, and Riemann-Roch on an abelian 4-fold, which the check would take as a named hypothesis.

**What is done.** On 2026-11-28, no target of the table is done. The lab of tamnd/mmp has two runs, both of 2026-11-26 and both of experiment E2, on minimal log discrepancies of cyclic quotient and simplicial singularities in dimension 3. Experiments E1, for C12, and E3, for C14, have no runs. Row Q10 of `records/trust.json`, which asks whether the authors of a checked claim have seen the result, is not run, because there is no check to send.

### Examples

**Example 16.4.14 (the leading term of O-R1-1).** Spec 04.2 describes the check as finite arithmetic over $\mathbb{F}_3^4$ and $\mathbb{Z}[\omega]$. Read it with the group $G = \mathbb{Z}/3$ acting on $A = E^4$ by the automorphism $\omega$ of the Fermat cubic $E$ on each factor; this reading is the handbook's, and the records do not state the group. The fixed points of $\omega$ on $E$ are the kernel of $1 - \omega$, which has degree 3, so $G$ has $3^4 = 81$ fixed points on $A$, each of type $\frac13(1,1,1,1)$, as the records say. The quotient map $\pi \colon A \to X$ has degree 3, so for $L = \pi^* D$ the self-intersection is $L^4 = 3 \cdot 72 = 216$, and Riemann-Roch on the abelian 4-fold gives $\chi(A, mL) = 216 \, m^4 / 4! = 9 m^4$. The invariant part has dimension $3 m^4$ to first order, which is the leading term of the claimed $h^0(mD) = 3(m^4 - 1)$. So the leading term is consistent with the records, and the content of the check is the constant term $-3$, which comes from the action on the fibres of $mL$ at the 81 fixed points and gives $h^0(D) = 0$ at $m = 1$.

**Example 16.4.15 (a dependency map).** For claim C10, spec 01.3 says that Corollary 1.2 rests on C3. The map of step 3 would have an edge from Corollary 1.2 of Hacon and Wang to the OpenAI family 034, marked unrefereed, and from 034 to its contested step, log Iitaka subadditivity. A reader of Corollary 1.2 then sees at once that it is no stronger than that step. This is target O-R1-11, the cheapest in the table.

### Lean

The fidelity record `records/fidelity.json` has entries for two of the statements of this section. `MinimalModel.NotEffectiveNonVanishing4` has the class claimed and passes F1 and F3 of its battery; it does not pass the battery. `MinimalModel.TerminationBigLe5` and `MinimalModel.TerminationBig` have no entry. None of the statements of step 2 has a proof, as a claimed statement must not.

### Notes and history

The route is spec 04.2 of tamnd/mmp; the claim records are `claims/` at commit b1f85dd; the trust rows are `records/trust.json` of 2026-11-26. Spec 04.2 names the first nodes of the route: the effective non-vanishing conjecture and its negation, the finite data of the first example of Ajit, the formula for $h^0(mD)$, the claim records of C12, C2, C3 and C4 with claimed statements, and the reduction of J. Liu as an implication.

**Questions for a reader.**

- Compute the constant term of $h^0(mD)$ in the first example above with the holomorphic Lefschetz formula at the 81 fixed points, and compare it with the claimed value $-3$.
- Which target of the table would change the most if it failed? A failure of O-R1-6 would touch claims C3, C4 and C10 at once.
