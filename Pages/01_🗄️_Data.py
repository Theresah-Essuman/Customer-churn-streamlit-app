import os
import time
import urllib

import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

from configparser import DATA, FIRST_FILE, SECOND_FILE, SECOND_FILE_URL, TRAIN_FILE, TRAIN_FILE_CLEANED, TEST_FILE, TEST_FILE_URL
import logo


st.title("Database")

         