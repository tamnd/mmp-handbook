---
title: Morphisms to projective space
nodes: []
sources: [Vak25, Har77, GW20, Stacks]
reads_with: [Vak25:ch16, Har77:II.7, GW20:ch13]
requires: [P3.4, P3.6, P3.7, P3.9]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Morphisms to projective space

### Statement

Let $X$ be a scheme over a field $k$ and $\mathcal{L}$ an invertible sheaf. For a base point free linear system $V \subseteq \Gamma(X, \mathcal{L})$ with basis $s_0, \dots, s_n$, Theorem P3.6.21 gives a morphism $\varphi_V \colon X \to \mathbb{P}^n_k$ with $\varphi_V^* \mathcal{O}(1) \cong \mathcal{L}$ and $\varphi_V^* x_i = s_i$. Write $\varphi_{|\mathcal{L}|}$ when $V$ is complete. A matrix $g = (g_{ij}) \in \operatorname{GL}_{n + 1}(k)$ acts on $k[x_0, \dots, x_n]$ by the graded automorphism $x_i \mapsto \sum_j g_{ij} x_j$, and so on $\mathbb{P}^n_k = \operatorname{Proj} k[x_0, \dots, x_n]$ by an automorphism, a *linear automorphism*.

**Theorem P3.10.9 (the morphism of a linear system).** Let $V$ be base point free with basis $s_0, \dots, s_n$.

1. For every linear form $\ell = \sum a_i x_i \neq 0$, $\varphi_V^{-1}(V_+(\ell)) = \{ x : s(x) = 0 \}$ for $s = \sum a_i s_i$. If $X$ is integral, the pullback of the Cartier divisor $V_+(\ell)$ is defined and equals $Z(s)$. So the hyperplanes pull back to the members of $|V|$.
2. Another basis $s'_i = \sum_j g_{ij} s_j$ gives $\varphi'_V = g \circ \varphi_V$, with $g$ the linear automorphism of the matrix $(g_{ij})$. So $\varphi_V$ is determined by $V$ up to a linear automorphism.
3. If $X$ is reduced, the image of $\varphi_V$ lies in no hyperplane. Conversely, let $\varphi \colon X \to \mathbb{P}^n_k$ be a morphism whose image lies in no hyperplane, with $X$ reduced. Then the sections $\varphi^* x_i$ of $\mathcal{L} = \varphi^* \mathcal{O}(1)$ are linearly independent, they span a base point free linear system $V$, and $\varphi = \varphi_V$.

Lean: not in Lean as stated. Mathlib `AlgebraicGeometry.Proj.fromOfGlobalSections` gives a morphism to $\operatorname{Proj}$ from global functions, the case $\mathcal{L} = \mathcal{O}_X$.

**Proposition P3.10.10 (incomplete systems and projections).** Let $V \subseteq W \subseteq \Gamma(X, \mathcal{L})$ be linear systems with $V$ base point free. Choose a basis $s_0, \dots, s_N$ of $W$ such that $s_0, \dots, s_n$ is a basis of $V$, and let $\Lambda = V_+(x_0, \dots, x_n) \subseteq \mathbb{P}^N_k$. Then $W$ is base point free, $\varphi_W(X) \cap \Lambda = \emptyset$, and $\varphi_V = \pi \circ \varphi_W$, where $\pi \colon \mathbb{P}^N_k \setminus \Lambda \to \mathbb{P}^n_k$ is the *linear projection* $[x_0 : \dots : x_N] \mapsto [x_0 : \dots : x_n]$. In particular, if $\Gamma(X, \mathcal{L})$ has finite dimension and is base point free, every base point free linear system of $\mathcal{L}$ gives a projection of $\varphi_{|\mathcal{L}|}$.

Lean: not in Lean as stated.

**Definition P3.10.11 (nondegenerate, linearly normal).** A closed subscheme $X \subseteq \mathbb{P}^n_k$ is *nondegenerate* if it lies in no hyperplane, that is, if the restriction $\Gamma(\mathbb{P}^n, \mathcal{O}(1)) \to \Gamma(X, \mathcal{O}_X(1))$ is injective. It is *linearly normal* if this map is surjective. So a nondegenerate $X$ is linearly normal if and only if its inclusion is $\varphi_{|\mathcal{O}_X(1)|}$, up to a linear automorphism.

Lean: not in Lean as stated.

**Theorem P3.10.12 (closed immersions).** Let $k$ be algebraically closed, $X$ a projective scheme over $k$, and $V \subseteq \Gamma(X, \mathcal{L})$ base point free. For a closed point $x$ let $V_x = \{ s \in V : s(x) = 0 \}$. Then $\varphi_V$ is a closed immersion if and only if:

1. ($V$ *separates points*) for closed points $x \neq y$ there is $s \in V$ with $s(x) = 0$ and $s(y) \neq 0$; and
2. ($V$ *separates tangent vectors*) for every closed point $x$ the map $V_x \to \mathfrak{m}_x \mathcal{L}_x / \mathfrak{m}_x^2 \mathcal{L}_x$ is surjective.

Lean: not in Lean as stated. Mathlib `AlgebraicGeometry.IsFinite.iff_isProper_and_locallyQuasiFinite` is the step from proper and quasi-finite to finite (proved in Mathlib).

### Proof in words

A base point free system of sections gives a morphism to projective space, and the hyperplanes pull back to the divisors of the sections. A larger system gives a morphism to a larger projective space, and the smaller system is recovered by forgetting coordinates. A morphism from a projective scheme is a closed immersion when it is injective on points and on tangent vectors. Injectivity makes the morphism finite, and on a finite morphism the tangent condition and Nakayama's lemma make the map of structure sheaves surjective.

### Examples

**Example P3.10.13 (rational normal curves).** Let $d \geq 1$. The complete system $\Gamma(\mathbb{P}^1_k, \mathcal{O}(d))$ has basis $s^d, s^{d - 1} t, \dots, t^d$ and gives $\nu_d \colon \mathbb{P}^1_k \to \mathbb{P}^d_k$. Over an algebraically closed $k$ the criterion holds: for $x = [a : b]$ the section $(bs - at)^d$ vanishes exactly at $x$, which separates points, and at $x = [1 : 0]$, with local coordinate $u = t/s$, the section $s^{d - 1} t$ has local function $u$, which generates $\mathfrak{m}_x / \mathfrak{m}_x^2$. By symmetry the same holds at every point, using the linear change of coordinates that moves $x$ to $[1 : 0]$. So $\nu_d$ is a closed immersion, onto the *rational normal curve* of degree $d$. For $d = 3$ this is the *twisted cubic*.

**Example P3.10.14 (a projection of the twisted cubic).** Let $V = \langle s^3, s t^2, t^3 \rangle \subseteq \Gamma(\mathbb{P}^1_k, \mathcal{O}(3))$. It is base point free, and $\varphi_V$ is the projection of the twisted cubic from the point $[0 : 1 : 0 : 0]$ by Proposition P3.10.10. Its image satisfies $y^3 = x z^2$ for $[x : y : z] = [s^3 : s t^2 : t^3]$, a cuspidal cubic. At $x_0 = [1 : 0]$, $V_{x_0} = \langle s t^2, t^3 \rangle$ has local functions $u^2$ and $u^3$, which lie in $\mathfrak{m}^2$. So $V$ does not separate tangent vectors at $x_0$, and $\varphi_V$ is not a closed immersion, although it is injective on closed points. The image is singular at $[1 : 0 : 0]$.

**Example P3.10.15 (the degree two map of the line).** Let $V = \langle s^2, t^2 \rangle \subseteq \Gamma(\mathbb{P}^1_k, \mathcal{O}(2))$, as in Example P3.10.8, and $k$ algebraically closed. Then $\varphi_V = [s^2 : t^2]$. If $\operatorname{char} k \neq 2$, the points $[1 : 1]$ and $[1 : -1]$ have the same image, and $V$ does not separate them. If $\operatorname{char} k = 2$, then $s^2 + c^2 t^2 = (s + ct)^2$, so every member of $|V|$ is twice a point, $V$ separates points, and $V_x$ has local functions in $\mathfrak{m}_x^2$. In both cases $\varphi_V$ is a finite morphism of degree $2$ and not a closed immersion.

**Example P3.10.16 (a fibration).** On $X = \mathbb{P}^1_k \times_k \mathbb{P}^1_k$ the system $\Gamma(\mathcal{O}(1, 0))$, spanned by the pullbacks of $s$ and $t$ from the first factor, is base point free, and its morphism is the first projection $X \to \mathbb{P}^1_k$. Its fibres are curves, so it is not finite. It does not separate the points of a fibre.

**Example P3.10.17 (the quadric cone).** On $Q_0 \subseteq \mathbb{P}^3_k$ of Example P3.10.7 the system $|H|$ of plane sections is base point free, and the restriction map $\Gamma(\mathbb{P}^3, \mathcal{O}(1)) \to \Gamma(Q_0, \mathcal{O}_{Q_0}(1))$ is injective, since $Q_0$ lies in no plane. The inclusion $Q_0 \to \mathbb{P}^3_k$ is $\varphi_V$ for $V$ the image of this map, so $H$ is very ample. The system $|L|$ has a base point, so it defines no morphism. It defines the rational map of Example P3.10.33.

### Proof

*Proof of Theorem P3.10.9.* (1) By Theorem P3.6.21, $\varphi_V^* x_i = s_i$, and $\varphi_V^*$ is linear on sections, so $\varphi_V^* \ell = s$. The set $\varphi_V^{-1}(V_+(\ell))$ is the set of $x$ where the pullback of $\ell$ vanishes in the fibre, that is, where $s(x) = 0$. If $X$ is integral and $s \neq 0$, the generic point of $X$ does not map into $V_+(\ell)$, as $s$ is not zero at the generic point. A local equation of $V_+(\ell)$ on $D_+(x_j)$ is $\ell/x_j$, and it pulls back to $s/s_j$ on $X_{s_j}$, which is a local equation of $Z(s)$. So $\varphi_V^* V_+(\ell) = Z(s)$ as Cartier divisors.

(2) The morphism $g \circ \varphi_V$ has $(g \circ \varphi_V)^* x_i = \varphi_V^*(\sum_j g_{ij} x_j) = s'_i$, under the isomorphism $\varphi_V^* g^* \mathcal{O}(1) \cong \varphi_V^* \mathcal{O}(1) \cong \mathcal{L}$ induced by $g$. By the uniqueness in part 3 of Theorem P3.6.21, it equals $\varphi'_V$.

(3) If the image of $\varphi_V$ lies in $V_+(\ell)$, then $s = \sum a_i s_i$ vanishes in every fibre. On a reduced scheme a section of an invertible sheaf that vanishes in every fibre is zero, since locally it is a function lying in every prime ideal, so nilpotent, so zero. This contradicts the independence of the $s_i$. Conversely, if $\sum a_i \varphi^* x_i = 0$ with some $a_i \neq 0$, then the pullback of $\ell = \sum a_i x_i$ vanishes everywhere, and the image lies in $V_+(\ell)$. So the sections $\varphi^* x_i$ are independent, they generate $\mathcal{L}$ by part 1 of Theorem P3.6.21, and $\varphi = \varphi_V$ by part 3 of that theorem. $\square$

*Proof of Proposition P3.10.10.* $W$ contains $V$, so $\operatorname{Bs}(W) \subseteq \operatorname{Bs}(V) = \emptyset$ by Proposition P3.10.2. By part 1 of Theorem P3.10.9, $\varphi_W^{-1}(\Lambda) = \bigcap_{i \leq n} \varphi_W^{-1}(V_+(x_i)) = \operatorname{Bs}(V) = \emptyset$. The sections $x_0, \dots, x_n$ of $\mathcal{O}(1)$ generate it on $\mathbb{P}^N_k \setminus \Lambda$, so they define the morphism $\pi$ by Theorem P3.6.21. The morphism $\pi \circ \varphi_W$ pulls $x_i$ back to $\varphi_W^* x_i = s_i$ for $i \leq n$, and so it equals $\varphi_V$ by part 3 of Theorem P3.6.21. $\square$

*Proof of Theorem P3.10.12.* Write $\varphi = \varphi_V \colon X \to P = \mathbb{P}^n_k$. Choose $x$ closed and $s_0 \in V$ with $s_0(x) \neq 0$, which exists as $V$ is base point free, and complete it to a basis $s_0, \dots, s_n$. Replacing $s_i$ by $s_i - c_i s_0$ with $c_i \in k = \kappa(x)$, assume $s_i(x) = 0$ for $i \geq 1$. Then $y = \varphi(x) = [1 : 0 : \dots : 0]$, and $\mathfrak{m}_y \subseteq \mathcal{O}_{P, y}$ is generated by $x_1/x_0, \dots, x_n/x_0$, which pull back to the functions $s_1/s_0, \dots, s_n/s_0$ on $X_{s_0}$. The elements $s_1, \dots, s_n$ span $V_x$, and under the isomorphism $\mathcal{L}_x \cong \mathcal{O}_{X, x}$, $s \mapsto s/s_0$, condition 2 says that the images of $s_i/s_0$ span $\mathfrak{m}_x / \mathfrak{m}_x^2$. So condition 2 at $x$ holds if and only if $\varphi^\sharp \colon \mathfrak{m}_y \to \mathfrak{m}_x / \mathfrak{m}_x^2$ is surjective. Condition 1 holds if and only if $\varphi$ is injective on closed points: if $s(x) = 0 \neq s(y)$ with $s = \sum a_i s_i$, the hyperplane $V_+(\sum a_i x_i)$ contains $\varphi(x)$ and not $\varphi(y)$, and conversely a hyperplane through $\varphi(x)$ that misses $\varphi(y)$ gives such an $s$, by part 1 of Theorem P3.10.9.

*The conditions are necessary.* If $\varphi$ is a closed immersion, it is injective, and $\mathcal{O}_{P, y} \to \mathcal{O}_{X, x}$ is surjective, so $\mathfrak{m}_y \to \mathfrak{m}_x$ is surjective.

*The conditions are sufficient.* Step 1: $\varphi$ is proper and injective. It is proper by Proposition P3.4.20, as $X$ is proper and $P$ is separated over $k$. Let $x \neq x'$ with $\varphi(x) = \varphi(x') = y$, and let $X_1, X_2$ be the closures of $x, x'$. Their images are closed, so $\varphi(X_1) = \varphi(X_2) = \overline{\{y\}} = Z$. A closed point $z$ of $Z$ has closed fibres $\varphi^{-1}(z) \cap X_i \neq \emptyset$, which contain closed points of $X$ by part 3 of Proposition P3.7.3. By condition 1 these closed points are a single point, so $X_1$ and $X_2$ have the same closed points. As the closed points are dense in every closed subset (part 3 of Proposition P3.7.3), $X_1 = X_2$, and so $x = x'$, as an irreducible closed set has one generic point. So $\varphi$ is injective, and in particular quasi-finite.

Step 2: $\varphi$ is finite. A proper morphism with finite fibres is finite (Stacks, Tag 02LS, recorded in Mathlib as `IsFinite.iff_isProper_and_locallyQuasiFinite`). This step is not proved in this handbook. It is a form of Zariski's main theorem.

Step 3: the stalks. Let $y = \varphi(x)$ with $x$ closed. Since $\varphi$ is finite and $\varphi^{-1}(y) = \{x\}$, $(\varphi_* \mathcal{O}_X)_y = \mathcal{O}_{X, x}$, a finite $\mathcal{O}_{P, y}$-module: on an affine open $\operatorname{Spec} A \ni y$ with preimage $\operatorname{Spec} B$, the localization $B_\mathfrak{q}$ at the prime $\mathfrak{q}$ of $y$ is a semilocal ring whose maximal ideals are the primes over $\mathfrak{q}$, so $B_\mathfrak{q} = B_x$. Condition 2 gives $\mathfrak{m}_y \mathcal{O}_{X, x} + \mathfrak{m}_x^2 = \mathfrak{m}_x$, so $\mathfrak{m}_y \mathcal{O}_{X, x} = \mathfrak{m}_x$ by Nakayama's lemma over $\mathcal{O}_{X, x}$. As $\kappa(x) = k = \kappa(y)$, $\mathcal{O}_{X, x} / \mathfrak{m}_y \mathcal{O}_{X, x} = k$ is generated by $1$, and Nakayama's lemma over $\mathcal{O}_{P, y}$ shows that $\mathcal{O}_{P, y} \to \mathcal{O}_{X, x}$ is surjective.

Step 4: conclusion. The cokernel $\mathcal{C}$ of $\mathcal{O}_P \to \varphi_* \mathcal{O}_X$ is coherent, as $\varphi_* \mathcal{O}_X$ is coherent for $\varphi$ finite. Its support is closed. By Step 3 it contains no image of a closed point, and it contains no point outside the closed set $\varphi(X)$, where $\varphi_* \mathcal{O}_X$ and so $\mathcal{C}$ vanish. So the support contains no closed point and is empty, by part 3 of Proposition P3.7.3. So $\mathcal{O}_P \to \varphi_* \mathcal{O}_X$ is surjective, and on an affine open $\operatorname{Spec} A$ of $P$ with preimage $\operatorname{Spec} B$ the map $A \to B$ is surjective. So $\varphi$ is a closed immersion. $\square$

### Exercises

1. (A) Write the twisted cubic $\nu_3(\mathbb{P}^1)$ as the zero locus of three quadrics in $\mathbb{P}^3_k$.
2. (A) Let $k$ be algebraically closed of characteristic $0$ and $V = \langle s^3, s^2 t + s t^2, t^3 \rangle \subseteq \Gamma(\mathbb{P}^1_k, \mathcal{O}(3))$. Show that $V$ is base point free and find two points of $\mathbb{P}^1$ with the same image under $\varphi_V$.
3. (A) Let $X \subseteq \mathbb{P}^n_k$ be closed and reduced. Show that $X$ is nondegenerate if and only if the linear forms are linearly independent as sections of $\mathcal{O}_X(1)$.
4. (B) Show that the image of $\varphi_V$ in Example P3.10.14 is the closed subscheme $C = V_+(y^3 - x z^2)$ of $\mathbb{P}^2_k$, and that $\varphi_V \colon \mathbb{P}^1_k \to C$ is finite and bijective but not an isomorphism.
5. (B) Let $k$ be algebraically closed and $X$ projective over $k$. Show that a very ample $\mathcal{L}$ is base point free and that $\Gamma(X, \mathcal{L})$ separates points and tangent vectors. Show that if $V \subseteq \Gamma(X, \mathcal{L})$ separates points and tangent vectors, so does every larger system.
6. (C) Let $X \subseteq \mathbb{P}^n_k$ be closed, $p \in \mathbb{P}^n_k(k) \setminus X$, and $\pi_p$ the projection from $p$. Show that $\pi_p|_X$ is a closed immersion if and only if every line through $p$ meets $X$ in a subscheme of length at most $1$, with $k$ algebraically closed.
7. (C) Let $k$ be algebraically closed, $X$ projective over $k$, $\mathcal{L}$ very ample and $\mathcal{M}$ base point free. Show with Theorem P3.10.12 that $\Gamma(X, \mathcal{L} \otimes \mathcal{M})$ separates points and tangent vectors, and deduce that $\mathcal{L} \otimes \mathcal{M}$ is very ample.

### Lean

Mathlib constructs morphisms to $\operatorname{Proj}$ from global functions, `AlgebraicGeometry.Proj.fromOfGlobalSections`, and proves that a proper locally quasi-finite morphism is finite, `AlgebraicGeometry.IsFinite.iff_isProper_and_locallyQuasiFinite`. Morphisms defined by sections of an invertible sheaf, and the criterion for closed immersions, are not in Lean as stated. The handbook adds no `MinimalModel` node here.

### Notes and history

Theorem P3.10.12 is Hartshorne, Proposition II.7.3, where Step 2 is the statement that a projective morphism with finite fibres is finite, Exercise III.11.2 there. The literature state is theorem. In the minimal model program a morphism given by a base point free system $|mD|$ is the contraction defined by $D$. Its Stein factorization has connected fibres, and the cone and contraction theorems of Volume 4 produce such systems from the negativity of $K_X$ on a ray of curves. Example P3.10.16 is the model of a Mori fibre space, and Example P3.10.14 shows that the image of a smooth curve under a finite morphism can be singular.
