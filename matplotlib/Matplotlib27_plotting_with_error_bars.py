import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 1)
y = np.log(x + 1)
yerr = 0.1 + 0.2*np.sqrt(x)

fig, ax = plt.subplots()
ax.errorbar(x, y, yerr=yerr, fmt='-o', ecolor='red', capsize=5)

ax.set_title('Plotting with Error Bars')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

st.pyplot(fig)
