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
            "/notebooks/SQL_20250703.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250705.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Problem 13: Actor Pairs with Strongest Genre Overlap

    Goal: Find the top 10 pairs of actors who have appeared together in the most *distinct genres*.

    Requirements:

    - Use the DVDRental database.
    - A pair is defined as two different actors who both appear in the same film.
    - For each actor pair, determine the number of distinct genres (categories) in which they've co-acted.
    - Output: actor_id_1, actor_id_2, actor_name_1, actor_name_2, shared_genres
    - Ensure each pair is listed only once (e.g., (1,2) not also (2,1))
    - Order by shared_genres DESC, then actor_id_1, then actor_id_2
    - Return only the top 10 pairs.

    Notes:

    - You may need to join actor, film_actor, film_category, and category.
    - Handle self-joins carefully to avoid duplication and self-pairing.
    """
    )
    return


@app.cell
def _():
    """
    SELECT
        fa1.actor_id AS actor_id_1,
        CONCAT(a1.first_name, ' ', a1.last_name) AS actor_name_1,
        fa2.actor_id AS actor_id_2,
        CONCAT(a2.first_name, ' ', a2.last_name) AS actor_name_2,
        COUNT(DISTINCT name) AS shared_genres
    FROM
        film_actor fa1
            JOIN film_actor fa2 USING(film_id)
            JOIN actor a1 ON fa1.actor_id = a1.actor_id
            JOIN actor a2 ON fa2.actor_id = a2.actor_id
            JOIN film_category USING(film_id)
            JOIN category USING(category_id)
    WHERE
        fa1.actor_id < fa2.actor_id
    GROUP BY
        1, 2, 3, 4
    ORDER BY
        5 DESC,
        1, 3
    LIMIT
        10;
    """
    return


if __name__ == "__main__":
    app.run()
