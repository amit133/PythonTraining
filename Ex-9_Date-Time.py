import time

ticks = time.time()
print("Number of ticks since 00:00:00, 01-Jan-1970: ", ticks)
print(time.localtime())
localtime = time.localtime(time.time())
print("Local current time: ", localtime)

print('We are in the year: ', localtime.tm_year)

#print formatted time
print(time.asctime(localtime))

## Calendar
import calendar

cal = calendar.month(2016, 2)
print(cal)

## datetime
import datetime

print("Earliest: ", datetime.time.min) # prints Earliest:  00:00:00
print("Latest: ", datetime.time.max) # prints Latest:  23:59:59.999999
print('Resolution', datetime.time.resolution) # prints Resolution 0:00:00.000001

for m in [1, 0, 0.1, 0.6]:
    try:
        # TODO: why do we error when we use {02.1f} instead of {:02.1f} in print
        print('{:02.1f} :'.format(m), datetime.time(0, 0, 0, microsecond = m))
    except TypeError as err:
        print('Error:', err)


print('Day of the week: ', datetime.date.today().strftime("%A"))

