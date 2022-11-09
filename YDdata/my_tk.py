from functools import partial
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


def create_plot(container, prepared_data):
    # for widget in container.winfo_children():
    #     widget.destroy()
    
    frame = ttk.Frame(container)
    frame.columnconfigure(0, weight=1)
    frame.winfo_name = 'PLOTER'
    fig = plt.Figure(figsize=(7,5), dpi=80)
    fig.patch.set_facecolor('black')
    ax = fig.add_subplot()
    df2 = prepared_data[['Time','Solt Mec']]
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
    canvas = FigureCanvasTkAgg(fig, master=frame)  # A tk.DrawingArea.
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas, frame, pack_toolbar=False)
    toolbar.update()
    toolbar.pack(side=tk.BOTTOM, fill=tk.X)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    frame.place(x=0, y=50)



class MyTk(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure(bg='black')
        self.state("zoomed")
        self.wm_title("YoDiagnostico")
        
        barra_menus = tk.Menu()
        barra_menus.winfo_name = 'MENU'
        menu_archivo = tk.Menu(barra_menus, tearoff=False)
        barra_menus.add_cascade(menu=menu_archivo, label="Principal")
#        menu_archivo.add_command(label="Salir", command=self.destroy)
        menu_archivo.add_command(label="Canal 1", command=self.channel_1)
        menu_archivo.add_command(label="Canal 4", command=self.channel_4)
        menu_archivo.add_command(label="Salir", command=self.destroy)
        self.config(menu=barra_menus)
        
    
    def channel_1(self):
        for widget in self.winfo_children():
            if widget.winfo_name != 'MENU':
                print(widget.winfo_name)
                widget.destroy()
        print('Channel 1')

    def channel_4(self):
        for widget in self.winfo_children():
            widget.destroy()
        print('Channel 4')


class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Combobox")
        self.combo = ttk.Combobox(
            self,
            values=["Python", "C", "C++", "Java"]
        )
        self.combo.bind("<<ComboboxSelected>>", self.selection_changed)
        self.combo.place(x=50, y=50)
        main_window.config(width=300, height=200)
        self.place(width=300, height=200)
    def selection_changed(self, event):
        selection = self.combo.get()
        messagebox.showinfo(
            title="Nuevo elemento seleccionado",
            message=selection
        )


def data_selector(container):
    def selection_changed(event):
        selection = combo.get()
        messagebox.showinfo(
        title="Nuevo elemento seleccionado",
        message=selection
        )
        print(combo.get())

        for widget in container.winfo_children():
            print(widget.winfo_name)
        
    frame = ttk.Frame(container)
    frame.columnconfigure(0, weight=1)
    frame.winfo_name = 'SELECTOR'
    combo_values = ['canal1', 'canal2', 'canal3', 'canal4']
    combo = ttk.Combobox(master=frame, state='readonly', values=combo_values)
    combo.bind("<<ComboboxSelected>>", selection_changed)
    combo.winfo_name = 'COMBOBOX'
    combo.pack()
    return frame