import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Data setup
labels = ['Q1', 'Q2', 'Q3', 'Q4']
men_means = [20, 35, 30, 35]
women_means = [25, 32, 34, 20]
children_means = [30, 32, 34, 20]

x = np.arange(len(labels))  # Label locations
width = 0.2  # Width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, men_means, width, label='Men')
rects2 = ax.bar(x, women_means, width, label='Women')
rects3 = ax.bar(x + width, children_means, width, label='Children')

ax.set_xlabel('Quarter')
ax.set_ylabel('Scores')
ax.set_title('Scores by group and quarter')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

st.pyplot(fig)
