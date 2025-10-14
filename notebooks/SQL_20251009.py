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
            "/notebooks/SQL_20251008.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251010.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 2978

    Table: Coordinates

    | Column Name | Type |
    |-------------|------|
    | X           | int  |
    | Y           | int  |

    Each row includes X and Y, where both are integers. Table may contain duplicate values. Two coordindates (X1, Y1) and (X2, Y2) are said to be symmetric coordintes if X1 == Y2 and X2 == Y1.

    Write a solution that outputs, among all these symmetric coordintes, only those unique coordinates that satisfy the condition X1 <= Y1.

    Return the result table ordered by X and  Y (respectively) in ascending order.
    """
    )
    return


@app.cell
def _():
    """
    WITH listed_coordinates AS (
        SELECT
            *,
            ROW_NUMBER() over () AS rnk
        FROM
            Coordinates
    )
    SELECT DISTINCT
        lc1.X,
        lc1.Y
    FROM
        listed_coordinates lc1
            JOIN listed_coordinates lc2 ON lc1.X = lc2.Y AND lc1.Y = lc2.X AND lc1.X <= lc1.Y AND lc1.rnk <> lc2.rnk
    ORDER BY
        1, 2;
    """
    return


@app.cell
def _():
    import pandas as pd

    def symmetric_pairs(coordinates: pd.DataFrame) -> pd.DataFrame:
        coordinates["rnk"] = coordinates.index
        df = pd.merge(coordinates, coordinates, how="cross", suffixes=("_1", "_2"))
        df = df[(df["X_1"] == df["Y_2"]) & (df["X_2"] == df["Y_1"]) & (df["X_1"] <= df["Y_1"]) & (df["rnk_1"] != df["rnk_2"])]
        df = df[["X_1", "Y_1"]].drop_duplicates().rename(columns={"X_1": "x", "Y_1": "y"}).sort_values(by=["x", "y"])

        return df

    return


if __name__ == "__main__":
    app.run()
