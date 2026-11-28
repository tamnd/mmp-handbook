---
title: The Kawamata-Viehweg vanishing theorem
nodes: []
sources: [Laz04, KM98, EV92, Kaw82, Vie82, Hir64, Har77]
reads_with: [Laz04:4.3, KM98:2.4, EV92:5]
requires: [P1.8, P2.4, P4.4, P4.7, P5.6, P7.3, P8.13, 1.3, 4.2, 4.6]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The Kawamata-Viehweg vanishing theorem

### Statement

Throughout, $X$ is a smooth projective variety of dimension $n$ over $k$, of characteristic $0$, and the language of $\mathbb{Q}$-divisors is that of Definition P7.8.1. For a proper birational morphism $\mu \colon X' \to X$ from a smooth variety, the *relative canonical divisor* $K_{X'/X} = \sum_E k_E E$ is the divisor of the pullback of a local generator of $\omega_X$, so that $K_{X'} = \mu^* K_X + K_{X'/X}$; it is effective and exceptional, and $k_E = a(E, X) \geq 1$ for every exceptional prime $E$ (Definition P8.13.1 and Proposition P8.13.4).

**Lemma P7.8.14 (snc pairs with small coefficients).** Let $D_1, \dots, D_r$ be smooth divisors with $D_1 + \dots + D_r$ reduced snc, $\mu \colon X' \to X$ a proper birational morphism from a smooth variety and $E$ an exceptional prime divisor on $X'$. Then
$$\sum_{j=1}^r \operatorname{ord}_E(\mu^* D_j) \leq k_E + 1.$$
So if $\Delta = \sum_j a_j D_j$ with every $a_j < 1$, then $\operatorname{ord}_E(\mu^* \Delta) < k_E + 1$, that is, $a(E, X, \Delta) > -1$.

Lean: not in Lean as stated.

**Theorem P7.8.15 (log resolutions, black box).** Let $D$ be a divisor on $X$. There is a proper birational morphism $\mu \colon X' \to X$ from a smooth projective variety, a composition of blow-ups along smooth centres, such that the exceptional set $\operatorname{Exc}(\mu)$ is a divisor and $\mu^{-1}_* D + \operatorname{Exc}(\mu)$ is a reduced snc divisor. There is an effective $\mu$-exceptional divisor $F$ with $-F$ ample over $X$, and then $\mu^* A - \delta F$ is ample for every ample $\mathbb{Q}$-divisor $A$ on $X$ and every rational $0 < \delta \leq \delta_0(A)$.

Lean: not in Lean as stated.

**Lemma P7.8.16 (relative vanishing from absolute vanishing).** Let $f \colon X' \to Z$ be a morphism of projective schemes, $A$ an ample line bundle on $Z$ and $\mathcal{F}$ a coherent sheaf on $X'$. If $H^i(X', \mathcal{F} \otimes f^* A^m) = 0$ for every $i > 0$ and every $m \geq m_0$, then $R^j f_* \mathcal{F} = 0$ for every $j > 0$, and $H^i(Z, f_* \mathcal{F} \otimes A^m) = 0$ for $i > 0$ and $m \geq m_0$.

Lean: not in Lean as stated.

**Proposition P7.8.17 (Kawamata-Viehweg, the ample case).** Let $N$ be a Cartier divisor on $X$ and $\Delta = \sum_{j=1}^r a_j D_j$, with $D_1, \dots, D_r$ smooth divisors such that $D_1 + \dots + D_r$ is reduced snc and $a_j \in \mathbb{Q} \cap [0, 1)$. If $N - \Delta$ is ample, then
$$H^i(X, \mathcal{O}_X(K_X + N)) = 0 \quad \text{for } i > 0.$$

Lean: not in Lean as stated.

**Theorem P7.8.18 (Kawamata-Viehweg vanishing).** Let $N$ be a Cartier divisor on $X$ and $\Delta = \sum_j a_j D_j$ a $\mathbb{Q}$-divisor with snc support and $0 \leq a_j < 1$. If $N - \Delta$ is nef and big, then
$$H^i(X, \mathcal{O}_X(K_X + N)) = 0 \quad \text{for } i > 0.$$

Lean: `MinimalModel.KawamataViehweg` states the relative klt form of Kollár and Mori, Theorem 2.70, without proof, and `MinimalModelBridge.KawamataViehwegSNC` states the form of KM98, Theorem 2.64; neither is the statement here verbatim.

**Corollary P7.8.19 (two standard forms).**

1. Let $D$ be a nef and big $\mathbb{Q}$-divisor whose fractional part $\{D\}$ has snc support. Then $H^i(X, \mathcal{O}_X(K_X + \lceil D \rceil)) = 0$ for $i > 0$.
2. Let $L$ be a nef and big line bundle. Then $H^i(X, \omega_X \otimes L) = 0$ for $i > 0$ and $H^i(X, L^{-1}) = 0$ for $i < n$.

Lean: not in Lean as stated.

### Proof in words

The proof has two steps, and both turn the theorem into Kodaira's theorem on another variety. In the first step the class $N - \Delta$ is ample. The coverings of Section 8.2 make the last coefficient $a_r = p/q$ integral: a Bloch-Gieseker cover makes $\mathcal{O}(D_r)$ a $q$-th power, and the cyclic cover then extracts a $q$-th root of $D_r$, so that $a_r D_r$ pulls back to $p D'$ with $D'$ reduced. The integral divisor $f^* N - p D'$ minus the remaining fractional part is ample, so the case with $r - 1$ components applies upstairs. The trace brings the vanishing down. The point of the computation in part 4 of Proposition P7.8.10 is that the forms pulled back from $X$ vanish to order $q - 1 \geq p$ along $D'$, so the cohomology of $K_X + N$ is a direct summand of the cohomology of $K_Y + f^* N - p D'$ and not only of $K_Y + f^* N$.

In the second step $N - \Delta$ is nef and big. Kodaira's lemma writes a big class as an ample class plus an effective one, and since a nef class plus an ample class is ample, $N - \Delta$ becomes ample after subtracting $\varepsilon E$ for a small multiple of an effective divisor $E$. The new boundary $\Delta + \varepsilon E$ need not have snc support, so pass to a log resolution and subtract a small multiple of the exceptional divisor $F$ to keep ampleness. The ample case applies upstairs to the round-down of the pulled back boundary. Lemma P7.8.14 says that a boundary with snc support and coefficients below $1$ pulls back to a divisor whose exceptional coefficients stay below $k_E + 1$, so the round-down is absorbed by $K_{X'/X}$, and the leftover is an effective exceptional divisor that pushes forward to $\mathcal{O}_X$. The ample case also gives relative vanishing by Lemma P7.8.16, and the Leray spectral sequence carries the vanishing down to $X$.

### Examples

**Example P7.8.20 (curves).** Let $C$ be a smooth projective curve and $D$ a $\mathbb{Q}$-divisor of positive degree, which is nef and big. Then $\deg \lceil D \rceil \geq \deg D > 0$, so $H^1(C, \omega_C(\lceil D \rceil)) = H^0(C, \mathcal{O}_C(-\lceil D \rceil))' = 0$, as part 1 of Corollary P7.8.19 says. The round-up cannot be replaced by the round-down: for $D = \frac12 P$ with $P$ a point, $\lfloor D \rfloor = 0$ and $H^1(C, \omega_C) = k$.

**Example P7.8.21 (nef and big, not ample).** Let $\pi \colon X \to \mathbb{P}^2$ be the blow-up of a point, with $H$ and $E$ as in Example P7.8.6. The class $H$ is nef and big, $H^2 = 1$, and not ample, since $H \cdot E = 0$. Kodaira's theorem does not apply, and part 2 of Corollary P7.8.19 gives $H^i(X, \mathcal{O}_X(K_X + H)) = 0$ for $i > 0$. Directly: $K_X + H = -2H + E$, $h^0 = 0$ since $H^0(\mathbb{P}^2, \mathcal{O}(-2)) = 0$, $h^2 = h^0(X, -H) = 0$, and $\chi = 1 + \frac12 (-2H + E) \cdot H = 0$, so $h^1 = 0$.

**Example P7.8.22 (three concurrent lines).** Let $L_1, L_2, L_3 \subseteq \mathbb{P}^2$ be distinct lines through a point $p$, and $D = c(L_1 + L_2 + L_3)$ with $0 < c < 1$. Then $D \equiv 3cH$ is ample, but $\operatorname{Supp} D$ is not snc at $p$, where three components meet on a surface. Let $\mu \colon X' \to \mathbb{P}^2$ be the blow-up of $p$, with exceptional curve $E$ and strict transforms $L_j'$, so $\mu^* L_j = L_j' + E$ and the $L_j'$ are disjoint fibres of the ruling of $X'$, each meeting $E$ transversally. Then
$$\mu^* D = c(L_1' + L_2' + L_3') + 3c E$$
is nef and big with snc support, and part 1 of Corollary P7.8.19 on $X'$ gives the vanishing of $H^i(X', \mathcal{O}(K_{X'} + \lceil \mu^* D \rceil))$ for $i > 0$. With $K_{X'} = -3H + E$ and $L_1' + L_2' + L_3' = 3H - 3E$,
$$K_{X'} + \lceil \mu^* D \rceil = -2E + \lceil 3c \rceil E = \begin{cases} -E & 0 < c \leq \tfrac13, \\ 0 & \tfrac13 < c \leq \tfrac23, \\ E & \tfrac23 < c < 1. \end{cases}$$
Each case can be checked by hand. By Proposition P4.4.16, $\mu_* \mathcal{O}(-E) = \mathfrak{m}_p$, $\mu_* \mathcal{O}(E) = \mu_* \mathcal{O} = \mathcal{O}_{\mathbb{P}^2}$, and the three sheaves have no higher direct images, so their cohomology is that of $\mathfrak{m}_p$ and $\mathcal{O}_{\mathbb{P}^2}$. Both have vanishing $H^1$ and $H^2$, by the sequence $0 \to \mathfrak{m}_p \to \mathcal{O} \to k(p) \to 0$ and Theorem P4.2.1. On $\mathbb{P}^2$, $K + \lceil D \rceil = -3H + 3H = 0$ for every $c$, while $\mu_* \mathcal{O}(K_{X'} + \lceil \mu^* D \rceil)$ is $\mathfrak{m}_p$ for $c \leq \frac13$. The difference is measured by the divisor $\lceil D \rceil - D = (1 - c)(L_1 + L_2 + L_3)$, whose multiplicity $3(1 - c)$ at $p$ is at least $2$ exactly when $c \leq \frac13$; it is the multiplier ideal of Chapter 10, computed in Example P7.10.15.

### Proof

*Lemma P7.8.14.* Choose a closed point $x$ in the centre $\mu(E)$, local coordinates $x_1, \dots, x_n$ on a neighbourhood $U$ of $x$ such that the $D_j$ through $x$ are $\{x_1 = 0\}, \dots, \{x_s = 0\}$, after renumbering, and shrink $U$ so that the other $D_j$ do not meet it. On $U$ consider the rational $n$-form
$$\eta = \frac{dx_1}{x_1} \wedge \dots \wedge \frac{dx_s}{x_s} \wedge dx_{s+1} \wedge \dots \wedge dx_n.$$
Since $dx_1 \wedge \dots \wedge dx_n$ generates $\omega_U$, the order of $\mu^* \eta$ along $E$ is $k_E - \sum_{j \leq s} \operatorname{ord}_E(\mu^* x_j) = k_E - \sum_j \operatorname{ord}_E(\mu^* D_j)$. Now compute the same order directly. Choose a closed point $y \in E \cap \mu^{-1}(U)$ at which $E$ is the only component of $\operatorname{Supp} \mu^*(x_1 \cdots x_s)$, and coordinates $y_1, \dots, y_n$ at $y$ with $E = \{y_1 = 0\}$. Then $\mu^* x_j = y_1^{e_j} u_j$ with $u_j$ a unit near $y$ and $e_j = \operatorname{ord}_E(\mu^* x_j)$, and
$$\mu^* \frac{dx_j}{x_j} = e_j \frac{dy_1}{y_1} + \frac{du_j}{u_j}$$
has at most a simple pole along $E$; the forms $\mu^* dx_i$ for $i > s$ are regular. A wedge product of $1$-forms each lying in $\Omega_{X'}(\log E)$ near $y$ has at most a simple pole along $E$, so $\operatorname{ord}_E(\mu^* \eta) \geq -1$. Hence $\sum_j \operatorname{ord}_E(\mu^* D_j) \leq k_E + 1$. If every $a_j < 1$ and some $\operatorname{ord}_E(\mu^* D_j) > 0$, then $\operatorname{ord}_E(\mu^* \Delta) = \sum_j a_j \operatorname{ord}_E(\mu^* D_j) < \sum_j \operatorname{ord}_E(\mu^* D_j) \leq k_E + 1$; if all the orders are $0$, then $\operatorname{ord}_E(\mu^* \Delta) = 0 < k_E + 1$.

*Theorem P7.8.15.* The existence of $\mu$ is Hironaka's theorem (Hir64), Theorem 4.2.10, in the form of Laz04, Theorem 4.1.3, which also gives the composition of blow-ups along smooth centres; it is a black box here. For a single blow-up $\beta \colon \operatorname{Bl}_Z W \to W$ of a smooth centre, with exceptional divisor $G$, $\mathcal{O}(-G) = \mathcal{O}(1)$ is ample over $W$. If $\mu = \mu' \circ \beta$ and $-F'$ is ample over $X$ for $\mu'$, then $-(c \beta^* F' + G)$ is ample over $X$ for $c \gg 0$ (Har77, Exercise II.7.14), and induction on the number of blow-ups gives $F$. For the last statement, $c \mu^* A - F$ is ample for $c \gg 0$ by the same exercise, and for $0 < \delta \leq 1/c$ the class $\mu^* A - \delta F = (1 - \delta c) \mu^* A + \delta (c \mu^* A - F)$ is a nef class plus an ample class, which is ample by part 3 of Theorem P7.3.12.

*Lemma P7.8.16.* The sheaves $R^j f_* \mathcal{F}$ are coherent (Theorem P4.4.8) and zero for $j$ large. By Theorem P4.2.7 there is $m \geq m_0$ such that, for every $j$, $H^i(Z, R^j f_* \mathcal{F} \otimes A^m) = 0$ for $i > 0$ and $R^j f_* \mathcal{F} \otimes A^m$ is generated by global sections. By the projection formula P4.4.10, $R^j f_*(\mathcal{F} \otimes f^* A^m) = R^j f_* \mathcal{F} \otimes A^m$, so the Leray spectral sequence (Corollary P2.4.26)
$$E_2^{i,j} = H^i(Z, R^j f_* \mathcal{F} \otimes A^m) \Rightarrow H^{i+j}(X', \mathcal{F} \otimes f^* A^m)$$
has $E_2^{i,j} = 0$ for $i > 0$ and gives $H^0(Z, R^j f_* \mathcal{F} \otimes A^m) = H^j(X', \mathcal{F} \otimes f^* A^m) = 0$ for $j > 0$. A sheaf generated by global sections with no nonzero global sections is zero, so $R^j f_* \mathcal{F} = 0$ for $j > 0$. Then for every $m \geq m_0$ the spectral sequence collapses to $H^i(Z, f_* \mathcal{F} \otimes A^m) = H^i(X', \mathcal{F} \otimes f^* A^m) = 0$ for $i > 0$.

*Proposition P7.8.17.* Drop the $D_j$ with $a_j = 0$, and induct on the number $r$ of the remaining ones. The statement on a smooth projective scheme of pure dimension $n$ means the statement on each connected component, with the restrictions of $N$ and of the $D_j$, which are again smooth divisors with reduced snc sum. If $r = 0$, then $N$ is ample and the claim is Theorem P7.8.2.

Let $r \geq 1$ and write $a_r = p/q$ with $0 < p < q$. By Proposition P7.8.11 applied to $\mathcal{O}_X(D_r)$ and $D_1 + \dots + D_r$, there is a finite flat surjective $g \colon X' \to X$ from a smooth projective scheme, and a line bundle $L'$ with $L'^q \cong \mathcal{O}_{X'}(g^* D_r)$, such that the $g^* D_j$ are smooth divisors with reduced snc sum. Let $s$ be a section of $L'^q$ with divisor $g^* D_r$, and $h \colon Y \to X'$ the cyclic cover of Proposition P7.8.10, with $h^* g^* D_r = q D'$. Put $f = g \circ h$ and $M = \mathcal{O}_X(N)$.

By part 3 of Lemma P7.8.9 for $g$, with $\mathcal{G} = g_*(\omega_{X'} \otimes g^* M)$, the group $H^i(X, \omega_X \otimes M)$ injects into $H^i(X', \omega_{X'} \otimes g^* M)$. By part 4 of Proposition P7.8.10, $\iota(\omega_{X'}) \subseteq h_*(\omega_Y(-(q-1)D')) \subseteq h_*(\omega_Y(-pD'))$, since $p \leq q - 1$. So part 3 of Lemma P7.8.9 for $h$, with $\mathcal{G} = h_*(\omega_Y \otimes h^* g^* M \otimes \mathcal{O}_Y(-pD'))$, shows that $H^i(X', \omega_{X'} \otimes g^* M)$ injects into $H^i(X', \mathcal{G}) = H^i(Y, \mathcal{O}_Y(K_Y + f^* N - pD'))$, the equality because $h$ is affine (Corollary P4.4.3). It remains to show that this last group vanishes for $i > 0$.

On $Y$ put $N_Y = f^* N - p D'$ and $\Delta_Y = \sum_{j < r} a_j f^* D_j$. Since $f^* D_r = q D'$ and $a_r q = p$,
$$N_Y - \Delta_Y = f^* N - a_r f^* D_r - \sum_{j < r} a_j f^* D_j = f^*(N - \Delta),$$
which is ample by Corollary P7.3.3, applied to a multiple that is Cartier. By part 5 of Proposition P7.8.10 with $\Delta_c = g^* D_c$ for $c < r$, the $f^* D_j$ with $j < r$ are smooth divisors and $D' + \sum_{j < r} f^* D_j$ is reduced snc. So $N_Y$ and $\Delta_Y$ satisfy the hypotheses with $r - 1$ divisors, on each component of $Y$, and the induction hypothesis gives $H^i(Y, \mathcal{O}_Y(K_Y + N_Y)) = 0$ for $i > 0$.

*Theorem P7.8.18.* Put $B = N - \Delta$, a nef and big $\mathbb{Q}$-divisor, and fix $m \geq 1$ with $mB$ Cartier and a very ample divisor $A_0$. Since $mB$ is big, Lemma 1.3.12 gives $m' \geq 1$ and an effective divisor $E_0 \sim m' m B - A_0$. Put $E = E_0 / (m'm)$ and $A_1 = A_0 / (m'm)$, so that $B \sim_{\mathbb{Q}} A_1 + E$, and for rational $0 < \varepsilon \leq 1$,
$$N = B + \Delta \sim_{\mathbb{Q}} A_\varepsilon + \varepsilon E + \Delta, \qquad A_\varepsilon = (1 - \varepsilon) B + \varepsilon A_1,$$
with $A_\varepsilon$ ample by part 3 of Theorem P7.3.12. Let $\mu \colon X' \to X$ and $F$ be as in Theorem P7.8.15 for the divisor $\operatorname{Supp} \Delta + \operatorname{Supp} E$, and $K_{X'/X} = \sum k_E E$. For rational $\varepsilon, \delta > 0$ put
$$G = \mu^* \Delta + \varepsilon \mu^* E + \delta F,$$
an effective $\mathbb{Q}$-divisor whose support lies in $\mu^{-1}_*(\operatorname{Supp} \Delta + \operatorname{Supp} E) + \operatorname{Exc}(\mu)$, so it has snc support. Choose $\varepsilon$ and then $\delta$ small, in this order, so that:

1. every coefficient of $G$ along a non-exceptional prime divisor is less than $1$, which is possible since such a coefficient is $a_j + \varepsilon \operatorname{coeff}(E)$ or $\varepsilon \operatorname{coeff}(E)$, and $a_j < 1$;
2. the coefficient of $G$ along every exceptional prime $E_i$ is less than $k_{E_i} + 1$, which is possible since it is $\operatorname{ord}_{E_i}(\mu^* \Delta) + \varepsilon \operatorname{ord}_{E_i}(\mu^* E) + \delta \operatorname{ord}_{E_i}(F)$ and $\operatorname{ord}_{E_i}(\mu^* \Delta) < k_{E_i} + 1$ by Lemma P7.8.14;
3. $\mu^* A_\varepsilon - \delta F$ is ample, by Theorem P7.8.15.

There are finitely many prime divisors in the support of $G$, so the choices are possible. Put $N' = \mu^* N - \lfloor G \rfloor$, a Cartier divisor, and $\Delta' = \{G\}$, with snc support and coefficients in $[0, 1)$. Then $N' - \Delta' = \mu^* N - G \equiv \mu^* A_\varepsilon - \delta F$ is ample, and for every $m \geq 0$, $(N' + m \mu^* A_0) - \Delta' \equiv \mu^*(A_\varepsilon + m A_0) - \delta F$ is ample as well, by part 3 of Theorem P7.3.12, since $\mu^* A_0$ is nef. Proposition P7.8.17, applied with the prime components of $\operatorname{Supp} \Delta'$ as the $D_j$, gives
$$H^i(X', \mathcal{F} \otimes \mu^* \mathcal{O}(m A_0)) = 0 \quad (i > 0, \ m \geq 0), \qquad \mathcal{F} = \mathcal{O}_{X'}(K_{X'} + N').$$
By Lemma P7.8.16, $R^j \mu_* \mathcal{F} = 0$ for $j > 0$. Now $K_{X'} + N' = \mu^*(K_X + N) + P$ with $P = K_{X'/X} - \lfloor G \rfloor$. By conditions 1 and 2, $P$ is effective and exceptional: along a non-exceptional prime both terms are $0$, and along $E_i$ the coefficient is $k_{E_i} - \lfloor \operatorname{coeff}_{E_i} G \rfloor \geq 0$. An effective exceptional divisor satisfies $\mu_* \mathcal{O}_{X'}(P) = \mathcal{O}_X$: a rational function $\varphi$ with $\operatorname{div}(\varphi) + P \geq 0$ over $\mu^{-1}(U)$ has $\operatorname{div}(\varphi) \geq 0$ on $U$, because $\mu_* P = 0$, so $\varphi$ is regular on $U$ by Corollary P1.8.3, and conversely every regular function is a section since $P \geq 0$. By the projection formula, $\mu_* \mathcal{F} = \mathcal{O}_X(K_X + N)$ and $R^j \mu_* \mathcal{F} = 0$ for $j > 0$, so the Leray spectral sequence gives $H^i(X, \mathcal{O}_X(K_X + N)) = H^i(X', \mathcal{F}) = 0$ for $i > 0$.

*Corollary P7.8.19.* Part 1 is Theorem P7.8.18 with $N = \lceil D \rceil$ and $\Delta = \lceil D \rceil - D$, whose coefficients lie in $[0, 1)$ and whose support is that of $\{D\}$; then $N - \Delta = D$. Part 2 is the case $D = L$ of part 1, with $\{D\} = 0$, together with Corollary P4.7.21 for the second statement.

### Exercises

1. (A) Let $\pi \colon X \to \mathbb{P}^2$ be the blow-up of a point. For which $a, b \in \mathbb{Z}$ is $aH - bE$ nef and big? Check part 2 of Corollary P7.8.19 for $aH - bE = 2H - E$ by computing $\chi(\mathcal{O}_X(-H))$.
2. (A) On $X = \mathbb{P}^1 \times \mathbb{P}^1$ with two fibres $F_1, F_2$ of the first projection and one fibre $G$ of the second, let $D = \frac12(F_1 + F_2) + \frac13 G$. Check the hypotheses of part 1 of Corollary P7.8.19 and verify its conclusion by the Künneth formula.
3. (B) Let $C \subseteq X$ be a smooth prime divisor and $N$ a Cartier divisor with $N - C$ ample. Show that $H^i(X, \mathcal{O}_X(K_X + N)) = 0$ for $i > 0$, using the sequence $0 \to \mathcal{O}_X(K_X + N - C) \to \mathcal{O}_X(K_X + N) \to \omega_C \otimes \mathcal{O}_C(N - C) \to 0$ and Theorem P7.8.2 on $X$ and on $C$. Then show by an example on the blow-up of a point of $\mathbb{P}^2$ that condition 2 in the proof of Theorem P7.8.18 fails when a coefficient $a_j$ equals $1$.
4. (B) Let $D$ be a nef and big $\mathbb{Q}$-divisor on $X$ without the snc assumption on $\{D\}$, and $\mu \colon X' \to X$ a log resolution of $\operatorname{Supp} D$. Show that $H^i(X, \mu_* \mathcal{O}_{X'}(K_{X'} + \lceil \mu^* D \rceil)) = 0$ for $i > 0$.
5. (B) Let $L$ be nef and big on $X$ and $D \in |L|$ a smooth divisor. Deduce from part 2 of Corollary P7.8.19 that $H^0(X, \omega_X \otimes L^2) \to H^0(D, \omega_D \otimes L|_D)$ is surjective, and show by an example that $H^0(X, \omega_X \otimes L) \to H^0(D, \omega_D)$ need not be.
6. (C) Prove Proposition P7.8.17 when $\Delta = \frac{1}{q} D_1$ with $D_1 \in |qL|$ smooth for a line bundle $L$, without Proposition P7.8.11: use the cyclic cover of Proposition P7.8.10 directly and identify the summand of $h_* \omega_Y$ that carries $\omega_X \otimes M$.

### Lean

The project library states two forms of the theorem without proof. `MinimalModel.KawamataViehweg` is the relative klt form of Kollár and Mori, Theorem 2.70: for a proper morphism $f$, a klt pair $(X, \Delta)$ and a $\mathbb{Q}$-Cartier Weil divisor $N$ with $N - (K_X + \Delta)$ nef and big over the base, $R^i f_* \mathcal{O}_X(N) = 0$ for $i > 0$; it is attached to node MM7MQT1KEA. `MinimalModelBridge.KawamataViehwegSNC` states the form of KM98, Theorem 2.64, $H^i(X, \mathcal{O}_X(-B)) = 0$ for $i < n$, and is matched with a theorem of the AxiomMath MMP library; the comparison is not finished. Theorem P7.8.18 is Serre dual to the second and is the absolute snc case of the first; neither deduction is in the library. Mathlib has no coherent cohomology of projective schemes. The handbook adds no `MinimalModel` node here.

### Notes and history

Kawamata (Kaw82) and Viehweg (Vie82) proved the theorem independently in 1982, Kawamata by cyclic covers and Viehweg by cyclic covers and the degeneration of the Hodge to de Rham spectral sequence. The surface case of nef and big line bundles is Ramanujam's (Ram72). The literature state is theorem. The proof above follows Kollár and Mori, Theorems 2.64 and 2.70 (KM98), and Lazarsfeld, Section 4.3 (Laz04), with the covers of Section 8.2 in place of Kawamata's covering lemma. Esnault and Viehweg (EV92) prove more general statements for integral parts of $\mathbb{Q}$-divisors and for logarithmic de Rham complexes. In the minimal model program the theorem is used in its relative form, with $N - (K_X + \Delta)$ nef and big over a base and $(X, \Delta)$ klt, and Chapter 9 deduces the relative form from the absolute one. Multiplier ideals in Chapter 10 package the passage to a log resolution in Theorem P7.8.18 into a single ideal sheaf.
