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
    # Sheaf Theory: A Simple Introduction

    In this notebook, we give a first glimpse of sheaf theory using a simple example over a simplicial complex.

    While topological data analysis often studies global topological invariants (like homology groups), sheaf theory allows us to systematically handle **local data attached to spaces** and study how this local information can (or cannot) be assembled into global information.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## What is a Sheaf?

    Roughly speaking, a sheaf is a data structure that assigns:

    - Local data to open sets (or simplices, in our discrete setting).
    - Restriction maps that allow data on larger sets to be restricted to smaller subsets.
    - Consistency conditions that govern how local data can be glued together into global data.

    In practice, sheaves are used to model situations where different parts of a system carry partial information that must be compatible where they overlap.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Sheaf Model in This Notebook

    We model a sheaf over a simplicial complex.

    - The underlying space is a simplicial complex: a set of vertices, edges, and higher-dimensional simplices;
    - Local data is assigned to each simplex as a list of values, one for each vertex of that simplex;
    - A restriction map allows data on higher-dimensional simplices to be projected down to faces by selecting only the data corresponding to shared vertices;
    - The sheaf is **consistent** if, for every simplex and its faces, the restricted data matches the local data assigned to the faces.

    In this simple model:

    - Each simplex carries values indexed by its vertices;
    - The restriction simply discards data associated with vertices not in the lower-dimensional face;
    - Inconsistency occurs if these projections do not match the already assigned data on lower-dimensional faces.
    """
    )
    return


@app.cell
def _():
    class sheaf_data:
        def __init__(self, simplicial_complex):
            """
            Initialize the sheaf with a given simplicial complex.
            Args:
                simplicial_complex (list of tuples): The simplicial complex, a collection of simplices.
            """
            self.simplicial_complex = (
                simplicial_complex  # The simplicial complex structure
            )
            self.data = {}  # Dictionary to store data assigned to simplices

        def assign_data(self, simplex, local_data):
            """
            Assign local data to a specific simplex.
            Args:
                simplex (tuple): A simplex (e.g., (1, 2)).
                local_data (list): Data associated with this simplex.
            """
            self.data[simplex] = local_data

        def restriction_map(self, simplex1, simplex2):
            """
            Restrict data from a higher-dimensional simplex (simplex1) to a lower-dimensional simplex (simplex2).
            Args:
                simplex1 (tuple): The source simplex (e.g., (1, 2, 3)).
                simplex2 (tuple): The target simplex, a face of simplex1 (e.g., (1, 2)).
            Returns:
                dict or None: The restricted data if simplex2 is a face of simplex1, else None.
            """
            if set(simplex2).issubset(
                set(simplex1)
            ):  # Check if simplex2 is a face of simplex1
                # Restrict data by projecting onto the shared vertices
                restricted_data = {
                    vertex: self.data[simplex1][i]
                    for i, vertex in enumerate(simplex1)
                    if vertex in simplex2
                }
                return restricted_data
            return None  # Return None if simplex2 is not a face of simplex1

        def check_consistency(self):
            """
            Check consistency of the sheaf by verifying if the restriction maps align with the assigned data.
            Returns:
                bool: True if the sheaf is consistent, False otherwise.
            """
            for (
                sup
            ) in (
                self.simplicial_complex
            ):  # Iterate over all simplices (sup: higher simplex)
                for (
                    sub
                ) in (
                    self.simplicial_complex
                ):  # Iterate over all simplices (sub: lower simplex)
                    if (
                        set(sub).issubset(set(sup)) and sup != sub
                    ):  # Check if sub is a face of sup
                        # Restrict data from sup to sub
                        restricted_data = self.restriction_map(sup, sub)
                        if restricted_data:  # If restriction is valid
                            # Construct sub's actual data for comparison
                            sub_data = {
                                vertex: self.data[sub][i]
                                for i, vertex in enumerate(sub)
                            }
                            if restricted_data != sub_data:  # Check consistency
                                return False  # Inconsistent if restriction does not match sub's data
            return True  # Return True if all checks pass

    def construct_sheaf(simplicial_complex, local_data):
        """
        Construct a sheaf by assigning local data to simplices in the simplicial complex.
        Args:
            simplicial_complex (list of tuples): The simplicial complex.
            local_data (list of lists): The local data for each simplex.
        Returns:
            sheaf_data: The constructed sheaf.
        """
        sheaf = sheaf_data(simplicial_complex)  # Initialize a sheaf
        for simplex, data in zip(
            simplicial_complex, local_data
        ):  # Assign data to each simplex
            sheaf.assign_data(simplex, data)
        return sheaf  # Return the constructed sheaf

    def find_global_section(sheaf):
        """
        Find a global section of the sheaf if it is consistent.
        Args:
            sheaf (sheaf_data): The sheaf to evaluate.
        Returns:
            dict or str: The global section (data on all simplices) if consistent, else a message.
        """
        if sheaf.check_consistency():  # Check if the sheaf is consistent
            # Return the global section as a dictionary
            return {k: v for k, v in sheaf.data.items()}
        else:
            return "Inconsistency detected."  # Return an error message if inconsistent

    return construct_sheaf, find_global_section


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Example 1: Consistent Sheaf

    In this example, the simplicial complex consists of:

    - Vertices: $1, 2, 3$;
    - Edges: $(1,2), (2,3), (1,3)$,
    - Triangle: $(1,2,3)$.

    We assign local data as:
    - Edge $(1,2)$: $[10, 20]$ (meaning vertex $1$ has $10$, vertex $2$ has $20$).
    - Edge $(2,3)$: $[20, 30]$.
    - Edge $(1,3)$: $[10, 30]$.
    - Triangle $(1,2,3)$: $[10, 20, 30]$.

    The restriction maps project data from higher simplices to their faces:
    - For example, restricting $[10, 20, 30]$ from the triangle to edge $(1,2)$ gives $[10, 20]$, which matches the assigned data on $(1,2)$.
    - Similar checks succeed for all faces.

    Since all restriction maps agree with assigned data, the sheaf is consistent, and we successfully obtain a global section: the full assignment of data across all simplices.
    """
    )
    return


@app.cell
def _(construct_sheaf, find_global_section):
    # Example Usage
    simplicial_complex_1 = [
        (1, 2),  # Edge (1, 2)
        (2, 3),  # Edge (2, 3)
        (1, 3),  # Edge (1, 3)
        (1, 2, 3),  # Triangle (1, 2, 3)
    ]
    local_data_1 = [
        [10, 20],  # Data on edge (1, 2)
        [20, 30],  # Data on edge (2, 3)
        [10, 30],  # Data on edge (1, 3)
        [10, 20, 30],  # Data on triangle (1, 2, 3)
    ]

    # Construct the sheaf
    example_sheaf_1 = construct_sheaf(simplicial_complex_1, local_data_1)

    # Find the global section
    global_section_1 = find_global_section(example_sheaf_1)

    # Print the global section or inconsistency message
    print(global_section_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Example 2: Inconsistent Sheaf

    The simplicial complex is the same as before.

    This time, we assign local data:
    
    - Edge $(1,2)$: $[10, 20]$.
    - Edge $(2,3)$: $[20, -30]$.
    - Edge $(1,3)$: $[10, 30]$.
    - Triangle $(1,2,3)$: $[10, 20, 30]$.

    The difference lies in the edge $(2,3)$: its assigned data is $[20, -30]$ instead of $[20, 30]$.

    When we apply the restriction map from the triangle $(1,2,3)$ to edge $(2,3)$, we obtain $[20, 30]$. This no longer matches the assigned data $[20, -30]$ on edge $(2,3)$.

    Thus, the sheaf fails the consistency check. There is no global section that respects both the assigned data and the restriction maps.
    """
    )
    return


@app.cell
def _(construct_sheaf, find_global_section):
    # Example Usage
    simplicial_complex_2 = [
        (1, 2),  # Edge (1, 2)
        (2, 3),  # Edge (2, 3)
        (1, 3),  # Edge (1, 3)
        (1, 2, 3),  # Triangle (1, 2, 3)
    ]
    local_data_2 = [
        [10, 20],  # Data on edge (1, 2)
        [20, -30],  # Data on edge (2, 3)
        [10, 30],  # Data on edge (1, 3)
        [10, 20, 30],  # Data on triangle (1, 2, 3)
    ]

    # Construct the sheaf
    example_sheaf_2 = construct_sheaf(simplicial_complex_2, local_data_2)

    # Find the global section
    global_section_2 = find_global_section(example_sheaf_2)

    # Print the global section or inconsistency message
    print(global_section_2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## What Does Inconsistency Mean in Practice?

    Intuitively, inconsistency means that local pieces of data cannot be glued together into a coherent global picture. The data assigned to lower-dimensional simplices is incompatible with the data induced from higher-dimensional ones. In many applications (sensor networks, distributed systems, multi-scale data), inconsistency signals conflicts or contradictions in local observations.

    In this simplified example, you can think of it as: The triangle “wants” vertex $3$ to have value $30$. The edge $(2,3)$ instead claims vertex $3$ has value $-30$. Both cannot be true simultaneously, so no global assignment exists that satisfies all local constraints.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## How Sheaf Theory Relates to TDA

    While much of topological data analysis focuses on global invariants like homology or persistent homology, sheaf theory offers a complementary perspective. It provides a flexible way to encode **local data constraints** over a topological space or a simplicial complex.

    In TDA, sheaves can model:

    - Local measurements attached to different regions of data.
    - Multi-scale or hierarchical data integration.
    - Compatibility conditions between local computations.
    - Obstructions to building global structures from local information.

    Sheaves have been applied in sensor networks, distributed systems, multiscale geometry, and even generalized persistent homology frameworks. They allow TDA to go beyond simply measuring the "shape" of data, and begin addressing how information is organized and consistent across different parts of a dataset.
    """
    )
    return


if __name__ == "__main__":
    app.run()
