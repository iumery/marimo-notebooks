import marimo

__generated_with = "0.14.16"
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
    mo.md(r"""<img src="public/university of miami logo.gif" alt="university of miami logo" style="display: block; margin: auto; zoom:35%;" />""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# MTH 161 - Calculus I""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Course Information""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Basic Information

    | | |
    | --------------: | :--------------------------------------------- |
    | Instructor | Zedan Liu |
    | Course Section | A1, N1 |
    | Email | zedan.liu@miami.edu or z.liu15@umiami.edu |
    | Office Hour | Monday, Tuesday 9:30 - 11:00 or by appointment |
    | Office Location | Ungar 433 |
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Course Description

    Limits, continuity, derivatives, integrals, and their applications.

    ### Prerequisites

    At least a **C-** in [MTH 108](https://mathematics.miami.edu/undergrad/courses/index.html#MTH108), or one of the following:

    - SAT Math Section Score ≥ 730  
    - ACT Math Score ≥ 31  
    - AP Calculus AB Score ≥ 4  
    - AP Calculus BC Score ≥ 3  
    - ALEKS Score ≥ 78.

    ### General Information

    All course information, policies, and documents are available under the **Course Information** link on the Blackboard course page. Announcements will be posted throughout the semester on Blackboard and sent via email.

    > **It is your responsibility to regularly check Blackboard and stay current with all announcements and materials.**

    ### Diagnostic Quiz

    A diagnostic quiz will be administered during the **first or second week of class**. **This quiz will not affect your course grade.**  
    To prepare, review the [Calculus Prerequisite Review](https://mathematics.miami.edu/_assets/pdf/undergrad/prepare/prepare-calculus.pdf) document.

    ### Organization and Notebooks

    To succeed in this course:

    - Stay organized and plan ahead  
    - Keep a dedicated notebook for class notes and homework problems  
    - Although homework is submitted and graded online, solving each problem by hand is highly recommended. This will be helpful for class discussions, office hours, and exam preparation.

    ### Required Course Materials

    **Textbook**: *Essential Calculus* by Stewart, 2nd edition, ISBN: 9781337772020.

    - The **eBook is available via the 'Canes Course Pack Program**, accessible through the **WebAssign** link on the Blackboard course page  
    - All **homework assignments will also be completed in WebAssign**.  

    ### GradeScope

    All quizzes and exams will be submitted via **GradeScope** for fast and accurate feedback. Access GradeScope through the link on the **Blackboard course homepage**.

    ### Grading Policy

    Final grades will be based on the following components:

    | Component         | Points | Weight | Notes |
    |-------------------|--------|--------|-------|
    | **Midterm Exams** | 550    | 55%    | 3 exams, 75 minutes each. |
    | **Quizzes**       | 150    | 15%    | **At least** 6 quizzes; top 5 scores count. |
    | **Homework**      | 50     | 5%     | Completed on WebAssign. Check deadlines regularly. |
    | **Final Exam**    | 250    | 25%    | Comprehensive, departmental exam (see below). |
    | **Extra Credit**  | +15    | —      | Optional assignments as determined by the instructor. |

    ### Final Exam

    **Date**: Friday, December 5, 2025  
    **Time**: 8:00 PM – 10:30 PM  
    **Room**: To be announced  

    > The exam is a **group final** for all sections of MTH 161. **Do not make travel plans before the date of the final exam.**

    ### Grading Scale

    | Score Range | Letter Grade |
    |-------------|:-------------|
    | 990–1000    | A+           |
    | 920–989     | A            |
    | 895–919     | A−           |
    | 880–894     | B+           |
    | 820–879     | B            |
    | 795–819     | B−           |
    | 780–794     | C+           |
    | 720–779     | C            |
    | 685–719     | C−           |
    | 670–684     | D+           |
    | 585–669     | D            |
    | ≤ 584       | F            |

    ### Final Exam Policy

    Your **final exam score will replace your lowest midterm exam grade** if it is higher. The **final exam grade is never dropped**. Only one midterm exam grade can be replaced.  

    ### Makeup Policy

    Makeup exams or quizzes will only be granted for **excused absences**, including:

    1. Religious holy days  
    2. University-approved academic activities  
    3. Events approved by the Academic Deans' Policy Council  
    4. Verifiable medical excuses with official documentation.  

    **Important**:

    - You must notify your instructor **at least 7 days in advance** for university-approved absences  
    - For emergencies on the exam day, contact your instructor **immediately** with documentation  
    - **No makeups will be allowed more than 7 days after the original date.**  

    ### Testing Policy

    1. You may be required to show **photo ID (Cane Card)** during any exam  
    2. **No calculators, phones, or electronic devices** are permitted during quizzes or exams  
    3. **Exam retakes are not permitted under any circumstances.**
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Honor Code""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Students are expected to adhere to the University of Miami [Honor Code](https://doso.studentaffairs.miami.edu/honor-council/honor-code/index.html) in completing the entirety of this course. Students are to complete all required coursework – exams, quizzes, homework, etc. – on their own. Any work completed in class or online is to be completed without assistance from any other individual, computer program, website, online solver, outside materials, etc.

    The instructor reserves the right, at their discretion, to require an oral examination during an on-campus conference or a live video conference, in order for the student to justify any work submitted for this course.

    Per the Student Rights and Responsibilities Handbook of the University of Miami, the Honor Code "is established for the undergraduate student body to protect the academic integrity of the University of Miami, to encourage consistent ethical behavior among undergraduate students, and to foster a climate of fair competition. While a student's commitment to honesty and personal integrity is assumed and expected, this Code is intended to provide an added measure of assurance that, in fulfilling the University's requirements, a student's work will never involve falsification, plagiarism, or other deception regarding the true nature of the materials presented. Each student is responsible for completing the academic requirements of each course in the manner indicated by the faculty."

    The ultimate responsibility for reading, understanding, and upholding the Honor Code rests with the Student.

    Violations of the Honor Code will be referred to the Academic Integrity Committee of the College of Arts & Sciences (or the Honor Council).

    If a student is found responsible for an Honor Code Violation, the recommended sanction for a violation on an exam or quiz will be a 0 on that assessment. Such a grade of 0 on an assessment will not be replaced by the final exam grade nor will it be dropped from the final average in the course. If a student is found responsible for an Honor Code Violation on the final exam, the recommended sanction will be a grade of 0 and an F in the course.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Academic Support""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Important Dates

    See [Academic Calendar](https://registrar.miami.edu/_assets/pdf/academic-calendar-fall-2025.pdf) and [Final Exam Schedule](https://registrar.miami.edu/_assets/pdf/final-exam-fall-2025.pdf).

    ### Math Lab

    Tutoring is available at the Math Lab for any undergraduate mathematics course, free of charge. The Math Lab is located at the Learning Commons on the 1st floor of the Richter Library. Tutoring will be available in-person, by appointment in 15 to 30 minute intervals. Appointments are made on CaneLink - Navigate. Please check the [Math Lab site](https://mathematics.miami.edu/resources/math-lab/index.html) for information regarding the schedule and tutoring availability.

    ### Camner Center

    The [Camner Center](https://www.camnercenter.miami.edu) offers peer tutoring, free of charge. Please check their website for information on tutoring services and how to request an appointment. The Camner Center also offers many useful workshops on Study Skills, Test Preparation, and more.

    ### Students With Disabilities

    The [Office of Disability Services](https://camnercenter.miami.edu/disability-services/accommodations/index.html) (ODS) provides academic accommodations and support to ensure that students with disabilities are able to access and participate in the opportunities available at the University of Miami. Individuals with disabilities must request academic accommodations through the Office of Disabilities Services.

    *Students with ODS accommodations must provide their instructor with the approved accommodations memo by no later than week 2 of the semester. Requests for extended time must be provided to the instructor at least 7 days in advance of the scheduled exam/quiz.*

    ### Resolution of Issues

    If you have any issue with this class, your first course of action is to contact your instructor for a resolution. If you are unable to resolve the matter with your instructor, you may contact the Department Coordinator.

    | | |
    | ---------------------- | :------------------------------------------------------------ |
    | Department Coordinator | Dr. Leticia Oropesa |
    | Email | l.oropesa@miami.edu |
    | Office Location | Ungar 515F |

    ### Well-Being Resources and Support

    As you complete your coursework, consider how you can maintain your health and well-being as a top priority. To help you become familiar with the many programs and services available on campus, review the information collected on the [Division of Student Affairs Student Well-Being and Resiliency website](https://www.studentaffairs.miami.edu/student-well-being/index.html). Please reach out to the Department Coordinator or any of the resources listed on the site if you need assistance or support throughout the semester.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Course Outline""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Text**: Essential Calculus by Stewart (2nd Edition)

    **Chapter 1: Functions and Limits (all sections)**: Functions and their graphs; limit of a function; limit laws; continuity; limits at infinity; precise definition of limit.

    **Chapter 2: Derivatives (sections 1 - 7)**: Derivatives; formulas for differentiation; derivatives of trigonometric functions; the Chain Rule; implicit differentiation; related rates; differentials.

    **Chapter 3: Applications of Differentiation (sections 1 - 5, 7)**: Maximum and minimum values; the Mean Value Theorem; first derivative test; concavity and points of inflection; curve sketching; applications involving optimization; antiderivatives.

    **Chapter 4: Integral (all sections)**: Area and distances; Riemann Sums; the definite integral and its properties; the Fundamental Theorem of Calculus; evaluating definite and indefinite integrals; change of variable.

    **Chapter 7: Applications of Integration (sections 1, 2)**: Areas between curves; volumes with disk method.
    """
    )
    return


if __name__ == "__main__":
    app.run()
