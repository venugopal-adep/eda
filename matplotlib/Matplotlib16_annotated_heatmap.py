import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Data generation
data = np.random.rand(10, 10)

fig, ax = plt.subplots()
cax = ax.matshow(data, cmap='coolwarm')

# Adding annotations
for (i, j), val in np.ndenumerate(data):
    ax.text(j, i, f"{val:.2f}", ha='center', va='center', color='white')

fig.colorbar(cax)
ax.set_title('Annotated Heatmap')

st.pyplot(fig)
