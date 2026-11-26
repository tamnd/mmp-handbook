---
title: Termination in dimension 5 and higher
nodes: [MMTJ3YNHTG, MMFCAWE0XH, MM3YGGD1TZ, MMQHRKKEZY, MMGSDKRGR6]
sources: [BCHM10, HLZ25, Sho04, HL25]
reads_with: []
requires: ["10"]
level: research
kind: survey
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Termination in dimension 5 and higher

### Statement

The conjecture is T(n) of Section 1.1 for $n \ge 5$. On 2026-11-26 it is open, and no claim in the records covers it without a bigness hypothesis.

Node: MMTJ3YNHTG · Lean: `MinimalModel.Termination`

Two results bear on it. Each is a theorem in refereed work.

**Theorem 17.1.13 (ACC for log canonical thresholds).** Fix $n$, a set $I \subseteq [0, 1]$ and a set $J \subseteq [0, \infty)$ that satisfy the DCC. The set of the thresholds $\operatorname{lct}(X, \Delta; M)$, for lc pairs $(X, \Delta)$ of dimension $n$ with coefficients in $I$ and effective $\mathbb{R}$-Cartier divisors $M$ with coefficients in $J$, satisfies the ACC.

Node: MMGSDKRGR6 · Lean: `MinimalModel.ACCLct`

**Theorem 17.1.14 (The Sarkisov program).** Two Mori fibre space outputs of programs from one klt pair are joined by a finite chain of Sarkisov links of types I to IV.

Node: MM3YGGD1TZ · Lean: `MinimalModel.Sarkisov`

The strong form of the Sarkisov program is a conjecture.

**Conjecture 17.1.15 (The strong Sarkisov program).** In dimension $n$, the chain of links of the Sarkisov program can be chosen with a decreasing Sarkisov degree.

Node: MMQHRKKEZY · Lean: `MinimalModel.StrongSarkisov`

The strong form is a theorem for $n \le 4$ (He, arXiv:2311.08750, JPAA 230 (2026)) and is claimed for all $n$ by Hashizume (arXiv:2609.33679, Corollary 1.7). It is open in refereed work for $n \ge 5$.

### Proof in words

In dimension 5 and higher, three kinds of results are known or claimed.

- **A big boundary.** The program with scaling is finite for a klt pair with a big boundary (BCHM10, Corollary 1.4.2; Section 1.1). Each program is claimed to be finite in dimension at most 5 (HLZ25) and in all dimensions (Hashizume) when $\Delta$ or $K + \Delta$ is big (Section 1.2).
- **Special termination.** T(m) for each $m < n$ gives special termination in dimension $n$ (statement S19). The records cite Fujino, and Lazić, Moraga and Tsakanikas (arXiv:2007.06458), for it (spec 07, row T8-03).
- **Reductions.** Shokurov's reduction and the Han-Liu reduction hold in each dimension (Section 1.1). Their hypotheses are open from dimension 3 or 4 on (Chapter 3).

The step from dimension 4 to dimension 5 has a known shape for pairs of non-negative Kodaira dimension. Birkar (math/0502116, row T8-02 of spec 07) shows that the ACC for log canonical thresholds and special termination give termination for pairs with $\kappa(K + \Delta) \ge 0$. The ACC for log canonical thresholds is a theorem (Hacon, McKernan and Xu, arXiv:1208.4150). Special termination in dimension 5 needs T(4). So T(4) with Birkar's reduction may give termination for effective lc 5-folds. The records do not settle this. Item 5 of spec 01.16 asks for the exact hypothesis of Birkar 0804.4587, and asks whether T(4) and Birkar's reduction give termination for effective lc 5-folds (D §23.2). The records do not say which of the two Birkar papers carries the hypothesis that matters.

So even if the audit of Section 7.3 turns the claim C1 into a theorem, it gives T(4) only for a rational boundary. A step to effective lc 5-folds then needs the same reduction for a rational boundary, or a real boundary in dimension 4.

The case $\kappa(K + \Delta) = -\infty$ in dimension 5 has no reduction of this kind in the records. Each program for such a pair ends with a Mori fibre space if it ends at all, but the records give no tool that bounds the number of flips before that end, except bigness and the ACC route.

### Examples

The first test cases in dimension 5 are the two targets of route R4 that name dimension 5.

- **O-R4-9.** Special termination in dimension 5 with $\lfloor B \rfloor$ irreducible. This is Conjecture 1.7 of Liu-Xu, as spec 04.5 gives it. Spec 04.5 rates its difficulty 2 (D §20 #12).
- **O-R4-10.** T(5) for effective lc pairs, from T(4) and Birkar's reduction, after the recheck of D §23.2. Spec 04.5 rates it 3 if the reduction applies [U].

A third test case is quantitative. HLZ give explicit bounds on the number of steps in dimension at most 4 for a big boundary. Target O-R1-10 names explicit bounds in dimension 5 as a research extension (target #22 of report D). The records do not say whether any bound in dimension 5 is known.

### Lean

`MinimalModel.Termination 5` is the statement of T(5) in the library. It is the same Lean statement as for $n = 4$, at a different argument. `MinimalModel.SpecialTermination n` takes T(m) for $m < n$ as a hypothesis, so a Lean proof of O-R4-9 can state its input as a named hypothesis.

`MinimalModel.ACCLct` is stated, with no proof. `MinimalModel.Sarkisov` and `MinimalModel.StrongSarkisov` are not in `records/lean.json` on 2026-11-26. The notes of the nodes say that the vocabulary of Sarkisov links is missing, and plan the statements for milestones S3 (S36) and S4 (S38).

### Notes and history

**Claims of 2025 and 2026.** Hashizume (C2, `claims/arXiv-2609-33679.yaml`, status fresh) claims termination for a big boundary in all dimensions and the strong Sarkisov program for all $n$. HLZ (paper record HLZ25, expert status claimed) claim the case of dimension at most 5. No claim in the records covers T(5) without bigness. Spec 03.11 gives the arrow "Hashizume Thm. 1.1 and He (dim 4) give the strong Sarkisov program in all $n$", with the source rated [P].

**Routes.** Route R4 (weight 0.10) has the targets O-R4-9 and O-R4-10. Route R1 has O-R1-5 for the core of Hashizume. The lab has experiment E8 for the HLZ bounds.

**References.** BCHM10; HLZ25; Sho04; HL25; arXiv:2609.33679 (Hashizume); arXiv:2311.08750 (He); math/0502116 (Birkar); arXiv:1208.4150 (Hacon, McKernan and Xu); arXiv:2007.06458 (Lazić, Moraga and Tsakanikas); arXiv:0905.0946 (Hacon and McKernan) for the Sarkisov program.

**Questions for a reader.**

- What is the exact hypothesis of Birkar's reduction on the boundary: rational, real, or with coefficients in a DCC set?
- Does special termination in dimension 5 need T(4) for all lc 4-folds, or only for the lc centres that appear, which are of dimension at most 4 and have a special boundary?
- Is there a pair of dimension 5 with $\kappa = -\infty$ for which no known method bounds the number of flips, and which is small enough to compute?
