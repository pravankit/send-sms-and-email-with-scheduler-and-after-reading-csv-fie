import datetime as dt
import pytz

dt1 = dt.datetime.now(pytz.timezone("US/Eastern"))
dt11 =dt1.strftime("%d-%m-%Y")
print(dt11)
dt2 = dt.datetime.now(pytz.timezone("Asia/Kolkata"))
dt22 =dt2.strftime("%d-%m-%Y")
print(dt22)