---
title: Mumford's intersection pairing
nodes: []
sources: [Mum61, KM98, Har77, Kol13]
reads_with: [KM98:ch4, Bea96:ch2]
requires: [P3.11, P5.5, P5.7, P5.8, P5.12, 4.3]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Mumford's intersection pairing

### Statement

In this chapter $k$ is an algebraically closed field, and a surface is an integral separated scheme of finite type over $k$ of dimension 2. Let $X$ be a normal projective surface. A *resolution* of $X$ is a birational morphism $f \colon Y \to X$ from a smooth projective surface $Y$. In characteristic 0 a resolution exists by Theorem 4.2.10; for surfaces it exists in every characteristic, by the theorem of Lipman cited in the notes. For a resolution, Theorem P5.8.3 gives a finite set $T_0 \subset X$ over which $f$ is not an isomorphism, and finitely many exceptional curves $E_1, \dots, E_r$, the components of the fibres over $T_0$. Their intersection matrix $M = (E_i \cdot E_j)$ is negative definite. An *$\mathbb{R}$-Weil divisor* on $X$ is a finite formal sum of integral curves of $X$ with real coefficients, as in Section 1 of Chapter P5.8, and $f^{-1}_*$, $f_*$ and Mumford's pullback $f^*$ are those of Corollary P5.8.5.

**Definition 2.3.1 (Mumford's intersection pairing).** Let $f \colon Y \to X$ be a resolution. For $\mathbb{R}$-Weil divisors $D$ and $D'$ on $X$, *Mumford's intersection number* is
$$D \cdot D' = f^*D \cdot f^*D'.$$
A divisor $D$ is *numerically trivial*, written $D \equiv 0$, if $D \cdot B = 0$ for every $\mathbb{R}$-Weil divisor $B$ on $X$, and $D \equiv D'$ means $D - D' \equiv 0$. The real vector space of $\mathbb{R}$-Weil divisors modulo numerical equivalence is $N^1_W(X)$.

For an integral projective curve $\Gamma$ and a line bundle $N$ on $\Gamma$, put $\deg N = \chi(N) - \chi(\mathcal{O}_\Gamma)$. On a smooth projective surface $S$, Proposition P5.5.12 says that $B \cdot C = \deg \mathcal{O}_S(B)|_C$ for a divisor $B$ and an integral curve $C$.

**Lemma 2.3.2 (the degree on a curve under a birational morphism).** Let $g \colon S \to T$ be a birational morphism from a smooth projective surface onto a normal projective surface, $N$ a line bundle on $T$, and $C'$ an integral curve on $S$. If $C'$ is $g$-exceptional, then $\deg (g^*N)|_{C'} = 0$. Otherwise $\deg (g^*N)|_{C'} = \deg N|_{g(C')}$. In particular, if $T$ is smooth, then $g^*B \cdot C' = B \cdot g_* C'$ for every $\mathbb{R}$-divisor $B$ on $T$ and every integral curve $C'$ on $S$.

Lean: not yet in Lean.

**Proposition 2.3.3 (independence of the resolution).** Let $f \colon Y \to X$ be a resolution and $g \colon Y' \to Y$ a birational morphism of smooth projective surfaces. Then $(f \circ g)^* D = g^*(f^*D)$ for every $\mathbb{R}$-Weil divisor $D$ on $X$. If $f_1$ and $f_2$ are two resolutions of $X$, then $f_1^* D \cdot f_1^* D' = f_2^* D \cdot f_2^* D'$. So Mumford's intersection number does not depend on the resolution.

Lean: not yet in Lean.

**Theorem 2.3.4 (properties of Mumford's pairing).** Let $X$ be a normal projective surface and $f \colon Y \to X$ a resolution.

1. The pairing is symmetric and $\mathbb{R}$-bilinear, and it takes rational values on $\mathbb{Q}$-Weil divisors.
2. If $D$ is a Cartier divisor and $C$ an integral curve on $X$, then $D \cdot C = \deg \mathcal{O}_X(D)|_C$. If $X$ is smooth, the pairing is the pairing of Theorem P5.5.6.
3. A principal divisor is numerically trivial. So the pairing is defined on $\operatorname{Cl}(X) \otimes \mathbb{R}$.
4. If $D, D' \ge 0$ have no common component, then $D \cdot D' \ge 0$, and $D \cdot D' > 0$ if their supports meet.
5. (*Projection formula.*) $f^*D \cdot B = D \cdot f_* B$ for every $\mathbb{R}$-Weil divisor $D$ on $X$ and every $\mathbb{R}$-divisor $B$ on $Y$.
6. If $H$ is an ample Cartier divisor, then $H^2 > 0$ and $H \cdot C > 0$ for every integral curve $C$.

Lean: not yet in Lean.

Let $N^1(Y)$ be the real Néron-Severi space of Definition P5.12.1, and let $E^\perp \subset N^1(Y)$ be the subspace of classes $\alpha$ with $\alpha \cdot [E_i] = 0$ for $i = 1, \dots, r$.

**Proposition 2.3.5 (the numerical classes of Weil divisors).** Let $f \colon Y \to X$ be a resolution with $r$ exceptional curves. Then $D \equiv 0$ on $X$ if and only if $f^*D \equiv 0$ on $Y$, and $D \mapsto [f^*D]$ induces an isometry $N^1_W(X) \to E^\perp$ onto $E^\perp$. So $N^1_W(X)$ has dimension $\rho(Y) - r$, Mumford's pairing on it is nondegenerate, and its signature is $(1, \rho(Y) - r - 1)$.

Lean: not yet in Lean.

**Theorem 2.3.6 (Hodge index theorem for normal surfaces).** Let $X$ be a normal projective surface, and let $H$ be an $\mathbb{R}$-Weil divisor with $H^2 > 0$, for instance an ample Cartier divisor. If $D \cdot H = 0$, then $D^2 \le 0$, with equality if and only if $D \equiv 0$. For every $\mathbb{R}$-Weil divisor $D$,
$$(D \cdot H)^2 \ge D^2 \, H^2.$$

Lean: not yet in Lean.

### Proof in words

All the work is on $Y$. Mumford's pullback is the unique lift of $D$ that is orthogonal to the exceptional curves, so any operation that keeps this property and pushes forward to $D$ gives the same lift. A further blow-up $g$ keeps it, by the projection formula on smooth surfaces, so the pullback is compatible with domination. Two resolutions are dominated by a third, by elimination of indeterminacy, and the intersection numbers agree.

The projection formula on $X$ is the same orthogonality: the part of $B$ that $f_*$ forgets is exceptional, and $f^*D$ does not see it. Orthogonality also identifies the Weil divisors of $X$ modulo numerical equivalence with the orthogonal complement of the exceptional curves in $N^1(Y)$. The span of the exceptional curves is negative definite, so it takes $r$ negative squares from the signature $(1, \rho(Y) - 1)$ of $N^1(Y)$, and the complement keeps the one positive square. The Hodge index theorem on $X$ is the statement that a form of signature $(1, m)$ is negative definite on the orthogonal complement of a vector of positive square.

### Examples

**Example 2.3.7 (the quadric cone).** Let $T = V_+(xy - z^2) \subset \mathbb{P}^3$ be the quadric cone with vertex $v$, and $f \colon S \to T$ the blow-up of $v$, with exceptional $(-2)$-curve $E$ (Example P5.8.9). For a line $L_a$ through $v$, Example P5.8.9 computes $f^* L_a = \tilde L_a + \frac12 E$, $L_a^2 = \frac12$ and $L_a \cdot L_b = \frac12$ for $a \ne b$. The plane section $H = T \cap V_+(w)$ misses $v$, so $f^*H$ is its strict transform; and $2 L_a = T \cap H_a$ is a plane section, so $H \sim 2 L_a$ and $H^2 = 4 L_a^2 = 2 = \deg T$. Here $S \cong F_2$ (Example P3.11.29 and Example 2.3.8 with $n = 2$), so $\rho(S) = 2$, and $r = 1$, so $N^1_W(T)$ is a line, spanned by $L_a$. The Hodge index theorem holds with equality, $(L_a \cdot H)^2 = 1 = L_a^2 H^2$, as it must for proportional classes.

**Example 2.3.8 (the cone over a rational normal curve).** Let $n \ge 1$ and let $F_n$ be the Hirzebruch surface of Theorem P3.11.25, with negative section $C_-$, positive section $C_+ \sim C_- + nF$ disjoint from $C_-$, and fibre class $F$. By Example P5.12.8,
$$C_-^2 = -n, \qquad F^2 = 0, \qquad C_- \cdot F = 1, \qquad K_{F_n} = -2C_- - (n+2)F,$$
and $\operatorname{Num}(F_n) = \mathbb{Z} C_- \oplus \mathbb{Z} F$, since these two classes have Gram determinant $-1$. By Example P5.8.19 and Theorem P5.8.16, $C_-$ is contracted by a birational morphism $f \colon F_n \to X_n$ onto a normal projective surface, to a rational singularity $v$ of multiplicity $n$. For $n = 1$ the point is smooth and $X_1 = \mathbb{P}^2$; for $n = 2$, $X_2$ is the quadric cone of Example 2.3.7. In general $X_n$ is the projective cone over the rational normal curve of degree $n$, and Volume 4 calls the germ at $v$ the quotient $\frac1n(1,1)$ (Example 4.3.7). The computations here use only the contraction $f$.

Let $\ell = f(F)$ be the image of a fibre, a line through $v$, and $H = f(C_+)$. Since $C_+ \cap C_- = \emptyset$, $f$ is an isomorphism near $C_+$, so $H$ is a Cartier divisor with $f^*H = C_+$. For $\ell$, the coefficient $c$ in $f^*\ell = F + cC_-$ solves $(F + cC_-) \cdot C_- = 1 - nc = 0$, so
$$f^*\ell = F + \tfrac1n C_-, \qquad \ell^2 = F^2 + \tfrac2n F \cdot C_- + \tfrac{1}{n^2} C_-^2 = \tfrac2n - \tfrac1n = \tfrac1n.$$
Two distinct lines $\ell, \ell'$ have $\ell \cdot \ell' = (F + \frac1n C_-) \cdot (F' + \frac1n C_-) = 0 + \frac1n + \frac1n - \frac1n = \frac1n$, although they meet only at $v$. Further $H^2 = C_+^2 = (C_- + nF)^2 = -n + 2n = n$ and $\ell \cdot H = (F + \frac1n C_-) \cdot (C_- + nF) = 1 + \frac1n(-n + n) = 1$. The relation $C_+ \sim C_- + nF$ pushes forward to $H \sim n\ell$, consistent with $n \ell^2 = \ell \cdot H$.

Here $\rho(F_n) = 2$ and $r = 1$. The space $E^\perp$ consists of the classes $\alpha C_- + \beta F$ with $-n\alpha + \beta = 0$, the line spanned by $C_- + nF = f^*H$. So $N^1_W(X_n) = \mathbb{R}\ell$ with $\ell^2 = \frac1n > 0$, of signature $(1, 0)$, as Proposition 2.3.5 says.

**Counterexample 2.3.9 (the strict transform is not the pullback).** In Example 2.3.8 the strict transform $F$ of $\ell$ has $F^2 = 0 \ne \frac1n = \ell^2$, and $F \cdot C_- = 1$ while $\ell \cdot f_*C_- = \ell \cdot 0 = 0$. So the projection formula of Theorem 2.3.4 fails if the Mumford pullback is replaced by the strict transform. The value $\ell \cdot \ell' = \frac1n$ also shows that Mumford's pairing is not integral on Weil divisors, and that $\ell$ is not Cartier at $v$ for $n \ge 2$: if it were, part 2 of Theorem 2.3.4 would make $\ell \cdot \ell' = \deg \mathcal{O}_X(\ell)|_{\ell'}$ an integer. Section 2 shows that $n\ell$ is Cartier.

### Proof

*Lemma 2.3.2.* If $C'$ is exceptional, then $(g^*N)|_{C'}$ is the pullback of $N|_{\{g(C')\}}$ along the constant map $C' \to g(C')$, a trivial bundle, and its degree is 0. Otherwise $\Gamma = g(C')$ is an integral curve, and $\nu = g|_{C'} \colon C' \to \Gamma$ is proper. Its fibres are finite: over $T \setminus T_0$ they are single points, and over a point of the finite set $T_0$ the fibre of $g$ is a union of exceptional curves, which meets $C'$ in finitely many points. So $\nu$ is finite (Corollary P4.6.17). It is birational, since $g$ is an isomorphism over $T \setminus T_0$ and $C' \not\subset g^{-1}(T_0)$. So $\mathcal{O}_\Gamma \to \nu_* \mathcal{O}_{C'}$ is injective with a cokernel $Q$ of finite length. For a line bundle $N_\Gamma$ on $\Gamma$, the projection formula gives $\nu_* \nu^* N_\Gamma = N_\Gamma \otimes \nu_* \mathcal{O}_{C'}$, and $\nu$ is affine, so
$$\chi(C', \nu^* N_\Gamma) = \chi(\Gamma, N_\Gamma \otimes \nu_*\mathcal{O}_{C'}) = \chi(N_\Gamma) + \chi(N_\Gamma \otimes Q) = \chi(N_\Gamma) + \operatorname{length} Q,$$
because $N_\Gamma$ is locally free and $Q$ has finite support. For $N_\Gamma = \mathcal{O}_\Gamma$ this gives $\chi(\mathcal{O}_{C'}) = \chi(\mathcal{O}_\Gamma) + \operatorname{length} Q$. Subtract, with $N_\Gamma = N|_\Gamma$: $\deg (g^*N)|_{C'} = \deg N|_\Gamma$. If $T$ is smooth and $B$ is a divisor, Proposition P5.5.12 on both surfaces turns this into $g^*B \cdot C' = B \cdot g_*C'$, where $g_* C' = 0$ in the exceptional case. Both sides are linear in $B$, which gives the statement for $\mathbb{R}$-divisors. $\square$

*Proposition 2.3.3.* Put $h = f \circ g$, a birational morphism from $Y'$ onto $X$, and $B = f^*D$. By Corollary P5.8.5 applied to $g$, $g^*B$ is the usual pullback, it equals $g^{-1}_*B$ plus a $g$-exceptional divisor, and $g_* g^* B = B$. So $h_* g^*B = f_* g_* g^* B = f_* B = D$. Let $C'$ be an $h$-exceptional curve. If $C'$ is $g$-exceptional, then $g^*B \cdot C' = 0$ by Lemma 2.3.2. Otherwise $C = g(C')$ is a curve with $f(C)$ a point, an $f$-exceptional curve, and Lemma 2.3.2 gives $g^*B \cdot C' = B \cdot C = 0$. So $g^*B$ has the two properties of Corollary P5.8.5 for $h$, and by uniqueness $h^*D = g^* f^* D$.

Now let $f_1 \colon Y_1 \to X$ and $f_2 \colon Y_2 \to X$ be resolutions. The surface $Y_2$ is projective, so by Theorem P5.7.9 the birational map $f_2^{-1} \circ f_1$ becomes a morphism $g \colon Y_3 \to Y_2$ after a composite of point blow-ups $\pi \colon Y_3 \to Y_1$. The morphisms $f_1 \circ \pi$ and $f_2 \circ g$ agree on a dense open subset of the reduced scheme $Y_3$, and $X$ is separated, so they are equal. By the first part, $\pi^* f_1^* D = (f_1 \circ \pi)^* D = (f_2 \circ g)^* D = g^* f_2^* D$. By part 2 of Theorem P5.7.12, extended bilinearly to $\mathbb{R}$-divisors, pullback by a birational morphism of smooth projective surfaces preserves intersection numbers. So
$$f_1^*D \cdot f_1^*D' = \pi^* f_1^* D \cdot \pi^* f_1^* D' = g^* f_2^*D \cdot g^* f_2^* D' = f_2^*D \cdot f_2^*D'. \qquad \square$$

*Theorem 2.3.4.* (1) Corollary P5.8.5 says that $f^*$ is linear and sends divisors with integer coefficients to $\mathbb{Q}$-divisors, and the pairing on $Y$ is symmetric and bilinear.

(2) Let $\tilde C = f^{-1}_* C$. Then $f^*C = \tilde C + Z$ with $Z$ exceptional, and $f^*D \cdot Z = 0$ by Corollary P5.8.5. Since $D$ is Cartier, $f^*D$ is the usual pullback of $\mathcal{O}_X(D)$, so
$$D \cdot C = f^*D \cdot \tilde C = \deg (f^*\mathcal{O}_X(D))|_{\tilde C} = \deg \mathcal{O}_X(D)|_C$$
by Proposition P5.5.12 and Lemma 2.3.2. If $X$ is smooth, take $f = \mathrm{id}$, which is a resolution, and use Proposition 2.3.3.

(3) A principal divisor $\operatorname{div}_X(h)$ is Cartier, so its Mumford pullback is its usual pullback $\operatorname{div}_Y(h)$, which is numerically trivial on $Y$ by Theorem P5.5.6. So $\operatorname{div}_X(h) \cdot D' = \operatorname{div}_Y(h) \cdot f^*D' = 0$.

(4) Write $f^*D = \tilde D + B$ and $f^*D' = \tilde D' + B'$ with $\tilde D, \tilde D'$ the strict transforms and $B, B'$ exceptional. By Corollary P5.8.5, $B, B' \ge 0$. Then $f^*D \cdot f^*D' = f^*D \cdot \tilde D' = \tilde D \cdot \tilde D' + B \cdot \tilde D'$. Both terms are at least 0 by Proposition P5.5.5, since $\tilde D, \tilde D'$ are effective with no common component and $\tilde D'$ has no exceptional component. Let $x \in \operatorname{Supp} D \cap \operatorname{Supp} D'$. If $x \notin T_0$, then $f$ is an isomorphism near $f^{-1}(x)$, the curves $\tilde D$ and $\tilde D'$ meet at $f^{-1}(x)$, and $\tilde D \cdot \tilde D' > 0$. If $x \in T_0$, let $E_1, \dots, E_s$ be the curves over $x$ and $B_x$ the part of $B$ supported on them. A component $\Gamma$ of $D$ through $x$ has strict transform with $f(f^{-1}_*\Gamma) = \Gamma \ni x$, so $\tilde D$ meets $f^{-1}(x)$ and $\tilde D \cdot E_j > 0$ for some $j \le s$. For $j \le s$, $B_x \cdot E_j = B \cdot E_j = -\tilde D \cdot E_j \le 0$, because the curves over other points of $T_0$ are disjoint from $E_j$. So $B_x \ne 0$, and Theorem P5.8.2 for the connected configuration $E_1, \dots, E_s$ gives that every coefficient of $B_x$ is positive. In the same way $\tilde D'$ meets some $E_i$ with $i \le s$, and $B \cdot \tilde D' \ge B_x \cdot \tilde D' > 0$.

(5) Write $B = f^{-1}_* f_* B + B_e$ with $B_e$ exceptional; this holds because $f_*$ is injective on non-exceptional curves (proof of Corollary P5.8.4). Also $f^* f_* B = f^{-1}_* f_* B + B_e'$ with $B_e'$ exceptional. Since $f^*D \cdot B_e = f^*D \cdot B_e' = 0$,
$$f^*D \cdot B = f^*D \cdot f^{-1}_* f_* B = f^*D \cdot f^* f_* B = D \cdot f_*B.$$

(6) Let $C$ be an integral curve. By part 2, $H \cdot C = \deg \mathcal{O}_X(H)|_C$, and an ample line bundle has positive degree on an integral projective curve (its restriction is ample, and some power has a nonzero section with a zero). So $H \cdot C > 0$. Some multiple $mH$ is linearly equivalent to an effective divisor $\sum_j m_j C_j$ with $m_j > 0$, so by part 3 and bilinearity $m H^2 = \sum_j m_j \, H \cdot C_j > 0$. $\square$

*Proposition 2.3.5.* If $D \equiv 0$ on $X$, then for every integral curve $C$ of $Y$, part 5 of Theorem 2.3.4 gives $f^*D \cdot C = D \cdot f_*C = 0$, so $f^*D \equiv 0$. If $f^*D \equiv 0$, then $D \cdot B = f^*D \cdot f^*B = 0$ for every $B$. So $D \mapsto [f^*D]$ is a well defined injective linear map $N^1_W(X) \to N^1(Y)$, and it preserves the pairing by definition. Its image lies in $E^\perp$ by Corollary P5.8.5.

Every $\alpha \in N^1(Y)$ is the class of an $\mathbb{R}$-divisor $B$. Let $\alpha \in E^\perp$. As in part 5, $B - f^*f_*B$ is exceptional, and $(B - f^*f_*B) \cdot E_i = 0$ for every $i$. By the last statement of Corollary P5.8.4 it is 0. So $\alpha = [f^* f_* B]$ lies in the image.

The classes $[E_1], \dots, [E_r]$ are linearly independent in $N^1(Y)$, because $M$ is invertible, and their span $W$ is negative definite. So $N^1(Y) = W \oplus E^\perp$, an orthogonal sum, and $\dim E^\perp = \rho(Y) - r$. By Lemma P5.12.3 the form on $N^1(Y)$ has signature $(1, \rho(Y) - 1)$. Signatures add over orthogonal sums, so $E^\perp$ has signature $(1, \rho(Y) - r - 1)$. In particular it is nondegenerate. $\square$

*Theorem 2.3.6.* By Proposition 2.3.5, $V = N^1_W(X)$ is a real quadratic space of signature $(1, m)$, and its class $h = [H]$ has $h^2 > 0$. Then $V = \mathbb{R}h \oplus h^\perp$ is an orthogonal sum, and signatures add, so $h^\perp$ has signature $(0, m)$: it is negative definite. So $D \cdot H = 0$ gives $D^2 \le 0$, with equality only if $[D] = 0$, that is $D \equiv 0$. For any $D$ with class $d$, the class $d - \frac{d \cdot h}{h^2} h$ lies in $h^\perp$, so its square $d^2 - \frac{(d \cdot h)^2}{h^2}$ is at most 0, which is the inequality. An ample Cartier $H$ has $H^2 > 0$ by part 6 of Theorem 2.3.4. $\square$

### Exercises

1. (A) In Example 2.3.8 with $n = 2$, check that the numbers $C_-^2 = -2$, $C_- \cdot F = 1$, $F^2 = 0$ agree with Example 2.3.7, and that $\rho(F_2) - 1 = 1 = \dim N^1_W(X_2)$.
2. (A) In Example 2.3.8, compute $(a\ell + bH)^2$ and verify the inequality $(D \cdot H)^2 \ge D^2 H^2$ for $D = a\ell + bH$. When does equality hold?
3. (A) Let $X$ be a normal projective surface and $D$ a Weil divisor whose support does not meet $T_0$. Show that $f^*D = f^{-1}_*D$ and that $D \cdot D'$ is the usual intersection number on the smooth locus when $D'$ is also disjoint from $T_0$.
4. (B) Let $f \colon Y \to X$ be a resolution and $B$ an $\mathbb{R}$-divisor on $Y$ with $B \cdot E_i \ge 0$ for every exceptional curve $E_i$. Show that $f^* f_* B - B$ is effective, using Corollary P5.8.4. Give an example with $f^*f_*B \ne B$.
5. (B) Let $X$ have one singular point, with resolution $f$ and matrix $M$. For Weil divisors $D, D'$, show that $D \cdot D' = \tilde D \cdot \tilde D' - u^T M^{-1} u'$, where $u_i = \tilde D \cdot E_i$ and $u'_i = \tilde D' \cdot E_i$. Recover $\ell^2 = \frac1n$ in Example 2.3.8 from this formula.
6. (C) Let $X$ be a normal projective surface. Show that the numerically trivial Cartier divisors form a subgroup of $\operatorname{Pic}(X)$, and that $N^1(X) = (\operatorname{Pic}(X)/\equiv) \otimes \mathbb{R}$ maps injectively to $N^1_W(X)$. Show that the map is onto when every Weil divisor of $X$ is $\mathbb{Q}$-Cartier.

### Lean

Nothing in this section is in Lean. The project library has no intersection numbers of curves on a surface and no resolution of surfaces. Mathlib has the linear algebra: `Matrix.PosDef` for positive definite matrices, `Matrix.det`, and the diagonalization of real quadratic forms in `QuadraticForm`. The handbook adds no `MinimalModel` node here.

### Notes and history

Mumford defined the rational intersection numbers of Weil divisors on a normal surface in 1961 (Mum61, Section II(b)), as a step in his proof that a normal surface singularity with trivial local fundamental group is smooth. The independence of the resolution is Exercise 6 of Section 1 of Chapter P5.8, proved here. Sakai (Sak84) developed the theory of Weil divisors on normal surfaces systematically, including the Riemann-Roch theorem with a correction term at each singular point and the Zariski decomposition of a Weil divisor, and KM98, Section 4.1, uses Mumford's pairing to define numerically lc and klt surface pairs. The existence of a resolution of an excellent surface in every characteristic is Lipman's theorem (*Desingularization of two-dimensional schemes*, Annals of Mathematics 107, 1978), after Zariski and Abhyankar.
