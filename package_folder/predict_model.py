import os
import pickle
import pandas as pd

ROOT_PATH = os.path.dirname(os.path.dirname(__file__))

def my_prediction_function(bedrooms, building_condition, construction_year,
                           double_glazing,energy_class, furnished,
                           surface_of_the_plot, tenement_building,
                           toilets, city):
    """Prediction function using a pretrained model loaded from disk

    Arguments:
    - 'bedrooms', 'building_condition', 'construction_year', 'double_glazing',
       'energy_class', 'furnished', 'surface_of_the_plot', 'tenement_building',
       'toilets', 'city'
    
    """
    # Load the model from the pickle file
    model_path = os.path.join(ROOT_PATH, 'models', 'best_model_2.pkl')
    with open(model_path, 'rb') as file:
        model = pickle.load(file)

    # Use the model to predict the given inputs
    df = pd.DataFrame(columns = ['bedrooms', 'building_condition', 'construction_year', 'double_glazing',
       'energy_class', 'furnished', 'surface_of_the_plot', 'tenement_building',
       'toilets', 'city'], data=[[bedrooms, building_condition, construction_year,
                           double_glazing,energy_class, furnished,
                           surface_of_the_plot, tenement_building,
                           toilets, city]])
    prediction = model.predict(df)

    return prediction[0]

# print(my_prediction_function(1,1,1,'Good',1979,1,1,1,'A',1,20,'Gas','Installed',
#                              90,30,1,1,19,1,120,1,1,'Brugge','Brussels'))