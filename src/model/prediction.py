import pandas as pd
import joblib
from src.schema.user_variable import user_variable

with open('src/model/model.pkl', 'rb') as f:
    model = joblib.load(f)

def prediction(user_input : user_variable):
    input_data = pd.DataFrame([{
        'Pregnancies': user_input.pregnancies,
        'Glucose': user_input.glucose,
        'BloodPressure': user_input.bloodPressure,
        'SkinThickness': user_input.skinThickness,
        'Insulin': user_input.insulin,
        'BMI': user_input.bmi,
        'DiabetesPedigreeFunction': user_input.diabetesPedigreeFunction,
        'Age': user_input.age
    }])
    pred =  model.predict(input_data)
    return pred[0]