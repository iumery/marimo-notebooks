import marimo

__generated_with = "0.15.4"
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
    mo.md(r"""# Fall Semester Homework 01""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Problem 1

    **Construct an explicit deformation retraction of the torus with one point deleted onto a graph consisting of two circles intersecting in a point, namely, longitude and meridian circles of the torus**.

    Solution

    Consider the plane model of the torus, that is the square $I \times I$ with opposite side identified. This space is homeomorphic to a disk with its boundary divided into four pieces and identified. Remove a point from the space (say the origin). Call the resulting space $X$.

    Consider $A \subseteq X$ consisting of the points $\| x \| = 1$ and with the same identification. $A$ is (homeomorphic to) two circles intersecting at a point.

    <img src="public/Pasted image 20221231121241.png" width="600" />

    Now define $f_0 = \text{id}_X$; for each $t \in I$, define $f_t(x) = t\frac{x}{\| x \|}+(1-t)x$, then $f_1(X) = A$, $f_t | A = \text{id}_A$ for each $A$, and the family $f_t$ is continuous. Thus $\lbrace f_t \rbrace$ give us a desired deformation retraction.

    ## Problem 2

    **Construct an explicit deformation retraction of $\mathbb{R}^n - \lbrace 0 \rbrace$ onto $S^{n-1}$**.

    Solution

    The same family $f_t$ in the first problem works here, only difference is now $X$ is $\mathbb{R}^n - \lbrace 0 \rbrace$.

    ## Problem 3

    1. **Show that the composition of homotopy equivalences $X \to Y$ and $Y \to Z$ is a homotopy equivalence $X \to Z$. Deduce that homotopy equivalence is an equivalence relation**;
    2. **Show that the relation of homotopy among maps $X \to Y$ is an equivalence relation**;
    3. **Show that a map homotopic to a homotopy equivalence is a homotopy equivalence**.

    Proof

    1. We will use a lemma: $f \simeq \tilde{f}$ implies that $f \circ g \simeq \tilde{f} \circ g$ and the other way of composition, for any $g$ such that the compositions make sense.
        Proof of the lemma: By assumption we have a map $F(x,t)$ that is the homotopy between $f$ and $\tilde{f}$, now consider the map $F \circ (g \times \text{id}_I): Y \times I \to Y$: it is continuous, $F\circ(g \times \text{id}_I)(x, 0) = F(g, 0)$ $=f(g)$ $=f \circ g$, and $F\circ (g \times \text{id}_I)(x,1) = \tilde{f}\circ g$. Thus it is a homotopy and $f \circ g \simeq \tilde{f} \circ g$. Similarly, with the function $g \circ F: X \times I \to X$ we have $g \circ f \simeq g \circ \tilde{f}$.
        Back to the problem. Suppose $f: X \to Y$ and $g: Y \to Z$ are the corresponding homotopy equivalence. That is, there exist $\tilde{f}: Y \to X$ and $\tilde{g}: Z \to Y$ such that $f\circ \tilde{f}$, $\tilde{f} \circ f$, $g \circ \tilde{g}$ and $\tilde{g}\circ g$ are all homotopic to identity maps.
        To prove $g \circ f$ is a homotopy equivalence, we need to find a function $h$ satisfies that $(g \circ f) \circ h \simeq \text{id}$ and $h \simeq (g \circ f) \simeq \text{id}$.
        Consider the map $\tilde{f} \circ \tilde{g}$, we have $g \circ f \circ \tilde{f} \circ \tilde{g}$ $= g \circ (f \circ \tilde{f}) \circ \tilde{g}$ (composition of functions is associative) $\simeq g \circ \text{id}_Y \circ \tilde{g}$ (by above lemma) $= g \circ \tilde{g}$ $=\text{id}_Z$; and similarly, $(\tilde{f} \circ \tilde{g})\circ(g \circ f)$ $\simeq \text{id}_X$. Thus by definition, $g\circ f$ is a homotopy equivalence.
        To prove that homotopy equivalence is an equivalence relation we follow the axioms:

        1. Reflexivity: any space is homotopy equivalent to itself by $f_t = \text{id}, \forall t$;
        2. Symmetry: if $f: X\to Y$ is a homotopy equivalence from $X$ to $Y$ and is realized by some $g$ such that $f\circ g \simeq 1$ and $g \circ f \simeq 1$, then $g: Y \to X$ is a homotopy equivalence from $Y$ to $X$ realized by $f$;
        3. Transitivity: this is what we proved above;
    2. Again we follow the axioms:
        1. Reflexivity: any map $f$ is homotopic to itself by $f_t = f, \forall t$;
        2. Symmetry: if $f \simeq g$ by $F(x, t)$, then $g \simeq f$ by $F(x, 1-t)$;
        3. Transitivity: if $f \simeq g$ by $F(x, t)$ and $g \simeq h$ by $G(x, s)$, then $f \simeq h$ by the function $\tilde{F}(x,t)$ defined by $\tilde{F}(x,t) = \begin{cases} F(x,2t), & t\le 0.5 \\ G(x, 2t-1),&t \ge 0.5\end{cases}$. Since by assumption $F(x, 1) = g$ and $G(x, 0) = g$, $\tilde{F}$ is continuous by the Pasting Lemma;
    3. Suppose $f: X \to Y$ is a homotopy equivalence (with some $g$ such that $f \circ g$ and $g \circ f$ are homotopic to identities), $\tilde{f}:X \to Y$ is a map homotopic to $f$. By the lemma in part 1, we know that that $f \simeq \tilde{f}$ implies that $(\text{id} \simeq) f \circ g \simeq \tilde{f} \circ g$ (and the other way of composition), this shows $\tilde{f}$ is a homotopy equivalence realized by $g$ as well.

    ## Problem 9

    **Show that a retract of a contractible space is contractible**.

    Proof

    Suppose $X$ is a contractible space, $r: X \to X$ where $r(X) = A$ and $r |_A = \text{id}_A$ is a retraction (so $A$ is the retract). By definition $\text{id}_X \simeq c$ where $c$ is a constant map on $X$.

    Write $\text{id}_A = r |_A = r \circ i$, where $i$ is the inclusion map from $A$ to $X$, $= r \circ \text{id}_X \circ i$ (we just insert an identity part) $\simeq r \circ c \circ i$ (this is from above exercise). Now $r \circ c \circ i = d$ is a constant map because $c$ is, then $\text{id}_A \simeq d$ proves that $A$ is contractible.

    ## Problem 10

    **Show that a space $X$ is contractible if and only if every map $f: X \to Y$, for arbitrary $Y$, is null-homotopic. Similarly, show $X$ is contractible if and only if every map $f: Y \to X$ is null-homotopic**.

    Proof

    First part:

    ($\Longrightarrow$) Suppose $X$ is contractible and it is realized by $F: X \times I \to X$. For any $f: X \to Y$, consider the map $f \circ F: X \times I \to Y$. We have that $(f \circ F)(x, 0) = f(F(x,0)) = f(\text{id}) = f$ and that $(f \circ F)(x, 1) = f(F(x, 1))$ $= f(c) = c'$ is a constant, so $f$ is null-homotopic;

    ($\Longleftarrow$) Suppose any map $f: X \to Y$ for any $Y$ is null-homotopic, then in particular $\text{id}_X: X \to X$ is null-homotopic, thus $X$ is contractible.

    Second part:

    ($\Longrightarrow$) Suppose $X$ is contractible and it is realized by $F: X \times I \to X$. For any $f: Y \to X$, consider the map $F \circ (f \times \text{id}_I): Y \times I \to X$, then similar with above, this gives a homotopy between $f$ and a constant map, thus $f$ is null-homotopic;

    ($\Longleftarrow$) Similar with above, this means $\text{id}_X: X \to X$ is null-homotopic and thus $X$ is contractible.

    ## Additional Problem

    **What is the mapping cylinder of $f: S^1 \to S^1$ where $f(z) = z^2$**?

    Solution

    By definition, the mapping cylinder $M_f$ is the quotient space of $((S^1 \times I) \sqcup S^1)/\sim$ by the rule $(z,1) \sim z^2 \in S^1$. We consider a plane model of such space.

    Start with $S^1 \times I$ and $S^1$:

    <img src="public/Pasted image 20221231121320.png" width="600" />

    Consider the function $f(z) = z^2$. In the mapping cylinder it identifies the first half circle to the full circle, and the second half circle to the full circle again. In the plane model it means to glue the green segment to the green segment on the rectangle twice:

    <img src="public/Pasted image 20221231121325.png" width="600" />

    We can cut the rectangle to half and do the glue by flipping part b:

    <img src="public/Pasted image 20221231121329.png" width="600" />

    We know this is a standard plane model for a Möbius band. So the mapping cylinder in the question is a Möbius band.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Fall Semester Homework 02""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Problem 14

    **Given positive integers $v, e$ and $f$ satisfying $v-e+f = 2$, construct a cell structure on $S^2$ having $v$ $0$-cells, $e$ $1$-cells, and $f$ $2$-cells**.

    Solution

    Start with the simplest case that $v = f = 1$ and $e = 0$. We can construct such a cell structure on $S^2$ by gluing the boundary of a disk ($2$-cell) to a point ($0$-cell).

    Now we do the following operations:

    1. Increase $v$ by $1$ until we get the desired number, to maintain the equation $v - e + f = 2$ we must increase $e$ by $1$: we attach one end of the new $1$-cell to the first $0$-cell, and attach the other end of the new $1$-cell to the new $0$-cell; we then modify *the* attaching map of the $2$-cell to the existing $1$-skeleton by letting it glue along the new components:

        <img src="public/Pasted image 20230101071207.png" width="600" />

    2. Increase $f$ by $1$ until we get the desired number, to maintain the equation $v - e + f = 2$ we must increase $e$ by $1$: we attach both ends of the new $1$-cell to the first $0$-cell; we then modify the (first) attaching map so that it glue along the new component; attach the new $2$-cell along the new $1$-cell and the first $0$-cell from the 'inside':

        <img src="public/Pasted image 20230101071213.png" width="600" />

        We should now achieve the desired $v, e, f$ and a corresponding cell structure on $S^2$.

    ## Additional Problem 1

    1. **Show that $CX$ (the cone of $X$) is contractible**;
    2. **Show $f: X \to Y$ is homotopic to a constant map if and only if $f$ extends to a map $CX \to Y$**.

    Proof

    1. Consider the following maps and diagram: $H: (X \times I) \times I \to X \times I$ by $(x, t, s) \mapsto (x, st +1 - s)$; a natural projection $\pi: X \times I \to X \times I/\sim \cong CX$: $$\begin{aligned}  &(X \times I) \times I \\ & &\searrow^H \\ &\downarrow^{\pi \times \text{id}_I} & X \times I \\ & & & \searrow^{\pi} \\ &CX \times I & \xrightarrow{H'} & CX \end{aligned}$$ (The space $CX \times I$ can be viewed as a quotient space of $(X \times I) \times I$ by the rule $(x,1,s)\sim (x',1,s)$)
    	Then: $H$ is continuous and $\pi$ is continuous, thus so is their composition; $\pi \circ H (x,1,s) = \pi(x,1)$ $=\pi(x',1) = \pi \circ H (x', 1, s)$ for any $x, x'\in X$ (so it is constant on equivalent class that realize $CX \times I$). Thus by the universal mapping property of quotient topology, there exists a continuous $H': CX \times I \to CX$ such that $H' \circ (\pi \times \text{id}_I)(x, t, 0) = H'(x,t,0)$ and also $= \pi \circ H(x,t,0) = \pi(x,1)$ $= c$. So $h'_0$ is a constant map; also $H'\circ (\pi \times \text{id}_I)(x, t, 1) = H'(x,t,1)$ and also $= \pi \circ H(x,t,1) = \pi(x, t)$ so $h'_1$ is the identity map. Thus $H'$ is a homotopy between a constant map and identity map on $CX$ and thus $CX$ is contractible;
    2. ($\Longrightarrow$) Suppose $f: X \to Y$ is homotopic to a constant map; say the homotopy is given by $H: X \times I \to Y$ where $h_0 = f$ and $h_1(X) = c$, a constant. In particular, $H$ is a map that is constant on equivalence class of $X \times I/\sim \cong CX$. The desired statement then follows directly from the universal mapping property of quotient topology.
    	($\Longleftarrow$) Suppose for a given $f: X \to Y$ we can extend it to $\tilde{f}: CX \to Y$ such that $\tilde{f}|_X = f$. Part 1 of this problem says $CX$ is contractible, and from an exercise in Homework 1 we know this means $\tilde{f}$ is null-homotopic. Write $f = \tilde{f} \circ \pi$ where $\pi$ is the natural projection from $X \to CX$, then again from an exercise in Homework 1 we have $f = \tilde{f} \circ \pi \simeq c \circ \pi \simeq c$ where $c$ is the constant map homotopic to $\tilde{f}$, i.e. $f$ is also null-homotopic.

    ## Additional Problem 2

    **Show that $S(S^n) = S^{n+1}$ for $n \ge 0$ (i.e. show that the suspension of $n$-sphere is homeomorphic to the $n+1$-sphere)**.

    Proof

    By definition, $S(S^n) = ((S^n \times I)/(S^n \times \lbrace 1 \rbrace))/(S^n \times \lbrace 0 \rbrace)$. We consider the CW-complex structure on this space. Say $S^n$ is given by a $0$-cell $n_1$ with an $n$-cell $n_2$ attaching to it through $\varphi$. $I$ is given by two $0$-cell $i_1, i_2$ and a $1$-cell $i_3$ attaching to them though $\psi$.

    Then $X = S^n \times I$ has a CW-complex structure as follow:

    1. $X^0$ consists of two $0$-cells come from $n_1 \times i_1$ and $n_1 \times i_2$;
    2. $X^1$ by attaching $X^0$ with one $1$-cell comes from $n_1 \times i_3$ through $\psi$;
    3. $X^n$ by attaching $X^1$ with two $n$-cells come from $n_2 \times i_1$ and $n_2 \times i_2$ through $\varphi$;
    4. $X^{n+1}$ by attaching $X^n$ with a $n+1$-cell comes from $n_2 \times i_3$.

    $Y = S^n \times \lbrace 1 \rbrace$ has a CW-complex structure with:

    1. $Y^0$ consists of one $0$-cell $n_1 \times i_2$;
    2. $Y^n$ by attaching $X^0$ with one $n$-cell $n_2 \times i_2$ through $\psi$;

    Thus $X/Y$ is given by:

    1. $(X/Y)^0$ consists of two $0$-cells, one from $n_1 \times i_1$, one from $Y$;
    2. $(X/Y)^1$ by attaching $(X/Y)^0$ with one $1$-cell from $n_1 \times i_3$;
    3. $(X/Y)^n$ by attaching $(X/Y)^1$ with one $n$-cell from $n_2 \times i_1$;
    4. $(X/Y)^{n+1}$ by attaching $(X/Y)^n$ with one $n+1$-cell from $n_2 \times i_3$.

    Similarly we take the quotient by $Z = S^n \times \lbrace 0 \rbrace$, the result $(X/Y)/Z = C$ is given by:

    1. $C^0$ consists of two $0$-cells, one from $Y$ and one from $Z$;
    2. $C^1$ by attaching $C^0$ with one $1$-cell from $n_1 \times i_3$;
    3. $C^{n+1}$ by attaching $C^1$ with one $n+1$-cell from $n_2 \times i_3$. The attachment is along $C^1$.

    Graphically it looks like:

    <img src="public/Pasted image 20230101071225.png" width="600" />

    Which is equivalent with a $n+1$-cell attaching to a $0$-cell, and thus the space is (homeomorphic to) $S^{n+1}$.

    ## Additional Problem 3

    **Show that $S^n \wedge S^m \cong S^{n+m}$ (i.e. show the smash product of spheres of dimensions $n$ and $m$ is homeomorphic to another sphere of dimension $n+m$)**.

    Proof

    By definition, $S^m \wedge S^n$ $= S^m \times S^n / S^m \vee S^n$. We consider the CW-complex structure on this space. Say $S^m$ is given by a $0$-cell $m_1$ plus an $m$-cell $m_2$ and the attaching map is given by $\varphi$; $S^n$ is given by a $0$-cell $n_1$ plus an $n$-cell $n_2$ and the attaching map is given by $\psi$, then their product $X = S^m \times S^n$ is given by (WLOG say $n \le m$):

    1. $X^0$ is a $0$-cell comes from $m_1 \times n_1$;
    2. $X^n$ comes from an $n$-cell (comes from $m_1 \times n_2$) attaching to $X^0$ via $\psi$, which in particular means the entire boundary is mapped to the $0$-cell;
    3. $X^m$ comes from an $m$-cell (comes from $m_2 \times n_1$) attaching to $X^n$ via $\varphi$, which again means the entire boundary is mapped to the $0$-cell;
    4. $X^{m+n}$ comes from an $m+n$-cell (comes from $m_2 \times n_2$) attaching to $X^m$.

    The wedge sum $Y = S^m \vee S^n$ is given by the disjoint union of $S^m$ and $S^n$ (so $2$ $0$-cells, an $m$-cell and an $n$-cell) with the two $0$-cells identified. In particular, $Y$ is the same as $X^m$.

    Thus by taking quotient, $X/Y$ has a CW-complex structure with a $0$-cell and an $m+n$-cell attaching to it (through a constant map), which means it is $S^{m+n}$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Fall Semester Homework 03""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Problem 20

    **Show that the subspace $X \subset \mathbb{R}^3$ formed by a Klein Bottle intersecting itself in a circle is homotopy equivalent to $S^1\vee S^1\vee S^2$**.

    Proof

    We will show the homotopy equivalence through the following images.

    First we give this space a CW-structure by adding some vertices/edges/faces:

    <img src="public/Pasted image 20230101071452.png" width="600" />

    (On the third picture, the blue line is not really an edge, it is just there to complete the shape of the surface)

    We then 'contract' the little circle to one vertex, split this vertex to three vertices, and drag the two tips. This creates two edges that have no face attached (colored in black):

    <img src="public/Pasted image 20230101071502.png" width="600" />

    Two pairs of vertices will meet again and merge to two vertices. Finally we drag the remaining vertices together:

    <img src="public/Pasted image 20230101071506.png" width="400" />

    So in the end we get a vertex, with two edges and a face attached to it as shown above, which is $S^1 \vee S^1 \vee S^2$. The transformation of the space we did above is preserved by homotopy equivalence, and thus the original $X$ is homotopy equivalent with $S^1 \vee S^1 \vee S^2$.

    ## Problem 22

    **Let $X$ be a finite graph lying in a half-plane $P \subset \mathbb{R}^3$ and intersecting the edge of $P$ in a subset of the vertices of $X$. Describe the homotopy type of the 'surface of revolution' obtained by rotating $X$ about the edge line of $P$**.

    Solution

    >This solution is not quite correct.

    Assume $X$ is a finite and connected graph that lies entirely on a half plane, take revolution as described in the question, the resulting space is $X \times S^1$. First a claim: if $X' \subset X$ and $Y' \subset Y$ are deformation retracts, then $X' \times Y' \subset X \times Y$ is also a deformation retract.

    A quick proof: we can prove that if $H$ is a homotopy between $f, g: X \to Y$ and $H'$ is a homotopy between $f', g': X' \to Y'$, then there exists a homotopy between $f\times f', g\times g'$- the map $G:X \times X' \times I \to Y \times Y'$ given by $G(x,x',t) \mapsto (H(x,t), H'(x',t))$ will do the work.

    Thus we can first take a rather simple space $X'$ that has the same homotopy type with $X$, then take the product $X' \times S^1$, and the result we get has the same homotopy type with $X \times S^1$.

    And another claim: any finite connected graph deformation retract to a finite wedge sum of circles, intuitively because we can 'contract' any edge (and merge its endpoints) that not having two endpoint attached to the same vertex, eventually the only remaining parts are one vertex and a number of edges attached to it:

    <img src="public/Pasted image 20230101071516.png" width="600" />

    (Each step we 'contract' the edge colored in black)

    Finally the third claim, the surface of revolution of an edge with both endpoints attached to the same vertex is homotopy equivalent with $S^1 \vee S^2$. This can be illustrated in the same manner as Problem 20 above:

    <img src="public/Pasted image 20230101071521.png" width="600" />

    If we have a (multiple) wedge sum of circles, take the revolution we will just get a (multiple) wedge sum of $S^1 \vee S^2$. All these $S^1$ and $S^2$'s are identified at a point.

    Put everything together, if we have a graph $X$, deformation retract it to a wedge sum of circles, say $X \simeq \bigvee\limits_{i = 1}^nS^1$. From above we can see this $n$ can be calculated by $n = e-v+1$ where $e$ is the number of edges and $v$ is the number of vertices of $X$ (each step we remove an edge and a vertex, until there is only one vertex, and the number of circle is the same as the number of remaining edges). Then the surface of revolution of $X$ is homotopy equivalent with $\bigvee\limits_{i = 1}^nS^1 \vee \bigvee\limits_{i = 1}^nS^2$. In $n=0$ then the surface is contractible.

    ## Additional Problem

    **Calculate homology groups for all closed, compact, connected surfaces**.

    Solution

    Any closed compact connected surface is homeomorphic to exactly one of $S^2 \# nT^2$ (orientable surface of genus $n$) and $S^2 \# n\mathbb{R}P^2$ (non-orientable surface of genus $n$). Since homeomorphic spaces have the same homology group, we have two cases (denote the surface itself to be $X$):

    1. Orientable surface of genus $n$. In this case the surface has a CW-structure with one $0$-cell, $2n$ $1$-cells ($a_1,b_1,a_2,b_2,\dots, a_n, b_n$), and one $2$-cells ($D^2$). The $1$-cells are attaching to the $0$-cell simply by attaching all the endpoints to it. And the $2$-cell is attaching to these $1$-cells by $\prod\limits_{i=1}^n[a_i,b_i]$.
    	So the chain groups are $C_0(X) \cong \mathbb{Z}$, $C_1(X) \cong \mathbb{Z}^{2n}$, $C_2(X) \cong \mathbb{Z}$, and everything else is the trivial group.
    	For the boundary operator: $\partial_0$ is $0$ because $C_{-1}(X) = 0$; for each $a_i$ or $b_i$, since both of its ends are attached to the $0$-cell (so with opposite signs), $\partial_1(a_i) = 0$ and $\partial_1(b_i) = 0$, thus $\partial_1 = 0$ as well; finally $\partial_2(D^2)$ $= a_1 + b_1 - a_1 - b_1 + \dots + a_n + b_n - a_n - b_n$ $=0$ so $\partial_2 = 0$. Everything else is the zero map as well.
    	Now we can calculate the homology groups: $H_0(X) = \ker{\partial_0}/im{\partial_1}$ $= \mathbb{Z}/0 \cong \mathbb{Z}$; $H_1(X) = \ker{\partial_1}/im{\partial_2}$ $=\mathbb{Z}^{2n}/0$ $\cong \mathbb{Z}^{2n}$; $H_2(X) = \ker{\partial_2}/im{\partial_3}$ $\cong \mathbb{Z}$. Everything else is the trivial group;
    2. Non-orientable surface of genus $n$. In this case the surface has a CW-structure with one $0$-cell, $n$ $1$-cells ($a_1,\dots,a_n$), and one $2$-cell ($D^2$). Again the $1$-cells are attaching to the $0$-cell by attaching all the ends to it. $D^2$ is attaching to the $1$-cells by $\prod\limits_{i = 1}^na_i^2$.
    	Thus the chain groups are $C_0(X) \cong \mathbb{Z}$, $C_1(X) \cong \mathbb{Z}^n$, $C_2(X) \cong \mathbb{Z}$, and everything else is the trivial group.
    	The boundary operators are: $\partial_0$ is again of course $0$; for each $i$, $\partial_1(a_i) = 0$ thus $\partial_1 = 0$ again; $\partial_2$ is different from before, we have $\partial_2(D^2) = a_1 + a_1 + \dots + a_n + a_n$, i.e. $\partial_2:\mathbb{Z} \to \mathbb{Z}^n$ by $\partial_2(x) \mapsto (2x,\dots,2x)$ (but the only independent term is $2x$). All the other boundary operators are the zero maps.
    	Thus we may calculate the homology group: $H_0(X) = \ker{\partial_0}/im{\partial_1}$ $= \mathbb{Z}/0 \cong \mathbb{Z}$; $H_1(X) = \ker{\partial_1}/im{\partial_2}$ $=\mathbb{Z}^{n}/2\mathbb{Z}$ $\cong \mathbb{Z}^{n-1} \times\mathbb{Z_2}$; $H_2(X) = \ker{\partial_2}/im{\partial_3}$ $= 0/0 \cong 0$ (because $(2x,\dots,2x) = (0,\dots, 0)$ $\implies x = 0$). Everything else is the trivial group.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Fall Semester Homework 04""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Problem 1

    **What familiar space is the quotient $\Delta$-complex of a $2$-simplex $[v_0, v_1, v_2]$ obtained by identifying the edges $[v_0, v_1]$ and $[v_1, v_2]$, preserving the ordering of vertices**?

    Solution

    The space is a Möbius strip, illustrated as follow:

    <img src="public/Pasted image 20230101071804.png" width="600" />

    ## Problem 2

    **Show that the $\Delta$-complex obtained from $\Delta^3$ by performing the order-preserving edge identifications $[v_0, v_1] \sim [v_1, v_3]$ and $[v_0, v_2] \sim [v_2, v_3]$ deformation retracts onto a Klein bottle. Also, find other pairs of identifications of edges that produce $\Delta$-complexes deformation retracing onto a torus, a $2$-sphere, and $\mathbb{R}P^2$**.

    Solution

    Start with an edge-identified tetrahedron and illustrate the deformation retract as follow:

    <img src="public/Pasted image 20230101071809.png" width="600" />

    Explanation of each step:

    1. Step 1: deformation retract to the face consists of two simplexes (like a projection) (and I think we can kind of stop here if we know the connected sum of two $\mathbb{R}P^2$ is a Klein bottle);
    2. Step 2 & 3: standard procedure to create a new edge to be glued later;
    3. Step 4: prepare for the gluing along the sides indicate by double-arrow. Rotate the triangle on the left clock-wise for one side, rotate the triangle on the right counter-clock-wise for one side;
    4. Step 5: flip the triangle on the right up-side-down, so the double-arrow is aligned;
    5. Step 6: glue, and get a standard planar model of Klein bottle.

    For the second part of the question, we can first imagine to have a tetrahedron deformation retract to a diamond shape, then just identify edges like we do for a planar model:

    <img src="public/Pasted image 20230101071816.png" width="600" />

    ## Problem 3

    **Construct a $\Delta$-complex on $\mathbb{R}P^n$ as a quotient of a $\Delta$-complex structure on $S^n$ having vertices the two vectors of length $1$ along each coordinate axis in $\mathbb{R}^{n+1}$**.

    Solution

    First we construct a $\Delta$-complex structure on $S^n$ consists of $2^{n+1}$ number of $n$-simplexes. For $n = 1$ or $2$ it can be illustrated as follow:

    <img src="public/Pasted image 20230101071826.png" width="600" />

    In general, let $v_0 = (1,\overbrace{0,\dots,0}^n)$, $v_1 = (0,1,0,\dots,0)$, $\dots$, $v_n = (0,\dots,0,1)$ so that $[v_0,\dots, v_n]$ is the standard $n$-simplex, then $S^n$ has a $\Delta$-complex structure consists of $\lbrace [\pm v_0, \pm v_1, \dots, \pm v_n] \rbrace$ with appropriate identification (e.g. $S^1$ consists of $[v_0, v_1]$, $[-v_0, v_1]$, $[v_0, -v_1]$ and $[-v_0, -v_1]$ as shown on the above graph).

    Now $\mathbb{R}P^n$ can be viewed as $S^n$ with antipodal points identified. So on simplex level we want each simplex $V$ to be identified with $-V$ (keep the ordering), then we get a $\Delta$-complex structure for $\mathbb{R}P^n$. For example, identify $[v_0, v_1] \sim [-v_0, -v_1]$ and $[-v_0, v_1] \sim [v_0, -v_1]$ gives us $\mathbb{R}P^1$.

    ## Problem 4

    **Compute the simplicial homology groups of the triangular parachute obtained from $\Delta^2$ by identifying its three vertices to a single point**.

    Solution

    By the description, $X$ can be described by the following diagram:

    <img src="public/Pasted image 20230101071832.png" width="600" />

    (With the three vertices identified; We give the simplices names for convenience)

    $X$ consists of $1$ $0$-simplex, $3$ $1$-simplices, and $1$ $2$-simplex. So we have $\Delta_0(X) \cong \mathbb{Z}$ generated by $\sigma_v$, $\Delta_1(X) \cong \mathbb{Z}^3$ generated by $\sigma_{a,b,c}$, and $\Delta_2(X) \cong \mathbb{Z}$ generated by $\sigma_D$. Since there is just one vertex, the maps are all rather simple. The other chain groups are trivial. We now calculate the boundary operators.

    1. $\partial_2(\sigma_D)$ $=\sigma_D|_b - \sigma_D|_c + \sigma_D |_a$ $= \sigma_b - \sigma_c + \sigma_a$;
    2. $\partial_1(\sigma_a)$ $= \sigma_a|_v - \sigma_a|_v = 0$, and similar for $\sigma_{b,c}$.

    So we have:

    1. $H_0^{\Delta}(X) = \ker{\partial_0}/im{\partial_1}$ $\cong \mathbb{Z}/0 \cong \mathbb{Z}$ (because $\partial_1$ and of course $\partial_0$ are $0$ maps);
    2. $H_1^{\Delta}(X) = \ker{\partial_1}/im{\partial_2}$ $\cong \langle \sigma_a,\sigma_b,\sigma_c \rangle/\langle \sigma_b - \sigma_c + \sigma_a \rangle$ $\cong \langle \sigma_a, \sigma_b \rangle$ $\cong \mathbb{Z}^2$;
    3. $H_2^{\Delta}(X) = \ker{\partial_2}/im{\partial_3}$ $\cong 0/0 \cong 0$.

    And the other simplicial homology groups are of course trivial.

    ## Problem 5

    **Compute the simplicial homology groups of the Klein bottle using the $\Delta$-complex structure described at the beginning of this section**.

    Solution

    The $\Delta$-complex structure was described as follow (a screenshot from the book):

    <img src="public/Pasted image 20230101071841.png" width="600" />

    So this space $K$ consists of $1$ $0$-simplex, thus $\Delta_0(K) \cong \mathbb{Z}$ generated by $\sigma_v$; $3$ $1$-simplices, thus $\Delta_1(K) \cong \mathbb{Z}^3$ generated by $\sigma_{a,b,c}$; and $2$ $2$-simplices, thus $\Delta_2(K) \cong \mathbb{Z}^2$ generated by $\sigma_{U,L}$, which can be described as following to preserve ordering of vertices:

    Calculate the boundary operators:

    1. $\partial_2(\sigma_U)$ $= \sigma_U|_b - \sigma_U|_c + \sigma_U|_a$ $= \sigma_b - \sigma_c + \sigma_a$;
    2. $\partial_2(\sigma_L)$ $= \sigma_L|_a - \sigma_L|_b + \sigma_L|_c$ $= \sigma_a - \sigma_b + \sigma_c$;
    3. $\partial_1(\sigma_a)$ $= \sigma_a|_v - \sigma_a|_v = 0$ and again same for $\sigma_{b,c}$.

    Thus we can compute the homology groups:

    1. $H_0^{\Delta}(K)$ $= \ker{\partial_0}/im{\partial_1}$ $\cong \mathbb{Z}/0$ $\cong \mathbb{Z}$;
    2. $H_1^{\Delta}(K)$ $= \ker{\partial_1}/im{\partial_2}$ $\cong \langle \sigma_a, \sigma_b, \sigma_c \rangle/\langle \sigma_a - \sigma_c + \sigma_b, \sigma_a - \sigma_b + \sigma_c \rangle$ $\cong \langle \sigma_a, \sigma_b, \sigma_c \rangle/\langle \sigma_a - \sigma_c + \sigma_b, 2\sigma_a \rangle$ $\cong \langle \sigma_a, \sigma_b \rangle/\langle 2\sigma_a \rangle$ $\cong \mathbb{Z} \times \mathbb{Z}_2$;
    3. $H_2^{\Delta}(K)$ $= \ker{\partial_2}/im{\partial_3}$ $\cong 0/0 \cong 0$ (because $\sigma_b - \sigma_c + \sigma_a$ and $\sigma_a - \sigma_b + \sigma_c$ are linearly independent if viewed as vectors in basis $\sigma_{a,b,c}$).

    ## Problem 9

    **Compute the homology groups of the $\Delta$-complex $X$ obtained from $\Delta^n$ by identifying all faces of the same dimension. Thus $X$ has a single $k$-simplex for each $k \le n$**.

    Solution

    By the description, $X$ consists of $1$ $k$-simplex (let us denote them by $\delta_k$) for each $k \le n$, thus $\Delta_k(X) \cong \mathbb{Z}$ for each $k$, generated by $\sigma_{\delta_k}$. Let us compute the boundary operator:

    1. $\partial_0(\sigma_{\delta_0}) = 0$ is trivial;
    2. $\partial_1(\sigma_{\delta_1})$ $= \sigma_{\delta_1} |_{\delta_0} - \sigma_{\delta_1} |_{\delta_0}$ $= 0$;
    3. $\partial_2(\sigma_{\delta_2})$ $= \sigma_{\delta_2} |_{\delta_1} - \sigma_{\delta_2} |_{\delta_1} + \sigma_{\delta_2} |_{\delta_1}$ $= \sigma_{\delta_2} |_{\delta_1}$ $= \sigma_{\delta_1}$;
    4. $\dots$
    5. We can see a pattern here from the way it is calculated: $$\partial_k(\sigma_{\delta_k})= \begin{cases} 0,&k\text{ odd or equals }0\\ \sigma_{\delta_{k-1}},&\text{otherwise}\end{cases}$$ With these we can now calculate the homology groups:
    6. $H^{\Delta}_0(X)$ $= \ker{\partial_0}/im{\partial_1}$ $\cong \mathbb{Z}/0$ $\cong \mathbb{Z}$; this works even if $n = 0$ because $im{\partial_1}$ would be $0$ anyway;
    7. If $n > 1$, then $H^{\Delta}_1(X)$ $= \ker{\partial_1}/im{\partial_2}$ $\cong \langle \sigma_{\delta_1} \rangle/\langle \sigma_{\delta_1} \rangle$ $\cong 0$; however if $n = 1$, then $im{\partial_2}$ would be $0$ thus $H^{\Delta}_1(X)$ $\cong \mathbb{Z}/0$ $\cong \mathbb{Z}$;
    8. $H^{\Delta}_2(X)$ $= \ker{\partial_2}/im{\partial_3}$ $\cong 0/im{\partial_3}$ $\cong 0$; and we can see that it does not depends on if $n > 2$ or not;
    9. So again, we can see a pattern here from the calculation: $$H^{\Delta}_k(X) \cong \begin{cases}\mathbb{Z},&k = 0\\0,&n < k\\\mathbb{Z},&k\text{ odd and }k = n\\0,&k\text{ odd and }k < n\\0,&k\text{ even} \end{cases}$$ (or put it in another way, if $n$ is even, then the only non-trivial homology group is $H^{\Delta}_0(X) \cong \mathbb{Z}$, and if $n$ is odd, then the only non-trivial homology group is $H^{\Delta}_0(X), H^{\Delta}_n(X) \cong \mathbb{Z}$)
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Fall Semester Homework 05""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Problem 11

    **Show that if $A$ is a retract of $X$ then the map $H_n(A) \to H_n(X)$ induced by the inclusion $A \hookrightarrow X$ is injective**.

    Proof

    If $A$ is a retract of $X$, then by definition there exists $r: X \to A$ so that $r \circ i = \text{id}$ where $i$ is the inclusion $A \hookrightarrow X$. Thus $(r \circ i)_{*} = \text{id}_{*}$, and thus $r_{*} \circ i_{*} = \text{id}$. In particular this means $r_{*} \circ i_{*}$ is injective. But then it is a rather preliminary result that $f \circ g$ being injective implies $g$ being injective, thus $i_{*}$ is injective which is the desired result.

    ## Problem 12

    **Show that chain homotopy of chain maps is an equivalence relation**.

    Proof

    Recall that two chain maps $f_{\#}, g_{\#}: C_n(X) \to C_n(Y)$ are chain homotopic if there exists maps $P_n: C_n(X) \to C_{n+1}(Y)$ such that $P_{n-1}\circ \partial_n^X + \partial_{n+1}^Y \circ P_n = g_{\#} - f_{\#}$. For readability, we just write LHS as $P\partial + \partial P$ and write $f_{\#} \sim g_{\#}$ if they are chain homotopic. We follow the axioms to prove it's an equivalence relation.

    1. Reflexivity: Take $P_n$ to be the zero map for each $n$, then $P\partial + \partial P$ $= 0+0 = 0$ ($\partial$ is a homomorphism) which can be viewed as $f_{\#} - f_{\#}$, so $f_{\#} \sim f_{\#}$;
    2. Symmetry: Suppose $f_{\#} \sim g_{\#}$ so $P\partial + \partial P = g_{\#} - f_{\#}$, then take $Q = -P$ we have $Q\partial + \partial Q$ $= -P\partial + \partial (-P)$ $= -(P\partial + \partial P)$ $= f_{\#} - g_{\#}$ thus $g_{\#} \sim f_{\#}$;
    3. Transitivity: Suppose $f_{\#} \sim g_{\#}$ realized by $P$ and $g_{\#} \sim h_{\#}$ realized by $Q$, then $h_{\#} - f_{\#}$ $= (h_{\#} - g_{\#}) + (g_{\#} - f_{\#})$ $= Q\partial + \partial Q + P\partial + \partial P$ $= (P+Q)\partial + \partial(P+Q)$ (point-wise addition for maps) which shows that $f_{\#} \sim h_{\#}$. The last equality is due to the fact that all involved groups are abelian so we can change orders, and $\partial, P, Q$ are all homomorphisms so preserve the operation.

    Thus all three axioms are satisfied, the relation is an equivalent relation.

    ## Problem 13

    **Verify that $f \simeq g$ implies $f_* = g_*$ for induced homomorphisms of reduced homology groups**.

    Proof

    (Let's give the spaces name, say $f\simeq g: X \to Y$. Also for clarity, let us write $\tilde{\cdot}$ whenever we are talking about reduced homology group or extended chain complex)

    We already have the theorem says that $f_* = g_*$ for induced homomorphisms of homology groups. We also know that $H_n \cong \tilde{H}_n$ except when $n = 0$.

    The reduced homology groups comes from the following chain complex: $$\begin{array}{ccccccccc} \dots &\longrightarrow &C_1(X) &\longrightarrow^{\partial_1} &C_0(X) &\longrightarrow^{\varepsilon} &\mathbb{Z} &\longrightarrow &0 \\ \\ &&^{f_{\#},g_{\#}}\downarrow&^P\swarrow &^{f_{\#},g_{\#}}\downarrow& ^Q\swarrow&^{\tilde{f}_{\#},\tilde{g}_{\#}}\downarrow \\ \\ \dots &\longrightarrow &C_1(Y) &\longrightarrow^{\partial_1} &C_0(Y) &\longrightarrow^{\varepsilon} &\mathbb{Z} &\longrightarrow &0\end{array}$$ where $\tilde{f}_{\#}$ and $\tilde{g}_{\#}$, by definition of $\varepsilon$, $f_{\#}$ and $g_{\#}$, must be the identity map. If there exists $Q$ so that $P$ (a collection of maps) together with $Q$ is a chain homotopy, then $f_{\#}(\alpha)$ and $g_{\#}(\alpha)$ would determine the same homology class and thus $f_* = g_*$ as desired.

    Indeed, take $Q$ to be the zero map, then we have:

    1. $\partial_1 P + Q\varepsilon$ $= \partial_1 P + 0$ $= g_{\#} - f_{\#}$;
    2. $\varepsilon Q (+0)$ $= 0 = \tilde{g}_{\#} - \tilde{f}_{\#}$ because they are both identity map;
    3. $\partial P + P \partial = g_{\#} - f_{\#}$ for higher $n$ still holds because $P$ is a chain homotopy.

    So we have a chain homotopy, then by the above argument, $f_*$ and $g_*$ are equal.

    ## Problem 14

    **Determine whether there exists a short exact sequence $0 \to \mathbb{Z}_4 \to \mathbb{Z}_8 \oplus \mathbb{Z}_2 \to \mathbb{Z}_4 \to 0$**.

    Solution

    So we want to find some $i: \mathbb{Z}_4 \to \mathbb{Z}_8 \oplus \mathbb{Z}_2$ that is injective, and $j: \mathbb{Z}_8 \oplus \mathbb{Z}_2 \to \mathbb{Z}_4$ that is surjective, and $\text{im}(i) = \ker{(j)}$. Merely from the point of order of groups ($4\times 4 = 16$), there can be a short exact sequence, indeed:

    One example is to have $i(1) = (2, 1)$, then $\text{im}(i) = \lbrace (2,1), (4, 0), (6,1), (0,0) \rbrace$ (so that it is a homomorphism). Notice then $(\mathbb{Z}_8 \oplus \mathbb{Z}_2)/\text{im}(i)$ $= \lbrace [(0,0)],[(1,0)],[(2,0)],[3,0] \rbrace$ $= \mathbb{Z}_4$, then the natural projection map $\mathbb{Z}_8 \oplus \mathbb{Z}_2 \to (\mathbb{Z}_8 \oplus \mathbb{Z}_2)/\text{im}(i)$ may serve as a desired $j$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Fall Semester Homework 06""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Problem 15

    **For an exact sequence $A \to B \to C \to D \to E$ show that $C = 0$ if and only if the map $A \to B$ is surjective and $D \to E$ is injective. Hence for a pair of spaces $(X, A)$, the inclusion $A \to X$ induces isomorphisms on all homology groups if and only if $H_n(X, A) = 0$ for all $n$**.

    Proof

    Let us give the maps names: $$A \xrightarrow{i} B \xrightarrow{j} C \xrightarrow{k} D \xrightarrow{h} E.$$ Suppose $C = 0$, then $j$ has no other choice but the zero map, thus $\ker{j} = B$, thus $\text{im}(i) = \ker{j} = B$, which means $i$ is surjective; also $k$ has no other choice but the zero map (because homomorphism maps identity to identity), so $\text{im}(k) = 0$, thus $\ker{h} = \text{im}(k) = 0$, which means $h$ is injective.

    Conversely, suppose $i$ is surjective and $h$ is injective, we can get that both $j$ and $k$ are zero maps (using the same argument but different direction). But then the exactness told us $0 = \text{im}(j) = \ker{k}$, so $k$ is an injective zero map, which forces $C$ to be $0$.

    The second statement is rather immediate from the first statement, consider $$\begin{aligned}\dots &\to H_{n+1}(A) \to H_{n+1}(X) \to H_{n+1}(X,A) = 0 \to \\ &\to H_{n}(A) \to H_{n}(X) \to H_{n}(X, A) = 0 \to \\ &\to H_{n-1}(A) \to H_{n-1}(X) \to H_{n-1}(X, A) = 0 \to \dots\end{aligned}$$ Then $H_{n+1}(A) \to H_{n+1}(X) \to 0 \to H_{n}(A) \to H_{n}(X)$ implies $H_{n}(A) \to H_{n}(X)$ is injective, and $H_{n}(A) \to H_{n}(X) \to 0 \to H_{n-1}(A) \to H_{n-1}(X)$ implies $H_{n}(A) \to H_{n}(X)$ is surjective, thus it is an isomorphism.

    ## Problem 16

    1. **Show that $H_0(X, A) = 0$ if and only if $A$ meets each path-component of $X$**;
    2. **Show that $H_1(X, A) = 0$ if and only if $H_1(A) \to H_1(X)$ is surjective and each path-component of $X$ contains at most one path-component of $A$**.

    Proof

    1. Suppose $A$ meets each path-component of $X$.
        First we assume $X$ is path-connected, in this case it means $A \subset X$ is not empty. Pick any $x \in A \subset X$, then the homology class $[x] \in H_0(A)$ is mapped to $[x] \in H_0(X)$ (because it is induced by inclusion). In particular $H_0(A) \to H_0(X)$ is surjective.
        Now assume the general case, we know $H_0(A) \cong \bigoplus H_0(A_i)$ and $H_0(X) \cong \bigoplus H_0(X_i)$ where $X_i$ are the path components of $X$ and $A_i = A \cap X_i$. Each $H_0(A_i) \to H_0(X_i)$ is surjective, thus $H_0(A) \to H_0(X)$ is also surjective. It then follows from Problem 15 that $H_0(X, A)$ must be $0$.
        Conversely, suppose $A$ does not meet each path-component of $X$, in particular it means $A_i = A \cap X_i = \varnothing$ for some $i$, but then for this $i$ we have $H_0(A_i) = 0 \to H_0(X_i) \to H_0(X_i,A_i) \to 0$, which by exactness means $H_0(X_i,A_i) \cong H_0(X_i) = \mathbb{Z}$, then $H_0(X,A)$ cannot be $0$;
    2. By problem 15, the statement is equivalent with '$H_0(A) \to H_0(X)$ is injective if and only if each path-component of $X$ contains at most one path-component of $A$'.
        So suppose each path-component of $X$ contains at most one path-component of $A$.
        First we assume $X$ is path-connected, then either $A = \varnothing$ or $A$ is path-connected and non-empty. If $A$ is empty, then of course $H_0(A) \to H_0(X)$ is injective. If $A$ is path-connected and non-empty, pick any $x \in A \subset X$, then the homology class $[x] \in H_0(A)$ is mapped to $[x] \in H_0(X)$. In fact, in this case the map $H_0(A) \to H_0(X)$ is just the identity, so of course is injective.
        For the general case, we have that $H_0(A) = \bigoplus H_0(A_i) \to H_0(X) = \bigoplus H_0(X_i)$ is injective because each $H_0(A_i) \to H_0(X_i)$ is injective.
        Conversely, suppose there is some path-component of $X$ contains at least two path-components of $A$. So for certain $i$, we have $H_0(A_i) \cong \mathbb{Z}^n$ ($n >1$) and $H_0(X_i) \cong \mathbb{Z}$. But for $n > 1$, there is no injective homomorphism $\mathbb{Z}^n \to \mathbb{Z}$, so $H_0(A_i) \to H_0(X_i)$ is not injective. Then $\bigoplus H_0(A_i) \to \bigoplus H_0(X_i)$ also cannot be injective.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Fall Semester Homework 07""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Problem 17

    1. **Compute the homology groups $H_n(X,A)$ when $X$ is $S^2$ or $S^1 \times S^1$ and $A$ is a finite set of points of $X$**;
    2. **Compute the groups $H_n(X,A)$ and $H_n(X,B)$ for $X$ a closed orientable surface of genus two with $A$ and $B$ the circles shown (What are $X/A$ and $X/B$?)**.

    <img src="public/Pasted image 20230101072547.png" width="400" />

    Solution

    1. Consider the LES of the pair $(X,A)$: $$\begin{array}{cccccccc} &&&\dots&\to&H_3(X,A)&\to &\\ \to & H_2(A) & \to & H_2(X) & \to & H_2(X, A) & \to & \\ \to & H_1(A) & \to & H_1(X) & \to & H_1(X, A) & \to & \\ \to & H_0(A) & \to & H_0(X) & \to & H_0(X, A) & \to &0 \end{array}$$ First, let $X$ be $S^2$, so that we know $H_2(X) = \mathbb{Z}$, $H_0(X) = \mathbb{Z}$, and all other $H_n(X) = 0$. $A$ is by assumption a finite set of discrete points, so $H_0(A) = \mathbb{Z}^m$ where $m$ is the number of points in $A$, and $H_n(A) = 0$ for all the other $n$'s.
        So in particular, $H_n(A) = H_n(X) = 0$ for all $n > 2$, which leaves that $H_n(X,A) = 0$ for all $n > 3$. For lower dimensions we have: $$\begin{array}{cccccccc} &\dots&\to&0&\to&H_3(X,A)&\to &\\ \to & 0 & \to & \mathbb{Z} & \to & H_2(X, A) & \to & \\ \to & 0 & \to & 0 & \to & H_1(X, A) & \to & \\ \to & \mathbb{Z}^m & \xrightarrow{i} & \mathbb{Z} & \xrightarrow{j} & H_0(X, A) & \xrightarrow{k} &0 \end{array}$$ $H_3(X, A)$ must be $0$ because it is in between two zeroes. $H_2(X, A)$ must be isomorphic to $\mathbb{Z}$ because we have $0 \to \mathbb{Z} \to H_2(X,A) \to 0$. Consider the map $i$, since $S^2$ has only one path-component, $i$ must be surjective because it is induced by the inclusion map. Thus $\text{im}(i) = \mathbb{Z} = \ker(j)$ thus $\text{im}(j) = 0 = \ker(k)$, but $\ker(k)$ should be the entire $H_0(X,A)$, so $H_0(X, A) = 0$. Thus we are left with a short exact sequence $0 \to H_1(X,A) \to \mathbb{Z}^m \to \mathbb{Z} \to 0$. Thus $H_1(X,A)$ must be $\mathbb{Z}^{m-1}$ because $\mathbb{Z}^m/H_1(X,A) \cong \mathbb{Z}$.
        In short, $H_n(X,A) = \begin{cases} 0&,n=0,n>2\\ \mathbb{Z}&,n = 2 \\ \mathbb{Z}^{m-1}&,n = 1,m=| A |\end{cases}$.
        Now let $X = S^1 \times S^1$ be the torus, then we know $H_0(X) = \mathbb{Z}$, $H_1(X) = \mathbb{Z}^2$, $H_2(X) = \mathbb{Z}$, and everything else is $0$. Same as before, $H_0(A) = \mathbb{Z}^m$ where $m$ is the number of points in $A$, and $H_n(A) = 0$ for all the other $n$'s. So again for $n > 3$ we must have $H_n(X,A) = 0$ and for lower dimensions we have: $$\begin{array}{cccccccc} &\dots&\to&0&\to&H_3(X,A)&\to &\\ \to & 0 & \to & \mathbb{Z} & \to & H_2(X, A) & \to & \\ \to & 0 & \to & \mathbb{Z}^2 & \to & H_1(X, A) & \to & \\ \to & \mathbb{Z}^m & \to & \mathbb{Z} & \to & H_0(X, A) & \to&0 \end{array}$$ So with the very same argument, we have that $H_3(X,A) = 0$, $H_2(X, A) = \mathbb{Z}$, and $H_0(X,A) = 0$. We are left with an exact sequence $$0 \xrightarrow{\alpha} \mathbb{Z}^2 \xrightarrow{\beta} H_1(X,A) \xrightarrow{\gamma} \mathbb{Z}^m \xrightarrow{\delta} \mathbb{Z} \xrightarrow{\varepsilon} 0.$$
        Since $\text{im}(\alpha) = 0$, we must have $\ker(\beta) = 0$ thus $\text{im}(\beta) = \mathbb{Z}^2 = \ker(\gamma)$. On the other side, $\text{im}(\delta) = \ker(\varepsilon) = \mathbb{Z}$, thus isomorphism theorem says $\text{im}(\delta) = \mathbb{Z}^m/\ker(\delta)$ thus $\ker(\delta) = \mathbb{Z}^{m-1}$. But $\ker(\delta) = \text{im}(\gamma)$, then isomorphism theorem says $\text{im}(\gamma) = H_1(X,A)/\ker(\gamma)$ thus $H_1(X,A) = \mathbb{Z}^{m-1} \times \mathbb{Z}^2 = \mathbb{Z}^{m+1}$.
        In short, $H_n(X,A) = \begin{cases} 0&,n=0,n>2\\ \mathbb{Z}&,n = 2 \\ \mathbb{Z}^{m+1}&,n = 1,m=| A |\end{cases}$;
    2. We will try to use the theorem that $H_n(X,A) = \tilde{H}_n(X/A)$. So we need to know what is $X/A$ and $X/B$. It's not too hard to see $X/A$ is homotopic equivalent to a wedge sum of two tori, and $X/B$ is homotopic equivalent to a wedge sum of one torus and one circle:

        <img src="public/Pasted image 20230101072605.png" width="600" />

        Then by corollary 2.25 in the book, we get that $\tilde{H}_n(X/A) \cong \tilde{H}_n(S^1 \times S^1) \oplus \tilde{H}_n(S^1 \times S^1)$, thus $H_n(X,A) = \tilde{H}_n(X/A) = \begin{cases} 0&,n=0, n>2\\ \mathbb{Z}^4&,n = 1 \\ \mathbb{Z}^2&,n=2 \end{cases}$. Similarly, $\tilde{H}_n(X/B) \cong \tilde{H}_n(S^1 \times S^1) \oplus \tilde{H}_n(S^1)$ thus $H_n(X,B) = \tilde{H}_n(X/B) = \begin{cases} 0&,n=0, n>2\\ \mathbb{Z}^3&,n = 1 \\ \mathbb{Z}&,n=2 \end{cases}$.

    ## Problem 22

    **Prove by induction on dimension the following facts about the homology of a finite-dimensional CW-complex $X$, using the observation that $X^n/X^{n-1}$ is a wedge sum of $n$-pheres**:

    1. **If $X$ has dimension $n$ then $H_i(X) = 0$ for $i > n$ and $H_n(X)$ is free**;
    2. **$H_n(X)$ is free with basis in bijective correspondence with the $n$-cells if there are no cells of dimension $n-1$ or $n+1$**;
    3. **If $X$ has $k$ $n$-cells, then $H_n(X)$ is generated by at most $k$ elements**.

    Proof

    1. If $n = 0$, then we know the statement is true: $H_i(X) = 0$ for all positive $i$ and $H_0(X) = \mathbb{Z}^m$ which is free where $m$ is the number of points in $X$.
        Suppose now $n>0$ and the statement is true for $n-1$ (in particular, it works for $X^{n-1}$). Then $X^{n-1}$ is not empty because at least it contains some $0$-cells, so the pair $(X^n, X^{n-1})$ makes sense. We have $H_i(X^n, X^{n-1})$ $\cong \tilde{H}_i(X^n/X^{n-1})$ $\cong \tilde{H}_i(\vee^\alpha S^n)$ $\cong \bigoplus_{\alpha}\tilde{H}_i(S^n)$ by the observation and corollary 2.25.
        We know $\tilde{H}_i(S^n) = \mathbb{Z}$ only when $i = n$, so for all $i>n$, we have $H_{i+1}(X^n,X^{n-1}) = 0 \to H_i(X^{n-1}) \to H_i(X^n) \to H_i(X^n, X^{n-1}) = 0$ thus $H_i(X^{n-1}) \cong H_i(X^n) = H_i(X)$. By inductive assumption, $H_i(X^{n-1}) = 0$, thus $H_i(X) = 0$. For $i = n$, we have the exact sequence $H_n(X^{n-1}) = 0 \to H_n(X^n) \xrightarrow{i} \bigoplus_{\alpha}\tilde{H}_n(S^n) = \mathbb{Z}^{\alpha}$ thus $H_n(X^n) = H_n(X)$ must be a subgroup (because $i$ is injective) of $\mathbb{Z}^{\alpha}$, but subgroup of free group is free, thus $H_n(X)$ is free;
    2. Suppose $X$ has dimension $m$. If $n > m$ then by part 1 $H_n(X) = 0$ and the statement is of course true. If $m > n+1$ ($X$ does not have $n+1$-cell so we won't have $m = n+1$), consider $k>n$ and the pair $(X^{k+1}, X^k)$. We have an exact sequence $H_{n+1}(X^{k+1}, X^k) \to H_n(X^k) \to H_n(X^{k+1}) \to H_n(X^{k+1},X^k)$, where by the observation and that $k+1 > n+1$, we get $0 \to H_n(X^k) \to H_n(X^{k+1}) \to 0$ thus $H_n(X^k) \cong H_n(X^{k+1})$. Since this work for any $k > n$, we get that $H_n(X^k) \cong H_n(X^{k+1}) \cong \dots \cong H_n(X^m) = H_n(X)$.
        In particular, take $k = n+1 > n$ we have $H_n(X) \cong H_n(X^{n+1})$. Since we are only interested in $H_n$, thus WLOG we can assume $X = X^{n+1}$. Also by the assumption we know $X = X^n$ and $X^{n-1} = X^{n-2}$.
        If $n = 0$ then we know $H_0(X)$ is free with rank equals the number of points in $X$, so the statement is true. The statement is also trivially true for $n = 1$ because there is no CW-complex without a $0$-cell.
        Suppose $n>1$ (so now $n-2$ makes sense). Consider the pair $(X_n,X^{n-1})$, we get an exact sequence $$H_n(X^{n-1})_{= 0} \to H_n(X^n)_{= H_n(X)} \to H_n(X^n, X^{n-1})_{\cong \mathbb{Z}^{\alpha}} \to H_{n-1}(X^{n-1})_{= H_{n-1}(X^{n-2}) = 0}.$$ Thus $H_n(X) \cong \mathbb{Z}^{\alpha}$ where by the observation, $\alpha$ should be the number of $n$-cells, as desired;
    3. Consider the pair $(X^n, X^{n-1})$, we have an exact sequence $H_n(X^{n-1}) = 0 \to H_n(X^n) \to H_n(X^n, X^{n-1}) \cong \mathbb{Z}^k$, thus $H_n(X^n)$ is a subgroup of $\mathbb{Z}^k$ so is generated by at most $k$ elements.
        Consider the pair $(X^{n+1},X^n)$ and the exact sequence $H_n(X^n) \xrightarrow{i} H_n(X^{n+1}) \to H_n(X^{n+1},X^n) = 0$, so that $i$ must be surjective, and thus $H_n(X^{n+1})$ is generated by at most $k$ elements. Now apply the result we used in part 2, we have $H_n(X) = H_n(X^{n+1})$ thus $H_n(X)$ is generated by at most $k$ elements.

    ## Problem 31

    **Using the notation of the five-lemma, give an example where the maps $\alpha$, $\beta$, $\delta$, and $\varepsilon$ are zero but $\gamma$ is non-zero. This can be done with short exact sequences in which all the groups are either $\mathbb{Z}$ or $0$**.

    Solution

    The following is an example with all groups are either $\mathbb{Z}$ or $0$: $$\begin{CD} 0 @>>> 0 @>>> \mathbb{Z} @>>> \mathbb{Z} @>>> 0 \\ @VVV @VVV @VVV @VVV @VVV \\ 0 @>>> \mathbb{Z} @>>> \mathbb{Z} @>>> 0 @>>> 0 \end{CD}$$ Let each map between $\mathbb{Z}$ and $\mathbb{Z}$ be the identity, and any other map be zero map. In particular, $\alpha$, $\beta$, $\delta$, and $\varepsilon$ are zero but $\gamma$ is non-zero.

    In both lines $0 \to \mathbb{Z} \to \mathbb{Z} \to 0$ satisfies the exactness condition, and each square is commutative (in fact, composition of any two arrows gives the zero map).

    ## Additional Problem

    **Calculate $H_*(\mathbb{C}P^n)$ for all non-negative integers $n$. Use the LES for pairs $(\mathbb{C}P^n, \mathbb{C}P^{n-1})$ and that $\mathbb{C}P^n/\mathbb{C}P^{n-1} = S^{2n}$**.

    Solution

    If $n = 0$ then $\mathbb{C}P^0$ is just a point. If $n = 1$ then $\mathbb{C}P^1 \cong S^2$. So in these cases it's easy to calculate the homology groups.

    Claim: $$H_i(\mathbb{C}P^n) = \begin{cases} \mathbb{Z}&, i\text{ even}, 0\le i \le 2n,\\0&,\text{ otherwise.} \end{cases}$$ We prove the claim with an induction. It's not hard to see this statement is true for $n = 0, 1$. Suppose the statement is true for $n-1$, we show it is true for $n$.

    Consider the pair $(\mathbb{C}P^n, \mathbb{C}P^{n-1})$ we have the following LES: $$\begin{array}{cccccccc} &&&\dots \\ \to & H_{2n+1}(\mathbb{C}P^{n-1}) & \to & H_{2n+1}(\mathbb{C}P^n) & \to & H_{2n+1}(\mathbb{C}P^n, \mathbb{C}P^{n-1}) & \to & \\ \to & H_{2n}(\mathbb{C}P^{n-1}) & \to & H_{2n}(\mathbb{C}P^n) & \to & H_{2n}(\mathbb{C}P^n, \mathbb{C}P^{n-1}) & \to &  \\ \to & H_{2n-1}(\mathbb{C}P^{n-1}) & \to & H_{2n-1}(\mathbb{C}P^n) & \to & H_{2n-1}(\mathbb{C}P^n, \mathbb{C}P^{n-1}) & \to & \\ &&&\dots \\ \to & H_{2m+1}(\mathbb{C}P^{n-1}) & \to & H_{2m+1}(\mathbb{C}P^n) & \to & H_{2m+1}(\mathbb{C}P^n, \mathbb{C}P^{n-1}) & \to & \\ \to & H_{2m}(\mathbb{C}P^{n-1}) & \to & H_{2m}(\mathbb{C}P^n) & \to & H_{2m}(\mathbb{C}P^n, \mathbb{C}P^{n-1}) & \to &  \\ \to & H_{2m-1}(\mathbb{C}P^{n-1}) & \to & H_{2m-1}(\mathbb{C}P^n) & \to & H_{2m-1}(\mathbb{C}P^n, \mathbb{C}P^{n-1}) & \to &\\ &&&\dots \\ \to & H_1(\mathbb{C}P^{n-1}) & \to & H_1(\mathbb{C}P^n) & \to & H_1(\mathbb{C}P^n, \mathbb{C}P^{n-1}) & \to & \\ \to & H_0(\mathbb{C}P^{n-1}) & \to & H_0(\mathbb{C}P^n) & \to & H_0(\mathbb{C}P^n, \mathbb{C}P^{n-1}) & \to &0 \end{array}$$ By the inductive assumption, the fact that $\mathbb{C}P^n$ has dimension $2n$, and that $H_i(\mathbb{C}P^n,\mathbb{C}P^{n-1}) = \tilde{H}_i(S^{2n})$, the above LES is the same as: $$\begin{array}{cccccccc} &&&\dots \\ \to & 0 & \to & 0 & \to & 0 & \to & \\ \to & 0 & \to & H_{2n}(\mathbb{C}P^n) & \to & \mathbb{Z} & \to &  \\ \to & 0 & \to & H_{2n-1}(\mathbb{C}P^n) & \to & 0 & \to & \\ &&&\dots \\ \to & 0 & \to & H_{2m+1}(\mathbb{C}P^n) & \to & 0 & \to & \\ \to & \mathbb{Z} & \to & H_{2m}(\mathbb{C}P^n) & \to & 0 & \to &  \\ \to & 0 & \to & H_{2m-1}(\mathbb{C}P^n) & \to & 0 & \to &\\ &&&\dots \\ \to & 0 & \to & H_1(\mathbb{C}P^n) & \to & 0 & \to & \\ \to & \mathbb{Z} & \to & H_0(\mathbb{C}P^n) & \to & 0 & \to &0 \end{array}$$ So that $0 \to H_{2n}(\mathbb{C}P^n) \to \mathbb{Z} \to 0$ implies $H_{2n}(\mathbb{C}P^n) \cong \mathbb{Z}$; for any $i$ odd, we have $0 \to H_i(\mathbb{C}P^n) \to 0$ thus $H_i(\mathbb{C}P^n) = 0$; and for any $0 \le i < n$ even, we have $0 \to \mathbb{Z} \to H_i(\mathbb{C}P^n) \to 0$ thus $H_i(\mathbb{C}P^n) \cong \mathbb{Z}$, as desired.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Fall Semester Homework 08""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Problem 28

    **Let $X$ be the cone on the $1$-keleton of $\Delta^3$, the union of all line segments joining points in the six edges of $\Delta^3$ to the barycenter of $\Delta^3$. Compute the local homology groups $H_n(X, X-x)$ for all $x \in X$. Define $\partial X$ to be the subspace of points $x$ such that $H_n(X, X - x) = 0$ for all $n$, and compute the local homology groups $H_n(\partial X, \partial X - x)$. Use these calculations to determine which subsets $A \subset X$ have the property that $f(A) \subset A$ for all homeomorphisms $f:X \to X$**.

    Solution

    ### Part 1

    Start by a diagram of the skeleton and the cone:

    <img src="public/image-20241218101640609.png" width="600" />

    So $X$ is a tetrahedron (only the edge and vertices), and a point at the center, and six triangle connecting the center with each side.

    We know that $H_n(X, X-x) \cong H_n(U, U-x)$ by excision where $U$ is a neighborhood of $x$. There are $5$ different type of choices of $x$.

    <img src="public/image-20241218101615122.png" width="600" />

    Consider the LES on pair $(U, U-x)$: $$\begin{array}{cccccccc} &\dots&\to&H_3(U)&\to&H_3(U,U-x)&\to &\\ \to & H_2(U-x) & \to & H_2(U) & \to & H_2(U, U-x) & \to & \\ \to & H_1(U-x) & \to & H_1(U) & \to & H_1(U, U-x) & \to & \\ \to & H_0(U-x) & \to & H_0(U) & \to & H_0(U, U-x) & \to &0 \end{array}$$ Since in any case $U$ has dimension $2$, we don't need to go further.

    1. Case 1, $x$ is a vertex on the skeleton. In this case $U$ is like three triangles identified on one of their sides and $x$ is the common 'tip'. So both $U$ and $U-x$ is contractible, thus the LES becomes $$\begin{array}{cccccccc} &\dots&\to&0&\to&H_3(U,U-x)&\to &\\ \to & 0 & \to & 0 & \to & H_2(U, U-x) & \to & \\ \to & 0 & \to & 0 & \to & H_1(U, U-x) & \to & \\ \to & \mathbb{Z} & \to & \mathbb{Z} & \to & H_0(U, U-x) & \to &0 \end{array}$$ The map $\mathbb{Z} \to \mathbb{Z}$ is surjective because $U$ is path connected and the map is induced by inclusion. Thus $H_0(U,U-x) = 0$, and it implies $H_1(U,U-x) = 0$ (because the preceding SES needs to split). $H_2(U, U-x)$ and $H_3(U, U-x)$ are apparently $0$. So $H_n(U,U-x) = 0$ for any $n$ in this case;
    2. Case 2, $x$ is on an edge of the skeleton. In this case $U$ is half of a disk and $x$ is on its boundary, so again both $U$ and $U-x$ is contractible, so the calculation is the same as case 1, so $H_n(U, U-x) =0$ for all $n$;
    3. Case 3, $x$ is on the interior of one of the triangle connecting an edge and the barycenter. In this case $U$ is a disk and $x$ is in its interior, so $U$ is contractible and $U-x$ is homotopy equivalent with $S^1$, thus the LES becomes $$\begin{array}{cccccccc} &\dots&\to&0&\to&H_3(U,U-x)&\to &\\ \to & 0 & \to & 0 & \to & H_2(U, U-x) & \to & \\ \to & \mathbb{Z} & \to & 0 & \to & H_1(U, U-x) & \to & \\ \to & \mathbb{Z} & \to & \mathbb{Z} & \to & H_0(U, U-x) & \to &0 \end{array}$$ The calculation on $H_0(U, U-x)$ and $H_1(U, U-x)$ is the same, and it's not hard to see $H_2(U, U-x) \cong \mathbb{Z}$ and $H_3(U, U-x) = 0$, so $H_n(U,U-x) = \begin{cases} \mathbb{Z}&,n=2 \\ 0&,\text{ otherwise}\end{cases}$;
    4. Case 4, $x$ is the barycenter. In this case $U$ is $6$ triangles glued together in a way that three of them are glued like in case 1 and the other three are also glued like in case 1, and the two parts are then glued along the sides. $U$ is again contractible, $U-x$ in this case can deformation retract to the skeleton of $\Delta_3$ (think of deformation retract each triangle without a tip to the opposite side). So we first need to calculate the homology groups of $U-x$. Start by giving the skeleton (call it $S$) a CW-complex structure:

        <img src="public/Pasted image 20230101073400.png" width="600" />

        So $C_0(S) \cong \mathbb{Z}^4$ and $C_1(S) \cong \mathbb{Z}^5$, and the boundary operator has $\partial_1(\delta_0)$ (the one correspond to $e_0$) $= v_1 - v_0$, $\partial_1(\delta_1) = v_2 - v_0$, $\partial_1(\delta_2) = v_3 - v_0$, $\partial_1(\delta_3) = v_2 - v_1$, $\partial_1(\delta_4) = v_3 - v_2$, $\partial_1(\delta_5) = v_3 - v_1$. So in general $\partial_1(a_0\delta_0 + \dots + a_5\delta_5) = v_0(-a_0-a_1-a_2) + v_1(a_0 - a_3 - a_5) + v_2(a_1 + a_3 - a_4) + v_3(a_2 + a_4 + a_5)$. We want to get the image and kernel of this map. Write the map in form of matrix and do row reduction, we get from $\begin{pmatrix} -1&-1&-1&0&0&0 \\ 1&0&0&-1&0&-1 \\ 0&1&0&1&-1&0 \\ 0&0&1&0&1&1 \end{pmatrix}$ to $\begin{pmatrix} 1&0&0&-1&0&-1 \\ 0&1&0&1&-1&0 \\ 0&0&1&0&1&1 \\ 0&0&0&0&0&0 \end{pmatrix}$ So the image is $\mathbb{Z}^3$ generated by any three of $v_0,v_1,v_2, v_3$ and thus $H_0(S) = \langle v_0,v_1,v_2,v_3 \rangle/\langle v_0,v_1,v_2 \rangle \cong \mathbb{Z}$. The kernel is also $\mathbb{Z}^{6-3} = \mathbb{Z}^3$, and thus $H_1(S) = \mathbb{Z}^3/0 = \mathbb{Z}^3$. So we get the LES: $$\begin{array}{cccccccc} &\dots&\to&0&\to&H_3(U,U-x)&\to &\\ \to & 0 & \to & 0 & \to & H_2(U, U-x) & \to & \\ \to & \mathbb{Z}^3 & \to & 0 & \to & H_1(U, U-x) & \to & \\ \to & \mathbb{Z} & \to & \mathbb{Z} & \to & H_0(U, U-x) & \to &0 \end{array}$$ So again $H_0(U,U-x), H_1(U, U-x) = 0$ and $H_2(U, U-x) = \mathbb{Z}^3$;
    5. Case 5, $x$ is on an edge of one of the triangles. In this case $U$ is three half disk glued along the straight edge, which is again contractible, and $U-x$ deformation retract to the space below (again we give it a CW-complex structure and call the space $S$):

        <img src="public/Pasted image 20230101073407.png" width="600" />

        So $C_0(S) \cong \mathbb{Z}^2$ and $C_1(S) \cong \mathbb{Z}^3$. We have $\partial_1(e_i) = v_1 - v_0$ thus in general $\partial_1(a_0e_0 + a_1e_1 + a_2e_2) = (a_0+a_1+a_2)(v_1 - v_0)$ and in this case it's rather easy to see the image is isomorphic to $\mathbb{Z}$ and kernel is isomorphic to $\mathbb{Z}^2$ (choice of any two of $a_0,a_1,a_2$ fixes the third one). So similarly as above we have $H_0(S) = \mathbb{Z}$ and $H_1(S) = \mathbb{Z}^2$. So we have the LES: $$\begin{array}{cccccccc} &\dots&\to&0&\to&H_3(U,U-x)&\to &\\ \to & 0 & \to & 0 & \to & H_2(U, U-x) & \to & \\ \to & \mathbb{Z}^2 & \to & 0 & \to & H_1(U, U-x) & \to & \\ \to & \mathbb{Z} & \to & \mathbb{Z} & \to & H_0(U, U-x) & \to &0 \end{array}$$ The only difference is we have $\mathbb{Z}^2$ instead of $\mathbb{Z}^3$ now, so similarly $H_0(U,U-x), H_1(U, U-x) = 0$ and $H_2(U, U-x) = \mathbb{Z}^2$.

    That concludes all the calculation.

    ### Part 2

    From above, we see $\partial X$ consists of points in case 1 and case 2, that is, $\partial X$ is the skeleton. Again we use $H_n(\partial X, \partial X-x) \cong H_n(U, U-x)$ where $U$ is a neighborhood of $x$ in $\partial X$, then there are only two cases:

    1. $x$ is a vertex, in this case $U$ is like a 'Y' shape, so $U$ is contractible, and $U-x$ is three disjoint line segments. So the LES gives: $$\begin{array}{cccccccc} &\dots&\to&0&\to&H_3(U,U-x)&\to &\\ \to & 0 & \to & 0 & \to & H_2(U, U-x) & \to & \\ \to & 0 & \to & 0 & \to & H_1(U, U-x) & \to & \\ \to & \mathbb{Z}^3 & \to & \mathbb{Z} & \to & H_0(U, U-x) & \to &0 \end{array}$$ So with similar argument as above, $H_1(U,U-x) = \mathbb{Z}^2$ otherwise $H_n(U,U-x) = 0$;
    2. $x$ is on (interior of) an edge, in this case $U$ is a line segment is contractible and $U-x$ is two disjoint line segments. We have $$\begin{array}{cccccccc} &\dots&\to&0&\to&H_3(U,U-x)&\to &\\ \to & 0 & \to & 0 & \to & H_2(U, U-x) & \to & \\ \to & 0 & \to & 0 & \to & H_1(U, U-x) & \to & \\ \to & \mathbb{Z}^2 & \to & \mathbb{Z} & \to & H_0(U, U-x) & \to &0 \end{array}$$ So $H_1(U,U-x) = \mathbb{Z}$ otherwise $H_n(U,U-x) = 0$.

    ### Part 3

    From the book: for any homeomorphism $f: X \to X$, we must have $H_n(X, X-x) \cong H_n(X, X-f(x))$.

    Now, notice that the local homology for different cases of $x$ are different (except for case 1 and 2). By the above statement, it follows that $x$ on the skeleton (case 1 & 2) must be sent to a point on the skeleton ($*$). Similarly, points inside the triangles (case 3) must be sent to points inside the triangles; barycenter (case 4) must be sent to barycenter, and points on the edges of the triangles (case 5) must be sent to the edges of triangles.

    Moreover, ($*$) implies that $f:X \to X$ restricted to $\partial X$ must be a homeomorphism $g: \partial X \to \partial X$, thus from part 2 of this problem and with the same argument as above, vertices of the skeleton must be sent to the vertices, and points on the edges of the skeleton must be sent to the edges.

    In other words, $A$ can be the following sets:

    1. Union of $4$ vertices of the skeleton;
    2. Union of $6$ edges of the skeleton;
    3. Union of (interior of) $6$ triangles connecting the barycenter and the edges;
    4. Barycenter (single point);
    5. Union of $4$ edges connecting the barycenter and the vertices;
    6. (and any union of above sets).

    ## Problem 3

    **Let $f: S^n \to S^n$ be a map of degree $0$. Show that there exist points $x, y \in S^n$ with $f(x) = x$ and $f(y) = -y$. Use this to show that if $F$ is a continuous vector field defined on the unit ball $D^n$ in $\mathbb{R}^n$ such that $F(x) \ne 0$ for all $x$, then there exists a point on $\partial D^n$ where $F$ points radially outward and another point of $\partial D^n$ where $F$ points radially inward**.

    Proof

    1. If there is no $x$ such that $f(x) = x$, then $f$ has no fixed point thus it has to have degree $1$ or $-1$, we have a contradiction. If there is no $y$ such that $f(y) = -y$, then $f$ compose with antipodal map has no fixed point thus has to have degree $1$ or $-1$, but degree of composition is product of degree, thus degree of $f$ cannot be zero, we again have a contradiction.

    2. Suppose $F$ is a continuous vector field defined on the unit ball $D^n$ in $\mathbb{R}^n$ such that $F(x) \ne 0$ for all $x$.

       Define a map $F'(x) = \frac{F(x)}{| F(x) |}$, it's well-defined because $F(x) \ne 0$ and $F': D^n \to S^{n-1}$. Compose this map with inclusion map $i: S^{n-1} \to D^n$, we get $G: S^{n-1} \to D^n \to S^{n-1}$. The induced homomorphism $G_* = (F' \circ i)_* = F'_{*} \circ i_*$ on reduced homology where $i_*: \tilde{H}_{n-1}(S^{n-1})\to \tilde{H}_{n-1}(D^n)$ must be the zero map because $D^n$ is contractible. Thus $G_*$ is the zero map thus $G$ have degree $0$ by definition. Thus there exists $x, y \in S^{n-1}$ such that $G(x) = x$ and $G(y) = -y$ by part 1, but this means $F(x) = G(x)| F(x) | = c\cdot x$ is pointing radially outward, and $F(y) = G(y)| F(y) | = -d\cdot y$ is pointing radially inward.

    ## Problem 4

    **Construct a surjective map $S^n \to S^n$ of degree zero, for each $n \ge 1$**.

    Solution

    Apparently a constant map has degree $0$. Since we know that homotopic maps give same induced homomorphism, we may look for surjective maps on $S^n$ that are homotopic to constant map.

    For $n = 1$, we may consider the map $f: S^1 \subset \mathbb{C} \to S^1$ given by $e^{i\theta} \mapsto \begin{cases} e^{i 2 \theta}&, \theta \le \pi\\ e^{i(- 2\theta)}&, \pi < \theta \le \pi \end{cases}$ (the map maps $S^1$ to $S^1$ 'twice', in different directions). It is homotopic to $0$ map through $f_t:S^1 \to S^1$ by $e^{i\theta} \mapsto \begin{cases} e^{i 2\theta(1-t)}&, \theta \le \pi\\ e^{i(-4\pi t+ 2\theta(1-t))}&, \pi < \theta \le \pi \end{cases}$ (don't go full circle each time). As discussed, this map should have degree $0$.

    Build inductively, assume we have a surjective map $f^n$ on $S^n$ that homotopic with the constant map $c: S^n \to S^n$. Consider a map $f^{n+1}$ on $S^{n+1} \cong \lbrace x_0^2 + x_1^2 + \dots + x_n^2 = 1 \rbrace$ such that $f^{n+1}|_{x_0 \in (0,1)\text{ is fixed}} = f^n$ up to a scalar. Since $f^n$ is surjective, $f^{n+1}$ is surjective. $f^{n+1}$ is homotopic to the map sending $S^{n+1}$ to a line segment on $S^{n+1}$ homeomorphic to $[0,1]$, but this map is homotopic to a constant map. So $f^{n+1}$ is a surjective map on $S^{n+1}$ to $S^{n+1}$ that homotopic with a constant map. So it has degree $0$.

    ## Problem 6

    **Show that every map $S^n \to S^n$ can be homotoped to have a fixed point if $n > 0$**.

    Proof

    Suppose we have an arbitrary $f: S^n \to S^n$. If $f$ has a fixed point, then the statement is trivial.

    If not, then first from the book we can homotope $f$ to the antipodal map on $S^n$ through $f_t(x) = \frac{(1-t)f(x)-tx}{| (1-t)f(x)-tx |}$.

    Now suppose $n = 2m - 1$ is odd, then we can view $S^n = \lbrace | z_1|^2 + \dots + | z_m |^2 = 1 \rbrace$ where $z_1, \dots, z_m \in \mathbb{C}$, then notice $e^{i \pi}z_i = - z_i$ and thus the map $f_t(z_1,\dots,z_m) = e^{i (1-t) \pi}(z_1,\dots,z_m)$ gives a homotopy between the antipodal map and the identity map, and identity map of course has a fixed point.

    Otherwise $n = 2m$ is even, in this case we can view $S^n = \lbrace | z_1 |^2 + \dots + | z_{m-1} |^2 + x^2 = 1 \rbrace$ where $z_1, \dots, z_{m-1} \in \mathbb{C}$ and $x \in \mathbb{R}$, and do the similar things as above but ignore $x$, i.e. $f_t(z_1, \dots, z_{m-1}, x) = (e^{i (1-t) \pi}z_1, \dots, e^{i (1-t) \pi}z_{m-1}, -x)$. This gives a homotopy between $f_0$ (antipodal map) and the map $f_1$ which in particular sends $(z_1, \dots, z_{m-1}, 0) \mapsto (z_1, \dots, z_{m-1}, 0)$ (so it also has fixed points).

    Since homotopy is transitive, in either case we get a homotopy between an arbitrary map (without fixed point) to a map with a fixed point.

    ## Problem 9

    **Compute the homology groups of the following $2$-omplexes**:

    1. **The quotient of $S^2$ obtained by identifying north and south poles to a point**;
    2. **$S^1 \times (S^1 \vee S^1)$**.

    Solution

    1. Let us call the space $X$.
    	First we need to give $X$ a CW-complex structure. Let's start with the structure on $S^2$ consists of $2$ $0$-cells (north and south poles), $2$ $1$-cells (connecting the north and south poles), and $2$ $2$-cells (two hemisphere). To identify north and south poles, we just combine the $2$ $0$-cells to one $0$-cell.
    	Thus $C^{CW}_0(X) \cong \mathbb{Z}$, and $C^{CW}_1(X) \cong \mathbb{Z}^2$, $C^{CW}_2(X) \cong \mathbb{Z}^2$, generated by $n$-cells respectively.

        <img src="public/Pasted image 20230101073418.png" width="600" />

        Now we need to evaluate the boundary map $d_n$ 's.
    	There are two $2$-cells: $d_2(f_1) = \varepsilon_{1,1}e_1 + \varepsilon_{1,2}e_2$ where $\varepsilon_{1,i}$ is the degree of $\Delta_{1,i}: S^1_1 \xrightarrow{\varphi} X^1 \xrightarrow{j} X^1/X^0 \xrightarrow{q_i} S^1_i$. We can think of the boundary of the $2$-cell goes once around each $1$-cell once, so both $\varepsilon_{1,i} = 1$, $d_2(f_1) = e_1 + e_2$. The other $2$-cell is doing the similar thing but in the other direction, thus $d_2(f_2) = -e_1 - e_2$. So we can see from the linear dependency that $\ker{d_2} = \langle f_1 + f_2 \rangle$ and $im{d_2} = \langle e_1 + e_2 \rangle$.
    	$d_1$ is easy to compute because there is only one $0$-cell, it is simply the zero map. Thus $\ker{d_1} = \langle e_1,e_2 \rangle$ and $im{d_1} = 0$.
    	Thus $H^{CW}_0(X) = \ker{d_0}/im{d_1}$ $\cong \mathbb{Z}$. $H_1^{CW}(X) = \ker{d_1}/im{d_2}$ $= \langle e_1,e_2 \rangle/\langle e_1 + e_2 \rangle$ $\cong \langle e_1 \rangle$ $\cong \mathbb{Z}$. And $H_2^{CW}(X) = \ker{d_2}/im{d_3}$ $\cong \ker{d_2}$ $= \langle f_1 + f_2 \rangle$ $\cong \mathbb{Z}$. $H_i^{CW}(X)$ for $i \ge 3$ is obviously $0$.
    2. Still, let us call this space $X$ and give it a CW-complex structure. It looks like a bigger donut and a smaller donut where the smaller one's outer longitude is glued with the bigger one's inner longitude. There are $1$ $0$-cell, $3$ $1$-cells, and $2$ $2$-cells. The two cell $f_1$ (the smaller donut) is glued to $X^1$ going along $e_1e_3e_1^{-1}e_3^{-1}$ and $f_2$ (the bigger donut) goes along $e_2e_3e_2^{-1}e_3^{-1}$, just like how we glue the standard torus.

        <img src="public/Pasted image 20230101073422.png" width="600" />

        Evaluate the boundary map: the degree of $\Delta_{1,1}: S^1_1 \xrightarrow{\varphi} X^1 \xrightarrow{j} X^1/X^0 \xrightarrow{q_1} S^1_1$ is zero, because it can be thought as sending the boundary to warp $e_1$ once and then warp it in the different direction. Similarly for other $\Delta_{i,j}$'s. Thus $d_2$ is the zero map. $d_1$ is also the zero map, because there is only one $0$-cell. Thus all boundary maps are zero map.
    	Thus $H_i^{CW}(X) \cong C_i^{CW}(X)$ for each $i$, i.e. $H_n^{CW}(X) = \begin{cases}\mathbb{Z}&,n=0\\\mathbb{Z}^3&,n=1\\\mathbb{Z}^2&,n=2\\0&,\text{ otherwise} \end{cases}$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Fall Semester Homework 09""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Problem 7

    **For an invertible linear transformation $f: \mathbb{R}^n \to  \mathbb{R}^n$ show that the induced map on $H_n(\mathbb{R}^n, \mathbb{R}^n - \lbrace 0 \rbrace)$ $\approx \tilde{H}_{n-1}(\mathbb{R}^n - \lbrace 0 \rbrace)$ $\approx \mathbb{Z}$ is $\text{id}$ or $-\text{id}$ according to whether the determinant of $f$ is positive or negative**. *Hint: Use Gaussian elimination to show that the matrix of $f$ can be joined by a path of invertible matrices to a diagonal matrix with $\pm 1$'s on the diagonal*.

    Proof

    Such a function can be viewed as an element of $GL(n, \mathbb{R})$. We know that $GL(n, \mathbb{R})$ has two (path-, because it's a manifold)connected components, which are preimages of positive numbers or negative numbers under the determinant map. Thus for any $f$, there is either a path connecting $f$ to the identity map (which has positive determinant), or a path connecting $f$ to the map (viewed as matrix) with $-1$ at the top-left corner, $1$ on the other diagonal terms, and $0$ everywhere else (let's call this map $\text{id}'$, it has negative determinant). But a path between maps can be viewed as homotopy, thus $f \sim \text{id}$ or $f \sim \text{id}'$ depending on that if the determinant of $f$ is positive or negative.

    Now the induced map $(\text{id})_*:H_n(\mathbb{R}^n, \mathbb{R}^n - \lbrace 0 \rbrace) \to H_n(\mathbb{R}^n, \mathbb{R}^n - \lbrace 0 \rbrace)$ is of course still $\text{id}$. The induced map $(\text{id}')_*$ is $-\text{id}$ on $\mathbb{Z} \cong \tilde{H}_{n-1}(\mathbb{R}^n - \lbrace 0 \rbrace) \cong H_{n-1}(S^{n-1})$ because it can be viewed as a reflection.

    Since homotopic maps induce same induced map (on relative homology), $f$ induces $\text{id}$ or $-\text{id}$ depending on the sign of its determinant.

    ## Problem 8

    **A polynomial $f(z)$ with complex coefficients, viewed as a map $\mathbb{C} \to \mathbb{C}$, can always be extended to a continuous map of one-point compactifications $\hat{f}: S^2 \to S^2$. Show that the degree of $\hat{f}$ equals the degree of $f$ as a polynomial. Show also that the local degree of $\hat{f}$ at a root of $f$ is the multiplicity of the root**.

    Proof

    Suppose $f$ is a constant map, then the extension $\hat{f}$ is also a constant map (in particular it is not surjective thus have degree $0$), so the statements in the question are true in a rather trivial way.

    So suppose $f$ has positive degree as a polynomial. Extend $f$ to $\hat{f}$ will not add another root ($\infty$ is always sent to $\infty$), and $0$ is always a regular value for $\hat{f}$ (because the differential is always surjective due to fundamental theorem of algebra).

    Suppose $f = c_0 + c_1z + \dots + c_nz^n$, and $z'$ is a root of $f$. Since $\hat{f}|_{\mathbb{C}} = f$ (view $S^2 \cong \overline{C}$), near $z'$ we have $\hat{f}(z) = f(z)$ $= (z-z')^k(a_0 + a_1(z-z') + \dots + a_{n-1}(z-z')^{n-1})$ where $k$ is the multiplicity of the root $z'$. It can be approximated by $a_0(z-z')^k$ because this is the term with lowest degree and $z-z'$ is near $0$. In particular, the local degree of $\hat{f}$ at $z'$ is $k$. This proves the first statement.

    By the formula $\deg{\hat{f}} = \sum \deg{\hat{f}|_{x_i}}$ and by the fact that degree of (complex) polynomial is the sum of multiplicity of distinct roots, we get the other statement.

    ## Problem 10

    **Let $X$ be the quotient space of $S^2$ under the identifications $x \sim -x$ for $x$ in the equator $S^1$. Compute the homology groups $H_i(X)$. Do the same for $S^3$ with antipodal points of the equatorial $S^2 \subset S^3$ identified**.

    Solution

    ### Part 1

    Let us give $S^2$ the usual CW structure of two $0$-cells ($v_1,v_2$), two $1$-cells ($e_1, e_2$), and two $2$-cells ($f_1, f_2$). $f_1$ is attached via $e_1e_2$ and $f_2$ is attached via $e_2^{-1}e_1^{-1}$. If we take the identification $x \sim -x$, then $e_1$ is identified with $e_2$ and $v_1$ is identified with $v_2$, so $f_1$ is now attached via $e_1^2$ and $f_2$ via $e_1^{-2}$. After the identification we get one $0$ and $1$-cell, and two $2$-cells, so the chain groups look like: $0 \to \mathbb{Z}^2 \xrightarrow{d_2} \mathbb{Z} \xrightarrow{d_1} \mathbb{Z} \to 0.$ Since there is only one $0$-cell, $d_1 = 0$.

    From above, we can evaluate $d_2(f_1) = 2e_1$, and $d_2(f_2) = -2e_1$, so $\text{im}(d_2) = \langle 2e_1 \rangle$ and $\ker{d_2} = \langle f_1 + f_2 \rangle$.

    The degree is $2$ because each (regular?) point in the image corresponds to two points from $S^1$, one from each hemisphere. One has local degree $1$ because the map is identity, and the other one also has local degree $1$ because it is identity compose with antipodal map on $S^1$. Thus $H_1(X) \cong \ker{d_1}/\text{im}(d_2)$ $=\langle e_1 \rangle/\langle 2e_1 \rangle$ $\cong \mathbb{Z}_2$, $H_2(X) \cong \ker{d_2}/0 \cong \mathbb{Z}$, and $H_0(X)$ is $\mathbb{Z}$ because the space is path-connected.

    ### Part 2

    Similarly, consider the CW structure after the identification, we have one $0$-cell $v_1$, one $1$-cell $e_1$, one $2$-cell $f_1$ and two $3$-cells $b_1, b_2$. The chain groups: $0 \to \mathbb{Z}^2 \xrightarrow{d_3} \mathbb{Z} \xrightarrow{d_2} \mathbb{Z} \xrightarrow{d_1} \mathbb{Z} \to 0.$ Now in this case, $d_3$ is the zero map, the reason is as above, but this time the degree of antipodal map on $S^2$ is $-1$, so $-1+1 = 0$. $d_2(f_1) = 2e_1$ like part 1, and $d_1 = 0$ because again there is only one $0$-cell. Thus $H_3(X) = \ker{d_3}/0 = \mathbb{Z}^2$, $H_2(X) = \ker{d_2}/\text{im}(d_3)$ $=0$, $H_1(X) = \ker{d_1}/\text{im}(d_2)$ $\cong \langle e_1 \rangle/\langle 2e_1 \rangle \cong \mathbb{Z}_2$, $H_0(X)$ is of course $\mathbb{Z}$.

    ## Problem 20

    **For finite CW-complexes $X$ and $Y$, show that $\chi(X \times Y) = \chi(X)\chi(Y)$**.

    Proof

    Recall that each $i$-cell in $X$ and $j$-cell in $Y$ gives an $i+j$-cell in $X \times Y$. Use that, we have: $$\begin{aligned} \chi(X \times Y)& = \sum\limits_{n}\lbrace(-1)^n \cdot \#~n\text{-cell in } X \times Y \rbrace \\ & =\sum\limits_n\lbrace (-1)^n \cdot \sum\limits_{i+j = n} (\#~i\text{-cell in } X \cdot \#~j\text{-cell in } Y)\rbrace \\ & = \sum\limits_n \sum\limits_{i+j = n} \lbrace (-1)^i\cdot\#~i\text{-cell in } X \cdot (-1)^j \cdot\#~j\text{-cell in } Y)\rbrace \\ & = \sum\limits_i \lbrace (-1)^i\cdot\#~i\text{-cell in } X \rbrace \cdot \sum\limits_j \lbrace(-1)^j \cdot\#~j\text{-cell in } Y)\rbrace \\ & = \chi(X) \cdot \chi(Y) \end{aligned}$$ as desired.

    ## Problem 21

    **If a finite CW-complex $X$ is the union of sub-complexes $A$ and $B$, show that $\chi(X) = \chi(A) + \chi(B) - \chi(A \cap B)$**.

    Proof

    If $A, B$ are sub-complexes of $X$, then $A \cap B$ is also sub-complex of $X$. Since $A \cup B = X$, the number of $i$-cells in $X$ should equal to the number of $i$-cells in $A$ plus number of $i$-cells in $B$, and minus number of $i$-cells in $A \cap B$ because they are double-counted.

    Take the (alternating) summation over $i$, we have: $$\begin{aligned}\chi(X) =& \sum\limits_i(-1)^i \cdot \#~i\text{-cell in }X \\=&\sum\limits_i(-1)^i \cdot (\#~i\text{-cell in }A + \#~i\text{-cell in }B - \#~i\text{-cell in }A \cap B) \\=&\sum\limits_i(-1)^i \cdot \#~i\text{-cell in }A + \sum\limits_i(-1)^i \cdot \#~i\text{-cell in }B - \\&\sum\limits_i(-1)^i \cdot\#~i\text{-cell in }A \cap B \\=&\chi(A) + \chi(B) - \chi(A \cap B)\end{aligned}$$ as desired.

    ## Problem 28

    1. **Use the Mayer-Vietoris sequence to compute the homology groups of the space obtained from a torus $S^1 \times S^1$ by attaching a Möbius band via a homeomorphism from the boundary circle of the Möbius band to the circle $S^1 \times \lbrace x_0 \rbrace$ in the torus**;
    2. **Do the same for the space obtained by attaching a Möbius band to $\mathbb{R}P^2$ via a homeomorphism of its boundary circle to the standard $\mathbb{R}P^1 \subset \mathbb{R}P^2$**.

    Solution

    1. Let us call the space $X$. It consists of a torus $A$ and a Möbius band $B$ such that their intersection is $A \cap B = S^1$. Recall that $H_n(A)= \begin{cases} \mathbb{Z}&,n = 0,2 \\ \mathbb{Z}^2&, n = 1\\0&,\text{ otherwise}\end{cases}$, and $H_n(B)= \begin{cases}\mathbb{Z}&,n = 0,1\\ 0&,\text{ otherwise}\end{cases}$ because it deformation retract to a circle. Also we have $H_n(A \cap B)= \begin{cases}\mathbb{Z}&,n = 0,1\\ 0&,\text{ otherwise}\end{cases}$.
        For the generator: we can think of $H_1(A)$ generated by a longitude and a meridian $e_a^1 = a, e_b^1 = b$, $H_1(B)$ generated by $e_c^1 = c$, and the homology of intersect $H_1(A \cap B)$ generated also by $a$. We have the following Mayer-Vietoris LES in low dimension: $$\begin{array}{cccccccccc} \to & H_2(A \cap B) & \to & H_2(A) \oplus H_2(B) & \to & H_2(X) & \to \\ \to & H_1(A \cap B) & \to & H_1(A) \oplus H_1(B) & \to & H_1(X) & \to \\ \to & \tilde{H}_0(A \cap B) & \to & \tilde{H}_0(A) \oplus \tilde{H}_0(B) & \to & \tilde{H}_0(X) & \to & 0 \\ \end{array}$$ which gives: $$\begin{array}{cccccccc} \to & 0 & \to & \mathbb{Z} & \to & H_2(X) & \to \\ \to & \langle a \rangle & \to & \langle a, b, c \rangle & \to & H_1(X) & \to \\ \to & 0 & \to & 0 & \to & \tilde{H}_0(X) & \to & 0 \\ \end{array}$$ So immediately we have $\tilde{H}_0(X) = 0$, and we have the following exact sequence: $$0 \to \mathbb{Z} \to H_2(X) \xrightarrow{i} \langle a \rangle \xrightarrow{j} \langle a,b,c \rangle \xrightarrow{k} H_1(X) \to 0$$ Now $j$ is induced by the map that sends $a$ to $(a, -2c)$ ($a$ because it just glued to the longitude of the torus, $2c$ because Möbius band goes around its core twice). So $j$ is injective, $\ker{j} = \text{im}(i) = 0$, so we can split this exact sequence to two parts, the first part reads $0 \to \mathbb{Z} \to H_2(X) \to 0$ thus $H_2(X) \cong \mathbb{Z}$. The second part is a short exact sequence $$0\to \langle  a  \rangle \xrightarrow{j} \langle  a,b,c  \rangle \xrightarrow{k} H_1(X) \to 0$$ thus $H_1(X) \cong \langle a,b,c \rangle/\ker{k}$ $\cong \langle a,b,c \rangle/\langle a-2c \rangle$ $\cong \mathbb{Z}^2$.
        So in short, $H_n(X) = \begin{cases} \mathbb{Z}&,n = 0,2 \\ \mathbb{Z}^2&,n = 1 \\ 0&,\text{ otherwise}\end{cases}$.
    2. Again let us call the space $X$, it consists of $A = \mathbb{R}P^2$, $B$ be a Möbius band, their intersection $A \cap B$ is a circle. We know that $H_n(A)= \begin{cases} \mathbb{Z}&,n = 0 \\ \mathbb{Z}_2&, n = 1\\0&,\text{ otherwise}\end{cases}$. $H_n(B)$ and $H_n(A \cap B)$ are the same as part 1.
        For the generator, say $H_1(A)$ is generated by $e^1_a = a$ (but also with a relation $2a = 0$), $H_1(B)$ by $e_b^1$, and $H_1(A \cap B)$ is generated also by $a$ because it's attached directed to the boundary of $A$. The Mayer-Vietoris LES gives: $$\begin{array}{cccccccc} \to & 0 & \to & 0 & \to & H_2(X) & \to \\ \to & \langle a \rangle & \to & \langle a, b \mid 2a = 0 \rangle & \to & H_1(X) & \to \\ \to & 0 & \to & 0 & \to & \tilde{H}_0(X) & \to & 0 \\ \end{array}$$ so again $\tilde{H}_0(X) = 0$ and we have the following exact sequence $0 \to H_2(X) \xrightarrow{i} \langle  a  \rangle \xrightarrow{j} \langle a,b|2a=0 \rangle \xrightarrow{k} H_1(X) \to 0$ Similar as above, we have $j(a) = (a, -2b)$. So again $j$ is injective so with the same reasoning we can split the sequence. The first part immediately gives $H_2(X) = 0$. The second part is again a short exact sequence and we have $H_1(X) \cong \langle a,b|2a = 0 \rangle/\langle a-2b \rangle$ $\cong \langle a,b|2a = 0,a =2b \rangle$, which is isomorphic to $\mathbb{Z}_4$ because $b$ has period $4$.
        So in short, $H_n(X) = \begin{cases} \mathbb{Z}&,n = 0 \\ \mathbb{Z}_4&,n = 1 \\ 0&,\text{ otherwise}\end{cases}$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Fall Semester Homework 10""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Problem 6

    <img src="public/Pasted image 20230101074057.png" width="600" />

    1. **Directly from the definition, compute the simplicial cohomology groups of $S^1 \times S^1$ with $\mathbb{Z}$ and $\mathbb{Z}_2$ coefficients, using the $\Delta$-omplex structure given in section 2.1**;
    2. **Do the same for $\mathbb{R}P^2$**;
    3. **Do the same for a Klein Bottle**.

    Solution

    1. Denote the space (torus) $X$. The simplicial chain complex: $$\dots \to 0 \to \Delta_2(X)_{\cong \langle U, L\rangle} \xrightarrow{\partial} \Delta_1(X)_{\cong \langle a,b,c\rangle} \xrightarrow{\partial} \Delta_0(X)_{\cong \langle v\rangle} \to 0$$ (like we did in the class, for simplicity let us omit all the $\sigma$'s, i.e. $U, L, \dots$ here are all maps) where $\partial(a), \partial(b), \partial(c)$ are all $= v - v = 0$. $\partial(U) = U|_{[v_1,v_2]}-U|_{[v_0,v_2]}+U|_{[v_0,v_1]}$ $= b - c + a$, and $\partial(L) = a-c+b$.
        Apply $\text{Hom}(\_,\mathbb{Z})$, we get: $$0 \leftarrow \text{Hom}(\mathbb{Z}^2,\mathbb{Z})_{\cong\mathbb{Z}^2} \leftarrow^{\delta} \text{Hom}(\mathbb{Z}^3,\mathbb{Z})_{\cong\mathbb{Z}^3} \leftarrow^{\delta} \text{Hom}(\mathbb{Z},\mathbb{Z})_{\cong\mathbb{Z}} \leftarrow 0$$ with generators $\langle \hat{U},\hat{L}\rangle , \langle \hat{a},\hat{b},\hat{c}\rangle , \langle \hat{v}\rangle$ where $\hat{U}$ is the map sending $U \mapsto 1$ and $L \mapsto 0$, etc.
        Evaluate coboundary maps:

        1. $\delta(\hat{v})(a)$ $= \partial^*(\hat{v})(a)$ $= \hat{v}(\partial(a)) = \hat{v}(0) = 0$;
        2. Similarly, $\delta(\hat{v})(b),\delta(\hat{v})(c) = 0$;
        3. $\delta(\hat{a})(U)$ $= \hat{a}(\partial(U))$ $=\hat{a}(b-c+a)$ $= 0 - 0 + 1 = 1$;
        4. $\delta(\hat{a})(L)$ $= \hat{a}(\partial(L))$ $=\hat{a}(a-c+b)$ $= 1 - 0 + 0 = 1$;
        5. $\delta(\hat{b})(U)$ $= \hat{a}(\partial(U))$ $=\hat{a}(b-c+a)$ $= 1$;
        6. $\delta(\hat{b})(L)$ $= \hat{a}(\partial(L))$ $=\hat{a}(a-c+b)$ $= 1$;
        7. $\delta(\hat{c})(U)$ $= \hat{a}(\partial(U))$ $=\hat{a}(b-c+a)$ $= -1$;
        8. $\delta(\hat{c})(L)$ $= \hat{a}(\partial(L))$ $=\hat{a}(a-c+b)$ $= -1$.

        Thus:

        1. $\delta(\hat{v}) = 0$;
        2. $\delta(\hat{a}) = \hat{U} + \hat{L}$;
        3. $\delta(\hat{b}) = \hat{U} + \hat{L}$;
        4. $\delta(\hat{c}) = -\hat{U} - \hat{L}$.

        So observe $\delta$'s are rather simple maps and we don't really need to use matrixes to calculate. We have $\delta_0$ is the zero map, so $\text{im}(\delta_0) = 0$ and $\ker{\delta_0} = \langle \hat{v}\rangle \cong \mathbb{Z}$. $\text{im}(\delta_1) = \langle \hat{U}+ \hat{L}\rangle \cong \mathbb{Z}$, and $\ker{\delta_1} = \langle \hat{a} - \hat{b}, \hat{a} + \hat{c}\rangle$. And we have $H_{\Delta}^0(X; \mathbb{Z}) = \ker{\delta_0} \cong \mathbb{Z}$, $H_{\Delta}^1(X; \mathbb{Z})$ $= \ker{\delta_1}/\text{im}(\delta_0)$ $\cong \mathbb{Z}^2$, and $H_{\Delta}^2(X; \mathbb{Z})$ $= \ker{0}/\text{im}(\delta_1)$ $\cong \langle \hat{U},\hat{L}\rangle /\langle \hat{U}+\hat{L}\rangle$ $\cong \mathbb{Z}$.
        Work with $\mathbb{Z}_2$, everything basically stays the same before the calculation of coboundary maps (replacing $(\_,\mathbb{Z})$ by $(\_,\mathbb{Z}_2)$). For the coboundary map: $\delta_0$ is still $0$, $\delta_1$ also becomes simpler because in $\mathbb{Z}_2$ there is no difference between $\pm 1$, so we have $\delta(\hat{a})(U)$ $= \delta(\hat{b})(U)$ $= \delta(\hat{c})(U)$ $= \delta(\hat{a})(L)$ $= \delta(\hat{b})(L)$ $= \delta(\hat{b})(L) = 1$.
        Thus $H_{\Delta}^0(X; \mathbb{Z}_2) = \ker{\delta_0} \cong \mathbb{Z}_2$, $H_{\Delta}^1(X; \mathbb{Z}_2)$ $= \ker{\delta_1}/\text{im}(\delta_0)$ $=\langle \hat{a} - \hat{b}, \hat{a} - \hat{c}; 2\hat{a}, 2\hat{b}, 2\hat{c}\rangle$ $\cong \mathbb{Z}^2_2$, and $H_{\Delta}^2(X; \mathbb{Z}_2)$ $= \ker{0}/\text{im}(\delta_1)$ $\cong \langle \hat{U},\hat{L}; 2\hat{U}, 2\hat{L}, \hat{U}+\hat{L}\rangle$ $\cong \mathbb{Z}_2$.
    2. Now we have $X = \mathbb{R}P^2$, we have chain complex: $$0 \to \mathbb{Z}^2 \to \mathbb{Z}^3 \to \mathbb{Z}^2 \to 0$$ and cochain complex: $$0 \leftarrow \mathbb{Z}^2_{\cong \langle \hat{U},\hat{L} \rangle} \leftarrow^{\delta} \mathbb{Z}^3_{\cong \langle \hat{a},\hat{b}, \hat{c} \rangle} \leftarrow^{\delta} \mathbb{Z}^2_{\cong \langle \hat{v},\hat{w} \rangle} \leftarrow 0.$$
        Evaluate coboundary maps:

        1. $\delta(\hat{v})(a)$ $= \hat{v}(\partial(a)) = \hat{v}(w - v) = -1$;
        2. $\delta(\hat{v})(b)$ $= \hat{v}(\partial(b)) = \hat{v}(w - v) = -1$;
        3. $\delta(\hat{v})(c)$ $= \hat{v}(\partial(c)) = \hat{v}(v - v) = 0$;
        4. $\delta(\hat{w})(a)$ $= 1$; $\delta(\hat{w})(b)$ $= 1$; $\delta(\hat{w})(c)$ $= 0$;
        5. $\delta(\hat{a})(U)$ $= \hat{a}(b-a+c) = -1$;
        6. $\delta(\hat{a})(L)$ $= \hat{a}(a-b+c) = 1$;
        7. $\delta(\hat{b})(U)$ $= 1$;
        8. $\delta(\hat{b})(L)$ $= -1$;
        9. $\delta(\hat{c})(U)$ $= 1$;
        10. $\delta(\hat{c})(L)$ $= 1$.

        Thus:

        1. $\delta(\hat{v}) = -\hat{a} - \hat{b}$;
        2. $\delta(\hat{w}) = \hat{a} + \hat{b}$;
        3. $\delta(\hat{a}) = \hat{L} - \hat{U}$;
        4. $\delta(\hat{b}) = \hat{U} - \hat{L}$;
        5. $\delta(\hat{c}) = \hat{U} + \hat{L}$.

        So $\ker{\delta_0} = \langle \hat{v}+\hat{w} \rangle$ and $\text{im}(\delta_0) = \langle \hat{a} + \hat{b}\rangle$; $\ker{\delta_1} = \langle \hat{a} + \hat{b} \rangle$ and $\text{im}(\delta_1) = \langle \hat{L} - \hat{U}, \hat{L} + \hat{U} \rangle$.
        Thus $H^0_{\Delta}(X;\mathbb{Z}) \cong \ker{\delta_0} \cong \mathbb{Z}$; $H^1_{\Delta}(X;\mathbb{Z}) \cong \ker{\delta_1}/\text{im}(\delta_0) \cong 0$; $H^2_{\Delta}(X;\mathbb{Z}) \cong \ker{0}/\text{im}(\delta_1)$ $\cong \langle \hat{U}, \hat{L}; \hat{L} - \hat{U}, \hat{L} + \hat{U}\rangle$ $\cong \langle \hat{U}; 2\hat{U}\rangle \cong \mathbb{Z}_2$.
        Work with $\mathbb{Z}_2$, we then have:

        1. $\delta(\hat{v}) = \hat{a} + \hat{b}$;
        2. $\delta(\hat{w}) = \hat{a} + \hat{b}$;
        3. $\delta(\hat{a}) = \hat{U} + \hat{L}$;
        4. $\delta(\hat{b}) = \hat{U} + \hat{L}$;
        5. $\delta(\hat{c}) = \hat{U} + \hat{L}$.

        So these are rather simple maps, and we get $H^0_{\Delta}(X;\mathbb{Z}_2) \cong \mathbb{Z}_2$; $H^1_{\Delta}(X;\mathbb{Z}_2) \cong \langle \hat{a}-\hat{b}, \hat{a} - \hat{c};2\hat{a},2\hat{b},2\hat{c},\hat{a}+ \hat{b}\rangle \cong \mathbb{Z}_2$; $H^2_{\Delta}(X;\mathbb{Z}_2) \cong \mathbb{Z}_2$.
    3. Now we have $X$ being a Klein Bottle. We have chain complex: $0 \to \mathbb{Z}^2 \to \mathbb{Z}^3 \to \mathbb{Z} \to 0$ and cochain complex: $$0 \leftarrow \mathbb{Z}^2_{\cong \langle \hat{U},\hat{L} \rangle} \leftarrow^{\delta} \mathbb{Z}^3_{\cong \langle \hat{a},\hat{b}, \hat{c} \rangle} \leftarrow^{\delta} \mathbb{Z}_{\cong \langle \hat{v} \rangle} \leftarrow 0.$$ Evaluate coboundary maps:

        1. $\delta(\hat{v})$ is clearly the zero map;
        2. $\delta(\hat{a})(U)$ $= \hat{a}(b-c+a) = 1$;
        3. $\delta(\hat{a})(L)$ $= \hat{a}(a-b+c) = 1$;
        4. $\delta(\hat{b})(U)$ $=1$;
        5. $\delta(\hat{b})(L)$ $=-1$;
        6. $\delta(\hat{c})(U)$ $=-1$;
        7. $\delta(\hat{c})(L)$ $=1$.

        Thus:

        1. $\delta(\hat{v}) = 0$;
        2. $\delta(\hat{a}) = \hat{U} + \hat{L}$;
        3. $\delta(\hat{b}) = \hat{U} - \hat{L}$;
        4. $\delta(\hat{c}) = \hat{L} - \hat{U}$.

        So $\ker{\delta_0} = \langle \hat{v} \rangle$ and $\text{im}(\delta_0) = 0$; $\ker{\delta_1} = \langle \hat{b} + \hat{c} \rangle$ and $\text{im}(\delta_1) = \langle \hat{L} - \hat{U}, \hat{L} + \hat{U} \rangle$.
        Thus $H^0_{\Delta}(X;\mathbb{Z}) \cong \ker{\delta_0} \cong \mathbb{Z}$; $H^1_{\Delta}(X;\mathbb{Z}) \cong \ker{\delta_1}/\text{im}(\delta_0) \cong \mathbb{Z}$; $H^2_{\Delta}(X;\mathbb{Z}) \cong \ker{0}/\text{im}(\delta_1) \cong \langle \hat{U}, \hat{L}; \hat{L} - \hat{U}, \hat{L} + \hat{U}\rangle \cong \mathbb{Z}_2$.
        Work with $\mathbb{Z}_2$, we then have:

        1. $\delta(\hat{v}) = 0$;
        2. $\delta(\hat{a}) = \hat{U} + \hat{L}$;
        3. $\delta(\hat{b}) = \hat{U} + \hat{L}$;
        4. $\delta(\hat{c}) = \hat{U} + \hat{L}$.

        Thus $H^0_{\Delta}(X;\mathbb{Z}_2) \cong \mathbb{Z}_2$; $H^1_{\Delta}(X;\mathbb{Z}_2) \cong \langle \hat{a}-\hat{b}, \hat{a} - \hat{c};2\hat{a},2\hat{b},2\hat{c} \rangle \cong \mathbb{Z}_2^2$; $H^2_{\Delta}(X;\mathbb{Z}_2) \cong \mathbb{Z}_2$.

    ## Problem 8

    **Many basic homology arguments work just as well for cohomology even though maps go in the opposite direction. Verify this in the following case**:

    **Compute $H^i(S^n;G)$ by induction on $n$ in two ways: using the long exact sequence of a pair, and using the Mayer-Vietoris sequence**.

    Solution

    We had examples in the class that $H^0(S^1;G) \cong H^1(S^1;G) \cong G$ and $0$ otherwise. So we can use that as the base step.

    Induction Step: consider the pair $(D^n,S^{n-1}= \partial D^n)$. Then the LES of the pair gives us: $$\begin{aligned}\dots \leftarrow H^{i+1}(D^n;G) \leftarrow H^{i+1}(D^n,S^{n-1};G) \\\leftarrow H^i(S^{n-1};G) \leftarrow H^i(D^n;G) \leftarrow \dots\end{aligned}$$ Use that $D^n$ is contractible and that $D^n/S^{n-1} = S^n$, we get that $0 \leftarrow H^{i+1}(S^n;G) \leftarrow H^i(S^{n-1};G) \leftarrow 0$ Which implies that $H^{i+1}(S^n;G) \cong H^i(S^{n-1};G)$. Thus $H^0(S^n;G) \cong H^n(S^n;G) \cong G$ and $0$ otherwise.

    With Mayer-Vietoris sequence: consider $X = S^n$ being the union of two hemisphere (with boundary) $A$ and $B$, then the MV sequence gives: $$\begin{aligned}\dots \leftarrow H^{i+1}(A;G)\oplus H^{i+1}(B;G) \leftarrow H^{i+1}(X; G) \\ \leftarrow H^i(A \cap B;G) \leftarrow H^i(A;G)\oplus H^i(B;G)\leftarrow \dots\end{aligned}$$ Use that $A,B$ are contractible and that $A \cap B \cong S^{n-1}$, we get that $0 \leftarrow H^{i+1}(S^n;G) \leftarrow H^i(S^{n-1};G) \leftarrow 0$ So that they are isomorphic, as above.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Fall Semester Homework 11""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Problem 1

    **Show that there exist nonorientable $1$-dimensional manifolds if the Hausdorff condition is dropped from the definition of a manifold**.

    ## Problem 2

    **Show that the maps $G \to^n G$ and $H \to^n H$ multiplying each element by the integer $n$ induce multiplication by $n$ in $\text{Ext}(H,G)$**.

    ## Problem 3

    **Regarding $\mathbb{Z}_2$ as a module over the ring $\mathbb{Z}_4$, construct a resolution of $\mathbb{Z}_2$ by free modules over $\mathbb{Z}_4$ and use this to show that $\text{Ext}_{\mathbb{Z}_4}^n(\mathbb{Z}_2, \mathbb{Z}_2)$ is non-zero for all $n$**.
    """
    )
    return


if __name__ == "__main__":
    app.run()
