import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(10, 10)

fig, ax = plt.subplots()
cax = ax.matshow(data, interpolation='nearest')
fig.colorbar(cax)

ax.set_title('Heatmap Example')
st.pyplot(fig)
