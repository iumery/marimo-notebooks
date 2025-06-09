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
    # An Illustrative Example: Topological Spaces, Continuity, and Homeomorphisms

    This notebook serves as a gentle prelude to some of the key concepts in Topological Data Analysis (TDA) by first exploring their foundations in classical topology. While most of the computational power in TDA lies in persistent homology and simplicial complexes, at the very heart of topology are spaces, open sets, continuous maps, and homeomorphisms.

    Here, we implement these concepts explicitly for finite sets, discrete toy models that strip away unnecessary technical complications but retain the core definitions. This exercise also highlights how one can implement topological notions entirely from scratch, without relying on any specialized TDA libraries.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Topological Spaces in Code

    We first define a `TopologicalSpace` class that models a topological space $(X, \mathcal{T})$, where:

    - $X$ is a set of points,
    - $\mathcal{T}$ is a collection of subsets of $X$ called the open sets,
    - and $\mathcal{T}$ satisfies the standard axioms: it contains the empty set and the whole space, is closed under arbitrary unions, and closed under finite intersections.

    Since we are using finite sets, we verify these conditions exhaustively.

    This direct check is feasible here, but computationally intractable for infinite or large-scale spaces, exactly why more efficient combinatorial models like simplicial complexes are used in practical TDA.
    """
    )
    return


@app.class_definition
class TopologicalSpace:
    def __init__(self, X, topology):
        """
        Initializes a topological space.

        Args:
            X: A set representing the underlying space.
            topology: A list of sets representing the topology (collection of open sets).

        Raises:
            TypeError: If X is not a set or topology is not a list of sets.
        """
        if not isinstance(X, set):
            raise TypeError("X must be a set.")
        if not isinstance(topology, list):
            raise TypeError("Topology must be a list of sets.")
        if not all(isinstance(U, set) for U in topology):
            raise TypeError("All elements of topology must be sets.")

        self.X = X
        self.topology = topology

        # Validate the provided topology
        assert (
            self._validate_topology()
        ), "Invalid topology: Topology must satisfy closure conditions."

    def _validate_topology(self):
        """
        Validates if the topology satisfies the basic properties of a topological space:
        - Contains the empty set and the whole space.
        - Closed under arbitrary unions.
        - Closed under finite intersections.

        Returns:
            bool: True if the topology is valid, False otherwise.
        """
        # Ensure the topology contains the empty set and the whole space
        if set() not in self.topology or self.X not in self.topology:
            return False

        # Check closure under unions and intersections using list checks
        for U in self.topology:
            for V in self.topology:
                if (U | V) not in self.topology or (U & V) not in self.topology:
                    return False
        return True


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Continuity

    We then define a `ContinuousFunction` class that models a continuous map between two topological spaces. The definition follows the usual "preimage" criterion: $$f : X \to Y\text{ is continuous if }\forall V \in \mathcal{T}_Y, f^{-1}(V) \in \mathcal{T}_X.$$

    The class explicitly computes the preimages of all open sets and verifies whether these are open in the domain topology.

    This concrete implementation shows how continuity is fundamentally a relationship between the open sets of the domain and codomain.
    """
    )
    return


@app.class_definition
class ContinuousFunction:
    def __init__(self, f, domain, codomain):
        """
        Initializes a continuous function between two topological spaces.

        Args:
            f: A function mapping elements from the domain to the codomain.
            domain: The topological space that serves as the domain of f.
            codomain: The topological space that serves as the codomain of f.
        """
        self.f = f
        self.domain = domain
        self.codomain = codomain

    def is_continuous(self):
        """
        Checks if the function is continuous by verifying that the preimage of every open set
        in the codomain is open in the domain.

        Returns:
            bool: True if the function is continuous, False otherwise.
        """
        return all(self._preimage_is_open(V) for V in self.codomain.topology)

    def _preimage_is_open(self, V):
        """
        Checks if the preimage of an open set V in the codomain is open in the domain.

        Args:
            V: A set in the topology of the codomain.

        Returns:
            bool: True if the preimage of V is open in the domain, False otherwise.
        """
        # Compute the preimage of the set V
        preimage = {x for x in self.domain.X if self.f(x) in V}
        # Check if the preimage is open in the domain
        return preimage in self.domain.topology


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Homeomorphisms

    Finally, we introduce the notion of homeomorphism: a bijective continuous function whose inverse is also continuous. Homeomorphisms capture the intuitive notion of "topological equivalence", spaces that have the same qualitative shape or structure.
    """
    )
    return


@app.class_definition
class Homeomorphism:
    def __init__(self, f, f_inv, space1, space2):
        """
        Initializes a homeomorphism (a bijective continuous function with a continuous inverse)
        between two topological spaces.

        Args:
            f: A function mapping from space1 to space2.
            f_inv: The inverse function mapping from space2 to space1.
            space1: The first topological space.
            space2: The second topological space.
        """
        self.f = f
        self.f_inv = f_inv
        self.space1 = space1
        self.space2 = space2

    def is_homeomorphism(self):
        """
        Checks if the function f and its inverse f_inv form a homeomorphism by verifying:
        - f is continuous.
        - f_inv is continuous.

        Returns:
            bool: True if the function f is a homeomorphism, False otherwise.
        """
        # Check continuity of f and f_inv using the ContinuousFunction class
        is_f_continuous = ContinuousFunction(
            self.f, self.space1, self.space2
        ).is_continuous()
        is_f_inv_continuous = ContinuousFunction(
            self.f_inv, self.space2, self.space1
        ).is_continuous()

        # A homeomorphism requires both f and f_inv to be continuous
        return is_f_continuous and is_f_inv_continuous


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Example

    We construct two toy spaces:

     - $X = \lbrace 1, 2, 3 \rbrace$ with topology $\mathcal{T}_X = \lbrace \emptyset, \lbrace 1 \rbrace, \lbrace 1, 2 \rbrace, X \rbrace$;
     - $Y = \lbrace a, b, c \rbrace$ with topology $\mathcal{T}_Y = \lbrace \emptyset, \lbrace a \rbrace, \lbrace a, b \rbrace, Y \rbrace$,

    and define a bijection between them by:

    $f(1) = a$, $f(2) = b$, $f(3) = c$.

    The code verifies that this mapping is indeed a homeomorphism.
    """
    )
    return


@app.cell
def _():
    # Example usage of the topological space, continuous function, and homeomorphism classes

    # Define a topological space X
    X = {1, 2, 3}
    topology_X = [set(), {1}, {1, 2}, X]
    space_X = TopologicalSpace(X, topology_X)

    # Define a topological space Y
    Y = {"a", "b", "c"}
    topology_Y = [set(), {"a"}, {"a", "b"}, Y]
    space_Y = TopologicalSpace(Y, topology_Y)

    # Define a bijective function f from X to Y
    def f(x):
        """
        Function mapping elements of space X to space Y.
        """
        mapping = {1: "a", 2: "b", 3: "c"}
        return mapping[x]

    # Define the inverse of f
    def f_inv(y):
        """
        Inverse function mapping elements of space Y back to space X.
        """
        inverse_mapping = {"a": 1, "b": 2, "c": 3}
        return inverse_mapping[y]

    # Check if f and f_inv form a homeomorphism between space_X and space_Y
    homeo_f_X_Y = Homeomorphism(f, f_inv, space_X, space_Y)
    print(
        homeo_f_X_Y.is_homeomorphism()
    )  # Output: True or False depending on the topology
    return f, f_inv


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Non-Example

    The following is a non-example: $M$ and $N$, although have the exact same elements with $X$ and $Y$ together with the same functions, are not homeomorphic to each other as the underlying topology has changed. For example, preimage of the set $\lbrace a \rbrace$ under $f$ is $\lbrace 1 \rbrace$ which is not a member of $\mathcal{T}_M$.
    """
    )
    return


@app.cell
def _(f, f_inv):
    # Example usage of the topological space, continuous function, and homeomorphism classes

    # Define a topological space M
    M = {1, 2, 3}
    topology_M = [set(), {1, 2}, {2, 3}, {2}, M]
    space_M = TopologicalSpace(M, topology_M)

    # Define a topological space N
    N = {"a", "b", "c"}
    topology_N = [set(), {"a"}, {"a", "b"}, N]
    space_N = TopologicalSpace(N, topology_N)

    # Check if f and f_inv form a homeomorphism between space_M and space_N
    homeo_f_M_N = Homeomorphism(f, f_inv, space_M, space_N)
    print(homeo_f_M_N.is_homeomorphism())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Why Start with This?

    While these examples are simple and somewhat trivial (which is always the case in finite discrete settings), they serve an important pedagogical role:

    - They allow us to see how the formal axioms operate algorithmically;
    - They give us insight into why TDA relies on combinatorial models such as simplicial complexes, filtrations, and persistent homology, rather than trying to work with open sets directly.

    In practical TDA applications, one typically works with metric data, filtrations, and algebraic constructions of homology.
    """
    )
    return


if __name__ == "__main__":
    app.run()
