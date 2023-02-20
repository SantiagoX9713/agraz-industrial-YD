from ftplib import FTP
from time import sleep
import pandas as pd
from datetime import datetime, timedelta
import json


class GetCsvFtp:

    def __init__(self) -> None:
        config_file = open('YDdata/config.json', 'r')
        self.chart_config = json.load(config_file)
        self.user = self.chart_config['ftp_config'][0]['user']
        self.password = self.chart_config['ftp_config'][0]['password']
        config_file.close()

    def conect(self):
        HOST = "localhost"
        ftp = FTP()
        ftp.connect(HOST)
        ftp.login(user=self.user, passwd=self.password)
        with open('./DDSMuestras.csv', 'wb') as fp:
            ftp.retrbinary('RETR DDSMuestras.csv', fp.write)
        ftp.close()


class DfFromCsv:
    
    def __init__(self):
    
        origin = pd.read_csv('./DDSMuestras.csv', delimiter='\t', encoding='utf-16', parse_dates=[['Date', 'Time']])
        columnas = ['Date_Time','Global','Desbalance','Desalineamiento','Solt Mec','Acc', 'Hd Env', 'Date', 'Time']
        self.canal1 = origin[['Date_Time', 'Ch 1 Global','Ch 1 Desbalance','Ch 1 Desalineamiento', 'Ch 1 Solt Mec', 'Ch 1 Acc', 'Ch 1 Hd Env']].copy()
        self.canal2 = origin[['Date_Time', 'Ch 2 Global','Ch 2 Desbalance','Ch 2 Desalineamiento', 'Ch 2 Solt Mec', 'Ch 2 Acc', 'Ch 2 Hd Env']].copy()
        self.canal3 = origin[['Date_Time', 'Ch 3 Global','Ch 3 Desbalance','Ch 3 Desalineamiento', 'Ch 3 Solt Mec', 'Ch 3 Acc', 'Ch 3 Hd Env']].copy()
        self.canal4 = origin[['Date_Time', 'Ch 4 Global','Ch 4 Desbalance','Ch 4 Desalineamiento', 'Ch 4 Solt Mec', 'Ch 4 Acc', 'Ch 4 Hd Env']].copy()
        
        self.canal1.set_index(pd.to_datetime(self.canal1['Date_Time']))
        self.canal1['Date'] = pd.to_datetime(self.canal1['Date_Time']).dt.date
        self.canal1['Time'] = pd.to_datetime(self.canal1['Date_Time']).dt.time
        self.canal1.columns = columnas
        
        self.canal2.set_index(pd.to_datetime(self.canal2['Date_Time']))
        self.canal2['Date'] = pd.to_datetime(self.canal2['Date_Time']).dt.date
        self.canal2['Time'] = pd.to_datetime(self.canal2['Date_Time']).dt.time
        self.canal2.columns = columnas
        
        self.canal3.set_index(pd.to_datetime(self.canal3['Date_Time']))
        self.canal3['Date'] = pd.to_datetime(self.canal3['Date_Time']).dt.date
        self.canal3['Time'] = pd.to_datetime(self.canal3['Date_Time']).dt.time
        self.canal3.columns = columnas
        
        self.canal4.set_index(pd.to_datetime(self.canal4['Date_Time']))
        self.canal4['Date'] = pd.to_datetime(self.canal4['Date_Time']).dt.date
        self.canal4['Time'] = pd.to_datetime(self.canal4['Date_Time']).dt.time
        self.canal4.columns = columnas