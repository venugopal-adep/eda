import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

x = np.random.rand(5)
bars = ax.bar(range(5), x)

def update_bars():
    for bar in bars:
        bar.set_height(np.random.rand())
    st.pyplot(fig)

if st.button('Update Data'):
    update_bars()

ax.set_title('Dynamic Bar Chart Race')
ax.set_xlabel('Categories')
ax.set_ylabel('Values')

st.pyplot(fig)
