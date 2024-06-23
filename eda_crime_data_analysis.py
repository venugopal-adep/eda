import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load the dataset
@st.cache_data
def load_data():
    data = pd.read_csv('Crimes_-_2001_to_Present1.csv')
    data['Date'] = pd.to_datetime(data['Date'])
    data['Year'] = data['Date'].dt.year
    data['Month'] = data['Date'].dt.month
    return data

data = load_data()

# Title of the application
st.title("Crime Data Analysis")

# Sidebar for navigation
visualization = st.sidebar.radio(
    "Select Visualization",
    ("Dataset Overview", "Missing Values", "Crime Types Distribution", "Arrests Distribution",
     "Crimes Over Time", "Crime Locations", "Geographic Distribution", "Common Crime Descriptions",
     "Seasonal Trends in Crime", "Crimes by Community Area")
)

# Slide 1: Data Overview
if visualization == "Dataset Overview":
    st.header("Overview of the Crime Dataset")
    st.write(data.head())
    st.markdown("""
    **Column Descriptions:**
    - **ID**: Unique identifier for the crime incident.
    - **Case Number**: The case number for the incident.
    - **Date**: The date and time when the incident occurred.
    - **Block**: The block address where the incident occurred.
    - **IUCR**: Illinois Uniform Crime Reporting code.
    - **Primary Type**: The primary description of the crime.
    - **Description**: A more detailed description of the crime.
    - **Location Description**: The location type where the incident occurred.
    - **Arrest**: Indicates whether an arrest was made.
    - **Domestic**: Indicates whether the incident was domestic-related.
    - **Beat**: The police beat where the incident occurred.
    - **District**: The police district where the incident occurred.
    - **Ward**: The ward where the incident occurred.
    - **Community Area**: The community area where the incident occurred.
    - **FBI Code**: The FBI code for the crime.
    - **X Coordinate**: The X coordinate of the incident location.
    - **Y Coordinate**: The Y coordinate of the incident location.
    - **Year**: The year when the incident occurred.
    - **Updated On**: The date and time when the record was last updated.
    - **Latitude**: The latitude of the incident location.
    - **Longitude**: The longitude of the incident location.
    - **Location**: The latitude and longitude coordinates as a tuple.
    """)

# Slide 2: Missing Values
elif visualization == "Missing Values":
    st.header("Missing Values in the Dataset")
    fig_missing_values = plt.figure(figsize=(12, 6))
    sns.heatmap(data.isnull(), cbar=False, cmap='viridis')
    st.pyplot(fig_missing_values)
    st.markdown("""
    **Insights:**
    - Missing values are present in columns like `Ward`, `Community Area`, `Latitude`, and `Longitude`.
    
    **Recommendations:**
    - Handle missing values through imputation or removal based on their significance.
    """)

# Slide 3: Crime Types Distribution
elif visualization == "Crime Types Distribution":
    st.header("Distribution of Primary Crime Types")
    crime_type_counts = data['Primary Type'].value_counts().head(10)
    fig_crime_types = px.bar(crime_type_counts, x=crime_type_counts.index, y=crime_type_counts.values, labels={'x': 'Crime Type', 'y': 'Count'}, title='Top 10 Primary Crime Types')
    st.plotly_chart(fig_crime_types)
    st.markdown("""
    **Insights:**
    - The most common crime types include `THEFT`, `BATTERY`, and `CRIMINAL DAMAGE`.
    
    **Recommendations:**
    - Focus on these common crime types for targeted interventions and resource allocation.
    """)

# Slide 4: Arrests Distribution
elif visualization == "Arrests Distribution":
    st.header("Distribution of Arrests")
    arrest_counts = data['Arrest'].value_counts()
    fig_arrests = px.pie(arrest_counts, values=arrest_counts.values, names=['Not Arrested', 'Arrested'], title='Arrests Distribution')
    st.plotly_chart(fig_arrests)
    st.markdown("""
    **Insights:**
    - A significant portion of crimes do not result in arrests.
    
    **Recommendations:**
    - Investigate factors influencing the low arrest rates and improve law enforcement strategies.
    """)

# Slide 5: Temporal Analysis
elif visualization == "Crimes Over Time":
    st.header("Crimes Over Time")
    yearly_crime_counts = data['Year'].value_counts().sort_index()
    fig_temporal = px.line(yearly_crime_counts, x=yearly_crime_counts.index, y=yearly_crime_counts.values, labels={'x': 'Year', 'y': 'Number of Crimes'}, title='Crimes Over Time')
    st.plotly_chart(fig_temporal)
    st.markdown("""
    **Insights:**
    - Variations in crime rates with certain peaks and troughs.
    
    **Recommendations:**
    - Analyze the factors contributing to these trends for better crime prevention strategies.
    """)

# Slide 6: Crime Locations
elif visualization == "Crime Locations":
    st.header("Top Locations of Crimes")
    location_counts = data['Location Description'].value_counts().head(10)
    fig_locations = px.bar(location_counts, x=location_counts.values, y=location_counts.index, labels={'x': 'Count', 'y': 'Location'}, orientation='h', title='Top 10 Crime Locations')
    st.plotly_chart(fig_locations)
    st.markdown("""
    **Insights:**
    - Common locations include `STREET`, `RESIDENCE`, and `APARTMENT`.
    
    **Recommendations:**
    - Increase surveillance and safety measures in these high-risk locations.
    """)

# Slide 7: Geographic Distribution
elif visualization == "Geographic Distribution":
    st.header("Geographic Distribution of Crimes")
    fig_geo = px.scatter(data, x='Longitude', y='Latitude', opacity=0.5, title='Geographic Distribution of Crimes')
    st.plotly_chart(fig_geo)
    st.markdown("""
    **Insights:**
    - Clusters of high crime density can be identified in certain areas.
    
    **Recommendations:**
    - Implement targeted patrolling and community programs in high-density areas.
    """)

# Slide 8: Crime Description Wordcloud
elif visualization == "Common Crime Descriptions":
    st.header("Common Crime Descriptions")
    text = ' '.join(data['Description'].dropna().tolist())
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    fig_wordcloud, ax = plt.subplots(figsize=(12, 6))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig_wordcloud)
    st.markdown("""
    **Insights:**
    - Common words include `BATTERY`, `THEFT`, and `CRIMINAL`.
    
    **Recommendations:**
    - Use these insights for focused awareness and prevention campaigns.
    """)

# Slide 9: Seasonal Analysis
elif visualization == "Seasonal Trends in Crime":
    st.header("Seasonal Trends in Crime")
    fig_seasonal = px.box(data, x='Month', y='Primary Type', title='Seasonal Trends in Crime')
    st.plotly_chart(fig_seasonal)
    st.markdown("""
    **Insights:**
    - Certain months show higher crime rates, indicating seasonal patterns.
    
    **Recommendations:**
    - Plan seasonal interventions and allocate resources accordingly.
    """)

# Slide 10: Community Area Analysis
elif visualization == "Crimes by Community Area":
    st.header("Crimes by Community Area")
    community_area_counts = data['Community Area'].value_counts().head(10)
    fig_community_area = px.bar(community_area_counts, x=community_area_counts.values, y=community_area_counts.index, labels={'x': 'Count', 'y': 'Community Area'}, orientation='h', title='Top 10 Community Areas with Most Crimes')
    st.plotly_chart(fig_community_area)
    st.markdown("""
    **Insights:**
    - Certain community areas are more prone to crimes.
    
    **Recommendations:**
    - Enhance community policing and social programs in high-crime areas.
    """)

# Conclusion
st.header("Conclusion")
st.markdown("""
- The dataset reveals significant patterns in crime types, locations, and temporal trends.
- Geographic and seasonal analyses provide crucial information for targeted interventions.

**Recommendations:**
- Improve data collection to reduce missing values.
- Implement focused law enforcement strategies in high-risk areas.
- Utilize seasonal trends for planning crime prevention initiatives.
- Enhance community engagement and policing in high-density crime areas.
""")
