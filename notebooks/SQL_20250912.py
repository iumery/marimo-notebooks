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
            "/notebooks/SQL_20250911.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250915.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 2329

    Table: Sales

    | Column Name | Type  |
    |-------------|-------|
    | sale_id     | int   |
    | product_id  | int   |
    | user_id     | int   |
    | quantity    | int   |

    sale_id contains unique values. product_id is a foreign key (column with unique values) to Product table. Each row of this table shows the ID of the product and the quantity purchased by a user.

    Table: Product

    | Column Name | Type |
    |-------------|------|
    | product_id  | int  |
    | price       | int  |

    product_id contains unique values. Each row of this table indicates the price of each product.

    Write a solution to report the spending of each user.

    Return the resulting table ordered by spending in descending order. In case of a tie, order them by user_id in ascending order.
    """
    )
    return


@app.cell
def _():
    """
    SELECT
        user_id,
        SUM(price * quantity) AS spending
    FROM
        Sales
            JOIN Product USING (product_id)
    GROUP BY
        1
    ORDER BY
        2 DESC,
        1;
    """
    return


@app.cell
def _():
    import pandas as pd

    def product_sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
        df = pd.merge(sales, product, on="product_id")
        df["spending"] = df["quantity"] * df["price"]
        df = df.groupby("user_id", as_index=False)["spending"].sum().sort_values(by=["spending", "user_id"], ascending=[False, True])
        return df

    return


if __name__ == "__main__":
    app.run()
