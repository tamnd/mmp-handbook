---
title: Running the program over a base and relative minimal models
nodes: []
sources: [KM98, Mat02, Bea96, Rei97]
reads_with: [KM98:ch3, Mat02:ch1, Bea96:ch5]
requires: [P3.11, P4.6, P5.2, P5.5, P5.6, P5.7, P5.8, P5.9, P5.10, P5.11, P5.12]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Running the program over a base and relative minimal models

### Statement

As in Section 1, $S$ is a smooth projective surface over an algebraically closed field $k$ and $f \colon S \to Z$ is a morphism to a projective variety, with Stein factorization $f = g \circ p$, $p \colon S \to Y$.

**Definition 2.1.16 (runs over a base and relative minimal models).** A *run of the minimal model program over $Z$* starting from $f$ is a sequence of smooth projective surfaces with morphisms $f_i \colon S_i \to Z$, $$S = S_0 \xrightarrow{\ \varphi_1\ } S_1 \xrightarrow{\ \varphi_2\ } \cdots \xrightarrow{\ \varphi_N\ } S_N,$$ with $f_0 = f$, in which each $\varphi_i$ is the contraction over $Z$ of a $K_{S_{i-1}}$-negative extremal ray of $\overline{NE}(S_{i-1}/Z)$ of the divisorial case 1 of Theorem 2.1.6, so that $f_{i-1} = f_i \circ \varphi_i$, and the last surface satisfies one of the following: $K_{S_N}$ is $f_N$-nef, and the run *ends at the relative minimal model* $S_N$ over $Z$; or $\overline{NE}(S_N/Z)$ has a $K$-negative extremal ray of case 2 or 3 of Theorem 2.1.6, the run is completed by its contraction, and it *ends at the Mori fibre space* $S_N \to T$ over $Z$. A *relative minimal model* of $f$ is a smooth projective surface $S'$ with a birational morphism $\psi \colon S \to S'$ and a morphism $f' \colon S' \to Z$ with $f = f' \circ \psi$ and $K_{S'}$ $f'$-nef.

**Theorem 2.1.17 (the relative minimal model program for surfaces).** Let $f \colon S \to Z$ be as above.

1. A run over $Z$ exists, and every sequence of divisorial contractions of $K$-negative relative extremal rays can be continued to a run. In every run, $\rho(S_i) = \rho(S) - i$, $\rho(S_i / Z) = \rho(S/Z) - i$, $K_{S_i}^2 = K_S^2 + i$, and $N \leq \rho(S/Z)$.
2. If $\dim f(S) = 2$, every run ends at a relative minimal model.
3. Let $\dim f(S) = 1$, so that $p \colon S \to B$ is a fibration with fibre class $F$. If $K_S \cdot F \geq 0$, every run ends at a relative minimal model. If $K_S \cdot F < 0$, then $K_S \cdot F = -2$, every run ends at a Mori fibre space $S_N \to B$ over $Z$ which is a $\mathbb{P}^1$-fibration in the sense of Definition 2.1.10, $\rho(S_N) = 2$, and $N = \rho(S) - 2$.
4. If $f(S)$ is a point, a run over $Z$ is a run in the sense of Definition P5.12.20, and Theorem P5.12.21 and Corollary P5.12.23 apply.

Lean: not yet in Lean.

**Theorem 2.1.18 (uniqueness of relative minimal models).** For $i = 1, 2$ let $f_i \colon S_i \to Z$ be a morphism from a smooth projective surface with $K_{S_i}$ $f_i$-nef, and let $\varphi \colon S_1 \dashrightarrow S_2$ be a birational map with $f_2 \circ \varphi = f_1$. Then $\varphi$ is an isomorphism. In particular, all runs over $Z$ starting from $f$ that end at a relative minimal model end at the same surface, up to a unique isomorphism over $Z$ compatible with the maps from $S$, and this surface is the only relative minimal model of $f$.

Lean: not yet in Lean.

**Proposition 2.1.19 (surfaces with $\kappa \geq 0$).** Let $\kappa(S) \geq 0$ and $f \colon S \to Z$ be as above.

1. No run over $Z$ ends at a Mori fibre space. So every run ends at the relative minimal model $S_Z$ of $f$, which is unique by Theorem 2.1.18.
2. Every $(-1)$-curve on $S_Z$ is horizontal for $f_Z$. If $\dim f(S) = 1$ and the curve $B$ of the Stein factorization has genus at least $1$, then $S_Z$ has no $(-1)$-curve, and $S_Z$ is the minimal model $S_0$ of $S$.
3. Let $S \to S_0$ be the minimal model of Corollary P5.11.19. There is a unique morphism $S_Z \to S_0$ compatible with the maps from $S$, and it is a composite of point blow-ups.

Lean: not yet in Lean.

### Proof in words

A run over $Z$ only ever contracts $(-1)$-curves in fibres of $f$, and each contraction lowers the relative Picard number by one, so the run stops. The way it stops depends on the dimension of the image. Over a surface there is no Mori fibre space, since the fibres of $f$ are points or curves of negative definite configurations. Over a curve the number $K \cdot F$ does not change along the run, because the contracted curves lie in fibres, and it is $-2$ on a $\mathbb{P}^1$-fibration and nonnegative when $K$ is relatively nef; so it decides the outcome in advance.

Uniqueness is the usual argument for minimal models, carried out over $Z$. Resolve a birational map between two relative minimal models by blow-ups on both sides with the fewest possible blow-ups. The last curve $E$ blown up on one side is a $(-1)$-curve. If the other side also contracts it, the resolution was not minimal. If not, it maps to a curve $C$ in a fibre over $Z$, and the formula $K_W = \pi_2^* K_{S_2} + Z_2$ gives $-1 = K_W \cdot E \geq K_{S_2} \cdot C \geq 0$. For a surface with $\kappa \geq 0$ there is no Mori fibre space in the birational class, so the relative program ends at a unique relative minimal model, which sits between $S$ and its absolute minimal model.

### Examples

**Example 2.1.20 (the quintic surface blown up in a point).** Let $S_0 \subseteq \mathbb{P}^3$ be a smooth quintic surface with plane section $H$. By Example P5.11.11, $K_{S_0} = H$ is very ample, $K_{S_0}^2 = 5$, $\kappa(S_0) = 2$, $p_g = 4$ and $P_2(S_0) = 10$. Let $\pi \colon S = \operatorname{Bl}_x S_0 \to S_0$ be the blow-up of a point, with exceptional curve $E$. Then $S$ is a surface of general type with a $(-1)$-curve.

*Canonical class and $(-1)$-curves.* By part 3 of Corollary P5.7.5, $K_S = \pi^* H + E$ and $K_S^2 = 4$. Let $C \neq E$ be an integral curve. Then $\pi(C)$ is a curve, $E \cdot C \geq 0$, and $K_S \cdot C = H \cdot \pi(C) + E \cdot C \geq 1$ by part 3 of Lemma P5.11.15, as $H$ is ample. So $E$ is the only integral curve with $K_S \cdot C < 0$, and the only $(-1)$-curve of $S$.

*Cone.* By Theorem P5.12.14, $\overline{NE}(S) = \overline{NE}(S)_{K \geq 0} + \mathbb{R}_{\geq 0}[E]$, with exactly one $K$-negative extremal ray. The absolute run contracts $E$ and ends at the nef model $S_0$ after one step.

*Canonical ring and Zariski decomposition.* The divisor $K_S$ is effective, as $p_g(S) = p_g(S_0) = 4$ by Theorem P5.11.6, and its Zariski decomposition (Theorem P5.8.24) is $P = \pi^* H$, $N = E$: the divisor $\pi^* H$ is nef, $\pi^* H \cdot E = 0$, and $E^2 = -1 < 0$. By Corollary P5.8.26, every member of $|mK_S|$ contains $mE$ and $H^0(S, mK_S) = H^0(S, m \pi^* H) = H^0(S_0, mH)$ for $m \geq 1$, so $|mK_S| = mE + |m \pi^* H|$. In particular $|2K_S| = 2E + |2 \pi^* H|$ and $P_2(S) = 10$. Twisting $0 \to \mathcal{O}_{\mathbb{P}^3}(-5) \to \mathcal{O}_{\mathbb{P}^3} \to \mathcal{O}_{S_0} \to 0$ by $\mathcal{O}(m)$ shows that $H^0(\mathbb{P}^3, \mathcal{O}(m)) \to H^0(S_0, \mathcal{O}(m))$ is surjective, since $H^1(\mathbb{P}^3, \mathcal{O}(m - 5)) = 0$. So the canonical ring $R(S, K_S) = \bigoplus_{m \geq 0} H^0(S, mK_S)$ is the homogeneous coordinate ring $k[x_0, x_1, x_2, x_3]/(Q)$ of $S_0$, with $Q$ the equation, and its $\operatorname{Proj}$ is the minimal model $S_0$. The fixed part $mE$ of $|mK_S|$ is the $(-1)$-curve that the program contracts.

*Relative runs.* Over $Z = \mathbb{P}^3$ with $f = \iota \circ \pi$, where $\iota$ is the inclusion, the Stein factorization is $p = \pi$, $Y = S_0$, $g = \iota$, and $NE(S/Z) = \mathbb{R}_{\geq 0}[E]$ by part 2 of Proposition 2.1.4. The run over $\mathbb{P}^3$ contracts $E$ and ends at $S_0 \to \mathbb{P}^3$, which contracts no curve. The same holds over $Z = S_0$. Over $Z = S$ with $f = \mathrm{id}$, no curve is contracted, $K_S$ is $f$-nef, and $S$ is its own relative minimal model, although it is not minimal. Over a point the run is the absolute one. So the relative minimal model depends on $Z$, and Theorem 2.1.18 asserts uniqueness only for a fixed $Z$.

**Example 2.1.21 (the conic bundle on a cubic surface).** Let $S = X_6$ be the blow-up of $\mathbb{P}^2$ at six points $P_1, \dots, P_6$ in general position, with the notation of Theorem P5.10.5: $E_i$ are the exceptional curves, $F_{ij} = \ell - E_i - E_j$ and $G_j = 2\ell - \sum_{k \neq j} E_k$. Let $p \colon S \to \mathbb{P}^1$ be the conic bundle of Example P5.10.8, given by the pencil $|Q|$ with $Q = \ell - E_6$, the strict transforms of the lines through $P_6$. Then $Q^2 = 0$, $K \cdot Q = -2$, and $p$ has $p_* \mathcal{O}_S = \mathcal{O}_{\mathbb{P}^1}$, since its general fibre, the strict transform of a general line through $P_6$, is integral.

*Singular fibres and the relative cone.* The line through $P_6$ and $P_j$ gives the fibre $F_{j6} + E_j$ for $j = 1, \dots, 5$, two $(-1)$-curves meeting once, and every other fibre is the strict transform of a line through $P_6$ and no other $P_i$, an integral curve isomorphic to $\mathbb{P}^1$. By part 3 of Proposition 2.1.4, $\rho(S/\mathbb{P}^1) = 1 + 5 = 6 = \rho(S) - 1$, and the extremal rays of $NE(S/\mathbb{P}^1)$ are the ten rays spanned by $E_1, \dots, E_5, F_{16}, \dots, F_{56}$, all $K$-negative. The numbers check against Theorem 2.1.17: $K_S^2 = 3$ and $K \cdot Q = -2$, so every run over $\mathbb{P}^1$ ends at a $\mathbb{P}^1$-fibration with $K^2 = 8$ after $N = \rho(S) - 2 = 5$ steps, and $3 + 5 = 8$.

*The thirty-two relative minimal models.* A run contracts one component in each singular fibre: after one of $E_j, F_{j6}$ is contracted, the image of the other is the whole fibre and is no longer a $(-1)$-curve. For a subset $J \subseteq \{1, \dots, 5\}$, let $S \to X_J$ contract $F_{j6}$ for $j \in J$ and $E_j$ for $j \notin J$. These are the $2^5 = 32$ outcomes, each a $\mathbb{P}^1$-fibration over $\mathbb{P}^1$, hence a Hirzebruch surface $F_{m(J)}$ by Proposition P5.9.9. Let $k = |J|$. The sections of $p$ among the $27$ lines are $E_6$, the ten $F_{ij}$ with $i < j \leq 5$ and the five $G_j$ with $j \leq 5$, sixteen in all; $G_6$ has $G_6 \cdot Q = 2$. A section $\sigma$ meets exactly one component of each singular fibre, transversally, The contracted curves are disjoint. Contracting a $(-1)$-curve that meets $\sigma$ once raises the square of $\sigma$ by $1$, by part 4 of Proposition P5.6.4 with $m = 1$, and contracting one disjoint from $\sigma$ leaves it unchanged, by Lemma P5.12.22. So the image of a section $\sigma$ among the lines in $X_J$ has square $-1$ plus the number of contracted curves that $\sigma$ meets. From the intersection numbers of Theorem P5.10.5, the image squares are as follows.

| section | condition | contracted curves met | image square |
| --- | --- | --- | --- |
| $E_6$ |  | $k$ | $k - 1$ |
| $F_{ij}$ | $i, j \in J$ | $k - 2$ | $k - 3$ |
| $F_{ij}$ | exactly one of $i, j$ in $J$ | $k$ | $k - 1$ |
| $F_{ij}$ | $i, j \notin J$ | $k + 2$ | $k + 1$ |
| $G_j$ | $j \in J$ | $6 - k$ | $5 - k$ |
| $G_j$ | $j \notin J$ | $4 - k$ | $3 - k$ |

For instance $G_j$ meets $E_m$ for $m \neq j$, $m \leq 5$, and $F_{j6}$, but not $E_j$ or $F_{m6}$ with $m \neq j$. On $F_m$, a section has square $-m$ or at least $m$, by Proposition P5.9.8 and part 1 of Corollary 2.1.12. So a section of square $0$ forces $m = 0$, and a section of square $-1$ forces $m = 1$. For $k = 0, 1, 2, 3, 4, 5$, the sections $E_6$, $E_6$, $F_{ij}$ with $i, j \in J$, $F_{ij}$ with $i, j \in J$, $G_j$ with $j \notin J$, and $G_j$ with $j \in J$ have image squares $-1, 0, -1, 0, -1, 0$. So $X_J \cong F_0$ when $k$ is odd and $X_J \cong F_1$ when $k$ is even, sixteen choices each. For $J = \emptyset$ the run contracts $E_1, \dots, E_5$ and ends at $\operatorname{Bl}_{P_6} \mathbb{P}^2 \cong F_1$, as Theorem P3.11.26 says. For $J = \{j\}$ the image of $E_6$ is a section of square $0$ of $F_0$. Changing the choice in one fibre $j$ replaces $X_J$ by $X_{J \triangle \{j\}}$: both are obtained from the surface in which only the fibre over $P_j$ is left reducible, by contracting one of its two components, so they differ by the elementary transformation of Definition 2.1.10 at the image of the contracted curve, and the parity of $k$ changes, as Example 2.1.15 predicts. The outcome over $\mathbb{P}^1$ is far from unique, in contrast with Theorem 2.1.18, and the thirty-two outcomes are linked by elementary transformations, as Theorem 2.1.13 asserts.

### Proof

*Proof of Theorem 2.1.17.* (1) Let $S_i \to Z$ be reached by a sequence of divisorial contractions over $Z$. If $K_{S_i}$ is $f_i$-nef, the sequence is a run ending at a relative minimal model. Otherwise $\overline{NE}(S_i/Z)$ has a $K$-negative extremal ray $R$ by part 3 of Theorem 2.1.5, and its contraction exists by Theorem 2.1.6. If $R$ is in case 2 or 3, its contraction completes a run ending at a Mori fibre space. If $R$ is in case 1, its contraction $\varphi_{i+1} \colon S_i \to S_{i+1}$ is the contraction of an $f_i$-contracted $(-1)$-curve, with $\rho(S_{i+1}) = \rho(S_i) - 1$, $\rho(S_{i+1}/Z) = \rho(S_i/Z) - 1$ and $K_{S_{i+1}}^2 = K_{S_i}^2 + 1$ by Theorem 2.1.6 and part 3 of Corollary P5.7.5. Since $\rho(S_i/Z) \geq 0$, this happens at most $\rho(S/Z)$ times, so the sequence ends after $N \leq \rho(S/Z)$ divisorial steps.

Along a run, $\dim f_i(S_i) = \dim f(S)$, since $\varphi_1 \circ \dots \circ \varphi_i$ is surjective and $f = f_i \circ \varphi_i \circ \dots \circ \varphi_1$. If $\dim f(S) = 1$, the Stein factorization of $f_i$ is $f_i = g \circ p_i$ with the same curve $B$: by part 1 of Corollary P5.7.5, $p_{i-1} = p_i \circ \varphi_i$ for a unique $p_i \colon S_i \to B$, because $\varphi_i$ contracts a curve in a fibre of $p_{i-1}$, and $p_{i*} \mathcal{O}_{S_i} = p_{i*} \varphi_{i*} \mathcal{O}_{S_{i-1}} = \mathcal{O}_B$, as $\varphi_{i*} \mathcal{O}_{S_{i-1}} = \mathcal{O}_{S_i}$.

(2) If $\dim f(S) = 2$, then $\dim f_i(S_i) = 2$ for every $i$, so cases 2 and 3 of Theorem 2.1.6 do not occur, and the run ends at a relative minimal model.

(3) Let $F_i$ be the fibre class of $p_i$. A fibre of $p_{i-1}$ is the pullback of a fibre of $p_i$, so $F_{i-1} = \varphi_i^* F_i$, and if $E_i$ is the curve contracted by $\varphi_i$, then $K_{S_{i-1}} \cdot F_{i-1} = (\varphi_i^* K_{S_i} + E_i) \cdot \varphi_i^* F_i = K_{S_i} \cdot F_i$ by parts 2 and 3 of Corollary P5.7.5. So $K \cdot F$ is constant along the run. Case 3 of Theorem 2.1.6 does not occur since $f_i(S_i)$ is a curve. If the run ends at a relative minimal model $S_N$, then $K_{S_N}$ is nonnegative on the components of a fibre, which are $f_N$-contracted, so $K_S \cdot F = K_{S_N} \cdot F_N \geq 0$. If the run ends at a Mori fibre space, it is case 2 of Theorem 2.1.6: $p_N \colon S_N \to B$ has all fibres $\mathbb{P}^1$, $\rho(S_N) = 2$ and $K_S \cdot F = K_{S_N} \cdot F_N = -2$, and $N = \rho(S) - \rho(S_N) = \rho(S) - 2$ by (1). Since every run ends in one of the two ways, the sign of $K_S \cdot F$ decides which, for all runs at once.

(4) If $f(S)$ is a point, every curve is $f$-contracted, $\overline{NE}(S/Z) = \overline{NE}(S)$ by part 4 of Proposition 2.1.4, and the contractions of Theorem 2.1.6 are those of Theorem P5.12.15. So the two notions of run agree. $\square$

*Proof of Theorem 2.1.18.* By Theorem P5.7.13 there are smooth projective surfaces $W$ with composites of point blow-ups $\pi_i \colon W \to S_i$ and $\pi_2 = \varphi \circ \pi_1$. Choose one with $\rho(W)$ as small as possible. The morphisms $f_1 \circ \pi_1$ and $f_2 \circ \pi_2 = f_2 \circ \varphi \circ \pi_1$ agree as rational maps from the integral scheme $W$ to the separated scheme $Z$, so they are equal; call this morphism $q$.

Suppose that $\pi_1$ is not an isomorphism, and let $E \subseteq W$ be the exceptional curve of the last blow-up in $\pi_1$, a $(-1)$-curve, with blow-down $\mu \colon W \to W'$ and $\pi_1 = \pi'_1 \circ \mu$. The curve $E$ is $q$-contracted, since $\pi_1(E)$ is a point.

If $\pi_2(E)$ is a point, Lemma P5.11.16 gives $\pi_2 = \pi'_2 \circ \mu$. By part 1 of Theorem P5.7.12, $\pi'_1$ and $\pi'_2$ are composites of point blow-ups, and $\pi'_2 = \varphi \circ \pi'_1$ since $\mu$ is surjective. As $\rho(W') = \rho(W) - 1$, this contradicts the choice of $W$.

If $C = \pi_2(E)$ is a curve, then $f_2(C) = q(E)$ is a point, so $C$ is $f_2$-contracted and $K_{S_2} \cdot C \geq 0$. By part 2 of Lemma P5.11.15, $K_W = \pi_2^* K_{S_2} + Z_2$ with $Z_2$ effective and supported on the curves contracted by $\pi_2$. The curve $E$ is not among them, so $Z_2 \cdot E \geq 0$. By part 3 of Lemma P5.11.15, $\pi_2^* K_{S_2} \cdot E = K_{S_2} \cdot C \geq 0$. So $K_W \cdot E \geq 0$, while $K_W \cdot E = -1$ for the $(-1)$-curve $E$ by part 1 of Corollary P5.5.15. This contradiction shows that $\pi_1$ is an isomorphism. The argument is symmetric in $S_1$ and $S_2$, so $\pi_2$ is an isomorphism as well, and $\varphi = \pi_2 \circ \pi_1^{-1}$ is an isomorphism.

For the second statement, let $\psi_1 \colon S \to S_1$ and $\psi_2 \colon S \to S_2$ be relative minimal models of $f$, for example the ends of two runs. Then $\varphi = \psi_2 \circ \psi_1^{-1}$ is birational with $f_2 \circ \varphi = f_1$, as both agree with $f \circ \psi_1^{-1}$ on a dense open set. So $\varphi$ is an isomorphism with $\varphi \circ \psi_1 = \psi_2$, and it is the only such isomorphism, since $\psi_1$ is surjective. $\square$

*Proof of Proposition 2.1.19.* (1) Suppose that a run ends at a Mori fibre space $S_N \to T$ over $Z$. By Theorem 2.1.6, this is a Mori fibre space in the sense of Definition P5.12.20, so $S_N$ is $\mathbb{P}^2$ or has a morphism onto a curve all of whose fibres are $\mathbb{P}^1$. In both cases $\overline{NE}(S_N)$ has a $K$-negative extremal ray of type 2 or 3 of Theorem P5.12.15, the line class of $\mathbb{P}^2$ or the fibre class, which spans $\overline{NE}(S_N)_{F = 0}$ since $F$ is nef with $F^2 = 0$ and $\rho(S_N) = 2$. So its contraction is a run on $S_N$ without divisorial steps that ends at a Mori fibre space, and $\kappa(S_N) = -\infty$ by part 1 of Corollary P5.12.23. As $S_N$ is birational to $S$, $\kappa(S) = \kappa(S_N) = -\infty$ by part 2 of Theorem P5.11.6, a contradiction. So every run ends at a relative minimal model, which is unique by Theorem 2.1.18.

(2) A $(-1)$-curve $E$ on $S_Z$ has $K_{S_Z} \cdot E = -1 < 0$, so it is not $f_Z$-contracted, as $K_{S_Z}$ is $f_Z$-nef. Let $\dim f(S) = 1$ and $p_Z \colon S_Z \to B$ the Stein factorization, as in the proof of Theorem 2.1.17. Then $p_Z(E)$ is not a point, so $p_Z$ maps $E \cong \mathbb{P}^1$ onto $B$, and $B \cong \mathbb{P}^1$ by Theorem P5.2.12. So if $g(B) \geq 1$, the surface $S_Z$ has no $(-1)$-curve, it is minimal in the sense of Definition P5.11.13, and $S \to S_Z$ is a minimal model of $S$, which is the minimal model $S_0$ by part 2 of Corollary P5.11.19.

(3) Let $\psi \colon S \to S_Z$ and $g_0 \colon S \to S_0$ be the given morphisms. The birational map $g_0 \circ \psi^{-1} \colon S_Z \dashrightarrow S_0$ is a morphism by Theorem P5.11.18, it is compatible with the maps from $S$, and it is unique with this property because $\psi$ is surjective. It is a birational morphism of smooth projective surfaces, hence a composite of point blow-ups by part 1 of Theorem P5.7.12. $\square$

### Exercises

1. (A) Let $S_0 \subseteq \mathbb{P}^3$ be a smooth quintic and $S$ its blow-up at two distinct points $x, y$, with exceptional curves $E_x, E_y$. Show that $E_x$ and $E_y$ are the only $(-1)$-curves of $S$, that $\overline{NE}(S)$ has exactly two $K$-negative extremal rays, and that the two runs over $Z = S_0$ contract them in the two possible orders and end at the same surface, as Theorem 2.1.18 requires.
2. (A) In Example 2.1.21, check the six rows of the table from the intersection numbers of the $27$ lines, and verify that exactly sixteen of the thirty-two subsets $J$ give $F_0$.
3. (B) In Example 2.1.21, show that the ten classes $E_j$, $F_{j6}$ span a subspace of $N^1(S)$ of dimension $6$, and find four independent linear relations among them. Show that $NE(S/\mathbb{P}^1)$ is not simplicial.
4. (B) Let $Y$ be a normal projective surface and $h_i \colon S_i \to Y$, $i = 1, 2$, two resolutions, birational morphisms from smooth projective surfaces, with $K_{S_i}$ $h_i$-nef. Deduce from Theorem 2.1.18 that $S_1 \cong S_2$ over $Y$, and identify the resulting surface for the quadric cone of Example 2.1.8. This surface is the minimal resolution of $Y$.
5. (B) Let $p \colon X_9 \to \mathbb{P}^1$ be the rational elliptic surface of Example 2.1.9, and $S = \operatorname{Bl}_x X_9$ for a point $x$ on a smooth fibre. Show that the run of $S$ over $\mathbb{P}^1$ has exactly one step and ends at $X_9$, that $K_S \cdot F = 0$, and that every run of $S$ over a point ends at a Mori fibre space. Conclude that relative minimality over $\mathbb{P}^1$ does not detect $\kappa(S) = -\infty$.
6. (C) Let $S_0 \subseteq \mathbb{P}^3$ be a smooth quintic, $L \subseteq \mathbb{P}^3$ a line meeting $S_0$ transversally in five points $x_1, \dots, x_5$, and $S$ the blow-up of $S_0$ at these points, with the morphism $p \colon S \to \mathbb{P}^1$ given by the pencil of planes through $L$. Show that $p$ is a fibration with $K_S \cdot F = 10$, that $K_S$ is $p$-nef, and that $S$ is the relative minimal model of $p$ although it has five $(-1)$-curves, all horizontal. Compare with part 2 of Proposition 2.1.19.

### Lean

The statements of this section are not yet in Lean. The library `mmp-lean` states the absolute surface program as `MinimalModel.SurfaceMMP` in `MinimalModel/Statements/LowDim.lean`: each smooth projective surface has a birational morphism to a surface that is minimal or a Mori fibre space. A relative version would replace nefness by the relative nefness of Definition 2.1.1 and needs the relative cone, which the library does not define.

### Notes and history

Relatively minimal models of fibred surfaces go back to Šafarevič's Tata lectures of 1966 and to Lichtenbaum's 1968 paper, which proved that a regular fibred surface whose fibres have arithmetic genus at least $1$ has a unique relatively minimal model, also over arithmetic bases; Theorem 2.1.18 and part 3 of Theorem 2.1.17 are the geometric case. For rational fibrations the relatively minimal models are the $\mathbb{P}^1$-bundles of Theorem P5.9.17 and are not unique, as Example 2.1.21 shows. In the language of the minimal model program, Theorem 2.1.17 is the relative program of Kollár and Mori, Chapter 3, in dimension $2$, where no flips occur; Matsuki, Chapter 1, and Reid's *Chapters on algebraic surfaces* run it in the same way, and Beauville, Chapter V, uses the absolute case in the proof of the classification. The literature state of the results of this section is theorem.
