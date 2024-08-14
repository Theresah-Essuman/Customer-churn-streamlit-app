import streamlit as st 

st.set_page_config(
    page_title="ML Prediction App",
    page_icon=":bar_chart:",
    layout="wide"
)

st.sidebar.success("Select a page from the sidebar above")
st.title("Embedded ML Model Analysis App")
st.sidebar.title("Home")
st.sidebar.markdown("View Data")
st.sidebar.markdown("Dashboard")
st.sidebar.markdown("Pedict")
st.sidebar.markdown("History")

