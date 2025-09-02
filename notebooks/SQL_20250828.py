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
            "/notebooks/SQL_20250827.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250829.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 1204

    Table: Queue

    | Column Name | Type    |
    |-------------|---------|
    | person_id   | int     |
    | person_name | varchar |
    | weight      | int     |
    | turn        | int     |

    person_id column contains unique values. This table has the information about all people waiting for a bus. The person_id and turn columns will contain all numbers from 1 to n, where n is the number of rows in the table. turn determines the order of which the people will board the bus, where turn=1 denotes the first person to board and turn=n denotes the last person to board. weight is the weight of the person in kilograms.
 

    There is a queue of people waiting to board a bus. However, the bus has a weight limit of 1000 kilograms, so there may be some people who cannot board.

    Write a solution to find the person_name of the last person that can fit on the bus without exceeding the weight limit. The test cases are generated such that the first person does not exceed the weight limit.

    Note that only one person can board the bus at any given turn.
    """
    )
    return


@app.cell
def _():
    """
    WITH total_weight_table AS (
    SELECT
        turn,
        person_name,
        weight,
        SUM(weight) OVER (ORDER BY turn ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS total_weight
    FROM
        Queue
    )
    SELECT
        person_name
    FROM
        total_weight_table
    WHERE
        total_weight <= 1000
    ORDER BY
        turn DESC
    LIMIT
        1;
    """
    return


@app.cell
def _():
    import pandas as pd


    def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
        df = queue[["turn", "person_name", "weight"]].sort_values("turn")
        df["total_weight"] = df["weight"].cumsum()
        df = df[df["total_weight"] <= 1000].iloc[[-1]][["person_name"]]
        return df
    return


if __name__ == "__main__":
    app.run()
