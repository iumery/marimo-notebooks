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
            "/notebooks/SQL_20250909.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250911.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 2314

    Table: Weather

    | Column Name | Type |
    |-------------|------|
    | city_id     | int  |
    | day         | date |
    | degree      | int  |

    (city_id, day) is the primary key (combination of columns with unique values) for this table. Each row in this table contains the degree of the weather of a city on a certain day. All the degrees are recorded in the year 2022.
 
    Write a solution to report the day that has the maximum recorded degree in each city. If the maximum degree was recorded for the same city multiple times, return the earliest day among them.

    Return the result table ordered by city_id in ascending order.
    """
    )
    return


@app.cell
def _():
    """
    SELECT
        city_id,
        day,
        degree
    FROM (
        SELECT
            *,
            ROW_NUMBER() OVER (PARTITION BY city_id ORDER BY degree DESC, day ASC) AS rank
        FROM
            Weather
    )
    WHERE
        rank = 1
    ORDER BY
        city_id;
    """
    return


@app.cell
def _():
    import pandas as pd

    def find_the_first_day(weather: pd.DataFrame) -> pd.DataFrame:
        weather = weather.sort_values(["degree", "day", "city_id"], ascending=[False, True, True])
        weather["row_number"] = weather.groupby("city_id").cumcount()
        sub_weather = weather[weather["row_number"] == 0][["city_id", "day", "degree"]].sort_values("city_id")
        return sub_weather

    return


if __name__ == "__main__":
    app.run()
