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
            "/notebooks/SQL_20250702.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250704.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Problem 11: Genre-Diverse Repeat Renters

    Goal: Identify customers who have rented more than 5 films in at least 3 different genres.

    Requirements:
    - Use the DVDRental database.
    - For each customer, compute:
        - genre_count: number of distinct genres they have rented from
        - total_rentals: total number of films rented
    - Only include customers where:
        - genre_count >= 3
        - total_rentals > 5
    - Output: customer_id, first_name, last_name, genre_count, total_rentals
    - Order by total_rentals DESC, then genre_count DESC
    """
    )
    return


@app.cell
def _():
    """
    WITH rental_by_genre AS (
        SELECT
            customer_id,
            first_name,
            last_name,
            name AS genre,
            rental_id
        FROM
            customer
                JOIN rental USING(customer_id)
                JOIN inventory USING(inventory_id)
                JOIN film USING(film_id)
                JOIN film_category USING(film_id)
                JOIN category USING(category_id)
    ),
    summary AS (
        SELECT
            customer_id,
            first_name,
            last_name,
            COUNT(DISTINCT genre) AS genre_count,
            COUNT(rental_id) AS total_rentals
        FROM
            rental_by_genre
        GROUP BY
            1, 2, 3
    )
    SELECT
        customer_id,
        first_name,
        last_name,
        genre_count,
        total_rentals
    FROM
        summary
    WHERE
        genre_count >= 3
        AND
        total_rentals > 5
    ORDER BY
        5 DESC,
        4 DESC;
    """
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Problem 12: Top Sponsors by Enrollment Accuracy in Phase 3

    Goal: Find the top 10 lead sponsors of Phase 3 interventional trials with the highest actual enrollment reporting ratio.

    Requirements:

    - Use the AACT database.
    - Filter trials where:
        - study_type = 'Interventional'
        - phase = 'Phase 3'
        - lead_or_collaborator = 'lead'
    - For each sponsor, compute:
        - total_trials: number of such trials
        - actual_count: number of trials where enrollment_type = 'Actual'
        - accuracy_ratio = actual_count / total_trials (rounded to 3 decimals)
    - Output: sponsor_name, total_trials, actual_count, accuracy_ratio
    - Order by accuracy_ratio DESC, then total_trials DESC
    - Return top 10 sponsors only
    """
    )
    return


@app.cell
def _():
    """
    WITH interventional_phase3_lead_trial AS (
        SELECT
            TRIM(name) AS sponsor_name,
            study_type,
            phase,
            lead_or_collaborator,
            enrollment_type
        FROM
            studies
                JOIN sponsors USING(nct_id)
        WHERE
            LOWER(study_type) = 'interventional'
            AND
            LOWER(phase) LIKE '%phase3%'
            AND
            LOWER(lead_or_collaborator) = 'lead'
    )
    SELECT
        sponsor_name,
        COUNT(*) AS total_trials,
        SUM(CASE WHEN LOWER(enrollment_type) = 'actual' THEN 1 ELSE 0 END) AS actual_count,
        ROUND(AVG(CASE WHEN LOWER(enrollment_type) = 'actual' THEN 1 ELSE 0 END), 3) AS accuracy_ratio
    FROM
        interventional_phase3_lead_trial
    GROUP BY
        1
    ORDER BY
        4 DESC,
        2 DESC
    LIMIT
        10;
    """
    return


if __name__ == "__main__":
    app.run()
