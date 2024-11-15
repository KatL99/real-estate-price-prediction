from fastapi import FastAPI,Query
import pickle
from package_folder.predict_model import my_prediction_function

# FastAPI instance
app = FastAPI()

  
# Root endpoint
@app.get("/")
def root():
    return {'greeting':"hello from utkarsh"}

# Prediction endpoint
@app.get("/predict") #added this part today
# def predict(
#      bedrooms: int= Query(...),
#      building_condition: str= Query(...),
#      construction_year: int= Query(...),
#      double_glazing: int= Query(...),
#      energy_class: str= Query(...),
#      furnished: int= Query(...),
#      surface_of_the_plot:int= Query(...),
#      tenement_building: int= Query(...),
#      toilets: int= Query(...),
#      city:str= Query(...),
#       ):
def predict(bedrooms, building_condition, construction_year,
            double_glazing,energy_class, furnished,
            surface_of_the_plot, tenement_building,
            toilets, city):
    # Use the function in our package to run the prediction
    prediction = my_prediction_function(bedrooms, building_condition, construction_year,
                           double_glazing,energy_class, furnished,
                           surface_of_the_plot, tenement_building,
                           toilets, city)

    # Return prediction
    return {"prediction": int(prediction)}