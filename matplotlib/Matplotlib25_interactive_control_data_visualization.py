import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
line, = ax.plot(x, y)

amp = st.sidebar.slider("Amplitude", 0.1, 1.0, 0.5)
freq = st.sidebar.slider("Frequency", 1, 10, 1)
color = st.sidebar.color_picker("Pick a color", '#0055ff')

def update_plot():
    y = amp * np.sin(freq * x)
    line.set_ydata(y)
    line.set_color(color)
    st.pyplot(fig)

if st.sidebar.button("Update Plot"):
    update_plot()

ax.set_title('Custom Interactive Controls for Data Visualization')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
