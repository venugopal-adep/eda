import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from textblob import TextBlob

# Load data
@st.cache_data
def load_data():
    data = pd.read_csv('Women_s_E-Commerce_Clothing_Reviews.csv')
    return data

data = load_data()

# Title
st.title('Women\'s E-Commerce Clothing Reviews : EDA')

# Sidebar for slide selection
st.sidebar.header('Slide Selection')
show_dataset = st.sidebar.checkbox('Show Dataset', value=False)
show_field_explanation = st.sidebar.checkbox('Show Field Explanation', value=False)
show_descriptive_stats = st.sidebar.checkbox('Show Descriptive Statistics', value=False)
show_visualizations = st.sidebar.checkbox('Show Visualizations', value=False)
show_sentiment_title = st.sidebar.checkbox('Sentiment Analysis on Title', value=False)
show_sentiment_summary = st.sidebar.checkbox('Sentiment Analysis on Summary', value=False)
show_conclusion = st.sidebar.checkbox('Show Conclusion', value=False)


# Slide 1: Show Dataset
if show_dataset:
    st.header('Dataset')
    st.write(data)

# Slide 2: Explanation of fields
if show_field_explanation:
    st.header('Field Explanation')
    st.markdown('''
    - **Clothing ID**: The unique identifier for the clothing item.
    - **Age**: The age of the reviewer.
    - **Title**: The title of the review.
    - **Review Text**: The body content of the review.
    - **Rating**: The rating given by the reviewer (1-5).
    - **Recommended IND**: Whether the reviewer recommends the product (1 for yes, 0 for no).
    - **Positive Feedback Count**: The number of positive feedback votes.
    - **Division Name**: The division name of the product.
    - **Department Name**: The department name of the product.
    - **Class Name**: The class name of the product.
    ''')

# Slide 3: Descriptive Statistics
if show_descriptive_stats:
    st.header('Descriptive Statistics')
    st.write(data.describe())

# Slide 4: Visualizations
if show_visualizations:
    st.header('Visualizations')

    # Visualization 1: Distribution of Ratings
    st.subheader('Distribution of Ratings')
    fig_ratings = px.histogram(data, x='Rating', title='Distribution of Ratings')
    st.plotly_chart(fig_ratings)
    st.markdown('**Insights:** The distribution of ratings shows the most common ratings given by reviewers.')
    st.markdown('**Recommendations:** Focus on improving products with lower ratings.')

    # Visualization 2: Age Distribution of Reviewers
    st.subheader('Age Distribution of Reviewers')
    fig_age = px.histogram(data, x='Age', title='Age Distribution of Reviewers')
    st.plotly_chart(fig_age)
    st.markdown('**Insights:** The age distribution helps understand the demographics of the reviewers.')
    st.markdown('**Recommendations:** Tailor marketing strategies to the predominant age groups.')

    # Visualization 3: Recommended vs. Not Recommended
    st.subheader('Recommended vs. Not Recommended')
    fig_recommend = px.histogram(data, x='Recommended IND', title='Recommended vs. Not Recommended')
    st.plotly_chart(fig_recommend)
    st.markdown('**Insights:** This shows the proportion of reviewers who recommend the products.')
    st.markdown('**Recommendations:** Investigate why some products are not recommended and address the issues.')

    # Visualization 4: Word Cloud of Review Text
    st.subheader('Word Cloud of Review Text')
    if 'Review.Text' in data.columns:
        review_text = ' '.join(data['Review.Text'].dropna().astype(str))
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(review_text)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        st.pyplot(plt)
        st.markdown('**Insights:** The word cloud highlights the most frequent words in the review texts.')
        st.markdown('**Recommendations:** Use these keywords to understand common sentiments and themes in the reviews.')

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
    st.header('Sentiment Analysis on Review Text')
    if 'Review.Text' in data.columns:
        data['Review_Text_Polarity'] = data['Review.Text'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
        data['Review_Text_Subjectivity'] = data['Review.Text'].apply(lambda x: TextBlob(str(x)).sentiment.subjectivity)
        st.write(data[['Review.Text', 'Review_Text_Polarity', 'Review_Text_Subjectivity']])
    else:
        st.error("The column 'Review Text' is not found in the dataset.")

# Slide 6: Conclusion
if show_conclusion:
    st.header('Conclusion')
    st.markdown('''
    The exploratory data analysis of women's e-commerce clothing reviews has highlighted several key insights:
    - The distribution of ratings shows the most common ratings given by reviewers.
    - The age distribution helps understand the demographics of the reviewers.
    - The proportion of reviewers who recommend the products provides insight into overall satisfaction.
    - The word cloud provides a visual representation of the most frequent words in the review texts.
    - Sentiment analysis helps in understanding the emotional tone and subjectivity of the titles and review texts.

    **Recommendations:**
    - Focus on improving products with lower ratings.
    - Tailor marketing strategies to the predominant age groups.
    - Investigate why some products are not recommended and address the issues.
    - Utilize common keywords from the word cloud to understand popular sentiments and enhance product descriptions.
    - Use sentiment analysis to gauge customer sentiment and adjust product offerings accordingly.

    Implementing these recommendations can help in understanding the dynamics of customer reviews and improving product offerings.
    ''')

# Footer
#st.sidebar.markdown('---')
#st.sidebar.markdown('Created by Venugopal Adep')
