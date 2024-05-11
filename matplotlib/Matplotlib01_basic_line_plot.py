import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Basic Line Plot')
ax.set_xlabel('x')
ax.set_ylabel('sin(x)')

st.pyplot(fig)
