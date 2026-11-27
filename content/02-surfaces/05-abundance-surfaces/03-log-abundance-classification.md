---
title: Log abundance for surface pairs and the Enriques-Kodaira outline
nodes: [MMMSGVFVJH]
sources: [KM98, Fuj11, Mat02, Bea96, Kol13]
reads_with: [KM98:ch3, Mat02:ch1, Bea96:ch8]
requires: [P5.8, P5.10, P5.11, P5.12, 4.2, 4.3]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Log abundance for surface pairs and the Enriques-Kodaira outline

### Statement

A *surface pair* $(X, \Delta)$ is a normal projective surface $X$ with an effective $\mathbb{R}$-divisor $\Delta$ such that $K_X + \Delta$ is $\mathbb{R}$-Cartier. It is klt or lc in the sense of Volume 4, Chapter 1. Chapter 4 runs the log minimal model program for such pairs, and it ends at a log Mori fibre space or at a pair with $K_X + \Delta$ nef. Log abundance treats the second case.

**Definition 2.5.21 (log canonical ring, numerical dimension).** Let $(X, \Delta)$ be a surface pair with $\Delta$ a $\mathbb{Q}$-divisor. Its *log canonical ring* is
$$R(X, K_X + \Delta) = \bigoplus_{n \geq 0} H^0\big(X, \mathcal{O}_X(\lfloor n(K_X + \Delta) \rfloor)\big),$$
and $\kappa(X, K_X + \Delta)$ is its growth: $-\infty$ if all the summands with $n \geq 1$ vanish, and otherwise the least $j$ with $h^0(\lfloor n(K_X + \Delta) \rfloor) \leq c \, n^j$. For a nef $\mathbb{R}$-Cartier divisor $D$ on a normal projective surface, the *numerical dimension* $\nu(D)$ is $0$ if $D \equiv 0$, $1$ if $D \not\equiv 0$ and $D^2 = 0$, and $2$ if $D^2 > 0$, where $D^2$ is Mumford's intersection number (Corollary P5.8.5).

This is the numerical dimension of Volume 1, Chapter 4, for surfaces. For a Cartier divisor on a smooth surface $\kappa(X, D) = \kappa(D)$ of Definition P5.11.1.

**Theorem 2.5.22 (log abundance for surfaces).** Let $(X, \Delta)$ be a projective lc surface pair over an algebraically closed field, with $K_X + \Delta$ nef. Then $K_X + \Delta$ is semiample: it is $\mathbb{R}$-linearly equivalent to a nonnegative real combination of semiample Cartier divisors. If $\Delta$ is a $\mathbb{Q}$-divisor, some multiple $m(K_X + \Delta)$ is a base point free Cartier divisor, and $\kappa(X, K_X + \Delta) = \nu(K_X + \Delta)$.

Node: MMMSGVFVJH · Lean: `MinimalModel.SurfaceAbundance`

The theorem has three sources. Fujita ("Fractionally logarithmic canonical rings of algebraic surfaces", J. Fac. Sci. Univ. Tokyo Sect. IA Math. 30 (1984), 685 to 696) proved it for a smooth surface with a boundary whose coefficients are at most $1$, by the Zariski decomposition, together with the finite generation of the log canonical ring. Fujino ("Minimal model theory for log surfaces", Publ. RIMS 48 (2012), 339 to 371, Theorem 8.1) proved it for every lc surface pair in characteristic $0$, with real coefficients, and without assuming $\mathbb{Q}$-factoriality. Tanaka ("Minimal models and abundance for positive characteristic log surfaces", Nagoya Math. J. 216 (2014), 1 to 70) proved it in characteristic $p > 0$. The handbook proves the big klt case and outlines the rest.

**Proposition 2.5.23 (the big case).** Let $\operatorname{char} k = 0$ and let $(X, \Delta)$ be a projective klt surface pair with $\Delta$ a $\mathbb{Q}$-divisor and $K_X + \Delta$ nef and big. Then $K_X + \Delta$ is semiample, the log canonical ring is finitely generated, and $\operatorname{Proj} R(X, K_X + \Delta)$ is the target of the semiample fibration of $K_X + \Delta$, a normal projective surface on which $K_X + \Delta$ descends to an ample divisor.

Lean: not yet in Lean.

**Theorem 2.5.24 (the classification from the minimal model program).** Let $S$ be a smooth projective surface, and run the minimal model program $S = S_r \to S_{r-1} \to \dots \to S_0$ of Theorem P5.12.21. Exactly one of the following holds.

1. $S_0$ is a Mori fibre space, $\mathbb{P}^2$ over a point or a $\mathbb{P}^1$-bundle over a curve, and $\kappa(S) = -\infty$.
2. $K_{S_0}$ is nef. Then $S_0$ is the unique minimal model, $K_{S_0}$ is semiample, $\kappa(S) \in \{0, 1, 2\}$, the canonical ring $R(S, K_S) \cong R(S_0, K_{S_0})$ is finitely generated, and the Iitaka fibration of $S_0$ is a morphism $S_0 \to Z = \operatorname{Proj} R(S, K_S)$ with $\dim Z = \kappa(S)$. For $\kappa = 0$, $Z$ is a point and $12 K_{S_0} \sim 0$. For $\kappa = 1$, $Z$ is a curve and $S_0 \to Z$ is an elliptic or quasi-elliptic fibration. For $\kappa = 2$, $Z$ is the canonical model and $S_0 \to Z$ contracts the $(-2)$-curves to rational double points.

Lean: not yet in Lean.

**Corollary 2.5.25 ($\kappa = \nu$).** Let $S$ be a smooth projective surface with $K_S$ nef. Then $\kappa(S) = \nu(K_S)$.

Lean: not yet in Lean.

### Proof in words

In the big case the base point free theorem applies directly: $K_X + \Delta$ is nef, and $2(K_X + \Delta) - (K_X + \Delta)$ is nef and big, so a multiple of $K_X + \Delta$ is free. When $K_X + \Delta \equiv 0$, the pair pulls back crepantly to the minimal resolution, and the question becomes whether a numerically trivial divisor is torsion, which the classification of surfaces with $\kappa = 0$ and of ruled surfaces decides. The case $\nu = 1$ is the hardest, and the cited proofs first show that $K_X + \Delta$ is effective and then use the Zariski decomposition.

For a smooth surface the program reduces everything to Sections 1 and 2. If the program stops at a Mori fibre space, $\kappa = -\infty$. If it stops at a minimal model, then $\kappa \geq 0$ by Theorem 2.5.3, and the three values of $\kappa$ are handled by Theorems 2.5.4, 2.5.5 and 2.5.16. The canonical ring does not change along the program, so its $\operatorname{Proj}$ is the base of the Iitaka fibration of the minimal model.

### Examples

**Example 2.5.26 (a klt pair on $\mathbb{P}^1 \times \mathbb{P}^1$ with $\kappa = 1$).** Let $X = \mathbb{P}^1 \times \mathbb{P}^1$, let $F_1 = \{\mathrm{pt}\} \times \mathbb{P}^1$ and $F_2 = \mathbb{P}^1 \times \{\mathrm{pt}\}$ be the two fibre classes, so $\operatorname{Pic} X = \mathbb{Z} F_1 \oplus \mathbb{Z} F_2$ with $F_1^2 = F_2^2 = 0$, $F_1 \cdot F_2 = 1$ and $K_X = -2F_1 - 2F_2$. Choose distinct fibres $A_1, \dots, A_6$ of class $F_1$ and distinct fibres $B_1, B_2, B_3$ of class $F_2$, and put
$$\Delta = \frac{1}{2} \sum_{i=1}^6 A_i + \frac{2}{3} \sum_{j=1}^3 B_j.$$
The support is snc: fibres of the same ruling are disjoint, and $A_i$ meets $B_j$ transversally in one point. By Theorem 4.2.12, $\operatorname{discrep}(X, \Delta) = \min\{1, \frac{1}{2}, \frac{1}{3}, 1 - \frac{1}{2} - \frac{2}{3}\} = -\frac{1}{6} > -1$, so the pair is klt. Then $K_X + \Delta \sim_{\mathbb{Q}} (-2 + 3) F_1 + (-2 + 2) F_2 = F_1$, which is nef with $F_1^2 = 0$, so $\nu = 1$, and $6(K_X + \Delta) \sim 6F_1$ is free with semiample fibration the first projection. The log plurigenera are explicit: $\lfloor n \Delta \rfloor = \lfloor n/2 \rfloor \sum A_i + \lfloor 2n/3 \rfloor \sum B_j$, so $\lfloor n(K_X + \Delta) \rfloor \sim a_n F_1 + b_n F_2$ with $a_n = -2n + 6 \lfloor n/2 \rfloor$ and $b_n = -2n + 3 \lfloor 2n/3 \rfloor$. Here $b_n = 0, -2, -1$ for $n \equiv 0, 1, 2 \pmod 3$, and for $n$ divisible by $3$, $a_n = 6 \lfloor n/6 \rfloor$, as the cases $n = 6j$ and $n = 6j + 3$ show: $a_{6j} = 6j$ and $a_{6j + 3} = -12j - 6 + 6(3j + 1) = 6j$. Since $h^0(aF_1 + bF_2) = (a + 1)(b + 1)$ for $a, b \geq 0$ and $0$ otherwise,
$$h^0(\lfloor n(K_X + \Delta) \rfloor) = \begin{cases} 6 \lfloor n/6 \rfloor + 1 & \text{if } 3 \mid n, \\ 0 & \text{otherwise.} \end{cases}$$
This grows linearly, so $\kappa(X, K_X + \Delta) = 1 = \nu$, as Theorem 2.5.22 predicts. The pair is the quotient picture of an elliptic fibration: the coefficients $\frac{1}{2}$ and $\frac{2}{3}$ are those $1 - \frac{1}{m}$ of multiple fibres in Corollary 2.5.8.

**Example 2.5.27 (plane pairs and the three outcomes).** Let $C \subseteq \mathbb{P}^2$ be a smooth quintic and $0 \leq t < 1$. The pair $(\mathbb{P}^2, tC)$ is klt by Theorem 4.2.12, and $K + tC \sim_{\mathbb{R}} (5t - 3) H$. For $t < \frac{3}{5}$, $-(K + tC)$ is ample and the program stops at once at the log Mori fibre space $\mathbb{P}^2 \to \mathrm{pt}$, with $\kappa = -\infty$. For $t = \frac{3}{5}$, $5(K + tC) = -15H + 3C \sim 0$, so $K + tC \sim_{\mathbb{Q}} 0$ is semiample with $\kappa = \nu = 0$. For $t = \frac{4}{5}$, $K + tC \sim_{\mathbb{Q}} \frac{1}{5} H$ is ample, $\kappa = \nu = 2$, and $\lfloor n(K + tC) \rfloor \sim (-3n + 5 \lfloor 4n/5 \rfloor) H$, which is $-3H$, $-H$, $H$, $3H$, $5H$ for $n = 1, \dots, 5$. The Veronese subring of degree $5$ of the log canonical ring is $\bigoplus_j H^0(\mathbb{P}^2, \mathcal{O}(j)) = k[x, y, z]$, and the log canonical model is $\mathbb{P}^2$ itself.

**Example 2.5.28 (failure for a coefficient bigger than one).** Let $X = X_9$ be the surface of Example P5.10.26, with $\tilde C \cong C$ the strict transform of the smooth cubic through the nine points, so that $-K_X = \tilde C$ and $\mathcal{O}_{\tilde C}(\tilde C)$ is a non-torsion element of $\operatorname{Pic}^0(\tilde C)$. For $t \geq 0$, $K_X + t\tilde C \sim (t - 1) \tilde C$. For $t < 1$ this is not nef, since its degree on an ample divisor is negative. For $t = 1$ the pair $(X, \tilde C)$ is lc, by Theorem 4.2.12, and $K_X + \tilde C \sim 0$ is semiample. For $t > 1$ the divisor $(t - 1)\tilde C$ is nef, because $\tilde C$ is integral with $\tilde C^2 = 0$, and $\nu = 1$. But Example P5.10.26 shows $h^0(j \tilde C) = 1$ for all $j \geq 0$, so every multiple $|j \tilde C|$ has base locus $\tilde C$: the divisor is nef and not semiample, with $\kappa = 0 \neq 1 = \nu$. The pair $(X, t\tilde C)$ with $t > 1$ is not lc, since $a(\tilde C, X, t\tilde C) = -t < -1$, so Theorem 2.5.22 does not apply. The lc hypothesis cannot be dropped.

### Proof

*Proof of Proposition 2.5.23.* Choose $m \geq 1$ with $D = m(K_X + \Delta)$ Cartier. Then $D$ is nef, and $2D - (K_X + \Delta) = (2m - 1)(K_X + \Delta)$ is nef and big. The base point free theorem (KM98, Theorem 3.3), applied to the klt pair $(X, \Delta)$, gives that $|bD|$ is free for all $b \gg 0$. So $K_X + \Delta$ is semiample. Let $\varphi' \colon X \to Z$ be the semiample fibration of $bD$, with $bD \sim \varphi'^* A$ for an ample $A$ (Lemma 2.5.2). Since $K_X + \Delta$ is big, $h^0(jbD) = h^0(Z, jA)$ grows like $j^2$, so $\dim Z = 2$. For $0 \leq i < bm$, $\lfloor (nbm + i)(K_X + \Delta) \rfloor = nbD + \lfloor i(K_X + \Delta) \rfloor$, because $nbD$ is an integral divisor, so the projection formula gives
$$\bigoplus_{n \geq 0} H^0\big(X, \lfloor (nbm + i)(K_X + \Delta) \rfloor\big) \cong \bigoplus_{n \geq 0} H^0\big(Z, \mathcal{G}_i \otimes \mathcal{O}_Z(nA)\big), \qquad \mathcal{G}_i = \varphi'_* \mathcal{O}_X(\lfloor i(K_X + \Delta) \rfloor),$$
with $\mathcal{G}_i$ coherent. The proof of Lemma 2.5.15 applies word for word to these modules, and shows that $R(X, K_X + \Delta)$ is finitely generated with $\operatorname{Proj} \cong Z$. Finally $A$ is ample with $\varphi'^* A \sim bm(K_X + \Delta)$, so $\frac{1}{bm} A$ is the ample divisor to which $K_X + \Delta$ descends. $\square$

*Outline of the proof of Theorem 2.5.22.* Suppose first that $\Delta$ is a $\mathbb{Q}$-divisor and $(X, \Delta)$ is klt, and write $\nu = \nu(K_X + \Delta)$. If $\nu = 2$, Proposition 2.5.23 applies in characteristic $0$. If $\nu = 0$, let $f \colon Y \to X$ be the minimal resolution and write $K_Y + \Delta_Y = f^*(K_X + \Delta)$, the Mumford pullback. By part 2 of Proposition 4.3.5 the exceptional coefficients of $\Delta_Y$ are nonnegative, so $\Delta_Y \geq 0$, and its coefficients are less than $1$ because the pair is klt. If $\Delta_Y = 0$, then $K_Y \equiv 0$ is nef, $\kappa(Y) \geq 0$ by Theorem 2.5.3, and $12 K_Y \sim 0$ by Theorem 2.5.4, so $12(K_X + \Delta) = f_*(12 K_Y) \sim 0$. If $\Delta_Y \neq 0$, then $K_Y \cdot H = -\Delta_Y \cdot H < 0$ for an ample $H$, so $Y$ is birationally ruled, and the remaining point is that the numerically trivial $\mathbb{Q}$-divisor $K_Y + \Delta_Y$ is torsion in $\operatorname{Pic}(Y) \otimes \mathbb{Q}$. When $q(Y) = 0$ this holds in characteristic $0$ because $\operatorname{Pic}^0(Y) = 0$ and numerically trivial classes in the finitely generated group $\operatorname{NS}(Y)$ are torsion. When $q(Y) > 0$, $Y$ maps to a curve of genus $q(Y)$, and Fujino, Section 8, and Tanaka analyse $\Delta_Y$ along the fibres. If $\nu = 1$, the cited proofs first prove nonvanishing, $\kappa(X, K_X + \Delta) \geq 0$, by Riemann-Roch on a resolution and the classification, and then use the Zariski decomposition (Theorem P5.8.24) of an effective member to show that a multiple moves in a free pencil. The lc case reduces to the klt case and to adjunction on the curves of coefficient $1$, and the case of real coefficients reduces to rational ones by writing $\Delta$ as a convex combination of nearby rational boundaries with the same nef property (Fujino, Section 8). $\square$

*Proof of Theorem 2.5.24.* By part 2 of Theorem P5.12.21 the run ends at a nef model or at a Mori fibre space, and not both. In the first case, $K_{S_0}$ is negative on the curves of a family that covers $S_0$, the lines of $\mathbb{P}^2$ or the fibres of the bundle. A member $G$ of $|nK_{S_0}|$ with $n \geq 1$ would satisfy $G \cdot F \geq 0$ for a curve $F$ of the family not contained in $G$, against $nK_{S_0} \cdot F < 0$. So $\kappa(S_0) = -\infty$, and $\kappa(S) = \kappa(S_0)$ by Theorem P5.11.6. In the second case $\kappa(S) = \kappa(S_0) \geq 0$ by Theorem 2.5.3, and $S_0$ is the unique minimal model by Corollary P5.11.19. Since $\kappa$ takes the values $-\infty, 0, 1, 2$ only (part 1 of Proposition P5.11.3), the two cases are separated by $\kappa(S)$. In the second case, $K_{S_0}$ is semiample by Theorem 2.5.4, Theorem 2.5.5 or Theorem 2.5.16, according as $\kappa(S)$ is $0$, $1$ or $2$. The proof of part 4 of Theorem 2.5.16 uses only the composite of blow-ups $S \to S_0$ and Theorem P5.11.6, so it gives $R(S, K_S) \cong R(S_0, K_{S_0})$ for every $\kappa(S) \geq 0$. By Lemma 2.5.15 this ring is finitely generated and its $\operatorname{Proj}$ is the base $Z$ of the Iitaka fibration of $S_0$, and $\dim Z = \kappa(S)$ by part 4 of Lemma 2.5.2. The descriptions of $Z$ are those of Theorems 2.5.4, 2.5.5 and 2.5.16. $\square$

*Proof of Corollary 2.5.25.* By Theorem 2.5.3, $\kappa(S) \in \{0, 1, 2\}$. If $\kappa(S) = 0$, then $K_S \equiv 0$ by Theorem 2.5.4, so $\nu = 0$. If $\kappa(S) = 1$, then $K_S^2 = 0$ by Theorem 2.5.5, and $K_S \not\equiv 0$ because some $|nK_S|$ contains a nonzero effective divisor, which has positive degree on an ample divisor; so $\nu = 1$. If $\kappa(S) = 2$, then $K_S^2 > 0$ by part 4 of Theorem P5.11.26, so $\nu = 2$. $\square$

### Exercises

1. (A) Let $L_1, \dots, L_4 \subseteq \mathbb{P}^2$ be four lines in general position and $0 \leq c < 1$. Show that $(\mathbb{P}^2, c \sum L_i)$ is klt, and that $\kappa(K + c\sum L_i)$ is $-\infty$, $0$ or $2$ according as $c < \frac{3}{4}$, $c = \frac{3}{4}$ or $c > \frac{3}{4}$.
2. (A) Let $D$ be a nef $\mathbb{Q}$-Cartier divisor on a normal projective surface. Show that if $D$ is semiample, then $\kappa(D) = \nu(D)$, and that in general $\kappa(D) \leq \nu(D)$.
3. (B) Let $E$ be an elliptic curve, $X = E \times \mathbb{P}^1$ and $\Delta = \frac{1}{2} \sum_{i=1}^4 E \times \{p_i\}$ for distinct points $p_i$. Show that $(X, \Delta)$ is klt, that $K_X + \Delta \sim_{\mathbb{Q}} 0$, and that this is the case $q(Y) > 0$, $\Delta_Y \neq 0$ of the outline of Theorem 2.5.22.
4. (B) For the pair $(\mathbb{P}^2, \frac{4}{5} C)$ of Example 2.5.27, compute $h^0(\lfloor n(K + \Delta) \rfloor)$ for $n = 1, \dots, 5$, and show that the log canonical ring is not generated in degree $1$.
5. (B) In Example 2.5.26 keep the six fibres $A_i$ with coefficient $\frac{1}{2}$, but take only two fibres $B_1, B_2$ with coefficient $\frac{2}{3}$. Show that $K_X + \Delta$ is not nef, that the first projection is a $(K_X + \Delta)$-negative extremal contraction, and that the log program stops at a log Mori fibre space over $\mathbb{P}^1$.
6. (C) Let $(X, \Delta)$ be a projective klt surface pair with $K_X + \Delta \equiv 0$, and $f \colon Y \to X$ its minimal resolution with $K_Y + \Delta_Y = f^*(K_X + \Delta)$. Suppose $\Delta_Y = 0$. Show that $\Delta = 0$, that $X$ has only rational double points, and that $12 K_X \sim 0$.

### Lean

`MinimalModel.SurfaceAbundance` states Theorem 2.5.22 for lc pairs with real coefficients, over an algebraically closed field of characteristic $0$, as in Fujino's paper. It is the case $n = 2$ of `MinimalModel.Abundance`, the abundance conjecture of Volume 1, Chapter 1. Proposition 2.5.23 is the case of surfaces of `MinimalModel.AbundanceBig`, the base point free theorem with $D = K + \Delta$. Corollary 2.5.25 is the equality $\kappa = \nu$ that abundance predicts in every dimension, and `MinimalModel.AbundanceNuZero` states abundance in the case $\nu = 0$ in every dimension. The positive characteristic case of Tanaka is not stated in Lean.

### Notes and history

Fujita's paper of 1984 is the first proof of log abundance for surfaces, and it uses the Zariski decomposition of Zariski's paper of 1962. Kawamata, Miyaoka and others extended the ideas to 3-folds, and the log abundance theorem for lc 3-folds is due to Keel, Matsuki and McKernan (1994). For surfaces, Fujino's paper of 2012 develops the whole log minimal model program for lc surfaces without $\mathbb{Q}$-factoriality, including the cone, contraction and abundance theorems, and Tanaka's paper of 2014 does the same in positive characteristic, where the Kawamata-Viehweg vanishing theorem fails and is replaced by arguments special to surfaces. The view of the Enriques-Kodaira classification as the output of the minimal model program and abundance is in Matsuki (Mat02, Chapter 1) and Kollár-Mori (KM98, Chapter 1). Example 2.5.28 is the standard example that the hypothesis lc is needed: it rests on a point of infinite order on an elliptic curve, as in Example P5.10.26.
