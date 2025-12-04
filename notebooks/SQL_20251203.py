import marimo

__generated_with = "0.18.1"
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
            "/notebooks/SQL_20251202.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251204.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### LeetCode 3198

    Table: cities

    | Column Name | Type    |
    |-------------|---------|
    | state       | varchar |
    | city        | varchar |

    (state, city) is the primary key (combination of columns with unique values) for this table. Each row of this table contains the state name and the city name within that state.

    Write a solution to find all the cities in each state and combine them into a single comma-separated string.

    Return the result table ordered by state and city in ascending order.
    """)
    return


@app.cell
def _():
    """
    SELECT
        state,
        STRING_AGG(city, ', ' ORDER BY city) AS cities
    FROM
        cities
    GROUP BY
        1
    ORDER BY
        1;
    """
    return


@app.cell
def _():
    import pandas as pd


    def find_cities(cities):
        df = (
            cities.groupby("state")["city"]
            .apply(lambda x: ", ".join(sorted(x)))
            .reset_index(name="cities")
        )
        df.sort_values(by=["state", "cities"], inplace=True)
        return df
    return


if __name__ == "__main__":
    app.run()
