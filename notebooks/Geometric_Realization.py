import marimo

__generated_with = "0.13.15"
app = marimo.App()


@app.cell(hide_code=True)
def _():
    import marimo as mo

    return (mo,)


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


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Abstract Simplicial Complexes and Geometric Realization

    In topological data analysis (TDA), we often construct simplicial complexes from data, but it’s important to distinguish between two closely related notions:

    - Abstract simplicial complexes: purely combinatorial structures.
    - Geometric realizations: embeddings of these combinatorial structures into Euclidean space.

    This notebook provides a simple illustration of both concepts.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Abstract Simplicial Complexes

    Given a finite set of vertices $V$, an abstract simplicial complex is a collection of finite subsets of $V$ that is closed under inclusion. That is, if $\sigma \subseteq V$ is in the complex, then every subset of $\sigma$ is also in the complex.

    In this notebook, we simply construct the full simplex on a given vertex set: that is, the set of all possible non-empty subsets of $V$.

    For example, with $5$ vertices $\{A, B, C, D, E\}$, the full simplicial complex consists of:

    - $5$ vertices ($0$-simplices),
    - $10$ edges ($1$-simplices),
    - $10$ triangles ($2$-simplices),
    - $5$ tetrahedra ($3$-simplices),
    - $1$ full $4$-simplex (the entire vertex set).

    This is simply the combinatorial power set (minus the empty set).
    """
    )
    return


@app.cell
def _():
    import itertools
    import numpy as np

    def is_simplex(vertices, subset):
        """
        Check if a subset is a valid simplex (non-empty subset of the vertex set).
        """
        return set(subset).issubset(vertices) and len(subset) > 0

    def construct_simplicial_complex(vertices):
        """
        Construct the full simplicial complex consisting of all non-empty subsets of vertices.
        """
        simplicial_complex = []
        for r in range(1, len(vertices) + 1):
            for subset in itertools.combinations(vertices, r):
                simplicial_complex.append(list(subset))
        return simplicial_complex

    def geometric_realization(simplex, dimension):
        """
        Perform geometric realization of a simplex into Euclidean space.
        (Random placement for illustration.)
        """
        return np.random.rand(len(simplex), dimension)

    def combinatorial_optimization(simplicial_complex, objective_func):
        """
        Find the simplex minimizing a given objective function.
        """
        optimal_value = np.inf
        optimal_solution = None
        for simplex in simplicial_complex:
            value = objective_func(simplex)
            if value < optimal_value:
                optimal_value = value
                optimal_solution = simplex
        return optimal_solution, optimal_value

    def dummy_objective(simplex):
        """
        Dummy objective function: minimize the size of the simplex.
        """
        return len(simplex)

    return (
        combinatorial_optimization,
        construct_simplicial_complex,
        dummy_objective,
        geometric_realization,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Geometric Realization

    An abstract simplicial complex can be embedded into Euclidean space to obtain a geometric realization. This allows us to:

    - Visualize simplices as actual geometric objects (points, edges, triangles, tetrahedra, etc);
    - Perform computations in geometry (e.g., barycentric coordinates, volumes, embeddings).

    In this notebook, we perform a simple random geometric realization of simplices into Euclidean space, simply assigning random coordinates to each vertex for illustration purposes.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Combinatorial Optimization Example

    We also introduce a simple toy example of combinatorial optimization over a simplicial complex: Given an objective function (here: minimizing the size of a simplex), we search for the simplex in the complex that minimizes this function. Of course, with this dummy objective function, the optimizer simply returns a $0$-simplex (vertex).

    In more realistic settings, one could design much more meaningful objective functions depending on the application (e.g., minimizing volume, maximizing weight, minimizing persistence, etc).
    """
    )
    return


@app.cell
def _(
    combinatorial_optimization,
    construct_simplicial_complex,
    dummy_objective,
    geometric_realization,
):
    # Example usage:

    vertices = ["A", "B", "C", "D", "E"]
    simplicial_complex = construct_simplicial_complex(vertices)

    optimal_solution, optimal_value = combinatorial_optimization(
        simplicial_complex, dummy_objective
    )

    geometric = geometric_realization(["A", "B"], 2)

    print("Simplicial Complex:", simplicial_complex)
    print("Optimal Solution:", optimal_solution)
    print("Optimal Value:", optimal_value)
    print("Geometric Realization of Simplex:", geometric)
    return


if __name__ == "__main__":
    app.run()
