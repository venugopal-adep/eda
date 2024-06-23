import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np

# Placeholder for loading the dataset
file_path_arrest_data = 'NYPD_Arrest_Data__Year_to_Date_.csv'

# Load the dataset
# data_arrest = pd.read_csv(file_path_arrest_data)

# For demonstration purposes, create a sample dataframe
data_arrest = pd.DataFrame({
    'ARREST_DATE': pd.date_range(start='2020-01-01', periods=100, freq='D'),
    'AGE_GROUP': np.random.choice(['<18', '18-24', '25-44', '45-64', '65+'], 100),
    'PERP_SEX': np.random.choice(['M', 'F'], 100),
    'OFNS_DESC': np.random.choice(['ROBBERY', 'ASSAULT 3 & RELATED OFFENSES', 'LARCENY', 'DANGEROUS DRUGS', 'MURDER & NON-NEGLIGENT MANSLAUGHTER'], 100),
    'ARREST_BORO': np.random.choice(['MANHATTAN', 'BRONX', 'BROOKLYN', 'QUEENS', 'STATEN ISLAND'], 100),
    'Latitude': np.random.uniform(40.5, 40.9, 100),
    'Longitude': np.random.uniform(-74.25, -73.7, 100)
})

# Function to display insights and recommendations
def display_insights_and_recommendations(insights, recommendations):
    st.markdown("### Insights")
    st.write(insights)
    st.markdown("### Recommendations")
    st.write(recommendations)

# App title
st.title("NYPD Arrest Data Analysis - Year to Date")
st.write("""
         NYPD Arrest Data (Year to Date)
Metadata Updated: April 26, 2024

This is a breakdown of every arrest effected in NYC by the NYPD during the current year. This data is manually extracted every quarter and reviewed by the Office of Management Analysis and Planning. Each record represents an arrest effected in NYC by the NYPD and includes information about the type of crime, the location and time of enforcement. In addition, information related to suspect demographics is also included. This data can be used by the public to explore the nature of police enforcement activity. Please refer to the attached data footnotes for additional information about this dataset.
         """)

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Select a visualization:", ["Overview", "Arrests Over Time", "Arrests by Age Group", "Arrests by Gender", "Arrests by Offense Description", "Geographical Distribution", "Correlation Analysis", "Word Cloud of Offense Descriptions"])

# Overview of the dataset
if options == "Overview":
    st.header("Overview of the Dataset")
    st.dataframe(data_arrest.head())
    display_insights_and_recommendations(
        """
        - The dataset includes information on arrests such as arrest date, age group, gender, offense description, and location.
        - It provides a comprehensive view of arrest trends and patterns over time and geography.
        """,
        """
        - Familiarize yourself with the dataset structure to understand the variables available for deeper analysis.
        - Use this overview to identify potential areas of interest for further exploration.
        """
    )

# Arrests Over Time
elif options == "Arrests Over Time":
    st.header("Arrests Over Time")
    fig = px.histogram(data_arrest, x='ARREST_DATE', title='Arrests Over Time')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The histogram shows the number of arrests over different dates.
        - Peaks in certain periods might indicate higher police activity or specific incidents leading to more arrests.
        """,
        """
        - Investigate the reasons behind peaks in arrests for certain periods.
        - Consider the impact of specific events or policies on the number of arrests.
        """
    )

# Arrests by Age Group
elif options == "Arrests by Age Group":
    st.header("Arrests by Age Group")
    fig = px.histogram(data_arrest, x='AGE_GROUP', title='Arrests by Age Group')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The histogram shows the distribution of arrests across different age groups.
        - Certain age groups might have higher arrest rates, indicating potential areas for targeted interventions.
        """,
        """
        - Investigate the factors contributing to higher arrest rates in specific age groups.
        - Develop targeted intervention programs to address the underlying causes of higher arrest rates among specific age groups.
        """
    )

# Arrests by Gender
elif options == "Arrests by Gender":
    st.header("Arrests by Gender")
    fig = px.histogram(data_arrest, x='PERP_SEX', title='Arrests by Gender')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The histogram shows the distribution of arrests between males and females.
        - There might be a significant difference in arrest rates between genders.
        """,
        """
        - Investigate the reasons behind the gender disparity in arrest rates.
        - Consider gender-specific strategies to address the underlying causes of arrests.
        """
    )

# Arrests by Offense Description
elif options == "Arrests by Offense Description":
    st.header("Arrests by Offense Description")
    fig = px.histogram(data_arrest, x='OFNS_DESC', title='Arrests by Offense Description')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The histogram shows the distribution of arrests for different offense descriptions.
        - Certain offenses might have higher arrest rates, indicating areas for focused law enforcement efforts.
        """,
        """
        - Investigate the factors contributing to higher arrest rates for specific offenses.
        - Develop strategies to prevent and reduce the occurrence of high-arrest offenses.
        """
    )

# Geographical Distribution of Arrests
elif options == "Geographical Distribution":
    st.header("Geographical Distribution of Arrests")
    fig = px.scatter_mapbox(data_arrest, lat='Latitude', lon='Longitude', hover_name='OFNS_DESC', color='ARREST_BORO', title='Geographical Distribution of Arrests', mapbox_style="carto-positron")
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The scatter map shows the geographical distribution of arrests across different boroughs.
        - Certain areas might have higher arrest concentrations, indicating hotspots of criminal activity.
        """,
        """
        - Analyze the geographical distribution to identify crime hotspots.
        - Implement targeted policing and community programs in high-arrest areas to reduce crime.
        """
    )

# Correlation Analysis
elif options == "Correlation Analysis":
    st.header("Correlation Analysis Between Variables")
    numeric_data = data_arrest.select_dtypes(include=[np.number])
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
        - Use correlation insights to inform strategies for reducing crime and improving law enforcement effectiveness.
        """
    )

# Word Cloud of Offense Descriptions
elif options == "Word Cloud of Offense Descriptions":
    st.header("Word Cloud of Offense Descriptions")
    offense_counts = data_arrest['OFNS_DESC'].value_counts().to_dict()
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(offense_counts)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)
    display_insights_and_recommendations(
        """
        - The word cloud visualizes the frequency of different offense descriptions.
        - Larger words indicate more common offenses within the dataset.
        """,
        """
        - Use the word cloud to identify the most common offenses at a glance.
        - Focus on developing strategies to address the most frequently occurring offenses.
        """
    )

# Footer
#st.sidebar.markdown("---")
#st.sidebar.markdown("Developed by [Your Name]")
