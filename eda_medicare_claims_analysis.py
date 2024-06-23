import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np

# Placeholder for loading the dataset
file_path_medicare_claims = 'Center_for_Medicare___Medicaid_Services__CMS____Medicare_Claims_data.csv'

# Load the dataset
# data_medicare_claims = pd.read_csv(file_path_medicare_claims)

# For demonstration purposes, create a sample dataframe
data_medicare_claims = pd.DataFrame({
    'Date': pd.date_range(start='2020-01-01', periods=100, freq='M'),
    'Provider Type': np.random.choice(['Hospital', 'Physician', 'Pharmacy', 'Nursing Facility'], 100),
    'State': np.random.choice(['CA', 'TX', 'NY', 'FL', 'PA'], 100),
    'Gender': np.random.choice(['Male', 'Female'], 100),
    'Age Group': np.random.choice(['<65', '65-74', '75-84', '85+'], 100),
    'Diagnosis': np.random.choice(['Diabetes', 'Hypertension', 'Heart Disease', 'Cancer', 'Arthritis'], 100),
    'Procedure': np.random.choice(['Surgery', 'Medication', 'Therapy', 'Diagnostic Test'], 100),
    'Claim Amount': np.random.uniform(1000, 10000, 100)
})

# Function to display insights and recommendations
def display_insights_and_recommendations(insights, recommendations):
    st.markdown("### Insights")
    st.write(insights)
    st.markdown("### Recommendations")
    st.write(recommendations)

# App title
st.title("Medicare Claims Analysis")

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Select a visualization:", [
    "Overview", "Claims Trends Over Time", "Claims by Provider Type", "Claims by State", "Claims by Gender",
    "Claims by Age Group", "Top Diagnoses and Procedures", "Cost Analysis", "Correlation Analysis",
    "Heatmap of Claims by Month and Year", "Word Cloud of Diagnoses and Procedures"])

# Overview of the dataset
if options == "Overview":
    st.header("Overview of the Dataset")
    st.dataframe(data_medicare_claims.head())
    display_insights_and_recommendations(
        """
        - The dataset includes information on Medicare claims categorized by date, provider type, state, gender, age group, diagnosis, procedure, and claim amount.
        - It provides a comprehensive view of Medicare claims trends and patterns over time and across different demographic groups.
        """,
        """
        - Familiarize yourself with the dataset structure to understand the variables available for deeper analysis.
        - Use this overview to identify potential areas of interest for further exploration.
        """
    )

# Claims Trends Over Time
elif options == "Claims Trends Over Time":
    st.header("Claims Trends Over Time")
    fig = px.line(data_medicare_claims, x='Date', y='Claim Amount', title='Claims Trends Over Time')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The line chart shows the total claim amounts over time.
        - There might be trends or seasonal patterns indicating peak periods for claims.
        """,
        """
        - Investigate the factors contributing to peak claim periods.
        - Develop strategies to manage resource allocation during high claim periods.
        """
    )

# Claims by Provider Type
elif options == "Claims by Provider Type":
    st.header("Claims by Provider Type")
    fig = px.bar(data_medicare_claims, x='Provider Type', y='Claim Amount', title='Claims by Provider Type', color='Provider Type')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The bar chart shows the distribution of claim amounts across different provider types.
        - Certain provider types might have higher claim amounts, indicating higher utilization or cost.
        """,
        """
        - Investigate the reasons behind higher claim amounts for specific provider types.
        - Focus on optimizing resource allocation and cost management for high-utilization provider types.
        """
    )

# Claims by State
elif options == "Claims by State":
    st.header("Claims by State")
    state_abbrev = {'CA': 'California', 'TX': 'Texas', 'NY': 'New York', 'FL': 'Florida', 'PA': 'Pennsylvania'}
    data_medicare_claims['State Name'] = data_medicare_claims['State'].map(state_abbrev)
    fig = px.choropleth(data_medicare_claims, locations='State', locationmode='USA-states', color='Claim Amount', hover_name='State Name', title='Claims by State', scope='usa')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The choropleth map shows the geographical distribution of claim amounts across different states.
        - Certain states might have higher claim amounts, indicating regional differences in healthcare utilization or costs.
        """,
        """
        - Analyze the geographical distribution to identify regional trends in Medicare claims.
        - Implement targeted healthcare policies and programs to address regional disparities in claims and costs.
        """
    )

# Claims by Gender
elif options == "Claims by Gender":
    st.header("Claims by Gender")
    fig = px.histogram(data_medicare_claims, x='Gender', y='Claim Amount', color='Gender', barmode='group', title='Claims by Gender')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The histogram shows the distribution of claim amounts between males and females.
        - There might be gender differences in claim amounts, indicating different healthcare utilization patterns.
        """,
        """
        - Investigate the reasons behind gender disparities in claim amounts.
        - Develop gender-specific healthcare programs to address the underlying causes of different utilization patterns.
        """
    )

# Claims by Age Group
elif options == "Claims by Age Group":
    st.header("Claims by Age Group")
    fig = px.bar(data_medicare_claims, x='Age Group', y='Claim Amount', title='Claims by Age Group', color='Age Group', barmode='group')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The bar chart shows the distribution of claim amounts across different age groups.
        - Certain age groups might have higher claim amounts, indicating higher healthcare utilization or costs.
        """,
        """
        - Investigate the lifestyle, health conditions, and other factors contributing to higher claim amounts in specific age groups.
        - Develop age-specific healthcare programs to manage and reduce high healthcare costs.
        """
    )

# Top Diagnoses and Procedures
elif options == "Top Diagnoses and Procedures":
    st.header("Top Diagnoses and Procedures")
    top_diagnoses = data_medicare_claims['Diagnosis'].value_counts().reset_index().head(10)
    top_diagnoses.columns = ['Diagnosis', 'Count']
    fig = px.bar(top_diagnoses, x='Diagnosis', y='Count', title='Top Diagnoses', color='Diagnosis')
    st.plotly_chart(fig)

    top_procedures = data_medicare_claims['Procedure'].value_counts().reset_index().head(10)
    top_procedures.columns = ['Procedure', 'Count']
    fig = px.bar(top_procedures, x='Procedure', y='Count', title='Top Procedures', color='Procedure')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The bar charts show the most common diagnoses and procedures.
        - Certain diagnoses and procedures might be more prevalent, indicating common health issues and treatments.
        """,
        """
        - Investigate the underlying causes of common diagnoses and the effectiveness of prevalent procedures.
        - Develop targeted health programs to address the most common health issues and improve treatment outcomes.
        """
    )

# Cost Analysis
elif options == "Cost Analysis":
    st.header("Cost Analysis")
    fig = px.box(data_medicare_claims, y='Claim Amount', title='Cost Distribution of Claims')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The box plot shows the distribution of claim amounts.
        - There might be significant variability in claim costs, indicating differences in treatment complexity and healthcare utilization.
        """,
        """
        - Investigate the factors contributing to high variability in claim costs.
        - Develop cost management strategies to reduce high healthcare costs and improve efficiency.
        """
    )

# Correlation Analysis
elif options == "Correlation Analysis":
    st.header("Correlation Analysis Between Variables")
    numeric_data = data_medicare_claims.select_dtypes(include=[np.number])
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
        - Use correlation insights to inform strategies for improving healthcare outcomes and managing costs.
        """
    )

# Heatmap of Claims by Month and Year
elif options == "Heatmap of Claims by Month and Year":
    st.header("Heatmap of Claims by Month and Year")
    data_medicare_claims['Month'] = data_medicare_claims['Date'].dt.month
    data_medicare_claims['Year'] = data_medicare_claims['Date'].dt.year
    heatmap_data = data_medicare_claims.pivot_table(index='Year', columns='Month', values='Claim Amount', aggfunc='sum')
    fig = px.imshow(heatmap_data, aspect='auto', title='Heatmap of Claims by Month and Year')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The heatmap shows the distribution of claim amounts across different months and years.
        - Certain months might consistently show higher claim amounts, indicating seasonal trends in healthcare utilization.
        """,
        """
        - Investigate the factors contributing to seasonal trends in healthcare claims.
        - Develop resource allocation and management strategies to handle seasonal variations in healthcare demand.
        """
    )

# Word Cloud of Diagnoses and Procedures
elif options == "Word Cloud of Diagnoses and Procedures":
    st.header("Word Cloud of Diagnoses and Procedures")
    diagnoses_counts = data_medicare_claims['Diagnosis'].value_counts().to_dict()
    procedures_counts = data_medicare_claims['Procedure'].value_counts().to_dict()
    
    st.subheader("Word Cloud of Diagnoses")
    wordcloud_diagnoses = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(diagnoses_counts)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud_diagnoses, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)

    st.subheader("Word Cloud of Procedures")
    wordcloud_procedures = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(procedures_counts)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud_procedures, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)
    
    display_insights_and_recommendations(
        """
        - The word clouds visualize the frequency of different diagnoses and procedures.
        - Larger words indicate more common diagnoses and procedures within the dataset.
        """,
        """
        - Use the word clouds to identify the most common diagnoses and procedures at a glance.
        - Focus on developing strategies to address the most frequently occurring health issues and improve treatment effectiveness.
        """
    )

# Footer
#st.sidebar.markdown("---")
#st.sidebar.markdown("Developed by [Your Name]")
