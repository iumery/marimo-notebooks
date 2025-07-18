import marimo

__generated_with = "0.13.15"
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
            "Optimization Problems Example Sets": {
                "/apps/Calculus_I_18_1.html": f"{mo.icon('lucide:file-text')} Set 1",
                "/apps/Calculus_I_18_2.html": f"{mo.icon('lucide:file-text')} Set 2",
                "/apps/Calculus_I_18_3.html": f"{mo.icon('lucide:file-text')} Set 3",
                "/apps/Calculus_I_18_4.html": f"{mo.icon('lucide:file-text')} Set 4",
            },
        },
        orientation="vertical",
    )
    nav_menu
    return


@app.cell
def _(mo):
    mo.md(r"""# 3.5 Optimization Problems Example Set 5""")
    return


@app.cell
def _(mo):
    mo.md(r"""### Example 9""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""A cone-shaped drinking cup is made from a circular piece of paper of radius $10$ cm by cutting out a sector and joining the edges. Find the maximum capacity of such a cup."""
    )
    return


@app.cell
def _(mo, np):
    theta_slider_1 = mo.ui.slider(
        steps=np.linspace(np.pi / 16, 1 * np.pi, 10001),
        label="Angle of the sector cut out",
        value=np.pi * 0.53125,
    )
    theta_slider_1
    return (theta_slider_1,)


@app.cell
def _(mo):
    mo.md(r"""**Try it youself using the above slidebar!**""")
    return


@app.cell
def _(go, make_subplots, np, theta_slider_1):
    # Parameters
    R_paper = 10
    theta_cut = theta_slider_1.value  # in radians
    alpha_remain = 2 * np.pi - theta_cut

    # Cone base radius and height
    r_cone = (R_paper * alpha_remain) / (2 * np.pi)
    h_cone = np.sqrt(R_paper**2 - r_cone**2)
    V_cone = (1 / 3) * np.pi * r_cone**2 * h_cone
    arc_length_remain = alpha_remain * R_paper

    # ------------------------
    # Create 2x2 subplots
    # ------------------------
    fig = make_subplots(
        rows=2,
        cols=2,
        subplot_titles=[
            "1. Circular Paper with Sector Removed",
            "2. Base of Cone (after folding)",
            "3. Cross-Section Triangle of Cone",
            "",
        ],
    )

    # ------------------------
    # 1. Flat circular paper with cut sector and labels
    # ------------------------
    theta_full = np.linspace(0, 2 * np.pi, 400)
    x_circle = R_paper * np.cos(theta_full)
    y_circle = R_paper * np.sin(theta_full)

    theta_sector = np.linspace(0, theta_cut, 100)
    x_cut = np.concatenate([[0], R_paper * np.cos(theta_sector), [0]])
    y_cut = np.concatenate([[0], R_paper * np.sin(theta_sector), [0]])

    # Full circle
    fig.add_trace(
        go.Scatter(x=x_circle, y=y_circle, mode="lines", line=dict(color="black")),
        row=1,
        col=1,
    )

    # Cut-out sector
    fig.add_trace(
        go.Scatter(
            x=x_cut,
            y=y_cut,
            fill="toself",
            fillcolor="rgba(200, 0, 0, 0.3)",
            line=dict(color="red"),
        ),
        row=1,
        col=1,
    )

    # Remaining arc label and arc line
    theta_remain = np.linspace(theta_cut, 2 * np.pi, 200)
    x_remain = R_paper * np.cos(theta_remain)
    y_remain = R_paper * np.sin(theta_remain)
    fig.add_trace(
        go.Scatter(
            x=x_remain, y=y_remain, mode="lines", line=dict(color="blue", dash="dot")
        ),
        row=1,
        col=1,
    )

    # θ label
    fig.add_trace(
        go.Scatter(
            x=[2.5 * np.cos(theta_cut / 2)],
            y=[2.5 * np.sin(theta_cut / 2)],
            mode="text",
            text=["θ"],
            textfont=dict(size=14, color="red"),
            showlegend=False,
        ),
        row=1,
        col=1,
    )

    # 2pi - θ label
    fig.add_trace(
        go.Scatter(
            x=[2.5 * np.cos(theta_cut + alpha_remain / 2)],
            y=[2.5 * np.sin(theta_cut + alpha_remain / 2)],
            mode="text",
            text=["2π - θ"],
            textfont=dict(size=14, color="blue"),
            showlegend=False,
        ),
        row=1,
        col=1,
    )

    # Arc length label
    fig.add_trace(
        go.Scatter(
            x=[x_remain[int(len(x_remain) / 2)]],
            y=[y_remain[int(len(y_remain) / 2)]],
            mode="text",
            text=[f"Arc = 10x(2π - θ)<br>={arc_length_remain:.1f} cm"],
            textfont=dict(size=14, color="blue"),
            showlegend=False,
        ),
        row=1,
        col=1,
    )

    # ------------------------
    # 2. Base of the cone (circle)
    # ------------------------
    theta_base = np.linspace(0, 2 * np.pi, 400)
    x_base = r_cone * np.cos(theta_base)
    y_base = r_cone * np.sin(theta_base)

    fig.add_trace(
        go.Scatter(x=x_base, y=y_base, mode="lines", line=dict(color="blue")),
        row=1,
        col=2,
    )

    # Radius line
    fig.add_trace(
        go.Scatter(
            x=[0, r_cone],
            y=[0, 0],
            mode="lines+text",
            text=[f"r= Perimeter/2π<br>={arc_length_remain/(2*np.pi):.1f} cm"],
            textposition="middle right",
            line=dict(color="black", dash="dot"),
            showlegend=False,
        ),
        row=1,
        col=2,
    )

    # Perimeter label
    fig.add_trace(
        go.Scatter(
            x=[0],
            y=[r_cone + 0.5],
            mode="text",
            text=[f"Circumference = {arc_length_remain:.1f} cm"],
            textfont=dict(size=14, color="blue"),
            showlegend=False,
        ),
        row=1,
        col=2,
    )

    # ------------------------
    # 3. Cross-section triangle of cone
    # ------------------------
    fig.add_trace(
        go.Scatter(
            x=[-r_cone, r_cone, 0, -r_cone],
            y=[0, 0, h_cone, 0],
            mode="lines",
            line=dict(color="blue"),
            showlegend=False,
        ),
        row=2,
        col=1,
    )

    # Label base
    fig.add_trace(
        go.Scatter(
            x=[0],
            y=[-1.5],
            mode="text",
            text=[f"2r={arc_length_remain/(np.pi):.1f} cm"],
            textfont=dict(size=14),
            showlegend=False,
        ),
        row=2,
        col=1,
    )

    # Label slant height
    fig.add_trace(
        go.Scatter(
            x=[-r_cone - 0.5],
            y=[h_cone / 2],
            mode="text",
            text=["10 cm"],
            textfont=dict(size=14),
            showlegend=False,
        ),
        row=2,
        col=1,
    )

    # Layout adjustments
    fig.update_layout(
        template="plotly_white",
        showlegend=False,
        title="Cone Construction from Circular Paper",
    )

    fig.update_xaxes(
        range=[-12, 12],
        showgrid=False,
        zeroline=False,
        showticklabels=False,
        row=1,
        col=1,
        scaleanchor="y",
    )
    fig.update_yaxes(
        range=[-11, 11],
        showgrid=False,
        zeroline=False,
        showticklabels=False,
        row=1,
        col=1,
        scaleanchor="x",
    )
    fig.update_xaxes(
        range=[-8, 8],
        showgrid=False,
        zeroline=False,
        showticklabels=False,
        row=1,
        col=2,
        scaleanchor="y",
    )
    fig.update_yaxes(
        range=[-8, 8],
        showgrid=False,
        zeroline=False,
        showticklabels=False,
        row=1,
        col=2,
        scaleanchor="x",
    )
    fig.update_xaxes(
        showgrid=False,
        zeroline=False,
        showticklabels=False,
        row=2,
        col=1,
        scaleanchor="y",
    )
    fig.update_yaxes(
        showgrid=False,
        zeroline=False,
        showticklabels=False,
        row=2,
        col=1,
        scaleanchor="x",
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

    fig_cone.add_trace(
        go.Surface(
            x=X_cone,
            y=Y_cone,
            z=Z_cone,
            showscale=False,
            colorscale="Blues",
            opacity=0.9,
        )
    )

    camera = dict(eye=dict(x=0.01, y=-2, z=0.6))

    # Layout
    fig_cone.update_layout(
        title=f"Cone Formed from Paper Sector with Volume ≈ {V_cone:.2f} cm³",
        scene=dict(
            xaxis=dict(
                showgrid=False,
                showticklabels=False,
                zeroline=False,
                range=[-r_cone - 1, r_cone + 1],
            ),
            yaxis=dict(
                showgrid=False,
                showticklabels=False,
                zeroline=False,
                range=[-r_cone - 1, r_cone + 1],
            ),
            zaxis=dict(
                showgrid=False,
                showticklabels=False,
                zeroline=False,
                range=[0, h_cone + 5],
            ),
            aspectmode="data",
            camera=dict(eye=dict(x=0.01, y=-2, z=0.6)),  # <<< This is the key
        ),
        template="plotly_white",
        showlegend=False,
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
    mo.md(
        r"""A box with a square base and open top must have a volume of $32000$ cm³. Find the dimensions of the box that minimize the amount of material used."""
    )
    return


@app.cell
def _(mo, np):
    base_slider = mo.ui.slider(
        steps=np.linspace(30, 50, 10001),
        label="Base of the box",
        value=40,
    )
    base_slider
    return (base_slider,)


@app.cell
def _(mo):
    mo.md(r"""**Try it youself using the above slidebar!**""")
    return


@app.cell
def _(base_slider, go, np):
    # Slider value
    x_box = base_slider.value  # base side length
    h_box = 32000 / x_box**2  # height from volume constraint

    # Compute surface area
    A_surface = x_box**2 + 128000 / x_box

    # Create figure
    fig_box3d = go.Figure()

    # Bottom face
    x_btm_1, y_btm_1 = np.meshgrid([0, x_box], [0, x_box])
    z_btm_1 = np.zeros_like(x_btm_1)
    fig_box3d.add_trace(
        go.Surface(
            x=x_btm_1,
            y=y_btm_1,
            z=z_btm_1,
            surfacecolor=np.ones_like(z_btm_1),
            colorscale=[[0, "lightblue"], [1, "lightblue"]],
            showscale=False,
            opacity=0.8,
        )
    )

    # Front wall (y = 0)
    fig_box3d.add_trace(
        go.Surface(
            x=[[0, x_box], [0, x_box]],
            y=[[0, 0], [0, 0]],
            z=[[0, 0], [h_box, h_box]],
            surfacecolor=[[1, 1], [1, 1]],
            colorscale=[[0, "lightblue"], [1, "lightblue"]],
            showscale=False,
            opacity=0.8,
        )
    )

    # Back wall (y = x_box)
    fig_box3d.add_trace(
        go.Surface(
            x=[[0, x_box], [0, x_box]],
            y=[[x_box, x_box], [x_box, x_box]],
            z=[[0, 0], [h_box, h_box]],
            surfacecolor=[[1, 1], [1, 1]],
            colorscale=[[0, "lightblue"], [1, "lightblue"]],
            showscale=False,
            opacity=0.8,
        )
    )

    # Left wall (x = 0)
    fig_box3d.add_trace(
        go.Surface(
            x=[[0, 0], [0, 0]],
            y=[[0, x_box], [0, x_box]],
            z=[[0, 0], [h_box, h_box]],
            surfacecolor=[[1, 1], [1, 1]],
            colorscale=[[0, "lightblue"], [1, "lightblue"]],
            showscale=False,
            opacity=0.8,
        )
    )

    # Right wall (x = x_box)
    fig_box3d.add_trace(
        go.Surface(
            x=[[x_box, x_box], [x_box, x_box]],
            y=[[0, x_box], [0, x_box]],
            z=[[0, 0], [h_box, h_box]],
            surfacecolor=[[1, 1], [1, 1]],
            colorscale=[[0, "lightblue"], [1, "lightblue"]],
            showscale=False,
            opacity=0.8,
        )
    )

    # Layout
    fig_box3d.update_layout(
        title=f"3D View of Open-Top Box<br>Surface Area ≈ {A_surface:.1f} cm²",
        scene=dict(
            xaxis=dict(
                showgrid=False,
                showticklabels=False,
                zeroline=False,
                range=[-1, x_box + 2],
            ),
            yaxis=dict(
                showgrid=False,
                showticklabels=False,
                zeroline=False,
                range=[-1, x_box + 2],
            ),
            zaxis=dict(
                showgrid=False,
                showticklabels=False,
                zeroline=False,
                range=[0, h_box + 5],
            ),
            aspectmode="data",
            camera=dict(eye=dict(x=1.4, y=-1.4, z=0.7)),  # nice angled view
        ),
        template="plotly_white",
        showlegend=False,
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
