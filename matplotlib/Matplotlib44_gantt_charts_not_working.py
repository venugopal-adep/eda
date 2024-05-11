import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

# Data setup
tasks = {
    "Task 1": ("2021-01-01", "2021-01-10"),
    "Task 2": ("2021-01-05", "2021-01-15"),
    "Task 3": ("2021-01-10", "2021-01-20")
}
df = pd.DataFrame(tasks, index=["Start", "Finish"]).T
df["Start"] = pd.to_datetime(df["Start"])
df["Finish"] = pd.to_datetime(df["Finish"])

fig, ax = plt.subplots()
for i, task in enumerate(df.index):
    ax.barh(task, (df.loc[task, "Finish"] - df.loc[task, "Start"]).days, left=df.loc[task, "Start"].day, color='cyan')

ax.set_title('Gantt Chart for Project Management')
ax.set_xlabel('Days in January 2021')
ax.set_ylabel('Tasks')
ax.xaxis.set_major_locator(mdates.DayLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d'))

st.pyplot(fig)
