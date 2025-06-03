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
    mo.md(r"""# Spring Semester Homework 1""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 1

    **Let $X$ consists of two points $a$ and $b$, put $\mu(\lbrace a \rbrace) = \mu(\lbrace b \rbrace) = 1/2$, and let $L^p(\mu)$ be the resulting real $L^p$-space. Identify each real function $f$ on $X$ with the point $(f(a),f(b))$ in the plane, and sketch the unit balls of $L^p(\mu)$ for $0 < p \le \infty$. Note that they are convex if and only if $1 \le p \le \infty$. For which $p$ is this unit ball a square? A circle? If $\mu(\lbrace a \rbrace) \ne \mu(\lbrace b \rbrace)$, how does the situation differ from the preceding one**?

    Solution

    We want to find the unit balls of $L^p(\mu)$, we just define the $L^p$-norm in the usual way, and see which functions are of $B_p = \lbrace f \in L^p(\mu) | \| f \|_p \le 1 \rbrace$. As usual, we need to consider two cases:

    If $p = \infty$, since both set $\lbrace a \rbrace, \lbrace b \rbrace$ are of finite non-zero measure, we can see the essential supremum is just the maximum of $| f(a) |$ and $| f(b) |$. I.e. $f \in B_{\infty}$ if and only if $\max{\lbrace | f(a) |, | f(b) | \rbrace} \le 1$. If we identify $f$ on the real plane, this is a square (of length $2$, centered at origin).

    If $0 < p < \infty$, $\| f \|_p :=  (\int_X | f |^pd\mu)^{1/p}$, by assumption this equals $(\frac{1}{2}| f(a) |^p + \frac{1}{2}| f(b) |^p)^{1/p}$ , move $\frac{1}{2}$ out and take $p$-power, it is not hard to see $\| f \|_p \le 1$ if and only if $| f(a) |^p + | f(b) |^p \le 2$.

    So if $p = 1$, this is a square (rotated); if $p = 2$ this is a circle (I think we should really call it a disk); if $1<p<2$, this is some shape in between a square and a circle; if $0<p <1$ the shape is 'thinner' and if $2<p<\infty$ it is 'fatter':

    <img src="public/Pasted image 20220309211216.png" width="600" />

    If $\mu(a) \ne \mu(b)$: if one of them is $\infty$ then $f$ can only take $0$ there, so $(f(a),f(b))$ form some line segment; if one of them is $0$ then it is a band; if one of them is $\infty$ and the other is $0$ then it is a line; otherwise $\mu(a) \ne \mu(b)$ but they are still finite and positive, then the $L^{\infty}$ case does not change, for $L^p$ case we need to have $\mu(a)| f(a) |^p + \mu(b) | f(b) |^p \le 1$, so the graph is 'stretched' so it's never a square or circle, for example if $p = 2$ it is an ellipse.

    ## Exercise 2

    **Prove that the unit ball (open or closed) is convex in every normed linear space**.

    Proof

    Let $X$ be a normed linear space, let $B$ be its open unit ball, then for any $x, y \in B$ and $t \in [0,1]$ we have $\| tx + (1-t)y \|$ $\le t\| x \| + (1-t)\| y \|$ (by the definition of a normed linear space) $\le \max{\lbrace \| x \|, \| y \| \rbrace} < 1$, so $tx +(1-t)y \in B$, so by definition $B$ is convex. For the closed unit ball, just change $<$ to $\le$ and the argument is the same.

    ## Exercise 3

    **If $1 < p < \infty$, prove that the unit ball of $L^p(\mu)$ is strictly convex; this means that if** $$\| f \|_p = \| g \|_p = 1, f \ne g, h = \frac{1}{2}(f+g),$$ **then $\| h \|_p < 1$. Show that this fails in every $L^1(\mu)$, $L^{\infty}(\mu)$ and $C(X)$ (ignore triviality, such as spaces consisting of only one point)**.

    Proof

    Let $f,g,h$ be as in the statement for strictly convex. By Minkowski's inequality we have $$\| h \|_p = \| \frac{1}{2}(f+g) \|_p \le (\| f \|_p + \| g \|_p)/2 = 1.$$ Now remember the equality in Minkowski's inequality holds if and only if:

    1. One of $f, g$ is $0$ almost everywhere: we cannot have this, because the norms are assumed to be $1$;
    2. $f = ag$ almost everywhere for some constant $a$: we cannot have this neither, because again the norms are both $1$, so $a$ must be $1$ thus $f = g$, but we assumed $f \ne g$.

    So equality cannot be achieved anyway, so we have $\| h \|_p < 1$, and thus we have strict convexity.

    Assume the space is not trivial, strictly convex fails in:

    1. Every $L^1(\mu)$: take $E_1, E_2$ any two disjoint measurable sets in $X$ such that $0 < \mu(E_1), \mu(E_2) < \infty$, define $f = \frac{\chi_{E_1}}{\mu(E_1)}$ and $g = \frac{\chi_{E_2}}{\mu(E_2)}$, then it is easy to see $\| f \|_1 = \| g \|_1 = 1$, $f \ne g$ and $\| \frac{1}{2}(f+g) \|_1 = 1$;
    2. Every $L^{\infty}(\mu)$: similarly, define $f = \chi_{E_1}$ and $g = \chi_{E_1 \cup E_2}$, this gives a counterexample;
    3. Every $C(X)$: from this notation in the book we should assume $X$ is a compact normed linear space and we are using the sup-norm; we also know $X$ can be regarded as a metric space, say the distance function is $d$. Fix a point $a \in X$ and define $f(x) = \frac{1}{1+d(x,a)}$ and $g(x) = \frac{1}{(1+d(x,a))^2}$, they are continuous. It is easy to see both functions achieve maximum thus supremum at $x = a$ and have norm equals $1$; $f \ne g$ and $h = \frac{1}{2}(f+g)$ also has norm $1$.

    Those counterexamples all work in any corresponding spaces, so we have the desired statement.

    ## Exercise 4

    **Let $C$ be the space of all continuous functions on $[0,1]$ with the supremum norm. Let $M$ consists of all $f \in C$ for which** $$\int_0^{1/2}f(t)dt - \int_{1/2}^1f(t)dt = 1.$$ **Prove that $M$ is a closed convex subset of $C$ which contains no element of minimal norm**.

    Proof

    First, $M$ is not empty: let $f$ be the function that takes $0$ on $[1/2, 1]$ and is linear on $[0,1/2]$ with appropriate coefficients, this $f \in M$.

    Suppose $f, g \in M$ and $s \in [0,1]$, let $h = sf + (1-s)g$, we want to show $h \in M$, write: $$\begin{aligned}&~~~~~\int_0^{0.5}hdt - \int_{0.5}^1hdt \\ &= \int_0^{0.5}sf + (1-s)gdt - \int_{0.5}^1sf + (1-s)gdt \\ &= s(\int_0^{0.5} f dt - \int_{0.5}^1fdt) + (1-s)(\int_0^{0.5} g dt - \int_{0.5}^1gdt) \\ &=s+1-s \\&= 1\end{aligned},$$ also $h$ is clearly continuous, so indeed $h \in M$, $M$ is convex.

    Now let $f_n$ be a sequence of functions in $M$ and $f_n \to f$, we want to show $f \in M$. We have $\| f_n - f \| = \sup\limits_x | f_n(x) - f(x) | \to 0$ (remark: this means $f_n \to f$ uniformly). In particular we can find $N$ such that for all $n>N$, $\sup\limits_x| f_n(x) - f(x) | < 1$, so $f_n$ is bounded by $\max{\lbrace f_1,\dots,f_N, f+1\rbrace}$, so Dominated Convergence Theorem says that we can interchange the limit and integrant operation, and we have $$\begin{aligned}1 &= \lim \int_0^{0.5}f_ndt - \int_{0.5}^1f_ndt \\&= \int_0^{0.5}\lim f_ndt - \int_{0.5}^1\lim f_ndt \\&= \int_0^{0.5}fdt - \int_{0.5}^1fdt\end{aligned}$$ as desired. So $M$ is closed.

    Finally we show that it does not have an element of minimal norm. First notice $1 = | 1 |$ $= | \int_0^{0.5}fdt - \int_{0.5}^1fdt |$ $\le \int_0^{0.5}\| f \| dt + \int_{0.5}^1\| f \| dt$ $=\| f \|$. Suppose $\| f \| = 1$, then the equality of above inequality holds, that is $\int_0^1| f | dt = 1$, and we can see that $| f | = 1$ on $[0,1]$ (a.e., but not that important, as we are talking about continuous functions here), but in this case to have $\int_0^{0.5}fdt - \int_{0.5}^1fdt = 1$ we must have $f = 1$ on $[0,1/2]$ and $f = -1$ on $[1/2,1]$, which makes $f$ not continuous. So there is no element with norm $1$. However, for any $\varepsilon$, we can see that there is some $f \in M$ with norm $1+\varepsilon$:

    <img src="public/Pasted image 20220309162929.png" width="400" />

    Some work is needed to write down the explicit function, but it is definitely achievable. It shows that $\inf\limits_{f \in M}\lbrace \| f \| \rbrace$ is indeed $1$ but it is never achieved.

    ## Exercise 5

    **Let $M$ be the set of all $f \in L^1([0,1])$ relative to Lebesgue measure such that** $$\int_0^1f(t)dt = 1.$$ **Show that $M$ is a closed convex subset of $L^1([0,1])$ which contains infinitely many elements of minimal norm**.

    Proof

    Let $f$ be constant $1$, then $f \in M$, thus $M$ is not empty. Suppose $f, g \in M$ and $s \in [0,1]$, let $h = sf + (1-s)g$, then $$\int_0^1 | h | dt = \int_0^1| sf+(1-s)g | dt \le t\int_0^1| f | dt + (1-s) \int_0^1| g | dt,$$ since both $f,g$ are by assumption $L^1$, $h$ is $L^1$. Also $$\int_0^1 h dt = \int_0^1 sf+(1-s)gdt = s\int_0^1fdt + (1-s)\int_0^1gdt = 1$$ thus $h \in M$, thus $M$ is convex.

    Suppose $f_n$ is a sequence in $M$ and $f_n \to f$, meaning that $\| f_n - f \|_1 \to 0$. Since convergent sequence is bounded, $f_n - f$ must be $L^1$ for all $n$, thus $$| \int_0^1 f_n dt - \int_0^1 f dt | = | \int_0^1 f_n - f dt | \le\int_0^1 | f_n - f | dt =: \| f_n - f \|_1 \to 0,$$ in particular $1 = \lim\int_0^1 f_ndt = \int_0^1fdt$, thus $f \in M$ and $M$ is closed.

    Since $1 = | \int_0^1 f dt | \le \int_0^1 | f | dt =: \| f \|_1$, the norm of any $f \in M$ is at least $1$. For each $n = 1, 2, \dots$, define $f_n$ as $f_n(x) = nx^{n-1}$, then $f_n \ne f_m$ for $n \ne m$ and each $f_n$ is non-negative. A direct calculation gives $$\int_0^1f_ndt = \int_0^1nt^{n-1}dt=1^n-0^n = 1$$ so all $f_n \in M$, and that $$\| f_n \|_1 = \int_0^1 | f_n | dt = \int_0^1 f_n dt = 1,$$ thus they are all of norm $1$, the minimal one, and there are infinitely many of them.

    ## Exercise 6

    **Let $f$ be a bounded linear functional on a subspace $M$ of a Hilbert space $H$. Prove that $f$ has a unique norm-preserving extension to a bounded linear functional on $H$, and that this extension vanishes on $M^T$**.

    Proof

    Any Hilbert space is a Banach space. Let $f: M \to \mathbb{C}$ be a bounded linear functional. By Theorem 5.4 $f$ is uniformly continuous. Since $M$ is by definition a dense subset of its closure $\overline{M}$, there is a unique uniformly continuous extension $\overline{f}: \overline{M} \to \mathbb{C}$ of $f$. Thus we may assume $M$ is closed.

    We know that a closed subspace of a Hilbert space is again a Hilbert space, thus there is a unique $y \in M$ such that $f(x) = \langle x,y \rangle$ for all $x \in M$. By definition $\| f \|$ is the smallest number such that $\| f(x) \| \le \| f \| \| x \|$ for all $x$, yet from definition of the inner product in the Hilbert space we have $\| f(y) \| = \langle y,y \rangle = \| y \|\| y \|$, we must have $\| f \| = \| y \|$.

    Define $F: H \to \mathbb{C}$ as $F(x) = \langle x, y \rangle$, then of course this is an extension of $f$. For $x \in M^T$, $F(x) = \langle x,y \rangle = 0$ because $y \in M$. By a very same argument, $\| F \| = \| y \|$ as well, so the extension is a norm-preserving extension.

    (The above part can also start by using Hahn-Banach Theorem, which states that given $M$ a subspace of a normed linear space (any Hilbert space is a normed linear space) $H$ and $f$ a bounded linear functional on $M$, then $f$ can be extended to a bounded linear functional $F$ on $H$ so that $\| F \| = \| f \|$. Here we don't need to bother if $M$ is closed)

    It remains to prove uniqueness. Suppose $F'$ is also a norm-preserving extension of $f$ such that $F'(x) = 0$ for $x \in M^T$. Again there is a unique $y' \in M$ such that $F'(x) = \langle x,y' \rangle$. Also $\langle x,y \rangle = \langle x,y' \rangle$ on $M$, so $\langle x,y \rangle - \langle x,y' \rangle = 0$ and thus $\langle x, y-y' \rangle = 0$, thus $y - y' \in M^T$. In particular, $y$ can be uniquely written as $y = y' + (y - y')$ where $y' \in M$ and $y-y' \in M^T$, and that $\| y \|^2 = \| y' \|^2 + \| y-y' \|^2$. Since $\| F' \| = \| y' \| = \| f \| = \| y \| = \| F \|$, we must have $\| y-y' \| = 0$ thus $y = y'$, thus $F' = F$.

    ## Exercise 7

    **Construct a bounded linear functional on some subspace of some $L^1(\mu)$ which has two (hence infinitely many) distinct norm-preserving linear extensions to $L^1(\mu)$**.

    Solution

    Consider the Lebesgue measure on $[-1, 1]$, and consider the subspace $$M = \lbrace f \in L^1([-1,1]) | f(x) = 0 \text{ for }x\in [-1,0], f(x) \ge 0 \text{ for }x\in [0,1] \rbrace.$$ Define $\Lambda: M \to \mathbb{C}$ by $\Lambda f = \int_0^1 f dx$, then this is a linear functional. $\| \Lambda \|$ is defined to be $\sup\lbrace \| \Lambda f \| : \| f \|_1 = 1 \rbrace$, which can be written as $=\sup\lbrace \int_0^1 fdx : \int_{-1}^1 | f | dx = 1 \rbrace$, notice that for $f \in M$ we have $\int_{-1}^1 | f | dx = \int_0^1 f dx$, thus we have $\| \Lambda \| = 1$.

    Now, define $\Lambda_0: L^1([-1,1]) \to \mathbb{C}$ as $\Lambda_0 f = \int_0^1 f dx$, it is easy to be seen as an extension of $\Lambda$, and $\| \Lambda_0 \| := \sup\lbrace \| \Lambda_0 f \|: \| f \|_1 = 1 \rbrace$ is still $1$, so it is norm-preserving.

    Define $\Lambda_1 : L^1([-1,1]) \to \mathbb{C}$ as $\Lambda_1 f = \int_{-1}^1 f dx$, by our assumption of $M$, we should see that $\Lambda_1 f = \Lambda f$ for $f \in M$. Also $\| \Lambda_1 \| := \sup\lbrace \| \Lambda_1 f \|: \| f \|_1 = 1 \rbrace$ $=\sup\lbrace | \int_{-1}^1 f dx | : \int_{-1}^1 | f | dx = 1 \rbrace$. Since we know that $| \int_Xfdx | \le \int_X| f | dx$ is always true, yet $f \equiv 1/2$ is an example that $| \int_{-1}^1 f dx |$ is indeed $1$, we have that $\| \Lambda_1 \| = 1$.

    Of course $\Lambda_0 \ne \Lambda_1$, and we have two desired extensions. In fact, for any $a \in [0,1]$ the functional $\Lambda_a f = \int_{-a}^1 f dx$ is a different extension, so we have infinite many of them.

    ## Exercise 8

    **Let $X$ be a normed linear space, and let $X^{*}$ be its dual space with the norm $\| f \| = \sup\lbrace | f(x) | : \| x \| \le 1 \rbrace$**.

    ### Part 1

    **Prove that $X^{*}$ is a Banach space**.

    Proof

    For a reminder, $X^{*}$ is defined as the collection of all bounded linear functionals on $X$. Follow the definition of Banach space:

    1. If $\Lambda,\Theta \in X^{*}$, then $| \Lambda x + \Theta x | \le | \Lambda x | + | \Theta x |$ for all $x$, thus $\| \Lambda + \Theta \| \le \| \Lambda \| + \| \Theta \|$;
    2. If $\alpha$ is a scalar and $\Lambda \in X^{*}$, then $| \alpha \Lambda x | = | \alpha \| \Lambda x |$ for all $x$, thus $\| \alpha \Lambda \| = | \alpha | \| \Lambda \|$; 1 and 2 also shows this is a vector space;
    3. If $\| \Lambda \| = 0$, then by definition $\| \Lambda x \|$ $=| \Lambda x | \le \| \Lambda \| \| x \|$ for all $x$, so $| \Lambda x | \equiv 0$ and $\Lambda \equiv 0$;
    4. Suppose $\lbrace \Lambda_n \rbrace \subset X^{*}$ is a Cauchy sequence and fix some $\varepsilon0$. By definition there is some $N$ such that for $n,m > N$ we have $\| \Lambda_n - \Lambda_m \| < \varepsilon$. Use the definition of norm of a linear transformation, we have that $\| (\Lambda_n -\Lambda_m)(x) \|$ $= | (\Lambda_n - \Lambda_m) x|$ $\le \| \Lambda_n - \Lambda_m \|\| x \|$ $<\varepsilon \| x \|$ for any $x$. Thus if we fix an $x$, then $\lbrace \Lambda_n x \rbrace$ is a Cauchy sequence in $\mathbb{C}$, thus is convergent, denote the limit as $\Lambda x$, and do this for all $x \in X$. We want to show that $\lbrace \Lambda_n \rbrace$ converges to $\Lambda$ and $\Lambda \in X^{*}$;
    	1. Let $a,b$ be scalars and $x,y\in X$, then $\Lambda(ax+by) := \lim \Lambda_n(ax+by)$ $= \lim a\Lambda_n x + b\Lambda_n y$ $= a\Lambda x + b\Lambda y$, thus $\Lambda$ is a linear functional;
    	2. Every Cauchy sequence is bounded, thus $\lbrace \Lambda_n \rbrace$ is bounded. Say $\| \Lambda_n \| \le M$, then we can write $| \Lambda x | \le | \Lambda x - \Lambda_n x | + | \Lambda_n x |$ (remember $| (\Lambda_n - \Lambda_m) x| < \varepsilon \| x \|$, taking $m \to \infty$ now) $\le \varepsilon \| x \| + \| \Lambda_n \|\| x \|$ $\le (M+\varepsilon)\| x \|$, so $\| \Lambda \| = \sup \lbrace | \Lambda x | : \| x \| = 1 \rbrace$ $\le M+\varepsilon$ is bounded; so $\Lambda$ is a bounded linear functional thus by definition is in $X^{*}$;
    	3. In the above steps we used $| \Lambda x - \Lambda_n x | \le \varepsilon \| x \|$ for $n > N$, so $\| \Lambda - \Lambda_n \| :=$ $\sup \lbrace | \Lambda x - \Lambda_n x | : \| x \| = 1\rbrace$ $\le \varepsilon$, that we have convergence as desired.

    This shows $X^{*}$ is complete and we finished the proof.

    ### Part 2

    **Prove that for each $x \in X$, the mapping $f\to f(x)$ is a bounded linear functional on $X^{*}$ of norm $\| x \|$. This gives a natural imbedding of $X$ in its 'second dual' $X^{**}$, the dual space of $X^{*}$**.

    Proof

    Let us call this map $\varphi$. As per defined, for a fixed $x$, $\varphi: X^{*} \to \mathbb{C}$ is given by $\varphi(f) = f(x)$.

    Suppose $\Lambda, \Theta \in X^{*}$ and $a, b \in \mathbb{C}$, then $\varphi(a\Lambda + b \Theta)$ $=(a\Lambda + b\Theta)x$ $=a\Lambda x + b \Theta x$ $=a\varphi(\Lambda) + b\varphi(\Theta)$, thus $\varphi$ is a linear functional.

    By definition of the norm, we have $| \varphi(f) |  = | f(x) |$ $\le \| f \| \| x \|$, so $\| \varphi \| :=$ $\sup \lbrace | \varphi(f) | : \| f \| = 1 \rbrace$ $\le \| x \|$. Since $x$ is fixed, we see $\varphi$ is a bounded linear functional as desired.

    To finish the proof we need the other way of the inequality:

    1. If $x \ne 0$, Theorem 5.20 says there is a bounded linear functional $f \in X^{*}$ such that $f(x) = \| x \|$ and $\| f \| = 1$, thus for this $f$ we have $\| \varphi(f) \|$ $= \| f(x) \|$ $= \| x \|$ thus $\| \varphi \| = \| x \|$ (because it is a achieved upper bounded);
    2. If $x = 0$ then it is trivial, as that $\varphi(f) = f(0) = 0$ for any (linear) $f$ so $\| \varphi \| = \| x \| = 0$ is still true.

    ### Part 3

    **Prove that $\lbrace \| x_n \| \rbrace$ is bounded if $\lbrace x_n \rbrace$ is a sequence in $X$ such that $\lbrace f(x_n) \rbrace$ is bounded for every $f \in X^{*}$**.

    Proof

    We have that $X^{*}$ is a Banach space and $\mathbb{C}$ is a normed linear space. Let $\lbrace \Lambda_{x_n} \rbrace$ be the collection of bounded linear functional as defined in part 2, $\Lambda_{x_i}(f) = f(x_i)$ for each $x_i$. We apply the Banach-Steinhaus Theorem:

    By assumption, for each $f$ we have $| f(x_n) |  = | \Lambda_{x_n}(f) |$ is bounded. So it is not true that there is some $f$ so that $\sup\limits_{x_n} | \Lambda_{x_n}(f) | = \infty$, so we must have that $\lbrace \| \Lambda_{x_n} \| \rbrace$ is bounded, but as showed in part 2, this is the same sequence as $\lbrace \| x_n \| \rbrace$.

    ## Exercise 9

    **Let $c_0, \ell^1, \ell^{\infty}$ be the Banach spaces consisting of all complex sequences $x = \lbrace \xi_i \rbrace$ defined as follows**:

    1. **$x \in \ell^1$ if and only if $\| x \|_1 = \sum | \xi_i | < \infty$**;
    2. **$x \in \ell^{\infty}$ if and only if $\| x \|_{\infty} = \sup | \xi_i | < \infty$**;
    3. **$x \in c_0$ if and only if $\xi_i \to 0$**.

    **Prove the following four statements**:

    1. **If $y = \lbrace \eta_i \rbrace \in \ell^1$ and $\Lambda x = \sum \xi_i \eta_i$ for every $x \in c_0$, then $\Lambda$ is a bounded linear functional on $c_0$ and $\| \Lambda \| = \| y \|_1$. Moreover, every $\Lambda \in (c_0)^{*}$ is obtained in this way. In brief, $(c_0)^{*} = \ell^1$**;
    2. **In the same sense, $(\ell^1)^{*} = \ell^{\infty}$**;
    3. **Every $y \in \ell^1$ induces a bounded linear functional on $\ell^{\infty}$, as in part 1. However, this does not give all of $(\ell^{\infty})^{*}$, since $(\ell^{\infty})^{*}$ contains non-trivial functionals that vanishes on all of $c_0$**;
    4. **$c_0$ and $l_1$ are separable but $\ell^{\infty}$ is not**.

    Proof

    ### Part 1

    Suppose $x = \lbrace \xi_i \rbrace, z = \lbrace \theta_i \rbrace \in c_0$ and $a,b \in \mathbb{C}$, then $\Lambda(ax+bz) = \sum\limits_{i = 1}^{\infty}(a\xi_i + b\theta_i)\eta_i$ $=a\sum\limits\xi_i\eta_i + b \sum\limits\theta_i\eta_i$ $=a\Lambda x + b \Lambda z$, so $\Lambda$ is linear. For any $x$, $| \Lambda x |$ $=| \sum\limits\xi_i\eta_i |$ $\le\sum\limits| \xi_i \| \eta_i |$ $\le \sup | \xi_i | \sum | \eta_i |$ $=\| x \|_{\infty}\| y \|_1$ (this also shows the series converges absolutely so $\Lambda$ is well-defined), so $\| \Lambda \| = \sup \lbrace | \Lambda x |: x \in c_0, \| x \|_{\infty} =1\rbrace$ $\le \| y \|_1$.

    For the other direction, for a given $y = \lbrace \eta_i \rbrace$ and $n \in \mathbb{N}$, take $x_n = \lbrace \xi_{n,i} \rbrace$ where $\xi_{n,i} = \frac{\overline{\eta_i}}{| \eta_i |}$ if $i \le n$, and $0$ otherwise. Each $x_n$ is by construction in $c_0$ because it is eventually-zero, and clearly $\| x_n \|_{\infty} = 1$. Now for this particular choice of $x$, $\| \Lambda \|$ $\ge | \Lambda x_n |$ $= \sum\limits_{i = 1}^{\infty}\xi_{n,i}\eta_i$ $=\sum\limits_{i=1}^n| \eta_i |$ (because $\eta_i\overline{\eta_i} = |\eta_i|^2$) for each $n$; take $n \to \infty$ then $\| \Lambda \| \ge \sum | \eta_i |$ $=\| y \|_1$. So we have equality.

    Define a function $\varphi:\ell^1 \to (c_0)^{*}$ by $\varphi(y) = \Lambda$, as above, it is well-defined. We want to show it is a bijection:

    1. It is surjective: let $\Lambda \in (c_0)^{*}$, we want to find $y \in \ell^1$ such that $\varphi(y) = \Lambda$. Consider the sequence $\lbrace e_i \rbrace$ the unit vector basis of $c_0$, define $y = \lbrace \eta_i \rbrace$ by $\eta_i = \Lambda e_i$ so that $\varphi(y)$ indeed maps each $\lbrace \xi_i \rbrace \in c_0$ to $\sum\limits\xi_i\eta_i$ $=\Lambda\sum\limits\xi_ie_i$ $=\Lambda x$, we will show $y \in \ell^1$. For each $n$, define $x_n$ as before ($\xi_{n,i} = \frac{\overline{\eta_i}}{| \eta_i |}$ for $i \le n$, $0$ otherwise), then $\Lambda x_n$ $=\Lambda \sum\limits\xi_{n,i}e_i = \sum\limits\xi_{n,i}\Lambda e_i$ $=\sum\limits_{i=1}^n\xi_{n,i}\eta_i = \sum\limits_{i=1}^n| \eta_i |$. On the other hand $| \Lambda x_n |$ $\le \| \Lambda \|\| x_n \|_{\infty} = \| \Lambda \|$, if we take $n \to \infty$ then $\| y \|_1 \le \| \Lambda \|$ which is by assumption bounded, so $y \in \ell^1$;
    2. It is injective: Suppose $y = \lbrace \eta_i \rbrace$ and $z = \lbrace \theta_i \rbrace$ are both $\ell^1$, and $\varphi(y) = \varphi(z)$. To avoid confusion, let us add a subscript, denoting $\Lambda_{*}$ be the image of $*$ under $\varphi$. Then $\varphi(y - z)$ $= \Lambda_{y-z}$ where $\Lambda_{y-z}(x) =$ $\sum\limits\xi_i(\eta_i - \theta_i)$ $= \sum\limits\xi_i\eta_i  - \sum\limits\xi_i\theta_i$ $=\Lambda_y x - \Lambda_z x$ $=0$, thus $\varphi(y-z)$ is the trivial linear functional sending everything in $c_0$ to $0$, in particular we must have $\eta_i - \theta_i = 0$ for all $i$, thus $y = z$.

    To conclude we should also show this is an isometry (i.e. isomorphism), but this is just what we proved, as $\| y \|_1 = \| \Lambda \| = \| \varphi(y) \|$.

    ### Part 2

    This is pretty much the same idea with part 1. Fix $y = \lbrace \eta_i \rbrace \in \ell^{\infty}$, define $\Lambda$ so that for any $x = \lbrace \xi_i \rbrace \in \ell^1$ we have $\Lambda x = \sum\limits\xi_i\eta_i$, with a very same argument, we see each such series converges absolutely, $\Lambda$ is linear and it is bounded, thus $\Lambda \in (\ell^1)^{*}$ by definition (for boundedness this time we have $| \Lambda x |$ $\le \| x \|_1\| y \|_{\infty}$ so that $\| \Lambda \|$ $\le \| y \|_{\infty}$, basically we interchange $1$ with $\infty$ as it in part 1).

    The next step is to show $\| \Lambda \| = \| y \|_{\infty}$: consider the unit vector basis $\lbrace e_i \rbrace$ for $\ell^1\ell^1$, apparently $| \eta_i | = | \Lambda e_i |$ for each $i$, we may continue to write $\le \| \Lambda \| \| e \|_i = \| \Lambda \|$, take supremum each side we have $\| y \|_{\infty} = \sup\| \eta_i \| \le \| \Lambda \|$. So we have both direction thus we have equality.

    Finally, we define function $\varphi: \ell^{\infty} \to (\ell^1)^{*}$ by $\varphi(y) = \Lambda$ (or $=\Lambda_y$ when the notation is needed). As before, since $\| y \|_{\infty} = \| \Lambda \| = \| \varphi(y) \|$, this is an isometry. We just need to show it is a bijection:

    1. It is surjective: let $\Lambda \in (l_1)^{*}$, we want to find $y \in \ell^{\infty}$ such that $\varphi(y) = \Lambda$. Consider the sequence $\lbrace e_i \rbrace$ the unit vector basis of $l_1$, define $y = \lbrace \eta_i \rbrace$ by $\eta_i = \Lambda e_i$ so that $\varphi(y)$ indeed maps each $\lbrace \xi_i \rbrace \in l_1$ to $\sum\limits\xi_i\eta_i$ $=\Lambda\sum\limits\xi_ie_i$ $=\Lambda x$. By above, we already know such $y$ lies in $\ell^{\infty}$;
    2. It is injective: the proof is the same as above.

    ### Part 3

    For each $y = \lbrace \eta_i \rbrace \in \ell^1$, define $\Lambda$ as before that $\Lambda x = \sum\limits\xi_i\eta_i$ for $x = \lbrace \xi_i \rbrace \in \ell^{\infty}$, we saw this series converges absolutely, and it is a bounded linear functional, so $y$ induces a bounded linear functional on $\ell^{\infty}$.

    Now apparently $c_0 \subsetneq \ell^{\infty}$, because any convergent series must be bounded, but for example a series $x = \lbrace 1, 1, \dots \rbrace$ is $\ell^{\infty}$ yet not $c_0$. Moreover, $c_0$ is closed: let $x = \lbrace \xi_i \rbrace \in \ell^{\infty} - c_0$, then by definition $\lim \xi_i \ne 0$, meaning that there is an $\varepsilon0$ so that for any $N$, there is $n>N$ with $| \xi_n | \ge \varepsilon$; take any sequence $y = \lbrace \eta_i \rbrace$ such that $\| x-y \|_{\infty} < \varepsilon/2$, meaning that $\sup | \xi_n - \eta_n | < \varepsilon/2$ (and $y \in \ell^{\infty}$), then by triangle inequality we must have for any $N$, there is $n>N$ with $| \eta_i | \ge \varepsilon/2$, meaning that $y$ is also not $c_0$, so $\ell^{\infty} - c_0$ is open, thus $c_0$ is closed. So by Theorem 5.19, apply to $c_0 = M = \overline{M}$, $\ell^{\infty} = X$ and $x_0 \in \ell^{\infty}-c_0$, we can find some bounded linear functional $f$ on $\ell^{\infty}$ such that $f(x) = 0$ for all $x \in c_0$ but $f(x_0) \ne 0$.

    If for contrary $y \in \ell^1$ gives all of $\Lambda \in (\ell^{\infty})^{*}$: by part 1, those $\Lambda$ are $(c_0)^{*}$, and the above $f$ is such a functional, so $f \in (c_0)^{*}$ and it is trivial on $c_0$; this $f$ is also in $(\ell^{\infty})^{*}$ in the first place, so it is of one-to-one correspondence with the trivial linear functional on $c_0$, so it must be the trivial functional on $\ell^{\infty}$, but it is not, as $f(x_0) \ne 0$.

    ### Part 4

    1. $c_0$: consider the subset $S_n = \lbrace \lbrace \xi_i \rbrace: \xi_i \in \mathbb{Q}, \xi_i = 0\text{ if }i>n \rbrace$ and $S = \cup S_n$, then $S$ is countable, and it is easy to see it is dense in $c_0$ (with supremum norm);
    2. $\ell^1$: we use the same $S$, and remember that $\sum | \xi_i | < \infty$ means that for a fixed $\varepsilon$ there exists $N$ so that $\sum\limits_{i=N}^{\infty}| \xi_i | < \varepsilon/2$. Then for any $x \in \ell^1$ and any $\varepsilon>0$, just pick $N$ as discussed, then choose $y = \lbrace \eta_i \rbrace \in S_N$ so that $\sum\limits_{i=1}^N| \xi_i - \eta_i | \le \varepsilon/2$ (it is certainly achievable because it is finite), and thus the $\ell^1\ell^1$ distance between $x$ and $y$ is no larger than $\varepsilon$, which proves separability;
    3. $\ell^{\infty}$: consider the set $U = \lbrace \lbrace \xi_i \rbrace: \xi_i \in \lbrace 0,1 \rbrace\rbrace$, it is well-known that $U$ is uncountable; furthermore, for any $x\ne y \in U$, it is easy to see $\| x-y \|_{\infty} = 1$ is a fixed positive number. In particular it means $\lbrace x \rbrace$ is an open set for any $x \in U$, so any dense subset must contain all $x$ thus the entire $U$, which is not countable, so the space is not separable.

    ## Exercise 10

    **If $\sum \alpha_i\xi_i$ converges for every sequences $\lbrace \xi_i \rbrace$ such that $\xi_i \to 0$, prove that $\sum | \alpha_i | < \infty$**.

    Proof

    By the above exercise, if we denote $x = \lbrace \xi_i \rbrace$ such that $\xi \to 0$ then $\lbrace x \rbrace = c_0$ is a Banach space. For each $n$ define $\Lambda_n : c_0 \to \mathbb{C}$ by $\Lambda_n(x) = \sum\limits_{i=1}^n\alpha_i\xi_i$. Each $\Lambda_n$ is obviously linear.

    Write $| \Lambda_n x | = \sum\limits_{i=1}^n | \alpha_i\xi_i |$ $\le \sum\limits_{i=1}^n | \alpha_i | \| x \|_{\infty}$, then by definition of the norm of a linear transformation, $\| \Lambda_n \| \le \sum\limits_{i=1}^n | \alpha_i |$. On the other hand, $\| \Lambda_n \| :=$ $\sup\lbrace \| \Lambda_n x \| : x \in c_0, \| x \|_{\infty} \le 1 \rbrace$, so it is greater than or equal to any particular choice of $x$: take $x = \lbrace \xi_i \rbrace$ where $\xi_i = \frac{\overline{\alpha_i}}{| \alpha_i |}$ if $i\le n$ and $0$ otherwise, we can see $\| x \|_{\infty} \le 1$ and this makes $\| \Lambda_n x \| = \sum\limits_{i=1}^n | \alpha_i |$. So in conclusion we have $\| \Lambda_n \| = \sum\limits_{i=1}^n | \alpha_i |$. In particular each $\Lambda_n$ is a bounded linear functional.

    We assume $\sum\limits_{i=1}^{\infty}\alpha_i\xi_i$ converges for any $x \in c_0$, which is the same to say $\sup\limits_n | \Lambda_nx | < \infty$ for any $x \in c_0$. Thus Banach-Steinhaus Theorem says that there exists $M < \infty$ such that $\sum\limits_{i=1}^n | \alpha_i |$ $= \| \Lambda_n \| \le M$ for all $n$. Take limit and we have that $\sum\limits_{i=1}^n | \alpha_i | \le M < \infty$ as desired.

    ## Exercise 11

    **For $0 < \alpha \le 1$, let $\text{Lip}~\alpha$ denote the space of all complex functions $f$ on $[a,b]$ for which** $$M_f = \sup\limits_{s \ne t}\frac{| f(s) - f(t) |}{| s - t |^{\alpha}} < \infty.$$ **Prove that $\text{Lip}~\alpha$ is a Banach space if $\| f \| = | f(a) | + M_f$, also if $\| f \| = \sup\limits_x | f(x) | + M_f$. The members of $\text{Lip}~\alpha$ are said to satisfy a Lipschitz condition of order $\alpha$**.

    Proof

    First a property of $M_f$ that will be used, for $f,g \in \text{Lip}~\alpha$ and $b, c$ scalars, $$\begin{aligned}M_{bf+cg}&:= \sup \frac{| bf(s) + cg(s) - bf(t) - cg(t) |}{| s - t |^{\alpha}} \\ &\le \sup \frac{| b\| f(s) - f(t) |}{| s - t |^{\alpha}} + \sup\frac{| c \| g(s) - g(t) |}{| s - t |^{\alpha}} \\ &=:| b | M_f + | c | M_g\end{aligned}.$$ Notice if (at least) one of the scalar is $0$ then we have equality, we merely pull the scalar out. This also shows that any linear combination $bf+cg$ is also a member of $\text{Lip}~\alpha$, thus $\text{Lip}~\alpha$ is a vector space.

    Now follow the definition of a Banach space:

    1. Let $f, g \in \text{Lip}~\alpha$. For the first norm, we have $\| f + g \|$ $=| (f+g)(a) | + M_{f+g}$, use the above property, $\le | f(a) | + | g(a) | + M_f + M_g = \| f \| + \| g \|$. For the second norm, we have $\| f+g \| = \sup| (f+g)(x) | + M_{f+g}$ $\le M_f + M_g + \sup | f(x) | + \sup | g(x) |$ $= \| f \| + \| g \|$;
    2. Let $f \in \text{Lip}~\alpha$ and $b$ a scalar. For the first norm we have $\| bf \|$ $= | bf(a) | + M_{bf}$ $= | b \| f(a) | + | b | M_f$ $= | b | \| f \|$. For the second norm we have $\| bf \|$ $= \sup| bf(x) | + M_{bf}$ $= | b | M_f + | b | \sup | f(x) |$ $= | b | \| f \|$;
    3. If $\| f \| = 0$, then for the first norm $| f(a) |$ and $M_f$ are $0$ because they are non-negative, but then $| f(s) - f(a) | = 0$ for all possible $s$, so $f(x) \equiv 0$ on $[a, b]$. For the second norm we have $M_f$ and $\sup | f(x) |$ are both $0$, again it is easy to see $f(x) \equiv 0$;
    4. Fix $\varepsilon > 0$ and let $\lbrace f_n \rbrace \subset \text{Lip}~\alpha$ be a Cauchy sequence with respect to the first norm, that is to say there is some $N$ such that for $n,m>N$ we have $\| f_n - f_m \|$ $= | f_n(a) - f_m(a) | + M_{f_n - f_m} < \varepsilon$. So $| f_n(a) - f_m(a) | < \varepsilon$, thus $\lbrace f_n(a)\rbrace$ is a Cauchy sequence. Since it lies in $\mathbb{C}$ and complex field is complete, $\lbrace f_n(a) \rbrace$ is convergent. Also for any $x \in [a,b]$, we have $\varepsilon> M_{f_n-f_m}$ $\ge \frac{| f_n(a)-f_n(x)-f_m(a)+f_m(x)|}{| a-x |^{\alpha}}$, this shows $f_n(x)$ is Cauchy (i.e. $| f_n(x) - f_m(x) | <\varepsilon$) thus convergent for any $x$. Define $f(x) = \lim f_n(x)$. We want to show $f \in \text{Lip}~\alpha$ and $\| f_n - f \| \to 0$:
    	1. By convergence, we have $| f_n(a) - f(a) | \le \varepsilon$. Also $\varepsilon > M_{f_n - f_m}$ $\ge \frac{f_n(s) - f_n(t) - f_m(s) + f_m(t)}{| st |^{\alpha}}$, take $m \to \infty$ we have $M_{f_n - f} \le \varepsilon$. So $\| f_n - f \|$ $= | f_n(a) -f(a) | + M_{f_n - f}$ $\le 2\varepsilon$;
    	2. For any $s,t \in [a, b]$ and $s \ne t$ we have $\frac{| f(s) - f(t) |}{| s - t|^{\alpha}}$ $= \frac{| f(s) - f_n(s) + f_n(s) - f_n(t) + f_n(t) - f(t)|}{| s-t |^{\alpha}}$ $\le \frac{| f(s) - f_n(s) + f_n(t) - f(t) | + | f_n(s) - f_n(t) |}{| s-t |^{\alpha}}$ $\le M_{f_n - f} + M_{f_n}$, by above this $\le \varepsilon + M_{f_n}$. Since $f_n \in \text{Lip}~\alpha$, $M_{f_n} < \infty$ and thus $M_f < \infty$, thus $f \in \text{Lip}~\alpha$.
    	This shows $\text{Lip}~\alpha$ is complete thus a Banach space with respect to the first norm. Let $\lbrace f_n \rbrace \subset \text{Lip}~\alpha$ be a Cauchy sequence with respect to the second norm, that is to say there is some $N$ such that for $n,m>N$ we have $\| f_n - f_m \|$ $= \sup | f_n(x) - f_m(x) | + M_{f_n - f_m} < \varepsilon$. So $| f_n(x) - f_m(x) | < \varepsilon$ for all $x$ for $n, m> N$, thus $\lbrace f_n(x)\rbrace$ is a Cauchy sequence, thus $\lbrace f_n(x) \rbrace$ is convergent, the rest is pretty much the same as above.
    	Remark: another way is to first show that $\text{Lip}~\alpha$ is complete with respect to the second norm, denoted by $\| \cdot \|_{*}$, then show $\| f \|_{*} \le c \| f \|_a$ ($\| \cdot \|_a$ to denote the first norm) for some $c$ independent from the choice of $\lbrace f_n \rbrace$:
    	For any $x \in (a, b]$, we have $$\begin{aligned} | f(x) | &\le | f(a) | + | f(x) - f(a) | \\ &= | f(a) | + \frac{| f(x) - f(a) |}{| x - a |^{\alpha}}| x - a |^{\alpha} \\ &\le | f(a) | + M_f | b - a |^{\alpha} \\ \implies \\ \sup{| f(x) |} &\le | f(a) | + M_f | b - a |^{\alpha} \\ \sup{| f(x) |} + M_f &\le | f(a) | + M_f | b - a |^{\alpha} + M_f + | f(a) \| b - a |^{\alpha} \\ \| f \|_{*} &\le c \| f \|_a\end{aligned}$$ if we take $c = | b - a |^{\alpha} + 1$.
    	Then $\| f \|_a \le \| f \|_{*}$ (from definition) $\le c\| f \|_{a}$, so the two norms are equivalent, and thus $\text{Lip}~\alpha$ is complete with respect to the first norm as well.

    ## Exercise 14

    **Let $C$ be the space of all real continuous functions on $I$ with the supremum norm. Let $X_n$ be the subset of $C$ consisting of those $f$ for which there exists a $t \in I$ such that $| f(s) - f(t) | \le n | s - t |$ for all $s \in I$. Fix $n$ and prove that each open set in $C$ contains an open set which does not intersect $X_n$. Show that this implies the existence of a dense $G_{\delta}$ in $C$ which consists entirely of nowhere differentiable functions**.

    Proof

    Let everything be as in the description of the problem. Fix $n$. First we prove $X_n$ is closed in $C$. Let $\lbrace f_i \rbrace$ be a sequence of functions in $X_n$ and $f_i \to f$ uniformly. By the assumption we can find a sequence $\lbrace t_i \rbrace$ such that $| f_i(s) - f_i(t_i) | \le n | s - t_i |$ holds for each $i$ and all $s \in I$. Since $[0,1]$ is compact, there is a subsequence of $t_i$ that is convergent, for simplicity of notations, let us just assume $t_i$ is convergent and the limit is $t$. Then $| f(s) - f(t) |$ $= \lim\limits_{i \to \infty} | f_i(s) - f_i(t_i)|$ $\le \lim n | s - t_i |$ $= n | s - t |$. Thus $X_n$ is closed.

    Now we show $X_n$ has empty interior. The idea is to uniformly approximate any $f \in X_n$ using some $f'$ as below:

    <img src="public/Pasted image 20220309162107.png" width="600" />

    We can think of a band covers the graph of $f$ of some tiny width $\varepsilon$, $f'$ moves zig-zag between the two sides of the band by some line segments of slope equals $\pm 2n$. Then this $f' \notin X_n$, as that by construction for each $t \in [0,1]$ there are some $s$ such that $\frac{| f(s) - f(t)|}{| s-t |} = 2n \not\le n$.

    Thus the complement of $X_n$ is open and dense in $C$. By Baire's Theorem, the intersection of those complements is a dense $G_{\delta}$ in $C$, call it $G = \cap X_n^c$. Now notice that if a continuous function is differentiable at some point in $[0,1]$ (which is compact, so that $f$ is bounded), it must lie inside some $X_n$, thus $G$ consists exactly those nowhere differentiable functions, and we have the desired result.

    ## Exercise 16

    **(Closed Graph Theorem) Suppose $X$ and $Y$ are Banach spaces, and suppose $\Lambda$ is a linear mapping of $X$ into $Y$, with the following property: For every sequence $\lbrace x_n \rbrace$ in $X$ for which $x = \lim x_n$ and $y = \lim \Lambda x_n$ exist, it is true that $y = \Lambda x$. Prove that $\Lambda$ is continuous**.

    Proof

    Let $X \oplus Y$ be the set of all ordered pairs $(x,y), x \in X$ and $y \in Y$, with addition and scalar multiplication defined component-wise, then $X \oplus Y$ is Banach if $\| (x,y) \| = \| x \| + \| y \|$:

    1. Suppose $(x,y), (x',y') \in X \oplus Y$, then $\| (x,y) + (x'y') \|$ $= \| (x+x',y+y') \|$ $=\| x+x' \| + \| y + y' \|$ $\le \| x \| + \| x' \| + \| y \| + \| y' \|$ $=\| (x,y) \| + \| (x',y') \|$;
    2. Suppose $(x,y) \in X \oplus Y$ and $\alpha$ is a scalar, then $\| \alpha(x,y) \|$ $= \| (\alpha x, \alpha y) \|$ $= \| \alpha x \| + \| \alpha y \|$ $= | \alpha | \| x \| + | \alpha | \| y \|$ $= | \alpha | \| (x,y) \|$;
    3. Suppose $\| (x,y) \| = 0$, then $\| x \| + \| y \| = 0$, thus both $x, y$ are $0$ thus $(x,y) = 0$;
    4. Suppose $\lbrace (x_n, y_n) \rbrace$ is a Cauchy sequence and fix $\varepsilon > 0$, then there is some $N$ such that for $n, m > N$ we have $\| (x_n, y_n) - (x_m, y_m) \|$ $=\| x_n-x_m \| + \| y_n - y_m \|$ $< \varepsilon$, so $\lbrace x_n \rbrace$ and $\lbrace y_n \rbrace$ are both Cauchy, thus convergent because $X$ and $Y$ are Banach. Say they converge to $x,y$ respectively, then $\| (x_n,y_n) - (x,y) \|$ $=\| x_n - x \| + \| y_n - y \| \to 0$, thus $(x_n, y_n) \to (x,y)$, thus this sequence is convergent, thus this space is complete.

    So by definition, $X \oplus Y$ is Banach. Suppose $G$ is the graph of $\Lambda$ of which is as assumed in the problem, then $G$ is closed (graph of continuous function to Hausdorff space). $G$ is a subspace, because $X$ is a vector space. Thus $G$ is a closed subspace of complete metric space thus is also complete, thus $G$ is Banach.

    Notice that $\varphi:G \to X$, $(x, \Lambda x) \mapsto x$ is a continuous linear bijection, thus by Theorem 5.4, $\varphi$ is bounded, and by Theorem 5.10 $\varphi^{-1}$ is also bounded (and continuous). Thus $\| x \| + \| \Lambda x \|$ $=\| (x,\Lambda x) \|$ $= \| \varphi^{-1}(x) \|$ $\le \| \varphi^{-1} \| \| x \|$ thus $\| \Lambda x \|$ $\le (\| \varphi^{-1} \| -1)\| x \|$.

    Now from definition, $\| \Lambda \| := \sup\lbrace \| \Lambda x \| : x \in X, \| x \| = 1\rbrace$ $\le \| \varphi^{-1} \| -1$, which by above is bounded, apply Theorem 5.4 again, we have that $\Lambda$ is continuous.

    ## Exercise 18

    **Suppose $\lbrace \Lambda_n \rbrace$ is a sequence of bounded linear transformations from a normed linear space $X$ to a Banach space $Y$, suppose $\| \Lambda_n \| \le M < \infty$ for all $n$, and suppose there is a dense set $E \subset X$ such that $\lbrace \Lambda_n x \rbrace$ converges for all $x \in E$. Prove that $\lbrace \Lambda_n x \rbrace$ converges for each $x \in X$**.

    Proof

    Suppose $x \in X$ and fix $\varepsilon>0$. Since $E$ is dense, we can find $y \in E$ such that $\| x - y \| < \varepsilon/M$.

    Since $y \in E$, by assumption $\lbrace \Lambda_ny \rbrace$ is convergent thus Cauchy, so there is some $N$ such that for $n, m > N$ we have $\| \Lambda_ny - \Lambda_my \| < \varepsilon$. For the same $N$ and for $n, m > N$, we can write $$\begin{aligned}\| \Lambda_nx - \Lambda_mx \| &\le \| \Lambda_nx - \Lambda_ny \| + \| \Lambda_ny - \Lambda_my \| + \| \Lambda_my - \Lambda_mx \|\end{aligned},$$ plug in $\| \Lambda_ny - \Lambda_my \| < \varepsilon$ and remember $\Lambda_i$'s are linear, we have $$\begin{aligned}&< \| \Lambda_n(x-y) \| + \| \Lambda_m(x-y) \| + \varepsilon \\ &\le \| \Lambda_n \| \| x-y \| + \| \Lambda_m \| \| x-y \| + \varepsilon\end{aligned},$$ plug in everything we have, this value is smaller than $2M\cdot\varepsilon/M + \varepsilon = 3\varepsilon$. Since $\varepsilon$ is chosen arbitrarily, this shows $\lbrace \Lambda_nx\rbrace$ is Cauchy. Since $Y$ is Banach thus complete, $\lbrace \Lambda_nx \rbrace$ is convergent.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Spring Semester Homework 2""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 2
    **Prove that the example given at the end of Sec. 6.10 has the stated properties**.

    Proof

    So we want to show:

    >If $\mu$ is the Lebesgue measure on $(0,1)$, $\lambda$ be the counting measure on the $\sigma$-algebra of all Lebesgue measurable sets in $(0,1)$, then $\lambda$ has no Lebesgue decomposition relative to $\mu$, and although $\mu \ll \lambda$ and $\mu$ is bounded, there is no $h \in L^1(\lambda)$ such that $d\mu = hd\lambda$.

    In particular, $\lambda$ is not $\sigma$-finite (because finite $\times$ countable is countable, yet $(0,1)$ is uncountable). This example show that Lebesgue-Radon-Nikodym Theorem is in general false if we omit the $\sigma$-finite condition.

    For any $x \in (0,1)$, $\lambda(\lbrace x \rbrace)$ is by definition $1$, and $\mu(\lbrace x \rbrace) = 0$. Suppose $\lambda$ has a Lebesgue decomposition $\lambda = \lambda_a + \lambda_s$ where $\lambda_a \ll \mu$ and $\lambda_s \perp \mu$: since $\mu(\lbrace x \rbrace) = 0$ we must have $\lambda_a(\lbrace x \rbrace) = 0$, so we must have $\lambda_s(\lbrace x \rbrace) = 1$. Since this is true for all $x \in (0,1)$, it follows that $\lambda_s$ is concentrated on the whole $(0,1)$. Thus we cannot have $\lambda_s \perp \mu$, otherwise $\mu$ has to be concentrated on $\varnothing$, which is absurd. In conclusion we cannot have such decomposition.

    Now, if $E \in M$ such that $\lambda(E) = 0$, then $E$ must be empty, and of course $\mu(\varnothing) = 0$, thus $\mu \ll \lambda$. Also $\mu$ is bounded. Suppose now if there is $h \in L^1(\lambda)$ such that $d\mu = hd\lambda$ $\iff \mu(E) = \int_Ed\mu = \int_Ehd\lambda$ for all $E$. For any $x \in (0,1)$, $\mu(\lbrace x \rbrace) = 0$, but $\lambda(\lbrace x \rbrace) \ne 0$, so we must have $h(x) = 0$, so $h \equiv 0$ on $(0,1)$. On the other hand, $\mu(0,1) = 1$, thus $h$ cannot be identically $0$, so such $h$ cannot exist.

    ## Exercise 3

    **Prove that the vector space $M(X)$ of all complex regular Boreal measures on a locally compact Hausdorff space $X$ is a Banach space if $\| \mu \| = | \mu |(X)$. That the difference of any two members of $M(X)$ is in $M(X)$ was used in the first paragraph of the proof of Theorem 6.19; supply a proof of this fact**.

    Proof

    ### Part 1

    A little translation: Riesz Representation Theorem says that for any $\Phi \in (C_0(X))^{*}$ we have a unique $\mu_{\Phi} \in M(X)$ such that $\Phi f = \int_X fd\mu_{\Phi}$ for all $f \in C_0(X)$ such that $\| \Phi \| = | \mu_{\Phi} | (X)$. Thus if we define $g: (C_0(X))^{*} \to M(X)$ by $g(\Phi) = \mu_{\Phi}$, then:

    1. $g$ is well-defined by Riesz Representation Theorem;
    2. $g$ is surjective by the 'inverse' of Riesz Representation Theorem;
    3. $g$ is injective because $\mu_{\Phi}$ is the trivial measure if and only if $\Phi f \equiv 0$, thus $\Phi \equiv 0$ and $g$ has trivial kernel;
    4. $g$ is linear because $\int_Xfd(\mu_{a\Phi+b\Psi})$ $=(a\Phi+b\Psi)f$ $=a\Phi f + b\Psi f$ $= a\int_X f d\mu_{\Phi} + b\int_X f \mu_{\Psi}$ $= \int_X f da\mu_{\Phi} + \int_X f db\mu_{\Psi}$ $= \int_X f d(a\mu_{\Phi} + b\mu_{\Psi})$, meaning that $\mu_{a\Phi + b\Psi} = a\mu_{\Phi} + b\mu_{\Psi}$, which just means $g(a\Phi + b\Psi) = ag(\Phi) + bg(\Psi)$;
    5. $g$ is an isometry as $\| \Phi \|$ $= | \mu_{\Phi} | (X)$ $= \| \mu_{\Phi} \|$ by Riesz Representation Theorem and the assumption.

    So $g$ is an isometry isomorphism of vector spaces. We know $C_0(X)$ is a Banach space, thus the dual space $(C_0(X))^{*}$ is a Banach space, thus the isometry isomorphism image $M(X)$ is also a Banach space.

    ### Part 2

    This part essentially want us to verify $M(X)$ is a vector space, i.e. if $\mu, \lambda \in M(X)$ and $a$ is a scalar, then $a\mu$, $\mu + \lambda$ are also in $M(X)$.

    So suppose $\mu, \lambda \in M(X)$ and $a$ is a scalar; fix $\varepsilon0$. By definition it means $| \mu |, | \lambda |$ are (positive) regular Borel measure. Let $E$ be any Borel set, there are $V_1,V_2$ open sets containing $E$ such that $| \mu |(V_1) < | \mu | (E) + \varepsilon \implies | \mu |(V_1 - E) < \varepsilon$ and $| \lambda |(V_2 - E) < \varepsilon$; also there are $K_1,K_2$ compact sets contained in $E$ such that $| \mu | (K_1) > | \mu | (E) - \varepsilon \implies | \mu |(E - K_1) < \varepsilon$ and $| \lambda |(E - K_2) < \varepsilon$.

    Consider $| \mu + \lambda | (E)$, it by definition equals $\sup\limits_{\text{partition }\lbrace E_i \rbrace} \sum\limits_i | (\mu+\lambda)(E_i) |$ $\le \sup\sum\limits(|\mu|(E) + |\lambda|(E))$ $=| \mu |(E) + | \lambda | (E)$.

    Let $V = V_1 \cap V_2$ and $K = K_1 \cup K_2$, then $K \subset E \subset V$, $K$ is compact and $V$ is open, and we have: $$\begin{aligned} | \mu+\lambda |(V) &= | \mu+ \lambda |(E) + | \mu + \lambda | (V-E)\\& \le| \mu+ \lambda |(E) +|\mu|(V-E)+| \lambda |(V-E), \text{ by above inequality;} \\ &\le| \mu+ \lambda |(E)+| \mu |(V_1 - E)+| \lambda |(V_2-E),\text{ because those are larger sets;} \\ &<| \mu+ \lambda |(E)+2\varepsilon,\text{ by regularity discussed above.}\end{aligned}$$ This shows $| \mu + \lambda |$ is outer regular. Similarly $$\begin{aligned} | \mu +\lambda |(K) &= | \mu+\lambda |(E) - | \mu+\lambda |(E-K) \\ &\ge | \mu+\lambda |(E) - | \mu |(E-K_1) - | \lambda | (E-K_2) \\ &>| \mu+\lambda |(E) - 2 \varepsilon\end{aligned}.$$ Thus $| \mu + \lambda |$ is inner regular, thus it is regular, and by definition $\mu + \lambda$ is regular, thus in $M(X)$. Regularity for $|\alpha\mu|$ is trivial - all we need to do is multiply everything by a scalar. In conclusion, $M(X)$ is a vector space, thus in particular the difference of any two members of $M(X)$ is still in $M(X)$.

    ## Exercise 6

    **Suppose $1 < p < \infty$, prove that $L^q(\mu)$ is the dual space of $L^p(\mu)$ even if $\mu$ is not $\sigma$-finite**.

    Proof

    The question essentially want us to show a similar statement as Theorem 6.16:

    >Suppose $1 < p < \infty$, $\mu$ is a positive measure on $X$, and $\Phi$ is a bounded linear functional on $L^p(\mu)$, then there is a unique $g \in L^q(\mu)$ where $q$ is the exponent conjugate to $p$ such that $\Phi(f) = \int_Xfgd\mu$ for all $f \in L^p(\mu)$ and $\| \Phi \| = \| g \|_q$.

    Suppose we have a pair of conjugate exponents $1 < p,q < \infty$; we are given an arbitrary positive measure $\mu$ and a bounded linear functional $\Phi$ on $L^p(\mu)$.

    By Theorem 6.16, on a $\sigma$-finite subset $E \subset X$ we know we have the result, i.e. there is some $g_E \in L^q(E)$ (denote for those $L^q(\mu)$ functions such that $g(x) = 0$ for $x \notin E$) such that $\Phi(f) = \int_Xfg_Ed\mu$, and $f \in L^p(E)$. We should see that under those restrictions there is no need to restrict $\mu$ as well. We also have that $\| g_E \|_q = \| \Phi|_{L^p(E)} \|$ (i.e. $\Phi$ restricted to those $f \in L^p(E)$) which $\le \| \Phi \|$. In particular if $E'$ contains $E$, then $\| g_{E'} \|_q \ge \| g_E \|_q$.

    Let $M = \sup\limits_E\| g_E \|_q$ where $E$ is $\sigma$-finite, then $M \le \| \Phi \|$. Choose a sequence $\lbrace E_n \rbrace$ so that $\lim\limits_{n \to \infty}\| g_{E_n} \|_q = M$, and let $E = \bigcup\limits_{i=1}^{\infty}E_i$, so $E$ is $\sigma$-finite. By the above inequality we have $\| g_E \|_q \ge \| g_{E_n} \|_q$ for any $n$, thus by definition of supremum and limit we must have $\| g_E \|_q = M$. Now if $E'$ is a $\sigma$-finite subset containing $E$, then $E' - E$ is also $\sigma$-finite, so we can write $$(\int_X| g_E |^q d\mu\le)\int_X| g_E |^q d\mu + \int_X| g_{E'-E} | ^qd\mu = \int_X | g_{E'} |^qd\mu$$ because they only 'concentrate' on disjoint sets. Since $E'$ is $\sigma$-finite, we must have $\| g_{E'} \|_q \le M = \| g_{E} \|_q$, in particular $\int_X | g_{E'} |^qd\mu \le \int_X | g_{E} |^qd\mu$, so by a squeeze argument we see $$\int_X| g_{E'-E} |^qd\mu= 0.$$ And thus $$\int_X| g_E|^qd\mu = \int_X | g_{E'}|^qd\mu,$$ which means $g_{E'} = g_E$ a.e. on $X$, in particular they are identified in $L^q(\mu)$.

    The above argument doesn't really work if $p = 1$ so that $q = \infty$, as the $L^\infty$-norm is defined in another way.

    Now for any $f \in L^p(\mu)$, $E' = E \cup \lbrace x | f(x) \ne 0 \rbrace$ $=E \cup \lbrace x : | f(x) | > 1 \rbrace \cup \lbrace x : | f(x) | > 1/2 \rbrace \cup \dots$ is $\sigma$-finite (if any of the set is of infinite measure, $f$ won't lie in $L^p(\mu)$). Since $f=0$ outside $E'$, we can safely write: $$\Phi(f) = \int_Xfg_{E'}d\mu = \int_Xfg_Ed\mu.$$ (The second equality is due to the above discussion and $E'$ contains $E$) So $g = g_E$ will satisfy $\Phi(f) = \int_Xfgd\mu$ for all $f$. The other properties are built-in, so we are finished.

    ## Exercise 7

    **Suppose $\mu$ is a complex Borel measure on $[0, 2\pi)$ (or on the unit circle $T$), and define the Fourier coefficients of $\mu$ by** $$\hat{\mu}(n) = \int e^{-int}d\mu(t), n \in \mathbb{Z}.$$ **Assume that $\hat{\mu}(n) \to 0$ as $n \to +\infty$, prove that $\hat{\mu}(n) \to 0$ as $n \to -\infty$**.

    Proof

    By the hint, the assumption holds with $fd\mu$ in place of $d\mu$ if $f$ is a trigonometric polynomial, hence if $f$ is continuous, hence if $f$ is bounded Borel measurable. Now by Theorem 6.12, there is a (Borel) measurable $h$ such that $| h(x) | = 1$ (so it is bounded) and $$d\mu = hd| \mu |,$$ which can be rewritten as $$d| \mu | = \overline{h}d\mu$$
    because $h\overline{h} \equiv 1$. $\overline{h}$ is bounded Borel measurable because $h$ is, thus we can replace $d\mu$ by $\overline{h}d\mu$ which equals $d| \mu |$.

    Now $| \mu |$ is a real and positive Borel measure. For simplicity of notation we just write $\mu$ and assume it is now a real Boreal measure, and we have $$\hat{\mu}(-n) = \int e^{int}d\mu(t) = \int \overline{e^{-int}}d\mu(t) = \overline{\int e^{-int}d\mu(t)} = \overline{\hat{\mu}(n)}$$ (the third equality (move the conjugate out) fails if $\mu$ is complex). Thus $$\lim\limits_{n\to -\infty}\hat{\mu}(n) = \lim\limits_{n\to \infty}\hat{\mu}(-n) = \lim\limits_{n\to \infty}\overline{\hat{\mu}(n)} = 0$$ by assumption.

    ## Exercise 10

    **Let $(X, M, \mu)$ be a positive measure space. Call a set $\Phi \subset L^1(\mu)$ uniformly integrable if to each $\varepsilon > 0$ corresponds a $\delta>0$ such that** $$| \int_Efd\mu | < \varepsilon$$ **whenever $f \in \Phi$ and $\mu(E) < \delta$**.

    1. **Prove that every finite subset of $L^1(\mu)$ is uniformly integrable**;
    2. **Prove the following convergence theorem of Vitali: If**:
        1. **$\mu(X) < \infty$**;
        2. **$\lbrace f_n \rbrace$ is uniformly integrable**;
        3. **$f_n(x) \to f(x)$ a.e. as $n \to \infty$**;
        4. **$| f(x) | < \infty$ a.e**.,
    
        **Then $f \in L^1(\mu)$ and** $$\lim\limits_{n \to \infty}\int_X| f_n - f | d\mu = 0;$$
    3. **Show that part 2 fails if $\mu$ is Lebesgue measure on $(-\infty, \infty)$ even if $\lbrace \| f_n \|_1 \rbrace$ is assumed to be bounded. Hypothesis 1 can therefore not be omitted in part 2**;
    4. **Show that hypothesis 4 is redundant in part 2 for some $\mu$ (for instance, for Lebesgue measure on a bounded interval), but that there are finite measures for which the omission of 4 would make part 2 false**;
    5. **Show that Vitali's Theorem implies Lebesgue's Dominated Convergence Theorem, for finite measurable spaces. Construct an example in which Vitali's Theorem applies although the hypotheses of Lebesgue's Theorem do not hold**.

    Proof

    ### Part 1

    Let $\Phi = \lbrace f_1,\dots, f_k \rbrace \subset L^1(\mu)$, fix $\varepsilon>0$. Since $f_i \in L^1(\mu)$, for each $i$ we can find $\delta_i$ such that $$| \int_{E}f_i d\mu | < \varepsilon$$ whenever $\mu(E) < \delta_i$ (this is an exercise we did in Chapter 1). Take $\delta = \min\limits_i{\delta_i}$, then we get the desired condition.

    In particular, any $L^1(\mu)$ function by itself is uniformly integrable.

    ### Part 2

    First we need to improve the uniform integrability condition a little bit:
    Let us fix $\varepsilon > 0$. Since $\lbrace f_n \rbrace$ is uniformly integrable, there is $\delta > 0$ such that $| \int_E f_i d\mu | < \varepsilon$ whenever $\mu(E) < \delta$. Suppose $f_i$'s are real-valued, then $$\int_E| f_i | d\mu = | \int_E| f_i| d\mu| = | \int_{E_+}f_i d\mu-\int_{E_-}f_i d\mu|,$$ where $E_+ = \lbrace x \in E | f(x) \ge 0 \rbrace$,similar definition for $E_-$. In particular $\mu(E_+),\mu(E_-)\le \mu(E)$ . Essentially $\int_{E_+}f_i d\mu$ is the same as $\int_Ef_i^+d\mu$ (we do this because $f_i^+ \notin \Phi$ in general). And we can continue to write $$\le | \int_{E_+}f_i d\mu| + | \int_{E_-}f_i d\mu| < 2\varepsilon.$$ Since this works for arbitrary $\varepsilon$, it follows that (for real valued set of $f$) we have $\int_E | f | d\mu < \varepsilon$ (move the absolute value sign inside). Use usual procedure, the statement is also true for complex valued functions.

    In conclusion, we have a $\delta > 0$ such that $$\int_E| f_n | d\mu < \varepsilon$$ whenever $\mu(E) < \delta$.

    Next we follow the hint and prove the theorem. We use Egoroff's Theorem, it appears in Chapter 3's exercises. We didn't prove it, but let's believe it for now:

    >Egoroff's Theorem
    >If $\mu(X) < \infty$, $\lbrace f_n \rbrace$ is a sequence of complex measurable functions which converges point-wise at every point of $X$, then for any $\varepsilon > 0$, there is a measurable set $E \subset X$ such that $\mu(E^c) < \varepsilon$ and $\lbrace f_n \rbrace$ converges uniformly on $E$.

    It follows that (we are using our $\delta$ in place of $\varepsilon$ in the statement of Egoroff's Theorem, and using $E$ in place of $E^c$) there is some $E$ such that $\mu(E) < \delta$ and $\lbrace f_n \rbrace$ converges uniformly (to $f$, by assumption) on $E^c$, which means that there is $N$ such that for $n > N$ we have $\int_{E^c}| f_n - f | d\mu < \varepsilon$. Since $| f(x) |$ is by assumption bounded a.e., we may assume that $\int_E | f | d\mu < \varepsilon$ whenever $\mu(E) < \delta$ as well (or just take the minimal of the $\delta$'s). Now we have everything we need and: $$\begin{aligned}\int_X| f_n - f | d\mu &=\int_{E^c}| f_n - f | d\mu + \int_{E}| f_n - f | d\mu \\&\le \int_{E^c}| f_n - f | d\mu + \int_E| f_n | d\mu + \int_{E}| f | d\mu \\&<\varepsilon + \varepsilon + \varepsilon = 3\varepsilon \to 0\end{aligned}.$$ This in particular shows $| f_n - f | = | f - f_n |$ is in $L^1(\mu)$; since $| f | \le | f_n | + | f - f_n |$, we have that $f$ is in $L^1(\mu)$ because both of the summand terms are.

    ### Part 3

    Let $\lbrace f_n \rbrace$ be indexed on the integers, and define each $f_n$ as $$f_n = \begin{cases} 1, n\le x \le n+1\\0, \text{otherwise} \end{cases}.$$ $\Phi = \lbrace f_n \rbrace$ is obviously uniformly integrable (just take $\delta = \varepsilon$). Also $f_n$ clearly converges to $f \equiv 0$ point-wisely, in particular $| f(x) | < \infty$. However $\int_X| f_n - f | d\mu = 1$ for any $f_n$, so the limit must be $1$, not $0$.

    ### Part 4

    Consider the Lebesgue measure $m$ on $[0,1]$, if we can show hypothesis 1,2,3 implies hypothesis 4, we are finished. So suppose $| f(x) |$ is not bounded a.e., i.e. $m(F) > 0$ for $F = \lbrace x : | f(x)| = \infty \rbrace$. Fix $\varepsilon > 0$, uniform integrability and part 2 says that there is $\delta > 0$ such that $\int_E | f_n | dm < \varepsilon$ for all $E$ with $m(E)< \delta$.

    Choose $E \subset F$ such that $0<m(E)<\delta$, this is always doable in Lebesgue measure, now:

    1. $\int_E | f | dm = \int_E \lim | f_n | dm$ $\le \liminf \int_E| f_n | dm < \varepsilon$;
    2. Since $E \subset F$, $| f(x)| = \infty$ on $E$, since $m(E)>0$, we must have $\int_E | f | dm = \infty$.

    So there is a contradiction, thus we must have $| f(x) | < \infty$ a.e., result follows.

    The key of above example is that for a given $\delta > 0$ we can always find a measurable set $E$ with $0 < m(E) < \delta$. Otherwise, say $\mu$ is the measure on $\mathbb{R}$, such that if $0 \in E$ then $\mu(E) = 1$, otherwise $\mu(E) = 0$. This is a finite measure such that the above property no longer exists. Now just take $\lbrace f_n \rbrace$ to be the functions taking $n$ at $0$ (and arbitrary elsewhere), then they are uniformly integrable: for any $\varepsilon>0$ we can take $\delta = 1$, then $\mu(E)<\delta$ means $\mu(E) = 0$, uniform integrability follows trivially. If we let $f$ be the function taking $\infty$ at $0$, then hypothesis 1,2,3 are all satisfied, yet hypothesis 4 is not.

    If hypothesis 4 is not satisfied, then of course $f$ is not in $L^1(\mu)$, so we don't have the result of Vitali's Theorem.

    ### Part 5

    Suppose $\lbrace f_n \rbrace$ is a sequence of complex measurable functions on $X$ such that $\lim f_n(x) = f(x)$ exists for every $x \in X$, and there is a function $g \in L^1(\mu)$ such that $| f_n(x) | \le g(x)$ for all $n$ and $x$ (these are hypothesis of LDCT). We also assumed that $\mu(X) < \infty$ as stated in the problem.

    So hypothesis 1 and 3 of Vitali's Theorem are built-in. As we proved in part 1, a single $L^1(\mu)$ function, in particular $g$, is always uniformly integrable. Let us fix $\varepsilon$, it means that there is $\delta > 0$ such that $\int_E | g | d\mu < \varepsilon$ whenever $\mu(E) < \delta$ (again by part 2). Since $| f_n(x) | < g(x)$ by assumption, all $f_n$'s are apparently $L^1(\mu)$, and $$| \int_E f_n d\mu | \le \int_E | f_n | d\mu \le \int_E | g | d\mu < \varepsilon,$$ so $\lbrace f_n \rbrace$ is uniformly integrable. Also we have $\int_X | f | d\mu = \int_X \lim | f_n | d\mu$ $\le \liminf \int_X| f_n | d\mu$ $< \int_X | g | d\mu<\infty$, so $f$ is $L^1$ and in particular $| f(x) | < \infty$ a.e..

    So all the hypothesis of Vitali's Theorem holds, thus we have $$\lim\limits_{n \to \infty} \int_X| f_n - f | d\mu = 0,$$ and thus $$| \int_X f_n - f d\mu | \le \int_X | f_n - f | d\mu \implies \lim| \int_X f_n - f d\mu |=0,$$ which then implies $$\lim\int_Xf_nd\mu = \int_Xfd\mu,$$
    which are exactly the results of LDCT.

    Examine the hypothesis of the two theorems, we shall see Vitali's Theorem never requires a $g$ that is $L^1(\mu)$. From here we can construct something that satisfies Vitali but not Lebesgue:

    Let's take $\mu$ be the Lebesgue measure on $(0,1)$. Let $\lbrace f_n \rbrace$ be the set of functions indexed on $\mathbb{N}$ and $f_n(x) = \frac{1}{x}\chi_{[\frac{1}{1+n},\frac{1}{n})}$. Each $f_n$ is $L^1$ and they have point-wise limit $f \equiv 0$. It is not hard to see the lowest upper bound is the function $\frac{1}{x}$, so $g(x) \ge \frac{1}{x}$ for all $x$, but this is a well-known function that is not in $L^1(m)$. So the hypothesis of LDCT are not satisfied. It remains to check if $\lbrace f_n \rbrace$ is uniformly integrable, then the hypothesis of Vitali's Theorem are satisfied and we are done:

    Fix $\varepsilon>0$. For each $n$, $| \int_X f_n dm |$ $= \int\limits_{\frac{1}{n+1}}^{\frac{1}{n}}\frac{1}{x}dx$ $= \ln{\frac{n+1}{n}}$, which goes to $0$ as $n \to \infty$. So we can find $N$ such that for all $n > N$, $| \int_X f_n dm | < \varepsilon$, that in particular for all $n > N$ we can choose $\delta_1=1$ (or any positive number), so that $| \int_E f_n dm | < \varepsilon$ whenever $m(E) < \delta_1$. Now $\lbrace f_1,\dots, f_N \rbrace$ is a finite collection of $L^1$ functions thus is uniformly integrable, i.e. we may find $\delta_2$ so that $| \int_E f_{1,\dots,N} dm | < \varepsilon$ whenever $m(E) < \delta_2$. Take $\delta = \min{\delta_1, \delta_2}$ then this delta proves uniform integrability for the whole set $\lbrace f_n \rbrace$.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Spring Semester Homework 3""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 1

    **Show that $| f(x) | \le (Mf)(x)$ at every Lebesgue point of $f$ if $f \in L^1(\mathbb{R}^k)$**.

    Proof

    Suppose $f \in L^1(\mathbb{R}^k)$ and $x$ is a Lebesgue point of $f$. By definition of Lebesgue point, we know that: $$\lim_{r \to 0}\frac{1}{m(B_r)}\int_{B(x,r)}| f(y) - f(x) | dm(y) = 0.$$ As usual, since $x$ in the above expression is constant, we can pull it out, fix any $r > 0$, and we have: $$\begin{aligned}&~~~~\frac{1}{m(B_r)}\int_{B(x,r)}| f(y) - f(x) | dm(y)\\&\ge |\frac{1}{m(B_r)}\int_{B(x,r)} f(y) - f(x) dm(y) | \\ &= | f(x) -\frac{1}{m(B_r)}\int_{B(x,r)}f(y) dm(y)|. \end{aligned}$$ Then by triangle inequality, the above inequality, and the definition of $Mf$, we have: $$\begin{aligned}| f(x) | &\le | f(x) -\frac{1}{m(B_r)}\int_{B(x,r)}f(y) dm(y)| + | \frac{1}{m(B_r)}\int_{B(x,r)}f(y) dm(y)| \\ &\le \frac{1}{m(B_r)}\int_{B(x,r)}| f(y) - f(x) | dm(y) + (Mf)(x).\end{aligned}$$ Pass $r \to 0$, by definition of Lebesgue point the first term of the expression goes to $0$, and we have $$| f(x) | \le (Mf)(x).$$

    ## Exercise 10

    **If $f \in \text{Lip}~{1}$ on $[a , b]$, prove that $f$ is absolutely continuous and that $f' \in L^{\infty}$**.

    Proof

    By definition of Lipschitz condition, we have that $f$ satisfies: $$M_f = \sup\limits_{s \ne t}\frac{| f(s) - f(t) |}{| s - t |} < \infty.$$ Which in particular means $$\infty>M_f| s - t | \ge | f(s) - f(t) |, \forall s\ne t \in [a,b].$$ Suppose $\varepsilon is given, take $\delta = \varepsilon$, then if $(a_1,b_1),\dots,(a_n,b_n)$ are disjoint segments in $[a,b]$ such that the sum of length is less than $\delta = \varepsilon$ (and of course, we are assuming $b_i > a_i$ for all $i$), we get: $$\begin{aligned}\sum_{i = 1}^n | f(b_i) - f(a_i) | &\le \sum_{i=1}^nM_f| b_i - a_i|\\&=M_f\sum_{i=1}^n(b_i - a_i)\\&<M_f\varepsilon,\end{aligned}$$ where $M_f$ is a fixed number thus the last quantity goes to $0$, then by definition we have that $f$ is AC.

    It follows that $f'$ exists a.e. on $[a, b]$. For any point $s \in [a,b]$ such that the derivative exists, use the definition of derivative: $$\begin{aligned}| f'(s) | &= | \lim_{t \to s}\frac{f(t)-f(s)}{t - s} | \\&=\lim_{t\to s}\frac{| f(t) - f(s) |}{| t - s |} \\&\le \lim_{t \to s}\frac{M_f | t - s |}{| t - s |} \\&=M_f < \infty.\end{aligned}$$ Thus $f'$ is $L^{\infty}$ by definition.

    ## Exercise 11

    **Assume that $1 < p < \infty$, $f$ is absolutely continuous on $[a, b]$, $f' \in L^p$, and $\alpha = 1/q$, where $q$ is the exponent conjugate to $p$, prove that $f \in \text{Lip}~{\alpha}$**.

    Proof

    Since $f$ is AC on $[a, b]$, we know from Theorem 7.20 that $$f(x) - f(a) = \int_a^x f'(t)dt$$ for all $x \in [a, b]$, and $f'$ is in $L^1$. For any $x \ne y \in [a, b]$ we can take difference and get $$\begin{aligned}f(x) - f(y) = f(x) - f(a) - f(y) + f(a) \\= \int_a^x f'(t)dt - \int_a^y f'(t)dt = \int_y^x f'(t)dt.\end{aligned}$$ Since $f'$ is in $L^1$ we have: $$| f(x) - f(y) | = | \int_y^xf'(t)dt | \le \int_y^x| f'(t) | dt.$$ By Hölder's inequality we get: $$=\int_y^x| f'(t)| \cdot 1 dt \le (\int_y^x | f'(t) |^p dt)^{\frac{1}{p}}(\int_y^x1dt)^{\frac{1}{q}}.$$ Since we are using Lebesgue measure, the last term is just $| x - y |^{\frac{1}{q}}$, or $| x - y |^{\alpha}$. It is of course positive and finite so we can move it to the left and we get: $$\frac{| f(x) - f(y) |}{| x - y |^{\alpha}} \le (\int_y^x | f'(t) |^p dt)^{\frac{1}{p}} \le (\int_a^b | f'(t) |^p dt)^{\frac{1}{p}},$$ the RHS is exactly the $L^p$ norm of $f'$, which is finite by assumption, and which is a fixed number that does not depend on $x$ or $y$. Since the inequality holds for any $x\ne y \in [a, b]$, we get $$\sup_{x\ne y} \frac{| f(x) - f(y) |}{| x - y |^{\alpha}} \le \| f' \|_p < \infty$$ which means $f \in \text{Lip}~\alpha$ by definition.

    ## Exercise 16

    **Suppose $E \subset [a, b]$, $m(E) = 0$. Construct an absolutely continuous monotonic function $f$ on $[a, b]$ so that $f'(x) = \infty$ at every $x \in E$**.

    Solution

    Let's follow the hint. Since the Lebesgue measure is (outer) regular, we can find a sequence of open sets $V_1 \supset V_2 \supset \dots \supset E$ (so $E \subseteq \cap V_n$)such that $m(V_n) < 2^{-n}$. WLOG let us assume $V_1$ lies entirely inside $[a, b]$, otherwise just take intersection. Consider the function $F:[a, b] \to \mathbb{R}$ given by $F(x) = \sum\limits_{n = 1}^{\infty}\chi_{V_n}(x)$. Since $$\int_a^bFdm = \int_a^b\sum\chi_{V_n}dm = \sum\int_a^b\chi_{V_n}dm < \sum 2^{-n} \to 1 < \infty.$$ Thus $F \in L^1(m)$. By Theorem 7.11, if we define $f:[a,b] \to \mathbb{R}$ by $$f(x) = \int_a^xFdm$$ then $f'(x) = F(x)$ almost everywhere.

    Since $F$ is summation of characteristic functions, $F$ is non-negative, thus $f$ is non-decreasing. Use Theorem 7.18, we have that $f$ satisfies condition c, thus it satisfies condition a, i.e. $f$ is AC on $[a, b]$. It remains to show $f'(x) = \infty$ on $E$.

    So suppose $x \in E$, we want to show $f'(x) = \lim\limits_{y \to x}\frac{f(y) - f(x)}{y - x} = \infty$. By construction $x \in V_n$ for any $n$, pick an arbitrary $n$. Since $V_n$ is open, we can find an open interval $U$ contains $x$ lies inside $V_n$. Since we are taking $y \to x$, we can choose to only care about $y \in U$. So suppose $y \in U$, from the definition of $f$ we have $f(y) - f(x) = \int_x^yFdm$. Since $y \in V_n$ but not necessarily in $V_m$ for $m > n$, we have that $$\int_x^yFdm \ge \int_x^y \sum_{i=1}^n\chi_{V_i}dm\ge n(y-x).$$ The following picture illustrates why we have the inequality:

    <img src="public/Pasted image 20220327095614.png" width="600" />

    The point is that by the construction the entire $U$, thus in particular $[y,x]$, lies inside $V_n$ thus $V_m$ for $m<n$, thus $\int_x^yFdm$ (area by blue) is no less than $\int_x^y \sum_{i=1}^n\chi_{V_i}dm$ (area by red).

    It follows that for $y$ close to $x$, we have that $f(y) - f(x) \ge n(y - x)$ for arbitrary $n$, which implies $f'(x) = \lim\limits_{y \to x}\frac{f(y) - f(x)}{y - x} = \infty$ as desired.

    ## Exercise 17

    **Suppose $\lbrace \mu_n \rbrace$ is a sequence of positive Borel measures on $\mathbb{R}^k$ and** $$\mu(E) = \sum_{n =1}^{\infty}\mu_n(E).$$ **Assume $\mu(\mathbb{R}^k) < \infty$. Show that $\mu$ is a Borel measure. What is the relation between the Lebesgue decompositions of the $\mu_n$ and that of $\mu$? Prove that** $$(D_{\mu})(x) = \sum_{n = 1}^{\infty}(D_{\mu_n})(x), a.e. [m],$$ **derive corresponding theorems for sequences $\lbrace f_n \rbrace$ of positive non-decreasing functions on $\mathbb{R}$ and their sums $f = \sum f_n$**.

    Proof

    ### Part 1

    By the construction, $\mu$ is of course defined on any Borel set $E$, so we just need to prove it is a measure, i.e. has countable additivity. Suppose $\lbrace E_i \rbrace$ is a collection of mutually disjoint Borel set, then $$\begin{aligned}\mu(\bigcup_{i} E_i) &= \sum_n\mu_n(\bigcup_i E_i)&\text{(by definition)}\\&=\sum_n\sum_i\mu_n(E_i)&\text{(because each }\mu_n\text{ is a measure)}\\&=\sum_i\sum_n\mu_n(E_i)&\text{(because each }\mu_n\text{ is positive)}\\&=\sum_i\mu(E_i).\end{aligned}$$ And we are done.

    ### Part 2

    Suppose $\lambda$ is a positive $\sigma$-finite measure on the Borel measure on $\mathbb{R}^k$ (such measure exists, for example, the Lebesgue measure), then by Lebesgue-Radon-Nikodym we have the Lebesgue decomposition $\mu = \mu_a + \mu_s$, and $\mu_n = \mu_{n,a} + \mu_{n,s}$ for each $n$, such that $\mu_a, \mu_{n, a} \ll \lambda$ and $\mu_s, \mu_{n,s} \perp \lambda$. We claim that $\mu_a = \sum\limits_n \mu_{n,a}$ and $\mu_s = \sum\limits_n\mu_{n,s}$.

    First, $\mu = \sum\limits_n \mu_n$ $= \sum\limits_n(\mu_{n,a} + \mu_{n,s})$ $= \sum\limits_n\mu_{n,a} + \sum\limits_n\mu_{n,s}$. Also since all $\mu_{n, a}$'s are absolutely continuous with respect to $\lambda$, the summation $\sum\limits_n\mu_{n,a} \ll \lambda$ as well, and similarly we get $\sum_{n}\mu_{n,s} \perp \lambda$. Thus $\mu = \sum\limits_n\mu_{n,a} + \sum\limits_n\mu_{n,s}$ is also a Lebesgue decomposition, but we know the decomposition is unique, thus we have our claim proved.

    ### Part 3

    By LRN and Theorem 7.8, and use the above notations, we get that for any Borel measure $E$ we have $$\mu_a(E) = \int_ED\mu_adm, \forall E,$$ and $$\mu_{n,a}(E) = \int_ED\mu_{n,a}dm, \forall E.$$ By part 2 we get $$\begin{aligned}\int_ED\mu_adm &= \sum_n\int_ED\mu_{n,a}dm, \forall E\\&=\int_E\sum_nD\mu_{n,a}dm, \forall E.\end{aligned}$$ So $$\int_E(D\mu_a - \sum_nD\mu_{n,a})dm = 0, \forall E,$$ which implies $$(D{\mu_a})(x) = \sum_{n = 1}^{\infty}(D{\mu_{n,a}})(x), a.e. [m].$$ Also we know from Theorem 7.14 that $D\mu_s$ and $D\mu_{n,s} = 0$ a.e. $[m]$, and from the definition of symmetric derivative we see $D\mu = D\mu_a + D\mu_s$ and $D\mu_{n} = D\mu_{n,a} + D\mu_{n,s}$, and we have that $$(D{\mu})(x) = \sum_{n = 1}^{\infty}(D{\mu_n})(x), a.e. [m]$$ as desired.

    ### Part 4

    The theorem we would like to prove is that: If $\lbrace f_n \rbrace$ is a sequence of positive non-decreasing functions on $\mathbb{R}$ such that $f = \sum\limits_n f_n$, then $f' = \sum\limits_n f'_n$ almost everywhere with respect to $m$.

    From the assumption, $f$ is also positive non-decreasing, so $f'$ and $f'_n$ all exist a.e. $[m]$ (a result of problem 7.12).

    $f_n$ (and thus $f$) are non-decreasing functions, thus for any partial sum we have $$\frac{f(y) - f(x)}{y-x}\ge \sum_{n=1}^N\frac{f_n(y) - f_n(x)}{y-x}$$ because each fraction is positive (as long as $y\ne x$, of course), and $f$ is defined to be the infinite sum. In particular, taking $y \to x$, this means $f'(x) \ge \sum\limits_{n=1}^Nf'_n(x)$ thus $f'(x) \ge \sum\limits_{n=1}^{\infty}f'_n(x)$, a.e. $[m]$, which implies $\lim\limits_{n\to \infty}f'_n(x) = 0$.

    Since $\sum\limits^Nf_n(x) \to f(x)$, we can take a subsequence $N_k$ so that $g_k(x) = f(x) - \sum\limits^{N_k}f_n(x) < 2^{-k}$. Since $g_k(x)$ can be rewritten as $\sum\limits_{n = N_k+1}^{\infty}f_n(x)$, $g_k$ is non-decreasing. By Weierstrass M test, $\sum g_k$ converges (uniformly). Thus by the same argument as preceding paragraph, $\lim\limits_{k \to \infty}g'_k(x) = \lim\limits_{k \to \infty} (f'(x) - \sum\limits^{N_k}f_n'(x)) = 0$. This combine with the preceding paragraph give us that $$f'(x) = \sum f'_n(x)$$ as desired.

    ## Exercise 21

    **If $f$ is a real function on $[0,1]$ and** $$\gamma(t) = t + if(t),$$ **the length of the graph of $f$ is, by definition, the total variation of $\gamma$ on $[0, 1]$. Show that this length is finite if and only if $f \in BV$ (the class of all $f$ on $[0,1]$ that have bounded variation on $[0,1]$). Show that it is equal to**$$\int_0^1 \sqrt{1+[f'(t)]^2}dt$$ **if $f$ is absolutely continuous**.

    Proof

    If $f, g \in BV$ then $\sup \sum | f(t_i) - f(t_{i-1}) |$ and $\sup \sum | g(t_j) - g(t_{j-1}) |$ are both finite, then for any partition of $[0,x]$ we have $$\begin{aligned}&~~~~~\sum | (f+g)(t_k) - (f+g)(t_{k-1})| \\ &= \sum | f(t_k) - f(t_{k-1}) + g(t_k) - g(t_{k-1})| \\ &\le \sum | f(t_k) - f(t_{k-1}) | + | g(t_k) - g(t_{k-1})| \\ &\le \sup \sum | f(t_i) - f(t_{i-1}) | + \sup \sum | g(t_j) - g(t_{j-1}) |,\end{aligned}$$ which is by assumption finite, and it follows that $f+g \in BV$. Also it is clear that if $f \in BV$ then $cf \in BV$ for any scaler $c$ (just multiply everything by $c$). In particular, since the identity function is in $BV$ (the total variation of $\text{id}$ on $[a, x]$ is just $x-a$), we get $\gamma \in BV$ if and only if $f \in BV$.

    For the second part, let's first add a notation to make things clearer: if we denote the total variation of $\gamma$ to be $\Gamma$, the question wants us to show that $$\Gamma(1) = \int_0^1\sqrt{1+[f'(t)]^2}dt.$$ Another thing is that if $\gamma(t) = t + if(t)$ then $\gamma'(t) = 1 + if'(t)$ then $| \gamma'(t) |$ $= \sqrt{1 + [f'(t)]^2}$, that is where this expression comes from.

    Now, with a very similar argument as the first part, we see the sum of two AC functions is still AC, so does multiply by a scaler, thus if $f$ is AC then $\gamma$ is AC, on $I$. It follows that $\gamma$ is differentiable a.e. on $I$, $\gamma' \in L^1$, and $\gamma(x) - \gamma(0) = \int_0^x \gamma'(t)dt$ by Theorem 7.18 (remember this direction does not need $\gamma$ to be non-decreasing. By the preceding paragraph, for any $x < y \in [0,1]$ we have $$| \gamma(y) - \gamma(x) | = | \int_x^y\gamma'(t)dt | \le \int_x^y | \gamma'(t) | dt = \int_x^y\sqrt{1+[f'(t)]^2}dt.$$ So by definition we have ($\sup$ is taken over partitions of $[0,1]$) $$\Gamma(1) = \sup\sum | \gamma(t_i) - \gamma(t_{i-1})| \le \sup \int_{t_i}^{t_{i-1}}\sqrt{1+[f'(t)]^2}dt,$$ where the last expression is by definition $\int_0^1\sqrt{1+[f'(t)]^2}dt$, so we get $$\Gamma(1) \le \int_0^1\sqrt{1+[f'(t)]^2}dt.$$ Notice that for any $x < y \in [0, 1]$, we have $\Gamma(y) - \Gamma(x) = \sup\sum|\gamma(t_i) - \gamma(t_{i-1})|$ where the $\sup$ is taken over partitions of $[x, y]$, which in particular no less than $| \gamma(y) - \gamma(x) |$, which equals $\sqrt{(y-x)^2 + (f(y) - f(x))^2}$ , similar with what we did to $| \gamma' |$. So we have $$\begin{align*} \sqrt{(y-x)^2 + (f(y) - f(x))^2} &\le \Gamma(y) - \Gamma(x), \\ \sqrt{1+(\frac{f(y)-f(x)}{y-x})^2}&\le \frac{\Gamma(y) - \Gamma(x)}{y-x}.\tag{*}\end{align*}$$ By Theorem 7.19, since we know $\gamma$ is AC, $\Gamma$ is non-decreasing and AC on $I$, so by Theorem 7.18 we get $$\Gamma(1) = \int_0^1\Gamma'(t)dt$$ ($\Gamma(0)$ is of course $0$). Since both $f'$ and $\Gamma'$ exist a.e. on $I$, $(*)$ implies that $\sqrt{1+[f'(x)]^2} \le \Gamma'(x)$ a.e. on $I$, thus $$\Gamma(1) = \int_0^1\Gamma'(t)dt \ge \int_0^1 \sqrt{1+[f'(x)]^2}dt.$$ And we are finished.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Spring Semester Homework 4""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 1

    **Find a monotone class $M$ in $\mathbb{R}$ which is not a $\sigma$-algebra, even though $\mathbb{R} \in M$ and $\mathbb{R}-A \in M$ for every $A \in M$**.

    Solution

    Define $M$ to be the collection $\lbrace \varnothing, \mathbb{R},(-\infty,a), (-\infty,a], (a,\infty),[a,\infty) | a \in \mathbb{R}\rbrace$. It is clearly not a $\sigma$-algebra: the difference of two elements, say $(0,\infty) - (1,\infty)$, is not (necessarily) in $M$. From the definition it is also easy to see that $\mathbb{R} \in M$ and $\mathbb{R} - A \in M$ whenever $A \in M$, it remains to show $M$ is a monotone class.

    Let's, for simplicity of notations, call element of $M$ of the form $(-\infty,a)$ and $(-\infty,a]$ type 1, $(a,\infty)$ and $[a,\infty)$ type 2, and $\varnothing, \mathbb{R}$ type 3.

    Suppose we have an ascending chain $A_i \subseteq A_{i+1}$ such that each $A_i$ is element of $M$, then either all $A_i$'s are of type 1 and type 3, or they are all of type 2 and type 3: because, for example, $(-\infty,a)$ cannot contain $[b,\infty)$ for any $a,b$. WLOG say all $A_i$'s are of type 1 and type 3, then if any of $A_i$ is $\mathbb{R}$ then their union is $\mathbb{R}$, and if all of $A_i$ is $\varnothing$ then their union is $\varnothing$, otherwise $A_i$'s are of type 1 except for finitely many of them being $\varnothing$, and denote them $A_i = (-\infty,a_i)$ or $(-\infty,a_i]$. Then $\cup A_i = (-\infty,a)$ or $(-\infty,a]$ where $a = \lim a_i$ (possibly infinity, in this case the union is just $\mathbb{R}$) depending on the openness or closedness of $A_i$'s. In any of the cases, the union is in $M$.

    Suppose we have a decending chain $B_i \supseteq B_{i+1}$ such that each $B_i$ is element of $M$, then with the samiliar reason we can see either all $B_i$'s are of type 1 and type 3, or they are all of type 2 and type 3. Their intersection could be $\varnothing$ (if one of $B_i$ is empty, or if the lower bound of $B_i$'s goes to infinity, or if the upper bound of $B_i$'s goes to negative infinity), $\mathbb{R}$ (if all of them are $\mathbb{R}$), or some set of the type 1 or 2. In any of the cases, the intersection is in $M$.

    ## Exercise 2

    **Suppose $f$ is a Lebesgue measurable non-negative real function on $\mathbb{R}$ and $A(f)$ is the ordinate set of $f$. This is the set of all points $(x,y) \in \mathbb{R}^2$ for which $0 < y <f(x)$**.

    1. **Is it true that $A(f)$ is Lebesgue measurable, in the two-dimensional sense**?
    2. **If the answer to part 1 is affirmative, is the integral of $f$ over $\mathbb{R}$ equal to the measure of $A(f)$**?
    3. **Is the graph of $f$ a measurable subset of $\mathbb{R}^2$**?
    4. **If the answer to part 3 is affirmative, is the measure of the graph equal to zero**?

    Solution

    ### Part 1

    Suppose first $f$ is simple (and Lebesgue measurable non-negative), then $f = \sum\limits_i^na_i\chi_{A_i}$ where $a_i \ge 0$ are the finitely many images, and $\chi_{A_i}$ are the preimage of $a_i$ (which is by assumption measurable). Then $A(f)$ is easily seen to be $\bigcup\limits_{i}^n(A_i \times (0,a_i))$, which is $\mathbb{R}^2$ Lebesgue measurable by definition of $\sigma$-algebra, definition of measurable rectangle, and Theorem 8.11.

    Now we lift the assumption that $f$ is simple, but since it is measurable, we know that $f$ can be approximated by a non-decreasing sequence of simple functions $\lbrace s_n \rbrace$. Claim that $A(f) = \cup A(s_n)$. If the claim is true then $A(f)$ be a countable union of measurable sets is measurable. Proof of the claim:

    1. From the definition we can see $A(s_n) \subseteq A(f)$ for each $n$ because $s_n \le f$ for each $n$, thus $A(f) \supseteq \cup A(s_n)$;
    2. Suppose $(x,y) \in A(f)$, then $0 < y < f(x)$. By construction and definition of limit, we can pick $n$ so that $y < s_n(x) \le x$, so by definition $(x,y) \in A(s_n)$, thus $(x,y) \in \cup A(s_n)$, thus $A(f) \subseteq \cup A(s_n)$.

    Since we have both inclusion, the claim $A(f) = \cup A(s_n)$ is proved, and we have that $A(f)$ is (two-dimensional Lebesgue) measurable.

    ### Part 2

    We know $m_2$ is completion of $m_1 \times m_1$, so $$m_2(A(f)) = (m_1\times m_1)(A(f)) = \int_{\mathbb{R}}m(A(f)_x)dm$$ by definition 8.7. $A(f)_x$ ($x$ section) is defined to be $\lbrace y| (x,y) \in A(f)\rbrace$ thus is the open segment $(0,f(x))$, thus $m(A(f)_x) = f(x)$, plug this in we get $m_2(A(f)) = \int_{\mathbb{R}}f(x)dm$, so the statement is affirmative.

    ### Part 3

    The graph of $f$ is defined to be $G = \lbrace (x,y) | y = f(x) \rbrace$. Consider the sequence $\lbrace \frac{1}{n} \rbrace$ and $\cap A(f+\frac{1}{n})$, it is not hard to see $\cap A(f+\frac{1}{n}) = \lbrace (x,y) | 0<y \le f(x) \rbrace$ thus $\cap A(f+\frac{1}{n}) - A(f) = \lbrace (x,y) | y = f(x) \text{ and }y \ne 0\rbrace$, so we have $$G = (\cap A(f+\frac{1}{n}) - A(f)) \sqcup \lbrace (x,0) | f(x) = 0 \rbrace, $$ or equivalently $$G = (\cap A(f+\frac{1}{n})  - A(f)) \sqcup (f^{-1}(0)\times \lbrace 0 \rbrace).$$ Now it is not hard to see each term is Lebesgue measurable, thus $G$ must be Lebesgue measurable.

    ### Part 4

    Yes, just use definition like part 2 again: $$m_2(G) = (m_1\times m_1)(G) = \int_{\mathbb{R}}m(G_x)dm,$$ now $G_x$ is by definition $\lbrace y | (x,y) \in G \rbrace = \lbrace f(x) \rbrace$ is a single point, thus $m(G_x) \equiv 0$ thus the integral equals $0$, result follows.

    ## Exercise 3

    **Find an example of a positive continuous function $f$ in the open unit square in $\mathbb{R}^2$, whose integral (relative to Lebesgue measure) is finite but such that $\varphi(x)$ (in the notation of Theorem 8.8) is infinite for some $x \in (0,1)$**.

    Solution

    Let $f(x,y)$ be defined on $(0,1) \times (0,1)$ be positive continuous, then by Theorem 8.8, define $$\varphi(x) = \int_0^1f_x(y)dy,$$ then $$\int_0^1\varphi(x)dx = \int_0^1\int_0^1f(x,y)dydx.$$ So we want an example with finite $\int_0^1\varphi(x)dx$ but $\int_0^1f_x(y)dy = \infty$.

    Consider $\varphi(x) = \frac{1}{\sqrt{| x-\frac{1}{2} |}}$. Clearly $\varphi(\frac{1}{2}) = \infty$, and $\int_0^1 \frac{1}{\sqrt{| x - \frac{1}{2}|}}dx$ $= \int_0^{1/2} \frac{1}{\sqrt{| x - \frac{1}{2}|}}dx + \int_{1/2}^1 \frac{1}{\sqrt{| x - \frac{1}{2}|}}dx$ $= 2\sqrt{2}$ (the point here, is that integrate $\frac{1}{x^a}$, $a < 1$, is finite from $0$ to $1$, is infinite from $1$ to $\infty$; and if $a>1$ then the integrant is finite if it is taken from $1$ to $\infty$, is infinite from $0$ to $1$). Then the natural choice for is $f(x,y) = y^{\sqrt{| x - \frac{1}{2}|}} -1$, and we have a desired example.

    ## Exercise 4

    **Suppose $1 \le p \le \infty$, $f \in L^1(\mathbb{R})$ and $g \in L^p(\mathbb{R})$**.

    1. **Imitate the proof of Theorem 8.14 to show that the integral defining $(f* g)(x)$ exists for almost all $x$, that $f* g \in L^p(\mathbb{R})$, and that $\| f* g \|_p \le \| f \|_1\| g\|_p$**;
    2. **Show that equality can hold in part 1 if $p= 1$ and if $p = \infty$, and find the conditions under which this happens**;
    3. **Assume $1 < p < \infty$, and equality holds in part 1, show that then either $f = 0$ a.e. or $g = 0$ a.e.**;
    4. **Assume $1 \le p \le \infty$, $\varepsilon 0$, and show that there exist $f \in L^1(\mathbb{R})$ and $g \in L^p(\mathbb{R})$ such that $\| f * g \|_p > (1-\varepsilon)\| f \|_1\| g \|_p$**.

    Proof

    ### Part 1

    As discussed in the proof of Theorem 8.14, we can assume $f,g$ are Borel. We separate the cases when $p = \infty$ and $1 \le p < \infty$:

    1. If $p = \infty$, then $$\begin{aligned}| f* g (x)| &:= |\int_{\mathbb{R}}f(x-y)g(y)dy| \\ &\le \int_{\mathbb{R}}| f(x-y) \| g(y)| dy  & \text{(product is in } L^1 \text{)}\\ &\le \| g \|_{\infty}\int_{\mathbb{R}}| f(x-y) | dy \\&= \| g \|_{\infty}\| f \|_1&\text{(translate invariant)}\end{aligned}$$ which proves all three statements;
    2. If $1 \le p < \infty$, write $g$ as a summation $g_1 + g_2$ where $g_1 \in L^1(\mathbb{R})$ and $g_2 \in L^{\infty}(\mathbb{R})$ except for possibly on a set of measure zero (if $g$ cannot be written in this way then it means it attains infinity on a set of positive measure, meaning $g$ is not $L^p$), then $f* g(x)$ $= \int f(x-y)g(y) dy$ $= \int f(x-y)(g_1(y) + g_2(y))dy$. Also it is Borel by the proof of Theorem 8.14, thus the integral defining this convolution exists almost everywhere (where $g = g_1+g_2$) by Theorem 8.14 ($L_1$ part is well-defined) and above ($L^{\infty}$ part is well-defined).
    	Let $q$ be $p$'s conjugate exponent, write $$\begin{aligned} &\int_{\mathbb{R}}| f(x-y)g(y)| dy = \int_{\mathbb{R}}| f(x-y) |^{1/q} | f(x-y) |^{1/p} | g(y) | dy \\&\le (\int_{\mathbb{R}}| f(x-y) | dy)^{1/q} (\int_{\mathbb{R}}| f(x-y) \| g(y)|^p dy)^{1/p} &\text{(Hölder)} \\&=\| f\|_1^{1/q}(\int_{\mathbb{R}}| f(x-y) \| g(y)|^p dy)^{1/p}\end{aligned}$$ so now $$\begin{aligned}\int_{\mathbb{R}}| (f* g)(x) |^p dx &=\int_{\mathbb{R}}(| \int_{\mathbb{R}} f(x-y)g(y)dy|^p) dx \\ &\le \int_{\mathbb{R}}(\int_{\mathbb{R}}| f(x-y)g(y)| dy)^p dx \\ &\le \int_{\mathbb{R}} (\| f \|_1^{p/q}\int_{\mathbb{R}}| f(x-y) \| g(y) |^pdy) dx &\text{(by above)} \\ &=\| f \|_1^{p/q} \int_{\mathbb{R}}\int_{\mathbb{R}} | f(x-y) \| g(y)|^p dxdy &\text{(Fubini)} \\&=\| f \|_1^{p/q}\cdot\| f\|_1\cdot\| g \|_p^{p} \\&=\| f \|_1^{p}\cdot \| g \|_p^{p} \end{aligned}$$ which proves the other two statements. Last step is due to $p,q$ conjugate exponents $\implies \frac{1}{p} + \frac{1}{q} = 1$ $\implies q = \frac{p}{p-1}$ $\implies \frac{p}{q}+1 = p$.

    ### Part 2

    Examine the proof of Theorem 8.14 and part 1. If $p = 1$, the only inequality appears is that $$\int_{\mathbb{R}}| h(x) | dx \le \int_{\mathbb{R}}dx \int_{\mathbb{R}}| F(x,y) | dy,$$ and equality is attained as long as both $f, g$ are non-negative.

    If $p = \infty$, the inequalities appear are:

    1. $|\int_{\mathbb{R}}f(x-y)g(y)dy| \le \int_{\mathbb{R}}| f(x-y) \| g(y)| dy$, which attains equality again if $f,g$ are non-negative;
    2. $| g(y) | \le \| g \|_{\infty}$, which attains equality if $g$ is a constant.

    Put them together, in the $p = \infty$ case, equality is attained if $f$ is non-negative, and $g$ is a non-negative constant function.

    ### Part 3

    Examine the proof of part 2 of part 1, we can see the equality holds only if we have $$\begin{aligned}&\int_{\mathbb{R}}| f(x-y) |^{1/q} | f(x-y) |^{1/p} | g(y) | dy \\&= (\int_{\mathbb{R}}| f(x-y) | dy)^{1/q} (\int_{\mathbb{R}}| f(x-y) \| g(y)|^p dy)^{1/p},\end{aligned}$$ i.e. equality in Hölder holds, so we need to have, for almost all $x$ and almost all $y$: $$a(x)f(x-y) = b(x)f(x-y)g(y)^p$$ where $a(x), b(x)$ are numbers depending on $x$ that are not both zero. Fix an $x_0$ such that the equality holds for $x_0$ and almost all $y$:

    1. Suppose $a(x_0)$ and $b(x_0)$ are both non-zero, and suppose both $f,g$ are not $0$ a.e., then we can cancel things out and get $c = g(y)^p$ for some non-zero constant $c$, but then $g$ is not $L^p$;
    2. Suppose $b(x_0) = 0$, then $a(x_0)$ is not $0$, thus we need to have $f(x_0-y) = 0$ a.e., which implies $f = 0$ a.e.;
    3. Suppose $a(x_0) = 0$, then $b(x_0)$ is not $0$, then $f(x_0-y)g(y)^p = 0$ a.e., the only problematic case is that $f(x_0-y),g(y)$ both not $0$ a.e., but the intersection of the set where $f(x_0-y),g(y)$ attains non-zero values is of measure zero (for example, $f(x_0-y) = 0$ if $y \in (-\infty,0)$ and $g(y) = 0$ if $y \in(0,\infty)$).
    	Suppose this is the case, i.e. $f(x_0-y) \begin{cases}=0, y \in E\\\ne 0,y \in E'\end{cases}$ and $g(y) \begin{cases}=0, y \in E'\\\ne 0,y \in E\end{cases}$ for some $E, E'$ both of positive measure and $m(\mathbb{R}-E-E') = 0$. Pick any $x_1 \ne x_0$ (such that the equality in Hölder should hold), then $f(x_1 -y) \begin{cases}= 0, y \in E+x_1-x_0\\ \ne 0, y \in E'+x_1-x_0\end{cases}$. Apparently $(E'+x_1-x_0)\cap E = E_{x_1}$ has positive measure. Pick any $y \in E_{x_1}$, then by construction $f(x_1 - y)\ne 0$ and $g(y) \ne 0$. In particular, if we consider $a(x_1)f(x_1-y) = b(x_1)f(x_1-y)g(y)^p$, then $a(x_1) = b(x_1) g(y)^p$. Since $g(y) \ne 0$, $a(x_1) = 0$ if and only if $b(x_1) = 0$ (which shouldn't be the case), thus neither of them is zero, thus $g(y)^p \equiv c^p \implies g(y) \equiv c$ on $E_{x_1}$ for some non-zero constant $c$.
    	Now, remember this works for almost all $x_1 \in \mathbb{R}$. By choosing all the possible $x_1$'s, we should see that $g(y) = c$ for all $y$ in $E$ (because $\lbrace E_{x_1} | x_1 \in \mathbb{R} \rbrace$ covers $E$). If $m(E) = \infty$ then $g \notin L^p$ gives a contradiction. If not, do the same but change place of $f,g$, we get that $m(E') < \infty$ otherwise $f \notin L^1$. But then both $m(E),m(E')<\infty$, which is also impossible.

    ### Part 4

    1. Suppose $p = \infty$, we can take $f = \chi_{[0,1]}$ and $g = 1$, then $(f* g)(x) = \int_{\mathbb{R}}f(x-y)g(y)dy$ $=\int_{\mathbb{R}}f(x-y)dy$ $=\int_0^11dy$ $=1$ and $\| f \|_1 \| g \|_p = 1$ as well, thus $\| f * g \|_p > (1-\varepsilon)\| f \|_1\| g \|_p$ holds for any positive $\varepsilon$;
    2. Suppose $1 \le p < \infty$. Let $a$ be a positive real number to be defined, define $f = \frac{1}{2a}\chi_{[-a,a]}$, define $g = \sqrt[p]{\frac{1}{2}}\chi_{[-1,1]}$. Clearly $f$ is $L^1$ and $g$ is $L^p$. Also $\| f \|_1 = 1$ no matter which $a$ we choose, and $\| g \|_p = (\int_{-1}^1 \frac{1}{2} dx)^p = 1$.
    	By definition, $$\begin{aligned}(f * g )(x) &= \int_{-\infty}^{\infty}\frac{1}{2a}\chi_{[-a,a]}(x-y)\sqrt[p]{\frac{1}{2}}\chi_{[-1,1]}(y)dy \\ &=\frac{1}{2\sqrt[p]{2}a}\int_{-1}^1 \chi_{[-a,a]}(x-y)dy\end{aligned}$$ $\chi_{[-a,a]}(x-y) = 1$ if and only if $-a \le x - y \le a$ $\implies -a+x \le y \le a+x$, so it can be rewrite as $\chi_{[-a+x,a+x]}(y)$. The valuation of $(f* g)$ depends on the intersection of $[-a+x,a+x]$ and $[-1,1]$: $$(f* g)(x) = \begin{cases}0,&x\le -1-a\\ \frac{a+x+1}{2\sqrt[p]{2}a},&-1-a<x\le -1+a \\ \frac{2a}{2\sqrt[p]{2}a} = \frac{1}{\sqrt[p]{2}},&-1+a<x\le 1-a \\ \frac{1+a-x}{2\sqrt[p]{2}a},&1-a<x\le 1+a\\0,&x>1+a\end{cases}$$ We can calculate $$\begin{aligned}\| f* g \|_p^p &= \int_{\mathbb{R}}| f* g |^pdx \\ &=\int_{-1-a}^{-1+a}\frac{(a+x+1)^p}{2^{p+1}a^p}dx + \int_{-1+a}^{1-a}\frac{1}{2}dx + \int_{1-a}^{1+a}\frac{(1+a-x)^p}{2^{p+1}a^p}dx \\ &= \int_{-1-a}^{-1+a}\frac{(a+x+1)^p}{2^pa^p}dx + 1 - a\end{aligned}$$ Now take $a$ so that $a < 1-(1-\varepsilon)^p$, also notice $a+x+1>0$ for $-1-a < x \le -1+a$, then $\| f * g \|_p^p \ge 1-a > (1-\varepsilon)^p$, which gives $$\| f * g \|_p >(1-\varepsilon) = (1-\varepsilon)\| f \|_1\| g \|_p.$$

    ## Exercise 5

    **Let $M$ be the Banach space of all complex Borel measures on $\mathbb{R}$. The norm in $M$ is $\| \mu \| = | \mu | (\mathbb{R})$. Associate to each Borel set $E \subset \mathbb{R}$ the set $E_2 = \lbrace(x,y) | x+y \in E \rbrace \subset \mathbb{R}^2$. If $\mu$ and $\lambda \in M$, define their convolution $\mu * \lambda$ to be the set function given by** $$(\mu * \lambda)(E) = (\mu \times \lambda)(E_2)$$ **for every Borel set $E \subset \mathbb{R}$; $\mu \times \lambda$ is as in Definition 8.7**.

    1. **Prove that $\mu * \lambda \in M$ and that $\| \mu * \lambda \| \le \| \mu \| \| \lambda \|$**;
    2. **Prove that $\mu * \lambda$ is the unique $v \in M$ such that** $$\int f dv = \int \int f(x+y)d\mu(x)d\lambda(y)$$ **for every $f \in C_0(\mathbb{R})$ (all integrals extend over $\mathbb{R}$)**;
    3. **Prove that convolution in $M$ is commutative, associative, and distributive with respect to addition**;
    4. **Prove the formula** $$(\mu * \lambda)(E) = \int \mu(E -t)d\lambda(t)$$ **for every $\mu$ and $\lambda \in M$ and every Borel set $E$. Here $E - t = \lbrace x - t | x \in E \rbrace$**;
    5. **Define $\mu$ to be discrete if $\mu$ is concentrated on a countable set; define $\mu$ to be continuous if $\mu(\lbrace x \rbrace) = 0$ for every point $x \in \mathbb{R}$; let $m$ be Lebesgue measure on $\mathbb{R}$ (note that $m \notin M$). Prove that $\mu * \lambda$ is discrete if both $\mu$ and $\lambda$ are discrete, that $\mu * \lambda$ is continuous if $\mu$ is continuous and $\lambda \in M$, and that $\mu * \lambda \ll m$ if $\mu \ll m$**;
    6. **Assume $d\mu = f dm$, $d\lambda = gdm$, $f \in L^1(\mathbb{R})$, and $g \in L^1(\mathbb{R})$, and prove that $d(\mu * \lambda) = (f* g)dm$**;
    7. **Properties 1 and 3 show that the Banach space $M$ is what one calls a commutative Banach algebra. Show that part 5 and 6 imply that the set of all discrete measures in $M$ is a sub-algebra of $M$, that the continuous measures form an ideal in $M$, and that the absolutely continuous measures (relative to $m$) form an ideal in $M$ which is isomorphic (as an algebra) to $L^1(\mathbb{R})$**;
    8. **Show that $M$ has a unit, i.e. show that there exists a $\delta \in M$ such that $\delta * \mu = \mu$ for all $\mu \in M$**;
    9. **Only two properties of $\mathbb{R}$ have been used in this discussion: $\mathbb{R}$ is a commutative group under addition, and there exists a translation invariant Borel measure $m$ on $\mathbb{R}$ which is not identically $0$ and which is finite on all compact subsets of $\mathbb{R}$. Show that the same result hold if $\mathbb{R}$ is replaced by $\mathbb{R}^k$ or by $T$ (the unit circle) or by $T^k$ (the $k$-dimensional torus, the cartesian product of $k$ copies of $T$), as soon as the definitions are properly formulated**.

    Proof

    ### Part 1

    From the definition, $\mu * \lambda$ is defined on each Borel set, so we just need to check it is a measure (countable additivity). Suppose $\lbrace E^i \rbrace$ is a sequence of disjoint measurable set. Then $(\cup E^i)_2 = \lbrace (x,y) | x+y \in \cup E^i \rbrace$ $=\lbrace (x,y) | x+y \in E^i\text{ for some }i \rbrace$ $= \cup E_2^i$. Since $\mu \times \lambda$ is a measure (has countable additivity), $$\begin{aligned}(\mu * \lambda)(\cup E^i) &= (\mu \times \lambda)((\cup E^i)_2) \\&= (\mu \times \lambda)(\cup E^i_2)\\ &=\sum(\mu \times \lambda)(E_2^i) \\&=\sum(\mu * \lambda)(E^i)\end{aligned}$$ so does $\mu * \lambda$.

    Let $\lbrace E^i \rbrace$ be an arbitrary partition of $\mathbb{R}$ (notice then $E_2^i$'s are then disjoint), then $$\begin{aligned} |\mu*\lambda|(\mathbb{R}) &\le \sum| (\mu * \lambda)(E^i)| \\&=\sum | (\mu\times \lambda)(E^i_2)| \\& \le | \mu \times \lambda | (\mathbb{R}^2) &(*)\end{aligned}$$ Remember there exists $h_1, h_2$ (real) functions with $| h_1 | = | h_2 | =1$ (Radon-Nikodym) such that $d\mu = h_1d| \mu |$ and $d\lambda = h_2 d| \lambda |$. By definition of product of measure, we have: $$\begin{aligned}(\mu \times \lambda)(E_2) &= \int_{\mathbb{R}}\lambda(E_{2y})h_1(x)d|\mu| \\ &=\int_{\mathbb{R}}(\int_{\mathbb{R}}\chi_{E_2}h_2d| \lambda|) h_1d| \mu| \\ &= \int_{E_2}h_2h_1d(| \mu | \times | \lambda |)\end{aligned}$$ (last step is due to Fubini, it is applicable because we know $| \mu |$ and $| \lambda |$ are finite). Thus $$\begin{aligned}| \mu \times \lambda | (E_2) &= \int_{E_2}| h_2 h_1| d(| \mu | \times | \lambda |) \\&=\int_{E_2}1d(| \mu | \times | \lambda |) \\ &= (| \mu | \times | \lambda |)(E_2) \end{aligned}$$ thus the total variation of the product is the product of total variation. Go back to ($*$) we have $| \mu * \lambda |(\mathbb{R}) \le (| \mu| \times | \lambda |) (\mathbb{R}^2)$ and result follows.

    ### Part 2

    First we proof $\mu * \lambda$ is such a measure. Let $E$ be a (Borel) measurable set, then we have: $$\begin{aligned}\int_{\mathbb{R}}\chi_E(x)d(\mu * \lambda) &= (\mu * \lambda)(E) \\ &= (\mu \times \lambda)(E_2) \\ &= \int_{\mathbb{R}}\lambda(E_{2x})d\mu(x) \\ &= \int_{\mathbb{R}} \int_{\mathbb{R}}\chi_E(x+y)d\lambda(y) d\mu(x) \\ &= \int_{\mathbb{R}} \int_{\mathbb{R}}\chi_E(x+y)d\mu(x) d\lambda(y)\end{aligned}$$ so $\mu * \lambda$ satisfies the condition with characteristic functions on Borel set, thus with simple functions, thus with Borel measurable functions, and thus with $f \in C_0(\mathbb{R})$.

    By Riesz Representation Theorem, this measure is unique.

    ### Part 3

    1. Commutative: $$\begin{aligned}\int_{\mathbb{R}}fd(\mu * \lambda) &= \int_{\mathbb{R}}\int_{\mathbb{R}}f(x+y)d\mu d\lambda \\&= \int_{\mathbb{R}} \int_{\mathbb{R}}f(y+x)d\lambda d\mu \\&= \int_{\mathbb{R}}fd(\lambda * \mu)\end{aligned}$$
    2. Associativity: $$\begin{aligned}\int_{\mathbb{R}}fd((\mu* \lambda)* \delta) &= \int_{\mathbb{R}} \int_{\mathbb{R}}\int_{\mathbb{R}}f(x+y+z)d\mu(x)d\lambda(y)d\delta(z) \\ \int_{\mathbb{R}}fd(\mu* (\lambda* \delta)) &= \int_{\mathbb{R}}(\int_{\mathbb{R}}f(x+w)d\mu(x))d(\lambda*\delta)(w) \\&=\int_{\mathbb{R}}\int_{\mathbb{R}}\int_{\mathbb{R}}f(x+y+z)d\mu(x)d\lambda(y)d\delta(z)\end{aligned}$$ so they are equal;
    3. Distributivity: $$\begin{aligned}\int_{\mathbb{R}}fd(\mu *(\lambda + \delta)) &= \int_{\mathbb{R}}\int_{\mathbb{R}}f(x+y)d\mu(x)d(\lambda(y)+\delta(y)) \\ &= \int_{\mathbb{R}}\int_{\mathbb{R}}f(x+y)d\mu d\lambda + \int_{\mathbb{R}}\int_{\mathbb{R}}f(x+y)d\mu d\delta\\&=\int_{\mathbb{R}}fd(\mu* \lambda)+\int_{\mathbb{R}}fd(\mu*\delta) \\&=\int_{\mathbb{R}}fd(\mu* \lambda + \mu * \delta)\end{aligned}$$

    ### Part 4

    By definition we have: $$(\mu * \lambda)(E) = (\mu\times \lambda)(E_2) = \int_{\mathbb{R}}\mu(E_2^y)d\lambda(y) = \int_{\mathbb{R}}\int_{E_2^y}d\mu(x)d\lambda(y).$$ Notice now $$E_2^y:= \lbrace x | (x,y) \in E_2\rbrace = \lbrace x | x+y \in E \rbrace = \lbrace x-y | x \in E \rbrace = E-y.$$ So $$(\mu * \lambda)(E) = \int_{\mathbb{R}}\int_{E_2^y}d\mu(x)d\lambda(y) = \int_{\mathbb{R}}\int_{E-y}d\mu d\lambda = \int_{\mathbb{R}}\mu(E-y)d\lambda(y)$$ as desired.

    ### Part 5

    1. Suppose $\mu, \lambda$ concentrate on countable sets $A, B$, then $A \cup B = C$ is also countable, I claim that $\mu * \lambda$ concentrate on $C$: Let $E$ be any Borel set disjoint from $C$, then $$\mu * \lambda(E) = \int_{\mathbb{R}}\mu(E-y)d\lambda(y).$$ Now if $y \in C$ then $E-y$ is disjoint from $C$ thus disjoint from $A$, thus $\mu(E - y) = 0$, and if $y \notin C$ then $y \notin B$ thus $\lambda(y) = 0$, so the integral equals $0$, result follows;
    2. Suppose $\mu$ is continuous and $\lambda \in M$, then for any $x \in \mathbb{R}$ we have $$\begin{aligned}(\mu * \lambda)(\lbrace x \rbrace) &= \int_{\mathbb{R}}\mu(\lbrace x \rbrace - t)d\lambda(t) \\ &= \int_{\mathbb{R}}\mu(\lbrace x - t \rbrace)d\lambda(t) \\ &= \int_{\mathbb{R}} 0 d\lambda(t) = 0 &\text{(because }\mu \text{ is continuous)}\end{aligned}$$ thus $\mu * \lambda$ is continuous;
    3. Suppose $\mu\ll m$, let $E$ be an arbitrary Borel set that has $m(E) = 0$. Then $m(E-t) = 0$ for all $t$ thus $\mu(E-t) = 0$ for all $t$. Thus $$(\mu * \lambda)(E) = \int_{\mathbb{R}}\mu(E-t)d\lambda(t) = \int_{\mathbb{R}}0d\lambda = 0$$ thus $\mu*\lambda \ll m$.

    ### Part 6

    We have $$\int_{\mathbb{R}}d(\mu* \lambda) = \int_{\mathbb{R}}\int_{\mathbb{R}}d\mu d\lambda = \int_{\mathbb{R}}\int_{\mathbb{R}}f(x)dm(x) g(y)dm(y)$$ by translate invariance, we get $$\begin{aligned}… &= \int_{\mathbb{R}}\int_{\mathbb{R}}f(x-y)g(y)dm(x)dm(y) \\ &= \int_{\mathbb{R}}(f* g)dm(y)\end{aligned}$$ which exactly means $d(\mu * \lambda) = (f* g)dm$.

    ### Part 8

    Consider the measure $\delta$ defined as $\delta(E) = \begin{cases}1,0\in E\\0,0\notin E\end{cases}$. Apparently this is a complex Borel measure. Let $E$ be an arbitrary Borel set, and $\mu \in M$ be an arbitrary Borel measure, then $$(\delta*\mu)(E) = \int_{\mathbb{R}}\delta(E-t)d\mu(t) = \int_E 1 d\mu(t) = \mu(E)$$ because $\delta(E-t) = 1$ if and only if $t \in E$ so that $0 \in E-t$, which proves $\delta * \mu = \mu$ for any $\mu$ as desired.

    ## Exercise 11

    **Let $\mathscr{B}_k$ be the $\sigma$-algebra of all Borel sets in $\mathbb{R}_k$. Prove that $\mathscr{B}_{m+n} = \mathscr{B}_m \times \mathscr{B}_n$. This is relevant in Theorem 8.14**.

    Proof

    We know $\mathbb{R}_k$ is second-countable, i.e. the open sets are generated by a countable collection $\mathcal{B}_k$. Then $\mathbb{R_{m+n}}$ has a basis $\mathcal{B}_{m+n} = \lbrace B_m \times B_n | B_m \in \mathcal{B}_m, B_n \in \mathcal{B}_n \rbrace$ which is countable.

    Suppose we have an open set in $\mathbb{R_{m+n}}$, then it is a countable union of elements of $\mathcal{B}_{m+n}$, thus it is an open set in $\mathbb{R}_m \times \mathbb{R}_n$ thus it is in $\mathscr{B}_m \times \mathscr{B}_n$. Since $\mathscr{B}_m \times \mathscr{B}_n$ is a $\sigma$-algebra, we have $\mathscr{B}_{m+n} \subseteq \mathscr{B}_m \times \mathscr{B}_n$.

    Suppose now $U$ is an open set in $\mathbb{R}_m$ and $V$ is an open set in $\mathbb{R}_n$, then $U \times \mathbb{R}_n$ and $\mathbb{R}_m \times V$ are open sets in $\mathbb{R}_{m+n}$, thus $U \times V = (U \times \mathbb{R}_n) \cap (\mathbb{R}_m \times V)$ is open in $\mathbb{R}_{m+n}$ thus in $\mathscr{B}_{m+n}$. Since $\mathscr{B}_{m+n}$ is a $\sigma$-algebra, we have the other inclusion.

    ## Exercise 12

    **Use Fubini's Theorem and the relation** $$\frac{1}{x} = \int_0^{\infty}e^{-xt}dt, x > 0$$ **to prove that** $$\lim_{A \to \infty}\int_0^A\frac{\sin(x)}{x}dx = \frac{\pi}{2}.$$

    Proof

    Let $f = \sin(x)\cdot e^{-xt}$, it is continuous thus Borel. By the given relation we have $$\begin{aligned}\int_0^A\frac{\sin(x)}{x}dx &= \int_0^A\sin(x)(\int_0^{\infty}e^{-xt}dt)dx \\ &= \int_0^A\int_0^{\infty}\sin(x)~e^{-xt}dtdx\\ &= \int_0^{\infty}\int_0^{A}\sin(x)~e^{-xt}dxdt &\text{(Fubini)}\\ &= \int_0^{\infty} \frac{1}{t^2+1} - \frac{e^{-At}(t\sin(A)+\cos(A))}{t^2+1}dt \\ &= \frac{\pi}{2} - \int_0^{\infty} \frac{e^{-At}(t\sin(A)+\cos(A))}{t^2+1}dt\end{aligned}$$ by evaluating the usual Riemann integral. Now for any $A$, $$\begin{aligned}| \frac{e^{-At}(t\sin(A)+\cos(A))}{t^2+1} | &\le |\frac{e^{-At}(1+t)}{t^2+1} | \\ &\le |\frac{e^{-At}}{t^2+1} | + |\frac{e^{-At}t}{t^2+1} | \\ &\le 2e^{-At}\end{aligned}$$ $$\lim_{A \to \infty}\int_0^{\infty}\frac{e^{At}(t\sin(A)+\cos(A))}{t^2+1}dt = \int_0^{\infty}0dt = 0.$$

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Spring Semester Homework 5""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 1

    **Suppose $f \in L^1$, $f>0$. Prove that $| \hat{f}(y) | < \hat{f}(0)$ for all $y \ne 0$**.

    Proof

    Use the fact that $| e^{ix} | = 1$ for any $x$, we get $| f(x) e^{-ixy} | = | f(x) | = f(x)$ (because $f$ is positive), and: $$| \hat{f}(y) | = | \int_{-\infty}^{\infty}f(x)e^{-ixy}dx | \le \int_{-\infty}^{\infty}| f(x)e^{-ixy} | dx = \int_{-\infty}^{\infty}f(x) dx = \hat{f}(0).$$ If there is some $y \ne 0$ with$| \hat{f}(y) | = \hat{f}(0)$, then the equality in above inequality holds. From chapter 1 we know this means there is a constant $a$ such that $af(x)e^{-ixy} = | f(x)e^{-ixy}| = f(x)$ a.e.. Since $f(x) \ne 0$ we can cancel it and get $a e^{-ixy} = 1$ a.e., but that is only possible when $e^{-ixy}$ is a constant a.e. (w.r.t. $x$), which only happens if $y = 0$. So if $y \ne 0$ we cannot have equality, and we have desired statement.

    ## Exercise 2

    **Compute the Fourier transform of the characteristic function of an interval. For $n = 1,2,3,\dots$, let $g_n$ be the characteristic function of $[-n,n]$, let $h$ be the characteristic function of $[-1,1]$, and compute $g_n * h$ explicitly (the graph is piece-wise linear). Show that $g_n * h$ is the Fourier transform of a function $f_n \in L^1$; except for a multiplicative constant,** $$f_n(x) = \frac{\sin(x)\sin(nx)}{x^2}.$$ **Show that $\| f_n \|_1 \to \infty$ and conclude that the mapping $f \to \hat{f}$ maps $L^1$ into a proper subset of $C_0$**.

    Solution

    Consider an interval $[a,b]$ and the characteristic function $\chi = \chi_{[a,b]}$, then follow definition, $$\begin{aligned}\hat{\chi}(t) &= \int_{-\infty}^{\infty} \chi(x) e^{-ixt} dx \\ &= \int^{b}_{a}e^{-ixt}dx \\ &= \begin{cases} -\frac{1}{it}(e^{-i b t} - e^{-iat}), & t \ne 0, \\ b - a, & t = 0. \end{cases}\end{aligned}$$ For obvious reason, characteristic function of half open interval or open interval has the same transformation. In particular if $a = -b$, or say the interval is of the form $[-n,n]$, then by property of complex number, we have $$\widehat{\chi_{[-n,n]}}(t) = \begin{cases} \frac{2 \sin(nt)}{t}, &t = 0,\\2n,&t \ne 0.\end{cases}$$ Or simply $$\widehat{\chi_{[-n,n]}}(t) = \frac{2 \sin(nt)}{t}$$ because the limit agrees.

    Let $g_n$ and $h$ be as given, we have: $$\begin{aligned}(g_n * h)(x) &= \int_{-\infty}^{\infty}\chi_{[-n,n]}(x-y)\chi_{[-1,1]}(y)dy \\ &=\int_{-1}^1\chi_{[-n,n]}(x-y)dy \\&=m([-1+x, 1+x] \cap [-n,n])\end{aligned}$$ Notice it is bounded above by $2$.

    $f_n \in L^1$ because on $[-1,1]$ it is bounded by $n$ and otherwise its absolute value is bounded by $\frac{1}{x^2}$ which is a well-known $L^1$ function. Also $g_n$ and $h$ are both $L^1$, and we have $\widehat{g * h} = \hat{g_n}\cdot \hat{h}$. Use the formula we had above, we get: $$(\widehat{g_n * h})(t) = \frac{4\sin(nt)\sin(t)}{t^2}$$ which is $4f_n(t)$. Notice $f_n$ is even function, so $f_n(t) = f_n(-t)$, we have: $$\begin{aligned}\hat{f_n}(t)= \hat{f_n}(-t) &= \int_{-\infty}^{\infty}f_n(-x)e^{ixt}dx \\&= \int f_n(x)e^{ixt} dx\\&=\frac{1}{4}\int \widehat{g_n * h}(x)e^{ixt}dx  \end{aligned}$$ The condition of the Inversion Theorem is satisfied, and we have $4\hat{f_n}(t) = (g_n* h)(t)$ a.e., i.e. $g_n* h$ is the Fourier transformation of $f_n$ up to a constant.

    We can write $$\| f_n \|_1 = \int_{-\infty}^{\infty}|\frac{\sin(x)}{x}| \cdot|\frac{\sin(nx)}{x}| dx.$$ Pick arbitrary $c \in (0,1)$, it is easy to see we can find an interval $[0,a]$ for certain $a$ such that $\frac{\sin(x)}{x} > c$ whenever $x \in [0,a]$. It follows that if we can show $$\lim_{n \to \infty}\int_0^a | \frac{\sin(nx)}{x} | dx = \infty$$ then $\| f_n \|_1$ also goes to infinity because it is greater than the above expression up to a multiplication of constant. But $$\lim_{n \to \infty}\int_0^a | \frac{\sin(nx)}{x} | dx =^{u = nx} \lim_{n}\int_0^{an}|\frac{\sin(u)}{u} | du = \int_{0}^{\infty}| \frac{\sin(u)}{u} | du$$ which is well-known to be infinite, so we are finished.

    The final assertion was proved in the book (Theorem 5.15) for $T$, follow that proof, the connection here is that if this function is (injective and) surjective then there is a $\delta > 0$ such that $\| \hat{f} \|_{\infty} \ge \delta \| f \|_1$ for every $f \in L^1$, but with the above example we have $$\| \hat{f_n} \|_{\infty} = \| g_n * h \|_{\infty} = 2$$ yet $\| f \|_1 \to \infty$, so such $\delta$ cannot exist.

    ## Exercise 3

    **Find** $$\lim_{A\to \infty}\int_{-A}^A\frac{\sin(\lambda t)}{t}e^{itx}dt, (-\infty < x < \infty)$$ **where $\lambda$ is a positive constant**.

    Solution

    Remember we have that if $g = \chi_{[-\lambda, \lambda]}$ then $\hat{g} = 2\frac{\sin(\lambda t)}{t}$. However $\hat{g}$ is $L^2$ yet not $L^1$ so the Inversion Theorem is not applicable. We can only use Inversion Theorem for $L^2$ function and get that $$\psi_A(x) = 2\int_{-A}^A\frac{\sin(\lambda t)}{t}e^{ixt}dt$$ with $\| \psi_A - g \|_2 \to 0$. Write explicitly: $$\| \int_{-A}^A\frac{\sin(\lambda t)}{t}e^{ixt}dt - \frac{1}{2}\chi_{[-\lambda, \lambda]} \|_2 \to 0,$$ if we only consider $A \in \mathbb{Z}$ then this means that $\lbrace\int_{-A}^A\frac{\sin(\lambda t)}{t}e^{ixt}dt\rbrace$ has subsequence converges point-wise to $\frac{1}{2}\chi_{[-\lambda, \lambda]}$ a.e..

    ## Exercise 4

    **Give examples of $f \in L^2$ such that $f \notin L^1$ but $\hat{f} \in L^1$. Under what circumstances can this happen**?

    Solution

    First, the underlying space must not be compact, otherwise $L^2 \subset L^1$. One possible circumstance is that suppose we have some $g \in L^2 \cap L^1$ and $\hat{g}$ not in $L^1$, then $\hat{g} \in L^2$ (Theorem 9.13). Then if we define $f(x)$ to be $\hat{g}(-x)$ then $f$ satisfies the condition. Proof:

    1. $f \in L^2$ and $f \notin L^1$ are immediate from construction;
    2. Notice we have $\hat{\hat{g}}(x) = g(-x)$ a.e.. Since $f(x) = \hat{g}(-x)$ we get $\hat{f}(x) = \hat{\hat{g}}(-x) = g(x)$, so $\hat{f}$ is $L^1$.

    Now consider $g = \chi_{[-1,1]}$, it is in $L^2 \cap L^1$. By above exercise we know $\hat{g}(x) = \frac{2\sin(x)}{x}$, which is not an $L^1$ function, so if we define $f(x) = \hat{g}(-x) = \frac{2\sin(x)}{x}$ (sine is odd function) then it is an example we want.

    ## Exercise 8

    **If $p$ and $q$ are conjugate exponents, $f \in L^p$, $g \in L^q$, and $h = f * g$, prove that $h$ is uniformly continuous. If also $1 < p < \infty$, then $h \in C_0$; show that this fails for some $f \in L^1, g \in L^{\infty}$**.

    Proof

    Let $p,q$ be conjugate exponents, fix arbitrary $x \in \mathbb{R}$ and let $a \in \mathbb{R}$, then $$\begin{aligned} | h(x-a) - h(x) | & = | \int_{-\infty}^{\infty} f(x-a-y)g(y) dy - \int_{-\infty}^{\infty} f(x-y)g(y)dy| \\&= | \int_{-\infty}^{\infty} f(x-y)g(y-a) dy - \int_{-\infty}^{\infty} f(x-y)g(y)dy| \\ &= | \int_{-\infty}^{\infty}f(x-y)(g(y-a) - g(y))dy | \\ &\le \int_{-\infty}^{\infty}| f(x-y) | \cdot| (g(y-a) - g(y))| dy \\&\le (\int_{-\infty}^{\infty}| f(x-y) |^pdy)^{1/p}(\int_{-\infty}^{\infty}| g(y-a) - g(y) |^qdy)^{1/q}\end{aligned}$$ The last step is due to Hölder. Since $g$ is $L^q$, $g'(y) = g(y-a) - g(y)$ is also $L^q$, in conclusion we have $$| h(x-a) - h(x) | \le \| f \|_p \| g' \|_q < \infty.$$ In particular, for any given $\varepsilon choose $\delta > 0$ so that $\| g' \|_q < \varepsilon/\| f \|_p$ whenever $| a | < \delta$ (this is apparently doable, because $g(y-a) \to g(y)$ with respect to $L^q$ norm when $a \to 0$), then $| h(x-a) - h(x) | < \varepsilon$. Since $a$ does not depend on $x$, we have uniform continuity.

    Suppose now $1 < p,q < \infty$. We know that $C_C(\mathbb{R})$ is dense in $L^p$ and $L^q$ (and it fails to the $L^{\infty}$ case, so this argument does not apply to $p = 1, q =\infty$ at this very beginning). So choose sequences $f_n$ and $g_n$ so that $f_n \to f$ and $g_n \to g$ with respect to $L^p$ and $L^q$ norm respectively. For each $n$, denote $h_n = f_n * g_n$. First we will show that $h_n$ is continuous and compact supported, and then we show $h_n \to h$ with respect to the $\sup$ norm. Since we know $C_0$ is completion of $C_C$, these would imply that $h$ is in $C_0$:

    1. First we fix $n$ and show $h_n$ is continuous and compact supported:

    	Since $f_n$ is continuous and compact supported, it is uniformly continuous. Fix $\varepsilon > 0$, choose $\delta > 0$ so that $| f_n(x) - f_n(y) | < \varepsilon$ whenever $| x - y | < \delta$, then $$| h_n(x) - h_n(y) | \le \int_{-\infty}^{\infty}| f_n(x-z)- f_n(y-z) | \cdot | g_n(z) | dz \le \varepsilon \int_{-\infty}^{\infty}| g_n(z) | dz,$$ now use the fact that $g_n$ is a compact supported function, we can conclude that $\int_{-\infty}^{\infty}| g_n(z) | dz$ is finite thus the above quantity goes to $0$ as $\varepsilon \to 0$, which proves (uniform) continuity of $h_n$.
	
    	Choose $M$ large enough so that support of $f_n$ and $g_n$ both lie in $[-M, M]$, then for any $x$ so that $| x | > 2M$, if $y \in [-M, M]$ then $x - y \notin [-M, M]$. This implies that for $| x | > 2M$, we have $f_n(x-y) g_n(y) = 0$ for any $y$, which means $h_n(x) = 0$, meaning that the support of $h_n$ lie inside $[-2M, 2M]$ thus is bounded thus compact, thus $h_n$ is compact supported;
    2. Now we show $h_n \to h$ with respect to the $\sup$ norm. We have: $$\begin{aligned} | h_n(x) - h(x) | &\le | h_n(x) - (f_n * g)(x) | + | (f_n* g)(x) - h(x) | \\&=| (f_n * (g_n - g))(x) | + | ((f_n-f)* g)(x) | \\ & \le \| f_n \|_p\| g_n - g \|_q + \| f_n - f \|_p \| g \|_q &(*) \\ &\to 0 \end{aligned}$$ where ($*$) comes from Holder (say $f \in L^p$ and $g \in L^q$): $$\begin{aligned} | (f * g ) (x)| &= | \int f(x-y)g(y)dy| \\ &\le \int | f(x-y) \| g(y) | dy \\ &\le (\int | f(x-y) |^p dy)^{1/p}(\int | g(y) |^q dy)^{1/q} \\ &= \| f \|_p \| g \|_q\end{aligned}$$ This proves convergence, and by the argument above, we finish the proof.

    For $p = 1$ and $q = \infty$: consider $f = \chi_{[-1,1]}$ and $g \equiv 1$ (which is $L^{\infty}$ but is not $L^q$ for any finite $1 \le q < \infty$), then $h(x) := \int \chi_{[-1,1]}(x-y) dy \equiv 2$ so $h \notin C_0$.

    ## Exercise 9

    **Suppose $1 \le p < \infty$, $f \in L^p$, and** $$g(x) = \int_x^{x+1}f(t)dt.$$ **Prove that $g \in C_0$. What can you say about $g$ if $f \in L^{\infty}$**?

    Proof

    First we need to show $g$ is continuous. Write $g(x) = \int_0^1f(x+t)dt$ and denote $f(x+t)$ as $f_x(t)$. Then $| g(x) - g(y) | = | \int_0^1f_xdt - \int_0^1 f_ydt |$ $\le \int_0^1| f_x - f_y | dt$ $\le (\int_0^1 1^qdt)^{1/q} \cdot (\int_0^1| f_x - f_y |^p)^{1/p}$ $= \| f_x - f_y \|_p$. By Theorem 9.5, $x \mapsto f_x$ is uniformly continuous, thus $g$ is also (uniformly) continuous.

    If $g \notin C_0$, then by definition there is some $\varepsilon > 0$ so that there is no compact set $K \subset \mathbb{R}$ with $| g(x) | < \varepsilon$ for all $x$ outside $K$. In particular, there is a sequence $\lbrace x_n \rbrace$, which we may choose to have $x_1 > 0$ and $x_n - x_{n-1} > 1$ for all $n$, and $| g(x_n) | \ge \varepsilon$ for any $n$. But then $$\int_{-\infty}^{\infty}| f(t) | ^pdt \ge \sum_n \int_{x_n}^{x_n+1}| f(t) |^pdt \ge \sum_n \varepsilon^p = \infty$$ so $f$ is not $L^p$ for any $1 \le p < \infty$. This proves the negation thus the original statement.

    If $f \in L^{\infty}$ then $g$ may not be $C_0$ (just take $f \equiv 1$ then $g \equiv 1$ as well). We could have that $$\begin{aligned}| g(x) | &= | \int_x^{x+1}f(t)dt | \le \int_x^{x+1} | f(t) | dt  \\ &\le\int_x^{x+1}\| f \|_{\infty}dt \\ &= \| f \|_{\infty}\end{aligned}$$ (because $\| f \|_{\infty}$ is independent of $x$), so $g$ is $L^{\infty}$ and $\| g \|_{\infty}$ is bounded by $\| f \|_{\infty}$.

    Also $g \in \text{Lip}~1$: $$\begin{aligned}| g(x) - g(y) | &= | \int_x^{x+1}fdt - \int_{y}^{y+1}fdt | \\ & \le | \int_{y+1}^{x+1}fdt | + | \int_x^yfdt| &(1)\\ & \le 2\| f \|_{\infty}| xy |.\end{aligned}$$ (in fact if $f \in L^p$ then $g \in \text{Lip}~\alpha$ for $\alpha = 1/q$ for $p$ other than $\infty$ as well: continue from $(1)$ above, apply Holder and we get $| g(x) - g(y) | \le 2\| f \|_p | x-y|^{1/q}$)

    ## Exercise 10

    1. **Let $C^{\infty}$ be the class of all infinitely differentiable complex functions on $\mathbb{R}$, and let $C_C^{\infty}$ consist of all $g \in C^{\infty}$ whose supports are compact. Show that $C_C^{\infty}$ does not consists of $0$ alone**;
    2. **Let $L^1_{loc}$ be the class of all $f$ belong to $L^1$ locally; that is, $f \in L^1_{loc}$ provided that $f$ is measurable and $\int_I| f | < \infty$ for every bounded interval $I$. If $f \in L^1_{loc}$ and $g \in C_C^{\infty}$, prove that $f * g \in C^{\infty}$**;
    3. **Prove that there are sequences $\lbrace g_n \rbrace$ in $C^{\infty}_C$ such that** $$\| f* g_n - f \|_1 \to 0$$ **as $n \to \infty$, for every $f \in L^1$ (compare Theorem 9.10). Prove that $\lbrace g_n \rbrace$ can also be so chosen that $(f* g_n)(x) \to f(x)$ a.e., for every $f \in L_{loc}^1$; in fact, for suitable $\lbrace g_n \rbrace$ the convergence occurs at every point $x$ at which $f$ is the derivative of its indefinite integral**.

    Proof

    ### Part 1

    A famous example is $\Psi(x) = \begin{cases} e^{-\frac{1}{1-x^2}},&x \in (-1,1)\\ 0,&\text{otherwise}\end{cases}$. It is smooth and clearly compact supported, i.e. it is a non-trivial member of $C_C^{\infty}$. It is so called the 'bump function'.

    ### Part 2

    Since $g \in C_C^{\infty}$, let us assume support of $g$ is contained in some interval $[-M, M]$ (which is apparently bounded). First, $$(f * g)(x) = \int_{-\infty}^{\infty}f(x-y)g(y)dy = \int_{-M}^M f(x-y)g(y)dy$$ where by assumption of $f$, on this interval $f$ is bounded, and $g$ is continuous on this compact interval thus also bounded, so the above quantity is bounded, which means $f* g$ is well-defined.

    Now we claim that $(f * g)' = f * g'$, if we prove this claim then it is not hard to see $g'$ is also in $C_C^{\infty}$ (because whenever $g = 0$, $g'$ has to be $0$), thus $(f* g)^{(n)} = f * g^{(n)}$ which proves $f * g$ is infinitely differentiable thus in $C^{\infty}$. Proof is as following:

    First we have (let $h$ be a number): $$\begin{aligned} \frac{(f* g)(x+h) - (f* g)(x)}{h} &= \frac{1}{h} (\int_{-M}^Mf(x+h-y)g(y)dy - \int_{-M}^Mf(x-y)g(y)dy) \\ &= \frac{1}{h} (\int_{-M+x+h}^{M+x+h}f(y)g(x+h-y)dy - \int_{-M+x}^{M+x}f(y)g(x-y)dy) \\ &= \frac{1}{h} (\int_{-M+x}^{M+x}f(y)g(x+h-y)dy - \int_{-M+x}^{M+x}f(y)g(x-y)dy) \\ &= \int_{-M+x}^{M+x}f(y)\cdot\frac{g(x+h-y)-g(x-y)}{h}dy\end{aligned}$$ (using the fact that $g$ is $0$ outside of $[-M,M]$, change of variable, and translate invariant). Now we send $h \to 0$, then the LHS is by definition $(f * g)'(x)$, and RHS is $$\lim_{h \to 0}\int_{-M+x}^{M+x}f(y)\cdot\frac{g(x+h-y)-g(x-y)}{h}dy.$$ If we view the integrant as a sequence of function indexed on $h$, it is dominated by some $L^1$ function: $f$ is in $L^{loc}_1$, and the expression with $g$ is dominated by some constant (on a bounded interval thus $L^1$) because $g$ is uniformly continuous and differentiable thus the derivative is bounded. Thus by Lebesgue Dominated Convergence Theorem we can interchange the $\lim$ and $\int$ operators and get: $$\begin{aligned}(f* g)'(x) &= \int_{-M+x}^{M+x}\lim_{h \to 0}\frac{g(x-y+h) - g(x-y)}{h}f(y)dy \\ &= \int_{-M+x}^{M+x}g'(x-y) f(y) dy \\& = (g'* f)(x) = (f* g')(x)\end{aligned}$$ as claimed.

    ### Part 3

    Consider the about bump function, rescale so that we assume $\int_{-1}^1\Psi(x)dx = 1$. For each $\varepsilon0$, define $\Psi_{\varepsilon}(x) = \frac{\Psi(x/\varepsilon)}{\varepsilon}$, it is not hard to see $\Psi_{\varepsilon}$ is in $C_C^{\infty}$, supported in $[-\varepsilon,\varepsilon]$, and have $L^1$ norm $=1$. We have: $$\begin{aligned} \| f * \Psi_{\varepsilon} - f \|_1 &= \int_{-\infty}^{\infty}| (f * \Psi_{\varepsilon})(x) - f(x)| dx \\ &= \int_{-\infty}^{\infty}| \int_{-\infty}^{\infty} (f(x-y) - f(x))\Psi_{\varepsilon}(y) dy | dx  \\ &= \int_{-\infty}^{\infty} | \int_{-\infty}^{\infty} (f(x-y) - f(x)) \frac{\Psi(y/\varepsilon)}{\varepsilon}dy | dx \\ &=^{z = y/\varepsilon} \int_{-\infty}^{\infty} | \int_{-\infty}^{\infty}(f(x-\varepsilon z)- f(x))\Psi(z)dz | dx \\ &\le  \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} | f(x-\varepsilon z) - f(x) \| \Psi(z) | dzdx \\ &= \int_{-\infty}^{\infty}\int_{-\infty}^{\infty} | f(x - \varepsilon z) - f(x) \| \Psi(z) | dxdz \\ &= \int_{-\infty}^{\infty} \| f_{\varepsilon z} - f \|_1 | \Psi(z) | dz\end{aligned}$$ Prove that $(f* h_{\lambda})(x) \to f(x)$ a.e. if $f \in L^1$, as $\lambda \to 0$, and that $f * h_{\lambda} \in C^{\infty}$, although $h_{\lambda}$ does not have compact support ($h_{\lambda}$ as defined in Section 9.7).

    """
    )
    return


if __name__ == "__main__":
    app.run()
