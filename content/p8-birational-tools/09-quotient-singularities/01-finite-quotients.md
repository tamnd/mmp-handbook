---
title: Quotients by finite groups
nodes: []
sources: [KM98, Rei87]
reads_with: [Rei87:ch4, KM98:5.2]
requires: [P1.4, P1.13, P3.9, P8.6]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Quotients by finite groups

### Statement

Throughout this chapter $k$ is algebraically closed and $G$ is a finite group whose order is invertible in $k$. A group acting on a variety acts on its functions by $(g \cdot a)(v) = a(g^{-1} v)$.

**Definition P8.9.1 (actions and quotients).** Let $V = \operatorname{Spec} A$ be an affine variety with an action of $G$ by automorphisms. The *ring of invariants* is $A^G = \{ a \in A : g \cdot a = a \text{ for all } g \in G \}$, the *quotient* is $V/G = \operatorname{Spec} A^G$, and the *quotient map* $\pi \colon V \to V/G$ is the morphism given by the inclusion $A^G \subseteq A$. The *stabiliser* of $v \in V$ is $G_v = \{ g \in G : g v = v \}$, and the action is *free* at $v$ if $G_v = \{ 1 \}$.

**Lemma P8.9.2 (the Reynolds operator).** The map $R \colon A \to A^G$, $R(a) = \frac{1}{|G|} \sum_{g \in G} g \cdot a$, is $A^G$-linear and is the identity on $A^G$. So $A^G$ is a direct summand of $A$ as an $A^G$-module, and $IA \cap A^G = I$ for every ideal $I$ of $A^G$. More generally, for every $A^G$-module $P$ the functor of invariants commutes with $- \otimes_{A^G} P$ on modules with a $G$-action, when $P$ is flat.

Lean: not in Lean as stated.

**Theorem P8.9.3 (the quotient of an affine variety).** Let $G$ act on the affine variety $V = \operatorname{Spec} A$, and put $X = V/G$.

1. $A^G$ is a finitely generated $k$-algebra and $A$ is a finite $A^G$-module, so $X$ is an affine variety and $\pi$ is finite and surjective.
2. The fibres of $\pi$ are exactly the orbits of $G$ on the closed points of $V$.
3. Every $G$-invariant morphism $V \to Z$ to an affine variety factors uniquely through $\pi$.
4. If $A$ is a normal domain then so is $A^G$, and $\dim X = \dim V$. If in addition $G$ acts faithfully, then $k(X) = k(V)^G$ and $k(V) / k(X)$ is a Galois extension with group $G$.

Lean: not in Lean as stated.

**Proposition P8.9.4 (quotients of factorial varieties).** Let $G$ act on $V = \operatorname{Spec} A$ with $A$ a unique factorization domain, for instance $V = \mathbb{A}^n$. Then $|G| \cdot D$ is principal for every Weil divisor $D$ on $X = V/G$. So $\operatorname{Cl}(X)$ is a torsion group killed by $|G|$, and $X$ is $\mathbb{Q}$-factorial.

Lean: not in Lean as stated.

**Proposition P8.9.5 (completions of quotients).** Let $G$ act on $V = \operatorname{Spec} A$, let $v \in V$ be a closed point with stabiliser $H = G_v$, and $x = \pi(v)$. Then $H$ acts on $\widehat{\mathcal{O}}_{V, v}$ and
$$\widehat{\mathcal{O}}_{X, x} \cong \left( \widehat{\mathcal{O}}_{V, v} \right)^H.$$
In particular, if the action is free at $v$, then $\pi$ is étale at $v$.

Lean: not in Lean as stated.

**Proposition P8.9.6 (Cartan's linearization).** Let $H$ act on a variety $V$ fixing a smooth point $v$, with $n = \dim V$. Then $H$ acts linearly on the cotangent space $\mathfrak{m}_v / \mathfrak{m}_v^2$, and there are a regular system of parameters $x_1, \dots, x_n$ of $\mathcal{O}_{V, v}$ spanning an $H$-stable subspace of $\mathfrak{m}_v$ that maps isomorphically to $\mathfrak{m}_v / \mathfrak{m}_v^2$, and an $H$-equivariant isomorphism $k[[x_1, \dots, x_n]] \cong \widehat{\mathcal{O}}_{V, v}$, where $H$ acts on the power series ring through its linear action on $x_1, \dots, x_n$.

Lean: not in Lean as stated.

**Definition P8.9.7 (quotient singularities).** A closed point $x$ of a normal variety $X$ of dimension $n$ is a *quotient singularity* if there are a finite subgroup $G \subseteq GL_n(k)$, with $|G|$ invertible in $k$, and an isomorphism $\widehat{\mathcal{O}}_{X, x} \cong \widehat{\mathcal{O}}_{\mathbb{A}^n / G, 0}$, where $0$ also denotes the image of the origin. By Propositions P8.9.5 and P8.9.6, every closed point of $V/G$ with $V$ smooth is a quotient singularity, with $G$ replaced by the stabiliser of a point above it acting on the tangent space.

### Proof in words

Every element of $A$ is a root of the monic polynomial $\prod_g (t - g \cdot a)$, whose coefficients are invariant, so $A$ is integral over $A^G$; finite generation follows by a classical argument of Noether. Invariant functions separate orbits, because the product of the translates of a function that vanishes on one orbit and is $1$ on another is invariant. Taking norms turns a defining equation of a $G$-stable divisor into an invariant function, which shows that $|G|$ kills the class group when $A$ is factorial. Completion along a fibre turns $A$ into a product of complete local rings permuted by $G$, and averaging with the Reynolds operator chooses coordinates on which a fixing group acts linearly.

### Examples

**Example P8.9.8 (the quadric cone).** Let $G = \{ \pm 1 \}$ act on $\mathbb{A}^2$, with $\operatorname{char} k \neq 2$. A monomial $x^a y^b$ is sent to $(-1)^{a + b} x^a y^b$, and $G$ acts diagonally, so $k[x, y]^G$ is spanned by the monomials of even degree. They are products of $u = x^2$, $v = xy$, $w = y^2$, so $k[x, y]^G = k[u, v, w] / (uw - v^2)$: the surjection $k[u, v, w] \to k[x^2, xy, y^2]$ kills $uw - v^2$, which is irreducible, and both rings have dimension $2$, so the kernel is the height one prime $(uw - v^2)$. The quotient $\mathbb{A}^2 / \{ \pm 1 \}$ is the quadric cone, the singularity $\frac{1}{2}(1, 1)$ of Section 9.3, and its class group is $\mathbb{Z}/2$ by Example P8.7.7, as Proposition P8.9.4 allows. The action is free away from the origin, so by Proposition P8.9.5 the quotient is smooth away from the vertex.

**Example P8.9.9 (roots of unity on the line).** Let $\mu_n \subseteq k^*$ be the group of $n$-th roots of unity, $n$ invertible in $k$, acting on $\mathbb{A}^1$ by multiplication. Then $k[x]^{\mu_n} = k[x^n]$, since $\zeta \cdot x^a = \zeta^{-a} x^a$, so the quotient $\mathbb{A}^1 \to \mathbb{A}^1$ is $x \mapsto x^n$. The quotient of a smooth variety can be smooth even when the action is not free, and the map then ramifies along the fixed locus.

**Example P8.9.10 (the symmetric group on the plane).** Let $S_2$ act on $\mathbb{A}^2$ by $(x, y) \mapsto (y, x)$, with $\operatorname{char} k \neq 2$. In the coordinates $s = x + y$, $d = x - y$ the action is $(s, d) \mapsto (s, -d)$, so $k[x, y]^{S_2} = k[s, d^2] = k[x + y, xy]$, since $d^2 = s^2 - 4xy$. The quotient is again $\mathbb{A}^2$, and $\pi$ is ramified along the diagonal $x = y$, the fixed line of the swap.

**Example P8.9.11 (the singularity $\frac{1}{2}(1, 1, 1)$).** Let $\{ \pm 1 \}$ act on $\mathbb{A}^3$, with $\operatorname{char} k \neq 2$. As in Example P8.9.8 the invariant ring is spanned by the monomials of even degree, and is generated by the six quadratic monomials $x_i x_j$. The quotient is the affine cone over the Veronese surface $v_2(\mathbb{P}^2) \subseteq \mathbb{P}^5$, a three-dimensional isolated singularity with class group $\mathbb{Z}/2$ (Chapter 12). Here no nontrivial element fixes a hyperplane, a condition that Section 9.2 shows is what keeps the quotient singular.

### Proof

*Lemma P8.9.2.* For $b \in A^G$ and $h \in G$, $h \cdot R(a) = \frac{1}{|G|} \sum_g hg \cdot a = R(a)$, so $R(a) \in A^G$, and $R(ba) = \frac{1}{|G|} \sum_g (g \cdot b)(g \cdot a) = b R(a)$. If $a \in A^G$ every term is $a$, so $R(a) = a$. Thus $A = A^G \oplus \ker R$ as $A^G$-modules. If $a = \sum_i b_i c_i \in IA \cap A^G$ with $b_i \in I$, $c_i \in A$, then $a = R(a) = \sum_i b_i R(c_i) \in I$. For a module $M$ with a $G$-action, $M^G$ is the kernel of $M \to \prod_{g \in G} M$, $m \mapsto (g m - m)_g$, and $- \otimes_{A^G} P$ preserves finite products and kernels when $P$ is flat, so $(M \otimes P)^G = M^G \otimes P$.

*Theorem P8.9.3.* (1) Let $a_1, \dots, a_r$ generate $A$ as a $k$-algebra. Each $a_i$ is a root of $p_i(t) = \prod_{g \in G} (t - g \cdot a_i)$, a monic polynomial whose coefficients are invariant, because $G$ permutes the factors. Let $B \subseteq A^G$ be the $k$-subalgebra generated by the coefficients of $p_1, \dots, p_r$. Then $A$ is generated as a $B$-module by the monomials $a_1^{e_1} \cdots a_r^{e_r}$ with $e_i < |G|$, so $A$ is a finite $B$-module. Since $B$ is a finitely generated $k$-algebra it is Noetherian, so the submodule $A^G$ of $A$ is a finite $B$-module, and $A^G$ is a finitely generated $k$-algebra. As $A^G$ is a domain, $X$ is an affine variety. The $A^G$-module $A$ is finite because it is finite over $B$. An injective integral extension satisfies lying over, so $\pi$ is surjective.

(2) Points in one orbit have the same image, because invariant functions take the same value at $v$ and $g v$. Let $v, w$ be closed points with $Gv \cap Gw = \emptyset$. The finite sets $Gv$ and $Gw$ are disjoint closed subsets of $V$, so by the Chinese remainder theorem there is $a \in A$ with $a = 0$ on $Gv$ and $a = 1$ on $Gw$. The norm $f = \prod_{g \in G} g \cdot a$ is invariant, $f(v) = \prod_g a(g^{-1} v) = 0$ and $f(w) = 1$. So $\pi(v) \neq \pi(w)$.

(3) A $G$-invariant morphism $V \to Z = \operatorname{Spec} C$ is a homomorphism $C \to A$ whose image consists of invariants, so it factors uniquely through $A^G$.

(4) Normality of $A^G$ is Proposition P1.4.21. Since $A$ is integral over $A^G$, the two rings have the same dimension. Every invariant fraction $\varphi \in k(V)^G$ can be written $a/b$ with $b$ invariant: multiply numerator and denominator by $\prod_{g \neq 1} g \cdot b$, so that the denominator becomes the norm of $b$, and then the numerator is $\varphi$ times an invariant, hence invariant. So $k(V)^G = \operatorname{Frac}(A^G) = k(X)$. If $G$ acts faithfully on $A$ it acts faithfully on $k(V)$, and Artin's theorem in Galois theory shows that $k(V) / k(V)^G$ is Galois with group $G$.

*Proposition P8.9.4.* Let $P$ be a prime divisor on $X$ and $Q_1, \dots, Q_s$ the prime divisors of $V$ lying over it. They are the codimension one points of $V$ over the generic point of $P$, and $G$ permutes the primes of $A$ over a given prime of $A^G$ transitively (Atiyah and Macdonald, Introduction to Commutative Algebra, Exercise 5.13), so $G$ permutes $Q_1, \dots, Q_s$ transitively. Let $Q = Q_1 + \dots + Q_s$. Since $A$ is factorial, $Q = \operatorname{div}_V(f)$ for some $f \in A$, and $g \cdot f$ has divisor $g(Q) = Q$. The norm $F = \prod_{g \in G} g \cdot f$ is invariant, and $\operatorname{div}_V(F) = \sum_g g(Q) = |G| Q$. Let $e$ be the ramification index of $\pi$ along $Q_1$, so that $v_{Q_i}(h) = e \, v_P(h)$ for $h \in k(X)$, the same $e$ for every $i$ by transitivity. The zeros of $F$ on $X$ lie in $\pi(Q) = P$, and $v_P(F) = v_{Q_1}(F)/e = |G|/e$. So $\operatorname{div}_X(F) = (|G|/e) P$, and $|G| P$ is principal. By linearity $|G| D$ is principal for every Weil divisor $D$, and in particular $|G| D$ is Cartier, so $X$ is $\mathbb{Q}$-factorial in the sense of Section P3.9.

*Proposition P8.9.5.* Let $\mathfrak{m} \subseteq A^G$ be the maximal ideal of $x$. By part 2 of Theorem P8.9.3, the maximal ideals of $A$ containing $\mathfrak{m} A$ are those of the points $g_1 v, \dots, g_s v$, where $g_1 = 1, \dots, g_s$ are representatives of $G/H$. Since $A$ is a finite $A^G$-module, its $\mathfrak{m}$-adic completion is $\widehat{A} = A \otimes_{A^G} \widehat{\mathcal{O}}_{X, x}$, and by the Chinese remainder theorem it is the product $\prod_{i} \widehat{\mathcal{O}}_{V, g_i v}$ (Matsumura, Theorem 8.15). The group $G$ acts on $\widehat{A}$ and permutes the factors as it permutes the points $g_i v$; the stabiliser of the factor at $v$ is $H$. An element $(c_1, \dots, c_s)$ of the product is $G$-invariant if and only if $c_1$ is $H$-invariant and $c_i = g_i \cdot c_1$ for every $i$, so projection to the first factor is an isomorphism $\widehat{A}^G \cong \widehat{\mathcal{O}}_{V, v}^H$. On the other hand $\widehat{\mathcal{O}}_{X, x}$ is flat over $A^G$, so Lemma P8.9.2 gives $\widehat{A}^G = A^G \otimes_{A^G} \widehat{\mathcal{O}}_{X, x} = \widehat{\mathcal{O}}_{X, x}$. If $H = \{1\}$ the map $\widehat{\mathcal{O}}_{X, x} \to \widehat{\mathcal{O}}_{V, v}$ induced by $\pi$ is an isomorphism, so $\mathcal{O}_{X, x} \to \mathcal{O}_{V, v}$ is flat and unramified, and $\pi$ is étale at $v$.

*Proposition P8.9.6.* The group $H$ preserves $\mathfrak{m}_v$ and $\mathfrak{m}_v^2$, so it acts linearly on $T^* = \mathfrak{m}_v / \mathfrak{m}_v^2$, a space of dimension $n$ because $v$ is a smooth point. Choose any $k$-linear section $s_0 \colon T^* \to \mathfrak{m}_v$ of the projection, and put $s = \frac{1}{|H|} \sum_{h \in H} h \circ s_0 \circ h^{-1}$. Each term is a section, because the projection is $H$-equivariant, so $s$ is an $H$-equivariant section. The images $x_1, \dots, x_n$ of a basis of $T^*$ span the $H$-stable subspace $s(T^*)$ and form a regular system of parameters. The ring $\widehat{\mathcal{O}}_{V, v}$ is a complete regular local ring containing its residue field $k$, so the continuous homomorphism $k[[x_1, \dots, x_n]] \to \widehat{\mathcal{O}}_{V, v}$ is an isomorphism (Matsumura, Theorem 29.7). It is $H$-equivariant, since both actions are continuous ring automorphisms that agree on the topological generators $x_i$.

### Exercises

1. (A) Let $\mu_3$ act on $\mathbb{A}^2$ by $\zeta (x, y) = (\zeta x, \zeta y)$. Show that the invariant ring is generated by the four cubic monomials, and write down the quadratic equations among them.
2. (A) Show that the map $\mathbb{A}^2 \to \mathbb{A}^2/\{ \pm 1 \}$ of Example P8.9.8 is étale away from the origin by computing its differential.
3. (B) Let $G$ act freely on a smooth affine variety $V$. Show that $V/G$ is smooth, and that $\pi_* \mathcal{O}_V$ is locally free of rank $|G|$.
4. (B) Let $\mu_n$ act on $\mathbb{A}^2$ by $\zeta (x, y) = (\zeta x, \zeta y)$. Show that $\operatorname{Cl}(\mathbb{A}^2/\mu_n) \cong \mathbb{Z}/n$, generated by the image of the line $x = 0$, using Proposition P8.9.4 for the bound and Example P8.7.7 for the equality.
5. (B) Let $p = \operatorname{char} k > 0$ and let $\mathbb{Z}/p$ act on $\mathbb{A}^2$ by $(x, y) \mapsto (x, x + y)$. Find the fixed locus, and explain which step of Lemma P8.9.2 fails.
6. (C) Let $V$ be a quasi-projective variety with an action of $G$. Show that every orbit is contained in an affine $G$-stable open set, and deduce that $V/G$ exists as a variety, glued from the quotients of Theorem P8.9.3.

### Lean

Group actions on varieties and their quotients are not in the repository. The singularity classes that quotient singularities belong to, `MinimalModel.IsKlt` in particular, are stated in `MinimalModel/Statements/Basic.lean`, but nothing there mentions group actions.

### Notes and history

The finite generation of rings of invariants of finite groups is due to Hilbert in characteristic zero and to Noether in general; the argument of part 1 of Theorem P8.9.3 is Noether's. Quotients of varieties by finite groups are treated in Mumford, Abelian Varieties, Section 7, and in the first chapters of Mumford's Geometric Invariant Theory. The linearization of a finite group action at a fixed point is due to Cartan, in the analytic setting. Quotient singularities are the starting point of Reid's Young Person's Guide (Rei87), and Kollár and Mori prove in Section 5.2 (KM98) that they are rational and klt, which this volume returns to in Chapter 11 and Volume 4 proves as Theorem 4.2.30.
