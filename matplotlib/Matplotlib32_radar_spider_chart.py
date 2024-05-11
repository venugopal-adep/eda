import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

labels=np.array(['A', 'B', 'C', 'D'])
stats=np.array([20, 34, 30, 35])

angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()

stats=np.concatenate((stats,[stats[0]]))
angles+=angles[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, stats, color='red', alpha=0.25)
ax.plot(angles, stats, color='red', marker='o')  # Line plot

ax.set_yticklabels([])
ax.set_thetagrids(np.degrees(angles[:-1]), labels)

st.pyplot(fig)
