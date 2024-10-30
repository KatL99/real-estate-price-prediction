import streamlit as st
import requests

 # Change this URL to the one of your API
API_URL = " https://my-api-app-ltqnoxdklq-ew.a.run.app/"

st.title("Real Estate Price Prediction MVP")

st.write("Real Estate Price Predictor")


bedrooms = st.slider('How many bedrooms', min_value=0, max_value=5, value=1, step=1)
bathrooms = st.slider('How many bathrooms',  min_value=0, max_value=5, value=1, step=1)

living_area = st.number('How much living area?',  min_value=0, max_value=200, value=1, step=5)
surface_of_the_plot = st.number('Which surface of the plot?',  min_value=0, max_value=500, value=1, step=5)

postal = st.number('What is the postal code? (from 1000 to 9999)',  min_value=1000, max_value=9999, value=1000, step=1)



url = f"{API_URL}/predict"
params = {
    'bedrooms': bedrooms,
    'bathrooms': bathrooms,
    'surface_of_the_plot ': surface_of_the_plot,
    'postal': postal,
}

response = requests.get(url, params=params).json()

st.write(f"The estimated price is {str(response[' Euro'])}")
