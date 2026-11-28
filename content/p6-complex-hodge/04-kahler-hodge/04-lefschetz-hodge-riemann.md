---
title: Hard Lefschetz and the Hodge-Riemann relations
nodes: []
sources: [Huy05, Voi02, GH78, Wel80, Lef24, Hod41, BT82]
reads_with: [Huy05:3.3, Voi02:6, Voi02:7, GH78:0.7, Wel80:V]
requires: [P5.5, P6.2, P6.3]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Hard Lefschetz and the Hodge-Riemann relations

### Statement

Let $(X, \omega)$ be a compact Kähler manifold of dimension $n$. Write $L \colon H^k(X, \mathbb{R}) \to H^{k+2}(X, \mathbb{R})$ for the cup product with $[\omega]$, induced by $\alpha \mapsto \omega \wedge \alpha$ on closed forms, and use the same letter on $H^k(X, \mathbb{C})$. Since $\omega$ is a real $(1,1)$-form, $L$ maps $H^{p,q}(X)$ to $H^{p+1,q+1}(X)$ (Theorem P6.4.16).

**Theorem P6.4.21 (hard Lefschetz theorem).** Let $(X, \omega)$ be a compact Kähler manifold of dimension $n$ and $k \leq n$.

1. $L^{n-k} \colon H^k(X, \mathbb{R}) \to H^{2n-k}(X, \mathbb{R})$ is an isomorphism. In particular $L^j \colon H^{k-2j}(X, \mathbb{R}) \to H^{k}(X, \mathbb{R})$ is injective for $j \geq 0$ and $b_{k-2} \leq b_k$ for $2 \leq k \leq n$.
2. Let $\alpha$ be a harmonic $k$-form. Then $L^{n-k+1}[\alpha] = 0$ if and only if $\alpha$ is primitive at every point (Definition P6.4.8).
3. $H^k(X, \mathbb{R}) = L H^{k-2}(X, \mathbb{R}) \oplus \ker(L^{n-k+1} \colon H^k(X, \mathbb{R}) \to H^{2n-k+2}(X, \mathbb{R}))$.

Lean: not yet in Lean.

**Definition P6.4.22 (primitive cohomology and the Hodge-Riemann form).** Let $(X, \omega)$ be a compact Kähler manifold of dimension $n$ and $k \leq n$. The *primitive cohomology* is
$$P^k(X) = \ker(L^{n-k+1} \colon H^k(X, \mathbb{R}) \to H^{2n-k+2}(X, \mathbb{R})),$$
with complexification $P^k(X)_{\mathbb{C}}$ and $P^{p,q}(X) = P^k(X)_{\mathbb{C}} \cap H^{p,q}(X)$ for $p + q = k$. The *Hodge-Riemann form* on $H^k(X, \mathbb{R})$ is
$$Q(a, b) = (-1)^{k(k-1)/2} \int_X \omega^{n-k} \wedge \alpha \wedge \beta, \qquad a = [\alpha], \ b = [\beta],$$
extended complex bilinearly to $H^k(X, \mathbb{C})$. It is well defined by Stokes, since $d\omega = 0$, and $Q(b, a) = (-1)^k Q(a, b)$.

Since $L$ shifts the type by $(1,1)$, $L^{n-k+1}$ maps each $H^{p,q}$ to a different summand of $H^{2n-k+2}(X, \mathbb{C})$, so $P^k(X)_{\mathbb{C}} = \bigoplus_{p+q=k} P^{p,q}(X)$, and conjugation maps $P^{p,q}(X)$ onto $P^{q,p}(X)$. Applying part 3 of Theorem P6.4.21 to $k, k-2, \dots$ gives the *Lefschetz decomposition* $H^k(X, \mathbb{R}) = \bigoplus_{j \geq 0} L^j P^{k-2j}(X)$ for $k \leq n$, with each $L^j$ injective on $P^{k-2j}(X)$. By part 1 this transports to degrees $2n - k \geq n$ through $L^{n-k}$. By part 2, the harmonic representative of a primitive class is a primitive form.

**Theorem P6.4.23 (Hodge-Riemann bilinear relations).** Let $(X, \omega)$ be a compact Kähler manifold of dimension $n$, $k \leq n$ and $p + q = k$.

1. $Q(H^{p,q}(X), H^{p',q'}(X)) = 0$ unless $(p', q') = (q, p)$.
2. For every nonzero $a \in P^{p,q}(X)$, $i^{p-q} Q(a, \bar a) > 0$. More precisely, if $\alpha$ is the harmonic representative of $a$ for the metric of $\omega$, then $i^{p-q}Q(a, \bar a) = (n-k)!\,\|\alpha\|^2$.
3. If $a \in P^{k-2j}(X)$ and $b \in P^{k-2l}(X)$ with $j \neq l$, then $Q(L^j a, L^l b) = 0$, so the Lefschetz decomposition of $H^k(X, \mathbb{R})$ is $Q$-orthogonal.

Lean: not yet in Lean.

**Corollary P6.4.24 (the Hodge index theorem for compact Kähler surfaces).** Let $X$ be a compact connected Kähler surface with Kähler form $\omega$, and consider the intersection form $(a, b) \mapsto a \cdot b = \int_X \alpha \wedge \beta$ on $H^2(X, \mathbb{R})$. Let $H^{1,1}_{\mathbb{R}}(X) = H^{1,1}(X) \cap H^2(X, \mathbb{R})$, of real dimension $h^{1,1}$.

1. The intersection form on $H^{1,1}_{\mathbb{R}}(X)$ has signature $(1, h^{1,1} - 1)$. If $a \in H^{1,1}_{\mathbb{R}}(X)$ and $a \cdot [\omega] = 0$, then $a^2 \leq 0$, with equality only for $a = 0$.
2. The intersection form on $H^2(X, \mathbb{R})$ has signature $(1 + 2h^{2,0}, h^{1,1} - 1)$, so its signature in the sense of topology is $\sigma(X) = 2 + 2h^{2,0} - h^{1,1}$.

Lean: not yet in Lean.

### Proof in words

The Kähler identities give $[L, \Delta_d] = 0$, so $L$ maps harmonic forms to harmonic forms. Each harmonic class has a unique harmonic representative, so the cohomology statements reduce to pointwise linear algebra, which Section 4.2 has already done. Pointwise, $L^{n-k}$ is an isomorphism on $k$-forms. So $L^{n-k}$ is injective on harmonic $k$-forms, and Poincaré duality, $b_k = b_{2n-k}$, makes it bijective. The decomposition $H^k = LH^{k-2} \oplus P^k$ is then a statement about one linear map, and the harmonic representative of a primitive class is primitive because $L^{n-k+1}\alpha$ is harmonic and exact, hence zero.

The Hodge-Riemann relations are Weil's formula integrated. For a primitive harmonic $(p,q)$-form $\alpha$, Weil's formula computes $*\bar\alpha$ as a multiple of $\omega^{n-k} \wedge \bar\alpha$. So $\|\alpha\|^2 = \int \alpha \wedge *\bar\alpha$ is a constant times $\int \omega^{n-k} \wedge \alpha \wedge \bar\alpha$. The sign $(-1)^{k(k-1)/2}$ in $Q$ and the factor $i^{p-q}$ cancel the constant, so the result is positive.

For a surface, $H^2 = \mathbb{R}[\omega] \oplus P^2$. On $P^2$ the form $Q$ is minus the intersection form, so the intersection form is positive on the real part of $H^{2,0} \oplus H^{0,2}$ and negative on the primitive $(1,1)$-classes. Counting dimensions gives the index formula. The examples compute Hodge diamonds. They check the signs on an abelian surface with explicit forms, and show that hard Lefschetz fails for a closed semipositive class that is not Kähler.

### Examples

**Example P6.4.25 (projective space).** By Example P6.2.31, $b_{2k}(\mathbb{P}^n) = 1$ for $0 \leq k \leq n$ and the odd Betti numbers vanish. By Corollary P6.4.17, $h^{k,k} \geq 1$ and $b_{2k} = \sum_{p+q=2k} h^{p,q}$, so $h^{p,q}(\mathbb{P}^n) = \delta_{pq}$. In particular $H^0(\mathbb{P}^n, \Omega^p) = 0$ for $p \geq 1$, and $H^q(\mathbb{P}^n, \mathcal{O}) = 0$ for $q \geq 1$. With $h = [\omega_{FS}]$, $H^{2k} = \mathbb{R}h^k$ (Example P6.3.29), and $L^{n-2k}$ maps $h^k$ to $h^{n-k}$, which is nonzero since $\int h^n = 1$. So hard Lefschetz holds, $P^0 = \mathbb{R}$, and $P^k = 0$ for $k > 0$. For $n = 2$, $\sigma(\mathbb{P}^2) = 2 + 0 - 1 = 1$, in agreement with $h^2 \cdot h^2 = 1 > 0$ on $H^2 = \mathbb{R}h$.

**Example P6.4.26 (compact Riemann surfaces and plane curves).** Let $X$ be a compact connected Riemann surface. It is Kähler (Example P6.4.3), and $h^{0,0} = h^{1,1} = 1$. Put $g = h^{1,0} = \dim H^0(X, K_X)$. Hodge symmetry gives $h^{0,1} = g$ and $b_1 = 2g$, so $\chi_{\mathrm{top}}(X) = 2 - 2g$, and $g$ is the topological genus. Every class in $H^1$ is $L$-primitive for degree reasons, and $Q(a, b) = \int_X \alpha \wedge \beta$. Part 2 of Theorem P6.4.23 for $(p, q) = (1, 0)$ says $i\int_X \alpha \wedge \bar\alpha > 0$ for a holomorphic $1$-form $\alpha \neq 0$. Locally, with $\alpha = f\, dz$ and $dz \wedge d\bar z = -2i\, dx \wedge dy$, the integrand is $2|f|^2\, dx \wedge dy$. For $(p, q) = (0, 1)$ the relation reads $-i\int \bar\alpha \wedge \alpha > 0$, the same inequality.

Let $C \subset \mathbb{P}^2$ be a smooth plane curve of degree $d$. It is connected, by the Lefschetz hyperplane theorem, cited from Griffiths and Harris, Chapter 1 (GH78). By Example P6.3.31 and the Gauss-Bonnet theorem, $\chi_{\mathrm{top}}(C) = d(3 - d)$, so
$$h^{1,0}(C) = g = \frac{2 - d(3 - d)}{2} = \frac{(d-1)(d-2)}{2}.$$
Lines and conics have $g = 0$, cubics $g = 1$, quartics $g = 3$. For a cubic, $K_C \cong \mathcal{O}_C$ (Example P6.2.20), so $H^0(C, K_C) \cong H^0(C, \mathcal{O}_C) = \mathbb{C}$, in agreement with $g = 1$.

**Example P6.4.27 (Hodge diamonds of surfaces).** Write the Hodge diamond of a surface with $h^{0,0}$ at the top and $h^{2,2}$ at the bottom.

1. *Abelian surfaces.* For $X = \mathbb{C}^2/\Lambda$, Example P6.4.20 gives $h^{p,q} = \binom{2}{p}\binom{2}{q}$, so the rows are $1$; $2, 2$; $1, 4, 1$; $2, 2$; $1$. Then $\sigma = 2 + 2 - 4 = 0$. This agrees with topology, since the wedge pairing on $\Lambda^2(\mathbb{R}^4)^*$ is hyperbolic. The signs can be checked with explicit forms for $\omega_0 = \frac{i}{2}(dz_1 \wedge d\bar z_1 + dz_2 \wedge d\bar z_2)$, writing $\mu = dz_1 \wedge d\bar z_1 \wedge dz_2 \wedge d\bar z_2 = -4\, dx_1 \wedge dy_1 \wedge dx_2 \wedge dy_2$. Then $\omega_0^2 = -\frac12\mu$, which is positive, as it should be. For $a = dz_1 \wedge dz_2 \in H^{2,0}$, $a \wedge \bar a = -\mu$ is positive, so $(a + \bar a)^2 = 2\int a \wedge \bar a > 0$. For the primitive $(1,1)$-form $c = dz_1 \wedge d\bar z_2$, $\omega_0 \wedge c = 0$ and $c \wedge \bar c = \mu$ is negative. So $i^0 Q(c, \bar c) = -\int_X c \wedge \bar c = 4\operatorname{vol}(X)$, and this is $(2-2)!\,\|c\|^2 = \langle dz_1, dz_1 \rangle \langle d\bar z_2, d\bar z_2 \rangle \operatorname{vol}(X)$, exactly as in Theorem P6.4.23, part 2.
2. *Products of curves.* Let $C_g$ and $C_h$ be compact connected Riemann surfaces of genus $g$ and $h$, and $X = C_g \times C_h$, Kähler by Proposition P6.4.4. By the Künneth formula (BT82, Chapter I), the classes $p_1^*a \cup p_2^*b$, with $a$ and $b$ running over bases of $H^*(C_g, \mathbb{C})$ and $H^*(C_h, \mathbb{C})$, form a basis of $H^*(X, \mathbb{C})$. If $a$ and $b$ are represented by closed forms of types $(r, s)$ and $(t, u)$, then $p_1^*a \cup p_2^*b$ is represented by a closed form of type $(r + t, s + u)$. Choose the bases adapted to the Hodge decompositions of the factors. These products span a subspace of $H^{p,q}(X)$ of dimension $\sum h^{r,s}(C_g)h^{t,u}(C_h)$, summed over $r + t = p$ and $s + u = q$. Summed over $(p, q)$ the subspaces fill $H^*(X, \mathbb{C})$, and the $H^{p,q}(X)$ are independent, so each is exactly $H^{p,q}(X)$. Hence $h^{1,0} = g + h$, $h^{2,0} = gh$ and $h^{1,1} = 1 + 1 + gh + hg = 2 + 2gh$, and $\sigma = 2 + 2gh - 2 - 2gh = 0$. For $g = h = 1$ this is the abelian surface above.
3. *Quartic surfaces.* Let $X \subset \mathbb{P}^3$ be a smooth quartic, Kähler by Proposition P6.4.4. By Example P6.2.20, $K_X \cong \mathcal{O}_X$ and $N_{X/\mathbb{P}^3} \cong \mathcal{O}_X(4)$. Cite from GH78, Chapter 1, that $X$ is connected and $b_1(X) = 0$ (Lefschetz hyperplane theorem), and that $\int_X h^2 = 4$ for $h = [\omega_{FS}]|_X$ (a general line meets $X$ in $4$ points). Then $h^{0,0} = 1$, $h^{1,0} = h^{0,1} = 0$, and $h^{2,0} = \dim H^0(X, K_X) = \dim H^0(X, \mathcal{O}_X) = 1$. The exact sequence $0 \to T_X \to T_{\mathbb{P}^3}|_X \to \mathcal{O}_X(4) \to 0$ of Proposition P6.2.19, the Whitney formula and Example P6.3.30 give
$$c(T_X) = \frac{(1 + h)^4}{1 + 4h} = (1 + 4h + 6h^2)(1 - 4h + 16h^2) = 1 + 6h^2,$$
so $c_1(T_X) = 0$ and $\int_X c_2(T_X) = 24$. By Gauss-Bonnet, $24 = \chi_{\mathrm{top}}(X) = 2 + b_2$, since $b_3 = b_1 = 0$ by Poincaré duality. So $b_2 = 22 = 2h^{2,0} + h^{1,1}$, which gives $h^{1,1} = 20$, the diamond $1$; $0, 0$; $1, 20, 1$; $0, 0$; $1$, and $\sigma = 2 + 2 - 20 = -16$.

**Example P6.4.28 (a class that is not Kähler).** On $X = \mathbb{P}^1 \times \mathbb{P}^1$ with projections $p_1$ and $p_2$, let $a = p_1^*\omega_{FS}$ and $b = p_2^*\omega_{FS}$. Both are closed real $(1,1)$-forms that are semipositive, and $a + b$ is a Kähler form by Proposition P6.4.4. By Künneth, $H^2(X, \mathbb{R}) = \mathbb{R}[a] \oplus \mathbb{R}[b]$, with $a^2 = 0$ as a form, since it is pulled back from a $4$-form on $\mathbb{P}^1$, and similarly $b^2 = 0$, and $\int_X a \wedge b = (\int_{\mathbb{P}^1}\omega_{FS})^2 = 1$. Replace $[\omega]$ by $[a]$ in the definition of $L$. Then $L_a^2 \colon H^0(X, \mathbb{R}) \to H^4(X, \mathbb{R})$ is zero, so hard Lefschetz fails for $[a]$, and $Q(1, 1) = \int_X a^2 = 0$ violates part 2 of Theorem P6.4.23 for $P^0$. The class $[a]$ is not the class of any Kähler form $\omega'$, since $\int_X \omega'^2 > 0$ by Proposition P6.4.5. The intersection form on $H^2$ is $(xa + yb)^2 = 2xy$, of signature $(1, 1)$, in agreement with Corollary P6.4.24 for $h^{1,1} = 2$, $h^{2,0} = 0$. The Kähler class $a + b$ has square $2 > 0$, and the class $a - b$ orthogonal to it has square $-2 < 0$. This is the real form $\alpha$ of Example P6.3.10.

### Proof

*Theorem P6.4.21.* (1) By Theorem P6.4.12, part 4, $L$ commutes with $\Delta_d$, so $L^{n-k}$ maps $\mathcal{H}^k(X)$ into $\mathcal{H}^{2n-k}(X)$. Under the isomorphisms $\mathcal{H}^j(X) \cong H^j(X, \mathbb{C})$ of Corollary P6.4.15 this is $L^{n-k}$ on cohomology. By Theorem P6.4.9, part 4, at each point $L^{n-k} \colon \Lambda^k \to \Lambda^{2n-k}$ is an isomorphism, so $L^{n-k}$ is injective on forms and on $\mathcal{H}^k(X)$. Since $b_k = b_{2n-k}$ (Corollary P6.4.15), it is an isomorphism. The map is real, so this holds over $\mathbb{R}$. If $L^j a = 0$ with $a \in H^{k-2j}$, then $L^{n-k+2j}a = L^{n-k+j}L^ja = 0$, so $a = 0$ by the case $k - 2j$.

(2) The form $L^{n-k+1}\alpha$ is harmonic, so it represents zero if and only if it vanishes. By Theorem P6.4.9, part 5, it vanishes if and only if $\alpha$ is primitive at every point.

(3) Let $c \in H^k$. By part 1 for $k - 2$, $L^{n-k+2} \colon H^{k-2} \to H^{2n-k+2}$ is onto, so $L^{n-k+1}c = L^{n-k+2}b$ for some $b \in H^{k-2}$. Then $c - Lb$ lies in the kernel of $L^{n-k+1}$, and $c = Lb + (c - Lb)$. If $Lb$ lies in the kernel, then $L^{n-k+2}b = 0$, so $b = 0$ by part 1. For $k < 2$, $H^{k-2} = 0$ and the claim is that $L^{n-k+1} = 0$ on $H^k$, which holds since $2n - k + 2 > 2n$.

*Theorem P6.4.23.* (1) Represent the classes by $d$-closed forms $\alpha$ and $\beta$ of types $(p, q)$ and $(p', q')$. The form $\omega^{n-k} \wedge \alpha \wedge \beta$ has type $(n - k + p + p', n - k + q + q')$, and its integral vanishes unless the type is $(n, n)$, that is, $p' = k - p = q$ and $q' = p$.

(2) Let $a \in P^{p,q}(X)$ be nonzero and $\alpha$ its harmonic representative. By Theorem P6.4.16, part 4, $\alpha$ has type $(p, q)$, and by Theorem P6.4.21, part 2, it is primitive at every point. Since $\Delta_d$ is a real operator, $\bar\alpha$ is the harmonic representative of $\bar a$, of type $(q, p)$ and primitive. Write $\varepsilon_k = (-1)^{k(k+1)/2}$. Weil's formula (Proposition P6.4.10, part 3) with $j = 0$, and $\mathbf{I}(\bar\alpha) = i^{q-p}\bar\alpha$, give
$$*\bar\alpha = \frac{\varepsilon_k\, i^{q-p}}{(n-k)!}\, \omega^{n-k} \wedge \bar\alpha.$$
By the definition of $*$ (Definition P6.4.7), $\alpha \wedge *\bar\alpha = |\alpha|^2 \operatorname{vol}$, and $\omega^{n-k}$ has even degree, so
$$\|\alpha\|^2 = \int_X \alpha \wedge *\bar\alpha = \frac{\varepsilon_k\, i^{q-p}}{(n-k)!}\int_X \omega^{n-k} \wedge \alpha \wedge \bar\alpha = \frac{\varepsilon_k (-1)^{k(k-1)/2}\, i^{q-p}}{(n-k)!}\, Q(a, \bar a).$$
Now $\varepsilon_k(-1)^{k(k-1)/2} = (-1)^{k^2} = (-1)^k$ and $i^{q-p} = (-1)^{p-q}\, i^{p-q}$, with $(-1)^{k + p - q} = (-1)^{2p} = 1$. So $\|\alpha\|^2 = i^{p-q}Q(a, \bar a)/(n-k)!$, which is positive because $\alpha \neq 0$.

(3) Say $j < l$, and let $\alpha$ be the primitive harmonic representative of $a$, of degree $k - 2j$. Then $Q(L^ja, L^lb)$ is $\pm\int_X \omega^{n-k+j+l} \wedge \alpha \wedge \beta$. Since $n - k + j + l \geq n - (k - 2j) + 1$, Theorem P6.4.9, part 2, gives $\omega^{n-k+j+l} \wedge \alpha = 0$. The case $j > l$ follows from $Q(b, a) = \pm Q(a, b)$.

*Corollary P6.4.24.* Here $n = 2$. Since $X$ is connected, $H^0(X, \mathbb{R}) = \mathbb{R}$, and $H^4(X, \mathbb{R}) \cong \mathbb{R}$ through $\int_X$ by Corollary P6.4.15, part 3. So $P^2(X) = \{a \in H^2 : a \cdot [\omega] = 0\}$, and Theorem P6.4.21, part 3, gives $H^2(X, \mathbb{R}) = \mathbb{R}[\omega] \oplus P^2(X)$ with $[\omega]^2 > 0$ (Proposition P6.4.5). On $H^2$, $Q(a, b) = -a \cdot b$. A class in $H^{2,0}$ is primitive, since $L$ maps it to $H^{3,1} = 0$, so $P^2(X)_{\mathbb{C}} = H^{2,0} \oplus P^{1,1} \oplus H^{0,2}$. The real subspace $W = \{a + \bar a : a \in H^{2,0}\}$ has dimension $2h^{2,0}$, and $P^2(X) = W \oplus P^{1,1}_{\mathbb{R}}$ with $\dim P^{1,1}_{\mathbb{R}} = h^{1,1} - 1$. For $a \in H^{2,0}$ nonzero, $a \cdot a = 0$ by type, so $(a + \bar a)^2 = 2\,a \cdot \bar a = 2\,i^2 Q(a, \bar a) > 0$ by Theorem P6.4.23, part 2. So the form is positive definite on $W$. For $c \in P^{1,1}_{\mathbb{R}}$ nonzero, $\bar c = c$ and $c^2 = -Q(c, \bar c) < 0$. The spaces $\mathbb{R}[\omega]$, $W$ and $P^{1,1}_{\mathbb{R}}$ are pairwise orthogonal: $[\omega]$ is orthogonal to $P^2$ by definition, and $W$ is orthogonal to $P^{1,1}_{\mathbb{R}}$ by Theorem P6.4.23, part 1. This proves part 2. Restricted to $H^{1,1}_{\mathbb{R}} = \mathbb{R}[\omega] \oplus P^{1,1}_{\mathbb{R}}$, the form has signature $(1, h^{1,1} - 1)$, and a class $a \in H^{1,1}_{\mathbb{R}}$ with $a \cdot [\omega] = 0$ lies in $P^{1,1}_{\mathbb{R}}$. $\square$

### Exercises

1. (A) Let $X$ be a compact Kähler manifold of dimension $n$. Show that $h^{p-1,q-1} \leq h^{p,q}$ for $p + q \leq n$. Show that $S^2 \times S^4$, with $b_2 = 1$ and $b_4 = 1$, passes this test, and that $S^3 \times S^3$ carries no Kähler structure.
2. (A) On a compact Riemann surface of genus $g$ show that $(a, b) \mapsto \int a \wedge b$ is a symplectic form on $H^1(X, \mathbb{R})$ and that $H^{1,0}$ is a Lagrangian subspace of $H^1(X, \mathbb{C})$ on which $i\int \alpha \wedge \bar\beta$ is positive definite Hermitian.
3. (B) On the abelian surface $X = \mathbb{C}^2/\mathbb{Z}^4$ with $\omega_0$, write down a basis of $P^{1,1}_{\mathbb{R}}$ from the real and imaginary parts of $dz_1 \wedge d\bar z_2$ and the real form $i(dz_1 \wedge d\bar z_1 - dz_2 \wedge d\bar z_2)$, and compute the Gram matrix of the intersection form on $H^{1,1}_{\mathbb{R}}$. Check the signature $(1, 3)$.
4. (B) Let $X$ be a compact connected Kähler surface. Show that the set $\{c \in H^{1,1}_{\mathbb{R}} : c^2 > 0\}$ has exactly two connected components, that $c \cdot c' > 0$ for $c$ and $c'$ in the same component, and that all Kähler classes lie in one component. Deduce the inequality $(c \cdot c')^2 \geq c^2 c'^2$ for $c^2 > 0$.
5. (B) Let $(X, \omega)$ be compact Kähler. Show that the operators $L$, $\Lambda$ and $H$ of Definition P6.4.7 preserve harmonic forms and give a representation of $\mathfrak{sl}_2(\mathbb{C})$ on $\bigoplus_k \mathcal{H}^k(X)$. Using only the representation theory of $\mathfrak{sl}_2(\mathbb{C})$ in finite dimension, give a second proof of Theorem P6.4.21, part 1, without Poincaré duality.
6. (C) Let $C = V(F) \subset \mathbb{P}^2$ be a smooth curve of degree $d \geq 3$, with affine equation $f(x, y) = 0$. Show that for every polynomial $P$ of degree at most $d - 3$ the form $P(x, y)\, dx/f_y$, defined where $f_y \neq 0$, extends to a holomorphic $1$-form on $C$, and that these forms span a space of dimension $(d-1)(d-2)/2$. Conclude with Example P6.4.26 that they are all holomorphic $1$-forms on $C$.

### Lean

Mathlib has the notion of an $\mathfrak{sl}_2$-triple in a Lie algebra and some of the representation theory of $\mathfrak{sl}_2$, and it has symmetric bilinear forms with their signature over ordered fields in some cases. It has no de Rham cohomology of manifolds, no Kähler manifolds and no harmonic forms, so neither hard Lefschetz nor the Hodge-Riemann relations can be stated. The handbook adds no `MinimalModel` node here.

### Notes and history

Lefschetz stated the hard Lefschetz theorem for projective manifolds in his 1924 monograph (Lef24), with a topological argument that was later found to be incomplete. Hodge gave the first complete proof, through harmonic forms, in Hod41, and the proof here, through the $\mathfrak{sl}_2$ structure, is the one in Huybrechts, Section 3.3 (Huy05), and Wells, Chapter V (Wel80). Deligne proved the analogue in étale cohomology in positive characteristic as part of his work on the Weil conjectures. The bilinear relations go back to Riemann's inequalities for the periods of abelian integrals on a curve, which are part 2 of Theorem P6.4.23 for $k = 1$ and $n = 1$, and Hodge extended them to all degrees. Corollary P6.4.24 is the analytic form of Theorem P5.5.22: for a projective surface and an ample divisor $H$, the class $c_1(\mathcal{O}(H))$ is a Kähler class, and a divisor $D$ with $D \cdot H = 0$ has $c_1(\mathcal{O}(D)) \in P^{1,1}_{\mathbb{R}}$. The comparison of intersection numbers with integrals of Chern classes is not proved here. The value $\sigma = -16$ for the quartic agrees with Hirzebruch's signature theorem $\sigma = (c_1^2 - 2c_2)/3 = -48/3$, which is not used. The sign conventions follow Huybrechts; Griffiths and Harris and Voisin state the relations with different normalizations of $Q$, which differ by signs that depend only on $k$.
