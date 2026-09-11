
# 🎓 Student Placement Prediction

A Machine Learning project that predicts whether a student is likely to get placed based on their **CGPA and IQ**.

The project uses **Python, Pandas, NumPy, Scikit-learn, Flask, HTML and CSS**. A Logistic Regression model is trained on student placement data and saved as `model.pkl` for deployment.

## 📌 Project Overview

The goal of this project is to build a simple machine learning system that predicts student placement chances.

### Input Features

* CGPA
* IQ

### Output

* `1` → Student is likely to get placed
* `0` → Student may not get placed

The dataset contains 100 student records with CGPA, IQ and placement information.

## 🤖 Machine Learning Model

The project uses:

**Logistic Regression**

The trained model is saved using Python Pickle:

```python
import pickle

pickle.dump(model, open("model.pkl", "wb"))
```

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Flask
* HTML
* CSS
* Git & GitHub

## 📂 Project Structure

```text
student-placement-prediction/
│
├── app.py
├── model.pkl
├── requirements.txt
│
├── student_placement_prediction.ipynb
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

## ⚙️ How to Run the Project Locally

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd student-placement-prediction
```

### 3. Install required libraries

```bash
pip install -r requirements.txt
```

### 4. Start the Flask server

```bash
python app.py
```

### 5. Open the application

Open this URL in your browser:

[**http://127.0.0.1:5000**](http://127.0.0.1:5000)

> This is a local development URL. It works when the Flask server is running on your computer.

## 🖥️ How It Works

```text
Student
   ↓
Enter CGPA and IQ
   ↓
Flask Web Application
   ↓
Trained Logistic Regression Model
   ↓
Prediction
   ↓
Placement Result
```

## 🔮 Example

Input:

```text
CGPA = 7.5
IQ = 120
```

The model processes these values and predicts the student's placement status.

## 📊 Dataset

The dataset contains:

* CGPA
* IQ
* Placement

The `placement` column is the target variable.

## 🚀 Deployment

The machine learning model can be deployed using Flask and a cloud hosting platform such as Render.

For production deployment, the Flask application can be started using:

```bash
gunicorn app:app
```

## 🎯 Future Improvements

* Add more student features
* Use a larger dataset
* Add placement probability
* Improve model accuracy
* Add multiple machine learning models
* Create a more advanced dashboard
* Deploy the application online

## 👨‍💻 Author

**Tanmay Paul**

Student | Computer Science & AI

## ⭐ Project

If you find this project useful, please consider giving the repository a ⭐ on GitHub.
