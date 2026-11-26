---
title: Cohen-Macaulay rings
nodes: []
sources: [AM69, Mat86, Eis95]
reads_with: [Mat86:ch6, Eis95:ch18]
requires: [P1.1, P1.2, P1.5, P1.6, P1.9]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Cohen-Macaulay rings

### Statement

Throughout, $(A, \mathfrak{m}, k)$ is a Noetherian local ring of dimension $d$. By the proposition on depth and dimension in Section 10.1, $\operatorname{depth} A \leq d$.

**Definition P1.10.13 (Cohen-Macaulay).** A finitely generated $A$-module $M \neq 0$ is *Cohen-Macaulay* if $\operatorname{depth} M = \dim M$. The local ring $A$ is *Cohen-Macaulay* if it is a Cohen-Macaulay module over itself, that is, if $\operatorname{depth} A = \dim A$. A Noetherian ring is *Cohen-Macaulay* if its localization at every maximal ideal is Cohen-Macaulay.

Lean: not in Mathlib. Mathlib has the two numbers, `IsLocalRing.depth` and `ringKrullDim`, as definitions.

**Theorem P1.10.14 (Cohen-Macaulay local rings).** Let $x_1, \dots, x_r \in \mathfrak{m}$.

1. If $x_1, \dots, x_r$ is an $A$-sequence, then $\dim A/(x_1, \dots, x_r) = d - r$, so $x_1, \dots, x_r$ is part of a system of parameters.
2. If $A$ is Cohen-Macaulay, then $\dim A/\mathfrak{p} = d$ for every $\mathfrak{p} \in \operatorname{Ass}(A)$. In particular $A$ has no embedded primes.
3. If $A$ is Cohen-Macaulay and $x_1, \dots, x_r$ is part of a system of parameters, then $x_1, \dots, x_r$ is an $A$-sequence. So $A$ is Cohen-Macaulay if and only if one system of parameters, or every system of parameters, is an $A$-sequence.
4. If $x_1, \dots, x_r$ is an $A$-sequence, then $A$ is Cohen-Macaulay if and only if $A/(x_1, \dots, x_r)$ is Cohen-Macaulay.
5. $A$ is Cohen-Macaulay if and only if $\hat{A}$ is Cohen-Macaulay.

Lean: not in Mathlib.

*Proof.* (1) Each $x_{i}$ is a nonzerodivisor on $A/(x_1, \dots, x_{i-1})$, so Corollary P1.5.22 gives $\dim A/(x_1, \dots, x_i) = \dim A/(x_1, \dots, x_{i-1}) - 1$. By induction $\dim A/(x_1, \dots, x_r) = d - r$, and by the same corollary $x_1, \dots, x_r$ is part of a system of parameters.

(2) By Section 10.1, $d = \operatorname{depth} A \leq \dim A/\mathfrak{p} \leq d$ for $\mathfrak{p} \in \operatorname{Ass}(A)$. A prime $\mathfrak{p}$ with $\dim A/\mathfrak{p} = d$ is minimal, since a smaller prime would give a longer chain.

(3) Use induction on $r$, the case $r = 0$ being empty. Let $r \geq 1$. Since $x_1$ is part of a system of parameters, $\dim A/x_1A = d - 1$ by Corollary P1.5.22. If $x_1 \in \mathfrak{p}$ for some $\mathfrak{p} \in \operatorname{Ass}(A)$, then $\dim A/x_1A \geq \dim A/\mathfrak{p} = d$ by (2), a contradiction. So $x_1$ lies in no associated prime, and it is a nonzerodivisor by Proposition P1.2.44. The ring $A' = A/x_1A$ has dimension $d - 1$ and depth $d - 1$ by Section 10.1, so it is Cohen-Macaulay, and the images of $x_2, \dots, x_r$ are part of a system of parameters of $A'$. By induction they form an $A'$-sequence, so $x_1, \dots, x_r$ is an $A$-sequence. The last claim follows: if $A$ is Cohen-Macaulay, every system of parameters is an $A$-sequence, and if one system of parameters is an $A$-sequence, then $\operatorname{depth} A \geq d$.

(4) By (1) and Section 10.1, $\dim A/(x) = d - r$ and $\operatorname{depth} A/(x) = \operatorname{depth} A - r$, where $(x) = (x_1, \dots, x_r)$. So the two differences $\dim - \operatorname{depth}$ agree.

(5) By Theorem P1.6.18, $\dim \hat{A} = \dim A$, and by the proposition on depth and completion in Section 10.1, $\operatorname{depth} \hat{A} = \operatorname{depth} A$. $\square$

Two more facts are used in the handbook with a citation. If $A$ is Cohen-Macaulay, then $A_\mathfrak{p}$ is Cohen-Macaulay for every prime $\mathfrak{p}$, and $\operatorname{ht} I + \dim A/I = \dim A$ for every proper ideal $I$, so that $A$ and all its quotients are catenary (Matsumura, Chapter 6, and Eisenbud, Chapter 18). For a Noetherian ring the condition at maximal ideals in the definition is therefore the same as the condition at all primes.

**Corollary P1.10.15 (regular rings and complete intersections).** A regular local ring is Cohen-Macaulay. If $R$ is a regular local ring of dimension $n$ and $f_1, \dots, f_c \in \mathfrak{m}_R$ satisfy $\dim R/(f_1, \dots, f_c) = n - c$, then $A = R/(f_1, \dots, f_c)$ is Cohen-Macaulay. Such a ring is a *complete intersection*. In particular a hypersurface $R/(f)$ with $f \neq 0$ is Cohen-Macaulay.

Lean: not in Mathlib.

*Proof.* A regular system of parameters is an $A$-sequence by Proposition P1.9.4, so a regular local ring is Cohen-Macaulay by part (3) of the theorem. For the second claim, $f_1, \dots, f_c$ is part of a system of parameters of $R$ by Corollary P1.5.22, hence an $R$-sequence by part (3), and $A$ is Cohen-Macaulay by part (4). For a hypersurface, $f \neq 0$ is a nonzerodivisor since $R$ is a domain, so $\dim R/(f) = n - 1$. $\square$

**Theorem P1.10.16 (Cohen-Macaulay and free).** Let $(R, \mathfrak{n}) \to (A, \mathfrak{m})$ be a local homomorphism of Noetherian local rings such that $R$ is regular, $A$ is a finitely generated $R$-module, and $\dim A = \dim R$. Then $A$ is Cohen-Macaulay if and only if $A$ is a free $R$-module.

Lean: not in Mathlib. Mathlib has `Module.Free` as a definition.

*Proof.* The ring $A/\mathfrak{n}A$ is a finitely generated $R/\mathfrak{n}$-module, so it is Artinian, and $\mathfrak{n}A$ is $\mathfrak{m}$-primary. First, the depth of $A$ as an $A$-module is equal to the depth of $A$ as an $R$-module. Let $y_1, \dots, y_s \in \mathfrak{n}$ be a maximal $R$-sequence on the $R$-module $A$, and $\bar{A} = A/(y_1, \dots, y_s)A$. The images of the $y_i$ in $\mathfrak{m}$ form an $A$-sequence. By the lemma on homomorphisms in Section 10.1 over $R$, there is $a \in \bar{A}$, $a \neq 0$, with $\mathfrak{n}a = 0$. The $A$-submodule $Aa$ is killed by the $\mathfrak{m}$-primary ideal $\mathfrak{n}A$, so it has finite length, and it contains an element $b \neq 0$ with $\mathfrak{m}b = 0$. So $\mathfrak{m} \in \operatorname{Ass}_A(\bar{A})$, the $A$-sequence cannot be extended in $\mathfrak{m}$, and $\operatorname{depth}_A A = s = \operatorname{depth}_R A$.

By Section 9.3, $\operatorname{pd}_R A < \infty$, since $R$ is regular. The Auslander-Buchsbaum formula of Section 10.1 over $R$ gives
$$
\operatorname{pd}_R A = \dim R - \operatorname{depth}_R A = \dim A - \operatorname{depth}_A A .
$$
So $\operatorname{pd}_R A = 0$ if and only if $A$ is Cohen-Macaulay. A finitely generated module over a local ring has projective dimension $0$ if and only if it is free, by Theorem P1.1.50. $\square$

The theorem applies to graded rings. Let $A = \bigoplus_{i \geq 0} A_i$ be a finitely generated graded $k$-algebra with $A_0 = k$, let $\mathfrak{m} = \bigoplus_{i > 0} A_i$, and let $R = k[y_1, \dots, y_d] \subseteq A$ be a polynomial ring in homogeneous elements of positive degree over which $A$ is finite, with $d = \dim A$. Put $\mathfrak{n} = (y_1, \dots, y_d)$. The ring $A/\mathfrak{n}A$ is a finite dimensional graded $k$-algebra, so $\mathfrak{m}$ is its only prime, and $\mathfrak{m}$ is the only prime of $A$ over $\mathfrak{n}$. So $A \otimes_R R_\mathfrak{n} = A_\mathfrak{m}$ is local and finite over $R_\mathfrak{n}$, and the theorem says that $A_\mathfrak{m}$ is Cohen-Macaulay if and only if $A$ is a free $R$-module (for the second step, a finitely generated graded module over $R$ that is free after localization at $\mathfrak{n}$ is free, by the graded Nakayama lemma). In geometry: a finite surjective morphism from a variety with Cohen-Macaulay local rings to a smooth variety is flat, and the converse holds when the target is smooth (Matsumura, Chapter 8, and Eisenbud, Chapter 18).

### Proof in words

In a Cohen-Macaulay ring every system of parameters cuts down the ring as cleanly as possible: each parameter is a nonzerodivisor, so no component is lost and no component is cut more than once. The proof needs only that the depth bounds the dimension of each associated component: if the depth equals the dimension, all associated components have full dimension, a parameter avoids them all, and the property passes to the quotient. Over a regular subring of the same dimension, the formula of Auslander and Buchsbaum turns the missing depth into projective dimension, so Cohen-Macaulay is the same as free.

### Examples

**Example P1.10.17 (the twisted cubic cone).** Let $A = k[s^3, s^2t, st^2, t^3] \subseteq k[s, t]$, the cone over the twisted cubic curve, and $R = k[s^3, t^3]$. A monomial $s^at^b$ lies in $A$ if and only if $3$ divides $a + b$, and it is the product of a monomial in $R$ and one of $1, s^2t, st^2$, according to the residues of $a$ and $b$ modulo $3$. So $A$ is a free $R$-module with basis $1, s^2t, st^2$. By the theorem on Cohen-Macaulay and free, the local ring of $A$ at the vertex is Cohen-Macaulay, and so are all its local rings. The same argument works for every Veronese ring $k[s, t]^{(n)}$ spanned by the monomials of degree divisible by $n$, with basis the monomials $s^at^b$ with $a, b < n$ and $n \mid a + b$.

**Example P1.10.18 (the quadric cone).** The ring $A = k[x, y, z]/(xy - z^2)$ is a hypersurface, so it is Cohen-Macaulay. It is also the Veronese ring $k[s^2, st, t^2]$, free over $k[s^2, t^2]$ with basis $1, st$. Its singular point is the $A_1$ singularity of Volume 4.

**Example P1.10.19 (two planes meeting in a point).** Let $A = k[x, y, z, w]/((x, y) \cap (z, w))$ and $R = k[s, t]$ with $s = x + z$, $t = y + w$, as in Example P1.5.50. That example shows that $A$ is not flat over $R$, so the theorem on Cohen-Macaulay and free shows that the local ring of $A$ at the origin is not Cohen-Macaulay. This agrees with Section 10.1, where its depth is $1$ and its dimension is $2$. So the failure of flatness in Example P1.5.50 comes from the failure of the Cohen-Macaulay property, as promised in Chapter 5. Geometrically, the two planes are glued at a single point, and removing that point disconnects the spectrum. Exercise 7 shows directly that this forces depth at most $1$. By the connectedness theorem of Hartshorne, the punctured spectrum of a local ring of depth at least $2$ is always connected (Eisenbud, Chapter 18).

**Example P1.10.20 (a normal surface that is not Cohen-Macaulay).** Let $A = k[s^4, s^3t, st^3, t^4]$, the ring of Example P1.8.7, and $R = k[s^4, t^4]$. The elements $s^4, t^4$ form a system of parameters of the local ring at the vertex, since $A/(s^4, t^4)$ is finite dimensional. With $u = s^3t$, the element $t^4 u^2 = s^6t^6 = s^4 \cdot s^2t^6$ lies in $s^4A$, since $s^2t^6 = (st^3)^2$, while $u^2 = s^6t^2 = s^4 \cdot s^2t^2$ does not, since $s^2t^2 \notin A$. So $t^4$ is a zero divisor on $A/s^4A$, and part (3) of the theorem shows that $A$ is not Cohen-Macaulay at the vertex. This ring is not normal (Example P1.8.7), and its normalization $k[s, t]^{(4)}$ is Cohen-Macaulay by the example of the twisted cubic cone. Chapter 11 shows that every normal surface is Cohen-Macaulay.

**Example P1.10.21 (curves).** Let $A$ be a local ring of dimension $1$. Then $A$ is Cohen-Macaulay if and only if $\mathfrak{m} \notin \operatorname{Ass}(A)$. A reduced local ring of dimension $1$ is Cohen-Macaulay: its associated primes are its minimal primes, by Exercise 3. So the local rings of reduced curves, such as the node and the cusp, are Cohen-Macaulay, while the line with an embedded point of Example P1.2.36 is not.

### Exercises

1. (A) Show that a Noetherian local ring of dimension $0$ is Cohen-Macaulay, and that a Noetherian local domain of dimension $1$ is Cohen-Macaulay.
2. (A) Show that $k[x, y]_{(x, y)}/(x^2, xy)$ is not Cohen-Macaulay by finding a system of parameters that is not a regular sequence.
3. (A) Let $A$ be a reduced Noetherian ring. Show that every associated prime of $A$ is minimal. (Hint: if $\mathfrak{p} = \operatorname{Ann}(a)$ with $a \neq 0$, choose a minimal prime $\mathfrak{q}$ with $a \notin \mathfrak{q}$ and show that $\mathfrak{p} \subseteq \mathfrak{q}$.)
4. (B) Let $A = k[x, y, z]_{(x, y, z)}/(xy, xz)$, the union of a plane and a line. Find the dimension and the depth of $A$, and decide whether $A$ is Cohen-Macaulay.
5. (B) Let $A$ be Cohen-Macaulay, let $x_1, \dots, x_d$ be a system of parameters and $\mathfrak{q} = (x_1, \dots, x_d)$. Let $e(\mathfrak{q})$ be $d!$ times the leading coefficient of the Hilbert-Samuel polynomial of $\mathfrak{q}$ (Section 5.3). Show that $e(\mathfrak{q}) = \ell(A/\mathfrak{q})$, and check this for $A = k[[x]]$ and $\mathfrak{q} = (x^2)$. (Hint: use the fact that $\bigoplus_n \mathfrak{q}^n/\mathfrak{q}^{n+1}$ is a polynomial ring in $d$ variables over $A/\mathfrak{q}$ when $\mathfrak{q}$ is generated by a regular sequence, Matsumura, Chapter 6.)
6. (B) Show that the $n$-th Veronese ring $k[s, t]^{(n)}$ is a free $k[s^n, t^n]$-module of rank $n$, and list a basis.
7. (C) Let $A$ be a reduced Noetherian local ring of dimension $2$ with exactly two minimal primes $\mathfrak{p}$ and $\mathfrak{q}$, such that $\dim A/\mathfrak{p} \geq 1$, $\dim A/\mathfrak{q} \geq 1$ and $\mathfrak{p} + \mathfrak{q}$ is $\mathfrak{m}$-primary. Use the exact sequence $0 \to A \to A/\mathfrak{p} \times A/\mathfrak{q} \to A/(\mathfrak{p} + \mathfrak{q}) \to 0$ to show that $\operatorname{Ext}^1_A(k, A) \neq 0$, and deduce that $A$ is not Cohen-Macaulay. Apply this to the two planes of Example P1.5.50 and to Exercise 4.
8. (C) Let $A = k[x_1, \dots, x_n]$ and $I$ an ideal generated by $c$ elements with $\dim A/I = n - c$. Show that $A/I$ is Cohen-Macaulay at every maximal ideal. Apply this to the twisted cubic in $\mathbb{A}^3$ and explain why it does not show that the cone over the twisted cubic is Cohen-Macaulay. (The ideal of the twisted cubic cone in $k[x_0, \dots, x_3]$ needs three generators while its height is two.)

### Lean

Mathlib has depth, `IsLocalRing.depth`, and Krull dimension, `ringKrullDim`, but no definition of a Cohen-Macaulay ring or module. The theorem on Cohen-Macaulay local rings, the corollary on complete intersections and the theorem on Cohen-Macaulay and free modules are not in Mathlib. The freeness in the last theorem would be stated with `Module.Free`. The handbook adds no `MinimalModel` node here.

### Notes and history

Macaulay proved in 1916 that an ideal of a polynomial ring generated by as many elements as its height is unmixed, and Cohen proved the analogous statement for regular local rings in 1946. The name Cohen-Macaulay ring comes from this, and Nagata and Serre made the class central in the 1950s. The characterization by freeness over a regular subring is classical and is sometimes called the miracle flatness theorem. Hartshorne proved his connectedness theorem in 1962. The literature state of every result here is theorem. The section follows Matsumura, Chapter 6, and Eisenbud, Chapter 18.
