import streamlit as st
import pandas as pd
import plotly.express as px

# Configure the page
st.set_page_config(
    page_title='Dashboard',
    page_icon='📊',
    layout='wide'
)

# Add custom CSS to adjust the width of the sidebar
st.markdown(""" 
<style> 
section[data-testid="stSidebar"] {
    width: 200px !important;
}
</style> 
""", unsafe_allow_html=True)

def dashboard_page():
    st.title('Dashboard')

    col1, col2, col3 = st.columns(3)
    with col2:
        options = st.selectbox('Choose viz to display', options=['', 'EDA Dashboard', 'KPIs Dashboard'])

    @st.cache_data(show_spinner='Loading data')
    def load_data():
        # Adjust the path to your data file
         df = pd.read_csv('C:/Users/HP/OneDrive/Desktop/lp4/Embed-ML-models-in-Web-Frameworks-with-Streamlit-/Data/datase.csv.csv')
         return df

    df = load_data()

    def eda_viz():
        st.subheader('EDA Dashboard')
        column1, column2 = st.columns(2)
        with column1:
            fig = px.histogram(df, x='tenure', title='Distribution of Tenure')
            st.plotly_chart(fig)
        with column1:
            fig = px.histogram(df, x='MonthlyCharges', title='Distribution of MonthlyCharges')
            st.plotly_chart(fig)
        with column1:
            fig = px.histogram(df, x='TotalCharges', title='Distribution of TotalCharges')
            st.plotly_chart(fig)

        with column2:
            fig = px.bar(df, x='Churn', title='Churn Distribution')
            st.plotly_chart(fig)
        with column2:
            fig = px.box(df, x='gender', y='TotalCharges', title='Total Charges Distribution across Gender')
            st.plotly_chart(fig)

    def kpi_viz():
        st.subheader('KPIs Dashboard')
        st.markdown('---')
        cols = st.columns(5)
        st.markdown('---')
        # Grand Total Charges
        with cols[0]:
            grand_tc = df['TotalCharges'].sum()
            st.metric(label="Grand TotalCharges", value=f"{'{:,.2f}'.format(grand_tc)}")

        # Grand Monthly Charges
        with cols[1]:
            grand_mc = df['MonthlyCharges'].sum()
            st.metric(label="Grand MonthlyCharges", value=f"{'{:,.2f}'.format(grand_mc)}")

        # Average Customer Tenure
        with cols[2]:
            average_tenure = df['tenure'].mean()
            st.metric(label="Average Tenure", value=f"{'{:,.2f}'.format(average_tenure)}")

        # Churned Customers
        with cols[3]:
            churned = df[df['Churn'] == 1].shape[0]
            st.metric(label="Churn", value=churned)

        # Total Customers
        with cols[4]:
            total_customers = df['customerID'].nunique()
            st.metric(label="Total Customers", value=total_customers)

    def analytical_ques_viz():
        # Analytical questions visualization code here...
        pass

    if options == 'EDA Dashboard':
        eda_viz()
    elif options == 'KPIs Dashboard':
        kpi_viz()
        analytical_ques_viz()
    else:
        st.markdown('#### No viz display selected yet')

if __name__ == '__main__':
    dashboard_page()
