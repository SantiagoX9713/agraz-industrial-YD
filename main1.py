import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


root = tk.Tk()
# simulate data
# =============================
np.random.seed(1234)
df = pd.DataFrame({'px_last': 100 + np.random.randn(1000).cumsum()}, index=pd.date_range('2010-01-01', periods=1000, freq='B'))
df['50dma'] = pd.rolling_mean(df['px_last'], window=50)
df['200dma'] = pd.rolling_mean(df['px_last'], window=200)
df['label'] = np.where(df['50dma'] > df['200dma'], 1, -1)


# plot
# =============================
df = df.dropna(axis=0, how='any')

fig, ax = plt.subplots()

def plot_func(group):
    global ax
    color = 'r' if (group['label'] < 0).all() else 'g'
    lw = 2.0
    ax.plot(group.index, group.px_last, c=color, linewidth=lw)

df.groupby((df['label'].shift() * df['label'] < 0).cumsum()).apply(plot_func)

# add ma lines
ax.plot(df.index, df['50dma'], 'k--', label='MA-50')
ax.plot(df.index, df['200dma'], 'b--', label='MA-200')
ax.legend(loc='best')

root.mainloop()