import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.cos(x)

fig, axs = plt.subplots(nrows=2, ncols=1)
axs[0].fill_between(x, y1, color="skyblue", alpha=0.4, label='Sin(x)')
axs[0].fill_between(x, y2, color="sandybrown", alpha=0.5, label='Cos(x)', bottom=y1)
axs[0].set_title('Stacked Area Plot')
axs[0].legend()

axs[1].fill_between(x, y1, color="skyblue", alpha=0.4, label='Sin(x)')
axs[1].fill_between(x, y2, color="sandybrown", alpha=0.5, label='Cos(x)')
axs[1].set_title('Unstacked Area Plot')
axs[1].legend()

st.pyplot(fig)
