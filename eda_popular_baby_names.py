import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np

# Placeholder for loading the dataset
file_path_baby_names = 'Popular_Baby_Names.csv'

# Load the dataset
# data_baby_names = pd.read_csv(file_path_baby_names)

# For demonstration purposes, create a sample dataframe
data_baby_names = pd.DataFrame({
    'Year of Birth': pd.date_range(start='2000', periods=20, freq='Y').year,
    'Gender': np.random.choice(['MALE', 'FEMALE'], 20),
    'Ethnicity': np.random.choice(['ASIAN AND PACIFIC ISLANDER', 'BLACK NON HISPANIC', 'WHITE NON HISPANIC', 'HISPANIC'], 20),
    'Child\'s First Name': np.random.choice(['Emma', 'Liam', 'Noah', 'Olivia', 'Ava', 'Sophia', 'Isabella', 'Mason', 'Jacob', 'Ethan'], 20),
    'Count': np.random.randint(1, 100, 20)
})

# Function to display insights and recommendations
def display_insights_and_recommendations(insights, recommendations):
    st.markdown("### Insights")
    st.write(insights)
    st.markdown("### Recommendations")
    st.write(recommendations)

# App title
st.title("Popular Baby Names Analysis")
st.write("""
         Popular Baby Names
Metadata Updated: June 15, 2024

Popular Baby Names by Sex and Ethnic Group Data were collected through civil birth registration. Each record represents the ranking of a baby name in the order of frequency. Data can be used to represent the popularity of a name. Caution should be used when assessing the rank of a baby name if the frequency count is close to 10; the ranking may vary year to year.
         """)

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Select a visualization:", ["Overview", "Most Popular Names Over Time", "Most Popular Names by Gender", "Name Trends Over Time", "Word Cloud of Popular Names", "Distribution of Names by Birth Year"])

# Overview of the dataset
if options == "Overview":
    st.header("Overview of the Dataset")
    st.dataframe(data_baby_names.head())
    display_insights_and_recommendations(
        "The dataset includes baby names along with their birth year, gender, ethnicity, and count.",
        "Familiarize yourself with the dataset structure to understand the variables available for deeper analysis."
    )

# Most Popular Names Over Time
elif options == "Most Popular Names Over Time":
    st.header("Most Popular Names Over Time")
    fig = px.bar(data_baby_names, x='Year of Birth', y='Count', color='Child\'s First Name', title='Most Popular Names Over Time')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        "Certain names remain popular over several years, while others fluctuate in popularity.",
        "Analyze the cultural and social factors influencing the popularity of certain names."
    )

# Most Popular Names by Gender
elif options == "Most Popular Names by Gender":
    st.header("Most Popular Names by Gender")
    gender = st.selectbox("Select a gender:", data_baby_names['Gender'].unique())
    filtered_data = data_baby_names[data_baby_names['Gender'] == gender]
    fig = px.bar(filtered_data, x='Child\'s First Name', y='Count', title=f'Most Popular Names for {gender}')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        f"Popular names for {gender} show distinct trends.",
        "Explore the reasons behind the popularity of certain names for each gender."
    )

# Name Trends Over Time
elif options == "Name Trends Over Time":
    st.header("Name Trends Over Time")
    name = st.selectbox("Select a name:", data_baby_names['Child\'s First Name'].unique())
    filtered_data = data_baby_names[data_baby_names['Child\'s First Name'] == name]
    fig = px.line(filtered_data, x='Year of Birth', y='Count', title=f'Trend of the Name {name} Over Time')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        f"The name {name} shows varying popularity over the years.",
        "Consider the social and cultural factors that may influence these trends."
    )

# Word Cloud of Popular Names
elif options == "Word Cloud of Popular Names":
    st.header("Word Cloud of Popular Names")
    name_counts = data_baby_names.groupby('Child\'s First Name')['Count'].sum().to_dict()
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(name_counts)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)
    display_insights_and_recommendations(
        "The word cloud visualizes the frequency of popular names.",
        "Use the word cloud to identify the most common names at a glance."
    )

# Distribution of Names by Birth Year
elif options == "Distribution of Names by Birth Year":
    st.header("Distribution of Names by Birth Year")
    fig = px.histogram(data_baby_names, x='Year of Birth', title='Distribution of Names by Birth Year')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        "The distribution shows the frequency of name occurrences by birth year.",
        "Investigate any notable patterns or anomalies in name distribution over the years."
    )

# Footer
#st.sidebar.markdown("---")
#st.sidebar.markdown("Developed by [Your Name]")
