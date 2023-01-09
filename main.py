from YDdata.get_csv import GetCsvFtp
from YDdata.my_tk import MyTk
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

# def filter_by_time(df,h):
#     now = datetime.now()
#     print(now)
#     df = df[(canal1.Time > (now - timedelta(hours=h)).time())]
#     return df

# df = filter_by_time(canal1, 10)
getter = GetCsvFtp()
getter.conect()

root = MyTk()
root.mainloop()
