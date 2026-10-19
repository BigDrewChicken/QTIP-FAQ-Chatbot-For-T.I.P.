
import joblib
import numpy as np
import pandas as pd

# ==========================================
# 1. LOAD TRAINED MODEL
# ==========================================

model = joblib.load("Q-TIP_Intent_Classifier.joblib") # REPLACE WITH MODEL PATH IF IN A DIFFERENT FOLDER 


# ==========================================
# 2. PREDICTION FUNCTION
# ==========================================

def predict_intent(text):
    scores = model.decision_function([text])[0]

    predicted_index = np.argmax(scores)
    predicted_intent = model.classes_[predicted_index]
    confidence = scores[predicted_index]

    THRESHOLD = -0.2

    if confidence < THRESHOLD:
        return "UNKNOWN"

    return predicted_intent

    
# ==========================================
# 3. TEST CASES: 5 PER INTENT
# ==========================================

test_cases = {
    "ACCREDITATION": [
        "What accreditations does TIP have?",
        "Is TIP accredited by ABET?",
        "Does TIP have international accreditation?",
        "Are TIP programs accredited?",
        "What quality certifications does TIP hold?"
    ],
    "ADMISSION_REQUIREMENTS": [
        "What are the admission requirements?",
        "What documents do I need to apply?",
        "What requirements are needed for admission to TIP?",
        "Do I need my report card to enroll?",
        "Where can I check the application requirements?"
    ],
    "COLLEGE_PROGRAMS": [
        "What college programs does TIP offer?",
        "Does TIP offer computer engineering?",
        "What engineering degrees can I take?",
        "Does TIP have an information technology degree?",
        "List the undergraduate programs available at TIP."
    ],
    "CONTACT_INFO": [
        "How can I contact TIP?",
        "What is the admissions office phone number?",
        "Can I have the admissions email address?",
        "How do I contact the TIP Quezon City campus?",
        "Where can I ask questions about admission?"
    ],
    "CREDIBILITY": [
        "What is employer recognition of graduates",
        "has TIP received academic awards",
        "How credible is the education at TIP?",
        "Is TIP a legitimate school?",
        "Why should I trust TIP as a university?"
    ],
    "ENROLLMENT_FORM": [
        "Where can I get the enrollment form?",
        "How do I access the application form?",
        "Can I fill out the TIP enrollment form online?",
        "Where can I submit my admission application?",
        "Send me the link to the enrollment form."
    ],
    "ENROLLMENT_GENERAL": [
        "How do I enroll at TIP?",
        "What is the general enrollment process?",
        "How can I start my enrollment?",
        "Can you explain how enrollment works?",
        "What steps should I follow to enroll?"
    ],
    "ENROLLMENT_SCHEDULE": [
        "When does enrollment start?",
        "What is the enrollment deadline?",
        "When is the next enrollment period?",
        "What are the enrollment dates for this semester?",
        "Is enrollment still open?"
    ],
    "ENROLLMENT_TECHNICAL_SUPPORT": [
        "The enrollment website is not working.",
        "I cannot submit my online application.",
        "I am getting an error while enrolling.",
        "The enrollment portal won't load.",
        "Who can help me fix an enrollment system problem?"
    ],
    "ENROLL_COLLEGE": [
        "How do I apply for college at TIP?",
        "I want to become a college freshman. What should I do?",
        "Where can incoming college students apply?",
        "How can I get admitted to a TIP college program?",
        "What is the process for applying to college?"
    ],
    "ENROLL_CONTINUESTUDENT": [
        "How can I reenroll after skipping a semester?",
        "How do I enroll next semester?",
        "Where do current college students register for classes?",
        "What should I do before enrolling for the next term?",
        "How do I enroll as a regular college student?"
    ],
    "ENROLL_CONTINUE_GRADUATE": [
        "How do continuing graduate students enroll?",
        "I am already in a graduate program. How do I register again?",
        "What is the enrollment process for current graduate students?",
        "How do I enroll for another semester in graduate school?",
        "Where do continuing master's students register?"
    ],
    "ENROLL_GRADE11": [
        "How do I enroll in Grade 11?",
        "I want to apply for senior high school at TIP.",
        "What is the Grade 11 admission process?",
        "Where can incoming Grade 11 students apply?",
        "How can I become a Grade 11 student at TIP?"
    ],
    "ENROLL_GRADE12": [
        "How do I enroll in Grade 12?",
        "What is the enrollment process for Grade 12?",
        "I am entering Grade 12. What should I do?",
        "How can I register for Grade 12 at TIP?",
        "Where can I find Grade 12 enrollment instructions?"
    ],
    "ENROLL_GRADE12_CONTINUING": [
        "I am a current Grade 11 student moving to Grade 12. How do I enroll?",
        "How do continuing senior high school students enroll in Grade 12?",
        "I will continue Grade 12 at TIP. What are the next steps?",
        "How do I enroll for my second year of senior high school?",
        "What should a continuing Grade 12 student do before enrollment?"
    ],
    "ENROLL_SHS_GENERAL": [
        "How do I enroll in senior high school?",
        "What is the SHS enrollment process at TIP?",
        "I want to study senior high school at TIP.",
        "Where can I apply for senior high school?",
        "How can I become a senior high school student?"
    ],
    "ENROLL_TRANSFEREE": [
        "How do I transfer to TIP from another school?",
        "I am a college transferee. How can I apply?",
        "What is the admission process for transfer students?",
        "Can I transfer my college studies to TIP?",
        "Where can transferees apply for admission?"
    ],
    "GRADUATE_ENROLLMENT": [
        "How do I enroll in a graduate program?",
        "I want to apply for graduate program.",
        "What is the admission process for graduate studies?",
        "How can I enroll in a master's degree program?",
        "Where can I apply for postgraduate studies at TIP?"
    ],
    "GRADUATE_PROGRAMS": [
        "What graduate programs are offered at TIP?",
        "Does TIP offer master's degrees?",
        "What postgraduate courses can I take?",
        "Are graduate engineering programs available?",
        "What fields of study are available in graduate school?"
    ],
    "GREETINGS": [
        "Hello!",
        "Hi Q-TIP!",
        "Good morning!",
        "Hey, how are you?",
        "Greetings!"
    ],
    "ID_APPLICATION": [
        "How do I apply for my student ID?",
        "Where can I request a TIP ID card?",
        "I need to get my student identification card.",
        "What is the process for applying for a school ID?",
        "How can I replace my lost student ID?"
    ],
    "LIBRARY_VALIDATION": [
        "How do I validate my library account?",
        "What is the library validation process?",
        "How can I get my library access validated?",
        "Where do I go to validate my library privileges?",
        "What do I need to do for library validation?"
    ],
    "MATH_ENHANCEMENT_PROGRAM": [
        "What is the Math Enhancement Program?",
        "Does TIP have a mathematics enhancement course?",
        "Who needs to take the math enhancement program?",
        "How do I join the Math Enhancement Program?",
        "Can you explain TIP's math enhancement program?"
    ],
    "MEDICAL_DENTAL_EXAM": [
        "How do I complete the medical examination?",
        "Where can I get my dental examination?",
        "What are the medical and dental requirements for enrollment?",
        "Do I need a medical exam before classes start?",
        "How do I submit my medical examination results?"
    ],
    "OFFERED_COURSES": [
        "What courses are offered at TIP?",
        "What subjects or programs can I study?",
        "Does TIP offer business courses?",
        "What senior high school strands are available?",
        "Can you list the courses available at TIP?"
    ],
    "PAYMENT_CONCERNS": [
        "My tuition payment has not been reflected.",
        "I paid my fees but my account still shows a balance.",
        "How can I resolve a payment problem?",
        "I made an online payment and need assistance.",
        "Who should I contact about a failed payment?"
    ],
    "PAYMENT_MODE": [
        "What payment methods does TIP accept?",
        "Can I pay tuition through GCash?",
        "How do I pay my school fees online?",
        "Does TIP accept Dragonpay?",
        "Can I pay at the campus cashier?"
    ],
    "SHS_PROGRAMS": [
        "What senior high school strands does TIP offer?",
        "Does TIP offer the STEM strand?",
        "What SHS tracks are available?",
        "Can I take ABM at TIP?",
        "What strands can incoming Grade 11 students choose?"
    ],
    "STUDENT_PORTAL": [
        "Where can I access the student portal?",
        "What is the link to the EmpowerED portal?",
        "How do I log in to my student account?",
        "I need to access the TIP student portal.",
        "Where can continuing students check their online account?"
    ],
    "TECHNOCORE": [
        "What is Technocore at TIP?",
        "Can you explain the Technocore program?",
        "What does Technocore mean?",
        "How does Technocore work at TIP?",
        "I want information about TIP Technocore."
    ],
    "TUITION_FEE": [
        "How much is tuition at TIP?",
        "What is the tuition fee for college?",
        "How much does one semester cost?",
        "Where can I inquire about tuition expenses?",
        "How can I find out the cost of studying at TIP?"
    ]
}


# ==========================================
# 4. VALIDATE INTENT LABELS
# ==========================================

model_intents = set(model.classes_)
test_intents = set(test_cases.keys())

if model_intents != test_intents:
    raise ValueError(
        "Test intents do not match model labels.\n"
        f"Missing test cases: {sorted(model_intents - test_intents)}\n"
        f"Extra test cases: {sorted(test_intents - model_intents)}"
    )


# ==========================================
# 5. RUN TESTS AND CREATE DATAFRAME
# ==========================================

results = []

for expected_intent, inputs in test_cases.items():
    for number, text in enumerate(inputs, start=1):
        predicted = predict_intent(text)

        results.append({
            "Intent": expected_intent,
            "Test Case": number,
            "Input": text,
            "Expected": expected_intent,
            "Predicted": predicted,
            "Result": (
                "PASS" if predicted == expected_intent else "FAIL"
            )
        })

df = pd.DataFrame(results)


# ==========================================
# 6. SUMMARY BY INTENT
# ==========================================

summary_df = (
    df.groupby("Intent", sort=True)
    .agg(
        Total_Tests=("Result", "count"),
        Correct=("Result", lambda x: (x == "PASS").sum()),
        Incorrect=("Result", lambda x: (x == "FAIL").sum())
    )
    .reset_index()
)

summary_df["Accuracy (%)"] = (
    summary_df["Correct"] / summary_df["Total_Tests"] * 100
).round(2)


# ==========================================
# 7. OVERALL RESULTS
# ==========================================

total_tests = len(df)
total_correct = int((df["Result"] == "PASS").sum())
total_incorrect = total_tests - total_correct

overall_accuracy = (
    round(total_correct / total_tests * 100, 2)
    if total_tests > 0 else 0
)

overall_df = pd.DataFrame([{
    "Number of Intents": df["Intent"].nunique(),
    "Total Test Cases": total_tests,
    "Correct Predictions": total_correct,
    "Incorrect Predictions": total_incorrect,
    "Overall Accuracy (%)": overall_accuracy
}])


# ==========================================
# 8. DISPLAY TABLES
# ==========================================

pd.set_option("display.max_columns", None)
pd.set_option("display.max_colwidth", 60)
pd.set_option("display.width", 180)

print("\nOVERALL CLASSIFIER RESULTS")
print(overall_df.to_string(index=False))

print("\nACCURACY BY INTENT")
print(summary_df.to_string(index=False))

print("\nDETAILED TEST RESULTS")
print(df.to_string(index=False))


# ==========================================
# 9. EXPORT CSV FILES FOR THE PAPER
# ==========================================

df.to_csv("test_cases\QTIP_Detailed_Test_Results.csv", index=False)
summary_df.to_csv("test_cases\QTIP_Accuracy_By_Intent.csv", index=False)
overall_df.to_csv("test_cases\QTIP_Overall_Results.csv", index=False)

print("\nCSV files exported successfully:")
print("- QTIP_Detailed_Test_Results.csv")
print("- QTIP_Accuracy_By_Intent.csv")
print("- QTIP_Overall_Results.csv")
