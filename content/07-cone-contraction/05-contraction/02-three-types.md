---
title: Divisorial, small and fibre type contractions
nodes: [MMQ2K4RSHT]
sources: [KM98, Mat02, KMM87]
reads_with: [KM98:2.5, KM98:3.36, Mat02:ch8]
requires: [P3.6, P3.7, P4.6, 4.1, 4.2, 6.3, 7.4]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Divisorial, small and fibre type contractions

### Statement

Keep the notation of Section 1: $(X, \Delta)$ is a projective klt pair of dimension $d$ in characteristic $0$, $R$ is a $K_\Delta$-negative extremal ray, and $\varphi = \varphi_R \colon X \to Y$ is its contraction, from Theorem 7.5.2. The minimal model program needs to know what $\varphi$ does to the variety and to the pair. The answer depends on the dimension of the exceptional locus, and it is clean when $X$ is $\mathbb{Q}$-factorial, that is, when every Weil divisor has a Cartier multiple.

**Definition 7.5.8 (the exceptional locus and the three types).** The *exceptional locus* $\operatorname{Exc}(\varphi)$ is the set of points $x \in X$ at which the fibre $\varphi^{-1}(\varphi(x))$ has positive dimension. The contraction $\varphi$ is

1. of *fibre type* if $\dim Y < \dim X$;
2. *divisorial* if it is birational and $\operatorname{Exc}(\varphi)$ has codimension $1$ in $X$;
3. *small* if it is birational and $\operatorname{Exc}(\varphi)$ has codimension at least $2$ in $X$.

**Lemma 7.5.9 (birational contractions).** Let $\varphi$ be birational. Then $\operatorname{Exc}(\varphi)$ is closed, it is the union of the curves contracted by $\varphi$, the set $Z = \varphi(\operatorname{Exc}(\varphi))$ has codimension at least $2$ in $Y$, and $\varphi$ restricts to an isomorphism $X \setminus \operatorname{Exc}(\varphi) \to Y \setminus Z$, with $\operatorname{Exc}(\varphi) = \varphi^{-1}(Z)$.

Lean: not yet in Lean.

**Proposition 7.5.10 (the trichotomy).** Suppose $X$ is $\mathbb{Q}$-factorial and $\varphi$ is birational. Either $\varphi$ is small, or $\operatorname{Exc}(\varphi)$ is a prime divisor $E$ with $E \cdot R < 0$, that is $E \cdot C < 0$ for every curve $C$ with $[C] \in R$. So every contraction of a negative ray on a $\mathbb{Q}$-factorial klt pair is of exactly one of the three types.

Lean: not yet in Lean.

**Proposition 7.5.11 (divisorial contractions).** Suppose $X$ is $\mathbb{Q}$-factorial and $\varphi$ is divisorial with exceptional divisor $E$, and put $\Delta_Y = \varphi_* \Delta$. Then

1. $Y$ is $\mathbb{Q}$-factorial and $\rho(Y) = \rho(X) - 1$;
2. $K_Y + \Delta_Y$ is $\mathbb{Q}$-Cartier and $K_X + \Delta = \varphi^* (K_Y + \Delta_Y) + \alpha E$ with $\alpha = K_\Delta \cdot C / E \cdot C > 0$ for any curve $C$ with $[C] \in R$;
3. $(Y, \Delta_Y)$ is klt, and $a(G, Y, \Delta_Y) \ge a(G, X, \Delta)$ for every divisor $G$ over $X$, with strict inequality when the centre of $G$ on $X$ lies in $E$.

Lean: not yet in Lean.

**Proposition 7.5.12 (small contractions).** Suppose $X$ is $\mathbb{Q}$-factorial and $\varphi$ is small, and put $\Delta_Y = \varphi_* \Delta$. Then $K_Y + \Delta_Y$ is not $\mathbb{Q}$-Cartier. In particular $(Y, \Delta_Y)$ is not a pair in the sense of Definition 4.1.3, and the minimal model program cannot continue on $Y$.

Lean: not yet in Lean.

**Proposition 7.5.13 (fibre type contractions).** Suppose $X$ is $\mathbb{Q}$-factorial and $\varphi$ is of fibre type. Then $Y$ is $\mathbb{Q}$-factorial, $\rho(Y) = \rho(X) - 1$, and $-K_\Delta$ is positive on $\overline{NE}(X/Y) \setminus \{0\} = R \setminus \{0\}$. If $G$ is a general fibre of $\varphi$, then $G$ is normal, $(G, \Delta|_G)$ is klt, and $-(K_G + \Delta|_G)$ is ample: the general fibre is a log Fano variety.

Lean: not yet in Lean.

### Proof in words

Zariski's main theorem says that a birational contraction to a normal variety is an isomorphism away from the positive dimensional fibres, and dimension counting puts the image of these fibres in codimension $2$. On a $\mathbb{Q}$-factorial $X$, an exceptional prime divisor $E$ is a Cartier divisor up to a multiple, and its degree on $R$ decides everything. If $E \cdot R = 0$, the contraction theorem makes a multiple of $E$ a pullback of a line bundle on $Y$ that is trivial off codimension $2$, hence trivial, which is absurd for an effective divisor. If $E \cdot R > 0$, then $E$ plus a large multiple of the supporting divisor is ample, while every section of its multiples vanishes on $E$, because functions on $Y$ have no poles in codimension $2$. So $E \cdot R < 0$, every curve in $R$ lies in $E$, and $E$ is the whole exceptional locus. In the divisorial case one corrects a divisor on $X$ by a multiple of $E$ until it is zero on $R$, and the contraction theorem pushes it down as a Cartier divisor. This proves $\mathbb{Q}$-factoriality of $Y$, the formula for $K_X + \Delta$ and, by comparing discrepancies, that $Y$ is klt. In the small case the same correction is impossible, since there is no exceptional divisor, and $K_X + \Delta$ cannot be a pullback because it is negative on $R$. In the fibre type case every divisor that is a pullback over the smooth locus of $Y$ is zero on $R$, because general fibres avoid it.

### Examples

**Example 7.5.14 (a small contraction of a smooth fourfold).** Let $\mathcal{E} = \mathcal{O} \oplus \mathcal{O}(1) \oplus \mathcal{O}(1)$ on $\mathbb{P}^2$, $X = \mathbb{P}(\mathcal{E}) = \operatorname{\mathbf{Proj}} \operatorname{Sym} \mathcal{E}$ (Definition P3.6.33), a smooth fourfold with $\pi \colon X \to \mathbb{P}^2$, $\xi = \mathcal{O}_X(1)$ and $h = \pi^* \mathcal{O}(1)$, so $\rho(X) = 2$ by Proposition P3.6.35. The quotient $\mathcal{E} \to \mathcal{O}$ defines a section $S \cong \mathbb{P}^2$ with $\xi|_S \cong \mathcal{O}_S$, and the normal bundle of $S$ is $\mathcal{H}om(\mathcal{O}(1)^{\oplus 2}, \mathcal{O}) = \mathcal{O}(-1)^{\oplus 2}$. Let $\ell \subseteq S$ be a line and $f$ a line in a fibre of $\pi$. Then $\xi \cdot f = 1$, $h \cdot f = 0$, $\xi \cdot \ell = 0$, $h \cdot \ell = 1$, and
$$K_X = -3 \xi + \pi^* (K_{\mathbb{P}^2} + \det \mathcal{E}) = -3 \xi - h, \qquad K_X \cdot f = -3, \quad K_X \cdot \ell = -1.$$
Both $\xi$ and $h$ are free, since $\mathcal{E}$ is globally generated, and the two bases are dual, so $\overline{NE}(X) = \langle f, \ell \rangle$ and $X$ is Fano by Theorem P7.3.13. The ray $\mathbb{R}_{\ge 0} [f]$ is contracted by $\pi$, of fibre type. The ray $\mathbb{R}_{\ge 0} [\ell]$ is cut out by $\xi$, and $|\xi|$ maps $X$ to $\mathbb{P}(H^0(\mathcal{E})) = \mathbb{P}^6$ onto the projective cone over the Segre embedding of $\mathbb{P}(\mathcal{O}(1)^{\oplus 2}) \cong \mathbb{P}^2 \times \mathbb{P}^1$ in $\mathbb{P}^5$. It contracts $S$ to the vertex and is an isomorphism elsewhere, so $\operatorname{Exc}(\varphi) = S$ has codimension $2$ and the contraction is small. By Proposition 7.5.12, $K_Y$ is not $\mathbb{Q}$-Cartier at the vertex. By Corollary 6.3.4 this cannot happen in dimension $3$ for smooth $X$.

**Example 7.5.15 (the discrepancy of a divisorial contraction).** For the blow-up $\pi \colon X = \operatorname{Bl}_p \mathbb{P}^d \to \mathbb{P}^d$ of Example 7.5.7, $K_X = \pi^* K_{\mathbb{P}^d} + (d - 1) E$, and with $C = e$ a line in $E$, $K_X \cdot e = -(d - 1)$ and $E \cdot e = -1$, so $\alpha = d - 1$, as part 2 of Proposition 7.5.11 predicts. For the contraction $\pi \colon \mathbb{F}_n \to \mathbb{P}(1, 1, n)$ of Example 7.5.6 with $\Delta = c \, C_-$, $\frac{n - 2}{n} < c < 1$, Example 7.4.21 gives
$$K_{\mathbb{F}_n} + c \, C_- = \pi^* K_Y + \Bigl( c - \frac{n - 2}{n} \Bigr) C_-,$$
with $\Delta_Y = 0$ and $\alpha = c - \frac{n-2}{n} > 0$. The ratio $K_\Delta \cdot C_- / C_-^2 = ((n - 2) - c n)/(-n)$ is the same number. The image $Y$ is klt, with $a(C_-, Y, 0) = -\frac{n-2}{n} > a(C_-, X, \Delta) = -c$.

**Example 7.5.16 ($\mathbb{Q}$-factoriality is needed).** Let $Y_0 = V(xy - zw) \subseteq \mathbb{A}^4$ be the cone over a smooth quadric surface, and $\bar Y \subseteq \mathbb{P}^4$ its projective closure, the cone over $\mathbb{P}^1 \times \mathbb{P}^1 \subseteq \mathbb{P}^3$. It has two small resolutions $X_1 \to \bar Y$ and $X_2 \to \bar Y$ (Example P4.6.13 locally), each replacing the vertex by a line, and the blow-up $\tilde Y \to \bar Y$ of the vertex, with exceptional divisor $Q \cong \mathbb{P}^1 \times \mathbb{P}^1$, factors through both. On $\tilde Y$, which is smooth, the contraction $\tilde Y \to X_1$ contracts $Q$ along one ruling: it is divisorial onto a curve. The contraction $X_1 \to \bar Y$ is small and $X_1$ is smooth, hence $\mathbb{Q}$-factorial, so Proposition 7.5.12 applies to it if it is $K$-negative. It is not: the exceptional line $\ell_1$ has normal bundle $\mathcal{O}(-1)^{\oplus 2}$, so $K_{X_1} \cdot \ell_1 = 0$, in accordance with Corollary 6.3.4. On $\bar Y$ itself, which is not $\mathbb{Q}$-factorial, the plane $\{x = z = 0\}$ is a Weil divisor with no Cartier multiple at the vertex.

### Proof

*Lemma 7.5.9.* The variety $Y$ is normal by Theorem 7.5.2, so Corollary P4.6.10 applies: the set $U$ of $y \in Y$ with finite fibre is open, $\varphi^{-1}(U) \to U$ is an isomorphism, and every fibre over $Z = Y \setminus U$ is connected of positive dimension at every point. So $\operatorname{Exc}(\varphi) = \varphi^{-1}(Z)$ is closed. Every point of a positive dimensional projective fibre lies on a curve in the fibre, so $\operatorname{Exc}(\varphi)$ is the union of the contracted curves. If an irreducible component $W$ of $Z$ had codimension $1$, every fibre over $W$ would have dimension at least $1$, so $\dim \varphi^{-1}(W) \ge \dim W + 1 = d$, and the closed set $\varphi^{-1}(W)$ would be all of $X$, against the birationality of $\varphi$.

*Proposition 7.5.10.* Suppose $\operatorname{Exc}(\varphi)$ contains a prime divisor $E$, and choose $m \ge 1$ with $m E$ Cartier. Let $C$ be a curve with $[C] \in R$, so $R = \mathbb{R}_{\ge 0} [C]$ by Corollary 7.4.12, and let $U = Y \setminus Z$ as in Lemma 7.5.9, so $E \cap \varphi^{-1}(U) = \emptyset$.

If $E \cdot C = 0$, then $\mathcal{O}_X(m E) \cong \varphi^* M$ for a line bundle $M$ on $Y$, by part 2 of Theorem 7.5.2. Since $\mathcal{O}_X(m E)$ is trivial on $\varphi^{-1}(U) \cong U$, $M|_U \cong \mathcal{O}_U$. The section $1$ of $M|_U$ and its inverse in $M^{-1}|_U$ extend to $Y$ by Theorem P3.7.33, as $Z$ has codimension at least $2$ and $Y$ is normal, and their product is $1$, so $M \cong \mathcal{O}_Y$. Then $m E \sim 0$, which is impossible for a nonzero effective divisor, since $m E \cdot H^{d-1} > 0$ for $H$ ample.

If $E \cdot C > 0$, let $A$ be very ample on $Y$, so that $L = \varphi^* A$ is nef with $F_L = R$ (part 1 of Theorem 7.5.2). By Lemma 7.4.2, $m E + k L$ is ample for some $k$, and $N(m E + k L)$ is very ample for some $N$. Now $\varphi_* \mathcal{O}_X(N m E) = \mathcal{O}_Y$: a section of $\mathcal{O}_X(N m E)$ over $\varphi^{-1}(V)$, $V \subseteq Y$ open, is a rational function $s$ regular on $\varphi^{-1}(V) \setminus E \supseteq \varphi^{-1}(V \cap U)$. So $s$ is a regular function on $V \cap U$, it extends to $V$ by Theorem P3.7.33, and $s$ is regular on $\varphi^{-1}(V)$. By the projection formula, $H^0(X, \mathcal{O}_X(N m E + N k L)) = H^0(Y, A^{N k})$, and every section of $\mathcal{O}_X(N m E + N k L)$ is the product of $\varphi^* t$ with the canonical section of $\mathcal{O}_X(N m E)$, which vanishes on $E$. A very ample linear system has no base points, a contradiction.

So $E \cdot C < 0$. If $C'$ is a curve with $[C'] \in R$, then $E \cdot C' < 0$, so $C' \subseteq E$. By Lemma 7.5.9, $\operatorname{Exc}(\varphi)$ is the union of such curves, so $\operatorname{Exc}(\varphi) \subseteq E$, and $\operatorname{Exc}(\varphi) = E$. If $\operatorname{Exc}(\varphi)$ contains no divisor, $\varphi$ is small.

*Proposition 7.5.11.* Let $C$ be a curve with $[C] \in R$; then $E \cdot C < 0$ by Proposition 7.5.10, and $\rho(Y) = \rho(X) - 1$ by Corollary 7.5.3. For part 1, let $D$ be a prime divisor on $Y$, $D'$ its strict transform on $X$, and $m \ge 1$ with $m D'$ and $m E$ Cartier. Put $e = -D' \cdot C / E \cdot C \in \mathbb{Q}$ and choose $N \ge 1$ with $N m e \in \mathbb{Z}$. Then $N m (D' + e E)$ is Cartier and zero on $C$, so it is $\varphi^* M$ for a line bundle $M$ on $Y$. On $U = Y \setminus \varphi(E)$, $M|_U \cong \mathcal{O}_U(N m D)$, and $\varphi(E)$ has codimension at least $2$ by Lemma 7.5.9. A line bundle and a reflexive sheaf of rank $1$ on a normal variety that agree off codimension $2$ agree, by Theorem P3.7.33, so $\mathcal{O}_Y(N m D) \cong M$ and $N m D$ is Cartier.

For part 2, choose $m$ with $m (K_X + \Delta)$ and $m E$ Cartier and $m \alpha \in \mathbb{Z}$, where $\alpha = K_\Delta \cdot C / E \cdot C$, positive since both numbers are negative. The Cartier divisor $m (K_X + \Delta - \alpha E)$ is zero on $C$, so it is $\varphi^* M$, and as in part 1, $M \cong \mathcal{O}_Y(m (K_Y + \Delta_Y))$, because $K_X + \Delta - \alpha E$ restricts to $K_U + \Delta_Y|_U$ on $U$. So $K_Y + \Delta_Y$ is $\mathbb{Q}$-Cartier and $K_X + \Delta = \varphi^* (K_Y + \Delta_Y) + \alpha E$.

For part 3, let $f \colon X' \to X$ be a log resolution and $g = \varphi \circ f$. By Definition 4.1.4,
$$K_{X'} = g^* (K_Y + \Delta_Y) + \alpha f^* E + \sum_G a(G, X, \Delta) G = g^* (K_Y + \Delta_Y) + \sum_G \bigl( a(G, X, \Delta) + \alpha \operatorname{mult}_G f^* E \bigr) G,$$
so $a(G, Y, \Delta_Y) = a(G, X, \Delta) + \alpha \operatorname{mult}_G f^* E$. The second term is nonnegative, and positive exactly when the centre of $G$ lies in $E$. Every divisor over $Y$ appears on some such $X'$, and $(X, \Delta)$ is klt, so $(Y, \Delta_Y)$ is klt by Definition 4.2.1.

*Proposition 7.5.12.* Suppose $m (K_Y + \Delta_Y)$ is Cartier. The Cartier divisors $m (K_X + \Delta)$ and $\varphi^* m (K_Y + \Delta_Y)$ agree on $X \setminus \operatorname{Exc}(\varphi)$, whose complement has codimension at least $2$. Two Cartier divisors on a normal variety that agree off codimension $2$ are linearly equivalent, by Theorem P3.7.33 applied to the quotient of the two line bundles, so $m K_\Delta = \varphi^* m (K_Y + \Delta_Y)$ in $N^1(X)$ and $K_\Delta \cdot C = 0$ for $[C] \in R$, against $K_\Delta \cdot R < 0$.

*Proposition 7.5.13.* By Corollary 7.5.3, $\rho(Y) = \rho(X) - 1$, and $\overline{NE}(X/Y) = F_\varphi = R$, on which $-K_\Delta$ is positive. Let $D$ be a prime divisor on $Y$ and $U \subseteq Y$ the smooth locus, whose complement has codimension at least $2$. The divisor $D|_U$ is Cartier, and $\varphi^*(D|_U)$ is a Cartier divisor on $\varphi^{-1}(U)$; let $D'$ be its closure in $X$, a Weil divisor, and $m$ such that $m D'$ is Cartier. A general fibre of $\varphi$ lies over $U \setminus D$, is positive dimensional and contains a curve $C_0$, with $[C_0] \in R$, disjoint from $D'$. So $D' \cdot C_0 = 0$, $D' \cdot R = 0$, and $m D' = \varphi^* M$ by part 2 of Theorem 7.5.2. Over $U$, $\varphi^* M|_U \cong \varphi^* \mathcal{O}_U(m D)$, and $\varphi^*$ is injective on line bundles because $\varphi_* \mathcal{O}_X = \mathcal{O}_Y$, so $M|_U \cong \mathcal{O}_U(m D)$, and $m D$ is Cartier as in the proof of Proposition 7.5.11. For the general fibre $G$: the generic fibre of $\varphi$ is normal, being a localization of $X$, and geometrically normal because $k$ has characteristic $0$, so the general fibre is normal. Its normal bundle is trivial, so $K_G + \Delta|_G = (K_X + \Delta)|_G$. If $f \colon X' \to X$ is a log resolution of $(X, \Delta)$, generic smoothness in characteristic $0$ makes the general fibre $G'$ of $\varphi \circ f$ smooth and transversal to every stratum of the snc divisor $\operatorname{Exc}(f) \cup f^{-1}_* \Delta$, so $G' \to G$ is a log resolution of $(G, \Delta|_G)$ whose discrepancies are among those of $(X, \Delta)$, and $(G, \Delta|_G)$ is klt. The restriction of $-K_\Delta$ to $G$ is positive on $\overline{NE}(G) \setminus \{0\}$, since the image of $\overline{NE}(G)$ in $N_1(X)$ lies in $R$ and the restriction to $G$ of an ample class on $X$ is ample. So $-(K_G + \Delta|_G)$ is ample by Theorem P7.3.13.

### Exercises

1. (A) For the contraction $X \to \mathbb{P}^6$ of Example 7.5.14, compute the images of the curves $f$ and of the fibres of $\pi$, and show that the fibres of $\pi$ map isomorphically onto planes through the vertex.
2. (A) Let $X = \operatorname{Bl}_p \mathbb{P}^2$ with $\Delta = c E$, $0 \le c < 1$. Compute $\alpha$ of Proposition 7.5.11 for the blow-down and check part 3 for $E$.
3. (B) Let $\mathcal{E} = \mathcal{O} \oplus \mathcal{O}(1)^{\oplus r}$ on $\mathbb{P}^s$ with $r \ge 1$, $s \ge 1$, and $X = \mathbb{P}(\mathcal{E})$. Compute $K_X \cdot \ell$ for a line $\ell$ in the section $S$ of Example 7.5.14, and decide for which $(r, s)$ the contraction of $\mathbb{R}_{\ge 0} [\ell]$ is $K_X$-negative, small or divisorial.
4. (B) Show that the flip of Example 7.5.14 is $X^+ = \mathbb{P}(\mathcal{O} \oplus \mathcal{O}(1)^{\oplus 3})$ over $\mathbb{P}^1$: show that it has a small contraction to the same cone, with exceptional locus a curve $\ell^+$ on which $K_{X^+} \cdot \ell^+ = 1$.
5. (B) Show that a contraction of fibre type onto a point occurs exactly when $\rho(X) = 1$ and $-K_\Delta$ is ample, and check Proposition 7.5.13 for $X = \mathbb{P}(1, 1, n)$ of Example 7.4.21.
6. (C) Let $\varphi$ be a divisorial contraction of a $\mathbb{Q}$-factorial klt pair with $\Delta = 0$ and $X$ terminal. Show that $Y$ is terminal, and that if $X$ is smooth and $\varphi$ contracts $E$ to a point then $E$ is covered by curves $C$ with $0 < -K_X \cdot C \le 2(d - 1)$.

### Lean

None of the statements of this section is in Lean yet. The input is `MinimalModel.ContractionTheorem`, a statement without proof.

### Notes and history

The trichotomy and the behaviour of $\mathbb{Q}$-factoriality and discrepancies under divisorial contractions are KM98, Propositions 3.36 and 3.37 and Corollary 3.43, following Kawamata, Matsuda and Matsuki (KMM87). Small contractions occur already for smooth fourfolds, as in Example 7.5.14, and the failure of $K_Y + \Delta_Y$ to be $\mathbb{Q}$-Cartier is the reason the minimal model program needs flips. For smooth threefolds Mori's theorem (Corollary 6.3.4) excludes small contractions, but they appear for terminal threefolds.
