import streamlit as st 

st.set_page_config(
    page_title="ML Prediction App",
    page_icon="🏠",
    layout="wide"
)

st.sidebar.success("Select a page from the sidebar above")
st.title("Embedded ML Model Analysis App")

 
 # About the app
st.markdown('### About the app')

    
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



 # How to run the application is a development environment
st.write("#### How to run the application")
with st.container(border=True):
            st.code("""
                # Create the virtual environemnt
                 py -m venv virtual
                
                # Activate the environment
                \virtual\Scripts\activate 
                
                # Run the app
                streamlit run 🏠_Home.py            
            """)




 # User Benefits

st.markdown("#### User Benefits")
st.markdown("""
        - **Decision-driven decisions:** Make data-driven decisions effortlessly harnessing the power of a data app that integrates analytics, machine learning and predictions.
        - **Improve Customer Retention:** Identify at-risk customers and implement proactive retention strategies.
        - **Optimize Marketing Strategies:** Customize marketing efforts to effectively target potential churners.
        - **Enhance Business Performance:** Lower churn rates and boost customer lifetime value.
        """)


st.subheader("Need consultation")
st.markdown("Have questions or need insights?")

# Markdown for Email and LinkedIn badges
st.markdown(
    """
    [![Email](https://img.shields.io/badge/Email-Contact-blue)](mailto:hasereth9@gmail.com)&nbsp;
    [![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/theresah-essuman)&nbsp;
    """, 
    unsafe_allow_html=True
)

# Button to navigate to the GitHub repository
if st.button('Go to GitHub Repository'):
    st.write('[Repository on GitHub](https://github.com/Theresah-Essuman/Embed-ML-models-in-Web-Frameworks-with-Streamlit-.git)')
    
    