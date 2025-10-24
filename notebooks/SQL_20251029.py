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
            "/notebooks/SQL_20251028.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251030.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 3053

    Table: Triangles

    | Column Name | Type | 
    |-------------|------|
    | A           | int  | 
    | B           | int  |
    | C           | int  |

    (A, B, C) is the primary key for this table. Each row include the lengths of each of a triangle's three sides.

    Write a query to find the type of triangle. Output one of the following for each row:

    - Equilateral: It's a triangle with 3 sides of equal length.
    - Isosceles: It's a triangle with 2 sides of equal length.
    - Scalene: It's a triangle with 3 sides of differing lengths.
    - Not A Triangle: The given values of A, B, and C don't form a triangle.

    Return the result table in any order.
    """
    )
    return


@app.cell
def _():
    """
    SELECT
        CASE
            WHEN A + B <= C OR A + C <= B OR B + C <= A THEN 'Not A Triangle'
            WHEN A = B AND B = C THEN 'Equilateral'
            WHEN A = B OR A = C OR C = B THEN 'Isosceles'
            ELSE 'Scalene'
        END AS triangle_type
    FROM
        Triangles
    """
    return


@app.cell
def _():
    import pandas as pd

    def get_type(row):
        a, b, c = row["A"], row["B"], row["C"]

        if a + b <= c or a + c <= b or b + c <= a:
            return "Not A Triangle"
        elif a == b and b == c:
            return "Equilateral"
        elif a == b or b == c or c == a:
            return "Isosceles"
        else:
            return "Scalene"

    def type_of_triangle(triangles):
        triangles["triangle_type"] = triangles.apply(get_type, axis="columns")
        return triangles[["triangle_type"]]

    return


if __name__ == "__main__":
    app.run()
