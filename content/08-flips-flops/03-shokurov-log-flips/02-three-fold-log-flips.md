---
title: Shokurov's 3-fold pl flips and complements
nodes: [MM3A98X8YR]
sources: [Sho92, Cor07, Kol92, Mor88, KM98]
reads_with: [Cor07:2, Kol92:18]
requires: [4.3, 4.5, 5.1, 1.1]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Shokurov's 3-fold pl flips and complements

### Statement

The notation is that of Section 1. For a pl flipping contraction $f \colon (X, S + B) \to Z$ of a 3-fold, $S$ is a normal surface (Theorem 4.5.18), $f$ restricts to a projective birational morphism $f_S \colon S \to T = f(S)$ onto a normal surface, and $(S, B_S)$ with $B_S = \operatorname{Diff}_S(B)$ is a klt surface pair with $K_S + B_S = (K_X + S + B)|_S$ (Theorem 4.5.17 and Theorem 4.5.13).

**Theorem 8.3.9 (Shokurov's 3-fold pl flips).** Let $f \colon X \to Z$ be a pl flipping contraction of a 3-fold pair $(X, S + B)$. Then the restricted algebra $R_S$ of Definition 8.3.3 is finitely generated, and so the pl flip exists.

Lean: not yet in Lean.

**Theorem 8.3.10 (3-fold klt flips exist).** Let $(X, \Delta)$ be a $\mathbb{Q}$-factorial klt 3-fold pair and $f \colon X \to Z$ a flipping contraction of $(X, \Delta)$. Then the flip of $f$ exists.

Node: MM3A98X8YR · Lean: `MinimalModel.ThreefoldFlips`

**Definition 8.3.11 (complements).** Let $(T, B)$ be a pair with $T$ normal, $B = \sum_j b_j B_j$ with $0 \le b_j \le 1$, and $\{B\} = B - \lfloor B \rfloor$ its fractional part, and let $n \ge 1$ be an integer. An *$n$-complement* of $K_T + B$ is a $\mathbb{Q}$-divisor $B^+$ on $T$ such that

1. $n(K_T + B^+) \sim 0$,
2. the pair $(T, B^+)$ is lc, and
3. $n B^+ \ge n \lfloor B \rfloor + \lfloor (n + 1) \{B\} \rfloor$.

The same definition applies to a germ of $T$ along a fibre of a morphism $T \to T'$, with linear equivalence on the germ. Condition 3 implies $B^+ \ge B$ for the coefficients of the form $1 - \frac1m$ that arise from adjunction, which is the case of interest.

**Theorem 8.3.12 (complements on surface germs).** Let $g \colon T \to T'$ be a projective birational morphism of normal surfaces, $t \in T'$ a point, and $(T, B)$ a klt pair with $-(K_T + B)$ nef over $T'$, and suppose the coefficients of $B$ are standard, of the form $1 - \frac1m$ with $m \ge 1$ an integer or $1$. Then over a neighbourhood of $t$, $K_T + B$ has an $n$-complement for some $n \in \{1, 2, 3, 4, 6\}$.

Lean: not yet in Lean.

Theorems 8.3.9 and 8.3.12 are due to Shokurov (Sho92) and are cited, with an outline of the proof of Theorem 8.3.9; Theorem 8.3.12 is stated in a simplified form, and the precise hypotheses are in Sho92; Kol92 and Cor07 contain complete accounts. Theorem 8.3.10 is proved from them, Theorem 8.3.5 and Theorem 8.3.6. It contains Mori's flip theorem of Chapter 2: a terminal 3-fold is klt, and for a $\mathbb{Q}$-factorial terminal 3-fold Theorem 8.3.10 with $\Delta = 0$ is Theorem 8.2.9 for $\mathbb{Q}$-factorial $X$.

### Proof in words

By Theorem 8.3.4 and Lemma 8.3.2, a pl flip exists when the restricted algebra $R_S$ on the surface $S$ is finitely generated. Shokurov's insight is that this algebra is very close to an algebra of complete linear systems on $S$, and that the difference is measured by the mobile parts of these linear systems on a fixed resolution of $S$. Kawamata-Viehweg vanishing on $X$ shows that the restriction maps are surjective onto sections of divisors whose fixed parts are bounded, a property called saturation, and the existence of complements on surfaces shows that the normalised mobile parts converge to a limit that is attained, so that the mobile parts are eventually given by one $\mathbb{Q}$-divisor. An algebra of this form is finitely generated.

For klt flips, the reduction theorem of Section 1 turns a klt flip into a sequence of pl flips, which exist, and special termination for 3-folds stops the sequence.

### Examples

**Example 8.3.13 (a $1$-complement of the plane).** Let $T = \mathbb{A}^2$ with coordinates $x, y$, and $B = 0$. Then $B^+ = \{x = 0\} + \{y = 0\}$ is a $1$-complement: $K_T + B^+ = \operatorname{div}\big((dx \wedge dy)/(xy)\big) \sim 0$, the pair $(\mathbb{A}^2, \{xy = 0\})$ is lc, being toric with its full toric boundary, and condition 3 reads $B^+ \ge 0$. The same $B^+$ is a $1$-complement of $(\mathbb{A}^2, \frac12 \{x = 0\})$, since condition 3 then asks $B^+ \ge \lfloor 2 \cdot \frac12 \rfloor \{x = 0\} = \{x = 0\}$.

**Example 8.3.14 (a 2-complement that is not a 1-complement).** Let $T = \mathbb{P}^1$ and $B = \frac12(p_1 + p_2 + p_3 + p_4)$ for distinct points $p_i$. Then $\deg(K_T + B) = -2 + 2 = 0$. The divisor $B^+ = B$ is a $2$-complement: $2(K_T + B) = 2K_T + \sum_i p_i$ has degree $0$, so it is linearly equivalent to $0$ on $\mathbb{P}^1$; the pair is klt; and condition 3 reads $2B \ge \lfloor 3 \cdot \frac12 \rfloor \sum_i p_i = \sum_i p_i$, which holds with equality. There is no $1$-complement: condition 3 for $n = 1$ asks $B^+ \ge \lfloor 2 \cdot \frac12 \rfloor \sum_i p_i = \sum_i p_i$, of degree $4$, while $K_T + B^+ \sim 0$ forces $\deg B^+ = 2$. This is the curve case of the phenomenon behind Theorem 8.3.12: the possible indices $n$ are bounded, but $n = 1$ is not always enough.

**Example 8.3.15 (complements on the plt centre of the Francia flip).** In Example 8.3.7, $(S, B_S) = (S, 0)$ with $S \to T = \mathbb{A}^2$ the weighted blow-up with weights $(1, 2)$ and $-K_S$ ample over $T$, as $K_S \cdot C^- = -1$. In the toric coordinates, $T = \operatorname{Spec} k[x, y]$ and the toric boundary $\{xy = 0\}$ pulls back to $K_S + \{x = 0\}' + \{y = 0\}' + C^- \sim 0$ over $T$, where the primes denote strict transforms. So $B^+ = \{x = 0\}' + \{y = 0\}' + C^-$ is a $1$-complement of $K_S$ over $T$, the toric one, and $(S, B^+)$ is lc as a toric pair with its full boundary.

### Proof

*Theorem 8.3.9, outline.* This follows Cor07, Chapter 2. By Corollary 8.1.7 and Lemma 8.3.2, work over an affine neighbourhood of a point of $Z$ and with $R_S$. Fix $r \ge 1$ with $r(K_X + S + B)$ Cartier. By Lemma 8.3.2 and part 2 of Lemma 8.1.5, finite generation of $R(X/Z, S)$ is equivalent to that of $\bigoplus_m f_* \mathcal{O}_X(mr(K_X + S + B))$, and by Theorem 8.3.4, applied to the divisor $r(K_X + S + B)$ with the section that cuts out $S$ replaced by the corresponding one, to the finite generation of the restricted algebra $\bigoplus_m \operatorname{Im}\big(H^0(X, mr(K_X + S + B)) \to H^0(S, mr(K_S + B_S))\big)$.

Step 1, saturation. Let $h \colon S' \to S$ be a log resolution of $(S, B_S)$, let $M_m$ be the mobile part of the pullback to $S'$ of the linear system given by the image in degree $m$, and let $D_m = M_m / m$. Kawamata-Viehweg vanishing on $X$ (Theorem 5.1.13), applied to sheaves of the form $\mathcal{O}_X(mr(K_X + S + B) - S)$ over $Z$, shows that the restriction maps are surjective onto the sections of the corresponding divisors on $S$, and this translates into the *a-saturation* of the algebra: there is a fixed $\mathbb{Q}$-divisor $A$ on $S'$, exceptional over $S$ with $\lceil A \rceil \ge 0$, such that $\operatorname{Mob} \lceil j D_i + A \rceil \le j D_j$ for all $i \ge j$ in a suitable divisible range. The precise form, and the choice of $A$ from the discrepancies of $(S, B_S)$, are in Cor07, Chapter 2.

Step 2, the limit of the mobile parts. The $\mathbb{Q}$-divisors $D_m = M_{m}/m$ on $S'$ satisfy $D_{i + j} \ge \frac{i}{i+j} D_i + \frac{j}{i+j} D_j$, so they converge to a limit $D$. A Diophantine approximation argument on the finite dimensional space spanned by the exceptional curves of $h$, combined with saturation, shows that if $D$ is attained, that is $D = D_m$ for some $m$, then the algebra is finitely generated, being a Veronese of the algebra of the semiample divisor $D$.

Step 3, the limit is attained. Here the dimension is used: on the surface $S$ the limit $D$ is semiample over $T$, and the existence of complements for the klt surface germs $(S, B_S) \to T$ near the image of $C$ (Theorem 8.3.12) bounds the denominators of the limit, which, together with saturation, forces $D_m = D$ for $m$ divisible by the index of the complement. Corti's account in Cor07 replaces the complements by a direct argument on the surface for the 3-fold case.

*Theorem 8.3.10.* Pl flips of 3-folds exist by Theorem 8.3.9, and special termination holds for 3-folds by Theorem 8.3.6. By Theorem 8.3.5 with $n = 3$, the flip of every flipping contraction of a 3-dimensional $\mathbb{Q}$-factorial klt pair exists.

### Exercises

1. (A) Show that $(\mathbb{A}^2, \{x = 0\} + \{y = 0\} + \{x = y\})$ is not lc, so that three lines through a point never form part of a complement.
2. (A) Let $T = \mathbb{P}^1$ and $B = \frac23(p_1 + p_2 + p_3)$. Find the least $n$ for which $K_T + B$ has an $n$-complement.
3. (A) Let $T = \mathbb{P}^1$ and $B = \frac12 p_1 + \frac23 p_2 + \frac56 p_3$. Show that $K_T + B$ has a $6$-complement and no $n$-complement with $n < 6$, using that $\deg(K_T + B^+) = 0$.
4. (B) Find a $1$-complement of the germ of an $A_1$ surface singularity $(T, 0)$, $T = \mathbb{A}^2/\pm 1$, with $B = 0$, and check that it is lc by passing to the double cover $\mathbb{A}^2$.
5. (B) In Example 8.3.15, compute the coefficient of $C^-$ in the pullback of $K_T + \{xy = 0\}$ to $S$, and check that it is $1$ using the weights $(1, 2)$.
6. (C) Let $D_m$ be a sequence of $\mathbb{Q}$-divisors on a smooth surface with $D_{i + j} \ge \frac{i}{i+j} D_i + \frac{j}{i+j} D_j$ for all $i, j$, and with bounded coefficients. Show that the coefficients of $D_m$ converge as $m \to \infty$, and give an example in which the limit is not attained.

### Lean

The library has `MinimalModel.ThreefoldFlips`, the statement that flips of $\mathbb{Q}$-factorial klt 3-folds exist, which is the map node of Theorem 8.3.10; it is a statement without proof in the library. It also has `MinimalModel.KltFlips` for klt flips in all dimensions and `MinimalModel.HasInfiniteFlips` for the failure of termination. Theorem 8.3.9 and the theory of complements are not yet in Lean.

### Notes and history

Shokurov proved the existence of 3-fold log flips in Sho92, a long paper whose ideas were digested in Kol92, Chapter 18 and the surrounding chapters, and much later in Corti's account in Cor07, Chapter 2, which introduced the language of the restricted algebra, saturation and the limit of mobile parts used here. The theory of complements is from the same paper. The method was extended to 4-folds by Shokurov, and the finite generation of the restricted algebra was proved in all dimensions by Hacon and McKernan, which led to BCHM10.
