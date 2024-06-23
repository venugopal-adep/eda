import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np

# Placeholder for loading the dataset
file_path_meteorite_landings = 'Meteorite_Landings.csv'

# Load the dataset
# data_meteorite_landings = pd.read_csv(file_path_meteorite_landings)

# For demonstration purposes, create a sample dataframe
data_meteorite_landings = pd.DataFrame({
    'name': ['Aachen', 'Aarhus', 'Abee', 'Acapulco', 'Achiras'],
    'id': [1, 2, 6, 10, 370],
    'nametype': ['Valid', 'Valid', 'Valid', 'Valid', 'Valid'],
    'recclass': ['L5', 'H6', 'EH4', 'Acapulcoite', 'L6'],
    'mass (g)': [21, 720, 107000, 1914, 780],
    'fall': ['Fell', 'Fell', 'Fell', 'Fell', 'Fell'],
    'year': [1880, 1951, 1952, 1976, 1902],
    'reclat': [50.775, 56.18333, 54.21667, 16.88333, -31.6],
    'reclong': [6.08333, 10.23333, -113, -99.9, -65.23333],
    'GeoLocation': ['(50.775, 6.08333)', '(56.18333, 10.23333)', '(54.21667, -113)', '(16.88333, -99.9)', '(-31.6, -65.23333)']
})

# Function to display insights and recommendations
def display_insights_and_recommendations(insights, recommendations):
    st.markdown("### Insights")
    st.write(insights)
    st.markdown("### Recommendations")
    st.write(recommendations)

# App title
st.title("Meteorite Landings Analysis")
st.write("""
         Meteorite Landings
Metadata Updated: December 6, 2023

This comprehensive data set from The Meteoritical Society contains information on all of the known meteorite landings. The Fusion Table is collected by Javier de la Torre and we've also provided an XLS file that consists of 34,513 meteorites and includes the following fields: place type_of_meteorite mass_g fell_found year database coordinate_1 coordinates_2 cartodb_id created_at updated_at year_date longitude latitude geojson

**5/14/13 Please find an updated data set from The Meteoritical Society that includes more recent meteorites. Under NameType, 'valid' is for most meteorites and 'relict' are for objects that were once meteorites but are now highly altered by weathering on Earth.
         """)

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Select a visualization:", ["Overview", "Meteorite Landings Over Time", "Meteorite Landings by Mass", "Meteorite Landings by Class", "Geographical Distribution", "Correlation Analysis", "Word Cloud of Meteorite Names"])

# Overview of the dataset
if options == "Overview":
    st.header("Overview of the Dataset")
    st.dataframe(data_meteorite_landings.head())
    display_insights_and_recommendations(
        """
        - The dataset includes information on meteorite landings such as name, class, mass, year, and location.
        - It provides a comprehensive view of meteorite landings over time and geography.
        """,
        """
        - Familiarize yourself with the dataset structure to understand the variables available for deeper analysis.
        - Use this overview to identify potential areas of interest for further exploration.
        """
    )

# Meteorite Landings Over Time
elif options == "Meteorite Landings Over Time":
    st.header("Meteorite Landings Over Time")
    fig = px.histogram(data_meteorite_landings, x='year', title='Meteorite Landings Over Time')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The histogram shows the frequency of meteorite landings over different years.
        - Peaks in certain years might indicate higher meteorite activity or better documentation.
        """,
        """
        - Investigate the reasons behind peaks in meteorite landings for certain years.
        - Consider the historical context and advancements in meteorite detection and documentation.
        """
    )

# Meteorite Landings by Mass
elif options == "Meteorite Landings by Mass":
    st.header("Meteorite Landings by Mass")
    fig = px.scatter(data_meteorite_landings, x='year', y='mass (g)', size='mass (g)', color='recclass', title='Meteorite Landings by Mass')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The scatter plot shows the distribution of meteorite masses over different years.
        - Larger meteorites are represented by bigger points on the plot.
        """,
        """
        - Analyze the distribution to understand the occurrence of larger meteorites over time.
        - Explore any patterns or anomalies in the distribution of meteorite masses.
        """
    )

# Meteorite Landings by Class
elif options == "Meteorite Landings by Class":
    st.header("Meteorite Landings by Class")
    fig = px.bar(data_meteorite_landings, x='recclass', y='mass (g)', title='Meteorite Landings by Class')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The bar chart shows the total mass of meteorites for each class.
        - Different classes of meteorites may have different characteristics and origins.
        """,
        """
        - Investigate the characteristics and origins of different meteorite classes.
        - Use this information to inform further research on meteorite classification and composition.
        """
    )

# Geographical Distribution of Meteorite Landings
elif options == "Geographical Distribution":
    st.header("Geographical Distribution of Meteorite Landings")
    fig = px.scatter_geo(data_meteorite_landings, lat='reclat', lon='reclong', hover_name='name', size='mass (g)', title='Geographical Distribution of Meteorite Landings')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The scatter geo plot shows the geographical distribution of meteorite landings around the world.
        - Larger meteorites are represented by bigger points on the map.
        """,
        """
        - Analyze the geographical distribution to identify patterns in meteorite landings.
        - Consider the impact of geography on the detection and documentation of meteorites.
        """
    )

# Correlation Analysis
elif options == "Correlation Analysis":
    st.header("Correlation Analysis Between Variables")
    numeric_data = data_meteorite_landings.select_dtypes(include=[np.number])
    corr = numeric_data.corr()
    fig = px.imshow(corr, title='Correlation Matrix of Variables')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - Certain variables show strong correlations with each other.
        - For example, the correlation between meteorite mass and year can highlight trends over time.
        """,
        """
        - Focus on correlated variables for more detailed analysis.
        - Use correlation insights to understand the relationships between different aspects of meteorite data.
        """
    )

# Word Cloud of Meteorite Names
elif options == "Word Cloud of Meteorite Names":
    st.header("Word Cloud of Meteorite Names")
    meteorite_name_counts = data_meteorite_landings['name'].value_counts().to_dict()
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(meteorite_name_counts)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)
    display_insights_and_recommendations(
        """
        - The word cloud visualizes the frequency of different meteorite names.
        - Larger words indicate more common meteorite names within the dataset.
        """,
        """
        - Use the word cloud to identify the most common meteorite names at a glance.
        - This can inform naming conventions and highlight popular meteorite names.
        """
    )

# Footer
#st.sidebar.markdown("---")
#st.sidebar.markdown("Developed by [Your Name]")
