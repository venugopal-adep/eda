import streamlit as st
import matplotlib.pyplot as plt

# Data
categories = ['Apples', 'Bananas', 'Cherries', 'Dates']
values = [15, 30, 7, 22]

fig, ax = plt.subplots()
ax.bar(categories, values)
ax.set_title('Bar Chart')
ax.set_xlabel('Fruit')
ax.set_ylabel('Quantity')

st.pyplot(fig)
