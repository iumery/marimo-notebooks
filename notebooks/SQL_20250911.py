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
            "/notebooks/SQL_20250910.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250912.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 2324

    Table: Sales

    | Column Name | Type  |
    |-------------|-------|
    | sale_id     | int   |
    | product_id  | int   |
    | user_id     | int   |
    | quantity    | int   |

    sale_id contains unique values. product_id is a foreign key (reference column) to Product table. Each row of this table shows the ID of the product and the quantity purchased by a user.
 
    Table: Product

    | Column Name | Type |
    |-------------|------|
    | product_id  | int  |
    | price       | int  |

    product_id contains unique values. Each row of this table indicates the price of each product.

    Write a solution that reports for each user the product id on which the user spent the most money. In case the same user spent the most money on two or more products, report all of them.

    Return the resulting table in any order.
    """
    )
    return


@app.cell
def _():
    """
    WITH total_price_info_rank AS (
        SELECT
            product_id,
            user_id,
            RANK() OVER (PARTITION BY user_id ORDER BY SUM(quantity * price) DESC) AS rank
        FROM
            Sales
                JOIN Product USING (product_id)
        GROUP BY
            1, 2
    )
    SELECT
        user_id,
        product_id
    FROM
        total_price_info_rank
    WHERE
        rank = 1;
    """
    return


@app.cell
def _():
    import pandas as pd

    def product_sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
        df = pd.merge(sales, product, on="product_id")
        df["total"] = df["quantity"] * df["price"]
        df = df.groupby(["user_id", "product_id"], as_index=False)["total"].sum()
        df["rank"] = df.groupby("user_id")["total"].rank(method="min", ascending=False).astype(int)
        df = df[df["rank"] == 1][["user_id", "product_id"]]
        return df

    return


if __name__ == "__main__":
    app.run()
