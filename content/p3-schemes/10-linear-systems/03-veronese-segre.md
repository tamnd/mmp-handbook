---
title: The Veronese and Segre embeddings
nodes: []
sources: [Vak25, Har77, GW20, Stacks]
reads_with: [Vak25:ch16, Har77:II.7, GW20:ch13]
requires: [P3.3, P3.4, P3.6]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The Veronese and Segre embeddings

### Statement

Let $A$ be a ring. On $\mathbb{P}^n_A$ use coordinates $x_0, \dots, x_n$, and for a multi-index $\alpha \in \mathbb{N}^{n + 1}$ with $|\alpha| = \sum \alpha_i = d$ write $x^\alpha = \prod x_i^{\alpha_i}$. Let $e_i$ be the $i$-th unit vector, so $x^{d e_i} = x_i^d$. On $P = \mathbb{P}^n_A \times_A \mathbb{P}^m_A$ with projections $p, q$ and coordinates $x_i$, $y_j$, put $\mathcal{O}(a, b) = p^* \mathcal{O}(a) \otimes q^* \mathcal{O}(b)$.

**Definition P3.10.18 (Veronese and Segre maps).**

1. For $d \geq 1$ let $N = \binom{n + d}{d} - 1$ and let $\mathbb{P}^N_A$ have coordinates $z_\alpha$, $|\alpha| = d$. The *Veronese map* $v_d \colon \mathbb{P}^n_A \to \mathbb{P}^N_A$ is the morphism of the sections $x^\alpha$ of $\mathcal{O}(d)$, so $v_d^* z_\alpha = x^\alpha$.
2. Let $\mathbb{P}^{nm + n + m}_A$ have coordinates $z_{ij}$, $0 \leq i \leq n$, $0 \leq j \leq m$. The *Segre map* $\sigma \colon \mathbb{P}^n_A \times_A \mathbb{P}^m_A \to \mathbb{P}^{nm + n + m}_A$ is the morphism of the sections $x_i y_j = p^* x_i \otimes q^* y_j$ of $\mathcal{O}(1, 1)$, so $\sigma^* z_{ij} = x_i y_j$.

These sections generate, since $x_i^d$ does not vanish on $D_+(x_i)$ and $x_i y_j$ does not vanish on $D_+(x_i) \times_A D_+(y_j)$, and these open sets cover. So the maps are defined by Theorem P3.6.21.

Lean: not in Lean as stated.

**Theorem P3.10.19 (the Veronese embedding).** Let $Q_d \subseteq A[z_\alpha]$ be the set of quadrics $z_\alpha z_\beta - z_\gamma z_\delta$ with $\alpha + \beta = \gamma + \delta$.

1. $v_d$ is a closed immersion with $v_d^* \mathcal{O}(1) \cong \mathcal{O}(d)$, and it is an isomorphism onto the closed subscheme $V_+(Q_d)$.
2. For a form $F = \sum_\alpha c_\alpha x^\alpha$ of degree $d$, $v_d^{-1}(V_+(\sum c_\alpha z_\alpha)) = V_+(F)$. So the hypersurfaces of degree $d$ in $\mathbb{P}^n_A$ are the hyperplane sections of $v_d(\mathbb{P}^n_A)$.

Lean: not in Lean as stated.

**Theorem P3.10.20 (the Segre embedding).** Let $J \subseteq A[z_{ij}]$ be the ideal of the $2 \times 2$ minors $z_{ij} z_{kl} - z_{il} z_{kj}$ of the matrix $(z_{ij})$. Then $\sigma$ is a closed immersion with $\sigma^* \mathcal{O}(1) \cong \mathcal{O}(1, 1)$, and it is an isomorphism onto $V_+(J)$.

Lean: not in Lean as stated.

**Corollary P3.10.21 (consequences).**

1. The complement $\mathbb{P}^n_A \setminus V_+(F)$ of a hypersurface of degree $d \geq 1$ is affine.
2. If $X \subseteq \mathbb{P}^n_A$ and $Y \subseteq \mathbb{P}^m_A$ are closed subschemes, then $X \times_A Y$ is a closed subscheme of $\mathbb{P}^{nm + n + m}_A$. So a product of projective $A$-schemes is projective.
3. For $a, b \geq 1$, $\mathcal{O}(a, b)$ is very ample on $\mathbb{P}^n_A \times_A \mathbb{P}^m_A$.

Lean: not in Lean as stated.

### Proof in words

Both maps are given by monomials. On the chart where one monomial is invertible, the ratios of the other monomials generate the ring of the chart, so the map is a closed immersion there. The quadrics express every ratio through the ratios of the first order, which shows that the image is cut out by the quadrics. Hypersurfaces become hyperplane sections, so the complement of a hypersurface is a closed subscheme of affine space.

### Examples

**Example P3.10.22 (the twisted cubic).** For $n = 1$, $d = 3$, write $z_0, \dots, z_3$ for the coordinates of $s^3, s^2 t, s t^2, t^3$. The quadrics of $Q_3$ are generated, up to sign, by $z_0 z_2 - z_1^2$, $z_1 z_3 - z_2^2$ and $z_0 z_3 - z_1 z_2$, the $2 \times 2$ minors of
$$
\begin{pmatrix} z_0 & z_1 & z_2 \\ z_1 & z_2 & z_3 \end{pmatrix}.
$$
The twisted cubic is $V_+$ of these three quadrics. Any two of them cut out a larger scheme: $V_+(z_0 z_2 - z_1^2, z_1 z_3 - z_2^2)$ contains the line $V_+(z_1, z_2)$.

**Example P3.10.23 (the Veronese surface).** For $n = 2$, $d = 2$, $v_2 \colon \mathbb{P}^2_k \to \mathbb{P}^5_k$ has image the *Veronese surface*. The conics of $\mathbb{P}^2$ are its hyperplane sections, and the linear system $|\mathcal{O}_{\mathbb{P}^2}(2)|$ of conics is the projective space $\mathbb{P}^5$ of Theorem P3.10.3. A line $\ell \subseteq \mathbb{P}^2$ maps to a conic in a plane of $\mathbb{P}^5$, since $v_2|_\ell$ is $v_2$ for $\mathbb{P}^1$.

**Example P3.10.24 (the quadric surface).** For $n = m = 1$, $\sigma \colon \mathbb{P}^1 \times \mathbb{P}^1 \to \mathbb{P}^3$ is an isomorphism onto $Q = V_+(z_{00} z_{11} - z_{01} z_{10})$. The fibres $\{a\} \times \mathbb{P}^1$ and $\mathbb{P}^1 \times \{b\}$ map to two families of lines, the *rulings*. Two lines of the same family are disjoint, and two lines of different families meet in one point. The plane $V_+(z_{00})$ meets $Q$ in the two lines $V_+(z_{00}, z_{01})$ and $V_+(z_{00}, z_{10})$, one from each family, which is the relation $\mathcal{O}(1, 1) \cong \mathcal{O}_Q(1)$ of Example P3.9.12.

**Example P3.10.25 (the cubic scroll).** For $n = 1$, $m = 2$, $\sigma$ embeds $\mathbb{P}^1 \times \mathbb{P}^2$ into $\mathbb{P}^5$ as $V_+$ of the $2 \times 2$ minors of a $2 \times 3$ matrix. By Exercise 3 each plane $\{a\} \times \mathbb{P}^2$ maps to a plane and each line $\mathbb{P}^1 \times \{b\}$ maps to a line. So $\sigma(\mathbb{P}^1 \times \mathbb{P}^2)$ is a union of a family of planes parametrized by $\mathbb{P}^1$, and also a union of a family of lines parametrized by $\mathbb{P}^2$.

### Proof

*Proof of Theorem P3.10.19.* (1) Let $Z = V_+(Q_d)$. Every element of $Q_d$ pulls back to $x^\alpha x^\beta - x^\gamma x^\delta = 0$, so $v_d$ factors through $Z$ (part 4 of Proposition P3.6.4 and Theorem P3.6.21). By definition $v_d^* \mathcal{O}(1) \cong \mathcal{O}(d)$.

The charts. Let $W_i = Z \cap D_+(z_{d e_i})$. The preimage $v_d^{-1}(W_i)$ is the set where $x_i^d$ does not vanish, which is $D_+(x_i)$. The ring of $W_i$ is $R_i = A[z_\alpha / z_{d e_i}] / (Q_d)$, with the quadrics divided by $z_{d e_i}^2$. Let $a_j = z_{(d - 1) e_i + e_j} / z_{d e_i}$ for $j \neq i$. For $\beta$ with $|\beta| = d$, $\beta_j > 0$ and $j \neq i$, the quadric
$$
z_\beta \, z_{d e_i} - z_{\beta - e_j + e_i} \, z_{(d - 1) e_i + e_j}
$$
lies in $Q_d$, so $z_\beta / z_{d e_i} = a_j \cdot z_{\beta - e_j + e_i} / z_{d e_i}$ in $R_i$. The index $\beta - e_j + e_i$ has larger $i$-th entry, so by induction on $d - \beta_i$ every $z_\beta / z_{d e_i}$ is a monomial in the $a_j$, and the $a_j$ generate $R_i$ as an $A$-algebra. The map $R_i \to \mathcal{O}(D_+(x_i)) = A[x_j / x_i]$ sends $a_j$ to $x_j / x_i$. So the composite $A[t_j] \to R_i \to A[x_j / x_i]$, $t_j \mapsto a_j \mapsto x_j / x_i$, is an isomorphism, and $A[t_j] \to R_i$ is surjective. Both maps are then isomorphisms, and $v_d \colon D_+(x_i) \to W_i$ is an isomorphism.

The charts cover $Z$. Let $\mathfrak{p}$ be a point of $Z$, a homogeneous prime containing $Q_d$ and not the irrelevant ideal. Then some $z_\alpha \notin \mathfrak{p}$. If $\alpha \neq d e_i$ for an $i$ with $\alpha_i > 0$, choose $j \neq i$ with $\alpha_j > 0$. The quadric $z_\alpha^2 - z_{\alpha + e_i - e_j} z_{\alpha - e_i + e_j}$ lies in $Q_d$, so $z_{\alpha + e_i - e_j} \notin \mathfrak{p}$, and its index has larger $i$-th entry. Repeating, $z_{d e_i} \notin \mathfrak{p}$, so $\mathfrak{p} \in W_i$.

So $v_d \colon \mathbb{P}^n_A \to Z$ is a morphism that restricts to isomorphisms $v_d^{-1}(W_i) \to W_i$ over an open cover of $Z$, and it is an isomorphism. As $Z \to \mathbb{P}^N_A$ is a closed immersion, so is $v_d$.

(2) By part 1 of Theorem P3.10.9, which holds over $A$ with the same proof, $v_d^{-1}(V_+(\sum c_\alpha z_\alpha))$ is the locus where $\sum c_\alpha x^\alpha = F$ vanishes, and the local equations agree: on $D_+(x_i)$, $\sum c_\alpha z_\alpha / z_{d e_i}$ pulls back to $F / x_i^d$. $\square$

*Proof of Theorem P3.10.20.* Let $Z = V_+(J)$. The minors pull back to $x_i y_j x_k y_l - x_i y_l x_k y_j = 0$, so $\sigma$ factors through $Z$, and $\sigma^* \mathcal{O}(1) \cong \mathcal{O}(1, 1)$ by definition. Let $W_{ij} = Z \cap D_+(z_{ij})$, with preimage $D_+(x_i) \times_A D_+(y_j)$, whose ring is $A[x_k / x_i] \otimes_A A[y_l / y_j]$, a polynomial ring over $A$ in the $n + m$ variables $x_k/x_i$ ($k \neq i$) and $y_l / y_j$ ($l \neq j$). In the ring $R_{ij}$ of $W_{ij}$, the minor $z_{kl} z_{ij} - z_{kj} z_{il}$ gives
$$
\frac{z_{kl}}{z_{ij}} = \frac{z_{kj}}{z_{ij}} \cdot \frac{z_{il}}{z_{ij}},
$$
so $R_{ij}$ is generated by $a_k = z_{kj}/z_{ij}$ and $b_l = z_{il}/z_{ij}$. These map to $x_k/x_i$ and $y_l/y_j$, and as in the previous proof $R_{ij} \to A[x_k/x_i, y_l/y_j]$ is an isomorphism. If $\mathfrak{p} \in Z$, then $z_{ij} \notin \mathfrak{p}$ for some $i, j$, so the $W_{ij}$ cover $Z$. So $\sigma$ is an isomorphism onto $Z$, and a closed immersion. $\square$

*Proof of Corollary P3.10.21.* (1) By Theorem P3.10.19, $v_d$ identifies $\mathbb{P}^n_A \setminus V_+(F)$ with $v_d(\mathbb{P}^n_A) \cap D_+(\ell)$ for the linear form $\ell = \sum c_\alpha z_\alpha$.The open set $D_+(\ell) = \operatorname{Spec} A[z_\alpha]_{(\ell)}$ is affine for every homogeneous $\ell$ of positive degree (Theorem P3.6.3), and $v_d(\mathbb{P}^n_A) \cap D_+(\ell)$ is a closed subscheme of it, so it is affine.

(2) The product $X \times_A Y \to \mathbb{P}^n_A \times_A \mathbb{P}^m_A$ is a closed immersion, as a composite of base changes of closed immersions (Proposition P3.3.20). Composing with $\sigma$ gives a closed immersion into $\mathbb{P}^{nm + n + m}_A$.

(3) The morphism $v_a \times v_b \colon \mathbb{P}^n_A \times_A \mathbb{P}^m_A \to \mathbb{P}^{N}_A \times_A \mathbb{P}^{M}_A$ is a closed immersion by Theorem P3.10.19 and the argument of (2), and it pulls $\mathcal{O}(1, 1)$ back to $\mathcal{O}(a, b)$. Composing with the Segre map of $\mathbb{P}^N \times \mathbb{P}^M$ gives a closed immersion that pulls $\mathcal{O}(1)$ back to $\mathcal{O}(a, b)$. $\square$

### Exercises

1. (A) Show that $v_2(\mathbb{P}^1_k)$ is the conic $V_+(z_0 z_2 - z_1^2)$, and compare with Example P3.3.8.
2. (A) Write the six quadrics of $Q_2$ for $n = 2$ that generate the ideal of the Veronese surface, as the $2 \times 2$ minors of a symmetric $3 \times 3$ matrix.
3. (A) Show that the image under $\sigma$ of $\{a\} \times \mathbb{P}^m$ is a linear subspace of dimension $m$.
4. (B) Show that the rational normal curve $v_d(\mathbb{P}^1_k)$ is nondegenerate, and that for $d \geq 2$ it contains no line.
5. (B) Show that $\mathcal{O}(a, b)$ on $\mathbb{P}^1_k \times \mathbb{P}^1_k$ has $\Gamma(\mathcal{O}(a, b))$ equal to the space of bihomogeneous forms of bidegree $(a, b)$ for $a, b \geq 0$, of dimension $(a + 1)(b + 1)$.
6. (B) Let $k$ be algebraically closed. Show that a hypersurface $V_+(F) \subseteq \mathbb{P}^n_k$ of degree $d \geq 1$ meets every integral closed curve $C \subseteq \mathbb{P}^n_k$, using part 1 of Corollary P3.10.21 and Corollary P3.4.22.
7. (C) Show that the kernel of $A[z_\alpha] \to A[x_0, \dots, x_n]$, $z_\alpha \mapsto x^\alpha$, is generated by $Q_d$ when $n = 1$.

### Lean

Mathlib has products of schemes and the projective spectrum, but no Veronese or Segre morphism. The statements of this section are not in Lean as stated. The handbook adds no `MinimalModel` node here.

### Notes and history

The Veronese surface is due to Veronese, and the Segre embedding to Segre, both in the nineteenth century. Hartshorne treats them in the exercises to Section I.2, for varieties. The literature state is theorem. In the minimal model program the Segre embedding proves that products of projective varieties are projective, which is used for fibre products of contractions, and the Veronese embedding replaces a divisor $D$ by $dD$ when a statement about very ample divisors has to be applied to an ample one. Part 1 of Corollary P3.10.21 shows that the complement of an ample divisor is affine in the case of $\mathbb{P}^n$.
