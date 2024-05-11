import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(2, 2, figsize=(10, 10))  # 2x2 grid
t = np.arange(0.0, 2.0, 0.01)

axs[0, 0].plot(t, np.sin(2 * np.pi * t))
axs[0, 0].set_title('Sin Wave')

axs[0, 1].plot(t, np.cos(2 * np.pi * t))
axs[0, 1].set_title('Cos Wave')

axs[1, 0].plot(t, np.tan(2 * np.pi * t))
axs[1, 0].set_title('Tan Wave')

axs[1, 1].plot(t, np.arctan(2 * np.pi * t))
axs[1, 1].set_title('ArcTan Wave')

for ax in axs.flat:
    ax.set(xlabel='Time (s)', ylabel='Magnitude')
    ax.label_outer()  # Hide x labels and tick labels for top plots and y ticks for right plots.

st.pyplot(fig)
