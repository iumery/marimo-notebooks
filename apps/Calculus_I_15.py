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
    mo.md(r"""# 3.2 The Mean Value Theorem""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Rolle's Theorem""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Suppose $f$ is a function such that:

    1. $f$ is **continuous** on a **closed** interval $[a, b]$;
    2. $f$ is **differentiable** on the **open** interval $(a, b)$;
    3. $f(a) = f(b)$.

    Then there exists $c$ on the **open** interval $(a, b)$ such that $f'(c) = 0$. In other words, there is a point $c \in (a, b)$ such that the tangent line of the graph at $(c, f(c))$ is horizontal.

    For example, $f(x) = x^2$ is continuous on $[-1, 1]$, it is differentiable on $(-1, 1)$, and $f(-1) = f(1) = 1$, thus there exists some number $c$ such that $f'(c) = 0$. In this particular case, it is not hard to see indeed $f'(0) = 0$.

    **None of the assumptions of the theorem can be omitted**:

    1. Consider the function with the following graph 1:
    	$$f(x) = \begin{cases} x,& 0 < x<5 \\ 1,& x = 0, 5\end{cases}$$
    	Then $f$ is differentiable on $(0,5)$ (second assumption is satisfied), $f(0) = f(5)$ (third assumption is satisfied), but $f$ is not continuous on $[0,5]$ (first assumption is NOT satisfied). It is not hard to see there is no point on the graph with a horizontal tangent line;
    2. Consider the function with the following graph 2:
    	$g$ is continuous on $[0,10]$ (first assumption is satisfied), $g(0) = g(10)$ (third assumption is satisfied), but $g$ is not differentiable on $(0,10)$ (there is a corner) (second assumption is NOT satisfied). Again, there is no point on the graph with a horizontal tangent line;
    3. Consider the function with the following graph 3:
    	$$h(x) = \frac{1}{5}x^2, x \in [1, 6]$$
    	Then $h$ is continuous on $[1,6]$ (first assumption is satisfied), $h$ is differentiable on $(1, 6)$ (second assumption is satisfied), but $h(1) \ne h(6)$ (third assumption is NOT satisfied). There is no point on the graph with a horizontal tangent line.

    **Moral of the story: always verify the assumptions of a theorem before using it**. If you want to apply a theorem to a question on an exam, you **MUST verify the assumptions of that theorem**.
    """
    )
    return


@app.cell
def _(go, make_subplots, np):
    # Create subplots
    fig_rolle = make_subplots(rows=3, cols=1, subplot_titles=[
        "1. Not continuous at endpoints",
        "2. Not differentiable (corner at x=5)",
        "3. End-points values are different"
    ])

    # --- First plot: f(x) = x on (0,5), f(0) = f(5) = 1
    x_f = np.linspace(0, 5, 300)
    y_f = x_f
    y_f[0] = 1
    y_f[-1] = 1
    fig_rolle.add_trace(go.Scatter(
        x=x_f, y=y_f,
        mode='lines',
        name='f(x)',
        line=dict(color='blue')
    ), row=1, col=1)
    fig_rolle.add_trace(go.Scatter(
        x=[0, 5], y=[1, 1],
        mode='markers',
        marker=dict(size=8, color='blue'),
        name='f(0), f(5)'
    ), row=1, col=1)

    # --- Second plot: g(x) = x on [0,5], -x+10 on (5,10]
    x_g1 = np.linspace(0, 5, 200)
    y_g1 = x_g1
    x_g2 = np.linspace(5, 10, 200)
    y_g2 = -x_g2 + 10
    fig_rolle.add_trace(go.Scatter(x=x_g1, y=y_g1, mode='lines', name='g(x)', line=dict(color='green')), row=2, col=1)
    fig_rolle.add_trace(go.Scatter(x=x_g2, y=y_g2, mode='lines', name='', line=dict(color='green'), showlegend=False), row=2, col=1)
    fig_rolle.add_trace(go.Scatter(
        x=[0, 10], y=[0, 0],
        mode='markers',
        marker=dict(size=8, color='red'),
        name='g(0), g(10)'
    ), row=2, col=1)

    # --- Third plot: h(x) = 1/5 x² on [1,6]
    x_h = np.linspace(1, 6, 300)
    y_h = (1/5) * x_h**2
    fig_rolle.add_trace(go.Scatter(
        x=x_h,
        y=y_h,
        mode='lines',
        name='h(x)',
        line=dict(color='purple')
    ), row=3, col=1)
    fig_rolle.add_trace(go.Scatter(
        x=[1, 6], y=[(1/5)*1**2, (1/5)*6**2],
        mode='markers',
        marker=dict(size=8, color='red'),
        name='h(1), h(6)'
    ), row=3, col=1)

    # Mark h(1) = h(6) = 1.2 for clarity
    fig_rolle.add_trace(go.Scatter(
        x=[1, 6], y=[1.2, 1.2],
        mode='text',
        text=["h(1) = 1.2", "h(6) = 1.2"],
        textposition='top center',
        showlegend=False
    ), row=3, col=1)

    # Layout
    fig_rolle.update_layout(
        title='Rolle\'s Theorem: Importance of Assumptions',
        template='plotly_white',
        showlegend=False,
        height=1200
    )

    fig_rolle.update_xaxes(title_text='x', row=1, col=1)
    fig_rolle.update_yaxes(title_text='f(x)', row=1, col=1)
    fig_rolle.update_xaxes(title_text='x', row=2, col=1)
    fig_rolle.update_yaxes(title_text='g(x)', row=2, col=1)
    fig_rolle.update_xaxes(title_text='x', row=3, col=1)
    fig_rolle.update_yaxes(title_text='h(x)', row=3, col=1)
    return


@app.cell
def _(mo):
    mo.md(r"""### Example""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Suppose $f(x) = x^{10} - 6x^7 + 5x + 8$. Show there is a point $c$ in $[0,1]$ such that $f'(c) = 0$.

    We will try to apply Rolle's Theorem.

    1. $f$ is continuous on $[0,1]$ because it is a polynomial;
    2. $f$ is differentiable on $(0,1)$ because it is a polynomial;
    3. $f(0) = 8$ and $f(1) = 1-6+5+8 = 8$ thus $f(0) = f(1)$.

    Thus the assumptions of Rolle's Theorem are satisfied, the theorem applies and we have that there is a point $c$ in $[0,1]$ such that $f'(c) = 0$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Mean Value Theorem""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Suppose $f$ is a function such that:

    1. $f$ is **continuous** on a **closed** interval $[a, b]$;
    2. $f$ is **differentiable** on the **open** interval $(a, b)$.

    Then there exists $c$ on the **open** interval $(a, b)$ such that $f'(c) = \frac{f(b) - f(a)}{b - a}$. Visualize the theorem:
    """
    )
    return


@app.cell
def _(go, np):
    # Define function
    f_log = lambda x: np.log(x)
    df_log = lambda x: 1 / x

    # Interval
    a_log = 1
    b_log = np.e
    x_vals_log = np.linspace(a_log, b_log, 400)
    y_vals_log = f_log(x_vals_log)

    # Endpoints
    fa_log = f_log(a_log)
    fb_log = f_log(b_log)

    # Secant slope
    m_secant_log = (fb_log - fa_log) / (b_log - a_log)

    # MVT point: f'(c) = m ⇒ 1/c = m ⇒ c = 1/m
    c_log = 1 / m_secant_log
    fc_log = f_log(c_log)

    # Tangent line at c
    x_tangent_log = np.linspace(c_log - 0.5, c_log + 0.5, 100)
    y_tangent_log = m_secant_log * (x_tangent_log - c_log) + fc_log

    # Plot
    fig_log = go.Figure()

    # Function curve
    fig_log.add_trace(go.Scatter(
        x=x_vals_log, y=y_vals_log,
        mode='lines',
        name='f(x)',
        line=dict(color='blue')
    ))

    # Secant line
    fig_log.add_trace(go.Scatter(
        x=[a_log, b_log], y=[fa_log, fb_log],
        mode='lines',
        name='Secant Line',
        line=dict(color='green', dash='dot')
    ))

    # Tangent at c
    fig_log.add_trace(go.Scatter(
        x=x_tangent_log, y=y_tangent_log,
        mode='lines',
        name='Tangent at c',
        line=dict(color='red', dash='dash')
    ))

    # Mark point c
    fig_log.add_trace(go.Scatter(
        x=[c_log], y=[fc_log],
        mode='markers',
        text=[f"c ≈ {round(c_log, 2)}"],
        textposition='top right',
        marker=dict(size=8, color='black'),
        name='Point c'
    ))

    # Layout
    fig_log.update_layout(
        title='Mean Value Theorem',
        xaxis_title='x',
        yaxis_title='f(x)',
        template='plotly_white',
        showlegend=True
    )
    return


@app.cell
def _(mo):
    mo.md(r"""Rolle's Theorem is a special case of the MVT: if $f(a) = f(b)$, then $\frac{f(b) - f(a)}{b - a} = \frac{0}{b-a} = 0$ as stated in the Rolle's Theorem. Again, whenever you are asked to, or need to apply MVT, **you MUST verify the assumptions**.""")
    return


@app.cell
def _(mo):
    mo.md(r"""### Example 1""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Verify the assumptions of MVT for the function $\displaystyle f(x) = \frac{x}{x^2-2x-3}$ on $[1,2]$. State a result that you may get from MVT applied to this function.

    Since $f$ is a rational function, it is always continuous and differentiable unless the denominator is zero. In our case, it follows that $f$ is continuous on $[1,2]$ and differentiable on $(1,2)$ because the problematic points are when $x^2 - 2x - 3 = 0$ $\implies (x+1)(x-3) = 0$ $\implies x = -1, 3$, neither is inside $[1,2]$. Thus the assumptions have been verified.

    The MVT in this case tells us there exists $c \in (1,2)$ such that $\displaystyle f'(c) = \frac{f(2) - f(1)}{2 - 1}$ $\displaystyle = \frac{2}{2^2 - 2\cdot 2 - 3} - \frac{1}{1^2 - 2 \cdot 1 - 3}$ $\displaystyle = -\frac{5}{12}$.
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
    Suppose $f$ is a function that is continuous and differentiable everywhere, and that $3 \le f'(x) \le 5$ for all $x$. Show that $18 \le f(8) - f(2) \le 30$.

    Since $f$ is continuous and differentiable everywhere, we can apply MVT on any (closed) interval. Apply MVT on $[2, 8]$, we get that there exists point $c$ on $(2, 8)$ such that $\displaystyle f'(c) = \frac{f(8) - f(2)}{8 - 2}$. By the assumption of the question, we know that $\displaystyle 3 \le f'(c) = \frac{f(8) - f(2)}{8 - 2} \le 5$, or $\displaystyle 3 \le \frac{f(8) - f(2)}{6} \le 5$. Multiply everything by $6$ we get that $18 \le f(8) - f(2) \le 30$, as desired.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    /// admonition | Open Interval
        type: danger

    The point $c$ such that $\displaystyle f'(c) = \frac{f(b)-f(a)}{b-a}$ **must** lie on the **open** interval $(a,b)$. In particular, if a question asks you to find all $c$ satisfy the MVT, you should **exclude** $c$ that equals $a$ or $b$. See the following example:

    ///
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
    Consider the function $f(x) = x^3 - 2x + 4$ on $[-2,1]$. Why does the Mean Value Theorem apply? Find the value $c$ that satisfy the conclusion of MVT.

    Since $f$ is a polynomial, it is automatically continuous (on $[-2,1]$) and differentiable (on $(-2,1)$). By MVT, there are $c$ on $(-2,1)$ such that $\displaystyle f'(c) = \frac{f(1) - f(-2)}{1-(-2)}$ $\displaystyle =\frac{3}{3} = 1$, i.e. $f'(c) = 3c^2 - 2 = 1$ or $c^2 = 1$, which means $c = 1$ or $-1$.

    However, $c$ needs to be in the open interval $(-2,1)$, thus it can only be $-1$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Corollary""")
    return


@app.cell
def _(mo):
    mo.md(r"""Suppose $f$ is a function defined on an open interval $(a, b)$, then $f$ is a constant on $(a, b)$ if and only if $f'(x) = 0$ for all $x \in (a, b)$.""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Corollary of Corollary""")
    return


@app.cell
def _(mo):
    mo.md(r"""Suppose $f, g$ are two functions defined on an open interval $(a, b)$ and $f'(x) = g'(x)$ for all $x \in (a, b)$, then $f - g$ is a constant on $(a, b)$. In other words, $f(x) = g(x) + c$ for some constant $c$ for all $x \in (a, b)$.""")
    return


if __name__ == "__main__":
    app.run()
