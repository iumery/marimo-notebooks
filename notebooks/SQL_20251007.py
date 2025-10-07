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
            "/notebooks/SQL_20251006.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251008.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 2990

    Table: Loans

    | Column Name | Type    |
    |-------------|---------|
    | loan_id     | int     |
    | user_id     | int     |
    | loan_type   | varchar |

    loan_id is column of unique values for this table. This table contains loan_id, user_id, and loan_type.

    Write a solution to find all distinct user_id's that have at least one Refinance loan type and at least one Mortgage loan type.

    Return the result table ordered by user_id in ascending order.
    """
    )
    return


@app.cell
def _():
    """
    SELECT DISTINCT
        user_id
    FROM
        Loans
    WHERE
        user_id IN (
            SELECT user_id FROM Loans WHERE loan_type='Mortgage'
            INTERSECT
            SELECT user_id FROM Loans WHERE loan_type='Refinance'
        )
    ORDER BY
        1;
    """
    return


@app.cell
def _():
    import pandas as pd


    def loan_types(loans: pd.DataFrame) -> pd.DataFrame:
        summary = loans.pivot_table(
            index="user_id",
            columns="loan_type",
            values="loan_id",
            aggfunc="count",
        ).reset_index()
        df = summary[(summary["Mortgage"] > 0) & (summary["Refinance"] > 0)][
            ["user_id"]
        ]
        return df
    return


if __name__ == "__main__":
    app.run()
