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
            "/notebooks/SQL_20251205.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251209.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### LeetCode 3673

    Table: app_events

    | Column Name      | Type     |
    |------------------|----------|
    | event_id         | int      |
    | user_id          | int      |
    | event_timestamp  | datetime |
    | event_type       | varchar  |
    | session_id       | varchar  |
    | event_value      | int      |

    event_id is the unique identifier for this table. event_type can be app_open, click, scroll, purchase, or app_close. session_id groups events within the same user session. event_value represents: for purchase - amount in dollars, for scroll - pixels scrolled, for others - NULL.

    Write a solution to identify zombie sessions, sessions where users appear active but show abnormal behavior patterns. A session is considered a zombie session if it meets ALL the following criteria:

    - The session duration is more than 30 minutes.
    - Has at least 5 scroll events.
    - The click-to-scroll ratio is less than 0.20 .
    - No purchases were made during the session.

    Return the result table ordered by scroll_count in descending order, then by session_id in ascending order.
    """)
    return


@app.cell
def _():
    """
    SELECT
        session_id,
        user_id,
        EXTRACT(EPOCH FROM MAX(event_timestamp) - MIN(event_timestamp)) / 60 AS session_duration_minutes,
        COUNT(*) FILTER (WHERE event_type = 'scroll') AS scroll_count
    FROM
        app_events
    GROUP BY
        1, 2
    HAVING
        MAX(event_timestamp) - INTERVAL '30 mins' > MIN(event_timestamp)
            AND COUNT(*) FILTER (WHERE event_type = 'scroll') >= 5
            AND ROUND(
                (COUNT(*) FILTER (WHERE event_type = 'click'))::NUMERIC /
                (COUNT(*) FILTER (WHERE event_type = 'scroll'))::NUMERIC, 2
                ) < 0.2
            AND COUNT(*) FILTER (WHERE event_type = 'purchase') = 0
    ORDER BY
        4 DESC, 1;
    """
    return


@app.cell
def _():
    import pandas as pd


    def find_zombie_sessions(app_events: pd.DataFrame) -> pd.DataFrame:
        df = app_events.copy()
        df["event_timestamp"] = pd.to_datetime(df["event_timestamp"])
        df = df.groupby(["session_id", "user_id"], as_index=False).agg(
            purchase_count=("event_type", lambda x: (x == "purchase").sum()),
            scroll_count=("event_type", lambda x: (x == "scroll").sum()),
            click_count=("event_type", lambda x: (x == "click").sum()),
            max_time=("event_timestamp", max),
            min_time=("event_timestamp", min),
        )
        df["session_duration_minutes"] = (
            df["max_time"] - df["min_time"]
        ).dt.seconds / 60
        df = df[
            (df.session_duration_minutes > 30)
            & (df.scroll_count >= 5)
            & (5 * df.click_count < df.scroll_count)
            & (df.purchase_count == 0)
        ][["session_id", "user_id", "session_duration_minutes", "scroll_count"]]
        df.sort_values(
            ["scroll_count", "session_id"], ascending=[False, True], inplace=True
        )
        return df
    return


if __name__ == "__main__":
    app.run()
