import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

Y, X = np.mgrid[-3:3:100j, -3:3:100j]
U = -1 - X**2 + Y
V = 1 + X - Y**2

fig, ax = plt.subplots()
strm = ax.streamplot(X, Y, U, V, color=U, linewidth=2, cmap='autumn')
fig.colorbar(strm.lines)

ax.set_title('Streamplot')
ax.set_xlabel('X')
ax.set_ylabel('Y')

st.pyplot(fig)
