from functools import partial
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from .get_csv import DfFromCsv
from .gauge_test import gauge
import plotly.graph_objects as go





class MyTk(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure(bg='black')
        self.state("zoomed")
        self.wm_title("YoDiagnostico")
        
        self.prepared_data = DfFromCsv()
        menu_bar = tk.Menu()
        menu_bar.winfo_name = 'MENU'
        
        menu_chart = tk.Menu(menu_bar, tearoff=False)
        menu_chart.add_command(label="Canal 1", command=self.channel_1)
        menu_chart.add_command(label="Canal 2", command=self.channel_2)
        menu_chart.add_command(label="Canal 3", command=self.channel_3)
        menu_chart.add_command(label="Canal 4", command=self.channel_4)
        menu_chart.add_command(label="Gauge", command=self.gauge)
        menu_chart.add_command(label="Salir", command=self.destroy_all)
        
        menu_bar.add_cascade(menu=menu_chart, label="Principal")
        

        menu_config = tk.Menu(menu_bar, tearoff=False)
        menu_config.add_command(label="Configuración", command=self.show_config)
        
        menu_bar.add_cascade(menu=menu_config, label="Config")
        
        self.config(menu=menu_bar)
        
    def destroy_all(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()

    def destroy_widgets(self):
        for widget in self.winfo_children():
            if widget.winfo_name != 'MENU':
                widget.destroy()


    def create_plot(self, container, prepared_data):
        # for widget in container.winfo_children():
        #     widget.destroy()

        frame = ttk.Frame(container)
        frame.columnconfigure(0, weight=1)
        frame.winfo_name = 'PLOTER'
        fig = plt.Figure(figsize=(7,5), dpi=120)
        fig.patch.set_facecolor('black')
        ax = fig.add_subplot()
        df2 = prepared_data[['Time','Solt Mec']]
        #colors = ["red" if i > 2.72 else "yellow" for i in df2['Solt Mec']]
        df2.plot.line(legend=True, ax=ax, fontsize=16, grid=True)
        # ax.axhline(y=2.81, color='r', linestyle='-')
        # ax.axhline(y=2.70, color='b', linestyle='-')
        # ax.set_title('Solturas Mecánicas')
        #ax.set_ylim([2.6,2.85])
        ax.set_facecolor('black')
        [t.set_color('white') for t in ax.xaxis.get_ticklines()]
        [t.set_color('white') for t in ax.xaxis.get_ticklabels()]
        [t.set_color('white') for t in ax.yaxis.get_ticklines()]
        [t.set_color('white') for t in ax.yaxis.get_ticklabels()]
        ax.spines['bottom'].set_color('white')
        ax.spines['top'].set_color('white')
        ax.spines['right'].set_color('white')
        ax.spines['left'].set_color('white')
        fig.autofmt_xdate()
        canvas = FigureCanvasTkAgg(fig, master=frame)  # A tk.DrawingArea.
        canvas.draw()
        toolbar = NavigationToolbar2Tk(canvas, frame, pack_toolbar=False)
        toolbar.update()
        toolbar.pack(side=tk.BOTTOM, fill=tk.X)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        frame.place(x=0, y=50)

    def create_gauge(self, container, title):
        labels=['Estable','Variación','Inestable','Falla']
        colors=['#3C33FF','#FFF033','#F6810B','#FF0000']
        frame = ttk.Frame(container)
        frame.columnconfigure(0, weight=1)
        frame.winfo_name = 'GAUGE'
        fig, ax = gauge(labels, colors, 3, title)
        fig.patch.set_facecolor('black')
        canvas = FigureCanvasTkAgg(fig, master=frame)  # A tk.DrawingArea.
        canvas.draw()
        toolbar = NavigationToolbar2Tk(canvas, frame, pack_toolbar=False)
        toolbar.update()
        toolbar.pack(side=tk.BOTTOM, fill=tk.X)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        frame.place(x=0, y=50)


    def gauge(self):
        self.destroy_widgets()
        self.wm_title("YoDiagnostico | Gauge")
        self.create_gauge(self, 'Estado de la maquina')


    def channel_1(self):
        self.destroy_widgets()
        self.wm_title("YoDiagnostico | Canal 1")
        self.create_plot(self, self.prepared_data.__getattribute__('canal1'))

    
    def channel_4(self):
        self.destroy_widgets()
        self.wm_title("YoDiagnostico | Canal 2")
        self.create_plot(self, self.prepared_data.__getattribute__('canal2'))
    
    
    def channel_2(self):
        self.destroy_widgets()
        self.wm_title("YoDiagnostico | Canal 3")
        self.create_plot(self, self.prepared_data.__getattribute__('canal3'))
    
    
    def channel_3(self):
        self.destroy_widgets()
        self.wm_title("YoDiagnostico | Canal 4")
        self.create_plot(self, self.prepared_data.__getattribute__('canal4'))

    def show_config(self):
        print('Config clicked')