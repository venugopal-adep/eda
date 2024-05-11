import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3.0, 3.0, 100)
y = np.linspace(-3.0, 3.0, 100)
X, Y = np.meshgrid(x, y)
Z = np.sqrt(X**2 + Y**2)

fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)

ax.clabel(CS, inline=True, fontsize=10)
ax.set_title('Contour Plot')
ax.set_xlabel('X')
ax.set_ylabel('Y')

st.pyplot(fig)
