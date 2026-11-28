---
title: Extension theorems
nodes: []
sources: [Siu98, Siu02, Kaw99, Tak06, HM07, Laz04]
reads_with: [Laz04:9.5, Tak06:sec4, HM07:sec5]
requires: [P7.8, P7.10, 5.4]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Extension theorems

### Statement

Let $S \subset X$ be a smooth prime divisor. An extension theorem says that certain sections of a line bundle on $S$ are restrictions of sections on $X$. The exact sequence $0 \to \mathcal{O}_X(K_X + L) \to \mathcal{O}_X(K_X + S + L) \to \mathcal{O}_S(K_S + L|_S) \to 0$ reduces the question to the vanishing of $H^1(X, \mathcal{O}_X(K_X + L))$, and Kawamata-Viehweg vanishing answers it when $L$ is nef and big. The extension theorems of Siu, Kawamata, Takayama and Hacon-McKernan extend pluricanonical sections, where no such vanishing is available, by an induction on the multiple $m$ in which multiplier ideals carry the information from one step to the next. This section proves the basic extension theorem with a multiplier ideal, and states the deeper theorems precisely, with outlines of their proofs. Throughout, $k$ has characteristic $0$, $X$ is a smooth projective variety of dimension $n$, and $S \subset X$ is a smooth prime divisor.

**Theorem 5.5.11 (extension with a multiplier ideal).** Let $L$ be a Cartier divisor and $D$ an effective $\mathbb{Q}$-divisor on $X$ with $S \not\subseteq \operatorname{Supp} D$, such that $L - D$ is nef and big. Then the image of the restriction map
$$H^0(X, \mathcal{O}_X(K_X + S + L)) \to H^0(S, \mathcal{O}_S(K_S + L|_S))$$
contains $H^0(S, \mathcal{O}_S(K_S + L|_S) \otimes \mathcal{J}(S, D|_S))$.

Lean: not yet in Lean.

**Corollary 5.5.12 (the klt case).** If in addition the pair $(S, D|_S)$ is klt, then the restriction map $H^0(X, \mathcal{O}_X(K_X + S + L)) \to H^0(S, \mathcal{O}_S(K_S + L|_S))$ is surjective.

Lean: not yet in Lean.

The following theorems are stated as black boxes, each with an outline of its proof in the Proof section. The field is $\mathbb{C}$.

**Theorem 5.5.13 (Siu's extension theorem, black box).** Let $\pi \colon X \to T$ be a smooth projective morphism from a smooth variety onto a smooth affine curve, and $X_0 = \pi^{-1}(0)$ a fibre. Then for every $m \geq 1$ the restriction map
$$H^0(X, \omega_X^{\otimes m}) \to H^0(X_0, \omega_{X_0}^{\otimes m})$$
is surjective. Siu proved this when $X_0$ is of general type (Siu98), and in general (Siu02); a shorter proof of the general case is due to Păun (Pau07).

Lean: not yet in Lean.

Since $X_0$ is a fibre over an affine curve, $\mathcal{O}_X(X_0)|_{X_0}$ is trivial and $\omega_X|_{X_0} = \omega_{X_0}$ by adjunction, so the map makes sense. The original statements are for a family over a disc in the analytic category; over an affine curve the statement is equivalent to invariance of plurigenera by Proposition 5.5.19, and so follows from Theorem 5.5.20.

**Theorem 5.5.14 (Kawamata, black box).** Let $\pi \colon X \to T$ be a flat projective morphism from a normal variety onto a smooth curve, and $0 \in T$ a point such that the fibre $X_0$ has only canonical singularities. Then there is a neighbourhood $T^\circ$ of $0$ such that $X_t$ has only canonical singularities for every $t \in T^\circ$, and if in addition $X_0$ is of general type, then $P_m(X_t) = h^0(X_t, \mathcal{O}_{X_t}(m K_{X_t}))$ is independent of $t \in T^\circ$ for every $m \geq 1$ (Kaw99, Main Theorem and its corollary).

Lean: not yet in Lean.

**Theorem 5.5.15 (Takayama, black box).** Let $X$ be smooth projective and $S \subset X$ a smooth prime divisor. Suppose that $K_X + S \sim_{\mathbb{Q}} A + D$ with $A$ an ample $\mathbb{Q}$-divisor and $D$ an effective $\mathbb{Q}$-divisor with $S \not\subseteq \operatorname{Supp} D$, such that the pair $(S, D|_S)$ is klt. Then for every $m \geq 1$ the restriction map
$$H^0(X, \mathcal{O}_X(m(K_X + S))) \to H^0(S, \mathcal{O}_S(m K_S))$$
is surjective (Tak06, Theorem 4.1).

Lean: not yet in Lean.

**Theorem 5.5.16 (Hacon-McKernan, black box).** Let $X$ be smooth projective and $\Delta = S + A + B$ a $\mathbb{Q}$-divisor with snc support, where $S$ is a smooth prime divisor, $A$ is a general ample $\mathbb{Q}$-divisor and $B$ is effective with $\lfloor B \rfloor = 0$ and $S \not\subseteq \operatorname{Supp} B$, so that $(X, \Delta)$ is plt. Let $k \geq 1$ with $k(K_X + \Delta)$ Cartier, and suppose that $S \not\subseteq \mathbf{B}(K_X + \Delta)$. Put $\Omega = (\Delta - S)|_S$,
$$F = \lim_{l \to \infty} \frac{1}{lk} \operatorname{Fix}\big(|lk(K_X + \Delta)|_S\big), \qquad \Theta = \Omega - \Omega \wedge F,$$
where $|\cdot|_S$ is the restricted linear system, $\operatorname{Fix}$ its fixed divisor, and $\wedge$ the componentwise minimum of coefficients. Then for every $m$ divisible by $k$ with $m \Theta$ integral,
$$|m(K_S + \Theta)| + m(\Omega - \Theta) \subseteq |m(K_X + \Delta)|_S.$$
(HM07, the main extension theorem of Section 5; the exact hypotheses are reproduced here as in that source, and the reader should consult it before using the statement.)

Lean: not yet in Lean.

The inclusion says that a member of $|m(K_S + \Theta)|$, plus the fixed part $m(\Omega - \Theta)$, is the restriction of a member of $|m(K_X + \Delta)|$. For $B = 0$ and $A$ small, this extends the sections of $m(K_S + A|_S)$, and it is the step in the proof of the existence of flips that passes from the restricted algebra on $S$ to the algebra on $X$ (Volume 8 and Volume 9).

### Proof in words

For Theorem 5.5.11, pass to a log resolution where $S$ and $D$ are snc, and put the fractional part of the pullback of $D$ into the boundary. The divisor $\mu^* L - \lfloor \mu^* D \rfloor$ minus its boundary is $\mu^*(L - D)$, nef and big, so Kawamata-Viehweg kills $H^1$ on the resolution and every section on the strict transform $S'$ extends. The sheaf on $S'$ pushes forward to $\mathcal{O}_S(K_S + L|_S) \otimes \mathcal{J}(S, D|_S)$, by the residue formula $K_{S'/S} = (K_{X'/X} - \Gamma)|_{S'}$ used for Theorem 5.4.4, and the sections on $X'$ push forward into sections on $X$. Siu's idea for pluricanonical forms is to apply this with $L = (m - 1)K_X + A$ and $D$ built from the sections already extended at the step before, so that the multiplier ideal on $S$ contains every section of $mK_S$ twisted by $A$; an effective global generation argument starts the induction, and letting the twist $A$ become small by taking roots gives the pure pluricanonical statement.

### Examples

**Example 5.5.17 (a product).** Let $C$ be a smooth projective curve, $X = \mathbb{P}^1 \times C$ with projections $p_1, p_2$, $S = \{0\} \times C \cong C$, and $L = p_1^* \mathcal{O}(a) + p_2^* A$ with $a \geq 1$ and $\deg A > 0$. Then $L$ is ample, and Corollary 5.5.12 with $D = 0$ applies. Directly, $K_X + S + L = p_1^* \mathcal{O}(a - 1) + p_2^*(K_C + A)$, and by the Künneth formula (Example P4.4.17 and its proof), $H^0(X, \mathcal{O}_X(K_X + S + L)) = H^0(\mathbb{P}^1, \mathcal{O}(a - 1)) \otimes H^0(C, K_C + A)$. The restriction to $S$ is evaluation at $0$ on the first factor, which is surjective since $a - 1 \geq 0$, so the map onto $H^0(C, K_C + A)$ is surjective.

**Counterexample 5.5.18 (bigness is needed).** In Example 5.5.17 take $a = 0$, so that $L = p_2^* A$ is nef and not big. Then $K_X + S + L = p_1^* \mathcal{O}(-1) + p_2^*(K_C + A)$ has no sections, since $H^0(\mathbb{P}^1, \mathcal{O}(-1)) = 0$, while $H^0(S, K_S + L|_S) = H^0(C, K_C + A) \neq 0$ for $\deg A \geq 1$. So the restriction map is not surjective, and Corollary 5.5.12 fails without bigness. The obstruction is $H^1(X, \mathcal{O}_X(K_X + L)) \supseteq H^1(\mathbb{P}^1, \mathcal{O}(-2)) \otimes H^0(C, K_C + A) \neq 0$.

### Proof

*Proof of Theorem 5.5.11.* Let $\mu \colon X' \to X$ be a log resolution of $D + S$ such that the strict transform $S'$ of $S$ is smooth and $S' + \operatorname{Exc}(\mu) + \mu^* D$ has snc support (Theorem P7.8.15). Write $\mu^* S = S' + \Gamma$ with $\Gamma$ effective and exceptional, and $\mu_S = \mu|_{S'} \colon S' \to S$, a proper birational morphism of smooth varieties. Since $S \not\subseteq \operatorname{Supp} D$, $S'$ is not a component of $\mu^* D$, and the divisor $\mu_S^*(D|_S) = (\mu^* D)|_{S'}$ has snc support on $S'$. Adjunction on $X$ and on $X'$ gives $K_S = (K_X + S)|_S$ and $K_{S'} = (K_{X'} + S')|_{S'}$, and $K_{X'} + S' = \mu^*(K_X + S) + K_{X'/X} - \Gamma$, so
$$K_{S'} = \mu_S^* K_S + (K_{X'/X} - \Gamma)|_{S'}, \qquad K_{S'/S} = (K_{X'/X} - \Gamma)|_{S'}.$$
Put $G = K_{X'} + S' + \mu^* L - \lfloor \mu^* D \rfloor$. Since restriction to $S'$ commutes with rounding down for an snc divisor not containing $S'$,
$$G|_{S'} = \mu_S^*(K_S + L|_S) + K_{S'/S} - \lfloor \mu_S^*(D|_S) \rfloor,$$
and by Lemma 5.4.2 applied to $\mu_S$,
$$(\mu_S)_* \mathcal{O}_{S'}(G|_{S'}) = \mathcal{O}_S(K_S + L|_S) \otimes \mathcal{J}(S, D|_S).$$
The exact sequence $0 \to \mathcal{O}_{X'}(G - S') \to \mathcal{O}_{X'}(G) \to \mathcal{O}_{S'}(G|_{S'}) \to 0$ has $G - S' = K_{X'} + N$ with $N = \mu^* L - \lfloor \mu^* D \rfloor$. With $\Delta' = \{\mu^* D\}$, which has snc support and coefficients in $[0, 1)$, $N - \Delta' = \mu^*(L - D)$ is nef and big, by Lemma P7.9.2. Theorem P7.8.18 gives $H^1(X', \mathcal{O}_{X'}(K_{X'} + N)) = 0$, so
$$H^0(X', \mathcal{O}_{X'}(G)) \to H^0(S', \mathcal{O}_{S'}(G|_{S'})) = H^0(S, \mathcal{O}_S(K_S + L|_S) \otimes \mathcal{J}(S, D|_S))$$
is surjective. Finally $G = \mu^*(K_X + S + L) + P$ with $P = K_{X'/X} - \Gamma - \lfloor \mu^* D \rfloor$, and the positive part of $P$ is exceptional. So $\mu_* \mathcal{O}_{X'}(P) \subseteq \mathcal{O}_X$, because a rational function on the normal variety $X$ that is regular outside a closed set of codimension $2$ is regular, and the projection formula gives $H^0(X', \mathcal{O}_{X'}(G)) \subseteq H^0(X, \mathcal{O}_X(K_X + S + L))$. On the open set $U \subseteq X$ over which $\mu$ is an isomorphism, these two inclusions and the two restriction maps to $S \cap U$ agree, and $S \cap U$ is dense in $S$ because $\mu(\operatorname{Exc}(\mu))$ has codimension at least $2$. Since a section of a torsion-free sheaf on $S$ is determined on a dense open set, every section of $\mathcal{O}_S(K_S + L|_S) \otimes \mathcal{J}(S, D|_S)$ is the restriction of a section of $\mathcal{O}_X(K_X + S + L)$. $\square$

*Proof of Corollary 5.5.12.* If $(S, D|_S)$ is klt, then $\mathcal{J}(S, D|_S) = \mathcal{O}_S$ by the klt criterion of Proposition P7.10.5 in the form for divisors, and Theorem 5.5.11 applies. $\square$

*Outline of Theorem 5.5.13 for $X_0$ of general type.* This is an outline, not a proof. Fix a very ample divisor $A$ on $X$, so positive that $A|_{X_0}$ and its adjoint bundles of Corollary 5.5.6 are globally generated, with all their sections extending to $X$ by Corollary 5.5.12. Inductively, the sections of $\mathcal{O}_{X_0}(m K_{X_0} + A|_{X_0})$ extend to $X$ for every $m$: the extended sections at step $m - 1$ define a divisor $D$ on $X$ with $\mathcal{J}(X_0, D|_{X_0})$ containing the base ideal of $|(m - 1) K_{X_0} + A|_{X_0}|$, and Theorem 5.5.11 with $S = X_0$ and $L = (m - 1) K_X + A$ adjusted by $D$ gives step $m$. The bound on the twist is the subtle point: the twist $A$ appears once at each step, not $m$ times. To remove it, apply the result to $r m K_{X_0}$ for large $r$ and take a root of the resulting divisor, which turns the induction into an inclusion of asymptotic multiplier ideals $\mathcal{J}(X_0, \| m K_{X_0} \|) \subseteq \mathcal{J}(X, \| m K_X \|) \cdot \mathcal{O}_{X_0}$. General type gives an effective divisor $E$ with $a K_{X_0} - A|_{X_0} \sim E$, which absorbs $A$; then Theorem 5.5.11 with $L = (m - 1) K_X$ and the inclusion of asymptotic ideals extend all sections of $m K_{X_0}$. The full argument is Laz04, Section 11.5, which follows Siu98 and Kaw99. The general case, Siu02 and Pau07, replaces general type by an approximation of the canonical bundle by $K + \varepsilon A$ and needs $L^2$ estimates of Ohsawa-Takegoshi type for the limit, which have no algebraic proof at present.

*Outline of Theorem 5.5.14.* This is an outline. The first statement is local near $X_0$. After passing to a projective model and an index one cover, Kawamata applies the extension argument of the previous outline on a log resolution of the pair $(X, X_0)$, with adjoint ideals in place of multiplier ideals, to show that sections of $m K_{X_0}$ on the resolution of $X_0$ extend to sections of $m(K_X + X_0)$ on a resolution of $X$. This forces the total space $X$ to have canonical singularities near $X_0$, and then a general fibre $X_t$, a general member of a free family of Cartier divisors, has canonical singularities too. The second statement is the algebraic form of Siu's argument for varieties of general type, with canonical singularities in place of smoothness: canonical singularities mean that the plurigenera are computed on a resolution, so the outline above applies to a resolution of the family.

*Outline of Theorem 5.5.15.* This is an outline. Takayama follows Siu's induction with $X_0$ replaced by $S$. The hypothesis $K_X + S \sim_{\mathbb{Q}} A + D$ plays the role of general type: it gives a fixed positive twist $A$ and a divisor $D$ whose restriction to $S$ is klt, so that $\mathcal{J}(S, \epsilon D|_S) = \mathcal{O}_S$ for $\epsilon \leq 1$, and Theorem 5.5.11 can be applied at every step with $L = (m - 1)(K_X + S) + (\text{a small multiple of } A) + (\text{a root of the divisor of the extended sections})$. The case $X \to T$ smooth is $S = X_0$, and Takayama's theorem gives the general type case of Theorem 5.5.13 and the boundedness of pluricanonical maps of Hacon-McKernan (HM06) and Takayama.

*Outline of Theorem 5.5.16.* This is an outline. Hacon and McKernan run the same induction for the log canonical divisor $K_X + \Delta$ with the boundary $A + B$. The divisor $F$ measures the part of the base locus of the restricted systems that is unavoidable, and $\Theta$ removes from $\Omega$ exactly that part, so that the pair $(S, \Theta)$ sees only the boundary components that are not fixed. The ample part $A$ provides the positivity that $L - D$ needs in Theorem 5.5.11, and the plt hypothesis makes the restricted pair klt. The output is the inclusion of linear systems, which is the input for the finite generation of the restricted algebra in the proof of the existence of pl-flips.

### Exercises

1. (A) Deduce from Theorem 5.5.11 that, if $L$ is nef and big, then $H^0(X, \mathcal{O}_X(K_X + S + L)) \to H^0(S, \mathcal{O}_S(K_S + L|_S))$ is surjective, and prove this directly from Kawamata-Viehweg vanishing.
2. (A) Let $X = \mathbb{P}^2$, $S$ a line and $L = \mathcal{O}(d)$. Check Corollary 5.5.12 by computing both sides for every $d \geq 1$.
3. (B) Let $X = \mathbb{P}^2$, $S$ a line, $p \in S$ a point and $D = c(L_1 + L_2 + L_3)$ for three lines through $p$ other than $S$, with $\frac23 \leq c < 1$. Compute $\mathcal{J}(S, D|_S)$ and determine for which $d$ Theorem 5.5.11 with $L = \mathcal{O}(d)$ applies. Compare the subspace of $H^0(S, \mathcal{O}(d - 2))$ that it produces with the image of the restriction map.
4. (B) Show that Theorem 5.5.11 implies the restriction theorem $\mathcal{J}(S, D|_S) \subseteq \mathcal{J}(X, D) \cdot \mathcal{O}_S$ of Theorem 5.4.4 for $X$ projective, after twisting by a sufficiently ample divisor.
5. (B) Let $\pi \colon X \to T$ be a smooth projective family of curves of genus $g \geq 2$ over a smooth affine curve. Show by Riemann-Roch that $P_m(X_t) = (2m - 1)(g - 1)$ for $m \geq 2$ and every $t$, and deduce Theorem 5.5.13 for this family from Proposition 5.5.19.
6. (C) In the setting of Theorem 5.5.15, let $X = \mathbb{P}^1 \times C$ and $S = \{0\} \times C$ with $C$ of genus $g \geq 2$. Show that $K_X + S$ is not $\mathbb{Q}$-linearly equivalent to an ample plus an effective divisor not containing $S$, and that the restriction map $H^0(X, m(K_X + S)) \to H^0(S, m K_S)$ is zero for every $m \geq 1$.

### Lean

None of the statements of this section is in Lean.

### Notes and history

The first extension theorem with multiplier ideals is the Ohsawa-Takegoshi $L^2$ extension theorem, whose algebraic shadow is Theorem 5.5.11; the algebraic form is in Laz04, Section 9.5 and Section 11.5. Siu introduced the inductive use of extension for the invariance of plurigenera (Siu98, Siu02), Kawamata gave the algebraic proof for general type with canonical singularities (Kaw99), and Takayama (Tak06) and Hacon-McKernan (HM06) used the same induction for the boundedness of pluricanonical maps of varieties of general type. The extension theorem of Hacon and McKernan (HM07) is the extension step in their proof of the existence of flips, and its refinements are central to the proof of the finite generation of the canonical ring (Volume 9).
