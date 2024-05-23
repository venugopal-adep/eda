import streamlit as st
import pandas as pd
import plotly.express as px
import io
import missingno as msno
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, spearmanr
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler, Normalizer
from sklearn.feature_selection import SelectKBest, f_regression
from wordcloud import WordCloud
from sklearn.cluster import KMeans

def main():
    st.title('Advanced EDA on Uploaded Dataset')
    st.subheader('Exploratory Data Analysis using Streamlit and Plotly')

    # File uploader allows user to add their own CSV
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)

        with st.sidebar:
            show_data = st.checkbox('Show Dataset', False)
            show_info = st.checkbox('Show Data Info', False)
            show_summary_numeric = st.checkbox('Show Summary Statistics (Numeric)', False)
            show_summary_categorical = st.checkbox('Show Summary Statistics (Categorical)', False)
            show_missing = st.checkbox('Show Missing Values', False)
            show_distribution = st.checkbox('Show Distribution Plot', False)
            show_boxplot = st.checkbox('Show Box Plot', False)
            show_violinplot = st.checkbox('Show Violin Plot', False)
            show_heatmap = st.checkbox('Correlation Heatmap', False)
            show_scatterplot = st.checkbox('Show Scatter Plot', False)
            show_crosstab = st.checkbox('Show Crosstab Analysis', False)
            show_unique_values = st.checkbox('Show Unique Values Count', False)
            show_pairplot = st.checkbox('Show Pair Plot', False)
            show_correlation = st.checkbox('Show Correlation Analysis', False)
            show_feature_scaling = st.checkbox('Show Feature Scaling', False)
            show_feature_selection = st.checkbox('Show Feature Selection', False)
            show_duplicates = st.checkbox('Show Duplicate Rows', False)
            show_outliers = st.checkbox('Show Outlier Detection', False)
            show_pivot_table = st.checkbox('Show Pivot Table', False)
            show_wordcloud = st.checkbox('Show Word Cloud', False)
            show_parallel_coordinates = st.checkbox('Show Parallel Coordinates Plot', False)
            show_bubble = st.checkbox('Show Bubble Plot', False)
            show_piechart = st.checkbox('Show Pie Chart', False)
            show_treemap = st.checkbox('Show Treemap', False)
            show_3d_scatter = st.checkbox('Show 3D Scatter Plot', False)
            show_3d_kmeans = st.checkbox('Show 3D K-Means Clustering', False)

        if show_data:
            st.write(data)

        if show_info:
            buffer = io.StringIO()
            data.info(buf=buffer)
            s = buffer.getvalue()
            st.text(s)

        if show_summary_numeric:
            st.subheader("Summary Statistics (Numeric)")
            st.write(data.describe())

        if show_summary_categorical:
            st.subheader("Summary Statistics (Categorical)")
            categorical_columns = data.select_dtypes(include=['object']).columns
            if len(categorical_columns) > 0:
                st.write(data[categorical_columns].describe())
            else:
                st.write("No categorical columns found in the dataset.")

        if show_missing:
            st.subheader("Missing Values Matrix")
            fig, ax = plt.subplots()
            msno.matrix(data, ax=ax)  # Missingno matrix plot
            st.pyplot(fig)

        if show_distribution:
            columns = data.select_dtypes(include=['float64', 'int64']).columns.tolist()
            column_to_plot = st.selectbox("Select Column for Histogram", columns, key='hist')
            fig = px.histogram(data, x=column_to_plot, nbins=20)
            st.plotly_chart(fig, use_container_width=True)

        if show_boxplot:
            columns = data.select_dtypes(include=['float64', 'int64']).columns.tolist()
            column_to_plot = st.selectbox("Select Column for Box Plot", columns, key='box')
            fig = px.box(data, y=column_to_plot)
            st.plotly_chart(fig, use_container_width=True)

        if show_violinplot:
            columns = data.select_dtypes(include=['float64', 'int64']).columns.tolist()
            column_to_plot = st.selectbox("Select Column for Violin Plot", columns, key='violin')
            fig = px.violin(data, y=column_to_plot)
            st.plotly_chart(fig, use_container_width=True)

        if show_heatmap:
            corr = data.corr()
            fig = px.imshow(corr, text_auto=".2f")
            fig.update_layout(height=600)  # Adjust the height as needed
            st.plotly_chart(fig, use_container_width=True)

        if show_scatterplot:
            numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns.tolist()
            x_axis = st.selectbox("Select X Axis", numeric_columns, index=0, key='scatter_x')
            y_axis = st.selectbox("Select Y Axis", numeric_columns, index=1, key='scatter_y')
            color_by = st.selectbox("Color By (Optional)", ["None"] + numeric_columns, index=0, key='scatter_color')
            
            if color_by == "None":
                fig = px.scatter(data, x=x_axis, y=y_axis)
            else:
                fig = px.scatter(data, x=x_axis, y=y_axis, color=color_by)
            
            st.plotly_chart(fig, use_container_width=True)

        if show_unique_values:
            st.subheader("Unique Values Count")
            unique_counts = {col: data[col].nunique() for col in data.columns}
            unique_df = pd.DataFrame.from_dict(unique_counts, orient='index', columns=['Count'])
            st.write(unique_df)

        if show_pairplot:
            st.subheader("Pair Plot")
            columns = data.select_dtypes(include=['float64', 'int64']).columns.tolist()
            selected_columns = st.multiselect("Select Columns for Pair Plot", columns)
            if len(selected_columns) > 1:
                fig = px.scatter_matrix(data[selected_columns])
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.warning("Please select at least two columns for the pair plot.")

        if show_correlation:
            st.subheader("Correlation Analysis")
            numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns.tolist()
            var = st.selectbox("Select Variable", numeric_columns, index=0, key='corr_var')
            corr_method = st.radio("Correlation Method", ("Pearson", "Spearman"))
            
            if corr_method == "Pearson":
                corr_matrix = data.corr(method='pearson')
            else:
                corr_matrix = data.corr(method='spearman')
            
            corr_with_var = corr_matrix[var].sort_values(ascending=False)
            st.write(corr_with_var)
        
        if show_crosstab:
            st.subheader("Crosstab Analysis")
            categorical_columns = data.select_dtypes(include=['object']).columns.tolist()
            if len(categorical_columns) >= 2:
                var1 = st.selectbox("Select Variable 1", categorical_columns, index=0, key='crosstab_var1')
                var2 = st.selectbox("Select Variable 2", categorical_columns, index=1, key='crosstab_var2')
                
                crosstab_count = pd.crosstab(data[var1], data[var2], margins=True)
                crosstab_pct = pd.crosstab(data[var1], data[var2], margins=True, normalize='all')
                
                crosstab_result = crosstab_count.astype(str) + " (" + crosstab_pct.applymap(lambda x: f"{x:.2%}") + ")"
                
                st.write("Crosstab Result (Count and Percentage):")
                st.write(crosstab_result)
                
                fig = px.imshow(crosstab_count, text_auto=True, aspect="auto")
                fig.update_layout(
                    xaxis_title=var2,
                    yaxis_title=var1
                )
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.warning("Please ensure the dataset has at least two categorical columns for Crosstab analysis.")


        if show_feature_scaling:
            st.subheader("Feature Scaling")
            numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns.tolist()
            selected_columns = st.multiselect("Select Columns for Scaling", numeric_columns)
            
            scaling_options = {
                "StandardScaler": StandardScaler(),
                "MinMaxScaler": MinMaxScaler(),
                "RobustScaler": RobustScaler(),
                "Normalizer": Normalizer()
            }
            
            selected_scaler = st.selectbox("Select Scaling Type", list(scaling_options.keys()))
            
            if len(selected_columns) > 0:
                scaler = scaling_options[selected_scaler]
                scaled_data = scaler.fit_transform(data[selected_columns])
                scaled_df = pd.DataFrame(scaled_data, columns=[f"{col}_scaled" for col in selected_columns])
                before_scaling_df = data[selected_columns]
                comparison_df = pd.concat([before_scaling_df, scaled_df], axis=1)
                st.write(comparison_df)
            else:
                st.warning("Please select at least one column for feature scaling.")

        if show_feature_selection:
            st.subheader("Feature Selection")
            numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns.tolist()
            target_column = st.selectbox("Select Target Column", numeric_columns)
            k = st.slider("Select Number of Top Features", min_value=1, max_value=len(numeric_columns), value=5)

            X = data.drop(columns=[target_column])
            y = data[target_column]

            selector = SelectKBest(score_func=f_regression, k=k)
            selector.fit(X, y)

            feature_scores = pd.DataFrame({'Feature': X.columns, 'Score': selector.scores_})
            feature_scores = feature_scores.sort_values(by='Score', ascending=False)

            st.write("Feature Importance Scores:")
            st.write(feature_scores)

            fig = px.bar(feature_scores, x='Feature', y='Score', title='Feature Importance Scores')
            st.plotly_chart(fig, use_container_width=True)

        if show_duplicates:
            st.subheader("Duplicate Rows")
            duplicates = data[data.duplicated()]
            if duplicates.empty:
                st.write("No duplicate rows found.")
            else:
                st.write(duplicates)

        if show_outliers:
            st.subheader("Outlier Detection")
            numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns.tolist()
            selected_column = st.selectbox("Select Column for Outlier Detection", numeric_columns)

            Q1 = data[selected_column].quantile(0.25)
            Q3 = data[selected_column].quantile(0.75)
            IQR = Q3 - Q1

            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            outliers = data[(data[selected_column] < lower_bound) | (data[selected_column] > upper_bound)]

            if outliers.empty:
                st.write("No outliers found in the selected column.")
            else:
                st.write("Outliers:")
                st.write(outliers)
        
        if show_pivot_table:
            st.subheader("Pivot Table")
            columns = data.columns.tolist()
            index_column = st.selectbox("Select Index Column", columns)
            value_column = st.selectbox("Select Value Column", columns)
            agg_func = st.selectbox("Select Aggregation Function", ["mean", "sum", "count"])

            pivot_table = pd.pivot_table(data, values=value_column, index=index_column, aggfunc=agg_func)

            st.write(pivot_table)

            fig = px.imshow(pivot_table, text_auto=True, aspect="auto")
            fig.update_layout(
                xaxis_title=value_column,
                yaxis_title=index_column
            )
            st.plotly_chart(fig, use_container_width=True)
        
        if show_wordcloud:
            st.subheader("Word Cloud")
            text_columns = data.select_dtypes(include=['object']).columns.tolist()
            selected_column = st.selectbox("Select Text Column for Word Cloud", text_columns)
            text = ' '.join(data[selected_column].astype(str))
            wordcloud = WordCloud(background_color='white').generate(text)
            plt.figure(figsize=(10, 8))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis('off')
            st.pyplot(plt)

        if show_parallel_coordinates:
            st.subheader("Parallel Coordinates Plot")
            numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns.tolist()
            selected_columns = st.multiselect("Select Columns for Parallel Coordinates Plot", numeric_columns)
            if len(selected_columns) > 1:
                fig = px.parallel_coordinates(data, dimensions=selected_columns)
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.warning("Please select at least two columns for the parallel coordinates plot.")

        if show_bubble:
            st.subheader("Bubble Plot")
            numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns.tolist()
            x_column = st.selectbox("Select X-axis Column", numeric_columns)
            y_column = st.selectbox("Select Y-axis Column", numeric_columns)
            size_column = st.selectbox("Select Size Column", numeric_columns)
            fig = px.scatter(data, x=x_column, y=y_column, size=size_column)
            st.plotly_chart(fig, use_container_width=True)

        if show_piechart:
            st.subheader("Pie Chart")
            categorical_columns = data.select_dtypes(include=['object']).columns.tolist()
            selected_column = st.selectbox("Select Column for Pie Chart", categorical_columns)
            fig = px.pie(data, names=selected_column)
            st.plotly_chart(fig, use_container_width=True)

        if show_treemap:
            st.subheader("Treemap")
            categorical_columns = data.select_dtypes(include=['object']).columns.tolist()
            selected_column = st.selectbox("Select Column for Treemap", categorical_columns)
            fig = px.treemap(data, path=[selected_column])
            st.plotly_chart(fig, use_container_width=True)
        if show_3d_scatter:
            st.subheader("3D Scatter Plot")
            numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns.tolist()
            x_column = st.selectbox("Select X-axis Column", numeric_columns, key='3d_scatter_x')
            y_column = st.selectbox("Select Y-axis Column", numeric_columns, key='3d_scatter_y')
            z_column = st.selectbox("Select Z-axis Column", numeric_columns, key='3d_scatter_z')
            color_column = st.selectbox("Select Color Column", ["None"] + numeric_columns, key='3d_scatter_color')
            
            if color_column == "None":
                fig = px.scatter_3d(data, x=x_column, y=y_column, z=z_column)
            else:
                fig = px.scatter_3d(data, x=x_column, y=y_column, z=z_column, color=color_column)
            
            st.plotly_chart(fig, use_container_width=True)

        if show_3d_kmeans:
            st.subheader("3D K-Means Clustering")
            numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns.tolist()
            x_column = st.selectbox("Select X-axis Column", numeric_columns, key='3d_kmeans_x')
            y_column = st.selectbox("Select Y-axis Column", numeric_columns, key='3d_kmeans_y')
            z_column = st.selectbox("Select Z-axis Column", numeric_columns, key='3d_kmeans_z')
            n_clusters = st.number_input("Select Number of Clusters", min_value=2, max_value=10, value=3, step=1)
            
            X = data[[x_column, y_column, z_column]]
            kmeans = KMeans(n_clusters=n_clusters, random_state=42)
            kmeans.fit(X)
            labels = kmeans.labels_
            
            fig = px.scatter_3d(data, x=x_column, y=y_column, z=z_column, color=labels.astype(str))
            st.plotly_chart(fig, use_container_width=True)

    else:
        st.info('Waiting for CSV file to be uploaded.')

if __name__ == "__main__":
    main()
