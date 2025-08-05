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
        },
        orientation="vertical",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Schedule""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    1. **Schedule and exam covering materials are subject to change, all midterm exams will be announced at least one week ahead during lectures**;
    2. **Quizzes may be given on any day of the week**;
    3. **Midterm exams are always given on Tuesday of the week, 75 minutes allowed**.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    | Week | Content | Note |
    | ------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
    | Week of 01/13 | Introduction: Syllabus, Course Policies<br/>1.1: Functions and Their Representation<br/>1.2: A Catalog of Essential Functions<br/>1.3: The Limit of a Function<br/>**Diagnostic Quiz** ||
    | Week of 01/20 | 1.4: Calculating Limits | **Jan 20: Dr. Martin Luther King Jr. Day, no school**<br/>**Jan 22: Last day to add a course** |
    | Week of 01/27 | 1.5: Continuity<br/>1.6: Limits Involving Infinity<br/>**Quiz 1** | **Jan 29: Last day to drop without "W"** |
    | Week of 02/03 | 2.1: Derivatives and Rates of Change<br/>2.2: Derivative as a Function<br/>Exam 1 Review<br/>**Exam 1: Chapter 1, Sections 2.1, 2.2** ||
    | Week of 02/10 | 2.3: Basic Differentiation Formulas<br/>2.4: The Product and Quotient Rules<br/>2.5: The Chain Rule<br/>**Quiz 2** ||
    | Week of 02/17 | 2.6: Implicit Differentiation<br/>2.7: Related Rates<br/>**Quiz 3** ||
    | Week of 02/24 | 3.1: Maximum and minimum Values<br/>3.3: Derivatives and the Shapes of Graphs<br/>3.4: Curve Sketching ||
    | Week of 03/03 | 3.2: The Mean Value Theorem<br/>Exam 2 Review<br/>**Exam 2: Sections 2.3 through 2.7, Sections 3.1, 3.3, 3.4 (possibly 3.2)** ||
    | Week of 03/10 |  | **Mar 8-16: Fall recess** |
    | Week of 03/17 | 3.5: Optimization Problems<br/>**Quiz 4** ||
    | Week of 03/24 | 4.1: Areas<br/>4.2: Definite Integral<br/>**Quiz 5** ||
    | Week of 03/31 | 3.7: Antiderivatives<br/>4.3: Evaluating Definite Integrals<br/>**Quiz 6** |  |
    | Week of 04/07 | 4.4: Fundamental Theorem Of Calculus<br/>4.5: Substitution Method |**Apr 11: Last day to drop**|
    | Week of 04/14 | 7.1: Area between Curves<br/>Exam 3 Review<br/>**Exam 3: Sections 3.2, 3.5, 3.7, Chapter 4** ||
    | Week of 04/21 | 7.2: Volumes by Slicing<br/>**Quiz 7** |  |
    | Week of 04/28 | Final exam review and catch up ||

    Final exam: Thursday, May 1st from 08:00 PM to 10:30 PM
    """
    )
    return


if __name__ == "__main__":
    app.run()
