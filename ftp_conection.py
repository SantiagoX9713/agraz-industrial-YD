from time import sleep
from ftplib import FTP

def progress(percent=0, width=40):
    left = width * percent // 100
    right = width - left
    
    tags = "#" * left
    spaces = " " * right
    percents = f"{percent:.0f}% Progress"
    
    print("\r[", tags, spaces, "]", percents, sep="", end="", flush=True)


HOST = "localhost"
ftp = FTP()
ftp.connect(HOST)
ftp.login(user='Usuario FTP', passwd='123456')
print(ftp.retrlines('LIST'))
for i in range(101):
    progress(i)
    sleep(0.05)

with open('DDSMuestras.csv', 'wb') as fp:
    ftp.retrbinary('RETR DDSMuestras.csv', fp.write)
ftp.close()
