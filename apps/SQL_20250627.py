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
            "/apps/SQL_20250629.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Problem 1: Top 3 Most Rented Movies by Revenue

    Goal: Use the DVDRental databse. Find the top 3 movies that generated the most revenue (i.e., sum of payment amounts for each film title).

    Requirements:

    - Output should include title, total_revenue, sorted descending
    - Handle ties deterministically by title
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ```{PostgreSQL}
    WITH film_revenue AS (
        SELECT 
            amount,
            title 
        FROM 
            payment  
                LEFT JOIN rental USING(rental_id)
                LEFT JOIN inventory USING(inventory_id)
                LEFT JOIN film USING(film_id)
    )
    SELECT 
        title, 
        SUM(amount) AS total_revenue 
    FROM 
        film_revenue 
    GROUP BY
        title 
    ORDER BY 
        2 DESC, 1
    LIMIT
        3;
    ```
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Problem 2: Customers With Continuous Rentals

    Goal: Use the DVDRental databse. Find customers who rented at least one film in 3 consecutive months.

    Requirements:

    - Output should include customer_id, first_name, last_name
    - Only consider distinct month/year combinations per customer
    - Don’t hardcode dates — calculate based on rental history
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ```{PostgreSQL}
    WITH rent_consecutive_month AS (
        SELECT 
            customer_id,
            first_name,
            last_name,
            mth,
            mth - LAG(mth, 1) OVER (PARTITION BY customer_id, first_name, last_name ORDER BY mth) AS mth_lag1,
            mth - LAG(mth, 2) OVER (PARTITION BY customer_id, first_name, last_name ORDER BY mth) AS mth_lag2
        FROM (
            SELECT DISTINCT 
                EXTRACT(YEAR FROM rental_date) * 12 + EXTRACT(MONTH FROM rental_date) AS mth,
                customer_id, 
                first_name, 
                last_name 
            FROM 
                rental 
                    LEFT JOIN customer USING(customer_id)
        ) sub
    )
    SELECT DISTINCT
        customer_id,
        first_name,
        last_name
    FROM
        rent_consecutive_month
    WHERE
        mth_lag1 = 1
        AND
        mth_lag2 = 2
    ORDER BY 
        1, 2, 3;
    ```
    """
    )
    return


if __name__ == "__main__":
    app.run()
