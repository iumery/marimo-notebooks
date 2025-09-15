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
            "/notebooks/SQL_20250814.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250816.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 3521

    Table: ProductPurchases

    | Column Name | Type | 
    |-------------|------|
    | user_id     | int  |
    | product_id  | int  |
    | quantity    | int  |

    (user_id, product_id) is the unique key for this table. Each row represents a purchase of a product by a user in a specific quantity.

    Table: ProductInfo

    | Column Name | Type    | 
    |-------------|---------|
    | product_id  | int     |
    | category    | varchar |
    | price       | decimal |

    product_id is the primary key for this table. Each row assigns a category and price to a product.

    Amazon wants to implement the Customers who bought this also bought... feature based on co-purchase patterns. Write a solution to :

    - Identify distinct product pairs frequently purchased together by the same customers (where product1_id < product2_id)
    - For each product pair, determine how many customers purchased both products
    - A product pair is considered for recommendation if at least 3 different customers have purchased both products.
    - Return the result table ordered by customer_count in descending order, and in case of a tie, by product1_id in ascending order, and then by product2_id in ascending order.
    """
    )
    return


@app.cell
def _():
    """
    WITH pair_purchase AS (
        SELECT
            pp1.user_id,
            pp1.product_id AS product1_id,
            pp2.product_id AS product2_id
        FROM
            ProductPurchases pp1
                JOIN ProductPurchases pp2 ON pp1.user_id = pp2.user_id AND pp1.product_id < pp2.product_id
    )
    SELECT
        pp.product1_id,
        pp.product2_id,
        pi1.category AS product1_category,
        pi2.category AS product2_category,
        COUNT(DISTINCT pp.user_id) AS customer_count
    FROM
        pair_purchase pp
            JOIN ProductInfo pi1 ON pp.product1_id = pi1.product_id
            JOIN ProductInfo pi2 ON pp.product2_id = pi2.product_id
    GROUP BY
        1, 2, 3, 4
    HAVING
        COUNT(DISTINCT pp.user_id) >= 3
    ORDER BY
        5 DESC, 1, 2;

    """
    return


@app.cell
def _():
    import pandas as pd

    def find_product_recommendation_pairs(product_purchases: pd.DataFrame, product_info: pd.DataFrame) -> pd.DataFrame:
        pair_purchases = pd.merge(
            product_purchases[["user_id", "product_id"]],
            product_purchases[["user_id", "product_id"]],
            on="user_id",
        )
        pair_purchases.columns = ["user_id", "product1_id", "product2_id"]
        pair_purchases = pair_purchases[pair_purchases["product2_id"] > pair_purchases["product1_id"]]
        pair_purchases = pair_purchases.merge(
            product_info[["product_id", "category"]].rename(columns={"product_id": "product1_id"}),
            on="product1_id",
        )
        pair_purchases = pair_purchases.merge(
            product_info[["product_id", "category"]].rename(columns={"product_id": "product2_id"}),
            on="product2_id",
        )
        pair_purchases.columns = [
            "user_id",
            "product1_id",
            "product2_id",
            "product1_category",
            "product2_category",
        ]
        df = (
            pair_purchases.groupby(
                [
                    "product1_id",
                    "product2_id",
                    "product1_category",
                    "product2_category",
                ]
            )
            .agg(customer_count=("user_id", lambda x: x.nunique()))
            .reset_index()
        )
        df = df[df["customer_count"] >= 3]
        df.sort_values(
            by=["customer_count", "product1_id", "product2_id"],
            ascending=[0, 1, 1],
            inplace=True,
        )
        return df

    return


if __name__ == "__main__":
    app.run()
