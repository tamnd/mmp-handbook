---
title: Semicontinuity and cohomology and base change
nodes: []
sources: [Har77, Vak25, GW23]
reads_with: [Har77:III.12, Vak25:ch25]
requires: [P1.1, P3.13, P4.3, P4.4, P4.5]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Semicontinuity and cohomology and base change

### Statement

Throughout, $Y$ is locally Noetherian, $f \colon X \to Y$ is projective with $X \subseteq \mathbb{P}^n_Y$, and $\mathcal{F}$ is a coherent sheaf on $X$ that is flat over $Y$. For $y \in Y$ write
$$h^q(y) = \dim_{\kappa(y)} H^q(X_y, \mathcal{F}_y), \qquad \chi(y) = \sum_q (-1)^q h^q(y),$$
and let $\varphi^q(y) \colon R^q f_* \mathcal{F} \otimes \kappa(y) \to H^q(X_y, \mathcal{F}_y)$ be the base change map of Section 5.1.

**Theorem P4.5.13 (semicontinuity).** For every $q$ and every integer $m$ the set $\{y \in Y : h^q(y) \geq m\}$ is closed, that is, $h^q$ is upper semicontinuous. The Euler characteristic $\chi(y)$ is locally constant on $Y$.

Lean: not in Lean as stated.

**Theorem P4.5.14 (cohomology and base change).** Let $y \in Y$ and $q \geq 0$.

1. If $\varphi^q(y)$ is surjective, it is an isomorphism, and $\varphi^q(y')$ is an isomorphism for all $y'$ in an open neighbourhood of $y$.
2. If $\varphi^q(y)$ is surjective, then $\varphi^{q-1}(y)$ is surjective if and only if $R^q f_* \mathcal{F}$ is locally free in a neighbourhood of $y$.

Lean: not in Lean as stated.

For $q = 0$ the map $\varphi^{-1}(y)$ has target $0$ and is surjective, so part 2 says that $f_* \mathcal{F}$ is locally free near $y$ whenever $\varphi^0(y)$ is surjective.

**Corollary P4.5.15 (vanishing on all fibres).** If $H^q(X_y, \mathcal{F}_y) = 0$ for every $y \in Y$, then $R^q f_* \mathcal{F} = 0$, and $\varphi^{q-1}(y)$ is an isomorphism for every $y \in Y$.

Lean: not in Lean as stated.

**Theorem P4.5.16 (Grauert).** Let $Y$ be reduced, and suppose that $h^q$ is locally constant on $Y$. Then $R^q f_* \mathcal{F}$ is locally free, of rank $h^q(y)$ near $y$, and $\varphi^q(y)$ and $\varphi^{q-1}(y)$ are isomorphisms for every $y \in Y$.

Lean: not in Lean as stated.

**Corollary P4.5.17 (fibres with only constant functions).** Let $Y$ be reduced, $f \colon X \to Y$ projective and flat, and suppose $\dim_{\kappa(y)} H^0(X_y, \mathcal{O}_{X_y}) = 1$ for every $y \in Y$. Then $\mathcal{O}_Y \to f_* \mathcal{O}_X$ is an isomorphism, and $\varphi^0(y)$ is an isomorphism for every $y \in Y$.

Lean: not in Lean as stated.

### Proof in words

Everything is local on $Y$, so $Y = \operatorname{Spec} A$, and the Grothendieck complex of Section 5.2 is a bounded complex of finitely generated free modules $L^\bullet$ with $H^q(X_y, \mathcal{F}_y) = H^q(L^\bullet \otimes \kappa(y))$. The fibre dimension is $\operatorname{rank} L^q$ minus the ranks of the two neighbouring differentials at $y$, and the rank of a matrix can only drop under specialization, which is semicontinuity. The alternating sum of the ranks of the $L^q$ does not see the differentials at all, which is the constancy of $\chi$. For base change, pass to a minimal complex at $y$, whose differentials vanish modulo $\mathfrak{m}_y$. Then $\varphi^q(y)$ is surjective exactly when the outgoing differential $d^q$ is zero. When it is, $H^q$ is the cokernel of $d^{q-1}$, which commutes with every base change, and it is free exactly when $d^{q-1}$ is zero too. Over a reduced base, a matrix that vanishes at every point of $\operatorname{Spec} A$ is zero, which is Grauert's theorem.

### Examples

**Example P4.5.18 (three points that become collinear).** In Examples P4.5.3 and P4.5.11, over $Y = \mathbb{A}^1$, $h^0(c) = h^1(c) = 1$ for $c = 0$ and $0$ otherwise. Both jump up at the special point, as Theorem P4.5.13 allows, while $\chi = 0$ throughout. The Grothendieck complex $A^3 \to A^3$ has length one, so $H^2(X_y, \mathcal{F}_y) = 0$ for all $y$, and by Corollary P4.5.15, $\varphi^1(y)$ is an isomorphism everywhere. At $y = 0$, $R^1 f_* \mathcal{F} = (A/tA)^\sim$ is not locally free, so by part 2 of Theorem P4.5.14, $\varphi^0(0) \colon f_* \mathcal{F} \otimes \kappa(0) = 0 \to H^0(X_0, \mathcal{F}_0) = k$ is not surjective, as computed directly. On $D(t)$ the fibre cohomology vanishes, and Corollary P4.5.15 gives $f_* \mathcal{F} = R^1 f_* \mathcal{F} = 0$ there.

**Example P4.5.19 (line bundles of degree zero on an elliptic curve).** Let $k$ be algebraically closed and $E$ a smooth projective curve over $k$ with $p_a(E) = 1$ and a point $0 \in E$. On $X = E \times E$ with $f = p_2 \colon X \to Y = E$, let $\mathcal{P} = \mathcal{O}_X(\Delta - \{0\} \times E)$. It is a line bundle, flat over $Y$ since $X$ is, and its restriction to the fibre $E \times \{y\}$ is $\mathcal{P}_y = \mathcal{O}_E(y - 0)$, of degree $0$. By Corollary P4.3.17, $H^0(\mathcal{P}_y) \neq 0$ only if $y - 0$ is principal. For $y \neq 0$ it is not, since a rational function with divisor $y - 0$ would be a morphism $E \to \mathbb{P}^1$ of degree $1$, an isomorphism, while $p_a(\mathbb{P}^1) = 0$. So $h^0(y) = 1$ for $y = 0$ and $0$ otherwise. By Theorem P4.3.16, $\chi(\mathcal{P}_y) = 0$, so $h^1 = h^0$.

The closed set $\{h^0 \geq 1\} = \{0\}$ does not contain the generic point $\eta$, so $H^0(X_\eta, \mathcal{P}_\eta) = 0$ and $(f_* \mathcal{P})_\eta = 0$ by Corollary P4.5.2. Since $\mathcal{P}$ is a line bundle on the integral scheme $X$ and $f$ is dominant, $f_* \mathcal{P}$ is torsion-free, so $f_* \mathcal{P} = 0$. The fibres are curves, so $H^2(X_y, \mathcal{P}_y) = 0$, and by Corollary P4.5.15 with $q = 2$, $\varphi^1(y)$ is an isomorphism for all $y$. So $R^1 f_* \mathcal{P} \otimes \kappa(y)$ is $k$ at $y = 0$ and $0$ elsewhere: $R^1 f_* \mathcal{P}$ is a nonzero coherent sheaf supported at the origin. It is not locally free, and accordingly $\varphi^0(0) \colon 0 \to k$ is not surjective. The family $\mathcal{P}$ contains every line bundle of degree $0$ on $E$, and this computation is the first step of the Fourier-Mukai transform.

**Example P4.5.20 (a degenerating conic).** Let $Y = \mathbb{A}^1 = \operatorname{Spec} k[t]$ and $X = V_+(x y - t z^2) \subseteq \mathbb{P}^2_Y$, flat over $Y$ by Exercise 5 of Section 5.1. The fibre over $t = c \neq 0$ is a smooth conic and the fibre over $0$ is the pair of lines $x y = 0$. Every fibre is a plane conic $C$, and the sequence $0 \to \mathcal{O}(-2) \to \mathcal{O} \to \mathcal{O}_C \to 0$ with Theorem P4.2.1 gives $h^0(\mathcal{O}_C) = 1$ and $h^1(\mathcal{O}_C) = 0$. Since $Y$ is reduced, Corollary P4.5.17 and Corollary P4.5.15 give $f_* \mathcal{O}_X = \mathcal{O}_Y$ and $R^1 f_* \mathcal{O}_X = 0$, compatible with base change to every point. The same sequence twisted by $n \geq 0$ gives $h^0(\mathcal{O}_C(n)) = 2n + 1$ and $h^1 = 0$, so by Theorem P4.5.16, $f_* \mathcal{O}_X(n)$ is locally free of rank $2n + 1$.

### Proof

The statements are local on $Y$, so let $Y = \operatorname{Spec} A$ with $A$ Noetherian. By Theorem P4.4.1, $R^q f_* \mathcal{F} = H^q(X, \mathcal{F})^\sim$. Let $L^\bullet$ be a Grothendieck complex for $\mathcal{F}$ (Theorem P4.5.8). By the last part of Theorem P4.5.8 and Theorem P4.5.1, after replacing $Y$ by a basic open neighbourhood of a given point, all $L^p$ are free. For $y = \mathfrak{p}$, $\varphi^q(y)$ is the map $H^q(L^\bullet) \otimes \kappa(y) \to H^q(L^\bullet \otimes \kappa(y))$, by the naturality of Theorem P4.5.8 applied to $A \to \kappa(y)$.

*Theorem P4.5.13.* For a matrix $D$ with entries in $A$ let $\rho_D(y)$ be the rank of its image over $\kappa(y)$. The set $\{y : \rho_D(y) \geq r\}$ is the union of the sets $D(\mu)$ over the $r \times r$ minors $\mu$ of $D$, which is open. With $d^p$ the differentials of $L^\bullet$,
$$h^q(y) = \dim \ker(d^q \otimes \kappa(y)) - \dim \operatorname{im}(d^{q-1} \otimes \kappa(y)) = \operatorname{rank} L^q - \rho_{d^q}(y) - \rho_{d^{q-1}}(y).$$
So $\{h^q \geq m\}$ is the complement of the set where $\rho_{d^q} + \rho_{d^{q-1}} \geq \operatorname{rank} L^q - m + 1$, which is the union over $a + b = \operatorname{rank} L^q - m + 1$ of the open sets $\{\rho_{d^q} \geq a\} \cap \{\rho_{d^{q-1}} \geq b\}$. So it is closed. Summing with signs, the ranks of the differentials cancel, and $\chi(y) = \sum_q (-1)^q \operatorname{rank} L^q$, which is constant. $\square$

*Theorem P4.5.14.* First let $A$ be local with closed point $y$, maximal ideal $\mathfrak{m}$ and residue field $\kappa$. By Lemma P4.5.9 we may take $L^\bullet$ minimal, so $H^q(L \otimes \kappa) = L^q \otimes \kappa$. The map $\varphi^q(y)$ sends the class of $z \in Z^q(L)$ to $z \bmod \mathfrak{m} L^q$, so its image is $(Z^q(L) + \mathfrak{m} L^q)/\mathfrak{m} L^q$, and $\varphi^q(y)$ is surjective if and only if $Z^q(L) + \mathfrak{m} L^q = L^q$. By Nakayama's lemma (Theorem P1.1.25) this happens if and only if $Z^q(L) = L^q$, that is,
$$\varphi^q(y) \text{ is surjective} \iff d^q = 0. \tag{1}$$
If $d^q = 0$, then $H^q(L \otimes M) = \operatorname{coker}(d^{q-1} \otimes M) = \operatorname{coker}(d^{q-1}) \otimes M = H^q(L) \otimes M$ for every module $M$, since tensor products are right exact. For $M = \kappa$ this says that $\varphi^q(y)$ is an isomorphism.

Now suppose $d^q = 0$, so $H^q(L) = \operatorname{coker} d^{q-1}$. If $d^{q-1} = 0$, then $H^q(L) = L^q$ is free. Conversely, if $H^q(L)$ is free, its rank is $\dim H^q(L) \otimes \kappa = \dim L^q \otimes \kappa = \operatorname{rank} L^q$, since $d^{q-1} \otimes \kappa = 0$. Then $L^q \to H^q(L)$ is a surjection of free modules of the same finite rank, hence an isomorphism, and $d^{q-1} = 0$. Together with (1) for $q - 1$:
$$\text{if } d^q = 0, \text{ then } \varphi^{q-1}(y) \text{ is surjective} \iff d^{q-1} = 0 \iff H^q(L) \text{ is free}. \tag{2}$$

For general $A$ and $y = \mathfrak{p}$, the stalk $(R^q f_* \mathcal{F})_y = H^q(L) \otimes A_\mathfrak{p}$ is computed by $L^\bullet \otimes A_\mathfrak{p}$, a Grothendieck complex over $A_\mathfrak{p}$ by Theorem P4.5.1, and $\varphi^q(y)$ is the same map for $A$ and for $A_\mathfrak{p}$. So (1) and (2) apply over $A_\mathfrak{p}$. For part 1, if $\varphi^q(y)$ is surjective, it is an isomorphism. The splitting of Lemma P4.5.9 over $A_\mathfrak{p}$ uses finitely many changes of basis, whose matrices and inverses have entries in $A_\mathfrak{p}$, so they are defined over $A_s$ for some $s \notin \mathfrak{p}$. Over $A_s$ the complex $L^\bullet$ is then the direct sum of complexes $A_s \xrightarrow{1} A_s$ and a complex $L'^\bullet$ of free modules whose $q$-th differential is zero. For every $A_s$-module $M$, $H^q(L \otimes M) = H^q(L' \otimes M) = H^q(L') \otimes M$ as above, and for $M = \kappa(y')$ with $y' \in D(s)$ this says that $\varphi^q(y')$ is an isomorphism. For part 2, by (2) $\varphi^{q-1}(y)$ is surjective if and only if the stalk $(R^q f_* \mathcal{F})_y$ is free. A coherent sheaf whose stalk at $y$ is free is free on a neighbourhood of $y$, by the argument at the end of the proof of Theorem P4.5.8, and conversely. $\square$

*Corollary P4.5.15.* The target of $\varphi^q(y)$ is $0$, so $\varphi^q(y)$ is surjective, hence an isomorphism by Theorem P4.5.14, and $R^q f_* \mathcal{F} \otimes \kappa(y) = 0$. The stalk $(R^q f_* \mathcal{F})_y$ is a finitely generated $\mathcal{O}_{Y, y}$-module by Theorem P4.4.8, so it is $0$ by Nakayama's lemma. So $R^q f_* \mathcal{F} = 0$, which is locally free, and part 2 of Theorem P4.5.14 makes $\varphi^{q-1}(y)$ surjective, hence an isomorphism by part 1. $\square$

*Theorem P4.5.16.* Fix $y = \mathfrak{p}$ and pass to $A_\mathfrak{p}$, which is local and reduced, with a minimal Grothendieck complex $L^\bullet$, so $\operatorname{rank} L^q = h^q(y)$ by Lemma P4.5.9. Every prime $\mathfrak{p}' \subseteq \mathfrak{p}$ of $A$ is a generization of $y$, so it lies in every open neighbourhood of $y$, and $h^q(\mathfrak{p}') = h^q(y)$. The formula in the proof of Theorem P4.5.13 then gives $\rho_{d^q}(\mathfrak{p}') = \rho_{d^{q-1}}(\mathfrak{p}') = 0$. So every entry of $d^q$ and of $d^{q-1}$ lies in every prime of $A_\mathfrak{p}$, hence in its nilradical, which is $0$. So $d^q = d^{q-1} = 0$, and $(R^q f_* \mathcal{F})_y = H^q(L) = L^q$ is free of rank $h^q(y)$, hence $R^q f_* \mathcal{F}$ is locally free near $y$. By (1) and (2) in the proof of Theorem P4.5.14, $\varphi^q(y)$ and $\varphi^{q-1}(y)$ are surjective, hence isomorphisms. $\square$

*Corollary P4.5.17.* With $\mathcal{F} = \mathcal{O}_X$, which is flat over $Y$, Theorem P4.5.16 for $q = 0$ makes $f_* \mathcal{O}_X$ a line bundle with $\varphi^0(y) \colon f_* \mathcal{O}_X \otimes \kappa(y) \to H^0(X_y, \mathcal{O}_{X_y})$ an isomorphism. The composite $\kappa(y) = \mathcal{O}_Y \otimes \kappa(y) \to f_* \mathcal{O}_X \otimes \kappa(y) \to H^0(X_y, \mathcal{O}_{X_y})$ sends $1$ to $1 \neq 0$, so $\mathcal{O}_Y \otimes \kappa(y) \to f_* \mathcal{O}_X \otimes \kappa(y)$ is a nonzero map of one-dimensional spaces, an isomorphism. By Nakayama's lemma $\mathcal{O}_{Y, y} \to (f_* \mathcal{O}_X)_y$ is surjective, and a surjection of free modules of rank one is an isomorphism. $\square$

### Exercises

1. (A) In Example P4.5.18, describe the sets $\{h^q \geq m\}$ for all $q$ and $m$, and check that they are closed.
2. (A) Let $Y$ be connected and Noetherian, $X \subseteq \mathbb{P}^n_Y$ closed, and $\mathcal{F}$ coherent on $X$ and flat over $Y$. Apply Theorem P4.5.13 to $\mathcal{F}(m)$ for all $m$ to show that the Hilbert polynomial of $\mathcal{F}_y$ is independent of $y$, and compare with Theorem P3.13.16.
3. (A) Let $f \colon X \to Y$ be projective and flat, with $Y$ Noetherian, and suppose $H^1(X_y, \mathcal{O}_{X_y}) = 0$ for every $y$. Show that $R^1 f_* \mathcal{O}_X = 0$ and that $\varphi^0(y) \colon f_* \mathcal{O}_X \otimes \kappa(y) \to H^0(X_y, \mathcal{O}_{X_y})$ is an isomorphism for every $y$.
4. (B) Base change Example P4.5.11 to $A' = k[t]/(t^2)$. Show that $h^0$ is constant on $\operatorname{Spec} A'$, which has one point, but that $H^0(X_{A'}, \mathcal{F}_{A'}) \cong k$ is not a free $A'$-module. So Theorem P4.5.16 needs $Y$ reduced.
5. (B) Let $f$ and $\mathcal{F}$ be as in this section, and suppose $R^q f_* \mathcal{F} = 0$ for all $q \geq 1$. Show by descending induction on $q$, starting from $q = n + 1$ and using Theorem P4.5.14, that $\varphi^q(y)$ is an isomorphism for all $q$ and $y$, and deduce that $f_* \mathcal{F}$ is locally free.
6. (C) On $\mathbb{P}^1_k$, $\operatorname{Ext}^1(\mathcal{O}(1), \mathcal{O}(-1)) \cong H^1(\mathbb{P}^1, \mathcal{O}(-2)) \cong k$. Let $\mathcal{E}$ be a sheaf on $\mathbb{P}^1_{k[t]}$ given as an extension $0 \to \mathcal{O}(-1) \to \mathcal{E} \to \mathcal{O}(1) \to 0$ whose class restricts to $c$ times a generator over $t = c$, so that $\mathcal{E}_0 = \mathcal{O}(-1) \oplus \mathcal{O}(1)$. Granting that $\mathcal{E}_c \cong \mathcal{O} \oplus \mathcal{O}$ for $c \neq 0$, compute $h^0$ and $h^1$ of $\mathcal{E}_c(-1)$ for all $c$, compute $f_* \mathcal{E}(-1)$ and $R^1 f_* \mathcal{E}(-1)$, and check the conclusions of Theorems P4.5.13 and P4.5.14 at $c = 0$.

### Lean

Semicontinuity, the theorem on cohomology and base change and Grauert's theorem are not in Mathlib. The linear algebra they reduce to, the rank of a matrix over the points of $\operatorname{Spec} A$ and Nakayama's lemma, is available, the latter as `Submodule.eq_bot_of_le_smul_of_le_jacobson_bot`. The handbook adds no `MinimalModel` node here.

### Notes and history

Theorem P4.5.13 is Hartshorne III.12.8 and EGA III.7.7.5, Theorem P4.5.14 is Hartshorne III.12.11 and EGA III.7.7.10, and Theorem P4.5.16 is Grauert's theorem, Hartshorne III.12.9, first proved analytically by Grauert in 1960. The proofs here follow Mumford's *Abelian varieties*, Section 5, which works with the complex of Section 5.2 throughout. The literature state is theorem. In the minimal model program, Corollary P4.5.17 is how a contraction $f$ with $f_* \mathcal{O}_X = \mathcal{O}_Y$ keeps this property under base change, Corollary P4.5.15 turns vanishing on the fibres into $R^i f_* \mathcal{O}_X = 0$ in Kawamata-Viehweg type arguments, and the semicontinuity of $h^0(X_y, \mathcal{O}(m K_{X_y}))$ is the starting point of the deformation invariance of plurigenera.
