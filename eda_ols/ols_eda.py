import streamlit as st
import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.preprocessing import MinMaxScaler

# Streamlit UI
st.write("## Model Summary and VIF Scores")
st.write("**Developed by : Venugopal Adep**")

# File upload
train_file = st.sidebar.file_uploader("Upload train CSV file", type="csv")
test_file = st.sidebar.file_uploader("Upload test CSV file", type="csv")

if train_file is not None and test_file is not None:
    # Load the data from the uploaded files
    train_df = pd.read_csv(train_file)
    test_df = pd.read_csv(test_file)

    # Data preprocessing
    train_df = train_df.drop(['Item_Identifier', 'Outlet_Identifier'], axis=1)
    test_df = test_df.drop(['Item_Identifier', 'Outlet_Identifier'], axis=1)

    train_df['Item_Fat_Content'] = train_df['Item_Fat_Content'].apply(lambda x: 'Low Fat' if x == 'low fat' or x == 'LF' else x)
    train_df['Item_Fat_Content'] = train_df['Item_Fat_Content'].apply(lambda x: 'Regular' if x == 'reg' else x)
    test_df['Item_Fat_Content'] = test_df['Item_Fat_Content'].apply(lambda x: 'Low Fat' if x == 'low fat' or x == 'LF' else x)
    test_df['Item_Fat_Content'] = test_df['Item_Fat_Content'].apply(lambda x: 'Regular' if x == 'reg' else x)

    item_weight_indices_to_be_updated = train_df[train_df['Item_Weight'].isnull()].index
    train_df.loc[item_weight_indices_to_be_updated, 'Item_Weight'] = np.random.uniform(10, 14, len(item_weight_indices_to_be_updated))

    item_weight_indices_to_be_updated = test_df[test_df['Item_Weight'].isnull()].index
    test_df.loc[item_weight_indices_to_be_updated, 'Item_Weight'] = np.random.uniform(10, 14, len(item_weight_indices_to_be_updated))

    grocery_store_indices = train_df[train_df['Outlet_Size'].isnull()].query(" Outlet_Type == 'Grocery Store' ").index
    tier_2_indices = train_df[train_df['Outlet_Size'].isnull()].query(" Outlet_Location_Type == 'Tier 2' ").index

    train_df.loc[grocery_store_indices, 'Outlet_Size'] = 'Small'
    train_df.loc[tier_2_indices, 'Outlet_Size'] = 'Small'

    grocery_store_indices = test_df[test_df['Outlet_Size'].isnull()].query(" Outlet_Type == 'Grocery Store' ").index
    tier_2_indices = test_df[test_df['Outlet_Size'].isnull()].query(" Outlet_Location_Type == 'Tier 2' ").index

    test_df.loc[grocery_store_indices, 'Outlet_Size'] = 'Small'
    test_df.loc[tier_2_indices, 'Outlet_Size'] = 'Small'

    train_df['Outlet_Age'] = 2013 - train_df['Outlet_Establishment_Year']
    test_df['Outlet_Age'] = 2013 - test_df['Outlet_Establishment_Year']

    train_features = train_df.drop(['Item_Outlet_Sales', 'Outlet_Establishment_Year'], axis=1)
    train_target = train_df['Item_Outlet_Sales']

    train_features = pd.get_dummies(train_features, drop_first=True)

    scaler = MinMaxScaler()
    train_features_scaled = scaler.fit_transform(train_features)
    train_features_scaled = pd.DataFrame(train_features_scaled, index=train_features.index, columns=train_features.columns)

    train_features_scaled = sm.add_constant(train_features_scaled)

    # Model building
    ols_model_0 = sm.OLS(train_target, train_features_scaled)
    ols_res_0 = ols_model_0.fit()

    train_features_scaled_new = train_features_scaled.drop("Outlet_Age", axis=1)
    ols_model_2 = sm.OLS(train_target, train_features_scaled_new)
    ols_res_2 = ols_model_2.fit()

    train_features_scaled_new2 = train_features_scaled_new.drop(['Item_Type_Breads', 'Item_Type_Breakfast', 'Item_Type_Canned', 'Item_Type_Dairy', 'Item_Type_Frozen Foods', 'Item_Type_Fruits and Vegetables', 'Item_Type_Hard Drinks', 'Item_Type_Health and Hygiene', 'Item_Type_Household', 'Item_Type_Meat', 'Item_Type_Others', 'Item_Type_Seafood', 'Item_Type_Snack Foods', 'Item_Type_Soft Drinks', 'Item_Type_Starchy Foods'], axis=1)
    ols_model_3 = sm.OLS(train_target, train_features_scaled_new2)
    ols_res_3 = ols_model_3.fit()

    train_features_scaled_new3 = train_features_scaled_new2.drop("Item_Weight", axis=1)
    ols_model_4 = sm.OLS(train_target, train_features_scaled_new3)
    ols_res_4 = ols_model_4.fit()

    train_features_scaled_new4 = train_features_scaled_new3.drop(["Outlet_Location_Type_Tier 2", "Outlet_Location_Type_Tier 3"], axis=1)
    ols_model_5 = sm.OLS(train_target, train_features_scaled_new4)
    ols_res_5 = ols_model_5.fit()

    train_features_scaled_new5 = train_features_scaled_new4.drop(["Outlet_Size_Small", "Outlet_Size_Medium"], axis=1)
    ols_model_6 = sm.OLS(train_target, train_features_scaled_new5)
    ols_res_6 = ols_model_6.fit()

    train_features_scaled_new6 = train_features_scaled_new5.drop("Item_Visibility", axis=1)
    ols_model_7 = sm.OLS(train_target, train_features_scaled_new6)
    ols_res_7 = ols_model_7.fit()

    # Log transformation on the target variable
    train_target_log = np.log(train_target)

    # Fitting new model with the transformed target variable
    ols_model_8 = sm.OLS(train_target_log, train_features_scaled_new6)
    ols_res_8 = ols_model_8.fit()

    # Create a dropdown to select the model
    model_options = ["ols_res_0", "ols_res_2", "ols_res_3", "ols_res_4", "ols_res_5", "ols_res_6", "ols_res_7", "ols_res_8"]
    selected_model = st.sidebar.selectbox("Select a model", model_options)

    # Display the summary of the selected model
    if selected_model == "ols_res_0":
        st.subheader("Model Summary")
        st.write(ols_res_0.summary())
        
        st.subheader("VIF Scores")
        vif_series = pd.Series(
            [variance_inflation_factor(train_features_scaled.values, i) for i in range(train_features_scaled.shape[1])],
            index=train_features_scaled.columns,
            dtype=float
        )
        st.write(vif_series)

    elif selected_model == "ols_res_2":
        st.subheader("Model Summary")
        st.write(ols_res_2.summary())
        
        st.subheader("VIF Scores")
        vif_series = pd.Series(
            [variance_inflation_factor(train_features_scaled_new.values, i) for i in range(train_features_scaled_new.shape[1])],
            index=train_features_scaled_new.columns,
            dtype=float
        )
        st.write(vif_series)

    elif selected_model == "ols_res_3":
        st.subheader("Model Summary")
        st.write(ols_res_3.summary())
        
        st.subheader("VIF Scores")
        vif_series = pd.Series(
            [variance_inflation_factor(train_features_scaled_new2.values, i) for i in range(train_features_scaled_new2.shape[1])],
            index=train_features_scaled_new2.columns,
            dtype=float
        )
        st.write(vif_series)

    elif selected_model == "ols_res_4":
        st.subheader("Model Summary")
        st.write(ols_res_4.summary())
        
        st.subheader("VIF Scores")
        vif_series = pd.Series(
            [variance_inflation_factor(train_features_scaled_new3.values, i) for i in range(train_features_scaled_new3.shape[1])],
            index=train_features_scaled_new3.columns,
            dtype=float
        )
        st.write(vif_series)

    elif selected_model == "ols_res_5":
        st.subheader("Model Summary")
        st.write(ols_res_5.summary())
        
        st.subheader("VIF Scores")
        vif_series = pd.Series(
            [variance_inflation_factor(train_features_scaled_new4.values, i) for i in range(train_features_scaled_new4.shape[1])],
            index=train_features_scaled_new4.columns,
            dtype=float
        )
        st.write(vif_series)

    elif selected_model == "ols_res_6":
        st.subheader("Model Summary")
        st.write(ols_res_6.summary())
        
        st.subheader("VIF Scores")
        vif_series = pd.Series(
            [variance_inflation_factor(train_features_scaled_new5.values, i) for i in range(train_features_scaled_new5.shape[1])],
            index=train_features_scaled_new5.columns,
            dtype=float
        )
        st.write(vif_series)

    elif selected_model == "ols_res_7":
        st.subheader("Model Summary")
        st.write(ols_res_7.summary())
        
        st.subheader("VIF Scores")
        vif_series = pd.Series(
            [variance_inflation_factor(train_features_scaled_new6.values, i) for i in range(train_features_scaled_new6.shape[1])],
            index=train_features_scaled_new6.columns,
            dtype=float
        )
        st.write(vif_series)

    else:
        st.subheader("Model Summary")
        st.write(ols_res_8.summary())
        
        st.subheader("VIF Scores")
        vif_series = pd.Series(
            [variance_inflation_factor(train_features_scaled_new6.values, i) for i in range(train_features_scaled_new6.shape[1])],
            index=train_features_scaled_new6.columns,
            dtype=float
        )
        st.write(vif_series)

else:
    st.write("Please upload both train and test CSV files to proceed.")
