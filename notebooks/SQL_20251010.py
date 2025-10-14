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
            "/notebooks/SQL_20251009.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251013.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 2984

    Table: Calls

    | Column Name  | Type     |
    |--------------|----------|
    | caller_id    | int      |
    | recipient_id | int      |
    | call_time    | datetime |
    | city         | varchar  |

    (caller_id, recipient_id, call_time) is the primary key (combination of columns with unique values) for this table. Each row contains caller id, recipient id, call time, and city.

    Write a solution to find the peak calling hour for each city. If multiple hours have the same number of calls, all of those hours will be recognized as peak hours for that specific city.

    Return the result table ordered by peak calling hour and city in descending order.
    """
    )
    return


@app.cell
def _():
    """
    WITH ranking_info AS (
        SELECT
            city,
            EXTRACT(HOUR FROM call_time) AS peak_calling_hour,
            COUNT(*) AS number_of_calls,
            DENSE_RANK() OVER (PARTITION BY city ORDER BY COUNT(*) DESC) AS rnk
        FROM
            Calls
        GROUP BY
            1, 2
    )
    SELECT
        city,
        peak_calling_hour,
        number_of_calls
    FROM
        ranking_info
    WHERE
        rnk = 1
    ORDER BY
        2 DESC, 1 DESC;
    """
    return


@app.cell
def _():
    import pandas as pd

    def peak_calling_hours(calls: pd.DataFrame) -> pd.DataFrame:
        df = calls.copy()
        df["peak_calling_hour"] = df["call_time"].dt.hour
        df = df.groupby(["city", "peak_calling_hour"])["caller_id"].count().reset_index(name="number_of_calls")
        df["rnk"] = df.groupby("city")["number_of_calls"].rank(method="min", ascending=False)
        df = df[df["rnk"] == 1].sort_values(by=["peak_calling_hour", "city"], ascending=[False, False])[
            ["city", "peak_calling_hour", "number_of_calls"]
        ]
        return df

    return


if __name__ == "__main__":
    app.run()
