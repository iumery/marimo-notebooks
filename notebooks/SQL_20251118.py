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
            "/notebooks/SQL_20251117.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251119.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### LeetCode 3126

    Table: Servers

    | Column Name    | Type     |
    |----------------|----------|
    | server_id      | int      |
    | status_time    | datetime |
    | session_status | enum     |

    (server_id, status_time, session_status) is the primary key (combination of columns with unique values) for this table. session_status is an ENUM (category) type of ('start', 'stop'). Each row of this table contains server_id, status_time, and session_status.

    Write a solution to find the total time when servers were running. The output should be rounded down to the nearest number of full days.

    Return the result table in any order.
    """)
    return


@app.cell
def _():
    """
    SELECT
        SUM((CASE WHEN session_status = 'start' THEN -1 ELSE 1 END) * EXTRACT(EPOCH FROM status_time)::INT)/(24*60*60) AS total_uptime_days
    FROM
        Servers;
    """
    return


@app.cell
def _():
    import pandas as pd


    def server_utilization_time(servers: pd.DataFrame) -> pd.DataFrame:
        df = servers.copy()
        df["status_time_seconds"] = df["status_time"].astype(int) // 10**9
        df["session_status_int"] = (
            df["session_status"].map({"start": -1, "stop": 1}).astype(int)
        )
        total_uptime_days = (
            df["status_time_seconds"] * df["session_status_int"]
        ).sum() // (24 * 60 * 60)
        return pd.DataFrame({"total_uptime_days": [total_uptime_days]})
    return


if __name__ == "__main__":
    app.run()
