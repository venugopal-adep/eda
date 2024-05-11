import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(2, 2)  # 2x2 grid of subplots

x = np.linspace(0, 2 * np.pi, 100)
axs[0, 0].plot(x, np.sin(x))
axs[0, 0].set_title('Sin(x)')

axs[0, 1].plot(x, np.cos(x))
axs[0, 1].set_title('Cos(x)')

axs[1, 0].plot(x, np.tan(x))
axs[1, 0].set_title('Tan(x)')

axs[1, 1].plot(x, np.arctan(x))
axs[1, 1].set_title('Arctan(x)')

for ax in axs.flat:
    ax.set(xlabel='x', ylabel='y')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()

st.pyplot(fig)
