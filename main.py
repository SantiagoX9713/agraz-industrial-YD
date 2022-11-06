import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
import matplotlib.pyplot as plt
from YDdata.get_csv import get_csv_ftp, df_from_csv

# def filter_by_time(df,h):
#     now = datetime.now()
#     print(now)
#     df = df[(canal1.Time > (now - timedelta(hours=h)).time())]
#     return df

# df = filter_by_time(canal1, 10)
getter = get_csv_ftp()
getter.conect()
prepared_data = df_from_csv()



class my_tk(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure(bg='black')
        self.state("zoomed")
        self.wm_title("YoDiagnostico")

root = my_tk()

fig = plt.Figure(figsize=(5,4), dpi=100)
fig.patch.set_facecolor('black')
ax = fig.add_subplot()
df2 = prepared_data.canal1[['Time','Solt Mec']]
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
root.mainloop()