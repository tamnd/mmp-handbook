---
title: Cyclic covers and the covering trick
nodes: []
sources: [Laz04, KM98, EV92, BG71, Har77, Mat86]
reads_with: [Laz04:4.1, KM98:2.5, EV92:3]
requires: [P3.10, P3.12, P4.4, P4.7, P4.9, P5.6, P7.3]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Cyclic covers and the covering trick

### Statement

Throughout, $X$ is a smooth projective variety of dimension $n$ over $k$, of characteristic $0$, and the language of snc divisors is that of Definition P7.8.1. For a reduced snc divisor $D = \sum_{j=1}^r D_j$ and a subset $J \subseteq \{1, \dots, r\}$, the *stratum* $D_J = \bigcap_{j \in J} D_j$ is smooth of pure codimension $|J|$ or empty, with $D_\emptyset = X$. A *smooth divisor* is a reduced divisor whose support is smooth; it may be disconnected, and its connected components are its prime components.

**Lemma P7.8.8 (Bertini for snc divisors).** Let $D = \sum_j D_j$ be a reduced snc divisor on $X$ and $V \subseteq H^0(X, L)$ a linear system without base points. For a general $s \in V$, the divisor $H = \operatorname{div}(s)$ is smooth, $D + H$ is snc, and $H \cap D_J$ is smooth of pure codimension $1$ in $D_J$ or empty for every $J$.

Lean: not in Lean as stated.

**Lemma P7.8.9 (trace splitting).** Let $f \colon Y \to X$ be a finite flat surjective morphism of degree $d$ from a smooth projective scheme $Y$ of pure dimension $n$. Then:

1. $f_* \mathcal{O}_Y$ is locally free of rank $d$, and the trace $\operatorname{Tr} \colon f_* \mathcal{O}_Y \to \mathcal{O}_X$, sending a local section $b$ to the trace of multiplication by $b$, satisfies $\operatorname{Tr}(1) = d$.
2. $f_* \omega_Y \cong \mathcal{H}om_{\mathcal{O}_X}(f_* \mathcal{O}_Y, \omega_X)$ as $f_* \mathcal{O}_Y$-modules. Under this isomorphism the maps $\iota \colon \omega_X \to f_* \omega_Y$, $\alpha \mapsto \alpha \circ \operatorname{Tr}$, and $\tau \colon f_* \omega_Y \to \omega_X$, $\varphi \mapsto \varphi(1)$, satisfy $\tau \circ \iota = d$.
3. For every line bundle $M$ on $X$, every $f_* \mathcal{O}_Y$-submodule $\mathcal{G} \subseteq f_*(\omega_Y \otimes f^* M)$ that contains $\iota(\omega_X) \otimes M$, and every $i$, the map $H^i(X, \omega_X \otimes M) \to H^i(X, \mathcal{G})$ induced by $\iota$ is injective.

Lean: not in Lean as stated.

**Proposition P7.8.10 (cyclic covers).** Let $L$ be a line bundle on $X$, $q \geq 2$, and $s \in H^0(X, L^q)$ a section whose divisor $D = \operatorname{div}(s)$ is smooth and reduced. Make $\mathcal{A} = \bigoplus_{i=0}^{q-1} L^{-i}$ an $\mathcal{O}_X$-algebra by the multiplication $L^{-i} \otimes L^{-j} \to L^{-i-j}$ for $i + j < q$ and $L^{-i} \otimes L^{-j} \to L^{-i-j} \xrightarrow{s} L^{-i-j+q}$ for $i + j \geq q$, and let $h \colon Y = \operatorname{Spec}_X \mathcal{A} \to X$.

1. $h$ is finite and flat of degree $q$, and étale over $X \setminus D$.
2. $Y$ is a smooth projective scheme of pure dimension $n$.
3. The tautological section $z$ of $h^* L$ has $z^q = h^* s$, its divisor $D' = \operatorname{div}(z)$ is smooth and maps isomorphically to $D$, and $h^* D = q D'$, $h^* L \cong \mathcal{O}_Y(D')$.
4. The image of $\iota \colon \omega_X \to h_* \omega_Y$ generates the subsheaf $h_*(\omega_Y(-(q-1)D'))$ as an $h_* \mathcal{O}_Y$-module, so $\omega_Y \cong h^* \omega_X \otimes \mathcal{O}_Y((q-1) D')$.
5. If $\Delta_1, \dots, \Delta_m$ are smooth divisors such that $D + \Delta_1 + \dots + \Delta_m$ is a reduced snc divisor, then $D' + h^* \Delta_1 + \dots + h^* \Delta_m$ is a reduced snc divisor and every $h^* \Delta_c$ is a smooth divisor.

Lean: not in Lean as stated.

**Proposition P7.8.11 (Bloch-Gieseker covers).** Let $L$ be a line bundle on $X$, $q \geq 1$, and $D = D_1 + \dots + D_r$ a reduced snc divisor with every $D_j$ a smooth divisor. There is a finite flat surjective morphism $g \colon X' \to X$ from a smooth projective scheme $X'$ of pure dimension $n$ and a line bundle $L'$ on $X'$ such that $g^* L \cong L'^{q}$, $g^* D$ is a reduced snc divisor, and every $g^* D_j$ is a smooth divisor.

Lean: not in Lean as stated.

### Proof in words

The covering trick moves a problem about a fractional divisor on $X$ to a problem about an integral divisor on a cover $Y$, and the trace brings the answer back. In characteristic $0$ the trace divided by the degree splits $\mathcal{O}_X \to f_* \mathcal{O}_Y$, and its dual splits $\omega_X \to f_* \omega_Y$, so cohomology of an adjoint bundle on $X$ is a direct summand of cohomology of an adjoint bundle on $Y$. If it vanishes on $Y$, it vanishes on $X$.

Two covers are needed. The cyclic cover extracts a $q$-th root of a smooth divisor $D$: locally it is $z^q = t$, with $t$ an equation of $D$, so $Y$ is smooth with coordinate $z$ in place of $t$, the divisor $D$ pulls back to $q$ times the reduced divisor $D' = \{z = 0\}$, and $q$-th roots of the coefficients along $D$ become integers. The local computation also measures the canonical sheaf: the dual of $B = R[z]/(z^q - t)$ over $R$ is generated by the coefficient of $z^{q-1}$, and the trace is $q z^{q-1}$ times this generator. So forms pulled back from $X$ vanish to order $q - 1$ along $D'$, which is the Hurwitz formula $\omega_Y = h^* \omega_X((q-1)D')$. The cyclic cover needs $\mathcal{O}_X(D)$ to be a $q$-th power. The cover of Bloch and Gieseker makes it one: a line bundle generated by its global sections is pulled back from $\mathcal{O}(1)$ on a projective space, and the Kummer map $[x_i] \mapsto [x_i^q]$ pulls $\mathcal{O}(1)$ back to $\mathcal{O}(q)$. Locally the Kummer cover is a product of cyclic covers branched along hyperplanes, and if the hyperplanes are general, Bertini's theorem keeps everything snc.

### Examples

**Example P7.8.12 (a double cover of the plane).** Let $X = \mathbb{P}^2$, $L = \mathcal{O}(1)$, $q = 2$ and $s$ a quadratic form whose conic $D$ is smooth. Then $Y = \operatorname{Spec}(\mathcal{O} \oplus \mathcal{O}(-1))$ is the quadric $\{w^2 = s(x_0, x_1, x_2)\} \subseteq \mathbb{P}^3$, and $h$ is the projection from the point $[0 : 0 : 0 : 1]$, which does not lie on $Y$. So $Y \cong \mathbb{P}^1 \times \mathbb{P}^1$, $h^* \mathcal{O}(1) = \mathcal{O}(1, 1)$, and $D' = \{w = 0\}$ is a conic of class $(1, 1)$, in agreement with part 3. Part 4 predicts $\omega_Y = h^* \mathcal{O}(-3) \otimes \mathcal{O}(1, 1) = \mathcal{O}(-2, -2)$, which is right. By the projection formula $h_* \mathcal{O}_Y(-1, -1) = h_* h^* \mathcal{O}(-1) = \mathcal{O}(-1) \oplus \mathcal{O}(-2)$, and $h_* \omega_Y = \mathcal{O}(-2) \oplus \mathcal{O}(-3)$, which is $\mathcal{H}om(\mathcal{O} \oplus \mathcal{O}(-1), \mathcal{O}(-3))$ as part 2 of Lemma P7.8.9 says. The trace splitting shows $H^i(\mathbb{P}^2, \mathcal{O}(m))$ is a direct summand of $H^i(Y, \mathcal{O}(m, m))$, and indeed $H^i(Y, \mathcal{O}(m, m)) = H^i(\mathbb{P}^2, \mathcal{O}(m)) \oplus H^i(\mathbb{P}^2, \mathcal{O}(m - 1))$.

**Example P7.8.13 (the Kummer cover of a line).** Let $\varphi \colon \mathbb{P}^1 \to \mathbb{P}^1$ be $[x_0 : x_1] \mapsto [x_0^q : x_1^q]$. Over $x_0 \neq 0$ it is $u \mapsto u^q$, the cyclic cover of $\mathbb{A}^1$ branched at $0$, and over $x_1 \neq 0$ it is the cyclic cover branched at $\infty$. It is finite flat of degree $q$, $\varphi^* \mathcal{O}(1) = \mathcal{O}(q)$, and $\varphi^*[0] = q[0]$, $\varphi^*[\infty] = q[\infty]$. Part 4 of Proposition P7.8.10, applied over each chart, gives $\omega_{\mathbb{P}^1} = \varphi^* \omega_{\mathbb{P}^1}((q-1)([0] + [\infty]))$, and the degrees check: $-2 = -2q + 2(q - 1)$. This is the one-dimensional case of the map used in Proposition P7.8.11.

### Proof

*Lemma P7.8.8.* For each $J$ with $D_J \neq \emptyset$, the restriction of $V$ to the smooth projective scheme $D_J$ has no base points, so by Bertini's theorem in characteristic $0$ (Har77, Corollary III.10.9 and Remark III.10.9.2) the members $s \in V$ with $\operatorname{div}(s|_{D_J})$ smooth of pure codimension $1$ in $D_J$, or empty, form a dense open subset $U_J \subseteq V$. There are finitely many $J$, and $U = \bigcap_J U_J$ is dense open. Let $s \in U$, $H = \operatorname{div}(s)$, and $x \in H$, and let $D_1, \dots, D_m$ be the components of $D$ through $x$, with local equations $x_1, \dots, x_m$ forming part of a coordinate system, and $h$ a local equation of $H$. For $J = \{1, \dots, m\}$, the stratum $D_J$ is smooth of codimension $m$ at $x$ and $H \cap D_J$ is smooth of codimension $m + 1$ at $x$, so $dx_1, \dots, dx_m, dh$ are linearly independent in the cotangent space at $x$. They extend to a coordinate system, so $D + H$ is snc at $x$. The case $J = \emptyset$ gives that $H$ is smooth.

*Lemma P7.8.9.* Part 1. $f_* \mathcal{O}_Y$ is coherent and flat, hence locally free, of rank $d$ by definition of the degree, and $\operatorname{Tr}(1)$ is the trace of the identity of a free module of rank $d$.

Part 2. Both $X$ and $Y$ are smooth projective of pure dimension $n$, so $\omega^\bullet_X = \omega_X[n]$ and $\omega^\bullet_Y = \omega_Y[n]$ by Corollary P4.7.21. Corollary P4.9.14 gives $f_* \omega_Y[n] \cong R\mathcal{H}om_{\mathcal{O}_X}(f_* \mathcal{O}_Y, \omega_X[n])$, and the right side is $\mathcal{H}om(f_* \mathcal{O}_Y, \omega_X)[n]$ since $f_* \mathcal{O}_Y$ is locally free. The isomorphism is $f_* \mathcal{O}_Y$-linear, the module structure on the right being $(b \varphi)(c) = \varphi(bc)$ (Har77, Exercises III.6.10 and III.7.2). Then $\tau(\iota(\alpha)) = \alpha(\operatorname{Tr}(1)) = d \alpha$.

Part 3. The composite $\omega_X \otimes M \xrightarrow{\iota} \mathcal{G} \subseteq f_*(\omega_Y \otimes f^* M) = f_* \omega_Y \otimes M \xrightarrow{\tau} \omega_X \otimes M$, where the equality is the projection formula P4.4.10, is multiplication by $d$, which is invertible since $k$ has characteristic $0$. So $\omega_X \otimes M$ is a direct summand of $\mathcal{G}$ and $H^i(X, \omega_X \otimes M) \to H^i(X, \mathcal{G})$ is injective.

*Proposition P7.8.10.* The algebra $\mathcal{A}$ is associative and commutative, since the multiplication is the one induced from $\bigoplus_{i \geq 0} L^{-i}$ modulo the relation $L^{-q} \ni \lambda = s(\lambda) \in \mathcal{O}_X$. Locally, on an open $U = \operatorname{Spec} R$ where $L$ is trivial with generator $e$, put $z = e^{-1} \in L^{-1}$ and write $s = t e^q$ with $t \in R$, an equation of $D$. Then $\mathcal{A}(U) = B = R[z]/(z^q - t)$.

Part 1. $B$ is a free $R$-module with basis $1, z, \dots, z^{q-1}$, so $h$ is finite and flat of degree $q$. Where $t$ is a unit, $B$ is étale over $R$, because the derivative $q z^{q-1}$ of $z^q - t$ is a unit, $q$ being invertible.

Part 2. $Y$ is projective, since $h$ is finite and $X$ is projective. Over $X \setminus D$ it is étale over a smooth scheme, hence smooth. Near a point $x \in D$, $D$ is smooth, so $t$ is part of a coordinate system $t, x_2, \dots, x_n$ at $x$. Then $B$ is a finite $R$-algebra with $B / (z, x_2, \dots, x_n) = R/(t, x_2, \dots, x_n) = k$, so $Y$ has one point $y$ over $x$, and its maximal ideal is generated by the $n$ elements $z, x_2, \dots, x_n$. Since $\dim \mathcal{O}_{Y, y} = n$, the local ring is regular.

Part 3. The section $z$ of $h^* L$ corresponds to the inclusion $L^{-1} \subseteq \mathcal{A}$, and $z^q = t e^q = h^* s$ by construction. Near $D$, $z$ is a coordinate at every point of $D' = \{z = 0\}$, so $D'$ is smooth, and $B/(z) = R/(t)$ shows that $D' \to D$ is an isomorphism. So $h^* D = \operatorname{div}(h^* s) = \operatorname{div}(z^q) = q D'$ and $h^* L = \mathcal{O}_Y(D')$.

Part 4. Write $\psi \in \operatorname{Hom}_R(B, R)$ for the map sending $\sum_{m=0}^{q-1} c_m z^m$ to $c_{q-1}$. For $0 \leq k \leq q - 1$, the map $z^k \psi$ sends $z^m$ to the coefficient of $z^{q-1}$ in $z^{k+m}$, which is $1$ if $k + m = q - 1$ and $0$ for the other $m$ in $0, \dots, q - 1$, because $z^{k+m} = t z^{k+m-q}$ when $k + m \geq q$ and then $k + m - q < q - 1$. So $\psi, z \psi, \dots, z^{q-1} \psi$ is the dual basis of $z^{q-1}, \dots, 1$, and $\operatorname{Hom}_R(B, R) = B \psi$ is free of rank $1$ over $B$. Multiplication by $z^m$ with $1 \leq m \leq q - 1$ sends each basis vector to a multiple of another one, so it has trace $0$, and $\operatorname{Tr}(1) = q$. Hence $\operatorname{Tr}(z^m) = q$ for $m = 0$ and $0$ for $1 \leq m \leq q - 1$, and comparing values on the basis gives
$$\operatorname{Tr} = q \, z^{q-1} \psi.$$
Let $\omega_0$ be a generator of $\omega_X$ on $U$. By part 2 of Lemma P7.8.9, $h_* \omega_Y|_U = B \cdot \psi \omega_0$, free of rank $1$ over $B$, and $\iota(\omega_0) = \operatorname{Tr} \cdot \omega_0 = q z^{q-1} \psi \omega_0$. Since $q$ is a unit and $z$ is an equation of $D'$, $B \cdot \iota(\omega_0) = z^{q-1} B \psi \omega_0 = h_*(\omega_Y(-(q-1)D'))|_U$. On the open set where $t$ is a unit, the same computation gives $B \cdot \iota(\omega_0) = B \psi \omega_0$, and $D'$ is empty there. Finally $\omega_Y(-(q-1)D')$ is generated by the pullback of the generator $\omega_0$ of $\omega_X$, so it is isomorphic to $h^* \omega_X$.

Part 5. Over $X \setminus D$, $h$ is étale, so $h^* (\Delta_1 + \dots + \Delta_m)$ is a reduced snc divisor there and each $h^* \Delta_c$ is smooth there. Near $x \in D$, choose coordinates $t, x_2, \dots, x_n$ such that each $\Delta_c$ through $x$ is $\{x_i = 0\}$ for some $i \geq 2$, distinct $c$ giving distinct $i$, which is possible since $D + \sum_c \Delta_c$ is snc and each $\Delta_c$ is smooth. In the coordinates $z, x_2, \dots, x_n$ at the point over $x$ found in part 2, $h^* \Delta_c$ is the same coordinate hyperplane and $D' = \{z = 0\}$, so $D' + \sum_c h^* \Delta_c$ is reduced snc and each $h^* \Delta_c$ is smooth.

*Proposition P7.8.11.* First let $L$ be generated by its global sections, put $V = H^0(X, L)$ and $N + 1 = \dim V$. Choose a general basis $s_0, \dots, s_N$ of $V$ and let $H_i = \operatorname{div}(s_i)$. By Lemma P7.8.8, applied $N + 1$ times to the base point free system $V$, $D + H_0 + \dots + H_N$ is a reduced snc divisor; in particular at most $n$ of the $H_i$ pass through any point of $X$, and they have no common point since $V$ has no base points. Let $j \colon X \to \mathbb{P}^N$ be the morphism defined by the basis, so that $j^* \mathcal{O}(1) = L$ and $s_i = j^* y_i$, and let $\varphi \colon \mathbb{P}^N \to \mathbb{P}^N$ be $[y_0 : \dots : y_N] \mapsto [y_0^q : \dots : y_N^q]$. It is finite and surjective, and flat since source and target are smooth of the same dimension (Mat86, Theorem 23.1), with $\varphi^* \mathcal{O}(1) = \mathcal{O}(q)$. Put $X' = X \times_{\mathbb{P}^N} \mathbb{P}^N$, the fibre product of $j$ and $\varphi$, with $g \colon X' \to X$ the projection and $L'$ the pullback of $\mathcal{O}(1)$ from the second factor. Then $g$ is finite, flat and surjective, being a base change of $\varphi$, and $g^* L = L'^q$.

It remains to show that $X'$ is smooth and that $g^* D$ is reduced snc with smooth pullbacks of components. On the open set $U_a = \{s_a \neq 0\}$ of $X$, put $t_i = s_i / s_a$ for $i \neq a$. Over $U_a$, $X'$ is $\operatorname{Spec}_{U_a} \mathcal{O}_{U_a}[z_i : i \neq a] / (z_i^q - t_i)$, the fibre product over $U_a$ of the cyclic covers $z_i^q = t_i$ of $U_a$ branched along $H_i \cap U_a$. Let $x \in U_a$, let $H_{i_1}, \dots, H_{i_m}$ be the $H_i$ through $x$ and $D_1, \dots, D_l$ the components of $D$ through $x$, renumbered, with equations $t_{i_1}, \dots, t_{i_m}$ and $x_1, \dots, x_l$ that together form part of a coordinate system at $x$. For $i$ not among the $i_c$, $t_i$ is a unit near $x$ and $z_i^q = t_i$ is étale, so it does not affect smoothness or the snc condition. Applying the local computation in parts 2 and 5 of Proposition P7.8.10 $m$ times, one coordinate $t_{i_c}$ at a time, every point of $X'$ over $x$ has coordinates $z_{i_1}, \dots, z_{i_m}, x_1, \dots, x_l$, completed by the remaining coordinates of $X$, in which $g^* D_c = \{x_c = 0\}$ for $c = 1, \dots, l$. So $X'$ is smooth of pure dimension $n$, each $g^* D_j$ is smooth, and $g^* D$ is reduced snc.

For general $L$, choose a very ample $C$ such that $B = L \otimes C$ is very ample (Theorem P4.2.7 and Har77, Exercise II.7.5). Apply the first case to $B$ and $D$, giving $g_1 \colon X_1 \to X$ and $B_1$ with $g_1^* B = B_1^q$. The pullback $g_1^* C$ is generated by global sections, and the first case applies on the smooth projective scheme $X_1$ to $g_1^* C$ and the reduced snc divisor $g_1^* D$; Lemma P7.8.8 holds on $X_1$ since a general member of a base point free system is general on each of the finitely many components. This gives $g_2 \colon X' \to X_1$ and $C'$ with $g_2^* g_1^* C = C'^q$. Then $g = g_1 \circ g_2$ and $L' = g_2^* B_1 \otimes C'^{-1}$ satisfy $g^* L = g^* B \otimes g^* C^{-1} = L'^q$, and $g^* D = g_2^* g_1^* D$ is reduced snc with smooth pullbacks of components.

### Exercises

1. (A) In Example P7.8.12, compute $h_* \mathcal{O}_Y(a, b)$ for $a \neq b$ and check that it is not of the form $h_* h^* M$.
2. (A) Let $h \colon Y \to X$ be the cyclic cover of Proposition P7.8.10. Show that $h_* \mathcal{O}_Y(-k D') = \bigoplus_{i=0}^{q-1} L^{-i} \otimes \mathcal{O}_X(-\lceil (k - i)/q \rceil D)$ for $0 \leq k \leq q$, where negative round-ups are replaced by $0$.
3. (B) Show that the trace splitting of Lemma P7.8.9 fails in characteristic $p$ for the Frobenius $F \colon \mathbb{P}^1 \to \mathbb{P}^1$: the trace $F_* \mathcal{O} \to \mathcal{O}$ is zero on $\mathcal{O}$.
4. (B) Show that the cyclic cover of Proposition P7.8.10 with $D = 0$ and $L^q \cong \mathcal{O}_X$ a nontrivial torsion line bundle of order exactly $q$ is a connected étale cover of degree $q$.
5. (B) Let $X$ be a curve of genus $g$ and $h \colon Y \to X$ a cyclic cover of degree $q$ branched along $D$, a reduced divisor of degree $qe$ with $L$ of degree $e$. Compute the genus of $Y$ by part 4 of Proposition P7.8.10 and compare with Riemann-Hurwitz.
6. (C) Let $D = \sum_{j=1}^r D_j$ be a reduced snc divisor and $q \geq 2$. Using Propositions P7.8.10 and P7.8.11 one component at a time, construct a finite flat surjective $f \colon Y \to X$ from a smooth projective scheme such that $f^* D_j = q D_j'$ for every $j$, with $\sum_j D_j'$ reduced snc. This is Kawamata's covering lemma. Say where the smoothness of $g^* D_j$ in Proposition P7.8.11 is used.

### Lean

Mathlib has finite flat morphisms through `Module.Finite` and `Module.Flat` on rings and the trace form `Algebra.trace`, but no cyclic covers, no canonical sheaves on schemes and no duality for finite morphisms. The project library has no statement about covers. The handbook adds no `MinimalModel` node here.

### Notes and history

Cyclic covers go back to the classical construction of hyperelliptic curves and double planes. Their use to prove vanishing theorems for fractional divisors is due to Kawamata (Kaw82) and Viehweg (Vie82), and the systematic treatment is Esnault and Viehweg, Lecture 3 (EV92). Bloch and Gieseker (BG71) used the Kummer cover of Proposition P7.8.11 to make a line bundle divisible in their work on positivity of Chern classes of ample vector bundles. Lazarsfeld, Section 4.1 (Laz04), and Kollár and Mori, Section 2.5 (KM98), give the same constructions; Kawamata's covering lemma, which produces a single cover on which every component of an snc divisor becomes divisible by $q$, is in Laz04, Section 4.1, and is the iteration of Exercise 6. The literature state is theorem.
