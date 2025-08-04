import marimo

__generated_with = "0.14.16"
app = marimo.App()


@app.cell
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
    mo.md(r"""# Mini-Project""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Goal""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""This mini project focuses on practicing machine learning and data visualization. The goal is to explore the [football match dataset](https://github.com/xgabora/Club-Football-Match-Data-2000-2025), uncover interesting patterns, and tell a compelling story based on the findings."""
    )
    return


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    import numpy as np
    import seaborn as sns
    import statsmodels.api as sm
    from collections import defaultdict
    from scipy.stats import ttest_ind
    from xgboost import XGBClassifier
    from sklearn.pipeline import Pipeline
    from sklearn.linear_model import LogisticRegression
    from sklearn.preprocessing import StandardScaler, LabelEncoder
    from sklearn.model_selection import train_test_split, GridSearchCV
    from sklearn.metrics import (
        make_scorer,
        ConfusionMatrixDisplay,
        classification_report,
        precision_score,
    )
    import os
    import warnings
    import sys

    # Hide all warnings
    warnings.filterwarnings("ignore")

    # Redirect stderr to devnull
    sys.stderr = open(os.devnull, "w")
    return LogisticRegression, np, pd, plt, sm, sns


@app.cell
def _(pd):
    url = "https://raw.githubusercontent.com/xgabora/Club-Football-Match-Data-2000-2025/refs/heads/main/data/Matches.csv"
    Matches = pd.read_csv(url)
    Matches["MatchDate"] = pd.to_datetime(Matches["MatchDate"])
    return (Matches,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Let's first check if there are null values:""")
    return


@app.cell
def _(Matches):
    percentage_nan = (Matches.isna().mean()).sort_values()
    print(percentage_nan)
    return


@app.cell
def _(Matches):
    missing_percentage_by_division = Matches.drop(columns="Division").groupby(Matches["Division"]).apply(lambda x: x.isna().mean()).sort_index()
    missing_percentage_by_division.mean(axis=1).sort_values()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Well, some of the columns have so many NaN values. Fortunately, some divisions have little missing values (guess they are the only ones that can afford archivists?). Let's focus on E0, the English Premier League, for now. Since there are not much missing values, let us for simplicity just drop rows with missing values. `MatchTime` is one of the only columns with large number of null values in this division, again for simplicity, let's just drop it for now.  
    Some other simple data-cleansings and validations are also performed.
    """
    )
    return


@app.cell
def _(Matches):
    England_Matches = Matches[(Matches["Division"] == "E0")].copy()
    England_Matches.drop(columns=["MatchTime"], inplace=True)
    England_Matches.dropna(inplace=True)

    # make sure the data makes sense: shot should be larger than target
    England_Matches = England_Matches[
        (England_Matches["HomeShots"] >= England_Matches["HomeTarget"]) & (England_Matches["AwayShots"] >= England_Matches["AwayTarget"])
    ]

    # card should not be nagative
    England_Matches = England_Matches[
        (England_Matches["HomeYellow"] >= 0)
        & (England_Matches["AwayYellow"] >= 0)
        & (England_Matches["HomeRed"] >= 0)
        & (England_Matches["AwayRed"] >= 0)
    ]

    # Total shots and on-target shots should be non-negative:
    England_Matches = England_Matches[
        (England_Matches["HomeShots"] >= 0)
        & (England_Matches["AwayShots"] >= 0)
        & (England_Matches["HomeTarget"] >= 0)
        & (England_Matches["AwayTarget"] >= 0)
    ]

    # Goals should not be negative:
    England_Matches = England_Matches[
        (England_Matches["FTHome"] >= 0) & (England_Matches["FTAway"] >= 0) & (England_Matches["HTHome"] >= 0) & (England_Matches["HTAway"] >= 0)
    ]

    # Odds should be > 1
    odds_cols = ["OddHome", "OddDraw", "OddAway", "MaxHome", "MaxDraw", "MaxAway"]
    for col in odds_cols:
        England_Matches = England_Matches[England_Matches[col] > 1]

    England_Matches
    return (England_Matches,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Wonderful, so we have above 7k5 rows of data to play with, not bad!""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""One thing that first comes to my mind is to explore Elo. Let us look at what are the teams with the highest Elo, and how are their Elo evolving."""
    )
    return


@app.cell
def _(England_Matches, plt, sns):
    top_teams = (England_Matches[["HomeTeam", "HomeElo"]].sort_values(by="HomeElo").tail(100))["HomeTeam"].value_counts()

    top_teams.plot(kind="barh", figsize=(10, 5))
    plt.xlabel("Count")
    plt.title("Home Teams with 100 Highest HomeElo")
    plt.gca().invert_yaxis()
    plt.show()

    top_teams = (England_Matches[["HomeTeam", "HomeElo"]].sort_values(by="HomeElo").tail(100))["HomeTeam"].value_counts().index

    filtered = England_Matches[England_Matches["HomeTeam"].isin(top_teams)].dropna(subset=["HomeElo", "MatchDate"])

    plt.figure(figsize=(10, 5))
    sns.lineplot(data=filtered, x="MatchDate", y="HomeElo", hue="HomeTeam")
    plt.title("Home Elo over Time for Top Frequent High-Elo Teams")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""Not a football fan but these are definitely big names. One thing immediately comes to my mind is that Elo is probably a good predictor of winning rate? Let's see."""
    )
    return


@app.cell
def _(England_Matches, plt, sm):
    def plot_elo_vs_winrate(team: str, last_n_games: int) -> None:
        df = England_Matches[England_Matches["HomeTeam"] == team].sort_values("MatchDate").dropna(subset=["HomeElo", "FTResult"]).copy()

        df["Win"] = (df["FTResult"] == "H").astype(int)
        winrate_col = f"WinRate{last_n_games}"
        df[winrate_col] = df["Win"].rolling(window=last_n_games).mean()

        # Line plot
        fig, ax1 = plt.subplots(figsize=(12, 6))
        ax1.plot(df["MatchDate"], df["HomeElo"], color="blue", label="Home Elo")
        ax1.set_ylabel("Home Elo", color="blue")
        ax1.tick_params(axis="y", labelcolor="blue")

        ax2 = ax1.twinx()
        ax2.plot(
            df["MatchDate"],
            df[winrate_col],
            color="green",
            linestyle="--",
            label="Win Rate",
        )
        ax2.set_ylabel(f"Rolling Win Rate ({last_n_games} Games)", color="green")
        ax2.tick_params(axis="y", labelcolor="green")

        plt.title(f"{team} - Home Elo vs {last_n_games}-Game Rolling Win Rate")
        plt.show()

        # Scatter + OLS
        valid = df.dropna(subset=[winrate_col])
        X = sm.add_constant(valid["HomeElo"])
        y = valid[winrate_col]
        model = sm.OLS(y, X).fit()

        plt.figure(figsize=(6, 4))
        plt.scatter(valid["HomeElo"], y, alpha=0.7, label="Data")
        plt.plot(valid["HomeElo"], model.predict(X), color="red", label="OLS Fit")
        plt.xlabel("Home Elo")
        plt.ylabel(f"Rolling Win Rate ({last_n_games} Games)")
        plt.title(f"{team} - Elo vs Rolling Win Rate")
        plt.legend()
        plt.show()

        print(model.summary())

    return (plot_elo_vs_winrate,)


@app.cell
def _(plot_elo_vs_winrate):
    plot_elo_vs_winrate("Man City", 40)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""That's actually surperisingly good. What if we put all the teams together?""")
    return


@app.cell
def _(England_Matches, pd, plt, sm):
    def plot_all_teams_elo_vs_winrate(last_n_games: int) -> None:
        records = []

        for team in England_Matches["HomeTeam"].unique():
            team_df = England_Matches[England_Matches["HomeTeam"] == team].sort_values("MatchDate").dropna(subset=["HomeElo", "FTResult"]).copy()

            team_df["Win"] = (team_df["FTResult"] == "H").astype(int)
            team_df[f"WinRate{last_n_games}"] = team_df["Win"].rolling(last_n_games).mean()

            records.append(team_df[["HomeElo", f"WinRate{last_n_games}"]])

        combined_df = pd.concat(records, ignore_index=True).dropna()

        X = combined_df["HomeElo"]
        y = combined_df[f"WinRate{last_n_games}"]

        X_const = sm.add_constant(X)
        model = sm.OLS(y, X_const).fit()

        # Plot
        plt.figure(figsize=(6, 4))
        plt.scatter(X, y, alpha=0.4, label="Data")
        plt.plot(X, model.predict(X_const), color="red", label="OLS Fit")
        plt.xlabel("Home Elo")
        plt.ylabel(f"Rolling Win Rate ({last_n_games} Games)")
        plt.title(f"All Teams - Elo vs Rolling Win Rate ({last_n_games} Games)")
        plt.legend()
        plt.show()

        print(model.summary())

    return (plot_all_teams_elo_vs_winrate,)


@app.cell
def _(plot_all_teams_elo_vs_winrate):
    plot_all_teams_elo_vs_winrate(40)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Looks amazing! Not exactly unexpected though after studying how is Elo defined in the first place.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    For now we just considered the home team's Elo. What if we see how a team's chance of winning changes depending on how strong they are compared to their opponent, using Elo ratings?

    Let's use a logistic regression model to predict the probability that the home team wins, based on both the home and away Elo. 

    Visualize it as a surface: home Elo on one axis, away Elo on the other, and the color shows the win probability. To get a better feel for it, look at slices of the surface - like fixing the home Elo at 1700 and seeing how the win chance changes as the opponent gets stronger or weaker. It gives a nice sense of how Elo actually plays out in match outcomes.
    """
    )
    return


@app.cell
def _(England_Matches, LogisticRegression, np, pd, plt):
    # Binary win column
    England_Matches["HomeWin"] = (England_Matches["FTResult"] == "H").astype(int)

    # Prepare training data
    df = England_Matches.dropna(subset=["HomeElo", "AwayElo", "HomeWin"])
    X = df[["HomeElo", "AwayElo"]]
    y = df["HomeWin"]

    # Fit logistic regression
    model = LogisticRegression()
    model.fit(X, y)

    # --- Build 2D Elo grid ---
    elo_min = int(min(England_Matches["HomeElo"].min(), England_Matches["AwayElo"].min()) // 100 * 100)
    elo_max = int(max(England_Matches["HomeElo"].max(), England_Matches["AwayElo"].max()) // 100 * 100 + 100)
    step = max(1, int((elo_max - elo_min) // 30))  # guard against step=0

    home_elo = np.arange(elo_min, elo_max + step, step)
    away_elo = np.arange(elo_min, elo_max + step, step)
    grid_home, grid_away = np.meshgrid(home_elo, away_elo)  # shapes: (len(away_elo), len(home_elo))

    # --- Predict win probabilities on the grid ---
    grid_points = np.column_stack([grid_home.ravel(), grid_away.ravel()])
    grid_df = pd.DataFrame(grid_points, columns=["HomeElo", "AwayElo"])
    win_probs = model.predict_proba(grid_df)[:, 1]  # probability of HomeWin == 1
    win_prob_grid = win_probs.reshape(grid_home.shape)

    # --- 3D Surface plot ---
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection="3d")

    surf = ax.plot_surface(
        grid_home,  # X = Home Elo
        grid_away,  # Y = Away Elo
        win_prob_grid,  # Z = P(Home Win)
        cmap="viridis",
        linewidth=0,
        antialiased=True,
        alpha=0.95,
    )

    # Optional: light wireframe overlay for structure
    ax.plot_wireframe(
        grid_home,
        grid_away,
        win_prob_grid,
        rstride=3,
        cstride=3,
        linewidth=0.3,
        alpha=0.4,
    )

    ax.set_title("Predicted Home Win Probability Surface (Logistic Regression)")
    ax.set_xlabel("Home Elo")
    ax.set_ylabel("Away Elo")
    ax.set_zlabel("P(Home Win)")

    # Colorbar for probabilities
    fig.colorbar(surf, ax=ax, shrink=0.6, aspect=12, label="P(Home Win)")

    # Nice view angle
    ax.view_init(elev=25, azim=105)

    plt.tight_layout()
    plt.show()
    return elo_max, elo_min, model, step


@app.cell
def _(elo_max, elo_min, model, np, pd, plt, step):
    def plot_winrate_given_homeelo(fixed_home_elo: int):
        away_range = np.arange(elo_min, elo_max, step)
        grid_input = pd.DataFrame({"HomeElo": [fixed_home_elo] * len(away_range), "AwayElo": away_range})

        predicted_probs = model.predict_proba(grid_input)[:, 1]

        plt.figure(figsize=(8, 5))
        plt.plot(away_range, predicted_probs, marker="o")
        plt.title(f"P(Home Win) vs Away Elo (Home Elo = {fixed_home_elo})")
        plt.xlabel("Away Elo")
        plt.ylabel("P(Home Win)")
        plt.grid(True)
        plt.show()

    plot_winrate_given_homeelo(1700)
    plot_winrate_given_homeelo(2000)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    The plot should look familiar, indeed, it's like a reversed logistic function. This reminds me the volatility surface in stock option modeling.

    A sanity check, does the number make sense? Let's see the winrate of a ~1700 elo home team vs a ~1600 elo away team:
    """
    )
    return


@app.cell
def _(England_Matches):
    England_Matches[
        (England_Matches["HomeElo"] >= 1700 - 15)
        & (England_Matches["HomeElo"] <= 1700 + 15)
        & (England_Matches["AwayElo"] >= 1600 - 15)
        & (England_Matches["AwayElo"] <= 1600 + 15)
    ]["FTResult"].value_counts(normalize=True)
    return


@app.cell
def _(England_Matches):
    England_Matches[
        (England_Matches["HomeElo"] >= 1700 - 15)
        & (England_Matches["HomeElo"] <= 1700 + 15)
        & (England_Matches["AwayElo"] >= 2000 - 15)
        & (England_Matches["AwayElo"] <= 2000 + 15)
    ]["FTResult"].value_counts(normalize=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Compare the win rate 0.55 (resp. 0.20, sample size is pretty small) with the above plot at x = 1600 (resp. 2000), I'd say we do have something that is making sense!  
    From here we can also kinda see Home team has an advantage over Away team - the probability of a home team with Elo x defeats a team with same Elo x is usually above 40%, even close to 50%. Considering that ~1/4 of games in soccer matches is draw, that is a very "biased" probability.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    So we have some simple win-probability forecasting. Why don't we go ahead and try to predict match result? To do that we need some further preparation.  
    In particular, there are columns in the dataset that we cannot directly use. For example, we should definitely NOT use `FTHome` and `FTAway` which are simply the scores of the matches to predict match result. A more subtle case is when we try to use things like `HomeTarget` (number of shots made by Home team that is on target) - things that is unknown *before* the match start. This is called lookahead bias in finance world, which should be avoided at all cost in predicting things.  
    However, there are things that we can use. For example, Elo, as a good feature predicting rolling winning rate, can be used, as it is updated once a while and the recorded Elo is the *most updated* Elo which is known to public before each match starts.  
    We can also do some feature engineering. For example, we cannot directly use `HomeTarget`, but we can calculate the average shots on target the Home team made (on average) in their past N games!  
    Let's start with some engineering.
    """
    )
    return


if __name__ == "__main__":
    app.run()
