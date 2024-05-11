import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)

# Customizing tick labels and styles
ax.xaxis.set_tick_params(rotation=45, labelcolor='red')
ax.yaxis.set_tick_params(length=10, width=2, colors='blue')
ax.grid(True, linestyle='--', color='gray', alpha=0.6)

ax.set_title('Advanced Customization of Matplotlib Figures')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

st.pyplot(fig)
