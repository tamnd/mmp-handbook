---
title: Kodaira's lemma and big line bundles
nodes: []
sources: [Laz04, Deb01, Eis95, Har77]
reads_with: [Laz04:2.2.A, Deb01:ch1]
requires: [P3.6, P3.10, P5.1, P5.6, P5.11, P7.1, P7.2, P7.3, P7.4]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Kodaira's lemma and big line bundles

### Statement

Throughout, $X$ is a projective variety over $k$ of dimension $n \geq 1$, that is, an integral projective scheme, and $h^0(\mathcal{G}) = \dim_k H^0(X, \mathcal{G})$ for a coherent sheaf $\mathcal{G}$. Since $X$ is integral, a nonzero section of a line bundle is nonzero at the generic point, and the product of two nonzero sections of line bundles is nonzero. A *$\mathbb{Q}$-divisor* is an element of $\operatorname{Div}(X) \otimes \mathbb{Q}$, a finite sum $\sum_i a_i D_i$ with $a_i \in \mathbb{Q}$ and $D_i$ Cartier divisors; its class in $N^1(X)$ is $\sum_i a_i [\mathcal{O}_X(D_i)]$. The cones $\operatorname{Amp}(X)$ and $\operatorname{Nef}(X)$ are those of Definition P7.3.8, and $\operatorname{Eff}(X)$ is the effective cone of Definition P7.4.13.

**Lemma P7.5.1 (a polynomial bound).** Let $Z$ be a projective scheme over $k$, $\mathcal{F}$ a coherent sheaf on $Z$ with $\dim \operatorname{Supp} \mathcal{F} \leq d$, and $L$, $M$ line bundles on $Z$. There is a constant $C$ with $h^0(Z, \mathcal{F} \otimes L^m \otimes M) \leq C m^d$ for every $m \geq 1$.

Lean: not in Lean as stated.

**Definition P7.5.2 (big line bundles).** A line bundle $L$ on $X$ is *big* if
$$\limsup_{m \to \infty} \frac{h^0(X, L^m)}{m^n} > 0.$$
A Cartier divisor $D$ is big if $\mathcal{O}_X(D)$ is. A $\mathbb{Q}$-divisor $D$ is big if $aD$ is a big Cartier divisor for some integer $a \geq 1$ with $aD$ integral; by part 3 of Corollary P7.5.4 this does not depend on $a$.

By Lemma P7.5.1 with $\mathcal{F} = \mathcal{O}_X$ the limit superior is finite, so a big line bundle has as many sections as the dimension allows, up to a constant.

**Theorem P7.5.3 (Kodaira's lemma).** Let $L$ be a big line bundle and $D$ an effective Cartier divisor on $X$. Then $H^0(X, L^m \otimes \mathcal{O}_X(-D)) \neq 0$ for infinitely many $m \geq 1$.

Lean: not in Lean as stated.

**Corollary P7.5.4 (bigness).** Let $L$ be a line bundle on $X$.

1. The following are equivalent: (a) $L$ is big; (b) for every ample line bundle $A$ there is $m \geq 1$ with $H^0(X, L^m \otimes A^{-1}) \neq 0$, that is, $L^m \cong A \otimes \mathcal{O}_X(E)$ with $E$ effective; (c) this holds for one ample line bundle $A$.
2. If $L$ is big, there are $p \geq 1$ and $c > 0$ such that for every effective Cartier divisor $D$, $H^0(X, L^m \otimes \mathcal{O}_X(-D)) \neq 0$ for all large $m$, $H^0(X, L^m) \neq 0$ for all $m \geq p$, and $h^0(X, L^m) \geq c m^n$ for all large $m$.
3. For $a \geq 1$, $L^a$ is big if and only if $L$ is big.
4. If $L' \equiv L$, then $L'$ is big if and only if $L$ is big.
5. If $L$ is big, $E$ is an effective Cartier divisor and $N$ is a nef line bundle, then $L \otimes \mathcal{O}_X(E)$ and $L \otimes N$ are big.
6. If $f \colon Y \to X$ is a surjective morphism from a projective variety with $\dim Y = \dim X$, and $L$ is big, then $f^* L$ is big.

Lean: `MinimalModel.IsBig`, in the project library, is the condition that an $\mathbb{R}$-divisor is $\mathbb{R}$-linearly equivalent to an ample divisor plus an effective divisor, the form of condition (b) of part 1; the equivalence with Definition P7.5.2 is not stated there.

**Definition P7.5.5 (the big cone).** The *big cone* of $X$ is
$$\operatorname{Big}(X) = \operatorname{Amp}(X) + \operatorname{Eff}(X) = \{ \alpha + \varepsilon : \alpha \in \operatorname{Amp}(X), \ \varepsilon \in \operatorname{Eff}(X) \} \subseteq N^1(X).$$
A class in $\operatorname{Big}(X)$ is *big*, and so is an $\mathbb{R}$-Cartier divisor whose class is big.

**Proposition P7.5.6 (the big cone).**

1. $\operatorname{Big}(X)$ is an open convex subset of $N^1(X)$, stable under sums and under multiplication by positive reals, and $\operatorname{Big}(X) + \operatorname{Eff}(X) \subseteq \operatorname{Big}(X)$ and $\operatorname{Big}(X) + \operatorname{Nef}(X) \subseteq \operatorname{Big}(X)$.
2. A line bundle $L$ is big if and only if $[L] \in \operatorname{Big}(X)$. The same holds for $\mathbb{Q}$-divisors, so the two meanings of big agree.
3. $\operatorname{Big}(X) \subseteq \operatorname{Eff}(X)$.

Lean: not in Lean as stated.

### Proof in words

The sections of $L^m$ that vanish on an effective divisor $D$ are the kernel of the restriction to $D$. Since $D$ has dimension $n - 1$, the restriction lands in a space of dimension at most a constant times $m^{n-1}$, while a big bundle has about $m^n$ sections. So for many $m$ the kernel is not zero, which is Kodaira's lemma. Applied to a divisor of a multiple of an ample bundle $A$, it writes a multiple of $L$ as $A$ plus an effective divisor; conversely such a decomposition gives at least as many sections as the multiples of $A$ have, which is about $m^n$ by asymptotic Riemann-Roch.

The decomposition ample plus effective is stable under the operations that do not destroy ampleness: twisting by a numerically trivial bundle, by a nef bundle or by an effective divisor, and passing to multiples. So bigness is numerical, and it is natural to define the big cone in $N^1(X)$ as the sum of the ample cone and the effective cone. Rational perturbation inside the open ample cone identifies the line bundles with classes in this cone with the big line bundles.

### Examples

**Example P7.5.7 (curves).** Let $X = C$ be a smooth projective curve and $L$ of degree $d$. By part 1 of Proposition P5.11.3, $h^0(L^m) \leq \max(0, md + 1)$, and by the theorem of Riemann-Roch (Theorem P5.1.10) $h^0(L^m) \geq md + 1 - g$. So $L$ is big if and only if $d > 0$, that is, if and only if $L$ is ample (part 3 of Corollary P5.1.20). On a curve $\operatorname{Big}(C) = \operatorname{Amp}(C) = \mathbb{R}_{> 0}$.

**Example P7.5.8 (a fibre of a Hirzebruch surface).** Let $X = \mathbb{F}_n$, $n \geq 1$, with $C_-$ and $F$ as in Proposition P7.4.19. The bundle $\mathcal{O}(F)$ is the pullback of $\mathcal{O}_{\mathbb{P}^1}(1)$ under the ruling $q$, so it is nef and $h^0(mF) \geq m + 1$. On the other hand, the exact sequence $0 \to \mathcal{O}(mF - C_-) \to \mathcal{O}(mF) \to \mathcal{O}_{C_-}(mF) \to 0$ gives $h^0(mF) \leq h^0(mF - C_-) + h^0(C_-, \mathcal{O}(mF)|_{C_-})$. The curve $C_- \cong \mathbb{P}^1$ meets $F$ once, so $\mathcal{O}(mF)|_{C_-}$ has degree $m$ and $m + 1$ sections. The class $mF - C_-$ has $(mF - C_-) \cdot F = -1 < 0$, and the fibres of $q$ form a set of curves of class $[F]$ covering $X$, so by part 2 of Proposition P7.4.15 $mF - C_-$ is not pseudo-effective, and in particular has no section. Hence $h^0(mF) = m + 1$, and $F$ is nef but not big.

**Example P7.5.9 (an effective divisor that is not big).** Let $X = \operatorname{Bl}_p \mathbb{P}^2$ with exceptional curve $E$. By part 3 of Corollary P5.6.5, $h^0(mE) = 1$ for all $m \geq 0$, so $E$ is effective and not big. Effective divisors with few sections are common, and the big cone sits strictly inside the effective cone whenever $X$ carries a divisor of this kind.

**Example P7.5.10 (big and nef, not ample).** Let $\pi \colon X = \operatorname{Bl}_p \mathbb{P}^n \to \mathbb{P}^n$, $n \geq 2$, with $H$ the pullback of a hyperplane. Pullback of sections embeds $H^0(\mathbb{P}^n, \mathcal{O}(m))$ in $H^0(X, mH)$, so $h^0(mH) \geq \binom{m + n}{n}$ and $H$ is big. It is nef, as the pullback of an ample bundle, and it is not ample, since $H \cdot e = 0$ for a line $e$ in the exceptional divisor (Example P7.2.25). So $[H]$ lies in $\operatorname{Big}(X)$ and on the boundary of $\operatorname{Nef}(X)$. Explicitly, $H = (H - \tfrac12 E) + \tfrac12 E$ with $H - \tfrac12 E$ ample by part 1 of Proposition P7.4.18, which writes $[H]$ as an ample class plus an effective class.

### Proof

*Lemma P7.5.1.* Replacing $\mathcal{F}$ by $\mathcal{F} \otimes M$, which has the same support, assume $M = \mathcal{O}_Z$. By part 2 of Lemma P7.1.1, $L \cong A \otimes B^{-1}$ with $A$ and $B$ very ample. The coherent sheaf $\mathcal{F}$ has finitely many associated points (Eisenbud, Theorem 3.1, in Eis95), so by part 1 of Lemma P7.1.1 there is $\sigma \in H^0(Z, B)$ that vanishes at none of them. Then $\sigma^m \in H^0(Z, B^m)$ vanishes at none of them either, and by part 1 of Lemma P7.1.2 multiplication by $\sigma^m$ is an injection $\mathcal{F} \otimes L^m \to \mathcal{F} \otimes L^m \otimes B^m = \mathcal{F} \otimes A^m$. So $h^0(\mathcal{F} \otimes L^m) \leq h^0(\mathcal{F} \otimes A^m)$. If $\mathcal{F} = 0$ there is nothing to prove. Otherwise let $d' = \dim \operatorname{Supp} \mathcal{F} \leq d$; by part 3 of Theorem P7.1.17, $h^0(\mathcal{F} \otimes A^m) = \frac{(A^{d'} \cdot \mathcal{F})}{d'!} m^{d'} + O(m^{d'-1})$, which is at most $C' m^d$ for $m \geq 1$, for a suitable $C'$.

*Theorem P7.5.3.* If $D = 0$ the claim is that $H^0(L^m) \neq 0$ for infinitely many $m$, which follows from the definition. Otherwise let $s_D$ be the canonical section of $\mathcal{O}_X(D)$. It does not vanish at the generic point, the only associated point of $\mathcal{O}_X$, so part 1 of Lemma P7.1.2 gives the exact sequence $0 \to \mathcal{O}_X(-D) \to \mathcal{O}_X \to \mathcal{O}_D \to 0$, and part 3 gives $\dim D \leq n - 1$. Tensoring with $L^m$ and taking sections,
$$0 \to H^0(X, L^m(-D)) \to H^0(X, L^m) \to H^0(D, L^m|_D).$$
By Lemma P7.5.1 with $\mathcal{F} = \mathcal{O}_D$, $h^0(D, L^m|_D) \leq C m^{n-1}$. Since $L$ is big there are $c > 0$ and infinitely many $m$ with $h^0(L^m) \geq c m^n$. For those $m$ with $c m^n > C m^{n-1}$, the restriction map is not injective, and $H^0(L^m(-D)) \neq 0$.

*Corollary P7.5.4.* Part 1. Assume (a) and let $A$ be ample. By part 2 of Proposition P3.10.27 with $\mathcal{M} = \mathcal{O}_X$, $A^j$ is very ample for all large $j$; fix $r \geq 2$ with $A^r$ and $A^{r-1}$ very ample. By part 1 of Lemma P7.1.1, $A^r$ has a nonzero section; let $D$ be its divisor, so $\mathcal{O}_X(D) \cong A^r$. By Theorem P7.5.3 there is $m$ with a nonzero section $t$ of $L^m \otimes A^{-r}$. Multiplying $t$ by a nonzero section of $A^{r-1}$ gives a nonzero section of $L^m \otimes A^{-1}$, which is (b). Clearly (b) implies (c). Assume (c), with $L^m \cong A \otimes \mathcal{O}_X(E)$ and $E$ effective. Multiplication by $s_E^j$ embeds $H^0(A^j)$ in $H^0(L^{mj})$, so by part 3 of Theorem P7.1.17 with $\mathcal{F} = \mathcal{O}_X$,
$$\limsup_{q \to \infty} \frac{h^0(L^q)}{q^n} \geq \limsup_{j \to \infty} \frac{h^0(A^j)}{(mj)^n} = \frac{(A^n)}{n! \, m^n} > 0,$$
and $L$ is big.

Part 2. Let $H$ be very ample and $D$ effective. By part 2 of Proposition P3.10.27, applied with $\mathcal{M}$ equal to $\mathcal{O}_X$, $L$, $\mathcal{O}_X(-D)$ and $L(-D)$, there is $s$ such that $B = H^s$, $B \otimes L$, $B(-D)$ and $B \otimes L(-D)$ are all very ample, hence have nonzero sections by part 1 of Lemma P7.1.1. By part 1 there is $p$ with $L^p \cong B \otimes \mathcal{O}_X(E)$, $E$ effective. Then $L^p$, $L^{p+1} \cong (B \otimes L)(E)$, $L^p(-D) \cong B(-D)(E)$ and $L^{p+1}(-D) \cong (B \otimes L(-D))(E)$ all have nonzero sections. Every integer $m \geq p(p-1)$ is a sum $m = \alpha p + \beta (p + 1)$ with $\alpha, \beta \geq 0$: write $m = \gamma p + \beta$ with $0 \leq \beta < p$, so $\gamma \geq p - 1 \geq \beta$, and take $\alpha = \gamma - \beta$. So $H^0(L^m) \neq 0$ for $m \geq p(p-1)$. For $m \geq p^2$, write $L^m(-D) = L^{p}(-D) \otimes L^{m - p}$ with $m - p \geq p(p-1)$, so $H^0(L^m(-D)) \neq 0$; this gives the first two claims, with $p(p-1)$ in place of $p$, where $p$ does not depend on $D$ for the second claim. For the bound, let $m \geq p^2 + p$ and write $m = jp + q$ with $p^2 \leq q < p^2 + p$, so $j \geq (m - p^2 - p)/p$. A nonzero section of $L^q$ times $s_E^j$ embeds $H^0(B^j)$ in $H^0(L^m)$, and $h^0(B^j) \geq \frac{(B^n)}{2 \, n!} j^n$ for large $j$ by part 3 of Theorem P7.1.17. For $m \geq 2(p^2 + p)$, $j \geq m/(2p)$, and the bound follows.

Part 3. If $L^a$ is big, the limit superior of $h^0(L^q)/q^n$ over the multiples $q = am$ is $a^{-n} \limsup_m h^0(L^{am})/m^n > 0$, so $L$ is big. If $L$ is big, part 2 gives $h^0(L^{am}) \geq c a^n m^n$ for large $m$, so $L^a$ is big.

Part 4. Write $L' = L \otimes P$ with $P \equiv 0$. Let $A$ be ample and $L^m \cong A(E)$ with $E$ effective, by part 1. Then $L'^m \cong (A \otimes P^m)(E)$, and $A \otimes P^m \equiv A$ is ample by Corollary P7.3.4. So $L'$ satisfies (c) of part 1 with the ample bundle $A \otimes P^m$. The converse follows by symmetry.

Part 5. Let $L^m \cong A(E')$ with $A$ ample and $E'$ effective. Then $(L(E))^m \cong A(E' + mE)$, so $L(E)$ is big by part 1. Also $(L \otimes N)^m \cong (A \otimes N^m)(E')$, and $A \otimes N^m$ is ample by parts 2 and 3 of Theorem P7.3.12, since $[A] + m[N]$ is an ample class plus a nef class. So $L \otimes N$ is big.

Part 6. The morphism $f$ is dominant and $Y$ is integral, so the generic point of $Y$ maps to the generic point of $X$, and the pullback of a nonzero section of $L^m$ is a nonzero section of $f^* L^m$. Hence $h^0(Y, f^* L^m) \geq h^0(X, L^m)$, and $f^* L$ is big since $\dim Y = n$.

*Proposition P7.5.6.* Part 1. $\operatorname{Amp}(X)$ is an open convex cone (part 1 of Theorem P7.3.12) and $\operatorname{Eff}(X)$ is a convex cone, so their sum is convex and stable under sums and positive multiples. It is open, since $\alpha + \varepsilon + U \subseteq \operatorname{Big}(X)$ whenever $\alpha + U \subseteq \operatorname{Amp}(X)$. The inclusion $\operatorname{Big}(X) + \operatorname{Eff}(X) \subseteq \operatorname{Big}(X)$ holds because $\operatorname{Eff}(X)$ is stable under sums, and $\operatorname{Big}(X) + \operatorname{Nef}(X) \subseteq \operatorname{Big}(X)$ because $\operatorname{Amp}(X) + \operatorname{Nef}(X) \subseteq \operatorname{Amp}(X)$ by part 3 of Theorem P7.3.12.

Part 2. If $L$ is big, part 1 of Corollary P7.5.4 gives $L^m \cong A(E)$, so $m[L] = [A] + [E] \in \operatorname{Big}(X)$ and $[L] \in \operatorname{Big}(X)$. Conversely let $[L] = \alpha + \sum_j b_j [E_j]$ with $\alpha$ ample, $b_j \geq 0$ real and $E_j$ effective Cartier divisors. Since $\operatorname{Amp}(X)$ is open, there are rational $b'_j \geq 0$ so close to $b_j$ that $\alpha' = [L] - \sum_j b'_j [E_j]$ is still ample. Choose $q \geq 1$ with all $q b'_j$ integers, and put $E = \sum_j q b'_j E_j$, an effective Cartier divisor. The line bundle $A' = L^q(-E)$ has class $q \alpha' \in \operatorname{Amp}(X)$, so it is ample by part 2 of Theorem P7.3.12, and $L^q \otimes A'^{-1} \cong \mathcal{O}_X(E)$ has a nonzero section. By part 1 of Corollary P7.5.4, $L^q$ is big, and by part 3 so is $L$. For a $\mathbb{Q}$-divisor $D$ with $aD$ integral, $[D] \in \operatorname{Big}(X)$ if and only if $a[D] = [\mathcal{O}_X(aD)] \in \operatorname{Big}(X)$, by part 1.

Part 3. By part 1 of Proposition P7.4.15, $\operatorname{Amp}(X) \subseteq \operatorname{Eff}(X)$, so $\operatorname{Big}(X) \subseteq \operatorname{Eff}(X) + \operatorname{Eff}(X) = \operatorname{Eff}(X)$.

### Exercises

1. (A) Let $X = \mathbb{P}^1 \times \mathbb{P}^1$ and $L = \mathcal{O}(a, b)$. Using Lemma P5.11.4, show that $L$ is big if and only if $a > 0$ and $b > 0$, and that this is also the condition for ampleness.
2. (A) On $\operatorname{Bl}_p \mathbb{P}^2$, write $H + E = (H - \tfrac13 E) + \tfrac43 E$ and deduce that $H + E$ is big. Compute $h^0(m(H + E))$ with part 3 of Corollary P5.6.5.
3. (B) Show that the integer $p$ of part 2 of Corollary P7.5.4 cannot be taken to be $1$ in general: on $\mathbb{P}^1 \times E$, with $E$ an elliptic curve and $\eta$ of order $2$ in $\operatorname{Pic}^0(E)$, find a big line bundle $L$ with $H^0(L) = 0$.
4. (B) Let $L$ be big and nef. Show that $L^m \otimes A^{-1}$ is effective for some $m$ and every ample $A$, and that $L \otimes A$ is ample for every ample $A$, using Theorem P7.3.12. Show by an example that a big line bundle $L$ can have $L \otimes A$ not ample for some ample $A$.
5. (B) Let $f \colon Y \to X$ be a surjective morphism of projective varieties with $\dim Y > \dim X$. Show that $f^* L$ is never big. Then show, for a birational morphism $f$ onto a normal $X$, that $f^* L$ is big if and only if $L$ is, using Theorem P4.6.8 and Proposition P4.4.10.
6. (C) Let $X$ be a normal projective variety and $L$ a line bundle such that $h^0(L^m) \geq 2$ for some $m$ and the rational map of $|L^m|$ is birational onto its image. Show that $L$ is big. Conversely, show that a big line bundle has a multiple whose rational map is birational onto its image.

### Lean

The project library defines `MinimalModel.IsBig` for an $\mathbb{R}$-divisor $D$ on a normal variety as the existence of an ample $A$ and an effective $E$ with $D$ $\mathbb{R}$-linearly equivalent to $A + E$, and `MinimalModel.IsREffective` as $\mathbb{R}$-linear equivalence to an effective divisor. The equivalence of this form with the growth condition of Definition P7.5.2, which is Kodaira's lemma, is not stated in the library, and neither is Lemma P7.5.1. Mathlib has no intersection numbers or big line bundles on projective schemes. The handbook adds no `MinimalModel` node here.

### Notes and history

Kodaira's lemma goes back to Kodaira's work on compact complex surfaces and the vanishing theorems; the form here, with the decomposition of a multiple into an ample and an effective part, is Lazarsfeld, Proposition 2.2.6 and Corollary 2.2.7 (Laz04), with the same proof by restriction to a divisor. Debarre, Section 1.5 (Deb01), proves the same statements. The literature state is theorem. The definition of bigness by growth of sections works over any algebraically closed field, and so do all the proofs here. In the minimal model program bigness is used in the relative form, over a base, and the library takes the decomposition ample plus effective as the definition, which is the conclusion of Kodaira's lemma. Section 6.1 shows that a line bundle is big exactly when its Iitaka dimension is $n$.
