---
title: The contraction theorem
nodes: [MMQ2K4RSHT]
sources: [KM98, KMM87, Mat02]
reads_with: [KM98:3.7, Mat02:ch8, KMM87:3-2]
requires: [P4.6, P7.1, P7.3, P7.4, 7.4]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The contraction theorem

### Statement

Let $(X, \Delta)$ be a projective klt pair over a field of characteristic $0$, with $\Delta$ a $\mathbb{Q}$-divisor and $K_\Delta$ the class of $K_X + \Delta$, as in Chapter 4. The cone theorem of Chapter 4 cuts out every $K_\Delta$-negative extremal face $F$ by a nef Cartier divisor $L$ with $L - K_\Delta$ ample (Corollary 7.4.7). The base point free theorem of Chapter 2 makes $|mL|$ free, and Stein factorization turns the morphism it defines into the contraction of $F$. A *contraction* is a projective surjective morphism $\varphi \colon X \to Y$ with $\varphi_* \mathcal{O}_X = \mathcal{O}_Y$ (Definition P4.6.14). For a contraction the fibres are connected, by Theorem P4.6.15.

**Lemma 7.5.1 (factorization through a contraction).** Let $g \colon X \to Y$ be a contraction of projective varieties and $h \colon X \to Z$ a morphism to a projective variety. Suppose that every curve contracted by $g$ is contracted by $h$. Then there is a unique morphism $h' \colon Y \to Z$ with $h = h' \circ g$.

Lean: not yet in Lean.

**Theorem 7.5.2 (the contraction theorem).** Let $F$ be a $K_\Delta$-negative extremal face of $\overline{NE}(X)$. There is a contraction $\varphi = \varphi_F \colon X \to Y$ onto a normal projective variety $Y$ such that:

1. an integral curve $C \subseteq X$ is contracted by $\varphi$ if and only if $[C] \in F$, so that $F = F_\varphi$;
2. if $M$ is a line bundle on $X$ with $M \cdot C = 0$ for every curve $C$ with $[C] \in F$, then $M \cong \varphi^* M_Y$ for a line bundle $M_Y$ on $Y$, unique up to isomorphism;
3. $\varphi^* \colon N^1(Y) \to N^1(X)$ is injective with image $F^\perp$, so $\rho(Y) = \rho(X) - \dim \operatorname{span} F$;
4. $\varphi$ is unique: if $\varphi' \colon X \to Y'$ is a contraction onto a projective variety that contracts exactly the curves with class in $F$, there is a unique isomorphism $\iota \colon Y \to Y'$ with $\varphi' = \iota \circ \varphi$.

Lean: `MinimalModel.ContractionTheorem`, in the project library, states the existence of the contraction of a $K_\Delta$-negative extremal ray, without proof.

**Corollary 7.5.3 (the contraction of a ray).** Let $R$ be a $K_\Delta$-negative extremal ray, $\varphi = \varphi_R \colon X \to Y$ its contraction and $C$ a curve with $[C] \in R$. Then $\rho(Y) = \rho(X) - 1$ and the sequence
$$0 \to \operatorname{Pic}(Y) \xrightarrow{\varphi^*} \operatorname{Pic}(X) \xrightarrow{\, \cdot C \,} \mathbb{Z}$$
is exact.

Lean: not yet in Lean.

**Corollary 7.5.4 (the relative contraction).** Let $f \colon X \to S$ be a morphism to a projective variety and $F$ a $K_\Delta$-negative extremal face of $\overline{NE}(X/S)$. Then $F$ is a $K_\Delta$-negative extremal face of $\overline{NE}(X)$, and $f = g \circ \varphi_F$ for a unique morphism $g \colon Y \to S$.

Lean: not yet in Lean.

### Proof in words

Lemma 7.5.1 compares $g$ with the graph of $(g, h)$: the projection of the graph to $Y$ has single points as fibres, since the connected fibres of $g$ are crushed by $h$, so it is finite, and $g_* \mathcal{O}_X = \mathcal{O}_Y$ forces it to be an isomorphism. For the theorem, the supporting divisor $L$ of Corollary 7.4.7 has $L - K_\Delta$ ample, so the base point free theorem applies to $L$, and the Stein factorization of the morphism of $|mL|$ is the contraction. A curve is contracted exactly when $L$ is zero on it, that is when its class lies in $F_L = F$. For part 2, the same corollary makes $kL + M$ nef with $kL + M - K_\Delta$ ample for every large $k$. The base point free theorem then shows that $m(kL + M)$ is a pullback from $Y$ for all large $m$, by Lemma 7.5.1. Taking differences for $m$ and $m + 1$, and for $k$ and $k + 1$, shows that $L$ and $M$ are pullbacks. Parts 3 and 4 are linear algebra and Lemma 7.5.1.

### Examples

**Example 7.5.5 (the two contractions of $\mathbb{P}^1 \times \mathbb{P}^2$).** Let $X = \mathbb{P}^1 \times \mathbb{P}^2$, $\Delta = 0$, with the notation of Example 7.4.10. The cone is $\langle f, g \rangle$, both rays are $K_X$-negative, and $X$ is Fano. The supporting divisor $h_1$ of $\mathbb{R}_{\ge 0} [f]$ is free, and the contraction is $p_1 \colon X \to \mathbb{P}^1$, with $\operatorname{Pic}(\mathbb{P}^1) = \mathbb{Z} \to \operatorname{Pic}(X) = \mathbb{Z} h_1 \oplus \mathbb{Z} h_2 \to \mathbb{Z}$, $(\alpha, \beta) \mapsto \beta$, exact as in Corollary 7.5.3. The other ray gives $p_2$. The whole cone, a face of dimension $2$, has the contraction $X \to \operatorname{Spec} k$, with $\rho = 2 - 2 = 0$.

**Example 7.5.6 (the contraction to $\mathbb{P}(1, 1, n)$).** Let $X = \mathbb{F}_n$ with $n \ge 3$ and $\Delta = c \, C_-$ as in Example 7.4.22, so both rays are $K_\Delta$-negative. The ray $\mathbb{R}_{\ge 0} [C_-]$ is cut out by $C_+ = C_- + n F$, and its contraction is the morphism $\pi \colon \mathbb{F}_n \to \mathbb{P}(1, 1, n)$ of Example 7.4.21, which is birational with normal image, so $\pi_* \mathcal{O} = \mathcal{O}$ by Theorem P4.6.8. The sequence of Corollary 7.5.3 is
$$0 \to \operatorname{Pic}(\mathbb{P}(1, 1, n)) \to \mathbb{Z} C_- \oplus \mathbb{Z} F \to \mathbb{Z}, \qquad \alpha C_- + \beta F \mapsto \beta - n \alpha,$$
and its kernel is $\mathbb{Z} (C_- + n F) = \mathbb{Z} C_+$. So $\operatorname{Pic}(\mathbb{P}(1, 1, n)) \cong \mathbb{Z}$, generated by the class with $\pi^* = C_+$, the hyperplane class of the cone in $\mathbb{P}^{n+1}$. The Weil divisor $\ell = \pi(F)$ is not Cartier for $n \ge 2$, since $\pi^* \ell = F + \frac1n C_-$ is not integral, in accordance with part 2: the theorem describes only line bundles.

**Example 7.5.7 (the blow-down of a point).** Let $X = \operatorname{Bl}_p \mathbb{P}^d$, $d \ge 2$, with exceptional divisor $E \cong \mathbb{P}^{d-1}$, a line $e \subseteq E$ and the pullback $H$ of a hyperplane. Then $K_X = -(d + 1) H + (d - 1) E$, $-K_X \cdot e = d - 1 > 0$, and $H$ is nef with $H^\perp \cap \overline{NE}(X) = \mathbb{R}_{\ge 0} [e]$, since a curve is contracted by the blow-down exactly when it lies in $E$; for $d = 3$ this is Example 6.3.19. Since $H - K_X = (d + 2) H - (d - 1) E$ is ample, $H$ is a supporting divisor as in Corollary 7.4.7, and $|H|$ is already free, defining the blow-down $\pi \colon X \to \mathbb{P}^d$. By part 4 this is the contraction of the ray. The line bundle $E$ has $E \cdot e = -1 \ne 0$ and is not a pullback, while $\mathcal{O}_X(H)$ is.

### Proof

*Lemma 7.5.1.* Let $\Gamma \subseteq Y \times Z$ be the image of $(g, h) \colon X \to Y \times Z$, an integral closed subvariety, with $u \colon X \to \Gamma$ and projections $p \colon \Gamma \to Y$, $q \colon \Gamma \to Z$, so that $g = p \circ u$ and $h = q \circ u$. Let $y \in Y$ and $G = g^{-1}(y)$, connected by Theorem P4.6.15. Every irreducible component $G_i$ of $G$ maps to a point under $h$: otherwise there are $x_1, x_2 \in G_i$ with $h(x_1) \ne h(x_2)$, and an irreducible curve $C \subseteq G_i$ through $x_1$ and $x_2$, which exists on every irreducible projective variety, is contracted by $g$ and not by $h$. Since $G$ is connected, $h(G)$ is a single point, and $p^{-1}(y) = \{y\} \times h(G)$ is a single point. So $p$ is projective with finite fibres, hence finite by Corollary P4.6.17. The composite
$$\mathcal{O}_Y \to p_* \mathcal{O}_\Gamma \to p_* u_* \mathcal{O}_X = g_* \mathcal{O}_X = \mathcal{O}_Y$$
is the identity, and the second map is injective because $u$ is surjective and $\Gamma$ is integral. So $p_* \mathcal{O}_\Gamma = \mathcal{O}_Y$, and since $p$ is finite, hence affine, $\Gamma = \operatorname{Spec}_Y p_* \mathcal{O}_\Gamma = Y$, that is $p$ is an isomorphism. Put $h' = q \circ p^{-1}$. It is unique because $g$ is surjective and $Z$ is separated, so two morphisms agreeing after composition with $g$ agree on a dense set of the reduced $Y$, hence everywhere.

*Theorem 7.5.2, existence and part 1.* By Corollary 7.4.7 there is a nef Cartier divisor $L$ with $F_L = F$ and $L - K_\Delta$ ample. By the base point free theorem of Chapter 2, with $b = 1$, $|mL|$ is free for every $m \ge m_0$. Fix such an $m$, let $\psi \colon X \to \mathbb{P}^N$ be the morphism of $|mL|$, and let $\psi = g \circ \varphi$ be its Stein factorization (Theorem P4.6.15), with $\varphi \colon X \to Y$ a contraction onto the projective variety $Y$ (part 5 of Proposition P7.4.11) and $g$ finite. By parts 5 and 6 of Proposition P7.4.11, $F_\varphi = F_\psi = \overline{NE}(X) \cap L^\perp = F$, and by part 3 a curve is contracted by $\varphi$ if and only if its class lies in $F$. The variety $Y$ is normal: $X$ is normal, being klt, and if a rational function $s$ on $Y$ is integral over $\mathcal{O}_{Y, y}$, then $\varphi^* s$ is integral over $\mathcal{O}_X$ near $\varphi^{-1}(y)$, hence regular there, so $s \in (\varphi_* \mathcal{O}_X)_y = \mathcal{O}_{Y, y}$.

*Part 2.* Since $M \cdot C = 0$ for every curve with class in $F$, and $F$ is the closure of the cone of such classes by part 1 and the cone theorem, $M \cdot z = 0$ for all $z \in F$. By Corollary 7.4.7 there is $k_0$ such that $D_k = k L + M$ is nef and $D_k - K_\Delta$ is ample for every $k \ge k_0$. By the base point free theorem, for each $k \ge k_0$ there is $m_k$ such that $|m D_k|$ is free for every $m \ge m_k$. For such $m$, let $h \colon X \to \mathbb{P}^{N'}$ be the morphism of $|m D_k|$. Every curve $C$ contracted by $\varphi$ has $D_k \cdot C = 0$, so it is contracted by $h$ (part 6 of Proposition P7.4.11), and by Lemma 7.5.1, $h = h' \circ \varphi$. So $\mathcal{O}_X(m D_k) \cong h^* \mathcal{O}(1) \cong \varphi^* h'^* \mathcal{O}(1)$ is a pullback. Taking $m$ and $m + 1$ shows that $\mathcal{O}_X(D_k)$ is a pullback, for $k = k_0$ and $k = k_0 + 1$; the difference $\mathcal{O}_X(L)$ is then a pullback, and so is $M = D_{k_0} - k_0 L$. For uniqueness, $\varphi_* \varphi^* M_Y \cong M_Y$ by the projection formula (Proposition P2.6.30) and $\varphi_* \mathcal{O}_X = \mathcal{O}_Y$, so $M_Y \cong \varphi_* M$ is determined by $M$.

*Part 3.* If $N$ is a line bundle on $Y$ with $\varphi^* N \equiv 0$, and $C' \subseteq Y$ is an integral curve, choose an integral curve $C \subseteq X$ with $\varphi(C) = C'$, by cutting $\varphi^{-1}(C')$ with general hyperplanes. Then $0 = \varphi^* N \cdot C = \deg(C \to C') \, N \cdot C'$ by Theorem P7.1.15, so $N \equiv 0$ and $\varphi^*$ is injective on $N^1$. Its image is contained in $F^\perp$, since $\varphi^* N \cdot z = N \cdot \varphi_* z = 0$ for $z \in F = F_\varphi$. The face $F$ is spanned by finitely many rays $R_i$, each spanned by the class of a curve, by part 2 of Theorem 7.4.6 and Corollary 7.4.12, since only finitely many negative rays meet a neighbourhood of a compact slice of $F$ on which $K_\Delta$ is negative. So $F^\perp$ is defined by finitely many linear forms with rational coefficients on $N^1(X)_\mathbb{Q}$, and it is spanned by classes of Cartier divisors $M$ with $M \cdot F = 0$. Each of them is a pullback by part 2. So the image is $F^\perp$, of dimension $\rho(X) - \dim \operatorname{span} F$.

*Part 4.* Both $\varphi$ and $\varphi'$ are contractions contracting the same curves. Lemma 7.5.1, applied twice, gives $\iota \colon Y \to Y'$ and $\iota' \colon Y' \to Y$ with $\varphi' = \iota \circ \varphi$ and $\varphi = \iota' \circ \varphi'$. Then $\iota' \circ \iota \circ \varphi = \varphi$, and the uniqueness in Lemma 7.5.1 gives $\iota' \circ \iota = \operatorname{id}_Y$; in the same way $\iota \circ \iota' = \operatorname{id}_{Y'}$.

*Corollary 7.5.3.* Part 3 of the theorem gives $\rho(Y) = \rho(X) - 1$. The map $\varphi^*$ is injective on $\operatorname{Pic}$ by the uniqueness in part 2, and $\varphi^* N \cdot C = N \cdot \varphi_* C = 0$. If $M \cdot C = 0$, then $M \cdot C' = 0$ for every curve $C'$ with $[C'] \in R$, since $[C']$ is a positive multiple of $[C]$, so $M$ is a pullback by part 2.

*Corollary 7.5.4.* The first claim is part 4 of Proposition 7.4.15. Every curve contracted by $\varphi_F$ has class in $F \subseteq \overline{NE}(X/S) = F_f$, so it is contracted by $f$ by part 3 of Proposition P7.4.11. Lemma 7.5.1 gives $g$.

### Exercises

1. (A) For $X = \mathbb{P}^1 \times \mathbb{P}^1 \times \mathbb{P}^1$, list the $K_X$-negative extremal faces and their contractions, and check part 3 of Theorem 7.5.2 for each.
2. (A) In Example 7.5.7, show directly that $\operatorname{Pic}(X) = \mathbb{Z} H \oplus \mathbb{Z} E$ and that the kernel of $M \mapsto M \cdot e$ is $\mathbb{Z} H$.
3. (B) Show that Lemma 7.5.1 fails without $g_* \mathcal{O}_X = \mathcal{O}_Y$: take $g$ the normalization of a nodal cubic and $h$ the identity.
4. (B) Let $\varphi \colon X \to Y$ be the contraction of a $K_\Delta$-negative extremal face. Show that $-K_\Delta$ is $\varphi$-ample, that is, positive on $\overline{NE}(X/Y) \setminus \{0\}$.
5. (B) In Example 7.5.6, show that the ray $\mathbb{R}_{\ge 0} [F]$ is cut out by $F$ and that its contraction is the ruling $q$; deduce that $\mathbb{F}_n$ with $c \, C_-$ has exactly three nonzero negative faces, and find the contraction of each.
6. (C) Let $\varphi \colon X \to Y$ be the contraction of a $K_\Delta$-negative extremal face $F$ and $G \subseteq F$ a face of $F$. Show that $\varphi_F = \psi \circ \varphi_G$ for a unique contraction $\psi$, and identify the face of $\psi$ with the image of $F$ in $N_1(Y_G)$.

### Lean

The library has `MinimalModel.ContractionTheorem` for projective klt pairs in characteristic $0$, as a statement without proof, and `MinimalModel.BasepointFree`, the base point free theorem, in the same form. Lemma 7.5.1 and the corollaries are not yet in Lean.

### Notes and history

The contraction theorem is due to Kawamata and Shokurov, as a consequence of the base point free theorem, Shokurov's nonvanishing and Kawamata's rationality theorem; the standard references are KMM87 and KM98, Theorem 3.7, parts 3 and 4. For smooth threefolds Mori constructed the contractions directly from the classification of extremal rays (Theorem 6.3.9). The method of part 2, comparing $m$ and $m + 1$, is the usual way to show that a divisor which is numerically trivial on a face descends.
