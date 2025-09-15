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
            "/notebooks/SQL_20250810.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250812.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 3570

    Table: library_books

    | Column Name      | Type    |
    |------------------|---------|
    | book_id          | int     |
    | title            | varchar |
    | author           | varchar |
    | genre            | varchar |
    | publication_year | int     |
    | total_copies     | int     |

    book_id is the unique identifier for this table. Each row contains information about a book in the library, including the total number of copies owned by the library.

    Table: borrowing_records

    | Column Name   | Type    |
    |---------------|---------|
    | record_id     | int     |
    | book_id       | int     |
    | borrower_name | varchar |
    | borrow_date   | date    |
    | return_date   | date    |

    record_id is the unique identifier for this table. Each row represents a borrowing transaction and return_date is NULL if the book is currently borrowed and hasn't been returned yet.

    Write a solution to find all books that are currently borrowed (not returned) and have zero copies available in the library.

    - A book is considered currently borrowed if there exists a borrowing record with a NULL return_date
    - Return the result table ordered by current borrowers in descending order, then by book title in ascending order.
    """
    )
    return


@app.cell
def _():
    """
    WITH borrowed_count AS (
        SELECT
            book_id,
            SUM(CASE WHEN return_date IS NULL THEN 1 ELSE 0 END) AS current_borrowers
        FROM
            borrowing_records
        GROUP BY
            book_id
    )
    SELECT
        book_id,
        title,
        author,
        genre,
        publication_year,
        current_borrowers
    FROM
        library_books
            LEFT JOIN borrowed_count USING(book_id) WHERE current_borrowers = total_copies
    ORDER BY
        6 DESC, 2;
    """
    return


@app.cell
def _():
    import pandas as pd

    def find_books_with_no_available_copies(library_books: pd.DataFrame, borrowing_records: pd.DataFrame) -> pd.DataFrame:
        # Filter borrowing_records to unreturned books only
        borrowing_records = borrowing_records[borrowing_records.return_date.isnull()]

        # Count the copies per title still unreturned
        df = borrowing_records.groupby("book_id").count().reset_index()

        # Merge the dataframes
        df = df.merge(library_books).rename(columns={"total_copies": "current_borrowers"})

        # Filter for titles for which all copies are unreturned
        df = df[df.record_id == df.current_borrowers]

        # Sort rows and rearrange columns as directed
        return df.sort_values(["current_borrowers", "title"], ascending=[False, True]).iloc[:, [0, 5, 6, 7, 8, 9]]

    return


if __name__ == "__main__":
    app.run()
