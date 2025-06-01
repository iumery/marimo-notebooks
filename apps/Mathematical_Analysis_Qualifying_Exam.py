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
    mo.md(r"""## Problem 01""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    1. **State the one dimensional Intermediate Value Theorem**;
    2. **State the corresponding result in higher dimensions, giving carefully the definitions of the concepts involved: e.g. connected sets, etc**.;
    3. **Explain why does part 2 imply part 1**.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 02""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""**Define the boundary $\partial A$ of $A \subset \mathbb{R}^n$ to be the set of points $y$ such that for any $r > 0$, the intersection of any ball $B(y,r)$ with both $A$ and $A^c$ is not empty. Show that $\partial A$ is a closed set**."""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 03""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""**Show that if $a_n \to a \in \mathbb{R}$, then $\lim\limits_{n \to \infty}q_n = a$ where $q_n = \frac{1}{n}(a_1+\dots + a_n)$. Is it true that if $q_n \to a$, then $a_n \to a$**?"""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 04""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Let $g(t) = t^2\sin(\frac{1}{t})$, $t \ne 0$ and $g(0) = 0$**.

    1. **Show that $g$ is differentiable and the derivative is not continuous. Find $g'(0)$**;
    2. **Define $F: \mathbb{R}^2 \to \mathbb{R}$, $F(x) = g(\| x \|)$. Show that $F$ has total derivative everywhere, including at $(0,0)$**;
    3. **Are the partial derivatives continuous**?
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
        r"""
    **Let** $$f(x) = \sum\limits_{k = 1}^{\infty}\frac{1}{n}(\frac{x}{x+4})^n.$$

    1. **Determine the exact set of $x \in \mathbb{R}$ such that $f(x)$ converges**;
    2. **When $x > 0$, calculate $f(x)$, justifying your steps**.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 06""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Let $f_n:[0,1] \to \mathbb{R}$ be continuous, equal to zero on $\{0\} \cup [\frac{1}{n},1]$, $f_n(\frac{1}{2n}) = 2n$ and linear on $[0,\frac{1}{2n}]$ and $[\frac{1}{2n},\frac{1}{n}]$**.

    1. **Show that $f_n(x)$ converges point-wise to a continuous function**;
    2. **Show that the integrals of $f_n$ do not converge to the integral of the limit**;
    3. **Does $f_n$ converge uniformly**?
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 07""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""**Assume $f: \mathbb{R}\to \mathbb{R}$ has a uniformly continuous derivative. Then** $$U(x) = \int_0^1f(tx)dt$$ **is well-defined on $\mathbb{R}$. Determine $U'(x)$ by using the definition of the derivative and carefully justifying your steps**."""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 08""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Let $(a_n)$ be a sequence of positive numbers such that $\sum\limits_{n = 0}^{\infty}a_n$ diverges. Show that**:

    1. **$f(x) = \sum\limits_{n=0}^{\infty}\frac{x^na_n}{1+a_n}$ converges on $(-1, 1)$ and the convergence is uniform on compact subsets of $(-1,1)$**;
    2. **$\sum\limits_{n=0}^{\infty}\frac{a_n}{1+a_n} = \infty$**.
    """
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
    **On $A = \{(x,y) \in \mathbb{R}^2|(x+y) \le (x+y)^2\}$, define** $$f(x,y) = x^2 - xy + y^2 - 2x.$$

    1. **Show that $A$ is closed but not compact**;
    2. **Justify that $f$ achieves its absolute minimum on $A$**;
    3. **Find the local critical points where $\nabla f(x,y) = (0,0)$**;
    4. **What is the absolute minimum? Which values must be considered**?
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
        r"""
    **Let** $$(x,y,z) \in \mathbb{R}^3, F(x,y,z) = (yz,xz,xy).$$

    1. **Determine the points where $F$ has a local continuous inverse $G(u,v,w)$**;
    2. **Calculate the total derivative of $G$ at $(1,1,1)$ with the formula in the Inverse Function Theorem**;
    3. **Calculate the inverse function directly, i.e. solve $(u,v,w) = F(x,y,z)$ for $(x,y,z)$**.
    """
    )
    return


if __name__ == "__main__":
    app.run()
