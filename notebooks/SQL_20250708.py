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
            "/notebooks/SQL_20250707.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250709.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Problem 19: Most Booked Multi-Leg Itineraries

    Goal: Find the top 10 flight itineraries (ordered sequences of flights) with the highest number of bookings.

    Requirements:

    - Use the `postgres_air` database.
    - Define an itinerary as a set of one or more `flight_id`s booked together (via booking_legs).
    - Two itineraries are considered the same if they have the same `flight_id`s in the same `leg_num` order.
    - For each distinct itinerary (ordered list of flight_ids), count how many bookings used it.
    - Output: itinerary_signature, booking_count
    - `itinerary_signature` can be a string like `'101 → 305 → 187'` (ordered flight_ids).
    - Order by booking_count DESC
    - Limit 10 rows
    """
    )
    return


@app.cell
def _():
    """
    WITH itinerary_agg AS (
        SELECT
            booking_id,
            STRING_AGG(CAST(flight_id AS VARCHAR), ' -> ' ORDER BY leg_num) AS itinerary_signature
        FROM
            booking_leg
        GROUP BY
            1
    )
    SELECT
        itinerary_signature,
        COUNT(booking_id) AS booking_count
    FROM
        itinerary_agg
    GROUP BY
        1
    ORDER BY
        2 DESC
    LIMIT
        10;
    """
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Problem 20: Trials with Rare Drug Use

    Goal: Identify drugs (interventions) that appear in trials with very low enrollment.

    Requirements:

    - Use the AACT database.
    - For each intervention where `intervention_type = 'Drug'`, find all trials it appears in.
    - Only include trials where:
        - `enrollment_type = 'Actual'`
        - `enrollment < 10`
    - Count how many such low-enrollment trials each drug appears in.
    - Output: intervention_name, low_enrollment_trial_count
    - Only include drugs with at least 3 such trials
    - Order by count DESC, then intervention_name
    """
    )
    return


@app.cell
def _():
    """
    WITH low_enroll_drug_trial AS (
        SELECT
            nct_id,
            TRIM(INITCAP(interventions.name)) AS intervention_name
        FROM
            interventions
                JOIN studies USING(nct_id)
        WHERE
            LOWER(intervention_type) = 'drug'
            AND
            LOWER(enrollment_type) = 'actual'
            AND
            enrollment < 10
    )
    SELECT
        intervention_name,
        COUNT(nct_id) AS low_enrollment_trial_count
    FROM
        low_enroll_drug_trial
    GROUP BY
        1
    HAVING
        COUNT(nct_id) >= 3
    ORDER BY
        2 DESC,
        1;
    """
    return


if __name__ == "__main__":
    app.run()
