import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Sample data
changes = [100, -20, -15, 5, -10, 15, -5, 10, -5, 105]
index = ['Start', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'End']
positive = np.maximum(changes, 0)
negative = np.minimum(changes, 0)

fig, ax = plt.subplots()
ax.bar(index, positive, 0.4, color='g')
ax.bar(index, negative, 0.4, color='r')

ax.set_title('Waterfall Chart')
ax.set_ylabel('Value')
ax.set_xlabel('Event')

st.pyplot(fig)
