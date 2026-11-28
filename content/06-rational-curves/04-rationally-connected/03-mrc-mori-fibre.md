---
title: The rationally connected quotient and Mori fibre spaces
nodes: []
sources: [Kol96, KMM92b, Cam92, GHS03, HM07b, Deb01]
reads_with: [Kol96:IV.5, Deb01:ch5, GHS03:all, HM07b:all]
requires: [P7.3, P8.3, 6.3]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The rationally connected quotient and Mori fibre spaces

### Statement

In this section $X$ is a smooth projective variety of dimension $n$ over $\mathbb{C}$. A point is *very general* if it lies outside a countable union of proper closed subsets.

**Theorem 6.4.14 (the maximal rationally connected fibration, cited).** There are a dense open subset $X^0 \subseteq X$, a normal variety $Z^0$ and a proper surjective morphism $\varphi \colon X^0 \to Z^0$ with connected fibres, and a dense open subset $U \subseteq Z^0$, such that:

1. for $z \in U$ the fibre $X_z = \varphi^{-1}(z)$ is smooth, projective and rationally connected;
2. for a very general point $z \in Z^0$, every rational curve in $X$ that meets $X_z$ is contained in $X_z$.

The pair $(X^0, \varphi)$ is unique up to birational equivalence of $Z^0$, and $\varphi$ is the *MRC fibration* of $X$.

Lean: not yet in Lean.

**Theorem 6.4.15 (the base is not uniruled).** In Theorem 6.4.14, every smooth projective variety birational to $Z^0$ is not uniruled.

Lean: not yet in Lean.

**Corollary 6.4.16 (uniruledness and the quotient).** $X$ is uniruled if and only if $\dim Z^0 < n$, and $X$ is rationally connected if and only if $Z^0$ is a point.

Lean: not yet in Lean.

**Definition 6.4.17 (Mori fibre space).** A *Mori fibre space* is a morphism $\varphi \colon X \to Y$ onto a normal projective variety with $\varphi_* \mathcal{O}_X = \mathcal{O}_Y$ and $\dim Y < n$, which is the contraction of a $K_X$-negative extremal ray $R$: a curve $C \subseteq X$ is contracted by $\varphi$ if and only if $[C] \in R$.

**Proposition 6.4.18 (fibres of a Mori fibre space).** Let $\varphi \colon X \to Y$ be a Mori fibre space. Then the general fibre $F$ of $\varphi$ is a Fano variety of dimension $n - \dim Y$, and it is rationally connected. The variety $X$ is uniruled, and it is rationally connected if and only if $Y$ is.

Lean: not yet in Lean.

**Theorem 6.4.19 (Hacon and McKernan, cited).** Let $(X, \Delta)$ be a klt pair over $\mathbb{C}$ and $f \colon X \to S$ a projective morphism with $f_* \mathcal{O}_X = \mathcal{O}_S$ such that $-(K_X + \Delta)$ is $f$-big and $f$-nef. Then every fibre of $f$ is rationally chain connected. In particular every fibre of a Mori fibre space, and every fibre of the contraction of a $K_X$-negative extremal ray, is rationally chain connected.

Lean: not yet in Lean.

### Proof in words

The MRC fibration is the quotient of Theorem 6.4.2 taken for all families of rational curves at once: its fibres are the largest rationally connected subvarieties through general points. Its base cannot be uniruled, by the theorem of Graber, Harris and Starr. A rational curve $D$ through a very general point $z$ of the base pulls back to a variety fibred over $\mathbb{P}^1$ with rationally connected general fibre, which is rationally connected by Corollary P8.3.22. A very free curve on it through a point over $z$ and a point over another point of $D$ maps to a rational curve in $X$ that meets $X_z$ and leaves it, which part 2 of Theorem 6.4.14 forbids. For a Mori fibre space, the anticanonical class restricted to a general fibre is the restriction of the ample class $-K_X + m L$, so the general fibre is Fano and rationally connected by Theorem 6.4.8. Rational connectedness then passes between $X$ and $Y$ in both directions.

### Examples

**Example 6.4.20 (a ruled surface over an elliptic curve).** For $X = E \times \mathbb{P}^1$, the projection to $E$ is a Mori fibre space: by Example 6.2.13 the ray of a fibre is $K_X$-negative and extremal. Its fibres are the only rational curves, so it is also the MRC fibration, and the base $E$ is not uniruled, in accordance with Theorem 6.4.15. So $X$ is uniruled but not rationally connected.

**Example 6.4.21 (a conic bundle over the plane).** For the general divisor $X \subseteq \mathbb{P}^2 \times \mathbb{P}^2$ of bidegree $(2, 1)$ of Example 6.3.14, the projection to the second factor is a Mori fibre space of type C1, with conics as fibres and a cubic discriminant curve. The general fibre is $\mathbb{P}^1$, the base is rationally connected, and so is $X$ by Proposition 6.4.18. The fibres over the discriminant are pairs of lines, rationally chain connected as Theorem 6.4.19 requires, but not irreducible.

**Example 6.4.22 (Hirzebruch surfaces).** On $\mathbb{F}_a = \mathbb{P}(\mathcal{O} \oplus \mathcal{O}(a))$ over $\mathbb{P}^1$, the fibre $f$ has $f^2 = 0$ and $-K \cdot f = 2$, and its ray is extremal, with contraction the bundle map $\mathbb{F}_a \to \mathbb{P}^1$, a Mori fibre space. Its fibres are $\mathbb{P}^1$ and the base is $\mathbb{P}^1$, so $\mathbb{F}_a$ is rationally connected for every $a \ge 0$, although it is Fano only for $a \le 1$.

### Proof

*Theorem 6.4.15.* The property is a birational invariant of smooth projective varieties, since a family of rational curves on one of them is a family on the other after removing a proper closed subset from the base. After shrinking $Z^0$ and $U$ we may assume that $Z^0$ is smooth and that $\varphi$ is smooth over $U$, by generic smoothness; parts 1 and 2 still hold for the restricted map. Let $Z$ be a smooth projective variety containing $Z^0$ as a dense open subset, which exists by Nagata's compactification and resolution of singularities, the resolution being an isomorphism over the smooth variety $Z^0$. Suppose that $Z$ is uniruled.

Let $z \in U$ be a very general point for which part 2 of Theorem 6.4.14 holds. By part 1 of Theorem P8.3.4 there is a nonconstant morphism $h \colon \mathbb{P}^1 \to Z$ with $z \in h(\mathbb{P}^1)$. Let $\Gamma \subseteq X \times Z$ be the closure of the graph of $\varphi$. The graph is the image of the proper morphism $X^0 \to X \times Z^0$ over $Z^0$, so it is closed in $X \times Z^0$, and $\Gamma \cap (X \times Z^0)$ is the graph. Let $T = h^{-1}(U)$, a dense open subset of $\mathbb{P}^1$, and $\Gamma_T = \varphi^{-1}(U) \times_U T$. It is smooth over $T$ with fibre $X_{h(t)}$ over $t \in T$, which is irreducible, so $\Gamma_T$ is irreducible. Let $\Gamma_D$ be its closure in $\Gamma \times_Z \mathbb{P}^1$ and $Y \to \Gamma_D$ a resolution of singularities that is an isomorphism over the smooth variety $\Gamma_T$. The composite $\pi \colon Y \to \mathbb{P}^1$ is a proper surjective morphism whose fibre over $t \in T$ is $X_{h(t)}$, smooth and rationally connected by part 1 of Theorem 6.4.14. Since $\mathbb{P}^1$ is rationally connected, $Y$ is rationally connected by Corollary P8.3.22.

Choose $t_1 \in T$ with $h(t_1) = z$ and $t_2 \in T$ with $h(t_2) = d \ne z$, which exists since $h(T)$ is an infinite subset of the curve $h(\mathbb{P}^1)$. Choose points $y_i \in \pi^{-1}(t_i)$, so that $y_1$ maps to a point $x_1 \in X_z$ and $y_2$ to a point $x_2 \in X_d$ under the projection $p \colon Y \to \Gamma_D \to X$. By part 1 of Theorem P8.3.13 there is a rational curve $g \colon \mathbb{P}^1 \to Y$ through $y_1$ and $y_2$. Then $p \circ g$ is a nonconstant morphism, since $x_1 \ne x_2$, as $X_z$ and $X_d$ are disjoint. Its image is a rational curve in $X$ that meets $X_z$ at $x_1$ and contains $x_2 \notin X_z$. This contradicts part 2 of Theorem 6.4.14.

*Corollary 6.4.16.* Suppose $X$ is uniruled, and let $z$ be a very general point of $Z^0$ as in part 2 of Theorem 6.4.14. By part 1 of Theorem P8.3.4 there is a rational curve through a point of $X_z$, and it lies in $X_z$, so $\dim X_z \ge 1$ and $\dim Z^0 < n$. Conversely, if $\dim Z^0 < n$, then for $z \in U$ the fibre $X_z$ is rationally connected of positive dimension, so $X_z$ is uniruled: a family on $X_z$ with dominant two-point map is dominant, and its members are not all constant, since otherwise the image of the two-point map would lie in the diagonal. By part 1 of Theorem P8.3.4 every point of $X_z$ lies on a rational curve. So every point of the dense open subset $\varphi^{-1}(U)$ lies on a rational curve, and $X$ is uniruled by part 2 of Theorem P8.3.4 and Lemma P8.3.2. If $Z^0$ is a point, then $X^0 = X_z$ is rationally connected for $z \in U$, and so is $X$, since a family with dominant two-point map on $X^0$ is one on $X$. If $X$ is rationally connected, let $z$ be very general. By part 1 of Theorem P8.3.13 every point $x \in X$ lies on a rational curve through a point of $X_z$, so $x \in X_z$ by part 2 of Theorem 6.4.14, and $X = X_z$, so $Z^0$ is a point.

*Proposition 6.4.18.* Let $L$ be the pullback of an ample Cartier divisor on $Y$. As in the proof of Proposition 6.3.15, $H = -K_X + m L$ is ample for $m$ large. By generic smoothness there is a dense open subset $Y^0 \subseteq Y$ over which $\varphi$ is smooth, and a fibre $F$ over $Y^0$ is a smooth projective variety, connected since $\varphi_* \mathcal{O}_X = \mathcal{O}_Y$, of dimension $n - \dim Y \ge 1$. Its normal bundle is trivial, so $K_F = K_X|_F$ by adjunction, and $L|_F$ is trivial. So $-K_F = H|_F$ is ample, and $F$ is a Fano variety. It is rationally connected by Theorem 6.4.8. Every point of $F$ lies on a rational curve, for instance a very free curve given by part 1 of Theorem P8.3.13, so every point of the dense open subset $\varphi^{-1}(Y^0)$ of $X$ lies on a rational curve, and $X$ is uniruled by part 2 of Theorem P8.3.4 and Lemma P8.3.2. If $X$ is rationally connected, then so is $Y$, by part 1 of Proposition 6.4.9. If $Y$ is rationally connected, then so is $X$, by Corollary P8.3.22.

### Exercises

1. (A) Let $X = C \times \mathbb{P}^m$ for a smooth projective curve $C$ of genus $g \ge 1$. Show that the projection to $C$ is both a Mori fibre space and the MRC fibration.
2. (A) Show that a smooth projective surface $S$ with $\kappa(S) \ge 0$ has MRC fibration the identity, and that a ruled surface over a curve of genus $g \ge 1$ has MRC fibration the ruling.
3. (B) Let $X$ be a smooth projective variety with $K_X$ nef. Use Theorem P8.3.10 and Corollary 6.4.16 to show that its MRC fibration is birational. Show that $X = E \times \mathbb{P}^1$ is not of this kind, and compute its MRC fibration.
4. (B) Let $\varphi \colon X \to Y$ be a Mori fibre space with $\dim Y = n - 1$. Show that the general fibre is $\mathbb{P}^1$, and that $-K_X \cdot F = 2$ for a general fibre $F$.
5. (B) Let $X$ be a smooth projective threefold with a Mori fibre space $\varphi \colon X \to C$ onto a curve of genus $g \ge 1$. Show that the MRC fibration of $X$ is $\varphi$, and that $X$ is not rationally connected.
6. (C) Let $\varphi \colon X \to Y$ be the contraction of a $K_X$-negative extremal ray of type E1 on a smooth threefold, the blow-up of a smooth curve $C \subseteq Y$. Check Theorem 6.4.19 on its fibres directly, and show that Theorem 6.4.19 gives nothing new for E2 to E5, whose nontrivial fibre is the exceptional divisor itself.

### Lean

`MinimalModel.IsMoriFibreSpace`, in the project library, is the notion of Definition 6.4.17 for a pair, with $\rho(X/Y) = 1$ and $\dim Y < \dim X$. Nothing else in this section is in Lean: there is no MRC fibration and no notion of rational connectedness.

### Notes and history

The MRC fibration was constructed by Campana (Cam92) and by Kollár, Miyaoka and Mori (KMM92b); see Kol96, Section IV.5. Theorem 6.4.15 is the corollary of the theorem of Graber, Harris and Starr (GHS03) that motivated it, and Corollary 6.4.16 characterizes uniruled varieties by their MRC fibration. Theorem 6.4.19 is the theorem of Hacon and McKernan on Shokurov's rational connectedness conjecture (HM07b). The minimal model program ends either with a minimal model or with a Mori fibre space, and Proposition 6.4.18 shows that in the second case the variety is uniruled, covered by the rationally connected fibres; Volume 7 runs the program with the cone and contraction theorems for klt pairs.
