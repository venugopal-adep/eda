import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Generate data
x = np.random.rand(50)
y = np.random.rand(50)

fig, ax = plt.subplots()
ax.scatter(x, y)
ax.set_title('Scatter Plot')
ax.set_xlabel('x')
ax.set_ylabel('y')

st.pyplot(fig)
