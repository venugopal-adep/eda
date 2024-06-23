import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np

# Placeholder for loading the dataset
file_path_youth_tobacco = 'Youth_Tobacco_Survey__YTS__Data.csv'

# Load the dataset
# data_youth_tobacco = pd.read_csv(file_path_youth_tobacco)

# For demonstration purposes, create a sample dataframe
data_youth_tobacco = pd.DataFrame({
    'Year': np.random.choice(range(2000, 2021), 100),
    'Age Group': np.random.choice(['12-14', '15-17', '18-20'], 100),
    'Gender': np.random.choice(['Male', 'Female'], 100),
    'Race/Ethnicity': np.random.choice(['White', 'Black', 'Hispanic', 'Asian', 'Other'], 100),
    'State': np.random.choice(['CA', 'TX', 'NY', 'FL', 'PA'], 100),
    'Tobacco Product': np.random.choice(['Cigarettes', 'E-cigarettes', 'Cigars', 'Hookah', 'Smokeless Tobacco'], 100),
    'Usage Rate': np.random.uniform(5, 50, 100)
})

# Function to display insights and recommendations
def display_insights_and_recommendations(insights, recommendations):
    st.markdown("### Insights")
    st.write(insights)
    st.markdown("### Recommendations")
    st.write(recommendations)

# App title
st.title("Youth Tobacco Survey Analysis")

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Select a visualization:", [
    "Overview", "Tobacco Use Trends Over Time", "Tobacco Use by Age Group", "Tobacco Use by Gender", "Tobacco Use by Race/Ethnicity",
    "Tobacco Use by State", "Correlation Analysis", "Heatmap of Tobacco Use by Month and Year", "Top Tobacco Products Used", "Word Cloud of Tobacco Products"])

# Overview of the dataset
if options == "Overview":
    st.header("Overview of the Dataset")
    st.dataframe(data_youth_tobacco.head())
    display_insights_and_recommendations(
        """
        - The dataset includes information on tobacco use trends, categorized by year, age group, gender, race/ethnicity, state, and tobacco product.
        - It provides a comprehensive view of youth tobacco use patterns and trends over time and across different demographic groups.
        """,
        """
        - Familiarize yourself with the dataset structure to understand the variables available for deeper analysis.
        - Use this overview to identify potential areas of interest for further exploration.
        """
    )

# Tobacco Use Trends Over Time
elif options == "Tobacco Use Trends Over Time":
    st.header("Tobacco Use Trends Over Time")
    fig = px.bar(data_youth_tobacco, x='Year', y='Usage Rate', color='Tobacco Product', title='Tobacco Use Trends Over Time')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The line chart shows the usage rates of different tobacco products over the years.
        - There might be an increasing trend in the use of certain products, indicating changing preferences among youth.
        """,
        """
        - Investigate the factors contributing to the rising use of specific tobacco products over the years.
        - Develop and promote public health initiatives to address the increasing trend in tobacco use among youth.
        """
    )

# Tobacco Use by Age Group
elif options == "Tobacco Use by Age Group":
    st.header("Tobacco Use by Age Group")
    fig = px.bar(data_youth_tobacco, x='Age Group', y='Usage Rate', color='Tobacco Product', title='Tobacco Use by Age Group', barmode='group')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The bar chart shows the distribution of tobacco use across different age groups.
        - Certain age groups might have higher usage rates, indicating targeted areas for intervention.
        """,
        """
        - Investigate the lifestyle and social factors contributing to higher tobacco use in specific age groups.
        - Develop age-specific health and education programs to reduce tobacco use among youth.
        """
    )

# Tobacco Use by Gender
elif options == "Tobacco Use by Gender":
    st.header("Tobacco Use by Gender")
    fig = px.histogram(data_youth_tobacco, x='Gender', y='Usage Rate', color='Tobacco Product', barmode='group', title='Tobacco Use by Gender')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The histogram shows the distribution of tobacco use between males and females.
        - There might be gender differences in usage rates, indicating a need for gender-specific interventions.
        """,
        """
        - Investigate the reasons behind gender disparities in tobacco use rates.
        - Develop gender-specific strategies to address the underlying causes of tobacco use among youth.
        """
    )

# Tobacco Use by Race/Ethnicity
elif options == "Tobacco Use by Race/Ethnicity":
    st.header("Tobacco Use by Race/Ethnicity")
    fig = px.bar(data_youth_tobacco, x='Race/Ethnicity', y='Usage Rate', color='Tobacco Product', title='Tobacco Use by Race/Ethnicity', barmode='group')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The bar chart shows the distribution of tobacco use across different racial and ethnic groups.
        - Certain racial/ethnic groups might have higher usage rates, indicating areas for focused public health efforts.
        """,
        """
        - Investigate the cultural, socio-economic, and environmental factors contributing to tobacco use in specific racial/ethnic groups.
        - Develop culturally sensitive and community-based interventions to reduce tobacco use.
        """
    )

# Tobacco Use by State
elif options == "Tobacco Use by State":
    st.header("Tobacco Use by State")
    state_abbrev = {'CA': 'California', 'TX': 'Texas', 'NY': 'New York', 'FL': 'Florida', 'PA': 'Pennsylvania'}
    data_youth_tobacco['State Name'] = data_youth_tobacco['State'].map(state_abbrev)
    fig = px.choropleth(data_youth_tobacco, locations='State', locationmode='USA-states', color='Usage Rate', hover_name='State Name', title='Tobacco Use by State', scope='usa')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The choropleth map shows the geographical distribution of tobacco use rates across different states.
        - Certain states might have higher usage rates, indicating hotspots of tobacco use among youth.
        """,
        """
        - Analyze the geographical distribution to identify hotspots of tobacco use.
        - Implement targeted public health initiatives in high-risk states to reduce tobacco use among youth.
        """
    )

# Correlation Analysis
elif options == "Correlation Analysis":
    st.header("Correlation Analysis Between Variables")
    numeric_data = data_youth_tobacco.select_dtypes(include=[np.number])
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
        - Use correlation insights to inform strategies for reducing tobacco use among youth through targeted interventions.
        """
    )

# Heatmap of Tobacco Use by Month and Year
elif options == "Heatmap of Tobacco Use by Month and Year":
    st.header("Heatmap of Tobacco Use by Month and Year")
    data_youth_tobacco['Month'] = pd.to_datetime(data_youth_tobacco['Year'], format='%Y').dt.month
    heatmap_data = data_youth_tobacco.pivot_table(index='Year', columns='Month', values='Usage Rate', aggfunc='mean')
    fig = px.imshow(heatmap_data, aspect='auto', title='Heatmap of Tobacco Use by Month and Year')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The heatmap shows the distribution of tobacco use rates across different months and years.
        - Certain months might consistently show higher usage rates, indicating seasonal trends.
        """,
        """
        - Investigate the factors contributing to seasonal trends in tobacco use.
        - Develop promotional campaigns and educational programs to align with seasonal usage patterns.
        """
    )

# Top Tobacco Products Used
# Top Tobacco Products Used
elif options == "Top Tobacco Products Used":
    st.header("Top Tobacco Products Used")
    top_products = data_youth_tobacco.groupby('Tobacco Product')['Usage Rate'].mean().reset_index().sort_values(by='Usage Rate', ascending=False)
    fig = px.bar(top_products, x='Tobacco Product', y='Usage Rate', title='Top Tobacco Products Used', color='Tobacco Product')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The bar chart shows the average usage rates of different tobacco products.
        - Certain products might be more popular among youth, indicating changing preferences and trends.
        """,
        """
        - Investigate the reasons behind the popularity of certain tobacco products.
        - Focus on developing targeted interventions and educational campaigns for the most commonly used products to reduce overall tobacco use.
        """
    )

# Word Cloud of Tobacco Products
elif options == "Word Cloud of Tobacco Products":
    st.header("Word Cloud of Tobacco Products")
    product_counts = data_youth_tobacco['Tobacco Product'].value_counts().to_dict()
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(product_counts)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)
    display_insights_and_recommendations(
        """
        - The word cloud visualizes the frequency of different tobacco products.
        - Larger words indicate more common tobacco products within the dataset.
        """,
        """
        - Use the word cloud to identify the most common tobacco products at a glance.
        - Focus on developing strategies to address the most frequently used tobacco products among youth.
        """
    )

# Footer
#st.sidebar.markdown("---")
#st.sidebar.markdown("Developed by [Your Name]")

