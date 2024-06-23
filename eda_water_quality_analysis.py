import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np

# Placeholder for loading the dataset
file_path_water_quality = 'BKB_WaterQualityData_2020084.csv'

# Load the dataset
# data_water_quality = pd.read_csv(file_path_water_quality)

# For demonstration purposes, create a sample dataframe
data_water_quality = pd.DataFrame({
    'Date': pd.date_range(start='2020-01-01', periods=100, freq='M'),
    'Location': np.random.choice(['River A', 'River B', 'Lake A', 'Lake B'], 100),
    'Season': np.random.choice(['Spring', 'Summer', 'Autumn', 'Winter'], 100),
    'pH': np.random.uniform(6.5, 8.5, 100),
    'Dissolved Oxygen': np.random.uniform(5, 15, 100),
    'Nitrate': np.random.uniform(0, 10, 100),
    'Phosphate': np.random.uniform(0, 5, 100),
    'Temperature': np.random.uniform(10, 30, 100),
    'Turbidity': np.random.uniform(1, 10, 100)
})

# Function to display insights and recommendations
def display_insights_and_recommendations(insights, recommendations):
    st.markdown("### Insights")
    st.write(insights)
    st.markdown("### Recommendations")
    st.write(recommendations)

# App title
st.title("Water Quality Analysis")
st.write("""
         Water Quality Data
Metadata Updated: October 29, 2023

Water quality data for the Refuge collected by volunteers collected once every two weeks: Turbidity, pH, Dissolved oxygen (DO), Salinity & Temperature. Sampling will occur at designated locations in the following water bodies: the Bay, D-Pool (fishing pond), C-Pool, B-Pool and A-Pool.
         """)

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Select a visualization:", [
    "Overview", "Water Quality Trends Over Time", "Parameter Levels by Location", "Parameter Levels by Season",
    "Parameter Correlations", "Heatmap of Parameter Levels", "Top Pollutants", "Parameter Distributions", "Word Cloud of Pollutants"])

# Overview of the dataset
if options == "Overview":
    st.header("Overview of the Dataset")
    st.dataframe(data_water_quality.head())
    display_insights_and_recommendations(
        """
        - The dataset includes information on various water quality parameters such as pH, dissolved oxygen, nitrate, phosphate, temperature, and turbidity.
        - It provides a comprehensive view of water quality trends and patterns over time and across different locations and seasons.
        """,
        """
        - Familiarize yourself with the dataset structure to understand the variables available for deeper analysis.
        - Use this overview to identify potential areas of interest for further exploration.
        """
    )

# Water Quality Trends Over Time
elif options == "Water Quality Trends Over Time":
    st.header("Water Quality Trends Over Time")
    fig = px.line(data_water_quality, x='Date', y=['pH', 'Dissolved Oxygen', 'Nitrate', 'Phosphate', 'Temperature', 'Turbidity'], title='Water Quality Trends Over Time')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The line chart shows the trends of various water quality parameters over time.
        - There might be seasonal patterns or trends indicating changes in water quality.
        """,
        """
        - Investigate the factors contributing to changes in water quality parameters over time.
        - Develop strategies to manage and improve water quality based on identified trends.
        """
    )

# Parameter Levels by Location
elif options == "Parameter Levels by Location":
    st.header("Parameter Levels by Location")
    fig = px.box(data_water_quality, x='Location', y=['pH', 'Dissolved Oxygen', 'Nitrate', 'Phosphate', 'Temperature', 'Turbidity'], title='Parameter Levels by Location')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The box plot shows the distribution of various water quality parameters across different locations.
        - Certain locations might have higher variability or levels of specific parameters, indicating potential pollution sources.
        """,
        """
        - Investigate the reasons behind higher variability or levels of specific parameters at certain locations.
        - Implement location-specific measures to address and mitigate pollution sources.
        """
    )

# Parameter Levels by Season
elif options == "Parameter Levels by Season":
    st.header("Parameter Levels by Season")
    fig = px.box(data_water_quality, x='Season', y=['pH', 'Dissolved Oxygen', 'Nitrate', 'Phosphate', 'Temperature', 'Turbidity'], title='Parameter Levels by Season')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The box plot shows the distribution of various water quality parameters across different seasons.
        - Certain seasons might show higher levels or variability in specific parameters, indicating seasonal effects on water quality.
        """,
        """
        - Investigate the factors contributing to seasonal effects on water quality parameters.
        - Develop seasonal management strategies to maintain and improve water quality.
        """
    )

# Parameter Correlations
elif options == "Parameter Correlations":
    st.header("Parameter Correlations")
    numeric_data = data_water_quality.select_dtypes(include=[np.number])
    corr = numeric_data.corr()
    fig = px.imshow(corr, title='Correlation Matrix of Parameters')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The correlation matrix shows the relationships between different water quality parameters.
        - Strong correlations can highlight underlying patterns or interactions between parameters.
        """,
        """
        - Focus on correlated parameters for more detailed analysis.
        - Use correlation insights to inform strategies for improving water quality by addressing interconnected parameters.
        """
    )

# Heatmap of Parameter Levels
elif options == "Heatmap of Parameter Levels":
    st.header("Heatmap of Parameter Levels")
    data_water_quality['Month'] = data_water_quality['Date'].dt.month
    data_water_quality['Year'] = data_water_quality['Date'].dt.year
    heatmap_data = data_water_quality.pivot_table(index='Year', columns='Month', values='Dissolved Oxygen', aggfunc='mean')
    fig = px.imshow(heatmap_data, aspect='auto', title='Heatmap of Dissolved Oxygen Levels by Month and Year')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The heatmap shows the average dissolved oxygen levels across different months and years.
        - Certain months might consistently show higher or lower levels, indicating seasonal trends.
        """,
        """
        - Investigate the factors contributing to seasonal trends in dissolved oxygen levels.
        - Develop strategies to manage and improve dissolved oxygen levels based on seasonal patterns.
        """
    )

# Top Pollutants
elif options == "Top Pollutants":
    st.header("Top Pollutants")
    top_pollutants = data_water_quality[['Nitrate', 'Phosphate', 'Turbidity']].mean().reset_index()
    top_pollutants.columns = ['Pollutant', 'Average Level']
    fig = px.bar(top_pollutants, x='Pollutant', y='Average Level', title='Top Pollutants', color='Pollutant')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The bar chart shows the average levels of key pollutants.
        - Certain pollutants might have higher average levels, indicating areas for focused water quality management.
        """,
        """
        - Investigate the sources and impacts of key pollutants with higher average levels.
        - Implement targeted measures to reduce the levels of key pollutants and improve overall water quality.
        """
    )

# Parameter Distributions
elif options == "Parameter Distributions":
    st.header("Parameter Distributions")
    fig = px.histogram(data_water_quality, x=['pH', 'Dissolved Oxygen', 'Nitrate', 'Phosphate', 'Temperature', 'Turbidity'], title='Parameter Distributions', barmode='overlay')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The histogram shows the distribution of various water quality parameters.
        - Certain parameters might show wider distributions, indicating variability in water quality.
        """,
        """
        - Investigate the factors contributing to variability in specific water quality parameters.
        - Develop strategies to reduce variability and maintain consistent water quality levels.
        """
    )

# Word Cloud of Pollutants
elif options == "Word Cloud of Pollutants":
    st.header("Word Cloud of Pollutants")
    pollutants_counts = data_water_quality[['Nitrate', 'Phosphate', 'Turbidity']].apply(lambda x: x.value_counts().sum())
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(pollutants_counts.to_dict())
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)
    display_insights_and_recommendations(
        """
        - The word cloud visualizes the frequency of key pollutants.
        - Larger words indicate more common pollutants within the dataset.
        """,
        """
        - Use the word cloud to identify the most common pollutants at a glance.
        - Focus on developing strategies to address the most frequently occurring pollutants to improve overall water quality.
        """
    )

# Footer
#st.sidebar.markdown("---")
#st.sidebar.markdown("Developed by [Your Name]")
