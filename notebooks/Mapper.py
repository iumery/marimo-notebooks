import marimo

__generated_with = "0.13.15"
app = marimo.App()


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Mapper Algorithm

    In this notebook, we introduce one of the most widely known tools in topological data analysis: the Mapper algorithm.

    Mapper is a method for extracting a simplified topological summary (usually a graph) from high-dimensional data. Unlike simplicial complexes such as Vietoris-Rips or Čech, Mapper can be thought of as a combination of:

    - Filtering (via a chosen lens function)
    - Covering (via intervals or overlapping bins)
    - Clustering (inside each bin)
    - Nerve construction (on the clustered cover)
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Basic Idea of Mapper

    The Mapper algorithm takes as input:

    - A point cloud in some metric space.
    - A filter function (or lens) that assigns scalar values to the points.
    - A covering of the filter function's range (usually overlapping intervals).
    - A clustering algorithm to partition points inside each interval.

    It outputs a simplicial complex (often just a 1-skeleton graph) where:

    - Vertices correspond to clusters.
    - Edges are drawn between overlapping clusters.

    Mapper can reveal global structure such as loops, branches, and connected components, even in noisy high-dimensional data.
    """
    )
    return


@app.cell
def _():
    import numpy as np
    import networkx as nx
    import matplotlib.pyplot as plt
    from sklearn.cluster import DBSCAN
    return DBSCAN, np, nx, plt


@app.cell
def _(np, plt):
    # Generate a random set of points that look like '\phi' (a straight vertical line through the center)

    # Number of points for the outer circle and inner "stroke"
    num_outer = 400
    num_inner = 200

    # Outer circle with reduced radius
    theta_outer = np.linspace(0, 20 * np.pi, num_outer)
    x_outer = 15 * np.cos(theta_outer)
    y_outer = 10 * np.sin(theta_outer)

    # Inner "stroke" of phi (straight vertical line through center)
    y_inner = np.linspace(-20, 20, num_inner)
    x_inner = 0 * np.ones(num_inner)

    # Add randomness to each coordinate
    randomness = 0.5
    np.random.seed(42)
    x_outer += np.random.normal(0, randomness, num_outer)
    y_outer += np.random.normal(0, randomness, num_outer)
    x_inner += np.random.normal(0, randomness, num_inner)
    y_inner += np.random.normal(0, randomness, num_inner)

    # Combine both sets of points into one list of tuples
    point_cloud = list(zip(np.concatenate((x_outer, x_inner)), np.concatenate((y_outer, y_inner))))

    # Plot to visualize
    x_coords, y_coords = zip(*point_cloud)
    plt.scatter(x_coords, y_coords, s=5)
    plt.gca().set_aspect("equal", adjustable="box")
    plt.show()
    return (point_cloud,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    In the above code, we simulate data sampled from a circle in the plane, with added Gaussian noise. This provides a simple dataset with a clear one-dimensional topological structure (a loop), making it a good candidate for demonstrating Mapper.

    The data points lie approximately along the unit circle, but are randomly perturbed to simulate measurement noise often found in real-world data.
    """
    )
    return


@app.cell
def _(np, plt, point_cloud):
    # Different ways to normalize a point cloud


    # 1. Min-Max Normalization (Scaling to [0, 1] range)
    def min_max_normalize(tuples):
        array = np.array(tuples)
        min_vals = array.min(axis=0)
        max_vals = array.max(axis=0)
        range_vals = np.where(max_vals - min_vals == 0, 1, max_vals - min_vals)
        normalized_array = (array - min_vals) / range_vals
        return [tuple(point) for point in normalized_array]


    # 2. Standardization (Z-score Normalization)
    def standardize(tuples):
        array = np.array(tuples)
        mean_vals = array.mean(axis=0)
        std_vals = array.std(axis=0)
        std_vals = np.where(std_vals == 0, 1, std_vals)
        standardized_array = (array - mean_vals) / std_vals
        return [tuple(point) for point in standardized_array]


    # 3. Mean Normalization (Centers data to approximately [-0.5, 0.5])
    def mean_normalize(tuples):
        array = np.array(tuples)
        mean_vals = array.mean(axis=0)
        min_vals = array.min(axis=0)
        max_vals = array.max(axis=0)
        range_vals = np.where(max_vals - min_vals == 0, 1, max_vals - min_vals)
        normalized_array = (array - mean_vals) / range_vals
        return [tuple(point) for point in normalized_array]


    # 4. Unit Vector Normalization (Normalize each vector to unit length)
    def unit_vector_normalize(tuples):
        array = np.array(tuples)
        norms = np.linalg.norm(array, axis=1, keepdims=True)
        norms = np.where(norms == 0, 1, norms)
        normalized_array = array / norms
        return [tuple(point) for point in normalized_array]


    # 5. Robust Scaling (Using Median and IQR)
    def robust_scale(tuples):
        array = np.array(tuples)
        median_vals = np.median(array, axis=0)
        q75, q25 = np.percentile(array, [75, 25], axis=0)
        iqr_vals = np.where((q75 - q25) == 0, 1, q75 - q25)
        scaled_array = (array - median_vals) / iqr_vals
        return [tuple(point) for point in scaled_array]


    # 6. Log Transformation (For skewed data)
    def log_transform(tuples, shift_constant=1e-5):
        array = np.array(tuples)
        min_val = array.min()
        if min_val <= 0:
            array += abs(min_val) + shift_constant
        log_transformed_array = np.log(array)
        return [tuple(point) for point in log_transformed_array]


    # 7. Max-Abs Scaling (Scaling each feature to [-1, 1] by its maximum absolute value)
    def max_abs_scale(tuples):
        array = np.array(tuples)
        max_abs_vals = np.max(np.abs(array), axis=0)
        max_abs_vals = np.where(max_abs_vals == 0, 1, max_abs_vals)
        scaled_array = array / max_abs_vals
        return [tuple(point) for point in scaled_array]


    # 8. Decimal Scaling (Scaling by a power of 10 to fit [-1, 1])
    def decimal_scale(tuples):
        array = np.array(tuples)
        max_abs_vals = np.max(np.abs(array), axis=0)
        j_vals = np.ceil(np.log10(np.where(max_abs_vals == 0, 1, max_abs_vals)))
        scaled_array = array / (10**j_vals)
        return [tuple(point) for point in scaled_array]


    normalized_point_cloud = min_max_normalize(point_cloud)
    x_coords_normal, y_coords_normal = zip(*normalized_point_cloud)
    plt.scatter(x_coords_normal, y_coords_normal, s=5)
    plt.gca().set_aspect("equal", adjustable="box")
    plt.show()
    return (normalized_point_cloud,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Before running Mapper, we normalize the data so that both coordinates lie approximately in the interval $[0, 1]$. This step ensures that:

    - The filter function operates on a consistent scale.
    - The cover intervals are well-aligned to the data range.
    - The clustering threshold works reasonably across dimensions.

    Normalization is a very common preprocessing step in real-world TDA pipelines to make parameter choices more meaningful.

    Different normalization methods are provided, we utilize the min/max normalization in the example in this notebook.
    """
    )
    return


@app.cell
def _(np):
    def divide_unit_n_cube(n, m, overlap=0.2):
        """
        Divide the n-dimensional unit cube into smaller overlapping subcubes.

        Args:
            n: The number of dimensions (e.g., n = 2 for a 2D unit square).
            m: The number of divisions per dimension (i.e., how many smaller cubes to divide each axis).
            overlap: The fraction of overlap between neighboring subcubes (default is 0.2).

        Returns:
            A list of tuples where each tuple contains the lower and upper bounds of the subcubes
            in each dimension.
        """
        # Define the step size for each division of the unit cube
        step = 1.0 / m  # Step size between adjacent subcubes
        overlap = overlap * step  # Adjust overlap relative to the step size

        # Create grid points for each dimension, ensuring the divisions are uniform
        grid_points = [np.linspace(0, 1 - step, m) for _ in range(n)]

        # List to hold the bounds of all small subcubes
        small_cubes = []

        # Iterate over all possible grid points (starting positions of the small cubes)
        for indices in np.ndindex(*[m] * n):
            cube_bounds = []
            # Iterate through each dimension and calculate lower and upper bounds
            for dim, idx in enumerate(indices):
                lower_bound = grid_points[dim][idx] - overlap  # Apply overlap
                upper_bound = lower_bound + step + 2 * overlap  # Extend by step and overlap
                cube_bounds.append((lower_bound, upper_bound))  # Store bounds for this dimension
            small_cubes.append(tuple(cube_bounds))  # Add the bounds as a subcube

        return small_cubes  # Return the list of small subcubes


    def dummy_process(point):
        """
        Dummy function for processing a point.

        Args:
            point: A point in the input space.

        Returns:
            The same point (identity function).
        """
        return point


    def projection_process(point):
        """
        Project the input point to a lower-dimensional space.

        In this case, it maps (x, y) -> (y,), projecting the xy-coordinates to the y-coordinate.

        Args:
            point: A tuple representing a point in higher-dimensional space.

        Returns:
            A tuple representing the projected point (in this case, just the y-coordinate).
        """
        return (point[1],)  # Return the second component of the point as the projection


    def preimage_cover(point_cloud, cover_codomain, process_function):
        """
        Compute the preimage of a cover in the codomain under a given mapping function.

        This function takes a point cloud, applies a mapping (process function), and assigns
        each point to the cover elements in the codomain based on its image.

        Args:
            point_cloud: A list of points in the original space (domain).
            cover_codomain: A list of subcubes in the codomain (created by `divide_unit_n_cube`).
            process_function: A function that maps points from the domain to the codomain.

        Returns:
            A dictionary where the keys are elements of the codomain (subcubes), and the values
            are lists of points from the point cloud that map into each corresponding subcube.
        """
        # Initialize a dictionary to store the points assigned to each subcube in the codomain
        cover_domain = {item: [] for item in cover_codomain}

        # Iterate through all points in the point cloud
        for point in point_cloud:
            # Apply the process function to map the point to the codomain
            image = process_function(point)

            # Check which subcubes in the codomain contain the image of the point
            for item in cover_codomain:
                for i in range(len(item)):
                    # Check if the image falls within the bounds of the subcube in the ith dimension
                    if item[i][0] < image[i] < item[i][1]:
                        pass  # Point is inside this subcube for this dimension
                    else:
                        continue  # Skip this subcube if the point falls outside the bounds

                    # If all dimensions are satisfied, assign the point to this subcube
                    if i == len(item) - 1:
                        cover_domain[item].append(point)

        return cover_domain  # Return the dictionary mapping subcubes to preimage points
    return divide_unit_n_cube, preimage_cover, projection_process


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    In this example, we use a simple coordinate projection (the first coordinate) as the filter function. In general, any scalar-valued function can serve as a filter, including:

    - Density estimators
    - PCA projections
    - Distance to landmark sets
    - Eccentricity functions
    - Domain-specific measurements

    Choosing an appropriate filter function is one of the key modeling decisions when using Mapper.
    """
    )
    return


@app.cell
def _(
    divide_unit_n_cube,
    normalized_point_cloud,
    plt,
    preimage_cover,
    projection_process,
):
    # Example usage of the functions
    n = 1  # Number of dimensions (1D unit interval)
    m = 6  # Number of divisions per dimension (6 divisions of the unit interval)
    cover_codomain = divide_unit_n_cube(n, m)  # Divide the unit interval into overlapping subintervals

    # Assume `normalized_point_cloud` is a list of points in the original space (e.g., a 2D point cloud)
    cover_domain = preimage_cover(normalized_point_cloud, cover_codomain, projection_process)

    # Create a figure with a specific size for the plot
    plt.figure(figsize=(6, 6))

    # Loop through each key-value pair in cover_domain
    # First, plot the points for even-indexed covers
    for key_group, values_group in cover_domain.items():
        index = list(cover_domain.keys()).index(key_group)  # Get the index of the key in the dictionary
        if index % 2 == 0:  # Handle even-indexed covers
            # Separate the x and y coordinates from the values (assumed to be 2D points)
            x_coords_group, y_coords_group = zip(*values_group)
            # Plot the points for this cover with the specified color
            plt.scatter(
                x_coords_group,
                y_coords_group,
                s=30,
                c=["#800080", "#90EE90"][index % 2],
                alpha=0.5,
                label=f"{index}-th cover",
            )

    # Loop again for odd-indexed covers (this ensures they are plotted on top of the even-indexed points)
    for key_group, values_group in cover_domain.items():
        index = list(cover_domain.keys()).index(key_group)  # Get the index of the key in the dictionary
        if index % 2 == 1:  # Handle odd-indexed covers
            # Separate the x and y coordinates from the values (assumed to be 2D points)
            x_coords_group, y_coords_group = zip(*values_group)
            # Plot the points for this cover with the specified color
            plt.scatter(
                x_coords_group,
                y_coords_group,
                s=30,
                c=["#800080", "#90EE90"][index % 2],
                alpha=0.5,
                label=f"{index}-th cover",
            )

    # Add a dummy point with a different color and label to indicate overlapping regions
    # (Since there is no actual computation of overlapping points in this code)
    plt.scatter([-10], [-10], s=30, c="#AAB5A6", label="Overlapping")

    # Add a legend to the plot to show which cover corresponds to which color
    plt.legend()

    # Ensure the aspect ratio of the plot is equal
    plt.gca().set_aspect("equal", adjustable="box")

    # Set the x and y limits of the plot to match the unit square (0 to 1)
    plt.xlim(-0.1, 1.1)
    plt.ylim(-0.1, 1.2)

    # Display the final plot
    plt.show()
    return (cover_domain,)


@app.cell
def _(DBSCAN, cover_domain, plt):
    def dbscan_clustering(points, eps=0.1, min_samples=5):
        """
        Perform DBSCAN clustering on a set of points.

        DBSCAN (Density-Based Spatial Clustering of Applications with Noise) groups together points
        that are close to each other (within 'eps' distance) and marks points as noise if they don't
        meet the 'min_samples' requirement.

        Args:
            points: A list or array of points to cluster.
            eps: The maximum distance between two points to be considered in the same neighborhood (default: 0.1).
            min_samples: The minimum number of points required to form a dense region (default: 5).

        Returns:
            clusters: A dictionary where the keys are cluster labels and the values are lists of points in each cluster.
        """
        # Perform DBSCAN clustering
        db = DBSCAN(eps=eps, min_samples=min_samples)
        labels = db.fit_predict(points)  # Fit the model and get cluster labels

        # Organize the points into clusters based on their labels
        clusters = {}
        for label in set(labels):  # Iterate over unique labels (clusters)
            clusters[label] = [point for point, l in zip(points, labels) if l == label]

        return clusters  # Return the clusters (including noise points if any)


    # Example: Choose a specific cover to cluster (e.g., the 3rd cover)
    k = 3
    k = k % len(cover_domain)  # Ensure k is within the range of the cover domain
    cover_points = cover_domain[list(cover_domain.keys())[k]]  # Select the points from the k-th cover

    # Perform DBSCAN clustering on the selected cover's points
    clusters_dbscan = dbscan_clustering(cover_points)

    # Define a list of colors to use for plotting clusters (extendable if needed)
    colors = ["r", "g", "b", "y", "c", "m", "k"]

    # Ensure enough colors for the number of clusters
    num_clusters = len(set(clusters_dbscan.keys()))
    if num_clusters > len(colors):
        colors = plt.cm.get_cmap("tab10", num_clusters)  # Dynamically generate colors if needed

    # Create a plot to visualize the clusters
    plt.figure(figsize=(5, 5))

    # Plot each cluster with a different color
    for key, values in clusters_dbscan.items():
        if values:  # Ensure the cluster is not empty
            x_coords_emp, y_coords_emp = zip(*values)  # Separate the x and y coordinates
            if isinstance(colors, list):
                # Use pre-defined colors if available
                plt.scatter(
                    x_coords_emp,
                    y_coords_emp,
                    s=30,
                    c=colors[key % len(colors)],
                    alpha=0.5,
                    label=f"{key}-th group",
                )
            else:
                # Use dynamically generated colors if necessary
                plt.scatter(
                    x_coords_emp,
                    y_coords_emp,
                    s=30,
                    c=[colors(key)],
                    alpha=0.5,
                    label=f"{key}-th group",
                )

    # Add a legend to show which cluster corresponds to which color
    plt.legend()

    # Set the aspect ratio of the plot to be equal
    plt.gca().set_aspect("equal", adjustable="box")

    # Set the limits for x and y axes to match the unit square (0 to 1)
    plt.xlim(-0.1, 1.1)
    plt.ylim(0.3, 1)

    # Display the plot
    plt.show()
    return (dbscan_clustering,)


@app.cell
def _(cover_domain, dbscan_clustering, nx, plt):
    # Dictionary to store all flattened clusters across different covers
    flat_clusters = {}

    # Counter to ensure unique keys for each cluster
    for outer_key, points in cover_domain.items():
        # Perform DBSCAN clustering on the points in each cover
        clusters = dbscan_clustering(points)

        # Flatten each cluster into the final dictionary `flat_clusters`
        for cluster_label, cluster_points in clusters.items():
            # Create a unique key for each cluster (combining the cover key and cluster label)
            unique_key = f"{outer_key}_cluster_{cluster_label}"
            flat_clusters[unique_key] = cluster_points

    # Initialize an empty graph to represent cluster intersections
    G = nx.Graph()

    # Step 1: Add a node for each cluster in `flat_clusters`
    for cluster_key in flat_clusters:
        G.add_node(cluster_key)

    # Step 2: Add edges between clusters that have non-empty intersections
    for key1, cluster1 in flat_clusters.items():
        for key2, cluster2 in flat_clusters.items():
            # Avoid duplicate edges and self-loops
            if key1 < key2:
                # Check if the intersection of cluster1 and cluster2 is non-empty
                if set(cluster1).intersection(cluster2):
                    G.add_edge(key1, key2)

    # Step 3: Set node sizes proportional to the size of each cluster
    # Each node size is proportional to the number of points in the cluster (scaled by 10)
    node_sizes = [len(flat_clusters[node]) * 10 for node in G.nodes]

    # Visualize the graph with the nodes and edges
    plt.figure(figsize=(10, 8))

    # Generate positions for nodes using the spring layout
    # The `seed` ensures that the layout is deterministic (consistent between runs)
    pos = nx.spring_layout(G, seed=42)

    # Draw the nodes with sizes proportional to the cluster size
    nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color="skyblue")

    # Draw the edges between nodes, with a slightly transparent gray color
    nx.draw_networkx_edges(G, pos, width=1.5, alpha=0.7, edge_color="gray")

    # Add a title and display the plot
    plt.title("Cluster Intersection Graph with Node Sizes Proportional to Cluster Sizes")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Summary and Interpretation

    In this example, we observe that:

    - The original noisy circle has a strong one-dimensional loop structure;
    - The Mapper graph successfully captures this loop as a cycle in the graph;
    - The number of intervals, amount of overlap, and clustering threshold all affect the resulting Mapper graph.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Remarks on Mapper

    - Mapper combines ideas from both topology and clustering. It is not a homology-based method but still reveals topological features;
    - The output depends heavily on the choice of filter, cover, clustering algorithm, and parameters;
    - Mapper is widely used for exploratory data analysis, particularly for datasets where simple geometric representations fail.

    For larger-scale and more automated Mapper implementations, the following libraries are commonly used:

    - `KeplerMapper` (Python),
    - `Giotto-tda` (Python),
    - `Ayasdi` (commercial platform).
    """
    )
    return


if __name__ == "__main__":
    app.run()
