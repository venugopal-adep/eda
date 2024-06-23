import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
file_path = 'Death_rates_for_suicide__by_sex__race__Hispanic_origin__and_age__United_States.csv'
data = pd.read_csv(file_path)

# Function to display insights and recommendations
def display_insights_and_recommendations(insights, recommendations):
    st.markdown("### Insights")
    st.write(insights)
    st.markdown("### Recommendations")
    st.write(recommendations)

# App title
st.title("Suicide Rates Analysis in the United States")
st.write("""
Death rates for suicide, by sex, race, Hispanic origin, and age: United States
Metadata Updated: April 28, 2022

Data on death rates for suicide, by selected population characteristics. Please refer to the PDF or Excel version of this table in the HUS 2019 Data Finder (https://www.cdc.gov/nchs/hus/contents2019.htm) for critical information about measures, definitions, and changes over time.

SOURCE: NCHS, National Vital Statistics System (NVSS); Grove RD, Hetzel AM. Vital statistics rates in the United States, 1940–1960. National Center for Health Statistics. 1968; numerator data from NVSS annual public-use Mortality Files; denominator data from U.S. Census Bureau national population estimates; and Murphy SL, Xu JQ, Kochanek KD, Arias E, Tejada-Vera B. Deaths: Final data for 2018. National Vital Statistics Reports; vol 69 no 13. Hyattsville, MD: National Center for Health Statistics. 2021. Available from: https://www.cdc.gov/nchs/products/nvsr.htm. For more information on the National Vital Statistics System, see the corresponding Appendix entry at https://www.cdc.gov/nchs/data/hus/hus19-appendix-508.pdf.
         
         """)

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Select a visualization:", ["Overview", "Suicide Rates Over Time", "Suicide Rates by Sex", "Suicide Rates by Race", "Suicide Rates by Age Group"])

# Overview of the dataset
if options == "Overview":
    st.header("Overview of the Dataset")
    st.dataframe(data.head())
    display_insights_and_recommendations(
        "The dataset includes suicide rates by sex, race, age, and year, providing a comprehensive view of demographic trends over time.",
        "Familiarize yourself with the dataset structure to understand the variables available for deeper analysis."
    )

# Suicide Rates Over Time
elif options == "Suicide Rates Over Time":
    st.header("Suicide Rates Over Time")
    fig = px.line(data, x='YEAR', y='ESTIMATE', title='Suicide Rates Over Time')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        "The suicide rates have fluctuated over the years, with significant peaks in certain periods.",
        "Investigate socio-economic and policy changes during periods of significant change in suicide rates."
    )

# Suicide Rates by Sex
elif options == "Suicide Rates by Sex":
    st.header("Suicide Rates by Sex")
    data_sex = data[data['STUB_LABEL'].isin(['Male', 'Female'])]
    fig = px.bar(data_sex, x='STUB_LABEL', y='ESTIMATE', title='Suicide Rates by Sex', labels={'STUB_LABEL': 'Sex', 'ESTIMATE': 'Suicide Rate (per 100,000)'})
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        "Males have consistently higher suicide rates compared to females.",
        "Develop gender-specific mental health interventions and support systems."
    )

# Suicide Rates by Race
elif options == "Suicide Rates by Race":
    st.header("Suicide Rates by Race")
    races = ['White', 'Black or African American', 'American Indian or Alaska Native', 'Asian', 'Pacific Islander']
    data_race_simple = data[data['STUB_LABEL'].str.contains('|'.join(races))]
    fig = px.bar(data_race_simple, x='STUB_LABEL', y='ESTIMATE', title='Suicide Rates by Race', labels={'STUB_LABEL': 'Race', 'ESTIMATE': 'Suicide Rate (per 100,000)'})
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        "Certain racial groups exhibit higher suicide rates, indicating potential cultural or systemic factors.",
        "Tailor mental health outreach programs to address the specific needs of high-risk racial groups."
    )

# Suicide Rates by Age Group
elif options == "Suicide Rates by Age Group":
    st.header("Suicide Rates by Age Group")
    age_groups = ['10-14 years', '15-24 years', '25-44 years', '45-64 years', '65 years and over']
    data_age = data[data['STUB_LABEL'].isin(age_groups)]
    fig = px.bar(data_age, x='STUB_LABEL', y='ESTIMATE', title='Suicide Rates by Age Group', labels={'STUB_LABEL': 'Age Group', 'ESTIMATE': 'Suicide Rate (per 100,000)'})
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        "The highest suicide rates are observed in specific age groups, such as young adults and the elderly.",
        "Focus mental health resources and preventative measures on age groups with higher suicide rates."
    )

# Footer
#st.sidebar.markdown("---")
#st.sidebar.markdown("Developed by [Your Name]")
