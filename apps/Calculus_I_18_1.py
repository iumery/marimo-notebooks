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
                "/apps/Calculus_I_18_2.html": f"{mo.icon('lucide:file-text')} Set 2",
                "/apps/Calculus_I_18_3.html": f"{mo.icon('lucide:file-text')} Set 3",
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
    mo.md(r"""# 3.5 Optimization Problems Example Set 1""")
    return


@app.cell
def _(mo):
    mo.md(r"""### Example 1""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""A company needs to produce a container of cylindrical shape to hold $1 \text{ L}$ (or $1000 \text{ cm}^3$) of liquid. Find the dimension of the container that minimize the material usage."""
    )
    return


@app.cell
def _(mo, np):
    r_slider = mo.ui.slider(
        steps=np.linspace(4, 8, 10001),
        label="Radius of the Cylinder",
        value=6,
    )
    r_slider
    return (r_slider,)


@app.cell
def _(mo):
    mo.md(r"""**Try it youself using the above slidebar!**""")
    return


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
    fig_cyl = go.Figure(
        data=[
            go.Surface(
                x=x_cyl,
                y=y_cyl,
                z=z_cyl,
                colorscale="Blues",
                showscale=False,
                opacity=0.8,
            )
        ]
    )

    # Adjust camera to improve visibility
    camera_config = dict(eye=dict(x=0.0, y=2.5, z=0.1))

    # Layout
    fig_cyl.update_layout(
        title=f"Cylinder with radius r ≈ {r_slider.value:.2f} cm<br>"
        f"height h ≈ {h_input:.2f} cm<br>"
        f"surface area A ≈ {cylinder_area:.2f} cm²",
        scene=dict(
            xaxis_title="x (cm)",
            yaxis_title="y (cm)",
            zaxis_title="height (cm)",
            aspectmode="data",
            camera=camera_config,
        ),
        template="plotly_white",
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
    mo.md(
        r"""There are $50$ apple trees in an orchard and each of them are producing $800$ apples. For each additional tree planted in the orchard, the output of each tree drops by $10$ apples. How many trees should be added to the existing orchard to maximize the total output?"""
    )
    return


@app.cell
def _(mo):
    n_trees = mo.ui.slider(0, 80, value=40, label="Number of Trees to Plant")
    n_trees
    return (n_trees,)


@app.cell
def _(mo):
    mo.md(r"""**Try it youself using the above slidebar!**""")
    return


@app.cell
def _(mo, n_trees):
    total_output = (50 + n_trees.value) * (800 - 10 * n_trees.value)
    mo.md(
        f"""If we plant {n_trees.value} new trees, total output is going to be (50 + {n_trees.value}) x (800 - 10 x {n_trees.value}) = {total_output}.
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


if __name__ == "__main__":
    app.run()
