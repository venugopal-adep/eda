import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Placeholder for loading the dataset
file_path_air_quality = 'Air_Quality.csv'

# Load the dataset
data_air_quality = pd.read_csv(file_path_air_quality)

# For demonstration purposes, create a sample dataframe
# data_air_quality = pd.DataFrame({
#     'Date': pd.date_range(start='1/1/2020', periods=100),
#     'PM2.5': np.random.rand(100) * 100,
#     'PM10': np.random.rand(100) * 150,
#     'NO2': np.random.rand(100) * 80,
#     'SO2': np.random.rand(100) * 20,
#     'O3': np.random.rand(100) * 120,
#     'Location': np.random.choice(['Location1', 'Location2', 'Location3'], 100)
# })

# Function to display insights and recommendations
def display_insights_and_recommendations(insights, recommendations):
    st.markdown("### Insights")
    st.write(insights)
    st.markdown("### Recommendations")
    st.write(recommendations)

# App title
st.title("Air Quality Analysis")
st.write("""
         Air Quality
Metadata Updated: April 19, 2024

Dataset contains information on New York City air quality surveillance data.

Air pollution is one of the most important environmental threats to urban populations and while all people are exposed, pollutant emissions, levels of exposure, and population vulnerability vary across neighborhoods. Exposures to common air pollutants have been linked to respiratory and cardiovascular diseases, cancers, and premature deaths. These indicators provide a perspective across time and NYC geographies to better characterize air quality and health in NYC. Data can also be explored online at the Environment and Health Data Portal: http://nyc.gov/health/environmentdata.
         """)

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Select a visualization:", ["Overview", "Time Series Analysis", "Air Quality by Location", "Correlation Analysis", "Pollutant Distribution"])

# Overview of the dataset
if options == "Overview":
    st.header("Overview of the Dataset")
    st.dataframe(data_air_quality.head())
    display_insights_and_recommendations(
        "The dataset includes various air quality indicators such as PM2.5, PM10, NO2, SO2, and O3, along with the date and location.",
        "Familiarize yourself with the dataset structure to understand the variables available for deeper analysis."
    )

# Time Series Analysis
elif options == "Time Series Analysis":
    st.header("Time Series Analysis of Air Quality Indicators")
    pollutant = st.selectbox("Select a pollutant:", ["PM2.5", "PM10", "NO2", "SO2", "O3"])
    fig = px.line(data_air_quality, x='Date', y=pollutant, title=f'Time Series Analysis of {pollutant}')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        f"The levels of {pollutant} fluctuate over time with noticeable peaks.",
        "Investigate the causes of high pollution levels during peak periods."
    )

# Air Quality by Location
elif options == "Air Quality by Location":
    st.header("Air Quality by Location")
    location = st.selectbox("Select a location:", data_air_quality['Location'].unique())
    filtered_data = data_air_quality[data_air_quality['Location'] == location]
    fig = px.line(filtered_data, x='Date', y='PM2.5', title=f'PM2.5 Levels in {location}')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        f"The PM2.5 levels in {location} show varying levels of pollution over time.",
        "Implement localized pollution control measures based on the trends observed."
    )

# Correlation Analysis
elif options == "Correlation Analysis":
    st.header("Correlation Analysis Between Pollutants")
    corr = data_air_quality[['PM2.5', 'PM10', 'NO2', 'SO2', 'O3']].corr()
    fig = px.imshow(corr, title='Correlation Matrix of Pollutants')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        "Certain pollutants show strong correlations with each other.",
        "Focus on correlated pollutants for combined pollution control strategies."
    )

# Pollutant Distribution
elif options == "Pollutant Distribution":
    st.header("Distribution of Pollutants")
    pollutant = st.selectbox("Select a pollutant:", ["PM2.5", "PM10", "NO2", "SO2", "O3"])
    fig = px.histogram(data_air_quality, x=pollutant, title=f'Distribution of {pollutant}')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        f"The distribution of {pollutant} shows the frequency of different pollution levels.",
        "Identify the common pollution levels and investigate the factors contributing to them."
    )

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("Developed by [Your Name]")
