---
title: Čech complexes on affine schemes
nodes: []
sources: [Har77, Vak25, GW23, Stacks]
reads_with: [Har77:III.4, Vak25:ch18]
requires: [P1.2, P2.7, P3.1, P3.5]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Čech complexes on affine schemes

### Statement

Throughout the section $A$ is a ring, $X = \operatorname{Spec} A$ and $M$ is an $A$-module. For elements $g_1, \dots, g_m \in A$ write $M_{g_1 \cdots g_m}$ for the localization of $M$ at the product $g_1 \cdots g_m$. Recall that $D(g) \cap D(h) = D(gh)$ and that $\widetilde{M}(D(g)) = M_g$ (Corollary P3.1.5).

**Definition P4.1.1 (the Čech complex of a module).** Let $f_1, \dots, f_r \in A$. The *Čech complex* $\check{C}^\bullet(f, M)$ of $M$ for $f = (f_1, \dots, f_r)$ has terms
$$\check{C}^p(f, M) = \prod_{1 \leq i_0 < \cdots < i_p \leq r} M_{f_{i_0} \cdots f_{i_p}}, \qquad 0 \leq p \leq r - 1,$$
and differential
$$(d c)_{i_0 \cdots i_{p+1}} = \sum_{k=0}^{p+1} (-1)^k \, c_{i_0 \cdots \widehat{i_k} \cdots i_{p+1}},$$
where each term on the right is mapped to $M_{f_{i_0} \cdots f_{i_{p+1}}}$ by the localization map. As in Definition P2.7.18, a cochain $c$ is extended to all index tuples by the alternating rule: $c$ vanishes on a tuple with a repeated index and changes sign when two indices are exchanged. The *augmented Čech complex* is
$$0 \to M \xrightarrow{\varepsilon} \check{C}^0(f, M) \xrightarrow{d} \check{C}^1(f, M) \xrightarrow{d} \cdots \xrightarrow{d} \check{C}^{r-1}(f, M) \to 0, \qquad \varepsilon(m) = (m/1)_i.$$

Let $U = D(f_1) \cup \cdots \cup D(f_r)$ and let $\mathcal{U}$ be its cover by the open sets $D(f_i)$. The intersection $D(f_{i_0}) \cap \cdots \cap D(f_{i_p})$ is $D(f_{i_0} \cdots f_{i_p})$, so $\check{C}^\bullet(f, M)$ is the Čech complex $\check{C}^\bullet(\mathcal{U}, \widetilde{M})$ of Definition P2.7.18, and $\varepsilon$ is the restriction from $\widetilde{M}(U)$ when $U = X$. Write $\check{H}^p(f, M)$ for its cohomology.

**Theorem P4.1.2 (exactness of the Čech complex).** If $f_1, \dots, f_r$ generate the unit ideal of $A$, then the augmented Čech complex of $M$ is exact.

Lean: not in Lean as stated.

**Corollary P4.1.3 (Čech cohomology of $\widetilde{M}$ for a standard cover).** Let $\mathcal{U}$ be a cover of $X = \operatorname{Spec} A$ by finitely many basic open sets $D(f_1), \dots, D(f_r)$. Then $\check{H}^0(\mathcal{U}, \widetilde{M}) = M$ and $\check{H}^p(\mathcal{U}, \widetilde{M}) = 0$ for all $p > 0$. The same holds for a cover of a basic open set $D(g)$ by finitely many basic open sets $D(f_i) \subseteq D(g)$, with $M_g$ in place of $M$.

Lean: Mathlib `CategoryTheory.cechComplexFunctor` is the Čech complex over all tuples. Theorem P4.1.2 and Corollary P4.1.3 are not in Lean as stated.

A cover of $X$ by basic open sets $D(f_i)$ is a cover if and only if no prime contains all the $f_i$, that is, if and only if the $f_i$ generate the unit ideal, since every proper ideal lies in a maximal ideal. Since $X$ is quasi-compact, every open cover of $X$ has a refinement by finitely many basic open sets. So Corollary P4.1.3 covers enough covers to be used in Section 1.2.

### Proof in words

Exactness of a complex of $A$-modules is a local property, and the basic open sets $D(f_j)$ cover $\operatorname{Spec} A$. So it suffices to prove exactness after inverting one $f_j$. Localization is exact and commutes with finite products, so after inverting $f_j$ the complex is the Čech complex of $M_{f_j}$ for the same elements, one of which is now a unit. The open set $D(f_j)$ is then the whole space, and a cochain can be pushed down one degree by putting the index $j$ in front: $(hc)_{i_0 \cdots i_{p-1}} = c_{j i_0 \cdots i_{p-1}}$. This is the homotopy of the proof of Proposition P2.7.19, and it shows that the complex is contractible. Geometrically, a cover that contains the whole space as one of its members has trivial Čech cohomology.

### Examples

**Example P4.1.4 (partial fractions).** Let $A = k[x]$ with $k$ a field, $f_1 = x$ and $f_2 = x - 1$. These generate the unit ideal, since $x - (x - 1) = 1$. The augmented Čech complex of $A$ is
$$0 \to k[x] \to k[x]_x \times k[x]_{x-1} \xrightarrow{d} k[x]_{x(x-1)} \to 0, \qquad d(a, b) = b - a.$$
Exactness on the left says that a rational function with poles only at $0$ and also only at $1$ is a polynomial. Exactness on the right says that every $g/(x^a (x-1)^b)$ with $g \in k[x]$ is a difference $p/x^a - q/(x-1)^b$ with polynomials $p$ and $q$. This is the decomposition into partial fractions, and the proof of Theorem P4.1.2 produces it: write $1 = (x - (x-1))^{a+b}$ and expand.

**Example P4.1.5 (the punctured plane).** Let $A = k[x, y]$, $f_1 = x$, $f_2 = y$. These do not generate the unit ideal, and $U = D(x) \cup D(y)$ is the punctured plane $\mathbb{A}^2 \setminus \{0\}$ of Example P3.1.10. The Čech complex of $A$ is
$$k[x, y]_x \times k[x, y]_y \xrightarrow{d} k[x, y]_{xy}, \qquad d(a, b) = b - a.$$
All three rings have bases of Laurent monomials $x^i y^j$: with $j \geq 0$ for $A_x$, with $i \geq 0$ for $A_y$, and all $(i, j) \in \mathbb{Z}^2$ for $A_{xy}$. The map $d$ is homogeneous for the $\mathbb{Z}^2$-grading, so its kernel and cokernel can be read off monomial by monomial. The kernel is spanned by the monomials in both $A_x$ and $A_y$, the $x^i y^j$ with $i, j \geq 0$, so $\check{H}^0 = k[x, y]$, as in Example P3.1.10. The image is spanned by the monomials with $i \geq 0$ or $j \geq 0$, so
$$\check{H}^1(f, A) = \bigoplus_{i, j \geq 1} k \cdot x^{-i} y^{-j},$$
an infinite-dimensional vector space. Corollary P4.1.3 does not apply, and Example P4.1.12 identifies this group with $H^1(U, \mathcal{O}_U)$.

**Example P4.1.6 (a module with torsion).** Let $A = \mathbb{Z}$, $M = \mathbb{Z}/6$, $f_1 = 2$ and $f_2 = 3$, which generate the unit ideal. Then $M_2 = \mathbb{Z}/3$, since $2$ is a unit on $\mathbb{Z}/3$ and inverting $2$ kills $\mathbb{Z}/2$. Similarly $M_3 = \mathbb{Z}/2$ and $M_6 = 0$. The augmented complex is $0 \to \mathbb{Z}/6 \to \mathbb{Z}/3 \times \mathbb{Z}/2 \to 0 \to 0$, and its exactness is the Chinese remainder theorem.

### Proof

*Theorem P4.1.2.* Let $K^\bullet$ be the augmented complex, with $K^{-1} = M$ and $K^p = \check{C}^p(f, M)$ for $p \geq 0$. Its cohomology modules $H^p(K^\bullet)$ are $A$-modules. Fix $j \in \{1, \dots, r\}$. Localization at $f_j$ is exact (Theorem P1.2.5), so $H^p(K^\bullet)_{f_j} = H^p(K^\bullet_{f_j})$. It commutes with finite products, and $(M_{g})_{f_j} = (M_{f_j})_{g}$ for $g \in A$. So $K^\bullet_{f_j}$ is the augmented Čech complex of the $A_{f_j}$-module $M' = M_{f_j}$ for the images of $f_1, \dots, f_r$ in $A' = A_{f_j}$. In $A'$ the element $f_j$ is a unit, so $M'_{f_j g} = M'_{g}$ for every $g \in A'$.

Define $h \colon K^{p}_{f_j} \to K^{p-1}_{f_j}$ for $p \geq 0$ by
$$(h c)_{i_0 \cdots i_{p-1}} = c_{j i_0 \cdots i_{p-1}} \quad (p \geq 1), \qquad h c = c_j \quad (p = 0),$$
using the alternating extension of $c$. The entry $c_{j i_0 \cdots i_{p-1}}$ lies in $M'_{f_j f_{i_0} \cdots f_{i_{p-1}}} = M'_{f_{i_0} \cdots f_{i_{p-1}}}$, the right module. The formula is alternating in $i_0, \dots, i_{p-1}$, so $hc$ is a cochain. For $p \geq 1$ and a cochain $c$ of degree $p$,
$$(d h c)_{i_0 \cdots i_p} = \sum_{k=0}^{p} (-1)^k c_{j i_0 \cdots \widehat{i_k} \cdots i_p}, \qquad (h d c)_{i_0 \cdots i_p} = (dc)_{j i_0 \cdots i_p} = c_{i_0 \cdots i_p} - \sum_{k=0}^{p} (-1)^k c_{j i_0 \cdots \widehat{i_k} \cdots i_p},$$
since the index $i_k$ of the tuple $j i_0 \cdots i_p$ sits in position $k + 1$. So $dh + hd = \mathrm{id}$ in degree $p$. The alternating rule makes these formulas valid also when $j$ is one of the $i_k$, where both sides are computed with the same conventions. In degree $0$, $(\varepsilon h c)_i = c_j$ and $(h d c)_i = (dc)_{j i} = c_i - c_j$, so $\varepsilon h + h d = \mathrm{id}$. In degree $-1$, $h \varepsilon m = m$. So the identity of $K^\bullet_{f_j}$ is homotopic to $0$, and $H^p(K^\bullet)_{f_j} = 0$ for every $p$ and every $j$.

Let $N = H^p(K^\bullet)$ and let $\mathfrak{p}$ be a prime of $A$. Some $f_j$ is not in $\mathfrak{p}$, since the $f_i$ generate the unit ideal. Then $N_\mathfrak{p}$ is a localization of $N_{f_j} = 0$, so $N_\mathfrak{p} = 0$. By Theorem P1.2.8, $N = 0$. $\square$

*Corollary P4.1.3.* By the discussion after Definition P4.1.1, $\check{C}^\bullet(\mathcal{U}, \widetilde{M}) = \check{C}^\bullet(f, M)$, and the $f_i$ generate the unit ideal because the $D(f_i)$ cover $X$. Theorem P4.1.2 says that $\varepsilon$ identifies $M$ with $\check{H}^0$ and that $\check{H}^p = 0$ for $p > 0$. For the second claim, $D(g) \cong \operatorname{Spec} A_g$ by Proposition P3.1.13, under which $D(f_i) \subseteq D(g)$ is the basic open set of the image of $f_i$ in $A_g$ and $\widetilde{M}|_{D(g)} \cong (M_g)^\sim$ (part 1 of Proposition P3.5.3). Apply the first claim to $A_g$ and $M_g$. $\square$

### Exercises

1. (A) Write down the augmented Čech complex of $A$ for a single element $f_1 = 1$, and for the pair $f_1 = f_2 = 1$. Check exactness directly.
2. (A) In Example P4.1.4, carry out the proof of Theorem P4.1.2 for $g/(x^2(x-1))$: find $p$ and $q$ with $g/(x^2(x-1)) = p/x^2 - q/(x-1)$ for $g = 1$.
3. (A) Let $A = k[x, y, z]$ and $f = (x, y, z)$. Show that $\check{H}^2(f, A)$ has the basis $x^{-i} y^{-j} z^{-l}$ with $i, j, l \geq 1$, and that $\check{H}^1(f, A) = 0$. (Use the $\mathbb{Z}^3$-grading as in Example P4.1.5, and compute the complex one monomial at a time.)
4. (B) Let $f_1, \dots, f_r \in A$ and let $\mathfrak{a} = (f_1, \dots, f_r)$. Show that $\check{H}^0(f, M) = \Gamma(U, \widetilde{M})$ for $U = X \setminus V(\mathfrak{a})$, and that the kernel of $\varepsilon \colon M \to \check{H}^0(f, M)$ is the set of $m \in M$ killed by a power of $\mathfrak{a}$. Show that $\check{H}^p(f, M)$ depends only on the radical of $\mathfrak{a}$. (Use Corollary P4.1.9.)
5. (B) Show that Theorem P4.1.2 holds for the Čech complex over all tuples $(i_0, \dots, i_p) \in \{1, \dots, r\}^{p+1}$, not only increasing ones, with the same homotopy $h$.
6. (B) Show that $M \mapsto \check{C}^\bullet(f, M)$ is an exact functor from $A$-modules to complexes, so that a short exact sequence of modules gives a long exact sequence of the groups $\check{H}^p(f, -)$. Use it and Example P4.1.5 to compute $\check{H}^p(f, k)$ for $A = k[x, y]$, $f = (x, y)$ and $k = A/(x, y)$.
7. (C) Let $A$ be a ring, $a \in A$, and $f = (a)$. Identify the cohomology of the complex $0 \to M \to M_a \to 0$ with the local cohomology modules of Chapter 8 for the ideal $(a)$: the kernel is the $a$-power torsion of $M$, and the cokernel is $M_a$ modulo the image of $M$. For $A = \mathbb{Z}$, $M = \mathbb{Z}$ and $a = p$ prime, show that the cokernel is $\mathbb{Z}[1/p]/\mathbb{Z}$.

### Lean

Mathlib defines the Čech complex of a presheaf for a family of objects in a category with finite products, `CategoryTheory.cechComplexFunctor`, over all tuples. It has the localization of modules and the sheaf $\widetilde{M}$ of P3 Ch. 5. The exactness of the Čech complex of a module for elements that generate the unit ideal and its sheaf form, Corollary P4.1.3, are not in Lean as stated. The handbook adds no `MinimalModel` node here.

### Notes and history

The Čech complex of a module for a sequence of elements is Serre's tool in *Faisceaux algébriques cohérents* (1955), where the cohomology of coherent sheaves on varieties is defined by Čech cochains. The homotopy that puts a fixed index in front is the standard proof that a cover containing the whole space has trivial Čech cohomology; the localization argument is in EGA III, Section 1, and in the Stacks project, chapter Cohomology of schemes. The complex of Exercise 7 and its relatives, the extended Čech complex and the Koszul complex, compute local cohomology, which returns in Chapter 8. The literature state is theorem.
