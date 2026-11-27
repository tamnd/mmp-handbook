---
title: Minimal models of surfaces
nodes: []
sources: [Har77, Bea96, Rei97, SGA6]
reads_with: [Har77:V.5, Bea96:ch2, Rei97:ch2]
requires: [P3.4, P4.6, P5.2, P5.5, P5.6, P5.7]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Minimal models of surfaces

### Statement

As in Section 11.1, $S$ is a smooth projective surface over an algebraically closed field $k$. A *$(-1)$-curve* is a smooth rational curve $E$ with $E^2 = -1$, and then $K_S \cdot E = -1$ by Corollary P5.5.15. The section uses three results of Chapter 7: Castelnuovo's contraction theorem (Hartshorne, Theorem V.5.7), which says that every $(-1)$-curve $E$ on $S$ is the exceptional curve of the blow-up $S \to S_1$ of a point on a smooth projective surface $S_1$; the elimination of indeterminacy, which says that for every rational map $\varphi \colon S \dashrightarrow X$ to a projective variety there is a composite $f \colon S'' \to S$ of blow-ups of points such that $\varphi \circ f$ is a morphism; and the factorization theorem, which says that every birational morphism of smooth projective surfaces is a composite of blow-ups of points. If such a composite is not an isomorphism, the exceptional curve of its last blow-up is a $(-1)$-curve on the source, by Theorems P5.6.2 and P5.6.3.

It also uses one fact from outside the handbook: the group $\operatorname{Num}(S)$ of Definition P5.5.7 is a free abelian group of finite rank $\rho(S)$, the *Picard number*. It is torsion free because a class $D$ with $nD \equiv 0$ has $D \cdot C = 0$ for all $C$. The finiteness of the rank is the theorem of the base of Néron and Severi; Kleiman's exposé XIII of SGA 6 proves it in every characteristic, and Hartshorne, Exercise V.1.8, gives a proof in characteristic $0$ through the cohomology class of a divisor in $H^1(S, \Omega_S)$. Since $H^2 > 0$ for $H$ ample (Lemma P5.5.20), $\rho(S) \geq 1$.

**Definition P5.11.13 (nef divisors, minimal surfaces, minimal models).** A divisor $D$ on $S$ is *nef* if $D \cdot C \geq 0$ for every integral curve $C$ on $S$. The surface $S$ is *minimal* if it contains no $(-1)$-curve. A *minimal model* of $S$ is a minimal surface $S_0$ together with a birational morphism $S \to S_0$.

By the factorization theorem of Chapter 7, $S$ is minimal if and only if every birational morphism from $S$ to a smooth projective surface is an isomorphism.

**Theorem P5.11.14 (existence of minimal models).** Every smooth projective surface $S$ has a minimal model. More precisely, there is a sequence $S = S_r \to S_{r-1} \to \dots \to S_0$ in which each map is the contraction of a $(-1)$-curve, $S_0$ is minimal, $r = \rho(S) - \rho(S_0) \leq \rho(S) - 1$, and $K_{S_0}^2 = K_S^2 + r$.

Lean: not in Lean as stated.

**Lemma P5.11.15 (pullbacks under a composite of blow-ups).** Let $g \colon X = X_r \to X_{r-1} \to \dots \to X_0 = Y$ be a composite of blow-ups $\sigma_i \colon X_i \to X_{i-1}$ of points, with exceptional curves $E_i \subseteq X_i$.

1. For an integral curve $C \subseteq X$, $g(C)$ is a point or an integral curve. The curves with $g(C)$ a point are exactly the $r$ strict transforms in $X$ of $E_1, \dots, E_r$.
2. $K_X = g^* K_Y + Z$ with $Z$ effective, and the support of $Z$ is the union of the curves contracted by $g$.
3. Let $D$ be a divisor on $Y$ and $C \subseteq X$ an integral curve. If $g(C)$ is a curve, then $g^* D \cdot C = D \cdot g(C)$; if $g(C)$ is a point, then $g^* D \cdot C = 0$.

Lean: not in Lean as stated.

**Lemma P5.11.16 (contracting a $(-1)$-curve first).** Let $g \colon X \to Y$ be a birational morphism of smooth projective surfaces, and $c \colon X \to X_1$ the blow-up of a point $p$ of a smooth projective surface $X_1$, with exceptional curve $E$. If $g(E)$ is a point, there is a unique morphism $h \colon X_1 \to Y$ with $g = h \circ c$.

Lean: not in Lean as stated.

**Proposition P5.11.17 (minimal surfaces with $\kappa \geq 0$).** Let $\kappa(S) \geq 0$. Then $S$ is minimal if and only if $K_S$ is nef. In that case $K_S^2 \geq 0$.

Lean: not in Lean as stated.

**Theorem P5.11.18 (maps to a minimal surface with $\kappa \geq 0$).** Let $S'$ be a minimal surface with $\kappa(S') \geq 0$ and $S$ a smooth projective surface. Every birational map $\varphi \colon S \dashrightarrow S'$ is a morphism.

Lean: not in Lean as stated.

**Corollary P5.11.19 (uniqueness of the minimal model).** Let $\kappa(S) \geq 0$.

1. Two minimal surfaces with $\kappa \geq 0$ that are birational are isomorphic, and every birational map between them is an isomorphism.
2. $S$ has a minimal model $g \colon S \to S_0$, unique up to unique isomorphism: for every minimal model $g' \colon S \to S'_0$ there is exactly one isomorphism $\psi \colon S_0 \to S'_0$ with $g' = \psi \circ g$. Every birational map from $S$ to a minimal surface is a morphism.
3. If $S$ is minimal, every birational map $S \dashrightarrow S$ is an automorphism.

Lean: not in Lean as stated.

### Proof in words

Existence is a descent: contracting a $(-1)$-curve lowers the Picard number by one, so the process stops. Uniqueness rests on the sign of $K$. On a surface with $\kappa \geq 0$ some multiple of $K$ is effective, so a curve $C$ with $K \cdot C < 0$ is a component of that multiple with $C^2 < 0$, hence a $(-1)$-curve by adjunction. On a minimal surface with $\kappa \geq 0$ the canonical divisor is therefore nef.

Now resolve a birational map $\varphi \colon S \dashrightarrow S'$ by blow-ups $f \colon S'' \to S$ with as few blow-ups as possible, and look at the last exceptional curve $E$ of $f$. The morphism $g = \varphi \circ f$ pulls $K_{S'}$ back to $K_{S''}$ minus an effective divisor supported on the curves that $g$ contracts. If $g$ did not contract $E$, then $K_{S''} \cdot E$ would be the sum of $K_{S'} \cdot g(E) \geq 0$ and a nonnegative term, which contradicts $K_{S''} \cdot E = -1$. So $g$ contracts $E$, then $g$ factors through the contraction of $E$, and a shorter resolution exists. Hence $f$ is an isomorphism and $\varphi$ is a morphism. A birational morphism onto a minimal surface from a minimal surface is an isomorphism, which gives uniqueness. On $\mathbb{P}^2$ the argument breaks down because $K$ is negative on every curve, and minimal models are not unique.

### Examples

**Example P5.11.20 (the plane and the quadric).** The surfaces $\mathbb{P}^2$ and $Q = \mathbb{P}^1 \times \mathbb{P}^1$ are minimal. On $\mathbb{P}^2$ every curve of degree $d$ has $C^2 = d^2 \geq 1$ by Example P5.5.8. On $Q$ an integral curve has class $aF_1 + bF_2$ and $C^2 = 2ab$, which is even, by Example P5.5.9. They are birational, since both contain $\mathbb{A}^2$ as a dense open subset (Example P3.9.12), and they are not isomorphic: two curves on $\mathbb{P}^2$ always meet, with $C \cdot D = de > 0$, while two fibres of $p_1$ on $Q$ are disjoint. So a rational surface has at least two non-isomorphic minimal models. Example P5.6.9 makes this concrete: $\operatorname{Bl}_p Q$ has the two disjoint $(-1)$-curves $F_1 - E$ and $F_2 - E$, whose contraction maps to $\mathbb{P}^2$, and the $(-1)$-curve $E$, whose contraction maps to $Q$. The projection $Q \dashrightarrow \mathbb{P}^2$ from $p$ is a birational map between minimal surfaces that is not a morphism, as $\kappa = -\infty$ allows. Here $\rho(\operatorname{Bl}_p Q) = 3$, $\rho(\mathbb{P}^2) = 1$ and $\rho(Q) = 2$, so the two descents of Theorem P5.11.14 have lengths $2$ and $1$, and $K^2$ goes from $7$ to $9$ and to $8$.

**Example P5.11.21 (blow-ups of a minimal surface with $\kappa \geq 0$).** Let $S$ be minimal with $\kappa(S) \geq 0$, for instance an abelian surface $E \times E'$, a smooth surface of degree $d \geq 4$ in $\mathbb{P}^3$, or one of the products of Examples P5.11.10 and P5.11.12. These are minimal by Proposition P5.11.17, since $K$ is trivial, a nonnegative multiple of a hyperplane section, or a sum of fibres of the two projections, and each of these is nef: a fibre $F$ has $F^2 = 0$ and meets every other integral curve properly. Let $\pi \colon S_r \to S$ be the blow-up of $r$ distinct points, with exceptional curves $E_1, \dots, E_r$. Then $E_1, \dots, E_r$ are the only $(-1)$-curves on $S_r$. Indeed, $K_{S_r} = \pi^* K_S + E_1 + \dots + E_r$ by Theorem P5.6.3, and for an integral curve $C$ different from the $E_i$, Lemma P5.11.15 gives
$$K_{S_r} \cdot C = K_S \cdot \pi(C) + \sum_i E_i \cdot C \geq 0,$$
since $K_S$ is nef and $C$ meets each $E_i$ properly. So $K_{S_r}$ is not nef, with $K_{S_r} \cdot E_i = -1$, and $\pi$ is the unique minimal model of $S_r$, with $K_{S_r}^2 = K_S^2 - r$. For the quartic, $K_{S_r} = E_1 + \dots + E_r$ is effective and $K_{S_r}^2 = -r$.

**Example P5.11.22 (the surfaces $C \times \mathbb{P}^1$ are minimal).** Let $C$ be a curve of genus $g \geq 1$ and $S = C \times \mathbb{P}^1$, with projection $p_1 \colon S \to C$. Suppose $E \subseteq S$ is a $(-1)$-curve. The restriction $p_1|_E \colon E \cong \mathbb{P}^1 \to C$ is constant, since otherwise it is dominant and $C \cong \mathbb{P}^1$ by Lüroth's theorem (Theorem P5.2.12). So $E$ lies in a fibre $\{x\} \times \mathbb{P}^1$, which is integral, and $E$ equals that fibre. But the restriction of $\mathcal{O}(\{x\} \times \mathbb{P}^1) = p_1^* \mathcal{O}_C(x)$ to the fibre is trivial, so $E^2 = 0$ by Theorem P5.5.6, a contradiction. With Example P5.11.20 for $g = 0$, every $C \times \mathbb{P}^1$ is minimal. Here $\kappa = -\infty$ and $K_S = p_1^* K_C - 2 F$, with $F = C \times \{y\}$, has $K_S \cdot (\{x\} \times \mathbb{P}^1) = -2$, so $K_S$ is not nef on a minimal surface; Proposition P5.11.17 needs $\kappa \geq 0$.

### Proof

*Theorem P5.11.14.* Induction on $\rho(S)$. If $S$ is minimal, take $r = 0$. Otherwise let $E \subseteq S$ be a $(-1)$-curve. By Castelnuovo's theorem (Chapter 7) there is a smooth projective surface $S_1$ and a point $p \in S_1$ with $S \cong \operatorname{Bl}_p S_1$ and $E$ the exceptional curve. By parts 3 and 4 of Theorem P5.6.3, $\rho(S_1) = \rho(S) - 1$ and $K_{S_1}^2 = K_S^2 + 1$. Since $\rho(S_1) \geq 1$, the induction applies to $S_1$ and gives a descent from $S_1$ of length $\rho(S_1) - \rho(S_0)$, and composing with $S \to S_1$ proves the claim for $S$. The composite $S \to S_0$ is a birational morphism. $\square$

*Lemma P5.11.15.* Induction on $r$; for $r = 0$ there is nothing to prove. Let $r \geq 1$, $\sigma = \sigma_r$, $E = E_r$ and $g' = \sigma_1 \circ \dots \circ \sigma_{r-1} \colon X_{r-1} \to Y$, so $g = g' \circ \sigma$, and assume the lemma for $g'$.

(1) The morphism $\sigma$ is an isomorphism over $X_{r-1} \setminus \{p\}$, where $p = \sigma(E)$ (Theorem P5.6.2). So an integral curve $C \neq E$ on $X$ is the closure of $\sigma^{-1}(\sigma(C) \setminus \{p\})$, that is, the strict transform of $\sigma(C)$ (Proposition P5.6.4). Hence $g(C) = g'(\sigma(C))$ is a point exactly when $\sigma(C)$ is contracted by $g'$, which by induction means that $\sigma(C)$ is the strict transform in $X_{r-1}$ of one of $E_1, \dots, E_{r-1}$. Together with $E$ itself these are the $r$ strict transforms. The image of an integral curve under a morphism of projective varieties is closed and irreducible, so it is a point or an integral curve.

(2) By induction, $K_{X_{r-1}} = g'^* K_Y + Z'$ with $Z'$ effective and supported exactly on the curves contracted by $g'$. By Theorem P5.6.3, $K_X = \sigma^* K_{X_{r-1}} + E = g^* K_Y + \sigma^* Z' + E$. Put $Z = \sigma^* Z' + E$. By Proposition P5.6.4, $\sigma^* Z' = \tilde Z' + m E$ with $\tilde Z'$ the strict transform and $m = m_p(Z') \geq 0$, so $Z$ is effective, and its support is $E$ together with the strict transforms of the components of $Z'$. By (1) these are exactly the curves contracted by $g$.

(3) By Theorem P5.6.3, $\sigma^* D' \cdot E = 0$ for every divisor $D'$ on $X_{r-1}$. If $C \neq E$, then $\sigma^* \sigma(C) = C + mE$ with $m = m_p(\sigma(C))$ by Proposition P5.6.4, so
$$\sigma^* D' \cdot C = \sigma^* D' \cdot \sigma^* \sigma(C) - m\, \sigma^* D' \cdot E = D' \cdot \sigma(C).$$
Apply this to $D' = g'^* D$, so that $g^* D = \sigma^* D'$. If $C = E$, then $g^* D \cdot C = 0$, and $g(E)$ is a point. Otherwise $g^* D \cdot C = g'^* D \cdot \sigma(C)$, and the induction hypothesis for $g'$ and the curve $\sigma(C)$, with $g'(\sigma(C)) = g(C)$, gives the claim. $\square$

*Lemma P5.11.16.* Let $\Gamma \subseteq X_1 \times Y$ be the image of $(c, g) \colon X \to X_1 \times Y$. It is closed, since $X$ is projective, and integral as the image of an integral scheme, with the reduced structure. The projection $\mathrm{pr}_1 \colon \Gamma \to X_1$ is projective, being the restriction to a closed subscheme of the base change of the projective morphism $Y \to \operatorname{Spec} k$. Since $\Gamma$ is the image of $X$ and $\mathrm{pr}_1 \circ (c, g) = c$, the fibre of $\mathrm{pr}_1$ over $x \in X_1$ is the image of $c^{-1}(x)$ under $(c, g)$. For $x \neq p$, $c^{-1}(x)$ is one point. For $x = p$, $c^{-1}(p) = E$ and $(c, g)(E) = \{p\} \times g(E)$ is one point by hypothesis. Over the dense open set $X_1 \setminus \{p\}$, where $c$ is an isomorphism, $\Gamma$ is the graph of $g \circ c^{-1}$, so $\mathrm{pr}_1$ is birational. The surface $X_1$ is normal, being smooth. By Corollary P4.6.10, the projective birational morphism $\mathrm{pr}_1$ with finite fibres is an isomorphism. Put $h = \mathrm{pr}_2 \circ \mathrm{pr}_1^{-1}$. Since $\mathrm{pr}_1 \circ (c, g) = c$, the morphism $(c, g) \colon X \to \Gamma$ equals $\mathrm{pr}_1^{-1} \circ c$, and $h \circ c = \mathrm{pr}_2 \circ (c, g) = g$. If $h'$ is a second such morphism, $h$ and $h'$ agree on $X_1 \setminus \{p\}$, hence everywhere by Theorem P3.4.11. $\square$

*Proposition P5.11.17.* If $K_S$ is nef, $S$ is minimal, since $K_S \cdot E = -1$ for a $(-1)$-curve. Conversely let $S$ be minimal, and choose $m \geq 1$ with $h^0(mK_S) > 0$, which exists because $\kappa(S) \geq 0$. Write $mK_S \sim F = \sum_i a_i C_i$ with $C_i$ distinct integral curves and $a_i > 0$, or $F = 0$. Let $C$ be an integral curve with $K_S \cdot C < 0$. If $C$ is not one of the $C_i$, then $mK_S \cdot C = F \cdot C \geq 0$ by Proposition P5.5.5, a contradiction. So $C = C_1$, say, and
$$0 > mK_S \cdot C = a_1 C^2 + \sum_{i \geq 2} a_i C_i \cdot C \geq a_1 C^2,$$
so $C^2 < 0$. By part 2 of Corollary P5.5.15, $C$ is a $(-1)$-curve, which contradicts minimality. So $K_S$ is nef. Then $m^2 K_S^2 = mK_S \cdot F = \sum_i a_i\, mK_S \cdot C_i \geq 0$. $\square$

*Theorem P5.11.18.* By Proposition P5.11.17, $K_{S'}$ is nef. By the elimination of indeterminacy of Chapter 7, the set of composites $f \colon S'' \to S$ of blow-ups of points for which $\varphi \circ f$ is a morphism is not empty. Choose one with the least number $n$ of blow-ups, and suppose $n \geq 1$. Write $f = f_1 \circ c$, where $c \colon S'' \to S''_1$ is the last blow-up, with exceptional curve $E$, a $(-1)$-curve, so $K_{S''} \cdot E = -1$. The morphism $g = \varphi \circ f \colon S'' \to S'$ is birational, so by the factorization theorem of Chapter 7 it is a composite of blow-ups of points, and Lemma P5.11.15 applies to it: $K_{S''} = g^* K_{S'} + Z$ with $Z$ effective and supported on the curves contracted by $g$.

Suppose $g(E)$ is a curve. Then $E$ is not a component of $Z$, so $Z \cdot E \geq 0$ by Proposition P5.5.5, and $g^* K_{S'} \cdot E = K_{S'} \cdot g(E) \geq 0$ by part 3 of Lemma P5.11.15, since $K_{S'}$ is nef. So $K_{S''} \cdot E \geq 0$, a contradiction. Hence $g(E)$ is a point, and by Lemma P5.11.16, $g = h \circ c$ for a morphism $h \colon S''_1 \to S'$. As rational maps, $h \circ c = \varphi \circ f_1 \circ c$, and $c$ is birational, so $h = \varphi \circ f_1$ on a dense open subset of $S''_1$. So $\varphi \circ f_1$ is a morphism, and $f_1$ is a composite of $n - 1$ blow-ups, which contradicts the choice of $n$. Hence $n = 0$, $f$ is an isomorphism, and $\varphi$ is a morphism. $\square$

*Corollary P5.11.19.* (1) Let $S_1$ and $S_2$ be minimal and birational with $\kappa \geq 0$; by Theorem P5.11.6 they have the same Kodaira dimension. Let $\varphi \colon S_1 \dashrightarrow S_2$ be birational. By Theorem P5.11.18, $\varphi$ and $\varphi^{-1}$ are morphisms. The composites $\varphi^{-1} \circ \varphi$ and $\varphi \circ \varphi^{-1}$ agree with the identities on dense open subsets, hence everywhere by Theorem P3.4.11. So $\varphi$ is an isomorphism.

(2) A minimal model exists by Theorem P5.11.14. A birational map from $S$ to a minimal surface $S'$ is a morphism by Theorem P5.11.18, since $\kappa(S') = \kappa(S) \geq 0$. Given minimal models $g$ and $g'$, the birational map $\psi = g' \circ g^{-1} \colon S_0 \dashrightarrow S'_0$ is an isomorphism by (1), and $\psi \circ g = g'$ on a dense open subset, hence everywhere. Uniqueness of $\psi$ follows from the surjectivity of $g$ and Theorem P3.4.11.

(3) This is (1) with $S_1 = S_2 = S$. $\square$

### Exercises

1. (A) Show that a smooth surface of degree $d \geq 4$ in $\mathbb{P}^3$ is minimal, and that a smooth cubic surface is not, using a line $L$ on it (Chapter 10) and the adjunction formula to compute $L^2$.
2. (A) Let $S$ be minimal with $\kappa(S) \geq 0$ and $\pi \colon \tilde S \to S$ a composite of $r$ blow-ups of points. Show that $K_{\tilde S}^2 = K_S^2 - r$, so that the number of blow-ups between a surface with $\kappa \geq 0$ and its minimal model is $K_{S_0}^2 - K_S^2$.
3. (B) Let $S$ be minimal with $\kappa(S) \geq 0$, and let $\tilde S$ be obtained by blowing up a point $p \in S$ and then a point $q$ on the exceptional curve $E_1$. Find all $(-1)$-curves on $\tilde S$ and show that there is exactly one. What is the class of the strict transform of $E_1$?
4. (B) Show that the projection $Q \dashrightarrow \mathbb{P}^2$ of Example P5.11.20 is not defined at $p$, by showing that the two lines of $Q$ through $p$ would have to map to points.
5. (B) Let $S$ be minimal with $\kappa(S) \geq 0$ and $C \subseteq S$ an integral curve with $C^2 < 0$. Show that either $K_S \cdot C > 0$, or $C$ is a smooth rational curve with $C^2 = -2$.
6. (C) Let $X \subseteq \mathbb{P}^3$ be a smooth quartic surface. Show that every birational map $X \dashrightarrow X$ is an automorphism, and that an automorphism $\alpha$ of $X$ with $\alpha^* \mathcal{O}_X(1) \cong \mathcal{O}_X(1)$ is the restriction of a projective linear transformation of $\mathbb{P}^3$. (Use $H^0(\mathbb{P}^3, \mathcal{O}(1)) \cong H^0(X, \mathcal{O}_X(1))$.)

### Lean

Mathlib has neither the intersection pairing on a surface nor blow-ups of points of surfaces, and it does not define $(-1)$-curves, nef divisors or minimal surfaces. Its rational maps (`AlgebraicGeometry.Scheme.RationalMap`) and the equalizer statement used in Theorem P3.4.11 are available. The handbook adds no `MinimalModel` node here.

### Notes and history

Minimal models of surfaces go back to Castelnuovo and Enriques, who proved around 1900 that a surface which is not birationally ruled has a unique minimal model. Zariski gave the first algebraic proof in 1958 and extended it to every characteristic, and Hartshorne, Section V.5, and Beauville, Chapter II, follow his line through the factorization of birational morphisms. Beauville, Chapter II, proves uniqueness for surfaces that are not birationally ruled by a similar argument. The literature state is theorem. In the language of the minimal model program, Theorem P5.11.14 is the run of the program on a surface, with each $(-1)$-curve spanning a $K$-negative extremal ray (Chapter 12), and Proposition P5.11.17 says that when $\kappa \geq 0$ the program ends at a surface with nef canonical divisor. In higher dimension minimal models exist for varieties of general type and more generally for klt pairs with big boundary in characteristic $0$ (Birkar, Cascini, Hacon and McKernan, 2010), but they are not unique: two minimal models of a threefold are connected by flops (Kawamata, 2008). So uniqueness of minimal models is special to dimension at most $2$.
