import marimo

__generated_with = "0.14.9"
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
            "/apps/SQL_20250627.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/apps/SQL_20250630.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Problem 3: Average Rental Duration by Category

    Goal: Use the DVDRental databse. For each film category (e.g., Comedy, Action), compute the average rental duration (in days) across all rentals of films in that category.

    Requirements:

    - Output: category_name, average_rental_duration
    - Round to 2 decimal places
    - Exclude rentals with missing return dates
    """
    )
    return


@app.cell
def _():
    """
    SELECT
        name AS category_name,
        ROUND(AVG(CAST(return_date AS date) - CAST(rental_date AS date)), 2) AS average_rental_duration
            -- cast to date then take difference
            -- take difference then extract day may behave unexpectedly, e.g. 5 days 23 hours -> 5
    FROM
        rental
        JOIN inventory USING (inventory_id)
        JOIN film_category USING (film_id)
        JOIN category USING (category_id)
    WHERE
        return_date IS NOT NULL
    GROUP BY
        1
    ORDER BY
        2 DESC;
    """
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Problem 4: Longest Consecutive Rental Streak by Customer

    Goal: Use the DVDRental databse. Find the customer(s) with the longest streak of consecutive days they rented at least one film (1+ rentals per day without gaps).

    Requirements:

    - Output: customer_id, first_name, last_name, streak_length
    - Use only calendar days (no need to consider time of day)
    - Ignore same-day multiple rentals
    - If multiple customers tie, include them all
    """
    )
    return


@app.cell
def _():
    """
    WITH daily_rentals AS (
        SELECT DISTINCT
            customer_id,
            first_name,
            last_name,
            CAST(rental_date AS date) AS rental_day
        FROM
            rental
                JOIN customer USING (customer_id)
    ),
    grouped_streaks AS (
            SELECT
                customer_id,
                first_name,
                last_name,
                rental_day,
                rental_day - CAST(RANK() OVER (PARTITION BY customer_id ORDER BY rental_day) AS int) AS grp
                    -- must cast to int when operating with date, rank itself gives bigint
            FROM
            daily_rentals
    ),
    streaks AS (
        SELECT
            customer_id,
            first_name,
            last_name,
            COUNT(*) AS streak_length
        FROM
            grouped_streaks
        GROUP BY
            1, 2, 3,
            grp
    ),
    ranked_streaks AS (
        SELECT
            *,
            MAX(streak_length) OVER () AS max_streak
        FROM
            streaks
    )
    SELECT
        customer_id,
        first_name,
        last_name,
        streak_length
    FROM
        ranked_streaks
    WHERE
        streak_length = max_streak
    ORDER BY
        1;
    """
    return


if __name__ == "__main__":
    app.run()
