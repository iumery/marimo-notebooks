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
            "/notebooks/SQL_20250719.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250721.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Problem 31: Binge Watching Detection

    Goal: Identify customers who tend to rent multiple films in short bursts (i.e., "binge rent").

    Requirements:

    - Consider each customer's rental history ordered by rental_date.
    - Define a *new session* as any rental that happens more than **3 days** after the previous one.
    - A session consists of one or more consecutive rentals within 3 days of each other.
    - For each customer, count how many distinct sessions they have.
    - Return only those customers who have **more than 5 sessions**.
    - Output: customer_id, full name, total rentals, session_count.
    - Order by session_count descending, then customer_id.

    Hint: Use LAG() to compute time differences and cumulative SUM() to create session_id.
    """
    )
    return


@app.cell
def _():
    """
    WITH rental_with_gap AS (
        SELECT
            customer_id,
            CONCAT(first_name, ' ', last_name) AS customer_name,
            rental_date,
            rental_date - COALESCE(LAG(rental_date, 1) OVER (PARTITION BY customer_id ORDER BY rental_date), rental_date) AS gap_days
        FROM
            customer
                JOIN rental USING(customer_id)
    ),
    sessionized AS (
        SELECT
            *,
            SUM(CASE WHEN gap_days > INTERVAL '3 days' THEN 1 ELSE 0 END) OVER (
                PARTITION BY customer_id ORDER BY rental_date
                ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
            ) AS session_id
        FROM
            rental_with_gap
    ),
    session_count AS (
        SELECT
            customer_id,
            customer_name,
            COUNT(DISTINCT session_id) AS session_count,
            COUNT(*) AS total_rentals
        FROM
            sessionized
        GROUP BY
            1, 2
    )
    SELECT
        *
    FROM
        session_count
    WHERE
        session_count > 5
    ORDER BY
        session_count DESC, customer_id;
    """
    return


if __name__ == "__main__":
    app.run()
