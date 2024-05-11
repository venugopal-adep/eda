import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.1, 15, 400)
y = x ** 2

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_yscale('log')

ax.set_title('Logarithmic Scale Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis (log scale)')

st.pyplot(fig)
