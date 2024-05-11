import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

data = np.random.randn(1000)
mu, std = norm.fit(data)

fig, ax = plt.subplots()
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
ax.plot(x, p, 'k', linewidth=2)

title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)
ax.set_title(title)
ax.set_xlabel('Data values')
ax.set_ylabel('Probability')

st.pyplot(fig)
