---
title: Summary and pointers
nodes: []
sources: [KM98, Kol92, BCHM10, Kaw92, Sho04, Kaw08]
reads_with: [KM98:6, BCHM10:main]
requires: [3.6, 7.2]
level: core
kind: survey
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Summary and pointers

### Statement

This section is a survey. It states what the volume proves, what it cites, and where the theory continues.

What is proved in full. The definitions and uniqueness of flips and flops, with the Atiyah flop, the Francia flip and the weighted blow-up of a point of type $\frac12(1,1,1)$ (Chapter 1). The comparison of discrepancies under flips and the termination of flips of terminal and canonical 3-folds by Shokurov's difficulty (Chapter 4, Theorems 8.4.11 and 8.4.12). The assembly of the 3-fold program from the cone, contraction and flip theorems (Theorem 8.5.3), crepant terminal models of canonical 3-folds and small $\mathbb{Q}$-factorializations of terminal ones (Theorem 8.5.11 and Corollary 8.5.13), the agreement of minimal models in codimension one (Proposition 8.5.20) and the pagoda computation (Proposition 8.5.24). The relative Zariski lemma and the program for semistable families of surfaces with trivial canonical class (Proposition 8.6.3, Theorem 8.6.4 and Corollary 8.6.5).

What is proved in outline or cited. Mori's flip theorem and the classification of extremal neighbourhoods (Chapter 2), Shokurov's 3-fold log flips and the reduction to pl flips (Chapter 3), termination of 3-fold log flips (Theorem 8.4.21) and of 4-fold terminal and canonical flips (Theorems 8.4.22 to 8.4.24), the lc 3-fold program (Theorem 8.5.4), Kollár's theorem on flops (Theorem 8.5.22, sketched), Kawamata's extension to all dimensions (Theorem 8.5.23), semistable reduction (Theorem 8.6.2), semistable flips (Theorem 8.6.6) and Kulikov models (Theorem 8.6.7).

### Proof in words

Every step of the 3-fold program has three parts: find a $K$-negative extremal ray, contract it, and if the contraction is small, flip it. Volume 7 supplies the first two in every dimension. This volume supplies the third in dimension $3$ and the proof that the steps stop. In higher dimensions the third part is the existence of flips for klt pairs, which is the theorem of Birkar, Cascini, Hacon and McKernan (BCHM10), proved by Shokurov's reduction to pl flips and an induction on the dimension; this is Volume 9. Termination in general is open. What is known, special termination, termination with scaling, termination in dimension 4 and the reductions to the ACC and semicontinuity conjectures for minimal log discrepancies (Sho04), is in Volume 10 and Volume 17.

### Examples

**Example 8.6.11 (one step, every chapter).** Let $X^- \to Z$ be the Francia flipping contraction, with $K_{X^-} \cdot C^- = -\frac12$ and the flip $X^+$ with $K_{X^+} \cdot C^+ = 1$. Chapter 1 defines the flip and shows that it is unique. Chapter 2 constructs it as a case of Mori's theorem, and Volume 3 constructs it torically. Chapter 4 computes $d(X^-) = 1$ and $d(X^+) = 0$, so a $K$-MMP through $X^-$ contains at most one flip after it reaches $X^-$, unless a divisorial step intervenes (Example 8.4.16). Chapter 5 places the flip in a program over $Z$, which ends at $X^+$, a minimal model over $Z$. In the toric description of Volume 3 (Theorem 3.6.8), the same flip is a wall crossing in the secondary fan, and this point of view is the one that Volume 9 generalizes with the MMP with scaling.

### Lean

`MinimalModel.ThreefoldFlips`, `MinimalModel.ThreefoldTermination` and `MinimalModel.ThreefoldLcMMP` state the main theorems of the volume without proof. `MinimalModel.KltFlips` and `MinimalModel.Termination` state the general existence of klt flips and the termination conjecture, for Volumes 9 and 10.

### Notes and history

The 3-fold program is due to Mori, Shokurov, Kawamata, Kollár and Reid in the 1980s and early 1990s; KM98 and Kol92 are the standard accounts, and Corti's volume on flips gives the modern account of Shokurov's pl flips. Volume 9 proves the existence of minimal models for varieties of general type in all dimensions (BCHM10). Volume 10 treats abundance for 3-folds (Kol92), termination in dimension 4, and the Sarkisov program, which relates the different Mori fibre spaces that a program can produce, as in Examples 8.5.6 and 8.5.7. Volume 11 treats the program in positive and mixed characteristic, where Kawamata's semistable program (Kaw94) was an early case, and Volume 13 treats moduli of stable varieties, for which semistable reduction and the semistable program of Chapter 6 are the local input.
