---
title: Pairs and the discrepancy on one model
nodes: []
sources: [KM98, Kol13, Rei87]
reads_with: [KM98:ch2, Kol13:ch2]
requires: [P3.9, P3.12, P4.6, P8.13, 1.1]
level: core
kind: background
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Pairs and the discrepancy on one model

### Statement

In this volume $k$ is an algebraically closed field of characteristic 0, and a variety is an integral separated scheme of finite type over $k$. Let $X$ be a normal variety of dimension $n$. Its function field is $k(X)$, and $\Omega^n_{k(X)/k}$ is a vector space of dimension 1 over $k(X)$. An element of it is a *rational top form*.

Let $D$ be a prime divisor of $X$. Since $X$ is normal, the local ring $\mathcal{O}_{X,D}$ is a discrete valuation ring, and $X$ is smooth at the generic point of $D$. So $\Omega^n_{\mathcal{O}_{X,D}/k}$ is free of rank 1. For a nonzero rational top form $\omega$, let $\operatorname{ord}_D(\omega)$ be the largest integer $m$ with $\omega \in t^m \, \Omega^n_{\mathcal{O}_{X,D}/k}$, where $t$ is a uniformizer. In local coordinates $x_1, \dots, x_n$ at a general point of $D$, write $\omega = g \, dx_1 \wedge \dots \wedge dx_n$. Then $\operatorname{ord}_D(\omega) = \operatorname{ord}_D(g)$.

**Definition 4.1.1 (canonical divisor).** The *divisor* of a nonzero rational top form $\omega$ is $\operatorname{div}_X(\omega) = \sum_D \operatorname{ord}_D(\omega) \, D$, a finite sum over the prime divisors of $X$. A *canonical divisor* of $X$ is a divisor $K_X = \operatorname{div}_X(\omega)$ together with the form $\omega$.

Each other nonzero form is $h\omega$ with $h \in k(X)^*$, and $\operatorname{div}_X(h\omega) = \operatorname{div}_X(\omega) + \operatorname{div}_X(h)$. So the canonical divisors form one linear equivalence class, the canonical class (P3, Chapter 12). The handbook keeps the form $\omega$ in the data, because the discrepancy uses the same form on two models.

An *$\mathbb{R}$-divisor* is a finite sum $\Delta = \sum d_i D_i$ of prime divisors with real coefficients, and $\operatorname{mult}_{D_i} \Delta = d_i$. It is *$\mathbb{R}$-Cartier* if $\Delta = \sum_j r_j H_j$ with $r_j \in \mathbb{R}$ and $H_j$ Cartier divisors (Volume 1, Definition 1.1.6). Here a Cartier divisor is identified with its Weil divisor. On a normal variety this map is injective: a Cartier divisor with local equation $h$ and Weil divisor 0 has $h$ a unit at each prime divisor, so $h$ is a unit, because a normal noetherian domain is the intersection of its localizations at the primes of height 1 (P1, Chapter 8).

**Lemma 4.1.2 (the pullback of an $\mathbb{R}$-Cartier divisor).** Let $f \colon Y \to X$ be a dominant morphism of normal varieties. If $\sum_i r_i H_i = \sum_j s_j G_j$ as $\mathbb{R}$-divisors on $X$, with $H_i$ and $G_j$ Cartier, then $\sum_i r_i f^* H_i = \sum_j s_j f^* G_j$. So $f^* D = \sum_i r_i f^* H_i$ is well defined for each $\mathbb{R}$-Cartier divisor $D = \sum_i r_i H_i$.

Lean: not yet in Lean.

*Proof.* Let $V \subset \mathbb{R}^{p+q}$ be the set of $(x, y)$ with $\sum_i x_i H_i - \sum_j y_j G_j = 0$ as a Weil divisor. It is cut out by one linear equation for each prime divisor in the supports, and these equations have integer coefficients. So $V$ is spanned by the rational points $V \cap \mathbb{Q}^{p+q}$. The map $V \to \operatorname{Div}_{\mathbb{R}}(Y)$, $(x, y) \mapsto \sum_i x_i f^*H_i - \sum_j y_j f^*G_j$, is $\mathbb{R}$-linear. Let $(x, y)$ be a rational point of $V$, and clear denominators. Then $\sum_i n_i H_i - \sum_j m_j G_j$ is a Cartier divisor with Weil divisor 0. By injectivity it is the zero Cartier divisor, so its pullback is 0. So the linear map vanishes on a spanning set of $V$, and so on $V$. $\square$

**Definition 4.1.3 (pair and sub-pair).** A *sub-pair* $(X, \Delta)$ is a normal variety $X$ and an $\mathbb{R}$-divisor $\Delta$ such that $K_X + \Delta$ is $\mathbb{R}$-Cartier. It is a *pair* if $\Delta$ is effective. A pair is a *boundary pair* if every coefficient of $\Delta$ lies in $[0, 1]$.

The condition does not depend on the choice of $K_X$, since two choices differ by a principal divisor. If $X$ is $\mathbb{Q}$-factorial, every $(X, \Delta)$ is a sub-pair. KM98, Chapter 2, allows coefficients of any sign. This volume needs sub-pairs, because the crepant pullback of a pair to a resolution is a sub-pair (Proposition 4.1.14).

Let $f \colon Y \to X$ be a proper birational morphism of normal varieties. Then $k(Y) = k(X)$, so a rational top form $\omega$ on $X$ is also one on $Y$. The map $f$ is an isomorphism over an open set $U \subset X$ whose complement has codimension at least 2, because a rational map from a normal variety to a variety proper over $X$ is defined in codimension 1 (P4, Chapter 6). A prime divisor $E$ of $Y$ is *$f$-exceptional* if $f(E)$ has codimension at least 2.

**Definition 4.1.4 (discrepancy on a model).** Let $(X, \Delta)$ be a sub-pair, $K_X = \operatorname{div}_X(\omega)$, and $f \colon Y \to X$ a proper birational morphism from a normal variety. Put $K_Y = \operatorname{div}_Y(\omega)$ with the same $\omega$, and define the $\mathbb{R}$-divisor $\Delta_Y$ by

$$K_Y + \Delta_Y = f^*(K_X + \Delta).$$

For a prime divisor $E$ of $Y$, the *discrepancy* of $E$ is $a(E, X, \Delta) = -\operatorname{mult}_E \Delta_Y$. The *log discrepancy* is $A(E, X, \Delta) = a(E, X, \Delta) + 1$.

On the open set $f^{-1}(U)$ the map $f$ is an isomorphism, so $\Delta_Y$ and $\Delta$ agree there, and $f_* \Delta_Y = \Delta$. So for the strict transform $E$ of a prime divisor $D$ of $X$, $a(E, X, \Delta) = -\operatorname{mult}_D \Delta$. The discrepancies of the $f$-exceptional divisors are the new information. When $K_X$ and $\Delta$ are $\mathbb{Q}$-Cartier one often writes $K_Y = f^*(K_X + \Delta) + \sum_E a(E, X, \Delta) E$, where the sum runs over all prime divisors of $Y$ and the strict transform of $\Delta$ appears with the coefficients $-\operatorname{mult}_D\Delta$.

**Lemma 4.1.5 (the choice of the form).** The divisor $\Delta_Y$, and so each $a(E, X, \Delta)$, does not depend on the choice of $\omega$.

Lean: not yet in Lean.

*Proof.* Replace $\omega$ by $h \omega$. Then $K_X$ becomes $K_X + \operatorname{div}_X(h)$ and $K_Y$ becomes $K_Y + \operatorname{div}_Y(h)$. The pullback of the principal Cartier divisor $\operatorname{div}_X(h)$ is $\operatorname{div}_Y(f^* h) = \operatorname{div}_Y(h)$. So both sides of $K_Y + \Delta_Y = f^*(K_X + \Delta)$ change by $\operatorname{div}_Y(h)$, and $\Delta_Y$ does not change. $\square$

The discrepancy box of Volume 0, Chapter 3, fixes these conventions for the whole handbook. The rest of the volume writes $a$ for the discrepancy and $A = a + 1$ for the log discrepancy, and never mixes them.

### Examples

**Example 4.1.6 (the blow-up of a smooth point).** Let $X = \mathbb{A}^n$ with $n \ge 2$, $\Delta = 0$ and $\omega = dx_1 \wedge \dots \wedge dx_n$, so $K_X = 0$. Let $f \colon Y \to X$ be the blow-up of the origin, with exceptional divisor $E \cong \mathbb{P}^{n-1}$. In the chart $x_1 = y_1$, $x_i = y_1 y_i$ for $i \ge 2$, the divisor $E$ is $\{y_1 = 0\}$ and

$$dx_1 \wedge dx_2 \wedge \dots \wedge dx_n = dy_1 \wedge (y_2 \, dy_1 + y_1 \, dy_2) \wedge \dots \wedge (y_n \, dy_1 + y_1 \, dy_n) = y_1^{n-1} \, dy_1 \wedge \dots \wedge dy_n.$$

So $K_Y = (n-1) E$, $\Delta_Y = -(n-1)E$, and $a(E, \mathbb{A}^n, 0) = n - 1$. The log discrepancy is $n$.

**Example 4.1.7 (a smooth centre).** Let $Z = \{x_1 = \dots = x_c = 0\} \subset \mathbb{A}^n$ with $c \ge 2$, and let $f$ be the blow-up of $Z$. The chart $x_1 = y_1$, $x_i = y_1 y_i$ for $2 \le i \le c$, $x_i = y_i$ for $i > c$ gives $\omega = y_1^{c-1} \, dy_1 \wedge \dots \wedge dy_n$, so $a(E_Z, \mathbb{A}^n, 0) = c - 1$. A codimension 2 centre gives $a = 1$, the smallest discrepancy that a blow-up of a smooth variety can give.

**Example 4.1.8 (the $A_1$ singularity).** Let $X = \{xy = z^2\} \subset \mathbb{A}^3$, the quadric cone. Write $F = xy - z^2$. On $X$ the relation $y \, dx + x \, dy - 2z \, dz = 0$ gives

$$\omega = \frac{dx \wedge dz}{x} = -\frac{dy \wedge dz}{y} = \frac{dx \wedge dy}{2z}.$$

This is the residue form $dx \wedge dy \wedge dz / dF$. Where $x \ne 0$ the functions $x, z$ are coordinates on $X$, and $\omega$ is a generator of $\Omega^2_X$ there. The same holds where $y \ne 0$ or $z \ne 0$. So $\omega$ generates $\Omega^2$ on $X \setminus \{0\}$, every prime divisor has $\operatorname{ord}_D(\omega) = 0$, and $K_X = \operatorname{div}_X(\omega) = 0$. Blow up the origin. In the chart $x = u$, $y = uv$, $z = uw$ of the blow-up of $\mathbb{A}^3$, the equation becomes $u^2(v - w^2) = 0$, so the strict transform $Y$ is $v = w^2$, smooth with coordinates $u, w$, and the exceptional curve $E$ is $\{u = 0\}$. Then $x = u$, $z = uw$, and

$$\omega = \frac{du \wedge (w \, du + u \, dw)}{u} = du \wedge dw.$$

So $\operatorname{ord}_E(\omega) = 0$, $K_Y = 0$ near $E$, and $a(E, X, 0) = 0$. The $A_1$ singularity has discrepancy 0. Volume 1, Section 1.1, finds the same number by adjunction, and Volume 3, Example 3.3.38, finds it from the fan.

**Example 4.1.9 (a line and two lines in the plane).** Let $X = \mathbb{A}^2$, $L = \{x = 0\}$, and $\Delta = cL$. Blow up the origin. In the chart $x = u$, $y = uv$, the form is $dx \wedge dy = u \, du \wedge dv$, so $K_Y = E$ on this chart, and $f^*L = \operatorname{div}(u) = E$ there. On the other chart $x = u'v'$, $y = v'$, $f^* L = L' + E$ with $L' = \{u' = 0\}$ the strict transform. So $f^*(K_X + cL) = cL' + cE$ and

$$\Delta_Y = cL' + cE - E = cL' + (c - 1) E, \qquad a(E, \mathbb{A}^2, cL) = 1 - c.$$

For two lines $L_1 + L_2$ through the origin, $f^*(L_1 + L_2) = L_1' + L_2' + 2E$, and $a(E, \mathbb{A}^2, c(L_1 + L_2)) = 1 - 2c$. For $c = 1$ this is $-1$.

**Counterexample 4.1.10 (a plane through the vertex of $xz = yw$).** Let $X = \{xz = yw\} \subset \mathbb{A}^4$, the cone over a smooth quadric surface, and let $D = \{x = y = 0\}$, a plane in $X$. The residue form of Example 4.1.8 gives $K_X = 0$, so $K_X$ is Cartier. Volume 3, Example 3.3.18, shows that no multiple $mD$ with $m \ne 0$ is Cartier, and Volume 3, Example 3.3.23, shows that $X$ is not $\mathbb{Q}$-factorial. By Exercise 3 below, $cD$ is not $\mathbb{R}$-Cartier for any real $c \ne 0$. So $(X, cD)$ is not a sub-pair for $c \ne 0$, the pullback $f^*(K_X + cD)$ has no meaning, and no discrepancy of $(X, cD)$ is defined.

### Exercises

1. (A) Let $X = \mathbb{A}^3$, $\ell = \{x = y = 0\}$ a line, and $H = \{x = 0\}$ a plane through $\ell$. Compute $a(E_\ell, X, cH)$ for the exceptional divisor of the blow-up of $\ell$.
2. (A) Let $X = \{xy = z^{n+1}\} \subset \mathbb{A}^3$. Show that the residue form $dx \wedge dz / x$ generates $\Omega^2$ on $X \setminus \{0\}$, so that $K_X = 0$.
3. (B) Let $D$ be a Weil divisor on a normal variety and $c \ne 0$ a real number. Show that if $cD$ is $\mathbb{R}$-Cartier, then $D$ is $\mathbb{Q}$-Cartier. Use the rational points of the space of relations, as in the proof of Lemma 4.1.2.
4. (B) Let $X$ be a smooth surface, $p \in X$, and $D$ a curve with multiplicity $m$ at $p$. Show that the blow-up of $p$ gives $a(E, X, cD) = 1 - cm$.
5. (B) Let $X = \{xy = z^{n+1}\}$ with $n \ge 2$. Show that the exceptional locus of the blow-up of the origin is two lines, that each has discrepancy 0, and that the blow-up has one singular point, of type $xy = z^{n-1}$, when $n \ge 3$. For $n = 2$ the blow-up is smooth.

### Lean

The definitions of this section are in the project library. `MinimalModel.TopForm` is the space of rational top forms, `MinimalModel.formLattice` is the lattice of forms that are regular on a subring, and `MinimalModel.IsDivOfForm` says that a divisor is the divisor of a form. `MinimalModel.CanonicalDivisor` holds a divisor $K$ and a form $\omega$ with $K = \operatorname{div}(\omega)$, as in Definition 4.1.1. `MinimalModel.IsRCartier` is the $\mathbb{R}$-span of the Cartier divisors. `MinimalModel.Pair` holds a canonical divisor, an effective $\Delta$, and the condition that $K + \Delta$ is $\mathbb{R}$-Cartier, and `MinimalModel.Pair.KΔ` is $K + \Delta$. The library has no sub-pairs: its $\Delta$ is effective. The discrepancy on one model is not in Lean. The library defines the log discrepancy of a valuation directly, by the formula of Section 2.

### Notes and history

The discrepancy appears in Reid's papers on canonical 3-folds of 1980 and on minimal models of 3-folds of 1983, for $\Delta = 0$. The boundary $\Delta$ came from the log category of Iitaka and from Kawamata and Shokurov in the 1980s. The definitions here follow KM98, Chapter 2, and Kol13, Chapter 2. Some authors write $K_Y = f^*K_X + \sum a_E E$ with the same sign and some write the log discrepancy $A = a + 1$ throughout. The Lean library uses $A$, and this volume gives both.
