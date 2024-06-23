import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np

# Placeholder for loading the dataset
file_path = 'Normal_weight__overweight__and_obesity_among_adults_aged_20_and_over__by_selected_characteristics__United_States.csv'

# Load the dataset
# data_obesity = pd.read_csv(file_path)

# For demonstration purposes, create a sample dataframe
data_obesity = pd.DataFrame({
    'Year': np.random.choice(range(2000, 2021), 100),
    'Age Group': np.random.choice(['20-29', '30-39', '40-49', '50-59', '60-69', '70+'], 100),
    'Gender': np.random.choice(['Male', 'Female'], 100),
    'Race/Ethnicity': np.random.choice(['White', 'Black', 'Hispanic', 'Asian'], 100),
    'BMI Category': np.random.choice(['Normal weight', 'Overweight', 'Obesity'], 100),
    'Percentage': np.random.uniform(10, 50, 100)
})

# Function to display insights and recommendations
def display_insights_and_recommendations(insights, recommendations):
    st.markdown("### Insights")
    st.write(insights)
    st.markdown("### Recommendations")
    st.write(recommendations)

# App title
st.title("Obesity Trends Analysis")

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Select a visualization:", ["Overview", "Obesity Trends Over Time", "Obesity by Age Group", "Obesity by Gender", "Obesity by Race/Ethnicity", "Correlation Analysis"])

# Overview of the dataset
if options == "Overview":
    st.header("Overview of the Dataset")
    st.dataframe(data_obesity.head())
    display_insights_and_recommendations(
        """
        - The dataset includes information on obesity trends categorized by year, age group, gender, race/ethnicity, and BMI category.
        - It provides a comprehensive view of obesity trends over time and across different demographic groups.
        """,
        """
        - Familiarize yourself with the dataset structure to understand the variables available for deeper analysis.
        - Use this overview to identify potential areas of interest for further exploration.
        """
    )

# Obesity Trends Over Time
elif options == "Obesity Trends Over Time":
    st.header("Obesity Trends Over Time")
    fig = px.bar(data_obesity, x='Year', y='Percentage', color='BMI Category', title='Obesity Trends Over Time', barmode='group')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The bar chart shows the trends of different BMI categories over the years.
        - There might be an increasing trend in obesity rates, indicating a growing public health concern.
        """,
        """
        - Investigate the factors contributing to the rising obesity rates over the years.
        - Develop and promote public health initiatives to address the increasing trend in obesity.
        """
    )

# Obesity by Age Group
elif options == "Obesity by Age Group":
    st.header("Obesity by Age Group")
    fig = px.bar(data_obesity, x='Age Group', y='Percentage', color='BMI Category', title='Obesity by Age Group', barmode='group')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The bar chart shows the distribution of BMI categories across different age groups.
        - Certain age groups might have higher rates of obesity, indicating targeted areas for intervention.
        """,
        """
        - Investigate the lifestyle and environmental factors contributing to higher obesity rates in specific age groups.
        - Develop age-specific health and wellness programs to combat obesity.
        """
    )

# Obesity by Gender
elif options == "Obesity by Gender":
    st.header("Obesity by Gender")
    fig = px.histogram(data_obesity, x='Gender', y='Percentage', color='BMI Category', barmode='group', title='Obesity by Gender')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The histogram shows the distribution of BMI categories between males and females.
        - There might be gender differences in obesity rates, indicating a need for gender-specific interventions.
        """,
        """
        - Investigate the reasons behind gender disparities in obesity rates.
        - Develop gender-specific strategies to address the underlying causes of obesity.
        """
    )

# Obesity by Race/Ethnicity
elif options == "Obesity by Race/Ethnicity":
    st.header("Obesity by Race/Ethnicity")
    fig = px.bar(data_obesity, x='Race/Ethnicity', y='Percentage', color='BMI Category', title='Obesity by Race/Ethnicity', barmode='group')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The bar chart shows the distribution of BMI categories across different racial and ethnic groups.
        - Certain racial/ethnic groups might have higher obesity rates, indicating areas for focused public health efforts.
        """,
        """
        - Investigate the cultural, socio-economic, and environmental factors contributing to obesity in specific racial/ethnic groups.
        - Develop culturally sensitive and community-based interventions to reduce obesity rates.
        """
    )

# Correlation Analysis
elif options == "Correlation Analysis":
    st.header("Correlation Analysis Between Variables")
    numeric_data = data_obesity.select_dtypes(include=[np.number])
    corr = numeric_data.corr()
    fig = px.imshow(corr, title='Correlation Matrix of Variables')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The correlation matrix shows the relationships between different numeric variables.
        - Strong correlations can highlight underlying patterns or trends in the data.
        """,
        """
        - Focus on correlated variables for more detailed analysis.
        - Use correlation insights to inform strategies for addressing obesity through targeted interventions.
        """
    )

# Footer
#st.sidebar.markdown("---")
#st.sidebar.markdown("Developed by [Your Name]")
