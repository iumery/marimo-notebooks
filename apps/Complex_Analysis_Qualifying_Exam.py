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
    mo.md(r"""# Section A""")
    return


@app.cell
def _(mo):
    mo.md(r"""Solve $2$ of the $3$ problems below.""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 01""")
    return


@app.cell
def _(mo):
    mo.md(r"""**Evaluate** $$\int_0^{\infty}\frac{t^2+1}{t^4+1}dt.$$""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 02""")
    return


@app.cell
def _(mo):
    mo.md(r"""**Fix $\lambda > 1$, and let $f(z) = z+ \lambda -e^z$. Show that $f$ has a unique zero in the left half-plane and that this zero is real**.""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 03""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Define** $$f(z) = \frac{e^{z^{1/2}} - e^{-z^{1/2}}}{\sin(z^{1/2})}.$$

    1. **$f$ has obvious poles at $z = n^2\pi^2$, $n = 1,2, \dots$. Explain why $f$ is single-valued and holomorphic everywhere else**;
    2. **What are the residues of $f$ at the poles? Compute $\int_{\partial D(0,25)}f(z)dz$**.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Section B""")
    return


@app.cell
def _(mo):
    mo.md(r"""Solve $2$ of the $3$ problems below.""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 04""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Let $f = u+iv$ be an entire function**.

    1. **Suppose $u^2(z) \ge v^2(z)$ for all $z \in \mathbb{C}$. Show that $f$ is a constant**;
    2. **Suppose $|f(z)| \le A + B|z|^m$ for all $z \in \mathbb{C}$ and some positive constants $A, B, m$. Show that $f$ is a polynomial of degree bounded by $m$**.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 05""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""**Let $f: \mathbb{D}\to \mathbb{D}$ be a holomorphic map of the unit disk to itself, and $f$ is not the identity map. Show that $f$ can have at most one fixed point**."""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 06""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""**Let $f: D \to \mathbb{C}$ be a complex-valued function on a domain $D$, and $g(z) = zf(z)$. Show that $f \in H(D)$ if and only if both $f$ and $g$ are harmonic**."""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Section C""")
    return


@app.cell
def _(mo):
    mo.md(r"""Solve $3$ of the $5$ problems below.""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 07""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""**Let $\Omega$ be a lattice in $\mathbb{C}$, $\mathbb{P}$ its period parallelogram, $P$ the Weierstrass function for $\Omega$, and $f$ an elliptic function of order $2$. Fix $z_0 \in \mathbb{P}$ such that $f'(z_0) = 0$. Then $g(z) = \frac{1}{f(z+z_0) -f(z_0)}$ has a pole of order $\_\_\_\_\_\_\_\_\_\_$ at $\_\_\_\_\_\_\_\_\_\_$. Use this fact to show that** $$f(z) = \frac{aP(z-z_0)+b}{cP(z-z_0)+d}$$ **for some $a, b, c, d \in \mathbb{C}$**."""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 08""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""**Consider the Riemann surface $S$ of the algebraic function given by** $$w = \sqrt{(\sqrt{z}+1)(\sqrt[3]{z}-1)}.$$ **What are the branching points of $S$? What are their orders? What is the genus of $S$? Sketch the scheme of $S$**."""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 09""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    1. **State the Weierstrass Factorization Theorem for entire functions**;
    2. **Let $f_1, f_2 \in H(\mathbb{C})$. Produce entire functions $h, g_1, g_2$ such that $f_1 = hg_1$, $f_2 = hg_2$ and $g_1, g_2$ have no common zeroes**.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 10""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""**Let $D = \mathbb{D} \setminus(-1,0]$, and $f(z) = z^i$. How do you make $f(z)$ a single-valued function on $D$? Is it possible to construct a sequence of polynomials $P_n$ such that $\lim\limits_{n \to \infty}P_n(z) = z^i$ for all $z \in D$? Explain carefully**."""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 11""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""**Consider a polynomial $P(z) = a_0 + a_1z + \dots + a_nz^n$, and suppose that $P$ is one-to-one in $\mathbb{D}$. Suppose also that $n > 1$ and $a_1 = 1$. Show that $|na_n|\le 1$**."""
    )
    return


if __name__ == "__main__":
    app.run()
