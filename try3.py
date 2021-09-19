


import numpy as np
import pickle
import pandas as pd
# from flasgger import Swagge

import streamlit as st
from sklearn.linear_model import LinearRegression

# app=Flask(__name__)
# Swagger(app)

pickle_in = open('model_pickle.pkl','rb')
classifier = pickle.load(pickle_in)


# @app.route('/')
#def welcome():
#    return "Welcome All"

# @app.route('/predict',methods=["Get"])
def salary_prediction(years):
    prediction = classifier.predict([[years]])
    print(prediction)
    return prediction


def main():
    st.title("Salary Finder")
    html_temp = """
    <div style="background-color:pink;padding:5px">
    <h2 style="color:black;text-align:center;">Streamlit Salary Predictor </h2>
    </div>
    
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    years = st.text_input("Years", "Type Here")
    result = ""
    if st.button("Predict"):
        result = salary_prediction(float(years))
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit")

