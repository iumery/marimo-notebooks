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
    mo.md(
        r"""
    # Introduction

    This notebook series is a hands-on introduction to several core topics in Topological Data Analysis (TDA). The current collection covers a range of subjects including:

    - Topological spaces and homeomorphisms
    - Geometric realization of simplicial complexes
    - Vietoris-Rips complexes
    - Homology computation (including persistence)
    - Mapper algorithm
    - Morse theory and Reeb graphs
    - Sheaf theory on simplicial complexes
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Prerequisites

    This series is not meant to be formal or mathematically rigorous. It's more like me trying to write down what I learned and how I understand these topics, mostly by coding things out directly.

    Some basic background in (algebraic) topology will definitely help. If you've seen things like topological spaces, continuous maps, simplicial complexes, or homology groups, you'll probably feel more comfortable following along.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Reference

    **Tamal K. Dey & Yusu Wang, _Computational Topology for Data Analysis_**

    A free pre-publication version is available online. This is a highly recommended reference for anyone interested in a rigorous but approachable introduction to the subject. The notebooks in this project do not directly follow the book's structure or notation, and occasionally take a slightly different route for demonstration and illustration purposes.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Philosophy of This Series

    The idea of these notebooks is to try and build as much as possible from scratch, not because that's always efficient or practical, but because it's the best way to really see how these algorithms work.

    I avoided using big TDA libraries most of the time, so you'll see lots of very naive, unoptimized code that just walks through the basic logic step by step. These are definitely not production-ready implementations.

    If you're interested in real-world TDA pipelines, you should definitely check out well-developed packages like gudhi, ripser, giotto-tda, and others. They're far better for serious applications.
    """
    )
    return


if __name__ == "__main__":
    app.run()
