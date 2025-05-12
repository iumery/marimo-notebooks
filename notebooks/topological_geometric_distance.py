import marimo

__generated_with = "0.13.4"
app = marimo.App(
    width="medium",
    css_file="/Users/zedanliu/Documents/project/marimo-theme/molokai.css",
)


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib as mpl

    mpl.rcParams["text.usetex"] = False
    from ripser import Rips
    import persim
    from scipy.spatial.distance import pdist, squareform
    import networkx as nx
    import gudhi as gd
    import gudhi.representations as gr
    from tslearn.metrics import dtw
    from scipy.spatial.distance import euclidean
    from scipy.stats import uniform
    import warnings

    warnings.filterwarnings("ignore", category=RuntimeWarning)
    return Rips, dtw, euclidean, gd, gr, np, nx, pdist, persim, plt, squareform


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


@app.cell
def _(Rips, np, nx, pdist, persim, plt, squareform):
    def analyze_series_with_orientation(
        log_returns, delay=1, dimension=2, add_sign=True, epsilon_factor=1.5
    ):
        """
        Analyze a log return series:
        - 2x2 grid of plots for trajectory, embedded points, Rips complex, and persistence diagram
        - Dynamically set ε for the Rips complex
        """
        fig, axs = plt.subplots(2, 2, figsize=(12, 8))  # 2x2 grid

        # === 1️⃣ Reconstruct and plot the trajectory ===
        initial_price = 100
        prices = initial_price * np.exp(np.cumsum(log_returns))

        axs[0, 0].plot(prices, marker="o", color="blue", markersize=3)
        axs[0, 0].set_title("Price Trajectory")
        axs[0, 0].set_xlabel("Time")
        axs[0, 0].set_ylabel("Price")
        axs[0, 0].grid(True)

        # === 2️⃣ Takens embedding ===
        embedding = np.array(
            [
                log_returns[i : i + dimension * delay : delay]
                for i in range(len(log_returns) - (dimension - 1) * delay)
            ]
        )

        if add_sign:
            signs = np.sign(embedding[:, 0]).reshape(-1, 1)
            embedding = np.hstack((embedding, signs))

        # Normalize data (prevents large value differences from hiding edges)
        # scaler = StandardScaler()
        # embedding = scaler.fit_transform(embedding)

        # Plot 2D embedded point cloud
        axs[0, 1].scatter(embedding[:, 0], embedding[:, 1], c="blue", s=10)
        axs[0, 1].set_title("2D Orientation-Aware Embedding")
        axs[0, 1].set_xlabel("rₜ")
        axs[0, 1].set_ylabel("rₜ₊₁")
        axs[0, 1].grid(True)

        # === 3️⃣ Compute pairwise distances & adaptively set ε ===
        distances = squareform(pdist(embedding))
        dist_std = np.std(distances)  # Compute standard deviation of distances
        epsilon = epsilon_factor * dist_std  # Dynamically choose ε

        print(f"🔹 Adaptive Epsilon: {epsilon:.6f}")

        # Build Rips complex
        G = nx.Graph()
        for i, point in enumerate(embedding):
            G.add_node(i, pos=(point[0], point[1]))

        for i in range(len(embedding)):
            for j in range(i + 1, len(embedding)):
                if distances[i, j] <= epsilon:
                    G.add_edge(i, j)

        pos = nx.get_node_attributes(G, "pos")
        nx.draw(
            G, pos, node_size=10, edge_color="gray", with_labels=False, ax=axs[1, 0]
        )
        axs[1, 0].set_title(f"Rips Complex (ε={epsilon:.4f})")
        axs[1, 0].set_xlabel("rₜ")
        axs[1, 0].set_ylabel("rₜ₊₁")

        # === 4️⃣ Compute and plot persistence diagram ===
        rips = Rips(maxdim=2)
        diagrams = rips.fit_transform(embedding)

        persim.plot_diagrams(diagrams, ax=axs[1, 1])
        axs[1, 1].set_title("Persistence Diagram")

        # === Final Adjustments ===
        plt.tight_layout()
        plt.show()

        return embedding, diagrams

    return (analyze_series_with_orientation,)


@app.cell
def _(analyze_series_with_orientation, np):
    neg_log_returns = -np.abs(np.random.normal(0, 0.05, 50))

    neg_embedding, neg_diagrams = analyze_series_with_orientation(
        neg_log_returns, delay=3, dimension=3, add_sign=False, epsilon_factor=0.5
    )

    pos_log_returns = np.abs(np.random.normal(0, 0.05, 50))

    pos_embedding, pos_diagrams = analyze_series_with_orientation(
        pos_log_returns, delay=3, dimension=3, add_sign=False, epsilon_factor=0.5
    )

    rnd_log_returns = np.random.normal(0, 0.05, 50)

    rnd_embedding, rnd_diagrams = analyze_series_with_orientation(
        rnd_log_returns, delay=3, dimension=3, add_sign=False, epsilon_factor=0.5
    )
    return neg_diagrams, pos_diagrams, rnd_diagrams


@app.cell
def _(neg_diagrams, persim, pos_diagrams, rnd_diagrams):
    wasserstein_distance = persim.wasserstein(
        neg_diagrams[1], pos_diagrams[1], matching=False
    )
    print(
        f"\n✅ Wasserstein Distance (H₁, loops) between negative and positive series: {wasserstein_distance}"
    )

    wasserstein_distance = persim.wasserstein(
        neg_diagrams[1], rnd_diagrams[1], matching=False
    )
    print(
        f"\n✅ Wasserstein Distance (H₁, loops) between negative and random series: {wasserstein_distance}"
    )

    wasserstein_distance = persim.wasserstein(
        rnd_diagrams[1], pos_diagrams[1], matching=False
    )
    print(
        f"\n✅ Wasserstein Distance (H₁, loops) between random and positive series: {wasserstein_distance}"
    )
    return


@app.cell
def _(dtw, euclidean, gd, gr, np, plt):
    def compute_persistence_diagram(
        time_series, lags=[1], max_edge_length=2.0, max_dimension=1
    ):
        """
        Compute the persistence diagram of a time series using Vietoris-Rips filtration.
        :param time_series: 1D NumPy array representing the time series.
        :param dim: Maximum homology dimension (default is 1 for loops).
        :return: Persistence diagram as a NumPy array.
        """
        point_cloud = np.array(
            [
                [time_series[i + j] for j in [0] + lags]
                for i in range(len(time_series) - max(lags))
            ]
        )
        rips = gd.RipsComplex(points=point_cloud, max_edge_length=max_edge_length)
        simplex_tree = rips.create_simplex_tree(max_dimension=max_dimension)
        persistence = simplex_tree.persistence()
        return np.array(
            simplex_tree.persistence_intervals_in_dimension(max_dimension - 1)
        )

    def sliced_wasserstein_distance(diag1, diag2, num_directions=100):
        """
        Compute the sliced Wasserstein distance between two persistence diagrams.
        :param diag1: Persistence diagram 1.
        :param diag2: Persistence diagram 2.
        :param num_directions: Number of random projection directions.
        :return: Sliced Wasserstein distance.
        """
        sw = gr.WassersteinDistance()
        return sw(diag1, diag2)

    def geometric_distance(time_series1, time_series2, method="dtw"):
        """
        Compute geometric similarity using either Euclidean Distance or DTW.
        :param time_series1: First time series.
        :param time_series2: Second time series.
        :param method: "euclidean" or "dtw".
        :return: Distance value.
        """
        if method == "euclidean":
            return euclidean(time_series1, time_series2)
        elif method == "dtw":
            return dtw(time_series1, time_series2)
        else:
            raise ValueError("Unsupported geometric distance method.")

    def tgmd(
        time_series1,
        time_series2,
        k=1,
        geo_method="dtw",
        num_directions=100,
        lags=[1],
        max_edge_length=2.0,
        max_dimension=1,
    ):
        """
        Compute the Topological-Geometric Mixed Distance (TGMD) between two time series.
        :param time_series1: First time series.
        :param time_series2: Second time series.
        :param k: Tuning parameter for balancing topology and geometry.
        :param geo_method: "euclidean" or "dtw" for geometric distance.
        :param num_directions: Number of directions for sliced Wasserstein distance.
        :return: TGMD distance.
        """
        # Compute persistence diagrams
        pd1 = compute_persistence_diagram(
            time_series1, lags, max_edge_length, max_dimension
        )
        pd2 = compute_persistence_diagram(
            time_series2, lags, max_edge_length, max_dimension
        )

        # Compute Sliced Wasserstein Distance (SWD) for topological similarity
        topological_similarity = sliced_wasserstein_distance(pd1, pd2, num_directions)

        # Normalize topological similarity to [0, 1]
        topological_similarity = np.exp(
            -topological_similarity
        )  # Map to (0,1) using exponential decay

        # Compute geometric distance
        geo_dist = geometric_distance(time_series1, time_series2, method=geo_method)

        def tuning_function(x, k=1):
            """
            Monotonic tuning function to balance topological and geometric distances.
            :param x: Normalized topological similarity (between 0 and 1).
            :param k: Tuning parameter (default is 1).
            :return: Tuning weight.
            """
            return 2 / (1 + np.exp(-k * (2 * x - 1)))

        # Apply tuning function
        weight = tuning_function(topological_similarity, k)

        # Compute TGMD
        tgmd_distance = weight * geo_dist

        return tgmd_distance

    def plot_time_series_and_stock_trajectory(
        time_series1, time_series2, tgmd_distance
    ):
        """
        Plot two time series and their corresponding stock price trajectories assuming returns.
        :param time_series1: First time series (returns).
        :param time_series2: Second time series (returns).
        :param tgmd_distance: Computed TGMD distance.
        """
        # Convert returns to stock price trajectory (assume initial price = 100)
        stock1 = 100 * np.cumprod(1 + time_series1)
        stock2 = 100 * np.cumprod(1 + time_series2)

        fig, axes = plt.subplots(2, 1, figsize=(10, 8))

        # Plot the time series (returns)
        axes[0].plot(
            time_series1, label="Returns - Time Series 1", linestyle="--", marker="o"
        )
        axes[0].plot(
            time_series2, label="Returns - Time Series 2", linestyle="-", marker="s"
        )
        axes[0].set_title(f"Time Series (TGMD Distance: {tgmd_distance:.4f})")
        axes[0].set_xlabel("Time")
        axes[0].set_ylabel("Returns")
        axes[0].legend()

        # Plot the stock price trajectories
        axes[1].plot(stock1, label="Stock Price - Series 1", linestyle="--", marker="o")
        axes[1].plot(stock2, label="Stock Price - Series 2", linestyle="-", marker="s")
        axes[1].set_title("Stock Price Trajectories")
        axes[1].set_xlabel("Time")
        axes[1].set_ylabel("Price")
        axes[1].legend()

        plt.tight_layout()
        plt.show()

    return plot_time_series_and_stock_trajectory, tgmd


@app.cell
def _(np, plot_time_series_and_stock_trajectory, tgmd):
    time_series_ran1 = np.random.normal(0, 0.1, 50)
    time_series_ran2 = np.random.normal(0, 0.1, 50)

    tgmd_result = tgmd(
        time_series_ran1,
        time_series_ran2,
        k=2,
        geo_method="dtw",
        num_directions=100,
        lags=[1],
        max_edge_length=0.075,
        max_dimension=2,
    )
    print(f"TGMD Distance: {tgmd_result}")

    plot_time_series_and_stock_trajectory(
        time_series_ran1, time_series_ran2, tgmd_result
    )
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _(np):
    def TimeDelayEmbedding(x, edim, delay=1):
        """time delay embedding of a d-dim times series into R^{d*edim}
        the time series is assumed to be periodic
        parameters:
            + x: a list of d lists of same length L or a dxL numpy array
            + edim: the number of points taken to build the embedding in R^{d*edim}
            + delay: embeeding given by (x[i],x[i+delay],...,x[i + (edim-1)*delay])
                Default value for delay is 1
        """
        ts = np.asarray(x)
        if len(np.shape(ts)) == 1:
            ts = np.reshape(ts, (1, ts.shape[0]))
        ts_d = ts.shape[0]
        ts_length = ts.shape[1]
        output = ts
        for i in range(edim - 1):
            output = np.concatenate(
                (output, np.roll(ts, -(i + 1) * delay, axis=1)), axis=0
            )
        return output

    return (TimeDelayEmbedding,)


@app.cell
def _(np):
    flute = np.genfromtxt("flute.csv", delimiter=",")
    clarinet = np.genfromtxt("clarinet.csv", delimiter=",")
    return clarinet, flute


@app.cell
def _(clarinet, flute, plt):
    fig1 = plt.figure(figsize=(15, 5))
    ax1_1 = fig1.add_subplot(1, 2, 1)
    ax1_2 = fig1.add_subplot(1, 2, 2)
    ax1_1.plot(range(1000), flute[0:1000])
    ax1_2.plot(range(1000), clarinet[0:1000])
    return


@app.cell
def _(tde):
    tde.T / 2
    return


@app.cell
def _(gd, plt, tde):
    rips = gd.RipsComplex(points=tde.T / 2, max_edge_length=0.3)
    st = rips.create_simplex_tree(max_dimension=2)

    barcode = st.persistence(homology_coeff_field=2)
    fig = plt.figure(figsize=(15, 5))
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)

    gd.plot_persistence_barcode(barcode, axes=ax1)
    gd.plot_persistence_diagram(barcode, axes=ax2)
    return


@app.cell
def _(TimeDelayEmbedding, clarinet, gd, np):
    n_cycles = []
    len_sample = 500
    for j in range(5):
        print("Sample {}".format(j))
        i = np.random.randint(0, len(clarinet) - len_sample)
        sample = clarinet[i : i + len_sample]
        tde = TimeDelayEmbedding(sample, edim=2, delay=2)
        rips_sample = gd.RipsComplex(points=tde.T / 2, max_edge_length=0.1)
        st_sample = rips_sample.create_simplex_tree(max_dimension=2)
        barcode_sample = st_sample.persistence(homology_coeff_field=2)
        large_persistence = [
            (a, b) for (j, (a, b)) in barcode_sample if b - a > 0.015 and j == 1
        ]
        n_cycles.append(len(large_persistence))
    print()
    print(np.mean(n_cycles))
    return (tde,)


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    import pickle as pickle

    file = open("acc.txt", "rb")
    data = pickle.load(file, encoding="latin1")
    file.close()

    data_A = data[0]
    data_B = data[1]
    data_C = data[2]
    return data_A, data_B, data_C


@app.cell
def _(data_A, plt):
    data_A_sample = data_A[0]

    figA = plt.figure(figsize=(10, 10))
    ax = figA.add_subplot(111, projection="3d")
    ax.scatter(data_A_sample[:, 0], data_A_sample[:, 1], data_A_sample[:, 2], c="black")
    ax.plot(data_A_sample[:, 0], data_A_sample[:, 1], data_A_sample[:, 2])
    return


@app.cell
def _(data_A, data_B, data_C, gd):
    barcodes = []
    for person in [data_A, data_B, data_C]:
        for series in person:
            st_person = gd.RipsComplex(
                points=series / 2, max_edge_length=1
            ).create_simplex_tree(max_dimension=2)
            st_person.persistence(homology_coeff_field=2)
            barcode_person = st_person.persistence_intervals_in_dimension(1)
            barcodes.append(barcode_person)
    return (barcodes,)


@app.cell
def _(barcodes, gd, np):
    dist = np.zeros((len(barcodes), len(barcodes)))
    for ii, barcode_i in enumerate(barcodes):
        for jj, barcode_j in enumerate(barcodes):
            dist[ii, jj] = gd.bottleneck_distance(barcode_i, barcode_j)
    return (dist,)


@app.cell
def _(dist, plt):
    from sklearn import manifold

    mds = manifold.MDS(
        n_components=3, max_iter=3000, eps=1e-9, dissimilarity="precomputed", n_jobs=1
    )
    pos = mds.fit(dist).embedding_
    figm = plt.figure(figsize=(10, 10))
    axm = figm.add_subplot(111, projection="3d")

    n = int(len(pos) / 3)
    label_color = ["magenta"] * n + ["blue"] * n + ["green"] * n
    axm.scatter(pos[:, 0], pos[:, 1], pos[:, 2], s=70, color=label_color)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
