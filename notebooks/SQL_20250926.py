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
            "/notebooks/SQL_20250925.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250929.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 2783

    Table: Flights

    | Column Name | Type |
    |-------------|------|
    | flight_id   | int  |
    | capacity    | int  |

    flight_id is the column with unique values for this table. Each row of this table contains flight id and its capacity.

    Table: Passengers

    | Column Name  | Type |
    |--------------|------|
    | passenger_id | int  |
    | flight_id    | int  |

    passenger_id is the column with unique values for this table. Each row of this table contains passenger id and flight id. Passengers book tickets for flights in advance. If a passenger books a ticket for a flight and there are still empty seats available on the flight, the passenger ticket will be confirmed. However, the passenger will be on a waitlist if the flight is already at full capacity.

    Write a solution to report the number of passengers who successfully booked a flight (got a seat) and the number of passengers who are on the waitlist for each flight.

    Return the result table ordered by flight_id in ascending order.
    """
    )
    return


@app.cell
def _():
    """
    WITH number_passenger AS (
        SELECT
            flight_id,
            COUNT(DISTINCT passenger_id) AS num_passenger
        FROM
            Passengers
        GROUP BY
            1
    )
    SELECT
        flight_id,
        LEAST(COALESCE(num_passenger,0), capacity) AS booked_cnt,
        GREATEST(COALESCE(num_passenger,0) - capacity, 0) AS waitlist_cnt
    FROM
        Flights
            LEFT JOIN number_passenger USING (flight_id)
    ORDER BY
        1;
    """
    return


@app.cell
def _():
    import pandas as pd


    def waitlist_analysis(
        flights: pd.DataFrame, passengers: pd.DataFrame
    ) -> pd.DataFrame:
        number_passenger = passengers.groupby("flight_id", as_index=False)[
            "passenger_id"
        ].nunique()
        df = pd.merge(
            flights, number_passenger, how="left", on="flight_id"
        ).fillna(0)
        df["booked_cnt"] = df[["capacity", "passenger_id"]].min(axis=1)
        df["waitlist_cnt"] = (df["passenger_id"] - df["capacity"]).clip(lower=0)
        df = df[["flight_id", "booked_cnt", "waitlist_cnt"]].sort_values(
            "flight_id"
        )
        return df
    return


if __name__ == "__main__":
    app.run()
