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
            "/notebooks/SQL_20250902.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250904.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 2159

    Table: Data

    | Column Name | Type |
    |-------------|------|
    | first_col   | int  |
    | second_col  | int  |

    This table may contain duplicate rows.
 
    Write a solution to independently:

    - order first_col in ascending order.
    - order second_col in descending order.
    """
    )
    return


@app.cell
def _():
    """
    WITH first_col_ranked AS (
        SELECT
            first_col,
            ROW_NUMBER() OVER (ORDER BY first_col) AS rank
        FROM
            Data
    ),
    second_col_ranked AS (
        SELECT
            second_col,
            ROW_NUMBER() OVER (ORDER BY second_col DESC) AS rank
        FROM
            Data
    )
    SELECT
        first_col,
        second_col
    FROM
        first_col_ranked
            JOIN second_col_ranked USING(rank)
    ORDER BY
        rank;
    """
    return


@app.cell
def _():
    import pandas as pd


    def order_two_columns(data: pd.DataFrame) -> pd.DataFrame:
        first_data = (
            data["first_col"].sort_values(ascending=True).reset_index(drop=True)
        )
        second_data = (
            data["second_col"].sort_values(ascending=False).reset_index(drop=True)
        )
        return pd.concat([first_data, second_data], axis=1)
    return


if __name__ == "__main__":
    app.run()
