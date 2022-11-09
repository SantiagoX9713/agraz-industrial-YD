try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


from YDdata.get_csv import GetCsvFtp, DfFromCsv
from YDdata.my_tk import MyTk, create_plot, data_selector

# def filter_by_time(df,h):
#     now = datetime.now()
#     print(now)
#     df = df[(canal1.Time > (now - timedelta(hours=h)).time())]
#     return df

# df = filter_by_time(canal1, 10)
getter = GetCsvFtp()
getter.conect()
prepared_data = DfFromCsv()
root = MyTk()
# channel_selector = data_selector(root)
# channel_selector.place(x=0, y=0)
create_plot(root, prepared_data.__getattribute__('canal1'))
# rec.place(x=0, y=50)
root.mainloop()
