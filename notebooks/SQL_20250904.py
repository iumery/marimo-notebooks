import marimo

__generated_with = "0.14.16"
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
            "/notebooks/SQL_20250903.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250905.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 2175

    Table: TeamPoints

    | Column Name | Type    |
    |-------------|---------|
    | team_id     | int     |
    | name        | varchar |
    | points      | int     |

    team_id contains unique values. Each row of this table contains the ID of a national team, the name of the country it represents, and the points it has in the global rankings. No two teams will represent the same country.

    Table: PointsChange

    | Column Name   | Type |
    |---------------|------|
    | team_id       | int  |
    | points_change | int  |

    team_id contains unique values. Each row of this table contains the ID of a national team and the change in its points in the global rankings.

    points_change can be:

    - 0: indicates no change in points.
    - positive: indicates an increase in points.
    - negative: indicates a decrease in points.

    Each team_id that appears in TeamPoints will also appear in this table.
 
    The global ranking of a national team is its rank after sorting all the teams by their points in descending order. If two teams have the same points, we break the tie by sorting them by their name in lexicographical order.

    The points of each national team should be updated based on its corresponding points_change value.

    Write a solution to calculate the change in the global rankings after updating each team's points.

    Return the result table in any order.
    """
    )
    return


@app.cell
def _():
    """
    SELECT
        team_id,
        name,
        ROW_NUMBER() OVER (ORDER BY points DESC, name ASC) - ROW_NUMBER() OVER (ORDER BY points + points_change DESC, name ASC) AS rank_diff
    FROM
        TeamPoints
            JOIN PointsChange USING(team_id);
    """
    return


@app.cell
def _():
    import pandas as pd


    def global_ratings_change(
        team_points: pd.DataFrame, points_change: pd.DataFrame
    ) -> pd.DataFrame:
        df = pd.merge(team_points, points_change, on="team_id")
        df["new_points"] = df["points"] + df["points_change"]
        df.sort_values(
            by=["points", "name"], ascending=[False, True], inplace=True
        )
        df["old_rank"] = df.reset_index(drop=True).index
        df.sort_values(
            by=["new_points", "name"], ascending=[False, True], inplace=True
        )
        df["new_rank"] = df.reset_index(drop=True).index
        df["rank_diff"] = df["old_rank"] - df["new_rank"]
        return df[["team_id", "name", "rank_diff"]]
    return


if __name__ == "__main__":
    app.run()
