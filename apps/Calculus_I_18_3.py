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
    nav_menu = mo.nav_menu(
        {
            "https://iumery.com": f"{mo.icon('lucide:home')} Home",
            "Optimization Problems Example Sets": {
                "/apps/Calculus_I_18_1.html": f"{mo.icon('lucide:file-text')} Set 1",
                "/apps/Calculus_I_18_2.html": f"{mo.icon('lucide:file-text')} Set 2",
                "/apps/Calculus_I_18_4.html": f"{mo.icon('lucide:file-text')} Set 4",
                "/apps/Calculus_I_18_5.html": f"{mo.icon('lucide:file-text')} Set 5",
            },
        },
        orientation="vertical",
    )
    nav_menu
    return


@app.cell
def _(mo):
    mo.md(r"""# 3.5 Optimization Problems Example Set 3""")
    return


@app.cell
def _(mo):
    mo.md(r"""### Example 5""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""Find the points on the ellipse $4x^2 + y^2 = 4$ that are farthest away from the point $(2,0)$."""
    )
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
def _(mo):
    mo.md(r"""**Try it youself using the above slidebar!**""")
    return


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
    segment_len_l = np.sqrt((x2_l - x1_l) ** 2 + (y2_l - y1_l) ** 2)

    # Create figure
    fig_l = go.Figure()

    # Plot full ellipse
    fig_l.add_trace(
        go.Scatter(
            x=np.concatenate([x_left_l, x_right_l[::-1]]),
            y=np.concatenate([y_vals_l, y_vals_l[::-1]]),
            fill="toself",
            fillcolor="rgba(173, 216, 230, 0.3)",
            line=dict(color="blue"),
            name="Ellipse",
        )
    )

    # Plot point on left half
    fig_l.add_trace(
        go.Scatter(
            x=[x2_l],
            y=[y2_l],
            mode="markers+text",
            marker=dict(size=8, color="red"),
            text=[f"({x2_l:.2f}, {y2_l:.2f})"],
            textposition="top left",
            name="Point on ellipse",
        )
    )

    fig_l.add_trace(
        go.Scatter(
            x=[x1_l],
            y=[y1_l],
            mode="markers+text",
            marker=dict(size=8, color="red"),
            text=[f"({x1_l:.0f}, {y1_l:.0f})"],
            textposition="top left",
            name="Point on ellipse",
        )
    )

    # Segment from (1, 0) to that point
    fig_l.add_trace(
        go.Scatter(
            x=[x1_l, x2_l],
            y=[y1_l, y2_l],
            mode="lines+text",
            line=dict(color="green", dash="dash"),
            text=[None, f"Length ≈ {segment_len_l:.2f}"],
            textposition="bottom right",
            showlegend=False,
        )
    )

    # Layout
    fig_l.update_layout(
        title="Segment from (2, 0) to a Point on Left Half of Ellipse",
        xaxis_title="x",
        yaxis_title="y",
        template="plotly_white",
        xaxis=dict(scaleanchor="y", range=[-2.5, 2]),
        yaxis=dict(scaleanchor="x", range=[-2.5, 2.5]),
        showlegend=False,
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
    mo.md(
        r"""Find the area of the largest trapezoid that can be inscribed in a circle of radius $1$ and whose base is a diameter of the circle."""
    )
    return


@app.cell
def _(mo, np):
    x_slider_2 = mo.ui.slider(
        steps=np.linspace(0, 1, 10001),
        label="x Coordinate of the top-right vertice of the trapezoid",
        value=0.5,
    )
    x_slider_2
    return (x_slider_2,)


@app.cell
def _(mo):
    mo.md(r"""**Try it youself using the above slidebar!**""")
    return


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
    fig_trapezoid.add_trace(
        go.Scatter(
            x=x_vals_u,
            y=y_vals_u,
            mode="lines",
            name="Upper Unit Circle",
            line=dict(color="blue"),
        )
    )

    # Plot trapezoid fill
    fig_trapezoid.add_trace(
        go.Scatter(
            x=x_trap,
            y=y_trap,
            fill="toself",
            fillcolor="rgba(255, 0, 0, 0.3)",
            line=dict(width=0),
            name="Trapezoid",
            showlegend=False,
        )
    )

    # Label area
    fig_trapezoid.add_trace(
        go.Scatter(
            x=[0],
            y=[y0_trap / 2],
            mode="text",
            text=[f"Area ≈ {trap_area:.3f}"],
            textfont=dict(size=16, color="darkred"),
            showlegend=False,
        )
    )

    # Vertical dotted line from (x0_trap, y0_trap) to (x0_trap, 0)
    fig_trapezoid.add_trace(
        go.Scatter(
            x=[x0_trap, x0_trap],
            y=[0, y0_trap],
            mode="lines",
            line=dict(color="black", dash="dot"),
            showlegend=False,
        )
    )

    # Horizontal dotted line from (0, y0_trap) to (x0_trap, y0_trap)
    fig_trapezoid.add_trace(
        go.Scatter(
            x=[0, x0_trap],
            y=[y0_trap, y0_trap],
            mode="lines",
            line=dict(color="black", dash="dot"),
            showlegend=False,
        )
    )

    # Label height as y
    fig_trapezoid.add_trace(
        go.Scatter(
            x=[x0_trap + 0.05],
            y=[y0_trap / 2],
            mode="text",
            text=["y"],
            textfont=dict(size=14, color="black"),
            showlegend=False,
        )
    )

    # Label width as x
    fig_trapezoid.add_trace(
        go.Scatter(
            x=[x0_trap / 2],
            y=[y0_trap + 0.05],
            mode="text",
            text=["x"],
            textfont=dict(size=14, color="black"),
            showlegend=False,
        )
    )

    # Layout
    fig_trapezoid.update_layout(
        title="Trapezoid Inscribed in the Unit Circle",
        xaxis_title="x",
        yaxis_title="y",
        xaxis=dict(scaleanchor="y", range=[-1.2, 1.2]),
        yaxis=dict(scaleanchor="x", range=[-0.1, 1.1]),
        template="plotly_white",
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
        steps=np.linspace(0, np.pi / 2, 10001),
        label="Angle between the top-right vertice of the trapezoid and the x-axis",
        value=np.pi / 4,
    )
    theta_slider
    return (theta_slider,)


@app.cell
def _(mo):
    mo.md(r"""**Try it youself using the above slidebar!**""")
    return


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
    fig_ang.add_trace(
        go.Scatter(
            x=x_unit,
            y=y_unit,
            mode="lines",
            name="Upper Unit Circle",
            line=dict(color="blue"),
        )
    )

    # Trapezoid region
    fig_ang.add_trace(
        go.Scatter(
            x=x_trap_ang,
            y=y_trap_ang,
            fill="toself",
            fillcolor="rgba(255, 100, 0, 0.3)",
            line=dict(width=0),
            name="Trapezoid",
            showlegend=False,
        )
    )

    # Segment from (0, 0) to top-right corner
    fig_ang.add_trace(
        go.Scatter(
            x=[0, x_corner],
            y=[0, y_corner],
            mode="lines",
            line=dict(color="black", dash="dash"),
            name="Angle arm",
            showlegend=False,
        )
    )

    # Arc to show angle θ
    fig_ang.add_trace(
        go.Scatter(
            x=x_arc, y=y_arc, mode="lines", line=dict(color="gray"), showlegend=False
        )
    )

    # θ label near middle of arc
    arc_label_x = arc_radius * np.cos(theta_angle / 2)
    arc_label_y = arc_radius * np.sin(theta_angle / 2)
    fig_ang.add_trace(
        go.Scatter(
            x=[arc_label_x],
            y=[arc_label_y],
            mode="text",
            text=["θ"],
            textposition="bottom left",
            textfont=dict(size=16, color="gray"),
            showlegend=False,
        )
    )

    # Area label
    fig_ang.add_trace(
        go.Scatter(
            x=[0],
            y=[y_corner / 2],
            mode="text",
            text=[f"Area ≈ {area_trap_ang:.3f}"],
            textfont=dict(size=16, color="darkred"),
            showlegend=False,
        )
    )

    # Vertical dotted line from (x_corner, y_corner) to (x_corner, 0)
    fig_ang.add_trace(
        go.Scatter(
            x=[x_corner, x_corner],
            y=[0, y_corner],
            mode="lines",
            line=dict(color="black", dash="dot"),
            showlegend=False,
        )
    )

    # Horizontal dotted line from (0, y_corner) to (x_corner, y_corner)
    fig_ang.add_trace(
        go.Scatter(
            x=[0, x_corner],
            y=[y_corner, y_corner],
            mode="lines",
            line=dict(color="black", dash="dot"),
            showlegend=False,
        )
    )

    # Label sin(theta)
    fig_ang.add_trace(
        go.Scatter(
            x=[x_corner + 0.05],
            y=[y_corner / 2],
            mode="text",
            text=["sin(θ)"],
            textfont=dict(size=14, color="black"),
            showlegend=False,
        )
    )

    # Label cos(theta)
    fig_ang.add_trace(
        go.Scatter(
            x=[x_corner / 2],
            y=[y_corner + 0.05],
            mode="text",
            text=["cos(θ)"],
            textfont=dict(size=14, color="black"),
            showlegend=False,
        )
    )

    # Layout
    fig_ang.update_layout(
        title="Trapezoid under Unit Circle with Angle θ",
        xaxis_title="x",
        yaxis_title="y",
        xaxis=dict(scaleanchor="y", range=[-1.2, 1.2]),
        yaxis=dict(scaleanchor="x", range=[-0.1, 1.1]),
        template="plotly_white",
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""Another way of doing this is to utilize trignometry functions. A point on unit circle always can be expressed as $(\cos(\theta), \sin(\theta))$, thus the area can be expressed as $A = (\cos(\theta) + 1)\cdot \sin(\theta)$. Proceed to take derivative to find critical point(s) and find (absolute) maximum(s)."""
    )
    return


if __name__ == "__main__":
    app.run()
