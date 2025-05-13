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
            "/index.html": f"{mo.icon('lucide:home')} Home",
            "Optimization Problems Example Sets": {
                "/apps/Calculus_I_18_1.html": f"{mo.icon('lucide:file-text')} Set 1",
                "/apps/Calculus_I_18_2.html": f"{mo.icon('lucide:file-text')} Set 2",
                "/apps/Calculus_I_18_3.html": f"{mo.icon('lucide:file-text')} Set 3",
                "/apps/Calculus_I_18_5.html": f"{mo.icon('lucide:file-text')} Set 5",
            },
        },
        orientation="vertical",
    )
    nav_menu
    return


@app.cell
def _(mo):
    mo.md(r"""# 3.5 Optimization Problems Example Set 4""")
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
        value=8,
    )
    corner_slider
    return (corner_slider,)


@app.cell
def _(mo):
    mo.md(r"""**Try it youself using the above slidebar!**""")
    return


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
    for dx, dy in [
        (0, 0),
        (card_size - x_cut, 0),
        (card_size - x_cut, card_size - x_cut),
        (0, card_size - x_cut),
    ]:
        cut_x = [dx, dx + x_cut, dx + x_cut, dx, dx]
        cut_y = [dy, dy, dy + x_cut, dy + x_cut, dy]
        cut_squares.append(
            go.Scatter(
                x=cut_x,
                y=cut_y,
                fill="toself",
                fillcolor="rgba(150, 150, 150, 0.5)",
                line=dict(color="gray"),
                showlegend=False,
            )
        )

    fig_flat = go.Figure()

    # Cardboard base
    fig_flat.add_trace(
        go.Scatter(
            x=card_x,
            y=card_y,
            fill="toself",
            fillcolor="white",
            line=dict(color="black"),
            name="Cardboard",
        )
    )

    # Cutouts
    for square in cut_squares:
        fig_flat.add_trace(square)

    # Label cut size
    fig_flat.add_trace(
        go.Scatter(
            x=[x_cut / 2],
            y=[x_cut / 2],
            mode="text",
            text=[f"x = {x_cut:.1f} cm"],
            textfont=dict(size=14),
            showlegend=False,
        )
    )

    # Layout for 2D view
    fig_flat.update_layout(
        title="Cardboard with Corner Cuts (Top View)",
        xaxis=dict(
            showgrid=False,
            zeroline=False,
            showticklabels=False,
            range=[-2, card_size + 2],
        ),
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            showticklabels=False,
            scaleanchor="x",
            range=[-2, card_size + 2],
        ),
        template="plotly_white",
        showlegend=False,
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
    x_btm, y_btm = np.meshgrid([0, box_base_val], [0, box_base_val])
    z_btm = np.zeros_like(x_btm)

    fig_box_fixed.add_trace(
        go.Surface(
            x=x_btm,
            y=y_btm,
            z=z_btm,
            showscale=False,
            opacity=0.8,
            colorscale="Blues",
            name="Bottom",
        )
    )

    # 4 vertical sides
    # Front wall (y=0)
    fig_box_fixed.add_trace(
        go.Surface(
            x=np.array([[0, box_base_val], [0, box_base_val]]),
            y=np.array([[0, 0], [0, 0]]),
            z=np.array([[0, 0], [box_height_val, box_height_val]]),
            showscale=False,
            colorscale="Blues",
            opacity=0.8,
        )
    )

    # Back wall (y=max)
    fig_box_fixed.add_trace(
        go.Surface(
            x=np.array([[0, box_base_val], [0, box_base_val]]),
            y=np.array([[box_base_val, box_base_val], [box_base_val, box_base_val]]),
            z=np.array([[0, 0], [box_height_val, box_height_val]]),
            showscale=False,
            colorscale="Blues",
            opacity=0.8,
        )
    )

    # Left wall (x=0)
    fig_box_fixed.add_trace(
        go.Surface(
            x=np.array([[0, 0], [0, 0]]),
            y=np.array([[0, box_base_val], [0, box_base_val]]),
            z=np.array([[0, 0], [box_height_val, box_height_val]]),
            showscale=False,
            colorscale="Blues",
            opacity=0.8,
        )
    )

    # Right wall (x=max)
    fig_box_fixed.add_trace(
        go.Surface(
            x=np.array([[box_base_val, box_base_val], [box_base_val, box_base_val]]),
            y=np.array([[0, box_base_val], [0, box_base_val]]),
            z=np.array([[0, 0], [box_height_val, box_height_val]]),
            showscale=False,
            colorscale="Blues",
            opacity=0.8,
        )
    )

    # Layout
    fig_box_fixed.update_layout(
        title=f"3D View of Folded Open-Top Box, Volume = {box_volume_val:.1f} cm³",
        scene=dict(
            xaxis=dict(
                showgrid=False,
                showticklabels=False,
                zeroline=False,
                range=[-1, box_base_val + 2],
            ),
            yaxis=dict(
                showgrid=False,
                showticklabels=False,
                zeroline=False,
                range=[-1, box_base_val + 2],
            ),
            zaxis=dict(
                showgrid=False,
                showticklabels=False,
                zeroline=False,
                range=[0, box_height_val + 5],
            ),
            aspectmode="data",
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
        value=12,
    )
    height_slider
    return (height_slider,)


@app.cell
def _(mo):
    mo.md(r"""**Try it youself using the above slidebar!**""")
    return


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
    fig_page.add_trace(
        go.Scatter(
            x=page_x,
            y=page_y,
            fill="toself",
            fillcolor="white",
            line=dict(color="black"),
            name="Page",
        )
    )

    # Printing area
    fig_page.add_trace(
        go.Scatter(
            x=print_x,
            y=print_y,
            fill="toself",
            fillcolor="rgba(150, 150, 150, 0.5)",
            line=dict(color="gray"),
            name="Print Area",
            showlegend=False,
        )
    )

    # Label total page width
    fig_page.add_trace(
        go.Scatter(
            x=[W_page / 2],
            y=[-0.5],
            mode="text",
            text=[f"Width ≈ {W_page:.2f} in"],
            textfont=dict(size=14),
            showlegend=False,
        )
    )

    # Label total page height
    fig_page.add_trace(
        go.Scatter(
            x=[-0.5],
            y=[H_page / 2],
            mode="text",
            text=[f"Height = {H_page} in"],
            textfont=dict(size=14),
            showlegend=False,
        )
    )

    # Label page area
    fig_page.add_trace(
        go.Scatter(
            x=[W_page / 2],
            y=[H_page + 0.3],
            mode="text",
            text=[f"Page Area ≈ {A_page:.2f} in²"],
            textfont=dict(size=16, color="black"),
            showlegend=False,
        )
    )

    # Margin labels
    fig_page.add_trace(
        go.Scatter(
            x=[W_page + 0.2],
            y=[H_page - 0.5],
            mode="text",
            text=["Top Margin = 1 in"],
            textfont=dict(size=12, color="blue"),
            showlegend=False,
        )
    )

    fig_page.add_trace(
        go.Scatter(
            x=[W_page + 0.2],
            y=[0.5],
            mode="text",
            text=["Bottom Margin = 2 in"],
            textfont=dict(size=12, color="blue"),
            showlegend=False,
        )
    )

    fig_page.add_trace(
        go.Scatter(
            x=[0.5],
            y=[-1.2],
            mode="text",
            text=["Side Margins = 1 in"],
            textfont=dict(size=12, color="blue"),
            showlegend=False,
        )
    )

    # Layout
    fig_page.update_layout(
        title="Printed Area Within Page with Fixed Margins",
        xaxis_title="",
        yaxis_title="",
        xaxis=dict(
            showgrid=False,
            zeroline=False,
            showticklabels=False,
            range=[-1, W_page + 2],
            constrain="domain",
        ),
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            showticklabels=False,
            range=[-2, H_page + 2],
            scaleanchor="x",
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

    If the height of the page is $h$, then the height of the printing area is $h - 1 - 2 = h - 3$ (taking out top and bottom margin). If the width of the page is $w$, then the width of the printing area is $w - 1- 1 = w- 2$. We know $24 = (h-3)(w-2)$ thus $\displaystyle w = \frac{24}{h-3}+2$, thus the area of the page is $\displaystyle A = h \cdot w = h \cdot (\frac{24}{h-3}+2)$. Proceed to take derivative to find critical point(s) and find (absolute) minimum(s).
    """
    )
    return


if __name__ == "__main__":
    app.run()
