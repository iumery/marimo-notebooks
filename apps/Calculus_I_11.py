import marimo

__generated_with = "0.13.15"
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
        },
        orientation="vertical",
    )
    nav_menu
    return


@app.cell
def _(mo):
    mo.md(r"""# 2.6 Application of Chain Rule Implicit Differentiation""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Motivation""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Recall a function $f: X \to Y$ is a rule that assigns **each** $x \in X$ **exactly one** value $f(x) = y \in Y$. If a rule assigns an $x$ more than one value in $Y$, its graph will fail the vertical-line-test, and this rule cannot be a function.

    **(Throughout this section, $y$ is always a variable that depends on $x$)**

    Sometimes this restriction makes our life (unnecessarily) hard. For example, if we want to consider a (set of) rule, such that it's graph is a circle, then we have to use (at least) two functions, otherwise it will fail the vertical-line-test:
    """
    )
    return


@app.cell
def _(go, np):
    # Unit circle parameterization
    theta = np.linspace(0, 2 * np.pi, 500)
    x_circle = np.cos(theta)
    y_circle = np.sin(theta)

    # Vertical line at x = 0.5
    x_line = np.full(500, 0.5)
    y_line = np.linspace(-1.2, 1.2, 500)

    # Create figure
    fig_1 = go.Figure()

    # Circle
    fig_1.add_trace(
        go.Scatter(
            x=x_circle,
            y=y_circle,
            mode="lines",
            name="Unit Circle",
            line=dict(color="blue"),
        )
    )

    # Vertical line
    fig_1.add_trace(
        go.Scatter(
            x=x_line,
            y=y_line,
            mode="lines",
            name="x = 0.5",
            line=dict(color="red", dash="dot"),
        )
    )

    # Intersections (for clarity)
    intersect_y = np.sqrt(1 - 0.5**2)
    fig_1.add_trace(
        go.Scatter(
            x=[0.5, 0.5],
            y=[intersect_y, -intersect_y],
            mode="markers",
            marker=dict(size=10, color="black"),
            name="Intersections",
        )
    )

    # Layout
    fig_1.update_layout(
        title="Unit Circle and Vertical Line (Fails Vertical Line Test)",
        xaxis_title="x",
        yaxis_title="y",
        xaxis=dict(scaleanchor="y"),
        yaxis=dict(scaleanchor="x"),
        template="plotly_white",
        showlegend=True,
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    So in certain cases, we would like to lift this restriction, and write the rule differently. For example, a point is on the unit circle if and only if its coordinate $(x, y)$ satisfies $x^2 + y^2 = 1$ (this is not a function!). A rule described in this way is called an implicit function.

    Sometimes it is possible to solve this equation so that we can express $y$ as one or more functions of $x$, but not always.

    (To differ implicit function and function in the usual sense, sometimes we call function in the usual sense 'explicit function'. Technically, explicit function is a type of implicit function.)

    For example, the implicit function $x^2 + y^2 = 1$ can be expresses by two explicit functions $y = \sqrt{1 - x^2}$ and $y = -\sqrt{1 - x^2}$ (their graphs are the upper & lower half-circles, respectively).
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Example (Folium of Descartes)""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""The curve described by $x^3 + y^3 - 3axy = 0$ for some positive $a$ is known as the folium of Descartes:"""
    )
    return


@app.cell
def _(go, np):
    # Create a grid over x and y
    x = np.linspace(-4, 4, 400)
    y = np.linspace(-4, 4, 400)
    X, Y = np.meshgrid(x, y)

    # Define the implicit function: F(x, y) = x^3 + y^3 - 6xy
    Z = X**3 + Y**3 - 6 * X * Y

    # Plot the zero-level contour: F(x, y) = 0
    fig_2 = go.Figure()

    fig_2.add_trace(
        go.Contour(
            x=x,
            y=y,
            z=Z,
            contours=dict(
                coloring="none",
                showlabels=True,
                labelfont=dict(size=12, color="black"),
                start=0,
                end=0,
                size=1,
            ),
            line=dict(color="blue"),
            showscale=False,
            name=r"$x^3 + y^3 - 6xy = 0$",
        )
    )

    # Make it square
    fig_2.update_layout(
        title=r"Implicit Curve: $x^3 + y^3 - 6xy = 0$",
        xaxis_title="x",
        yaxis_title="y",
        xaxis=dict(scaleanchor="y"),
        yaxis=dict(scaleanchor="x"),
        template="plotly_white",
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""This curve fails the vertical-line-test, but can be expressed as few pieces of graphs of functions together:"""
    )
    return


@app.cell
def _(go, np):
    # Create a grid
    x_e = np.linspace(-3, 4, 8000)
    y_e = np.linspace(-3, 4, 8000)
    X_e, Y_e = np.meshgrid(x_e, y_e)
    Z_e = X_e**3 + Y_e**3 - 6 * X_e * Y_e

    # Approximate zero level set
    tol = 0.001
    mask = np.abs(Z_e) < tol
    x_vals = X_e[mask]
    y_vals = Y_e[mask]

    # Categorize by quadrant
    branches = {
        "lower-right": (x_vals > 0) & (y_vals < 0),
        "upper-left": ((x_vals < 0) & (y_vals > 0))
        | ((x_vals > 0) & (y_vals > 0) & (x_vals > y_vals)),
        "upper-right": (x_vals > 0) & (y_vals > 0) & (x_vals < y_vals),
    }

    styles = {
        "lower-right": dict(color="red", dash="dot"),
        "upper-left": dict(color="green", dash="dash"),
        "upper-right": dict(color="blue", dash="solid"),
    }

    fig_3 = go.Figure()

    # For each branch, extract, sort, and plot
    for name, cond in branches.items():
        x_branch = x_vals[cond]
        y_branch = y_vals[cond]

        # Sort by x if x variation is dominant, else by y
        if np.ptp(x_branch) > np.ptp(y_branch):
            sorted_indices = np.argsort(x_branch)
        else:
            sorted_indices = np.argsort(y_branch)

        x_sorted = x_branch[sorted_indices]
        y_sorted = y_branch[sorted_indices]

        fig_3.add_trace(
            go.Scatter(
                x=x_sorted,
                y=y_sorted,
                mode="markers",
                line=styles[name],
                name=name.replace("-", " ").title(),
            )
        )

    # Layout
    fig_3.update_layout(
        title=r"Smooth Explicit Branches of $x^3 + y^3 - 6xy = 0$",
        xaxis_title="x",
        yaxis_title="y",
        xaxis=dict(scaleanchor="y"),
        yaxis=dict(scaleanchor="x"),
        template="plotly_white",
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    (The above picture is not an *exactly* correct illustration, can you see why?)

    It is hard, though possible, to write down these functions explicitly. So why do we need implicit functions? Because sometimes it is impossible to write an implicit function into multiple explicit ones.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Motivation, Continued""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    In general, implicit functions like above, i.e. implicit functions of the form $P_n(x)y^n + P_{n-1}(x)y^{n-1}+\dots + P_1(x)y + P_0(x) = 0$, where $P_i(x)$'s are polynomials of $x$, are called algebraic functions (in particular, there is no terms like $\sin(x)$, etc.).

    You may think that implicit functions, or at least algebraic functions, can always be written as a collection of explicit functions. But this is not true. In fact, this is not true even for algebraic functions. **In general, quintic polynomials (polynomials with degree $5$) do not have explicit solutions**, thus in general an algebraic function with highest degree of $y$ being greater than or equals to $5$ cannot be expressed as a collection of explicit functions (of $x$).

    The point is: for an implicit function, $y$ still depends on $x$, so it still makes sense to talk about 'rate of change of $y$ with respect to $x$', or in other words, derivative of $y$ with respect to $x$. For some of the implicit functions, like the circle, we can write it as a collection of explicit functions and evaluate the derivative in the old way. However, **we need a different method if we cannot find the explicit functions, or if these functions are too hard to be written**. We call the procedure of differentiating an implicit function 'implicit differentiation'. It is done as follow:
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Implicit Differentiation""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Implicit differentiation (with respect to $x$) is done by viewing $y$ as a function of $x$. We calculate the derivative in the usual manner - with the only difference that whenever we see $y$, we treat it with the Chain Rule.

    Let us calculate $y'$ for the implicit function $x^3 + y^3 = 6xy$:

    1. Write differential signs at each sides: $(x^3 + y^3)' = (6xy)'$. **Keep in mind that we are differentiating with respect to $x$**;
    2. For LHS, first we use summation rule: $(x^3 + y^3)' = (x^3)' + (y^3)'$. The derivative of $x^3$ is $3x^2$ as usual. The derivative of $y^3$ can be more carefully written as $\bigg(\Big(y(x)\Big)^3\bigg)'$ and we apply the Chain Rule, which says it equals the product of:
    	1. The derivative of $y^3$ with respect to $y$, which is $3y^2$, and
    	2. The derivative of $y$ with respect to $x$, which we do not know (*this is what we are looking for*!), so we just put $y'$ here. That is, the derivative of $y^3$ with respect to $x$ is $3y^2y'$. Put things together, the LHS equals $3x^2 + 3y^2y'$;
    3. For RHS, **there is a product $x$ times $y$, so we need to apply the product rule**: $(6xy)' = (6x)'y + 6x(y)'$, which equals $6y + 6xy'$;
    4. Put things together, we get that $$3x^2 + 3y^2y' = 6y + 6xy';$$
    5. We are not done just yet. The ultimate goal is to find the derivative of $y$ with respect to $x$, which is $y'$ in our notation. Thus our final answer should be in the format $y' = f(x, y)$ where $f(x,y)$ is some expression in terms of $x$ and $y$. We can achieve this by some basic algebra. The result is $$y' = \frac{2y - x^2}{y^2 - 2x}.$$

    To find the (implicit) derivative at a specific point, just plugin values. For example, the (implicit) derivative of the above implicit function at $(3, 3)$ (check, is this point on the graph?) is $$y' = \frac{2 \cdot 3 - 3^2}{3^2 - 2 \cdot 3} = -1.$$ As usual, this value can be viewed as the slope of tangent line to the curve of Folium of Descartes at point $(3,3)$:
    """
    )
    return


@app.cell
def _(go, np):
    # Grid for implicit function
    x_t = np.linspace(-1, 4, 500)
    y_t = np.linspace(-1, 4, 500)
    X_t, Y_t = np.meshgrid(x_t, y_t)
    Z_t = X_t**3 + Y_t**3 - 6 * X_t * Y_t

    # Tangent line at (3, 3): y = -x + 6
    x_line_t = np.linspace(1, 5, 200)
    y_tangent_t = -x_line_t + 6

    # Plot
    fig_4 = go.Figure()

    # Implicit curve (contour at level 0)
    fig_4.add_trace(
        go.Contour(
            x=x_t,
            y=y_t,
            z=Z_t,
            contours=dict(start=0, end=0, size=1, coloring="none"),
            line=dict(color="blue", width=3),
            showscale=False,
            name="Descartes Folium",
        )
    )

    # Tangent line
    fig_4.add_trace(
        go.Scatter(
            x=x_line_t,
            y=y_tangent_t,
            mode="lines",
            line=dict(color="red", dash="dash"),
            name="Tangent at (3, 3)",
        )
    )

    # Mark the point (3, 3)
    fig_4.add_trace(
        go.Scatter(
            x=[3],
            y=[3],
            mode="markers+text",
            text=["(3, 3)"],
            textposition="top right",
            marker=dict(size=8, color="black"),
            name="Point (3, 3)",
        )
    )

    # Layout
    fig_4.update_layout(
        title=r"Descartes Folium and Tangent Line at (3, 3)",
        xaxis_title="x",
        yaxis_title="y",
        xaxis=dict(scaleanchor="y"),
        yaxis=dict(scaleanchor="x"),
        template="plotly_white",
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Like the usual derivative, **the implicit derivative may not be well-defined**.

    Let us still consider the Folium of Descartes $x^3 + y^3 = 6xy$. Can we make sense of the derivative at $(0,0)$? In the above sense, we cannot - because both lines $x = 0$ and $y = 0$ are tangential to the curve. These two lines obviously have different slopes, but we should only have one derivative. In fact, one of the two lines even has infinite slope because the direction is vertical (and recall that we don't allow infinite derivative)!

    There are in fact ways to make sense of this derivative. One of them is called parametrization. It is a rather important topic especially in physics and engineering, but it is beyond the scope of this course.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Implicit Differentiation Made Simple""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    To simply describe the above method, first we need to decide what is the independent variable and which is the dependent one. This should be specified in the question. For example, if a question is asking for $\frac{dy}{dx}$ then it means that $x$ is the independent variable and $y$ is the dependent one.

    Now, to evaluate derivative:

    1. If you need to take derivative of an expression that contains both the independent and the dependent variables, then you need to use rules to separate them first, then apply the following two (or you may need to separate further). E.g. to evaluate $(x^2y^2)'$ you need to realize this is a product and do $= (x^2)'y^2 + x^2(y^2)'$;
    2. If you need to take derivative of an expression that **contains the independent variable only**, then you just take derivative in the usual way. E.g. $(3x^2)' = 6x$;
    3. If you need to take derivative of an expression that **contains the dependent variable only**, then you take derivative in the usual way, then multiply it by derivative of the dependent variable, which is what we are looking for. E.g. $(3y^2)' = 6y \cdot y'$, because $6y$ is the usual derivative, and $y'$ is just the notation for derivative.

    Do algebra to finish:

    1. First, put every term with $y'$ to one side, and everything else to the other side of the equation;
    2. Factor out $y'$ on the first side;
    3. Take quotient and get expression of $y'$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### A Very Common Mistake""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""When you take derivative of a constant, it goes away. **In particular, derivative of $\pi$ is $0$, so does $\pi^2$- that is still a constant**. For example, if you have $y^2 = x^2 + \sin(\pi^2)$, then by taking derivative we just get $2yy' = 2x$. $(\sin(\pi^2))' = 0$ no matter how complex it looks, it is a constant number."""
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
    Many things that we know about derivative still work for implicit derivative.

    Assume $y$ is a function of $x$, find $y'$ for $$y^2 = 4 x^2 (1 − x^2).$$ When is this derivative not existing? When is the tangent line horizontal? Give answers in $(x,y)$ coordinates.

    Answer:

    $$y' = \frac{4x-8x^3}{y},$$ thus it does not exist when $y = 0$. To find the $x$ values corresponds to $y = 0$, we solve for $4 x^2 (1-x^2) = 0$ - this should be easy because it is already factored for you, the solutions are $x = 0$, $-1$ or $1$. That is, the implicit function is not differentiable at $(0,0), (-1, 0)$ and $(1, 0)$.

    Horizontal tangent line happens when $y' = 0$, that is $4x - 8x^3 = 0$, or $4x(1-2x^2) = 0$. We get that $x = 0$, $\displaystyle \frac{\sqrt{2}}{2}$ or $\displaystyle - \frac{\sqrt{2}}{2}$. However, plug it back to the original implicit function we get that $x = 0$ corresponds to $y = 0$, and we just showed that at the point $(0,0)$ the implicit function is not differentiable. Thus $\displaystyle x = \pm \frac{\sqrt{2}}{2}$, plug them back to the original implicit function, we get that in both case $y = \pm 1$. So there are four points with horizontal tangent, $\displaystyle (\pm \frac{\sqrt{2}}{2}, \pm 1)$:
    """
    )
    return


@app.cell
def _(go, np):
    # Define a grid
    x_f = np.linspace(-1.2, 1.2, 100)
    y_f = np.linspace(-1.5, 1.5, 100)
    X_f, Y_f = np.meshgrid(x_f, y_f)

    # Define the implicit function: F(x, y) = y² - 4x²(1 - x²)
    Z_f = Y_f**2 - 4 * X_f**2 * (1 - X_f**2)

    # Define the four labeled points
    from math import sqrt

    x_pts = [sqrt(2) / 2, sqrt(2) / 2, -sqrt(2) / 2, -sqrt(2) / 2]
    y_pts = [1, -1, 1, -1]
    labels = [
        r"$(+\sqrt{2}/2, +1)$",
        r"$(+\sqrt{2}/2, -1)$",
        r"$(-\sqrt{2}/2, +1)$",
        r"$(-\sqrt{2}/2, -1)$",
    ]

    # Create figure
    fig_5 = go.Figure()

    # Plot the curve implicitly
    fig_5.add_trace(
        go.Contour(
            x=x_f,
            y=y_f,
            z=Z_f,
            contours=dict(start=0, end=0, size=1, coloring="none"),
            line=dict(color="blue", width=3),
            showscale=False,
            name=r"$y^2 = 4x^2(1 - x^2)$",
        )
    )

    # Add the four points
    fig_5.add_trace(
        go.Scatter(
            x=x_pts,
            y=y_pts,
            mode="markers+text",
            marker=dict(color="red", size=8),
            text=labels,
            name="Horizontal Tangent Points",
        )
    )

    # Layout
    fig_5.update_layout(
        title=r"Curve $y^2 = 4x^2(1 - x^2)$ with Horizontal Tangent Points",
        xaxis_title="x",
        yaxis_title="y",
        xaxis=dict(scaleanchor="y"),
        yaxis=dict(scaleanchor="x"),
        template="plotly_white",
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
    Assume $y$ is a function of $x$, find $y'$ for $$\cos^2(x) + \cos^2(y) = \cos(2x+2y).$$

    The answer is: $$y' = \frac{\cos(x)\sin(x) - \sin(2x+2y)}{\sin(2x+2y) - \cos(y)\sin(y)}.$$
    """
    )
    return


if __name__ == "__main__":
    app.run()
