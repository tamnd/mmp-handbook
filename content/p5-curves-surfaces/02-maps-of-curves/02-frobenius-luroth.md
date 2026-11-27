---
title: Frobenius, inseparable maps and Lüroth's theorem
nodes: []
sources: [Har77, Sil09, Vak25]
reads_with: [Har77:IV.2, Sil09:II.2]
requires: [P1.12, P3.12, P4.5, P5.1, P5.2]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Frobenius, inseparable maps and Lüroth's theorem

### Statement

In this section $k$ is algebraically closed of characteristic $p > 0$, except in Theorem P5.2.12, where $p \geq 0$. Let $C$ be a smooth projective curve with function field $K = K(C)$. Since $k$ is perfect, $K^p = \{ a^p : a \in K \}$ is a subfield of $K$ containing $k$, and it is a function field of one variable over $k$.

**Definition P5.2.8 (Frobenius).** Let $C^{(p)}$ be the smooth projective curve with function field $K^p$, as in Theorem P5.1.3. The *$k$-linear Frobenius morphism* $F \colon C \to C^{(p)}$ is the morphism corresponding to the inclusion $K^p \subseteq K$. For $r \geq 1$, $F^r \colon C \to C^{(p^r)}$ corresponds to $K^{p^r} \subseteq K$.

**Proposition P5.2.9 (the Frobenius morphism).**

1. $[K : K^p] = p$, so $F$ has degree $p$. It is purely inseparable, bijective on points, and totally ramified at every point: $e_P = p$ for all $P$.
2. $C^{(p)}$ is isomorphic to $C$ as a scheme, not necessarily over $k$, and $g(C^{(p)}) = g(C)$.
3. If $C \subseteq \mathbb{P}^n$ is defined by homogeneous polynomials $G_j$, then $C^{(p)}$ is defined by the polynomials $G_j^{(p)}$ obtained by raising each coefficient to the power $p$, and $F$ is $[x_0 : \dots : x_n] \mapsto [x_0^p : \dots : x_n^p]$.
4. $F^* \colon \omega_{C^{(p)}} \to \omega_C$ is zero, and $\Omega_{C / C^{(p)}} = \omega_C$.

Lean: not in Lean as stated.

**Proposition P5.2.10 (factorization).** Let $f \colon C \to D$ be a nonconstant morphism of smooth projective curves. Then $f = f_s \circ F^r$ for a unique $r \geq 0$ and a separable morphism $f_s \colon C^{(p^r)} \to D$. The integer $p^r$ is the *inseparable degree* of $f$, and $\deg f = p^r \deg f_s$. In particular $f$ is separable if and only if $f^* \colon \omega_D \to \omega_C$ is nonzero.

Lean: not in Lean as stated.

**Corollary P5.2.11.** Let $f \colon C \to D$ be a nonconstant morphism of smooth projective curves, in any characteristic. Then $g(C) \geq g(D)$.

Lean: not in Lean as stated.

**Theorem P5.2.12 (Lüroth).** Let $k$ be algebraically closed of any characteristic, and $L$ a field with $k \subsetneq L \subseteq k(t)$. Then $L = k(s)$ for some $s \in L$. Equivalently, a curve dominated by $\mathbb{P}^1$ is isomorphic to $\mathbb{P}^1$.

Lean: not in Lean as stated.

### Proof in words

A function field $K$ of one variable has a separating transcendental element $x$, and $K = K^p(x)$ with $x^p \in K^p$, which gives degree $p$. Raising to the $p$-th power is a field isomorphism $K \to K^p$ that acts on $k$ by the Frobenius of $k$. So $C^{(p)}$ is $C$ with its structure map to $\operatorname{Spec} k$ twisted, and has the same genus. A general morphism corresponds to a field extension, which splits into a separable part and a purely inseparable part, and the purely inseparable extensions of $K(D)$ inside $K$ are the fields $K^{p^r}$. Lüroth's theorem follows by factoring a map from $\mathbb{P}^1$ into a power of Frobenius, which preserves $\mathbb{P}^1$, and a separable map, for which Hurwitz forces the target to have genus $0$.

### Examples

**Example P5.2.13 (the projective line).** For $C = \mathbb{P}^1$, $K = k(t)$ and $K^p = k(t^p)$, so $C^{(p)} = \mathbb{P}^1$ and $F$ is $t \mapsto t^p$. Example P3.12.8 computed $\Omega_{\mathbb{A}^1/\mathbb{A}^1} = k[t] \, dt$ for this map, the affine part of part 4 of Proposition P5.2.9.

**Example P5.2.14 (elliptic curves).** Let $p \neq 2$ and $E$ be the curve $y^2 = x^3 + ax + b$. Then $E^{(p)}$ is $y^2 = x^3 + a^p x + b^p$, and $F(x, y) = (x^p, y^p)$. If $a, b \in \mathbb{F}_p$, then $E^{(p)} = E$, and $F$ is an endomorphism of $E$ of degree $p$, fixing the point at infinity. Its fixed points are the points of $E$ with coordinates in $\mathbb{F}_p$, and $1 - F$ is a separable endomorphism, so $\#E(\mathbb{F}_p) = \deg(1 - F)$. This is the starting point of Hasse's bound $|\#E(\mathbb{F}_p) - p - 1| \leq 2\sqrt{p}$ (Silverman, Theorem V.1.1), which Theorem P5.5.25 proves for curves of every genus.

**Example P5.2.15 (an inseparable map that is not a Frobenius).** Let $m = p m'$ with $p \nmid m'$, and let $C$ be the smooth projective model of $y^p - y = x^m$; the affine curve is smooth since the partial derivative in $y$ is $-1$. The map $y \colon C \to \mathbb{P}^1$ has degree $m$, since $K = k(y)(x)$ with $x^m = y^p - y$. Over $k(y)$, the element $x^p$ satisfies the separable equation $X^{m'} = y^p - y$, and $x$ is purely inseparable of degree $p$ over $k(y, x^p)$. So the separable closure of $k(y)$ in $K$ is $k(y, x^p)$, which equals $K^p = k(x^p, y^p)$ because $y = y^p - (x^p)^{m'}$. Proposition P5.2.10 gives $y = f_s \circ F$ with $f_s$ separable of degree $m'$, and $y$ itself is neither separable nor a power of Frobenius.

**Example P5.2.16 (a Lüroth computation).** Let $k$ have characteristic $\neq 2$ and $L = k(t)^G$ for the group $G \cong (\mathbb{Z}/2)^2$ of automorphisms generated by $t \mapsto -t$ and $t \mapsto 1/t$. Lüroth's theorem says $L = k(s)$ for some $s$, and $s = t^2 + t^{-2}$ works: $s$ is $G$-invariant, so $k(s) \subseteq L$, and $[k(t) : k(s)] = 4 = |G| = [k(t) : L]$ by Artin's theorem, since $t$ is a root of $t^4 - s t^2 + 1$. By Hurwitz, the quotient map $\mathbb{P}^1 \to \mathbb{P}^1$ of degree $4$ has $\deg R = 6$, carried by the $6$ points $t \in \{0, \infty, \pm 1, \pm i\}$ with nontrivial stabilizers, each with $e = 2$.

### Proof

*Proposition P5.2.9, part 1.* By Theorem P1.12.14 and Corollary P1.12.17, there is $x \in K$ with $K / k(x)$ finite separable: choose $x$ with $dx \neq 0$ in $\Omega_{K/k}$, which is one-dimensional over $K$. Then $K = K^p(x)$: the field $K^p(x)$ contains $k(x)$, so $K / K^p(x)$ is separable, and it is purely inseparable since $a^p \in K^p$ for every $a \in K$, so it is trivial. The element $x$ satisfies $X^p - x^p$ over $K^p$, and $x \notin K^p$, since $d(K^p) = 0$ while $dx \neq 0$. The minimal polynomial of $x$ over $K^p$ divides $(X - x)^p$, so it is $(X - x)^j$ for some $1 \leq j \leq p$. Its coefficient of $X^{j-1}$ is $-jx \in K^p$, so $j = p$, and the degree is $p$.

$F$ is purely inseparable by construction. On points, $F$ is a bijection: for each DVR $R$ of $K/k$, the ring $R \cap K^p = R^p$ is a DVR of $K^p$, and conversely every DVR $S$ of $K^p$ has exactly one DVR of $K$ over it, namely $\{a : a^p \in S\}$. For a local parameter $s$ at $P$, $s^p$ is a local parameter at $F(P)$, since $v_P(s^p) = p$ and $R^p$ has valuation $v_{F(P)}(a^p) = v_P(a)$. So $e_P = v_P(F^*(s^p)) = p$.

*Part 2.* The map $\phi \colon K \to K^p$, $a \mapsto a^p$, is an isomorphism of fields, and it maps $k$ onto $k$ by the Frobenius of $k$, which is an automorphism since $k$ is perfect. It maps DVRs of $K$ to DVRs of $K^p$, so it induces an isomorphism of schemes $C^{(p)} \to C$ lying over the automorphism $\operatorname{Spec} \phi|_k$ of $\operatorname{Spec} k$. So $C^{(p)} \cong C \times_{\operatorname{Spec} k, \sigma} \operatorname{Spec} k$ is the base change of $C$ by the Frobenius $\sigma$ of $k$. Cohomology commutes with flat base change (Theorem P4.5.1), and $\sigma$ is an isomorphism, so $h^1(C^{(p)}, \mathcal{O}) = h^1(C, \mathcal{O})$.

*Part 3.* The base change by $\sigma$ applies $\sigma$ to the coefficients of the equations. The map $x_i \mapsto x_i^p$ sends a point of $C$ to a point of $C^{(p)}$, since $G_j^{(p)}(x_0^p, \dots, x_n^p) = G_j(x_0, \dots, x_n)^p = 0$, and on function fields it gives the inclusion $K^p \subseteq K$ in the coordinates $x_i / x_0$.

*Part 4.* For a local parameter $u = s^p$ at $F(P)$, $F^* du = d(s^p) = 0$. So $F^* \colon F^* \omega_{C^{(p)}} \to \omega_C$ is zero, and the sequence of Theorem P3.12.4 gives $\Omega_{C/C^{(p)}} = \omega_C$.

*Proposition P5.2.10.* Let $L_s$ be the separable closure of $K(D)$ in $K$. Then $K/L_s$ is purely inseparable of some degree $p^r$, so $a^{p^r} \in L_s$ for all $a \in K$, that is, $K^{p^r} \subseteq L_s$. By part 1 applied $r$ times, $[K : K^{p^r}] = p^r = [K : L_s]$, so $L_s = K^{p^r}$. By Theorem P5.1.3, the inclusions $K(D) \subseteq K^{p^r} \subseteq K$ give $C \xrightarrow{F^r} C^{(p^r)} \xrightarrow{f_s} D$ with $f_s$ separable. Uniqueness of $r$ holds since $p^r$ is the inseparable degree $[K : L_s]$. For the last statement, if $f$ is separable, $f^* \omega_D \to \omega_C$ is injective by Proposition P5.2.1. If $r \geq 1$, then $f^* = F^{r*} f_s^*$ is zero on differentials by part 4 of Proposition P5.2.9.

*Corollary P5.2.11.* Write $f = f_s \circ F^r$. By part 2 of Proposition P5.2.9, $g(C^{(p^r)}) = g(C)$, and by Corollary P5.2.3, $g(C^{(p^r)}) \geq g(D)$. In characteristic $0$ every morphism is separable and Corollary P5.2.3 applies directly.

*Theorem P5.2.12.* The field $L$ has transcendence degree $1$ over $k$, since it contains an element not in $k$, which is transcendental as $k$ is algebraically closed in $k(t)$. It is finitely generated: $k(t)$ is finite over $L$, since $t$ is algebraic over $k(u)$ for any $u \in L \setminus k$, and a subfield of a finitely generated field extension is finitely generated (Exercise 4). So $L = K(D)$ for a smooth projective curve $D$, and the inclusion $L \subseteq k(t)$ gives a nonconstant morphism $\mathbb{P}^1 \to D$. By Corollary P5.2.11, $g(D) \leq g(\mathbb{P}^1) = 0$, so $D \cong \mathbb{P}^1$ by Proposition P5.1.12, and $L \cong k(s)$.

### Exercises

1. (A) Show that the $k$-linear Frobenius of the plane cubic $y^2 z = x^3 + x z^2$ over $\overline{\mathbb{F}}_3$ is an endomorphism, and find its degree and its fixed points.
2. (A) Show that the composite $C \xrightarrow{F} C^{(p)} \to C$ of the Frobenius with the isomorphism of part 2 of Proposition P5.2.9 is the absolute Frobenius of the scheme $C$, which is not a morphism over $k$.
3. (B) Show that every purely inseparable morphism of smooth projective curves of degree $p^r$ is isomorphic to $F^r$.
4. (B) Let $k \subseteq L \subseteq M$ be fields with $M/k$ finitely generated. Show that $L/k$ is finitely generated. Use a transcendence basis of $L$ and the finiteness of $M$ over $k(\text{basis})(\text{further generators})$.
5. (B) Let $C$ be a smooth projective curve in characteristic $p$ and $f \colon C \to \mathbb{P}^1$ separable. Show that $\operatorname{div}(f^* dx)$ is the ramification divisor minus $2 f^* \infty$, and use it to compute the genus of the curve $y^2 = x^p - x$ for $p$ odd.
6. (C) Show that the hypothesis that $k$ is algebraically closed matters. Let $L = \mathbb{R}(x, y)$ with $x^2 + y^2 + 1 = 0$. Show that $L$ is not of the form $\mathbb{R}(s)$, since the conic has no real point, while $L \otimes_\mathbb{R} \mathbb{C} \cong \mathbb{C}(t)$. Then show that over any field $k$, a subfield $k \subsetneq L \subseteq k(t)$ is still of the form $k(s)$, by the argument of Steinitz: take $s$ to be a nonconstant coefficient of the minimal polynomial of $t$ over $L$.

### Lean

Mathlib has the Frobenius endomorphism of a ring of characteristic $p$, separable and purely inseparable closures, and the separable degree of a field extension, but not the Frobenius morphism of a curve or Lüroth's theorem. The handbook adds no `MinimalModel` node here.

### Notes and history

Lüroth proved his theorem over $\mathbb{C}$ in 1876, and Steinitz gave a purely algebraic proof valid over any field in 1910. Castelnuovo proved the analogue for surfaces over $\mathbb{C}$ in 1894: a unirational surface is rational. Zariski found unirational surfaces in characteristic $p$ that are not rational, using purely inseparable covers of $\mathbb{P}^2$, and in dimension $3$ over $\mathbb{C}$ the analogue fails by Clemens-Griffiths and Iskovskikh-Manin (1971). The literature state is theorem. In the minimal model program in characteristic $p$, the Frobenius morphism is both an obstacle and a tool: it breaks Kodaira vanishing, and it gives the Frobenius splitting and $F$-singularity methods of Volume 11.
