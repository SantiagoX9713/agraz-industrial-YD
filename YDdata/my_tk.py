import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

class my_tk(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure(bg='black')
        self.state("zoomed")
        self.wm_title("YoDiagnostico")
        

    def reset_data(self, new_data):
        self.__init__(new_data)
        # self.fig.canvas.draw_idle()
        print('refreshed')







def create_plot(container, prepared_data):
    rec = ttk.Frame(container)
    rec.columnconfigure(0, weight=1)
    rec.columnconfigure(0, weight=3)
    fig = plt.Figure(figsize=(5,4), dpi=100)
    fig.patch.set_facecolor('black')
    ax = fig.add_subplot()
    df2 = prepared_data.canal2[['Time','Solt Mec']]
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
    canvas = FigureCanvasTkAgg(fig, master=rec)  # A tk.DrawingArea.
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas, rec, pack_toolbar=False)
    toolbar.update()
    toolbar.pack(side=tk.BOTTOM, fill=tk.X)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    return rec