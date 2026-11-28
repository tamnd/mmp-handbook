---
title: Holomorphic line bundles and the exponential sequence
nodes: []
sources: [Huy05, GH78, Voi02a, BHPV04a]
reads_with: [Huy05:2.2, Huy05:2.3, Huy05:4.4, GH78:1.1]
requires: [P2.3, P2.7, P3.9, P6.2, P6.3, P6.4]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Holomorphic line bundles and the exponential sequence

### Statement

Throughout Chapters 5 and 6, $X$ is a connected complex manifold of dimension $n$, $\mathcal{O}_X$ is its sheaf of holomorphic functions, $\mathcal{O}_X^\times$ the sheaf of nowhere vanishing holomorphic functions under multiplication, $\mathcal{A}^k_X$ the sheaf of smooth complex $k$-forms and $\mathcal{A}^{p,q}_X$ the sheaf of smooth forms of type $(p, q)$, as in Chapter 2. Constant sheaves are written $\mathbb{Z}$, $\mathbb{R}$ and $\mathbb{C}$.

**Definition P6.5.1 (holomorphic line bundles and the Picard group).** A *holomorphic line bundle* on $X$ is a holomorphic vector bundle of rank $1$ in the sense of Chapter 2. Its sheaf of holomorphic sections is an invertible $\mathcal{O}_X$-module, and every invertible $\mathcal{O}_X$-module arises in this way from a line bundle that is unique up to isomorphism. The *Picard group* $\operatorname{Pic}(X)$ is the group of isomorphism classes of holomorphic line bundles, with the tensor product as group law, the trivial bundle as identity and the dual bundle $L^{-1} = L^\vee$ as inverse; by Theorem P2.6.29 it is the Picard group of the ringed space $(X, \mathcal{O}_X)$. Let $\mathcal{U} = (U_i)$ be an open cover and $e_i$ a nowhere vanishing holomorphic section of $L$ over $U_i$, a *local frame*. The *transition functions* of $L$ with respect to these frames are the functions $g_{ij} \in \mathcal{O}^\times(U_i \cap U_j)$ with
$$e_i = g_{ij} e_j \quad \text{on } U_{ij} = U_i \cap U_j.$$
They satisfy $g_{ii} = 1$ and the cocycle rule $g_{ik} = g_{ij} g_{jk}$ on $U_{ijk}$.

**Proposition P6.5.2 (the Picard group as cohomology).** Sending a line bundle to the class of its transition functions defines a group isomorphism
$$\operatorname{Pic}(X) \cong H^1(X, \mathcal{O}_X^\times).$$

Lean: not in Lean as stated.

A *meromorphic function* on an open set $U \subseteq X$ is a section over $U$ of the sheaf $\mathcal{M}_X$ whose stalk at $x$ is the field of fractions of the integral domain $\mathcal{O}_{X,x}$ (Chapter 1); $\mathcal{M}_X^\times$ is the sheaf of meromorphic functions that are not zero divisors, that is, that do not vanish identically on any open subset of their domain.

**Definition P6.5.3 (divisors and their line bundles).** A *divisor* on $X$ is a global section $D$ of the sheaf $\mathcal{M}_X^\times / \mathcal{O}_X^\times$. It is given by an open cover $(U_i)$ and functions $f_i \in \mathcal{M}^\times(U_i)$, the *local equations*, with $f_i / f_j \in \mathcal{O}^\times(U_{ij})$; two systems define the same divisor if their union is again a system of local equations. The divisor is *effective* if every $f_i$ is holomorphic, and *principal* if it is defined by one $f \in \mathcal{M}^\times(X)$, written $D = \operatorname{div}(f)$. Divisors form a group $\operatorname{Div}(X)$ under multiplication of local equations, written additively. The line bundle $\mathcal{O}_X(D)$ is the subsheaf of $\mathcal{M}_X$ equal to $f_i^{-1} \mathcal{O}_{U_i}$ on $U_i$; the functions $e_i = f_i^{-1}$ are local frames with transition functions $g_{ij} = f_j / f_i$.

Since $\mathcal{O}_{X,x}$ is a unique factorization domain (Chapter 1), a divisor is the same as a locally finite formal sum $\sum_j a_j D_j$ of irreducible hypersurfaces with integer coefficients, the coefficient $a_j$ being the order of vanishing of $f_i$ along $D_j$; this is the analytic form of Theorem P3.9.10, and the handbook does not use it below except in the examples.

**Proposition P6.5.4 (divisors and line bundles).** Let $D, D'$ be divisors on $X$.

1. $\mathcal{O}_X(D + D') \cong \mathcal{O}_X(D) \otimes \mathcal{O}_X(D')$, so $D \mapsto \mathcal{O}_X(D)$ is a homomorphism $\operatorname{Div}(X) \to \operatorname{Pic}(X)$. Its kernel is the group of principal divisors.
2. If $D$ is effective, the constant function $1$ is a global section $s_D$ of $\mathcal{O}_X(D)$ whose local expression in the frame $e_i$ is $f_i$; it vanishes exactly along $D$.
3. A line bundle $L$ is isomorphic to $\mathcal{O}_X(D)$ for some divisor $D$ if and only if $L$ has a meromorphic section that is not a zero divisor, that is, a section of $L \otimes \mathcal{M}_X$ that is locally $f e$ with $e$ a frame and $f \in \mathcal{M}^\times$. It is isomorphic to $\mathcal{O}_X(D)$ with $D$ effective if and only if $L$ has a holomorphic section that is not identically zero.

Lean: not in Lean as stated.

The exponential map $f \mapsto \exp(2 \pi i f)$ is a homomorphism of sheaves of groups $\mathcal{O}_X \to \mathcal{O}_X^\times$. Its kernel is the sheaf of locally constant integer valued functions, and it is surjective on stalks, since a nowhere vanishing holomorphic function on a ball has a holomorphic logarithm. So there is an exact sequence of sheaves, the *exponential sequence*,
$$0 \to \mathbb{Z} \to \mathcal{O}_X \xrightarrow{\exp(2\pi i \,\cdot\,)} \mathcal{O}_X^\times \to 0. \tag{5.1}$$

**Definition P6.5.5 (the first Chern class).** The *first Chern class* of a holomorphic line bundle $L$ is the image $c_1(L) \in H^2(X, \mathbb{Z})$ of its class under the connecting map $H^1(X, \mathcal{O}_X^\times) \to H^2(X, \mathbb{Z})$ of (5.1). Concretely, let $\mathcal{U}$ be a cover whose finite intersections are contractible, $g_{ij}$ transition functions of $L$ on it, and $f_{ij} = \frac{1}{2 \pi i} \log g_{ij}$ a choice of logarithm on $U_{ij}$. Then
$$c_{ijk} = f_{jk} - f_{ik} + f_{ij} \in \mathbb{Z}$$
is a Čech $2$-cocycle with values in $\mathbb{Z}$, and $c_1(L)$ is its class. Write $c_1(L)_{\mathbb{R}}$ for the image of $c_1(L)$ in $H^2(X, \mathbb{R})$, identified with de Rham cohomology.

**Proposition P6.5.6 (Chern-Weil and the exponential sequence).** Let $h$ be a Hermitian metric on $L$, with Chern curvature $\Theta_h$, given on a set with frame $e$ by $\Theta_h = -\partial \bar\partial \log |e|^2_h$ (Chapter 3).

1. $\frac{i}{2\pi} \Theta_h$ is a closed real $(1,1)$-form, and its de Rham class does not depend on $h$.
2. Its de Rham class is $c_1(L)_\mathbb{R}$.
3. $c_1(L \otimes M) = c_1(L) + c_1(M)$, $c_1(L^{-1}) = -c_1(L)$, and $c_1(f^* L) = f^* c_1(L)$ for a holomorphic map $f \colon Y \to X$.

Lean: not in Lean as stated.

**Lemma P6.5.7 (the map from $H^k(X, \mathbb{C})$ to $H^k(X, \mathcal{O}_X)$).** Let $\iota \colon H^k(X, \mathbb{C}) \to H^k(X, \mathcal{O}_X)$ be induced by the inclusion $\mathbb{C} \to \mathcal{O}_X$. Under the de Rham isomorphism and the Dolbeault isomorphism $H^k(X, \mathcal{O}_X) \cong H^{0,k}_{\bar\partial}(X)$ of Chapter 2, $\iota$ sends the class of a closed $k$-form $\alpha$ to the class of its component $\alpha^{0,k}$ of type $(0, k)$. If $X$ is compact Kähler, $\iota$ is the projection onto the summand $H^{0,k}(X)$ in the Hodge decomposition $H^k(X, \mathbb{C}) = \bigoplus_{p + q = k} H^{p,q}(X)$ of Chapter 4.

Lean: not in Lean as stated.

**Theorem P6.5.8 (the Picard variety).** Let $X$ be a compact Kähler manifold and $q = h^{0,1}(X)$.

1. The map $H^1(X, \mathbb{Z}) \to H^1(X, \mathcal{O}_X)$ of (5.1) is injective, and its image is a lattice in the complex vector space $H^1(X, \mathcal{O}_X) \cong \mathbb{C}^q$. In particular $b_1(X) = 2q$.
2. The group $\operatorname{Pic}^0(X) = \ker(c_1)$ of line bundles with trivial first Chern class is isomorphic to the compact complex torus $H^1(X, \mathcal{O}_X) / H^1(X, \mathbb{Z})$ of dimension $q$, the *Picard variety* of $X$.
3. There is an exact sequence
$$0 \to \operatorname{Pic}^0(X) \to \operatorname{Pic}(X) \xrightarrow{c_1} H^2(X, \mathbb{Z}) \to H^2(X, \mathcal{O}_X),$$
and the image $\operatorname{NS}(X)$ of $c_1$ is a finitely generated abelian group.

Lean: not in Lean as stated.

### Proof in words

Line bundles are glued from trivial pieces, and the gluing data are transition functions, which form a Čech cocycle with values in $\mathcal{O}_X^\times$; this is the general statement for ringed spaces, Theorem P2.7.28. The exponential sequence turns the multiplicative group $\mathcal{O}_X^\times$ into the additive group $\mathcal{O}_X$ modulo the integers, and its connecting map gives an integral class $c_1(L)$. Over the reals the same class is computed by a metric: the curvature form of any Hermitian metric is closed, two metrics differ by a positive function whose logarithm changes the curvature by an exact form, and the Čech to de Rham zigzag applied to $\frac{i}{2\pi} \Theta_h$ produces exactly the cocycle $f_{jk} - f_{ik} + f_{ij}$ that defines $c_1(L)$.

The rest of the long exact sequence of (5.1) describes $\operatorname{Pic}(X)$. Its kernel part is $H^1(X, \mathcal{O}_X)$ modulo the image of $H^1(X, \mathbb{Z})$. The map $H^1(X, \mathbb{C}) \to H^1(X, \mathcal{O}_X)$ is the projection to the $(0,1)$-part, and on a compact Kähler manifold the Hodge decomposition says that this projection is a real isomorphism from $H^1(X, \mathbb{R})$ onto $H^{0,1}(X)$: a real class whose $(0,1)$-part vanishes has vanishing $(1,0)$-part too, because the two parts are complex conjugate. So the integral classes form a lattice and the quotient is a torus.

### Examples

**Example P6.5.9 (projective space).** Let $X = \mathbb{P}^n$. Its Betti numbers are $b_{2k} = 1$ for $0 \leq k \leq n$ and $b_j = 0$ for odd $j$, and $H^2(\mathbb{P}^n, \mathbb{Z}) \cong \mathbb{Z}$ (the cell decomposition $\mathbb{P}^n = \mathbb{C}^n \cup \mathbb{C}^{n-1} \cup \cdots \cup \mathbb{C}^0$). The Hodge decomposition of Chapter 4 gives $\sum_{p+q = k} h^{p,q} = b_k$, and $h^{k,k} \geq 1$ for $k \leq n$ because the power $\omega^k$ of a Kähler form has $\int_{\mathbb{P}^k} \omega^k > 0$ on a linear subspace, so its class is not zero. Hence $h^{p,q} = 0$ for $p \neq q$, and in particular $H^1(\mathbb{P}^n, \mathcal{O}) = H^2(\mathbb{P}^n, \mathcal{O}) = 0$ by the Dolbeault isomorphism. Theorem P6.5.8 gives
$$c_1 \colon \operatorname{Pic}(\mathbb{P}^n) \xrightarrow{\ \sim\ } H^2(\mathbb{P}^n, \mathbb{Z}) \cong \mathbb{Z}.$$
The hyperplane bundle $\mathcal{O}(1)$ maps to a generator: by Proposition P6.5.20 in Section 5.3, $\frac{i}{2\pi} \Theta$ for the Fubini-Study metric integrates to $1$ over a line, so $c_1(\mathcal{O}(1))$ pairs to $1$ with the generator of $H_2(\mathbb{P}^n, \mathbb{Z})$ given by a line. So every holomorphic line bundle on $\mathbb{P}^n$ is $\mathcal{O}(d)$ for a unique $d \in \mathbb{Z}$, the analytic counterpart of Theorem P3.8.20.

**Example P6.5.10 (curves and the Jacobian).** Let $X$ be a compact Riemann surface of genus $g$, so $b_1 = 2g$, $H^2(X, \mathbb{Z}) \cong \mathbb{Z}$ through the orientation, and $H^2(X, \mathcal{O}_X) = H^{0,2}(X) = 0$ for dimension reasons. Theorem P6.5.8 gives an exact sequence
$$0 \to J(X) \to \operatorname{Pic}(X) \xrightarrow{\deg} \mathbb{Z} \to 0, \qquad J(X) = H^1(X, \mathcal{O}_X) / H^1(X, \mathbb{Z}) \cong \mathbb{C}^g / \mathbb{Z}^{2g},$$
where $\deg L = \int_X c_1(L)$. The degree of $\mathcal{O}_X(D)$ is $\deg D = \sum a_j$ for $D = \sum a_j p_j$. It suffices to treat $D = p$, by Proposition P6.5.6, part 3, and Proposition P6.5.4, part 1. Choose a metric $h$ on $L = \mathcal{O}_X(p)$, put $u = \log |s_p|^2_h$ on $X \setminus \{p\}$, where $s_p$ is the section of Proposition P6.5.4, part 2, and let $z$ be a coordinate centred at $p$, so that $u = \log |z|^2 + \psi$ with $\psi$ smooth near $p$. Since $s_p$ is a frame on $X \setminus \{p\}$, $\Theta_h = -\partial \bar\partial u = -d \bar\partial u$ there. Let $\Delta_r = \{|z| < r\}$. By Stokes' theorem, with $\partial \Delta_r$ oriented counterclockwise,
$$\int_{X \setminus \Delta_r} \frac{i}{2\pi} \Theta_h = -\frac{i}{2\pi} \int_{X \setminus \Delta_r} d \bar\partial u = \frac{i}{2\pi} \int_{\partial \Delta_r} \Big( \frac{d\bar z}{\bar z} + \bar\partial \psi \Big).$$
Here $\int_{|z| = r} d\bar z / \bar z = \overline{\int_{|z| = r} dz / z} = -2\pi i$ and $\int_{|z|=r} \bar\partial \psi \to 0$ as $r \to 0$. Letting $r \to 0$, $\deg \mathcal{O}_X(p) = \frac{i}{2\pi} \cdot (-2\pi i) = 1$. For $g = 1$ and $X = \mathbb{C}/\Lambda$, $J(X)$ is again an elliptic curve, and the map $p \mapsto \mathcal{O}_X(p - p_0)$ identifies it with $X$ (Abel's theorem, GH78, Chapter 2, Section 2).

### Proof

*Proposition P6.5.2.* A holomorphic line bundle and its sheaf of sections determine each other up to isomorphism: the sheaf of sections of a line bundle is locally isomorphic to $\mathcal{O}_X$, and conversely an invertible sheaf with trivializations $\mathcal{O}_{U_i} \cong \mathcal{L}|_{U_i}$ is the sheaf of sections of the line bundle glued from the $U_i \times \mathbb{C}$ by the same transition functions (Chapter 2). The tensor product of line bundles corresponds to the tensor product of sheaves. Theorem P2.7.28, applied to the ringed space $(X, \mathcal{O}_X)$, identifies the group of invertible sheaves with $H^1(X, \mathcal{O}_X^\times)$ through their transition functions.

*Proposition P6.5.4.* Part 1: if $D$ and $D'$ have local equations $f_i$, $f'_i$ on a common cover, then $D + D'$ has local equations $f_i f'_i$, and multiplication $\mathcal{O}(D) \otimes \mathcal{O}(D') \to \mathcal{M}_X$ maps the tensor product isomorphically onto $(f_i f'_i)^{-1} \mathcal{O}_{U_i}$, since on $U_i$ both sides are free of rank one with generators $f_i^{-1} \otimes f_i'^{-1}$ and $(f_i f_i')^{-1}$. If $D = \operatorname{div}(f)$, multiplication by $f$ is an isomorphism $\mathcal{O}_X(D) \to \mathcal{O}_X$. Conversely, an isomorphism $\varphi \colon \mathcal{O}_X \to \mathcal{O}_X(D)$ sends $1$ to a global section $f^{-1} = \varphi(1) \in \mathcal{M}^\times(X)$ which on $U_i$ is a unit multiple $u_i f_i^{-1}$, so $f = u_i^{-1} f_i$ and $D = \operatorname{div}(f)$. Part 2: if every $f_i$ is holomorphic, $1 = f_i \cdot f_i^{-1}$ is a holomorphic section of $f_i^{-1} \mathcal{O}_{U_i}$, with coefficient $f_i$ in the frame $e_i = f_i^{-1}$, and it vanishes where $f_i$ does. Part 3: a section $s$ of $L \otimes \mathcal{M}_X$ that is locally $s = f_i e_i$ with $f_i \in \mathcal{M}^\times(U_i)$ defines the divisor $D$ with local equations $f_i$, because $e_i = g_{ij} e_j$ gives $f_j = g_{ij} f_i$ and $f_i / f_j = g_{ij}^{-1}$ is a unit. The map $\mathcal{O}_X(D) \to L$, $\phi \mapsto \phi s$, sends the frame $f_i^{-1}$ to $e_i$, so it is an isomorphism. Conversely $\mathcal{O}_X(D)$ has the section $1$, which is $f_i \cdot f_i^{-1}$ locally. For the effective statement, a holomorphic section that is not identically zero is locally $f_i e_i$ with $f_i$ holomorphic, and $f_i$ does not vanish identically on any open set because $X$ is connected and the zero set of a nonzero holomorphic section has empty interior by the identity theorem of Chapter 1.

*Proposition P6.5.6.* Part 1: on $U_i$ write $h_i = |e_i|_h^2$, a positive smooth function. Since $e_i = g_{ij} e_j$, $h_i = |g_{ij}|^2 h_j$ and $\log h_i - \log h_j = \log g_{ij} + \overline{\log g_{ij}}$ on simply connected pieces of $U_{ij}$, so $\partial \bar\partial \log h_i = \partial \bar\partial \log h_j$ because $\partial\bar\partial$ kills holomorphic and antiholomorphic functions. So $\Theta_h$ is a global form of type $(1,1)$. It is closed, since locally $\Theta_h = d(\partial \log h_i)$, using $d \partial u = \bar\partial \partial u = - \partial \bar\partial u$ for a function $u$. It is purely imaginary: $\overline{\partial \bar\partial u} = \bar\partial \partial u = -\partial \bar\partial u$ for real $u$, so $\frac{i}{2\pi} \Theta_h$ is real. A second metric is $h' = e^{-\varphi} h$ with $\varphi$ a smooth real function on $X$, and $\Theta_{h'} = \Theta_h + \partial \bar\partial \varphi = \Theta_h + d \bar\partial \varphi$. Since $\frac{i}{2\pi}\partial\bar\partial\varphi$ is real and exact as a complex form, it is $d$ of the real form $\operatorname{Re}(\frac{i}{2\pi} \bar\partial \varphi)$, so the real classes agree.

Part 2: take the cover of Definition P6.5.5, refined so that each $U_i$ carries a frame; its finite intersections are contractible, so the Čech complexes of $\mathbb{Z}$, $\mathbb{R}$ and $\mathbb{C}$ on it compute sheaf cohomology (Theorem P2.7.21, with the vanishing of the cohomology of constant sheaves on contractible manifolds) and the Poincaré lemma holds on each $U_{i_0 \cdots i_p}$. The de Rham isomorphism $H^2_{\mathrm{dR}}(X) \cong \check{H}^2(\mathcal{U}, \mathbb{R})$ is the zigzag of the Čech-de Rham double complex: a closed real $2$-form $\omega$ is written $\omega = d\alpha_i$ on $U_i$, then $\alpha_j - \alpha_i = d\beta_{ij}$ on $U_{ij}$, and then $\beta_{jk} - \beta_{ik} + \beta_{ij}$ is a constant $c_{ijk}$, whose class is the image of $[\omega]$; this is the convention of Griffiths and Harris (GH78, Chapter 0, Section 3, and Chapter 1, Section 1). Apply it to $\omega = \frac{i}{2\pi} \Theta_h$. Take $\alpha_i = \frac{i}{2\pi} \partial \log h_i$, so that $d\alpha_i = \frac{i}{2\pi} \bar\partial \partial \log h_i = \omega$. On $U_{ij}$, $\log h_j - \log h_i = -\log g_{ij} - \overline{\log g_{ij}}$, so
$$\alpha_j - \alpha_i = -\frac{i}{2\pi} \partial \log g_{ij} = \frac{1}{2\pi i} d \log g_{ij} = d f_{ij}.$$
So $\beta_{ij} = f_{ij}$ is a valid choice, and $c_{ijk} = f_{jk} - f_{ik} + f_{ij}$, the cocycle of Definition P6.5.5. The complex valued $\alpha_i$ and $\beta_{ij}$ compute the image in $\check{H}^2(\mathcal{U}, \mathbb{C})$; since the resulting cocycle is integral and the map $\check H^2(\mathcal{U}, \mathbb{R}) \to \check H^2(\mathcal{U}, \mathbb{C})$ is injective, the real class of $\omega$ is the image of $c_1(L)$.

Part 3: transition functions of $L \otimes M$, $L^{-1}$ and $f^*L$ are $g_{ij} g'_{ij}$, $g_{ij}^{-1}$ and $g_{ij} \circ f$, and one may take logarithms $f_{ij} + f'_{ij}$, $-f_{ij}$ and $f_{ij} \circ f$.

*Lemma P6.5.7.* The complexes $(\mathcal{A}^\bullet_X, d)$ and $(\mathcal{A}^{0, \bullet}_X, \bar\partial)$ are resolutions of $\mathbb{C}$ and of $\mathcal{O}_X$ by fine sheaves, by the Poincaré lemma and the Dolbeault-Grothendieck lemma of Chapter 1, and fine sheaves are acyclic. The projection $\pi^{0, \bullet} \colon \mathcal{A}^k \to \mathcal{A}^{0,k}$ onto the $(0,k)$-component is a map of complexes: for a $k$-form $\alpha = \sum_{p+q=k} \alpha^{p,q}$, the $(0, k+1)$-component of $d\alpha = \sum (\partial + \bar\partial) \alpha^{p,q}$ is $\bar\partial \alpha^{0,k}$. In degree $0$ it restricts to the inclusion $\mathbb{C} \to \mathcal{O}_X$. A map of acyclic resolutions lying over a map of sheaves induces on global sections the map of derived functors (Theorem P2.3.11 and Theorem P2.3.25), so $\iota[\alpha] = [\alpha^{0,k}]$. If $X$ is compact Kähler, let $\alpha$ be the harmonic representative of a class; its components $\alpha^{p,q}$ are harmonic, the class of $\alpha^{p,q}$ is the $(p,q)$-summand of the Hodge decomposition, and $[\alpha^{0,k}] \in H^{0,k}_{\bar\partial}(X)$ is identified with the summand $H^{0,k}(X)$ through harmonic forms (Chapter 4). So $\iota$ is the projection.

*Theorem P6.5.8.* The long exact cohomology sequence of (5.1) reads
$$H^0(X, \mathcal{O}_X) \to H^0(X, \mathcal{O}_X^\times) \to H^1(X, \mathbb{Z}) \to H^1(X, \mathcal{O}_X) \to \operatorname{Pic}(X) \xrightarrow{c_1} H^2(X, \mathbb{Z}) \to H^2(X, \mathcal{O}_X).$$
Since $X$ is compact and connected, global holomorphic functions are constant (maximum principle, Chapter 2), so the first map is $\exp(2\pi i \,\cdot\,) \colon \mathbb{C} \to \mathbb{C}^\times$, which is surjective. Hence $H^1(X, \mathbb{Z}) \to H^1(X, \mathcal{O}_X)$ is injective, and part 3 follows from exactness at $\operatorname{Pic}(X)$, with $\operatorname{Pic}^0(X) \cong H^1(X, \mathcal{O}_X)/H^1(X, \mathbb{Z})$. The group $H^2(X, \mathbb{Z})$ of a compact manifold is finitely generated, so its subgroup $\operatorname{NS}(X)$ is too.

For part 1, the map $\mathbb{Z} \to \mathcal{O}_X$ factors through $\mathbb{R} \to \mathbb{C} \to \mathcal{O}_X$, so the map in question is the composite
$$H^1(X, \mathbb{Z}) \to H^1(X, \mathbb{R}) \xrightarrow{\ r\ } H^1(X, \mathcal{O}_X).$$
The group $H^1(X, \mathbb{Z}) = \operatorname{Hom}(H_1(X, \mathbb{Z}), \mathbb{Z})$ is free of rank $b_1$, and by the universal coefficient theorem its image in $H^1(X, \mathbb{R}) = H^1(X, \mathbb{Z}) \otimes \mathbb{R}$ is a lattice. It remains to show that the real linear map $r$ is bijective. By Lemma P6.5.7, $r$ sends the class of a real harmonic $1$-form $\alpha = \alpha^{1,0} + \alpha^{0,1}$ to the class of $\alpha^{0,1}$ in $H^{0,1}(X)$. Since $\alpha$ is real, $\alpha^{1,0} = \overline{\alpha^{0,1}}$. If $r[\alpha] = 0$, then the harmonic form $\alpha^{0,1}$ represents zero, so it vanishes (Chapter 4), and $\alpha^{1,0} = 0$ as well; so $r$ is injective. The Hodge decomposition $H^1(X, \mathbb{C}) = H^{1,0} \oplus H^{0,1}$ with $H^{1,0} = \overline{H^{0,1}}$ gives $b_1 = 2 h^{0,1}$, so $\dim_\mathbb{R} H^1(X, \mathbb{R}) = b_1 = 2q = \dim_\mathbb{R} H^1(X, \mathcal{O}_X)$, and the injective map $r$ is bijective. A real linear isomorphism carries a lattice to a lattice, and the quotient of $\mathbb{C}^q$ by a lattice is a compact complex torus of dimension $q$, the group law on $\operatorname{Pic}^0(X)$ corresponding to addition.

### Exercises

1. (A) Let $X = \mathbb{P}^1$ with the cover $U_0 = \{z_0 \neq 0\}$, $U_1 = \{z_1 \neq 0\}$ and frames $e_0 = z_0$, $e_1 = z_1$ of $\mathcal{O}(1)$. Compute the transition function $g_{01}$ in the coordinate $t = z_1 / z_0$, and the transition function of $\mathcal{O}(d)$.
2. (A) Show that the canonical bundle $K_X = \bigwedge^n T^*X$ of a complex manifold has transition functions $\det(\partial w / \partial z)$ in the frames $dz_1 \wedge \cdots \wedge dz_n$ and $dw_1 \wedge \cdots \wedge dw_n$ of two charts, with the convention of Definition P6.5.1. Compute $K_{\mathbb{P}^1}$ and show that $\deg K_{\mathbb{P}^1} = -2$.
3. (B) Let $h$ be a Hermitian metric on a line bundle $L$ over a compact Riemann surface and $s$ a meromorphic section with divisor $D$. Generalize the computation of Example P6.5.10 to show $\int_X \frac{i}{2\pi} \Theta_h = \deg D$.
4. (B) Let $X = \mathbb{C}^n / \Lambda$ be a complex torus. Show that $H^1(X, \mathcal{O}_X) \cong \overline{V}^*$, the space of conjugate linear forms on $V = \mathbb{C}^n$, using the translation invariant forms $d\bar z_1, \dots, d\bar z_n$, and describe $\operatorname{Pic}^0(X)$ as the dual torus $\overline{V}^* / \Lambda^*$ with $\Lambda^* = \{ \ell : \operatorname{Im} \ell(\Lambda) \subseteq \mathbb{Z} \}$.
5. (B) Show that a line bundle $L$ on a compact Kähler manifold with $c_1(L)$ torsion in $H^2(X, \mathbb{Z})$ admits a Hermitian metric with $\Theta_h = 0$. Hint: Proposition P6.5.6 and the $\partial\bar\partial$-lemma of Chapter 4.
6. (C) Let $X$ be compact Kähler and $L \in \operatorname{Pic}^0(X)$. Show that $L$ is defined by transition functions that are constants of absolute value $1$, that is, $L$ comes from a unitary character of $\pi_1(X)$. Hint: write the class of $L$ in $H^1(X, \mathcal{O}_X)$ as the image of a harmonic form $\alpha^{0,1}$ and use $\alpha = \alpha^{0,1} - \overline{\alpha^{0,1}}$.

### Lean

Mathlib has complex manifolds as manifolds modelled on $\mathbb{C}^n$ and holomorphic functions of several variables, but no holomorphic line bundles, no Dolbeault cohomology and no Hodge decomposition, so nothing in this section is formalized. The project library has no node here.

### Notes and history

The exponential sequence and the description of the Picard group by sheaf cohomology go back to Kodaira and Spencer and to Serre's work on coherent sheaves in the early 1950s; the presentation follows Griffiths and Harris, Chapter 1, Section 1 (GH78), and Huybrechts, Sections 2.2, 2.3 and 4.4 (Huy05). The Picard variety of a compact Kähler manifold, as the torus $H^1(X, \mathcal{O}_X)/H^1(X, \mathbb{Z})$, is due to Picard for surfaces and to Weil and Kodaira in general; Voisin, Chapters 7 and 12 (Voi02a), treats it with the Albanese torus, its dual. The sign in Proposition P6.5.6 depends on the conventions for transition functions and for the Čech to de Rham zigzag; with the conventions fixed here, $\deg \mathcal{O}(p) = 1$ on a curve, which pins it down. Theorem P6.5.8 fails without the Kähler hypothesis: on a Hopf surface $b_1 = 1$ while $h^{0,1} = 1$, so the image of $H^1(X, \mathbb{Z})$ in $H^1(X, \mathcal{O}_X) \cong \mathbb{C}$ is not a lattice and $\operatorname{Pic}^0$ is $\mathbb{C}^\times$ (BHPV04a, Chapter V).
