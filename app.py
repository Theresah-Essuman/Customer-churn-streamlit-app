import streamlit as st 

st.set_page_config(
    page_title="ML Prediction App",
    page_icon="🏠",
    layout="wide"
)

st.sidebar.success("Select a page from the sidebar above")
st.title("Embedded ML Model Analysis App")

 
 # About the app
st.markdown.title("About This App")

    
st.markdown("""   
        This intelligent application empowers stakeholders to predict customer churn effectively. 
        By integrating machine learning models into a user-friendly and intuitive interface, the app provides real-time insights, helping business stakeholders implement targeted retention strategies. 
        This user-friendly solution enhances decision-making and improves customer retention efforts.
    """)

# Create columns for Key Features and User Benefits
col1, col2 = st.columns(2)

    # Key Features
with col1:
    st.markdown("#### Key Features")
st.markdown("""
                 
            - **Data:** A page that allows users to view the raw, clean and test data across the various tabs. It includes a download csv feature. 
            The data cleaning logic and pipeline is in the code base of this page.
            - **Dashboard:** It contains visualizations of the dataset used to train the models. 
            You can select between the 3 different types using a drop down menu. An **EDA** dashboard, an analytics **KPIs** dashboard with filtering capabilities and 
            a **model explainer** dashboard with Confusion matrix, AUC ROC Curves and a feature importances visualization to understand the drivers of customer churn for the leading model.        
            - **Predict:** Contains a list of models in a drop down with corresponding pipelines used to predict customer churn. There are two tabs namely predict and bulk predict for single and bulk prediction(s) respectively. 
            The bulk predict allow users to upload of csv or excel files with same schema as the data used for training and testing. 
            A toggle button allow users to make predictions by way of searching a particular customer or several customers in the predict and bulk predict tabs respectively.  
            - **History:** This page contains table view of the past predictions made including their churn, probability, model used and time stamp.
          
        """)

