import os
import time
import urllib

import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

import configparser 
import logo
from login import login_user


st.title("Database")

# --------- Add custom CSS to adjust the width of the sidebar
st.markdown( """ <style> 
            section[data-testid="stSidebar"]
            { width: 200px !important;
            }
            </style> """,
            unsafe_allow_html=True,
)

def data_page():

    login_user()
    if st.session_state["authentication_status"] == True:
        
        # Set header for dataset view
        st.title('Dataset View')

        # Create selection option
        column1, column2 = st.columns(2)
        with column2:
                option = st.selectbox('Choose columns to be viewed',
                                    ('All Columns','Numeric Columns','Categorical Columns'))
                


                                     