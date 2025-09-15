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
            "/notebooks/SQL_20250722.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250724.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Problem 34: High-Frequency Travelers with Interleaved Itineraries

    Goal:

    Identify passengers who have **at least two interleaved travel sessions** over the past year. A **travel session** is defined as a sequence of flights under the same booking_id (i.e., an itinerary), ordered by leg_num, where:

    - the first leg's scheduled_departure is the start of the session
    - the last leg's scheduled_arrival is the end of the session

    Requirements:

    - Only include flights scheduled within the last 1 year of data (relative to the max date)
    - Two sessions are considered **interleaved** if:
        - their time windows overlap (i.e., one session starts before the other ends)
        - and the bookings are **different** and not trivially nested (i.e., overlap is non-trivial)
    - Return passengers who had **at least 2 such interleaved sessions**
      and list how many such interleaved pairs exist for them.

    Output:

    - passenger_id
    - full_name
    - num_interleaved_sessions
    """
    )
    return


@app.cell
def _():
    """
    WITH travel_session_info AS (
        SELECT
            passenger_id,
            CONCAT(INITCAP(first_name), ' ', INITCAP(last_name)) AS full_name,
            booking_id,
            MIN(scheduled_departure) AS trip_start,
            MAX(scheduled_arrival) AS trip_end
        FROM
            booking
                JOIN booking_leg USING(booking_id)
                JOIN flight USING(flight_id)
                JOIN passenger USING(booking_id)
        WHERE
            scheduled_departure >= NOW() - INTERVAL '1 year'
        GROUP BY
            1, 2, 3
    ), interleave_travel_sessions AS (
        SELECT
            t1.passenger_id,
            t1.full_name,
            t1.booking_id
        FROM
            travel_session_info t1
                JOIN travel_session_info t2
                    ON t1.passenger_id = t2.passenger_id
                        AND t1.booking_id != t2.booking_id
                        AND t2.trip_start BETWEEN t1.trip_start AND t1.trip_end
                        AND (t2.trip_start, t2.trip_end) != (t1.trip_start, t1.trip_end)
    )
    SELECT
        passenger_id,
        full_name,
        COUNT(DISTINCT booking_id) AS num_interleaved_sessions
    FROM
        interleave_travel_sessions
    GROUP BY
        1, 2
    HAVING
        COUNT(*) >= 2
    ORDER BY
        3 DESC,
        1;
    """
    return


if __name__ == "__main__":
    app.run()
