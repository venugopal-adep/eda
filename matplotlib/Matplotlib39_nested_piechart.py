import streamlit as st
import matplotlib.pyplot as plt

# Data setup
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
explode = (0, 0.1, 0, 0)  

fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, colors=colors,
       autopct='%1.1f%%', shadow=True, startangle=90)

# Insert a smaller pie
sizes = [5, 10, 15, 70]
ax.pie(sizes, radius=0.7, startangle=90, colors=colors, autopct='%1.1f%%')

ax.set(aspect="equal", title='Nested Pie Chart')
st.pyplot(fig)
