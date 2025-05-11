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
    In mathematics, an ==optimization problem== is a problem to find the best solution(s) from all **feasible** solutions.

    Optimization plays crucial roles in many fields, including the hottest topics today, machine learning and AI. There are a lot of typical optimization problems. A big category is to find the largest or smallest value. For example:

    1. The traveling-businessman problem: a businessman need to travel to $5$ (or any number greater than $1$) cities and go back home, the order of visit does not matter, what should be the order if he want to have the shortest distance traveled?
    2. Marginal profit problem: how many product should a company produce to maximize profit?
    3. Portfolio risk management: how should a hedge-fund manager allocate the fund to maximize return-to-risk ratio?
    4. Package design problem: how to design the package so that the material usage is the lowest and easy to be transported?

    There are also optimization problem of optimization problem. An rather 'easy' way to solve an optimization problem is to list *all* feasible solutions and find the best solution among them, but this usually takes a *very* long time. How do we acceleration this process? This is a very hot topic right now because it has very important application in the field of machine learning and AI.

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
    5. If $Q$ has been expressed as a function of more than one variable in Step 4, use the given information to find relationships (in the form of equations) among these variables. Then use these equations to eliminate all but one of the variables in the expression for $Q$. So that $Q$ is expressed as a function of **one** variable $x$, say, $Q = f(x)$. Write the domain of this function;
    6. Use the methods of Sections 3.1 and 3.3 to find the maximum or minimum value of $f$. In particular, if the domain of $f$ is a closed interval, then the Closed Interval Method in Section 3.1 can be used. If domain of $f$ is an open interval, you can use 3.3 to verify if it is a local minimum or maximum (and it automatically comes absolute extremum).
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Example 1""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    A company needs to produce a container of cylindrical shape to hold $1 \text{ L}$ (or $1000 \text{ cm}^3$) of liquid. Find the dimension of the container that minimize the material usage.

    Suppose we have a cylindrical container with height $h$ and radius $r$, then the volume of the container is $\pi r^2 h$, we want it to be $1000$. On the other hand, to produce such a cylindrical container we need two disks, and a rectangle shape of material.

    The disks have radius $r$, so we need $2 \pi r^2$ (unit in squared centimeter) of material to produce them; the rectangle has length $2\pi r$ (the perimeter of the disk) and width $h$, so we need $2\pi r h$ (unit in squared centimeter) of material to produce it.

    Thus the material usage is $A = 2\pi r^2 + 2\pi r h$. There are three quantities, and we want to minimize $A$ that depends on two quantities. We need to reduce the number of quantities using the relation between them.

    Since we have $\pi r^2 h = 1000$, we can rewrite $h = 1000/(\pi r^2)$. Substitute it to $A$, we get $$A = 2 \pi r^2 + 2\pi r \frac{1000}{\pi r^2} = 2\pi r^2 + \frac{2000}{r}.$$ Now we take the derivative of $A$ with respect to $r$ to find the critical number. We have $\displaystyle A' = 4\pi r - \frac{2000}{r^2}$ $\displaystyle = \frac{4(\pi r^3 -500)}{r^2}$, thus $A' = 0$ when $r = \sqrt[3]{500/\pi}$.

    Observe that if $r < \sqrt[3]{500/\pi}$, then $A'(r)<0$ and if $r > \sqrt[3]{500/\pi}$, then $A'(r) > 0$. Thus by the First Derivative Test, $A$ at $\sqrt[3]{500/\pi}$ is a local minimum. In fact, it is the absolute minimum.

    We can then calculate $h$ corresponds to this $r$, that is $\displaystyle h = \frac{1000}{\pi r^2} = \frac{1000}{\pi(500/\pi)^{2/3}}$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Example 2""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    There are $50$ apple trees in an orchard and each of them are producing $800$ apples. For each additional tree planted in the orchard, the output of each tree drops by $10$ apples. How many trees should be added to the existing orchard to maximize the total output?

    Suppose we add $x$ apple trees, then there are $50+x$ trees and the output per tree becomes $800 - 10x$, thus the total output is $(50+x)(800 - 10x) = O$. Take derivative with respect to $x$, we get $O' = 300 - 20x$, it is $0$ when $x = 15$. It is easy to see that when $x<15$, $O'>0$, and when $x > 15$, $O'<0$, so this is the absolute maximum. Thus we should plant $15$ more trees.
    """
    )
    return


@app.cell
def _(mo):
    n_trees = mo.ui.slider(0, 80, value=50, label="Number of Trees to Plant")
    n_trees
    return (n_trees,)


@app.cell
def _(n_trees):
    print('Try it youself using the above slidebar!')
    total_output = (50+n_trees.value) * (800 - 10*n_trees.value)
    print(f'If we plant {n_trees.value} new trees, total output is going to be {total_output}.')
    return


@app.cell
def _(mo):
    mo.md(r"""### Example 3""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Find the area of the largest rectangle that can be inscribed inside the ellipse $\displaystyle \frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ for arbitrary positive constant $a, b$.

    Notice that, the vertices of the rectangle is on four different quadrant, and once the vertices inside one quadrant is chosen, the other three are fixed. Thus we can assume we are choosing from the first quadrant - that is, both $x, y$ are positive.

    Suppose then we choose a positive $x$, then $y$ is fixed by the formula $\displaystyle y = \sqrt{1- \frac{x^2}{a^2}}\cdot b$. The area of the rectangle is then $\displaystyle A = 4xy = 4 x \sqrt{1- \frac{x^2}{a^2}}\cdot b$. We want to maximize this $A$.

    Take the derivative we get $\displaystyle A' = \frac{4b(a^2 - 2x^2)}{a^2\sqrt{1-\frac{x^2}{a^2}}}$, thus it equals $0$ when $2x^2 = a^2$, or $\displaystyle x = \frac{\sqrt{2}}{2}\cdot a$ (we assumed $x$ and $a$ are positive). It is not hard to check with the First Derivative Test and Closed Interval Method (notice $0\le x \le a$) that this is the (absolute) maximum.

    If $\displaystyle x = \frac{\sqrt{2}}{2}\cdot a$, then $\displaystyle y = \frac{\sqrt{2}}{2}\cdot b$, and thus the area of the rectangle is $4xy = 2ab$.
    """
    )
    return


@app.cell
def _(mo, np):
    x_slider = mo.ui.slider(steps=np.linspace(0, 5, 10001), label="x Coordinate of the top-right vertice", value=0)
    x_slider
    return (x_slider,)


@app.cell
def _(go, np, x_slider):
    # Ellipse parametric points
    theta_e = np.linspace(0, 2 * np.pi, 400)
    x_ellipse = 5 * np.cos(theta_e)
    y_ellipse = 3 * np.sin(theta_e)

    # Top-right corner from slider
    x_rect = x_slider.value
    y_rect = np.sqrt(9 * (1 - x_rect**2 / 25))  # From ellipse equation

    # Rectangle vertices (counterclockwise)
    rect_x = [-x_rect, x_rect, x_rect, -x_rect, -x_rect]
    rect_y = [-y_rect, -y_rect, y_rect, y_rect, -y_rect]

    # Area of rectangle
    area = 4 * x_rect * y_rect

    # Create figure
    fig_ellipse = go.Figure()

    # Ellipse outline
    fig_ellipse.add_trace(go.Scatter(
        x=x_ellipse, y=y_ellipse,
        mode='lines',
        name='Ellipse',
        line=dict(color='blue')
    ))

    # Shaded rectangle
    fig_ellipse.add_trace(go.Scatter(
        x=rect_x, y=rect_y,
        fill='toself',
        name='Inscribed Rectangle',
        fillcolor='rgba(255,165,0,0.4)',
        line=dict(color='orange')
    ))

    # Label the area near the center
    fig_ellipse.add_trace(go.Scatter(
        x=[0], y=[0],
        mode='text',
        text=[f"Area = {area:.2f}"],
        textposition='middle center',
        showlegend=False
    ))

    # Top-right corner marker
    fig_ellipse.add_trace(go.Scatter(
        x=[x_rect], y=[y_rect],
        mode='markers+text',
        text=[f"({x_rect:.2f}, {y_rect:.2f})"],
        textposition='top right',
        marker=dict(size=8, color='red'),
        name='Top-right corner'
    ))

    # Layout
    fig_ellipse.update_layout(
        title='Example When a = 5 and b = 3',
        xaxis_title='x',
        yaxis_title='y',
        xaxis=dict(scaleanchor='y', range=[-6, 6]),
        yaxis=dict(scaleanchor='x', range=[-4, 4]),
        template='plotly_white'
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Example 4""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Let us do example 3 again but this time without using calculus.

    Let $m, n$ be any two values, we must have $(m-n)^2 \ge 0$ because LHS is a square. Expand it, we get $m^2 + n^2 - 2mn \ge 0$, or $m^2 + n^2 \ge 2mn$. That is, **for any two quantities** $m, n$, we must have $m^2 + n^2 \ge 2mn$, and $m^2 + n^2 = 2mn$ if and only if $m = n$ (that is when $(m-n)^2 = 0$).

    Now take $\displaystyle m = \frac{x}{a}$ and $\displaystyle n = \frac{y}{b}$, we must have $\displaystyle 1 = \frac{x^2}{a^2} + \frac{y^2}{b^2} \ge 2\frac{xy}{ab}$.

    Now remember to maximize the area, it is the same to maximize $4xy$. We know from above that $\displaystyle 2 \frac{xy}{ab}$ is bounded above by $1$ (and it is achievable, when $\displaystyle \frac{x}{a} = \frac{y}{b}$), thus $4xy$ is bounded above by $2ab$ and it is achieved when $\displaystyle \frac{x}{a} = \frac{y}{b}$.
    """
    )
    return


if __name__ == "__main__":
    app.run()
