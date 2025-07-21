import marimo

__generated_with = "0.14.10"
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
            "/notebooks/SQL_20250716.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250718.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Problem 28: Genre Stickiness After First Try

    Goal: Find customers who tried a film genre *once* early in their rental history, then stuck to it for *at least 40%* of their next 10 rentals.

    Requirements:

    - Only consider customers with at least 15 total rentals.
    - Identify the first genre that appears *only once* in the customer's first 5 rentals.
    - Check if the next 10 rentals (i.e. rentals 6 through 15) include that genre in 4 or more rentals.
    - Return: customer_id, first_name, last_name, the genre name, and how many times it appeared in the next 10.
    """
    )
    return


@app.cell
def _():
    """
    WITH customer_with_15_more_rents AS (
        SELECT
            customer_id
        FROM
            customer
                JOIN rental USING(customer_id)
        GROUP BY
            1
        HAVING
            COUNT(*) >= 15
    ), rental_info_with_rank AS (
        SELECT
            customer_id,
            first_name,
            last_name,
            name AS category_name,
            ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY rental_date) as rank_by_date
        FROM
            customer
                JOIN rental USING(customer_id)
                JOIN inventory USING(inventory_id)
                JOIN film USING(film_id)
                JOIN film_category USING(film_id)
                JOIN category USING(category_id)
        WHERE
            customer_id in (SELECT customer_id FROM customer_with_15_more_rents)
    ), first_5_single_rent AS (
        SELECT
            customer_id,
            first_name,
            last_name,
            category_name
        FROM
            rental_info_with_rank
        WHERE
            rank_by_date BETWEEN 1 AND 5
        GROUP BY
            1, 2, 3, 4
        HAVING
            COUNT(*) = 1
    ), next_15_rent AS (
        SELECT
            customer_id,
            first_name,
            last_name,
            category_name
        FROM
            rental_info_with_rank
        WHERE
            rank_by_date BETWEEN 6 AND 15
    )
    SELECT
        f5.customer_id,
        f5.first_name,
        f5.last_name,
        f5.category_name,
        COUNT(*) AS liked_category_rental_counts
    FROM
        first_5_single_rent f5
            JOIN next_15_rent n15 ON f5.customer_id = n15.customer_id
                AND f5.category_name = n15.category_name
    GROUP BY
        1, 2, 3, 4
    HAVING
        COUNT(*) >= 4;
    """
    return


if __name__ == "__main__":
    app.run()
