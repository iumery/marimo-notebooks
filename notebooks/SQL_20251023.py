import marimo

__generated_with = "0.16.5"
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
            "/notebooks/SQL_20251022.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251024.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 2995

    Table: Sessions

    | Column Name   | Type     |
    |---------------|----------|
    | user_id       | int      |
    | session_start | datetime |
    | session_end   | datetime |
    | session_id    | int      |
    | session_type  | enum     |

    session_id is column of unique values for this table. session_type is an ENUM (category) type of (Viewer, Streamer). This table contains user id, session start, session end, session id and session type.

    Write a solution to find the number of streaming sessions for users whose first session was as a viewer.

    Return the result table ordered by count of streaming sessions,  user_id in descending order.
    """
    )
    return


@app.cell
def _():
    """
    WITH users AS (
        SELECT DISTINCT
            user_id,
            FIRST_VALUE(session_type) OVER (PARTITION BY user_id ORDER BY session_start) AS first_session_type
        FROM
            Sessions
    )
    SELECT
        user_id,
        COUNT(session_id) AS sessions_count
    FROM
        users
            JOIN Sessions USING (user_id)
    WHERE
        first_session_type = 'Viewer'
            AND session_type = 'Streamer'
    GROUP BY
        1
    ORDER BY
        2 desc,
        1 desc;
    """
    return


@app.cell
def _():
    import pandas as pd

    def count_turned_streamers(sessions: pd.DataFrame) -> pd.DataFrame:
        df = sessions.sort_values(by=["user_id", "session_start"])
        df["first_session_type"] = df.groupby("user_id")["session_type"].transform("first")
        df = (
            df[(df["session_type"] == "Streamer") & (df["first_session_type"] == "Viewer")]
            .groupby("user_id")["session_id"]
            .agg("count")
            .reset_index(name="sessions_count")
        )
        df.sort_values(
            by=["sessions_count", "user_id"],
            ascending=[False, False],
            inplace=True,
        )
        return df

    return


if __name__ == "__main__":
    app.run()
