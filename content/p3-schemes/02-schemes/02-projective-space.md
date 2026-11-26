---
title: Projective space by gluing
nodes: []
sources: [Vak25, Har77, GW20, EGA1]
reads_with: [Vak25:ch4, Har77:II.2, GW20:ch3]
requires: [P1.2, P3.1]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Projective space by gluing

### Statement

Let $A$ be a ring and $n \geq 0$. Let $S = A[x_0, \dots, x_n]$ and $L = A[x_0^{\pm 1}, \dots, x_n^{\pm 1}]$, the ring of Laurent polynomials. For each $i$ let $S_{(x_i)} \subseteq S_{x_i}$ be the subring of elements of degree $0$, that is, of fractions $g/x_i^m$ with $g$ homogeneous of degree $m$. It is the polynomial ring $A[x_0/x_i, \dots, x_n/x_i]$ in the $n$ elements $x_j/x_i$, $j \neq i$ (Example P1.13.27 for $A = k$; the same proof works over any $A$).

**Definition P3.2.10 (projective space).** Let $U_i = \operatorname{Spec} S_{(x_i)} \cong \mathbb{A}^n_A$. For $i \neq j$ let $U_{ij} \subseteq U_i$ be the basic open set $D(x_j/x_i)$, so $U_{ij} = \operatorname{Spec} S_{(x_i x_j)}$, where $S_{(x_i x_j)}$ is the degree $0$ part of $S_{x_i x_j}$. The rings $S_{(x_i)}[(x_j/x_i)^{-1}]$ and $S_{(x_j)}[(x_i/x_j)^{-1}]$ are both equal to $S_{(x_i x_j)}$ inside $L$, and $\varphi_{ij} \colon U_{ij} \to U_{ji}$ is the morphism of this identity. *Projective $n$-space over $A$* is the scheme $\mathbb{P}^n_A$ glued from the $U_i$ along the $\varphi_{ij}$ by Theorem P3.2.3. The elements $x_0, \dots, x_n$ are the *homogeneous coordinates*, and $U_i$ is the *standard chart* where $x_i \neq 0$.

Lean: not in Lean as stated. Mathlib has the homogeneous spectrum `AlgebraicGeometry.Proj` of a graded ring, which Chapter 6 compares with this construction.

**Theorem P3.2.11 (global functions on projective space).** For $n \geq 1$, the map $A \to \Gamma(\mathbb{P}^n_A, \mathcal{O})$ is an isomorphism.

Lean: not in Lean as stated.

**Corollary P3.2.12 (projective space is not affine).** If $n \geq 1$ and $A \neq 0$, then $\mathbb{P}^n_A$ is not affine.

Lean: not in Lean as stated.

**Proposition P3.2.13 (points of projective space).** Let $K$ be a field, or more generally a local ring, with an $A$-algebra structure. Let $\mathrm{Um}(K)$ be the set of $(a_0, \dots, a_n) \in K^{n+1}$ that generate the unit ideal, that is, with some $a_i$ a unit. The morphisms $\operatorname{Spec} K \to \mathbb{P}^n_A$ over $\operatorname{Spec} A$ are in bijection with $\mathrm{Um}(K)/K^\times$, where $K^\times$ acts by scalar multiplication. The class of $(a_0, \dots, a_n)$ is written $[a_0 : \dots : a_n]$, and it corresponds to the morphism into $U_i$, for any $i$ with $a_i$ a unit, given by $x_j/x_i \mapsto a_j/a_i$.

Lean: not in Lean as stated.

### Proof in words

The cocycle condition holds because all the gluing maps are identities inside one ring, the Laurent ring $L$. Every chart ring $S_{(x_i)}$ and every overlap ring $S_{(x_i x_j)}$ is a subring of $L$, so a global function is a family of elements of $L$ that are all equal. It is one Laurent polynomial of degree $0$ that has no negative power of $x_j$ for any $j \neq i$, for every $i$. With two indices this forces all exponents to be $0$.

For the points, a map from a local scheme lands in one chart, because the only open set that contains the closed point is the whole space. In the chart it is an $n$-tuple $(a_j/a_i)$, and changing the chart multiplies the vector by a unit.

### Examples

**Example P3.2.14 (the projective line again).** For $n = 1$ and $A = k$, $U_0 = \operatorname{Spec} k[x_1/x_0]$ and $U_1 = \operatorname{Spec} k[x_0/x_1]$, glued along $x_0/x_1 = (x_1/x_0)^{-1}$. With $x = x_1/x_0$ and $y = x_0/x_1$ this is Example P3.2.6. The closed points of $\mathbb{P}^1_k$, for $k$ algebraically closed, are the points $[a_0 : a_1]$ of the classical projective line: $[1 : a]$ in $U_0$ and the point at infinity $[0 : 1]$.

**Example P3.2.15 (real points of the projective line).** For $A = K = \mathbb{R}$ the proposition gives $\mathbb{P}^1(\mathbb{R}) = \mathbb{R}^2 \setminus \{0\}/\mathbb{R}^\times$, the real projective line. The scheme $\mathbb{P}^1_\mathbb{R}$ has more points than $\mathbb{P}^1(\mathbb{R})$: the closed points of $U_0 = \operatorname{Spec} \mathbb{R}[x]$ include the points $(x^2 + bx + c)$ with $b^2 < 4c$, with residue field $\mathbb{C}$, which are the pairs of complex conjugate points of $\mathbb{P}^1(\mathbb{C})$.

**Example P3.2.16 (a hypersurface by gluing).** Let $F \in S$ be homogeneous of degree $d$. On $U_i$ let $f_i = F/x_i^d \in S_{(x_i)}$. On $U_{ij}$, $f_i = (x_j/x_i)^d f_j$, and $x_j/x_i$ is a unit there. So the closed subschemes $V(f_i) \subseteq U_i$ agree on overlaps: $V(f_i) \cap U_{ij}$ and $V(f_j) \cap U_{ji}$ are the same closed subscheme $\operatorname{Spec} S_{(x_i x_j)}/(f_i)$. Gluing the schemes $\operatorname{Spec} S_{(x_i)}/(f_i)$ along these gives a scheme $V(F)$ with a morphism to $\mathbb{P}^n_A$ that is a closed immersion in the sense of Chapter 3. For $F = x_0 x_2 - x_1^2$ in $\mathbb{P}^2_k$ this is the conic of Example P1.13.28, and for $F$ of degree $3$ in $\mathbb{P}^2_k$ it is a plane cubic, the projective closure of the curves of Section 1.4.

**Example P3.2.17 (the cubic with a node, projectively).** The nodal cubic $y^2 = x^2(x + 1)$ of Example P3.1.37 is the chart $U_2$ of $V(F) \subseteq \mathbb{P}^2_k$ for $F = x_1^2 x_2 - x_0^2 (x_0 + x_2)$, with $x = x_0/x_2$ and $y = x_1/x_2$. In the chart $U_1$, with $u = x_0/x_1$ and $w = x_2/x_1$, the equation is $w - u^2(u + w) = 0$, and the points with $x_2 = 0$ satisfy $u^3 = 0$, $w = 0$. So the line at infinity $V(x_2)$ meets the cubic in the single point $[0 : 1 : 0]$ with the non-reduced scheme $\operatorname{Spec} k[u]/(u^3)$: the line is a flex tangent. The scheme structure records the multiplicity $3 = \deg F$, as Bezout predicts.

**Example P3.2.18 (projective space over the integers).** For $A = \mathbb{Z}$ the scheme $\mathbb{P}^n_\mathbb{Z}$ maps to $\operatorname{Spec} \mathbb{Z}$, and every $\mathbb{P}^n_A$ is obtained from it by base change, $\mathbb{P}^n_A = \mathbb{P}^n_\mathbb{Z} \times_{\operatorname{Spec} \mathbb{Z}} \operatorname{Spec} A$, as Chapter 3 shows. The proposition gives $\mathbb{P}^n_\mathbb{Z}(\mathbb{F}_q) = (\mathbb{F}_q^{n+1} \setminus \{0\})/\mathbb{F}_q^\times$, a set with $(q^{n+1} - 1)/(q - 1) = 1 + q + \dots + q^n$ elements.

### Proof

The gluing data. Inside $L$, the subring $S_{(x_i x_j)}$ consists of the sums of monomials $\prod_k x_k^{e_k}$ with $\sum e_k = 0$ and $e_k \geq 0$ for $k \neq i, j$. The ring $S_{(x_i)}[(x_j/x_i)^{-1}]$ is generated by the $x_k/x_i$ and by $x_i/x_j$, and these monomials generate exactly that set: a monomial with $e_k \geq 0$ for $k \neq i, j$ and total degree $0$ is $\prod_{k \neq i, j} (x_k/x_i)^{e_k} \cdot (x_i/x_j)^{-e_j}$ if $e_j \leq 0$, and $\prod_{k \neq i, j}(x_k/x_i)^{e_k} (x_j/x_i)^{e_j}$ if $e_j \geq 0$. The description is symmetric in $i$ and $j$, so the same ring is $S_{(x_j)}[(x_i/x_j)^{-1}]$. So $\varphi_{ij}$ is well defined, and $\varphi_{ji} = \varphi_{ij}^{-1}$. For three indices, $U_{ij} \cap U_{ik} = \operatorname{Spec} S_{(x_i x_j x_k)}$, and all three maps $\varphi_{ij}$, $\varphi_{jk}$, $\varphi_{ik}$ are induced by the identity of the subring $S_{(x_i x_j x_k)}$ of $L$, so conditions 2 and 3 of Theorem P3.2.3 hold. The localization maps from all these rings to $L$ are injective, since each ring is a subring of $L$ by construction and each $x_k$ is a nonzerodivisor in $S$. $\square$

*Proof of Theorem P3.2.11.* By the sheaf property for the cover $(U_i)$, a global section is a family $s_i \in S_{(x_i)}$ with the same image in $S_{(x_i x_j)}$ for all $i, j$. All these rings are subrings of $L$ and the maps are inclusions, so the family is one element $s \in L$ that lies in every $S_{(x_i)}$. Write $s$ as a sum of monomials $\prod_k x_k^{e_k}$. Membership in $S_{(x_0)}$ forces $e_k \geq 0$ for $k \neq 0$, and membership in $S_{(x_1)}$ forces $e_0 \geq 0$, since $n \geq 1$. So all $e_k \geq 0$, and $\sum e_k = 0$ forces all $e_k = 0$. So $s \in A$. Conversely every $a \in A$ is a global section, and $A \to L$ is injective. $\square$

*Proof of Corollary P3.2.12.* Let $X = \mathbb{P}^n_A$. By Theorem P3.2.11, $c_X$ of Corollary P3.1.24 is a morphism $X \to \operatorname{Spec} A$, and it sends a point $x$ to $\{a \in A : a(x) = 0\}$. Since $A \neq 0$, it has a prime $\mathfrak{p}$. In the chart $U_0 = \operatorname{Spec} A[t_1, \dots, t_n]$, with $t_j = x_j/x_0$, the ideals $\mathfrak{q} = \mathfrak{p} A[t] + (t_1, \dots, t_n)$ and $\mathfrak{q}' = \mathfrak{p} A[t] + (t_1 - 1, t_2, \dots, t_n)$ are primes, since $A[t]/\mathfrak{q} \cong A/\mathfrak{p} \cong A[t]/\mathfrak{q}'$. They are distinct, since $1 = t_1 - (t_1 - 1)$ is in $\mathfrak{q} + \mathfrak{q}'$ and $1 \notin \mathfrak{q}$. Both contract to $\mathfrak{p}$ in $A$. So $c_X$ is not injective, and $X$ is not affine by Corollary P3.1.24. $\square$

*Proof of Proposition P3.2.13.* Let $K$ be a local $A$-algebra with maximal ideal $\mathfrak{m}$, and let $f \colon \operatorname{Spec} K \to \mathbb{P}^n_A$ be a morphism over $A$. The closed point $\mathfrak{m}$ lies in some $f^{-1}(U_i)$. Every prime of $K$ lies in $\mathfrak{m}$, so every point of $\operatorname{Spec} K$ specializes to $\mathfrak{m}$, and an open set that contains $\mathfrak{m}$ contains every point. So $f$ factors through $U_i$. By Theorem P3.1.22, $f$ is then an $A$-algebra map $S_{(x_i)} \to K$, that is, a tuple $(b_j)_{j \neq i}$ in $K$. With $b_i = 1$, the vector $b = (b_0, \dots, b_n)$ is in $\mathrm{Um}(K)$. If $f$ also factors through $U_j$, then $f$ factors through $U_i \cap U_j = U_{ij} = D(x_j/x_i)$, so $b_j$ is a unit, and the tuple in the chart $U_j$ is $b/b_j$. So the class of $b$ in $\mathrm{Um}(K)/K^\times$ does not depend on the choice of chart.

Conversely let $a \in \mathrm{Um}(K)$. Since $K$ is local and the $a_i$ generate the unit ideal, some $a_i$ is a unit: otherwise all $a_i$ lie in $\mathfrak{m}$. Define $f$ through $U_i$ by $x_j/x_i \mapsto a_j/a_i$. If $a_j$ is also a unit, the two definitions through $U_i$ and $U_j$ agree, since both factor through $U_{ij}$ and the ring map $S_{(x_i x_j)} \to K$ sends each monomial $\prod x_k^{e_k}$ with $\sum e_k = 0$ to $\prod a_k^{e_k}$ in both cases. Replacing $a$ by $\lambda a$ with $\lambda \in K^\times$ does not change $a_j/a_i$. These two constructions are inverse to each other. $\square$

### Exercises

1. (A) Show that $\mathbb{P}^0_A = \operatorname{Spec} A$.
2. (A) Show that the $n + 1$ points $[1 : 0 : \dots : 0], \dots, [0 : \dots : 0 : 1]$ of $\mathbb{P}^n_k$ are closed, and that the complement of $U_0$ in $\mathbb{P}^n_k$ is homeomorphic to $\mathbb{P}^{n-1}_k$. (Use Example P3.2.16 with $F = x_0$.)
3. (A) Count the points of $\mathbb{P}^2(\mathbb{F}_2)$ and list the lines of $\mathbb{P}^2_{\mathbb{F}_2}$ through each of them. (This is the Fano plane.)
4. (B) Let $A$ be a ring and $e \in A$ an idempotent with $e \neq 0, 1$. Show that $\mathbb{P}^n_A = \mathbb{P}^n_{Ae} \sqcup \mathbb{P}^n_{A(1-e)}$.
5. (B) Let $R$ be any $A$-algebra. Show that each $(a_0, \dots, a_n) \in R^{n+1}$ that generates the unit ideal defines a morphism $\operatorname{Spec} R \to \mathbb{P}^n_A$, by gluing the morphisms $\operatorname{Spec} R_{a_i} \to U_i$ with Proposition P3.2.4, and that $(a_i)$ and $(\lambda a_i)$ give the same morphism for $\lambda \in R^\times$. (Chapter 6 shows that not every morphism arises in this way when $\operatorname{Pic}(R) \neq 0$.)
6. (B) Show that $V(x_0 x_2 - x_1^2) \subseteq \mathbb{P}^2_k$ is isomorphic to $\mathbb{P}^1_k$, by gluing the isomorphisms $\operatorname{Spec} k[t] \to V \cap U_0$, $t \mapsto (x_1/x_0 = t, x_2/x_0 = t^2)$, and its analogue on $V \cap U_2$.
7. (C) Show that for $n \geq 1$ every morphism $\mathbb{P}^n_A \to \mathbb{A}^1_A$ over $A$ is constant, that is, factors through a section $\operatorname{Spec} A \to \mathbb{A}^1_A$. (Use Theorem P3.2.11 and Theorem P3.1.22.)

### Lean

Mathlib does not have $\mathbb{P}^n_A$ as a glued scheme with the statements of this section. It has `AlgebraicGeometry.Proj`, the scheme of a graded ring, and `AlgebraicGeometry.AffineSpace` for the charts. The computation of global sections, the failure of affineness and the description of points with values in a local ring are not in Lean as stated. The handbook adds no `MinimalModel` node here.

### Notes and history

Projective space over a ring by gluing is the first non-affine example in Hartshorne, Section II.2, and in Vakil, Chapter 4. EGA II constructs it as $\operatorname{Proj}$ of a polynomial ring, the approach of Chapter 6. The description of points with values in a local ring is the first step toward the description of $\mathbb{P}^n$ as the scheme that represents the functor of line bundles with $n + 1$ generating sections, which Chapter 6 proves. The literature state is theorem. Example P3.2.17 is the classical computation of a flex of the nodal cubic.
