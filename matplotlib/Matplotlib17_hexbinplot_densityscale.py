import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

x = np.random.standard_normal(1000)
y = 2 + 3 * x + 4 * np.random.standard_normal(1000)

fig, ax = plt.subplots()
hb = ax.hexbin(x, y, gridsize=50, cmap='inferno')
ax.grid(True)

cb = fig.colorbar(hb, ax=ax)
cb.set_label('counts')

ax.set_title('Hexbin Plot with Density Scale')
ax.set_xlabel('X')
ax.set_ylabel('Y')

st.pyplot(fig)
