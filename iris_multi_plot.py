import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import altair as alt

# Load the Iris dataset
iris = sns.load_dataset('iris')

# Set up the Streamlit app
st.title('Iris Dataset Visualization')
st.markdown('Venugopal Adep')

# Create dropdown menus for plotting library and plot type
library = st.selectbox('Select a plotting library', ['matplotlib', 'seaborn', 'plotly', 'altair'])
plot_type = st.selectbox('Select a plot type', ['bar plot', 'violin plot', 'swarm plot', 'scatter plot', 'line plot'])

# Create the plot based on the selected library and plot type
if library == 'matplotlib':
    fig, ax = plt.subplots(figsize=(8, 6))
    if plot_type == 'bar plot':
        iris.groupby('species').mean().plot(kind='bar', ax=ax)
    elif plot_type == 'violin plot':
        data = [iris[col] for col in iris.columns[:-1]]
        ax.violinplot(data, showmeans=True)
        ax.set_xticks(range(1, len(iris.columns[:-1]) + 1))
        ax.set_xticklabels(iris.columns[:-1])
    elif plot_type == 'swarm plot':
        sns.swarmplot(data=iris, x='species', y='sepal_length', ax=ax)
    elif plot_type == 'scatter plot':
        iris.plot(kind='scatter', x='sepal_length', y='sepal_width', ax=ax)
    elif plot_type == 'line plot':
        iris.groupby('species').mean().plot(kind='line', ax=ax)
    st.pyplot(fig)

elif library == 'seaborn':
    if plot_type == 'bar plot':
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.barplot(data=iris, x='species', y='sepal_length', ax=ax)
        st.pyplot(fig)
    elif plot_type == 'violin plot':
        fig = sns.catplot(data=iris, x='species', y='sepal_length', kind='violin', aspect=1.5)
        st.pyplot(fig)
    elif plot_type == 'swarm plot':
        fig = sns.catplot(data=iris, x='species', y='sepal_length', kind='swarm', aspect=1.5)
        st.pyplot(fig)
    elif plot_type == 'scatter plot':
        fig = sns.relplot(data=iris, x='sepal_length', y='sepal_width', hue='species', aspect=1.5)
        st.pyplot(fig)
    elif plot_type == 'line plot':
        fig = sns.relplot(data=iris, x='sepal_length', y='sepal_width', hue='species', kind='line', aspect=1.5)
        st.pyplot(fig)

elif library == 'plotly':
    if plot_type == 'bar plot':
        fig = px.bar(iris.groupby('species').mean().reset_index(), x='species', y=iris.columns[:-1], barmode='group')
    elif plot_type == 'violin plot':
        fig = px.violin(iris, x='species', y='sepal_length', box=True, points='all')
    elif plot_type == 'swarm plot':
        fig = px.strip(iris, x='species', y='sepal_length')
    elif plot_type == 'scatter plot':
        fig = px.scatter(iris, x='sepal_length', y='sepal_width', color='species')
    elif plot_type == 'line plot':
        fig = px.line(iris.groupby('species').mean().reset_index(), x='species', y=iris.columns[:-1])
    st.plotly_chart(fig)

elif library == 'altair':
    if plot_type == 'bar plot':
        chart = alt.Chart(iris).mark_bar().encode(x='species', y='average(sepal_length)')
    elif plot_type == 'violin plot':
        chart = alt.Chart(iris).transform_density('sepal_length', as_=['sepal_length', 'density'], groupby=['species']).mark_area(orient='horizontal').encode(y='sepal_length:Q', color='species:N', x=alt.X('density:Q', stack='center', impute=None), column=alt.Column(field='species', type='nominal'), row=alt.Row(field='species', type='nominal')).properties(width=100)
    elif plot_type == 'swarm plot':
        chart = alt.Chart(iris).mark_circle().encode(x='species', y='sepal_length', color='species', tooltip=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
    elif plot_type == 'scatter plot':
        chart = alt.Chart(iris).mark_point().encode(x='sepal_length', y='sepal_width', color='species', tooltip=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
    elif plot_type == 'line plot':
        chart = alt.Chart(iris.groupby('species').mean().reset_index()).mark_line().encode(x='species', y='sepal_length', color='species')
    st.altair_chart(chart, use_container_width=True)
