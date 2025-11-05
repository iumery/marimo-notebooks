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
            "/notebooks/SQL_20251107.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251111.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### LeetCode 3061

    Table: Heights

    | Column Name | Type |
    |-------------|------|
    | id          | int  |
    | height      | int  |

    id is the primary key (column with unique values) for this table, and it is guaranteed to be in sequential order. Each row of this table contains an id and height.

    Write a solution to calculate the amount of rainwater can be trapped between the bars in the landscape, considering that each bar has a width of 1 unit.

    Return the result table in any order.
    """)
    return


@app.cell
def _():
    """
    SELECT
        SUM(trapped_water) AS total_trapped_water
    FROM (
        SELECT
            LEAST(
                (MAX(height) OVER (ORDER BY id ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)) - height,
                (MAX(height) OVER (ORDER BY id ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING)) - height
            ) AS trapped_water
        FROM
            Heights
    ) sub;
    """
    return


@app.cell
def _():
    import pandas as pd


    def calculate_trapped_rain_water(heights: pd.DataFrame) -> pd.DataFrame:
        df = heights.sort_values("id")
        df["max_preceding_height"] = df["height"].cummax()
        df = df.sort_values("id", ascending=False)
        df["max_following_height"] = df["height"].cummax()
        df = df.sort_values("id")
        df["trapped_water"] = (
            df[["max_preceding_height", "max_following_height"]].min(axis=1)
            - df["height"]
        )
        total_trapped_water = sum(df["trapped_water"])
        df = pd.DataFrame({"total_trapped_water": [total_trapped_water]})
        return df
    return


if __name__ == "__main__":
    app.run()
