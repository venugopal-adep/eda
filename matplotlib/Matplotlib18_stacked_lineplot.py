import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Time series data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.cos(x)

fig, ax = plt.subplots()
ax.stackplot(x, y1, y2, y3, labels=['sin(x)', 'cos(x)', 'sin(x)*cos(x)'])
ax.legend(loc='upper right')
ax.set_title('Stacked Line Plot')
ax.set_xlabel('X')
ax.set_ylabel('Y')

st.pyplot(fig)
