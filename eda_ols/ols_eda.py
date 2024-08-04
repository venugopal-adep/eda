import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.preprocessing import MinMaxScaler

# Set page config
st.set_page_config(page_title="VIF and Model Analysis", layout="wide", page_icon="📊")

# Custom CSS
st.markdown("""
<style>
.stApp {
    background-color: #f0f8ff;
}
.stButton>button {
    background-color: #4CAF50;
    color: white;
}
.stTabs [data-baseweb="tab-list"] {
    gap: 2px;
}
.stTabs [data-baseweb="tab"] {
    height: 50px;
    white-space: pre-wrap;
    background-color: #e6e6fa;
    border-radius: 4px 4px 0 0;
    gap: 1px;
    padding-top: 10px;
    padding-bottom: 10px;
}
.stTabs [aria-selected="true"] {
    background-color: #4CAF50;
    color: white;
}
.highlight {
    background-color: #e6e6fa;
    padding: 10px;
    border-radius: 5px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# Title and description
st.title("📊 VIF and Model Analysis")
st.markdown("**Developed by: Venugopal Adep**")
st.markdown("Explore Variance Inflation Factor and model performance for BigMart Sales data!")

# File upload
train_file = st.sidebar.file_uploader("Upload train CSV file", type="csv")
test_file = st.sidebar.file_uploader("Upload test CSV file", type="csv")

# Function to preprocess data
def preprocess_data(df):
    df = df.drop(['Item_Identifier', 'Outlet_Identifier'], axis=1)
    df['Item_Fat_Content'] = df['Item_Fat_Content'].replace({'low fat': 'Low Fat', 'LF': 'Low Fat', 'reg': 'Regular'})
    df['Item_Weight'].fillna(df['Item_Weight'].mean(), inplace=True)
    df['Outlet_Size'].fillna(df['Outlet_Size'].mode()[0], inplace=True)
    df['Outlet_Age'] = 2013 - df['Outlet_Establishment_Year']
    df = df.drop('Outlet_Establishment_Year', axis=1)
    return df

# Function to create models
def create_models(X, y):
    X = pd.get_dummies(X, drop_first=True)
    scaler = MinMaxScaler()
    X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns, index=X.index)
    X_scaled = sm.add_constant(X_scaled)
    
    models = {}
    models['Full Model'] = sm.OLS(y, X_scaled).fit()
    
    # Create additional models by dropping specific columns
    columns_to_drop = ['Outlet_Age', 'Item_Weight', 'Item_Visibility']
    for col in columns_to_drop:
        X_reduced = X_scaled.drop(col, axis=1)
        models[f'Model without {col}'] = sm.OLS(y, X_reduced).fit()
    
    return models, X_scaled

# Function to calculate VIF
def calculate_vif(X):
    vif = pd.DataFrame()
    vif["Feature"] = X.columns
    vif["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    return vif.sort_values('VIF', ascending=False)

# Main content
if train_file is not None and test_file is not None:
    # Load and preprocess data
    train_df = preprocess_data(pd.read_csv(train_file))
    test_df = preprocess_data(pd.read_csv(test_file))
    
    X = train_df.drop('Item_Outlet_Sales', axis=1)
    y = train_df['Item_Outlet_Sales']
    
    # Create models
    models, X_scaled = create_models(X, y)
    
    # Calculate VIF
    vif_df = calculate_vif(X_scaled)
    
    # Tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📚 Learn", "📊 Data Analysis", "🧮 Model Performance", "🔬 VIF Analysis", "🧠 Quiz"])
    
    with tab1:
        st.header("📚 Learn about VIF and Model Analysis")
        
        st.markdown("""
        <div class="highlight">
        <h3>What is Variance Inflation Factor (VIF)?</h3>
        <p>VIF is a measure of the amount of multicollinearity in a set of multiple regression variables. It provides an index that measures how much the variance of an estimated regression coefficient is increased because of collinearity.</p>
        <ul>
            <li>VIF = 1: Not correlated</li>
            <li>1 < VIF < 5: Moderately correlated</li>
            <li>VIF > 5: Highly correlated</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="highlight">
        <h3>Why is VIF Important?</h3>
        <ul>
            <li>Helps identify multicollinearity in regression analysis</li>
            <li>Assists in feature selection by identifying redundant variables</li>
            <li>Improves model stability and interpretability</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="highlight">
        <h3>Model Performance Metrics</h3>
        <ul>
            <li>R-squared: Proportion of variance explained by the model</li>
            <li>Adjusted R-squared: R-squared adjusted for the number of predictors</li>
            <li>F-statistic: Overall significance of the model</li>
            <li>AIC/BIC: Model comparison metrics (lower is better)</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with tab2:
        st.header("📊 Data Analysis")
        
        st.subheader("Dataset Overview")
        st.write(train_df.head())
        
        st.subheader("Descriptive Statistics")
        st.write(train_df.describe())
        
        st.subheader("Correlation Heatmap")
        corr = train_df.corr()
        fig = px.imshow(corr, text_auto=True, aspect="auto")
        st.plotly_chart(fig)
        
        st.subheader("Feature Distribution")
        feature = st.selectbox("Select a feature", train_df.columns)
        fig = px.histogram(train_df, x=feature, marginal="box")
        st.plotly_chart(fig)
    
    with tab3:
        st.header("🧮 Model Performance")
        
        selected_model = st.selectbox("Select a model", list(models.keys()))
        
        st.subheader("Model Summary")
        st.write(models[selected_model].summary())
        
        st.subheader("Coefficient Plot")
        coef_df = pd.DataFrame({'Feature': models[selected_model].params.index, 'Coefficient': models[selected_model].params.values})
        fig = px.bar(coef_df, x='Coefficient', y='Feature', orientation='h')
        st.plotly_chart(fig)
    
    with tab4:
        st.header("🔬 VIF Analysis")
        
        st.subheader("VIF Scores")
        st.write(vif_df)
        
        st.subheader("VIF Plot")
        fig = px.bar(vif_df, x='VIF', y='Feature', orientation='h')
        fig.add_vline(x=5, line_dash="dash", line_color="red", annotation_text="High VIF Threshold")
        st.plotly_chart(fig)
    
    with tab5:
        st.header("🧠 Test Your Knowledge")
        
        questions = [
            {
                "question": "What does VIF stand for?",
                "options": ["Variable Inflation Factor", "Variance Inflation Factor", "Value Increase Factor", "Variable Importance Factor"],
                "correct": 1
            },
            {
                "question": "What is generally considered a high VIF value?",
                "options": ["Above 1", "Above 3", "Above 5", "Above 10"],
                "correct": 2
            },
            {
                "question": "What does a high VIF indicate?",
                "options": ["Low correlation", "High correlation", "No correlation", "Negative correlation"],
                "correct": 1
            }
        ]
        
        for i, q in enumerate(questions):
            st.subheader(f"Question {i+1}: {q['question']}")
            user_answer = st.radio(f"Select your answer for Question {i+1}:", q['options'], key=f"q{i}")
            
            if st.button(f"Check Answer for Question {i+1}", key=f"check{i}"):
                if q['options'].index(user_answer) == q['correct']:
                    st.success("Correct! Well done!")
                else:
                    st.error("Not quite right. Try again!")
            st.write("---")

else:
    st.write("Please upload both train and test CSV files to proceed.")

# Footer
st.markdown("""
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #0E1117;
    color: #FAFAFA;
    text-align: center;
    padding: 10px;
    font-size: 12px;
}
</style>
<div class="footer">
    Developed by Venugopal Adep | Data source: BigMart Sales Dataset
</div>
""", unsafe_allow_html=True)

# Add some spacing at the bottom to prevent content from being hidden by the footer
st.write("<br><br><br>", unsafe_allow_html=True)
