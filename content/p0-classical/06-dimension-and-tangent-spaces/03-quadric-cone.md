---
title: The quadric cone as a quotient of the plane
nodes: []
sources: [Rei88, Har77, Sha13, Rei97]
reads_with: [Rei88:ch6, Har77:I.5, Sha13:ch2]
requires: [P0.3, P0.4, P0.5]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The quadric cone as a quotient of the plane

### Statement

In this section $\operatorname{char} k \neq 2$.

**Definition P0.6.22.** The *quadric cone* is the surface $Q = V(uw - v^2) \subset \mathbb{A}^3$. The linear change of coordinates $u = z + x$, $w = z - x$, $v = y$ turns $uw - v^2$ into $z^2 - x^2 - y^2$, so $Q$ is isomorphic to the cone $V(x^2 + y^2 - z^2)$. Its singular point at the origin is called the $A_1$ singularity, or the quotient singularity $\frac12(1,1)$.

Lean: not in Lean.

**Example P0.6.23.** The plane section $Q \cap \{w = 1\}$ is the parabola $u = v^2$, which is nonsingular. The projective closure of $Q$ in $\mathbb{P}^3$ meets the plane at infinity in the conic $uw = v^2$. So $Q$ is the affine cone over a nonsingular conic.

**Example P0.6.24.** For each $(\alpha : \beta) \in \mathbb{P}^1$, the line $\{(\alpha^2 \lambda, \alpha\beta\lambda, \beta^2 \lambda) : \lambda \in k\}$ lies in $Q$ and passes through $0$. Every point $(u, v, w) \neq 0$ of $Q$ lies on exactly one of these lines, the line of the point $(u : v : w)$ of the conic. These are the rulings of the cone.

**Definition P0.6.25.** Let a finite group $G$ act on $\mathbb{A}^n$ by linear maps. Then $G$ acts on $k[x_1, \dots, x_n]$ by $(g \cdot h)(P) = h(g^{-1} P)$. The *ring of invariants* is $k[x_1, \dots, x_n]^G = \{h : g \cdot h = h \text{ for all } g \in G\}$. The quotient $\mathbb{A}^n/G$ is the affine variety with coordinate ring $k[x_1, \dots, x_n]^G$ (it is of finite type by a theorem of Emmy Noether, and P8 Ch. 9 treats such quotients). For $G = \{\pm 1\}$ acting on $\mathbb{A}^2$ by $(s, t) \mapsto (-s, -t)$, the quotient is the $\frac12(1,1)$ singularity: the weights $(1, 1)$ are the exponents of $-1$ on the two coordinates.

Lean: Mathlib `FixedPoints.subalgebra` (the subalgebra of elements fixed by a group action).

**Example P0.6.26.** The group $\{\pm 1\}$ acts on $k[s]$ by $s \mapsto -s$. A polynomial is invariant if and only if it is even, so $k[s]^{\pm 1} = k[s^2]$, a polynomial ring. The quotient $\mathbb{A}^1/\{\pm 1\}$ is $\mathbb{A}^1$, and the quotient map is $s \mapsto s^2$.

**Example P0.6.27.** The group $\{\pm 1\}$ acts on $\mathbb{A}^2$ by $(s, t) \mapsto (-s, t)$. The ring of invariants is $k[s^2, t]$, a polynomial ring, and the quotient is $\mathbb{A}^2$. A reflection gives a nonsingular quotient. The action by $-1$ on both coordinates has no reflection, and the quotient is singular, by the theorem below.

**Theorem P0.6.28 (the quadric cone is $\mathbb{A}^2/\pm 1$).** Let $G = \{\pm 1\}$ act on $\mathbb{A}^2$ by $(s, t) \mapsto (-s, -t)$, and let $R = k[s, t]$.

1. $R^G = k[s^2, st, t^2]$, and the homomorphism $\varphi : k[u, v, w] \to R^G$, $u \mapsto s^2$, $v \mapsto st$, $w \mapsto t^2$, is surjective with kernel $(uw - v^2)$. So $R^G \cong k[Q]$.
2. The morphism $q : \mathbb{A}^2 \to Q$, $q(s, t) = (s^2, st, t^2)$, is surjective, and $q(P) = q(P')$ if and only if $P' = \pm P$. So the points of $Q$ are the orbits of $G$.
3. $Q$ is a surface, and its only singular point is $0$, with $\dim T_0 Q = 3$.

Lean: not in Lean.

*Proof.* Part 1. The element $-1$ maps the monomial $s^i t^j$ to $(-1)^{i+j} s^i t^j$. Since $-1 \neq 1$ in $k$, a polynomial is invariant if and only if each of its monomials has $i + j$ even. Such a monomial is a product of $s^2$, $st$ and $t^2$: for $i \leq j$ it is $(st)^i (t^2)^{(j-i)/2}$, and for $i > j$ it is $(st)^j (s^2)^{(i-j)/2}$. So $R^G = k[s^2, st, t^2]$ and $\varphi$ is surjective. Clearly $uw - v^2 \in \ker \varphi$. Conversely, modulo $uw - v^2$ every $h \in k[u, v, w]$ is congruent to $A(u, w) + v B(u, w)$: replace $v^2$ by $uw$ until $v$ occurs with exponent at most $1$. If $\varphi(A + vB) = 0$, then

$$ A(s^2, t^2) + st \, B(s^2, t^2) = 0. $$

All monomials of $A(s^2, t^2)$ have even exponents of $s$, and all monomials of $st B(s^2, t^2)$ have odd exponents of $s$. So both terms are zero. Since $s^2$ and $t^2$ are algebraically independent, $A = B = 0$. So $\ker \varphi = (uw - v^2)$. In particular $k[u, v, w]/(uw - v^2)$ is a subring of $k[s, t]$, so it is a domain, $(uw - v^2)$ is prime, and $I(Q) = (uw - v^2)$, $k[Q] \cong R^G$.

Part 2. Let $(u, v, w) \in Q$. If $u \neq 0$, choose $s$ with $s^2 = u$ and put $t = v/s$. Then $st = v$ and $t^2 = v^2/u = w$. If $u = 0$, then $v^2 = uw = 0$, so $v = 0$; choose $s = 0$ and $t$ with $t^2 = w$. So $q$ is surjective. Clearly $q(-P) = q(P)$. Suppose that $q(s, t) = q(s', t')$. Then $s' = \varepsilon s$ and $t' = \delta t$ with $\varepsilon, \delta \in \{\pm 1\}$. If $st \neq 0$, then $s't' = st$ gives $\varepsilon \delta = 1$, so $\varepsilon = \delta$. If $s = 0$, then $s' = 0$ and $(s', t') = \delta (s, t)$. If $t = 0$, then $(s', t') = \varepsilon (s, t)$.

Part 3. By Part 1, $Q = V(uw - v^2)$ with $uw - v^2$ irreducible, so $\dim Q = 2$ by Section 6.1, and the Jacobian criterion applies with $I(Q) = (uw - v^2)$. The Jacobian matrix is $(w, -2v, u)$. It is zero only at $u = v = w = 0$, because $2 \neq 0$. At other points its rank is $1 = 3 - 2$, so they are nonsingular. At $0$ the rank is $0$, so $\dim T_0 Q = 3 > 2$. $\square$

### Proof in words

The invariants of $-1$ are the polynomials of even degree, and the even degree monomials are generated by the three quadrics $s^2$, $st$, $t^2$. The only relation between them is $s^2 \cdot t^2 = (st)^2$. The proof of this uses a normal form: modulo the relation, an element is $A(u, w) + v B(u, w)$, and the two parts have different parities after substitution. The geometry follows: a square root gives the surjectivity of $q$, and the Jacobian matrix $(w, -2v, u)$ vanishes only at the vertex.

### Examples

**Example P0.6.29.** The function field of $Q$ is $k(s^2, st) = k(s, t)^G$: it contains $t^2 = (st)^2/s^2$. The extension $k(s, t)/k(Q)$ has degree $2$, because $s$ satisfies $X^2 - s^2 = 0$, $t = (st)/s$, and $s \notin k(Q)$ (it is not invariant). So the quotient map $q$ has degree $2$. Its fibre over a point of $Q \setminus \{0\}$ has two points, and its fibre over $0$ has one point.

**Example P0.6.30.** In characteristic $2$ the hypothesis fails and the conclusion fails. Then $-1 = 1$, so the action is trivial, $R^G = k[s, t]$, and $\mathbb{A}^2/G = \mathbb{A}^2$ is nonsingular. The ring $k[s^2, st, t^2]$ is still isomorphic to $k[Q]$, by the same proof with "even degree" in place of "invariant", but it is no longer a ring of invariants of $\pm 1$. (It is the ring of invariants of the group scheme $\mu_2$, which is outside this chapter.)

### Exercises

1. (A) Show that $Q$ is not isomorphic to $\mathbb{A}^2$.
2. (A) Let $\operatorname{char} k \neq 3$ and let $\zeta$ be a primitive cube root of $1$. Let $\mathbb{Z}/3$ act on $\mathbb{A}^2$ by $(s, t) \mapsto (\zeta s, \zeta t)$. Show that the ring of invariants is $k[s^3, s^2 t, s t^2, t^3]$. This is the $\frac13(1,1)$ singularity.
3. (A) Show that the quotient in Exercise 2 is the affine cone over the twisted cubic in $\mathbb{P}^3$, and that its tangent space at $0$ has dimension $4$.
4. (B) Show that the quotient map $q$ maps each line through $0$ in $\mathbb{A}^2$ onto a ruling of $Q$, and that the map from lines in $\mathbb{A}^2$ through $0$ to rulings of $Q$ is a bijection.
5. (B) Let $\widetilde{Q} \subset \operatorname{Bl}_0 \mathbb{A}^3$ be the strict transform of $Q$ (Exercise 4 of Section 5.3 defines the blow-up of $\mathbb{A}^3$). Show that $\widetilde{Q}$ is nonsingular and that it meets the exceptional $\mathbb{P}^2$ in the conic $uw = v^2$.

### Lean

Not in Lean. Mathlib has `FixedPoints.subalgebra` for the invariant subalgebra and `MvPolynomial` for the polynomial rings, but no theorem that identifies $k[s, t]^{\pm 1}$ with $k[u, v, w]/(uw - v^2)$, and no quotient varieties.

### Notes and history

Quotients of $\mathbb{A}^2$ by finite subgroups of $\mathrm{SL}_2$ were studied by Klein in the 1880s, and their singularities are the Du Val singularities, also called rational double points or ADE singularities. The quadric cone is the simplest, $A_1$. Reid's Park City notes treat these singularities in detail. The literature state of the theorem above is theorem. The quadric cone is a running example of the handbook. P8 Ch. 10 classifies Du Val singularities, and P8 Ch. 12 treats $Q$ as the cone over a conic and $\frac1n(1,1)$ as the cone over a rational normal curve. The blow-up of Exercise 5 resolves $Q$, and its exceptional curve is a $(-2)$-curve. Volume 3 studies $Q$ as a toric variety, Volume 4 shows that it is canonical (the discrepancy of the exceptional curve is $0$), and Volume 11 studies its $F$-purity in characteristic $p$.
