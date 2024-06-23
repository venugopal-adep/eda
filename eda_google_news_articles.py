import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from textblob import TextBlob

# Load data
@st.cache_data
def load_data():
    data = pd.read_csv('google_news_articles.csv')
    return data

data = load_data()

# Title
st.title('Google News Articles : EDA & Sentiment Analysis')

# Sidebar for slide selection
st.sidebar.header('Slide Selection')
show_dataset = st.sidebar.checkbox('Show Dataset', value=False)
show_field_explanation = st.sidebar.checkbox('Show Field Explanation', value=False)
show_descriptive_stats = st.sidebar.checkbox('Show Descriptive Statistics', value=False)
show_visualizations = st.sidebar.checkbox('Show Visualizations', value=False)
show_conclusion = st.sidebar.checkbox('Show Conclusion', value=False)
show_sentiment_title = st.sidebar.checkbox('Sentiment Analysis on Title', value=False)
show_sentiment_summary = st.sidebar.checkbox('Sentiment Analysis on Summary', value=False)
show_sentiment_body = st.sidebar.checkbox('Sentiment Analysis on Body', value=False)

# Slide 1: Show Dataset
if show_dataset:
    st.header('Dataset')
    st.write(data)

# Slide 2: Explanation of fields
if show_field_explanation:
    st.header('Field Explanation')
    st.markdown('''
    - **ID**: The unique identifier for the article.
    - **Title**: The title of the news article.
    - **URL**: The URL of the news article.
    - **Summary**: The summary of the news article.
    - **Body**: The body content of the news article.
    - **Published Date**: The date and time when the article was published.
    ''')

# Slide 3: Descriptive Statistics
if show_descriptive_stats:
    st.header('Descriptive Statistics')
    st.write(data.describe())

# Slide 4: Visualizations
if show_visualizations:
 

    # Visualization 3: Word Cloud of Titles
    st.subheader('Word Cloud of Titles')
    if 'Title' in data.columns:
        title_text = ' '.join(data['Title'].dropna().astype(str))
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(title_text)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        st.pyplot(plt)
        st.markdown('**Insights:** The word cloud highlights the most frequent words in the article titles.')
        st.markdown('**Recommendations:** Use these keywords to understand common topics and themes in the articles.')
    else:
        st.error("The column 'Title' is not found in the dataset.")

    # Add more visualizations as needed

# Slide 5: Sentiment Analysis
if show_sentiment_title:
    st.header('Sentiment Analysis on Title')
    if 'Title' in data.columns:
        data['Title_Polarity'] = data['Title'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
        data['Title_Subjectivity'] = data['Title'].apply(lambda x: TextBlob(str(x)).sentiment.subjectivity)
        st.write(data[['Title', 'Title_Polarity', 'Title_Subjectivity']])
    else:
        st.error("The column 'Title' is not found in the dataset.")

if show_sentiment_summary:
    st.header('Sentiment Analysis on Summary')
    if 'Summary' in data.columns:
        data['Summary_Polarity'] = data['Summary'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
        data['Summary_Subjectivity'] = data['Summary'].apply(lambda x: TextBlob(str(x)).sentiment.subjectivity)
        st.write(data[['Summary', 'Summary_Polarity', 'Summary_Subjectivity']])
    else:
        st.error("The column 'Summary' is not found in the dataset.")

if show_sentiment_body:
    st.header('Sentiment Analysis on Body')
    if 'Body' in data.columns:
        data['Body_Polarity'] = data['Body'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
        data['Body_Subjectivity'] = data['Body'].apply(lambda x: TextBlob(str(x)).sentiment.subjectivity)
        st.write(data[['Body', 'Body_Polarity', 'Body_Subjectivity']])
    else:
        st.error("The column 'Body' is not found in the dataset.")

# Slide 6: Conclusion
if show_conclusion:
    st.header('Conclusion')
    st.markdown('''
    The exploratory data analysis of Google News articles has highlighted several key insights:
    - The number of articles varies significantly across different publications.
    - There are observable trends in the number of articles published over the years.
    - The word cloud provides a visual representation of the most frequent words in the article titles.
    - Sentiment analysis helps in understanding the emotional tone and subjectivity of the titles, summaries, and body content of the articles.

    **Recommendations:**
    - Focus on top publications for better reach.
    - Analyze years with high publication rates for potential factors influencing these trends.
    - Utilize common keywords from the word cloud to understand popular topics and enhance content strategy.
    - Use sentiment analysis to gauge public sentiment and adjust content strategy accordingly.

    Implementing these recommendations can help in understanding the dynamics of news article publication better.
    ''')

# Footer
#st.sidebar.markdown('---')
#st.sidebar.markdown('Created by [Your Name]')
