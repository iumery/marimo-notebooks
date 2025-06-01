import marimo

__generated_with = "0.13.15"
app = marimo.App()


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
    mo.md(r"""## Problem 01""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Let $f: \mathbb{R} \to \mathbb{R}$ be a Lebesgue measurable function, $\int_a^b f dm = 0$ for all $a\le b \in \mathbb{Q}$, prove that $f = 0$ a.e**..

    Proof

    Any open or closed set $U$ in $\mathbb{R}$ can be written as a countable union of disjoint rational segments $R_i$, thus $\int_U f dm = \sum_i \int_{R_i}fdm = \sum_i 0 = 0$. Thus $\int_Bfdm = 0$ for all bounded Borel sets $B$. It is known that any Lebesgue measurable set is a union of a Borel measurable set and a set of Lebesgue measure zero (this is easy to prove: remember Lebesgue measure is inner regular, so any Lebesgue measurable set can be approximated by a sequence of closed (compact) sets, whose union is by definition Borel, and the complement is of Lebesgue measure zero), thus $\int_Lfdm = \int_Bfdm + \int_0 fdm = 0$ for any bounded Lebesgue measurable set. In particular, the sets $E_{+n} = \lbrace x | f(x) > 0 \rbrace \cap [-n, n]$ and $E_{-n} = \lbrace x | f(x) <0 \rbrace \cap [-n,n]$ are bounded Lebesgue measurable for all $n$, thus $\int_{E_{+n}}f dm = 0$ for all $n$, which implies $m(E_{+n}) = 0$ thus $m \lbrace f>0 \rbrace = 0$and similarly $m\lbrace f<0 \rbrace = 0$, thus $f = 0$ a.e..
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 02""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Let $X$ be the vector space of all real polynomials in one variable $x$. Prove of disprove that there exists a norm on $X$ making $X$ into a Banach space**.

    Proof

    We'll disprove this statement. Clearly $X$ has a countable basis ($x^0, x^1, x^2,\dots$); we will show that no normed linear space with countable basis is complete.

    Denote $X_n$ be the subspace of $X$ spanned by $x^0,x^1,\dots,x^n$. Each $X_n$ is of finite-dimension, thus is complete, thus is closed. By definition of basis, each $X_n$ is proper subspace of $X$, thus has empty interior (otherwise it contains an open ball, thus contains the entire space). In particular, $X_n$ is nowhere dense. Thus $X = \bigcup\limits_{n = 1}^{\infty} X_n$ is a countable union of nowhere dense subsets, thus $X$ is not complete by Baire.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 03""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Let $f$ be a non-decreasing function on $[0,1]$**.

    1. **Prove that $\int_0^1f'(x)dx \le f(1) - f(0)$**;
    2. **Let $\lbrace f_n \rbrace$ be a sequence of non-decreasing functions on $[0,1]$ such that the series $F(x) = \sum_{n=1}^{\infty}f_n(x)$ converges for all $x \in [0,1]$, prove that $F'(x) = \sum_{n=1}^{\infty}f'(x)$ a.e**..

    Proof

    1. Extend the definition of $f$ by setting $f(x) = f(1)$ for all $x > 1$. Since $f$ is non-decreasing, it is differentiable a.e., thus we have $f'(x) = \lim_{h \to 0^+}\frac{f(x+h)-f(x)}{h}$ for almost all $x$. We have: $$\begin{aligned}\int_0^1f'(x)dx &= \int_0^1\lim \frac{f(x+h)-f(x)}{h}dx \\ &\le \liminf \int_0^1\frac{f(x+h)-f(x)}{h}dx &\text{(Fatou's Lemma)} \\ &=\liminf(\frac{1}{h}\int_h^{1+h}f(x)dx - \frac{1}{h}\int_0^1f(x)dx) \\ &=\liminf(\underbrace{\frac{1}{h}\int_1^{1+h}f(x)dx}_{=f(1)} - \underbrace{\frac{1}{h}\int_0^hf(x)dx}_{\ge f(0)}) \\ &\le f(1) - f(0).\end{aligned}$$
    2. Since each $f_n$ is non-decreasing, $F$ is non-decreasing thus differentiable a.e.. Let $r_N(x) = \sum_{n=N+1}^{\infty}f_n(x)$ be the remainder of partial sum, then $r_N$ is also non-decreasing thus differentiable a.e., thus we can write $F'(x) = \sum_{n=1}^Nf'_n(x) + r'_N(x)$ for $x$ where all these functions are differentiable, which is viable a.e.. We will show that $r'_N(x) \to 0$ a.e. as $N \to \infty$. Notice that for almost all $x$, $r'_N(x) - r'_{N+1}(x) = f'_N(x) \ge 0$ because derivative of non-decreasing function is non-negative. Thus for almost all $x$, $\lbrace r'_N(x) \rbrace$ is a non-increasing sequence (index on $N$); it is also bounded below by $0$, thus the sequence converges and the limit is also non-negative (because all terms are non-negative). Monotone Convergence Theorem applies, we have that $\int_0^1 \lim r'_N(x)dx = \lim \int_0^1 r'_N(x)dx$, which by part 1 is less than $\lim(r_N(1) - r_N(0))$, which is $0$ because $F$ converges everywhere. Since $\lim r'_N(x)$ is a non-negative function which integrates to $0$, it is zero a.e..
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 04""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Let $I_{0,0} = [0,1]$; for $n \ge 0$ and $0 \le j \le 2^n-1$, let $I_{n,j} = [j2^{-n},(j+1)2^{-n}]$. For $f \in L^1([0,1])$, define $E_nf = \sum\limits_{j=0}^{2^n-1}(2^n\int_{I_{n,j}}f(t)dt)\chi_{I_{n,j}}$. Prove that $E_nf \to f$ a.e. on $[0,1]$**.

    Proof

    Realize that for each $x \in [0,1]$ and a fixed , $E_nf$ is the sum of over the intervals $I_{n,j}$ where $x$ lies in (there are at most $2$ of them), we can write $E_nf(x) = \sum\limits_{j, x\in I_{n,j}}\underbrace{\frac{1}{m(I_{n,j})}}_{=2^n}\int_{I_{n,j}}f(t)dt$. Since such family of intervals clearly shrinks nicely to $x$, thus the result is immediate by a theorem in chapter 7.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 05""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Let $H$ be a Hilbert space with the scalar product of $x$ and denoted by $(x,y)$ and let $A, B:H \to H$ be linear operators such that $(Bx,y) = (x,Ay)$ for all $x, y$. Prove that $A, B$ are bounded**.

    Proof

    Any Hilbert space is Banach space. Suppose $B$ is not bounded, then we can find a sequence $x_n \in H$ such that $\| x_n \| = 1$ but $\| Bx_n \| > n$ for each . By Banach-Steinhaus, there is some $y \in H$ such that $\sup\limits_n | (Bx_n, y)| = \infty$, thus $\sup\limits_n | (x_n,Ay) | = \infty$, but this is impossible because $| (x_n, Ay) | \le\| x_n \| \| Ay \| = \| Ay \|$ which is a fixed number (this has nothing to do with $A$ being bounded or not), thus $B$ must be bounded. Similarly we can get $A$ is bounded.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 06""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **$\ell^{\infty}(\mathbb{N})$ is a Banach space with respect to the norm $\| x \|_{\infty} = \sup_n| x_n |$**.

    1. **Prove that there exists a continuous linear functional $\varphi$ on $\ell^{\infty}(\mathbb{N})$ such that $\varphi(x) = \lim\limits_{n \to \infty}x_n$ whenever the limit exists**;
    2. **Prove that $\varphi$ is not unique**.

    Proof

    1. The set $C$ of all sequences in $\ell^{\infty}(\mathbb{N})$ for which the limit exists is a proper subspace of $\ell^{\infty}(\mathbb{N})$, and the operator $L$ on $C$ that sends a sequence to its limit is linear. $L$ is bounded because the limit of a sequence can be no more than its supremum, which in $\ell^{\infty}(\mathbb{N})$ is just the norm of the sequence. Thus by Hahn-Banach we can extend to a continuous (bounded) linear functional on $\ell^{\infty}(\mathbb{N})$, this is a $\varphi$ we wanted;
    2. Let $z$ be the sequence given by $z_n = (-1)^n$ (any sequence that is not in $C$ works). Let $D$ be the subspace spanned by $C$ and $z$; $D$ is apparently proper. We can extend $L$ to a bounded linear functional $L'$ on $D$ by choosing a value for $L'(z)$, then extend $L'$ to $\ell^{\infty}(\mathbb{N})$ by Hahn-Banach. Any two different choices of $L'(z)$ give different $\varphi$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 07""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Let $X$ be a Banach space and $X^{*}$ be its dual. Prove that if $X^{*}$ is separable then $X$ is separable**.

    Proof

    Let $\lbrace f_n \rbrace$, $n \in \mathbb{N}$ be a countable dense subset of $X^{*}$. For each $n$, pick $x_n \in X$ with $\| x_n \| = 1$ and $\| f_n(x_n) \| > \frac{1}{2} \| f_n \|$. Let $M$ be the span of $\lbrace x_n \rbrace$. We will show $M$ is dense in $X$. Suppose not, then there is $y \in X$ and $y \notin \overline{M}$, then by Hahn-Banach, there is a linear functional $f \in X^{*}$ such that $f = 0$ on $\overline{M}$ but $f(y) \ne 0$. Since $\lbrace f_n \rbrace$ is dense in $X^{*}$, there is a sub-collection $\lbrace f_{n_k} \rbrace$, viewed as a sequence, converges to $f$. Now $\frac{1}{2}\| f_{n_k} \| < \| f_{n_k}(x_{n_k}) \| = \| f_{n_k}(x_{n_k}) - \underbrace{f(x_{n_k})}_{=0}\| \le \| f_{n_k} - f \| \to 0$, thus $\| f_{n_k} \| \to 0$, thus $f_{n_k} \to 0$, but $f_{n_k} \to f$ and $f \ne 0$, so we have a contradiction.

    So we have $M$ is dense in $X$. Let $S$ be the subset of $M$ with all coefficients of $x_n$ being rational, then $S$ is a dense subset of $M$ thus a dense subset of $X$, thus $X$ is separable.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 08""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Suppose $f$ is a continuous function on $[0,2\pi]$ with Fourier series expansion $f(x) = \sum\limits_{n = -\infty}^{\infty}a_ne^{inx}$ such that $\sum | n a_n | \le 1$. Prove that $f$ is continuously differentiable**.

    Proof

    Denote $S_n$ to be partial sum of $\sum\limits_{n = -\infty}^{\infty}a_ne^{inx}$, then $S'_n(x) = \sum\limits_{k= -n}^nika_ke^{ikx}$, then for $n \ne m$, we have $| S_n'(x) - S_m'(x) | = | \sum\limits_{m+1 \le | k | \le n} ika_ke^{ikx}|$ $\le \sum | ika_ke^{ikx} |$ $=\sum | k a_k |$, which, if we take $n,m$ sufficiently large enough, can be taken to be $< \varepsilon$ for any fixed $\varepsilon > 0$ (because $\sum\limits_{n = -\infty}^{\infty}| n a_n | \le 1 < \infty$ so the terms goes to zero). Thus $S_n'(x)$ is a Cauchy sequence, thus convergent (because the space $\mathbb{C}$ is complete), and the convergence is uniform, because in the above inequality the $\varepsilon$ does not depends on $x$, it only depends on the sequence $a_n$. Thus $f'(x) = \lim S'_n(x) = (\lim S_n(x))' = (f(x))'$ and thus $f$ is differentiable. Also uniform limit of continuous function is continuous, thus the derivative of $f$ is continuous.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 09""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Suppose that $\lbrace \varphi_n \rbrace$ is an orthonormal sequence in a complex Hilbert space $H$, prove that the set of sums of the form $S = \sum_{i=1}^n\alpha_i\varphi_i$ is dense in $H$ if and only if $f \in H$ and $(f, \varphi_n) = 0$ for all $n$ implies that $f = 0$**.

    Proof

    ($\implies$) Suppose $S$ is dense in $H$ and $(f, \varphi_n) = 0$ for all $n$. Since $S$ is dense, we can pick $f_n$ to be a sequence in $S$ such that $f_n \to f$, then $\| f \|^2 = (f,f) = \lim(f,f_n) = 0$, which means $f = 0$;

    ($\impliedby$) By assumption it is not hard to see the only element in $S^{\perp}$ is $0$, thus $S$ is dense.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 10""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Suppose $X$ is a measurable space with positive measure $\mu$ such that $\mu(X) = 1$. Suppose $f$ is a complex measurable function on $X$. Prove that $\| f \|_r \le \| f \|_s$ for $0 < r < s \le \infty$**.

    Proof

    Suppose first $1\le r < s \le \infty$, then $s/r > 1$. Let $t$ be the conjugate exponent of $s/r$, then by Holder's inequality (applied to $| f |^r \cdot 1$) we have $| f|^r \|_1 \le$ $| f |^r \|_{s/r}\cdot\| 1 \|_t =$ $| f |^r \|_{s/r}$. That is to say $\int | f |^r d\mu \le (\int | f |^{r\cdot s/r}d\mu)^{r/s}$, take $r$-th root and we have $\| f \|_r \le \| f \|_s$.

    Suppose then $0 < r < s \le 1$, then $1 \le \frac{1}{s} < \frac{1}{r} < \infty$, then $\frac{1/r}{1/s} = \frac{s}{r} > 1$. Let again $t$ be the conjugate exponent of $s/r$, the rest is similar. Combine the two parts together and we have the desired result.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 11""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    1. **Suppose $\mu(\Omega) = 1$ and $f,g$ are positive measurable functions on $\Omega$ such that $fg \ge 1$. Show that $\int_{\Omega}f d\mu \cdot \int_{\Omega}g d\mu \ge 1$**;
    2. **Suppose $h: \Omega\to [0,\infty]$ is measurable. Let $A = \int_{\Omega}hd\mu$, prove that $\sqrt{1+A^2} \le \int_{\Omega}\sqrt{1+h^2}d\mu \le 1 + A$**.

    Proof

    1. $\sqrt{f},\sqrt{g}$ are also positive measurable functions and $\sqrt{fg} \ge 1$. By Holder's inequality, $p = q = 2$, $\int \sqrt{fg}d\mu \le \int (\sqrt{f}^2d\mu)^{1/2} \cdot \int (\sqrt{g}^2d\mu)^{1/2}$. LHS is greater than or equal to $1$, take square both sides and we have desired inequality;
    2. Consider the function $x \mapsto \sqrt{1+x^2}$, we will show it is convex: the derivative is $x(1+x^2)^{-1/2}$ and the second derivative is $(1+x^2)^{-3/2}$, which is always positive, so we have convexity. Now by Jensen's inequality, $\varphi \int h d\mu \le \int \varphi \circ h d\mu$ we have the first half.
        For the second half, write $1+A = 1 + \int_{\Omega}hd\mu = \int_{\Omega} 1+ h d\mu$. Notice now $1+h^2 \le (1+h)^2$ $\implies \sqrt{1+h^2} \le 1+h$ if $h \ge 0$, which gives the other half.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 12""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Let $L:X \to Y$ be a linear map from one Banach space to another. Suppose $f \circ L : X \to \mathbb{C}$ is bounded for each bounded linear functional $f$ on $Y$, show that $L$ is bounded**.

    Proof

    Suppose $L$ is unbounded, then there exists a sequence $x_n$, all with norm $1$, and $\| L x_n \| \ge n$ for each $n$. For each $n$, $x_n$ is of course not $0$ so $Lx_n$ is not $0$, so we can find a bounded linear functional $f_n$ on $Y$ with norm $1$ and $f_n(Lx_n) = \| Lx_n \|$. Use Banach-Steinhaus applied to $f_n \circ L$, the theorem says either there is some $M < \infty$ with $\| f_n\circ L \| \le M$ for all $n$, or $\sup\limits_{n}\| (f_n \circ L)x\| = \infty$ for all $x$ in some dense $G_{\delta}$ of $X$. By our construction we have $\| f_n\circ L \| \ge \| Lx_n \|$ which is assumed to be unbounded, so we do not have such $M$, so we must have the other situation. However, $\| (f_n \circ L)x \| \le \| f_n \| \| Lx \| = \| Lx \|$ is a fixed number (with respect to $n$), so we have a contradiction.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 13""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Suppose $f:[0,1] \to \mathbb{R}$ is continuous with $f(0) = 0$ and $f'(0)$ existing as a number. Prove that $x^{-3/2}f(x) \in L^1([0,1])$**.

    Proof

    By assumption we know $f'(0) = \lim\limits_{h \to 0} \frac{f(h)}{h}$ exists, so by definition of limit, we can find $\delta > 0$ so that $|\frac{f(h)}{h} | < 1$ whenever $0 \le h < \delta$. Then
    $$
    \begin{aligned}\int_0^1| x^{-3/2}f(x) | dx & = \int_0^{\delta}| x^{-3/2}f(x) | dx + \int_{\delta}^1 | x^{-3/2}f(x) | dx \\ &= \int_0^{\delta}| \frac{1}{x^{1/2}} \| \frac{f(x)}{x} | dx + \int_{\delta}^1 | x^{-3/2}f(x) | dx \end{aligned}
    $$
    The first part is finite by above and the fact that integrate of $\frac{1}{x^p}$, $p<1$ is finite over $[0,\delta]$. The second part is obviously finite (remember continuous map that is well-defined on compact set is bounded). So the sum is finite and the function is in $L^1$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 14""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Suppose $1<p < \infty$, $q$ be its exponent conjugate, $\alpha = 1/q$. Prove that if $f$ is absolutely continuous on $[a,b]$ and $f' \in L^p([a,b])$, then $f \in \text{Lip}~\alpha$**.

    Proof

    By assumption we have $f' \in L^1$ and $f(x) - f(a) = \int_a^x f'(t)dt$ for all $x \in [a, b]$. For any $x \ne y \in [a, b]$, write $$\begin{aligned}| f(x) - f(y) | &= | \int_y^x f'(t)dt | \le \int_y^x | f'(t)| dt \\ & \le (\int_y^x | f'(t)|^pdt)^{1/p} \underbrace{(\int_y^x1dt)^{1/q}}_{= | x - y |^{1/q}} \\ \frac{| f(x) - f(y) |}{| x-y |^{1/q}}&\le (\int_y^x | f'(t)|^pdt)^{1/p} = \| f' \|_p < \infty\end{aligned}$$ Take supremum over all pairs $x\ne y$ both sides, the RHS is a constant, so we get $\sup_{x\ne y} \frac{| f(x) - f(y) |}{| x-y |^{1/q}} < \infty$ and that is exactly the definition of $\text{Lip}~\alpha$ function.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 15""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Set $\varphi(t) = \begin{cases}1-\cos(t),&0 \le t \le 2\pi, \\ 0, &\text{otherwise.} \end{cases}$ For $-\infty < x < \infty$, set $f(x) = 1$, $g(x) = \varphi'(x)$, $h(x) = \int_{-\infty}^x\varphi(t)dt$. Verify the following**:

    1. **$(f* g)(x) = 0$**;
    2. **$(g * h)(x) = (\varphi * \varphi)(x) > 0$ for $x \in (0,4\pi)$**;
    3. **$(f * g)* h \equiv 0$ whereas $f*(g* h) \equiv k > 0$. Why they are not equal**?

    Proof

    An easy calculation gives that $g(x) = \begin{cases}\sin(x),&0 \le x \le 2\pi, \\ 0, &\text{otherwise} \end{cases}$ and it is continuous. By definition, $$(f* g)(x) = \int_{-\infty}^{\infty}f(x-y)g(y)dy = \int_{-\infty}^{\infty}g(y)dy = 0$$ because $f \equiv 1$ and sine curve over $[0,2\pi]$ is symmetric. $$(\varphi * \varphi)(x) = \int_{-\infty}^{\infty}\varphi(x-y)\varphi(y)dy.$$ Since $\cos(t) \le 1$, $1-\cos(t)\ge 0$, thus the only possibility that $(\varphi * \varphi)(x) = 0$ is when the function in the integrant is constant zero, which happens if and only if $x-y$ and $y$, $y \in [0,2\pi]$ has intersection of measure zero, which happens if and only if $x \le 0$ or $x \ge 4\pi$. Also $$\begin{aligned}(g * h)(x) &= \int_0^{2\pi}\varphi'(y)h(x-y)dy \\&=\varphi(2\pi)h(x-2\pi)- \varphi(0)h(x-0) + \int_0^{2\pi}\varphi(y)h'(x-y)dy \\ &= (\varphi * \varphi)(x)\end{aligned}$$ (when we do this we need to verify if $h$ and $\varphi$ are AC, but here it is obvious, continuous function on compact set is AC). The third assertion is now obvious. It's not associative because $f$ is not $L^1$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 16""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Suppose $f$, $f'$ and $f'' \in L^1$, $f, f'$ are absolutely continuous on any bounded subset of $\mathbb{R}$, and $\lim\limits_{x\to \pm\infty}f(x) = 0 = \lim\limits_{x \to \pm \infty}f'(x)$. Show that if $g = f''$, then $\hat{g}(t) = -t^2\hat{f}(t)$**.

    Proof

    By the assumption, integral by part applies, we have: $$\begin{aligned} \hat{g}(t) &= \int g(x)e^{-ixt}dx = \int f''(x)e^{-ixt}dx \\ &= f'(x)e^{-ixt} |_{x=-\infty}^{\infty} + \int-itf'(x)e^{-ixt}dx \\ &= \int-itf'(x)e^{-ixt}dx \\ &=-itf(x)e^{-ixt}|_{x=-\infty}^{\infty} + \int-t^2f(x)e^{-ixt}dx \\ &= \int-t^2f(x)e^{-ixt}dx = -t^2\hat{f}(t),\end{aligned}$$ as desired.
    """
    )
    return


if __name__ == "__main__":
    app.run()
