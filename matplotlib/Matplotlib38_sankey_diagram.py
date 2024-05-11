import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey

fig, ax = plt.subplots()
sankey = Sankey(ax=ax, scale=0.01)
sankey.add(flows=[1, -1], labels=['input', 'output'], orientations=[-1, 1])
sankey.finish()

ax.set_title('Sankey Diagram')
st.pyplot(fig)
