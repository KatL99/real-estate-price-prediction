import os
import pickle

ROOT_PATH = os.path.dirname(os.path.dirname(__file__))

def my_prediction_function(bedrooms, bathrooms, living_area, surface_of_the_plot, postal):
    """Prediction function using a pretrained model loaded from disk

    Arguments:
    - bedrooms
    - bathrooms
    - living_area
    - surface_of_the_plot
    - postal
    """
    # Load the model from the pickle file
    model_path = os.path.join(ROOT_PATH, 'models', 'best_model.pkl')
    with open(model_path, 'rb') as file:
        model = pickle.load(file)

    # Use the model to predict the given inputs
    prediction = model.predict([[float(bedrooms), float(bathrooms), float(living_area), float(surface_of_the_plot), float(postal)]])

    return prediction[0]

print(my_prediction_function(2,1,70,80,84773.0))