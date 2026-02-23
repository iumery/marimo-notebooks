import marimo

__generated_with = "0.19.11"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import pandas as pd
    import numpy as np
    import pyreadr

    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import roc_auc_score

    import plotly.express as px
    import plotly.graph_objects as go

    return (
        RandomForestClassifier,
        np,
        pd,
        px,
        pyreadr,
        roc_auc_score,
        train_test_split,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Load datasets.
    """)
    return


@app.cell
def _(mo, pd, pyreadr):
    train_file = str(mo.notebook_location() / "public" / "train.rds")
    df: pd.DataFrame = pyreadr.read_r(train_file)[None]
    test_file = str(mo.notebook_location() / "public" / "test.rds")
    df_test: pd.DataFrame = pyreadr.read_r(test_file)[None]
    return df, df_test


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Validate if training and testing datasets are similar.
    """)
    return


@app.cell
def _(
    RandomForestClassifier,
    df: "pd.DataFrame",
    df_test: "pd.DataFrame",
    pd,
    roc_auc_score,
    train_test_split,
):
    def adversarial_validation(
        train_df, test_df, target_col, return_feature_importance
    ):
        """
        Checks if train and test data come from the same distribution.

        Args:
            train_df: Your training dataframe
            test_df: Your test dataframe
            target_col: The name of your regression target column to exclude
        """

        train_adv = train_df.copy()
        test_adv = test_df.copy()

        # Drop the regression target from train
        if target_col in train_adv.columns:
            train_adv = train_adv.drop(columns=[target_col])

        train_adv["is_test"] = 0
        test_adv["is_test"] = 1

        combined_data = pd.concat([train_adv, test_adv], axis=0).reset_index(
            drop=True
        )
        X = combined_data.drop(columns=["is_test"])
        y = combined_data["is_test"]

        # Train the Classifier
        X_train, X_val, y_train, y_val = train_test_split(
            X, y, test_size=0.3, stratify=y
        )

        clf = RandomForestClassifier(n_estimators=50, max_depth=5)
        clf.fit(X_train, y_train)

        # Predict the PROBABILITY of a row being in the Test set
        probs = clf.predict_proba(X_val)[:, 1]
        auc_score = roc_auc_score(y_val, probs)

        print(f"---------------------------------------")
        print(f"Adversarial Validation AUC Score: {auc_score:.4f}")
        print(f"---------------------------------------")

        # Interpret Results
        if auc_score > 0.70:
            print(
                "DANGER: Strong drift detected. Train and Test are very different."
            )
        elif auc_score > 0.60:
            print("WARNING: Moderate drift detected.")
        else:
            print("PASS: Train and Test distributions look similar.")

        # Feature Importance
        feature_imp = pd.DataFrame(
            {"Feature": X.columns, "Importance": clf.feature_importances_}
        ).sort_values("Importance", ascending=False)

        print("\nTop features helping the model distinguish Train from Test:")
        print(feature_imp.head(5))

        if return_feature_importance:
            return feature_imp
        return


    adversarial_validation(df, df_test, "LBDHDD_outcome", False)
    return


@app.cell
def _(np, pd):
    # -------------------------
    # Config
    # -------------------------
    TARGET: str = "LBDHDD_outcome"
    CAT_UNIQUE_MAX: int = (
        30  # "categorical-like" threshold (same idea as your schema)
    )
    TOPK: int = 20  # show top-k features/bars in some plots


    # -------------------------
    # Helpers
    # -------------------------
    def split_cols_by_cardinality(
        df_train: pd.DataFrame,
        target: str,
        cat_unique_max: int = 30,
    ) -> tuple[list[str], list[str], pd.Series]:
        X = df_train.drop(columns=[target], errors="ignore")
        nunique = X.nunique(dropna=False)
        cat_cols = [c for c in X.columns if 2 <= int(nunique[c]) <= cat_unique_max]
        num_cols = [c for c in X.columns if c not in cat_cols]
        return num_cols, cat_cols, nunique


    def numeric_drift_table(
        df_train: pd.DataFrame,
        df_test: pd.DataFrame,
        num_cols: list[str],
        target: str,
    ) -> pd.DataFrame:
        Xtr = df_train.drop(columns=[target], errors="ignore")
        Xte = df_test.copy()
        rows = []
        for c in num_cols:
            a = pd.to_numeric(Xtr[c], errors="coerce")
            b = pd.to_numeric(Xte[c], errors="coerce")

            # robust summaries
            rows.append(
                {
                    "feature": c,
                    "train_mean": float(np.nanmean(a)),
                    "test_mean": float(np.nanmean(b)),
                    "train_median": float(np.nanmedian(a)),
                    "test_median": float(np.nanmedian(b)),
                    "train_std": float(np.nanstd(a)),
                    "test_std": float(np.nanstd(b)),
                    "train_missing": float(a.isna().mean()),
                    "test_missing": float(b.isna().mean()),
                }
            )
        out = pd.DataFrame(rows)
        # simple drift score: relative median shift (robust) + missing shift
        denom = out["train_std"].replace(0.0, np.nan)
        out["median_zshift"] = (out["test_median"] - out["train_median"]) / denom
        out["missing_shift"] = out["test_missing"] - out["train_missing"]
        out["drift_score"] = (
            out["median_zshift"].abs().fillna(0.0)
            + 2.0 * out["missing_shift"].abs()
        )
        return out.sort_values("drift_score", ascending=False).reset_index(
            drop=True
        )


    def categorical_drift_table(
        df_train: pd.DataFrame,
        df_test: pd.DataFrame,
        cat_cols: list[str],
        target: str,
        topk: int = 8,
    ) -> pd.DataFrame:
        Xtr = df_train.drop(columns=[target], errors="ignore")
        Xte = df_test.copy()

        rows = []
        for c in cat_cols:
            tr = Xtr[c].astype("string")
            te = Xte[c].astype("string")

            tr_v = tr.value_counts(dropna=False, normalize=True)
            te_v = te.value_counts(dropna=False, normalize=True)

            # align on union
            idx = tr_v.index.union(te_v.index)
            p = tr_v.reindex(idx, fill_value=0.0).to_numpy(dtype=float)
            q = te_v.reindex(idx, fill_value=0.0).to_numpy(dtype=float)

            # Total Variation Distance: 0..1
            tv = 0.5 * float(np.abs(p - q).sum())

            # store a few biggest movers
            diff = pd.Series(q - p, index=idx).sort_values(
                key=lambda s: s.abs(), ascending=False
            )
            movers = diff.head(topk)
            movers_str = "; ".join([f"{k}:{v:+.3f}" for k, v in movers.items()])

            rows.append(
                {
                    "feature": c,
                    "train_unique": int(tr_v.shape[0]),
                    "test_unique": int(te_v.shape[0]),
                    "tvd": tv,
                    "top_movers(test-train)": movers_str,
                    "train_missing": float(tr.isna().mean()),
                    "test_missing": float(te.isna().mean()),
                }
            )

        out = (
            pd.DataFrame(rows)
            .sort_values("tvd", ascending=False)
            .reset_index(drop=True)
        )
        return out

    return (
        CAT_UNIQUE_MAX,
        TARGET,
        TOPK,
        categorical_drift_table,
        numeric_drift_table,
        split_cols_by_cardinality,
    )


@app.cell
def _(
    CAT_UNIQUE_MAX: int,
    TARGET: str,
    categorical_drift_table,
    df: "pd.DataFrame",
    df_test: "pd.DataFrame",
    numeric_drift_table,
    split_cols_by_cardinality,
):
    # -------------------------
    # Column split
    # -------------------------
    num_cols, cat_cols, nunique = split_cols_by_cardinality(
        df, TARGET, CAT_UNIQUE_MAX
    )

    print(f"Train shape: {df.shape} | Test shape: {df_test.shape}")
    print(f"Detected num cols: {len(num_cols)} | cat-like cols: {len(cat_cols)}")

    num_drift = numeric_drift_table(
        df,
        df_test,
        num_cols=num_cols,
        target=TARGET,
    )

    cat_drift = categorical_drift_table(
        df,
        df_test,
        cat_cols=cat_cols,
        target=TARGET,
        topk=8,
    )
    return cat_cols, cat_drift, num_cols, num_drift


@app.cell
def _(num_drift):
    num_drift.head(10)
    return


@app.cell
def _(cat_drift):
    cat_drift.head(10)
    return


@app.cell
def _(
    TARGET: str,
    TOPK: int,
    cat_cols,
    cat_drift,
    df: "pd.DataFrame",
    df_test: "pd.DataFrame",
    np,
    num_cols,
    num_drift,
    pd,
    px,
):
    # ============================================================
    # 1) Target distribution
    # ============================================================
    px.histogram(
        df, x=TARGET, nbins=80, title="Target distribution (train)"
    ).show()
    px.ecdf(df, x=TARGET, title="Target ECDF (train)").show()

    fig = px.histogram(df, x=TARGET, nbins=80, title="Target distribution (log y)")
    fig.update_yaxes(type="log")
    fig.show()


    # ============================================================
    # 2) Numeric drift overlays for selected features
    # ============================================================
    drift_num_features: list[str] = num_drift.head(3)["feature"].to_list()

    for feature in drift_num_features:
        train_vals = pd.to_numeric(df[feature], errors="coerce")
        test_vals = pd.to_numeric(df_test[feature], errors="coerce")

        overlay_df = pd.DataFrame(
            {
                "value": pd.concat([train_vals, test_vals], ignore_index=True),
                "split": (["train"] * len(train_vals))
                + (["test"] * len(test_vals)),
            }
        )

        px.histogram(
            overlay_df,
            x="value",
            color="split",
            barmode="overlay",
            nbins=80,
            title=f"Train vs test overlay: {feature}",
        ).show()

        px.box(
            overlay_df,
            x="split",
            y="value",
            title=f"Box plot: {feature} (train vs test)",
            points="outliers",
        ).show()


    # ============================================================
    # 3) Categorical drift: top frequency shifts for a chosen feature
    # ============================================================
    drift_cat_feature: str = cat_drift["feature"][0]

    train_cat = df.drop(columns=[TARGET], errors="ignore")[
        drift_cat_feature
    ].astype("string")
    test_cat = df_test[drift_cat_feature].astype("string")

    train_freq = train_cat.value_counts(dropna=False, normalize=True)
    test_freq = test_cat.value_counts(dropna=False, normalize=True)

    all_levels = train_freq.index.union(test_freq.index)

    freq_df = pd.DataFrame(
        {
            "category": all_levels.astype(str),
            "train_freq": train_freq.reindex(
                all_levels, fill_value=0.0
            ).to_numpy(),
            "test_freq": test_freq.reindex(all_levels, fill_value=0.0).to_numpy(),
        }
    )
    freq_df["abs_diff"] = (freq_df["test_freq"] - freq_df["train_freq"]).abs()

    top_shift_df = freq_df.sort_values("abs_diff", ascending=False).head(20)
    top_shift_long = top_shift_df.melt(
        id_vars=["category"],
        value_vars=["train_freq", "test_freq"],
        var_name="split",
        value_name="freq",
    )

    px.bar(
        top_shift_long,
        x="freq",
        y="category",
        color="split",
        barmode="group",
        orientation="h",
        title=f"Top category frequency shifts (train vs test): {drift_cat_feature}",
    ).show()


    # ============================================================
    # 4) Feature-target quick screens (train only)
    #   - numeric: Spearman correlation + top scatter (LOWESS)
    #   - cat-like: group means variability + top-level means
    # ============================================================
    # ----- Numeric correlations -----
    corr_rows: list[dict[str, object]] = []
    target_series = pd.to_numeric(df[TARGET], errors="coerce")

    for feature in num_cols:
        x = pd.to_numeric(df[feature], errors="coerce")
        ok = ~(x.isna() | target_series.isna())
        if int(ok.sum()) < 50:
            continue
        rho = float(
            pd.Series(x[ok]).corr(pd.Series(target_series[ok]), method="spearman")
        )
        if np.isnan(rho):
            continue
        corr_rows.append(
            {
                "feature": feature,
                "spearman_rho": rho,
                "abs_rho": abs(rho),
                "n": int(ok.sum()),
            }
        )

    corr_df = (
        pd.DataFrame(corr_rows)
        .sort_values("abs_rho", ascending=False)
        .reset_index(drop=True)
    )

    if len(corr_df):
        px.bar(
            corr_df.head(TOPK),
            x="spearman_rho",
            y="feature",
            orientation="h",
            title=f"Top {TOPK} numeric features by |Spearman rho| with target",
            hover_data=["abs_rho", "n"],
        ).show()

        best_num_feature = str(corr_df.loc[0, "feature"])
        px.scatter(
            df,
            x=best_num_feature,
            y=TARGET,
            trendline="lowess",
            title=f"Target vs numeric feature: {best_num_feature} (LOWESS trend)",
        ).show()


    # ----- Cat-like group effects -----
    cat_rows: list[dict[str, object]] = []

    for feature in cat_cols:
        vc = df[feature].value_counts(dropna=False)
        if vc.shape[0] < 2:
            continue

        group_stats = (
            df.groupby(feature, dropna=False)[TARGET]
            .agg(["mean", "size"])
            .reset_index()
        )
        weights = group_stats["size"].to_numpy(dtype=float)
        means = group_stats["mean"].to_numpy(dtype=float)

        mean_bar = float(np.average(means, weights=weights))
        effect = float(
            np.sqrt(np.average((means - mean_bar) ** 2, weights=weights))
        )

        cat_rows.append(
            {
                "feature": feature,
                "group_mean_std": effect,
                "n_levels": int(vc.shape[0]),
            }
        )

    cat_assoc_df = (
        pd.DataFrame(cat_rows)
        .sort_values("group_mean_std", ascending=False)
        .reset_index(drop=True)
    )

    if len(cat_assoc_df):
        px.bar(
            cat_assoc_df.head(TOPK),
            x="group_mean_std",
            y="feature",
            orientation="h",
            title=f"Top {TOPK} cat-like features by variability of target across groups",
            hover_data=["n_levels"],
        ).show()

        best_cat_feature = str(cat_assoc_df.loc[0, "feature"])
        top_levels_df = (
            df.groupby(best_cat_feature, dropna=False)[TARGET]
            .agg(["mean", "size"])
            .reset_index()
        )
        top_levels_df = top_levels_df.sort_values("size", ascending=False).head(25)
        top_levels_df[best_cat_feature] = top_levels_df[best_cat_feature].astype(
            str
        )

        px.bar(
            top_levels_df,
            x="mean",
            y=best_cat_feature,
            orientation="h",
            title=f"Target mean by top levels (by count): {best_cat_feature}",
            hover_data=["size"],
        ).show()


    # ============================================================
    # 5) Simple interaction heatmap (two top numeric features)
    # ============================================================
    if len(num_cols) >= 2:
        if len(corr_df) >= 2:
            f1, f2 = str(corr_df.loc[0, "feature"]), str(corr_df.loc[1, "feature"])
        else:
            f1, f2 = str(num_cols[0]), str(num_cols[1])

        heat_df = df[[f1, f2, TARGET]].copy()
        heat_df[f1] = pd.to_numeric(heat_df[f1], errors="coerce")
        heat_df[f2] = pd.to_numeric(heat_df[f2], errors="coerce")
        heat_df[TARGET] = pd.to_numeric(heat_df[TARGET], errors="coerce")
        heat_df = heat_df.dropna(subset=[f1, f2, TARGET])

        if len(heat_df) > 200:
            q = 20
            heat_df["b1"] = pd.qcut(heat_df[f1], q=q, duplicates="drop")
            heat_df["b2"] = pd.qcut(heat_df[f2], q=q, duplicates="drop")

            grid_df = (
                heat_df.groupby(["b1", "b2"], observed=True)[TARGET]
                .mean()
                .reset_index()
            )
            pivot_df = grid_df.pivot(index="b1", columns="b2", values=TARGET)

            fig = px.imshow(
                pivot_df.to_numpy(),
                aspect="auto",
                title=f"Interaction heatmap: mean(target) over quantile bins ({f1} x {f2})",
            )
            fig.update_xaxes(title=f"{f2} bins")
            fig.update_yaxes(title=f"{f1} bins")
            fig.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Summary of findings from the EDA plots

    ### Target distribution (train)
    - The target `LBDHDD_outcome` is roughly bell-shaped, concentrated around the mid-range (about the 50s).
    - The tails are relatively sparse (few very low or very high outcomes).
    - The ECDF shows most probability mass accumulates quickly in the middle range, confirming limited tail coverage.
    - The log-count histogram highlights how rare extreme target values are compared to the center.

    ### Train vs test drift (numeric features: `DR1TCALC`, `DR1TVC`, `DR1TNUMF`)
    - These features show noticeable distribution shift between train and test.
    - In all three cases, the test set tends to be shifted toward higher values than train (higher central tendency).
    - The box plots suggest differences in spread and outliers as well, not just a simple mean shift.
    - Implication: even if CV on train looks stable, inference on test may face mild covariate shift, which can contribute to systematic prediction bias.

    ### Train vs test drift (categorical feature: `ALQ121`)
    - `ALQ121` exhibits clear category frequency changes between train and test.
    - Some categories become more common in test while others become less common, indicating a changed mixture of groups.
    - Rare categories exist and may appear in only one split (or be extremely uncommon).
    - Implication: category mix shift can affect generalization, especially if certain categories are underrepresented in train.

    ### Numeric feature-target association (Spearman correlation ranking)
    - The strongest marginal relationships with the target are negative for `BMXWAIST` and `BMXBMI`.
    - Several diet-related features have smaller to moderate correlations (some positive), but are weaker than waist/BMI.
    - Interpretation: body composition variables appear to be primary drivers of the target signal.

    ### Shape of relationship (scatter + LOWESS: `BMXWAIST` vs target)
    - There is a clear negative trend: higher waist is associated with lower `LBDHDD_outcome`.
    - The LOWESS curve suggests mild nonlinearity (not perfectly linear).
    - There is still substantial scatter around the trend, meaning waist alone does not fully explain the target.

    ### Categorical feature-target association (group mean variability ranking)
    - `RIAGENDR` stands out as the categorical-like feature with the largest between-group differences in target mean.
    - `ALQ121` also shows meaningful group-level variation, consistent with it being both predictive and drift-prone.

    ### Group mean plot (`RIAGENDR`)
    - `RIAGENDR` has a large separation in mean target across its main levels (one group noticeably higher than the other).
    - This is a large effect relative to typical RMSE scale, so it is likely an important predictor and/or interaction term.

    ### Interaction structure (heatmap: `BMXWAIST` x `BMXBMI`)
    - The heatmap shows a coherent gradient: higher BMI and higher waist together correspond to lower mean target.
    - Sparse regions (blank cells) appear in extreme combinations, suggesting limited data support there.
    - Implication: the model will likely perform best in the dense “typical” region and be less reliable at extreme BMI/waist combinations, which aligns with tail prediction difficulties.
    """)
    return


@app.cell
def _(df: "pd.DataFrame", df_test: "pd.DataFrame", np, pd):
    # ============================================================
    # Feature engineering pipeline (train/test) for your project
    # - Works starting from: df (train), df_test (test) already loaded
    # - Implements:
    #   1) Drop constant columns (train-derived)
    #   2) Inflated-mode indicators (train-derived)
    #   3) Split "cat-like" vs numeric by cardinality (train-derived)
    #   4) Feature engineering:
    #        - Body composition combos (waist/bmi): ratios, interactions, bins
    #        - Group-aware centering by RIAGENDR (target-free)
    #        - Diet aggregates + per-kcal densities (auto-detect DR1T* vars)
    #        - Heavy-tail clipping (winsorize) for numeric vars (train-derived)
    #        - Rank-percent features for numeric vars (train-derived)
    #        - Extreme flags (p05/p95) for numeric vars (train-derived)
    #        - Categorical rare-level bucketing + frequency encoding (train-derived)
    #   5) Preprocessing for modeling:
    #        - Numeric: log1p -> RobustScaler
    #        - Cat-like: keep as integer categories (for CatBoost), plus engineered cat bins
    #
    # Notes:
    # - Everything uses TRAIN-derived stats/thresholds to avoid leakage.
    # - No missingness checks (as you requested).
    # - Uses built-in generics for type annotations (dict/list/tuple).
    # ============================================================

    from dataclasses import dataclass
    from sklearn.preprocessing import RobustScaler

    EPS: float = 1e-9


    @dataclass
    class FEConfig:
        target: str = "LBDHDD_outcome"
        cat_unique_max: int = 30

        inflated_unique_min: int = 31
        inflated_freq_threshold: float = 0.30

        clip_lo: float = 0.01
        clip_hi: float = 0.99
        extreme_lo: float = 0.05
        extreme_hi: float = 0.95

        qbins_waist: int = 10
        qbins_bmi: int = 10

        rare_level_min_frac: float = 0.01
        add_rank_pct: bool = True

        diet_prefix: str = "DR1T"
        diet_kcal_col: str = "DR1TCALC"


    @dataclass
    class FEArtifacts:
        const_cols: list[str]
        mode_map: dict[str, object]
        num_cols: list[str]
        cat_cols: list[str]
        final_cols: list[str]

        clip_map: dict[str, tuple[float, float]]
        extreme_map: dict[str, tuple[float, float]]
        rank_ref: dict[str, np.ndarray]

        cat_keep_levels: dict[str, set[str]]
        cat_freq_map: dict[str, dict[str, float]]

        qcut_edges: dict[str, np.ndarray]
        group_medians: dict[str, dict[str, float]]


    # -------------------------
    # Utilities
    # -------------------------
    def _safe_to_numeric(s: pd.Series) -> pd.Series:
        return pd.to_numeric(s, errors="coerce")


    def _winsor_bounds(x: pd.Series, lo: float, hi: float) -> tuple[float, float]:
        arr = x.to_numpy(dtype=float)
        qlo = float(np.nanquantile(arr, lo))
        qhi = float(np.nanquantile(arr, hi))
        return qlo, qhi


    def _compute_rank_ref(x: pd.Series) -> np.ndarray:
        arr = x.to_numpy(dtype=float)
        arr = arr[~np.isnan(arr)]
        arr.sort()
        return arr


    def _rank_pct_from_ref(x: pd.Series, ref_sorted: np.ndarray) -> np.ndarray:
        xv = x.to_numpy(dtype=float)
        out = np.full_like(xv, np.nan, dtype=float)
        if ref_sorted.size == 0:
            return out
        idx = np.searchsorted(ref_sorted, xv, side="left")
        return idx / max(ref_sorted.size, 1)


    def _qcut_edges_train(x: pd.Series, q: int) -> np.ndarray:
        arr = x.to_numpy(dtype=float)
        arr = arr[~np.isnan(arr)]
        if arr.size == 0:
            return np.array([0.0, 1.0], dtype=float)
        qs = np.linspace(0.0, 1.0, q + 1)
        edges = np.quantile(arr, qs)
        edges = np.unique(edges)
        if edges.size < 2:
            edges = np.array([edges[0] - 1.0, edges[0] + 1.0], dtype=float)
        return edges.astype(float)


    def _bin_with_edges(x: pd.Series, edges: np.ndarray) -> pd.Series:
        bins = pd.cut(
            _safe_to_numeric(x),
            bins=edges,
            include_lowest=True,
            right=True,
            labels=False,
        )
        return bins.astype("Int64")


    def _compute_cat_levels_and_freq(
        s: pd.Series, min_frac: float
    ) -> tuple[set[str], dict[str, float]]:
        ss = s.astype("string").fillna("__NA__")
        vc = ss.value_counts(normalize=True, dropna=False)
        keep = set(vc[vc >= min_frac].index.astype(str).tolist())
        if "__NA__" in vc.index.astype(str).tolist():
            keep.add("__NA__")
        freq_map = {str(k): float(v) for k, v in vc.items()}
        return keep, freq_map


    def _make_cat_other(s: pd.Series, keep: set[str]) -> pd.Series:
        ss = s.astype("string").fillna("__NA__")
        return ss.where(ss.isin(list(keep)), "__OTHER__")


    def _clean_numeric_for_log1p(
        Xdf: pd.DataFrame,
        cols: list[str],
        *,
        treat_le_minus1_as_nan: bool = True,
        clip_nonneg: bool = True,
    ) -> np.ndarray:
        X = Xdf[cols].apply(pd.to_numeric, errors="coerce").to_numpy(dtype=float)
        X[~np.isfinite(X)] = np.nan
        if treat_le_minus1_as_nan:
            X[X <= -1.0] = np.nan
        if clip_nonneg:
            X = np.clip(X, 0.0, None)
        return np.log1p(X)


    def _impute_with_train_median(
        X_train: np.ndarray,
        X_other: np.ndarray,
    ) -> tuple[np.ndarray, np.ndarray]:
        med = np.nanmedian(X_train, axis=0)
        med = np.where(np.isfinite(med), med, 0.0)
        Xtr = np.where(np.isnan(X_train), med, X_train)
        Xot = np.where(np.isnan(X_other), med, X_other)
        return Xtr, Xot


    def _dedupe_columns(X: pd.DataFrame) -> pd.DataFrame:
        # If you have duplicate column names, keep the first occurrence.
        if X.columns.duplicated().any():
            X = X.loc[:, ~X.columns.duplicated()].copy()
        return X


    def _infer_cat_num_cols_for_catboost(X: pd.DataFrame) -> tuple[list[str], list[str]]:
        """
        After FE, infer CatBoost categorical columns.
        Safe against duplicate names (but we dedupe anyway).
        """
        cat_cols: list[str] = []
        for c in X.columns:
            col_obj = X[c]
            # If duplicates exist, X[c] can be a DataFrame; take first column
            if isinstance(col_obj, pd.DataFrame):
                col_obj = col_obj.iloc[:, 0]
            dt = col_obj.dtype

            if (str(dt) == "string") or (dt == object) or c.endswith("__qbin") or c.endswith("__qbin2d"):
                cat_cols.append(c)

        num_cols = [c for c in X.columns if c not in cat_cols]
        return num_cols, cat_cols


    # -------------------------
    # Fit artifacts on train
    # -------------------------
    def fit_feature_pipeline(df_train: pd.DataFrame, cfg: FEConfig) -> FEArtifacts:
        X_raw = df_train.drop(columns=[cfg.target], errors="ignore").copy()
        n = len(X_raw)

        nunique = X_raw.nunique(dropna=False)
        const_cols = nunique[nunique <= 1].index.tolist()
        X0 = X_raw.drop(columns=const_cols).copy()

        mode_map: dict[str, object] = {}
        for col in X0.columns:
            u = int(X0[col].nunique(dropna=False))
            if u >= cfg.inflated_unique_min:
                vc = X0[col].value_counts(dropna=False)
                mode_val = vc.index[0]
                mode_freq = float(vc.iloc[0] / max(n, 1))
                if mode_freq >= cfg.inflated_freq_threshold:
                    mode_map[col] = mode_val

        X_base = X0.copy()
        for col, mv in mode_map.items():
            X_base[f"{col}__is_mode"] = (X_base[col].to_numpy() == mv).astype(np.int8)

        nunique2 = X_base.nunique(dropna=False)
        cat_cols = [
            c
            for c in X_base.columns
            if (not c.endswith("__is_mode"))
            and (2 <= int(nunique2[c]) <= cfg.cat_unique_max)
        ]
        num_cols = [c for c in X_base.columns if c not in cat_cols]

        final_cols = num_cols + cat_cols
        X_base = X_base.reindex(columns=final_cols)

        clip_map: dict[str, tuple[float, float]] = {}
        extreme_map: dict[str, tuple[float, float]] = {}
        rank_ref: dict[str, np.ndarray] = {}

        for c in num_cols:
            xc = _safe_to_numeric(X_base[c])
            qlo, qhi = _winsor_bounds(xc, cfg.clip_lo, cfg.clip_hi)
            clip_map[c] = (qlo, qhi)

            lo = float(np.nanquantile(xc.to_numpy(dtype=float), cfg.extreme_lo))
            hi = float(np.nanquantile(xc.to_numpy(dtype=float), cfg.extreme_hi))
            extreme_map[c] = (lo, hi)

            if cfg.add_rank_pct:
                rank_ref[c] = _compute_rank_ref(xc)

        cat_keep_levels: dict[str, set[str]] = {}
        cat_freq_map: dict[str, dict[str, float]] = {}
        for c in cat_cols:
            keep, fmap = _compute_cat_levels_and_freq(X_base[c], cfg.rare_level_min_frac)
            cat_keep_levels[c] = keep
            cat_freq_map[c] = fmap

        qcut_edges: dict[str, np.ndarray] = {}
        for key in ["BMXWAIST", "BMXBMI"]:
            if key in X_base.columns:
                q = cfg.qbins_waist if key == "BMXWAIST" else cfg.qbins_bmi
                qcut_edges[key] = _qcut_edges_train(_safe_to_numeric(X_base[key]), q=q)

        group_medians: dict[str, dict[str, float]] = {}
        if "RIAGENDR" in X_base.columns:
            gcol = X_base["RIAGENDR"].astype("string").fillna("__NA__")
            for feat in ["BMXWAIST", "BMXBMI"]:
                if feat in X_base.columns:
                    tmp = pd.DataFrame({"g": gcol, "x": _safe_to_numeric(X_base[feat])})
                    med = tmp.groupby("g", dropna=False)["x"].median()
                    group_medians[feat] = {str(k): float(v) for k, v in med.items()}

        return FEArtifacts(
            const_cols=const_cols,
            mode_map=mode_map,
            num_cols=num_cols,
            cat_cols=cat_cols,
            final_cols=final_cols,
            clip_map=clip_map,
            extreme_map=extreme_map,
            rank_ref=rank_ref,
            cat_keep_levels=cat_keep_levels,
            cat_freq_map=cat_freq_map,
            qcut_edges=qcut_edges,
            group_medians=group_medians,
        )


    # -------------------------
    # Transform df -> engineered features
    # -------------------------
    def transform_features(df_any: pd.DataFrame, artifacts: FEArtifacts, cfg: FEConfig) -> pd.DataFrame:
        X = df_any.drop(columns=[cfg.target], errors="ignore").copy()
        X = X.drop(columns=artifacts.const_cols, errors="ignore").copy()

        # align base cols (prevents mismatch)
        X = X.reindex(columns=artifacts.final_cols)

        # winsorize base numeric
        for c in artifacts.num_cols:
            lo, hi = artifacts.clip_map[c]
            X[c] = _safe_to_numeric(X[c]).clip(lower=lo, upper=hi)

        new_cols: dict[str, object] = {}

        # inflated-mode indicators
        for col, mv in artifacts.mode_map.items():
            if col in X.columns:
                new_cols[f"{col}__is_mode"] = (X[col].to_numpy() == mv).astype(np.int8)
            else:
                new_cols[f"{col}__is_mode"] = np.zeros(len(X), dtype=np.int8)

        # extreme flags
        for c in artifacts.num_cols:
            lo, hi = artifacts.extreme_map[c]
            xv = _safe_to_numeric(X[c]).to_numpy(dtype=float)
            new_cols[f"{c}__is_extreme"] = ((xv <= lo) | (xv >= hi)).astype(np.int8)

        # rank pct
        if cfg.add_rank_pct:
            for c in artifacts.num_cols:
                ref = artifacts.rank_ref.get(c)
                if ref is not None:
                    new_cols[f"{c}__rank_pct"] = _rank_pct_from_ref(_safe_to_numeric(X[c]), ref)

        # waist/bmi combos + bins (bins as string cats)
        if ("BMXWAIST" in X.columns) and ("BMXBMI" in X.columns):
            waist = _safe_to_numeric(X["BMXWAIST"]).to_numpy(dtype=float)
            bmi = _safe_to_numeric(X["BMXBMI"]).to_numpy(dtype=float)

            new_cols["BMXWAIST__sq"] = waist**2
            new_cols["BMXBMI__sq"] = bmi**2
            new_cols["BMXWAIST_x_BMXBMI"] = waist * bmi
            new_cols["BMXWAIST_over_BMXBMI"] = waist / (bmi + EPS)

            ew = artifacts.qcut_edges.get("BMXWAIST")
            eb = artifacts.qcut_edges.get("BMXBMI")
            if (ew is not None) and (eb is not None):
                bw = _bin_with_edges(X["BMXWAIST"], ew).astype("string").fillna("__NA__")
                bb = _bin_with_edges(X["BMXBMI"], eb).astype("string").fillna("__NA__")
                new_cols["BMXWAIST__qbin"] = bw
                new_cols["BMXBMI__qbin"] = bb
                new_cols["BMXWAIST_BMXBMI__qbin2d"] = bw + "_" + bb

        # centering by RIAGENDR
        if ("RIAGENDR" in X.columns) and artifacts.group_medians:
            g = X["RIAGENDR"].astype("string").fillna("__NA__")
            for feat, medmap in artifacts.group_medians.items():
                if feat in X.columns:
                    xm = _safe_to_numeric(X[feat]).to_numpy(dtype=float)
                    med = g.map(lambda k: medmap.get(str(k), np.nan)).to_numpy(dtype=float)
                    new_cols[f"{feat}__center_by_RIAGENDR"] = xm - med

        # diet features
        diet_cols = [c for c in X.columns if c.startswith(cfg.diet_prefix)]
        kcal_col = cfg.diet_kcal_col if cfg.diet_kcal_col in X.columns else None

        macro_candidates = ["DR1TCARB", "DR1TPROT", "DR1TTFAT"]
        have_macros = [c for c in macro_candidates if c in X.columns]
        if len(have_macros) >= 2:
            macro_total = np.zeros(len(X), dtype=float)
            for c in have_macros:
                macro_total += _safe_to_numeric(X[c]).to_numpy(dtype=float)
            new_cols["DR1T__macro_total"] = macro_total
            for c in have_macros:
                new_cols[f"{c}__share_of_macro_total"] = _safe_to_numeric(X[c]).to_numpy(dtype=float) / (macro_total + EPS)

        if kcal_col is not None:
            kcal = _safe_to_numeric(X[kcal_col]).to_numpy(dtype=float)
            for c in diet_cols:
                if c == kcal_col:
                    continue
                xv = _safe_to_numeric(X[c]).to_numpy(dtype=float)
                new_cols[f"{c}__per_kcal"] = xv / (kcal + EPS)
            new_cols["DR1TCALC__is_zero_or_nan"] = (np.isnan(kcal) | (kcal <= 0)).astype(np.int8)

        # categorical bucketing + freq encoding (overwrite base cat col is OK)
        for c in artifacts.cat_cols:
            keep = artifacts.cat_keep_levels.get(c)
            fmap = artifacts.cat_freq_map.get(c)
            if keep is None or fmap is None:
                continue
            s = _make_cat_other(X[c], keep).astype("string").fillna("__NA__")
            X[c] = s
            new_cols[f"{c}__freq"] = s.map(lambda v: fmap.get(str(v), 0.0)).astype(float)

        if new_cols:
            X = pd.concat([X, pd.DataFrame(new_cols, index=X.index)], axis=1)

        # CRITICAL: remove any accidental duplicate names
        X = _dedupe_columns(X)
        return X


    # -------------------------
    # CatBoost matrices (numeric scaled + cat strings)
    # -------------------------
    def make_catboost_matrices(
        X_tr_df: pd.DataFrame,
        X_va_df: pd.DataFrame,
        num_cols: list[str],
        cat_cols: list[str],
    ) -> tuple[pd.DataFrame, pd.DataFrame, list[int]]:
        # numeric
        Xtr_num = _clean_numeric_for_log1p(X_tr_df, num_cols, treat_le_minus1_as_nan=True, clip_nonneg=True)
        Xva_num = _clean_numeric_for_log1p(X_va_df, num_cols, treat_le_minus1_as_nan=True, clip_nonneg=True)

        Xtr_num, Xva_num = _impute_with_train_median(Xtr_num, Xva_num)

        scaler = RobustScaler().fit(Xtr_num)
        Xtr_num_t = scaler.transform(Xtr_num)
        Xva_num_t = scaler.transform(Xva_num)

        Xtr_num_df = pd.DataFrame(Xtr_num_t, columns=num_cols, index=X_tr_df.index)
        Xva_num_df = pd.DataFrame(Xva_num_t, columns=num_cols, index=X_va_df.index)

        # cats
        Xtr_cat = X_tr_df[cat_cols].copy()
        Xva_cat = X_va_df[cat_cols].copy()
        for c in cat_cols:
            Xtr_cat[c] = Xtr_cat[c].astype("string").fillna("__NA__")
            Xva_cat[c] = Xva_cat[c].astype("string").fillna("__NA__")

        Xtr = pd.concat([Xtr_num_df, Xtr_cat], axis=1)
        Xva = pd.concat([Xva_num_df, Xva_cat], axis=1)

        cat_idx = [Xtr.columns.get_loc(c) for c in cat_cols]
        return Xtr, Xva, cat_idx


    # -------------------------
    # End-to-end
    # -------------------------
    def build_pipeline_outputs(
        df: pd.DataFrame,
        df_test: pd.DataFrame,
        cfg: FEConfig,
    ) -> tuple[pd.DataFrame, np.ndarray, pd.DataFrame, list[int], FEArtifacts]:
        artifacts = fit_feature_pipeline(df, cfg)
        y = df[cfg.target].to_numpy(dtype=float)

        X_train_fe = transform_features(df, artifacts, cfg)
        X_test_fe = transform_features(df_test, artifacts, cfg)

        # align columns exactly
        X_test_fe = X_test_fe.reindex(columns=X_train_fe.columns)

        # recompute cat/num based on engineered dtypes (the bug fix)
        num_cols_cb, cat_cols_cb = _infer_cat_num_cols_for_catboost(X_train_fe)

        Xtr_cb, Xte_cb, cat_idx = make_catboost_matrices(
            X_train_fe,
            X_test_fe,
            num_cols_cb,
            cat_cols_cb,
        )

        # keep for debugging downstream
        artifacts.num_cols = num_cols_cb
        artifacts.cat_cols = cat_cols_cb
        artifacts.final_cols = list(X_train_fe.columns)

        return Xtr_cb, y, Xte_cb, cat_idx, artifacts


    # -------------------------
    # Usage
    # -------------------------
    cfg = FEConfig(target="LBDHDD_outcome")
    Xtr_cb, y, Xte_cb, cat_idx, artifacts = build_pipeline_outputs(df, df_test, cfg)
    print(Xtr_cb.shape, Xte_cb.shape, len(cat_idx))
    print("Duplicate columns after FE?", bool(pd.Index(artifacts.final_cols).duplicated().any()))
    return Xtr_cb, cat_idx, y


@app.cell
def _(Xtr_cb, cat_idx, np, pd, px, y):
    from sklearn.model_selection import KFold
    from sklearn.metrics import mean_squared_error
    from catboost import CatBoostRegressor, Pool


    def rmse(y_true: np.ndarray, y_pred: np.ndarray) -> float:
        return float(np.sqrt(mean_squared_error(y_true, y_pred)))


    def run_catboost_cv_oof(
        X: pd.DataFrame,
        y: np.ndarray,
        cat_idx: list[int],
        params: dict,
        *,
        n_splits: int = 5,
        seed: int = 42,
        use_log_target: bool = False,
    ) -> tuple[np.ndarray, np.ndarray, float, float]:
        kf = KFold(n_splits=n_splits, shuffle=True, random_state=seed)
        oof = np.full(shape=(len(y),), fill_value=np.nan, dtype=float)
        fold_scores: list[float] = []

        y_fit = np.log1p(y) if use_log_target else y

        for fold, (tr_idx, va_idx) in enumerate(kf.split(X), start=1):
            X_tr, X_va = X.iloc[tr_idx], X.iloc[va_idx]
            y_tr, y_va = y_fit[tr_idx], y_fit[va_idx]

            tr_pool = Pool(X_tr, y_tr, cat_features=cat_idx)
            va_pool = Pool(X_va, y_va, cat_features=cat_idx)

            model = CatBoostRegressor(**params)
            model.fit(
                tr_pool,
                eval_set=va_pool,
                use_best_model=True,
                verbose=False,
            )

            pred_va = model.predict(X_va).astype(float)
            if use_log_target:
                pred_va = np.expm1(pred_va)

            oof[va_idx] = pred_va
            fold_rmse = rmse(y[va_idx], pred_va)
            fold_scores.append(fold_rmse)
            print(f"Fold {fold}: RMSE={fold_rmse:.6f}")

        mean_s = float(np.mean(fold_scores))
        std_s = float(np.std(fold_scores))
        print(f"CV summary: mean={mean_s:.6f} std={std_s:.6f}")
        return oof, np.array(fold_scores, dtype=float), mean_s, std_s


    def residual_diagnostics(
        y: np.ndarray, pred: np.ndarray, title_prefix: str = ""
    ) -> None:
        resid = y - pred
        dfp = pd.DataFrame({"y": y, "pred": pred, "resid": resid})
        dfp = dfp.replace([np.inf, -np.inf], np.nan).dropna()

        # Residual vs y
        fig1 = px.scatter(
            dfp,
            x="y",
            y="resid",
            title=f"{title_prefix}Residual vs true y",
            opacity=0.6,
        )
        fig1.add_hline(y=0.0)
        fig1.show()

        # Mean residual by y-bin
        dfp["y_bin"] = pd.qcut(dfp["y"], q=12, duplicates="drop")
        gb = (
            dfp.groupby("y_bin", observed=True)
            .agg(
                y_mean=("y", "mean"),
                resid_mean=("resid", "mean"),
                n=("resid", "size"),
            )
            .reset_index(drop=True)
        )

        fig2 = px.line(
            gb,
            x="y_mean",
            y="resid_mean",
            markers=True,
            title=f"{title_prefix}Mean residual by y-bin (target is ~0)",
            hover_data=["n"],
        )
        fig2.add_hline(y=0.0)
        fig2.show()

        # Pred vs y (OOF)
        mn = float(min(dfp["y"].min(), dfp["pred"].min()))
        mx = float(max(dfp["y"].max(), dfp["pred"].max()))
        fig3 = px.scatter(
            dfp,
            x="pred",
            y="y",
            title=f"{title_prefix}OOF pred vs true",
            opacity=0.6,
        )
        fig3.add_shape(type="line", x0=mn, y0=mn, x1=mx, y1=mx)
        fig3.show()


    def tune_catboost_random(
        X: pd.DataFrame,
        y: np.ndarray,
        cat_idx: list[int],
        *,
        n_splits: int = 5,
        seed: int = 42,
        use_log_target: bool = False,
        n_trials: int = 40,
    ) -> tuple[pd.DataFrame, dict, np.ndarray]:
        rng = np.random.default_rng(seed)

        base = dict(
            loss_function="RMSE",
            eval_metric="RMSE",
            random_seed=seed,
            task_type="CPU",
            allow_writing_files=False,
            verbose=False,
            od_type="Iter",
            od_wait=300,
        )

        def log_uniform(a: float, b: float) -> float:
            return float(np.exp(rng.uniform(np.log(a), np.log(b))))

        def sample_params() -> dict:
            bootstrap_type = str(rng.choice(["Bayesian", "Bernoulli"]))
            params = dict(base)

            params["depth"] = int(rng.choice([4, 5, 6, 7, 8, 9, 10]))
            params["learning_rate"] = float(
                rng.choice([0.01, 0.015, 0.02, 0.03, 0.05, 0.08])
            )
            params["iterations"] = int(
                rng.choice([6000, 8000, 10000, 12000, 15000, 20000])
            )
            params["l2_leaf_reg"] = log_uniform(0.2, 30.0)
            params["random_strength"] = log_uniform(0.05, 10.0)

            # IMPORTANT: use only ONE of these. We'll keep rsm.
            params["rsm"] = float(rng.choice([0.7, 0.8, 0.85, 0.9, 0.95, 1.0]))

            params["min_data_in_leaf"] = int(
                rng.choice([1, 2, 3, 5, 8, 12, 20, 30])
            )

            params["bootstrap_type"] = bootstrap_type
            if bootstrap_type == "Bayesian":
                params["bagging_temperature"] = float(
                    rng.choice([0.0, 0.1, 0.2, 0.4, 0.7, 1.0, 2.0])
                )
                # do NOT set subsample
                params.pop("subsample", None)
            else:
                params["subsample"] = float(
                    rng.choice([0.55, 0.60, 0.65, 0.70, 0.75, 0.85, 1.0])
                )
                # do NOT set bagging_temperature
                params.pop("bagging_temperature", None)

            # REMOVE this line if you had it:
            # params["colsample_bylevel"] = ...

            return params

        rows: list[dict] = []
        best_oof: np.ndarray | None = None
        best_params: dict | None = None
        best_rmse: float = float("inf")

        print(f"Tuning CatBoost (random search): {n_trials} trials\n")
        for t in range(1, n_trials + 1):
            params = sample_params()
            print(
                f"[{t}/{n_trials}] params = "
                f"depth={params['depth']}, lr={params['learning_rate']}, iters={params['iterations']}, "
                f"l2={params['l2_leaf_reg']:.3g}, rsm={params['rsm']}, boot={params['bootstrap_type']}"
            )

            oof, folds, mean_s, std_s = run_catboost_cv_oof(
                X,
                y,
                cat_idx,
                params,
                n_splits=n_splits,
                seed=seed,
                use_log_target=use_log_target,
            )

            row = {
                "trial": t,
                "rmse_mean": mean_s,
                "rmse_std": std_s,
                "depth": params["depth"],
                "learning_rate": params["learning_rate"],
                "iterations": params["iterations"],
                "l2_leaf_reg": params["l2_leaf_reg"],
                "random_strength": params["random_strength"],
                "rsm": params["rsm"],
                "min_data_in_leaf": params["min_data_in_leaf"],
                "bootstrap_type": params["bootstrap_type"],
                "bagging_temperature": params.get("bagging_temperature", np.nan),
                "subsample": params.get("subsample", np.nan),
                "colsample_bylevel": params.get("colsample_bylevel", np.nan),
            }
            rows.append(row)

            if mean_s < best_rmse:
                best_rmse = mean_s
                best_params = params
                best_oof = oof

            print(f"  -> RMSE mean={mean_s:.6f} std={std_s:.6f}\n")

        lb = (
            pd.DataFrame(rows)
            .sort_values("rmse_mean", ascending=True)
            .reset_index(drop=True)
        )
        print("Top 10 trials:")
        print(lb.head(10).to_string(index=False))

        assert best_params is not None and best_oof is not None
        print("\nBest RMSE:", best_rmse)
        print("Best params (full):")
        print(best_params)

        return lb, best_params, best_oof


    # ----------------------------
    # Run tuning
    # ----------------------------
    USE_LOG_TARGET = False
    lb, best_params, best_oof = tune_catboost_random(
        X=Xtr_cb,
        y=y,
        cat_idx=cat_idx,
        n_splits=5,
        seed=42,
        use_log_target=USE_LOG_TARGET,
        n_trials=40,
    )
    residual_diagnostics(y=y, pred=best_oof, title_prefix="CatBoost (best) | ")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
