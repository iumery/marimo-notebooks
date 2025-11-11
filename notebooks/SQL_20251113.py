import marimo

__generated_with = "0.17.4"
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
            "/notebooks/SQL_20251112.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251114.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### LeetCode 3103

    Table: Tweets

    | Column Name | Type    |
    |-------------|---------|
    | user_id     | int     |
    | tweet_id    | int     |
    | tweet_date  | date    |
    | tweet       | varchar |

    tweet_id is the primary key (column with unique values) for this table. Each row of this table contains user_id, tweet_id, tweet_date and tweet.
    It is guaranteed that all tweet_date are valid dates in February 2024.

    Write a solution to find the top 3 trending hashtags in February 2024. Every tweet may contain several hashtags.

    Return the result table ordered by count of hashtag, hashtag in descending order.
    """)
    return


@app.cell
def _():
    """
    WITH extracted AS (
        SELECT
            REGEXP_MATCHES(tweet, '(#[A-z]+)', 'g') AS hashtag
        FROM
            Tweets
    )
    SELECT
        hashtag[1],
        COUNT(*) AS count
    FROM
        extracted
    GROUP BY
        1
    ORDER BY
        2 desc,
        1 desc
    LIMIT
        3;
    """
    return


@app.cell
def _():
    import pandas as pd


    def find_trending_hashtags(tweets: pd.DataFrame) -> pd.DataFrame:
        df = tweets[
            (tweets["tweet_date"].dt.year == 2024)
            & (tweets["tweet_date"].dt.month == 2)
        ]
        df = df["tweet"].str.findall(r"(#\w+)").explode()
        df = df.value_counts().reset_index().rename(columns={"tweet": "hashtag"})
        df = df.sort_values(
            by=["count", "hashtag"], ascending=[False, False]
        ).head(3)
        return df
    return


if __name__ == "__main__":
    app.run()
