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
    mo.md(r"""# 7.1 Area between Curves""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Introduction

    In chapter 4 we learnt about how to calculate the signed area of region under **a** curve. To be more specific, we calculate the signed area of region bounded by:

    1. Some function $f(x)$, it gives us the upper boundary;
    2. The $x$-axis, it gives us the lower boundary;
    3. Two vertical lines $x = a$ and $x = b$, they give us the left and right boundaries.

    In this chapter we generalize the above settings.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Generalization 1""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""We usually think of $y = f(x)$ being a function of $x$- but there is no reason that this must be the case - we can also take $x = g(y)$ to be a function of $y$:"""
    )
    return


@app.cell
def _(go, np):
    # y values
    y_vals_parab = np.linspace(-3, 3, 400)
    x_vals_parab = y_vals_parab**2 + 2

    # Create plot
    fig_parab = go.Figure()

    # Plot x = y^2 + 2
    fig_parab.add_trace(
        go.Scatter(
            x=x_vals_parab,
            y=y_vals_parab,
            mode="lines",
            name=r"$x = y^2 + 2$",
            line=dict(color="blue"),
        )
    )

    # Layout
    fig_parab.update_layout(
        title="Function of y",
        xaxis_title="x",
        yaxis_title="y",
        template="plotly_white",
        xaxis=dict(range=[0, 12]),
        yaxis=dict(range=[-4, 4]),
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""Notice though that when we talk about a function, each input corresponds to exact **one** output, so the following graph cannot be the graph of a function of $y$ (because $y = 0$ corresponds to more than one $x$ values), you can only view it as a function of $x$:"""
    )
    return


@app.cell
def _(go, np):
    # Function
    f = lambda x: x**3 - 3 * x**2 + 2
    x_vals = np.linspace(-1, 4, 400)
    y_vals = f(x_vals)

    # Create figure
    fig_func = go.Figure()

    # Plot f(x)
    fig_func.add_trace(
        go.Scatter(
            x=x_vals,
            y=y_vals,
            mode="lines",
            name="f(x) = x³ - 3x² + 2",
            line=dict(color="blue"),
        )
    )

    # Plot horizontal line y = 0
    fig_func.add_trace(
        go.Scatter(
            x=[-1, 4],
            y=[0, 0],
            mode="lines",
            name="y = 0",
            line=dict(color="red", dash="dash"),
        )
    )

    # Layout
    fig_func.update_layout(
        title="Function Fails Horizontal Line Test",
        xaxis_title="x",
        yaxis_title="y",
        template="plotly_white",
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    If we have a function $x = g(y)$, then it makes sense to calculate the signed area of region 'under' curve as well. To be more specific, we calculate the signed area of region bounded by:

    1. Some function $g(y)$;
    2. The $y$-axis;
    3. Two horizontal lines $y = a$ and $y = b$.
    """
    )
    return


@app.cell
def _(go, np):
    # y-range for region
    y_fill = np.linspace(-2, 2, 400)
    x_parab = y_fill**2 + 2
    x_axis = np.zeros_like(y_fill)

    # Create figure
    fig_shaded = go.Figure()

    # Filled region between x = y^2 + 2 and x = 0
    fig_shaded.add_trace(
        go.Scatter(
            x=np.concatenate([x_axis, x_parab[::-1]]),
            y=np.concatenate([y_fill, y_fill[::-1]]),
            fill="toself",
            fillcolor="rgba(255, 165, 0, 0.4)",
            line=dict(color="orange"),
            name="Shaded Region",
        )
    )

    # Parabola: x = y^2 + 2
    fig_shaded.add_trace(
        go.Scatter(
            x=x_parab,
            y=y_fill,
            mode="lines",
            name=r"$x = y^2 + 2$",
            line=dict(color="blue"),
        )
    )

    # y-axis (x = 0)
    fig_shaded.add_trace(
        go.Scatter(
            x=[0, 0],
            y=[-2.5, 2.5],
            mode="lines",
            name="y-axis",
            line=dict(color="black", dash="dot"),
        )
    )

    # y = -2 and y = 2
    fig_shaded.add_trace(
        go.Scatter(
            x=[0, 10],
            y=[-2, -2],
            mode="lines",
            name="y = -2",
            line=dict(color="gray", dash="dot"),
        )
    )
    fig_shaded.add_trace(
        go.Scatter(
            x=[0, 10],
            y=[2, 2],
            mode="lines",
            name="y = 2",
            line=dict(color="gray", dash="dot"),
        )
    )

    # Layout
    fig_shaded.update_layout(
        title="Region Bounded by Function of y",
        xaxis_title="x",
        yaxis_title="y",
        xaxis=dict(range=[-1, 10], scaleanchor="y"),
        yaxis=dict(range=[-2.5, 2.5]),
        template="plotly_white",
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""How to evaluate the value of the area? There is nothing new. Recall that the signed area under curve $f(x)$ on $x \in [a, b]$ is given by $\displaystyle \int\limits_a^bf(x)dx$, so similarly, the signed area 'under' curve $g(y)$ on $y \in [a, b]$ is given by $\displaystyle \int\limits_a^b g(y)dy$."""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Generalization 2""")
    return


@app.cell
def _(go, np):
    # Domain
    x = np.linspace(0, 2, 400)
    fb = np.sin(x) + 2
    gb = (1 / 3) * x + 1

    # Create figure
    fig = go.Figure()

    # --- Curves ---
    fig.add_trace(
        go.Scatter(
            x=x, y=fb, mode="lines", name="f(x) = sin(x) + 2", line=dict(color="red")
        )
    )

    fig.add_trace(
        go.Scatter(
            x=x, y=gb, mode="lines", name="g(x) = 1/3 x + 1", line=dict(color="green")
        )
    )

    # --- Fill: area under g (Region B) ---
    fig.add_trace(
        go.Scatter(
            x=np.concatenate([x, x[::-1]]),
            y=np.concatenate([gb, np.zeros_like(x)]),
            fill="toself",
            line=dict(width=0),
            fillcolor="rgba(0, 200, 0, 0.3)",
            name="Region B",
            showlegend=False,
        )
    )

    # --- Fill: area between f and g (Region A) ---
    fig.add_trace(
        go.Scatter(
            x=np.concatenate([x, x[::-1]]),
            y=np.concatenate([fb, gb[::-1]]),
            fill="toself",
            line=dict(width=0),
            fillcolor="rgba(255, 0, 0, 0.3)",
            name="Region A",
            showlegend=False,
        )
    )

    # --- Labels A and B ---
    fig.add_trace(
        go.Scatter(
            x=[1],
            y=[2.1],
            mode="text",
            text=["A"],
            textfont=dict(size=18, color="darkred"),
            showlegend=False,
        )
    )

    fig.add_trace(
        go.Scatter(
            x=[1],
            y=[0.6],
            mode="text",
            text=["B"],
            textfont=dict(size=18, color="darkgreen"),
            showlegend=False,
        )
    )

    # Layout
    fig.update_layout(
        title="Shaded Regions: A (between f and g), B (under g)",
        xaxis_title="x",
        yaxis_title="y",
        xaxis=dict(range=[-0.5, 2.5]),
        yaxis=dict(range=[0, 4]),
        template="plotly_white",
    )
    return


app._unparsable_cell(
    r"""
    Consider the above diagram. It is not hard to tell that the signed area of region under the red curve is $A + B$, the signed area of region under the green curve is $B$.

    In this case, **we say the signed area of region between the red curve and the green curve is $A$**, which is the (area under the red curve) minus (area under the green curve).

    In particular, say the red curve is given by $f$ and green curve is given by $g$, then the area under the red curve is $\displaystyle \int\limits_a^bf(x)dx$, area under the green curve is $\displaystyle \int\limits_a^bg(x)dx$, thus the area between the red and green curves is $\displaystyle \int\limits_a^bf(x)dx - \int\limits_a^bg(x)dx$, using the property of integral, we have: $$\boxed{\text{signed area between }f\text{ and }g = \int\limits_a^b f(x) - g(x) dx}.$$
    """,
    name="_",
)


@app.cell
def _(mo):
    mo.md(r"""## Signed Area Vs. Area""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Recall that when we learnt about the motion problem, there were two questions: displacement and distance traveled. Displacement is visualized as the signed area under the velocity curve, while the distance traveled can be visualized as the area under the velocity curve.

    Similarly, consider the following diagram:
    """
    )
    return


@app.cell
def _(go, np):
    # Domain and functions
    x2 = np.linspace(0, 6, 400)
    fb2 = np.sin(x2) + 2
    gb2 = (1 / 3) * x2 + 1

    # Create figure
    fig_2 = go.Figure()

    # --- Curves ---
    fig_2.add_trace(
        go.Scatter(
            x=x2, y=fb2, mode="lines", name="f(x) = sin(x) + 2", line=dict(color="red")
        )
    )

    fig_2.add_trace(
        go.Scatter(
            x=x2, y=gb2, mode="lines", name="g(x) = 1/3 x + 1", line=dict(color="green")
        )
    )

    # --- Conditional fill between curves ---
    above = fb2 > gb2
    regions = []
    current_region = []
    for i in range(len(x2)):
        if i == 0 or above[i] == above[i - 1]:
            current_region.append(i)
        else:
            regions.append((above[i - 1], current_region.copy()))
            current_region = [i]
    regions.append((above[-1], current_region))

    # Shade regions
    for is_above, idx_group in regions:
        x_region = x2[idx_group]
        y_upper = fb2[idx_group] if is_above else gb2[idx_group]
        y_lower = gb2[idx_group] if is_above else fb2[idx_group]
        color = "rgba(255, 0, 0, 0.3)" if is_above else "rgba(0, 200, 0, 0.3)"
        fig_2.add_trace(
            go.Scatter(
                x=np.concatenate([x_region, x_region[::-1]]),
                y=np.concatenate([y_upper, y_lower[::-1]]),
                fill="toself",
                line=dict(width=0),
                fillcolor=color,
                showlegend=False,
            )
        )

    # --- Optional labels ---
    fig_2.add_trace(
        go.Scatter(
            x=[1.5],
            y=[2],
            mode="text",
            text=["A: f > g"],
            textfont=dict(size=16, color="darkred"),
            showlegend=False,
        )
    )
    fig_2.add_trace(
        go.Scatter(
            x=[5],
            y=[2],
            mode="text",
            text=["B: g > f"],
            textfont=dict(size=16, color="darkgreen"),
            showlegend=False,
        )
    )

    # --- Layout ---
    fig_2.update_layout(
        title="Region between Two Curves that Crosses Each Other",
        xaxis_title="x",
        yaxis_title="y",
        xaxis=dict(range=[-0.5, 6.5]),
        yaxis=dict(range=[0, 4]),
        template="plotly_white",
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    The region between the red curve and green curve is of course the region A and region B. However, on region A, the red curve ($f$) is on top of the green curve ($g$), but on region B, the red curve is below the green curve. If we directly calculate $\displaystyle \int\limits_a^b f(x) - g(x) dx$, then we are calculating 'area of region A minus area of region B', instead of 'area of region A plus area of region B'. The first one is the signed area between the two curves, and the second one is the (unsigned) area between the two curves.

    If you get a question of this type, you should always check if the question is asking for signed area or just area (which means unsigned area). In exams of this course, most likely you will always be asked for area instead of signed area.

    Like the motion problem, to calculate the area, we need to figure out on which region $f$ is on top, and on which region $g$ is on top. In general: $$\boxed{\text{area between }f\text{ and }g = \int\limits_a^b | f(x) - g(x) | dx}.$$
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Generalization 1 and 2""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""Put the two generalization together, we can get: $$\boxed{\text{area between }f\text{ and }g\text{ that depend on }y = \int\limits_a^b | f(y) - g(y) | dy}.$$"""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Example""")
    return


@app.cell
def _(go, np):
    # New variable names
    x_vals_m = np.linspace(0, np.pi, 400)
    y_sin_m = np.sin(x_vals_m)
    y_line_m = (2 / np.pi) * x_vals_m

    # Create figure
    fig_m = go.Figure()

    # Plot y = sin(x)
    fig_m.add_trace(
        go.Scatter(
            x=x_vals_m,
            y=y_sin_m,
            mode="lines",
            name="f(x) = sin(x)",
            line=dict(color="blue"),
        )
    )

    # Plot y = (2/π) x
    fig_m.add_trace(
        go.Scatter(
            x=x_vals_m,
            y=y_line_m,
            mode="lines",
            name="g(x) = (2/π)x",
            line=dict(color="green"),
        )
    )

    # Shaded region between curves
    fig_m.add_trace(
        go.Scatter(
            x=np.concatenate([x_vals_m, x_vals_m[::-1]]),
            y=np.concatenate([y_sin_m, y_line_m[::-1]]),
            fill="toself",
            fillcolor="rgba(255, 0, 0, 0.3)",
            line=dict(width=0),
            name="Region between f and g",
            showlegend=False,
        )
    )

    # Layout
    fig_m.update_layout(
        title=r"Region Bounded by Two Curves",
        xaxis_title="x",
        yaxis_title="y",
        template="plotly_white",
        xaxis=dict(range=[0, np.pi]),
        yaxis=dict(range=[0, 2.2]),
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    What is the signed area between $y = \sin(x)$ and $\displaystyle y = \frac{2}{\pi}x$ on $[0, \pi]$?

    The area can be evaluated as $\displaystyle \int\limits_0^{\pi} \sin(x) - \frac{2}{\pi}x dx$. There is nothing special about this integral, we just evaluate it as usual, the answer is $2 - \pi$.

    What is the area between the above two curves?

    The area can be evaluated as $\displaystyle \int\limits_0^{\pi} | \sin(x) - \frac{2}{\pi}x | dx$. To proceed, we need to figure out when is $\sin(x)$ greater than $\displaystyle \frac{2}{\pi}x$ and when is the other way around.

    Plot the two curve, and notice that they intersect at $x = 0$ and $\displaystyle x = \frac{\pi}{2}$. On $\displaystyle [0, \frac{\pi}{2}]$, $\sin(x)$ is larger, and on $\displaystyle [\frac{\pi}{2}, \pi]$, $\displaystyle \frac{2}{\pi}x$ is larger.

    Thus the (unsigned) area between the two curves is given by $\displaystyle \int\limits_0^{\pi} | \sin(x) - \frac{2}{\pi}x | dx$ $\displaystyle = \int\limits_0^{\pi/2} \sin(x) - \frac{2}{\pi}x dx + \int\limits_{\pi/2}^{\pi} \frac{2}{\pi}x - \sin(x) dx$. Evaluate it, the answer should be $\displaystyle \frac{\pi}{2}$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Special Kind of Question: Area Enclosed by Two Curves""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Suppose we have two continuous curves $f(x)$ and $g(x)$ and they **intersect exactly twice**. Say they intersect at $x = a$ and $x = b$. In particular, **either we have $f(x) \ge g(x)$ on entire $[a,b]$, or $g(x) \ge f(x)$ on entire $[a, b]$**.

    Up to interchange their names, let us assume $f(x) \ge g(x)$ on entire $[a, b]$.

    Then the area enclosed by two curves is given by: $$\boxed{\text{area enclosed by }f\text{ and }g = \int\limits_a^b f(x) - g(x) dx}.$$ Similarly, if the two curves are functions of $y$, then $$\boxed{\text{area enclosed by }f\text{ and }g = \int\limits_a^b f(y) - g(y) dy}.$$ Why is this question special? In the description of this kind of question, $a$ and $b$ **will not be given**, which function is on top **will also not be given**.
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
    Find the area of the region enclosed by the curves $\displaystyle f(y) = \frac{1}{9}y^3$ and $g(y) = y^2$.

    First we need to find where do the two curves intersect. We solve $\displaystyle \frac{1}{9}y^3 = y^2$. We can either have $y = 0$ or we can cancel $y^2$ each side and get $\displaystyle \frac{1}{9}y = 1$ or $y = 9$.

    On the region $[0,9]$, pick any number in between, say $y = 1$, then $\displaystyle f(1) = \frac{1}{9}$ and $g(1) = 1$, so $g \ge f$ on $[0, 9]$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    /// admonition | f - g or g - f?
        type: info

    Remember that we either have $f \ge g$ on **entire** $[0,9]$ or $g \ge f$, so as long as there is one value that $g > f$, we can safely say $g \ge f$. Do not plugin the endpoints because apparently you will have $g(0) = f(0)$ and $g(9) = f(9)$ which does not tell you which one is greater.

    Another way to solve the problem is to **forget about this comparison**: since we are evaluating **area**, the answer **has to be positive**, thus you can use whichever of $g - f$ or $f-g$, and take absolute value if you get a negative number.

    Thus the area of region enclosed by the two curves is $\displaystyle \int\limits_0^9 g(y) - f(y) dy$ $\displaystyle = \int\limits_0^9 y^2 - \frac{1}{9}y^3 dy$. Evaluate this integral as usual, the answer should be $\displaystyle \frac{243}{4}$.

    For example, you can also calculate $\displaystyle \int\limits_0^9 f(y) - g(y) dy$, and you will get $\displaystyle -\frac{243}{4}$, a negative number. Now you can just take absolute value and the final answer is $\displaystyle \frac{243}{4}$.

    (**However, if the question specifically ask you not to use absolute value, then use the first method!**)
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
    Sometimes the question is even harder and you also need to figure out if we should view the functions to depend on $x$ or $y$.

    Find the area of the region enclosed by $4x + y^2 = 12$ and $x = y$.

    To proceed, it is good to first plot the graph:
    """
    )
    return


@app.cell
def _(go, np):
    # y range where the curves intersect: solve 4y + y^2 = 12 ⇒ y^2 + 4y - 12 = 0
    y_vals_r = np.linspace(-6, 2, 400)
    x_parab_r = (12 - y_vals_r**2) / 4
    x_line_r = y_vals_r

    # Create figure
    fig_r = go.Figure()

    # Plot x = (12 - y^2)/4
    fig_r.add_trace(
        go.Scatter(
            x=x_parab_r,
            y=y_vals_r,
            mode="lines",
            name=r"$4x + y^2 = 12$",
            line=dict(color="blue"),
        )
    )

    # Plot x = y
    fig_r.add_trace(
        go.Scatter(
            x=x_line_r,
            y=y_vals_r,
            mode="lines",
            name=r"$x = y$",
            line=dict(color="green"),
        )
    )

    # Fill between the curves
    fig_r.add_trace(
        go.Scatter(
            x=np.concatenate([x_parab_r, x_line_r[::-1]]),
            y=np.concatenate([y_vals_r, y_vals_r[::-1]]),
            fill="toself",
            fillcolor="rgba(255, 0, 0, 0.3)",
            line=dict(width=0),
            name="Shaded Region",
            showlegend=False,
        )
    )

    # Layout
    fig_r.update_layout(
        title=r"Region Enclosed by Two Curves",
        xaxis_title="x",
        yaxis_title="y",
        template="plotly_white",
        xaxis=dict(scaleanchor="y", range=[-6, 4]),
        yaxis=dict(range=[-7, 3]),
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    The region enclosed is then easier to be evaluated if we view the functions to depend on $y$ (why? because the red curve, $4x + y^2 = 12$ is not a function of $x$). We also need to calculate the intersections. First we rewrite the first curve as $\displaystyle x = 3 - \frac{1}{4}y^2$ (because we want to view it as a function of $y$), and solve $\displaystyle 3 - \frac{1}{4}y^2 = y$. This is a quadratic equation so should not be too hard to solve. The answer is $y = 2$ or $-6$.

    On the region, from the graph it is not hard to tell that the red curve is on the 'top' (right, because right direction is where $x$-xis is positive). Algebraically, it is because if we take $y = 0$, then $\displaystyle 3 - \frac{1}{4}\cdot 0 \ge 0$.

    Thus the area enclosed by the region is given by $\displaystyle \int\limits_{-6}^23 - \frac{1}{4}y^2 - y dy$. The answer is $\displaystyle \frac{64}{3}$.
    """
    )
    return


if __name__ == "__main__":
    app.run()
