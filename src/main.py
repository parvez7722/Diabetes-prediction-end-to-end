from  fastapi import FastAPI
from src.schema.user_variable import user_variable
from src.schema.create_json import save_data,load_data
from src.model.prediction import prediction

app = FastAPI()

@app.get("/")
def root():
    return {"message": "hello world"}

@app.post("/patient")
def create_patient(patient: user_variable):
    data = load_data()

    if patient.name in data:
        return {"message": "Patient already exists", "patient_data": data[patient.name]}
    
    data[patient.name] = patient.model_dump(exclude={"name"})

    save_data(data)
    return {"message": "Patient created successfully", "patient_data": data[patient.name]}

@app.post("/predict")
def predict_diabetes(patient: user_variable):
    pred = prediction(patient)
    if pred == 1:
        return {"message": "The patient is likely to have diabetes."}
    else:
        return {"message": "The patient is unlikely to have diabetes."}
