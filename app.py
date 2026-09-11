from pathlib import Path
import pickle

from flask import Flask, render_template, request
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

MODEL_PATH = Path(__file__).with_name("model.pkl")


def train_default_model():
    X = [
        [5.0, 80], [7.0, 100], [4.0, 60], [8.5, 120], [6.5, 90],
        [5.5, 70], [7.5, 110], [6.0, 85], [3.5, 50], [9.0, 130],
        [8.0, 115], [4.5, 65], [6.0, 88], [7.2, 98], [5.8, 75]
    ]
    y = [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0]

    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X, y)

    with MODEL_PATH.open("wb") as file:
        pickle.dump(model, file)

    return model


if MODEL_PATH.exists():
    with MODEL_PATH.open("rb") as file:
        model = pickle.load(file)
else:
    model = train_default_model()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    cgpa = float(request.form["cgpa"])
    iq = float(request.form["iq"])

    prediction = model.predict([[cgpa, iq]])

    if prediction[0] == 1:
        result = "You are likely to get placed!"
    else:
        result = "You may need to improve your placement chances."

    return render_template(
        "index.html",
        prediction=result
    )

if __name__ == "__main__":
    app.run(debug=True)