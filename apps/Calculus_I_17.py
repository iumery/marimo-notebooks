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
    mo.md(r"""# 3.4 Curve Sketching""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Motivation""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    In this section we will apply what we have learnt before (section 3.1 and 3.3) to graph a function. Before we get started, let us think about the question: why should we learn to graph a function, when there are graphic calculators out there?

    The book gives an one-line answer to the question - "**but even the best graphing devices have to be used intelligently**". That is pretty much the gist, but let us be a bit more specific.

    First, let us talk only about curve sketching. There are several (potential) problems with graphic calculators:

    1. **Resolution**: for most images, resolution is a limitation. An image in 800x600 shows much less details than an image in 3840x2160. Curve width is also a limitation. A line should not have width but we have to plot it with certain width on the graph to actually see it;
    2. **Domain and Range**: when you ask a graphic calculator to graph a function, many of them can automatically adjust the domain and range of the function to be displayed. But this may lead to some problems. Take the example in the book, if you graph $f(x) = 2x^6 + 3x^5 + 3x^3 - 2x^2$, some calculators may automatically adjust the range to $-1000$ to $41000$ and thus 'hide' the detail;
    3. **Algorithm**: some of the calculators are designed 'poorly', some of the calculators may not interpret your input correctly, some of the calculators have different assumptions of your input (but you may not know it without reading the instruction). For example, if you ask WolframAlpha to graph the cubic root of $x-2$, i.e. $(x-2)^{1/3}$, it will give you:
    	<img src="public/iShot_2025-05-11_10.14.31.png" width="400" />
    	Which you may think is wrong. For example, there should be a point corresponds to $x = 1$: if $x = 1$, then $x-2 = -1$, and we can take the cubic root of $-1$ and get $-1$. **WolframAlpha does have its reason to not graph it** - it involves some more advanced stuffs involving complex analysis (the study of complex numbers and complex valued functions), called the 'principal branch'. Technically WolframAlpha is **not wrong**, but its graph is indeed incomplete in the **real number setting**.
    	Desmos, for example, is a calculator that can handle this in a 'correct' manner. **But how can you be sure that it won't handle other functions wrongly**?
    	<img src="public/iShot_2025-05-11_10.12.56.png" width="600" />

    In general, there are (potential) problems that you may face *whenever* you use technology:

    1. **Hardware limitation**: your computer is not powerful enough, your screen is not large enough, etc. Usually in practice this is not a big problem, in the sense that it is easy to tell when this happens (then just ask your company/department to get a better machine for you);
    2. **Software limitation**: the assumptions of the algorithm are not consistent with your setting; the algorithm has a glitch; the algorithm is badly designed, etc. This could be a big problem because this could be hidden. **You need to indeed 'understand what you are doing' to realize there is something wrong**.

    So back to our topic, we need to learn curve sketching to really understand what is going on. It may help us to interpret the graphic calculator, and more important, to realize the graphic calculator makes a mistake when it does.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Guideline for Sketching A Curve""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    To do a detailed graphing, we use the following guideline. Not every item is relevant to every function, but it is good to check all of them.

    1. **Domain**: where is the function defined?
    2. **Axis-Intersections**: where does the graph intersects with the $x$-axis and where does the graph intersects with the $y$-axis? To find the $x$-intercepts, we set $f(x) = 0$ and solve for $x$; to find $y$-intercept, we evaluate $f(0)$. Remember that by definition of a function, there can be only one $y$-intercept, but there can be more than one $x$-intercepts;
    3. **Symmetry and Period**: is the function a(n):
    	1. Odd function? That is, for any $x$ in the domain, we have $f(x) = -f(-x)$. Typical odd functions are $\sin(x)$, $x$, $x^3$ (power is odd number). If the function is odd, we can plot the part that $x \le 0$ or $x \ge 0$, rotate $180$ degree to get the full graph;
    	2. Even function? That is, for any $x$ in the domain, we have $f(x) = f(-x)$. Typical even functions are $\cos(x)$, $x^2$, $x^4$ (power is even number). If the function is even, we can plot the part that $x \le 0$ or $x \ge 0$, flip along $y$-axis to get the full graph.
    	Is the function periodic? That is, if $f(x) = f(x+p)$ for all $x$ in the domain and a certain constant $p$. Typical periodic functions are the trigonometry functions. If the function is periodic, we can plot one period and copy it to get the full graph.
    	Notice that a function can be periodic and even ($\cos(x)$), or periodic and odd ($\sin(x)$)at the same time.
    	In the scope of this course, it is safe to say that **trigonometry functions (and functions composed with trigonometry functions) are the only interesting periodic functions**. Constant function is of course also periodic, but it is not very interesting;
    4. **Asymptotes**:
    	1. If $\lim_{x \to \infty}f(x) = L$ or $\lim_{x\to -\infty}f(x) = l$, then $y = L$ or $y = l$ is a horizontal asymptote. If $\lim_{x \to \infty}f(x) = \pm \infty$ or $\lim_{x\to -\infty}f(x) = \pm \infty$ then it does not give a horizontal asymptote, but it also gives important information as that, for example, if $\lim_{x \to \infty}f(x) = \infty$ then you may think of it as $f$ passes the point 'that is on the right-top corner';
    	2. If any of $\lim_{x \to a^-}f(x) = \infty$, $\lim_{x \to a^+}f(x) = \infty$, $\lim_{x \to a^-}f(x) = -\infty$, $\lim_{x \to a^+}f(x) = -\infty$ is true for certain $a$, then $x = a$ is a vertical asymptote. If the function is a rational function, then the vertical asymptote happens when the denominator is $0$;
    5. **Intervals of Increase or Decrease**: use the increasing/decreasing test we have in section 3.3 to determine where is $f$ increasing or decreasing;
    6. **Local Extremums**: use the methods (First or Second Derivative Tests) we have in section 3.3 to determine where are the local extremums and what are the values;
    7. **Concavity and Points of Inflection**: use Concavity Test to determine the concavity and points of inflection;
    8. Sketch the Curve:
    	1. Sketch the asymptotes as dashed lines;
    	2. Plot the $x$ and $y$-intercepts;
    	3. Plot the local extremums (whenever it is local maximum, you can plot a little '$\cap$', and whenever it is local minimum, you can plot a little '$\cup$', except for the endpoints);
    	4. Plot the inflection points;
    	5. Comment on the $x$-axis the intervals of increasing/decreasing and concavity;
    	6. Draw the curve, make sure that it passes all the points you plotted, and it is consistent with the increasing/decreasing/concave downward/concave upward information;
    	7. (If you want to be more confident about the shape - it is never harmful to evaluate $f(x)$ at a few more points and plot it on the graph, the curve then also needs to pass these points)
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    /// admonition | Increasing/Decreasing and Concavity
        type: info

    There are four possible shapes of a graph considering concavity and increasing/decreasing info:

    ///
    """
    )
    return


@app.cell
def _(go, make_subplots, np):
    # Define x range and functions
    x_vals_side = np.linspace(-3, 3, 400)
    y_up = x_vals_side**2
    y_down = -(x_vals_side**2)

    # Create subplots
    fig_side = make_subplots(rows=2, cols=1, subplot_titles=["f(x) = x²", "f(x) = -x²"])

    # --- Plot x^2
    fig_side.add_trace(
        go.Scatter(
            x=x_vals_side, y=y_up, mode="lines", name="x²", line=dict(color="blue")
        ),
        row=1,
        col=1,
    )

    # Label left half: Concave up & Decreasing
    fig_side.add_trace(
        go.Scatter(
            x=[-2],
            y=[4],
            mode="text",
            text=["Concave Up<br>Decreasing"],
            textposition="bottom center",
            showlegend=False,
        ),
        row=1,
        col=1,
    )

    # Label right half: Concave up & Increasing
    fig_side.add_trace(
        go.Scatter(
            x=[2],
            y=[4],
            mode="text",
            text=["Concave Up<br>Increasing"],
            textposition="bottom center",
            showlegend=False,
        ),
        row=1,
        col=1,
    )

    # --- Plot -x^2
    fig_side.add_trace(
        go.Scatter(
            x=x_vals_side, y=y_down, mode="lines", name="-x²", line=dict(color="red")
        ),
        row=2,
        col=1,
    )

    # Label left half: Concave Down & Increasing
    fig_side.add_trace(
        go.Scatter(
            x=[-2],
            y=[-4],
            mode="text",
            text=["Concave Down<br>Increasing"],
            textposition="top center",
            showlegend=False,
        ),
        row=2,
        col=1,
    )

    # Label right half: Concave Down & Decreasing
    fig_side.add_trace(
        go.Scatter(
            x=[2],
            y=[-4],
            mode="text",
            text=["Concave Down<br>Decreasing"],
            textposition="top center",
            showlegend=False,
        ),
        row=2,
        col=1,
    )

    # Layout
    fig_side.update_layout(
        title="Concavity and Monotonicity of f(x) = x² vs f(x) = -x²",
        template="plotly_white",
        height=800,
        width=600,
    )

    # Axis titles
    fig_side.update_xaxes(title_text="x", row=1, col=1)
    fig_side.update_yaxes(title_text="f(x)", row=1, col=1)
    fig_side.update_xaxes(title_text="x", row=1, col=2)
    fig_side.update_yaxes(title_text="f(x)", row=1, col=2)
    return


@app.cell
def _(mo):
    mo.md(r"""### Example""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Let us do the detailed graphing for the example in section 3.3. I.e. the function $f(x) = (x-1)^{1/3}(x+1)$. We follow the guideline.

    1. Domain: $f(x)$ is defined for any $x \in \mathbb{R}$, thus the domain is the entire real line;
    2. Intercepts: evaluate $f(0) = -1$, thus the $y$-intercept is at $(0,-1)$; set $f(x) = 0$, we get $0 = (x-1)^{1/3}(x+1)$, since it is factored for us, we get that $x = 1$ or $x = -1$, so the $x$-intercepts are at $(1, 0)$ and $(-1, 0)$;
    3. Symmetry and Period:
    	1. $f(-x) = (-x-1)^{1/3}(-x+1)$ is not the same as $f(x) = (x-1)^{1/3}(x+1)$, so the function is not even;
    	2. Similarly $-f(-x) \ne f(x)$ thus the function is not odd;
    	3. The function is not periodic because it is not trigonometry functions and it is not constant;
    4. Asymptotes:
    	1. Evaluate the limits we get $\lim_{x\to \infty}f(x) = \infty$ and $\lim_{x \to -\infty}f(x) = \infty$ thus we can think of $f$ passes the left-top corner and right-top corner;
    	2. There is no vertical asymptotes;
    5. Intervals of Increase or Decrease: by section 3.3, we get $f$ is decreasing on $x<\frac{1}{2}$ and increasing on $x > \frac{1}{2}$;
    6. Local Extremum: we have a local minimum at $\frac{1}{2}$, evaluate $f(\frac{1}{2}) \approx -1.2$ (note that it is not very easy to evaluate $(-\frac{1}{2})^{1/3}$, just give a reasonable guess if it is on the exam);
    7. Concavity and Points of Inflection: the graph is concave upward on $(-\infty, 1)$ and $(2, \infty)$; concave downward on $(1,2)$; with inflection points on $(1,0)$ and $(2,3)$;
    8. Now we do the plot:
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    <img src="public/Pasted image 20230813095937.png"/>
    <img src="public/Pasted image 20230813100003.png"/>
    <img src="public/Pasted image 20230813100104.png"/>
    """
    )
    return


if __name__ == "__main__":
    app.run()
