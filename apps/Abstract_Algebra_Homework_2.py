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
    mo.md(r"""# Fall Semester Homework 1""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 1

    **Consider the irreducible (why?) polynomial $f(X) = X^3+2X+2$ over $\mathbb{Q}$, and let $\alpha$ denote one of its roots**.

    1. **Express the element $\alpha^{-1}$ and $\beta = \alpha^6 + 3\alpha^4+2\alpha^3+6\alpha$ as linear combinations of $1, \alpha, \alpha^2$**;
    2. **Determine the minimal polynomial of $\beta$ over $\mathbb{Q}$**.

    Solution

    To see $f$ is irreducible, since its degree is only $3$ and it is monic we can just check if it has integer root, and there is no any such root.

    Since $\alpha$ is a root of $f$, $\alpha^3 + 2\alpha + 2 = 0$ $\implies \alpha^3 + 2 \alpha = -2$ $\implies \alpha(\alpha^2+2) = -2$, thus we may write $\alpha^{-1} = -\frac{1}{2}(\alpha^2+2)$ $=-1-\frac{1}{2}\alpha^2$.

    For $\beta$, factorize it as $\beta = \alpha(\alpha^2+3)(\alpha^3+2)$, notice from $\alpha^3 + 2\alpha + 2 = 0$ that the third part equals $-2\alpha$, so $\beta = \alpha(\alpha^2+3)(-2\alpha)$. Combine the first two terms to get $\alpha^3+3\alpha$ and notice it equals $\alpha-2$, thus $\beta = (\alpha-2)(-2\alpha)$ $=4\alpha-2\alpha^2$.

    Use the result above $\beta = 4\alpha - 2\alpha^2$, since the minimal polynomial of $\alpha$ is $f$ (because it is irreducible), the degree of the minimal polynomial of $\beta$ is at least $3$. So rise $\beta$ to the power $3$ first, and we get $-8\alpha^6+48\alpha^5-96\alpha^4+64\alpha^3$. Now use $\alpha^3 + 2\alpha + 2 = 0$ to decrease the degree of $f$, for example $-8\alpha^6-16\alpha^4 = \alpha^3(-8\alpha^3-16\alpha)= 16\alpha^3$ so $\beta^2 = 48\alpha^5-80\alpha^4+64\alpha^3+16\alpha^3$, now move to $\alpha^5$ and so on.

    We would get $\beta^3 = 32\alpha^4-128\alpha^3+128\alpha^2-224$ $=8\beta^2-224$, so $\beta$ is a root of $X^3-8X^2+224$. This polynomial also does not have integer root so it is irreducible, thus it is the minimal polynomial of $\beta$.

    ## Exercise 2

    **Prove that if $[F(\alpha):F]$ is odd, then $F(\alpha) = F(\alpha^2)$**.

    Proof

    Clearly $F(\alpha^2) \subseteq F(\alpha)$. Suppose the inclusion is strict so that $F \subseteq F(\alpha^2) \subset F(\alpha)$, we have that $[F(\alpha):F] = [F(\alpha):F(\alpha^2)][F(\alpha^2):F]$.

    In particular we have that:

    1. $[F(\alpha):F(\alpha^2)] > 1$ because they are (assumed) not equal;
    2. $[F(\alpha):F(\alpha^2)]$ is odd because only odd times odd get odd;

    1 and 2 implies that in particular $[F(\alpha):F(\alpha^2)]$ is at least $3$.

    However the polynomial $x^2-\alpha^2$ is a polynomial in $F(\alpha^2)[x]$ with $\alpha$ be a root, so $[F(\alpha):F(\alpha^2)]$ is at most $2$, so we have a contradiction.

    ## Exercise 3

    **Let $\alpha = 1+2^{1/3}+4^{1/3}$, what is the degree of $\alpha$ over $\mathbb{Q}$? Produce the minimal polynomial for $\alpha$**.

    Solution

    The minimal polynomial clearly at least needs to be degree $3$. Let's write down $\alpha^3,\alpha^2,\alpha^1$:

    1. $\alpha^3 = 12\cdot 2^{2/3} + 15 \cdot 2^{1/3} + 19$;
    2. $\alpha^2 = 3\cdot 2^{2/3}+4\cdot 2^{1/3}+5$;
    3. $\alpha^1 = 1\cdot 2^{2/3} + 1\cdot 2^{1/3} +1$.

    So we are basically solving a linear system and it's not hard to see $\alpha^3 - 3\alpha^2 - 3\alpha -1 = 0$, it is the minimal polynomial because it is irreducible, and thus the degree is $3$.

    ## Exercise 4

    **Let $\alpha = e^{2\pi i/7}$ and $\zeta = \alpha + \alpha^{-1}$. Use the minimal polynomial for $\alpha$ to write down the minimal polynomial for $\zeta$ over $\mathbb{Q}$. Conclude that the regular heptagon is not constructible**.

    Solution

    $(e^{2\pi i/7})^7 - 1 = 0$ but we can factor $x^7-1$ $= (x-1)(x^6+x^5+x^4+x^3+x^2+x+1)$ (given $\alpha \ne 1$). So if $f(x) = (x^6+x^5+x^4+x^3+x^2+x+1)$ is irreducible then this is the minimal polynomial of $\alpha$. Consider $g(x) = f(x+1) = x^6+7x^5+21x^4+35x^3+35x^2+21x+7$ is irreducible by Eisenstein, so $f$ is also irreducible.

    Since $\alpha^{-1}$ and $\alpha$ are conjugate, they are both root of $f$, i.e. the minimal polynomial of them are both $f$.

    So we have $\alpha^6+\alpha^5+\alpha^4+\alpha^3+\alpha^2+\alpha^1+1 = 0$ $=\alpha^{-6}+\alpha^{-5}+\alpha^{-4}+\alpha^{-3}+\alpha^{-2}+\alpha^{-1}+1$, so the sum of everything is also $0$. We may see $\alpha^6+\alpha^5+\alpha^4+\alpha^3+\alpha^2+\alpha^1+1 + \alpha^{-6}+\alpha^{-5}+\alpha^{-4}+\alpha^{-3}+\alpha^{-2}+\alpha^{-1}+1$ as a polynomial of $x = \alpha+\alpha^{-1}$, we can write it as $x^6+x^5-5x^4-4x^3+6x^2+3x = x(x^2-3)(x^3+x^2-2x-1)$, and we can see that this part $x^3+x^2-2x-1$ is the minimal polynomial of $\zeta$ (because $\zeta$ is not a root of $x$ nor a root of $x^2-3$), which means it has degree $3$.

    Now since $\alpha$ and $\alpha^{-1}$ are conjugate, $\zeta = 2\cos(2\pi/7)$, which means $\zeta$ is constructible if and only if the regular heptagon is constructible, and since the degree of $\zeta$ is odd, we conclude the regular heptagon is not constructible.

    ## Exercise 5

    **Consider the factorization of the quartic**: $$x^4 + px^2 + qx + r = (x^2+ax+b)(x^2-ax+d).$$

    1. **Determine $b$ and $d$ in terms of $p,q,a$. Rewrite the identity $bd = r$ to obtain a cubic equation for $s = a^2$ (Descartes' method for the quartic)**;
    2. **Let $\alpha \in \mathbb{C}$ be a complex number of degree $4$ over $\mathbb{Q}$, and let $f(X) = X^4+pX^2+qX+r$ be its minimal polynomial over $\mathbb{Q}$. Show that there exists a quadratic extension $L$ of $\mathbb{Q}$, contained in $\mathbb{Q}(\alpha)$, if and only if the polynomial** $$R(X) = X^3+2pX^2+(p^2-4r)X-q^2$$**has a rational root**;
    3. **Show that a real root of $X^4 + 2X-2$ is not constructible**.

    Solution

    1. Expand RHS and we get $\begin{cases}d+b-a^2 = p\\ad-ab = q\end{cases}$, and we may get $d = \frac{p+a^2+q/a}{2}$, $b = \frac{p+a^2-q/a}{2}$.
    	So we may write $r= \frac{p+a^2+q/a}{2}\frac{p+a^2-q/a}{2}$ $= \frac{a^6+2a^4p+a^2p^2-q^2}{4a^2}$, and we may get $s^3+2ps^2+(p^2-4r)s-q^2=0$ if we substitute $s = a^2$;
    2. If such $L$ exists, then $[\mathbb{Q}(\alpha):\mathbb{Q}] = [\mathbb{Q}(\alpha):L][L:\mathbb{Q}]$ implies that $[\mathbb{Q}(\alpha):L] = 2$. So some quadratic equation in $L[x]$ has $\alpha$ as root, so $f$ must be able to factorize as $(x^2+ax+b)(x^2-ax+d)$. WLOG say $\alpha$ is a root of $(x^2+ax+b)$ with $a,b \in L$, then $d \in L$. Since $L$ is quadratic extension, $a$ is of the form $m+n\sqrt{k}, k \in \mathbb{Q}$. If $a = \sqrt{k}$ then $s = a^2$ is a rational solution for $R(X)$; otherwise $m-n\sqrt{k}$ is another solution for $R(X)$, but then the third root must be rational otherwise $R(X)$ will not be a rational polynomial.
    	Conversely if $R(X)$ has a rational root, then by part 1, $f$ can be factorized as $(x^2+ax+b)(x^2-ax+d)$. Since $s = a^2$ is rational, $L = \mathbb{Q}(a)$ is then a quadratic extension of $\mathbb{Q}$ we want;
    3. See it as a polynomial $f = X^4+pX^2+qX+r$ then $p = 0, q = 2, r = -2$. The polynomial $R(X) = X^3+2pX^2+(p^2-4r)X-q^2 = x^3+8x-4$ does not have rational (integer) root, so by part 2, for any (real) root $a$ of $X^4 + 2X-2$ there is no quadratic extension $L\subset \mathbb{Q}(a)$, in particular it cannot be of the form $\mathbb{Q}(\sqrt{a_1},\sqrt{a_2}), a_2 \in \mathbb{Q}(\sqrt{a_1})$ (otherwise $L$ is such an $L$), but this means $a$ is not constructible.

    ## Exercise 6

    **Determine all the distinct subfields of $\mathbb{C}$ that are $\mathbb{Q}$-isomorphic to**:

    1. $\mathbb{Q}(\sqrt[3]{15})$;
    2. $\mathbb{Q}(\sqrt[5]{3})$;
    3. $\mathbb{Q}(\sqrt[6]{3})$;

    Solution

    Start with the first one, the minimal polynomial of $\sqrt[3]{15}$ is $x^3-15$ and it has two other roots $\sqrt[3]{15}e^{2\pi i/3}$ and $\sqrt[3]{15}e^{4\pi i/3}$, so the candidates for the field that is $\mathbb{Q}$-isomorphic to $A = \mathbb{Q}(\sqrt[3]{15})$ are $B = \mathbb{Q}(\sqrt[3]{15}e^{2\pi i/3})$ and $C = \mathbb{Q}(\sqrt[3]{15}e^{4\pi i/3})$.

    First, $B$ and $C$ certainly not equal to $A$ because they contain complex numbers while $A$ not. If say $B = C$, then $B$ also contains $e^{2\pi i/3}$, so it also contains $\sqrt[3]{15}$, so we must have $A \subset B$, thus by the Tower Rule we have $3 = [B:\mathbb{Q}]$ $= [B:A][A:\mathbb{Q}]$ where $[A:\mathbb{Q}] = 3$, so $[B:A] = 1$, but that means $B = A$ which as argued cannot be true.

    So the distinct subfields of $\mathbb{C}$ that are $\mathbb{Q}$-isomorphic to $\mathbb{Q}(\sqrt[3]{15})$ are $\mathbb{Q}(\sqrt[3]{15}e^{2\pi i/3})$ and $\mathbb{Q}(\sqrt[3]{15}e^{4\pi i/3})$.

    Now by a very similar argument the distinct subfields of $\mathbb{C}$ that are $\mathbb{Q}$-isomorphic to $\mathbb{Q}(\sqrt[5]{3})$ are:

    1. $\mathbb{Q}(\sqrt[5]{3}e^{2\pi i/5})$;
    2. $\mathbb{Q}(\sqrt[5]{3}e^{4\pi i/5})$;
    3. $\mathbb{Q}(\sqrt[5]{3}e^{6\pi i/5})$;
    4. $\mathbb{Q}(\sqrt[5]{3}e^{8\pi i/5})$.

    For $\mathbb{Q}(\sqrt[6]{3})$, notice that its minimal polynomial $x^6-3$ has $6$ roots but with an additional property:

    1. $a_1 = \sqrt[6]{3}$;
    2. $a_2 = \sqrt[6]{3}e^{\pi i/3}$;
    3. $a_3 = \sqrt[6]{3}e^{2\pi i/3}$;
    4. $a_4 = \sqrt[6]{3}e^{3\pi i/3} = -a_1$;
    5. $a_5 = \sqrt[6]{3}e^{4\pi i/3} = -a_2$;
    6. $a_6 = \sqrt[6]{3}e^{5\pi i/3} = -a_3$.

    So $3$ of the $\mathbb{Q}$-isomorphic fields are clearly equal to other fields, so there are only $3$ distinct of them:

    1. $\mathbb{Q}(\sqrt[6]{3})$;
    2. $\mathbb{Q}(\sqrt[6]{3}e^{\pi i/3})$;
    3. $\mathbb{Q}(\sqrt[6]{3}e^{2\pi i/3})$.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Fall Semester Homework 2""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 1
    **Consider the irreducible cubic $f(X) = X^3+pX+q$ over $\mathbb{Q}$, and let $a,b,c$ denote its roots in $\mathbb{C}$. Set $d = (a-b)(b-c)(c-a)$. With some patience, it is not hard to check that $d^2 = D(f) = -4p^3 - 27q^2$ (the discriminant of $f$). Let $F = \mathbb{Q}(a,d)$**.

    1. **Clearly $F$ is a subfield of the splitting field $E = \mathbb{Q}(a,b,c)$ of $f$. Show that in fact $E = F$. Conclude that $[E : \mathbb{Q}]$ is $3$ or $6$ according to whether $D(f)$ is or is not a square in $\mathbb{Q}$**;
    2. **Let $a,b,c$ be the roots of $f(X) = X^3 - 3X + 1$. Verify that $f$ splits in $\mathbb{Q}(a)$. Express $b,c$ in the basis $\lbrace 1, a, a^2\rbrace$**.

    Proof

    It remains to check $b,c \in F$. From $f(X) = X^3+pX+q$ and that $(X-a)(X-b)(X-c) =0$, expand latter and correspond coefficients we get $abc = -q$ and $a+b+c = 0$. Expand $(x-b)(x-c) = x^2 + (-b-c)x + bc$, then it equals $x^2 + ax - q/a$, so $(a-b)(a-c) = a^2+aa-q/a = 2a^2 - q/a$, this quantity is clearly in $F$, thus $d((a-b)(a-c))^{-1} = -(b-c) = c-b$ is also in $F$. Since $a+b+c = 0$, we have that $c - b + a+b+c = a + 2c$ is in $F$, thus $c$ in $F$, and thus $b$ in $F$.

    Now if $D(f)$ is a square then $d \in \mathbb{Q}$ so $E = F = \mathbb{Q}(a,d) = \mathbb{Q}(a)$, but since $f$ is by assumption irreducible, so it is still the minimal polynomial of $a$, and thus $[E:\mathbb{Q}] = \deg{f} = 3$. Otherwise $d^2$ is rational yet $d$ is not, then $[E:\mathbb{Q}] = [F:\mathbb{Q}]$ $= [F:\mathbb{Q}(a)][\mathbb{Q}(a):\mathbb{Q}]$ $= 2\cdot 3 = 6$.

    For part 2, in this case $D(f) = -4p^3 - 27q^2 = 81$ is a square, so as argued above $f$ splits in $E = \mathbb{Q}(a)$.

    Now, remember we have $9 = d = (b-c)(2a^2-1/a)$, so $9a = (b-c)(2a^3-1)$ (it does not matter here if we take $d = 9$ or $-9$, eventually we will get a $\pm$ because it is used in quadratic solutions). Since $a$ is a solution for $x^3-3x+1$, we can write $2a^3-1 = 6a-3$, also that since $E$ is degree $3$, we can write $b-c = la^2+ma+n$, so we have $(la^2+ma+n)(6a-3)-9a = 0$, expand this and remember that $a^3-3a+1 = 0$, it is easy to calculate $l = 2, m = 1, n = -4$. Now notice that $b-c$ is also the discriminant of the quadratic $(x-b)(x-c) = x^2 + (-b-c)x + bc$, thus use the quadratic formula we have $b,c = \frac{-a\pm (2a^2+a-4)}{2}$, simplify and they are $-a^2-a+2$ and $a^2-2$.

    ## Exercise 2

    **Let $f(X) = X^4 + 1$ and $E$ be its splitting field over $\mathbb{Q}$. Then $E = \mathbb{Q}(e^{\pi i/4}) = \mathbb{Q}(i, ?)$**.

    1. **Describe the corresponding between the subgroups of $G = Gal(E | \mathbb{Q})$ and the subextensions of $E$**;
    2. **Construct the factorization of $f$ over each of the intermediate extensions**.

    Solution

    The four roots of $f$ are $e^{i\pi/4},e^{i3\pi/4},e^{-i3\pi/4},e^{-i\pi/4}$ which are $\pm \sqrt{2}/2 \pm i \sqrt{2}/2$, so we can also write $E = \mathbb{Q}(i, \sqrt{2})$.

    Here it is easier to think of $E = \mathbb{Q}(e^{\pi i/4})$ as then we can see that the element of $G$ is completely determined by where it sends $e^{\pi i/4} = \zeta$. Let $\tau$ be the automorphism sending $\zeta$ to $\zeta^3$ and $\sigma$ be the automorphism sending $\zeta$ to $\zeta^5$, then $G = \lbrace \text{id}, \tau,\sigma,\tau\sigma\rbrace$. Subgroups of $G$ are $H_1 = \lbrace \text{id}, \tau\rbrace, H_2 = \lbrace \text{id}, \sigma\rbrace, H_3 = \lbrace \text{id}, \tau\sigma\rbrace$, it is not hard to determine the fixed fields, which correspond to the subextensions $G_1 = \mathbb{Q}(\sqrt{-2}), G_2 = \mathbb{Q}(i), G_3 = \mathbb{Q}(\sqrt{2})$ respectively.

    Starting from the 'full' split $f(x) = (x-\zeta)(x-\zeta^3)(x-\zeta^5)(x-\zeta^7)$, then:

    1. The factorization in $G_1$ would be $((x-\zeta)(x-\zeta^3))((x-\zeta^5)(x-\zeta^7))$ $= (x^2 -\sqrt{2}ix-1)(x^2 +\sqrt{2}ix-1)$;
    2. The factorization in $G_2$ would be $((x-\zeta)(x-\zeta^5))((x-\zeta^3)(x-\zeta^7))$ $= (x^2 -i)(x^2 +i)$;
    3. The factorization in $G_3$ would be $((x-\zeta)(x-\zeta^7))((x-\zeta^3)(x-\zeta^5))$ $= (x^2 -\sqrt{2}x+1)(x^2 +\sqrt{2}x+1)$.

    ## Exercise 3

    **Let $a = \sqrt{2 + \sqrt{2}}$ and $E = \mathbb{Q}(a)$**.

    1. **Write down the minimal polynomial $f$ of $a$ and check that $f$ split in $E$**;
    2. **Prove that the extension $E$ has cyclic Galois group $G = C_4$**.

    Solution

    $a^2 = 2+\sqrt{2}$ and $a^4 = 4 + 2 + 4\sqrt{2}$, so $x^4-4x^2+2$ is a polynomial in $\mathbb{Q}$ with $a$ as a root; it is Eisenstein thus irreducible and thus the minimal polynomial of $a$.

    From the form of $f$, $-a$ is also a root for $f$ thus $f = (x-a)(x+a)g$, long division reveals that $f = (x-a)(x+a)(x^2-(2-\sqrt{2}))$ $= (x-a)(x+a)(x-\sqrt{2-\sqrt{2}})(x+\sqrt{2-\sqrt{2}})$.

    Since $E$ contains $a$, it contains $a^2 = 2+\sqrt{2}$ and thus $\sqrt{2}$; it also contains the inverse of $a = \frac{1}{\sqrt{2+\sqrt{2}}}$ $= \frac{\sqrt{2-\sqrt{2}}}{\sqrt{2}}$ thus $\sqrt{2 - \sqrt{2}}$. And thus $f$ splits in $E$.

    The element (automorphism) in Galois group needs to map root of $f$ to root of $f$, with some calculations we can see that each automorphism is completely determined by how we map one of the root, for example, if $\sqrt{2+\sqrt{2}} \mapsto \sqrt{2-\sqrt{2}}$, then we must have $-\sqrt{2+\sqrt{2}} \mapsto -\sqrt{2-\sqrt{2}}$ and $\sqrt{2} \mapsto -\sqrt{2}$. In order to make the latter holds, we must have $\sqrt{2-\sqrt{2}} \mapsto -\sqrt{2+\sqrt{2}}$ because $\sqrt{2+\sqrt{2}}\sqrt{2-\sqrt{2}}$ $=\sqrt{2} \mapsto -\sqrt{2}$ $= \sqrt{2-\sqrt{2}}(-\sqrt{2+\sqrt{2}})$. So the Galois group is exactly $\lbrace \text{id}, \alpha,\beta,\tau\rbrace$ where $$\alpha = \begin{cases}\sqrt{2 + \sqrt{2}} &\mapsto& \sqrt{2 - \sqrt{2}}\\-\sqrt{2 + \sqrt{2}} &\mapsto& -\sqrt{2 - \sqrt{2}}\\\sqrt{2 - \sqrt{2}} &\mapsto& -\sqrt{2 + \sqrt{2}}\\-\sqrt{2 - \sqrt{2}} &\mapsto& \sqrt{2 + \sqrt{2}}\end{cases}$$ $$\beta = \begin{cases}\sqrt{2 + \sqrt{2}} &\mapsto& -\sqrt{2 + \sqrt{2}}\\-\sqrt{2 + \sqrt{2}} &\mapsto& \sqrt{2 + \sqrt{2}}\\\sqrt{2 - \sqrt{2}} &\mapsto& -\sqrt{2 - \sqrt{2}}\\-\sqrt{2 - \sqrt{2}} &\mapsto& \sqrt{2 - \sqrt{2}}\end{cases}$$ and $$\tau = \begin{cases}\sqrt{2 + \sqrt{2}} &\mapsto& -\sqrt{2 - \sqrt{2}}\\-\sqrt{2 + \sqrt{2}} &\mapsto& \sqrt{2 - \sqrt{2}}\\\sqrt{2 - \sqrt{2}} &\mapsto& \sqrt{2 + \sqrt{2}}\\-\sqrt{2 - \sqrt{2}} &\mapsto& -\sqrt{2 + \sqrt{2}}\end{cases}.$$ Now it is straightforward to verify $\beta = \alpha^2, \tau = \alpha^3$ and they all commute, so the Galois group is isomorphic to $C_4$

    ## Exercise 4

    **Let $L = \mathbb{Q}(\sqrt{2},\sqrt{3})$ and $E = L(a)$, where $\alpha = \sqrt{(2+\sqrt{2})(3+\sqrt{3})}$. Recall that $Gal(L | \mathbb{Q}) = C_2 \times C_2 = \lbrace 1,\sigma,\tau,\sigma\tau\rbrace$**.

    1. **Check that $\alpha \notin L$. Determine the degree $[E : \mathbb{Q}]$. Extend $\sigma, \tau$ to $E$ (consider $\frac{\sigma \alpha^2}{\alpha^2})$ and determine the possible value for $\sigma \alpha$ etc.)**
    2. **Do $\sigma$ and $\tau$ commute in $G = Gal(E | \mathbb{Q})$? What are their orders in $G$? Show that $G$ is the quaternion group**.

    Solution

    Suppose $\alpha \in L$ then $\alpha$ can be written in the form $a + b\sqrt{2} + c\sqrt{3} + d\sqrt{6}$. Consider the automorphism $\tau$ on $L$ fixing $\sqrt{2}$, then $(\alpha\tau(\alpha))^2$ $= \alpha^2\tau(\alpha^2)$ $= (2+\sqrt{2})(3+\sqrt{3})(2+\sqrt{2})(3-\sqrt{3})$ $= 6 (2+\sqrt{2})^2$ $= 36 + 24\sqrt{2}$. On the other hand $\alpha\tau(\alpha)$ $= (a + b\sqrt{2} + c\sqrt{3} + d\sqrt{6})(a + b\sqrt{2} - c\sqrt{3} - d\sqrt{6})$ and can be checked that it is in $\mathbb{Q}(\sqrt{2})$ which then must have the form $a+b\sqrt{2}$, but then $(\alpha\tau(\alpha))^2$ $= (a+b\sqrt{2})^2 \implies a^2+2b^2 = 36, ab = 12$, if there are rational solutions they must be integers, but there is no integer solutions, we have a contradiction, thus $\alpha \notin L$.

    The degree of $E$ over $L$ is $2$ and degree of $L$ over $\mathbb{Q}$ is $4$, the degree of $E$ over $\mathbb{Q}$ is $8$.

    As a remainder/for clarity, say $\sigma$ sends $\pm\sqrt{2}$ to $\mp\sqrt{2}$ and $\tau$ sends $\pm\sqrt{3}$ to $\mp\sqrt{3}$.

    $\alpha^2 = (2+\sqrt{2})(3+\sqrt{3})$ so $\sigma$ sends $\alpha^2$ to $(2-\sqrt{2})(3+\sqrt{3})$ and $\tau$ sends $\alpha^2$ to $(2+\sqrt{2})(3-\sqrt{3})$.

    So $\sigma$ extends to $\sigma^+$ and $\sigma^-$, sending $\alpha$ to $\pm \sqrt{(2-\sqrt{2})(3+\sqrt{3})}$ respectively, $\tau$ extends to $\tau^+$ and $\tau^-$, sending $\alpha$ to $\pm \sqrt{(2+\sqrt{2})(3-\sqrt{3})}$ respectively.

    Now notice $\sigma^+$ has order $4$: it sends $\sqrt{(2+\sqrt{2})(3+\sqrt{3})}$ to $\sqrt{(2-\sqrt{2})(3+\sqrt{3})}$; now since it should send $\sqrt{(2+\sqrt{2})(3+\sqrt{3})}\sqrt{(2-\sqrt{2})(3+\sqrt{3})}$ $=\sqrt{2}(3+\sqrt{3})$ to $-\sqrt{2}(3+\sqrt{3})$ (inherited from $\sigma$), we must have that it sends $\sqrt{(2-\sqrt{2})(3+\sqrt{3})}$ to $-\sqrt{(2+\sqrt{2})(3+\sqrt{3})}$; it then send this to $-\sqrt{(2-\sqrt{2})(3+\sqrt{3})}$ and then to $\sqrt{(2+\sqrt{2})(3+\sqrt{3})}$, combine the fact that we know $\sigma$ has order $2$, we get that $\sigma^+ \ne (\sigma^+)^2 \ne (\sigma^+)^3 \ne (\sigma^+)^4 = \text{id}$ so it has order $4$ (also notice that $(\sigma^+)^2 = \sigma^-$).

    The same argument hold for $\tau^+$, so it also has order $4$. But for now let's stick with $\sigma^+$.

    Since the whole group has $8$ elements, the subgroup $\lbrace \text{id}, \sigma^+, (\sigma^+)^2,(\sigma^+)^3\rbrace$ has index $2$ thus is a normal subgroup, and thus we can write the whole group as (since now everything has $~^+$, I will just drop it for simplicity) $\lbrace \text{id}, \sigma, \sigma^2,\sigma^3, \tau, \tau\sigma, \tau\sigma^2,\tau\sigma^3\rbrace$.

    With a similar argument (that why $\sigma$ has order $4$ instead of $2$), we may see that $\tau\sigma \ne \sigma\tau$: in short, it is because $\sigma$ has to map $\sqrt{6}$ to $-\sqrt{6}$.

    With all these information, we can write down the full Cayley table and notice that the relators $\sigma^4, \sigma^2\tau^2, \tau\sigma\tau\sigma^{-1}$ fully describe the group, and thus it has the presentation $G = \langle \sigma,\tau; \sigma^4,\sigma^2\tau^2,\tau\sigma\tau\sigma^{-1} \rangle$ and it is isomorphic to the quaternions group.

    ## Exercise 5

    **Let $E$ be the splitting field for $X^4-2$ over $\mathbb{Q}$ and $\alpha = i + 2^{1/4} \in E$**.

    1. **Check that no element of the Galois group $Gal(E| \mathbb{Q})$ fixes $\alpha$**;
    2. **Prove that $E = \mathbb{Q}(\alpha)$**.

    Solution

    By some easy factorization we should be able to see that $X^4 -2 = (X - 2^{1/4})(X+2^{1/4})(X - i2^{1/4})(X+i2^{1/4})$, thus $E = \mathbb{Q}(i,2^{1/4})$ so the Galois group has $8$ elements in it.


    Since all roots of $X^4 -2$ are distinct, the Galois group is a subgroup of $S_4$, and the only subgroup of $S_4$ with $8$ elements is $D_8$, which is generated by the permutations $D_8 = \langle (1234),(13) \rangle$, i.e. the Galois group is generated by $$\sigma=\begin{cases}2^{1/4} &\mapsto& i2^{1/4}\\i2^{1/4} &\mapsto& -2^{1/4}\\-2^{1/4} &\mapsto& -i2^{1/4}\\-i2^{1/4} &\mapsto& 2^{1/4}\end{cases} \iff \sigma=\begin{cases}2^{1/4} &\mapsto& i2^{1/4}\\i &\mapsto& i\end{cases}$$ and $$\tau=\begin{cases}2^{1/4} &\mapsto& -2^{1/4}\\-2^{1/4} &\mapsto& 2^{1/4}\\i2^{1/4} &\mapsto& i2^{1/4}\\-i2^{1/4} &\mapsto& -i2^{1/4}\end{cases} \iff \tau=\begin{cases}2^{1/4} &\mapsto& 2^{1/4}\\i &\mapsto& -i\end{cases}.$$ From here we can see that the only map(s) sends both $2^{1/4}$ and $i$ to themselves are $\sigma^4$ or $\tau^2$ or equivalent ones, which are all just the identity.

    For the second part, apparently $\mathbb{Q}(\alpha)\subset E$, and we know that $[E:\mathbb{Q}] = 8$. If we may find the minimal polynomial of $i+2^{1/4}$ and it has degree $8$, then it means $[\mathbb{Q}(\alpha):\mathbb{Q}] = 8$ as well thus $[E:\mathbb{Q}(\alpha)]= 1$ and we will have the desired equality, here is a construction:

    From the term $2^{1/4}$ we can see there is no way the degree is less than $4$, lets write down $\alpha$ to the power $1,2,3,4$:

    1. $\alpha = i+2^{1/4}$;
    2. $\alpha^2 = (i+2^{1/4})^2 = -1 + 2i2^{1/4} + 2^{2/4}$;
    3. $\alpha^3 = (i+2^{1/4})^3 = -i - 32^{1/4}+3i2^{2/4}+2^{3/4}$;
    4. $\alpha^4 = (i+2^{1/4})^4 = 3 - 4i2^{1/4}-62^{2/4}+4i2^{3/4}$;

    And now we can think $1, 2^{1/4}, 2^{2/4}, 2^{3/4}$ as 'basis', and try to simplify it, for example, $\alpha^4 - 4i\alpha^3$ will eliminate $2^{3/4}$ term, and so on, we will get $$\alpha^4 - 4i\alpha^3 - 6\alpha^2 + 4i\alpha - 1 = 0.$$ Now move the terms with $i$ to the right, and square them $$\begin{aligned}\alpha^4 - 6\alpha^2 - 1 &= 4i\alpha^3 - 4i\alpha\\\alpha^8-12\alpha^6+34\alpha^4+12\alpha^2+1 &= -16\alpha^6+32\alpha^4-16\alpha^2\\\alpha^8+4\alpha^6+2\alpha^4+28\alpha^2+1 &= 0\end{aligned}.$$ This polynomial is irreducible as $\alpha^8+1$ (take module $2$) is irreducible over $\mathbb{Q}$, and we find the degree $8$ minimal polynomial as desired.

    #### Remark

    Here is an easier way to prove part 2: Suppose $\mathbb{Q}(\alpha) \ne E$, then $\mathbb{Q}(a) = E^H$ for some $H \ne 1$, $H < G$, however then $H$ must fix $\alpha$, yet we just proved that the only element in $G$ fixes $\alpha$ is $1$, thus $H = 1$, a contradiction.

    ## Exercise 6

    **Let $\zeta = e^{2\pi i/15}, \eta = e^{2\pi i /5}$ (note that $\eta + \eta^{-1} = \frac{-1+\sqrt{5}}{2}$), $\rho = e^{2\pi i/3}$ and $\Phi_{15}(X) = \frac{(X^{15}-1)(X-1)}{(X^5-1)(X^3-1)} = X^8-X^7+X^5-X^4+X^3-X+1$ (irreducible over $\mathbb{Q}$)**.

    1. **Give the decomposition of $X^{15}-1$ as a product of irreducibles over $\mathbb{Q}$. What is the degree of $E = \mathbb{Q}(\zeta)$ over $\mathbb{Q}$**?
    2. **Show that the Galois group $G = Gal(E | \mathbb{Q})$ is isomorphic to a product $P$ of two cyclic groups, and construct this isomorphism**;
    3. **What subgroups of $G$ correspond to the subfields $\mathbb{Q}(\rho), \mathbb{Q}(\eta)$, $\mathbb{Q}(\sqrt{5})$, $\mathbb{Q}(\rho,\sqrt{5})$ of $E$ respectively**?

    Solution

    1. By class material we have $x^{15} - 1 = \prod\limits_{d | 15}\Phi_d(x) = \Phi_1(x)\Phi_3(x)\Phi_5(x)\Phi_{15}(x)$.
    	$\Phi_1(x)$ is simply $x-1$; $\Phi_3(x)$ $=x^2+x+1$, and $\Phi_5(x) = x^4+x^3+x^2+x+1$ because $3,5$ are primes, and we have $\Phi_{15}(x)$ given, so we have $x^{15} - 1 = (x-1)(x^2+x+1)(x^4+x^3+x^2+x+1)(x^8-x^7+x^5-x^4+x^3-x+1)$ Since $\zeta$ is a root of $x^{15}-1$, yet is clearly not root of $x-1$, $x^2+x+1$, or $x^4+x^3+x^2+x+1$, we must have that it is a root of $x^8-x^7+x^5-x^4+x^3-x+1$ and we know it is irreducible, thus $[E:\mathbb{Q}] = 8$;
    2. The roots of $\Phi_{15}(x)$ would be $\zeta, \zeta^2,\zeta^4, \zeta^7,\zeta^8,\zeta^{11},\zeta^{13},\zeta^{14}$, and can be written as $\zeta, \zeta^2, \zeta^4, \zeta^7, \overline{\zeta^7}, \overline{\zeta^4}, \overline{\zeta^2}, \overline{\zeta}$. Map in $G$ is completely determined by the value it sends $\zeta$ to, and can be seen as generated by $\sigma(\zeta) = \zeta^2$ and $\tau(\zeta) = \overline{\zeta}$, so that $\zeta \mapsto^\sigma \zeta^2 \mapsto^\sigma \zeta^4 \mapsto^\sigma \zeta^8 \mapsto^\sigma \zeta^{16} = \zeta$, $\sigma$ has order $4$, and similarly $\tau$ has order $2$. All maps commute. Now if we consider the map $$\alpha=\begin{cases}\sigma \mapsto (1,0) \\ \tau \mapsto (0,1) \end{cases}$$ then it is an isomorphism between $G$ and $C_4 \times C_2$;
    3. Write down the fix table for each of the map in $G$, for example $\sigma$ sends $\zeta$ to $\zeta^2$, so it sends $\rho = \zeta^5$ to $\zeta^{10}$ (not fixed), $\eta$ to $\zeta^6$ (not fixed), and $\sqrt{5} = 2(\zeta^3+\zeta^{-3})+1$ to $2(\zeta^6+\zeta^{-6})+1 = -\sqrt{5}$ (not fixed): $$\begin{array} {|r|r|r|r|}\hline \text{fixes:} & \eta & \rho & \sqrt{5} = 2(\eta+\eta^{-1})+1 \\\hline 1 & \surd & \surd & \surd \\\hline \sigma &  &  & \\\hline \sigma^2 &  & \surd & \surd \\\hline \sigma^3 &  &  & \\\hline \tau &  &  & \surd \\\hline \tau\sigma &  & \surd & \\\hline \tau\sigma^2 & \surd &  & \surd \\\hline \tau\sigma^3 &  & \surd & \\\hline \end{array}$$ And now it is easy to see the correspondences:
	
    	1. $\mathbb{Q}(\rho) \to \lbrace 1,\sigma^2,\tau\sigma,\tau\sigma^3 \rbrace$;
    	2. $\mathbb{Q}(\eta) \to \lbrace 1, \tau\sigma^2 \rbrace$;
    	3. $\mathbb{Q}(\sqrt{5}) \to \lbrace 1, \sigma^2, \tau, \tau\sigma^2 \rbrace$;
    	4. $\mathbb{Q}(\rho,\sqrt{5}) \to \lbrace 1, \sigma^2 \rbrace$.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Fall Semester Homework 3""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 1

    **Describe the Galois group $G = Gal(f)$ of $f(x) = x^6-4x^3+1 \in \mathbb{Q}[x]$ as a permutation group. Start by observing that the two real roots are inverse of each other**.

    Solution

    To see $f$ is irreducible, $f(x) = x^6 + x^3 + 1 \in \mathbb{F}_5[x]$, consider $f(x+1)$ and we will see its irreducibility by Eisenstein.

    Now, substitute $y = x^3$ then it is easy to calculate $y = 2 \pm \sqrt{3}$, so the $6$ roots for $f$ are the cubic roots of $2 + \sqrt{3}$ and $2 - \sqrt{3}$. Also observe that the real cubic root of $2+ \sqrt{3}$ is the inverse of the real cubic root of $2 - \sqrt{3}$. In particular, we can write $(2-\sqrt{3})^{1/3} = (2+\sqrt{3})^{-1/3} = (2+\sqrt{3})^{2/3}(2+\sqrt{3})^{-1} = ((2+\sqrt{3})^{1/3})^2(2-\sqrt{3})$, so the splitting field of $f$ can be written as $E = \mathbb{Q}(\omega, \sqrt[3]{2+\sqrt{3}})$ where $\omega$ is the root of unity of degree $3$. Also notice that we can write $\omega = -\frac{1}{2} + \frac{\sqrt{3}}{2}i$, so $E$ can also be written as $\mathbb{Q}(\sqrt{3}, i ,\sqrt[3]{2+\sqrt{3}})$, thus can be seen has degree $12$ over $\mathbb{Q}$. In particular, $G$ contains (at most) $12$ elements.

    Use SAGE and apply Dedekind Theorem:

    1. Factor in mod $7$ gives a cycle of type $(2,2,2)$:
    	```python
    	F.<a> = GF(7)
    	R.<x> = PolynomialRing(F)
    	f = x^6 - 4* x^3 + 1
    	f.factor()
    	>> (x^2 + x + 4) * (x^2 + 2*x + 2) * (x^2 + 4*x + 1)
    	```
    2. Factor in mod $5$ gives a cycle of type $(6)$:
    	```python
    	F.<a> = GF(5)
    	R.<x> = PolynomialRing(F)
    	f = x^6 - 4* x^3 + 1
    	f.factor()
    	>> x^6 + x^3 + 1
    	```

    So $G$ contains an $6$-cycle and an involution, so it contains at least $12$ elements.

    So $G$ has exactly $12$ elements.

    Now consider the intermediate extension $\mathbb{Q}(\sqrt{3})$, $f$ factor in $\mathbb{Q}(\sqrt{3})$ as $f = (x^3 - 2 - \sqrt{3})(x^3 - 2 + \sqrt{3})$, so, $Gal(E | \mathbb{Q}(\sqrt{3}))$ can be seen to be $S_3$, which has $6$ elements (in particular it has index $2$ in $G$), so $G$ can be seen as two copies of $S_3$, i.e. $G = S_3 \times \mathbb{Z}_2 = D_6$.

    ## Exercise 2

    **For $n$ odd, show that $\Phi_{2n}(x) = \Phi_n(-x)$**.

    Proof

    As a remainder, the definition of $\Phi$ is: $$\Phi_n(x) = \prod\limits_{\zeta \in \psi_n,\zeta\text{ primitive}}(x-\zeta) =\prod\limits_{o(\zeta) = n,\zeta \in \psi}(x-\zeta).$$ So by definition we have $$\Phi_{2n}(x) := \prod\limits_{\gcd(d,2n)=1}(x - e^{2\pi i d/2n}$$ The crucial step is somehow changing the subscript $\gcd(d,2n)=1$ to $\gcd(d,n)=1$. Notice that if $n$ is odd and $\gcd(d,n) = 1$, then the only possible common factor between $2d$ and $2n$ is $2$, and then $2d+n$ and $2n$ has no common factor (the prime factors of $2n$ are $2$ and factors of $n$, none of them are factors of $2d+n$ given $n$ is odd). The set of those $d$'s that are coprime with $n$ are clearly in a one-to-one correspondence with those $2d+n$'s that are coprime with $n$. So we can write $$\begin{aligned}=& \prod\limits_{\gcd(d,n)=1}(x - e^{2\pi i (2d+n)/2n}) \\ =& \prod\limits_{\gcd(d,n)=1}(x + (-1)e^{2\pi i (2d+n)/2n}) \\ =& \prod\limits_{\gcd(d,n)=1}(x + e^{2\pi i (2d+n)/2n}e^{2n\pi i/2n}) \\ =& \prod\limits_{\gcd(d,n)=1}(x + e^{\pi i (2d +2n)/n}) \\ =& \prod\limits_{\gcd(d,n)=1}(x + e^{2\pi i d/n})\end{aligned}.$$ Now remember that the number of $d$'s such that $1 \le d \le n$ and $\gcd(d,n) = 1$ is always even for $n > 2$. It can be seen by observing that every $d$ coprime with $n$ comes in pairs $d, n-d$ (and this fails for $n=1,2$ for an obvious reason). In particular, by multiplying $-1$ to each item will not change the result of the product, i.e. we can continue to write $$\begin{aligned}=& \prod\limits_{\gcd(d,n)=1}(-1)(x + e^{2\pi i d/n}) \\ =& \prod\limits_{\gcd(d,n)=1}(-x - e^{2\pi i d/n})\end{aligned}$$ which we should see that is $\Phi_n(-x)$ by definition.

    ## Exercise 3

    **Let $p \ge 3$ be prime, $\omega = \omega_p = \exp{\frac{2\pi i}{p}}$ and define the following expression in $\mathbb{Q}_p = \mathbb{Q}(\omega_p)$**: $$\alpha = \sum\limits_{r = 0}^{p-1}\omega^{r^2}, \beta = \prod\limits_{r = 1}^{(p-1)/2}(\omega^r - \omega^{-r}).$$

    1. **Show that $\mathbb{Q}(\alpha)$ is the unique quadratic subfield of $\mathbb{Q}_p$. Show that $\alpha\overline{\alpha} = p$ ($\alpha$ is known as the Gauss sum)**;
    2. **Check that $\beta^2 = (-1)^{(p-1)/2}\prod\limits_{r = 1}^{p-1}(1-\omega^r)$. Deduce that $\sqrt{p} \in \mathbb{Q}_p$ for $p \equiv 1$ mod $4$ and $\sqrt{-p} \in \mathbb{Q}_p$ for $p \equiv 3$ mod $4$**;
    3. **Show that $\mathbb{Q}_n(i) = \mathbb{Q}_{4n}$ for every odd integer $n$**;
    4. **Deduce the following Theorem: For every $N \in \mathbb{Z}$ there exists $n$ such that $\sqrt{N} \in \mathbb{Q}_n$ (this is the simplest special case of the Kronecker-Weber Theorem)**.

    Proof

    ### Part 1

    For $p$ being prime, the Galois group $Gal(\mathbb{Q}_q | \mathbb{Q})$ is known to be $U_p$ which in this case $\lbrace 1,2,3,\dots,p-1 \rbrace$. In order to have a quadratic subfield of $\mathbb{Q}_p$ we must have a subgroup of $U_p$ of index $2$ (Remainder: operation is multiplicity). Notice that in order to have a group structure, $1$ is of course in this subgroup, and any $a$ in this subgroup, $a^2$ must in this subgroup. Now observe that:

    1. $a^2 - (p-a)^2 = (a+p-a)(a-p+a)$ is a multiple of $p$, thus $a^2 \equiv (a-p)^2$ mod $p$;
    2. $a^2 \not\equiv b^2$ mod $p$ if $a,b \le (p-1)/2$.

    So it means there are exactly $(p-1)/2$ possibilities for $a^2$ mod $p$.

    For example, if $p = 7$, then $U_p$ is $\lbrace 1,2,3,4,5,6 \rbrace$, with that:

    1. $1^2 \equiv 1$ mod $7$;
    2. $2^2 \equiv 4$ mod $7$;
    3. $3^2 \equiv 2$ mod $7$;
    4. $4^2 \equiv 2$ mod $7$;
    5. $5^2 \equiv 4$ mod $7$;
    6. $6^2 \equiv 1$ mod $7$.

    (i.e. the point is they appear in pairs)

    It then means that there is exactly one subgroup $U'$ of index $2$ in $U_p$, for example in $U_7$ the only choice of $U'$ is $\lbrace 1,2,4 \rbrace$. It then means $\mathbb{Q}_p$ has a unique quadratic subfield. Now we just need to see what does this group fixes, and actually it is pretty clear from the above construction: the squares (mod $p$) of the elements in our $U'$ are still $U'$, so their sums must be the same, and thus they will fix the non-trivial number $\alpha$. In other words, $\mathbb{Q}(\alpha)$ is the unique quadratic subfield of $\mathbb{Q}_p$.

    To see $\alpha\overline{\alpha} = p$, notice that for each $\omega^r$, its complex conjugate is just $\omega^{p-r}$ because $p$ is odd. From construction, there are two possibilities for $\overline{\alpha}$:

    1. $\overline{\alpha} = \alpha$. For example in $U_5$, we can see that the subgroup of index $2$ is $\lbrace 1,4 \rbrace$, thus $\alpha = 1 + 2\omega_p^1 + 2\omega_p^4$, so $\overline{\alpha} = 1 + 2\omega_p^{5-1} +2\omega_p^{5-4} = \alpha$;
    2. Otherwise, $p - a^2$ is not in $U' \subset U_p$ for $a \in U'$. For example in $U_7$, $\alpha = 1 + 2\omega_p^1 + 2\omega_p^2 + 2\omega_p^4$ and $\overline{\alpha} = 1 + 2\omega_p^6 + 2\omega_p^5 + 2\omega_p^3$.

    Now we expand $\alpha\overline{\alpha}$:

    1. In the first case we will get $= (1 + 2\omega_p^1 + 2\omega_p^{a_2} + \dots + 2\omega_p^{p-a_2}+ 2\omega_p^{p-1})^2$ gives $= 1 + 2(p-1) + (p-1)(\omega_p^1 + \omega_p^2 + \dots + \omega_p^{p-1})$ $= 1 + p - 1 = p$.
    	To see this equality, remember $(1+a)^2 = 1+2a+a^2$, so expand the formula we will have one $1$; each $2\omega_p^a \cdot 2\omega_p^{p-a}$ gives $4$ and there are $(p-1)/2$ of such pair, so we have $2(p-1)$; the rest $(p-1)^2$ terms are just $\omega_p^1,\dots,\omega_p^{p-1}$, distributed evenly. The next case is similar, but little bit more complex;
    2. In the second case we will get $= 1 + 2(\omega_p^1+\dots + \omega_p^{p-1})$ $+ 4((p-1)/2 + ((\frac{p-1}{2})^2 - \frac{p-1}{2})/(p-1) \cdot (\omega_p^1+\dots + \omega_p^{p-1}))$ $= -1 + 4(\frac{p+1}{4} + \frac{p-3}{4} + \frac{p-3}{4}(\omega_p^1+\dots + \omega_p^{p-1}))$ $= -1 + p + 1 = p$.

    So in either case we have $\alpha\overline{\alpha} = p$.

    ### Part 2

    We defined $\beta = \prod\limits_{r = 1}^{(p-1)/2}(\omega^r - \omega^{-r})$, so $\beta^2 = \prod\limits_{r = 1}^{(p-1)/2}(\omega^r - \omega^{-r})^2$ $= \prod\limits_{r = 1}^{(p-1)/2}(\omega^r - \omega^{p-r})^2$. For each $(\omega^r - \omega^{p-r})^2$, expand it and we have $= \omega^{2r} + \omega^{2p-2r} - 2$, thus it equals to another pair $= \omega^{r'} + \omega^{-r'} -2$. Thus $\beta^2 = \prod\limits_{r = 1}^{(p-1)/2}(\omega^r + \omega^{p-r} -2)$ (i.e. we can remove $2\cdot$). Now notice that we can write each $(\omega^r - \omega^{p-r} -2) = -(2 - \omega^r - \omega^{p-r})$ $=-(1-\omega^r)(1-\omega^{p-r})$, and this gives the desired equality.

    Now use this expression for $\beta^2$, for now focus on the product part. Notice that for $p$ prime we can factor $x^p - 1 = (x-1)(x^{p-1}+\dots+x+1)$, but can also factor as $(x-1)(x-\omega_p^1)\dots (x-\omega_p^{p-1})$, so we must have $(x^{p-1}+\dots+x+1) = (x-\omega_p^1)\dots (x-\omega_p^{p-1})$, if we plugin $x = 1$, then we get $(x-\omega_p^1)\dots (x-\omega_p^{p-1}) = p$, i.e. $\beta^2 = (-1)^{(p-1)/2}p$, which is $p$ if $p \equiv 1 \pmod{4}$ and $-p$ if $p \equiv 3 \pmod{4}$. So $\beta = \sqrt{p}$ or $\sqrt{-p}$; $\beta$ is clearly in $\mathbb{Q}_p$ and we have the desired statement.

    ### Part 3

    $\mathbb{Q}_n(i)$ contains $e^{2\pi i/n}$ and $i = e^{\pi i/2}$, we want to build $e^{2 \pi i/4n}$ from them. It is easy: $e^{2\pi i/n}e^{\pi i/2}$ gives $e^{(4+n)\pi i/2n}$, since $n$ is odd, it can only be $\pm 1 \pmod{4}$, i.e. by times multiple of $i$'s, eventually we will get $e^{2 \pi i/4n}$ or $e^{-2 \pi i/4n}$, which can generate all the $4n$-th roots of unity.

    The other inclusion is obvious.

    ### Part 4

    Any $N$ can be factorized into product of (positive) primes and possibly a $-1$, so if we can find a $\mathbb{Q}_n$ such that it contains all $\sqrt{p}$ for $p$ prime factor of $N$ and possibly $i$ we are done.

    By above arguments:

    1. If $p$ is odd (i.e. not $2$) and $\equiv 1 \pmod{4}$ then $\sqrt{p} \in \mathbb{Q}_p$;
    2. If $p$ is odd and $\equiv 3 \pmod{4}$ then $\sqrt{-p} \in \mathbb{Q}_p$ and $\sqrt{p} \in \mathbb{Q}_{4p}$ (this one will also contain $i$);
    3. The only special case is when $p = 2$, but we know $\sqrt{\pm 2}$ are in $\mathbb{Q}_8 = \mathbb{Q}(\sqrt{2},i)$.

    Also it is easy to see that $\mathbb{Q}_p \subset \mathbb{Q}_q$ if $p | q$, so it is easy to put all the prime factors together, and the result follows.

    ## Exercise 4

    **Write down an irreducible polynomial of degree $5$ whose Galois group over $\mathbb{Q}$ is cyclic**.

    Solution

    We may use the result of Gauss Theorem about the cyclotomic field:

    > $\Phi_n$ is irreducible over $\mathbb{Q}$, thus $\mathbb{Q}_n$ is Galois extension of $\mathbb{Q}$, $[\mathbb{Q}_n:\mathbb{Q}]= \varphi(n)$, and $Gal(\mathbb{Q}_n | \mathbb{Q}) = U_n$.

    However we cannot use it directly on $5$, because as argued in exercise No. 2 above, $\varphi(n)$ is always even so cannot be $5$- but there is an easy workaround: take $11$, which is a prime, so that $\varphi(11) = 11 - 1 = 10$ is a multiple of $5$, and we will use Fundamental Theorem of Galois Theory to find some degree $5$ Galois (normal) extension from here.

    So consider $\mathbb{Q}_{11} = \mathbb{Q}(\zeta_{11})$ ($\zeta_{11}$ is the first root of unity of degree $11$, which is $e^{2\pi i/11}$), by Gauss it is Galois over $\mathbb{Q}$ with degree $10$ and $Gal(\mathbb{Q}_{11}| \mathbb{Q}) = C_{10}$. $C_{10} = C_2 \times C_5$, and since cyclic groups are abelian, any subgroup is normal. So essentially we want to find an intermediate fixed field $E$ which corresponds to the subgroup $C_2$ of $C_{10}$. We can find such $E$ by noticing that the minimal polynomial of $\zeta_{11}$ over the field $\mathbb{Q}(\zeta_{11} + \zeta_{11}^{-1})$ (which is $(x-\zeta_{11})(x-\zeta_{11}^{-1}) = x^2 - (\zeta_{11} + \zeta_{11}^{-1})x + 1$) has degree $2$, so $\mathbb{Q}(\zeta_{11} + \zeta_{11}^{-1})$ is what we want. By Fundamental Theorem of Galois Theory we have that $$Gal(\mathbb{Q}(\zeta_{11}+\zeta_{11}^{-1}) | \mathbb{Q}) \cong Gal(\mathbb{Q}(\zeta_{11}) | \mathbb{Q})/Gal(\mathbb{Q}(\zeta_{11}) | \mathbb{Q}(\zeta_{11}+\zeta_{11}^{-1})) \cong C_{10}/C_2 \cong C_5.$$ Now we just need to find the minimal polynomial of $\zeta_{11}+\zeta_{11}^{-1} = \zeta + \zeta^{10}$, and it will have a Galois group of $C_5$. We already know that this polynomial will be a quintic, so let's just write it down in its $1,2,3,4,5$-th powers: $$\begin{aligned} x &= \zeta + \zeta^{10} \\ x^2 &= 2 + \zeta^2 + \zeta^9 \\ x^3 &= 3\zeta + \zeta^3 + \zeta^8 + 3\zeta^{10} \\ x^4 &= 6 + 4\zeta^2 + \zeta^4 + \zeta^7 + 4\zeta^9 \\ x^5 &= 10\zeta + 5\zeta^3 + \zeta^5 + \zeta^6 + 5\zeta^8 + 10\zeta^{10}\end{aligned}.$$ Use the fact that summation of all $n$-th root of unity (including $1$) is $0$, it is not hard to get $x^5 + x^4 - 4x^3 - 3x^2 + 3x + 1 = 0$. That is a polynomial we want.

    ## Exercise 5

    **These problems involve $Gal(f)$ for $f(x) = x^n+px+q$. Note that $D(f) = (-1)^{n(n-1)/2}n^nq^{n-1} + (-1)^{(n-2)(n-1)/2}(n-1)^{n-1}p^n$**.

    1. **Prove that the Galois group of $x^5 + 20x + 16$ over $\mathbb{Q}$ is $A_5$**;
    2. **Let $f(x) = x^7 - 7x + 3$. Running SAGE to determine its Galois group, e.g**.,
    	```python
    	K.<z> = NumberField(x^7-7*x+3)
    	G = K.galois_group()
    	>> Galois group 7T5 (L(3,2)) with order 168 of x^7-7*x+3.
    	```
    	**Try to decipher and justify this answer. What are the roots of $x^7-7x+3$ in $\mathbb{C}$? What cycle types arise in its Galois group**?

    Solution

    Carefully calculate $D(f) = 1024000000 = 32000^2$, so the Galois group $G$ of $x^5 + 20x + 16$ over $\mathbb{Q}$ will be a subgroup of $A_5$.

    Use SAGE, take $f$ mod $3$ we have $x^5 + 2x + 1$ is irreducible, so $G$ contains a $5$-cycle; take mod $7$ we have a $3$-cycle; take mod $23$ we have a $(2,2)$-cycle.

    So now the cardinality of $G$ must divides $3,5,2$ thus $30$, but $A_5$ is simple thus cannot have a subgroup of cardinality $30$ (otherwise it is a normal subgroup because $| A_5 | = 60 = 2\cdot 30$), so the only possible value of $| G |$ is $60$, i.e. $G = A_5$.

    For the second part, calculate $D(f) = 37822859361 = 194481^2$, so $G_f$ is a subgroup of $A_7$. Use SAGE, in mod $5$ we have a $7$-cycle, $13$ we have $(2,4)$-cycle, $(3,3)$-cycle in $17$ and $(2,2)$-cycle in $79$.

    On the LMFDB website there are information about this group '7T5', in particular it lists the conjugacy classes: $$\begin{array} {|r|r|r|}\hline \text{Cycle Type} & \text{Size} & \text{Order} \\ \hline 0 & 1 & 1 \\ \hline 22 & 21 & 2 \\ \hline 42 & 42 & 4 \\ \hline 33 & 56 & 3 \\ \hline 7 & 24 & 7 \\ \hline 7 & 24 & 7 \\ \hline  \end{array}$$
    So we know the occurrences of cycle types in the Galois group, without a better idea I used some python code to iterate the first ~40k prime numbers to see if the occurrences of cycle types associated with $\overline{f} \in \mathbb{Z}_p$ match this distribution (normalized so total occurrences are $168$). The result:
    ```python
    cyc-tp occtarget occ
    1111111 0.97 1
    11122 21.06 21
    124 42.16 42
    133 56.2 56
    7 47.61 48
    ```
    So they are indeed 'pretty close', so '7T5' is highly possible to be the answer (if it is the only subgroup of $A_7$ with such a distribution of cycle types).

    Plot the graph of this polynomial we can see it has $3$ real roots, thus $2$ pairs of complex roots conjugate to each other, I can't see a further relation between them though.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Fall Semester Homework 4""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 1

    **Show that $Aut(\mathbb{Z}_8) = \mathbb{Z}_2 \times \mathbb{Z}_2$**.

    Proof

    Let $\sigma$ be automorphism, so it must has the form sending $x \mapsto x^n$, apparently we must have $\gcd(n,8) = 1$ otherwise it is not an automorphism, so $n$ can be $1,3,5$ or $7$, these maps are all distinct, so $| Aut(\mathbb{Z}_8) | = 4$, and it is easy to see each of the automorphism has period (at most) $2$, so the group $Aut(\mathbb{Z}_8) \cong \mathbb{Z}_2 \times \mathbb{Z}_2$.

    ## Exercise 2

    **Let $A \lhd G, B \lhd G$ with the quotients $G/A, G/B$ both abelian. Claim: Then $G/(A \cap B)$ is abelian**.

    1. **Give a one-line proof of this claim by using the derived subgroup $G'$**;
    2. **Deduce this claim from the Homomorphism Theorem without using $G'$ or the commutators**.

    Proof

    We have that $G' \le A$ and $G' \le B$ thus $G' \le A \cap B$, thus $G/(A\cap B)$ is abelian.

    To be a little bit more specific, first we use the fact that intersection of normal subgroups is still a normal subgroup, so $G/(A\cap B)$ is indeed a group. Then we have $A \cap B$ contains all commutators, so for any $x,y \in G$ we have that $x(A \cap B)y(A\cap B)(A \cap B)x^{-1}(A \cap B)y^{-1}$ $= (xyx^{-1}y^{-1})(A \cap B)$ $= A \cap B$. Thus $G/(A \cap B)$ is abelian because commutator is always the neutral element.

    Now without using commutators:

    1. $AB$ is normal subgroup of $G$ and $G/AB$ is abelian: For any $g \in G, a \in A, b \in B$, we have $gabg^{-1} = gag^{-1}gbg^{-1} \in AB$ because $A,B$ are normal; similarly $G/AB$ is abelian because both $G/A, G/B$ are abelian;
    2. $AB/A\cap B$ is abelian: consider the map $\varphi: AB \to AB/A \times AB/B$ given by $g \mapsto (gA, gB)$;
    	1. $\ker{\varphi} = A \cap B$;
    	2. $AB/A, AB/B$ are subgroup of $G/A, G/B$ thus abelian;
    	3. $\varphi$ is surjective: an generic element in the codomain is $(g_1A,g_2B) = (a_1b_1A, a_2b_2B)$ $=(b_1a_3b_1^{-1}b_1A, a_2B)$ $=(b_1A,a_2B)$, so image of $g = b_1a_2$ is $(g_1A,g_2B)$;
    	So $AB/A \cap B \cong AB/A \times AB/B$ by First Isomorphism Theorem and (product of abelian groups) is abelian;
    3. Now Third Isomorphism Theorem says $G/A \cap B \cong (G/AB) \times (AB/A \cap B)$ thus it is abelian.

    A much easier way for part 2 (it is actually in the above proof):

    Consider the map $\varphi: G \to G/A \times G/B$ given by $g \mapsto (gA, gB)$, then $\ker{\varphi} = A \cap B$, so we have $G/(A \cap B) \cong G/A \times G/B$ and result follows.

    ## Exercise 3

    **Let $H \lhd G$, $| H | = 7$, $| G | = 203$, show that $H < Z(G)$**.

    Proof

    Since $203 = 7 \cdot 29$ and $7, 29$ are both primes, in particular we know there is some subgroup $H'$ with 29 elements (Cauchy), and that $H, H'$ are both cyclic.

    Given that the subgroup of order $7$ is normal, semi-direct product is not possible:

    We know $Aut(H) \cong \mathbb{Z}_6$. Element in $H'$ can only have order $1$ or $29$, so order of $\varphi(a)$ can only be $1$ (because it must be factor of $6$, and also factor of $1$ or $29$), where $\varphi: H' \to Aut(H)$ and $a \in H'$. Thus $\varphi$ can only be trivial homomorphism and $G = H \times H'$.

    In particular $G$ is (direct) product of abelian groups thus abelian, thus $Z(G) = G$ and of course we have $H < Z(G) = G$.

    ## Exercise 4

    **We consider $G = \mathbb{Z}_5 \ltimes N$ where $| N | = 29^2 = 841$**.

    1. **Show that the only possible semi-direct product $\mathbb{Z}_5 \ltimes \mathbb{Z}_{841}$ is actually a direct product (Fact: $Aut(\mathbb{Z}_{p^2}) \cong \mathbb{Z}_{p^2-p}$)**;
    2. **Find an element of order $5$ in $GL(2, \mathbb{F}_{29})$, use it to construct an non-abelian semi-direct product $G = \mathbb{Z}_5 \ltimes (\mathbb{Z}_{29} \times \mathbb{Z}_{29})$. Describe this product by giving the presentation**.

    Solution

    1. We have $Aut(\mathbb{Z}_{841}) \cong \mathbb{Z}_{812}$, where $812 = 2\cdot 2 \cdot 7 \cdot 29$, so a homomorphism $\varphi: \mathbb{Z}_5 \to \mathbb{Z}_{812}$ can only map element with order $5$ to element with order $1$, i.e. $\varphi$ can only be trivial, which means only direct product is viable;
    2. The idea is that $N = \mathbb{Z}_{29} \times \mathbb{Z}_{29} = \langle b \rangle \times \langle c \rangle$ is isomorphic to $\mathbb{F}_{29}^2$ with the standard generators $\tilde{b} = \begin{pmatrix} 1\\0 \end{pmatrix}$ and $\tilde{c} = \begin{pmatrix} 0\\1 \end{pmatrix}$ which correspond to $b,c$ respectively, so $Aut(N)$ can be viewed as $GL(2,\mathbb{F}_{29})$. Elements in $\mathbb{Z}_5 = \langle a \rangle$ have order $5$ (except for $e$), so we need an automorphism of order $5$ (which can be viewed as a matrix in $GL(2,\mathbb{F}_{29})$). We may do that by factoring $x^5 = 1 \implies x^5-1 = 0$ in $\mathbb{F}_{29}$ (we want, in particular, a quadratic term), which is $= (x-1)(x^2+6x+1)(x^2-5x+1)$, the last part can be seen as the characteristic polynomial of $\begin{pmatrix} 0&-1\\1&5 \end{pmatrix} = \tilde{\sigma}$, this tells us $\tilde{\sigma}^5 = 1 = e$ and is an automorphism we want. This automorphism takes the standard basis in the addition group $\tilde{\sigma}\tilde{b} = \tilde{c}$ and $\tilde{\sigma}\tilde{c} = \begin{pmatrix} -1\\5 \end{pmatrix} = -\tilde{b}+5\tilde{c}$, so viewed in $(N, \cdot)$ we have an automorphism $\sigma$ taking $b$ to $c$, and taking $c$ to $b^{-1}c^5$. Since this automorphism is originally defined as $\sigma(x) = axa^{-1}$, we have a presentation of $G$ as
    	$$
    	G = \langle a,b,c | a^5 = b^{29} = c^{29} = 1, bc = cb, aba^{-1} = c, aca^{-1}=b^{-1}c^5 \rangle.
    	$$

    ## Exercise 5

    **Let $P = \mathbb{Z}_3 \times \mathbb{Z}_3$ be a subgroup of $GL(2,\mathbb{F}_7)$ generated by $t = \begin{pmatrix} 2&0\\0&1 \end{pmatrix}, s = \begin{pmatrix} 1&0\\0&2 \end{pmatrix}$. The group $P$ has four subgroups $P_i$ of order $3$ generated by $t,s,ts,t^2s$ respectively. Define $G_i = \mathbb{Z}_3 \ltimes_{\varphi_i}(\mathbb{Z}_7 \times \mathbb{Z}_7)$ where $\varphi_i$ is an isomorphism of $\mathbb{Z}_3$ with $P_i < GL(2,\mathbb{F}_7) = Aut(\mathbb{Z}_7 \times \mathbb{Z}_7)$**.

    1. **Show that $G_1 \cong G_2$. Give the presentations of $G_2, G_3, G_4$**;
    2. **Show that $Z(G_2)$ is non-trivial, but $Z(G_3), Z(G_4)$ are trivial**;
    3. **Show that every subgroup of order $7$ is normal in $G_3$, but $G_4$ has subgroups of order $7$ that are not normal**;
    4. **There are four non-isomorphic non-abelian groups of order $147$. We have constructed three of them so far, what is the missing one? Give its presentation**.

    Proof

    ### Part 1

    We know that $G_i \cong G_j$ if and only if the underlying automorphisms are conjugate, which can be viewed as matrices in our case. Note that two matrices that are conjugate must have same trace: $ABA^{-1} = C \implies tr(B) = tr(C)$, so each pair of $t, ts, t^2s$ are not conjugate, $G_1, G_3, G_4$ are not isomorphic. $G_1, G_2$ are isomorphic because $\begin{pmatrix} 0&1 \\ 1&0 \end{pmatrix} \begin{pmatrix} 2&0 \\ 0&1 \end{pmatrix} \begin{pmatrix} 0&1 \\ 1&0 \end{pmatrix}^{-1} = \begin{pmatrix} 1&0 \\ 0&2 \end{pmatrix}$.

    Follow the reasoning as problem 4, we see $s$ sends standard basis $b = \begin{pmatrix} 1\\0 \end{pmatrix}, c = \begin{pmatrix} 0\\1 \end{pmatrix}$ to $b$ and $2c$ respectively. $ts = \begin{pmatrix} 2&0 \\ 0&2 \end{pmatrix}$ sends $b, c$ to $2b, 2c$. $t^2s = \begin{pmatrix} 4&0 \\ 0&2 \end{pmatrix}$ sends $b,c$ to $4b, 2c$. So the presentations can be given as:

    1. $G_2 = \langle a,b,c | a^3 = b^7 = c^7 = 1, bc = cb, aba^{-1} = b, aca^{-1} = c^2 \rangle$;
    2. $G_3 = \langle a,b,c | a^3 = b^7 = c^7 = 1, bc = cb, aba^{-1} = b^2, aca^{-1} = c^2 \rangle$;
    3. $G_4 = \langle a,b,c | a^3 = b^7 = c^7 = 1, bc = cb, aba^{-1} = b^4, aca^{-1} = c^2 \rangle$.

    ### Part 2

    From the presentation we can see in $G_2$, $b$ is commutative with both $a$ and $c$, so $\langle b \rangle$ is also in the center, i.e. $Z(G_2)$ is not trivial. It is also not hard to see in $G_3, G_4$, none of the generators is commutative with both the other generators, so there will not be any non-trivial elements in the centers.

    ### Part 3

    Any group of $7$ elements is cyclic $\langle g \rangle$, since we define $G_i$ as $\mathbb{Z}_3 \ltimes_{\varphi_i}(\mathbb{Z}_7 \times \mathbb{Z}_7)$, the generator $g$ is of form $(b^ic^j, a^k)$. So $g^2 = (b^ic^j, a^k) \cdot (b^ic^j, a^k)$ $=(b^ic^j\varphi(a^k)(b^ic^j),a^{2k})$ (in our case $\varphi(a)$ sends $bc$ to $b^2c^2$) $=(b^{i+2^ki}c^{j+2^kj},a^{2k})$. Similarly $g^7 = (b^{i+6\cdot 2^ki}c^{j+6\cdot 2^kj},a^{7k})$ $=e$, in particular $7k \equiv 0 \pmod{3}$ and $i+6\cdot 2^ki \equiv 0 \pmod{7}$, so we must have $k = 0$ (will also need the fact that $g^3 \ne e$). Thus $\langle g \rangle$ is of the form $\langle b^ic^j \rangle$. This works for both $G_3$ and $G_4$.

    (The above part can also be proved using Sylow's Second Theorem. A subgroup of $7$ elements is a $7$ subgroup, so lies inside a (conjugate of) Sylow $7$-subgroup. In our case $\langle b,c \rangle$ is a Sylow $7$-subgroup, and it is also normal, so it is the only Sylow $7$-subgroup, so any subgroup of $7$ elements must lie inside $\langle b,c \rangle$ so has the form $\langle b^ic^j \rangle$)

    In $G_3$ we then have $ab^ic^ja^{-1}$ $= ab^ia^{-1}ac^ja^{-1}$ $=(b^ic^j)^2 \in \langle b^ic^j \rangle$; $bb^{i}c^jb^{-1} = b^ic^j$ and $cb^ic^jc^{-1} = b^ic^j$ because $b,c$ commute, so this subgroup is always normal.

    In $G_4$, the subgroup $\langle bc \rangle$ has order $7$ but is not normal, because $abca^{-1} = aba^{-1}aca^{-1} = b^4c^2$ is not in $\langle bc \rangle$.

    ### Part 4

    We may also factor $147$ as $3 \cdot 49$, since $Aut(\mathbb{Z}_{49}) \cong \mathbb{Z}_{42}$ and $3 | 42$, we have a non-trivial homomorphism from $\mathbb{Z}_3 = \langle a \rangle$ to $\mathbb{Z}_{42} = \langle \varphi \rangle$, namely sending $a \to \varphi^{14}$. We can take $\varphi$ as the automorphism sending $b \in \mathbb{Z}_{49} = \langle b \rangle$ to $b^2$, then $\varphi^{14}$ sends $b \to b^{2^{14}} = b^{18}$ (taking mod $49$, because $b^{49} = e$), and this gives a semi-direct product $\mathbb{Z}_3 \ltimes \mathbb{Z}_{49} = \langle a,b | a^3 = b^{49} = 1, aba^{-1} = b^{18} \rangle$.

    ## Exercise 6

    **Let $Q$ be the quaternion group of order $8$. Show that $Q$ can be realized as a non-trivial extension in four ways - thrice as an extension of $\mathbb{Z}_4$ by $\mathbb{Z}_2$ and once as an extension of $\mathbb{Z}_2$ by $\mathbb{Z}_2 \times \mathbb{Z}_2$- but that none of these extensions is split**.

    Proof

    Write $Q = \lbrace \pm 1,\pm i, \pm j, \pm k \rbrace$.

    Consider the short exact sequence $1 \to N \xrightarrow{i} Q \xrightarrow{\pi} H \to 1$. By assumption we must have that $N$ is a normal subgroup of $Q$. There are $4$ non-trivial subgroups of $Q$ and they are all normal.

    Three of them are isomorphic to $\mathbb{Z}_4$, namely $\lbrace \pm1,\pm i \rbrace$, $\lbrace \pm1,\pm j \rbrace$ and $\lbrace \pm1,\pm k \rbrace$. Since those subgroups are of order $4$ we must have $H = Q/N \cong \mathbb{Z}_2$. If we assume the result of exercise precedent, then we know $Q$ is a split extension if and only $Q$ is a semi-direct product of $N$ by $H$ if and only if we have a non-trivial homomorphism $H \to Aut(N)$, but in our case $H = Z(Q)$, in particular, $1\cdot n \cdot 1^{-1} = n$ and $-1 \cdot n \cdot -1^{-1} = n$ for any $n \in N$, so this homomorphism is always trivial, so $Q$ is not a split extension.

    The remaining normal subgroup of $Q$ is $\lbrace \pm 1 \rbrace \cong \mathbb{Z}_2$ (so $Aut(N) = 1$, $\varphi: H \to Aut(N)$ must be trivial, so $Q$ is not a split extension), in this case $Q/N = \lbrace N, iN, jN, kN \rbrace \cong \mathbb{Z}_2 \times \mathbb{Z}_2$.

    ## Exercise 7

    **Let $[G:H] = n$, show that there exists $K \lhd G$ with $K < H$ and $[G:K] \le n!$**.

    Proof

    By assumption, there are $n$ (left) cosets $gH$ in $G$, and $G$ (left) act on $G/H$ by $g(g'H) = (gg')H$. If we denote the set of cosets of $H$ as $X$ then for any $g \in G$ we have $g(X) = X$ (if $(gg_1)H = (gg_2)H$ then $g_2^{-1}g^{-1}gg_1 \in H$ then $g_2^{-1}g_1 \in H$ then $g_1H = g_2H$); for each $g$, we can in particular view the correspondence as a permutation $\alpha_g$.

    Thus we have a map $\varphi: G \to S_n$ where $S_n$ is the symmetry group with $n = | X|$, and $\varphi(g) = \alpha_g$. For any $g_1,g_2 \in G$, we have $\varphi(g_1g_2) = \alpha_{g_1g_2}$ maps $gH$ to $g_1g_2gH$; and $\varphi(g_1)\varphi(g_2) = \alpha_{g_1}\alpha_{g_2}$ maps $gH$ to $g_2gH$ to $g_1g_2gH$, so they are equivalent as maps, thus $\varphi$ is a homomorphism.

    Let $K = \ker{\varphi}$, then $K$ is a normal subgroup of $G$. The First Isomorphism Theorem says $G/K \cong \text{im}(\varphi)$, which is a subgroup of $S_n$ with $| S_n | = n!$, in particular $[G:K] = | G/K | \le n!$.

    By definition of kernel, for any $k \in K$ we have $\varphi(k) = \alpha_k = \text{id}$, i.e. $kgH = gH$ for all $g$, which means $k \in H$ thus $K < H$.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Fall Semester Homework 5""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 1

    **Let $G$ be a finite group, let $r$ be the number of conjugacy classes of $G$, show that $| \lbrace (a,b) \in G \times G | ab = ba \rbrace | = r | G |$**.

    Proof

    Write the LHS as $| \lbrace (a,b) \in G \times G | aba^{-1} = b \rbrace |$, we can realize that what it does is to count $C_G(b)$ for all $b \in G$ and add them together.

    We know from the counting rule (Orbit-Stabilizer Theorem, $G$ acts on itself by conjugation) that for each $b$ we have $| K_b | = [G : C_G(x)]$ so $| C_G(b) | = | G | / | K_b |$ where $K_b$ is the conjugacy class of $b$. We also know that the conjugacy classes form a partition of $G$.

    So we have LHS $=$ $| \lbrace (a,b) \in G \times G | aba^{-1} = b \rbrace |$ $= \sum\limits_{b \in G} | C_G(b) |$ $= \sum\limits_{U_i\text{ conjugacy classes of G}} \sum\limits_{b \in U_i} | C_G(b) |$ $= \sum\limits_{U_i} \sum\limits_{b \in U_i} | G | / | K_b |$ $= \sum\limits_{U_i} | K_b \| G | / | K_b |$ (because for each $b$ in the same conjugacy class, $K_b$ are apparently the same, and there are $| K_b |$ many of them) $= \sum\limits_{U_i}| G |$, and now it is easy to see this summation only depends on the number of conjugacy classes of $G$, which equals $r | G |$ as desired.

    ## Exercise 2

    **Let $G$ be a finite group, $C = \mathbb{Z}_n, n\ge 2$ and it is viewed additively (as $\mathbb{Z}/n\mathbb{Z}$). Let $\Omega$ be the set of $n$-tuples $(x_1,\dots, x_n)$ of elements of $G$ such that $x_1x_2\dots x_n = 1$**.

    1. **Show that $C$ acts on $\Omega$ by $\overline{k}\cdot(x_1,\dots,x_n) = (x_{1+k},\dots, x_{n+k})$ where $\overline{k} \in C$ and the subscripts on the right are interpreted modulo $n$**;
    2. **(McKay's proof of Cauchy Theorem) Now suppose $n = p$ is a prime that divides $| G |$. Examine the number of $C$-orbits of size $1$ in $\Omega$, and deduce that the number of elements of order $p$ in $G$ is $-1 \pmod{p}$**.

    Proof

    1. Observe that $(x_{1+k},\dots, x_{n+k})$ is just $(x_{1},\dots, x_{n})$ 'move to the right' but the elements are the same. For example, $(x_{1+3},\dots, x_{5+3})$ is the same as $(x_{4},\dots, x_{8}) = (x_4, x_5, x_1, x_2, x_3)$. In particular, this action is well defined in the sense that $\overline{k}\cdot(x_1,\dots,x_n) \in \Omega$.
    	Now, for any element $(x_1,\dots,x_n) \in \Omega$, $0\cdot(x_1,\dots,x_n)$ $:=(x_1,\dots, x_n)$ (since we view $C$ as additive group, the identity is $0$). Also that $\overline{h}\cdot(\overline{k}\cdot(x_1,\dots,x_n))$ and $(\overline{h}+\overline{k})\cdot(x_1,\dots,x_n)$ are apparently the same, the first one means to move $k$ then $h$ units to the right (up to module $n$), and the second one just means to move $h+k$ units to the right.
    	So this is a group action by definition.
    2. $G$ is finite, so let us suppose $G$ has cardinality $m$. Since $G$ is a group, any element has an unique inverse, that means we can freely choose $x_1,\dots, x_{n-1}$, and then $x_n$ is fixed to make the tuple in $\Omega$. Thus the cardinality of $\Omega$ is $m^{n-1}$.
    	Observe that in general, $\overline{k}\cdot(x_1,\dots,x_n) = (x_1,\dots, x_n)$ if and only if we have either $\overline{k} = 0$ or $x_1 = x_2 = \dots = x_n$.
    	In particular, the $C$-orbits in $\Omega$ have either size $1$ (those are for the elements in the form $(x_1,\dots,x_1)$), or size $n$, which consists of $n$ different (because $n$ is a prime) elements $(x_1,\dots,x_n)$, $(x_2,\dots,x_n,x_1)$, $\dots$, $(x_n,x_1,\dots,x_{n-1})$.
    	Those orbits form a partition of $\Omega$, so we have $m^{n-1} = a\cdot 1 + b \cdot n$ $\implies m^{n-1} - a = b \cdot n$ for some $a, b$. By assumption $m$ is a multiple of $n$ and $n$ is a prime, so we must have that $a$ is also a multiple of $n$.
    	So we have $a = k\cdot n$, and by construction it is the number of elements $x$ in $G$ such that $x^n = 1$. Since $n$ is a prime, the periods of those $x$'s are either $1$ or $n$, but there is exactly $1$ element with period $1$ (namely $1$), thus there are $k\cdot n - 1$ elements with period $n$ in $G$, in particular, this number $\equiv -1 \pmod{n}$.

    ## Exercise 3

    **Show that if $P$ is a Sylow $p$-subgroup of $G$, then $N_G(P)$ is a self-normalizing subgroup of $G$, meaning that $N_G(N_G(P)) = N_G(P)$. Any subgroup of $G$ that can be written as $N_G(P)$ for some non-trivial $p$-subgroup $P$ of $G$ is said to be a $p$-local subgroup of $G$**.

    Proof

    By definition of normalizer, $N_G(P) \lhd N_G(N_G(P))$. $P \le N_G(P) \le G$, so $P$ must also be Sylow $p$-subgroup of $N_G(P)$.

    So Frattini's Argument says that $N_G(N_G(P)) = N_G(P)\cdot N_{N_G(N_G(P))}(P)$. The last term looks complicated, but apparently it sits inside $N_G(P)$, so RHS is just $N_G(P)$, and that gives the desired statement.

    ## Exercise 4

    **Let $G= A_7$. Start by counting the $7$-cycles and the $5$-cycles in $G$. Let $\sigma = (1234567)$ and $\rho = (12345)$**.

    1. **Let $P = \langle \sigma \rangle \in Syl_7(G)$ and $H = N_G(P)$. Determine $n_7 = | Syl_7(G) |$ and $| H |$. Besides powers of $\sigma$, what even permutations $\tau \in A_7$ normalize $P$? Describe $H$ as a semi-direct product**;
    2. **Now let $Q = \langle \rho \rangle \in Syl_5(G)$ and $K = N_G(Q)$. Find $n_5$ and describe $K$**.

    Solution

    1. There are $6! = 720$ of $7$-cycles (first must be $1$, the rest can be in any order). $7$-cycles are the only cycle type that have order $7$, so they are the only possible elements in the Sylow $7$-subgroups. For any $7$-cycle $\alpha$, its powers $\alpha^2,\dots,\alpha^6$ are apparently also $7$-cycles. So these $720$ elements gives $720/6 = 120$ disjoint set of $7$-cycles in the form $\lbrace \alpha,\dots,\alpha^6 \rbrace$, each of them together with the identity gives a Sylow $7$-subgroup, so $n_7 = 120$. Now by Sylow, $n_7 = [G:N_G(P)]$ so $| N_G(P) | = 2520/120 = 21$.
    	Now a fact when doing multiplication of permutations: $\tau (1234567) \tau^{-1} = (\tau(1)\tau(2)\dots\tau(7))$. With this it is not too hard to find that $\langle (235)(476) \rangle$ also normalize $P$ (it makes sense, as we may want something with order $3$), also note that $(235)(476)(1234567)(467)(253)$ $= (1357246)$ $= (1234567)^2$. Denote this group $P' \cong \mathbb{Z}_3$, then $P'$ is not a normal subgroup of $H$ and $P \cap P' = 1$, thus $H = P \rtimes P' = \mathbb{Z}_7 \rtimes \mathbb{Z}_3$, and a presentation of $H$ is $\langle a,b | a^7 = b^3 = 1, bab^{-1} = a^2 \rangle$.
    2. Now similarly we count $5$ cycles, if we start with $1$, there are $6\cdot5\cdot 4 \cdot 3 = 360$ of them, if we start with $2$, there are $5\cdot4\cdot 3 \cdot 2 = 120$ of them (cycle always start with smallest number, so they cannot be chosen from $1$), if we start with $3$ there are $24$ of them, and we cannot start with $4,5,6,7$. So there are $504$ $5$-cycles in $A_7$. Notice again that this is the only cycle type with period $5$, so with a similar argument we should see $n_5 = 126$, and thus $| N_G(Q) | = 20$.
    	Proceed as before we may see $\langle (2354) \rangle$ normalize $\langle (12345) \rangle$, $(2354)(12345)(2453) = (12345)^2$. The problem is that this is not an even permutation. Nevertheless, since we are working in $A_7$ there is an easy way to solve this: we use $(2354)(67)$. This is an even permutation and $(2354)(67)(12345)(2453)(67) = (12345)^3$. So we have $K \cong \mathbb{Z}_5 \rtimes \mathbb{Z}_4$ $\cong \langle a,b| a^5 = b^4 = 1, bab^{-1} = a^3 \rangle$ (so it is $F_5$).

    ## Exercise 5

    **Show that $G$ is not simple whenever $| G | = p^a(p+1)$ where $a > 1$**.

    Proof

    By Sylow, $n_p | p+1$ and $n_p \equiv 1 \pmod{p}$, thus $n_p = 1$ or $p+1$.

    If $n_p = 1$ then $G$ is not simple.


    Suppose now $n_p = p+1$. Since $p+1 \not\equiv 1 \pmod{p^2}$, we can find $S,T$ Sylow $p$-subgroups such that $[S:S \cap T] = p$ $= [T: S \cap T]$ (note: here we use the assumption that $a$ is at least $2$, otherwise $S \cap T$ is just $\lbrace 1 \rbrace$ and it cannot be used to prove simpleness). By a property of $p$-subgroup, $S\cap T \lhd S$ and $S\cap T \lhd T$. Thus by definition of normalizer we have $S, T < N_G(S \cap T)$, thus $N_G(S \cap T)$ has more than $1$ Sylow $p$-subgroups, thus it has at least $1+p$ Sylow $p$-subgroups. Thus it has at least $p^a(p+1)$ elements by Sylow's Third. Since $G$ only has $p^a(p+1)$ element, $N_G(S \cap T)$ must equal $G$, but then $S \cap T$ is a normal subgroup of $G$.

    (Or, after that we have $S, T < N_G(S \cap T)$ we can get that $ST \subseteq N_G(S \cap T)$ (it is not necessarily a subgroup), and $| ST | = \frac{| S \| T |}{| S \cap T |} = p^{a+1}$, so $| N_G(S \cap T) |$ is greater than or equal to $p^{a+1}$ but also a divisor of $p^a(p+1)$ because it is a subgroup of $G$, the only option is $| N_G(S\cap T) | = p^a(p+1)$ thus $N_G(S \cap T) = G$)

    Nevertheless, the statement is also true for $a = 1$, i.e. $G$ is not simple if $| G | = p(p+1)$:

    Again $n_p$ is either $1$ or $p+1$, and we are done if $n_p = 1$, so assume $n_p = 1+p$, those groups now must intersect trivially (otherwise the intersection all have $p$ elements by Lagrange because intersection of subgroups is subgroup, which means they are the same group), so they take up $(1+p) \cdot (p-1) = p^2 - 1$ elements (of period $p$). There are $p+1$ other elements. They together form a subgroup, and that is the only subgroup with $1+p$ elements (because any other element has period $p$), so it is characteristic thus normal.

    ## Exercise 6

    **Show that if $| G | \in \lbrace 30, 56, 105, 132 \rbrace$ then $G$ is not simple**.

    Proof

    Since $30 = 5\cdot (5+1)$, $56 = 7 \cdot (7+1)$ and $132 = 11 \cdot (11+1)$, by the statement mentioned above, those groups are not simple.

    For $105 = 3 \cdot 5 \cdot 7$: $n_7 | 15$ and $n_7 \equiv 1 \pmod{7}$, so $n_7 = 1$ or $15$; $n_5 | 21$ and $n_5 \equiv 1 \pmod{5}$ thus $n_5 = 1$ or $21$. Assume $n_7 = 15$ and $n_5 = 21$, otherwise we are done. By Lagrange those $5$ and $7$-groups all intersect trivially, so there are $15 \cdot (7-1) = 90$ elements of period $7$, and $21\cdot(5-1) = 84$ elements of period $5$, but $90+84>105$ there is already not enough room for that.

    ## Exercise 7

    **Let $| G | = 56$. Follow the steps below to construct a full list of distinct non-abelian groups of order $56$**.

    1. **Show that $G$ has either a normal Sylow $2$-subgroup $S$ or a normal Sylow $7$-subgroup $P = \langle u \rangle$**;
    2. **Let now $\mathbb{Z}_7 \cong P \lhd G$, then $G = S \ltimes \mathbb{Z}_7$ and two such semi-direct products are not isomorphic if the kernels of the maps from $S$ into $U_7 \cong \mathbb{Z}_6$ are not isomorphic (this is not hard to prove, so let's assume it for now). Construct the following non-abelian groups**:
    	- **one group when $S = \mathbb{Z}_2 \times \mathbb{Z}_2 \times \mathbb{Z}_2$**;
    	- **two non-isomorphic groups when $S = \mathbb{Z}_4 \times \mathbb{Z}_2$**;
    	- **one group when $S = \mathbb{Z}_8$**;
    	- **two non-isomorphic groups when $S = Q_8$ (this includes the direct product $S \times P$)**;
    	- **three non-isomorphic groups when $S = D_8$ (this includes the direct product as well)**;
    3. **Let now $P \not\lhd G$, $S \lhd G$ (so $G = S \rtimes P$). Let an element $u \in P$ act by conjugation on $S$, and deduce that all non-identity elements of $S$ have the same order, thus $S = …$**;
    4. **Prove that there is a unique group of order $56$ with a non-normal Sylow $7$-subgroup. Give its presentation**. *Hint: $168 = 7 \times 24$*.

    Solution

    1. We know $n_7 = 1$ or $8$. Suppose $n_7 = 8$, then there are $8 \cdot 6 = 48$ elements of order $7$, the remaining $8$ elements form a subgroup and it must be the unique Sylow $2$-subgroup.
    2. So we want to identify homomorphisms $\varphi: S \to \mathbb{Z}_6$ up to isomorphic kernels. The first three cases we do not want trivial homomorphism, because otherwise we have a direct product of abelian group thus $G$ is abelian:
    	1. If $S = \mathbb{Z}_2 \times \mathbb{Z}_2 \times \mathbb{Z}_2$ $= \langle a,b,c \rangle$, then $\varphi(a),\varphi(b),\varphi(c)$ have either period $1$ or $2$. There is only one element in $Aut(\mathbb{Z}_7)$ with order $2$, which is the one (call it $\psi$) sending $1$ to $6$ (because $6\cdot 6 = 36 \equiv 1 \pmod{7}$). So there are not too many choices: one or two or three of the generators are sent to $\psi$. It is not hard to see that those homomorphisms all have the same kernel, so the semi-direct product are all isomorphic. So let's say we use the homomorphism sends $a$ to $\psi$ and $b,c$ to $1$, then we have the relations $a^2 = b^2 = c^2 = d^7 = 1$ (denote the generator of $\mathbb{Z}_7$ by $d$), $ada^{-1} = d^6$, $bdb^{-1} = d$ and $cdc^{-1} = d$, also $ab = ba$, $bc = cb$, and $ac = ca$;
    	2. If $S = \mathbb{Z}_4 \times \mathbb{Z}_2 = \langle a,b \rangle$, then $\varphi(a)$ has period $1, 2$ or $4$ and $\varphi(b)$ has period $1$ or $2$. But there is no automorphism of order $4$ in $Aut(\mathbb{Z}_7)$, so we have the following circumstances: $\varphi_1$ sending $a$ to $\text{id}$, $b$ to $\psi$ (the map sending $1$ to $6$); $\varphi_2$ sending $a$ to $\psi$, $b$ to $\text{id}$, and $\varphi_3$ sending both $a,b$ to $\psi$. It is not hard to see that $\ker{\varphi_1}$ is $\mathbb{Z}_4$ and the other two have kernel $\mathbb{Z}_2 \times \mathbb{Z}_2$. So we have two different semi-direct product, $\varphi_1$ induces $$\langle a,b,c | a^4 = b^2 = c^7 = 1, ab = ba, aca^{-1} = c, bcb^{-1} = c^6 \rangle;$$	$\varphi_2$ or $\varphi_3$ induces $$\langle a,b,c | a^4 = b^2 = c^7 = 1, ab = ba, aca^{-1}=c^6, bcb^{-1} = c^6 \rangle.$$
    	3. If $S = \mathbb{Z}_8 = \langle a \rangle$ then $\varphi(a)$ has period $1,2,4$ or $8$, again there is no element of order $4, 8$ in $Aut(\mathbb{Z}_7)$ so the only none trivial one is $\varphi(a) = \psi$, induces the semi-direct product $$\langle a,b | a^8 = b^7 = 1, aba^{-1} = b^6 \rangle.$$
    		4. If $S = Q_8 = \langle a,b | a^4 = 1, b^2 = a^2, ba = a^{-1}b \rangle$, with a similar argument, there are $4$ choices of $\varphi$: $\varphi_1$ sending $a,b$ to $\text{id}$ (we start to allow trivial homomorphisms because $Q_8$ is not abelian), $\varphi_2$ sending $a$ to $\text{id}$, $b$ to $\psi$, $\varphi_3$ sending $a$ to $\psi$, $b$ to $\text{id}$, and $\varphi_4$ sending $a,b$ to $\psi$. The kernel of $\varphi_1$ is of course $Q_8$, and kernels of $\varphi_{2,3,4}$ are all $\mathbb{Z}_4$ sitting in $Q_8$. So we either have a direct product $Q_8 \times \mathbb{Z}_7$, or a semi-direct product $$\langle a,b,c | a^4 =c^7 = 1, b^2 = a^2, ba = a^{-1}b, ada^{-1} = d^6, bdb^{-1} = d^6 \rangle.$$
    		5. If $S = D_8 = \langle a,b | a^4 = b^2 = 1, ba = a^{-1}b^{-1} \rangle$, again, there are $4$ choices of $\varphi$: $\varphi_1$ sending $a,b$ to $\text{id}$, $\varphi_2$ sending $a$ to $\text{id}$, $b$ to $\psi$, $\varphi_3$ sending $a$ to $\psi$, $b$ to $\text{id}$, and $\varphi_4$ sending $a,b$ to $\psi$. $\varphi_1$ still gives us a direct product. Kernel of $\varphi_2$ is cyclic, induces the semi-direct product $$\langle a,b,c | a^4 = b^2 = c^7 = 1, ba = a^{-1}b^{-1}, aca^{-1} = c, bcb^{-1} = c^6 \rangle$$ and kernel of $\varphi_{3,4}$ is $\mathbb{Z}_2\times \mathbb{Z}_2$, gives the semi-direct product $$\langle a,b,c | a^4 = b^2 = c^7 = 1, ba = a^{-1}b^{-1}, aca^{-1} = c^6, bcb^{-1} = c \rangle.$$
    3. Consider $P$ act by conjugation on $S$. For any $s \in S$ we know that $| C_P(s) |$ can be either $1$ or $7$. For at least one $s$, we must have $| C_P(s) | \ne 1$, otherwise we have a direct product. But $S$ only have $8$ elements, and the conjugacy class of identity already takes up $1$ slot, it follows that all other $7$ non-identity elements in $S$ are in the same conjugacy class. But conjugation preserves order: $x^n = 1 \iff (gxg^{-1})^n = gx^ng^{-1} = 1$, we thus have that all non-identity elements in $S$ are of the same order. The only such group with $8$ elements is $\mathbb{Z}_2 \times \mathbb{Z}_2 \times \mathbb{Z}_2$.
    4. By part 1, if it has a non-normal Sylow $7$-subgroup, it must have a normal Sylow $2$-subgroup; by part 3, $G \cong \mathbb{Z}_7 \ltimes (\mathbb{Z}_2^3)$. So we are looking for a non-trivial homomorphism $\varphi: \mathbb{Z}_7 \to Aut(\mathbb{Z}_2^3)$. The latter can be interpreted as $GL_3(F_2)$ (i.e. $3 \times 3$ matrices with non-zero determinant). Notice the order of $GL_3(F_2)$ is $(2^3-1)(2^3-2)(2^3-2^2) = 168 = 2^3 \cdot 3 \cdot 7$. By Cauchy there are element of order $7$ in this group, so we must be able to find a homomorphism.
    	To prove uniqueness, notice the image of $\mathbb{Z}_7$ under that homomorphism $\varphi$ (which is not trivial) must have $7$ elements thus a Sylow $7$-subgroup. We know that $\varphi$ is identified up to conjugacy, yet all Sylow $p$-subgroups are conjugate, so the homomorphism is unique.
    	To find the presentation of the group, we want to find a matrix $x$ such that $x^7 - 1 = 0$. In $\mathbb{Z}_2$ it factors as $(x + 1) (x^3 + x + 1) (x^3 + x^2 + 1)$, the third term can be seen as $x^3 + x^2 + 1 \equiv -x^3 + x^2 + 1 = -x\cdot -x(-x+1) + 1$ and can be seen as the characteristic polynomial of $\begin{pmatrix} 0&0&1\\1&1&0\\0&1&0 \end{pmatrix}$. If we use the standard basis $a,b,c = e_1, e_2, e_3$, then $xa = b$, $xb = b+c$ and $xc = a$. So we have the presentation $$\begin{aligned}\langle a,b,c,d &| a^2 = b^2 = c^2 = d^7 = 1, \\ & ab = ba, ac = ca, bc = cb, dad^{-1} = b, dbd^{-1} = bc, dcd^{-1} = a \rangle\end{aligned}.$$

    ## Exercise 8

    **Prove that group of order $144$ is not simple**.

    Proof

    $| G | = 144 = 2^4 \cdot 3^2$. Since $n_3 | 16$ and $n_3 \equiv 1 \pmod{3}$, we must have $n_3 = 4$ or $16$. It cannot be $4$, because $144 > 4!$. Assume $G$ is simple, we must have $n_3 = 16$.

    All Sylow $3$-subgroups must intersect trivially or have $3$ elements in the intersection (by Lagrange). Suppose all of them intersect trivially, then there are $8\cdot 16$ elements of order $3$, and $16$ elements of other orders, which must be the unique Sylow $2$-subgroup, thus $G$ is not simple.

    Otherwise there are some $S,T \in Syl_3(G)$ such that $| S \cap T | = 3$, it follows that $S \cap T$ is normal subgroup of both $S$ and $T$ thus $S,T \le N_G(S \cap T) = H$, but then $ST \subseteq H$ (not subgroup), so $| H | \ge 27$ by $| ST | = | S \| T | / | S \cap T |$. Also we know $| H |$ divides $144$, but then either $H = G$, so that $G$ has a normal subgroup $S \cap T$, or $[G:H]\le 5$, but $144 > 5!$, so $G$ is not simple in any case.

    """
    )
    return


if __name__ == "__main__":
    app.run()
