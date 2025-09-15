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
            "/notebooks/SQL_20250713.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250715.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Problem 25: Genre Loyalty and Churn Detection

    Goal: Identify customers who were highly loyal to a single genre for a period of time, but later switched to predominantly renting from a different genre.

    Requirements:

    - Use the dvdrental database.
    - For each customer with at least 15 rentals, track their rental history **chronologically**.
    - Determine the **main genre** in the first half of their rentals (most frequent category).
    - Determine the **main genre** in the second half of their rentals.
    - If these two main genres are different, count them as "genre switchers".
    - Output: customer_id, first_half_genre, second_half_genre, total_rentals
    - Only include customers where:
        - total_rentals ≥ 15
        - main genres in first vs second half are different
    """
    )
    return


@app.cell
def _():
    """
    WITH rental_category_info AS (
        SELECT
            customer_id,
            rental_date,
            category.name AS category_name,
            total_rentals,
            SIGN(total_rentals/2 + 0.5 - ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY rental_date)) AS half_split
        FROM
            customer
                JOIN rental USING(customer_id)
                JOIN inventory USING(inventory_id)
                JOIN film USING(film_id)
                JOIN film_category USING(film_id)
                JOIN category USING(category_id)
                JOIN (SELECT customer_id, COUNT(*) AS total_rentals FROM customer JOIN rental USING(customer_id) GROUP BY 1 HAVING COUNT(*) >= 15) USING(customer_id)
    ),
    category_count_by_half AS (
        SELECT
            customer_id,
            half_split,
            category_name,
            total_rentals,
            count(*) AS category_count
        FROM
            rental_category_info
        GROUP BY
            1, 2, 3, 4
    ),
    category_rank_by_half AS (
    SELECT
        customer_id,
        half_split,
        category_name,
        total_rentals,
        ROW_NUMBER() OVER (PARTITION BY customer_id, half_split, total_rentals ORDER BY category_count DESC, category_name) AS category_rank
    FROM
        category_count_by_half
    ),
    first_half AS (
    SELECT
        customer_id,
        category_name AS first_half_genre
    FROM
        category_rank_by_half
    WHERE
        half_split = -1
        AND
        category_rank = 1
    ),
    second_half AS (
    SELECT
        customer_id,
        category_name AS second_half_genre,
        total_rentals
    FROM
        category_rank_by_half
    WHERE
        half_split = 1
        AND
        category_rank = 1
    )
    SELECT
        customer_id,
        first_half_genre,
        second_half_genre,
        total_rentals
    FROM
        first_half JOIN second_half USING(customer_id)
    WHERE
        first_half_genre != second_half_genre;
    """
    return


if __name__ == "__main__":
    app.run()
