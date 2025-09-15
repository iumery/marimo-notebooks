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
            "/notebooks/SQL_20250812.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250814.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 3564

    Table: sales

    | Column Name   | Type    |
    |---------------|---------|
    | sale_id       | int     |
    | product_id    | int     |
    | sale_date     | date    |
    | quantity      | int     |
    | price         | decimal |

    sale_id is the unique identifier for this table. Each row contains information about a product sale including the product_id, date of sale, quantity sold, and price per unit.

    Table: products

    | Column Name   | Type    |
    |---------------|---------|
    | product_id    | int     |
    | product_name  | varchar |
    | category      | varchar |

    product_id is the unique identifier for this table. Each row contains information about a product including its name and category.

    Write a solution to find the most popular product category for each season.

    - The seasons are defined as:
        - Winter: December, January, February
        - Spring: March, April, May
        - Summer: June, July, August
        - Fall: September, October, November
    - The popularity of a category is determined by the total quantity sold in that season. If there is a tie, select the category with the highest total revenue (quantity × price).
    - Return the result table ordered by season in ascending order.
    """
    )
    return


@app.cell
def _():
    """
    WITH season_sales AS (
        SELECT
            *,
            CASE
                WHEN EXTRACT(MONTH FROM sale_date) IN (12, 1, 2) THEN 'Winter'
                WHEN EXTRACT(MONTH FROM sale_date) IN (3, 4, 5) THEN 'Spring'
                WHEN EXTRACT(MONTH FROM sale_date) IN (6, 7, 8) THEN 'Summer'
                ELSE 'Fall'
            END AS season
        FROM
            sales
    )
    SELECT DISTINCT ON (season)
        season,
        category,
        SUM(quantity) AS total_quantity,
        SUM(quantity * price) AS total_revenue
    FROM
        season_sales
            JOIN products USING(product_id)
    GROUP BY
        1, 2
    ORDER BY
        1, 3 DESC, 4 DESC;
    """
    return


@app.cell
def _():
    import pandas as pd

    def seasonal_sales_analysis(products: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
        products_sales = pd.merge(sales, products, on="product_id", how="left")
        products_sales["sale_month"] = products_sales["sale_date"].dt.month.astype(int)
        products_sales["season"] = products_sales["sale_month"].map(
            {
                1: "Winter",
                2: "Winter",
                3: "Spring",
                4: "Spring",
                5: "Spring",
                6: "Summer",
                7: "Summer",
                8: "Summer",
                9: "Fall",
                10: "Fall",
                11: "Fall",
                12: "Winter",
            }
        )
        products_sales["revenue"] = products_sales["quantity"] * products_sales["price"]
        summary = products_sales.groupby(["season", "category"]).agg(
            total_quantity=("quantity", lambda x: sum(x)),
            total_revenue=("revenue", lambda x: sum(x)),
        )
        return (
            summary.reset_index()
            .sort_values(
                by=["season", "total_quantity", "total_revenue"],
                ascending=[True, False, False],
            )
            .drop_duplicates(subset=["season"], keep="first")
        )

    return


if __name__ == "__main__":
    app.run()
