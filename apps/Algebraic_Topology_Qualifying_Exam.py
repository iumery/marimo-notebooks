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
    mo.md(r"""## Problem 1""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Let $X$ be the CW-complex obtained from a Möbius band and $\mathbb{R}P^2$ by identifying the boundary of the Möbius band with $\mathbb{R}P^1 \subset \mathbb{R}P^2$**.

    1. **Calculate the fundamental group of $X$**;
    2. **Calculate the homology groups of $X$**;
    3. **Calculate the cohomology groups of $X$ with $\mathbb{Z}_2$ coefficients**.

    Idea

    Part 1 and 2: direct calculation. Part 3: use Universal Coefficient Theorems.
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
    **Is the one point union $S^2 \vee S^4$ homotopy equivalent to a closed manifold? Explain why or why not**.

    Idea

    Argue that the cap product structure that realizes Poincaré Duality fails.
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
    **Determine the connected covers of $\mathbb{R}P^2 \vee \mathbb{R}P^2$ of degrees $2, 3$ and $4$, if any**.

    Idea

    Calculate the fundamental group, find index $2$ and $4$ subgroups, and argue that there is no index $3$ subgroup.
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
        r"""
    1. **Prove that a closed odd dimensional manifold has zero Euler characteristic**;
    2. **Can $\mathbb{R}P^4$ be the boundary of a compact manifold? Explain**.

    Idea

    Part 1: for orientable manifold, use Poincaré Duality; for non-orientable manifold, consider orientation double cover.

    Part 2: use part 1 to show it is impossible.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 5""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **The $n$-dimensional torus $T^n$ is the $n$-fold product $S^1 \times \cdots \times S^1$. For each positive integer $k$, determine $H_k(T^{2k})$ and $\pi_k(T^{2k})$**.

    Idea

    Direct calculation.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 6""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Recall that $[X, Y]$ denotes the set of homotopy classes of continuous maps from $X$ to $Y$ . Suppose $M$ is a closed $4$-manifold with a CW-structure, prove that $[M, \mathbb{C}P^{\infty}] = [M, \mathbb{C}P^2]$**.

    Idea

    Use the fact that the $(\dim(M) + 1)$-skeleton of $\mathbb{C}P^{\infty}$ is $\mathbb{C}P^2$.
    """
    )
    return


if __name__ == "__main__":
    app.run()
