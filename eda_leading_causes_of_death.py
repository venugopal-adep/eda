import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'NCHS_-_Leading_Causes_of_Death__United_States.csv'
df = pd.read_csv(file_path)

# Sidebar for navigation
st.sidebar.title("EDA Navigation")
options = [
    "Dataset Overview",
    "Descriptive Statistics",
    "Deaths by Year",
    "Age-adjusted Death Rate by State",
    "Leading Causes of Death Word Cloud",
    "Deaths by Cause in 2017",
    "Trend of Heart Disease Deaths Over the Years",
    "Comparison of Death Rates Between States for Cancer in 2017"
]
choice = st.sidebar.radio("Select Visualization", options)

# Function to generate word cloud
def generate_wordcloud(data):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(data)
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud of Leading Causes of Death')
    st.pyplot(plt)

# Display the selected visualization
if choice == "Dataset Overview":
    st.title("Dataset Overview")
    st.write("### Data Preview")
    st.write(df.head())

    st.write("### Explanation of Fields")
    st.write("""
    - **Year**: The year the data was recorded.
    - **113 Cause Name**: The official cause of death code and description.
    - **Cause Name**: Simplified cause of death description.
    - **State**: The state where the death was recorded.
    - **Deaths**: Number of deaths recorded for the cause.
    - **Age-adjusted Death Rate**: The death rate adjusted for age.
    """)

elif choice == "Descriptive Statistics":
    st.title("Descriptive Statistics")
    st.write("### Summary Statistics")
    st.write(df.describe())

elif choice == "Deaths by Year":
    st.title("Total Deaths by Year")
    deaths_by_year = df.groupby('Year')['Deaths'].sum().reset_index()
    fig = px.bar(deaths_by_year, x='Year', y='Deaths', title='Total Deaths by Year')
    st.plotly_chart(fig)

    st.write("**Insights:**")
    st.write("- This visualization shows the total number of deaths recorded each year.")
    st.write("- Identify any trends or anomalies in the number of deaths over the years.")
    st.write("**Recommendation:**")
    st.write("- Investigate years with significant increases or decreases in deaths for potential public health interventions.")

elif choice == "Age-adjusted Death Rate by State":
    st.title("Age-adjusted Death Rate by State")
    fig = px.box(df, x='State', y='Age-adjusted Death Rate', title='Age-adjusted Death Rate by State')
    st.plotly_chart(fig)

    st.write("**Insights:**")
    st.write("- This boxplot shows the distribution of age-adjusted death rates across states.")
    st.write("- States with higher or lower median death rates can be identified.")
    st.write("**Recommendation:**")
    st.write("- Focus on states with consistently high death rates for targeted health programs.")

elif choice == "Leading Causes of Death Word Cloud":
    st.title("Leading Causes of Death Word Cloud")
    generate_wordcloud(' '.join(df['Cause Name']))

    st.write("**Insights:**")
    st.write("- This word cloud visualizes the most common causes of death.")
    st.write("- Larger words represent more frequent causes.")
    st.write("**Recommendation:**")
    st.write("- Develop health awareness campaigns focusing on the most frequent causes of death.")

elif choice == "Deaths by Cause in 2017":
    st.title("Number of Deaths by Cause in 2017")
    year_data = df[df['Year'] == 2017]
    cause_deaths = year_data.groupby('Cause Name')['Deaths'].sum().reset_index().sort_values(by='Deaths', ascending=False)
    fig = px.bar(cause_deaths, x='Deaths', y='Cause Name', title='Number of Deaths by Cause in 2017', orientation='h')
    st.plotly_chart(fig)

    st.write("**Insights:**")
    st.write("- This bar plot shows the number of deaths for each cause in 2017.")
    st.write("- Identify the most lethal causes of death for that year.")
    st.write("**Recommendation:**")
    st.write("- Allocate resources to combat the leading causes of death based on annual data.")

elif choice == "Trend of Heart Disease Deaths Over the Years":
    st.title("Trend of Heart Disease Deaths Over the Years")
    heart_disease_data = df[df['Cause Name'] == 'Heart disease']
    heart_trend = heart_disease_data.groupby('Year')['Deaths'].sum().reset_index()
    fig = px.line(heart_trend, x='Year', y='Deaths', title='Trend of Heart Disease Deaths Over the Years', markers=True)
    st.plotly_chart(fig)

    st.write("**Insights:**")
    st.write("- This line plot shows the trend in the number of deaths due to heart disease over the years.")
    st.write("- Notice any increasing or decreasing patterns.")
    st.write("**Recommendation:**")
    st.write("- Implement long-term health strategies to address rising trends in specific causes of death.")

elif choice == "Comparison of Death Rates Between States for Cancer in 2017":
    st.title("Comparison of Death Rates Between States for Cancer in 2017")
    cause_2017 = df[(df['Year'] == 2017) & (df['Cause Name'] == 'Cancer')]
    fig = px.bar(cause_2017, x='Age-adjusted Death Rate', y='State', title='Age-adjusted Death Rate by State for Cancer in 2017', orientation='h')
    st.plotly_chart(fig)

    st.write("**Insights:**")
    st.write("- This bar plot compares the age-adjusted death rates for cancer across states in 2017.")
    st.write("- States with the highest and lowest death rates are identified.")
    st.write("**Recommendation:**")
    st.write("- Prioritize states with high death rates for cancer screening and prevention programs.")
