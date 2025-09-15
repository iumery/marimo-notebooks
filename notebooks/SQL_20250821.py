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
            "/notebooks/SQL_20250820.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250822.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 601

    Table: Stadium

    | Column Name   | Type    |
    |---------------|---------|
    | id            | int     |
    | visit_date    | date    |
    | people        | int     |

    visit_date is the column with unique values for this table. Each row of this table contains the visit date and visit id to the stadium with the number of people during the visit. As the id increases, the date increases as well.
 
    Write a solution to display the records with three or more rows with consecutive id's, and the number of people is greater than or equal to 100 for each.

    Return the result table ordered by visit_date in ascending order.
    """
    )
    return


@app.cell
def _():
    """
    WITH group_info AS (
        SELECT
            id,
            visit_date,
            people,
            ROW_NUMBER() OVER (ORDER BY id) - id AS cons_group
        FROM
            Stadium
        WHERE
            people >= 100
    )
    SELECT
        id,
        visit_date,
        people
    FROM
        group_info
    WHERE
        cons_group IN (SELECT cons_group FROM group_info GROUP BY 1 HAVING COUNT(*) >= 3)
    ORDER BY
        2;
    """
    return


@app.cell
def _():
    import pandas as pd

    def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
        high_traffic = stadium[stadium["people"] >= 100].reset_index(drop=True)
        high_traffic["cons_group"] = pd.Series(range(0, len(high_traffic))) - high_traffic["id"]
        group_count = high_traffic.groupby("cons_group")["id"].count()
        high_groups = group_count[group_count >= 3].index.to_list()
        return high_traffic[high_traffic["cons_group"].isin(high_groups)][["id", "visit_date", "people"]].reset_index(drop=True)

    return


if __name__ == "__main__":
    app.run()
