import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'Provisional_COVID-19_death_counts__rates__and_percent_of_total_deaths__by_jurisdiction_of_residence.csv'
data = pd.read_csv(file_path)

# Title of the app
st.title('Exploratory Data Analysis on Provisional COVID-19 Death Counts')

# Sidebar for navigation
st.sidebar.title('Navigation')
options = st.sidebar.radio('Select a step for EDA:', 
                           ['Dataset Overview', 'Summary Statistics', 'COVID-19 Deaths Over Time', 
                            'Distribution of COVID-19 Death Rates', 'COVID-19 Deaths Percentage of Total Deaths', 
                            'Weekly Percentage Change in COVID-19 Deaths', 'Word Cloud of Footnotes'])

# Dataset Overview
if options == 'Dataset Overview':
    st.header('Dataset Overview')
    st.write('### Raw Dataset')
    st.write(data)
    
    st.write('### Explanation of Fields')
    st.markdown('''
    - **data_as_of:** Date of data collection.
    - **Jurisdiction_Residence:** Jurisdiction of residence.
    - **Group:** Group category.
    - **data_period_start:** Start date of the data period.
    - **data_period_end:** End date of the data period.
    - **COVID_deaths:** Number of COVID-19 deaths.
    - **COVID_pct_of_total:** Percentage of total deaths due to COVID-19.
    - **pct_change_wk:** Weekly percentage change in COVID-19 deaths.
    - **pct_diff_wk:** Weekly percentage difference in COVID-19 deaths.
    - **crude_COVID_rate:** Crude COVID-19 death rate.
    - **aa_COVID_rate:** Age-adjusted COVID-19 death rate.
    - **crude_COVID_rate_ann:** Annualized crude COVID-19 death rate.
    - **aa_COVID_rate_ann:** Annualized age-adjusted COVID-19 death rate.
    - **footnote:** Additional notes.
    ''')

# Summary Statistics
if options == 'Summary Statistics':
    st.header('Summary Statistics')
    st.write('### Statistical Overview')
    st.write(data.describe())

# COVID-19 Deaths Over Time
if options == 'COVID-19 Deaths Over Time':
    st.header('COVID-19 Deaths Over Time by Jurisdiction')
    
    # Filter data for visualization
    data_filtered = data.groupby(['data_period_start', 'Jurisdiction_Residence'])['COVID_deaths'].sum().reset_index()

    # Plotting
    fig = px.line(data_filtered, x='data_period_start', y='COVID_deaths', color='Jurisdiction_Residence', 
                  title='COVID-19 Deaths Over Time by Jurisdiction')
    st.plotly_chart(fig)
    
    st.write('### Insights:')
    st.write('- The plot shows the trend of COVID-19 deaths over time for different jurisdictions.')
    st.write('- Significant peaks indicate surges in deaths, aligning with known waves of the pandemic.')
    
    st.write('### Recommendation:')
    st.write('- Focus on analyzing the time periods with spikes in deaths for further investigation into possible causes and mitigating factors.')

# Distribution of COVID-19 Death Rates
if options == 'Distribution of COVID-19 Death Rates':
    st.header('Distribution of COVID-19 Death Rates')
    
    # Plotting distribution of COVID-19 death rates
    fig = px.histogram(data, x='crude_COVID_rate', nbins=30, title='Distribution of Crude COVID-19 Death Rates', 
                       marginal='box', hover_data=data.columns)
    st.plotly_chart(fig)
    
    st.write('### Insights:')
    st.write('- The histogram shows the distribution of crude COVID-19 death rates.')
    st.write('- Most jurisdictions have a low death rate, with a few outliers having higher rates.')
    
    st.write('### Recommendation:')
    st.write('- Investigate jurisdictions with higher death rates to identify underlying factors and implement targeted interventions.')

# COVID-19 Deaths Percentage of Total Deaths by Jurisdiction
if options == 'COVID-19 Deaths Percentage of Total Deaths':
    st.header('Average COVID-19 Deaths as Percentage of Total Deaths by Jurisdiction')
    
    # Filter data for visualization
    data_filtered_pct = data.groupby('Jurisdiction_Residence')['COVID_pct_of_total'].mean().reset_index()

    # Plotting
    fig = px.bar(data_filtered_pct, x='Jurisdiction_Residence', y='COVID_pct_of_total', 
                 title='Average COVID-19 Deaths as Percentage of Total Deaths by Jurisdiction')
    st.plotly_chart(fig)
    
    st.write('### Insights:')
    st.write('- The bar plot shows the average percentage of total deaths attributed to COVID-19 for each jurisdiction.')
    st.write('- Significant variation exists between jurisdictions, indicating diverse impacts of the pandemic.')
    
    st.write('### Recommendation:')
    st.write('- Jurisdictions with higher percentages should be prioritized for resource allocation and support.')

# Weekly Percentage Change in COVID-19 Deaths
if options == 'Weekly Percentage Change in COVID-19 Deaths':
    st.header('Weekly Percentage Change in COVID-19 Deaths')
    
    # Plotting weekly percentage change
    fig = px.line(data, x='data_period_start', y='pct_change_wk', title='Weekly Percentage Change in COVID-19 Deaths')
    st.plotly_chart(fig)
    
    st.write('### Insights:')
    st.write('- The line plot shows the weekly percentage change in COVID-19 deaths over time.')
    st.write('- Peaks indicate periods of rapid changes, useful for identifying critical moments in the pandemic.')
    
    st.write('### Recommendation:')
    st.write('- Analyze periods with drastic changes to understand factors contributing to these shifts and prepare for future similar events.')

# Word Cloud of Footnotes
if options == 'Word Cloud of Footnotes':
    st.header('Word Cloud of Footnotes')
    
    # Combine all footnotes
    text = ' '.join(data['footnote'].dropna().astype(str).tolist())

    # Generate word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud of Footnotes')
    st.pyplot(plt)
    
    st.write('### Insights:')
    st.write('- The word cloud visualizes the most frequent words in the footnotes, providing a qualitative overview of the notes\' content.')
    
    st.write('### Recommendation:')
    st.write('- Review frequently mentioned terms in the footnotes for additional context or potential data adjustments.')
