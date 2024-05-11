import streamlit as st
import matplotlib.pyplot as plt

# Initial data
labels = ['Red', 'Blue', 'Green', 'Yellow']
sizes = [215, 130, 245, 210]

fig, ax = plt.subplots()
pie = ax.pie(sizes, labels=labels, autopct='%1.1f%%')[0]  # Storing only the first element of the returned tuple

def update_pie(new_size):
    for wedge, size in zip(pie, new_size):
        wedge.set_radius(size)  # Update the sizes of the existing pie chart
    st.pyplot(fig)

new_sizes = st.slider("Adjust the sizes:", 100, 300, 215, step=10)  # Pass a single value to the slider
if st.button("Update Chart"):
    update_pie([new_sizes] * len(labels))  # Convert the single value to a list for each label
