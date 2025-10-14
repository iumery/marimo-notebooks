import marimo

__generated_with = "0.15.4"
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
            "/notebooks/SQL_20250918.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250922.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 2377

    Table: Olympic

    | Column Name   | Type    |
    |---------------|---------|
    | country       | varchar |
    | gold_medals   | int     |
    | silver_medals | int     |
    | bronze_medals | int     |

    In SQL, country is the primary key for this table. Each row in this table shows a country name and the number of gold, silver, and bronze medals it won in the Olympic games.

    The Olympic table is sorted according to the following rules:

    - The country with more gold medals comes first.
    - If there is a tie in the gold medals, the country with more silver medals comes first.
    - If there is a tie in the silver medals, the country with more bronze medals comes first.
    - If there is a tie in the bronze medals, the countries with the tie are sorted in ascending order lexicographically.

    Write a solution to sort the Olympic table.
    """
    )
    return


@app.cell
def _():
    """
    SELECT
        country,
        gold_medals,
        silver_medals,
        bronze_medals
    FROM
        Olympic
    ORDER BY
        2 DESC, 3 DESC, 4 DESC, 1;
    """
    return


@app.cell
def _():
    import pandas as pd

    def sort_table(olympic: pd.DataFrame) -> pd.DataFrame:
        return olympic.sort_values(
            by=["gold_medals", "silver_medals", "bronze_medals", "country"],
            ascending=[False, False, False, True],
        )

    return


if __name__ == "__main__":
    app.run()
