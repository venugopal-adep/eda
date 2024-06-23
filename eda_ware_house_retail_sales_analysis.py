import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np

# Placeholder for loading the dataset
file_path_warehouse_sales = 'Warehouse_and_Retail_Sales.csv'

# Load the dataset
# data_warehouse_sales = pd.read_csv(file_path_warehouse_sales)

# For demonstration purposes, create a sample dataframe
data_warehouse_sales = pd.DataFrame({
    'Date': pd.date_range(start='2020-01-01', periods=100, freq='M'),
    'Product Category': np.random.choice(['Electronics', 'Clothing', 'Furniture', 'Food', 'Books'], 100),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], 100),
    'Store': np.random.choice(['Store A', 'Store B', 'Store C', 'Store D'], 100),
    'Sales': np.random.uniform(1000, 10000, 100),
    'Product Name': np.random.choice(['Product 1', 'Product 2', 'Product 3', 'Product 4', 'Product 5'], 100)
})

# Function to display insights and recommendations
def display_insights_and_recommendations(insights, recommendations):
    st.markdown("### Insights")
    st.write(insights)
    st.markdown("### Recommendations")
    st.write(recommendations)

# App title
st.title("Warehouse and Retail Sales Analysis")

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Select a visualization:", [
    "Overview", "Sales Trends Over Time", "Sales by Product Category", "Sales by Region", "Sales Performance by Store",
    "Correlation Analysis", "Sales Heatmap by Month and Year", "Top Performing Products", "Word Cloud of Product Names"])

# Overview of the dataset
if options == "Overview":
    st.header("Overview of the Dataset")
    st.dataframe(data_warehouse_sales.head())
    display_insights_and_recommendations(
        """
        - The dataset includes information on sales, product categories, regions, stores, and product names.
        - It provides a comprehensive view of sales trends and performance across different dimensions.
        """,
        """
        - Familiarize yourself with the dataset structure to understand the variables available for deeper analysis.
        - Use this overview to identify potential areas of interest for further exploration.
        """
    )

# Sales Trends Over Time
elif options == "Sales Trends Over Time":
    st.header("Sales Trends Over Time")
    fig = px.line(data_warehouse_sales, x='Date', y='Sales', title='Sales Trends Over Time')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The line chart shows the sales trends over time.
        - There might be seasonal patterns or trends indicating peak sales periods.
        """,
        """
        - Investigate the factors contributing to peak sales periods.
        - Develop strategies to capitalize on peak sales times and mitigate low sales periods.
        """
    )

# Sales by Product Category
elif options == "Sales by Product Category":
    st.header("Sales by Product Category")
    fig = px.bar(data_warehouse_sales, x='Product Category', y='Sales', title='Sales by Product Category', color='Product Category')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The bar chart shows the sales distribution across different product categories.
        - Certain categories might have higher sales, indicating popular product types.
        """,
        """
        - Investigate the reasons behind the popularity of certain product categories.
        - Focus on stocking and promoting high-selling product categories to maximize revenue.
        """
    )

# Sales by Region
elif options == "Sales by Region":
    st.header("Sales by Region")
    fig = px.bar(data_warehouse_sales, x='Region', y='Sales', title='Sales by Region', color='Region')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The bar chart shows the sales distribution across different regions.
        - Certain regions might have higher sales, indicating regional preferences and demand.
        """,
        """
        - Investigate the factors contributing to higher sales in specific regions.
        - Tailor marketing and sales strategies to regional preferences to boost sales.
        """
    )

# Sales Performance by Store
elif options == "Sales Performance by Store":
    st.header("Sales Performance by Store")
    fig = px.bar(data_warehouse_sales, x='Store', y='Sales', title='Sales Performance by Store', color='Store')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The bar chart shows the sales performance of different stores.
        - Certain stores might consistently outperform others, indicating better management or location.
        """,
        """
        - Investigate the factors contributing to higher performance in top stores.
        - Implement best practices from high-performing stores across all locations to boost overall sales.
        """
    )

# Correlation Analysis
elif options == "Correlation Analysis":
    st.header("Correlation Analysis Between Variables")
    numeric_data = data_warehouse_sales.select_dtypes(include=[np.number])
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
        - Use correlation insights to inform strategies for improving sales performance.
        """
    )

# Sales Heatmap by Month and Year
elif options == "Sales Heatmap by Month and Year":
    st.header("Sales Heatmap by Month and Year")
    data_warehouse_sales['Month'] = data_warehouse_sales['Date'].dt.month
    data_warehouse_sales['Year'] = data_warehouse_sales['Date'].dt.year
    heatmap_data = data_warehouse_sales.pivot_table(index='Year', columns='Month', values='Sales', aggfunc='sum')
    fig = px.imshow(heatmap_data, aspect='auto', title='Sales Heatmap by Month and Year')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The heatmap shows the sales distribution across different months and years.
        - Certain months might consistently show higher sales, indicating seasonal trends.
        """,
        """
        - Investigate the factors contributing to seasonal sales trends.
        - Develop promotional campaigns and inventory strategies to align with seasonal sales patterns.
        """
    )

# Top Performing Products
elif options == "Top Performing Products":
    st.header("Top Performing Products")
    top_products = data_warehouse_sales.groupby('Product Name')['Sales'].sum().reset_index().sort_values(by='Sales', ascending=False).head(10)
    fig = px.bar(top_products, x='Product Name', y='Sales', title='Top Performing Products', color='Product Name')
    st.plotly_chart(fig)
    display_insights_and_recommendations(
        """
        - The bar chart shows the top performing products based on total sales.
        - Certain products might consistently generate high revenue, indicating customer preference.
        """,
        """
        - Investigate the reasons behind the success of top performing products.
        - Focus on promoting and stocking high-performing products to maximize sales revenue.
        """
    )

# Word Cloud of Product Names
elif options == "Word Cloud of Product Names":
    st.header("Word Cloud of Product Names")
    product_name_counts = data_warehouse_sales['Product Name'].value_counts().to_dict()
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(product_name_counts)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)
    display_insights_and_recommendations(
        """
        - The word cloud visualizes the frequency of different product names.
        - Larger words indicate more common product names within the dataset.
        """,
        """
        - Use the word cloud to identify the most common product names at a glance.
        - Focus on promoting and stocking frequently purchased products to boost sales.
        """
    )

# Footer
#st.sidebar.markdown("---")
#st.sidebar.markdown("Developed by [Your Name]")
