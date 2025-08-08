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
            "/notebooks/SQL_20250808.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250810.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 3586

    Table: patients

    | Column Name | Type    |
    |-------------|---------|
    | patient_id  | int     |
    | patient_name| varchar |
    | age         | int     |

    patient_id is the unique identifier for this table. Each row contains information about a patient.

    Table: covid_tests

    | Column Name | Type    |
    |-------------|---------|
    | test_id     | int     |
    | patient_id  | int     |
    | test_date   | date    |
    | result      | varchar |

    test_id is the unique identifier for this table. Each row represents a COVID test result. The result can be Positive, Negative, or Inconclusive.

    Write a solution to find patients who have recovered from COVID - patients who tested positive but later tested negative.

    - A patient is considered recovered if they have at least one Positive test followed by at least one Negative test on a later date  
    - Calculate the recovery time in days as the difference between the first positive test and the first negative test after that positive test  
    - Only include patients who have both positive and negative test results  
    - Return the result table ordered by recovery_time in ascending order, then by patient_name in ascending order.  
    """
    )
    return


@app.cell
def _():
    """
    WITH first_positives AS (
        SELECT DISTINCT ON (patient_id)
            *
        FROM
            covid_tests
        WHERE
            result = 'Positive'
        ORDER BY
            patient_id,test_date
    ), recovery AS (
        SELECT DISTINCT ON (f.patient_id)
            f.patient_id,
            p.patient_name,
            p.age,
            c.test_date - f.test_date AS recovery_time
        FROM
            first_positives f
                JOIN covid_tests c ON f.patient_id = c.patient_id AND c.result = 'Negative' AND c.test_date >= f.test_date
                JOIN patients p ON f.patient_id = p.patient_id
        ORDER BY
            f.patient_id, c.test_date
    )
    SELECT
        *
    FROM
        recovery
    ORDER BY
        4, 2 ASC;
    """
    return


@app.cell
def _():
    import pandas as pd


    def find_covid_recovery_patients(
        patients: pd.DataFrame, covid_tests: pd.DataFrame
    ) -> pd.DataFrame:
        frstPos = (
            covid_tests[covid_tests.result == "Positive"]
            .groupby("patient_id")
            .agg(Pos_date=("test_date", "min"))
            .reset_index()
        )
        df = covid_tests.merge(frstPos)

        frstNeg = (
            df[(df.test_date > df.Pos_date) & (df.result == "Negative")]
            .groupby("patient_id")
            .agg(Neg_date=("test_date", "min"))
            .reset_index()
        )
        df = frstPos.merge(frstNeg).dropna()

        df["recovery_time"] = (
            pd.to_datetime(df.Neg_date) - pd.to_datetime(df.Pos_date)
        ).dt.days

        df = df.merge(patients).sort_values(["recovery_time", "patient_name"])
        return df.iloc[:, [0, 4, 5, 3]]
    return


if __name__ == "__main__":
    app.run()
