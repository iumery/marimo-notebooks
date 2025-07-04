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
    mo.md(r"""# 1.4 Calculating Limits""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Limit""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""Recall that we say $\lim\limits_{x\to a}f(x) = L$ if there exists $L$ such that $f(x)$ is arbitrarily close to $L$ whenever $x$ is sufficiently close to $a$."""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Main Limit Theorem""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    We can do operations on limits in the usual sense. Remember we cannot simply divide number by zero. Suppose $\lim\limits_{x\to a}f(x)$ and $\lim\limits_{x\to a}g(x)$ both exists and $c$ denotes a constant, then:

    1. $\lim\limits_{x\to a}(f(x)+g(x)) = \lim\limits_{x\to a}f(x)+\lim\limits_{x\to a}g(x)$;
    2. $\lim\limits_{x\to a}(f(x)-g(x)) = \lim\limits_{x\to a}f(x)-\lim\limits_{x\to a}g(x)$;
    3. $\lim\limits_{x\to a}(f(x)\cdot g(x)) = \lim\limits_{x\to a}f(x) \cdot \lim\limits_{x\to a}g(x)$;
    4. $\lim\limits_{x\to a}\frac{f(x)}{g(x)} = \frac{\lim\limits_{x\to a}f(x)}{\lim\limits_{x\to a}g(x)}$ provided that $\lim\limits_{x\to a}g(x) \ne 0$;
    5. $\lim\limits_{x\to a}(cf(x)) = c \lim\limits_{x\to a}f(x)$;
    6. $\lim\limits_{x\to a}(f(x))^n = (\lim\limits_{x\to a}f(x))^n$;
    7. $\lim\limits_{x\to a}\sqrt[n]{f(x)} = \sqrt[n]{\lim\limits_{x\to a}f(x)}$;
    8. $\lim\limits_{x\to a}c = c$;
    9. **If we somehow know $f$ is continuous at $a$**, then $\lim\limits_{x\to a}f(x) = f(a)$.

    These statements also work for one-side-limits: replace all $\lim\limits_{x \to a}$ by $\lim\limits_{x \to a^+}$ or $\lim\limits_{x \to a^-}$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Example (Evaluating Limits)""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    1. $\displaystyle \lim\limits_{x\to 2}\frac{x^2 + 5x + 3}{x-1}$ $\displaystyle = \frac{2^2+5\cdot 2 + 3}{2-1}$ $=17$;
    2. $\displaystyle \lim\limits_{x\to 0}(\frac{1}{x} + \frac{1}{x^2-x})$ $\displaystyle = \lim\limits_{x\to 0}\frac{x}{x^2-x}$ $\displaystyle =\lim\limits_{x\to 0}\frac{1}{x-1}$ $=-1$;
    3. $\displaystyle \lim\limits_{x\to 0}\frac{\sqrt{x^2+9}-3}{x^2}$ $\displaystyle = \lim\limits_{x\to 0}\frac{\sqrt{x^2+9}-3}{x^2} \cdot \frac{\sqrt{x^2+9}+3}{\sqrt{x^2+9}+3}$ $\displaystyle = \lim\limits_{x\to 0} \frac{x^2}{x^2(\sqrt{x^2+9}+3)}$ $\displaystyle = \lim\limits_{x\to 0}\frac{1}{(\sqrt{x^2+9}+3)} = \frac{1}{6}$.
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
        r"""
    $\lim\limits_{x\to a}f(x) = L$ if and only if $\lim\limits_{x\to a^+}f(x) = L$ and $\lim\limits_{x\to a^-}f(x) = L$, with the possible exceptions at end-points.

    For example, if we are given $f(x)$ whose domain is $[1,2]$, then $\lim\limits_{x\to 1^-}f(x)$ does not make much sense because there is no $x$ in the domain of $f$ such is smaller than $1$: in this case, $\lim\limits_{x \to 1}f(x) = L$ as long as $\lim\limits_{x \to 1^+}f(x) = L$. Similar for the other end-point.
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
    Consider the function $$f(x) = \begin{cases} x^2+5x, & x<2,\\ 6x+2, & x \ge 2. \end{cases}$$
    Does $\lim\limits_{x\to 2}f(x)$ exist? If it does, what is it?
    Using rule 9. (why are these function continuous? We (will) know (that from Section 1.5 that) $\lim\limits_{x \to 2^-}f(x) = 2^2 + 5\cdot 2 = 14$, and $\lim\limits_{x \to 2^+}f(x) = 6\cdot 2 + 2 = 14$. Since they are equal, by the above theorem, $\lim\limits_{x\to 2}f(x)$ exists and equals $14$.
    """
    )
    return


@app.cell
def _(go, np):
    # Define x ranges
    x1 = np.linspace(-5, 2, 300, endpoint=False)  # x < 2
    x2 = np.linspace(2, 5, 300)  # x >= 2

    # Define y values for each piece
    y1 = x1**2 + 5 * x1
    y2 = 6 * x2 + 2

    # Evaluate the function exactly at x = 2
    x_split = 2
    y_split = 6 * x_split + 2  # Since x = 2 is included in the second piece

    # Create figure
    fig = go.Figure()

    # Add first piece: solid line
    fig.add_trace(
        go.Scatter(
            x=x1, y=y1, mode="lines", name="x² + 5x", line=dict(dash="solid", width=3)
        )
    )

    # Add second piece: dashed line
    fig.add_trace(
        go.Scatter(
            x=x2, y=y2, mode="lines", name="6x + 2", line=dict(dash="dash", width=3)
        )
    )

    # Add splitting point marker
    fig.add_trace(
        go.Scatter(
            x=[x_split],
            y=[y_split],
            mode="markers",
            name="transition point",
            marker=dict(size=10, color="red", symbol="circle"),
        )
    )

    # Layout customization
    fig.update_layout(
        title="Piecewise Function Visualization",
        xaxis_title="x",
        yaxis_title="f(x)",
        showlegend=True,
        template="plotly_white",
    )

    fig.show()
    return


@app.cell
def _(mo):
    mo.md(r"""### Example 2""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    The step function is defined to be $f(x) = \lfloor x \rfloor$ which denote the largest integer smaller than or equals to $x$. For example, $\lfloor 2 \rfloor = 2$, $\lfloor 2.5 \rfloor = 2$, and $\lfloor -2.3 \rfloor = -3$.

    The step function does not have limit at all integers. For example, $\lim\limits_{x\to2^-}f(x) = 2$ but $\lim\limits_{x \to 2^+}f(x) = 3$, thus $\lim\limits_{x\to 2} f(x)$ does not exist.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Lemma""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""Suppose $f(x) \le g(x)$ when $x$ is near $a$ (except possibly at $a$), and both $\lim\limits_{x\to a}f(x)$, $\lim\limits_{x\to a}g(x)$ exist, then $\lim\limits_{x\to a}f(x) \le \lim\limits_{x\to a}g(x)$."""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Squeeze Theorem""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""Suppose $f(x) \le g(x) \le h(x)$ when $x$ is near $a$ (except possibly at $a$), and $\lim\limits_{x\to a}f(x) = \lim\limits_{x \to a}h(x) = L$, then we also have $\lim\limits_{x \to a}g(x) = L$."""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Example (Squeeze Theorem)""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Evaluate $\displaystyle \lim\limits_{x\to 0}x^2\cdot\sin(\frac{1}{x})$.

    As we known from last lecture, $\displaystyle \lim\limits_{x\to 0}\sin(\frac{1}{x})$ does not exist, so we cannot just calculate the limits for two parts and multiply them together. We use the Squeeze Theorem.

    Notice that $\displaystyle -1 \le \sin(\frac{1}{x}) \le 1$, thus we have $\displaystyle -x^2 \le x^2\cdot\sin(\frac{1}{x}) \le x^2$. Now we know that $\lim\limits_{x\to 0}-x^2 = 0$ and $\lim\limits_{x\to 0}x^2 = 0$ (using rule 9.), thus by the Squeeze Theorem, we have $\displaystyle \lim\limits_{x\to 0}x^2\cdot\sin(\frac{1}{x}) = 0$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## An Important Limit""")
    return


@app.cell
def _(mo):
    mo.md(r"""$$\boxed{\lim\limits_{x\to 0}\frac{\sin(x)}{x} = 1}.$$""")
    return


@app.cell
def _(go, np):
    # Angle x (sample: pi/5)
    x_angle = np.pi / 5
    x_point = np.cos(x_angle)
    y_point = np.sin(x_angle)

    # Unit circle first quadrant
    theta_circle = np.linspace(0, np.pi / 2, 400)
    x_circle = np.cos(theta_circle)
    y_circle = np.sin(theta_circle)

    # Sector arc (0 to x)
    theta_arc = np.linspace(0, x_angle, 100)
    x_arc = np.cos(theta_arc)
    y_arc = np.sin(theta_arc)

    # Tangent line at (cos(x), sin(x))
    slope_tangent = -np.cos(x_angle) / np.sin(x_angle)
    x_tangent_range = np.linspace(x_point, x_point + 0.4254, 50)
    y_tangent = slope_tangent * (x_tangent_range - x_point) + y_point

    # Create figure
    fig_circle = go.Figure()

    # Sector arc
    fig_circle.add_trace(
        go.Scatter(
            x=x_arc,
            y=y_arc,
            mode="lines",
            line=dict(color="blue"),
            name="Sector Arc",
            showlegend=False,
        )
    )

    fig_circle.add_trace(
        go.Scatter(
            x=x_arc * 0.1,
            y=y_arc * 0.1,
            mode="lines",
            line=dict(color="grey"),
            name="Sector Arc",
            showlegend=False,
        )
    )

    # Angle arm
    fig_circle.add_trace(
        go.Scatter(
            x=[0, x_point],
            y=[0, y_point],
            mode="lines",
            line=dict(color="black"),
            showlegend=False,
        )
    )

    # sin(x) projection
    fig_circle.add_trace(
        go.Scatter(
            x=[x_point, x_point],
            y=[0, y_point],
            mode="lines",
            line=dict(color="red", dash="dot"),
            showlegend=False,
        )
    )

    # Tangent line at point (cos(x), sin(x))
    fig_circle.add_trace(
        go.Scatter(
            x=x_tangent_range,
            y=y_tangent,
            mode="lines",
            line=dict(color="green"),
            name="Tangent at x",
            showlegend=False,
        )
    )

    # θ label
    fig_circle.add_trace(
        go.Scatter(
            x=[0.15 * np.cos(x_angle / 2)],
            y=[0.15 * np.sin(x_angle / 2)],
            mode="text",
            text=["x"],
            textfont=dict(size=14),
            showlegend=False,
        )
    )

    # sin(x) label
    fig_circle.add_trace(
        go.Scatter(
            x=[0.7],
            y=[0.3],
            mode="text",
            text=["sin(x)"],
            textfont=dict(size=14, color="red"),
            showlegend=False,
        )
    )

    # Arc length label
    fig_circle.add_trace(
        go.Scatter(
            x=[x_arc[-1] + 0.05],
            y=[y_arc[-1] + 0.05],
            mode="text",
            text=["Arc Length = x"],
            textfont=dict(size=14, color="blue"),
            showlegend=False,
        )
    )

    fig_circle.add_trace(
        go.Scatter(
            x=[0.4],
            y=[0.34],
            mode="text",
            text=["1"],
            textfont=dict(size=14, color="black"),
            showlegend=False,
        )
    )

    # tan(x) label (on tangent line)
    fig_circle.add_trace(
        go.Scatter(
            x=[1.1],
            y=[0.3],
            mode="text",
            text=["tan(x)"],
            textfont=dict(size=14, color="green"),
            showlegend=False,
        )
    )

    # X and Y axes
    fig_circle.add_trace(
        go.Scatter(
            x=[-0.1, 1.4],
            y=[0, 0],
            mode="lines",
            line=dict(color="black", width=1),
            showlegend=False,
        )
    )

    fig_circle.add_trace(
        go.Scatter(
            x=[0, 0],
            y=[-0.1, 0.6],
            mode="lines",
            line=dict(color="black", width=1),
            showlegend=False,
        )
    )

    # Layout
    fig_circle.update_layout(
        title="First Quadrant: Unit Circle with sin(x), arc length x, and tan(x)",
        xaxis=dict(scaleanchor="y", range=[-0.1, 1.3], showgrid=False, zeroline=False),
        yaxis=dict(scaleanchor="x", range=[-0.1, 0.6], showgrid=False, zeroline=False),
        template="plotly_white",
        showlegend=False,
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    From the picture we can see when $x$ is small and greater than $0$, we have $\sin(x) < x < \tan(x)$, do some algebra we have:

    1. $\displaystyle \frac{\sin(x)}{x}<1$;
    2. $\displaystyle 1 < \frac{\tan(x)}{x} = \frac{\sin(x)}{\cos(x)\cdot x}$ $\displaystyle \implies \cos(x)< \frac{\sin(x)}{x}$.

    The Squeeze Theorem applies because $\lim\limits_{x\to 0}\cos(x) = 1$ (rule 9.), and we have $\displaystyle \lim\limits_{x\to 0^+}\frac{\sin(x)}{x} = 1$. For $x < 0$, remember sine is an odd function so we have $\displaystyle \frac{\sin(x)}{x} = \frac{\sin(-x)}{-x}$ so we have the same result.
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
    Evaluate $\displaystyle \lim\limits_{x\to 0}\frac{\sin(5x)}{2x}$.

    At a first glance, the answer might appear to be $1$ as a direct result of the above equality - this is **not correct**. The above equality in particular says that the limit of $\sin(\text{an expression})$ divided by **the same expression** as that expression goes to $0$, is $1$. In this example, the denominator appears to be $2x$ but the top has $\sin(5x)$ instead of $2x$, thus we need some extra effort.

    $\displaystyle \lim\limits_{x\to 0}\frac{\sin(5x)}{2x}$ $\displaystyle =\lim\limits_{x\to 0}\frac{\sin(5x)}{2x}\cdot\frac{5}{5}$ $\displaystyle =\lim\limits_{x\to 0}\frac{\sin(5x)}{5x} \cdot \frac{5}{2}$ $\displaystyle =1 \cdot \frac{5}{2}= \frac{5}{2}$. We create a quotient that is indeed $\sin(\text{an expression})$ divided by **the same expression**, also notice $5x$ indeed goes to $0$ if $x$ itself goes to $0$.
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
    Now we know $\displaystyle \lim\limits_{x\to 0}\frac{\sin(x)}{x} = 1$, what about $\displaystyle \lim\limits_{x\to 0}\frac{x}{\sin(x)}$?

    Simply apply rule 4. And 8.: $\displaystyle \lim\limits_{x\to 0}\frac{x}{\sin(x)}$ $\displaystyle = \lim\limits_{x\to 0}\frac{1}{\frac{\sin(x)}{x}}$ $\displaystyle = \frac{\lim\limits_{x\to 0}1}{\lim\limits_{x\to 0}\frac{\sin(x)}{x}}$ $\displaystyle = \frac{1}{1} = 1$ as well.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Summary: Typical Methods to Evaluate a Limit""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    1. Try first if the limit is of an indeterminant form or not, if it is not, you can simply plug in value to get result. Otherwise:
    2. If there is absolute value function involved, you should try to evaluate the limit from left and right separately;
    3. If there are trigonometry functions involved, you should try to use Squeeze Theorem or rewrite the function in terms of $\sin(\cdot)$ and apply the important limit;
    4. Otherwise, you should try to simplify the expression and try to get rid of the indeterminant form. Typical methods include combining fractions, and multiply/quotient by conjugate (useful when a square root function, or $1 \pm \cos(\cdot)$ is involved).

    Of course, these are not all possible methods to evaluate an arbitrary limit. Practice more and see what else can happen!
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Another Important Limit""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    $$\lim\limits_{x\to 0}\frac{\cos(x) - 1}{x} = 0.$$

    This can be derived using the important limit above. The proof is left as an exercise.
    """
    )
    return


if __name__ == "__main__":
    app.run()
