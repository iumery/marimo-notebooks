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
            "/notebooks/SQL_20250720.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250722.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Problem 32: Longest Consecutive Rental Streak

    Goal: For each customer, find their longest consecutive-day streak of rentals (one rental per day per streak).

    Requirements:

    - Use the `dvdrental` database.
    - Ignore customers with fewer than 10 total rentals.
    - A "consecutive-day streak" means rentals that occurred on sequential calendar days (e.g., July 1, 2, 3).
    - Count each streak's length (number of days).
    - For each customer, report the maximum such streak.
    - Output: customer_id, full_name, longest_streak
    """
    )
    return


@app.cell
def _():
    """
    WITH rental_dates AS (
        SELECT DISTINCT
            customer_id,
            CONCAT(first_name, ' ', last_name) AS full_name,
            CAST(rental_date AS DATE) AS rental_date
        FROM
            customer
                JOIN rental USING(customer_id)
    ), groups_of_consecutive_rentals AS (
        SELECT
            customer_id,
            full_name,
            rental_date,
            rental_date - FIRST_VALUE(rental_date) OVER (PARTITION BY customer_id ORDER BY rental_date) AS day_since_first_rental,
            ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY rental_date) AS rental_date_order,
            rental_date - FIRST_VALUE(rental_date) OVER (PARTITION BY customer_id ORDER BY rental_date) - ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY rental_date) AS consecutive_grouping
        FROM
            rental_dates
    ), consecutive_streaks AS (
        SELECT
            customer_id,
            full_name,
            consecutive_grouping,
            COUNT(*) AS streak
        FROM
            groups_of_consecutive_rentals
        GROUP BY
            1, 2, 3
    )
    SELECT
        customer_id,
        full_name,
        MAX(streak) AS longest_streak
    FROM
        consecutive_streaks
    WHERE
        customer_id IN (SELECT customer_id FROM rental GROUP BY 1 HAVING COUNT(*) >= 10)
    GROUP BY
        1, 2
    ORDER BY
        3 DESC;
    """
    return


if __name__ == "__main__":
    app.run()
