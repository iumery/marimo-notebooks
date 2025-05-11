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
    mo.md(r"""# 3.3 Derivatives and the Shapes of Graphs""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Introduction""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Recall that in section 3.1 we learnt that if a function $f$ has an (absolute or local) extremum at $c$, then $c$ must be a critical point of $f$. But it does not tell us what exact is that point. Is it a local maximum? Local minimum? How can you be sure of it?

    **Moving onward, for simplicity we assume that $f$ is continuous, and piecewise smooth in this section**. The latter means that $f$ can be differentiated indefinitely many times at all the points in its domain except for possibly a set of discrete points.

    Before we start, start to think about a question, (assume $f$ is differentiable) what characterize a local maximum or minimum? How can this character be stated in a mathematical way?

    For example, here we see a local maximum at $0$:
    """
    )
    return


@app.cell
def _(go, np):
    # Define function
    x_parabola = np.linspace(-3, 3, 400)
    y_parabola = -x_parabola**2 + 4

    # Maximum point
    x_max = 0
    y_max = -x_max**2 + 4

    # Create figure
    fig_parabola = go.Figure()

    # Plot the function
    fig_parabola.add_trace(go.Scatter(
        x=x_parabola,
        y=y_parabola,
        mode='lines',
        name='f(x) = -x² + 4',
        line=dict(color='blue')
    ))

    # Mark local max at (0, 4)
    fig_parabola.add_trace(go.Scatter(
        x=[x_max], y=[y_max],
        mode='markers+text',
        text=['Local Max<br>(0, 4)'],
        textposition='top right',
        marker=dict(size=10, color='red'),
        name='Local Max'
    ))

    # Layout
    fig_parabola.update_layout(
        title='f(x) = -x² + 4 with Local Maximum at x = 0',
        xaxis_title='x',
        yaxis_title='f(x)',
        template='plotly_white'
    )
    return


@app.cell
def _(mo):
    mo.md(r"""A natural way to characterize the local maximum $0$, is that $f$ is **increasing before $0$, but decreasing after $0$**. A natural way to characterize the local minimum $0$, is that $f$ is **decreasing before $0$, and increasing after $0$**.""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Increasing/Decreasing Test""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    1. If $f'(x) > 0$ for all $x$ on an (open) interval, then $f$ is increasing on that interval;
    2. If $f'(x) < 0$ for all $x$ on an (open) interval, then $f$ is decreasing on that interval.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Proof""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    For an intuitive proof, recall the derivative is the same thing as 'slope of tangent line'. Try some graphs of some functions, we should be able to see that upwards tangent line (i.e. positive slope, i.e. positive derivative) means the function is increasing, and downwards tangent line means the function is decreasing.

    For a formal proof, we can use the MVT. The proof is omitted here.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## The First Derivative Test""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Suppose $c$ is a critical point of $f$, then:

    1. If $f'$ **changes to being negative** at $c$, or if $f'$ **changes from being positive** at $c$, then $f$ has a **local maximum** at $c$;
    2. If $f'$ **changes to being positive** at $c$, or if $f'$ **changes from being negative** at $c$, then $f$ has a **local minimum** at $c$;
    3. If $f'$ **remains** being positive or being negative at $c$, $f$ does not have a local extremum at $c$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    /// admonition | 0
        type: info

    Technically, every "negative" above should be "non-positive", every "positive" above should be "non-negative", every $<$ above should be $\le$, and every $>$ above should be $\ge$.

    These "$=0$" cases corresponds to places on the graph that is horizontal lines (function is constant), and they are in some sense not very interesting because every point in that area is both local max and local min. **For simplicity and less confusion, in the following discussion (and 3.4) we are assuming the function is not a constant.
    """
    )
    return


@app.cell
def _(go, make_subplots, np):
    # Create subplot grid
    fig_fd = make_subplots(
        rows=2, cols=2,
        subplot_titles=[
            "No Extrema",
            "No Extrema",
            "Local Min",
            "Local Max"
        ]
    )

    # x range
    x_vals_fd = np.linspace(-2, 2, 400)

    y1 = -x_vals_fd**3
    fig_fd.add_trace(go.Scatter(x=x_vals_fd, y=y1, mode='lines', name='Local Max', line=dict(color='blue')), row=1, col=1)
    fig_fd.add_trace(go.Scatter(
        x=[0], y=[0], mode='markers+text',
        text=['No Extrema'],
        textposition='top right',
        marker=dict(size=8, color='red')
    ), row=1, col=1)

    y2 = x_vals_fd**3
    fig_fd.add_trace(go.Scatter(x=x_vals_fd, y=y2, mode='lines', name='Local Min', line=dict(color='green')), row=1, col=2)
    fig_fd.add_trace(go.Scatter(
        x=[0], y=[0], mode='markers+text',
        text=['No Extrema'],
        textposition='bottom right',
        marker=dict(size=8, color='red')
    ), row=1, col=2)

    y3 = x_vals_fd**2
    fig_fd.add_trace(go.Scatter(x=x_vals_fd, y=y3, mode='lines', name='Local Min', line=dict(color='orange')), row=2, col=1)
    fig_fd.add_trace(go.Scatter(
        x=[0], y=[0], mode='markers+text',
        text=['Local Min'],
        textposition='bottom right',
        marker=dict(size=8, color='red')
    ), row=2, col=1)

    y4 = -x_vals_fd**2
    fig_fd.add_trace(go.Scatter(x=x_vals_fd, y=y4, mode='lines', name='Local Min', line=dict(color='purple')), row=2, col=2)
    fig_fd.add_trace(go.Scatter(
        x=[0], y=[0], mode='markers+text',
        text=['Local Max'],
        textposition='bottom right',
        marker=dict(size=8, color='red')
    ), row=2, col=2)

    # Layout
    fig_fd.update_layout(
        title="First Derivative Test — 4 Scenarios",
        template="plotly_white",
        height=700
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    If (piece-wise smooth) $f$ is defined on a closed interval $[a, b]$, then $f'$ must be changing at $a$ and $b$:

    $f'$ is of course DNE before $a$ because $f$ is not even defined there, and $f'$ is either positive or negative after $a$ (see remark above, we exclude the cases that the graph is flat), thus $f'$ **changes** from being DNE to being positive/negative at $a$. Similar for $b$.

    **In particular, if (piece-wise smooth) $f$ is defined on a closed interval $[a, b]$, then $a, b$ must be local extremes**.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    /// admonition | Draw the diagram!
        type: info

    Don't try to memorize this theorem directly - it's very likely to make a mistake. Whenever you need to use them, just draw a simple diagram and extract information from there.

    ///
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
    Find the local minimums and maximums of the function $f(x) = 3x^4 - 4x^3 - 12x^2 + 5$ defined on $[-2, 3]$.

    Calculate $f'(x) = 12x^3 - 12x^2 -24x$, factor it to get $f'(x) = 12x(x-2)(x+1)$. We can use the following table to determine the sign of $f'(x)$:

    | Interval | $12x$ | $x-2$ | $x+1$ | $f'(x)$ |
    |:--:|:--:|:--:|:--:|:--:|
    | $x<-1$ | $-$ | $-$ | $-$ | $-$ |
    | $-1<x<0$ | $-$ | $-$ | $+$ | $+$ |
    | $0<x<2$ | $+$ | $-$ | $+$ | $-$ |
    | $x<2$ | $+$ | $+$ | $+$ | $+$ |

    The columns of this table are individual terms of $f'(x)$, follows by $f'(x)$ itself. The rows of this table are the domain of $f(x)$ (NOT $f'(x)$!) separated by the critical points of $f(x)$, i.e. when $f'(x) = 0$ or DNE.

    For each cell except for the last column ($f'(x)$ column), we plug-in any number in the row name to the column name, calculate it and get the **sign** of the result.

    After we get everything except for the last column, we calculate the last column by counting numbers of $-$ in that row. If there are odd number of $-$ in that row, the last column also has $-$. If there are even number of $-$ in that row, the last column has $+$.

    For example, we have $-$ on first row last column, because there are three (odd) $-$ on that row already. We have $+$ on the second row last column, because there are two (even) $-$ on the row.

    Thus $f'$ changes from positive to negative at $0$, changes from negative to positive at $-1$ and $2$. Also, it is negative after the left-endpoint $-2$, and positive before the right-endpoint $3$.

    Thus by the First Derivative Test, we have that:

    1. $-2,0,3$ are local maximums;
    2. $-1,2$ are local minimums.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Restriction of the First Derivative Test""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    In some sense the First Derivative Test is complicated - we have to calculate a lot of things - which in general is hard (or even impossible). For example, what if in the above example we have a polynomial of degree $10$? Then the derivative has degree $9$, and there is no way to factor it, thus there is no way to tell when does it change signs.

    We will now learn an easier test (but has more restriction).
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Concavity""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    We say a function $f$ is concave upward on an interval $I$ if its graph on the interval $I$ lies above all its tangents on $I$; concave downward on an interval $I$ if its graph on the interval $I$ lies below all its tangents on $I$.

    A point $p$ on the graph of $f$ is called an inflection point if $f$ is continuous there and the function changes from concave downward to upward, or from concave upward to downward at $p$.
    """
    )
    return


@app.cell
def _(go, np):

    # Function and domain
    x_inflect = np.linspace(-3, 3, 400)
    f_inflect = x_inflect**3

    # Regions
    x_left = x_inflect[x_inflect < 0]
    y_left = x_left**3

    x_right = x_inflect[x_inflect > 0]
    y_right = x_right**3

    # Create plot
    fig_inflect = go.Figure()

    # Concave down region
    fig_inflect.add_trace(go.Scatter(
        x=x_left, y=y_left,
        mode='lines',
        name='Concave Down',
        line=dict(color='blue', dash='solid')
    ))

    # Concave up region
    fig_inflect.add_trace(go.Scatter(
        x=x_right, y=y_right,
        mode='lines',
        name='Concave Up',
        line=dict(color='green', dash='solid')
    ))

    # Inflection point
    fig_inflect.add_trace(go.Scatter(
        x=[0], y=[0],
        mode='markers+text',
        text=["Inflection Point<br>(0, 0)"],
        textposition='top right',
        marker=dict(size=10, color='red'),
        name='Inflection Point'
    ))

    # Layout
    fig_inflect.update_layout(
        title='Concavity and Inflection Point: f(x) = x³',
        xaxis_title='x',
        yaxis_title='f(x)',
        template='plotly_white'
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    We have the following concavity test:

    1. If $f''(x)> 0$ for all $x \in I$, then $f$ is concave upward on $I$;
    2. If $f''(x)< 0$ for all $x \in I$, then $f$ is concave downward on $I$.

    Follow from the concavity test, we have the following test of local extremum:
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## The Second Derivative Test""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Suppose $f'(c) = 0$, then:

    1. If $f''(c) > 0$, then $f$ has a **local minimum** at $c$;
    2. If $f''(c) < 0$, then $f$ has a **local maximum** at $c$.

    The 'restriction' mentioned above is that, by writing down this statement, we are assuming the second derivative exists (and continuous at $c$), this is apparently not required for the First Derivative Test.

    In the scope of this course, however, this *usually* won't be a big problem, because most functions we are dealing with are actually smooth.

    **If, however, we want to describe function without a continuous second derivative, we may need to go back to the First Derivative Test**.

    **Or, if the second derivative exists but equals $0$, then the Second Derivative Test does not tell us anything so again we need to go back and use the First Derivative Test**.

    Also note that if $f$ is defined on a closed interval, then the First Derivative Test is sufficient to tell us the information about the endpoints.
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
    Consider the function $f(x) = (x-1)^{1/3}(x+1)$, so that $\displaystyle f'(x) = \frac{4(2x-1)}{3(x-1)^{2/3}}$ and $\displaystyle f''(x) = \frac{4(x-2)}{9(x-1)^{5/3}}$. What information can we get from the First Derivative Test, Concavity Test, and Second Derivative Test?

    First we need to determine what are some 'important values': these are the values $x$ where the first or the second derivative may change signs. In our case, they are $\displaystyle \frac{1}{2}$, $1$, and $2$, we can write down the table:

    | Interval | $2x-1$ | $(x-1)^{2/3}$ | $(x-2)$ | $(x-1)^{5/3}$ | $f'$ | $f''$ |
    |:--:|:--:|:--:|:--:|:--:|:--:|:--:|
    | $x<\frac{1}{2}$ | $-$ | $+$ | $-$ | $-$ | $-$ | $+$ |
    | $\frac{1}{2}<x<1$ | $+$ | $+$ | $-$ | $-$ | $+$ | $+$ |
    | $1<x<2$ | $+$ | $+$ | $-$ | $+$ | $+$ | $-$ |
    | $2<x$ | $+$ | $+$ | $+$ | $+$ | $+$ | $+$ |

    **(Be careful here! $(x-1)^{2/3}$ is always positive because the power is 'even' in the sense that the numerator of the power is even)**
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    /// admonition | One table vs two tables
        type: info

    Here I put two sign tables into one. You don't have to do it. You may do one table for $f'(x)$ and the other one for $f''(x)$.

    ///
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Results of First Derivative Test:

    1. $\displaystyle \frac{1}{2}$ is local minimum;
    2. $1$ is not local extremum;
    3. $2$ is not local extremum.

    Results of Concavity Test:

    1. $f$ is concave upward on $(-\infty, 1)$;
    2. $f$ is concave downward on $(1,2)$;
    3. $f$ is concave upward on $(2, \infty)$.

    In particular, $1$ and $2$ are ($x$-xis of) the inflection points.

    Since $\displaystyle f'(x) = \frac{4(2x-1)}{3(x-1)^{2/3}}$, $f'(x) = 0$ if and only if the numerator is zero, so $f'(x) = 0$ at $\displaystyle \frac{1}{2}$. At $\displaystyle \frac{1}{2}$, plug it into $\displaystyle f''(x) = \frac{4(x-2)}{9(x-1)^{5/3}}$ and we shall see it is positive, thus the Second Derivative Test tells us $\displaystyle \frac{1}{2}$ is a local minimum.

    A quick check: results of First/Second Derivative Test are the same.

    This is the graph of $f$ if we put it into a graphic calculator, it is consistent with the results above:
    """
    )
    return


@app.cell
def _(go, np):
    # Define the function
    def f_custom(x):
        return np.cbrt(x - 1) * (x + 1)

    # Domain
    x_vals_plot = np.linspace(-4, 4, 500)
    y_vals_plot = f_custom(x_vals_plot)

    # Create plot
    fig_custom = go.Figure()

    fig_custom.add_trace(go.Scatter(
        x=x_vals_plot,
        y=y_vals_plot,
        mode='lines',
        name=r'$f(x) = (x - 1)^{1/3} \cdot (x + 1)$',
        line=dict(color='blue')
    ))

    # Optional: mark origin or key point
    fig_custom.add_trace(go.Scatter(
        x=[1],
        y=[f_custom(1)],
        mode='markers+text',
        text=["x = 1"],
        textposition='top right',
        marker=dict(size=8, color='red'),
        name='x = 1'
    ))

    # Layout
    fig_custom.update_layout(
        title=r'Graph of $f(x) = (x - 1)^{1/3}(x + 1)$',
        xaxis_title='x',
        yaxis_title='f(x)',
        template='plotly_white'
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
