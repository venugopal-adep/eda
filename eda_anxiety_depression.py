import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'Indicators_of_Anxiety_or_Depression_Based_on_Reported_Frequency_of_Symptoms_During_Last_7_Days.csv'
data = pd.read_csv(file_path)

# Function to generate a word cloud
def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    return wordcloud

# Function to create bar plot for age group
def plot_age_group(data):
    data_age = data[(data['Indicator'] == 'Symptoms of Depressive Disorder') & (data['Group'] == 'By Age')]
    fig = px.bar(data_age, x='Subgroup', y='Value', title='Symptoms of Depressive Disorder by Age Group',
                 labels={'Subgroup': 'Age Group', 'Value': 'Percentage'})
    return fig

# Function to create line plot for national trends
def plot_national_trends(data):
    data_national = data[(data['Group'] == 'National Estimate') & (data['State'] == 'United States')]
    fig = px.line(data_national, x='Time Period Start Date', y='Value', color='Indicator',
                  title='Trends Over Time for National Estimate',
                  labels={'Time Period Start Date': 'Time Period', 'Value': 'Percentage'})
    return fig

# Function to create bar plot for gender comparison
def plot_gender_comparison(data):
    data_gender = data[data['Group'] == 'By Sex']
    fig = px.bar(data_gender, x='Subgroup', y='Value', color='Indicator', barmode='group',
                 title='Comparison of Symptoms by Gender',
                 labels={'Subgroup': 'Gender', 'Value': 'Percentage'})
    return fig

# Function to create heatmap for state-wise symptoms
def plot_state_heatmap(data):
    data_state = data[data['Group'] == 'By State']
    pivot_table = data_state.pivot_table(values='Value', index='State', columns='Indicator')
    fig = px.imshow(pivot_table, title='Heatmap of State-wise Symptoms', aspect='auto', color_continuous_scale='RdBu_r')
    return fig

# Streamlit application
st.title("Step-by-Step EDA on Indicators of Anxiety or Depression")

# Sidebar for navigation
option = st.sidebar.radio(
    "Select a visualization:",
    ('Dataset Overview', 'Field Explanation', 'Age Group Distribution', 'National Trends', 'Gender Comparison', 'State-wise Heatmap', 'Word Cloud')
)

# Dataset Overview
if option == 'Dataset Overview':
    st.header("Dataset Overview")
    st.dataframe(data)

# Field Explanation
elif option == 'Field Explanation':
    st.header("Field Explanation")
    st.markdown("""
    **Indicator:** Type of mental health issue (e.g., Symptoms of Depressive Disorder, Symptoms of Anxiety Disorder, etc.).  
    **Group:** Category of the data (e.g., National Estimate, By Age, By Sex, etc.).  
    **State:** Geographic area (e.g., United States, individual states).  
    **Subgroup:** Specific subgroup within the population (e.g., age ranges, gender).  
    **Phase:** Data collection phase.  
    **Time Period:** Numerical representation of the time period.  
    **Time Period Label:** Descriptive representation of the time period.  
    **Time Period Start Date:** Start date of the time period.  
    **Time Period End Date:** End date of the time period.  
    **Value:** Reported percentage of individuals with symptoms.  
    **Low CI:** Lower bound of the confidence interval.  
    **High CI:** Upper bound of the confidence interval.  
    **Confidence Interval:** Range of confidence interval.  
    **Quartile Range:** Quartile range of the values.
    """)

# Age Group Distribution
elif option == 'Age Group Distribution':
    st.header("Symptoms of Depressive Disorder by Age Group")
    fig = plot_age_group(data)
    st.plotly_chart(fig)
    st.markdown("**Insight:** Younger age groups (18-29 years) report higher percentages of symptoms compared to older age groups.")
    st.markdown("**Recommendation:** Focus on younger age groups for targeted mental health interventions.")

# National Trends
elif option == 'National Trends':
    st.header("Trends Over Time for National Estimate")
    fig = plot_national_trends(data)
    st.plotly_chart(fig)
    st.markdown("**Insight:** Changes in mental health issues such as anxiety and depressive disorders over different phases are highlighted.")
    st.markdown("**Recommendation:** Use these trends to inform policymakers about the areas and demographics needing immediate attention.")

# Gender Comparison
elif option == 'Gender Comparison':
    st.header("Comparison of Symptoms by Gender")
    fig = plot_gender_comparison(data)
    st.plotly_chart(fig)
    st.markdown("**Insight:** This comparison helps in understanding gender disparities in mental health.")
    st.markdown("**Recommendation:** Increase awareness campaigns and support services, especially for groups with higher percentages of symptoms.")

# State-wise Heatmap
elif option == 'State-wise Heatmap':
    st.header("Heatmap of State-wise Symptoms")
    fig = plot_state_heatmap(data)
    st.plotly_chart(fig)
    st.markdown("**Insight:** The heatmap shows the variations in reported symptoms across different states.")
    st.markdown("**Recommendation:** Focus on states with higher reported symptoms for targeted mental health interventions.")

# Word Cloud
elif option == 'Word Cloud':
    st.header("Word Cloud of Mental Health Indicators")
    text = ' '.join(data['Indicator'].unique())
    wordcloud = generate_wordcloud(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)
    st.markdown("**Insight:** The word cloud highlights the various mental health indicators present in the dataset.")
    st.markdown("**Recommendation:** Use these insights for further research and to inform strategic decision-making to improve mental health outcomes.")

#st.sidebar.markdown("**Call to Action:** Follow us on LinkedIn for more insights and updates on mental health research and data analysis.")
