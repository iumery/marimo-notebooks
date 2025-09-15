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
            "/notebooks/SQL_20250807.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250809.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 3601

    Table: drivers

    | Column Name | Type    |
    |-------------|---------|
    | driver_id   | int     |
    | driver_name | varchar |

    driver_id is the unique identifier for this table. Each row contains information about a driver.

    Table: trips


    | Column Name   | Type    |
    |---------------|---------|
    | trip_id       | int     |
    | driver_id     | int     |
    | trip_date     | date    |
    | distance_km   | decimal |
    | fuel_consumed | decimal |

    trip_id is the unique identifier for this table. Each row represents a trip made by a driver, including the distance traveled and fuel consumed for that trip.

    Write a solution to find drivers whose fuel efficiency has improved by comparing their average fuel efficiency in the first half of the year with the second half of the year.

    - Calculate fuel efficiency as distance_km / fuel_consumed for each trip
    - First half: January to June, Second half: July to December
    - Only include drivers who have trips in both halves of the year
    - Calculate the efficiency improvement as (second_half_avg - first_half_avg)
    - Round all results to 2 decimal places
    - Return the result table ordered by efficiency improvement in descending order, then by driver name in ascending order.
    """
    )
    return


@app.cell
def _():
    """
    WITH first_half AS (
        SELECT
            driver_id,
            AVG(distance_km / fuel_consumed) AS first_half_avg
        FROM
            trips
        WHERE
            EXTRACT(MONTH FROM trip_date) BETWEEN 1 AND 6
        GROUP BY
            1
    ), second_half AS (
        SELECT
            driver_id,
            AVG(distance_km / fuel_consumed) AS second_half_avg
        FROM
            trips
        WHERE
            EXTRACT(MONTH FROM trip_date) BETWEEN 7 AND 12
        GROUP BY
            1
    )
    SELECT
        driver_id,
        driver_name,
        ROUND(first_half_avg,2) AS first_half_avg,
        ROUND(second_half_avg,2) AS second_half_avg,
        ROUND(second_half_avg - first_half_avg,2) AS efficiency_improvement
    FROM
        first_half
            JOIN second_half USING(driver_id)
            JOIN drivers USING(driver_id)
    WHERE
        second_half_avg IS NOT NULL
        AND
        second_half_avg > first_half_avg
    ORDER BY
        5 DESC, 2;
    """
    return


@app.cell
def _():
    import pandas as pd

    def find_improved_efficiency_drivers(drivers: pd.DataFrame, trips: pd.DataFrame) -> pd.DataFrame:
        # Merge drivers with their trips
        df = pd.merge(drivers, trips, on="driver_id")

        # Calculate fuel efficiency for each trip
        df["efficiency"] = df["distance_km"] / df["fuel_consumed"]

        # Split into first and second half of the year
        first_half = df[df["trip_date"] < "2023-07-01"]
        second_half = df[df["trip_date"] >= "2023-07-01"]

        # Aggregate: total efficiency and number of trips per driver
        def aggregate_efficiency(data):
            grouped = data.groupby(["driver_id", "driver_name"], as_index=False).agg(
                total_efficiency=("efficiency", "sum"),
                trip_count=("trip_id", "count"),
            )
            grouped["avg_efficiency"] = grouped["total_efficiency"] / grouped["trip_count"]
            return grouped

        first_agg = aggregate_efficiency(first_half)
        second_agg = aggregate_efficiency(second_half)

        # Merge first and second half data on driver_id
        merged = pd.merge(
            first_agg[["driver_id", "driver_name", "avg_efficiency"]],
            second_agg[["driver_id", "avg_efficiency"]],
            on="driver_id",
            suffixes=("_first", "_second"),
        )

        # Calculate improvement
        merged["efficiency_improvement"] = round(merged["avg_efficiency_second"] - merged["avg_efficiency_first"], 2)

        # Round efficiency values for clarity
        merged["avg_efficiency_first"] = round(merged["avg_efficiency_first"], 2)
        merged["avg_efficiency_second"] = round(merged["avg_efficiency_second"], 2)

        # Filter and rename for final output
        improved = merged[merged["efficiency_improvement"] > 0].rename(
            columns={
                "avg_efficiency_first": "first_half_avg",
                "avg_efficiency_second": "second_half_avg",
            }
        )

        return improved.sort_values(by=["efficiency_improvement", "driver_name"], ascending=[False, True])

    return


if __name__ == "__main__":
    app.run()
