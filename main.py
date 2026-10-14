
import joblib
import numpy as np
from replies import INTENT_RESPONSES

# Load trained intent classifier
model = joblib.load("Q-TIP_Intent_Classifier.joblib")

# SVM decision-score threshold
THRESHOLD = 0.20


def predict_intent(text):
    scores = model.decision_function([text])[0]

    predicted_index = np.argmax(scores)
    predicted_tag = model.classes_[predicted_index]
    confidence = scores[predicted_index]

    if confidence < THRESHOLD:
        return "UNKNOWN"

    return predicted_tag


# Q-TIP APPLICATION
print("Q-TIP: Hello! I'm your TIP assistant.")

while True:
    user_input = input("\nYou: ").strip()

    if user_input.lower() == "exit":
        print("Q-TIP: Goodbye! Good luck with your studies!")
        break

    if not user_input:
        print("Q-TIP: Please enter a message.")
        continue

    intent = predict_intent(user_input)

    # Get the corresponding reply
    response = INTENT_RESPONSES.get(
        intent,
        "Sorry, I can't quite understand that."
    )

    print(f"Intent: {intent}")
    print(f"Q-TIP: {response.strip()}")
