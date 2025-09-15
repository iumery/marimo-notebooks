import marimo

__generated_with = "0.15.4"
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
    mo.md(r"""# 4.4 Fundamental Theorem of Calculus""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Fundamental Theorem of Calculus""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""If $f$ is integrable on $[a, b]$, we can define a function $g$ by $\displaystyle g(x) = \int\limits_a^x f(t)dt$, $x \in [a, b]$. Then $g$ is continuous on $[a,b]$, is differentiable on $(a, b)$, and $g'(x) = f(x)$. In other words: $$\frac{d}{dx} \int_a^x f(t) dt = f(x).$$"""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Remark""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""Remember to use a different variable in $f$ and after $d$ (in the statement we use $t$) to differ from the variable in the upper limit."""
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    /// admonition | Integral and Derivative
        type: info

    In some sense, the theorem just says if you take (definite) integral and then take derivative, you get the original function back.

    ///
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Example""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    The Theorem at first glance may be confusing. Let us see an example to see if it really works.

    First, let us imagine we have a plane. Instead of having the usual $xy$-coordinate, we now use $ty$-coordinate. It is the exact same thing, just a name-change (i.e. the horizontal axis is now called the $t$-axis).

    What is the area of the region bounded by the following curves/lines?

    1. The $t$-axis;
    2. $y(t) = 2t + 1$;
    3. $t = 1$;
    4. $t = x$, where $x$ is a number that is greater than $1$, but we don't know the value.
    """
    )
    return


@app.cell
def _(go, np):
    # x range for main line
    x_line = np.linspace(0, 4, 400)
    y_line = 2 * x_line + 1

    # Vertical lines at x = 1 and x = 3
    x1 = np.full(100, 1)
    x3 = np.full(100, 3)
    y_vert = np.linspace(0, 8, 100)

    # Horizontal segment y = 3 on x in [1, 3]
    x_horiz = np.linspace(1, 3, 200)
    y_horiz = np.full_like(x_horiz, 3)

    # Create figure
    fig_1 = go.Figure()

    # Line y = 2x + 1
    fig_1.add_trace(go.Scatter(x=x_line, y=y_line, mode="lines", name="y = 2x + 1", line=dict(color="blue")))

    # Vertical lines
    fig_1.add_trace(
        go.Scatter(
            x=x1,
            y=y_vert,
            mode="lines",
            name="x = 1",
            line=dict(color="red", dash="dot"),
        )
    )
    fig_1.add_trace(
        go.Scatter(
            x=x3,
            y=y_vert,
            mode="lines",
            name="x = 3",
            line=dict(color="red", dash="dot"),
        )
    )

    # Horizontal line y = 3 from x = 1 to x = 3
    fig_1.add_trace(
        go.Scatter(
            x=x_horiz,
            y=y_horiz,
            mode="lines",
            name="y = 3",
            line=dict(color="green", dash="dash"),
        )
    )

    # Points with labels
    points_1 = [
        (1, 3, "(1, 3)"),
        (1, 0, "(1, 0)"),
        (3, 3, "(x, 3)"),
        (3, 0, "(x, 0)"),
        (3, 7, "(x, 2x+1)"),
    ]

    for x_pt_1, y_pt_1, label_1 in points_1:
        fig_1.add_trace(
            go.Scatter(
                x=[x_pt_1],
                y=[y_pt_1],
                mode="markers+text",
                marker=dict(size=8, color="black"),
                text=[label_1],
                textposition="top right",
                showlegend=False,
            )
        )

    # Layout
    fig_1.update_layout(
        title="Integrating y = 2x + 1",
        xaxis_title="x",
        yaxis_title="y",
        xaxis=dict(range=[0, 4], scaleanchor="y"),
        yaxis=dict(range=[-1, 8]),
        template="plotly_white",
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    We can do it with simple geometry. The region consists of two parts, a rectangle and a triangle. The rectangle has area $(x-1) \cdot 3 = 3x-3$, and the triangle has area $\displaystyle \frac{1}{2} \cdot (x-1) \cdot (2x+1 - 3)$ $= x^2 - 2x + 1$. The summation is $x^2 + x - 2$.

    This area depends on $x$, thus let us call it $A(x)$. Notice by definition of definite integral, $\displaystyle A(x) = \int_1^x 2t+1 dt$. What is the derivative of $A(x)$ with respect to $x$? We can calculate $(x^2+ x - 2)' = 2x+1$. And it should look familiar - replace $x$ by $t$ we get $2t+1$ which is exactly our original $y(t)$.
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
    Find $\displaystyle \frac{d}{dx} \int_1^x \sqrt{1 + t^3}dt$.

    By FTC, we know that if we write $\displaystyle g(x) = \int_1^x \sqrt{1 + t^3}dt$, then $g'(x) = f(x) = \sqrt{1 + x^3}$. But that is exactly what we want, i.e. $\displaystyle \frac{d}{dx} \int_1^x \sqrt{1 + t^3}dt = g'(x)$ (it's just two ways of writing the notation for derivative) $= \sqrt{1 + x^3}$.
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
    Find $\displaystyle \frac{d}{dx} \int_x^{5} \tan(\theta)d\theta$.

    Notice the upper/lower limits are not what they look like as in the theorem, so we should be careful about it.

    Write $\displaystyle g(x) = \int_x^5 \tan(\theta)d\theta$, then $\displaystyle -g(x) = \int_5^x \tan(\theta)d\theta$ by a property of definite integral. Then $\displaystyle (-g(x))' = \frac{d}{dx}\int_5^x \tan(\theta)d\theta = \tan(x)$ by FTC. Now $(-g(x))' = -g'(x)$, and what we want is $g'(x)$, thus $g'(x) = - \tan(x)$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Example 3""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Find $\displaystyle \frac{d}{dx} \int_2^{1/x^2} (2 + \sin(t)) dt$.

    Notice the upper limit are not what it looks like as in the theorem, it is a function of $x$, not just $x$. **The FTC does not work directly in this case**.

    We need to use the Chain Rule on top of FTC.

    Let us for now write $\displaystyle \frac{1}{x^2} = y$, then if we write $\displaystyle g(y) = \int_2^{y} (2 + \sin(t)) dt$, we know from the FTC that $\displaystyle \frac{d}{dy} g(y) = \frac{d}{dy} \int_2^{y} (2 + \sin(t)) dt = 2 + \sin(y)$. What we need is $\displaystyle \frac{d}{dx} g(y)$.

    Notice $\displaystyle \frac{dg(y)}{dy} \frac{dy}{dx} = \frac{dg(y)}{dx}$, and we can calculate $\displaystyle \frac{dy}{dx} = (\frac{1}{x^2})' = -\frac{2}{x^3}$. Thus $\displaystyle \frac{dg(y)}{dx}$ $\displaystyle = (2 + \sin(y))(-\frac{2}{x^3})$ $\displaystyle = -(2+\sin(\frac{1}{x^2}))\frac{2}{x^3}$ is what we need.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Theorem""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""In general, $$\boxed{\frac{d}{dx} \int_a^{g(x)} f(t) dt = f(g(x))\cdot g'(x)}$$ and $$\boxed{\frac{d}{dx} \int_{g(x)}^a f(t) dt = -f(g(x))\cdot g'(x)}$$ as we worked out above."""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Example (Graph Problem)""")
    return


@app.cell
def _(go, np):
    fig_2 = go.Figure()

    # 1. Line from (-4, 1) to (-2, 3)
    x21, y21 = [-4, -2], [1, 3]
    fig_2.add_trace(go.Scatter(x=x21, y=y21, mode="lines", name="Segment 1", line=dict(color="blue")))

    # 2. Line from (-2, 3) to (-1, 0)
    x22, y22 = [-2, -1], [3, 0]
    fig_2.add_trace(go.Scatter(x=x22, y=y22, mode="lines", name="Segment 2", line=dict(color="blue")))

    # 3. Lower half of unit circle: x in [-1, 1], y = -sqrt(1 - x^2)
    x_circle = np.linspace(-1, 1, 400)
    y_circle = -np.sqrt(1 - x_circle**2)
    fig_2.add_trace(
        go.Scatter(
            x=x_circle,
            y=y_circle,
            mode="lines",
            name="Lower Unit Circle",
            line=dict(color="blue"),
        )
    )

    # 4. Line from (1, 0) to (3, -1)
    x24, y24 = [1, 3], [0, -1]
    fig_2.add_trace(go.Scatter(x=x24, y=y24, mode="lines", name="Segment 3", line=dict(color="blue")))

    # Points with labels
    points_2 = [
        (-4, 1, "(-4, 1)"),
        (-2, 3, "(-2, 3)"),
        (-1, 0, "(-1, 0)"),
        (1, 0, "(1, 0)"),
        (3, -1, "(3, -1)"),
    ]

    for x_pt_2, y_pt_2, label_2 in points_2:
        fig_2.add_trace(
            go.Scatter(
                x=[x_pt_2],
                y=[y_pt_2],
                mode="markers+text",
                marker=dict(size=8, color="black"),
                text=[label_2],
                textposition="top right",
                showlegend=False,
            )
        )

    # Layout settings
    fig_2.update_layout(
        title="Graph of f",
        xaxis_title="x",
        yaxis_title="y",
        xaxis=dict(range=[-5, 4], scaleanchor="y"),
        yaxis=dict(scaleanchor="x"),
        template="plotly_white",
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Let $f$ be the continuous function defined on $[-4,3]$ whose graph consisting of three line segments and a semicircle centered at origin is given above. Define $\displaystyle g(x) = \int\limits_1^xf(t)dt$.

    1. Evaluate $g(2)$ and $g(-2)$;
    2. Evaluate $g'(-3)$ and $g''(-3)$;
    3. Find the $x$-oordinate(s) of all point(s) at which the graph of $g$ has a horizontal tangent line. For each of these points, determine if it is a local maximum, local minimum, or neither;
    4. Find the $x$-coordinate(s) of all inflection point(s) of $g$.

    Solution:

    1. By construction, $\displaystyle g(2) = \int\limits_1^2f(t)dt$, from the graph we see this is the **signed** area of a triangle. The length of the triangle is $1$ and the height is $\displaystyle \frac{1}{2}$; the triangle is below $x$-axis thus should have negative area, thus the answer is $\displaystyle -\frac{1}{2}\cdot 1 \cdot \frac{1}{2} = -\frac{1}{4}$.
        $\displaystyle g(-2) = \int\limits_1^{-2}f(t)dt$, notice that $-2$ is smaller than $1$, thus we should write it as $\displaystyle g(-2) = -\int\limits_{-2}^1f(t)dt$ and the integral is the **signed** area of a triangle and a half-disk. The area of the triangle is $\displaystyle \frac{1}{2}\cdot 1 \cdot 3 = \frac{3}{2}$; the area of the half-disk is $\displaystyle -\frac{1}{2}\cdot \pi\cdot 1^2 = -\frac{\pi}{2}$ (it is negative because it is below $x$-axis). Do not forget the minus sign from inverting $1$ and $-2$, the final answer if $\displaystyle -(\frac{3}{2} - \frac{\pi}{2})$ or $\displaystyle \frac{\pi}{2} - \frac{3}{2}$;
    2. By FTC, $g'(x) = f(x)$ thus $g'(-3) = f(-3)$, so we can observe from the graph that $g'(-3)$ equals $2$.
        Since $g'(x) = f(x)$, we should have $g''(x) = f'(x)$, thus $g''(-3) = f'(-3)$, which means it equals the slope of tangent line of $f$ at $-3$, we can observe from the graph that the slope is $1$, thus $g''(-3) = 1$;
    3. $g$ has a horizontal tangent line at $x$ if $g'(x)$ is defined and equals $0$, from part 2 we know $g'(x) = f(x)$, and we can observe from the graph that $f(x) = 0$ when $x = -1$ or $1$.
        At $-1$, $g'(x) = f(x)$ changes from positive to negative (before $-1$, the graph of $f$ is above $x$-axis, but after $-1$, the graph of $f$ is below $x$-axis), thus by First Derivative Test, $-1$ is a local maximum.
        At $1$, $g'(x)$ remains from negative to negative, thus it is not a local extremum;
    4. Recall that inflection point is when $g''(x)$ changes sign, which is equivalent with that $f'(x)$ changes sign. Observe from the graph, we can find the inflection points are $-2$ (positive to negative, because $f$ is increasing before $-2$ and decreasing after $-2$, meaning that $f'$ is positive before $-2$ and negative after $-2$), $0$ (negative to positive), and $1$ (positive to negative).
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Remark""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    In particular, with such setup (given graph of $f$, and define $\displaystyle g(x) = \int_a^xf(t)dt$),

    1. $g(b)$ evaluate the area of the region from $a$ to $b$ on the graph;
    2. $g'(b)$ is simply the $y$-value at $b$ on the graph, and;
    3. $g''(b)$ is the slope of the graph at $b$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Average Value of a Function""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Let $f$ be integrable on $[a, b]$, intuitively, if we choose $n$ points on the curve $f(x)$, then their average should be $\displaystyle \frac{f(x_1) + f(x_2) + \dots + f(x_n)}{n}$.

    The average value (of all points) of a function on $[a, b]$ can then be thought as the limit of the above expression as $n$ goes to infinity.

    Now, recall our definition of definite integral, we have
    $$
    \int_a^bf(x)dx = \lim_{n \to \infty}\sum_{i = 1}^nf(x_i)\Delta(x)
    $$
    which is the same as
    $$
    \int_a^bf(x)dx = \lim_{n \to \infty}\frac{\left(f(x_1)+ f(x_2) + \dots + f(x_n)\right)\cdot(b-a)}{n}
    $$
    So if we divide $b-a$ both sides, the left hand side becomes $\displaystyle \frac{1}{b-a}\int_a^bf(x)dx$, and the right hand side is $\displaystyle \lim\limits_{n \to \infty}\frac{f(x_1) + f(x_2) + \dots + f(x_n)}{n}$ which is the average.

    Thus we have the following definition: let $f$ be integrable on $[a, b]$, the average value of $f$ on $[a,b]$ (there is no 'right' notation for this, we can write $f_{\text{average}}$) is $\displaystyle f_{\text{average}} = \frac{1}{b-a}\int_a^b f(x) dx$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Example""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    What is the average value of $x - x^2$ on $[0,2]$?

    By definition, the average value $\displaystyle = \frac{1}{2 - 0} \int_0^2 x - x^2 dx$ $\displaystyle = \frac{1}{2}\left( (\frac{x^2}{2} - \frac{x^3}{3}) |_0^2 \right)$ $\displaystyle = \frac{1}{2} (\frac{4}{2} - \frac{8}{3})$ $\displaystyle = - \frac{1}{3}$.
    """
    )
    return


if __name__ == "__main__":
    app.run()
