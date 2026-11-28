---
title: The minimal model program for compact Kähler 3-folds
nodes: [MMK4VRWSWA, MMH0CM56AA]
sources: [HP16, BDPP13, KM98, Mor88]
reads_with: []
requires: ["1", "9", "12"]
level: research
kind: survey
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The minimal model program for compact Kähler 3-folds

### Statement

Let $X$ be a normal compact complex space. It is *Kähler* if it has a Kähler form in the sense of local potentials: a closed positive $(1,1)$-form, locally $i \partial \bar\partial$ of a smooth strictly plurisubharmonic function on local embeddings. Divisors, $\mathbb{Q}$-factoriality and the classes of singularities (terminal, canonical, klt, lc) are defined as for varieties, by discrepancies on a resolution. The real space $N^1(X)$ is replaced by the Bott-Chern cohomology $H^{1,1}_{BC}(X)$, which contains the classes of all line bundles and also transcendental classes.

A compact Kähler 3-fold may contain no curves at all. So the cone of curves $\overline{NE}(X)$ is too small, and the program uses the larger cone $\overline{NA}(X) \subset H^{2,2}_{BC}(X)$, the closure of the cone of classes of positive closed currents of bidimension $(1,1)$. It contains $\overline{NE}(X)$. A class $\alpha \in H^{1,1}_{BC}(X)$ is *nef* if it is a limit of Kähler classes. HP16 use $\overline{NA}(X)$ as the cone dual to the nef cone, so that a class is nef when it is nonnegative on $\overline{NA}(X)$.

**Theorem 16.2.1 (the minimal model program for Kähler 3-folds, Höring and Peternell).** Let $X$ be a $\mathbb{Q}$-factorial compact Kähler 3-fold with terminal singularities. Then there is a finite sequence of divisorial contractions and flips $X = X_0 \dashrightarrow X_1 \dashrightarrow \cdots \dashrightarrow X_m$ of $\mathbb{Q}$-factorial compact Kähler 3-folds with terminal singularities such that $K_{X_m}$ is nef or $X_m$ has a Mori fibre space structure $X_m \to Y$.

Node: MMK4VRWSWA

Lean: not yet in Lean.

This is statement S59. The case $K_X$ pseudo-effective is HP16; the case of a Mori fibre space is the companion work of Höring and Peternell on Mori fibre spaces for Kähler 3-folds. Das and Hacon extended the program to klt pairs. Each step has an analytic cone theorem behind it: the $K_X$-negative part of $\overline{NA}(X)$ is spanned by countably many classes of rational curves, as in the projective case.

**Theorem 16.2.2 (abundance for Kähler 3-folds, Campana, Höring and Peternell).** Let $X$ be a compact Kähler 3-fold with terminal singularities and $K_X$ nef. Then $K_X$ is semiample.

Lean: not yet in Lean.

Log abundance for klt Kähler 3-fold pairs is due to Das and Ou, and slc abundance to S. Das (arXiv:2604.28085), as spec 01.5 records them. Termination of terminal 3-fold flips holds in the Kähler case by the difficulty argument of the projective case: Shokurov's difficulty counts the exceptional divisors of small discrepancy, and the count does not use projectivity. The projective statement is this one.

Node: MMH0CM56AA · Lean: `MinimalModel.ThreefoldTermination`

### Proof in words

**Why currents.** In outline, as HP16 present it: on a projective 3-fold the cone theorem comes from the basepoint free theorem, which uses ample divisors. A Kähler class is not the class of a divisor, so that route is closed. Höring and Peternell work in $H^{1,1}_{BC}(X)$ with the dual cone $\overline{NA}(X)$. The key input for $K_X$ pseudo-effective is that a Kähler 3-fold with $K_X$ pseudo-effective and not nef has a $K_X$-negative rational curve: either $X$ is covered by rational curves, or the negative part of the divisorial Zariski decomposition of $K_X$ (Boucksom) gives a surface on which the program for surfaces produces the curve. If $K_X$ is not pseudo-effective, a theorem of Brunella on foliations shows that $X$ is uniruled (in the projective case this is BDPP13), and the work on Mori fibre spaces constructs the contraction.

**Contractions and flips.** In outline: a $K_X$-negative extremal ray $R$ of $\overline{NA}(X)$ is cut out by a nef class $\alpha$ with $\alpha^\perp \cap \overline{NA}(X) = R$. When $R$ is a ray of curves that cover a surface or a curve, the contraction is built from $\alpha$ analytically, by results of Grauert type on the contraction of exceptional sets. The flips of 3-folds are local over the base of the contraction, and Mori's flip theorem (Mor88) is proved by a local argument over the base, which applies over an analytic germ.

**Abundance.** In outline, the argument of Campana, Höring and Peternell splits by the algebraic dimension $a(X)$: if $a(X) = 3$, $X$ is Moishezon and the projective methods apply; if $a(X) \le 2$, the algebraic reduction is a fibration whose general fibre is a torus or a curve, and the canonical bundle formula of Chapter 16.1 gives the semiampleness on the base.

### Examples

**Example 16.2.3 (a divisorial contraction to a torus).** Let $T = \mathbb{C}^3/\Lambda$ be a general complex torus of dimension 3. It is Kähler, it is not projective, and it contains no curve and no surface. Let $\pi \colon X \to T$ be the blow-up of a point, with exceptional divisor $E \cong \mathbb{P}^2$. Then $K_X = \pi^* K_T + 2E = 2E$. A line $l \subset E$ has $E \cdot l = -1$, so $K_X \cdot l = -2$. Every curve of $X$ lies in $E$, since its image in $T$ is a point, so $\overline{NE}(X) = \mathbb{R}_{\ge 0}[l]$. The program contracts this ray, the contraction is $\pi$, and $K_T = 0$ is nef. So $T$ is the minimal model of $X$, reached in one divisorial step. Here $\overline{NA}(X)$ is much larger than $\overline{NE}(X)$: it contains the classes $\pi^*\omega^2$ for Kähler forms $\omega$ on $T$, and $K_X \cdot \pi^*\omega^2 = 2 E \cdot \pi^* \omega^2 = 0$.

**Example 16.2.4 (a Mori fibre space over a non-projective base).** Let $S$ be a K3 surface with Picard number 0. It is Kähler, not projective, and contains no curve. Let $X = S \times \mathbb{P}^1$. Then $K_X = p_2^* K_{\mathbb{P}^1}$, and a fibre $\ell = \{s\} \times \mathbb{P}^1$ has $K_X \cdot \ell = -2$. Every curve of $X$ is a fibre, since its image in $S$ is a point. So $\overline{NE}(X) = \mathbb{R}_{\ge 0}[\ell]$, the ray is $K_X$-negative, and its contraction is the projection $X \to S$, a Mori fibre space over a base that is not projective. The program stops at once.

**Example 16.2.5 (a nef class that kills no curve).** On the torus $T$ of the first example, $\overline{NE}(T) = 0$, so every class is nef on curves. But not every class of $H^{1,1}_{BC}(T)$ is nef: a class $\alpha$ with $\alpha^3 < 0$ is not a limit of Kähler classes. So nefness on curves is not nefness, and a cone theorem in terms of curves alone would say nothing on $T$. This is the reason for the cone $\overline{NA}(X)$.

### Lean

On 2026-11-28 the library mmp-lean has no Kähler spaces, and Mathlib has none (spec 01.9 lists Kähler manifolds among the missing parts of Mathlib). Spec 06.2 lists S59 (`KahlerThreefoldMMP`) with vocabulary "missing (Kähler)" and plans it at milestone S6. A `git grep` of the library finds no declaration of that name. `MinimalModel.ThreefoldTermination` is a statement about projective 3-folds over a field, stated as a `def` with no proof.

### Notes and history

The program is HP16 and its companion on Mori fibre spaces, with the klt case of Das and Hacon; abundance is Campana-Höring-Peternell (Ann. Sci. ENS 2016), log abundance Das-Ou, slc abundance S. Das, arXiv:2604.28085, as spec 01.5 lists them. The records give expert status only for HP16, through its row in spec 01.5; the other papers have no paper record in the map. For the projective statements used in the proofs, see KM98 and BDPP13.

**Questions for a reader.**

- Which parts of the cone theorem of HP16 need $X$ to be a 3-fold, and which hold for a $\mathbb{Q}$-factorial klt compact Kähler space of any dimension?
- The flips of the theorem are local analytic objects. Does the analytic flip of a projective morphism of complex spaces (spec 01.5: Fujino; Das-Hacon-Păun) give them directly?
