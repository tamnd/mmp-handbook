---
title: The negativity lemma
nodes: []
sources: [Har77, Bea96, KM98, Mum61]
reads_with: [KM98:ch3, Bea96:ch2]
requires: [P1.5, P3.7, P3.11, P4.6, P5.5, P5.6]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The negativity lemma

### Statement

In this chapter $k$ is algebraically closed, $S$ is a smooth projective surface over $k$, and the notation of Chapters 5 and 6 is in force. An *$\mathbb{R}$-divisor* on $S$ is a finite formal sum $B = \sum_i b_i C_i$ of integral curves $C_i$ with real coefficients, and a *$\mathbb{Q}$-divisor* is one with rational coefficients. Its *support* $\operatorname{Supp} B$ is the union of the $C_i$ with $b_i \neq 0$. The divisor $B$ is *effective*, written $B \geq 0$, if every $b_i \geq 0$, and $B \geq B'$ means $B - B' \geq 0$. The intersection pairing of Theorem P5.5.6 extends $\mathbb{R}$-bilinearly to $\mathbb{R}$-divisors. A *configuration* is a finite set $\{C_1, \dots, C_r\}$ of distinct integral curves, and its *intersection matrix* is $M = (C_i \cdot C_j)$. By Proposition P5.5.5 the entries off the diagonal are nonnegative, and $C_i \cdot C_j > 0$ for $i \neq j$ if and only if $C_i \cap C_j \neq \emptyset$. The configuration is *negative definite* if $M$ is.

For a real symmetric $r \times r$ matrix $M = (m_{ij})$, the *graph* $\Gamma(M)$ has vertices $1, \dots, r$ and an edge between $i \neq j$ when $m_{ij} > 0$. For an intersection matrix this is the *dual graph* of the configuration, and it is connected if and only if the union $C_1 \cup \dots \cup C_r$ is connected: a splitting of the vertices into two sets with no edges between them writes the union as a disjoint union of two closed sets, and conversely each $C_i$ is irreducible, so curves joined by a path of meeting curves lie in one connected component. For $x, y \in \mathbb{R}^r$, $x \geq y$ means $x_i \geq y_i$ for all $i$.

**Lemma P5.8.1 (matrices with nonnegative entries off the diagonal).** Let $M$ be a real symmetric $r \times r$ matrix with $m_{ij} \geq 0$ for all $i \neq j$.

1. If $M$ is negative definite and $x \in \mathbb{R}^r$ satisfies $M x \leq 0$, then $x \geq 0$. If in addition $\Gamma(M)$ is connected and $x \neq 0$, then $x_i > 0$ for every $i$.
2. If $M$ is not negative definite, there is $y \in \mathbb{R}^r$ with $y \geq 0$, $y \neq 0$ and $M y \geq 0$.
3. If $\Gamma(M)$ is connected and there is $z \in \mathbb{R}^r$ with every $z_i > 0$, $M z \leq 0$ and $M z \neq 0$, then $M$ is negative definite.
4. If $\Gamma(M)$ is connected and there is $z \in \mathbb{R}^r$ with every $z_i > 0$ and $M z = 0$, then $M$ is negative semidefinite, and $x^T M x = 0$ only for $x \in \mathbb{R} z$.

Lean: not in Lean as stated.

**Theorem P5.8.2 (negativity lemma for a configuration).** Let $C_1, \dots, C_r$ be a negative definite configuration and $B = \sum_i b_i C_i$ an $\mathbb{R}$-divisor supported on it. If $B \cdot C_j \leq 0$ for every $j$, then $B \geq 0$. If in addition $C_1 \cup \dots \cup C_r$ is connected and $B \neq 0$, then $b_i > 0$ for every $i$. If $B \cdot C_j = 0$ for every $j$, then $B = 0$.

Lean: not in Lean as stated.

Let $f \colon S \to T$ be a birational morphism onto a normal projective surface $T$. An integral curve $C$ on $S$ is *$f$-exceptional* if $f(C)$ is a point. For an integral curve $C$ that is not exceptional, $f(C)$ is an integral curve on $T$, because $f$ is proper. Put $f_* C = f(C)$ for such $C$ and $f_* C = 0$ for exceptional $C$, and extend linearly to $\mathbb{R}$-divisors. The values are $\mathbb{R}$-Weil divisors on $T$, finite formal sums of integral curves on $T$ with real coefficients. An $\mathbb{R}$-divisor $B$ on $S$ is *$f$-exceptional* if every component of $\operatorname{Supp} B$ is.

**Theorem P5.8.3 (exceptional curves of a birational morphism).** Let $f \colon S \to T$ be a birational morphism onto a normal projective surface.

1. The set $T_0$ of points $t \in T$ for which $f^{-1}(t)$ is not a single point is finite, and $f$ is an isomorphism over $T \setminus T_0$.
2. For $t \in T_0$ the fibre $f^{-1}(t)$ is connected and is the union of finitely many integral curves $C_1, \dots, C_r$. The exceptional curves of $f$ are the curves arising in this way for the points of $T_0$, so there are finitely many.
3. (*Mumford.*) For $t \in T_0$ the intersection matrix of $C_1, \dots, C_r$ is negative definite. Exceptional curves over distinct points are disjoint, so the configuration of all exceptional curves of $f$ is negative definite.

Lean: not in Lean as stated.

**Corollary P5.8.4 (negativity lemma for a birational morphism).** Let $f \colon S \to T$ be as in Theorem P5.8.3 and $B$ an $\mathbb{R}$-divisor on $S$. If $f_* B \geq 0$ and $B \cdot C \leq 0$ for every exceptional curve $C$, then $B \geq 0$. In particular an exceptional $\mathbb{R}$-divisor $B$ with $B \cdot C = 0$ for every exceptional curve $C$ is zero.

Lean: not in Lean as stated.

For an integral curve $\Gamma$ on $T$, its *strict transform* $f^{-1}_* \Gamma$ is the closure of $f^{-1}(\Gamma \setminus T_0)$, an integral curve on $S$ with $f_* f^{-1}_* \Gamma = \Gamma$, and $f^{-1}_*$ extends linearly to $\mathbb{R}$-Weil divisors.

**Corollary P5.8.5 (Mumford's pullback).** Let $f \colon S \to T$ be as in Theorem P5.8.3. For every $\mathbb{R}$-Weil divisor $D$ on $T$ there is a unique $\mathbb{R}$-divisor $f^* D$ on $S$ with
$$f_* f^* D = D \qquad \text{and} \qquad f^* D \cdot C = 0 \text{ for every exceptional curve } C.$$
It is $f^{-1}_* D$ plus an exceptional $\mathbb{R}$-divisor, it depends linearly on $D$, it is a $\mathbb{Q}$-divisor if $D$ has integer coefficients, and it is effective if $D$ is. If $D$ is a Cartier divisor, $f^* D$ is the usual pullback. The number $D \cdot D' = f^* D \cdot f^* D'$ is *Mumford's intersection number* of two $\mathbb{R}$-Weil divisors on $T$.

Lean: not in Lean as stated.

### Proof in words

The linear algebra is the whole content of the negativity lemma. A negative definite matrix with nonnegative entries off the diagonal behaves like the negative of a Cartan matrix: splitting a vector into its positive and negative parts, the cross term has a sign, and the negative part is forced to vanish. When $M$ is not negative definite, the largest eigenvalue is nonnegative, and an eigenvector for it can be taken with nonnegative coordinates, because replacing the coordinates by their absolute values can only increase the quadratic form. The last two parts rest on one identity, which writes $x^T M x$ in terms of a positive vector $z$ as a sum of terms of one sign.

Mumford's theorem applies this to a birational morphism $f$. A function $g$ that vanishes at a point $t$ pulls back to a function whose divisor is $Z + R$, with $Z$ a positive combination of the curves over $t$ and $R$ the rest. A principal divisor is numerically trivial, so $Z \cdot C_j = -R \cdot C_j \leq 0$, and the strict transform of the zero locus of $g$ makes one of these inequalities strict. Part 3 of the lemma then gives negative definiteness. The negativity lemma for $f$ and Mumford's pullback follow by splitting a divisor into its exceptional part and the rest.

### Examples

**Example P5.8.6 (a chain of $(-2)$-curves).** Let $n \geq 1$, $p_1 \in \mathbb{P}^2$, and let $S_1 \to \mathbb{P}^2$ be the blow-up of $p_1$, with exceptional curve $E_1$. For $1 \leq i \leq n$, let $p_{i+1}$ be a point of $E_i$ not on the strict transforms of $E_1, \dots, E_{i-1}$, which meet $E_i$ in finitely many points, and let $S_{i+1} \to S_i$ be its blow-up, with exceptional curve $E_{i+1}$. Let $f \colon S_{n+1} \to \mathbb{P}^2$ be the composite and $e_i$ the total transform of $E_i$ on $S_{n+1}$. By Theorem P5.6.3, applied $n+1$ times,
$$\operatorname{Pic}(S_{n+1}) = \mathbb{Z} \ell \oplus \mathbb{Z} e_1 \oplus \dots \oplus \mathbb{Z} e_{n+1}, \qquad \ell^2 = 1, \quad e_i^2 = -1,$$
an orthogonal sum, with $K_{S_{n+1}} = -3\ell + e_1 + \dots + e_{n+1}$. The smooth curve $E_i$ passes through $p_{i+1}$ with multiplicity $1$ and through no later centre, so by Proposition P5.6.4 its strict transform on $S_{n+1}$ is $C_i = e_i - e_{i+1}$ for $i \leq n$, and $C_{n+1} = e_{n+1}$. So $C_i^2 = -2$ and $K_{S_{n+1}} \cdot C_i = -1 + 1 = 0$ for $i \leq n$, $C_i \cdot C_{i+1} = -e_{i+1}^2 = 1$, and $C_i \cdot C_j = 0$ for $|i - j| \geq 2$. The curves $C_1, \dots, C_n$ form a chain of $(-2)$-curves, the configuration $A_n$, with intersection matrix
$$M_{A_n} = \begin{pmatrix} -2 & 1 & & \\ 1 & -2 & \ddots & \\ & \ddots & \ddots & 1 \\ & & 1 & -2 \end{pmatrix}.$$
For $z = (1, \dots, 1)$, $M_{A_n} z = (-1, 0, \dots, 0, -1)$ if $n \geq 2$ and $M_{A_1} z = (-2)$, so $M_{A_n}$ is negative definite by part 3 of Lemma P5.8.1. The full exceptional locus $f^{-1}(p_1) = C_1 \cup \dots \cup C_{n+1}$ is negative definite in the same way: $e_1 = C_1 + \dots + C_{n+1}$ has $e_1 \cdot C_1 = -1$ and $e_1 \cdot C_j = 0$ for $j \geq 2$. This is the vector $Z$ of the proof of Theorem P5.8.3 for a function $g$ vanishing on a general line through $p_1$.

**Example P5.8.7 (the relative canonical divisor).** In Example P5.8.6, $B = K_{S_{n+1}} - f^* K_{\mathbb{P}^2} = e_1 + \dots + e_{n+1}$. Since $e_i = C_i + C_{i+1} + \dots + C_{n+1}$,
$$B = C_1 + 2 C_2 + \dots + (n + 1) C_{n+1},$$
and $B \cdot C_j = (j - 1) - 2j + (j + 1) = 0$ for $j \leq n$, with $B \cdot C_1 = -2 + 2 = 0$, while $B \cdot C_{n+1} = n - (n+1) = -1$. So $B$ is exceptional with $B \cdot C \leq 0$ for every exceptional $C$, and Corollary P5.8.4 predicts $B \geq 0$, as the formula shows. The coefficients of $B$ are positive although only one of the numbers $B \cdot C_j$ is negative, as the second statement of Theorem P5.8.2 says for the connected configuration $C_1 \cup \dots \cup C_{n+1}$.

**Example P5.8.8 (a configuration that is not negative definite).** On $\tilde S = \operatorname{Bl}_p \mathbb{P}^2$ let $E$ be the exceptional curve and $F$ the strict transform of a line through $p$, of class $\ell - E$ (Example P5.6.7). The intersection matrix of $\{E, F\}$ is
$$\begin{pmatrix} -1 & 1 \\ 1 & 0 \end{pmatrix},$$
with determinant $-1$, so it is indefinite. Part 2 of Lemma P5.8.1 gives $y = (1, 1)$ with $M y = (0, 1) \geq 0$, the divisor $E + F \sim \ell$. It is nef in the sense that $\ell \cdot C \geq 0$ for every curve $C$, since $\ell \cdot E = 0$ and every other integral curve is a strict transform of class $a \ell - bE$ with $a \geq 1$. By Theorem P5.8.3, no birational morphism onto a normal projective surface contracts the connected curve $E \cup F$ to a point.

**Example P5.8.9 (the quadric cone).** Let $T = V_+(xy - z^2) \subseteq \mathbb{P}^3$, with coordinates $x, y, z, w$, and $v = [0 : 0 : 0 : 1]$ its vertex. The partial derivatives $y, x, -2z, 0$ vanish on $T$ only where $x = y = 0$, hence $z = 0$, so $T \setminus \{v\}$ is smooth. The chart $w \neq 0$ is the affine cone $\operatorname{Spec} A$, $A = k[x, y, z]/(xy - z^2)$, of Example P3.11.15. By Example P3.11.29 and part 6 of Theorem P3.11.25, $A$ is the ring of global functions on the smooth surface $F_2 \setminus C_+$: the map $x \mapsto r$, $z \mapsto rt$, $y \mapsto rt^2$ is onto $\bigoplus_i r^i k[t]_{\leq 2i}$, because $r^i t^j$ with $j \leq 2i$ is a product of $r$, $rt$, $rt^2$, and it is injective because both rings are domains of dimension $2$. A rational function integral over this ring is integral over every local ring of the normal surface, hence regular everywhere, so $A$ is normal and $T$ is a normal projective surface.

Let $f \colon S = \operatorname{Bl}_v T \to T$. By Example P3.11.15, $f^{-1}(\operatorname{Spec} A)$ is glued from two planes $\operatorname{Spec} k[x, z']$ and $\operatorname{Spec} k[y, z'']$ along $z'' = 1/z'$, $y = x z'^2$, with exceptional curve $E = V(x) \cup V(y) \cong \mathbb{P}^1$. So $S$ is smooth, and it is projective: by part 2 of Corollary P3.11.10 it is a closed subscheme of $\operatorname{Bl}_v \mathbb{P}^3$, which is projective by the proof of part 1 of Theorem P5.6.2. The function $x$ generates $\mathcal{I}_E$ on the first chart, and on the second chart $x = y z''^2$. So the image of $x$ is a section of the conormal bundle $\mathcal{I}_E / \mathcal{I}_E^2$ with a double zero at $z'' = 0$ and no other zero, the conormal bundle has degree $2$, and $E^2 = \deg \mathcal{O}_S(E)|_E = -2$ by Theorem P5.5.6.

For $a \in k$ the line $L_a = V_+(z - ax, y - a^2 x)$ lies on $T$. On the first chart $z - ax = x(z' - a)$, so $\tilde L_a = f^{-1}_* L_a$ is $V(z' - a)$ there, and it meets $E$ transversally in one point: $\tilde L_a \cdot E = 1$. The plane $H_a = V_+(a^2 x - 2a z + y)$ meets $T$ where $x (2az - a^2 x) = z^2$, that is, $(z - ax)^2 = 0$, so $H_a \cap T = L_a$ as sets, and on the first chart $a^2 x - 2a x z' + x z'^2 = x (z' - a)^2$. Hence $f^* H_a = 2 \tilde L_a + E$ as Cartier divisors. Theorem P5.5.6 gives $f^* H_a \cdot \tilde L_a = \deg \mathcal{O}_{L_a}(1) = 1$, since $\tilde L_a \to L_a$ is birational and both curves have the same normalization, so $2 \tilde L_a^2 + 1 = 1$ and $\tilde L_a^2 = 0$. As a check, $f^* H_a \cdot E = 2 - 2 = 0$. The Weil divisor $L_a$ is not Cartier at $v$. Its Mumford pullback is $f^* L_a = \tilde L_a + \frac{1}{2} E$, since $(\tilde L_a + c E) \cdot E = 1 - 2c$ vanishes for $c = \frac12$, and
$$L_a^2 = \left(\tilde L_a + \tfrac{1}{2} E\right)^2 = 0 + 1 - \tfrac{1}{2} = \tfrac{1}{2}.$$
Two lines of the cone meet only at the vertex, and $L_a \cdot L_b = (\tilde L_a + \tfrac12 E) \cdot (\tilde L_b + \tfrac12 E) = 0 + \tfrac12 + \tfrac12 - \tfrac12 = \tfrac12$ for $a \neq b$, since $\tilde L_a$ and $\tilde L_b$ are disjoint. Twice a line is the Cartier divisor $H_a \cap T$, and $(2 L_a)^2 = 2 = \deg T$.

### Proof

*Lemma P5.8.1.* (1) Write $x = x^+ - x^-$ with $x^+, x^- \geq 0$ and $x^+_i x^-_i = 0$ for all $i$. Then
$$(x^-)^T M x^- = (x^-)^T M x^+ - (x^-)^T M x.$$
The first term is $\sum_{i \neq j} m_{ij} x^-_i x^+_j \geq 0$, since the terms with $i = j$ vanish and $m_{ij} \geq 0$ otherwise. The second term is $-\sum_i x^-_i (Mx)_i \geq 0$. So $(x^-)^T M x^- \geq 0$, and $x^- = 0$ because $M$ is negative definite. Now let $\Gamma(M)$ be connected, $x \geq 0$, $x \neq 0$, and suppose $x_i = 0$ for some $i$. Then $0 \geq (Mx)_i = \sum_{j \neq i} m_{ij} x_j$, a sum of nonnegative terms, so $x_j = 0$ for every neighbour $j$ of $i$ in $\Gamma(M)$. By connectedness $x = 0$, a contradiction.

(2) By the spectral theorem $M$ has an orthonormal basis of eigenvectors. Let $\lambda$ be its largest eigenvalue. Writing a unit vector $x$ in this basis shows $x^T M x \leq \lambda$, with equality exactly when $x$ lies in the $\lambda$-eigenspace. Since $M$ is not negative definite, $\lambda \geq 0$. Let $x$ be a unit eigenvector for $\lambda$ and $y = (|x_1|, \dots, |x_r|)$, again a unit vector. Then
$$y^T M y = \sum_i m_{ii} x_i^2 + \sum_{i \neq j} m_{ij} |x_i| |x_j| \geq x^T M x = \lambda,$$
so $y^T M y = \lambda$, $y$ is an eigenvector, and $M y = \lambda y \geq 0$.

(3) and (4). For $x \in \mathbb{R}^r$ put $u_i = x_i / z_i$. Then
$$x^T M x = \sum_i z_i (Mz)_i \, u_i^2 - \sum_{i < j} m_{ij} z_i z_j (u_i - u_j)^2. \tag{$\dagger$}$$
Indeed, the first sum is $\sum_{i, j} m_{ij} z_i z_j u_i^2 = \sum_i m_{ii} x_i^2 + \sum_{i \neq j} m_{ij} z_i z_j u_i^2$, and by symmetry $\sum_{i < j} m_{ij} z_i z_j (u_i^2 + u_j^2) = \sum_{i \neq j} m_{ij} z_i z_j u_i^2$, so the right side is $\sum_i m_{ii} x_i^2 + 2 \sum_{i < j} m_{ij} x_i x_j$. Under either hypothesis every term of $(\dagger)$ is $\leq 0$, so $x^T M x \leq 0$. If $x^T M x = 0$, then $u_i = u_j$ whenever $m_{ij} > 0$, and since $\Gamma(M)$ is connected, $u_i = c$ for all $i$, that is, $x = c z$. Under the hypothesis of (3) the first sum is then $c^2 \sum_i z_i (Mz)_i$ with some $(Mz)_i < 0$, so $c = 0$ and $x = 0$. This proves (3), and the same argument without the last step proves (4). $\square$

*Theorem P5.8.2.* Let $b = (b_1, \dots, b_r)$. Then $(M b)_j = B \cdot C_j$, so the hypothesis is $M b \leq 0$, and part 1 of Lemma P5.8.1 gives $b \geq 0$, and $b_i > 0$ for all $i$ when the union is connected and $b \neq 0$, since then $\Gamma(M)$ is connected. If $M b = 0$, then $b = 0$ because $M$ is invertible. $\square$

*Theorem P5.8.3.* The surface $S$ is projective over $k$, so $f$ is projective (Hartshorne, Exercise II.4.9), and its image is closed and dense, so $f$ is surjective. (1) By Corollary P4.6.10 the set $U$ of points with finite fibre is open, $f$ is an isomorphism over $U$, and every fibre over $T \setminus U$ is connected and of positive dimension at each of its points. A finite fibre of $f$ over a point of $U$ is a single point, since $f^{-1}(U) \to U$ is an isomorphism, so $T_0 = T \setminus U$. The set $U$ is nonempty, so $W = f^{-1}(T_0)$ is a proper closed subset of the irreducible surface $S$, of dimension at most $1$, with finitely many irreducible components. For $t \in T_0$ the fibre $f^{-1}(t)$ contains an irreducible closed subset of dimension $1$, which is an irreducible component of $W$. Fibres over distinct points are disjoint, so distinct points of $T_0$ give distinct components of $W$, and $T_0$ is finite.

(2) For $t \in T_0$ the fibre is connected and every irreducible component of it has dimension $1$, so it is a union of finitely many integral curves, each mapped to $t$. Conversely an exceptional curve $C$ maps to a point $t$ with infinite fibre, so $t \in T_0$ and $C$ is a component of $f^{-1}(t)$.

(3) Let $t \in T_0$ with $f^{-1}(t) = C_1 \cup \dots \cup C_r$. The local ring $\mathcal{O}_{T,t}$ is a Noetherian domain of dimension $2$. Choose $0 \neq g \in \mathfrak{m}_t$ and an affine open $V \ni t$ with $g \in \mathcal{O}(V)$. On $S$, the rational function $f^* g$ is regular on $f^{-1}(V)$, which contains $f^{-1}(t)$, and vanishes at every point of $f^{-1}(t)$. Write
$$\operatorname{div}(f^* g) = Z + R, \qquad Z = \sum_i a_i C_i,$$
where $R$ has no $C_i$ in its support. Then $a_i = \operatorname{ord}_{C_i}(f^* g) \geq 1$. A component $\Gamma$ of $R$ that meets $f^{-1}(t)$ meets the open set $f^{-1}(V)$, where $f^* g$ is regular, so its coefficient in $R$ is positive. Components of $R$ that do not meet $f^{-1}(t)$ have intersection number $0$ with every $C_j$, by Proposition P5.5.5. So $R \cdot C_j \geq 0$ for all $j$. By Krull's principal ideal theorem (Theorem P1.5.17), $V(g) \subseteq V$ has an irreducible component $\Gamma_0$ of dimension $1$ through $t$. Its strict transform $\Gamma = f^{-1}_* \Gamma_0$ is a component of $R$, since $f^* g$ vanishes on it and it is not exceptional, and $f(\Gamma)$ is closed and contains the dense subset $\Gamma_0 \setminus T_0$ of $\Gamma_0$, so $f(\Gamma) = \Gamma_0 \ni t$. So $\Gamma$ meets some $C_j$, and $R \cdot C_j \geq \Gamma \cdot C_j > 0$ by Proposition P5.5.5. A principal divisor has intersection number $0$ with every curve, by Theorem P5.5.6, so
$$Z \cdot C_j = -R \cdot C_j \leq 0 \text{ for all } j, \text{ with strict inequality for some } j.$$
The union $C_1 \cup \dots \cup C_r$ is connected by part 2, so the dual graph is connected, and part 3 of Lemma P5.8.1 with $z = (a_1, \dots, a_r)$ shows that the intersection matrix is negative definite. Curves over distinct points lie in disjoint fibres, so their intersection numbers vanish by Proposition P5.5.5, and the intersection matrix of all exceptional curves is block diagonal with negative definite blocks. $\square$

*Corollary P5.8.4.* Write $B = B_e + B'$, where $B_e$ is exceptional and $B' = \sum_\Gamma b_\Gamma \Gamma$ has no exceptional component. A non-exceptional integral curve $\Gamma$ is not contained in $f^{-1}(T_0)$, a union of exceptional curves by Theorem P5.8.3, so $\Gamma \setminus f^{-1}(T_0)$ is dense in $\Gamma$ and $\Gamma = f^{-1}_* f(\Gamma)$. So $\Gamma \mapsto f(\Gamma)$ is injective on non-exceptional curves, and the coefficients of $f_* B = f_* B'$ are the $b_\Gamma$. The hypothesis $f_* B \geq 0$ gives $B' \geq 0$. For every exceptional curve $C$, $B' \cdot C \geq 0$ because $B'$ is effective without $C$ in its support, so $B_e \cdot C = B \cdot C - B' \cdot C \leq 0$. The configuration of all exceptional curves is negative definite by Theorem P5.8.3, and Theorem P5.8.2 gives $B_e \geq 0$. For the last statement apply this to $B$ and to $-B$, both with $f_* (\pm B) = 0$. $\square$

*Corollary P5.8.5.* Let $C_1, \dots, C_r$ be all the exceptional curves, with intersection matrix $M$, invertible by Theorem P5.8.3. A divisor $f^{-1}_* D + \sum_i a_i C_i$ has the two properties if and only if $M a = -\big( f^{-1}_* D \cdot C_j \big)_j$, which has exactly one solution $a$, depending linearly on $D$ and rational when $D$ has integer coefficients, since $M$ has integer entries. If two $\mathbb{R}$-divisors $B_1, B_2$ have the two properties, then $f_*(B_1 - B_2) = 0$, so $B_1 - B_2$ is exceptional by the injectivity shown in the proof of Corollary P5.8.4, and $B_1 = B_2$ by Corollary P5.8.4. If $D \geq 0$, then $f_* f^* D = D \geq 0$ and $f^* D \cdot C = 0$ for exceptional $C$, so $f^* D \geq 0$ by Corollary P5.8.4. If $D$ is Cartier, its usual pullback $f^* D$ is defined by the pullbacks of local equations, which are nonzero rational functions since $f$ is dominant. For an exceptional curve $C$, the restriction of $f^* \mathcal{O}_T(D)$ to $C$ is the pullback of $\mathcal{O}_T(D)|_{\{f(C)\}}$ along $C \to f(C)$, a trivial bundle, so $f^* D \cdot C = 0$ by Theorem P5.5.6. Over $T \setminus T_0$, where $f$ is an isomorphism, $f_* f^* D$ and $D$ agree, and a Weil divisor on $T$ is determined by its restriction to the complement of the finite set $T_0$. So the usual pullback has the two properties. $\square$

### Exercises

1. (A) Show that $\det M_{A_n} = (-1)^n (n + 1)$, compute $M_{A_2}^{-1}$, and check that all its entries are negative, as part 1 of Lemma P5.8.1 predicts for the solutions of $M x = -e_j$.
2. (A) Let $C_1, C_2$ be smooth rational curves with $C_i^2 = -a_i$, $a_i \geq 1$, meeting transversally in one point. Show that $\{C_1, C_2\}$ is negative definite if and only if $a_1 a_2 > 1$. For $a_1 = a_2 = 1$, show that $F = C_1 + C_2$ satisfies $F \cdot C_1 = F \cdot C_2 = 0$, and relate this to part 4 of Lemma P5.8.1.
3. (B) Show by an example with $r = 2$ that part 1 of Lemma P5.8.1 fails for negative definite matrices with a negative entry off the diagonal.
4. (B) (*Zariski's lemma.*) Let $\varphi \colon S \to B$ be a surjective morphism onto a smooth projective curve and $F = \varphi^* b = \sum_i a_i C_i$ a fibre, with $C_i$ distinct integral curves. Show that $F \cdot C_i = 0$ for all $i$, that the intersection matrix of the $C_i$ is negative semidefinite, and that an $\mathbb{R}$-divisor $D$ supported on $F$ has $D^2 = 0$ only if $D$ is a real multiple of $F$. You may use that fibres of $\varphi$ are connected when $\varphi_* \mathcal{O}_S = \mathcal{O}_B$.
5. (B) In Example P5.8.6 with $n = 1$, let $L$ be the line through $p_1$ with tangent direction $p_2$. Using Proposition P5.6.4 twice, show that $f^* L = \tilde L + C_1 + 2 C_2$, and recover the coefficients $1$ and $2$ from the conditions of Corollary P5.8.5 and $\tilde L \cdot C_1 = 0$, $\tilde L \cdot C_2 = 1$.
6. (C) Let $f \colon S \to T$ be as in Theorem P5.8.3 and $g \colon S' \to S$ the blow-up of a point. Show that $(f \circ g)^* D = g^* (f^* D)$ for every $\mathbb{R}$-Weil divisor $D$ on $T$, and deduce that Mumford's intersection number does not change when $f$ is replaced by $f \circ g$. Using the factorization theorem of Chapter 7, show that it does not depend on the choice of $f$.

### Lean

Mathlib has positive definite matrices (`Matrix.PosDef`) and the spectral theorem for Hermitian matrices (`Matrix.IsHermitian.eigenvalues`), which give the linear algebra of Lemma P5.8.1 up to the sign conventions. It has no intersection pairing on a surface and no negativity lemma. The handbook adds no `MinimalModel` node here.

### Notes and history

Du Val described in 1934 the configurations of $(-2)$-curves that resolve the surface singularities which do not affect the conditions of adjunction (DuV34), and their intersection matrices are the negatives of the Cartan matrices of types $A$, $D$ and $E$. Mumford proved in 1961 (Mum61, Section 1) that the exceptional curves of every resolution of a normal surface singularity have a negative definite intersection matrix, by the argument of Theorem P5.8.3, and used Mumford's pullback to define rational intersection numbers on a normal surface. Grauert proved the converse in the analytic category in 1962, as Section 8.2 explains. The sign lemma for matrices is a symmetric form of the Perron-Frobenius theorem. The literature state is theorem. In the minimal model program the negativity lemma is used in every dimension in the form of Kollár and Mori, Lemma 3.39 (KM98): if $f \colon X \to Y$ is a proper birational morphism of normal varieties, $-B$ is $f$-nef and $f_* B$ is effective, then $B$ is effective. Its proof reduces to the surface case of Corollary P5.8.4 by cutting with general hyperplanes, and it drives the comparison of discrepancies under flips and divisorial contractions in Volume 4.
