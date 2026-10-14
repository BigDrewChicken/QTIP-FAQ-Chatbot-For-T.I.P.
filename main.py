
import joblib
import numpy as np

# Load intent classifier trained via DATASET_QTIP
model = joblib.load("Q-TIP_Intent_Classifier.joblib")

# Set our threshold for classifying a valid intent (if < 0.20, it's UNKNOWN)
THRESHOLD = 0.20

def predict_intent(text):

    # Get decision scores for each intent
    scores = model.decision_function([text])[0]

    # Get the predicted intent and its score
    predicted_index = np.argmax(scores)
    predicted_tag = model.classes_[predicted_index]
    confidence = scores[predicted_index]

    # Reject uncertain predictions
    if confidence < THRESHOLD:
        return "UNKNOWN"

    return predicted_tag


# APP ITSELF 

while True:
    user_input = input("\nEnter text (type 'exit' to stop): ").strip()

    if user_input.lower() == "exit":
        break

    intent = predict_intent(user_input)

    if intent == "UNKNOWN":
        print("Intent: UNKNOWN")
        print("Sorry, I can't quite understand that.")
    else:
        print("Predicted intent:", intent)
