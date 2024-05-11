import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

n = 50
x = np.random.rand(n)
y = np.random.rand(n)
colors = np.random.rand(n)
area = np.pi * (15 * np.random.rand(n))**2  # Bubble size

fig, ax = plt.subplots()
bubble = ax.scatter(x, y, s=area, c=colors, alpha=0.5)

slider_val = st.slider("Change the bubble size scale", 0.5, 2.0, 1.0)
bubble.set_sizes(area * slider_val)

ax.set_xlabel('X Value')
ax.set_ylabel('Y Value')
ax.set_title('Interactive Bubble Chart')

st.pyplot(fig)
