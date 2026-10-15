INTENT_RESPONSES = {
    "GREETINGS": """
    Hello! Welcome to Q-TIP, your TIP assistant. How can I help you?
    """,

    # ------------------------------------------------------------------
    # ADMISSION AND ENROLLMENT
    # ------------------------------------------------------------------
    "ENROLLMENT_GENERAL": """
    TIP enrollment depends on your student category: college freshman, Grade 11 applicant, transferee, continuing student, returnee, or graduate student.
    New applicants start with online registration at https://admission.tip.edu.ph/web/.
    Tell me your category and I can give you the exact steps.
    Admission requirements: https://tip.edu.ph/be-a-tip-ian/tip-admission-requirements/
    """,

    "ENROLL_COLLEGE": """
    Enrollment process for college freshmen:
    1. Online registration and submission and evaluation of admission credentials: https://admission.tip.edu.ph/web/ (you may also apply for entrance scholarships here).
    2. Interview with the Security, Occupational, Health and Safety office (SOHAS) and the Guidance and Counseling Center (GCC). Only applicants with a 75%-79% GWA take the TIP entrance exam.
    3. Registration and assessment of fees: encode your courses and sections, then print the enrollment assessment form.
    4. Payment: pay at the teller and receive your official receipt.
    5. Issuance of the Official Registration Form: print it.
    After that, you can take care of your ID application, library validation, medical and dental exam, and the Math Enhancement Program (MEP).
    Admission requirements: https://tip.edu.ph/be-a-tip-ian/tip-admission-requirements/
    """,

    "ENROLL_GRADE11": """
    Enrollment process for Grade 11 applicants:
    1. Online registration and submission and evaluation of admission credentials: https://admission.tip.edu.ph/web/ (you may also apply for entrance scholarships here).
    2. Interview with SOHAS and the Guidance and Counseling Center (GCC). Only applicants with a 75%-79% GWA take the TIP entrance exam.
    3. Registration and assessment of fees: encode your courses and sections, then print the enrollment assessment form.
    4. Payment: pay at the teller and receive your official receipt.
    5. Issuance of the Official Registration Form: print it.
    Afterward, you can do your ID application, library validation, and medical and dental exam at your own convenience.
    Admission requirements: https://tip.edu.ph/be-a-tip-ian/tip-admission-requirements/
    """,

    "ENROLL_GRADE12": """
    For Grade 12 enrollment, check TIP's official admission and enrollment announcements at https://admission.tip.edu.ph/.
    If you are a continuing TIP Senior High School student, process your enrollment through ARIS and complete any required clearances and advising first.
    """,

    "ENROLL_GRADE12_CONTINUING": """
    Online enrollment for continuing TIP Senior High School students:
    1. Clearance: students on academic probation seek study load advice from the GCC. Returnees secure readmission clearance from the Office of Student Affairs (OSA), Student Accounting Services (SAS), and SOHAS. Students with liabilities must clear them with the concerned offices.
    2. Pre-register through your ARIS student portal.
    QC: https://webqc2.tip.edu.ph/portal/student/new/public/login.php
    Manila: https://webmla2.tip.edu.ph/portal/student/new/public/login.php
    3. Advising: consult your Academic Adviser about which courses to enroll in. The Program Evaluator will validate and encode the advised courses.
    4. Print your enrollment form.
    5. Pay at the teller and get your official receipt.
    """,

    "ENROLL_TRANSFEREE": """
    Enrollment process for transferees:
    1. Online registration and submission and evaluation of admission credentials: https://admission.tip.edu.ph/web/ (you may also apply for entrance scholarships here).
    2. Interview with SOHAS, the Office of Student Affairs (OSA), and the GCC. Transferees are required to take the TIP entrance exam.
    3. Evaluation of credits and drug testing: ask your Program Chair about credit evaluation, and get the drug testing consent form at the SRO.
    4. Registration and assessment of fees: encode your courses and sections, then print the enrollment assessment form.
    5. Payment: pay at the teller and receive your official receipt.
    6. Issuance of the Official Registration Form: print it.
    Afterward, you can do your ID application and library validation at your own convenience.
    """,

    "ENROLL_CONTINUESTUDENT": """
    Online enrollment for continuing college students without concerns:
    1. Pre-register using your EmpowerED student portal.
    QC: https://student-qc.tip.edu.ph/login
    Manila: https://student-mla.tip.edu.ph/login
    2. Print your enrollment form.
    3. Pay at the teller or online. You can request your official receipt onsite.

    For students with concerns (including returnees), do these steps instead:
    1. Clearance: students on academic probation seek study load advice from the GCC. Returnees secure readmission clearance from the Office of Student Affairs (OSA), Student Accounting Services (SAS), and SOHAS. Students with liabilities secure clearance from the concerned offices.
    2. Pre-register using your EmpowerED student portal (links above).
    3. Advising: seek advice from your Academic Adviser on which courses to enroll in. The Program Evaluator will validate and encode the advised courses.
    4. Print your enrollment form.
    5. Pay at the teller and get your official receipt.
    Academic advisers are available onsite. The Office of the Registrar may validate courses for course credit, course equivalency, overload, simultaneous enrollment, and posting of elective courses.
    """,

    "ENROLLMENT_SCHEDULE": """
    TIP is now accepting college applications for SY 2026-2027. Apply here: https://admission.tip.edu.ph/
    Schedules for other categories may vary by campus and program. Check the admission website or contact the Admissions Office for announcements.
    Admission requirements: https://tip.edu.ph/be-a-tip-ian/tip-admission-requirements/
    """,

    "ENROLLMENT_FORM": """
    For online registration, fill out the form at https://admission.tip.edu.ph/web/.
    Graduate applicants will receive a reference number and an email confirmation after filling out the form, then submit their requirements through their campus link:
    QC: https://bit.ly/TIPQCGradProgramApplication
    Manila: https://bit.ly/TIPMNLGradProgramApplication
    """,

    "ADMISSION_REQUIREMENTS": """
    TIP's admission requirements are available at:
    https://tip.edu.ph/be-a-tip-ian/tip-admission-requirements/
    Requirements may vary depending on your applicant category and program.
    For other concerns, contact the Admissions Office:
    QC: admissions.qc@tip.edu.ph | 8911-0964 loc. 305
    Manila: admissions.manila@tip.edu.ph | 8733-9117 loc. 102
    """,

    # ------------------------------------------------------------------
    # GRADUATE STUDIES
    # ------------------------------------------------------------------
    "GRADUATE_PROGRAMS": """
    TIP graduate programs:
    Doctoral: Doctor in Information Technology (DIT); Doctor of Philosophy in Computer Science (Manila only); Doctor of Engineering with specialization in Computer Engineering (QC only).
    Master's: Professional Science Master's in Data Science; Professional Science Master's in Construction Management (QC only); Professional Science Master's in Engineering Management; Master in Logistics and Supply Chain Management (QC only); Master in Information Technology; Master of Science in Computer Science; Master in Information Systems.
    Master of Engineering in: Chemical Engineering (Manila only), Civil Engineering (QC only), Computer Engineering, Electrical Engineering, Electronics Engineering (QC only), Industrial Engineering (QC only), and Mechanical Engineering.
    Apply:
    QC: https://bit.ly/TIPQCGradProgramApplication
    Manila: https://bit.ly/TIPMNLGradProgramApplication
    """,

    "GRADUATE_ENROLLMENT": """
    Enrollment process for incoming graduate students:
    1. Fill out the online application form at https://admission.tip.edu.ph/web.
    2. You will receive a reference number and an email confirmation.
    3. Submit your requirements and reference number.
    QC: https://bit.ly/TIPQCGradProgramApplication
    Manila: https://bit.ly/TIPMNLGradProgramApplication
    4. Your requirements will be verified and evaluated.
    5. Expect an email about the evaluation results.
    6. If accepted, tell the Graduate Programs Coordinator (GPC) how many units you plan to enroll. The GPC will pre-register you.
    7. The GPC will email you the pre-enrollment form with your courses, fees, payment instructions, and a guide to registering in EmpowerED ARIS.
    8. Pay through Dragonpay, PayApp, BDO, or Landbank online banking.
    9. Attend the online school orientation. The schedule will be sent by email.
    """,

    "ENROLL_CONTINUE_GRADUATE": """
    Enrollment process for continuing graduate students:
    1. Log in to your ARIS student portal.
    QC: https://webqc2.tip.edu.ph/portal/student/new/public/login.php
    Manila: https://webmla2.tip.edu.ph/portal/student/new/public/login.php
    2. Select your courses and inform the Graduate Programs Coordinator for approval.
    3. Save the transaction.
    4. Print the pre-enrollment form.
    5. Pay through Dragonpay, PayApp, BDO, or Landbank online banking.
    """,

    # ------------------------------------------------------------------
    # PROGRAMS
    # ------------------------------------------------------------------
    "OFFERED_COURSES": """
    TIP offers:
    College: Engineering and Architecture, Information Technology Education, Business Education, Teacher Education, and Arts and Mathematics.
    Senior High School (Academic Track): ABM, HUMSS, STEM, and General Academic.
    Graduate: doctoral and master's programs in fields such as Information Technology, Computer Science, Engineering, and Data Science.
    Program availability may vary by campus. Check https://www.tip.edu.ph/ for the latest list.
    """,

    "COLLEGE_PROGRAMS": """
    TIP college program offerings:
    - Engineering and Architecture
    - Information Technology Education
    - Business Education
    - Teacher Education
    - Arts and Mathematics
    For the latest program list and availability per campus, visit https://www.tip.edu.ph/.
    """,

    "SHS_PROGRAMS": """
    TIP Senior High School offers the Academic Track in 4 strands:
    - Accountancy, Business and Management (ABM)
    - Humanities and Social Sciences (HUMSS)
    - Science, Technology, Engineering and Mathematics (STEM)
    - General Academic
    Check https://www.tip.edu.ph/ for campus availability.
    """,

    "ENROLL_SHS_GENERAL": """
    Enrollment for TIP Senior High School (SHS):
    New Grade 11 applicants:
    1. Register online at https://admission.tip.edu.ph/web/ (you may also apply for entrance scholarships here).
    2. Interview with SOHAS and the Guidance and Counseling Center (GCC). Only applicants with a 75%-79% GWA take the TIP entrance exam.
    3. Registration and assessment of fees.
    4. Pay at the teller and get your official receipt.
    5. Print your Official Registration Form.
    Continuing SHS students enroll through their ARIS student portal after completing any required clearances and advising.
    TIP SHS offers the Academic Track in 4 strands: ABM, HUMSS, STEM, and General Academic.
    Ask me about Grade 11, Grade 12, or continuing SHS enrollment for the detailed steps.
    """,

    "TECHNOCORE": """
    TIP TechnoCoRe was established in 2017 to build Technopreneurship and Collaborative Applied Research into TIP education.
    It teaches four core technopreneurship skills: problem-opportunity formulation, ideation, validation, and execution, to students, faculty, researchers, and other stakeholders.
    It also builds collaborative applied research partnerships with government, industry, and other organizations.
    In 2019, TIP opened the TechnoCoRe building at its Quezon City campus, a seven-storey innovation hub with classrooms, seminar rooms, computer rooms, and engineering, computing, and fabrication laboratories.
    """,

    "CREDIBILITY": """
    TIP's academic quality is recognized locally and internationally:
    - ABET accreditation of 20 engineering and computing programs (first in 2013, reaccredited in 2019)
    - Seoul Accord recognition for BSCS, BSIS, and BSIT
    - AUN-QA assessment of 20 programs, plus the AUN-QA Institutional Assessment
    - ISO 9001 certification since 1999 and ISO 21001:2018 certification as of 2024
    - 16 CHED Centers of Excellence and Development
    - CHED Autonomous Status for both campuses for 2024-2027
    Ask me about accreditation for more details.
    """,

    "ACCREDITATION": """
    TIP accreditations:
    ABET: first accredited in 2013 (14 programs from the Engineering Accreditation Commission and 6 from the Computing Accreditation Commission). All 20 engineering and computing programs were reaccredited in 2019.
    Seoul Accord: since 2015, the BSCS, BSIS, and BSIT programs are recognized through their ABET CAC accreditation, so graduates enjoy recognition of their degrees in countries such as South Korea, Canada, Australia, the UK, the US, China, and Japan.
    AUN-QA: since 2021, 20 programs have been assessed, and TIP recently passed the Institutional Assessment.
    ISO: certified to ISO 9001 since 1999 (by DNV) and to ISO 21001:2018 for Educational Organizations Management System as of 2024.
    Local: PACUCOA (under FAAP), the Philippine Technological Council, and the PCS Information and Computing Accreditation Board (PICAB).
    CHED: 16 Centers of Excellence and Development, and Autonomous Status for both campuses renewed for 2024-2027.
    """,

    # ------------------------------------------------------------------
    # PAYMENT, FEES, SUPPORT
    # ------------------------------------------------------------------
    "PAYMENT_MODE": """
    You can pay through:
    - Cashier / Tellering Office at the TIP campus
    - PayApp: https://bit.ly/TIPOnlinePayment
    - DragonPay (current students: log in to your TIP e-mail to access the link): https://tip.instructure.com/courses/4925/files?preview=331490
    - 7-Eleven: https://www.dragonpay.ph/dragonpay-payments-via-7-11-are-now-easier-and-faster
    - BDO online banking and over-the-counter
    - Landbank online banking
    TIP does not use GCash, Maya, or any other alternative payment channels, and does not authorize anyone to receive payment outside these official channels.
    """,

    "TUITION_FEE": """
    The updated list of fees and discounts is available at the Admissions Office. You may also apply for entrance scholarships during online registration at https://admission.tip.edu.ph/web/.
    Admissions Office:
    QC: admissions.qc@tip.edu.ph | 8911-0964 loc. 305
    Manila: admissions.manila@tip.edu.ph | 8733-9117 loc. 102
    For concerns about payment or assessment, contact Student Accounting Services:
    QC: 8911-0964 loc. 391
    Manila: 8733-9117 loc. 153
    """,

    "PAYMENT_CONCERNS": """
    For concerns about payment or assessment, contact Student Accounting Services (SAS) or Tellering Services:
    Student Accounting - QC: 8911-0964 loc. 391 | Manila: 8733-9117 loc. 153
    Tellering - QC: 8911-0964 loc. 365 | Manila: 8733-9117 loc. 155
    """,

    "CONTACT_INFO": """
    Admissions Office contacts:
    TIP Quezon City
    8911-0964 loc. 305 | 8911-7199 | (02) 7917-8477 loc. 305
    9171772556 loc. 305 | 0917-8592871
    admissions.qc@tip.edu.ph

    TIP Manila
    8733-9117 loc. 102 | 8736-2580 | (02) 7918-8476 loc. 102
    9171772566 loc. 102 | 0917-1059581
    admissions.manila@tip.edu.ph
    """,

    "STUDENT_PORTAL": """
    Access your student portal using the link for your campus.
    EmpowerED (college students):
    QC: https://student-qc.tip.edu.ph/login
    Manila: https://student-mla.tip.edu.ph/login
    ARIS (Senior High School and graduate students):
    QC: https://webqc2.tip.edu.ph/portal/student/new/public/login.php
    Manila: https://webmla2.tip.edu.ph/portal/student/new/public/login.php
    """,

    "ENROLLMENT_TECHNICAL_SUPPORT": """
    For technical problems during online enrollment, contact concerns@tip.edu.ph
    You can also submit a support ticket at:
    https://tip.jitbit.com/helpdesk/Tickets/New
    """,

    # ------------------------------------------------------------------
    # AFTER ENROLLMENT
    # ------------------------------------------------------------------
    "ID_APPLICATION": """
    After you get your Official Registration Form, scan the QR code on it for the ID application and schedule.
    You can do this at your own convenience.
    """,

    "LIBRARY_VALIDATION": """
    You may go to the library after receiving your Official Registration Form, or once classes begin, for Validation / KOHA Validation.
    You can do this at your own convenience.
    """,

    "MEDICAL_DENTAL_EXAM": """
    College freshmen and Grade 11 applicants should go to the clinic after getting the Official Registration Form to register for their medical and dental examination schedule.
    """,

    "MATH_ENHANCEMENT_PROGRAM": """
    The Math Enhancement Program (MEP) is a FREE math tutorial program covering the fundamental topics needed for college math.
    Engineering, Architecture, and Computer Studies freshmen are encouraged to join.
    After securing your Official Registration Form, go to the MEP Registration Desk.
    """,

    "UNKNOWN": """
    Sorry, I can't quite understand your question.
    Try asking about enrollment, tuition fees, payment methods, programs, accreditation, or TIP contact information.
    """
}