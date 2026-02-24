from flask import Flask, request, render_template
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
app=Flask(__name__)
df = pd.read_csv("cancer.csv")
selected_feature=['Air Pollution', 'Genetic Risk','Obesity','Balanced Diet','OccuPational Hazards','Coughing of Blood']
X=df[selected_feature]
y=df['Level']
X_train,X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
rf_clf= RandomForestClassifier(n_estimators=100, random_state=42)
rf_clf.fit(X_train,y_train)
y_pred = rf_clf.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)
classification_rep = classification_report(y_test,y_pred)
conf_matrix= confusion_matrix(y_test,y_pred)
print("Accuracy On Test Data:",accuracy*100)
print("Confusion Matrix:\n", conf_matrix)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    air_pollution = float(request.form['Air_Pollution'])
    genetic_risk = float(request.form['Genetic_risk'])
    obesity = float(request.form['Obesity'])
    balanced_diet = float(request.form['Balanced_diet'])
    occupational_hazards = float(request.form['Occpational_hazards'])
    coughing_of_blood = float(request.form['Conghing_of_blood'])
    
    input_data = [[air_pollution, genetic_risk, obesity, balanced_diet, occupational_hazards, coughing_of_blood]]
    predicted_class = rf_clf.predict(input_data)
    predicted_proba = rf_clf.predict_proba(input_data)
    predicted_class = predicted_class[0]
    predicted_proba = predicted_proba[0]
    result = {
        'predicted_class':predicted_class,
        'predicted_probability':dict(zip(rf_clf.classes_, predicted_proba))
    }
    return render_template('index.html', result=result)
if __name__=='__main__':
    app.run(debug=True)


