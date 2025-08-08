import marimo

__generated_with = "0.14.16"
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
            "/notebooks/SQL_20250809.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250811.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 3580

    Table: employees

    | Column Name | Type    |
    |-------------|---------|
    | employee_id | int     |
    | name        | varchar |

    employee_id is the unique identifier for this table. Each row contains information about an employee.

    Table: performance_reviews

    | Column Name | Type |
    |-------------|------|
    | review_id   | int  |
    | employee_id | int  |
    | review_date | date |
    | rating      | int  |

    review_id is the unique identifier for this table. Each row represents a performance review for an employee. The rating is on a scale of 1-5 where 5 is excellent and 1 is poor.

    Write a solution to find employees who have consistently improved their performance over their last three reviews.

    - An employee must have at least 3 review to be considered
    - The employee's last 3 reviews must show strictly increasing ratings (each review better than the previous)
    - Use the most recent 3 reviews based on review_date for each employee
    - Calculate the improvement score as the difference between the latest rating and the earliest rating among the last 3 reviews
    - Return the result table ordered by improvement score in descending order, then by name in ascending order.
    """
    )
    return


@app.cell
def _():
    """
    WITH process_1 AS (
        SELECT DISTINCT
            p.employee_id,
            sub.review_date,
            sub.rating
        FROM
            performance_reviews p
                JOIN LATERAL (
                    SELECT
                        p1.review_date,
                        p1.rating
                    FROM
                        performance_reviews p1
                    WHERE
                        p.employee_id = p1.employee_id
                    ORDER BY
                        1 DESC
                    LIMIT 3
                )sub ON 1 = 1
    ),
    process_2 AS (
        SELECT
            p.employee_id,
            p.rating,
            sub.rating rating_1,
            sub.review_date
        FROM
            process_1 p
                LEFT JOIN LATERAL (
                    SELECT
                        p1.rating,
                        p1.review_date
                    FROM
                        process_1 p1
                    WHERE
                        p.employee_id = p1.employee_id
                        AND
                        p1.rating > p.rating
                    LIMIT 1
                )sub ON 1 = 1
        WHERE p.rating < sub.rating
    )
    SELECT
        p.employee_id,
        (
            SELECT DISTINCT
                name
            FROM
                employees e
            WHERE
                e.employee_id = p.employee_id
        ),
        MAX(rating_1) - MIN(rating) improvement_score
    FROM
        process_2 p
    GROUP BY
        p.employee_id,
        name
    HAVING
        COUNT(DISTINCT review_date) > 1
    ORDER BY
        improvement_score DESC,
        name;
    """
    return


@app.cell
def _():
    import pandas as pd


    def find_consistently_improving_employees(
        employees: pd.DataFrame, performance_reviews: pd.DataFrame
    ) -> pd.DataFrame:
        performance_reviews["rank"] = performance_reviews.groupby("employee_id")[
            "review_date"
        ].rank(ascending=False)

        df = performance_reviews[performance_reviews["rank"] <= 3]

        df = df.pivot(
            index="employee_id", columns="rank", values="rating"
        ).reset_index()

        df = df.dropna()[(df[1] > df[2]) & (df[2] > df[3])]
        df["improvement_score"] = df[1] - df[3]

        return (
            df.merge(employees)
            .sort_values(["improvement_score", "name"], ascending=[0, 1])
            .iloc[:, [0, 5, 4]]
        )
    return


if __name__ == "__main__":
    app.run()
