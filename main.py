from tkinter import ttk
import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from YDdata.get_csv import get_csv_ftp, df_from_csv
from YDdata.my_tk import my_tk, create_plot
from functools import partial
# def filter_by_time(df,h):
#     now = datetime.now()
#     print(now)
#     df = df[(canal1.Time > (now - timedelta(hours=h)).time())]
#     return df

# df = filter_by_time(canal1, 10)
getter = get_csv_ftp()
getter.conect()
prepared_data = df_from_csv()
root = my_tk()
# canvas = FigureCanvasTkAgg(root.fig, master=root)  # A tk.DrawingArea.
# canvas.draw()
# toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
# toolbar.update()
# toolbar.pack(side=tk.BOTTOM, fill=tk.X)
# canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
button_quit = tk.Button(master=root, text="Quit", command=root.destroy)
button_quit1 = tk.Button(master=root, text="Refresh", command=partial(root.reset_data, prepared_data))
button_quit.pack(side=tk.BOTTOM)
button_quit1.pack(side=tk.RIGHT)
rec = create_plot(root, prepared_data)
rec.pack(side=tk.TOP)
# rec.grid(column=0, row=0)
#button_quit = ttk.Button(root, text="Quit", command=root.destroy)
#button_quit1 = ttk.Button(root, text="Refresh", command=partial(root.reset_data, prepared_data))
#button_quit.grid(column=0, row=1)
#button_quit1.grid(column=0, row=2)

root.mainloop()