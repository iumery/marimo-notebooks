import marimo

__generated_with = "0.15.3"
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
            "/notebooks/SQL_20250912.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250916.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 2339

    Table: Teams

    | Column Name | Type    |
    |-------------|---------|
    | team_name   | varchar |

    team_name is the column with unique values of this table. Each row of this table shows the name of a team.

    Write a solution to report all the possible matches of the league. Note that every two teams play two matches with each other, with one team being the home_team once and the other time being the away_team.

    Return the result table in any order.
    """
    )
    return


@app.cell
def _():
    """
    SELECT
        t1.team_name AS home_team,
        t2.team_name AS away_team
    FROM
        Teams t1
            JOIN Teams t2 ON t1.team_name <> t2.team_name;
    """
    return


@app.cell
def _():
    import pandas as pd


    def find_all_matches(teams: pd.DataFrame) -> pd.DataFrame:
        df = pd.merge(teams, teams, how="cross")
        df.columns = ["home_team", "away_team"]
        df = df[df["home_team"] != df["away_team"]]
        return df
    return


if __name__ == "__main__":
    app.run()
