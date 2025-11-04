import marimo

__generated_with = "0.17.4"
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
            "/notebooks/SQL_20251106.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251110.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### LeetCode 3060

    Table: Sessions

    | Column Name   | Type     |
    |---------------|----------|
    | user_id       | int      |
    | session_start | datetime |
    | session_end   | datetime |
    | session_id    | int      |
    | session_type  | enum     |

    session_id is column of unique values for this table. session_type is an ENUM (category) type of (Viewer, Streamer). This table contains user id, session start, session end, session id and session type.

    Write a solution to find the the users who have had at least two session of the same type (either 'Viewer' or 'Streamer') with a maximum gap of 12 hours between sessions.

    Return the result table ordered by user_id in ascending order.
    """)
    return


@app.cell
def _():
    """
    SELECT DISTINCT
        s1.user_id
    FROM
        Sessions s1
            JOIN Sessions s2 ON s1.user_id = s2.user_id
                AND s1.session_type = s2.session_type
                AND s1.session_start < s2.session_start
                AND s2.session_start - s1.session_end <= INTERVAL '12 hour'
    ORDER BY
        1;
    """
    return


@app.cell
def _():
    import pandas as pd


    def user_activities(sessions: pd.DataFrame) -> pd.DataFrame:
        df = sessions.sort_values(by=["user_id", "session_type", "session_start"])
        df["next_session_start"] = df.groupby(["user_id", "session_type"])[
            "session_start"
        ].shift(-1)
        df["diff_hours"] = (
            df["next_session_start"] - df["session_end"]
        ).dt.total_seconds() / 3600
        df = (
            df[df["diff_hours"] <= 12][["user_id"]]
            .drop_duplicates()
            .sort_values(by="user_id")
        )

        return df
    return


if __name__ == "__main__":
    app.run()
