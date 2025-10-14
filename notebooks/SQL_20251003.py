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
            "/notebooks/SQL_20251002.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251006.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 2922

    Table: Users

    | Column Name    | Type    |
    |----------------|---------|
    | seller_id      | int     |
    | join_date      | date    |
    | favorite_brand | varchar |

    seller_id is column of unique values for this table. This table contains seller id, join date, and favorite brand of sellers.

    Table: Items

    | Column Name   | Type    |
    |---------------|---------|
    | item_id       | int     |
    | item_brand    | varchar |

    item_id is the column of unique values for this table. This table contains item id and item brand.

    Table: Orders

    | Column Name   | Type    |
    |---------------|---------|
    | order_id      | int     |
    | order_date    | date    |
    | item_id       | int     |
    | seller_id     | int     |

    order_id is the column of unique values for this table. item_id is a foreign key to the Items table. seller_id is a foreign key to the Users table. This table contains order id, order date, item id and seller id.

    Write a solution to find the top seller who has sold the highest number of unique items with a different brand than their favorite brand. If there are multiple sellers with the same highest count, return all of them.

    Return the result table ordered by seller_id in ascending order.
    """
    )
    return


@app.cell
def _():
    """
    WITH sell_unique AS (
        SELECT
            seller_id,
            COUNT(DISTINCT item_id) AS num_items
        FROM
            Orders
                LEFT JOIN Users USING (seller_id)
                LEFT JOIN Items USING (item_id)
        WHERE
            favorite_brand <> item_brand
        GROUP BY
            1
    )
    SELECT
        *
    FROM
        sell_unique
    WHERE
        num_items = (SELECT MAX(num_items) FROM sell_unique)
    ORDER BY
        seller_id;
    """
    return


if __name__ == "__main__":
    app.run()
