import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y, label='Sin(x)')
ax.axvspan(2, 4, color='yellow', alpha=0.3, label='Highlight Region')

ax.set_title('Time Series with Highlighted Regions')
ax.set_xlabel('Time')
ax.set_ylabel('Amplitude')
ax.legend()

st.pyplot(fig)
