import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('Listing_of_Active_Businesses1.csv')

# Data preprocessing
data['LOCATION START DATE'] = pd.to_datetime(data['LOCATION START DATE'], errors='coerce')
data[['LAT', 'LON']] = data['LOCATION'].str.extract(r'\((.*), (.*)\)')
data['LAT'] = pd.to_numeric(data['LAT'], errors='coerce')
data['LON'] = pd.to_numeric(data['LON'], errors='coerce')

st.title('Active Businesses Analysis')
st.write("""
         Listing of Active Businesses
Metadata Updated: June 15, 2024

Listing of all active businesses currently registered with the Office of Finance. An "active" business is defined as a registered business whose owner has not notified the Office of Finance of a cease of business operations. Update Interval: Monthly.

NAICS Codes are from 2007 NAICS: https://www.census.gov/cgi-bin/sssd/naics/naicsrch?chart=2007
         """)

# Sidebar for navigation
visualization = st.sidebar.radio("Choose a visualization", [
    "Dataset Overview", 
    "Summary Statistics", 
    "Business Distribution by City", 
    "NAICS Code Distribution", 
    "Business Distribution by Council District", 
    "Business Start Dates Analysis", 
    "Geographic Distribution of Businesses",
    "Word Cloud of Business Names"
])

if visualization == "Dataset Overview":
    st.header('Dataset Overview')
    st.write(data.head())
    st.write("""
        **Insights:**
        - This dataset provides detailed information about active businesses including business name, address, NAICS code, council district, and start dates.
        - There are missing values in some columns such as DBA Name, Mailing Address, and Mailing City.
        
        **Recommendations:**
        - Address missing values for a more comprehensive analysis.
        - Standardize date formats for ease of processing.
    """)

elif visualization == "Summary Statistics":
    st.header('Summary Statistics')
    summary_stats = data.describe(include='all').transpose()
    st.write(summary_stats)
    st.write("""
        **Insights:**
        - High variability in business names and street addresses.
        - Most businesses do not have a DBA (Doing Business As) name.
        
        **Recommendations:**
        - Investigate columns with high missing values to determine their impact on analysis.
    """)

elif visualization == "Business Distribution by City":
    st.header('Business Distribution by City')
    city_counts = data['CITY'].value_counts().head(10)
    fig_city = px.bar(city_counts, x=city_counts.index, y=city_counts.values, labels={'x': 'City', 'y': 'Number of Businesses'}, title='Top 10 Cities with Most Businesses')
    st.plotly_chart(fig_city)
    st.write("""
        **Insights:**
        - High concentration of businesses in major cities like Los Angeles, Van Nuys, and North Hollywood.
        - Diverse distribution across multiple smaller cities.
        
        **Recommendations:**
        - Focus on highly concentrated cities for targeted business support and development programs.
    """)

elif visualization == "NAICS Code Distribution":
    st.header('NAICS Code Distribution')
    naics_counts = data['PRIMARY NAICS DESCRIPTION'].value_counts().head(10)
    fig_naics = px.bar(naics_counts, x=naics_counts.index, y=naics_counts.values, labels={'x': 'NAICS Description', 'y': 'Number of Businesses'}, title='Top 10 NAICS Codes')
    st.plotly_chart(fig_naics)
    st.write("""
        **Insights:**
        - Diverse range of industries represented.
        - Top industries include couriers & messengers, personal care services, and nondurable goods.
        
        **Recommendations:**
        - Tailor economic policies to support the leading industries.
        - Encourage growth in underrepresented sectors.
    """)

elif visualization == "Business Distribution by Council District":
    st.header('Business Distribution by Council District')
    district_counts = data['COUNCIL DISTRICT'].value_counts().sort_index()
    fig_district = px.bar(district_counts, x=district_counts.index, y=district_counts.values, labels={'x': 'Council District', 'y': 'Number of Businesses'}, title='Business Distribution by Council District')
    st.plotly_chart(fig_district)
    st.write("""
        **Insights:**
        - Uneven distribution of businesses across council districts.
        - Districts 0 has the highest business density.
        
        **Recommendations:**
        - Evaluate resource allocation to ensure balanced economic development.
        - Strengthen support for districts with lower business activity.
    """)

elif visualization == "Business Start Dates Analysis":
    st.header('Business Start Dates Analysis')
    start_dates = data['LOCATION START DATE'].dt.year.value_counts().sort_index()
    fig_start_dates = px.line(start_dates, x=start_dates.index, y=start_dates.values, labels={'x': 'Year', 'y': 'Number of Businesses Started'}, title='Business Start Dates Over Years')
    st.plotly_chart(fig_start_dates)
    st.write("""
        **Insights:**
        - A surge in business registrations around 2019.
        - Consistent growth in new business formations over the years.
        
        **Recommendations:**
        - Analyze periods with high growth to identify successful policies.
        - Implement initiatives to sustain growth trends.
    """)

elif visualization == "Geographic Distribution of Businesses":
    st.header('Geographic Distribution of Businesses')
    fig_geo = px.scatter_mapbox(data, lat='LAT', lon='LON', hover_name='BUSINESS NAME', hover_data=['CITY', 'ZIP CODE'],
                                color_discrete_sequence=['fuchsia'], zoom=1, height=500)
    fig_geo.update_layout(mapbox_style="open-street-map")
    fig_geo.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig_geo)
    st.write("""
        **Insights:**
        - Businesses spread across various geographical coordinates.
        - Clustering of businesses in urban areas.
        
        **Recommendations:**
        - Develop infrastructure to support business operations in clustered areas.
        - Promote business opportunities in less dense regions.
    """)

elif visualization == "Word Cloud of Business Names":
    st.header('Word Cloud of Business Names')
    business_names = ' '.join(data['BUSINESS NAME'].dropna())
    wordcloud = WordCloud(background_color='white', max_words=100, contour_color='steelblue').generate(business_names)
    
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)
    st.write("""
        **Insights:**
        - The word cloud visualization highlights the most common words in business names.
        
        **Recommendations:**
        - Use common keywords for marketing and promotional activities to attract more businesses.
    """)
