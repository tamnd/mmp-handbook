---
title: Serre's conditions and extension of functions
nodes: []
sources: [AM69, Mat86, Eis95]
reads_with: [Mat86:ch8, Eis95:ch11, Eis95:ch18]
requires: [P1.1, P1.2, P1.5, P1.8, P1.9, P1.10]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Serre's conditions and extension of functions

### Statement

Throughout, $A$ is a Noetherian ring. For a prime $\mathfrak{p}$, $\operatorname{depth} A_\mathfrak{p}$ is the depth of the local ring $A_\mathfrak{p}$ as in Section 10.1, and $\dim A_\mathfrak{p} = \operatorname{ht} \mathfrak{p}$.

**Definition P1.11.1 (Serre's conditions).** Let $k \geq 0$ be an integer.

1. $A$ satisfies $R_k$ if $A_\mathfrak{p}$ is a regular local ring for every prime $\mathfrak{p}$ with $\operatorname{ht} \mathfrak{p} \leq k$.
2. $A$ satisfies $S_k$ if $\operatorname{depth} A_\mathfrak{p} \geq \min(k, \operatorname{ht} \mathfrak{p})$ for every prime $\mathfrak{p}$.

Lean: not in Mathlib.

The condition $R_0$ says that $A_\mathfrak{p}$ is a field for each minimal prime $\mathfrak{p}$, and $S_0$ always holds. For a variety, $R_k$ says that the singular locus has codimension greater than $k$. By Section 10.2, $A$ is Cohen-Macaulay if and only if it satisfies $S_k$ for all $k$, since a Cohen-Macaulay local ring has Cohen-Macaulay localizations. In particular regular rings, complete intersections and hypersurfaces satisfy every $S_k$. For a local ring of dimension $d$, the condition $S_d$ at the maximal ideal says that the ring is Cohen-Macaulay.

**Lemma P1.11.2 (associated primes and localization).** Let $M$ be a finitely generated $A$-module and $\mathfrak{p}$ a prime. Then $\mathfrak{p} \in \operatorname{Ass}_A(M)$ if and only if $\mathfrak{p}A_\mathfrak{p} \in \operatorname{Ass}_{A_\mathfrak{p}}(M_\mathfrak{p})$, that is, if and only if $M_\mathfrak{p} \neq 0$ and $\operatorname{depth} M_\mathfrak{p} = 0$.

Lean: not in Mathlib in this form.

*Proof.* If $A/\mathfrak{p} \to M$ is injective, then so is $A_\mathfrak{p}/\mathfrak{p}A_\mathfrak{p} \to M_\mathfrak{p}$, by exactness of localization (Theorem P1.2.5). Conversely, let $u = m/s \in M_\mathfrak{p}$ have annihilator $\mathfrak{p}A_\mathfrak{p}$. Then $m/1$ has the same annihilator. Write $\mathfrak{p} = (a_1, \dots, a_r)$. Since $a_i m/1 = 0$, there are $t_i \notin \mathfrak{p}$ with $t_i a_i m = 0$. Put $t = t_1 \cdots t_r$. Then $\mathfrak{p} \subseteq \operatorname{Ann}(tm)$. If $c \in \operatorname{Ann}(tm)$, then $c \cdot (m/1) = 0$ in $M_\mathfrak{p}$, since $t$ is a unit there, so $c \in \mathfrak{p}A_\mathfrak{p} \cap A = \mathfrak{p}$. Hence $\mathfrak{p} = \operatorname{Ann}(tm)$. The last statement is the remark after the definition of depth in Section 10.1. $\square$

So $S_1$ says that $\operatorname{Ass}(A)$ contains only primes of height $0$, that is, $A$ has no embedded primes. The condition $S_2$ says in addition that $A/xA$ has no embedded primes for every nonzerodivisor $x$, by the next proposition.

**Proposition P1.11.3 (the condition $S_2$).** Let $A$ satisfy $S_1$. Then $A$ satisfies $S_2$ if and only if, for every nonzerodivisor $x \in A$ that is not a unit, every associated prime of $A/xA$ has height $1$.

Lean: not in Mathlib.

*Proof.* Let $x$ be a nonzerodivisor and $\mathfrak{p} \supseteq xA$ a prime. Then $x/1$ is a nonzerodivisor of $A_\mathfrak{p}$ by exactness of localization, so $\operatorname{depth} (A/xA)_\mathfrak{p} = \operatorname{depth} A_\mathfrak{p} - 1$ by Section 10.1, and $\operatorname{ht} \mathfrak{p} \geq 1$. By the lemma, $\mathfrak{p} \in \operatorname{Ass}(A/xA)$ if and only if $\operatorname{depth} A_\mathfrak{p} = 1$.

Assume $S_2$ and $\mathfrak{p} \in \operatorname{Ass}(A/xA)$. Then $1 = \operatorname{depth} A_\mathfrak{p} \geq \min(2, \operatorname{ht} \mathfrak{p})$, so $\operatorname{ht} \mathfrak{p} = 1$. Conversely, let $\mathfrak{p}$ be a prime with $\operatorname{ht} \mathfrak{p} \geq 2$. By $S_1$ and the lemma, the associated primes of $A$ have height $0$, so $\mathfrak{p}$ is not contained in any of them, and by prime avoidance (Proposition P1.1.11) there is $x \in \mathfrak{p}$ that is a nonzerodivisor on $A$. If $\operatorname{depth} A_\mathfrak{p} = 1$, then $\mathfrak{p} \in \operatorname{Ass}(A/xA)$ with $\operatorname{ht} \mathfrak{p} \geq 2$, against the assumption. So $\operatorname{depth} A_\mathfrak{p} \geq 2$. For $\operatorname{ht} \mathfrak{p} = 1$, $S_1$ gives $\operatorname{depth} A_\mathfrak{p} \geq 1$, and for $\operatorname{ht} \mathfrak{p} = 0$ there is nothing to prove. $\square$

**Proposition P1.11.4 (depth two and extension).** Let $I \neq A$ be an ideal. Restriction of homomorphisms gives a map $\rho : A = \operatorname{Hom}_A(A, A) \to \operatorname{Hom}_A(I, A)$, $a \mapsto (b \mapsto ab)$. Then $\rho$ is bijective if and only if $\operatorname{depth}_I(A) \geq 2$.

Lean: not in Mathlib.

*Proof.* Apply $\operatorname{Hom}_A(-, A)$ to $0 \to I \to A \to A/I \to 0$. Since $A$ is free, $\operatorname{Ext}^1_A(A, A) = 0$, and the long exact sequence is
$$
0 \to \operatorname{Hom}_A(A/I, A) \to A \xrightarrow{\rho} \operatorname{Hom}_A(I, A) \to \operatorname{Ext}^1_A(A/I, A) \to 0 .
$$
So $\rho$ is bijective if and only if $\operatorname{Ext}^0_A(A/I, A) = \operatorname{Ext}^1_A(A/I, A) = 0$, which by Rees's theorem in Section 10.1 means $\operatorname{depth}_I(A) \geq 2$. $\square$

For a reduced ring, a homomorphism $I \to A$ is a regular function on the open set $U = \operatorname{Spec} A \setminus V(I)$ in the following sense: if $I = (a_1, \dots, a_r)$ and $\varphi : I \to A$ is linear, the elements $\varphi(a_i)/a_i \in A_{a_i}$ agree on overlaps, since $a_j \varphi(a_i) = \varphi(a_ia_j) = a_i \varphi(a_j)$. So the proposition says that, when $\operatorname{depth}_I(A) \geq 2$, every such function on $U$ comes from $A$.

**Proposition P1.11.5 (codimension two).** Let $A$ satisfy $S_2$, and let $I$ be an ideal with $\operatorname{ht} \mathfrak{p} \geq 2$ for every prime $\mathfrak{p} \supseteq I$. Then $\operatorname{depth}_I(A) \geq 2$, and every homomorphism $I \to A$ is multiplication by an element of $A$.

Lean: not in Mathlib.

*Proof.* If $I = A$ there is nothing to prove, so let $I \neq A$. By $S_1$ and the lemma, every associated prime of $A$ has height $0$, so $I$ is contained in none of them, and prime avoidance gives $x \in I$ that is a nonzerodivisor on $A$. By the proposition on $S_2$, every associated prime of $A/xA$ has height $1$, so $I$ is contained in none of them, and there is $y \in I$ that is a nonzerodivisor on $A/xA$. Since $I \neq A$, $A/(x, y) \neq 0$, so $x, y$ is an $A$-sequence in $I$, and $\operatorname{depth}_I(A) \geq 2$. The last statement is the proposition on depth two and extension. $\square$

**Theorem P1.11.6 (algebraic Hartogs property).** Let $A$ be a Noetherian domain with fraction field $K$. If $A$ satisfies $S_2$, then
$$
A = \bigcap_{\operatorname{ht} \mathfrak{p} = 1} A_\mathfrak{p}
$$
inside $K$.

Lean: not in Mathlib.

*Proof.* The inclusion $\subseteq$ is clear. Let $f \in K$ lie in every $A_\mathfrak{p}$ with $\operatorname{ht} \mathfrak{p} = 1$, and write $f = a/b$ with $a, b \in A$, $b \neq 0$. If $b$ is a unit, $f \in A$. Otherwise, by the proposition on $S_2$, the associated primes $\mathfrak{p}_1, \dots, \mathfrak{p}_n$ of $A/bA$ have height $1$, so they are the minimal primes of $bA$, and there are no embedded components. Let $bA = \mathfrak{q}_1 \cap \dots \cap \mathfrak{q}_n$ be a minimal primary decomposition with $\sqrt{\mathfrak{q}_i} = \mathfrak{p}_i$ (Theorem P1.2.47). Each $\mathfrak{q}_i$ is an isolated component, so $\mathfrak{q}_i = bA_{\mathfrak{p}_i} \cap A$ by the second uniqueness theorem (Theorem P1.2.35). Since $f \in A_{\mathfrak{p}_i}$, $a = bf \in bA_{\mathfrak{p}_i} \cap A = \mathfrak{q}_i$ for each $i$, so $a \in bA$ and $f \in A$. $\square$

For a Noetherian normal domain this is Corollary P1.8.3. The theorem shows that the proof of that corollary used only the condition $S_2$, which holds for normal domains by Section 11.2.

### Proof in words

Depth at least one in an ideal means that no element is killed by the whole ideal, and depth at least two means that in addition every homomorphism from the ideal to the ring is given by an element of the ring. The second condition is the algebraic form of the extension of functions across the zero set of the ideal. The condition $S_2$ gives depth two in every ideal of height at least two, because a nonzerodivisor exists by $S_1$ and the quotient by it has no embedded primes. For a domain, the absence of embedded primes in every $A/bA$ says that divisibility by $b$ can be tested at the height one primes, and this is the Hartogs property.

### Examples

**Example P1.11.7 (the plane minus a point).** For $A = k[x, y]$ and $I = (x, y)$, the sequence $x, y$ is regular, so $\operatorname{depth}_I(A) = 2$, and every function on $\mathbb{A}^2 \setminus \{0\}$ extends. This is Example P1.8.6 in the language of this section: a homomorphism $\varphi : (x, y) \to A$ gives $\varphi(x)/x = \varphi(y)/y \in A_x \cap A_y = A$.

**Example P1.11.8 (two planes meeting in a point).** Let $A = k[x, y, z, w]/((x, y) \cap (z, w))$ and $\mathfrak{m} = (x, y, z, w)$, as in Example P1.5.50. The origin has codimension $2$ in each plane. Let $\varphi : \mathfrak{m} \to A$ be the map that is the identity on the ideal $(x, y)$ and zero on the ideal $(z, w)$. It is well defined, since $(x, y) \cap (z, w) = 0$ in $A$ and $\mathfrak{m} = (x, y) + (z, w)$. It is the function that is $1$ on the plane $z = w = 0$ and $0$ on the plane $x = y = 0$, outside the origin. If $\varphi$ were multiplication by $a \in A$, then $ax = x$ and $az = 0$, so $a \equiv 1$ modulo $(z, w)$ and $a \equiv 0$ modulo $(x, y)$, which is impossible at the origin. So $\rho$ is not surjective, $\operatorname{depth}_\mathfrak{m}(A) \leq 1$, and $A$ fails $S_2$ at $\mathfrak{m}$, in agreement with Section 10.1.

**Example P1.11.9 (a non-normal surface).** Let $A = k[s^4, s^3t, st^3, t^4]$ with $\mathfrak{m}$ the ideal of the vertex, and $f = s^2t^2 \in K$. As in Example P1.10.20, each generator of $\mathfrak{m}$ times $f$ lies in $A$: the products are $s^6t^2 = (s^3t)^2$, $s^5t^3 = s^4 \cdot st^3$, $s^3t^5 = s^3t \cdot t^4$ and $s^2t^6 = (st^3)^2$. So multiplication by $f$ is a homomorphism $\mathfrak{m} \to A$ that is not multiplication by an element of $A$, since $f \notin A$. So $A$ fails $S_2$ at the vertex, and the function $f$ on the punctured surface does not extend. By Exercise 6, $f$ lies in $A_\mathfrak{p}$ for every prime $\mathfrak{p}$ of height one, so the Hartogs property fails too.

**Example P1.11.10 (an embedded point).** Let $A = k[x, y]/(x^2, xy)$. The prime $(x, y)$ is associated, so $A$ fails $S_1$. Its only minimal prime is $(x)$, and $A_{(x)}$ is the field $k(y)$, since $y$ is a unit there and $xy = 0$ forces $x = 0$. So $A$ satisfies $R_0$ but not $S_1$. It does not satisfy $R_1$, since the prime $(x, y)$ has height $1$ and $A_{(x, y)}$ is not a domain.

### Exercises

1. (A) Show that every Noetherian ring satisfies $S_0$, and that a Noetherian domain satisfies $S_1$.
2. (A) Show that a Noetherian ring of dimension $1$ satisfies $S_2$ if and only if it satisfies $S_1$, if and only if it is Cohen-Macaulay.
3. (A) Let $A = k[x, y, z]/(xy, xz)$, the union of a plane and a line. Find the primes where $S_2$ fails, and give a homomorphism $\mathfrak{m} \to A$ that does not extend, with $\mathfrak{m} = (x, y, z)$.
4. (B) Let $A$ be a Noetherian ring and $I$ an ideal with $\operatorname{depth}_I(A) \geq 2$. Show that $\operatorname{Hom}_A(I^n, A) = A$ for every $n \geq 1$. (Hint: $I^n$ and $I$ have the same radical; use the lemma on homomorphisms in Section 10.1 twice.)
5. (B) Let $A$ satisfy $S_2$ and $x \in A$ a nonzerodivisor. Show that $A/xA$ satisfies $S_1$. (Hint: use the lemma and the proposition on $S_2$.)
6. (B) In the example of the non-normal surface, show that $A_{t^4}$ and $A_{s^4}$ are normal, and deduce that $f = s^2t^2$ lies in $A_\mathfrak{p}$ for every prime $\mathfrak{p}$ of height one. (Hint: $A_{s^4} = k[s^4, s^{-4}, t/s]$.)
7. (C) Let $A$ satisfy $S_2$, $I$ as in the proposition on codimension two, and $U = \operatorname{Spec} A \setminus V(I)$. Let $I = (a_1, \dots, a_r)$ and let $f_i \in A_{a_i}$ satisfy $f_i = f_j$ in $A_{a_ia_j}$ for all $i, j$. Show that there is a unique $f \in A$ with $f = f_i$ in $A_{a_i}$ for all $i$. (Hint: some power $a_i^N$ makes all $a_i^N f_i$ lie in $A$; apply the proposition to $I' = (a_1^N, \dots, a_r^N)$.)

### Lean

Mathlib has depth, `Ideal.depth` and `IsLocalRing.depth`, and the comparison with regular sequences, but it does not define Serre's conditions $R_k$ and $S_k$. The lemma on localization of associated primes in this form, the propositions on $S_2$ and on extension, and the Hartogs property for $S_2$ domains are not in Mathlib. The handbook adds no `MinimalModel` node here.

### Notes and history

The conditions $R_k$ and $S_k$ are named after Serre, who used them in his work of the 1950s on the homological theory of local rings, and Grothendieck used them throughout EGA IV. The link between depth two and the extension of sections is the algebraic form of the theorem of Hartogs on holomorphic functions in several variables, and Grothendieck developed it through local cohomology in his seminar of 1962. The literature state of every result here is theorem. The section follows Matsumura, Chapter 8, and Eisenbud, Chapters 11 and 18.
