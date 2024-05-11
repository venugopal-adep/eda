import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(10, 10)

fig, ax = plt.subplots()
heatmap = ax.imshow(data, cmap='coolwarm')

# Add color bar
cbar = fig.colorbar(heatmap)
cbar.set_label('Intensity')

# Apply conditional formatting
heatmap.set_clim(-1, 1)  # Set the range of colors

ax.set_title('Conditional Formatting in Heatmaps')
ax.set_xlabel('Variable X')
ax.set_ylabel('Variable Y')

st.pyplot(fig)
