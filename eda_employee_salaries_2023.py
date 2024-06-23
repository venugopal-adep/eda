import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np

# Placeholder for loading the dataset
file_path_employee_salaries = 'Employee_Salaries_-_2023.csv'

# Load the dataset
# data_employee_salaries = pd.read_csv(file_path_employee_salaries)

# For demonstration purposes, create a sample dataframe
data_employee_salaries = pd.DataFrame({
    'Year': pd.date_range(start='2020', periods=100, freq='M').year,
    'Department': np.random.choice(['HR', 'Finance', 'Engineering', 'Marketing', 'Sales'], 100),
    'Job Title': np.random.choice(['Analyst', 'Manager', 'Engineer', 'Director', 'Consultant'], 100),
    'Salary': np.random.randint(50000, 150000, 100)
})

# Function to display insights and recommendations
def display_insights_and_recommendations(insights, recommendations):
    st.markdown("### Insights")
    st.write(insights)
    st.markdown("### Recommendations")
    st.write(recommendations)

# App title
st.title("Employee Salaries Analysis - 2023")
st.write("""
         Employee Salaries - 2023
Metadata Updated: February 17, 2024

Annual salary information including gross pay and overtime pay for all active, permanent employees of Montgomery County, MD paid in calendar year 2023. This information will be published annually each year.
         """)

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Select a visualization:", ["Overview", "Distribution of Salaries", "Average Salary by Department", "Salary Trends by Year", "Salary Distribution by Job Title", "Correlation Analysis", "Word Cloud of Job Titles"])

# Overview of the dataset
if options == "Overview":
    st.header("Overview of the Dataset")
    st.dataframe(data_employee_salaries.head())
    display_insights_and_recommendations(
        """
        - The dataset includes employee salaries along with their department, job title, and year.
        - It provides a comprehensive view of the salary distribution across different departments and job titles.
        """,
        """
        - Familiarize yourself with the dataset structure to understand the variables available for deeper analysis.
        - Use this overview to identify potential areas of interest for further exploration.
        """
    )

# Distribution of Salaries
elif options == "Distribution of Salaries":
    st.header("Distribution of Salaries")
    fig = px.histogram(data_employee_salaries, x='Salary', title='Distribution of Salaries')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The salary distribution shows the frequency of different salary ranges among employees.
        - Most employees fall within a specific salary range, indicating common pay scales.
        """,
        """
        - Identify the common salary ranges and investigate the factors contributing to them.
        - Consider policies or initiatives to address salary disparities if any are observed.
        """
    )

# Average Salary by Department
elif options == "Average Salary by Department":
    st.header("Average Salary by Department")
    avg_salary_dept = data_employee_salaries.groupby('Department')['Salary'].mean().reset_index()
    fig = px.bar(avg_salary_dept, x='Department', y='Salary', title='Average Salary by Department')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The average salary varies significantly across different departments.
        - Some departments, like Engineering or Finance, may have higher average salaries compared to others like HR or Marketing.
        """,
        """
        - Investigate the reasons behind the salary differences between departments.
        - Use this information to inform salary reviews and ensure equitable pay across departments.
        """
    )

# Salary Trends by Year
elif options == "Salary Trends by Year":
    st.header("Salary Trends by Year")
    avg_salary_year = data_employee_salaries.groupby('Year')['Salary'].mean().reset_index()
    fig = px.line(avg_salary_year, x='Year', y='Salary', title='Salary Trends by Year')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The average salary shows trends over the years, with potential increases or decreases.
        - Observing salary trends can help in understanding the impact of economic conditions or company policies on employee compensation.
        """,
        """
        - Analyze the factors influencing salary trends over time.
        - Use trend analysis to forecast future salary budgets and ensure competitive compensation.
        """
    )

# Salary Distribution by Job Title
elif options == "Salary Distribution by Job Title":
    st.header("Salary Distribution by Job Title")
    fig = px.box(data_employee_salaries, x='Job Title', y='Salary', title='Salary Distribution by Job Title')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The salary distribution varies across different job titles, indicating potential differences in pay scale.
        - Higher-level positions like Directors typically have a wider salary range compared to entry-level positions like Analysts.
        """,
        """
        - Consider the job roles and responsibilities that may contribute to salary variations.
        - Ensure that salary ranges for each job title are competitive and aligned with industry standards.
        """
    )

# Correlation Analysis
elif options == "Correlation Analysis":
    st.header("Correlation Analysis Between Variables")
    numeric_data = data_employee_salaries.select_dtypes(include=[np.number])
    corr = numeric_data.corr()
    fig = px.imshow(corr, title='Correlation Matrix of Variables')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - Certain variables show strong correlations with each other.
        - For example, the correlation between job titles and departments can highlight common salary structures within departments.
        """,
        """
        - Focus on correlated variables for more detailed analysis.
        - Use correlation insights to understand the relationships between different aspects of employee data.
        """
    )

# Word Cloud of Job Titles
elif options == "Word Cloud of Job Titles":
    st.header("Word Cloud of Job Titles")
    job_title_counts = data_employee_salaries['Job Title'].value_counts().to_dict()
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(job_title_counts)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)
    display_insights_and_recommendations(
        """
        - The word cloud visualizes the frequency of different job titles.
        - Larger words indicate more common job titles within the dataset.
        """,
        """
        - Use the word cloud to identify the most common job titles at a glance.
        - This can inform hiring strategies and highlight key roles within the organization.
        """
    )

# Footer
#st.sidebar.markdown("---")
#st.sidebar.markdown("Developed by [Your Name]")
