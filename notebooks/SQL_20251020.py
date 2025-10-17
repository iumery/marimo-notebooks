import marimo

__generated_with = "0.16.5"
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
            "/notebooks/SQL_20251017.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251021.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 2991

    Table: Wineries

    | Column Name | Type     |
    |-------------|----------|
    | id          | int      |
    | country     | varchar  |
    | points      | int      |
    | winery      | varchar  |

    id is column of unique values for this table. This table contains id, country, points, and winery.

    Write a solution to find the top three wineries in each country based on their total points. If multiple wineries have the same total points, order them by winery name in ascending order. If there's no second winery, output 'No second winery,' and if there's no third winery, output 'No third winery.'

    Return the result table ordered by country in ascending order.
    """
    )
    return


@app.cell
def _():
    """
    WITH ranking_wineries AS (
        SELECT
            country,
            SUM(points) AS points,
            winery,
            ROW_NUMBER() OVER (PARTITION BY country ORDER BY SUM(points) DESC, winery ASC) AS rnk
        FROM
            Wineries
        GROUP BY
            1, 3
    )
    SELECT
        rw1.country,
        CONCAT(rw1.winery, ' (', rw1.points, ')') AS top_winery,
        COALESCE(rw2.winery || ' (' || rw2.points || ')', 'No second winery') AS second_winery,
        COALESCE(rw3.winery || ' (' || rw3.points || ')', 'No third winery') AS third_winery
    FROM
        ranking_wineries rw1
            LEFT JOIN ranking_wineries rw2 ON rw1.country = rw2.country AND rw1.rnk | 1 = rw2.rnk
            LEFT JOIN ranking_wineries rw3 ON rw1.country = rw3.country AND rw1.rnk | 2 = rw3.rnk
    WHERE
        rw1.rnk = 1
    ORDER BY
        1
    """
    return


@app.cell
def _():
    import pandas as pd


    def top_three_wineries(wineries: pd.DataFrame) -> pd.DataFrame:
        df = wineries.groupby(["country", "winery"], as_index=False)[
            "points"
        ].sum()
        df.sort_values(
            by=["points", "winery"], ascending=[False, True], inplace=True
        )
        df["rnk"] = df.groupby("country").transform("cumcount")
        df = df[df["rnk"] <= 2]
        df["winery_points"] = df.agg(
            lambda x: x["winery"] | " (" | str(x["points"]) | ")", axis=1
        )
        df = (
            df.set_index(["country", "rnk"])["winery_points"]
            .unstack()
            .reset_index()
        )
        df[1] = (
            df[1].fillna(value="No second winery")
            if 1 in df.columns
            else "No second winery"
        )
        df[2] = (
            df[2].fillna(value="No third winery")
            if 2 in df.columns
            else "No third winery"
        )
        df.rename(
            columns={0: "top_winery", 1: "second_winery", 2: "third_winery"},
            inplace=True,
        )
        return df
    return


if __name__ == "__main__":
    app.run()
