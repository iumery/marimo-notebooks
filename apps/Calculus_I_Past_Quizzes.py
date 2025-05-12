import marimo

__generated_with = "0.13.6"
app = marimo.App(width="columns")


@app.cell(column=0)
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.pdf(
        src="/public/Quiz 1.pdf",
        width="100%",
        height="50vh",
    )
    return


@app.cell(column=1)
def _(mo):
    mo.pdf(
        src="/public/Quiz 2.pdf",
        width="100%",
        height="50vh",
    )
    return


@app.cell(column=2)
def _(mo):
    mo.pdf(
        src="/public/Quiz 3.pdf",
        width="100%",
        height="50vh",
    )
    return


@app.cell(column=3)
def _(mo):
    mo.pdf(
        src="/public/Quiz 4.pdf",
        width="100%",
        height="50vh",
    )
    return


@app.cell(column=4)
def _(mo):
    mo.pdf(
        src="/public/Quiz 5.pdf",
        width="100%",
        height="50vh",
    )
    return


@app.cell(column=5)
def _(mo):
    mo.pdf(
        src="/public/Quiz 6.pdf",
        width="100%",
        height="50vh",
    )
    return


@app.cell(column=6)
def _(mo):
    mo.pdf(
        src="/public/Quiz 7.pdf",
        width="100%",
        height="50vh",
    )
    return


if __name__ == "__main__":
    app.run()
