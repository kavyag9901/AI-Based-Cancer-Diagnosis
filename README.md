# 🧬 Cancer Level Prediction System using Random Forest and Flask

## 📌 Project Overview

The **Cancer Level Prediction System** is a Machine Learning web application developed using **Python**, **Flask**, and the **Random Forest Algorithm**.  

This system predicts the **cancer severity level** based on various health and environmental risk factors such as air pollution, genetic risk, obesity, diet, occupational hazards, and coughing of blood.

The model is trained using a dataset (`cancer.csv`) and deployed as a web application where users can input their health parameters and receive a predicted cancer level along with probability scores.

---

## 🎯 Objective

- To build a Machine Learning model that predicts cancer level.
- To implement the Random Forest classification algorithm.
- To deploy the model using Flask as a web application.
- To provide a user-friendly interface for prediction.

---

## 🛠️ Technologies Used

- **Python**
- **Flask**
- **Pandas**
- **Scikit-learn**
- **HTML (Frontend)**

---

## 📊 Dataset Information

The dataset (`cancer.csv`) contains the following selected features:

- Air Pollution
- Genetic Risk
- Obesity
- Balanced Diet
- Occupational Hazards
- Coughing of Blood



### Why Random Forest?
- High accuracy
- Handles multiple features efficiently
- Reduces overfitting
- Works well for classification problems

### Model Training Steps:

1. Load dataset using Pandas
2. Select important features
3. Split dataset into training and testing sets (70% training, 30% testing)
4. Train Random Forest model
5. Evaluate using:
   - Accuracy Score
   - Classification Report
   - Confusion Matrix

---

## 📈 Model Evaluation

The model performance is evaluated using:

- **Accuracy Score**
- **Confusion Matrix**
- **Classification Report**

The accuracy is printed in the terminal when the application runs.

---

## 🌐 Web Application Workflow

1. User opens homepage (`/`)
2. User enters health-related input values
3. Data is sent to `/predict` route via POST method
4. Model predicts:
   - Cancer Level
   - Probability for each class
5. Result is displayed on the same page

---

## 🧠 How Prediction Works

```python
input_data = [[air_pollution, genetic_risk, obesity, balanced_diet, occupational_hazards, coughing_of_blood]]
predicted_class = rf_clf.predict(input_data)
predicted_proba = rf_clf.predict_proba(input_data)
```

- `predict()` returns the predicted cancer level
- `predict_proba()` returns probability for each class

---

## 📂 Project Structure

```
Cancer-Prediction-Project/
│
├── app.py
├── cancer.csv
├── templates/
│   └── index.html
└── README.md
```

---

## 🚀 How to Run the Project

### Step 1: Install Required Libraries

```bash
pip install flask pandas scikit-learn
```

### Step 2: Run the Application

```bash
python app.py
```

### Step 3: Open in Browser

```
http://127.0.0.1:5000/
```

--- Easy to understand and modify

---







---

## ⚠️ Disclaimer

This project is developed for educational purposes only and should not be used for real medical diagnosis. Always consult a healthcare professional for medical advice.

---=
