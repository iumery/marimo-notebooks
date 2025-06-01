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
    mo.md(r"""# 3.1 Maximum and Minimum Values""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Extremums""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    The concepts of maximum and minimum value of a function should be intuitive - they corresponds to the highest and lowest points of the graph of the function.

    To be more specific, we have the following definitions. Suppose $f: X \to Y$ is a function, then:

    1. We say that $f$ has an absolute maximum (point) at $c$, if $f(x) \le f(c)$ for all $x \in X$. We may also say that $f(c)$ is the absolute maximum value of $f$;
    2. We say that $f$ has an absolute minimum (point) at $c$, if $f(x) \ge f(c)$ for all $x \in X$. We may also say that $f(c)$ is the absolute minimum value of $f$;
    3. We say that $f$ has a local maximum (point) at $c$, if $f(x) \le f(c)$ for all $x$ in some open interval containing $c$. We may also say that $f(c)$ is a local maximum value of $f$;
    4. We say that $f$ has a local minimum (point) at $c$, if $f(x) \ge f(c)$ for all $x$ in some open interval containing $c$. We may also say that $f(c)$ is a local minimum value of $f$.
    """
    )
    return


@app.cell
def _(go, np):
    # Define function and domain
    x_vals_b = np.linspace(-np.pi, np.pi - 0.5, 800)
    f_b = lambda x: np.sin(2 * x) + x / 2
    y_vals_b = f_b(x_vals_b)

    # Critical points (approximate using derivative)
    from scipy.signal import argrelextrema

    # Detect interior extrema
    local_max_idx_b = argrelextrema(y_vals_b, np.greater)[0].tolist()
    local_min_idx_b = argrelextrema(y_vals_b, np.less)[0].tolist()

    # Manually include endpoints if they qualify
    if y_vals_b[0] > y_vals_b[1]:
        local_max_idx_b.insert(0, 0)
    elif y_vals_b[0] < y_vals_b[1]:
        local_min_idx_b.insert(0, 0)

    if y_vals_b[-1] > y_vals_b[-2]:
        local_max_idx_b.append(len(y_vals_b) - 1)
    elif y_vals_b[-1] < y_vals_b[-2]:
        local_min_idx_b.append(len(y_vals_b) - 1)

    # Absolute extrema at endpoints
    abs_min_x_b = x_vals_b[np.argmin(y_vals_b)]
    abs_max_x_b = x_vals_b[np.argmax(y_vals_b)]
    abs_min_y_b = min(y_vals_b)
    abs_max_y_b = max(y_vals_b)

    fig_b = go.Figure()

    # Plot the function
    fig_b.add_trace(
        go.Scatter(
            x=x_vals_b,
            y=y_vals_b,
            mode="lines",
            name="Graph of function",
            line=dict(color="blue"),
        )
    )

    # Local maxima
    for i in local_max_idx_b:
        fig_b.add_trace(
            go.Scatter(
                x=[x_vals_b[i]],
                y=[y_vals_b[i]],
                mode="markers+text",
                text=[f"Local Max"],
                textposition="top right",
                marker=dict(size=8, color="red"),
                name="Local Max",
            )
        )

    # Local minima
    for i in local_min_idx_b:
        fig_b.add_trace(
            go.Scatter(
                x=[x_vals_b[i]],
                y=[y_vals_b[i]],
                mode="markers+text",
                text=[f"Local Min"],
                textposition="bottom center",
                marker=dict(size=8, color="green"),
                name="Local Min",
            )
        )

    # Absolute min
    fig_b.add_trace(
        go.Scatter(
            x=[abs_min_x_b],
            y=[abs_min_y_b],
            mode="markers+text",
            text=[f"Abs Min"],
            textposition="top right",
            marker=dict(size=10, color="black"),
            name="Abs Min",
        )
    )

    # Absolute max
    fig_b.add_trace(
        go.Scatter(
            x=[abs_max_x_b],
            y=[abs_max_y_b],
            mode="markers+text",
            text=[f"Abs Max"],
            textposition="top left",
            marker=dict(size=10, color="orange"),
            name="Abs Max",
        )
    )

    # Layout
    fig_b.update_layout(
        title="Distinct Local and Absolute Extrema",
        xaxis_title="x",
        yaxis_title="f(x)",
        xaxis=dict(range=[-5, 4]),
        template="plotly_white",
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    /// admonition | Value vs Point
        type: info

    The convention is that '**… value' means for the $y$-coordinate** value and **'… point' means for the $x$-coordinate** value.

    ///
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    It particular, if the graph of the function is given, then absolute maximum correspond to the highest point(s) on the graph. There could be multiple absolute maximum because we used $\le$ in the definition. For example, $\sin(x)$ has infinitely absolute maximum.

    It should be clear that an absolute minimum (resp. maximum) is also a local minimum (resp. maximum). But a local minimum (resp. maximum) is not necessarily an absolute minimum (resp. maximum).

    There are also other names of the above terms, here are some that you should know:

    1. If $f$ has an absolute maximum or an absolute minimum at $c$, we say $f$ has an extremum, or an absolute extremum, at $c$. We may also say that $f(c)$ is an extreme value, or absolute extreme value, of $f$;
    2. If $f$ has a local maximum or a local minimum at $c$, we say $f$ has a local extremum at $c$. We may also say that $f(c)$ is a local extreme value of $f$.

    Recall that $\infty$ is NOT a real number, which means **we never have (absolute) extreme at $\infty$, or have $\infty$ being the (absolute) extreme value**. There are concepts that allow $\infty$ to be 'extreme values', called supremum and infimum, but they are out of scope of this course. In particular, absolute extremums may not exist.

    Local extremums also may not exist, though for a different reason.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Extreme Value Theorem""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""If $f$ is **continuous** and is defined on a **closed interval** $[a,b]$, then $f$ attains its **absolute maximum value and absolute minimum value** on the **closed interval** $[a,b]$."""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Remark 1 Assumptions of the Theorem""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    We have two assumptions: $f$ is **continuous**, and $f$ is defined on a **closed** interval, neither of them can be omitted:

    1. Consider a function with graph below, then:
    	$f$ is defined on a closed interval $[1,3]$ but $f$ is not continuous on $[1,3]$. $f$ does not have absolute maximum nor absolute minimum on $[a,b]$;
    2. Consider the function $f(x) = x$ defined on $\mathbb{R} = (-\infty, \infty)$. $f$ is continuous, but it is not defined on a closed interval. $f$ does not have absolute maximum nor absolute minimum on $(-\infty, \infty)$.
    """
    )
    return


@app.cell
def _(go, np):
    # Left and right of the discontinuity
    x1_evt = np.linspace(1, 1.99, 400)
    x2_evt = np.linspace(2.01, 3, 400)
    f_evt = lambda x: 1 / (x - 2)

    y1_evt = f_evt(x1_evt)
    y2_evt = f_evt(x2_evt)

    # Vertical asymptote at x = 2
    x_asym_evt = [2, 2]
    y_asym_evt = [-20, 20]

    # Plot
    fig_evt = go.Figure()

    # Left and right branches
    fig_evt.add_trace(
        go.Scatter(
            x=x1_evt, y=y1_evt, mode="lines", name="Graph of f", line=dict(color="blue")
        )
    )
    fig_evt.add_trace(
        go.Scatter(
            x=x2_evt,
            y=y2_evt,
            mode="lines",
            name="",
            line=dict(color="blue"),
            showlegend=False,
        )
    )
    fig_evt.add_trace(
        go.Scatter(
            x=[2],
            y=[0],
            mode="markers",
            name="",
            line=dict(color="blue"),
            showlegend=False,
        )
    )

    # Vertical asymptote
    fig_evt.add_trace(
        go.Scatter(
            x=x_asym_evt,
            y=y_asym_evt,
            mode="lines",
            name="Discontinuity at x = 2",
            line=dict(color="red", dash="dot"),
        )
    )

    # Layout
    fig_evt.update_layout(
        title="Function Discontinuous on [1, 3] — EVT Fails",
        xaxis_title="x",
        yaxis_title="f(x)",
        xaxis=dict(range=[0.9, 3.1]),
        yaxis=dict(range=[-20, 20]),
        template="plotly_white",
    )
    return f_evt, x_asym_evt, y_asym_evt


@app.cell
def _(mo):
    mo.md(r"""### Remark 2 How to Correctly Use a Theorem""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Whenever you want to use a theorem, you have to check its assumptions**. Here is an easy example of how should you write down a solution of a problem involving using a theorem:

    Use the EVT to show $f: [0, 1] \to \mathbb{R}$ given by $f(x) = 2x^2 + 3$ has absolute extremes.

    By the description of the problem, $f$ is defined on a closed interval $[0,1]$. $f$ is continuous because $f$ is a polynomial. Thus by EVT, $f$ has absolute extremes on $[0,1]$.

    Does $f(x) = 2x^2 +3$ have absolute extremes on $(-10,10)$? Probably it does, but that is NOT the result of EVT, since it is defined on $(-10, 10)$ which is an open interval, but the assumption is that the interval should be closed.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Critical Point""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Suppose $f(x)$ is a function, then we say that $c$ is a critical point (or a critical number) of $f$, if $f'(c) = 0$ **or $f'(c)$ does not exist**. In this case, we also say $f(c)$ is a critical value of $f$.

    **In particular, if $f$ is defined on a closed interval, then the end-points of its domain are always critical points** (because the derivative is never defined there).
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Fermat's Theorem""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Let $f(x)$ be a function. Suppose $f$ has an absolute extremum or local extremum at $c$, then $c$ is a critical point of $f$.

    The converse is not true. Consider $f(x) = x^3$ defined on $\mathbb{R}$, then $0$ is a critical point because $f'(0) = 3\cdot 0^2 = 0$ but it is not an (absolute or local) extremum point.
    """
    )
    return


@app.cell
def _(go, np):
    # Define function
    x_cp = np.linspace(-5, 5, 400)
    y_cp = x_cp**3

    # Create figure
    fig_cp = go.Figure()

    # Plot f(x) = x^3
    fig_cp.add_trace(
        go.Scatter(
            x=x_cp, y=y_cp, mode="lines", name="f(x) = x³", line=dict(color="blue")
        )
    )

    # Mark the critical point at (0, 0)
    fig_cp.add_trace(
        go.Scatter(
            x=[0],
            y=[0],
            mode="markers+text",
            marker=dict(size=10, color="red"),
            text=["Critical Point (0, 0)<br>Not a Local Extrema"],
            textposition="top right",
            name="Critical Point",
        )
    )

    # Layout
    fig_cp.update_layout(
        title="f(x) = x³ — Critical Point with No Local Min or Max",
        xaxis_title="x",
        yaxis_title="f(x)",
        template="plotly_white",
        xaxis=dict(range=[-6, 6]),
        yaxis=dict(range=[-10, 10]),
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Fermat's Theorem tells us to find the extremums of $f$, we only need to check the critical points. However, remember that:

    1. Say $c$ is a critical point of $f$, if we only use Fermat's Theorem, it will not tell us if this point is absolute maximum/minimum or local maximum/minimum;
    2. None of absolute or local extremums has to exist.
    """
    )
    return


@app.cell
def _(f_evt, go, np, x_asym_evt, y_asym_evt):
    # Left and right of the discontinuity
    x1_evt_2 = np.linspace(1, 1.99, 400)
    x2_evt_2 = np.linspace(2.01, 3, 400)
    f_evt_2 = lambda x: 1 / (x - 2)

    y1_evt_2 = f_evt(x1_evt_2)
    y2_evt_2 = f_evt(x2_evt_2)

    # Vertical asymptote at x = 2
    x_asym_evt_2 = [2, 2]
    y_asym_evt_2 = [-20, 20]

    # Plot
    fig_evt_2 = go.Figure()

    # Left and right branches
    fig_evt_2.add_trace(
        go.Scatter(
            x=x1_evt_2,
            y=y1_evt_2,
            mode="lines",
            name="Graph of f",
            line=dict(color="blue"),
        )
    )
    fig_evt_2.add_trace(
        go.Scatter(
            x=x2_evt_2,
            y=y2_evt_2,
            mode="lines",
            name="",
            line=dict(color="blue"),
            showlegend=False,
        )
    )
    fig_evt_2.add_trace(
        go.Scatter(
            x=[2],
            y=[0],
            mode="markers",
            name="",
            line=dict(color="blue"),
            showlegend=False,
        )
    )

    # Vertical asymptote
    fig_evt_2.add_trace(
        go.Scatter(
            x=x_asym_evt,
            y=y_asym_evt,
            mode="lines",
            name="Discontinuity at x = 2",
            line=dict(color="red", dash="dot"),
        )
    )

    # Layout
    fig_evt_2.update_layout(
        title="Function Discontinuous on [1, 3] — EVT Fails",
        xaxis_title="x",
        yaxis_title="f(x)",
        xaxis=dict(range=[0.9, 3.1]),
        yaxis=dict(range=[-20, 20]),
        template="plotly_white",
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    For example, consider the function with the above graph again:

    $2$ is a critical point of $f$ because $\displaystyle f'(2)$ does not exist (why?). It is not an (absolute or local) extremum. $1$ and $3$ are also critical points (they are end-points), from the graph we can see they are local maximum / minimum respectively, but it is not a direct result from Fermat's Theorem.

    Nevertheless, we can have specific solution for a much restricted type of question:
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Closed Interval Method""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    By Fermat's Theorem, we can find the **absolute** extremums of a **continuous** function $f$ on a **closed** interval $[a, b]$. Here are the steps:

    1. Find the critical points of $f$, that is, $c \in [a, b]$ such that $f'(c) = 0$ or $f'(c)$ does not exist. **Remember to include $a, b$** because the end-points are always critical points;
    2. Evaluate $f(c)$ at all the critical points $c$ we found above;
    3. Compare those values, the largest value from step 2 is the absolute maximum value of $f$ and the corresponding $c$ is the absolute maximum of $f$; the smallest value from step 2 is the absolute minimum value of $f$ and the corresponding $c$ is the absolute minimum of $f$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    /// admonition | End-points
        type: danger

    When you apply the closed interval method, always remember to include the end-points. They are crucial.

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
    Find the absolute maximum and minimum of $f(x) = (x^2-1)^5$ defined on $[0,2]$.

    First, we need to find the critical points, these are $c$'s inside $[0,2]$ that satisfy $f'(c) = 0$ or $f'(c)$ does not exist. We evaluate the derivative of $f$ first: $f'(x) = 5(x^2-1)^4(2x)$ (apply Chain Rule) $= 10x(x^2-1)^4$.

    Do not expand the expression here: to find $c$ such that $f'(c) = 0$, we want to have $10x(x^2-1)^4 = 0$, that is either $x = 0$ or $x^2 - 1 = 0 \implies x = \pm 1$. Since $0$ is an end-point, technically $f'(0)$ is not $0$, but $0$ is a critical point anyway. We also need to include $2$ (it is an end-point) and exclude $-1$ (it is not in $[0,2]$).

    So the candidates for the extremums are $0, 1, 2$. We evaluate the function at these points: $f(0) = (0^2 - 1)^5 = -1$, $f(1) = (1^2-1)^5 = 0$, and $f(2) = (4-1)^5 = 243$.

    Compare these values, we shall see the absolute maximum is achieved at $0$ with value $-1$, absolute minimum is achieved at $2$ with value $243$.

    On the exam the question may specifically ask you to provide $(x,y)$ coordinates for the extremum points, in that case, you should write $(0,-1)$ and $(2, 243)$.
    """
    )
    return


if __name__ == "__main__":
    app.run()
