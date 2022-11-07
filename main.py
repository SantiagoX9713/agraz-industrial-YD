try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
from YDdata.get_csv import get_csv_ftp, df_from_csv
from YDdata.my_tk import my_tk, create_plot, data_selector

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
channel_selector = data_selector(root)
channel_selector.place(x=0, y=0)
rec = create_plot(root, prepared_data.__getattribute__('canal1'))
rec.place(x=0, y=50)

root.mainloop()