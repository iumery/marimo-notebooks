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
            "/notebooks/SQL_20250916.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250918.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 2362

    Table: Products

    | Column Name | Type |
    |-------------|------|
    | product_id  | int  |
    | price       | int  |

    product_id contains unique values. Each row in this table shows the ID of a product and the price of one unit.

    Table: Purchases

    | Column Name | Type |
    |-------------|------|
    | invoice_id  | int  |
    | product_id  | int  |
    | quantity    | int  |

    (invoice_id, product_id) is the primary key (combination of columns with unique values) for this table. Each row in this table shows the quantity ordered from one product in an invoice. 

    Write a solution to show the details of the invoice with the highest price. If two or more invoices have the same price, return the details of the one with the smallest invoice_id.

    Return the result table in any order.
    """
    )
    return


@app.cell
def _():
    """
    SELECT
        product_id,
        quantity,
        quantity * price AS price
    FROM
        Purchases
            JOIN Products USING (product_id)
    WHERE
        invoice_id IN (
            SELECT
                invoice_id
            FROM (
                SELECT
                    invoice_id,
                    SUM(quantity * price) AS invoice_price
                FROM
                    Purchases
                        JOIN Products USING (product_id)
                GROUP BY
                    1
                ORDER BY
                    2 DESC, 1
                LIMIT 1
            )
        )
    """
    return


@app.cell
def _():
    import pandas as pd

    def generate_the_invoice(products: pd.DataFrame, purchases: pd.DataFrame) -> pd.DataFrame:
        df = pd.merge(purchases, products, on="product_id")
        df["price"] = df["quantity"] * df["price"]
        top: int = (
            df.groupby("invoice_id", as_index=False)["price"]
            .sum()
            .sort_values(by=["price", "invoice_id"], ascending=[False, True])
            .iloc[0]
            .loc["invoice_id"]
        )
        df = df[df["invoice_id"] == top][["product_id", "quantity", "price"]]
        return df

    return


if __name__ == "__main__":
    app.run()
