import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(100)
y = np.random.rand(100)
colors = np.random.rand(100)
sizes = 1000 * np.random.rand(100)

fig, ax = plt.subplots()
scatter = ax.scatter(x, y, c=colors, s=sizes, alpha=0.5)

selected_index = st.slider("Select index of data point", 0, len(x)-1, 0)
highlighted = ax.scatter(x[selected_index], y[selected_index], color='red')

ax.set_title('Interactive Data Selection')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

st.pyplot(fig)
