import marimo

__generated_with = "0.14.8"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    nav_menu = mo.nav_menu(
        {
            "/index.html": f"{mo.icon('lucide:home')} Home",
            "apps/SQL_20250627.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "apps/SQL_20250630.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Problem 3: Average Rental Duration by Category

    Goal: For each film category (e.g., Comedy, Action), compute the average rental duration (in days) across all rentals of films in that category.

    Requirements:

    - Output: category_name, average_rental_duration
    - Round to 2 decimal places
    - Exclude rentals with missing return dates
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ```{PostgreSQL}
    SELECT 
        name AS category_name,
        ROUND(AVG(return_date::date - rental_date::date), 2) AS average_rental_duration
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
        name
    ORDER BY 
        average_rental_duration DESC;
    ```
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Problem 4: Longest Consecutive Rental Streak by Customer

    Goal: Find the customer(s) with the longest streak of consecutive days they rented at least one film (1+ rentals per day without gaps).

    Requirements:

    - Output: customer_id, first_name, last_name, streak_length
    - Use only calendar days (no need to consider time of day)
    - Ignore same-day multiple rentals
    - If multiple customers tie, include them all
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ```{PostgreSQL}
    WITH daily_rentals AS (
        SELECT DISTINCT
            customer_id,
            first_name,
            last_name,
            rental_date::date AS rental_day
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
            rental_day - (RANK() OVER (PARTITION BY customer_id ORDER BY rental_day)::int) AS grp 
            -- must cast to int when operating with date; rank itself is bigint type
        FROM daily_rentals
    ),
    streaks AS (
        SELECT 
            customer_id,
            first_name,
            last_name,
            COUNT(*) AS streak_length
        FROM grouped_streaks
        GROUP BY customer_id, first_name, last_name, grp
    ),
    ranked_streaks AS (
        SELECT *, MAX(streak_length) OVER () AS max_streak FROM streaks
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
        customer_id;
    ```
    """
    )
    return


if __name__ == "__main__":
    app.run()
