import marimo

__generated_with = "0.17.8"
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
            "/notebooks/SQL_20251119.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251121.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### LeetCode 3150

    Table: Tweets

    | Column Name    | Type    |
    |----------------|---------|
    | tweet_id       | int     |
    | content        | varchar |

    tweet_id is the primary key (column with unique values) for this table. This table contains all the tweets in a social media app.

    Write a solution to find invalid tweets. A tweet is considered invalid if it meets any of the following criteria:

    - It exceeds 140 characters in length.
    - It has more than 3 mentions.
    - It includes more than 3 hashtags.

    Return the result table ordered by tweet_id in ascending order.
    """)
    return


@app.cell
def _():
    """
    SELECT
        tweet_id
    FROM
        Tweets
    WHERE
        LENGTH(content) > 140
            OR content LIKE '%@%@%@%@%'
            OR content LIKE '%#%#%#%#%'
    ORDER BY
        1;
    """
    return


@app.cell
def _():
    import pandas as pd

    def find_invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
        df = tweets.copy()
        df = df[(df["content"].str.len() > 140) | (df["content"].str.count("#") > 3) | (df["content"].str.count("@") > 3)][["tweet_id"]]
        df.sort_values("tweet_id", inplace=True)
        return df
    return


if __name__ == "__main__":
    app.run()
