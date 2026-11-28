---
title: Mori's theorem and the general elephant
nodes: []
sources: [Mor88, KM92, KM98, Kol92, Rei83b]
reads_with: [Mor88:0, KM92:1]
requires: [1.1, 4.4, 4.3]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Mori's theorem and the general elephant

### Statement

The setting is that of Section 1: $f \colon (X \supset C) \to (Z \ni z)$ is a flipping extremal neighbourhood (Definition 8.2.1), or $f \colon X \to Z$ is a flipping contraction of an algebraic 3-fold with terminal singularities. By Corollary 4.4.18, every point $P \in X$ of index $m \ge 2$ is a quotient of an isolated cDV point by a cyclic group $\mu_m$, and its analytic type is one of those of Mori's list (Theorem 4.4.26).

**Definition 8.2.8 (the general elephant).** Let $X$ be a normal variety or analytic germ with $|-K_X| \ne \emptyset$. A *general elephant* of $X$ is a general member $E \in |-K_X|$, that is a general effective Weil divisor linearly equivalent to $-K_X$. For a germ $(X \supset C)$ along a curve, $|-K_X|$ is the linear system of the germ, and $E$ is a general member that may or may not contain $C$.

**Theorem 8.2.9 (Mori's flip theorem).** Let $X$ be a 3-fold with terminal singularities and $f \colon X \to Z$ a flipping contraction. Then the flip $f^+ \colon X^+ \to Z$ of $f$ exists.

Lean: not yet in Lean.

**Theorem 8.2.10 (the general elephant of an extremal neighbourhood).** Let $f \colon (X \supset C) \to (Z \ni z)$ be a flipping extremal neighbourhood. Then a general elephant $E \in |-K_X|$ is a normal surface with only Du Val singularities, and $f(E) \in |-K_Z|$ is a Du Val singularity of $Z$ at $z$.

Lean: not yet in Lean.

**Corollary 8.2.11 (the flip of a terminal 3-fold).** Let $X$ be a projective 3-fold with terminal singularities and $f \colon X \to Z$ a flipping contraction, with flip $f^+ \colon X^+ \to Z$ given by Theorem 8.2.9.

1. $X^+$ has terminal singularities, and $a(E, X^+) > a(E, X)$ for every divisor $E$ whose centre on $X$ lies in $\operatorname{Exc}(f)$.
2. $\operatorname{Exc}(f^+)$ is a curve, $f^+$ is an isomorphism over $Z \setminus f(\operatorname{Exc}(f))$, and $X^+$ has only finitely many singular points.
3. If $X$ is $\mathbb{Q}$-factorial and $f$ is the contraction of an extremal ray, then $X^+$ is projective and $\mathbb{Q}$-factorial with $\rho(X^+) = \rho(X)$ and $\rho(X^+/Z) = 1$.

Lean: not yet in Lean.

Theorems 8.2.9 and 8.2.10 are cited from Mor88 and KM92 and are not proved in this handbook. Corollary 8.2.11 is proved in full from them and Chapter 1. Mori proved the existence of flips for every flipping extremal neighbourhood in the analytic category and deduced the algebraic case; the general elephant theorem in the generality stated, with the classification of extremal neighbourhoods, is due to Kollár and Mori. A second proof of Theorem 8.2.9, independent of the classification, is Shokurov's, in Chapter 3.

### Proof in words

Mori's proof is a classification. The general elephant controls everything: if $E \in |-K_X|$ is a Du Val surface, then on $E$ the flipping curve is a configuration of curves on a Du Val surface, and the flip is constructed from the minimal resolution of $E$ and the contraction of $C$ on $E$, a computation that ends with an explicit description of $X^+$ in each case. To find a Du Val elephant one works point by point along $C$: at each non-Gorenstein point of the curve the local analytic type is on Mori's list, and the condition $-K_X \cdot C > 0$, the vanishing $R^1 f_* \mathcal{O}_X = 0$ of Proposition 8.2.2 and its refinements give strong restrictions on the possible configurations, which are then handled one by one.

The corollary is the theory of Chapter 1 applied to the flip once it exists: discrepancies go up, the exceptional loci correspond, and the class of projective $\mathbb{Q}$-factorial varieties is preserved for extremal rays.

### Examples

**Example 8.2.12 (the elephant of the Francia flip).** In Proposition 8.1.13, $-K_{X^-} = D_1 + D_2 + D_3 + D_4$. A general member of $|-K_{X^-}|$ near $C^-$ is the divisor of a general semi-invariant section, and at the $\frac12(1,1,1)$ point $P$ it is the image of a quadric cone section: $|-K|$ near $P$ consists of the images of the surfaces $\{h = 0\}$ with $h$ an odd function on $\mathbb{A}^3$, such as a general linear form, and $\{\ell = 0\}/\mu_2 = \mathbb{A}^2/\pm 1$ is an $A_1$ point. So the general elephant passes through $P$ with a Du Val singularity of type $A_1$, as Theorem 8.2.10 asserts at this point.

**Example 8.2.13 (an elephant at a smooth point).** At a smooth point of $X$ the general elephant is a smooth surface, the zero set of a general local section of $\omega_X^{-1}$. At a point of type $\frac1n(1, -1, 1)$, with coordinates $x, y, w$ of weights $1, -1, 1$, the invariants of $\omega^{-1}$ correspond to the semi-invariant functions of weight $1$ times the generator $(dx \wedge dy \wedge dw)^{-1}$ of weight $-1$, and a general one is $x + w + \text{higher terms}$; the elephant is $\{x + w = 0\}/\mu_n \cong \mathbb{A}^2_{y, w}/\frac1n(-1, 1)$, a Du Val singularity of type $A_{n-1}$ (Theorem 4.3.13).

**Example 8.2.14 (the types of Kollár and Mori, in outline).** For an extremal neighbourhood with irreducible $C$, Kollár and Mori sort the possibilities by the non-Gorenstein points of $X$ on $C$ and their position relative to $C$, and by the behaviour of a general member $H$ of the linear system of $f^* \mathfrak{m}_z$, the pullback of a general hyperplane section of $Z$ through $z$. The neighbourhood is *semistable* if the image $f(H)$ is a Du Val singularity of type $A$; this happens in the two types called k1A and k2A, with one or two non-Gorenstein points on $C$, each of type IA, that is a terminal cyclic quotient point or a terminal point of type $cA/m$ meeting $C$ in a particular way. The remaining types, called cD/2, cAx/2, cE/2, cD/3, IIA, IIB and IC in KM92, have a single non-Gorenstein point, of the indicated local type, and are the *exceptional* ones. This description is an outline only: the precise definitions of the types, and the proof that the list is complete, occupy KM92, and the statements here should be checked against that source.

### Proof

*Theorems 8.2.9 and 8.2.10.* Cited: Mor88 for the existence of flips and the general elephant in the cases needed for the existence proof, and KM92 for the general elephant theorem and the classification. The reduction from the algebraic contraction to its analytic germs at the finitely many points of $f(\operatorname{Exc}(f))$ is Lemma 8.2.4 and the comparison of formal and analytic algebras explained after it.

*Corollary 8.2.11.* Part 1. A terminal variety is klt, and $K_X$ is $\mathbb{Q}$-Cartier with $-K_X$ ample over $Z$, so $f$ is a flipping contraction of the pair $(X, 0)$ in the sense of Definition 8.1.1. By Corollary 8.1.20, $X^+$ is terminal, and the strict inequality is Lemma 8.1.19.

Part 2. By Lemma 8.1.18, $f^+$ is an isomorphism over $Z \setminus S$, where $S = f(\operatorname{Exc}(f))$ is finite since $\operatorname{Exc}(f)$ is a curve, and $\operatorname{Exc}(f^+) = f^{+\,-1}(S)$ is the union of finitely many fibres. Since $f^+$ is small and $X^+$ is a 3-fold, these fibres have dimension at most $1$, and they are nonempty curves since $f^+$ is not an isomorphism (part 2 of the proof of Proposition 8.1.17 shows this for any flip). The singular points of $X^+$ are isolated by Theorem 4.4.15, as $X^+$ is terminal by part 1, so there are finitely many.

Part 3. A terminal pair is klt, so Proposition 8.1.17 applies with $\Delta = 0$.

### Exercises

1. (A) In Example 8.2.12, compute the general elephant of $X^-$ near a smooth point of $C^-$, and show that it does not contain $C^-$ for a general choice.
2. (A) Show that the general elephant of $X^+$ in the Francia flip, a general member of $|-K_{X^+}|$, contains the flipped curve $C^+$, by computing $-K_{X^+} \cdot C^+$.
3. (A) Let $(X, P)$ be the terminal point $\frac13(1, 2, 1)$. Write down the general elephant at $P$ and identify its Du Val type.
4. (B) In Example 8.2.13, verify the weight computation for $\omega_X^{-1}$ at a point $\frac1n(1, -1, 1)$, and show that for $n \ge 2$ every member of $|-K_X|$ passes through the point and is singular there.
5. (B) Let $f$ be a flipping contraction of a terminal 3-fold with a single irreducible flipping curve $C$ through one non-Gorenstein point $P$ of index $m$. Using Corollary 8.2.11 and Lemma 8.1.19, show that every divisor $E$ with centre $P$ on $X$ has $a(E, X) \in \frac1m \mathbb{Z}_{>0}$, so $a(E, X) \ge \frac1m$, and $a(E, X^+) > a(E, X)$.
6. (C) For the family of Example 8.1.14, describe a general member $H$ of the pullback of a general hyperplane section of $Z$ through the vertex, and show that $f(H)$ is a Du Val singularity of type $A$, so that these flips are semistable in the sense of Example 8.2.14.

### Lean

Nothing in this section is in Lean. The library has `MinimalModel.ThreefoldFlips` for the existence of 3-fold klt flips, which contains Theorem 8.2.9 and is treated in Chapter 3.

### Notes and history

Mori's theorem (Mor88) completed the minimal model program for 3-folds, with the cone and contraction theorems of Volume 1 and the termination of Chapter 4. Reid's idea of the general elephant (Rei83b) organised the search for flips, and Kollár and Mori proved it for all extremal neighbourhoods together with a classification of the semistable ones and a description of the flips in KM92. The point of view of KM98, Chapter 6, is that of flops, where the general elephant is used in the same way, and KM98, Chapter 7, uses semistable extremal neighbourhoods; the proof of Theorem 8.2.9 is not given in KM98. Shokurov's proof via pl flips (Sho92), and its account in Cor07, give a proof that does not need the classification, and it is the one that generalises to higher dimension.
