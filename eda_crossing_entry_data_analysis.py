import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
@st.cache_data
def load_data():
    data = pd.read_csv('Border_Crossing_Entry_Data1.csv')
    data['Date'] = pd.to_datetime(data['Date'], format='%b %Y')
    return data

data = load_data()

# Set up the Streamlit app layout
st.title("Border Crossing Entry Data Analysis")
st.write("""
         Border Crossing Entry Data
Metadata Updated: April 26, 2024

The Bureau of Transportation Statistics (BTS) Border Crossing Data provide summary statistics for inbound crossings at the U.S.-Canada and the U.S.-Mexico border at the port level. Data are available for trucks, trains, containers, buses, personal vehicles, passengers, and pedestrians. Border crossing data are collected at ports of entry by U.S. Customs and Border Protection (CBP). The data reflect the number of vehicles, containers, passengers or pedestrians entering the United States. CBP does not collect comparable data on outbound crossings. Users seeking data on outbound counts may therefore want to review data from individual bridge operators, border state governments, or the Mexican and Canadian governments.
         """)

st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ["Overview", "Distribution by State", "Volume Over Time", "Comparison of Measures", "Geographical Distribution", "Monthly Trends", "Latitude vs Volume", "Impact of Border"])

if options == "Overview":
    st.header("Dataset Overview")
    st.write(data.head())
    st.write("Total Rows:", data.shape[0])
    st.write("Total Columns:", data.shape[1])
    st.write("Columns:", list(data.columns))

if options == "Distribution by State":
    st.header("Distribution of Border Crossings by State")
    state_counts = data['State'].value_counts().reset_index()
    state_counts.columns = ['State', 'Count']
    fig = px.bar(state_counts, x='Count', y='State', orientation='h', title="Distribution of Border Crossings by State")
    st.plotly_chart(fig)
    st.markdown("""
    **Insight:**
    - The majority of border crossings occur in a few key states, with North Dakota, Washington and Maine leading.
    
    **Recommendation:**
    - Focus on enhancing infrastructure and resources in states with high traffic to improve efficiency and security.
    """)

if options == "Volume Over Time":
    st.header("Border Crossing Volume Over Time")
    monthly_data = data[['Date', 'Value']].groupby(pd.Grouper(key='Date', freq='M')).sum().reset_index()
    fig = px.line(monthly_data, x='Date', y='Value', title="Border Crossing Volume Over Time")
    st.plotly_chart(fig)
    st.markdown("""
    **Insight:**
    - The data shows visible trends and seasonality in border crossing volumes. Peaks and troughs may correspond to specific events or policies.
    
    **Recommendation:**
    - Analyze causes of significant peaks and troughs to improve forecasting and resource allocation.
    """)

if options == "Comparison of Measures":
    st.header("Comparison of Border Crossing Measures")
    measure_counts = data['Measure'].value_counts().reset_index()
    measure_counts.columns = ['Measure', 'Count']
    fig = px.bar(measure_counts, x='Count', y='Measure', orientation='h', title="Comparison of Border Crossing Measures")
    st.plotly_chart(fig)
    st.markdown("""
    **Insight:**
    - Personal vehicles are the most common measure, indicating a heavy reliance on road transport for cross-border trade.
    
    **Recommendation:**
    - Enhance infrastructure and policies to support personal vehicles, while exploring opportunities to increase rail and train usage for better efficiency.
    """)

if options == "Geographical Distribution":
    st.header("Geographical Distribution of Border Crossings")
    fig = px.scatter_mapbox(data, lat="Latitude", lon="Longitude", color="Border",
                            title="Geographical Distribution of Border Crossings",
                            mapbox_style="carto-positron", zoom=1, height=500)
    st.plotly_chart(fig)
    st.markdown("""
    **Insight:**
    - Border crossings are concentrated in specific geographical regions along both the US-Canada and US-Mexico borders.
    
    **Recommendation:**
    - Enhance security measures and manage resources more effectively in high-traffic regions to ensure smooth and secure border crossings.
    """)

if options == "Monthly Trends":
    st.header("Monthly Trends in Border Crossings")
    monthly_trends = data[['Value']].groupby(data['Date'].dt.month).sum().reset_index()
    monthly_trends.columns = ['Month', 'Value']
    fig = px.line(monthly_trends, x='Month', y='Value', title="Monthly Trends in Border Crossings")
    st.plotly_chart(fig)
    st.markdown("""
    **Insight:**
    - Clear monthly trends are observed, with certain months consistently showing higher volumes of crossings, likely due to seasonal travel or commercial cycles.
    
    **Recommendation:**
    - Implement flexible resource planning to accommodate monthly fluctuations in border crossing volumes.
    """)

if options == "Latitude vs Volume":
    st.header("Relationship Between Latitude and Border Crossing Volume")
    lat_volume = data[['Latitude', 'Value']].groupby('Latitude').sum().reset_index()
    fig = px.scatter(lat_volume, x='Latitude', y='Value', title="Latitude vs Border Crossing Volume")
    st.plotly_chart(fig)
    st.markdown("""
    **Insight:**
    - Certain latitudes, corresponding to major border cities, show higher volumes of crossings.
    
    **Recommendation:**
    - Focus on improving infrastructure and facilities in regions with high border crossing volumes to ensure efficient processing.
    """)

if options == "Impact of Border":
    st.header("Impact of Border on Crossing Volumes")
    fig = px.box(data, x='Border', y='Value', title="Impact of Border on Crossing Volumes")
    st.plotly_chart(fig)
    st.markdown("""
    **Insight:**
    - The US-Mexico border has significantly higher volumes of crossings compared to the US-Canada border, possibly due to different trade policies and economic activities.
    
    **Recommendation:**
    - Prioritize resource allocation and policy adjustments for the US-Mexico border to manage the higher traffic effectively.
    """)

# Run the app using Streamlit
# Save this script as `app.py` and run it using `streamlit run app.py`
