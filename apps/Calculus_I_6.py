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
    mo.md(r"""# 2.1 Derivatives and Rates of Change""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Instantaneous Velocity Problem""")
    return


@app.cell
def _(go, np):
    # Define the domain
    t = np.linspace(0, 2.5, 500)
    f_t = -16 * t**2 + 40 * t

    # Create the plot
    fig_1 = go.Figure()

    fig_1.add_trace(go.Scatter(x=t, y=f_t, mode="lines", name="f(t)", line=dict(color="green")))

    # Customize layout
    fig_1.update_layout(
        title=r"f(t) = -16t² + 40t on [0, 2.5]",
        xaxis_title="t",
        yaxis_title="f(t)",
        template="plotly_white",
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Suppose a ball is thrown into the air, its height in feet $t$ seconds later is given by $f(t) = -16t^2 + 40 t$.

    You should know from a general physics class that speed equals distance divided by time, in particular, (assume $T$ is close enough to $2$,) the expression for the **average velocity** of the ball for the interval $2\le t \le T$ is given by $\displaystyle \frac{f(T) - f(2)}{T - 2}$, where the numerator can be viewed as the **displacement**, and the denominator can be viewed as the **change of time**.

    For example, we can calculate without too much difficulty, that the average velocity for time $2$ to $2.5$ seconds is $-32$ (feet per second).

    This value, on the graph, can be viewed as the slope of the straight line passing through $(2, f(2))$ and $(2.5, f(2.5))$.

    The instantaneous velocity of the ball at $t=2$, in the same sense, can be viewed as the time interval goes to 'instant', that is, the instantaneous velocity is $\displaystyle \lim\limits_{T \to 2} \frac{f(T) - f(2)}{T - 2}$. By the material from previous sections, we now have the tool to evaluate it, $\displaystyle \lim\limits_{T \to 2} \frac{f(T) - f(2)}{T - 2}$ $\displaystyle = \lim\limits_{T \to 2} \frac{-16T^2 + 40T - (-16\cdot 2^2 + 40 \cdot 2)}{T - 2}$ $\displaystyle = \lim\limits_{T \to 2} \frac{-16T^2 + 40T - 16}{T - 2}$ $\displaystyle = \lim\limits_{T \to 2} \frac{-8(2T^2 - 5T + 2)}{T - 2}$ $\displaystyle = \lim\limits_{T \to 2} \frac{-8(T-2)(2T-1)}{T - 2}$ $= \lim\limits_{T \to 2} -8(2T-1)$ $=-24$.

    This value can be viewed as the (limit) slope of the line that passing through the points $(2, f(2))$ and $(T, f(T))$ as $T \to 2$.

    But what if we want to know the general case? What is the instantaneous velocity at time $t$?
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Rate of Change""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Suppose $f(x)$ is a quantity that depends on $x$. If $x$ changes from $x_1$ to $x_2$, then $f(x)$ should change from $f(x_1)$ to $f(x_2)$. We denote the change $x_2 - x_1$ as $\Delta(x)$ and the change $f(x_2) - f(x_1)$ as $\Delta(f(x))$.

    The average rate of change of $f(x)$ with respect to $x$ over the interval $[x_1, x_2]$ is then the quantity $\displaystyle \frac{\Delta(f(x))}{\Delta(x)}$. It can be viewed as the slope of the line passing through $(x_1, f(x_1))$ and $(x_2, f(x_2))$.

    Analogy with the velocity problem, the instantaneous rate of change of $f(x)$ with respect of $x$ at $x = x_1$ is defined to be $\displaystyle \lim\limits_{x_1 \to x_2}\frac{f(x_2) - f(x_1)}{x_2 - x_1}$. We can substitute $x_2$ by $x_1 + \Delta(x)$ (so that taking limit as $x_1 \to x_2$ is the same as taking limit as $\Delta(x) \to 0$), and the instantaneous rate of change is thus equivalently defined to be $\displaystyle \lim\limits_{\Delta(x) \to 0} \frac{f(x_1 + \Delta(x)) - f(x_1)}{\Delta(x)}$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Tangent Line and Normal Line""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Given a curve of a function $f(x)$, the tangent line to the curve at a point $(p, f(p))$ is the line that passes through $(p, f(p))$ and has slope $\displaystyle m = \lim\limits_{x \to p} \frac{f(x) - f(p)}{x - p}$, that is, the instantaneous rate of change at $p$, provided that the limit exists.

    If the limit does not exists, then the tangent line does not exist.

    Given a curve of a function $f(x)$, the normal line to the curve at a point $(p, f(p))$ is the line that passes through $(p, f(p))$ and is orthogonal to the tangent line.

    Recall this means the slope of the normal line times the slope of the tangent line (at the same point) is $-1$.
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
    Consider $f(x) = -x^2 + x$, find the tangent line and normal line to the curve at $(1,0)$.

    The slope of the tangent line is $\displaystyle m_t = \lim\limits_{x \to p} \frac{f(x) - f(p)}{x - p}$ $\displaystyle = \lim\limits_{x \to 1} \frac{-x^2+x - 0}{x - 1}$ $\displaystyle = \lim\limits_{x \to 1}\frac{-x(x -1)}{x-1} = -1$.

    Thus the slope of the normal line is $1$.

    To find the tangent line, we need to find a line that has slope $-1$ and passes $(1, 0)$, that is a function of the form $y = m_tx + b_t$ where $m_t = -1$ and satisfies $0 = -1 +b_t$ thus $b_t = 1$, so the line is $y = -x + 1$.

    Similarly to find the normal line, we have to solve $y = m_nx + b_n$ where $m_n = 1$ and $0 = 1 + b_n$ thus $b_n = -1$, so the line is $y = x - 1$.
    """
    )
    return


@app.cell
def _(go, np):
    # Define x range
    x = np.linspace(-1, 2, 500)
    x_line = np.linspace(-1, 3, 500)
    f_x = -(x**2) + x

    # Tangent line at x = 1: y = -x + 1
    tangent = -x_line + 1

    # Normal line at x = 1: y = x - 1
    normal = x_line - 1

    # Create plot
    fig_2 = go.Figure()

    # Original function
    fig_2.add_trace(go.Scatter(x=x, y=f_x, mode="lines", name="f(x) = -x² + x", line=dict(color="blue")))

    # Tangent line
    fig_2.add_trace(
        go.Scatter(
            x=x_line,
            y=tangent,
            mode="lines",
            name="Tangent at (1, 0)",
            line=dict(color="red", dash="dash"),
        )
    )

    # Normal line
    fig_2.add_trace(
        go.Scatter(
            x=x_line,
            y=normal,
            mode="lines",
            name="Normal at (1, 0)",
            line=dict(color="green", dash="dot"),
        )
    )

    # Highlight point (1, 0)
    fig_2.add_trace(
        go.Scatter(
            x=[1],
            y=[0],
            mode="markers+text",
            name="Point (1, 0)",
            marker=dict(size=8, color="black"),
            text=["(1, 0)"],
            textposition="top right",
        )
    )

    # Layout
    fig_2.update_layout(
        title="Function, Tangent, and Normal at x = 1",
        xaxis_title="x",
        yaxis_title="y",
        template="plotly_white",
        xaxis=dict(scaleanchor="y"),
        yaxis=dict(scaleanchor="x"),
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    /// admonition | Point on the Graph
        type: danger

    The above calculation assumes that the point $(1, 0)$ is on the graph of $f$. In case it is not, this method does not apply.

    ///
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Derivative of a Function at a Point""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""The derivative of $f(x)$ at $p$, denoted by $f'(p)$, is defined to be the instantaneous rate of change of $f(x)$ at $p$, given that the limit exists. In other words, the derivative of $f(x)$ at $a$, denoted by $f'(a)$, is given by (provided that the following limits exist) $$f'(a) = \lim\limits_{h \to 0} \frac{f(a+h) - f(a)}{h},$$ or equivalently, $$f'(a) = \lim\limits_{b \to a} \frac{f(b) - f(a)}{b-a}.$$ In particular, derivative at $a$, instantaneous rate of change at $a$, and slope of tangent line at $a$ are **three names for the same quantity**. Derivative is more of an abstract term, instantaneous rate of change provides a physical meaning, and slope of tangent line provides a geometric meaning."""
    )
    return


if __name__ == "__main__":
    app.run()
