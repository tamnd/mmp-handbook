---
title: Fano manifolds are rationally connected
nodes: []
sources: [KMM92b, Cam92, Kol96, Deb01]
reads_with: [KMM92b:all, Kol96:V.2, Deb01:ch5]
requires: [P8.3, 6.1, 6.3]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Fano manifolds are rationally connected

### Statement

Let $X$ be a smooth projective variety of dimension $n$ over an algebraically closed field $k$. Rational connectedness is as in Definition P8.3.11, and Fano varieties as in Definition P8.3.18.

**Theorem 6.4.8 (Kollár, Miyaoka and Mori; Campana, cited).** Let $X$ be a Fano variety. Then any two closed points of $X$ are joined by a chain of rational curves $\Gamma_1, \dots, \Gamma_r$ with $-K_X \cdot \Gamma_j \le n + 1$ for every $j$. In particular $X$ is rationally chain connected, and rationally connected if $k$ has characteristic $0$.

Lean: not yet in Lean.

**Proposition 6.4.9 (images and products).** Let $X$ and $Y$ be varieties over $k$.

1. If $X$ is rationally connected and $g \colon X \to Y$ is a dominant morphism, then $Y$ is rationally connected.
2. If $X$ and $Y$ are rationally connected, then $X \times Y$ is rationally connected.

Lean: not yet in Lean.

**Proposition 6.4.10 (two fibre type rays).** Let $k$ have characteristic $0$ and $\rho(X) = 2$, and suppose that $\overline{NE}(X)$ has two distinct $K_X$-negative extremal rays $R_1$, $R_2$, each with a contraction of fibre type. Then $X$ is rationally connected.

Lean: not yet in Lean.

### Proof in words

Theorem 6.4.8 is the main theorem of KMM92b, proved independently by Campana; it is Theorem P8.3.19 with the degree bound added, and it is cited. Its proof runs the quotient of Theorem 6.4.2 for the finitely many families of rational curves with $-K_X \cdot \Gamma \le n + 1$. If the quotient $q \colon X^0 \to Z^0$ had positive dimension, take a general curve $C$ in $X$ that is not contracted by $q$ and apply bend-and-break to $C$ with the points of $C$ in one fibre of $q$ held fixed, as in the proof of Theorem 6.2.9. With the degree computed against $-K_X$, the rational curves that break off have $-K_X$-degree at most $n + 1$ and pass through general points, and one of them is not contained in a fibre of $q$, which contradicts part 1 of Theorem 6.4.2. The delicate step is to keep the curves produced through general points while bounding their degree, and it is done in characteristic $p$ and lifted, as in Chapter 1.

The two propositions are proved here. Images are immediate from the two-point map. For products, a rational curve in $X$ through two points and one in $Y$ through two points give a curve in $X \times Y$ through the two pairs, once the two parametrizations are matched by an automorphism of $\mathbb{P}^1$. With two fibre type rays, Proposition 6.3.15 gives a dominating family of rational curves in each ray, the two classes span $N_1(X)$, and Proposition 6.4.3 applies.

### Examples

**Example 6.4.11 (the product $\mathbb{P}^1 \times \mathbb{P}^2$).** Both rays of $\mathbb{P}^1 \times \mathbb{P}^2$ are of fibre type, of lengths $2$ and $3$ (Example 6.3.18), so Proposition 6.4.10 applies, and so does part 2 of Proposition 6.4.9. Two general points $(s, a)$, $(t, b)$ lie on the curve $\{ (\sigma(u), \lambda(u)) \}$, where $\lambda$ parametrizes the line through $a$ and $b$ and $\sigma \in \operatorname{PGL}_2$ sends $\lambda^{-1}(a)$, $\lambda^{-1}(b)$ to $s$, $t$. Its class is $[\ell_1] + [\ell_2]$, of anticanonical degree $5 = n + 2$: two general points are not on one rational curve of degree at most $n + 1$, since such a curve has class $[\ell_1]$, $[\ell_2]$ or $2 [\ell_1]$ and lies in a fibre of a projection.

**Example 6.4.12 (the flag threefold).** For $W \subseteq \mathbb{P}^2 \times \mathbb{P}^2$ of Example 6.3.21, both contractions are $\mathbb{P}^1$-bundles over $\mathbb{P}^2$, so Proposition 6.4.10 applies. The chains are explicit: a point of $W$ is a pair $(p, L)$ with $p \in L$, a fibre of the first projection is the pencil of lines through $p$, and a fibre of the second is the line $L$ itself. From $(p, L)$ to $(p', L')$, move along $L$ to $p'' = L \cap L'$, rotate the line about $p''$ from $L$ to $L'$, and move along $L'$ to $p'$: a chain of three curves, each of anticanonical degree $2$.

**Example 6.4.13 (a conic bundle threefold).** Let $X \subseteq \mathbb{P}^2 \times \mathbb{P}^2$ be the general divisor of bidegree $(2, 1)$ of Example 6.3.14, with a ray of type C1 and a ray of type C2. Both are of fibre type, so $X$ is rationally connected by Proposition 6.4.10, which here uses only the conics and lines in the fibres. In this example $-K_X = H_1 + 2 H_2$ is ample, so Theorem 6.4.8 applies too.

### Proof

*Proposition 6.4.9.* For part 1, let $F \colon \mathbb{P}^1 \times M \to X$ be a family with $F^{(2)}$ dominant. Then $g \circ F$ is a family of rational curves on $Y$ and $(g \circ F)^{(2)} = (g \times g) \circ F^{(2)}$ is dominant, since $g \times g \colon X \times X \to Y \times Y$ is dominant.

For part 2, let $F \colon \mathbb{P}^1 \times M \to X$ and $G \colon \mathbb{P}^1 \times N \to Y$ be families with $F^{(2)}$ and $G^{(2)}$ dominant, and define
$$\Phi \colon \mathbb{P}^1 \times (M \times N \times \operatorname{PGL}_2) \to X \times Y, \qquad (u, m, m', \sigma) \mapsto (F(u, m), G(\sigma(u), m')).$$
By Chevalley's theorem the images of $F^{(2)}$ and $G^{(2)}$ contain dense open subsets $A \subseteq X \times X$ and $B \subseteq Y \times Y$, and we may remove the diagonals from them. Let $((x_1, x_2), (y_1, y_2)) \in A \times B$, and write $x_i = F(u_i, m)$ and $y_i = G(v_i, m')$. Then $u_1 \ne u_2$ and $v_1 \ne v_2$, since $x_1 \ne x_2$ and $y_1 \ne y_2$. As $\operatorname{PGL}_2$ acts doubly transitively on $\mathbb{P}^1$, there is $\sigma$ with $\sigma(u_i) = v_i$, and then $\Phi(u_i, m, m', \sigma) = (x_i, y_i)$ for $i = 1, 2$. So the image of $\Phi^{(2)}$ contains the dense subset $A \times B$ of $(X \times Y)^2$, after the identification $(X \times Y)^2 = X^2 \times Y^2$, and $\Phi^{(2)}$ is dominant.

*Proposition 6.4.10.* By Proposition 6.3.15, for $i = 1, 2$ there is a dominating family $V_i$ of rational curves with $[V_i] \in R_i$, and $[V_i] \ne 0$ since $K_X \cdot V_i < 0$. Since $R_1 \ne R_2$ are rays of a salient cone (Corollary P7.3.14), $[V_1]$ and $[V_2]$ are linearly independent, so they span $N_1(X)$, of dimension $2$. By Proposition 6.4.3, $X$ is rationally connected.

### Exercises

1. (A) Show that a smooth quadric $Q \subseteq \mathbb{P}^{n+1}$, $n \ge 3$, satisfies Theorem 6.4.8 with chains of two lines, of anticanonical degree $n$.
2. (A) Use Proposition 6.4.9 to show that $\mathbb{P}^{a_1} \times \dots \times \mathbb{P}^{a_r}$ is rationally connected, and find a very free rational curve on it.
3. (B) Let $X = \operatorname{Bl}_C \mathbb{P}^3$ for a line $C$, as in Example 6.3.20. Only one of its rays is of fibre type. Show directly that $X$ is rationally connected, using Corollary P8.3.22 for the morphism $X \to \mathbb{P}^1$, and compare with Theorem 6.4.8.
4. (B) In Example 6.4.12, show that two general points of $W$ are not joined by a chain of two fibres, and find a single rational curve through them of anticanonical degree $4$.
5. (B) Show that the hypothesis $\rho(X) = 2$ in Proposition 6.4.10 cannot be dropped: give a smooth projective threefold with $\rho(X) = 3$ and two fibre type rays that is not rationally connected. (Try $E \times \mathbb{P}^1 \times \mathbb{P}^1$ for an elliptic curve $E$.)
6. (C) Let $X$ be a Fano variety of dimension $n$ in characteristic $0$. Using Theorem 6.4.8 and part 1 of Theorem P8.3.13, show that $X$ contains a very free rational curve, and explain why Theorem 6.4.8 does not bound its anticanonical degree.

### Lean

Nothing in this section is in Lean. The library states `MinimalModel.ConeTheoremKlt` and `MinimalModel.LengthOfExtremalRays` without proof, but has no notion of rational connectedness and no families of rational curves.

### Notes and history

Theorem 6.4.8 is due to Kollár, Miyaoka and Mori (KMM92b) and to Campana (Cam92). For the bound $n + 1$ on the degrees of the curves in the chains see Kol96, Theorem V.2.13, and Debarre's Chapter 5 (Deb01). The bound on the anticanonical degree of a single very free curve through two general points is a separate and weaker statement, of order $n^2$, and it gives the boundedness of smooth Fano varieties of a given dimension (KMM92b). The proof of Proposition 6.4.10 is in the spirit of the Picard number one case of KMM92a.
