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
            "/notebooks/SQL_20250813.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250815.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 3554

    Table: ProductPurchases

    | Column Name | Type | 
    |-------------|------|
    | user_id     | int  |
    | product_id  | int  |
    | quantity    | int  |

    (user_id, product_id) is the unique identifier for this table. Each row represents a purchase of a product by a user in a specific quantity.

    Table: ProductInfo

    | Column Name | Type    | 
    |-------------|---------|
    | product_id  | int     |
    | category    | varchar |
    | price       | decimal |

    product_id is the unique identifier for this table. Each row assigns a category and price to a product.

    Amazon wants to understand shopping patterns across product categories. Write a solution to:

    - Find all category pairs (where category1 < category2)
    - For each category pair, determine the number of unique customers who purchased products from both categories
    - A category pair is considered reportable if at least 3 different customers have purchased products from both categories.
    - Return the result table of reportable category pairs ordered by customer_count in descending order, and in case of a tie, by category1 in ascending order lexicographically, and then by category2 in ascending order.
    """
    )
    return


@app.cell
def _():
    """
    WITH user_category AS (
        SELECT DISTINCT
            user_id,
            category
        FROM
            ProductPurchases
                JOIN ProductInfo USING(product_id)
    ),
    user_2_category AS (
        SELECT
            u1.category AS category1,
            u2.category AS category2,
            u1.user_id
        FROM
            user_category u1
                JOIN user_category u2 ON u1.user_id = u2.user_id and u1.category < u2.category
    )
    SELECT
        category1,
        category2,
        COUNT(*) AS customer_count
    FROM
        user_2_category
    GROUP BY
        1,2
    HAVING
        COUNT(*) >= 3
    ORDER BY
        3 DESC, 1, 2;
    """
    return


@app.cell
def _():
    import pandas as pd


    def find_category_recommendation_pairs(
        product_purchases: pd.DataFrame, product_info: pd.DataFrame
    ) -> pd.DataFrame:
        df = product_purchases.merge(
            product_info[["product_id", "category"]], on="product_id", how="inner"
        )
        user_cat = df[["user_id", "category"]].drop_duplicates()
        pairs = user_cat.merge(user_cat, on="user_id", suffixes=("1", "2")).query(
            "category1 < category2"
        )[["category1", "category2"]]

        if pairs.empty:
            return pd.DataFrame(
                columns=["category1", "category2", "customer_count"]
            )
        out = (
            pairs.groupby(["category1", "category2"])
            .size()
            .rename("customer_count")
            .reset_index()
        )
        out = (
            out[out["customer_count"] >= 3]
            .sort_values(
                ["customer_count", "category1", "category2"],
                ascending=[False, True, True],
            )
            .reset_index(drop=True)
        )

        return out
    return


if __name__ == "__main__":
    app.run()
