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
        },
        orientation="vertical",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Schedule

    **Schedule and exam covering materials are subject to change, all midterm exams will be announced at least one week ahead during lectures**. **Midterm exams are always given on Thursday of the week, 75 minutes allowed**.  

    **Final exam: Friday, December 5th from 08:00 PM to 10:30 PM**.

    | Week # | Week of | Content | Note |
    | :----: | :-----: | :------ | :--- |
    | 1 | 08/18 | Introduction: Syllabus, Course Policies<br/>1.1: Functions and Their Representation<br/>1.2: A Catalog of Essential Functions |  |
    | 2 | 08/25 | 1.3: The Limit of a Function<br/>1.4: Calculating Limits| Aug 27: Last day to add a course |
    | 3 | 09/01 | 1.5: Continuity<br/>1.6: Limits Involving Infinity| Sep 1: Labor Day, No School<br/>Sep 3: Last day to drop without "W" |
    | 4 | 09/08 | 2.1: Derivatives and Rates of Change<br/>2.2: The Derivative as a Function<br/>Exam 1 Review<br/>**Exam 1: Chapter 1, Sections 2.1, 2.2** |  |
    | 5 | 09/15 | 2.3: Basic Differentiation Rules<br/>2.4: The Product and Quotient Rules<br/>2.5: The Chain Rule|  |
    | 6 | 09/22 | 2.5: The Chain Rule (continued)<br/>2.6: Implicit Differentiation<br/>2.7: Related Rates |  |
    | 7 | 09/29 | 3.1: Maximum and Minimum Values<br/>3.3: How Derivatives Affect the Graph<br/>3.4: Curve Sketching |  |
    | 8 | 10/06 | 3.4: Curve Sketching (continued)<br/>3.2: The Mean Value Theorem<br/>Exam 2 Review<br/>**Exam 2: Sections 2.3–2.7, 3.1, 3.3, 3.4** |  |
    | 9 | 10/13 | 3.5: Optimization Problems<br/>Appendix B: Sigma Notation | Fall Break: Oct 11–14 |
    | 10 | 10/20 | 4.1: Areas and Distances<br/>4.2: The Definite Integral<br/>3.7: Antiderivatives |  |
    | 11 | 10/27 | 3.7: Antiderivatives (continued)<br/>4.3: Evaluating Definite Integrals |  |
    | 12 | 11/03 | 4.4: Fundamental Theorem of Calculus<br/>4.5: The Substitution Rule | Nov 7: Last day to drop a course |
    | 13 | 11/10 | 4.5: The Substitution Rule (continued)<br/>7.1: Areas Between Curves<br/>Exam 3 Review<br/>**Exam 3: Sections 3.2, 3.5, 3.7, Chapter 4 (all)** |  |
    | 14 | 11/17 | 7.2: Volumes by Slicing |  |
    | 15 | 11/24 | Final Exam Review and Catch Up | Nov 24: Online Teaching<br/>Thanksgiving Break: Nov 25–30 |
    | 16 | 12/01 | Final Exam Review and Catch Up |  |
    """
    )
    return


if __name__ == "__main__":
    app.run()
