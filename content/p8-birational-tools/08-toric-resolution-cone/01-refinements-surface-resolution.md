---
title: Refinements and toric resolution
nodes: []
sources: [CLS11, Ful93, KKMS73]
reads_with: [CLS11:ch10, CLS11:ch11, Ful93:2.6]
requires: [P3.4, P3.11]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Refinements and toric resolution

### Statement

Throughout, $k$ is algebraically closed and all fans are in the same space $N_\mathbb{R}$.

**Definition P8.8.1 (refinements and multiplicity).** A fan $\Sigma'$ *refines* a fan $\Sigma$ if every cone of $\Sigma'$ is contained in a cone of $\Sigma$ and $|\Sigma'| = |\Sigma|$. For a simplicial cone $\sigma$ with ray generators $u_1, \dots, u_d$, the *multiplicity* is the index
$$\operatorname{mult}(\sigma) = [N_\sigma : \mathbb{Z} u_1 + \dots + \mathbb{Z} u_d], \qquad N_\sigma = N \cap \operatorname{span}(\sigma).$$
So $\sigma$ is smooth if and only if $\operatorname{mult}(\sigma) = 1$. For a fan $\Sigma$ and a primitive $w \in |\Sigma| \cap N$, the *star subdivision* $\Sigma^*(w)$ consists of the cones of $\Sigma$ not containing $w$ together with the cones $\operatorname{Cone}(\tau, w)$ for $\tau \in \Sigma$ with $w \notin \tau$ and $\tau \cup \{ w \}$ contained in a cone of $\Sigma$.

**Proposition P8.8.2 (refinements give proper birational morphisms).** Let $\Sigma'$ refine $\Sigma$. The identity of $N$ induces a toric morphism $\pi \colon X_{\Sigma'} \to X_\Sigma$, which is the identity on $T_N$. For $\sigma \in \Sigma$, $\pi^{-1}(U_\sigma)$ is the toric variety of the fan $\Sigma'_\sigma = \{ \sigma' \in \Sigma' : \sigma' \subseteq \sigma \}$, and $\pi$ is proper and birational. It is an isomorphism over $U_\sigma$ whenever $\sigma \in \Sigma'$.

Lean: the combinatorial condition is `MinimalModel.Toric.Fan.Refines`; the morphism is not in Lean as stated.

**Theorem P8.8.3 (resolution of toric surface singularities).** Let $d \geq 2$ and $0 < k < d$ with $\gcd(d, k) = 1$, and let $\sigma = \operatorname{Cone}(e_2, d e_1 - k e_2)$, so that $U_\sigma$ is the cyclic quotient singularity $\frac{1}{d}(1, k)$. Write
$$\frac{d}{k} = [b_1, \dots, b_r] = b_1 - \cfrac{1}{b_2 - \cfrac{1}{\ddots - \cfrac{1}{b_r}}}, \qquad b_i \geq 2,$$
the Hirzebruch-Jung continued fraction, and define $v_0 = e_2$, $v_1 = e_1$ and $v_{i+1} = b_i v_i - v_{i-1}$ for $1 \leq i \leq r$.

1. $v_{r+1} = d e_1 - k e_2$, every $v_i$ lies in $\sigma$, and the cones $\operatorname{Cone}(v_i, v_{i+1})$, $0 \leq i \leq r$, with their faces form a smooth fan $\Sigma'$ refining $\sigma$.
2. The morphism $\pi \colon X_{\Sigma'} \to U_\sigma$ is a resolution of singularities. It is an isomorphism over $U_\sigma \setminus \{ \gamma_\sigma \}$, and $\pi^{-1}(\gamma_\sigma) = E_1 \cup \dots \cup E_r$ with $E_i = D_{v_i}$.
3. Each $E_i$ is isomorphic to $\mathbb{P}^1$, $E_i$ and $E_{i+1}$ meet transversally in one point, $E_i \cap E_j = \emptyset$ for $|i - j| \geq 2$, and $E_i^2 = -b_i$.

Lean: not in Lean as stated.

**Theorem P8.8.4 (toric resolution).** Let $\Sigma$ be a simplicial fan. Then there is a smooth fan $\Sigma'$ refining $\Sigma$, obtained by a finite sequence of star subdivisions at lattice points $w = \sum \lambda_i u_i$ of cones of $\Sigma$ with $0 \leq \lambda_i < 1$, each of which lowers the multiplicities of the new cones: the cone obtained from $\sigma$ by replacing $u_i$ with $w$ has multiplicity $\lambda_i \operatorname{mult}(\sigma)$. So $X_{\Sigma'} \to X_\Sigma$ is a resolution of singularities that is an isomorphism over the smooth locus of $X_\Sigma$. Every fan has a simplicial refinement with the same rays, so every toric variety has a toric resolution.

Lean: not in Lean as stated.

### Proof in words

A refinement maps each small cone into a big cone, so the affine charts map to each other, and the maps glue. Properness is the valuative criterion of Theorem P8.6.28, run inside a cone of $\Sigma$: a one-parameter limit that exists in $U_\sigma$ is a vector in $\sigma$, and $\sigma$ is covered by the small cones. For surfaces the continued fraction produces, step by step, the lattice points on the boundary of the convex hull of $\sigma \cap N \setminus \{0\}$, and the recursion $v_{i+1} = b_i v_i - v_{i-1}$ keeps the determinant of consecutive vectors equal to $\pm 1$, so every small cone is smooth. The relation $v_{i-1} + v_{i+1} = b_i v_i$ is the wall relation of Section 8.2, which gives $E_i^2 = -b_i$. In higher dimension a simplicial cone of multiplicity greater than one contains a nonzero lattice point in its half-open fundamental parallelepiped, and subdividing at it lowers the multiplicity.

### Examples

**Example P8.8.5 (the singularity $\frac{1}{5}(1, 2)$).** Let $\sigma = \operatorname{Cone}(e_2, 5 e_1 - 2 e_2)$. The continued fraction is
$$\frac{5}{2} = 3 - \frac{1}{2} = [3, 2],$$
so $b_1 = 3$, $b_2 = 2$, and
$$v_0 = (0, 1), \quad v_1 = (1, 0), \quad v_2 = 3 v_1 - v_0 = (3, -1), \quad v_3 = 2 v_2 - v_1 = (5, -2).$$
The determinants $\det(v_0, v_1)$, $\det(v_1, v_2)$ and $\det(v_2, v_3) = -6 + 5$ are all $-1$, so the three cones are smooth. The relations $v_0 + v_2 = 3 v_1$ and $v_1 + v_3 = 2 v_2$ give, by Theorem P8.8.3, two exceptional curves with $E_1^2 = -3$ and $E_2^2 = -2$, meeting in one point. Reading the cone from the other ray, with the basis in which $5 e_1 - 2 e_2$ becomes $e_2$, gives $\frac{1}{5}(1, 3)$ and $\frac{5}{3} = [2, 3]$, the same chain in the opposite order; this reflects $2 \cdot 3 \equiv 1 \pmod 5$.

**Example P8.8.6 (the $A_{d-1}$ singularities and $\frac{1}{n}(1, 1)$).** For $k = d - 1$, $\frac{d}{d - 1} = [2, 2, \dots, 2]$ with $d - 1$ entries, since $[2, \dots, 2]$ with $j$ entries is $\frac{j + 1}{j}$. So the resolution of $\frac{1}{d}(1, d - 1)$, the du Val singularity $A_{d-1}$ of $xy = z^d$, is a chain of $d - 1$ curves of self-intersection $-2$. For $k = 1$, $\frac{n}{1} = [n]$, so the resolution of $\frac{1}{n}(1, 1)$, the cone over the rational normal curve of degree $n$, has one exceptional curve $E$ with $E^2 = -n$, and $v_0 = e_2$, $v_1 = e_1$, $v_2 = n e_1 - e_2$. For $n = 2$ both descriptions give the blow-up of the quadric cone with exceptional curve $C_- \subseteq F_2 \setminus C_+$ of Example P3.11.29.

**Example P8.8.7 (the Hirzebruch surface over $\mathbb{P}(1, 1, n)$).** The fan of $F_n$ of Example P8.6.20 has rays $u_1 = (1, 0)$, $u_2 = (0, 1)$, $u_3 = (-1, n)$, $u_4 = (0, -1)$, and removing $u_2$ gives the fan of $\mathbb{P}(1, 1, n)$ of Exercise 6 of Section 6.2, whose cone $\operatorname{Cone}(u_1, u_3)$ is $\frac{1}{n}(1, 1)$. Since $u_2 = \frac{1}{n}(u_1 + u_3)$, the fan of $F_n$ is the star subdivision at $u_2$, so Proposition P8.8.2 gives a proper birational morphism $F_n \to \mathbb{P}(1, 1, n)$ that contracts $C_- = D_2$, with $C_-^2 = -n$, to the singular point and is an isomorphism elsewhere. In the basis $u_1$, $u_2$ of $N$, $u_3 = -u_1 + n u_2$, and the cone $\operatorname{Cone}(u_1, u_3)$ subdivided at $u_2$ is the resolution of Example P8.8.6.

**Example P8.8.8 (a three-dimensional example).** Let $\sigma = \operatorname{Cone}(e_1, e_2, e_1 + e_2 + 2 e_3)$ in $\mathbb{R}^3$, with multiplicity $|\det| = 2$; it is the quotient singularity $\frac{1}{2}(1, 1, 1)$. The half-open parallelepiped contains the lattice point $w = \frac{1}{2}(e_1 + e_2 + (e_1 + e_2 + 2 e_3)) = e_1 + e_2 + e_3$, with $\lambda = (\frac{1}{2}, \frac{1}{2}, \frac{1}{2})$, and the star subdivision at $w$ has three cones, each of multiplicity $\frac{1}{2} \cdot 2 = 1$. The exceptional divisor $D_w$ is the toric surface of the quotient fan, which is $\mathbb{P}^2$.

### Proof

*Proposition P8.8.2.* For $\sigma' \in \Sigma'$ choose $\sigma \in \Sigma$ with $\sigma' \subseteq \sigma$. Then $\sigma^\vee \subseteq \sigma'^\vee$, so $S_\sigma \subseteq S_{\sigma'}$, and the inclusion $k[S_\sigma] \subseteq k[S_{\sigma'}]$ is a morphism $U_{\sigma'} \to U_\sigma \subseteq X_\Sigma$ that is the identity on $T_N$. Two such morphisms, on $U_{\sigma'_1}$ and $U_{\sigma'_2}$, agree on the dense open $T_N$ of the reduced scheme $U_{\sigma'_1 \cap \sigma'_2}$, and $X_\Sigma$ is separated, so they agree on the overlap and glue to $\pi$. It is equivariant because it is on $T_N$. It is birational because it is the identity on $T_N$.

The point $\gamma_{\tau'}$, $\tau' \in \Sigma'$, maps to $\gamma_\tau$ where $\tau$ is the smallest cone of $\Sigma$ containing $\tau'$: in a chart $U_\tau$ the image is the homomorphism $S_\tau \to k$ that is $1$ on $S_\tau \cap \tau'^\perp$ and $0$ elsewhere, and a form $m \in \tau^\vee$ vanishing on $\tau'$ defines a face $\tau \cap m^\perp$ of $\tau$ containing $\tau'$, which is $\tau$; so $S_\tau \cap \tau'^\perp = S_\tau \cap \tau^\perp$. By equivariance $\pi(O(\tau')) = O(\tau)$. If $\pi(O(\tau')) \subseteq U_\sigma$, then $O(\tau) \subseteq U_\sigma$, so $\tau \preceq \sigma$ by Theorem P8.6.25, and $\tau' \subseteq \sigma$. Hence $\pi^{-1}(U_\sigma) = \bigcup_{\sigma' \in \Sigma'_\sigma} U_{\sigma'} = X_{\Sigma'_\sigma}$, and $\Sigma'_\sigma$ is a fan with support $\sigma$, because $|\Sigma'| = |\Sigma|$ and a cone of $\Sigma'$ meeting the interior of $\sigma$ in a nonempty open set lies in $\sigma$. If $\sigma \in \Sigma'$, then $\Sigma'_\sigma$ is the fan of faces of $\sigma$, since every cone of $\Sigma'$ contained in $\sigma$ meets $\sigma$ in a face, so $\pi^{-1}(U_\sigma) = U_\sigma$.

Properness is local on the target, so it suffices to show that $X_{\Sigma'_\sigma} \to U_\sigma$ is proper. It is separated and of finite type, and the target is Noetherian, so by the valuative criterion for discrete valuation rings (Grothendieck, EGA II, Théorème 7.3.8) it suffices to lift. Let $R \supseteq k$ be a discrete valuation ring with fraction field $K$ and valuation $v$, let $a \colon \operatorname{Spec} K \to X_{\Sigma'_\sigma}$, and let $\beta \colon k[S_\sigma] \to R$ define an $R$-point of $U_\sigma$ compatible with $a$. As in the proof of Theorem P8.6.28, $a$ lies in an orbit $O(\tau')$, $\tau' \in \Sigma'_\sigma$, it is given by a homomorphism $\tilde \psi \colon \tau'^\perp \cap M \to K^*$ on the face $S_{\tau'} \cap \tau'^\perp$ and by $0$ elsewhere, and there is $\tilde u \in N$ with $\langle m, \tilde u \rangle = v(\tilde\psi(m))$ for $m \in \tau'^\perp \cap M$. For $m \in S_\sigma \subseteq S_{\tau'}$, compatibility says $\beta(\chi^m) = \tilde\psi(m)$ if $m \in \tau'^\perp$ and $\beta(\chi^m) = 0$ otherwise. So $\langle m, \tilde u \rangle = v(\beta(\chi^m)) \geq 0$ for $m \in S_\sigma \cap \tau'^\perp$. For $m \in S_\sigma \setminus \tau'^\perp$, $m$ is nonnegative on $\tau' \subseteq \sigma$ and nonzero on some ray of $\tau'$, so $\langle m, u_{\tau'} \rangle > 0$. Applying this to a finite generating set of $S_\sigma$, $\tilde u + c u_{\tau'} \in \sigma^{\vee\vee} = \sigma$ for every large integer $c$. The cones of $\Sigma'_\sigma$ that do not contain $u_{\tau'}$ are closed and miss $u_{\tau'}$, and $u_{\tau'} + \tilde u / c \in \sigma = |\Sigma'_\sigma|$ tends to $u_{\tau'}$, so for large $c$ the point $\tilde u + c u_{\tau'}$ lies in a cone $\sigma' \in \Sigma'_\sigma$ containing $u_{\tau'}$, and $\tau' \preceq \sigma'$ by Lemma P8.6.23. The rest of the proof of Theorem P8.6.28 gives a lift $\operatorname{Spec} R \to U_{\sigma'}$ of $a$. Its composite with $\pi$ and the point $\beta$ are two $R$-points of the affine scheme $U_\sigma$ that agree on $K$, and $R \to K$ is injective, so they agree.

*Theorem P8.8.3.* (1) Put $d_0 = d$, $d_1 = k$ and $d_{i+1} = b_i d_i - d_{i-1}$, where $b_i = \lceil d_{i-1} / d_i \rceil$; this is the Euclidean algorithm with rounding up, and it computes the continued fraction, since $\frac{d_{i-1}}{d_i} = b_i - \frac{d_{i+1}}{d_i}$ with $0 \leq d_{i+1} < d_i$. As $\gcd(d_{i-1}, d_i) = \gcd(d, k) = 1$, the algorithm stops with $d_r = 1$ and $d_{r+1} = 0$, and $b_i \geq 2$ for all $i$, since $d_{i-1} > d_i$. Let $C = d e_1 - k e_2$. Then $d_0 v_1 - d_1 v_0 = C$, and
$$d_i v_{i+1} - d_{i+1} v_i = d_i (b_i v_i - v_{i-1}) - (b_i d_i - d_{i-1}) v_i = d_{i-1} v_i - d_i v_{i-1},$$
so $d_{i-1} v_i - d_i v_{i-1} = C$ for $1 \leq i \leq r + 1$. At $i = r + 1$ this is $v_{r+1} = C$. The same identity, $d_{i-1} v_i = C + d_i v_{i-1}$, shows by induction that every $v_i$ is in $\sigma$, since $C, v_0 \in \sigma$ and $d_{i-1} > 0$. Also $\det(v_i, v_{i+1}) = \det(v_i, b_i v_i - v_{i-1}) = \det(v_{i-1}, v_i)$, so all these determinants equal $\det(e_2, e_1) = -1$, and each $\operatorname{Cone}(v_i, v_{i+1})$ is smooth. Since all $v_i$ lie in the cone $\sigma$, whose angle is less than $\pi$, and each consecutive pair has the same orientation, the angle from $v_0$ increases strictly along the sequence, from $v_0$ to $v_{r+1}$. So the cones $\operatorname{Cone}(v_i, v_{i+1})$ meet only along common rays and cover $\sigma$, and they form a fan refining $\sigma$.

(2) $X_{\Sigma'}$ is smooth by Theorem P8.6.27, and $\pi$ is proper and birational by Proposition P8.8.2. The proof of that proposition shows $\pi(O(\tau')) = O(\tau)$ with $\tau$ the smallest face of $\sigma$ containing $\tau'$. This face is $\sigma$ exactly for the rays $\operatorname{Cone}(v_i)$, $1 \leq i \leq r$, and the two-dimensional cones. So $\pi^{-1}(\gamma_\sigma)$ is the union of these orbits, which is $\bigcup_{i=1}^r V(\operatorname{Cone}(v_i)) = \bigcup E_i$ by Theorem P8.6.25. Over $U_\sigma \setminus \{ \gamma_\sigma \} = U_{\operatorname{Cone}(v_0)} \cup U_{\operatorname{Cone}(v_{r+1})}$, $\pi$ is an isomorphism, as these two rays are cones of $\Sigma'$.

(3) $E_i = V(\operatorname{Cone}(v_i))$ is the closure of the orbit of a ray that lies in the two cones $\operatorname{Cone}(v_{i-1}, v_i)$ and $\operatorname{Cone}(v_i, v_{i+1})$, so it is isomorphic to $\mathbb{P}^1$ by Proposition P8.8.10. For $|i - j| = 1$, $E_i \cap E_j$ is the fixed point of the smooth cone $\operatorname{Cone}(v_i, v_j)$, where in the chart $\mathbb{A}^2$ the two curves are the coordinate axes, which meet transversally. For $|i - j| \geq 2$ no cone contains both rays, so $E_i \cap E_j = \emptyset$ by Theorem P8.6.25. Finally $v_{i-1} + v_{i+1} = b_i v_i$ is the wall relation of Corollary P8.8.13 for the wall $\operatorname{Cone}(v_i)$, so $E_i^2 = D_{v_i} \cdot V(\operatorname{Cone}(v_i)) = -b_i$.

*Theorem P8.8.4.* Let $\sigma$ be simplicial with ray generators $u_1, \dots, u_d$ and $L = \mathbb{Z} u_1 + \dots + \mathbb{Z} u_d$. Every element of $N_\sigma$ can be written uniquely as $\sum \lambda_i u_i$ with real $\lambda_i$, and subtracting the integer parts shows that the set $\Pi = \{ \sum \lambda_i u_i \in N_\sigma : 0 \leq \lambda_i < 1 \}$ is a set of representatives of $N_\sigma / L$. So $|\Pi| = \operatorname{mult}(\sigma)$, and if $\sigma$ is not smooth, $\Pi$ contains some $w \neq 0$. Replacing $w$ by the primitive vector on its ray keeps it in $\Pi$, since the coefficients only shrink. For $\lambda_i > 0$, the cone $\sigma_i$ generated by $w$ and the $u_j$, $j \neq i$, is simplicial, and
$$\det(u_1, \dots, w, \dots, u_d) = \lambda_i \det(u_1, \dots, u_d),$$
computed in a basis of $N_\sigma$, so $\operatorname{mult}(\sigma_i) = \lambda_i \operatorname{mult}(\sigma) < \operatorname{mult}(\sigma)$. The star subdivision $\Sigma^*(w)$ is a fan refining $\Sigma$ (Cox, Little and Schenck, Lemma 11.1.3), and its new cones are faces of the cones $\operatorname{Cone}(\tau, w)$ for $\tau$ a facet of a cone of $\Sigma$ containing $w$, each of which is of the form $\sigma_i$ for a cone $\sigma \ni w$, by the computation above applied to $\sigma$. So the new cones have multiplicity smaller than the largest multiplicity of a cone containing $w$, and the cones not containing $w$ are unchanged. Repeating, with induction on the largest multiplicity and the number of cones attaining it, ends with a smooth fan. Each step is an isomorphism over the open set $\bigcup U_\sigma$ for the smooth cones $\sigma$, as these are not subdivided, and by Theorem P8.6.27 this is the smooth locus. The existence of a simplicial refinement without new rays is Cox, Little and Schenck, Proposition 11.1.7, and is not proved here.

### Exercises

1. (A) Compute the continued fractions $\frac{7}{3}$, $\frac{7}{2}$ and $\frac{8}{3}$, and draw the resolutions of $\frac{1}{7}(1, 3)$, $\frac{1}{7}(1, 2)$ and $\frac{1}{8}(1, 3)$.
2. (A) Show that the resolution of $\frac{1}{d}(1, k)$ has exactly one exceptional curve if and only if $k = 1$.
3. (B) Show that the vectors $v_1, \dots, v_r$ of Theorem P8.8.3 are the lattice points on the compact edges of the boundary of the convex hull of $\sigma \cap N \setminus \{0\}$.
4. (B) Show that the minimal resolution of $\frac{1}{d}(1, k)$ and of $\frac{1}{d}(1, k')$ with $k k' \equiv 1 \pmod d$ have the same chain of curves in the opposite order, and that $\frac{1}{d}(1, k) \cong \frac{1}{d}(1, k')$ as varieties.
5. (B) Let $\Sigma'$ be the star subdivision of the fan of $\mathbb{A}^n$ at $e_1 + \dots + e_n$. Show that $X_{\Sigma'}$ is the blow-up of $\mathbb{A}^n$ at the origin, by comparing its charts with the charts of the blow-up in Chapter 11 of Volume P3.
6. (C) Let $\sigma = \operatorname{Cone}(e_1, e_2, e_1 + e_2 + d e_3)$ in $\mathbb{R}^3$ for $d \geq 2$. Compute the multiplicities of the cones after one star subdivision at a point of the half-open parallelepiped, and resolve $U_\sigma$ completely for $d = 3$.

### Lean

The refinement condition `MinimalModel.Toric.Fan.Refines` is in the repository: it says that every cone of the fan lies in a cone of a given set of cones and that every cone of the set is the union of the cones of the fan that it contains. It is used to state the steps of the toric minimal model program in Volume 3. The morphism $X_{\Sigma'} \to X_\Sigma$, the continued fraction resolution and Theorem P8.8.4 are not in Lean.

### Notes and history

The resolution of cyclic quotient surface singularities by continued fractions is due to Hirzebruch, in his 1953 paper on the resolution of surface singularities in $\mathbb{C}^2$ quotients, and to Jung for the underlying analytic method; the toric form is in Fulton, Section 2.6, and in Cox, Little and Schenck, Theorem 10.2.3. The toric resolution in all dimensions is due to Kempf, Knudsen, Mumford and Saint-Donat, who also show that the refinement can be chosen projective, by a sequence of star subdivisions; Cox, Little and Schenck, Theorem 11.1.9, is the standard reference. The dual graph of the resolution, a chain of rational curves with self-intersections $-b_i$, is the starting point of the classification of surface quotient singularities in Chapter 10.
