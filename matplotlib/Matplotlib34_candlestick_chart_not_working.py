import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc
import pandas as pd
import datetime

# Mock data
data = {
    'Date': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04'],
    'Open': [100, 101, 102, 103],
    'High': [110, 111, 112, 113],
    'Low': [90, 91, 92, 93],
    'Close': [105, 106, 107, 108]
}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = df['Date'].apply(mdates.date2num)

fig, ax = plt.subplots()
candlestick_ohlc(ax, df.values, width=0.6)

ax.xaxis_date()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

st.pyplot(fig)
