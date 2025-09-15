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
            "/notebooks/SQL_20250629.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250701.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Problem 5: Customer Activity Classification

    Goal: Use the DVDRental databse. Classify each customer based on how many rentals they've made.

    Requirements:

    - Output: customer_id, first_name, last_name, activity_level
    - Classification rules:
        - 'High' if rentals >= 40
        - 'Medium' if rentals between 20 and 39 (inclusive)
        - 'Low' if rentals < 20
    - Use a CASE statement to assign activity_level
    - Order by activity_level descending (High > Medium > Low), then customer_id
    """
    )
    return


@app.cell
def _():
    """
    SELECT
        customer_id,
        first_name,
        last_name,
        CASE
            WHEN COUNT(rental_id) >= 40 THEN 'High'
            WHEN COUNT(rental_id) >= 20 THEN 'Medium'
            ELSE 'Low'
        END AS activity_level
    FROM
        customer
            JOIN rental USING(customer_id)
    GROUP BY
        1, 2, 3
    ORDER BY
        CASE
            WHEN COUNT(rental_id) >= 40 THEN 1
            WHEN COUNT(rental_id) >= 20 THEN 2
            ELSE 3
        END,
        1;
    """
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Problem 6: Film Rental Availability Label

    Goal: Use the DVDRental databse. Label each film as 'Available', 'Rented', or 'Not in Inventory'.

    Requirements:

    - Output: film_id, title, availability_status
    - Use the following logic:
        - 'Available' if there is at least one inventory item for the film that is not currently rented out
        - 'Rented' if all inventory items are currently rented out
        - 'Not in Inventory' if the film has no inventory entries at all
    - Use a CASE statement to generate the availability_status
    - Tip: The `rental.return_date` is NULL if the item hasn't been returned yet
    """
    )
    return


@app.cell
def _():
    """
    WITH unique_inventory AS (
    SELECT
        film_id,
        title,
        inventory_id,
        MAX(rental_date) AS rental_date,
        MAX(return_date) AS return_date
    FROM
        film
            LEFT JOIN inventory USING(film_id)
            LEFT JOIN rental USING(inventory_id)
    GROUP BY
        1, 2, 3
    ),
    inventory_count AS (
        SELECT
            film_id,
            title,
            COUNT(inventory_id) AS num_inventory,
            COUNT(rental_date) AS num_rented,
            COUNT(return_date) AS num_returned
        FROM
            unique_inventory
        GROUP BY
            1, 2
    )
    SELECT
        film_id,
        title,
        CASE
            WHEN num_inventory = 0 THEN 'Not in Inventory'
            WHEN num_returned = num_inventory THEN 'Available'
            ELSE 'Rented'
        END AS availability_status
    FROM
        inventory_count
    ORDER BY
        1;
    """
    return


@app.cell
def _():
    """
    SELECT
        film_id,
        title,
        CASE
            WHEN COUNT(inventory_id) = 0 THEN 'Not in Inventory'
            WHEN COUNT(CASE WHEN return_date IS NULL THEN 1 END) > 0 THEN 'Available'
            ELSE 'Rented'
        END AS availability_status
    FROM
        film
            LEFT JOIN inventory USING(film_id)
            LEFT JOIN rental USING(inventory_id)
    GROUP BY
        1, 2
    ORDER BY
        1;
    """
    return


if __name__ == "__main__":
    app.run()
