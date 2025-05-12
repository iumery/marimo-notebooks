import marimo

__generated_with = "0.13.6"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import plotly.graph_objects as go

    return go, mo, np


@app.cell
def _(mo):
    nav_menu = mo.nav_menu(
        {
            "/index.html": f"{mo.icon('lucide:home')} Home",
            "Optimization Problems Example Sets": {
                "/apps/Calculus_I_18_1.html": f"{mo.icon('lucide:file-text')} Set 1",
                "/apps/Calculus_I_18_2.html": f"{mo.icon('lucide:file-text')} Set 2",
                "/apps/Calculus_I_18_3.html": f"{mo.icon('lucide:file-text')} Set 3",
                "/apps/Calculus_I_18_4.html": f"{mo.icon('lucide:file-text')} Set 4",
                "/apps/Calculus_I_18_5.html": f"{mo.icon('lucide:file-text')} Set 5",
            },
        },
        orientation="vertical",
    )
    nav_menu
    return


@app.cell
def _(mo):
    mo.md(r"""# 3.5 Optimization Problems""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Introduction""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    In mathematics, an optimization problem is a problem to find the best solution(s) from all **feasible** solutions.

    Optimization plays crucial roles in many fields, including the hottest topics today, machine learning and AI. There are a lot of typical optimization problems. A big category is to find the largest or smallest value. For example:

    1. The traveling-businessman problem: a businessman need to travel to $5$ (or any number greater than $1$) cities and go back home, the order of visit does not matter, what should be the order if he want to have the shortest distance traveled?
    2. Marginal profit problem: how many product should a company produce to maximize profit?
    3. Portfolio risk management: how should a hedge-fund manager allocate the fund to maximize return-to-risk ratio?
    4. Package design problem: how to design the package so that the material usage is the lowest and easy to be transported?

    There are also optimization problem of optimization problem. An rather 'easy' way to solve an optimization problem is to list *all* feasible solutions and find the best solution among them, but this usually takes a *very* long time. How do we acceleration this process? This is a very hot topic right now because computing power is a crucial part of AI.

    There are tons of methods to solve optimization problems. Some of them can be solved purely algebraically. Some of them need more complicated methods (if you are interested in it, you can google keywords like 'linear programming', 'quadratic programming', or 'dynamic programming').

    In the scope of this course, **we mainly study optimization problems that can be described by a function, and we find the maximum and minimum value using the method we had in section 3.1**.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Strategy of Solve Optimization Problem""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Like related rates problem in section 2.7, optimization problems are often described as a word problem. As a result, we need to interpret a problem before doing it. To solve an optimization problem, we can follow the guideline from the book:

    1. Understand the Problem: The first step is to read the problem carefully until it is clearly understood. Ask yourself: What is the unknown? What are the given quantities? What are the given conditions?
    2. Draw a Diagram: In most problems it is useful to draw a diagram and identify the given and required quantities on the diagram;
    3. Introduce Notation: Assign a symbol to the quantity that is to be maximized or minimized (let's call it $Q$ for now). Also select symbols $a, b, c, \dots, x, y$ for other unknown quantities and label the diagram with these symbols. It may help to use initials as suggestive symbols — for example, $A$ for area, $h$ for height, $t$ for time;
    4. Express $Q$ in terms of some of the other symbols from Step 3;
    5. If $Q$ has been expressed as a function of more than one variable in Step 4, use the given information to find relationships (in the form of equations) among these variables. Then use these equations to eliminate all but one of the variables in the expression for $Q$. So that $Q$ is expressed as a function of **one** variable $x$, say, $Q = f(x)$. Determine the domain of this function;
    6. Use the methods of Sections 3.1 and 3.3 to find the maximum or minimum value of $f$. In particular, if the domain of $f$ is a closed interval, then the Closed Interval Method in Section 3.1 can be used. If domain of $f$ is an open interval, you can use 3.3 to verify if it is a local minimum or maximum (and it automatically comes absolute extremum).
    """
    )
    return


if __name__ == "__main__":
    app.run()
