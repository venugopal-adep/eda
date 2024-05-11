import streamlit as st
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 2, 3])

def on_click(event):
    if event.dblclick:
        ax.plot([event.xdata], [event.ydata], 'ro')
        st.pyplot(fig)

fig.canvas.mpl_connect('button_press_event', on_click)

ax.set_title('Interactive Plot with Event Handling')
ax.set_xlabel('X')
ax.set_ylabel('Y')

st.pyplot(fig)
