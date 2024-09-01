import streamlit as st
import pandas as pd
import numpy as np
from io import BytesIO
import requests
from sklearn.base import BaseEstimator, TransformerMixin
import joblib
import imblearn
import os
from login import login_user


# Configure the page
st.set_page_config(
    page_title='Predictions',
    page_icon='🔮',
    layout='wide'
)

# --------- Add custom CSS to adjust the width of the sidebar
st.markdown( """ <style> 
            section[data-testid="stSidebar"]
            { width: 200px !important;
            }
            </style> """,
            unsafe_allow_html=True,
)


login_user()

if st.session_state["authentication_status"] == True:

    # ------ Set header for page
    st.title('Predict Churn Status')

    column1, column2 = st.columns([.6, .4])
    with column1:
        model_option = st.selectbox('Choose which model to use for prediction', options=['Gradient Boosting', 'Support Vector'])


    # Load trained machine learning model and encoder from GitHub
    github_model1_url = 'https://raw.githubusercontent.com/pk-aduyaw/Customer_Churn_Classification_Project/master/model/GradientBoosting.joblib'
    github_model2_url = 'https://raw.githubusercontent.com/pk-aduyaw/Customer_Churn_Classification_Project/master/model/SupportVector.joblib'
    encoder_url = 'https://raw.githubusercontent.com/pk-aduyaw/Customer_Churn_Classification_Project/master/model/label_encoder.joblib'
    
    
      # -------- Function to load the model from GitHub
    @st.cache_resource(show_spinner="Loading model")
    def gb_pipeline():
        response = requests.get(github_model1_url)
        model_bytes = BytesIO(response.content)
        pipeline = joblib.load(model_bytes)
        return pipeline


    @st.cache_resource(show_spinner="Loading model")
    def sv_pipeline():
        response = requests.get(github_model2_url)
        model_bytes = BytesIO(response.content)
        pipeline = joblib.load(model_bytes)
        return pipeline


    # --------- Function to load encoder from GitHub
    def load_encoder():
        response = requests.get(encoder_url)
        encoder_bytes = BytesIO(response.content)
        encoder = joblib.load(encoder_bytes)
        return encoder


    # --------- Create a function for model selection
    def select_model():
        # ------- Option for first model
        if model_option == 'Gradient Boosting':
            model = gb_pipeline()
        # ------- Option for second model
        if model_option == 'Support Vector':
            model = sv_pipeline()
        encoder = load_encoder()
        return model, encoder


    # Custom function to deal with cleaning the total charges column
    class TotalCharges_cleaner(BaseEstimator, TransformerMixin):
        def fit(self, X, y=None):
            return self
            
        def transform(self, X):
            # Replace empty string with NA
            X['TotalCharges'].replace(' ', np.nan, inplace=True)

            # Convert the values in the Totalcharges column to a float
            X['TotalCharges'] = X['TotalCharges'].transform(lambda x: float(x))
            return X
            
        # Serialization methods
        def __getstate__(self):
            # Return state to be serialized
            return {}

        def __setstate__(self, state):
            # Restore state from serialized data
            pass
            
        # Since this transformer doesn't remove or alter features, return the input features
        def get_feature_names_out(self, input_features=None):
            return input_features
        
        
        