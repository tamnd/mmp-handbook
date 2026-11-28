---
title: The Hodge decomposition
nodes: []
sources: [Huy05, Voi02, GH78, Wel80, Hod41, Ser56, BT82]
reads_with: [Huy05:3.2, Huy05:4.1, Huy05:A, Voi02:5, Voi02:6, GH78:0.6, GH78:0.7, Wel80:IV, Wel80:V.2, Wel80:V.5]
requires: [P2.7, P6.1, P6.2, P6.3]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The Hodge decomposition

### Statement

Let $X$ be a compact complex manifold of dimension $n$ with a Hermitian metric, and use the inner product $(\ , \ )$, the adjoints and the Laplacians of Definition P6.4.11. Write $\mathcal{H}^k(X)$ for the space of $\Delta_d$-harmonic $k$-forms and $\mathcal{H}^{p,q}_{\bar\partial}(X)$ for the space of $\Delta_{\bar\partial}$-harmonic $(p,q)$-forms. Write $H^{p,q}_{\bar\partial}(X)$ for Dolbeault cohomology and $H^k(X, \mathbb{C}) = H^k_{dR}(X, \mathbb{C})$ for de Rham cohomology (Definition P6.2.22, Theorem P6.2.25).

**Theorem P6.4.14 (Hodge theorem, black box).** Let $X$ be a compact complex manifold with a Hermitian metric. Then the spaces $\mathcal{H}^k(X)$ and $\mathcal{H}^{p,q}_{\bar\partial}(X)$ are finite-dimensional, and there are decompositions, orthogonal for $(\ , \ )$,
$$A^k(X) = \mathcal{H}^k(X) \oplus dA^{k-1}(X) \oplus d^*A^{k+1}(X), \qquad A^{p,q}(X) = \mathcal{H}^{p,q}_{\bar\partial}(X) \oplus \bar\partial A^{p,q-1}(X) \oplus \bar\partial^*A^{p,q+1}(X).$$

Lean: not yet in Lean.

The theorem is the case of the Laplacians $\Delta_d$ and $\Delta_{\bar\partial}$ of the general theorem on elliptic self-adjoint operators on compact manifolds. It is cited from Huybrechts, Appendix A and Section 4.1 (Huy05), Wells, Chapter IV and Section V.2 (Wel80), Voisin, Chapter 5 (Voi02), and Griffiths and Harris, Section 0.6 (GH78), and it is not proved in this handbook. Complex conjugation maps $\Delta_{\bar\partial}$ to $\Delta_\partial$, so the theorem also gives $A^{p,q}(X) = \mathcal{H}^{p,q}_\partial(X) \oplus \partial A^{p-1,q}(X) \oplus \partial^*A^{p+1,q}(X)$, the conjugate of the decomposition of $A^{q,p}(X)$.

**Corollary P6.4.15 (finiteness and Serre duality).** Let $X$ be a compact complex manifold of dimension $n$ with any Hermitian metric.

1. A form $\alpha$ is $\Delta_d$-harmonic if and only if $d\alpha = 0$ and $d^*\alpha = 0$, and $\Delta_{\bar\partial}$-harmonic if and only if $\bar\partial\alpha = 0$ and $\bar\partial^*\alpha = 0$. Every de Rham class contains exactly one $\Delta_d$-harmonic form and every Dolbeault class exactly one $\Delta_{\bar\partial}$-harmonic form, so $\mathcal{H}^k(X) \cong H^k(X, \mathbb{C})$ and $\mathcal{H}^{p,q}_{\bar\partial}(X) \cong H^{p,q}_{\bar\partial}(X) \cong H^q(X, \Omega^p_X)$. In particular $b_k$ and $h^{p,q}$ are finite.
2. (Serre duality.) The pairing $H^{p,q}_{\bar\partial}(X) \times H^{n-p,n-q}_{\bar\partial}(X) \to \mathbb{C}$, $([\alpha], [\beta]) \mapsto \int_X \alpha \wedge \beta$, is well defined and perfect. Hence $h^{p,q} = h^{n-p,n-q}$ and $H^q(X, \Omega^p_X) \cong H^{n-q}(X, \Omega^{n-p}_X)^\vee$.
3. (Poincaré duality.) The pairing $H^k(X, \mathbb{R}) \times H^{2n-k}(X, \mathbb{R}) \to \mathbb{R}$, $([\alpha], [\beta]) \mapsto \int_X \alpha \wedge \beta$, is perfect, and $b_k = b_{2n-k}$.

Lean: not yet in Lean.

**Theorem P6.4.16 (Hodge decomposition).** Let $X$ be a compact Kähler manifold. For $p + q = k$ let $H^{p,q}(X) \subseteq H^k(X, \mathbb{C})$ be the set of classes that contain a $d$-closed form of type $(p,q)$. Then:

1. $H^k(X, \mathbb{C}) = \bigoplus_{p+q=k} H^{p,q}(X)$.
2. The map $H^{p,q}(X) \to H^{p,q}_{\bar\partial}(X)$ that sends the class of a $d$-closed $(p,q)$-form to its Dolbeault class is well defined and an isomorphism, so $H^{p,q}(X) \cong H^q(X, \Omega^p_X)$ by Theorem P6.2.24.
3. Complex conjugation of $H^k(X, \mathbb{C}) = H^k(X, \mathbb{R}) \otimes \mathbb{C}$ maps $H^{p,q}(X)$ onto $H^{q,p}(X)$.
4. For any Kähler metric, $H^{p,q}(X)$ is the image of the space $\mathcal{H}^{p,q}(X) = \mathcal{H}^k(X) \cap A^{p,q}(X)$ of harmonic $(p,q)$-forms, and $\mathcal{H}^{p,q}(X) = \mathcal{H}^{p,q}_{\bar\partial}(X) = \mathcal{H}^{p,q}_\partial(X)$. The subspaces $H^{p,q}(X)$ themselves do not depend on the metric.

Lean: not yet in Lean.

**Corollary P6.4.17 (Hodge symmetry and consequences).** Let $X$ be a compact Kähler manifold of dimension $n$, and write $h^{p,q} = \dim H^q(X, \Omega^p_X)$.

1. $h^{p,q} = h^{q,p} = h^{n-p,n-q}$.
2. $b_k = \sum_{p+q=k} h^{p,q}$.
3. $b_{2k+1}$ is even for every $k$, and $h^{k,k} \geq 1$ for $0 \leq k \leq n$.
4. Every holomorphic $p$-form on $X$ is $d$-closed and harmonic for every Kähler metric, $H^0(X, \Omega^p_X) \cong H^{p,0}(X)$, and a nonzero holomorphic form is not $d$-exact.
5. The Frölicher spectral sequence $E_1^{p,q} = H^q(X, \Omega^p_X) \Rightarrow H^{p+q}(X, \mathbb{C})$ of Proposition P6.2.26 degenerates at $E_1$.

Lean: not yet in Lean.

**Corollary P6.4.18 (the $\partial\bar\partial$-lemma).** Let $X$ be a compact Kähler manifold and $\alpha$ a $d$-closed form of type $(p,q)$. The following are equivalent: $\alpha$ is $d$-exact; $\alpha$ is $\partial$-exact; $\alpha$ is $\bar\partial$-exact; $\alpha = \partial\bar\partial\beta$ for some $\beta \in A^{p-1,q-1}(X)$. If $\alpha$ is a real $d$-exact $(1,1)$-form, then $\alpha = i\partial\bar\partial\varphi$ for a smooth real function $\varphi$, unique up to an additive constant when $X$ is connected. In particular two Kähler forms with the same Kähler class differ by $i\partial\bar\partial\varphi$.

Lean: not yet in Lean.

### Proof in words

The Hodge theorem is cited. On any compact Hermitian manifold it gives finiteness at once: harmonic forms are closed and coclosed, and each cohomology class has a unique harmonic representative, the one of smallest norm. Serre duality and Poincaré duality follow because the conjugate-linear star sends harmonic forms to harmonic forms, and $\int \alpha \wedge \overline{*\alpha}$ is the squared norm of $\alpha$.

On a Kähler manifold, $\Delta_d = 2\Delta_{\bar\partial}$ (Theorem P6.4.12). So the $\Delta_d$-harmonic forms are the $\Delta_{\bar\partial}$-harmonic forms. Since $\Delta_{\bar\partial}$ preserves type, the type components of a harmonic form are harmonic. This splits $H^k(X, \mathbb{C})$, represented by $\mathcal{H}^k$, into the pieces $\mathcal{H}^{p,q}$, which represent Dolbeault cohomology. The pieces are described without the metric: $H^{p,q}(X)$ consists of the classes that contain a closed $(p,q)$-form. Conjugation swaps $(p,q)$ and $(q,p)$, which gives Hodge symmetry and the parity of odd Betti numbers. A holomorphic form is $\bar\partial$-closed and trivially $\bar\partial^*$-closed, so it is harmonic.

The $\partial\bar\partial$-lemma combines the two Hodge decompositions, for $\bar\partial$ and for $\partial$, which have the same harmonic forms. An exact pure-type closed form is orthogonal to the harmonic forms, so it is $\bar\partial$-exact. Writing the primitive by the $\partial$-decomposition and using $\bar\partial\partial^* = -\partial^*\bar\partial$, the part that is not $\partial\bar\partial$-exact has to vanish.

The Kähler hypothesis is needed. The Hopf surface has $b_1 = 1$ and $h^{1,0} = 0 < h^{0,1}$, so Hodge symmetry fails on it, and odd $b_1$ shows again that it carries no Kähler metric.

### Examples

**Example P6.4.19 (the Hopf surface again).** Let $X$ be the Hopf surface of Example P6.2.4, with $b_1(X) = 1$. By Corollary P6.4.17, part 3, $b_1$ of a compact Kähler manifold is even, so $X$ is not Kähler. This is a second proof, independent of Example P6.4.6, and it uses odd degree. The Hodge numbers in degree $1$ show what goes wrong.

1. $h^{1,0} = 0$. A holomorphic $1$-form on $X$ pulls back to $\alpha = f_1\, dz_1 + f_2\, dz_2$ on $\mathbb{C}^2 \setminus \{0\}$, invariant under $\phi(z) = 2z$. By Hartogs (Corollary P6.1.15) the $f_j$ extend to entire functions with power series $f_j = \sum_m a_{j,m} z^m$. Since $\phi^*\alpha = \sum_j 2f_j(2z)\, dz_j$, invariance means $f_j(z) = 2f_j(2z)$, so $a_{j,m}(2^{|m|+1} - 1) = 0$ for every multi-index $m$. Hence $f_j = 0$. In the same way $h^{2,0} = 0$, since $dz_1 \wedge dz_2$ is multiplied by $4$.
2. $h^{0,1} \geq 1$. In the Frölicher spectral sequence (Proposition P6.2.26) the terms $E_\infty^{p,q}$ are subquotients of $E_1^{p,q} = H^q(X, \Omega^p_X)$, finite-dimensional by Corollary P6.4.15, and $\sum_{p+q=1} \dim E_\infty^{p,q} = b_1$. So $1 = b_1 \leq h^{1,0} + h^{0,1} = h^{0,1}$.

So $h^{1,0} \neq h^{0,1}$, and Hodge symmetry fails on this compact complex surface. Serre duality, which needs no Kähler metric, still holds: $h^{2,1} = h^{0,1}$ and $h^{2,2} = h^{0,0} = 1$.

**Example P6.4.20 (elliptic curves and tori, checked against P6.2.29).** Let $X = \mathbb{C}^n/\Lambda$ with the flat Kähler form $\omega_0$ (Example P6.4.3). By Example P6.4.13, the harmonic forms are the forms $\sum c_{IJ}\, dz_I \wedge d\bar z_J$ with constant coefficients. Hence
$$H^{p,q}(X) = \bigoplus_{|I| = p,\, |J| = q} \mathbb{C}\,[dz_I \wedge d\bar z_J], \qquad h^{p,q} = \binom{n}{p}\binom{n}{q}, \qquad b_k = \sum_{p+q=k}\binom{n}{p}\binom{n}{q} = \binom{2n}{k},$$
in agreement with Theorem P6.2.29, which computed the same groups by Fourier series without Hodge theory.

For an elliptic curve $E_\tau = \mathbb{C}/(\mathbb{Z} + \mathbb{Z}\tau)$, $\operatorname{Im}\tau > 0$, the decomposition is $H^1(E_\tau, \mathbb{C}) = \mathbb{C}[dz] \oplus \mathbb{C}[d\bar z]$. Let $\gamma_1$ and $\gamma_2$ be the images of the segments from $0$ to $1$ and from $0$ to $\tau$. Integration over these loops gives an isomorphism $H^1(E_\tau, \mathbb{C}) \to \mathbb{C}^2$, since they form a basis of $H_1(E_\tau, \mathbb{Z})$ and $dx$, $dy$ have the period matrix $\begin{pmatrix} 1 & \operatorname{Re}\tau \\ 0 & \operatorname{Im}\tau \end{pmatrix}$, which is invertible. The periods of $dz$ are $(1, \tau)$ and those of $d\bar z$ are $(1, \bar\tau)$, with determinant $\bar\tau - \tau = -2i\operatorname{Im}\tau \neq 0$. This confirms directly that $[dz]$ and $[d\bar z]$ form a basis. Also $i\int_{E_\tau} dz \wedge d\bar z = 2\int_{E_\tau} dx \wedge dy = 2\operatorname{Im}\tau > 0$, the first case of the Hodge-Riemann relations of Section 4.4.

The $\partial\bar\partial$-lemma on $E_\tau$ is a statement about Fourier series. Write $e_\xi$ for the characters of Example P6.4.13, for which $\partial_z\partial_{\bar z} e_\xi = -\pi^2|\xi|^2 e_\xi$. A $(1,1)$-form $\alpha = f\, dz \wedge d\bar z$ is exact if and only if $\int_{E_\tau} \alpha = 0$, that is, if and only if $f = \sum_{\xi \neq 0} c_\xi e_\xi$ has no constant term, by Poincaré duality ($b_2 = 1$). Then $\beta = -\sum_{\xi \neq 0} \pi^{-2}|\xi|^{-2} c_\xi e_\xi$ is smooth, since the $c_\xi$ decay faster than any power of $|\xi|$, and $\partial\bar\partial\beta = \alpha$.

### Proof

*Theorem P6.4.14.* This is the Hodge theorem for the elliptic operators $\Delta_d$ and $\Delta_{\bar\partial}$, cited as stated above.

*Corollary P6.4.15.* (1) For every form, $(\Delta_d\alpha, \alpha) = \|d\alpha\|^2 + \|d^*\alpha\|^2$ by Definition P6.4.11, and similarly for $\Delta_{\bar\partial}$, which gives the characterization of harmonic forms. Let $\alpha$ be $d$-closed and decompose $\alpha = h + d\beta + d^*\gamma$ by Theorem P6.4.14. Then $0 = d\alpha = dd^*\gamma$, so $\|d^*\gamma\|^2 = (dd^*\gamma, \gamma) = 0$ and $\alpha = h + d\beta$. So $\ker d = \mathcal{H}^k \oplus dA^{k-1}$, and since the sum is direct, each class has exactly one harmonic representative. The same argument applies to $\bar\partial$. The last isomorphism of part 1 is Theorem P6.2.24.

(2) Let $\alpha \in A^{p,q}$ and $\beta \in A^{n-p,n-q}$ be $\bar\partial$-closed and $\gamma \in A^{p,q-1}$. The form $\gamma \wedge \beta$ has type $(n, n-1)$, so $d(\gamma \wedge \beta) = \bar\partial(\gamma \wedge \beta) = \bar\partial\gamma \wedge \beta \pm \gamma \wedge \bar\partial\beta = \bar\partial\gamma \wedge \beta$, and $\int_X \bar\partial\gamma \wedge \beta = 0$ by Stokes. So the pairing is well defined. Define the conjugate-linear map $\bar * \colon A^{p,q} \to A^{n-p,n-q}$, $\bar*\alpha = *\bar\alpha$, of the right type by Proposition P6.4.10, part 2. If $\alpha$ is $\Delta_{\bar\partial}$-harmonic, then $\bar\partial(*\bar\alpha) = -{*}^{-1}\partial^*\bar\alpha = -{*}^{-1}\overline{\bar\partial^*\alpha} = 0$, because $\partial^* = -{*}\bar\partial{*}$, and $\bar\partial^*(*\bar\alpha) = -{*}\partial{*}{*}\bar\alpha = \pm{*}\overline{\bar\partial\alpha} = 0$. So $\bar*\alpha$ is harmonic. For harmonic $\alpha \neq 0$, $\int_X \alpha \wedge \bar*\alpha = \int_X \alpha \wedge *\bar\alpha = \|\alpha\|^2 > 0$. Hence the map $H^{p,q}_{\bar\partial} \to (H^{n-p,n-q}_{\bar\partial})^\vee$ is injective. The symmetric argument gives the reverse inequality of dimensions, so the pairing is perfect.

(3) The same argument with $d$, real forms and $*$ applies, since $\Delta_d$ commutes with $*$ on any Hermitian manifold. The computation in the proof of Theorem P6.4.12, part 4, uses only $d^* = -{*}d{*}$ and $** = (-1)^{\deg}$.

*Theorem P6.4.16.* Fix a Kähler metric. By Theorem P6.4.12, $\Delta_d = 2\Delta_{\bar\partial} = 2\Delta_\partial$, and $\Delta_d$ preserves type. So a $k$-form is $\Delta_d$-harmonic if and only if each of its type components is, and $\mathcal{H}^k = \bigoplus_{p+q=k}\mathcal{H}^{p,q}$ with $\mathcal{H}^{p,q} = \mathcal{H}^{p,q}_{\bar\partial} = \mathcal{H}^{p,q}_\partial$. This proves the equalities of part 4. By Corollary P6.4.15, $\mathcal{H}^k \to H^k(X, \mathbb{C})$ is an isomorphism, so $H^k(X, \mathbb{C})$ is the direct sum of the images of the $\mathcal{H}^{p,q}$.

The image of $\mathcal{H}^{p,q}$ is $H^{p,q}(X)$. Harmonic forms are closed, so it is contained in $H^{p,q}(X)$. Conversely let $\alpha$ be a $d$-closed $(p,q)$-form. By Theorem P6.4.14 and Corollary P6.4.15, $\alpha = h + \bar\partial\beta$ with $h \in \mathcal{H}^{p,q}$. The form $\alpha - h = \bar\partial\beta$ is $d$-closed and orthogonal to $\mathcal{H}^k$: it is orthogonal to harmonic forms of other types, and $(\bar\partial\beta, h') = (\beta, \bar\partial^*h') = 0$ for $h' \in \mathcal{H}^{p,q}$. By the decomposition $\ker d = \mathcal{H}^k \oplus dA^{k-1}$ it is $d$-exact, so $[\alpha] = [h]$. This proves part 1 and the first assertion of part 4. The subspace $H^{p,q}(X)$ is defined without a metric, which gives the last assertion.

(2) If $\alpha$ and $\alpha'$ are $d$-closed $(p,q)$-forms in the same de Rham class, then $\alpha - \alpha'$ is $d$-exact, hence orthogonal to $\mathcal{H}^k$. Its $\bar\partial$-decomposition $\alpha - \alpha' = h + \bar\partial u$ has $h = 0$, so $\alpha - \alpha'$ is $\bar\partial$-exact and the map is well defined. Composed with the isomorphism $\mathcal{H}^{p,q} \to H^{p,q}(X)$ it is the isomorphism $\mathcal{H}^{p,q}_{\bar\partial} \to H^{p,q}_{\bar\partial}(X)$ of Corollary P6.4.15, so it is an isomorphism.

(3) If $\alpha$ is a $d$-closed $(p,q)$-form, $\bar\alpha$ is a $d$-closed $(q,p)$-form, and $\overline{[\alpha]} = [\bar\alpha]$.

*Corollary P6.4.17.* (1) Part 2 of Theorem P6.4.16 gives $h^{p,q} = \dim H^{p,q}(X)$, and part 3 gives $h^{p,q} = h^{q,p}$. Serre duality (Corollary P6.4.15) gives $h^{p,q} = h^{n-p,n-q}$. (2) This is part 1 of Theorem P6.4.16. (3) $b_{2k+1} = \sum_{p=0}^{2k+1} h^{p,2k+1-p} = 2\sum_{p=0}^{k} h^{p,2k+1-p}$ by symmetry. For $k \leq n$, $\omega^k$ is a closed $(k,k)$-form whose class is nonzero by Proposition P6.4.5, so $h^{k,k} \geq 1$. (4) A holomorphic $p$-form $\alpha$ satisfies $\bar\partial\alpha = 0$, and $\bar\partial^*\alpha = 0$ because $\bar\partial^*\alpha$ would have type $(p, -1)$. So $\alpha$ is $\Delta_{\bar\partial}$-harmonic, hence $\Delta_d$-harmonic and $d$-closed. Since $\bar\partial A^{p,-1} = 0$, $H^{p,0}_{\bar\partial}(X) = H^0(X, \Omega^p_X)$, and Theorem P6.4.16 identifies it with $H^{p,0}(X)$. A nonzero harmonic form is not exact. (5) In a spectral sequence of finite-dimensional spaces, $E_{r+1}^{p,q}$ is a subquotient of $E_r^{p,q}$, with $\dim E_{r+1}^{p,q} = \dim E_r^{p,q}$ for all $(p,q)$ if and only if $d_r = 0$. The spaces $E_\infty^{p,q}$ with $p + q = k$ are the graded pieces of a filtration of $H^k(X, \mathbb{C})$. So $b_k = \sum_{p+q=k}\dim E_\infty^{p,q} \leq \sum_{p+q=k} h^{p,q}$, and by part 2 equality holds for every $k$. Hence $d_r = 0$ for all $r \geq 1$.

*Corollary P6.4.18.* If $\alpha = \partial\bar\partial\beta$, then $\alpha = d(\bar\partial\beta) = \partial(\bar\partial\beta) = \bar\partial(-\partial\beta)$, so it is exact for all three operators. Conversely suppose $\alpha$ is exact for one of $d$, $\partial$, $\bar\partial$. Every harmonic form $h$ satisfies $d^*h = \partial^*h = \bar\partial^*h = 0$, since it is harmonic for all three Laplacians (Theorem P6.4.16). So $(\alpha, h) = (\gamma, d^*h)$, $(\gamma, \partial^*h)$ or $(\gamma, \bar\partial^*h)$ is $0$, and $\alpha$ is orthogonal to $\mathcal{H}^{p,q}$. Since $\bar\partial\alpha = 0$, Corollary P6.4.15 gives $\alpha = \bar\partial\gamma$ with $\gamma \in A^{p,q-1}$. Decompose $\gamma = h + \partial u + \partial^*v$ by the $\partial$-version of Theorem P6.4.14, with $u \in A^{p-1,q-1}$ and $v \in A^{p+1,q-1}$. Then $\bar\partial h = 0$, and $\bar\partial\partial^* = -\partial^*\bar\partial$ by Theorem P6.4.12, part 2, so
$$\alpha = \bar\partial\partial u + \bar\partial\partial^*v = -\partial\bar\partial u - \partial^*\bar\partial v.$$
As $\alpha$ is $d$-closed of pure type, $\partial\alpha = 0$, hence $\partial\partial^*\bar\partial v = 0$ and $\|\partial^*\bar\partial v\|^2 = (\partial\partial^*\bar\partial v, \bar\partial v) = 0$. So $\alpha = \partial\bar\partial(-u)$.

If $\alpha$ is real, $d$-exact and of type $(1,1)$, then $\alpha = \partial\bar\partial\beta$ for a function $\beta$. Since $\alpha = \bar\alpha = \bar\partial\partial\bar\beta = -\partial\bar\partial\bar\beta$, also $\alpha = \partial\bar\partial\frac{\beta - \bar\beta}{2} = i\partial\bar\partial\operatorname{Im}\beta$, and $\varphi = \operatorname{Im}\beta$ is real. If $i\partial\bar\partial\varphi = 0$ with $\varphi$ real, apply $\Lambda$. Since $\Lambda$ vanishes on $1$-forms, Theorem P6.4.12 gives $\Lambda\partial\bar\partial\varphi = [\Lambda, \partial]\bar\partial\varphi = i\bar\partial^*\bar\partial\varphi$, so $\Lambda(i\partial\bar\partial\varphi) = -\Delta_{\bar\partial}\varphi$ and $\Delta_{\bar\partial}\varphi = 0$. On $\mathbb{C}$ this reads $\Lambda(i\varphi_{z\bar z}\, dz \wedge d\bar z) = 2\varphi_{z\bar z} = -\Delta_{\bar\partial}\varphi$, in agreement with Example P6.4.13. Then $\varphi$ is harmonic, hence locally constant. For two Kähler forms with $[\omega] = [\omega']$, apply this to $\alpha = \omega' - \omega$. $\square$

### Exercises

1. (A) Let $X$ be a compact Kähler manifold of dimension $3$ with $b_1 = 2$, $b_2 = 3$ and $b_3 = 4$. List all Hodge diamonds compatible with Corollary P6.4.17.
2. (A) Show that every compact complex surface with odd $b_1$ is not Kähler. Show that the product of the Hopf surface with $\mathbb{P}^1$ is a compact complex manifold of dimension $3$ that is not Kähler, by computing $b_1$ with the Künneth formula (BT82, Chapter I).
3. (B) Verify Serre duality and Hodge symmetry on $\mathbb{P}^1$ directly from Example P6.2.27. Show that the pairing $H^{0,0} \times H^{1,1} \to \mathbb{C}$ sends $(1, [\omega_{FS}])$ to $1$.
4. (B) Let $X$ be compact connected Kähler and $\omega$, $\omega'$ Kähler forms with $[\omega] = [\omega']$. Show that $\omega' = \omega + i\partial\bar\partial\varphi$ with $\varphi$ real and unique up to a constant, and that $\int_X \omega^n = \int_X \omega'^n$. Show more generally that $\int_Y \omega^d$ depends only on the class $[\omega]$ for every compact complex submanifold $Y$ of dimension $d$.
5. (B) On $E_\tau$ consider the Kähler forms $\rho\,\omega_0$ with $\rho > 0$ smooth. Show that the harmonic $1$-forms are the forms with constant coefficients for every $\rho$, and that the harmonic $2$-forms are the constant multiples of $\rho\,\omega_0$. Conclude that the spaces of harmonic forms depend on the metric, while $H^{p,q}(E_\tau)$ does not.
6. (C) The Bott-Chern cohomology of a complex manifold is $H^{p,q}_{BC}(X) = (\ker\partial \cap \ker\bar\partial \cap A^{p,q}(X))/\partial\bar\partial A^{p-1,q-1}(X)$. Show that for compact Kähler $X$ the natural map $H^{p,q}_{BC}(X) \to H^{p,q}(X)$ is an isomorphism: injectivity is Corollary P6.4.18 and surjectivity is the definition of $H^{p,q}(X)$. Deduce that a $d$-closed $(p,q)$-form that is $\bar\partial$-exact is $\partial$-exact.

### Lean

Mathlib has the spectral theory of compact self-adjoint operators on Hilbert spaces and Fourier series on tori, but no Sobolev spaces of sections of vector bundles on manifolds and no elliptic regularity, so the Hodge theorem is out of reach at present. It has no Dolbeault cohomology, no Serre duality and no Hodge decomposition. The handbook adds no `MinimalModel` node here.

### Notes and history

Hodge proved the existence of harmonic representatives in his book on harmonic integrals (Hod41). The proof there had a gap in the analysis, repaired by Weyl and by Kodaira in the 1940s, and the modern proof uses elliptic regularity, as in Wells, Chapter IV (Wel80). The decomposition of the cohomology of a compact Kähler manifold by type, with $H^{p,q} \cong H^q(X, \Omega^p)$ through Dolbeault's theorem, is the Hodge decomposition. Serre proved the duality that bears his name in 1955 for arbitrary compact complex manifolds; the proof here through harmonic forms is the one in Huybrechts, Section 4.1 (Huy05). The $\partial\bar\partial$-lemma is due to Deligne, Griffiths, Morgan and Sullivan (1975) in its use for the formality of compact Kähler manifolds, and the form here follows Huybrechts, Section 3.2 (Huy05) and Voisin, Chapter 6 (Voi02). For non-Kähler compact surfaces the Frölicher spectral sequence still degenerates at $E_1$, but Hodge symmetry fails, as the Hopf surface shows.
