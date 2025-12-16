import marimo

__generated_with = "0.18.1"
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
            "/notebooks/SQL_20251215.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251217.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### LeetCode 1097

    Table: Activity

    | Column Name  | Type    |
    |--------------|---------|
    | player_id    | int     |
    | device_id    | int     |
    | event_date   | date    |
    | games_played | int     |

    (player_id, event_date) is the primary key (combination of columns with unique values) of this table. This table shows the activity of players of some games. Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.

    The install date of a player is the first login day of that player.

    We define day one retention of some date x to be the number of players whose install date is x and they logged back in on the day right after x, divided by the number of players whose install date is x, rounded to 2 decimal places.

    Write a solution to report for each install date, the number of players that installed the game on that day, and the day one retention.

    Return the result table in any order.
    """)
    return


@app.cell
def _():
    """
    WITH retention_info AS (
        SELECT DISTINCT ON (player_id)
            player_id,
            event_date,
            CASE WHEN (LEAD(event_date, 1) OVER (PARTITION BY player_id ORDER BY event_date) - event_date) = 1 THEN 1 ELSE 0 END AS Day1_retention
        FROM
            Activity
        ORDER BY
            1, 2
    )
    SELECT
        event_date AS install_dt,
        COUNT(*) AS installs,
        ROUND(AVG(Day1_retention),2) AS Day1_retention
    FROM
        retention_info
    GROUP BY
        1
    ORDER BY
        1;
    """
    return


@app.cell
def _(mean):
    import pandas as pd


    def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
        df = activity.sort_values(["player_id", "event_date"])
        df["next_event_date"] = df.groupby("player_id")["event_date"].shift(-1)
        df = df.groupby("player_id", as_index=False).first()
        df["Day1_retention"] = (
            (df["next_event_date"] - df["event_date"]).dt.days
        ) == 1
        df = df.groupby("event_date", as_index=False).agg(
            installs=("player_id", "count"),
            Day1_retention=("Day1_retention", lambda x: round(mean(x), 2)),
        )
        df.rename(columns={"event_date": "install_dt"}, inplace=True)
        return df
    return


if __name__ == "__main__":
    app.run()
