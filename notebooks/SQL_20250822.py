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
            "/notebooks/SQL_20250821.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250825.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 1070

    Table: Sales

    | Column Name | Type  |
    |-------------|-------|
    | sale_id     | int   |
    | product_id  | int   |
    | year        | int   |
    | quantity    | int   |
    | price       | int   |

    (sale_id, year) is the primary key (combination of columns with unique values) of this table. product_id is a foreign key (reference column) to Product table. Each row records a sale of a product in a given year. A product may have multiple sales entries in the same year. Note that the per-unit price.

    Write a solution to find all sales that occurred in the first year each product was sold.

    - For each product_id, identify the earliest year it appears in the Sales table.
    - Return all sales entries for that product in that year.
    - Return a table with the following columns: product_id, first_year, quantity, and price.
    - Return the result in any order.
    """
    )
    return


@app.cell
def _():
    """
    WITH first_year_info AS (
        SELECT
            product_id,
            MIN(year) AS year
        FROM
            Sales
        GROUP BY
            product_id
    )
    SELECT
        s.product_id,
        s.year AS first_year,
        s.quantity,
        s.price
    FROM
        Sales s
            JOIN first_year_info f ON s.product_id = f.product_id AND s.year = f.year;
    """
    return


@app.cell
def _():
    import pandas as pd

    def sales_analysis(sales: pd.DataFrame) -> pd.DataFrame:
        first_year = sales.groupby("product_id")["year"].min().reset_index()
        first_year.columns = ["product_id", "year"]
        df = pd.merge(sales, first_year, on=["product_id", "year"], how="inner")
        return df[["product_id", "year", "quantity", "price"]].rename(columns={"year": "first_year"})

    return


if __name__ == "__main__":
    app.run()
