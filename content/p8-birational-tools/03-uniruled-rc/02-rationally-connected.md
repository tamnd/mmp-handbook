---
title: Rationally connected varieties
nodes: []
sources: [Kol96, Deb01, KMM92a, Cam92, Bea96, Har77]
reads_with: [Deb01:4.2, Kol96:IV.3]
requires: [P3.7, P3.12, P4.2, P4.7, P5.2, P5.4, P5.6, P5.10, P8.1, P8.2]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Rationally connected varieties

### Statement

In this section $k$ is algebraically closed and $X$ is a projective variety of dimension $n \geq 1$ over $k$. Families of rational curves are as in Section 3.1. For a family $F \colon \mathbb{P}^1 \times M \to X$, write
$$F^{(2)} \colon \mathbb{P}^1 \times \mathbb{P}^1 \times M \to X \times X, \qquad (s, s', m) \mapsto (F(s, m), F(s', m)).$$

**Definition P8.3.11 (rationally connected, rationally chain connected).**

1. $X$ is *rationally connected* if there is a family of rational curves $F \colon \mathbb{P}^1 \times M \to X$ with $F^{(2)}$ dominant.
2. $X$ is *rationally chain connected* if there are a variety $M$, a proper flat morphism $u \colon U \to M$ whose fibres over closed points are connected curves all of whose irreducible components are rational curves, and a morphism $F \colon U \to X$ such that $U \times_M U \to X \times X$, $(a, b) \mapsto (F(a), F(b))$, is dominant.

A rationally connected variety is rationally chain connected, with $U = \mathbb{P}^1 \times M$, and it is uniruled, since $F^{(2)}$ dominant forces $F$ dominant with nonconstant members.

**Proposition P8.3.12 (very free curves give rational connectedness).** Let $X$ be smooth, $f \colon \mathbb{P}^1 \to X$ a very free rational curve and $H_0$ the irreducible component of $\operatorname{Hom}(\mathbb{P}^1, X)$ through $[f]$, with its reduced structure. Then $\operatorname{ev}^{(2)} \colon \mathbb{P}^1 \times \mathbb{P}^1 \times H_0 \to X \times X$ is dominant, and $X$ is rationally connected.

Lean: not in Lean as stated.

**Theorem P8.3.13 (Kollár, Miyaoka and Mori; Campana, cited).** Let $k$ have characteristic $0$ and $X$ be smooth.

1. If $X$ is rationally connected, then for every finite set of closed points $x_1, \dots, x_r \in X$ there is a very free rational curve $f \colon \mathbb{P}^1 \to X$ whose image contains $x_1, \dots, x_r$. In particular $X$ is rationally connected if and only if it contains a very free rational curve.
2. If $X$ is rationally chain connected, then $X$ is rationally connected.

Lean: not in Lean as stated.

**Proposition P8.3.14 (no tensor forms).** Let $X$ be smooth and suppose that $X$ contains a very free rational curve, for example that $X$ is rationally connected and $k$ has characteristic $0$. Then for every $m \geq 1$ and every $1 \leq p \leq n$,
$$H^0(X, (\Omega^1_X)^{\otimes m}) = 0, \qquad H^0(X, \Omega^p_X) = 0, \qquad H^0(X, \omega_X^{\otimes m}) = 0.$$

Lean: not in Lean as stated.

**Example P8.3.15 (projective space).** Any two points of $\mathbb{P}^n$ lie on a line, so the family of all lines, with $F^{(2)}$ surjective, shows that $\mathbb{P}^n$ is rationally connected. A line $f$ is very free, with $f^* T_{\mathbb{P}^n} \cong \mathcal{O}(2) \oplus \mathcal{O}(1)^{n-1}$, and Proposition P8.3.14 gives $H^0(\mathbb{P}^n, \Omega^p) = 0$ for $p \geq 1$.

**Example P8.3.16 (the cubic surface).** Let $P_1, \dots, P_6 \in \mathbb{P}^2$ be in general position, $\pi \colon X \to \mathbb{P}^2$ the blow-up and $X \cong Y \subseteq \mathbb{P}^3$ the anticanonical model of Theorem P5.10.3, a smooth cubic surface. Let $\ell \subseteq \mathbb{P}^2$ be a line through none of the $P_i$ and $C = \pi^{-1}(\ell) \cong \ell$. Then $f \colon \mathbb{P}^1 \cong C \subseteq X$ has $f^* T_X \cong \mathcal{O}(2) \oplus \mathcal{O}(1)$, so it is very free, and $X$ is rationally connected. In $Y$, the curve $C$ has degree $-K \cdot C = 3$: it is a twisted cubic. Every smooth cubic surface is of this form (Beauville, Chapter IV (Bea96)), so every smooth cubic surface is rationally connected. A line $L$ on the cubic surface is not free, with $f^* T \cong \mathcal{O}(2) \oplus \mathcal{O}(-1)$ by Proposition P8.1.18.

**Example P8.3.17 (uniruled but not rationally connected).** Let $C$ be a smooth projective curve of genus $g \geq 1$ and $X = C \times \mathbb{P}^1$, uniruled by Example P8.3.9. Then $X$ is not rationally chain connected, and $H^0(X, \Omega^1_X) \neq 0$.

### Proof in words

A very free curve can be deformed so that its two marked points move independently in all directions: the obstruction to prescribing first order motions of $f(0)$ and $f(\infty)$ is $H^1(f^* T_X(-2))$, which vanishes. So the evaluation map at two points is dominant from the family of deformations, and two general points lie on one curve of the family. The same positivity kills tensor forms: pulled back to a very free curve, the cotangent bundle is a sum of line bundles of negative degree, so a tensor form vanishes along every very free curve, and these cover a dense subset of $X$.

The converse statements, that in characteristic $0$ a rationally connected variety has very free curves through any finite set of points and that chains can be smoothed to single curves, are deeper. A chain of free curves glued at points can be deformed to an irreducible curve once enough free curves are attached, a technique called smoothing combs, and these results are cited.

### Examples

*Example P8.3.15.* For a line $f$, the Euler sequence of Theorem P3.12.20 restricted to $f(\mathbb{P}^1)$ and the tangent-normal sequence of the line, $0 \to \mathcal{O}(2) \to f^* T_{\mathbb{P}^n} \to \mathcal{O}(1)^{n-1} \to 0$, split since $\operatorname{Ext}^1(\mathcal{O}(1), \mathcal{O}(2)) = H^1(\mathcal{O}(1)) = 0$.

*Example P8.3.16.* Since $\ell$ misses the $P_i$, $\pi$ is an isomorphism over a neighbourhood of $\ell$, and $C = \pi^* \ell$. By Theorem P5.6.3, $C^2 = \ell^2 = 1$ and $K_X \cdot C = (\pi^* K_{\mathbb{P}^2} + \sum_i E_i) \cdot \pi^* \ell = -3$. The normal bundle $N_{C/X} = \mathcal{O}_C(C)$ has degree $C^2 = 1$, so $N_{C/X} \cong \mathcal{O}(1)$. Dualizing the conormal sequence of Theorem P3.12.14 gives $0 \to T_C \to T_X|_C \to N_{C/X} \to 0$, an extension of $\mathcal{O}(1)$ by $\mathcal{O}(2)$, classified by $\operatorname{Ext}^1(\mathcal{O}(1), \mathcal{O}(2)) = H^1(\mathcal{O}(1)) = 0$, by Proposition P4.7.2 and Theorem P4.2.1. So $f^* T_X \cong \mathcal{O}(2) \oplus \mathcal{O}(1)$, both degrees at least $1$, and Proposition P8.3.12 applies. Proposition P8.3.14 gives $H^0(X, \Omega^1_X) = 0$ and $H^0(X, \omega_X^{\otimes m}) = 0$, in agreement with $q = p_g = 0$ for the blown-up plane.

*Example P8.3.17.* Every rational curve on $X$ is a fibre $\{c\} \times \mathbb{P}^1$, by Example P8.3.9, so every connected curve with rational components lies in one fibre. In Definition P8.3.11, the image of $U \times_M U$ in $X \times X$ then lies in the proper closed subset $\{(a, b) : p_1(a) = p_1(b)\}$, so it is not dominant. By Proposition P3.12.23, $\Omega^1_X \cong p_1^* \omega_C \oplus p_2^* \Omega^1_{\mathbb{P}^1}$, and the pullback of a nonzero section of $\omega_C$, which exists since $g \geq 1$, is a nonzero global $1$-form.

### Proof

*Proposition P8.3.12.* Let $E = f^* T_X \cong \bigoplus_i \mathcal{O}(a_i)$ with all $a_i \geq 1$. By Corollary P8.1.13, $\operatorname{Hom}(\mathbb{P}^1, X)$ is smooth at $[f]$, so $H_0$ is smooth at $[f]$ with $T_{[f]} H_0 = H^0(\mathbb{P}^1, E)$ by Theorem P8.1.9. By Exercise 6 of Section 1.2, applied to each factor, the differential of $\operatorname{ev}^{(2)}$ at $(0, \infty, [f])$ is
$$(v, v', \sigma) \mapsto (df_0(v) + \sigma(0), \ df_\infty(v') + \sigma(\infty)).$$
Its restriction to $H^0(E)$ is the restriction map $H^0(E) \to E|_0 \oplus E|_\infty$, which sits in the cohomology sequence of
$$0 \to E(-2) \to E \to E|_0 \oplus E|_\infty \to 0,$$
where $E(-2) = E \otimes \mathcal{O}(-0 - \infty)$. Since $E(-2) \cong \bigoplus_i \mathcal{O}(a_i - 2)$ with $a_i - 2 \geq -1$, part 3 of Corollary P5.4.11 gives $H^1(E(-2)) = 0$, so the restriction map is surjective, and so is the differential. The variety $\mathbb{P}^1 \times \mathbb{P}^1 \times H_0$ is smooth at $(0, \infty, [f])$, and Lemma P8.3.3 shows that $\operatorname{ev}^{(2)}$ is dominant.

*Theorem P8.3.13.* Part 1 is Kollár, Miyaoka and Mori (KMM92a), and Kollár, Chapter IV, Section 3 (Kol96); part 2 is due to Kollár, Miyaoka and Mori (KMM92a) and to Campana (Cam92), and is also in Kollár, Chapter IV, Section 3. See also Debarre, Chapter 4 (Deb01). The proofs are not given here. Part 1 starts from a free curve through a general point, given by part 4 of Theorem P8.3.4, and uses the dominance of the two-point evaluation map, through generic smoothness, to show that the general member is very free. Part 2 deforms a chain of free curves, after attaching more free curves, into a single very free curve.

*Proposition P8.3.14.* Let $f$ be very free and $H_0$ as in Proposition P8.3.12. On $\mathbb{P}^1 \times H_0$, the sheaf $\mathcal{G} = \operatorname{ev}^* T_X \otimes p_1^* \mathcal{O}(-2)$ is locally free, hence flat over $H_0$, and its restriction to $\mathbb{P}^1 \times \{[g]\}$ is $g^* T_X(-2)$. By Theorem P4.5.13, the set $H_0^{vf}$ of $[g]$ with $H^1(g^* T_X(-2)) = 0$ is open, and it contains $[f]$. By Theorem P5.4.10 and part 3 of Corollary P5.4.11, $g^* T_X(-2) \cong \bigoplus_i \mathcal{O}(b_i - 2)$ has $H^1 = 0$ exactly when every $b_i \geq 1$, so $H_0^{vf}$ is the set of very free members. By part 3 of Theorem P8.3.4 and the proof of Proposition P8.3.12, $\operatorname{ev} \colon \mathbb{P}^1 \times H_0^{vf} \to X$ is dominant, so the closed points of $X$ lying on very free curves are dense.

Let $\mathcal{T}$ be one of the locally free sheaves $(\Omega^1_X)^{\otimes m}$, $\Omega^p_X$ or $\omega_X^{\otimes m}$, and $s \in H^0(X, \mathcal{T})$. For a very free $g$ with $g^* T_X \cong \bigoplus_i \mathcal{O}(b_i)$, $b_i \geq 1$, the sheaf $g^* \Omega^1_X \cong \bigoplus_i \mathcal{O}(-b_i)$, and $g^* \mathcal{T}$ is a direct sum of line bundles $\mathcal{O}(-b_{i_1} - \dots - b_{i_r})$ with $r = m$, $r = p$ or $r = n m$, all of negative degree. So $g^* s = 0$, and $s$ vanishes in the fibre of $\mathcal{T}$ at every point of $g(\mathbb{P}^1)$. The zero set of $s$ is closed and contains a dense set of closed points, so it is $X$, and since $X$ is reduced, $s = 0$.

### Exercises

1. (A) Show that a product of two rationally connected varieties is rationally connected, and that $\mathbb{P}^1 \times \mathbb{P}^1$ contains very free curves of bidegree $(1, 1)$.
2. (B) Let $X$ be smooth and rationally connected, $k$ of characteristic $0$. Using Proposition P8.3.14 and Hodge theory over $\mathbb{C}$, show that $\chi(\mathcal{O}_X) = 1$ when $k = \mathbb{C}$.
3. (A) Show that a smooth quadric $Q \subseteq \mathbb{P}^{n+1}$, $n \geq 2$, is rationally connected, by projecting from a point of $Q$ or by exhibiting a very free conic.
4. (B) Let $X$ be a smooth projective surface containing a very free rational curve. Show that $q(X) = 0$ and $p_g(X) = 0$.
5. (B) Show that a unirational variety, one that admits a dominant rational map from $\mathbb{P}^n$, is rationally connected. In characteristic $0$, deduce that it has no nonzero global $1$-forms.
6. (C) Let $X$ be the cone over a smooth plane cubic, a normal surface in $\mathbb{P}^3$. Show that $X$ is rationally chain connected, every two points being joined by two lines through the vertex, but not rationally connected, by considering a resolution of the vertex. Explain why part 2 of Theorem P8.3.13 needs smoothness.

### Lean

Rationally connected and rationally chain connected varieties are not in the repository, and neither are the sheaves of differential forms of higher degree on general varieties; `MinimalModel/Statements/Basic.lean` has the canonical divisor `MinimalModel.CanonicalDivisor` but no statement about the vanishing of forms.

### Notes and history

Rationally connected varieties were introduced independently by Kollár, Miyaoka and Mori (KMM92a) and by Campana (Cam92), as the higher-dimensional analogue of rational surfaces: in dimension $2$ over $\mathbb{C}$, Castelnuovo's criterion shows that a smooth projective surface is rationally connected if and only if it is rational. In dimension at least $3$ there are rationally connected varieties that are not rational, such as smooth cubic threefolds, by Clemens and Griffiths, so rational connectedness is the notion that behaves well in families and under fibrations, as Section 3.3 shows. Theorem P8.3.13 is in Kollár, Chapter IV (Kol96), and Debarre, Chapter 4 (Deb01). In characteristic $p$ the right notion is separable rational connectedness, the existence of a very free curve, and Proposition P8.3.12 holds in that form. The two notions differ: for $p \geq 3$ the Fermat surfaces of Example P8.3.10 are unirational, hence rationally connected, but they have nonzero pluricanonical forms, since $K = (p - 3) H$, so by Proposition P8.3.14 they contain no very free curve, and part 1 of Theorem P8.3.13 fails in characteristic $p$.
