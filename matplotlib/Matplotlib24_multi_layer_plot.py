import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots()
ax.plot(x, y1, label='Sin(x)')
ax.scatter(x, y2, color='red', label='Cos(x) Points')
ax.legend()

ax.set_title('Multi-layer Plots')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

st.pyplot(fig)
