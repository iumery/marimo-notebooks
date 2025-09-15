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
            "/notebooks/SQL_20250715.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250717.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Problem 27: Genre Loyalty Shift

    Goal: Identify customers who switched their preferred genre between their first and last 5 rentals.

    Requirements:

    - A customer's "preferred genre" is the most frequent genre (category.name) among a set of rentals.
    - Consider only customers with at least 10 total rentals.
    - Define the "first 5" and "last 5" rentals by rental_date.
    - For each qualified customer whose preferred genre changed, return:
        - customer_id
        - first_name
        - last_name
        - first_preferred_genre
        - last_preferred_genre

    Notes:

    - If there is a tie for most frequent genre in either set, return any one of the tied genres.
    - A "change" means the two preferred genres are different strings.
    """
    )
    return


@app.cell
def _():
    """
    WITH rental_rank_with_category AS (
        SELECT
            customer_id,
            first_name,
            last_name,
            name,
            rental_date,
            ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY rental_date) AS asc_rental_rank,
            ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY rental_date DESC) AS desc_rental_rank
        FROM
            customer
                JOIN rental USING(customer_id)
                JOIN inventory USING(inventory_id)
                JOIN film USING(film_id)
                JOIN film_category USING(film_id)
                JOIN category USING(category_id)
        WHERE
            customer_id IN (SELECT customer_id FROM rental GROUP BY customer_id HAVING count(*) >= 10)
    ), rental_rank_with_category_with_rank AS (
        SELECT
            customer_id,
            first_name,
            last_name,
            name,
            SUM(CASE WHEN asc_rental_rank <=5 THEN 1 ELSE 0 END) AS first_five_cate_count,
            SUM(CASE WHEN desc_rental_rank <=5 THEN 1 ELSE 0 END) AS last_five_cate_count
        FROM
            rental_rank_with_category
        GROUP BY
            1, 2, 3,4
    ), customer_with_preferred_genre AS (
        SELECT DISTINCT
            customer_id,
            first_name,
            last_name,
            FIRST_VALUE(name) OVER (PARTITION BY customer_id ORDER BY first_five_cate_count DESC, name) AS first_preferred_genre,
            FIRST_VALUE(name) OVER (PARTITION BY customer_id ORDER BY last_five_cate_count DESC, name) AS last_preferred_genre
        FROM
            rental_rank_with_category_with_rank
    )
    SELECT
        *
    FROM
        customer_with_preferred_genre
    WHERE
        first_preferred_genre != last_preferred_genre
    ORDER BY
        1;
    """
    return


if __name__ == "__main__":
    app.run()
