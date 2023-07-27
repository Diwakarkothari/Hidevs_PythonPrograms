
from _datetime import datetime,timedelta
import pytz

"""dt_local=datetime.now()
print("Current location time: " ,dt_local)
dt_utc=datetime.now(pytz.utc)
print("utc -> ",dt_utc)
q=datetime.now(pytz.timezone('Asia/Kolkata'))
print(q)  #time of india = utc + 5:30
print(q.tzname())
print(q.utcoffset())
dt_us_central=dt_utc.astimezone(pytz.timezone("US/Central"))  #coverting utc to us central
print("Us Time-> ",dt_us_central )

#converting us central to india
dt_india=dt_us_central.astimezone(pytz.timezone("Asia/Kolkata"))
print("India ->  ",dt_india)"""


def check_tz(tz):
    try:
        pytz.timezone(tz)
        return True
    except pytz.exceptions.UnknownTimeZoneError:
        return False

#time_format='%d-%m-%y  %H:%M'
print("Enter the first timezone")
tz1=input()
z1=check_tz(tz1)
if z1==False:
    while z1!=True:
        print("Enter valid timezone")
        tz1=input()
        z1=check_tz(tz1)

dt1=datetime.now(pytz.timezone(tz1))
print("date time in first timezone ",dt1)
dif=timedelta(minutes=30)


print("Enter the second timezone")
tz2=input()
z2=check_tz(tz2)
if z2==False:
    while z2!=True:
        print("Enter valid timezone")
        tz2=input()
        z2=check_tz(tz2)

dt2=datetime.now(pytz.timezone(tz2))
print("date time in second timezone ",dt2)

#setting the duration to talk
start_time=dt1.replace(hour=10,minute=0,second=0)
end_time=dt1.replace(hour=18,minute=0,second=0)

if  start_time <= dt1 + dif <=end_time and start_time <= dt2 + dif <=end_time:
    print(f"They can talk for half n hour between {start_time} and {end_time}")
else:
    print(f"They cannot talk for half n hour between {start_time} and {end_time}")