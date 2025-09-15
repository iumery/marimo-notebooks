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
    mo.md(r"""## Problem 1""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Let $\mathbb{R}^{\omega}$ be the Cartesian product of countably many copies of the real line, and $f: \mathbb{R} \to \mathbb{R}^{\omega}$ the diagonal function $f(x) = (x,x,\dots,x,\dots)$**.

    1. **Is $f$ continuous with respect to the product topology on $\mathbb{R}^{\omega}$? Explain**;
    2. **Is $f$ continuous with respect to the box topology on $\mathbb{R}^{\omega}$? Explain**.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 2""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Let $f_n: \mathbb{R} \to \mathbb{R}$ be a sequence of continuous functions defined by the formula** $$f_n(x) = \begin{cases} \frac{1}{n}\sqrt{n^2 - x^2},&|x|<n,\\0,&|x|\ge n.\end{cases}$$

    1. **Show that the sequence $f_n(x)$ converges point-wise and find its limit**;
    2. **Does the sequence $f_n(x)$ converges uniformly? Explain**.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 3""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Prove or disprove the following statements with brief but complete reasoning**:

    1. **Any infinite set with the finite complement topology is connected**;
    2. **The real line with the lower limit topology is connected**;
    3. **The complement of the central circle in the Möbius band is connected**;
    4. **The union of the graphs $y = e^x$ and $y = 0$ in the coordinate $xy$-plane is connected**.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 4""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""**Let $X$ be a Hausdorff topological space and suppose that you are given a nested collection** $$\dots \subset C_n \subset C_{n-1} \subset \dots \subset C_2 \subset C_1$$ **of non-empty compact subspaces of $X$. Prove that the intersection** $$C = \bigcap_{n=1}^{\infty}C_n$$ **is non-empty and compact**."""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 5""")
    return


@app.cell
def _(mo):
    mo.md(r"""**Prove that the set $X = \{(x,y) \in \mathbb{R}^2|x^2 = y^3\}$ is not a smooth manifold**.""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 6""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""**Let $S^1$ be the unit circle $x^2 + y^2 = 1$ in the coordinate $xy$-plane. Find all the critical points of the function $f: S^1 \to \mathbb{R}$ given by the formula $f(x,y) = xy$**."""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 7""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""**Let $X$ be a compact smooth oriented manifold with boundary. Prove that there does not exist a smooth retraction of $X$ onto its boundary $\partial X$**."""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 8""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""**Let the Euclidean space $\mathbb{R}^4$ have coordinates $x, y, z$ and $w$. Integrate the differential $2$-form** $$dz \wedge dw + xzdy \wedge dw$$ **over the torus $T \subset \mathbb{R}^4$ given by the equations $x^2 + y^2 = 1$ and $z^2 + w^2 = 1$**."""
    )
    return


if __name__ == "__main__":
    app.run()
