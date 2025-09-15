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
            "/notebooks/SQL_20250816.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250818.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 3475

    Table: Samples

    | Column Name    | Type    | 
    |----------------|---------|
    | sample_id      | int     |
    | dna_sequence   | varchar |
    | species        | varchar |

    sample_id is the unique key for this table. Each row contains a DNA sequence represented as a string of characters (A, T, G, C) and the species it was collected from.

    Biologists are studying basic patterns in DNA sequences. Write a solution to identify sample_id with the following patterns:

    - Sequences that start with ATG (a common start codon)
    - Sequences that end with either TAA, TAG, or TGA (stop codons)
    - Sequences containing the motif ATAT (a simple repeated pattern)
    - Sequences that have at least 3 consecutive G (like GGG or GGGG)
    - Return the result table ordered by sample_id in ascending order.
    """
    )
    return


@app.cell
def _():
    """
    SELECT
        sample_id,
        dna_sequence,
        species,
        CASE
            WHEN dna_sequence LIKE 'ATG%' THEN 1
            ELSE 0
        END AS has_start,
        CASE
            WHEN dna_sequence LIKE '%TAA' OR dna_sequence LIKE '%TAG' OR dna_sequence LIKE '%TGA' THEN 1
            ELSE 0
        END AS has_stop,
        CASE
            WHEN dna_sequence LIKE '%ATAT%' THEN 1
            ELSE 0
        END AS has_atat,
        CASE
            WHEN dna_sequence LIKE '%GGG%' THEN 1
            ELSE 0
        END AS has_ggg
    FROM
        Samples
    ORDER BY
        1
    """
    return


@app.cell
def _():
    import pandas as pd

    def analyze_dna_patterns(samples: pd.DataFrame) -> pd.DataFrame:
        samples["has_start"] = samples.dna_sequence.str.startswith("ATG").astype(int)
        samples["has_stop"] = samples.dna_sequence.str.endswith(("TAA", "TAG", "TGA")).astype(int)
        samples["has_atat"] = samples.dna_sequence.str.contains("ATAT").astype(int)
        samples["has_ggg"] = samples.dna_sequence.str.contains(("GGG")).astype(int)

        return samples.sort_values("sample_id")

    return


if __name__ == "__main__":
    app.run()
