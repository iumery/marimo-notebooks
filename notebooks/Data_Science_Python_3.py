import marimo

__generated_with = "0.14.9"
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
        },
        orientation="vertical",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Optimization: A Real World Example""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Attention!

    Code in this notebook **WOULD NOT** run directly as Marimo does not include AMPL package (it needs registration anyway). Check AMPL [official website](https://ampl.com) for more info.

    ///
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Imagine a situation like the following: a group of people need to be assigned to a set of projects (assume number of people $S$ is at least as large as number of projects $P$). Each person has two things you know about them:

    - A list of which projects they’d most like to work on, ranked from most to least preferred
    - Their level of ability in a few different skill areas (like communication, coding, or teamwork, there are $T$ of them), each rated as 1, 2, 3, or 4

    The challenge is to assign each person to a team in a way that:

    - Each person is placed on exactly one team, and each team has about the same number of people
    - Respects their preferences as much as possible, so people are placed on projects they’re interested in
    - Balances skills across teams, so no group ends up with all the strongest (or weakest) skill levels

    Let's use `amplpy` to setup a optimization problem and solve an example!
    """
    )
    return


@app.cell
def _():
    """
    from amplpy import AMPL
    import numpy as np
    """
    return


@app.cell
def _():
    r"""
    def AMPL_group_assignment(
        data_matrix: np.ndarray, T: int | None = None, lambda_skill: float = 1.0
    ) -> dict[int, int]:
        '''
        data_matrix: (S, P+T) numpy array, where each row corresponds to one person.
            - The first P columns represent their preference ranking of P projects (1 = most preferred).
            - The last T columns represent skill levels on T different skills, each encoded as an integer in {1, 2, 3, 4}.
        T: Number of skill dimensions. Required to parse the input matrix correctly.
        lambda_skill: Weight for the skill-balancing term in the objective function.

        The function solves a linear program to minimize total dissatisfaction and skill imbalance.

        Returns a dictionary mapping person to assigned project.
        '''

        S: int
        cols: int

        S, cols = data_matrix.shape

        if T is None:
            raise ValueError("Number of skill columns T must be specified.")

        P: int = cols - T

        # Trivial case
        if P == 0:
            raise ValueError("Inferred P = 0, check the input data_matrix or T.")
        elif S < P:
            raise ValueError("Inferred S < P, check the input data_matrix or T.")
        elif P == 1:
            print("There is only 1 project, trivial assignment is returned.")
            return {s: 1 for s in range(1, S + 1)}

        # Input validation
        for s in range(S):
            # Extract preference rankings and skill levels
            prefs: np.ndarray = data_matrix[s, :P]
            skills: np.ndarray = data_matrix[s, P:]

            # Check if prefs form a valid permutation of 1..P
            if set(prefs) != set(range(1, P + 1)):
                raise ValueError(
                    f"Row {s+1} has invalid project rankings: {prefs}. "
                    f"Expected a permutation of [1, ..., {P}]"
                )

            # Check skill levels are all in {1, 2, 3, 4}
            if not np.all(np.isin(skills, [1, 2, 3, 4])):
                raise ValueError(
                    f"Row {s+1} has invalid skill levels: {skills}. "
                    "Each skill must be in {1, 2, 3, 4}"
                )

        L: int = np.floor(S / P)  # Minimum team size
        U: int = np.ceil(S / P)  # Maximum team size

        ampl: AMPL = AMPL()
        ampl.set_option("solver", "gurobi")

        ampl.eval(
            r'''
            param S;
            param P;
            param T;
            param L;
            param U;
            param lambda_skill;

            set PEOPLE := 1..S;
            set PROJECTS := 1..P;
            set SKILLS := 1..T;

            param pref_rank {PEOPLE, PROJECTS};  # Preference ranking: 1 = most preferred
            param skill_level {PEOPLE, SKILLS};  # Skill levels in {1, 2, 3, 4}

            var x {s in PEOPLE, p in PROJECTS} binary;  # x[s, p] = 1 if person s is assigned to project p

            # Each person is assigned to exactly one project
            s.t. OneProjectPerPerson {s in PEOPLE}:
                sum {p in PROJECTS} x[s, p] = 1;

            # Project size constraints
            s.t. ProjectSizeLower {p in PROJECTS}:
                sum {s in PEOPLE} x[s, p] >= L;

            s.t. ProjectSizeUpper {p in PROJECTS}:
                sum {s in PEOPLE} x[s, p] <= U;

            # Global average for each skill across all participants
            param skill_avg {k in SKILLS} :=
                (1.0 / S) * sum {s in PEOPLE} skill_level[s, k];

            # Declare the linear deviation variable
            var skill_dev {p in PROJECTS, k in SKILLS};

            # Absolute value of skill deviation
            var skill_dev_abs {p in PROJECTS, k in SKILLS} >= 0;

            s.t. AbsUpper {p in PROJECTS, k in SKILLS}:
                skill_dev_abs[p,k] >= skill_dev[p,k];

            s.t. AbsLower {p in PROJECTS, k in SKILLS}:
                skill_dev_abs[p,k] >= -skill_dev[p,k];

            # Define the deviation from global average
            s.t. SkillDeviation {p in PROJECTS, k in SKILLS}:
                skill_dev[p, k] =
                    (sum {s in PEOPLE} skill_level[s, k] * x[s, p]) /
                    (sum {s in PEOPLE} x[s, p]) - skill_avg[k];

            # Objective: minimize total dissatisfaction (preference ranks) and skill imbalance
            minimize TotalCost:
                sum {s in PEOPLE, p in PROJECTS} pref_rank[s, p] * x[s, p]
                + lambda_skill * sum {p in PROJECTS, k in SKILLS} skill_dev_abs[p,k];
            '''
        )

        # Set scalar parameters
        ampl.param["S"] = S
        ampl.param["P"] = P
        ampl.param["T"] = T
        ampl.param["L"] = L
        ampl.param["U"] = U
        ampl.param["lambda_skill"] = lambda_skill

        # Set preference rankings
        for s in range(1, S + 1):
            for p in range(1, P + 1):
                ampl.param["pref_rank"][s, p] = int(data_matrix[s - 1, p - 1])

        # Set skill levels
        for s in range(1, S + 1):
            for k in range(1, T + 1):
                ampl.param["skill_level"][s, k] = int(data_matrix[s - 1, P + k - 1])

        # Solve the optimization problem
        ampl.solve()

        # Extract assignment result
        assignment: dict[int, int] = {}
        for s in range(1, S + 1):
            for p in range(1, P + 1):
                if ampl.var["x"][s, p].value() == 1:  # Can set this to `> 0.5` for safety
                    assignment[s] = p

        # Build reverse mapping: project → list of assigned people
        project_groups: dict[int, list[int]] = {p: [] for p in range(1, P + 1)}
        for s, p in assignment.items():
            project_groups[p].append(s)

        # Print per-person assignments and preference ranks
        print("\n=== Participant Assignments ===")
        for s in range(1, S + 1):
            assigned_p: int = assignment[s]
            rank: int = data_matrix[s - 1, assigned_p - 1]
            print(f"  - Person {s}: Project {assigned_p} (Preference Rank = {rank})")

        # Print per-project average skill levels
        print("\n=== Project Skill Averages ===")
        for p in range(1, P + 1):
            group: list[int] = project_groups[p]
            skills_avg: list[float] = []
            for k in range(1, T + 1):
                avg: np.float64 = np.mean([data_matrix[s - 1, P + k - 1] for s in group])
                skills_avg.append(float(round(avg, 2)))
            print(f"  - Project {p}: Members = {group}; Skill Averages = {skills_avg}")
        print()

        return assignment
    """
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Worth to remark: absolute value of skill deviation can be replaced with other metrics. For example, we can replace it with squared deviation. If we do so, the code will be simpler (because there is no more absolute value), but the optimization problem is not linear anymore - it would be a quadratic program (Gorubi can still solve it though)!

    Let's run an example and see how it goes!
    """
    )
    return


@app.cell
def _():
    """
    # Example
    # S = 9 people, P = 4 projects, T = 2 skills
    data: np.ndarray = np.array(
        [
            [3, 4, 1, 2, 1, 2],
            [2, 3, 1, 4, 4, 3],
            [1, 2, 3, 4, 2, 1],
            [2, 1, 4, 3, 3, 2],
            [4, 2, 1, 3, 1, 1],
            [2, 4, 1, 3, 3, 4],
            [1, 3, 4, 2, 2, 3],
            [3, 4, 1, 2, 3, 1],
            [2, 1, 4, 3, 4, 1],
        ]
    )

    assignment: dict[int, int] = AMPL_group_assignment(
        data_matrix=data,
        T=2,
        lambda_skill=1.0,
    )

    print("Group assignments:", assignment)

    # Gurobi 12.0.2:Gurobi 12.0.2: optimal solution; objective 14.61111111
    # 163 simplex iterations
    # 1 branching node
    # absmipgap=5.50671e-14, relmipgap=0

    # === Participant Assignments ===
    #   - Person 1: Project 3 (Preference Rank = 1)
    #   - Person 2: Project 3 (Preference Rank = 1)
    #   - Person 3: Project 1 (Preference Rank = 1)
    #   - Person 4: Project 2 (Preference Rank = 1)
    #   - Person 5: Project 3 (Preference Rank = 1)
    #   - Person 6: Project 1 (Preference Rank = 2)
    #   - Person 7: Project 4 (Preference Rank = 2)
    #   - Person 8: Project 4 (Preference Rank = 2)
    #   - Person 9: Project 2 (Preference Rank = 1)

    # === Project Skill Averages ===
    #   - Project 1: Members = [3, 6]; Skill Averages = [2.5, 2.5]
    #   - Project 2: Members = [4, 9]; Skill Averages = [3.5, 1.5]
    #   - Project 3: Members = [1, 2, 5]; Skill Averages = [2.0, 2.0]
    #   - Project 4: Members = [7, 8]; Skill Averages = [2.5, 2.0]

    # Group assignments: {1: 3, 2: 3, 3: 1, 4: 2, 5: 3, 6: 1, 7: 4, 8: 4, 9: 2}
    """
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Not bad at all! Everyone is assigned to one of their top-two preferred projects, and the skills across groups seem well-balanced!""")
    return


if __name__ == "__main__":
    app.run()
