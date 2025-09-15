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
            "/notebooks/SQL_20250802.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250805.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 3465

    Table: products

    | Column Name  | Type       |
    |--------------|------------|
    | product_id   | int        |
    | product_name | varchar    |
    | description  | varchar    |

    `product_id` is the unique key for this table.  
    Each row in the table represents a product with its unique ID, name, and description.  
    Write a solution to find all products whose description contains a valid serial number pattern. A valid serial number follows these rules:  

    - It starts with the letters SN (case-sensitive).
    - Followed by exactly 4 digits.
    - It must have a hyphen (-) followed by exactly 4 digits.
    - The serial number must be within the description (it may not necessarily start at the beginning).

    Return the result table ordered by product_id in ascending order.
    """
    )
    return


@app.cell
def _():
    r"""
    -- ~: case sensitive
    -- \m: ensure a start of a word, avoid things like ASN1234-1234
    -- SN: substring start with SN
    -- [0-9]{4}: followed by 4 digits
    -- -: followed by -
    -- [0-9]{4}: again, followed by 4 digits
    -- \M: ensure an end of a word, avoid things like SN1234-12345

    SELECT
        *
    FROM
        products
    WHERE
        description ~ '\mSN[0-9]{4}-[0-9]{4}\M'
    ORDER BY
        product_id;
    """
    return


if __name__ == "__main__":
    app.run()
