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
    mo.md(r"""# 3.5 Optimization Problems""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Introduction""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    In mathematics, an optimization problem is a problem to find the best solution(s) from all **feasible** solutions.

    Optimization plays crucial roles in many fields, including the hottest topics today, machine learning and AI. There are a lot of typical optimization problems. A big category is to find the largest or smallest value. For example:

    1. The traveling-businessman problem: a businessman need to travel to $5$ (or any number greater than $1$) cities and go back home, the order of visit does not matter, what should be the order if he want to have the shortest distance traveled?
    2. Marginal profit problem: how many product should a company produce to maximize profit?
    3. Portfolio risk management: how should a hedge-fund manager allocate the fund to maximize return-to-risk ratio?
    4. Package design problem: how to design the package so that the material usage is the lowest and easy to be transported?

    There are also optimization problem of optimization problem. An rather 'easy' way to solve an optimization problem is to list *all* feasible solutions and find the best solution among them, but this usually takes a *very* long time. How do we acceleration this process? This is a very hot topic right now because it has very important application in the field of machine learning and AI.

    There are tons of methods to solve optimization problems. Some of them can be solved purely algebraically. Some of them need more complicated methods (if you are interested in it, you can google keywords like 'linear programming', 'quadratic programming', or 'dynamic programming').

    In the scope of this course, **we mainly study optimization problems that can be described by a function, and we find the maximum and minimum value using the method we had in section 3.1**.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Strategy of Solve Optimization Problem""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Like related rates problem in section 2.7, optimization problems are often described as a word problem. As a result, we need to interpret a problem before doing it. To solve an optimization problem, we can follow the guideline from the book:

    1. Understand the Problem: The first step is to read the problem carefully until it is clearly understood. Ask yourself: What is the unknown? What are the given quantities? What are the given conditions?
    2. Draw a Diagram: In most problems it is useful to draw a diagram and identify the given and required quantities on the diagram;
    3. Introduce Notation: Assign a symbol to the quantity that is to be maximized or minimized (let's call it $Q$ for now). Also select symbols $a, b, c, \dots, x, y$ for other unknown quantities and label the diagram with these symbols. It may help to use initials as suggestive symbols — for example, $A$ for area, $h$ for height, $t$ for time;
    4. Express $Q$ in terms of some of the other symbols from Step 3;
    5. If $Q$ has been expressed as a function of more than one variable in Step 4, use the given information to find relationships (in the form of equations) among these variables. Then use these equations to eliminate all but one of the variables in the expression for $Q$. So that $Q$ is expressed as a function of **one** variable $x$, say, $Q = f(x)$. Write the domain of this function;
    6. Use the methods of Sections 3.1 and 3.3 to find the maximum or minimum value of $f$. In particular, if the domain of $f$ is a closed interval, then the Closed Interval Method in Section 3.1 can be used. If domain of $f$ is an open interval, you can use 3.3 to verify if it is a local minimum or maximum (and it automatically comes absolute extremum).
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Example 1""")
    return


@app.cell
def _(mo):
    mo.md(r"""A company needs to produce a container of cylindrical shape to hold $1 \text{ L}$ (or $1000 \text{ cm}^3$) of liquid. Find the dimension of the container that minimize the material usage.""")
    return


@app.cell
def _(mo, np):
    r_slider = mo.ui.slider(
        steps=np.linspace(4, 8, 10001),
        label="Radius of the Cylinder",
        value=4,
    )
    r_slider
    return (r_slider,)


app._unparsable_cell(
    r"""
    Try it youself using the above slidebar!
    """,
    name="_"
)


@app.cell
def _(go, np, r_slider):
    # Compute height using volume constraint
    h_input = 1000 / (np.pi * r_slider.value**2)

    cylinder_area = 2 * np.pi * r_slider.value**2 + 2 * np.pi * r_slider.value * h_input

    # Create cylinder surface
    theta = np.linspace(0, 2 * np.pi, 100)
    z = np.linspace(0, h_input, 50)
    theta_grid, z_grid = np.meshgrid(theta, z)
    x_cyl = r_slider.value * np.cos(theta_grid)
    y_cyl = r_slider.value * np.sin(theta_grid)
    z_cyl = z_grid

    # Create 3D surface plot
    fig_cyl = go.Figure(data=[
        go.Surface(x=x_cyl, y=y_cyl, z=z_cyl, colorscale='Blues', showscale=False, opacity=0.8)
    ])

    # Adjust camera to improve visibility
    camera_config = dict(
        eye=dict(x=0., y=2.5, z=0.1)
    )

    # Layout
    fig_cyl.update_layout(
        title=f"Cylinder with radius r ≈ {r_slider.value:.2f} cm<br>" \
          f"height h ≈ {h_input:.2f} cm<br>" \
          f"surface area A ≈ {cylinder_area:.2f} cm²",
        scene=dict(
            xaxis_title='x (cm)',
            yaxis_title='y (cm)',
            zaxis_title='height (cm)',
            aspectmode='data',
            camera=camera_config
        ),
        template='plotly_white'
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Solution:

    Suppose we have a cylindrical container with height $h$ and radius $r$, then the volume of the container is $\pi r^2 h$, we want it to be $1000$. On the other hand, to produce such a cylindrical container we need two disks, and a rectangle shape of material.

    The disks have radius $r$, so we need $2 \pi r^2$ (unit in squared centimeter) of material to produce them; the rectangle has length $2\pi r$ (the perimeter of the disk) and width $h$, so we need $2\pi r h$ (unit in squared centimeter) of material to produce it.

    Thus the material usage is $A = 2\pi r^2 + 2\pi r h$. There are three quantities, and we want to minimize $A$ that depends on two quantities. We need to reduce the number of quantities using the relation between them.

    Since we have $\pi r^2 h = 1000$, we can rewrite $h = 1000/(\pi r^2)$. Substitute it to $A$, we get $$A = 2 \pi r^2 + 2\pi r \frac{1000}{\pi r^2} = 2\pi r^2 + \frac{2000}{r}.$$ Now we take the derivative of $A$ with respect to $r$ to find the critical number. We have $\displaystyle A' = 4\pi r - \frac{2000}{r^2}$ $\displaystyle = \frac{4(\pi r^3 -500)}{r^2}$, thus $A' = 0$ when $r = \sqrt[3]{500/\pi}$.

    Observe that if $r < \sqrt[3]{500/\pi}$, then $A'(r)<0$ and if $r > \sqrt[3]{500/\pi}$, then $A'(r) > 0$. Thus by the First Derivative Test, $A$ at $\sqrt[3]{500/\pi}$ is a local minimum. In fact, it is the absolute minimum.

    We can then calculate $h$ corresponds to this $r$, that is $\displaystyle h = \frac{1000}{\pi r^2} = \frac{1000}{\pi(500/\pi)^{2/3}}$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Example 2""")
    return


@app.cell
def _(mo):
    mo.md(r"""There are $50$ apple trees in an orchard and each of them are producing $800$ apples. For each additional tree planted in the orchard, the output of each tree drops by $10$ apples. How many trees should be added to the existing orchard to maximize the total output?""")
    return


@app.cell
def _(mo):
    n_trees = mo.ui.slider(0, 80, value=0, label="Number of Trees to Plant")
    n_trees
    return (n_trees,)


@app.cell
def _(mo, n_trees):
    total_output = (50 + n_trees.value) * (800 - 10 * n_trees.value)
    mo.md(
        f"""
        Try it youself using the above slidebar!

        If we plant {n_trees.value} new trees, total output is going to be (50 + {n_trees.value}) x (800 - 10 x {n_trees.value}) = {total_output}.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Solution: 

    Suppose we add $x$ apple trees, then there are $50+x$ trees and the output per tree becomes $800 - 10x$, thus the total output is $(50+x)(800 - 10x) = O$. Take derivative with respect to $x$, we get $O' = 300 - 20x$, it is $0$ when $x = 15$. It is easy to see that when $x<15$, $O'>0$, and when $x > 15$, $O'<0$, so this is the absolute maximum. Thus we should plant $15$ more trees.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Example 3""")
    return


@app.cell
def _(mo):
    mo.md(r"""Find the area of the largest rectangle that can be inscribed inside the ellipse $\displaystyle \frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ for arbitrary positive constant $a, b$.""")
    return


@app.cell
def _(mo, np):
    x_slider = mo.ui.slider(
        steps=np.linspace(0, 5, 10001),
        label="x Coordinate of the top-right vertice",
        value=0,
    )
    x_slider
    return (x_slider,)


@app.cell
def _(mo):
    mo.md(f"""Try it youself using the above slidebar!""")
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
    mo.md(r"""What is the minimum vertical distance between the parabolas $y = x^2 + 1$ and $y = x - x^2$?""")
    return


@app.cell
def _(mo, np):
    x_slider_1 = mo.ui.slider(
        steps=np.linspace(-1, 1, 10001),
        label="x Coordinate of the point",
        value=-1,
    )
    x_slider_1
    return (x_slider_1,)


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
    fig_dist.add_trace(go.Scatter(
        x=x_vals_d, y=y_f_vals,
        mode='lines',
        name='f(x) = x² + 1',
        line=dict(color='blue')
    ))
    fig_dist.add_trace(go.Scatter(
        x=x_vals_d, y=y_g_vals,
        mode='lines',
        name='g(x) = x - x²',
        line=dict(color='green')
    ))

    # Vertical segment from g(x) to f(x)
    fig_dist.add_trace(go.Scatter(
        x=[x_point, x_point],
        y=[y_bot, y_top],
        mode='lines+text',
        line=dict(color='red', width=3, dash='dash'),
        text=[f"{delta_y:.2f}"],
        textposition='bottom right',
        textfont=dict(size=14, color='red'),
        name='Vertical Distance',
        showlegend=False
    ))

    # Layout
    fig_dist.update_layout(
        title='Vertical Distance Between f(x) and g(x) at x = {:.2f}'.format(x_point),
        xaxis_title='x',
        yaxis_title='y',
        template='plotly_white',
        xaxis=dict(range=[-2, 2]),
        yaxis=dict(range=[-4, 4])
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


@app.cell
def _(mo):
    mo.md(r"""### Example 5""")
    return


@app.cell
def _(mo):
    mo.md(r"""Find the points on the ellipse $4x^2 + y^2 = 4$ that are farthest away from the point $(2,0)$.""")
    return


@app.cell
def _(mo, np):
    y_slider = mo.ui.slider(
        steps=np.linspace(-2, 2, 10001),
        label="y Coordinate of the point",
        value=0,
    )
    y_slider
    return (y_slider,)


@app.cell
def _(go, np, y_slider):
    # Ellipse: 4x^2 + y^2 = 4 → y in [-2, 2]
    y_vals_l = np.linspace(-2, 2, 400)
    x_right_l = np.sqrt((4 - y_vals_l**2) / 4)
    x_left_l = -x_right_l

    # Given y from slider
    y_given_l = y_slider.value  # ← your slider value
    x_on_ellipse_l = -np.sqrt((4 - y_given_l**2) / 4)
    point_on_ellipse_l = (x_on_ellipse_l, y_given_l)

    # Segment from (1, 0) to point on ellipse
    x1_l, y1_l = 2, 0
    x2_l, y2_l = point_on_ellipse_l
    segment_len_l = np.sqrt((x2_l - x1_l)**2 + (y2_l - y1_l)**2)

    # Create figure
    fig_l = go.Figure()

    # Plot full ellipse
    fig_l.add_trace(go.Scatter(
        x=np.concatenate([x_left_l, x_right_l[::-1]]),
        y=np.concatenate([y_vals_l, y_vals_l[::-1]]),
        fill='toself',
        fillcolor='rgba(173, 216, 230, 0.3)',
        line=dict(color='blue'),
        name='Ellipse'
    ))

    # Plot point on left half
    fig_l.add_trace(go.Scatter(
        x=[x2_l], y=[y2_l],
        mode='markers+text',
        marker=dict(size=8, color='red'),
        text=[f"({x2_l:.2f}, {y2_l:.2f})"],
        textposition='top left',
        name='Point on ellipse'
    ))

    fig_l.add_trace(go.Scatter(
        x=[x1_l], y=[y1_l],
        mode='markers+text',
        marker=dict(size=8, color='red'),
        text=[f"({x1_l:.0f}, {y1_l:.0f})"],
        textposition='top left',
        name='Point on ellipse'
    ))

    # Segment from (1, 0) to that point
    fig_l.add_trace(go.Scatter(
        x=[x1_l, x2_l],
        y=[y1_l, y2_l],
        mode='lines+text',
        line=dict(color='green', dash='dash'),
        text=[None, f"Length ≈ {segment_len_l:.2f}"],
        textposition='bottom right',
        showlegend=False
    ))

    # Layout
    fig_l.update_layout(
        title='Segment from (2, 0) to a Point on Left Half of Ellipse',
        xaxis_title='x',
        yaxis_title='y',
        template='plotly_white',
        xaxis=dict(scaleanchor="y",range=[-2.5, 2]),
        yaxis=dict(scaleanchor="x",range=[-2.5, 2.5]),
        showlegend=False
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Solution Sketch:

    Since we are looking for point farthest away from $(2, 0)$, a point on the right half of the $xy$-plane, we can safely ignore points on the right half of the ellipse since they are always going to be closer to $(2, 0)$ compare to their mirrored point on the left half.

    Suppose the point has $y$-coordinate being $y$, since it is on the ellipse, its coordinate satisfies $4x^2 + y^2 = 4$, which means $4x^2 = 4 - y^2$ thus $x = - \sqrt{1 - \frac{1}{4}y^2}$ (**why there's a minus on the front?**).

    Distance between two points $(x_1, y_1)$ and $(x_2, y_2)$ is $d = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$. To make our calculation simpler, we can consider $d^2$ which takes out the square-root (**why can we do this?**).

    In particular, $d^2 = \left(- \sqrt{1 - \frac{1}{4}y^2} - 2\right)^2 + (y - 0)^2$. Simplify this expression, proceed to take derivative to find critical point(s) and find (absolute) maximum(s).
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Example 6""")
    return


@app.cell
def _(mo):
    mo.md(r"""Find the area of the largest trapezoid that can be inscribed in a circle of radius $1$ and whose base is a diameter of the circle.""")
    return


@app.cell
def _(mo, np):
    x_slider_2 = mo.ui.slider(
        steps=np.linspace(0, 1, 10001),
        label="x Coordinate of the top-right vertice of the trapezoid",
        value=0,
    )
    x_slider_2
    return (x_slider_2,)


@app.cell
def _(go, np, x_slider_2):
    # Unit circle upper half
    x_vals_u = np.linspace(-1, 1, 400)
    y_vals_u = np.sqrt(1 - x_vals_u**2)

    # Slider input
    x0_trap = x_slider_2.value  # <-- your slider value in [0, 1]
    y0_trap = np.sqrt(1 - x0_trap**2)

    # Trapezoid vertices (clockwise)
    x_trap = [-1, 1, x0_trap, -x0_trap, -1]
    y_trap = [0, 0, y0_trap, y0_trap, 0]

    # Area of trapezoid
    trap_area = (1 + x0_trap) * y0_trap

    # Create figure
    fig_trapezoid = go.Figure()

    # Plot upper unit circle
    fig_trapezoid.add_trace(go.Scatter(
        x=x_vals_u, y=y_vals_u,
        mode='lines',
        name='Upper Unit Circle',
        line=dict(color='blue')
    ))

    # Plot trapezoid fill
    fig_trapezoid.add_trace(go.Scatter(
        x=x_trap,
        y=y_trap,
        fill='toself',
        fillcolor='rgba(255, 0, 0, 0.3)',
        line=dict(width=0),
        name='Trapezoid',
        showlegend=False
    ))

    # Label area
    fig_trapezoid.add_trace(go.Scatter(
        x=[0],
        y=[y0_trap / 2],
        mode='text',
        text=[f"Area ≈ {trap_area:.3f}"],
        textfont=dict(size=16, color='darkred'),
        showlegend=False
    ))

    # Layout
    fig_trapezoid.update_layout(
        title='Trapezoid Inscribed in the Unit Circle',
        xaxis_title='x',
        yaxis_title='y',
        xaxis=dict(scaleanchor="y", range=[-1.2, 1.2]),
        yaxis=dict(scaleanchor="x", range=[-0.1, 1.1]),
        template='plotly_white'
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Solution Sketch:

    A trapezoid has area (top-base + bottom-base) x height / 2. In particular, if the top-right corner of the trapezoid has coordinate $(x, y)$, then we have $A = (2x + 2) \times y / 2 = (x + 1) \times y$. Since $(x, y)$ is also on the unit circle, we can express $y = \sqrt{1-x^2}$ thus $A = (x+1)\cdot \sqrt{1 - x^2}$. Proceed to take derivative to find critical point(s) and find (absolute) maximum(s).
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Example 6.1""")
    return


@app.cell
def _(mo, np):
    theta_slider = mo.ui.slider(
        steps=np.linspace(0, np.pi/2, 10001),
        label="Angle between the top-right vertice of the trapezoid and the x-axis",
        value=0,
    )
    theta_slider
    return (theta_slider,)


@app.cell
def _(go, np, theta_slider):
    # Upper half of unit circle
    x_unit = np.linspace(-1, 1, 400)
    y_unit = np.sqrt(1 - x_unit**2)

    # Angle from slider (in radians)
    theta_angle = theta_slider.value
    x_corner = np.cos(theta_angle)
    y_corner = np.sin(theta_angle)

    # Trapezoid vertices (base [-1,1], top [-cosθ, cosθ])
    x_trap_ang = [-1, 1, x_corner, -x_corner, -1]
    y_trap_ang = [0, 0, y_corner, y_corner, 0]

    # Area of trapezoid
    area_trap_ang = (1 + x_corner) * y_corner

    # Arc for θ label (a small circular arc from (1, 0) to the angle)
    theta_arc = np.linspace(0, theta_angle, 100)
    arc_radius = 0.3
    x_arc = arc_radius * np.cos(theta_arc)
    y_arc = arc_radius * np.sin(theta_arc)

    # Create figure
    fig_ang = go.Figure()

    # Unit circle upper half
    fig_ang.add_trace(go.Scatter(
        x=x_unit,
        y=y_unit,
        mode='lines',
        name='Upper Unit Circle',
        line=dict(color='blue')
    ))

    # Trapezoid region
    fig_ang.add_trace(go.Scatter(
        x=x_trap_ang,
        y=y_trap_ang,
        fill='toself',
        fillcolor='rgba(255, 100, 0, 0.3)',
        line=dict(width=0),
        name='Trapezoid',
        showlegend=False
    ))

    # Segment from (0, 0) to top-right corner
    fig_ang.add_trace(go.Scatter(
        x=[0, x_corner],
        y=[0, y_corner],
        mode='lines',
        line=dict(color='black', dash='dash'),
        name='Angle arm',
        showlegend=False
    ))

    # Arc to show angle θ
    fig_ang.add_trace(go.Scatter(
        x=x_arc,
        y=y_arc,
        mode='lines',
        line=dict(color='gray'),
        showlegend=False
    ))

    # θ label near middle of arc
    arc_label_x = arc_radius * np.cos(theta_angle / 2)
    arc_label_y = arc_radius * np.sin(theta_angle / 2)
    fig_ang.add_trace(go.Scatter(
        x=[arc_label_x],
        y=[arc_label_y],
        mode='text',
        text=["θ"],
        textposition='bottom left',
        textfont=dict(size=16, color='gray'),
        showlegend=False
    ))

    # Area label
    fig_ang.add_trace(go.Scatter(
        x=[0],
        y=[y_corner / 2],
        mode='text',
        text=[f"Area ≈ {area_trap_ang:.3f}"],
        textfont=dict(size=16, color='darkred'),
        showlegend=False
    ))

    # Layout
    fig_ang.update_layout(
        title='Trapezoid under Unit Circle with Angle θ',
        xaxis_title='x',
        yaxis_title='y',
        xaxis=dict(scaleanchor="y", range=[-1.2, 1.2]),
        yaxis=dict(scaleanchor="x", range=[-0.1, 1.1]),
        template='plotly_white'
    )
    return


@app.cell
def _(mo):
    mo.md(r"""Another way of doing this is to utilize trignometry functions. A point on unit circle always can be expressed as $(\cos(\theta), \sin(\theta))$, thus the area can be expressed as $A = (\cos(\theta) + 1)\cdot \sin(\theta)$. Proceed to take derivative to find critical point(s) and find (absolute) maximum(s).""")
    return


@app.cell
def _(mo):
    mo.md(r"""### Example 7""")
    return


@app.cell
def _(mo):
    mo.md(r"""A box with an open top is to be constructed from a square piece of cardboard, $30$ cm wide, by cutting out a square from each of the four corners and bending up the sides. Find the largest volume that such a box can have.""")
    return


@app.cell
def _(mo, np):
    corner_slider = mo.ui.slider(
        steps=np.linspace(1, 15, 10001),
        label="Size of the square cut out",
        value=1,
    )
    corner_slider
    return (corner_slider,)


@app.cell
def _(corner_slider, go):
    # Given corner cut size from slider
    x_cut = corner_slider.value  # must be in (0, 15)

    # Card dimensions
    card_size = 30
    box_height = x_cut
    box_base = card_size - 2 * x_cut
    box_volume = box_height * box_base**2

    # --- 1. 2D Cardboard Layout with Corner Cuts ---

    # Outer square (cardboard)
    card_x = [0, card_size, card_size, 0, 0]
    card_y = [0, 0, card_size, card_size, 0]

    # Corner squares (4 cutouts)
    cut_squares = []
    for dx, dy in [(0, 0), (card_size - x_cut, 0), (card_size - x_cut, card_size - x_cut), (0, card_size - x_cut)]:
        cut_x = [dx, dx + x_cut, dx + x_cut, dx, dx]
        cut_y = [dy, dy, dy + x_cut, dy + x_cut, dy]
        cut_squares.append(go.Scatter(
            x=cut_x,
            y=cut_y,
            fill='toself',
            fillcolor='rgba(150, 150, 150, 0.5)',
            line=dict(color='gray'),
            showlegend=False
        ))

    fig_flat = go.Figure()

    # Cardboard base
    fig_flat.add_trace(go.Scatter(
        x=card_x,
        y=card_y,
        fill='toself',
        fillcolor='white',
        line=dict(color='black'),
        name='Cardboard'
    ))

    # Cutouts
    for square in cut_squares:
        fig_flat.add_trace(square)

    # Label cut size
    fig_flat.add_trace(go.Scatter(
        x=[x_cut / 2], y=[x_cut / 2],
        mode='text',
        text=[f"x = {x_cut:.1f} cm"],
        textfont=dict(size=14),
        showlegend=False
    ))

    # Layout for 2D view
    fig_flat.update_layout(
        title='Cardboard with Corner Cuts (Top View)',
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-2, card_size + 2]),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, scaleanchor='x', range=[-2, card_size + 2]),
        template='plotly_white',
        showlegend=False
    )
    return


@app.cell
def _(corner_slider, go, np):
    # Box dimensions
    x_cut_val = corner_slider.value  # must be in (0, 15)
    card_size_val = 30
    box_base_val = card_size_val - 2 * x_cut_val
    box_height_val = x_cut_val
    box_volume_val = box_height_val * box_base_val**2

    # Create figure
    fig_box_fixed = go.Figure()

    # Bottom face
    x_btm, y_btm = np.meshgrid(
        [0, box_base_val],
        [0, box_base_val]
    )
    z_btm = np.zeros_like(x_btm)

    fig_box_fixed.add_trace(go.Surface(
        x=x_btm, y=y_btm, z=z_btm,
        showscale=False,
        opacity=0.8,
        colorscale='Blues',
        name='Bottom'
    ))

    # 4 vertical sides
    # Front wall (y=0)
    fig_box_fixed.add_trace(go.Surface(
        x=np.array([[0, box_base_val], [0, box_base_val]]),
        y=np.array([[0, 0], [0, 0]]),
        z=np.array([[0, 0], [box_height_val, box_height_val]]),
        showscale=False,
        colorscale='Blues',
        opacity=0.8
    ))

    # Back wall (y=max)
    fig_box_fixed.add_trace(go.Surface(
        x=np.array([[0, box_base_val], [0, box_base_val]]),
        y=np.array([[box_base_val, box_base_val], [box_base_val, box_base_val]]),
        z=np.array([[0, 0], [box_height_val, box_height_val]]),
        showscale=False,
        colorscale='Blues',
        opacity=0.8
    ))

    # Left wall (x=0)
    fig_box_fixed.add_trace(go.Surface(
        x=np.array([[0, 0], [0, 0]]),
        y=np.array([[0, box_base_val], [0, box_base_val]]),
        z=np.array([[0, 0], [box_height_val, box_height_val]]),
        showscale=False,
        colorscale='Blues',
        opacity=0.8
    ))

    # Right wall (x=max)
    fig_box_fixed.add_trace(go.Surface(
        x=np.array([[box_base_val, box_base_val], [box_base_val, box_base_val]]),
        y=np.array([[0, box_base_val], [0, box_base_val]]),
        z=np.array([[0, 0], [box_height_val, box_height_val]]),
        showscale=False,
        colorscale='Blues',
        opacity=0.8
    ))

    # Layout
    fig_box_fixed.update_layout(
        title=f'3D View of Folded Open-Top Box, Volume = {box_volume_val:.1f} cm³',
        scene=dict(
            xaxis=dict(showgrid=False, showticklabels=False, zeroline=False, range=[-1, box_base_val + 2]),
            yaxis=dict(showgrid=False, showticklabels=False, zeroline=False, range=[-1, box_base_val + 2]),
            zaxis=dict(showgrid=False, showticklabels=False, zeroline=False, range=[0, box_height_val + 5]),
            aspectmode='data'
        ),
        template='plotly_white',
        showlegend=False
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Solution Sketch:

    Suppose we cut out squares with side-length $x$, then the box we create will have base-square with side-length $30 - 2x$, and height being $x$. Thus, we have $V = (30 - 2x)^2 \cdot x$. Proceed to take derivative to find critical point(s) and find (absolute) maximum(s).
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Example 8""")
    return


@app.cell
def _(mo):
    mo.md(r"""A rectangular page (white rectangle) is to contain $24$ square inches of print (gray rectangle). The margins at top, left, and right are to be $1$ inches, and the margin at bottom is to be $2$ inches. What should the dimensions of the page be so that least amount of paper is used?""")
    return


@app.cell
def _(mo, np):
    height_slider = mo.ui.slider(
        steps=np.linspace(4, 20, 10001),
        label="Height of the page",
        value=4,
    )
    height_slider
    return (height_slider,)


@app.cell
def _(go, height_slider):
    # Slider input
    H_page = height_slider.value  # total page height

    # Margins
    margin_top = 1
    margin_bottom = 2
    margin_side = 1

    # Compute print area height and width
    H_print = H_page - margin_top - margin_bottom
    W_print = 24 / H_print
    W_page = W_print + 2 * margin_side
    A_page = W_page * H_page

    # Page rectangle (white)
    page_x = [0, W_page, W_page, 0, 0]
    page_y = [0, 0, H_page, H_page, 0]

    # Print rectangle (gray)
    x0_print = margin_side
    x1_print = margin_side + W_print
    y0_print = margin_bottom
    y1_print = margin_bottom + H_print
    print_x = [x0_print, x1_print, x1_print, x0_print, x0_print]
    print_y = [y0_print, y0_print, y1_print, y1_print, y0_print]

    # Create figure
    fig_page = go.Figure()

    # Page outline
    fig_page.add_trace(go.Scatter(
        x=page_x, y=page_y,
        fill='toself',
        fillcolor='white',
        line=dict(color='black'),
        name='Page'
    ))

    # Printing area
    fig_page.add_trace(go.Scatter(
        x=print_x, y=print_y,
        fill='toself',
        fillcolor='rgba(150, 150, 150, 0.5)',
        line=dict(color='gray'),
        name='Print Area',
        showlegend=False
    ))

    # Label total page width
    fig_page.add_trace(go.Scatter(
        x=[W_page / 2], y=[-0.5],
        mode='text',
        text=[f"Width ≈ {W_page:.2f} in"],
        textfont=dict(size=14),
        showlegend=False
    ))

    # Label total page height
    fig_page.add_trace(go.Scatter(
        x=[-0.5], y=[H_page / 2],
        mode='text',
        text=[f"Height = {H_page} in"],
        textfont=dict(size=14),
        showlegend=False
    ))

    # Label page area
    fig_page.add_trace(go.Scatter(
        x=[W_page / 2],
        y=[H_page + 0.3],
        mode='text',
        text=[f"Page Area ≈ {A_page:.2f} in²"],
        textfont=dict(size=16, color='black'),
        showlegend=False
    ))

    # Margin labels
    fig_page.add_trace(go.Scatter(
        x=[W_page + 0.2], y=[H_page - 0.5],
        mode='text',
        text=["Top Margin = 1 in"],
        textfont=dict(size=12, color='blue'),
        showlegend=False
    ))

    fig_page.add_trace(go.Scatter(
        x=[W_page + 0.2], y=[0.5],
        mode='text',
        text=["Bottom Margin = 2 in"],
        textfont=dict(size=12, color='blue'),
        showlegend=False
    ))

    fig_page.add_trace(go.Scatter(
        x=[0.5], y=[-1.2],
        mode='text',
        text=["Side Margins = 1 in"],
        textfont=dict(size=12, color='blue'),
        showlegend=False
    ))

    # Layout
    fig_page.update_layout(
        title='Printed Area Within Page with Fixed Margins',
        xaxis_title='',
        yaxis_title='',
        xaxis=dict(
            showgrid=False,
            zeroline=False,
            showticklabels=False,
            range=[-1, W_page + 2],
            constrain='domain'
        ),
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            showticklabels=False,
            range=[-2, H_page + 2],
            scaleanchor='x'
        ),
        template='plotly_white',
        showlegend=False
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Solution Sketch:

    If the height of the page is $h$, then the height of the printing area is $h - 1 - 2 = h - 3$ (taking out top and bottom margin). If the width of the page is $w$, then the width of the printing area is $w - 1- 1 = w- 2$. We know $24 = (h-3)(w-2)$ thus $\displaystyle w = \frac{24}{h-3}+2$, thus the area of the page is $\displaystyle A = h \cdot w = h \cdot (\frac{24}{h-3}+2)$. Proceed to take derivative to find critical point(s) and find (absolute) minimum(s).
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Example 9""")
    return


@app.cell
def _(mo):
    mo.md(r"""A cone-shaped drinking cup is made from a circular piece of paper of radius $10$ cm by cutting out a sector and joining the edges. Find the maximum capacity of such a cup.""")
    return


@app.cell
def _(mo, np):
    theta_slider_1 = mo.ui.slider(
        steps=np.linspace(0, 2 * np.pi, 10001),
        label="Angle of the sector cut out",
        value=0,
    )
    theta_slider_1
    return (theta_slider_1,)


@app.cell
def _(go, np, theta_slider_1):
    # Parameters
    R_paper = 10
    theta_cut = theta_slider_1.value  # in radians
    alpha_remain = 2 * np.pi - theta_cut

    # Cone base radius and height
    r_cone = (R_paper * alpha_remain) / (2 * np.pi)
    h_cone = np.sqrt(R_paper**2 - r_cone**2)
    V_cone = (1 / 3) * np.pi * r_cone**2 * h_cone

    # ------------------------
    # 1. Flat circular paper with cut sector
    # ------------------------
    theta_full = np.linspace(0, 2 * np.pi, 400)
    x_circle = R_paper * np.cos(theta_full)
    y_circle = R_paper * np.sin(theta_full)

    # Cut sector (from 0 to θ)
    theta_sector = np.linspace(0, theta_cut, 100)
    x_cut_1 = np.concatenate([[0], R_paper * np.cos(theta_sector), [0]])
    y_cut = np.concatenate([[0], R_paper * np.sin(theta_sector), [0]])

    fig_flat_circle = go.Figure()

    # Full circle outline
    fig_flat_circle.add_trace(go.Scatter(
        x=x_circle, y=y_circle,
        mode='lines',
        line=dict(color='black'),
        name='Paper'
    ))

    # Cut-out sector
    fig_flat_circle.add_trace(go.Scatter(
        x=x_cut_1, y=y_cut,
        fill='toself',
        fillcolor='rgba(200, 0, 0, 0.3)',
        line=dict(color='red'),
        showlegend=False
    ))

    # Theta label
    label_x = 2.5 * np.cos(theta_cut / 2)
    label_y = 2.5 * np.sin(theta_cut / 2)
    fig_flat_circle.add_trace(go.Scatter(
        x=[label_x],
        y=[label_y],
        mode='text',
        text=["θ"],
        textfont=dict(size=16, color='red'),
        showlegend=False
    ))

    # Layout
    fig_flat_circle.update_layout(
        title='Circular Paper with Sector Removed',
        xaxis=dict(showgrid=False, showticklabels=False, zeroline=False, range=[-11, 11]),
        yaxis=dict(showgrid=False, showticklabels=False, zeroline=False, scaleanchor='x', range=[-11, 11]),
        template='plotly_white',
        showlegend=False
    )
    return V_cone, h_cone, r_cone


@app.cell
def _(V_cone, go, h_cone, np, r_cone):
    theta_cone = np.linspace(0, 2 * np.pi, 100)
    z_cone = np.linspace(0, h_cone, 50)
    T_cone, Z_cone = np.meshgrid(theta_cone, z_cone)
    X_cone = (r_cone * (1 - Z_cone / h_cone)) * np.cos(T_cone)
    Y_cone = (r_cone * (1 - Z_cone / h_cone)) * np.sin(T_cone)
    Z_cone = Z_cone

    fig_cone = go.Figure()

    fig_cone.add_trace(go.Surface(
        x=X_cone, y=Y_cone, z=Z_cone,
        showscale=False,
        colorscale='Blues',
        opacity=0.9
    ))

    camera=dict(eye=dict(x=0.01, y=-2, z=0.6))

    # Layout
    fig_cone.update_layout(
        title=f'Cone Formed from Paper Sector with Volume ≈ {V_cone:.2f} cm³',
        scene=dict(
            xaxis=dict(showgrid=False, showticklabels=False, zeroline=False, range=[-r_cone - 1, r_cone + 1]),
            yaxis=dict(showgrid=False, showticklabels=False, zeroline=False, range=[-r_cone - 1, r_cone + 1]),
            zaxis=dict(showgrid=False, showticklabels=False, zeroline=False, range=[0, h_cone + 5]),
            aspectmode='data',
            camera=dict(eye=dict(x=0.01, y=-2, z=0.6))  # <<< This is the key
        ),
        template='plotly_white',
        showlegend=False
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Solution Sketch:

    If the sector removed has angle $\theta$, then the remaining angle is $2\pi - \theta$, and the arc length becomes the base circumference of the cone. Since the radius of the paper is $10$ cm, the slant height of the cone is $10$. The base circumference is $C = 10(2\pi - \theta)$ so the radius of the cone is $r = \frac{10(2\pi - \theta)}{2\pi}$. By the Pythagorean theorem, the height of the cone is $h = \sqrt{10^2 - r^2}$ and the volume is $V = \frac{1}{3} \pi r^2 h = \frac{1}{3} \pi \left( \frac{10(2\pi - \theta)}{2\pi} \right)^2 \cdot \sqrt{100 - \left( \frac{10(2\pi - \theta)}{2\pi} \right)^2}$. Now differentiate $V(\theta)$ to find the maximum.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Example 10""")
    return


@app.cell
def _(mo):
    mo.md(r"""A box with a square base and open top must have a volume of $32000$ cm³. Find the dimensions of the box that minimize the amount of material used.""")
    return


@app.cell
def _(mo, np):
    base_slider = mo.ui.slider(
        steps=np.linspace(30, 50, 10001),
        label="Base of the box",
        value=30,
    )
    base_slider
    return (base_slider,)


@app.cell
def _(base_slider, go, np):
    # Slider value
    x_box = base_slider.value  # base side length
    h_box = 32000 / x_box**2   # height from volume constraint

    # Compute surface area
    A_surface = x_box**2 + 128000 / x_box

    # Create figure
    fig_box3d = go.Figure()

    # Bottom face
    x_btm_1, y_btm_1 = np.meshgrid([0, x_box], [0, x_box])
    z_btm_1 = np.zeros_like(x_btm_1)
    fig_box3d.add_trace(go.Surface(
        x=x_btm_1, y=y_btm_1, z=z_btm_1,
        surfacecolor=np.ones_like(z_btm_1),
        colorscale=[[0, 'lightblue'], [1, 'lightblue']],
        showscale=False,
        opacity=0.8
    ))

    # Front wall (y = 0)
    fig_box3d.add_trace(go.Surface(
        x=[[0, x_box], [0, x_box]],
        y=[[0, 0], [0, 0]],
        z=[[0, 0], [h_box, h_box]],
        surfacecolor=[[1, 1], [1, 1]],
        colorscale=[[0, 'lightblue'], [1, 'lightblue']],
        showscale=False,
        opacity=0.8
    ))

    # Back wall (y = x_box)
    fig_box3d.add_trace(go.Surface(
        x=[[0, x_box], [0, x_box]],
        y=[[x_box, x_box], [x_box, x_box]],
        z=[[0, 0], [h_box, h_box]],
        surfacecolor=[[1, 1], [1, 1]],
        colorscale=[[0, 'lightblue'], [1, 'lightblue']],
        showscale=False,
        opacity=0.8
    ))

    # Left wall (x = 0)
    fig_box3d.add_trace(go.Surface(
        x=[[0, 0], [0, 0]],
        y=[[0, x_box], [0, x_box]],
        z=[[0, 0], [h_box, h_box]],
        surfacecolor=[[1, 1], [1, 1]],
        colorscale=[[0, 'lightblue'], [1, 'lightblue']],
        showscale=False,
        opacity=0.8
    ))

    # Right wall (x = x_box)
    fig_box3d.add_trace(go.Surface(
        x=[[x_box, x_box], [x_box, x_box]],
        y=[[0, x_box], [0, x_box]],
        z=[[0, 0], [h_box, h_box]],
        surfacecolor=[[1, 1], [1, 1]],
        colorscale=[[0, 'lightblue'], [1, 'lightblue']],
        showscale=False,
        opacity=0.8
    ))

    # Layout
    fig_box3d.update_layout(
        title=f"3D View of Open-Top Box<br>Surface Area ≈ {A_surface:.1f} cm²",
        scene=dict(
            xaxis=dict(showgrid=False, showticklabels=False, zeroline=False, range=[-1, x_box + 2]),
            yaxis=dict(showgrid=False, showticklabels=False, zeroline=False, range=[-1, x_box + 2]),
            zaxis=dict(showgrid=False, showticklabels=False, zeroline=False, range=[0, h_box + 5]),
            aspectmode='data',
            camera=dict(eye=dict(x=1.4, y=-1.4, z=0.7))  # nice angled view
        ),
        template='plotly_white',
        showlegend=False
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Solution Sketch:

    If the base has side length $x$ and the height is $h$, then the volume is
    $\displaystyle V = x^2 h = 32000 \quad \Rightarrow \quad h = \frac{32000}{x^2}$. The surface area (amount of material used) is the area of the base plus the four sides: $\displaystyle A = x^2 + 4xh = x^2 + 4x \cdot \frac{32000}{x^2} = x^2 + \frac{128000}{x}$. Now differentiate $A(x)$ to find the minimum.
    """
    )
    return


if __name__ == "__main__":
    app.run()
