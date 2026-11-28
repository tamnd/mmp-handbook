---
title: Unsplit families and the Ionescu-Wiśniewski inequality
nodes: []
sources: [Ion86, Wis91, Kol96, Deb01, Har77]
reads_with: [Kol96:IV.2, Deb01:ch5, Wis91:all]
requires: [P7.4, P8.1, P8.2, 6.1, 6.2]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Unsplit families and the Ionescu-Wiśniewski inequality

### Statement

Let $X$ be a smooth projective variety of dimension $n$ over an algebraically closed field $k$ of any characteristic, and let $V$ be a family of rational curves in the sense of Definition 6.1.5, with $\operatorname{ev}_0 \colon V \to X$, $f \mapsto f(0)$. A *contraction* of an extremal ray $R$ is a surjective morphism $\varphi \colon X \to Y$ onto a normal projective variety, with connected fibres, whose face (Definition P7.4.10) is $R$: an integral curve is contracted by $\varphi$ if and only if its class lies in $R$. Its *exceptional locus* $\operatorname{Exc}(\varphi)$ is the union of the curves it contracts. The contraction theorem of Volume 7 provides a contraction for every $K_X$-negative extremal ray when $k$ has characteristic $0$; in this chapter a contraction is assumed whenever one is used.

**Theorem 6.3.1 (the Ionescu-Wiśniewski inequality).** Let $V$ be an unsplit family of rational curves on $X$ and $x \in \operatorname{ev}_0(V)$. Then
$$\dim \operatorname{Locus}(V) + \dim \operatorname{Locus}(V_x) \ge n + (-K_X \cdot V) - 1.$$

Lean: not yet in Lean.

**Corollary 6.3.2 (dominating unsplit families).** If $V$ is unsplit and dominating, then $\dim \operatorname{Locus}(V_x) \ge -K_X \cdot V - 1$ for every $x \in \operatorname{ev}_0(V)$, and in particular $-K_X \cdot V \le n + 1$.

Lean: not yet in Lean.

**Corollary 6.3.3 (fibres of an extremal contraction).** Let $R$ be a $K_X$-negative extremal ray with a contraction $\varphi \colon X \to Y$, and $\Gamma$ a rational curve with $[\Gamma] \in R$ and $-K_X \cdot \Gamma = \ell(R)$. Let $F$ be the fibre of $\varphi$ through a point of $\Gamma$, and $E = \operatorname{Exc}(\varphi)$. Then
$$\dim E + \dim F \ge n + \ell(R) - 1.$$
In particular, if $\varphi$ is birational, then $\dim F \ge \ell(R)$, and $\dim F \ge \ell(R) + 1$ if in addition $E$ has codimension at least $2$. If $\varphi$ is of fibre type, then $\dim F \ge \ell(R) - 1$.

Lean: not yet in Lean.

**Corollary 6.3.4 (no small contractions of smooth threefolds).** Let $X$ be a smooth projective threefold and $R$ a $K_X$-negative extremal ray with a contraction $\varphi$. Then $\varphi$ is not small: either $\varphi$ is of fibre type, or $\operatorname{Exc}(\varphi)$ is a divisor.

Lean: not yet in Lean.

### Proof in words

The family $V$ has dimension at least $n + (-K_X \cdot V)$ by the dimension estimate. Its members through a fixed point $x$ form $V_x$, of dimension at least $\dim V - \dim \operatorname{Locus}(V)$. These curves sweep out $\operatorname{Locus}(V_x)$, and the point is that the map $\mathbb{P}^1 \times V_x \to \operatorname{Locus}(V_x)$ has fibres of dimension at most $2$ away from $x$: a fibre over $y \ne x$ is the set of curves of $V$ through $x$ and $y$, with a marked point, and since $V$ is unsplit, the curves through two fixed points move only by the one-dimensional group of automorphisms of $\mathbb{P}^1$ that fix $0$ and $\infty$, by Corollary 6.1.7. Counting dimensions gives the inequality. For an extremal contraction, the curves of a minimal family through a point of a fibre stay in that fibre, and all of them lie in the exceptional locus, so the inequality bounds $\dim E + \dim F$. On a smooth threefold a small contraction would have $\dim E + \dim F \le 2$, while the inequality asks for at least $n + \ell(R) - 1 \ge 3$.

### Examples

**Example 6.3.5 (lines in projective space).** On $\mathbb{P}^n$ the family $V$ of lines is unsplit and dominating with $-K \cdot V = n + 1$, and $\operatorname{Locus}(V_x) = \mathbb{P}^n$ for every $x$. The inequality reads $n + n \ge n + (n + 1) - 1$, an equality. The contraction of the only ray is the map to a point, with $E = F = \mathbb{P}^n$.

**Example 6.3.6 (lines on quadrics).** Let $Q \subseteq \mathbb{P}^{n+1}$ be a smooth quadric, $n \ge 3$. Lines have $-K_Q \cdot L = n$, and the lines through $x$ sweep out $T_x Q \cap Q$, a cone of dimension $n - 1$ over the quadric $Q^{n-2}$ of Example 6.1.17. The inequality reads $n + (n - 1) \ge n + n - 1$, again an equality.

**Example 6.3.7 (the checks of Chapter 2).** For the two rays of $\operatorname{Bl}_p \mathbb{P}^n$ in Proposition 6.2.17, the ray of $e$ has $E = F = $ the exceptional divisor, and $(n - 1) + (n - 1) \ge n + (n - 1) - 1$; the ray of $\tilde\ell$ has $E = X$ and $F \cong \mathbb{P}^1$, and $n + 1 \ge n + 2 - 1$. On $\mathbb{P}^1 \times \mathbb{P}^2$ in Proposition 6.2.16, the ray of $\ell_1$ gives $3 + 1 \ge 3 + 2 - 1$, and the ray of $\ell_2$ gives $3 + 2 \ge 3 + 3 - 1$. On a smooth cubic surface, the ray of a line $L$ has $E = F = L$ and $1 + 1 \ge 2 + 1 - 1$. All five are equalities.

**Example 6.3.8 (a strict inequality).** Let $X$ be the blow-up of a smooth threefold at a point, so the exceptional divisor $E \cong \mathbb{P}^2$ has normal bundle $\mathcal{O}(-1)$, and the ray of a line $e \subseteq E$ has $\ell = -K_X \cdot e = 3 - 1 = 2$. Then $\dim E + \dim F = 4 = 3 + 2 - 1$. If instead $E \cong \mathbb{P}^2$ has normal bundle $\mathcal{O}(-2)$ and the ray of $e$ is extremal, as for a projective threefold that resolves a singularity $\frac12(1, 1, 1)$ by one exceptional plane (Example P8.11.7), then $\ell = 3 - 2 = 1$ and $4 > 3 + 1 - 1$.

### Proof

*Theorem 6.3.1.* Let $d = -K_X \cdot V$. By Lemma 6.1.3 with $b = 0$, $\dim V \ge d + n$. The group $\operatorname{Aut}(\mathbb{P}^1)$ is connected and acts on $\operatorname{Hom}(\mathbb{P}^1, X)$ by $f \mapsto f \circ \sigma$, so it preserves the irreducible component $V$, and $\operatorname{ev}(\mathbb{P}^1 \times V) = \operatorname{ev}_0(V)$; so $\operatorname{Locus}(V)$ is the closure of $\operatorname{ev}_0(V)$. The fibre of $\operatorname{ev}_0$ over $x$ is $V_x$, and by the theorem on the dimension of fibres every irreducible component of a nonempty fibre has dimension at least $\dim V - \dim \operatorname{Locus}(V)$. Fix such a component $V'_x$ of $V_x$, so
$$\dim V'_x \ge d + n - \dim \operatorname{Locus}(V).$$

Let $\Phi \colon \mathbb{P}^1 \times V'_x \to X$ be $(t, f) \mapsto f(t)$, whose image lies in $\operatorname{Locus}(V_x)$. Every member $f$ is nonconstant, so $f(t) \ne x$ for general $t$, and $U = \Phi^{-1}(X \setminus \{x\})$ is a dense open subset of $\mathbb{P}^1 \times V'_x$. Let $y \ne x$ be a point of $\Phi(U)$. For $(t, f) \in \Phi^{-1}(y)$ we have $t \ne 0$, and there is $\sigma \in G = \{ \sigma \in \operatorname{Aut}(\mathbb{P}^1) : \sigma(0) = 0 \}$ with $\sigma(\infty) = t$. So the morphism
$$G \times H_{x, y} \to \Phi^{-1}(y), \qquad (\sigma, g) \mapsto (\sigma(\infty), g \circ \sigma^{-1}),$$
with $H_{x, y} = \{ g \in V : g(0) = x, \ g(\infty) = y \}$, is surjective onto the part of $\Phi^{-1}(y)$ in $\mathbb{P}^1 \times V'_x$. Two pairs have the same image exactly when they differ by an element of the stabilizer $\mathbb{G}_m$ of $0$ and $\infty$, so $\dim \Phi^{-1}(y) \le \dim G + \dim H_{x, y} - 1 = \dim H_{x, y} + 1$. Every point $g$ of $H_{x, y}$ lies in $\operatorname{Hom}(\mathbb{P}^1, X; g|_{\{0, \infty\}})$, every component of which through $g$ has dimension at most $1$ by Corollary 6.1.7, since $[g] = [V]$ is unsplit. So $\dim H_{x, y} \le 1$ and $\dim \Phi^{-1}(y) \le 2$. By the theorem on the dimension of fibres applied to $\Phi|_U$,
$$\dim \operatorname{Locus}(V_x) \ge \dim U - 2 = \dim V'_x - 1 \ge d + n - \dim \operatorname{Locus}(V) - 1.$$

*Corollary 6.3.2.* Put $\dim \operatorname{Locus}(V) = n$ in the theorem, and use $\dim \operatorname{Locus}(V_x) \le n$.

*Corollary 6.3.3.* Let $f \colon \mathbb{P}^1 \to \Gamma$ be the normalization, $V$ the irreducible component of $\operatorname{Hom}(\mathbb{P}^1, X)$ through $[f]$ with its reduced structure, and $x = f(0)$, a point of $\Gamma$ and of $\operatorname{ev}_0(V)$; after composing $f$ with an automorphism, $x$ is any given point of $\Gamma$. By Lemma 6.1.6, $V$ is unsplit, and $-K_X \cdot V = \ell(R)$. Every member $g$ of $V$ has class $[\Gamma] \in R$ (Proposition P8.1.6), so its image is contracted by $\varphi$ and lies in $E$, and if $g(0) = x$ it lies in the fibre $F$ of $\varphi$ through $x$. So $\operatorname{Locus}(V) \subseteq E$ and $\operatorname{Locus}(V_x) \subseteq F$, both being closed, and Theorem 6.3.1 gives the inequality. If $\varphi$ is birational, $\dim E \le n - 1$, so $\dim F \ge \ell(R)$, and $\dim F \ge \ell(R) + 1$ when $\dim E \le n - 2$. If $\varphi$ is of fibre type, $\dim E = n$ and $\dim F \ge \ell(R) - 1$.

*Corollary 6.3.4.* By part 1 of Theorem 6.2.9 the ray $R$ contains the class of a rational curve, so a rational curve $\Gamma$ with $-K_X \cdot \Gamma = \ell(R) \ge 1$ exists, and Corollary 6.3.3 applies to the fibre $F$ through a point of $\Gamma$. If $\varphi$ were small, then $E$ would be a curve, since it is a union of curves and has dimension at most $1$, and $F \subseteq E$. Then $\dim E + \dim F \le 2 < 3 + \ell(R) - 1$, a contradiction.

### Exercises

1. (A) Check Theorem 6.3.1 for the family of lines in one ruling of $\mathbb{P}^1 \times \mathbb{P}^1$, and for the family of fibres of a $\mathbb{P}^1$-bundle over a smooth variety.
2. (A) Let $X = \mathbb{P}^a \times \mathbb{P}^b$. Check Corollary 6.3.3 for both extremal rays and decide when it is an equality.
3. (B) Show that the conics on $\mathbb{P}^2$ do not form an unsplit family, and that Theorem 6.3.1 fails for them: $\dim \operatorname{Locus}(V) + \dim \operatorname{Locus}(V_x) = 4 < 2 + 6 - 1$.
4. (B) Let $X$ be a smooth projective variety of dimension $n$ with an unsplit dominating family $V$ with $-K_X \cdot V = n + 1$. Show that $\operatorname{Locus}(V_x) = X$ for every $x \in \operatorname{ev}_0(V)$. (The theorem of Cho, Miyaoka and Shepherd-Barron says that then $X \cong \mathbb{P}^n$ in characteristic $0$; see CMSB02.)
5. (B) Let $\varphi \colon X \to Y$ be a contraction of a $K_X$-negative extremal ray on a smooth fourfold, small with exceptional locus a surface. Use Corollary 6.3.3 to show that every fibre through a minimal curve is a surface, and that $\ell(R) = 1$.
6. (C) Let $\varphi$ be the contraction of a $K_X$-negative extremal ray $R$ of a smooth projective variety, birational with exceptional locus $E$ a prime divisor. Show that every fibre of $E \to \varphi(E)$ through a minimal curve has dimension at least $\ell(R)$, and deduce that $\dim \varphi(E) \le n - 1 - \ell(R)$. Check this on the blow-up of a smooth subvariety of codimension $c \ge 2$, where $\ell(R) = c - 1$.

### Lean

Nothing in this section is in Lean. The library has `MinimalModel.ExtremalRay` and `MinimalModel.ContractionTheorem`, the statement that provides the contraction $\varphi$ in characteristic $0$, but no Hom schemes and no loci of families.

### Notes and history

The inequality is due to Ionescu (Ion86) and Wiśniewski (Wis91). Wiśniewski proved Corollary 6.3.3 for every irreducible component of every nontrivial fibre, which needs a family of minimal curves through each point of the fibre; the form here, through a point of a minimal curve, is the one that the dimension count gives directly. The proof follows Kol96, Section IV.2, and Debarre's Chapter 5 (Deb01). Corollary 6.3.4 is part of Mori's theorem on threefolds (Mor82), whose classification is the subject of Section 2.
