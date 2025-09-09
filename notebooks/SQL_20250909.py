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
            "/notebooks/SQL_20250908.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250910.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 2308

    Table: Genders

    | Column Name | Type    |
    |-------------|---------|
    | user_id     | int     |
    | gender      | varchar |

    user_id is the primary key (column with unique values) for this table. gender is ENUM (category) of type 'female', 'male', or 'other'. Each row in this table contains the ID of a user and their gender. The table has an equal number of 'female', 'male', and 'other'.
 
    Write a solution to rearrange the Genders table such that the rows alternate between 'female', 'other', and 'male' in order. The table should be rearranged such that the IDs of each gender are sorted in ascending order.

    Return the result table in the mentioned order.
    """
    )
    return


@app.cell
def _():
    """
    WITH gender_group_info AS(
        SELECT
            *,
            CASE
                WHEN gender = 'female' THEN 1
                WHEN gender = 'other' THEN 2
                ELSE 3
            END AS gender_group,
            ROW_NUMBER() OVER (PARTITION BY gender ORDER BY user_id) AS rank
        FROM
            Genders
    )
    SELECT
        user_id,
        gender
    FROM
        gender_group_info
    ORDER BY
        rank,
        gender_group
    """
    return


@app.cell
def _():
    import pandas as pd


    def arrange_table(genders: pd.DataFrame) -> pd.DataFrame:
        gender_map = {"female": 0, "other": 1, "male": 2}
        genders["group"] = genders["gender"].transform(lambda x: gender_map[x])
        genders["rank_within_group"] = genders.groupby("gender")["user_id"].rank(
            method="min"
        )
        return genders.sort_values(by=["rank_within_group", "group"])[
            ["user_id", "gender"]
        ]
    return


if __name__ == "__main__":
    app.run()
