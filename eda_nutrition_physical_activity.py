import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'Nutrition__Physical_Activity__and_Obesity_-_Behavioral_Risk_Factor_Surveillance_System1.csv'
data = pd.read_csv(file_path)

# Define column explanations
column_explanations = {
    "YearStart": "Start year of data collection.",
    "YearEnd": "End year of data collection.",
    "LocationAbbr": "Abbreviation of the location.",
    "LocationDesc": "Description of the location.",
    "Datasource": "Source of the data.",
    "Class": "Category of the data.",
    "Topic": "Specific topic of the data.",
    "Question": "Question asked in the survey.",
    "Data_Value_Unit": "Unit of the data value.",
    "Data_Value_Type": "Type of the data value.",
    "Data_Value": "Value of the data.",
    "Data_Value_Footnote_Symbol": "Footnote symbol for the data value.",
    "Data_Value_Footnote": "Footnote for the data value.",
    "Low_Confidence_Limit": "Lower confidence limit of the data value.",
    "High_Confidence_Limit": "Higher confidence limit of the data value.",
    "Sample_Size": "Sample size of the data collection.",
    "Total": "Total number of observations.",
    "Age(years)": "Age of respondents in years.",
    "Education": "Education level of respondents.",
    "Gender": "Gender of respondents.",
    "Income": "Income level of respondents.",
    "Race/Ethnicity": "Race/Ethnicity of respondents.",
    "GeoLocation": "Geolocation coordinates.",
    "ClassID": "ID for the class.",
    "TopicID": "ID for the topic.",
    "QuestionID": "ID for the question.",
    "DataValueTypeID": "ID for the data value type.",
    "LocationID": "ID for the location.",
    "StratificationCategory1": "First stratification category.",
    "Stratification1": "First stratification.",
    "StratificationCategoryId1": "ID for the first stratification category.",
    "StratificationID1": "ID for the first stratification."
}

# Sidebar for navigation
st.sidebar.title("EDA Navigation")
visualization = st.sidebar.radio(
    "Select a visualization",
    (
        "Dataset Overview",
        "Distribution of Data Collection Years",
        "Geographic Distribution of Data",
        "Data Sources and Categories",
        "Topics and Questions",
        "Demographic Stratifications",
        "Distribution of Data Values",
        "Summary of Insights and Recommendations",
    ),
)

# Function to display dataset overview
def dataset_overview():
    st.title("Nutrition and Physical Activity")
    st.write("""
             Nutrition, Physical Activity, and Obesity - Behavioral Risk Factor Surveillance System
Metadata Updated: December 8, 2023

This dataset includes data on adult's diet, physical activity, and weight status from Behavioral Risk Factor Surveillance System. This data is used for DNPAO's Data, Trends, and Maps database, which provides national and state specific data on obesity, nutrition, physical activity, and breastfeeding.
             
             """)
    st.write(data.head())
    st.write("**Number of Rows and Columns:**", data.shape)
    st.write("**Column Names and Descriptions:**")
    for column, description in column_explanations.items():
        st.write(f"**{column}**: {description}")

# Function to display distribution of data collection years
def data_collection_years():
    st.title("Distribution of Data Collection Years")
    year_counts = data['YearStart'].value_counts().sort_index()
    fig = px.bar(year_counts, x=year_counts.index, y=year_counts.values, labels={'x': 'Year', 'y': 'Frequency'}, title='Distribution of Data Collection Years')
    st.plotly_chart(fig)
    st.write("**Insights:**")
    st.write("- The dataset includes data collected over several years, from 2011 to 2020.")
    st.write("- Certain years have more data entries than others, indicating more extensive surveys or data collection efforts during those periods.")
    st.write("**Recommendation:**")
    st.write("- Focus on trends over time to understand how physical activity and obesity-related behaviors have changed over the years.")

# Function to display geographic distribution of data
def geographic_distribution():
    st.title("Geographic Distribution of Data")
    location_counts = data['LocationDesc'].value_counts()
    fig = px.bar(location_counts, x=location_counts.index, y=location_counts.values, labels={'x': 'Location', 'y': 'Frequency'}, title='Geographic Distribution of Data')
    fig.update_layout(xaxis={'categoryorder':'total descending'}, xaxis_tickangle=-45)
    st.plotly_chart(fig)
    st.write("**Insights:**")
    st.write("- Data is collected from various locations, including states and territories within the United States.")
    st.write("- National-level data is also prominently represented.")
    st.write("**Recommendation:**")
    st.write("- Analyze the geographic differences in physical activity and obesity-related behaviors to identify areas that may need more targeted interventions.")

# Function to display data sources and categories
def data_sources_categories():
    st.title("Data Sources and Categories")
    datasource_counts = data['Datasource'].value_counts()
    class_counts = data['Class'].value_counts()
    fig1 = px.bar(datasource_counts, x=datasource_counts.index, y=datasource_counts.values, labels={'x': 'Datasource', 'y': 'Frequency'}, title='Data Sources Distribution')
    fig2 = px.bar(class_counts, x=class_counts.index, y=class_counts.values, labels={'x': 'Class', 'y': 'Frequency'}, title='Class Distribution')
    st.plotly_chart(fig1)
    st.plotly_chart(fig2)
    st.write("**Insights:**")
    st.write("- The primary data source is the Behavioral Risk Factor Surveillance System.")
    st.write("- The classes include Physical Activity, Obesity / Weight Status, and other related categories.")
    st.write("**Recommendation:**")
    st.write("- Ensure to explore each class separately to understand the specific behaviors and risk factors associated with each category.")

# Function to display word cloud of topics and questions
def topics_questions():
    st.title("Topics and Questions")
    topics = ' '.join(data['Topic'].dropna().unique())
    questions = ' '.join(data['Question'].dropna().unique())
    wordcloud_topics = WordCloud(width=800, height=400, background_color='white').generate(topics)
    wordcloud_questions = WordCloud(width=800, height=400, background_color='white').generate(questions)
    
    st.write("**Word Cloud of Topics**")
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud_topics, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)
    
    st.write("**Word Cloud of Questions**")
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud_questions, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)

    st.write("**Insights:**")
    st.write("- Common topics include physical activity, obesity, and weight status.")
    st.write("- Questions focus on behaviors, demographic factors, and health outcomes related to these topics.")
    st.write("**Recommendation:**")
    st.write("- Dive deeper into specific questions to understand the detailed behaviors and outcomes being measured.")

# Function to display demographic stratifications
def demographic_stratifications():
    st.title("Demographic Stratifications")
    stratification_category_counts = data['StratificationCategory1'].value_counts()
    stratification_counts = data['Stratification1'].value_counts()
    fig1 = px.bar(stratification_category_counts, x=stratification_category_counts.index, y=stratification_category_counts.values, labels={'x': 'Stratification Category', 'y': 'Frequency'}, title='Stratification Category Distribution')
    fig2 = px.bar(stratification_counts, x=stratification_counts.index, y=stratification_counts.values, labels={'x': 'Stratification', 'y': 'Frequency'}, title='Stratification Distribution')
    fig2.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig1)
    st.plotly_chart(fig2)
    st.write("**Insights:**")
    st.write("- Stratifications are made based on categories such as race/ethnicity, education, income, etc.")
    st.write("- A wide range of stratifications helps in understanding the diversity in behaviors across different demographic groups.")
    st.write("**Recommendation:**")
    st.write("- Analyze how different demographic groups vary in terms of physical activity and obesity-related behaviors to identify specific target groups for interventions.")

# Function to display distribution of data values
def data_values_distribution():
    st.title("Distribution of Data Values")
    fig = px.histogram(data, x='Data_Value', nbins=30, title='Distribution of Data Values')
    st.plotly_chart(fig)
    st.write("**Insights:**")
    st.write("- The distribution of data values shows the variability in the measured behaviors and outcomes.")
    st.write("- Identifying any outliers or unusual distributions is crucial for further analysis.")
    st.write("**Recommendation:**")
    st.write("- Focus on data cleaning and normalization where necessary to ensure accurate analysis.")

# Function to display summary of insights and recommendations

# Function to display summary of insights and recommendations
def summary_insights():
    st.title("Summary of Insights and Recommendations")
    st.write("**Insights:**")
    st.write("1. The dataset covers multiple years, locations, and demographic groups, providing a comprehensive view of physical activity and obesity-related behaviors.")
    st.write("2. Geographic and demographic differences are evident, suggesting the need for targeted interventions.")
    st.write("3. The variability in data values indicates a need for careful cleaning and normalization.")
    st.write("**Recommendation:**")
    st.write("- Conduct further analysis focusing on temporal trends, geographic disparities, and demographic differences to develop targeted public health strategies.")
    st.write("- Utilize the rich stratification data to understand the specific needs of different demographic groups and tailor interventions accordingly.")

# Display the selected visualization
if visualization == "Dataset Overview":
    dataset_overview()
elif visualization == "Distribution of Data Collection Years":
    data_collection_years()
elif visualization == "Geographic Distribution of Data":
    geographic_distribution()
elif visualization == "Data Sources and Categories":
    data_sources_categories()
elif visualization == "Topics and Questions":
    topics_questions()
elif visualization == "Demographic Stratifications":
    demographic_stratifications()
elif visualization == "Distribution of Data Values":
    data_values_distribution()
elif visualization == "Summary of Insights and Recommendations":
    summary_insights()
