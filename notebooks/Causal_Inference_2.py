import marimo

__generated_with = "0.15.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import numpy as np
    import plotly.express as px
    from statsmodels.stats.proportion import proportions_ztest, proportion_confint
    from scipy.stats import chi2_contingency
    import statsmodels.api as sm
    import statsmodels.formula.api as smf
    from scipy import stats
    return (
        chi2_contingency,
        mo,
        np,
        pd,
        proportion_confint,
        proportions_ztest,
        px,
        smf,
        stats,
    )


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
    df = pd.read_csv(mo.notebook_location() / "public" / "marketing_AB.csv")
    df.drop(axis=1, columns=["Unnamed: 0"], inplace=True)
    return (df,)


@app.cell
def _(df):
    df.head()
    return


@app.cell
def _(df):
    df["converted"] = df["converted"].astype(int)
    return


@app.cell
def _(df):
    df.describe()
    return


@app.cell
def _(df):
    df[df.duplicated("user id")]
    return


@app.cell
def _(df):
    df.isna().sum()
    return


@app.cell
def _(df):
    df["test group"].value_counts(normalize=True)
    return


@app.cell
def _(df):
    df["converted"].value_counts(normalize=True)
    return


@app.cell
def _(df):
    df["most ads day"].value_counts(normalize=True)
    return


@app.cell
def _(df, mo, pd, px):
    counts_1 = pd.cut(df["total ads"], bins=50).value_counts().sort_index()
    fig_1 = px.bar(
        x=[str(c) for c in counts_1.index],
        y=counts_1.values,
        labels={"x": "total ads (bins)", "y": "count"},
        title="Binned Histogram: total ads",
    )
    plot_1 = mo.ui.plotly(fig_1)
    plot_1
    return


@app.cell
def _(df, mo, pd, px):
    counts_2 = pd.cut(df["most ads hour"], bins=24).value_counts().sort_index()
    fig_2 = px.bar(
        x=[str(c) for c in counts_2.index],
        y=counts_2.values,
        labels={"x": "most ads hour (bins)", "y": "count"},
        title="Binned Histogram: most ads hour",
    )
    plot_2 = mo.ui.plotly(fig_2)
    plot_2
    return


@app.cell
def _(df, np):
    upper = df["total ads"].quantile(0.99)
    df["total ads winsor"] = np.clip(df["total ads"], None, upper)
    return


@app.cell
def _(df, mo, pd, px):
    counts_3 = pd.cut(df["total ads winsor"], bins=50).value_counts().sort_index()
    fig_3 = px.bar(
        x=[str(c) for c in counts_3.index],
        y=counts_3.values,
        labels={"x": "total ads, winsored (bins)", "y": "count"},
        title="Binned Histogram: total ads, winsored",
    )
    plot_3 = mo.ui.plotly(fig_3)
    plot_3
    return


@app.cell
def _(df, np, proportion_confint, proportions_ztest):
    conv_counts = df.groupby("test group")["converted"].sum()
    n_obs = df.groupby("test group")["converted"].count()

    # Order groups for clarity
    success = np.array([conv_counts["ad"], conv_counts["psa"]])
    nobs = np.array([n_obs["ad"], n_obs["psa"]])

    # Two-proportion z-test
    z_stat, p_val = proportions_ztest(success, nobs)
    ci_low, ci_upp = proportion_confint(success, nobs, alpha=0.05, method="normal")

    print("Conversion rates:")
    print(f"ad:  {success[0]}/{nobs[0]} = {success[0]/nobs[0]:.3f}")
    print(f"psa: {success[1]}/{nobs[1]} = {success[1]/nobs[1]:.3f}")
    print("\nTwo-proportion z-test:")
    print(f"z = {z_stat:.3f}, p = {p_val:.4f}")
    print(f"95% CI (ad):  [{ci_low[0]:.3f}, {ci_upp[0]:.3f}]")
    print(f"95% CI (psa): [{ci_low[1]:.3f}, {ci_upp[1]:.3f}]")
    return


@app.cell
def _(df, pd):
    bins = [0, 6, 12, 18, 24]
    labels = ["Night", "Morning", "Afternoon", "Evening"]

    df["time_of_day"] = pd.cut(
        df["most ads hour"], 
        bins=bins, right=False, labels=labels
    )
    return


@app.cell
def _(df):
    df["most ads day"] = df["most ads day"].astype("category")
    df["time_of_day"]  = df["time_of_day"].astype("category")
    df["test group"]   = df["test group"].astype("category")
    return


@app.cell
def _(chi2_contingency, df, np, pd):
    def chi_sq_independence(sub: pd.DataFrame, cat_col: str):
        """
        Chi-square test of independence between `converted` and `cat_col`
        using categories as they appear in the data (no reindexing).
        Returns: dict with table, chi2, dof, p, cramers_v, n, small_expected_cells
        """
        table = pd.crosstab(sub[cat_col], sub["converted"])
        chi2, p, dof, expected = chi2_contingency(table)

        n = int(table.values.sum())
        r, c = table.shape
        phi2 = chi2 / n if n > 0 else np.nan
        v = np.sqrt(phi2 / (min(r - 1, c - 1))) if min(r, c) > 1 and n > 0 else np.nan
        small_cells = int((expected < 5).sum())

        return {
            "table": table,
            "chi2": chi2,
            "dof": dof,
            "p": p,
            "cramers_v": v,
            "n": n,
            "small_expected_cells": small_cells,
        }

    # Run for both groups and both categorical factors
    results = {}
    for group in ["ad", "psa"]:
        sub = df[df["test group"] == group]

        res_day = chi_sq_independence(sub, "most ads day")
        res_tod = chi_sq_independence(sub, "time_of_day")

        results[group] = {"day": res_day, "tod": res_tod}

    # Pretty print
    for group in ["ad", "psa"]:
        print(f"\n================ {group.upper()} GROUP ================")

        print("\nConverted ~ Most Ads Day")
        r = results[group]["day"]
        print(r["table"])
        print(f"Chi2 = {r['chi2']:.3f}, df = {r['dof']}, p = {r['p']:.4f}, Cramér's V = {r['cramers_v']:.3f}")
        if r["small_expected_cells"] > 0:
            print(f"⚠️ {r['small_expected_cells']} cells have expected count < 5.")

        print("\nConverted ~ Time of Day")
        r = results[group]["tod"]
        print(r["table"])
        print(f"Chi2 = {r['chi2']:.3f}, df = {r['dof']}, p = {r['p']:.4f}, Cramér's V = {r['cramers_v']:.3f}")
        if r["small_expected_cells"] > 0:
            print(f"⚠️ {r['small_expected_cells']} cells have expected count < 5.")
    return


@app.cell
def _(df, np, smf, stats):
    # --- 2) Baseline model -----------------------------------------------------
    formula = 'converted ~ C(Q("test group"), Treatment("psa")) + C(Q("most ads day")) + C(Q("time_of_day"))'
    model = smf.logit(formula=formula, data=df).fit(disp=False)

    print(model.summary2().tables[1].loc[lambda s: s.index.str.contains('test group')])

    # --- 3) Odds ratios & 95% CIs ---------------------------------------------
    tr_name = 'C(Q("test group"), Treatment("psa"))[T.ad]'
    beta = model.params[tr_name]
    se   = model.bse[tr_name]
    z    = 1.96

    or_point = np.exp(beta)
    or_low   = np.exp(beta - z*se)
    or_high  = np.exp(beta + z*se)

    print("\nTreatment (ad vs psa): Odds Ratio")
    print(f"OR = {or_point:.3f}   95% CI [{or_low:.3f}, {or_high:.3f}]   p = {model.pvalues[tr_name]:.4g}")

    # --- 4) Average Marginal Effect (AME) -------------------------------------
    marg = model.get_margeff(at='overall', method='dydx')
    marg_table = marg.summary_frame()

    # p-value column name differs by version: try both
    p_col = "P>|z|" if "P>|z|" in marg_table.columns else ("Pr(>|z|)" if "Pr(>|z|)" in marg_table.columns else None)
    ame_row = marg_table.loc[tr_name]

    print("\nAverage Marginal Effect of ad (on Pr[converted])")
    print(f"AME = {ame_row['dy/dx']:.4f}   SE = {ame_row['Std. Err.']:.4f}   z = {ame_row['z']:.2f}   p = {ame_row[p_col]:.4g}")

    # --- 5) Adjusted predicted probabilities by group -------------------------
    pred = (
        df.assign(_pred = model.predict(df))
          .groupby("test group", observed=True)   # <-- silence FutureWarning
          ["_pred"].mean()
          .rename("adj_predicted_conversion")
    )
    print("\nAdjusted predicted conversion by group (averaged over observed covariate mix):")
    print(pred)

    # --- 6) Heterogeneity: interaction with time_of_day ------------------------
    formula_int = 'converted ~ C(Q("test group"), Treatment("psa")) * C(Q("time_of_day")) + C(Q("most ads day"))'
    model_int = smf.logit(formula=formula_int, data=df).fit(disp=False)

    # Likelihood-ratio test: compare interaction vs baseline
    lr_stat = 2 * (model_int.llf - model.llf)
    df_diff = model_int.df_model - model.df_model
    p_lr = stats.chi2.sf(lr_stat, df_diff)

    print(f"\nInteraction LRT (group × time_of_day): chi2 = {lr_stat:.2f}, df = {df_diff}, p = {p_lr:.4g}")
    return


@app.cell
def _(df, np, pd, smf):
    def stratified_resample(df, strata_cols):
        return (df.groupby(strata_cols, observed=True, group_keys=False)
                  .apply(lambda g: g.sample(len(g), replace=True, random_state=np.random.randint(1e9))))

    def uplift_ci_stratified(df, n_boot=200, alpha=0.05):
        levels_time = list(df["time_of_day"].cat.categories)
        uplifts = {t: [] for t in levels_time}
        for _ in range(n_boot):
            df_b = stratified_resample(df, ["time_of_day", "test group"])
            # L2-regularized logit to avoid singularities
            m_b = smf.logit(
                'converted ~ C(Q("test group"), Treatment("psa")) * C(Q("time_of_day")) + C(Q("most ads day"))',
                data=df_b
            ).fit_regularized(method="l1", alpha=0.0, L1_wt=0.0)  # pure L2; alpha is ridge strength

            # adjusted rates
            rates = []
            for t in levels_time:
                for g in df["test group"].cat.categories:
                    base = df_b.copy()
                    base["time_of_day"] = t
                    base["test group"] = g
                    rates.append({"time_of_day": t, "test group": g, "adj_rate": float(m_b.predict(base).mean())})
            piv = pd.DataFrame(rates).pivot(index="time_of_day", columns="test group", values="adj_rate")
            for t in levels_time:
                uplifts[t].append(piv.loc[t, "ad"] - piv.loc[t, "psa"])
        rows = []
        for t in levels_time:
            arr = np.array(uplifts[t])
            lo, hi = np.quantile(arr, [alpha/2, 1-alpha/2])
            rows.append({"time_of_day": t, "uplift": float(arr.mean()), "uplift_lo": lo, "uplift_hi": hi})
        return pd.DataFrame(rows)

    # Example:
    lift_tod_ci = uplift_ci_stratified(df, n_boot=200)
    return (lift_tod_ci,)


@app.cell
def _(mo, px, rates_tod):
    # Bar: adjusted conversion by group per time_of_day
    fig_4 = px.bar(
        rates_tod, x="time_of_day", y="adj_rate", color="test group", barmode="group",
        labels={"adj_rate": "Adjusted conversion rate"}, title="Adjusted conversion by time of day"
    )
    plot_4 = mo.ui.plotly(fig_4)
    plot_4
    return


@app.cell
def _(lift_tod_ci, mo, px):
    # Bar with error bars: uplift by time_of_day
    fig_5 = px.bar(
        lift_tod_ci, x="time_of_day", y="uplift",
        error_y=lift_tod_ci["uplift_hi"] - lift_tod_ci["uplift"],
        error_y_minus=lift_tod_ci["uplift"] - lift_tod_ci["uplift_lo"],
        labels={"uplift": "Uplift (ad − psa)"},
        title="Uplift by time of day (95% bootstrap CI)"
    )
    plot_5 = mo.ui.plotly(fig_5)
    plot_5
    return


if __name__ == "__main__":
    app.run()
