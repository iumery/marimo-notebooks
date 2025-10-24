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
            "/notebooks/SQL_20251027.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251029.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 3052

    Table: Inventory

    | Column Name    | Type    | 
    |----------------|---------| 
    | item_id        | int     | 
    | item_type      | varchar |
    | item_category  | varchar |
    | square_footage | decimal |

    item_id is the column of unique values for this table. Each row includes item id, item type, item category and sqaure footage. Leetcode warehouse wants to maximize the number of items it can stock in a 500,000 square feet warehouse. It wants to stock as many prime items as possible, and afterwards use the remaining square footage to stock the most number of non-prime items.

    Write a solution to find the number of prime and non-prime items that can be stored in the 500,000 square feet warehouse. Output the item type with prime_eligible followed by not_prime and the maximum number of items that can be stocked.

    Note:

    - Item count must be a whole number (integer).
    - If the count for the not_prime category is 0, you should output 0 for that particular category.

    Return the result table ordered by item count in descending order.
    """
    )
    return


@app.cell
def _():
    """
    WITH grouped_info AS (
        SELECT
            item_type,
            COUNT(*) AS item_multiplier,
            SUM(square_footage) AS taken
        FROM
            Inventory
        GROUP BY
            1
    )
    SELECT
        item_type,
        FLOOR(COALESCE((LEAD(500000 % taken) OVER (ORDER BY item_type)), 500000) / taken) * item_multiplier AS item_count
    FROM
        grouped_info
    ORDER BY
        2 DESC;
    """
    return


@app.cell
def _():
    import pandas as pd

    def maximize_items(inventory: pd.DataFrame) -> pd.DataFrame:
        df = inventory.groupby("item_type").agg(
            total_footage=("square_footage", "sum"),
            num_of_items=("item_id", "size"),
        )

        available_footage = 500000

        prime = df.loc["prime_eligible"]
        prime_combos = available_footage // prime["total_footage"]
        prime_total_items = prime["num_of_items"] * prime_combos
        prime_used_footage = prime["total_footage"] * prime_combos
        footage_left = 500000 - prime_used_footage

        non_prime = df.loc["not_prime"]
        non_prime_combos = footage_left // non_prime["total_footage"]
        non_prime_total_items = non_prime["num_of_items"] * non_prime_combos

        df = pd.DataFrame(
            [
                {"item_type": "prime_eligible", "item_count": prime_total_items},
                {"item_type": "not_prime", "item_count": non_prime_total_items},
            ]
        ).sort_values("item_count", ascending=False)

        return df

    return


if __name__ == "__main__":
    app.run()
