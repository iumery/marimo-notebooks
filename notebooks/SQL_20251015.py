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
            "/notebooks/SQL_20251014.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251016.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 2987

    Table: Listings

    | Column Name | Type    |
    |-------------|---------|
    | listing_id  | int     |
    | city        | varchar |
    | price       | int     |

    listing_id is column of unique values for this table. This table contains listing_id, city, and price.

    Write a solution to find cities where the average home prices exceed the national average home price.

    Return the result table sorted by city in ascending order.
    """
    )
    return


@app.cell
def _():
    """
    SELECT
        city
    FROM
        Listings
    GROUP BY
        1
    HAVING
        AVG(price) > (SELECT AVG(price) FROM Listings)
    ORDER BY
        1;
    """
    return


@app.cell
def _():
    import pandas as pd

    def find_expensive_cities(listings: pd.DataFrame) -> pd.DataFrame:
        df = listings.copy()
        national_avg = df["price"].mean()
        df = df.groupby("city", as_index=False)["price"].mean()
        df = df[df["price"] > national_avg][["city"]].sort_values("city")
        return df

    return


if __name__ == "__main__":
    app.run()
