import inspect
import os

import joblib
import numpy as np
from flask import Flask, jsonify, request, send_from_directory

from replies import INTENT_RESPONSES

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, static_folder="static", static_url_path="/static")

# Load trained intent classifier (once, at startup)
model = joblib.load(os.path.join(BASE_DIR, "Q-TIP_Intent_Classifier.joblib"))
THRESHOLD = 0.20


def predict_intent(text):
    scores = model.decision_function([text])[0]

    predicted_index = np.argmax(scores)
    predicted_tag = model.classes_[predicted_index]
    confidence = scores[predicted_index]

    if confidence < THRESHOLD:
        return "UNKNOWN"

    return predicted_tag


@app.get("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


@app.post("/api/chat")
def chat():
    data = request.get_json(silent=True) or {}
    user_input = str(data.get("message", "")).strip()

    if not user_input:
        return jsonify({"error": "Message is empty."}), 400

    intent = predict_intent(user_input)

    response = INTENT_RESPONSES.get(
        intent,
        INTENT_RESPONSES["UNKNOWN"]
    )

    return jsonify({
        "reply": inspect.cleandoc(response),
        "intent": str(intent),
    })


if __name__ == "__main__":
    # For local use. In production, run with: gunicorn app:app
    app.run(host="127.0.0.1", port=5000, debug=False)