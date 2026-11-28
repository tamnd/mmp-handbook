---
title: Lines on a cubic surface as minimal rational curves
nodes: []
sources: [Kol96, Deb01, Har77, Hwa01]
reads_with: [Har77:V.4, Kol96:IV.2, Deb01:ch2]
requires: [2.2, P5.10, P5.12, P8.1, P8.2]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Lines on a cubic surface as minimal rational curves

### Statement

Let $P_1, \dots, P_6 \in \mathbb{P}^2$ be in general position, $X_6$ the blow-up, and $S \subseteq \mathbb{P}^3$ its image under the anticanonical embedding of Theorem P5.10.3, a smooth cubic surface with $-K_S = H$ the hyperplane class. Every smooth cubic surface over $k$ arises in this way (Har77, Remark V.4.7.1), so the results below hold for every smooth cubic surface. The cubic surface shows the two faces of minimality. Its lines are the rational curves of least anticanonical degree, and they span the extremal rays of the cone, but they do not move. The rational curves of least degree through a general point are conics.

**Proposition 6.1.18 (the lines as minimal curves of the extremal rays).**

1. The rational curves $\Gamma \subseteq S$ with $-K_S \cdot \Gamma = 1$ are exactly the $27$ lines of Theorem P5.10.5.
2. For a line $L$ and an isomorphism $f \colon \mathbb{P}^1 \to L$, the component of $\operatorname{Hom}(\mathbb{P}^1, S)$ through $[f]$ is $f \circ \operatorname{PGL}_2$, of dimension $3 = -K_S \cdot L + n$, so $\operatorname{Locus}(V) = L$ for the family $V$ of $L$.
3. Each line spans a $K_S$-negative extremal ray $R_L$ of $\overline{NE}(S) = NE(S)$, these $27$ rays are all the extremal rays, and $\ell(R_L) = 1$ in the notation of Lemma 6.1.6. Every class $[L]$ is unsplit.

Lean: not yet in Lean.

**Proposition 6.1.19 (the conics on a cubic surface).** Let $L \subseteq S$ be a line.

1. The planes through $L$ cut $S$ in $L$ and a residual conic, and the residual conics form a base point free pencil $|H - L|$ with $(H - L)^2 = 0$. Its morphism $\pi_L \colon S \to \mathbb{P}^1$ has exactly $5$ singular fibres, each a pair of lines meeting in a point.
2. The rational curves $\Gamma$ with $-K_S \cdot \Gamma = 2$ are the smooth members of the $27$ pencils $|H - L|$.
3. A smooth conic $C$ has $N_{C/S} \cong \mathcal{O}_{\mathbb{P}^1}$ and $f^* T_S \cong \mathcal{O}(2) \oplus \mathcal{O}$ for an isomorphism $f \colon \mathbb{P}^1 \to C$. It is free and not very free, and the component of $\operatorname{Hom}(\mathbb{P}^1, S)$ through $[f]$ is smooth of dimension $4$ at $[f]$.
4. The minimal rational components of $S$ (Definition 6.1.13, in characteristic $0$) are the $27$ families of conics of the pencils $|H - L|$. Through a point $x$ that lies on no line there passes exactly one conic of each pencil, so $27$ conics in all, and the VMRT of each family at $x$ is a single point of $\mathbb{P}(T_x S)$.

Lean: not yet in Lean.

### Proof in words

A curve of degree $1$ in $\mathbb{P}^3$ is a line, so the curves of anticanonical degree $1$ are the lines, and Volume P8 has already shown that they are rigid with normal bundle $\mathcal{O}(-1)$. Since $-K_S$ is the hyperplane class, a sum of two nonzero cycles has degree at least $2$, so lines are unsplit, and the cone theorem for del Pezzo surfaces of Volume 2 says that they span all the extremal rays. A family of rational curves that sweeps out $S$ must therefore have degree at least $2$. A curve of degree $2$ spans a plane, and the plane meets $S$ in the conic and a residual line, so the conics fall into the $27$ pencils residual to the lines. A conic has self-intersection $0$, hence trivial normal bundle, so it is free, and it moves in its pencil through every point. The VMRT is a point because only one member of a pencil passes through a given point.

### Examples

**Example 6.1.20 (the Fermat cubic).** For the Fermat cubic $S = V(x_0^3 + x_1^3 + x_2^3 + x_3^3)$ in characteristic different from $3$, the $27$ lines are $V(x_a + \zeta x_b, x_c + \zeta' x_d)$ for the three pairings $\{\{a, b\}, \{c, d\}\}$ and $\zeta, \zeta' \in \mu_3$ (Example P5.10.7). For $L = V(x_0 + x_1, x_2 + x_3)$, the planes through $L$ are $V(\lambda (x_0 + x_1) - \mu (x_2 + x_3))$, and on such a plane $x_0^3 + x_1^3 = (x_0 + x_1)(x_0^2 - x_0 x_1 + x_1^2)$ and $x_2^3 + x_3^3 = (x_2 + x_3)(x_2^2 - x_2 x_3 + x_3^2)$. So for $\mu \ne 0$ the residual conic is cut out by $\mu (x_0^2 - x_0 x_1 + x_1^2) + \lambda (x_2^2 - x_2 x_3 + x_3^2)$ on the plane. The pencil $\pi_L$ is $[\lambda : \mu]$, and the members through a general point of $S$ are smooth conics.

**Example 6.1.21 (twisted cubics and the decomposition of classes).** In the notation of Theorem P5.10.5, the class $\ell$ of the pullback of a line of $\mathbb{P}^2$ has $\ell^2 = 1$ and $-K_S \cdot \ell = 3$, so its smooth members are twisted cubics on $S$. They form a family of dimension $-K_S \cdot \ell + 2 = 5$, namely the $2$-dimensional family of lines in $\mathbb{P}^2$ times the $3$-dimensional group $\operatorname{PGL}_2$. Their class splits as $\ell = (\ell - E_1) + E_1$, a conic of the pencil $|H - G_1|$ plus a line: indeed $H - G_1 = 3 \ell - \sum_k E_k - 2 \ell + \sum_{k \ne 1} E_k = \ell - E_1$. The members of $|\ell|$ that contain $E_1$ are the total transforms of the lines of $\mathbb{P}^2$ through $P_1$, and they are the members of the family that split in this way.

### Proof

*Proposition 6.1.18.* (1) By Theorem P5.10.3, the image of an integral curve $\Gamma \subseteq X_6$ is a curve of degree $-K \cdot \Gamma$ in $\mathbb{P}^3$, and a curve of degree $1$ is a line. Conversely a line $L$ has $H \cdot L = 1$. (2) This is Proposition P8.1.18: the component through $[f]$ has the $k$-points $f \circ \operatorname{PGL}_2$ and is smooth of dimension $3$. Every member has image $L$, so $\operatorname{Locus}(V) = L$. (3) By Theorem 2.2.2, $\overline{NE}(S) = NE(S)$ is spanned by the $(-1)$-curves, each spanning an extremal ray, and these are all the extremal rays; by part 2 of Theorem P5.10.5 the $(-1)$-curves are the $27$ lines. Each ray is $K_S$-negative since $-K_S$ is ample. Integral curves have $-K_S \cdot \Gamma \ge 1$, so $\ell(R_L) = 1$, and $[L]$ is unsplit by Lemma 6.1.6. Directly, a sum of two nonzero effective cycles has $H$-degree at least $2$.

*Proposition 6.1.19.* (1) A plane $\Pi \supseteq L$ cuts $S$ in a cubic curve $\Pi \cap S = L + C_\Pi$ with $C_\Pi$ of degree $2$, so $C_\Pi \in |H - L|$. The pencil of planes through $L$ gives the pencil $|H - L|$, and $(H - L)^2 = H^2 - 2 H \cdot L + L^2 = 3 - 2 - 1 = 0$. Two distinct members meet in $(H - L)^2 = 0$ points, so the pencil has no base points and defines $\pi_L \colon S \to \mathbb{P}^1$. For $L = G_6$ this is the conic bundle of Example P5.10.8. A singular member is a plane conic that is not integral, so a pair of distinct lines or a double line. If a member were $2M$ for a line $M$, then $(H - L) \cdot M = 2 M^2 = -2$; but $(H - L) \cdot M = 1 - L \cdot M \ge 0$ for $M \ne L$, and $M = L$ would give $H = 3L$, against $H^2 = 3$. So double lines do not occur, and the singular fibres are pairs of lines $M + M'$ with $M \cdot M' = 1$. The topological Euler characteristic, or over any field the $\ell$-adic one, gives $e(S) = e(\mathbb{P}^1) \, e(\mathbb{P}^1) + s$ for a conic bundle with $s$ singular fibres, each of which adds $1$. Since $S$ is $\mathbb{P}^2$ blown up in $6$ points, $e(S) = 3 + 6 = 9$, so $s = 9 - 4 = 5$.

(2) A rational curve $\Gamma$ with $H \cdot \Gamma = 2$ is a curve of degree $2$ in $\mathbb{P}^3$, hence a smooth plane conic, since it is integral. Its plane $\Pi$ meets $S$ in a cubic curve containing $\Gamma$, so $\Pi \cap S = \Gamma + M$ with $M$ a line, and $\Gamma \in |H - M|$. Conversely a smooth member of $|H - L|$ is a rational curve of degree $(H - L) \cdot H = 2$.

(3) The normal bundle $N_{C/S} = \mathcal{O}_C(C)$ has degree $C^2 = 0$, so it is trivial on $C \cong \mathbb{P}^1$. The sequence $0 \to T_C \to T_S|_C \to N_{C/S} \to 0$ is $0 \to \mathcal{O}(2) \to f^* T_S \to \mathcal{O} \to 0$, and $\operatorname{Ext}^1(\mathcal{O}, \mathcal{O}(2)) = H^1(\mathcal{O}(2)) = 0$, so it splits. Then $H^1(f^* T_S) = 0$, and Corollary P8.1.13 gives smoothness of dimension $-K_S \cdot C + 2 = 4$: one parameter for the conic in its pencil and three for $\operatorname{PGL}_2$.

(4) Let $k$ have characteristic $0$. By (3) and part 3 of Theorem P8.3.4 each family of conics is dominating. A dominating family of rational curves has degree at least $2$: by (1) of Proposition 6.1.18 a family of degree $1$ has locus a line. So the minimal rational components are the dominating families of degree $2$, and by (2) these are the $27$ families of conics, one for each pencil, since the smooth members of one pencil form a connected family and two pencils have different classes. If $x$ lies on no line, the fibre $\pi_L^{-1}(\pi_L(x))$ is the unique member of $|H - L|$ through $x$, and it is smooth since the singular members are unions of lines. So each family $V_L$ has a single curve through $x$, and its VMRT at $x$ is the tangent direction of that conic, a point, of dimension $0 = -K_S \cdot C - 2$ as in Lemma 6.1.14.

### Exercises

1. (A) Show that two residual conics $C \in |H - L|$ and $C' \in |H - L'|$ satisfy $C \cdot C' = 1 + L \cdot L'$, and deduce that the conics through a point $x$ in pencils of disjoint lines meet transversally at $x$.
2. (A) Let $L$, $M$, $M'$ be three coplanar lines on $S$. Show that $M + M'$ is a singular member of $|H - L|$, and that the $5$ singular fibres of $\pi_L$ account for the $10$ lines that meet $L$.
3. (B) Check the dimension estimate of Corollary P8.1.12 for the line, the conic and the twisted cubic of Example 6.1.21, with $0$, $1$ and $2$ points fixed, and decide in which cases it is an equality.
4. (B) Show that the class $\ell$ of Example 6.1.21 can be written as a sum of a conic class and a line class in exactly $6$ ways using the classes $\ell - E_i$ and $E_i$, and find a second family of twisted cubics whose class is not $\ell$.
5. (B) Let $x \in S$ lie on exactly one line $L$. Show that the conic of $|H - M|$ through $x$ is smooth for every line $M \ne L$ that does not meet $L$, and count how many of the $27$ pencils have a singular member through $x$.
6. (C) Assume $k = \mathbb{C}$. Show that the union of the $27$ VMRTs at a general point $x$ consists of $27$ distinct points of $\mathbb{P}(T_x S)$. (Hint: if two conics through $x$ were tangent at $x$, use Exercise 1 to find the lines involved, and show that the set of such $x$ is a curve.)

### Lean

The library has no cubic surfaces, no lines and no Hom schemes, so Proposition 6.1.18 and Proposition 6.1.19 are not yet in Lean.

### Notes and history

The $27$ lines are due to Cayley and Salmon (1849), and the conic bundle structures residual to the lines are classical. That the lines are the extremal rays of the cone of a cubic surface is the del Pezzo case of the cone theorem for surfaces (Theorem 2.2.2). The contrast between minimal curves of an extremal ray, which may be rigid, and minimal rational curves through a general point, which are free, is the starting point of the theory of varieties of minimal rational tangents (Hwa01); Kol96, Section IV.2, treats the families of minimal degree, and Deb01, Chapter 2, works the lines on hypersurfaces.
