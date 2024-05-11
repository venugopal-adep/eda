import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Generate data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots()
ax.plot(x, y1, label='sin(x)')
ax.plot(x, y2, label='cos(x)')
ax.set_title('Multiple Lines on a Plot')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()

st.pyplot(fig)

