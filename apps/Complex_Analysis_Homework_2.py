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

    **Let $f \in H(V)$ and $| f | =$ constant. Show that $f$ is a constant function**.

    Proof

    Suppose $f = u + iv$, then $| f | = (u + iv)(u - iv) = (u u + v v) + i(-u v + u v) = u^2 + v^2$, by assumption, is some constant.

    Take the derivative of $u^2 + v^2 =$ constant with respect to $x, y$ both side then: $$\begin{cases} u_xu+v_xv = 0 \\ u_y u + v_y v = 0 \end{cases}.$$ Since $f \in H(V)$ clearly it has to satisfy the Cauchy-Riemann Equation, thus we can rewrite the above two equations as: $$\begin{cases} u_x u - u_y v = 0 \\ u_xv+u_yu = 0 \end{cases}.$$ Which is the same as: $$\begin{bmatrix} u & -v \\ v & u \end{bmatrix} \begin{bmatrix} u_x \\ u_y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}.$$ Then $\det(\begin{bmatrix} u & -v \\ v & u \end{bmatrix}) = u^2 + v^2$.

    If $u^2 + v^2 = 0$ then $f = 0$ is clearly constant.

    If else then the matrix has non-zero determinant, then the two vectors $(u, v)$ and $(-v, u)$ are linearly independent. Thus $u_x, u_y$ thus $u_x, u_y, v_x, v_y$ all zero, thus $f$ is a constant.

    ## Exercise 2

    **Use Cauchy's Theorem 2.7 to evaluate $\int_{0}^{\infty} e^{-x^2} \cos((2 b x))dx$**.

    Solution

    Denote this integral as $I$ for convenience. $e^{-x^2} \cos((2 b x))$ is an even function. Thus $I = \frac{1}{2} \int_{- \infty}^{\infty} e^{-x^2} \cos((2 b x))dx$. Since $e^{i z} = \cos(z) + i \sin(z)$, $\cos(z) = \text{re}(e^{i z})$ and sine is the imaginary part. $I = \frac{1}{2} \int_{- \infty}^{\infty}e^{-x^2}\text{re}(e^{i 2 b x})dx = \text{re}(\frac{1}{2} \int_{- \infty}^{\infty}e^{-x^2+i 2 b x}dx)$. Thus $I + i \text{im}(\frac{1}{2} \int_{- \infty}^{\infty}e^{-x^2+i 2 b x}dx)$ $= \frac{1}{2} \int_{- \infty}^{\infty}e^{-x^2+i 2 b x}dx$ $= \frac{1}{2} \int_{- \infty}^{\infty}e^{-(x-ib)^2-b^2}dx$ $=e^{-b^2}/2 \int_{- \infty}^{\infty}e^{-(x-ib)^2}dx$. Consider $f(z) = e^{-z^2}$ which is entire, by Cauchy' Theorem 2.7 $\int_{\gamma}f(z)dz = 0$ for smooth closed $\gamma$. So consider the (oriented) square $\gamma = \gamma_1 + \gamma_2 + \gamma_3 + \gamma_4$, where $\gamma_1 = x, x \in [a, -a]$, $\gamma_2 = -a+iy, y \in [0,-b]$, $\gamma_3 = x - ib, x \in [-a, a]$, and $\gamma_4 = a + iy, y \in [-b, 0]$. Then $\int_{\gamma_1}f(z)dz + \int_{\gamma_2}f(z)dz + \int_{\gamma_3}f(z)dz + \int_{\gamma_4}f(z)dz = 0$.

    Back to the above equation, we have $\int_{- \infty}^{\infty}e^{-(x-ib)^2}dx = \lim\limits_{a \rightarrow \infty} \int_{-a}^{a}e^{-(x-ib)^2}dx = \lim\limits_{a \rightarrow \infty} \int_{-a}^{a}e^{-(x-ib)^2} \cdot 1 dx$ $= \lim\limits_{a \rightarrow \infty} \int_{-a}^{a}f(\gamma_3(x)) \gamma_3'(x)dx$ $= \lim\limits_{a \rightarrow \infty} \int_{\gamma_3}e^{-z^2}dz$; So similarly, $\int_{a}^{-a}e^{-x^2}dx = \int_{\gamma_1}e^{-z^2}dz$; $\int_{0}^{-b}e^{-(-a+i y)^2}i dy = \int_{\gamma_2}e^{-z^2}dz$; $\int_{-b}^{0}e^{-(a+i y)^2}i dy = \int_{\gamma_4}e^{-z^2}dz$.

    Yet for $\gamma_2$, $\int_{0}^{-b}e^{-(-a+i y)^2}i dy = \int_{0}^{-b}e^{-a^2+y^2+2i a y}i dy$, take absolute value to vanish the imaginary part to get $\int_{0}^{-b} | e^{-a^2+y^2+2i a y}i | dy= \int_{0}^{-b}e^{-a^2+y^2}dy$ $= e^{-a^2} \int_{0}^{-b}e^{y^2}dy \le e^{-a^2} \int_{0}^{-b}e^{b^2}dy = \frac{-be^{b^2}}{e^{a^2}} =^{a \rightarrow \infty} 0$. Similar to $\gamma_4$.

    So we have $\lim\limits_{a \rightarrow \infty}(\int_{\gamma_1}f(z)dz + \int_{\gamma_3}f(z)dz)= 0$:

    $\lim\limits_{a \rightarrow \infty} (\int_{a}^{-a}e^{-x^2}dx + \int_{-a}^{a}e^{-(x-ib)^2}dx)$ $= \lim\limits_{a \rightarrow \infty} \int_{a}^{-a}e^{-x^2}dx + (I + i \text{im}(\frac{1}{2} \int_{- \infty}^{\infty}e^{-x^2+i2 b x}dx)) \frac{2}{e^{-b^2}}$ $= 0 \implies I + i \text{im}(\frac{1}{2} \int_{- \infty}^{\infty}e^{-x^2+i2 b x}dx) = \frac{e^{-b^2}}{2} \lim\limits_{a \rightarrow \infty} \int_{-a}^{a}e^{-x^2}dx = \frac{e^{-b^2}}{2} \sqrt{\pi}$ which is the Gaussian integral.

    Finally notice that sine is odd so that the imaginary part is actually just $0$, so we have $I = \frac{e^{-b^2}}{2} \sqrt{\pi}$.

    ## Exercise 3

    **Prove that $\zeta(z)= \sum\limits_{n = 1}^{\infty} \frac{1}{n^z}$ does not converge uniformly on $V = \lbrace z | \text{re}(z) > 1 \rbrace$**.

    Proof

    Prove by a counter example.

    Take $k = 2N$ and $z = 1 + \frac{1}{k}$, then $| \sum\limits_{n = 1}^{k} \frac{1}{n^z} - \sum\limits_{n = 1}^{N} \frac{1}{n^z} | = | \sum\limits_{n = 1}^{2N} \frac{1}{n^{1 + 1/(2N)}} - \sum\limits_{n = 1}^{N} \frac{1}{n^{1 + 1/(2N)}} |$ $= \sum\limits_{n = N+1}^{2N} \frac{1}{n^{1 + 1/(2N)}} > \sum\limits_{n = N + 1}^{2N} \frac{1}{(2N)^{1 + 1/(2N)}} = \frac{N}{(2N)^{1 + 1/(2N)}}$ goes to $\frac{N}{2N} = \frac{1}{2}$ and have a local minimum $\frac{e^{-1/e}}{2}$.

    So if we take $\varepsilon = \frac{e^{-1/e}}{2}$, this contradict the definition of uniformly convergence.

    ## Exercise 4

    **Big Picard Theorem says that if $f' \in H(D'(z_0, r))$ has an essential singularity at $z_0$, then with at most one exception it attains every complex value infinitely many times in every neighborhood of $z_0$. Verify this statement for $f(z) = e^{1/z}$ and $z_0 = 0$**.

    Proof

    $f(z) = e^{1/z} = \sum\limits_{n = 0}^{\infty} \frac{(1/z)^n}{n!} = \sum\limits_{n = 0}^{\infty} \frac{1}{n!}(1/z)^n$ it is clear that $f(z) \ne 0, \forall z$.

    If $f(z) = e^{1/z} = x, x \in \mathbb{C} - \lbrace 0 \rbrace$, then $1/z = \log(x)$, write $x$ in the form $re^{it}$, $1/z = \log(re^{it})$, $z = \frac{1}{\log(re^{it})}$ $= \frac{1}{\log(re^{i(t + 2n \pi)})}$ $= \frac{1}{\log(r)+ \log(e^{it})+ \log(e^{2n \pi})}$ $= \frac{1}{\log(r)+it+i2n \pi}, \forall n \in \mathbb{Z}$.

    Thus it is clear that for every given radius, if we take large enough $n$, $z$ in the above form is the solution for $e^{1/z} = re^{it}, \forall re^{it} \in \mathbb{C} - \lbrace 0 \rbrace$ which lies inside the neighborhood of $z_0 = 0$.

    For example, $z = \frac{1}{\log(5)+i2} \approx 0.24 - i 0.3,$ $\frac{1}{\log(5)+i2+i2 \pi} \approx 0.02 - i 0.11,$ $\frac{1}{\log(5)+i2+i20 \pi} \approx 0.0004 - i 0.015, \cdots$ are all solutions for $e^{1/z} = 5e^{i2}$.

    ## Exercise 2.1

    **Define $f: \mathbb{C} \rightarrow \mathbb{C}$ by $f(z) = z^2 \sin(1/z)$ for $z \ne 0,f(0)=0$. The last few paragraphs almost seem to give a proof that $f$ is differentiable everywhere but $f'$ is not continuous at the origin. This is impossible - where does the 'proof' fail**?

    Solution

    The step that $| \frac{h^2 \sin(1/h)}{h} | \le | h |$ requires that $-1 \le \sin(z) \le 1, \forall z$, however this is not true in $\mathbb{C}$, indeed it could be a totally random number.

    $| \sin(z) | = | \frac{\exp(iz) - \exp(-iz)}{2i} |$ so for example $| \sin(2i) | = | \frac{\exp(-2) - \exp(2)}{2i} | \approx | \frac{-7.3}{2i} | = 3.65 > 1$.

    ## Exercise 2.5

    **Let $V = \mathbb{C} - \lbrace 0 \rbrace$, and define $f: V \rightarrow \mathbb{C}$ by $f(z) = 1/z$. Then $\int_{\partial T}f(z)dz = 0$ for every triangle $T \subseteq V$ but there does not exist $F: V \rightarrow \mathbb{C}$ such that $F' = f$ in $V$**.

    Proof

    Clearly $V$ is open, for any $z \in V$, by construction $z \ne 0$, thus $\lim\limits_{h \rightarrow 0} \frac{f(z+h) - f(z)}{h} = \lim\limits_{h \rightarrow 0} \frac{\frac{1}{z+h} - \frac{1}{z}}{h} = \lim\limits_{h \rightarrow 0} \frac{\frac{-h}{z(z+h)}}{h} = \lim\limits_{h \rightarrow 0} \frac{-1}{z^2 + zh} = - \frac{1}{z^2}$ exists. I.e. $f$ differentiable everywhere in $V$. Thus by Cauchy-Goursat $\int_{\partial T}f(z)dz = 0$ for every triangle $T \subseteq V$.

    Now suppose $F$ described in the statement exists. Let $\gamma: [0, 2 \pi] \rightarrow \mathbb{C}$ be the boundary of the unit disk, $\gamma(t) = e^{it}$.

    Then by Lemma 2.0, $\int_{\gamma}f(z)dz = 0$; yet by calculate the integral by definition, $\int_{\gamma}f(z)dz = \int_0^{2 \pi} \frac{1}{e^{it}}(e^{it})' dt = \int_0^{2 \pi} i dt = 2 \pi i$ which is a contradiction, thus such $F$ does not exist.

    ## Exercise 3.4

    **Suppose that $f \in H(\mathbb{C})$ and $| f(z) | \le e^{\text{re}(z)}$ for all $z$. Show that $f(z) = c e^z$ for some constant $c$**.

    Proof

    If $| f(z) | \le e^{\text{re}(z)}$ then $\frac{| f(z) |}{e^{\text{re}(z)}} \le 1$ where $\frac{| f(z) |}{e^{\text{re}(z)}} = \frac{| f(z) |}{| e^z |} = | \frac{f(z)}{e^z} |$, thus $\frac{f(z)}{e^z}$ is bounded, clearly it is entire, thus by Corollary 3.6 Liouville's Theorem $\frac{f(z)}{e^z} = c$ for some constant $c$ thus $f(z) = c e^z$.

    ## Exercise 3.7

    **Suppose that $f \in H(\mathbb{C})$ and $f(n) = 0$ for all $n \in \mathbb{Z}$. Show that all the singularities of $f(z)/ \sin(\pi z)$ are removable**.

    Proof

    Since $f$ itself is entire, the singularities occur where $\sin(\pi z) = 0$.

    We have $\sin(\pi z) = \frac{\exp(i \pi z) - \exp(-i \pi z)}{2i}$ thus it is $0$ when $\exp(i \pi z) = \exp(-i \pi z)$. By the Appendix 3 this equality holds when $z = 0, \pm 1, \pm 2, \cdots$, i.e. $z \in \mathbb{Z}$.

    Let $g(z) = \sin(\pi z)$ then for real $z$'s simply $g'(z) = \pi \cos(\pi z) = \pi$ for $z \in \mathbb{Z}$ from calculus. Thus $g$ has zero of order $1$ at $z \in \mathbb{Z}$. Since $f(z) = 0$ for $z \in \mathbb{Z}$, $f$ has zero of order at least $1$ at $z \in \mathbb{Z}$. By the previous exercise $f/g$ has removable singularities at $z \in \mathbb{Z}$.

    ## Exercise 3.11

    **Let $V = \mathbb{C} - \lbrace 0 \rbrace$. Show that there does not exist $f \in H(V)$ such that $e^{f(z)} = z$ for all $z \in V$**.

    Proof

    Suppose such $f$ exists. Then for $z \in V$, $e^{f(z)} = z$, take derivatives each side we have $e^{f(z)}f'(z) = z' = 1$. Thus $f'(z) = \frac{1}{e^{f(z)}} = \frac{1}{z}$. Think $f'$ as a function with $(f') = f'$ then we can apply Cauchy's Theorem of derivatives.

    Let $\gamma: [0, 2 \pi] \rightarrow \mathbb{C}$ be the boundary of the unit disk, $\gamma(t) = e^{it}$. Then by Lemma 2.0, $\int_{\gamma}f'(z)dz = 0$; yet by calculate the integral by definition $\int_{\gamma}f'(z)dz = 2 \pi i$, which is a contradiction and thus such $f$ does not exist.

    ## Exercise 3.12

    **Suppose that $V$ is a bounded open subset of the plane and $f \in C(\overline{V}) \cap H(V)$. Show that if $M \ge 0$ and $| f(z) | \le M$ for all $z \in \partial V$ then $| f(z) | \le M$ for all $z \in V$**.

    Proof

    Since $f \in C(\overline{V})$, $\overline{V}$ (and $V$) is connected. Then by the Maximum Modulus Theorem either $f$ constant (thus clearly $| f(z) | \le M$ for all $z \in V$) or $| f |$ achieve absolute maximum on the boundary of $V$. Since by construct the value of $| f |$ on the boundary of $V$ is bounded by $M$, the value of $| f |$ inside $V$ is thus also bounded by $M$.

    ## Exercise 3.13

    **Let $V = D(0, 1)$. Suppose that $f \in C(\overline{V}) \cap H(V)$, $f(0) = 0$ and $| f(z) | \le 1$ for all $z \in \overline{V}$. Show that $| f(z) | \le | z |$ for all $z \in V$**.

    Proof

    Let $g(z) = f(z)/z$. Since $f \in H(V)$, the only singularity of $g$ may occur at $z = 0$. Since $f(0) = 0$ thus $f$ has a zero of order at least $1$ at $0$; $z = 0$, $z' = 1$ thus $z$ has a zero of order $1$ at $0$, thus by Exercise 3.6 $f(z)/z$ has a removable singularity at $0$.

    $| f(z) | \le 1$ for all $z \in \overline{V}$ then $| f(z) | \le 1$ for all $z \in \partial V$. Since $V$ is the unit disk, $| z | = 1$ for $z \in \partial V$. Thus $| g(z) | = | \frac{f(z)}{z} | \le 1$ for $z \in \partial V$. By Exercise 3.12, $| g(z) | = | \frac{f(z)}{z} | \le 1$ thus $| f(z) | \le | z |$ also for $z \in V$.

    ## Exercise 4.10

    **Show that $\int_{- \infty}^{+ \infty} \frac{dx}{1+x^2} = \pi$, using the Residue Theorem**.

    Proof

    Let $R > 1$, $\Gamma = \gamma_1 + \gamma_2$ where $\gamma_1 = [-R, R]$ and $\gamma_2:[0, \pi] \rightarrow \mathbb{C}$ given by $\gamma_2(t) = Re^{it}$. Let $f(z) = \frac{1}{1+z^2}$, then $f$ has isolated singularities when $1 + z^2 = 0$ thus at $z^2 = -1, z = \pm i$. Graphically $\Gamma$ is an upper half circle with radius $R$, thus $Ind(\Gamma, a)$ is clearly $0$ for any $a$ such that $\text{im}(a) < 0$. To make it a little bit clearer let $V = \lbrace z | \text{im}(z) > -2 \rbrace$. Then $V \subseteq \mathbb{C}$ is open, $S = \lbrace -i, i \rbrace$ is closed in $V$. By the Residue Theorem we have: $\frac{1}{2 \pi i} \int_{\Gamma}f(z)dz = \sum\limits_{z \in S}Ind(\Gamma, z)Res(f, z)$.

    Righthand-side $= Ind(\Gamma, i)Res(f, i) + Ind(\Gamma, -i)Res(f, -i)$ $= Ind(\Gamma, i)Res(f, i)$ $= Res(f, i)$ because graphically we can easily tell $Ind(\Gamma, i) = 1$ and $Ind(\Gamma, -i) = 0$. $f = \frac{1}{z - i} \cdot \frac{1}{z + i}$, thus $z = i$ is a simple pole for $f$ as the Laurent expansion has $N = 1$, thus $Res(f, i) = Res(\frac{1}{1+z^2}, i) = \frac{1}{(1 + z^2)'} = \frac{1}{2z} = \frac{1}{2 i}$. Thus $\int_{\Gamma}f(z)dz = 2 \pi i \frac{1}{2 i} = \pi$.

    Now $\gamma_1$ is simply an inclusion map, we have $\int_{\Gamma}f(z)dz$ $= \lim\limits_{R \rightarrow \infty} \int_{\Gamma}f(z)dz$ $= \lim\limits_{R \rightarrow \infty}(\int_{\gamma_1}f(z)dz + \int_{\gamma_2}f(z)dz)$ $= \lim\limits_{R \rightarrow \infty}(\int_{-R}^{+R} \frac{1}{1+z^2}z' dz$ $+i \int_{0}^{\pi} \frac{1}{1+(Re^{it})^2}Re^{it}dt)$ $= \int_{- \infty}^{+ \infty} \frac{dz}{1+z^2}$. Thus we have $\int_{- \infty}^{+ \infty} \frac{dx}{1+x^2} = \pi$.

    ## Exercise 4.12

    **Suppose that $f \in H(A(z_0, r, R))$ has Laurent series $f(z) = \sum\limits_{n = - \infty}^{+ \infty}c_n(z - z_0)^n$. Show that $\frac{1}{2 \pi} \int_{0}^{2 \pi} | f(z_0 + \rho e^{it}) |^2 dt = \sum\limits_{n = - \infty}^{+ \infty} \rho^{2n} | c_n |^2$ for $r < \rho < R$**.

    Proof

    Let $s_N(z) = \sum\limits_{n = -N}^{N}c_n(z - z_0)^n$.

    Then $$\begin{aligned}\frac{1}{2 \pi} \int_{0}^{2 \pi} | s_N(z_0 + \rho e^{it}) |^2 dt &= \frac{1}{2 \pi} \int_{0}^{2 \pi} \sum\limits_{n = -N}^{N}c_n \rho^n e^{int} \overline{\sum\limits_{m = -N}^{N} c_m \rho^m e^{i m t}} dt \\ &= \sum\limits_{n, m = -N}^{N}c_n \overline{c_m} \rho^{n+m} \frac{1}{2 \pi} \int_{0}^{2 \pi}e^{i (n-m) t} dt \\ &= \sum\limits_{n = -N}^{N} | c_n |^2 \rho^{2n}.\end{aligned}$$ And we have $$\begin{aligned}\frac{1}{2 \pi} \int_{0}^{2 \pi} | f(z_0 + \rho e^{it}) |^2 dt &= \lim\limits_{N \rightarrow \infty} \frac{1}{2 \pi} \int_{0}^{2 \pi} | s_N(z_0 + \rho e^{it}) |^2 dt \\ &= \lim\limits_{N \rightarrow \infty} \sum\limits_{n = -N}^{N} | c_n |^2 \rho^{2n} \\&= \sum\limits_{n = - \infty}^{+ \infty} \rho^{2n} | c_n |^2.\end{aligned}$$

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

    **Let $f(z) = \frac{1}{z^2 \sin(z)}$**.

    1. **Write down the principal part of the Laurent series for $f(z)$ near the pole $z_0 = 0$. What is the order of this pole and the residue $Res(f, 0)$**?
    2. **Evaluate $\frac{1}{2 \pi i} \int_{\gamma} \frac{dw}{\sin(\frac{1}{w})}$, where $\gamma$ is the circle $| w | = \frac{1}{5}$, positively oriented**.

    Solution

    1. Near the pole $z = 0$: Taylor expansion of $\sin(z) = z - \frac{z^3}{6} + \frac{z^5}{120} - \frac{z^7}{5040} + O(z^8)$; expansion of $\frac{1}{\sin(z)} = \frac{1}{z - \frac{z^3}{6} + \frac{z^5}{120} - \frac{z^7}{5040} + O(z^8)} = \frac{1}{z} + \frac{z}{6} + \frac{7z^3}{360} + \frac{31z^5}{15120} + O(z^7)$; expansion of $f(z) = \frac{1}{z^3} + \frac{1}{6z} + \frac{7z}{360} + \frac{31z^3}{15120} + O(z^5)$; so principle part is $\frac{1}{z^3} + \frac{1}{6z}$.
    	This is a pole of order $3$, and residue is $\frac{1}{6}$;
    2. Substitute $z = \frac{1}{w}$ then $\frac{1}{2 \pi i} \int_{| w = 1/5 |} \frac{dw}{\sin(\frac{1}{w})} = - \frac{1}{2 \pi i} \int_{| z = 5 |} \frac{dz}{z^2 \sin(z)}$.
    	Inside the curve we have $f(z) = \frac{1}{z^2 \sin(z)}$ has three poles: two simple poles at $z = \pm \pi$ with residue $- \frac{1}{\pi^2}$, and a pole of order $3$ at $0$ with residue $\frac{1}{6}$.
    	Winding numbers at these poles are clearly 1.
    	Thus by Residue Theorem $- \frac{1}{2 \pi i} \int_{| z = 5 |} \frac{dz}{z^2 \sin(z)} = -(- \frac{2}{\pi^2} + \frac{1}{6}) = \frac{2}{\pi^2} - \frac{1}{6}$.

    ## Exercise 2

    **Let $a > 0, a \ne 2$. Evaluate $\int_{\gamma_a} \frac{z^2+e^z}{z^2(z - 2)}dz$, where $\gamma_a$ is the positively oriented circle $| z | = a$**.

    Solution

    $f(z) = \frac{z^2+e^z}{z^2(z - 2)}$ has simple pole at $z = 2$ with residue $1 + \frac{1}{4}e^2$ and pole of order $2$ at $0$ with residue $- \frac{3}{4}$. By Residue Theorem, if $0 < a < 2$ then $\int_{\gamma_a} \frac{z^2+e^z}{z^2(z - 2)}dz = 2 \pi i \cdot - \frac{3}{4} = - \frac{3 \pi i}{2}$, otherwise $\int_{\gamma_a} \frac{z^2+e^z}{z^2(z - 2)}dz$ $= 2 \pi i \cdot (- \frac{3}{4} + 1 + \frac{1}{4}e^2)$ $= \frac{\pi i}{2}(1 + e^2)$.

    ## Exercise 3

    **Evaluate $\int_0^{\infty} \frac{\sin^2(x)}{x^2}dx$ (Try $f(z) = \frac{1 - e^{2 i z}}{z^2}$, what kind of singularity does $f(z)$ have at zero?)**.

    Solution

    ***(Note that generally do not use such $\Gamma_3$, try to use the upper half circle, because weird thing can happen at $0$.)***

    By the hint, notice that $\sin^2(x) = \frac{1}{2}\text{re}(1 - e^{2 i x})$, thus $\int_0^{\infty} \frac{\sin^2(x)}{x^2}dx = \frac{1}{2} \int_{0}^{\infty} \frac{1 - e^{2 i x}}{x^2}dx = \frac{1}{4} \int_{- \infty}^{\infty} \frac{1 - e^{2 i x}}{x^2} dx$ (because it's even).

    $f(x) = \frac{1 - e^{2 i x}}{x^2}$ has a simple pole at $x = 0$ with residue $-2 i$. Then take the graph $\Gamma = \Gamma_1 + \Gamma_2 + \Gamma_3$ where $\Gamma_1$ being the upper-half of the counter-clockwise circle with radius $R$, $\Gamma_3$ being the upper-half of the counter-clockwise circle with radius $r$, and $\Gamma_2$ being the two connecting segments that respect the orientations.

    Then $\lim\limits_{R \rightarrow \infty, r \rightarrow 0} \int_{\Gamma} \frac{1 - e^{2 i x}}{x^2} dx$ $= 2 \pi i \cdot (- 2 i) = 4 \pi$ $= \lim\limits_{R \rightarrow \infty, r \rightarrow 0} (\int_{\Gamma_1} \frac{1 - e^{2 i x}}{x^2} dx + \int_{\Gamma_2} \frac{1 - e^{2 i x}}{x^2} dx + \int_{\Gamma_3} \frac{1 - e^{2 i x}}{x^2} dx)$. The integrant over $\Gamma_1$ goes to $0$; the integrant over $\Gamma_2$ is what we need; the integrant over $\Gamma_3$ is $\pi i \cdot (- 2 i) = 2 \pi$. Thus the integrant over $\Gamma_2$ goes to $2 \pi$, the origin integrant is one fourth of it thus is $\frac{\pi}{2}$.

    ## Exercise 4

    **Evaluate $\int_0^{\infty} \frac{\cos(n x)}{x^4+1}dx$**.

    Solution

    ***(The following writing is WRONG! One has to try to use $e^{n z}$ to replace cosine, otherwise ML does not work!)***

    Clearly for each $n$ we have $f(z) = \frac{\cos(n z)}{z^4 + 1}$ has $4$ simple poles at the four solutions $z^4 + 1= 0, z = e^{\frac{\pi}{4} + n \frac{\pi}{2} i}, n = 0, 1, 2, 3$, each would have residue $- \frac{z}{4} \cos(n z)$.

    For each $n$, $f$ is even thus $\int_0^{\infty} \frac{\cos(n x)}{x^4+1}dx = \frac{1}{2} \int_{- \infty}^{\infty} \frac{\cos(n x)}{x^4+1}dx$, with the usual method, take the half circle and the horizontal line, we have it $= \lim\limits_{R \rightarrow \infty} \frac{1}{2} \int_{\Gamma} \frac{\cos(n x)}{x^4+1}dx = \pi i (Res(f(z), z = e^{\pi i/4}) + Res(f(z), z = e^{3 \pi i/4}))$ $= \pi i(- \frac{1}{4}e^{\pi i/4} \cos(n e^{\pi i/4}) - \frac{1}{4}e^{3 \pi i/4} \cos(n e^{3 \pi i/4}))$.

    ## Exercise 4.21

    **Suppose that $P(z)$ is a polynomial of degree $n \ge 2$ with $n$ distinct zeros $z_1, \dots, z_n$. Explain why it follows that every zero of $P$ is simple, and show that $\sum\limits_{j = 1}^n \frac{1}{P'(z_j)} = 0$**.

    Solution

    By Fundamental Theorem of Algebra we have $P(z) = a_n \prod\limits_{j = 1}^n (z - z_j)$, if we expand the product it is then clear to see that $P'(z)$ at zeros' are not $0$, i.e. every zero is simple.

    Thus we have $Res(\frac{1}{P(z)}, z) = \frac{1}{P'(z)}$.

    Then $\sum\limits_{j = 1}^n \frac{1}{P'(z_j)} = \sum\limits_{j = 1}^n Res(\frac{1}{P(z)}, z_j)$, let's take $\Gamma$ to be the circle centered at $0$ with radius $R$, where $R$ is large enough for the circle to cover all $z_j$'s (we can do that because there are only finite of them), then we continue the above equation $= \frac{1}{2 \pi i} \int_{\Gamma} \frac{dz}{P(z)} \overset{\text{def}}{=} \frac{1}{2 \pi i} \int_0^1 \frac{(R e^{2 \pi i t})'}{P(R e^{2 \pi i t})}dt = \int_0^1 \frac{R e^{2 \pi i t}}{P(R e^{2 \pi i t})}dt = \int_0^1 \frac{R e^{2 \pi i t}}{a_n \prod\limits_{j = 1}^n (R e^{2 \pi i t} - z_j)}dt$.

    Take absolute sign we have $| \int_0^1 \frac{R e^{2 \pi i t}}{a_n \prod\limits_{j = 1}^n (R e^{2 \pi i t} - z_j)}dt |$ $\le | \frac{R}{a_n} | \int_0^1 \frac{1}{\prod\limits_{j = 1}^n | R e^{2 \pi i t} - z_j |}dt$ $= | \frac{1}{R^{n - 1} a_n} | \int_0^1 \frac{1}{\prod\limits_{j = 1}^n | 1 - \frac{z_j}{R e^{2 \pi i t}} |}dt$. For fixed $z_j$'s, $R$ can arbitrarily large, take $R \rightarrow \infty$, then the function inside the integral goes to constant $1$, thus $| \sum\limits_{j = 1}^n \frac{1}{P'(z_j)} | \le | \frac{1}{R^{n - 1} a_n} |$ ($\rightarrow 0$), i.e. $\sum\limits_{j = 1}^n \frac{1}{P'(z_j)} = 0$.

    ## Exercise 5.3

    **Determine the number of zeros of $f(z) = 1 + 6z^3 + 3z^{10} + z^{11}$ in the annulus $A(0, 1, 2)$**.

    Solution

    First, it is easy to see that there is no zero on the boundaries of the annulus;

    Second we count the number of zeros in $D(0, 2)$: take $g(z) = z^{11} + 3z^{10}$, then $| f(z) - g(z) | < | g(z) |$ on $| z | = 2$. Notice that one zero of $g$ is $-3$ not in the disk thus there are $10$ zeros in the disk; (Here $g = z^{11}$ fails because take $z = -2$ then $| 1 + 6z^3 + 3z^{10} | = | 1 + 6z^3 + 3z^{10} + z^{11} | + | z^{11} |$) then we count the number of zeros in $D(0, 1)$: take $g(z) = 6z^3$ then again $| f(z) - g(z) | < | g(z) |$. There are $3$ zeros in the disk.

    Thus in conclusion there are $10 - 3 = 7$ zeros in the annulus.

    ## Exercise 5.6

    **Prove Hurwitz's Theorem: Suppose that $D$ is an open set, $f_n \in H(D), f_n \rightarrow f$ uniformly on compact subsets of $D, \overline{D(z, r)} \subseteq D$, and $f$ has no zero on $\partial D(z, r)$. Then there exists $N$ such that $f_n$ and $f$ have the same number of zeros in $D(z, r)$ for all $n > N$**.

    Proof

    By construction $f \in H(D)$ thus $f \in H(\overline{D(z, r)})$. $\partial D(z, r)$ is clearly compact, thus $f(\partial D(z, r))$ is compact. Now $f$ achieves no zero on $\partial D(z, r)$, in other word $| f(\partial D(z, r)) | > 0$, since it is compact (closed), $| f(\partial D(z, r)) | \ge \varepsilon$ for some $\varepsilon > 0$.

    Now by definition, if a sequence of functions $f_n$ converges uniformly to $f$ then for the above $\varepsilon > 0$, $\exists N$ such that $\forall n > N$, $| f_n(z) - f(z) | < \varepsilon \le | f(z) |$ (on $\partial D(z, r)$).

    By Rouche's Theorem, $f_n$ and $f$ have the same number of zeros for all $n > N$.

    ## Exercise 6.6

    **Find $\sum\limits_{n = 1}^{\infty} \frac{1}{n^2}$, using the infinite series for $\cot(\pi z)$**.

    Solution

    The infinite series for $\cot(\pi z)$ is given by $\pi \cot(\pi z) = \frac{1}{z} + \sum\limits_{n =1}^{\infty}(\frac{1}{z-n} + \frac{1}{z+n})$. The term $\frac{1}{z-n} + \frac{1}{z+n} = \frac{2 z}{(z - n)(z + n)} = \frac{2 z}{z^2 - n^2}$.

    Then consider $\sum\limits_{n = 1}^{\infty} \frac{1}{n^2 - z^2} = - \sum\limits_{n = 1}^{\infty} \frac{1}{z^2 - n^2} = - \frac{1}{2z} \sum\limits_{n = 1}^{\infty} \frac{2z}{z^2 - n^2} = - \frac{1}{2z} \pi \cot(\pi z) + \frac{1}{2z^2}$ $= \frac{1}{2 z^2} - \frac{\pi}{2 z} \frac{\cos(\pi z)}{\sin(\pi z)} = \frac{1}{2 z^2} - \frac{\pi z}{\sin(\pi z)} \frac{\cos(\pi z)}{2 z^2} = \frac{\pi z}{\sin(\pi z)} \frac{1}{2 z^2}(\frac{\sin(\pi z)}{\pi z} - \cos(\pi z))$, at this point we can just use Taylor expansion $= \frac{\pi z}{\sin(\pi z)} \frac{1}{2 z^2}(\frac{\pi^2 z^2}{3} - \frac{\pi^4 z^4}{30} + \frac{\pi^6 z^6}{840} + O(z^7)) = \frac{\pi z}{\sin(\pi z)} (\frac{\pi^2}{6} - \frac{\pi^4 z^2}{60} + O(z^3))$. Take $\lim\limits_{z \rightarrow 0}$, $\frac{\pi z}{\sin(\pi z)}$ goes to one, and the whole thing $= \frac{\pi^2}{6}$.

    ## Exercise 5

    **Let $1 < \lambda < \infty$, and $f_{\lambda}(z) = z + \lambda - e^z$. Show that this function has only one zero in the left half-plane $V = \lbrace z | \text{re}(z) < 0 \rbrace$, and that this zero is real**.

    Proof

    At a zero, clearly $z + \lambda = e^z$. Take absolute value $| z + \lambda | = | e^z | = e^{\text{re}(z)}$. Now since we work on the left half-plane $e^{\text{re}(z)}$ is $e$ to some negative real power, thus less than $1$. Thus $| z + \lambda | < 1$. For a fixed $\lambda$ this is an open disk of radius $1$ centered at the real line. In other words, if $f_{\lambda}$ has zeros in the left half plane, these zeros also must lie in the disk described above.

    Now we consider the circle $| z+ \lambda | =1$, take $f(z) = z+ \lambda, g(z) = -e^z$, then $| f + g -f | = | g | = e^{\text{re}(z)} < 1 = | z + \lambda | = | f |$, thus $f + g$, which is our original function, and $f$ have the same number of zeros in the circle. $f = z + \lambda$ clearly only has one zero. Thus the original function has only one zero in the disk, thus in the left half plane.

    Suppose the zero is $x + i y$. As stated in the first paragraph, this zero must lie with in some open disk of radius $1$ centered at the real line, thus $| y | < 1$ ($*$).

    Rewrite $z + \lambda = e^z$ as $x + \lambda + i y = e^x \cos(y) + i e^x \sin(y)$, then the imaginary part we have $y = e^x \sin(y)$ (and now we work completely in $\mathbb{R}$). $e^x$ is again smaller than $1$. So to make the equation holds, we have either $y = 0 \implies \sin(y) = 0 \implies 0 = e^x \cdot 0$ clearly true; or we have $e^x = \frac{y}{\sin(y)} < 1$. However, this is impossible given ($*$).

    Thus we must have $y = 0$, in other words, this zero is real.

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

    **The following statement is known as Summation Theorem: Let $f \in H(\mathbb{C} - S)$, where $S = \lbrace p_1, \dots, p_m \rbrace$ is a finite set of isolated singularities. Let $C_N$ be a square with vertices at $(N + 1/2) \times (\pm 1 \pm i)$, and $\int_{C_N}f(z) \cot(\pi z)dz \rightarrow 0$ as $N \rightarrow \infty$. Then $\lim\limits_{N \rightarrow \infty} \sum\limits_{n = -N, n \notin S}^{N}f(n) = - \sum\limits_{k = 1}^{m}Res(\pi f(z) \cot(\pi z), p_k)$**.

    1. **Prove the Summation Theorem**;
    2. **What should you replace $\cot(\pi z)$ with if you wish to evaluate the sum of the alternating series $\sum (-1)^n f(n)$**?

    Proof

    1. For $z \in \mathbb{C - Z}$. $\pi \cot(\pi z) = \frac{1}{z} + \sum\limits_{n =1}^{\infty}(\frac{1}{z-n} + \frac{1}{z+n})$.
    	Thus $\pi \cot(\pi z)$ has isolated singularities at all integers. Thus $\pi f(z) \cot(\pi z)$ has isolated singularities at all integers (well we only interest in those bounded by $\pm N$, let's denote this set $A$) and $p_k$'s, there may be repeat, though:
    	$\int_{C_N} \pi f(z) \cot(\pi z)dz = 2 \pi i (\sum_{z_0 \in S} Res(\pi f(z) \cot(\pi z), z_0) + \sum_{z_0 \notin S, z_0 \in A} Res(\pi f(z) \cot(\pi z), z_0))$.
    	Now for $z_0 \in A, z_0 \notin S$, $z_0$ is a simple pole, thus $Res(\pi f(z) \cot(\pi z), z_0) = \lim_{z \rightarrow z_0}(z - z_0) \pi f(z) \cot(\pi z) =$, we use the above cotangent expansion to have, $= \lim_{z \rightarrow z_0}f(z)(\frac{z - z_0}{z} + \sum_{n = 1}^{\infty} \frac{2z(z - z_0)}{(z - n)(z + n)}) =$, we can see that most of the terms got canceled, $= \lim_{z \rightarrow z_0}f(z) \frac{2z}{z + z_0} = f(z_0)$.
    	Now remember that we have $\int_{C_N}f(z) \cot(\pi z)dz \rightarrow 0 \implies \int_{C_N} \pi f(z) \cot(\pi z)dz \rightarrow 0$, where $\int_{C_N} \pi f(z) \cot(\pi z)dz = 2 \pi i (\sum_{z_0 \in S} Res(\pi f(z) \cot(\pi z), z_0) + \sum_{z_0 \notin S, z_0 \in A} f(z_0)) \rightarrow 0 \implies$ $\sum_{z_0 \in S} Res(\pi f(z) \cot(\pi z), z_0) + \sum_{z_0 \notin S, z_0 \in A} f(z_0) = 0$, which is just a rephrase of the desired statement;
    2. So if we follow the above proof then we may want to have some $g(z)$ such that it has isolated singularities at integers, and $Res(f(z) g(z), z_0) = (-1)^{z_0} f(z_0)$.
    	Then $\pi \csc(\pi z)$ should do the work: the expansion is $\pi \csc(\pi z) = \frac{1}{z} + \sum\limits_{n =1}^{\infty}(\frac{-1^{n}}{z-n} + \frac{-1^n}{z+n})$, and the prove is basically the same.

    ## Exercise 2

    **Use the Summation Theorem to evaluate**:

    1. $\sum\limits_{n = 1}^{\infty} \frac{1}{n^2+4}$;
    2. $\zeta(4)$.

    Solution

    1. $2 \sum\limits_{n = 1}^{\infty} \frac{1}{n^2+4} + \frac{1}{4} = - (Res(\frac{\pi \cot(\pi z)}{z^2 + 4}, -2i) + Res(\frac{\pi \cot(\pi z)}{z^2 + 4}, 2i))$, those are both simple poles and the function is in fractional form so we have $\sum\limits_{n = 1}^{\infty} \frac{1}{n^2+4} = \frac{1}{2}(- \frac{\pi \cot(2 \pi i)}{4 i} - \frac{\pi \cot(- 2 \pi i)}{-4 i} - \frac{1}{4}) \approx 0.66$;
    2. $\zeta(4) = \sum\limits_{n = 1}^{\infty} \frac{1}{n^4} = - \frac{1}{2}Res(\frac{\pi \cot(\pi z)}{z^4}, 0) = \frac{\pi^4}{90}$.

    ## Exercise 3

    **Consider the function $f_n(z) = 1 + \frac{1}{z} + \frac{1}{2!z^2} + \dots + \frac{1}{n!z^n}$**.

    1. **What does the integral $\frac{1}{2 \pi i} \int_{\partial D(0, r)} \frac{f'_n(z)}{f_n(z)}dz$ count**?
    2. **What is the value of this integral for large $n$ and fixed $r$? What does this tell you about the zeros of $f_n(z)$ for large $n$**?

    Solution

    1. $f_n(z)$ is not holomorphic near $0$. Consider $F_n(z) = f_n(\frac{1}{z}) = 1 + z + \frac{z^2}{2!} + \dots + \frac{z^n}{n!}$, then substitute the contour $re^{it} \rightarrow 1/(re^{it}) = \frac{1}{r}e^{it}$ we have a disk of radius $1/r$ with a negative orientation. We have $\frac{1}{2 \pi i} \int_{\partial D(0, r)} \frac{f'_n(z)}{f_n(z)}dz = - \frac{1}{2 \pi i} \int_{\partial D(0, 1/r)} \frac{F'_n(z)}{F_n(z)}dz$.
    	Now $F_n$ is holomorphic on the disk , thus the original integral counts the negative of the number of zeros of $F_n$ inside the disk of radius $1/r$, which is the number of zeros of $f_n$ outside the disk of radius $r$;
    2. We can derive that $f'_n(z) = - \frac{1}{z^2} - \frac{1}{z^3} - \frac{1}{2! z^4} - \dots - \frac{1}{(n-1)!z^{n+1}}$ and thus we can bring $- \frac{1}{z^2}$ out and see that $\lim\limits_{n \rightarrow \infty} \frac{f'_n(z)}{f_n(z)} = - \frac{1}{z^2}$.
    	And we know that $\int_{\partial D(0, r)} \frac{1}{z^2}dz = 0$, so for fixed $r$ and large enough $n$, $f_n(z)$ has no zero outside the disk, i.e. all of its zeros are inside the disk.

    ## Exercise 4

    **Let $V = \lbrace z \in \mathbb{C} \| z | > 1 \rbrace$ and $f \in H(V)$. Suppose $f$ is real valued on $(1, \infty)$. Show that $f$ is also real valued on $(- \infty, -1)$**.

    Proof

    By construction $f$ is holomorphic in the neighborhood of $\infty$, thus we can write it as Laurent expansion at $\infty$: $f(z) = \sum\limits_{i = 1}^{\infty} \frac{c_i}{z^i}$. Let $b_i = \text{re}(c_i)$ and consider $g(z) = \sum\limits_{i = 1}^{\infty} \frac{b_i}{z^i}$, for all $| z | > 1$, $g(z)$ converges because it converges absolutely. For any $x \in \mathbb{R}, x > 1$, $f(x) = \sum\limits_{i = 1}^{\infty} \frac{\text{re}(c_i)}{x^i} + i \sum\limits_{i = 1}^{\infty} \frac{\text{im}(c_i)}{x^i}$, and since $f(x)$ is by assumption real, $f(x) = \sum\limits_{i = 1}^{\infty} \frac{\text{re}(c_i)}{x^i} = g(x)$ (thus also converge).

    Now consider $F(x) = f(x) - g(x)$, it is holomorphic on $V$ as both $f, g$ are. By above we have $F(x) = 0, x > 1$, for any $x' > 1$, $x'$ is a limit point of $Z(F)$, thus $F(x) \equiv 0$ for $x \in V$, thus $f(x) = g(x)$ also for $x < -1$, i.e. $f$ is also real valued on $(- \infty, -1)$.

    ## Exercise 5

    **Let $f \in C(\overline{D(0, 1)})$ and $f(\frac{1}{n}) = \frac{1}{n + 1}$ for $n = 2, 3, \dots$. Show that $f \notin H(D(0, 1))$**.

    Proof

    To have $f(\frac{1}{n}) = \frac{1}{n + 1}$ we need to have $f(z) = \frac{z}{1+z}, z = \frac{1}{n}$. Now consider $g(z) = \frac{z}{1 + z}$, then $f(z) = g(z), \forall z = 1/n, n = 2,3, \dots$. Note that $1/n \rightarrow 0$, so if in case that $f$ is holomorphic, then by Identity Theorem $f(z) = g(z) = \frac{z}{1 + z}$ on $D(0, 1)$, but then clearly this function is not continuous at $-1$, thus $f$ cannot be holomorphic on the open unit disk.

    ## Exercise 24.2

    **Show that the functional equation $\Gamma(z+1) = z \Gamma(z)$ follows immediately from Theorem 24.7**.

    Proof

    $z \Gamma(z) = \lim\limits_{n \rightarrow \infty} \frac{n!n^z z}{z \dots(z+n)} = \lim\limits_{n \rightarrow \infty} \frac{n!n^z}{(z+1) \dots(z+n)} = \lim\limits_{n \rightarrow \infty} \frac{n!n^{z+1}}{(z+1) \dots(z+n)n} =$, since we take $n \rightarrow \infty$ it does not matter to add a 'constant' term to one $n$, thus $= \lim\limits_{n \rightarrow \infty} \frac{n!n^{z+1}}{(z+1) \dots(z+n)(z+n+1)}$ which is exactly $\Gamma(z + 1)$.

    ## Exercise 24.6

    **Deduce from Stirling's formula that in fact $(2n)! \sim \frac{2^{2n}(n!)^2}{\sqrt{\pi n}}$ as $n \rightarrow \infty$**.

    Solution

    $n! \sim \sqrt{2 \pi n} \frac{n^n}{e^n} \implies \frac{2^{2n}(n!)^2}{\sqrt{\pi n}} \sim \frac{\sqrt{2 \pi n}^2}{\sqrt{\pi n}}(\frac{n^{2n}}{e^{2n}})2^{2n} = \sqrt{4 \pi n} \frac{(2n)^{2n}}{e^{2n}} \sim (2n)!$.

    ## Exercise 24.7

    **Deduce the duplication formula directly from Theorem 24.7, using Exercise 24.6 or 24.5**.

    Solution

    First we have $$(2n)!\sim \frac{2^{2n}(n!)^2}{\sqrt{\pi n}} \implies (n!)^2 \sim \frac{(2n!)(\sqrt{\pi n}}{2^{2n}}.$$ Use it, we have $$\begin{aligned} \Gamma(z)\Gamma(z + 1/2)\frac{2^{2z-1}}{\sqrt{\pi}} &= \lim_{n\to \infty} \frac{2^{2z-1}}{\sqrt{\pi}}\frac{n!n^2}{z(z+1)\dots(z+n)}\frac{n!n^{z+\frac{1}{2}}}{(z+\frac{1}{2})\dots(z+\frac{2n+1}{2})} \\ &=\lim \frac{2^{2z-1}}{\sqrt{\pi}}\frac{n^{2z+\frac{1}{2}}(2n)!\sqrt{\pi n}}{2^{2n}z(z+\frac{1}{2})\dots(z+\frac{2n+1}{2})}\\&=\lim\frac{(2n)^{2z+1}(2n)!}{2z(2z+1)\dots(2z+2n+1)}\\&=\lim\frac{n^{2z}n!}{2z(2z+1)\dots(2z+n)}\\&=\Gamma(2z).\end{aligned}$$

    ## Exercise 7.1

    **Show that Theorem 7.5 follows 'immediately' from Theorem 7.6**.

    Proof

    Suppose $f \in H(V)$, one-to-one, and $W = f(V)$. By Open mapping theorem $f$ is an open map thus $W$ is open. For any $w \in W$, there is $v = f^{-1}(w)$, consider $\overline{D(v, r)} \subseteq V$ and $f(D(v, r)) \subseteq W$ containing $w$.

    $f^{-1}(w_0)$ is defined for all $w_0 \in f(D(v, r))$. Let $v_0 \in D(v, r)$, then $(f^{-1})'(w) \overset{\text{def}}{=} \lim\limits_{f(v_0) \rightarrow w} \frac{f^{-1}(f(v_0)) - f^{-1}(w)}{f(v_0) - w} = \lim\limits_{f(v_0) \rightarrow w} \frac{v_0 - v}{f(v_0) - w}$ $= \frac{1}{\lim\limits_{v_0 \rightarrow f^{-1}(w)} \frac{f(v_0) - f(f^{-1}(w))}{v_0 - f^{-1}(w)}} \overset{\text{def}}{=} \frac{1}{f'(f^{-1}(w))}$, which is well-defined since $f$ itself is holomorphic, and thus $f^{-1} \in H(W)$ with valuation as above.

    ## Exercise 6

    **If $f = p/q$ is a rational function, with $p$ and $q$ coprime polynomials, its degree is defined as $deg(f) = \max{(deg(p), deg(q))}$. Let $f: \mathbb{C}_{\infty} \rightarrow \mathbb{C}_{\infty}$ be a rational function of degree $d > 0$**.

    1. **Prove that $f$ attains each value $c \in \mathbb{C}_{\infty}$ exactly $d$ times, counting multiplicities**;
    2. **A point of multiplicity $k > 1$ is often called a branch-point of $f$ of order $k - 1$. Let $f(z) = \frac{z}{z^3 + 2}$. Find all branch points of $f$ on $\mathbb{C}_{\infty}$ and their orders. Don't forget to examine $z = \infty$ and poles of $f$**.

    Proof
	
    1. Let $c \in \mathbb{C}_{\infty}$ be an arbitrary element. $f$ attains $c$ if $f(a) = p(a)/q(a) = c \implies p(a) = c q(a) \implies p(a) - c q(a) = 0$. By construction this should be a polynomial with degree $d$, thus it has $d$, may be repeated, solutions, which in return means $f$ achieves $c$ $d$ times;
    2. At $0$: $z = 0, \infty$ are the solutions, so this is a branch point of order $1$;
    	At $\infty$: it is the solution for $z^3 + 2 = 0, z \ne 0$ and we have $3$ distinct solutions;
    	For any other $c$: we need to solve for $z = cz^3 + 2c \implies z^3 - \frac{1}{c}z + 2 = 0$, which would always have $3$ distinct solutions.
    	So $\infty$ is the only branch point of order $1$.
    	Redo: Note that let $c$ be a solution of $cz = z^3 + 2, c = 3z^2$ (the derivative), then $z$ would also have less than $3$ solutions. For example when $c = 1$, $z = -2, 1$ are solutions and thus $1$ is also a branch point of order 1.
    	Similarly for $c = e^{i \pi 2/3}$ and $e^{i \pi 4/3}$, we can find $z$ at $e^{i \pi 2/3}$ and $e^{i \pi 4/3}$ are also branch points of order 1, notice they coincide with $c$.

    ## Exercise 8.1

    **Show directly (without using any results in Chapters 7 or 8) that an entire function with a pole at $\infty$ must be a polynomial**.

    Proof

    If $f$ is entire, it could be written as a series $f(z) = \sum\limits_{i = 0}^{\infty}a_i z^i$.

    Consider $f(\frac{1}{z})$, then $f(\frac{1}{0}) = f(\infty) = \infty$ since $f$ has pole at infinity, thus $f(\frac{1}{z}) = \sum\limits_{i = 0}^{\infty} \frac{a_i}{z^i}$ has pole at $0$, which means that $a_i = 0$ for all large enough $i$ (greater than the order of the pole).

    Thus $f(z) = \sum\limits_{i = 0}^{N}a_i z^i$ is a polynomial.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Spring Semester Homework 1""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 1

    **Let $D$ be the region inside the disk $D(1,1)$ and outside the disk $\overline{D(1/2,1/2)}$. Construct the conformal equivalence between $D$ and $\Pi^+$**.

    Solution

    $D$ would be something looks like:

    <img src="public/Pasted image 20210903021579.png" width="300" />

    We may map it to $D_1 = \lbrace z | 0<\text{im}(z)<1 \rbrace$ by the map $f_1:D \to D_1, z \mapsto i\frac{1+z}{1-z}$:

    <img src="public/Pasted image 20210903021350.png" width="600" />

    Now expand this area to the upper half plane. $e^z$ would map $\lbrace z | 0<\text{im}(z)<\pi \rbrace$ to $\Pi^+$ so $f_2: D_1 \to \Pi^+, z \mapsto e^{\pi z}$ would do the job:

    <img src="public/Pasted image 20210903021352.png" width="600" />

    Then we may use $f_3: \Pi^+ \to \mathbb{D}, z \mapsto \frac{z-i}{z+i}$, which is in fact the inverse of our $f_1$, to map to upper half plane to the unit circle, composite the three maps and we are done.

    ## Exercise 2

    **Prove that there is no one-to-one conformal map between the punctured disk $A(0,1,0)$ and the annulus $A(0,2,1)$**.

    Proof

    Suppose there exists such $f:A \to B$ where $f$ is conformal (being surjective), $A$ is the punctured disk and $B$ is the annulus.

    By our construction $f$ is bounded, so $0$ is a removable singularity. Extend $f$ and let $f(0) = w$. A conformal map is by definition continuous, thus $w \in \overline{B}$.

    Suppose $w \in \partial B$, then $f(\mathbb{D}) = B \cup \lbrace w \rbrace$ is not open, which contradict open mapping theorem.

    So $w \in B$, since the original $f$ is surjective, $\exists z \in A$ with $f(z) = w$. Choose $U(0)$ and $U(z)$ be disjoint neighborhood of $0$ and $z$, then by open mapping theorem $f(U(0))$ and $f(U(z))$ are open sets containing $w$ and thus there exists $w' \ne w$ in $f(U(0)) \cap f(U(z))$, but this means that there exists $z_0 \in U(0)$ and $z_1 \in U(z)$ with $f(z_0) = w' = f(z_1)$, i.e. $f$ not injective.

    ## Exercise 3

    **Let $f$ be elliptic function of order $m\ge 2$. What are the bounds on the order of the elliptic function $f'$**?

    Solution

    A property of elliptic function is that $m$ equals the sum of orders of poles of $f$. Seeing $f$ as a polynomial and it is easy to see that $f'$ add $1$ order to each pole of $f$. Thus $f'$ must have order between $m+1$ (just one pole of order $m$) and $2m$ ($m$ distinct simple poles).

    ## Exercise 4

    **Let $\zeta(z)$ be the Weierstrass $\zeta$-function of the lattice $\Omega = \mathbb{Z}\omega + \mathbb{Z}\omega'$**.

    1. **Use the definition of $\zeta(z)$ to write the Laurent series for $\zeta$ near $z = 0$ and express it in terms of the Eisenstein sums $s_n = s_n(\omega, \omega')$**.
    2. **Use $1$. to write the Laurent series for $\wp(z)$**.

    Solution

    Let $m = \min{| \omega_k |}$ and $D = \lbrace z \| z | < m \rbrace$ be a neighborhood of $0$. $\zeta(z) \overset{\text{def}}{=} \frac{\sigma'(z)}{\sigma(z)} = \frac{1}{z} + \sum\limits_{k=1}^{\infty}(\frac{1}{z-\omega_k}+\frac{1}{\omega_k}+\frac{z}{\omega_k^2})$, then:

    First, $\frac{1}{\omega_k-z}+\frac{1}{\omega_k}+\frac{z}{\omega_k^2} = \frac{\omega_k^2+\omega_k(z-\omega_k)+z(z-\omega_k)}{\omega_k^2(z-\omega_k)} = \frac{z^2}{\omega_k^2(z-\omega_k)}$. The power in the denominator is $3$ thus $\sum\limits_{k=1}^{\infty}(\frac{1}{z-\omega_k}+\frac{1}{\omega_k}+\frac{z}{\omega_k^2})$ converges absolutely.

    Second, by construction we have $| z/\omega_k | < 1$, thus we can write $\frac{1}{\omega_k - z} = -\frac{1}{\omega_k}\frac{1}{1 - \frac{z}{\omega_k}} = -\frac{1}{\omega_k}\sum\limits_n(\frac{z}{\omega_k})^n = -\frac{1}{\omega_k} - \frac{z}{\omega_k^2}-\frac{z^2}{\omega_k^3}-\dots$, the later sum converges absolutely (on $D$).

    So we can rewrite the sum $\sum\limits_{k=1}^{\infty}(\frac{1}{\omega_k-z}+\frac{1}{\omega_k}+\frac{z}{\omega_k^2})$ as $\sum\limits_{k=1}^{\infty}(\frac{1}{\omega_k}+\frac{z}{\omega_k^2} -\frac{1}{\omega_k} - \frac{z}{\omega_k^2}-\frac{z^2}{\omega_k^3}-\dots)$ $= \sum\limits_{k=1}^{\infty}(-\frac{z^2}{\omega_k^3}-\frac{z^3}{\omega_k^4}-\dots)$ $= - \sum\limits_{k=1}^{\infty}\frac{z^2}{\omega_k^3} - \sum\limits_{k=1}^{\infty}\frac{z^3}{\omega_k^4} - \dots \overset{\text{def}}{=} -s_3z^2-s_4z^3-\dots$. Moreover, $s_i = 0$ for odd $i$ so $=-s_4z^3-s_6z^5-\dots$

    Now $\zeta(z) = \frac{1}{z} -s_4z^3-s_6z^5-\dots$ $= \frac{1}{z} - \sum\limits_{n=2}^{\infty}s_{2n}z^{2n-1}$ is in the form of Laurent expansion around $z = 0$ in terms of Eisenstein sums. We have that $\wp(z) = -\zeta'(z)$, so take derivative term by term we have $\wp(z) = -\frac{1}{z}' + \sum\limits_{n=2}^{\infty}{s_{2n}z^{2n-1}}'$ $=z^{-2}+\sum\limits_{n=2}^{\infty}(2n-1)s_{2n}z^{2n-2}$ is the Laurent expansion around $0$ in terms of Eisenstein sums.

    ## Exercise 5

    **Prove that for $\Omega = \mathbb{Z}\omega+\mathbb{Z}\omega'$, $\wp'(z) = 2 \frac{\sigma(z-\omega/2)\sigma(z-\omega'/2)\sigma(z+\eta/2)}{\sigma^3(z)\sigma(\omega/2)\sigma(\omega'/2)\sigma(-\eta/2)}$ when** $\eta = \omega + \omega'$.

    Proof

    From course material we have $\wp$ has $3$ zeroes at $\omega/2, \omega'/2$ and $\eta/2$ (or, we can choose it as $-\eta/2$ to have sum of zeroes equals sum of poles) and a pole of order $3$ at $0$.

    By the property of sigma function, $\sigma(z+\omega) = -e^{\eta(z+\omega/2)}\sigma(z)$, $\sigma(z+\omega') = -e^{\eta'(z+\omega'/2)}\sigma(z)$, the function on the right hand side $2 \frac{\sigma(z-\omega/2)\sigma(z-\omega'/2)\sigma(z+\eta/2)}{\sigma^3(z)\sigma(\omega/2)\sigma(\omega'/2)\sigma(-\eta/2)}$ is periodic with respect to $\omega$ and $\omega'$ thus elliptical. It's zeroes and poles are clearly the same with $\wp'$, thus $\wp'(z) = 2c \frac{\sigma(z-\omega/2)\sigma(z-\omega'/2)\sigma(z+\eta/2)}{\sigma^3(z)\sigma(\omega/2)\sigma(\omega'/2)\sigma(-\eta/2)}$.

    Now by above exercise, expand $\wp'$ near zero and the coefficient of $\wp'$ before $\frac{1}{z^3}$ would be $-2$. Consider $z^3$ times the other side, take $z \to 0$, $\lim\limits_{z \to 0}2 \frac{z^3\sigma(z-\omega/2)\sigma(z-\omega'/2)\sigma(z+\eta/2)}{\sigma^3(z)\sigma(\omega/2)\sigma(\omega'/2)\sigma(-\eta/2)}$, each of the $\frac{\sigma(z-\omega/2)}{\sigma(\omega/2)}$ goes to $-1$ because $\sigma$ is odd. Expand $\sigma(z) = z\prod\limits_{k =1}^{\infty}(1-\frac{z}{\omega_K})\exp{(z/\omega_k + z^2/2\omega_k^2)}$ and plug in, we have $\lim\limits_{z \to 0}2 \frac{z^3\sigma(z-\omega/2)\sigma(z-\omega'/2)\sigma(z+\eta/2)}{\sigma^3(z)\sigma(\omega/2)\sigma(\omega'/2)\sigma(-\eta/2)}$ $= \lim\limits -2 \frac{z^3}{(z\prod\limits_{k =1}^{\infty}(1-\frac{z}{\omega_K})\exp{(z/\omega_k + z^2/2\omega_k^2)})^3}$, $z^3$ cancels out and the limit is $-2$. Thus the coefficient before $\frac{1}{z^3}$ on the right hand side is also $-2$, and thus the equality holds.

    ## Exercise 6

    **Compute a few terms of the normalized Eisenstein series $\xi = e^{2\pi i \tau}, \tau \in \Pi^+$**:

    1. $E_4(\tau) = \frac{s_4(1,\tau)}{2\zeta(4)} = 1+240(\xi+?\xi^2+?\xi^3+\dots), \zeta(4) = \pi^4/90$;
    2. $E_8(\tau) = \frac{s_8(1,\tau)}{2\zeta(8)} = 1+?(\xi+?\xi^2+?\xi^3+\dots), \zeta(8) = \pi^8/9450$.

    **Conjecture a relation between these two functions (modular forms)**.

    Solution

    Start with $\pi \cot(\pi \tau) = \frac{1}{\tau} + {\sum\limits_{m = -\infty}^{\infty}}'(\frac{1}{\tau-m}+\frac{1}{m})$. $\frac{i \pi(e^{\pi i \tau}+e^{-\pi i \tau})}{e^{\pi i \tau}-e^{-\pi i \tau}} = \frac{i \pi (\xi + 1)}{\xi - 1}$ $= -i \pi (\frac{2}{1-\xi}-1)$ $- i \pi (2 \sum\limits_{k=0}^{\infty}\xi^k-1) = \frac{1}{\tau} + \sum\limits_{m = -\infty}^{\infty}(\frac{1}{\tau+m} - \frac{1}{m})$. Differentiate both sides three times gives us $-16\pi^4\sum\limits_{k=1}^{\infty}k^3\xi^k = -6\sum\limits_{m=-\infty}^{\infty}\frac{1}{(\tau+m)^4}$. Summing over $n$ gives $-6\sum\limits_{n=1}^{\infty}\sum\limits_{m=-\infty}^{\infty}\frac{1}{(n\tau+m)^4}$ $= -16\pi^4\sum\limits_{n=1}^{\infty} \sum\limits_{k=1}^{\infty}k^3\xi^{nk}$ $= -16\pi^4\sum\limits_{k=1}^{\infty} \xi^k\sigma_3(k)$ ($*$) where $\sigma_a$ is the divisor function.

    Back to $s_4(1,\tau) = \frac{1}{60}g_2(1,\tau) = \sum\limits_{(n,m)}'(n\omega+m\omega')^{-4}$ $=2{\sum\limits_{m=1}^{\infty}}{m^{-4}} + 2 {\sum\limits_{n=1}^{\infty}}{\sum\limits_{m = - \infty}^{\infty}}{(m+n\tau)^{-4}}$ $= \frac{\pi^4}{45} + 2 {\sum\limits_{n=1}^{\infty}}{\sum\limits_{m = - \infty}^{\infty}}{(m+n\tau)^{-4}}$, then by above equation ($*$) we have $= \frac{\pi^4}{45} + \frac{16}{3}\pi^4\sum\limits_{k=1}^{\infty} \xi^k\sigma_3(k)$ $= \frac{\pi^4}{45} + \frac{16}{3}\pi^4 \xi + \frac{16 \cdot 9}{3}\pi^4 \xi^2 + \frac{16\cdot 28}{3}\pi^4 \xi^3 + \dots$.

    So the normalized term would be $E_4 = s_4/2\xi(4) = 45s_4/\pi^4$ $= 1 + 240(\xi + 9\xi^2 + 28\xi^3 + \dots)$.

    Now $E_8$, for this we need to differentiate ($*$) more times to get $-5040\sum\limits_{n=1}^{\infty}\sum\limits_{m=-\infty}^{\infty}\frac{1}{(n\tau+m)^8}$ $= -256\pi^8\sum\limits_{k=1}^{\infty} \xi^k\sigma_7(k)$. So that $E_8$ will have the form $1 + a(\xi + b\xi^2 + c\xi^3 + \dots)$ where:

    1. $a = \frac{2}{5040}\cdot 256 \cdot \frac{9450}{2} = 480$ (first $2$ comes from the coefficient before summation; $\frac{256}{5040}$ comes from the $8$-th derivative; and $\frac{9450}{2}$ comes from $2\zeta(8)$);
    2. $b = \sigma_7(2) = 1^7 + 2^7 = 129$;
    3. $c = 1^7 + 3^7 = 2188$;
    4. $\dots$

    i.e. $E_8 = 1 + 480(\xi + 129\xi^2 + 2188\xi^3 + \dots)$. A reasonable conjecture will be that $E_4^2 = E_8$ (See Wikipedia 'modular form').

    ## Exercise 7

    **Let $D$ be the left half of the fundamental region $G_0$, i.e. $D = \lbrace \tau \in \Pi^+ : | \tau | > 1, -1/2 < Re \tau < 0 \rbrace$. Show that the modular invariant $J$ is a conformal equivalence between $D$ and $\Pi^+$**.

    Proof

    Let $D'$ be the right half of the fundamental region, by the proposition about surjectivity of $J$ (part of the proof would be exercise 8) and from the property of $J$ that $J(-\overline{\tau}) = \overline{J(\tau)}$, we know that $J$ maps $D$ and $D'$ bijectively to $\Pi^+$ and $\Pi^-$ (but not too clearly which domain corresponding to which codomain).

    From the calculation of $g_2$ and $g_3$, we have that $J(\tau) \overset{\text{def}}{=} \frac{g_2^3(1,\tau)}{\triangle(1,\tau)}$ has the form $= \zeta^{-1}(\tau) + c_0 + O(\zeta(\tau))$, where $\zeta(\tau) = e^{2\pi i \tau}$. Thus $J$ is holomorphic. Moreover, plug in some value $z = -x+iy$ in $D$, i.e. $0<x<1/2, x^2+y^2> 1$, and we can check that $\zeta^{-1}(z) = (e^{2 \pi i z})^{-1}$ belongs to the upper half plane from direct calculation. Thus $J:D \to \Pi^+$ is a holomorphic bijection, thus a conformal map.

    ## Exercise 8

    **Check that the zero of $J(\tau)$ at $\rho = e^{2\pi i/3}$ has order $3$**.

    Proof

    Consider the following (blue) contour $C$ spliced into $7$ parts:

    <img src="public/Pasted image 20210903021351.png" width="400" />

    $\rho$ together with $\rho+1$ need to be excluded, as we know $J(\rho) = J(\rho+1) = 0$. We achieve this by having the two contours like small arcs with radius $\varepsilon \to 0$. The radians of those two circular sectors would both be $\pi/3$, as illustrated in the graph, using the fact that $| \text{re}(\rho) | = \frac{1}{2}$.

    Follows the reasoning from course material, let $m \ge 3$ be number of zeroes of $J$ in the domain, $k \ge 3$ be order of zero of $\rho$, we have $\Delta(arg(J),C) = 2\pi (m-k) = 2 \pi - \frac{\pi}{3}k - \frac{\pi}{3}k$, where $M$ contributes $\Delta(arg(\frac{1}{\zeta}), M) = 2 \pi$, $\gamma$ and $\gamma'$ contribute $-\frac{2\pi}{3}$ together, and the rest cancels out. We have that $m = k = 3$.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Spring Semester Homework 2""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 1

    **Fix the branch $\arctan$ of the inverse tangent so that $0 \le \arctan{t} \le \pi$ for $t \in \mathbb{R}$ and use the convention that $\arctan{\pm\infty} = \pi/2$. Check that $v(x,y) = \arctan{y/x}$ is harmonic on $\Pi^+$**.

    1. **Let now $w(x,y) = b+\frac{a-b}{\pi}\arctan{\frac{y}{x-c}}$. What is the boundary condition for the Dirichlet problem it solves on $\Pi^+$**?
    2. **Generalize 1. To write down the solution to the Dirichlet problem on $\Pi^+$ if the boundary condition on $\mathbb{R}$ is piece-wise constant (so called $N$-value Dirichlet problem for the upper half-plane)**.

    Solution

    1. $\arctan{y/x}$ is harmonic: consider the (rewrite of) log: $\log{x+iy} = \log{z} = \log{r} + i \theta$, where $r = | z |, \theta = \arg{z}$. If we take $\theta$ to be in $(-\frac{\pi}{2}, \frac{3\pi}{2})$, i.e. the branch cut is along $y<0$ so it does not mess up with the upper half plane, we have that $\arctan{y/x} = \theta$. Then $\arctan{y/x}$ can be seen as the real part of $-i\log{z}$ in that branch, which is holomorphic on $\Pi^+$;
    2. By the above argument, $\arctan{y/x}$ would have boundary condition $= 0$ on $x > 0$ and $= \pi$ on $x < 0$; so that $w(x,y)$ would have boundary condition $= a$ on $x < c$ and $= b$ on $x > c$;

    The setup should be like: let $c_0 < c_1 < \dots < c_n$ be a list of real numbers, let $a_0, \dots, a_{n+1}$ be a list of prescribed numbers and consider the boundary condition $w(x,0) = a_i$ for all $x \in (c_{i-1}, c_i)$ for each $i \ge 1$, and say that $w(x,0) = a_0$ for $x < c_0$, $w(x,0) = a_{n+1}$ for $x > c_n$. So $c_i$'s are analogous to above $c$ (they kind of split the line), and $a_i$'s are analogous to above $a$ and $b$ (they determine the values).

    So analogous as $w$ above, try this function $w(x,y) = \frac{1}{\pi}(\pi a_{n+1}$ $+ (a_0 - a_{n+1})(\arctan{\frac{y}{x-c_0}})$ $+ (a_1 - a_{n+1})(\arctan{\frac{y}{x-c_1}} - \arctan{\frac{y}{x-c_0}})$ $+ \dots$ $+ (a_n - a_{n+1})(\arctan{\frac{y}{x-c_n}} - \arctan{\frac{y}{x-c_{n-1}}}))$;

    1. For $x > c_n$, all other summing terms are $0$, only $\pi a_{n+1}$ remains;
    2. For $x < c_0$, only $\pi a_{n+1}$ and $(a_0 - a_{n+1})(\arctan{\frac{y}{x-c_0}}) = \pi (a_0 - a_{n+1})$ remain, summing to $a_0$; the other terms have form $(a-b)(\pi - \pi)$;
    3. For $c_i < x < c_{i+1}$, only $\pi a_{n+1}$ and $(a_{i+1} - a_{n+1})(\arctan{\frac{y}{x-c_{i+1}}} - \arctan{\frac{y}{x-c_i}})$ remain and they sum to $a_{i+1}$, all as desired.


    ## Exercise 2

    **Let $D$ be the horizontal strip $0 < \text{im}(z) < \pi$ and $\varphi: \partial D \to \mathbb{R}$ be given by $\varphi(x) = 1$ for $x \ge 0$, $\varphi = 0$ on the rest of $\partial D$. Find the solution to the Dirichlet problem on $D$ with the boundary condition $u|_{\partial D} = \varphi$**.

    Solution

    First a claim, harmonic function compose a holomorphic function is harmonic, let $f$ be harmonic and $g$ be holomorphic, then by chain rule $4\Delta{f \circ g} = (f \circ g)_{z\overline{z}} = ((\frac{\partial f}{\partial z} \circ g)\frac{\partial g}{\partial z} + (\frac{\partial f}{\partial \overline{z}} \circ g)\frac{\partial \overline{g}}{\partial z})_{\overline{z}}$ $= (\frac{\partial f}{\partial z} \circ g)\frac{\partial^2 g}{\partial z \partial \overline{z}}$ $+ (\frac{\partial^2 f}{\partial z^2} \circ g)\frac{\partial^2 g}{\partial z \partial \overline{z}}$ $+ (\frac{\partial^2 f}{\partial z \partial \overline{z}} \circ g)\frac{\partial g \partial \overline{g}}{\partial z \partial \overline{z}}$ $+ (\frac{\partial f}{\partial \overline{z}} \circ g)\frac{\partial^2 g}{\partial z \partial \overline{z}}$ $+ (\frac{\partial^2 f}{\partial z \partial \overline{z}} \circ g)\frac{\partial g \partial \overline{g}}{\partial z \partial \overline{z}}$ $+ (\frac{\partial^2 f}{\partial \overline{z}^2} \circ g)\frac{\partial^2 \overline{g}}{\partial z \partial \overline{z}}$.

    Since $g$ is holomorphic, basically everything vanishes, and the remaining $(\frac{\partial^2 f}{\partial z \partial \overline{z}} \circ g)\frac{\partial g \partial \overline{g}}{\partial z \partial \overline{z}}$ is also $0$ because $f$ is harmonic.

    Now in particular, a conformal map is holomorphic, so if we have a conformal map between a strip and the upper half plane, compose this map and the solution of Dirichlet problem on upper half plane we may get our answer.

    The conformal map is easy to find: $f(z) = e^z$ maps the strip to upper half plane.

    From last problem, the solution for Dirichlet problem on the upper half plane with the desired boundary condition is given by splitting $R$ by $-1,1$ and taking value of $1, 0, 1$ on the three segments respectively. I.e. $w(x,y) = \frac{1}{\pi}(\pi - (\arg{z-1} -\arg{z+1}))$. Composition gives us $u = \frac{1}{\pi}(\pi - (\arg{e^z-1} -\arg{e^z+1}))$ and this is the solution: the conformal map maps the boundary of the strip $x<0$ to $(-1,1)$, which has boundary value $0$, and the rest part of the boundary to $(-\infty,-1), (1,\infty)$, which has boundary value $1$.

    ## Exercise 3

    **Let $u$ be a positive harmonic function on $\mathbb{R}^2$. Show that $u$ is constant**.

    Proof

    Let $u$ be harmonic, then it is the real part of some holomorphic $f(z) = u(z) + iv(z)$. Consider $e^{f(z)}$, it is holomorphic and never $0$. Moreover, $| e^{f(z)} | = | e^{u+iv} | = e^u$. Since $u$ positive (and real), $e^u > 1$, thus $\frac{1}{e^{f(z)}}$ is bounded by $1$. By Liouville's Theorem it is a constant, which implies $u$ is a constant as well.

    ## Exercise 4

    **Let $u$ be a real-valued harmonic function in the complex plane such that $u(z) \le b+a\log{| z |}$ whenever $| z | \ge 1$ (for some constants $a > 0$ and $b$). Show that $u$ is constant**.

    Proof

    Rewrite the inequality we have $\frac{u-b}{a} \le \log{| z |}$. Since $u$ is real-valued harmonic, $\frac{u-b}{a}$ must also be real-valued harmonic, thus it is the real part of some holomorphic $f$.

    Now take exponential: $| \exp{f} | = \exp{\frac{u-b}{a}}$, (now we work in real numbers), $\le \exp{\log{| z |}} = | z |$.

    Again we want to find some way to apply Liouville's Theorem, so we need something entire and bounded by some constant:

    Consider $| \exp{f(z)} - \exp{f(0)} | \le | \exp{f(z)} | + | \exp{f(0)} |$, the first part is less than $| z |$ as shown above, and the second part is a constant, $\le | z | + c$, if $| z | \ge 1$, it is $\le | z | + c | z | = (1+c) | z |$. So $\frac{\exp{f(z)}-\exp{f(0)}}{z}$ is bounded; it may only have pole at $0$, but $\exp{f(z)}-\exp{f(0)} = 0$ at zero and the singularity is removable. So $\frac{\exp{f(z)}-\exp{f(0)}}{z}$ is entire and bounded thus equals some constant $c^{*}$.

    Thus $\exp{f(z)} = zc^{*}+\exp{f(0)} = zc^{*}+c$; if $c^{*} \ne 0$ then $\exp{f(z)}$ is an non-constant polynomial (thus has a root), but that should not be true, because $\exp{z} \ne 0$ for all $z$, thus $c^{*} = 0$ and $\exp{f(z)}$ is constant, which implies $f$ and $u$ are constant as well.

    ## Exercise 5

    **The trigonometric polynomials are dense in $C(\partial \mathbb{D})$. That is, if $f \in C(\partial \mathbb{D})$ and $\varepsilon > 0$, then there exists a trigonometric polynomial $P$ such that $| P(e^{it}) - f(e^{it}) | < \varepsilon$ for all $t \in \mathbb{R}$ (Page 188)**.

    Proof

    For $0 < r < 1$, let $f_r(e^{it}) = \sum\limits_{n=-\infty}^{\infty}r^{| n |}c_ne^{int}$, where $c_n$ is the $n$-th Fourier coefficient of $f$, which is exactly $P[[re^{it}|f]]$ in the form stated in Theorem 10.4.0, and it gives a solution to Dirichlet problem in $\mathbb{D}$ with boundary condition $f$. In other word, for any given $\varepsilon$, by continuity we have that there exists $R$ such that $| f_r(e^{it}) - f(e^{it}) | < \varepsilon/2$ for all $t$ for all $R < r < 1$.

    Fix such $r$, then for each $n$, the $n$-th Fourier coefficient of $f$ is $\frac{1}{2\pi}\int_{0}^{2\pi}f(e^{it})e^{-int}dt$. Since $f \in C(\partial \mathbb{D})$, $f$ is bounded on $\partial \mathbb{D}$, thus $| \frac{1}{2\pi}\int_{0}^{2\pi}f(e^{it})e^{-int}dt |$ $\le \frac{1}{2\pi}(2 \pi M)$ $\le M$ is bounded, since $| e^{int} | = 1$.

    Now $| P(e^{it}) - f_r(e^{it}) |$ has the form $= | \sum\limits_{-N}^Nc_ne^{int} - \sum\limits_{-\infty}^{\infty}r^{| n |}c_ne^{int}|$ $=| \sum\limits_{| n | >N} r^{| n |}c_ne^{int} + \sum\limits_{| n | \le N}(r^{| n |}c_ne^{int} - c_ne^{int})|$.

    The first part: $\sum\limits_{n > N} r^{| n |}$ is a geometric series, for any $\varepsilon$ we can choose appropriate $N$ such that $\sum\limits_{n > N} r^{| n |} < \varepsilon$. Since $c_n$ is bounded, we can tweak the $N$ to make $\sum\limits_{| n | > N}| c_n | r^{| n |} < \varepsilon/2$. The second part has finite terms, by choose $r$ closer enough to $1$ we can neglect it. Thus for large enough $r$ and large enough $N$, we have that $| P(e^{it}) - f_r(e^{it}) | < \varepsilon/2$.

    Now by triangle inequality we have the desired statement.

    ## Exercise 6

    **Find the most general harmonic function of the form $f(| z |), z \in \mathbb{C} - \lbrace 0 \rbrace$**.

    Solution

    For $z \ne 0$ we have $f(| z |) = f(\sqrt{x^2 + y^2})$. So $f_x = \frac{x}{\sqrt{x^2+y^2}}f'(\sqrt{x^2 + y^2})$, and $f_{xx} = \frac{y^2}{(x^2+y^2)^{3/2}}f' + \frac{x}{\sqrt{x^2 + y^2}}f'_x$ $=\frac{y^2}{(x^2+y^2)^{3/2}}f' + \frac{x^2}{x^2 + y^2}f''$. By symmetric $f_{yy} = \frac{x^2}{(x^2+y^2)^{3/2}}f' + \frac{y^2}{x^2 + y^2}f'_y$.

    If it is harmonic we need to have $f_{xx} + f_{yy} = 0$ $\implies y^2f'+x^2\sqrt{x^2+y^2}f'' +x^2f'+y^2\sqrt{x^2+y^2}f'' = 0$ $\implies f'+ \sqrt{x^2+y^2}f'' = 0$. Since $f'$ and $f''$ are taking derivatives with respect to $\sqrt{x^2+y^2}$, essentially we are solving an ODE $y' + xy'' = 0$:

    Let $v = \frac{dy}{dx}$, then $\frac{d^2y}{dx^2} = \frac{dv}{dx}$, the ODE becomes $\frac{dv}{dx}/v = -\frac{1}{x}$, taking integral each side to get $\int \frac{1}{v}dv = \int - \frac{1}{x}dx$ $\implies \ln{v} = -\ln{x} + c$, take exponential and we have $v = \frac{c}{x}$, i.e. $\frac{dy}{dx} = \frac{c}{x}$ thus $y = c\ln{x} + c'$. In other word we have the original $f$ has the form $f(| z |) = c\log{| z |} + c'$, $c,c'$ are constants.

    ## Exercise 7

    **Suppose that $K \subseteq \mathbb{C}$ is compact, suppose that $(R_n)$ and $(S_n)$ are sequences of elements of $C(K)$ which converge to uniformly on $K$ to $f$ and $g$ respectively. Show that $R_nS_n$ converges to $fg$ uniformly on $K$ (Page 232)**.

    Proof

    Consider that $| R_nS_n - fg |$ $= | R_nS_n -R_ng+R_ng-fg|$ $\le | R_nS_n -R_ng | + | R_ng-fg |$ $\le | R_n \| S_n - g | + | g \| R_n -f |$. Since $(R_n)$ and $(S_n)$ are continuous, $f$ and $g$ are continuous, and thus bounded (by $B_f, B_g$) on compact $K$. For any $\varepsilon > 0$, choose $N_f, N_g$ such that for all $n > N_f, m > N_g$, $| R_n -f | < \frac{\varepsilon}{2B_f+2}$ and $| S_m -g | < \frac{\varepsilon}{2B_g}$, and take $N = \max{N_f, N_g}$. $R_n$ in this case is bounded by $B_f + 1$.

    Then $| R_nS_n - fg | \le \varepsilon$, by definition we have uniform convergence.

    ## Exercise 8

    **Show that there exists a sequence of polynomials $(P_n)$ with $P_n(0) = 1$ for all $n$ and $\lim\limits_{n \to \infty}P_n(z) = 0$ for all $z \in \mathbb{C} - \mathbb{R}_{\ge 0}$**.

    Proof

    For each $n$, define $K_n = K_n^+ \cup K_n^0 \cup K_n^- \cup \lbrace 0 \rbrace$ where $K_n^+$ is the closed rectangle with vertices $-n+i/n$, $n+i/n$, $-n+in$, $n+in$; $K_n^-$ is the closed rectangle with vertices $-n-i/n$, $n-i/n$, $-n-in$, $n-in$; and $K_n^0$ is the line segment $[-1-n,-1+1/n]$:

    <img src="public/Pasted image 20210903021353.png" width="400" />

    Now define $f_n:K_n \to \mathbb{C}$ by $f_n(z) = 0$ for $z \in K_n^+ \cup K_n^0 \cup K_n^-$ and $=1$ for $z = 0$.

    Each $C - K_n$ is connected, $f_n$ is holomorphic in a neighborhood of $K_n$, by Runge's Theorem on compact set there exists sequence $(P_n)$ with the desired properties.

    ## Exercise 9

    **Show that there exists a sequence of polynomials $(P_n)$ such that $P_n(0) = 1$ for all $n$, while $P_n(z) \to 0$ as $n \to \infty$ if $z \in \mathbb{C}$ and $z \ne 0$ (Page 240)**.

    Proof

    Similarly, for each $n$, define $K_n = K_n^+ \cup K_n^{0+} \cup K_n^{0-} \cup K_n^- \cup \lbrace 0 \rbrace$ where $K_n^+$ is the closed rectangle with vertices $-n+i/n$, $n+i/n$, $-n+in$, $n+in$; $K_n^-$ is the closed rectangle with vertices $-n-i/n$, $n-i/n$, $-n-in$, $n-in$; $K_n^{0-}$ is the line segment $[1+n,1-1/n]$; and $K_n^{0-}$ is the line segment $[-1-n,-1+1/n]$ (add another segment on the right):

    <img src="public/Pasted image 20210903021641.png" width="400" />

    Now define $f_n:K_n \to \mathbb{C}$ by $f_n(z) = 0$ for $z \in K_n^+ \cup K_n^{0+} \cup K_n^{0-} \cup K_n^-$ and $=1$ for $z = 0$.

    Each $C - K_n$ is connected, $f_n$ is holomorphic in a neighborhood of $K_n$, by Runge's Theorem on compact set there exists sequence $(P_n)$ with the desired properties.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Spring Semester Homework 3""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 1

    **Write down an entire function which has a zero of order $k^2$ for each $k \in \mathbb{Z}$**.

    Solution

    By Weierstrass Theorem for Entire Functions (well, actually the proposition before it in the class), choose $(a_n)$ be the zeroes we want, i.e.: $1,-1,2,2,2,2,-2,-2,-2,-2,\dots$, this is countable, then the function $f(z) = \prod\limits_{j=1}^{\infty}E_{j}(\frac{z}{a_j})$ is entire with the desired zeroes.

    A revise: to apply this proposition we need that $\sum\limits_{j=1}^{\infty}(\frac{r}{| z_j |})^{n_j+1}$ converges for all $r > 0$, so we need to modify the $n_j+1$ a little bit, $E_{3}(\frac{z}{a_j})$ should work.

    ## Exercise 2

    **Prove that if $f_1$ and $f_2$ are two entire functions with no common zeroes, then there exist entire functions $g_1$ and $g_2$ such that $g_1f_1 + g_2f_2 = 1$**.

    Proof

    Rewrite the condition as $g_1 = \frac{1 - g_2f_2}{f_1}$, we need this to be entire: if $f_1$ has zeroes at $z_i$ with orders $m_i$, then if we manage to find entire $g_2$ making $1-g_2f_2$ has zeroes at those $z_i$ with orders $n_i$, such that $n_i \ge m_i$ for each $i$, we can make $g_1$ entire as well.

    By holomorphic interpolate theorem there exists $g_2$ such that $1 - f_2g_2$ has zeroes of order $n_i$ at $z_i$, i.e. prescribed $g_2^{(n_i)}(z_i) = \frac{1}{f_2(z_i)}$, which leads to no problem because $f_2$ by assumption does not have zeroes at $z_i$.

    Once we have $g_2$, compute $g_1 = \frac{1-g_2f_2}{f_1}$, by construction the singularities are all removable, thus there exists suitable entire $g_1$ and $g_2$.

    ## Exercise 3

    **Suppose that $D$ is a bounded and connected open subset of the plane, show that there exists $f \in H(D)$ which cannot be extended to a function holomorphic in a strictly larger connected open set**.

    Proof

    Hint says to show that there exists a set $E \subseteq D$ such that $E$ has no limit point in $D$ but every point of $\partial D$ is a limit point of $E$.

    Assuming we have known this statement (and that $E$ is countable, in particular, $E \ne D$), then by Weierstrass Factorization Theorem (in an open set) we have that there exists $f \in H(D)$ such that the zeroes of $f$ are exactly those points in $E$. This $f$ cannot be extended to a function holomorphic on a strictly larger (connected) open set: otherwise this open set contains at least a point in $\partial D$ thus contains a limit point of $E$, then the identity principle tells us $f \equiv 0$ on this open set, but this gives a contradiction, because $f$ on $D$ should not have zeroes other than those points in $E$.

    For the hint: the boundary is by assumption closed and bounded in $\mathbb{C}$ thus compact; for each $n \in \mathbb{N}$, $\bigcup\limits_{d \in \partial D} B(d,\frac{1}{n})$ covers $\partial D$ thus admit a finite sub-cover $\cup B(d,\frac{1}{n})$, choose one point in each of ball that is contained in $D$, and do it for all $n$, those points together give the desired countable $E$.

    ## Exercise 4

    **An entire function $f$ is said to be of finite order if there is a number $t > 0$ such that $| f(z) | \le \exp{| z |^t}$ for all sufficiently large $z$. The infimum of all such $t$ is called the order of $f$**.

    1. **Show that $\cos(z^{1/2})$ is a single valued entire function of order $1/2$**;
    2. **Construct an entire function of order** $1/4$.
	

    Proof

    1. Part 1:
    	1. Entire: write the series expansion $\cos(z) = \sum\limits_{n = 0}^{\infty} \frac{(-1)^nz^{2n}}{(2n)!}$ so that $\cos(z^{1/2}) = \sum\limits_{n=0}^{\infty}\frac{(-1)^nz^n}{(2n)!}$, this is a power series, and anywhere convergent, thus entire;
    	2. Single-valued: we can see that from the series expansion. The 'multi-valued' property of $z^{1/2}$ is offset by the fact that cosine is even;
    	3. Order is $1/2$:
    		1. From the series expansion above, $| f(z) | = \sum \frac{| z |^n}{(2n)!}$, yet series expansion for $e^{| z |} = \sum \frac{| z |^n}{n!}$ and that $e^{| z |^{1/2}} = \sum \frac{| z |^{n/2}}{n!}$. We can see that $| f(z) | \le \exp{| z |^{1/2}}$ simply because the latter has more non-negative terms, this gives an upper bound for the order;
    		2. On the other hand, write $\cos(z^{1/2})$ as $= \frac{e^{i\sqrt{z}} + e^{-i\sqrt{z}}}{2}$ and say we take $z = -x$ then $| \cos(z^{1/2}) |$ $= \frac{e^{\sqrt{x}} + e^{-\sqrt{x}}}{2}$ $> \frac{e^{\sqrt{x}}}{2}$ $= \frac{e^{| z |^{1/2}}}{2}$, the constant $1/2$ can be ignored, and thus $1/2$ is also a lower bound for the order, this conclude that the order is $1/2$;
    2. Simply take $\cos(\sqrt[4]{z})$ would not work, because it is not even entire: $\cos(\sqrt[4]{z})$ $= \sum \frac{(-1)^nz^{n/2}}{(2n)!}$ is not a power series, but we can pad $\cos(i\sqrt[4]{z})$ on it, which has the expansion $= \sum \frac{z^{n/2}}{(2n)!}$, so that the even term, where $n/2$ is not an integer, got offset. The resulting $\cos(\sqrt[4]{z}) + \cos(i\sqrt[4]{z})$ $= \sum \frac{2 z^n}{(4n)!}$ is entire. By the very same argument as above, write the expansion for $e^{\sqrt[4]{z}}$ we can see $1/4$ is an upper bound for the order; also $\cos(\sqrt[4]{z}) + \cos(i\sqrt[4]{z})$ can be written as $\frac{e^{\sqrt[4]{z}}+e^{-\sqrt[4]{z}}+e^{i\sqrt[4]{z}} + e^{-i\sqrt[4]{z}}}{2}$ $>\frac{e^{| z |^{1/4}}}{2}$ so $1/4$ is also an lower bound.

    ## Exercise 5

    **Fix $k\ge 2$ and consider $f \in H(\mathbb{D})$ given by $f(z) = \sum\limits_{n=0}^{\infty}z^{k^n}$. Show that the unit circle $\partial \mathbb{D}$ is a natural boundary for $f$**.

    Proof

    On $\partial \mathbb{D}$ we can write $z = e^{2 \pi i t}$, for a fixed $k$, take $t$ as any (non-zero) rational number with the form $r/k$, $r$ be an integer, then we look at each term of $f(z)$: $z^{k^n} = e^{2 \pi i \frac{r}{k} k^n}$, for any $n \ge 1$, $z^{k^n} = e^{2 \pi i r k^{n-1}}$, this $rk^{n-1}$ is clearly an integer thus $z^{k^n} = 1$.

    This equality holds true for any $n \ge 1$ and any rational with the form $r/k$ (in particular, those $z = e^{2 \pi i r/k}$ are dense in the circle). Thus $\lim\limits z^{k^n}$ is not even $0$ thus is impossible for $f(z)$ to converge.

    Now any continuation of $(f, \mathbb{D}) \sim (g, D)$ would have some $p = e^{2 \pi i r/k} \in D$, but then $\lim\limits_{z \to p}g(z)$ would go to $\infty$ thus it is not a (holomorphic) continuation anyway.

    ## Exercise 6

    **Let $a = 1+i$ and $D = \mathbb{C} - S$ be the complement of the spiral $S = \lbrace 0 \rbrace \cup \lbrace e^{at} | t \in \mathbb{R} \rbrace$ in $\mathbb{C}$. Let $\log$ be a branch of the logarithm on $D$ such that $\log{e} = 1$, find $\log{e^{20}}$**.

    Solution

    The spiral looks something like this:

    <img src="public/Pasted image 20210903021566.png" width="600" />

    Now by the continuation of $\log$ (branch cut along $z \le 0$), along the positive real axis, we basically need to 'change the branch' once we go to another 'layer' of the (complement of) spiral. As it illustrated in the drawing, if say $\log{a} = Log(a)$ then $\log{b} = Log(b) + 2\pi i$. So we want to see how many times do we 'cross' the spiral if we go from $e$ to $e^{20}$:

    Write $e^{t+it}$ as $e^t\cos(t) + i e^t\sin(t)$, so the spiral intersects with the real axis at those points where $e^t \sin(t) = 0$, since $e^t$ is never zero we have $\sin(t) = 0$, and those are exactly the points $t = \mathbb{Z}\pi$. On those points $e^t \cos(t)$ (the real part) is positive if and only if $t$ is an even integer times $\pi$. Thus the spiral intersect with the positive real axis on:

    1. $…, e^{-2\pi - 2\pi i}$ (those points with $t<0$, not important for us, they are too small);
    2. $e^0 = 1$;
    3. $e^{2\pi + 2\pi i} = e^{2 \pi} \approx e^{6.28}$ (so notice our original $e$ is in between this and $1$);
    4. $e^{4\pi + 4\pi i} = e^{4 \pi} \approx e^{12.57}$;
    5. $e^{6\pi + 6\pi i} \approx e^{18.85}$;
    6. $e^{8\pi + 8\pi i} \approx e^{25.13}$, and finally we got passed $e^{20}$, the larger $t$'s are again not important for us anymore.

    So it means to get from $e$ to $e^{20}$ we cross the spiral $3$ times, and thus $\log e^{20}$ will be $Log(e^{20}) + 2\cdot 3 \pi i = 20+6\pi i$.

    ## Exercise 7

    **Show that the monodromy group of $h(z) = \sqrt{f(z)}$ is solvable whenever the monodromy group of $f(z)$ is solvable. Generalize it to $f(z)^{1/n}$**.

    Proof

    Following the example in the class, the scheme of the Riemann surface of $h(z)$ is a certain number of $2$-stacks of sheets, so the monodromy group is generated by flips and chain(s) of flips, where each flip is of the form $(2k+1,2k+2)$, for example $\langle (12), (12)(34),(56) \rangle$ maybe such a group, but not $\langle (12), (12)(14) \rangle$ nor $\langle (23) \rangle$ (and we can generalize this to $n > 2$). We need to prove that $N$ be the group generated by such permutations is abelian. We need to show that:

    1. Product of disjoint cycles is abelian, so that we can rearrange any products to the form $(a_{1_1}\dots a_{1_n})^{k_1}\dots (a_{m_1}\dots a_{m_n})^{k_m}$:
    	Let $X$ be a set with certain non-zero number of element, set $X_1 = \lbrace x \in X | \sigma_1(x) \ne x \rbrace$ and $X_2 = \lbrace x \in X | \sigma_2(x) \ne x \rbrace$, if $X_1 \cap X_2 = \varnothing$ we can say $\sigma_1$ and $\sigma_2$ are disjoint. If $\sigma_1$ and $\sigma_2$ are disjoint, then for any element in $X_1$, $\sigma_1 \circ \sigma_2 (x) = \sigma_1 (\sigma_2(x)) = \sigma_1 (x)$, and that $\sigma_2 \circ \sigma_1 (x) = \sigma_2 (\sigma_1(x))$, since $x \in X_1$, $\sigma_1(x)$ is also in $X_1$ thus not in $X_2$, thus $\sigma_2 \circ \sigma_1 (x) = \sigma_1 (x)$ as well. Similar for $x \in X_2$. For any $x \in X - X_1 - X_2$, $\sigma_1 \circ \sigma_2 (x) = x = \sigma_2 \circ \sigma_1 (x)$. So in any case the product is abelian.
    	For $h(z) = \sqrt{f(z)}$ we can finish here, because product of $k$ same flip $(ab)$ is either $(ab)(ab)$ (just no permutation here) if $k$ even or $(ab)$ if $k$ is odd, so that product of chains of such flips will yield another chain of (disjoint) flips, thus the whole group is abelian. For $h(z) = f(z)^{1/n}$ we also need to check that:
    2. $(a_1\dots a_n)^k$ yield disjoint cycles with element in $a_1, \dots, a_n$:
    	But this is quite obvious simply from the way we do cycles compositions. Now that each $(a_{1_1}\dots a_{1_n})^{k_1}$ is a composition of disjoint cycles, and by part 1 product of disjoint cycles is abelian. Thus the whole group generated by the permutations described above is indeed abelian.

    """
    )
    return


if __name__ == "__main__":
    app.run()
