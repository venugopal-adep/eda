import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)
errors = np.random.normal(0.1, 0.02, size=y.shape)

fig, ax = plt.subplots()
line, = ax.plot(x, y, label='Sin(x)')
ax.fill_between(x, y - errors, y + errors, alpha=0.2)
line.set_label('Sin(x) with error')

ax.legend(loc='upper right', shadow=True, fancybox=True, borderpad=2)
ax.set_title('Customizing Plot Legends')
ax.set_xlabel('X')
ax.set_ylabel('Y')

st.pyplot(fig)
