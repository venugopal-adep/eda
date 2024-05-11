import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Generate data
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

fig, ax = plt.subplots()
ax.boxplot(data, vert=True, patch_artist=True)
ax.set_title('Box plot')
ax.set_xlabel('Category')
ax.set_ylabel('Values')

st.pyplot(fig)
