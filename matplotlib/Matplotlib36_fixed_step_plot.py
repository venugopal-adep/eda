import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 6, 1)
y = np.random.randint(1, 10, size=5)

fig, ax = plt.subplots()
ax.step(x, y, where='mid', label='Step Data')
ax.fill_between(x, y, step='mid', alpha=0.4)

ax.set_title('Filled Step Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.legend()

st.pyplot(fig)
