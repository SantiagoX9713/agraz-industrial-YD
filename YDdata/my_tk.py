from  matplotlib import pyplot as plt, dates
import tkinter as tk
from tkinter import ttk, Toplevel, Button, Checkbutton, IntVar, StringVar
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from .get_csv import DfFromCsv
from .gauge_test import gauge
from PIL import ImageTk, Image
import json


class MyTk(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure(bg='black')
        # self.state("zoomed")
        self.wm_title("YoDiagnostico")
        self.geometry("1500x750")
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
        menu_config.add_command(label="Configuración",
                                command=self.show_config)

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

    def create_plot(self, container, prepared_data, coords):
        # for widget in container.winfo_children():
        #     widget.destroy()

        frame = ttk.Frame(container)
        frame.columnconfigure(0, weight=1)
        frame.winfo_name = 'PLOTER'
        
        fig = plt.Figure(figsize=(12, 6), dpi=100)
        t = prepared_data['Time'][0:10].astype(str)
        ax = fig.add_subplot()
        line, = ax.plot(t, prepared_data['Solt Mec'][0:10])
        ax.set_xlabel("time [s]")
        ax.set_ylabel("f(t)")
        ax.set_xticks(ax.get_xticks(), rotation = 45)        
        # fig = plt.Figure(figsize=(10, 5), dpi=100)
        # fig.patch.set_facecolor('black')
        # ax = fig.add_subplot()
        # df = prepared_data[['Time', 'Solt Mec']][0:20].set_index(prepared_data['Time'][0:20])
        # #df.set_index(prepared_data['Date_Time'][0:10])
        # # colors = ["red" if i > 2.72 else "yellow" for i in df['Solt Mec']]
        # df.plot.line(legend=True, ax=ax, fontsize=8, grid=True)
        # # ax.axhline(y=2.81, color='r', linestyle='-')
        # # ax.axhline(y=2.70, color='b', linestyle='-')
        # # ax.set_title('Solturas Mecánicas')
        # # ax.set_ylim([2.6,2.85])
        # ax.set_facecolor('black')
        # [t.set_color('white') for t in ax.xaxis.get_ticklines()]
        # [t.set_color('white') for t in ax.xaxis.get_ticklabels()]
        # [t.set_color('white') for t in ax.yaxis.get_ticklines()]
        # [t.set_color('white') for t in ax.yaxis.get_ticklabels()]
        # ax.spines['bottom'].set_color('white')
        # ax.spines['top'].set_color('white')
        # ax.spines['right'].set_color('white')
        # ax.spines['left'].set_color('white')
        # #ax.xaxis.set_major_formatter(dates.DateFormatter('%H:%M:%S'))
        # #fig.autofmt_xdate()
        canvas = FigureCanvasTkAgg(fig, master=frame)  # A tk.DrawingArea.
        canvas.draw()
        toolbar = NavigationToolbar2Tk(canvas, frame, pack_toolbar=False)
        toolbar.update()
        toolbar.pack(side=tk.BOTTOM, fill=tk.X)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        frame.place(coords)

    def create_gauge(self, container, title):
        labels = ['Estable', 'Variación', 'Inestable', 'Falla']
        colors = ['#3C33FF', '#FFF033', '#F6810B', '#FF0000']
        frame = ttk.Frame(container)
        frame.columnconfigure(0, weight=1)
        frame.winfo_name = 'GAUGE'
        gauge(labels, colors, 3, title)
        img = ImageTk.PhotoImage(Image.open("gauge.png"))
        label = ttk.Label(frame, image=img)
        label.pack()
        print('PNG generated')
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
        # Aquí va la nueva función para renderear los charts
        # self.destroy_widgets()
        def restart_tk_widgets():
            pass

        
        def save_config():
            # Abrir y guardar archivos
            config_file2 = open('YDdata/config.json', 'r')
            config_json2 = json.load(config_file2)
            config_file2.close()
            display_charts = [
                {
                    "chart1": bool(chart1.get()),
                    "chart2": bool(chart2.get()),
                    "chart3": bool(chart3.get()),
                    "chart4": bool(chart4.get())
                }
            ]
            users = [
                {
                    "user": user,
                    "password": password
                }
            ]
            config_json2['display_charts'] = display_charts
            config_file = open('YDdata/config.json', 'w')
            json.dump(config_json, config_file, indent=4)
            config_file.close()
            restart_tk_widgets()


        # Config for second window
        x = self.winfo_x()
        y = self.winfo_y()
        newWindow = Toplevel(self)
        newWindow.title("Configuración")
        newWindow.geometry("600x300")
        newWindow.geometry("+%d+%d" % (x+200, y+200))
        newWindow.wm_transient(self)
        #  Variables for JSON
        
        config_file1 = open('YDdata/config.json', 'r')
        config_json1 = json.load(config_file1)
        config_file1.close()
        user = StringVar(value=config_json1)
        password = StringVar()
        chart1 = IntVar(value=int(config_json1["display_charts"][0]["chart1"]))
        chart2 = IntVar(value=int(config_json1["display_charts"][0]["chart2"]))
        chart3 = IntVar(value=int(config_json1["display_charts"][0]["chart3"]))
        chart4 = IntVar(value=int(config_json1["display_charts"][0]["chart4"]))
        # Checkboxes
        check1 = Checkbutton(
            newWindow,
            cnf={
                'text': 'Chart 1',
                'offvalue': False,
                'onvalue': True,
                'variable': chart1
            }
        ).place(x=150, y=50)
        check2 = Checkbutton(
            newWindow,
            cnf={
                'text': 'Chart 2',
                'offvalue': False,
                'onvalue': True,
                'variable': chart2
            }
        ).place(x=400, y=50)
        check3 = Checkbutton(
            newWindow,
            cnf={
                'text': 'Chart 3',
                'offvalue': False,
                'onvalue': True,
                'variable': chart3
            }
        ).place(x=150, y=150)
        check4 = Checkbutton(
            newWindow,
            cnf={
                'text': 'Chart 4',
                'offvalue': False,
                'onvalue': True,
                'variable': chart4
            }
        ).place(x=400, y=150)
        # Button for save the config
        btn = Button(newWindow,
                     text="Guardar Configuración",
                     command=save_config).place(x=230, y=200)
