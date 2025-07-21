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
            "/notebooks/SQL_20250718.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250720.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Problem 30: Category Switcher After High Activity

    Goal: Identify customers who rented 10+ films from a single category in a single calendar month, but then *completely stopped* renting that category in the following month.

    Requirements:

    - Use the dvdrental database.
    - Identify customer_id, full name, the category name, the high-activity month (e.g., 2005-06),
      and the number of rentals in that peak month.
    - Exclude customers who returned to the same category later.

    Hints:

    - Use DATE_TRUNC('month', rental_date) for monthly grouping.
    - Only consider categories with 10+ rentals in the peak month.
    - "Completely stopped" = 0 rentals in that category the next month.
    - Assume the data spans multiple months — edge cases at the end of dataset are okay to ignore.
    """
    )
    return


@app.cell
def _():
    """
    WITH monthly_category AS (
        SELECT
            customer_id,
            CONCAT(first_name, ' ', last_name) AS customer_name,
            name AS category_name,
            EXTRACT(YEAR FROM rental_date) * 12 + EXTRACT(MONTH FROM rental_date) AS numbered_month,
            count(*) AS rental_count
        FROM
            customer
                JOIN rental USING(customer_id)
                JOIN inventory USING(inventory_id)
                JOIN film USING(film_id)
                JOIN film_category USING(film_id)
                JOIN category USING(category_id)
        GROUP BY
            1, 3, 4
    ), all_customer_category_month AS (
        SELECT
            *
        FROM
            (SELECT customer_id, CONCAT(first_name, ' ', last_name) AS customer_name FROM customer),
            (SELECT name AS category_name FROM category),
            (SELECT DISTINCT EXTRACT(YEAR FROM rental_date) * 12 + EXTRACT(MONTH FROM rental_date) AS numbered_month FROM rental)
    ), monthly_and_next_category AS (
        SELECT
            a.customer_id,
            a.customer_name,
            a.category_name,
            a.numbered_month,
            m.rental_count,
            LEAD(m.rental_count) OVER (PARTITION BY a.customer_id, a.category_name ORDER BY a.numbered_month) AS next_month_rental
        FROM
            all_customer_category_month a
                LEFT JOIN monthly_category m
                    ON a.customer_id = m.customer_id
                        AND a.category_name = m.category_name
                        AND a.numbered_month = m.numbered_month
    )
    SELECT
        customer_id,
        customer_name,
        category_name,
        CONCAT(LPAD(CAST(FLOOR(numbered_month/12) AS VARCHAR),4,'0'),'-',LPAD(CAST(numbered_month%12 AS VARCHAR), 2, '0')) AS high_activity_month
    FROM
        monthly_and_next_category
    WHERE
        rental_count >= 10
        AND
        next_month_rental IS NULL
    ORDER BY
        1, 4, 3;
    """
    return


if __name__ == "__main__":
    app.run()
