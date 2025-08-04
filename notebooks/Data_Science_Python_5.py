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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Import""")
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
    return (
        ConfusionMatrixDisplay,
        GridSearchCV,
        LabelEncoder,
        LogisticRegression,
        Pipeline,
        StandardScaler,
        XGBClassifier,
        classification_report,
        defaultdict,
        make_scorer,
        np,
        pd,
        plt,
        precision_score,
        sm,
        sns,
        train_test_split,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Load Data and Pre-Processing""")
    return


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
    missing_percentage_by_division = (
        Matches.drop(columns="Division")
        .groupby(Matches["Division"])
        .apply(lambda x: x.isna().mean())
        .sort_index()
    )
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
        (England_Matches["HomeShots"] >= England_Matches["HomeTarget"])
        & (England_Matches["AwayShots"] >= England_Matches["AwayTarget"])
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
        (England_Matches["FTHome"] >= 0)
        & (England_Matches["FTAway"] >= 0)
        & (England_Matches["HTHome"] >= 0)
        & (England_Matches["HTAway"] >= 0)
    ]

    # Odds should be > 1
    odds_cols = ["OddHome", "OddDraw", "OddAway", "MaxHome", "MaxDraw", "MaxAway"]
    for odd_col in odds_cols:
        England_Matches = England_Matches[England_Matches[odd_col] > 1]

    England_Matches
    return (England_Matches,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""Wonderful, so we have above 7k5 rows of data to play with, not bad!"""
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Elo and Winning Probability""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""One thing that first comes to my mind is to explore Elo. Let us look at what are the teams with the highest Elo, and how are their Elo evolving."""
    )
    return


@app.cell
def _(England_Matches, plt, sns):
    top_teams = (
        England_Matches[["HomeTeam", "HomeElo"]]
        .sort_values(by="HomeElo")
        .tail(100)
    )["HomeTeam"].value_counts()

    top_teams.plot(kind="barh", figsize=(10, 5))
    plt.xlabel("Count")
    plt.title("Home Teams with 100 Highest HomeElo")
    plt.gca().invert_yaxis()
    plt.show()

    top_teams = (
        (
            England_Matches[["HomeTeam", "HomeElo"]]
            .sort_values(by="HomeElo")
            .tail(100)
        )["HomeTeam"]
        .value_counts()
        .index
    )

    filtered = England_Matches[England_Matches["HomeTeam"].isin(top_teams)].dropna(
        subset=["HomeElo", "MatchDate"]
    )

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
        df = (
            England_Matches[England_Matches["HomeTeam"] == team]
            .sort_values("MatchDate")
            .dropna(subset=["HomeElo", "FTResult"])
            .copy()
        )

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
    mo.md(
        r"""That's actually surperisingly good. What if we put all the teams together?"""
    )
    return


@app.cell
def _(England_Matches, pd, plt, sm):
    def plot_all_teams_elo_vs_winrate(last_n_games: int) -> None:
        records = []

        for team in England_Matches["HomeTeam"].unique():
            team_df = (
                England_Matches[England_Matches["HomeTeam"] == team]
                .sort_values("MatchDate")
                .dropna(subset=["HomeElo", "FTResult"])
                .copy()
            )

            team_df["Win"] = (team_df["FTResult"] == "H").astype(int)
            team_df[f"WinRate{last_n_games}"] = (
                team_df["Win"].rolling(last_n_games).mean()
            )

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
    mo.md(
        r"""Looks amazing! Not exactly unexpected though after studying how is Elo defined in the first place."""
    )
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
    surface_df = England_Matches.dropna(subset=["HomeElo", "AwayElo", "HomeWin"])
    surface_X = surface_df[["HomeElo", "AwayElo"]]
    surface_y = surface_df["HomeWin"]

    # Fit logistic regression
    surface_model = LogisticRegression()
    surface_model.fit(surface_X, surface_y)

    # --- Build 2D Elo grid ---
    elo_min = int(
        min(England_Matches["HomeElo"].min(), England_Matches["AwayElo"].min())
        // 100
        * 100
    )
    elo_max = int(
        max(England_Matches["HomeElo"].max(), England_Matches["AwayElo"].max())
        // 100
        * 100
        + 100
    )
    step = max(1, int((elo_max - elo_min) // 30))  # guard against step=0

    home_elo = np.arange(elo_min, elo_max + step, step)
    away_elo = np.arange(elo_min, elo_max + step, step)
    grid_home, grid_away = np.meshgrid(
        home_elo, away_elo
    )  # shapes: (len(away_elo), len(home_elo))

    # --- Predict win probabilities on the grid ---
    grid_points = np.column_stack([grid_home.ravel(), grid_away.ravel()])
    grid_df = pd.DataFrame(grid_points, columns=["HomeElo", "AwayElo"])
    win_probs = surface_model.predict_proba(grid_df)[
        :, 1
    ]  # probability of HomeWin == 1
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
    return elo_max, elo_min, step, surface_model


@app.cell
def _(elo_max, elo_min, np, pd, plt, step, surface_model):
    def plot_winrate_given_homeelo(fixed_home_elo: int):
        away_range = np.arange(elo_min, elo_max, step)
        grid_input = pd.DataFrame(
            {"HomeElo": [fixed_home_elo] * len(away_range), "AwayElo": away_range}
        )

        predicted_probs = surface_model.predict_proba(grid_input)[:, 1]

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
    mo.md(r"""## Predict Match Result with ML""")
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


@app.cell
def _(England_Matches, defaultdict, np, pd):
    England_Matches_copy = England_Matches.copy()

    England_Matches_copy.sort_values(by="MatchDate", inplace=True)
    England_Matches_copy.reset_index(drop=True, inplace=True)

    # Difference in current game's goal.
    # This can be potentially used for a regression version of the model
    England_Matches_copy["NetHomeGoal"] = (
        England_Matches_copy["FTHome"] - England_Matches_copy["FTAway"]
    )

    # Some of the original features are too much right-skewed
    for col in [
        "OddHome",
        "OddDraw",
        "OddAway",
        "MaxHome",
        "MaxDraw",
        "MaxAway",
        "Under25",
        "MaxUnder25",
        "HandiHome",
        "HandiAway",
    ]:
        England_Matches_copy[f"LOG_{col}"] = np.log(England_Matches_copy[col])

    # Difference in Elo
    England_Matches_copy["EloDiff"] = (
        England_Matches_copy["HomeElo"] - England_Matches_copy["AwayElo"]
    )

    # Number of goals made in the last 5 games
    home_goals_last5 = []
    away_goals_last5 = []
    goal_history = defaultdict(list)

    for _, row in England_Matches_copy.iterrows():
        home_team = row["HomeTeam"]
        away_team = row["AwayTeam"]

        home_past_goals = goal_history[home_team][-5:]
        away_past_goals = goal_history[away_team][-5:]

        home_goals_last5.append(sum(home_past_goals))
        away_goals_last5.append(sum(away_past_goals))

        goal_history[home_team].append(row["FTHome"])
        goal_history[away_team].append(row["FTAway"])

    England_Matches_copy["HomeGoalsLast5"] = home_goals_last5
    England_Matches_copy["AwayGoalsLast5"] = away_goals_last5

    # Number of goals conceded in the last 5 games
    conceded_history = defaultdict(list)
    home_conceded_last5 = []
    away_conceded_last5 = []

    for _, row in England_Matches_copy.iterrows():
        home_team = row["HomeTeam"]
        away_team = row["AwayTeam"]

        home_past_conceded = conceded_history[home_team][-5:]
        away_past_conceded = conceded_history[away_team][-5:]

        home_conceded_last5.append(sum(home_past_conceded))
        away_conceded_last5.append(sum(away_past_conceded))

        conceded_history[home_team].append(
            row["FTAway"]
        )  # home conceded away goals
        conceded_history[away_team].append(
            row["FTHome"]
        )  # away conceded home goals

    England_Matches_copy["HomeConcededLast5"] = home_conceded_last5
    England_Matches_copy["AwayConcededLast5"] = away_conceded_last5

    # Win streak and loss streak
    win_streaks = defaultdict(int)
    home_streak = []
    away_streak = []

    for _, row in England_Matches_copy.iterrows():
        home = row["HomeTeam"]
        away = row["AwayTeam"]
        result = row["FTResult"]

        home_streak.append(win_streaks[home])
        away_streak.append(win_streaks[away])

        if result == "H":
            win_streaks[home] += 1
            win_streaks[away] = 0
        elif result == "A":
            win_streaks[away] += 1
            win_streaks[home] = 0
        else:  # Draw resets both
            win_streaks[home] = 0
            win_streaks[away] = 0

    England_Matches_copy["HomeWinStreak"] = home_streak
    England_Matches_copy["AwayWinStreak"] = away_streak

    loss_streaks = defaultdict(int)
    home_loss_streak = []
    away_loss_streak = []

    for _, row in England_Matches_copy.iterrows():
        home = row["HomeTeam"]
        away = row["AwayTeam"]
        result = row["FTResult"]

        home_loss_streak.append(loss_streaks[home])
        away_loss_streak.append(loss_streaks[away])

        if result == "A":
            loss_streaks[home] += 1
            loss_streaks[away] = 0
        elif result == "H":
            loss_streaks[away] += 1
            loss_streaks[home] = 0
        else:  # Draw resets both
            loss_streaks[home] = 0
            loss_streaks[away] = 0

    England_Matches_copy["HomeLossStreak"] = home_loss_streak
    England_Matches_copy["AwayLossStreak"] = away_loss_streak

    # how many day between this match and the team's last match
    last_played: dict[str, pd.Timestamp] = {}
    home_rest_days = []
    away_rest_days = []

    for _, row in England_Matches_copy.iterrows():
        date = row["MatchDate"]
        home = row["HomeTeam"]
        away = row["AwayTeam"]

        home_rest = (
            (date - last_played[home]).days if home in last_played else None
        )
        away_rest = (
            (date - last_played[away]).days if away in last_played else None
        )

        home_rest_days.append(home_rest)
        away_rest_days.append(away_rest)

        last_played[home] = date
        last_played[away] = date

    England_Matches_copy["HomeRestDays"] = home_rest_days
    England_Matches_copy["AwayRestDays"] = away_rest_days


    # Elo momentum: difference between current Elo and Elo n games before
    def compute_elo_momentum_all_roles(
        df: pd.DataFrame, team_col: str, new_col: str, n: int = 5
    ) -> pd.DataFrame:
        df = df.copy()
        records = []

        for team in df[team_col].unique():
            team_matches = df[
                (df["HomeTeam"] == team) | (df["AwayTeam"] == team)
            ].copy()
            team_matches = team_matches.sort_values("MatchDate")

            team_matches["TeamElo"] = team_matches.apply(
                lambda row: row["HomeElo"]
                if row["HomeTeam"] == team
                else row["AwayElo"],
                axis=1,
            )

            team_matches[new_col] = team_matches["TeamElo"] - team_matches[
                "TeamElo"
            ].shift(n)
            team_matches["MatchIndex"] = team_matches.index  # Keep original index

            records.append(team_matches[["MatchIndex", new_col]])

        merged = (
            pd.concat(records)
            .drop_duplicates("MatchIndex", keep="first")
            .set_index("MatchIndex")
        )

        df.loc[merged.index, new_col] = merged[new_col]
        return df


    England_Matches_copy = compute_elo_momentum_all_roles(
        England_Matches_copy, "HomeTeam", "HomeEloMomentum", n=5
    )
    England_Matches_copy = compute_elo_momentum_all_roles(
        England_Matches_copy, "AwayTeam", "AwayEloMomentum", n=5
    )

    # Discipline: average cards got in the past 5 games (red counts as 2)
    home_discipline_last5 = []
    away_discipline_last5 = []

    discipline_history = defaultdict(list)

    for _, row in England_Matches_copy.iterrows():
        home = row["HomeTeam"]
        away = row["AwayTeam"]
        home_yellow, home_red = row["HomeYellow"], row["HomeRed"]
        away_yellow, away_red = row["AwayYellow"], row["AwayRed"]

        home_past = discipline_history[home][-5:]
        away_past = discipline_history[away][-5:]

        home_score = np.mean(home_past) if home_past else np.nan
        away_score = np.mean(away_past) if away_past else np.nan

        home_discipline_last5.append(home_score)
        away_discipline_last5.append(away_score)

        discipline_history[home].append(home_yellow + 2 * home_red)
        discipline_history[away].append(away_yellow + 2 * away_red)

    England_Matches_copy["HomeDisciplineScore"] = home_discipline_last5
    England_Matches_copy["AwayDisciplineScore"] = away_discipline_last5


    # In the last 5 games, what's the average different between the shot the team made versus their competent made?
    def compute_avg_shot_diff(
        matches: pd.DataFrame, team_col: str, side: str
    ) -> pd.Series:
        shot_diffs = []

        for i, row in matches.iterrows():
            team = row[team_col]
            match_date = row["MatchDate"]

            past_matches = (
                matches[
                    (
                        (
                            (matches["HomeTeam"] == team)
                            | (matches["AwayTeam"] == team)
                        )
                        & (matches["MatchDate"] < match_date)
                    )
                ]
                .sort_values("MatchDate", ascending=False)
                .head(5)
            )

            diffs = []
            for _, match in past_matches.iterrows():
                if match["HomeTeam"] == team:
                    diff = match["HomeShots"] - match["AwayShots"]
                else:
                    diff = match["AwayShots"] - match["HomeShots"]
                diffs.append(diff)

            avg_diff = np.mean(diffs) if diffs else np.nan
            shot_diffs.append(avg_diff)

        return pd.Series(shot_diffs, index=matches.index)


    England_Matches_copy["HomeAvgShotDiff5"] = compute_avg_shot_diff(
        England_Matches_copy, "HomeTeam", "home"
    )
    England_Matches_copy["AwayAvgShotDiff5"] = compute_avg_shot_diff(
        England_Matches_copy, "AwayTeam", "away"
    )


    # In the last 5 games, what's the average different between the corner the team made versus their competent made?
    def compute_avg_corner_diff(
        matches: pd.DataFrame, team_col: str, side: str
    ) -> pd.Series:
        corner_diffs = []

        for i, row in matches.iterrows():
            team = row[team_col]
            match_date = row["MatchDate"]

            past_matches = (
                matches[
                    (
                        (
                            (matches["HomeTeam"] == team)
                            | (matches["AwayTeam"] == team)
                        )
                        & (matches["MatchDate"] < match_date)
                    )
                ]
                .sort_values("MatchDate", ascending=False)
                .head(5)
            )

            diffs = []
            for _, match in past_matches.iterrows():
                if match["HomeTeam"] == team:
                    diff = match["HomeCorners"] - match["AwayCorners"]
                else:
                    diff = match["AwayCorners"] - match["HomeCorners"]
                diffs.append(diff)

            avg_diff = np.mean(diffs) if diffs else np.nan
            corner_diffs.append(avg_diff)

        return pd.Series(corner_diffs, index=matches.index)


    England_Matches_copy["HomeAvgCornerDiff5"] = compute_avg_corner_diff(
        England_Matches_copy, "HomeTeam", "home"
    )
    England_Matches_copy["AwayAvgCornerDiff5"] = compute_avg_corner_diff(
        England_Matches_copy, "AwayTeam", "away"
    )

    # And difference in accuracy? (shots on target / total shots)
    home_acc = []
    away_acc = []

    for idx, row in England_Matches_copy.iterrows():
        date = row["MatchDate"]
        home_team = row["HomeTeam"]
        away_team = row["AwayTeam"]

        past_home = England_Matches_copy[
            (
                (England_Matches_copy["HomeTeam"] == home_team)
                | (England_Matches_copy["AwayTeam"] == home_team)
            )
            & (England_Matches_copy["MatchDate"] < date)
        ].tail(5)

        accs = []
        for _, match in past_home.iterrows():
            if match["HomeTeam"] == home_team:
                shots, target = match["HomeShots"], match["HomeTarget"]
            else:
                shots, target = match["AwayShots"], match["AwayTarget"]
            if pd.notna(shots) and shots > 0:
                accs.append(target / shots)
        home_acc.append(np.mean(accs) if accs else np.nan)

        past_away = England_Matches_copy[
            (
                (England_Matches_copy["HomeTeam"] == away_team)
                | (England_Matches_copy["AwayTeam"] == away_team)
            )
            & (England_Matches_copy["MatchDate"] < date)
        ].tail(5)

        accs = []
        for _, match in past_away.iterrows():
            if match["HomeTeam"] == away_team:
                shots, target = match["HomeShots"], match["HomeTarget"]
            else:
                shots, target = match["AwayShots"], match["AwayTarget"]
            if pd.notna(shots) and shots > 0:
                accs.append(target / shots)
        away_acc.append(np.mean(accs) if accs else np.nan)

    England_Matches_copy["HomeAvgShotAcc5"] = home_acc
    England_Matches_copy["AwayAvgShotAcc5"] = away_acc

    # Head-to-head win/loss/draw probability
    England_Matches_copy["H2H_HomeWinRate"] = np.nan
    England_Matches_copy["H2H_HomeLossRate"] = np.nan
    England_Matches_copy["H2H_HomeDrawRate"] = np.nan

    for idx, row in England_Matches_copy.iterrows():
        home = row["HomeTeam"]
        away = row["AwayTeam"]
        match_date = row["MatchDate"]

        past_matches = England_Matches_copy[
            (
                (
                    (England_Matches_copy["HomeTeam"] == home)
                    & (England_Matches_copy["AwayTeam"] == away)
                )
                | (
                    (England_Matches_copy["HomeTeam"] == away)
                    & (England_Matches_copy["AwayTeam"] == home)
                )
            )
            & (England_Matches_copy["MatchDate"] < match_date)
        ]

        if past_matches.empty:
            continue

        def result_for_home(row):
            if row["HomeTeam"] == home:
                return row["FTResult"]
            else:  # HomeTeam != home => current home team was Away
                if row["FTResult"] == "H":
                    return "A"
                elif row["FTResult"] == "A":
                    return "H"
                else:
                    return "D"

        mapped_results = past_matches.apply(result_for_home, axis=1)

        win_rate = np.mean(mapped_results == "H")
        loss_rate = np.mean(mapped_results == "A")
        draw_rate = np.mean(mapped_results == "D")

        England_Matches_copy.at[idx, "H2H_HomeWinRate"] = win_rate
        England_Matches_copy.at[idx, "H2H_HomeLossRate"] = loss_rate
        England_Matches_copy.at[idx, "H2H_HomeDrawRate"] = draw_rate

    # Recent 5 games' trend
    result_history = defaultdict(list)
    home_trend_scores = []
    away_trend_scores = []


    def trend_score(results):
        return sum(results[-5:])


    for _, row in England_Matches_copy.iterrows():
        home_team = row["HomeTeam"]
        away_team = row["AwayTeam"]
        result = row["FTResult"]

        home_score = trend_score(result_history[home_team])
        away_score = trend_score(result_history[away_team])
        home_trend_scores.append(home_score)
        away_trend_scores.append(away_score)

        if result == "H":
            result_history[home_team].append(3)
            result_history[away_team].append(0)
        elif result == "A":
            result_history[home_team].append(0)
            result_history[away_team].append(3)
        else:  # Draw
            result_history[home_team].append(1)
            result_history[away_team].append(1)

    England_Matches_copy["HomeTrendScore5"] = home_trend_scores
    England_Matches_copy["AwayTrendScore5"] = away_trend_scores

    England_Matches_copy.dropna(inplace=True)

    # As mentioned before, Diff features are preferred
    England_Matches_copy["GoalsLast5Diff"] = (
        England_Matches_copy["HomeGoalsLast5"]
        - England_Matches_copy["AwayGoalsLast5"]
    )
    England_Matches_copy["ConcededLast5Diff"] = (
        England_Matches_copy["HomeConcededLast5"]
        - England_Matches_copy["AwayConcededLast5"]
    )
    England_Matches_copy["WinStreakDiff"] = (
        England_Matches_copy["HomeWinStreak"]
        - England_Matches_copy["AwayWinStreak"]
    )
    England_Matches_copy["ConcededLast5Diff"] = (
        England_Matches_copy["HomeConcededLast5"]
        - England_Matches_copy["AwayConcededLast5"]
    )
    England_Matches_copy["WinStreakDiff"] = (
        England_Matches_copy["HomeWinStreak"]
        - England_Matches_copy["AwayWinStreak"]
    )
    England_Matches_copy["LossStreakDiff"] = (
        England_Matches_copy["HomeLossStreak"]
        - England_Matches_copy["AwayLossStreak"]
    )
    England_Matches_copy["RestDaysDiff"] = (
        England_Matches_copy["HomeRestDays"] - England_Matches_copy["AwayRestDays"]
    )
    England_Matches_copy["EloMomentumDiff"] = (
        England_Matches_copy["HomeEloMomentum"]
        - England_Matches_copy["AwayEloMomentum"]
    )
    England_Matches_copy["DisciplineScoreDiff"] = (
        England_Matches_copy["HomeDisciplineScore"]
        - England_Matches_copy["AwayDisciplineScore"]
    )
    England_Matches_copy["AvgCornerDiff5Diff"] = (
        England_Matches_copy["HomeAvgCornerDiff5"]
        - England_Matches_copy["AwayAvgCornerDiff5"]
    )
    England_Matches_copy["AvgShotAcc5Diff"] = (
        England_Matches_copy["HomeAvgShotAcc5"]
        - England_Matches_copy["AwayAvgShotAcc5"]
    )
    England_Matches_copy["AvgShotDiff5Diff"] = (
        England_Matches_copy["HomeAvgShotDiff5"]
        - England_Matches_copy["AwayAvgShotDiff5"]
    )
    England_Matches_copy["TrendScore5Diff"] = (
        England_Matches_copy["HomeTrendScore5"]
        - England_Matches_copy["AwayTrendScore5"]
    )
    return (England_Matches_copy,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""Alright, now let's build a model without looking ahead to predict match result! Let's leave 1000 rows for final testing, no cheat!"""
    )
    return


@app.cell
def _(England_Matches_copy):
    df = England_Matches_copy[
        [
            "FTResult",
            "NetHomeGoal",
            "HomeElo",
            "AwayElo",
            "Over25",
            "MaxOver25",
            "HandiSize",
            "LOG_OddHome",
            "LOG_OddDraw",
            "LOG_OddAway",
            "LOG_MaxHome",
            "LOG_MaxDraw",
            "LOG_MaxAway",
            "LOG_Under25",
            "LOG_MaxUnder25",
            "LOG_HandiHome",
            "LOG_HandiAway",
            "EloDiff",
            "GoalsLast5Diff",
            "ConcededLast5Diff",
            "WinStreakDiff",
            "LossStreakDiff",
            "RestDaysDiff",
            "EloMomentumDiff",
            "DisciplineScoreDiff",
            "AvgCornerDiff5Diff",
            "AvgShotAcc5Diff",
            "AvgShotDiff5Diff",
            "TrendScore5Diff",
            "H2H_HomeWinRate",
            "H2H_HomeLossRate",
            "H2H_HomeDrawRate",
        ]
    ]


    FINAL_TESTING = df[-1000:]
    df = df[:-1000]
    return FINAL_TESTING, df


@app.cell
def _(
    ConfusionMatrixDisplay,
    GridSearchCV,
    LabelEncoder,
    Pipeline,
    StandardScaler,
    XGBClassifier,
    classification_report,
    df,
    make_scorer,
    np,
    plt,
    precision_score,
    train_test_split,
):
    X = df.drop(columns=["FTResult", "NetHomeGoal"])
    y = df["FTResult"]
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, stratify=y_encoded, test_size=0.2, random_state=322
    )


    def weighted_precision(y_true, y_pred):
        p_A = precision_score(
            y_true, y_pred, labels=[0], average="macro", zero_division=0
        )
        p_D = precision_score(
            y_true, y_pred, labels=[1], average="macro", zero_division=0
        )
        p_H = precision_score(
            y_true, y_pred, labels=[2], average="macro", zero_division=0
        )
        return 0.4 * p_A + 0.4 * p_H + 0.2 * p_D


    custom_precision_scorer = make_scorer(weighted_precision)

    class_counts = np.bincount(y_train)
    class_weights = {i: class_counts.max() / c for i, c in enumerate(class_counts)}
    sample_weights = np.array([class_weights[c] for c in y_train])

    model = XGBClassifier(
        use_label_encoder=False,
        eval_metric="mlogloss",
        objective="multi:softprob",
        num_class=3,  # NOTE: should be 3 for "H", "D", "A"
    )

    param_grid = {
        "clf__n_estimators": [15, 20, 50, 100, 150, 200, 300],
        "clf__max_depth": [2, 3, 5, 7],
        "clf__learning_rate": [0.0005, 0.001, 0.002],
    }

    pipe = Pipeline([("scaler", StandardScaler()), ("clf", model)])

    grid = GridSearchCV(
        pipe, param_grid, cv=3, scoring=custom_precision_scorer, n_jobs=-1
    )
    grid.fit(X_train, y_train, clf__sample_weight=sample_weights)

    best_model = grid.best_estimator_
    print(f"Best Params for XGBoost: {grid.best_params_}")

    y_pred = best_model.predict(X_test)
    y_test_decoded = le.inverse_transform(y_test)
    y_pred_decoded = le.inverse_transform(y_pred)

    ConfusionMatrixDisplay.from_predictions(
        y_test_decoded, y_pred_decoded, display_labels=le.classes_, cmap="Blues"
    )
    plt.title("XGBoost (Precision-Weighted Scoring)")
    plt.show()

    print("\nXGBoost Classification Report:\n")
    print(classification_report(y_test_decoded, y_pred_decoded, digits=3))
    return X, best_model, le


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Feature importance:""")
    return


@app.cell
def _(X, best_model, np, plt):
    final_xgb = best_model.named_steps["clf"]
    feature_names = X.columns

    importances = final_xgb.feature_importances_
    indices = np.argsort(importances)[::-1]

    top_n = 8  # number of top features to show

    plt.figure(figsize=(6, 6))
    plt.bar(range(top_n), importances[indices[:top_n]], align="center")
    plt.xticks(
        range(top_n), feature_names[indices[:top_n]], rotation=45, ha="right"
    )
    plt.title(f"Top {top_n} XGBoost Feature Importances")
    plt.tight_layout()
    plt.show()
    return (final_xgb,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""Seems like the book makers are already doing a great job, but our head-to-head probabilities also play some roles. Alright, let's check it out in the final test!"""
    )
    return


@app.cell
def _(
    ConfusionMatrixDisplay,
    FINAL_TESTING,
    best_model,
    classification_report,
    final_xgb,
    le,
    plt,
):
    X_FINAL_TESTING = FINAL_TESTING.drop(columns=["FTResult", "NetHomeGoal"])
    X_FINAL_TESTING_scaled = best_model.named_steps["scaler"].transform(
        X_FINAL_TESTING
    )

    y_pred_FINAL_TESTING = final_xgb.predict(X_FINAL_TESTING_scaled)
    y_pred_FINAL_TESTING_decoded = le.inverse_transform(y_pred_FINAL_TESTING)

    y_true_FINAL_TESTING = le.transform(FINAL_TESTING["FTResult"])

    print(
        classification_report(y_true_FINAL_TESTING, y_pred_FINAL_TESTING, digits=3)
    )

    ConfusionMatrixDisplay.from_predictions(
        le.inverse_transform(y_true_FINAL_TESTING),
        y_pred_FINAL_TESTING_decoded,
        display_labels=le.classes_,
        cmap="Blues",
    )
    plt.title("Evaluation on FINAL_TESTING")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Not bad!""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Future Improvement""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    1. Seems like the engineered features are not very important after all, and the `Odds` features are very important. This is making sense though, as I'm sure the gambling organizations have more detailed features of the matches and have better understanding of the chances;
    2. The model has very poor performance when predicting for Draw: this is a big problem in soccer match prediction in general. In fact, out model is doing pretty good in real-world standard, see [here](https://journalofbigdata.springeropen.com/articles/10.1186/s40537-024-01008-2);
    3. If we change the random state of sampling, sometimes the model's feature importance chances quite a bit, makes me wonder if the model is not very robust.
    """
    )
    return


if __name__ == "__main__":
    app.run()
