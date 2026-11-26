---
title: Gale duality
nodes: []
sources: [CLS11, FS04]
reads_with: [CLS11:ch14, CLS11:ch15]
requires: [3.1, 3.3, 3.4, 3.5]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Gale duality

### Statement

A complete simplicial fan lives in $N_{\mathbb{R}}$, but its nef cone, its effective cone and the steps of its minimal model program live in $N^1(X) = \operatorname{Cl}(X) \otimes \mathbb{R}$. Gale duality is the bridge between the two spaces. It sends the list of ray generators $u_\rho \in N_{\mathbb{R}}$ to the list of divisor classes $[D_\rho] \in N^1(X)$, and it turns statements about subsets of the $u_\rho$ into statements about the complementary subsets of the $[D_\rho]$. This section sets up the duality and computes the nef, ample and effective cones of a projective simplicial toric variety in its terms.

Throughout the chapter, $N \cong \mathbb{Z}^n$ is a lattice with dual $M$, and $U = (u_1, \dots, u_r)$ is a list of distinct primitive vectors of $N$ that span $N_{\mathbb{R}}$. The indices $\rho = 1, \dots, r$ play the role of rays. For $I \subseteq \{1, \dots, r\}$, write $I^c$ for its complement and $u_I$ for the list $(u_\rho)_{\rho \in I}$.

**Definition 3.7.1 (the Gale dual).** Let $\partial \colon M_{\mathbb{R}} \to \mathbb{R}^r$ be the map $m \mapsto (\langle m, u_\rho \rangle)_\rho$. It is injective, since the $u_\rho$ span $N_{\mathbb{R}}$. Put

$$G_U = \mathbb{R}^r / \partial(M_{\mathbb{R}}), \qquad \beta_\rho = [e_\rho] \in G_U, \qquad R(U) = \Big\{ b \in \mathbb{R}^r : \sum_\rho b_\rho u_\rho = 0 \Big\}.$$

The list $B = (\beta_1, \dots, \beta_r)$ is the *Gale dual* of $U$. The space $G_U$ has dimension $r - n$. The standard pairing of $\mathbb{R}^r$ with itself identifies $R(U)$ with the dual space of $G_U$: a vector $b$ vanishes on $\partial(M_{\mathbb{R}})$ if and only if $\langle m, \sum_\rho b_\rho u_\rho \rangle = 0$ for all $m$, that is, if and only if $b \in R(U)$. So for $a \in \mathbb{R}^r$ and $b \in R(U)$ the number $\langle [a], b \rangle = \sum_\rho a_\rho b_\rho$ is well defined. The class $[a]$ is the *class* of the vector $a$, or of the divisor $\sum_\rho a_\rho D_\rho$.

When $U$ is the list of minimal generators of the rays of a complete simplicial fan $\Sigma$, Theorem 3.3.4 and Theorem 3.4.20 identify $G_U$ with $N^1(X_\Sigma) = \operatorname{Cl}(X_\Sigma) \otimes \mathbb{R}$, with $\beta_\rho = [D_\rho]$, and $R(U)$ with $N_1(X_\Sigma)$, with the pairing equal to the intersection number: $D \cdot C = \langle [a], b \rangle$ for $D = \sum_\rho a_\rho D_\rho$ and $C$ with $D_\rho \cdot C = b_\rho$.

**Lemma 3.7.2 (Gale duality).** Let $I \subseteq \{1, \dots, r\}$.

1. $u_I$ is linearly independent if and only if $(\beta_\rho)_{\rho \in I^c}$ spans $G_U$.
2. $u_I$ spans $N_{\mathbb{R}}$ if and only if $(\beta_\rho)_{\rho \in I^c}$ is linearly independent.
3. $u_I$ is a basis of $N_{\mathbb{R}}$ if and only if $(\beta_\rho)_{\rho \in I^c}$ is a basis of $G_U$. In that case let $a \in \mathbb{R}^r$ and let $m_I \in M_{\mathbb{R}}$ be the unique form with $\langle m_I, u_\rho \rangle = -a_\rho$ for $\rho \in I$. Then
$$[a] = \sum_{\rho \in I^c} \big( a_\rho + \langle m_I, u_\rho \rangle \big) \beta_\rho .$$
4. For $a \in \mathbb{R}^r$, $[a] \in \operatorname{Cone}(\beta_\rho : \rho \in I^c)$ if and only if there is $m \in M_{\mathbb{R}}$ with $\langle m, u_\rho \rangle = -a_\rho$ for $\rho \in I$ and $\langle m, u_\rho \rangle \ge -a_\rho$ for $\rho \notin I$.
5. $\operatorname{Cone}(U) = N_{\mathbb{R}}$ if and only if the only $c \in \mathbb{R}^r$ with all $c_\rho \ge 0$ and $\sum_\rho c_\rho \beta_\rho = 0$ is $c = 0$. In that case $\operatorname{Cone}(B)$ is strongly convex, and every $\beta_\rho$ is nonzero.

Lean: not yet in Lean.

**Theorem 3.7.3 (the nef, ample and effective cones).** Let $\Sigma$ be a complete simplicial fan, $U$ the list of the minimal generators of its rays, $X = X_\Sigma$, and identify $N^1(X) = G_U$ as above.

1. $\operatorname{Nef}(X) = \bigcap_{\sigma} \operatorname{Cone}(\beta_\rho : \rho \notin \sigma(1))$, the intersection over the cones $\sigma \in \Sigma$ of dimension $n$.
2. If $X$ is projective, the ample cone of $X$ is $\bigcap_{\sigma} \operatorname{Cone}^\circ(\beta_\rho : \rho \notin \sigma(1))$, where $\operatorname{Cone}^\circ(\beta_\rho : \rho \in J)$ is the set of the sums $\sum_{\rho \in J} c_\rho \beta_\rho$ with all $c_\rho > 0$.
3. The cone $\operatorname{Eff}(X) \subset N^1(X)$ of the classes of effective $\mathbb{R}$-divisors is $\operatorname{Cone}(B)$. It is a strongly convex rational polyhedral cone of dimension $r - n$.

Lean: not yet in Lean.

For a maximal cone $\sigma$ the vectors $\beta_\rho$, $\rho \notin \sigma(1)$, form a basis of $G_U$ by part 3 of Lemma 3.7.2, since $\sigma$ is simplicial. So each cone in part 1 is simplicial of full dimension, and $\operatorname{Cone}^\circ$ in part 2 is its interior. The coordinates of $[D]$ in this basis are the numbers $a_\rho + \langle m_\sigma, u_\rho \rangle$, the coefficients of the effective divisor $D + \operatorname{div}(\chi^{m_\sigma})$, which vanishes on $U_\sigma$. Part 1 says that $D$ is nef if and only if all these divisors are effective.

### Proof in words

The space of divisor classes is the space of coefficient vectors modulo the vectors $(\langle m, u_\rho \rangle)_\rho$ of principal divisors. Asking for a combination of the classes $\beta_\rho$, $\rho \notin I$, is asking to kill the coefficients at the indices in $I$ by a principal divisor, that is, to find a linear form with prescribed values on the $u_\rho$, $\rho \in I$. Such a form exists for all prescribed values when $u_I$ is independent, and it is unique when $u_I$ spans. That is the whole of Gale duality: independence on one side is spanning on the other.

For the nef cone, take a maximal cone $\sigma$ and the form $m_\sigma$ of $D$ on it. The divisor $D + \operatorname{div}(\chi^{m_\sigma})$ has coefficient zero on the rays of $\sigma$ and coefficient $a_\rho + \langle m_\sigma, u_\rho \rangle$ on the others. These coefficients are nonnegative for every $\sigma$ exactly when every flat piece of the support function lies above the tent at every ray, which is convexity (Proposition 3.4.12). A toric variety has enough torus-invariant sections, so an effective class is a combination of the $\beta_\rho$ with nonnegative coefficients.

### Examples

**Example 3.7.4 (weighted projective spaces).** Let $u_0, \dots, u_n$ span $N_{\mathbb{R}}$ with the relation $\sum_i q_i u_i = 0$, all $q_i > 0$; when the $u_i$ generate $N$ and $q$ is primitive, the cones spanned by the proper subsets form the fan of the weighted projective space $\mathbb{P}(q_0, \dots, q_n)$ (Cox-Little-Schenck, Chapter 3), and $\mathbb{P}(1,1,1,2)$ of Example 3.3.25 is the case $q = (1, 1, 1, 2)$. Then $R(U) = \mathbb{R} q$, $G_U = \mathbb{R}$ via the pairing with $q$, and $\beta_i = q_i$. Every maximal cone misses exactly one $u_i$, so Theorem 3.7.3 gives $\operatorname{Nef} = \bigcap_i \operatorname{Cone}(q_i) = \mathbb{R}_{\ge 0} = \operatorname{Eff}$. For $\mathbb{P}^n$ all $\beta_i$ equal $1$, the class of a hyperplane.

**Example 3.7.5 (Hirzebruch surfaces).** Let $\mathbb{F}_a$, $a \ge 0$, have the rays $u_1 = (1, 0)$, $u_2 = (0, 1)$, $u_3 = (-1, a)$, $u_4 = (0, -1)$ of Example 3.5.7. The space $R(U)$ has the basis $b_1 = (1, -a, 1, 0)$ and $b_2 = (0, 1, 0, 1)$, from $u_1 + u_3 = a u_2$ and $u_2 + u_4 = 0$. These are the wall relations at $u_2$ and at $u_1$, so $b_1$ is the class of the negative section $D_2$, with $D_2^2 = -a$, and $b_2$ the class of a fibre. In the coordinates $g \mapsto (\langle g, b_1 \rangle, \langle g, b_2 \rangle)$ on $G_U \cong \mathbb{R}^2$,

$$\beta_1 = \beta_3 = (1, 0), \qquad \beta_2 = (-a, 1), \qquad \beta_4 = (0, 1).$$

The four maximal cones $\operatorname{Cone}(u_1, u_2)$, $\operatorname{Cone}(u_2, u_3)$, $\operatorname{Cone}(u_3, u_4)$, $\operatorname{Cone}(u_4, u_1)$ have the complements $\{3, 4\}$, $\{1, 4\}$, $\{1, 2\}$, $\{2, 3\}$, and Theorem 3.7.3 gives

$$\operatorname{Nef}(\mathbb{F}_a) = \operatorname{Cone}((1,0), (0,1)) \cap \operatorname{Cone}((1, 0), (-a, 1)) = \operatorname{Cone}(\beta_1, \beta_4), \qquad \operatorname{Eff}(\mathbb{F}_a) = \operatorname{Cone}(\beta_1, \beta_2).$$

The nef cone is the dual of $NE = \operatorname{Cone}(b_1, b_2)$, as it must be. The canonical class is $K = -\sum_\rho \beta_\rho = (a - 2, -2)$, so $-K = (2 - a, 2)$ is ample for $a \le 1$ and lies on the boundary ray $\langle \cdot, b_1 \rangle = 0$ of the nef cone for $a = 2$.

**Example 3.7.6 (circuits: rank one).** Let $(W, q)$ be circuit data with $J_0 = \emptyset$ (Definition 3.5.10), with $U = W$. Then $R(U) = \mathbb{R} q$, $G_U = \mathbb{R}$ via the pairing with $q$, and the Gale dual is the list of the numbers $\beta_i = q_i$. The fans $T_\pm$ are not complete, so Theorem 3.7.3 does not apply, but its formula still makes sense: each maximal cone $\operatorname{Cone}(W \setminus \{w_j\})$ of $T_+$ has the complement $\{j\}$ with $q_j > 0$, so the intersection of the cones $\operatorname{Cone}(\beta_j)$ is $\mathbb{R}_{\ge 0}$, and for $T_-$ it is $\mathbb{R}_{\le 0}$. A class $[a]$ with $\langle [a], q \rangle > 0$ is positive on the wall curves of $X_+$, since their classes are positive multiples of $q$ (Lemma 3.5.11, part 4), and negative on those of $X_-$. The two triangulations of the circuit are the two half-lines of $G_U$:

- the Atiyah flop $u_1 + u_3 = u_2 + u_4$ has $B = (1, -1, 1, -1)$;
- the Francia flip has $B = (1, 1, -1, -2)$;
- the cone $\frac1n(1,1)$ with its resolution, $u_1 + u_2 = n u_E$, has $B = (1, 1, -n)$. The half-line $\mathbb{R}_{\ge 0}$ is the triangulation $T_+ = \{\operatorname{Cone}(u_1, u_E), \operatorname{Cone}(u_E, u_2)\}$, the minimal resolution, and $\mathbb{R}_{\le 0}$ is the single cone $\operatorname{Cone}(u_1, u_2)$, in which $u_E$ is not a ray. For $n = 2$ and $n = 3$ these are $\frac12(1,1)$ and $\frac13(1,1)$.

In Chapter 8 the same numbers $q_i$ are the weights of an action of $\mathbb{C}^*$ on $\mathbb{C}^{n+1}$, and the two half-lines are the two choices of a character for the quotient.

### Proof

*Proof of Lemma 3.7.2.* Part 1. The list $u_I$ is independent if and only if the map $\mathbb{R}^I \to N_{\mathbb{R}}$, $\lambda \mapsto \sum_{\rho \in I} \lambda_\rho u_\rho$, is injective, that is, if and only if its dual map $M_{\mathbb{R}} \to \mathbb{R}^I$, $m \mapsto (\langle m, u_\rho \rangle)_{\rho \in I}$, is surjective. The vectors $\beta_\rho$, $\rho \in I^c$, span $G_U$ if and only if $\mathbb{R}^{I^c} + \partial(M_{\mathbb{R}}) = \mathbb{R}^r$, where $\mathbb{R}^{I^c}$ is the span of the $e_\rho$ with $\rho \in I^c$. Projecting to the coordinates in $I$, this holds if and only if $\partial(M_{\mathbb{R}})$ maps onto $\mathbb{R}^I$, which is the surjectivity above.

Part 2. The list $u_I$ spans $N_{\mathbb{R}}$ if and only if the only $m$ with $\langle m, u_\rho \rangle = 0$ for all $\rho \in I$ is $m = 0$. The vectors $\beta_\rho$, $\rho \in I^c$, are independent if and only if $\mathbb{R}^{I^c} \cap \partial(M_{\mathbb{R}}) = 0$. A vector $\partial(m)$ lies in $\mathbb{R}^{I^c}$ if and only if $\langle m, u_\rho \rangle = 0$ for $\rho \in I$, and it is zero if and only if $m = 0$, since $\partial$ is injective. So the two conditions agree.

Part 3. The first claim is parts 1 and 2 together. Put $c_\rho = a_\rho + \langle m_I, u_\rho \rangle$ for all $\rho$. Then $c_\rho = 0$ for $\rho \in I$, and $a - c = -\partial(m_I)$, so $[a] = [c] = \sum_{\rho \in I^c} c_\rho \beta_\rho$.

Part 4. The class $[a]$ lies in $\operatorname{Cone}(\beta_\rho : \rho \in I^c)$ if and only if there is $c \in \mathbb{R}^r$ with $c_\rho = 0$ for $\rho \in I$, $c_\rho \ge 0$ for $\rho \notin I$ and $a - c \in \partial(M_{\mathbb{R}})$. Write $a - c = -\partial(m)$. Then $\langle m, u_\rho \rangle = c_\rho - a_\rho$, which is $-a_\rho$ for $\rho \in I$ and at least $-a_\rho$ for $\rho \notin I$. Conversely, given such an $m$, the vector $c = a + \partial(m)$ has these properties.

Part 5. By Theorem 3.1.3, $\operatorname{Cone}(U) = N_{\mathbb{R}}$ if and only if $\operatorname{Cone}(U)^\vee = 0$, that is, if and only if the only $m$ with $\langle m, u_\rho \rangle \ge 0$ for all $\rho$ is $m = 0$: if the dual is $0$, the cone is the dual of $0$, which is $N_{\mathbb{R}}$, and conversely. Now $\sum_\rho c_\rho \beta_\rho = 0$ if and only if $c = \partial(m)$ for some $m$, and then $c \ge 0$ if and only if $m \in \operatorname{Cone}(U)^\vee$, and $c = 0$ if and only if $m = 0$. This proves the equivalence. In that case, if $g$ and $-g$ lie in $\operatorname{Cone}(B)$, write $g = \sum c_\rho \beta_\rho$ and $-g = \sum c'_\rho \beta_\rho$ with $c, c' \ge 0$. Then $\sum (c_\rho + c'_\rho) \beta_\rho = 0$, so $c + c' = 0$, so $c = c' = 0$ and $g = 0$. And $\beta_\rho = 0$ would give the nonzero vector $c = e_\rho$. $\square$

*Proof of Theorem 3.7.3.* Let $D = \sum_\rho a_\rho D_\rho$, with forms $m_\sigma$ on the maximal cones (Definition 3.4.11).

Part 1. For a maximal cone $\sigma$, the list $u_{\sigma(1)}$ is a basis of $N_{\mathbb{R}}$, and the form $m$ of part 4 of Lemma 3.7.2 with $I = \sigma(1)$ must be $m_\sigma$. So $[D] \in \operatorname{Cone}(\beta_\rho : \rho \notin \sigma(1))$ if and only if $\langle m_\sigma, u_\rho \rangle \ge -a_\rho = \varphi_D(u_\rho)$ for all $\rho$. If $D$ is nef, $\varphi_D$ is convex (Theorem 3.4.19), and Proposition 3.4.12, part 2, gives these inequalities for all $\sigma$. Conversely, assume them for all $\sigma$. Let $x \in N_{\mathbb{R}}$. Since $\Sigma$ is complete, $x$ lies in a cone $\tau \in \Sigma$, so $x = \sum_{\rho \in \tau(1)} \lambda_\rho u_\rho$ with $\lambda_\rho \ge 0$, and since $\varphi_D$ is linear on $\tau$,
$$\varphi_D(x) = \sum_{\rho \in \tau(1)} \lambda_\rho \varphi_D(u_\rho) \le \sum_{\rho \in \tau(1)} \lambda_\rho \langle m_\sigma, u_\rho \rangle = \langle m_\sigma, x \rangle.$$
So part 2 of Proposition 3.4.12 holds, $\varphi_D$ is convex, and $D$ is nef by Theorem 3.4.19.

Part 2. For $X$ projective, the ample cone is the interior of $\operatorname{Nef}(X)$ (Theorem 3.4.21). The interior of a finite intersection of sets is the intersection of their interiors, and the interior of the simplicial cone $\operatorname{Cone}(\beta_\rho : \rho \notin \sigma(1))$ of full dimension is $\operatorname{Cone}^\circ(\beta_\rho : \rho \notin \sigma(1))$, since the coordinates in a basis are continuous and the cone is the set where they are nonnegative.

Part 3. Every $\sum_\rho c_\rho D_\rho$ with $c \ge 0$ is effective, so $\operatorname{Cone}(B) \subseteq \operatorname{Eff}(X)$. Conversely, an effective $\mathbb{R}$-divisor is $\sum_i r_i E_i$ with $r_i \ge 0$ and $E_i$ prime divisors, so it suffices to show $[E] \in \operatorname{Cone}(B)$ for a prime divisor $E$. By Theorem 3.3.4, $E$ is linearly equivalent to a torus-invariant divisor $D' = \sum_\rho a_\rho D_\rho$. The sheaf $\mathcal{O}(D') \cong \mathcal{O}(E)$ has a nonzero global section. The global sections of $\mathcal{O}(D')$ are spanned by the characters $\chi^m$ with $\operatorname{div}(\chi^m) + D' \ge 0$ (Cox-Little-Schenck, Chapter 4), so there is such an $m$, and $[E] = [D' + \operatorname{div}(\chi^m)]$ is the class of an effective torus-invariant divisor, which lies in $\operatorname{Cone}(B)$. The cone $\operatorname{Cone}(B)$ is rational polyhedral, since the $\beta_\rho$ are images of lattice vectors. It has dimension $r - n$ by part 1 of Lemma 3.7.2 with $I = \emptyset$, and it is strongly convex by part 5, since $\operatorname{Cone}(U) = |\Sigma| = N_{\mathbb{R}}$. $\square$

### Exercises

1. (A) Compute the Gale dual of the rays of $\mathbb{P}^1 \times \mathbb{P}^1$ and of $\mathbb{P}^1 \times \mathbb{P}^2$, and check Theorem 3.7.3 for both.
2. (A) Let $X$ be the blow-up of $\mathbb{P}^2$ at one fixed point, with rays $(1, 0), (1, 1), (0, 1), (-1, -1)$. Compute $B$ in a basis of $R(U)$ given by two wall relations and compare with Example 3.7.5 for $a = 1$.
3. (B) Show that the Gale dual determines $U$ up to a linear automorphism of $N_{\mathbb{R}}$: if two spanning lists $U$ and $U'$ of length $r$ in $N_{\mathbb{R}}$ have $R(U) = R(U')$, then $u'_\rho = g(u_\rho)$ for a linear automorphism $g$.
4. (B) Show that $\operatorname{Cone}(U) = N_{\mathbb{R}}$ if and only if $U$ spans $N_{\mathbb{R}}$ and $R(U)$ contains a vector with all coordinates positive.
5. (B) In the situation of Theorem 3.7.3, let $\rho$ be a ray. Show that $\beta_\rho$ spans an edge of $\operatorname{Eff}(X)$ if $D_\rho$ is contracted by a birational toric morphism to a projective toric variety, as in Theorem 3.5.15, part 4.
6. (C) Let $\Sigma$ be complete simplicial. Show that the cone $\operatorname{Mov}(X) = \bigcap_\rho \operatorname{Cone}(\beta_{\rho'} : \rho' \neq \rho)$ is the set of classes $[D]$ such that for each $\rho$ some effective torus-invariant divisor in the class does not contain $D_\rho$, and show that $\operatorname{Nef}(X) \subseteq \operatorname{Mov}(X)$.

### Lean

- Status: not yet in Lean. The library has fans, support functions and the wall relations, but no class group, no space $N^1$ and no Gale dual.
- Fidelity: a Lean form of Lemma 3.7.2 is linear algebra over $\mathbb{R}$ and needs no scheme. Part 1 of Theorem 3.7.3 with nef read as convexity of the support function, `MinimalModel.Toric.Fan.IsNef`, is also a statement on fans. Part 3 needs the global sections of $\mathcal{O}(D)$ and so the scheme $X_\Sigma$.
- No node of the map covers this section.

### Notes and history

Gale duality is named after David Gale, who used it for polytopes; its use for toric varieties goes back to the work of Oda and Park and of Gelfand, Kapranov and Zelevinsky around 1990 on the secondary fan, the subject of the next section. Cox-Little-Schenck give the duality and the description of the nef and effective cones in Chapters 14 and 15, in the language of the GKZ cones. The proofs here were written for the handbook from the definitions; the only inputs are the class group sequence, the convexity criterion of Chapter 4, and the fact from Cox-Little-Schenck, Chapter 4, that the sections of $\mathcal{O}(D)$ on a toric variety are spanned by characters. Fujino and Sato (2004) work with $N^1$ and $N_1$ directly, which is the same picture seen from the curve side.
