import datetime

date = datetime.date(2025,3,16)
print(date)

today = datetime.date.today()
print(today)

time = datetime.time(12, 30, 0)
print(time)

now = datetime.datetime.now()
now = now.strftime("%H:%M:%S %d/%m/%Y")
print(now)