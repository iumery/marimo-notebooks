import marimo

__generated_with = "0.15.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    from scipy.stats import binomtest
    return mo, pd


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


@app.cell
def _(mo, pd):
    df = pd.read_csv(mo.notebook_location() / "public" / "cookie_cats.csv")
    return (df,)


@app.cell
def _(df):
    df.head()
    return


@app.cell
def _(df):
    # Basic summary
    df.describe()
    return


@app.cell
def _(df):
    df.isna().sum()
    return


@app.cell
def _(df):
    df.duplicated("userid").sum()
    return


@app.cell
def _(df):
    df.groupby("version")["userid"].count()
    return


@app.cell
def _(df):
    counts = df.groupby("version")["userid"].count()

    if len(counts) != 2:
        raise ValueError("Expected exactly two groups")

    n_1 = counts.iloc[0]
    n_2 = counts.iloc[1]
    N = n_1 + n_2
    vif = 0.5 * (1 - 0.5) / ((n_1 / N) * (1 - n_1 / N))
    power_loss_pct = (vif - 1) * 100

    print(
        f"Variance inflation factor: {vif:.8f}, Percentage power loss: {power_loss_pct:.2f}%"
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
