---
title: Vanishing on affine schemes
nodes: []
sources: [Har77, Vak25, GW23, Stacks]
reads_with: [Har77:III.3, Har77:III.4, Vak25:ch18]
requires: [P2.7, P3.2, P3.4, P3.5, P4.1]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Vanishing on affine schemes

### Statement

The first theorem turns the vanishing of Čech cohomology for enough covers into the vanishing of sheaf cohomology. It is stated for a sheaf of abelian groups on a space, and it applies equally to sheaves of modules, whose cohomology is the same (part 4 of Theorem P2.7.11).

**Theorem P4.1.7 (vanishing from Čech cohomology).** Let $X$ be a topological space and $\mathcal{F}$ a sheaf of abelian groups on $X$. Let $\mathcal{B}$ be a set of open subsets of $X$ and $\mathsf{Cov}$ a set of open covers, such that:

1. every member of $\mathsf{Cov}$ is a cover $\mathcal{U} = (U_i)_{i \in I}$ of some $U \in \mathcal{B}$ by finitely many members of $\mathcal{B}$, and every finite intersection $U_{i_0 \cdots i_p}$ is in $\mathcal{B}$;
2. every open cover of a member $U \in \mathcal{B}$ has a refinement in $\mathsf{Cov}$ that covers $U$;
3. $\check{H}^p(\mathcal{U}, \mathcal{F}) = 0$ for every $\mathcal{U} \in \mathsf{Cov}$ and every $p > 0$.

Then $H^p(U, \mathcal{F}) = 0$ for every $U \in \mathcal{B}$ and every $p > 0$.

Lean: not in Lean as stated.

**Theorem P4.1.8 (Serre's vanishing theorem on affine schemes).** Let $X$ be an affine scheme and $\mathcal{F}$ a quasi-coherent $\mathcal{O}_X$-module. Then $H^p(X, \mathcal{F}) = 0$ for every $p > 0$.

Lean: not in Lean as stated.

**Corollary P4.1.9 (Čech cohomology computes cohomology).** Let $X$ be a scheme and $\mathcal{U} = (U_i)$ an open cover of $X$ such that every finite intersection $U_{i_0 \cdots i_p}$ is affine. Then for every quasi-coherent $\mathcal{F}$ the natural maps $\check{H}^p(\mathcal{U}, \mathcal{F}) \to H^p(X, \mathcal{F})$ of Proposition P2.7.19 are isomorphisms. If $X$ is separated, this holds for every cover of $X$ by affine open sets.

Lean: not in Lean as stated.

**Corollary P4.1.10 (a bound by the number of affine pieces).** Let $X$ be a scheme covered by $r$ affine open sets with all finite intersections affine, for instance a separated scheme covered by $r$ affine open sets. Then $H^p(X, \mathcal{F}) = 0$ for every quasi-coherent $\mathcal{F}$ and every $p \geq r$. In particular $H^p(\mathbb{P}^n_A, \mathcal{F}) = 0$ for $p > n$, for every ring $A$ and every quasi-coherent sheaf $\mathcal{F}$ on $\mathbb{P}^n_A$.

Lean: not in Lean as stated.

**Corollary P4.1.11 (sections and extensions on affine schemes).** Let $X$ be an affine scheme and $0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$ an exact sequence of $\mathcal{O}_X$-modules.

1. If $\mathcal{F}'$ is quasi-coherent, then $0 \to \mathcal{F}'(X) \to \mathcal{F}(X) \to \mathcal{F}''(X) \to 0$ is exact.
2. If $\mathcal{F}'$ and $\mathcal{F}''$ are quasi-coherent, then so is $\mathcal{F}$. So on every scheme an extension of two quasi-coherent sheaves is quasi-coherent.

Lean: not in Lean as stated.

Part 1 strengthens part 3 of Corollary P3.5.13, which assumes all three sheaves quasi-coherent. Part 2 is the closure of $\mathsf{QCoh}(X)$ under extensions that P3 Ch. 5 deferred to this chapter.

### Proof in words

A class in $H^1(U, \mathcal{F})$ vanishes locally, so it comes from the Čech cohomology of some cover, and Čech cohomology of a good enough cover is zero. This kills $H^1$. For higher degrees, embed $\mathcal{F}$ in an injective sheaf $\mathcal{I}$ and let $\mathcal{G} = \mathcal{I}/\mathcal{F}$. Because $H^1$ of $\mathcal{F}$ vanishes on every member of $\mathcal{B}$, the sequence $0 \to \mathcal{F} \to \mathcal{I} \to \mathcal{G} \to 0$ stays exact on sections over members of $\mathcal{B}$. So it gives a short exact sequence of Čech complexes, and $\mathcal{G}$ again has vanishing Čech cohomology, one degree lower. The cohomology of $\mathcal{F}$ in degree $p + 1$ is the cohomology of $\mathcal{G}$ in degree $p$, and induction on $p$ finishes.

On an affine scheme the basic open sets and their finite covers by basic open sets satisfy the hypotheses, by Corollary P4.1.3. Once quasi-coherent sheaves have no higher cohomology on affine pieces, Leray's theorem says that any cover by affine open sets with affine intersections computes cohomology, and on a separated scheme every intersection of affine open sets is affine.

### Examples

**Example P4.1.12 (the punctured plane is not affine).** Let $U = \mathbb{A}^2_k \setminus \{0\} = D(x) \cup D(y)$. The open sets $D(x)$, $D(y)$ and $D(x) \cap D(y) = D(xy)$ are affine, so by Corollary P4.1.9 and Example P4.1.5
$$H^1(U, \mathcal{O}_U) \cong \bigoplus_{i, j \geq 1} k \cdot x^{-i} y^{-j} \neq 0.$$
By Theorem P4.1.8, $U$ is not affine. This is a second proof of Example P3.2.8, which used that $\Gamma(U, \mathcal{O}_U) = k[x, y]$. Corollary P4.1.10 gives $H^p(U, \mathcal{F}) = 0$ for $p \geq 2$ and every quasi-coherent $\mathcal{F}$.

**Example P4.1.13 (the affine line with a doubled origin).** Let $X$ be the line with a doubled origin of Example P3.2.5, glued from two copies $U_1$ and $U_2$ of $\mathbb{A}^1_k = \operatorname{Spec} k[t]$ along $U_{12} = \operatorname{Spec} k[t, t^{-1}]$. The scheme $X$ is not separated (Example P3.4.4), but $U_{12}$ is affine, so Corollary P4.1.9 applies to the cover $(U_1, U_2)$. The Čech complex of $\mathcal{O}_X$ is
$$k[t] \times k[t] \xrightarrow{d} k[t, t^{-1}], \qquad d(a, b) = b - a.$$
Its kernel is $k[t]$ and its image is $k[t]$. So $H^0(X, \mathcal{O}_X) = k[t]$ and
$$H^1(X, \mathcal{O}_X) \cong k[t, t^{-1}]/k[t] = \bigoplus_{m \geq 1} k \cdot t^{-m},$$
infinite-dimensional, although $X$ is of finite type over $k$ and covered by two copies of the affine line. For $\mathbb{P}^1$ the same two affine lines are glued by $t \mapsto t^{-1}$, the image of $d$ becomes all of $k[t, t^{-1}]$, and $H^1(\mathbb{P}^1, \mathcal{O}) = 0$ (Example P2.7.23). The failure of separatedness is not the cause: the punctured plane of Example P4.1.12 is separated and also has an infinite-dimensional $H^1$. Chapter 2 proves that on a projective scheme over a field the cohomology groups of a coherent sheaf are finite-dimensional.

**Example P4.1.14 (the projective line is not affine).** By Example P2.7.23, $H^1(\mathbb{P}^1_k, \mathcal{O}(-2)) \cong k$. The sheaf $\mathcal{O}(-2)$ is quasi-coherent, so Theorem P4.1.8 shows again that $\mathbb{P}^1_k$ is not affine. More generally, a scheme with a quasi-coherent sheaf that has a nonzero higher cohomology group is not affine. Section 1.3 proves a converse for Noetherian schemes.

**Example P4.1.15 (an extension that is not split).** On $X = \mathbb{A}^1_k$ the sequence $0 \to \mathcal{O}_X \xrightarrow{t} \mathcal{O}_X \to k(0) \to 0$ of Example P3.5.4 shows an extension of the skyscraper sheaf $k(0)$ by $\mathcal{O}_X$. Its middle term is quasi-coherent, as part 2 of Corollary P4.1.11 predicts. It does not split, since $\mathcal{O}_X$ has no torsion sections and $k(0)$ is torsion. On global sections it is $0 \to k[t] \xrightarrow{t} k[t] \to k \to 0$, exact as part 1 predicts.

### Proof

*Theorem P4.1.7.* Restriction maps make $U \mapsto H^p(U, \mathcal{F})$ a presheaf, and $H^p(U, \mathcal{F}) = H^p(U, \mathcal{F}|_U)$ (part 3 of Theorem P2.7.3). The proof is by induction on $p \geq 1$, for the statement: for every sheaf $\mathcal{F}$ that satisfies hypothesis 3, $H^q(U, \mathcal{F}) = 0$ for every $U \in \mathcal{B}$ and every $1 \leq q \leq p$. Hypotheses 1 and 2 do not involve $\mathcal{F}$.

*The case $p = 1$.* Let $U \in \mathcal{B}$ and $\xi \in H^1(U, \mathcal{F})$. By part 5 of Theorem P2.7.3 every point of $U$ has an open neighbourhood on which $\xi$ restricts to $0$. These neighbourhoods form an open cover of $U$, and by hypothesis 2 it has a refinement $\mathcal{U} = (U_i) \in \mathsf{Cov}$ that covers $U$. Each $U_i$ lies in one of the neighbourhoods, so $\xi|_{U_i} = 0$ for all $i$. By Theorem P2.7.22, applied to the space $U$ and the sheaf $\mathcal{F}|_U$, $\xi$ lies in the image of $\check{H}^1(\mathcal{U}, \mathcal{F}) \to H^1(U, \mathcal{F})$. This group is $0$ by hypothesis 3, so $\xi = 0$.

*The inductive step.* Assume the statement for $p \geq 1$, and let $\mathcal{F}$ satisfy hypothesis 3. Embed $\mathcal{F}$ in an injective sheaf $\mathcal{I}$ of $\mathsf{Ab}(X)$, which has enough injectives by Theorem P2.5.23, and let $\mathcal{G} = \mathcal{I}/\mathcal{F}$, so that $0 \to \mathcal{F} \to \mathcal{I} \to \mathcal{G} \to 0$ is exact. The sheaf $\mathcal{I}$ is flasque by part 1 of Theorem P2.7.11, so is every restriction $\mathcal{I}|_V$, and so $H^q(V, \mathcal{I}) = 0$ for every open $V$ and $q > 0$ by part 2 of Theorem P2.7.11.

For every $V \in \mathcal{B}$, $H^1(V, \mathcal{F}) = 0$ by the case $p = 1$. The long exact sequence on $V$ (part 2 of Theorem P2.7.3) gives the exactness of $0 \to \mathcal{F}(V) \to \mathcal{I}(V) \to \mathcal{G}(V) \to 0$. Let $\mathcal{U} \in \mathsf{Cov}$. By hypothesis 1 every finite intersection of its members lies in $\mathcal{B}$, so the sequence of Čech complexes
$$0 \to \check{C}^\bullet(\mathcal{U}, \mathcal{F}) \to \check{C}^\bullet(\mathcal{U}, \mathcal{I}) \to \check{C}^\bullet(\mathcal{U}, \mathcal{G}) \to 0$$
is exact in each degree, being a finite product of exact sequences. By Theorem P2.7.20, $\check{H}^q(\mathcal{U}, \mathcal{I}) = 0$ for $q > 0$. The long exact sequence of cohomology of this sequence of complexes gives $\check{H}^q(\mathcal{U}, \mathcal{G}) \cong \check{H}^{q+1}(\mathcal{U}, \mathcal{F}) = 0$ for $q \geq 1$. So $\mathcal{G}$ satisfies hypothesis 3, and by the inductive hypothesis $H^q(U, \mathcal{G}) = 0$ for $U \in \mathcal{B}$ and $1 \leq q \leq p$. The long exact sequence on $U$ and the vanishing of $H^q(U, \mathcal{I})$ for $q \geq 1$ give $H^{q+1}(U, \mathcal{F}) \cong H^q(U, \mathcal{G})$ for $q \geq 1$. So $H^{p+1}(U, \mathcal{F}) = 0$, which completes the induction. $\square$

*Theorem P4.1.8.* After an isomorphism, $X = \operatorname{Spec} A$. By Theorem P3.5.12, $\mathcal{F} \cong \widetilde{M}$ with $M = \mathcal{F}(X)$. Let $\mathcal{B}$ be the set of basic open sets $D(g)$, $g \in A$, and $\mathsf{Cov}$ the set of covers of some $D(g)$ by finitely many basic open sets $D(f_i) \subseteq D(g)$. Hypothesis 1 holds since $D(f_{i_0}) \cap \cdots \cap D(f_{i_p}) = D(f_{i_0} \cdots f_{i_p})$. For hypothesis 2, an open cover of $D(g)$ can be refined to a cover by basic open sets, since these form a basis of the topology, and $D(g) \cong \operatorname{Spec} A_g$ (Proposition P3.1.13) is quasi-compact, so finitely many of them suffice. Hypothesis 3 is Corollary P4.1.3. Theorem P4.1.7 gives $H^p(D(g), \mathcal{F}) = 0$ for $p > 0$, and $D(1) = X$. $\square$

*Corollary P4.1.9.* The restriction of $\mathcal{F}$ to an open subscheme is quasi-coherent, and $H^q(V, \mathcal{F}) = H^q(V, \mathcal{F}|_V)$ (part 3 of Theorem P2.7.3). So Theorem P4.1.8 gives $H^q(U_{i_0 \cdots i_p}, \mathcal{F}) = 0$ for all $q > 0$ and all finite intersections, which is the hypothesis of Leray's theorem, Theorem P2.7.21. If $X$ is separated, a finite intersection of affine open sets is affine by Proposition P3.4.12 and induction on the number of sets. $\square$

*Corollary P4.1.10.* Order the index set $\{1, \dots, r\}$ of the cover. The ordered Čech complex of Definition P2.7.18 has $\check{C}^p = 0$ for $p \geq r$, since there are no strictly increasing tuples of length $p + 1 > r$. Corollary P4.1.9 identifies its cohomology with $H^p(X, \mathcal{F})$. The scheme $\mathbb{P}^n_A$ is separated (Example P3.4.6) and is covered by the $n + 1$ affine open sets $D_+(x_i)$. $\square$

*Corollary P4.1.11.* (1) This is the long exact sequence of part 2 of Theorem P2.7.3 and $H^1(X, \mathcal{F}') = 0$ (Theorem P4.1.8).

(2) Let $X = \operatorname{Spec} A$ and $\theta$ the counit of Theorem P3.5.2, natural in the sheaf. By part 1, applied to $X$, the global sections form an exact sequence $0 \to \mathcal{F}'(X) \to \mathcal{F}(X) \to \mathcal{F}''(X) \to 0$, and the functor $M \mapsto \widetilde{M}$ is exact (part 2 of Proposition P3.5.1). So there is a commutative diagram with exact rows
$$\begin{array}{ccccccccc} 0 & \to & \mathcal{F}'(X)^\sim & \to & \mathcal{F}(X)^\sim & \to & \mathcal{F}''(X)^\sim & \to & 0 \\ & & \downarrow \theta_{\mathcal{F}'} & & \downarrow \theta_{\mathcal{F}} & & \downarrow \theta_{\mathcal{F}''} & & \\ 0 & \to & \mathcal{F}' & \to & \mathcal{F} & \to & \mathcal{F}'' & \to & 0. \end{array}$$
The outer vertical maps are isomorphisms by Theorem P3.5.12, so $\theta_\mathcal{F}$ is an isomorphism by the five lemma in the abelian category $\mathsf{Mod}(\mathcal{O}_X)$, and $\mathcal{F}$ is quasi-coherent by Theorem P3.5.12. On a general scheme, quasi-coherence is local (Proposition P3.5.10), and the restriction of the sequence to an affine open set is an exact sequence of the same kind. $\square$

### Exercises

1. (B) Let $X$ be the affine plane with a doubled origin of Example P3.4.5, glued from two copies $U_1$, $U_2$ of $\mathbb{A}^2_k$ along $\mathbb{A}^2_k \setminus \{0\}$. Show that $X$ has no cover by affine open sets with affine pairwise intersections. (An affine open set through one origin and one through the other meet in $W \setminus \{0\}$ for an open $W \subseteq \mathbb{A}^2_k$ that contains $0$; compare with Example P4.1.12.) Use the Mayer-Vietoris sequence of P2 Ch. 7 for $(U_1, U_2)$ to show that $H^1(X, \mathcal{O}_X) = 0$ and $H^2(X, \mathcal{O}_X) \cong H^1(\mathbb{A}^2_k \setminus \{0\}, \mathcal{O})$, which is nonzero. So the hypothesis on intersections in Corollary P4.1.10 cannot be dropped.
2. (A) Let $X = \operatorname{Spec} A$ and let $\mathcal{U}$ be any finite cover of $X$ by affine open sets, not necessarily basic. Show that $\check{H}^p(\mathcal{U}, \widetilde{M}) = 0$ for $p > 0$. (An affine scheme is separated.)
3. (A) Let $X$ be a separated scheme and $\mathcal{F}$ quasi-coherent. Show that $H^p(X, \mathcal{F})$ is the colimit of $\check{H}^p(\mathcal{U}, \mathcal{F})$ over finite affine covers when $X$ is quasi-compact, and that each map in the system is an isomorphism.
4. (A) Let $C \subseteq \mathbb{P}^2_k$ be a plane curve, the closed subscheme $V_+(F)$ of a homogeneous polynomial $F$ of degree $d \geq 1$. Show that $H^p(C, \mathcal{F}) = 0$ for $p \geq 2$ and every quasi-coherent $\mathcal{F}$. (Find two affine open sets that cover $C$.)
5. (B) Show that part 1 of Corollary P4.1.11 fails without the quasi-coherence of $\mathcal{F}'$: on $X = \mathbb{A}^1_k$ with $U = X \setminus \{0\}$ and $j \colon U \to X$ the inclusion, the extension by zero $j_! \mathcal{O}_U$ is not quasi-coherent, and $\Gamma(X, \mathcal{O}_X) \to \Gamma(X, \mathcal{O}_X / j_! \mathcal{O}_U)$ is not surjective. (Section 1.4 computes the cokernel.)
6. (B) Let $X$ be a quasi-compact separated scheme covered by $r$ affine open sets. Show that $H^p(X, \mathcal{F})$ is a quotient of a submodule of $\prod_{i_0 < \cdots < i_p} \mathcal{F}(U_{i_0 \cdots i_p})$, and deduce that if all $\mathcal{F}(U_{i_0 \cdots i_p})$ are finite-dimensional over $k$, then so is $H^p(X, \mathcal{F})$.
7. (B) Prove the following form of Theorem P4.1.7 for a basis: if $\mathcal{B}$ is a basis of the topology closed under finite intersections, every $U \in \mathcal{B}$ is quasi-compact, and $\check{H}^p(\mathcal{U}, \mathcal{F}) = 0$ for every finite cover of a member of $\mathcal{B}$ by members of $\mathcal{B}$ and every $p > 0$, then $H^p(U, \mathcal{F}) = 0$ for $U \in \mathcal{B}$ and $p > 0$.
8. (C) Let $X$ be a quasi-compact scheme in which the intersection of two affine open sets is quasi-compact. Show that $H^p(X, \mathcal{F}) = 0$ for $p$ larger than a bound that depends only on $X$. (Cover $X$ by affines and each pairwise intersection by finitely many affines, and use a spectral sequence in the style of P2 Ch. 4.)

### Lean

Mathlib defines sheaf cohomology on a site as Ext groups, `CategoryTheory.Sheaf.H`, and has affine schemes and quasi-coherent sheaves of modules. Cartan's criterion, the vanishing of the cohomology of quasi-coherent sheaves on affine schemes, the comparison of Čech cohomology with sheaf cohomology on separated schemes and the closure of quasi-coherent sheaves under extensions are not in Lean as stated. The handbook adds no `MinimalModel` node here.

### Notes and history

Theorem P4.1.8 is Serre's, in *Faisceaux algébriques cohérents* (1955), for affine varieties and Čech cohomology. For schemes and derived functor cohomology it is EGA III, Théorème 1.3.1, and Hartshorne, Theorem III.3.5, which proves it for Noetherian affine schemes by showing that the injective $A$-modules give flasque sheaves. The route through Theorem P4.1.7, which needs no Noetherian hypothesis, follows the Stacks project, chapter Cohomology of sheaves, where the criterion is stated for a basis with a family of coverings. It is often called Cartan's criterion. The literature state is theorem. In the minimal model program the theorem is the reason why the higher direct images $R^i f_* \mathcal{F}$ can be computed over an affine base as $H^i(X, \mathcal{F})^\sim$, which Chapter 4 proves, and so why every vanishing theorem of Volume 5 is local over the base.
