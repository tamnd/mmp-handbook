---
title: Finite generation for a surface by hand
nodes: []
sources: [Zar62, Laz04, KM98, Har77]
reads_with: [Laz04:2.3, KM98:3.5]
requires: [P5.8, 2.4, 2.5, 7.1]
level: advanced
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Finite generation for a surface by hand

### Statement

In this section $S$ denotes a smooth projective surface and $X$ a normal projective surface, over an algebraically closed field. For a pseudo-effective $\mathbb{Q}$-divisor $D$ on $S$, Theorem P5.8.24 gives the Zariski decomposition $D = P + N$: $P$ is nef, $N = \sum_i n_i N_i$ is effective with negative definite intersection matrix $(N_i \cdot N_j)$, and $P \cdot N_i = 0$ for every $i$. Both $P$ and $N$ are $\mathbb{Q}$-divisors when $D$ is.

**Proposition 9.5.9 (the fixed part of $|mD|$).** Let $D$ be a pseudo-effective $\mathbb{Q}$-divisor on $S$ with Zariski decomposition $D = P + N$, and let $m \ge 1$ be such that $mD$ is integral. Every effective divisor $G \sim mD$ satisfies $G \ge \lceil mN \rceil$. Consequently multiplication by the canonical section of $\mathcal{O}_S(\lceil mN \rceil)$ is an isomorphism
$$H^0(S, \lfloor mP \rfloor) \to H^0(S, mD),$$
and if $m_0 D$ and $m_0 P$ are integral, then $R(S, D)^{(m_0)} \cong R(S, P)^{(m_0)}$ as graded rings.

Lean: not yet in Lean.

**Theorem 9.5.10 (finite generation for klt surface pairs).** Let $(X, \Delta)$ be a projective klt surface pair with $\Delta$ a $\mathbb{Q}$-divisor. Then $R(X, K_X + \Delta)$ is a finitely generated $k$-algebra, and if $K_X + \Delta$ is pseudo-effective its $\operatorname{Proj}$ is the target of the semiample fibration of $K_Y + \Gamma$ on the output $(Y, \Gamma)$ of the log minimal model program.

Lean: not yet in Lean.

### Proof in words

On a smooth surface the negative part of the Zariski decomposition is a fixed part of every multiple: the part of a member of $|mD|$ supported on the components of $N$ must be at least $mN$, because the difference would be a nonzero divisor on a negative definite configuration with nonnegative intersection with each of its own components. So the section ring of $D$ is that of the nef divisor $P$, up to Veronese subrings.

For a klt pair the minimal model program of Volume 2 makes this concrete: it contracts the curves of the negative part one at a time, each contraction increases the discrepancy of the contracted curve, and the output has nef log canonical divisor. Log abundance for surfaces makes that divisor semiample, so its section ring is finitely generated, and the comparison of sections on the contraction of Lemma 7.1.6 identifies the two rings up to a Veronese subring.

### Examples

**Example 9.5.11 (a quintic surface blown up at a point).** Let $S_0 \subseteq \mathbb{P}^3$ be a smooth quintic surface with equation $f$, and $\pi \colon S \to S_0$ the blow-up of a point with exceptional curve $E$. By adjunction $K_{S_0} = \mathcal{O}_{S_0}(1)$, and $K_S = \pi^* K_{S_0} + E$. The Zariski decomposition of $K_S$ is $P = \pi^* K_{S_0}$, $N = E$: indeed $\pi^* K_{S_0}$ is nef, $E^2 = -1$, and $\pi^* K_{S_0} \cdot E = 0$. By Proposition 9.5.9, or directly by Lemma 7.1.6, $H^0(S, mK_S) \cong H^0(S_0, \mathcal{O}_{S_0}(m))$ for every $m \ge 0$. The restriction $H^0(\mathbb{P}^3, \mathcal{O}(m)) \to H^0(S_0, \mathcal{O}_{S_0}(m))$ is surjective because $H^1(\mathbb{P}^3, \mathcal{O}(m - 5)) = 0$, with kernel $f \cdot H^0(\mathbb{P}^3, \mathcal{O}(m - 5))$. So
$$R(S, K_S) \cong k[x_0, x_1, x_2, x_3]/(f),$$
generated in degree $1$ with one relation in degree $5$, and $\operatorname{Proj} R(S, K_S) = S_0$, the canonical model.

**Example 9.5.12 (eight lines with coefficient one half).** Let $L_1, \ldots, L_8 \subseteq \mathbb{P}^2$ be lines in general position with equations $\ell_1, \ldots, \ell_8$, let $h = \ell_1 \cdots \ell_8$, of degree $8$, and $\Delta = \frac{1}{2} \sum_i L_i$. The pair $(\mathbb{P}^2, \Delta)$ is klt, since $\sum L_i$ has simple normal crossings and the coefficients are $\frac{1}{2}$, and $K + \Delta \equiv -3L + 4L = L$ is ample. Fix a line $L_0$ with equation $\ell_0$, not among the $L_i$, and take $K = -3L_0$. Then
$$\lfloor m(K + \Delta) \rfloor = \lfloor \tfrac{m}{2} \rfloor \sum_i L_i - 3m L_0, \qquad \deg = 8 \lfloor \tfrac{m}{2} \rfloor - 3m = \begin{cases} 2j & m = 2j, \\ 2j - 3 & m = 2j + 1. \end{cases}$$
A rational function $\phi$ satisfies $\operatorname{div} \phi + \lfloor m(K + \Delta) \rfloor \ge 0$ if and only if $\phi = G \ell_0^{3m} / h^{\lfloor m/2 \rfloor}$ with $G$ a form of degree $d(m) = 8 \lfloor m/2 \rfloor - 3m$, because then $\operatorname{div} \phi + \lfloor m(K + \Delta) \rfloor = \operatorname{div} G$. So $R_m \cong S_{d(m)}$, with $S = k[x_0, x_1, x_2]$. For the multiplication, $\phi_m \phi_{m'}$ corresponds to $G G' h^{\varepsilon}$ with $\varepsilon = \lfloor \frac{m + m'}{2} \rfloor - \lfloor \frac{m}{2} \rfloor - \lfloor \frac{m'}{2} \rfloor$, which is $1$ if $m$ and $m'$ are both odd and $0$ otherwise. Let $B = S[w]/(w^2 - h)$, graded by $\deg x_i = 1$ and $\deg w = 4$, so that $B_m = S_m \oplus S_{m - 4} w$. The map sending $G \in R_{2j}$ to $G \in S_{2j}$ and $G \in R_{2j + 1}$ to $G w \in S_{2j - 3} w$ is an isomorphism of graded rings from $R$ onto the subring
$$\bigoplus_{m \text{ even}} S_m \ \oplus \bigoplus_{m \text{ odd}} S_{m - 4} w \subseteq B,$$
since $(G w)(G' w) = G G' h$ matches the multiplication rule. Now $S_{2j} = (S_2)^j$ and, for $j \ge 2$, $S_{2j - 3} w = (S_2)^{j - 2} \cdot S_1 w$, while $R_1 = R_3 = 0$. So $R$ is generated by $R_2 \cong S_2$, of dimension $6$, and $R_5 \cong S_1 w$, of dimension $3$. Its second Veronese subring is $\bigoplus_j S_{2j}$, so $\operatorname{Proj} R = \mathbb{P}^2$, as it must be since $K + \Delta$ is ample. The generator in degree $5$ records the rounding: $R(\mathbb{P}^2, K + \Delta)$ is not a Veronese ring of a polynomial ring, although its $\operatorname{Proj}$ is $\mathbb{P}^2$.

**Example 9.5.13 (Zariski's example).** Let $C_0 \subseteq \mathbb{P}^2$ be a smooth cubic, $p_1, \ldots, p_{12} \in C_0$ general points, $\pi \colon S \to \mathbb{P}^2$ their blow-up with exceptional curves $E_i$, $C \sim \pi^* 3L - \sum E_i$ the strict transform of $C_0$, and $D = \pi^* 4L - \sum E_i$. Then $C^2 = 9 - 12 = -3$, $D \cdot C = 12 - 12 = 0$, $D^2 = 16 - 12 = 4$, and $D \sim \pi^* L + C$, so $D$ is effective, nef (it meets every curve other than $C$ nonnegatively, being $\pi^* L + C$, and $D \cdot C = 0$) and big. The restriction $\mathcal{O}_C(D)$ is the degree $0$ line bundle $\mathcal{O}_{C_0}(4L) \otimes \mathcal{O}_{C_0}(-p_1 - \cdots - p_{12})$, which is not torsion for general points. So no section of $mD$ is nonzero along $C$, for any $m \ge 1$, because its restriction would be a nonzero section of a nontrivial degree $0$ line bundle; $C$ lies in the base locus of every $|mD|$, and $D$ is nef and big but not semiample. Zariski proved that $R(S, D)$ is not finitely generated (Zar62; see also Laz04, Chapter 2). By Theorem 9.5.10 and Lemma 9.5.1, it follows that $D$ is not $\mathbb{Q}$-linearly equivalent to $K_S + \Delta$ for any klt $\mathbb{Q}$-boundary $\Delta$: the adjoint form is essential.

### Proof

*Proof of Proposition 9.5.9.* Let $G \sim mD$ be effective and write $G = M + \sum_i g_i N_i$ with $M \ge 0$ containing no $N_i$. Since $G \equiv mP + mN$ and $P \cdot N_j = 0$, the divisor $Z = mN - \sum_i g_i N_i$ satisfies $Z \equiv M - mP$, so $Z \cdot N_j = M \cdot N_j \ge 0$ for every $j$. Write $Z = Y - Y'$ with $Y = \sum_i \max(0, m n_i - g_i) N_i$ and $Y' = \sum_i \max(0, g_i - m n_i) N_i$, which have no common component. For each component $N_j$ of $Y$, $Y' \cdot N_j \ge 0$ because $N_j$ is not a component of $Y'$, so $Y \cdot N_j = Z \cdot N_j + Y' \cdot N_j \ge 0$. Writing $Y = \sum y_j N_j$ with $y_j \ge 0$, this gives $Y^2 = \sum_j y_j \, Y \cdot N_j \ge 0$. The intersection form on the span of the $N_i$ is negative definite, so $Y = 0$, that is $g_i \ge m n_i$ for every $i$. As $g_i$ is an integer, $g_i \ge \lceil m n_i \rceil$, and $G \ge \lceil mN \rceil$.

Since $mD$ is integral, $\lfloor mP \rfloor = \lfloor mD - mN \rfloor = mD - \lceil mN \rceil$. Multiplication by the canonical section of $\mathcal{O}_S(\lceil mN \rceil)$ is injective from $H^0(S, mD - \lceil mN \rceil)$ to $H^0(S, mD)$, and it is surjective because the divisor of every nonzero section of $mD$ is an effective $G \sim mD$, hence $G \ge \lceil mN \rceil$, so the section is divisible by the canonical section. If $m_0 D$ and $m_0 P$ are integral, then for $m = m_0 m'$ the divisor $mN$ is integral and the isomorphisms are multiplication by the $m'$-th power of a fixed section, so they are compatible with products. $\square$

*Proof of Theorem 9.5.10.* If $K_X + \Delta$ is not pseudo-effective, then $H^0(X, \lfloor m(K_X + \Delta) \rfloor) = 0$ for $m \ge 1$, since an effective divisor in $|\lfloor m(K_X + \Delta) \rfloor|$ would make $m(K_X + \Delta)$ the sum of an effective divisor and the effective divisor $m(K_X + \Delta) - \lfloor m(K_X + \Delta) \rfloor$; so $R = k$.

Assume $K_X + \Delta$ is pseudo-effective. Run the log minimal model program of Theorem 2.4.17: it gives klt pairs $(X_i, \Delta_i)$ with $(X_0, \Delta_0) = (X, \Delta)$ and birational morphisms $\varphi_i \colon X_i \to X_{i+1}$, each contracting one irreducible curve $C_i$ with $(K_{X_i} + \Delta_i) \cdot C_i < 0$, with $\Delta_{i+1} = \varphi_{i*} \Delta_i$. The surfaces in the program are $\mathbb{Q}$-factorial, as all klt surfaces are. The program cannot end with a Mori fibre space, because $K_{X_i} + \Delta_i = \varphi_*(K_X + \Delta)$ stays pseudo-effective while on a Mori fibre space it is negative on a family of curves covering the surface. So it ends with $(Y, \Gamma)$, $K_Y + \Gamma$ nef. For each step write $K_{X_i} + \Delta_i = \varphi_i^*(K_{X_{i+1}} + \Delta_{i+1}) + a_i C_i$; intersecting with $C_i$ gives $a_i C_i^2 = (K_{X_i} + \Delta_i) \cdot C_i < 0$, and $C_i^2 < 0$, so $a_i > 0$. Composing, with $\varphi \colon X \to Y$ the composite,
$$K_X + \Delta = \varphi^*(K_Y + \Gamma) + E, \qquad E \ge 0 \text{ and } \varphi\text{-exceptional},$$
since the pullback of an effective exceptional divisor is effective and exceptional.

By Theorem 2.5.22, applied to the lc pair $(Y, \Gamma)$ with $K_Y + \Gamma$ nef, there is $r \ge 1$ with $r(K_Y + \Gamma)$ a base point free Cartier divisor; enlarging $r$, assume also that $r(K_X + \Delta)$ is Cartier. Then $rE = r(K_X + \Delta) - \varphi^* r(K_Y + \Gamma)$ is an integral effective $\varphi$-exceptional Cartier divisor. By Lemma 7.1.6, part 2, with $N = mr(K_Y + \Gamma)$ and the divisor $mrE$, pullback followed by multiplication by the $m$-th power of the canonical section of $\mathcal{O}_X(rE)$ is an isomorphism $H^0(Y, mr(K_Y + \Gamma)) \to H^0(X, mr(K_X + \Delta))$, compatible with products. So $R(X, K_X + \Delta)^{(r)} \cong R(Y, r(K_Y + \Gamma))$, which is finitely generated by Lemma 2.5.15, with $\operatorname{Proj}$ the target of the semiample fibration. By Lemma 9.5.1, $R(X, K_X + \Delta)$ is finitely generated, with the same $\operatorname{Proj}$. $\square$

### Exercises

1. (B) Let $S$ be the blow-up of $\mathbb{P}^2$ at a point with exceptional curve $E$, and $D = \pi^* L + \frac{3}{2} E$. Compute the Zariski decomposition, and use Proposition 9.5.9 to find $R(S, D)$.
2. (B) In Example 9.5.12 replace eight lines by six lines in general position with coefficient $\frac{2}{3}$. Compute $\lfloor m(K + \Delta) \rfloor$, the graded pieces of $R$, and a set of generators.
3. (B) Let $S_0$ be a smooth sextic surface in $\mathbb{P}^3$ and $S$ its blow-up at two points. Compute $R(S, K_S)$ and its Hilbert function.
4. (B) In Example 9.5.13, verify that $D$ is nef by computing $D \cdot E_i$, $D \cdot C$ and $D \cdot \Gamma$ for every other irreducible curve $\Gamma$, and show that $h^0(S, mD) \ge \frac{1}{2} D^2 m^2 - O(m)$ by Riemann-Roch.
5. (C) In Example 9.5.13 the negative part of the Zariski decomposition of $D$ is zero, yet $C$ lies in the base locus of every $|mD|$. Explain why this is consistent with Proposition 9.5.9, and which input of the proof of Theorem 9.5.10 rules out this behaviour for adjoint divisors.
6. (C) Let $(X, \Delta)$ be a projective klt surface pair with $K_X + \Delta$ big. Show without Theorem 2.4.17, using only the Zariski decomposition on a minimal resolution and Theorem 2.5.22 on the contraction of the negative part, that $R(X, K_X + \Delta)$ is finitely generated.

### Lean

Nothing in this section is formalised. The Zariski decomposition and log abundance for surfaces are recorded in Volume 2 with their Lean status.

### Notes and history

Zariski introduced the decomposition named after him in his 1962 paper (Zar62) precisely to study the finite generation of section rings on surfaces, proved finite generation for the canonical ring of a surface, and gave the example of a nef and big divisor with non-finitely generated section ring. The approach through the minimal model program and log abundance is the surface case of the general strategy of the previous section; Lazarsfeld (Laz04) discusses Zariski's example and its variants.
