import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Data generation
data = [np.random.normal(0, std, 100) for std in range(1, 5)]

fig, ax = plt.subplots()
ax.violinplot(data, showmeans=False, showmedians=True)
ax.set_title('Violin Plot')
ax.set_xlabel('Category')
ax.set_ylabel('Value')

st.pyplot(fig)
