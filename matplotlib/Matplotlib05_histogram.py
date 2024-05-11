import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Generate data
data = np.random.normal(0, 1, 1000)

fig, ax = plt.subplots()
ax.hist(data, bins=30)
ax.set_title('Histogram')
ax.set_xlabel('Value')
ax.set_ylabel('Frequency')

st.pyplot(fig)
