---
title: Rational curves on projective space and minimal rational curves
nodes: []
sources: [Kol96, Deb01, Hwa01, CMSB02, Mor79, Har77]
reads_with: [Kol96:II.3, Deb01:ch4, Hwa01:all]
requires: [P4.2, P4.7, P5.4, P8.1, P8.3]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Rational curves on projective space and minimal rational curves

### Statement

Projective space is the model for every statement of the volume: its rational curves are as free as possible, and its lines are the extreme case of the bound $-K_X \cdot \Gamma \le n + 1$.

**Proposition 6.1.10 (rational curves on projective space are very free).** Let $f \colon \mathbb{P}^1 \to \mathbb{P}^n$ be a morphism of degree $d \ge 1$, that is, $f^* \mathcal{O}(1) \cong \mathcal{O}(d)$, and write $f^* T_{\mathbb{P}^n} \cong \bigoplus_{i=1}^n \mathcal{O}(a_i)$. Then $a_i \ge d$ for every $i$ and $\sum_i a_i = (n + 1) d$. In particular $f$ is very free.

Lean: not yet in Lean.

**Theorem 6.1.11 (the space of rational curves of degree $d$).** Let $d \ge 1$ and $\operatorname{Hom}_d(\mathbb{P}^1, \mathbb{P}^n)$ the open and closed subscheme of morphisms of degree $d$.

1. $\operatorname{Hom}_d(\mathbb{P}^1, \mathbb{P}^n)$ is a smooth irreducible variety of dimension $(n + 1)(d + 1) - 1 = -K_{\mathbb{P}^n} \cdot f + n$.
2. For distinct points $x, y \in \mathbb{P}^n$ and $f$ of degree $d$ with $f(0) = x$ and $f(\infty) = y$, the scheme $\operatorname{Hom}(\mathbb{P}^1, \mathbb{P}^n; f|_{\{0, \infty\}})$ is smooth of dimension $(n + 1) d - n$ at $[f]$.
3. $\mathbb{P}^n$ is rationally connected in the sense of Definition P8.3.11, in every characteristic.

Lean: not yet in Lean.

**Proposition 6.1.12 (the rational normal curve).** Let $f \colon \mathbb{P}^1 \to \mathbb{P}^n$ be the rational normal curve $[s : t] \mapsto [s^n : s^{n-1} t : \dots : t^n]$. Then
$$f^* T_{\mathbb{P}^n} \cong \mathcal{O}(n + 1)^{\oplus n}.$$

Lean: not yet in Lean.

The second half of the section introduces the minimal rational curves of a uniruled variety, in the brief form that the volume uses.

**Definition 6.1.13 (minimal rational components and the VMRT).** Let $k$ have characteristic $0$ and $X$ be uniruled (Definition P8.3.1).

1. A *minimal rational component* of $X$ is a dominating family $V$ of rational curves (Definition 6.1.5) whose members are birational onto their images and whose degree $-K_X \cdot V$ is minimal among such families. Such a family exists. The dominant family $F \colon \mathbb{P}^1 \times M \to X$ of Definition P8.3.1, with $M$ irreducible, defines a morphism from $M$ to one irreducible component of $\operatorname{Hom}(\mathbb{P}^1, X)$, which is then dominating, and replacing the members by the normalizations of their images gives a dominating family of birational members (Kol96, Section IV.2). A member through a general point is free, so its degree is at least $2$ by Definition P5.4.12, and the degrees are positive integers.
2. For a general point $x \in X$, the *tangent map* sends a member $f \in V_x$ with $df_0 \ne 0$ to the tangent direction $[df_0(T_0 \mathbb{P}^1)] \in \mathbb{P}(T_x X)$. The closure $\mathcal{C}_x \subseteq \mathbb{P}(T_x X)$ of its image is the *variety of minimal rational tangents*, or VMRT, of $V$ at $x$.

**Lemma 6.1.14 (the curves through a general point).** Let $k$ have characteristic $0$, $V$ a dominating family whose members are birational onto their images, and $x \in X$ a general point. Then every member of $V_x$ is free, $V_x$ is smooth of pure dimension $-K_X \cdot V$, and
$$\dim \mathcal{C}_x \le -K_X \cdot V - 2.$$

Lean: not yet in Lean.

### Proof in words

On $\mathbb{P}^n$ the restricted Euler sequence presents $f^* T_{\mathbb{P}^n}$ as a quotient of $\mathcal{O}(d)^{\oplus(n+1)}$, and a quotient of a bundle all of whose summands have degree $d$ has all its summands of degree at least $d$. So every rational curve is very free and every obstruction space vanishes, and the dimension estimate becomes an equality. For the rational normal curve the twisted Euler sequence turns the computation of $h^0(f^* T(-n-2))$ into the statement that the $n + 1$ monomials of degree $n$ in two variables are linearly independent, so no summand has degree above $n + 1$, and the degree count forces all of them to equal $n + 1$. For minimal rational curves, generic smoothness makes the members through a general point free, Corollary P8.1.13 computes the dimension of $V_x$, and the two-dimensional group of automorphisms of $\mathbb{P}^1$ fixing $0$ does not change the tangent direction.

### Examples

**Example 6.1.15 (lines, conics and multiple covers).** For a line, Proposition 6.1.10 gives $a_i \ge 1$ with sum $n + 1$, so $f^* T_{\mathbb{P}^n} \cong \mathcal{O}(2) \oplus \mathcal{O}(1)^{\oplus (n-1)}$, which is Example P5.4.13. For a smooth conic in $\mathbb{P}^2$ the summands have degree at least $2$ and sum $6$; Proposition 6.1.12 with $n = 2$ gives $\mathcal{O}(3) \oplus \mathcal{O}(3)$, in accordance with Example P5.4.14. The bound $a_i \ge d$ is sharp: if $f = \lambda \circ g$ with $\lambda \colon \mathbb{P}^1 \to L$ a line and $g \colon \mathbb{P}^1 \to \mathbb{P}^1$ of degree $d$, then $f^* T_{\mathbb{P}^n} = g^*(\mathcal{O}(2) \oplus \mathcal{O}(1)^{\oplus(n-1)}) = \mathcal{O}(2d) \oplus \mathcal{O}(d)^{\oplus(n-1)}$. So the splitting type is not constant on $\operatorname{Hom}_d(\mathbb{P}^1, \mathbb{P}^n)$, even though every member is very free.

**Example 6.1.16 (the VMRT of projective space).** The lines form the unique minimal rational component of $\mathbb{P}^n$: a dominating family has degree $(n + 1) d$ for its degree $d$, so $d = 1$ is minimal. Through $x$ there is a line in every direction, so $\mathcal{C}_x = \mathbb{P}(T_x \mathbb{P}^n) \cong \mathbb{P}^{n-1}$, of dimension $n - 1 = -K \cdot \ell - 2$, and Lemma 6.1.14 is an equality. By the theorem of Cho, Miyaoka and Shepherd-Barron (CMSB02) this characterizes projective space in characteristic $0$: a Fano manifold whose VMRT at a general point is all of $\mathbb{P}(T_x X)$ is $\mathbb{P}^n$.

**Example 6.1.17 (the VMRT of a quadric).** Let $Q \subseteq \mathbb{P}^{n+1}$ be a smooth quadric with $n \ge 3$, so $-K_Q = n H$ and $\rho(Q) = 1$. A line $\ell \subseteq Q$ has $-K_Q \cdot \ell = n$, and a dominating family of rational curves has degree $n \cdot H \cdot f \ge n$, so the lines form the minimal rational component. The lines of $\mathbb{P}^{n+1}$ through $x$ that lie in $Q$ are the lines through $x$ in the cone $Q \cap T_x Q$, a cone with vertex $x$ over a smooth quadric of dimension $n - 2$. So $\mathcal{C}_x \cong Q^{n-2} \subseteq \mathbb{P}^{n-1}$, of dimension $n - 2 = -K_Q \cdot \ell - 2$, and Lemma 6.1.14 is again an equality.

### Proof

*Proposition 6.1.10.* Pull back the Euler sequence $0 \to \mathcal{O} \to \mathcal{O}(1)^{\oplus(n+1)} \to T_{\mathbb{P}^n} \to 0$ (Har77, Example II.8.20.1) by $f$:
$$0 \to \mathcal{O}_{\mathbb{P}^1} \to \mathcal{O}(d)^{\oplus(n+1)} \to f^* T_{\mathbb{P}^n} \to 0.$$
The degree gives $\sum_i a_i = (n + 1) d$. For each $i$ the projection $f^* T_{\mathbb{P}^n} \to \mathcal{O}(a_i)$ is surjective, so the composite $\mathcal{O}(d)^{\oplus(n+1)} \to \mathcal{O}(a_i)$ is surjective and in particular nonzero. A nonzero map $\mathcal{O}(d) \to \mathcal{O}(a_i)$ is a nonzero section of $\mathcal{O}(a_i - d)$, so $a_i \ge d \ge 1$, and $f$ is very free (Definition P5.4.12).

*Theorem 6.1.11.* By Example P8.1.7, $\operatorname{Hom}_d(\mathbb{P}^1, \mathbb{P}^n)$ is the open subset of $\mathbb{P}^{(n+1)(d+1) - 1}$ of tuples of binary forms of degree $d$ without common zero, which is nonempty, so it is smooth and irreducible of that dimension. The value $-K \cdot f + n = (n + 1) d + n$ agrees with it, as Corollary P8.1.13 predicts for a free curve. For part 2, all $a_i \ge 1$ by Proposition 6.1.10, so $H^1(f^* T(-2)) = 0$ by part 3 of Corollary P5.4.11, and part 2 of Corollary P8.1.13 gives smoothness of dimension $-K \cdot f - n = (n + 1) d - n$. For part 3, a line is very free, and Proposition P8.3.12 shows that $\mathbb{P}^n$ is rationally connected; directly, the family of lines $F \colon \mathbb{P}^1 \times \operatorname{Hom}_1 \to \mathbb{P}^n$ has $F^{(2)}$ dominant, since two distinct points lie on a line.

*Proposition 6.1.12.* By Proposition 6.1.10 with $d = n$, the summands have $a_i \ge n$ and $\sum_i a_i = n(n + 1)$. It is enough to show $H^0(f^* T_{\mathbb{P}^n}(-n - 2)) = 0$: then $a_i - n - 2 < 0$, so $a_i \le n + 1$ for every $i$, and since there are $n$ summands with sum $n(n + 1)$, every $a_i = n + 1$. Twist the pulled back Euler sequence by $\mathcal{O}(-n - 2)$:
$$0 \to \mathcal{O}(-n - 2) \to \mathcal{O}(-2)^{\oplus(n+1)} \to f^* T_{\mathbb{P}^n}(-n - 2) \to 0.$$
Since $H^0(\mathcal{O}(-2)) = 0$, the space $H^0(f^* T(-n-2))$ is the kernel of $\mu \colon H^1(\mathcal{O}(-n - 2)) \to H^1(\mathcal{O}(-2))^{\oplus(n+1)}$, the map given by the coordinate sections $s_j = s^{n-j} t^j \in H^0(\mathcal{O}(n))$. Both spaces have dimension $n + 1$ (Theorem P4.2.1 computes the cohomology of $\mathcal{O}(m)$ on $\mathbb{P}^1$). By Serre duality on $\mathbb{P}^1$ (Theorem P4.7.8), with $\omega = \mathcal{O}(-2)$, the dual of $\mu$ is the map $H^0(\mathcal{O})^{\oplus(n+1)} \to H^0(\mathcal{O}(n))$, $(c_j) \mapsto \sum_j c_j s_j$, which is an isomorphism because the monomials $s^{n-j} t^j$ form a basis of the binary forms of degree $n$. So $\mu$ is an isomorphism and its kernel is $0$.

*Lemma 6.1.14.* In characteristic $0$ there is a dense open subset $U \subseteq X$ such that every member $f$ of $V$ with $f(\mathbb{P}^1) \cap U \ne \emptyset$ is free (Kol96, Section II.3, by generic smoothness of $\operatorname{ev}$); take $x \in U$. For $f \in V_x$, $H^1(f^* T_X(-1)) = 0$ by part 2 of Corollary P5.4.11, so $\operatorname{Hom}(\mathbb{P}^1, X; 0 \mapsto x)$ is smooth of dimension $-K_X \cdot V$ at $[f]$ by part 1 of Corollary P8.1.13. Its points near $[f]$ lie on the unique component of $\operatorname{Hom}(\mathbb{P}^1, X)$ through $[f]$, which is smooth there by the same corollary with $b = 0$, so $V_x$ is smooth of pure dimension $-K_X \cdot V$. The group $G_0 \subseteq \operatorname{Aut}(\mathbb{P}^1)$ of automorphisms fixing $0$ has dimension $2$ and acts on $V_x$ by $f \mapsto f \circ g$. Its stabilizers are trivial, since $f \circ g = f$ with $f$ birational onto its image forces $g = \operatorname{id}$ on a dense open set. So the orbits have dimension $2$. The tangent direction of $f \circ g$ at $0$ is $df_0(dg_0(T_0 \mathbb{P}^1)) = df_0(T_0 \mathbb{P}^1)$, since $dg_0$ is an isomorphism, so the tangent map is constant on orbits. The tangent map is defined on the open $G_0$-stable subset of members with $df_0 \ne 0$, so its image has dimension at most $\dim V_x - 2 = -K_X \cdot V - 2$, and so has the closure $\mathcal{C}_x$.

### Exercises

1. (A) Use Proposition 6.1.10 to list the possible splitting types of $f^* T_{\mathbb{P}^2}$ for $f$ of degree $2$ and degree $3$, and show that $(4, 2)$ occurs in degree $2$ only for a double cover of a line.
2. (A) Check Theorem 6.1.11 for $n = 1$: $\operatorname{Hom}_d(\mathbb{P}^1, \mathbb{P}^1)$ has dimension $2d + 1$, and the maps with $0 \mapsto 0$, $\infty \mapsto \infty$ form a space of dimension $2d - 1$.
3. (B) Let $f \colon \mathbb{P}^1 \to \mathbb{P}^3$ be the twisted cubic. Use Proposition 6.1.12 and the sequence $0 \to T_{\mathbb{P}^1} \to f^* T_{\mathbb{P}^3} \to N_f \to 0$ to show that the normal bundle $N_f$ has rank $2$, degree $10$ and summands of degree at least $4$, and list the possible splitting types.
4. (B) Let $Q \subseteq \mathbb{P}^4$ be a smooth quadric threefold. Show directly that the lines of $Q$ through a point $x$ form a smooth conic, and that two general points of $Q$ are not joined by a line but are joined by a conic.
5. (B) Let $X = \mathbb{P}^1 \times \mathbb{P}^2$. Show that the fibres of the second projection form the unique minimal rational component, compute its VMRT at a general point, and check Lemma 6.1.14.
6. (C) Let $X \subseteq \mathbb{P}^{n+1}$ be a smooth hypersurface of degree $e \le n$. Assume that the lines of $X$ through a general point $x$ form a family of the expected dimension. Show that $-K_X \cdot \ell = n + 2 - e$ and that the VMRT at $x$ has dimension $n - e$, and identify it with a complete intersection of hypersurfaces of degrees $1, 2, \dots, e$ in $\mathbb{P}(T_x \mathbb{P}^{n+1})$ cut out by the Taylor expansion of the equation at $x$.

### Lean

The library has no morphisms from $\mathbb{P}^1$ and no tangent bundles, so Proposition 6.1.10, Theorem 6.1.11, Proposition 6.1.12 and Lemma 6.1.14 are not yet in Lean.

### Notes and history

Proposition 6.1.10 and its consequence that $\mathbb{P}^n$ is covered by very free curves of every degree are in Kol96, Chapter II.3, and in Debarre's Chapter 4 (Deb01). The theory of minimal rational curves and their VMRT was developed by Hwang and Mok in the 1990s; Hwang's ICTP notes are a survey (Hwa01). The characterization of projective space in Example 6.1.16 is due to Cho, Miyaoka and Shepherd-Barron, after Mori's theorem that a smooth projective variety with ample tangent bundle is $\mathbb{P}^n$ (Mor79), which is the case of a VMRT equal to $\mathbb{P}(T_x X)$ at every point.
