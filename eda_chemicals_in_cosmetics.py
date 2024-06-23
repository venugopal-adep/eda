import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'Chemicals in Cosmetics.csv'
data = pd.read_csv(file_path)

# Data preprocessing
data['InitialDateReported'] = pd.to_datetime(data['InitialDateReported'], errors='coerce')
data['MostRecentDateReported'] = pd.to_datetime(data['MostRecentDateReported'], errors='coerce')

# Define functions for each visualization
def show_dataset():
    st.write("### Chemicals in Cosmetics Dataset")
    st.write(data)
    st.write("#### Explanation of Fields:")
    st.write("""
    - **CDPHId**: California Department of Public Health ID
    - **ProductName**: Name of the product
    - **CSFId**: Chemical Structure Framework ID
    - **CSF**: Chemical Structure Framework
    - **CompanyId**: ID of the company
    - **CompanyName**: Name of the company
    - **BrandName**: Brand name of the product
    - **PrimaryCategoryId**: Primary category ID
    - **PrimaryCategory**: Primary category of the product
    - **SubCategoryId**: Subcategory ID
    - **SubCategory**: Subcategory of the product
    - **CasNumber**: Chemical Abstracts Service number
    - **ChemicalId**: Chemical ID
    - **ChemicalName**: Name of the chemical
    - **InitialDateReported**: Initial date when the chemical was reported
    - **MostRecentDateReported**: Most recent date when the chemical was reported
    - **DiscontinuedDate**: Date when the product was discontinued
    - **ChemicalCreatedAt**: Date when the chemical record was created
    - **ChemicalUpdatedAt**: Date when the chemical record was last updated
    - **ChemicalDateRemoved**: Date when the chemical record was removed
    - **ChemicalCount**: Count of chemicals
    """)

def missing_values_heatmap():
    st.write("### Missing Values Heatmap")
    fig = go.Figure(data=go.Heatmap(z=data.isnull().astype(int).transpose(),
                                    x=data.index,
                                    y=data.columns,
                                    colorscale='Viridis'))
    fig.update_layout(title='Missing Values Heatmap', xaxis_title='Index', yaxis_title='Columns')
    st.plotly_chart(fig)

def primary_category_distribution():
    st.write("### Distribution of Primary Categories")
    category_counts = data['PrimaryCategory'].value_counts()
    fig = px.bar(category_counts, x=category_counts.index, y=category_counts.values,
                 labels={'x': 'Primary Category', 'y': 'Count'},
                 title='Distribution of Primary Categories')
    st.plotly_chart(fig)

def top_companies_by_products():
    st.write("### Top 10 Companies by Number of Products")
    top_companies = data['CompanyName'].value_counts().head(10)
    fig = px.bar(top_companies, x=top_companies.index, y=top_companies.values,
                 labels={'x': 'Company Name', 'y': 'Number of Products'},
                 title='Top 10 Companies by Number of Products')
    st.plotly_chart(fig)

def product_name_wordcloud():
    st.write("### Word Cloud of Product Names")
    product_names = ' '.join(data['ProductName'].dropna().tolist())
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(product_names)
    
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)

def top_chemicals():
    st.write("### Top 10 Chemicals Used")
    top_chemicals = data['ChemicalName'].value_counts().head(10)
    fig = px.bar(top_chemicals, x=top_chemicals.index, y=top_chemicals.values,
                 labels={'x': 'Chemical Name', 'y': 'Frequency'},
                 title='Top 10 Chemicals Used')
    st.plotly_chart(fig)

def reported_dates_distribution():
    st.write("### Distribution of Reported Dates")
    fig = px.histogram(data, x='InitialDateReported', nbins=30, title='Distribution of Initial Reported Dates')
    st.plotly_chart(fig)

# Create the Streamlit app
st.sidebar.title("EDA on Chemicals in Cosmetics")
visualization = st.sidebar.radio("Select Visualization", 
                                 ["Dataset Overview", "Missing Values Heatmap", 
                                  "Primary Category Distribution", "Top Companies by Products", 
                                  "Word Cloud of Product Names", "Top Chemicals Used", 
                                  "Reported Dates Distribution"])

if visualization == "Dataset Overview":
    show_dataset()
elif visualization == "Missing Values Heatmap":
    missing_values_heatmap()
elif visualization == "Primary Category Distribution":
    primary_category_distribution()
elif visualization == "Top Companies by Products":
    top_companies_by_products()
elif visualization == "Word Cloud of Product Names":
    product_name_wordcloud()
elif visualization == "Top Chemicals Used":
    top_chemicals()
elif visualization == "Reported Dates Distribution":
    reported_dates_distribution()
