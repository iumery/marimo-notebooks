import marimo

__generated_with = "0.15.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import numpy as np
    import math
    import plotly.express as px
    import statsmodels.api as sm
    from scipy import stats
    return math, mo, np, pd, px, sm, stats


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
    ## Dataset Description

    This dataset comes from an A/B test in a mobile puzzle game. The experiment tested whether moving a progression gate from level 30 (control) to level 40 (treatment) affects player behavior. Each row represents a unique player with the following features:

    - `userid`: Unique identifier.
    - `version`: Group assignment (gate_30 vs. gate_40).
    - `sum_gamerounds`: Total rounds played in the first 14 days.
    - `retention_1`: Returned after 1 day (1/0).
    - `retention_7`: Returned after 7 days (1/0).

    ## Objective

    The goal is to assess whether shifting the gate impacts engagement (rounds played), short-term retention (day-1 return), and long-term retention (day-7 return). Retention is critical for mobile games: even small lifts can translate into large revenue gains. This analysis shows how causal inference and A/B testing guide product decisions, such as whether to keep the gate at level 30 or move it to 40.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Basic Preparation""")
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""There's no null value and there's no duplicated user id.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## A Quick Look at Grouped Data""")
    return


@app.cell
def _(df):
    df.groupby("version", as_index=False).agg(
        sum_gamerounds_mean=("sum_gamerounds", "mean"),
        sum_gamerounds_median=("sum_gamerounds", "median"),
        sum_gamerounds_std=("sum_gamerounds", "std"),
        sum_gamerounds_min=("sum_gamerounds", "min"),
        sum_gamerounds_max=("sum_gamerounds", "max"),
        retention_1_mean=("retention_1", "mean"),
        retention_7_mean=("retention_7", "mean"),
        count=("userid", "count"),
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Some observations:

    - Group sizes: Slight imbalance (44700 vs 45489) and can be ignored in our case. In general a useful way to assess this is via the variance inflation factor (VIF) for the group indicator defined as $\text{VIF} = \frac{1}{p(1-p)}$, where $p = \frac{N_{\text{group 1}}}{N_{\text{group 1}+N_{\text{group 2}}}}$. Our data gives a VIF about 4.0003, very close to the ideal value of $4 = \frac{1}{0.5 \cdot 0.5}$ for a 50/50 design. Thus, the imbalance is negligible.
    - Retention: gating at 40 shows slightly lower day-1 and day-7 retention. With this sample size, even small differences are likely statistically significant, but practical impact needs consideration.
    - Engagement skew: `sum_gamerounds` distributions are highly skewed. Means are far above medians, and maximum values (49854 and 2640) suggest extreme outliers.
    - Variance imbalance: Standard deviation is much larger for gate_30 than gate_40, suggesting heteroskedasticity. This affects choice of statistical test (e.g., Welch’s t-test vs. regular t-test).
    """
    )
    return


@app.cell
def _(df, mo, px):
    fig_1 = px.box(
        df,
        x="version",
        y="sum_gamerounds",
        points="outliers",  # only show outlier points beyond whiskers
        title="Boxplot of Game Rounds by Group (gate_30 vs gate_40)",
        labels={"version": "Group", "sum_gamerounds": "Total Rounds Played"},
    )

    fig_1.update_layout(
        height=500, yaxis_title="sum_gamerounds", xaxis_title="version"
    )

    plot_1 = mo.ui.plotly(fig_1)
    plot_1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Outlier Removal""")
    return


@app.cell
def _(df, mo, pd, px):
    # Winsorize at the 99th percentile within each group
    df_winsor = df.copy()
    df_winsor["sum_gamerounds"] = df_winsor["sum_gamerounds"].astype("float64")

    for v in df_winsor["version"].unique():
        cutoff = df_winsor.loc[
            df_winsor["version"] == v, "sum_gamerounds"
        ].quantile(0.99)
        mask = df_winsor["version"] == v
        df_winsor.loc[mask, "sum_gamerounds"] = df_winsor.loc[
            mask, "sum_gamerounds"
        ].clip(upper=cutoff)

    # Optional: round & cast back to integer
    df_winsor["sum_gamerounds"] = (
        df_winsor["sum_gamerounds"].round().astype("Int64")
    )

    # Add dataset labels
    df_raw = df.copy()
    df_raw["dataset"] = "Before Winsorization"
    df_winsor["dataset"] = "After Winsorization"

    df_compare = pd.concat([df_raw, df_winsor], ignore_index=True)

    # Plot
    fig_2 = px.histogram(
        df_compare,
        x="sum_gamerounds",
        color="version",
        facet_row="dataset",
        barmode="overlay",
        opacity=0.7,
        title="Distribution of Game Rounds: Before vs After Winsorization (99th percentile)",
    )

    # Independent x-axis scaling
    fig_2.update_xaxes(matches=None)

    # Show both x-axes explicitly
    fig_2.update_xaxes(showticklabels=True, row=1, col=1)
    fig_2.update_xaxes(showticklabels=True, row=2, col=1)

    # Clean facet labels
    fig_2.for_each_annotation(
        lambda a: a.update(text=a.text.replace("dataset=", ""))
    )

    fig_2.update_layout(height=700, bargap=0.05, legend_title="Version")

    plot_2 = mo.ui.plotly(fig_2)
    plot_2
    return (df_winsor,)


@app.cell
def _(df_winsor):
    df_winsor.groupby("version", as_index=False).agg(
        sum_gamerounds_mean=("sum_gamerounds", "mean"),
        sum_gamerounds_median=("sum_gamerounds", "median"),
        sum_gamerounds_std=("sum_gamerounds", "std"),
        sum_gamerounds_min=("sum_gamerounds", "min"),
        sum_gamerounds_max=("sum_gamerounds", "max"),
        retention_1_mean=("retention_1", "mean"),
        retention_7_mean=("retention_7", "mean"),
        count=("userid", "count"),
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""After winsorization at the 99th percentile, the distribution of total game rounds played has become much more stable: the mean is about 49 for both groups, the medians are 17 and 16, and the standard deviations have dropped to around 84 from the highly inflated values in the raw data – notice this means heteroskedasticity is also mitigated. The maximum values are now around 493 and 492, a sharp reduction from the tens of thousands observed earlier, confirming that the extreme outliers have been capped. Importantly, retention metrics are unchanged by this adjustment, with day-1 retention at roughly 0.448 vs. 0.442 and day-7 retention at 0.190 vs. 0.182. Overall, winsorization yields a distribution of engagement that is more comparable across groups and easier to analyze, while the slight differences in retention remain the key point for further statistical testing."""
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## A/B Testing""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Metrics under test

    - Primary: `retention_7` (long-term retention; binary).
    - Secondary: `retention_1` (short-term retention; binary) and `sum_gamerounds` (engagement; continuous, analyzed on the winsorized data you created).

    ### Hypotheses

    All tests are two-sided (we don’t assume which gate is better a priori).

    1. Day-7 retention (primary)
        - $H_0$: $p_{40} = p_{30}$
        - $H_1$: $p_{40} \ne p_{30}$ where $p_{g}$ is the probability of retention for group $g\in{30,40}$.
    2. Day-1 retention (secondary)
        - $H_0$: $p_{40} = p_{30}$
        - $H_1$: $p_{40} \ne p_{30}$
    3. Engagement (winsorized `sum_gamerounds`)
        - $H_0$: $\mu_{40} = \mu_{30}$
        - $H_1$: $\mu_{40} \ne \mu_{30}$ where $\mu_g$ is the mean rounds for group $g$.

    ### Tests & Why These Choices

    1. Retention metrics (binary)
    Use a two-sample test of proportions (asymptotic z-test) or equivalently a 2x2 chi-square test. With around 90k users, the normal approximation is excellent. Report:
        - Effect size: risk difference $\Delta = p_{40}-p_{30}$, relative lift $p_{40}/p_{30}-1$, and optionally the odds ratio.
        - Uncertainty: Wald or Newcombe CIs for $\Delta$.
    2. Engagement (continuous, skewed)
    On the winsorized data, use Welch’s t-test (allows unequal variances observed earlier). Also report a non-parametric check (Mann–Whitney U) to confirm robustness. Provide:
        - Effect size: mean difference $\mu_{40}-\mu_{30}$ with 95% CI, and Cliff’s delta or the Hodges–Lehmann median difference for robustness.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### `retention_7`""")
    return


@app.cell
def _(df, math, np, sm):
    # Counts of successes and totals
    successes_7 = np.array(
        [
            df.loc[df["version"] == "gate_30", "retention_7"].sum(),
            df.loc[df["version"] == "gate_40", "retention_7"].sum(),
        ]
    )
    totals = np.array(
        [(df["version"] == "gate_30").sum(), (df["version"] == "gate_40").sum()]
    )

    # Two-proportion z-test
    zstat_7, pval_7 = sm.stats.proportions_ztest(successes_7, totals)
    confint_30_7 = sm.stats.proportion_confint(
        successes_7[0], totals[0], method="normal"
    )
    confint_40_7 = sm.stats.proportion_confint(
        successes_7[1], totals[1], method="normal"
    )

    # Effect sizes
    p_30_7, p_40_7 = successes_7 / totals
    risk_diff_7 = p_40_7 - p_30_7
    relative_lift_7 = p_40_7 / p_30_7 - 1


    def cohens_h(p1, p2):
        # signed difference on arcsine scale
        return 2 * (math.asin(math.sqrt(p1)) - math.asin(math.sqrt(p2)))


    h_7 = abs(cohens_h(p_40_7, p_30_7))  # <- report magnitude

    print("Retention_7 A/B Test (gate_30 vs gate_40)")
    print("-" * 60)
    print(
        f"gate_30: {successes_7[0]} / {totals[0]} = {p_30_7:.3%} "
        f"(95% CI: {confint_30_7[0]:.3%} – {confint_30_7[1]:.3%})"
    )
    print(
        f"gate_40: {successes_7[1]} / {totals[1]} = {p_40_7:.3%} "
        f"(95% CI: {confint_40_7[0]:.3%} – {confint_40_7[1]:.3%})"
    )
    print()
    print(f"Risk difference (gate_40 - gate_30): {risk_diff_7:.3%}")
    print(f"Relative lift: {relative_lift_7:.2%}")
    print(f"Cohen's h: {h_7:.3f} (~0.2 small, ~0.5 medium, ~0.8 large)")
    print()
    print(f"Z-statistic = {zstat_7:.3f}, p-value = {pval_7:.4g}")
    if pval_7 < 0.05:
        print("Result: Statistically significant difference in 7-day retention.")
    else:
        print(
            "Result: No statistically significant difference in 7-day retention."
        )
    return cohens_h, totals


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    - The negative risk difference and relative lift show that retention is lower when the gate is moved to level 40, suggesting that players are slightly less likely to return after a week.
    - The result is statistically significant, meaning the drop is unlikely to be due to random variation in assignment.
    - However, the effect size is very small (h = 0.021), so in behavioral terms, the change has little practical impact.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### `retention_1`""")
    return


@app.cell
def _(cohens_h, df, np, sm, totals):
    # Counts of successes and totals
    successes_1 = np.array(
        [
            df.loc[df["version"] == "gate_30", "retention_1"].sum(),
            df.loc[df["version"] == "gate_40", "retention_1"].sum(),
        ]
    )

    # Two-proportion z-test
    zstat_1, pval_1 = sm.stats.proportions_ztest(successes_1, totals)
    confint_30_1 = sm.stats.proportion_confint(
        successes_1[0], totals[0], method="normal"
    )
    confint_40_1 = sm.stats.proportion_confint(
        successes_1[1], totals[1], method="normal"
    )

    # Effect sizes
    p_30_1, p_40_1 = successes_1 / totals
    risk_diff_1 = p_40_1 - p_30_1
    relative_lift_1 = p_40_1 / p_30_1 - 1

    h_1 = abs(cohens_h(p_40_1, p_30_1))  # <- report magnitude

    print("Retention_1 A/B Test (gate_30 vs gate_40)")
    print("-" * 60)
    print(
        f"gate_30: {successes_1[0]} / {totals[0]} = {p_30_1:.3%} "
        f"(95% CI: {confint_30_1[0]:.3%} – {confint_30_1[1]:.3%})"
    )
    print(
        f"gate_40: {successes_1[1]} / {totals[1]} = {p_40_1:.3%} "
        f"(95% CI: {confint_40_1[0]:.3%} – {confint_40_1[1]:.3%})"
    )
    print()
    print(f"Risk difference (gate_40 - gate_30): {risk_diff_1:.3%}")
    print(f"Relative lift: {relative_lift_1:.2%}")
    print(f"Cohen's h: {h_1:.3f} (~0.2 small, ~0.5 medium, ~0.8 large)")
    print()
    print(f"Z-statistic = {zstat_1:.3f}, p-value = {pval_1:.4g}")
    if pval_1 < 0.05:
        print("Result: Statistically significant difference in 1-day retention.")
    else:
        print(
            "Result: No statistically significant difference in 1-day retention."
        )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""The day-1 retention difference between groups is small and not statistically significant, meaning we cannot rule out random variation as the cause. Even if real, the effect is tiny in magnitude and unlikely to have meaningful business impact."""
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### `sum_gamerounds`""")
    return


@app.cell
def _(df_winsor, np, sm, stats):
    # Split groups
    g30 = df_winsor.loc[df_winsor["version"] == "gate_30", "sum_gamerounds"]
    g40 = df_winsor.loc[df_winsor["version"] == "gate_40", "sum_gamerounds"]

    # Welch’s t-test (from statsmodels)
    tstat, pval_t, dfree = sm.stats.ttest_ind(g30, g40, usevar="unequal")

    # Mann–Whitney U test (non-parametric, insensitive to normality assumption)
    u_stat, pval_u = stats.mannwhitneyu(g30, g40, alternative="two-sided")

    # Summary stats
    mean30, mean40 = g30.mean(), g40.mean()
    median30, median40 = g30.median(), g40.median()
    std30, std40 = g30.std(), g40.std()

    # Effect size: Cohen’s d (Welch version)
    nx, ny = len(g30), len(g40)
    pooled_sd = np.sqrt(((std30**2) / nx + (std40**2) / ny))
    cohen_d = (mean40 - mean30) / pooled_sd

    print("Sum_gamerounds A/B Test (gate_30 vs gate_40)")
    print("-" * 60)
    print(
        f"gate_30: mean={mean30:.3f}, median={median30}, std={std30:.3f}, n={nx}"
    )
    print(
        f"gate_40: mean={mean40:.3f}, median={median40}, std={std40:.3f}, n={ny}"
    )
    print()
    print(f"Mean difference (gate_40 - gate_30): {mean40 - mean30:.3f}")
    print(f"Cohen's d: {cohen_d:.3f} (~0.2 small, ~0.5 medium, ~0.8 large)")
    print()
    print(
        f"Welch’s t-test: t = {tstat:.3f}, df = {dfree:.1f}, p-value = {pval_t:.4g}"
    )
    print(f"Mann–Whitney U test: U = {u_stat:.0f}, p-value = {pval_u:.4g}")
    if pval_t < 0.05 or pval_u < 0.05:
        print(
            "Result: Statistically significant difference in average game rounds."
        )
    else:
        print(
            "Result: No statistically significant difference in average game rounds."
        )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    - Descriptives: Both groups play about the same number of rounds on average (49.1 vs. 48.8) and have nearly identical medians (17 vs. 16). Standard deviations are also very close (~84), showing no meaningful dispersion difference after winsorization.
    - Welch’s t-test: The mean difference of –0.29 rounds is tiny and not statistically significant ($p \approx 0.60$). On the level of means, there is no evidence that gate placement affects engagement.
    - Mann–Whitney U: The U test finds a marginally significant difference ($p \approx 0.047$), but given the huge sample size, even trivial distributional shifts can become significant. The estimated effect size is negligible.
    - Interpretation: Taken together, the evidence suggests no practically meaningful difference in engagement between gate_30 and gate_40. The apparent “significance” from U test is likely an artifact of sample size and rounding/ties, not a signal of real behavioral change.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Analysis and Conclusion

    Across all three metrics, the experiment shows that moving the progression gate from level 30 to level 40 does not improve player outcomes.

    - `retention_7` (primary metric): Players in the gate_40 group had lower 7-day retention (18.2% vs. 19.0%), a small but statistically significant decline. Even though the effect size is tiny, at scale this could mean thousands fewer returning players.
    - `retention_1`: The day-1 retention difference (44.2% vs. 44.8%) was small and not statistically significant, indicating no clear effect on short-term engagement.
    - `sum_gamerounds`: Both groups played nearly the same number of rounds (means ~49), with no practically meaningful difference after handling outliers.

    Conclusion: Shifting the gate later in progression slightly reduces long-term retention while leaving short-term retention and engagement unchanged. From a business perspective, **the reasonable choice is to keep the gate at level 30**.

    A possible explanation is that players who encounter the gate earlier (level 30) get an earlier “milestone moment” that anchors commitment and motivates continued play. Delaying that milestone to level 40 may make the early game feel less structured, reducing the likelihood of returning after the novelty wears off. Another interpretation is that the later gate reduces friction too much, so players churn naturally before ever reaching it. This is known as the Hedonic adaptation in behavioral science.
    """
    )
    return


if __name__ == "__main__":
    app.run()
