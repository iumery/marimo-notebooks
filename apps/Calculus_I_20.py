import marimo

__generated_with = "0.13.6"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    return go, make_subplots, mo, np


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
    mo.md(r"""# 4.1 Areas""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Introduction""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    We learnt how to calculate area of some basic shapes in geometry course. For example, the area of a rectangle is width times length, the area of a disk is $\pi$ times radius squared, and so on.

    What if we want to know the area of an arbitrary shape (say it is described by a function)?

    One intuitive idea is to cover it by certain numbers of rectangles. The (sum of) areas of the rectangles give us an estimation of the area of the desired region.

    Let us try to estimate the area of a hemisphere with $4$ rectangles, we list $3$ different ways to do it here:
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Example 1 (Left Endpoint Method)""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    With this method, we divide the 'width' into $4$ equal parts - those are the width of the $4$ rectangles we are going to use. For the height, we take the (absolute value of) $y$-value that corresponds to the left endpoint of each sub-interval we just got.

    We should know the function $y = \sqrt{1-x^2}$ describes the upper hemisphere. The width we are going to divide is $2$ (the diameter), which is the length of the interval $[-1, 1]$. If we divide this interval to $4$ intervals, we get $[-1,-0.5], [-0.5,0],[0,0.5]$ and $[0.5,1]$- each has length $0.5 = 2/4$.

    So the left endpoints for these intervals are $-1, -0.5, 0$ and $0.5$. The $y$-values correspond to these points are $y(-1) = 0$, $y(0.5) = \sqrt{0.75} \approx 0.86$, $y(0) = 1$ and $y(-0.5) \approx 0.86$ again. These can be understood as the height of the rectangles.

    So we have the heights and width for each of the four rectangles, we estimate the area of the hemisphere to be their sum, which is $\approx 0.5\cdot 0 + 0.5 \cdot 0.86 + 0.5 \cdot 1 + 0.5 \cdot 0.86$ $= 0.5(0+0.86+1+0.86) = 1.36$.
    """
    )
    return


@app.cell
def _(go, np):
    # Upper unit circle: y = sqrt(1 - x^2)
    x_curve = np.linspace(-1, 1, 400)
    y_curve = np.sqrt(1 - x_curve**2)

    fig_1 = go.Figure()

    # Plot upper unit circle
    fig_1.add_trace(
        go.Scatter(
            x=x_curve,
            y=y_curve,
            mode="lines",
            name="Upper Unit Circle",
            line=dict(color="blue"),
        )
    )

    # Left-endpoint rectangles
    n_rects = 4
    x_left = np.linspace(-1, 1 - 2 / n_rects, n_rects)  # left x values
    dx = 2 / n_rects

    for x0 in x_left:
        height_left = np.sqrt(1 - x0**2)
        fig_1.add_shape(
            type="rect",
            x0=x0,
            x1=x0 + dx,
            y0=0,
            y1=height_left,
            fillcolor="rgba(255, 165, 0, 0.5)",  # semi-transparent orange
            line=dict(color="orange"),
        )

    # Layout
    fig_1.update_layout(
        title="Upper Unit Circle with 4 Left-Endpoint Rectangles",
        xaxis_title="x",
        yaxis_title="y",
        xaxis=dict(scaleanchor="y", range=[-1.2, 1.2]),
        yaxis=dict(scaleanchor="x", range=[-0.1, 1.2]),
        template="plotly_white",
        showlegend=True,
    )
    return dx, n_rects, x_curve, y_curve


@app.cell
def _(mo):
    mo.md(r"""### Example 2 (Right Endpoint Method)""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    The procedure of this method is the same as left endpoint method, with the only difference that we take $y$-values correspond to the right endpoint of the sub-intervals we get.

    In the hemisphere example, right and left endpoint methods yield the same answer. Check it.
    """
    )
    return


@app.cell
def _(dx, go, n_rects, np, x_curve, y_curve):
    fig_2 = go.Figure()

    # Plot upper unit circle
    fig_2.add_trace(
        go.Scatter(
            x=x_curve,
            y=y_curve,
            mode="lines",
            name="Upper Unit Circle",
            line=dict(color="blue"),
        )
    )

    # Right-endpoint rectangles
    x_right = np.linspace(-1 + dx, 1, n_rects)  # right x values

    for x1 in x_right:
        height_right = np.sqrt(1 - x1**2)
        fig_2.add_shape(
            type="rect",
            x0=x1 - dx,
            x1=x1,
            y0=0,
            y1=height_right,
            fillcolor="rgba(0, 200, 255, 0.4)",  # semi-transparent cyan
            line=dict(color="teal"),
        )

    # Layout
    fig_2.update_layout(
        title="Upper Unit Circle with 4 Right-Endpoint Rectangles",
        xaxis_title="x",
        yaxis_title="y",
        xaxis=dict(scaleanchor="y", range=[-1.2, 1.2]),
        yaxis=dict(scaleanchor="x", range=[-0.1, 1.2]),
        template="plotly_white",
        showlegend=True,
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Example 3 Midpoint Method""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    The procedure of this method is the same as left endpoint method, with the only difference that we take $y$-values correspond to the midpoint of the sub-intervals we get.

    In the hemisphere example, remember we have the sub-intervals $[-1,-0.5], [-0.5,0],[0,0.5]$ and $[0.5,1]$, so the midpoints are $-0.75, -0.25, 0.25$, and $0.75$. The corresponding $y$-values are $\approx 0.66, 0.97, 0.97, 0.66$, so the estimation of area with this method is $\approx 0.5(0.66+0.97+0.97+0.66) = 1.71$.
    """
    )
    return


@app.cell
def _(dx, go, n_rects, np, x_curve, y_curve):
    fig_3 = go.Figure()

    # Plot the upper unit circle
    fig_3.add_trace(
        go.Scatter(
            x=x_curve,
            y=y_curve,
            mode="lines",
            name="Upper Unit Circle",
            line=dict(color="blue"),
        )
    )

    # Midpoint rectangles
    x_mid = np.linspace(-1 + dx / 2, 1 - dx / 2, n_rects)  # midpoints

    for x_m in x_mid:
        height_mid = np.sqrt(1 - x_m**2)
        fig_3.add_shape(
            type="rect",
            x0=x_m - dx / 2,
            x1=x_m + dx / 2,
            y0=0,
            y1=height_mid,
            fillcolor="rgba(0, 255, 0, 0.4)",  # semi-transparent green
            line=dict(color="darkgreen"),
        )

    # Layout
    fig_3.update_layout(
        title="Upper Unit Circle with 4 Midpoint Rectangles",
        xaxis_title="x",
        yaxis_title="y",
        xaxis=dict(scaleanchor="y", range=[-1.2, 1.2]),
        yaxis=dict(scaleanchor="x", range=[-0.1, 1.2]),
        template="plotly_white",
        showlegend=True,
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Remark 1""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    If we calculate the exact area of a hemisphere, we get $\frac{1}{2}\pi \cdot 1^2 \approx 1.57$, which is closer to $1.71$ (the result we get from midpoint method).

    In general, **there is no reason that midpoint method will always give a better estimation**. It is also **not true** that left and right endpoint methods will give the same result (if the function is even, then left and right endpoint methods do give same result. Why?).
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Remark 2""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""In the above case, all the rectangles have *positive* height ($y$-values). But in general this may not be the case (for example, if we want to evaluate the 'area' under the sine curve). The area calculated in this way may be called a signed area. **If we want to calculate the area in the usual sense (unsigned area), we should use the absolute value of each $y$-value**."""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Introduction, Continued""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    It is very intuitive to see, that in general the more rectangles we use, the better estimation of the area we should get.

    This gives a natural idea to evaluate the area - what if we take **infinitely many rectangle and take the sum of their areas**? Since infinity, again, is not a number, we have to use the concept of limit.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Area Under Curve""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    The signed area (denoted by $A$) of the region that is bounded by $f(x)$, $x$-axis, $x = a$, and $x = b$ (with $b > a$), is given by the limit of $f(x_1)\Delta(x) + f(x_2) \Delta(x) + \dots + f(x_n)\Delta(x)$ as $n$ goes to infinity, where:

    1. We divide the interval $[a, b]$ into $n$ sub-intervals, and denote the endpoints to be $[x_0,x_1], [x_1,x_2], \dots, [x_{n-1},x_n]$;
    2. Each sub-interval has the same length, which is $\frac{b-a}{n}$, and we denote it by $\Delta(x)$.

    In other words, $\displaystyle A = \lim\limits_{n \to \infty}[f(x_1)\Delta(x) + f(x_2) \Delta(x) + \dots + f(x_n)\Delta(x)]$, or put it into a sigma notation, we have $$A = \lim\limits_{n \to \infty}\sum_{i = 1}^nf(x_i)\Delta(x).$$
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Remark 1""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    The above formula, with careful inspection, is using the right endpoint method (because the first interval is $[x_0,x_1]$ and we used $f(x_1)$ as the height).

    **It is provable, that the choice of point does not matter** (that is, you can use right endpoint, left endpoint, midpoint, or in fact, any point in each sub-interval). This depends on the fact that we are using infinitely many rectangles.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Remark 2""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    For now we are dividing $x$-axis into sub-intervals. Another intuitive method is to divide $y$-axis into sub-intervals.

    Roughly speaking, the summation involving dividing $x$-axis is called a Riemann sum, and the summation involving dividing $y$-axis is called a Lebesgue sum (there are other differences between them). Lebesgue sum has some (big) advantages over the Riemann sum. However, the discuss of Lebesgue sum is way beyond the scope of this course.
    """
    )
    return


@app.cell
def _(go, make_subplots, np):
    # Function: upper semicircle
    f_c = lambda x: np.sqrt(1 - x**2)
    x_curve_c = np.linspace(-1, 1, 400)
    y_curve_c = f_c(x_curve_c)

    # Create subplots
    fig_c = make_subplots(
        rows=1,
        cols=2,
        subplot_titles=("Riemann (x-subdivision)", "Lebesgue (y-subdivision)"),
    )

    # --- Left: Riemann integration (x-subdivision) ---
    n_rects_c = 6
    dx_c = 2 / n_rects_c
    x_left_c = np.linspace(-1, 1 - dx_c, n_rects_c)

    # Curve
    fig_c.add_trace(
        go.Scatter(
            x=x_curve_c, y=y_curve_c, mode="lines", name="f(x)", line=dict(color="blue")
        ),
        row=1,
        col=1,
    )

    # Riemann rectangles
    for x0_c in x_left_c:
        height_c = f_c(x0_c)
        fig_c.add_shape(
            type="rect",
            x0=x0_c,
            x1=x0_c + dx_c,
            y0=0,
            y1=height_c,
            fillcolor="rgba(0, 150, 255, 0.4)",
            line=dict(color="blue"),
            row=1,
            col=1,
        )

    # --- Right: Lebesgue integration (y-subdivision) ---
    n_bands_c = 6
    y_vals_c = np.linspace(0, 1, 400)
    dy_c = 1 / n_bands_c
    y_bands_c = np.linspace(0, 1 - dy_c, n_bands_c)

    # Curve
    fig_c.add_trace(
        go.Scatter(
            x=x_curve_c,
            y=y_curve_c,
            mode="lines",
            showlegend=False,
            line=dict(color="green"),
        ),
        row=1,
        col=2,
    )

    # Lebesgue horizontal bands
    for y0_c in y_bands_c:
        y1_c = y0_c + dy_c
        mask_c = (y_curve_c >= y0_c) & (y_curve_c < y1_c)
        x_band_c = x_curve_c[mask_c]
        if len(x_band_c) == 0:
            continue
        x_min_c, x_max_c = x_band_c[0], x_band_c[-1]
        fig_c.add_shape(
            type="rect",
            x0=x_min_c,
            x1=x_max_c,
            y0=y0_c,
            y1=y1_c,
            fillcolor="rgba(0, 200, 0, 0.4)",
            line=dict(color="green"),
            row=1,
            col=2,
        )

    # Layout
    fig_c.update_layout(
        title="Riemann vs Lebesgue Integration Illustration",
        xaxis=dict(scaleanchor="y", range=[-1.2, 1.2]),
        yaxis=dict(scaleanchor="x", range=[-0.1, 1.1]),
        xaxis2=dict(scaleanchor="y2", range=[-1.2, 1.2]),
        yaxis2=dict(scaleanchor="x2", range=[-0.1, 1.1]),
        template="plotly_white",
        showlegend=False,
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
    Write down the expression that calculate the signed area under the curve $y = x^2 + 4$ on $[1, 4]$.

    First we divide $[1,4]$ to $n$ sub-intervals, then each interval has length $\displaystyle \frac{4-1}{n} = \frac{3}{n}$. This is our $\Delta(x)$.

    This means our intervals are $\displaystyle [1,1+\frac{3}{n}]$, $\displaystyle [1+\frac{3}{n}, 1+ 2\times \frac{3}{n}]$, $\displaystyle [1+2 \times\frac{3}{n}, 1+ 3\times \frac{3}{n}]$ and so on, and up to $\displaystyle [1+(n-1) \times\frac{3}{n}, 1+ n\times \frac{3}{n}]$ (or $\displaystyle [1+(n-1)\times \frac{3}{n},4]$).

    Let us use the right endpoint because it's in the definition: they are $\displaystyle 1 + \frac{3}{n}, 1+ 2 \times \frac{3}{n}$, up to $\displaystyle 1+ n\times \frac{3}{n}$.

    So the expression we want should be $$A = \lim\limits_{n \to \infty}\sum_{i = 1}^nf(x_i)\Delta(x)= \lim\limits_{n \to \infty}\sum_{i = 1}^n\left[((1+ i \times \frac{3}{n})^2+4)\cdot \frac{3}{n}\right].$$ We can do some algebra to simplify it, we can get $$\lim\limits_{n \to \infty}\sum\limits_{i=1}^n\left( \frac{15}{n} + \frac{18i}{n^2} + \frac{27i^2}{n^3}\right).$$
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
    Suppose the expression of area of region under a curve is given as $\displaystyle \lim\limits_{n \to \infty}\sum\limits_{i=1}^n\sin(\frac{i\pi}{4n})\frac{\pi}{4n}$. What are the bounds of this region?

    A natural choice is to understand the expression with that $\displaystyle \sin(\frac{i\pi}{4n})$ is our $f(x_i)$, and $\displaystyle \frac{\pi}{4n}$ is our $\Delta(x)$.

    Since $\displaystyle \Delta(x) = \frac{b-a}{n}$, we should have $\displaystyle b - a = \frac{\pi}{4}$ (but we don't know what is $a$ and $b$).

    We can choose to consider $f(x) = \sin(x)$, then we should have $\displaystyle x_i = \frac{i\pi}{4n}$. These values should satisfy that $\displaystyle x_n - x_0 = \frac{\pi}{4}$. Check: $\displaystyle x_n - x_0 = \frac{n\pi}{4 n} - \frac{0\pi}{4n}$ $\displaystyle =\frac{\pi}{4}$ indeed. Our $a = x_0 = 0$, and $\displaystyle b = a + \frac{\pi}{4} = \frac{\pi}{4}$.

    Thus the region is bounded by $\displaystyle f(x) = \sin(x), x = 0, x = \frac{\pi}{4}$, and $x$-axis.
    """
    )
    return


if __name__ == "__main__":
    app.run()
