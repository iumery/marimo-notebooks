import marimo

__generated_with = "0.15.4"
app = marimo.App(width="full")


@app.cell
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
    return


@app.cell
def _(mo):
    mo.md(r"""# Basic Reference""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    | | Homology | Cohomology | Cohomology Ring | Fundamental Group | Higher Homotopy Group |
    | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | $S^n$ | $H_k(S^n) = \begin{cases}\mathbb{Z}, &k = 0,n\\0, &\text{ otherwise}\end{cases}$ | $H^k(S^n) = \begin{cases}\mathbb{Z}, &k = 0,n\\0, &\text{ otherwise}\end{cases}$ | $H^*(S^n) = \mathbb{Z}[\alpha]/(\alpha^2)$ where $\mid \alpha \mid = n$ | $\pi_1(S^n) = \begin{cases}\mathbb{Z},&n = 1\\0,&\text{ otherwise}\end{cases}$ | all homotopy group of $S^0$ is trivial,<br/> $\pi_n(S^n) = \mathbb{Z}$,<br/> if $n = 1$ then the only non-trivial homotopy group for $S^1$ is $\pi_1(S^1)$ |
    | Genus $g$ Orientable | $H_k(\Sigma_g) = \begin{cases}\mathbb{Z}, &k = 0,2\\\mathbb{Z}^{2g},&k=1\\0, &\text{ otherwise}\end{cases}$ | $H^k(\Sigma_g) = \begin{cases}\mathbb{Z}, &k = 0,2\\\mathbb{Z}^{2g},&k=1\\0, &\text{ otherwise}\end{cases}$ | (surface when $n = 2$)<br/>$H^*(T^n) = \Lambda[a_1,\dots,a_n]$ with $a_i^2 = 0$ and $a_ia_j = -a_ja_i$ | $\pi_1(\Sigma_g) = \langle a_1,b_1,\dots,a_g,b_g\mid[a_1,b_1]\cdot\dots\cdot[a_g,b_g] = 1 \rangle$ | if $g = 1$, $\pi_k(\mathbb{R}P^2) \cong \pi_k(S^2)$<br/>if $g> 1$, all higher homotopy groups are trivial |
    | Genus $g$ Non-Orientable | $H_k(M_g) = \begin{cases}\mathbb{Z}, &k = 0\\\mathbb{Z}^{g-1}\oplus \mathbb{Z}_2,&k = 1\\0, &\text{ otherwise}\end{cases}$ | $H^k(M_g) = \begin{cases}\mathbb{Z}, &k = 0\\\mathbb{Z}^{g-1},&k=1\\\mathbb{Z}_2,&k = 2\\0, &\text{ otherwise}\end{cases}$ | | $\pi_1(M_g) = \langle a_1,\dots,a_g \mid a_1^2\cdot\dots\cdot a_g^2 = 1 \rangle$ | all higher homotopy groups are trivial |
    | $\mathbb{R}P^n$ | if $n$ is odd, $H_k(\mathbb{R}P^n) = \begin{cases}\mathbb{Z},&k = 0,n\\\mathbb{Z}_2,&0<k<n,k\text{ odd}\\0,&\text{ otherwise}\end{cases}$<br/> if $n$ is even, $H_k(\mathbb{R}P^n) = \begin{cases}\mathbb{Z},&k = 0\\\mathbb{Z}_2,&0<k<n,k\text{ odd}\\0,&\text{ otherwise}\end{cases}$ | if $n$ is odd, $H^k(\mathbb{R}P^n) = \begin{cases} \mathbb{Z},&k = 0,n\\\mathbb{Z}_2,&0<k<n, k\text{ even}\\0,&\text{ otherwise}\end{cases}$<br/> if $n$ is even, $H^k(\mathbb{R}P^n) = \begin{cases} \mathbb{Z},&k = 0\\\mathbb{Z}_2,&0<k\le n, k\text{ even}\\0,&\text{ otherwise}\end{cases}$ | $H^*(\mathbb{R}P^n;\mathbb{Z}_2) = \mathbb{Z}_2[\alpha]/(\alpha^{n+1})$ where $\mid \alpha \mid = 1$ | $\pi_1(\mathbb{R}P^n) = \begin{cases}\mathbb{Z},&n=1\\\mathbb{Z}_2,&\text{ otherwise}\end{cases}$ | $\pi_k(\mathbb{R}P^n) \cong \pi_k(S^n)$ |
    | $\mathbb{R}P^{\infty}$ | inherit from $\mathbb{R}P^n$ | inherit from $\mathbb{R}P^n$ | $H^*(\mathbb{R}P^{\infty};\mathbb{Z}_2) = \mathbb{Z}_2[\alpha]$ where $\mid \alpha \mid = 1$,<br/> $H^*(\mathbb{R}P^{\infty}) = \mathbb{Z}[\alpha]/(2\alpha)$ where $\mid \alpha \mid = 2$ | $\pi_1(\mathbb{R}P^{\infty}) = \mathbb{Z}_2$ | all higher homotopy groups are trivial |
    | $\mathbb{C}P^n$ | $H_k(\mathbb{C}P^n) = \begin{cases}\mathbb{Z},&0\le k\le 2n, k \text{ even}\\0, &\text{ otherwise} \end{cases}$ | $H^k(\mathbb{C}P^n) = \begin{cases} \mathbb{Z},&0\le k \le 2n, k \text{ even}\\0,&\text{ otherwise}\end{cases}$ | $H^*(\mathbb{C}P^n) = \mathbb{Z}[\alpha]/(\alpha^{n+1})$ where $\mid \alpha \mid = 2$ | $\pi_1(\mathbb{C}P^n)$ is trivial | $\pi_2(\mathbb{C}P^n) \cong \mathbb{Z}$,<br/> $\pi_k(\mathbb{C}P^n) \cong \pi_k(S^{2n+1})$ for $n > 2$ |
    | $\mathbb{C}P^{\infty}$ | inherit from $\mathbb{C}P^n$ | inherit from $\mathbb{C}P^n$ | $H^*(\mathbb{C}P^{\infty}) = \mathbb{Z}[\alpha]$ where $\mid \alpha \mid = 2$ | $\pi_1(\mathbb{C}P^{\infty})$ is trivial | $\pi_2(\mathbb{C}P^{\infty}) \cong \mathbb{Z}$,<br/> all higher homotopy groups are trivial |
    | $X \vee Y$ | $\tilde{H_k}(X \vee Y) = \tilde{H_k}(X) \oplus \tilde{H_k}(Y)$ | $\tilde{H^k}(X \vee Y) = \tilde{H^k}(X) \oplus \tilde{H^k}(Y)$ | $\tilde{H^*}(X \vee Y) = \tilde{H^*}(X) \oplus \tilde{H^*}(Y)$ | $\pi_1(X \vee Y) = \pi_1(X) * \pi_1(Y)$ | very complicated in general,<br/> $\pi_n(S^n \vee S^n) = \mathbb{Z}^2$<br/>(consider CW structure),<br/> $\pi_n(S^1 \vee S^n) = \mathbb{Z}^{\mathbb{Z}}$<br/>(consider universal cover) |
    | $X \times Y$ | Künneth Formula | Künneth Formula | $H^*(X \times Y) = H^*(X) \otimes H^*(Y)$ | $\pi_1(X \times Y) = \pi_1(X) \oplus \pi_1(Y)$ | $\pi_k(X \times Y) = \pi_k(X) \oplus \pi_k(Y)$ |
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Eilenberg-MacLane Spaces Examples""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    1. $\bigvee\limits_kS^1$ is a $K(F_k, 1)$;
    2. $\mathbb{R}P^{\infty}$ is a $K(\mathbb{Z}_2, 1)$;
    3. $\mathbb{C}P^{\infty}$ is a $K(\mathbb{Z}, 2)$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Covering Spaces Reference""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    1. $\mathbb{R}$ is universal cover of $S^1$;
    2. $\mathbb{R}^2$ is universal cover of all closed orientable surfaces with genus $g \ge 1$ and all closed non-orientable surfaces with genus $g \ge 2$;
    3. $\mathbb{R}^n$ is universal cover of $T^n$;
    4. $S^1$ is $n$-sheeted cover of $S^1$;
    5. $S^k$ is double-sheeted and universal cover of $\mathbb{R}P^k$ for $k \ge 2$;
    6. Cayley graph on two generators is universal cover of $S^1 \vee S^1$.
    """
    )
    return


if __name__ == "__main__":
    app.run()
