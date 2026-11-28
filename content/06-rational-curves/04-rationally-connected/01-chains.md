---
title: Chains of rational curves and the quotient by a family
nodes: []
sources: [Kol96, KMM92a, Cam92, Deb01]
reads_with: [Kol96:IV.4, Deb01:ch5, KMM92a:all]
requires: [P8.2, P8.3, 6.1, 6.3]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Chains of rational curves and the quotient by a family

### Statement

Let $X$ be a smooth projective variety of dimension $n$ over an algebraically closed field $k$, and $V_1, \dots, V_m$ families of rational curves on $X$ in the sense of Definition 6.1.5. Rational connectedness and rational chain connectedness are as in Definition P8.3.11.

**Definition 6.4.1 (chains and the equivalence relation).** A *chain* of curves of $V_1, \dots, V_m$ is a connected union $C_1 \cup \dots \cup C_r$ of curves, each of which is a component of a $1$-cycle in the closure of the image of some $V_i$ in the Chow variety of $X$. Two points $x, y \in X$ are *$(V_1, \dots, V_m)$-equivalent* if $x = y$ or some chain contains both.

**Theorem 6.4.2 (the quotient by chains, cited).** There are a dense open subset $X^0 \subseteq X$, a normal variety $Z^0$ and a proper surjective morphism $q \colon X^0 \to Z^0$ with connected fibres such that:

1. for every $x \in X^0$, the fibre $q^{-1}(q(x))$ is the equivalence class of $x$, and in particular it is contained in $X^0$;
2. there is a family of chains $u \colon U \to M$ and $F \colon U \to X$ as in part 2 of Definition P8.3.11, each chain made of curves of $V_1, \dots, V_m$, such that the image of $U \times_M U \to X \times X$ contains a dense open subset of $X^0 \times_{Z^0} X^0$.

Lean: not yet in Lean.

**Proposition 6.4.3 (spanning families give chains).** Suppose that $V_1, \dots, V_m$ are dominating and that their classes span $N_1(X)$. Then $X$ is rationally chain connected, by chains of curves of $V_1, \dots, V_m$. If $k$ has characteristic $0$, then $X$ is rationally connected.

Lean: not yet in Lean.

**Corollary 6.4.4 (Picard number one).** Let $X$ be uniruled with $\rho(X) = 1$. Then $X$ is rationally chain connected, and rationally connected if $k$ has characteristic $0$. This applies to every Fano manifold with $\rho(X) = 1$ in characteristic $0$, and in characteristic $p$ when $k$ is uncountable.

Lean: not yet in Lean.

### Proof in words

The quotient of Theorem 6.4.2 collapses each equivalence class to a point, and the proof that it exists, on an open set, is the main work of Kollár, Miyaoka and Mori and of Campana; it is cited. Granting it, the proposition is a short argument with a divisor. If the quotient $Z^0$ had positive dimension, the preimage of a hypersurface of $Z^0$ would close up to an effective nonzero divisor $D$ on $X$. A curve of $V_i$ through a general point lies in one fibre of $q$, away from $D$, so $D$ has degree $0$ on every $[V_i]$. These classes span $N_1(X)$, so $D \equiv 0$, which is impossible for a nonzero effective divisor. So $Z^0$ is a point, and two general points of $X$ are joined by a chain. In characteristic $0$, part 2 of Theorem P8.3.13 turns chains into single curves.

### Examples

**Example 6.4.5 (quadrics).** Let $Q \subseteq \mathbb{P}^{n+1}$ be a smooth quadric, $n \ge 2$, and $V$ the family of lines, dominating with $\rho(Q) = 1$ for $n \ge 3$. Two general points $x, y$ are not on a common line, since the lines through $x$ lie in $T_x Q$. But $T_x Q \cap T_y Q \cap Q$ is nonempty, of dimension $n - 2$, and for $z$ in it the lines $xz$ and $zy$ lie on $Q$: a chain of two lines joins $x$ and $y$. Smoothing such a chain gives the conics through $x$ and $y$.

**Example 6.4.6 (one family on $\mathbb{P}^1 \times \mathbb{P}^2$).** Let $X = \mathbb{P}^1 \times \mathbb{P}^2$ and $V$ the family of lines $\ell_2$ in the fibres of $p_1$. The equivalence classes are the fibres $\{ t \} \times \mathbb{P}^2$, and the quotient of Theorem 6.4.2 is $p_1 \colon X \to \mathbb{P}^1$; the class $[\ell_2]$ does not span $N_1(X)$, which has dimension $2$. Adding the family of fibres $\ell_1$ of $p_2$, the two classes span, and two points $(s, a)$ and $(t, b)$ are joined by the chain $\mathbb{P}^1 \times \{ a \}$ followed by a line from $(t, a)$ to $(t, b)$.

**Example 6.4.7 (a ruled surface over an elliptic curve).** Let $X = E \times \mathbb{P}^1$ with $E$ an elliptic curve. The only rational curves are the fibres $\{ p \} \times \mathbb{P}^1$ (Example P8.3.9), so for the family $V$ of fibres the quotient is the projection to $E$, of positive dimension, and $X$ is not rationally chain connected (Example P8.3.17). Here $[V]$ spans only the ray of $f$ in Example 6.2.13, so Proposition 6.4.3 does not apply.

### Proof

*Proposition 6.4.3.* Let $q \colon X^0 \to Z^0$ be as in Theorem 6.4.2, and suppose $\dim Z^0 \ge 1$. After shrinking $Z^0$ to a dense affine open subset and $X^0$ to its preimage, part 1 still holds, and there is a nonconstant regular function $g$ on $Z^0$ that vanishes somewhere. Its zero set $V(g)$ is a nonempty proper closed subset of $Z^0$, and $q^{-1}(V(g))$ is locally cut out by one equation $g \circ q$ and is a nonempty proper closed subset of $X^0$, since $q$ is surjective; so it has pure codimension $1$. Let $D$ be its closure in $X$, an effective nonzero divisor, Cartier since $X$ is smooth, with $D \cap X^0 = q^{-1}(V(g))$.

Fix $i$. Since $V_i$ is dominating, $\operatorname{ev}(\mathbb{P}^1 \times V_i)$ contains a dense open subset of $X$, so some member $f$ of $V_i$ passes through a point $x \in X^0$ with $g(q(x)) \ne 0$. The curve $C = f(\mathbb{P}^1)$ lies in the equivalence class of $x$, which is $q^{-1}(q(x)) \subseteq X^0$ by part 1. So $C \subseteq X^0$ and $C \cap D = C \cap q^{-1}(V(g)) = \emptyset$, since $g \circ q$ is constant on $C$ and nonzero at $x$. Hence $D \cdot [V_i] = D \cdot C = 0$ for every $i$. The classes $[V_i]$ span $N_1(X)$, so $D \equiv 0$. But $D \cdot H^{n-1} > 0$ for an ample $H$, since $D$ is effective and nonzero. This contradiction shows $\dim Z^0 = 0$, so $Z^0$ is a point and $X^0$ is a single equivalence class. By part 2 of Theorem 6.4.2, the family of chains $U \to M$ has $U \times_M U \to X \times X$ dominant, so $X$ is rationally chain connected. In characteristic $0$ it is rationally connected by part 2 of Theorem P8.3.13.

*Corollary 6.4.4.* Since $X$ is uniruled, some irreducible component $V$ of $\operatorname{Hom}(\mathbb{P}^1, X)$ has $\operatorname{ev} \colon \mathbb{P}^1 \times V \to X$ dominant: a family $F \colon \mathbb{P}^1 \times M \to X$ as in Definition P8.3.1 gives a morphism from $M$ to $\operatorname{Hom}(\mathbb{P}^1, X)$, whose image lies in one component because $M$ is irreducible. Its members are nonconstant by part 1 of Theorem P8.3.4, so $[V] \ne 0$, and $[V]$ spans $N_1(X)$, of dimension $1$. Proposition 6.4.3 applies. A Fano manifold is uniruled in characteristic $0$ by part 1 of Corollary P8.3.20. In characteristic $p$ there is a rational curve through every point by Theorem P8.2.9, applied to any curve through the point, since $-K_X$ is ample, and $X$ is uniruled by part 2 of Theorem P8.3.4 when $k$ is uncountable.

### Exercises

1. (A) Show that $\mathbb{P}^n$ is rationally chain connected by chains of one line, and that the quotient of Theorem 6.4.2 for the family of lines is the map to a point.
2. (A) Let $X = \mathbb{P}^a \times \mathbb{P}^b$ with the two families of lines in the factors. Show that every two points are joined by a chain of at most two lines.
3. (B) In Example 6.4.5 with $n = 2$, $\rho(Q) = 2$ and there are two families of lines. Show that each family alone has quotient $\mathbb{P}^1$, and that both together join any two points by a chain of two lines.
4. (B) Let $X$ be a smooth cubic surface and $V$ the family of conics in one pencil $|H - L|$ of Proposition 6.1.19. Show that the quotient by $V$ is the conic bundle $X \to \mathbb{P}^1$, and find a second pencil such that the two families together make $X$ rationally chain connected. Do their classes span $N_1(X)$?
5. (B) Find the step of the proof of Proposition 6.4.3 that uses that the families dominate. On $\operatorname{Bl}_p \mathbb{P}^2$, let $V_1$ be the family of maps onto $E$ and $V_2$ the family of strict transforms of lines through $p$. Show that the classes span $N_1$, that $V_1$ is not dominating, and that the surface is still rationally chain connected by chains of curves of $V_1$ and $V_2$.
6. (C) Let $X$ be a smooth projective variety in characteristic $0$ with $\rho(X) = 1$ and $K_X$ not nef. Show that $X$ is Fano and rationally connected.

### Lean

Nothing in this section is in Lean. The library has `MinimalModel.Curve.IsRational`, but no families of rational curves, no chains and no notion of rational connectedness.

### Notes and history

The quotient by chains of rational curves was constructed by Campana (Cam92) and by Kollár, Miyaoka and Mori (KMM92a); see Kol96, Theorem IV.4.16, for the form used here, and Debarre's Chapter 5 (Deb01). The divisor argument of Proposition 6.4.3 is the argument for Picard number one in KMM92a. The quotient is the tool that turns the existence of rational curves into rational connectedness, and in Section 2 it is used with the families of curves of anticanonical degree at most $n + 1$ that the cone theorem provides.
