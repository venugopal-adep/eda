import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Generate data
r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, r)

ax.set_title('Polar Plot')
ax.set_xlabel('Angle (radians)')
ax.set_ylabel('Radius')

st.pyplot(fig)
