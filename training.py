
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, classification_report

# 1. Load dataset
df = pd.read_csv("DATASET_QTIP.csv")

# 2. Clean the data
df = df[["Data", "Tag"]].dropna()
df["Data"] = df["Data"].astype(str).str.strip()
df["Tag"] = df["Tag"].astype(str).str.strip()

df = df[(df["Data"] != "") & (df["Tag"] != "")]
df = df.drop_duplicates(subset=["Data"])

print("Total examples:", len(df))
print("Number of intents:", df["Tag"].nunique())
print("\nExamples per intent:")
print(df["Tag"].value_counts())

# 3. Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    df["Data"],
    df["Tag"],
    test_size=0.20,
    random_state=42,
    stratify=df["Tag"]
)

# 4. Create the TF-IDF + SVM pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer(
        lowercase=True,
        ngram_range=(1, 2),
        strip_accents="unicode"
    )),
    ("classifier", LinearSVC(C=1.0))
])

# 5. Train the model
model.fit(X_train, y_train)

# 6. Evaluate on unseen test examples
predictions = model.predict(X_test)

print("\nAccuracy:", round(
    accuracy_score(y_test, predictions) * 100, 2
), "%")

print("\nClassification report:")
print(classification_report(
    y_test, predictions, zero_division=0
))

# 7. Save the trained model
joblib.dump(model, "Q-TIP_Intent_Classifier.joblib")

print("\nModel saved successfully!")
