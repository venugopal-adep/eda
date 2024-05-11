import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y, label='Sin(x)')
ax.annotate('Local max', xy=(1.57, 1), xytext=(2, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05))

ax.set_title('Complex Line Plot with Annotations')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.legend()

st.pyplot(fig)
