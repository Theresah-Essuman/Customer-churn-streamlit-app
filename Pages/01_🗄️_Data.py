import streamlit as st
import pandas as pd
import numpy as np

# Configure the page
st.set_page_config(
    page_title='Data Viewer',
    page_icon='👨‍💻',
    layout='wide'
)

def data_page():
    # Set header for dataset view
    st.title('Dataset View')

    # Create selection option
    column1, column2 = st.columns(2)
    with column2:
        option = st.selectbox('Choose columns to be viewed', 
                              ('All Columns', 'Numeric Columns', 'Categorical Columns'))

    # ---- Load remote dataset
    @st.cache_data(show_spinner='Loading data')
    def load_data():
        # Adjusted file path with forward slashes
        df = pd.read_csv('C:/Users/HP/OneDrive/Desktop/lp4/Embed-ML-models-in-Web-Frameworks-with-Streamlit-/Data/datase.csv.csv')
        return df

    df = load_data().head(100)

    # Display based on selection
    if option == 'Numeric Columns':
        st.subheader('Numeric Columns')
        st.write(df.select_dtypes(include='number'))

    elif option == 'Categorical Columns':
        st.subheader('Categorical Columns')
        st.write(df.select_dtypes(include='object'))

    else:
        st.subheader('Complete Dataset')
        st.write(df)

    # ----- Add column descriptions of the dataset
    with st.expander('**Click to view column description**'):
        st.markdown('''...''')  # Your description here

if __name__ == '__main__':
    data_page()