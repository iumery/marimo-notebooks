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
            "/notebooks/SQL_20250717.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_202507019.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Problem 29: Long-Term Returners by Genre

    Goal: Find customers who rented a film from a genre, returned it within 2 days, and then rented **another film from the same genre** at least 30 days later.

    Requirements:

    - Use the `rental`, `inventory`, `film`, `film_category`, `category`, and `customer` tables.
    - The return should be within 2 days of rental.
    - The second rental (from the same genre) must be at least 30 days after the first.
    - For each qualifying customer and genre, return:
        - customer_id, full name
        - category name
        - rental date of the first film
        - rental date of the second film
        - days between the rentals

    Output:

    - One row per customer-genre where this long-term return pattern happened.
    - Order by days between rentals descending, then customer_id, then category name.
    """
    )
    return


@app.cell
def _():
    """
    WITH rental_return_date_info AS (
        SELECT
            customer_id,
            first_name,
            last_name,
            name AS category_name,
            rental_date,
            return_date,
            return_date - rental_date AS rental_duration
        FROM
            customer
                JOIN rental USING(customer_id)
                JOIN inventory USING(inventory_id)
                JOIN film USING(film_id)
                JOIN film_category USING(film_id)
                JOIN category USING(category_id)
    ), return_then_rent AS (
        SELECT
            *,
            LEAD(rental_date, 1) OVER (PARTITION BY customer_id, category_name ORDER BY rental_date) AS next_rental_in_this_genre,
            CAST(LEAD(rental_date, 1) OVER (PARTITION BY customer_id, category_name ORDER BY rental_date) AS date) - CAST(rental_date AS date) AS days_between_the_rentals
        FROM
            rental_return_date_info
    )
    SELECT
        customer_id,
        CONCAT(first_name, ' ', last_name) AS full_name,
        category_name,
        rental_date AS rental_date_of_first_film,
        next_rental_in_this_genre AS rental_date_of_second_film,
        days_between_the_rentals
    FROM
        return_then_rent
    WHERE
        rental_duration <= INTERVAL '2 days'
        AND
        days_between_the_rentals >= 30
    ORDER BY
        6 DESC,
        1, 3;
    """
    return


if __name__ == "__main__":
    app.run()
