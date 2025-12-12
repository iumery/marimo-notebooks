import marimo

__generated_with = "0.18.1"
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
            "/notebooks/SQL_20251211.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251215.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### LeetCode 2253

    Table: Products

    | Column Name | Type    |
    |-------------|---------|
    | product_id  | int     |
    | store_name1 | int     |
    | store_name2 | int     |
    |      :      | int     |
    |      :      | int     |
    |      :      | int     |
    | store_namen | int     |

    product_id is the primary key for this table. Each row in this table indicates the product's price in n different stores. If the product is not available in a store, the price will be null in that store's column. The names of the stores may change from one testcase to another. There will be at least 1 store and at most 30 stores.

    Implement the procedure UnpivotProducts to reorganize the Products table so that each row has the id of one product, the name of a store where it is sold, and its price in that store. If a product is not available in a store, do not include a row with that product_id and store combination in the result table. There should be three columns: product_id, store, and price.

    The procedure should return the table after reorganizing it.

    Return the result table in any order.
    """)
    return


@app.cell
def _():
    import pandas as pd


    def find_valid_users(products: pd.DataFrame) -> pd.DataFrame:
        df = pd.melt(
            products, id_vars=["product_id"], var_name="store", value_name="price"
        )
        df.dropna(inplace=True)

        return df
    return


if __name__ == "__main__":
    app.run()
