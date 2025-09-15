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
            "/notebooks/SQL_20250829.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250903.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 2112

    Table: Flights

    | Column Name       | Type |
    |-------------------|------|
    | departure_airport | int  |
    | arrival_airport   | int  |
    | flights_count     | int  |

    (departure_airport, arrival_airport) is the primary key column (combination of columns with unique values) for this table. Each row of this table indicates that there were flights_count flights that departed from departure_airport and arrived at arrival_airport.
 
    Write a solution to report the ID of the airport with the most traffic. The airport with the most traffic is the airport that has the largest total number of flights that either departed from or arrived at the airport. If there is more than one airport with the most traffic, report them all.

    Return the result table in any order.
    """
    )
    return


@app.cell
def _():
    """
    WITH flight_airport AS (
        SELECT
            departure_airport AS airport_id,
            flights_count
        FROM
            Flights
        UNION ALL
        SELECT
            arrival_airport AS airport_id,
            flights_count
        FROM
            Flights
    ),
    flight_airport_grouped AS (
        SELECT
            airport_id,
            SUM(flights_count) AS sum_flights_count
        FROM
            flight_airport
        GROUP BY
            1
    ),
    flight_airport_grouped_with_rank AS (
        SELECT
            *,
            RANK() OVER (ORDER BY sum_flights_count DESC) AS rank
        FROM
            flight_airport_grouped
    )
    SELECT
        airport_id
    FROM
        flight_airport_grouped_with_rank
    WHERE
        rank = 1
    ORDER BY
        1;
    """
    return


@app.cell
def _():
    import pandas as pd

    def airport_with_most_traffic(flights: pd.DataFrame) -> pd.DataFrame:
        flights_airport = pd.concat(
            [
                flights[["departure_airport", "flights_count"]].rename(columns={"departure_airport": "airport_id"}),
                flights[["arrival_airport", "flights_count"]].rename(columns={"arrival_airport": "airport_id"}),
            ]
        )
        flights_airport = flights_airport.groupby("airport_id")["flights_count"].sum().reset_index()
        flights_airport["rank"] = flights_airport["flights_count"].rank(method="min", ascending=False)
        return flights_airport[flights_airport["rank"] == 1][["airport_id"]]

    return


if __name__ == "__main__":
    app.run()
