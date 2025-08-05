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
            "/notebooks/SQL_20250804.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250806.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 3626

    Table: stores

    | Column Name | Type    |
    |-------------|---------|
    | store_id    | int     |
    | store_name  | varchar |
    | location    | varchar |

    store_id is the unique identifier for this table.  
    Each row contains information about a store and its location.  

    Table: inventory

    | Column Name | Type    |
    |-------------|---------|
    | inventory_id| int     |
    | store_id    | int     |
    | product_name| varchar |
    | quantity    | int     |
    | price       | decimal |

    inventory_id is the unique identifier for this table.  
    Each row represents the inventory of a specific product at a specific store.  

    Write a solution to find stores that have inventory imbalance - stores where the most expensive product has lower stock than the cheapest product.

    - For each store, identify the most expensive product (highest price) and its quantity
    - For each store, identify the cheapest product (lowest price) and its quantity
    - A store has inventory imbalance if the most expensive product's quantity is less than the cheapest product's quantity
    - Calculate the imbalance ratio as (cheapest_quantity / most_expensive_quantity)
    - Round the imbalance ratio to 2 decimal places
    - Only include stores that have at least 3 different products
    - Return the result table ordered by imbalance ratio in descending order, then by store name in ascending order.
    """
    )
    return


@app.cell
def _():
    """
    WITH product_counts AS (
        SELECT
            store_id
        FROM
            inventory
        GROUP BY
            1
        HAVING
            COUNT(*) >= 3
    ),
    max_price_product AS (
        SELECT DISTINCT ON (store_id)
            store_id,
            product_name AS most_exp_product,
            quantity AS most_exp_quantity,
            price AS most_exp_price
        FROM
            inventory
        WHERE
            store_id IN (SELECT store_id FROM product_counts)
        ORDER BY
            store_id,
            price DESC
    ),
    min_price_product AS (
        SELECT DISTINCT ON (store_id)
            store_id,
            product_name AS cheapest_product,
            quantity AS cheapest_quantity,
            price AS cheapest_price
        FROM
            inventory
        WHERE
            store_id IN (SELECT store_id FROM product_counts)
        ORDER BY
            store_id,
            price ASC
    )
    SELECT
        store_id,
        store_name,
        location,
        most_exp_product,
        cheapest_product,
        ROUND(CAST(cheapest_quantity AS DECIMAL) / CAST(most_exp_quantity AS DECIMAL), 2) AS imbalance_ratio
    FROM max_price_product
        JOIN min_price_product USING(store_id)
        JOIN stores USING(store_id)
    WHERE
        most_exp_quantity < cheapest_quantity
    ORDER BY
        6 DESC,
        2;
    """
    return


if __name__ == "__main__":
    app.run()
