
# 🎓 Student Placement Prediction

## 📌 Project Overview

**Student Placement Prediction** is a Machine Learning project that predicts whether a student is likely to get placed based on their **CGPA** and **IQ**.

The project uses **Logistic Regression**, a classification algorithm, to predict the placement result.

* `1` → Placed
* `0` → Not Placed

The model is trained using a placement dataset containing student CGPA, IQ, and placement information.

---

## 🚀 Features

* Predicts student placement status
* Uses CGPA and IQ as input features
* Uses Logistic Regression for classification
* Data preprocessing and exploratory data analysis
* Train-test split for model evaluation
* Saves the trained ML model using Pickle
* Can be deployed as a web application using Flask

---

## 🛠️ Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Scikit-learn
* Pickle
* Flask

---

## 📂 Project Structure

```text
Student-Placement-Prediction/
│
├── student_placement_prediction.ipynb
├── placement.csv
├── model.pkl
├── app.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

## 📊 Dataset

The dataset contains student information such as:

| Feature   | Description                    |
| --------- | ------------------------------ |
| CGPA      | Student's academic performance |
| IQ        | Student's IQ score             |
| Placement | Placement result               |

The dataset contains **100 student records**.

---

## 🔄 Machine Learning Workflow

The project follows these steps:

```text
Dataset
   ↓
Data Preprocessing
   ↓
Exploratory Data Analysis
   ↓
Feature Selection
   ↓
Train-Test Split
   ↓
Logistic Regression
   ↓
Model Evaluation
   ↓
Save Model
   ↓
Deployment
```

---

## 🧹 Data Preprocessing

The original dataset contains an unnecessary index column.

It is removed before training the model.

The final useful columns are:

```text
cgpa
iq
placement
```

The input features are:

```text
X = [cgpa, iq]
```

The target variable is:

```text
y = placement
```

---

## 🤖 Machine Learning Model

The project uses **Logistic Regression** from Scikit-learn.

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

model.fit(X_train, y_train)
```

Logistic Regression is suitable for this project because the target is a binary classification:

```text
0 = Not Placed
1 = Placed
```

---

## 💾 Saving the Model

After training, the model is saved using Pickle:

```python
import pickle

pickle.dump(model, open("model.pkl", "wb"))
```

This allows the trained model to be reused without training it again.

---

## 🌐 Deployment

The trained model can be connected to a Flask web application.

The user enters:

```text
CGPA
IQ
```

The Flask application sends these values to the trained model.

The model then predicts:

```text
Placed
```

or

```text
Not Placed
```

### Deployment Architecture

```text
User
  ↓
Web Interface
  ↓
Flask Application
  ↓
Machine Learning Model
  ↓
Prediction
  ↓
Placed / Not Placed
```

---

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project

```bash
cd Student-Placement-Prediction
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Flask

```bash
python app.py
```

### 5. Open in browser

```text
http://127.0.0.1:5000
```

---

## 🧪 Example Prediction

### Input

```text
CGPA: 7.5
IQ: 120
```

### Output

```text
Placement Prediction: Placed
```

The actual prediction depends on the trained model.

---

## 🎯 Project Objective

The main objective of this project is to demonstrate how Machine Learning can be used to predict student placement outcomes from academic and aptitude-related features.

---

## 📚 Learning Outcomes

Through this project, I learned:

* Data loading using Pandas
* Data preprocessing
* Exploratory Data Analysis
* Feature selection
* Train-test splitting
* Logistic Regression
* Model evaluation
* Saving ML models using Pickle
* Deploying an ML model using Flask

---

## 🔮 Future Improvements

The project can be improved by adding more student-related features such as:

* 10th percentage
* 12th percentage
* Number of internships
* Number of projects
* Technical skills
* Communication skills
* Certifications
* Backlogs
* Attendance

A larger and more diverse dataset can also improve the reliability of the prediction.

---

## 👨‍💻 Author

**Tanmay Paul**

Student | Computer Science & Artificial Intelligence

### ⭐ If you find this project useful, consider giving the repository a star!
