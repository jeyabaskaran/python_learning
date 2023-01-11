import datetime

x=datetime.datetime.now()
print(x.year, x.month , x.minute, x.hour, x.strftime('%d-%m-%Y %H:%M:%S'))  #date formater



y=datetime.datetime(2022,1,11)
print(y, y.strftime('%A'))
