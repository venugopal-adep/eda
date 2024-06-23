import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'Mental_Health_Care_in_the_Last_4_Weeks.csv'
df = pd.read_csv(file_path)

# Sidebar for navigation
st.sidebar.title("EDA Navigation")
options = [
    "Dataset Overview",
    "Descriptive Statistics",
    "Mental Health Care by Group",
    "Mental Health Care by State",
    "Mental Health Care by Subgroup (Age)",
    "Word Cloud of Indicators",
    "Trend of Mental Health Care Over Time"
]
choice = st.sidebar.radio("Select Visualization", options)

# Function to generate word cloud
def generate_wordcloud(data):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(data)
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud of Indicators')
    st.pyplot(plt)

# Display the selected visualization
if choice == "Dataset Overview":
    st.title("Mental Health Care in the Last 4 Weeks")
    st.write("""
    Metadata Updated: April 15, 2023

The U.S. Census Bureau, in collaboration with five federal agencies, launched the Household Pulse Survey to produce data on the social and economic impacts of Covid-19 on American households. The Household Pulse Survey was designed to gauge the impact of the pandemic on employment status, consumer spending, food security, housing, education disruptions, and dimensions of physical and mental wellness.

The survey was designed to meet the goal of accurate and timely weekly estimates. It was conducted by an internet questionnaire, with invitations to participate sent by email and text message. The sample frame is the Census Bureau Master Address File Data. Housing units linked to one or more email addresses or cell phone numbers were randomly selected to participate, and one respondent from each housing unit was selected to respond for him or herself. Estimates are weighted to adjust for nonresponse and to match Census Bureau estimates of the population by age, gender, race and ethnicity, and educational attainment. All estimates shown meet the NCHS Data Presentation Standards for Proportions.
             """)
    st.write("### Data Preview")
    st.write(df.head())

    st.write("### Explanation of Fields")
    st.write("""
    - **Indicator**: Description of the mental health care metric.
    - **Group**: Group categorization (e.g., National Estimate, By Age).
    - **State**: The state where the data was recorded.
    - **Subgroup**: Subgroup details (e.g., specific age group).
    - **Phase**: Phase of the data collection.
    - **Time Period**: Time period number.
    - **Time Period Label**: Label of the time period.
    - **Time Period Start Date**: Start date of the time period.
    - **Time Period End Date**: End date of the time period.
    - **Value**: Value of the mental health care metric.
    - **LowCI** and **HighCI**: Lower and upper bounds of the confidence interval.
    - **Confidence Interval**: Combined confidence interval as a string.
    """)

elif choice == "Descriptive Statistics":
    st.title("Descriptive Statistics")
    st.write("### Summary Statistics")
    st.write(df.describe())

elif choice == "Mental Health Care by Group":
    st.title("Mental Health Care by Group")
    group_data = df.groupby('Group')['Value'].mean().reset_index()
    fig = px.bar(group_data, x='Group', y='Value', title='Average Mental Health Care Value by Group')
    st.plotly_chart(fig)

    st.write("**Insights:**")
    st.write("- This bar chart shows the average mental health care value by group.")
    st.write("- Identify which groups have higher or lower average values.")

    st.write("**Recommendation:**")
    st.write("- Focus on groups with lower mental health care values for targeted interventions.")

elif choice == "Mental Health Care by State":
    st.title("Mental Health Care by State")
    state_data = df.groupby('State')['Value'].mean().reset_index()
    fig = px.bar(state_data, x='Value', y='State', title='Average Mental Health Care Value by State', orientation='h')
    st.plotly_chart(fig)

    st.write("**Insights:**")
    st.write("- This horizontal bar chart shows the average mental health care value by state.")
    st.write("- States with higher or lower average values are easily identified.")

    st.write("**Recommendation:**")
    st.write("- Prioritize states with lower mental health care values for additional resources and support.")

elif choice == "Mental Health Care by Subgroup (Age)":
    st.title("Mental Health Care by Subgroup (Age)")
    age_data = df[df['Group'] == 'By Age']
    fig = px.box(age_data, x='Subgroup', y='Value', title='Mental Health Care Value by Age Group')
    st.plotly_chart(fig)

    st.write("**Insights:**")
    st.write("- This box plot shows the distribution of mental health care values across different age groups.")
    st.write("- Identify age groups with higher variability or extreme values.")

    st.write("**Recommendation:**")
    st.write("- Tailor mental health programs to age groups with lower care values or higher variability.")

elif choice == "Word Cloud of Indicators":
    st.title("Word Cloud of Indicators")
    indicator_text = ' '.join(df['Indicator'])
    generate_wordcloud(indicator_text)

    st.write("**Insights:**")
    st.write("- This word cloud visualizes the most common indicators related to mental health care.")
    st.write("- Larger words represent more frequently occurring indicators.")

    st.write("**Recommendation:**")
    st.write("- Focus on addressing the most common indicators in mental health care programs.")

elif choice == "Trend of Mental Health Care Over Time":
    st.title("Trend of Mental Health Care Over Time")
    time_data = df.groupby('Time Period Label')['Value'].mean().reset_index()
    fig = px.line(time_data, x='Time Period Label', y='Value', title='Trend of Mental Health Care Over Time', markers=True)
    st.plotly_chart(fig)

    st.write("**Insights:**")
    st.write("- This line plot shows the trend of mental health care values over different time periods.")
    st.write("- Identify any increasing or decreasing trends in mental health care.")

    st.write("**Recommendation:**")
    st.write("- Implement long-term strategies to address observed trends in mental health care.")
