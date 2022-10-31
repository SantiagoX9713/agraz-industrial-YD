import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
from matplotlib.backend_bases import key_press_handler
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta
from time import sleep
from ftplib import FTP

def progress(percent=0, width=40):
    left = width * percent // 100
    right = width - left
    
    tags = "#" * left
    spaces = " " * right
    percents = f"{percent:.0f}% Progress"
    
    print("\r[", tags, spaces, "]", percents, sep="", end="", flush=True)


HOST = "localhost"
ftp = FTP()
ftp.connect(HOST)
ftp.login(user='Usuario FTP', passwd='123456')
print(ftp.retrlines('LIST'))
for i in range(101):
    progress(i)
    sleep(0.05)

with open('DDSMuestras.csv', 'wb') as fp:
    ftp.retrbinary('RETR DDSMuestras.csv', fp.write)
ftp.close()



origin = pd.read_csv('DDSMuestras.CSV', delimiter='\t', encoding='utf-16', parse_dates=[['Date', 'Time']])
columnas = ['Date_Time','Global','Desbalance','Desalineamiento','Solt Mec','Acc', 'Hd Env', 'Date', 'Time']
canal1 = origin[['Date_Time', 'Ch 1 Global','Ch 1 Desbalance','Ch 1 Desalineamiento', 'Ch 1 Solt Mec', 'Ch 1 Acc', 'Ch 1 Hd Env']].copy()
canal2 = origin[['Date_Time', 'Ch 2 Global','Ch 2 Desbalance','Ch 2 Desalineamiento', 'Ch 2 Solt Mec', 'Ch 2 Acc', 'Ch 2 Hd Env']].copy()
canal3 = origin[['Date_Time', 'Ch 3 Global','Ch 3 Desbalance','Ch 3 Desalineamiento', 'Ch 3 Solt Mec', 'Ch 3 Acc', 'Ch 3 Hd Env']].copy()
canal4 = origin[['Date_Time', 'Ch 4 Global','Ch 4 Desbalance','Ch 4 Desalineamiento', 'Ch 4 Solt Mec', 'Ch 4 Acc', 'Ch 4 Hd Env']].copy()
canal1['Date'] = pd.to_datetime(canal1['Date_Time']).dt.date
canal1['Time'] = pd.to_datetime(canal1['Date_Time']).dt.time
canal1.columns = columnas
canal2['Date'] = pd.to_datetime(canal2['Date_Time']).dt.date
canal2['Time'] = pd.to_datetime(canal2['Date_Time']).dt.time
canal2.columns = columnas
canal3['Date'] = pd.to_datetime(canal3['Date_Time']).dt.date
canal3['Time'] = pd.to_datetime(canal3['Date_Time']).dt.time
canal3.columns = columnas
canal4['Date'] = pd.to_datetime(canal4['Date_Time']).dt.date
canal4['Time'] = pd.to_datetime(canal4['Date_Time']).dt.time
canal4.columns = columnas


def filter_by_time(df,h):
    now = datetime.now()
    print(now)
    df = df[(canal1.Time > (now - timedelta(hours=h)).time())]
    return df

df = filter_by_time(canal1, 10)

root = tk.Tk()
root.configure(bg='black')
root.state("zoomed")
# root.attributes('-fullscreen', True)
root.wm_title("YoDiagnostico")




fig = plt.Figure(figsize=(5,4), dpi=100)
fig.patch.set_facecolor('black')
ax = fig.add_subplot()
df2 = df[['Time','Solt Mec']]
colors = ["red" if i > 2.72 else "yellow" for i in df2['Solt Mec']]
df2.plot.line(legend=True, ax=ax, color=colors, fontsize=16, grid=True)
ax.axhline(y=2.81, color='r', linestyle='-')
ax.axhline(y=2.70, color='b', linestyle='-')
ax.set_title('Solturas Mecánicas')
ax.set_ylim([2.6,2.85])
ax.set_facecolor('black')
[t.set_color('white') for t in ax.xaxis.get_ticklines()]
[t.set_color('white') for t in ax.xaxis.get_ticklabels()]
[t.set_color('white') for t in ax.yaxis.get_ticklines()]
[t.set_color('white') for t in ax.yaxis.get_ticklabels()]
ax.spines['bottom'].set_color('white')
ax.spines['top'].set_color('white')
ax.spines['right'].set_color('white')
ax.spines['left'].set_color('white')



canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()

toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
toolbar.update()

canvas.mpl_connect(
    "key_press_event", lambda event: print(f"you pressed {event.key}"))
canvas.mpl_connect("key_press_event", key_press_handler)

button_quit = tk.Button(master=root, text="Quit", command=root.destroy)


button_quit.pack(side=tk.BOTTOM)
toolbar.pack(side=tk.BOTTOM, fill=tk.X)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

tk.mainloop()
