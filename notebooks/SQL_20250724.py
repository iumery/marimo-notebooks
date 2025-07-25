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
            "/notebooks/SQL_20250723.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250725.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Problem 35: Flight Layover Anomaly Detection

    Goal: Identify passengers who experienced abnormal layovers (too short or too long) during multi-leg bookings.

    Requirements:

    - A "travel session" is a sequence of flights under the same booking_id.
    - Only consider booking_ids with at least two flights (i.e. connecting flights).
    - For each pair of consecutive flights in a session (ordered by scheduled_departure), calculate the layover = next_flight.scheduled_departure - prev_flight.scheduled_arrival
    - Return cases where layover < 20 minutes OR layover > 1 day.
    - Output: passenger_id, booking_id, flight_id_prev, flight_id_next, layover_minutes
    - Order by passenger_id, booking_id, layover_minutes ascending
    """
    )
    return


@app.cell
def _():
    """
    WITH layover_info AS (
        SELECT 
            leg_num, 
            CONCAT(first_name, ' ', last_name) AS full_name, 
            passenger_id, 
            booking_id,
            is_returning,
            flight_id AS flight_id_prev,
            LEAD(scheduled_departure, 1) OVER (PARTITION BY booking_id, passenger_id, is_returning ORDER BY leg_num) - scheduled_arrival AS layover,
            LEAD(flight_id, 1) OVER (PARTITION BY booking_id, passenger_id, is_returning ORDER BY leg_num) AS flight_id_next
        FROM
            booking 
                JOIN booking_leg USING(booking_id) 
                JOIN flight USING(flight_id) 
                JOIN passenger USING(booking_id)
    )
    SELECT
        passenger_id,
        full_name,
        booking_id,
        flight_id_prev,
        flight_id_next,
        ROUND(EXTRACT(EPOCH FROM layover)/60) AS layover_minutes
    FROM
        layover_info
    WHERE
        layover <= INTERVAL '20 minutes'
        OR
        layover >= INTERVAL '1 day'
    ORDER BY
        6 DESC,
        1,2;
    """
    return


if __name__ == "__main__":
    app.run()
