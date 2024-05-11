import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.linspace(0, 100, 100)

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('X-axis')
ax1.set_ylabel('Sin(X)', color=color)
ax1.plot(x, y1, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Linear', color=color)
ax2.plot(x, y2, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
ax1.set_title('Multiple Y-Axis Plot')

st.pyplot(fig)
