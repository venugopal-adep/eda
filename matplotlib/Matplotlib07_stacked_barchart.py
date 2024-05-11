import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['Q1', 'Q2', 'Q3', 'Q4']
men_means = [20, 35, 30, 35]
women_means = [25, 32, 34, 20]
children_means = [30, 32, 34, 20]

x = np.arange(len(labels))  # the label locations

fig, ax = plt.subplots()
ax.bar(x - 0.2, men_means, 0.2, label='Men')
ax.bar(x, women_means, 0.2, label='Women', bottom=men_means)
ax.bar(x + 0.2, children_means, 0.2, label='Children', bottom=np.array(men_means)+np.array(women_means))

ax.set_xlabel('Quarters')
ax.set_ylabel('Scores')
ax.set_title('Scores by group and quarter')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

st.pyplot(fig)
