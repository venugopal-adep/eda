import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
@st.cache_data
def load_data():
    data = pd.read_csv('prevalence-of-undernourishment new.csv')
    data['percentage'] = data['percentage'].str.replace(',', '.').str.rstrip('%').astype(float, errors='ignore')
    data = data[~data['percentage'].str.contains('#VALUE!', na=False)]
    data['percentage'] = data['percentage'].astype(float)
    return data

data = load_data()

# Title
st.title('Exploratory Data Analysis: Prevalence of Undernourishment')

# Sidebar for visualization options
st.sidebar.header('Visualization Options')
show_dataset = st.sidebar.checkbox('Show Dataset', value=False)
show_field_explanation = st.sidebar.checkbox('Field explanation', value=False)
show_descriptive_stats = st.sidebar.checkbox('Show Descriptive Statistics', value=False)
show_global_trends = st.sidebar.checkbox('Global Trends', value=False)
show_regional_trends = st.sidebar.checkbox('Regional Trends', value=False)
show_distribution = st.sidebar.checkbox('Distribution', value=False)
show_top_undernourished_countries = st.sidebar.checkbox('Top 10 Undernourished Countries', value=False)
show_conclusion = st.sidebar.checkbox('Show Conclusion', value=False)

# Show dataset
if show_dataset:
    st.subheader('Dataset')
    st.write(data)



# Explanation of fields
if show_field_explanation:
    st.subheader('Field Explanation')
    st.markdown('''
    - **Entity**: The name of the country or region.
    - **Year**: The year of the data point.
    - **2.1.1 Prevalence of undernourishment**: The percentage of the population that is undernourished.
    - **Percentage**: The same as above, formatted as a percentage string.
    ''')

# Show descriptive statistics
if show_descriptive_stats:
    st.subheader('Descriptive Statistics')
    st.write(data.describe())

# Global Trends
if show_global_trends:
    st.header('Global Trends in Prevalence of Undernourishment (2000-2022)')
    global_trends = data.groupby('Year')['2.1.1 Prevalence of undernourishment'].mean().reset_index()
    fig_global_trends = px.line(global_trends, x='Year', y='2.1.1 Prevalence of undernourishment', title='Global Trends in Prevalence of Undernourishment')
    st.plotly_chart(fig_global_trends)
    st.markdown('**Insights:** The global prevalence of undernourishment has shown a decreasing trend over the years.')
    st.markdown('**Recommendations:** Continue monitoring and implementing global initiatives to reduce undernourishment.')

# Regional Trends
if show_regional_trends:
    st.header('Regional Trends in Prevalence of Undernourishment (2000-2022)')
    fig_regional_trends = px.line(data, x='Year', y='2.1.1 Prevalence of undernourishment', color='Entity', title='Regional Trends in Prevalence of Undernourishment')
    st.plotly_chart(fig_regional_trends)
    st.markdown('**Insights:** Different regions exhibit varying trends in undernourishment, with some regions showing significant improvements while others lag behind.')
    st.markdown('**Recommendations:** Tailor interventions to the specific needs of each region to effectively combat undernourishment.')

# Distribution of Prevalence of Undernourishment
if show_distribution:
    st.header('Distribution of Prevalence of Undernourishment')
    fig_distribution = px.histogram(data, x='2.1.1 Prevalence of undernourishment', nbins=50, title='Distribution of Prevalence of Undernourishment')
    fig_distribution.update_layout(bargap=0.1)
    st.plotly_chart(fig_distribution)
    st.markdown('**Insights:** The distribution shows a right skew, indicating that while many countries have low undernourishment rates, a few have very high rates.')
    st.markdown('**Recommendations:** Focus efforts on countries with the highest rates to address extreme undernourishment.')

# Top 10 Countries with Highest Prevalence of Undernourishment
if show_top_undernourished_countries:
    st.header('Top 10 Countries with Highest Prevalence of Undernourishment')
    top_countries = data.groupby('Entity')['2.1.1 Prevalence of undernourishment'].mean().nlargest(10).index
    top_data = data[data['Entity'].isin(top_countries)]
    fig_top_countries = px.box(top_data, x='Entity', y='2.1.1 Prevalence of undernourishment', title='Top 10 Countries with Highest Prevalence of Undernourishment')
    fig_top_countries.update_layout(xaxis={'categoryorder':'total descending'})
    st.plotly_chart(fig_top_countries)
    st.markdown('**Insights:** The top 10 countries with the highest prevalence of undernourishment show a wide range of values, with some countries having extremely high rates.')
    st.markdown('**Recommendations:** Prioritize aid and resources to these countries to make the most significant impact on reducing global undernourishment.')

# Conclusion
if show_conclusion:
    st.header('Conclusion')
    st.markdown('''
    The exploratory data analysis of the prevalence of undernourishment has highlighted several key trends and insights. The global trend indicates a decrease in undernourishment over the years, although regional disparities remain significant. Specific countries continue to experience high levels of undernourishment, necessitating targeted interventions and resource allocation.

    **Recommendations:**
    - Continue global monitoring and initiatives to reduce undernourishment.
    - Tailor interventions to the specific needs of each region.
    - Focus efforts on countries with the highest rates of undernourishment to address extreme cases.

    By implementing these recommendations, we can make significant strides towards reducing undernourishment and improving global food security.
    ''')

#st.sidebar.markdown('----')
#st.sidebar.markdown('Created by [Your Name]')
