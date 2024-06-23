import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np

# Placeholder for loading the dataset
file_path_drug_overdose = 'Drug_overdose_death_rates__by_drug_type__sex__age__race__and_Hispanic_origin__United_States.csv'

# Load the dataset
# data_drug_overdose = pd.read_csv(file_path_drug_overdose)

# For demonstration purposes, create a sample dataframe
data_drug_overdose = pd.DataFrame({
    'Year': np.random.choice(range(2000, 2021), 100),
    'Drug Type': np.random.choice(['Opioids', 'Cocaine', 'Methamphetamine', 'Heroin', 'Prescription Drugs'], 100),
    'Age Group': np.random.choice(['0-24', '25-34', '35-44', '45-54', '55-64', '65+'], 100),
    'Gender': np.random.choice(['Male', 'Female'], 100),
    'Race/Ethnicity': np.random.choice(['White', 'Black', 'Hispanic', 'Asian', 'Other'], 100),
    'Death Rate': np.random.uniform(5, 50, 100),
    'State': np.random.choice(['CA', 'TX', 'NY', 'FL', 'PA'], 100)
})

# Function to display insights and recommendations
def display_insights_and_recommendations(insights, recommendations):
    st.markdown("### Insights")
    st.write(insights)
    st.markdown("### Recommendations")
    st.write(recommendations)

# App title
st.title("Drug Overdose Death Rates Analysis")
st.write("""
         Drug overdose death rates, by drug type, sex, age, race, and Hispanic origin: United States
Metadata Updated: April 29, 2022

Data on drug overdose death rates, by drug type and selected population characteristics. Please refer to the PDF or Excel version of this table in the HUS 2019 Data Finder (https://www.cdc.gov/nchs/hus/contents2019.htm) for critical information about measures, definitions, and changes over time.

SOURCE: NCHS, National Vital Statistics System, numerator data from annual public-use Mortality Files; denominator data from U.S. Census Bureau national population estimates; and Murphy SL, Xu JQ, Kochanek KD, Arias E, Tejada-Vera B. Deaths: Final data for 2018. National Vital Statistics Reports; vol 69 no 13. Hyattsville, MD: National Center for Health Statistics.2021. Available from: https://www.cdc.gov/nchs/products/nvsr.htm. For more information on the National Vital Statistics System, see the corresponding Appendix entry at https://www.cdc.gov/nchs/data/hus/hus19-appendix-508.pdf.
         """)

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Select a visualization:", ["Overview", "Death Rates Over Time", "Death Rates by Drug Type", "Death Rates by Age Group", "Death Rates by Gender", "Death Rates by Race/Ethnicity", "Geographical Distribution", "Correlation Analysis", "Word Cloud of Drug Types"])

# Overview of the dataset
if options == "Overview":
    st.header("Overview of the Dataset")
    st.dataframe(data_drug_overdose.head())
    display_insights_and_recommendations(
        """
        - The dataset includes information on drug overdose death rates categorized by year, drug type, age group, gender, race/ethnicity, and state.
        - It provides a comprehensive view of drug overdose trends and patterns over time and across different demographic groups.
        """,
        """
        - Familiarize yourself with the dataset structure to understand the variables available for deeper analysis.
        - Use this overview to identify potential areas of interest for further exploration.
        """
    )

# Death Rates Over Time
elif options == "Death Rates Over Time":
    st.header("Death Rates Over Time")
    fig = px.bar(data_drug_overdose, x='Year', y='Death Rate', color='Drug Type', title='Death Rates Over Time', barmode='group')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The bar chart shows the death rates from different drugs over the years.
        - There might be an increasing trend in death rates for certain drugs, indicating a growing public health concern.
        """,
        """
        - Investigate the factors contributing to the rising death rates for specific drugs over the years.
        - Develop and promote public health initiatives to address the increasing trend in drug overdose deaths.
        """
    )

# Death Rates by Drug Type
elif options == "Death Rates by Drug Type":
    st.header("Death Rates by Drug Type")
    fig = px.pie(data_drug_overdose, names='Drug Type', values='Death Rate', title='Death Rates by Drug Type')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The pie chart shows the distribution of death rates by drug type.
        - Certain drugs might have higher death rates, indicating areas for focused public health efforts.
        """,
        """
        - Investigate the reasons behind higher death rates for specific drug types.
        - Develop targeted intervention programs to reduce overdose deaths related to high-risk drugs.
        """
    )

# Death Rates by Age Group
elif options == "Death Rates by Age Group":
    st.header("Death Rates by Age Group")
    fig = px.bar(data_drug_overdose, x='Age Group', y='Death Rate', color='Drug Type', title='Death Rates by Age Group', barmode='group')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The bar chart shows the distribution of death rates across different age groups.
        - Certain age groups might have higher death rates, indicating targeted areas for intervention.
        """,
        """
        - Investigate the lifestyle and environmental factors contributing to higher death rates in specific age groups.
        - Develop age-specific health and wellness programs to combat drug overdose deaths.
        """
    )

# Death Rates by Gender
elif options == "Death Rates by Gender":
    st.header("Death Rates by Gender")
    fig = px.histogram(data_drug_overdose, x='Gender', y='Death Rate', color='Drug Type', barmode='group', title='Death Rates by Gender')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The histogram shows the distribution of death rates between males and females.
        - There might be gender differences in death rates, indicating a need for gender-specific interventions.
        """,
        """
        - Investigate the reasons behind gender disparities in drug overdose death rates.
        - Develop gender-specific strategies to address the underlying causes of overdose deaths.
        """
    )

# Death Rates by Race/Ethnicity
elif options == "Death Rates by Race/Ethnicity":
    st.header("Death Rates by Race/Ethnicity")
    fig = px.bar(data_drug_overdose, x='Race/Ethnicity', y='Death Rate', color='Drug Type', title='Death Rates by Race/Ethnicity', barmode='group')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The bar chart shows the distribution of death rates across different racial and ethnic groups.
        - Certain racial/ethnic groups might have higher death rates, indicating areas for focused public health efforts.
        """,
        """
        - Investigate the cultural, socio-economic, and environmental factors contributing to drug overdose deaths in specific racial/ethnic groups.
        - Develop culturally sensitive and community-based interventions to reduce drug overdose deaths.
        """
    )

# Geographical Distribution of Death Rates
elif options == "Geographical Distribution":
    st.header("Geographical Distribution of Death Rates")
    state_abbrev = {'CA': 'California', 'TX': 'Texas', 'NY': 'New York', 'FL': 'Florida', 'PA': 'Pennsylvania'}
    data_drug_overdose['State Name'] = data_drug_overdose['State'].map(state_abbrev)
    fig = px.choropleth(data_drug_overdose, locations='State', locationmode='USA-states', color='Death Rate', hover_name='State Name', title='Geographical Distribution of Death Rates', scope='usa')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The choropleth map shows the geographical distribution of drug overdose death rates across different states.
        - Certain states might have higher death rates, indicating hotspots of drug overdose deaths.
        """,
        """
        - Analyze the geographical distribution to identify hotspots of drug overdose deaths.
        - Implement targeted public health initiatives in high-risk states to reduce drug overdose deaths.
        """
    )

# Correlation Analysis
elif options == "Correlation Analysis":
    st.header("Correlation Analysis Between Variables")
    numeric_data = data_drug_overdose.select_dtypes(include=[np.number])
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
        - Use correlation insights to inform strategies for reducing drug overdose deaths through targeted interventions.
        """
    )

# Word Cloud of Drug Types
elif options == "Word Cloud of Drug Types":
    st.header("Word Cloud of Drug Types")
    drug_type_counts = data_drug_overdose['Drug Type'].value_counts().to_dict()
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(drug_type_counts)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)
    display_insights_and_recommendations(
        """
        - The word cloud visualizes the frequency of different drug types.
        - Larger words indicate more common drug types within the dataset.
        """,
        """
        - Use the word cloud to identify the most common drug types at a glance.
        - Focus on developing strategies to address the most frequently occurring drug types associated with overdose deaths.
        """
    )

# Footer
#st.sidebar.markdown("---")
#st.sidebar.markdown("Developed by [Your Name]")
