---
title: Serre's criterion, flat base change and affine morphisms
nodes: []
sources: [Har77, Vak25, GW23, EGA1, Stacks]
reads_with: [Har77:III.3, Har77:III.9, Vak25:ch18]
requires: [P1.2, P2.7, P3.3, P3.4, P3.5, P4.1]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Serre's criterion, flat base change and affine morphisms

### Statement

Section 1.2 proved that a quasi-coherent sheaf on an affine scheme has no higher cohomology. The first theorem is the converse for Noetherian schemes: the vanishing of $H^1$ for coherent ideal sheaves alone forces the scheme to be affine. The other three results of the section are consequences of the comparison with Čech cohomology, Corollary P4.1.9.

**Theorem P4.1.16 (Serre's criterion for affineness).** Let $X$ be a Noetherian scheme. The following are equivalent:

1. $X$ is affine;
2. $H^p(X, \mathcal{F}) = 0$ for every quasi-coherent $\mathcal{F}$ and every $p > 0$;
3. $H^1(X, \mathcal{I}) = 0$ for every coherent sheaf of ideals $\mathcal{I} \subseteq \mathcal{O}_X$.

Lean: not in Lean as stated. Mathlib proves the affineness criterion of Theorem P3.3.4 as `AlgebraicGeometry.isAffine_of_isAffineOpen_basicOpen`, which is the last step of the proof.

**Theorem P4.1.17 (flat base change over an affine base).** Let $A$ be a ring, $X$ a quasi-compact separated scheme over $A$, and $\mathcal{F}$ a quasi-coherent sheaf on $X$. Let $A \to B$ be a ring map, $X_B = X \times_{\operatorname{Spec} A} \operatorname{Spec} B$ and $g \colon X_B \to X$ the projection. There are natural maps
$$H^p(X, \mathcal{F}) \otimes_A B \to H^p(X_B, g^* \mathcal{F}),$$
and they are isomorphisms for all $p$ if $B$ is flat over $A$.

Lean: not in Lean as stated.

**Proposition P4.1.18 (direct sums).** Let $X$ be a quasi-compact separated scheme and $(\mathcal{F}_i)_{i \in I}$ a family of quasi-coherent sheaves. Then the natural map $\bigoplus_i H^p(X, \mathcal{F}_i) \to H^p(X, \bigoplus_i \mathcal{F}_i)$ is an isomorphism for every $p$.

Lean: not in Lean as stated.

**Proposition P4.1.19 (affine morphisms).** Let $f \colon X \to Y$ be an affine morphism with $Y$ separated, and $\mathcal{F}$ a quasi-coherent sheaf on $X$. Then $H^p(X, \mathcal{F}) \cong H^p(Y, f_* \mathcal{F})$ for every $p$. In particular this holds for a closed immersion $f$.

Lean: not in Lean as stated.

For a closed immersion Proposition P4.1.19 also follows from Proposition P2.7.4, which needs no hypothesis on $Y$ or on $\mathcal{F}$. Chapter 4 proves that $R^p f_* \mathcal{F} = 0$ for $p > 0$ when $f$ is affine, and so removes the separatedness of $Y$ by the Leray spectral sequence.

### Proof in words

For Serre's criterion, the affineness criterion of Theorem P3.3.4 asks for global functions $f_1, \dots, f_r$ that generate the unit ideal and have affine nonvanishing loci $X_{f_i}$. The functions come from the vanishing of $H^1$. To find a function that is $1$ at a closed point $P$ and vanishes outside an affine neighbourhood $U$ of $P$, compare the ideal sheaf of $Y = X \setminus U$ with that of $Y \cup \{P\}$. Their quotient is the skyscraper $\kappa(P)$, and the vanishing of $H^1$ of the smaller ideal lifts $1 \in \kappa(P)$ to a global section. To show that finitely many such functions generate the unit ideal, write $\sum a_i f_i = 1$ as the surjectivity on global sections of $\mathcal{O}_X^r \to \mathcal{O}_X$, and kill the obstruction, the $H^1$ of the kernel, by filtering the kernel by ideal sheaves.

The other results are statements about Čech complexes. Over an affine base, base change sends the Čech complex of an affine cover to its tensor product with $B$, and a flat module commutes with taking cohomology. Direct sums commute with sections over affine open sets and with finite products. An affine morphism sends an affine cover of $Y$ to an affine cover of $X$ with the same Čech complex.

### Examples

**Example P4.1.20 (extension of the base field).** Let $X$ be a separated scheme of finite type over a field $k$, $\mathcal{F}$ quasi-coherent, and $K \supseteq k$ a field extension. Every $k$-vector space is flat, so Theorem P4.1.17 gives $H^p(X_K, \mathcal{F}_K) \cong H^p(X, \mathcal{F}) \otimes_k K$ and $\dim_K H^p(X_K, \mathcal{F}_K) = \dim_k H^p(X, \mathcal{F})$. For instance $H^1(\mathbb{P}^1_K, \mathcal{O}(-2)) \cong K$, as Example P2.7.23 computes directly. Numerical invariants such as the genus of a curve, $\dim_k H^1(X, \mathcal{O}_X)$, can therefore be computed after passing to an algebraic closure.

**Example P4.1.21 (base change that is not flat).** Let $A = k[x]$ and let $X = \mathbb{A}^2_k \setminus \{0\}$, the punctured plane of Example P4.1.12, mapped to $\operatorname{Spec} A$ by the first coordinate. It is quasi-compact and separated. Let $B = A/(x) = k$, which is not flat over $A$. The fibre $X_B$ is the line $\{x = 0\}$ with the origin removed, $\operatorname{Spec} k[y, y^{-1}]$. Then
$$H^0(X, \mathcal{O}_X) \otimes_A B = k[x, y]/(x) = k[y], \qquad H^0(X_B, \mathcal{O}_{X_B}) = k[y, y^{-1}],$$
so the map of Theorem P4.1.17 is not surjective for $p = 0$. The section $y^{-1}$ of the fibre does not extend to $X$. In degree $1$, $H^1(X, \mathcal{O}_X) \otimes_A B = 0$, since multiplication by $x$ is surjective on the span of the $x^{-i} y^{-j}$, $i, j \geq 1$, while $H^1(X_B, \mathcal{O}_{X_B}) = 0$ because $X_B$ is affine. Chapter 5 studies when base change to a fibre works without flatness.

**Example P4.1.22 (closed subschemes of projective space).** Let $Z \subseteq \mathbb{P}^n_A$ be a closed subscheme with closed immersion $i$ and $\mathcal{G}$ a quasi-coherent sheaf on $Z$. The scheme $\mathbb{P}^n_A$ is separated, so Proposition P4.1.19 gives $H^p(Z, \mathcal{G}) = H^p(\mathbb{P}^n_A, i_* \mathcal{G})$, and $i_* \mathcal{G}$ is quasi-coherent by part 2 of Theorem P3.5.33. This is how Chapter 2 computes the cohomology of coherent sheaves on projective schemes: it moves them to projective space and resolves them there by sums of the sheaves $\mathcal{O}(m)$.

### Proof

*Theorem P4.1.16.* (1) implies (2) by Theorem P4.1.8, and (2) implies (3) since a coherent sheaf is quasi-coherent. Assume (3), and let $B = \Gamma(X, \mathcal{O}_X)$.

*Step 1: closed points have affine neighbourhoods of the form $X_f$.* Let $P \in X$ be a closed point and $U$ an affine open neighbourhood of $P$. Let $Y = X \setminus U$, a closed set, and give $Y$ and $Y \cup \{P\}$ their reduced induced structures (Proposition P3.3.12). Their ideal sheaves $\mathcal{I}_{Y \cup \{P\}} \subseteq \mathcal{I}_Y$ are quasi-coherent, hence coherent since $X$ is Noetherian. On $X \setminus \{P\}$ the two ideals agree, since both are the ideal of the functions that vanish on $Y \setminus \{P\} = Y$. On $U$, $\mathcal{I}_Y|_U = \mathcal{O}_U$ and $\mathcal{I}_{Y \cup \{P\}}|_U$ is the ideal of the closed point $P$, whose quotient is $\kappa(P)$ (Example P3.3.13). So there is an exact sequence
$$0 \to \mathcal{I}_{Y \cup \{P\}} \to \mathcal{I}_Y \to \kappa(P) \to 0,$$
where $\kappa(P)$ is the skyscraper sheaf at $P$. By (3), $H^1(X, \mathcal{I}_{Y \cup \{P\}}) = 0$, so $\Gamma(X, \mathcal{I}_Y) \to \kappa(P)$ is surjective. Choose $f \in \Gamma(X, \mathcal{I}_Y) \subseteq B$ that maps to $1$. Then $f(P) = 1 \neq 0$, so $P \in X_f$. For $y \in Y$ the germ $f_y$ lies in $(\mathcal{I}_Y)_y \subseteq \mathfrak{m}_y$, so $f(y) = 0$ and $X_f \subseteq U$. So $X_f$ is the locus in $U = \operatorname{Spec} C$ where the restriction $\bar f \in C$ does not vanish, which is the basic open set $D(\bar f)$, affine by Proposition P3.1.13.

*Step 2: finitely many such sets cover $X$.* Let $Z$ be the complement of the union of the open sets $X_f$ of Step 1, for all closed points $P$. Suppose $Z \neq \emptyset$. The space $X$ is Noetherian, so $Z$ contains a minimal nonempty closed subset $Z'$, and every point $z \in Z'$ has closure $Z'$. Let $V$ be an affine open set that meets $Z'$. Then $Z' \cap V$ is a nonempty closed subset of an affine scheme, so it contains a closed point $w$ of $V$. The closure of $w$ in $X$ is $Z'$, and every $z \in Z'$ has $w$ in its closure, so $z$ lies in every open set that contains $w$, in particular in $V$. So $Z' \subseteq V$, and $Z' = \{w\}$ since $w$ is closed in $V$. Then $w$ is a closed point of $X$ in $Z$, which contradicts Step 1. So the sets $X_f$ cover $X$. A Noetherian space is quasi-compact, so finitely many of them, $X_{f_1}, \dots, X_{f_r}$, cover $X$.

*Step 3: $f_1, \dots, f_r$ generate the unit ideal of $B$.* Let $\alpha \colon \mathcal{O}_X^r \to \mathcal{O}_X$ be $(a_1, \dots, a_r) \mapsto \sum_i f_i a_i$. It is surjective: at a point $x$ some $f_i$ is a unit of $\mathcal{O}_{X, x}$, since $x \in X_{f_i}$. Its kernel $\mathcal{K}$ is coherent (part 1 of Theorem P3.5.20, and finite type because $X$ is Noetherian). Let $\mathcal{K}_i = \mathcal{K} \cap \mathcal{O}_X^i$, where $\mathcal{O}_X^i \subseteq \mathcal{O}_X^r$ is the sum of the first $i$ factors. Then $0 = \mathcal{K}_0 \subseteq \mathcal{K}_1 \subseteq \cdots \subseteq \mathcal{K}_r = \mathcal{K}$, and $\mathcal{K}_i / \mathcal{K}_{i-1}$ maps injectively to $\mathcal{O}_X^i / \mathcal{O}_X^{i-1} \cong \mathcal{O}_X$, the projection to the $i$-th coordinate. So $\mathcal{K}_i/\mathcal{K}_{i-1}$ is isomorphic to a coherent sheaf of ideals, and its $H^1$ vanishes by (3). The long exact sequences of $0 \to \mathcal{K}_{i-1} \to \mathcal{K}_i \to \mathcal{K}_i/\mathcal{K}_{i-1} \to 0$ give $H^1(X, \mathcal{K}_i) = 0$ by induction on $i$. So $H^1(X, \mathcal{K}) = 0$, and the long exact sequence of $0 \to \mathcal{K} \to \mathcal{O}_X^r \to \mathcal{O}_X \to 0$ shows that $B^r \to B$ is surjective. So $1 = \sum_i a_i f_i$ with $a_i \in B$.

*Step 4.* The $f_i \in B$ generate the unit ideal and each $X_{f_i}$ is affine. By Theorem P3.3.4, $X$ is affine. $\square$

*Theorem P4.1.17.* Let $\mathcal{U} = (U_1, \dots, U_r)$ be a finite cover of $X$ by affine open sets. Since $X$ is separated, every finite intersection $U_J = U_{j_0 \cdots j_p}$ is affine, say $U_J = \operatorname{Spec} C_J$ (Proposition P3.4.12). The open sets $g^{-1}(U_J) = U_J \times_{\operatorname{Spec} A} \operatorname{Spec} B = \operatorname{Spec}(C_J \otimes_A B)$ are affine (Proposition P3.3.19), and they are the finite intersections of the cover $g^{-1}\mathcal{U} = (g^{-1}(U_i))$ of $X_B$. By part 2 of Proposition P3.5.32,
$$(g^* \mathcal{F})(g^{-1}(U_J)) = \mathcal{F}(U_J) \otimes_{C_J} (C_J \otimes_A B) = \mathcal{F}(U_J) \otimes_A B,$$
compatibly with the restriction maps. A finite product commutes with $- \otimes_A B$, so $\check{C}^\bullet(g^{-1}\mathcal{U}, g^* \mathcal{F}) = \check{C}^\bullet(\mathcal{U}, \mathcal{F}) \otimes_A B$. By Corollary P4.1.9, applied on $X$ and on $X_B$, the cohomology of the left side is $H^p(X_B, g^* \mathcal{F})$ and that of $\check{C}^\bullet(\mathcal{U}, \mathcal{F})$ is $H^p(X, \mathcal{F})$. For any complex $C^\bullet$ of $A$-modules there is a natural map $H^p(C^\bullet) \otimes_A B \to H^p(C^\bullet \otimes_A B)$, $[z] \otimes b \mapsto [z \otimes b]$. If $B$ is flat, $- \otimes_A B$ is exact, so it preserves the kernel and the image of each differential, and the map is an isomorphism. The maps do not depend on the cover, since a common refinement by affine open sets induces compatible maps of Čech complexes. $\square$

*Proposition P4.1.18.* The sum $\mathcal{F} = \bigoplus_i \mathcal{F}_i$ is quasi-coherent by part 2 of Theorem P3.5.20. Let $V$ be an affine open set, $V = \operatorname{Spec} C$, with $\mathcal{F}_i|_V \cong (M_i)^\sim$ (Theorem P3.5.12). By part 3 of Proposition P3.5.1, $\mathcal{F}|_V \cong (\bigoplus_i M_i)^\sim$, so $\mathcal{F}(V) = \bigoplus_i \mathcal{F}_i(V)$ by Corollary P3.1.5. Let $\mathcal{U}$ be a finite cover of $X$ by affine open sets. Its finite intersections are affine, so $\check{C}^\bullet(\mathcal{U}, \mathcal{F}) = \bigoplus_i \check{C}^\bullet(\mathcal{U}, \mathcal{F}_i)$, since finite products commute with direct sums. Cohomology of complexes commutes with direct sums, and Corollary P4.1.9 identifies both sides with sheaf cohomology. $\square$

*Proposition P4.1.19.* The sheaf $f_* \mathcal{F}$ is quasi-coherent by part 2 of Theorem P3.5.33. Let $(V_j)$ be a cover of $Y$ by affine open sets. Every finite intersection $V_J$ is affine since $Y$ is separated, and $f^{-1}(V_J)$ is affine since $f$ is affine (Proposition P3.3.30). So the cover $(f^{-1}(V_j))$ of $X$ has affine finite intersections $f^{-1}(V_J)$, and
$$\check{C}^\bullet((V_j), f_* \mathcal{F}) = \check{C}^\bullet((f^{-1}(V_j)), \mathcal{F}),$$
term by term, since $(f_* \mathcal{F})(V_J) = \mathcal{F}(f^{-1}(V_J))$. Corollary P4.1.9 on $Y$ and on $X$ identifies the two sides with $H^p(Y, f_* \mathcal{F})$ and $H^p(X, \mathcal{F})$. A closed immersion is affine, since the preimage of an affine open set $\operatorname{Spec} C$ is $\operatorname{Spec} C/I$. $\square$

### Exercises

1. (A) Let $X$ be a Noetherian scheme. Show that $X$ is affine if and only if $X_{\mathrm{red}}$ is affine. (For a coherent $\mathcal{F}$, filter it by $\mathcal{N}^k \mathcal{F}$, where $\mathcal{N}$ is the nilradical, and note that each quotient is a sheaf on $X_{\mathrm{red}}$.)
2. (A) Show that a closed subscheme of a Noetherian affine scheme is affine, using Theorem P4.1.16 and Proposition P4.1.19.
3. (A) Show that Theorem P4.1.17 holds for $B = A_g$ with $g \in A$, and that it then says $H^p(X_g, \mathcal{F}) = H^p(X, \mathcal{F})_g$ for $X_g$ the preimage of $D(g)$. Compare with Lemma P3.5.11 for $p = 0$.
4. (B) Let $X$ be a Noetherian scheme. Show that $X$ is affine if and only if every irreducible component of $X$, with its reduced induced structure, is affine. (Use Exercise 1 and induction on the number of components.)
5. (B) Let $X$ be a quasi-compact separated scheme over a ring $A$ and $\mathcal{F}$ quasi-coherent. Show that $H^p(X, \mathcal{F})$ commutes with filtered colimits of quasi-coherent sheaves.
6. (B) In the setting of Theorem P4.1.17, show that for every $B$ the map is an isomorphism for the top degree $p = r - 1$, where $r$ is the number of affine pieces of a cover. (Right exactness of the tensor product.)
7. (B) Let $X$ be a Noetherian separated scheme covered by two affine open sets $U$ and $V$. Show that $X$ is affine if and only if $\mathcal{I}(U) \oplus \mathcal{I}(V) \to \mathcal{I}(U \cap V)$, $(a, b) \mapsto b - a$, is surjective for every coherent sheaf of ideals $\mathcal{I}$. Check the condition fails for $\mathbb{P}^1_k$ and $\mathcal{I} = \mathcal{O}(-2)$, viewed as the ideal sheaf of two points.
8. (C) Let $f \colon X \to Y$ be a morphism of Noetherian separated schemes. Show that $f$ is affine if and only if $R^p f_* \mathcal{F}$, defined in P2 Ch. 7, is $0$ for every quasi-coherent $\mathcal{F}$ and every $p > 0$. (Use part 4 of Theorem P2.7.3 and Theorem P4.1.16 on the preimages of affine open sets.)

### Lean

Mathlib proves the affineness criterion `AlgebraicGeometry.isAffine_of_isAffineOpen_basicOpen` and has fibre products of schemes and the pullback of sheaves of modules. Serre's criterion for affineness, flat base change for cohomology, the commutation with direct sums and the comparison along affine morphisms are not in Lean as stated. The handbook adds no `MinimalModel` node here.

### Notes and history

Theorem P4.1.16 is Serre's, from *Sur la cohomologie des variétés algébriques* (1957), and the proof is Hartshorne, Theorem III.3.7. EGA II, Théorème 5.2.1, proves it for quasi-compact quasi-separated schemes, in the form: $X$ is affine if $H^1(X, \mathcal{F}) = 0$ for every quasi-coherent $\mathcal{F}$. Flat base change is Hartshorne, Proposition III.9.3, where it is stated for higher direct images; Chapter 5 returns to it in that form. The literature state is theorem. In the minimal model program flat base change is the reason why cohomological statements, such as the vanishing theorems of Volume 5, can be checked after extending the base field, and Proposition P4.1.19 is used, often without comment, to compute cohomology on a closed subvariety in the ambient space.
