---
title: Gorenstein rings
nodes: []
sources: [AM69, Mat86, Eis95]
reads_with: [Mat86:ch6, Eis95:ch21]
requires: [P1.1, P1.2, P1.5, P1.6, P1.9]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Gorenstein rings

### Statement

Throughout, $(A, \mathfrak{m}, k)$ is a Noetherian local ring of dimension $d$. The *socle* of an $A$-module $M$ is $\operatorname{Soc}(M) = \{ u \in M : \mathfrak{m}u = 0 \} \cong \operatorname{Hom}_A(k, M)$. It is a $k$-vector space, of finite dimension if $M$ is finitely generated.

**Definition P1.10.22 (type).** Let $A$ be Cohen-Macaulay. The *type* of $A$ is
$$
r(A) = \dim_k \operatorname{Ext}^d_A(k, A) .
$$

Lean: not in Mathlib. Mathlib has `CategoryTheory.Abelian.Ext` as a definition.

**Proposition P1.10.23 (type and socle).** Let $A$ be Cohen-Macaulay and $x_1, \dots, x_d$ a system of parameters. Then
$$
r(A) = \dim_k \operatorname{Soc}(A/(x_1, \dots, x_d)) .
$$
In particular the right side does not depend on the system of parameters, and $r(A) \geq 1$.

Lean: not in Mathlib.

*Proof.* By part (3) of the theorem on Cohen-Macaulay local rings in Section 10.2, $x_1, \dots, x_d$ is an $A$-sequence. Rees's theorem in Section 10.1 with $I = \mathfrak{m}$ gives $\operatorname{Ext}^d_A(k, A) \cong \operatorname{Hom}_A(k, A/(x_1, \dots, x_d))$, which is the socle. The ring $A/(x_1, \dots, x_d)$ is a nonzero Artinian local ring, so $\mathfrak{m}$ is an associated prime of it, and its socle is nonzero. $\square$

**Definition P1.10.24 (Gorenstein).** A Noetherian local ring $A$ is *Gorenstein* if it is Cohen-Macaulay of type $1$. A Noetherian ring is *Gorenstein* if its localization at every maximal ideal is Gorenstein.

Lean: not in Mathlib.

The definition is equivalent to others in the literature. A Noetherian local ring $A$ is Gorenstein if and only if $A$ has finite injective dimension as a module over itself, and then the injective dimension is $d$; the localizations of a Gorenstein local ring at primes are Gorenstein; and $A$ is Gorenstein if and only if $\operatorname{Ext}^i_A(k, A) = 0$ for $i \neq d$ and $\operatorname{Ext}^d_A(k, A) \cong k$. These facts are due to Bass and are proved in Matsumura, Chapter 6, and Eisenbud, Chapter 21. The handbook uses the definition through the type, which needs only Sections 10.1 and 10.2.

**Proposition P1.10.25 (Artinian Gorenstein rings).** Let $A$ be Artinian. Then every nonzero ideal of $A$ meets $\operatorname{Soc}(A)$ in a nonzero element, and the minimal nonzero ideals of $A$ are the lines in $\operatorname{Soc}(A)$. So $A$ is Gorenstein if and only if $A$ has a unique minimal nonzero ideal.

Lean: not in Mathlib.

*Proof.* Let $I \neq 0$ and $a \in I$ nonzero. The ideal $\mathfrak{m}$ is nilpotent, by Chapter 3, so there is a largest $j$ with $\mathfrak{m}^j a \neq 0$, and any nonzero $b \in \mathfrak{m}^j a \subseteq I$ satisfies $\mathfrak{m}b = 0$. So $I \cap \operatorname{Soc}(A) \neq 0$. Each subspace of $\operatorname{Soc}(A)$ is an ideal, since $\mathfrak{m}$ acts on it by zero. So a minimal nonzero ideal is a line in $\operatorname{Soc}(A)$, and every line in $\operatorname{Soc}(A)$ is a minimal nonzero ideal. There is a unique line if and only if $\dim_k \operatorname{Soc}(A) = 1$, which is $r(A) = 1$ since $d = 0$. $\square$

**Proposition P1.10.26 (type under quotients and completion).** Let $A$ be Cohen-Macaulay.

1. If $x \in \mathfrak{m}$ is a nonzerodivisor, then $A/xA$ is Cohen-Macaulay and $r(A/xA) = r(A)$.
2. $\hat{A}$ is Cohen-Macaulay and $r(\hat{A}) = r(A)$.

So $A$ is Gorenstein if and only if $A/xA$ is Gorenstein, if and only if $\hat{A}$ is Gorenstein.

Lean: not in Mathlib.

*Proof.* (1) By Section 10.2, $A/xA$ is Cohen-Macaulay and $x$ is part of a system of parameters $x, x_2, \dots, x_d$ of $A$. The images of $x_2, \dots, x_d$ form a system of parameters of $A/xA$, and both rings have the same Artinian quotient $A/(x, x_2, \dots, x_d)$. The proposition on type and socle gives $r(A/xA) = r(A)$.

(2) By Section 10.2, $\hat{A}$ is Cohen-Macaulay of dimension $d$. As in the proof of the proposition on depth and completion in Section 10.1, $\operatorname{Ext}^d_{\hat{A}}(k, \hat{A}) \cong \operatorname{Ext}^d_A(k, A) \otimes_A \hat{A} \cong \operatorname{Ext}^d_A(k, A)$. $\square$

**Corollary P1.10.27 (complete intersections are Gorenstein).** A regular local ring is Gorenstein. A complete intersection $R/(f_1, \dots, f_c)$, with $R$ regular local of dimension $n$ and $\dim R/(f_1, \dots, f_c) = n - c$, is Gorenstein. In particular every hypersurface $R/(f)$, $f \neq 0$, is Gorenstein.

Lean: not in Mathlib.

*Proof.* Let $R$ be regular with a regular system of parameters $y_1, \dots, y_n$. Then $R/(y_1, \dots, y_n) = k$ has socle $k$, so $r(R) = 1$. The elements $f_1, \dots, f_c$ form an $R$-sequence by Section 10.2, and part (1) of the proposition on type under quotients, applied $c$ times, gives $r(R/(f_1, \dots, f_c)) = r(R) = 1$. $\square$

### Proof in words

The type counts the independent elements killed by $\mathfrak{m}$ after cutting the ring down to dimension zero by parameters. Rees's theorem identifies this socle with an Ext module, so the count does not depend on the parameters, and it does not change under a further cut by a nonzerodivisor or under completion. A regular ring cuts down to the field $k$, which has a one dimensional socle, and a complete intersection cuts down to the same kind of ring. In an Artinian ring every ideal reaches down to the socle, so type $1$ means a unique smallest ideal.

### Examples

**Example P1.10.28 (Artinian rings).** The ring $k[x]/(x^n)$ has socle $k x^{n-1}$, so it is Gorenstein. The ring $k[x, y]/(x^2, y^2)$, with basis $1, x, y, xy$, has socle $k xy$, so it is Gorenstein, as the corollary also shows. The ring $k[x, y]/(x, y)^2$, with basis $1, x, y$, has socle $kx + ky$, so it has type $2$ and is not Gorenstein. Its two minimal ideals $(x)$ and $(y)$ are different.

**Example P1.10.29 (Gorenstein but not a complete intersection).** Let $A = k[x, y, z]/I$ with $I = (x^2 - y^2, y^2 - z^2, xy, yz, xz)$. In $A$ the products of two distinct variables vanish and $x^2 = y^2 = z^2$, so $x^3 = x \cdot z^2 = 0$, and $A$ has basis $1, x, y, z, x^2$. For $u = ax + by + cz$, $xu = ax^2$, $yu = bx^2$ and $zu = cx^2$, so $\operatorname{Soc}(A) = kx^2$ and $A$ is Gorenstein. The ideal $I$ has five linearly independent generators of degree $2$ and no generators of degree $1$, so it needs five generators, while a complete intersection of dimension $0$ in $k[x, y, z]$ is defined by three. Since the property of being a complete intersection does not depend on the presentation (Matsumura, Chapter 7), the local ring of $A$ is not a complete intersection. In codimension $2$ every Gorenstein ring is a complete intersection, by a theorem of Serre, and in codimension $3$ Buchsbaum and Eisenbud described the Gorenstein rings by Pfaffians (Eisenbud, Chapter 21).

**Example P1.10.30 (Veronese rings).** Let $A = k[s, t]^{(n)}$ be the ring spanned by the monomials of degree divisible by $n$, localized at the vertex, and $R = k[s^n, t^n]$. By Section 10.2, $A$ is Cohen-Macaulay and $s^n, t^n$ is a system of parameters. The quotient $A/(s^n, t^n)$ has basis $1$ and $s^at^{n-a}$ for $1 \leq a \leq n - 1$. A product $s^at^{n-a} \cdot s^ct^{n-c}$ has degree $2n$, and it is divisible in $A$ by $s^n$ if $a + c \geq n$ and by $t^n$ otherwise. So all the elements $s^at^{n-a}$ lie in the socle, and $r(A) = n - 1$. For $n = 2$ this is the quadric cone, which is Gorenstein. For $n = 3$ it is the twisted cubic cone, with socle spanned by $s^2t$ and $st^2$, and type $2$, so the cone over the twisted cubic is Cohen-Macaulay but not Gorenstein.

**Example P1.10.31 (Gorenstein singularities in the minimal model program).** For a normal Cohen-Macaulay variety $X$, the local ring at a point is Gorenstein if and only if the canonical divisor $K_X$ is Cartier near that point (Eisenbud, Chapter 21, and Volume 4). The du Val singularities $A_n$, $D_n$, $E_6$, $E_7$, $E_8$ are hypersurfaces in $\mathbb{A}^3$, so they are Gorenstein by the corollary. The cone over the twisted cubic is the quotient singularity of type $\frac{1}{3}(1, 1)$, and by the last example it is not Gorenstein, so its canonical divisor is not Cartier. It is $\mathbb{Q}$-Cartier, since $3K_X$ is Cartier, and it is a basic example of a klt singularity that is not canonical (Volume 4). It is the singularity obtained by contracting a smooth rational curve of self-intersection $-3$ on a smooth surface.

### Exercises

1. (A) Find the socle and the type of $k[x, y]/(x^2, xy, y^3)$.
2. (A) Show that $k[x, y]/(x^2, y^3)$ is Gorenstein and find its socle.
3. (A) Show that the type of $k[x_1, \dots, x_n]/(x_1, \dots, x_n)^2$ is $n$.
4. (B) Let $A$ be an Artinian local Gorenstein ring with socle $ku$. Show that the map $A \to \operatorname{Hom}_k(A, k)$ defined by $a \mapsto (b \mapsto \lambda(ab))$, where $\lambda$ is a linear form with $\lambda(u) \neq 0$, is injective, and hence an isomorphism. (Hint: use the proposition on Artinian Gorenstein rings.)
5. (B) Let $A = k[x, y]_{(x, y)}/(xy)$, the node. Show that $A$ is Gorenstein by two methods: as a hypersurface, and by computing the socle of $A/(x + y)$.
6. (B) Let $A = k[[t^3, t^4, t^5]]$. Show that $A$ is Cohen-Macaulay, that $t^3$ is a parameter, and that $A/t^3A$ has basis $1, t^4, t^5$ with socle spanned by $t^4$ and $t^5$. Deduce that $A$ is not Gorenstein. Compare with $k[[t^3, t^4]]$.
7. (B) Use the proposition on type under quotients to show that the Veronese ring of the example has type $n - 1$ also after completion, and decide for which $n$ the completion is a complete intersection.
8. (C) Let $A$ be Cohen-Macaulay and $x_1, \dots, x_d$ a system of parameters. Show that $A$ is Gorenstein if and only if the ideal $(x_1, \dots, x_d)$ is an irreducible ideal (Definition P1.2.39). Use this to show that $(x_1, \dots, x_d)$ is irreducible in a regular local ring.

### Lean

Mathlib has no definition of a Gorenstein ring and no notion of the type. It has the Ext groups, `CategoryTheory.Abelian.Ext`, and injective dimension, `CategoryTheory.injectiveDimension` with `CategoryTheory.HasInjectiveDimensionLT`, which are the ingredients of Bass's characterization. The propositions and examples of this section are not in Mathlib. The handbook adds no `MinimalModel` node here.

### Notes and history

Gorenstein met the condition in 1952 in his work on adjoint plane curves, and Kunz showed in 1970 that a monomial curve is Gorenstein if and only if its semigroup is symmetric. Grothendieck and Serre recognized the condition in duality theory, and Bass's paper of 1963, On the ubiquity of Gorenstein rings, gave the homological characterizations quoted here. Serre proved that Gorenstein rings of codimension $2$ are complete intersections, and Buchsbaum and Eisenbud described the codimension $3$ case in 1977. The literature state of every result here is theorem. The section follows Matsumura, Chapter 6, and Eisenbud, Chapter 21.
