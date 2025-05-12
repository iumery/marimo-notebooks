import marimo

__generated_with = "0.13.6"
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
    mo.md(
        r"""<img src="public/university of miami logo.png" alt="university of miami logo" style="display: block; margin: auto; zoom:10%;" />"""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# MTH 161 - Calculus I""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    | Instructor | Zedan Liu |
    | -------------- | --------------------------------------------- |
    | Course Section | A1, N1 |
    | Email | zedan.liu@miami.edu or<br/>z.liu15@umiami.edu |
    | Office Hour | By arrangement |
    | Text | Essential Calculus by Stewart (2nd Edition) |
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Course Description**: Limits and continuity, derivatives and applications, definite integral and applications.

    **Prerequisite**: At least a C- in [MTH 108](https://mathematics.miami.edu/undergrad/courses/index.html#MTH108) or SAT Math Section Score $\ge$ 730 or Math ACT Score $\ge$ 31 or AP Calculus AB score of 4 or AP Calculus BC score of 3 or ALEKS score $\ge$ 78 together with completion of high school trigonometry and analytic geometry.

    **General Information**: Please read all the information and documents found under the Course Information link on the UM Blackboard course page. On UM Blackboard, you will find the course schedule, course announcements, videos, Zoom links, and other relevant course documents. All homework assignments for this course will be completed in WebAssign. In WebAssign you can also find the complete digital textbook, video clips and other study tools.

    This course will have many materials available on Blackboard, including course notes, reference materials, videos, and so on. It is your responsibility to catch up on material covered during any class days missed for whatever reason.

    There will be a diagnostic quiz administered in the first or second week of class.  This will not affect your grade in the course but will be used for determination of readiness for MTH 161. To prepare for this quiz and the course, you are strongly encouraged to look through the "Prepare for Success" Calculus Prerequisite Review posted [here](https://mathematics.miami.edu/_assets/pdf/undergrad/prepare/prepare-calculus.pdf).

    **Communication**: Communication is very important. Please be sure to check your UM email and Blackboard announcements frequently. It is your responsibility to be aware of any information discussed in class, sent to you by email, or posted on Blackboard.

    **Class Recordings**: Select class meetings, discussion meetings, and office hours for this class may require a Zoom connection and may be recorded. By enrolling in this course and participating in these class activities, you grant your instructor, and the University, the right to use any portion of these recordings as a learning tool in this class section. Any recordings will be available to students registered for this class, as they are intended to supplement the classroom experience. Students are expected to follow appropriate University policies and maintain the security of passwords used to access recorded lectures. Recordings may not be reproduced, shared with those not in the class, or uploaded to other online environments. Students are expressly prohibited from recording any part of this course or downloading and distributing any class video recording. If the instructor or a University of Miami office plans any other uses for the recordings, beyond this class, students identifiable in the recordings will be notified to request consent prior to such use.

    **Intellectual Property**: Pursuant to the University's Policy on Inventions, Intellectual Property, and Technology Transfer, "courseware" includes: course syllabi, assignments, assessments, course notes, and/or other materials that are first created and made available to students as part of the educational curriculum at the University.

    Your instructor and/or the University is the copyright owner of the courseware. Individual downloading or recording of any course video or course materials/documents issued to you or posted in Blackboard is not allowed; individual downloading or recording of any in-person or virtual class session is not allowed; such materials cannot be shared outside the physical or virtual classroom environment. All course materials are protected by copyright laws and misuse of the materials is a violation of the Student Rights and Responsibilities Handbook. Violations will be reported to the Dean of Students.

    **Organization and Notebooks**: To succeed in this course it is important to be organized and to plan ahead. Students are expected to keep an organized notebook for class notes and for homework. Although homework is submitted online and graded, it is extremely helpful to have the homework problems worked out in your notebook in order to refer to them when asking questions in class or during office hours and when preparing for an exam.

    **Technical Requirement**: Since portions of this class may use an online platform, students will be required to have or complete the following:

    1. A computer or laptop with reliable internet connection;
    2. A functioning web camera, speakers, and microphone. A headset or earphones may be helpful;
    3. Set up your UMiami Zoom account. Go to miami.zoom.us and select SSO log in. Sign in using your UM credentials and Duo Authentication. Download the Zoom app on your computer or laptop and phone.

    **Required Course Materials**: The textbook for this course is Essential Calculus by Stewart, 2nd edition, ISBN 9781337772020. Access to WebAssign and the ebook is available to you through the 'Canes Course Pack Program. Please click on the WebAssign link on the Course homepage in Blackboard.

    The 'Canes Course Pack provides students with access to their required course materials at the start of each semester. The 'Canes Course Pack allows the university to reduce student course material costs compared to traditional print text and ensures every student can access their course materials on or before the first day of class. Undergraduate students are automatically enrolled in the 'Canes Course Pack when they register for their courses. This enrollment will provide students with all required materials for class for one low, flat fee. Course materials will be provided to the student in a digital format, or a physical format when digital is not available. Print materials do not need to be returned at the end of the semester.

    **GradeScope**: GradeScope allows us to provide fast and accurate feedback on your quizzes and Exams. You will enroll in GradeScope with an entry code given by your instructor. The entry code for this class is **2BXRR2**.

    1. If you don't have a GradeScope account yet, go to [GradeScope](https://www.gradescope.com/) , click Sign Up in the upper right corner, select Student, and put in your entry code in the sign-up form;
    2. If you already have a GradeScope account, go to [GradeScope](https://www.gradescope.com/) , log into that account and navigate to your Account Dashboard by clicking the GradeScope logo in the top left and click Add Course in the bottom right corner. Then enter your course code.

    **Grading Policy**: Final grades for this course will be based on the following:

    1. Midterm Exams (550 points): There will be three midterm exams scheduled during the semester. The exams will be held during a 75 minutes class period. Details, content, and instructions will be provided later in class and in the Announcements on Blackboard;
    2. Quizzes (150 points): There will be at least 6 quizzes during the semester. If more than 6 quizzes were given, only the 6 quizzes with the highest scores would be counted toward the final grade. The date and content of the quizzes will be announced in class;
    3. Homework (50 points): Homework will be assigned and completed in WebAssign. The student is responsible for checking WebAssign frequently for upcoming deadlines for these assignments;
    4. Final Exam (250 points): The final exam for the course is scheduled as a Group Exam on campus, meaning all sections of MTH 161 will be taking the exam at the same time. The final exam will be a comprehensive departmental exam. A review packet will be provided to all students taking this course;
    5. Extra Credit: Each student may earn up to 15 points of extra credit by completing assignments as determined by the instructor.

    The group final exam for all sections of MTH 161 is scheduled on **Thursday, May 1st, 2025, 08:00 PM to 10:30 PM**. Room assignment is to be announced. Please do not make plans to travel before the date of the final exam.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Grading Scale**:

    | Score | Letter Grade |
    | ------------- | ------------ |
    | 990-1000 | A+ |
    | 920-989 | A |
    | 895-919 | A- |
    | 880-894 | B+ |
    | 820-879 | B |
    | 795-819 | B- |
    | 780-794 | C+ |
    | 720-779 | C |
    | 685-719 | C- |
    | 670-684 | D+ |
    | 585-669 | D |
    | 584 and below | F |

    Final Exam Score Replaces Lowest Midterm Exam: Your (weighted) score on the final exam will replace your lowest midterm exam grade, provided it is higher. The final exam grade is never dropped. Only one midterm exam grade will be replaced. The final exam will count in place of any missed exam due to an unexcused absence and no other exam grade will be replaced.

    **Quiz and Midterm Exam Schedule**: Please refer to the tentative class schedule posted on Blackboard.

    **Makeup Policy**: Makeups will be given only for excused absences as defined below:

    1. A religious holy day. 
    2. A student has participated in an activity approved by the Academic Deans' Policy Council, such as music and debate activity, R.O.T.C. function, or varsity athletic trip (Issued by the sponsor when authorized by the Executive Vice President and Provost);
    3. A student has participated in a special academic activity, such as a field trip or other special event connected with coursework. (Issued by the sponsor when authorized by the Executive Vice President and Provost);
    4. A student has a verifiable medical excuse which consists of written documentation from a medical provider such as the Student Health Center or a physician confirming the absence was due to illness or hospitalization.

    Any student who will be missing an exam or quiz for a university approved event must notify their instructor 7 days in advance. If an emergency occurs on the day of the exam, falling within the University approved reasons, you must contact the instructor immediately and provide supporting document. No makeup exam will be scheduled after the graded exams are returned to the class.

    **Testing Policy**:

    1. Any student may be asked to present photo identification during an exam;
    2. No calculators and other electronic devices will be allowed during quizzes and exams;
    3. Repeating an exam will not be permitted under any circumstances.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Honor Code""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Students are expected to adhere to the University of Miami [Honor Code](https://doso.studentaffairs.miami.edu/honor-council/honor-code/index.html) in completing the entirety of this course. Students are to complete all required coursework – exams, quizzes, homework, etc. – on their own. Any work completed in class or online is to be completed without assistance from any other individual, computer program, website, online solver, outside materials, etc.

    Your instructor reserves the right, at their discretion, to require an oral examination during an on-campus conference or a live video conference, in order for you to justify any work that you have submitted for this course.

    Per the Student Rights and Responsibilities Handbook of the University of Miami, the Honor Code "is established for the undergraduate student body to protect the academic integrity of the University of Miami, to encourage consistent ethical behavior among undergraduate students, and to foster a climate of fair competition. While a student's commitment to honesty and personal integrity is assumed and expected, this Code is intended to provide an added measure of assurance that, in fulfilling the University's requirements, a student's work will never involve falsification, plagiarism, or other deception regarding the true nature of the materials presented. Each student is responsible for completing the academic requirements of each course in the manner indicated by the faculty."

    **The Honor Creed**: As a student of the University of Miami, I commit myself to upholding the Honor Code and promoting the values of Honesty, Responsibility, and Integrity.

    The ultimate responsibility for reading, understanding, and upholding the Honor Code rests with the Student.

    Violations of the Honor Code will be referred to the Academic Integrity Committee of the College of Arts & Sciences (or the Honor Council).

    If a student is found responsible for an Honor Code Violation, the recommended sanction for a violation on an exam or quiz will be a 0 on that assessment. Such a grade of 0 on an assessment will not be replaced by the final exam grade nor will it be dropped from the final average in the course. If a student is found responsible for an Honor Code Violation on the final exam, the recommended sanction will be a grade of 0 and an F in the course.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Academic Support""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **[Academic Calendar](https://registrar.miami.edu/_assets/pdf/academic-calendar-spring-2025.pdf)** and **[Final Exam Schedule](https://registrar.miami.edu/_assets/pdf/final-exam-spring-2025.pdf)**.

    **Math Lab**: Tutoring is available at the Math Lab for any undergraduate mathematics course, free of charge. The Math Lab is located at the Learning Commons on the 1st floor of the Richter Library. Tutoring will be available in-person, by appointment in 15 to 30 minute intervals. Appointments are made on CaneLink - Navigate. Please check the [Math Lab site](https://mathematics.miami.edu/resources/math-lab/index.html) for information regarding the schedule and tutoring availability.

    **Camner Center**: The [Camner Center](https://www.camnercenter.miami.edu) offers peer tutoring, free of charge. Please check their website for information on tutoring services and how to request an appointment. The Camner Center also offers many useful workshops on Study Skills, Test Preparation, and more.

    **Students With Disabilities**: The [Office of Disability Services](https://camnercenter.miami.edu/disability-services/accommodations/index.html) (ODS) provides academic accommodations and support to ensure that students with disabilities are able to access and participate in the opportunities available at the University of Miami. Individuals with disabilities must request academic accommodations through the Office of Disabilities Services. The ODS is located at the Camner Center for Academic Resources, Student Services Building, 1307 Stanford Drive, 2nd Floor. ODS staff can be reached at 305-284-2374.

    Students with ODS accommodations must provide their instructor with the approved accommodations memo by no later than week 2 of the semester. Requests for extended time must be provided to the instructor at least 7 days in advance of the scheduled exam/quiz.

    **Resolution of Issues**: If you have any issue with this class, your first course of action is to contact your instructor for a resolution. If you are unable to resolve the matter with your instructor, you may contact the Department Coordinator.

    | Department Coordinator | Dr. Leticia Oropesa |
    | ---------------------- | ------------------------------------------------------------ |
    | Email | l.oropesa@miami.edu |
    | Office Hours | In-person at Ungar 515F<br/>Mondays, Tuesdays, Wednesdays, Thursdays 3:00 PM to 5:00 PM<br/>Schedule a meeting at [Calendly](https://calendly.com/l-oropesa/dr-oropesa-s-office-hours) or by arrangement |

    **Well-Being Resources and Support**: As you complete your coursework, consider how you can maintain your health and well-being as a top priority. To help you become familiar with the many programs and services available on campus, review the information collected on the [Division of Student Affairs Student Well-Being and Resiliency website](https://www.studentaffairs.miami.edu/student-well-being/index.html). Please reach out to the Department Coordinator or any of the resources listed on the site if you need assistance or support throughout the semester.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Course Outline""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Text: Essential Calculus by Stewart (2nd Edition)

    Chapter 1: Functions and Limits (all sections)

    Functions and their graphs; limit of a function; limit laws; continuity; limits at infinity; precise definition of limit.

    Chapter 2: Derivatives (sections 1 - 7)

    Derivatives; formulas for differentiation; derivatives of trigonometric functions; the Chain Rule; implicit differentiation; related rates; differentials.

    Chapter 3: Applications of Differentiation (sections 1 - 5, 7)

    Maximum and minimum values; the Mean Value Theorem; first derivative test; concavity and points of inflection; curve sketching; applications involving optimization; antiderivatives.

    Chapter 4: Integral (all sections)

    Area and distances; Riemann Sums; the definite integral and its properties; the Fundamental Theorem of Calculus; evaluating definite and indefinite integrals; change of variable.

    Chapter 7: Applications of Integration (sections 1, 2, 3)

    Areas between curves; volumes with disk method, washer method, cylindrical shells.
    """
    )
    return


if __name__ == "__main__":
    app.run()
