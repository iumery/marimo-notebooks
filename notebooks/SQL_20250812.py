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
            "/notebooks/SQL_20250811.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250813.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 3642

    Table: books

    | Column Name | Type    |
    |-------------|---------|
    | book_id     | int     |
    | title       | varchar |
    | author      | varchar |
    | genre       | varchar |
    | pages       | int     |

    book_id is the unique ID for this table. Each row contains information about a book including its genre and page count.

    Table: reading_sessions

    | Column Name    | Type    |
    |----------------|---------|
    | session_id     | int     |
    | book_id        | int     |
    | reader_name    | varchar |
    | pages_read     | int     |
    | session_rating | int     |

    session_id is the unique ID for this table. Each row represents a reading session where someone read a portion of a book. session_rating is on a scale of 1-5.

    Write a solution to find books that have polarized opinions - books that receive both very high ratings and very low ratings from different readers.

    - A book has polarized opinions if it has at least one rating ≥ 4 and at least one rating ≤ 2
    - Only consider books that have at least 5 reading sessions
    - Calculate the rating spread as (highest_rating - lowest_rating)
    - Calculate the polarization score as the number of extreme ratings (ratings ≤ 2 or ≥ 4) divided by total sessions
    - Only include books where polarization score ≥ 0.6 (at least 60% extreme ratings)
    - Return the result table ordered by polarization score in descending order, then by title in descending order.
    """
    )
    return


@app.cell
def _():
    """
    WITH session_summary AS (
        SELECT
            book_id,
            MIN(session_rating) AS min_session_rating,
            MAX(session_rating) AS max_session_rating,
            SUM(CASE WHEN session_rating <= 2 THEN 1 WHEN session_rating >=4 THEN 1 ELSE 0 END) AS polarization_session_count,
            COUNT(session_id) AS session_count
        FROM
            reading_sessions
        GROUP BY
            1
    )
    SELECT
        book_id,
        title,
        author,
        genre,
        pages,
        max_session_rating - min_session_rating AS rating_spread,
        ROUND(polarization_session_count * 1.0 / session_count, 2) AS polarization_score
    FROM
        session_summary
            JOIN books USING(book_id)
    WHERE
        min_session_rating <= 2
        AND max_session_rating >= 4
        AND session_count >= 5
        AND polarization_session_count * 1.0 / session_count >= 0.6
    ORDER BY
        7 DESC, 2 DESC;
    """
    return


@app.cell
def _():
    import pandas as pd

    def find_polarized_books(books: pd.DataFrame, reading_sessions: pd.DataFrame) -> pd.DataFrame:
        session_summary = reading_sessions.groupby("book_id").agg(
            session_count=("session_id", len),
            min_rating=("session_rating", "min"),
            max_rating=("session_rating", "max"),
            polarization=(
                "session_rating",
                lambda x: len(x[x >= 4]) + len(x[x <= 2]),
            ),
            polarization_score=(
                "session_rating",
                lambda x: round((len(x[x >= 4]) + len(x[x <= 2])) * 1.0 / len(x), 2),
            ),
            rating_spread=("session_rating", lambda x: x.max() - x.min()),
        )
        df = pd.merge(session_summary, books, on="book_id", how="left")
        df = df[(df["session_count"] >= 5) & (df["min_rating"] <= 2) & (df["max_rating"] >= 4) & (df["polarization_score"] >= 0.6)]
        return df[
            [
                "book_id",
                "title",
                "author",
                "genre",
                "pages",
                "rating_spread",
                "polarization_score",
            ]
        ].sort_values(by=["polarization_score", "title"], ascending=[False, False])

    return


if __name__ == "__main__":
    app.run()
