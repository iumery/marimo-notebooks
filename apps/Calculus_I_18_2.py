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
    mo.md(r"""# 3.5 Optimization Problems Example Set 2""")
    return


@app.cell
def _(mo):
    mo.md(r"""### Example 3""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""Find the area of the largest rectangle that can be inscribed inside the ellipse $\displaystyle \frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ for arbitrary positive constant $a, b$."""
    )
    return


@app.cell
def _(mo, np):
    x_slider = mo.ui.slider(
        steps=np.linspace(0, 5, 10001),
        label="x Coordinate of the top-right vertice",
        value=2.5,
    )
    x_slider
    return (x_slider,)


@app.cell
def _(mo):
    mo.md(r"""**Try it youself using the above slidebar!**""")
    return


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
    fig_ellipse.add_trace(
        go.Scatter(
            x=x_ellipse,
            y=y_ellipse,
            mode="lines",
            name="Ellipse",
            line=dict(color="blue"),
        )
    )

    # Shaded rectangle
    fig_ellipse.add_trace(
        go.Scatter(
            x=rect_x,
            y=rect_y,
            fill="toself",
            name="Inscribed Rectangle",
            fillcolor="rgba(255,165,0,0.4)",
            line=dict(color="orange"),
        )
    )

    # Label the area near the center
    fig_ellipse.add_trace(
        go.Scatter(
            x=[0],
            y=[0],
            mode="text",
            text=[f"Area = {area:.2f}"],
            textposition="middle center",
            showlegend=False,
        )
    )

    # Top-right corner marker
    fig_ellipse.add_trace(
        go.Scatter(
            x=[x_rect],
            y=[y_rect],
            mode="markers+text",
            text=[f"({x_rect:.2f}, {y_rect:.2f})"],
            textposition="top right",
            marker=dict(size=8, color="red"),
            name="Top-right corner",
        )
    )

    # Layout
    fig_ellipse.update_layout(
        title="Example When a = 5 and b = 3",
        xaxis_title="x",
        yaxis_title="y",
        xaxis=dict(scaleanchor="y", range=[-6, 6]),
        yaxis=dict(scaleanchor="x", range=[-4, 4]),
        template="plotly_white",
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Solution:

    Notice that, the vertices of the rectangle is on four different quadrant, and once the vertices inside one quadrant is chosen, the other three are fixed. Thus we can assume we are choosing from the first quadrant - that is, both $x, y$ are positive.

    Suppose then we choose a positive $x$, then $y$ is fixed by the formula $\displaystyle y = \sqrt{1- \frac{x^2}{a^2}}\cdot b$. The area of the rectangle is then $\displaystyle A = 4xy = 4 x \sqrt{1- \frac{x^2}{a^2}}\cdot b$. We want to maximize this $A$.

    Take the derivative we get $\displaystyle A' = \frac{4b(a^2 - 2x^2)}{a^2\sqrt{1-\frac{x^2}{a^2}}}$, thus it equals $0$ when $2x^2 = a^2$, or $\displaystyle x = \frac{\sqrt{2}}{2}\cdot a$ (we assumed $x$ and $a$ are positive). It is not hard to check with the First Derivative Test and Closed Interval Method (notice $0\le x \le a$) that this is the (absolute) maximum.

    If $\displaystyle x = \frac{\sqrt{2}}{2}\cdot a$, then $\displaystyle y = \frac{\sqrt{2}}{2}\cdot b$, and thus the area of the rectangle is $4xy = 2ab$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Example 3.1""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Let us do example 3 again but this time without using calculus.

    Let $m, n$ be any two values, we must have $(m-n)^2 \ge 0$ because LHS is a square. Expand it, we get $m^2 + n^2 - 2mn \ge 0$, or $m^2 + n^2 \ge 2mn$. That is, for any two quantities $m, n$, we must have $m^2 + n^2 \ge 2mn$, and $m^2 + n^2 = 2mn$ if and only if $m = n$ (that is when $(m-n)^2 = 0$).

    Now take $\displaystyle m = \frac{x}{a}$ and $\displaystyle n = \frac{y}{b}$, we must have $\displaystyle 1 = \frac{x^2}{a^2} + \frac{y^2}{b^2} \ge 2\frac{xy}{ab}$.

    Now remember to maximize the area, it is the same to maximize $4xy$. We know from above that $\displaystyle 2 \frac{xy}{ab}$ is bounded above by $1$ (and it is achievable, when $\displaystyle \frac{x}{a} = \frac{y}{b}$), thus $4xy$ is bounded above by $2ab$ and it is achieved when $\displaystyle \frac{x}{a} = \frac{y}{b}$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Example 4""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""What is the minimum vertical distance between the parabolas $y = x^2 + 1$ and $y = x - x^2$?"""
    )
    return


@app.cell
def _(mo, np):
    x_slider_1 = mo.ui.slider(
        steps=np.linspace(-1, 1, 10001),
        label="x Coordinate of the point",
        value=0,
    )
    x_slider_1
    return (x_slider_1,)


@app.cell
def _(mo):
    mo.md(r"""**Try it youself using the above slidebar!**""")
    return


@app.cell
def _(go, np, x_slider_1):
    # Define functions
    f_dist = lambda x: x**2 + 1
    g_dist = lambda x: x - x**2

    # Domain
    x_vals_d = np.linspace(-1.5, 1.5, 400)
    y_f_vals = f_dist(x_vals_d)
    y_g_vals = g_dist(x_vals_d)

    # Given x value from slider
    x_point = x_slider_1.value  # <-- use your actual slider
    y_top = f_dist(x_point)
    y_bot = g_dist(x_point)
    delta_y = y_top - y_bot

    # Create figure
    fig_dist = go.Figure()

    # Plot both curves
    fig_dist.add_trace(
        go.Scatter(
            x=x_vals_d,
            y=y_f_vals,
            mode="lines",
            name="f(x) = x² + 1",
            line=dict(color="blue"),
        )
    )
    fig_dist.add_trace(
        go.Scatter(
            x=x_vals_d,
            y=y_g_vals,
            mode="lines",
            name="g(x) = x - x²",
            line=dict(color="green"),
        )
    )

    # Vertical segment from g(x) to f(x)
    fig_dist.add_trace(
        go.Scatter(
            x=[x_point, x_point],
            y=[y_bot, y_top],
            mode="lines+text",
            line=dict(color="red", width=3, dash="dash"),
            text=[f"{delta_y:.2f}"],
            textposition="bottom right",
            textfont=dict(size=14, color="red"),
            name="Vertical Distance",
            showlegend=False,
        )
    )

    # Layout
    fig_dist.update_layout(
        title="Vertical Distance Between f(x) and g(x) at x = {:.2f}".format(x_point),
        xaxis_title="x",
        yaxis_title="y",
        template="plotly_white",
        xaxis=dict(range=[-2, 2]),
        yaxis=dict(range=[-4, 4]),
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Solution Sketch:

    Vertical distance is simply calculated by subtracting the smaller $y$-coordinate from the other one. After figuring out that $y = x^2 + 1$ is always on top, the distance is then $d = (x^2 + 1) - (x - x^2)$ which is $d = 2x^2 - x + 1$. Proceed to find critical point(s) and find (absolute) minimum(s).
    """
    )
    return


if __name__ == "__main__":
    app.run()
