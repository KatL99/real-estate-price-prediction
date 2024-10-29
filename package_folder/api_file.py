from fastapi import FastAPI 
import pickle

from package_folder.predict_model import my_prediction_function

# FastAPI instance
app = FastAPI()

# Root endpoint
@app.get("/")
def root():
    return {'greeting':"hello from utkarsh"}

# # Prediction endpoint
# @app.get("/predict")
# def predict():
#     # Use the function in our package to run the prediction
#     prediction = my_prediction_function()

#     # Return prediction
#     return {"prediction": int(prediction[0])}