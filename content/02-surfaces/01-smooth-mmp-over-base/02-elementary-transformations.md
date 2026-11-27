---
title: Mori fibre spaces over curves and elementary transformations
nodes: []
sources: [Har77, Bea96, Mat02, Rei97]
reads_with: [Har77:V.5, Bea96:ch3, Mat02:ch1]
requires: [P3.11, P5.5, P5.6, P5.7, P5.8, P5.9, P5.11, P5.12]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Mori fibre spaces over curves and elementary transformations

### Statement

A Mori fibre space over a curve, case 2 of Theorem 2.1.6, is a $\mathbb{P}^1$-bundle. This section studies the birational maps between them over the same curve. The basic move is the elementary transformation of Proposition P5.9.10, which is there defined for the Hirzebruch surfaces and is here defined over any curve and followed through its effect on sections.

**Definition 2.1.10 ($\mathbb{P}^1$-fibrations and elementary transformations).** A *$\mathbb{P}^1$-fibration* is a surjective morphism $p \colon X \to B$ from a smooth projective surface onto a smooth projective curve all of whose closed scheme-theoretic fibres $X_b = p^* b$ are isomorphic to $\mathbb{P}^1$. Let $x \in X$ be a closed point over $b \in B$, let $\pi \colon Y = \operatorname{Bl}_x X \to X$ be the blow-up with exceptional curve $E$, and let $\tilde F \subseteq Y$ be the strict transform of $X_b$. The *elementary transformation* of $X$ at $x$ is the surface $\operatorname{elm}_x X$ obtained by contracting $\tilde F$, with the birational map $\varepsilon_x = c \circ \pi^{-1} \colon X \dashrightarrow \operatorname{elm}_x X$, where $c \colon Y \to \operatorname{elm}_x X$ is the contraction.

By part 1 of Proposition P5.9.16, a $\mathbb{P}^1$-fibration has $p_* \mathcal{O}_X = \mathcal{O}_B$. By Theorem P5.9.18 it has a section, so by Proposition P5.9.5 it is a geometrically ruled surface $\mathbb{P}(\mathcal{E})$ over $B$, and $\rho(X) = 2$ by Theorem P5.9.4. A *section* of $p$ is identified with its image, an integral curve $\sigma$ with $\sigma \cdot F = 1$.

**Proposition 2.1.11 (elementary transformations).** Let $p \colon X \to B$ be a $\mathbb{P}^1$-fibration, $x \in X$ a closed point over $b$, and $Y$, $E$, $\tilde F$, $c$ as in Definition 2.1.10.

1. $\tilde F$ is a $(-1)$-curve, its contraction $c \colon Y \to X' = \operatorname{elm}_x X$ exists, and there is a unique morphism $p' \colon X' \to B$ with $p' \circ c = p \circ \pi$. It is a $\mathbb{P}^1$-fibration, and its fibre over $b$ is the image $E'$ of $E$.
2. Let $x' = c(\tilde F) \in E'$. Then $\operatorname{elm}_{x'} X' = X$: the morphism $c$ is the blow-up of $x'$ with exceptional curve $\tilde F$, the strict transform of $X'_b$ is $E$, and its contraction is $\pi$. So $\varepsilon_{x'} \circ \varepsilon_x = \mathrm{id}_X$.
3. $\varepsilon_x$ is an isomorphism from $X \setminus X_b$ onto $X' \setminus X'_b$ over $B \setminus \{b\}$, a morphism on $X \setminus \{x\}$ that maps $X_b \setminus \{x\}$ to the point $x'$, and it is not defined at $x$.
4. For every section $\sigma$ of $X$, the image $\sigma'$ of its strict transform is a section of $X'$, and every section of $X'$ arises from exactly one section of $X$. If $x \in \sigma$, then $\sigma'^2 = \sigma^2 - 1$ and $x' \notin \sigma'$. If $x \notin \sigma$, then $\sigma'^2 = \sigma^2 + 1$ and $x' \in \sigma'$.
5. $K_{X'}^2 = K_X^2 = 8(1 - g(B))$.

Lean: not yet in Lean.

**Corollary 2.1.12 (elementary transformations of Hirzebruch surfaces).** Let $n \geq 0$ and let $x \in F_n$ be a closed point.

1. For every $m \geq 0$, the smallest self-intersection of a section of $F_m$ is $-m$. It is attained by $C_-$, and for $m \geq 1$ only by $C_-$.
2. If $x \in C_-$, then $\operatorname{elm}_x F_n \cong F_{n+1}$.
3. If $x \notin C_-$ and $n \geq 1$, then $\operatorname{elm}_x F_n \cong F_{n-1}$.
4. If $n = 0$, then $\operatorname{elm}_x F_0 \cong F_1$ for every $x$.

Lean: not yet in Lean.

The isomorphisms are over $\mathbb{P}^1$. Proposition P5.9.10 proves parts 2 to 4 by explicit formulas in the charts of Definition P3.11.24; the proof below reads them off from part 4 of Proposition 2.1.11.

**Theorem 2.1.13 (factorization into elementary transformations).** Let $p_1 \colon X_1 \to B$ and $p_2 \colon X_2 \to B$ be $\mathbb{P}^1$-fibrations over the same curve, and $\varphi \colon X_1 \dashrightarrow X_2$ a birational map with $p_2 \circ \varphi = p_1$. Let $W$ be a smooth projective surface with composites of point blow-ups $\pi_i \colon W \to X_i$ and $\pi_2 = \varphi \circ \pi_1$, which exists by Theorem P5.7.13. Then there are elementary transformations $\varepsilon_1, \dots, \varepsilon_N$, with $N \leq \rho(W) - 2$, and an isomorphism $\alpha$ over $B$ with $$\varphi = \alpha \circ \varepsilon_N \circ \dots \circ \varepsilon_1.$$ Each $\varepsilon_j$ is centred at a point over a point of $B$ over which $\varphi$ is not an isomorphism.

Lean: not yet in Lean.

### Proof in words

Blowing up a point of a fibre of a $\mathbb{P}^1$-bundle breaks the fibre into two $(-1)$-curves meeting once. Either one can be contracted. Contracting the new curve gives back the bundle, and contracting the old fibre gives a new bundle, in which the exceptional curve has become the fibre and the old fibre has become a point. The same picture read backwards shows that the inverse of an elementary transformation is again one. A section through the centre loses a point of contact with the contracted curve and its square drops by one. A section not through the centre gains one and its square rises by one. On $F_n$ the negative section has the smallest square, which is $-n$, so this rule decides the new Hirzebruch surface without coordinates.

For the factorization, resolve the map by blow-ups on both sides. Look at the last curve $A$ blown up on the target side. If the source side also contracts $A$, then $A$ can be contracted on the common resolution. If not, $A$ maps onto a fibre of the source, and the fibre of the target over the same point has a strict transform that the source contracts to a point $x$. The elementary transformation at $x$ turns the image of $A$ into a point, and then $A$ can be contracted. In both cases the common resolution gets smaller, and when it has Picard number $2$ the map is an isomorphism.

### Examples

**Example 2.1.14 (chains of Hirzebruch surfaces).** By Corollary 2.1.12, every elementary transformation changes the index $n$ of $F_n$ by exactly $1$. So a factorization $\varphi = \alpha \circ \varepsilon_N \circ \dots \circ \varepsilon_1$ of a birational map $F_n \dashrightarrow F_m$ over $\mathbb{P}^1$ has $N \geq |n - m|$ and $N \equiv n - m \pmod 2$. For instance $F_0 \dashrightarrow F_3$ is the composite of three elementary transformations at points of the negative sections, in distinct fibres or in the same fibre: on $F_0$ any point $x_1$, on $F_1$ the point $x_2 = C_- \cap F_{c_2}$, on $F_2$ the point $x_3 = C_- \cap F_{c_3}$. Track the section $\sigma = C_-$ of $F_0$ through $x_1$: its squares are $0, -1, -2, -3$, and it ends as the negative section of $F_3$. Track the section $\tau = C_+$ of $F_0$, which has $\tau^2 = 0$ and avoids $x_1$ when $x_1 \in C_-$: in each step $\tau$ does not pass through the centre, which lies on the negative section, so its squares are $0, 1, 2, 3$, and it ends in the class $C_+$ of $F_3$. In the other direction, starting from $F_n$ with $n \geq 1$ and taking $n$ centres off the negative sections gives $F_n \dashrightarrow F_0$. The map $\varepsilon_y \circ \varepsilon_x \colon F_n \dashrightarrow F_n$, with $x \in C_-$ over $c$ and $y \notin C_-$ over $d \neq c$, is a birational self-map over $\mathbb{P}^1$ that is not an isomorphism, since it contracts the fibre over $c$ to a point.

**Example 2.1.15 (the parity of a ruled surface).** Let $p \colon X \to B$ be a $\mathbb{P}^1$-fibration. By Theorem P5.9.4, $\operatorname{Num}(X) = \mathbb{Z} \sigma_0 \oplus \mathbb{Z} F$ for a section $\sigma_0$, so every section $\sigma$ has $\sigma \equiv \sigma_0 + a F$ with $a \in \mathbb{Z}$ and $\sigma^2 = \sigma_0^2 + 2a$. So the parity $\epsilon(X) \in \mathbb{Z}/2$ of $\sigma^2$ does not depend on $\sigma$. For $X = \mathbb{P}(\mathcal{E})$ it is the parity of $e(X)$ and of $\deg \mathcal{E}$, as in Example P5.9.23. By part 4 of Proposition 2.1.11, $\epsilon(\operatorname{elm}_x X) = \epsilon(X) + 1$. So in Theorem 2.1.13, $N \equiv \epsilon(X_1) + \epsilon(X_2) \pmod 2$. Over an elliptic curve $C$, the product $C \times \mathbb{P}^1$ has $\epsilon = 0$ and the surface of Example P5.9.13 has $e = -1$, so $\epsilon = 1$, and any birational map between them over $C$ needs an odd number of elementary transformations. The elementary transformation of $C \times \mathbb{P}^1$ at a point $x$ is the surface $S'$ of Example P5.9.23: the section $C \times \{t\}$ through $x$ becomes a section of square $-1$, and every section $C \times \{t'\}$ with $t' \neq t$ becomes a section of square $1$.

### Proof

*Proof of Proposition 2.1.11.* (1) The fibre $X_b$ is smooth at $x$, so $\pi^* X_b = \tilde F + E$ by part 2 of Proposition P5.6.4, and $\tilde F^2 = X_b^2 - 1 = -1$ by part 4. As $\tilde F \cong X_b \cong \mathbb{P}^1$, it is a $(-1)$-curve, and Theorem P5.7.4 gives its contraction $c$. Let $b_0 \neq b$. The fibration $p \circ \pi \colon Y \to B$ has the fibre $Y_{b_0} \cong X_{b_0} \cong \mathbb{P}^1$, and $\tilde F$ lies in the fibre over $b$, so part 5 of Proposition P5.9.16 gives a unique $p'$ with $p' \circ c = p \circ \pi$. Over $B \setminus \{b\}$, both $\pi$ and $c$ are isomorphisms, so $X'_{b'} \cong X_{b'} \cong \mathbb{P}^1$ for $b' \neq b$. Over $b$, $c^* X'_b = \pi^* X_b = \tilde F + E$. Since $E \cdot \tilde F = (\pi^* X_b - E) \cdot E = 1$, the image $E' = c(E)$ has $c^* E' = E + \tilde F$ by parts 2 and 3 of Proposition P5.6.4, applied to the blow-up $c$ of $x' = c(\tilde F)$ given by Definition P5.7.1, since $E$ is smooth and meets $\tilde F$ once. As $c^*$ is injective on $\operatorname{Pic}$, $X'_b = E'$, an integral fibre, which is isomorphic to $\mathbb{P}^1$ by part 3 of Proposition P5.9.16. So $p'$ is a $\mathbb{P}^1$-fibration.

(2) By Definition P5.7.1 the contraction $c$ comes with an isomorphism $Y \cong \operatorname{Bl}_{x'} X'$ over $X'$ carrying $\tilde F$ to the exceptional curve. The total transform of $X'_b = E'$ is $c^* E' = E + \tilde F$, so the strict transform of $X'_b$ is $E$, and its contraction is $\pi$, by the uniqueness in part 1 of Corollary P5.7.5. So $\operatorname{elm}_{x'} X' = X$ and $\varepsilon_{x'} = \pi \circ c^{-1} = \varepsilon_x^{-1}$.

(3) Over $B \setminus \{b\}$ the maps $\pi$ and $c$ are isomorphisms. On $X \setminus \{x\}$, $\pi^{-1}$ is an isomorphism onto $Y \setminus E$, so $\varepsilon_x = c \circ \pi^{-1}$ is a morphism there, and it maps $X_b \setminus \{x\} = \pi(\tilde F \setminus E)$ to $c(\tilde F) = x'$. If $\varepsilon_x$ were defined at $x$, it would be a birational morphism $X \to X'$ of surfaces with $\rho(X) = \rho(X') = 2$, hence an isomorphism by parts 1 and 2 of Theorem P5.7.12, but it contracts the curve $X_b$.

(4) Let $\sigma$ be a section. If $x \in \sigma$, its strict transform is $\tilde \sigma = \pi^* \sigma - E$, with $\tilde \sigma^2 = \sigma^2 - 1$ and $\tilde \sigma \cdot \tilde F = (\pi^* \sigma - E) \cdot (\pi^* X_b - E) = 1 - 1 = 0$, so $\tilde \sigma \cap \tilde F = \emptyset$ by Proposition P5.5.5. Then Lemma P5.12.22 gives $\sigma'^2 = \tilde \sigma^2 = \sigma^2 - 1$, and $x' = c(\tilde F) \notin \sigma' = c(\tilde \sigma)$. If $x \notin \sigma$, then $\tilde \sigma = \pi^* \sigma$, $\tilde \sigma \cdot \tilde F = \sigma \cdot X_b = 1$, so $c^* \sigma' = \tilde \sigma + \tilde F$ by parts 2 and 3 of Proposition P5.6.4 applied to the blow-up $c$, and $\sigma'^2 = \tilde \sigma^2 + 2 \tilde \sigma \cdot \tilde F + \tilde F^2 = \sigma^2 + 2 - 1 = \sigma^2 + 1$; and $x' \in \sigma'$ as $\tilde \sigma$ meets $\tilde F$. In both cases $\sigma'$ is an integral curve with $\sigma' \cdot X'_{b'} = \sigma \cdot X_{b'} = 1$ for $b' \neq b$, computed where $\varepsilon_x$ is an isomorphism, so it is a section. Applying the same construction to $\varepsilon_{x'}$, by (2), shows that every section of $X'$ is the image of exactly one section of $X$.

(5) Blowing up lowers $K^2$ by $1$ and contracting a $(-1)$-curve raises it by $1$, by part 3 of Corollary P5.7.5. For a $\mathbb{P}^1$-fibration with a section $\sigma$, Theorem P5.9.4 gives $K \equiv -2 \sigma + (2g - 2 + \sigma^2) F$, with $g = g(B)$, so $K^2 = 4 \sigma^2 - 4(2g - 2 + \sigma^2) = 8(1 - g)$. $\square$

*Proof of Corollary 2.1.12.* (1) For $m \geq 1$, part 2 of Proposition P5.9.8 with $e = m$ (part 1 of Proposition P5.9.9) says that every section $\sigma \neq C_-$ has $\sigma^2 \geq m > 0$, while $C_-^2 = -m$. For $m = 0$, part 1 of Proposition P5.9.8 gives $\sigma \equiv C_- + b F$ with $b \geq 0$, so $\sigma^2 = 2b \geq 0 = C_-^2$.

Let $X' = \operatorname{elm}_x F_n$. It is a $\mathbb{P}^1$-fibration over $\mathbb{P}^1$ with a section by Proposition 2.1.11, so it is geometrically ruled over $\mathbb{P}^1$ by Proposition P5.9.5, and $X' \cong F_m$ over $\mathbb{P}^1$ for some $m \geq 0$ by part 1 of Proposition P5.9.9. By (1), $-m$ is the smallest square of a section of $X'$, and by part 4 of Proposition 2.1.11 the squares of the sections of $X'$ are the numbers $\sigma^2 - 1$ for the sections $\sigma \ni x$ of $F_n$ and $\sigma^2 + 1$ for the sections $\sigma \not\ni x$.

(2) If $x \in C_-$, then $C_-'^2 = -n - 1$. Every other section of $F_n$ has square at least $-n$ by (1), so its image has square at least $-n - 1$. So $m = n + 1$.

(3) If $x \notin C_-$ and $n \geq 1$, then $C_-'^2 = -n + 1$, and every other section has square at least $n$ by (1), so its image has square at least $n - 1 \geq -n + 1$. So $m = n - 1$.

(4) If $n = 0$, the fibre of the second projection $F_0 = \mathbb{P}^1 \times \mathbb{P}^1 \to \mathbb{P}^1$ through $x$ is a section of square $0$ through $x$, whose image has square $-1$, and every image has square at least $0 - 1 = -1$. So $m = 1$. $\square$

*Proof of Theorem 2.1.13.* The morphisms $p_1 \circ \pi_1$ and $p_2 \circ \pi_2 = p_2 \circ \varphi \circ \pi_1$ agree as rational maps from the integral scheme $W$ to the separated scheme $B$, so they are equal; call this morphism $q$. Induct on $\rho(W)$. By parts 1 and 2 of Theorem P5.7.12, $\pi_i$ is a composite of $\rho(W) - \rho(X_i) = \rho(W) - 2$ blow-ups. If $\rho(W) = 2$, both $\pi_i$ are isomorphisms, and $\varphi = \pi_2 \circ \pi_1^{-1}$ is an isomorphism over $B$.

Let $\rho(W) > 2$. Let $A$ be the exceptional curve of the last blow-up in $\pi_2$, a $(-1)$-curve, $\mu \colon W \to W'$ its blow-down, and $\pi_2 = \pi'_2 \circ \mu$. Then $\rho(W') = \rho(W) - 1$, and $q(A)$ is a point $b$, since $\pi_2(A)$ is a point.

*Case 1: $\pi_1$ contracts $A$.* By Lemma P5.11.16, $\pi_1 = \pi'_1 \circ \mu$ for a morphism $\pi'_1 \colon W' \to X_1$. Then $\pi'_1$ and $\pi'_2$ are birational morphisms of smooth projective surfaces, hence composites of point blow-ups by part 1 of Theorem P5.7.12, and $\pi'_2 \circ \mu = \varphi \circ \pi'_1 \circ \mu$ gives $\pi'_2 = \varphi \circ \pi'_1$, as $\mu$ is surjective. The induction hypothesis applies to $W'$.

*Case 2: $\pi_1$ does not contract $A$.* Then $\pi_1(A)$ is an integral curve in the integral fibre $(X_1)_b$, so $\pi_1(A) = (X_1)_b$. The support of the fibre $W_b = q^* b$ maps onto $(X_2)_b$ under $\pi_2$, so some component $G$ of $W_b$ has $\pi_2(G) = (X_2)_b$, and $G \neq A$. The morphism $\pi_1$ is an isomorphism over the complement of a finite set $\Sigma \subseteq X_1$ by part 1 of Theorem P5.8.3, so $\pi_1^{-1}((X_1)_b \setminus \Sigma)$ is irreducible, and $A$ is the only component of $W_b$ that maps onto $(X_1)_b$. So $\pi_1(G)$ is a point $x \in (X_1)_b$, the fibre $\pi_1^{-1}(x) \supseteq G$ is not finite, and $\pi_1^{-1}$ is not defined at $x$ by part 1 of Lemma P5.7.10. By Proposition P5.7.11, $\pi_1 = \beta \circ \nu$ with $\beta \colon Y = \operatorname{Bl}_x X_1 \to X_1$ and $\nu \colon W \to Y$. The curve $\nu(A)$ is not a point and maps onto $(X_1)_b$, and $\beta$ is an isomorphism off the exceptional curve, so $\nu(A) = \tilde F$, the strict transform of $(X_1)_b$. Let $c \colon Y \to X'_1 = \operatorname{elm}_x X_1$ be the contraction of $\tilde F$ and $\varepsilon = \varepsilon_x = c \circ \beta^{-1}$. The birational morphism $c \circ \nu \colon W \to X'_1$ contracts $A$, so by Lemma P5.11.16 it factors as $c \circ \nu = \pi'_1 \circ \mu$, and $\pi'_1 \colon W' \to X'_1$ is a composite of point blow-ups by Theorem P5.7.12. Let $\varphi' = \varphi \circ \varepsilon^{-1} \colon X'_1 \dashrightarrow X_2$. Then $p_2 \circ \varphi' = p_1 \circ \varepsilon^{-1} = p'_1$, where $p'_1$ is the fibration of $X'_1$, and $\varphi' \circ \pi'_1 \circ \mu = \varphi \circ \varepsilon^{-1} \circ c \circ \nu = \varphi \circ \beta \circ \nu = \varphi \circ \pi_1 = \pi_2 = \pi'_2 \circ \mu$, so $\varphi' \circ \pi'_1 = \pi'_2$. The induction hypothesis applies to $\varphi'$ and $W'$ and gives $\varphi' = \alpha \circ \varepsilon_N \circ \dots \circ \varepsilon_2$, so $\varphi = \varphi' \circ \varepsilon$ is of the required form with $\varepsilon_1 = \varepsilon$.

Each step lowers $\rho(W)$ by $1$ and contributes at most one elementary transformation, so $N \leq \rho(W) - 2$. The centre $x$ in Case 2 lies over $b = q(A)$, and $\varphi$ is not an isomorphism over any neighbourhood $U$ of $b$: otherwise $\pi_2 = \varphi \circ \pi_1$ would contract over $U$ exactly the curves that $\pi_1$ contracts, but $\pi_2$ contracts $A$ and $\pi_1$ does not. In Case 1 no elementary transformation is introduced. $\square$

### Exercises

1. (A) Let $x \in F_0 = \mathbb{P}^1 \times \mathbb{P}^1$ and $\sigma_t = \mathbb{P}^1 \times \{t\}$ the sections of the first projection. Compute the squares of the images of all $\sigma_t$ and of a section of class $C_- + F$ through $x$ in $\operatorname{elm}_x F_0$, and confirm that $\operatorname{elm}_x F_0 \cong F_1$.
2. (A) Write a birational map $F_3 \dashrightarrow F_0$ over $\mathbb{P}^1$ as a composite of three elementary transformations, and show that no factorization has fewer. Show that a birational map $F_3 \dashrightarrow F_3$ over $\mathbb{P}^1$ which is not an isomorphism needs at least two.
3. (B) Let $x, y$ be closed points of a $\mathbb{P}^1$-fibration $X \to B$ over distinct points of $B$, and let $y_1$ be the image of $y$ in $\operatorname{elm}_x X$ and $x_1$ the image of $x$ in $\operatorname{elm}_y X$. Show that $\operatorname{elm}_{y_1} \operatorname{elm}_x X$ and $\operatorname{elm}_{x_1} \operatorname{elm}_y X$ are isomorphic over $B$, by an isomorphism compatible with the maps from $X$.
4. (B) Let $X \to B$ be a $\mathbb{P}^1$-fibration with a section $\sigma$ through $x$, and $X' = \operatorname{elm}_x X$. Express $K_{X'}$ in terms of $\sigma'$ and $F$, and check that the formula of Theorem P5.9.4 gives the same class.
5. (B) Let $x, x'$ be two points of the same fibre of a $\mathbb{P}^1$-fibration $X \to B$, with $x' \neq x$, and let $x_1$ be the image of $x'$ in $\operatorname{elm}_x X$. Show that $x_1$ is the point $c(\tilde F)$ of Proposition 2.1.11, so that $\operatorname{elm}_{x_1} \operatorname{elm}_x X = X$. For $X = F_n$ and $x \in C_-$, show that the point where the negative section of $\operatorname{elm}_x F_n \cong F_{n+1}$ meets $E'$ differs from $x_1$, and that the elementary transformation there gives $F_{n+2}$.
6. (C) Let $\varphi \colon F_0 \dashrightarrow F_0$ be given by $(r, t) \mapsto (r + t^{-1}, t)$ in the affine coordinates $r$ on the fibres and $t$ on the base. Show that $\varphi$ is a birational map over $\mathbb{P}^1$ which is an isomorphism over $\mathbb{P}^1 \setminus \{0\}$ and not an isomorphism, and deduce from Theorem 2.1.13 and Example 2.1.15 that every factorization of $\varphi$ uses an even number, at least two, of elementary transformations centred over $0$.

### Lean

The statements of this section are not yet in Lean. The library `mmp-lean` has no ruled surfaces and no elementary transformations; its statement `MinimalModel.SurfaceMMP` in `MinimalModel/Statements/LowDim.lean` mentions Mori fibre spaces through the predicate `IsMoriFibreSpace` of `MinimalModel/Statements/Basic.lean`, without the structure of a $\mathbb{P}^1$-bundle.

### Notes and history

Elementary transformations go back to the Italian school, and Nagata used them in 1960 to classify the rational ruled surfaces and to construct ruled surfaces with prescribed invariants; Hartshorne, Example V.5.7.1, and Beauville, Chapter III, treat them as here. Theorem 2.1.13 is the classical statement that the birational maps between ruled surfaces over a curve are generated by elementary transformations, and in the language of the minimal model program it is the two-dimensional case of the Sarkisov program: elementary transformations are the links of type II between Mori fibre spaces over the same base, and the blow-down $F_1 \to \mathbb{P}^2$ and its inverse are the links of types III and I. Matsuki, Chapter 13, and Corti's 1995 paper treat the Sarkisov program in dimensions 2 and 3. The literature state of the results of this section is theorem.
