---
title: Running the minimal model program on a surface
nodes: []
sources: [KM98, Mat02, Bea96, Har77, Rei97]
reads_with: [KM98:ch1, Mat02:ch1, Bea96:ch2]
requires: [P3.11, P5.5, P5.6, P5.7, P5.11]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Running the minimal model program on a surface

### Statement

Let $S$ be a smooth projective surface over the algebraically closed field $k$. The contractions of Theorem P5.12.15 are of three types: type 1 contracts a $(-1)$-curve to a smooth point, type 2 maps onto a curve with fibres $\mathbb{P}^1$, and type 3 is $\mathbb{P}^2$ mapping to a point. Only type 1 produces a new surface, and the program iterates it.

**Definition P5.12.20 (Mori fibre spaces and runs of the program).**

1. A *Mori fibre space* is the contraction $\varphi_R \colon S \to T$ of a $K$-negative extremal ray $R$ of type 2 or 3: either $S \cong \mathbb{P}^2$ and $T$ is a point, or $\rho(S) = 2$ and $T$ is a smooth projective curve over which every fibre is $\mathbb{P}^1$.
2. A *run of the minimal model program* on $S$ is a sequence
$$S = S_0 \xrightarrow{\ \varphi_1\ } S_1 \xrightarrow{\ \varphi_2\ } \cdots \xrightarrow{\ \varphi_N\ } S_N$$
in which each $\varphi_i$ is the contraction of a $K_{S_{i-1}}$-negative extremal ray of type 1, and the last surface satisfies one of: $K_{S_N}$ is nef, and the run *ends at the nef model* $S_N$; or $S_N$ has a $K$-negative extremal ray of type 2 or 3, the run is completed by its contraction, and it *ends at the Mori fibre space* $S_N \to T$.

A surface with $K_S$ nef has no $(-1)$-curve, since $K \cdot E = -1$ for a $(-1)$-curve $E$. So the nef model $S_N$ is a minimal surface in the sense of Definition P5.11.13, and $S \to S_N$ is a minimal model of $S$ in that sense. The converse fails: $\mathbb{P}^2$ is minimal and $K_{\mathbb{P}^2}$ is not nef.

**Theorem P5.12.21 (the minimal model program for surfaces).**

1. Every smooth projective surface $S$ has a run of the minimal model program. In every run, $S_i$ is a smooth projective surface with $\rho(S_i) = \rho(S) - i$ and $K_{S_i}^2 = K_S^2 + i$, and the number $N$ of divisorial steps satisfies $N \leq \rho(S) - 1$.
2. A run ends at a nef model or at a Mori fibre space, and not both.
3. A smooth projective surface without $(-1)$-curves has $K$ nef, or is $\mathbb{P}^2$, or has $\rho = 2$ and a morphism onto a smooth projective curve all of whose fibres are $\mathbb{P}^1$.

Lean: not in Lean as stated.

**Lemma P5.12.22 (curves away from a contracted curve).** Let $\pi \colon S \to S'$ be the contraction of a $(-1)$-curve $E$, and $C \neq E$ an integral curve with $C \cdot E = 0$. Then $C \cap E = \emptyset$, $\pi$ maps $C$ isomorphically onto the integral curve $C' = \pi(C)$, $\pi^* C' = C$, $C'^2 = C^2$ and $K_{S'} \cdot C' = K_S \cdot C$. In particular, if $C$ is a $(-1)$-curve, so is $C'$, and pairwise disjoint $(-1)$-curves $C_1, \dots, C_r$ on $S$ can be contracted one after another, in any order, by $r$ steps of a run.

Lean: not in Lean as stated.

**Corollary P5.12.23 (the outcome is determined by $S$).**

1. If some run on $S$ ends at a Mori fibre space, then no run ends at a nef model, and $h^0(S, nK_S) = 0$ for all $n \geq 1$, so $\kappa(S) = -\infty$.
2. If some run ends at a nef model $S_N$, then $\kappa(S) \geq 0$, every run ends at a nef model, and $S_N$ is, up to unique isomorphism over $S$, the unique minimal model of $S$.

Lean: not in Lean as stated.

### Proof in words

Each type 1 step lowers the Picard number by one and keeps the surface smooth and projective, so the process stops before the Picard number would reach $0$; at the end the cone theorem says that $K$ is nef or that a $K$-negative ray remains, and the classification says that a remaining ray not of type 1 is a Mori fibre space. A surface without $(-1)$-curves has no ray of type 1, which is part 3. A Mori fibre space is covered by curves $L$ with $K \cdot L < 0$, lines or fibres, and a general one avoids the finitely many points blown up on the way down from $S$, so $S$ itself is covered by curves on which $K_S$ is negative. Such curves kill all plurigenera, and they also obstruct any birational morphism $S \to S_0$ with $K_{S_0}$ nef, because $K_S$ is $K_{S_0}$ pulled back plus an effective exceptional divisor. The uniqueness of the nef model is the uniqueness of minimal models for $\kappa \geq 0$ from Chapter 11. In contrast, the Mori fibre space at the end of a run is far from unique, as the examples show.

### Examples

**Example P5.12.24 (a blown-up abelian surface).** Let $A = E \times E$ as in Example P5.12.9, $p \in A$, and $\pi \colon S = \operatorname{Bl}_p A \to A$ with exceptional curve $E_p$. Then $K_S = \pi^* K_A + E_p = E_p$ by Theorem P5.6.3, since $K_A \sim 0$. An integral curve $C \neq E_p$ has $K_S \cdot C = E_p \cdot C \geq 0$, while $K_S \cdot E_p = -1$. So every $K$-negative extremal ray, which by Theorem P5.12.15 is spanned by a curve $C$ with $K \cdot C < 0$, is the ray of $E_p$, and
$$\overline{NE}(S) = \overline{NE}(S)_{K \geq 0} + \mathbb{R}_{\geq 0} [E_p]$$
by Lemma P5.12.11, with $\overline{NE}(S)_{E_p \geq 0} = \overline{NE}(S)_{K \geq 0}$. The only run is $S \to A$, with $N = 1 = \rho(S) - \rho(A)$, ending at the nef model $A$ with $K_A = 0$. This is the case $r = 1$ of Example P5.11.21.

**Example P5.12.25 (the plane blown up at a point).** On $F_1 = \operatorname{Bl}_p \mathbb{P}^2$ both extremal rays are $K$-negative (Example P5.12.16): the ray of $E$ is of type 1 and the ray of $\ell - E$ of type 2. So there are two runs. In the first, $N = 1$ and $F_1 \to \mathbb{P}^2$ is followed by the Mori fibre space $\mathbb{P}^2 \to \operatorname{pt}$. In the second, $N = 0$ and the run is the Mori fibre space $F_1 \to \mathbb{P}^1$ itself, the projection of Theorem P3.11.25, whose fibres are the strict transforms of the lines through $p$. The two Mori fibre spaces are not isomorphic, since $\rho(\mathbb{P}^2) = 1$ and $\rho(F_1) = 2$.

**Example P5.12.26 (the plane blown up at two points).** Let $S = \operatorname{Bl}_{q_1, q_2} \mathbb{P}^2$ with the three $(-1)$-curves $E_1$, $E_2$ and $L_{12} = \ell - E_1 - E_2$ spanning $\overline{NE}(S)$ (Example P5.12.17). Contracting $E_1$ gives $\operatorname{Bl}_{q_2} \mathbb{P}^2 \cong F_1$, and by Example P5.12.25 the run continues to $\mathbb{P}^2$ or stops at $F_1 \to \mathbb{P}^1$; the same holds for $E_2$. Let $\pi \colon S \to S'$ contract $L_{12}$. By Theorem P5.6.3 (4), $\pi^* \operatorname{Num}(S')$ is the orthogonal complement of $L_{12}$, the classes $a\ell - b_1 E_1 - b_2 E_2$ with $a = b_1 + b_2$, which is $\mathbb{Z}(\ell - E_1) \oplus \mathbb{Z}(\ell - E_2)$. Write $f_1, f_2$ for the classes on $S'$ with $\pi^* f_i = \ell - E_i$. Then $f_1^2 = f_2^2 = 0$, $f_1 \cdot f_2 = 1$, and
$$\pi^* K_{S'} = K_S - L_{12} = -4\ell + 2E_1 + 2E_2 = -2(\ell - E_1) - 2(\ell - E_2), \qquad K_{S'} = -2f_1 - 2f_2.$$
The strict transform of a line through $q_1$ other than the line $q_1 q_2$ has class $\ell - E_1$ and meets $L_{12}$ in $(\ell - E_1) \cdot (\ell - E_1 - E_2) = 0$ points, so by Lemma P5.12.22 its image is an integral curve of class $f_1$ and square $0$; the same holds for $f_2$. These classes are nef by Lemma P5.12.4, so $\mathbb{R}_{\geq 0} f_1 + \mathbb{R}_{\geq 0} f_2 \subseteq NE(S') \cap \operatorname{Nef}(S')$. A nef class $af_1 + bf_2$ has $b = (af_1 + bf_2) \cdot f_1 \geq 0$ and $a \geq 0$, so $\operatorname{Nef}(S') = \mathbb{R}_{\geq 0} f_1 + \mathbb{R}_{\geq 0} f_2$, and by the duality of Theorem P5.12.6 (3), $\overline{NE}(S')$ is the same cone. Both rays have $K_{S'} \cdot f_i = -2$ and square $0$, so they are of type 2: $S'$ is a Mori fibre space over $\mathbb{P}^1$ in two ways. By Examples P5.6.9 and P5.7.17, $S \cong \operatorname{Bl}_p(\mathbb{P}^1 \times \mathbb{P}^1)$ with $L_{12}$ corresponding to the exceptional curve, and $S' \cong \mathbb{P}^1 \times \mathbb{P}^1$. So the runs on $S$ end at $\mathbb{P}^2$, at $F_1 \to \mathbb{P}^1$, or at $\mathbb{P}^1 \times \mathbb{P}^1 \to \mathbb{P}^1$, with $N = 2$, $1$ and $1$, and $K_{S_N}^2 = 7 + N$ equals $9$, $8$ and $8$.

**Example P5.12.27 (runs on a cubic surface).** Let $q_1, \dots, q_6 \in \mathbb{P}^2$ be six points, no three on a line and not all six on a conic, and $S = \operatorname{Bl}_{q_1, \dots, q_6} \mathbb{P}^2$, with $\rho(S) = 7$, $K = -3\ell + \sum E_i$ and $K^2 = 3$ (Example P5.6.8). By Example P5.6.8, the line through $q_i, q_j$ has strict transform $L_{ij} = \ell - E_i - E_j$, a $(-1)$-curve. For each $j$, the conics through the five points $q_i$, $i \neq j$, form a nonempty linear system, since conics form a $\mathbb{P}^5$ and each point imposes one linear condition. Such a conic is irreducible, since a pair of lines would contain three of the five points on one line, and it is unique, since two distinct irreducible conics meet in at most $4$ points by Example P5.5.8. It does not pass through $q_j$. An irreducible conic is smooth, so its strict transform is $C_j = 2\ell - \sum_{i \neq j} E_i$, with $C_j^2 = 4 - 5 = -1$ and $K \cdot C_j = -6 + 5 = -1$: a $(-1)$-curve. The intersection numbers needed are
$$E_i \cdot E_j = 0, \qquad C_i \cdot C_j = 4 - 4 = 0, \qquad L_{56} \cdot E_i = 0 \ (i \leq 4) \qquad \text{for } i \neq j.$$
By Lemma P5.12.22, each of the following sets of pairwise disjoint $(-1)$-curves can be contracted in sequence.

1. Contract $E_1, \dots, E_6$. The result is $\mathbb{P}^2$, with $N = 6$, and the run ends at $\mathbb{P}^2 \to \operatorname{pt}$.
2. Contract $C_1, \dots, C_6$, with composite $\pi \colon S \to S''$. Then $\rho(S'') = 1$, and $\pi^* K_{S''} = K_S - \sum_j C_j = -15\ell + 6 \sum_i E_i$, which is orthogonal to every $C_j$, as it should be: $-30 + 6 \cdot 5 = 0$. The curve $E_1$ is not contracted, and by Lemma P5.11.15 (3), $K_{S''} \cdot \pi(E_1) = \pi^* K_{S''} \cdot E_1 = -6 < 0$. So $S''$ has a $K$-negative extremal ray, of type 3 since $\rho(S'') = 1$, and $S'' \cong \mathbb{P}^2$ by Theorem P5.12.15. The pullback of a line of $S''$ is $\ell' = -\frac{1}{3} \pi^* K_{S''} = 5\ell - 2\sum E_i$, with $\ell'^2 = 25 - 24 = 1$, and $\pi(E_1)$ is a conic, since $\pi^* \pi(E_1) = E_1 + \sum_{j \neq 1} C_j$ has square $-1 + 10 - 5 = 4$. The two maps $S \to \mathbb{P}^2$ of runs 1 and 2 differ by the birational map of $\mathbb{P}^2$ given by the plane quintics with double points at $q_1, \dots, q_6$, which is not an isomorphism.
3. Contract $E_1, \dots, E_5$. The result is $\operatorname{Bl}_{q_6} \mathbb{P}^2 \cong F_1$, and the run may stop at the Mori fibre space $F_1 \to \mathbb{P}^1$ of Example P5.12.25, with $N = 5$.
4. Contract $E_1, \dots, E_4$ and then the image of $L_{56}$. The first four steps give $\operatorname{Bl}_{q_5, q_6} \mathbb{P}^2$, in which the image of $L_{56}$ is the line through the two points, and Example P5.12.26 shows that its contraction is $\mathbb{P}^1 \times \mathbb{P}^1$, a Mori fibre space over $\mathbb{P}^1$ in two ways, with $N = 5$.

The surfaces $\mathbb{P}^2$, $F_1$ and $\mathbb{P}^1 \times \mathbb{P}^1$ are pairwise non-isomorphic: $\rho(\mathbb{P}^2) = 1$, $F_1$ contains a curve of square $-1$, and every curve on $\mathbb{P}^1 \times \mathbb{P}^1$ has class $aF_1 + bF_2$ with $a, b \geq 0$ and square $2ab \geq 0$. So the cubic surface is the source of runs ending at three different Mori fibre spaces, and of two runs ending at $\mathbb{P}^2$ through different birational maps. By Corollary P5.12.23, no run on $S$ ends at a nef model.

### Proof

*Lemma P5.12.22.* The curves $C$ and $E$ are distinct with $C \cdot E = 0$, so they are disjoint by Proposition P5.5.5. Let $p = \pi(E)$. Since $\pi^{-1}(p) = E$, the integral curve $C' = \pi(C)$ does not pass through $p$, and $\pi$ is an isomorphism from the open set $S \setminus E \supseteq C$ onto $S' \setminus \{p\}$, so $C \to C'$ is an isomorphism. By Proposition P5.6.4 (2) with $m_p(C') = 0$, $\pi^* C' = \tilde C' = C$. By Theorem P5.6.3 (2) and (3), $C'^2 = \pi^* C' \cdot \pi^* C' = C^2$ and $K_S \cdot C = (\pi^* K_{S'} + E) \cdot \pi^* C' = K_{S'} \cdot C'$. If $C$ is a $(-1)$-curve, then $C' \cong C \cong \mathbb{P}^1$ and $C'^2 = -1$. For disjoint $(-1)$-curves $C_1, \dots, C_r$, contract $C_1$: the images of $C_2, \dots, C_r$ are pairwise disjoint $(-1)$-curves, since $\pi$ is injective off $C_1$, and the claim follows by induction, each step being the contraction of a $K$-negative extremal ray of type 1 by Lemma P5.12.11.

*Theorem P5.12.21.* (1) Construct the run step by step. Given $S_i$, if $K_{S_i}$ is nef, stop. Otherwise Theorem P5.12.14 (4) gives a $K_{S_i}$-negative extremal ray $R$, of one of the three types of Theorem P5.12.15. If $R$ can be chosen of type 2 or 3, the run may stop with its contraction; if every such ray is of type 1, or if one chooses a ray of type 1, let $\varphi_{i+1} \colon S_i \to S_{i+1}$ be its contraction. By Theorem P5.12.15 (1), $S_{i+1}$ is a smooth projective surface with $\rho(S_{i+1}) = \rho(S_i) - 1$, and $K_{S_{i+1}}^2 = K_{S_i}^2 + 1$ by Theorem P5.6.3 (3). The Picard number of a projective surface is at least $1$, because an ample $H$ has $H^2 > 0$ and so $[H] \neq 0$. So at most $\rho(S) - 1$ steps of type 1 occur, and the process stops at some $S_N$ with $N \leq \rho(S) - 1$, either with $K_{S_N}$ nef or with a ray of type 2 or 3.

(2) A run ends at a nef model or at a Mori fibre space by construction. Both cannot happen at the same $S_N$, since a Mori fibre space comes from a $K_{S_N}$-negative ray, so $K_{S_N}$ is not nef.

(3) If $S$ has no $(-1)$-curve, it has no ray of type 1, because a ray of type 1 is spanned by a $(-1)$-curve. If $K$ is not nef, Theorem P5.12.14 (4) gives a $K$-negative ray, of type 2 or 3, and Theorem P5.12.15 gives the two remaining cases.

*Corollary P5.12.23.* (1) Let $\psi \colon S \to S_N$ be the composite of the divisorial steps of a run ending at a Mori fibre space $S_N \to T$. By Lemma P5.11.15 (1), there is a finite set $P \subseteq S_N$ of points such that $\psi$ is an isomorphism over $S_N \setminus P$, namely the images of the curves contracted by $\psi$. The surface $S_N$ is covered by an infinite family of integral curves $L$ with $K_{S_N} \cdot L < 0$: the lines of $\mathbb{P}^2$, with $K \cdot L = -3$, or the fibres over $T$, with $K \cdot L = -2$. Only finitely many fibres meet $P$, and the lines through a given point form a pencil, so in either case infinitely many members $L$ of the family avoid $P$. For such $L$, the curve $L' = \psi^{-1}(L)$ lies in the open set where $\psi$ is an isomorphism, so $K_S \cdot L' = \deg \omega_S|_{L'} = \deg \omega_{S_N}|_L = K_{S_N} \cdot L < 0$ by Theorem P5.5.6.

Suppose a second run ends at a nef model, with composite $g \colon S \to S_0$ and $K_{S_0}$ nef. By Lemma P5.11.15 (2), $K_S = g^* K_{S_0} + Z$ with $Z$ effective. The curves $L'$ form an infinite family, so some $L'$ is not a component of $Z$, and $Z \cdot L' \geq 0$ by Proposition P5.5.5. By Lemma P5.11.15 (3), $g^* K_{S_0} \cdot L'$ is $0$ or $K_{S_0} \cdot g(L') \geq 0$. So $K_S \cdot L' \geq 0$, a contradiction. Similarly, if $D \in |nK_S|$ for some $n \geq 1$, some $L'$ is not a component of $D$, and $0 \leq D \cdot L' = n K_S \cdot L' < 0$ is impossible. So $h^0(nK_S) = 0$ for all $n \geq 1$, which is $\kappa(S) = -\infty$ (Definition P5.11.2).

(2) Let $S \to S_N$ be a run ending at the nef model $S_N$. By (1), no run on $S$ ends at a Mori fibre space, so every run ends at a nef model. The surface $S_N$ is minimal and birational to $S$. If $\kappa(S) = -\infty$, then by Theorem P5.11.26 (1) the minimal model $S_N$ is $\mathbb{P}^2$ or a geometrically ruled surface over a curve, and both contain curves with $K \cdot L < 0$, lines or fibres, contradicting nefness. So $\kappa(S) \geq 0$, and by Corollary P5.11.19 (2) the minimal model of $S$ is unique up to unique isomorphism; every nef model at the end of a run is minimal, so it is this one.

### Exercises

1. (A) Show that every run on $\mathbb{P}^2$ and on $\mathbb{P}^1 \times \mathbb{P}^1$ has $N = 0$, and list the Mori fibre spaces in which they end.
2. (A) For each of the runs of Example P5.12.27, check that $K_{S_N}^2 = 3 + N$ and $\rho(S_N) = 7 - N$.
3. (B) Show that a run on $S$ ending at a Mori fibre space over a curve has $N = \rho(S) - 2$, and that a run ending at $\mathbb{P}^2$ has $N = \rho(S) - 1$. Deduce that for $S = \operatorname{Bl}_{q_1, \dots, q_r} \mathbb{P}^2$ every run has $N = r$ or $N = r - 1$, and ends at a surface with $K^2 = 9$ or $K^2 = 8$.
4. (B) On the cubic surface of Example P5.12.27, show that $\ell' = 5\ell - 2\sum E_i$ and $E'_j = C_j$ form a $\mathbb{Z}$-basis of $\operatorname{Num}(S)$ with the same Gram matrix as $\ell, E_1, \dots, E_6$, and that $K = -3\ell' + \sum E'_j$.
5. (B) Let $h^0(S, nK_S) > 0$ for some $n \geq 1$. Show that every $(-1)$-curve is a component of every member of $|nK_S|$, and deduce from Corollary P5.12.23 that every run on $S$ ends at a nef model.
6. (C) Let $E$ be an elliptic curve, $X = E \times \mathbb{P}^1$ with fibre $f$ of $p_1$, $p \in X$, and $S = \operatorname{Bl}_p X$. Show that the $(-1)$-curves of $S$ are $E_p$ and the strict transform $\tilde f$ of the fibre through $p$, and that $E_p \cdot \tilde f = 1$. Show that contracting $\tilde f$ gives a Mori fibre space $X' \to E$ in which the strict transform of the section $E \times \{y\}$ through $p$ becomes a section of square $-1$, and deduce that $X' \not\cong X$. So the runs on $S$ end at two non-isomorphic Mori fibre spaces over the same curve.

### Lean

Mathlib has no surfaces with intersection theory, no blow-ups of schemes, and no contraction morphisms, so neither runs of the program nor Mori fibre spaces can be expressed there. The handbook adds no `MinimalModel` node here.

### Notes and history

The minimal model program for surfaces is Castelnuovo and Enriques's theory of minimal models, rewritten by Mori in 1982 as the contraction of extremal rays; Kollár and Mori, Chapter 1, and Matsuki's book present it in this form. The literature state is theorem. Corollary P5.12.23 recovers the classical dichotomy: a surface with $\kappa \geq 0$ has a unique minimal model, reached by contracting $(-1)$-curves, while a surface with $\kappa = -\infty$ ends at a Mori fibre space that depends on the run; the birational maps between Mori fibre spaces are composites of elementary links, the Sarkisov program, which for surfaces goes back to the Noether-Castelnuovo theorem on generators of the Cremona group. The cubic surface examples are the classical double six of Schläfli. Volume 2 carries this program into higher dimension, where three new phenomena appear: extremal contractions may be small, contracting no divisor, and must be followed by flips; the contracted varieties are singular, so the program works with $\mathbb{Q}$-factorial terminal singularities; and termination is no longer a count of Picard numbers, since flips do not change $\rho$. The cone theorem, the basepoint-free theorem, the existence and termination of flips, and the abundance conjecture take the places of Theorems P5.12.14, P5.12.15 and P5.12.21 and of Corollary P5.12.23.
