# import os
# import pickle

# ROOT_PATH = os.path.dirname(os.path.dirname(__file__))

def my_prediction_function(name):
    
    # # Load the model from the pickle file
    # model_path = os.path.join(ROOT_PATH, 'models', 'best_model.pkl')
    # with open(model_path, 'rb') as file:
    #     model = pickle.load(file)

    # # Use the model to predict the given inputs
    # prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    print(f"Hello {name}")

