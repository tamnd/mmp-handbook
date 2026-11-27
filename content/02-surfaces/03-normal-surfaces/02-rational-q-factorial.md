---
title: Rational singularities are Q-factorial
nodes: []
sources: [Lip69, Art66, Mum61, Sil09]
reads_with: [KM98:ch4, Kol13:ch3]
requires: [P1.8, P3.9, P5.5, P5.8, 4.2, 4.3]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Rational singularities are Q-factorial

### Statement

Let $X$ be a normal projective surface, $f \colon Y \to X$ a resolution, and $x \in X$ a point. Let $E_1, \dots, E_r$ be the curves of $f^{-1}(x)$, and $M_x = (E_i \cdot E_j)$ their intersection matrix, negative definite by Theorem P5.8.3. The fibre $f^{-1}(x)$ is connected, by part 1 of Theorem P5.8.3. If $r = 0$, then $f$ is an isomorphism over a neighbourhood of $x$ and $x$ is a smooth point. Write $\mathcal{O} = \mathcal{O}_{X,x}$, and let $\operatorname{Cl}(\mathcal{O})$ be its class group, the target of the surjection $\operatorname{Cl}(X) \to \operatorname{Cl}(\mathcal{O})$ of part 1 of Proposition P3.9.19.

**Definition 2.3.10 (numerically Cartier divisors and the discriminant group).** For an $\mathbb{R}$-Weil divisor $D$ on $X$, let $c_x(D) \in \mathbb{R}^r$ be the vector of coefficients of $E_1, \dots, E_r$ in the Mumford pullback $f^*D$ of Corollary P5.8.5. A Weil divisor $D$ is *numerically Cartier at $x$* if $c_x(D) \in \mathbb{Z}^r$. The *discriminant group* of $x$ is the finite abelian group
$$\Phi_x = M_x^{-1} \mathbb{Z}^r / \mathbb{Z}^r \cong \mathbb{Z}^r / M_x \mathbb{Z}^r,$$
of order $|\det M_x|$, where the isomorphism is multiplication by $M_x$.

Let $u_x(D) = (f^{-1}_* D \cdot E_j)_j \in \mathbb{Z}^r$ for a Weil divisor $D$. By Corollary P5.8.5, $M_x c_x(D) = -u_x(D)$, because the curves over other points of $T_0$ are disjoint from the $E_j$. So $c_x(D) = -M_x^{-1} u_x(D)$ lies in $M_x^{-1}\mathbb{Z}^r$.

**Lemma 2.3.11 (the class map).** The map $D \mapsto c_x(D) \bmod \mathbb{Z}^r$ on Weil divisors induces a group homomorphism
$$\gamma_x \colon \operatorname{Cl}(\mathcal{O}_{X,x}) \to \Phi_x.$$
Its kernel is the set of classes of divisors that are numerically Cartier at $x$, and every divisor that is Cartier at $x$ is numerically Cartier at $x$.

Lean: not yet in Lean.

Rational singularities are those of Definition P5.8.14, with $(R^1 f_* \mathcal{O}_Y)_x = 0$. By Exercise 5 of Section 2 of Chapter P5.8 and Theorem P5.7.12 the condition does not depend on the resolution, and Theorem P5.8.16 decides it from $M_x$ and the genera of the $E_i$. The deep input of this section is Lipman's theorem.

**Theorem 2.3.12 (Lipman's generation theorem).** Let $x$ be a rational singularity, and $\mathcal{L}$ a line bundle on $Y$ with $\mathcal{L} \cdot E_i \ge 0$ for $i = 1, \dots, r$. Then for every point $y \in f^{-1}(x)$ there are an open neighbourhood $U$ of $x$ and a section $s \in H^0(f^{-1}(U), \mathcal{L})$ with $s(y) \ne 0$.

Lean: not yet in Lean.

**Theorem 2.3.13 (numerically Cartier is Cartier at a rational singularity).** Let $x$ be a rational singularity and $D$ a Weil divisor on $X$.

1. $D$ is Cartier at $x$ if and only if it is numerically Cartier at $x$.
2. The class map $\gamma_x$ is injective. So $\operatorname{Cl}(\mathcal{O}_{X,x})$ is a finite abelian group whose order divides $|\det M_x|$.
3. $mD$ is Cartier at $x$ for $m = |\det M_x|$, and the index $r_x(D)$ is the order of $c_x(D)$ in $\mathbb{Q}^r / \mathbb{Z}^r$. So $X$ is $\mathbb{Q}$-factorial at $x$.

Lean: not yet in Lean.

**Corollary 2.3.14 (surfaces with rational singularities).** Let $X$ be a normal projective surface whose singular points $x_1, \dots, x_s$ are rational. Then $X$ is $\mathbb{Q}$-factorial, and for every Weil divisor $D$ the divisor $mD$ is Cartier, where $m = \operatorname{lcm}_j |\det M_{x_j}|$ is computed on any resolution. For every resolution $f$ and every Weil divisor $D$, the Mumford pullback $f^*D$ is $\frac1m f^*(mD)$, the pullback of the $\mathbb{Q}$-Cartier divisor $D$ in the sense of Volume 4.

Lean: not yet in Lean.

### Proof in words

A Weil divisor is Cartier at $x$ when it is principal near $x$. Its Mumford pullback is then the pullback of a function, with integer coefficients, so being Cartier forces being numerically Cartier, and the discriminant group measures the failure. For the converse, an integral Mumford pullback $f^*D$ is a line bundle on $Y$ of degree 0 on every exceptional curve. At a rational singularity Lipman's theorem gives it a section that does not vanish at a chosen point of the fibre. The divisor of that section has degree 0 on every exceptional curve; the negativity lemma on the connected fibre forbids an exceptional part, and positivity of local intersections then forbids any other part near the fibre. So $f^*D$ is the divisor of a function near the fibre, and $D$ is its pushforward, principal near $x$. The local class group therefore injects into a finite group of order $|\det M_x|$, and every Weil divisor is $\mathbb{Q}$-Cartier. Without rationality, Lipman's theorem fails, and the cone over an elliptic curve has an uncountable local class group.

### Examples

**Example 2.3.15 (the cone $X_n$).** In Example 2.3.8 the vertex $v$ of $X_n$ is a rational singularity by Example P5.8.19 and Theorem P5.8.16, with $r = 1$, $M_v = (-n)$ and $\Phi_v = \frac1n \mathbb{Z} / \mathbb{Z} \cong \mathbb{Z}/n$. The line $\ell$ has $c_v(\ell) = \frac1n$, a generator of $\Phi_v$. By Theorem 2.3.13, $\gamma_v$ is injective with image containing a generator, so $\operatorname{Cl}(\mathcal{O}_{X_n, v}) \cong \mathbb{Z}/n$, generated by $\ell$. The divisor $k\ell$ is Cartier at $v$ exactly when $n \mid k$, in accordance with $H \sim n\ell$, and every Weil divisor of $X_n$ is $\mathbb{Q}$-Cartier of index dividing $n$. For $n = 2$ this recovers Example P5.8.9: $L_a$ is not Cartier and $2L_a$ is.

**Example 2.3.16 (the $A_n$ singularities).** Let $x$ be a point whose exceptional curves $E_1, \dots, E_n$ form the chain $A_n$ of $(-2)$-curves, $E_i \cdot E_{i+1} = 1$. By Proposition P5.8.17 it is a rational double point. The matrix $M_x$ has $\det M_x = (-1)^n (n+1)$, by expansion along the last row: $d_n = -2 d_{n-1} - d_{n-2}$ with $d_1 = -2$ and $d_0 = 1$. A Weil divisor $D$ whose strict transform meets $E_1$ transversally in one point and no other $E_i$ has $u_x(D) = (1, 0, \dots, 0)$, and
$$c_x(D) = \Big( \frac{n}{n+1}, \frac{n-1}{n+1}, \dots, \frac{1}{n+1} \Big),$$
since $c_{i-1} - 2c_i + c_{i+1} = 0$ for $1 < i < n$, $-2c_1 + c_2 = -1$ and $c_{n-1} - 2c_n = 0$, with $c_0 = 1$ in the middle equations. Its class has order $n + 1$ in $\Phi_x$, and $\Phi_x$ has order $n + 1$, so $\Phi_x$ is cyclic and $\gamma_x$ is an isomorphism when such a $D$ exists. If $x$ has a neighbourhood isomorphic to a neighbourhood of the vertex of $V(xy - z^{n+1}) \subset \mathbb{A}^3$, whose minimal resolution is the chain $A_n$ by Theorem 4.3.13 and Example 4.3.21, then Example P3.9.21 gives $\operatorname{Cl}(\mathcal{O}_{X,x}) \cong \mathbb{Z}/(n+1)$ directly, and the injective map $\gamma_x$ of Theorem 2.3.13 is an isomorphism, as the orders agree.

**Example 2.3.17 (the $E_8$ singularity is factorial).** Let $x$ be a point whose exceptional curves form the $E_8$ configuration of $(-2)$-curves: a chain $e_1, e_3, e_4, e_5, e_6, e_7, e_8$ with a curve $e_2$ meeting $e_4$. It is a rational double point by Proposition P5.8.17. A direct computation, Problem 8, gives $\det M_x = 1$. So $\Phi_x = 0$, and by Theorem 2.3.13 the local class group $\operatorname{Cl}(\mathcal{O}_{X,x})$ is zero: every Weil divisor is Cartier at $x$, and by Proposition P1.8.10 the local ring $\mathcal{O}_{X,x}$ is a unique factorization domain although it is not regular. For a divisor whose strict transform meets $e_1$ once, $c_x = (4, 5, 7, 10, 8, 6, 4, 2)$ in the order $e_1, \dots, e_8$, an integer vector, as it must be.

**Counterexample 2.3.18 (the cone over an elliptic curve is not $\mathbb{Q}$-factorial).** Let $k = \mathbb{C}$, let $V$ be a smooth projective curve of genus 1, $L$ a line bundle of degree $d \ge 1$, and $X = C(V, L)$ the cone of Section 3 of Chapter 2 of Volume 4, with the resolution $f \colon Y \to X$ by the total space of $L^{-1}$ and exceptional curve $E \cong V$. Then $\mathcal{O}_Y(-E) \cong p^*L$, so $\mathcal{O}_Y(E)|_E \cong L^{-1}$ and $E^2 = -d$. This $X$ is affine, so the global theory above does not apply directly, but every statement used here is local near $E$, and the numerical pullback of Definition 4.3.3 plays the role of $f^*$. For $q \in V$ let $F_q = p^{-1}(q)$ be the fibre, a line meeting $E$ transversally at one point, and $\ell_q = f(F_q)$, a line through the vertex $0$. Since $(F_q + cE) \cdot E = 1 - dc$, the pullback is $f^*\ell_q = F_q + \frac1d E$.

Suppose $m\ell_q$ is Cartier at $0$ for some $m \ge 1$. Then $m\ell_q = \operatorname{div}(h)$ on a neighbourhood $U$ of $0$, so $f^*(m\ell_q) = mF_q + \frac md E$ is $\operatorname{div}_Y(h)$ on $f^{-1}(U)$. So $d \mid m$, and the line bundle $\mathcal{O}_Y(mF_q + \frac md E)$ is trivial near $E$. Restricted to $E$ it is $\mathcal{O}_V(mq) \otimes L^{-m/d}$. So $\mathcal{O}_V(dq) \otimes L^{-1}$ is a torsion point of $\operatorname{Pic}^0(V)$. Fix $q_0 \in V$. The map $V \to \operatorname{Pic}^0(V)$, $q \mapsto \mathcal{O}_V(dq) \otimes L^{-1}$, is the composite of the isomorphism $q \mapsto \mathcal{O}_V(q - q_0)$ of Sil09, Proposition III.3.4, with multiplication by $d$ and a translation, so it is surjective with finite fibres. The torsion of the group $V(\mathbb{C})$ is countable, since its $N$-torsion is finite for each $N$ (Sil09, Corollary III.6.4). So the $q$ with $\ell_q$ $\mathbb{Q}$-Cartier form a countable subset of $V$, and for a general $q$ the line $\ell_q$ is not $\mathbb{Q}$-Cartier. So $X$ is not $\mathbb{Q}$-factorial at $0$, and $\operatorname{Cl}(\mathcal{O}_{X,0})$ is not torsion, although $\Phi_0 = \mathbb{Z}/d$ is finite. The divisor $d\ell_q$ is numerically Cartier at $0$ and, for general $q$, not Cartier. This does not contradict Theorem 2.3.13: by Exercise 6 of Section 2 of Chapter P5.8, a curve of genus 1 is never contracted to a rational singularity, and Example P5.8.21 shows this for the cone over a plane cubic. The canonical divisor, on the other hand, is Cartier: by the facts listed in Section 3 of Chapter 2 of Volume 4, $K_Y \sim p^*K_V - E \sim -E$, so $K_X = f_*K_Y \sim 0$, and $a(E, X, 0) = -1$ by Corollary 4.2.20.

### Proof

*Lemma 2.3.11.* The map $D \mapsto c_x(D)$ is linear by Corollary P5.8.5, with values in $M_x^{-1}\mathbb{Z}^r$, so $D \mapsto c_x(D) \bmod \mathbb{Z}^r$ is a homomorphism from the group of Weil divisors to $\Phi_x$. If $D$ is Cartier at $x$, then $D = \operatorname{div}_X(h) + D_1$ with $\operatorname{Supp} D_1$ not containing $x$, for $h$ a local equation of $D$ at $x$ and $D_1 = D - \operatorname{div}_X(h)$, which vanishes near $x$. The principal divisor $\operatorname{div}_X(h)$ is Cartier, so $f^* \operatorname{div}_X(h) = \operatorname{div}_Y(h)$ by Corollary P5.8.5, with integer coefficients. The strict transform of $D_1$ does not meet $f^{-1}(x)$, so $u_x(D_1) = 0$ and $c_x(D_1) = 0$. So $c_x(D) \in \mathbb{Z}^r$. By part 1 of Proposition P3.9.19 every class of $\operatorname{Cl}(\mathcal{O})$ is the class of some Weil divisor $D$ on $X$, and $[\rho_x(D)] = 0$ if and only if $D$ is Cartier at $x$, by part 2 of Proposition P3.9.19. The homomorphism therefore vanishes on the divisors with $[\rho_x(D)] = 0$, so it factors through $\operatorname{Cl}(\mathcal{O})$, and the kernel of $\gamma_x$ consists of the classes of divisors with $c_x(D) \in \mathbb{Z}^r$. The order of $\Phi_x$ is $|\det M_x|$ by the Smith normal form of $M_x$. $\square$

*Theorem 2.3.12.* This is Lip69, Theorem 12.1, which is stated for a desingularization $Y_x = Y \times_X \operatorname{Spec} \mathcal{O}$ of the spectrum of a two-dimensional rational local ring: an invertible sheaf on $Y_x$ with nonnegative degree on every exceptional curve is generated by its global sections, and its first cohomology vanishes. The translation is by flat base change: $H^0(Y_x, \mathcal{L}) = (f_*\mathcal{L})_x$, so a global section on $Y_x$ that does not vanish at $y$ is the germ of a section of $f_*\mathcal{L}$ over some neighbourhood $U$ of $x$, that is, of a section of $\mathcal{L}$ over $f^{-1}(U)$. Lipman's proof uses the vanishing of $H^1(\mathcal{O}_Z)$ for positive cycles $Z$ supported on the fibre (Proposition P5.8.15). $\square$

*Theorem 2.3.13.* (1) Cartier implies numerically Cartier by Lemma 2.3.11. Conversely let $D$ be numerically Cartier at $x$. The coefficients of $f^*D$ on curves over other singular points may be fractional, so replace $f^*D$ by the divisor $B$ with integer coefficients that agrees with $f^*D$ except on the curves over $T_0 \setminus \{x\}$, where its coefficients are 0. Then $B$ agrees with $f^*D$ near $f^{-1}(x)$, so $B \cdot E_i = f^*D \cdot E_i = 0$ for $i \le r$. Let $\mathcal{L} = \mathcal{O}_Y(B)$, whose sections over an open $V$ are the rational functions $h$ with $\operatorname{div}_Y(h) + B \ge 0$ on $V$. Then $\mathcal{L} \cdot E_i = 0$, so by Theorem 2.3.12 there are $U \ni x$ and $h$ with $\Delta = \operatorname{div}_Y(h) + B$ effective on $f^{-1}(U)$ and not containing a chosen point $y \in E_1$.

The divisor $\Delta$ on $Y$ satisfies $\Delta \cdot E_i = B \cdot E_i = 0$ for $i \le r$, by Theorem P5.5.6. Write $\Delta = \Delta_E + \Delta_A + \Delta_N$, where $\Delta_E$ is the part supported on $E_1, \dots, E_r$, $\Delta_A$ the part supported on the other curves that meet $f^{-1}(x)$, and $\Delta_N$ the part supported on curves disjoint from $f^{-1}(x)$. A curve meeting $f^{-1}(x)$ meets the open set $f^{-1}(U)$, so its coefficient in $\Delta$ is nonnegative: $\Delta_E \ge 0$ and $\Delta_A \ge 0$. By Proposition P5.5.5, $\Delta_A \cdot E_i \ge 0$, so $\Delta_E \cdot E_i = -\Delta_A \cdot E_i \le 0$ for every $i \le r$. If $\Delta_E \ne 0$, then by Theorem P5.8.2 for the connected configuration $E_1, \dots, E_r$ every coefficient of $\Delta_E$ is positive, so $y \in E_1 \subset \operatorname{Supp} \Delta$, which is false. So $\Delta_E = 0$, and then $\Delta_A \cdot E_i = 0$ for every $i$. Each point of $\operatorname{Supp} \Delta_A \cap E_i$ contributes a positive local multiplicity to $\Delta_A \cdot E_i$ (Proposition P5.5.5), so $\Delta_A$ does not meet $f^{-1}(x)$, and by its definition $\Delta_A = 0$.

So $\operatorname{div}_Y(h) + B = \Delta_N$ with $\operatorname{Supp} \Delta_N$ disjoint from $f^{-1}(x)$. The morphism $f$ is proper, so $Z = f(\operatorname{Supp} \Delta_N) \cup (T_0 \setminus \{x\})$ is a closed set not containing $x$. Put $U' = X \setminus Z$. On $f^{-1}(U')$, $B = f^*D = -\operatorname{div}_Y(h)$. Applying $f_*$, which commutes with restriction to $U'$ and satisfies $f_*\operatorname{div}_Y(h) = \operatorname{div}_X(h)$ because $f$ is an isomorphism over $U' \setminus \{x\}$ and both sides are Weil divisors on $U'$, gives $D|_{U'} = \operatorname{div}_X(h^{-1})|_{U'}$. So $D$ is principal near $x$, and Cartier at $x$.

(2) By Lemma 2.3.11 and part 1, the kernel of $\gamma_x$ consists of the classes of divisors that are Cartier at $x$, which are 0 in $\operatorname{Cl}(\mathcal{O})$ by part 2 of Proposition P3.9.19. So $\gamma_x$ is injective, and $\operatorname{Cl}(\mathcal{O})$ is isomorphic to a subgroup of $\Phi_x$, whose order is $|\det M_x|$.

(3) By Lagrange's theorem, $|\det M_x| \cdot \gamma_x([D]) = 0$, so $|\det M_x| \, [\rho_x(D)] = 0$ by part 2, and $|\det M_x| D$ is Cartier at $x$ by part 2 of Proposition P3.9.19. By the same proposition the index $r_x(D)$ is the order of $[\rho_x(D)]$, which is the order of $\gamma_x([\rho_x(D)])$, the class of $c_x(D)$. $\square$

*Corollary 2.3.14.* At a smooth point every Weil divisor is Cartier (part 3 of Proposition P3.9.19). At $x_j$, $mD$ is Cartier by part 3 of Theorem 2.3.13, since $|\det M_{x_j}|$ divides $m$. By part 4 of Proposition P3.9.19, $mD$ is Cartier and $X$ is $\mathbb{Q}$-factorial. The Mumford pullback of the Cartier divisor $mD$ is its usual pullback (Corollary P5.8.5), and $f^*$ is linear, so $f^*D = \frac1m f^*(mD)$. $\square$

### Exercises

1. (A) Compute $\Phi_x$ for a single smooth rational curve $E$ with $E^2 = -n$, and show that the local class group of a point obtained by contracting it is $\mathbb{Z}/n$, generated by the image of a curve meeting $E$ transversally once.
2. (A) For two $(-2)$-curves meeting transversally once (the $A_2$ configuration), list the vectors $c_x(D)$ for $u_x(D) = (1, 0)$ and $(0, 1)$, and show that their classes are inverse to each other in $\Phi_x \cong \mathbb{Z}/3$.
3. (A) Let $x$ be a rational singularity and $D$ a Weil divisor with $u_x(D) \in M_x \mathbb{Z}^r$. Show that $D$ is Cartier at $x$.
4. (B) Let $X$ be a normal projective surface with rational singularities and $m$ as in Corollary 2.3.14. Show that $D \cdot D'$ is an integer when $D$ is Cartier, and that $m \, (D \cdot D') \in \mathbb{Z}$ for all Weil divisors $D, D'$. For $X_n$ of Example 2.3.15, show that $n$ is the least such integer.
5. (B) In Counterexample 2.3.18, show that $c_0(\ell_q - \ell_{q'}) = 0$, so that $\ell_q - \ell_{q'}$ is numerically Cartier at $0$. Show that it is Cartier at $0$ only if $q = q'$, and $\mathbb{Q}$-Cartier at $0$ only if $\mathcal{O}_V(q - q')$ is a torsion point of $\operatorname{Pic}^0(V)$.
6. (C) Let $x$ be a rational singularity, and suppose that for each $j$ there is an integral curve $\tilde C_j$ on $Y$ that meets $E_j$ transversally in one point and meets no other $E_i$. Show that $\gamma_x([f(\tilde C_j)])$ is the class of $-M_x^{-1} e_j$, that these classes generate $\Phi_x$, and conclude that $\gamma_x$ is an isomorphism $\operatorname{Cl}(\mathcal{O}_{X,x}) \cong \Phi_x$. (Lipman proves the isomorphism for every rational singularity with algebraically closed residue field, working on $\operatorname{Spec} \mathcal{O}_{X,x}$, where such curves exist.)

### Lean

Nothing in this section is in Lean. Mathlib has class groups of Dedekind domains, `ClassGroup`, but no Weil divisor class group of a normal Noetherian domain of dimension 2, and the project library has no rational singularities. The discriminant group of an integer matrix and the formula $|\mathbb{Z}^r / M\mathbb{Z}^r| = |\det M|$ are within reach of Mathlib's Smith normal form, `Submodule.smithNormalForm` over a principal ideal domain. The handbook adds no `MinimalModel` node here.

### Notes and history

Mumford (Mum61) observed that the local class group of a normal surface singularity maps to the discriminant group of the intersection matrix, and used the resulting finiteness when the local fundamental group is trivial. Artin (Art66) introduced rational singularities and proved the contractibility and rationality criteria of Theorem P5.8.16. Lipman (Lip69) proved the generation theorem (Theorem 12.1 there) and deduced that the local class group of a rational singularity is finite, isomorphic to the discriminant group $\mathbb{Z}^r / M\mathbb{Z}^r$ when the residue field is algebraically closed (Sections 14 to 17 there). He also showed that $E_8$ is the only two-dimensional rational singularity, other than a regular point, whose local ring is factorial (Section 25 there), a result that goes back to Brieskorn's work on the $E_8$ singularity as the quotient of $\mathbb{C}^2$ by the binary icosahedral group. The fact that dlt, and in particular klt, surface singularities are rational, so that Theorem 2.3.13 applies to all the singularities of the log minimal model program for surfaces, is in Section 3.
