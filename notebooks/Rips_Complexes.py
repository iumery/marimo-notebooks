import marimo

__generated_with = "0.13.15"
app = marimo.App()


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    nav_menu = mo.nav_menu(
        {
            "/index.html": f"{mo.icon('lucide:home')} Home",
        },
        orientation="vertical",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Vietoris-Rips Complex: Constructing Simplicial Complexes from Point Clouds

    Topological data analysis provides a way to study the "shape" of data. At the heart of TDA lies the idea of building simplicial complexes from finite sets of points in metric spaces. In this notebook, we focus on one of the most widely used constructions in practice: the Vietoris-Rips complex.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Why Vietoris-Rips?

    There are multiple ways to build simplicial complexes from data:

    - The Čech complex is defined via the nerve of balls around points: for each point $p_i$, consider a closed ball $B_r(p_i)$, and include simplices whenever the intersection of balls is non-empty. However, directly checking for these intersections is computationally expensive;
    - The Vietoris-Rips complex provides a simpler, purely combinatorial approximation that can be built directly from pairwise distances.

    In most real-world TDA applications, the Vietoris-Rips complex is used because it is straightforward to compute, even in high dimensions.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Formal Definition: Vietoris-Rips Complex

    Let $(P, d)$ be a finite metric space, where $P$ is a set of points and $d$ is a distance function.

    Given a scale parameter $r > 0$, the Vietoris-Rips complex $\mathbb{VR}^r(P)$ is the simplicial complex where:

    - Each point $p_i \in P$ becomes a $0$-simplex (vertex);
    - Any collection of points $\lbrace p_{i_0}, p_{i_1}, \dots, p_{i_k} \rbrace$ spans a $k$-simplex if and only if $$d(p_{i_a}, p_{i_b}) \leq r \text{ for all pairs } a, b.$$

    In other words, a simplex is included whenever all of its edges are “short enough” relative to the chosen radius $r$.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Code Structure

    In this notebook, we define a `VietorisRipsComplex` class that:

    - Accepts a point cloud;
    - Computes the Vietoris-Rips complex at any chosen scale;
    - Supports visualization in both 2D and 3D.

    We fully separate the mathematical logic of complex construction, the visualization logic (with both static and interactive options), and the class supports arbitrary distance metrics via the `scipy.spatial.distance package`.
    """
    )
    return


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt
    import itertools
    from mpl_toolkits.mplot3d.art3d import Poly3DCollection
    from scipy.spatial import distance
    import plotly.graph_objs as go
    import plotly.io as pio

    pio.templates.default = "plotly_white"


    class VietorisRipsComplex:
        def __init__(self, point_cloud, max_dimension=None, metric="euclidean"):
            self.points = np.array(point_cloud)
            self.n = len(self.points)
            self.dim = self.points.shape[1]
            self.max_dimension = max_dimension if max_dimension is not None else self.dim
            self.metric = metric
            self.distance = distance.cdist(self.points, self.points, metric=self.metric)
            self.rips_complex = None

        def compute_rips_complex(self, radius):
            simplices = [(i,) for i in range(self.n)]  # 0-simplices

            for k in range(2, self.max_dimension + 2):
                for simplex in itertools.combinations(range(self.n), k):
                    pairs = itertools.combinations(simplex, 2)
                    if all(self.distance[i, j] <= radius for i, j in pairs):
                        simplices.append(simplex)

            self.rips_complex = simplices
            return simplices

        def plot_complex(self, radius, interactive=False, box_aspect=[1, 1, 1]):
            simplices = self.compute_rips_complex(radius)

            if interactive and self.dim == 3:
                self._plot_3d_interactive(simplices, radius)
            elif self.dim == 2:
                self._plot_2d(simplices, radius)
            elif self.dim == 3:
                self._plot_3d(simplices, radius, box_aspect)
            else:
                raise ValueError("Only 2D or 3D supported.")

        def _plot_2d(self, simplices, radius):
            fig, ax = plt.subplots(figsize=(8, 8))
            ax.scatter(self.points[:, 0], self.points[:, 1], color="r", s=10)
            for simplex in simplices:
                pts = self.points[list(simplex)]
                if len(simplex) == 2:
                    ax.plot(pts[:, 0], pts[:, 1], "b-", lw=1)
                elif len(simplex) == 3:
                    polygon = plt.Polygon(pts, facecolor="green", alpha=0.3)
                    ax.add_patch(polygon)
            ax.set_title(f"Vietoris-Rips Complex (radius={radius})")
            ax.set_aspect("equal")
            plt.show()

        def _plot_3d(self, simplices, radius, box_aspect):
            fig = plt.figure(figsize=(10, 8))
            ax = fig.add_subplot(111, projection="3d")
            ax.scatter(self.points[:, 0], self.points[:, 1], self.points[:, 2], color="r", s=5)
            for simplex in simplices:
                pts = self.points[list(simplex)]
                if len(simplex) == 2:
                    ax.plot(pts[:, 0], pts[:, 1], pts[:, 2], "b-", lw=1)
                elif len(simplex) == 3:
                    tri = Poly3DCollection([pts], alpha=0.3, facecolor="green")
                    ax.add_collection3d(tri)
            ax.set_title(f"Vietoris-Rips Complex (radius={radius})")
            ax.set_box_aspect(box_aspect)
            plt.show()

        def _plot_3d_interactive(self, simplices, radius):
            vertices = go.Scatter3d(
                x=self.points[:, 0],
                y=self.points[:, 1],
                z=self.points[:, 2],
                mode="markers",
                marker=dict(size=3, color="red"),
            )

            edges, faces = [], []
            for simplex in simplices:
                pts = self.points[list(simplex)]
                if len(simplex) == 2:
                    edges.append(
                        go.Scatter3d(
                            x=[pts[0, 0], pts[1, 0], None],
                            y=[pts[0, 1], pts[1, 1], None],
                            z=[pts[0, 2], pts[1, 2], None],
                            mode="lines",
                            line=dict(color="blue", width=2),
                        )
                    )
                elif len(simplex) == 3:
                    faces.append(
                        go.Mesh3d(
                            x=pts[:, 0],
                            y=pts[:, 1],
                            z=pts[:, 2],
                            color="green",
                            opacity=0.4,
                        )
                    )

            x_range = [self.points[:, 0].min() - 1, self.points[:, 0].max() + 1]
            y_range = [self.points[:, 1].min() - 1, self.points[:, 1].max() + 1]
            z_range = [self.points[:, 2].min() - 0.5, self.points[:, 2].max() + 0.5]

            fig = go.Figure(data=[vertices] + edges + faces)
            fig.update_layout(
                width=1000,
                height=800,
                scene=dict(
                    xaxis=dict(title="X", range=x_range),
                    yaxis=dict(title="Y", range=y_range),
                    zaxis=dict(title="Z", range=z_range),
                    aspectmode="manual",
                    aspectratio={"x": 4, "y": 4, "z": 1},
                    camera=dict(eye=dict(x=3, y=3, z=2)),
                ),
                showlegend=False,
            )
            fig.show()
    return VietorisRipsComplex, np


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Example: Vietoris-Rips Complex on a Torus Point Cloud

    We generate a noisy sample of points lying approximately on a torus embedded in $\mathbb{R}^3$:
    """
    )
    return


@app.cell
def _(np):
    def generate_torus(R=7, r=1, m=50, n=15, noise=0.1, seed=42):
        np.random.seed(seed)
        u = np.linspace(0, 2 * np.pi, m)
        v = np.linspace(0, 2 * np.pi, n)
        u, v = np.meshgrid(u, v)
        x = (R + r * np.cos(v)) * np.cos(u) + np.random.normal(0, noise, u.shape)
        y = (R + r * np.cos(v)) * np.sin(u) + np.random.normal(0, noise, u.shape)
        z = r * np.sin(v) + np.random.normal(0, noise, u.shape)
        return list(zip(x.flatten(), y.flatten(), z.flatten()))


    point_cloud = generate_torus()
    return (point_cloud,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""And we can compute and plot the Rips complexes with different radius parameters. As the radius changes, the Vietoris-Rips complex gradually adds higher-dimensional simplices, revealing information about the underlying geometry and topology of the data."""
    )
    return


@app.cell
def _(VietorisRipsComplex, point_cloud):
    rips3d = VietorisRipsComplex(point_cloud, max_dimension=2)
    # rips3d.plot_complex(radius=.4, box_aspect=[4,4,1])
    # rips3d.plot_complex(radius=.6, box_aspect=[4,4,1])
    # rips3d.plot_complex(radius=.8, box_aspect=[4,4,1])
    # rips3d.plot_complex(radius=1.0, box_aspect=[4,4,1])
    # rips3d.plot_complex(radius=1.0, interactive=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    <div style="display: flex; flex-wrap: wrap; gap: 10px;">
      <img src="public/complex 04.png" style="width: 300px;"/>
      <img src="public/complex 06.png" style="width: 300px;"/>
      <img src="public/complex 08.png" style="width: 300px;"/>
      <img src="public/complex 10.png" style="width: 300px;"/>
      <img src="public/complex 3d.png" style="width: 300px;"/>
    </div>
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Note on performance

    The code presented above is designed for educational clarity, not computational efficiency. In particular, we directly enumerate all possible simplices using brute-force combinatorics (`itertools.combinations`), which scales exponentially in both the number of points and the simplex dimension. For real-world datasets (especially when working with hundreds or thousands of points), such naive enumeration becomes computationally infeasible even for moderate dimensions.

    For this reason, the figures displayed above are generated using precomputed complexes, and we simply show static images to illustrate the output.

    In practical TDA pipelines, highly optimized libraries are used to construct Vietoris-Rips complexes and compute persistent homology efficiently. Some widely used packages include:

    - `GUDHI` (Geometry Understanding in Higher Dimensions);
    - `Ripser` (extremely fast computation of Vietoris-Rips persistent homology);
    - `Giotto-tda`, ...

    These libraries implement sophisticated data structures and algorithms to avoid redundant computations and efficiently handle filtrations and persistence calculations.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Why We Omit Čech Complex Computation

    While the Čech complex provides a more “faithful” topological model (via the Nerve Theorem), it requires explicitly checking intersections of balls, which becomes computationally challenging even for moderate-sized datasets.

    In practice, the Vietoris-Rips complex is widely used because:

    - It is much easier to compute;
    - It captures similar qualitative topological features;
    - It allows efficient persistence computations for persistent homology.

    The Čech and Vietoris-Rips complexes are related via the following inclusions: $$\mathbb{C}^r(P) \subseteq \mathbb{VR}^r(P) \subseteq \mathbb{C}^{2r}(P).$$
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## The Limitation of Single Radius and the Idea of Filtrations

    As we can see in the above plots, a big drawback of building a simplicial complex at a single scale parameter $r$ is that the resulting complex depends heavily on this arbitrary choice. If $r$ is too small, the complex may be disconnected and fail to capture any meaningful structure. If $r$ is too large, the complex may quickly become contractible and lose all useful topological information.

    To address this, TDA works not with a single complex, but with a filtration, a nested sequence of complexes, indexed by scale parameter.

    For example, a Vietoris-Rips filtration is a family: $$\mathbb{VR}^{r_1}(P) \subseteq \mathbb{VR}^{r_2}(P) \subseteq \cdots \subseteq \mathbb{VR}^{r_n}(P)$$ as $r_1 \le r_2 \le \cdots \le r_n$.

    This allows us to track how topological features (connected components, loops, voids, etc.) appear and disappear as $r$ varies, a process known as persistent homology.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Types of Filtrations

    While we focus here on Vietoris-Rips filtrations (built from distances), in more general settings TDA uses various types of filtrations depending on the context:

    - Vietoris-Rips filtration: built from pairwise distances;
    - Čech filtration: based on intersections of metric balls;
    - Alpha complexes: based on Delaunay triangulation; often preferred in Euclidean spaces for better geometric approximation;
    - Witness complexes: approximate complexes for large-scale datasets using a subset of landmark points;
    - Sublevel filtrations: built from scalar functions or continuous measurements defined on a space;
    - Zigzag filtrations: allow simplices to both enter and leave the filtration as the parameter varies, useful for dynamic or time-varying data.

    Zigzag filtrations generalize the usual (nested) filtration framework and require more sophisticated algebraic machinery, but they allow TDA to handle non-monotonic data sequences. For example, streaming data, or situations where data points or simplices may both appear and disappear over time.
    """
    )
    return


if __name__ == "__main__":
    app.run()
