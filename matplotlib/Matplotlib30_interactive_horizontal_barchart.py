import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

categories = ['Apples', 'Bananas', 'Oranges', 'Berries', 'Melons']
values = [20, 35, 30, 35, 27]

fig, ax = plt.subplots()
bars = ax.barh(categories, values)

def update_chart():
    for i, bar in enumerate(bars):
        bar.set_width(values[i])

if st.button('Shuffle Values'):
    np.random.shuffle(values)
    update_chart()

st.pyplot(fig)
