---
title: Invariance of plurigenera
nodes: []
sources: [Siu98, Siu02, Pau07, Kaw99, Laz04, Har77]
reads_with: [Laz04:11.5, Siu98:main, Har77:III.12]
requires: [P4.5, P7.10, 4.2, 4.3]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Invariance of plurigenera

### Statement

The $m$-th plurigenus of a smooth projective variety $X$ is $P_m(X) = h^0(X, \omega_X^{\otimes m})$. In a smooth projective family, upper semicontinuity says that $P_m$ can only go up under specialisation, and in general the dimension of the space of sections of a line bundle does jump. Siu's theorem says that the plurigenera do not jump. This section proves that invariance is equivalent to extension, states Siu's theorem, outlines its proof in the general type case, and shows by examples that both smoothness of the family and the canonical bundle are needed. The field is $\mathbb{C}$, or any algebraically closed field of characteristic $0$ in the proved statements.

**Proposition 5.5.19 (invariance is extension).** Let $\pi \colon X \to T$ be a smooth projective morphism from a smooth variety onto a smooth connected affine curve, and $m \geq 1$. The following are equivalent:

1. for every $t \in T$ the restriction map $H^0(X, \omega_X^{\otimes m}) \to H^0(X_t, \omega_{X_t}^{\otimes m})$ is surjective;
2. $P_m(X_t)$ is independent of $t \in T$.

Lean: not yet in Lean.

**Theorem 5.5.20 (invariance of plurigenera, black box).** Let $\pi \colon X \to T$ be a smooth projective morphism of complex varieties with $T$ connected. Then $P_m(X_t)$ is independent of $t \in T$ for every $m \geq 1$. This is due to Siu for fibres of general type (Siu98) and in general (Siu02), with a simplified proof by Păun (Pau07).

Lean: not yet in Lean.

**Remark 5.5.21 (an outline of the proof in the general type case).** This is an outline, following Laz04, Section 11.5. It is enough to treat a family over a smooth affine curve $T$ with a fibre $X_0$, since any two points of a connected $T$ are joined by a chain of curves. By Proposition 5.5.19 it is enough to extend sections from $X_0$. The key step is the inclusion of asymptotic multiplier ideals
$$\mathcal{J}(X_0, \| m K_{X_0} \|) \subseteq \mathcal{J}(X, \| m K_X \|) \cdot \mathcal{O}_{X_0} \quad \text{for all } m \geq 1,$$
on a projective compactification of $\pi$, proved by the induction on $m$ of the outline of Theorem 5.5.13, with the extension theorem 5.5.11 at each step and Corollary 5.5.6 to start it. Granting the inclusion, let $s \in H^0(X_0, m K_{X_0})$. By part 1 of Proposition 5.5.4 applied on $X_0$, $s$ is a section of $\mathcal{O}_{X_0}(m K_{X_0}) \otimes \mathcal{J}(X_0, \| m K_{X_0} \|)$, and since $X_0$ is of general type the twist needed to apply Theorem 5.5.11 with $L = (m - 1) K_X$ and $D$ a root of a general divisor of $|p (m - 1) K_X|$ can be absorbed, so $s$ extends. Without general type the absorption fails, and Siu02 uses $L^2$ methods instead.

The inclusion of asymptotic ideals is the multiplier ideal form of a restriction theorem: by Theorem 5.4.4 the opposite inclusion $\mathcal{J}(X_0, D|_{X_0}) \subseteq \mathcal{J}(X, D) \cdot \mathcal{O}_{X_0}$ holds for one divisor; the point is that the base ideals of $|m K_{X_0}|$ can be smaller than the restrictions of those of $|m K_X|$, and the inclusion says that asymptotically this does not happen.

### Proof in words

The direct image $\pi_* \omega_X^{\otimes m}$ is torsion free on a smooth curve, hence locally free, and its rank is the generic plurigenus. Its fibre at $t$ maps to $H^0(X_t, \omega_{X_t}^{\otimes m})$, and on an affine base every element of the fibre comes from a global section. If every restriction is surjective, the plurigenus at $t$ is at most the rank, and semicontinuity gives the opposite inequality. Conversely, constant $h^0$ makes the base change map an isomorphism, by Grauert's theorem.

### Examples

**Example 5.5.22 (sections of line bundles do jump).** Let $E$ be an elliptic curve with origin $o$, $T = E \setminus \{ p \}$ for a point $p \neq o$, which is affine, and $\mathcal{P}$ the line bundle $\mathcal{O}_{E \times T}(\Delta - \{o\} \times T)$ on $E \times T$, where $\Delta$ is the graph of the inclusion $T \subseteq E$. Then $\mathcal{P}_t = \mathcal{O}_E(t - o)$, of degree $0$, so $h^0(E, \mathcal{P}_t) = 1$ for $t = o$ and $0$ otherwise. The family $E \times T \to T$ is smooth and projective, so semicontinuity allows the jump, and only for the pluricanonical bundles does Theorem 5.5.20 forbid it. Here $\omega_{E \times T / T}$ is trivial and $P_m(E) = 1$ for every fibre.

**Example 5.5.23 (a family with a non-canonical fibre).** Let $X_0 \subset \mathbb{P}^3$ be a quintic surface with an ordinary triple point $p$ at $(0 : 0 : 0 : 1)$, given by $w^2 f_3 + w f_4 + f_5 = 0$ with $f_i \in k[x, y, z]$ homogeneous of degree $i$ and $\{f_3 = 0\} \subset \mathbb{P}^2$ a smooth cubic, and no other singular points; a general choice of $f_4$ and $f_5$ gives this. Let $\pi \colon Y \to X_0$ be the blow-up of $p$, with exceptional curve $E$, the smooth cubic $\{f_3 = 0\}$. Let $\sigma \colon \widetilde{\mathbb{P}} \to \mathbb{P}^3$ be the blow-up of $p$ with exceptional divisor $E_0 \cong \mathbb{P}^2$, so $K_{\widetilde{\mathbb{P}}} = \sigma^* K_{\mathbb{P}^3} + 2E_0$ and $Y = \sigma^* X_0 - 3E_0$. Adjunction gives
$$K_Y = (K_{\widetilde{\mathbb{P}}} + Y)|_Y = \pi^*(K_{\mathbb{P}^3} + X_0)|_{X_0} - E_0|_Y = \pi^* \mathcal{O}_{X_0}(1) - E,$$
so the discrepancy of $E$ is $-1$: the singularity is log canonical, a simple elliptic singularity, and not canonical. The canonical sections of $Y$ are the restrictions of the planes through $p$, so $p_g(Y) = 3$, while a smooth quintic $X_t$ has $p_g(X_t) = h^0(\mathbb{P}^3, \mathcal{O}(1)) = 4$. In the family of quintics $X_t = \{ w^2 f_3 + w f_4 + f_5 + t g = 0 \}$ with $g$ a general quintic, the geometric genus jumps from $4$ to $3$ at $t = 0$. The total space is singular and the fibre $X_0$ is not canonical, so neither Theorem 5.5.20 nor Theorem 5.5.14 applies.

**Example 5.5.24 (a canonical fibre).** Let instead $X_0$ be a quintic surface with one ordinary double point $p$. The blow-up $Y \to X_0$ of $p$ has exceptional curve a $(-2)$-curve and $K_Y = \pi^* K_{X_0}$, since the discrepancy of an $A_1$ point is $0$ (Volume 4, Chapter 3). The canonical sections of $Y$ are the pullbacks of all of $H^0(X_0, \mathcal{O}(1))$, so $p_g(Y) = 4 = p_g(X_t)$, as Theorem 5.5.14 predicts: $X_0$ has canonical singularities and is of general type.

### Proof

*Proof of Proposition 5.5.19.* Let $\mathcal{F} = \omega_X^{\otimes m}$, a line bundle on $X$, flat over $T$ because $\pi$ is flat. Since $X_t = \pi^{-1}(t)$ is the pullback of the Cartier divisor $t$ on $T$, its normal bundle $\mathcal{O}_X(X_t)|_{X_t} = \pi^* (\mathcal{O}_T(t)|_t)$ is trivial, and adjunction gives $\omega_X|_{X_t} = \omega_{X_t}$. So $\mathcal{F}|_{X_t} = \omega_{X_t}^{\otimes m}$, and $h^0(t) = P_m(X_t)$ in the notation of Section P4.5. The sheaf $\pi_* \mathcal{F}$ is coherent and torsion free, since a local section killed by a nonzero function on $T$ vanishes on a dense open subset of the integral scheme $X$. On the smooth curve $T$ it is locally free, of some rank $r$. Since $T$ is affine, $H^0(X, \mathcal{F}) = H^0(T, \pi_* \mathcal{F})$ generates $\pi_* \mathcal{F}$, and the restriction map of part 1 factors as
$$H^0(T, \pi_* \mathcal{F}) \twoheadrightarrow \pi_* \mathcal{F} \otimes k(t) \xrightarrow{\varphi^0(t)} H^0(X_t, \mathcal{F}_t).$$
Let $U \subseteq T$ be the dense open set on which $h^0$ takes its minimal value $h$, which exists by Theorem P4.5.13. By Theorem P4.5.16 on $U$, $\pi_* \mathcal{F}|_U$ is locally free of rank $h$, so $r = h$.

Assume part 1. Then $\varphi^0(t)$ is surjective for every $t$, so $P_m(X_t) \leq \dim \pi_* \mathcal{F} \otimes k(t) = r = h$, and $P_m(X_t) \geq h$ by the choice of $h$. So $P_m(X_t) = h$ for every $t$.

Assume part 2. Then $h^0$ is constant on the reduced scheme $T$, and Theorem P4.5.16 says $\varphi^0(t)$ is an isomorphism for every $t$. With the surjection from global sections, the restriction map is surjective. $\square$

### Exercises

1. (A) Show that in Example 5.5.22 the direct image of $\mathcal{P}$ is zero, and explain why this is consistent with Proposition 5.5.19.
2. (A) Let $\pi \colon X \to T$ be a smooth projective family of curves. Show that $P_m(X_t)$ is constant by Riemann-Roch alone, using that the genus is constant in a smooth projective family over a connected base.
3. (B) Let $X_0$ be a quintic surface with an ordinary triple point as in Example 5.5.23. Show that $K_Y^2 = 2$ and $\chi(\mathcal{O}_Y) = 4$, and compare with $K^2 = 5$ and $\chi = 5$ for a smooth quintic.
4. (B) Show that in Example 5.5.23, $P_2(Y) < P_2(X_t)$ for $t \neq 0$. Hint: $2K_Y = \pi^* \mathcal{O}(2) - 2E$, and count the quadrics with a double point at $p$ modulo the equation.
5. (B) Let $\pi \colon X \to T$ be a smooth projective morphism over a smooth affine curve and $L$ a line bundle on $X$ with $h^0(X_t, L_t)$ constant. Show that every section of $L_t$ extends to $X$, and that this fails for $X = C \times \mathbb{P}^1 \to T = \mathbb{P}^1$ and $L = p_2^* \mathcal{O}(-1)$.
6. (C) Use Theorem 5.5.20 to show that the Kodaira dimension is constant in a smooth projective family over a connected base, and that being of general type is an open and closed condition.

### Lean

None of the statements of this section is in Lean. Mathlib has the sheaf cohomology needed to state Proposition 5.5.19 only in part.

### Notes and history

Iitaka asked whether plurigenera are deformation invariant, and for surfaces the answer follows from the Enriques-Kodaira classification. Siu's proof for general type (Siu98) uses the Ohsawa-Takegoshi extension theorem and an induction on twisted pluricanonical sections, and was made algebraic by Kawamata (Kaw99) and, in Laz04, Section 11.5, with asymptotic multiplier ideals. Siu's general case (Siu02) and Păun's proof (Pau07) are analytic; an algebraic proof of Theorem 5.5.20 in general is not known. In positive characteristic the plurigenera of smooth families can jump, by examples of Katsura and Ueno for elliptic surfaces, and Chapter 6 explains why the vanishing theorems behind the proof fail.
