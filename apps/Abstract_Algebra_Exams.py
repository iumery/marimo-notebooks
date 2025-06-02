import marimo

__generated_with = "0.13.15"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    nav_menu = mo.nav_menu(
        {
            "/index.html": f"{mo.icon('lucide:home')} Home",
        },
        orientation="vertical",
    )
    nav_menu
    return


@app.cell
def _(mo):
    mo.md(r"""# Fall Semester Midterm Exam""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Problem 1

    **Let $\alpha = \sqrt{6+\sqrt{11}}$ and $L = \mathbb{Q}[\alpha]$. The minimal polynomial of $\alpha$ is $p(x) = x^4-12x^2+25$**:

    1. **Explain why the inclusion $\mathbb{Q}[\sqrt{11}] \subset L$ is strict**;
    2. **Show that $\beta = \sqrt{6-\sqrt{11}}$ lies in $L$ and give its expression in the basis $\lbrace 1, \alpha, \alpha^2,\alpha^3\rbrace$**;
    3. **$L$ is Galois over $\mathbb{Q}$. Explain why and determine its Galois group $G$. Is $G$ cyclic**?

    Proof

    1. If not, then there is some $a,b\in \mathbb{Q}$ so that $a+b\sqrt{11} = \sqrt{6+\sqrt{11}}$ so that $a^2+b^2\cdot 11 + 2ab\sqrt{11} = 6+\sqrt{11}$, but those $a, b$ are not rational;
    2. Factor $p(x)$ $= (x-\sqrt{6+\sqrt{11}})(x-\sqrt{6-\sqrt{11}})$ $(x+\sqrt{6+\sqrt{11}})(x+\sqrt{6-\sqrt{11}})$, result follows. We may calculate $\alpha \beta = 5 \implies \beta = 5\alpha^{-1}$, now use $\alpha^4-12\alpha^2+25 = 0$ $\implies \alpha(\alpha^3-12\alpha) = -25$ $\implies \alpha^{-1} = (-\alpha^3+12\alpha)/25$, plugin and get the expression.
    3. Because it is the splitting field of a rational polynomial in $\mathbb{Q}$. The group is $C_2^2$.

    ## Problem 2

    **Let $\alpha = 2^{1/4}$. Claim: There exists $n$ such that $\alpha$ belongs to the cyclotomic field $\mathbb{Q}_n$. Is this claim true or false? Either produce some appropriate $n$ or disprove its existence**.

    Proof

    We know Galois group of $\mathbb{Q} \subset \mathbb{Q}_n$ is abelian, in particular every subgroup of the Galois group is a normal subgroup and the corresponding intermediate field extension is normal. If $\alpha \in \mathbb{Q}_n$ then $\mathbb{Q}(\alpha)$ should be a normal extension of $\mathbb{Q}$, but it is not: $x^4-2$ does not split in $\mathbb{Q}(\alpha)$ (because we will need the complex numbers).

    ## Problem 3

    **Let $E = \mathbb{Q}_f$ be the splitting field of $f(x) = x^7-5 \in \mathbb{Q}[x]$. Then $E$ is a composite of two simple extensions $L_1 = \mathbb{Q}(5^{1/7})$ and $L_2 = \_\_\_\_\_$**?

    1. **Determine $[E: \mathbb{Q}]$ without using Galois theory**;
    2. **Determine the Galois group $G=G_f$. What subgroups of $G$ correspond to $L_1$ and $L_2$? Is $G$ solvable**?

    Proof

    1. $L_2 = \mathbb{Q}(e^{2\pi i/7})$ $=\mathbb{Q}_7$ is a degree $6$ extension, and $L_1$ is a degree $7$ extension. Since $6,7$ are coprime, we know the composition is a degree $6\cdot 7 = 42$ extension;
    2. $L_2$ corresponds to a subgroup $C_7$ and it should be a normal subgroup because the extension is normal; $L_1$ corresponds to a subgroup $C_6$ and it is not a normal subgroup. $G_f = C_7 \rtimes C_6 (= F_7)$.

    ## Problem 4

    **Explain why the regular $65$-gon is not constructible**.

    Proof

    If it is, then regular $13$-gon should be constructible, which happens if and only if $\cos(2\pi/13)$ is constructible, but $[\mathbb{Q}(\cos(2\pi/13)):\mathbb{Q}]$ is a degree $6$ extension: this degree should be half of $[\mathbb{Q}(e^{2\pi i /13}):\mathbb{Q}] = [\mathbb{Q}_{13}:\mathbb{Q}] = 12$. Since $6$ has a factor that is not $2$, $13$-gon is not constructible.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Spring Semester Midterm Practice""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 1

    **Let $R$ be a ring with $1$, $M$ be an $R$-module, consider an ascending chain** $$M_1 \subsetneq M_2 \subsetneq \dots$$ **of submodules of $M$, prove the union is a submodule of $M$**.

    Proof

    Call the union $U$, we need to show:

    1. $x + y \in U$ whenever $x, y \in U$ so that it maintains a group structure;
    2. $rx \in U$ whenever $x \in U$ and $r \in R$.

    For 1: if $x , y \in U$ then $x \in M_n, y \in M_m$ for some $n, m$, WLOG $m \ge n$ then $x ,y \in M_m$, then $x + y \in M_m \subseteq U$. For $2$, $x \in M_n$ for some $n$, which has a submodule structure.

    ## Exercise 2

    **If $M$ is a finite abelian group then it is naturally a $\mathbb{Z}$-module, can the action on $M$ be extended so that $M$ is a $\mathbb{Q}$-module**?

    Proof

    The answer is no, and we prove by a counter-example. Suppose $M = \mathbb{Z}_2$ and the action on $M$ is extended to $\mathbb{Q}$, then in particular for any $x \in M$, we must have $\frac{1}{2} \cdot x = y \in M$. But then $$x = 1 \cdot x = 2 \cdot \frac{1}{2} \cdot x = 2\cdot y = 0.$$

    ## Exercise 3

    **Let $M$ be an $R$-module, then**:

    1. **$0m = 0$ for all $m \in M$**;
    2. **$r0 = 0$ for all $r \in R$**;
    3. **$(-1)m = -m$ for all $m$**;
    4. **If $rm = 0$ for some $r \in R$ and non-zero $m \in M$, then $r$ does not have a left inverse**.

    Proof

    1. $0m = (0+0)m = 0m + 0m \implies 0 = 0m$;
    2. $r0 = r(0+0) = r0 + r0 \implies 0 = r0$;
    3. $m + (-1)m = 1m + (-1)m = 0m = 0 \implies (-1)m = -m$;
    4. Suppose $sr = 1$ for some $s \in R$. $s(rm) = s0 = 0$, but LHS also $= (sr)m = 1m = m$, contradicts assumption.

    ## Exercise 4

    1. **Let $R$ be a commutative ring viewed as an $R$-module, then any two distinct elements of $R$ are linearly dependent**;
    2. **Let $f: M \to N$ be an $R$-module homomorphism, let $\lbrace x_1, \dots, x_n \rbrace$ be a subset in $M$. Prove that if $\lbrace f(x_1), \dots, f(x_n) \rbrace$ is linearly independent, then the set $\lbrace x_1,\dots, x_n \rbrace$ is linearly independent**.

    Proof

    1. If $x \ne y \in R$, consider $$(-y)\cdot x + x \cdot y = 0,$$ which can be viewed as linear combination of $x$ and $y$. Since $x \ne y$, at least one of them is non-zero, which implies dependence;
    2. Suppose $r_1x_1 + \dots + r_n x_n = 0$, then $$\begin{aligned} 0 & = f(0)\\&=f(r_1x_1 + \dots + r_nx_n) \\ &=r_1f(x_1)+ \dots + r_nf(x_n) \end{aligned}$$ thus $r_1 = \dots = r_n = 0$ because $\lbrace f(x_1), \dots, f(x_n) \rbrace$ are linearly independent.

    ## Exercise 5

    **An $R$-module $M$ is simple if and only if $M$ is isomorphic to $R/I$ where $I$ is a maximal ideal of $R$ as an $R$-module**.

    Proof

    Suppose $I$ is maximal then $R/I$ is a field, and a field only has two ideals, namely $0$ and itself, so the only ideal of $R/I$ are $0$ and $R/I$, which means the only submodule of $M$ is $0$ and $M$, which means $M$ is simple.

    Suppose $M$ is simple. By definition $M$ is not trivial, i.e. there exists some non-zero $m \in M$. Consider $(m)$ the cyclic module generated by $m$. Since $M$ is simple we must have $M = (m) = Rm$. Define a map $\varphi: R \to M$ by $r \mapsto rm$, then $\varphi$ is an $R$-module homomorphism and it is surjective, thus $M \cong R/I$ where $I = \ker{f}$. We need to show $I$ is a maximal ideal. Suppose $I \subseteq J \subseteq R$, then by isomorphism theorem, $J/I$ is an ideal of $R/I \cong M$, thus $J/I$ is a submodule. Since $M$ is simple, $J/I = 0$ or $J/I = M$, but this means $J = 0$ or $J = R$, which proves maximality of $I$.

    ## Exercise 6

    **Determine the characters of dihedral group** $$D_{2n} = \langle r,s | s^2 = r^n = 1, srs = r^{-1} \rangle.$$

    Solution

    1. If $n$ is even. There are four obvious representation sending $r, s$ to $\pm 1$, they corresponds to four linear characters. Now let $w = e^{2 i \pi/n}$ and $h \in \mathbb{Z}$, we may define $\rho(r) = \begin{pmatrix} w^h&0\\0&w^{-h} \end{pmatrix}$ and $\rho(s) = \begin{pmatrix} 0&1\\1&0 \end{pmatrix}$, there are $\frac{n}{2}-1$ of such representation and it's not too hard to check they are distinct irreducible dimension $2$ characters. Since $| D_{2n} | = 2n = 4 + (\frac{n}{2}-1)\cdot 4$, we are done;
    2. If $n$ is odd, we have two linear character sending $s$ to $\pm 1$ but $r$ to $1$, and there are $\frac{n-1}{2}$ of above $\rho$'s, dimension match, and again we are done.

    ## Exercise 7

    **Let $N$ be a normal subgroup of finite group $G$, show that** $$| C_{G/N}(xN) | \le | C_G(x) |.$$

    Proof

    If $g$ is in the conjugacy class of $x$, i.e. $g = kxk^{-1}$, then $gN$ is in conjugacy class of $xN$, i.e. $| \text{Cl}(x) | \le | N \| \text{Cl}(xN) |$. So $$| G |/| \text{Cl}(x) | \ge | G | / (| N \| \text{Cl}(xN) |)$$ which by orbit-stabilizer theorem is the same as $$| C_{G/N}(xN) | \le | C_G(x) |.$$

    ## Exercise 8

    **See character table as a matrix, what is its determinant**?

    Solution

    Call the matrix $A$ and we have $(A)_{ij} = \chi_i(g_j)$. Let $A^H$ be the conjugate transpose, call $B = A^H A$, then $$(B)_{ij} = \sum_k A_{ik}^HA_{kj} = \sum_k \overline{A_{ki}}A_{kj} = \sum_k \overline{\chi_k(g_i)}\chi_k(g_j) = | C_G(g_j)| \delta_{ij}$$ by the (second) orthogonality relation, so $\det{B} = \prod_j | C_G(g_j) |$ $=\det{A^H}\det{A}$. Consider the permutation map on conjugacy classes $[g] \mapsto [g^{-1}]$, it's a composition of flips and fixes conjugacy classes invariant under taking inverse, take $\tilde{A}$ be the matrix got from $A$ under this map, since $\chi(g^{-1}) = \overline{\chi(g)}$, we get $A^H = \tilde{A}^T$, so $\det{A^H} = (-1)^l\det{A}$ if $l$ is the number of flips. So $(-1)^l(\det{A})^2 = \det{B}$ thus $$\det{A} = \pm i^l \sqrt{\prod_j | C_G(g_j) |}.$$

    ## Exercise 9

    **Sum of elements in any row of character table is a non-negative integer**.

    Proof

    Let $\chi$ be an irreducible character, and let $\chi'$ be a character, by definition we get $$\langle \chi, \chi' \rangle = \frac{1}{| G |}\sum_g \chi(g) \overline{\chi'(g)} = \sum_i \frac{1}{C_i}\chi(g_i)\overline{\chi'(g_i)}$$ with our usual notation. We want to find some particular character $\chi'$ such that $\chi'(g_i) = C_i$ then we are done. Let $G$ act on $G$ by conjugation $g(x) = gxg^{-1}$, then regard it as the permutation representation of $G$ we get (call the character $\chi'$) (i.e. we count fixed points) $$\chi'(g_i) = tr(\rho(g_i)) = | \lbrace x \in X: x = g_i(x) = g_ixg_i^{-1} \rbrace | = | G_{g_i} |$$ where $G_{g_i}$ is the stabilizer of $g_i$ under conjugation, which by orbit-stabilizer theorem $| G_{g_i} | =  C_i$, and we are done.

    ## Exercise 10

    **Irreducible characters are linearly independent**.

    Proof

    Decompose $\mathbb{C}G = M_{f_1}(\mathbb{C}) \oplus \dots \oplus M_{f_r}(\mathbb{C})$ and decompose $I = e_1 + \dots + e_r$, then $\chi_i(e_i) = f_i$ and $\chi_j(e_i) = 0$ if $i \ne j$. If $\lambda_1,\dots, \lambda_r \in \mathbb{C}$ so that $\sum \lambda_i \chi_i = 0$, then $0 = \sum \lambda_i \chi_i(e_j) = \lambda_j f_j$ for each $j$ so $\lambda_j = 0$ for each $j$.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Spring Semester Midterm Exam""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Problem 1

    **Let $G$ be a finite group and $\rho: G \to GL(2,\mathbb{C})$ be a representation of $G$. Suppose that there are elements $g, h \in G$ such that $\rho(g)$ and $\rho(h)$ do not commute, show that $\rho$ is irreducible**.

    Proof

    Two diagonalized matrices always commute, thus $\rho(g)$ and $\rho(h)$ do not commute implies they are not simultaneously diagonalizable, thus $\rho$ is irreducible.

    ## Problem 2

    **Let $V$ be non-trivial $\mathbb{C}G$-module and $\chi = \chi_V$ be the corresponding character of $G$. Suppose $\chi(g) \ge 0$ for all $g \in G$. Prove that $V$ is reducible**.

    Proof

    Consider $(\chi, \chi_1)$ where $\chi_1$ is the trivial character and suppose $V$ is irreducible, then by the orthonormal relation either $(\chi,\chi_1) = 0$ (this won't happen because $\chi_1 \equiv 1$ and $\chi(1) > 0$, $\chi(g) \ge 0$ for other $g \in G$ thus $(\chi,\chi_1)>0$) or $\chi = \chi_1$ (not the case by assumption). Since both are not the case, we have a contradiction.

    ## Problem 3

    **Let $G = F_{5,4}$ where $F_{5,4} = \langle a,b | a^5 = b^4 = 1, b^{-1}ab = a^2 \rangle$. Then its commutator subgroup $G' =$**?

    1. **Describe the conjugacy classes of $G$ and construct its character table**;
    2. **Realize $G$ as a subgroup of $S_5$. What is the character of the corresponding permutation representation, and how does it decompose into irreducible characters**?

    Solution

    By definition of commutator subgroup, it must contain $a^{-1}b^{-1}ab = a$. Since $G/\langle a \rangle = C_4$ is abelian, the commutator subgroup must be $\langle a \rangle = C_5$ and no larger.

    $1$ is in its only conjugacy class. $a , a^2, a^4, a^8 = a^3$ are in a conjugacy class (each time by $b$). There are $3$ other classes, with representatives $b, b^2, b^3$ respectively. There are $4$ relatively obvious character/irreducible representations, namely sending $a$ to $1$ and $b$ to the four forth roots of unity. Since there are $5$ conjugacy classes, there are $5$ irreducible characters, from dimension the last one has $\chi_5(1) = 4$, and we can use orthonormal relations to get the rest: $$\begin{array}{|c|c|c|c|c|c|} \hline & 1&a&b&b^2&b^3\\\hline C_i & 20 & 5 & 4 & 4 &4 \\\hline \chi_1 & 1 & 1 & 1 & 1 & 1 \\\hline \chi_2 & 1 & 1 & -1 & 1 & -1 \\\hline \chi_3 & 1 & 1 & i & -1 & -i \\\hline \chi_4 & 1 & 1 & -i & -1 & i \\\hline \chi_5 & 4 & -1 & 0 & 0 & 0 \\\hline\end{array}$$ For the second part, first we need to realize $G$ as a subgroup of $S_5$, i.e. we need to find permutations $a, b$ satisfies the relators. $a = (12345)$ is easy; calculate $a^2 = (13524)$ then we can see $b = (2354)$ fits that $(4532)(12345)(2354) = (13524)$. Now the character of permutation representation is easy to calculate, we just need to count fixed points, i.e. elements not appear in the permutation. So $\chi_G = (5, 0,1,1,1)$. It's not hard to see $\chi_G = \chi_1 + \chi_5$ in the above table.

    ## Problem 4

    1. **Let $G$ be a non-abelian group of order $16$. Show that $G$ has either $7$ or $10$ conjugacy classes**;
    2. **Let $G = \langle a,b | a^8 = b^2 = 1, b^{-1}ab = a^3 \rangle$. Note that $Z(G) = \lbrace 1, a^4 \rbrace$ and $G/Z(G) \cong D_4$. $G$ has $7$ conjugacy classes with representative $1, a^4, a^2, a, a^{-1}, b$ and $ab$ respectively. Construct the character table of $G$**.

    Proof

    $G$ is not abelian, so there must be some conjugacy class with elements not $1$. By properties of character, we know the order of each conjugacy class can be only $1$ or $2$. Thus there are three choices:

    1. $12$ classes of $1$ element, $1$ class of $2$ elements;
    2. $8$ classes of $1$ element, $2$ classes of $2$ elements;
    3. $4$ classes of $1$ element, $3$ classes of $2$ elements.

    Since an element is in the center of a group if and only if it has singleton conjugacy class, and that center is always a subgroup, option 1 is not really viable because $12 \nmid 16$. Thus we have the other two choices, which leaves with $10$ or $7$ conjugacy classes.

    Start with basic information: $$\begin{array}{|c|c|c|c|c|c|c|c|} \hline & 1&a^4&a^2&a&a^{-1}&b&ab\\\hline C_i & 16 & 16 & 8 & 8 & 8 & 4 & 4\\\hline \chi_1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \\\hline \chi_2 & 1 &  &  &  &  &  &  \\\hline \chi_3 & 1 &  &  &  &  &  &  \\\hline \chi_4 & 1 &  &  &  &  &  &  \\\hline \chi_5 & 2 &  &  &  &  &  &  \\\hline \chi_6 & 2 &  &  &  &  &  &  \\\hline \chi_7 & 2 &  &  &  &  &  &  \\\hline\end{array}$$ The four linear ones are easy to get, $b^2 = 1 \implies b = \pm 1$, so that $a$ is $8$-th root of $1$ such that $a = a^3$, so $a= \pm 1$ also, so we can fill in the others. For the other $3$, realize $b = \begin{pmatrix} 0 & 1 \\ 1& 0 \end{pmatrix}$ and $a$ is of form $\begin{pmatrix} e^{2 k \pi i/8} & 0 \\ 0 & e^{2 l \pi i /8} \end{pmatrix}$ such that $3k \equiv l \pmod{8}$ and $3l \equiv k \pmod{8}$ would give $3$ irreducible representations (because $a, b$ are not simultaneously diagonalizable). So we can have $k = 1, l = 3$; $k = 2, l = 6$; $k = 5, l = 7$ (the others are isomorphic to these three, because they have the same trace), do some calculations and we fill the rest of the table. $$\begin{array}{|c|c|c|c|c|c|c|c|} \hline & 1& a^4 &a^2 &a &a^{-1} & b &ab\\\hline C_i & 16 & 16 & 8 & 8 & 8 & 4 & 4\\\hline \chi_1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \\\hline \chi_2 & 1 & 1 & 1 & -1 & -1 & 1 & -1 \\\hline \chi_3 & 1 & 1 & 1 & 1 & 1 & -1 & -1 \\\hline \chi_4 & 1 & 1 & 1 & -1 & -1 & -1 & 1 \\\hline \chi_5 & 2 & 2 & -2 & 0 & 0 & 0 & 0 \\\hline \chi_6 & 2 & -2 & 0 & \sqrt{2}i & -\sqrt{2}i & 0 & 0 \\\hline \chi_7 & 2 & -2 & 0 & -\sqrt{2}i & \sqrt{2}i & 0 & 0 \\\hline\end{array}$$
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Spring Semester Final Exam""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Problem 1

    **A subring $R$ of a field $K$ is said to be a valuation ring if for each $x \in K^{*}$, we have either $x \in R$ or $x^{-1} \in R$ or both. Show that a valuation ring $R$ is local and integrally closed**.

    Proof

    It suffice to show the set of non-unit elements in $R$ form an ideal (so it is the unique maximal ideal). Denote this set be $M = \lbrace x \in R | x^{-1} \notin R \rbrace$. We need to show $a, b \in M$ implies $a+b, ab \in M$. If either of $a, b$ is zero, this is obviously true, so suppose both of them are not zero.

    Since $a,b \in K$, $\frac{a}{b}, \frac{b}{a} \in K^{*}$, thus either of them is in $R$. If $\frac{a}{b} \in R$, then we can write $a+b = (1+\frac{a}{b})b$. Suppose $a+b \notin M$, then $(a+b)^{-1} \in R$, then $b^{-1} = (1+\frac{a}{b})(a+b)^{-1} \in R$ implies $b \notin M$, which is a contradiction. Similar if $\frac{b}{a} \in R$.

    Now suppose $ab \notin M$, then $(ab)^{-1} \in R$, then $(ab)^{-1}ab = 1$ implies $b^{-1} = (ab)^{-1}a \in R$ so $b \notin M$ so again we have a contradiction.

    Thus $R$ is local.

    Suppose now $\alpha \in K$ is integral over $R$, we need to show $\alpha \in R$. Being integral over $R$ means that $f(\alpha) = \alpha^n + r_{n-1}\alpha^{n-1} + \dots + r_0 = 0$ for $r_i \in R$. If $\alpha = 0$ then $\alpha \in R$, so we can assume $\alpha \ne 0$ thus by assumption either $\alpha$ or $\alpha^{-1} \in R$. If $\alpha \in R$ then we are done. So suppose $\alpha^{-1} \in R$. Then times $\alpha^{-n+1}$ to the polynomial, we get $\alpha + \frac{r_{n-1}}{\alpha} + \dots + \frac{r_0}{\alpha^{n-1}} = 0$, but then $\alpha = -(\frac{r_{n-1}}{\alpha} + \dots + \frac{r_0}{\alpha^{n-1}}) \in R$ so $\alpha \in R$ anyway.

    ## Problem 2

    **Let $\alpha$ be a real root of $f(x) = x^3-x+4 \in \mathbb{Z}[x]$ ($D(f) = -428$). Consider $K = \mathbb{Q}[\alpha]$ and $R = \mathbb{Z}[\alpha]$. Explain why $R$ is not Dedekind and exhibit a non-invertible ideal of $R$. What is the integral basis of $K$ and what is the discriminant $\Delta_K$**?

    Proof

    Since $D(f) = -2^2\cdot 107$ thus possible ramified primes are $2$ or $107$. Factor $f$ over $\mathbb{F}_2$ we have $\overline{f} = x^3-x = x(x^2-1) = x(x-1)^2$. The remainder of $f$ divided by $(x-1)$ is $1-1+4 = 4 \equiv 0 \pmod{4}$ thus $2$ is a singular prime, thus $R$ is not Dedekind. By Kummer-Dedekind Theorem, $(2, \alpha - 1)$ is a non-invertible ideal of $R$. $107$ is regular because it is larger than Minkowski's bound.

    Now write $f = (x-1)(x^2+x)+4$. Since $\alpha$ is a root of $f$, $(\alpha - 1)(\alpha^2 + \alpha) + 4 = 0$. If we take $\beta = \frac{-(\alpha^2+ \alpha)}{2} \notin R$ so that $\frac{2}{\beta} = \alpha - 1$, then the minimal polynomial for $\beta$ is $x^3-x^2+3x - 2 = 0$. It is not hard to check $2$ is not a singular prime for $\mathbb{Z}[\beta]$. Thus $O_K = \mathbb{Z} + \mathbb{Z}[\alpha] + \mathbb{Z}[\beta]$.

    The discriminant can be calculated to be $| \det(T: O_K \to \mathbb{Z}^3) |$ where the transformation is given by the inverse of $\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & -\frac{1}{2} \\ 0 & 0 & -\frac{1}{2}\end{pmatrix}$ thus $\Delta_K = 2$.

    ## Problem 3

    **Let $K = \mathbb{Q}[\sqrt{-103}]$ and $R = O_K = \mathbb{Z}[?]$ be the maximal order in $K$. Find the class group $\text{Cl}(K)$**.

    Solution

    Since $-103 \equiv 1 \pmod{4}$, we know that $O_K = \mathbb{Z}[\frac{1+\sqrt{-103}}{2}]$. $R$ is realized by the polynomial $f = x^2 - x + 26$. The Minkowski's bound in this case is $M_R = (\frac{4}{\pi})^3 \frac{2!}{2^2}\sqrt{103} < 7$, thus the possible generators of the class group has norm $2,3$ or $5$. Calculate $N(c-\alpha) = f(c)$, we have that $f(c) = 2^5$ when $c = -2$. Also check $\overline{f}$ in $\mathbb{F}_{2,3,5}$, it is not hard to get $(2) = (2,\alpha)(2,\alpha-1)$ and both $3,5$ are inert. So $\text{Cl}(K) = \text{Cl}(R)$ is cyclic group $C_5$.

    ## Problem 4

    **Let $S$ be a Dedekind domain, $I, J$ be two non-zero fractional ideals of $S$. We write $I | J$ if there exists an integral ideal $L \subset S$ such that $J = IL$. Prove that $I | J$ if and only if $I \supseteq J$**.

    Proof

    ($\implies$) Suppose $I | J$, then $J = IL$ for some $L \in S$. Then for any $j \in J$, $j = i\cdot s \in I$ by definition of ideal;

    ($\impliedby$) Suppose now $I \supseteq J$. Since $S$ is Dedekind, any fractional ideal is invertible, thus we can write $S = II^{-1} = JJ^{-1}$, thus $J = II^{-1}J$. Since $J \subseteq I$, $I^{-1}J \subseteq II^{-1} = S$ thus $I^{-1}J$ is an integral ideal, and we are done.

    """
    )
    return


if __name__ == "__main__":
    app.run()
