# Symptoms Based Disease Prediction System - Documentation

## Project Overview
This is a medical-themed web application built with **Flask** and **Scikit-learn**. It allows users to register, log in, and input their symptoms to receive a disease prediction along with a confidence percentage. The project uses a **RandomForest Classifier** trained on synthetic medical data.

---

## 🏗️ Architecture

The system follows a modular architecture separating the web layer, data layer, and machine learning logic.

### 1. Technology Stack
*   **Backend**: Flask (Python 3.13+)
*   **Frontend**: Bootstrap 5 (Styling), Jinja2 (Templating), Google Fonts (Inter)
*   **Machine Learning**: Scikit-Learn (RandomForest), Pandas, NumPy, Joblib
*   **Database**: SQLite via Flask-SQLAlchemy
*   **Authentication**: Werkzeug (Password hashing)

### 2. Machine Learning Pipeline
The project uses a sophisticated `sklearn.pipeline.Pipeline` to ensure that data transformation is consistent between training and prediction.
*   **Symptoms (Text)**: Processed using `TfidfVectorizer` (N-grams 1-2) to capture combinations of symptoms.
*   **Gender (Categorical)**: Processed using `OneHotEncoder`.
*   **Age & Symptom Count (Numerical)**: Passed through directly.
*   **Classifier**: `RandomForestClassifier` with 200 estimators.

### 3. Data Storage
*   **SQLite (`instance/app.db`)**: Stores user credentials and prediction history.
*   **Pickle Files (`ml/*.pkl`)**: Stores the trained model and data encoders for fast inference.

---

## 📁 File Structure

```text
├── app.py              # Main Flask entry point (routes, auth, prediction logic)
├── database.py         # SQLAlchemy models (User, Prediction)
├── view_db.py          # Helper script to view database contents
├── requirements.txt    # Project dependencies
│
├── ml/
│   ├── train_model.py  # Script to generate synthetic data and train the model
│   ├── preprocess.py   # Shared logic for cleaning symptoms (used in training & app)
│   ├── model.pkl       # The binary file for the trained ML pipeline
│   └── dataset.csv     # The generated training data
│
├── templates/          # HTML files (base, home, login, predict, result, dashboard)
├── static/             # CSS (Medical theme) and JS files
└── instance/           # Contains app.db (SQLite database)
```

---

## 🛠️ Setup Process (How it was configured)

1.  **Environment Isolation**: 
    A virtual environment (`venv`) was created to keep project dependencies separate from the system Python.
    
2.  **Dependency Installation**:
    Crucial libraries like `scikit-learn` and `Flask` were installed. Since Python 3.13 is new, dependencies were installed one-by-one to ensure compatibility.

3.  **Model Training**:
    The command `python ml/train_model.py` was executed. This script:
    *   Created **25,000 synthetic patient records** based on 30 different diseases.
    *   Trained the RandomForest model.
    *   Saved the results as `model.pkl`.

4.  **Database Setup**:
    The `instance/` folder was created manually, and Flask-SQLAlchemy automatically generated the `app.db` file upon the first run.

---

## 🚀 How to Run

1.  **Activate Environment**:
    ```powershell
    .\venv\Scripts\activate
    ```
2.  **Start Application**:
    ```powershell
    python app.py
    ```
3.  **Access Web UI**:
    Open [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🔒 Security & Features
*   **Hashed Passwords**: No plain-text passwords are stored in the database.
*   **Session Management**: Users must be logged in to access the predictor and their history.
*   **Dashboard**: Each user has a unique dashboard showing their past health checks.

---
> **Disclaimer**: This is a college/educational project. It is not for real medical diagnosis.
