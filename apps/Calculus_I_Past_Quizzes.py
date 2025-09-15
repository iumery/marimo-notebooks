import marimo

__generated_with = "0.15.4"
app = marimo.App(width="columns")


@app.cell(column=0)
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    nav_menu = mo.nav_menu(
        {
            "/index.html": f"{mo.icon('lucide:home')} Home",
        },
        orientation="vertical",
    )
    nav_menu
    return (nav_menu,)


@app.cell
def _(mo):
    mo.md(
        r"""
    /// danger | Important Note:

    # The exams and quizzes provided here are for reference only. The actual content, topics, and coverage of future assessments may differ. Please always follow my in-class or email announcements and guidelines for the specific material covered on upcoming tests.
    ///
    """
    )
    return


@app.cell(column=1)
def _(nav_menu):
    nav_menu
    return


@app.cell
def _(mo):
    mo.pdf(
        src="public/Quiz 1.pdf",
        width="100%",
        height="80vh",
    )
    return


@app.cell(column=2)
def _(nav_menu):
    nav_menu
    return


@app.cell
def _(mo):
    mo.pdf(
        src="public/Quiz 2.pdf",
        width="100%",
        height="80vh",
    )
    return


@app.cell(column=3)
def _(nav_menu):
    nav_menu
    return


@app.cell
def _(mo):
    mo.pdf(
        src="public/Quiz 3.pdf",
        width="100%",
        height="80vh",
    )
    return


@app.cell(column=4)
def _(nav_menu):
    nav_menu
    return


@app.cell
def _(mo):
    mo.pdf(
        src="public/Quiz 4.pdf",
        width="100%",
        height="80vh",
    )
    return


@app.cell(column=5)
def _(nav_menu):
    nav_menu
    return


@app.cell
def _(mo):
    mo.pdf(
        src="public/Quiz 5.pdf",
        width="100%",
        height="80vh",
    )
    return


@app.cell(column=6)
def _(nav_menu):
    nav_menu
    return


@app.cell
def _(mo):
    mo.pdf(
        src="public/Quiz 6.pdf",
        width="100%",
        height="80vh",
    )
    return


@app.cell(column=7)
def _(nav_menu):
    nav_menu
    return


@app.cell
def _(mo):
    mo.pdf(
        src="public/Quiz 7.pdf",
        width="100%",
        height="80vh",
    )
    return


if __name__ == "__main__":
    app.run()
