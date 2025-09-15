import marimo

__generated_with = "0.15.4"
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
    mo.md(r"""# Fall Semester Final Exam""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Problem 01

    **Let $f$ be an entire function and $a, b$ be positive constants**.

    1. **If $| f(z) | \le a|z|^{1/2}+b$ for all $z$, prove that $f$ is a constant**;
    2. **What can you conclude if $|f(z)|\le a|z|^{5/2}+b$ for all $z$**?

    ## Problem 02

    **Let $f$ be a non-constant entire function, prove that $f(\mathbb{C})$ is dense in $\mathbb{C}$**.

    ## Problem 03

    **Evaluate** $$\int_0^{\infty}\frac{x\sin(x)}{(1+x^2)^2}dx.$$

    ## Problem 04

    **State and prove the Open Mapping Theorem. Indicate what theorems are you using in your proof**.

    ## Problem 05

    **Suppose that $f: \Pi^+ \to \mathbb{D}$ is holomorphic and $f(i) = 0$. How large can $|f(2i)|$ be under these conditions**?

    ## Problem 06

    **Let $f, g$ be entire functions such that $\lim\limits_{z \to \infty}g(f(z)) = \infty$. Prove that both $f$ and $g$ are polynomials**.

    ## Problem 07

    **For $\alpha \in \mathbb{C}$, evaluate** $$\int_0^{\infty}\frac{t^{2\alpha-1}}{1+t^2}dt$$ **and express the answer in terms of trigonometric functions of $\alpha$. You may impose any restrictions on $\alpha$ you find necessary, but indicate them clearly**.

    ## Problem 08

    **Suppose that $V$ is a connected open set and $\mathcal{F} \subset H(V)$, $\mathcal{F}^{(n)} = \{f^{(n)}: f\in\mathcal{F}\}$**.

    1. **Show that if $\mathcal{F}$ is a normal family, so is $\mathcal{F}^{(n)}$**;
    2. **Claim: if $\mathcal{F}^{(1)}$ is normal, so is $\mathcal{F}$. Under what reasonable condition on $\mathcal{F}$ is this claim true**?

    ## Problem 09

    **Let $V = D(1,1) \cap D(-i,1)$, and $\varphi(z) = z^{-1}$**.

    1. **Describe $\varphi(V)$**;
    2. **Construct the conformal equivalence $f: V \to \mathbb{D}$**.

    ## Problem 10

    **Let $g: \mathbb{D} \to \mathbb{D}$ be holomorphic and $g(0) = 0$**.

    1. **Prove that $|g(z) + g(-z)| \le 2 |z|^2$ for $z \in \mathbb{D}$**;
    2. **Prove that the inequality above is strict for $z \ne 0$, unless $g(z) = \lambda z^2$ and $|\lambda| = 1$. *Hint: Start by writing $g(z) = \lambda z^2 + h(z).$**
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

    **Suppose $K \subset \partial \mathbb{D}$ is compact and $K \ne \partial \mathbb{D}$, $K \ne \varnothing$. Show that for any $\varepsilon > 0$ there exists a polynomial $Q$ with $Q(0) = 1$ and $|Q(z)|<\varepsilon$ on $K$**.

    Proof

    This is just a direct application of the Runge's Theorem for one compact set. Take $K' = K \cup \{0\}$, $$f(z) = \begin{cases} 2,&z = 0,\\0,&z \in K.\end{cases}$$ Since $K \ne \partial \mathbb{D}$, $\mathbb{C}^{\infty} \setminus K'$ is connected, and we can take $R$ in the Runge's Theorem to be a polynomial. Then normalize it to have $R(0) = 1$.

    ## Problem 2

    **Consider an elliptic function $f$ with periods $w$ and $w'$, and let $a_1, \dots, a_m$, $b_1,\dots, b_n$ be the lists of its zeroes and poles respectively in the period parallelogram $P$, listed with multiplicity**.

    1. **Show that $m = n$**;
    2. **How are the sums $a_1 + \dots + a_m$ and $b_1 + \dots + b_n$ related? Explain**.

    Proof

    For part 1, use the fact that $$\frac{1}{2\pi i}\int_{\partial P}\frac{f'(z)}{f(z)}dz = 0$$ by periodicity of $f$, and on the other hand this integral is $m - n$ (number of zeroes minus number of poles) by the Residue Theorem.

    For part 2, consider $g(z) = \frac{zf'(z)}{f(z)}$. By the Residue Theorem $$\frac{1}{2\pi i}\int_{\partial P}g(z)dz = a_1+\dots +a_m -b_1-\dots-b_n.$$ Let $A = [z_0,z_0+w]$, $A' = [z_0+w',z_0+w+w']$. Again, from periodicity $$\frac{1}{2\pi i}\int_Ag(z)dz - \frac{1}{2\pi i}\int_{A'}g(z)dz = -\frac{w'}{2\pi i}\int_A\frac{f'(z)}{f(z)}dz,$$ and this gives us an integer multiple $-kw'$ by the Argument Principle, where $k$ is the number of times the closed curve $f(A)$ winds around the origin. Similarly, the other two sides of $\partial P$ will contribute a multiple of $w$. Thus $$a_1+\dots+a_m \equiv b_1+\dots+b_n\pmod{w\mathbb{Z}+w'\mathbb{Z}}.$$

    ## Problem 3

    **Let $D \subset \mathbb{C}$ be open connected, $\overline{\mathbb{D}} \subset D$**.

    1. **Let $f \in H(D)$ such that $f(\partial \mathbb{D})$ is real, show that $f$ is a constant**;
    2. **Fix $z = e^{i \theta} \in \partial \mathbb{D}$. Construct a non-constant $f \in H(D \setminus \{z\})$ such that $f$ is real on $\partial \mathbb{D} \setminus \{z\}$**.

    Proof

    Let $v = \text{Im}(f)$, then $v$ is harmonic in $\mathbb{D}$ and vanishes on the boundary, thus $v \equiv 0$ from the uniqueness property for the Dirichlet problem in the unit disk. Then $f$ is real holomorphic, thus constant directly from Cauchy-Riemann equations.

    Take $g(z) = i \frac{z+1}{z-1}$, this is Cayley transform mapping $\mathbb{D} \to \Pi^+$. It is holomorphic in $\mathbb{C} \setminus \{1\}$. Clearly $g(\partial \mathbb{D}) = \mathbb{R}^{\infty}$, which can be checked by computing $$g(e^{it}) = i\frac{e^{it}+1}{e^{it}-1} = \frac{e^{it/2}+e^{-it/2}}{e^{it/2}-e^{-it/2}} = \cot(\frac{t}{2}).$$ Now let $f(z) = g(e^{-i\theta}z)$ to get the answer for part 2.

    ## Problem 4

    **Let $a_n = 1 - \frac{1}{n^2}$, $g_n(z) = \frac{a_n - z}{1-a_nz} = 1 - \frac{1}{n^2}\frac{1+z}{1-a_nz}$ and** $$f(z) = \prod_{n=1}^{\infty}g_n(z).$$

    1. **Show that $f \in H(\mathbb{D})$**;
    2. **Prove that $f$ does not have an analytic continuation to any larger disk $D(0,r)$, $r > 1$**.

    Proof

    In part 1, it suffices to check that the series $$\sum_{n=1}^{\infty}|1-g_n| = \sum_{n=1}^{\infty}\frac{1}{n^2}\frac{|1+z|}{|1-a_nz|}$$ converges uniformly in $\overline{D(0,r)}$ for any $r < 1$. For $z \in \overline{D(0,r)}$, $$\frac{|1+z|}{|1-a_nz|} \le \frac{1+r}{1-r},$$ and uniform convergence follows from convergence of $\sum \frac{1}{n^2}$.

    Thus $f$ is a non-zero holomorphic function in $\mathbb{D}$ with zeroes at every $a_n$, $n \ge 1$. Since these zeroes have a limit point at $1$, $f$ cannot be holomorphic continued to any open set containing $1$.

    ## Problem 5

    **Consider the Riemann surface $S$ of the algebraic function given by** $$w = \sqrt[3]{(z-2)^2(\sqrt{z}+i)}.$$

    1. **What are the branching points of $S$? What are their orders? What is the genus of $S$**?
    2. **Sketch the scheme of $S$ and describe its monodromy group $G$**.

    Proof

    Take three copies of the scheme for $z^{1/2}$ and label six sheets of the Riemann surface $S$ so that 1, 2, 3 correspond to the positive branch of $z^{1/2}$, and 4, 5, 6 to the negative branch, and the monodromy permutation $\sigma_0$ for critical point $z= 0$ acts by $\sigma_0 = (14)(25)(36)$. The remaining critical points are $z = 2$, $z = -1$ and $z = \infty$. We can write $\sigma_{-1} = (456)$ (no branching over $z = -1$ on the positive sheets) and $\sigma_2 = (132)(465)$. Note that on the negative sheets $\sigma_{-1}$ and $\sigma_2$ act in the opposite directions, due to the exponent $2$ in $(z-2)^2$.

    Let's compute $\sigma_{\infty} = \sigma_2^{-1}\sigma_{-1}^{-1}\sigma_0^{-1} = (123)(14)(25)(36)$ $= (142536)$. Not surprisingly, it is a $6$-ycle, since at infinity $w$ behaves as $\sqrt[3]{z^2z^{1/2}} = z^{5/6} = \frac{z}{z^{1/6}}$, and all six sheets come together there at a single branching points.

    So, we have $3$ branching points over $z = 0$ of order $1$ each, $2$ branching points over $z = 2$ of order $2$ each, $1$ branching point over $z = -1$ of order $2$, and $1$ branching point over $z = \infty$ of order $5$. By the Riemann-Hurwitz formula, $$g(S) = 1-6+\frac{1}{2}(3+2\cdot 2 + 2+5) = 2.$$ The monodromy group $G$ of $S$ is a solvable group of order $18$.

    """
    )
    return


if __name__ == "__main__":
    app.run()
