---
title: Dimension of finitely generated algebras and of fibres
nodes: []
sources: [AM69, Mat86, Eis95]
reads_with: [AM69:ch11, Mat86:ch5, Eis95:ch10, Eis95:ch13]
requires: [P1.1, P1.2, P1.4]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Dimension of finitely generated algebras and of fibres

### Statement

Throughout, $k$ is a field. A chain of primes $\mathfrak{p}_0 \subsetneq \dots \subsetneq \mathfrak{p}_r$ is *saturated* if no prime lies strictly between two neighbours. A saturated chain in a domain that starts at $0$ and ends at a maximal ideal is called *maximal*.

**Lemma P1.5.40 (height one primes of an affine domain).** Let $A$ be a finitely generated $k$-algebra that is a domain, with $\dim A = d$, and let $\mathfrak{p}$ be a prime of height $1$. Then $\dim A/\mathfrak{p} = d - 1$.

Lean: not in Lean.

*Proof.* By Noether normalization (Theorem P1.4.27) there is a polynomial ring $R = k[y_1, \dots, y_d] \subseteq A$ with $A$ finite over $R$, and $d = \dim A$ by Theorem P1.4.31. Let $\mathfrak{q} = \mathfrak{p} \cap R$. A chain of primes below $\mathfrak{p}$ contracts to a chain below $\mathfrak{q}$, and the inclusions stay strict by incomparability (Theorem P1.4.11). So $\operatorname{ht} \mathfrak{q} \geq 1$. The ring $R$ is factorial, hence normal (Proposition P1.4.19), so going down (Theorem P1.4.22) lifts a chain below $\mathfrak{q}$ to a chain below $\mathfrak{p}$, and $\operatorname{ht} \mathfrak{q} \leq 1$. So $\operatorname{ht} \mathfrak{q} = 1$. Take $0 \neq g \in \mathfrak{q}$. Since $\mathfrak{q}$ is prime, it contains an irreducible factor $f$ of $g$, and $(f)$ is a nonzero prime in the factorial ring $R$. Since $0 \subsetneq (f) \subseteq \mathfrak{q}$ and $\operatorname{ht} \mathfrak{q} = 1$, $\mathfrak{q} = (f)$.

Next, $\dim R/(f) = d - 1$. After a renumbering, $f$ has positive degree in $y_d$. If $h \in k[y_1, \dots, y_{d-1}]$ lies in $(f)$, then $f$ divides $h$, which has degree $0$ in $y_d$, so $h = 0$. So the images of $y_1, \dots, y_{d-1}$ in $R/(f)$ are algebraically independent. The image of $y_d$ is algebraic over them, since $f(y_1, \dots, y_d) = 0$ is a nonzero polynomial relation in $y_d$. So the fraction field of $R/(f)$ has transcendence degree $d - 1$, and $\dim R/(f) = d - 1$ by Theorem P1.4.31. Finally $A/\mathfrak{p}$ is integral over $R/\mathfrak{q} \subseteq A/\mathfrak{p}$, so $\dim A/\mathfrak{p} = \dim R/\mathfrak{q} = d - 1$ by Corollary P1.4.14. $\square$

**Theorem P1.5.41 (chains in an affine domain).** Let $A$ be a finitely generated $k$-algebra that is a domain, with $\dim A = d$. Then every maximal chain of primes of $A$ has length $d$.

Lean: not in Lean.

*Proof.* Induction on $d$. If $d = 0$, then $A$ is a field and the only chain is $0$. Let $d \geq 1$ and let $0 = \mathfrak{p}_0 \subsetneq \mathfrak{p}_1 \subsetneq \dots \subsetneq \mathfrak{p}_r$ be a maximal chain. Since $0$ is not maximal, $r \geq 1$. Since the chain is saturated, no prime lies strictly between $0$ and $\mathfrak{p}_1$, so $\operatorname{ht} \mathfrak{p}_1 = 1$, and $\dim A/\mathfrak{p}_1 = d - 1$ by the lemma. The primes $\mathfrak{p}_i/\mathfrak{p}_1$ form a maximal chain of length $r - 1$ in the finitely generated domain $A/\mathfrak{p}_1$. By induction $r - 1 = d - 1$. $\square$

**Corollary P1.5.42 (the dimension formula).** Let $A$ be a finitely generated $k$-algebra that is a domain.

1. For every prime $\mathfrak{p}$, $\operatorname{ht} \mathfrak{p} + \dim A/\mathfrak{p} = \dim A$.
2. For every maximal ideal $\mathfrak{m}$, $\dim A_{\mathfrak{m}} = \dim A$.
3. For primes $\mathfrak{p} \subseteq \mathfrak{q}$, every saturated chain from $\mathfrak{p}$ to $\mathfrak{q}$ has length $\operatorname{ht} \mathfrak{q} - \operatorname{ht} \mathfrak{p}$.

Every finitely generated $k$-algebra is catenary.

Lean: not in Lean; Mathlib has no notion of a catenary ring.

*Proof.* (1) Let $d = \dim A$. A chain of greatest length below $\mathfrak{p}$ has length $\operatorname{ht} \mathfrak{p} \leq d$ and is saturated, and a chain of greatest length above $\mathfrak{p}$ has length $\dim A/\mathfrak{p}$, is saturated and ends at a maximal ideal. Together they form a maximal chain, of length $d$ by the theorem.

(2) By (1) and Proposition P1.2.6, $\dim A_{\mathfrak{m}} = \operatorname{ht} \mathfrak{m} = d - \dim A/\mathfrak{m} = d$.

(3) Every saturated chain from $0$ to $\mathfrak{p}$, followed by a saturated chain from $\mathfrak{p}$ to a maximal ideal, is a maximal chain. By the theorem applied to $A/\mathfrak{p}$, the second part has length $\dim A/\mathfrak{p}$. So the first part has length $d - \dim A/\mathfrak{p} = \operatorname{ht} \mathfrak{p}$. In the same way, a saturated chain from $\mathfrak{p}$ to $\mathfrak{q}$, put between a saturated chain from $0$ to $\mathfrak{p}$ and one from $\mathfrak{q}$ to a maximal ideal, gives a maximal chain. So its length is $d - \operatorname{ht} \mathfrak{p} - \dim A/\mathfrak{q} = \operatorname{ht} \mathfrak{q} - \operatorname{ht} \mathfrak{p}$.

For an arbitrary finitely generated $k$-algebra $B$ and primes $\mathfrak{p} \subseteq \mathfrak{q}$, the primes between them are the primes of the domain $B/\mathfrak{p}$ between $0$ and $\mathfrak{q}/\mathfrak{p}$. By (3) for $B/\mathfrak{p}$, all saturated chains between them have the same length. $\square$

**Corollary P1.5.43 (sections by hypersurfaces).** Let $A$ be a finitely generated $k$-algebra that is a domain of dimension $d$, and let $f_1, \dots, f_r \in A$. Every minimal prime $\mathfrak{p}$ over $(f_1, \dots, f_r)$ has $\dim A/\mathfrak{p} \geq d - r$. If $r = 1$ and $f_1$ is a nonzero nonunit, then $\dim A/\mathfrak{p} = d - 1$ for every minimal prime over $(f_1)$.

Lean: Mathlib `Ideal.height_le_card_of_mem_minimalPrimes_span_finset` (the height bound, proved in Mathlib).

*Proof.* By Krull's height theorem (Section 5.2), $\operatorname{ht} \mathfrak{p} \leq r$, so $\dim A/\mathfrak{p} = d - \operatorname{ht} \mathfrak{p} \geq d - r$ by the dimension formula. If $r = 1$ and $f_1 \neq 0$, then $\mathfrak{p} \neq 0$, so $\operatorname{ht} \mathfrak{p} = 1$. $\square$

In geometric terms: every irreducible component of $X \cap V(f_1, \dots, f_r)$, for an affine variety $X$ of dimension $d$, has dimension at least $d - r$, and every component of a hypersurface section $X \cap V(f)$ that is not empty and not all of $X$ has dimension exactly $d - 1$.

**Lemma P1.5.44 (going down for flat maps).** Let $\varphi: A \to B$ be a flat ring homomorphism, $\mathfrak{Q}$ a prime of $B$, $\mathfrak{p} = \varphi^{-1}(\mathfrak{Q})$, and $\mathfrak{p}' \subseteq \mathfrak{p}$ a prime of $A$. Then there is a prime $\mathfrak{Q}' \subseteq \mathfrak{Q}$ of $B$ with $\varphi^{-1}(\mathfrak{Q}') = \mathfrak{p}'$.

Lean: Mathlib `Algebra.HasGoingDown.of_flat` (instance, proved in Mathlib).

*Proof.* The map $A_{\mathfrak{p}} \to B_{\mathfrak{Q}}$ is flat, as the composite of $A_{\mathfrak{p}} \to B_{\mathfrak{p}} = B \otimes_A A_{\mathfrak{p}}$, flat by base change, and the localization $B_{\mathfrak{p}} \to B_{\mathfrak{Q}}$. It is local, so $\mathfrak{p} B_{\mathfrak{Q}} \subseteq \mathfrak{Q} B_{\mathfrak{Q}} \neq B_{\mathfrak{Q}}$, and it is faithfully flat by Proposition P1.1.53. Let $C = A_{\mathfrak{p}'}$, a localization of $A_{\mathfrak{p}}$. Then $C \to B_{\mathfrak{Q}} \otimes_{A_{\mathfrak{p}}} C$ is faithfully flat, since for a $C$-module $M$, $M \otimes_C (B_{\mathfrak{Q}} \otimes_{A_{\mathfrak{p}}} C) = M \otimes_{A_{\mathfrak{p}}} B_{\mathfrak{Q}}$, which is not zero if $M \neq 0$. By Proposition P1.1.53, the maximal ideal $\mathfrak{p}' C$ is the contraction of a prime of $B_{\mathfrak{Q}} \otimes_{A_{\mathfrak{p}}} C$, which is a localization of $B_{\mathfrak{Q}}$. So there is a prime of $B_{\mathfrak{Q}}$ that contracts to $\mathfrak{p}' A_{\mathfrak{p}}$, and it has the form $\mathfrak{Q}' B_{\mathfrak{Q}}$ with $\mathfrak{Q}' \subseteq \mathfrak{Q}$ (Proposition P1.2.6). Then $\varphi^{-1}(\mathfrak{Q}') = \mathfrak{p}'$. $\square$

**Theorem P1.5.45 (dimension of fibres).** Let $\varphi: (A, \mathfrak{m}) \to (B, \mathfrak{n})$ be a local homomorphism of Noetherian local rings. Then
$$
\dim B \leq \dim A + \dim B/\mathfrak{m}B ,
$$
with equality if $B$ is flat over $A$.

Lean: Mathlib `Ideal.height_le_height_add_of_liesOver` and `Ideal.height_eq_height_add_of_liesOver_of_hasGoingDown` (the same statement for heights of primes, the equality under going down, proved in Mathlib).

*Proof.* Let $a = \dim A$ and $b = \dim B/\mathfrak{m}B$. Choose a system of parameters $x_1, \dots, x_a$ of $A$, so that $\mathfrak{m}^s \subseteq (x_1, \dots, x_a)$ for some $s$, and choose $y_1, \dots, y_b \in \mathfrak{n}$ whose images form a system of parameters of $B/\mathfrak{m}B$, so that $\mathfrak{n}^t \subseteq \mathfrak{m}B + (y_1, \dots, y_b)$ for some $t$. Then
$$
\mathfrak{n}^{st} \subseteq (\mathfrak{m}B + (y_1, \dots, y_b))^s \subseteq \mathfrak{m}^s B + (y_1, \dots, y_b) \subseteq (\varphi(x_1), \dots, \varphi(x_a), y_1, \dots, y_b),
$$
so these $a + b$ elements generate an $\mathfrak{n}$-primary ideal, and $\dim B \leq a + b$ by Krull's height theorem (Section 5.2).

Let $B$ be flat over $A$. Induction on $a$. If $a = 0$, then $A$ is Artinian and $\mathfrak{m}^s = 0$ for some $s$ (Theorem P1.3.35). So $\mathfrak{m}B$ is nilpotent, every prime of $B$ contains it, and $\dim B = \dim B/\mathfrak{m}B$. Let $a > 0$. Let $N$ be the nilradical of $A$. It is nilpotent, since $A$ is Noetherian, so $NB$ is nilpotent, and $A/N \to B/NB$ is flat by base change, with the same fibre and the same dimensions. So $A$ may be assumed reduced. Then the associated primes of $A$ are its minimal primes (Theorem P1.2.47, since $0$ is an intersection of primes), and $\mathfrak{m}$ is not minimal because $a > 0$. By prime avoidance (Lemma P1.1.11) there is $x \in \mathfrak{m}$ in no minimal prime, so $x$ is a nonzerodivisor on $A$ (Proposition P1.2.44). Tensoring the injection $A \xrightarrow{x} A$ with $B$ shows that $\varphi(x)$ is a nonzerodivisor on $B$, so it lies in no minimal prime of $B$ (Theorem P1.2.48). By Section 5.2, an element of the maximal ideal outside every minimal prime lowers the dimension by exactly one, so
$$
\dim A/xA = a - 1, \qquad \dim B/xB = \dim B - 1 .
$$
The map $A/xA \to B/xB$ is flat and local, and its fibre $B/(\mathfrak{m}B + xB) = B/\mathfrak{m}B$ is unchanged. By induction $\dim B - 1 = (a - 1) + b$. $\square$

**Corollary P1.5.46 (polynomial rings).** Let $A$ be a Noetherian ring. Then $\dim A[x] = \dim A + 1$, and $\dim A[x_1, \dots, x_n] = \dim A + n$.

Lean: Mathlib `Polynomial.ringKrullDim_of_isNoetherianRing` and `MvPolynomial.ringKrullDim_of_isNoetherianRing` (proved in Mathlib).

*Proof.* For a prime $\mathfrak{p}$ of $A$, $\mathfrak{p}[x] = \mathfrak{p}A[x]$ is prime, since $A[x]/\mathfrak{p}[x] = (A/\mathfrak{p})[x]$ is a domain, and $\mathfrak{p}[x] \subsetneq \mathfrak{p}[x] + (x)$, which is prime with quotient $A/\mathfrak{p}$. So a chain $\mathfrak{p}_0 \subsetneq \dots \subsetneq \mathfrak{p}_d$ in $A$ gives the chain $\mathfrak{p}_0[x] \subsetneq \dots \subsetneq \mathfrak{p}_d[x] \subsetneq \mathfrak{p}_d[x] + (x)$ of length $d + 1$, and $\dim A[x] \geq \dim A + 1$.

Conversely, let $\mathfrak{P}$ be a prime of $A[x]$ and $\mathfrak{p} = \mathfrak{P} \cap A$. The map $A_{\mathfrak{p}} \to A[x]_{\mathfrak{P}}$ is a flat local homomorphism of Noetherian local rings, since $A[x]$ is free over $A$. Its fibre $A[x]_{\mathfrak{P}}/\mathfrak{p}A[x]_{\mathfrak{P}}$ is a localization of $\kappa(\mathfrak{p})[x]$, which has dimension at most $1$. By the theorem, $\operatorname{ht} \mathfrak{P} \leq \operatorname{ht} \mathfrak{p} + 1 \leq \dim A + 1$. The second statement follows by induction. $\square$

**Remark P1.5.47 (without the Noetherian hypothesis).** For an arbitrary ring of finite dimension, Seidenberg proved $\dim A + 1 \leq \dim A[x] \leq 2 \dim A + 1$, and every value between the bounds occurs. The upper bound comes from the same fibre argument: over a prime $\mathfrak{p}$ of $A$, at most two primes of a chain in $A[x]$ lie over $\mathfrak{p}$, since $\kappa(\mathfrak{p})[x]$ has dimension $1$.

### Proof in words

A finitely generated domain over a field looks the same from every point: every maximal chain of irreducible closed subsets has the same length. The reason is Noether normalization. It makes $A$ finite over a polynomial ring, where an irreducible hypersurface is cut out by one irreducible polynomial and so has dimension one less. Going up, going down and incomparability carry this from the polynomial ring to $A$. Induction then shows that every saturated chain is as long as possible. So codimension and dimension add up, a point has a local ring of the full dimension, and a hypersurface section drops the dimension by exactly one.

For a morphism, the dimension at a point upstairs is at most the dimension of the base plus the dimension of the fibre: equations of the base point, pulled back, together with equations of the point in its fibre, cut out the point upstairs. For a flat morphism there is equality, since a nonzerodivisor of the base stays a nonzerodivisor upstairs and lowers both dimensions by one. This is the algebra behind the statement that the fibres of a flat family all have the same dimension.

The minimal model program uses these results all the time. A prime divisor on a normal variety $X$ is a subvariety of codimension one, and the dimension formula says that this is the same as a height one prime in every affine chart, so that the local ring at its generic point has dimension one (Chapter 7 and Chapter 8). A contraction $X \to Y$ is divisorial or small according to the dimension of its exceptional locus, which is measured by the fibre dimension. The families of stable varieties in Volume 13 are flat, and their fibres are equidimensional by the theorem on fibres.

### Examples

**Example P1.5.48 (a flat family of conics).** Let $A = k[t]$ and $B = k[x, y, t]/(xy - t) \cong k[x, y]$, which is flat over $A$ by Example P1.1.54. At the origin, $A_{(t)}$ has dimension $1$, the fibre $k[x, y]_{(x, y)}/(xy)$ is the local ring of the node, of dimension $1$, and $B_{(x, y)}$ has dimension $2 = 1 + 1$. This is the equality of the theorem.

**Example P1.5.49 (the blow-up chart).** Let $A = k[x, y]_{(x, y)}$ and let $B$ be the localization of $k[x, u]$ at $(x, u)$, with $y \mapsto xu$, a chart of the blow-up of the origin at a point of the exceptional curve. The fibre is $B/(x, xu)B = B/xB$, the local ring of the line $x = 0$, of dimension $1$. So $\dim B = 2 < 2 + 1$. The inequality is strict, so $B$ is not flat over $A$, which is Example P1.1.56 again. Geometrically, a whole curve, the exceptional curve, lies over one point of the plane, and a flat map from a surface to a surface can not have a curve as a fibre.

**Example P1.5.50 (two planes meeting in a point).** Let $A = k[x, y, z, w]/((x, y) \cap (z, w))$, the union of the planes $z = w = 0$ and $x = y = 0$ in $\mathbb{A}^4$, which meet only at the origin. Here $(x, y) \cap (z, w) = (xz, xw, yz, yw)$. Let $R = k[s, t] \subseteq A$ with $s = x + z$ and $t = y + w$. Each plane maps isomorphically onto the $(s, t)$-plane, so $A$ is finite over $R$, and $A \otimes_R \operatorname{Frac}(R)$ has dimension $2$ over $\operatorname{Frac}(R)$. The fibre over the origin is $A/(s, t)A \cong k[x, y]/(x^2, xy, y^2)$, after the substitution $z = -x$, $w = -y$, and it has dimension $3$. If $A$ were flat over $R$, then the finite module $A \otimes_R R_{(s,t)}$ would be free over the local ring $R_{(s,t)}$ by Theorem P1.1.50, and both numbers would be its rank. So $A$ is not flat over $R$. All the same, $\dim A_{\mathfrak{n}} = 2 = 2 + 0$ at the origin $\mathfrak{n}$, so equality in the theorem does not imply flatness. Chapter 10 shows that $A$ is not Cohen-Macaulay, and this is the reason for the failure.

### Exercises

1. (A) Let $A = k[x, y, z, w]/(xw - yz)$ and $\mathfrak{p} = (x, y)A$. Show that $\dim A = 3$, $\operatorname{ht} \mathfrak{p} = 1$ and $\dim A/\mathfrak{p} = 2$.
2. (A) Let $A = k[x, y, z]/(xz, yz)$, the plane $z = 0$ and the line $x = y = 0$ of Example P1.3.23. Compute $\dim A_{\mathfrak{m}}$ for the maximal ideals $\mathfrak{m}$ of the points of the plane, of the line, and of the origin. Show that $\operatorname{ht} \mathfrak{p} + \dim A/\mathfrak{p} = \dim A$ fails for the prime $\mathfrak{p} = (x, y)$ of the line.
3. (A) Show that every maximal ideal of $\mathbb{Z}[x]$ has height $2$ and that $\dim \mathbb{Z}[x] = 2$. (Hint: if a maximal ideal $\mathfrak{M}$ has $\mathfrak{M} \cap \mathbb{Z} = 0$, then $\mathbb{Q} \subseteq \mathbb{Z}[x]/\mathfrak{M} = \mathbb{Z}[\alpha]$ with $\alpha$ algebraic over $\mathbb{Q}$; find $N$ with $\alpha$ integral over $\mathbb{Z}[1/N]$ and deduce that $\mathbb{Z}[1/N]$ is a field. So $\mathfrak{M}$ contains a prime number $p$, and $\mathfrak{M}/(p)$ is maximal in $\mathbb{F}_p[x]$.) Compare with the ring $R[t]$ of Section 5.1, with $R$ a discrete valuation ring, which has a maximal ideal of height $1$.
4. (B) Let $\varphi: (A, \mathfrak{m}) \to (B, \mathfrak{n})$ be a local homomorphism of Noetherian local rings with $B$ a finite $A$-module. Show that $\dim B \leq \dim A$, with equality if $B$ is flat over $A$.
5. (B) Let $k$ be algebraically closed and let $X, Y \subseteq \mathbb{A}^n$ be affine varieties. Show that every irreducible component of $X \cap Y$ has dimension at least $\dim X + \dim Y - n$. (Hint: $X \cap Y$ is isomorphic to $(X \times Y) \cap \Delta$, where the diagonal $\Delta$ is cut out by $n$ equations, and $k[X] \otimes_k k[Y]$ is a domain with transcendence degree $\dim X + \dim Y$.)
6. (B) Let $A \subseteq B$ be finitely generated $k$-algebras that are domains, $\mathfrak{Q}$ a prime of $B$ and $\mathfrak{p} = \mathfrak{Q} \cap A$. Show the dimension formula $\operatorname{ht} \mathfrak{Q} + \operatorname{trdeg}_{\kappa(\mathfrak{p})} \kappa(\mathfrak{Q}) = \operatorname{ht} \mathfrak{p} + \operatorname{trdeg}_A B$, where $\operatorname{trdeg}_A B$ is the transcendence degree of $\operatorname{Frac}(B)$ over $\operatorname{Frac}(A)$.
7. (B) Let $A$ be a Noetherian ring and $\mathfrak{p}$ a prime. Show that $\operatorname{ht} \mathfrak{p}A[x] = \operatorname{ht} \mathfrak{p}$ and $\operatorname{ht}(\mathfrak{p}A[x] + xA[x]) = \operatorname{ht} \mathfrak{p} + 1$.
8. (C) Let $A$ be a Noetherian ring. Show that $\dim A[[x]] = \dim A + 1$. (Hint: $x$ lies in the Jacobson radical of $A[[x]]$, so every maximal ideal has the form $\mathfrak{n} + (x)$ with $\mathfrak{n}$ maximal in $A$. Use the theorem on fibres for $A_{\mathfrak{n}} \to A[[x]]_{\mathfrak{n} + (x)}$, which is flat by Chapter 6, and the fibre $(A/\mathfrak{n})[[x]]$.)

### Lean

Mathlib proves the fibre inequality for heights as `Ideal.height_le_height_add_of_liesOver` and the equality under going down as `Ideal.height_eq_height_add_of_liesOver_of_hasGoingDown`, in the file of Krull's height theorem. Going down for flat algebras is the instance `Algebra.HasGoingDown.of_flat`. With these it proves $\dim A[x] = \dim A + 1$ for Noetherian $A$ as `Polynomial.ringKrullDim_of_isNoetherianRing`, and the version with $n$ variables as `MvPolynomial.ringKrullDim_of_isNoetherianRing`. The dimension formula for affine domains and the notion of a catenary ring are not in Mathlib. The handbook adds no `MinimalModel` node here.

### Notes and history

The equality of the lengths of all maximal chains in an affine domain is classical, and the proof here, through Noether normalization, is the one in Eisenbud, Chapter 13. The fibre theorem is in Matsumura, Chapter 5, and the two-planes example is the standard example of a ring that is not Cohen-Macaulay. Seidenberg proved his bounds for $\dim A[x]$ in 1953. Cohen-Macaulay rings and their quotients are catenary (Matsumura, Chapter 6), and the examples of Nagata in Section 5.1 show that a Noetherian domain need not be catenary. The literature state of every result here is theorem. The section follows Atiyah-Macdonald, Chapter 11, Matsumura, Chapter 5, and Eisenbud, Chapters 10 and 13.
