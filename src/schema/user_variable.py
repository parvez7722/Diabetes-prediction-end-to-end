from pydantic import BaseModel,Field

class user_variable(BaseModel):
    name : str = Field(..., description= "Name of the patient")
    pregnancies: int = Field(..., description= "Number of times pregnant")
    glucose: int = Field(..., gt = 0, description= "Glucose level in the blood")
    bloodPressure: int = Field(..., gt= 0, description= "Blood pressure level")
    skinThickness: int = Field(..., description= "Skin thickness level")
    insulin: int = Field(..., description= "Insulin level in the blood")
    bmi: float = Field(..., description= "Body mass index")
    diabetesPedigreeFunction: float = Field(..., description= "Diabetes pedigree function")
    age: int = Field(..., gt=0, lt=120, description= "Age of the person")