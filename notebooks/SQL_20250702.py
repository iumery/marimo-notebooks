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
            "/notebooks/SQL_20250701.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250703.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Problem 9: Last Rental per Customer and Category

    Goal: For each customer and film category, show the last rental they made.

    Requirements:

    - Use the DVDRental database
    - Output: customer_id, category_name, rental_date, film_title
    - If a customer never rented a certain category, exclude it
    - If multiple films were rented on the same last date in the same category, show all of them
    """
    )
    return


@app.cell
def _():
    """
    WITH category_rank AS (
        SELECT
            customer_id,
            name AS category_name,
            CAST(rental_date AS date),
            title,
            RANK() OVER (PARTITION BY customer_id, name ORDER BY CAST(rental_date AS date) DESC) AS date_rank
        FROM
            rental
                JOIN inventory USING(inventory_id)
                JOIN film USING(film_id)
                JOIN film_category USING(film_id)
                JOIN category USING(category_id)
    )
    SELECT
        customer_id, category_name, rental_date, title
    FROM
        category_rank
    WHERE
        date_rank = 1
    ORDER BY
        1, 2;
    """
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Problem 10: Most Frequent Diagnoses per Intervention Type

    Goal: From the AACT database, for each intervention type, find the top 3 most frequently co-occurring conditions.

    Requirements:

    - Use the ctgov schema of the AACT database
    - Output: intervention_type, condition_name, count
    - Limit to top 3 conditions per intervention_type based on co-occurrence count
    - Include ties
    """
    )
    return


@app.cell
def _():
    """
    WITH co_occurrence_count AS (
        SELECT
            intervention_type,
            LOWER(downcase_name) AS condition_name,
            COUNT(*) AS co_occurrence
        FROM
            interventions
                JOIN conditions USING(nct_id)
        GROUP BY
            1, 2
    ),
    co_occurrence_rank AS (
        SELECT
            *,
            DENSE_RANK() OVER (PARTITION BY intervention_type ORDER BY co_occurrence DESC) AS co_occurrence_rank
        FROM
            co_occurrence_count
    )
    SELECT
        intervention_type,
        condition_name,
        co_occurrence
    FROM
        co_occurrence_rank
    WHERE
        co_occurrence_rank <= 3
    ORDER BY
        1, 3 DESC;
    """
    return


if __name__ == "__main__":
    app.run()
