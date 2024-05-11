import streamlit as st
import matplotlib.pyplot as plt

# Data
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
sizes = [215, 130, 245, 210]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig)
