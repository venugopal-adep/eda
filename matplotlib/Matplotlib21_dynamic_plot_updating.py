import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
line, = ax.plot(x, y)

def update_plot(amp, freq):
    y = amp * np.sin(freq * x)
    line.set_ydata(y)
    ax.relim()
    ax.autoscale_view()
    st.pyplot(fig)

amp = st.slider("Amplitude", 0.1, 1.0, 0.5)
freq = st.slider("Frequency", 1, 10, 1)

update_plot(amp, freq)
