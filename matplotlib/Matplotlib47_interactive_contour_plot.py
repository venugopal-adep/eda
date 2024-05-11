import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3.0, 3.0, 100)
y = np.linspace(-3.0, 3.0, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

fig, ax = plt.subplots()

levels = st.slider("Select contour levels", 5, 50, 20)
contour = ax.contourf(X, Y, Z, levels=levels, cmap='viridis')

# Add color bar
fig.colorbar(contour)

ax.set_title('Interactive Contour Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

st.pyplot(fig)
