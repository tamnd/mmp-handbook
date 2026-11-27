---
title: Representable functors and the Grassmannian
nodes: []
sources: [Vak25, Har77, Stacks]
reads_with: [Vak25:ch24, Har77:III.9]
requires: [P2.1, P3.2, P3.5, P3.6, P3.7]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Representable functors and the Grassmannian

### Statement

A scheme $X$ is determined by its functor of points $h_X = \operatorname{Hom}(-, X)$ (Theorem P3.2.33). A moduli problem gives a functor $F \colon \mathsf{Sch}^{\mathrm{op}} \to \mathsf{Set}$, which sends $T$ to the set of families over $T$ and a morphism $g \colon T' \to T$ to the pullback of families. For $\xi \in F(T)$ write $g^* \xi = F(g)(\xi)$.

**Definition P3.13.23 (representable functors, Zariski sheaves, open subfunctors).** Let $F \colon \mathsf{Sch}^{\mathrm{op}} \to \mathsf{Set}$ be a functor.

1. $F$ is *represented* by a scheme $X$ and a *universal element* $\xi \in F(X)$ if for every scheme $T$ the map $h_X(T) \to F(T)$, $g \mapsto g^* \xi$, is a bijection. By the Yoneda lemma (Theorem P2.1.23) this is the same as an isomorphism $h_X \cong F$, and $(X, \xi)$ is unique up to a unique isomorphism.
2. $F$ is a *Zariski sheaf* if for every scheme $T$ and every open cover $T = \bigcup_i T_i$, the map $F(T) \to \prod_i F(T_i)$ is injective, and its image is the set of families $(\xi_i)$ with $\xi_i|_{T_i \cap T_j} = \xi_j|_{T_i \cap T_j}$ for all $i, j$.
3. A subfunctor $G \subseteq F$ is *open* if for every scheme $T$ and every $\xi \in F(T)$ there is an open subset $T_\xi \subseteq T$ such that a morphism $g \colon T' \to T$ has $g^* \xi \in G(T')$ if and only if $g(T') \subseteq T_\xi$.
4. A family $(F_i)$ of open subfunctors is an *open cover* of $F$ if for every $T$ and $\xi \in F(T)$ the open sets $T_{\xi, i}$ cover $T$.

Lean: Mathlib `CategoryTheory.Functor.RepresentableBy` (definition) is part 1 for any category. The Zariski sheaf condition and open subfunctors of functors on schemes are not in Lean as stated.

The functor $h_X$ is a Zariski sheaf by Proposition P3.2.4, and for an open $U \subseteq X$ the subfunctor $h_U \subseteq h_X$ is open, with $T_g = g^{-1}(U)$. An open cover of $X$ gives an open cover of $h_X$.

**Theorem P3.13.24 (the representability criterion).** Let $F$ be a Zariski sheaf with an open cover $(F_i)_{i \in \Lambda}$ by subfunctors that are representable. Then $F$ is representable. If $F_i$ is represented by $X_i$, the scheme $X$ that represents $F$ has an open cover by subschemes $U_i \cong X_i$, and $U_i$ represents $F_i$.

Lean: not in Lean as stated.

Fix integers $0 \leq r \leq n$. For a scheme $T$, a *quotient of rank $r$* of $\mathcal{O}_T^n$ is a surjection $q \colon \mathcal{O}_T^n \to \mathcal{Q}$ onto a locally free sheaf of rank $r$. Two quotients $(\mathcal{Q}, q)$ and $(\mathcal{Q}', q')$ are *isomorphic* if there is an isomorphism $\psi \colon \mathcal{Q} \to \mathcal{Q}'$ with $\psi q = q'$. Such a $\psi$ is unique, since $q$ is surjective, and the quotients are isomorphic if and only if $\ker q = \ker q'$.

**Definition P3.13.25 (the Grassmannian functor).** The *Grassmannian functor* $\mathbf{G}(r, n)$ sends a scheme $T$ to the set of isomorphism classes of quotients of rank $r$ of $\mathcal{O}_T^n$, and $g \colon T' \to T$ to the pullback $(g^*\mathcal{Q}, g^* q)$. For a subset $I = \{i_1 < \dots < i_r\}$ of $\{1, \dots, n\}$ let $e_I \colon \mathcal{O}^r \to \mathcal{O}^n$ be the inclusion of the coordinates in $I$, and let $\mathbf{G}_I(T)$ be the set of quotients for which $q e_I \colon \mathcal{O}_T^r \to \mathcal{Q}$ is an isomorphism.

Lean: Mathlib `Module.Grassmannian` (definition), written `G(k, M; R)`, is the set of submodules $N$ of an $R$-module $M$ with $M/N$ locally free of rank $k$, the points of $\mathbf{G}(k, n)$ over $\operatorname{Spec} R$ for $M = R^n$ in the convention of quotients used here, and `Module.Grassmannian.functor` is the functor on commutative $R$-algebras, with base change `Module.Grassmannian.map`. The scheme that represents it is not in Lean as stated.

**Theorem P3.13.26 (the Grassmannian is a scheme).** The functor $\mathbf{G}(r, n)$ is represented by a scheme $\operatorname{Gr}(r, n)$ over $\mathbb{Z}$ with a universal quotient $\mathcal{O}^n \to \mathcal{Q}_{\mathrm{univ}}$. The subfunctors $\mathbf{G}_I$ form an open cover of $\mathbf{G}(r, n)$, and each $\mathbf{G}_I$ is represented by an open subscheme $U_I \cong \mathbb{A}^{r(n - r)}_\mathbb{Z}$: on $U_I$ the universal quotient is $\mathcal{O}^n \to \mathcal{O}^r$ given by the $r \times n$ matrix whose columns in $I$ form the identity matrix and whose other $r(n - r)$ entries are the coordinates.

Lean: not in Lean as stated.

**Theorem P3.13.27 (the Plücker embedding).** Let $N = \binom{n}{r} - 1$. The surjection $\bigwedge^r q \colon \bigwedge^r \mathcal{O}^n \cong \mathcal{O}^{N + 1} \to \bigwedge^r \mathcal{Q}_{\mathrm{univ}} = \det \mathcal{Q}_{\mathrm{univ}}$ defines a morphism $p \colon \operatorname{Gr}(r, n) \to \mathbb{P}^N_{\mathbb{Z}}$, and $p$ is a closed immersion. In homogeneous coordinates $p_J$, $J \subseteq \{1, \dots, n\}$ with $|J| = r$, a point given by an $r \times n$ matrix $M$ maps to the $r \times r$ minors $p_J = \det M_J$. For a field $k$, $\operatorname{Gr}(r, n)_k = \operatorname{Gr}(r, n) \times_\mathbb{Z} k$ is a smooth irreducible projective variety of dimension $r(n - r)$.

Lean: not in Lean as stated.

### Proof in words

A Zariski sheaf is determined by what it does on the pieces of an open cover. If the pieces of an open cover of the functor are represented by schemes, the overlaps are represented by open subschemes of these schemes, and the identity of the overlaps glues the schemes. The universal elements glue too, by the sheaf condition, and the glued scheme represents the functor because a morphism into it is the same as morphisms from the pieces of a cover.

For the Grassmannian the pieces are the quotients for which a fixed set of $r$ coordinates maps isomorphically. Using these coordinates as a basis of the quotient turns the quotient into an $r \times n$ matrix whose $I$-columns are the identity, and such a matrix is a point of affine space of dimension $r(n - r)$. The determinant of the quotient is an invertible sheaf generated by the $r \times r$ minors, which gives the Plücker map. On the chart $U_I$ the minors that differ from $I$ in one column are, up to sign, the coordinates themselves, so the map is a closed immersion.

### Examples

**Example P3.13.28 (projective space).** For $r = 1$, a quotient of rank $1$ is a surjection onto an invertible sheaf. By Theorem P3.6.34 and Example P3.6.36, $\mathbf{G}(1, n) = h_{\mathbb{P}^{n - 1}}$, so $\operatorname{Gr}(1, n) = \mathbb{P}^{n - 1}_\mathbb{Z}$, and the charts $U_{\{i\}}$ are the standard charts $D_+(x_i)$. The Plücker map is the identity. The point $[a_1 : \dots : a_n]$ of $\mathbb{P}^{n-1}(k)$ is the quotient $k^n \to k$, $e_i \mapsto a_i$, and its kernel is a hyperplane of $k^n$. In this convention a point of $\mathbb{P}^{n-1}$ is a quotient of rank $1$ of the space of linear forms, and a line of $\mathbb{P}^{n-1}$ is a quotient of rank $2$.

**Example P3.13.29 (the Klein quadric).** Let $r = 2$, $n = 4$, $N = 5$. On $U_{12}$ the universal matrix is
$$
M = \begin{pmatrix} 1 & 0 & a & b \\ 0 & 1 & c & d \end{pmatrix}, \qquad p_{12} = 1, \; p_{13} = c, \; p_{14} = d, \; p_{23} = -a, \; p_{24} = -b, \; p_{34} = ad - bc.
$$
These satisfy $p_{12} p_{34} - p_{13} p_{24} + p_{14} p_{23} = (ad - bc) + bc - ad = 0$. So $p(U_{12})$ lies in the quadric $\mathcal{Q} = V_+(p_{12} p_{34} - p_{13} p_{24} + p_{14} p_{23}) \subseteq \mathbb{P}^5_\mathbb{Z}$. On $D_+(p_{12})$ the quadric is $\operatorname{Spec} \mathbb{Z}[p_{13}, p_{14}, p_{23}, p_{24}, p_{34}]/(p_{34} - p_{13} p_{24} + p_{14} p_{23})$, a polynomial ring in $p_{13}, p_{14}, p_{23}, p_{24}$, and $p$ maps $U_{12}$ isomorphically onto it. The same computation on the other five charts shows $\operatorname{Gr}(2, 4) \cong \mathcal{Q}$, the *Klein quadric*. Over a field it is a smooth quadric of dimension $4 = 2 \cdot 2$.

**Example P3.13.30 (lines in projective space).** Let $k$ be a field and $V = S_1$ the space of linear forms in $x_0, \dots, x_n$, of dimension $n + 1$. A line $L \subseteq \mathbb{P}^n_k$ has the ideal generated by $(I_L)_1$, a subspace of codimension $2$ in $V$, and the restriction $V \to V/(I_L)_1$ is a quotient of rank $2$. Conversely a quotient $V \to Q$ of rank $2$ has a kernel $W$ of codimension $2$ and gives the line $V_+(W)$. So the lines of $\mathbb{P}^n_k$ are the points of $\operatorname{Gr}(2, n + 1)(k)$, and the lines of $\mathbb{P}^3_k$ form the Klein quadric, of dimension $4$. Over a scheme $T$, a quotient $\mathcal{O}_T^{n+1} \to \mathcal{Q}$ of rank $2$ gives the closed subscheme $\mathbb{P}(\mathcal{Q}) \subseteq \mathbb{P}(\mathcal{O}_T^{n+1}) = \mathbb{P}^n_T$, locally $\mathbb{P}^1_U$ by part 3 of Proposition P3.6.35, hence flat over $T$ with fibres lines, with Hilbert polynomial $m + 1$. This is the family of lines over the Grassmannian. Section 13.4 compares it with the Hilbert functor.

**Example P3.13.31 (a functor that is not a sheaf).** Let $F(T) = \operatorname{Pic}(T)$, the group of isomorphism classes of invertible sheaves, with pullback. On $T = \mathbb{P}^1_k$ with the cover by $D_+(x_0)$ and $D_+(x_1)$, the class of $\mathcal{O}(1)$ restricts to the trivial class on both opens, and it is not trivial (Example P3.6.16). So $F(T) \to F(T_0) \times F(T_1)$ is not injective, $F$ is not a Zariski sheaf, and $F$ is not representable. The functor of isomorphism classes of objects is rarely a sheaf, because the isomorphisms between local pieces are not part of the data. The Grassmannian avoids this: a quotient of $\mathcal{O}^n$ has no automorphisms, as the isomorphism $\psi$ is unique.

### Proof

*Proof of Theorem P3.13.24.* Let $\xi_i \in F_i(X_i)$ be the universal element of $F_i$. Apply the openness of $F_j$ to $\xi_i \in F(X_i)$: there is an open $X_{ij} \subseteq X_i$ such that $g \colon T \to X_i$ has $g^* \xi_i \in F_j(T)$ if and only if $g$ factors through $X_{ij}$. As $g^* \xi_i$ always lies in $F_i(T)$, the scheme $X_{ij}$ with the element $\xi_i|_{X_{ij}}$ represents $F_i \cap F_j$. So does $X_{ji}$ with $\xi_j|_{X_{ji}}$. There is a unique isomorphism $\varphi_{ij} \colon X_{ij} \to X_{ji}$ with $\varphi_{ij}^* (\xi_j|_{X_{ji}}) = \xi_i|_{X_{ij}}$. In the same way $X_{ij} \cap X_{ik}$ with $\xi_i$ represents $F_i \cap F_j \cap F_k$, so $\varphi_{ij}$ maps $X_{ij} \cap X_{ik}$ onto $X_{ji} \cap X_{jk}$, and $\varphi_{jk} \varphi_{ij}$ and $\varphi_{ik}$ both pull $\xi_k$ back to $\xi_i$ on $X_{ij} \cap X_{ik}$, so they agree by the uniqueness in part 1 of Definition P3.13.23. These are the conditions of Theorem P3.2.3, which glues the $X_i$ to a scheme $X$ with open subschemes $U_i \cong X_i$ and $U_i \cap U_j = X_{ij}$. By construction $\xi_i$ and $\xi_j$ agree on $U_i \cap U_j$, so by the sheaf condition there is a unique $\xi \in F(X)$ with $\xi|_{U_i} = \xi_i$.

First, a morphism $g \colon T \to X$ has $g^* \xi \in F_i(T)$ if and only if $g(T) \subseteq U_i$. If $g(T) \subseteq U_i$, then $g^* \xi$ is a pullback of $\xi_i \in F_i(X_i)$. Conversely let $g^* \xi \in F_i(T)$, and put $T_j = g^{-1}(U_j)$. The restriction $g_j \colon T_j \to U_j \cong X_j$ pulls $\xi_j$ back to $(g^* \xi)|_{T_j}$, which lies in $F_i(T_j)$, so $g_j$ factors through $X_{ji} = U_j \cap U_i$. As the $T_j$ cover $T$, $g(T) \subseteq U_i$.

Now let $T$ be a scheme. The map $h_X(T) \to F(T)$ is injective: let $g, g' \colon T \to X$ with $g^* \xi = g'^* \xi = \eta$. By the first step $g^{-1}(U_i) = g'^{-1}(U_i) = T_{\eta, i}$ for every $i$, and on $T_{\eta, i}$ both $g$ and $g'$ are morphisms to $U_i \cong X_i$ that pull $\xi_i$ back to $\eta|_{T_{\eta, i}}$. As $X_i$ represents $F_i$, they agree on $T_{\eta, i}$, and these opens cover $T$, so $g = g'$. The map is surjective: let $\eta \in F(T)$. The opens $T_i = T_{\eta, i}$ cover $T$, and $\eta|_{T_i} \in F_i(T_i)$ is $g_i^* \xi_i$ for a unique $g_i \colon T_i \to X_i = U_i$. On $T_i \cap T_j$, $g_i$ and $g_j$ both pull $\xi$ back to $\eta|_{T_i \cap T_j}$, so they agree by injectivity for $T_i \cap T_j$. By Proposition P3.2.4 they glue to $g \colon T \to X$, and $g^* \xi = \eta$ since both restrict to $\eta|_{T_i}$ on each $T_i$ and $F$ is a sheaf. $\square$

*Proof of Theorem P3.13.26.* The functor $\mathbf{G}(r, n)$ is well defined. For $g \colon T' \to T$ and $t' \in T'$, the stalk of $g^* \mathcal{Q}$ at $t'$ is $\mathcal{Q}_{g(t')} \otimes \mathcal{O}_{T', t'}$, and tensor products are right exact, so $g^* q$ is surjective. By part 1 of Proposition P3.5.32, $g^* \mathcal{Q}$ is locally free of rank $r$.

It is a Zariski sheaf. A quotient is determined up to isomorphism by its kernel $\mathcal{K} \subseteq \mathcal{O}_T^n$. Let $T = \bigcup T_i$ and let $\mathcal{K}_i \subseteq \mathcal{O}_{T_i}^n$ be kernels of quotients of rank $r$ with $\mathcal{K}_i = \mathcal{K}_j$ on $T_i \cap T_j$. The sections $s$ of $\mathcal{O}^n$ over $V$ with $s|_{V \cap T_i} \in \mathcal{K}_i(V \cap T_i)$ for all $i$ form a subsheaf $\mathcal{K}$, the only one that restricts to $\mathcal{K}_i$ on each $T_i$. The quotient $\mathcal{O}_T^n/\mathcal{K}$ restricts to $\mathcal{O}_{T_i}^n/\mathcal{K}_i$ on $T_i$, so it is locally free of rank $r$.

Each $\mathbf{G}_I$ is open. Let $\xi = (\mathcal{Q}, q) \in \mathbf{G}(r, n)(T)$ and $\varphi = q e_I \colon \mathcal{O}_T^r \to \mathcal{Q}$. Let $T_\xi$ be the set of $t$ where $\varphi \otimes \kappa(t)$ is an isomorphism. On an open $V$ where $\mathcal{Q} \cong \mathcal{O}_V^r$, $\varphi$ is an $r \times r$ matrix $\Phi$ over $\mathcal{O}(V)$, and $T_\xi \cap V$ is the open set where $\det \Phi$ does not vanish. So $T_\xi$ is open. A map of free modules of rank $r$ is an isomorphism if and only if its determinant is a unit, and a function that vanishes at no point is a unit. So for $g \colon T' \to T$, $g^* \varphi$ is an isomorphism if and only if $(g^*\varphi) \otimes \kappa(t') = (\varphi \otimes \kappa(g(t'))) \otimes_{\kappa(g(t'))} \kappa(t')$ is an isomorphism for every $t'$, if and only if $g(T') \subseteq T_\xi$. The $\mathbf{G}_I$ cover $\mathbf{G}(r, n)$: at a point $t$, $\mathcal{Q} \otimes \kappa(t)$ is a quotient of dimension $r$ of $\kappa(t)^n$, so the images of some $r$ basis vectors $e_i$, $i \in I$, form a basis, and $t \in T_{\xi, I}$.

Each $\mathbf{G}_I$ is representable. For $\xi = (\mathcal{Q}, q) \in \mathbf{G}_I(T)$, the map $\varphi^{-1} q \colon \mathcal{O}_T^n \to \mathcal{O}_T^r$ is an $r \times n$ matrix $M(\xi)$ over $\Gamma(T, \mathcal{O}_T)$ with $M(\xi)_I = 1$, where $M_I$ is the square submatrix of the columns in $I$. An isomorphism $\psi \colon (\mathcal{Q}, q) \to (\mathcal{Q}', q')$ has $q' e_I = \psi q e_I$, so $M(\xi') = (\psi \varphi)^{-1} \psi q = M(\xi)$. Conversely every $r \times n$ matrix $M$ with $M_I = 1$ is surjective as a map $\mathcal{O}_T^n \to \mathcal{O}_T^r$ and gives the element $(\mathcal{O}_T^r, M)$ of $\mathbf{G}_I(T)$, with $M(\mathcal{O}_T^r, M) = M$; and $\xi$ is isomorphic to $(\mathcal{O}_T^r, M(\xi))$ through $\varphi^{-1}$. So $\mathbf{G}_I(T)$ is the set of these matrices, which is $\Gamma(T, \mathcal{O}_T)^{r(n - r)} = \mathbb{A}^{r(n-r)}_\mathbb{Z}(T)$ by Example P3.2.36, naturally in $T$. The universal element on $U_I = \mathbb{A}^{r(n - r)}_\mathbb{Z}$ is the matrix of coordinates. Theorem P3.13.24 gives $\operatorname{Gr}(r, n)$. $\square$

*Proof of Theorem P3.13.27.* Let $\mathcal{L} = \det \mathcal{Q}_{\mathrm{univ}}$, an invertible sheaf, and for $|J| = r$ let $s_J \in \Gamma(\operatorname{Gr}(r, n), \mathcal{L})$ be the image of $e_{j_1} \wedge \dots \wedge e_{j_r}$ under $\bigwedge^r q$. Locally, where $\mathcal{Q}_{\mathrm{univ}} \cong \mathcal{O}^r$ and $q$ is a matrix $M$, $s_J$ is $\det M_J$. At a point $t$, $s_J$ generates $\mathcal{L} \otimes \kappa(t)$ if and only if $\det M_J(t) \neq 0$, that is, if and only if $t \in U_J$. As the $U_J$ cover, the $s_J$ generate $\mathcal{L}$, and part 2 of Theorem P3.6.21 (over $A = \mathbb{Z}$) gives $p$ with $p^* x_J = s_J$. The open set $\operatorname{Gr}(r, n)_{s_J}$ where $s_J$ generates is $U_J$, which is affine.

On $U_I$, trivialize $\mathcal{Q}_{\mathrm{univ}}$ by $q e_I$, so that $q$ is the matrix $M$ of coordinates $a_{kl}$, $1 \leq k \leq r$ and $l \notin I$, with $M_I = 1$ and $s_I = 1$. The ring map of part 4 of Theorem P3.6.21 is $\mathbb{Z}[y_J] \to \mathbb{Z}[a_{kl}]$, $y_J \mapsto s_J/s_I = \det M_J$. Let $J = (I \setminus \{i_k\}) \cup \{l\}$ with $l \notin I$. Then $M_J$ is the identity matrix with its $k$-th column replaced by the column $l$ of $M$, put in increasing order of indices, so $\det M_J = \pm a_{kl}$. So every coordinate lies in the image, the ring map is surjective, and $p$ is a closed immersion by part 4 of Theorem P3.6.21. On points, a quotient given by $M$ maps to the generator of $\mathcal{L}$ with coordinates $\det M_J$.

Let $k$ be a field. By base change $\operatorname{Gr}(r, n)_k$ is a closed subscheme of $\mathbb{P}^N_k$, hence projective, and it is covered by the opens $(U_I)_k \cong \mathbb{A}^{r(n-r)}_k$, which are smooth and irreducible of dimension $r(n - r)$ (Example P3.7.16). The open $(U_I)_k \cap (U_J)_k$ is the subset of $(U_I)_k$ where $\det M_J \neq 0$. Up to sign, $\det M_J$ is the determinant of the square matrix of distinct coordinates $a_{kl}$ with $i_k \notin J$ and $l \in J \setminus I$, a nonzero polynomial, so $(U_I)_k \cap (U_J)_k \neq \emptyset$. A nonempty open subset of an irreducible space is dense, so $\overline{(U_I)_k}$ contains every $(U_J)_k$, and $\operatorname{Gr}(r, n)_k$ is the closure of the irreducible set $(U_I)_k$, hence irreducible. It is reduced, since it is covered by reduced opens, so it is an integral scheme, smooth of dimension $r(n - r)$. $\square$

### Exercises

1. (A) For $r = 1$, write the matrices of Theorem P3.13.26 and check that $U_{\{i\}} \cap U_{\{j\}}$ is the open where the coordinate in column $j$ is invertible, with the gluing maps of $\mathbb{P}^{n-1}$ (Definition P3.2.10).
2. (A) Show that $\operatorname{Gr}(r, n)(k)$, for a field $k$, is the set of subspaces of codimension $r$ of $k^n$, and that $\operatorname{Gr}(n, n) = \operatorname{Spec} \mathbb{Z}$ and $\operatorname{Gr}(0, n) = \operatorname{Spec} \mathbb{Z}$.
3. (B) Show that the kernel of a quotient of rank $r$ of $\mathcal{O}_T^n$ is locally free of rank $n - r$, and that dualizing $0 \to \mathcal{K} \to \mathcal{O}^n \to \mathcal{Q} \to 0$ gives an isomorphism $\operatorname{Gr}(r, n) \cong \operatorname{Gr}(n - r, n)$.
4. (B) Show that the image of $\operatorname{Gr}(2, n)$ in $\mathbb{P}^N$ lies in the quadrics $p_{ij} p_{kl} - p_{ik} p_{jl} + p_{il} p_{jk}$ for $i < j < k < l$. (Expand the determinant of the $4 \times 4$ matrix of the columns $i, j, k, l$ of $M$ stacked on itself.)
5. (B) Let $\mathcal{E}$ be locally free of rank $n$ on a scheme $Y$. Define the functor of quotients of rank $r$ of $\mathcal{E}$ on $Y$-schemes, and show that it is represented by a $Y$-scheme $\operatorname{Gr}(r, \mathcal{E})$ that is locally $\operatorname{Gr}(r, n) \times U$ over opens $U$ where $\mathcal{E}$ is free. For $r = 1$ it is $\mathbb{P}(\mathcal{E})$.
6. (C) Let $k$ be a field and $x \in \operatorname{Gr}(r, n)(k)$ the quotient $k^n \to Q$ with kernel $K$. Using Proposition P3.7.13, show that the tangent space of $\operatorname{Gr}(r, n)_k$ at $x$ is $\operatorname{Hom}_k(K, Q)$, of dimension $r(n - r)$.

### Lean

Mathlib has `Module.Grassmannian` as a set of submodules with locally free quotient of rank $k$, which is the convention of quotients used in Definition P3.13.25, and `Module.Grassmannian.functor`, the functor $\mathbf{G}(k, M)$ on commutative $R$-algebras with base change `Module.Grassmannian.map`. The comments of the Mathlib file explain that this convention is chosen so that the functor is representable. The representing scheme, the charts $U_I$ and the Plücker embedding are not in Lean as stated. `CategoryTheory.Functor.RepresentableBy` is part 1 of Definition P3.13.23 in any category. mmp-lean does not use the Grassmannian, and the handbook adds no `MinimalModel` node here.

### Notes and history

The Grassmannian goes back to Grassmann's *Ausdehnungslehre* (1844) and the coordinates to Plücker, who described the lines of space by the six coordinates $p_{ij}$ in the 1860s; Klein's dissertation (1868) studies the quadric they satisfy. The functorial construction is Grothendieck's, from his Séminaire Bourbaki talk on Hilbert schemes (1961) and the second edition of EGA I (1971). Theorem P3.13.24 is in the Stacks Project, in the chapter on schemes (functors and Zariski sheaves), and Vakil uses it to construct the Grassmannian; the proof here follows these. The literature state is theorem.

The Grassmannian is the first moduli space of the handbook defined by its functor. The same pattern, an open cover of the functor by representable pieces, glued by the representability criterion, constructs the Hilbert scheme: Grothendieck embeds $\operatorname{Hilb}^P$ in a Grassmannian of quotients of $\Gamma(\mathbb{P}^n, \mathcal{O}(m))$ for large $m$, a black box of P8 Ch. 1.
